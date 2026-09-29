"""Observed cooperative execution; owns participants until placement or recovery.

Optional initial donor loading precedes carrier transport and receiver placement.
Participants share one reservation and retain it whenever recovery is required.
No physics object or ground-truth state is available to this coordinator.
"""
from copy import deepcopy
import math
from uuid import uuid4

from .catalog import model_by_id
from .navigation import radius
from .transport_workflow import TransportWorkflow
from .handoff_receiver import HandoffReceiver
from .loading_workflow import LoadingWorkflow
from .cooperative_resources import CooperativeResources


class CooperativeControl:
    def __init__(self, orchestrator, support_geometry, *, rng, arm_geometry=None):
        self.o = orchestrator
        self.geometry = deepcopy(support_geometry)
        # Immutable-by-copy model metadata, never a simulator state handle.
        # Runtime supplies each compiled arm's own chain and joint bounds.
        self.arm_geometry = deepcopy(arm_geometry or {})
        self.require_arm_geometry = arm_geometry is not None
        self.rng = rng
        self.resources = CooperativeResources()
        self.executions = {}
        self.reports = {}
        from .cooperative_recovery import CooperativeRecovery
        self.recovery = CooperativeRecovery(self)

    def _arm_contract(self, robot_id):
        contract = self.arm_geometry.get(robot_id)
        if self.require_arm_geometry and (not isinstance(contract, dict) or contract.get('robot_id') != robot_id):
            raise ValueError('참여 팔의 모델 기하 계약이 없거나 로봇 식별자가 다릅니다: '+robot_id)
        if contract is not None:
            from .arm_kinematics import validate_contract
            return validate_contract(contract)
        return deepcopy(contract)

    def command_active(self, task_id, recovery_id=None):
        e=self.executions.get(task_id)
        if not e or e['released']:return False
        if recovery_id is not None:
            return self.recovery.active(e) and e['recovery']['recovery_id']==recovery_id
        return not e['terminal'] and self.o.tasks[task_id]['status']=='running'

    def locked(self, robot_id):
        return any(robot_id in e['participants'].values() and not e.get('released')
                   for e in self.executions.values())

    def _valid_participant(self, rid, observation, now):
        if not isinstance(observation, dict) or observation.get('robot_id') != rid:
            return False
        def number(value):
            return type(value) in (int,float) and math.isfinite(value)
        if not all(number(observation.get(key)) for key in ('sampled_at','battery','upright')):
            return False
        if (not 0<=now-observation['sampled_at']<=self.o.policy.stale_after
                or observation['battery']<=0 or observation['upright']<.98 or observation.get('fault')!='none'):
            return False
        pose = observation.get('pose')
        if not isinstance(pose,dict) or not all(number(pose.get(key)) for key in ('x','y','z','yaw')):
            return False
        for key in ('velocity','angular_velocity'):
            vector=observation.get(key)
            if not isinstance(vector,(list,tuple)) or len(vector)!=3 or not all(number(v) for v in vector):
                return False
        sensors=observation.get('sensors')
        if not isinstance(sensors,dict) or sensors.get('controller_error') or not isinstance(sensors.get('contacts'),list):
            return False
        return all(isinstance(row,dict) and isinstance(row.get('a'),str) and isinstance(row.get('b'),str)
            and number(row.get('force')) and row['force']>=0 for row in sensors['contacts'])

    def _eligible(self, task, observations, now):
        c = task.cooperation
        if not c.donor_id and task.kind not in ('handoff', 'transport', 'unload'):
            return '초기 상차 로봇을 지정해야 하는 협업 작업입니다'
        if c.carrier_id not in self.geometry:
            return '운반 로봇의 물리 지지면 계약 없음'
        carrier, receiver = self.o.robots[c.carrier_id], self.o.robots[c.receiver_id]
        if not carrier.sensors.lidar:
            return '협업 접근에는 전방 거리 관측 센서가 필요합니다'
        if receiver.model_id not in ('arm', 'mobile_manipulator'):
            return '인수 로봇의 조작 제어기 없음'
        if c.donor_id and self.o.robots[c.donor_id].model_id not in ('arm', 'mobile_manipulator'):
            return '상차 로봇의 조작 제어기 없음'
        try:
            self._arm_contract(c.receiver_id)
            if c.donor_id:
                self._arm_contract(c.donor_id)
        except ValueError as error:
            return str(error)
        item = next(i for i in self.o.project.items if i.id == task.item_id)
        if item.mass > min(self.geometry[c.carrier_id]['max_payload'], model_by_id(receiver.model_id)['max_payload']):
            return '협업 참여 로봇의 허용 적재량 초과'
        if c.donor_id and item.mass > model_by_id(self.o.robots[c.donor_id].model_id)['max_payload']:
            return '상차 로봇의 허용 적재량 초과'
        for rid in (c.carrier_id, c.receiver_id, *([c.donor_id] if c.donor_id else [])):
            obs = observations.get(rid)
            if self.o.robot_states[rid]['status'] != 'idle' or self.locked(rid):
                return '협업 참여 로봇 또는 복구 예약 대기'
            if not self._valid_participant(rid, obs, now):
                return '협업 참여 로봇의 신선한 관측 대기'
            if obs['fault'] != 'none' or obs['battery'] < self.o.policy.charge_below or obs['upright'] < .98:
                return '협업 참여 로봇의 장애·배터리·자세 조건 불충족'
            expected_floor = task.floor_id if rid == c.receiver_id else (c.source_floor_id or task.floor_id)
            if self.o._floor(obs['pose']['z']) != expected_floor:
                return '협업 참여 로봇의 현재 관측 층 불일치'
            if not self.o.robots[rid].sensors.item_tracking:
                return '협업 물품 위치 관측 센서 없음'
        if self.o.reservations.owners.get('item:'+item.id):
            return '물품의 다른 작업 또는 복구 예약 대기'
        obs = observations[c.carrier_id]
        trip = self._trip(task, obs, item)
        cross_floor = self.o._floor(obs['pose']['z']) != task.floor_id
        if cross_floor and trip is None:
            return '적재 질량·외곽·출발 및 도착 경로를 만족하는 승강기 없음'
        if c.carrier_loading_pose and self._handoff_route(carrier, obs, c.carrier_loading_pose.model_dump(), c.source_floor_id or task.floor_id) is None:
            return '상차 접근 경로 없음'
        route = trip['route'] if trip else self._handoff_route(carrier, obs, c.carrier_destination.model_dump(), task.floor_id)
        if route is None:
            return '적재 운반 경로 없음'
        # The peer approach uses a reserved workspace, but does not waive the
        # route planner, third-party collision avoidance, or front range sensor.
        energy = self.o.charging.task_budget(carrier, task, obs, route, trip)
        if energy.get('energy_observation_valid') is False:
            return '협업 운반 에너지 예측에 사용할 현재 관측 필요'
        if energy.get('return_route_required') and not energy.get('return_route_available'):
            return '협업 운반 후 충전 경로·대기 에너지 예측 불가'
        if energy.get('energy_estimate_valid') is False or energy.get('required_percent') is None:
            return '협업 운반 이동 시간·에너지 예측 불가'
        if obs['battery'] < energy['required_percent']:
            return '협업 운반·복귀 에너지 부족'
        return None

    def _trip(self, task, observation, item):
        if self.o._floor(observation['pose']['z']) == task.floor_id:return None
        movement = task.model_copy(update={'destination': task.cooperation.carrier_destination})
        return self.o._trip_plan(self.o.robots[task.cooperation.carrier_id], observation, movement, cargo=item)

    def assign(self, record, now, observations):
        task, c = record['spec'], record['spec'].cooperation
        reason = self._eligible(task, observations, now)
        if reason:
            record.update(status='waiting', reason=reason)
            return
        item = next(i for i in self.o.project.items if i.id == task.item_id)
        participants = dict(carrier=c.carrier_id, receiver=c.receiver_id)
        if c.donor_id:
            participants['donor'] = c.donor_id
        execution_id = uuid4().hex
        height = next(f.elevation for f in self.o.project.environment.floors if f.id == task.floor_id)
        destination = c.carrier_destination.model_dump()
        destination['z'] += height
        placement = task.destination.model_dump()
        placement['z'] += height
        geom = self.geometry[c.carrier_id]
        flow = TransportWorkflow(task.id, c.carrier_id, item.id, destination, item.mass, item.size,
            receiver_id=c.receiver_id, timeout=task.timeout, **geom)
        receiver = HandoffReceiver(task.id, c.carrier_id, c.receiver_id, item.id,
            item.mass, item.size.model_dump(), placement, timeout=task.timeout,
            arm_geometry=self._arm_contract(c.receiver_id))
        loading = None
        if c.donor_id:
            source = (task.source or item.pose).model_dump()
            source['z'] += next(f.elevation for f in self.o.project.environment.floors if f.id == (c.source_floor_id or task.floor_id))
            try:
                loading = LoadingWorkflow(task.id, c.donor_id, c.carrier_id, item.id, source,
                    item.mass, item.size.model_dump(), loading_offset=c.loading_offset,
                    timeout=task.timeout, arm_geometry=self._arm_contract(c.donor_id),
                    **{key: geom[key] for key in ('support_geom','support_size','support_top_offset')})
            except ValueError as error:
                record.update(status='waiting', reason='상차 지지면 조건 불충족: '+str(error))
                return
        try:
            self.resources.acquire(execution_id, task.id, participants, item.id, c.workspace_id)
        except ValueError as error:
            record.update(status='waiting', reason=str(error))
            return
        trip = self._trip(task, observations[c.carrier_id], item)
        if trip:
            trip['route'] = self._route(self.o.robots[c.carrier_id], observations[c.carrier_id], trip['staging'], trip['source_floor'])
        self.executions[task.id] = dict(id=execution_id, participants=participants, flow=flow,
            receiver=receiver, result=None, arm_result=None, action=None, generation=0,
            committed=False, custody_seen=False, released=False, terminal=False,
            loading=loading, loading_result=None, loading_committed=loading is None, donor_custody_seen=False,
            trip_plan=trip,
            loading_approach_done=c.carrier_loading_pose is None,
            loading_route=(self._handoff_route(self.o.robots[c.carrier_id], observations[c.carrier_id],
                c.carrier_loading_pose.model_dump(), c.source_floor_id or task.floor_id) if c.carrier_loading_pose else None),
            route=deepcopy(trip['route']) if trip else self._handoff_route(self.o.robots[c.carrier_id], observations[c.carrier_id], destination, task.floor_id))
        self.reports.pop(task.id, None)
        # The legacy item reservation is a bridge to single-robot schedulers.
        # Every participant retains it on failure; the atomic ledger is primary.
        self.o.reservations.owners['item:'+item.id] = list(participants.values())
        record.update(status='running', robot_id=c.carrier_id, participant_ids=list(participants.values()),
            execution_id=execution_id, started_at=now, progress_at=now, reason='협업 자원 원자 예약 완료')
        for rid in participants.values():
            self.o.robot_states[rid].update(status='cooperating', task_id=task.id, path=[], mode='stand', reason=record['reason'])
            self.o.robot_states[rid]['command_epoch'] += 1
            self.o.count[rid] += 1
        self.o.emit('cooperation_started', c.carrier_id, record['reason'], dict(task_id=task.id, execution_id=execution_id, participants=participants))

    def terminate(self, task_id, now, reason, *, cancelled=False):
        e = self.executions.get(task_id)
        if not e or e['terminal'] or e['released']:
            return
        e['terminal'] = True
        e['generation'] += 1
        e['action'] = 'hold'
        e['flow'].cancel(now, reason)
        if e.get('loading'):
            e['loading'].cancel(now)
        method = self.resources.cancel if cancelled else self.resources.fail
        method(e['id'], reason, now=now)
        record = self.o.tasks[task_id]
        record.update(status='cancelled' if cancelled else 'failed', completed_at=now, reason=reason)
        if not cancelled:
            record['attempts'] += 1
        for rid in e['participants'].values():
            state = self.o.robot_states[rid]
            trip = state.get('trip')
            if trip:
                if self.o.facilities.cancel(trip['elevator_id'], rid):state.pop('trip', None)
                else:
                    lift = self.o.facilities.elevators[trip['elevator_id']]
                    lift.fault, lift.fault_latched = 'cargo_execution_requires_recovery', True
            state['command_epoch'] += 1
            state.update(status='recovery_required', task_id=None, path=[], reason=reason, mode='stand')
        self.o.emit('cooperation_cancelled' if cancelled else 'cooperation_failed', task_id, reason,
                    dict(execution_id=e['id'], resources_retained=True))

    def _record_report(self, task_id, execution_id, now, report, observation):
        """Cache central FSM evidence from an already delivered sensor sample.

        The receiver FSM runs here, not on a second simulated network host.
        ObservationBus already applied observation delay, network delay and
        loss. Sending this derived result through that network again would
        double-charge the inbound hop. Actuator commands still use the normal
        outbound network path. Never replace the original evidence timestamp.
        """
        e = self.executions.get(task_id)
        if not e or e['id'] != execution_id or e['terminal'] or e['released']:
            return False
        if not isinstance(report, dict) or not isinstance(observation, dict):
            return False
        task = self.o.tasks[task_id]['spec']
        if (report.get('task_id') != task_id or report.get('item_id') != task.item_id
                or report.get('carrier_id') != e['participants']['carrier']
                or report.get('receiver_id') != e['participants']['receiver']
                or observation.get('robot_id') != e['participants']['receiver']
                or report.get('state') not in ('ready', 'received', 'placed')):
            return False
        stamp, observed = report.get('sampled_at'), observation.get('sampled_at')
        if (not all(type(value) in (int, float) and math.isfinite(value) for value in (now, stamp, observed))
                or not 0 <= now-stamp <= min(TransportWorkflow.FRESH_AGE, self.o.policy.stale_after)
                or not stamp <= observed <= now):
            return False
        old = self.reports.get(task_id)
        if old and old.get('execution_id') == execution_id and stamp <= old['sampled_at']:
            return False
        self.reports[task_id] = dict(deepcopy(report), execution_id=execution_id,
            source='delivered_receiver_observation', derived_at=now)
        return True

    def _route(self, robot, observation, destination, floor_id):
        route=self.o._route(robot,observation,destination,floor_id)
        if robot.model_id=='agv':return route  # Preserve its authored route.
        start=observation['pose']
        if self.o.planner.path_clear(start,[destination],floor_id,robot):
            return [deepcopy(destination)]
        if route is None:return None
        # Remove grid-centre overshoot near a handoff. Every shortcut retains
        # continuous static and reviewed-topology clearance, ending at the
        # authored rendezvous rather than a cell beyond the receiving base.
        short=[];anchor=start;index=0
        while index<len(route):
            far=index
            for candidate in range(index+1,len(route)):
                if self.o.planner.path_clear(anchor,[route[candidate]],floor_id,robot):far=candidate
            anchor=route[far];short.append(anchor);index=far+1
        return short

    def _hold_arms(self, task_id, execution):
        return {rid: dict(hold=True, task_id=task_id, generation=execution['generation'])
                for role,rid in execution['participants'].items() if role in ('donor','receiver')}

    def _handoff_route(self, robot, observation, destination, floor_id):
        from .orchestration import angle
        pose=observation['pose'];c,s=math.cos(destination['yaw']),math.sin(destination['yaw'])
        dx,dy=destination['x']-pose['x'],destination['y']-pose['y']
        if (abs(angle(pose['yaw']-destination['yaw']))<.1 and dx*c+dy*s>=-.03
                and abs(-dx*s+dy*c)<.07 and self.o.planner.path_clear(pose,[destination],floor_id,robot)):
            return [deepcopy(destination)]
        # Align outside the close handoff workspace, then drive straight in.
        # A reachable XY alone cannot authorize turning alongside an arm base.
        distance=max(.8,radius(robot)+.25)
        approach=dict(destination,x=destination['x']-c*distance,y=destination['y']-s*distance)
        if not self.o.planner.path_clear(approach,[destination],floor_id,robot):return None
        route=self._route(robot,observation,approach,floor_id)
        if route is None:return None
        route[-1]=dict(approach,align=True)
        return [*route,deepcopy(destination)]

    def _loading(self, task_id, now, observations):
        e, record = self.executions[task_id], self.o.tasks[task_id]
        task, c = record['spec'], record['spec'].cooperation
        result = e['loading'].update(now, observations.get(c.donor_id, {}), observations.get(c.carrier_id, {}))
        e['loading_result'] = result
        proof = dict(result, execution_id=e['id'])
        intent = result.get('resource_intent') or {}
        try:
            if not e['donor_custody_seen'] and intent.get('donor_custody'):
                self.resources.observe_donor_custody(e['id'], task.item_id, c.donor_id, proof, now=now)
                e['donor_custody_seen'] = True
                self.o.emit('cooperation_donor_grasped', c.donor_id, '양측 파지와 들어 올림을 관측하여 최초 소유 확인', dict(task_id=task_id))
            if result['status'] == 'completed' and not e['loading_committed']:
                version = self.resources.snapshot()['items'][task.item_id]['version']
                self.resources.commit_loading_transfer(e['id'], task.item_id, c.donor_id, c.carrier_id, now, proof, expected_version=version)
                e['loading_committed'] = e['custody_seen'] = True
                self.o.emit('cooperation_loaded', c.carrier_id, '물품 지지·해제·상차 팔 후퇴 확인 후 운반차 소유 이전', dict(task_id=task_id, proof=proof))
        except ValueError as error:
            self.terminate(task_id, now, '상차 소유 확인 실패: '+str(error))
        if result['status'] == 'failed':
            self.terminate(task_id, now, result['reason']+': '+result['code'])
        action = 'hold' if e['terminal'] or e['loading_committed'] else 'loading:'+result['phase']
        if action != e['action']:
            e['generation'] += 1
            e['action'] = action
        commands = self._hold_arms(task_id, e)
        commands[c.donor_id] = dict(result, hold=result['hold'] or e['terminal'] or e['loading_committed'], task_id=task_id, generation=e['generation'])
        record['cooperation'] = dict(execution_id=e['id'], phase='loading', loading_phase=result['phase'],
            loading_committed=e['loading_committed'], receiver_phase='await_prepare', committed=False, resources_retained=True)
        record['evidence'] = dict(loading=deepcopy(result['evidence']))
        if not e['terminal']:
            record['reason'] = result['reason']
        for rid in e['participants'].values():
            self.o.robot_states[rid]['reason'] = record['reason']
        return commands

    def update(self, now, observations):
        arms = {}
        for task_id, e in self.executions.items():
            record = self.o.tasks[task_id]
            task, c = record['spec'], record['spec'].cooperation
            if e['released']:
                continue
            if self.recovery.active(e):
                arms.update(self.recovery.update(task_id,now,observations))
                continue
            if e['terminal']:
                arms.update(self._hold_arms(task_id, e))
                continue
            if now-record['started_at'] > task.timeout or (task.deadline is not None and now > task.deadline):
                self.terminate(task_id, now, '협업 작업 기한 또는 제한 시간 초과')
                arms.update(self._hold_arms(task_id, e))
                continue
            participants = set(e['participants'].values())
            invalid = any(not self._valid_participant(rid, observations.get(rid), now) for rid in participants)
            if invalid:
                self.terminate(task_id, now, '협업 참여 로봇의 관측 단절·장애·전원·자세 이상')
                arms.update(self._hold_arms(task_id, e))
                continue
            carrier = observations.get(c.carrier_id, {})
            peer = deepcopy(observations.get(c.receiver_id, {}))
            if any(row.get('a')!=row.get('b') and {row.get('a'),row.get('b')}<=participants and row.get('force',0)>5.
                   for rid in participants for row in observations[rid].get('sensors',{}).get('contacts',[]) if isinstance(row,dict)):
                self.terminate(task_id,now,'인계 참여 로봇 사이의 의도하지 않은 충돌 접촉')
                arms.update(self._hold_arms(task_id, e))
                continue
            if not e.get('loading_approach_done', True):
                from .orchestration import angle
                target = c.carrier_loading_pose
                pose = carrier['pose']
                arrived = (math.hypot(pose['x']-target.x, pose['y']-target.y) < .07
                    and abs(angle(pose['yaw']-target.yaw)) < .08
                    and math.hypot(*carrier['velocity'][:2]) < .04)
                if arrived:
                    e['loading_approach_done'] = True
                    e['result'] = None
                    self.o.emit('cooperation_loading_arrived', c.carrier_id,
                        '예약된 상차 위치 도착·정렬·정지 관측 확인', dict(task_id=task_id, pose=deepcopy(pose)))
                else:
                    record['reason'] = '상차 팔 정지·작업 공간 예약 후 운반차 접근'
                    record['cooperation'] = dict(execution_id=e['id'], phase='loading_approach', resources_retained=True)
                    self.o.robot_states[c.carrier_id]['reason'] = record['reason']
                    arms.update(self._hold_arms(task_id, e))
                    continue
            if not e.get('loading_committed', True):
                arms.update(self._loading(task_id, now, observations))
                continue
            if c.donor_id:
                arms[c.donor_id] = dict(hold=True, task_id=task_id, generation=e['generation'])
            report = self.reports.get(task_id)
            if (report and report.get('execution_id') == e['id']
                    and 0 <= now-report['sampled_at']<=TransportWorkflow.FRESH_AGE
                    and report['sampled_at'] <= peer.get('sampled_at', -1)):
                peer.setdefault('sensors', {})['handoff'] = deepcopy(report)
            result = e['result'] if e['committed'] else e['flow'].update(now, carrier, peer)
            e['result'] = result
            proof = dict(result, execution_id=e['id'])
            try:
                if not e['custody_seen'] and result['phase'] != 'await_load' and result['supported']:
                    self.resources.observe_custody(e['id'], task.item_id, c.carrier_id, proof, now=now)
                    e['custody_seen'] = True
                if result['status'] == 'completed' and not e['committed']:
                    version=self.resources.snapshot()['items'][task.item_id]['version']
                    self.resources.commit_transfer(e['id'], task.item_id, c.carrier_id, c.receiver_id, now, proof, expected_version=version)
                    e['committed'] = True
                    self.o.emit('cooperation_transferred', c.receiver_id, '양측 관측과 물리적 분리 확인 후 물품 소유 이전', dict(task_id=task_id, proof=proof))
            except ValueError as error:
                self.terminate(task_id, now, '협업 소유 확인 실패: '+str(error))
            if result['status'] == 'failed':
                self.terminate(task_id, now, result['reason'])
            action = 'hold' if e['terminal'] else 'place' if e['committed'] else result.get('receiver_action') or 'hold'
            if action != e['action']:
                e['generation'] += 1
                e['action'] = action
            # A reserved receiver on another floor cannot see cargo in transit.
            # Its grasp workflow starts only on the observed-arrival prepare
            # request. Participant health and the overall task deadline remain
            # checked above; no observation or success is synthesized here.
            arm = (e['receiver']._result() if action == 'hold' and e['receiver'].phase == 'await_prepare'
                   else e['receiver'].update(now, observations.get(c.receiver_id, {}), action))
            e['arm_result'] = arm
            if arm['status'] == 'failed':
                self.terminate(task_id, now, arm['reason'])
            arms[c.receiver_id] = dict(arm, hold=arm.get('hold', False) or e['terminal'], task_id=task_id, generation=e['generation'])
            report = arm.get('report')
            if report:
                self._record_report(task_id, e['id'], now, report, observations.get(c.receiver_id))
            record['cooperation'] = dict(execution_id=e['id'], phase=result['phase'], receiver_phase=arm['phase'], committed=e['committed'], resources_retained=not e['released'],
                loading_phase=e['loading_result']['phase'] if e.get('loading_result') else None, loading_committed=e.get('loading_committed', True))
            record.setdefault('evidence', {}).update(transport=deepcopy(result.get('evidence')), receiver=deepcopy(arm.get('evidence')))
            if not e['terminal']:record['reason'] = arm['reason'] if e['committed'] else result['reason']
            for rid in e['participants'].values():
                self.o.robot_states[rid]['reason'] = record['reason']
            if e['committed'] and arm['status'] == 'completed' and not e['terminal']:
                self._complete(task_id, now, observations)
        return arms

    def _placement_proof(self, task_id, now, observations, *, actor_id=None, destination=None, report=None):
        """Recheck live observations; a cached success report is not a release."""
        e, record = self.executions[task_id], self.o.tasks[task_id]
        task, item_id = record['spec'], record['spec'].item_id
        actor_id=actor_id or e['participants']['receiver']
        if report is None:
            report = self.reports.get(task_id)
            if not isinstance(report, dict) or report.get('execution_id') != e['id']:
                return None
        if (not isinstance(report, dict) or report.get('state') != 'placed'
                or report.get('task_id') != task_id or report.get('item_id') != item_id
                or report.get('receiver_id') != actor_id
                or report.get('carrier_id') != e['participants']['carrier']):
            return None
        def fresh(stamp):
            return type(stamp) in (float, int) and math.isfinite(stamp) and 0 <= now-stamp <= min(1., self.o.policy.stale_after)
        if not fresh(report.get('sampled_at')):
            return None
        participants = {}
        for rid in e['participants'].values():
            obs = observations.get(rid, {})
            if not self._valid_participant(rid, obs, now):
                return None
            sensors = obs.get('sensors', {})
            contacts = sensors.get('contacts')
            if any(type(obs.get(k)) not in (float,int) or not math.isfinite(obs[k]) for k in ('battery','upright')):return None
            if (obs.get('robot_id') != rid or not fresh(obs.get('sampled_at'))
                    or obs.get('fault') != 'none' or sensors.get('controller_error') or obs.get('battery', 0) <= 0
                    or obs.get('upright', 0) < .98 or not isinstance(contacts, list)):
                return None
            for key,limit in (('velocity',.04),('angular_velocity',.08)):
                vector=obs.get(key)
                if (not isinstance(vector,(list,tuple)) or len(vector)!=3
                        or not all(type(v) in (int,float) and math.isfinite(v) for v in vector)
                        or math.sqrt(sum(v*v for v in vector))>limit):return None
            if any(not isinstance(c,dict) or not isinstance(c.get('a'),str) or not isinstance(c.get('b'),str)
                   or not isinstance(c.get('force'),(int,float)) or not math.isfinite(c['force']) or c['force']<0 for c in contacts):return None
            feedback = sensors.get('manipulation', {}).get(item_id, {})
            if rid in (e['participants']['receiver'], e['participants'].get('donor')):
                if feedback.get('finger_contacts') != [] or feedback.get('bilateral_contact') is not False:
                    return None
            touching = any(item_id in (c.get('a'), c.get('b')) and rid in (c.get('a'), c.get('b')) and c.get('force', 0) > .1 for c in contacts)
            if touching:
                return None
            participants[rid] = dict(robot_id=rid, item_id=item_id, sampled_at=obs['sampled_at'], holding=False)
        peer = observations[actor_id]
        matches = [i for i in peer['sensors'].get('items', []) if i.get('id') == item_id and i.get('visible', True)]
        if len(matches) != 1:
            return None
        tracked = matches[0]
        item = next(i for i in self.o.project.items if i.id == item_id)
        height = next(f.elevation for f in self.o.project.environment.floors if f.id == task.floor_id)
        destination = ([task.destination.x, task.destination.y, task.destination.z+height] if destination is None
            else [destination[key] for key in ('x','y','z')])
        try:
            pos, velocity = tracked['position'], tracked['velocity']
            if (len(pos)!=3 or len(velocity)!=3 or not all(math.isfinite(v) for v in [*pos,*velocity])
                    or math.hypot(pos[0]-destination[0],pos[1]-destination[1]) > .04
                    or abs(pos[2]-destination[2]-item.size.z/2) > .025
                    or math.sqrt(sum(v*v for v in velocity)) > .035):
                return None
            contacts = tracked.get('support_contacts')
            if not isinstance(contacts, list):
                return None
            upward = 0.
            for contact in contacts:
                a, b = contact['geom_a'], contact['geom_b']
                if item_id+'/shape' not in (a,b):continue
                other = a if b == item_id+'/shape' else b
                if any(other.startswith(rid+'/') for rid in e['participants'].values()):continue
                point, force = contact['position'], contact['force_on_b_world']
                if not all(math.isfinite(v) for v in [*point,*force]):return None
                if math.hypot(point[0]-destination[0],point[1]-destination[1]) <= math.hypot(item.size.x,item.size.y)/2+.025 and abs(point[2]-destination[2]) <= .025:
                    upward += max(0., force[2] if b == item_id+'/shape' else -force[2])
            if upward < .6*item.mass*9.81:return None
        except (KeyError, TypeError, ValueError, IndexError):
            return None
        return dict(execution_id=e['id'], task_id=task_id, item_id=item_id, source='observations', final_placed=True,
            placement=dict(sampled_at=report['sampled_at'], item_id=item_id, support_confirmed=True, stable=True, holders=[],
                observed_at=peer['sampled_at'], upward_support_force_N=upward, item_position=list(pos)), participants=participants)

    def _complete(self, task_id, now, observations):
        e, record = self.executions[task_id], self.o.tasks[task_id]
        proof = self._placement_proof(task_id, now, observations)
        if proof is None:return
        try:
            self.resources.release(e['id'], now, proof)
        except ValueError:
            return  # Keep all leases until fresh peer confirmations agree.
        e['released'] = True
        e['generation'] += 1
        record.update(status='completed', completed_at=now, reason='물리적 인계·최종 배치·양측 접촉 해제 확인')
        record['cooperation']['resources_retained'] = False
        record['evidence']['final_placement'] = proof
        for rid in e['participants'].values():
            state = self.o.robot_states[rid]
            state.update(status='idle', task_id=None, path=[], reason=record['reason'])
            state['command_epoch'] += 1
            self.o.reservations.release_all(rid)
        self.o.emit('task_completed', record['robot_id'], record['reason'], dict(task_id=task_id, evidence=record['evidence']))

    def base_command(self, rid, now, observations):
        from .orchestration import angle
        state = self.o.robot_states[rid]
        e = self.executions.get(state['task_id'])
        stopped = dict(v=0., w=0., mode='stand')
        if not e or e['terminal'] or e['released'] or rid != e['participants']['carrier']:
            return stopped
        approaching = not e.get('loading_approach_done', True)
        result = (dict(hold=False, navigation_target=self.o.tasks[state['task_id']]['spec'].cooperation.carrier_loading_pose.model_dump())
                  if approaching else e['result'])
        if not result or result['hold'] or not result.get('navigation_target'):
            return stopped
        obs = observations.get(rid, {})
        if any(not self._valid_participant(peer_id, observations.get(peer_id), now) for peer_id in e['participants'].values()):
            return stopped
        peer=observations.get(e['participants']['receiver'],{})
        if (now-peer.get('sampled_at',-math.inf)>self.o.policy.stale_after or peer.get('fault')!='none'
                or math.sqrt(sum(v*v for v in peer.get('velocity',[math.inf])))>.04
                or math.sqrt(sum(v*v for v in peer.get('angular_velocity',[math.inf])))>.08):
            return stopped
        donor_id = e['participants'].get('donor')
        if donor_id:
            donor = observations.get(donor_id, {})
            if (now-donor.get('sampled_at',-math.inf)>self.o.policy.stale_after or donor.get('fault')!='none'
                    or math.sqrt(sum(v*v for v in donor.get('velocity',[math.inf])))>.04
                    or math.sqrt(sum(v*v for v in donor.get('angular_velocity',[math.inf])))>.08):
                return stopped
        target = result['navigation_target']
        if not approaching and e.get('trip_plan') and not state.get('trip'):
            trip = e.pop('trip_plan')
            receipt = self.o.facilities.request(trip['elevator_id'], rid, trip['source_floor'], trip['dest_floor'], trip['mass'], trip['envelope'])
            state['trip'] = dict(trip, request_id=receipt['request_id'])
            self.o.emit('cargo_elevator_reserved', rid, '적재 지지 확인 후 승강기 예약',
                        dict(task_id=state['task_id'], item_id=self.o.tasks[state['task_id']]['spec'].item_id, **receipt))
        trip = state.get('trip')
        if trip:
            command = self.o._trip_command(rid, state, obs, now)
            if not state.get('trip'):
                task = self.o.tasks[state['task_id']]['spec']
                e['route'] = self._handoff_route(self.o.robots[rid], obs, target, task.floor_id)
                if e['route'] is None:
                    self.terminate(task.id, now, '적재 하차 후 인계 공간 경로 없음')
                return stopped
            if command is not None:return command
            target = trip['staging']
        path = e['loading_route'] if approaching else e['route']
        while path and math.hypot(path[0]['x']-obs['pose']['x'],path[0]['y']-obs['pose']['y']) < .10:
            if path[0].get('align') and abs(angle(path[0]['yaw']-obs['pose']['yaw']))>.1:break
            path.pop(0)
        waypoint = path[0] if path else target
        dx, dy = waypoint['x']-obs['pose']['x'], waypoint['y']-obs['pose']['y']
        distance = math.hypot(dx,dy)
        aligning=bool(waypoint.get('align') and distance<.10)
        yaw = angle(waypoint['yaw']-obs['pose']['yaw']) if aligning else angle(math.atan2(dy,dx)-obs['pose']['yaw']) if distance > .07 else angle(target['yaw']-obs['pose']['yaw'])
        if trip and not path and distance <= .07 and abs(yaw) <= .1:
            trip['phase'] = 'ride'
            state['reason'] = '적재 상태 승강기 탑승 허가 대기'
            return stopped
        # Coordinated approach uses the measured front free space. Other robots
        # retain their full motion envelope; the stationary peer's actual base
        # remains a range obstacle inside the reserved handoff workspace.
        for other_id, other in observations.items():
            approach_peer = donor_id if approaching else e['participants']['receiver']
            if other_id == rid or other_id == approach_peer or now-other['sampled_at'] > self.o.policy.stale_after:
                continue
            if abs(other['pose']['z']-obs['pose']['z']) < 1.2 and math.hypot(other['pose']['x']-obs['pose']['x'],other['pose']['y']-obs['pose']['y']) < radius(self.o.robots[rid])+radius(self.o.robots[other_id])+self.o.policy.safety_distance:
                # After a verified retraction, permit only a straight departure
                # away from the reserved stationary donor. Turning or moving
                # toward its full arm envelope still waits. All participant
                # contacts and forward range remain active stop conditions.
                if other_id == donor_id and e.get('loading_committed') and abs(yaw)<.05:
                    away = (obs['pose']['x']-other['pose']['x'])*dx+(obs['pose']['y']-other['pose']['y'])*dy
                    feedback=other.get('sensors',{}).get('manipulation',{}).get(self.o.tasks[state['task_id']]['spec'].item_id,{})
                    if away>0 and feedback.get('finger_contacts')==[] and feedback.get('bilateral_contact') is False:
                        continue
                return stopped
        scan = obs.get('sensors',{}).get('lidar')
        if not isinstance(scan,dict):return stopped
        if isinstance(scan,dict):
            front = [d for a,d in zip(scan['angles'],scan['ranges']) if abs(a) < .3]
            if not front or not all(isinstance(d,(int,float)) and math.isfinite(d) and d>=0 for d in front):return stopped
            length = model_by_id(self.o.robots[rid].model_id)['size']['x']/2
            mount_x=scan.get('mount_position',[0.,0.,0.])[0]
            if front and min(front) < length-mount_x+self.o.policy.safety_distance:
                state['reason'] = '협업 접근 전방 실제 거리 여유 부족'
                return stopped
        speed = min(.15, self.o.robots[rid].max_speed, self.o.policy.speed_limit, distance*.65)
        return dict(v=speed if distance > .07 and abs(yaw)<.35 and not aligning else 0., w=max(-.3,min(.3,yaw*1.8)), mode='drive')

    def snapshot(self):
        return self.resources.snapshot()
