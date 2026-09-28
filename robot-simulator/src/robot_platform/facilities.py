"""Observed elevator reservations and interlocks, independent of simulation truth.

Positions are metres relative to the cabin's lowest configured origin. Door
fraction is a delivered physical sensor reading (0 closed, 1 open), not a timer.
Robot commands are navigation intentions; an adapter must execute them and feed
back observations. This module cannot move a robot or complete an unseen trip.
"""
from __future__ import annotations

from collections import deque
from copy import deepcopy
from dataclasses import dataclass, field
import math

from .domain import Project

VERSION = "observed-elevator-0.3"


@dataclass
class Ride:
    id: str
    robot_id: str
    source_floor: str
    dest_floor: str
    mass: float
    envelope: tuple[float, float, float]
    status: str = "queued"
    slot: tuple[float, float] = (0., 0.)
    stable_since: float | None = None
    facility_stable_since: float | None = None
    boarded: bool = False
    exited: bool = False


@dataclass
class Elevator:
    queue: deque = field(default_factory=deque)
    active: list[Ride] = field(default_factory=list)
    phase: str = "idle"
    phase_since: float = 0.
    target: float = 0.
    physical_occupants: set[str] = field(default_factory=set)
    fault: str | None = None
    resume_phase: str = "idle"
    last_observation: dict = field(default_factory=dict)
    stable_since: float | None = None
    fault_latched: bool = False
    call_floor: str | None = None
    motion_distance: float = 0.


class FacilityManager:
    """FIFO batch trips with observed boarding, door and arrival interlocks.

    update(time, observations, facility_observations) -> dict with commands,
    robot_commands and states. Required elevator sensor keys: sampled_at,
    position, velocity, door_fraction, door_blocked, occupants, load_kg. Robot
    observations use the existing ObservationBus pose/velocity/sensors contract.
    A request envelope uses robot-local full x/y/z dimensions. Boarding targets
    face along the cabin's positive local y direction (front entrance is -y).
    """
    clearance = .05
    cabin_height = 2.2  # Explicit authored cabin model, not shaft height.
    position_tolerance = .025
    velocity_tolerance = .025
    confirmation_time = .35

    def __init__(self, project: Project):
        self.project = project.model_copy(deep=True)
        self.elements = {e.id: e for e in project.environment.elements if e.kind == "elevator"}
        self.floors = {f.id: f.elevation for f in project.environment.floors}
        self.elevators = {eid: Elevator() for eid in self.elements}
        self.rides: dict[str, Ride] = {}
        self.sequence = 0
        self.time = 0.
        self.stale_after = project.policy.stale_after
        self.robot_ids = {r.id for r in project.robots}
        self.robot_observations: dict[str, dict] = {}

    def _height(self, eid, floor):
        e = self.elements[eid]
        return self.floors[floor] - self.floors[e.floor_id] - e.pose.z

    def request(self, elevator_id, robot_id, source_floor, dest_floor, robot_mass, envelope):
        if elevator_id not in self.elements:
            raise ValueError("없는 승강기")
        if robot_id not in self.robot_ids:
            raise ValueError("없는 로봇")
        e = self.elements[elevator_id]
        floors = e.facility.served_floors or [e.floor_id]
        if source_floor not in floors or dest_floor not in floors or source_floor == dest_floor:
            raise ValueError("서로 다른 서비스 층을 지정하세요")
        if min(self._height(elevator_id, source_floor), self._height(elevator_id, dest_floor)) < -.001:
            raise ValueError("승강기 원점보다 낮은 층은 지원하지 않습니다")
        mass = float(robot_mass)
        if hasattr(envelope, "model_dump"):
            envelope = envelope.model_dump()
        if isinstance(envelope, dict):
            shape = tuple(float(envelope[k]) for k in ("x", "y", "z"))
        else:
            shape = tuple(float(v) for v in envelope)
        if len(shape) != 3 or not all(math.isfinite(v) and v > 0 for v in shape):
            raise ValueError("외곽 치수는 양수인 x/y/z 전체 길이여야 합니다")
        if not math.isfinite(mass) or mass <= 0 or mass > e.facility.max_load:
            raise ValueError("허용 하중을 초과했거나 질량이 잘못되었습니다")
        if shape[1] + 2*self.clearance > e.size.x or shape[0] + 2*self.clearance > e.size.y or shape[2] + self.clearance > self.cabin_height:
            raise ValueError("로봇 외곽 치수가 승강기 내부에 맞지 않습니다")
        for ride in self.rides.values():
            if ride.robot_id == robot_id and ride.status not in ("completed", "cancelled"):
                same = ride.id.startswith(elevator_id + ":") and (ride.source_floor, ride.dest_floor) == (source_floor, dest_floor)
                if not same:
                    raise ValueError("로봇에 진행 중인 다른 승강기 예약이 있습니다")
                return self._receipt(ride)
        self.sequence += 1
        ride = Ride(f"{elevator_id}:{robot_id}:{self.sequence}", robot_id, source_floor, dest_floor, mass, shape)
        self.rides[ride.id] = ride
        self.elevators[elevator_id].queue.append(ride)
        return self._receipt(ride)

    @staticmethod
    def _receipt(ride):
        return {"request_id": ride.id, "robot_id": ride.robot_id,
                "source_floor": ride.source_floor, "dest_floor": ride.dest_floor,
                "status": ride.status}

    def cancel(self, elevator_id, robot_id):
        state = self.elevators[elevator_id]
        for ride in list(state.queue):
            if ride.robot_id == robot_id:
                state.queue.remove(ride)
                ride.status = "cancelled"
                return True
        for ride in state.active:
            if ride.robot_id == robot_id:
                # Removing an active reservation could strand a boarding robot.
                return False
        return False

    def call(self, elevator_id, floor_id):
        """Request an empty-cabin landing call through the same interlocks."""
        e=self.elements[elevator_id]
        state=self.elevators[elevator_id]
        if floor_id not in (e.facility.served_floors or [e.floor_id]):
            raise ValueError("서비스하지 않는 층입니다")
        if state.phase!="idle" or state.active or state.queue or state.physical_occupants:
            raise ValueError("진행 중인 예약 또는 실제 탑승자가 있어 빈 객실 호출이 불가합니다")
        if not self._fresh(state.last_observation,self.time):
            raise ValueError("승강기 실제 상태 관측을 먼저 수신해야 합니다")
        if self._height(elevator_id,floor_id)<-.001:
            raise ValueError("승강기 원점보다 낮은 층은 지원하지 않습니다")
        state.call_floor=floor_id
        state.target=self._height(elevator_id,floor_id)
        self._phase(state,"closing_empty",self.time)
        return {"elevator_id":elevator_id,"floor_id":floor_id,"status":"accepted"}

    def release(self, elevator_id, robot_id):
        state = self.elevators[elevator_id]
        if robot_id in state.physical_occupants:
            return False
        for ride in state.active:
            if ride.robot_id == robot_id:
                if not ride.exited:
                    return False
                ride.status = "completed"
                state.active.remove(ride)
                return True
        return any(r.robot_id == robot_id and r.id.startswith(elevator_id + ":") and r.status == "completed" for r in self.rides.values())

    def recover(self, elevator_id):
        """Acknowledge a timeout after inspection; live interlocks still apply.

        Sensor/facility faults recover when fresh safe observations return.
        Mechanical motion/door timeouts require this explicit acknowledgement
        so an unchanged stalled actuator cannot repeatedly restart itself.
        """
        state = self.elevators[elevator_id]
        state.fault_latched = False

    def _fresh(self, obs, time):
        try:
            stamp=obs["sampled_at"]
            if not isinstance(stamp,(int,float)) or isinstance(stamp,bool) or not math.isfinite(stamp):
                return False
            age = time - stamp
            return 0 <= age <= self.stale_after
        except (TypeError, ValueError, KeyError):
            return False

    def _slots(self, e, rides):
        """Conservative shelf packing in FIFO order, from rear to front."""
        width, depth = e.size.x - 2*self.clearance, e.size.y - 2*self.clearance
        x, y, row_depth, slots = -width/2, depth/2, 0., []
        if len(rides) == 1:
            return [(0., 0.)]
        for ride in rides:
            w, d = ride.envelope[1], ride.envelope[0]
            if x + w > width/2 + 1e-9:
                x, y, row_depth = -width/2, y-row_depth-self.clearance, 0.
            if y-d < -depth/2-1e-9:
                return None
            slots.append((x+w/2, y-d/2))
            x += w + self.clearance
            row_depth = max(row_depth, d)
        return slots

    def _promote(self, eid, state, time):
        if state.active or not state.queue or state.physical_occupants:
            return
        e = self.elements[eid]
        first = state.queue[0]
        chosen = []
        total = 0.
        for ride in state.queue:
            if (ride.source_floor, ride.dest_floor) != (first.source_floor, first.dest_floor):
                break  # Strict FIFO: never overtake an incompatible earlier trip.
            if len(chosen) >= e.facility.capacity or total + ride.mass > e.facility.max_load:
                break
            candidate = chosen + [ride]
            if self._slots(e, candidate) is None:
                break
            chosen = candidate
            total += ride.mass
        slots = self._slots(e, chosen)
        for ride, slot in zip(chosen, slots):
            state.queue.popleft()
            ride.slot, ride.status = slot, "reserved"
            state.active.append(ride)
        if chosen:
            state.target = self._height(eid, first.source_floor)
            self._phase(state, "closing_empty", time)

    @staticmethod
    def _phase(state, phase, time):
        state.phase, state.phase_since, state.stable_since = phase, time, None
        if phase in ("positioning","moving"):
            state.motion_distance=abs(state.target-float(state.last_observation.get("position",0.)))
        for ride in state.active:
            ride.stable_since = ride.facility_stable_since = None
            if phase=="boarding":
                ride.boarded=False
                ride.status="reserved"

    def _local_pose(self, e, pose):
        c, s = math.cos(e.pose.yaw), math.sin(e.pose.yaw)
        dx, dy = pose["x"]-e.pose.x, pose["y"]-e.pose.y
        return c*dx+s*dy, -s*dx+c*dy

    def _contains(self, e, ride, obs):
        pose = obs["pose"]
        x, y = self._local_pose(e, pose)
        angle = pose["yaw"] - e.pose.yaw
        hx = (abs(math.cos(angle))*ride.envelope[0] + abs(math.sin(angle))*ride.envelope[1])/2
        hy = (abs(math.sin(angle))*ride.envelope[0] + abs(math.cos(angle))*ride.envelope[1])/2
        return abs(x)+hx <= e.size.x/2-self.clearance and abs(y)+hy <= e.size.y/2-self.clearance

    def _outside(self, e, ride, obs):
        pose = obs["pose"]
        x, y = self._local_pose(e, pose)
        angle = pose["yaw"]-e.pose.yaw
        hx = (abs(math.cos(angle))*ride.envelope[0] + abs(math.sin(angle))*ride.envelope[1])/2
        hy = (abs(math.sin(angle))*ride.envelope[0] + abs(math.cos(angle))*ride.envelope[1])/2
        # Require the entire footprint beyond the cabin, not only its centre.
        return abs(x)-hx >= e.size.x/2+self.clearance or abs(y)-hy >= e.size.y/2+self.clearance

    @staticmethod
    def _support(eid, obs):
        contacts = obs.get("sensors", {}).get("contacts", [])
        return any(eid+"/platform" in (c.get("geom_a"), c.get("geom_b")) and float(c.get("force", 0)) > 1. for c in contacts)

    @staticmethod
    def _stopped(obs):
        return sum(float(v)**2 for v in obs.get("velocity", [float("inf")])) < .035**2 and sum(float(v)**2 for v in obs.get("angular_velocity", [float("inf")])) < .1**2

    def _robot_fresh(self, ride, obs, time):
        if not self._fresh(obs, time) or obs.get("fault", "none") in ("communication", "sensor"):
            return False
        previous=self.robot_observations.get(ride.robot_id)
        if previous and (obs["sampled_at"]<previous["sampled_at"] or (obs["sampled_at"]==previous["sampled_at"] and obs!=previous)):
            return False
        try:
            values = [obs["pose"][key] for key in ("x", "y", "z", "yaw")]
            values += list(obs["velocity"]) + list(obs["angular_velocity"])
            contacts=obs.get("sensors",{}).get("contacts",[])
            valid_contacts=isinstance(contacts,list) and all(isinstance(c,dict) and isinstance(c.get("force",0),(int,float)) and math.isfinite(c.get("force",0)) and c.get("force",0)>=0 for c in contacts)
            valid=valid_contacts and len(obs["velocity"]) == len(obs["angular_velocity"]) == 3 and all(isinstance(v,(int,float)) and math.isfinite(v) for v in values)
            if valid:
                self.robot_observations[ride.robot_id]=deepcopy(obs)
            return valid
        except (KeyError, TypeError, ValueError, AttributeError):
            return False

    def _arrived(self, state, observation, time):
        sampled_at=observation["sampled_at"]
        good = sampled_at>=state.phase_since and abs(observation["position"]-state.target) <= self.position_tolerance and abs(observation["velocity"]) <= self.velocity_tolerance
        if not good:
            state.stable_since = None
            return False
        if state.stable_since is None:
            state.stable_since = sampled_at
        return sampled_at-state.stable_since >= self.confirmation_time-1e-9

    def _ride_confirmed(self,ride,robot_observation,facility_observation,phase_since):
        """Both sensor streams must independently advance across the dwell.

        Cached observations can sustain safe control while fresh, but repeating
        them at later manager ticks cannot provide new boarding/exit evidence.
        """
        robot_at=robot_observation["sampled_at"]
        facility_at=facility_observation["sampled_at"]
        if min(robot_at,facility_at)<phase_since:
            ride.stable_since=ride.facility_stable_since=None
            return False
        if ride.stable_since is None or ride.facility_stable_since is None:
            ride.stable_since=robot_at
            ride.facility_stable_since=facility_at
            return False
        return min(robot_at-ride.stable_since,facility_at-ride.facility_stable_since)>=self.confirmation_time-1e-9

    def _robot_target(self, eid, ride, action):
        e = self.elements[eid]
        x, y = ride.slot
        floor = ride.source_floor
        if action == "exit":
            # Same front entrance at destination; backing out is adapter policy.
            y = -e.size.y/2-ride.envelope[0]/2-.3
            floor = ride.dest_floor
        c, s = math.cos(e.pose.yaw), math.sin(e.pose.yaw)
        return {"action": action, "elevator_id": eid, "request_id": ride.id, "floor_id": floor,
                "target": {"x": e.pose.x+c*x-s*y, "y": e.pose.y+s*x+c*y, "z": self.floors[floor], "yaw": e.pose.yaw+math.pi/2}}

    def update(self, time, observations, facility_observations):
        time = float(time)
        if not math.isfinite(time) or time < self.time:
            raise ValueError("시설 시간은 유한하며 역행할 수 없습니다")
        self.time = time
        commands, robot_commands, states = {}, {}, {}
        for eid, state in self.elevators.items():
            e = self.elements[eid]
            obs = facility_observations.get(eid, {})
            fresh = self._fresh(obs, time)
            if fresh and state.last_observation:
                previous=state.last_observation
                if obs["sampled_at"]<previous["sampled_at"] or (obs["sampled_at"]==previous["sampled_at"] and obs!=previous):
                    fresh=False
            required = ("position", "velocity", "door_fraction", "door_blocked", "occupants", "load_kg")
            sensor_valid = fresh and all(k in obs for k in required)
            if sensor_valid:
                try:
                    sensor_valid = all(isinstance(obs[k], (int, float)) and math.isfinite(obs[k]) for k in ("position", "velocity", "door_fraction", "load_kg")) and 0 <= obs["door_fraction"] <= 1 and obs["load_kg"] >= 0 and isinstance(obs["door_blocked"], bool) and isinstance(obs["occupants"], (list, tuple, set)) and all(isinstance(v, str) for v in obs["occupants"]) and len(set(obs["occupants"])) == len(obs["occupants"])
                except (TypeError, ValueError):
                    sensor_valid = False
            if sensor_valid:
                state.last_observation = deepcopy(obs)
                state.physical_occupants = set(obs["occupants"])
            measured = state.last_observation
            position = float(measured.get("position", 0.))
            door = float(measured.get("door_fraction", 0.))
            active_ids = {r.robot_id for r in state.active}
            error = None
            if state.fault_latched:
                error = state.fault
            elif not sensor_valid:
                error = "facility_observation_stale_or_invalid"
            elif obs.get("fault", e.facility.fault):
                error = "facility_fault"
            elif not e.facility.automatic:
                error = "manual_mode"
            elif obs["load_kg"] > e.facility.max_load + .01:
                error = "overload"
            elif len(state.physical_occupants) > e.facility.capacity:
                error = "overcapacity"
            elif state.active and state.physical_occupants-active_ids:
                error = "unreserved_occupant"
            elif state.call_floor and state.physical_occupants:
                error = "unreserved_occupant"
            elif state.active and any(not self._robot_fresh(r, observations.get(r.robot_id, {}), time) for r in state.active):
                error = "robot_observation_stale"
            elif state.phase in ("closing_depart", "moving") and active_ids-state.physical_occupants:
                error = "missing_boarded_occupant"
            elif state.phase in ("positioning", "moving") and door > .02:
                error = "door_open_during_motion"
            if error:
                if state.phase != "fault":
                    state.resume_phase = state.phase
                    self._phase(state, "fault", time)
                state.fault = error
            elif state.phase == "fault":
                phase = state.resume_phase
                # Re-close/re-check interlocks before restoring any suspended motion.
                phase = {"moving": "closing_depart", "positioning": "closing_empty"}.get(phase, phase)
                self._phase(state, phase, time)
                state.fault = None
            if state.phase == "idle" and sensor_valid:
                self._promote(eid, state, time)
            # Commands always start with a physical hold target. Adapters must
            # retain motor support/braking; hold does not mean remove motor force.
            command = {"lift_target": position, "door_target": door, "hold": True,
                       "max_speed": e.facility.speed, "door_duration": e.facility.door_duration}
            for ride in state.queue:
                robot_commands[ride.robot_id] = {"action": "wait", "elevator_id": eid, "request_id": ride.id}
            for ride in state.active:
                robot_commands[ride.robot_id] = {"action": "hold", "elevator_id": eid, "request_id": ride.id}
            if state.phase == "fault":
                # A doorway obstruction keeps doors open only while level at a
                # landing. In the shaft the adapter holds the measured aperture.
                level = any(abs(position-self._height(eid, f)) <= self.position_tolerance for f in (e.facility.served_floors or [e.floor_id]))
                if level and abs(measured.get("velocity", 1)) <= self.velocity_tolerance:
                    command["door_target"] = 1.
            elif state.phase in ("closing_empty", "closing_depart"):
                command["door_target"] = 0.
                if obs["door_blocked"]:
                    command["door_target"] = 1.
                    if state.phase == "closing_depart":
                        self._phase(state, "boarding", time)
                elif door <= .02:
                    if state.phase == "closing_depart":
                        all_inside = all(self._contains(e, r, observations[r.robot_id]) and self._support(eid, observations[r.robot_id]) and self._stopped(observations[r.robot_id]) for r in state.active)
                        if not all_inside:
                            self._phase(state, "boarding", time)
                            command["door_target"] = 1.
                        else:
                            state.target = self._height(eid, state.active[0].dest_floor)
                            self._phase(state, "moving", time)
                    elif not state.physical_occupants:
                        self._phase(state, "positioning", time)
            elif state.phase in ("positioning", "moving"):
                command.update(lift_target=state.target, door_target=0., hold=False)
                if self._arrived(state, obs, time):
                    self._phase(state, ("opening_call" if state.call_floor else "opening_board") if state.phase == "positioning" else "opening_exit", time)
                    command.update(lift_target=state.target, door_target=1., hold=True)
                elif time-state.phase_since > state.motion_distance/e.facility.speed*3+20:
                    state.resume_phase = state.phase
                    self._phase(state, "fault", time)
                    state.fault = "motion_timeout"
                    state.fault_latched = True
                    command.update(lift_target=position, hold=True)
            elif state.phase in ("opening_board", "opening_exit", "opening_call"):
                command.update(lift_target=state.target, door_target=1.)
                if door >= .98 and abs(position-state.target) <= self.position_tolerance and abs(obs["velocity"]) <= self.velocity_tolerance:
                    if state.phase=="opening_call":
                        state.call_floor=None
                        self._phase(state,"idle",time)
                    else:
                        self._phase(state, "boarding" if state.phase == "opening_board" else "alighting", time)
            elif state.phase == "boarding":
                command.update(lift_target=state.target, door_target=1.)
                if door >= .98 and abs(position-state.target) <= self.position_tolerance and abs(obs["velocity"]) <= self.velocity_tolerance:
                    for ride in state.active:
                        rob = observations[ride.robot_id]
                        good = ride.robot_id in state.physical_occupants and self._contains(e, ride, rob) and self._support(eid, rob) and self._stopped(rob)
                        if not good:
                            ride.stable_since = ride.facility_stable_since = None
                            ride.boarded = False
                        elif self._ride_confirmed(ride,rob,obs,state.phase_since):
                            ride.boarded, ride.status = True, "boarded"
                        robot_commands[ride.robot_id] = self._robot_target(eid, ride, "hold" if ride.boarded else "board")
                    if all(r.boarded for r in state.active) and state.active:
                        self._phase(state, "closing_depart", time)
                else:
                    for ride in state.active:
                        ride.stable_since = ride.facility_stable_since = None
            elif state.phase == "alighting":
                command.update(lift_target=state.target, door_target=1.)
                if door >= .98 and abs(position-state.target) <= self.position_tolerance and abs(obs["velocity"]) <= self.velocity_tolerance:
                    for ride in list(state.active):
                        rob = observations[ride.robot_id]
                        good = ride.robot_id not in state.physical_occupants and self._outside(e, ride, rob) and not self._support(eid, rob) and self._stopped(rob)
                        # A floor contact is required: falling outside is not exit.
                        floor_contact = any(any(str(c.get(k, "")).startswith("floor/"+ride.dest_floor+"/") for k in ("geom_a", "geom_b")) and c.get("force", 0) > 1 for c in rob.get("sensors", {}).get("contacts", []))
                        if not (good and floor_contact):
                            ride.stable_since = ride.facility_stable_since = None
                        elif self._ride_confirmed(ride,rob,obs,state.phase_since):
                            ride.exited = True
                            self.release(eid, ride.robot_id)
                        robot_commands[ride.robot_id] = self._robot_target(eid, ride, "done" if ride.exited else "exit")
                    if not state.active:
                        self._phase(state, "idle", time)
                else:
                    for ride in state.active:
                        ride.stable_since = ride.facility_stable_since = None
            if state.phase in ("closing_empty", "closing_depart", "opening_board", "opening_exit", "opening_call") and time-state.phase_since > e.facility.door_duration*3+2:
                state.resume_phase = state.phase
                self._phase(state, "fault", time)
                state.fault = "door_timeout"
                state.fault_latched = True
            commands[eid] = command
            states[eid] = {"id": eid, "phase": state.phase, "position": position, "target": state.target,
                "door": "open" if door >= .98 else "closed" if door <= .02 else "partial",
                "door_fraction": door, "fault": state.fault, "queue": [r.robot_id for r in state.queue],
                "reserved_by": [r.robot_id for r in state.active], "occupants": sorted(state.physical_occupants),
                "load_kg": measured.get("load_kg"), "capacity": e.facility.capacity, "max_load": e.facility.max_load,"call_floor":state.call_floor,
                "requests": [{**self._receipt(r), "boarded": r.boarded, "exited": r.exited} for r in self.rides.values() if r.id.startswith(eid+":")]}
        return deepcopy({"commands": commands, "robot_commands": robot_commands, "states": states})
