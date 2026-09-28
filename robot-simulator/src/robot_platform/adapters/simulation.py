"""Simulation binding to the common adapter contract, with no synthetic successes."""

from __future__ import annotations

from dataclasses import dataclass
import json
import math
from threading import RLock
import time
from typing import Any, Callable, Protocol

from .contracts import (
    CommandFeedback, CommandStatus, ConnectionStatus, RobotCapabilities,
    RobotCommand, RobotObservation,
)
from .journal import CommandJournal


class SimulationRuntime(Protocol):
    """Implementations must expose delivered sensor observations, never simulator truth."""
    def command(self, robot_id: str, kind: str, target: dict | None = None,
                *, expires_at: float | None = None) -> dict: ...
    def robot_observation(self, robot_id: str) -> dict: ...
    def command_feedback(self, command_id: str | int) -> dict: ...


class ObservationUnavailable(RuntimeError):
    pass


@dataclass(frozen=True)
class SimulationAdapterConfig:
    robot_id: str
    run_id: str
    heartbeat_timeout_s: float = 5.0
    max_observation_age_sim_s: float = 1.0
    max_command_horizon_s: float = 300.0

    def __post_init__(self):
        if not self.robot_id or not self.run_id:
            raise ValueError("robot_id and run_id required")
        for value in (self.heartbeat_timeout_s, self.max_observation_age_sim_s, self.max_command_horizon_s):
            if not math.isfinite(value) or value <= 0:
                raise ValueError("time limits must be finite and positive")


class SimulationAdapter:
    SUPPORTED = frozenset({"stand", "sit", "stop", "navigate"})
    TERMINAL = frozenset({CommandStatus.SUCCEEDED, CommandStatus.FAILED, CommandStatus.REJECTED,
                          CommandStatus.UNKNOWN, CommandStatus.EXPIRED})

    def __init__(self, runtime: SimulationRuntime, config: SimulationAdapterConfig,
                 capabilities: RobotCapabilities, journal: CommandJournal | None = None,
                 clock: Callable[[], float] = time.time,
                 monotonic: Callable[[], float] = time.monotonic):
        if capabilities.robot_id != config.robot_id:
            raise ValueError("capabilities robot_id mismatch")
        self.runtime, self.config = runtime, config
        self._capabilities = RobotCapabilities(
            capabilities.robot_id, capabilities.manufacturer, capabilities.model,
            capabilities.serial_number, capabilities.commands & self.SUPPORTED,
            capabilities.frames & frozenset({"world", "body"}), capabilities.hardware,
            capabilities.validation)
        self.journal = journal or CommandJournal()
        self.scope = json.dumps(["simulation", config.run_id, config.robot_id], separators=(",", ":"))
        self._clock, self._monotonic = clock, monotonic
        self._epoch = 0
        self._status = ConnectionStatus.DISCONNECTED
        self._last_heartbeat = -math.inf
        self._lock = RLock()
        self._last_observation: RobotObservation | None = None
        self._observation_sequence = 0
        self._last_sim_time = -math.inf
        self._pending: dict[str, tuple[RobotCommand, float]] = {}

    @property
    def status(self) -> ConnectionStatus:
        with self._lock:
            if (self._status in (ConnectionStatus.OBSERVING, ConnectionStatus.CONTROLLING)
                    and self._monotonic() - self._last_heartbeat > self.config.heartbeat_timeout_s):
                self._lose("heartbeat_timeout")
            return self._status

    @property
    def connection_epoch(self) -> int:
        return self._epoch

    def _lose(self, reason: str):
        self._status = ConnectionStatus.LOST
        for cid in list(self._pending):
            previous = self.journal.lookup(self.scope, cid)
            if previous and previous.status not in self.TERMINAL:
                self.journal.update(self.scope, CommandFeedback(cid, CommandStatus.UNKNOWN,
                    self._clock(), reason, previous.vendor_command_id, previous.connection_epoch))

    def connect(self) -> RobotCapabilities:
        with self._lock:
            if self._status not in (ConnectionStatus.DISCONNECTED, ConnectionStatus.LOST):
                raise RuntimeError("already connected")
            self._epoch = self.journal.new_epoch(self.scope, self._clock())
            self._last_observation = None
            self._pending.clear()
            self._last_heartbeat = self._monotonic()
            self._status = ConnectionStatus.OBSERVING
            try:
                self.observe()
            except Exception:
                self._status = ConnectionStatus.LOST
                raise
            return self._capabilities

    def acquire_control(self) -> None:
        with self._lock:
            if self.status != ConnectionStatus.OBSERVING:
                raise RuntimeError("connect before acquiring simulation control")
            self._status = ConnectionStatus.CONTROLLING

    def discover(self) -> RobotCapabilities:
        if self.status in (ConnectionStatus.DISCONNECTED, ConnectionStatus.LOST):
            raise RuntimeError("not connected")
        return self._capabilities

    def disconnect(self) -> None:
        with self._lock:
            self._lose("disconnected_completion_unconfirmed")
            self._status = ConnectionStatus.DISCONNECTED

    def reconnect(self) -> RobotCapabilities:
        self.disconnect()
        return self.connect()

    def _reject(self, command: RobotCommand, reason: str) -> CommandFeedback:
        return CommandFeedback(command.command_id, CommandStatus.REJECTED,
                               self._clock(), reason, connection_epoch=self._epoch)

    def _validate(self, c: RobotCommand) -> str | None:
        now = self._clock()
        if not c.command_id or c.robot_id != self.config.robot_id:
            return "robot_or_command_id_invalid"
        if not isinstance(c.sequence, int) or isinstance(c.sequence, bool) or c.sequence < 0:
            return "invalid_sequence"
        if c.connection_epoch != self._epoch:
            return "stale_connection_epoch"
        if not all(math.isfinite(t) for t in (c.issued_at, c.expires_at)):
            return "invalid_timestamp"
        if c.issued_at > now + .5:
            return "future_command"
        if c.expires_at <= max(now, c.issued_at):
            return "expired_command"
        if c.expires_at - now > self.config.max_command_horizon_s:
            return "command_horizon_exceeded"
        if c.kind not in self._capabilities.commands:
            return "unsupported_command"
        if c.kind == "navigate":
            if c.frame != "world":
                return "navigation_requires_world_frame"
            if not {"x_m", "y_m", "yaw_rad"} <= set(c.parameters) <= {"x_m", "y_m", "z_m", "yaw_rad"}:
                return "invalid_parameters"
            if any(not isinstance(v, (float, int)) or isinstance(v, bool) or not math.isfinite(v)
                   for v in c.parameters.values()):
                return "invalid_parameters"
        elif c.frame != "body" or c.parameters:
            return "invalid_parameters"
        return None

    def submit(self, command: RobotCommand) -> CommandFeedback:
        with self._lock:
            try:
                previous = self.journal.duplicate(self.scope, command, self._clock())
            except (ValueError, TypeError):
                return self._reject(command, "non_serializable_or_non_finite_command")
            if previous:
                return previous
            reason = self._validate(command)
            if reason:
                return self._reject(command, reason)
            if self.status != ConnectionStatus.CONTROLLING:
                return self._reject(command, "control_not_held")
            try:
                observation = self.observe()
            except ObservationUnavailable as exc:
                return self._reject(command, str(exc))
            if observation.estopped or not observation.powered or observation.faults:
                return self._reject(command, "robot_not_ready")
            claim = self.journal.reserve(self.scope, command, self._clock())
            if not claim.dispatch:
                return claim.feedback
            self._pending[command.command_id] = (command, self._last_sim_time)
            target = None
            if command.kind == "navigate":
                p = command.parameters
                target = {"x": p["x_m"], "y": p["y_m"], "yaw": p["yaw_rad"],
                          "z": p.get("z_m", observation.position_m[2])}
            try:
                response = self.runtime.command(self.config.robot_id,
                    "move" if command.kind == "navigate" else command.kind, target,
                    expires_at=command.expires_at)
                vendor_id = response.get("command_id")
                if not isinstance(vendor_id, (str, int)) or isinstance(vendor_id, bool):
                    result = CommandFeedback(command.command_id, CommandStatus.UNKNOWN,
                        self._clock(), "runtime_command_id_missing", connection_epoch=self._epoch)
                else:
                    status = CommandStatus.REJECTED if response.get("status") == "rejected" else CommandStatus.ACCEPTED
                    result = CommandFeedback(command.command_id, status, self._clock(),
                        response.get("reason", "awaiting_physical_feedback"), vendor_id, self._epoch)
            except ValueError as exc:
                result = self._reject(command, str(exc))
            except Exception as exc:
                self._lose("runtime_dispatch_outcome_unknown")
                result = CommandFeedback(command.command_id, CommandStatus.UNKNOWN, self._clock(),
                    f"runtime_dispatch_outcome_unknown:{type(exc).__name__}", connection_epoch=self._epoch)
            return self.journal.update(self.scope, result)

    def poll_feedback(self, command_id: str) -> CommandFeedback:
        with self._lock:
            previous = self.journal.lookup(self.scope, command_id)
            if previous is None:
                raise KeyError(command_id)
            if previous.status in self.TERMINAL:
                return previous
            if self.status != ConnectionStatus.CONTROLLING or previous.connection_epoch != self._epoch:
                self._lose("session_or_control_changed")
                return self.journal.lookup(self.scope, command_id)
            command, submitted_sim_time = self._pending[command_id]
            try:
                response = self.runtime.command_feedback(previous.vendor_command_id)
                if response.get("command_id") != previous.vendor_command_id:
                    raise ValueError("runtime_feedback_id_mismatch")
                name = response.get("status")
                status = {"accepted": CommandStatus.ACCEPTED, "running": CommandStatus.RUNNING,
                          "executing": CommandStatus.RUNNING,
                          "completed": CommandStatus.SUCCEEDED, "succeeded": CommandStatus.SUCCEEDED,
                          "rejected": CommandStatus.REJECTED, "failed": CommandStatus.FAILED,
                          "cancelled": CommandStatus.FAILED, "expired": CommandStatus.EXPIRED,
                          "unknown": CommandStatus.UNKNOWN}.get(name, CommandStatus.UNKNOWN)
                reason = response.get("reason", str(name))
                if status == CommandStatus.SUCCEEDED:
                    evidence = response.get("evidence", {})
                    sample = evidence.get("sampled_at", -math.inf)
                    if (evidence.get("source") != "observation" or not evidence.get("criterion")
                            or not isinstance(sample, (int, float)) or not math.isfinite(sample)
                            or sample <= submitted_sim_time):
                        status, reason = CommandStatus.UNKNOWN, "physical_completion_evidence_missing"
                result = CommandFeedback(command_id, status, self._clock(), reason,
                                         previous.vendor_command_id, self._epoch)
            except Exception as exc:
                self._lose("runtime_feedback_unavailable")
                result = CommandFeedback(command_id, CommandStatus.UNKNOWN, self._clock(),
                    f"runtime_feedback_unavailable:{type(exc).__name__}", previous.vendor_command_id, self._epoch)
            return self.journal.update(self.scope, result)

    def observe(self) -> RobotObservation:
        with self._lock:
            if self.status in (ConnectionStatus.DISCONNECTED, ConnectionStatus.LOST):
                raise ObservationUnavailable("not_connected")
            try:
                raw = self.runtime.robot_observation(self.config.robot_id)
            except Exception as exc:
                self._lose("runtime_observation_unavailable")
                raise ObservationUnavailable(f"runtime_observation_unavailable:{type(exc).__name__}") from exc
            required = {"sampled_at", "received_at", "simulation_time", "pose", "powered", "estopped"}
            if not isinstance(raw, dict) or not required <= raw.keys():
                raise ObservationUnavailable("observation_fields_missing")
            source_time, received_sim, sim_time = raw["sampled_at"], raw["received_at"], raw["simulation_time"]
            if not all(isinstance(t, (int, float)) and math.isfinite(t) for t in (source_time, received_sim, sim_time)):
                raise ObservationUnavailable("invalid_observation_timestamp")
            if source_time > received_sim + 1e-9 or received_sim > sim_time + 1e-9:
                raise ObservationUnavailable("future_observation")
            if sim_time - source_time > self.config.max_observation_age_sim_s:
                raise ObservationUnavailable("stale_observation")
            self._last_sim_time = sim_time
            if self._last_observation:
                if source_time < self._last_observation.acquired_at_robot:
                    raise ObservationUnavailable("out_of_order_observation")
                if source_time == self._last_observation.acquired_at_robot:
                    self._last_heartbeat = self._monotonic()
                    return self._last_observation
            pose = raw["pose"]
            if not isinstance(pose, dict) or not {"x", "y", "z"} <= pose.keys():
                raise ObservationUnavailable("position_missing")
            position = tuple(pose[k] for k in ("x", "y", "z"))
            if not all(isinstance(v, (int, float)) and math.isfinite(v) for v in position):
                raise ObservationUnavailable("invalid_position")
            if not isinstance(raw["powered"], bool) or not isinstance(raw["estopped"], bool):
                raise ObservationUnavailable("invalid_power_or_estop_state")
            q = raw.get("quaternion")
            orientation = (q[1], q[2], q[3], q[0]) if q is not None and len(q) == 4 else None
            fault = raw.get("fault")
            faults = () if fault in (None, "none") else (str(fault),)
            battery = raw.get("battery")
            self._observation_sequence += 1
            observation = RobotObservation(
                self.config.robot_id, self._observation_sequence, self._epoch, self._clock(),
                source_time, None, "world", position, orientation,
                tuple(raw["velocity"]) if raw.get("velocity") is not None else None,
                tuple(raw["angular_velocity"]) if raw.get("angular_velocity") is not None else None,
                battery / 100 if battery is not None else None, raw["powered"], raw["estopped"],
                raw.get("joints", {}), faults,
                {"source": "delivered_simulation_observation", "simulation_time": sim_time,
                 "received_at_sim": received_sim, "sensors": raw.get("sensors", {})}, "simulation")
            self._last_observation = observation
            self._last_heartbeat = self._monotonic()
            return observation

    def heartbeat(self) -> RobotObservation:
        return self.observe()
