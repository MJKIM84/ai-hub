"""Lazy, replaceable facade over the unmodified Boston Dynamics Python SDK 5.2.0.

Importing this module never imports bosdyn or contacts a robot. Connections require
an explicit caller-supplied host and credentials. No E-Stop configuration is replaced.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Protocol

from .contracts import CommandStatus, RobotCommand


class TransportFailure(RuntimeError):
    """RPC outcome may be unknown; never automatically retry a motion request."""


class RemoteRejected(RuntimeError):
    """The robot rejected a request; no completion can be inferred."""


@dataclass(frozen=True)
class SafetyState:
    powered: bool
    estopped: bool
    time_synced: bool
    lease_valid: bool


class SpotSDKFacade(Protocol):
    def connect(self, host: str, username: str, password: str, timeout: float) -> None: ...
    def discover(self) -> dict[str, Any]: ...
    def safety(self) -> SafetyState: ...
    def acquire(self) -> None: ...
    def retain(self) -> None: ...
    def release(self) -> None: ...
    def power_on(self) -> None: ...
    def power_off(self) -> None: ...
    def submit(self, command: RobotCommand) -> int: ...
    def feedback(self, vendor_id: int, kind: str) -> tuple[CommandStatus, str]: ...
    def observe(self) -> dict[str, Any]: ...
    def close(self) -> None: ...


def build_command(command: RobotCommand, linear_limit: float = 0.5,
                  angular_limit: float = 0.5) -> Any:
    """Uses official builders. Input validation is in SpotAdapter before any RPC."""
    from bosdyn.client.robot_command import RobotCommandBuilder as Builder

    p = command.parameters
    if command.kind == "stand":
        return Builder.synchro_stand_command()
    if command.kind == "sit":
        return Builder.synchro_sit_command()
    if command.kind == "stop":
        return Builder.stop_command()
    if command.kind == "velocity":
        return Builder.synchro_velocity_command(
            p["vx_mps"], p["vy_mps"], p["yaw_rate_rps"], frame_name=command.frame)
    if command.kind == "navigate":
        params = Builder.mobility_params()
        # Axis bounds form a conservative square inside the configured speed disk.
        axis_limit = linear_limit / (2 ** 0.5)
        params.vel_limit.max_vel.linear.x = params.vel_limit.max_vel.linear.y = axis_limit
        params.vel_limit.max_vel.angular = angular_limit
        params.vel_limit.min_vel.linear.x = params.vel_limit.min_vel.linear.y = -axis_limit
        params.vel_limit.min_vel.angular = -angular_limit
        return Builder.synchro_se2_trajectory_point_command(
            p["x_m"], p["y_m"], p["yaw_rad"], frame_name=command.frame, params=params)
    raise ValueError(f"unsupported command: {command.kind}")


def decode_feedback(response: Any, kind: str) -> tuple[CommandStatus, str]:
    """Do not equate STATUS_PROCESSING or a command ID with completion."""
    from bosdyn.api import basic_command_pb2 as basic

    root = response.feedback
    if root.HasField("full_body_feedback"):
        status = root.full_body_feedback.status
    elif root.HasField("synchronized_feedback"):
        mobility = root.synchronized_feedback.mobility_command_feedback
        status = mobility.status
    else:
        return CommandStatus.UNKNOWN, "missing_robot_feedback"
    status_name = basic.RobotCommandFeedbackStatus.Status.Name(status)
    if status == basic.RobotCommandFeedbackStatus.STATUS_UNKNOWN:
        return CommandStatus.UNKNOWN, status_name
    if status != basic.RobotCommandFeedbackStatus.STATUS_PROCESSING:
        return CommandStatus.FAILED, status_name
    if kind == "stand" and root.HasField("synchronized_feedback"):
        if mobility.stand_feedback.status == basic.StandCommand.Feedback.STATUS_IS_STANDING:
            return CommandStatus.SUCCEEDED, "robot_reports_standing"
    if kind == "sit" and root.HasField("synchronized_feedback"):
        if mobility.sit_feedback.status == basic.SitCommand.Feedback.STATUS_IS_SITTING:
            return CommandStatus.SUCCEEDED, "robot_reports_sitting"
    if kind == "navigate" and root.HasField("synchronized_feedback"):
        trajectory = mobility.se2_trajectory_feedback
        if (trajectory.status == basic.SE2TrajectoryCommand.Feedback.STATUS_AT_GOAL
                and trajectory.body_movement_status == basic.SE2TrajectoryCommand.Feedback.BODY_STATUS_SETTLED):
            return CommandStatus.SUCCEEDED, "robot_reports_goal_and_settled"
    # Stop has no completion payload; the adapter additionally checks measured velocity.
    # Velocity is a streaming/expiring intent and has no SDK success terminal state.
    return CommandStatus.RUNNING, status_name


class BosdynSDKFacade:
    def __init__(self, linear_limit: float = 0.5, angular_limit: float = 0.5,
                 liveness_guard: Callable[[], bool] | None = None) -> None:
        self.robot = None
        self._keepalive = None
        self._lease_error: Exception | None = None
        self.timeout = 5.0
        self.linear_limit, self.angular_limit = linear_limit, angular_limit
        self.liveness_guard = liveness_guard

    def _rpc(self, callback, *args, **kwargs):
        from bosdyn.client.exceptions import RpcError, ResponseError
        try:
            return callback(*args, **kwargs)
        except RpcError as exc:
            raise TransportFailure(type(exc).__name__) from exc
        except ResponseError as exc:
            raise RemoteRejected(type(exc).__name__) from exc

    def connect(self, host: str, username: str, password: str, timeout: float) -> None:
        try:
            import bosdyn.client
            from bosdyn.client.lease import LeaseClient
            from bosdyn.client.robot_command import RobotCommandClient
            from bosdyn.client.robot_state import RobotStateClient
        except ImportError as exc:
            raise RuntimeError("Install optional dependency bosdyn-client==5.2.0") from exc
        self.timeout = timeout
        self.robot = bosdyn.client.create_standard_sdk("robot-platform").create_robot(host)
        self._rpc(self.robot.authenticate, username, password, timeout=timeout)
        self._rpc(self.robot.time_sync.wait_for_sync, timeout_sec=timeout)
        self._rpc(self.robot.sync_with_directory)
        self._state = self.robot.ensure_client(RobotStateClient.default_service_name)
        self._command = self.robot.ensure_client(RobotCommandClient.default_service_name)
        self._lease = self.robot.ensure_client(LeaseClient.default_service_name)

    def discover(self) -> dict[str, Any]:
        rid = self._rpc(self.robot.get_id)
        services = self._rpc(self.robot.list_services)
        return {
            "serial_number": rid.serial_number, "model": rid.species,
            "hardware_version": rid.version,
            "software_version": str(rid.software_release.version),
            "has_arm": self._rpc(self.robot.has_arm, timeout=self.timeout),
            "services": sorted(s.name for s in services),
        }

    def _lease_failed(self, error: Exception) -> None:
        self._lease_error = error

    def safety(self) -> SafetyState:
        from bosdyn.client.lease import Error as LeaseError, LeaseState
        valid = False
        if self._keepalive and self._keepalive.is_alive() and not self._lease_error:
            try:
                state = self.robot.lease_wallet.get_lease_state("body")
                valid = state.lease_status == LeaseState.Status.SELF_OWNER
            except LeaseError:
                valid = False
        return SafetyState(
            self._rpc(self.robot.is_powered_on, timeout=self.timeout),
            self._rpc(self.robot.is_estopped, timeout=self.timeout),
            (self.robot.time_sync.endpoint.has_established_time_sync
             and not self.robot.time_sync.stopped and self.robot.time_sync.thread_exception is None),
            valid,
        )

    def acquire(self) -> None:
        from bosdyn.client.lease import LeaseKeepAlive
        self._lease_error = None
        self._keepalive = self._rpc(
            LeaseKeepAlive, self._lease, must_acquire=True, return_at_exit=True,
            on_failure_callback=self._lease_failed,
            keep_running_cb=self.liveness_guard,
        )

    def retain(self) -> None:
        if self._lease_error:
            raise RemoteRejected(f"lease_keepalive_failed:{type(self._lease_error).__name__}")
        lease = self.robot.lease_wallet.get_lease("body")
        self._rpc(self._lease.retain_lease, lease, timeout=self.timeout)

    def release(self) -> None:
        if self._keepalive:
            try:
                self._keepalive.shutdown()
            finally:
                self._keepalive = None

    def power_on(self) -> None:
        self._rpc(self.robot.power_on, timeout_sec=20, timeout=self.timeout)

    def power_off(self) -> None:
        self._rpc(self.robot.power_off, cut_immediately=False, timeout_sec=20, timeout=self.timeout)

    def submit(self, command: RobotCommand) -> int:
        return self._rpc(
            self._command.robot_command, build_command(command, self.linear_limit, self.angular_limit),
            end_time_secs=command.expires_at, timeout=self.timeout,
        )

    def feedback(self, vendor_id: int, kind: str) -> tuple[CommandStatus, str]:
        response = self._rpc(self._command.robot_command_feedback,
                             vendor_id, timeout=self.timeout)
        return decode_feedback(response, kind)

    def observe(self) -> dict[str, Any]:
        from bosdyn.client.frame_helpers import get_a_tform_b
        from bosdyn.api import robot_state_pb2

        state = self._rpc(self._state.get_robot_state, timeout=self.timeout)
        k = state.kinematic_state
        transform = get_a_tform_b(k.transforms_snapshot, "odom", "body")
        timestamp = k.acquisition_timestamp.seconds + k.acquisition_timestamp.nanos / 1e9
        skew = self.robot.time_sync.endpoint.clock_skew
        skew_s = skew.seconds + skew.nanos / 1e9
        velocity = k.velocity_of_body_in_odom
        battery = state.battery_states[0] if state.battery_states else None
        return {
            "acquired_at_robot": timestamp, "acquired_at_local": timestamp - skew_s,
            "frame": "odom",
            "position_m": (transform.x, transform.y, transform.z) if transform else None,
            "orientation_xyzw": (transform.rot.x, transform.rot.y, transform.rot.z, transform.rot.w) if transform else None,
            "linear_velocity_mps": (velocity.linear.x, velocity.linear.y, velocity.linear.z),
            "angular_velocity_rps": (velocity.angular.x, velocity.angular.y, velocity.angular.z),
            "battery_fraction": battery.charge_percentage.value / 100 if battery else None,
            "powered": state.power_state.motor_power_state == robot_state_pb2.PowerState.STATE_ON,
            "estopped": any(e.state != robot_state_pb2.EStopState.STATE_NOT_ESTOPPED for e in state.estop_states),
            "joint_positions_rad": {j.name: j.position.value for j in k.joint_states},
            "faults": tuple(f.name for f in state.system_fault_state.faults),
            "raw": {"source": "bosdyn_robot_state", "clock_skew_s": skew_s,
                    "joint_velocity_rad_s": {j.name: j.velocity.value for j in k.joint_states},
                    "joint_load_nm": {j.name: j.load.value for j in k.joint_states}},
        }

    def close(self) -> None:
        try:
            self.release()
        finally:
            if self.robot:
                self.robot.shutdown()
                self.robot = None
