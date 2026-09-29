import type { Project, Pose, Size, PedestrianBehavior, Task } from "./types";

export type EntityTransform = { id: string; pose?: Pose; size?: Size };
export const draftKey = "robot-lab.workspace-draft.v2";

/** Object key order and the server's revision counter are not draft edits. */
export function fingerprint(project: Project): string {
  const canonical = (value: unknown): unknown => {
    if (Array.isArray(value)) return value.map(canonical);
    if (value && typeof value === "object")
      return Object.fromEntries(
        Object.entries(value)
          .filter(([key, child]) => (key !== "reviewed_topology" || child !== null) &&
            (key !== "pedestrian_access" || child !== false) && (key !== "carrier_loading_pose" || child !== null))
          .sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0))
          .map(([key, child]) => [key, canonical(child)]),
      );
    return value;
  };
  const { revision: _revision, ...content } = project;
  return JSON.stringify(canonical(content));
}

type Rule = (value: unknown, path: string, errors: string[]) => void;
const scalar =
  (kind: "string" | "number" | "boolean"): Rule =>
  (value, path, errors) => {
    if (typeof value !== kind)
      errors.push(
        `${path}: ${kind === "string" ? "문자열" : kind === "number" ? "숫자" : "참/거짓 값"} 형식이어야 합니다.`,
      );
  };
const string = scalar("string"),
  number = scalar("number"),
  boolean = scalar("boolean");
const list =
  (child: Rule): Rule =>
  (value, path, errors) => {
    if (!Array.isArray(value)) {
      errors.push(`${path}: 배열이 필요합니다.`);
      return;
    }
    // forEach skips sparse slots, which would later crash a render loop.
    for (let index = 0; index < value.length; index++)
      child(value[index], `${path}[${index + 1}]`, errors);
  };
const nullable =
  (child: Rule): Rule =>
  (value, path, errors) => {
    if (value !== null) child(value, path, errors);
  };
const record =
  (shape: Record<string, Rule>, optional: Record<string, Rule> = {}): Rule =>
  (value, path, errors) => {
    if (!value || typeof value !== "object" || Array.isArray(value)) {
      errors.push(`${path}: 객체가 필요합니다.`);
      return;
    }
    const row = value as Record<string, unknown>;
    for (const key of Object.keys(row))
      if (!Object.hasOwn(shape, key) && !Object.hasOwn(optional, key))
        errors.push(
          `${path}.${key}: 이 프로젝트 형식에서 지원하지 않는 필드입니다.`,
        );
    for (const [key, rule] of Object.entries(shape))
      rule(row[key], `${path}.${key}`, errors);
    for (const [key, rule] of Object.entries(optional))
      if (row[key] !== undefined) rule(row[key], `${path}.${key}`, errors);
  };
const pose = record({ x: number, y: number, z: number, yaw: number });
const size = record({ x: number, y: number, z: number });
const identity = { id: string, name: string };
const entity = { ...identity, floor_id: string, pose };
const facility = record(
  {
    capacity: number,
    max_load: number,
    speed: number,
    door_duration: number,
    served_floors: list(string),
    fault: boolean,
    automatic: boolean,
  },
  { charge_power_w: number, charge_efficiency: number, door_motion: nullable(string) },
);
const sensors = record(
  {
    position_noise: number,
    yaw_noise: number,
    observation_delay: number,
    communication_delay: number,
    dropout: number,
    rate_hz: number,
    camera: boolean,
    lidar: boolean,
    imu: boolean,
  },
  { item_tracking: boolean },
);
const cooperation = record(
  {
    carrier_id: string,
    receiver_id: string,
    workspace_id: string,
    carrier_destination: pose,
  },
  { carrier_loading_pose: nullable(pose), donor_id: nullable(string), source_floor_id: nullable(string), loading_offset: list(number) },
);
// The opt-in records and each defaulted field may be omitted. Validate without
// inserting defaults, so legacy drafts and explicitly null settings round-trip.
const pedestrianBehavior = record(
  {},
  {
    mode: string,
    allowed_floor_ids: list(string),
    allowed_zone_ids: list(string),
    destinations: list(pose),
    speed_min_m_s: number,
    speed_max_m_s: number,
    stop_rate_per_s: number,
    stop_duration_min_s: number,
    stop_duration_max_s: number,
    destination_change_rate_per_s: number,
    crossing_rate_per_s: number,
    seed: nullable(number),
    start_delay_s: number,
  },
);
const pedestrianAvoidance = record(
  {},
  {
    desired_clearance_m: number,
    slowdown_distance_m: number,
    stop_distance_m: number,
    resume_distance_m: number,
    max_near_speed_m_s: number,
    strategy: string,
    replan_after_s: number,
    blocked_timeout_s: number,
    observation_range_m: number,
    braking_deceleration_m_s2: number,
  },
);
const reviewedTopology = record({
  nodes: list(record({ id: string, name: string, kind: string, floor_id: string })),
  containment: list(record({ container: string, member: string })),
  connections: list(record({ from_id: string, to_id: string, via: string, width_m: number, condition: string })),
  resources: list(string),
  isolated_zones: list(string),
  zone_components: list(list(string)),
  unlinked_apertures: list(record({ id: string, name: string, kind: string, floor_id: string,
    adjacent_zones: list(string), reason: string })),
  source_plan_id: string,
  source_revision: number,
}, {
  overlapping_zones: list(record({ first_id: string, second_id: string, floor_id: string,
    smaller_covered_ratio: number })),
});
const projectShape = record({
  ...identity,
  schema_version: string,
  revision: number,
  environment: record({
    ...identity,
    version: number,
    floors: list(
      record({ ...identity, elevation: number, width: number, depth: number }),
    ),
    elements: list(
      record({
        ...entity,
        kind: string,
        size,
        material: string,
        friction: number,
        mass: number,
        slope: number,
        step_height: number,
        speed_limit: number,
        allowed_groups: list(string),
        dynamic: boolean,
        facility,
      }, { pedestrian_access: boolean }),
    ),
  }, { reviewed_topology: nullable(reviewedTopology) }),
  robots: list(
    record(
      {
        ...entity,
        model_id: string,
        group: string,
        battery: number,
        payload_mass: number,
        max_speed: number,
        controller: string,
        fault: string,
        equipment: list(
          record({ kind: string, mass: number, size, capacity: number }),
        ),
        sensors,
        agv_route: list(pose),
      },
      {
        gripper_kp: number,
        battery_capacity_wh: number,
        estimated_drive_power_w: number,
      },
    ),
  ),
  people: list(
    record(
      {
        ...entity,
        path: list(pose),
        speed: number,
        reaction_time: number,
        avoidance: boolean,
        sudden_probability: number,
        mass: number,
      },
      { behavior: nullable(pedestrianBehavior) },
    ),
  ),
  items: list(
    record({
      ...entity,
      size,
      mass: number,
      friction: number,
      fragility_impulse: number,
    }),
  ),
  tasks: list(
    record(
      {
        ...identity,
        kind: string,
        destination: pose,
        floor_id: string,
        source: nullable(pose),
        item_id: nullable(string),
        predecessor_ids: list(string),
        preferred_robot: nullable(string),
        priority: number,
        release_time: number,
        deadline: nullable(number),
        quantity: number,
        interval: number,
        retries: number,
        timeout: number,
        dwell: number,
      },
      { cooperation: nullable(cooperation), approved_route: list(pose), confirmation: nullable(record({label:string,actor:string,criterion:string,timeout_s:number})), condition: nullable(record({task_id:string,outcome:string})) },
    ),
  ),
  policy: record(
    {
      ...identity,
      version: number,
      assignment: string,
      traffic: string,
      safety_distance: number,
      speed_limit: number,
      charge_below: number,
      charge_until: number,
      stale_after: number,
      deadlock_timeout: number,
      failure: string,
    },
    {
      charge_target_mode: string,
      pedestrian_avoidance: nullable(pedestrianAvoidance),
    },
  ),
  physics: record(
    {
      timestep: number,
      control_hz: number,
      orchestration_hz: number,
      render_hz: number,
      fidelity: string,
      seed: number,
    },
    { impratio: number },
  ),
  faults: list(
    record({
      time: number,
      target_id: string,
      kind: string,
      magnitude: number,
      duration: number,
    }),
  ),
}, { auto_stop_after_seconds: nullable(number) });

/** Safe shape for UI reads. Out-of-range numeric drafts remain editable. No defaults or mutations. */
export function projectStructureErrors(value: unknown): string[] {
  const errors: string[] = [];
  try {
    projectShape(value, "프로젝트", errors);
  } catch {
    return [
      "프로젝트 JSON의 객체·배열 구조를 읽을 수 없습니다. 현재 초안을 유지하세요.",
    ];
  }
  return errors;
}

/** Import/save/apply preflight; backend validation remains authoritative. */
export function validateProject(value: unknown): string[] {
  try {
    return validateProjectContent(value);
  } catch {
    return ["프로젝트의 값과 참조를 읽을 수 없습니다. 현재 초안을 유지하세요."];
  }
}

function validateProjectContent(value: unknown): string[] {
  const errors = projectStructureErrors(value);
  if (errors.length) return errors;
  const p = value as Project;
  const finite = (n: number, path: string) => {
    if (!Number.isFinite(n)) errors.push(`${path}: 유한한 숫자를 입력하세요.`);
  };
  const range = (
    n: number,
    path: string,
    min: number,
    max = Infinity,
    exclusive = false,
    integer = false,
  ) => {
    if (
      !Number.isFinite(n) ||
      (exclusive ? n <= min : n < min) ||
      n > max ||
      (integer && !Number.isInteger(n))
    )
      errors.push(
        `${path}: ${exclusive ? `${min} 초과` : `${min} 이상`}${max === Infinity ? "" : `, ${max} 이하`}${integer ? "인 정수" : "인 유한한 숫자"}를 입력하세요.`,
      );
  };
  const text = (v: string, path: string) => {
    if (!v.trim()) errors.push(`${path}: 빈 값은 사용할 수 없습니다.`);
  };
  const choice = (v: string, values: string[], path: string) => {
    if (!values.includes(v))
      errors.push(`${path}: 지원하는 항목을 선택하세요.`);
  };
  const validPose = (v: Pose, path: string) => {
    for (const key of ["x", "y", "z", "yaw"] as const)
      finite(v[key], `${path}.${key}`);
  };
  const validSize = (v: Size, path: string) => {
    for (const key of ["x", "y", "z"] as const)
      range(v[key], `${path}.${key}`, 0, Infinity, true);
  };
  const unique = (ids: string[], path: string) => {
    if (new Set(ids).size !== ids.length)
      errors.push(`${path}: 식별자가 중복되었습니다.`);
  };
  for (const [path, v] of [
    ["프로젝트 이름", p.name],
    ["프로젝트 식별자", p.id],
    ["환경 이름", p.environment.name],
    ["환경 식별자", p.environment.id],
    ["정책 이름", p.policy.name],
    ["정책 식별자", p.policy.id],
  ])
    text(v, path);
  if (p.schema_version !== "1.0")
    errors.push("프로젝트 형식 버전 1.0을 사용하세요.");
  range(p.revision, "구성 버전", 1, Infinity, false, true);
  if (p.auto_stop_after_seconds !== undefined && p.auto_stop_after_seconds !== null)
    range(p.auto_stop_after_seconds, "자동 종료 시간", 0, 3600, true);
  range(p.environment.version, "환경 버전", 1, Infinity, false, true);
  range(p.policy.version, "정책 버전", 1, Infinity, false, true);
  if (!p.environment.floors.length) errors.push("층을 하나 이상 추가하세요.");
  const floors = new Set(p.environment.floors.map((f) => f.id));
  unique([...p.environment.floors.map((f) => f.id)], "층");
  for (const f of p.environment.floors) {
    text(f.id, "층 식별자");
    text(f.name, "층 이름");
    range(f.width, `${f.name} 폭`, 0, Infinity, true);
    range(f.depth, `${f.name} 깊이`, 0, Infinity, true);
    finite(f.elevation, `${f.name} 높이`);
  }
  const entities = [
    ...p.environment.elements,
    ...p.robots,
    ...p.people,
    ...p.items,
  ];
  unique(
    entities.map((e) => e.id),
    "객체",
  );
  const allIds = new Set(entities.map((e) => e.id));
  for (const e of entities) {
    text(e.id, "객체 식별자");
    text(e.name, `${e.id} 이름`);
    if (/[\\/]/.test(e.id))
      errors.push(`${e.name}: 식별자에는 경로 구분자를 사용할 수 없습니다.`);
    if (!floors.has(e.floor_id))
      errors.push(`${e.name}: 존재하는 층을 선택하세요.`);
    validPose(e.pose, `${e.name} 위치`);
    if ("size" in e) validSize(e.size, `${e.name} 크기`);
  }
  for (const e of p.environment.elements) {
    choice(
      e.kind,
      [
        "room",
        "corridor",
        "wall",
        "column",
        "door",
        "opening",
        "stairs",
        "ramp",
        "elevator",
        "charger",
        "dock",
        "loading",
        "shelf",
        "workbench",
        "conveyor",
        "waiting",
        "obstacle",
        "restricted",
        "speed_zone",
        "one_way",
        "entrance",
      ],
      `${e.name} 종류`,
    );
    range(e.friction, `${e.name} 마찰`, 0, 5);
    range(e.mass, `${e.name} 질량`, 0, Infinity, true);
    range(e.slope, `${e.name} 경사`, -1.2, 1.2);
    range(e.step_height, `${e.name} 단 높이`, 0, Infinity, true);
    range(e.speed_limit, `${e.name} 속도`, 0, Infinity, true);
    const f = e.facility;
    range(f.capacity, `${e.name} 수용 대수`, 1, Infinity, false, true);
    range(f.max_load, `${e.name} 최대 하중`, 0, Infinity, true);
    range(f.speed, `${e.name} 시설 속도`, 0, Infinity, true);
    range(f.door_duration, `${e.name} 문 작동 시간`, 0, Infinity, true);
    if (f.charge_power_w !== undefined)
      range(f.charge_power_w, `${e.name} 충전 전력`, 0, 100000, true);
    if (f.charge_efficiency !== undefined)
      range(f.charge_efficiency, `${e.name} 충전 효율`, 0, 1, true);
    if (f.served_floors.some((id) => !floors.has(id)))
      errors.push(`${e.name}: 시설 서비스 층이 존재하지 않습니다.`);
    if (["charger", "dock"].includes(e.kind) && f.capacity !== 1)
      errors.push(
        `${e.name}: 접점 한 쌍의 수용 대수는 1대입니다. 추가 접점은 별도 시설로 배치하세요.`,
      );
  }
  for (const r of p.robots) {
    text(r.model_id, `${r.name} 모델`);
    range(r.battery, `${r.name} 배터리`, 0, 100);
    if (r.battery_capacity_wh !== undefined)
      range(r.battery_capacity_wh, `${r.name} 배터리 용량`, 0, Infinity, true);
    if (r.estimated_drive_power_w !== undefined)
      range(r.estimated_drive_power_w, `${r.name} 예상 소비 전력`, 20);
    range(r.payload_mass, `${r.name} 적재 질량`, 0);
    range(r.max_speed, `${r.name} 최대 속도`, 0, 3, true);
    choice(
      r.fault,
      ["none", "motor", "sensor", "communication", "battery"],
      `${r.name} 고장`,
    );
    if (r.gripper_kp !== undefined) {
      range(r.gripper_kp, `${r.name} 그리퍼 강성`, 100, 2000);
      if (
        r.gripper_kp !== 400 &&
        !["arm", "mobile_manipulator"].includes(r.model_id)
      )
        errors.push(
          `${r.name}: 그리퍼 강성 변경은 연구용 고정형·이동형 팔에서 지원합니다.`,
        );
    }
    for (const key of [
      "position_noise",
      "yaw_noise",
      "observation_delay",
      "communication_delay",
    ] as const)
      range(r.sensors[key], `${r.name} 센서 ${key}`, 0);
    range(r.sensors.dropout, `${r.name} 관측 누락률`, 0, 1);
    range(r.sensors.rate_hz, `${r.name} 관측 빈도`, 0, 1000, true);
    r.agv_route.forEach((v, i) => validPose(v, `${r.name} AGV 경로 ${i + 1}`));
    for (const gear of r.equipment) {
      choice(
        gear.kind,
        ["cargo_tray", "arm", "gripper", "inspection_camera"],
        `${r.name} 장비 종류`,
      );
      range(gear.mass, `${r.name} 장비 질량`, 0, Infinity, true);
      range(gear.capacity, `${r.name} 장비 용량`, 0);
      validSize(gear.size, `${r.name} 장비 크기`);
    }
  }
  for (const person of p.people) {
    range(person.speed, `${person.name} 속도`, 0, 4);
    range(person.reaction_time, `${person.name} 반응 시간`, 0);
    range(person.sudden_probability, `${person.name} 돌발 확률`, 0, 1);
    range(person.mass, `${person.name} 질량`, 0, Infinity, true);
    person.path.forEach((v, i) => validPose(v, `${person.name} 경로 ${i + 1}`));
    if (person.behavior !== undefined && person.behavior !== null) {
      const b = {
        mode: "free_roam",
        allowed_floor_ids: [] as string[],
        allowed_zone_ids: [] as string[],
        destinations: [] as Pose[],
        speed_min_m_s: 0.5,
        speed_max_m_s: 1.2,
        stop_rate_per_s: 0.08,
        stop_duration_min_s: 0.5,
        stop_duration_max_s: 2,
        destination_change_rate_per_s: 0.03,
        crossing_rate_per_s: 0.04,
        seed: null as number | null,
        start_delay_s: 0,
        ...(person.behavior as Partial<PedestrianBehavior>),
      };
      const label = `${person.name} 보행 행동`;
      choice(b.mode, ["route", "free_roam", "destinations"], `${label} 방식`);
      range(b.speed_min_m_s, `${label} 최소 속도`, 0, 4);
      range(b.speed_max_m_s, `${label} 최대 속도`, 0, 4);
      range(b.stop_rate_per_s, `${label} 정지 빈도`, 0, 10);
      range(
        b.destination_change_rate_per_s,
        `${label} 목적지 변경 빈도`,
        0,
        10,
      );
      range(b.crossing_rate_per_s, `${label} 횡단 빈도`, 0, 10);
      range(b.start_delay_s, `${label} 이동 시작 지연`, 0, 3600);
      range(b.stop_duration_min_s, `${label} 최소 정지 시간`, 0, 300, true);
      range(b.stop_duration_max_s, `${label} 최대 정지 시간`, 0, 300, true);
      if (b.speed_min_m_s > b.speed_max_m_s)
        errors.push(`${label}: 최소 속도는 최대 속도 이하여야 합니다.`);
      if (b.stop_duration_min_s > b.stop_duration_max_s)
        errors.push(
          `${label}: 최소 정지 시간은 최대 정지 시간 이하여야 합니다.`,
        );
      if (
        b.seed !== null &&
        (!Number.isFinite(b.seed) || !Number.isInteger(b.seed))
      )
        errors.push(`${label}: 시드에는 유한한 정수를 입력하세요.`);
      if (b.allowed_floor_ids.some((id) => !floors.has(id)))
        errors.push(`${label}: 이동 허용 층이 존재하지 않습니다.`);
      if (
        b.allowed_floor_ids.length &&
        !b.allowed_floor_ids.includes(person.floor_id)
      )
        errors.push(`${label}: 초기 층이 이동 허용 층에 없습니다.`);
      const zones = b.allowed_zone_ids.map((id) =>
        p.environment.elements.find((e) => e.id === id),
      );
      if (
        zones.some(
          (zone) =>
            !zone ||
            !["room", "corridor", "waiting", "entrance", "loading"].includes(
              zone.kind,
            ),
        )
      )
        errors.push(
          `${label}: 허용 구역은 실제 방·복도·대기·입구·하역 구역을 선택하세요.`,
        );
      if (
        zones.length &&
        !zones.some((zone) => zone?.floor_id === person.floor_id)
      )
        errors.push(`${label}: 현재 층에 이동 허용 구역이 없습니다.`);
      if (b.mode === "destinations" && !b.destinations.length)
        errors.push(
          `${label}: 목적지 이동에는 하나 이상의 목적지가 필요합니다.`,
        );
      b.destinations.forEach((point, i) => {
        validPose(point, `${label} 목적지 ${i + 1}`);
        if (Math.abs(point.z) > 1e-6)
          errors.push(
            `${label}: 현재 보행자는 같은 층의 평면 목적지(z=0)만 지원합니다.`,
          );
      });
    }
  }
  for (const item of p.items) {
    range(item.mass, `${item.name} 질량`, 0, Infinity, true);
    range(item.friction, `${item.name} 마찰`, 0);
    range(
      item.fragility_impulse,
      `${item.name} 손상 충격량`,
      0,
      Infinity,
      true,
    );
  }
  const robots = new Map(p.robots.map((r) => [r.id, r])),
    items = new Map(p.items.map((i) => [i.id, i])),
    tasks = new Map(p.tasks.map((t) => [t.id, t]));
  unique(
    p.tasks.map((t) => t.id),
    "작업",
  );
  for (const task of p.tasks) {
    text(task.id, "작업 식별자");
    text(task.name, `${task.id} 이름`);
    choice(
      task.kind,
      [
        "delivery",
        "transport",
        "load",
        "unload",
        "retrieve",
        "patrol",
        "inspect",
        "manipulate",
        "handoff",
      ],
      `${task.name} 종류`,
    );
    if (!floors.has(task.floor_id))
      errors.push(`${task.name}: 작업 층이 존재하지 않습니다.`);
    validPose(task.destination, `${task.name} 목적지`);
    task.approved_route?.forEach((point, index) =>
      validPose(point, `${task.name} 승인 경로 ${index + 1}`),
    );
    if (task.approved_route?.length &&
        (!['patrol', 'inspect'].includes(task.kind) || task.cooperation))
      errors.push(`${task.name}: 승인 경로는 단일 로봇 순찰·점검 작업에만 사용할 수 있습니다.`);
    if (task.source) validPose(task.source, `${task.name} 출발지`);
    if (task.item_id !== null && !items.has(task.item_id))
      errors.push(`${task.name}: 물품 식별자가 존재하지 않습니다.`);
    if (task.preferred_robot !== null && !robots.has(task.preferred_robot))
      errors.push(`${task.name}: 지정 로봇이 존재하지 않습니다.`);
    if (task.predecessor_ids.some((id) => !tasks.has(id)))
      errors.push(`${task.name}: 선행 작업이 존재하지 않습니다.`);
    range(task.priority, `${task.name} 우선순위`, 0, 100, false, true);
    range(task.release_time, `${task.name} 발생 시각`, 0);
    range(task.quantity, `${task.name} 수량`, 1, Infinity, false, true);
    range(task.interval, `${task.name} 간격`, 0);
    range(task.retries, `${task.name} 재시도`, 0, Infinity, false, true);
    range(task.timeout, `${task.name} 제한 시간`, 0, Infinity, true);
    range(task.dwell, `${task.name} 머무는 시간`, 0);
    if (task.deadline !== null) {
      range(task.deadline, `${task.name} 기한`, 0);
      if (task.deadline < task.release_time)
        errors.push(`${task.name}: 기한은 발생 시각 이후여야 합니다.`);
    }
    const c = task.cooperation;
    if (c) {
      choice(
        task.kind,
        ["handoff", "transport", "load", "unload", "delivery", "retrieve"],
        `${task.name} 협업 작업 종류`,
      );
      text(c.workspace_id, `${task.name} 논리 작업 공간 식별자`);
      if (c.carrier_loading_pose) validPose(c.carrier_loading_pose, `${task.name} 상차 접근 위치`);
      validPose(c.carrier_destination, `${task.name} 운반 로봇 목적지`);
      const roles = [
        c.carrier_id,
        c.receiver_id,
        ...(c.donor_id !== undefined && c.donor_id !== null
          ? [c.donor_id]
          : []),
      ];
      if (new Set(roles).size !== roles.length)
        errors.push(`${task.name}: 협업 역할은 서로 다른 로봇이어야 합니다.`);
      const previous = new Map<string, Task>();
      const collect = (id: string) => {
        const prior = p.tasks.find(t => t.id === id);
        if (!prior || previous.has(id)) return;
        previous.set(id, prior);
        prior.predecessor_ids.forEach(collect);
      };
      if (c.source_floor_id) task.predecessor_ids.forEach(collect);
      const sourceFloor = c.source_floor_id || task.floor_id;
      if (!floors.has(sourceFloor)) errors.push(`${task.name}: 상차 층이 존재하지 않습니다.`);
      for (const id of roles) {
        const r = robots.get(id);
        const expected = id === c.receiver_id ? task.floor_id : sourceFloor;
        const arrives = [...previous.values()].some(t => t.cooperation?.carrier_id === id && t.floor_id === expected);
        if (!r)
          errors.push(`${task.name}: 협업 로봇 ${id}가 존재하지 않습니다.`);
        else if (r.floor_id !== expected && !arrives)
          errors.push(`${task.name}: 협업 로봇과 작업은 같은 층이어야 합니다.`);
      }
      const item = task.item_id ? items.get(task.item_id) : undefined;
      if (!item) errors.push(`${task.name}: 협업 물품이 필요합니다.`);
      else if (item.floor_id !== sourceFloor && ![...previous.values()].some(t => t.item_id === item.id && t.floor_id === sourceFloor))
        errors.push(`${task.name}: 협업 물품과 작업은 같은 층이어야 합니다.`);
      if (
        task.preferred_robot !== null &&
        task.preferred_robot !== c.carrier_id
      )
        errors.push(
          `${task.name}: 지정 로봇은 협업 운반 로봇과 같아야 합니다.`,
        );
      if (c.loading_offset !== undefined) {
        if (c.loading_offset.length !== 2)
          errors.push(`${task.name}: 적재 오프셋에는 숫자 두 개가 필요합니다.`);
        c.loading_offset.forEach((n, i) =>
          finite(n, `${task.name} 적재 오프셋 ${i + 1}`),
        );
      }
    }
  }
  // Iterative graph walk also handles large imported task lists without stack recursion.
  const visited = new Set<string>(),
    active = new Set<string>();
  for (const id of tasks.keys()) {
    if (visited.has(id)) continue;
    const stack: [string, boolean][] = [[id, false]];
    while (stack.length) {
      const [current, exit] = stack.pop()!;
      if (exit) {
        active.delete(current);
        visited.add(current);
        continue;
      }
      if (active.has(current)) {
        errors.push("작업 선후행에 순환이 있습니다.");
        break;
      }
      if (visited.has(current)) continue;
      const task = tasks.get(current);
      if (!task) continue;
      active.add(current);
      stack.push([current, true]);
      for (const predecessor of task.predecessor_ids)
        stack.push([predecessor, false]);
    }
    if (active.size) {
      active.clear();
      break;
    }
  }
  const policy = p.policy;
  choice(policy.assignment, ["nearest", "balanced", "deadline"], "배정 정책");
  choice(policy.traffic, ["priority", "fifo"], "통행 정책");
  choice(policy.failure, ["retry", "reassign", "stop"], "실패 정책");
  range(policy.safety_distance, "안전 거리", 0);
  range(policy.speed_limit, "정책 속도", 0, Infinity, true);
  range(policy.charge_below, "충전 시작", 0, 100);
  range(policy.charge_until, "충전 종료", 0, 100);
  choice(
    policy.charge_target_mode ?? "fixed",
    ["fixed", "task_budget"],
    "충전 목표 방식",
  );
  range(policy.stale_after, "관측 유효 시간", 0, Infinity, true);
  range(policy.deadlock_timeout, "교착 제한 시간", 0, Infinity, true);
  if (policy.charge_until <= policy.charge_below)
    errors.push("충전 종료 기준은 시작 기준보다 높아야 합니다.");
  if (
    policy.pedestrian_avoidance !== undefined &&
    policy.pedestrian_avoidance !== null
  ) {
    const a = {
      desired_clearance_m: 0.5,
      slowdown_distance_m: 2,
      stop_distance_m: 0.65,
      resume_distance_m: 0.9,
      max_near_speed_m_s: 0.2,
      strategy: "detour",
      replan_after_s: 2,
      blocked_timeout_s: 15,
      observation_range_m: 6,
      braking_deceleration_m_s2: 0.8,
      ...policy.pedestrian_avoidance,
    };
    range(a.desired_clearance_m, "사람 목표 간격", 0, 10);
    range(a.slowdown_distance_m, "사람 감속 거리", 0, 20, true);
    range(a.stop_distance_m, "사람 정지 거리", 0, 10, true);
    range(a.resume_distance_m, "사람 재출발 거리", 0, 15, true);
    range(a.max_near_speed_m_s, "사람 근처 속도 상한", 0, 3, true);
    range(a.replan_after_s, "사람 회피 재계획 시점", 0, 300, true);
    range(a.blocked_timeout_s, "사람 통로 차단 제한 시간", 0, 3600, true);
    range(a.observation_range_m, "사람 관측 범위", 0, 30, true);
    range(a.braking_deceleration_m_s2, "사람 회피 제동 감속도", 0, 5, true);
    choice(a.strategy, ["yield", "detour"], "사람 회피 방식");
    if (!(
      a.desired_clearance_m <= a.stop_distance_m &&
      a.stop_distance_m < a.resume_distance_m &&
      a.resume_distance_m <= a.slowdown_distance_m
    ))
      errors.push(
        "사람 경계 간 거리: 유지 ≤ 정지 < 재출발 ≤ 감속 거리여야 합니다.",
      );
    if (a.replan_after_s >= a.blocked_timeout_s)
      errors.push("사람 회피 재계획 시점은 차단 종료 시간보다 빨라야 합니다.");
    if (a.observation_range_m <= a.slowdown_distance_m)
      errors.push("사람 관측 범위는 감속 거리보다 커야 합니다.");
  }
  const physics = p.physics;
  range(physics.timestep, "물리 계산 간격", 0.0005, 0.01);
  range(physics.control_hz, "제어 빈도", 0, 1000, true);
  range(physics.orchestration_hz, "관제 빈도", 0, 100, true);
  range(physics.render_hz, "화면 갱신 빈도", 0, 60, true);
  if (physics.impratio !== undefined)
    range(physics.impratio, "접촉 임피던스 비", 1, 100);
  if (!Number.isFinite(physics.seed) || !Number.isInteger(physics.seed))
    errors.push("시드에는 유한한 정수를 입력하세요.");
  choice(physics.fidelity, ["detailed", "operational"], "물리 충실도");
  if (
    Math.max(physics.control_hz, physics.orchestration_hz) >
    1 / physics.timestep + 1e-10
  )
    errors.push("제어·관제 빈도는 물리 계산보다 빠를 수 없습니다.");
  for (const [i, fault] of p.faults.entries()) {
    const label = `고장 주입 ${i + 1}`;
    if (!allIds.has(fault.target_id))
      errors.push(`${label}: 대상 객체가 존재하지 않습니다.`);
    range(fault.time, `${label} 발생 시각`, 0);
    range(fault.duration, `${label} 지속 시간`, 0, Infinity, true);
    finite(fault.magnitude, `${label} 크기`);
    choice(
      fault.kind,
      [
        "motor",
        "sensor",
        "communication",
        "battery",
        "facility",
        "recover",
        "push",
      ],
      `${label} 종류`,
    );
  }
  return errors;
}

export function transformed(
  project: Project,
  changes: EntityTransform[],
): Project {
  const next = structuredClone(project);
  const entities = new Map(
    [
      ...next.environment.elements,
      ...next.robots,
      ...next.people,
      ...next.items,
    ].map((e) => [e.id, e]),
  );
  for (const change of changes) {
    const entity = entities.get(change.id);
    if (!entity) continue;
    if (change.pose) entity.pose = { ...change.pose };
    if (change.size && "size" in entity) entity.size = { ...change.size };
  }
  return next;
}
export function duplicateEntities(
  project: Project,
  ids: string[],
  createId: (prefix: string) => string,
): { project: Project; ids: string[] } {
  const next = structuredClone(project),
    created: string[] = [];
  const occupied = new Set(
    [
      ...next.environment.elements,
      ...next.robots,
      ...next.people,
      ...next.items,
    ].map((e) => e.id),
  );
  const selected = new Set(ids);
  for (const collection of [
    next.environment.elements,
    next.robots,
    next.people,
    next.items,
  ]) {
    const originals = collection.filter((e) => selected.has(e.id));
    for (const original of originals) {
      const copy = structuredClone(original);
      const id = createId("copy");
      if (
        typeof id !== "string" ||
        !id.trim() ||
        /[\\/]/.test(id) ||
        occupied.has(id)
      )
        throw new Error(
          "복제 식별자가 비어 있거나 중복되었습니다. 원본은 변경하지 않았습니다.",
        );
      occupied.add(id);
      copy.id = id;
      copy.name += " 복사";
      copy.pose.x += 0.5;
      copy.pose.y += 0.5;
      // Routes, task roles and fault targets remain explicit; never silently retarget work.
      (collection as (typeof copy)[]).push(copy);
      created.push(copy.id);
    }
  }
  return { project: next, ids: created };
}
export function deletionReferences(project: Project, ids: string[]): string[] {
  const selected = new Set(ids),
    referenced = new Set<string>();
  for (const task of project.tasks) {
    const values = [
      task.item_id,
      task.preferred_robot,
      task.cooperation?.carrier_id,
      task.cooperation?.receiver_id,
      task.cooperation?.donor_id,
    ];
    if (values.some((id) => id && selected.has(id))) referenced.add(task.name);
  }
  for (const [i, fault] of project.faults.entries())
    if (selected.has(fault.target_id))
      referenced.add(`고장 주입 ${i + 1} (${fault.target_id})`);
  return [...referenced];
}
