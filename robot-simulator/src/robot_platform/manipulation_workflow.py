"""Observation-only pick/place sequencing for the research arm controller.

This module has no simulator or controller reference. Commands are requests;
only fresh, identified tactile and item-tracking observations advance a task.
"""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import math


def _vector(value, name):
    if isinstance(value, Mapping):
        value = [value.get(axis) for axis in "xyz"]
    elif all(hasattr(value, axis) for axis in "xyz"):
        value = [getattr(value, axis) for axis in "xyz"]
    try:
        result = tuple(float(component) for component in value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{name} requires three finite coordinates") from exc
    if len(result) != 3 or not all(math.isfinite(component) for component in result):
        raise ValueError(f"{name} requires three finite coordinates")
    return result


def _distance(a, b):
    return math.sqrt(sum((x-y)**2 for x, y in zip(a, b)))


class ManipulationWorkflow:
    """Issue world-space tool targets; never create attachment or ownership.

    ``source`` and ``destination`` are item bottom centers, while item tracking
    reports its center. ``opening`` is the controller's per-finger slide target.
    Retries are additional attempts, and the overall timeout includes retries.
    """

    VERSION = "observed-contact-pick-place-0.1"
    OBSERVATION_MAX_AGE = 1.0
    OBSERVATION_TIMEOUT = 3.0
    OCCLUSION_TIMEOUT = 2.0
    CONTACT_LOSS_TIMEOUT = .30
    TOOL_TOLERANCE = .035
    PLACEMENT_XY_TOLERANCE = .04
    PLACEMENT_Z_TOLERANCE = .015
    SETTLED_SPEED = .035
    PHASE_TIMEOUTS = {
        "approach": 18., "descend": 12., "grasp": 5., "lift": 15.,
        "translate": 20., "lower": 15., "release": 6., "retract": 15.,
        "retry_open": 4.,
    }

    def __init__(self, task_id, robot_id, item_id, source, destination,
                 item_mass, item_size, max_payload=3, retries=1, timeout=120):
        if not all(isinstance(value, str) and value for value in (task_id, robot_id, item_id)):
            raise ValueError("task, robot, and item IDs must be nonempty strings")
        self.task_id, self.robot_id, self.item_id = task_id, robot_id, item_id
        self.source = _vector(source, "source")
        self.destination = _vector(destination, "destination")
        self.item_size = _vector(item_size, "item_size")
        self.item_mass, self.max_payload, self.timeout = map(float, (item_mass, max_payload, timeout))
        if (not all(math.isfinite(value) for value in (self.item_mass, self.max_payload, self.timeout))
                or self.item_mass <= 0 or self.max_payload <= 0 or self.timeout <= 0
                or min(self.item_size) <= 0):
            raise ValueError("mass, payload limit, item dimensions, and timeout must be positive and finite")
        if isinstance(retries, bool) or not isinstance(retries, int) or retries < 0:
            raise ValueError("retries must be a nonnegative integer")
        self.retries = retries
        self.attempt = 1
        self.status = "running"
        self.phase = "approach"
        self.holding = False
        self.reason = "새 관측과 접근 위치 도달을 기다립니다"
        self.code = "approaching"
        self.evidence = {"source": "observation", "workflow_version": self.VERSION, "events": []}
        self._started_at = self._phase_started = self._last_now = None
        self._last_sample = self._last_fresh_at = None
        self._stable_since = self._occluded_since = self._contact_lost_since = None
        self._hold = True
        self._tool = None
        self._retry_reason = None
        self._grasp_z = self.source[2] + self.item_size[2]/2 + .13
        self._place_z = self.destination[2] + self.item_size[2]/2 + .13
        self._cruise_z = max(self._grasp_z, self._place_z) + .30
        self._target = (self.source[0], self.source[1], self._cruise_z)

    def _command(self):
        opening = .1 if self.phase in ("approach", "descend", "release", "retract", "retry_open") else 0.
        payload = self.item_mass if self.holding and self.phase != "release" else 0.
        return {
            "task_id": self.task_id, "robot_id": self.robot_id, "item_id": self.item_id,
            "target": list(self._target), "targetXYZ": list(self._target),
            "opening": opening, "payload_estimate": payload,
            "hold": self._hold,
            "status": self.status, "phase": self.phase, "holding": self.holding,
            "reason": self.reason, "code": self.code, "attempt": self.attempt,
            "evidence": deepcopy(self.evidence),
        }

    def _event(self, name, sampled_at=None, **details):
        event = {"event": name, "attempt": self.attempt, "phase": self.phase, **details}
        if sampled_at is not None:
            event["sampled_at"] = sampled_at
        self.evidence["events"].append(event)

    def _fail(self, code, reason, sampled_at=None):
        self.status, self.code, self.reason = "failed", code, reason
        self._hold = True
        # A terminal failure requests holding the last observed tool pose. The
        # caller must still manage the robot's stop/fault response explicitly.
        if self._tool is not None:
            self._target = self._tool
        self._event("failed", sampled_at, code=code, reason=reason)
        return self._command()

    def _transition(self, phase, now, sampled_at, reason):
        self.phase = phase
        self._phase_started, self._stable_since = now, None
        self.code, self.reason = phase, reason
        sx, sy, _ = self.source
        dx, dy, _ = self.destination
        self._target = {
            "approach": (sx, sy, self._cruise_z),
            "descend": (sx, sy, self._grasp_z),
            "grasp": (sx, sy, self._grasp_z),
            "lift": (sx, sy, self._cruise_z),
            "translate": (dx, dy, self._cruise_z),
            "lower": (dx, dy, self._place_z),
            "release": (dx, dy, self._place_z),
            "retract": (dx, dy, self._cruise_z),
            "retry_open": (sx, sy, self._grasp_z),
        }[phase]
        self._event("phase_entered", sampled_at)

    def _stable(self, condition, sampled_at, dwell=.2):
        if not condition:
            self._stable_since = None
            return False
        if self._stable_since is None:
            self._stable_since = sampled_at
        return sampled_at-self._stable_since >= dwell-1e-9

    def _at_source(self, position):
        center = (self.source[0], self.source[1], self.source[2]+self.item_size[2]/2)
        return math.hypot(position[0]-center[0], position[1]-center[1]) <= .07 and abs(position[2]-center[2]) <= .025

    def _placed(self, position):
        center = (self.destination[0], self.destination[1], self.destination[2]+self.item_size[2]/2)
        return (math.hypot(position[0]-center[0], position[1]-center[1]) <= self.PLACEMENT_XY_TOLERANCE
                and abs(position[2]-center[2]) <= self.PLACEMENT_Z_TOLERANCE)

    def _retry(self, now, sampled_at, position, speed, code):
        if self.attempt > self.retries:
            return self._fail("retries_exhausted", "파지 재시도 횟수를 모두 사용했습니다", sampled_at)
        if not self._at_source(position) or speed > self.SETTLED_SPEED or self.holding:
            return self._fail("recovery_required", "물품이 시작 위치에 안정적으로 놓여 있지 않아 별도 복구가 필요합니다", sampled_at)
        self._event("retry_scheduled", sampled_at, cause=code)
        self.attempt += 1
        self.status, self._retry_reason = "retrying", code
        self._transition("retry_open", now, sampled_at, "시작 위치의 물품을 확인하고 그리퍼를 열어 재시도합니다")
        return self._command()

    def update(self, now, robot_observation):
        """Return a controller request derived exclusively from the observation.

        Duplicate, reordered, future, stale, missing, or malformed observations
        cannot advance phases, accumulate dwell evidence, or declare success.
        ``now`` and ``sampled_at`` must share the simulation/robot time base.
        """
        now = float(now)
        if not math.isfinite(now) or (self._last_now is not None and now < self._last_now):
            raise ValueError("workflow time must be finite and monotonic")
        self._last_now = now
        if self.status in ("completed", "failed"):
            return self._command()
        if self._started_at is None:
            self._started_at = self._phase_started = self._last_fresh_at = now
        if self.item_mass > self.max_payload:
            return self._fail("overload", "물품 질량이 허용 적재량을 초과합니다")
        if now-self._started_at >= self.timeout:
            return self._fail("timeout", "물품 조작 전체 제한 시간을 초과했습니다", self._last_sample)
        if not isinstance(robot_observation, Mapping):
            return self._wait_observation(now, "missing_observation", "로봇 관측을 기다립니다")
        obs = robot_observation
        try:
            sampled_at = float(obs["sampled_at"])
        except (KeyError, TypeError, ValueError, OverflowError):
            return self._wait_observation(now, "invalid_observation", "관측 시각이 유효하지 않습니다")
        if obs.get("robot_id") != self.robot_id:
            return self._wait_observation(now, "wrong_robot", "지정 로봇의 관측을 기다립니다")
        if not math.isfinite(sampled_at) or sampled_at > now+1e-6:
            return self._wait_observation(now, "future_observation", "현재 시간보다 앞선 관측은 사용할 수 없습니다")
        if now-sampled_at > self.OBSERVATION_MAX_AGE:
            return self._wait_observation(now, "stale_observation", "오래된 관측으로 조작을 진행할 수 없습니다")
        if self._last_sample is not None and sampled_at <= self._last_sample:
            return self._wait_observation(now, "awaiting_fresh_observation", "새로운 시각의 관측을 기다립니다", reset=False)
        sensors = obs.get("sensors")
        if not isinstance(sensors, Mapping) or not isinstance(sensors.get("manipulation"), Mapping):
            return self._wait_observation(now, "missing_manipulation_sensor", "도구 위치·접촉 관측을 기다립니다")
        manipulation = sensors["manipulation"]
        try:
            tool = _vector(manipulation["tool_position"], "tool_position")
        except (KeyError, ValueError):
            return self._wait_observation(now, "invalid_tool_observation", "유효한 도구 위치 관측을 기다립니다")
        contacts = manipulation.get("finger_contacts")
        if (type(manipulation.get("bilateral_contact")) is not bool
                or not isinstance(contacts, (tuple, list, set))
                or any(side not in ("left", "right") for side in contacts)):
            return self._wait_observation(now, "invalid_contact_observation", "유효한 손가락 접촉 관측을 기다립니다")
        contacts = set(contacts)
        if self._last_sample is not None and sampled_at-self._last_sample > .5:
            self._stable_since = None
        self._last_sample, self._last_fresh_at, self._tool = sampled_at, now, tool
        self.evidence.update(sampled_at=sampled_at, observation_age=now-sampled_at)
        if obs.get("fault") not in (None, False, "none"):
            return self._fail("robot_fault", "로봇이 장애 상태를 보고했습니다", sampled_at)
        measured_load = manipulation.get("payload_estimate_kg")
        if isinstance(measured_load, (int, float)) and math.isfinite(measured_load) and measured_load > self.max_payload:
            return self._fail("overload", "관측된 적재량이 허용치를 초과합니다", sampled_at)
        tracking = sensors.get("item_tracking", {})
        item = tracking.get(self.item_id) if isinstance(tracking, Mapping) else None
        if not isinstance(item, Mapping) or item.get("visible") is not True:
            return self._occluded(now, sampled_at)
        try:
            position = _vector(item["position"], "item position")
            velocity = _vector(item["velocity"], "item velocity")
        except (KeyError, ValueError):
            return self._occluded(now, sampled_at)
        self._occluded_since = None
        self._hold = False
        speed = _distance(velocity, (0., 0., 0.))
        identified = manipulation.get("contact_item_id") == self.item_id
        bilateral = manipulation.get("bilateral_contact") is True and identified and {"left", "right"} <= contacts
        released = manipulation.get("bilateral_contact") is False and not contacts
        self.evidence.update(tool_position=list(tool), item_position=list(position), item_speed=speed,
                             bilateral_contact=bilateral, contact_item_id=manipulation.get("contact_item_id"))
        if manipulation.get("bilateral_contact") is True and not identified:
            return self._fail("wrong_item_contact", "양쪽 손가락 접촉의 물품 식별자가 일치하지 않습니다", sampled_at)
        if self.phase in ("lift", "translate", "lower"):
            if not bilateral:
                self._hold = True
                self._stable_since = None
                if self._contact_lost_since is None:
                    self._contact_lost_since = now
                self.code, self.reason = "contact_loss_pending", "파지 접촉 소실을 관측하여 유지 여부를 확인합니다"
                if now-self._contact_lost_since >= self.CONTACT_LOSS_TIMEOUT-1e-9:
                    self.holding = False
                    return self._fail("contact_lost", "운반 중 양쪽 손가락의 파지 접촉이 소실되었습니다", sampled_at)
                return self._command()
            self._contact_lost_since = None
        if sampled_at < self._phase_started:
            self._stable_since = None
            return self._command()
        if now-self._phase_started >= self.PHASE_TIMEOUTS[self.phase]:
            if self.phase == "grasp":
                return self._retry(now, sampled_at, position, speed, "grasp_timeout")
            return self._fail("phase_timeout", f"{self.phase} 단계의 관측 확인 제한 시간을 초과했습니다", sampled_at)
        at_target = _distance(tool, self._target) <= self.TOOL_TOLERANCE
        self.code, self.reason = self.phase, f"{self.phase} 단계의 센서 확인을 기다립니다"
        if self.phase in ("approach", "descend"):
            if not self._at_source(position):
                return self._fail("item_outside_source", "물품이 지정 시작 위치에서 관측되지 않습니다", sampled_at)
            if self._stable(at_target, sampled_at):
                following = "descend" if self.phase == "approach" else "grasp"
                self._transition(following, now, sampled_at, "도구 도달을 관측하여 다음 조작을 요청합니다")
        elif self.phase == "grasp":
            if self._stable(bilateral and at_target, sampled_at, .35):
                self.holding = True
                self._event("grasp_confirmed", sampled_at, criterion="identified_bilateral_contact")
                self._transition("lift", now, sampled_at, "양쪽 접촉을 확인하여 물품을 들어 올립니다")
        elif self.phase == "lift":
            lifted = position[2] >= self.source[2]+self.item_size[2]/2+.12
            if self._stable(at_target and lifted and bilateral, sampled_at):
                self._event("lift_confirmed", sampled_at, item_position=list(position))
                self._transition("translate", now, sampled_at, "물품 상승을 관측하여 목적 위치로 이동합니다")
        elif self.phase == "translate":
            lifted = position[2] >= max(self.source[2], self.destination[2])+self.item_size[2]/2+.10
            aligned = math.hypot(position[0]-self.destination[0], position[1]-self.destination[1]) <= .06
            if self._stable(at_target and aligned and lifted and bilateral, sampled_at):
                self._transition("lower", now, sampled_at, "목적 위치 위의 물품을 확인하여 낮춥니다")
        elif self.phase == "lower":
            close_to_surface = (math.hypot(position[0]-self.destination[0], position[1]-self.destination[1]) <= .06
                                and abs(position[2]-(self.destination[2]+self.item_size[2]/2)) <= .04)
            if self._stable(at_target and close_to_surface and bilateral, sampled_at):
                self._transition("release", now, sampled_at, "지지 위치까지 낮춘 물품의 그리퍼를 엽니다")
        elif self.phase == "release":
            if released:
                self.holding = False
            if self._stable(released and self._placed(position) and speed <= self.SETTLED_SPEED, sampled_at, .5):
                self._event("release_confirmed", sampled_at, criterion="no_finger_contact_placed_and_settled")
                self._transition("retract", now, sampled_at, "접촉 해제와 물품 안정을 확인하여 도구를 물립니다")
        elif self.phase == "retract":
            if self._stable(at_target and released and self._placed(position) and speed <= self.SETTLED_SPEED,
                            sampled_at, .5):
                self.status, self.code = "completed", "placement_verified"
                self.reason = "도구 후퇴·접촉 해제·목적 위치의 물품 안정을 관측했습니다"
                self._event("completed", sampled_at, criterion="retracted_released_placed_and_settled")
        elif self.phase == "retry_open":
            if self._stable(released and self._at_source(position) and speed <= self.SETTLED_SPEED, sampled_at, .3):
                self.status = "running"
                self._transition("approach", now, sampled_at, "물품 안정과 그리퍼 해제를 확인하여 다시 접근합니다")
        return self._command()

    def _wait_observation(self, now, code, reason, reset=True):
        if reset:
            self._stable_since = None
            self._hold = True
        if now-self._last_fresh_at >= self.OBSERVATION_TIMEOUT:
            return self._fail("observation_timeout", "유효한 새 관측이 제한 시간 동안 도착하지 않았습니다", self._last_sample)
        self.code, self.reason = code, reason
        return self._command()

    def _occluded(self, now, sampled_at):
        self._stable_since = None
        self._hold = True
        if self._occluded_since is None:
            self._occluded_since = now
        if now-self._occluded_since >= self.OCCLUSION_TIMEOUT:
            return self._fail("item_occluded", "물품 위치·속도 관측이 제한 시간 동안 소실되었습니다", sampled_at)
        self.code, self.reason = "item_occluded_pending", "물품 위치·속도가 다시 관측되기를 기다립니다"
        return self._command()
