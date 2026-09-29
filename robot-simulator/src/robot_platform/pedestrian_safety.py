"""Opt-in person avoidance using delivered observations, never physics truth."""
from copy import deepcopy
import math
from .navigation import radius


class PedestrianSafety:
    VERSION='observed-pedestrian-avoidance-v1'

    def __init__(self, owner):
        self.owner=owner;self.config=owner.policy.pedestrian_avoidance
        self.states={}

    def report(self,rid,time,mode,reason,**values):
        state=self.states.setdefault(rid,dict(mode=None,blocked_since=None,last_replan=-math.inf,failed=False))
        if state['mode']!=mode:
            self.owner.emit('pedestrian_avoidance',rid,reason,dict(previous=state['mode'],mode=mode,**values))
            state['mode']=mode
        result=dict(version=self.VERSION,mode=mode,reason=reason,assessed_at=time,
                    desired_clearance_m=self.config.desired_clearance_m,
                    blocked_since=state['blocked_since'],blocked_seconds=time-state['blocked_since'] if state['blocked_since'] is not None else 0.,
                    sensor_model='ideal_visible_person_tracker_v1; sampled, delayed, noisy, occlusion gated',**values)
        self.owner.robot_states[rid]['pedestrian_avoidance']=result
        return result

    def read(self,rid,obs,time):
        if not isinstance(obs,dict):return None,'사람 회피에 사용할 로봇 관측 없음'
        stamp=obs.get('sampled_at')
        if not isinstance(stamp,(int,float)) or not math.isfinite(stamp) or stamp>time or time-stamp>self.owner.policy.stale_after:
            return None,'사람 관측 지연: 정지 후 새 관측 대기'
        try:
            values=[obs['pose'][key] for key in ('x','y','z','yaw')]+list(obs['velocity'])
            if len(obs['velocity'])!=3 or not all(isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) for v in values):
                raise ValueError()
        except (KeyError,TypeError,ValueError,OverflowError):return None,'사람 회피에 사용할 위치·속도 관측 오류'
        scan=obs.get('sensors',{}).get('pedestrians')
        if not isinstance(scan,dict) or scan.get('model')!='ideal_visible_person_tracker_v1' or not scan.get('enabled'):
            return None,'사람 관측 센서가 비활성입니다. 거리 센서를 켜고 다시 실행하세요'
        if scan.get('sampled_at')!=stamp:
            return None,'사람 관측과 로봇 관측 시각 불일치'
        people=scan.get('people')
        if not isinstance(people,list):return None,'사람 관측 형식 오류'
        floor=self.owner._floor(obs['pose']['z']);result=[]
        for person in people:
            try:
                p,v=person['position'],person['velocity'];r=person['radius']
                if len(p)!=3 or len(v)!=3 or not all(math.isfinite(x) for x in (*p,*v,r)) or r<=0:raise ValueError()
            except (KeyError,TypeError,ValueError,OverflowError):return None,'사람 관측 수치 오류'
            if person.get('floor_id')!=floor:continue
            result.append(person)
        return result,None

    def detour(self,rid,obs,time,people):
        owner=self.owner;robot=owner.robots[rid];state=owner.robot_states[rid]
        # Preserve fixed guides and cabin boarding/alighting. A supported
        # cooperative load can detour on its current floor to the SAME approved
        # rendezvous/staging point; leases, custody and task order never change.
        if robot.model_id in ('agv','arm') or state['status'] not in ('working','manual','cooperating'):
            return False
        task=owner.tasks.get(state['task_id'])
        execution=None; approach_suffix=[]
        if task and task['spec'].cooperation:
            execution=owner.cooperative.executions.get(task['id']) if owner.cooperative else None
            result=(execution or {}).get('result') or {}
            if (not execution or execution['terminal'] or execution['released'] or execution['committed']
                    or result.get('phase')!='transport' or not result.get('supported')):return False
            # Loading departure is deliberately straight inside the donor's
            # motion envelope. A detour turn here would be rejected by the
            # cooperative base controller and permanently strand the carrier.
            # Keep its route while the common person gate slows/stops it;
            # detours resume after observed clearance from the stationary arm.
            donor_id=execution['participants'].get('donor')
            donor=owner.last_observations.get(donor_id) if donor_id else None
            if donor and execution.get('loading_committed'):
                if time-donor['sampled_at']>owner.policy.stale_after:return False
                separation=math.hypot(obs['pose']['x']-donor['pose']['x'],obs['pose']['y']-donor['pose']['y'])
                if separation<radius(robot)+radius(owner.robots[donor_id])+owner.policy.safety_distance:
                    return False
            trip=state.get('trip')
            if trip and trip['phase']!='approach':return False
            goal=trip['staging'] if trip else result.get('navigation_target')
            if not trip:
                # Keep the approved straight-in handoff maneuver. Replanning
                # to XY alone drops its heading and can turn the loaded chassis
                # into the receiving arm. Once inside that maneuver, wait for
                # clearance instead of inventing a new close-range approach.
                route=execution.get('route') or []
                index=next((i for i,p in enumerate(route) if p.get('align')),None)
                if index is None:return False
                goal=route[index]
                approach_suffix=deepcopy(route[index:])
        else:
            if state.get('trip'):return False
            goal=task['spec'].destination.model_dump() if task else state.get('manual_target')
        if goal is None:return False
        floor=owner._floor(obs['pose']['z']);rr=radius(robot)
        disks=[(p['position'][0],p['position'][1],rr+p['radius']+self.config.desired_clearance_m+.12) for p in people]
        for other,reading in owner.last_observations.items():
            if other==rid or other not in owner.robots or time-reading['sampled_at']>owner.policy.stale_after:continue
            # Reserved handoff participants use the contact/range-gated
            # approach contract, whose rendezvous can lie inside arm reach.
            if execution and other in execution['participants'].values():continue
            if owner._floor(reading['pose']['z'])==floor:
                disks.append((reading['pose']['x'],reading['pose']['y'],rr+radius(owner.robots[other])+owner.policy.safety_distance))
        path=owner.planner.path(obs['pose'],goal,floor,robot,peer_disks=disks)
        if not path:return False
        if approach_suffix:
            path=[*path[:-1],*approach_suffix]
        state['path']=path
        if execution:execution['route']=path
        if task:task['progress_at']=time
        owner.emit('pedestrian_replan',rid,'관측된 사람을 피해 같은 목표로 우회',dict(path=deepcopy(path),sampled_at=obs['sampled_at'],person_ids=[p['id'] for p in people]))
        return True

    def apply(self,rid,obs,time,command):
        if self.config is None:return command
        c=self.config;owner=self.owner;robot=owner.robots[rid];robot_state=owner.robot_states[rid]
        state=self.states.setdefault(rid,dict(mode=None,blocked_since=None,last_replan=-math.inf,failed=False))
        stopped=dict(command,v=0.,w=0.)
        # A previous bounded failure requires explicit recovery, never silent
        # restart after a person disappears or a different task is assigned.
        if state['failed']:
            self.report(rid,time,'blocked_failed','보행자 통로 차단 종료: 경로를 확인하고 운영 재개를 요청하세요')
            return stopped
        people,error=self.read(rid,obs,time)
        if error:
            if robot_state['status'] in ('working','manual','charging'):robot_state['reason']=error
            self.report(rid,time,'observation_hold',error,sampled_at=obs.get('sampled_at') if isinstance(obs,dict) else None)
            return stopped
        p=obs['pose'];rr=radius(robot);age=time-obs['sampled_at']
        velocity=math.hypot(*obs['velocity'][:2]);latency=age+robot.sensors.communication_delay+1/owner.project.physics.orchestration_hz
        effective_stop=max(c.stop_distance_m,c.desired_clearance_m+velocity*latency+velocity*velocity/(2*c.braking_deceleration_m_s2))
        effective_slow=max(c.slowdown_distance_m,effective_stop+.5)
        vx,vy=command['v']*math.cos(p['yaw']),command['v']*math.sin(p['yaw'])
        heading=(math.cos(p['yaw']),math.sin(p['yaw']))
        if command['v']<0:heading=(-heading[0],-heading[1])
        hazards=[];clearances=[]
        for person in people:
            dx,dy=person['position'][0]-p['x'],person['position'][1]-p['y']
            distance=math.hypot(dx,dy);clearance=distance-rr-person['radius'];clearances.append(clearance)
            rvx,rvy=person['velocity'][0]-vx,person['velocity'][1]-vy
            speed2=rvx*rvx+rvy*rvy
            closest_time=max(0.,min(2.,-(dx*rvx+dy*rvy)/speed2)) if speed2>1e-12 else 0.
            closest=math.hypot(dx+rvx*closest_time,dy+rvy*closest_time)-rr-person['radius']
            front=dx*heading[0]+dy*heading[1]>0
            lateral=abs(dx*heading[1]-dy*heading[0])
            in_lane=front and lateral<rr+person['radius']+c.desired_clearance_m
            crossing=closest<c.desired_clearance_m and closest_time>0
            # A nearby person can step into the body envelope from the side
            # while the robot coasts during an observation/control cycle.
            # Brake inside the effective stop margin regardless of heading.
            if clearance<effective_stop or ((in_lane or crossing) and clearance<effective_slow):
                hazards.append((clearance,person,closest,closest_time))
        common=dict(sampled_at=obs['sampled_at'],observed_min_clearance_m=min(clearances,default=None),
                    effective_stop_distance_m=effective_stop,visible_person_ids=[p['id'] for p in people])
        if not hazards:
            resumed=state['blocked_since'] is not None or state['mode'] in ('slowing','yielding','waiting','detouring','detour_align')
            state['blocked_since']=None
            state['encounter_since']=None
            self.report(rid,time,'resuming' if resumed else 'clear','사람 통행 후 경로 재개' if resumed else '관측된 사람과 진행 공간 확보',**common)
            return command
        clearance,person,closest,closest_time=min(hazards,key=lambda row:row[0])
        intended_motion=abs(command['v'])>1e-9 or abs(command['w'])>1e-9 or bool(robot_state['path'])
        active=robot_state['status'] in ('working','manual','charging','cooperating','recovering') and intended_motion
        held=state['mode'] in ('yielding','waiting','detouring','detour_align')
        threshold=max(effective_stop,c.resume_distance_m if held else 0.)
        imminent=closest<c.desired_clearance_m and 0<closest_time<=latency+velocity/c.braking_deceleration_m_s2+.3
        must_stop=clearance<threshold or imminent
        if not active or not must_stop:state['blocked_since']=None
        if active and must_stop and state['blocked_since'] is None:state['blocked_since']=time
        if active and state.get('encounter_since') is None:state['encounter_since']=time
        if not active:state['encounter_since']=None
        duration=time-state['blocked_since'] if state['blocked_since'] is not None else 0.
        encounter=time-state['encounter_since'] if state.get('encounter_since') is not None else 0.
        common.update(person_id=person['id'],predicted_min_clearance_m=closest)
        if active and duration>=c.blocked_timeout_s:
            reason='보행자 통로 차단 시간 초과: 통로와 목적지를 확인한 뒤 운영 재개를 요청하세요'
            if robot_state['task_id']:owner._failure(robot_state['task_id'],time,reason,allow_retry=False)
            owner.charging.interrupt(rid,reason)
            robot_state.update(status='recovery_required',reason=reason,path=[],operator_hold=True,command_epoch=robot_state['command_epoch']+1)
            state['failed']=True
            self.report(rid,time,'blocked_failed',reason,**common)
            return stopped
        if active and c.strategy=='detour' and encounter>=c.replan_after_s and time-state['last_replan']>=c.replan_after_s:
            state['last_replan']=time
            if self.detour(rid,obs,time,people):
                self.report(rid,time,'detouring','사람 우회 경로 준비: 새 경로로 재출발',**common)
                return stopped
        if must_stop:
            # Rotation stays inside the same circumscribed footprint. Permit
            # an approved detour heading at rest only with observed clearance.
            align=c.strategy=='detour' and bool(robot_state['path']) and clearance>c.desired_clearance_m and not imminent and abs(command['v'])<1e-9 and abs(command['w'])>0
            mode='detour_align' if align else 'waiting' if duration>=c.replan_after_s else 'yielding'
            reason='사람과 여유를 유지하며 제자리 우회 방향 정렬' if align else '보행자 통행 대기: 거리 확보 후 재출발'
            if active:robot_state['reason']=reason
            self.report(rid,time,mode,reason,**common)
            return dict(command,v=0.) if align else stopped
        cap=min(c.max_near_speed_m_s,abs(command['v']))
        self.report(rid,time,'slowing','사람 근처 감속',**common)
        return dict(command,v=math.copysign(cap,command['v']))

    def resume(self,rid):
        self.states.pop(rid,None)
