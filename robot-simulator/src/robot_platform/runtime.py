"""Owns one simulation run; truth, observation, control and evaluation are distinct."""
from __future__ import annotations
from collections import deque
from copy import deepcopy
import math
import time
import resource
from uuid import uuid4

import mujoco
import numpy as np

from .catalog import model_by_id
from .domain import Project, FaultInjection
from .incidents import IncidentScheduler
from .physics import PhysicsWorld
from .sensing import ObservationBus
from .orchestration import Orchestrator
from .pedestrians import PedestrianController
from .facility_metrics import FacilityMetrics
from .consumption_meter import ConsumptionObservations, VERSION as CONSUMPTION_METER_VERSION


class Session:
    def __init__(self,project: Project, *, stop_when_tasks_terminal=False):
        self.project=project.model_copy(deep=True)
        self.stop_when_tasks_terminal=stop_when_tasks_terminal
        from .pedestrian_navigation import validate_pedestrian_placements
        validate_pedestrian_placements(project)
        self.world=PhysicsWorld(project)
        self.run_id=uuid4().hex
        self.status="paused"
        self.speed=1.
        self.started_wall=time.monotonic()
        self.compute_seconds=0.
        self.events=[]
        self.bus=ObservationBus(project)
        self.consumption_observations=ConsumptionObservations(self.run_id,self.project.robots,self.project.policy.stale_after)
        self.orchestrator=Orchestrator(project,self.emit)
        self.elevator_metrics=FacilityMetrics(kind='elevator',facility_ids=list(self.orchestrator.facilities.elements))
        self.charging_metrics=FacilityMetrics(kind='charger',facility_ids=list(self.orchestrator.charging.manager.elements))
        dock_geometry={}
        for robot in project.robots:
            for station in project.environment.elements:
                if station.kind not in ('charger','dock'):continue
                try:dock_geometry[(robot.id,station.id)]=self.world.docking_geometry(robot.id,station.id)
                except ValueError:continue  # A model without a tested connector is not assigned.
        self.orchestrator.charging.configure(dock_geometry)
        self.batteries={r.id:r.battery for r in project.robots}
        self.energy={r.id:0. for r in project.robots}
        self.energy_demand={r.id:0. for r in project.robots}
        self.energy_unserved={r.id:0. for r in project.robots}
        self.charge_input={r.id:0. for r in project.robots}
        self.charge_stored={r.id:0. for r in project.robots}
        self.charge_power={r.id:0. for r in project.robots}
        self.distances={r.id:0. for r in project.robots}
        self.previous={r.id:self.world.truth(r.id)["pose"] for r in project.robots}
        self.robot_faults={r.id:r.fault for r in project.robots}
        self.observations={}
        self.next_orchestration=0.
        self.next_sensor=0.
        self.next_frame=0.
        self.frames=[]
        self.transit=deque()
        self.last_delivery={r.id:0. for r in project.robots}
        self.injections=[f.model_copy(deep=True) for f in project.faults]
        self.replan_watch=None
        self.incident_scheduler=IncidentScheduler()
        self.pushes=[]
        self.pedestrians=PedestrianController(project.people,self.world.floor_heights,project.physics.seed,floor_bounds={f.id:[0,0,f.width,f.depth] for f in project.environment.floors},environment=project.environment,
            desired_robot_clearance_m=(project.policy.pedestrian_avoidance.desired_clearance_m
                                       if project.policy.pedestrian_avoidance else .5))
        self.pedestrian_states={}
        self.pedestrian_headings={p.id:p.pose.yaw for p in project.people}
        self.pedestrian_min_clearance={r.id:None for r in project.robots}
        self.active_pedestrian_near=set()
        self.collision_pairs=set()
        self.collision_count=0
        self.near_count=0
        self.fallen=set()
        self.damaged=set()
        self.active_near=set()
        self.busy_seconds={r.id:0. for r in project.robots}
        self.wait_seconds={r.id:0. for r in project.robots}
        self.orchestration_latencies=[]
        self.command_records={}
        self.manipulation_workflows={}
        self.manipulation_results={}
        self.manipulation_transit=[]
        self.item_custody={item.id:None for item in project.items}
        self.item_custody_status={item.id:"unassigned" for item in project.items}
        from .cooperative_control import CooperativeControl
        support_geometry={}
        for robot in project.robots:
            try:support_geometry[robot.id]=self.world.support_geometry(robot.id)
            except ValueError:continue
        self.cooperative=CooperativeControl(self.orchestrator,support_geometry,rng=self.bus.rng,
            arm_geometry={rid:controller.geometry_contract for rid,controller in self.world.arm_controllers.items()})
        self.orchestrator.cooperative=self.cooperative
        self.cooperative_transit=[]
        self.cooperative_last_delivery={}
        self.cooperative_delivery_receipts={}
        self.cooperative_stop_epochs={}
        self.facility_faults={e.id:e.facility.fault for e in project.environment.elements}
        self.facility_states={e.id:dict(id=e.id,name=e.name,kind=e.kind,position=0.,target=0.,door="closed",status="fault" if e.facility.fault else "idle",capacity=e.facility.capacity,max_load=e.facility.max_load,queue=[],occupants=[],fault=e.facility.fault) for e in project.environment.elements if e.kind in ("door","elevator","charger","dock")}
        self.warnings=["실제 로봇 연동은 미검증입니다.","Spot 제어기는 연구용이며 4cm 계단·5° 경사로 외 조건은 검증 범위에 포함되지 않습니다.","정지 차체 물품 조작·승강기 이동은 조건부 검증이며 협업 인계는 미완료입니다.","카메라 영상·거리 센서 재질 반응과 정량적 손상 보정은 미완료입니다."]
        self.emit("run_created",None,"실행 초기화",dict(seed=project.physics.seed,physics=project.physics.model_dump(),policy=project.policy.model_dump()))

    @property
    def time(self):return float(self.world.data.time)

    def emit(self,kind,entity_id,message,details):
        row=dict(seq=len(self.events)+1,time=self.time,kind=kind,severity="error" if "failed" in kind or "damage" in kind else "warning" if kind in ("collision","fall","fault","near_miss") else "info",entity_id=entity_id,message=message,details=deepcopy(details))
        self.events.append(row)

    def inject(self,fault: FaultInjection):
        if fault.target_id not in self.world.entity_types:raise ValueError("없는 장애 주입 대상")
        validation=self.project.model_dump();validation['faults']=[fault.model_dump()]
        Project.model_validate(validation)
        fault=fault.model_copy(deep=True);fault.time=max(fault.time,self.time)
        self.injections.append(fault)
        self.emit("fault_scheduled",fault.target_id,"장애 주입 예약",fault.model_dump())

    def _faults(self):
        active={**{rid:'facility' if fault else 'none' for rid,fault in self.facility_faults.items()},**self.robot_faults}
        actions=self.incident_scheduler.tick(self.time,self.injections,self.orchestrator.tasks,self.events,active)
        for f,incident in actions:
            if incident['phase']=='blocked':
                self.emit('incident_blocked',f.target_id,'기존 장애를 덮어쓰지 않습니다. 기존 장애를 먼저 복구하세요',incident)
                continue
            if f.kind=="push":
                if f.target_id in self.world.robot_bodies:self.pushes.append((self.world.robot_bodies[f.target_id],self.time+f.duration,f.magnitude))
            elif f.target_id in self.robot_faults:
                self.robot_faults[f.target_id]="none" if f.kind=="recover" else f.kind
                for r in self.world.project.robots:
                    if r.id==f.target_id:r.fault=self.robot_faults[f.target_id]
                if f.kind=="battery":self.batteries[f.target_id]=max(0,min(100,f.magnitude))
            elif f.target_id in self.facility_states:
                self.facility_faults[f.target_id]=f.kind!="recover"
                if f.kind=="recover" and f.target_id in self.orchestrator.facilities.elements:self.orchestrator.facilities.recover(f.target_id)
                if f.kind=='recover' and f.target_id in self.orchestrator.charging.manager.elements:
                    self.orchestrator.charging.manager.recover(f.target_id)
            self.emit("fault",f.target_id,f"{f.kind} 장애 조건 적용",f.model_dump())
            self.emit('incident_'+incident['phase'],f.target_id,
                      '돌발 상황 자동 해제' if incident['phase']=='released' else '돌발 상황 발생',incident)
        self.world.data.xfrc_applied[:]=0
        self.pushes=[x for x in self.pushes if self.time<x[1]]
        for body,until,magnitude in self.pushes:self.world.data.xfrc_applied[body,0]=magnitude

    def _people(self):
        if not self.project.people:return
        # This perception port belongs to each simulated human, never to robot
        # orchestration. Its range and reaction delay are applied by the model.
        from .navigation import radius
        objects=[]
        for robot in self.project.robots:
            truth=self.world.truth(robot.id)
            pose=truth["pose"]
            objects.append(dict(id=robot.id,kind="robot",position=[pose[k] for k in ("x","y","z")],velocity=truth["velocity"],radius=radius(robot),floor_id=self.orchestrator._floor(pose["z"])))
        for person in self.project.people:
            body=self.world.model.body(person.id+"/body").id
            velocity=np.zeros(6)
            mujoco.mj_objectVelocity(self.world.model,self.world.data,mujoco.mjtObj.mjOBJ_BODY,body,velocity,0)
            if math.hypot(*velocity[3:5])>.01:self.pedestrian_headings[person.id]=math.atan2(velocity[4],velocity[3])
            objects.append(dict(id=person.id,kind="person",position=self.world.data.xpos[body].tolist(),velocity=velocity[3:].tolist(),radius=.22,floor_id=person.floor_id))
        perceptions={obj["id"]:dict(sampled_at=self.time,position=obj["position"],floor_id=obj["floor_id"],neighbors=[other for other in objects if other["id"]!=obj["id"]]) for obj in objects if obj["kind"]=="person"}
        self.pedestrian_states=self.pedestrians.update(self.time,perceptions)
        for person_id,command in self.pedestrian_states.items():
            self.world.data.ctrl[self.world.model.actuator(f"{person_id}/x-motor").id]=command["vx"]
            self.world.data.ctrl[self.world.model.actuator(f"{person_id}/y-motor").id]=command["vy"]
            for event in command["events"]:
                self.emit("person_"+event["type"],person_id,command["reason"],dict(event,model=command['controller_version']))

    def _facilities(self):
        sensed=self.world.facility_observations(self.time)
        for eid,reading in sensed.items():reading["fault"]=self.facility_faults[eid]
        result=self.orchestrator.facilities.update(self.time,self.observations,sensed)
        self.elevator_metrics.update(self.time,result['states'])
        self.orchestrator.facility_intentions=result["robot_commands"]
        for eid,command in result["commands"].items():
            self.world.facility_command(eid,command)
            previous=self.facility_states[eid].get("phase")
            state=result["states"][eid]
            self.facility_states[eid].update(state,status=state["phase"],sampled_at=sensed[eid]["sampled_at"],sensor_model=sensed[eid].get("sensor_model"))
            if previous!=state["phase"]:
                self.emit("facility_phase",eid,"승강기 상태 전이",dict(phase=state["phase"],fault=state["fault"],position=state["position"]))
        for e in self.project.environment.elements:
            if e.kind!="door":continue
            state=self.facility_states[e.id]
            position=float(self.world.data.joint(f"{e.id}/slide").qpos[0])
            from .door_geometry import door_geometry
            travel=door_geometry(e,self.project.environment.id)['travel']
            nearby=any(abs(o["pose"]["x"]-e.pose.x)<2 and abs(o["pose"]["y"]-e.pose.y)<2 and abs(o["pose"]["z"]-self.world.floor_heights[e.floor_id]-.35)<1 and self.time-o["sampled_at"]<1 for o in self.observations.values())
            obstructed=any(e.id in (c["a"],c["b"]) and c["force"]>1 for c in self.world.contacts())
            target=position if self.facility_faults[e.id] else travel if (nearby and e.facility.automatic) or obstructed else 0.
            actuator=self.world.model.actuator(f"{e.id}/motor").id
            increment=travel/e.facility.door_duration/self.project.physics.control_hz
            self.world.data.ctrl[actuator]+=max(-increment,min(increment,target-self.world.data.ctrl[actuator]))
            state.update(position=position,target=target,fault=self.facility_faults[e.id],door="open" if position>travel*.8 else "closed" if position<.05 else "moving",sensor_model="ideal door encoder and contact obstruction switch")

    def facility_target(self,elevator_id,height):
        manager=self.orchestrator.facilities
        if elevator_id not in manager.elements:raise ValueError("호출 가능한 승강기가 아닙니다")
        element=manager.elements[elevator_id]
        floors=[floor for floor in element.facility.served_floors if abs(manager._height(elevator_id,floor)-height)<.025]
        if not floors:raise ValueError("서비스 층 높이를 지정하세요")
        receipt=manager.call(elevator_id,floors[0])
        self.emit("facility_call",elevator_id,"빈 승강기 호출 수락",dict(floor_id=floors[0]))
        return receipt

    def _charging(self):
        sensed=self.world.charger_observations(self.time)
        for eid,reading in sensed.items():reading['fault']=self.facility_faults[eid]
        control=self.orchestrator.charging
        control.station_observations=deepcopy(sensed)
        result=control.manager.update(self.time,self.observations,sensed)
        self.charging_metrics.update(self.time,result['states'])
        control.intentions=result['robot_intentions']
        control.power_requests=result['power_requests']
        for eid,state in result['states'].items():
            previous=self.facility_states[eid].get('phase')
            self.facility_states[eid].update(state,status=state['phase'])
            if eid in sensed:
                self.facility_states[eid].update(sampled_at=sensed[eid]['sampled_at'],sensor_model=sensed[eid].get('sensor_model'))
            if previous!=state['phase']:
                self.emit('charging_phase',eid,'충전 시설 상태 전이',dict(phase=state['phase'],reserved_by=state.get('reserved_by')))

    def _sense(self):
        contact_rows=self.world.contacts()
        dock_readings=self.world.charger_observations(self.time)
        for r in self.project.robots:
            if self.time-self.bus.last_sample[r.id]+1e-12<1/r.sensors.rate_hz:continue
            truth=self.world.truth(r.id)
            sensors=dict(imu=dict(angular_velocity=truth["angular_velocity"],orientation=truth["quaternion"]) if r.sensors.imu else None,joints=truth["joints"],contacts=[x for x in contact_rows if r.id in (x["a"],x["b"])],camera="미구현" if r.sensors.camera else "비활성",lidar=self.world.range_scan(r.id) if r.sensors.lidar else None)
            sensors["items"]=self.world.tracked_items(r.id) if r.sensors.item_tracking else []
            if self.project.policy.pedestrian_avoidance is not None:
                settings=self.project.policy.pedestrian_avoidance
                sensors['pedestrians']=dict(model='ideal_visible_person_tracker_v1',enabled=r.sensors.lidar,
                    max_range_m=settings.observation_range_m,
                    people=self.world.tracked_people(r.id,settings.observation_range_m) if r.sensors.lidar else [])
            # Explicit ideal instrumented-item contact sensing. It is sampled
            # only for visible tracked items and shares the observation bus's
            # delay/dropout; the coordinator never reads contact truth directly.
            for item in sensors['items']:
                item['support_contacts']=[deepcopy(row) for row in contact_rows if item['id'] in (row['a'],row['b'])]
                item['support_sensor_model']='ideal_visible_item_contact_wrench'
            sensors['docking']={eid:deepcopy(reading['contacts'][r.id]) for eid,reading in dock_readings.items() if r.id in reading['contacts']}
            # Ideal research meter at this sample's physics time. Consumption
            # and charging are separate integrals, never battery derivatives.
            # The payload shares the existing bus delay/dropout and RNG draws.
            sensors['consumption_meter']=dict(version=CONSUMPTION_METER_VERSION,run_id=self.run_id,
                robot_id=r.id,sampled_at=self.time,demand_j=self.energy_demand[r.id],drawn_j=self.energy[r.id],
                unserved_j=self.energy_unserved[r.id],charging_input_j=self.charge_input[r.id],charging_stored_j=self.charge_stored[r.id])
            if r.id in self.world.arm_controllers:
                controller=self.world.arm_controllers[r.id]
                sensors["manipulation"]={item.id:controller.feedback(self.world.data,item.id) for item in self.project.items}
                sensors["controller_error"]=self.world.controller_errors.get(r.id)
            else:
                # This explicit configuration report is distinct from missing
                # gripper observations and travels through the same sensor bus.
                sensors['manipulation']={item.id:dict(gripper_installed=False,
                    finger_contacts=[],bilateral_contact=False) for item in self.project.items}
            self.bus.sample(r.id,self.time,truth,self.batteries[r.id],self.robot_faults[r.id],sensors)
        self.observations=self.bus.deliver(self.time)
        self.consumption_observations.observe(self.time,self.observations)
        self._near_risk()

    def _manipulations(self):
        """Translate delivered sensor evidence into commands; never query item truth."""
        for task_id,record in self.orchestrator.tasks.items():
            task=record["spec"]
            if task.kind!="manipulate":continue
            rid=record["robot_id"]
            if record["status"]!="running":
                if task_id in self.manipulation_workflows:
                    previous=self.manipulation_results.get(task_id,{})
                    old_id=previous.get("robot_id")
                    if old_id in self.world.arm_controllers:self.world.arm_controllers[old_id].hold(self.world.data)
                    self.manipulation_workflows.pop(task_id,None)
                continue
            if rid not in self.world.arm_controllers:
                self.orchestrator.external_result(task_id,self.time,"failed","팔 제어기 없음",{})
                continue
            item=next(i for i in self.project.items if i.id==task.item_id)
            if task_id not in self.manipulation_workflows:
                from .manipulation_workflow import ManipulationWorkflow
                source=(task.source or item.pose).model_dump()
                source["z"]+=self.world.floor_heights[item.floor_id]
                destination=task.destination.model_dump()
                destination["z"]+=self.world.floor_heights[task.floor_id]
                self.manipulation_workflows[task_id]=ManipulationWorkflow(task_id,rid,item.id,source,destination,item.mass,item.size.model_dump(),max_payload=model_by_id(self.orchestrator.robots[rid].model_id)["max_payload"],retries=task.retries,timeout=task.timeout)
                self.emit("manipulation_started",rid,"물품 조작 흐름 시작",dict(task_id=task_id,item_id=item.id))
            obs=deepcopy(self.observations.get(rid,{}))
            sensors=obs.get("sensors",{})
            manipulation=sensors.get("manipulation",{}).get(item.id,{})
            manipulation["contact_item_id"]=item.id if manipulation.get("finger_contacts") else None
            sensors["manipulation"]=manipulation
            sensors["item_tracking"]={row["id"]:dict(row,visible=True) for row in sensors.get("items",[])}
            obs["sensors"]=sensors
            result=self.manipulation_workflows[task_id].update(self.time,obs)
            result["robot_id"]=rid
            old=self.manipulation_results.get(task_id)
            self.manipulation_results[task_id]=result
            if not old or old.get("phase")!=result.get("phase"):
                self.emit("manipulation_phase",rid,result["reason"],dict(task_id=task_id,phase=result["phase"]))
            if result.get("holding"):
                previous=self.item_custody[item.id]
                if previous is not None and previous!=rid:
                    self.orchestrator.external_result(task_id,self.time,"failed","물품 소유 확인 충돌",{})
                    continue
                self.item_custody[item.id]=rid
                self.item_custody_status[item.id]="observed_held"
            elif result["phase"] in ("release","retract","done","completed"):
                if self.item_custody[item.id]==rid:self.item_custody[item.id]=None
                self.item_custody_status[item.id]="observed_released"
            self.orchestrator.external_result(task_id,self.time,result["status"],result["reason"],result.get("evidence",{}))
            if sensors.get("controller_error"):
                self.orchestrator.external_result(task_id,self.time,"failed",sensors["controller_error"],{})
                self.world.arm_controllers[rid].hold(self.world.data)
                continue
            if result["status"]=="failed":
                self.world.arm_controllers[rid].hold(self.world.data)
                if self.item_custody[item.id]==rid:self.item_custody_status[item.id]="recovery_required"
                continue
            if result.get("hold"):
                self.world.arm_controllers[rid].hold(self.world.data)
                self.manipulation_transit=[entry for entry in self.manipulation_transit if entry[2]!=task_id]
                continue
            config=self.orchestrator.robots[rid].sensors
            if result.get("target") is not None and self.robot_faults[rid]=="none" and self.batteries[rid]>0 and self.bus.rng.random()>=config.dropout:
                if not self.manipulation_transit or self.manipulation_transit[-1][2:]!=(task_id,result):
                    self.manipulation_transit.append((self.time+config.communication_delay,rid,task_id,deepcopy(result)))
        remaining=[]
        for deliver,rid,task_id,result in self.manipulation_transit:
            if self.orchestrator.tasks[task_id]["status"]!="running":continue
            if deliver>self.time:remaining.append((deliver,rid,task_id,result));continue
            if self.robot_faults[rid]!="none" or self.batteries[rid]<=0:continue
            controller=self.world.arm_controllers[rid]
            controller.move_to(result["target"],opening=result["opening"])
            controller.set_payload_estimate(result["payload_estimate"])
        self.manipulation_transit=remaining

    def _cooperations(self):
        commands=self.cooperative.update(self.time,self.observations)
        # Send a terminal stop at control cadence through the usual network
        # path. Its physical arrival still obeys delay/loss; a broken link is
        # bounded by the robot's existing local command watchdog.
        for execution in self.cooperative.executions.values():
            if not execution['terminal'] or execution['released']:continue
            for rid in execution['participants'].values():
                epoch=self.orchestrator.robot_states[rid]['command_epoch']
                key=(execution['id'],rid)
                if self.cooperative_stop_epochs.get(key)==epoch:continue
                config=self.orchestrator.robots[rid].sensors
                if self.robot_faults[rid]=='communication' or self.bus.rng.random()<config.dropout:continue
                self.transit.append((self.time+config.communication_delay,rid,dict(v=0.,w=0.,mode='stand'),epoch,self.time+self.project.policy.stale_after))
                self.cooperative_stop_epochs[key]=epoch
        for rid,result in commands.items():
            controller=self.world.arm_controllers.get(rid)
            if controller is None:continue
            task_id=result['task_id']
            if result.get('hold') or not self.cooperative.command_active(task_id,result.get('recovery_id')):
                controller.hold(self.world.data)
                self.cooperative_transit=[entry for entry in self.cooperative_transit if entry['robot_id']!=rid]
                continue
            config=self.orchestrator.robots[rid].sensors
            observation=self.observations.get(rid,{})
            if observation.get('sensors',{}).get('controller_error'):
                if result.get('recovery_id'):
                    self.cooperative.recovery.stop(task_id,self.time,observation['sensors']['controller_error'])
                else:self.cooperative.terminate(task_id,self.time,observation['sensors']['controller_error'])
                controller.hold(self.world.data)
                continue
            if (result.get('target') is not None or result.get('release_settle') is True) and self.robot_faults[rid]=='none' and self.batteries[rid]>0 and self.bus.rng.random()>=config.dropout:
                self.cooperative_transit.append(dict(deliver=self.time+config.communication_delay,expires=observation.get('sampled_at',-1)+self.project.policy.stale_after,
                    robot_id=rid,task_id=task_id,execution_id=self.cooperative.executions[task_id]['id'],
                    recovery_id=result.get('recovery_id'),generation=result['generation'],epoch=self.orchestrator.robot_states[rid]['command_epoch'],
                    sampled_at=observation.get('sampled_at'),result=deepcopy(result)))
        pending=[]
        for entry in self.cooperative_transit:
            rid=entry['robot_id'];task_id=entry['task_id'];execution=self.cooperative.executions.get(task_id)
            if (execution is None or entry.get('execution_id')!=execution['id']
                    or not self.cooperative.command_active(task_id,entry.get('recovery_id')) or entry['generation']!=execution['generation']
                    or entry['epoch']!=self.orchestrator.robot_states[rid]['command_epoch'] or self.time>entry['expires']):continue
            if self.robot_faults[rid]!='none' or self.batteries[rid]<=0:continue
            if entry['deliver']>self.time:pending.append(entry);continue
            result=entry['result'];controller=self.world.arm_controllers[rid]
            # A source sample can authorize at most one delivered command
            # per execution/generation/epoch. A late release must not undo a
            # newer retract, including within the same workflow generation.
            stamp=entry.get('sampled_at')
            if isinstance(stamp,bool) or not isinstance(stamp,(int,float)) or not math.isfinite(stamp) or stamp>self.time:continue
            identity=(entry['execution_id'],entry['generation'],entry.get('recovery_id'),entry['epoch'])
            previous=self.cooperative_delivery_receipts.get(rid,{})
            if previous.get('identity')!=identity:previous={}
            if stamp<=previous.get('sampled_at',-math.inf):continue
            settle=result.get('release_settle',False)
            if type(settle) is not bool:continue
            if settle:
                setting_values=(result.get('opening'),result.get('payload_estimate'))
                if (result.get('phase')!='release' or result.get('hold') is not False
                        or not all(isinstance(value,(int,float)) and not isinstance(value,bool) and math.isfinite(value) for value in setting_values)
                        or setting_values!=(.1,0.) or previous.get('settle_retired')):continue
                controller.release_and_hold(self.world.data)
            else:
                controller.move_to(result['target'],opening=result['opening'])
                controller.set_payload_estimate(result['payload_estimate'])
            self.cooperative_delivery_receipts[rid]=dict(identity=identity,sampled_at=stamp,
                phase=result.get('phase'),release_settle=settle,
                settle_seen=settle or previous.get('settle_seen',False),
                settle_retired=previous.get('settle_retired',False) or result.get('phase')=='retract'
                    or (previous.get('settle_seen',False) and not settle))
            self.cooperative_last_delivery[rid]=self.time
        self.cooperative_transit=pending
        for rid in commands:
            if self.time-self.cooperative_last_delivery.get(rid,self.time)>self.project.policy.stale_after:
                self.world.arm_controllers[rid].hold(self.world.data)
        ledger=self.cooperative.snapshot()['items']
        for task_id,execution in self.cooperative.executions.items():
            if execution.get('released') and execution.get('custody_synced'):continue
            item_id=self.orchestrator.tasks[task_id]['spec'].item_id
            state=ledger[item_id]
            self.item_custody[item_id]=state['owner']
            self.item_custody_status[item_id]='observed_released' if execution['released'] else 'observed_recovery' if self.cooperative.recovery.active(execution) else 'recovery_required' if execution['terminal'] else 'observed_cooperative' if state['owner'] else 'custody_pending'
            if execution['released']:execution['custody_synced']=True

    def _near_risk(self):
        from .navigation import radius
        active=set()
        objects=[(r.id,self.world.data.xpos[self.world.robot_bodies[r.id]],radius(r)) for r in self.project.robots]
        objects += [(p.id,self.world.data.body(f"{p.id}/body").xpos,.22) for p in self.project.people]
        for i,(aid,a,ar) in enumerate(objects):
            for bid,b,br in objects[i+1:]:
                if abs(a[2]-b[2])>1.2:continue
                separation=math.hypot(a[0]-b[0],a[1]-b[1])-ar-br
                kinds=(self.world.entity_types.get(aid),self.world.entity_types.get(bid))
                if set(kinds)=={'robot','person'}:
                    rid=aid if kinds[0]=='robot' else bid
                    previous=self.pedestrian_min_clearance[rid]
                    self.pedestrian_min_clearance[rid]=separation if previous is None else min(previous,separation)
                if self.project.policy.pedestrian_avoidance is not None:
                    if set(kinds)=={'robot','person'}:
                        continue  # Opt-in human proximity is audited at every physics step below.
                pair=tuple(sorted((aid,bid)))
                threshold=self.project.policy.safety_distance
                if self.project.policy.pedestrian_avoidance is not None and {'robot','person'}=={self.world.entity_types.get(aid),self.world.entity_types.get(bid)}:
                    threshold=max(threshold,self.project.policy.pedestrian_avoidance.desired_clearance_m)
                if 0<separation<threshold:
                    active.add(pair)
                    if pair not in self.active_near:
                        self.near_count+=1;self.emit("near_miss",aid,"動作 공간 사이 안전 여유 부족".replace("動作","동작"),dict(other=bid,clearance_m=separation,requested_clearance_m=threshold,basis="circumscribed planar motion envelopes"))
        self.active_near=active

    def _evaluate(self):
        dt=float(self.world.model.opt.timestep)
        # Local electrical interlock runs at every physical step. A delayed
        # enable request cannot supply energy after an actual connector opens.
        requests=self.orchestrator.charging.power_requests
        connectors=self.world.charger_observations(self.time) if any(r['power_w']>0 for r in requests.values()) else {}
        active_pedestrian_near=set()
        for r in self.project.robots:
            truth=self.world.truth(r.id)
            pose=truth["pose"];prev=self.previous[r.id]
            if self.project.policy.pedestrian_avoidance is not None:
                from .navigation import radius
                for person in self.project.people:
                    if self.orchestrator._floor(pose['z'])!=person.floor_id:continue
                    person_pose=self.world.data.body(person.id+'/body').xpos
                    clearance=math.hypot(pose['x']-person_pose[0],pose['y']-person_pose[1])-radius(r)-.22
                    previous_clearance=self.pedestrian_min_clearance[r.id]
                    self.pedestrian_min_clearance[r.id]=clearance if previous_clearance is None else min(previous_clearance,clearance)
                    requested=self.project.policy.pedestrian_avoidance.desired_clearance_m
                    pair=(r.id,person.id)
                    if clearance<requested:
                        active_pedestrian_near.add(pair)
                        if pair not in self.active_pedestrian_near:
                            self.near_count+=1
                            self.emit('near_miss',r.id,'사람과 실제 안전 여유가 설정값보다 작습니다',
                                dict(other=person.id,clearance_m=clearance,requested_clearance_m=requested,
                                     basis='actual physics-step evaluator; not controller observation'))
            self.distances[r.id]+=math.hypot(pose["x"]-prev["x"],pose["y"]-prev["y"])
            self.previous[r.id]=pose
            power=0.
            for a in self.world._actuators[r.id]:
                power+=abs(self.world.data.actuator_force[a]*self.world.data.actuator_velocity[a])
            power=float(power)
            # Research proxy: absolute actuator work plus 20 W electronics.
            # Capacity and conservative route power are explicit per-instance inputs.
            capacity_j=r.battery_capacity_wh*3600
            demand=(power+20)*dt
            drawn=min(demand,self.batteries[r.id]/100*capacity_j)
            self.energy[r.id]+=drawn
            self.energy_demand[r.id]+=demand
            self.energy_unserved[r.id]+=demand-drawn
            self.batteries[r.id]=max(0,self.batteries[r.id]-drawn/capacity_j*100)
            self.charge_power[r.id]=0.
            request=requests.get(r.id)
            if request:
                eid=request['station_id']
                reading=connectors.get(eid,{}).get('contacts',{}).get(r.id,{})
                enabled=not self.facility_faults[eid] and self.robot_faults[r.id]=='none' and not self.orchestrator.robot_states[r.id]['operator_hold']
                connected=reading.get('left') and reading.get('right') and reading.get('aligned') and reading.get('relative_speed',float('inf'))<=.04
                if enabled and connected:
                    station=next(e for e in self.project.environment.elements if e.id==eid)
                    input_w=min(max(0.,request['power_w']),station.facility.charge_power_w)
                    supplied=input_w*dt
                    stored=min(supplied*station.facility.charge_efficiency,(100-self.batteries[r.id])/100*capacity_j)
                    self.charge_power[r.id]=input_w
                    self.charge_input[r.id]+=supplied
                    self.charge_stored[r.id]+=stored
                    self.batteries[r.id]=min(100.,self.batteries[r.id]+stored/capacity_j*100)
            state=self.orchestrator.robot_states[r.id]
            if state["status"] in ("working","manual","manipulating","cooperating","recovering"):self.busy_seconds[r.id]+=dt
            if "대기" in state["reason"]:self.wait_seconds[r.id]+=dt
            self.world.set_power(r.id,self.batteries[r.id]>0)
            if truth["upright"]<.45 and r.id not in self.fallen:
                self.fallen.add(r.id);self.emit("fall",r.id,"전도 기준 초과",dict(upright=truth["upright"]))
        self.active_pedestrian_near=active_pedestrian_near
        pairs=set()
        for c in self.world.contacts():
            a,b=c["a"],c["b"]
            for item in self.project.items:
                if item.id in (a,b) and c["impulse"]>item.fragility_impulse and item.id not in self.damaged:
                    self.damaged.add(item.id);self.emit("damage",item.id,"추정 손상 임계 충격량 초과",c)
            if "floor" in (a,b):continue
            if self.world.entity_types.get(a)!="robot" and self.world.entity_types.get(b)!="robot":continue
            # Intended contact with ground-like ramps and stairs is support, not collision count.
            support_names={e.id+"/platform" for e in self.project.environment.elements if e.kind=="elevator"}
            support_ids={e.id for e in self.project.environment.elements if e.kind in ("stairs","ramp")}
            if a in support_ids or b in support_ids or c["geom_a"] in support_names or c["geom_b"] in support_names:continue
            # Matched connector pads are intended contact. A chassis hitting a
            # station frame or the wrong contact side remains a collision.
            intended_connector=False
            for rid,eid,robot_geom,station_geom in ((a,b,c['geom_a'],c['geom_b']),(b,a,c['geom_b'],c['geom_a'])):
                if eid not in self.world._chargers or rid not in self.world._charging_robots:continue
                if any(robot_geom==f'{rid}/charge-{side}' and station_geom==f'{eid}/pad-{side}' for side in ('left','right')):
                    intended_connector=True
            if intended_connector:continue
            if c["force"]<1.:continue
            key=tuple(sorted((a,b)))
            if key not in self.collision_pairs and key not in pairs:
                self.collision_count+=1;self.emit("collision",a,"개체 간 물리 접촉",c)
            pairs.add(key)
        self.collision_pairs=pairs

    def step(self,steps=1):
        start=time.perf_counter()
        for _ in range(steps):
            self._faults()
            for rid,battery in self.batteries.items():self.world.set_power(rid,battery>0)
            if self.time+1e-10>=self.next_sensor:
                self._sense();self._people();self._facilities();self._charging();self._manipulations();self._cooperations()
                self.next_sensor+=1/self.project.physics.control_hz
            if self.time+1e-10>=self.next_orchestration:
                decision_start=time.perf_counter()
                commands=self.orchestrator.tick(self.time,self.observations)
                self.orchestration_latencies.append(time.perf_counter()-decision_start)
                for r in self.project.robots:
                    if self.robot_faults[r.id]=="communication" or self.bus.rng.random()<r.sensors.dropout:continue
                    cmd=deepcopy(commands[r.id])
                    token=self.orchestrator.charging.manager.motion_token(r.id)
                    if token is not None:cmd['_charging_motion_token']=token
                    self.transit.append((self.time+r.sensors.communication_delay,r.id,cmd,self.orchestrator.robot_states[r.id]["command_epoch"],self.time+self.project.policy.stale_after))
                self.next_orchestration+=1/self.project.physics.orchestration_hz
            # Different per-robot delays need delivery-order sorting, not FIFO blocking.
            waiting=deque()
            while self.transit:
                delivery,rid,cmd,epoch,expires=self.transit.popleft()
                if epoch!=self.orchestrator.robot_states[rid]["command_epoch"] or self.time>expires or self.robot_faults[rid]=="communication":continue
                token=cmd.get('_charging_motion_token')
                if token is not None and token!=self.orchestrator.charging.manager.motion_token(rid):continue
                if delivery<=self.time+1e-10:
                    delivered={key:value for key,value in cmd.items() if key!='_charging_motion_token'}
                    if self.batteries[rid]>0:
                        self.world.command(rid,**delivered)
                        if token is not None and delivered.get('v',0)==0 and delivered.get('w',0)==0 and delivered.get('mode') in ('stand','stop'):
                            self.orchestrator.charging.manager.acknowledge_handoff_stop(rid,token,self.time)
                    self.last_delivery[rid]=self.time
                else:waiting.append((delivery,rid,cmd,epoch,expires))
            self.transit=waiting
            for rid,last in self.last_delivery.items():
                if self.time-last>self.project.policy.stale_after:self.world.command(rid,mode="stop")
            self.world.step();self._evaluate();self._feedback()
            if not np.all(np.isfinite(self.world.data.qpos)):
                self.status="failed";self.emit("simulation_failed",None,"물리 상태가 유한하지 않습니다",{});break
            if self.time+1e-10>=self.next_frame:
                self.frames.append(dict(time=self.time,qpos=self.world.data.qpos.tolist(),qvel=self.world.data.qvel.tolist(),ctrl=self.world.data.ctrl.tolist(),robots={r.id:deepcopy(self.previous[r.id]) for r in self.project.robots},battery=self.batteries.copy()))
                self.next_frame+=.1
            if (self.project.auto_stop_after_seconds is not None or self.stop_when_tasks_terminal) and self.status!="failed":
                rows=self.orchestrator.task_rows()
                if rows and all(row['status'] in ('completed','failed','cancelled','skipped') for row in rows):
                    failed=[row for row in rows if row['status'] not in ('completed','skipped')]
                    self.status='failed' if failed else 'completed'
                    reason='; '.join(f"{row['name']}: {row.get('reason') or row['status']}" for row in failed) if failed else '모든 작업 완료'
                    self.emit('scenario_stopped' if self.stop_when_tasks_terminal else 'sample_stopped',None,reason,dict(result=self.status,limit_s=self.project.auto_stop_after_seconds))
                    break
                if self.project.auto_stop_after_seconds is not None and self.time+1e-10>=self.project.auto_stop_after_seconds:
                    self.status='timed_out'
                    reasons=[]
                    for row in rows:
                        if row['status']=='completed':continue
                        state=self.orchestrator.robot_states.get(row.get('robot_id'),{})
                        current=state.get('reason') if row['status']=='running' else row.get('reason')
                        reasons.append(f"{row['name']}: {current or row.get('reason') or row['status']}")
                    self.emit('sample_stopped',None,f"{self.project.auto_stop_after_seconds:g}초 제한 도달 · {'; '.join(reasons)}",dict(result=self.status,limit_s=self.project.auto_stop_after_seconds))
                    break
            if self.replan_watch:
                watched=self.orchestrator.tasks.get(self.replan_watch['task_id'])
                if watched and watched['status'] in ('completed','cancelled','failed','skipped'):
                    self.replan_watch=None
                elif self.time>=self.replan_watch['until']:
                    self.status='paused'
                    self.emit('replan_attention_required',self.replan_watch['task_id'],
                              '승인한 관측 시간 상한 도달 · 다음 조치가 필요합니다',dict(self.replan_watch))
                    self.replan_watch=None
                    break
        self.compute_seconds+=time.perf_counter()-start

    def _feedback(self):
        for command_id,record in self.command_records.items():
            if record["status"] in ("completed","failed","rejected","expired"):continue
            if record.get("expires_at") is not None and time.time()>record["expires_at"]:
                self.orchestrator.manual(record["robot_id"],"stop",None,self.time)
                record.update(status="expired",reason="명령 실행 기한 만료: 제동 요청")
                self.emit("command_expired",record["robot_id"],record["reason"],record)
                continue
            rid=record["robot_id"];obs=self.observations.get(rid)
            if obs is None or obs["sampled_at"]<=record["requested_at"]:continue
            record["status"]="executing"
            if self.time-record["requested_at"]>30:
                record.update(status="failed",reason="명령 확인 시간 초과");continue
            if record["kind"]=="move":
                from .orchestration import angle
                target=record["target"]
                reached=math.hypot(obs["pose"]["x"]-target["x"],obs["pose"]["y"]-target["y"])<.25 and abs(angle(obs["pose"]["yaw"]-target["yaw"]))<.12 and np.linalg.norm(obs["velocity"])<.12 and np.linalg.norm(obs["angular_velocity"])<.12
                if reached:
                    if record.get("stable_since") is None:record["stable_since"]=obs["sampled_at"]
                    if obs["sampled_at"]-record["stable_since"]>=.35:record["status"]="completed"
                else:record["stable_since"]=None
            else:
                stable=np.linalg.norm(obs["velocity"])<.08 and np.linalg.norm(obs["angular_velocity"])<.12 and obs["upright"]>.95
                robot=next(r for r in self.project.robots if r.id==rid)
                floor=min(self.project.environment.floors,key=lambda f:abs(obs["pose"]["z"]-f.elevation-.35))
                height=obs["pose"]["z"]-floor.elevation
                if robot.model_id=="spot":
                    stable=stable and ((.18<height<.31) if record["kind"]=="sit" else (.40<height<.53))
                if stable:
                    if record.get("stable_since") is None:record["stable_since"]=obs["sampled_at"]
                    if obs["sampled_at"]-record["stable_since"]>=.35:record["status"]="completed"
                else:record["stable_since"]=None
            if record["status"]=="completed":
                record["completed_at"]=self.time
                record["evidence"]={"source":"observation","sampled_at":obs["sampled_at"],"criterion":"목표 도달·속도·자세 관측 판정"}
                self.emit("command_completed",rid,"관측으로 명령 결과 확인",record)

    def command(self,robot_id,kind,target=None,*,expires_at=None):
        if expires_at is not None and expires_at<=time.time():raise ValueError("만료된 명령")
        result=self.orchestrator.manual(robot_id,kind,target,self.time)
        for previous in self.command_records.values():
            if previous["robot_id"]==robot_id and previous["status"] in ("accepted","executing"):
                previous.update(status="failed",reason="새 명령으로 대체됨",superseded=True)
                self.emit("command_superseded",robot_id,"기존 명령 종료",previous)
        record=dict(result,command_id=uuid4().hex,robot_id=robot_id,expires_at=expires_at,target=deepcopy(target))
        self.orchestrator.robot_states[robot_id]["last_command"]["command_id"]=record["command_id"]
        self.command_records[record["command_id"]]=record
        return deepcopy(record)

    def robot_observation(self,robot_id):
        if robot_id not in self.observations:raise ValueError("관측이 아직 없습니다")
        return dict(deepcopy(self.observations[robot_id]),simulation_time=self.time,powered=bool(self.observations[robot_id]["battery"]>0),estopped=False)

    def resume_robot(self,robot_id):
        receipt=self.orchestrator.resume(robot_id,self.time)
        if receipt["status"]=="accepted":
            for record in self.command_records.values():
                if record["robot_id"]==robot_id and record["status"] in ("accepted","executing"):
                    record.update(status="failed",reason="명시적 운영 재개 요청으로 대체됨",superseded=True)
        return receipt

    def recover_cooperation(self,task_id,actor_id,destination=None,*,request_id=None,retry=False,timeout=90.):
        return self.cooperative.recovery.start(task_id,actor_id,destination,self.time,self.observations,
            request_id=request_id,retry=retry,timeout=timeout)

    def cancel_cooperation_recovery(self,task_id,recovery_id):
        e=self.cooperative.executions.get(task_id)
        if not e or e.get('recovery',{}).get('recovery_id')!=recovery_id:
            raise ValueError('현재 복구 요청 ID와 일치하지 않습니다')
        self.cooperative.recovery.stop(task_id,self.time,'사용자 복구 중단',cancelled=True)
        return self.cooperative.recovery.receipt(e)

    def command_feedback(self,command_id):return dict(deepcopy(self.command_records[command_id]),observed_at=self.time)

    def metrics(self):
        rows=self.orchestrator.task_rows();completed=[t for t in rows if t["status"]=="completed"]
        finished=[t for t in rows if t["status"] in ("completed","failed")]
        times=[t["completed_at"]-t["started_at"] for t in completed]
        result=dict(task_count=len(rows),completed=len(completed),failed=sum(t["status"]=="failed" for t in rows),success_rate=len(completed)/len(finished) if finished else None,throughput_per_hour=len(completed)/self.time*3600 if self.time else 0,mean_completion_seconds=float(np.mean(times)) if times else None,distance_m=sum(self.distances.values()),energy_j=sum(self.energy.values()),collisions=self.collision_count,near_misses=self.near_count,falls=len(self.fallen),damaged_items=len(self.damaged),physics_realtime_factor=self.time/self.compute_seconds if self.compute_seconds else None,compute_seconds=self.compute_seconds,orchestration_mean_ms=float(np.mean(self.orchestration_latencies))*1000 if self.orchestration_latencies else None,orchestration_max_ms=max(self.orchestration_latencies,default=0)*1000,peak_process_memory_native=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,allocation_imbalance=max(self.orchestrator.count.values(),default=0)-min(self.orchestrator.count.values(),default=0),per_robot={r.id:dict(distance_m=self.distances[r.id],energy_j=self.energy[r.id],assignments=self.orchestrator.count[r.id],utilization=self.busy_seconds[r.id]/self.time if self.time else 0,waiting_seconds=self.wait_seconds[r.id],completed=sum(t["robot_id"]==r.id for t in completed)) for r in self.project.robots})


        result["per_type"]={}
        recoveries=[event for event in self.events if event['kind']=='cooperation_recovery_completed']
        result['cooperative_recovery']=dict(
            started=sum(event['kind']=='cooperation_recovery_started' for event in self.events),
            completed=len(recoveries),
            failed_or_cancelled=sum(event['kind']=='cooperation_recovery_failed' for event in self.events),
            mean_active_seconds=float(np.mean([event['details']['duration_s'] for event in recoveries])) if recoveries else None,
            mean_failure_to_recovery_seconds=float(np.mean([event['details']['failure_to_recovery_s'] for event in recoveries])) if recoveries else None)
        result['charging_input_j']=sum(self.charge_input.values())
        result['charging_stored_j']=sum(self.charge_stored.values())
        result['energy_demand_j']=sum(self.energy_demand.values())
        result['unserved_energy_j']=sum(self.energy_unserved.values())
        if self.project.people:
            result['pedestrian_min_clearance_m']=deepcopy(self.pedestrian_min_clearance)
            result['pedestrian_min_clearance_basis']='actual planar circumscribed robot radius and person torso radius at every physics step'
        if self.project.policy.pedestrian_avoidance is not None:
            result['pedestrian_safety']=dict(desired_clearance_m=self.project.policy.pedestrian_avoidance.desired_clearance_m,
                actual_min_clearance_m=deepcopy(self.pedestrian_min_clearance),
                basis='actual planar circumscribed robot radius and person torso radius; evaluator only',
                observation_model='ideal_visible_person_tracker_v1 with geometric occlusion, configured delay/noise/dropout')
        elevator=self.elevator_metrics.snapshot(self.time)
        charging=self.charging_metrics.snapshot(self.time)
        result['facilities']={**elevator['facilities'],**charging['facilities']}
        result['facility_queue_wait_seconds']=elevator['totals']['queue_wait_seconds']+charging['totals']['queue_wait_seconds']
        result['charging_queue_wait_seconds']=charging['totals']['queue_wait_seconds']
        result['facility_fault_seconds']=elevator['totals']['fault_seconds']+charging['totals']['fault_seconds']
        result['facility_metrics_basis']='manager-state transition intervals; robot-seconds for queue wait; facility-seconds for faults; see docs/facility-metrics.md'
        for rid,individual in result['per_robot'].items():
            individual['cooperative_completed_participations']=sum(rid in t.get('participant_ids',[]) for t in completed)
            individual.update(charging_input_j=self.charge_input[rid],charging_stored_j=self.charge_stored[rid],energy_demand_j=self.energy_demand[rid],unserved_energy_j=self.energy_unserved[rid])
            individual['facility_queue_wait_seconds']=sum(group['robots'].get(rid,{}).get('queue_wait_seconds',0.) for group in (elevator,charging))
            individual['charging_queue_wait_seconds']=charging['robots'].get(rid,{}).get('queue_wait_seconds',0.)
        for robot in self.project.robots:
            group=result["per_type"].setdefault(robot.model_id,dict(robot_count=0,completed=0,cooperative_completed_participations=0,assignments=0,busy_seconds=0.,distance_m=0.,energy_j=0.,waiting_seconds=0.))
            individual=result["per_robot"][robot.id]
            group["robot_count"]+=1
            for metric in ("completed","cooperative_completed_participations","assignments","distance_m","energy_j","waiting_seconds"):group[metric]+=individual[metric]
            group["busy_seconds"]+=self.busy_seconds[robot.id]
        for group in result["per_type"].values():
            group["utilization"]=group["busy_seconds"]/(self.time*group["robot_count"]) if self.time else 0.
            group["completion_share"]=group["completed"]/len(completed) if completed else None
        return result

    def snapshot(self,include_geometry=True):
        robots=[]
        for r in self.project.robots:
            obs=self.observations.get(r.id); state=self.orchestrator.robot_states[r.id]
            latest=next((cmd for cmd in reversed(list(self.command_records.values())) if cmd["robot_id"]==r.id),state["last_command"])
            robots.append(dict(id=r.id,model_id=r.model_id,name=r.name,**self.world.truth(r.id),battery=self.batteries[r.id],charging_power_w=self.charge_power[r.id],charging_station_id=self.orchestrator.charging.plans.get(r.id,{}).get('station_id'),charging_energy=deepcopy(state.get('charging_energy')),charging_workflow=self.orchestrator.charging.workflow.snapshot(r.id,self.time),motion_limit=deepcopy(state.get('motion_limit')),consumption_meter=self.consumption_observations.report(r.id,self.time),status=state["status"],operator_hold=state["operator_hold"],task_id=state["task_id"],path=deepcopy(state["path"]),observation_age=self.time-obs["sampled_at"] if obs else None,reason=state["reason"],sensors=deepcopy(obs["sensors"]) if obs else {},last_command=deepcopy(latest),payload=[dict(id=item.id,name=item.name,mass=item.mass,custody=self.item_custody_status[item.id]) for item in self.project.items if self.item_custody[item.id]==r.id],equipment=[e.model_dump() for e in r.equipment],observed_pose=deepcopy(obs["pose"]) if obs else None))
        for row in robots:row['pedestrian_avoidance']=deepcopy(self.orchestrator.robot_states[row['id']].get('pedestrian_avoidance'))
        people=deepcopy(self.pedestrian_states)
        for person in self.project.people:
            body=self.world.model.body(person.id+'/body').id;velocity=np.zeros(6)
            mujoco.mj_objectVelocity(self.world.model,self.world.data,mujoco.mjtObj.mjOBJ_BODY,body,velocity,0)
            speed=math.hypot(*velocity[3:5])
            # Presentation orientation follows physical translation, never the
            # requested actuator velocity. It does not alter any physics state.
            heading=math.atan2(velocity[4],velocity[3]) if speed>.01 else self.pedestrian_headings[person.id]
            people.setdefault(person.id,{}).update(actual_position=self.world.data.xpos[body].tolist(),
                actual_velocity=velocity[3:].tolist(),actual_speed_m_s=speed,actual_heading_rad=heading,sampled_at=self.time,
                behavior=person.behavior.mode if person.behavior else 'legacy',
                destination=people.get(person.id,{}).get('destination'),
                allowed_floor_ids=list(person.behavior.allowed_floor_ids or [person.floor_id]) if person.behavior else [person.floor_id],
                allowed_zone_ids=list(person.behavior.allowed_zone_ids) if person.behavior else [])
        items=[]
        for item in self.project.items:
            body=self.world.model.body(item.id+'/body').id
            items.append(dict(id=item.id,name=item.name,position=self.world.data.xpos[body].tolist(),
                owner=self.item_custody[item.id],custody=self.item_custody_status[item.id],
                damaged=item.id in self.damaged,sampled_at=self.time,basis='simulation_physics_state'))
        return dict(run_id=self.run_id,status=self.status,speed=self.speed,sim_time=self.time,wall_time=time.monotonic()-self.started_wall,project_revision=self.project.revision,incidents=self.incident_scheduler.snapshot(self.injections),robots=robots,tasks=self.orchestrator.task_rows(),cooperation=self.cooperative.snapshot(),items=items,people=people,facilities=deepcopy(list(self.facility_states.values())),events=deepcopy(self.events[-250:]),metrics=self.metrics(),geoms=self.world.geometries() if include_geometry else [],warnings=self.warnings.copy(),fidelity=self.project.physics.fidelity,render_hz=self.project.physics.render_hz)

    def recording(self):
        return dict(run_id=self.run_id,project=self.project.model_dump(),frames=self.frames,events=self.events,metrics=self.metrics(),semantics="recorded-state playback; not physics recomputation")
