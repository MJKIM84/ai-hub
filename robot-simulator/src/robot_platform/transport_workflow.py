"""Contact-evidenced carrier transport and receiver handoff coordination.

No simulator, navigation controller, ownership table, or reservation manager is
referenced. Outputs are requests and evidence, including an optional atomic
handoff proposal. Acknowledgements alone never establish physical success.
"""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import math


def _vector(value, length=3):
    if isinstance(value, Mapping):
        value = [value.get(axis) for axis in "xyz"[:length]]
    elif all(hasattr(value, axis) for axis in "xyz"[:length]):
        value = [getattr(value, axis) for axis in "xyz"[:length]]
    try:
        result = tuple(float(component) for component in value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("finite coordinates required") from error
    if len(result) != length or not all(math.isfinite(component) for component in result):
        raise ValueError("finite coordinates required")
    return result


def _norm(values):
    return math.sqrt(sum(value*value for value in values))


class TransportWorkflow:
    VERSION = "observed-supported-transport-0.3"
    GRAVITY = 9.81
    FRESH_AGE = 1.0
    SENSOR_TIMEOUT = 2.0
    TRACKING_TIMEOUT = 1.0
    SUPPORT_EVIDENCE_TIMEOUT = 1.0
    SUPPORT_LOSS_TIMEOUT = .25
    SLIP_TIMEOUT = .20
    SUPPORT_WEIGHT_FRACTION = .60
    LOAD_DWELL = .50
    SETTLE_DWELL = .50
    SEPARATION_DWELL = .35
    ACK_DWELL = .20
    STATIONARY_SPEED = .04
    RELATIVE_SPEED = .06
    MAX_SLIP_DISTANCE = .045
    MAX_PEER_SKEW = .20
    HANDOFF_PHASES = frozenset(("await_receiver", "handoff_grasp", "separating", "confirm_handoff"))
    TRACKING_ERROR = .06

    def __init__(self, task_id, carrier_id, item_id, destination, item_mass, item_size,
                 *, support_geom, support_size, support_top_offset, receiver_id,
                 max_payload=3., timeout=180., resource_ids=None):
        if not all(isinstance(value, str) and value for value in
                   (task_id, carrier_id, item_id, support_geom, receiver_id)):
            raise ValueError("nonempty task, carrier, item, support, and receiver IDs are required")
        if carrier_id == receiver_id or not support_geom.startswith(carrier_id+"/"):
            raise ValueError("receiver must differ from carrier and support geometry must belong to carrier")
        self.task_id, self.carrier_id, self.item_id, self.receiver_id = task_id, carrier_id, item_id, receiver_id
        self.destination = dict(zip("xyz", _vector(destination)))
        self.destination["yaw"] = float(destination.get("yaw", 0.)) if isinstance(destination, Mapping) else float(getattr(destination, "yaw", 0.))
        self.item_mass, self.max_payload, self.timeout = map(float, (item_mass, max_payload, timeout))
        self.item_size = _vector(item_size)
        self.support_geom = support_geom
        self.support_size = _vector(support_size, 2)
        self.support_top_offset = _vector(support_top_offset)
        if (not all(math.isfinite(value) and value > 0 for value in
                    (self.item_mass, self.max_payload, self.timeout, *self.item_size, *self.support_size))
                or not math.isfinite(self.destination["yaw"])):
            raise ValueError("positive finite mass, dimensions, limits, and timeout required")
        # Without an observed item yaw, an enclosing circle gives a conservative
        # support footprint for any in-plane orientation of this rigid box.
        self.item_radius = math.hypot(*self.item_size[:2])/2
        self.resources = tuple(resource_ids or ("item:"+item_id, "carrier:"+carrier_id, "handoff:"+task_id))
        if not all(isinstance(value, str) and value for value in self.resources):
            raise ValueError("resource IDs must be nonempty strings")
        self.phase, self.status = "await_load", "running"
        self.code, self.reason = "awaiting_supported_load", "지지 접촉과 물품 안정을 기다립니다"
        self.hold, self.supported = True, False
        self._receiver_hold = True
        self.evidence = {"source": "observations", "workflow_version": self.VERSION, "events": []}
        self._last_now = self._started = self._phase_started = None
        self._carrier_sample = self._receiver_sample = None
        self._last_carrier = self._last_receiver = None
        self._stable_since = self._missing_item = self._missing_force = None
        self._support_lost = self._slip_since = None
        self._anchor = self._separation_at = None
        self._proposal = None
        self._ready_handshake = None
        self._tracking_previous = None

    def _event(self, event, sampled_at=None, **details):
        self.evidence["events"].append(dict(event=event, phase=self.phase, sampled_at=sampled_at, **details))

    def _result(self):
        receiver_hold = self._receiver_hold or self.status != "running"
        receiver_action = {
            "await_receiver": "prepare", "handoff_grasp": "grasp",
            "separating": "lift_and_hold", "confirm_handoff": "confirm_received",
        }.get(self.phase)
        if receiver_hold and (receiver_action is not None or self.status != "running"):
            # Stop tool trajectory tracking while preserving the existing grip
            # opening and payload compensation. This never requests release,
            # a new grasp, or a lift; the receiver's local controller executes
            # the hold and watchdog, including during communication loss.
            receiver_action = "hold"
        return dict(
            task_id=self.task_id, carrier_id=self.carrier_id, receiver_id=self.receiver_id, item_id=self.item_id,
            status=self.status, phase=self.phase, code=self.code, reason=self.reason,
            hold=self.hold, navigation_target=deepcopy(self.destination) if self.phase == "transport" and not self.hold else None,
            supported=self.supported,
            receiver_hold=receiver_hold, receiver_action=receiver_action,
            evidence=deepcopy(self.evidence),
            resource_intent={"retain": list(self.resources), "release": [], "handoff_commit": deepcopy(self._proposal)},
        )

    def _fail(self, code, reason, sampled_at=None):
        self.status, self.code, self.reason, self.hold = "failed", code, reason, True
        self._receiver_hold = True
        self._stable_since = None
        self._event("failed", sampled_at, code=code, reason=reason)
        return self._result()

    def _time(self, now):
        now = float(now)
        if not math.isfinite(now) or (self._last_now is not None and now < self._last_now):
            raise ValueError("transport time must be finite and monotonic")
        self._last_now = now
        if self._started is None:
            self._started = self._phase_started = self._last_carrier = now
        return now

    def cancel(self, now, reason="사용자 취소: 물품과 작업 공간 예약을 복구 확인까지 유지합니다"):
        self._time(now)
        if self.status in ("completed", "failed", "cancelled"):
            return self._result()
        self.status, self.code, self.reason, self.hold = "cancelled", "cancelled", reason, True
        self._receiver_hold = True
        self._event("cancelled", self._carrier_sample, reason=reason)
        return self._result()

    def _transition(self, phase, now, sampled_at):
        self.phase, self._phase_started, self._stable_since = phase, now, None
        self.code, self.reason = phase, f"{phase} 단계의 물리 관측 확인을 기다립니다"
        self.hold = phase != "transport"
        if phase == "await_receiver":
            self._last_receiver = now
        self._event("phase_entered", sampled_at)

    def _stable(self, condition, stamp, dwell):
        if not condition:
            self._stable_since = None
            return False
        if self._stable_since is None:
            self._stable_since = stamp
        return stamp-self._stable_since >= dwell-1e-9

    def _wait(self, code, reason, hold=True, reset=True):
        self.code, self.reason = code, reason
        if hold:
            self.hold = True
            self._receiver_hold = True
        if reset:
            self._stable_since = None
        return self._result()

    def _observation(self, now, observation, robot_id):
        if not isinstance(observation, Mapping) or observation.get("robot_id") != robot_id:
            raise ValueError("missing_or_wrong_robot_observation")
        try:
            stamp = float(observation["sampled_at"])
            pose = observation["pose"]
            position = _vector(pose)
            yaw = float(pose["yaw"])
            velocity = _vector(observation["velocity"])
            angular = _vector(observation["angular_velocity"])
            upright = float(observation["upright"])
        except (KeyError, TypeError, ValueError, OverflowError) as error:
            raise ValueError("invalid_robot_observation") from error
        if not all(math.isfinite(value) for value in (stamp, yaw, upright)) or stamp > now+1e-6:
            raise ValueError("future_or_invalid_observation")
        if now-stamp > self.FRESH_AGE:
            raise ValueError("stale_observation")
        sensors = observation.get("sensors")
        if not isinstance(sensors, Mapping) or not isinstance(sensors.get("items"), list) or not isinstance(sensors.get("contacts"), list):
            raise ValueError("missing_item_or_contact_sensor")
        return dict(stamp=stamp, position=position, yaw=yaw, velocity=velocity, angular=angular,
                    upright=upright, fault=observation.get("fault", "none"), sensors=sensors)

    def _item(self, reading):
        matches = [item for item in reading["sensors"]["items"] if isinstance(item, Mapping) and item.get("id") == self.item_id]
        if len(matches) != 1 or matches[0].get("visible", True) is not True:
            return None
        try:
            return dict(position=_vector(matches[0]["position"]), velocity=_vector(matches[0]["velocity"]),
                        observation=deepcopy(matches[0]))
        except (KeyError, ValueError):
            return None

    def _surface(self, carrier, item):
        c, s = math.cos(carrier["yaw"]), math.sin(carrier["yaw"])
        ox, oy, oz = self.support_top_offset
        top = (carrier["position"][0]+c*ox-s*oy, carrier["position"][1]+s*ox+c*oy, carrier["position"][2]+oz)
        delta = tuple(item["position"][axis]-top[axis] for axis in range(3))
        local = (c*delta[0]+s*delta[1], -s*delta[0]+c*delta[1], delta[2])
        inside = all(abs(local[axis])+self.item_radius <= self.support_size[axis]/2-.01 for axis in (0, 1))
        height_good = abs(local[2]-self.item_size[2]/2) <= .035
        r = tuple(item["position"][axis]-carrier["position"][axis] for axis in range(3))
        wx, wy, wz = carrier["angular"]
        rotation_velocity = (wy*r[2]-wz*r[1], wz*r[0]-wx*r[2], wx*r[1]-wy*r[0])
        relative = tuple(item["velocity"][axis]-carrier["velocity"][axis]-rotation_velocity[axis] for axis in range(3))
        separated = (item["position"][2]-self.item_size[2]/2 > top[2]+.06
                     or any(abs(local[axis])-self.item_radius > self.support_size[axis]/2+.03 for axis in (0, 1)))
        return dict(top=top, local=local, inside=inside, height_good=height_good,
                    relative_speed=_norm(relative), separated=separated)

    def _contacts(self, reading, surface):
        upward = 0.
        any_carrier_contact = False
        missing_force = False
        item_geom = self.item_id+"/shape"
        for contact in reading["sensors"]["contacts"]:
            if not isinstance(contact, Mapping):
                raise ValueError("invalid_contact_observation")
            a, b = contact.get("geom_a"), contact.get("geom_b")
            if item_geom not in (a, b):
                continue
            other = b if a == item_geom else a
            if not isinstance(other, str):
                raise ValueError("invalid_contact_observation")
            try:
                magnitude = float(contact["force"])
                point = _vector(contact["position"])
            except (KeyError, TypeError, ValueError, OverflowError) as error:
                raise ValueError("invalid_contact_observation") from error
            if not math.isfinite(magnitude) or magnitude < 0:
                raise ValueError("invalid_contact_observation")
            if other.startswith(self.carrier_id+"/") and magnitude > .1:
                any_carrier_contact = True
            if other != self.support_geom or magnitude <= .1:
                continue
            try:
                force_b = _vector(contact["force_on_b_world"])
            except (KeyError, ValueError):
                missing_force = True
                continue
            # Contact wrench is explicitly on geom_b. Reverse when the item is
            # geom_a; a force magnitude alone is never treated as upward load.
            item_upward = force_b[2] if b == item_geom else -force_b[2]
            c, s = math.cos(reading["yaw"]), math.sin(reading["yaw"])
            dx, dy = point[0]-surface["top"][0], point[1]-surface["top"][1]
            on_face = abs(c*dx+s*dy) <= self.support_size[0]/2+.015 and abs(-s*dx+c*dy) <= self.support_size[1]/2+.015
            if on_face and abs(point[2]-surface["top"][2]) <= .04:
                upward += max(0., item_upward)
        return upward, any_carrier_contact, missing_force

    def _at_destination(self, carrier):
        yaw_error = (carrier["yaw"]-self.destination["yaw"]+math.pi) % (2*math.pi)-math.pi
        return (math.hypot(carrier["position"][0]-self.destination["x"], carrier["position"][1]-self.destination["y"]) <= .12
                and abs(carrier["position"][2]-self.destination["z"]) <= .12 and abs(yaw_error) <= .12)

    def _receiver(self, now, observation, carrier, item):
        receiver = self._observation(now, observation, self.receiver_id)
        if abs(receiver["stamp"]-carrier["stamp"]) > self.MAX_PEER_SKEW:
            raise ValueError("receiver_observation_skew")
        tracked = self._item(receiver)
        if tracked is None or _norm(tuple(a-b for a, b in zip(tracked["position"], item["position"]))) > .06:
            raise ValueError("receiver_item_disagreement")
        reports = receiver["sensors"].get("manipulation", {})
        manipulation = reports.get(self.item_id, {}) if isinstance(reports, Mapping) and "tool_position" not in reports else reports
        if not isinstance(manipulation, Mapping):
            manipulation = {}
        # Keyed feedback is identified by the item key; normalized feedback can
        # instead carry an explicit contact_item_id.
        identified = (isinstance(reports, Mapping) and self.item_id in reports) or manipulation.get("contact_item_id") == self.item_id
        contacts = manipulation.get("finger_contacts", [])
        bilateral = (identified and manipulation.get("bilateral_contact") is True
                     and isinstance(contacts, (list, tuple)) and "left" in contacts and "right" in contacts)
        ack = receiver["sensors"].get("handoff")
        if ack is not None:
            if (not isinstance(ack, Mapping) or ack.get("task_id") != self.task_id
                    or ack.get("item_id") != self.item_id or ack.get("carrier_id") != self.carrier_id
                    or ack.get("receiver_id", self.receiver_id) != self.receiver_id):
                raise ValueError("handoff_identity_mismatch")
            try:
                ack_stamp = float(ack["sampled_at"])
            except (KeyError, TypeError, ValueError, OverflowError) as error:
                raise ValueError("invalid_handoff_ack") from error
            if (not math.isfinite(ack_stamp) or ack_stamp > receiver["stamp"]+1e-6
                    or now-ack_stamp > self.FRESH_AGE or ack.get("state") not in ("ready", "received")):
                raise ValueError("invalid_handoff_ack")
        return receiver, tracked, bilateral, ack

    def _tracking(self, now, carrier, receiver_observation, *, duplicate=False):
        """Choose an identified observation without editing either input.

        During a previously negotiated handoff only, the receiver can observe
        an item hidden from the carrier's tag ray by the receiving gripper.
        Carrier force/contact observations are never replaced by this choice.
        """
        item = self._item(carrier)
        if item is not None:
            return item, dict(tracking_source="carrier", tracking_robot_id=self.carrier_id,
                              tracking_sampled_at=carrier["stamp"], tracking_prediction_error_m=None)
        if self.phase not in self.HANDOFF_PHASES:
            return None, None
        own_matches = [row for row in carrier["sensors"]["items"]
                       if isinstance(row, Mapping) and row.get("id") == self.item_id]
        # A missing/explicitly occluded item is eligible for fallback. A
        # malformed or duplicate visible carrier item is not hidden by it.
        if len(own_matches) > 1 or (own_matches and own_matches[0].get("visible", True) is True):
            raise ValueError("invalid_carrier_item_tracking")
        peer = self._observation(now, receiver_observation, self.receiver_id)
        tracked = self._item(peer)
        if tracked is None:
            raise ValueError("receiver_item_tracking_missing")
        receiver, tracked, bilateral, ack = self._receiver(now, receiver_observation, carrier, tracked)
        if receiver["fault"] not in (None, False, "none") or receiver["sensors"].get("controller_error"):
            raise ValueError("receiver_fault")
        if (receiver["upright"] < .98 or _norm(receiver["velocity"]) > self.STATIONARY_SPEED
                or _norm(receiver["angular"]) > .08 or receiver_observation.get("operator_hold", False)):
            raise ValueError("receiver_not_stationary")
        if self._receiver_sample is not None:
            if receiver["stamp"] < self._receiver_sample:
                raise ValueError("reordered_receiver_observation")
            if not duplicate and receiver["stamp"] == self._receiver_sample:
                raise ValueError("awaiting_fresh_receiver_observation")
        ready = ack is not None and ack["state"] == "ready"
        if (self.phase == "await_receiver" and not ready) or (self._ready_handshake is None and not ready):
            raise ValueError("receiver_tracking_not_negotiated")
        if self.phase in ("separating", "confirm_handoff") and not bilateral:
            raise ValueError("receiver_contact_lost")
        previous = self._tracking_previous
        if previous is None:
            raise ValueError("receiver_tracking_without_anchor")
        dt = receiver["stamp"]-previous["sampled_at"]
        if dt < -1e-9:
            raise ValueError("reordered_tracking_observation")
        if dt > self.FRESH_AGE:
            raise ValueError("receiver_tracking_anchor_stale")
        predicted = tuple(previous["position"][i]+.5*(previous["velocity"][i]+tracked["velocity"][i])*dt for i in range(3))
        error = _norm(tuple(tracked["position"][i]-predicted[i] for i in range(3)))
        if error > self.TRACKING_ERROR:
            raise ValueError("receiver_tracking_discontinuity")
        return tracked, dict(tracking_source="receiver_fallback", tracking_robot_id=self.receiver_id,
                             tracking_sampled_at=receiver["stamp"], tracking_prediction_error_m=error)

    def update(self, now, carrier_observation, receiver_observation=None):
        now = self._time(now)
        if self.status in ("failed", "completed", "cancelled"):
            return self._result()
        if self.item_mass > self.max_payload:
            return self._fail("overload", "물품 질량이 운반 지지면의 허용 적재량을 초과합니다")
        if any(self.item_radius >= side/2-.01 for side in self.support_size):
            return self._fail("item_exceeds_support", "회전을 고려한 물품 외곽이 지지면에 들어가지 않습니다")
        if now-self._started >= self.timeout:
            return self._fail("timeout", "운반·인계 제한 시간을 초과했습니다", self._carrier_sample)
        try:
            carrier = self._observation(now, carrier_observation, self.carrier_id)
            if self._carrier_sample is not None and carrier["stamp"] < self._carrier_sample:
                raise ValueError("reordered_observation")
        except ValueError as error:
            self.supported = False
            if now-self._last_carrier >= self.SENSOR_TIMEOUT:
                return self._fail("carrier_observation_timeout", "운반 로봇의 신선한 관측이 소실되었습니다", self._carrier_sample)
            return self._wait(str(error), "운반 로봇의 신선한 관측을 기다립니다")
        stamp = carrier["stamp"]
        if carrier["fault"] not in (None, False, "none"):
            return self._fail("communication_lost" if carrier["fault"] in ("communication", "sensor") else "carrier_fault", "운반 로봇이 장애를 보고했습니다", stamp)
        if carrier["upright"] < .98:
            return self._fail("carrier_unstable", "검증된 수평 지지면 자세 범위를 벗어났습니다", stamp)
        if self._carrier_sample is not None and stamp == self._carrier_sample:
            if now-self._last_carrier >= self.SENSOR_TIMEOUT:
                return self._fail("carrier_observation_timeout", "같은 관측만 반복 수신했습니다", stamp)
            if self.phase in ("await_receiver", "handoff_grasp", "separating", "confirm_handoff"):
                # A duplicate carrier sample cannot hide a missing/faulted
                # receiver or lost grip. Validate safety without advancing
                # either peer's sample counter or any phase dwell.
                try:
                    item, _ = self._tracking(now, carrier, receiver_observation, duplicate=True)
                    if item is None:
                        raise ValueError("item_tracking_pending")
                    peer, _, bilateral, _ = self._receiver(now, receiver_observation, carrier, item)
                    if self._receiver_sample is not None and peer["stamp"] < self._receiver_sample:
                        raise ValueError("reordered_receiver_observation")
                except ValueError as error:
                    if str(error) in ("handoff_identity_mismatch", "receiver_fault", "receiver_contact_lost"):
                        return self._fail(str(error), "인계 메시지의 식별자가 다릅니다", stamp)
                    if now-self._last_receiver >= self.SENSOR_TIMEOUT:
                        return self._fail("receiver_observation_timeout", "인수 로봇의 관측이 소실되었습니다", stamp)
                    return self._wait(str(error), "인수 로봇의 유효한 관측을 기다립니다")
                if peer["fault"] not in (None, False, "none"):
                    return self._fail("receiver_fault", "인수 로봇이 장애를 보고했습니다", peer["stamp"])
                if self.phase in ("separating", "confirm_handoff") and not bilateral:
                    return self._fail("receiver_contact_lost", "인수 로봇의 양쪽 파지 접촉이 소실되었습니다", peer["stamp"])
            return self._wait("awaiting_fresh_observation", "새 물리 관측을 기다립니다", hold=False, reset=False)
        if self._carrier_sample is not None and stamp-self._carrier_sample > .5:
            self._stable_since = None
        self._carrier_sample, self._last_carrier = stamp, now
        self._receiver_hold = True  # Only a valid pair below can authorize motion.
        self.evidence.update(sampled_at=stamp, carrier_id=self.carrier_id)
        measured_mass = carrier["sensors"].get("payload_mass_kg")
        if isinstance(measured_mass, (int, float)) and math.isfinite(measured_mass) and measured_mass > self.max_payload:
            return self._fail("overload", "하중 센서가 허용 적재량 초과를 보고했습니다", stamp)
        tracking_error = None
        try:
            item, tracking = self._tracking(now, carrier, receiver_observation)
        except ValueError as error:
            tracking_error = str(error)
            if tracking_error in ("handoff_identity_mismatch", "receiver_fault", "receiver_contact_lost"):
                return self._fail(tracking_error, "인수 관측의 식별자·장애·파지 조건을 확인할 수 없습니다", stamp)
            item, tracking = None, None
        if item is None:
            self.supported = False
            if self._missing_item is None:
                self._missing_item = now
            if now-self._missing_item >= self.TRACKING_TIMEOUT:
                return self._fail("item_tracking_lost", "운반 중 물품 위치·속도 관측이 소실되었습니다", stamp)
            return self._wait(tracking_error or "item_tracking_pending", "물품 위치·속도 관측을 기다립니다")
        self._missing_item = None
        self.evidence.update(tracking, tracking_observation=deepcopy(item["observation"]))
        self._tracking_previous = dict(sampled_at=tracking["tracking_sampled_at"],
                                       position=item["position"], velocity=item["velocity"])
        surface = self._surface(carrier, item)
        try:
            upward, touching, missing_force = self._contacts(carrier, surface)
        except ValueError as error:
            return self._fail(str(error), "유효하지 않은 접촉 관측입니다", stamp)
        if missing_force:
            self.supported = False
            if self._missing_force is None:
                self._missing_force = now
            if now-self._missing_force >= self.SUPPORT_EVIDENCE_TIMEOUT:
                return self._fail("support_evidence_unavailable", "접촉 힘의 수직 방향 증거가 없습니다", stamp)
            return self._wait("support_force_unavailable", "스칼라 접촉 크기만으로 적재 지지를 확인할 수 없습니다")
        self._missing_force = None
        minimum_force = self.SUPPORT_WEIGHT_FRACTION*self.item_mass*self.GRAVITY
        self.supported = surface["inside"] and surface["height_good"] and upward >= minimum_force
        self.evidence.update(item_position=list(item["position"]), upward_support_force_N=upward,
                             minimum_support_force_N=minimum_force, item_relative_speed=surface["relative_speed"],
                             item_local_position=list(surface["local"]), carrier_item_contact=touching)
        self.hold = self.phase != "transport"
        self.code, self.reason = self.phase, f"{self.phase} 단계의 관측 증거를 확인합니다"
        stopped = _norm(carrier["velocity"]) <= self.STATIONARY_SPEED and _norm(carrier["angular"]) <= .08
        settled = surface["relative_speed"] <= self.RELATIVE_SPEED
        if self._anchor is not None and item["position"][2] < surface["top"][2]+self.item_size[2]/2-.08:
            return self._fail("item_dropped", "물품이 지지면보다 아래로 떨어졌습니다", stamp)
        if self.phase in ("transport", "settle", "await_receiver"):
            slipping = (not surface["inside"] or surface["relative_speed"] > self.RELATIVE_SPEED
                        or math.hypot(surface["local"][0]-self._anchor[0], surface["local"][1]-self._anchor[1]) > self.MAX_SLIP_DISTANCE)
            if slipping:
                if self._slip_since is None:
                    self._slip_since = now
                if now-self._slip_since >= self.SLIP_TIMEOUT-1e-9:
                    return self._fail("item_slipping", "물품이 운반 지지면에 대해 미끄러지고 있습니다", stamp)
                return self._wait("slip_pending", "물품 상대 이동을 관측하여 제동합니다")
            self._slip_since = None
            if not self.supported:
                if self._support_lost is None:
                    self._support_lost = now
                if now-self._support_lost >= self.SUPPORT_LOSS_TIMEOUT-1e-9:
                    return self._fail("item_support_lost", "적재 지지 접촉이 소실되었습니다", stamp)
                return self._wait("support_loss_pending", "적재 지지 접촉을 재확인합니다")
            self._support_lost = None
        if stamp < self._phase_started:
            return self._wait("awaiting_phase_observation", "명령 이후의 관측을 기다립니다")
        if self.phase == "await_load":
            if self._stable(self.supported and settled and stopped, stamp, self.LOAD_DWELL):
                self._anchor = surface["local"]
                self._event("load_supported", stamp, criterion="identified_upward_contact_and_settled_item")
                self._transition("transport", now, stamp)
        elif self.phase == "transport":
            if self._at_destination(carrier):
                self._transition("settle", now, stamp)
        elif self.phase == "settle":
            if not self._at_destination(carrier):
                self._transition("transport", now, stamp)
            elif self._stable(self.supported and settled and stopped, stamp, self.SETTLE_DWELL):
                self._event("destination_settled", stamp)
                self._transition("await_receiver", now, stamp)
        else:
            if not self._at_destination(carrier):
                return self._fail("carrier_left_handoff", "인계 중 운반 로봇이 목적 위치를 벗어났습니다", stamp)
            if not stopped:
                return self._wait("carrier_moving_during_handoff", "인계 중 운반 로봇이 아직 정지하지 않았습니다")
            try:
                receiver, receiver_item, bilateral, ack = self._receiver(now, receiver_observation, carrier, item)
                if self._receiver_sample is not None and receiver["stamp"] <= self._receiver_sample:
                    raise ValueError("awaiting_fresh_receiver_observation")
            except ValueError as error:
                if str(error) == "handoff_identity_mismatch":
                    return self._fail(str(error), "인계 메시지의 작업·물품·상대 로봇 식별자가 다릅니다", stamp)
                if now-self._last_receiver >= self.SENSOR_TIMEOUT:
                    return self._fail("receiver_observation_timeout", "인수 로봇의 신선한 관측 또는 물품 일치 증거가 소실되었습니다", stamp)
                return self._wait(str(error), "인수 로봇의 일치하는 새 관측을 기다립니다")
            self._receiver_sample, self._last_receiver = receiver["stamp"], now
            if receiver["fault"] not in (None, False, "none"):
                return self._fail("receiver_fault", "인수 로봇이 장애를 보고했습니다", stamp)
            self._receiver_hold = False
            self.evidence.update(receiver_sampled_at=receiver["stamp"], receiver_bilateral_contact=bilateral)
            if self.phase == "await_receiver":
                if ack is not None and ack["state"] == "ready":
                    self._ready_handshake = deepcopy(ack)
                    self._event("receiver_ready", receiver["stamp"])
                    self._transition("handoff_grasp", now, stamp)
            elif self.phase == "handoff_grasp":
                if self._stable(bilateral, min(stamp, receiver["stamp"]), .2):
                    self._event("receiver_grasp_confirmed", receiver["stamp"])
                    self._transition("separating", now, stamp)
                elif not self.supported and not bilateral:
                    return self._fail("handoff_support_lost", "운반 지지와 인수 로봇 파지 모두 확인되지 않습니다", stamp)
            else:
                if not bilateral:
                    return self._fail("receiver_contact_lost", "인수 로봇의 양쪽 파지 접촉이 소실되었습니다", receiver["stamp"])
                separated = not touching and surface["separated"]
                stationary_item = _norm(item["velocity"]) <= self.STATIONARY_SPEED and _norm(receiver_item["velocity"]) <= self.STATIONARY_SPEED
                physically_ready = separated and stationary_item and bilateral
                if self.phase == "separating":
                    if self._stable(physically_ready, min(stamp, receiver["stamp"]), self.SEPARATION_DWELL):
                        self._separation_at = max(stamp, receiver["stamp"])
                        self.evidence["sender_confirmation"] = dict(task_id=self.task_id, item_id=self.item_id,
                            robot_id=self.carrier_id, receiver_id=self.receiver_id, sampled_at=stamp, state="observed_released")
                        self._event("physical_separation_confirmed", stamp)
                        self._transition("confirm_handoff", now, stamp)
                elif self.phase == "confirm_handoff":
                    if not physically_ready:
                        return self._fail("handoff_evidence_lost", "최종 확인 전에 분리·정지·파지 증거가 사라졌습니다", stamp)
                    acknowledged = ack is not None and ack["state"] == "received" and ack["sampled_at"] > self._separation_at
                    if self._stable(acknowledged, min(stamp, receiver["stamp"]), self.ACK_DWELL):
                        self.status, self.code, self.reason = "completed", "handoff_verified", "물리적 분리와 양쪽의 신선한 인계 확인을 수신했습니다"
                        self._proposal = dict(task_id=self.task_id, item_id=self.item_id, from_robot=self.carrier_id,
                            to_robot=self.receiver_id, carrier_sampled_at=stamp, receiver_sampled_at=receiver["stamp"],
                            receiver_ack_at=ack["sampled_at"], separated_at=self._separation_at)
                        self.evidence["sender_confirmation"]["sampled_at"] = stamp
                        self.evidence["receiver_confirmation"] = deepcopy(ack)
                        self._event("handoff_verified", stamp)
                    elif not acknowledged:
                        self.code, self.reason = "awaiting_post_separation_ack", "물리적 분리 이후의 인수 완료 메시지를 기다립니다"
        return self._result()
