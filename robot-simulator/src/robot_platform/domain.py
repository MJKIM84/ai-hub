"""Versioned experiment inputs. SI units; z-up, right-handed world coordinates."""
from __future__ import annotations

from typing import Literal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, model_validator


def identifier() -> str:
    return uuid4().hex[:12]


class Record(BaseModel):
    model_config = ConfigDict(extra="forbid", validate_assignment=True, allow_inf_nan=False)


class Pose(Record):
    x: float = 0
    y: float = 0
    z: float = 0
    yaw: float = 0


class Size(Record):
    x: float = Field(default=1, gt=0)
    y: float = Field(default=1, gt=0)
    z: float = Field(default=1, gt=0)


class Floor(Record):
    id: str = Field(default_factory=identifier)
    name: str = "1층"
    elevation: float = 0
    width: float = Field(default=20, gt=0)
    depth: float = Field(default=14, gt=0)


ElementKind = Literal["room", "corridor", "wall", "column", "door", "opening", "stairs", "ramp", "elevator", "charger", "dock", "loading", "shelf", "workbench", "conveyor", "waiting", "obstacle", "restricted", "speed_zone", "one_way", "entrance"]


class FacilitySettings(Record):
    capacity: int = Field(default=1, ge=1)
    max_load: float = Field(default=500, gt=0)
    speed: float = Field(default=0.5, gt=0)
    door_duration: float = Field(default=2, gt=0)
    served_floors: list[str] = Field(default_factory=list)
    fault: bool = False
    automatic: bool = True
    door_motion: Literal['lateral', 'normal', 'vertical'] | None = None
    charge_power_w: float = Field(default=400, gt=0, le=100000)
    charge_efficiency: float = Field(default=0.9, gt=0, le=1)


class Element(Record):
    id: str = Field(default_factory=identifier)
    kind: ElementKind
    name: str = "요소"
    floor_id: str
    pose: Pose = Field(default_factory=Pose)
    size: Size = Field(default_factory=Size)
    material: str = "concrete"
    friction: float = Field(default=0.8, ge=0, le=5)
    mass: float = Field(default=20, gt=0)
    slope: float = Field(default=0, ge=-1.2, le=1.2)
    step_height: float = Field(default=0.15, gt=0)
    speed_limit: float = Field(default=0.5, gt=0)
    allowed_groups: list[str] = Field(default_factory=list)
    pedestrian_access: bool = False
    dynamic: bool = False
    facility: FacilitySettings = Field(default_factory=FacilitySettings)

    @model_validator(mode='after')
    def connector_capacity(self):
        if self.kind in ('charger','dock') and self.facility.capacity!=1:
            raise ValueError('연구용 충전·도킹 요소 하나는 접점 한 쌍입니다. 여러 접점은 별도 요소로 배치하세요')
        return self


class Environment(Record):
    id: str = Field(default_factory=identifier)
    name: str = "새 공간"
    version: int = Field(default=1, ge=1)
    floors: list[Floor] = Field(default_factory=lambda: [Floor(id="floor-1")], min_length=1)
    elements: list[Element] = Field(default_factory=list)
    # Confirmed floorplan topology is a navigation constraint, not a visual
    # annotation. Non-floorplan environments leave it unset.
    reviewed_topology: dict | None = None

    @model_validator(mode="after")
    def valid_references(self):
        floors = {f.id for f in self.floors}
        if len(floors) != len(self.floors):
            raise ValueError("층 식별자가 중복되었습니다")
        if len({e.id for e in self.elements}) != len(self.elements):
            raise ValueError("환경 요소 식별자가 중복되었습니다")
        for e in self.elements:
            if e.floor_id not in floors:
                raise ValueError(f"존재하지 않는 층: {e.floor_id}")
            if not set(e.facility.served_floors) <= floors:
                raise ValueError("시설의 서비스 층을 확인하세요")
        return self


class SensorSettings(Record):
    position_noise: float = Field(default=0.01, ge=0)
    yaw_noise: float = Field(default=0.005, ge=0)
    observation_delay: float = Field(default=0.05, ge=0)
    communication_delay: float = Field(default=0.02, ge=0)
    dropout: float = Field(default=0, ge=0, le=1)
    rate_hz: float = Field(default=20, gt=0, le=1000)
    camera: bool = False
    lidar: bool = True
    imu: bool = True
    item_tracking: bool = True


class Equipment(Record):
    kind: Literal["cargo_tray", "arm", "gripper", "inspection_camera"]
    mass: float = Field(default=1, gt=0)
    size: Size = Field(default_factory=lambda: Size(x=0.4, y=0.3, z=0.15))
    capacity: float = Field(default=5, ge=0)


class RobotInstance(Record):
    id: str = Field(default_factory=identifier)
    name: str = "로봇"
    model_id: str
    floor_id: str = "floor-1"
    pose: Pose = Field(default_factory=Pose)
    group: str = "기본"
    battery: float = Field(default=100, ge=0, le=100)
    battery_capacity_wh: float = Field(default=400, gt=0)
    estimated_drive_power_w: float = Field(default=120, ge=20)
    payload_mass: float = Field(default=0, ge=0)
    equipment: list[Equipment] = Field(default_factory=list)
    sensors: SensorSettings = Field(default_factory=SensorSettings)
    max_speed: float = Field(default=0.5, gt=0, le=3)
    controller: str = "default"
    gripper_kp: float = Field(default=400., strict=True, ge=100., le=2000.,
        description="연구용 arm/mobile_manipulator의 그리퍼 위치 이득(N/m); 제조사 사양 아님. 새 물리 실행에 적용")
    fault: Literal["none", "motor", "sensor", "communication", "battery"] = "none"
    agv_route: list[Pose] = Field(default_factory=list)

    @model_validator(mode="after")
    def gripper_profile(self):
        if self.gripper_kp != 400. and self.model_id not in ("arm", "mobile_manipulator"):
            raise ValueError("그리퍼 이득 설정은 연구용 arm/mobile_manipulator에서만 지원합니다")
        return self


class PersonBehavior(Record):
    """Opt-in planar, map-constrained intentions; rates use simulation seconds."""
    mode: Literal['route', 'free_roam', 'destinations'] = 'free_roam'
    allowed_floor_ids: list[str] = Field(default_factory=list)
    allowed_zone_ids: list[str] = Field(default_factory=list)
    destinations: list[Pose] = Field(default_factory=list)
    speed_min_m_s: float = Field(default=.5, ge=0, le=4)
    speed_max_m_s: float = Field(default=1.2, ge=0, le=4)
    stop_rate_per_s: float = Field(default=.08, ge=0, le=10)
    stop_duration_min_s: float = Field(default=.5, gt=0, le=300)
    stop_duration_max_s: float = Field(default=2, gt=0, le=300)
    destination_change_rate_per_s: float = Field(default=.03, ge=0, le=10)
    crossing_rate_per_s: float = Field(default=.04, ge=0, le=10)
    seed: int | None = None
    start_delay_s: float = Field(default=0, ge=0, le=3600)

    @model_validator(mode='after')
    def ordered_ranges(self):
        if self.speed_min_m_s > self.speed_max_m_s:
            raise ValueError('보행 속도 최솟값은 최댓값 이하여야 합니다')
        if self.stop_duration_min_s > self.stop_duration_max_s:
            raise ValueError('정지 시간 최솟값은 최댓값 이하여야 합니다')
        if self.mode == 'destinations' and not self.destinations:
            raise ValueError('목적지 이동에는 하나 이상의 목적지가 필요합니다')
        return self


class Person(Record):
    id: str = Field(default_factory=identifier)
    name: str = "보행자"
    floor_id: str = "floor-1"
    pose: Pose = Field(default_factory=Pose)
    path: list[Pose] = Field(default_factory=list)
    speed: float = Field(default=0.8, ge=0, le=4)
    reaction_time: float = Field(default=0.5, ge=0)
    avoidance: bool = True
    sudden_probability: float = Field(default=0, ge=0, le=1)
    mass: float = Field(default=70, gt=0)
    behavior: PersonBehavior | None = None


class Item(Record):
    id: str = Field(default_factory=identifier)
    name: str = "물품"
    floor_id: str = "floor-1"
    pose: Pose = Field(default_factory=Pose)
    size: Size = Field(default_factory=lambda: Size(x=0.25, y=0.2, z=0.15))
    mass: float = Field(default=1, gt=0)
    friction: float = Field(default=0.5, ge=0)
    fragility_impulse: float = Field(default=15, gt=0)


TaskKind = Literal["delivery", "transport", "load", "unload", "retrieve", "patrol", "inspect", "manipulate", "handoff"]


class CooperativeTask(Record):
    """Explicit robot roles; schema validity does not imply executor support."""

    carrier_id: str = Field(min_length=1, pattern=r"\S")
    receiver_id: str = Field(min_length=1, pattern=r"\S")
    workspace_id: str = Field(min_length=1, pattern=r"\S", description="협업 작업 공간의 논리적 예약 식별자")
    carrier_destination: Pose = Field(description="적재 후 수신 로봇과 만나는 작업 층 기준 운반 로봇 몸체 원점 목표; 물품 목표와 구분")
    carrier_loading_pose: Pose | None = Field(default=None, description="상차 전 예약 작업 공간 안에서 정렬할 운반차 위치; 생략하면 현재 위치에서 상차")
    donor_id: str | None = Field(default=None, min_length=1, pattern=r"\S", description="선택적인 초기 상차 로봇; 생략하면 물품이 이미 실린 운반 로봇에서 시작")
    source_floor_id: str | None = Field(default=None, description="명시적인 상차 층. source 좌표는 이 층 기준이며 최종 배치는 Task.floor_id 기준")
    loading_offset: list[StrictFloat] = Field(default_factory=lambda: [0.0, 0.0], min_length=2, max_length=2,
        description="운반 로봇 몸체 좌표계의 물품 적재 목표 [x, y] 오프셋(m); 유한한 숫자 두 개",
        json_schema_extra={"default": [0.0, 0.0]})

    @model_validator(mode="after")
    def distinct_roles(self):
        if self.carrier_loading_pose is not None and self.donor_id is None:
            raise ValueError("상차 접근에는 상차 로봇이 필요합니다")
        roles = [self.carrier_id, self.receiver_id]
        if self.donor_id is not None:
            roles.append(self.donor_id)
        if len(roles) != len(set(roles)):
            raise ValueError("협업 역할의 로봇은 서로 달라야 합니다")
        return self


class TaskCondition(Record):
    task_id: str = Field(min_length=1, max_length=120)
    outcome: Literal['completed','failed']


class HumanConfirmation(Record):
    label: str = Field(min_length=1, max_length=200)
    actor: Literal['human'] = 'human'
    criterion: str = Field(min_length=1, max_length=1000)
    timeout_s: float = Field(default=120, gt=0, le=3600)


class Task(Record):
    id: str = Field(default_factory=identifier)
    name: str = "작업"
    kind: TaskKind = "patrol"
    destination: Pose = Field(default_factory=Pose, description="일반 작업 목표; 협업 작업에서는 작업 층 기준 최종 물품 바닥 중심(BOTTOM) 목표")
    approved_route: list[Pose] = Field(default_factory=list, description="사용자가 승인한 같은 층의 검증된 경유 경로")
    floor_id: str = "floor-1"
    source: Pose | None = Field(default=None, description="협업 초기 상차의 작업 층 기준 물품 바닥 중심(BOTTOM) 위치; 생략하면 item.pose 사용")
    item_id: str | None = None
    predecessor_ids: list[str] = Field(default_factory=list)
    preferred_robot: str | None = None
    priority: int = Field(default=5, ge=0, le=100)
    release_time: float = Field(default=0, ge=0)
    deadline: float | None = Field(default=None, ge=0)
    quantity: int = Field(default=1, ge=1)
    interval: float = Field(default=0, ge=0)
    retries: int = Field(default=1, ge=0)
    timeout: float = Field(default=120, gt=0)
    dwell: float = Field(default=1, ge=0)
    cooperation: CooperativeTask | None = None
    confirmation: HumanConfirmation | None = None
    condition: TaskCondition | None = None

    @model_validator(mode="after")
    def valid_cooperation(self):
        if self.condition and self.condition.task_id not in self.predecessor_ids:
            raise ValueError("분기 기준 작업은 선행 작업 목록에 있어야 합니다")
        if self.confirmation and (self.kind != "patrol" or self.cooperation or self.item_id):
            raise ValueError("사용자 확인은 이동 후 현장 확인에만 적용하며 물품 이동을 대신하지 않습니다")
        if self.approved_route and (self.kind not in ('patrol','inspect') or self.cooperation is not None):
            raise ValueError("승인 경로는 단일 로봇 순찰·점검 작업에만 사용할 수 있습니다")
        if self.cooperation is not None:
            if self.kind not in ("handoff", "transport", "load", "unload", "delivery", "retrieve"):
                raise ValueError("이 작업 종류에는 협업 설정을 사용할 수 없습니다")
            if not self.item_id or not self.item_id.strip():
                raise ValueError("협업 작업에는 물품 식별자가 필요합니다")
        return self


class PedestrianAvoidance(Record):
    """Surface clearances; delayed observations and braking add further margin."""
    desired_clearance_m: float = Field(default=.5, ge=0, le=10)
    slowdown_distance_m: float = Field(default=2, gt=0, le=20)
    stop_distance_m: float = Field(default=.65, gt=0, le=10)
    resume_distance_m: float = Field(default=.9, gt=0, le=15)
    max_near_speed_m_s: float = Field(default=.2, gt=0, le=3)
    strategy: Literal['yield', 'detour'] = 'detour'
    replan_after_s: float = Field(default=2, gt=0, le=300)
    blocked_timeout_s: float = Field(default=15, gt=0, le=3600)
    observation_range_m: float = Field(default=6, gt=0, le=30)
    braking_deceleration_m_s2: float = Field(default=.8, gt=0, le=5)

    @model_validator(mode='after')
    def ordered_distances(self):
        if not self.desired_clearance_m <= self.stop_distance_m < self.resume_distance_m <= self.slowdown_distance_m:
            raise ValueError('사람 경계 간 거리: 유지 ≤ 정지 < 재출발 ≤ 감속 거리여야 합니다')
        if self.replan_after_s >= self.blocked_timeout_s:
            raise ValueError('재계획 시점은 차단 종료 시간보다 빨라야 합니다')
        if self.observation_range_m <= self.slowdown_distance_m:
            raise ValueError('사람 관측 범위는 감속 거리보다 커야 합니다')
        return self


class Policy(Record):
    id: str = "default"
    name: str = "가까운 로봇 우선"
    version: int = Field(default=1, ge=1)
    assignment: Literal["nearest", "balanced", "deadline"] = "nearest"
    traffic: Literal["priority", "fifo"] = "priority"
    safety_distance: float = Field(default=0.25, ge=0)
    speed_limit: float = Field(default=0.6, gt=0)
    charge_below: float = Field(default=20, ge=0, le=100)
    charge_until: float = Field(default=80, ge=0, le=100)
    charge_target_mode: Literal["fixed", "task_budget"] = "fixed"
    stale_after: float = Field(default=1, gt=0)
    deadlock_timeout: float = Field(default=8, gt=0)
    failure: Literal["retry", "reassign", "stop"] = "reassign"
    pedestrian_avoidance: PedestrianAvoidance | None = None

    @model_validator(mode="after")
    def charge_range(self):
        if self.charge_until<=self.charge_below:raise ValueError("충전 종료 기준은 시작 기준보다 높아야 합니다")
        return self


class PhysicsSettings(Record):
    timestep: float = Field(default=0.002, ge=0.0005, le=0.01)
    impratio: float = Field(default=1., strict=True, ge=1., le=100.,
        description="MuJoCo 타원 마찰 원뿔의 마찰/법선 제약 임피던스 비; 모든 접촉에 적용하는 연구 설정")
    control_hz: float = Field(default=100, gt=0, le=1000)
    orchestration_hz: float = Field(default=5, gt=0, le=100)
    render_hz: float = Field(default=20, gt=0, le=60)
    fidelity: Literal["detailed", "operational"] = "detailed"
    seed: int = 42

    @model_validator(mode="after")
    def rates(self):
        if max(self.control_hz,self.orchestration_hz)>1/self.timestep+1e-10:raise ValueError("제어·관제 주기는 물리 계산보다 빠를 수 없습니다")
        return self


class FaultTrigger(Record):
    kind: Literal['task_status', 'event']
    task_id: str | None = None
    status: Literal['completed', 'failed', 'cancelled'] = 'completed'
    event_kind: Literal['cooperation_loaded', 'task_completed', 'task_failed', 'pedestrian_avoidance'] = 'cooperation_loaded'
    entity_id: str | None = None


class FaultInjection(Record):
    time: float = Field(default=0,ge=0)
    target_id: str
    kind: Literal["motor", "sensor", "communication", "battery", "facility", "recover", "push"]
    magnitude: float = 100
    duration: float = Field(default=1, gt=0)
    trigger: FaultTrigger | None = None
    max_occurrences: int = Field(default=1, ge=1, le=10)
    auto_recover: bool = False

    @model_validator(mode='after')
    def recovery_contract(self):
        if self.auto_recover and self.kind not in ('motor', 'sensor', 'communication', 'facility'):
            raise ValueError('자동 해제는 모터·센서·통신·시설 장애만 지원합니다')
        if (self.trigger is None or self.trigger.kind == 'task_status') and self.max_occurrences != 1:
            raise ValueError('시각·작업 상태 조건은 한 번만 발생합니다. 반복은 사건 조건을 사용하세요')
        return self


class Project(Record):
    schema_version: str = "1.0"
    id: str = Field(default_factory=identifier)
    name: str = "로봇 운영 실험"
    revision: int = Field(default=1, ge=1)
    environment: Environment = Field(default_factory=Environment)
    robots: list[RobotInstance] = Field(default_factory=list)
    people: list[Person] = Field(default_factory=list)
    items: list[Item] = Field(default_factory=list)
    tasks: list[Task] = Field(default_factory=list)
    policy: Policy = Field(default_factory=Policy)
    physics: PhysicsSettings = Field(default_factory=PhysicsSettings)
    faults: list[FaultInjection] = Field(default_factory=list)
    auto_stop_after_seconds: float | None = Field(default=None, gt=0, le=3600,
        description="설정한 시뮬레이션 시간이 되거나 모든 작업이 끝나면 자동 종료")

    @model_validator(mode="after")
    def validate_graph(self):
        floors = {f.id for f in self.environment.floors}
        entity_ids = [e.id for e in self.environment.elements] + [x.id for x in self.robots + self.people + self.items]
        if any(not key or "/" in key or "\\" in key for key in entity_ids):
            raise ValueError("개체 식별자는 비어 있거나 경로 구분자를 포함할 수 없습니다")
        if len(entity_ids) != len(set(entity_ids)):
            raise ValueError("개체 식별자가 중복되었습니다")
        for fault in self.faults:
            if fault.target_id not in entity_ids:
                raise ValueError('돌발 상황 대상이 존재하지 않습니다')
            robot_target=any(r.id==fault.target_id for r in self.robots)
            facility_target=any(e.id==fault.target_id and e.kind in ('door','elevator','charger','dock') for e in self.environment.elements)
            if not ((robot_target and fault.kind!='facility') or (facility_target and fault.kind in ('facility','recover'))):
                raise ValueError('대상에 적용할 수 없는 돌발 상황입니다. 로봇 장애와 시설 장애를 구분하세요')
            if fault.trigger:
                trigger = fault.trigger
                if trigger.kind == 'task_status' and not trigger.task_id:
                    raise ValueError('작업 상태 조건에는 작업이 필요합니다')
                if trigger.task_id and trigger.task_id not in {t.id for t in self.tasks}:
                    raise ValueError('돌발 상황의 조건 작업이 존재하지 않습니다')
                if trigger.entity_id and trigger.entity_id not in entity_ids:
                    raise ValueError('돌발 상황의 조건 객체가 존재하지 않습니다')
        for x in self.robots + self.people + self.items + self.tasks:
            if x.floor_id not in floors:
                raise ValueError(f"존재하지 않는 층: {x.floor_id}")
        zones = {e.id:e for e in self.environment.elements}
        for person in self.people:
            behavior = person.behavior
            if behavior is None:
                continue
            if not set(behavior.allowed_floor_ids) <= floors:
                raise ValueError('보행자의 이동 허용 층이 존재하지 않습니다')
            if behavior.allowed_floor_ids and person.floor_id not in behavior.allowed_floor_ids:
                raise ValueError('보행자의 초기 층이 이동 허용 층에 없습니다')
            if any(key not in zones or zones[key].kind not in ('room','corridor','waiting','entrance','loading')
                   for key in behavior.allowed_zone_ids):
                raise ValueError('보행자 허용 구역은 실제 방·복도·대기·입구·하역 구역을 선택하세요')
            if behavior.allowed_zone_ids and not any(zones[key].floor_id == person.floor_id for key in behavior.allowed_zone_ids):
                raise ValueError('보행자의 현재 층에 이동 허용 구역이 없습니다')
            if any(abs(point.z)>1e-6 for point in behavior.destinations):
                raise ValueError('현재 보행자 물리는 같은 층의 평면 목적지(z=0)만 지원합니다')
        tasks = {t.id: t for t in self.tasks}
        if len(tasks) != len(self.tasks):
            raise ValueError("작업 식별자가 중복되었습니다")
        items = {i.id for i in self.items}
        robots = {r.id for r in self.robots}
        item_by_id = {i.id: i for i in self.items}
        robot_by_id = {r.id: r for r in self.robots}
        visited: set[str] = set()
        active: set[str] = set()

        def visit(task_id: str):
            if task_id in active:
                raise ValueError("작업 선후행에 순환이 있습니다")
            if task_id in visited:
                return
            active.add(task_id)
            t = tasks[task_id]
            for predecessor in t.predecessor_ids:
                if predecessor not in tasks:
                    raise ValueError(f"없는 선행 작업: {predecessor}")
                visit(predecessor)
            active.remove(task_id)
            visited.add(task_id)

        # Validate the dependency graph before following prior physical outputs.
        for task_id in tasks:
            visit(task_id)

        def prior_outputs(t):
            found = {}
            def collect(key):
                if key in found:return
                found[key] = tasks[key]
                for parent in tasks[key].predecessor_ids:collect(parent)
            for key in t.predecessor_ids:collect(key)
            return list(found.values())

        for t in self.tasks:
            if t.item_id and t.item_id not in items:
                raise ValueError(f"없는 물품: {t.item_id}")
            if t.preferred_robot and t.preferred_robot not in robots:
                raise ValueError(f"없는 로봇: {t.preferred_robot}")
            if t.cooperation is not None:
                cooperation = t.cooperation
                roles = [cooperation.carrier_id, cooperation.receiver_id]
                if cooperation.donor_id is not None:
                    roles.append(cooperation.donor_id)
                if len(roles) != len(set(roles)):
                    raise ValueError("협업 역할의 로봇은 서로 달라야 합니다")
                for robot_id in roles:
                    if robot_id not in robot_by_id:
                        raise ValueError(f"없는 협업 로봇: {robot_id}")
                    source_floor = cooperation.source_floor_id or t.floor_id
                    if source_floor not in floors:
                        raise ValueError("존재하지 않는 상차 층")
                    required_floor = t.floor_id if robot_id == cooperation.receiver_id else source_floor
                    prior = prior_outputs(t) if cooperation.source_floor_id else []
                    arrived = any(p.cooperation and p.cooperation.carrier_id == robot_id and p.floor_id == required_floor for p in prior)
                    if robot_by_id[robot_id].floor_id != required_floor and not arrived:
                        raise ValueError("협업 역할 로봇과 작업은 같은 층이어야 합니다")
                if t.item_id not in item_by_id:
                    raise ValueError("협업 작업에는 존재하는 물품이 필요합니다")
                delivered = any(p.item_id == t.item_id and p.floor_id == source_floor for p in prior)
                if item_by_id[t.item_id].floor_id != source_floor and not delivered:
                    raise ValueError("협업 물품과 작업은 같은 층이어야 합니다")
                if t.preferred_robot is not None and t.preferred_robot != cooperation.carrier_id:
                    raise ValueError("협업 작업의 지정 로봇은 운반 로봇과 같아야 합니다")
            if t.deadline is not None and t.deadline < t.release_time:
                raise ValueError("기한은 발생 시각 이후여야 합니다")
            visit(t.id)
        return self
