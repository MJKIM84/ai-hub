"""Shared observed-point translation limits and static route time estimates.

The m/s limit caps requested XY translation, not angular/joint/elevator motion.
Delayed observations, inertia, acceleration and traffic prevent treating either
this cap as an instantaneous physical-speed bound or these times as guarantees.
"""
import math
from .catalog import model_by_id


def _finite(value):
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def _xy(pose):
    if not isinstance(pose, dict) or not all(_finite(pose.get(k)) for k in ('x', 'y')):
        raise ValueError('invalid_position')
    if any(k in pose and not _finite(pose[k]) for k in ('z', 'yaw')):
        raise ValueError('invalid_pose')
    return pose['x'], pose['y']


def _base_limit(robot, policy, cap):
    values = [robot.max_speed, policy.speed_limit, model_by_id(robot.model_id)['max_speed']]
    if cap is not None:
        values.append(cap)
    if any(not _finite(v) or v < 0 for v in values):
        raise ValueError('invalid_speed_limit')
    return min(values)


def _zones(environment, floor_id):
    return [] if environment is None else [zone for zone in environment.elements
        if zone.kind == 'speed_zone' and zone.floor_id == floor_id]


def _local(zone, pose):
    x, y = _xy(pose)
    if (not all(_finite(v) for v in (zone.pose.x, zone.pose.y, zone.pose.yaw,
            zone.size.x, zone.size.y, zone.speed_limit))
            or min(zone.size.x, zone.size.y, zone.speed_limit) <= 0):
        raise ValueError('invalid_speed_zone')
    c, s = math.cos(zone.pose.yaw), math.sin(zone.pose.yaw)
    dx, dy = x - zone.pose.x, y - zone.pose.y
    result = (c * dx + s * dy, -s * dx + c * dy)
    if not all(_finite(v) for v in result):
        raise ValueError('invalid_zone_position')
    # The transform can cancel world coordinates much larger than its local
    # edge coordinate. Local-value ULPs alone understate that round-off.
    rounding = 4 * max(math.ulp(v) for v in
        (x, y, zone.pose.x, zone.pose.y, dx, dy, *result))
    halves = (zone.size.x / 2, zone.size.y / 2)
    if rounding >= min(halves):
        raise ValueError('unresolvable_zone_precision')
    return tuple(_closed_coordinate(value, half, rounding)
        for value, half in zip(result, halves))


def _closed_coordinate(value, half, rounding=0.):
    """Snap representational rounding at a closed edge, without metric padding."""
    if abs(abs(value) - half) <= max(rounding, 4 * max(math.ulp(value), math.ulp(half))):
        return math.copysign(half, value)
    return value


def _contains(zone, pose):
    x, y = _local(zone, pose)
    return abs(x) <= zone.size.x / 2 and abs(y) <= zone.size.y / 2


def zones_at(environment, pose, floor_id):
    _xy(pose)
    return [zone for zone in _zones(environment, floor_id) if _contains(zone, pose)]


def limit_at(robot, policy, environment, pose, floor_id, cap=None):
    """Fail closed for malformed observation/configuration; never raise a cap."""
    try:
        return min([_base_limit(robot, policy, cap),
            *(zone.speed_limit for zone in zones_at(environment, pose, floor_id))])
    except (ValueError, TypeError, KeyError, OverflowError):
        return 0.


def observed_limit(robot, policy, environment, observation, now):
    """Current observation's environment cap, independent of requested speed."""
    model_limit = model_by_id(robot.model_id)['max_speed']
    report = dict(version='observed-motion-limit-v1', sampled_at=None, assessed_at=now,
        status='unknown', floor_id=None, limit_m_s=None, model_limit_m_s=model_limit,
        robot_limit_m_s=robot.max_speed, policy_limit_m_s=policy.speed_limit,
        zone_ids=[], reason='missing_or_stale_motion_observation')
    if not isinstance(observation, dict):
        return report
    stamp = observation.get('sampled_at')
    if _finite(stamp):
        report['sampled_at'] = stamp
    if (not _finite(now) or not _finite(stamp) or stamp < 0 or stamp > now + 1e-9
            or now - stamp > policy.stale_after):
        return report
    try:
        pose = observation.get('pose')
        _xy(pose)
        if not _finite(pose.get('z')):
            raise ValueError('invalid_pose')
        floor = min(environment.floors, key=lambda f: abs(pose['z'] - f.elevation - .35)).id
        active = zones_at(environment, pose, floor)
        base = _base_limit(robot, policy, None)
        report.update(status='known', reason=None, floor_id=floor,
            limit_m_s=min([base, *(z.speed_limit for z in active)]), zone_ids=[z.id for z in active])
    except (ValueError, TypeError, KeyError, OverflowError):
        report['reason'] = 'invalid_motion_observation_or_configuration'
    return report


def clamp_translation(requested, cap):
    if not _finite(requested) or not _finite(cap) or cap < 0:
        return 0.
    return math.copysign(min(abs(requested), cap), requested)


def _intersection(zone, start, end):
    """Closed Liang–Barsky interval in the rotated zone's local coordinates."""
    a, b = _local(zone, start), _local(zone, end)
    lo, hi = 0., 1.
    for origin, target, half in zip(a, b, (zone.size.x / 2, zone.size.y / 2)):
        # Use the same closed-edge interpretation as point membership. Without
        # this, a rounded, almost-parallel boundary can lose its true interval,
        # after which a single midpoint incorrectly classifies an unsplit leg.
        delta = target - origin
        if not _finite(delta):
            raise ValueError('invalid_segment_difference')
        if delta == 0:
            if abs(origin) > half:
                return None
            continue
        if max(origin, target) < -half or min(origin, target) > half:
            return None
        # Only crossing bounds restrict this segment. Avoid dividing by a
        # tiny delta for a far-away bound which never intersects it.
        enter = (-half - origin) / delta if origin < -half else (half - origin) / delta if origin > half else 0.
        leave = (-half - origin) / delta if target < -half else (half - origin) / delta if target > half else 1.
        if not _finite(enter) or not _finite(leave):
            # A tiny segment wholly on one side can yield infinite ratios.
            # Rejection is preferable to silently losing a real restriction.
            raise ValueError('invalid_zone_intersection')
        lo, hi = max(lo, enter), min(hi, leave)
        if lo > hi:
            return None
    return lo, hi


def _unknown(reason):
    return dict(known=False, reason=reason, seconds=None, distance_m=None,
        base_speed_limit_m_s=None, limited_distance_m=None, segments=[])


def translation_time(robot, policy, environment, start, path, floor_id, cap=None):
    """Split every segment at zone boundaries, including between waypoints."""
    try:
        base = _base_limit(robot, policy, cap)
        zones = _zones(environment, floor_id)
        points = [start, *path]
        for point in points:
            _xy(point)
        parts, total, limited, seconds = [], 0., 0., 0.
        for a, b in zip(points, points[1:]):
            dx, dy = b['x'] - a['x'], b['y'] - a['y']
            length = math.hypot(dx, dy)
            if not _finite(length):
                return _unknown('invalid_route_distance')
            if length == 0:
                continue
            if base == 0:
                return _unknown('translation_unavailable')
            cuts = {0., 1.}
            for zone in zones:
                crossing = _intersection(zone, a, b)
                if crossing is not None:
                    cuts.update(crossing)
            ordered = sorted(cuts)
            for lo, hi in zip(ordered, ordered[1:]):
                midpoint = (lo + hi) / 2
                pose = dict(x=a['x'] + dx * midpoint, y=a['y'] + dy * midpoint)
                active = [zone for zone in zones if _contains(zone, pose)]
                speed = min([base, *(zone.speed_limit for zone in active)])
                distance = length * (hi - lo)
                elapsed = distance / speed
                if not _finite(elapsed):
                    return _unknown('invalid_translation_time')
                parts.append(dict(distance_m=distance, seconds=elapsed,
                    speed_limit_m_s=speed, zone_ids=[zone.id for zone in active]))
                seconds += elapsed
                total += distance
                if speed < base:
                    limited += distance
        if not all(_finite(v) for v in (seconds, total, limited)):
            return _unknown('invalid_route_time_sum')
        return dict(known=True, reason=None, seconds=seconds, distance_m=total,
            base_speed_limit_m_s=base, limited_distance_m=limited, segments=parts)
    except (ValueError, TypeError, KeyError, OverflowError, ZeroDivisionError) as error:
        return _unknown(str(error) or 'invalid_route_time')


def _angle(value):
    if not _finite(value):
        raise ValueError('invalid_rotation')
    return (value + math.pi) % (2 * math.pi) - math.pi


def route_timing(robot, policy, environment, start, path, floor_id, final_yaw=None,
                 dwell=0., arrival_allowance=0., cap=None, turn_rate=.5):
    """Static serial turn allowance; moving turns may overlap translation.

    turn_rate is an explicit scheduling assumption. This does not reproduce
    proportional angular control, waypoint tolerance, acceleration or stopping.
    """
    result = translation_time(robot, policy, environment, start, path, floor_id, cap)
    if not result['known']:
        return result
    try:
        if (not _finite(start.get('yaw')) or not _finite(turn_rate) or turn_rate <= 0
                or not _finite(dwell) or dwell < 0
                or not _finite(arrival_allowance) or arrival_allowance < 0):
            return _unknown('invalid_timing_parameters')
        yaw, path_turn = start['yaw'], 0.
        for a, b in zip([start, *path], path):
            dx, dy = b['x'] - a['x'], b['y'] - a['y']
            if dx == 0 and dy == 0:
                continue
            heading = math.atan2(dy, dx)
            path_turn += abs(_angle(heading - yaw))
            yaw = heading
        alignment = abs(_angle(final_yaw - yaw)) if final_yaw is not None else 0.
        if model_by_id(robot.model_id)['locomotion'] == 'fixed' and path_turn + alignment > 0:
            return _unknown('fixed_base_rotation_unavailable')
        turn_seconds, align_seconds = path_turn / turn_rate, alignment / turn_rate
        seconds = result['seconds'] + turn_seconds + align_seconds + dwell + arrival_allowance
        if not all(_finite(v) for v in (path_turn, alignment, turn_seconds, align_seconds, seconds)):
            return _unknown('invalid_timing_sum')
        return dict(result, seconds=seconds, translation_seconds=result['seconds'],
            path_turn_radians=path_turn, path_turn_seconds=turn_seconds,
            final_alignment_radians=alignment, final_alignment_seconds=align_seconds,
            turn_radians=path_turn + alignment, dwell_seconds=dwell,
            arrival_allowance_seconds=arrival_allowance,
            basis='Static model/instance/policy/zone translation caps plus serial rotation allowance; excludes traffic, faults, acceleration, tracking error and observation/command delays; not calibrated or guaranteed')
    except (ValueError, TypeError, KeyError, OverflowError, ZeroDivisionError) as error:
        return _unknown(str(error) or 'invalid_route_timing')
