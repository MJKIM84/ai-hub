"""Charging approach routes from accepted observations, never hidden truth.

Peer disks are a per-call snapshot. Tracking/normal-delay allowances improve
planning clearance but are not a bound on noisy sensors or moving obstacles.
Only an explicit queue forecast may project a healthy predecessor to its
committed exit. Actual motion always rechecks the observed occupied space.
"""
from .navigation import radius, path_clear_of_disks
from .charging_target import finite


class ChargingTraffic:
    def __init__(self, control):
        self.control = control

    def _ahead(self, station_id, robot_id):
        c = self.control
        station = c.manager.stations.get(station_id)
        if station is None:
            return set()
        order = []
        for rid, plan in sorted(c.plans.items(), key=lambda pair: pair[1]['requested_at']):
            request = c.manager.requests.get(plan.get('request_id'))
            if (plan.get('station_id') == station_id and request is not None
                    and request.station_id == station_id and request.robot_id == rid
                    and request.status == 'completed' and request.phase == 'done'
                    and plan.get('clearing')):
                order.append(rid)
        if station.active is not None:
            order.append(station.active.robot_id)
        order.extend(request.robot_id for request in station.queue)
        ahead = set()
        for rid in order:
            if rid == robot_id:
                break
            ahead.add(rid)
        return ahead

    def _valid_observation(self, rid, now):
        c = self.control
        if rid in c.energy_observation_errors:
            return None
        obs = c.energy_observations.get(rid)
        if not isinstance(obs, dict) or obs.get('robot_id') != rid:
            return None
        stamp = obs.get('sampled_at')
        pose = obs.get('pose')
        if (not finite(stamp) or stamp < 0 or stamp > now
                or now - stamp > c.owner.policy.stale_after
                or not isinstance(pose, dict)
                or any(not finite(pose.get(key)) for key in ('x', 'y', 'z', 'yaw'))):
            return None
        return obs

    def disks(self, robot, floor_id, station_id, now, planning=False):
        c = self.control
        owner = c.owner
        if not finite(now) or now < 0 or floor_id not in owner.planner.floors:
            return None, 'invalid_traffic_context'
        ahead = self._ahead(station_id, robot.id) if planning else set()
        own = self._valid_observation(robot.id, now)
        age = now - own['sampled_at'] if own is not None else owner.policy.stale_after
        result = []
        for other_id, peer in owner.robots.items():
            if other_id == robot.id:
                continue
            obs = self._valid_observation(other_id, now)
            # A declared initial floor is no evidence of a missing robot's
            # current floor. Missing/stale/invalid reports cannot clear space.
            if obs is None:
                return None, 'peer_observation_unavailable'
            if owner._floor(obs['pose']['z']) != floor_id:
                continue
            pose = obs['pose']
            plan = c.plans.get(other_id, {})
            state = owner.robot_states[other_id]
            request = c.manager.requests.get(plan.get('request_id'))
            if (other_id in ahead and plan.get('station_id') == station_id
                    and request is not None and request.robot_id == other_id
                    and request.station_id == station_id
                    and request.status in ('queued', 'running', 'completed')
                    and request.phase not in ('fault', 'cancelled')
                    and not request.cancel_requested
                    and state['status'] == 'charging' and not state['operator_hold']
                    and not plan.get('interrupted') and obs.get('fault') == 'none'
                    and finite(obs.get('battery')) and obs['battery'] > 0
                    and finite(obs.get('upright')) and obs['upright'] >= .45):
                exit_pose = c._reserved_egress(plan)
                if (isinstance(exit_pose, dict)
                        and all(finite(exit_pose.get(key)) for key in ('x', 'y', 'z', 'yaw'))
                        and owner._floor(exit_pose['z']) == floor_id):
                    pose = exit_pose
            physics = c.project.physics
            speed = min(.3, robot.max_speed, owner.policy.speed_limit)
            delay = max(age, now - obs['sampled_at']) + 1 / physics.orchestration_hz + robot.sensors.communication_delay + 1 / physics.control_hz
            allowance = .08 + 3 * (robot.sensors.position_noise + peer.sensors.position_noise) + speed * delay
            clearance = radius(robot) + radius(peer) + owner.policy.safety_distance + allowance
            if not finite(clearance) or clearance < 0:
                return None, 'invalid_traffic_clearance'
            result.append((pose['x'], pose['y'], clearance))
        return tuple(result), None

    def route(self, robot, observation, target, floor_id, station_id, now, planning=False):
        owner = self.control.owner
        disks, reason = self.disks(robot, floor_id, station_id, now, planning=planning)
        if disks is None:
            return None, reason
        route = owner._route(robot, observation, target, floor_id)
        if route is None:
            return None, 'approach_route_unavailable'
        if path_clear_of_disks(observation['pose'], [*route, target], disks):
            return route, None
        # A guided vehicle can wait for its authored route, never cut across
        # free space to get around an occupied segment.
        if robot.model_id == 'agv':
            return None, 'guided_approach_occupied'
        route = owner.planner.path(observation['pose'], target, floor_id, robot, peer_disks=disks)
        return (route, None) if route is not None else (None, 'approach_traffic_blocked')
