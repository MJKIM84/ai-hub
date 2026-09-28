"""Actuator-only IK and contact grasp controller for the authored four-joint arm.

No item state, ownership, equality constraint, or floating-base state is changed.
This is a research-model controller, not a manufacturer manipulation stack.
"""
from __future__ import annotations

import math
from copy import deepcopy

import mujoco
import numpy as np
from ..arm_kinematics import build_contract, solve_local


class ManipulationController:
    VERSION = "research-arm-contact-0.3"

    def __init__(self, model: mujoco.MjModel, robot_id: str):
        self.model = model
        self.robot_id = robot_id
        self._geometry_contract = build_contract(model, robot_id)
        self.base_id = model.body(robot_id + "/arm-base").id
        self.gripper_id = model.body(robot_id + "/gripper").id
        self.actuators = np.array([model.actuator(f"{robot_id}/arm-motor-{i}").id for i in range(4)])
        joints = [model.joint(f"{robot_id}/arm-{i}") for i in range(4)]
        self.qpos = np.array([j.qposadr[0] for j in joints])
        self.dofs = np.array([j.dofadr[0] for j in joints])
        self.finger_actuators = np.array([model.actuator(f"{robot_id}/grip-motor-{s}").id for s in ("left", "right")])
        self.finger_geoms = [model.geom(f"{robot_id}/finger-shape-{s}").id for s in ("left", "right")]
        self.finger_qpos = {side: int(model.joint(f"{robot_id}/grip-{side}").qposadr[0])
                            for side in ("left", "right")}
        self.target = None
        self.holding_position = False
        self.target_opening = .1
        self.pitch = math.pi
        self.joint_targets = None
        self.payload_estimate_kg = 0.0
        self.control_mode = 'idle'

    @property
    def geometry_contract(self):
        """Detached metadata; changing it cannot alter controller geometry."""
        return deepcopy(self._geometry_contract)

    def inverse_kinematics(self, data: mujoco.MjData, target, pitch: float = math.pi):
        """World gripper origin target, requested tool pitch from upward +Z."""
        base = data.xpos[self.base_id]
        orientation = data.xmat[self.base_id].reshape(3, 3)
        point = orientation.T @ (np.asarray(target, dtype=float) - base)
        return np.array(solve_local(self._geometry_contract, point, pitch=pitch)['joint_targets'])

    def move_to(self, target, *, opening: float | None = None, pitch: float = math.pi):
        new_target = np.asarray(target, dtype=float).copy()
        if new_target.shape != (3,) or not np.isfinite(new_target).all() or not math.isfinite(pitch):
            raise ValueError("유한한 3D 목표 좌표가 필요합니다")
        if opening is not None:
            self.open_gripper(opening)
        self.target = new_target
        self.holding_position = False
        self.control_mode = 'trajectory'
        self.pitch = float(pitch)

    def open_gripper(self, opening: float = .1):
        """Set each finger slide in meters; opening range 0..0.1, not full gap."""
        if not 0 <= opening <= .1:
            raise ValueError("그리퍼 관절 목표는 0..0.1 m 범위입니다")
        self.target_opening = float(opening)

    def set_payload_estimate(self, mass_kg: float):
        """Known/estimated held load for gravity compensation, not attachment."""
        if not math.isfinite(mass_kg) or mass_kg < 0:
            raise ValueError("유효한 적재 질량 추정값이 필요합니다")
        self.payload_estimate_kg = float(mass_kg)

    def hold(self, data: mujoco.MjData):
        """Stop trajectory tracking at measured joints while retaining grip force."""
        self.target = None
        self.holding_position = True
        self.control_mode = 'joint_hold'
        self.joint_targets = data.qpos[self.qpos].copy()
        self.update(data)

    def release_and_hold(self, data: mujoco.MjData):
        """Apply an authorized release at measured joints, through actuators only.

        Repeated deliveries of the same release episode keep its original
        measured joint targets. Runtime separately rejects retired/stale
        deliveries after a newer trajectory command.
        """
        if self.control_mode != 'release_settle':
            measured = data.qpos[self.qpos].copy()
            if not np.isfinite(measured).all():
                raise ValueError('해제 정지 기준 관절 측정이 유효하지 않습니다')
            self.joint_targets = measured
        self.target = None
        self.holding_position = True
        self.target_opening = .1
        self.payload_estimate_kg = 0.
        self.control_mode = 'release_settle'
        self.update(data)

    def update(self, data: mujoco.MjData, dt: float = .01):
        if not math.isfinite(dt) or dt <= 0:
            raise ValueError("양의 유한한 제어 시간 간격이 필요합니다")
        if self.target is None and not self.holding_position:
            return
        desired = self.joint_targets if self.holding_position else self.inverse_kinematics(data, self.target, self.pitch)
        if self.joint_targets is None:
            self.joint_targets = data.qpos[self.qpos].copy()
        delta=desired-self.joint_targets
        # Move the joint vector with one common scale so a downward-facing
        # tool remains downward during a grasped lift between IK solutions.
        scale=min(1.0, .7*dt/max(float(np.max(np.abs(delta))), 1e-12))
        self.joint_targets += delta*scale
        # Feedforward of this model's ideal gravity/Coriolis estimate through
        # actuator targets. Live qpos/qvel and item poses remain untouched.
        kp = self.model.actuator_gainprm[self.actuators, 0]
        feedforward = data.qfrc_bias[self.dofs].copy()
        if self.payload_estimate_kg:
            jac = np.zeros((3, self.model.nv))
            mujoco.mj_jacBody(self.model, data, jac, None, self.gripper_id)
            upward = -self.model.opt.gravity * self.payload_estimate_kg
            feedforward += jac[:, self.dofs].T @ upward
        compensation = np.divide(feedforward, kp, out=np.zeros(4), where=kp>0)
        targets = self.joint_targets + compensation
        data.ctrl[self.actuators] = np.clip(targets, self.model.actuator_ctrlrange[self.actuators, 0], self.model.actuator_ctrlrange[self.actuators, 1])
        data.ctrl[self.finger_actuators] = self.target_opening

    def feedback(self, data: mujoco.MjData, item_id: str | None = None):
        touched = set()
        normal_forces = {"left": 0.0, "right": 0.0}
        item_geom = self.model.geom(f"{item_id}/shape").id if item_id else None
        for index, contact in enumerate(data.contact[:data.ncon]):
            pair = (contact.geom1, contact.geom2)
            if item_geom not in pair:
                continue
            for side, geom in zip(("left", "right"), self.finger_geoms):
                if geom in pair:
                    force = np.zeros(6)
                    mujoco.mj_contactForce(self.model, data, index, force)
                    if force[0] > .1:
                        touched.add(side)
                        normal_forces[side] += float(force[0])
        position = data.xpos[self.gripper_id].copy()
        return {
            "tool_position": position.tolist(),
            "tool_quaternion": data.xquat[self.gripper_id].tolist(),
            # Joint measurements and the delivered servo path start share the
            # same delayed observation as tool/finger feedback. The planner
            # must not replace a settled, compliant posture with ideal IK.
            "arm_joint_positions_rad": data.qpos[self.qpos].tolist(),
            "arm_joint_targets_rad": (self.joint_targets.tolist()
                                      if self.joint_targets is not None else None),
            "position_error_m": float(np.linalg.norm(position-self.target)) if self.target is not None else None,
            "finger_contacts": sorted(touched),
            "bilateral_contact": len(touched) == 2,
            "finger_normal_forces_N": normal_forces,
            # Actual slide measurements, not the actuator command or a
            # geometrical assumption that the fingers reached full opening.
            "finger_positions_m": {side: float(data.qpos[address])
                                   for side, address in self.finger_qpos.items()},
            # Local controller telemetry is sampled through the observation
            # bus. Recovery must preserve what was actually delivered, not
            # a previously generated (possibly undelivered) command.
            "commanded_opening": self.target_opening,
            "payload_estimate_kg": self.payload_estimate_kg,
            "control_mode": self.control_mode,
            "controller_version": self.VERSION,
        }
