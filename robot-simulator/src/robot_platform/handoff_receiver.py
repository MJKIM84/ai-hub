"""Observation-only receive/hold/place sequence for the authored research arm.

Targets are world gripper origins; destination is the item bottom center.
This module owns no simulator/controller, attachment, custody, or reservation.
"""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import math


def _vec(value):
    if isinstance(value, Mapping):
        value = [value.get(axis) for axis in "xyz"]
    try:
        result = tuple(float(component) for component in value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("finite XYZ coordinates required") from error
    if len(result) != 3 or not all(math.isfinite(component) for component in result):
        raise ValueError("finite XYZ coordinates required")
    return result


def _distance(a, b=(0., 0., 0.)):
    return math.sqrt(sum((x-y)**2 for x, y in zip(a, b)))


def _quaternion(value):
    if not isinstance(value, (list,tuple)) or len(value) != 4:
        raise ValueError('missing_tool_orientation')
    if any(type(v) not in (int,float) or not math.isfinite(v) for v in value) or abs(sum(v*v for v in value)-1) > .001:
        raise ValueError('invalid_tool_orientation')
    return tuple(value)


class HandoffReceiver:
    VERSION = "observed-receive-place-0.6"
    PROFILE = dict(grasp_above_center_m=.10, approach_above_grasp_m=.10,
                   lift_above_grasp_m=.12, lift_toward_base_m=.02,
                   maximum_placement_overtravel_m=.012)
    MAX_PAYLOAD = 3.
    FRESH_AGE = 1.
    OBSERVATION_TIMEOUT = 2.
    TRACKING_TIMEOUT = 1.
    CONTACT_LOSS_TIMEOUT = .25
    SLIP_TIMEOUT = .20
    SLIP_DISTANCE = .025
    TOOL_TOLERANCE = .020
    SETTLED_SPEED = .035
    SUPPORT_FRACTION = .60
    TRANSFER_HEIGHT_ERROR = .01
    TRANSFER_CONTACT_DWELL = .15
    TRANSFER_RATE_FRACTION = .50
    TRANSFER_REMAINDER_FRACTION = .02
    TRANSFER_READY_DWELL = .25
    PHASE_TIMEOUTS = dict(approach=18., descend=12., grasp=6., lift=15.,
                          clearance=15., translate=20., lower=15., release=8., retract=15.)
    ACTIONS = frozenset(("prepare", "grasp", "lift_and_hold", "confirm_received", "place", "hold"))
    ALLOWED = dict(await_prepare={"prepare"}, approach={"prepare"}, ready={"prepare", "grasp"},
                   descend={"grasp", "lift_and_hold", "confirm_received"},
                   grasp={"grasp", "lift_and_hold", "confirm_received"},
                   grasped={"grasp", "lift_and_hold", "confirm_received"},
                   lift={"lift_and_hold", "confirm_received"},
                   received={"lift_and_hold", "confirm_received", "place"},
                   clearance={"place"}, translate={"place"}, lower={"place"}, release={"place"}, retract={"place"})

    def __init__(self, task_id, carrier_id, receiver_id, item_id, item_mass, item_size,
                 destination, timeout=120., *, manage_load_transfer=True, arm_geometry=None):
        if type(manage_load_transfer) is not bool:
            raise ValueError("manage_load_transfer must be a boolean")
        if not all(isinstance(value, str) and value for value in (task_id, carrier_id, receiver_id, item_id)):
            raise ValueError("nonempty task and participant IDs required")
        if carrier_id == receiver_id:
            raise ValueError("carrier and receiver must differ")
        self.task_id, self.carrier_id, self.receiver_id, self.item_id = task_id, carrier_id, receiver_id, item_id
        self.item_mass, self.timeout = float(item_mass), float(timeout)
        self.manage_load_transfer = manage_load_transfer
        if arm_geometry is not None and (not isinstance(arm_geometry, Mapping)
                                         or arm_geometry.get('robot_id') != receiver_id):
            raise ValueError('compiled arm geometry must identify this receiver')
        self.arm_geometry = deepcopy(arm_geometry)
        self._planned_targets = None
        self._place_target = None
        self._planning_observation = None
        self._planning_noise = 0.
        self.item_size, self.destination = _vec(item_size), _vec(destination)
        if not all(math.isfinite(value) and value > 0 for value in (self.item_mass, self.timeout, *self.item_size)):
            raise ValueError("positive finite mass, size, and timeout required")
        self.status, self.phase = "running", "await_prepare"
        self.code, self.reason = "await_prepare", "인수 준비 요청과 새 물품 관측을 기다립니다"
        self.target, self.opening, self.payload_estimate, self.hold = None, .1, 0., True
        self.report = None
        self.evidence = dict(source="observations", workflow_version=self.VERSION,
                             research_profile=deepcopy(self.PROFILE), events=[],
                             research_profile_scope='legacy_unplanned_fixture_defaults',
                             grasp_height_source=('compiled_wrist_capsule_and_observed_item' if arm_geometry is not None
                                                  else 'legacy_fixed_profile'),
                             manage_load_transfer=manage_load_transfer)
        self.evidence['geometry_mode'] = ('compiled_observed_planning' if arm_geometry is not None
                                          else 'legacy_unplanned_fixture')
        self._started = self._last_now = self._last_sample = self._last_fresh = self._phase_started = None
        self._stable_since = self._tracking_lost = self._contact_lost = self._slipping = None
        self._source = self._grasp = self._lift = self._held_offset = None
        self._held_local_offset = None
        self._holding = False
        self._place_grasp_z = self.destination[2]+self.item_size[2]/2+.10
        self._place_cruise_z = None
        self._lower_offset = 0.
        self._carry_opening = 0.
        self._held_bootstrap = None
        self._transfer_since = self._transfer_ready_since = None
        self._transfer_restore = False
        self._transfer_engaged = False
        self._release_settle_started = None
        self._retract_recheck_after = None

    def start_from_held(self, now, observation, *, opening=0., payload_estimate=None):
        """Observe a stable existing grasp, then enter placement without opening.

        Repeated fresh observations are required for .30 s. This public entry
        point never requests prepare/descent/closing or invents a prior lift.
        It does not establish custody or external-support separation; the
        recovery coordinator checks those independent observations.
        """
        if self.phase not in ("await_prepare", "verify_held") or self.status != "running":
            raise ValueError("held initialization requires a new unstarted receiver")
        now, opening = float(now), float(opening)
        payload = self.item_mass if payload_estimate is None else float(payload_estimate)
        if (not math.isfinite(now) or (self._last_now is not None and now < self._last_now)
                or not math.isfinite(opening) or not 0 <= opening <= .1
                or not math.isfinite(payload) or payload < 0):
            raise ValueError("finite monotonic time and valid retained gripper command required")
        if self._held_bootstrap and self._held_bootstrap["command"] != (opening, payload):
            raise ValueError("held initialization must retain the same gripper command")
        self._last_now = now
        if self._started is None:
            self._started = self._phase_started = self._last_fresh = now
        self.opening, self.payload_estimate, self._carry_opening = opening, payload, opening
        self.phase, self.hold = "verify_held", True
        if self.item_mass > self.MAX_PAYLOAD:
            return self._fail("overload", "연구용 팔의 검증 적재량을 초과합니다")
        if now-self._started >= min(self.timeout, 12.):
            return self._fail("held_verification_timeout", "기존 파지 안정 확인 제한 시간을 초과했습니다")
        try:
            reading = self._read(now, observation)
            if self._last_sample is not None and reading["stamp"] < self._last_sample:
                raise ValueError("reordered_observation")
        except ValueError as error:
            if now-self._last_fresh >= self.OBSERVATION_TIMEOUT:
                return self._fail("observation_timeout", "기존 파지의 관측이 소실되었습니다")
            return self._wait(str(error), "기존 파지의 새 관측을 기다립니다")
        stamp = reading["stamp"]
        self._planning_observation = deepcopy(observation)
        if reading["fault"] not in (None, False, "none") or reading["sensors"].get("controller_error"):
            return self._fail("receiver_fault", "복구 팔이 장애를 보고했습니다", stamp)
        if reading["upright"] < .98 or reading["wrong_contact"]:
            return self._fail("invalid_held_state", "기존 파지의 식별자·차체 자세가 유효하지 않습니다", stamp)
        if reading["operator_hold"] or not reading["bilateral"]:
            return self._wait("held_grip_pending", "현재 그리퍼를 유지하며 양쪽 파지를 기다립니다")
        if stamp == self._last_sample:
            self.code = "awaiting_fresh_observation"
            return self._result()
        if self._last_sample is not None and stamp-self._last_sample > .5:
            self._stable_since = None
            self._held_bootstrap = None
        self._last_sample, self._last_fresh = stamp, now
        item = self._item(reading)
        if item is None:
            return self._wait("item_tracking_pending", "현재 보유 물품의 위치·속도를 기다립니다")
        if self._held_bootstrap is None:
            self._held_bootstrap = dict(command=(opening, payload), tool=reading["tool"], item=item["position"])
        tool_error = _distance(reading["tool"], self._held_bootstrap["tool"])
        item_drift = _distance(item["position"], self._held_bootstrap["item"])
        stable = (_distance(item["velocity"]) <= self.SETTLED_SPEED
                  and _distance(reading["velocity"]) <= .04 and _distance(reading["angular"]) <= .08
                  and tool_error <= self.TOOL_TOLERANCE and item_drift <= self.TOOL_TOLERANCE)
        if not stable:
            self._held_bootstrap.update(tool=reading["tool"], item=item["position"])
        if self._stable(stable, stamp, .30):
            since = self._stable_since
            self._holding = True
            self._source = item["position"]
            self._held_offset = tuple(item["position"][i]-reading["tool"][i] for i in range(3))
            self._remember_local_grip(reading)
            self._place_grasp_z = self.destination[2]+self.item_size[2]/2-self._held_offset[2]
            self._place_cruise_z = max(reading["tool"][2], self._place_grasp_z+.12)
            if self.arm_geometry is not None and not self._prepare_motion_plan(observation, item, already_held=True,
                    tool=reading['tool'], tool_quaternion=reading['tool_quaternion']):
                return self._result()
            self.evidence["held_confirmation"] = dict(sampled_at=stamp, stable_since=since,
                stable_duration_s=stamp-since, bilateral_contact=True, item_position=list(item["position"]),
                tool_position=list(reading["tool"]), tool_error_m=tool_error, item_drift_m=item_drift)
            self._event("existing_grasp_confirmed", stamp)
            self._transition("clearance", now, stamp,
                self._planned_targets['clearance'] if self._planned_targets else (*reading["tool"][:2], self._place_cruise_z), opening)
            self.hold = False
        else:
            self.code = "held_stability_pending"
        return self._result()

    def _result(self):
        release_settle = (self.phase == 'release' and self.status == 'running' and not self.hold
                          and self.opening == .1 and self.payload_estimate == 0.)
        if (self.arm_geometry is not None and self.status == 'running' and not self.hold and not release_settle
                and self.target is not None and self._planning_observation is not None):
            from .arm_kinematics import solve_observed, ArmKinematicsError
            try:
                checked = solve_observed(self.arm_geometry, self._planning_observation, self.target,
                    margin_m=.015+3*self._planning_noise, joint_margin_rad=.02)
                self.evidence['target_validation'] = dict(sampled_at=self._planning_observation['sampled_at'],
                                                         target=list(self.target), **checked)
            except ArmKinematicsError as error:
                self.evidence['target_rejection'] = dict(code=error.code, target=list(self.target),
                    sampled_at=self._planning_observation.get('sampled_at'))
                return self._fail('arm_target_'+error.code, '현재 관측과 기구학 여유로 팔 목표를 실행할 수 없습니다')
        return dict(task_id=self.task_id, receiver_id=self.receiver_id, carrier_id=self.carrier_id,
                    item_id=self.item_id, target=list(self.target) if self.target is not None else None,
                    opening=self.opening, payload_estimate=self.payload_estimate, hold=self.hold,
                    release_settle=release_settle,
                    report=deepcopy(self.report), status=self.status, phase=self.phase,
                    code=self.code, reason=self.reason, evidence=deepcopy(self.evidence))

    def _prepare_motion_plan(self, observation, item, *, already_held=False, approach_completed=False,
                             tool=None, tool_quaternion=None):
        from .arm_motion_plan import plan_motion, ArmMotionPlanError
        self._planning_noise = item['noise']
        try:
            current_offset = (tuple(item['position'][i]-tool[i] for i in range(3))
                              if already_held or approach_completed else self._held_offset)
            plan = plan_motion(self.arm_geometry, observation,
                item['position'] if already_held else self._source, self.item_size, self.destination,
                noise=item['noise'], held_offset=current_offset, current_tool=tool,
                already_held=already_held, approach_completed=approach_completed,
                item_quaternion=item.get('quaternion'), current_tool_quaternion=tool_quaternion)
        except (ArmMotionPlanError, ValueError) as error:
            self.evidence['motion_plan'] = deepcopy(getattr(error, 'evidence', dict(rejection=str(error))))
            self._fail(getattr(error, 'code', 'arm_plan_invalid'), '관측 물품과 도달 여유를 만족하는 팔 경로가 없습니다')
            return False
        if 'motion_plan' in self.evidence:
            previous = self.evidence['motion_plan']
            self.evidence.setdefault('motion_plan_history', []).append({key:deepcopy(previous[key]) for key in
                ('sampled_at','source_item_position','destination_bottom','held_offset','targets','sweeps',
                 'minimum_reach_margin_m','grasp_geometry','planning_stage','version')
                if key in previous})
        self._planned_targets = plan['targets']
        self.evidence['motion_plan'] = plan['evidence']
        self._place_target = self._planned_targets['lower']
        self._place_grasp_z = self._place_target[2]
        self._place_cruise_z = self._planned_targets['clearance'][2]
        if not already_held:
            self._grasp, self._lift = self._planned_targets['grasp'], self._planned_targets['lift']
        return True

    def _lower_target(self):
        xy = self._place_target[:2] if self._place_target is not None else self.destination[:2]
        return (*xy, self._place_grasp_z-self._lower_offset)

    def _remember_local_grip(self, reading):
        if self.arm_geometry is not None:
            from .arm_motion_plan import _rotate
            q = reading['tool_quaternion']
            self._held_local_offset = _rotate((q[0],-q[1],-q[2],-q[3]), self._held_offset)

    def _expected_held_offset(self, reading):
        if self._held_local_offset is not None:
            from .arm_motion_plan import _rotate
            return _rotate(reading['tool_quaternion'], self._held_local_offset)
        return self._held_offset

    def _event(self, name, stamp, **extra):
        self.evidence["events"].append(dict(event=name, sampled_at=stamp, phase=self.phase, **extra))

    def _fail(self, code, reason, stamp=None):
        self.status, self.code, self.reason, self.hold = "failed", code, reason, True
        self.report, self._stable_since = None, None
        self._transfer_since = self._transfer_ready_since = None
        self._event("failed", stamp, code=code)
        # Opening and compensation are deliberately retained. Failure never
        # turns a gripped load into an automatic release or new grasp.
        return self._result()

    def _wait(self, code, reason):
        if self.phase == 'retract':
            self._retract_recheck_after = self._last_sample
        self.code, self.reason, self.hold = code, reason, True
        self.report, self._stable_since = None, None
        self._transfer_since = self._transfer_ready_since = None
        return self._result()

    def _transition(self, phase, now, stamp, target=None, opening=None):
        self.phase, self._phase_started, self._stable_since = phase, now, None
        if target is not None:
            self.target = tuple(target)
        if opening is not None:
            self.opening = opening
        self.code, self.reason = phase, f"{phase} 단계의 물리 관측을 확인합니다"
        self._event("phase_entered", stamp)

    def _stable(self, condition, stamp, duration=.20):
        if not condition:
            self._stable_since = None
            return False
        if self._stable_since is None:
            self._stable_since = stamp
        return stamp-self._stable_since >= duration-1e-9

    def _report(self, state, stamp):
        self.report = dict(task_id=self.task_id, carrier_id=self.carrier_id,
                           receiver_id=self.receiver_id, item_id=self.item_id,
                           state=state, sampled_at=stamp)

    def _read(self, now, obs):
        if not isinstance(obs, Mapping) or obs.get("robot_id") != self.receiver_id:
            raise ValueError("missing_or_wrong_receiver")
        try:
            stamp = float(obs["sampled_at"])
            base, velocity = _vec(obs["pose"]), _vec(obs["velocity"])
            angular = _vec(obs["angular_velocity"])
            upright = float(obs["upright"])
        except (KeyError, TypeError, ValueError, OverflowError) as error:
            raise ValueError("invalid_receiver_observation") from error
        if not all(math.isfinite(value) for value in (stamp, upright)) or stamp > now+1e-6:
            raise ValueError("future_observation")
        if now-stamp > self.FRESH_AGE:
            raise ValueError("stale_observation")
        sensors = obs.get("sensors")
        if not isinstance(sensors, Mapping):
            raise ValueError("missing_sensors")
        reports = sensors.get("manipulation", {})
        feedback = reports.get(self.item_id, {}) if isinstance(reports, Mapping) and "tool_position" not in reports else reports
        if not isinstance(feedback, Mapping):
            raise ValueError("missing_manipulation")
        try:
            tool = _vec(feedback["tool_position"])
        except (KeyError, ValueError) as error:
            raise ValueError("missing_manipulation") from error
        fingers = feedback.get("finger_contacts")
        if not isinstance(fingers, (list, tuple)) or any(side not in ("left", "right") for side in fingers):
            raise ValueError("invalid_finger_contacts")
        identified = (isinstance(reports, Mapping) and self.item_id in reports) or feedback.get("contact_item_id") == self.item_id
        bilateral = identified and feedback.get("bilateral_contact") is True and {"left", "right"} <= set(fingers)
        released = feedback.get("bilateral_contact") is False and not fingers
        tool_quaternion = _quaternion(feedback.get('tool_quaternion')) if self.arm_geometry is not None else None
        return dict(stamp=stamp, base=base, tool=tool, velocity=velocity, angular=angular,
                    tool_quaternion=tool_quaternion,
                    upright=upright, sensors=sensors, bilateral=bilateral, released=released, feedback=feedback,
                    fault=obs.get("fault", "none"), operator_hold=obs.get("operator_hold", False),
                    wrong_contact=feedback.get("bilateral_contact") is True and not identified)

    def _item(self, reading):
        items = reading["sensors"].get("items", [])
        if not isinstance(items, list):
            return None
        matches = [row for row in items if isinstance(row, Mapping) and row.get("id") == self.item_id]
        if len(matches) != 1 or matches[0].get("visible", True) is not True:
            return None
        try:
            noise = float(matches[0].get("position_noise_std_m", 0.))
            if not math.isfinite(noise) or noise < 0:
                return None
            return dict(position=_vec(matches[0]["position"]), velocity=_vec(matches[0]["velocity"]),
                        support_contacts=matches[0].get("support_contacts"), noise=noise,
                        quaternion=matches[0].get('quaternion'))
        except (KeyError, TypeError, ValueError, OverflowError):
            return None

    def _support(self, reading, item):
        # Prefer per-visible-item contacts to avoid counting the same contact
        # twice when it is also present in the receiver's robot contact list.
        contacts = item["support_contacts"]
        if contacts is None:
            contacts = reading["sensors"].get("contacts", [])
        if not isinstance(contacts, list):
            raise ValueError("invalid_support_contacts")
        upward = 0.
        own_contact = False
        for row in contacts:
            if not isinstance(row, Mapping):
                raise ValueError("invalid_support_contacts")
            a, b = row.get("geom_a"), row.get("geom_b")
            if self.item_id+"/shape" not in (a, b):
                continue
            other = a if b == self.item_id+"/shape" else b
            if not isinstance(other, str):
                raise ValueError("invalid_support_contacts")
            try:
                force, point = _vec(row["force_on_b_world"]), _vec(row["position"])
                magnitude = float(row["force"])
            except (KeyError, TypeError, ValueError, OverflowError) as error:
                raise ValueError("support_force_unavailable") from error
            if not math.isfinite(magnitude) or magnitude < 0:
                raise ValueError("invalid_support_contacts")
            if other.startswith(self.receiver_id+"/"):
                own_contact |= magnitude > .1
                continue
            if abs(_distance(force)-magnitude) > max(1e-6, magnitude*1e-6):
                raise ValueError("inconsistent_support_force")
            on_destination = (math.hypot(point[0]-self.destination[0], point[1]-self.destination[1])
                              <= math.hypot(*self.item_size[:2])/2+.025
                              and abs(point[2]-self.destination[2]) <= .025)
            if on_destination:
                upward += max(0., force[2] if b == self.item_id+"/shape" else -force[2])
        # Some adapters expose only supporting external contacts on the item.
        # Receiver body contacts must still veto a completed release, without
        # counting support forces from the second list a second time.
        robot_contacts = reading["sensors"].get("contacts", [])
        if not isinstance(robot_contacts, list):
            raise ValueError("invalid_support_contacts")
        for row in robot_contacts:
            if not isinstance(row, Mapping):
                raise ValueError("invalid_support_contacts")
            pair = (row.get("geom_a"), row.get("geom_b"))
            if self.item_id+"/shape" not in pair:
                continue
            if not any(isinstance(geom, str) and geom.startswith(self.receiver_id+"/") for geom in pair):
                continue
            try:
                magnitude = float(row["force"])
            except (KeyError, TypeError, ValueError, OverflowError) as error:
                raise ValueError("support_force_unavailable") from error
            if not math.isfinite(magnitude) or magnitude < 0:
                raise ValueError("invalid_support_contacts")
            own_contact |= magnitude > .1
        return upward, own_contact

    def _delivered_grip(self, reading):
        """Controller settings received through the observation bus, not mass sensing."""
        feedback = reading["feedback"]
        opening, payload = feedback.get("commanded_opening"), feedback.get("payload_estimate_kg")
        numeric = all(isinstance(value, (int, float)) and not isinstance(value, bool)
                      and math.isfinite(value) for value in (opening, payload))
        valid = numeric and 0 <= opening <= .1 and payload >= 0
        return dict(valid=valid, opening=float(opening) if valid else None,
                    payload=float(payload) if valid else None)

    def _release_delivered(self, reading):
        """Delivered settings are required in addition to physical release proof."""
        delivered = self._delivered_grip(reading)
        return bool(delivered['valid'] and abs(delivered['opening']-.1) <= 1e-9
                    and delivered['payload'] <= 1e-9
                    and reading['feedback'].get('control_mode') == 'release_settle')

    def _duplicate_release_veto(self, reading):
        if self.phase != 'release':
            return None
        item = self._item(reading)
        if item is None:
            return self._wait('item_tracking_pending', '해제 중 반복 표본의 물품 소실로 안정을 재확인합니다')
        try:
            upward, own_contact = self._support(reading, item)
        except ValueError as error:
            return self._wait(str(error), '해제 중 반복 표본의 지지 증거가 유효하지 않습니다')
        placed = (math.hypot(item['position'][0]-self.destination[0], item['position'][1]-self.destination[1]) <= .04
                  and abs(item['position'][2]-self.destination[2]-self.item_size[2]/2) <= .025)
        supported = placed and upward >= self.SUPPORT_FRACTION*self.item_mass*9.81
        if self.manage_load_transfer and not supported:
            return self._fail('release_support_lost', '개방 중 반복 표본의 지지 소실로 명령과 예약을 유지합니다', reading['stamp'])
        if not self._delivered_grip(reading)['valid']:
            return self._wait('release_delivery_pending', '반복 표본의 개방 전달 설정이 불완전합니다')
        settings = self._delivered_grip(reading)
        if self._release_settle_started is not None and (abs(settings['opening']-.1) > 1e-9 or settings['payload'] > 1e-9):
            return self._wait('release_delivery_pending', '개방·무하중 보상의 전달 설정을 재확인합니다')
        if not (reading['released'] and not own_contact and supported
                and _distance(item['velocity']) <= self.SETTLED_SPEED and self._release_delivered(reading)):
            self._stable_since = None
        return None

    def _retract_veto(self, reading):
        """Fresh or repeated danger can stop retreat; neither earns dwell."""
        if self.phase != 'retract':
            return None
        item = self._item(reading)
        if item is None:
            return self._wait('item_tracking_pending', '후퇴 중 물품 관측을 재확인합니다')
        if item['support_contacts'] is None and 'contacts' not in reading['sensors']:
            return self._wait('invalid_support_contacts', '후퇴 중 지지 접촉 관측을 재확인합니다')
        try:
            upward, own_contact = self._support(reading, item)
        except ValueError as error:
            return self._wait(str(error), '후퇴 중 지지 접촉 관측을 재확인합니다')
        placed = (math.hypot(item['position'][0]-self.destination[0], item['position'][1]-self.destination[1]) <= .04
                  and abs(item['position'][2]-self.destination[2]-self.item_size[2]/2) <= .025)
        supported = placed and upward >= self.SUPPORT_FRACTION*self.item_mass*9.81
        self.evidence['retract_safety'] = dict(sampled_at=reading['stamp'], own_contact=own_contact,
            released=reading['released'], destination_supported=supported, support_force_N=upward,
            item_speed_m_s=_distance(item['velocity']))
        if own_contact or not reading['released']:
            return self._fail('retract_contact', '후퇴 중 물품 접촉이 다시 관측되어 팔과 예약을 유지합니다', reading['stamp'])
        if not supported:
            return self._fail('retract_support_lost', '후퇴 중 물품 지지가 소실되어 팔과 예약을 유지합니다', reading['stamp'])
        settings = self._delivered_grip(reading)
        if not settings['valid'] or abs(settings['opening']-.1) > 1e-9 or settings['payload'] > 1e-9:
            return self._wait('retract_delivery_pending', '후퇴 중 개방·무하중 보상 전달을 재확인합니다')
        if _distance(item['velocity']) > self.SETTLED_SPEED:
            return self._wait('retract_item_unsettled', '후퇴 중 물품 안정을 재확인합니다')
        return None

    def _transfer_load(self, reading, item, upward, stamp, dt):
        """Return (opening_ready, defer_lowering) from one current observation."""
        if not self.manage_load_transfer:
            return True, False
        delivered = self._delivered_grip(reading)
        height = abs(item["position"][2]-self.destination[2]-self.item_size[2]/2)
        aligned = math.hypot(item["position"][0]-self.destination[0], item["position"][1]-self.destination[1]) <= .04
        speed = _distance(item["velocity"])
        contact = (reading["bilateral"] and aligned and height <= self.TRANSFER_HEIGHT_ERROR
                   and speed <= self.SETTLED_SPEED and upward > .1)
        identity = dict(source="observations", workflow_version=self.VERSION,
            task_id=self.task_id, item_id=self.item_id, receiver_id=self.receiver_id,
            carrier_id=self.carrier_id, sampled_at=stamp,
            upward_support_force_N=upward, height_error_m=height, item_speed_m_s=speed,
            bilateral_contact=reading["bilateral"],
            observed_command_feedback_valid=delivered["valid"],
            observed_commanded_opening=delivered["opening"],
            observed_payload_estimate_kg=delivered["payload"],
            observed_command_settings_source="delayed_controller_feedback")
        if not contact:
            self._transfer_since = self._transfer_ready_since = None
            if self._transfer_engaged and self.payload_estimate < self.item_mass:
                # Only current, otherwise valid held observations reach here.
                # A normal stationary command is needed: hold=True would keep
                # the delivered low compensation instead of restoring it.
                self.payload_estimate, self.opening = self.item_mass, self._carry_opening
                self.target, self.hold, self._transfer_restore = reading["tool"], False, True
                self._stable_since = None
                self.code, self.reason = "load_transfer_support_pending", "현재 도구 위치와 파지를 유지하며 전체 하중 보상을 복원합니다"
            self.evidence["load_transfer"] = dict(identity, active=False, payload_estimate_kg=self.payload_estimate,
                                                  restoring=self._transfer_restore, release_ready_since=None)
            return False, self._transfer_restore
        if not delivered["valid"] or abs(delivered["opening"]-self._carry_opening) > 1e-6:
            # A generated command is not evidence that the gripper still has
            # valid closed settings. Do not accumulate dwell or reduce load
            # compensation until a fresh delivered setting confirms them.
            self._wait("load_transfer_feedback_pending", "현재 전달된 파지 설정을 확인할 때까지 하중 전달을 정지합니다")
            self.evidence["load_transfer"] = dict(identity, active=False,
                payload_estimate_kg=self.payload_estimate, restoring=self._transfer_restore,
                release_ready_since=None)
            return False, True
        if self._transfer_restore:
            self.target = self._lower_target()
            self._transfer_restore = False
        if self._transfer_since is None:
            self._transfer_since = stamp
        desired = max(0., self.item_mass-upward/9.81)
        interval = min(.1, max(0., dt))
        if stamp-self._transfer_since >= self.TRANSFER_CONTACT_DWELL-1e-9:
            change = self.TRANSFER_RATE_FRACTION*self.item_mass*interval
            # Actively unload at a bounded rate. The measured residual load
            # is a release veto, not a target that can trap this controller
            # at a stable arm/floor load-sharing equilibrium.
            self._transfer_engaged |= self.payload_estimate > 0 and change > 0
            self.payload_estimate = max(0., self.payload_estimate-change)
        limit = self.TRANSFER_REMAINDER_FRACTION*self.item_mass
        ready = (self.payload_estimate <= limit and desired <= limit and delivered["valid"]
                 and delivered["payload"] <= limit
                 and abs(delivered["opening"]-self._carry_opening) <= 1e-6)
        if not ready:
            self._transfer_ready_since = None
        elif self._transfer_ready_since is None:
            self._transfer_ready_since = stamp
        self.evidence["load_transfer"] = dict(identity, active=True, restoring=False,
            desired_payload_estimate_kg=desired, payload_estimate_kg=self.payload_estimate,
            strategy="bounded_unloading_with_observed_support_gate", unloading_target_kg=0.,
            observed_unsupported_mass_kg=desired,
            contact_since=self._transfer_since, contact_duration_s=stamp-self._transfer_since,
            minimum_contact_duration_s=self.TRANSFER_CONTACT_DWELL,
            maximum_rate_kg_s=self.TRANSFER_RATE_FRACTION*self.item_mass, command_sample_interval_s=interval,
            maximum_release_payload_kg=limit, retained_grip_opening=self._carry_opening,
            release_ready_since=self._transfer_ready_since, minimum_release_dwell_s=self.TRANSFER_READY_DWELL)
        return bool(ready and stamp-self._transfer_ready_since >= self.TRANSFER_READY_DWELL-1e-9), False

    def _duplicate_transfer_veto(self, reading):
        """Repeated timestamps can invalidate evidence, never advance unloading."""
        if not self.manage_load_transfer or self.phase not in ("lower", "release"):
            return None
        item = self._item(reading)
        if item is None:
            return self._wait("item_tracking_pending", "반복 표본의 물품 관측 소실로 해제 준비를 취소합니다")
        try:
            upward, _ = self._support(reading, item)
        except ValueError as error:
            return self._wait(str(error), "반복 표본의 지지 증거가 유효하지 않습니다")
        height = abs(item["position"][2]-self.destination[2]-self.item_size[2]/2)
        aligned = math.hypot(item["position"][0]-self.destination[0], item["position"][1]-self.destination[1]) <= .04
        if self.phase == "release":
            if not (aligned and height <= .025 and upward >= self.SUPPORT_FRACTION*self.item_mass*9.81):
                return self._fail("release_support_lost", "개방 중 반복 표본의 지지 소실로 명령과 예약을 유지합니다", reading["stamp"])
            return None
        offset = tuple(item["position"][i]-reading["tool"][i] for i in range(3))
        if self._holding and _distance(offset, self._expected_held_offset(reading)) > max(self.SLIP_DISTANCE, 3*max(0., item["noise"])):
            return self._wait("slip_pending", "반복 표본의 물품 상대 이동으로 해제 준비를 취소합니다")
        if self.target is not None and _distance(reading["tool"], self.target) > self.TOOL_TOLERANCE:
            self._stable_since = None
        contact = (aligned and height <= self.TRANSFER_HEIGHT_ERROR
                   and _distance(item["velocity"]) <= self.SETTLED_SPEED and upward > .1)
        if (self._transfer_engaged or self._transfer_since is not None) and not contact:
            return self._wait("load_transfer_evidence_lost", "반복 표본의 지지 이상으로 새 관측을 기다립니다")
        if self._transfer_engaged or self._transfer_since is not None:
            delivered = self._delivered_grip(reading)
            if not delivered["valid"] or abs(delivered["opening"]-self._carry_opening) > 1e-6:
                return self._wait("load_transfer_feedback_pending", "반복 표본의 전달된 파지 설정을 재확인합니다")
        if self._transfer_ready_since is not None:
            delivered = self._delivered_grip(reading)
            limit = self.TRANSFER_REMAINDER_FRACTION*self.item_mass
            if (max(0., self.item_mass-upward/9.81) > limit or not delivered["valid"]
                    or delivered["payload"] > limit
                    or abs(delivered["opening"]-self._carry_opening) > 1e-6):
                return self._wait("load_transfer_evidence_lost", "반복 표본의 전달 설정·지지를 재확인합니다")
        return None

    def update(self, now, receiver_observation, action, *, allow_release=True):
        # A coordinator may require additional support evidence, but cannot
        # use this gate to bypass any local placement or release predicate.
        if type(allow_release) is not bool:
            raise ValueError("allow_release must be a boolean")
        now = float(now)
        if not math.isfinite(now) or (self._last_now is not None and now < self._last_now):
            raise ValueError("receiver time must be finite and monotonic")
        if action not in self.ACTIONS:
            raise ValueError("unsupported receiver action")
        self._last_now = now
        if self._started is None:
            self._started = self._phase_started = self._last_fresh = now
        if self.status in ("failed", "completed"):
            return self._result()
        if self.item_mass > self.MAX_PAYLOAD:
            return self._fail("overload", "연구용 팔의 검증 적재량을 초과합니다")
        if now-self._started >= self.timeout:
            return self._fail("timeout", "인수·놓기 실행 제한 시간을 초과했습니다", self._last_sample)
        try:
            reading = self._read(now, receiver_observation)
            if self._last_sample is not None and reading["stamp"] < self._last_sample:
                raise ValueError("reordered_observation")
        except ValueError as error:
            if now-self._last_fresh >= self.OBSERVATION_TIMEOUT:
                return self._fail("observation_timeout", "인수 팔의 신선한 관측이 소실되었습니다", self._last_sample)
            return self._wait(str(error), "유효한 새 인수 팔 관측을 기다립니다")
        stamp = reading["stamp"]
        self._planning_observation = deepcopy(receiver_observation)
        if reading["fault"] not in (None, False, "none"):
            return self._fail("receiver_fault", "인수 팔이 장애를 보고했습니다", stamp)
        if reading["sensors"].get("controller_error"):
            return self._fail("controller_error", str(reading["sensors"]["controller_error"]), stamp)
        if reading["upright"] < .98:
            return self._fail("unstable_base", "인수 팔 기반이 검증 자세를 벗어났습니다", stamp)
        if reading["wrong_contact"]:
            return self._fail("wrong_item_contact", "다른 물품의 접촉을 보고했습니다", stamp)
        paused = action == "hold" or reading["operator_hold"]
        if stamp == self._last_sample:
            if self.phase == "lower" and not allow_release:
                self._stable_since = None
            if paused:
                return self._wait("operator_hold", "현재 그리퍼와 하중 보상을 유지하며 팔 궤적을 정지합니다")
            if self._holding and not reading["bilateral"] and self.phase not in ("release", "retract"):
                return self._wait("contact_loss_pending", "반복 표본의 파지 이상을 확인하여 정지합니다")
            if self._holding and self.phase not in ('release','retract'):
                repeated_item = self._item(reading)
                if repeated_item is None:
                    return self._wait('item_tracking_pending', '반복 표본의 물품 관측이 소실되었습니다')
                repeated_offset = tuple(repeated_item['position'][i]-reading['tool'][i] for i in range(3))
                if _distance(repeated_offset,self._expected_held_offset(reading)) > max(self.SLIP_DISTANCE,3*repeated_item['noise']):
                    return self._wait('slip_pending', '반복 표본의 물품 상대 이동으로 동작을 정지합니다')
            if _distance(reading["velocity"]) > .04 or _distance(reading["angular"]) > .08:
                return self._wait("base_moving", "반복 표본의 기반 이동을 확인하여 정지합니다")
            veto = self._duplicate_release_veto(reading)
            if veto is not None:
                return veto
            veto = self._retract_veto(reading)
            if veto is not None:
                return veto
            veto = self._duplicate_transfer_veto(reading)
            if veto is not None:
                return veto
            self.code = "awaiting_fresh_observation"
            return self._result()
        dt = .05 if self._last_sample is None else stamp-self._last_sample
        if dt > .5:
            self._stable_since = None
            self._transfer_since = self._transfer_ready_since = None
        self._last_sample, self._last_fresh = stamp, now
        self.report = None
        item = self._item(reading)
        if item is None:
            if self._tracking_lost is None:
                self._tracking_lost = now
            if now-self._tracking_lost >= self.TRACKING_TIMEOUT-1e-9:
                return self._fail("item_tracking_lost", "물품 위치·속도 관측이 소실되었습니다", stamp)
            return self._wait("item_tracking_pending", "물품 관측이 복구되기를 기다립니다")
        self._tracking_lost = None
        veto = self._retract_veto(reading)
        if veto is not None:
            return veto
        position, tool = item["position"], reading["tool"]
        self._planning_noise = item['noise']
        speed, bilateral, released = _distance(item["velocity"]), reading["bilateral"], reading["released"]
        self.evidence.update(sampled_at=stamp, tool_position=list(tool), item_position=list(position),
                             item_speed=speed, bilateral_contact=bilateral)
        if self._holding and self.phase not in ("release", "retract"):
            if not bilateral:
                if self._contact_lost is None:
                    self._contact_lost = now
                if now-self._contact_lost >= self.CONTACT_LOSS_TIMEOUT-1e-9:
                    return self._fail("receiver_contact_lost", "물품의 양쪽 파지 접촉이 소실되었습니다", stamp)
                return self._wait("contact_loss_pending", "그리퍼를 유지하고 접촉 소실을 확인합니다")
            self._contact_lost = None
            offset = tuple(position[i]-tool[i] for i in range(3))
            drift = _distance(offset, self._expected_held_offset(reading))
            threshold = max(self.SLIP_DISTANCE, 3*max(0., item["noise"]))
            self.evidence.update(held_offset_error_m=drift, held_offset_limit_m=threshold)
            if drift > threshold:
                if self._slipping is None:
                    self._slipping = now
                if now-self._slipping >= self.SLIP_TIMEOUT-1e-9:
                    return self._fail("item_slipping", "손가락 접촉이 남아 있지만 물품이 도구에 대해 미끄러졌습니다", stamp)
                return self._wait("slip_pending", "파지 중 물품의 상대 변위를 확인하여 정지합니다")
            self._slipping = None
        if paused:
            return self._wait("operator_hold", "현재 그리퍼와 하중 보상을 유지하며 팔 궤적을 정지합니다")
        if _distance(reading["velocity"]) > .04 or _distance(reading["angular"]) > .08:
            return self._wait("base_moving", "인수 팔 기반의 정지를 기다립니다")
        if action not in self.ALLOWED[self.phase]:
            return self._wait("action_out_of_phase", "현재 단계에 맞는 인수 동작을 기다립니다")
        if self.phase == 'retract' and self._retract_recheck_after is not None:
            if stamp <= self._retract_recheck_after:
                return self._wait('awaiting_fresh_observation', '후퇴 재개 전 새 관측을 기다립니다')
            if self.arm_geometry is not None:
                from .arm_motion_plan import check_open_path, ArmMotionPlanError
                feedback = reading['feedback']
                joints, targets = feedback.get('arm_joint_positions_rad'), feedback.get('arm_joint_targets_rad')
                if joints is None or targets is None or item.get('quaternion') is None:
                    return self._wait('retract_observation_pending', '후퇴 재개 전 현재 관절·물품 방향 관측을 기다립니다')
                try:
                    proof = check_open_path(self.arm_geometry,receiver_observation,tool,self.target,
                        position,self.item_size,noise=item['noise'],item_quaternion=item['quaternion'],
                        finger_positions=feedback.get('finger_positions_m'),current_tool_quaternion=reading['tool_quaternion'],
                        current_joint_positions=joints,start_joint_targets=targets)
                except ArmMotionPlanError as error:
                    self.evidence['retract_revalidation'] = error.evidence
                    return self._fail(error.code, '일시 정지 후 같은 후퇴 목표까지의 현재 경로가 안전하지 않습니다', stamp)
                self.evidence['retract_revalidation'] = dict(proof,after_hold_sampled_at=self._retract_recheck_after,
                    fixed_target=list(self.target))
                self._event('retract_revalidated',stamp)
            self._retract_recheck_after = None
        self.hold = False
        self.code, self.reason = self.phase, f"{self.phase} 단계의 물리 관측을 확인합니다"
        if now-self._phase_started >= self.PHASE_TIMEOUTS.get(self.phase, math.inf):
            return self._fail("phase_timeout", f"{self.phase} 단계 제한 시간을 초과했습니다", stamp)
        if stamp < self._phase_started:
            return self._result()
        at_target = self.target is not None and _distance(tool, self.target) <= self.TOOL_TOLERANCE
        if self.phase == "await_prepare":
            if speed > self.SETTLED_SPEED:
                return self._wait("source_moving", "차량 위 물품의 정지를 기다립니다")
            self._source = position
            self._grasp = (position[0], position[1], position[2]+.10)
            inward = (reading["base"][0]-position[0], reading["base"][1]-position[1])
            length = math.hypot(*inward)
            shift = tuple(.02*axis/max(length, 1e-9) for axis in inward)
            self._lift = (position[0]+shift[0], position[1]+shift[1], self._grasp[2]+.12)
            if self.arm_geometry is not None and not self._prepare_motion_plan(receiver_observation, item):
                return self._result()
            self._transition("approach", now, stamp,
                self._planned_targets['approach'] if self._planned_targets else (*position[:2], self._grasp[2]+.10), .1)
        elif self.phase in ("approach", "ready", "descend", "grasp"):
            if _distance(position, self._source) > .05:
                return self._fail("item_moved_before_grasp", "인수 시작 위치에서 물품이 이동했습니다", stamp)
            if self.phase == "approach":
                if self._stable(at_target and speed <= self.SETTLED_SPEED, stamp):
                    self._transition("ready", now, stamp)
                    self._report("ready", stamp)
            elif self.phase == "ready":
                if not at_target or speed > self.SETTLED_SPEED:
                    return self._wait("ready_evidence_lost", "준비 자세와 물품 안정을 재확인합니다")
                self._report("ready", stamp)
                if action == "grasp":
                    self._transition("descend", now, stamp, self._grasp, .1)
                    self.report = None
            elif self.phase == "descend":
                if self._stable(at_target, stamp):
                    self._transition("grasp", now, stamp, self._grasp, 0.)
            elif self._stable(bilateral and at_target, stamp):
                self._holding = True
                self.payload_estimate = self.item_mass
                self._held_offset = tuple(position[i]-tool[i] for i in range(3))
                self._remember_local_grip(reading)
                if self.arm_geometry is not None and not self._prepare_motion_plan(receiver_observation, item,
                        approach_completed=True, tool=tool, tool_quaternion=reading['tool_quaternion']):
                    return self._result()
                self._event("grasp_confirmed", stamp)
                self._transition("grasped", now, stamp)
        elif self.phase == "grasped":
            # The coordinator's delayed observations may finish its bilateral
            # dwell before this controller. Later-stage intent authorizes
            # continued progress, but never bypasses our own grasp evidence.
            if action in ("lift_and_hold", "confirm_received"):
                self._transition("lift", now, stamp, self._lift, 0.)
        elif self.phase in ("lift", "received"):
            lifted = position[2] >= self._source[2]+.08
            confirmed = bilateral and lifted and at_target and speed <= self.SETTLED_SPEED
            if self.phase == "lift":
                if self._stable(confirmed, stamp, .30):
                    self._transition("received", now, stamp)
                    self._report("received", stamp)
            elif not confirmed:
                return self._wait("received_evidence_lost", "인수 후 파지·높이·안정을 재확인합니다")
            elif action == "place":
                self._place_cruise_z = max(self._lift[2], self._place_grasp_z+.12)
                if self.arm_geometry is not None and not self._prepare_motion_plan(receiver_observation, item,
                        already_held=True, tool=tool, tool_quaternion=reading['tool_quaternion']):
                    return self._result()
                self._transition("clearance", now, stamp,
                    self._planned_targets['clearance'] if self._planned_targets else (*tool[:2], self._place_cruise_z), self._carry_opening)
            else:
                self._report("received", stamp)
        elif self.phase == "clearance":
            if self._stable(at_target, stamp):
                self._transition("translate", now, stamp,
                    self._planned_targets['translate'] if self._planned_targets else (*self.destination[:2], self._place_cruise_z), self._carry_opening)
        elif self.phase == "translate":
            expected = (tuple(self.target[i]+self._expected_held_offset(reading)[i] for i in range(2))
                        if self._planned_targets else self.destination[:2])
            aligned = math.hypot(position[0]-expected[0], position[1]-expected[1]) <= .04
            if self._stable(at_target and aligned, stamp):
                if self.arm_geometry is not None and not self._prepare_motion_plan(receiver_observation, item,
                        already_held=True, tool=tool, tool_quaternion=reading['tool_quaternion']):
                    return self._result()
                self._transition("lower", now, stamp, self._lower_target(), self._carry_opening)
        else:
            try:
                upward, own_contact = self._support(reading, item)
            except ValueError as error:
                return self._wait(str(error), "최종 지지면의 접촉 힘 증거를 기다립니다")
            placed = (math.hypot(position[0]-self.destination[0], position[1]-self.destination[1]) <= .04
                      and abs(position[2]-self.destination[2]-self.item_size[2]/2) <= .025)
            supported = placed and upward >= self.SUPPORT_FRACTION*self.item_mass*9.81
            self.evidence.update(destination_support_force_N=upward, destination_supported=supported,
                                 minimum_support_force_N=self.SUPPORT_FRACTION*self.item_mass*9.81)
            if self.phase == "lower":
                transfer_ready, defer_lowering = self._transfer_load(reading, item, upward, stamp, dt)
                if defer_lowering:
                    return self._result()
                at_target = self.target is not None and _distance(tool, self.target) <= self.TOOL_TOLERANCE
                if self._stable(allow_release and transfer_ready and supported and at_target and speed <= self.SETTLED_SPEED, stamp, .25):
                    self.payload_estimate = 0.
                    self._transition("release", now, stamp, opening=.1)
                elif at_target and placed and not supported:
                    self._lower_offset = min(.012, self._lower_offset+.01*min(dt, .1))
                    self.target = self._lower_target()
            elif self.phase == "release":
                if self.manage_load_transfer and not supported:
                    return self._fail("release_support_lost", "개방 중 현재 지지가 소실되어 명령과 예약을 유지합니다", stamp)
                if released:
                    self._holding = False
                    self.payload_estimate = 0.
                settings = self._delivered_grip(reading)
                if not settings['valid']:
                    return self._wait('release_delivery_pending', '개방 전달 설정이 불완전하여 현재 설정을 보존합니다')
                delivered = self._release_delivered(reading)
                settings_ready = abs(settings['opening']-.1) <= 1e-9 and settings['payload'] <= 1e-9
                if self._release_settle_started is not None and not settings_ready:
                    return self._wait('release_delivery_pending', '현재 개방·무하중 보상 전달을 재확인하며 정지합니다')
                if delivered:
                    if self._release_settle_started is None:
                        self._release_settle_started = stamp
                        self._event('release_settings_observed', stamp)
                # Normal release keeps the atomic release_settle command
                # active. Its executor fixes measured joints only once and
                # ignores the old lower target; general hold is reserved for
                # safety vetoes and must not repeatedly recapture this pose.
                self.evidence['release_settle'] = dict(sampled_at=stamp,
                    requested_since=self._phase_started, delivered_settings_since=self._release_settle_started,
                    atomic_settle_requested=True, delivered_settings_confirmed=settings_ready,
                    atomic_settle_confirmed=delivered,
                    observed_control_mode=reading['feedback'].get('control_mode'),
                    observed_commanded_opening=settings['opening'], observed_payload_estimate_kg=settings['payload'],
                    observed_finger_positions_m=deepcopy(reading['feedback'].get('finger_positions_m')),
                    command_settings_source='delayed_controller_feedback',
                    physical_release_confirmed=False)
                if self._stable(delivered and released and not own_contact and supported
                                and speed <= self.SETTLED_SPEED, stamp, .40):
                    retract_target = (*self.destination[:2], self._place_grasp_z+.10)
                    if self._planned_targets:
                        from .arm_motion_plan import select_open_retract, ArmMotionPlanError
                        try:
                            retreat = select_open_retract(self.arm_geometry,
                                receiver_observation, tool, self._planned_targets['retract'], position,
                                self.item_size, noise=item['noise'], item_quaternion=item.get('quaternion'),
                                finger_positions=reading['feedback'].get('finger_positions_m'),
                                current_tool_quaternion=reading['tool_quaternion'],
                                current_joint_positions=reading['feedback'].get('arm_joint_positions_rad'),
                                start_joint_targets=reading['feedback'].get('arm_joint_targets_rad'))
                            self.evidence['retract_validation'] = retreat['evidence']
                            retract_target = retreat['target']
                        except ArmMotionPlanError as error:
                            self.evidence['retract_validation'] = error.evidence
                            return self._fail(error.code, '현재 놓인 물품과 열린 그리퍼의 후퇴 여유가 없습니다', stamp)
                    self._event("release_confirmed", stamp)
                    self.evidence['release_settle']['physical_release_confirmed'] = True
                    self._transition("retract", now, stamp, retract_target, .1)
                    self.hold = False
            elif self.phase == "retract":
                if self._stable(at_target and released and not own_contact and supported
                                and speed <= self.SETTLED_SPEED, stamp, .40):
                    self.status, self.phase, self.code, self.hold = "completed", "placed", "placement_verified", True
                    self.reason = "최종 지지·물품 안정·그리퍼 해제·후퇴를 관측했습니다"
                    self._report("placed", stamp)
                    self._event("placement_verified", stamp)
        return self._result()
