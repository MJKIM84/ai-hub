"""Pure observed waypoint planning for the compiled research arm contract.

No simulator state, item placement, actuator state, or reservation is changed.
This bounded planner checks kinematic margins and the known item's clearance;
it is not an environment obstacle map or a general collision planner.
"""
from copy import deepcopy
import math


class ArmMotionPlanError(ValueError):
    def __init__(self, code, evidence):
        self.code, self.evidence = code, evidence
        super().__init__(code)


def _xyz(value):
    result = tuple(float(v) for v in value)
    if len(result) != 3 or not all(math.isfinite(v) for v in result):
        raise ValueError('finite XYZ required')
    return result


def _inward(point, observation, distance):
    # This is a candidate direction only; the compiled transform, including
    # its offset and tilt, is used by the solver to accept or reject it.
    pose = observation['pose']
    dx, dy = pose['x']-point[0], pose['y']-point[1]
    length = math.hypot(dx, dy)
    if length <= distance:
        raise ValueError('inward candidate crosses arm base')
    return (point[0]+distance*dx/length, point[1]+distance*dy/length, point[2])


def _rotate(quaternion, vector):
    w, x, y, z = quaternion
    vx, vy, vz = vector
    return ((1-2*y*y-2*z*z)*vx+(2*x*y-2*z*w)*vy+(2*x*z+2*y*w)*vz,
            (2*x*y+2*z*w)*vx+(1-2*x*x-2*z*z)*vy+(2*y*z-2*x*w)*vz,
            (2*x*z-2*y*w)*vx+(2*y*z+2*x*w)*vy+(1-2*x*x-2*y*y)*vz)


def _multiply(a, b):
    w,x,y,z=a; v,i,j,k=b
    return (w*v-x*i-y*j-z*k, w*i+x*v+y*k-z*j,
            w*j-x*k+y*v+z*i, w*k+x*j-y*i+z*v)


def _segment_box_distance(begin, end, half_size):
    """Exact segment-to-axis-aligned-box distance, without sampling the segment."""
    delta = tuple(end[i]-begin[i] for i in range(3))
    cuts = {0., 1.}
    for i in range(3):
        if abs(delta[i]) > 1e-15:
            for boundary in (-half_size[i], half_size[i]):
                t = (boundary-begin[i])/delta[i]
                if 0. < t < 1.:
                    cuts.add(t)
    cuts = sorted(cuts)
    def squared(t):
        return sum(max(0.,abs(begin[i]+t*delta[i])-half_size[i])**2 for i in range(3))
    minimum = min(squared(t) for t in cuts)
    for lo, hi in zip(cuts, cuts[1:]):
        middle = (lo+hi)/2
        active = [(i,math.copysign(half_size[i],begin[i]+middle*delta[i])) for i in range(3)
                  if abs(begin[i]+middle*delta[i]) > half_size[i]]
        denominator = sum(delta[i]**2 for i,_ in active)
        if denominator:
            t = -sum((begin[i]-boundary)*delta[i] for i,boundary in active)/denominator
            minimum = min(minimum,squared(max(lo,min(hi,t))))
    return math.sqrt(minimum)


def _wrist_item_clearance(contract, tool, center, size, quaternion=None):
    capsule = contract['wrist_capsule']
    tool_q, tool_position = tool['tool_quaternion'], tool['tool_position']
    endpoints = []
    for sign in (-1,1):
        local = tuple(capsule['center_m'][i]+sign*capsule['half_length_m']*capsule['axis'][i] for i in range(3))
        rotated = _rotate(tool_q,local)
        relative = tuple(tool_position[i]+rotated[i]-center[i] for i in range(3))
        if quaternion is not None:
            relative = _rotate((quaternion[0],-quaternion[1],-quaternion[2],-quaternion[3]),relative)
        endpoints.append(relative)
    half = tuple(v/2 for v in size)
    if quaternion is None:
        half = (math.hypot(*size[:2])/2,math.hypot(*size[:2])/2,size[2]/2)
    return _segment_box_distance(*endpoints,half)-capsule['radius_m']


def _known_item_clearance(contract, tool, center, size, quaternion=None, *, with_details=False, finger_positions=None):
    """OBB separating-axis clearance, or an upright cylinder fallback.

    An observed orientation checks all 15 OBB separating axes. A positive
    projection gap lower-bounds Euclidean separation; requiring the clearance
    on one axis is conservative even for diagonally separated corners.
    Legacy observations without orientation use an upright XY bounding
    circle covering every yaw. This is not an arbitrary-tilt fallback.
    """
    gripper = contract['gripper']
    position, quat = tool['tool_position'], tool['tool_quaternion']
    local = _rotate((quat[0], -quat[1], -quat[2], -quat[3]),
                    tuple(center[i]-position[i] for i in range(3)))
    radius, halfheight = math.hypot(*size[:2])/2, size[2]/2
    axes = None
    if quaternion is not None:
        inverse = (quat[0], -quat[1], -quat[2], -quat[3])
        axes = [_rotate(inverse, _rotate(quaternion, axis)) for axis in ((1,0,0),(0,1,0),(0,0,1))]
    gap = math.inf
    limiting = None
    palm = gripper['palm_half_size_m']
    boxes = [((0., 0., 0.), palm)]
    offset = gripper['finger_center_offset_m']
    for side in (-1, 1):
        opening = .1 if finger_positions is None else finger_positions['left' if side == 1 else 'right']
        boxes.append(((offset[0], side*(abs(offset[1])+opening), offset[2]),
                      gripper['finger_half_size_m']))
    for box_index, (box, half) in enumerate(boxes):
        if axes is not None:
            tool_axes = ((1,0,0),(0,1,0),(0,0,1))
            separating = list(tool_axes)+axes
            for a in tool_axes:
                for b in axes:
                    axis = (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
                    length = math.sqrt(sum(v*v for v in axis))
                    if length > 1e-9:
                        separating.append(tuple(v/length for v in axis))
            separation = -math.inf
            for axis in separating:
                center_distance = abs(sum((local[i]-box[i])*axis[i] for i in range(3)))
                box_radius = sum(abs(axis[i])*half[i] for i in range(3))
                item_radius = sum(abs(sum(axes[j][i]*axis[i] for i in range(3)))*size[j]/2 for j in range(3))
                separation = max(separation, center_distance-box_radius-item_radius)
            if separation < gap:
                gap, limiting = separation, box_index
            continue
        horizontal = math.hypot(max(0., abs(local[0]-box[0])-half[0]),
                                max(0., abs(local[1]-box[1])-half[1]))-radius
        vertical = abs(local[2]-box[2])-half[2]-halfheight
        separation = max(horizontal, vertical)
        if separation < gap:
            gap, limiting = separation, box_index
    wrist_gap = _wrist_item_clearance(contract,tool,center,size,quaternion)
    limiting_name = ('palm','finger_negative','finger_positive')[limiting]
    if wrist_gap < gap:
        gap, limiting_name = wrist_gap, 'wrist_capsule'
    if with_details:
        return dict(gap_m=gap, limiting_gripper_box=limiting_name, wrist_capsule_clearance_m=wrist_gap,
                    item_center_tool_frame=list(local), tool_position=list(position),
                    tool_quaternion=list(quat), item_quaternion=list(quaternion) if quaternion is not None else None)
    return gap


def check_open_path(contract, observation, begin, end, item_position, item_size, *, noise=0., item_quaternion=None,
                    finger_positions=None, current_tool_quaternion=None,
                    current_joint_positions=None, start_joint_targets=None):
    """Recheck an open-gripper retreat against the latest visible item."""
    from .arm_kinematics import solve_observed, forward_observed, joint_path_margins, ArmKinematicsError
    valid_noise = type(noise) in (int,float) and math.isfinite(noise) and noise >= 0
    evidence = dict(source='observations_and_compiled_geometry', sampled_at=observation.get('sampled_at'),
                    begin=list(begin), end=list(end), item_position=list(item_position),
                    item_quaternion=(list(item_quaternion) if isinstance(item_quaternion,(list,tuple))
                        and all(type(v) in (int,float) and math.isfinite(v) for v in item_quaternion) else None),
                    minimum_clearance_m=.001+3*noise if valid_noise else None,
                    minimum_reach_margin_m=.015+3*noise if valid_noise else None)
    try:
        if not valid_noise:
            raise ValueError('invalid_noise')
        if (not isinstance(finger_positions,dict) or set(finger_positions) != {'left','right'}
                or any(type(v) not in (int,float) or not math.isfinite(v) for v in finger_positions.values())):
            raise ValueError('missing_or_invalid_actual_finger_positions')
        evidence['observed_finger_positions_m'] = deepcopy(finger_positions)
        if (not isinstance(current_tool_quaternion,(list,tuple)) or len(current_tool_quaternion) != 4
                or any(type(v) not in (int,float) or not math.isfinite(v) for v in current_tool_quaternion)
                or abs(sum(v*v for v in current_tool_quaternion)-1) > .001):
            raise ValueError('missing_or_invalid_actual_tool_orientation')
        if item_quaternion is None:
            raise ValueError('missing_item_orientation')
        if (not isinstance(item_quaternion,(list,tuple)) or len(item_quaternion) != 4
                or not all(type(v) in (int,float) and math.isfinite(v) for v in item_quaternion)
                or abs(sum(v*v for v in item_quaternion)-1) > .001):
            raise ValueError('invalid_item_quaternion')
        observed = _known_item_clearance(contract,dict(tool_position=begin,tool_quaternion=current_tool_quaternion),
            item_position,item_size,item_quaternion,finger_positions=finger_positions,with_details=True)
        evidence['observed_start_clearance'] = observed
        if observed['gap_m'] < .001+3*noise-1e-9:
            raise ValueError('observed_open_gripper_item_clearance')
        qa, qb = [solve_observed(contract, observation, p, margin_m=.015+3*noise,
                  joint_margin_rad=.02)['joint_targets'] for p in (begin, end)]
        starts = [('ideal_ik_fixture', qa)]
        if current_joint_positions is not None or start_joint_targets is not None:
            starts = []
            for name, values in (('observed_joints',current_joint_positions),
                                 ('delivered_joint_targets',start_joint_targets)):
                if (not isinstance(values,(list,tuple)) or len(values) != 4
                        or any(type(v) not in (int,float) or not math.isfinite(v) for v in values)):
                    raise ValueError('missing_or_invalid_'+name)
                for q, joint, actuator in zip(values, contract['joint_limits_rad'], contract['actuator_limits_rad']):
                    if q < max(joint[0],actuator[0])+.02 or q > min(joint[1],actuator[1])-.02:
                        raise ValueError('joint_margin')
                starts.append((name,list(values)))
            measured = forward_observed(contract,observation,current_joint_positions)
            if math.dist(measured['tool_position'],begin) > .002+3*noise:
                raise ValueError('inconsistent_observed_joint_pose')
            evidence['observed_joint_positions_rad'] = list(current_joint_positions)
            evidence['observed_joint_targets_rad'] = list(start_joint_targets)
        gap, sample_total = math.inf, 0
        sweeps = []
        gripper, lengths = contract['gripper'], contract['lengths']
        finger = [abs(c)+h+(max(abs(v) for v in finger_positions.values()) if i == 1 else 0.)
                  for i,(c,h) in enumerate(zip(gripper['finger_center_offset_m'],gripper['finger_half_size_m']))]
        capsule = contract['wrist_capsule']
        extent = max(math.sqrt(sum(v*v for v in gripper['palm_half_size_m'])),
                     math.sqrt(sum(v*v for v in finger)),
                     math.sqrt(sum(v*v for v in capsule['center_m']))+capsule['half_length_m']+capsule['radius_m'])
        tool_levers = [lengths['upper']+lengths['forearm']+lengths['tool']]*2+[
                      lengths['forearm']+lengths['tool'],lengths['tool']]
        shape_levers = [value+extent for value in tool_levers]
        for start_name, qa in starts:
            evidence['checking_start'] = start_name
            actual_margins = joint_path_margins(contract,qa,qb,margin_m=.015+3*noise,joint_margin_rad=.02)
            count = max(10, math.ceil(max(abs(a-b) for a,b in zip(qa,qb))/.01))
            sweep_gap = math.inf
            for index in range(count+1):
                q = [a+(b-a)*index/count for a,b in zip(qa,qb)]
                tool = forward_observed(contract, observation, q)
                solve_observed(contract, observation, tool['tool_position'], margin_m=.015+3*noise, joint_margin_rad=.02)
                sweep_gap = min(sweep_gap, _known_item_clearance(contract, tool, item_position, item_size, item_quaternion,
                                                               finger_positions=finger_positions))
                if sweep_gap < .001+3*noise-1e-9:
                    evidence['limiting_sample'] = dict(index=index, count=count+1, start=start_name,
                        **_known_item_clearance(contract,tool,item_position,item_size,item_quaternion,
                                               finger_positions=finger_positions,with_details=True))
                    raise ValueError('open_gripper_item_clearance')
            # A finite sample list alone can miss a collision between samples.
            # At an interval midpoint each box's separating plane (or capsule
            # distance) remains valid after subtracting a bound on *every*
            # robot point's motion. Sum(radius * joint angle) bounds that
            # motion along the four revolute joints, from compiled lengths
            # and the full open gripper/capsule extent. Wrist reach and joint
            # margins are independently certified above over the exact elbow
            # interval, without substituting a different fixed-pitch IK pose.
            pending = [(qa,qb,0)]
            intervals, extra_samples, certified_gap = 0, 0, math.inf
            while pending:
                if extra_samples >= 4096:
                    raise ValueError('uncertified_open_gripper_sweep')
                left, right, depth = pending.pop()
                middle = [(a+b)/2 for a,b in zip(left,right)]
                tool = forward_observed(contract,observation,middle)
                solve_observed(contract,observation,tool['tool_position'],margin_m=.015+3*noise,joint_margin_rad=.02)
                mid_gap = _known_item_clearance(contract,tool,item_position,item_size,item_quaternion,
                                                finger_positions=finger_positions)
                extra_samples += 1
                sweep_gap = min(sweep_gap,mid_gap)
                if mid_gap < .001+3*noise-1e-9:
                    evidence['limiting_sample'] = dict(start=start_name,interval_depth=depth,
                        **_known_item_clearance(contract,tool,item_position,item_size,item_quaternion,
                                               finger_positions=finger_positions,with_details=True))
                    raise ValueError('open_gripper_item_clearance')
                deltas = [abs(b-a)/2 for a,b in zip(left,right)]
                point_motion = sum(r*d for r,d in zip(shape_levers,deltas))
                lower_gap = mid_gap-point_motion
                if lower_gap >= .001+3*noise-1e-9:
                    intervals += 1
                    certified_gap = min(certified_gap,lower_gap)
                elif depth >= 18:
                    raise ValueError('uncertified_open_gripper_sweep')
                else:
                    pending.extend(((left,middle,depth+1),(middle,right,depth+1)))
            gap = min(gap,sweep_gap)
            sample_total += count+1+extra_samples
            sweeps.append(dict(start=start_name,samples=count+1+extra_samples,minimum_clearance_m=sweep_gap,
                certified_intervals=intervals,certified_clearance_lower_bound_m=certified_gap,
                actual_joint_path_margins=actual_margins))
        return dict(evidence, accepted=True, samples=sample_total, observed_item_clearance_m=observed['gap_m'],
                    planned_path_clearance_m=gap, sweeps=sweeps, joint_step_limit_rad=.01,
                    path_model='joint interpolation with bounded continuous geometric clearance; actual dynamics require physical contact audit')
    except (ArmKinematicsError, ValueError) as error:
        evidence.update(accepted=False, rejection=getattr(error,'code',str(error)))
        raise ArmMotionPlanError('arm_retract_clearance', evidence) from error


def select_open_retract(contract, observation, begin, planned_end, item_position, item_size, *,
                        current_joint_positions, start_joint_targets, **kwargs):
    """Select a fixed retreat endpoint from fresh release observations.

    Keep the planned tool height (derived from compiled finger/item geometry).
    If returning to its old XY would sweep through the settled item, also
    consider rising over the currently observed tool XY. This changes only
    the empty arm path, never the task's source or item destination.
    """
    begin, planned_end = _xyz(begin), _xyz(planned_end)
    evidence = dict(source='observations_and_compiled_geometry', sampled_at=observation.get('sampled_at'),
                    original_planned_end=list(planned_end), candidates=[])
    if current_joint_positions is None or start_joint_targets is None:
        evidence.update(accepted=False,rejection='missing_observed_arm_joints')
        raise ArmMotionPlanError('arm_retract_clearance',evidence)
    if planned_end[2] <= begin[2]+1e-9:
        evidence.update(accepted=False,rejection='retract_not_upward')
        raise ArmMotionPlanError('arm_retract_clearance',evidence)
    candidates = [('planned',planned_end), ('observed_tool_vertical',(*begin[:2],planned_end[2]))]
    for name, endpoint in candidates:
        try:
            checked = check_open_path(contract,observation,begin,endpoint,item_position,item_size,
                current_joint_positions=current_joint_positions,start_joint_targets=start_joint_targets,**kwargs)
        except ArmMotionPlanError as error:
            evidence['candidates'].append(dict(name=name,**error.evidence))
            continue
        evidence['candidates'].append(dict(name=name,**checked))
        evidence.update(checked,selected_candidate=name,selected_target=list(endpoint),accepted=True)
        return dict(target=tuple(endpoint),evidence=evidence)
    evidence.update(accepted=False,rejection='no_clear_reachable_retract')
    raise ArmMotionPlanError('arm_retract_clearance',evidence)


def plan_motion(contract, observation, source, item_size, destination, *, noise=0.,
                held_offset=None, current_tool=None, already_held=False, item_quaternion=None,
                current_tool_quaternion=None, approach_completed=False):
    """Plan all future targets together, leaving source/destination unchanged.

    Targets have a 15 mm + 6-sigma planning margin and 0.02 rad joint margin.
    Execution keeps a 15 mm + 3-sigma gate; the extra 3-sigma reserve reduces
    rejection from independent later pose samples. Gaussian noise is unbounded.
    Inward staging preserves a 10 mm + 3-sigma finger-tip clearance above
    the source. A normal pick plans >=120 mm nominal lift; the workflow's
    independent observed 80 mm lift predicate remains mandatory.
    A confirmed grasp starts its future lift at the observed tool pose. It
    does not re-enact or certify an open approach that has already completed.
    """
    from .arm_kinematics import solve_observed, forward_observed, ArmKinematicsError
    source, size, destination = _xyz(source), _xyz(item_size), _xyz(destination)
    if type(approach_completed) is not bool or type(already_held) is not bool:
        raise ValueError('boolean planning stage required')
    if approach_completed and already_held:
        raise ValueError('completed approach and already lifted stages are distinct')
    if approach_completed:
        if current_tool is None or current_tool_quaternion is None or held_offset is None:
            raise ValueError('confirmed grasp requires current observed tool pose and held offset')
        current_tool = _xyz(current_tool)
        current_tool_quaternion = tuple(current_tool_quaternion)
        if (len(current_tool_quaternion) != 4
                or any(type(v) not in (int,float) or not math.isfinite(v) for v in current_tool_quaternion)
                or abs(sum(v*v for v in current_tool_quaternion)-1) > .001):
            raise ValueError('finite unit observed tool quaternion required')
    noise = float(noise)
    if not math.isfinite(noise) or noise < 0 or any(v <= 0 for v in size):
        raise ValueError('valid dimensions and nonnegative observation noise required')
    if item_quaternion is not None:
        item_quaternion = tuple(float(v) for v in item_quaternion)
        if (len(item_quaternion) != 4 or not all(math.isfinite(v) for v in item_quaternion)
                or abs(sum(v*v for v in item_quaternion)-1) > .001):
            raise ValueError('finite unit item quaternion required')
    offset = (0., 0., -.10) if held_offset is None else _xyz(held_offset)
    margin, joint_margin = .015+6*noise, .02
    evidence = dict(source='observations_and_compiled_geometry', version='observed-arm-motion-plan-2',
        robot_id=observation.get('robot_id'), sampled_at=observation.get('sampled_at'),
        geometry_version=contract.get('version'), source_item_position=list(source),
        destination_bottom=list(destination), item_size=list(size), held_offset=list(offset),
        minimum_reach_margin_m=margin, minimum_joint_margin_rad=joint_margin,
        execution_reach_margin_m=.015+3*noise, subsequent_pose_sample_reserve_m=3*noise,
        position_noise_std_m=noise, already_held=already_held, approach_completed=approach_completed,
        planning_stage=('already_lifted' if already_held else 'confirmed_grasp' if approach_completed else 'before_approach'),
        rejected_candidates=[],
        collision_scope='Known item versus wrist capsule, palm, and fingers; no other-link/environment/peer swept-volume model or initial rest-to-staging joint observation.',
        item_yaw_model=('observed quaternion OBB 15-axis separating gaps' if item_quaternion is not None else
                        'conservative upright-box XY bounding circle; item orientation is unavailable'),
        source_item_quaternion=list(item_quaternion) if item_quaternion is not None else None)
    evidence.update(observed_body_pose=deepcopy(observation.get('pose')),
                    observed_body_quaternion=deepcopy(observation.get('quaternion')),
                    observed_upright=observation.get('upright'),
                    observed_tool_position=list(current_tool) if current_tool is not None else None,
                    observed_tool_quaternion=list(current_tool_quaternion) if current_tool_quaternion is not None else None)
    try:
        gripper = contract['gripper']
        tip = float(gripper['finger_tip_offset_m'])
        if not math.isfinite(tip) or tip <= 0:
            raise ValueError('invalid compiled finger geometry')
        if gripper['maximum_opening_m'] < .1-1e-9:
            raise ValueError('research workflow requires 0.1 m opening support')
    except (KeyError, TypeError, ValueError) as error:
        raise ArmMotionPlanError('invalid_gripper_geometry', evidence) from error
    capsule = contract['wrist_capsule']
    vertical_half = (sum(abs(_rotate(item_quaternion,axis)[2])*size[i]/2
                        for i,axis in enumerate(((1,0,0),(0,1,0),(0,0,1))))
                     if item_quaternion is not None else size[2]/2)
    settling_reserve = .015+3*noise
    if held_offset is None:
        extension = max(0.,capsule['center_m'][2]+abs(capsule['axis'][2])*capsule['half_length_m']+capsule['radius_m'])
        offset = (0.,0.,-(vertical_half+extension+settling_reserve))
        evidence['held_offset'] = list(offset)
    grasp = tuple(current_tool) if approach_completed else tuple(source[i]-offset[i] for i in range(3))
    lower = (destination[0]-offset[0], destination[1]-offset[1], destination[2]+size[2]/2-offset[2])
    approach_z = max(grasp[2], source[2]+size[2]/2+tip+.010+3*noise)
    retract_z = max(lower[2], destination[2]+size[2]+tip+.010+3*noise)
    shift_options = (0., .02, .04, .06, .08, .10, .12, .16)
    cache = {}

    def solve(name, target):
        key = tuple(target)
        if key not in cache:
            try:
                cache[key] = solve_observed(contract, observation, target,
                    margin_m=margin, joint_margin_rad=joint_margin)
            except ArmKinematicsError as error:
                if len(evidence['rejected_candidates']) < 40:
                    evidence['rejected_candidates'].append(dict(waypoint=name, target=list(target), code=error.code))
                raise
        return cache[key]

    def segment(name, begin, end, *, clear_item=None, minimum_tool_z=None, clear_quaternion=None,
                require_clearance=True):
        qa, qb = solve(name+'_start', begin)['joint_targets'], solve(name+'_end', end)['joint_targets']
        count = max(10, math.ceil(max(abs(a-b) for a, b in zip(qa, qb))/.04))
        minimum_gap, reach = math.inf, math.inf
        for index in range(count+1):
            q = [a+(b-a)*index/count for a, b in zip(qa, qb)]
            tool = forward_observed(contract, observation, q)
            checked = solve(name+'_sweep', tool['tool_position'])
            reach = min(reach, checked['reach_margin_m'])
            if minimum_tool_z is not None and tool['tool_position'][2] < minimum_tool_z-1e-6:
                raise ValueError('carried_item_clearance')
            if clear_item is not None:
                current_gap = _known_item_clearance(contract, tool, clear_item, size, clear_quaternion)
                minimum_gap = min(minimum_gap, current_gap)
                if current_gap < .001+3*noise-1e-9:
                    detail = _known_item_clearance(contract,tool,clear_item,size,clear_quaternion,with_details=True)
                    detail = dict(segment=name,sample_index=index,sample_count=count+1,
                        begin=list(begin),end=list(end),item_position=list(clear_item),minimum_clearance_m=.001+3*noise,
                        joint_targets=q,**detail)
                    if require_clearance:
                        evidence['last_rejected_segment'] = detail
                        raise ValueError('open_gripper_item_clearance')
                    if current_gap < evidence.get('predicted_retract_clearance_failure',{}).get('gap_m',math.inf):
                        evidence['predicted_retract_clearance_failure'] = detail
        return dict(segment=name, samples=count+1, joint_step_limit_rad=.04,
                    minimum_reach_margin_m=reach,
                    nominal_item_clearance_m=minimum_gap if clear_item is not None else None,
                    clearance_status=('required_now' if require_clearance else 'pending_actual_placed_item_and_finger_positions'))

    try:
        if held_offset is None:
            # Convert the actual compiled wrist capsule into the planned
            # world tool frame. The initial local +Z bound is refined for an
            # observed tilted base without changing the item XY or source.
            for _ in range(8):
                grasp_frame = forward_observed(contract,observation,solve('grasp_geometry',grasp)['joint_targets'])
                q = grasp_frame['tool_quaternion']
                wrist_center, wrist_axis = _rotate(q,capsule['center_m']), _rotate(q,capsule['axis'])
                extension = max(0.,-wrist_center[2]+abs(wrist_axis[2])*capsule['half_length_m']+capsule['radius_m'])
                height = vertical_half+extension+settling_reserve
                if abs(height+offset[2]) < 1e-9:
                    break
                offset = (0.,0.,-height)
                grasp = tuple(source[i]-offset[i] for i in range(3))
            else:
                raise ValueError('grasp_geometry_did_not_converge')
            lower = (destination[0],destination[1],destination[2]+size[2]/2-offset[2])
            approach_z = max(grasp[2],source[2]+vertical_half+tip+.010+3*noise)
            evidence['held_offset'] = list(offset)
            evidence['grasp_geometry'] = dict(height_above_item_center_m=-offset[2],
                observed_item_vertical_half_extent_m=vertical_half,wrist_downward_extension_m=extension,
                settling_overtravel_reserve_m=settling_reserve,wrist_geom_name=capsule['geom_name'])
        anchor = grasp if not already_held else current_tool
        anchor_solution = solve('grasp' if not already_held else 'held_anchor', anchor)
        anchor_q = (current_tool_quaternion if (already_held or approach_completed) and current_tool_quaternion is not None else
                    forward_observed(contract, observation, anchor_solution['joint_targets'])['tool_quaternion'])
        anchor_item = tuple(anchor[i]+offset[i] for i in range(3))
        wrist_gap = _wrist_item_clearance(contract,dict(tool_position=anchor,tool_quaternion=anchor_q),
                                         anchor_item,size,item_quaternion)
        if wrist_gap < .001+3*noise-1e-9:
            evidence['held_wrist_clearance_m'] = wrist_gap
            raise ValueError('held_wrist_item_clearance')
        # Necessary vertical side overlap at either end of the real finger
        # stroke. This does not claim friction, grasp success, or a general
        # tilted-object grasp solution; those require physical observations.
        finger_half_z = sum(abs(_rotate(anchor_q,axis)[2])*gripper['finger_half_size_m'][i]
                            for i,axis in enumerate(((1,0,0),(0,1,0),(0,0,1))))
        overlaps = []
        for side in (-1,1):
            for opening in (0.,.1):
                c = gripper['finger_center_offset_m']
                finger_z = anchor[2]+_rotate(anchor_q,(c[0],side*(abs(c[1])+opening),c[2]))[2]
                overlaps.append(min(finger_z+finger_half_z,anchor_item[2]+vertical_half)
                                -max(finger_z-finger_half_z,anchor_item[2]-vertical_half))
        evidence.update(held_wrist_clearance_m=wrist_gap,minimum_finger_vertical_overlap_m=min(overlaps),
                        required_finger_vertical_overlap_m=.020+3*noise)
        if min(overlaps) < .020+3*noise-1e-9:
            raise ValueError('insufficient_finger_side_overlap')
        local_offset = _rotate((anchor_q[0],-anchor_q[1],-anchor_q[2],-anchor_q[3]), offset)
        # The observed held offset is a world vector. Carrying it unchanged
        # through a different tool yaw would move the requested item center.
        # Solve the tool origin whose rotated local offset reaches the exact
        # unchanged destination center instead.
        center = (*destination[:2], destination[2]+size[2]/2)
        for _ in range(12):
            lower_solution = solve('lower', lower)
            lower_q = forward_observed(contract, observation, lower_solution['joint_targets'])['tool_quaternion']
            destination_offset = _rotate(lower_q, local_offset)
            updated = tuple(center[i]-destination_offset[i] for i in range(3))
            if math.dist(updated, lower) < 1e-8:
                lower = updated
                break
            lower = updated
        else:
            raise ValueError('placement_offset_did_not_converge')
        evidence.update(held_offset_tool_local=list(local_offset),
                        held_offset_at_destination=list(destination_offset))
        solve('lower', lower)
        solve('maximum_lower_overtravel', (*lower[:2], lower[2]-.012))
    except (ArmKinematicsError, ValueError) as error:
        evidence['rejection'] = getattr(error, 'code', str(error))
        raise ArmMotionPlanError('arm_plan_unreachable', evidence) from error
    retract_z = max(lower[2], destination[2]+size[2]+tip+.010+3*noise)
    placed_quaternion = item_quaternion
    if item_quaternion is not None:
        begin = current_tool if already_held else grasp
        start_q = (current_tool_quaternion if (already_held or approach_completed) and current_tool_quaternion is not None else
                   forward_observed(contract, observation, solve('grasp_frame', begin)['joint_targets'])['tool_quaternion'])
        end_q = forward_observed(contract, observation, solve('placement_frame', lower)['joint_targets'])['tool_quaternion']
        placed_quaternion = _multiply(end_q, _multiply((start_q[0],-start_q[1],-start_q[2],-start_q[3]), item_quaternion))
    approach = None
    approach_sweep = []
    if not already_held and not approach_completed:
        for shift in shift_options:
            try:
                candidate = _inward((*grasp[:2], approach_z), observation, shift)
                solve('approach', candidate)
                sweep = segment('approach_to_grasp', candidate, grasp, clear_item=source, clear_quaternion=item_quaternion)
                approach, approach_sweep = candidate, [sweep]
                break
            except (ArmKinematicsError, ValueError):
                continue
        if approach is None:
            evidence['rejection'] = 'no_clear_reachable_approach'
            raise ArmMotionPlanError('arm_plan_unreachable', evidence)
    for lift_shift in ((0.,) if already_held else (.02, .04, .06, .08, .10, .12, .16)):
        # Keep the original source as the lift reference even when the fresh
        # grasp sample moves slightly with noise or actual compliant settling.
        lift_z = max(grasp[2]+.12, source[2]+.12-offset[2])
        lift = tuple(current_tool) if already_held else _inward((*grasp[:2], lift_z), observation, lift_shift)
        cruise_z = max(lift[2], retract_z)
        clearance = (*lift[:2], cruise_z)
        try:
            solve('lift', lift)
            solve('clearance', clearance)
            prefix = list(approach_sweep)
            if not already_held:
                prefix.append(segment('grasp_to_lift', grasp, lift))
            prefix.append(segment('lift_to_clearance', lift, clearance, minimum_tool_z=lift[2]-.001))
        except (ArmKinematicsError, ValueError):
            continue
        for destination_shift in shift_options:
            try:
                translate = _inward((*lower[:2], cruise_z), observation, destination_shift)
                retract = _inward((*lower[:2], retract_z), observation, destination_shift)
                for name, target in (('translate', translate), ('retract', retract)):
                    solve(name, target)
                sweeps = prefix+[segment('clearance_to_translate', clearance, translate,
                    minimum_tool_z=(max(lift[2]-.02, destination[2]+size[2]/2-offset[2]+.02) if already_held else
                                    max(source[2]-size[2]/2, destination[2])+size[2]/2-offset[2]+.02)),
                    segment('translate_to_lower', translate, lower),
                    segment('released_retract', lower, retract,
                            clear_item=(*destination[:2], destination[2]+size[2]/2), clear_quaternion=placed_quaternion,
                            require_clearance=False)]
            except (ArmKinematicsError, ValueError) as error:
                if len(evidence['rejected_candidates']) < 40:
                    evidence['rejected_candidates'].append(dict(waypoint='placement_path', code=getattr(error, 'code', str(error))))
                continue
            targets = dict(grasp=grasp, approach=approach, lift=lift, clearance=clearance,
                           translate=translate, lower=lower, retract=retract)
            evidence.update(accepted=True, approach_finger_clearance_m=.010+3*noise,
                retract_clearance_status='requires_fresh_placed_item_and_actual_finger_positions',
                nominal_lift_m=None if already_held else lift[2]-grasp[2], sweeps=sweeps,
                targets={k:list(v) if v is not None else None for k,v in targets.items()},
                solutions={k:deepcopy(solve(k,v)) for k,v in targets.items() if v is not None},
                commanded_opening_m=.1,
                nominal_open_finger_gap_m=abs(gripper['finger_center_offset_m'][1])+.1-gripper['finger_half_size_m'][1]-math.hypot(*size[:2])/2,
                open_finger_uncertainty_covered=(abs(gripper['finger_center_offset_m'][1])+.1-gripper['finger_half_size_m'][1]-math.hypot(*size[:2])/2 >= .001+3*noise))
            return dict(targets=targets, evidence=evidence)
    evidence['rejection'] = 'no_reachable_lift_and_placement_path'
    raise ArmMotionPlanError('arm_plan_unreachable', evidence)
