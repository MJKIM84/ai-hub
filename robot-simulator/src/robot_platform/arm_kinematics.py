"""Compiled research-arm geometry and pure, observation-frame kinematics.

Only build_contract reads MjModel. No function reads or writes MjData.
The solver supports the validated yaw / three parallel pitch hinge chain,
with the positive-elbow branch used by the existing actuator controller.
"""
from collections.abc import Mapping
import math
from numbers import Real

import numpy as np

VERSION = 'research-arm-kinematics-2'


class ArmKinematicsError(ValueError):
    def __init__(self, code, message):
        self.code = code
        super().__init__(message)


def _number(value, code):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Real):
        raise ArmKinematicsError(code, '유한한 숫자가 필요합니다')
    try:
        result = float(value)
    except (OverflowError, ValueError) as error:
        raise ArmKinematicsError(code, '유한한 숫자가 필요합니다') from error
    if not math.isfinite(result):
        raise ArmKinematicsError(code, '유한한 숫자가 필요합니다')
    return result


def _vector(value, count, code):
    if isinstance(value, Mapping):
        if count != 3 or not all(axis in value for axis in 'xyz'):
            raise ArmKinematicsError(code, '좌표 형식이 올바르지 않습니다')
        value = [value[axis] for axis in 'xyz']
    if not isinstance(value, (list, tuple, np.ndarray)):
        raise ArmKinematicsError(code, f'{count}개 좌표가 필요합니다')
    if (isinstance(value, np.ndarray) and value.ndim != 1) or len(value) != count:
        raise ArmKinematicsError(code, f'{count}개 좌표가 필요합니다')
    return np.array([_number(component, code) for component in value])


def _quaternion(value, code):
    q = _vector(value, 4, code)
    norm = float(np.linalg.norm(q))
    if not math.isfinite(norm) or abs(norm-1.) > 1e-6:
        raise ArmKinematicsError(code, '단위 quaternion(w,x,y,z)이 필요합니다')
    return q/norm


def _rotation(q):
    w, x, y, z = q
    return np.array([[1-2*(y*y+z*z), 2*(x*y-z*w), 2*(x*z+y*w)],
                     [2*(x*y+z*w), 1-2*(x*x+z*z), 2*(y*z-x*w)],
                     [2*(x*z-y*w), 2*(y*z+x*w), 1-2*(x*x+y*y)]])


def _multiply(a, b):
    w, x, y, z = a
    v, i, j, k = b
    return np.array([w*v-x*i-y*j-z*k, w*i+x*v+y*k-z*j,
                     w*j-x*k+y*v+z*i, w*k+x*j-y*i+z*v])


def _yaw_quaternion(yaw):
    return np.array([math.cos(yaw/2), 0., 0., math.sin(yaw/2)])


def _pitch_quaternion(pitch):
    return np.array([math.cos(pitch/2), 0., math.sin(pitch/2), 0.])


def _limits(value, code):
    if not isinstance(value, (list, tuple)) or len(value) != 4:
        raise ArmKinematicsError(code, '네 관절의 제한값이 필요합니다')
    bounds = np.array([_vector(row, 2, code) for row in value])
    if np.any(bounds[:, 0] >= bounds[:, 1]):
        raise ArmKinematicsError(code, '관절 하한은 상한보다 작아야 합니다')
    return bounds


def _gripper_contract(palm, finger, center, maximum):
    closed_min = np.minimum(-palm, [center[0]-finger[0], -center[1]-finger[1], center[2]-finger[2]])
    closed_max = np.maximum(palm, [center[0]+finger[0], center[1]+finger[1], center[2]+finger[2]])
    opened_min, opened_max = closed_min.copy(), closed_max.copy()
    opened_min[1] = min(-palm[1], -center[1]-maximum-finger[1])
    opened_max[1] = max(palm[1], center[1]+maximum+finger[1])
    return dict(palm_half_size_m=palm.tolist(), finger_half_size_m=finger.tolist(),
        finger_center_offset_m=center.tolist(), finger_tip_offset_m=float(center[2]+finger[2]),
        open_inner_half_gap_m=float(center[1]+maximum-finger[1]), maximum_opening_m=float(maximum),
        local_bounds_closed_m=[closed_min.tolist(), closed_max.tolist()],
        local_bounds_open_m=[opened_min.tolist(), opened_max.tolist()])


def _wrist_capsule(value, robot_id):
    code = 'invalid_contract'
    keys = {'geom_name', 'center_m', 'axis', 'half_length_m', 'radius_m'}
    if not isinstance(value, Mapping) or set(value) != keys or value['geom_name'] != robot_id+'/arm-link-3':
        raise ArmKinematicsError(code, '지정 로봇 손목 링크의 capsule 충돌 형상이 필요합니다')
    center = _vector(value['center_m'], 3, code)
    axis = _vector(value['axis'], 3, code)
    half = _number(value['half_length_m'], code)
    radius = _number(value['radius_m'], code)
    if abs(float(np.linalg.norm(axis))-1.) > 1e-6 or half <= 0 or radius <= 0:
        raise ArmKinematicsError(code, '손목 capsule의 단위 축과 양의 치수가 필요합니다')
    return dict(geom_name=value['geom_name'], center_m=center.tolist(), axis=axis.tolist(),
                half_length_m=half, radius_m=radius)


def _validate(contract):
    code = 'invalid_contract'
    required = {'version', 'robot_id', 'body_to_arm_base', 'lengths', 'joint_names', 'actuator_names',
                'joint_limits_rad', 'actuator_limits_rad', 'gripper', 'wrist_capsule'}
    if not isinstance(contract, Mapping) or set(contract) != required or contract['version'] != VERSION:
        raise ArmKinematicsError(code, '지원하는 기구학 계약과 버전이 필요합니다')
    if not isinstance(contract['robot_id'], str) or not contract['robot_id'].strip():
        raise ArmKinematicsError(code, '로봇 식별자가 필요합니다')
    _wrist_capsule(contract['wrist_capsule'], contract['robot_id'])
    mount, lengths = contract['body_to_arm_base'], contract['lengths']
    if not isinstance(mount, Mapping) or set(mount) != {'position', 'quaternion'}:
        raise ArmKinematicsError(code, '몸체에서 팔 기반으로의 정적 변환이 필요합니다')
    offset, quaternion = _vector(mount['position'], 3, code), _quaternion(mount['quaternion'], code)
    if not isinstance(lengths, Mapping) or set(lengths) != {'shoulder', 'upper', 'forearm', 'tool'}:
        raise ArmKinematicsError(code, '팔 링크 치수 계약이 필요합니다')
    dimensions = {name: _number(value, code) for name, value in lengths.items()}
    if min(dimensions.values()) <= 0 or not math.isfinite(sum(dimensions.values())):
        raise ArmKinematicsError(code, '양의 유한한 링크 길이가 필요합니다')
    for key in ('joint_names', 'actuator_names'):
        names = contract[key]
        stem = 'arm-' if key == 'joint_names' else 'arm-motor-'
        if (not isinstance(names, (list, tuple)) or len(names) != 4
                or list(names) != [f"{contract['robot_id']}/{stem}{i}" for i in range(4)]):
            raise ArmKinematicsError(code, '지정 로봇의 순서가 정해진 네 관절·구동기 이름이 필요합니다')
    joints, actuators = _limits(contract['joint_limits_rad'], code), _limits(contract['actuator_limits_rad'], code)
    bounds = np.column_stack((np.maximum(joints[:, 0], actuators[:, 0]), np.minimum(joints[:, 1], actuators[:, 1])))
    if np.any(bounds[:, 0] >= bounds[:, 1]):
        raise ArmKinematicsError(code, '관절·구동기의 공통 허용 범위가 없습니다')
    gripper = contract['gripper']
    gripper_keys = {'palm_half_size_m', 'finger_half_size_m', 'finger_center_offset_m', 'finger_tip_offset_m',
                    'open_inner_half_gap_m', 'maximum_opening_m', 'local_bounds_closed_m', 'local_bounds_open_m'}
    if not isinstance(gripper, Mapping) or set(gripper) != gripper_keys:
        raise ArmKinematicsError(code, '검증된 그리퍼 형상이 필요합니다')
    palm = _vector(gripper['palm_half_size_m'], 3, code)
    finger = _vector(gripper['finger_half_size_m'], 3, code)
    center = _vector(gripper['finger_center_offset_m'], 3, code)
    maximum = _number(gripper['maximum_opening_m'], code)
    if min(*palm, *finger, maximum, center[1]) <= 0 or abs(center[0]) > 1e-10 or center[2] < 0:
        raise ArmKinematicsError(code, '대칭 상자형 그리퍼 치수만 지원합니다')
    derived = _gripper_contract(palm, finger, center, maximum)
    for key in ('finger_tip_offset_m', 'open_inner_half_gap_m'):
        if abs(_number(gripper[key], code)-derived[key]) > 1e-9 or derived[key] <= 0:
            raise ArmKinematicsError(code, '그리퍼 파생 치수가 일치하지 않습니다')
    for key in ('local_bounds_closed_m', 'local_bounds_open_m'):
        value = gripper[key]
        if not isinstance(value, (list, tuple)) or len(value) != 2:
            raise ArmKinematicsError(code, '그리퍼 경계 형식이 잘못됐습니다')
        bounds_value = np.array([_vector(row, 3, code) for row in value])
        if not np.allclose(bounds_value, derived[key], atol=1e-9, rtol=0):
            raise ArmKinematicsError(code, '그리퍼 경계가 치수와 일치하지 않습니다')
    return dimensions, bounds, offset, quaternion


def validate_contract(contract):
    """Validate and return a detached, JSON-compatible normalized contract.

    This checks internal consistency, not provenance: callers must obtain the
    original contract from their compiled model, never from an untrusted peer.
    """
    lengths, _, offset, quaternion = _validate(contract)
    gripper = contract['gripper']
    return dict(version=VERSION, robot_id=contract['robot_id'],
        body_to_arm_base=dict(position=offset.tolist(), quaternion=quaternion.tolist()),
        lengths=lengths, joint_names=list(contract['joint_names']), actuator_names=list(contract['actuator_names']),
        joint_limits_rad=_limits(contract['joint_limits_rad'], 'invalid_contract').tolist(),
        actuator_limits_rad=_limits(contract['actuator_limits_rad'], 'invalid_contract').tolist(),
        wrist_capsule=_wrist_capsule(contract['wrist_capsule'], contract['robot_id']),
        gripper=_gripper_contract(_vector(gripper['palm_half_size_m'], 3, 'invalid_contract'),
            _vector(gripper['finger_half_size_m'], 3, 'invalid_contract'),
            _vector(gripper['finger_center_offset_m'], 3, 'invalid_contract'),
            _number(gripper['maximum_opening_m'], 'invalid_contract')))


def build_contract(model, robot_id):
    """Extract the supported chain from compiled MJCF, without MjData."""
    import mujoco
    code = 'unsupported_chain'
    def require(condition, message):
        if not condition:
            raise ArmKinematicsError(code, message)
    def equal(value, expected):
        return bool(np.allclose(value, expected, rtol=0, atol=1e-9))
    def unrotated(body):
        return equal(_rotation(model.body_quat[body]), np.eye(3))
    require(isinstance(robot_id, str) and bool(robot_id.strip()), '로봇 식별자가 필요합니다')
    try:
        root = model.body(robot_id+'/body').id
        base = model.body(robot_id+'/arm-base').id
        links = [model.body(f'{robot_id}/link-{i}').id for i in range(4)]
        gripper = model.body(robot_id+'/gripper').id
        joint_names = [f'{robot_id}/arm-{i}' for i in range(4)]
        actuator_names = [f'{robot_id}/arm-motor-{i}' for i in range(4)]
        joints = [model.joint(name).id for name in joint_names]
        actuators = [model.actuator(name).id for name in actuator_names]
        # The mount may contain additional fixed bodies; moving mounts are
        # not reducible to this static contract and must not be guessed.
        path, current = [], base
        while current != root and current != 0:
            require(model.body_jntnum[current] == 0, '팔 장착 경로는 정적이어야 합니다')
            path.append(current)
            current = int(model.body_parentid[current])
        require(current == root, '팔 기반이 지정 로봇 몸체의 자손이 아닙니다')
        offset, mount_q = np.zeros(3), np.array([1., 0., 0., 0.])
        for body in reversed(path):
            offset += _rotation(mount_q) @ model.body_pos[body]
            mount_q = _multiply(mount_q, model.body_quat[body])
        parents = [base, *links[:-1]]
        for i, (body, parent, joint, actuator) in enumerate(zip(links, parents, joints, actuators)):
            require(model.body_parentid[body] == parent and unrotated(body), '직렬 링크의 부모·회전 형식이 지원되지 않습니다')
            require(model.body_jntnum[body] == 1 and model.body_jntadr[body] == joint,
                    '링크마다 지정 hinge 하나가 필요합니다')
            require(model.jnt_type[joint] == mujoco.mjtJoint.mjJNT_HINGE
                    and equal(model.jnt_axis[joint], [0, 0, 1] if i == 0 else [0, 1, 0])
                    and equal(model.jnt_pos[joint], [0, 0, 0]), '관절 축·유형·기준점이 지원되지 않습니다')
            require(model.qpos0[model.jnt_qposadr[joint]] == 0, '0이 아닌 hinge 기준각은 지원하지 않습니다')
            require(bool(model.jnt_limited[joint]) and bool(model.actuator_ctrllimited[actuator]), '명시적 관절·구동기 제한이 필요합니다')
            require(model.actuator_trntype[actuator] == mujoco.mjtTrn.mjTRN_JOINT
                    and model.actuator_trnid[actuator, 0] == joint
                    and equal(model.actuator_gear[actuator], [1, 0, 0, 0, 0, 0]), '관절 위치 구동의 직접 전달만 지원합니다')
            gain, bias = model.actuator_gainprm[actuator], model.actuator_biasprm[actuator]
            require(model.actuator_dyntype[actuator] == mujoco.mjtDyn.mjDYN_NONE
                    and model.actuator_gaintype[actuator] == mujoco.mjtGain.mjGAIN_FIXED
                    and model.actuator_biastype[actuator] == mujoco.mjtBias.mjBIAS_AFFINE
                    and gain[0] > 0 and math.isfinite(gain[0]) and bias[0] == 0
                    and bias[1] == -gain[0], '직접 관절 위치 servo가 필요합니다')
        require(equal(model.body_pos[links[0]], [0, 0, 0]), '첫 yaw 관절의 추가 위치 이동은 지원하지 않습니다')
        require(model.body_parentid[gripper] == links[-1] and model.body_jntnum[gripper] == 0 and unrotated(gripper),
                '그리퍼는 마지막 링크의 정적 자손이어야 합니다')
        dimensions = {}
        for name, body in zip(('shoulder', 'upper', 'forearm', 'tool'), [*links[1:], gripper]):
            position = model.body_pos[body]
            require(equal(position[:2], [0, 0]) and position[2] > 0, '링크는 양의 Z축 방향 길이여야 합니다')
            dimensions[name] = float(position[2])
        palm = model.geom(robot_id+'/palm').id
        require(model.geom_bodyid[palm] == gripper and model.geom_type[palm] == mujoco.mjtGeom.mjGEOM_BOX
                and equal(model.geom_pos[palm], [0, 0, 0]) and equal(_rotation(model.geom_quat[palm]), np.eye(3)),
                '중앙에 정렬된 상자형 palm이 필요합니다')
        require(model.body_geomnum[gripper] == 1, '추가 gripper 형상은 이 계약에서 지원하지 않습니다')
        wrist = model.geom(robot_id+'/arm-link-3').id
        require(model.geom_bodyid[wrist] == links[-1] and model.body_geomnum[links[-1]] == 1
                and model.geom_type[wrist] == mujoco.mjtGeom.mjGEOM_CAPSULE,
                '마지막 링크는 지정한 단일 capsule 충돌 형상이어야 합니다')
        wrist_capsule = dict(geom_name=robot_id+'/arm-link-3',
            center_m=(model.geom_pos[wrist]-model.body_pos[gripper]).tolist(),
            axis=(_rotation(model.geom_quat[wrist]) @ np.array([0.,0.,1.])).tolist(),
            half_length_m=float(model.geom_size[wrist, 1]), radius_m=float(model.geom_size[wrist, 0]))
        finger_specs = []
        finger_bodies = []
        for side, sign in (('left', 1), ('right', -1)):
            body = model.body(f'{robot_id}/finger-{side}').id
            joint = model.joint(f'{robot_id}/grip-{side}').id
            geom = model.geom(f'{robot_id}/finger-shape-{side}').id
            actuator = model.actuator(f'{robot_id}/grip-motor-{side}').id
            require(model.body_parentid[body] == gripper and unrotated(body)
                    and model.body_jntnum[body] == 1 and model.body_jntadr[body] == joint
                    and model.jnt_type[joint] == mujoco.mjtJoint.mjJNT_SLIDE
                    and equal(model.jnt_axis[joint], [0, sign, 0]) and equal(model.jnt_pos[joint], [0, 0, 0])
                    and model.qpos0[model.jnt_qposadr[joint]] == 0 and model.jnt_limited[joint]
                    and model.jnt_range[joint, 0] == 0 and model.jnt_range[joint, 1] > 0,
                    '좌우 대칭 Y축 slide 그리퍼만 지원합니다')
            require(model.actuator_trntype[actuator] == mujoco.mjtTrn.mjTRN_JOINT
                    and model.actuator_trnid[actuator, 0] == joint
                    and equal(model.actuator_gear[actuator], [1, 0, 0, 0, 0, 0])
                    and bool(model.actuator_ctrllimited[actuator])
                    and equal(model.actuator_ctrlrange[actuator], model.jnt_range[joint]),
                    '그리퍼의 직접 위치 구동 범위는 slide 범위와 같아야 합니다')
            gain, bias = model.actuator_gainprm[actuator], model.actuator_biasprm[actuator]
            require(model.actuator_dyntype[actuator] == mujoco.mjtDyn.mjDYN_NONE
                    and model.actuator_gaintype[actuator] == mujoco.mjtGain.mjGAIN_FIXED
                    and model.actuator_biastype[actuator] == mujoco.mjtBias.mjBIAS_AFFINE
                    and gain[0] > 0 and math.isfinite(gain[0]) and bias[0] == 0
                    and bias[1] == -gain[0], '그리퍼는 직접 위치 servo여야 합니다')
            require(model.geom_bodyid[geom] == body and model.geom_type[geom] == mujoco.mjtGeom.mjGEOM_BOX
                    and model.body_geomnum[body] == 1
                    and equal(_rotation(model.geom_quat[geom]), np.eye(3)), '정렬된 단일 상자형 finger가 필요합니다')
            finger_bodies.append(body)
            center = model.body_pos[body]+model.geom_pos[geom]
            center = center.copy(); center[1] *= sign
            finger_specs.append((model.geom_size[geom].copy(), center, float(model.jnt_range[joint, 1])))
        require(all(equal(a, b) for a, b in zip(*finger_specs)), '그리퍼 좌우 치수가 다릅니다')
        require(set(np.flatnonzero(model.body_parentid == gripper)) == set(finger_bodies)
                and not any(np.any(model.body_parentid == body) for body in finger_bodies),
                '추가 그리퍼 자손은 이 계약에서 지원하지 않습니다')
        contract = dict(version=VERSION, robot_id=robot_id,
            body_to_arm_base=dict(position=offset.tolist(), quaternion=mount_q.tolist()), lengths=dimensions,
            joint_names=joint_names, actuator_names=actuator_names,
            joint_limits_rad=model.jnt_range[joints].tolist(), actuator_limits_rad=model.actuator_ctrlrange[actuators].tolist(),
            wrist_capsule=wrist_capsule,
            gripper=_gripper_contract(model.geom_size[palm], *finger_specs[0]))
        return validate_contract(contract)
    except ArmKinematicsError:
        raise
    except (KeyError, ValueError, IndexError, TypeError, AttributeError) as error:
        raise ArmKinematicsError(code, '지원하는 연구 팔의 compiled 모델 구조가 필요합니다') from error


def solve_local(contract, target, pitch=math.pi, margin_m=0., joint_margin_rad=0.):
    lengths, bounds, _, _ = _validate(contract)
    point = _vector(target, 3, 'invalid_target')
    pitch = _number(pitch, 'invalid_target')
    margin = _number(margin_m, 'invalid_margin')
    joint_margin = _number(joint_margin_rad, 'invalid_margin')
    if margin < 0 or joint_margin < 0:
        raise ArmKinematicsError('invalid_margin', '여유값은 음수일 수 없습니다')
    yaw = math.atan2(point[1], point[0])
    x = math.hypot(point[0], point[1])-lengths['tool']*math.sin(pitch)
    z = point[2]-lengths['shoulder']-lengths['tool']*math.cos(pitch)
    upper, forearm = lengths['upper'], lengths['forearm']
    distance = math.hypot(x, z)
    reach_margin = min(upper+forearm-distance, distance-abs(upper-forearm))
    if not math.isfinite(distance) or reach_margin < 0:
        raise ArmKinematicsError('unreachable', '목표가 연구용 팔의 역기구학 작업 범위를 벗어났습니다')
    if reach_margin < margin:
        raise ArmKinematicsError('reach_margin', '목표의 기구학 도달 여유가 부족합니다')
    scale = max(upper, forearm, distance)
    denominator = 2*(upper/scale)*(forearm/scale)
    if denominator == 0:
        raise ArmKinematicsError('invalid_contract', '링크 비율이 수치 계산 범위를 벗어났습니다')
    cosine = ((x/scale)**2+(z/scale)**2-(upper/scale)**2-(forearm/scale)**2)/denominator
    elbow = math.acos(min(1., max(-1., cosine)))
    shoulder = math.atan2(x, z)-math.atan2(forearm*math.sin(elbow), upper+forearm*math.cos(elbow))
    targets = np.array([yaw, shoulder, elbow, pitch-shoulder-elbow])
    measured_joint_margin = float(np.min(np.minimum(targets-bounds[:, 0], bounds[:, 1]-targets)))
    if measured_joint_margin < 0:
        raise ArmKinematicsError('joint_limit', '목표 자세가 팔 관절 제한을 벗어났습니다')
    if measured_joint_margin < joint_margin:
        raise ArmKinematicsError('joint_margin', '목표의 관절 제한 여유가 부족합니다')
    return dict(joint_targets=targets.tolist(), reach_margin_m=reach_margin,
                joint_margin_rad=measured_joint_margin, wrist_distance_m=distance)


def joint_path_margins(contract, begin, end, *, margin_m=.015, joint_margin_rad=.02):
    """Exact joint/wrist margins for a linear joint-space segment.

    Wrist reach depends on the actual elbow angle, regardless of tool pitch.
    Its distance extrema occur at segment endpoints or an integer multiple
    of pi. Checking these also rejects a negative-to-positive elbow path
    that crosses full extension, even when both endpoints have ample margin.
    """
    lengths, bounds, _, _ = _validate(contract)
    a, b = (_vector(q,4,'invalid_target') for q in (begin,end))
    margin, joint_margin = _number(margin_m,'invalid_margin'), _number(joint_margin_rad,'invalid_margin')
    if margin < 0 or joint_margin < 0:
        raise ArmKinematicsError('invalid_margin','여유값은 음수일 수 없습니다')
    measured_joint = float(min(np.min(np.minimum(q-bounds[:,0],bounds[:,1]-q)) for q in (a,b)))
    if measured_joint < joint_margin:
        raise ArmKinematicsError('joint_margin','관절 경로의 제한 여유가 부족합니다')
    upper, forearm = lengths['upper'], lengths['forearm']
    inner, outer = abs(upper-forearm), upper+forearm
    low, high = sorted((float(a[2]),float(b[2])))
    distances = [math.sqrt(max(0.,upper*upper+forearm*forearm+2*upper*forearm*math.cos(q))) for q in (low,high)]
    if math.ceil(low/(2*math.pi)) <= math.floor(high/(2*math.pi)):
        distances.append(outer)
    if math.ceil((low-math.pi)/(2*math.pi)) <= math.floor((high-math.pi)/(2*math.pi)):
        distances.append(inner)
    measured_reach = min(outer-max(distances),min(distances)-inner)
    if measured_reach < margin:
        raise ArmKinematicsError('reach_margin','실제 관절 경로의 손목 도달 여유가 부족합니다')
    return dict(reach_margin_m=measured_reach,joint_margin_rad=measured_joint,
                minimum_wrist_distance_m=min(distances),maximum_wrist_distance_m=max(distances),
                model='exact elbow extrema over linear joint interpolation')


def _observed_frame(contract, observation):
    _, _, mount_pos, mount_q = _validate(contract)
    code = 'invalid_observation'
    if not isinstance(observation, Mapping) or observation.get('robot_id') != contract['robot_id']:
        raise ArmKinematicsError(code, '기구학 계약과 같은 로봇의 관측이 필요합니다')
    pose = observation.get('pose')
    if not isinstance(pose, Mapping):
        raise ArmKinematicsError(code, '전달된 몸체 자세가 필요합니다')
    position, yaw = _vector(pose, 3, code), _number(pose.get('yaw'), code)
    if 'quaternion' in observation:
        body_q = _quaternion(observation['quaternion'], code)
        rotation = _rotation(body_q)
        if math.hypot(rotation[0, 0], rotation[1, 0]) < 1e-8:
            raise ArmKinematicsError(code, 'yaw가 정의되지 않는 수직 기반 자세는 지원하지 않습니다')
        quaternion_yaw = math.atan2(rotation[1, 0], rotation[0, 0])
        body_q = _multiply(_yaw_quaternion(yaw-quaternion_yaw), body_q)
        source = 'observed_quaternion_tilt_pose_yaw'
    else:
        if abs(_number(observation.get('upright'), code)-1.) > 1e-9:
            raise ArmKinematicsError(code, 'quaternion이 없는 관측은 upright=1인 yaw 전용 기반만 지원합니다')
        body_q, source = _yaw_quaternion(yaw), 'explicit_upright_pose_yaw'
    base_position = position+_rotation(body_q) @ mount_pos
    base_q = _multiply(body_q, mount_q)
    return base_position, base_q, source


def solve_observed(contract, observation, world_target, pitch=math.pi, margin_m=.015, joint_margin_rad=.02):
    base_position, base_q, source = _observed_frame(contract, observation)
    point = _rotation(base_q).T @ (_vector(world_target, 3, 'invalid_target')-base_position)
    result = solve_local(contract, point, pitch, margin_m, joint_margin_rad)
    result.update(arm_base_local_target=point.tolist(), arm_base_position=base_position.tolist(), orientation_source=source)
    return result


def forward_observed(contract, observation, joint_targets):
    """Pure FK for planning; returned quaternion uses w,x,y,z order."""
    lengths, bounds, _, _ = _validate(contract)
    q = _vector(joint_targets, 4, 'invalid_target')
    if np.any(q < bounds[:, 0]) or np.any(q > bounds[:, 1]):
        raise ArmKinematicsError('joint_limit', '관절 목표가 허용 범위를 벗어났습니다')
    base_position, base_q, source = _observed_frame(contract, observation)
    yaw, shoulder, elbow, wrist = q
    pitches = (shoulder, shoulder+elbow, shoulder+elbow+wrist)
    radial = sum(lengths[name]*math.sin(angle) for name, angle in zip(('upper', 'forearm', 'tool'), pitches))
    height = lengths['shoulder']+sum(lengths[name]*math.cos(angle) for name, angle in zip(('upper', 'forearm', 'tool'), pitches))
    point = np.array([radial*math.cos(yaw), radial*math.sin(yaw), height])
    tool_q = _multiply(_multiply(base_q, _yaw_quaternion(yaw)), _pitch_quaternion(pitches[-1]))
    return dict(tool_position=(base_position+_rotation(base_q) @ point).tolist(),
                tool_quaternion=tool_q.tolist(), orientation_source=source)
