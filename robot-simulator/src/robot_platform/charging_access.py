"""Service access and exit routing from configuration and accepted observations.

Long-term parking must preserve another guided robot's future charger access.
This does not reserve a whole lane against crossing traffic: only the final
parking footprint is excluded. Moving peers still require live route checks.
"""
from copy import deepcopy
import math

from .catalog import model_by_id
from .guided_route import DirectedRoute, GuidedRouteError
from .navigation import path_clear_of_disks, radius


def parking_blocks_service(control, rid, target, floor):
    owner = control.owner
    robot = owner.robots[rid]
    # Configuration is immutable within a Session. Including its values also
    # keeps isolated configuration-edit callers from reusing an obsolete lane.
    signature = (floor, repr(control.project.environment.model_dump()),
                 repr(control.geometry),
                 tuple((r.id,r.model_id,r.floor_id,repr(r.agv_route),r.group,
                        r.payload_mass,repr(r.equipment)) for r in owner.robots.values()))
    cache = getattr(control, '_service_access_cache', None)
    if cache is None or cache[0] != signature:
        corridors=[]
        for peer_id, peer in owner.robots.items():
            if peer.model_id != 'agv' or peer.floor_id != floor:
                continue
            try:
                authored=DirectedRoute([point.model_dump() for point in peer.agv_route])
            except GuidedRouteError:
                continue
            model=model_by_id(peer.model_id)
            mass=model['mass']+peer.payload_mass+sum(e.mass for e in peer.equipment)
            for station_id, element in control.manager.elements.items():
                geometry=control.geometry.get((peer_id,station_id))
                if (geometry is None or element.floor_id != floor
                        or not element.facility.automatic or mass > element.facility.max_load
                        or peer.payload_mass > model['max_payload']
                        or element.allowed_groups and peer.group not in element.allowed_groups
                        or authored.waypoint(geometry['staging']) is None):
                    continue
                for begin,end in zip(authored.points,authored.points[1:]):
                    previous=deepcopy(owner.guided_rejections)
                    try:
                        route=owner._route(peer,{'pose':dict(end,z=geometry['staging']['z'])},geometry['staging'],floor)
                        edge=owner._route(peer,{'pose':dict(begin,z=geometry['staging']['z'])},end,floor)
                    finally:
                        owner.guided_rejections.clear();owner.guided_rejections.update(previous)
                    if route is not None and edge is not None:
                        corridors.append((peer_id,[begin,*edge,*route,geometry['staging']]))
        control._service_access_cache=(signature,corridors)
    for peer_id,points in control._service_access_cache[1]:
        if peer_id==rid:continue
        clearance=radius(robot)+radius(owner.robots[peer_id])+owner.policy.safety_distance
        if control._path_near_point(points,target,clearance):return True
    return False


def initial_exit_anchor_valid(control, observation, plan):
    """Only the normal release envelope may join an unstarted committed exit.

    Once a remaining path exists, its consumed progress is authoritative. This
    check must never bring an already consumed staging anchor back into it.
    """
    committed=plan.get('egress_route')
    if not plan.get('clearing') or 'egress_remaining' in plan or not committed:
        return True
    try:
        pose=observation['pose'];anchor=committed[0]
        values=[pose[key] for key in ('x','y')]+[anchor[key] for key in ('x','y')]
        if any(isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) for value in values):
            return False
        return math.hypot(pose['x']-anchor['x'],pose['y']-anchor['y']) <= control.manager.position_tolerance
    except (KeyError,TypeError,IndexError,OverflowError):
        return False


def exit_route(control, robot, observation, target, floor, now, plan=None,
               *, live=True, planning=False):
    """Budget and drive the same immutable accepted exit polyline.

An uncommitted AMR may select an observed-clear detour. After admission the
polyline is kept; a later obstruction is a wait/recovery condition, never an
unbudgeted replacement or a different parking reservation.
"""
    owner = control.owner
    plan = plan or {}
    committed = plan.get('egress_route')
    if committed:
        if not initial_exit_anchor_valid(control,observation,plan):
            return None
        # Before the first clearance command, staging is an unconsumed point
        # of the accepted route. Normal .12 m release tolerance may leave a
        # robot just before it, beyond the motion follower's .08 m tolerance.
        # Subsequent calls use only saved progress, including an empty path.
        points = plan.get('egress_remaining',committed) if plan.get('clearing') else committed[1:]
        route = deepcopy(points)
    else:
        route = owner._route(robot, observation, target, floor)
    if route is None:
        return route
    # A recovered observation may no longer join the saved remaining route
    # safely. Validate that join without inventing an unbudgeted replacement.
    if committed and not owner.planner.path_clear(observation['pose'], [*route, target], floor, robot):
        return None
    if not live:
        return route
    disks, _ = control.traffic.disks(robot, floor, plan.get('station_id'), now, planning=planning)
    if disks is None:
        return None
    if path_clear_of_disks(observation['pose'], [*route, target], disks):
        return route
    if committed or robot.model_id == 'agv':
        return None
    return owner.planner.path(observation['pose'], target, floor, robot, peer_disks=disks)
