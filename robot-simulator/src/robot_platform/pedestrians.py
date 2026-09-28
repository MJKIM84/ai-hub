"""Seeded local pedestrian intentions expressed only as actuator velocities.

Delivered local perception is an explicit input; no simulation state is read or
changed here. This research heuristic is not a calibrated human behavior model.
"""
from __future__ import annotations

from collections import deque
from collections.abc import Mapping
from copy import deepcopy
import hashlib
import math
import random

from .domain import Person


def _xyz(value):
    if isinstance(value, Mapping):
        value = [value.get(axis) for axis in "xyz"]
    try:
        result = tuple(float(component) for component in value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("position/velocity must contain three finite coordinates") from exc
    if len(result) != 3 or not all(math.isfinite(component) for component in result):
        raise ValueError("position/velocity must contain three finite coordinates")
    return result


class PedestrianController:
    VERSION = "seeded-local-pedestrian-0.1"
    BODY_RADIUS = .22
    WAYPOINT_TOLERANCE = .18
    SUDDEN_COOLDOWN = .5

    def __init__(self, people, floor_heights, seed=1, *, floor_bounds=None,
                 perception_range=3.0, stale_after=1.0, environment=None,
                 desired_robot_clearance_m=.5):
        self.people = {}
        for value in people:
            person = Person.model_validate(value).model_copy(deep=True)
            if person.id in self.people:
                raise ValueError("pedestrian IDs must be unique")
            self.people[person.id] = person
        self.floor_heights = {str(key): float(value) for key, value in floor_heights.items()}
        if not self.floor_heights or not all(math.isfinite(value) for value in self.floor_heights.values()):
            raise ValueError("finite floor elevations are required")
        if any(person.floor_id not in self.floor_heights for person in self.people.values()):
            raise ValueError("pedestrian floor is unknown")
        if isinstance(seed, bool) or not isinstance(seed, int):
            raise ValueError("seed must be an integer")
        self.perception_range, self.stale_after = float(perception_range), float(stale_after)
        if not all(math.isfinite(value) and value > 0 for value in (self.perception_range, self.stale_after)):
            raise ValueError("perception range and stale time must be positive and finite")
        self.desired_robot_clearance_m = float(desired_robot_clearance_m)
        if not math.isfinite(self.desired_robot_clearance_m) or self.desired_robot_clearance_m < 0:
            raise ValueError("desired robot clearance must be finite and nonnegative")
        self.floor_bounds = {}
        for floor_id, value in (floor_bounds or {}).items():
            bounds = tuple(float(component) for component in value)
            if (floor_id not in self.floor_heights or len(bounds) != 4
                    or not all(math.isfinite(component) for component in bounds)
                    or bounds[2]-bounds[0] <= 2*self.BODY_RADIUS
                    or bounds[3]-bounds[1] <= 2*self.BODY_RADIUS):
                raise ValueError("floor bounds require [xmin, ymin, xmax, ymax] and room for a pedestrian")
            self.floor_bounds[floor_id] = bounds
        self._states = {}
        for person_id in self.people:
            digest = hashlib.sha256(f"{seed}\0{person_id}".encode()).digest()
            self._states[person_id] = dict(
                rng=random.Random(int.from_bytes(digest[:16], "big")), path_index=0,
                sampled_at=None, observation=None, suspended=True, reactions=deque(),
                response=None, mode=None, started=False, next_sudden=math.inf,
                sudden=None, last_result=None, observed_velocity=None, separation=None,
            )
        self._last_now = None
        from .pedestrian_behavior import FreeWalking
        if any(person.behavior is not None for person in self.people.values()) and environment is None:
            raise ValueError('configured free walking requires approved environment geometry')
        self.behaviors = {key:FreeWalking(person,environment,seed) for key,person in self.people.items() if person.behavior is not None}

    @staticmethod
    def _event(events, event_type, time, **details):
        events.append({"type": event_type, "time": float(time), **details})

    def _sudden_wait(self, person, state):
        if not person.path or person.speed == 0 or person.sudden_probability == 0:
            return math.inf
        if person.sudden_probability == 1:
            return 0.
        # p is the probability of at least one onset in one eligible second.
        rate = -math.log1p(-person.sudden_probability)
        return state["rng"].expovariate(rate)

    def _sudden_events(self, person, state, now, events):
        if not state["started"]:
            state["started"] = True
            state["next_sudden"] = now + self._sudden_wait(person, state)
        # Every cycle contains >=0.85 s of action/cooldown, so ordinary time
        # steps cannot produce an unbounded number of sudden transitions.
        transitions = 0
        while True:
            active = state["sudden"]
            if active is not None:
                if now+1e-10 < active["until"]:
                    break
                self._event(events, "sudden_end", active["until"], action=active["action"])
                state["sudden"] = None
                state["next_sudden"] = active["until"] + self.SUDDEN_COOLDOWN + self._sudden_wait(person, state)
            elif now+1e-10 >= state["next_sudden"]:
                rng = state["rng"]
                action = rng.choice(("pause", "turn"))
                duration = rng.uniform(.35, 1.2) if action == "pause" else rng.uniform(.35, .9)
                angle = rng.choice((-math.pi/2, -math.pi/3, math.pi/3, math.pi/2)) if action == "turn" else 0.
                start = state["next_sudden"]
                state["sudden"] = dict(action=action, angle=angle, until=start+duration)
                self._event(events, "sudden_start", start, action=action, duration=duration, angle=angle)
            else:
                break
            transitions += 1
            if transitions > 10000:
                raise ValueError("time jump exceeds 10000 pedestrian behavior transitions")

    def _normalize(self, person, now, reading):
        if not isinstance(reading, Mapping):
            raise ValueError("missing_perception")
        if reading.get("person_id", person.id) != person.id:
            raise ValueError("wrong_person")
        try:
            stamp = float(reading["sampled_at"])
            position = _xyz(reading["position"])
        except (KeyError, TypeError, ValueError, OverflowError) as exc:
            raise ValueError("invalid_perception") from exc
        if not math.isfinite(stamp) or stamp > now+1e-6:
            raise ValueError("future_perception")
        if now-stamp > self.stale_after:
            raise ValueError("stale_perception")
        if reading.get("floor_id", person.floor_id) != person.floor_id:
            raise ValueError("floor_mismatch")
        # Authored people's torso origin is 0.85 m above the declared floor.
        if abs(position[2]-(self.floor_heights[person.floor_id]+.85)) > .5:
            raise ValueError("floor_height_mismatch")
        values = reading.get("neighbors")
        if not isinstance(values, (list, tuple)):
            raise ValueError("invalid_perception")
        neighbors = []
        for value in values:
            if not isinstance(value, Mapping):
                raise ValueError("invalid_neighbor")
            if value.get("id") == person.id:
                continue
            if value.get("kind") not in ("robot", "person"):
                continue
            if value.get("floor_id", person.floor_id) != person.floor_id:
                continue
            try:
                pos = _xyz(value["position"])
                vel = _xyz(value.get("velocity", (0, 0, 0)))
                radius = float(value.get("radius", .22 if value["kind"] == "person" else .4))
            except (KeyError, TypeError, ValueError, OverflowError) as exc:
                raise ValueError("invalid_neighbor") from exc
            if not math.isfinite(radius) or radius <= 0:
                raise ValueError("invalid_neighbor")
            # Vertical separation also protects callers omitting neighbor floor.
            if abs(pos[2]-position[2]) > 1.5 or math.hypot(pos[0]-position[0], pos[1]-position[1]) > self.perception_range:
                continue
            neighbors.append(dict(id=str(value.get("id", "unknown")), kind=value['kind'], position=pos, velocity=vel, radius=radius))
        return dict(sampled_at=stamp, position=position, neighbors=neighbors)

    def _nominal(self, person, state, position, events, now, fresh):
        if not person.path or person.speed == 0:
            return (0., 0.), "stationary"
        # A planar torso-slide model cannot follow vertical or inter-floor paths.
        if any(abs(point.z) > 1e-6 for point in person.path):
            return (0., 0.), "unsupported_vertical_path"
        target = person.path[state["path_index"]]
        if fresh and math.hypot(target.x-position[0], target.y-position[1]) <= self.WAYPOINT_TOLERANCE:
            old = state["path_index"]
            state["path_index"] = (old+1) % len(person.path)
            if len(person.path) > 1:
                self._event(events, "waypoint_reached", now, index=old, next_index=state["path_index"])
            target = person.path[state["path_index"]]
        dx, dy = target.x-position[0], target.y-position[1]
        distance = math.hypot(dx, dy)
        if distance <= self.WAYPOINT_TOLERANCE:
            return (0., 0.), "at_waypoint"
        bounds = self.floor_bounds.get(person.floor_id)
        if bounds and not (bounds[0]+self.BODY_RADIUS <= target.x <= bounds[2]-self.BODY_RADIUS
                           and bounds[1]+self.BODY_RADIUS <= target.y <= bounds[3]-self.BODY_RADIUS):
            return (0., 0.), "path_outside_bounds"
        # Slow near the waypoint to avoid high-speed overshoot.
        speed = min(person.speed, distance/.35)
        return (speed*dx/distance, speed*dy/distance), "walking"

    def _hazard(self, person, reading, nominal):
        if not person.avoidance:
            return None
        position = reading["position"]
        candidates = []
        for neighbor in reading["neighbors"]:
            dx, dy = neighbor["position"][0]-position[0], neighbor["position"][1]-position[1]
            distance = math.hypot(dx, dy)
            combined = self.BODY_RADIUS+neighbor["radius"]
            relative = (neighbor["velocity"][0]-nominal[0], neighbor["velocity"][1]-nominal[1])
            speed2 = relative[0]**2+relative[1]**2
            closest_time = max(0., min(1.2, -(dx*relative[0]+dy*relative[1])/speed2)) if speed2 > 1e-9 else 0.
            closest = math.hypot(dx+relative[0]*closest_time, dy+relative[1]*closest_time)
            if distance <= combined+.25:
                candidates.append(dict(action="stop", neighbor_id=neighbor["id"], neighbor_kind=neighbor["kind"], distance=distance, delta=(dx, dy)))
            elif closest <= combined+.45 and distance <= combined+1.25:
                candidates.append(dict(action="avoid", neighbor_id=neighbor["id"], neighbor_kind=neighbor["kind"], distance=distance, delta=(dx, dy)))
        if not candidates:
            return None
        return min(candidates, key=lambda value: (value["action"] != "stop", value["distance"], value["neighbor_id"]))

    def _bounded(self, person, position, velocity, dt):
        bounds = self.floor_bounds.get(person.floor_id)
        if bounds is None:
            return velocity, None
        low = (bounds[0]+self.BODY_RADIUS, bounds[1]+self.BODY_RADIUS)
        high = (bounds[2]-self.BODY_RADIUS, bounds[3]-self.BODY_RADIUS)
        if any(position[axis] < low[axis]-1e-6 or position[axis] > high[axis]+1e-6 for axis in (0, 1)):
            return (0., 0.), "outside_bounds"
        horizon = max(.35, min(dt, 1.))
        result = tuple(max((low[axis]-position[axis])/horizon,
                           min((high[axis]-position[axis])/horizon, velocity[axis])) for axis in (0, 1))
        changed = any(abs(result[axis]-velocity[axis]) > 1e-9 for axis in (0, 1))
        return result, "boundary_limited" if changed else None

    def _separate_people(self, person, state, reading, nominal, now, fresh, dt):
        """Leave a close-person stop without authorizing motion toward an actor.

        Only configured walkers opt in. This uses delivered observations, never
        world state, and does not relax the existing stop/physical radii. A
        nearby robot, overlap, missing fresh sample or blocked geometry holds.
        An accepted direction persists until the peer is beyond the avoidance
        margin; random destination changes cannot immediately reverse it.
        """
        behavior = self.behaviors.get(person.id)
        if behavior is None or not person.avoidance:
            return None
        position = reading["position"]
        neighbors = reading["neighbors"]
        close = [n for n in neighbors if n["kind"] == "person" and
                 math.dist(position[:2], n["position"][:2]) <= self.BODY_RADIUS+n["radius"]+.25]
        episode = state["separation"]
        if episode is not None:
            peer = next((n for n in neighbors if n["id"] == episode["peer_id"] and n["kind"] == "person"), None)
            if peer is None:
                state["separation"] = None
                return (0., 0.), "yielding", "separation_observation_lost"
            if math.dist(position[:2], peer["position"][:2]) > self.BODY_RADIUS+peer["radius"]+.45:
                state["separation"] = episode = None
        if episode is None and not close:
            return None
        # A scheduled pause, reached destination, or zero configured speed is
        # an intention to remain stationary, not permission to escape it.
        if nominal == (0., 0.):
            return None
        response = state["response"]
        if response is not None and response["action"] == "stop" and response.get("neighbor_kind") == "robot":
            return (0., 0.), "yielding", "stop:"+response["neighbor_id"]
        if episode is None:
            peer = min(close, key=lambda n: (math.dist(position[:2], n["position"][:2]), n["id"]))
            episode = dict(peer_id=peer["id"], direction=None)
            state["separation"] = episode
        reason = "separation_blocked:"+episode["peer_id"]
        age = now-reading["sampled_at"]
        if not fresh or age > min(.1, self.stale_after):
            return (0., 0.), "yielding", "separation_awaiting_fresh_observation"
        # Brake existing approach inertia before the first separation command.
        # Velocity is estimated from consecutive delivered position samples.
        if episode["direction"] is None and (state["observed_velocity"] is None or
                math.hypot(*state["observed_velocity"]) > .05):
            return (0., 0.), "yielding", "separation_settling:"+episode["peer_id"]
        if any(n["kind"] == "robot" and math.dist(position[:2], n["position"][:2]) <=
               self.BODY_RADIUS+n["radius"]+.25 for n in neighbors):
            return (0., 0.), "yielding", "separation_robot_stop"
        peer = next(n for n in neighbors if n["id"] == episode["peer_id"])
        dx, dy = position[0]-peer["position"][0], position[1]-peer["position"][1]
        distance = math.hypot(dx, dy)
        if distance <= self.BODY_RADIUS+peer["radius"]:
            return (0., 0.), "yielding", reason
        away = (dx/distance, dy/distance)
        speed = min(.15, math.hypot(*nominal))
        horizon = max(1.2, person.reaction_time+.5)+age
        directions = [episode["direction"]] if episode["direction"] is not None else []
        # Finite local choices. Every candidate still passes the same complete
        # observation and continuous static-segment checks below.
        offsets = [0]+[sign*step for step in range(1, 8) for sign in (1, -1)]+[8]
        for offset in offsets:
            angle = offset*math.pi/8
            cosine, sine = math.cos(angle), math.sin(angle)
            directions.append((away[0]*cosine-away[1]*sine, away[0]*sine+away[1]*cosine))
        for direction in directions:
            velocity = (speed*direction[0], speed*direction[1])
            velocity, _ = self._bounded(person, position, velocity, dt)
            # Check the final bounded velocity, not the pre-clipped candidate.
            # An angular tolerance rejects floating-point cos(pi/2) as a
            # fictitious outward component, without imposing a minimum speed.
            if velocity[0]*away[0]+velocity[1]*away[1] <= speed*1e-12:
                continue
            clear = True
            for neighbor in neighbors:
                x, y = neighbor["position"][0]-position[0], neighbor["position"][1]-position[1]
                center = math.hypot(x, y)
                combined = self.BODY_RADIUS+neighbor["radius"]
                if center <= combined:
                    clear = False; break
                relative = (neighbor["velocity"][0]-velocity[0], neighbor["velocity"][1]-velocity[1])
                if center <= combined+.45:
                    # Both the command itself and observed relative motion
                    # must not reduce any close actor's existing separation.
                    if x*velocity[0]+y*velocity[1] > 0 or x*relative[0]+y*relative[1] < 0:
                        clear = False; break
                speed2 = relative[0]**2+relative[1]**2
                closest_time = max(0., min(horizon, -(x*relative[0]+y*relative[1])/speed2)) if speed2 else 0.
                closest = math.hypot(x+relative[0]*closest_time, y+relative[1]*closest_time)
                if closest < min(center, combined+.25):
                    clear = False; break
            target = dict(x=position[0]+velocity[0]*horizon, y=position[1]+velocity[1]*horizon)
            if not clear or not behavior.navigator.segment_clear(dict(x=position[0], y=position[1]), target):
                continue
            magnitude = math.hypot(*velocity)
            episode["direction"] = (velocity[0]/magnitude, velocity[1]/magnitude)
            return velocity, "separating", "separating_from:"+episode["peer_id"]
        return (0., 0.), "yielding", reason

    def _result(self, person, state, now, events, velocity=(0., 0.), mode="perception_hold", reason=None):
        if state["mode"] != mode:
            self._event(events, "pedestrian_mode", now, previous=state["mode"], mode=mode, reason=reason or mode)
            state["mode"] = mode
        result = dict(vx=float(velocity[0]), vy=float(velocity[1]), events=events, mode=mode,
                      path_index=state["path_index"], reason=reason or mode,
                      sensor_model="ideal_local_proximity", controller_version=self.VERSION)
        behavior=self.behaviors.get(person.id)
        if behavior:result['controller_version']='seeded-map-pedestrian-v1'
        result.update(behavior=person.behavior.mode if behavior else 'legacy',
                      destination=deepcopy(behavior.destination) if behavior else (person.path[state['path_index']].model_dump() if person.path else None),
                      allowed_floor_ids=list(person.behavior.allowed_floor_ids or [person.floor_id]) if behavior else [person.floor_id],
                      allowed_zone_ids=list(person.behavior.allowed_zone_ids) if behavior else [],
                      movement_model='planar_same_floor_actuator; no pedestrian stairs/elevator controller')
        state["last_result"] = deepcopy(result)
        return result

    def _robot_safety(self, person, reading, velocity, behavior, dt):
        """Bound a free walker's command against imminent observed robot motion.

        Behavioral reaction delay still governs ordinary yielding. This local
        safety envelope only constrains an imminent command, using delivered
        perception and reachable, statically clear positions; it never moves
        the person or changes a robot command directly.
        """
        robots=[n for n in reading['neighbors'] if n['kind']=='robot']
        if not robots or velocity==(0.,0.):return velocity,None
        x,y=reading['position'][:2]
        horizon=min(1.,max(.5,person.reaction_time+.25))
        def clearance(candidate):
            return min(math.hypot(n['position'][0]-x+(n['velocity'][0]-candidate[0])*time,
                                  n['position'][1]-y+(n['velocity'][1]-candidate[1])*time)
                       -self.BODY_RADIUS-n['radius']
                       for n in robots for time in (0.,horizon/2,horizon))
        # The robot's safety target is a *physical* clearance, while this
        # controller sees sampled poses and commands a moving physics body.
        # Reserve one short reaction margin before permitting the nominal walk.
        guard_clearance=self.desired_robot_clearance_m+.12
        if clearance(velocity)>=guard_clearance:return velocity,None
        nearest=min(robots,key=lambda n:math.hypot(n['position'][0]-x,n['position'][1]-y)-n['radius'])
        dx,dy=x-nearest['position'][0],y-nearest['position'][1]
        distance=math.hypot(dx,dy)
        if distance<1e-9:return (0.,0.),'robot_safety_hold'
        ux,uy=dx/distance,dy/distance
        speed=min(.7,max(.25,math.hypot(*velocity)))
        candidates=[(speed*ux,speed*uy),(-speed*uy,speed*ux),(speed*uy,-speed*ux),(0.,0.)]
        safe=[]
        for candidate in candidates:
            bounded,_=self._bounded(person,reading['position'],candidate,dt)
            if bounded!=candidate or behavior.constrain(reading['position'],bounded)!=bounded:continue
            safe.append((clearance(bounded),bounded))
        if not safe:return (0.,0.),'robot_safety_hold'
        best,command=max(safe,key=lambda item:(item[0],-math.hypot(*item[1])))
        # Avoid turning an uncertain model estimate into permission to squeeze
        # through a person/robot. A zero command is the fail-closed outcome.
        if best<guard_clearance:
            # A person already inside the margin may still recover by moving
            # away. Require every observed robot's predicted gap to stay at
            # least as large as its present gap throughout the same horizon.
            for robot in robots:
                start=math.hypot(robot['position'][0]-x,robot['position'][1]-y)
                if any(math.hypot(robot['position'][0]-x+(robot['velocity'][0]-command[0])*time,
                                  robot['position'][1]-y+(robot['velocity'][1]-command[1])*time)<start-1e-6
                       for time in (horizon/2,horizon)):
                    return (0.,0.),'robot_safety_hold'
        return command,'robot_safety_avoid' if command!=(0.,0.) else 'robot_safety_hold'

    def _yield_from_stopped_robot(self, person, reading, behavior, dt):
        """Let a free walker clear a stopped robot's lane using fresh perception.

        Both controllers can otherwise wait forever: the robot waits for the
        pedestrian while the pedestrian's delayed stop response commands zero.
        This only permits a slow, statically clear move *away* from a stationary
        observed robot; a close overlap or a moving robot still holds position.
        """
        robots=[n for n in reading['neighbors'] if n['kind']=='robot']
        if not robots or behavior.speed<=0:return None
        position=reading['position'];x,y=position[:2]
        nearest=min(robots,key=lambda n:math.hypot(x-n['position'][0],y-n['position'][1])-n['radius'])
        dx,dy=x-nearest['position'][0],y-nearest['position'][1]
        distance=math.hypot(dx,dy)
        gap=distance-self.BODY_RADIUS-nearest['radius']
        if (distance<1e-9 or not .2<=gap<.9 or
                math.hypot(*nearest['velocity'][:2])>.05):return None
        speed=min(.3,behavior.speed)
        command=(speed*dx/distance,speed*dy/distance)
        bounded,_=self._bounded(person,position,command,dt)
        if bounded!=command or behavior.constrain(position,command)!=command:return None
        # Check every observed robot, including those beside or behind the
        # preferred direction. Do not turn an escape heuristic into overlap.
        for robot in robots:
            for horizon in (0.,.5,1.):
                separation=math.hypot(robot['position'][0]+robot['velocity'][0]*horizon-x-command[0]*horizon,
                                      robot['position'][1]+robot['velocity'][1]*horizon-y-command[1]*horizon)
                if separation-self.BODY_RADIUS-robot['radius']<.2:return None
        return command

    def update(self, now, perceptions):
        now = float(now)
        if not math.isfinite(now) or (self._last_now is not None and now < self._last_now):
            raise ValueError("pedestrian time must be finite and monotonic")
        dt = 0. if self._last_now is None else now-self._last_now
        self._last_now = now
        readings = perceptions if isinstance(perceptions, Mapping) else {}
        output = {}
        for person_id, person in self.people.items():
            state = self._states[person_id]
            events = []
            if person_id not in self.behaviors:self._sudden_events(person, state, now, events)
            try:
                reading = self._normalize(person, now, readings.get(person_id))
                stamp = reading["sampled_at"]
                if state["sampled_at"] is not None and stamp < state["sampled_at"]:
                    raise ValueError("reordered_perception")
                fresh = state["sampled_at"] is None or stamp > state["sampled_at"]
                if state["suspended"] and not fresh:
                    raise ValueError("awaiting_fresh_perception")
            except ValueError as error:
                state["suspended"] = True
                output[person_id] = self._result(person, state, now, events, reason=str(error))
                continue
            if fresh:
                previous = state["observation"]
                elapsed = stamp-state["sampled_at"] if state["sampled_at"] is not None else 0.
                state["observed_velocity"] = tuple((reading["position"][axis]-previous["position"][axis])/elapsed
                    for axis in (0, 1)) if previous is not None and 0 < elapsed <= .1+1e-9 else None
                state["sampled_at"], state["observation"] = stamp, reading
                state["suspended"] = False
            else:
                reading = state["observation"]
            position = reading["position"]
            behavior=self.behaviors.get(person_id)
            nominal, mode = behavior.nominal(position,reading,now,events) if behavior else self._nominal(person, state, position, events, now, fresh)
            if fresh:
                response = self._hazard(person, reading, nominal)
                state["reactions"].append((now+person.reaction_time, response))
            while state["reactions"] and state["reactions"][0][0] <= now+1e-9:
                _, state["response"] = state["reactions"].popleft()
            velocity = nominal
            sudden = state["sudden"]
            if sudden and mode == "walking":
                if sudden["action"] == "pause":
                    velocity, mode = (0., 0.), "sudden_pause"
                else:
                    cosine, sine = math.cos(sudden["angle"]), math.sin(sudden["angle"])
                    velocity = (nominal[0]*cosine-nominal[1]*sine, nominal[0]*sine+nominal[1]*cosine)
                    mode = "sudden_turn"
            response = state["response"]
            reason = mode
            if response is not None and person.avoidance and nominal != (0., 0.):
                reason = f"{response['action']}:{response['neighbor_id']}"
                if response["action"] == "stop":
                    velocity, mode = (0., 0.), "yielding"
                elif mode != "sudden_pause":
                    speed = math.hypot(*nominal)
                    ux, uy = nominal[0]/speed, nominal[1]/speed
                    # Keep right relative to travel. Opposing pedestrians then
                    # choose opposite world-space sides without shared state.
                    velocity = ((.45*ux+.55*uy)*speed, (.45*uy-.55*ux)*speed)
                    mode = "avoiding"
            separation = self._separate_people(person, state, reading, nominal, now, fresh, dt)
            if separation is not None:
                velocity, mode, reason = separation
            velocity, boundary = self._bounded(person, position, velocity, dt)
            if behavior:
                safe=behavior.constrain(position,velocity)
                if safe!=velocity:velocity=safe;mode=reason='static_clearance_hold'
                if person.avoidance:
                    guarded,safety_mode=self._robot_safety(person,reading,velocity,behavior,dt)
                    if safety_mode:
                        velocity=guarded;mode=reason=safety_mode
                    if velocity==(0.,0.) and nominal!=(0.,0.) and mode in ('yielding','robot_safety_hold','static_clearance_hold'):
                        escape=self._yield_from_stopped_robot(person,reading,behavior,dt)
                        if escape is not None:velocity=escape;mode=reason='robot_safety_yield'
            if boundary:
                mode = reason = boundary
            output[person_id] = self._result(person, state, now, events, velocity, mode, reason)
        return output
