"""Observed recovery placement with retained grip and explicit custody evidence.

No simulator, ownership table, reservation, attachment, or robot pose is owned
here. The caller retains resources and explicitly authorizes this new attempt.
"""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import math

from .handoff_receiver import HandoffReceiver, _vec, _distance


class RecoveryPlacement:
    VERSION = "observed-recovery-placement-0.1"
    FRESH_AGE = 1.
    MAX_PEER_SKEW = .20
    GRASP_DWELL = .30
    MIN_LIFT = .08
    SETTLED_SPEED = .035
    TOOL_TOLERANCE = .02
    SUPPORT_FRACTION = .60
    PLACEMENT_DWELL = .40

    def __init__(self, task_id, actor_id, carrier_id, item_id, item_mass, item_size,
                 destination, *, mode="held", timeout=120., grip_opening=0.,
                 payload_estimate=None, support_geometry=None, arm_geometry=None):
        if mode not in ("held", "pickup"):
            raise ValueError("recovery mode must be held or pickup")
        self._arm = HandoffReceiver(task_id, carrier_id, actor_id, item_id, item_mass,
                                    item_size, destination, timeout=timeout, arm_geometry=arm_geometry)
        self.task_id, self.actor_id, self.carrier_id, self.item_id = task_id, actor_id, carrier_id, item_id
        self.item_mass, self.item_size, self.destination = self._arm.item_mass, self._arm.item_size, self._arm.destination
        self.mode, self.timeout = mode, float(timeout)
        self._opening = float(grip_opening)
        self._payload = self.item_mass if payload_estimate is None else float(payload_estimate)
        if not math.isfinite(self._opening) or not 0 <= self._opening <= .1 or not math.isfinite(self._payload) or self._payload < 0:
            raise ValueError("valid retained opening and payload estimate required")
        self.geometry = deepcopy(support_geometry) if mode == "pickup" else None
        if mode == "pickup":
            if not isinstance(self.geometry, Mapping):
                raise ValueError("pickup requires static carrier support_geometry")
            if not isinstance(self.geometry.get("support_geom"), str) or not self.geometry["support_geom"].startswith(carrier_id+"/"):
                raise ValueError("pickup support must belong to carrier")
            try:
                size = tuple(float(v) for v in self.geometry["support_size"])
                offset = _vec(self.geometry["support_top_offset"])
                maximum = float(self.geometry.get("max_payload", 3.))
            except (KeyError, TypeError, ValueError, OverflowError) as error:
                raise ValueError("finite carrier support geometry required") from error
            if len(size) != 2 or not all(math.isfinite(v) and v > 0 for v in (*size, maximum)):
                raise ValueError("positive carrier support geometry required")
            self.geometry = dict(support_geom=self.geometry["support_geom"], support_size=size,
                                 support_top_offset=offset, max_payload=maximum)
        self.status, self.phase, self.code = "running", "verify_held" if mode == "held" else "await_pickup", "recovery_started"
        self.reason = "새 관측으로 복구 물품 상태를 확인합니다"
        self.target, self.hold = None, True
        self._release_settle = False
        self.opening = self._opening if mode == "held" else .1
        self.payload_estimate = self._payload if mode == "held" else 0.
        self.report = None
        self.evidence = dict(source="observations", workflow_version=self.VERSION, task_id=task_id,
                             actor_id=actor_id, carrier_id=carrier_id, item_id=item_id, mode=mode,
                             grasp_verified=None, placed=None, events=[])
        self._proposal = None
        self._started = self._last_now = self._last_fresh = self._last_samples = None
        self._grasp_since = self._placed_since = self._missing_item = None
        self._tool_anchor = self._item_anchor = self._source_item = self._carrier_anchor = None
        self._grasp_verified = False

    def _result(self):
        return dict(task_id=self.task_id, actor_id=self.actor_id, receiver_id=self.actor_id,
                    carrier_id=self.carrier_id, item_id=self.item_id, mode=self.mode,
                    status=self.status, phase=self.phase, code=self.code, reason=self.reason,
                    target=list(self.target) if self.target is not None else None, opening=self.opening,
                    payload_estimate=self.payload_estimate, hold=self.hold, report=deepcopy(self.report),
                    release_settle=bool(self._release_settle and self.status == "running"
                        and self.phase == "release" and not self.hold
                        and self.opening == .1 and self.payload_estimate == 0.),
                    evidence=deepcopy(self.evidence), resource_intent=dict(
                        retain=["task:"+self.task_id, "item:"+self.item_id, "robot:"+self.actor_id, "robot:"+self.carrier_id],
                        release=[], recovery_custody=deepcopy(self._proposal) if self.status == "running" else None))

    def _event(self, event, stamp, **extra):
        self.evidence["events"].append(dict(event=event, sampled_at=stamp, phase=self.phase, **extra))

    def _wait(self, code, *, reset=True):
        self.code, self.hold, self._proposal = code, True, None
        if reset:
            self._grasp_since = self._placed_since = None
            if self._arm.phase == "release":
                self._arm._stable_since = None
        return self._result()

    def _fail(self, code, stamp=None):
        self.status, self.code, self.hold, self._proposal = "failed", code, True, None
        self.reason = "복구 조건을 확인하지 못해 현재 파지와 예약을 유지합니다"
        self._event("failed", stamp, code=code)
        return self._result()

    def cancel(self, now):
        self._time(now)
        if self.status == "running":
            self.status, self.code, self.hold, self._proposal = "cancelled", "cancelled", True, None
            self._event("cancelled", min(self._last_samples) if self._last_samples else None)
        return self._result()

    def _time(self, now):
        now = float(now)
        if not math.isfinite(now) or (self._last_now is not None and now < self._last_now):
            raise ValueError("recovery time must be finite and monotonic")
        self._last_now = now
        if self._started is None:
            self._started = self._last_fresh = now
        return now

    def _carrier(self, now, obs):
        if not isinstance(obs, Mapping) or obs.get("robot_id") != self.carrier_id:
            raise ValueError("missing_or_wrong_carrier")
        try:
            stamp, upright = float(obs["sampled_at"]), float(obs["upright"])
            position, velocity, angular = _vec(obs["pose"]), _vec(obs["velocity"]), _vec(obs["angular_velocity"])
            yaw = float(obs["pose"]["yaw"])
            sensors = obs["sensors"]
        except (KeyError, TypeError, ValueError, OverflowError) as error:
            raise ValueError("invalid_carrier_observation") from error
        if not all(math.isfinite(v) for v in (stamp, upright, yaw)) or stamp > now+1e-6 or now-stamp > self.FRESH_AGE:
            raise ValueError("stale_or_future_carrier")
        if not isinstance(sensors, Mapping) or not isinstance(sensors.get("contacts"), list):
            raise ValueError("missing_carrier_contacts")
        feedback = sensors.get("manipulation", {}).get(self.item_id) if isinstance(sensors.get("manipulation"), Mapping) else None
        if not isinstance(feedback, Mapping) or feedback.get("bilateral_contact") is not False or feedback.get("finger_contacts") != []:
            raise ValueError("carrier_release_unconfirmed")
        return dict(stamp=stamp, position=position, yaw=yaw, velocity=velocity, angular=angular,
                    upright=upright, sensors=sensors, fault=obs.get("fault", "none"), operator_hold=obs.get("operator_hold", False))

    def _wrenches(self, rows):
        if not isinstance(rows, list):
            raise ValueError("missing_item_contact_sensor")
        result = []
        for row in rows:
            if not isinstance(row, Mapping):
                raise ValueError("invalid_contact_sensor")
            pair = (row.get("geom_a"), row.get("geom_b"))
            if self.item_id+"/shape" not in pair:
                continue
            if not all(isinstance(value, str) for value in pair):
                raise ValueError("invalid_contact_sensor")
            try:
                if isinstance(row["force"], bool) or not isinstance(row["force"], (int, float)):
                    raise ValueError("numeric contact force required")
                magnitude = float(row["force"])
                vector = _vec(row["force_on_b_world"])
                _vec(row["position"])
            except (KeyError, TypeError, ValueError, OverflowError) as error:
                raise ValueError("invalid_contact_wrench") from error
            if not math.isfinite(magnitude) or magnitude < 0:
                raise ValueError("invalid_contact_wrench")
            if magnitude > .1 and _distance(vector) <= .1:
                raise ValueError("invalid_contact_wrench")
            result.append(deepcopy(row))
        return result

    def _contact_state(self, actor, carrier, item):
        # The visible-item sensor is required: actor-only contacts cannot prove
        # absence of an external floor/table/carrier contact.
        item_rows = self._wrenches(item["support_contacts"])
        item_rows += self._wrenches(actor["sensors"].get("contacts"))
        carrier_rows = self._wrenches(carrier["sensors"]["contacts"])
        fingers, external = set(), False
        for row in item_rows:
            if row["force"] <= .1:
                continue
            pair = (row["geom_a"], row["geom_b"])
            other = pair[0] if pair[1] == self.item_id+"/shape" else pair[1]
            for side in ("left", "right"):
                if other == f"{self.actor_id}/finger-shape-{side}":
                    fingers.add(side)
            external |= not other.startswith(self.actor_id+"/")
        carrier_contact = any(row["force"] > .1 and any(g.startswith(self.carrier_id+"/") for g in (row["geom_a"], row["geom_b"])) for row in carrier_rows)
        return dict(item_contact_wrenches=item_rows, carrier_contact_wrenches=carrier_rows,
                    raw_bilateral={"left", "right"} <= fingers, external_contact=external,
                    carrier_contact=carrier_contact, source_separated=not external and not carrier_contact)

    def _source_supported(self, carrier, item, contacts):
        geom, size, offset = (self.geometry[key] for key in ("support_geom", "support_size", "support_top_offset"))
        c, s = math.cos(carrier["yaw"]), math.sin(carrier["yaw"])
        top = (carrier["position"][0]+c*offset[0]-s*offset[1], carrier["position"][1]+s*offset[0]+c*offset[1], carrier["position"][2]+offset[2])
        dx, dy = item["position"][0]-top[0], item["position"][1]-top[1]
        local = (c*dx+s*dy, -s*dx+c*dy)
        radius = math.hypot(*self.item_size[:2])/2
        inside = all(abs(local[i])+radius <= size[i]/2-.01 for i in (0, 1))
        upward = 0.
        for row in contacts["carrier_contact_wrenches"]:
            if geom not in (row["geom_a"], row["geom_b"]):
                continue
            point, force = _vec(row["position"]), _vec(row["force_on_b_world"])
            px, py = point[0]-top[0], point[1]-top[1]
            if abs(point[2]-top[2]) <= .04 and abs(c*px+s*py) <= size[0]/2+.015 and abs(-s*px+c*py) <= size[1]/2+.015:
                upward += max(0., force[2] if row["geom_b"] == self.item_id+"/shape" else -force[2])
        supported = inside and abs(item["position"][2]-top[2]-self.item_size[2]/2) <= .035 and upward >= self.SUPPORT_FRACTION*self.item_mass*9.81
        return supported, upward

    def _identity(self, actor, carrier):
        stamp = min(actor["stamp"], carrier["stamp"])
        return dict(source="observations", workflow_version=self.VERSION, task_id=self.task_id,
                    actor_id=self.actor_id, carrier_id=self.carrier_id, item_id=self.item_id, mode=self.mode,
                    actor_sampled_at=actor["stamp"], carrier_sampled_at=carrier["stamp"], sampled_at=stamp, confirmed_at=stamp)

    def update(self, now, actor_observation, carrier_observation):
        now = self._time(now)
        if self.status != "running":
            return self._result()
        if now-self._started >= self.timeout:
            return self._fail("timeout")
        if self.item_mass > min(HandoffReceiver.MAX_PAYLOAD, self.geometry["max_payload"] if self.geometry else math.inf):
            return self._fail("overload")
        try:
            actor = self._arm._read(now, actor_observation)
            carrier = self._carrier(now, carrier_observation)
            stamps = (actor["stamp"], carrier["stamp"])
            if abs(stamps[0]-stamps[1]) > self.MAX_PEER_SKEW:
                raise ValueError("peer_time_skew")
            if self._last_samples and any(stamps[i] < self._last_samples[i] for i in (0, 1)):
                raise ValueError("reordered_observation")
        except ValueError as error:
            if now-self._last_fresh >= 2.:
                return self._fail("observation_timeout")
            return self._wait(str(error))
        stamp = min(stamps)
        for reading in (actor, carrier):
            if reading["fault"] not in (None, False, "none") or reading["sensors"].get("controller_error"):
                return self._fail("participant_fault", stamp)
            if reading["upright"] < .98:
                return self._fail("unstable_base", stamp)
            if reading["operator_hold"] or _distance(reading["velocity"]) > .04 or _distance(reading["angular"]) > .08:
                return self._wait("participant_not_stationary")
            rows = reading["sensors"].get("contacts")
            if not isinstance(rows, list):
                return self._wait("missing_contact_sensor")
            for row in rows:
                if not isinstance(row, Mapping):
                    return self._wait("invalid_contact_sensor")
                pair = (row.get("geom_a"), row.get("geom_b"))
                if (any(isinstance(g, str) and g.startswith(self.actor_id+"/") for g in pair)
                        and any(isinstance(g, str) and g.startswith(self.carrier_id+"/") for g in pair)):
                    try:
                        force = float(row["force"])
                    except (KeyError, TypeError, ValueError, OverflowError):
                        return self._wait("invalid_contact_sensor")
                    if not math.isfinite(force) or force < 0:
                        return self._wait("invalid_contact_sensor")
                    if force > .1:
                        return self._fail("participant_collision", stamp)
        if actor["wrong_contact"]:
            return self._fail("wrong_item_contact", stamp)
        if self._carrier_anchor and (_distance(carrier["position"], self._carrier_anchor[0]) > .025
                or abs((carrier["yaw"]-self._carrier_anchor[1]+math.pi) % (2*math.pi)-math.pi) > .04):
            return self._fail("carrier_moved", stamp)
        if self._last_samples and any(stamps[i] == self._last_samples[i] for i in (0, 1)):
            if self._grasp_verified and self.phase not in ("release", "retract", "verify_placement") and not actor["bilateral"]:
                return self._wait("contact_loss_pending")
            if self.phase == "release":
                # Only veto the existing release here; earning dwell or
                # advancing a phase still requires a fresh observation pair.
                veto = self._arm._duplicate_release_veto(actor)
                if veto is not None:
                    self.evidence["arm"] = veto["evidence"]
                    if veto["status"] == "failed":
                        return self._fail(veto["code"], stamp)
                    return self._wait(veto["code"])
            self.code = "awaiting_fresh_observations"
            return self._result()
        if self._last_samples and max(stamps[i]-self._last_samples[i] for i in (0, 1)) > .5:
            self._grasp_since = self._placed_since = None
        self._last_samples, self._last_fresh, self._proposal = stamps, now, None
        item = self._arm._item(actor)
        if item is None:
            if self._missing_item is None:
                self._missing_item = now
            if now-self._missing_item >= 1.:
                return self._fail("item_tracking_lost", stamp)
            return self._wait("item_tracking_pending")
        self._missing_item = None
        try:
            contacts = self._contact_state(actor, carrier, item)
        except ValueError as error:
            return self._wait(str(error))
        if (self._grasp_verified and self.phase not in ("lower", "release", "retract", "verify_placement")
                and (contacts["external_contact"] or contacts["carrier_contact"])):
            return self._fail("unexpected_external_contact", stamp)
        self.evidence.update(actor_sampled_at=stamps[0], carrier_sampled_at=stamps[1],
                             item_position=list(item["position"]), tool_position=list(actor["tool"]))
        if self._tool_anchor is None:
            if self.mode == "held":
                self._source_item = item["position"]
            self._tool_anchor, self._item_anchor = actor["tool"], item["position"]
            self._carrier_anchor = (carrier["position"], carrier["yaw"])
        speed = _distance(item["velocity"])
        tool_target = self._tool_anchor if self.mode == "held" and not self._grasp_verified else self._arm.target
        tool_error = _distance(actor["tool"], tool_target) if tool_target is not None else math.inf
        lift = item["position"][2]-(self._source_item or item["position"])[2]
        lifted = self.mode == "held" or lift >= self.MIN_LIFT
        grasp_ok = (actor["bilateral"] and contacts["raw_bilateral"] and contacts["source_separated"]
                    and speed <= self.SETTLED_SPEED and tool_error <= self.TOOL_TOLERANCE and lifted)
        if self.mode == "held" and not self._grasp_verified:
            grasp_ok &= _distance(item["position"], self._item_anchor) <= self.TOOL_TOLERANCE
            if not grasp_ok:
                self._tool_anchor, self._item_anchor = actor["tool"], item["position"]
        if not grasp_ok:
            self._grasp_since = None
        elif self._grasp_since is None:
            self._grasp_since = stamp
        if grasp_ok and stamp-self._grasp_since >= self.GRASP_DWELL-1e-9:
            proof = dict(self._identity(actor, carrier), robot_id=self.actor_id, bilateral_contact=True,
                finger_contacts=["left", "right"], already_held=self.mode == "held", **contacts,
                item_position=list(item["position"]), source_item_position=list(self._source_item),
                item_speed_m_s=speed, maximum_item_speed_m_s=self.SETTLED_SPEED,
                tool_position=list(actor["tool"]), tool_target=list(tool_target), tool_anchor=list(tool_target),
                tool_error_m=tool_error, maximum_tool_error_m=self.TOOL_TOLERANCE,
                stable_since=self._grasp_since, stable_duration_s=stamp-self._grasp_since,
                minimum_stable_duration_s=self.GRASP_DWELL)
            if self.mode == "pickup":
                proof.update(lifted=True, lift_height_m=lift, minimum_lift_height_m=self.MIN_LIFT)
            self.evidence["grasp_verified"] = proof
            self._proposal = dict(task_id=self.task_id, item_id=self.item_id, actor_id=self.actor_id,
                carrier_id=self.carrier_id, to_robot=self.actor_id, actor_sampled_at=stamps[0], carrier_sampled_at=stamps[1], confirmed_at=stamp)
            if not self._grasp_verified:
                self._grasp_verified = True
                self._event("grasp_verified", stamp)
        if self.mode == "held" and self._arm.phase in ("await_prepare", "verify_held"):
            if not contacts["source_separated"] or not contacts["raw_bilateral"]:
                if now-self._started >= 12.:
                    return self._fail("held_verification_timeout", stamp)
                return self._wait("held_contact_pending")
            arm = self._arm.start_from_held(now, actor_observation, opening=self._opening, payload_estimate=self._payload)
        else:
            if self.mode == "pickup" and self._arm.phase in ("await_prepare", "approach", "ready", "descend"):
                supported, force = self._source_supported(carrier, item, contacts)
                self.evidence.update(source_supported=supported, source_support_force_N=force)
                if not supported or speed > self.SETTLED_SPEED:
                    return self._wait("pickup_source_not_supported")
                if self._source_item is None:
                    self._source_item = item["position"]
            phase = self._arm.phase
            action = ("prepare" if phase in ("await_prepare", "approach") else
                      "grasp" if phase in ("ready", "descend", "grasp") else
                      "lift_and_hold" if phase in ("grasped", "lift") else
                      "confirm_received" if phase == "received" and not self._grasp_verified else "place")
            if self.mode == "held" and not self._grasp_verified:
                # The arm's local initializer may finish before a paired
                # observation dwell that was interrupted by a missing peer.
                # Keep holding while fresh pairs accumulate; do not reset
                # that valid ongoing dwell on each control callback.
                return self._wait("held_stability_pending", reset=False)
            arm = self._arm.update(now, actor_observation, action)
        self.evidence["arm"] = arm["evidence"]
        self.target, self.opening, self.payload_estimate = arm["target"], arm["opening"], arm["payload_estimate"]
        self._release_settle = arm.get("release_settle") is True
        self.hold = arm["hold"] or self.target is None
        if self.mode == "held" and not self._grasp_verified:
            self.hold = True
        self.phase, self.code, self.reason = arm["phase"], arm["code"], arm["reason"]
        if arm["status"] == "failed":
            return self._fail(arm["code"], stamp)
        if self.phase in ("retract", "placed"):
            try:
                upward, own_contact = self._arm._support(actor, item)
            except ValueError as error:
                return self._wait(str(error))
            position_error = math.hypot(item["position"][0]-self.destination[0], item["position"][1]-self.destination[1])
            height_error = abs(item["position"][2]-self.destination[2]-self.item_size[2]/2)
            retreat_error = _distance(actor["tool"], self.target)
            valid = (self._grasp_verified and actor["released"] and not own_contact
                and upward >= self.SUPPORT_FRACTION*self.item_mass*9.81 and position_error <= .04
                and height_error <= .025 and speed <= self.SETTLED_SPEED and retreat_error <= self.TOOL_TOLERANCE)
            if not valid:
                self._placed_since = None
            elif self._placed_since is None:
                self._placed_since = stamp
            if arm["status"] == "completed":
                self.phase, self.hold = "verify_placement", True
                if valid and stamp-self._placed_since >= self.PLACEMENT_DWELL-1e-9:
                    self.status, self.phase, self.code = "completed", "placed", "recovery_placement_verified"
                    self.report = dict(task_id=self.task_id, item_id=self.item_id, carrier_id=self.carrier_id,
                                       receiver_id=self.actor_id, actor_id=self.actor_id, state="placed", sampled_at=stamp)
                    self.evidence["placed"] = dict(self._identity(actor, carrier), destination=list(self.destination),
                        item_position=list(item["position"]), item_speed_m_s=speed, upward_support_force_N=upward,
                        minimum_support_force_N=self.SUPPORT_FRACTION*self.item_mass*9.81,
                        actor_released=True, carrier_released=True, actor_contact=False, retreat_error_m=retreat_error,
                        position_error_m=position_error, height_error_m=height_error,
                        stable_since=self._placed_since, stable_duration_s=stamp-self._placed_since,
                        item_contact_wrenches=contacts["item_contact_wrenches"], carrier_contact_wrenches=contacts["carrier_contact_wrenches"])
                    self._event("recovery_placement_verified", stamp)
        return self._result()
