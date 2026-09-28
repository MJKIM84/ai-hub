"""Explicit recovery of retained cooperation leases through physical placement.

This coordinator reads delivered observations only. A failed business task stays
failed while recovery runs; an optional, bounded retry receives a new execution.
"""
from copy import deepcopy
import math
from uuid import uuid4


class CooperativeRecovery:
    def __init__(self, control):
        self.c, self.o = control, control.o
        self.requests = {}

    @staticmethod
    def active(execution):
        return execution.get('recovery',{}).get('status')=='running'

    def receipt(self, execution):
        return {key:deepcopy(value) for key,value in execution['recovery'].items()
                if key not in ('flow','result','stable_since')}

    def _stationary(self, execution, now, observations):
        for rid in execution['participants'].values():
            obs=observations.get(rid)
            if not self.c._valid_participant(rid,obs,now):return False
            if (math.sqrt(sum(v*v for v in obs['velocity']))>.04
                    or math.sqrt(sum(v*v for v in obs['angular_velocity']))>.08):return False
        return True

    def _proof(self, task_id, now, observations, recovery, report=None):
        actor=recovery['actor_id']
        if report is None:
            report=dict(task_id=task_id,item_id=self.o.tasks[task_id]['spec'].item_id,
                carrier_id=self.c.executions[task_id]['participants']['carrier'],receiver_id=actor,
                state='placed',sampled_at=observations.get(actor,{}).get('sampled_at'))
        proof=self.c._placement_proof(task_id,now,observations,actor_id=actor,
            destination=recovery['destination_world'],report=report)
        if proof:
            proof.update(recovery_id=recovery['recovery_id'],actor_id=actor)
        return proof

    def start(self, task_id, actor_id, destination, now, observations, *, request_id=None, retry=False, timeout=90.):
        from .domain import Pose
        from .recovery_workflow import RecoveryPlacement
        e=self.c.executions.get(task_id)
        if not e:raise ValueError('복구할 협업 실행이 없습니다')
        record=self.o.tasks[task_id];task=record['spec']
        item=next(i for i in self.o.project.items if i.id==task.item_id)
        if actor_id not in e['participants'].values() or self.o.robots[actor_id].model_id not in ('arm','mobile_manipulator'):
            raise ValueError('예약된 참여 팔을 복구 로봇으로 지정하세요')
        default=(task.source or item.pose) if actor_id==e['participants'].get('donor') else task.destination
        local=Pose.model_validate(destination) if destination is not None else default.model_copy(deep=True)
        if type(timeout) not in (int,float) or not math.isfinite(timeout) or not 0<timeout<=300:
            raise ValueError('복구 제한 시간은 0초 초과 300초 이하입니다')
        if type(retry) is not bool:raise ValueError('재시도 여부는 참/거짓이어야 합니다')
        fingerprint=dict(task_id=task_id,execution_id=e['id'],actor_id=actor_id,
            destination=local.model_dump(),retry=retry,timeout=timeout)
        if request_id is not None and (not isinstance(request_id,str) or not request_id.strip()):
            raise ValueError('복구 요청 ID는 비어 있지 않은 문자열이어야 합니다')
        request_id=request_id if request_id is not None else uuid4().hex
        if request_id in self.requests:
            old=self.requests[request_id]
            # Reassignment creates a new execution, but a lost response to the
            # original request must still return that original receipt.
            if any(old['request'][key]!=value for key,value in fingerprint.items() if key!='execution_id'):
                raise ValueError('같은 복구 요청 ID의 내용이 다릅니다')
            return deepcopy(old['receipt'])
        arm_contract=self.c._arm_contract(actor_id)
        if not e['terminal'] or e['released'] or self.active(e):
            raise ValueError('실패·취소 후 예약이 유지된 작업만 복구할 수 있습니다')
        if not self._stationary(e,now,observations):
            raise ValueError('모든 참여 로봇의 신선한 정상·정지 관측이 필요합니다')
        source=(task.source or item.pose)
        if retry and (actor_id!=e['participants'].get('donor') or
                any(abs(getattr(local,key)-getattr(source,key))>1e-6 for key in ('x','y','z'))):
            raise ValueError('재시도는 최초 상차 팔로 원래 출발 지점에 복구한 경우에만 가능합니다')
        if retry and (record['attempts']>task.retries or record.get('cooperative_retry_count',0)>=task.retries or
                (task.deadline is not None and now>=task.deadline)):
            raise ValueError('재시도 예산 또는 작업 기한이 남아 있지 않습니다')
        height=next(f.elevation for f in self.o.project.environment.floors if f.id==task.floor_id)
        target=local.model_dump();target['z']+=height
        r=dict(recovery_id=request_id,actor_id=actor_id,status='running',mode=None,started_at=now,
            destination=local.model_dump(),destination_world=target,retry=retry,timeout=timeout,
            original_status=record['status'],original_reason=record['reason'],flow=None,result=None,
            stable_since=None,custody_confirmed=False,phase='verify',reason='현재 물품과 참여자 상태를 재확인합니다')
        state=self.c.resources.snapshot()['items'][task.item_id]
        owner=state['owner'];carrier=e['participants']['carrier']
        if self._proof(task_id,now,observations,r):
            r['mode']='reconcile'
        else:
            feedback=observations[actor_id]['sensors'].get('manipulation',{}).get(task.item_id,{})
            if owner==carrier:
                if feedback.get('bilateral_contact') is not False or feedback.get('finger_contacts')!=[]:
                    raise ValueError('운반차와 팔의 공동 접촉 상태는 먼저 별도 복구 확인이 필요합니다')
                r['mode']='pickup'
            elif owner in (None,actor_id):
                if feedback.get('bilateral_contact') is not True:
                    raise ValueError('현재 물품의 양쪽 파지 또는 목적지 지지를 확인할 수 없습니다')
                r['mode']='held'
            else:raise ValueError('다른 팔이 소유한 물품을 지정 팔로 복구할 수 없습니다')
            opening,payload=0.,item.mass
            if r['mode']=='held':
                opening,payload=feedback.get('commanded_opening'),feedback.get('payload_estimate_kg')
                if (type(opening) not in (int,float) or not math.isfinite(opening) or not 0<=opening<=.1
                        or type(payload) not in (int,float) or not math.isfinite(payload) or payload<0):
                    raise ValueError('현재 로봇이 보고한 그리퍼·하중 보상 설정이 필요합니다')
            geometry=self.c.geometry[carrier]
            r['flow']=RecoveryPlacement(task_id,actor_id,carrier,task.item_id,item.mass,item.size.model_dump(),target,
                mode=r['mode'],timeout=timeout,grip_opening=opening,
                payload_estimate=payload,support_geometry=geometry,
                arm_geometry=arm_contract)
        self.c.resources.begin_recovery(e['id'],request_id,actor_id,now,expected_version=state['version'])
        e['recovery']=r;e['generation']+=1
        self.c.reports.pop(task_id,None)
        for rid in e['participants'].values():
            rs=self.o.robot_states[rid]
            rs.update(status='recovering',task_id=task_id,path=[],mode='stand',reason=r['reason'])
            rs['command_epoch']+=1
        self.o.robot_states[actor_id]['operator_hold']=False
        self.requests[request_id]=dict(request=fingerprint,receipt=self.receipt(e))
        record['recovery']=self.receipt(e)
        self.o.emit('cooperation_recovery_started',actor_id,'물품 복구 요청 수락; 기존 예약 유지',dict(task_id=task_id,**record['recovery']))
        return deepcopy(record['recovery'])

    def stop(self, task_id, now, reason, *, cancelled=False):
        e=self.c.executions.get(task_id)
        if not e or not self.active(e):return
        r=e['recovery'];r.update(status='cancelled' if cancelled else 'failed',reason=reason,completed_at=now)
        method=self.c.resources.cancel_recovery if cancelled else self.c.resources.fail_recovery
        method(e['id'],r['recovery_id'],reason,now=now)
        e['generation']+=1
        for rid in e['participants'].values():
            state=self.o.robot_states[rid];state['command_epoch']+=1
            state.update(status='recovery_required',task_id=None,path=[],mode='stand',reason=reason)
        self._record(task_id)
        self.o.emit('cooperation_recovery_failed',r['actor_id'],reason,dict(task_id=task_id,recovery_id=r['recovery_id'],resources_retained=True))

    def _record(self, task_id):
        e=self.c.executions[task_id];receipt=self.receipt(e)
        self.o.tasks[task_id]['recovery']=receipt
        self.requests[receipt['recovery_id']]['receipt']=deepcopy(receipt)

    def update(self, task_id, now, observations):
        e=self.c.executions[task_id];r=e['recovery'];record=self.o.tasks[task_id]
        task=record['spec'];actor=r['actor_id']
        commands=self.c._hold_arms(task_id,e)
        if not self._stationary(e,now,observations):
            self.stop(task_id,now,'복구 중 참여자 관측·정지·장애 조건 소실');return self.c._hold_arms(task_id,e)
        participants=set(e['participants'].values())
        if any(row['a']!=row['b'] and {row['a'],row['b']}<=participants and row['force']>5
               for rid in participants for row in observations[rid]['sensors']['contacts']):
            self.stop(task_id,now,'복구 참여 로봇 간 충돌');return self.c._hold_arms(task_id,e)
        if now-r['started_at']>r['timeout']:
            self.stop(task_id,now,'물품 복구 제한 시간 초과');return self.c._hold_arms(task_id,e)
        proof=None
        if r['mode']=='reconcile':
            proof=self._proof(task_id,now,observations,r)
            if proof:
                stamp=min(row['sampled_at'] for row in proof['participants'].values())
                if r['stable_since'] is None:r['stable_since']=stamp
                if stamp-r['stable_since']<.5:proof=None
            else:r['stable_since']=None
        else:
            result=r['flow'].update(now,observations[actor],observations[e['participants']['carrier']])
            r['result']=result;r['phase']=result['phase'];r['reason']=result['reason']
            envelope=dict(result,execution_id=e['id'],recovery_id=r['recovery_id'],actor_id=actor)
            intent=result.get('resource_intent') or {}
            try:
                if not r['custody_confirmed'] and intent.get('recovery_custody'):
                    state=self.c.resources.snapshot()['items'][task.item_id]
                    self.c.resources.observe_recovery_custody(e['id'],task.item_id,state['owner'],actor,now,envelope,
                        recovery_id=r['recovery_id'],expected_version=state['version'])
                    r['custody_confirmed']=True
            except ValueError as error:
                self.stop(task_id,now,'복구 소유 확인 실패: '+str(error))
            if result['status']=='failed':self.stop(task_id,now,result['reason']+': '+result['code'])
            action='recovery:'+result['phase']
            if e.get('action')!=action:e['generation']+=1;e['action']=action
            commands[actor]=dict(result,hold=result['hold'] or not self.active(e),task_id=task_id,
                generation=e['generation'],recovery_id=r['recovery_id'])
            if result['status']=='completed' and self.active(e) and r['custody_confirmed']:
                proof=self._proof(task_id,now,observations,r,result.get('report'))
        if proof and self.active(e):
            try:self.c.resources.recover(e['id'],now,proof)
            except ValueError:pass
            else:
                r.update(status='completed',phase='placed',completed_at=now,reason='복구 위치 지지·해제·안정 확인',evidence=proof)
                e['released']=True;e['generation']+=1
                for rid in e['participants'].values():
                    state=self.o.robot_states[rid];state['command_epoch']+=1
                    state.update(status='stopped' if state['operator_hold'] else 'idle',task_id=None,path=[],reason=r['reason'])
                    self.o.reservations.release_all(rid)
                record.setdefault('cooperation',{})['resources_retained']=False
                self.o.emit('cooperation_recovery_completed',actor,r['reason'],dict(task_id=task_id,
                    recovery_id=r['recovery_id'],duration_s=now-r['started_at'],failure_to_recovery_s=now-record['completed_at']))
                commands=self.c._hold_arms(task_id,e)
                if r['retry']:
                    if ((task.deadline is not None and now>=task.deadline) or record['attempts']>task.retries
                            or record.get('cooperative_retry_count',0)>=task.retries):
                        r['retry_result']='기한 또는 재시도 예산 소진으로 재배정하지 않음'
                    else:
                        record['cooperative_retry_count']=record.get('cooperative_retry_count',0)+1
                        record.setdefault('cooperative_attempt_history',[]).append(dict(execution_id=e['id'],
                            status=record['status'],reason=record['reason'],started_at=record['started_at'],
                            completed_at=record['completed_at'],recovery_id=r['recovery_id'],evidence=deepcopy(record.get('evidence'))))
                        record.update(status='pending',robot_id=None,started_at=None,completed_at=None,arrival_at=None,
                            reason='출발 물품 복구 완료; 새 실행으로 재시도 대기')
                        r['retry_result']='pending_new_execution'
        self._record(task_id)
        return commands
