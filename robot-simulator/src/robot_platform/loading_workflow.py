"""Observation-only donor pick, carrier loading, and donor clearance.

The existing research-arm receive/place controller supplies its actuator targets.
This coordinator adds a fixed source, stationary peer, exact carrier support,
two observed releases, and retreat back to the source before reporting loaded.
It never reads simulator state or changes custody/reservations.
"""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import math

from .handoff_receiver import HandoffReceiver


def _vec(value, count=3):
    if isinstance(value, Mapping):
        value = [value.get(axis) for axis in "xyz"[:count]]
    try:
        values = tuple(float(component) for component in value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("finite coordinates required") from error
    if len(values) != count or not all(math.isfinite(component) for component in values):
        raise ValueError("finite coordinates required")
    return values


def _norm(value):
    return math.sqrt(sum(component*component for component in value))


def _distance(a, b):
    return _norm(tuple(x-y for x, y in zip(a, b)))


class LoadingWorkflow:
    VERSION = "observed-donor-carrier-loading-0.3"
    FRESH_AGE = 1.
    PEER_SKEW = .20
    OBSERVATION_TIMEOUT = 2.
    SUPPORT_FRACTION = .60
    CLEARANCE_DWELL = .50
    DONOR_LIFT_MIN = .08
    DONOR_SETTLED_SPEED = .035
    DONOR_TOOL_TOLERANCE = .02
    DONOR_DWELL = .30
    MAX_RELATIVE_SPEED = .06
    MAX_HEIGHT_ERROR = .025
    RETREAT_TOLERANCE = .02
    TRANSFER_HEIGHT_ERROR = .01
    TRANSFER_RELATIVE_SPEED = .035
    TRANSFER_CONTACT_DWELL = .15
    TRANSFER_RATE_FRACTION = .50  # at most half the item mass per observed second
    TRANSFER_REMAINDER_FRACTION = .02
    TRANSFER_RELEASE_DWELL = .25

    def __init__(self, task_id, donor_id, carrier_id, item_id, source, item_mass, item_size,
                 *, support_geom, support_size, support_top_offset, loading_offset=(0., 0.),
                 timeout=120., arm_geometry=None):
        if not all(isinstance(value, str) and value for value in
                   (task_id, donor_id, carrier_id, item_id, support_geom)):
            raise ValueError("nonempty task, robot, item, and support IDs required")
        if donor_id == carrier_id or not support_geom.startswith(carrier_id+"/"):
            raise ValueError("distinct participants and carrier-owned support required")
        self.task_id, self.donor_id, self.carrier_id, self.item_id = task_id, donor_id, carrier_id, item_id
        self.source, self.item_size = _vec(source), _vec(item_size)
        self.support_size, self.support_top_offset = _vec(support_size, 2), _vec(support_top_offset)
        self.loading_offset = _vec(loading_offset, 2)
        self.support_geom = support_geom
        self.arm_geometry = deepcopy(arm_geometry)
        self.item_mass, self.timeout = float(item_mass), float(timeout)
        if not all(math.isfinite(value) and value > 0 for value in
                   (self.item_mass, self.timeout, *self.item_size, *self.support_size)):
            raise ValueError("positive finite dimensions, mass and timeout required")
        self.radius = math.hypot(*self.item_size[:2])/2
        if any(abs(self.loading_offset[axis])+self.radius > self.support_size[axis]/2-.01
               for axis in (0, 1)):
            raise ValueError("item footprint must fit the carrier support with 1 cm margin")
        self.status, self.phase, self.code = "running", "await_source", "await_source"
        self.reason = "출발 물품과 정지한 운반차의 관측을 기다립니다"
        self.target, self.opening, self.payload_estimate, self.hold = None, .1, 0., True
        self._release_settle = False
        self.report, self.destination = None, None
        self.evidence = dict(source="observations", workflow_version=self.VERSION, events=[],
                             task_id=task_id, item_id=item_id, donor_id=donor_id, carrier_id=carrier_id,
                             donor_grip=None, loaded=None,
                             arm_workflow_version=HandoffReceiver.VERSION)
        self._arm = None
        self._started = self._last_now = self._last_fresh = None
        self._samples = None
        self._anchor = self._stable_since = self._retreat_started = None
        self._support_since = None
        self._grip_since = self._source_center = None
        self._donor_proposal = self._loading_proposal = None
        self._donor_verified = False
        self._transfer_payload = self._transfer_since = self._transfer_stamp = None
        self._transfer_ready_since = None
        self._park = (*self.source[:2], self.source[2]+self.item_size[2]/2+.20)

    def _result(self):
        return dict(task_id=self.task_id, donor_id=self.donor_id, carrier_id=self.carrier_id,
                    item_id=self.item_id, target=list(self.target) if self.target is not None else None,
                    opening=self.opening, payload_estimate=self.payload_estimate, hold=self.hold,
                    release_settle=bool(self._release_settle and self.status == "running"
                        and self.phase == "release" and not self.hold
                        and self.opening == .1 and self.payload_estimate == 0.),
                    status=self.status, phase=self.phase, code=self.code, reason=self.reason,
                    report=deepcopy(self.report), evidence=deepcopy(self.evidence),
                    resource_intent=dict(
                        retain=["task:"+self.task_id, "item:"+self.item_id,
                                "robot:"+self.donor_id, "robot:"+self.carrier_id],
                        release=[],
                        donor_custody=deepcopy(self._donor_proposal) if self.status == "running" and not self.hold else None,
                        loading_commit=deepcopy(self._loading_proposal) if self.status == "completed" else None))

    def _event(self, event, stamp, **extra):
        self.evidence["events"].append(dict(event=event, sampled_at=stamp, phase=self.phase, **extra))

    def _wait(self, code, *, reset=True):
        self.code, self.reason, self.hold, self.report = code, "새롭고 유효한 적재 관측을 기다립니다", True, None
        if reset:
            self._stable_since = None
            self._support_since = None
            self._grip_since = None
            self._transfer_since = None
            self._transfer_ready_since = None
            if self._arm is not None and self._arm.phase == "release":
                self._arm._stable_since = None
        self._donor_proposal = None
        return self._result()

    def _fail(self, code, stamp=None):
        self.status, self.code, self.reason, self.hold = "failed", code, "적재 검증에 실패하여 현재 파지와 예약을 유지합니다", True
        self.report, self._stable_since = None, None
        self._event("failed", stamp, code=code)
        return self._result()

    def cancel(self, now):
        self._time(now)
        if self.status == "running":
            self.status, self.code, self.hold, self.report = "cancelled", "cancelled", True, None
            self._event("cancelled", min(self._samples) if self._samples else None)
        return self._result()

    def _time(self, now):
        now = float(now)
        if not math.isfinite(now) or (self._last_now is not None and now < self._last_now):
            raise ValueError("loading time must be finite and monotonic")
        self._last_now = now
        if self._started is None:
            self._started = self._last_fresh = now
        return now

    def _read(self, now, obs, robot_id):
        if not isinstance(obs, Mapping) or obs.get("robot_id") != robot_id:
            raise ValueError("missing_or_wrong_robot")
        try:
            stamp, yaw = float(obs["sampled_at"]), float(obs["pose"]["yaw"])
            position, velocity, angular = _vec(obs["pose"]), _vec(obs["velocity"]), _vec(obs["angular_velocity"])
            upright = float(obs["upright"])
            sensors = obs["sensors"]
        except (KeyError, ValueError, TypeError, OverflowError) as error:
            raise ValueError("invalid_observation") from error
        if not all(math.isfinite(value) for value in (stamp, yaw, upright)) or stamp > now+1e-6:
            raise ValueError("future_or_invalid_observation")
        if now-stamp > self.FRESH_AGE:
            raise ValueError("stale_observation")
        if not isinstance(sensors, Mapping) or not isinstance(sensors.get("items"), list) or not isinstance(sensors.get("contacts"), list):
            raise ValueError("missing_item_or_contact_sensor")
        reports = sensors.get("manipulation")
        feedback = reports.get(self.item_id) if isinstance(reports, Mapping) else None
        if not isinstance(feedback, Mapping):
            raise ValueError("missing_release_sensor")
        fingers = feedback.get("finger_contacts")
        if not isinstance(fingers, (list, tuple)) or any(side not in ("left", "right") for side in fingers):
            raise ValueError("invalid_release_sensor")
        if not isinstance(feedback.get("bilateral_contact"), bool):
            raise ValueError("invalid_release_sensor")
        released = feedback["bilateral_contact"] is False and not fingers
        tool = None
        if robot_id == self.donor_id:
            try:
                tool = _vec(feedback["tool_position"])
            except (KeyError, ValueError) as error:
                raise ValueError("missing_tool_observation") from error
        return dict(stamp=stamp, position=position, yaw=yaw, velocity=velocity, angular=angular,
                    upright=upright, sensors=sensors, released=released,
                    tool=tool, bilateral=feedback["bilateral_contact"] is True and {"left", "right"} <= set(fingers),
                    feedback=feedback, fault=obs.get("fault", "none"), operator_hold=obs.get("operator_hold", False))

    def _item(self, reading):
        items = [row for row in reading["sensors"]["items"] if isinstance(row, Mapping) and row.get("id") == self.item_id]
        if len(items) != 1 or items[0].get("visible", True) is not True:
            raise ValueError("item_tracking_missing")
        try:
            noise = items[0].get('position_noise_std_m', 0.)
            if type(noise) not in (int, float) or not math.isfinite(noise) or noise < 0:
                raise ValueError('invalid item position noise')
            return dict(position=_vec(items[0]["position"]), velocity=_vec(items[0]["velocity"]), noise=noise)
        except (KeyError, ValueError) as error:
            raise ValueError("invalid_item_tracking") from error

    def _check_retreat_reach(self, observation, item, stamp):
        if self.arm_geometry is None:
            return True
        from .arm_kinematics import solve_observed, ArmKinematicsError
        margin = .015+3*item['noise']
        try:
            result = solve_observed(self.arm_geometry, observation, self._park,
                                    margin_m=margin, joint_margin_rad=.02)
        except ArmKinematicsError as error:
            self.evidence['retreat_reachability'] = dict(accepted=False, target=list(self._park),
                sampled_at=stamp, code=error.code, minimum_reach_margin_m=margin)
            self._fail('retreat_unreachable', stamp)
            return False
        self.evidence['retreat_reachability'] = dict(accepted=True, target=list(self._park),
            sampled_at=stamp, minimum_reach_margin_m=margin, solution=result)
        return True

    def _surface(self, carrier):
        c, s = math.cos(carrier["yaw"]), math.sin(carrier["yaw"])
        ox, oy, oz = self.support_top_offset
        return (carrier["position"][0]+c*ox-s*oy, carrier["position"][1]+s*ox+c*oy,
                carrier["position"][2]+oz)

    def _support(self, carrier, item):
        top = self._surface(carrier)
        c, s = math.cos(carrier["yaw"]), math.sin(carrier["yaw"])
        dx, dy, dz = tuple(item["position"][axis]-top[axis] for axis in range(3))
        local = (c*dx+s*dy, -s*dx+c*dy, dz)
        inside = all(abs(local[i])+self.radius <= self.support_size[i]/2-.01 for i in (0, 1))
        height_error = abs(dz-self.item_size[2]/2)
        height_good = height_error <= self.MAX_HEIGHT_ERROR
        upward = 0.
        donor_contact = False
        for row in carrier["sensors"]["contacts"]:
            if not isinstance(row, Mapping):
                raise ValueError("invalid_contact_sensor")
            a, b = row.get("geom_a"), row.get("geom_b")
            if self.item_id+"/shape" not in (a, b):
                continue
            other = a if b == self.item_id+"/shape" else b
            try:
                force, point = _vec(row["force_on_b_world"]), _vec(row["position"])
                magnitude = float(row["force"])
            except (KeyError, TypeError, ValueError, OverflowError) as error:
                raise ValueError("support_force_unavailable") from error
            if not isinstance(other, str) or not math.isfinite(magnitude) or magnitude < 0:
                raise ValueError("invalid_contact_sensor")
            if abs(_norm(force)-magnitude) > max(1e-6, magnitude*1e-6):
                raise ValueError("inconsistent_contact_force")
            donor_contact |= other.startswith(self.donor_id+"/") and magnitude > .1
            px, py = point[0]-top[0], point[1]-top[1]
            face = (abs(c*px+s*py) <= self.support_size[0]/2+.015
                    and abs(-s*px+c*py) <= self.support_size[1]/2+.015
                    and abs(point[2]-top[2]) <= .025)
            if other == self.support_geom and face:
                upward += max(0., force[2] if b == self.item_id+"/shape" else -force[2])
        r = tuple(item["position"][axis]-carrier["position"][axis] for axis in range(3))
        wx, wy, wz = carrier["angular"]
        rotation = (wy*r[2]-wz*r[1], wz*r[0]-wx*r[2], wx*r[1]-wy*r[0])
        relative = _norm(tuple(item["velocity"][i]-carrier["velocity"][i]-rotation[i] for i in range(3)))
        supported = inside and height_good and upward >= self.SUPPORT_FRACTION*self.item_mass*9.81 and relative <= self.MAX_RELATIVE_SPEED
        return dict(upward_support_force_N=upward, minimum_support_force_N=self.SUPPORT_FRACTION*self.item_mass*9.81,
                    supported=supported, item_local_position=list(local), item_relative_speed=relative,
                    footprint_inside=inside, height_good=height_good, height_error_m=height_error,
                    donor_contact=donor_contact)

    def _proof_identity(self, donor, carrier):
        stamp = min(donor["stamp"], carrier["stamp"])
        return dict(source="observations", workflow_version=self.VERSION, task_id=self.task_id,
                    item_id=self.item_id, donor_id=self.donor_id, carrier_id=self.carrier_id,
                    donor_sampled_at=donor["stamp"], carrier_sampled_at=carrier["stamp"],
                    sampled_at=stamp, confirmed_at=stamp)

    def _transfer_contact(self, donor, support):
        return bool(support and donor["bilateral"] and support["footprint_inside"]
                    and support["height_error_m"] <= self.TRANSFER_HEIGHT_ERROR
                    and support["item_relative_speed"] <= self.TRANSFER_RELATIVE_SPEED
                    and support["upward_support_force_N"] > .1)

    def _observed_transfer_command(self, donor):
        """Delayed controller settings, not a sensor measurement of load mass."""
        opening = donor["feedback"].get("commanded_opening")
        payload = donor["feedback"].get("payload_estimate_kg")
        numeric = all(isinstance(value, (int, float)) and not isinstance(value, bool)
                      and math.isfinite(value) for value in (opening, payload))
        valid = numeric and 0 <= opening <= .1 and payload >= 0
        return dict(valid=valid, opening=float(opening) if valid else None,
                    payload=float(payload) if valid else None)

    def _observed_transfer_ready(self, donor):
        command = self._observed_transfer_command(donor)
        return (command["valid"] and command["opening"] <= 1e-6
                and command["payload"] <= self.TRANSFER_REMAINDER_FRACTION*self.item_mass)

    def _release_allowed(self, donor, support, stamp):
        return (self._transfer_ready_since is not None and self._transfer_contact(donor, support)
                and self._observed_transfer_ready(donor)
                and support["supported"] and self._transfer_payload is not None
                and self._transfer_payload <= self.TRANSFER_REMAINDER_FRACTION*self.item_mass
                and max(0., self.item_mass-support["upward_support_force_N"]/9.81)
                    <= self.TRANSFER_REMAINDER_FRACTION*self.item_mass
                and stamp-self._transfer_ready_since >= self.TRANSFER_RELEASE_DWELL-1e-9)

    def _load_transfer(self, donor, carrier, support, stamp, arm):
        """Unload the held item only against current measured carrier support.

        This is an actuator feedforward command, not an estimate of changed
        item mass or a relaxation of the independent release predicates.
        The receiver keeps its own grasp, slip, target and support checks.
        """
        if self.phase not in ("lower", "release"):
            return None
        previous_stamp = self._transfer_stamp
        self._transfer_stamp = stamp
        # An open command is conditional on *current* carrier support. A
        # previously earned support dwell cannot authorize an unsupported
        # release after the handoff has started.
        if self.phase == "release" and (not support or not support["supported"]):
            # The runtime's hold preserves its delivered grip/compensation;
            # do not claim that a closed command was sent or that a lost grip
            # can be re-established merely by changing result fields.
            return self._fail("carrier_support_lost_during_release", stamp)
        if self.phase == "release":
            if donor["released"]:
                arm["payload_estimate"] = 0.
            elif self._transfer_payload is not None:
                arm["payload_estimate"] = self._transfer_payload
            return None
        if arm["hold"] or arm["status"] != "running":
            self._transfer_since = self._transfer_ready_since = None
            if self._transfer_payload is not None:
                arm["payload_estimate"] = self._transfer_payload
            return None
        valid = self._transfer_contact(donor, support)
        if not valid:
            self._transfer_since = None
            self._transfer_ready_since = None
            if self._transfer_payload is not None and self._transfer_payload < self.item_mass:
                self._transfer_payload = self.payload_estimate = self.item_mass
                self.opening = 0.
                self.evidence["load_transfer"] = dict(self._proof_identity(donor, carrier),
                    active=False, reason="current_support_lost", payload_estimate_kg=self.item_mass)
                # Valid current robot observations permit a normal, delayed
                # actuator command to the observed tool position. A hold=True
                # result would not actually deliver the restored feedforward.
                self.target, self.hold = list(donor["tool"]), False
                self._stable_since = self._support_since = self._grip_since = None
                self._donor_proposal = self.report = None
                self.code, self.reason = "load_transfer_support_pending", "현재 도구 위치에서 닫힌 파지와 전체 하중 보상을 복원합니다"
                return self._result()
            return None
        if self._transfer_since is None:
            self._transfer_since = stamp
        if self._transfer_payload is None:
            self._transfer_payload = self.item_mass
        desired = max(0., self.item_mass-support["upward_support_force_N"]/9.81)
        observed = self._observed_transfer_command(donor)
        dt = 0. if previous_stamp is None else min(.1, max(0., stamp-previous_stamp))
        if stamp-self._transfer_since >= self.TRANSFER_CONTACT_DWELL-1e-9:
            change = self.TRANSFER_RATE_FRACTION*self.item_mass*dt
            self._transfer_payload += max(-change, min(change, desired-self._transfer_payload))
        arm["payload_estimate"] = self._transfer_payload
        if (self._transfer_payload <= self.TRANSFER_REMAINDER_FRACTION*self.item_mass
                and desired <= self.TRANSFER_REMAINDER_FRACTION*self.item_mass and support["supported"]
                and self._observed_transfer_ready(donor)):
            if self._transfer_ready_since is None:
                self._transfer_ready_since = stamp
        else:
            self._transfer_ready_since = None
        self.evidence["load_transfer"] = dict(self._proof_identity(donor, carrier),
            active=True, support_geom=self.support_geom, upward_support_force_N=support["upward_support_force_N"],
            height_error_m=support["height_error_m"], item_relative_speed=support["item_relative_speed"],
            footprint_inside=support["footprint_inside"], bilateral_contact=donor["bilateral"],
            contact_since=self._transfer_since, contact_duration_s=stamp-self._transfer_since,
            minimum_contact_duration_s=self.TRANSFER_CONTACT_DWELL,
            desired_payload_estimate_kg=desired, payload_estimate_kg=self._transfer_payload,
            observed_command_feedback_valid=observed["valid"],
            observed_commanded_opening=observed["opening"], observed_payload_estimate_kg=observed["payload"],
            observed_command_settings_source="donor_delayed_controller_feedback",
            maximum_rate_kg_s=self.TRANSFER_RATE_FRACTION*self.item_mass,
            command_sample_interval_s=dt, release_ready_since=self._transfer_ready_since,
            maximum_release_payload_kg=self.TRANSFER_REMAINDER_FRACTION*self.item_mass,
            minimum_release_dwell_s=self.TRANSFER_RELEASE_DWELL)
        return None

    def _proposal(self, proof, owner):
        return dict(task_id=self.task_id, item_id=self.item_id, donor_id=self.donor_id,
                    carrier_id=self.carrier_id, from_robot=None if owner == self.donor_id else self.donor_id,
                    to_robot=owner, donor_sampled_at=proof["donor_sampled_at"],
                    carrier_sampled_at=proof["carrier_sampled_at"], confirmed_at=proof["confirmed_at"])

    def _grip_evidence(self, donor, carrier, item):
        """Confirm initial custody only after fresh paired lift and stable grip."""
        stamp = min(donor["stamp"], carrier["stamp"])
        lift = item["position"][2]-self._source_center[2]
        speed = _norm(item["velocity"])
        tool_error = _distance(donor["tool"], self.target) if self.target is not None else math.inf
        valid = (self.phase in ("lift", "received", "clearance", "translate", "lower")
                 and donor["bilateral"] and lift >= self.DONOR_LIFT_MIN
                 and speed <= self.DONOR_SETTLED_SPEED and tool_error <= self.DONOR_TOOL_TOLERANCE)
        if not valid:
            self._grip_since = None
            return
        if self._grip_since is None:
            self._grip_since = stamp
        if stamp-self._grip_since < self.DONOR_DWELL-1e-9:
            return
        proof = dict(self._proof_identity(donor, carrier), robot_id=self.donor_id,
                     bilateral_contact=True, finger_contacts=sorted(donor["feedback"]["finger_contacts"]),
                     lifted=True, lift_height_m=lift, minimum_lift_height_m=self.DONOR_LIFT_MIN,
                     item_speed_m_s=speed, maximum_item_speed_m_s=self.DONOR_SETTLED_SPEED,
                     tool_error_m=tool_error, maximum_tool_error_m=self.DONOR_TOOL_TOLERANCE,
                     stable_since=self._grip_since, stable_duration_s=stamp-self._grip_since,
                     minimum_stable_duration_s=self.DONOR_DWELL,
                     source_item_position=list(self._source_center), item_position=list(item["position"]))
        self.evidence["donor_grip"] = proof
        self._donor_proposal = self._proposal(proof, self.donor_id)
        if not self._donor_verified:
            self._donor_verified = True
            self._event("donor_grip_verified", stamp)

    def update(self, now, donor_observation, carrier_observation):
        now = self._time(now)
        if self.status != "running":
            return self._result()
        if now-self._started >= self.timeout:
            return self._fail("timeout")
        if self.item_mass > HandoffReceiver.MAX_PAYLOAD:
            return self._fail("overload")
        try:
            donor = self._read(now, donor_observation, self.donor_id)
            carrier = self._read(now, carrier_observation, self.carrier_id)
            stamps = (donor["stamp"], carrier["stamp"])
            if abs(stamps[0]-stamps[1]) > self.PEER_SKEW:
                raise ValueError("peer_time_skew")
            if self._samples and any(stamps[i] < self._samples[i] for i in (0, 1)):
                raise ValueError("reordered_observation")
        except ValueError as error:
            if now-self._last_fresh >= self.OBSERVATION_TIMEOUT:
                return self._fail("observation_timeout")
            return self._wait(str(error))
        stamp = min(stamps)
        for reading in (donor, carrier):
            if reading["fault"] not in (None, False, "none") or reading["sensors"].get("controller_error"):
                return self._fail("participant_fault", stamp)
            if reading["upright"] < .98:
                return self._fail("unstable_base", stamp)
            if reading["operator_hold"]:
                return self._wait("operator_hold")
            if _norm(reading["velocity"]) > .04 or _norm(reading["angular"]) > .08:
                return self._wait("participant_moving")
            for row in reading["sensors"]["contacts"]:
                if not isinstance(row, Mapping):
                    return self._wait("invalid_contact_sensor")
                pair = (row.get("geom_a"), row.get("geom_b"))
                robot_pair = (any(isinstance(g, str) and g.startswith(self.donor_id+"/") for g in pair)
                              and any(isinstance(g, str) and g.startswith(self.carrier_id+"/") for g in pair))
                if robot_pair:
                    try:
                        force = float(row["force"])
                    except (KeyError, ValueError, TypeError, OverflowError):
                        return self._wait("invalid_contact_sensor")
                    if not math.isfinite(force) or force < 0:
                        return self._wait("invalid_contact_sensor")
                    if force > .1:
                        return self._fail("participant_collision", stamp)
        if not carrier["released"]:
            return self._fail("carrier_holding", stamp)
        # Safety checks also apply to a newer peer paired with an unchanged
        # donor sample; a partial sensor update is not permission to move it.
        if self._anchor is not None:
            yaw_error = (carrier["yaw"]-self._anchor[1]+math.pi) % (2*math.pi)-math.pi
            if _distance(carrier["position"], self._anchor[0]) > .025 or abs(yaw_error) > .04:
                return self._fail("carrier_moved", stamp)
        if self._samples and any(stamps[i] == self._samples[i] for i in (0, 1)):
            if now-self._last_fresh >= self.OBSERVATION_TIMEOUT:
                return self._fail("observation_timeout", stamp)
            if ((self.phase == "lower" or self.payload_estimate > 0
                    and self.phase not in ("release", "retract", "retreat")) and not donor["bilateral"]):
                return self._wait("contact_loss_pending")
            if (self.phase == "lower" and self._transfer_ready_since is not None
                    and stamps[0] > self._samples[0] and not self._observed_transfer_ready(donor)):
                return self._wait("load_transfer_command_pending")
            if self.phase in ("lower", "release") and stamps[1] > self._samples[1]:
                # A partial pair cannot earn unloading/opening progress, but
                # a newly observed support loss must veto the old command.
                try:
                    current_item = self._item(carrier)
                    current_support = self._support(carrier, current_item)
                    if _distance(current_item["position"], self._item(donor)["position"]) > .04:
                        raise ValueError("peer_item_disagreement")
                except ValueError as error:
                    return self._wait(str(error))
                if self.phase == "release" and not current_support["supported"]:
                    return self._fail("carrier_support_lost_during_release", stamp)
                if (self.phase == "lower" and self._transfer_payload is not None
                        and self._transfer_payload < self.item_mass
                        and not self._transfer_contact(donor, current_support)):
                    return self._wait("load_transfer_support_pending")
                if (self.phase == "lower" and self._transfer_ready_since is not None
                        and max(0., self.item_mass-current_support["upward_support_force_N"]/9.81)
                            > self.TRANSFER_REMAINDER_FRACTION*self.item_mass):
                    return self._wait("load_transfer_support_pending")
            if self.phase == "release":
                # A partial pair cannot advance the arm, but current actor
                # feedback can invalidate its continuous release proof.
                veto = self._arm._duplicate_release_veto(donor)
                if veto is not None:
                    self.evidence["arm"] = veto["evidence"]
                    if veto["status"] == "failed":
                        return self._fail(veto["code"], stamp)
                    return self._wait(veto["code"])
            # A fast control loop may re-use the exact 20 Hz sensor pair.
            # Keep its last safe command; only a fresh pair advances evidence.
            self.code = "awaiting_fresh_observations"
            return self._result()
        if self._samples and max(stamps[i]-self._samples[i] for i in (0, 1)) > .5:
            self._stable_since = None
            self._support_since = None
            self._grip_since = None
            self._transfer_since = None
            self._transfer_ready_since = None
        self._samples, self._last_fresh = stamps, now
        self._donor_proposal = None
        try:
            donor_item = self._item(donor)
            # Carrier tracking is mandatory once the load enters its workspace.
            carrier_item = self._item(carrier) if self.phase in ("lower", "release", "retract", "retreat", "verify_loaded") else None
            support = self._support(carrier, carrier_item) if carrier_item is not None else None
            if carrier_item and _distance(carrier_item["position"], donor_item["position"]) > .04:
                raise ValueError("peer_item_disagreement")
            if support:
                for row in donor["sensors"]["contacts"]:
                    if not isinstance(row, Mapping):
                        raise ValueError("invalid_contact_sensor")
                    pair = (row.get("geom_a"), row.get("geom_b"))
                    if self.item_id+"/shape" in pair and any(isinstance(g, str) and g.startswith(self.donor_id+"/") for g in pair):
                        try:
                            magnitude = float(row.get("force", math.nan))
                        except (TypeError, ValueError, OverflowError) as error:
                            raise ValueError("invalid_contact_sensor") from error
                        if not math.isfinite(magnitude) or magnitude < 0:
                            raise ValueError("invalid_contact_sensor")
                        support["donor_contact"] |= magnitude > .1
        except ValueError as error:
            return self._wait(str(error))
        if self._arm is None:
            expected = (*self.source[:2], self.source[2]+self.item_size[2]/2)
            if _distance(donor_item["position"], expected) > .05:
                return self._fail("source_mismatch", stamp)
            if not carrier["released"]:
                return self._fail("carrier_holding", stamp)
            top = self._surface(carrier)
            c, s = math.cos(carrier["yaw"]), math.sin(carrier["yaw"])
            ox, oy = self.loading_offset
            self.destination = (top[0]+c*ox-s*oy, top[1]+s*ox+c*oy, top[2])
            self._park = (*self.source[:2], max(self._park[2], self.destination[2]+self.item_size[2]/2+.20))
            if not self._check_retreat_reach(donor_observation, donor_item, stamp):
                return self._result()
            self._anchor = (carrier["position"], carrier["yaw"])
            self._source_center = donor_item["position"]
            self._arm = HandoffReceiver(self.task_id, self.carrier_id, self.donor_id, self.item_id,
                                        self.item_mass, self.item_size, self.destination, timeout=self.timeout,
                                        manage_load_transfer=False, arm_geometry=self.arm_geometry)
            self._event("source_confirmed", stamp)
        self.evidence.update(donor_sampled_at=stamps[0], carrier_sampled_at=stamps[1],
                             item_position=list(donor_item["position"]), donor_released=donor["released"],
                             carrier_released=carrier["released"], destination=list(self.destination))
        if support:
            self.evidence.update(support)
        self._grip_evidence(donor, carrier, donor_item)
        if support and support["supported"]:
            if self._support_since is None:
                self._support_since = stamp
        else:
            self._support_since = None
        if self.phase in ("retreat", "verify_loaded"):
            if not self._check_retreat_reach(donor_observation, donor_item, stamp):
                return self._result()
            self.hold, self.target = False, self._park
            try:
                tool = _vec(donor["feedback"]["tool_position"])
            except (KeyError, ValueError):
                return self._wait("missing_tool_observation")
            retreat_error = _distance(tool, self._park)
            verified = (self._donor_verified and support["supported"] and not support["donor_contact"] and donor["released"]
                        and carrier["released"] and retreat_error <= self.RETREAT_TOLERANCE)
            if not verified:
                self._stable_since = None
            elif self._stable_since is None:
                self._stable_since = stamp
            elif stamp-self._stable_since >= self.CLEARANCE_DWELL-1e-9:
                self.status, self.phase, self.code, self.hold = "completed", "loaded", "loading_verified", True
                self.report = dict(task_id=self.task_id, donor_id=self.donor_id, carrier_id=self.carrier_id,
                                   item_id=self.item_id, state="loaded", sampled_at=stamp)
                proof = dict(self._proof_identity(donor, carrier), **support,
                    support_geom=self.support_geom, item_mass_kg=self.item_mass,
                    support_size=list(self.support_size), item_size=list(self.item_size),
                    maximum_relative_speed=self.MAX_RELATIVE_SPEED, maximum_height_error_m=self.MAX_HEIGHT_ERROR,
                    donor_released=donor["released"], carrier_released=carrier["released"],
                    donor_bilateral_contact=donor["feedback"]["bilateral_contact"],
                    carrier_bilateral_contact=carrier["feedback"]["bilateral_contact"],
                    donor_finger_contacts=list(donor["feedback"]["finger_contacts"]),
                    carrier_finger_contacts=list(carrier["feedback"]["finger_contacts"]),
                    retreat_target=list(self._park), donor_tool_position=list(tool), retreat_error_m=retreat_error,
                    maximum_retreat_error_m=self.RETREAT_TOLERANCE,
                    stable_since=self._stable_since, stable_duration_s=stamp-self._stable_since,
                    minimum_stable_duration_s=self.CLEARANCE_DWELL)
                self.evidence["loaded"] = proof
                self._loading_proposal = self._proposal(proof, self.carrier_id)
                self._event("loading_verified", stamp)
            if self.status == "running" and now-self._retreat_started >= 18.:
                return self._fail("retreat_timeout", stamp)
            return self._result()
        phase = self._arm.phase
        action = ("prepare" if phase in ("await_prepare", "approach") else
                  "grasp" if phase in ("ready", "descend", "grasp") else
                  "lift_and_hold" if phase in ("grasped", "lift") else
                  "confirm_received" if phase == "received" and not self._donor_verified else "place")
        arm = self._arm.update(now, donor_observation, action,
                              allow_release=phase != "lower" or self._release_allowed(donor, support, stamp))
        self.evidence["arm"] = arm["evidence"]
        # Do not execute a release authorized by a different support surface.
        if phase == "lower" and arm["phase"] == "release" and (not support or not support["supported"]
                or self._support_since is None or stamp-self._support_since < .25-1e-9):
            return self._fail("carrier_support_not_verified", stamp)
        stopped = self._load_transfer(donor, carrier, support, stamp, arm)
        if stopped is not None:
            return stopped
        self.target, self.opening, self.payload_estimate, self.hold = arm["target"], arm["opening"], arm["payload_estimate"], arm["hold"]
        self._release_settle = arm.get("release_settle") is True
        if self.target is None:
            self.hold = True
        if arm["status"] == "failed":
            return self._fail(arm["code"], stamp)
        self.phase, self.code, self.reason = arm["phase"], arm["code"], arm["reason"]
        if arm["status"] == "completed":
            if not support or not support["supported"] or not donor["released"] or not carrier["released"]:
                return self._fail("release_not_verified", stamp)
            self.phase, self.code = "retreat", "retreat"
            self.target, self.hold, self._retreat_started = self._park, False, now
            self._event("carrier_load_released", stamp)
        return self._result()
