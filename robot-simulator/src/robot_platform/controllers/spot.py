"""Experimental joint-space Spot controller for Menagerie; not Boston Dynamics firmware.

Only actuator targets are written. Floating-base translation results from joint
forces and contact dynamics. Capability gates live in the validation report.
"""
from __future__ import annotations

import math

import mujoco
import numpy as np


class SpotController:
    VERSION = "spot-ik-trot-0.2"
    LEGS = ("fl", "fr", "hl", "hr")
    FEET = ("FL", "FR", "HL", "HR")

    def __init__(self, model: mujoco.MjModel, robot_id: str = ""):
        self.model = model
        self.prefix = f"{robot_id}/" if robot_id else ""
        self.body_id = model.body(self.prefix + "body").id
        self.actuator_ids = np.array([model.actuator(self.prefix + f"{leg}_{j}").id for leg in self.LEGS for j in ("hx", "hy", "kn")])
        self.geom_ids = [model.geom(self.prefix + foot).id for foot in self.FEET]
        self.phase = 0.0
        self.frequency = 1.2
        self.duty = 0.6
        self.height = 0.46
        self.lift = 0.12
        self.last_targets = np.tile([0.0, 1.04, -1.8], 4)
        self.velocity = np.zeros(3)
        self.measured_velocity = np.zeros(3)
        self.velocity_integral = np.zeros(3)
        self.joint_rate_limit = 14.0
        self.last_feedback = {"mode": "stand", "feet_in_contact": [], "upright_cos": 1.0, "status": "idle"}

    @staticmethod
    def inverse_leg(x: float, y: float, z: float, side: int) -> np.ndarray:
        """Analytic IK for source model hip offset and thigh/shank transforms."""
        offset = side * 0.1108
        zplane = -math.sqrt(max(0.01, y * y + z * z - offset * offset))
        hx = math.atan2(y, -z) - math.atan2(offset, -zplane)
        length1, length2 = math.hypot(0.025, 0.32), 0.3365
        alpha = math.atan2(0.025, 0.32)
        costheta = np.clip((x * x + zplane * zplane - length1**2 - length2**2) / (2 * length1 * length2), -0.999, 0.999)
        knee_eff = -math.acos(float(costheta))
        thigh_eff = math.atan2(-x, -zplane) - math.atan2(length2 * math.sin(knee_eff), length1 + length2 * math.cos(knee_eff))
        return np.array([hx, thigh_eff + alpha, knee_eff - alpha])

    def update(self, data: mujoco.MjData, vx: float = 0.0, vy: float = 0.0, yaw_rate: float = 0.0, mode: str = "stand", dt: float = 0.01) -> dict:
        if mode not in {"stand", "sit", "walk", "stop"}:
            raise ValueError(f"Unsupported Spot control mode: {mode}")
        desired = np.array([vx, vy, yaw_rate]) if mode == "walk" else np.zeros(3)
        # Validated research operating ceiling; manufacturer firmware supports
        # 1.6 m/s, which this joint-space controller does not claim to reproduce.
        desired = np.clip(desired, [-1.0, -0.2, -0.6], [1.0, 0.2, 0.6])
        self.velocity += np.clip(desired - self.velocity, -0.8 * dt, 0.8 * dt)
        active = np.linalg.norm(self.velocity) > 0.008
        if active:
            self.frequency = 1.2 + 1.2 * min(1., abs(self.velocity[0]) / .8)
            self.duty = .6 - .1 * min(1., abs(self.velocity[0]) / .8)
            self.phase = (self.phase + self.frequency * dt) % 1.0
        rot = data.xmat[self.body_id].reshape(3, 3)
        twist = np.zeros(6)
        mujoco.mj_objectVelocity(self.model, data, mujoco.mjtObj.mjOBJ_BODY, self.body_id, twist, 1)
        measured = np.array([twist[3], twist[4], twist[2]])
        self.measured_velocity += min(1.0, dt / 0.25) * (measured - self.measured_velocity)
        if np.linalg.norm(desired) < .008:
            self.velocity_integral *= math.exp(-8 * dt)
        elif active:
            self.velocity_integral += 0.6 * (self.velocity - self.measured_velocity) * dt
            self.velocity_integral = np.clip(self.velocity_integral, [-1.6, -0.2, -0.5], [1.6, 0.2, 0.5])
        else:
            self.velocity_integral *= max(0.0, 1.0 - dt * 4)
        # Do not carry forward-speed wind-up into a stop or in-place turn.
        braking = ((desired - self.velocity) * self.velocity < 0)
        # Once an axis has stopped, retain velocity feedback during a turn so
        # stance drift is corrected instead of accumulating a position error.
        if np.linalg.norm(desired) < .008:
            braking[:] = True
        self.velocity_integral[braking] *= math.exp(-8 * dt)
        gait_velocity = np.clip(self.velocity + self.velocity_integral, [-3.2, -0.3, -0.8], [3.2, 0.3, 0.8])
        roll = math.atan2(rot[2, 1], rot[2, 2])
        pitch = math.asin(float(np.clip(-rot[2, 0], -1.0, 1.0)))
        desired_height = 0.23 if mode == "sit" else 0.46
        self.height += float(np.clip(desired_height - self.height, -0.15 * dt, 0.15 * dt))
        targets = []
        contacts = set()
        for con in data.contact[:data.ncon]:
            for gid in (con.geom1, con.geom2):
                if gid in self.geom_ids:
                    contacts.add(self.FEET[self.geom_ids.index(gid)])
        for index, leg in enumerate(self.LEGS):
            side = 1 if index in (0, 2) else -1
            hip_x = 0.29785 if index < 2 else -0.29785
            hip_y = side * 0.055
            # Diagonal pairs have opposite swing phases. Translation never
            # changes the floating base state; contact does the work.
            phase = (self.phase + (0.5 if index in (1, 2) else 0)) % 1.0
            vx_leg = gait_velocity[0] - gait_velocity[2] * (hip_y + side * 0.1108)
            vy_leg = gait_velocity[1] + gait_velocity[2] * hip_x
            duration = self.duty / self.frequency
            if phase < self.duty:
                sweep = 0.5 - phase / self.duty
                lift = 0.0
            else:
                p = (phase - self.duty) / (1.0 - self.duty)
                sweep = -0.5 + p
                lift = (self.lift - .04 * min(1., abs(self.velocity[0]) / .8)) * math.sin(math.pi * p)
            if not active:
                sweep, lift = 0.0, 0.0
            x = -0.035 + vx_leg * duration * sweep
            y = side * 0.1108 + vy_leg * duration * sweep
            # Body attitude feedback counteracts roll/pitch via foot height.
            z = -self.height + lift + 0.35 * (roll * (hip_y + y) - pitch * hip_x)
            targets.extend(self.inverse_leg(x, y, z, side))
        targets = np.asarray(targets)
        targets = np.clip(targets, self.model.actuator_ctrlrange[self.actuator_ids, 0], self.model.actuator_ctrlrange[self.actuator_ids, 1])
        self.last_targets += np.clip(targets - self.last_targets, -self.joint_rate_limit * dt, self.joint_rate_limit * dt)
        data.ctrl[self.actuator_ids] = self.last_targets
        self.last_feedback = {
            "mode": mode, "feet_in_contact": sorted(contacts), "upright_cos": float(rot[2, 2]),
            "status": "fallen" if rot[2, 2] < 0.6 else ("moving" if active else "holding"),
            "controller_version": self.VERSION,
        }
        return self.last_feedback
