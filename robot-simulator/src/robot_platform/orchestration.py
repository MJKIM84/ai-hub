"""Decision layer receives observations and static configuration only."""
from __future__ import annotations
from copy import deepcopy
import math

from .catalog import model_by_id
from .navigation import Planner,radius,path_clear_of_disks
from .facilities import FacilityManager
from .charging_control import ChargingControl
from .guided_route import DirectedRoute,GuidedRouteError,ARRIVAL_TOLERANCE_M
from .motion_limits import observed_limit, clamp_translation
from .pedestrian_safety import PedestrianSafety


def angle(x): return (x+math.pi)%(2*math.pi)-math.pi


class Reservations:
    def __init__(self):self.owners={};self.queues={}

    def request(self,resource,robot_id,capacity=1):
        owners=self.owners.setdefault(resource,[]);queue=self.queues.setdefault(resource,[])
        if robot_id in owners:return True
        if robot_id not in queue:queue.append(robot_id)
        while queue and len(owners)<capacity:owners.append(queue.pop(0))
        return robot_id in owners

    def release(self,resource,robot_id):
        for collection in (self.owners,self.queues):
            if robot_id in collection.get(resource,[]):collection[resource].remove(robot_id)

    def release_all(self,robot_id,keep_items=False):
        for resource in list(self.owners):
            if not (keep_items and resource.startswith("item:")):self.release(resource,robot_id)


class Orchestrator:
    def __init__(self,project,emit):
        self.project=project.model_copy(deep=True)
        self.policy=project.policy.model_copy(deep=True)
        self.emit=emit
        self.planner=Planner(project.environment)
        self.robots={r.id:r for r in project.robots}
        self.tasks={}
        for t in project.tasks:
            for number in range(t.quantity):
                task=t.model_copy(deep=True)
                task.id=t.id if number==0 else f"{t.id}~{number+1}"
                task.release_time+=number*t.interval
                self.tasks[task.id]=dict(spec=task,id=task.id,name=task.name,status="pending",robot_id=None,reason="발생 시각 대기",started_at=None,completed_at=None,attempts=0,progress_at=0,arrival_at=None)
        self.robot_states={r.id:dict(status="idle",task_id=None,path=[],reason="관측 대기",last_command={},mode="stand",manual_target=None,command_epoch=0,operator_hold=False) for r in project.robots}
        self.count={r.id:0 for r in project.robots}
        self.reservations=Reservations()
        self.last_observations={}
        self.facilities=FacilityManager(project)
        self.facility_intentions={}
        self.charging=ChargingControl(self)
        self.cooperative=None
        self.guided_progress={}
        self.guided_rejections={}
        self.guided_observation_valid={}
        self.pedestrian_safety=PedestrianSafety(self)

    def _reason(self,state,text):
        state["reason"]=text

    def _eligible(self,robot,task,obs,time):
        if obs is None or time-obs["sampled_at"]>self.policy.stale_after:return "관측 없음 또는 오래된 관측"
        if obs["fault"]!="none":return "장애 상태"
        if obs["battery"]<self.policy.charge_below:return "배터리 부족"
        spec=model_by_id(robot.model_id)
        if task.kind not in spec["capabilities"]:return "필요한 작업 능력 없음"
        if task.kind=="inspect":return "설비 점검 결과 판정 실행기 미검증"
        if task.preferred_robot and task.preferred_robot!=robot.id:return "지정 로봇 아님"
        if task.kind in ("load","unload","handoff","delivery","transport","retrieve"):
            return "물리 파지·적재·인계 실행기가 아직 검증되지 않음"
        floor=self._floor(obs["pose"]["z"])
        if task.floor_id!=floor and self._trip_plan(robot,obs,task) is None:return "사용 가능한 층간 시설 경로 없음"
        if robot.model_id=="agv" and not robot.agv_route:return "AGV 지정 경로 없음"
        if task.item_id:
            item=next(i for i in self.project.items if i.id==task.item_id)
            if item.mass>spec["max_payload"]:return "적재량 초과"
            if self.reservations.owners.get("item:"+task.item_id):return "물품의 다른 작업 또는 복구 예약 대기"
        if task.kind=="manipulate":
            if not task.item_id:return "조작할 물품을 지정해야 합니다"
            if not robot.sensors.item_tracking:return "물품 위치 관측 센서 없음"
            item=next(i for i in self.project.items if i.id==task.item_id)
            source=task.source or item.pose
            if item.floor_id!=task.floor_id:return "물품과 작업 층이 다릅니다"
            if any(math.hypot(p.x-obs["pose"]["x"],p.y-obs["pose"]["y"])>.73 for p in (source,task.destination)):
                return "현재 팔 작업 공간 밖: 이동 기반 접근 계획 필요"
        return None

    def _trip_plan(self,robot,obs,task,*,cargo=None):
        spec=model_by_id(robot.model_id)
        if spec["locomotion"]=="fixed" or robot.model_id=="agv" or task.kind=="manipulate":return None
        source=self._floor(obs["pose"]["z"])
        shape=deepcopy(spec["size"])
        for equipment in robot.equipment:
            for axis in ("x","y","z"):shape[axis]=max(shape[axis],getattr(equipment.size,axis))
        if robot.model_id=="mobile_manipulator":shape["x"]=shape["y"]=radius(robot)*2
        mass=spec["mass"]+robot.payload_mass+sum(e.mass for e in robot.equipment)
        if cargo is not None:
            mass += cargo.mass
            # Cargo fits the registered support footprint; include its height
            # and mass in lift admission without changing physical dimensions.
            shape['z'] += cargo.size.z
        candidates=[]
        for eid,e in self.facilities.elements.items():
            if not e.facility.automatic or e.facility.fault or mass>e.facility.max_load:continue
            if not {source,task.floor_id}<=set(e.facility.served_floors):continue
            if shape["y"]+.1>e.size.x or shape["x"]+.1>e.size.y or shape["z"]+.05>self.facilities.cabin_height:continue
            c,s=math.cos(e.pose.yaw),math.sin(e.pose.yaw)
            waiting=sum(ride.source_floor==source for ride in self.facilities.elevators[eid].queue)+sum(ride.source_floor==source for ride in self.facilities.elevators[eid].active)
            distance=e.size.y/2+radius(robot)+.4+waiting*(2*radius(robot)+self.policy.safety_distance+.3)
            staging=dict(x=e.pose.x+s*distance,y=e.pose.y-c*distance,z=self.facilities.floors[source],yaw=e.pose.yaw+math.pi/2)
            route=self._route(robot,obs,staging,source)
            exit_pose=dict(staging,z=self.facilities.floors[task.floor_id])
            onward=self._route(robot,{"pose":exit_pose},task.destination.model_dump(),task.floor_id)
            if route is None or onward is None:continue
            candidates.append((len(route)+len(onward),dict(elevator_id=eid,source_floor=source,dest_floor=task.floor_id,staging=staging,envelope=shape,mass=mass,route=route,phase="approach")))
        return min(candidates,key=lambda x:x[0])[1] if candidates else None

    def _trip_command(self,rid,state,obs,time):
        trip=state.get("trip")
        if not trip:return None
        ride=self.facilities.rides.get(trip["request_id"])
        if ride and ride.status=="completed":
            state.pop("trip",None)
            record=self.tasks.get(state["task_id"])
            if record is None:
                state.update(status="idle",path=[],reason="승강기에서 안전하게 하차 확인")
            else:
                task=record["spec"]
                goal=task.cooperation.carrier_destination if task.cooperation else task.destination
                path=self._route(self.robots[rid],obs,goal.model_dump(),task.floor_id)
                if path is None:
                    self._failure(task.id,time,"하차 후 목적지 경로 없음")
                else:state.update(path=path,reason="하차 후 목적지 이동")
            self.emit("elevator_exit",rid,"관측·바닥 접촉으로 하차 확인",dict(request_id=trip["request_id"]))
            return dict(v=0.,w=0.,mode="stand")
        if trip["phase"]=="approach" and state["status"]!="transit_recovery":return None
        intention=self.facility_intentions.get(rid,{"action":"wait"})
        state["reason"]=f"승강기 {intention['action']} · {trip['elevator_id']}"
        if intention["action"] not in ("board","exit"):return dict(v=0.,w=0.,mode="stand")
        target=intention["target"];pose=obs["pose"]
        dx,dy=target["x"]-pose["x"],target["y"]-pose["y"]
        forward=dx*math.cos(target["yaw"])+dy*math.sin(target["yaw"])
        lateral=-dx*math.sin(target["yaw"])+dy*math.cos(target["yaw"])
        sign=1 if forward>=0 else -1
        desired=target["yaw"]+sign*max(-.35,min(.35,lateral*1.5))
        error=angle(desired-pose["yaw"])
        speed=max(-.20,min(.20,forward*.65)) if abs(forward)>.025 else 0.
        if abs(error)>.35:speed=0.
        return dict(v=speed,w=max(-.3,min(.3,error)),mode="walk" if self.robots[rid].model_id=="spot" else "drive")

    def _floor(self,z):
        return min(self.project.environment.floors,key=lambda f:abs(z-f.elevation-.35)).id

    def _guided_plan(self,robot,obs,target,floor_id):
        try:
            if floor_id!=robot.floor_id or self._floor(obs['pose']['z'])!=floor_id:
                raise GuidedRouteError('same_floor_only')
            result=DirectedRoute([p.model_dump() for p in robot.agv_route]).path(obs['pose'],target)
            previous=obs['pose']
            for point in result['points']:
                dx,dy=point['x']-previous['x'],point['y']-previous['y']
                n=max(1,math.ceil(math.hypot(dx,dy)/.1))
                for i in range(n+1):
                    x,y=previous['x']+dx*i/n,previous['y']+dy*i/n
                    if self.planner.blocked(x,y,floor_id,robot):raise GuidedRouteError('blocked_segment')
                    for zone in self.project.environment.elements:
                        if zone.kind!='one_way' or zone.floor_id!=floor_id:continue
                        c,s=math.cos(zone.pose.yaw),math.sin(zone.pose.yaw)
                        lx,ly=c*(x-zone.pose.x)+s*(y-zone.pose.y),-s*(x-zone.pose.x)+c*(y-zone.pose.y)
                        if abs(lx)<=zone.size.x/2 and abs(ly)<=zone.size.y/2 and dx*c+dy*s < -1e-9:
                            raise GuidedRouteError('opposite_one_way')
                previous=point
            self.guided_rejections.pop(robot.id,None)
            return result
        except GuidedRouteError as error:
            self.guided_rejections[robot.id]=error.code
            return None

    def _observe_guided_progress(self,robot,obs,time):
        previous=self.guided_progress.get(robot.id,{})
        stamp=obs.get('sampled_at') if isinstance(obs,dict) else None
        if (not isinstance(stamp,(int,float)) or not math.isfinite(stamp) or stamp>time+1e-9
                or time-stamp>self.policy.stale_after or stamp<previous.get('sampled_at',-math.inf)):
            return False
        if stamp==previous.get('sampled_at'):
            return previous.get('on_route',False) and obs.get('pose')==previous.get('observed_pose')
        try:
            route=DirectedRoute([p.model_dump() for p in robot.agv_route])
            located=route.locate(obs['pose'])
            self.guided_progress[robot.id]=dict(located,sampled_at=stamp,closed=route.closed,on_route=True,observed_pose=deepcopy(obs['pose']))
            return True
        except GuidedRouteError as error:
            self.guided_progress[robot.id]=dict(previous,sampled_at=stamp,on_route=False,reason=error.code)
            return False

    def _route(self,robot,obs,target,floor_id):
        if robot.model_id=="agv":
            plan=self._guided_plan(robot,obs,target,floor_id)
            return plan['points'] if plan else None
        # A geometry-only return route can lead a freshly released carrier
        # back into a stationary arm's rotation envelope before the reactive
        # peer gate stops it. Include observed fixed peers while still outside
        # their envelope; close handoff departures retain _peer_detour's
        # straight, monotonically separating escape contract.
        disks=[]
        for rid,peer in self.last_observations.items():
            if (rid==robot.id or rid not in self.robots
                    or model_by_id(self.robots[rid].model_id)['locomotion']!='fixed'
                    or obs.get('sampled_at') is None
                    or abs(obs['sampled_at']-peer['sampled_at'])>self.policy.stale_after
                    or self._floor(peer['pose']['z'])!=floor_id):continue
            disks.append((peer['pose']['x'],peer['pose']['y'],
                          radius(robot)+radius(self.robots[rid])+self.policy.safety_distance))
        if disks and all(math.hypot(obs['pose']['x']-x,obs['pose']['y']-y)>r for x,y,r in disks):
            return self.planner.path(obs['pose'],target,floor_id,robot,peer_disks=disks)
        return self.planner.path(obs["pose"],target,floor_id,robot)

    def _task_route(self,robot,obs,task):
        if not task.approved_route:
            return self._route(robot,obs,task.destination.model_dump(),task.floor_id)
        if robot.model_id=='agv' or self._floor(obs['pose']['z'])!=task.floor_id:
            return None
        points=[pose.model_dump() for pose in task.approved_route]
        if math.hypot(points[-1]['x']-task.destination.x,points[-1]['y']-task.destination.y)>.001:
            return None
        return points if self.planner.path_clear(obs['pose'],points,task.floor_id,robot) else None

    def _peer_detour(self,robot,obs,target,floor_id,observations,time):
        """Observed local avoidance, including retreat after a close handoff.

        Never shrink a peer envelope. If a completed handoff left us inside
        its navigation clearance, only a statically checked, monotonically
        separating segment may exit it before normal full-clearance planning.
        AGVs retain their authored route. This does not move peers or cargo.
        """
        if robot.model_id=='agv':return None
        disks=[]
        for rid,peer in observations.items():
            if rid==robot.id or time-peer['sampled_at']>self.policy.stale_after:continue
            if self._floor(peer['pose']['z'])!=floor_id:continue
            disks.append((peer['pose']['x'],peer['pose']['y'],radius(robot)+radius(self.robots[rid])+self.policy.safety_distance))
        start=obs['pose']
        inside=[disk for disk in disks if math.hypot(start['x']-disk[0],start['y']-disk[1])<disk[2]]
        if not inside:
            return self.planner.path(start,target,floor_id,robot,peer_disks=disks)
        outside=[disk for disk in disks if disk not in inside]
        # Circle envelopes include in-place rotation; leave a margin larger
        # than waypoint arrival tolerance before turning back toward the goal.
        # A centerline moving away is not enough: rotating a rectangular
        # chassis at close range can sweep into the stationary arm. Preserve
        # the observed heading until the full rotation envelope is clear.
        # If forward departure is not separating, wait for intervention rather
        # than inventing an unsafe turn (reverse motion is not supported here).
        hx,hy=math.cos(start['yaw']),math.sin(start['yaw'])
        projections=[((start['x']-x)*hx+(start['y']-y)*hy,x,y,r) for x,y,r in inside]
        if any(dot<=0 for dot,x,y,r in projections):return None
        needed=max(-dot+math.sqrt(max(0.,dot*dot+(r+.31)**2-
            (start['x']-x)**2-(start['y']-y)**2)) for dot,x,y,r in projections)
        for distance in sorted(set((needed,.5,1.,1.5,2.))):
            if distance<needed or distance>2.:continue
            dx,dy=distance*hx,distance*hy
            escape=dict(x=start['x']+dx,y=start['y']+dy,z=start['z'],yaw=start['yaw'])
            if not self.planner.path_clear(start,[escape],floor_id,robot):continue
            if not path_clear_of_disks(start,[escape],outside):continue
            onward=self.planner.path(escape,target,floor_id,robot,peer_disks=disks)
            if onward is not None:return [escape,*onward]
        return None

    def _guided_remaining(self,robot,obs,path,target,floor_id):
        """An old next waypoint is never a license for a backward shortcut.

        The next directly reachable authored leg has exactly one destination.
        A behind waypoint on a loop needs other authored vertices; an open
        behind waypoint is unreachable. Replan to the actual final goal in
        either case, using this same approved observation and static route.
        """
        if path:
            next_leg=self._guided_plan(robot,obs,path[0],floor_id)
            if next_leg is not None:
                remaining=next_leg['points']
                # The route projection can remain just before a vertex which
                # this same observation already reached within arrival tolerance.
                # Do not reinsert that consumed vertex on every control cycle.
                while remaining and math.hypot(remaining[0]['x']-obs['pose']['x'],remaining[0]['y']-obs['pose']['y'])<ARRIVAL_TOLERANCE_M:
                    remaining.pop(0)
                if len(remaining)==1:return path
        return self._route(robot,obs,target,floor_id)

    def tick(self,time,observations):
        self.last_observations=deepcopy(observations)
        for task_id,record in self.tasks.items():
            deadline=record["spec"].deadline
            if record["status"]=="running" and deadline is not None and time>deadline:
                self._failure(task_id,time,"실행 중 작업 기한 초과",allow_retry=False)
        for rid,state in self.robot_states.items():
            obs=observations.get(rid)
            if self.robots[rid].model_id=='agv':
                self.guided_observation_valid[rid]=self._observe_guided_progress(self.robots[rid],obs,time)
            if obs is None or time-obs["sampled_at"]>self.policy.stale_after:
                if state["task_id"]:self._failure(state["task_id"],time,"관측 시간 초과")
                state.update(status="disconnected",reason="관측 없음 또는 통신 지연")
            elif obs["fault"]!="none" or obs["upright"]<.45 or obs["battery"]<=0:
                if state["task_id"]:self._failure(state["task_id"],time,"로봇 장애 또는 전도")
                state.update(status="fault",reason="장애 격리")
            elif state["status"] in ("disconnected","fault"):
                locked_item=any(rid in owners for resource,owners in self.reservations.owners.items() if resource.startswith("item:"))
                state.update(status="stopped" if state["operator_hold"] else "transit_recovery" if state.get("trip") else "recovery_required" if locked_item else "idle",reason="관측 연결 복구")
                self.emit("recovery",rid,"로봇 관측 복구",{})
        self.charging.prepare(time, observations)
        pending=[t for t in self.tasks.values() if t["status"] in ("pending","waiting")]
        pending.sort(key=lambda t:(t["spec"].deadline if self.policy.assignment=="deadline" and t["spec"].deadline is not None else -t["spec"].priority,t["spec"].release_time,t["id"]))
        for record in pending:
            task=record["spec"]
            condition=task.condition
            dependencies=task.predecessor_ids
            if condition:
                branch=self.tasks[condition.task_id]
                if branch['status']=='cancelled':
                    record.update(status='cancelled',reason='선행 작업 취소로 분기 실행 금지',completed_at=time)
                    self.emit('task_cancelled',task.id,record['reason'],{})
                    continue
                if branch['status'] not in ('completed','failed','skipped'):
                    record.update(status='waiting',reason='승인한 분기 조건 관측 대기')
                    continue
                if branch['status']!=condition.outcome:
                    record.update(status='skipped',reason='승인한 분기 조건과 실제 결과가 달라 실행하지 않음',completed_at=time)
                    self.emit('task_skipped',task.id,record['reason'],{'condition':condition.model_dump(),'observed':branch['status']})
                    continue
                dependencies=[d for d in dependencies if d!=condition.task_id]
            if any(self.tasks[d]['status']=='skipped' for d in dependencies):
                record.update(status='skipped',reason='선행 분기가 실행되지 않아 후속 단계 생략',completed_at=time)
                continue
            terminal=next((self.tasks[d] for d in dependencies
                           if self.tasks[d]["status"] in ("failed","cancelled")),None)
            if terminal:
                record.update(status="failed",reason=f"선행 작업 {terminal['name']} {terminal['status']}로 실행 불가",completed_at=time)
                self.emit("task_failed",task.id,record["reason"],{"predecessor_id":terminal['id']})
                continue
            if time<task.release_time:continue
            if task.deadline is not None and time>task.deadline:
                record.update(status="failed",reason="작업 기한 초과",completed_at=time);self.emit("task_failed",task.id,record["reason"],{});continue
            if any(self.tasks[d]["status"]!="completed" for d in dependencies):
                record.update(status="waiting",reason="선행 작업 완료 대기");continue
            if task.cooperation:
                if self.cooperative:self.cooperative.assign(record,time,observations)
                else:record.update(status='waiting',reason='협업 실행부 연결 대기')
                continue
            candidates=[];rejected={}
            for rid,robot in self.robots.items():
                if self.robot_states[rid]["status"]!="idle":continue
                obs=observations.get(rid)
                reason=self._eligible(robot,task,obs,time)
                if reason:rejected[rid]=reason;continue
                trip=self._trip_plan(robot,obs,task) if task.floor_id!=self._floor(obs["pose"]["z"]) else None
                route=trip["route"] if trip else [] if task.kind=="manipulate" else self._task_route(robot,obs,task)
                if route is None:rejected[rid]="몸체·장비 공간을 만족하는 경로 없음";continue
                energy=self.charging.task_budget(robot,task,obs,route,trip)
                if energy.get('energy_observation_valid') is False:
                    rejected[rid]='작업 에너지 판단에 사용할 현재 관측 없음: '+energy.get('reason','unknown')
                    record['energy_budget']=energy
                    continue
                if ((energy.get('energy_estimate_valid') is False or energy.get('required_percent') is None)
                        and not (energy.get('return_route_required') and not energy.get('return_route_available')
                            and energy.get('reason') in ('return_route_unavailable','guided_return_route_unavailable'))):
                    rejected[rid]='작업 이동 시간·에너지 예측 불가: '+energy.get('reason','unknown')
                    record['energy_budget']=energy
                    continue
                if energy.get('return_route_required') and not energy['return_route_available']:
                    reasons=sorted({row.get('reason') for row in energy.get('return_candidates',[]) if row.get('reason')})
                    rejected[rid]=('AGV 업무 후 순방향 충전·통로 복귀 경로 없음' if robot.model_id=='agv' else '업무 후 충전 경로·대기 에너지 예측 불가')+(': '+', '.join(reasons) if reasons else '')
                    record['energy_budget']=energy
                    continue
                if obs['battery']<energy['required_percent']:
                    rejected[rid]='예상 작업·복귀 에너지와 충전 예비량 부족'
                    target_ceiling=100. if self.policy.charge_target_mode=='task_budget' else self.policy.charge_until
                    if energy['required_percent']<=target_ceiling:
                        self.robot_states[rid]['charge_needed_percent']=energy['required_percent']
                    record['energy_budget']=energy
                    continue
                distance=math.hypot(obs["pose"]["x"]-task.destination.x,obs["pose"]["y"]-task.destination.y)
                score=distance+(self.count[rid]*4 if self.policy.assignment=="balanced" else 0)
                candidates.append((score,rid,route,trip))
            if not candidates:
                record.update(status="waiting",reason="; ".join(sorted(set(rejected.values()))) or "사용 가능한 로봇 대기");continue
            score,rid,route,trip=min(candidates,key=lambda c:(c[0],c[1]))
            if task.item_id:self.reservations.request("item:"+task.item_id,rid)
            record.update(status="running",robot_id=rid,started_at=time,reason=f"{self.policy.assignment} 정책 · 점수 {score:.2f}",progress_at=time)
            self.robot_states[rid].update(status="manipulating" if task.kind=="manipulate" else "working",task_id=task.id,path=route,reason=record["reason"],peer_replans={})
            self.robot_states[rid]["command_epoch"]+=1
            if trip:
                receipt=self.facilities.request(trip["elevator_id"],rid,trip["source_floor"],trip["dest_floor"],trip["mass"],trip["envelope"])
                self.robot_states[rid]["trip"]=dict(trip,request_id=receipt["request_id"])
            self.count[rid]+=1
            self.emit("assignment",rid,f"{task.name} 배정",dict(task_id=task.id,policy=self.policy.model_dump(),score=score,rejected=rejected))
        commands={}
        for rid,state in self.robot_states.items():
            obs=observations.get(rid); robot=self.robots[rid]
            commands[rid]=dict(v=0.,w=0.,mode=state["mode"])
            if state['status']=='cooperating' and self.cooperative:
                commands[rid]=self.cooperative.base_command(rid,time,observations)
                continue
            if obs and state['status']=='charging':
                commands[rid]=self.charging.command(rid,obs,time)
                continue
            if not obs or state["status"] not in ("working","manual","transit_recovery"):continue
            record=self.tasks.get(state["task_id"])
            if record and time-record["started_at"]>record["spec"].timeout:
                self._failure(record["id"],time,"작업 시간 초과");continue
            facility_command=self._trip_command(rid,state,obs,time)
            if facility_command is not None:
                commands[rid]=facility_command;continue
            path=state["path"]
            tolerance=ARRIVAL_TOLERANCE_M if robot.model_id=='agv' else .22
            if robot.model_id=='agv':
                stamp=obs.get('sampled_at')
                if (not isinstance(stamp,(int,float)) or not math.isfinite(stamp) or stamp>time+1e-9
                        or time-stamp>self.policy.stale_after or not self.guided_observation_valid.get(rid,False)):
                    if record:record['arrival_at']=None
                    state['reason']='AGV 신선한 지정 경로 관측 확인 필요'
                    continue
            while path and math.hypot(path[0]["x"]-obs["pose"]["x"],path[0]["y"]-obs["pose"]["y"])<tolerance:
                path.pop(0)
                if record:record["progress_at"]=time
            if robot.model_id=='agv' and path:
                target=record['spec'].destination.model_dump() if record else state.get('manual_target')
                forward=self._guided_remaining(robot,obs,path,target,self._floor(obs['pose']['z']))
                if forward is None:
                    reason='AGV 남은 지정 경로 순방향 재계획 불가: '+self.guided_rejections.get(rid,'unknown')
                    if record:self._failure(record['id'],time,reason,allow_retry=False)
                    else:state.update(status='recovery_required',reason=reason,path=[])
                    continue
                if forward is not path:
                    state['path']=path=forward
                    if record:record['progress_at']=time
                    self.emit('replan',rid,'관측상 지난 AGV 경유점을 건너뛰고 남은 순방향 경로 재계획',{'path':deepcopy(path),'sampled_at':obs['sampled_at']})
            if not path:
                trip=state.get("trip")
                target=trip["staging"] if trip else record["spec"].destination.model_dump() if record else state.get("manual_target")
                if target and math.hypot(target['x']-obs['pose']['x'],target['y']-obs['pose']['y'])>=tolerance:
                    # A consumed waypoint never substitutes for the actual goal.
                    if record:record['arrival_at']=None
                    if robot.model_id=='agv':
                        forward=self._route(robot,obs,target,self._floor(obs['pose']['z']))
                        if forward is None:
                            reason='AGV 목표지점 순방향 재접근 불가: '+self.guided_rejections.get(rid,'unknown')
                            if record:self._failure(record['id'],time,reason,allow_retry=False)
                            else:state.update(status='recovery_required',reason=reason)
                            continue
                        state['path']=forward
                    else:state['path']=[deepcopy(target)]
                    state['reason']='마지막 목표의 실제 XY 도달 재확인'
                    continue
                yaw_error=angle(target["yaw"]-obs["pose"]["yaw"]) if target else 0.
                if abs(yaw_error)>.1:
                    commands[rid]=dict(v=0.,w=max(-.5,min(.5,yaw_error*1.8)),mode="walk" if robot.model_id=="spot" else "drive")
                    state["reason"]="목표 방향 정렬"
                    continue
                if trip:
                    trip["phase"]="ride"
                    state["reason"]="승강기 탑승 허가 대기"
                    continue
                if record:
                    arrival_clock=obs['sampled_at']
                    previous_sample=record.get('arrival_sampled_at')
                    gap_limit=min(self.policy.stale_after,max(2/self.project.physics.orchestration_hz,2/robot.sensors.rate_hz))
                    if previous_sample is not None and (arrival_clock<previous_sample or arrival_clock-previous_sample>gap_limit+1e-9):record['arrival_at']=None
                    record['arrival_sampled_at']=arrival_clock
                    if record["arrival_at"] is None:record["arrival_at"]=arrival_clock
                    if arrival_clock-record["arrival_at"]>=record["spec"].dwell and math.hypot(*obs["velocity"][:2])<.12:
                        confirmation=record['spec'].confirmation
                        if confirmation and not record.get('confirmation_receipt'):
                            if record.get('confirmation_requested_at') is None:
                                record['confirmation_requested_at']=time
                                self.emit('confirmation_required',rid,confirmation.label,{'task_id':record['id'],'criterion':confirmation.criterion})
                            if time-record['confirmation_requested_at']>confirmation.timeout_s:
                                self._failure(record['id'],time,'현장 확인 제한 시간 초과',allow_retry=False)
                                continue
                            record['reason']='사용자 현장 확인 대기: '+confirmation.criterion
                            state['reason']=record['reason']
                            continue
                        record.update(status="completed",completed_at=time,reason="목표 관측 도달·정지 및 사용자 현장 확인" if confirmation else "목표 관측 도달 및 정지 확인")
                        state.update(status="idle",task_id=None,reason="작업 완료")
                        self.emit("task_completed",rid,record["spec"].name,{"task_id":record["id"]})
                elif np_speed(obs)<.12:
                    state.update(status="idle",reason="명령 목표 관측 도달");state["last_command"]["status"]="completed"
                continue
            if record and time-record["progress_at"]>self.policy.deadlock_timeout:
                trip=state.get("trip")
                target=trip["staging"] if trip else record["spec"].destination.model_dump()
                floor=trip["source_floor"] if trip else record["spec"].floor_id
                new=self._route(robot,obs,target,floor)
                if new is not None:
                    state["path"]=path=new;record["progress_at"]=time
                    self.emit("replan",rid,"장시간 진행 정체로 경로 재계획",{})
            if not path:continue
            dx,dy=path[0]["x"]-obs["pose"]["x"],path[0]["y"]-obs["pose"]["y"]
            turn=angle(math.atan2(dy,dx)-obs["pose"]["yaw"])
            speed=min(robot.max_speed,self.policy.speed_limit,model_by_id(robot.model_id)["max_speed"])
            wait=None
            for other_id,other in observations.items():
                if other_id==rid or time-other["sampled_at"]>self.policy.stale_after:continue
                if abs(other["pose"]["z"]-obs["pose"]["z"])>1.2:continue
                distance=math.hypot(other["pose"]["x"]-obs["pose"]["x"],other["pose"]["y"]-obs["pose"]["y"])
                ahead=dx*(other["pose"]["x"]-obs["pose"]["x"])+dy*(other["pose"]["y"]-obs["pose"]["y"])>0
                other_state=self.robot_states[other_id]
                if ahead and distance<radius(robot)+radius(self.robots[other_id])+self.policy.safety_distance:
                    def rank(robot_id,robot_state):
                        assignment=self.tasks.get(robot_state["task_id"])
                        started=assignment["started_at"] if assignment else robot_state["last_command"].get("requested_at",time)
                        priority=assignment["spec"].priority if assignment else 100
                        return (-priority,started,robot_id) if self.policy.traffic=="priority" else (started,robot_id)
                    if other_state["status"] not in ("working","manual") or rank(rid,state)>rank(other_id,other_state):wait=other_id;break
            if wait:
                state["reason"]=f"{wait} 통행 공간 대기"
                # Replanning the same geometry-only path cannot resolve an
                # idle receiver blocking a subsequent stage. Try bounded
                # local avoidance without changing any approved destination.
                attempts=state.setdefault('peer_replans',{})
                attempt=attempts.get(wait,{'count':0,'at':-math.inf})
                if record and attempt['count']<3 and time-attempt['at']>=2.:
                    attempts[wait]={'count':attempt['count']+1,'at':time}
                    trip=state.get('trip')
                    target=trip['staging'] if trip else record['spec'].destination.model_dump()
                    floor=trip['source_floor'] if trip else record['spec'].floor_id
                    alternate=self._peer_detour(robot,obs,target,floor,observations,time)
                    if alternate is not None:
                        state['path']=alternate;record['progress_at']=time
                        self.emit('peer_detour',rid,'관측된 로봇 점유를 피해 승인된 목적지로 국소 재계획',
                            {'task_id':record['id'],'blocking_robot':wait,'attempt':attempt['count']+1,'path':deepcopy(alternate),'sampled_at':obs['sampled_at']})
                elif record and attempt['count']>=3:
                    state['reason']=f'{wait} 통행 공간 대기 · 국소 우회 3회 소진 · 경로 해소 또는 사용자 개입 필요'
                continue
            scan=obs.get("sensors",{}).get("lidar")
            if isinstance(scan,dict) and abs(turn)<.65:
                front=[d for a,d in zip(scan["angles"],scan["ranges"]) if abs(a)<.3]
                if front and min(front)<radius(robot)+self.policy.safety_distance:
                    state["reason"]="거리 센서의 전방 장애물 관측으로 제동";continue
            state["reason"]="관측 기반 경로 추종"
            if robot.model_id=='agv':speed=min(speed,math.hypot(dx,dy)*.8)
            turn_limit=.12 if robot.model_id=='agv' else .65
            commands[rid]=dict(v=speed*max(0,math.cos(turn)) if abs(turn)<turn_limit else 0.,w=max(-.65,min(.65,turn*1.8)),mode="walk" if robot.model_id=="spot" else "drive")
        # Every base-motion branch (including charging, facilities and peers)
        # passes this common gate. Existing lower action caps stay lower.
        for rid, command in commands.items():
            report=observed_limit(self.robots[rid],self.policy,self.project.environment,observations.get(rid),time)
            self.robot_states[rid]['motion_limit']=report
            cap=report['limit_m_s'] if report['status']=='known' else 0.
            command['v']=clamp_translation(command['v'],cap)
            commands[rid]=self.pedestrian_safety.apply(rid,observations.get(rid),time,command)
        return commands

    def _failure(self,task_id,time,reason,allow_retry=True):
        record=self.tasks[task_id];rid=record["robot_id"]
        if record["status"]!="running":return
        if record['spec'].cooperation and self.cooperative:
            self.cooperative.terminate(task_id,time,reason)
            return
        record.pop("confirmation_receipt",None)
        record.pop("confirmation_requested_at",None)
        record["attempts"]+=1
        # Manipulation owns its sensor-confirmed retries. A terminal failure may
        # leave a load held or dropped and must not silently start a new grasp.
        retry=allow_retry and record["spec"].kind!="manipulate" and self.policy.failure!="stop" and record["attempts"]<=record["spec"].retries
        record.update(status="waiting" if retry else "failed",reason=reason,robot_id=None,arrival_at=None)
        if not retry:record["completed_at"]=time
        if rid:
            state=self.robot_states[rid]
            if state["task_id"]!=task_id:return
            state["command_epoch"]+=1
            trip=state.get("trip")
            riding=bool(trip and not self.facilities.cancel(trip["elevator_id"],rid))
            if trip and not riding:state.pop("trip",None)
            manipulation=record["spec"].kind=="manipulate"
            state.update(status="transit_recovery" if riding else "recovery_required" if manipulation else "idle",task_id=None,path=[],reason=reason)
            self.reservations.release_all(rid,keep_items=manipulation)
        self.emit("task_retry" if retry else "task_failed",rid,reason,{"task_id":task_id})

    def cancel(self,task_id,time):
        record=self.tasks[task_id]
        if self.cooperative:
            execution=self.cooperative.executions.get(task_id)
            if execution and self.cooperative.recovery.active(execution):
                self.cooperative.recovery.stop(task_id,time,'사용자 복구 중단',cancelled=True)
                return
        if record["status"] in ("cancelled","completed","failed"):return
        if record['status']=='running' and record['spec'].cooperation and self.cooperative:
            self.cooperative.terminate(task_id,time,'사용자 취소: 협업 복구 확인 필요',cancelled=True)
            return
        if record["robot_id"] and self.robot_states[record["robot_id"]]["task_id"]==task_id:
            self.robot_states[record["robot_id"]]["command_epoch"]+=1
            self.robot_states[record["robot_id"]].update(status="idle",task_id=None,path=[],reason="작업 취소")
            rid=record["robot_id"];state=self.robot_states[rid];trip=state.get("trip")
            if trip and not self.facilities.cancel(trip["elevator_id"],rid):state["status"]="transit_recovery"
            elif trip:state.pop("trip",None)
            manipulation=record["spec"].kind=="manipulate"
            if manipulation:state["status"]="recovery_required"
            self.reservations.release_all(rid,keep_items=manipulation)
        record.update(status="cancelled",reason="사용자 취소",completed_at=time)
        self.emit("task_cancelled",task_id,"작업 취소",{})

    def external_result(self,task_id,time,status,reason,evidence):
        record=self.tasks[task_id]
        if record["status"]!="running":return
        if record['spec'].cooperation:
            if status=='failed':self._failure(task_id,time,reason,allow_retry=False)
            return  # Only the cooperative placement/lease transaction completes it.
        deadline=record["spec"].deadline
        overdue=(deadline is not None and time>deadline) or time-record["started_at"]>record["spec"].timeout
        if overdue:
            record["evidence"]=deepcopy(evidence)
            self._failure(task_id,time,"작업 기한 또는 실행 제한 시간 초과",allow_retry=False)
            return
        rid=record["robot_id"]
        if status=="completed":
            record.update(status="completed",completed_at=time,reason=reason,evidence=evidence)
            self.robot_states[rid].update(status="idle",task_id=None,reason=reason)
            self.robot_states[rid]["command_epoch"]+=1
            self.reservations.release_all(rid)
            self.emit("task_completed",rid,reason,{"task_id":task_id,"evidence":evidence})
        elif status=="failed":self._failure(task_id,time,reason)
        else:self.robot_states[rid]["reason"]=reason

    def manual(self,rid,kind,target,time):
        if rid not in self.robots:raise ValueError("없는 로봇")
        state=self.robot_states[rid]
        if kind not in ("stop","stand","sit","move"):raise ValueError("지원하지 않는 명령")
        if kind=="sit" and self.robots[rid].model_id!="spot":raise ValueError("이 모델에는 앉기 능력이 없습니다")
        route=None
        if kind=="move":
            if self.pedestrian_safety.states.get(rid,{}).get('failed'):
                raise ValueError('보행자 차단 복구 확인 후 운영 재개를 먼저 요청하세요')
            if self.cooperative and self.cooperative.locked(rid):raise ValueError('협업 예약 또는 물품 복구 확인이 먼저 필요합니다')
            if rid in self.charging.plans:raise ValueError("충전 예약 이용 중: 운영 재개로 충전·접점 분리를 먼저 완료하세요")
            trip=state.get("trip")
            if trip and self.facilities.rides[trip["request_id"]].status!="completed":raise ValueError("승강기 이용 중 수동 경로 변경 불가: 로봇 운영 재개로 예약된 하차를 먼저 완료하세요")
            if target is None:raise ValueError("목표 위치 필요")
            obs=self.last_observations.get(rid)
            if not obs or time-obs["sampled_at"]>self.policy.stale_after:raise ValueError("유효한 관측 대기")
            if model_by_id(self.robots[rid].model_id)["locomotion"]=="fixed":raise ValueError("고정형 로봇은 이동할 수 없습니다")
            route=self._route(self.robots[rid],obs,target,self._floor(obs["pose"]["z"]))
            if route is None:raise ValueError("통과 가능한 경로 없음")
            if trip:state.pop("trip",None)
        if state["task_id"]:self.cancel(state["task_id"],time)
        if kind!="move":self.charging.interrupt(rid,"operator_hold")
        command={"kind":kind,"status":"accepted","requested_at":time}
        state["last_command"]=command
        state["command_epoch"]+=1
        state["operator_hold"]=kind!="move"
        if kind=="move":
            state.update(status="manual",path=route,reason="수동 이동 명령",mode="stand",manual_target=dict(target))
        else:
            state.update(status="stopped",path=[],mode="sit" if kind=="sit" else "stop" if kind=="stop" else "stand",reason=f"{kind} 명령 수락")
        self.emit("command",rid,f"{kind} 요청 수락",command)
        return command

    def resume(self,rid,time):
        if rid not in self.robots:raise ValueError("없는 로봇")
        state=self.robot_states[rid]
        if self.cooperative and self.cooperative.locked(rid):raise ValueError('협업 물품·참여 로봇 복구 확인이 먼저 필요합니다')
        obs=self.last_observations.get(rid)
        if not obs or time-obs["sampled_at"]>self.policy.stale_after or obs["fault"]!="none" or obs["battery"]<=0 or obs["upright"]<.45:raise ValueError("신선한 정상 관측이 필요합니다")
        if any(rid in owners for resource,owners in self.reservations.owners.items() if resource.startswith("item:")):raise ValueError("물품 조작 복구 확인이 먼저 필요합니다")
        if not state["operator_hold"] and rid not in self.charging.plans:return dict(status="unchanged",robot_id=rid)
        self.charging.recover(rid)
        self.pedestrian_safety.resume(rid)
        state.update(operator_hold=False,status="transit_recovery" if state.get("trip") else "idle",mode="stand",reason="사용자 운영 재개 요청")
        state["command_epoch"]+=1
        self.emit("robot_resumed",rid,"사용자 운영 재개 요청 수락",{})
        return dict(status="accepted",robot_id=rid,meaning="운영 재개 요청; 이동이나 하차 완료를 의미하지 않음")

    def confirm_step(self, task_id, time, note):
        record=self.tasks.get(task_id)
        if not record or not record['spec'].confirmation:
            raise ValueError('승인된 현장 확인 단계가 아닙니다')
        if record.get('confirmation_receipt'):
            return dict(record['confirmation_receipt'],replayed=True)
        if record['status']!='running' or record.get('confirmation_requested_at') is None:
            raise ValueError('도착 관측 뒤 확인 대기 중인 단계만 확인할 수 있습니다')
        receipt={'task_id':task_id,'sim_time':time,'note':note,'source':'user_confirmation','physical_item_change':False}
        record['confirmation_receipt']=receipt
        self.emit('human_confirmed',record['robot_id'],note,receipt)
        return receipt

    def task_rows(self):
        return [{k:v for k,v in t.items() if k!="spec"} for t in self.tasks.values()]


def np_speed(obs):
    return math.sqrt(sum(x*x for x in obs["velocity"]))+math.sqrt(sum(x*x for x in obs["angular_velocity"]))
