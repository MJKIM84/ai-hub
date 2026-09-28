"""Observation-only route and motion integration for reserved research docks."""
from copy import deepcopy
import math
import json

from .catalog import model_by_id
from .charging import ChargingManager
from .navigation import radius
from .motion_limits import route_timing, translation_time
from .guided_route import DirectedRoute,GuidedRouteError
from .charging_energy import ChargingEnergy,VERSION as ENERGY_VERSION,IDLE_POWER_W,RESERVE_SECONDS,travel
from .charging_target import plan_target,finite,service_ready
from .charging_traffic import ChargingTraffic
from .navigation import path_clear_of_disks
from .charging_access import parking_blocks_service, exit_route, initial_exit_anchor_valid
from .charging_workflow import ChargingWorkflow


def angle(value):
    return (value + math.pi) % (2 * math.pi) - math.pi


class ChargingControl:
    def __init__(self, orchestrator):
        self.owner = orchestrator
        self.project = orchestrator.project
        self.manager = ChargingManager(self.project)
        self.geometry = {}
        self.plans = {}
        self.intentions = {}
        self.power_requests = {}
        self.station_observations = {}
        self.departure_history = {}
        self.energy = ChargingEnergy(self)
        self.energy_observations = {}
        self.energy_observation_errors = {}
        self._energy_history = {}
        self._energy_station_history = {}
        self.energy_station_errors = {}
        self.energy_now = None
        self.traffic = ChargingTraffic(self)
        self.workflow = ChargingWorkflow(self)

    def available(self, element):
        reading=self.station_observations.get(element.id)
        fault=reading.get('fault',True) if isinstance(reading,dict) else element.facility.fault
        return element.facility.automatic and not fault and not self.manager.stations[element.id].fault_latched

    def compatible(self,robot,element):
        model=model_by_id(robot.model_id)
        mass=model['mass']+robot.payload_mass+sum(e.mass for e in robot.equipment)
        return (self.available(element) and mass<=element.facility.max_load and robot.payload_mass<=model['max_payload']
                and (not element.allowed_groups or robot.group in element.allowed_groups))

    def configure(self, geometries):
        # Geometry is a static model contract, not a simulator truth handle.
        self.geometry = deepcopy(geometries)

    def _observe_energy(self,now,observations):
        self.energy_now=now
        self.energy_observations={};self.energy_observation_errors={}
        for rid in self.owner.robots:
            obs=observations.get(rid);error=None
            stamp=obs.get('sampled_at') if isinstance(obs,dict) else None
            if (not isinstance(stamp,(int,float)) or isinstance(stamp,bool) or not math.isfinite(stamp)
                    or stamp>now or now-stamp>self.owner.policy.stale_after):error='missing_or_stale_robot_observation'
            elif (obs.get('robot_id')!=rid or not isinstance(obs.get('pose'),dict)
                    or any(not isinstance(obs['pose'].get(k),(int,float)) or isinstance(obs['pose'].get(k),bool) or not math.isfinite(obs['pose'][k]) for k in ('x','y','z','yaw'))
                    or not isinstance(obs.get('battery'),(int,float)) or isinstance(obs.get('battery'),bool) or not math.isfinite(obs['battery']) or not 0<=obs['battery']<=100
                    or not isinstance(obs.get('fault'),str) or not obs['fault']
                    or not isinstance(obs.get('upright'),(int,float)) or isinstance(obs.get('upright'),bool) or not math.isfinite(obs['upright'])):error='invalid_robot_energy_observation'
            else:
                try:signature=json.dumps(obs,sort_keys=True,allow_nan=False)
                except (ValueError,TypeError):
                    self.energy_observation_errors[rid]='invalid_robot_energy_observation'
                    continue
                previous=self._energy_history.get(rid)
                if previous and (stamp<previous[0] or (stamp==previous[0] and signature!=previous[1])):error='reordered_or_changed_robot_observation'
                else:
                    self._energy_history[rid]=(stamp,signature)
                    self.energy_observations[rid]=deepcopy(obs)
            if error:self.energy_observation_errors[rid]=error
        self.energy_station_errors={}
        for eid in self.manager.stations:
            reading=self.station_observations.get(eid)
            if not isinstance(reading,dict):self.energy_station_errors[eid]='missing_station_observation';continue
            stamp=reading.get('sampled_at')
            if (not isinstance(stamp,(int,float)) or isinstance(stamp,bool) or not math.isfinite(stamp)
                    or stamp>now or now-stamp>self.owner.policy.stale_after):self.energy_station_errors[eid]='station_observation_not_fresh';continue
            try:signature=json.dumps(reading,sort_keys=True,allow_nan=False)
            except (ValueError,TypeError):self.energy_station_errors[eid]='invalid_station_observation';continue
            previous=self._energy_station_history.get(eid)
            if previous and (stamp<previous[0] or (stamp==previous[0] and signature!=previous[1])):self.energy_station_errors[eid]='reordered_or_changed_station_observation'
            else:self._energy_station_history[eid]=(stamp,signature)

    def _energy_candidates(self,robot,observation,now,floor_id=None,*,live_traffic=True):
        owner=self.owner;floor_id=floor_id or owner._floor(observation['pose']['z']);rows=[]
        capacity_j=robot.battery_capacity_wh*3600
        available=observation['battery']/100*capacity_j
        valid_capacity=math.isfinite(capacity_j) and capacity_j>0 and math.isfinite(available)
        for element in self.project.environment.elements:
            geometry=self.geometry.get((robot.id,element.id))
            if geometry is None or element.kind!='charger' or element.floor_id!=floor_id:continue
            row=dict(station_id=element.id,known=False,feasible=False,reason=None,available_j=available if valid_capacity else None,
                     queue_wait_seconds=None,wait_energy_j=None,approach_energy_j=None,dock_energy_j=None,required_before_contact_j=None,shortfall_j=None)
            rows.append(row)
            if not valid_capacity:row['reason']='nonfinite_battery_capacity';continue
            if not self.compatible(robot,element):row['reason']='station_incompatible_or_unavailable';continue
            if element.facility.charge_power_w*element.facility.charge_efficiency<=robot.estimated_drive_power_w:row['reason']='nonpositive_estimated_net_charge_power';continue
            if live_traffic:
                path,traffic_reason=self.traffic.route(robot,observation,geometry['staging'],floor_id,element.id,now,planning=True)
            else:
                path=owner._route(robot,observation,geometry['staging'],floor_id)
                traffic_reason='approach_route_unavailable'
            if path is None:row['reason']=traffic_reason;continue
            if robot.model_id=='agv':
                try:
                    if DirectedRoute([p.model_dump() for p in robot.agv_route]).waypoint(geometry['staging']) is None:row['reason']='staging_not_authored_waypoint';continue
                except GuidedRouteError:row['reason']='invalid_guided_route';continue
            exit_plan=dict(geometry=geometry,origin=observation['pose'],station_id=element.id)
            accepted=self.plans.get(robot.id)
            if accepted and accepted['station_id']==element.id:
                # Forecast the space actually committed to this request. A
                # cheaper newly visible exit is not an implicit reassignment.
                target=self._reserved_egress(accepted)
                if target is not None:exit_plan['egress_target']=target
            parking=self._parking(robot.id,{'pose':geometry['staging']},exit_plan,now,consider_occupancy=False)
            if parking is None:row['reason']='clearance_route_unavailable';continue
            a,b=geometry['staging'],geometry['target']
            if any(owner.planner.blocked(a['x']+(b['x']-a['x'])*part/20,a['y']+(b['y']-a['y'])*part/20,floor_id,robot,ignore_element=element.id) for part in range(21)):
                row['reason']='dock_branch_blocked';continue
            forecast=self.energy.queue(element.id,robot.id,now)
            row['queue_forecast']=forecast
            if not forecast['known']:row['reason']=forecast['reason'];continue
            own=self.energy.own_approach(robot,observation,path,geometry,floor_id)
            if not own['known']:
                row.update(own)
                continue
            needed=own['estimated_drive_j']+forecast['wait_energy_j']+IDLE_POWER_W*RESERVE_SECONDS
            trigger=needed/(robot.battery_capacity_wh*3600)*100+owner.policy.charge_below
            if not all(math.isfinite(value) for value in (available,needed,trigger)):
                row['reason']='nonfinite_approach_energy'
                row['available_j']=available if math.isfinite(available) else None
                continue
            row.update(own,known=True,queue_wait_seconds=forecast['queue_wait_seconds'],wait_energy_j=forecast['wait_energy_j'],reserve_j=IDLE_POWER_W*RESERVE_SECONDS,
                       required_before_contact_j=needed,shortfall_j=max(0.,needed-available),feasible=available>=needed,
                       trigger_percent=max(owner.policy.charge_below,trigger),
                       reason='energy_shortfall' if available<needed else None,path=path,geometry=geometry,parking=parking)
        return rows

    def _assessment(self,robot,obs,now):
        candidates=self._energy_candidates(robot,obs,now)
        viable=[row for row in candidates if row['feasible']]
        selected=min(viable,key=lambda row:(row['required_before_contact_j'],row['station_id'])) if viable else None
        known=[row for row in candidates if row['known']]
        best=selected or (min(known,key=lambda row:(row['required_before_contact_j'],row['station_id'])) if known else None)
        trigger=best['trigger_percent'] if best else None
        # Traffic availability cannot erase the configured energy need. The
        # static alternative is diagnostic only: selected remains a live,
        # accepted-observation admission candidate and still grants no motion.
        static_candidates=self._energy_candidates(robot,obs,now,live_traffic=False) if best is None else candidates
        static_known=[row for row in static_candidates if row['known']]
        static_best=min(static_known,key=lambda row:(row['required_before_contact_j'],row['station_id'])) if static_known else None
        need_trigger=static_best['trigger_percent'] if static_best else None
        if trigger is None:trigger=need_trigger
        # Paths/static geometry stay in the private plan, not a UI energy field.
        public=[{key:deepcopy(value) for key,value in row.items() if key not in ('path','geometry','parking')} for row in candidates]
        status='unknown' if best is None else 'insufficient' if selected is None else 'charge_early' if obs['battery']<trigger else 'sufficient'
        available=obs['battery']/100*robot.battery_capacity_wh*3600
        summary=dict(version=ENERGY_VERSION,sampled_at=obs['sampled_at'],assessed_at=now,status=status,trigger_percent=trigger,
                     selected_station_id=selected['station_id'] if selected else None,available_j=available if math.isfinite(available) else None,
                     access_status='available' if selected else 'blocked' if static_best else 'unknown',
                     reason=next((row['reason'] for row in candidates if row['reason']),None) if selected is None else None,
                     need_trigger_percent=need_trigger,
                     static_need_candidates=[{key:deepcopy(value) for key,value in row.items() if key not in ('path','geometry','parking')} for row in static_candidates] if best is None else [],
                     candidates=public,basis='Configured scheduling estimate, not measured consumption or guaranteed queue release; stationary demand20W, drive estimate per robot, charge input×efficiency minus configured drive demand')
        return summary,candidates,selected

    def task_budget(self, robot, task, observation, route, trip=None, *, projected_start=None):
        """Static route timing plus the present queue at a hypothetical task end.

        Current backlog is not discounted by task duration. These explicit
        scheduling assumptions grant neither a future reservation nor a bound
        on delays, traffic, actuator dynamics or actual consumption.
        """
        environment = self.project.environment
        return_required = any(element.kind == 'charger' and element.floor_id == task.floor_id
                              and (robot.model_id == 'agv' or (robot.id, element.id) in self.geometry)
                              for element in environment.elements)
        destination = task.cooperation.carrier_destination if task.cooperation else task.destination
        candidates = []
        work_time = None
        work_j = None

        def unknown(reason, observation_valid=True):
            return dict(energy_observation_valid=observation_valid, energy_estimate_valid=False,
                        reason=reason, required_percent=None, estimated_work_and_return_j=None,
                        estimated_work_j=work_j, estimated_return_j=None, work_time=work_time,
                        return_route_available=False, return_route_required=return_required,
                        queue_wait_seconds=None, queue_wait_energy_j=None, guided_return=None,
                        return_candidates=[{key: value for key, value in row.items()
                                            if key not in ('path', 'geometry', 'parking')}
                                           for row in candidates],
                        basis='Static motion or current observation is unavailable; no energy admission from an unknown duration')

        if self.energy_now is not None and self.energy_observations.get(robot.id) != observation:
            return unknown(self.energy_observation_errors.get(robot.id, 'unaccepted_current_robot_observation'),
                           observation_valid=False)
        start_pose = observation['pose'] if projected_start is None else projected_start
        if not isinstance(start_pose,dict) or any(not finite(start_pose.get(k)) for k in ('x','y','z','yaw')):
            return unknown('invalid_projected_task_start')
        if trip or task.kind == 'manipulate':
            # Existing whole-operation timeout budget is deliberately retained.
            work_time = dict(known=True, reason=None, seconds=task.timeout,
                             basis='Configured whole-operation timeout for elevator/manipulation; not a motion-time prediction')
        else:
            work_time = route_timing(robot, self.owner.policy, environment, start_pose,
                                     route, task.floor_id, final_yaw=destination.yaw, dwell=task.dwell)
            if not work_time['known']:
                return unknown(work_time['reason'])
            allowance = 1. if work_time['distance_m'] > .08 else 0.
            work_time = dict(work_time, arrival_allowance_seconds=allowance,
                             seconds=work_time['seconds'] + allowance,
                             basis='Static model/instance/policy and rotated same-floor zone caps, sequential route turns and final alignment; one-second arrival allowance above 0.08 m, not a guarantee')
        work_j = work_time['seconds'] * robot.estimated_drive_power_w
        if not math.isfinite(work_j):
            work_j = None
            return unknown('nonfinite_work_energy')
        now = self.energy_now if self.energy_now is not None else observation.get('sampled_at', 0.)
        end = deepcopy(observation)
        end['pose'] = dict(destination.model_dump(), z=self.owner.planner.floors[task.floor_id].elevation + .3)
        candidates = self._energy_candidates(robot, end, now, task.floor_id, live_traffic=False)
        known = [row for row in candidates if row['known']]
        selected = min(known, key=lambda row: (row['required_before_contact_j'], row['station_id'])) if known else None
        if return_required and selected is None:
            return unknown('return_route_unavailable')
        return_j = selected['required_before_contact_j'] if selected else 0.
        guided_return = None
        if selected and robot.model_id == 'agv':
            geometry = selected['geometry']
            parking = selected['parking']
            route_info = self.owner._guided_plan(robot, end, geometry['staging'], task.floor_id)
            departure = self.owner._guided_plan(robot, {'pose': geometry['staging']}, parking, task.floor_id)
            if route_info is None or departure is None:
                return unknown('guided_return_route_unavailable')
            undock = translation_time(robot, self.owner.policy, environment, geometry['target'],
                                      [geometry['staging']], task.floor_id, cap=.12)
            clearance = travel(robot, self.owner.policy, geometry['staging'], departure['points'],
                               parking['yaw'], environment, task.floor_id, preserve_corners=True)
            if not undock['known'] or not clearance['known']:
                return unknown((undock if not undock['known'] else clearance)['reason'])
            handoff = self.energy.handoff_estimate(robot)
            # Match the service forecast: one-second undock deceleration plus
            # the existing two0.3-second confirmations and stop handoff.
            extra_seconds = undock['seconds'] + 1. + clearance['seconds'] + .6 + handoff['seconds']
            return_j += extra_seconds * robot.estimated_drive_power_w
            guided_return = dict(station_id=selected['station_id'], route=route_info, departure=departure,
                                 route_distance_m=route_info['distance_m'], dock_distance_m=undock['distance_m'],
                                 undock_distance_m=undock['distance_m'], clearance_distance_m=clearance['distance_m'],
                                 undock_time=undock, clearance_time=clearance,
                                 handoff_seconds=handoff['seconds'], handoff_estimate=handoff,
                                 seconds=selected['approach_seconds'] + selected['dock_seconds'] + extra_seconds)
        joules = work_j + return_j
        capacity_j = robot.battery_capacity_wh * 3600
        if not math.isfinite(joules) or not math.isfinite(capacity_j) or capacity_j <= 0:
            return unknown('nonfinite_task_energy')
        required_percent = self.owner.policy.charge_below + joules / capacity_j * 100
        if not math.isfinite(required_percent):
            return unknown('nonfinite_task_energy')
        return dict(energy_observation_valid=True, energy_estimate_valid=True, required_percent=required_percent,
                    estimated_work_and_return_j=joules, estimated_work_j=work_j, estimated_return_j=return_j,
                    work_time=work_time,
                    queue_wait_seconds=selected['queue_wait_seconds'] if selected else None,
                    queue_wait_energy_j=selected['wait_energy_j'] if selected else None,
                    return_route_available=bool(selected), return_route_required=return_required,
                    guided_return=guided_return,
                    return_candidates=[{key: value for key, value in row.items()
                                        if key not in ('path', 'geometry', 'parking')} for row in candidates],
                    basis='Configured drive power, static route timing and current queue workload; low-speed approach/dock; not calibrated or guaranteed')

    def prepare(self, now, observations):
        self._prepare(now, observations)
        self.workflow.observe(now)

    def _prepare(self, now, observations):
        owner = self.owner
        self._observe_energy(now,observations)
        for rid, state in owner.robot_states.items():
            observation = observations.get(rid)
            if rid in self.plans:
                plan=self.plans[rid]
                req=self.manager.requests.get(plan['request_id'])
                self._release_cancelled_egress(plan)
                if req and req.status=='cancelled' and req.phase=='cancelled':
                    # A queued cancellation is terminal without any movement.
                    # Manager's generic terminal "done" intention is not an
                    # observed undock and cannot start a clearance departure.
                    if not plan.get('interrupted'):state['command_epoch']+=1
                    plan['interrupted']=True
                    plan['clear_since']=None
                    self.power_requests.pop(rid,None)
                    state['path']=[]
                    if not state['operator_hold'] and state['status'] not in ('fault','disconnected'):
                        state.update(status='recovery_required',reason='충전 대기 예약 취소: 명시적 운영 재개 필요')
                    state['charging_energy']=dict(version=ENERGY_VERSION,sampled_at=observation.get('sampled_at') if isinstance(observation,dict) else None,
                        assessed_at=now,status='unknown',selected_station_id=None,trigger_percent=None,candidates=[],reason='charge_request_cancelled',
                        target_plan=deepcopy(plan.get('target_plan')),
                        basis='Unstarted cancelled request owns no connector or exit; explicit resume required')
                    continue
                if rid in self.energy_observations and req and req.status=='queued':
                    state['charging_energy']=self._assessment(owner.robots[rid],observation,now)[0]
                    state['charging_energy']['status']='queued'
                else:
                    state['charging_energy']=dict(version=ENERGY_VERSION,sampled_at=observation.get('sampled_at') if isinstance(observation,dict) else None,assessed_at=now,
                        status='unknown' if rid not in self.energy_observations else 'in_progress',selected_station_id=plan['station_id'],trigger_percent=None,candidates=[],
                        reason=self.energy_observation_errors.get(rid),basis='Existing reservation is retained; forecast grants neither contact nor completion')
                state['charging_energy']['target_plan']=deepcopy(plan.get('target_plan'))
                intention = self.intentions.get(rid, {})
                action = intention.get('action')
                if state['operator_hold']:
                    self.interrupt(rid,'operator_hold')
                    continue
                if state['status'] in ('fault', 'disconnected'):
                    self.interrupt(rid,state['status'])
                    continue
                if self.plans[rid].get('interrupted'):
                    reason=plan.get('interruption_reason') or '충전 중단 후 명시적 운영 재개 필요'
                    reason={'clearance_timeout':'충전 통로 비움 제한 시간 초과: 경로와 점유를 확인한 뒤 운영 재개 필요',
                            'clearance_route_unavailable':'충전 통로 밖 대기 위치 또는 경로 확보 후 운영 재개 필요'}.get(reason,reason)
                    state.update(status='recovery_required',reason=reason)
                    continue
                if self.plans[rid].get('clearing'):
                    plan=self.plans[rid]
                    if now-plan.get('clearance_started_at',now)>self.manager.phase_timeouts['approach']:
                        self.interrupt(rid,'clearance_timeout')
                        state.update(status='recovery_required',path=[],reason='충전 통로 비움 제한 시간 초과: 경로와 점유를 확인한 뒤 운영 재개 필요')
                        continue
                    stamp=observation.get('sampled_at') if isinstance(observation,dict) else None
                    if (not isinstance(stamp,(int,float)) or not math.isfinite(stamp) or stamp>now+1e-9
                            or now-stamp>owner.policy.stale_after or stamp<plan.get('clear_sampled_at',-math.inf)):
                        plan['clear_since']=None
                        continue
                    if stamp==plan.get('clear_sampled_at'):continue
                    plan['clear_sampled_at']=stamp
                    target=plan['parking']
                    pose=observation['pose']
                    settled=(math.hypot(pose['x']-target['x'],pose['y']-target['y'])<.08
                             and abs(angle(pose['yaw']-target['yaw']))<.1
                             and math.sqrt(sum(v*v for v in observation['velocity']))<.04)
                    if settled:
                        if plan.get('clear_since') is None:plan['clear_since']=observation['sampled_at']
                    else:plan['clear_since']=None
                    if plan.get('clear_since') is not None and observation['sampled_at']-plan['clear_since']>=.3:
                        station=self.plans.pop(rid)['station_id']
                        self.departure_history[rid]=dict(battery=observation['battery'],pose=deepcopy(pose),completed_at=now,
                            target_plan=deepcopy(plan.get('target_plan')))
                        if owner.policy.charge_target_mode=='task_budget':
                            # Compare later maintenance needs with the threshold
                            # observed at departure, never a retroactive queue.
                            rejections=deepcopy(owner.guided_rejections)
                            try:
                                self.departure_history[rid]['route_trigger_percent']=self._assessment(owner.robots[rid],observation,now)[0]['trigger_percent']
                            finally:
                                owner.guided_rejections.clear();owner.guided_rejections.update(rejections)
                        state.update(status='idle',path=[],reason='충전 접점 분리와 공용 접근 통로 비움 확인')
                        state['command_epoch']+=1
                        owner.emit('charging_completed',rid,state['reason'],dict(station_id=station))
                    else:
                        state.update(status='charging',reason='다음 로봇을 위해 충전 접근 통로 비우기')
                    continue
                if action == 'done':
                    plan=self.plans[rid]
                    parking=self._parking(rid,observation,plan,now)
                    if parking is None:
                        self.interrupt(rid,'clearance_route_unavailable')
                        state.update(status='recovery_required',reason='충전 통로 밖 대기 위치 또는 경로 확보 후 운영 재개 필요')
                        continue
                    # The selected footprint is owned by this unfinished plan,
                    # including while it is stopped or waiting for recovery.
                    plan.update(clearing=True,parking=parking,clearance_started_at=now,
                                parking_floor_id=owner._floor(observation['pose']['z']),route_started=False)
                    if owner.robots[rid].model_id=='agv':
                        plan['guided_departure']=owner._guided_plan(owner.robots[rid],observation,parking,owner._floor(observation['pose']['z']))
                    state.update(status='charging',path=[],reason='충전 후 공용 접근 통로에서 이동')
                    state['command_epoch']+=1
                    owner.emit('charging_departure',rid,state['reason'],dict(station_id=plan['station_id'],target=parking))
                elif action == 'fault':
                    if state['status'] != 'recovery_required':
                        state['command_epoch'] += 1
                    state.update(status='recovery_required', reason=intention.get('reason', '충전 복구 필요'))
                else:
                    state.update(status='charging', reason=intention.get('reason', '충전 시설 예약 대기'))
                continue
            stamp=observation.get('sampled_at') if isinstance(observation,dict) else None
            if rid not in self.energy_observations:
                state['charging_energy']=dict(version=ENERGY_VERSION,sampled_at=stamp,assessed_at=now,status='unknown',reason=self.energy_observation_errors.get(rid),trigger_percent=None,selected_station_id=None,candidates=[])
                continue
            if not isinstance(stamp,(int,float)) or not math.isfinite(stamp) or stamp>now+1e-9 or now-stamp > owner.policy.stale_after:
                continue
            if state['operator_hold'] or observation['fault'] != 'none' or observation['battery'] <= 0:
                continue
            robot=owner.robots[rid]
            summary,candidates,selected=self._assessment(robot,observation,now)
            state['charging_energy']=summary
            # Forecasts remain visible, but charging cannot replace an item,
            # facility or fault recovery reason with a lower-priority need.
            if state['status'] not in ('idle','working'):
                continue
            if owner.policy.charge_target_mode=='task_budget':
                self._prepare_adaptive(robot,state,observation,now,summary,candidates,selected)
                continue
            needed=max(owner.policy.charge_below,state.get('charge_needed_percent',0),summary['trigger_percent'] or 0)
            # Report the same threshold used below, including a pending task's
            # work-and-return budget. A valid route estimate alone can otherwise
            # say "sufficient" in the very event that requests task-driven charge.
            summary['route_trigger_percent']=summary['trigger_percent']
            summary['task_needed_percent']=state.get('charge_needed_percent')
            if summary['trigger_percent'] is not None:
                summary['trigger_percent']=needed
                if selected is not None:
                    summary['status']='charge_early' if observation['battery']<needed else 'sufficient'
            if observation['battery']>=needed:
                state.pop('charge_needed_percent',None)
                continue
            last=self.departure_history.get(rid)
            if (owner.policy.charge_target_mode=='fixed' and last and needed>last['battery'] and math.hypot(observation['pose']['x']-last['pose']['x'],observation['pose']['y']-last['pose']['y'])<.2):
                state['reason']='충전 종료 기준으로 통로 복귀 후 작업 예비량 확보 불가: 종료 기준·용량·업무 조건 조정 필요'
                state['charging_energy']['status']='policy_insufficient'
                continue
            if selected is None:
                reasons=','.join(sorted({r['reason'] for r in candidates if r['reason']})) or 'no_compatible_station'
                state['reason']='충전 필요: 큐 대기·접근·도킹 에너지 또는 경로 예측 불가/부족 ('+reasons+')'
                continue
            # A held load or elevator ride must finish its specific recovery first.
            if state.get('trip') or any(rid in owners for resource, owners in owner.reservations.owners.items() if resource.startswith('item:')):continue
            if state['status']=='working' and state['task_id']:
                owner._failure(state['task_id'],now,'충전 큐·복귀 예비량 기준 도달: 작업 회수 후 조기 충전 계획')
            if state['status']!='idle':continue
            candidates=[row for row in candidates if row['feasible']]
            receipt=None
            admission_wait_reason=None
            admission_wait_status='waiting_for_egress'
            for candidate in sorted(candidates,key=lambda row:(row['required_before_contact_j'],row['station_id'])):
                station=candidate['station_id'];path=candidate['path'];geometry=candidate['geometry'];approach_budget={k:v for k,v in candidate.items()if k not in ('path','geometry','parking')}
                # A forecast can ignore transient occupancy, but committing a
                # future parking footprint must not bind an already parked
                # robot's space when another observed-clear exit is available.
                exit_target=self._parking(rid,{'pose':geometry['staging']},dict(geometry=geometry,origin=observation['pose'],station_id=station),now,admission=True)
                if exit_target is None:
                    admission_wait_reason='충전 후 이동할 공간의 현재 점유 해제 대기'
                    continue
                exit_path=self._exit_route(robot,{'pose':geometry['staging']},exit_target,owner._floor(geometry['staging']['z']),now,dict(station_id=station),planning=True)
                if exit_path is None:
                    admission_wait_reason='충전 후 이동 경로 재확인 필요'
                    continue
                target_plan=plan_target(self,robot,observation,geometry,exit_target,exit_path,now)
                target_plan['station_id']=station
                target_plan['service_target']['station_id']=station
                state['charging_energy']['target_plan']=deepcopy(target_plan)
                if target_plan['status']!='ready':
                    admission_wait_reason='예정 작업의 충전 목표 계산 불가 또는 배터리 용량 초과'
                    admission_wait_status='waiting_for_target'
                    state['charging_energy'].update(status='policy_insufficient' if target_plan['status']=='infeasible' else 'unknown',reason=target_plan['reason'])
                    continue
                previous_target=(last or {}).get('target_plan') or {}
                previous_percent=previous_target.get('target_percent')
                if not finite(previous_percent):previous_percent=owner.policy.charge_until
                if (owner.policy.charge_target_mode=='task_budget' and last and needed>last['battery']
                        and math.hypot(observation['pose']['x']-last['pose']['x'],observation['pose']['y']-last['pose']['y'])<.2
                        and (target_plan['task_id']==previous_target.get('task_id')
                            or target_plan['target_percent']<=previous_percent)):
                    admission_wait_reason='예정 목표로 충전 후에도 작업 예비량 부족: 시간·소비 예측 또는 업무 조건 조정 필요'
                    admission_wait_status='waiting_for_target'
                    state['charging_energy']['status']='policy_insufficient'
                    continue
                try:
                    request_geometry={key:geometry[key] for key in ('staging','target')}
                    if owner.policy.charge_target_mode=='fixed':
                        receipt=self.manager.request(station,rid,now,request_geometry)
                    else:
                        receipt=self.manager.request(station,rid,now,request_geometry,target_percent=target_plan['target_percent'])
                    target_plan['request_id']=receipt['request_id']
                    target_plan['service_target']['request_id']=receipt['request_id']
                    # Earlier candidates may have an unknown or over-capacity
                    # target. A successful alternate admission has its own
                    # station, approach threshold and ready target report.
                    state['charging_energy'].update(status='charge_early',reason=None,
                        selected_station_id=station,route_trigger_percent=candidate['trigger_percent'],
                        trigger_percent=max(owner.policy.charge_below,state.get('charge_needed_percent',0),candidate['trigger_percent']),
                        target_plan=deepcopy(target_plan))
                    break
                except ValueError as exc:
                    state['reason'] = str(exc)
            if receipt is None:
                if admission_wait_reason:
                    state['reason']=admission_wait_reason
                    state['charging_energy']['admission_status']=admission_wait_status
                continue
            # Admission is serialized in this loop: commit the chosen exit
            # only after the connector request succeeds, before assessing the
            # next robot. Forecast candidates themselves own no space.
            self.plans[rid] = dict(station_id=station, geometry=geometry, path=path, route_started=False, requested_at=now,request_id=receipt['request_id'],origin=deepcopy(observation['pose']),
                                  egress_target=deepcopy(exit_target),
                                  egress_route=deepcopy([geometry['staging'],*exit_path]),
                                  egress_floor_id=owner._floor(geometry['staging']['z']),target_plan=deepcopy(target_plan))
            if approach_budget is not None:self.plans[rid]['approach_budget']=approach_budget
            if robot.model_id=='agv':self.plans[rid]['guided_approach']=owner._guided_plan(robot,observation,geometry['staging'],owner._floor(observation['pose']['z']))
            state.pop('charge_needed_percent',None)
            state.update(status='charging', path=[], reason='충전 큐·접근 예비량에 따른 시설 예약 요청')
            state['command_epoch'] += 1
            owner.emit('charging_requested', rid, state['reason'], dict(receipt,energy_forecast=deepcopy(state['charging_energy']),
                       egress_reservation=dict(target=deepcopy(exit_target),floor_id=self.plans[rid]['egress_floor_id'])))

    def _prepare_adaptive(self,robot,state,observation,now,summary,candidates,selected):
        owner=self.owner;rid=robot.id
        last=self.departure_history.get(rid)
        if (last and finite(summary['trigger_percent']) and observation['battery']>=summary['trigger_percent']
                and now>=last['completed_at']):
            # A later known, sufficient observation also establishes a safe
            # interval when the departure-time queue itself was unknown.
            last['reserve_ready_observed']=True
        task_needed=state.get('charge_needed_percent',0)
        legacy_needed=max(owner.policy.charge_below,task_needed,summary['trigger_percent'] or 0)
        summary.update(route_trigger_percent=summary['trigger_percent'],task_needed_percent=state.get('charge_needed_percent'))
        if observation['battery']>=legacy_needed:
            state.pop('charge_needed_percent',None)
            return
        if selected is None:
            reasons=','.join(sorted({row['reason'] for row in candidates if row['reason']})) or 'no_compatible_station'
            state['reason']='충전 필요: 큐 대기·접근·도킹 에너지 또는 경로 예측 불가/부족 ('+reasons+')'
            return
        if state.get('trip') or any(rid in owners for resource,owners in owner.reservations.owners.items() if resource.startswith('item:')):
            return
        if state['status'] not in ('idle','working'):
            return
        options=[];wait_reason=None;wait_status='waiting_for_egress'
        for candidate in sorted((row for row in candidates if row['feasible']),key=lambda row:(row['required_before_contact_j'],row['station_id'])):
            geometry=candidate['geometry'];station=candidate['station_id']
            exit_target=self._parking(rid,{'pose':geometry['staging']},dict(geometry=geometry,origin=observation['pose'],station_id=station),now,admission=True)
            if exit_target is None:
                wait_reason='충전 후 이동할 공간의 현재 점유 해제 대기'
                continue
            exit_path=self._exit_route(robot,{'pose':geometry['staging']},exit_target,owner._floor(geometry['staging']['z']),now,dict(station_id=station),planning=True)
            if exit_path is None:
                wait_reason='충전 후 이동 경로 재확인 필요'
                continue
            target=plan_target(self,robot,observation,geometry,exit_target,exit_path,now)
            target['station_id']=station
            service=target.get('service_target') or {}
            service['station_id']=station
            summary['target_plan']=deepcopy(target)
            if not service_ready(target,owner.policy.charge_until):
                wait_reason='충전 후 이동·다음 접근 예비량 계산 불가 또는 배터리 용량 초과'
                wait_status='waiting_for_target'
                summary.update(status='policy_insufficient' if service.get('status')=='infeasible' else 'unknown',reason=service.get('reason') or target.get('reason'))
                continue
            needed=max(owner.policy.charge_below,candidate['trigger_percent'],
                task_needed if service['purpose']=='task_budget' else 0)
            options.append((candidate,target,exit_target,exit_path,needed))
        # Prefer a known useful work target, then the original approach cost.
        # No connector, exit or task is changed by prospective calculations.
        options.sort(key=lambda option:(option[1]['service_target']['purpose']!='task_budget',option[0]['required_before_contact_j'],option[0]['station_id']))
        for candidate,target,exit_target,exit_path,needed in options:
            service=target['service_target'];station=candidate['station_id'];geometry=candidate['geometry']
            summary.update(status='charge_early' if observation['battery']<needed else 'sufficient',reason=None,
                selected_station_id=station,route_trigger_percent=candidate['trigger_percent'],trigger_percent=needed,target_plan=deepcopy(target))
            if observation['battery']>=needed:
                state.pop('charge_needed_percent',None)
                return
            same_place=last and math.hypot(observation['pose']['x']-last['pose']['x'],observation['pose']['y']-last['pose']['y'])<.2
            if same_place:
                previous=last.get('target_plan') or {}
                previous_percent=previous.get('target_percent')
                if not finite(previous_percent):previous_percent=owner.policy.charge_until
                if service['purpose']=='reserve_only':
                    prior_trigger=last.get('route_trigger_percent')
                    repeated=(last['battery']<prior_trigger and needed<=prior_trigger) if finite(prior_trigger) else needed>last['battery']
                    repeated=repeated and not last.get('reserve_ready_observed',False)
                else:
                    repeated=needed>last['battery'] and (target['task_id']==previous.get('task_id') or target['target_percent']<=previous_percent)
                if repeated:
                    wait_reason='충전 후에도 예비량 부족: 시간·소비 예측 또는 업무 조건 조정 필요'
                    wait_status='waiting_for_target';summary['status']='policy_insufficient'
                    continue
            # Work interruption is justified only by the selected service's
            # current threshold, not an impossible unrelated task forecast.
            if state['status']=='working' and state['task_id']:
                owner._failure(state['task_id'],now,'충전 큐·복귀 예비량 기준 도달: 작업 회수 후 조기 충전 계획')
            if state['status']!='idle':
                return
            try:
                receipt=self.manager.request(station,rid,now,{key:geometry[key] for key in ('staging','target')},target_percent=service['target_percent'])
            except ValueError as exc:
                wait_reason=str(exc)
                continue
            target['request_id']=service['request_id']=receipt['request_id']
            summary.update(status='charge_early',reason=None,target_plan=deepcopy(target))
            summary.pop('admission_status',None)
            self.plans[rid]=dict(station_id=station,geometry=geometry,path=candidate['path'],route_started=False,
                requested_at=now,request_id=receipt['request_id'],origin=deepcopy(observation['pose']),
                egress_target=deepcopy(exit_target),egress_route=deepcopy([geometry['staging'],*exit_path]),
                egress_floor_id=owner._floor(geometry['staging']['z']),target_plan=deepcopy(target),
                approach_budget={key:deepcopy(value) for key,value in candidate.items() if key not in ('path','geometry','parking')})
            if robot.model_id=='agv':self.plans[rid]['guided_approach']=owner._guided_plan(robot,observation,geometry['staging'],owner._floor(observation['pose']['z']))
            state.pop('charge_needed_percent',None)
            state.update(status='charging',path=[],reason='기본 예비량 충전 예약: 예정 작업은 별도 판단' if service['purpose']=='reserve_only' else '충전 큐·접근 예비량에 따른 시설 예약 요청')
            state['command_epoch']+=1
            owner.emit('charging_requested',rid,state['reason'],dict(receipt,energy_forecast=deepcopy(summary),
                egress_reservation=dict(target=deepcopy(exit_target),floor_id=self.plans[rid]['egress_floor_id'])))
            return
        if wait_reason:
            state['reason']=wait_reason
            summary['admission_status']=wait_status

    def _reserved_egress(self,plan):
        request=self.manager.requests.get(plan.get('request_id'))
        if (request and request.status=='cancelled' and request.phase=='cancelled'
                and not plan.get('clearing') and plan.get('parking') is None):
            return None
        return plan.get('parking') or plan.get('egress_target')

    def _release_cancelled_egress(self,plan):
        request=self.manager.requests.get(plan.get('request_id'))
        if (request and request.status=='cancelled' and request.phase=='cancelled'
                and not plan.get('clearing') and plan.get('parking') is None):
            plan.pop('egress_target',None)
            plan.pop('egress_floor_id',None)
            plan.pop('egress_route',None)

    @staticmethod
    def _path_near_point(path,point,clearance):
        for a,b in zip(path,path[1:]):
            dx,dy=b['x']-a['x'],b['y']-a['y']
            length2=dx*dx+dy*dy
            fraction=max(0.,min(1.,((point['x']-a['x'])*dx+(point['y']-a['y'])*dy)/length2)) if length2 else 0.
            if math.hypot(a['x']+fraction*dx-point['x'],a['y']+fraction*dy-point['y'])<clearance:
                return True
        return False

    def _parking_reservation_conflict(self,rid,start,route,target,floor):
        """Exclude other unfinished plans' destinations, without observing truth.

        A destination cannot occupy an earlier committed exit route, and a new
        route cannot cross an existing reserved destination. Crossing routes
        themselves are not mutually exclusive trajectories; live observation
        and motion control still govern their use.
        """
        points=[start,*route,target]
        for other_id,other_plan in self.plans.items():
            parking=self._reserved_egress(other_plan)
            if other_id==rid or parking is None:continue
            other_floor=other_plan.get('parking_floor_id',other_plan.get('egress_floor_id',self.owner._floor(parking['z'])))
            if other_floor!=floor:continue
            clearance=radius(self.owner.robots[rid])+radius(self.owner.robots[other_id])+self.owner.policy.safety_distance
            if self._path_near_point(points,parking,clearance):return True
            committed_route=other_plan.get('egress_route')
            if committed_route is None:
                staging=other_plan['geometry']['staging']
                planned=self.owner._route(self.owner.robots[other_id],{'pose':staging},parking,floor)
                if planned is None:return True
                committed_route=[staging,*planned]
            if self._path_near_point([*committed_route,parking],target,clearance):return True
        return False

    def _exit_route(self,robot,observation,target,floor,now,plan=None,*,live=True,planning=False):
        return exit_route(self,robot,observation,target,floor,now,plan,live=live,planning=planning)

    def _parking(self,rid,observation,plan,now,consider_occupancy=True,admission=False):
        robot=self.owner.robots[rid]
        floor=self.owner._floor(observation['pose']['z'])
        staging=plan['geometry']['staging']
        yaw=staging['yaw']; c,s=math.cos(yaw),math.sin(yaw)
        clearance=2*max(radius(r) for r in self.owner.robots.values())+self.owner.policy.safety_distance+.4
        candidates=[(0,dict(x=e.pose.x,y=e.pose.y,z=staging['z'],yaw=e.pose.yaw)) for e in self.project.environment.elements if e.kind=='waiting' and e.floor_id==floor and (not e.allowed_groups or robot.group in e.allowed_groups)]
        guided=robot.model_id=='agv'
        if guided:
            try:authored=DirectedRoute([p.model_dump() for p in robot.agv_route])
            except GuidedRouteError:return None
            candidates=[row for row in candidates if authored.waypoint(row[1]) is not None]
            candidates.extend((1,dict(p,z=staging['z'])) for p in authored.points)
        else:
            candidates.append((1,plan['origin']))
            for back in (.5,1.5,2.5):
                for side in (-1,1):
                    candidates.append((2,dict(x=staging['x']-c*back-s*side*clearance,y=staging['y']-s*back+c*side*clearance,z=staging['z'],yaw=yaw)))
        committed=self._reserved_egress(plan)
        if committed is not None:
            # Departure may wait for its committed space to become clear, but
            # must not silently steal another exit after admission.
            candidates=[(0,committed)]
        choices=[]
        for rank,target in candidates:
            if math.hypot(target['x']-staging['x'],target['y']-staging['y'])<clearance:continue
            if parking_blocks_service(self,rid,target,floor):continue
            route=self._exit_route(robot,observation,target,floor,now,plan,
                live=consider_occupancy and self.energy_now is not None,planning=admission)
            if route is None:continue
            if self._parking_reservation_conflict(rid,observation['pose'],route,target,floor):continue
            occupied=False
            for other_id,other in self.owner.last_observations.items() if consider_occupancy else []:
                if other_id==rid or now-other['sampled_at']>self.owner.policy.stale_after or abs(other['pose']['z']-staging['z'])>1.:continue
                # An admitted predecessor is expected to depart its current
                # connector position. Its immutable destination and exit route
                # were checked above; don't defeat FIFO by treating that
                # temporary position as a permanently parked robot.
                other_plan=self.plans.get(other_id,{})
                other_state=self.owner.robot_states[other_id]
                other_request=self.manager.requests.get(other_plan.get('request_id'))
                if (admission and self._reserved_egress(other_plan) is not None
                        and other_state['status']=='charging' and not other_state['operator_hold']
                        and not other_plan.get('interrupted') and other.get('fault')=='none'
                        and other.get('battery',0)>0 and other.get('upright',0)>=.45
                        and other_request and other_request.phase!='fault'):
                    continue
                if self._path_near_point([observation['pose'],*route,target],other['pose'],radius(robot)+radius(self.owner.robots[other_id])+self.owner.policy.safety_distance):
                    occupied=True;break
            if not occupied:
                points=[observation['pose'],*route]
                length=sum(math.hypot(b['x']-a['x'],b['y']-a['y']) for a,b in zip(points,points[1:]))
                choices.append((rank,length if guided else len(route),target))
        return min(choices,key=lambda row:(row[0],row[1]))[2] if choices else None

    def interrupt(self, rid, reason):
        if rid in self.plans:
            self.manager.interrupt(self.plans[rid]['station_id'], rid, reason)
            self._release_cancelled_egress(self.plans[rid])
            self.plans[rid]['interrupted']=True
            self.plans[rid]['interruption_reason']=reason
            self.plans[rid]['clear_since']=None
            state=self.owner.robot_states[rid]
            if state['status']=='charging' and not state['operator_hold']:
                state['reason']=reason
            self.power_requests.pop(rid, None)

    def recover(self, rid):
        if rid in self.plans:
            request=self.manager.requests[self.plans[rid]['request_id']]
            # A cancelled connector request may already have completed its
            # undock and be clearing. Explicit resume must retain that parking
            # ownership until observed clearance, not discard the live plan.
            if request.status=='cancelled' and request.phase=='cancelled' and self.plans[rid].get('parking') is None:
                self.plans.pop(rid)
                return
            self.manager.recover(self.plans[rid]['station_id'], rid)
            station=self.manager.stations[self.plans[rid]['station_id']]
            if (self.plans[rid].get('clearing') and station.active is request
                    and request.phase=='approach'):
                # The connector FSM is authoritative about physical release.
                # A retained/stale clearance flag cannot skip a still-active
                # approach after explicit recovery. Keep the accepted exit for
                # the later, actually completed undock; rejoin staging first.
                self.plans[rid]['clearing']=False
                self.plans[rid].pop('parking',None)
                self.plans[rid].pop('egress_remaining',None)
                self.intentions[rid]=dict(action='approach',phase='approach',
                    target=deepcopy(self.plans[rid]['geometry']['staging']),
                    reason='명시적 복구: 현재 충전 예약의 접근 단계부터 재확인')
            self.plans[rid]['interrupted']=False
            self.plans[rid].pop('interruption_reason',None)
            # Stop clears the live path; never resume by connecting directly to
            # a later parking node. Revalidate from the current observation.
            self.plans[rid]['route_started']=False
            self.plans[rid]['clear_since']=None
            self.plans[rid]['clearance_started_at']=self.energy_now if self.energy_now is not None else self.manager.time
            self.plans[rid]['recovery_attempts']=self.plans[rid].get('recovery_attempts',0)+1
            self.plans[rid].pop('clear_sampled_at',None)

    def _blocked_by_observation(self, rid, observation, target, now):
        owner = self.owner
        robot = owner.robots[rid]
        dx, dy = target['x']-observation['pose']['x'], target['y']-observation['pose']['y']
        for other_id, other in owner.last_observations.items():
            if other_id == rid or now-other['sampled_at'] > owner.policy.stale_after:
                continue
            if abs(other['pose']['z']-observation['pose']['z']) > 1.2:
                continue
            ox, oy = other['pose']['x']-observation['pose']['x'], other['pose']['y']-observation['pose']['y']
            if dx*ox+dy*oy > 0 and math.hypot(ox,oy) < radius(robot)+radius(owner.robots[other_id])+owner.policy.safety_distance:
                return other_id+' 통행 공간 대기'
        return None

    def command(self, rid, observation, now):
        stop = dict(v=0., w=0., mode='stand')
        if not isinstance(observation,dict):return stop
        stamp=observation.get('sampled_at')
        if not isinstance(stamp,(int,float)) or not math.isfinite(stamp) or stamp>now+1e-9 or now-stamp>self.owner.policy.stale_after:return stop
        if observation.get('fault')!='none' or observation.get('battery',0)<=0 or observation.get('upright',0)<.45:return stop
        state = self.owner.robot_states[rid]
        if rid not in self.plans or self.plans[rid].get('interrupted') or state['status'] != 'charging' or state['operator_hold']:
            return stop
        intention = self.intentions.get(rid, {})
        plan = self.plans[rid]
        previous=plan.get('command_sampled_at',-math.inf)
        if stamp<previous or (stamp==previous and observation['pose']!=plan.get('command_pose')):
            return stop
        plan['command_sampled_at']=stamp
        plan['command_pose']=deepcopy(observation['pose'])
        action = intention.get('action', 'hold')
        target = intention.get('target')
        state['reason'] = intention.get('reason', '충전 시설 예약 대기')
        clearing=plan.get('clearing',False)
        if clearing:
            action='approach'
            state['reason']='다음 로봇을 위해 충전 접근 통로 비우기'
        elif any(other_id!=rid and other.get('clearing') and other['station_id']==plan['station_id'] for other_id,other in self.plans.items()):
            state['reason']='앞 로봇의 충전 접근 통로 비움 대기'
            return stop
        if action == 'approach':
            approach_target=plan['parking'] if clearing else plan['geometry']['staging']
            robot=self.owner.robots[rid]
            floor=self.owner._floor(observation['pose']['z'])
            disks=()
            disks,traffic_reason=self.traffic.disks(robot,floor,plan['station_id'],now)
            if disks is None:
                state['reason']='충전 접근 대기: 다른 로봇의 새 위치 관측 필요'
                plan['traffic_reason']=traffic_reason
                return stop
            if plan['route_started'] and not self.owner.planner.path_clear(observation['pose'],[*state['path'],approach_target],floor,robot,peer_disks=disks):
                # Only the route is renewed. FIFO ownership, accepted
                # charge goal and the committed exit remain unchanged.
                plan['route_started']=False
            if not plan['route_started']:
                plan['replan_attempts']=plan.get('replan_attempts',0)+1
                plan['last_replan_at']=now
                # Replan when FIFO reservation is actually granted.
                if clearing:
                    if not initial_exit_anchor_valid(self,observation,plan):
                        self.interrupt(rid,'충전 종료 위치 허용 범위 밖: 승인 출구 시작 위치 확인 후 명시적 복구 필요')
                        return stop
                    route = self._exit_route(robot, observation, approach_target, floor, now, plan)
                else:
                    route,traffic_reason=self.traffic.route(robot,observation,approach_target,floor,plan['station_id'],now)
                if route is None:
                    remaining=plan.get('egress_remaining',plan.get('egress_route',[])[1:])
                    if clearing and not self.owner.planner.path_clear(observation['pose'],[*remaining,approach_target],floor,robot):
                        self.interrupt(rid,'충전 출구의 현재 위치에서 승인 경로로 연결 불가: 정적 장애물·방향·경계 확인 필요')
                    elif not clearing and traffic_reason=='approach_route_unavailable':
                        self.interrupt(rid, '충전 대기 위치까지 경로 없음')
                    else:
                        state['reason']='충전 접근 대기: 다른 로봇의 통행 공간 확보 필요'
                        plan['traffic_reason']='clearance_traffic_blocked' if clearing else traffic_reason
                    return stop
                state['path'] = route
                if clearing:plan['egress_remaining']=route
                plan['route_started'] = True
                plan.pop('traffic_reason',None)
                if self.owner.robots[rid].model_id=='agv':plan['guided_active_route']=self.owner._guided_plan(self.owner.robots[rid],observation,approach_target,self.owner._floor(observation['pose']['z']))
            if self.owner.robots[rid].model_id=='agv':
                try:DirectedRoute([p.model_dump() for p in self.owner.robots[rid].agv_route]).locate(observation['pose'])
                except GuidedRouteError:
                    self.interrupt(rid,'AGV 지정 경로 관측 이탈: 명시적 복구 필요')
                    return stop
            path = state['path']
            retained_corner = None
            while path and math.hypot(path[0]['x']-observation['pose']['x'], path[0]['y']-observation['pose']['y']) < .08:
                # Arrival tolerance cannot authorize a new chord through an
                # observed peer. Keep this corner until the actual observation
                # makes the remaining route, including exact staging, clear.
                if not self.owner.planner.path_clear(observation['pose'],[*path[1:],approach_target],floor,robot,peer_disks=disks):
                    retained_corner = path[0]
                    break
                path.pop(0)
            if (self.owner.robots[rid].model_id=='agv' and (path or
                    math.hypot(approach_target['x']-observation['pose']['x'],approach_target['y']-observation['pose']['y'])>=.08)):
                forward=self.owner._guided_remaining(self.owner.robots[rid],observation,path,approach_target,self.owner._floor(observation['pose']['z']))
                if forward is None:
                    self.interrupt(rid,'AGV 충전 이동의 순방향 경로 재계획 불가')
                    return stop
                if forward is not path:
                    if clearing and plan.get('egress_route') and (len(forward)>len(path) or any(
                            math.hypot(a['x']-b['x'],a['y']-b['y'])>1e-7
                            for a,b in zip(forward,path[len(path)-len(forward):]))):
                        self.interrupt(rid,'AGV 충전 출구의 승인 경로를 넘는 재계획: 명시적 복구 필요')
                        return stop
                    state['path']=path=forward
                    if clearing:plan['egress_remaining']=path
                    plan['guided_active_route']=self.owner._guided_plan(self.owner.robots[rid],observation,approach_target,self.owner._floor(observation['pose']['z']))
            # The guided forward-only repair may replace a previously clear
            # path. Check the actual command route after every transformation.
            if not self.owner.planner.path_clear(observation['pose'],[*path,approach_target],floor,robot):
                self.interrupt(rid,'충전 이동 경로 연결 불가: 정적 장애물·방향·경계 확인 필요')
                return stop
            if not path_clear_of_disks(observation['pose'],[*path,approach_target],disks):
                state['reason']='충전 접근 대기: 다른 로봇의 통행 공간 확보 필요'
                plan['traffic_reason']='guided_approach_occupied' if robot.model_id=='agv' else 'approach_traffic_blocked'
                return stop
            target = path[0] if path else approach_target
            blocked = self._blocked_by_observation(rid, observation, target, now)
            if blocked:
                state['reason'] = blocked
                return stop
            dx,dy = target['x']-observation['pose']['x'],target['y']-observation['pose']['y']
            distance = math.hypot(dx,dy)
            position_tolerance=.08 if not path else .05
            if retained_corner is not None and path and path[0] == retained_corner:
                # The usual .05 m tolerance would strand a retained corner.
                # Keep the existing distance*.8 speed with no artificial floor.
                position_tolerance=0.
            turn = angle(math.atan2(dy,dx)-observation['pose']['yaw']) if distance > position_tolerance else angle(approach_target['yaw']-observation['pose']['yaw'])
            speed = min(.3, self.owner.robots[rid].max_speed, self.owner.policy.speed_limit, distance*.8)
            scan = observation.get('sensors',{}).get('lidar')
            if isinstance(scan,dict) and abs(turn)<.65:
                front=[d for a,d in zip(scan['angles'],scan['ranges']) if abs(a)<.3]
                if front and min(front) < radius(self.owner.robots[rid])+self.owner.policy.safety_distance:
                    state['reason'] = '충전 접근 경로의 거리 센서 장애물로 제동'
                    return stop
            # Guided vehicles turn in place before taking the next authored
            # edge; AMR-style simultaneous corner cutting leaves that corridor.
            turn_limit=.12 if self.owner.robots[rid].model_id=='agv' else .65
            return dict(v=speed*max(0.,math.cos(turn)) if distance>position_tolerance and abs(turn)<turn_limit else 0., w=max(-.5,min(.5,turn*1.8)), mode='drive')
        seating = action=='hold' and intention.get('phase')=='charging' and self.power_requests.get(rid,{}).get('power_w',0)>0
        if action not in ('dock','undock') and not seating:
            return stop
        target = target or plan['geometry']['target']
        blocked = self._blocked_by_observation(rid, observation, target, now)
        if blocked:
            state['reason'] = blocked
            return stop
        pose = observation['pose']
        dx,dy = target['x']-pose['x'], target['y']-pose['y']
        forward = dx*math.cos(target['yaw'])+dy*math.sin(target['yaw'])
        lateral = -dx*math.sin(target['yaw'])+dy*math.cos(target['yaw'])
        sign = -1 if action=='undock' else 1
        error = angle(target['yaw']+sign*max(-.15,min(.15,lateral*1.8))-pose['yaw'])
        velocity = max(-.12,min(.12,forward*.6))
        if action=='dock':
            velocity=max(0.,min(.06,velocity))
            # The final pose is an intention; only actual contact enables power.
            if abs(forward)<.035 and abs(lateral)<.025:velocity=.018
        if seating:velocity=.012
        if abs(error)>.18:velocity=0.
        return dict(v=velocity,w=max(-.25,min(.25,error*1.4)),mode='drive')
