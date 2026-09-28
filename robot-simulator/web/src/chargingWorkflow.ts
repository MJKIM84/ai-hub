import type { Pose } from "./types";

export interface ChargingWorkflowReport {
  version: "charging-workflow-v1";
  robot_id: string;
  assessed_at: number;
  current: boolean;
  report_age_seconds: number | null;
  observation: {
    status: "current" | "stale" | "unknown";
    sampled_at: number | null;
    age_seconds: number | null;
    battery_percent: number | null;
    pose: Pose | null;
    reason: string | null;
  };
  stage: string;
  stage_since: number;
  stage_since_basis: string;
  elapsed_seconds: number | null;
  reason: string | null;
  robot_status: string;
  operator_hold: boolean;
  station_id: string | null;
  request: {
    request_id: string;
    station_id: string;
    current: boolean;
    status: string;
    phase: string;
    reason: string;
    requested_at: number;
    phase_since: number;
    elapsed_seconds: number | null;
    phase_elapsed_seconds: number | null;
    target_percent: number;
    stop_pending: boolean;
    stop_delivered_at: number | null;
    cancel_requested: boolean;
    attempts: number | null;
    limits: {
      phase_timeout_seconds: number | null;
      contact_timeout_seconds: number | null;
      clearance_timeout_seconds: number | null;
      approach_budget: unknown;
    };
  } | null;
  traffic: {
    status: "available" | "blocked" | "unknown";
    reason: string | null;
    source: string;
    replan_attempts: number | null;
    last_replan_at: number | null;
    blocking_robot_ids: string[];
    need_trigger_percent: number | null;
  };
  waiting_classification: string;
  ownership: {
    connector_robot_id: string | null;
    queue_robot_ids: string[];
    occupants: string[];
    station_fault: string | null;
    station_fault_latched: boolean;
    egress_reservations: {
      robot_id: string;
      request_id: string | null;
      station_id: string | null;
      floor_id: string | null;
      target: Pose;
      clearing: boolean;
      interrupted: boolean;
    }[];
    resources: { resource: string; robot_ids: string[] }[];
    path_owner: string;
    path_waypoint_count: number;
    path_owner_basis: string;
  };
  clearance: {
    completed_at: number;
    request_id: string | null;
    battery_percent: number | null;
    pose: Pose | null;
    basis: string;
  } | null;
  task_after_clearance: {
    status: string;
    task_id: string | null;
    started_at: number | null;
    completed_at: number | null;
    reason?: string;
    basis?: string;
  };
  current_task_id: string | null;
  recovery: {
    resume_applicable: boolean;
    blocked_reason: string | null;
    attempts: number | null;
    server_rechecks_required: boolean;
    automatic_yield_supported: boolean;
  };
  cycles: {
    request_id: string;
    station_id: string;
    requested_at: number;
    first_seen_at: number;
    last_seen_at: number;
    status: string;
    phase: string;
    target_percent: number;
    clearance_completed_at?: number;
  }[];
  history_limit: number;
}

export const chargingStages: Record<string, string> = {
  idle: "현재 충전 절차 없음",
  request_wait: "충전 요청 조건 확인 대기",
  queued: "충전 순서 대기",
  approach: "충전소로 접근 중",
  dock: "충전 접점 연결 중",
  charging: "충전 접점 유지 단계",
  undock: "충전 접점 분리 중",
  stop_handoff: "접점 반납 전 정지 확인",
  clearing: "충전 후 통로 비우는 중",
  interrupted: "충전 중단 · 복구 확인 필요",
  observation_wait: "새 관측 확인 대기",
  other_recovery: "다른 복구 절차 진행 중",
  task_running: "작업 진행 중",
  done: "접점 반납 확인 · 통로 상태 확인 필요",
  cancelled: "충전 예약 취소",
  fault: "충전 중단 · 고장 확인 필요",
  unknown: "충전 단계 확인 필요",
};

export const trafficReasons: Record<string, string> = {
  clearance_timeout:
    "통로를 비우는 제한 시간이 지났습니다. 경로와 복구 조건을 확인하세요.",
  guided_approach_occupied: "AGV 지정 경로의 통행 공간이 확보되지 않았습니다.",
  approach_traffic_blocked:
    "다른 로봇을 고려한 충전 접근 경로가 막혀 있습니다.",
  clearance_traffic_blocked: "충전 후 통로를 비울 경로가 막혀 있습니다.",
  parking_blocks_service: "충전 진입 경로를 막지 않는 대기 위치가 필요합니다.",
  peer_observation_unavailable: "주변 로봇의 새 위치 관측이 필요합니다.",
  invalid_traffic_context:
    "교통 판단에 필요한 층과 시각 정보를 확인해야 합니다.",
  invalid_traffic_clearance: "로봇 사이 통행 여유를 계산할 수 없습니다.",
  approach_route_unavailable: "충전 접근 위치까지 연결되는 경로가 없습니다.",
  clearance_route_unavailable: "충전 후 통로를 비울 경로가 없습니다.",
  fresh_observation_required: "로봇의 새 정상 관측을 기다립니다.",
  healthy_observation_required:
    "고장·잔량·자세를 확인한 뒤 정상 관측이 필요합니다.",
  item_recovery_required: "예약된 물품의 복구 상태를 먼저 확인하세요.",
};

/** Bring live charging work or an explicit access block above general details. */
export function chargingWorkflowIsActive(
  report?: ChargingWorkflowReport | null,
): boolean {
  if (!report || report.version !== "charging-workflow-v1") return false;
  return !!(
    report.request?.current ||
    report.stage === "request_wait" ||
    report.traffic?.status === "blocked" ||
    report.ownership?.egress_reservations?.some(
      (entry) => entry.robot_id === report.robot_id,
    )
  );
}

export function chargingWorkflowHasHistory(
  report?: ChargingWorkflowReport | null,
): boolean {
  return (
    !!report && !!(report.request || report.clearance || report.cycles?.length)
  );
}

const nonnegative = (value: unknown): value is number =>
  typeof value === "number" && Number.isFinite(value) && value >= 0;

/** An old, malformed, future or mismatched report cannot describe live progress. */
export function workflowIsCurrent(
  report: ChargingWorkflowReport,
  robotId: string,
  now: number,
  staleAfter: number,
  live: boolean,
): boolean {
  return !!(
    live &&
    report.version === "charging-workflow-v1" &&
    report.robot_id === robotId &&
    report.current === true &&
    report.observation?.status === "current" &&
    nonnegative(now) &&
    nonnegative(staleAfter) &&
    nonnegative(report.assessed_at) &&
    nonnegative(report.observation.sampled_at) &&
    report.observation.sampled_at <= report.assessed_at &&
    report.assessed_at <= now &&
    now - report.assessed_at <= staleAfter &&
    now - report.observation.sampled_at <= staleAfter
  );
}
