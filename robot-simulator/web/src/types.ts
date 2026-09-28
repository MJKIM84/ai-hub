export interface Pose {
  x: number;
  y: number;
  z: number;
  yaw: number;
}
export interface Size {
  x: number;
  y: number;
  z: number;
}
export interface Floor {
  id: string;
  name: string;
  elevation: number;
  width: number;
  depth: number;
}
export type ElementKind =
  | "room"
  | "corridor"
  | "wall"
  | "column"
  | "door"
  | "opening"
  | "stairs"
  | "ramp"
  | "elevator"
  | "charger"
  | "dock"
  | "loading"
  | "shelf"
  | "workbench"
  | "conveyor"
  | "waiting"
  | "obstacle"
  | "restricted"
  | "speed_zone"
  | "one_way"
  | "entrance";
export interface FacilitySettings {
  capacity: number;
  max_load: number;
  speed: number;
  door_duration: number;
  served_floors: string[];
  fault: boolean;
  automatic: boolean;
  door_motion?: 'lateral' | 'normal' | 'vertical' | null;
  charge_power_w: number;
  charge_efficiency: number;
}
export interface Element {
  id: string;
  kind: ElementKind;
  name: string;
  floor_id: string;
  pose: Pose;
  size: Size;
  material: string;
  friction: number;
  mass: number;
  slope: number;
  step_height: number;
  speed_limit: number;
  allowed_groups: string[];
  dynamic: boolean;
  facility: FacilitySettings;
}
export interface Environment {
  id: string;
  name: string;
  version: number;
  floors: Floor[];
  elements: Element[];
  reviewed_topology?: Record<string, unknown> | null;
}
export interface SensorSettings {
  position_noise: number;
  yaw_noise: number;
  observation_delay: number;
  communication_delay: number;
  dropout: number;
  rate_hz: number;
  camera: boolean;
  lidar: boolean;
  imu: boolean;
  item_tracking?: boolean;
}
export interface Equipment {
  kind: "cargo_tray" | "arm" | "gripper" | "inspection_camera";
  mass: number;
  size: Size;
  capacity: number;
}
export interface RobotInstance {
  id: string;
  name: string;
  model_id: string;
  floor_id: string;
  pose: Pose;
  group: string;
  battery: number;
  battery_capacity_wh: number;
  estimated_drive_power_w: number;
  payload_mass: number;
  /** Finite 100..2000 N/m; only arm/mobile_manipulator permit values other than the default 400. */
  gripper_kp: number;
  equipment: Equipment[];
  sensors: SensorSettings;
  max_speed: number;
  controller: string;
  fault: "none" | "motor" | "sensor" | "communication" | "battery";
  agv_route: Pose[];
}
export interface Person {
  id: string;
  name: string;
  floor_id: string;
  pose: Pose;
  path: Pose[];
  speed: number;
  reaction_time: number;
  avoidance: boolean;
  sudden_probability: number;
  mass: number;
  behavior?: PedestrianBehavior | null;
}
export interface PedestrianBehavior {
  mode: "route" | "free_roam" | "destinations";
  allowed_floor_ids: string[];
  allowed_zone_ids: string[];
  destinations: Pose[];
  speed_min_m_s: number;
  speed_max_m_s: number;
  stop_rate_per_s: number;
  stop_duration_min_s: number;
  stop_duration_max_s: number;
  destination_change_rate_per_s: number;
  crossing_rate_per_s: number;
  seed: number | null;
  start_delay_s?: number;
}
export interface PedestrianRuntime {
  actual_position?: [number, number, number];
  actual_velocity?: [number, number, number];
  actual_speed_m_s?: number;
  actual_heading_rad?: number | null;
  sampled_at?: number;
  behavior?: string;
  destination?: Pose | null;
  allowed_floor_ids?: string[];
  allowed_zone_ids?: string[];
  mode?: string;
  reason?: string | null;
  vx?: number;
  vy?: number;
}
export interface Item {
  id: string;
  name: string;
  floor_id: string;
  pose: Pose;
  size: Size;
  mass: number;
  friction: number;
  fragility_impulse: number;
}
export type TaskKind =
  | "delivery"
  | "transport"
  | "load"
  | "unload"
  | "retrieve"
  | "patrol"
  | "inspect"
  | "manipulate"
  | "handoff";
export interface CooperativeTask {
  carrier_id: string;
  receiver_id: string;
  workspace_id: string;
  /** Floor-relative carrier body origin at the post-loading receiver rendezvous. */
  carrier_destination: Pose;
  donor_id?: string | null;
  source_floor_id?: string | null;
  /** Carrier body-frame x/y metres; omitted legacy inputs default to [0, 0]. */
  loading_offset?: [number, number];
}
export interface Task {
  id: string;
  name: string;
  kind: TaskKind;
  destination: Pose;
  /** Reviewed waypoints for a same-floor patrol or inspection. */
  approved_route?: Pose[];
  floor_id: string;
  source: Pose | null;
  item_id: string | null;
  predecessor_ids: string[];
  preferred_robot: string | null;
  priority: number;
  release_time: number;
  deadline: number | null;
  quantity: number;
  interval: number;
  retries: number;
  timeout: number;
  dwell: number;
  cooperation?: CooperativeTask | null;
  condition?:{task_id:string;outcome:"completed"|"failed"}|null;
  confirmation?:{label:string;actor:"human";criterion:string;timeout_s:number}|null;
}
export interface Policy {
  pedestrian_avoidance?: Record<string, number | string> | null;
  id: string;
  name: string;
  version: number;
  assignment: "nearest" | "balanced" | "deadline";
  traffic: "priority" | "fifo";
  safety_distance: number;
  speed_limit: number;
  charge_below: number;
  charge_until: number;
  charge_target_mode?: "fixed" | "task_budget";
  stale_after: number;
  deadlock_timeout: number;
  failure: "retry" | "reassign" | "stop";
}
export interface PhysicsSettings {
  timestep: number;
  /** Dimensionless global MuJoCo contact impedance ratio. */
  impratio: number;
  control_hz: number;
  orchestration_hz: number;
  render_hz: number;
  fidelity: "detailed" | "operational";
  seed: number;
}
export interface FaultInjection {
  time: number;
  target_id: string;
  kind:
    | "motor"
    | "sensor"
    | "communication"
    | "battery"
    | "facility"
    | "recover"
    | "push";
  magnitude: number;
  duration: number;
}
export interface Project {
  schema_version: string;
  id: string;
  name: string;
  revision: number;
  environment: Environment;
  robots: RobotInstance[];
  people: Person[];
  items: Item[];
  tasks: Task[];
  policy: Policy;
  physics: PhysicsSettings;
  faults: FaultInjection[];
  auto_stop_after_seconds?: number | null;
}
export interface RobotModel {
  id: string;
  name: string;
  kind: string;
  locomotion: string;
  capabilities: string[];
  capability_status?: Record<string, string>;
  size: Size;
  mass: number;
  max_payload: number;
  max_speed: number;
  support: Record<string, string | boolean>;
  limitations: string[];
  source: string;
}
export interface Catalog {
  models: RobotModel[];
  templates: { id: string; name: string; group?: string }[];
  documentation_models?: { id: string; name: string; status: string }[];
}
export interface ChargingEnergyCandidate {
  station_id: string;
  known: boolean;
  feasible: boolean;
  reason?: string | null;
  queue_wait_seconds: number | null;
  wait_energy_j: number | null;
  approach_energy_j: number | null;
  dock_energy_j: number | null;
  required_before_contact_j: number | null;
  shortfall_j: number | null;
  reserve_j?: number;
  available_j?: number;
  queue_forecast?: {
    known: boolean;
    ahead: { robot_id: string; phase: string; seconds: number }[];
    reason?: string | null;
    basis?: string;
  };
}
export interface ChargingEnergyReport {
  version: string;
  sampled_at: number | null;
  assessed_at: number;
  status: string;
  admission_status?: "waiting_for_egress" | "waiting_for_target";
  reason?: string | null;
  trigger_percent: number | null;
  route_trigger_percent?: number | null;
  task_needed_percent?: number | null;
  selected_station_id: string | null;
  available_j?: number;
  candidates: ChargingEnergyCandidate[];
  basis?: string;
  target_plan?: ChargingTargetPlan | null;
}
export interface ChargingTargetPlan {
  version: "charging-target-plan-v1";
  mode: "fixed" | "task_budget";
  status: "ready" | "unknown" | "infeasible";
  configured_target_percent: number;
  target_percent: number | null;
  required_target_percent?: number | null;
  assessed_at: number;
  sampled_at: number | null;
  task_id: string | null;
  task_name: string | null;
  request_id: string | null;
  exit_energy_j: number | null;
  task_required_percent: number | null;
  reason: string | null;
  exit_target: Pose | null;
  station_id?: string | null;
  service_target?: ChargingServiceTarget;
}
export interface ChargingServiceTarget {
  version: "charging-service-target-v1";
  status: "ready" | "unknown" | "infeasible";
  purpose: "fixed" | "task_budget" | "reserve_only" | null;
  target_percent: number | null;
  required_reserve_percent: number | null;
  reason: string | null;
  assessed_at: number;
  sampled_at: number | null;
  station_id: string | null;
  request_id: string | null;
  next_charge_trigger_percent: number | null;
}
export interface ConsumptionMeterReport {
  version: "research-consumption-v1";
  run_id: string;
  robot_id: string;
  status: "waiting" | "ready" | "stale" | "invalid";
  reason: string | null;
  sampled_at: number | null;
  received_at: number | null;
  counters: {
    demand_j: number;
    drawn_j: number;
    unserved_j: number;
    charging_input_j: number;
    charging_stored_j: number;
  } | null;
  interval: {
    start_at: number;
    end_at: number;
    seconds: number;
    demand_w: number;
    drawn_w: number;
  } | null;
  configured_drive_power_w: number;
}
export interface MotionLimitReport {
  version: "observed-motion-limit-v1";
  sampled_at: number | null;
  assessed_at: number;
  status: "known" | "unknown";
  floor_id: string | null;
  limit_m_s: number | null;
  model_limit_m_s: number;
  robot_limit_m_s: number;
  policy_limit_m_s: number;
  zone_ids: string[];
  reason: string | null;
}
export interface RobotState {
  pedestrian_avoidance?: import("./PedestrianSafetyPanel").PedestrianAvoidanceReport;
  id: string;
  model_id: string;
  name: string;
  pose: Pose;
  observed_pose?: Pose | null;
  quaternion: number[];
  battery: number;
  charging_power_w?: number;
  charging_station_id?: string | null;
  charging_energy?: ChargingEnergyReport | null;
  charging_workflow?:
    import("./chargingWorkflow").ChargingWorkflowReport | null;
  consumption_meter?: ConsumptionMeterReport | null;
  motion_limit?: MotionLimitReport | null;
  status: string;
  task_id: string | null;
  path: Pose[];
  velocity: number[];
  observation_age: number | null;
  reason: string;
  joints: Record<string, number>;
  sensors: Record<string, unknown>;
  last_command: Record<string, unknown> | null;
  payload: unknown[];
  operator_hold?: boolean;
}
export interface TaskState {
  confirmation_requested_at?:number;
  confirmation_receipt?:{note:string;sim_time:number};
  id: string;
  name: string;
  status: string;
  robot_id: string | null;
  reason: string;
  started_at: number | null;
  completed_at: number | null;
  participant_ids?: string[];
  execution_id?: string;
  recovery?: RecoveryState;
  cooperation?: {
    execution_id?: string;
    phase?: string;
    receiver_phase?: string;
    loading_phase?: string;
    loading_committed?: boolean;
    committed?: boolean;
    resources_retained?: boolean;
  };
}
export interface RecoveryRequest {
  request_id: string;
  actor_id: string;
  destination?: Pose;
  retry: boolean;
  timeout: number;
}
export interface RecoveryState {
  recovery_id: string;
  actor_id: string;
  status: "running" | "completed" | "failed" | "cancelled";
  mode?: "held" | "pickup" | "reconcile" | null;
  phase?: string;
  reason: string;
  started_at: number;
  completed_at?: number | null;
  destination: Pose;
  retry: boolean;
  timeout: number;
  original_status?: string;
  original_reason?: string;
}
export interface RuntimeEvent {
  seq: number;
  time: number;
  kind: string;
  severity: string;
  entity_id: string | null;
  message: string;
  details: Record<string, unknown>;
}
export interface Geom {
  id: number;
  entity_id: string;
  name: string;
  type: string | number;
  size: number[];
  position: number[];
  quaternion: number[];
  rgba: number[];
  mesh_id?: number;
}
export interface MeshData {
  id: number;
  vertices: number[];
  faces: number[];
}
export interface RunState {
  items?:{id:string;name:string;position:number[];owner:string|null;custody:string;damaged:boolean;sampled_at:number}[];
  people?: Record<string, PedestrianRuntime>;
  run_id: string;
  /** Acknowledged Session wall-clock multiplier; not a locally requested value. */
  speed: number;
  render_hz?: number;
  status: "paused" | "running" | "failed" | "completed" | "timed_out";
  sim_time: number;
  wall_time: number;
  project_revision: number;
  robots: RobotState[];
  tasks: TaskState[];
  cooperation?: {
    executions: Record<
      string,
      {
        participants: Record<string, string>;
        item_id: string;
        owner: string | null;
      }
    >;
  };
  facilities: Record<string, unknown>[];
  events: RuntimeEvent[];
  metrics: Record<string, unknown>;
  geoms: Geom[];
  warnings: string[];
}
export interface SavedProject {
  id: string;
  name: string;
  revision: number;
  updated_at?: number;
  version_count?: number;
  versions?: { revision: number; name: string; floor_count: number; robot_count: number;
    map_name: string; map_version: number; saved_at?: string | null; source?: string;
    person_count?: number; task_count?: number; seed?: number; policy_name?: string;
    auto_stop_after_seconds?: number | null;
    original_revision?: number | null; source_file?: string | null }[];
}
export interface Experiment {
  id: string;
  name?: string;
  created_at?: string;
  status?: string;
  results?: Record<string, unknown>[];
  runs?: Record<string, unknown>[];
  [key: string]: unknown;
}
export interface Recording {
  run_id: string;
  project: Project;
  frames: {
    time: number;
    qpos: number[];
    qvel: number[];
    ctrl: number[];
    robots: Record<string, Pose>;
    battery: Record<string, number>;
  }[];
  events: RuntimeEvent[];
  metrics: Record<string, unknown>;
  semantics: string;
}
