"""Read-only checks for a new experiment from declared initial conditions.

No Session, physics step, assignment, reservation or live command is created.
Static forecasts do not certify contact, completion or worst-case energy.
"""
from copy import deepcopy
import math

from .catalog import model_by_id
from .domain import Project
from .navigation import _enters_open_rectangle, radius
from .orchestration import Orchestrator


def finite(value):
    try:
        return type(value) in (int, float) and math.isfinite(value)
    except OverflowError:
        return False


def issue(code, message, *, task_id=None, robot_id=None, suggestion=None):
    return dict(code=code, message=message, task_id=task_id, robot_id=robot_id,
                suggestion=suggestion)


def initial_observation(project, robot):
    """Explicit planning input, never presented as a measured observation."""
    floor = next(f for f in project.environment.floors if f.id == robot.floor_id)
    height = .6 if robot.model_id == 'spot' else 0. if robot.model_id == 'arm' else .3
    return dict(robot_id=robot.id, sampled_at=0.,
                pose=dict(robot.pose.model_dump(), z=floor.elevation+robot.pose.z+height),
                battery=robot.battery, fault=robot.fault, upright=1.,
                velocity=[0., 0., 0.], angular_velocity=[0., 0., 0.], sensors={})


def planning_context(project):
    """Reuse route and budget functions on an isolated, never-ticked owner."""
    owner = Orchestrator(project.model_copy(deep=True), lambda *args: None)
    owner.last_observations = {r.id: initial_observation(project, r) for r in project.robots}
    geometries = {}
    for robot in project.robots:
        if robot.model_id not in ('delivery', 'amr', 'agv', 'logistics', 'mobile_manipulator'):
            continue
        length = model_by_id(robot.model_id)['size']['x']
        for station in project.environment.elements:
            if station.kind != 'charger':
                continue
            floor = owner.planner.floors[station.floor_id]
            c, s = math.cos(station.pose.yaw), math.sin(station.pose.yaw)
            def pose(offset):
                return dict(x=station.pose.x+c*offset, y=station.pose.y+s*offset,
                            z=floor.elevation+station.pose.z+.3, yaw=station.pose.yaw)
            # Matches PhysicsWorld.docking_geometry's declared research model.
            contact = -length/2-.062
            geometries[(robot.id, station.id)] = dict(staging=pose(contact-1.), target=pose(contact))
    owner.charging.configure(geometries)
    # A new experiment has no existing queue. This is a static assumption,
    # neither a fabricated current connector observation nor a power grant.
    owner.charging.station_observations = {
        e.id: dict(sampled_at=0., fault=e.facility.fault, contacts={})
        for e in project.environment.elements if e.kind == 'charger'}
    return owner


def availability(project, robot, observations=None):
    if robot.fault != 'none':
        return '편집 초기조건에 로봇 장애가 설정되어 있습니다'
    if robot.battery < project.policy.charge_below:
        return '편집 초기 배터리가 작업 시작 기준보다 낮습니다'
    if observations is None:
        return None
    if not isinstance(observations, dict) or not finite(observations.get('now')):
        return '현재 관측 시각을 확인할 수 없습니다'
    reading = observations.get('robots', {}).get(robot.id)
    if not isinstance(reading, dict) or reading.get('robot_id') != robot.id:
        return '현재 로봇 관측이 없습니다'
    now, stamp = observations['now'], reading.get('sampled_at')
    if not finite(stamp) or not 0 <= now-stamp <= project.policy.stale_after:
        return '현재 로봇 관측이 오래되었거나 시각이 올바르지 않습니다'
    if not finite(reading.get('battery')) or not 0 <= reading['battery'] <= 100:
        return '현재 배터리 관측이 올바르지 않습니다'
    if reading.get('fault') != 'none' or reading['battery'] < project.policy.charge_below:
        return '현재 로봇의 장애·배터리 조건이 충족되지 않습니다'
    if not finite(reading.get('upright')) or reading['upright'] < .45:
        return '현재 로봇의 자세를 확인할 수 없거나 전도 상태입니다'
    pose = reading.get('pose')
    if not isinstance(pose, dict) or not all(finite(pose.get(k)) for k in ('x', 'y', 'z', 'yaw')):
        return '현재 로봇 위치 관측이 올바르지 않습니다'
    state = observations.get('robot_states', {}).get(robot.id, {})
    if state and (state.get('status') != 'idle' or state.get('operator_hold')):
        return '현재 로봇이 작업·정지·복구 상태입니다'
    return None


def support_contract(robot):
    """Declared fixed support dimensions; not evidence of item custody."""
    if robot.model_id not in ('amr', 'delivery', 'agv', 'logistics'):
        return None
    spec = model_by_id(robot.model_id)
    trays = [e for e in robot.equipment if e.kind == 'cargo_tray']
    if len(trays) > 1:
        return None
    if trays:
        tray = trays[0]
        return dict(size=[tray.size.x, tray.size.y], top=.2+tray.size.z,
                    capacity=min(spec['max_payload'], tray.capacity))
    return dict(size=[spec['size']['x'], spec['size']['y']], top=.1,
                capacity=min(spec['max_payload'], 3.))


def initial_footprints_overlap(a, b):
    """SAT for declared oriented body/equipment footprints, not arm sweeps."""
    if a.floor_id != b.floor_id:
        return False
    def shape(robot):
        size = model_by_id(robot.model_id)['size']
        half = [max([size[axis]]+[getattr(e.size,axis) for e in robot.equipment])/2 for axis in ('x','y')]
        c, s = math.cos(robot.pose.yaw), math.sin(robot.pose.yaw)
        return half, [(c,s),(-s,c)]
    ha, aa = shape(a); hb, ab = shape(b)
    delta = (b.pose.x-a.pose.x,b.pose.y-a.pose.y)
    for axis in aa+ab:
        gap = abs(sum(x*y for x,y in zip(delta,axis)))
        ra = sum(h*abs(sum(x*y for x,y in zip(u,axis))) for h,u in zip(ha,aa))
        rb = sum(h*abs(sum(x*y for x,y in zip(u,axis))) for h,u in zip(hb,ab))
        if gap >= ra+rb:
            return False
    return True


def fixed_base_blocked(project, robot):
    """Fixed manipulators need base clearance, not an empty entire arm reach.

Reachable worktables are intentional. The arm controller still plans its joint
trajectory and the physics model retains all table and robot contacts.
"""
    floor=next(f for f in project.environment.floors if f.id==robot.floor_id)
    size=model_by_id(robot.model_id)['size']
    c,s=math.cos(robot.pose.yaw),math.sin(robot.pose.yaw)
    ex=(abs(c)*size['x']+abs(s)*size['y'])/2
    ey=(abs(s)*size['x']+abs(c)*size['y'])/2
    if not ex<robot.pose.x<floor.width-ex or not ey<robot.pose.y<floor.depth-ey:return True
    # Use the same SAT, with explicit element dimensions instead of a model.
    ha=[size['x']/2,size['y']/2];aa=[(c,s),(-s,c)]
    for e in project.environment.elements:
        if e.floor_id!=robot.floor_id or e.kind not in ('wall','column','shelf','workbench','conveyor','obstacle','restricted','stairs','elevator','charger','dock'):continue
        if e.kind=='restricted' and robot.group in e.allowed_groups:continue
        ec,es=math.cos(e.pose.yaw),math.sin(e.pose.yaw)
        ab=[(ec,es),(-es,ec)];hb=[e.size.x/2,e.size.y/2]
        delta=(e.pose.x-robot.pose.x,e.pose.y-robot.pose.y)
        overlap=True
        for axis in aa+ab:
            gap=abs(sum(x*y for x,y in zip(delta,axis)))
            extent=sum(h*abs(sum(x*y for x,y in zip(u,axis))) for h,u in zip(ha,aa))+sum(h*abs(sum(x*y for x,y in zip(u,axis))) for h,u in zip(hb,ab))
            if gap>=extent-1e-9:overlap=False;break
        if overlap:return True
    return False


def _local_xy(pose, target):
    dx, dy = target.x-pose.x, target.y-pose.y
    c, s = math.cos(pose.yaw), math.sin(pose.yaw)
    return c*dx+s*dy, -s*dx+c*dy


def validate_task(project, task, robot, *, observations=None, owner=None,
                  start=None, battery=None):
    """Check executable capabilities plus real static routes and budget."""
    owner = owner or planning_context(project)
    blockers, resources = [], []
    def block(code, message, suggestion=None):
        blockers.append(issue(code, message, task_id=task.id, robot_id=robot.id, suggestion=suggestion))
    reason = availability(project, robot, observations)
    if reason:
        block('robot_unavailable', reason, '정상·충전된 로봇으로 바꾸거나 초기조건을 수정하세요')
    spec = model_by_id(robot.model_id)
    if task.kind == 'inspect':
        block('executor_unverified', '점검 능력 표시는 있지만 점검 결과 판정 실행기는 아직 지원하지 않습니다', '이동·대기 순찰 작업으로 목적을 명시하거나 점검 실행기를 연결하세요')
    if not task.cooperation and task.kind not in spec['capabilities']:
        block('capability_missing', '이 로봇에 구현된 작업 능력이 없습니다')
    if not task.cooperation and task.kind in ('delivery', 'transport', 'handoff', 'load', 'unload', 'retrieve'):
        block('cooperation_required', '물품 작업에는 실제 적재·운반·인수 역할과 협업 설정이 필요합니다', '기존 협업 작업을 선택하거나 물품·참여 로봇·인계점을 지정하세요')
    if task.kind not in ('patrol', 'inspect', 'delivery', 'transport', 'handoff', 'load', 'unload', 'retrieve'):
        block('unsupported_plan_kind', '이 계획 경로에서 지원하지 않는 작업 종류입니다')
    obs = initial_observation(project, robot)
    if start is not None:
        obs['pose'] = deepcopy(start)
    if battery is not None:
        obs['battery'] = battery
    destination = task.cooperation.carrier_destination if task.cooperation else task.destination
    if task.cooperation:
        c = task.cooperation
        by_id = {r.id: r for r in project.robots}
        item = next(i for i in project.items if i.id == task.item_id)
        carrier, receiver = by_id[c.carrier_id], by_id[c.receiver_id]
        support = support_contract(carrier)
        if support is None:
            block('support_missing', '운반 로봇의 검증 대상 단일 적재 지지면이 없습니다')
        if not c.donor_id and task.kind not in ('handoff', 'transport', 'unload'):
            block('donor_required', '이 작업은 초기 상차 로봇을 지정해야 합니다')
        roles = [carrier, receiver] + ([by_id[c.donor_id]] if c.donor_id else [])
        for participant in roles:
            reason = availability(project, participant, observations)
            if reason:
                block('participant_unavailable', participant.name+': '+reason)
            expected_floor = task.floor_id if participant.id == c.receiver_id else (c.source_floor_id or task.floor_id)
            actual_floor = owner._floor(obs['pose']['z']) if participant.id == c.carrier_id else participant.floor_id
            if actual_floor != expected_floor:
                block('cooperation_floor', participant.name+': 상차·운반 출발 층 또는 인수 작업 층이 일치하지 않습니다')
            if not participant.sensors.item_tracking:
                block('item_sensor_missing', participant.name+': 물품 관측 센서가 없습니다')
        if not carrier.sensors.lidar:
            block('range_sensor_missing', '협업 운반 접근에는 거리 센서가 필요합니다')
        arms = [receiver] + ([by_id[c.donor_id]] if c.donor_id else [])
        if any(r.model_id not in ('arm', 'mobile_manipulator') for r in arms):
            block('arm_controller_missing', '상차·인수 역할에는 실제 팔 제어기가 있는 로봇이 필요합니다')
        for arm in arms:
            demand = task.timeout*arm.estimated_drive_power_w/(arm.battery_capacity_wh*3600)*100+project.policy.charge_below
            if not finite(demand) or arm.battery < demand:
                block('participant_energy_shortfall', arm.name+': 협업 제한 시간 동안의 설정 전력·예비량을 확보하지 못했습니다')
        if support:
            capacity = min([support['capacity']] + [model_by_id(r.model_id)['max_payload'] for r in arms])
            if item.mass > capacity or carrier.payload_mass+item.mass > model_by_id(carrier.model_id)['max_payload']:
                block('payload_exceeded', f'물품 {item.mass:g}kg가 참여 지지면·팔의 적재 한도를 초과합니다')
            item_radius = math.hypot(item.size.x, item.size.y)/2
            offset = c.loading_offset if c.donor_id else _local_xy(carrier.pose, item.pose)
            if any(abs(offset[i])+item_radius > support['size'][i]/2-.01 for i in (0, 1)):
                block('support_footprint', '물품이 운반 지지면의 안전한 내부에 들어가지 않습니다')
            if not c.donor_id and abs(item.pose.z-(carrier.pose.z+.3+support['top'])) > .04:
                block('preloaded_item_required', '상차 로봇이 없으므로 물품이 실제 초기 지지면 위에 있어야 합니다')
            c_yaw = c.carrier_destination.yaw
            handoff_xy = (c.carrier_destination.x+math.cos(c_yaw)*offset[0]-math.sin(c_yaw)*offset[1],
                          c.carrier_destination.y+math.sin(c_yaw)*offset[0]+math.cos(c_yaw)*offset[1])
            if math.hypot(handoff_xy[0]-receiver.pose.x, handoff_xy[1]-receiver.pose.y) > .73:
                block('receiver_reach', '인계 물품 위치가 현재 인수 팔의 보수적인 작업 반경 밖입니다')
        if math.hypot(task.destination.x-receiver.pose.x, task.destination.y-receiver.pose.y) > .73:
            block('placement_reach', '최종 물품 위치가 현재 인수 팔의 작업 반경 밖입니다')
        if c.donor_id:
            donor = by_id[c.donor_id]
            source = task.source or item.pose
            if math.hypot(source.x-donor.pose.x, source.y-donor.pose.y) > .73:
                block('donor_reach', '출발 물품이 현재 상차 팔의 작업 반경 밖입니다')
            ca,sa=math.cos(obs['pose']['yaw']),math.sin(obs['pose']['yaw'])
            load_x=obs['pose']['x']+ca*c.loading_offset[0]-sa*c.loading_offset[1]
            load_y=obs['pose']['y']+sa*c.loading_offset[0]+ca*c.loading_offset[1]
            if math.hypot(load_x-donor.pose.x,load_y-donor.pose.y)>.73:
                block('loading_reach','물품 적재 위치가 현재 상차 팔의 작업 반경 밖입니다')
        resources += ['item:'+item.id, 'workspace:'+c.workspace_id]
    elif task.item_id:
        item = next(i for i in project.items if i.id == task.item_id)
        if item.mass+robot.payload_mass > spec['max_payload']:
            block('payload_exceeded', '물품과 기존 적재량이 로봇 허용 적재량을 초과합니다')
    trip = None
    source_floor = owner._floor(obs['pose']['z'])
    if source_floor != task.floor_id:
        movement=task.model_copy(update={'destination':destination})
        trip = owner._trip_plan(robot, obs, movement, cargo=item if task.cooperation else None)
        if trip is None:
            block('floor_route_unavailable', '현재 크기·중량·장비·층 조건에 맞는 승강기 경로가 없습니다')
        else:
            resources.append('elevator:'+trip['elevator_id'])
    route = trip['route'] if trip else owner._task_route(robot, obs, task) if source_floor == task.floor_id and not task.cooperation else owner._route(robot, obs, destination.model_dump(), task.floor_id) if source_floor == task.floor_id else None
    if route is None:
        block('route_unavailable', '실제 지도에서 몸체·장비·지정 경로·방향을 만족하는 경로가 없습니다')
    elif not owner.planner.path_clear(obs['pose'], route, source_floor, robot):
        block('route_clearance', '출발점부터 경로의 벽·경계·진행 방향 여유를 확인하지 못했습니다')
    legs=[] if route is None else [(obs['pose'],route,source_floor)]
    if trip:
        exit_pose=dict(trip['staging'],z=owner.planner.floors[task.floor_id].elevation)
        onward=owner._route(robot,{'pose':exit_pose},destination.model_dump(),task.floor_id)
        if onward is None or not owner.planner.path_clear(exit_pose,onward,task.floor_id,robot):
            block('onward_route_unavailable','승강기 하차 후 목적지의 경로 여유를 확인하지 못했습니다')
        else:
            legs.append((exit_pose,onward,task.floor_id))
    for start_pose,path,floor in legs:
        topology=project.environment.reviewed_topology or {}
        reviewed_doors={edge.get('via') for edge in topology.get('connections',[])
                        if edge.get('condition') in ('reviewed_door','reviewed_opening')}
        for element in project.environment.elements:
            if element.kind!='door' or element.floor_id!=floor:
                continue
            c,s=math.cos(element.pose.yaw),math.sin(element.pose.yaw)
            def local(p):
                dx,dy=p['x']-element.pose.x,p['y']-element.pose.y
                return c*dx+s*dy,-s*dx+c*dy
            # A floorplan edge is reserved when the route enters its reviewed
            # aperture. Inflating by the whole robot radius also reserves a
            # neighboring door that the route merely approaches, and can
            # create false sharing/dependencies between unrelated tasks.
            clearance=.15 if element.id in reviewed_doors else radius(robot)
            bounds=(-element.size.x/2-clearance,element.size.x/2+clearance,
                    -element.size.y/2-clearance,element.size.y/2+clearance)
            points=[start_pose]+path
            if any(_enters_open_rectangle(local(a),local(b),bounds) for a,b in zip(points,points[1:])):
                resources.append('door:'+element.id)
                if element.facility.fault or not element.facility.automatic:
                    block('door_unavailable','경로의 문이 장애 상태이거나 자동 개방되지 않습니다: '+element.name)
    budget = None
    if route is not None and not any(b['code'] == 'floor_route_unavailable' for b in blockers):
        budget = owner.charging.task_budget(robot, task, obs, route, trip)
        required = budget.get('required_percent')
        if not finite(required) or budget.get('energy_estimate_valid') is False:
            block('energy_unknown', '작업·충전 복귀의 정적 에너지 예측이 불가합니다: '+str(budget.get('reason', 'unknown')))
        elif obs['battery'] < required:
            block('energy_shortfall', f'계획상 배터리 {required:.2f}%가 필요하지만 초기 조건은 {obs["battery"]:.2f}%입니다', '초기 충전량·작업 길이·구성을 검토하세요')
        for candidate in budget.get('return_candidates', []):
            if candidate.get('known'):
                resources.append('charger:'+candidate['station_id'])
    return dict(valid=not blockers, blockers=blockers, route=deepcopy(route),
                route_legs=[dict(floor_id=floor,start=deepcopy(start_pose),points=deepcopy(path)) for start_pose,path,floor in legs],
                trip=deepcopy(trip), energy=deepcopy(budget), resources=sorted(set(resources)),
                basis='편집 초기조건의 정적 경로·설정 전력 예측; 실제 성공·접촉·최악 에너지 보증 아님')
