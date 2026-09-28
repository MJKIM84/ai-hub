"""Observed single-connector charging reservations for authored research robots.

This manager neither moves robots nor changes battery state. Its requested watts
must pass a separate instantaneous physical contact/electrical interlock before
energy is integrated. Two independent delivered observation streams authorize
charging; a reservation or proximity alone never does.
"""
from __future__ import annotations

from collections import deque
from copy import deepcopy
from dataclasses import dataclass, field
import json
import math

from .catalog import model_by_id
from .domain import Project

VERSION = "observed-charging-0.1"


def _number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _pose(value):
    if not isinstance(value, dict) or any(not _number(value.get(k)) for k in ("x", "y", "z", "yaw")):
        raise ValueError("목표는 유한한 x/y/z/yaw 좌표여야 합니다")
    return {k: float(value[k]) for k in ("x", "y", "z", "yaw")}


@dataclass
class ChargeRequest:
    id: str
    station_id: str
    robot_id: str
    geometry: dict
    requested_at: float
    target_percent: float
    status: str = "queued"
    phase: str = "queued"
    phase_since: float = 0.
    minimum_stamp: float = 0.
    robot_stable_since: float | None = None
    station_stable_since: float | None = None
    near_since: float | None = None
    cancel_requested: bool = False
    handoff_pending: bool = False
    motion_generation: int = 0
    stop_delivered_at: float | None = None
    resume_phase: str = "approach"
    reason: str = "충전 접점 FIFO 대기"


@dataclass
class Station:
    queue: deque = field(default_factory=deque)
    active: ChargeRequest | None = None
    phase: str = "idle"
    fault: str | None = None
    fault_latched: bool = False
    occupants: list[str] = field(default_factory=list)


class ChargingManager:
    """FIFO, one connector per station, fresh bilateral contact and safe release.

    ``geometry`` has ``staging`` and ``target`` world poses using the robot's
    observed pose origin. Station contacts and robot ``sensors.docking[eid]``
    share left/right/aligned booleans, normal_force N and relative_speed m/s.
    Their enclosing sampled_at values are independent simulation timestamps.
    Exact fresh duplicate packets may sustain a previously authorized request,
    but never accrue confirmation time. Altered same-time packets are faults.
    """

    confirmation_time = .3
    position_tolerance = .12
    yaw_tolerance = .15
    stopped_speed = .04
    stopped_angular_speed = .08
    minimum_force = .1
    near_contact_timeout = 8.
    phase_timeouts = {"approach": 120., "dock": 30., "charging": 7200., "undock": 30.}

    def __init__(self, project: Project):
        self.project = project.model_copy(deep=True)
        self.elements = {e.id: e for e in self.project.environment.elements if e.kind == "charger"}
        self.robots = {r.id: r for r in self.project.robots}
        self.floors = {f.id: f.elevation for f in self.project.environment.floors}
        self.stations = {eid: Station() for eid in self.elements}
        self.requests: dict[str, ChargeRequest] = {}
        self.time = 0.
        self.sequence = 0
        self.stale_after = project.policy.stale_after
        self.charge_until = project.policy.charge_until
        self._stream_history: dict[tuple[str, str], tuple[float, str]] = {}
        self._robot_observations: dict[str, dict] = {}
        self._station_observations: dict[str, dict] = {}

    @staticmethod
    def _receipt(request):
        return {"request_id": request.id, "station_id": request.station_id,
                "robot_id": request.robot_id, "status": request.status, "phase": request.phase,
                "target_percent": request.target_percent}

    def request(self, station_id, robot_id, time, geometry, target_percent=None):
        if station_id not in self.elements or robot_id not in self.robots:
            raise ValueError("없는 충전소 또는 로봇")
        if not _number(time) or time < self.time:
            raise ValueError("예약 시각은 현재 이후의 유한한 시각이어야 합니다")
        # A target belongs to this reservation. An omitted target on a retry
        # preserves its original value, including an explicitly higher target.
        if target_percent is not None:
            if (not isinstance(target_percent, (int, float)) or isinstance(target_percent, bool)
                    or not self.charge_until <= target_percent <= 100
                    or not math.isfinite(target_percent)):
                raise ValueError("충전 목표는 설정 종료 기준 이상, 100 이하의 유한한 수여야 합니다")
            target_percent = float(target_percent)
        if not isinstance(geometry, dict) or set(geometry) != {"staging", "target"}:
            raise ValueError("staging과 target 충전 좌표가 필요합니다")
        geometry = {key: _pose(geometry[key]) for key in ("staging", "target")}
        staging, target = geometry["staging"], geometry["target"]
        if math.hypot(staging["x"]-target["x"], staging["y"]-target["y"]) < .25 or abs(staging["z"]-target["z"]) > .15:
            raise ValueError("대기점은 같은 높이에서 접점 목표와 0.25m 이상 떨어져야 합니다")
        for old in self.requests.values():
            if old.robot_id == robot_id and old.status not in ("completed", "cancelled"):
                if old.station_id != station_id or old.geometry != geometry:
                    raise ValueError("로봇에 다른 활성 충전 예약이 있습니다")
                if target_percent is not None and old.target_percent != target_percent:
                    raise ValueError("활성 충전 예약의 목표는 변경할 수 없습니다")
                return self._receipt(old)
        element, robot = self.elements[station_id], self.robots[robot_id]
        model = model_by_id(robot.model_id)
        if model["locomotion"] not in ("differential", "guided"):
            raise ValueError("연구용 바퀴 로봇 충전 커넥터만 지원합니다")
        observed_station = self._station_observations.get(station_id)
        station_fault = observed_station["fault"] if observed_station and time-observed_station["sampled_at"] <= self.stale_after else element.facility.fault
        if station_fault or not element.facility.automatic or self.stations[station_id].fault_latched:
            raise ValueError("충전소가 사용 불가하거나 명시적 복구가 필요합니다")
        if element.allowed_groups and robot.group not in element.allowed_groups:
            raise ValueError("충전소가 로봇 그룹을 허용하지 않습니다")
        observed = self._robot_observations.get(robot_id)
        if observed and time-observed["sampled_at"] > self.stale_after:
            raise ValueError("로봇의 현재 층을 확인할 신선한 관측이 없습니다")
        if (observed.get("fault", "none") if observed else robot.fault) != "none" or (observed and observed.get("operator_hold", False)):
            raise ValueError("고장·정지 로봇은 충전 예약 전에 복구해야 합니다")
        observed_floor = robot.floor_id
        if observed:
            # Current ObservationBus has no floor_id. Research wheeled bodies
            # use a nominal 0.3 m base origin; reject unsupported midair heights.
            observed_floor = min(self.floors, key=lambda fid: abs(self.floors[fid]-(observed["pose"]["z"]-.3)))
            if abs(self.floors[observed_floor]-(observed["pose"]["z"]-.3)) > .75:
                raise ValueError("관측 높이에서 지원되는 층을 확인할 수 없습니다")
        if observed_floor != element.floor_id:
            raise ValueError("충전소와 로봇의 층이 다릅니다")
        if observed and abs(observed["pose"]["z"]-target["z"]) > .75:
            raise ValueError("로봇 관측 높이와 충전 목표 높이가 다릅니다")
        if robot.payload_mass > model["max_payload"]:
            raise ValueError("로봇 연구 모델의 적재 한도를 초과했습니다")
        total_mass = model["mass"] + robot.payload_mass + sum(e.mass for e in robot.equipment)
        if total_mass > element.facility.max_load:
            raise ValueError("충전소의 연구용 허용 하중을 초과했습니다")
        self.sequence += 1
        req = ChargeRequest(f"{station_id}:{robot_id}:{self.sequence}", station_id, robot_id,
                            deepcopy(geometry), float(time),
                            self.charge_until if target_percent is None else target_percent,
                            minimum_stamp=float(time))
        self.requests[req.id] = req
        self.stations[station_id].queue.append(req)
        return self._receipt(req)

    def cancel(self, station_id, robot_id):
        state = self.stations[station_id]
        for req in list(state.queue):
            if req.robot_id == robot_id:
                state.queue.remove(req)
                req.status, req.phase, req.reason = "cancelled", "cancelled", "대기 예약 취소"
                return True
        if state.active and state.active.robot_id == robot_id:
            state.active.cancel_requested = True
            self._fault(state, "cancelled_requires_recovery")
            return True
        return any(r.station_id == station_id and r.robot_id == robot_id and r.status == "cancelled"
                   for r in self.requests.values())

    def interrupt(self, station_id, robot_id, reason="operator_hold"):
        state = self.stations[station_id]
        if state.active and state.active.robot_id == robot_id:
            self._fault(state, str(reason))
            return True
        for req in list(state.queue):
            if req.robot_id == robot_id:
                # Removing a waiting request must not move it or later start it.
                state.queue.remove(req)
                req.status, req.phase, req.reason = "cancelled", "cancelled", str(reason)
                return True
        return False

    def recover(self, station_id, robot_id=None):
        state = self.stations[station_id]
        if robot_id is not None and (not state.active or state.active.robot_id != robot_id):
            return False
        if not state.fault_latched:
            return False
        state.fault, state.fault_latched = None, False
        if state.active:
            req = state.active
            phase = "undock" if req.cancel_requested else req.resume_phase
            if phase == "charging":
                phase = "dock"  # Reconfirm both contacts after interruption.
            req.minimum_stamp = self.time
            self._phase(state, phase, self.time)
            req.reason = "명시적 복구 후 양쪽 새 관측 대기"
        else:
            state.phase = "idle"
        return True

    @staticmethod
    def _fault(state, reason):
        if state.active:
            req = state.active
            if req.phase != "fault":
                req.resume_phase = req.phase
            req.phase, req.status, req.reason = "fault", "interrupted", reason
            req.robot_stable_since = req.station_stable_since = None
        state.phase, state.fault, state.fault_latched = "fault", reason, True

    @staticmethod
    def _phase(state, phase, now):
        req = state.active
        req.motion_generation += 1
        req.handoff_pending = False
        req.stop_delivered_at = None
        state.phase = req.phase = phase
        req.status = "running"
        req.phase_since = now
        req.robot_stable_since = req.station_stable_since = req.near_since = None

    def motion_token(self, robot_id):
        """Receipt fencing only; a token is not physical movement permission."""
        for station in self.stations.values():
            if station.active and station.active.robot_id == robot_id:
                req = station.active
                return (req.id, req.motion_generation, req.phase)
        return None

    def acknowledge_handoff_stop(self, robot_id, token, delivered_at):
        """Called only after the normal command queue delivered a zero command."""
        if not _number(delivered_at) or token != self.motion_token(robot_id):
            return False
        for station in self.stations.values():
            req = station.active
            if req and req.robot_id == robot_id and req.phase == "undock" and req.handoff_pending:
                if delivered_at < req.minimum_stamp:
                    return False
                if req.stop_delivered_at is None:
                    req.stop_delivered_at = delivered_at
                    req.minimum_stamp = delivered_at
                    req.robot_stable_since = req.station_stable_since = None
                return True
        return False

    def _stream(self, key, obs, now):
        if not isinstance(obs, dict) or not _number(obs.get("sampled_at")):
            return False, False, "missing_or_invalid_observation"
        stamp = float(obs["sampled_at"])
        if stamp > now + 1e-9:
            return False, False, "future_observation"
        if now-stamp > self.stale_after + 1e-9:
            return False, False, "stale_observation"
        try:
            fingerprint = json.dumps(obs, sort_keys=True, allow_nan=False, separators=(",", ":"))
        except (ValueError, TypeError):
            return False, False, "invalid_observation"
        previous = self._stream_history.get(key)
        if previous and stamp < previous[0]:
            return False, False, "out_of_order_observation"
        if previous and stamp == previous[0]:
            if fingerprint != previous[1]:
                return False, False, "altered_duplicate_observation"
            return True, False, None
        self._stream_history[key] = (stamp, fingerprint)
        return True, True, None

    @staticmethod
    def _connector(connector):
        if not isinstance(connector, dict):
            return False
        return (all(type(connector.get(k)) is bool for k in ("left", "right", "aligned"))
                and all(_number(connector.get(k)) and connector[k] >= 0 for k in ("normal_force", "relative_speed")))

    def _contact(self, connector):
        return (self._connector(connector) and connector["left"] and connector["right"]
                and connector["aligned"] and connector["normal_force"] >= self.minimum_force
                and connector["relative_speed"] <= self.stopped_speed)

    @staticmethod
    def _clear(connector):
        return not connector["left"] and not connector["right"] and connector["normal_force"] < .1

    def _valid_robot(self, obs, rid):
        try:
            _pose(obs["pose"])
            for key in ("velocity", "angular_velocity"):
                value = obs[key]
                if not isinstance(value, (list, tuple)) or len(value) != 3 or not all(_number(v) for v in value):
                    return False
            return (obs.get("robot_id", rid) == rid and _number(obs.get("battery"))
                    and 0 <= obs["battery"] <= 100 and isinstance(obs.get("sensors"), dict))
        except (KeyError, TypeError, ValueError):
            return False

    def _stopped(self, obs):
        return (math.sqrt(sum(v*v for v in obs["velocity"])) <= self.stopped_speed
                and math.sqrt(sum(v*v for v in obs["angular_velocity"])) <= self.stopped_angular_speed)

    def _near(self, obs, target):
        pose = obs["pose"]
        yaw_error = abs((pose["yaw"]-target["yaw"]+math.pi) % (2*math.pi)-math.pi)
        return (math.hypot(pose["x"]-target["x"], pose["y"]-target["y"]) <= self.position_tolerance
                and abs(pose["z"]-target["z"]) <= .15 and yaw_error <= self.yaw_tolerance)

    def _confirmed(self, req, condition, robot_obs, station_obs, robot_new, station_new):
        if not condition:
            req.robot_stable_since = req.station_stable_since = None
            return False
        if robot_new and req.robot_stable_since is None:
            req.robot_stable_since = robot_obs["sampled_at"]
        if station_new and req.station_stable_since is None:
            req.station_stable_since = station_obs["sampled_at"]
        return ((robot_new or station_new) and req.robot_stable_since is not None
                and req.station_stable_since is not None
                and robot_obs["sampled_at"]-req.robot_stable_since >= self.confirmation_time-1e-9
                and station_obs["sampled_at"]-req.station_stable_since >= self.confirmation_time-1e-9)

    @staticmethod
    def _intention(req, action, reason=None, target=None):
        result = {"action": action, "phase": req.phase, "reason": reason or req.reason,
                  "station_id": req.station_id, "request_id": req.id,
                  "target_percent": req.target_percent}
        if target is not None:
            result["target"] = deepcopy(target)
        return result

    def update(self, now, robot_observations, station_observations):
        if not _number(now) or now < self.time:
            raise ValueError("관측 갱신 시각은 단조 증가하는 유한한 시각이어야 합니다")
        self.time = float(now)
        if not self.elements:
            return {"robot_intentions": {}, "states": {}, "power_requests": {}}
        intentions, powers, states = {}, {}, {}
        robot_checks = {}
        for rid in self.robots:
            obs = robot_observations.get(rid)
            valid, fresh, error = self._stream(("robot", rid), obs, now)
            if valid and not self._valid_robot(obs, rid):
                valid, error = False, "invalid_robot_observation"
            robot_checks[rid] = valid, fresh, error
            if valid:
                self._robot_observations[rid] = deepcopy(obs)
        for eid, state in self.stations.items():
            station_obs = station_observations.get(eid)
            station_ok, station_new, station_error = self._stream(("station", eid), station_obs, now)
            contacts = station_obs.get("contacts") if isinstance(station_obs, dict) else None
            if station_ok and (not isinstance(contacts, dict) or type(station_obs.get("fault")) is not bool
                               or any(not isinstance(rid, str) or not self._connector(conn) for rid, conn in contacts.items())):
                station_ok, station_error = False, "invalid_station_observation"
            if station_ok:
                self._station_observations[eid] = deepcopy(station_obs)
                state.occupants = sorted(rid for rid, conn in contacts.items() if conn["left"] or conn["right"] or conn["normal_force"] >= self.minimum_force)
                if station_obs["fault"]:
                    self._fault(state, "station_fault")
                expected = {state.active.robot_id} if state.active else set()
                if set(state.occupants)-expected:
                    self._fault(state, "unreserved_contact")
            elif state.active:
                self._fault(state, station_error)
            if not state.active and state.queue and station_ok and not state.fault_latched and not state.occupants:
                state.active = state.queue.popleft()
                self._phase(state, "approach", now)
            for queued in state.queue:
                intentions[queued.robot_id] = self._intention(queued, "hold")
                powers[queued.robot_id] = {"station_id": eid, "power_w": 0.}
            req = state.active
            if req:
                rid = req.robot_id
                powers[rid] = {"station_id": eid, "power_w": 0.}
                robot_obs = robot_observations.get(rid)
                robot_ok, robot_new, robot_error = robot_checks[rid]
                if robot_ok:
                    if robot_obs.get("fault", "none") != "none" or robot_obs.get("operator_hold", False):
                        self._fault(state, "operator_hold" if robot_obs.get("operator_hold") else "robot_fault")
                else:
                    self._fault(state, robot_error)
                if state.fault_latched:
                    intentions[rid] = self._intention(req, "fault")
                elif not station_ok or not robot_ok:
                    intentions[rid] = self._intention(req, "hold", "양쪽 정상 관측 대기")
                elif min(robot_obs["sampled_at"], station_obs["sampled_at"]) <= req.minimum_stamp:
                    intentions[rid] = self._intention(req, "hold", "예약·복구 이후 양쪽 새 관측 대기")
                else:
                    docking = robot_obs["sensors"].get("docking")
                    connector = docking.get(eid) if isinstance(docking, dict) else None
                    station_connector = contacts.get(rid)
                    if not self._connector(connector) or not self._connector(station_connector):
                        self._fault(state, "missing_or_invalid_connector")
                        intentions[rid] = self._intention(req, "fault")
                    elif now-req.phase_since > self.phase_timeouts[req.phase]:
                        self._fault(state, req.phase+"_timeout")
                        intentions[rid] = self._intention(req, "fault")
                    else:
                        self._advance(state, req, now, robot_obs, station_obs, connector,
                                      station_connector, robot_new, station_new, intentions, powers)
            states[eid] = {"phase": state.phase, "queue": [r.robot_id for r in state.queue],
                           "reserved_by": [state.active.robot_id] if state.active else [],
                           "occupants": list(state.occupants), "fault": state.fault,
                           "fault_latched": state.fault_latched,
                           "requests": [self._receipt(r) for r in self.requests.values() if r.station_id == eid],
                           "sensor_model": station_obs.get("sensor_model") if isinstance(station_obs, dict) else None,
                           "workflow_version": VERSION,
                           "stop_pending": bool(state.active and state.active.handoff_pending)}
        for req in reversed(list(self.requests.values())):
            if req.status in ("completed", "cancelled") and req.robot_id not in intentions:
                intentions[req.robot_id] = self._intention(req, "done")
                powers[req.robot_id] = {"station_id": req.station_id, "power_w": 0.}
        return {"robot_intentions": intentions, "states": states, "power_requests": powers}

    def _advance(self, state, req, now, obs, station_obs, connector, station_connector,
                 robot_new, station_new, intentions, powers):
        rid = req.robot_id
        both_contact = self._contact(connector) and self._contact(station_connector)
        stopped = self._stopped(obs)
        target, staging = req.geometry["target"], req.geometry["staging"]
        if req.phase == "approach":
            req.reason = "충전 대기점 접근"
            if self._confirmed(req, self._near(obs, staging) and stopped, obs, station_obs, robot_new, station_new):
                self._phase(state, "dock", now)
        elif req.phase == "dock":
            req.reason = "양측 실제 접촉·정렬·정지 확인"
            safe = both_contact and stopped and self._near(obs, target)
            if self._confirmed(req, safe, obs, station_obs, robot_new, station_new):
                self._phase(state, "charging", now)
            elif self._near(obs, target) and not both_contact:
                if req.near_since is None:
                    req.near_since = now
                elif now-req.near_since >= self.near_contact_timeout:
                    self._fault(state, "contact_timeout")
            else:
                req.near_since = None
        elif req.phase == "charging":
            req.reason = "양쪽 접점 관측 유지·충전 전력 요청"
            if not both_contact or not stopped or not self._near(obs, target):
                self._fault(state, "contact_or_alignment_lost")
            elif obs["battery"] >= req.target_percent:
                self._phase(state, "undock", now)
        elif req.phase == "undock" and not req.handoff_pending:
            req.reason = "전력 차단·대기점 후진·실제 양측 분리 확인"
            safe = self._near(obs, staging) and stopped and self._clear(connector) and self._clear(station_connector)
            if self._confirmed(req, safe, obs, station_obs, robot_new, station_new):
                original_since = req.phase_since
                self._phase(state, "undock", now)
                req.phase_since = original_since  # Preserve the original undock timeout.
                req.minimum_stamp = now
                req.handoff_pending = True
        elif req.phase == "undock" and req.handoff_pending:
            req.reason = "후진 명령 종료 전달·새 분리 정지 관측 확인"
            safe = (req.stop_delivered_at is not None and self._near(obs, staging)
                    and stopped and self._clear(connector) and self._clear(station_connector))
            if self._confirmed(req, safe, obs, station_obs, robot_new, station_new):
                req.status = "cancelled" if req.cancel_requested else "completed"
                req.phase, req.reason = "done", "충전 예약 분리·정지 명령 확인 후 반납 완료"
                state.active, state.phase = None, "idle"
        if req.phase == "charging" and obs["battery"] >= req.target_percent:
            self._phase(state, "undock", now)
        action = {"approach": "approach", "dock": "dock", "charging": "hold", "undock": "undock", "done": "done", "fault": "fault"}[req.phase]
        if req.handoff_pending and req.phase == "undock":action = "hold"
        move_target = staging if action in ("approach", "undock") else target if action == "dock" else None
        intentions[rid] = self._intention(req, action, target=move_target)
        if req.phase == "charging" and not state.fault_latched and both_contact and stopped:
            powers[rid]["power_w"] = float(getattr(self.elements[req.station_id].facility, "charge_power_w", 400.))
