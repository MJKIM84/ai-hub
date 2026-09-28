"""Spot transport state machine. Construction has no network or motion side effects."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
import json
import math
from threading import RLock
import time
from typing import Callable

from .contracts import (
    CommandFeedback, CommandStatus, ConnectionStatus, RobotCapabilities,
    RobotCommand, RobotObservation,
)
from .spot_sdk import BosdynSDKFacade, RemoteRejected, SpotSDKFacade, TransportFailure


@dataclass(frozen=True)
class SpotCredentials:
    username: str
    password: str = field(repr=False)


@dataclass(frozen=True)
class SpotAdapterConfig:
    robot_id: str
    host: str
    expected_serial: str | None = None
    rpc_timeout_s: float = 5.0
    heartbeat_timeout_s: float = 5.0
    max_observation_age_s: float = 2.0
    max_future_clock_s: float = 0.5
    max_command_horizon_s: float = 10.0
    # Deployment guardrails, not manufacturer capability claims.
    max_linear_speed_mps: float = 0.5
    max_angular_speed_rps: float = 0.5
    stop_linear_tolerance_mps: float = 0.02
    stop_angular_tolerance_rps: float = 0.03

    def __post_init__(self):
        if not self.robot_id or not self.host:
            raise ValueError("robot_id and host are required")
        for key, value in asdict(self).items():
            if isinstance(value, (int, float)) and (not math.isfinite(value) or value <= 0):
                raise ValueError(f"{key} must be finite and positive")


class SpotAdapter:
    COMMANDS = frozenset({"stand", "sit", "stop", "velocity", "navigate"})
    TERMINAL = frozenset({CommandStatus.SUCCEEDED, CommandStatus.REJECTED,
                          CommandStatus.FAILED, CommandStatus.EXPIRED, CommandStatus.UNKNOWN})

    def __init__(self, config: SpotAdapterConfig, sdk: SpotSDKFacade | None = None,
                 clock: Callable[[], float] = time.time,
                 monotonic: Callable[[], float] = time.monotonic):
        self.config = config
        self._sdk = sdk or BosdynSDKFacade(
            config.max_linear_speed_mps, config.max_angular_speed_rps,
            self._application_is_live)
        self._clock, self._monotonic = clock, monotonic
        self._lock = RLock()
        self._status = ConnectionStatus.DISCONNECTED
        self._epoch = 0
        self._capabilities: RobotCapabilities | None = None
        self._last_heartbeat = -math.inf
        self._last_sequence = -1
        self._observation_sequence = 0
        self._last_source_time = -math.inf
        self._commands: dict[str, RobotCommand] = {}
        self._fingerprints: dict[str, str] = {}
        self._feedback: dict[str, CommandFeedback] = {}
        self.events: list[dict] = []

    def _application_is_live(self) -> bool:
        # Called from the SDK keepalive thread. Do not acquire our lock: shutdown
        # can wait for this thread while the main thread owns that lock.
        return (self._status in (ConnectionStatus.OBSERVING, ConnectionStatus.CONTROLLING)
                and self._monotonic() - self._last_heartbeat <= self.config.heartbeat_timeout_s)

    @property
    def status(self) -> ConnectionStatus:
        with self._lock:
            if self._status in (ConnectionStatus.OBSERVING, ConnectionStatus.CONTROLLING):
                if self._monotonic() - self._last_heartbeat > self.config.heartbeat_timeout_s:
                    self._lose("heartbeat_timeout")
            return self._status

    @property
    def connection_epoch(self) -> int:
        return self._epoch

    def _event(self, kind: str, **values) -> None:
        self.events.append({"kind": kind, "time": self._clock(), "epoch": self._epoch, **values})

    def _lose(self, reason: str) -> None:
        self._status = ConnectionStatus.LOST
        for cid, previous in list(self._feedback.items()):
            if previous.status not in self.TERMINAL:
                self._feedback[cid] = CommandFeedback(cid, CommandStatus.UNKNOWN, self._clock(),
                    reason, previous.vendor_command_id, previous.connection_epoch)
        self._event("connection_lost", reason=reason)

    def _call(self, method, *args):
        try:
            return method(*args)
        except TransportFailure as exc:
            self._lose(str(exc))
            raise

    def connect(self, credentials: SpotCredentials) -> RobotCapabilities:
        with self._lock:
            if self._status not in (ConnectionStatus.DISCONNECTED, ConnectionStatus.LOST):
                raise RuntimeError("disconnect before connecting again")
            self._epoch += 1
            self._status = ConnectionStatus.DISCONNECTED
            self._last_source_time = -math.inf
            try:
                self._call(self._sdk.connect, self.config.host, credentials.username,
                           credentials.password, self.config.rpc_timeout_s)
                hardware = self._call(self._sdk.discover)
                if self.config.expected_serial and hardware["serial_number"] != self.config.expected_serial:
                    raise RemoteRejected("serial_number_mismatch")
                commands = self.COMMANDS if "robot-command" in hardware.get("services", ()) else frozenset()
                self._capabilities = RobotCapabilities(
                    self.config.robot_id, "Boston Dynamics", hardware.get("model", "Spot"),
                    hardware["serial_number"], commands,
                    frozenset({"body", "odom", "vision"}), hardware)
                self._status = ConnectionStatus.OBSERVING
                self._last_heartbeat = self._monotonic()
                self.observe()  # Resynchronize before exposing a connected session.
                self._event("connected", serial_number=hardware["serial_number"])
                return self._capabilities
            except Exception:
                self._status = ConnectionStatus.LOST
                try:
                    self._sdk.close()
                except Exception as cleanup_error:
                    self._event("cleanup_failed", error=type(cleanup_error).__name__)
                raise

    def discover(self) -> RobotCapabilities:
        if self.status in (ConnectionStatus.DISCONNECTED, ConnectionStatus.LOST):
            raise RuntimeError("not connected")
        assert self._capabilities is not None
        return self._capabilities

    def acquire_control(self) -> None:
        with self._lock:
            if self.status != ConnectionStatus.OBSERVING:
                raise RuntimeError("control requires a synchronized observation connection")
            self._call(self._sdk.acquire)  # acquire only: never force-take another owner's lease.
            safety = self._call(self._sdk.safety)
            if not safety.lease_valid or not safety.time_synced or safety.estopped:
                self._sdk.release()
                raise RemoteRejected("control_preconditions_failed")
            self._status = ConnectionStatus.CONTROLLING
            self._event("control_acquired")

    def release_control(self) -> None:
        with self._lock:
            self._call(self._sdk.release)
            if self._status == ConnectionStatus.CONTROLLING:
                self._status = ConnectionStatus.OBSERVING
            self._event("control_released")

    def power_on(self) -> None:
        with self._lock:
            self._assert_control(require_power=False)
            self._call(self._sdk.power_on)
            if not self._call(self._sdk.safety).powered:
                raise RemoteRejected("power_on_not_confirmed")
            self._event("power_on_confirmed")

    def power_off(self) -> None:
        with self._lock:
            self._assert_control(require_power=False)
            self._call(self._sdk.power_off)
            if self._call(self._sdk.safety).powered:
                raise RemoteRejected("power_off_not_confirmed")
            self._event("power_off_confirmed")

    def _assert_control(self, require_power: bool = True) -> None:
        if self.status != ConnectionStatus.CONTROLLING:
            raise RemoteRejected("control_not_held")
        safety = self._call(self._sdk.safety)
        if not safety.lease_valid:
            self._lose("lease_lost")
            raise RemoteRejected("lease_lost")
        if not safety.time_synced:
            self._lose("time_sync_lost")
            raise RemoteRejected("time_sync_lost")
        if safety.estopped:
            raise RemoteRejected("estop_active")
        if require_power and not safety.powered:
            raise RemoteRejected("motor_power_off")

    def _validate(self, c: RobotCommand) -> str | None:
        now = self._clock()
        if not c.command_id or c.robot_id != self.config.robot_id:
            return "robot_or_command_id_invalid"
        if c.connection_epoch != self._epoch:
            return "stale_connection_epoch"
        if not isinstance(c.sequence, int) or c.sequence <= self._last_sequence:
            return "out_of_order_sequence"
        if not all(math.isfinite(t) for t in (c.issued_at, c.expires_at)):
            return "invalid_timestamp"
        if c.issued_at > now + self.config.max_future_clock_s:
            return "future_command"
        if c.expires_at <= now or c.expires_at <= c.issued_at:
            return "expired_command"
        if c.expires_at - now > self.config.max_command_horizon_s:
            return "command_horizon_exceeded"
        if c.kind not in self.COMMANDS:
            return "unsupported_command"
        if self._capabilities is None or c.kind not in self._capabilities.commands:
            return "command_service_unavailable"
        expected = {"velocity": {"vx_mps", "vy_mps", "yaw_rate_rps"},
                    "navigate": {"x_m", "y_m", "yaw_rad"}}.get(c.kind, set())
        if set(c.parameters) != expected:
            return "invalid_parameters"
        if any(not isinstance(v, (int, float)) or isinstance(v, bool) or not math.isfinite(v)
               for v in c.parameters.values()):
            return "non_finite_parameter"
        if c.kind == "navigate" and c.frame not in ("odom", "vision"):
            return "navigation_requires_fixed_frame"
        if c.kind != "navigate" and c.frame != "body":
            return "body_frame_required"
        if c.kind == "velocity":
            p = c.parameters
            if (math.hypot(p["vx_mps"], p["vy_mps"]) > self.config.max_linear_speed_mps
                    or abs(p["yaw_rate_rps"]) > self.config.max_angular_speed_rps):
                return "configured_velocity_limit_exceeded"
        return None

    def submit(self, command: RobotCommand) -> CommandFeedback:
        with self._lock:
            fingerprint = json.dumps(asdict(command), sort_keys=True, allow_nan=True)
            if command.command_id in self._fingerprints:
                if self._fingerprints[command.command_id] != fingerprint:
                    return CommandFeedback(command.command_id, CommandStatus.REJECTED,
                        self._clock(), "command_id_payload_conflict", connection_epoch=self._epoch)
                return self._feedback[command.command_id]
            reason = self._validate(command)
            if reason is None:
                try:
                    self._assert_control()
                except (RemoteRejected, TransportFailure) as exc:
                    reason = str(exc)
            self._fingerprints[command.command_id] = fingerprint
            # Snapshot user-owned mappings so later mutation cannot change a queued command.
            snapshot = RobotCommand(**json.loads(fingerprint))
            self._commands[command.command_id] = snapshot
            if reason:
                result = CommandFeedback(command.command_id, CommandStatus.REJECTED,
                    self._clock(), reason, connection_epoch=self._epoch)
            else:
                self._last_sequence = command.sequence
                # Record before the RPC: its response can be lost after robot acceptance.
                try:
                    vendor_id = self._call(self._sdk.submit, snapshot)
                    result = CommandFeedback(command.command_id, CommandStatus.ACCEPTED,
                        self._clock(), "awaiting_physical_feedback", vendor_id, self._epoch)
                except TransportFailure as exc:
                    result = CommandFeedback(command.command_id, CommandStatus.UNKNOWN,
                        self._clock(), f"submit_outcome_unknown:{exc}", connection_epoch=self._epoch)
                except RemoteRejected as exc:
                    result = CommandFeedback(command.command_id, CommandStatus.REJECTED,
                        self._clock(), str(exc), connection_epoch=self._epoch)
            self._feedback[command.command_id] = result
            self._event("command_feedback", command_id=command.command_id,
                        status=result.status, reason=result.reason)
            return result

    def poll_feedback(self, command_id: str) -> CommandFeedback:
        with self._lock:
            previous = self._feedback[command_id]
            if previous.status in self.TERMINAL:
                return previous
            c = self._commands[command_id]
            if self.status != ConnectionStatus.CONTROLLING or c.connection_epoch != self._epoch:
                self._feedback[command_id] = CommandFeedback(command_id, CommandStatus.UNKNOWN,
                    self._clock(), "control_or_session_changed_completion_unconfirmed",
                    previous.vendor_command_id, previous.connection_epoch)
                return self._feedback[command_id]
            try:
                status, reason = self._call(self._sdk.feedback, previous.vendor_command_id, c.kind)
                if status == CommandStatus.RUNNING and c.kind == "stop":
                    observation = self.observe()
                    linear, angular = observation.linear_velocity_mps, observation.angular_velocity_rps
                    if (observation.acquired_at_local >= c.issued_at and linear is not None and angular is not None
                            and math.sqrt(sum(v*v for v in linear)) <= self.config.stop_linear_tolerance_mps
                            and math.sqrt(sum(v*v for v in angular)) <= self.config.stop_angular_tolerance_rps):
                        status, reason = CommandStatus.SUCCEEDED, "measured_stationary_within_configured_tolerance"
                if status in (CommandStatus.RUNNING, CommandStatus.UNKNOWN) and self._clock() >= c.expires_at:
                    status, reason = CommandStatus.EXPIRED, "deadline_elapsed_completion_unconfirmed"
                result = CommandFeedback(command_id, status, self._clock(), reason,
                                         previous.vendor_command_id, self._epoch)
            except TransportFailure:
                return self._feedback[command_id]
            except RemoteRejected as exc:
                result = CommandFeedback(command_id, CommandStatus.FAILED, self._clock(),
                                         str(exc), previous.vendor_command_id, self._epoch)
            self._feedback[command_id] = result
            return result

    def observe(self) -> RobotObservation:
        with self._lock:
            if self.status in (ConnectionStatus.DISCONNECTED, ConnectionStatus.LOST):
                raise RuntimeError("not connected")
            raw = self._call(self._sdk.observe)
            source_time = raw["acquired_at_robot"]
            local_time = raw["acquired_at_local"]
            now = self._clock()
            if not all(math.isfinite(t) for t in (source_time, local_time)):
                raise RemoteRejected("non_finite_observation_timestamp")
            if source_time <= self._last_source_time:
                raise RemoteRejected("duplicate_or_out_of_order_observation")
            if now - local_time > self.config.max_observation_age_s:
                raise RemoteRejected("stale_observation")
            if local_time - now > self.config.max_future_clock_s:
                self._lose("observation_clock_mismatch")
                raise RemoteRejected("observation_clock_mismatch")
            self._last_source_time = source_time
            self._observation_sequence += 1
            self._last_heartbeat = self._monotonic()
            return RobotObservation(self.config.robot_id, self._observation_sequence,
                self._epoch, now, **raw)

    def heartbeat(self) -> RobotObservation:
        with self._lock:
            if self.status == ConnectionStatus.CONTROLLING:
                try:
                    self._call(self._sdk.retain)
                    self._assert_control(require_power=False)
                except RemoteRejected:
                    self._lose("lease_or_safety_heartbeat_failed")
                    raise
            return self.observe()

    def disconnect(self) -> None:
        with self._lock:
            self._lose("disconnected_completion_unconfirmed")
            try:
                self._sdk.close()
            finally:
                self._status = ConnectionStatus.DISCONNECTED
                self._event("disconnected")

    def reconnect(self, credentials: SpotCredentials) -> RobotCapabilities:
        self.disconnect()
        return self.connect(credentials)
