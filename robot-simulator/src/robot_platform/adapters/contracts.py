"""Vendor-neutral command/observation contracts. SI units; timestamps name their clock."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any, Mapping, Protocol, runtime_checkable


class CommandStatus(StrEnum):
    ACCEPTED = "accepted"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    REJECTED = "rejected"
    FAILED = "failed"
    EXPIRED = "expired"
    UNKNOWN = "unknown"


class ConnectionStatus(StrEnum):
    DISCONNECTED = "disconnected"
    OBSERVING = "observing"
    CONTROLLING = "controlling"
    LOST = "lost"


@dataclass(frozen=True)
class RobotCommand:
    command_id: str
    robot_id: str
    sequence: int
    kind: str
    issued_at: float  # UTC Unix seconds in the issuing host clock
    expires_at: float
    connection_epoch: int
    frame: str = "body"
    parameters: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class CommandFeedback:
    command_id: str
    status: CommandStatus
    observed_at: float  # local UTC Unix seconds, never simulation time
    reason: str = ""
    vendor_command_id: int | str | None = None
    connection_epoch: int = 0


@dataclass(frozen=True)
class RobotCapabilities:
    robot_id: str
    manufacturer: str
    model: str
    serial_number: str
    commands: frozenset[str]
    frames: frozenset[str]
    hardware: Mapping[str, Any] = field(default_factory=dict)
    validation: str = "contract_only_hardware_unverified"


@dataclass(frozen=True)
class RobotObservation:
    robot_id: str
    sequence: int
    connection_epoch: int
    received_at: float  # local UTC Unix seconds
    acquired_at_robot: float  # source clock, not receipt time
    acquired_at_local: float | None  # measured conversion, or None for a simulation clock
    frame: str
    position_m: tuple[float, float, float] | None
    orientation_xyzw: tuple[float, float, float, float] | None
    linear_velocity_mps: tuple[float, float, float] | None
    angular_velocity_rps: tuple[float, float, float] | None
    battery_fraction: float | None
    powered: bool
    estopped: bool
    joint_positions_rad: Mapping[str, float] = field(default_factory=dict)
    faults: tuple[str, ...] = ()
    raw: Mapping[str, Any] = field(default_factory=dict)
    clock_domain: str = "wall"


@runtime_checkable
class RobotAdapter(Protocol):
    """Adapters report commands; only physical feedback may establish completion."""

    @property
    def status(self) -> ConnectionStatus: ...
    @property
    def connection_epoch(self) -> int: ...
    def discover(self) -> RobotCapabilities: ...
    def submit(self, command: RobotCommand) -> CommandFeedback: ...
    def poll_feedback(self, command_id: str) -> CommandFeedback: ...
    def observe(self) -> RobotObservation: ...
    def heartbeat(self) -> RobotObservation: ...
    def disconnect(self) -> None: ...
