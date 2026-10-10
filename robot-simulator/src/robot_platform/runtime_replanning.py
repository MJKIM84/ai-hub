"""Bounded, separately approved changes to a paused live run; never reconstruct it.

Cargo and already-started tasks retain their executor/custody. Reassignment is
limited to not-yet-started empty patrols and the same executable robot model.
"""
from copy import deepcopy
import hashlib
import json
import time
from uuid import uuid4


def state_hash(session):
    value=dict(run_id=session.run_id,time=session.time,project=session.project.model_dump(),
               tasks=session.orchestrator.task_rows(),faults=session.robot_faults,
               facilities=session.facility_faults,custody=session.item_custody)
    return hashlib.sha256(json.dumps(value,sort_keys=True,default=str).encode()).hexdigest()


class RuntimeReplanning:
    def __init__(self):
        self.proposals={}
        self.receipts={}

    def prepare(self, session, task_id, wait_seconds=15):
        if session.status not in ('running','paused'):
            raise ValueError('진행 또는 일시 정지된 실행에서만 재계획할 수 있습니다')
        owner=session.orchestrator
        record=owner.tasks.get(task_id)
        if record is None:raise ValueError('현재 실행에 없는 작업입니다')
        if record['status'] in ('completed','cancelled','skipped'):
            raise ValueError('종료한 작업을 재계획하지 않습니다')
        if sum(r['run_id']==session.run_id for r in self.receipts.values())>=3:
            raise ValueError('이 실행의 재계획 3회 상한에 도달했습니다. 실행 기록을 검토하세요')
        session.status='paused'
        task=record['spec']
        options=[];excluded=[]
        if record['status']!='failed':
            options.append(dict(id='wait',kind='wait',label=f'현재 배정 유지 · 최대 {wait_seconds:g}초 관측',
                changes=[],delay_seconds=wait_seconds,delay_basis='관측 시간 상한; 완료 예상 시간 아님'))
        original=owner.robots.get(task.preferred_robot or '')
        if (task.kind=='patrol' and not task.item_id and not task.cooperation
                and record['status'] in ('pending','waiting') and record['started_at'] is None and original):
            for robot in owner.robots.values():
                if robot.id==original.id:continue
                candidate=task.model_copy(update={'preferred_robot':robot.id})
                observation=session.observations.get(robot.id)
                reason=('기존 문서·실행 계약과 같은 모델만 지원' if robot.model_id!=original.model_id else
                    '로봇이 다른 작업·복구·정지 상태' if owner.robot_states[robot.id]['status']!='idle' else
                    '물품 소유 중' if robot.id in session.item_custody.values() else
                    owner._eligible(robot,candidate,observation,session.time))
                if not reason and owner._floor(observation['pose']['z'])!=task.floor_id:
                    reason='실행 중 재배정은 같은 층 순찰만 지원'
                route=None if reason else owner._task_route(robot,observation,candidate)
                if not reason and route is None:reason='현재 위치에서 유효한 경로 없음'
                if reason:
                    excluded.append(dict(robot_id=robot.id,reason=reason));continue
                options.append(dict(id='assign-'+robot.id,kind='reassign',robot_id=robot.id,
                    label=f'{robot.name}으로 미시작 순찰 재배정',
                    changes=[dict(field='preferred_robot',before=task.preferred_robot,after=robot.id)],
                    route=route,delay_seconds=None,delay_basis='현재 경로는 계산됨; 완료 시간은 미예측'))
        else:
            excluded.append(dict(robot_id=None,reason='시작된 작업·물품 업무는 소유권과 복구 예약을 유지합니다. 자동 역할 교체는 지원하지 않습니다.'))
        proposal=dict(id=uuid4().hex,run_id=session.run_id,task_id=task_id,source_hash=state_hash(session),
                      reason=record['reason'],options=options,excluded=excluded,created_at=time.time(),
                      expires_at=time.time()+300,wait_seconds=wait_seconds,status='awaiting_approval')
        self.proposals[proposal['id']]=proposal
        # Bound retained review state; old IDs expire explicitly.
        while len(self.proposals)>50:self.proposals.pop(next(iter(self.proposals)))
        session.emit('replan_proposed',task_id,'실행을 일시 정지하고 변경 대안을 준비했습니다',deepcopy(proposal))
        return deepcopy(proposal)

    def approve(self, session, proposal_id, option_id, request_id):
        if request_id in self.receipts:
            receipt=self.receipts[request_id]
            if (receipt['proposal_id'],receipt['option_id'],receipt['run_id'])!=(proposal_id,option_id,session.run_id):
                raise ValueError('같은 승인 요청 식별자를 다른 변경에 사용할 수 없습니다')
            return deepcopy(receipt)
        proposal=self.proposals.get(proposal_id)
        if not proposal or proposal['status']!='awaiting_approval':raise ValueError('유효한 미승인 대안이 없습니다')
        if (session.status!='paused' or time.time()>proposal['expires_at']
                or proposal['source_hash']!=state_hash(session)):
            raise ValueError('실행 상태가 변경되었거나 승인이 만료됐습니다. 대안을 다시 계산하세요')
        option=next((o for o in proposal['options'] if o['id']==option_id),None)
        if option is None:raise ValueError('서버가 검증한 대안만 승인할 수 있습니다')
        if sum(r['run_id']==session.run_id for r in self.receipts.values())>=3:
            raise ValueError('재계획 횟수 상한에 도달했습니다')
        if option['kind']=='reassign':
            record=session.orchestrator.tasks[proposal['task_id']]
            record['spec'].preferred_robot=option['robot_id']
            record['reason']='새 실행 변경 승인에 따라 재배정 대기'
            for source in (session.project,session.orchestrator.project):
                for task in source.tasks:
                    if task.id==proposal['task_id']:task.preferred_robot=option['robot_id']
        receipt=dict(proposal_id=proposal_id,option_id=option_id,run_id=session.run_id,
                     task_id=proposal['task_id'],source_hash=proposal['source_hash'],
                     changes=option['changes'],request_id=request_id,approved_at=time.time(),sim_time=session.time)
        self.receipts[request_id]=receipt;proposal['status']='approved'
        session.replan_watch=dict(task_id=proposal['task_id'],until=session.time+proposal['wait_seconds'])
        session.emit('replan_approved',proposal['task_id'],'새 실행 변경 승인 · 실제 상태에서 계속',deepcopy(receipt))
        session.status='running'
        return deepcopy(receipt)
