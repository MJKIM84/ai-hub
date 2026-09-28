import type { Floor, Pose, RobotState, RuntimeEvent } from "./types";

/** Keep empty command inputs distinct from the last valid coordinate or zero. */
export function validateMoveTarget(
  input: Record<keyof Pose, string>,
  floor: Pick<Floor, "name" | "width" | "depth"> | null,
): {
  target: Pose | null;
  errors: Partial<Record<keyof Pose, string>>;
  reason: string | null;
} {
  const errors: Partial<Record<keyof Pose, string>> = {};
  const target = {} as Pose;
  const labels = {
    x: "목표 X (m)",
    y: "목표 Y (m)",
    z: "목표 Z (m)",
    yaw: "방향 (rad)",
  };
  for (const axis of ["x", "y", "z", "yaw"] as const) {
    const raw = input[axis];
    if (
      typeof raw !== "string" ||
      !raw.trim() ||
      !/^[+-]?(?:\d+\.?\d*|\.\d+)(?:e[+-]?\d+)?$/i.test(raw.trim()) ||
      !Number.isFinite(Number(raw))
    )
      errors[axis] = `${labels[axis]}에 공백 없이 유한한 숫자를 입력하세요.`;
    else target[axis] = Number(raw);
  }
  const validFloor =
    floor &&
    Number.isFinite(floor.width) &&
    floor.width > 0 &&
    Number.isFinite(floor.depth) &&
    floor.depth > 0;
  if (validFloor) {
    for (const [axis, maximum] of [
      ["x", floor.width],
      ["y", floor.depth],
    ] as const)
      if (!errors[axis] && (target[axis] < 0 || target[axis] > maximum))
        errors[axis] =
          `${labels[axis]}는 ${floor.name}의 0~${maximum} m 안으로 입력하세요. 도면에서 목표 위치를 확인하세요.`;
  }
  const reason =
    Object.values(errors)[0] ??
    (validFloor
      ? null
      : "현재 실행의 로봇 관측과 층 구성을 수신한 뒤 목표 범위를 확인하세요.");
  return { target: reason ? null : target, errors, reason };
}

export type MessageTone = "neutral" | "info" | "warning" | "danger" | "success";
export interface EventDescription {
  title: string;
  summary: string;
  nextAction?: string;
  tone: MessageTone;
}

const eventNames: Record<string, string> = {
  run_created: "실행 초기화",
  sample_stopped: "샘플 자동 종료",
  assignment: "작업 배정",
  replan: "경로 재계획",
  task_completed: "작업 완료 확인",
  task_failed: "작업 실패",
  task_retry: "작업 재시도 대기",
  task_cancelled: "작업 취소",
  command: "명령 수락",
  command_requested: "명령 요청",
  command_accepted: "명령 수락",
  command_executing: "명령 실행 중",
  command_completed: "명령 결과 확인",
  command_expired: "명령 기한 만료",
  command_rejected: "명령 거부",
  command_failed: "명령 실패",
  command_superseded: "이전 명령 종료",
  robot_resumed: "운영 재개 요청 수락",
  collision: "충돌 접촉",
  near_miss: "안전 간격 부족",
  fall: "전도 감지",
  damage: "물품 손상 추정",
  fault: "장애 조건 적용",
  fault_scheduled: "장애 주입 예약",
  recovery: "관측 연결 복구",
  simulation_failed: "물리 실행 실패",
  facility_phase: "승강기 상태 변경",
  facility_call: "승강기 호출 수락",
  elevator_exit: "하차 확인",
  charging_requested: "충전 예약 요청",
  charging_phase: "충전 단계 변경",
  charging_departure: "충전 통로 비우기",
  charging_completed: "충전 후 통로 비움 확인",
  manipulation_started: "물품 조작 시작",
  manipulation_phase: "물품 조작 단계 변경",
  cooperation_started: "협업 시작",
  cooperation_failed: "협업 실패",
  cooperation_cancelled: "협업 취소",
  cooperation_donor_grasped: "상차 로봇의 파지 확인",
  cooperation_loaded: "운반차 상차 확인",
  cooperation_transferred: "물품 인계 확인",
  cooperation_recovery_started: "물품 복구 요청 수락",
  cooperation_recovery_failed: "물품 복구 중단",
  cooperation_recovery_completed: "물품 복구 확인",
  person_pause: "보행자 일시 정지",
  person_turn: "보행자 방향 변경",
};
const statuses: Record<string, string> = {
  sending: "전송 중",
  unknown: "결과 미확인",
  requested: "요청됨",
  accepted: "수락됨",
  executing: "실행 중",
  running: "실행 중",
  completed: "완료 확인",
  skipped: "분기 조건 불충족 · 미실행",
  failed: "실패",
  rejected: "거부됨",
  expired: "기한 만료",
  superseded: "새 명령으로 교체",
  cancelled: "취소됨",
  pending: "발생 대기",
  waiting: "대기",
  idle: "유휴",
  stopped: "정지",
  paused: "일시 정지",
  disconnected: "연결 끊김",
  recovery_required: "복구 확인 필요",
  recovering: "복구 중",
  cooperating: "협업 중",
  unchanged: "변경 없음",
};
// Robot operational status is separate from command acknowledgement status.
// charging spans queueing, docking, energy transfer and clearing the station.
const robotStatuses: Record<string, string> = {
  idle: "대기",
  working: "작업 중",
  manual: "수동 이동",
  stopped: "정지",
  charging: "충전 절차 중",
  manipulating: "물품 조작 중",
  cooperating: "협업 중",
  recovering: "물품 복구 중",
  recovery_required: "복구 확인 필요",
  transit_recovery: "층간 이동 복구",
  disconnected: "연결 끊김",
  fault: "고장",
  draft: "초안",
  stale: "오래된 관측",
  unknown: "상태 확인 필요",
  moving: "이동 중",
  executing: "수행 중",
  running: "실행 중",
  waiting: "대기",
  blocked: "진행 대기",
  paused: "일시 정지",
  completed: "완료 확인",
  skipped: "분기 조건 불충족 · 미실행",
  failed: "실패",
};
const commands: Record<string, string> = {
  stop: "정지",
  stand: "서기",
  sit: "앉기",
  move: "이동",
  resume: "운영 재개",
};

export function eventKindLabel(kind: string): string {
  if (kind.startsWith("person_")) return "보행자 행동";
  if (kind === "pedestrian_avoidance") return "사람 회피";
  return eventNames[kind] ?? "실행 사건";
}
export function commandKindLabel(kind: string): string {
  return commands[kind] ?? kind;
}
export function commandStatusLabel(status: string): string {
  return statuses[status] ?? status;
}
export function taskStatusLabel(status: string): string {
  return statuses[status] ?? status;
}
export function robotStatusLabel(status: string | null | undefined): string {
  if (!status?.trim()) return "상태 미수신";
  return robotStatuses[status] ?? "상태 확인 필요";
}
const robotReasons: Record<string, string> = {
  approach_timeout: "충전 접근 제한 시간 초과",
  dock_timeout: "충전 접점 진입 제한 시간 초과",
  charging_timeout: "충전 제한 시간 초과",
  undock_timeout: "충전 접점 분리 제한 시간 초과",
  contact_timeout: "충전 접촉 확인 시간 초과",
  contact_or_alignment_lost: "충전 접촉 또는 정렬 확인 끊김",
  missing_or_invalid_connector: "충전 접점 관측 확인 필요",
  station_fault: "충전소 고장 보고",
  robot_fault: "로봇 고장 보고",
  operator_hold: "운영자 정지 유지",
  fault: "로봇 고장 보고",
  disconnected: "로봇 관측 연결 끊김",
  cancelled_requires_recovery: "충전 예약 취소 후 복구 확인 필요",
  unreserved_contact: "예약되지 않은 충전 접촉 감지",
  missing_or_invalid_observation: "관측 누락 또는 형식 이상",
  stale_observation: "새 관측 수신 지연",
  future_observation: "관측 시각 확인 필요",
  invalid_observation: "관측값 확인 필요",
  out_of_order_observation: "관측 순서 확인 필요",
  altered_duplicate_observation: "같은 시각의 관측 내용 불일치",
  "stop 명령 수락": "정지 명령 수락",
  "stand 명령 수락": "서기 명령 수락 · 자동 운영 정지",
  "sit 명령 수락": "앉기 명령 수락 · 자동 운영 정지",
};
export function robotReasonLabel(reason: string | null | undefined): string {
  if (typeof reason !== "string" || !reason.trim()) return "보고된 사유 없음";
  return robotReasons[reason] ?? reason;
}
export type ChargingRobotContext = Pick<
  RobotState,
  "status" | "reason" | "operator_hold" | "observation_age"
>;
/** Operational evidence takes precedence over a retained energy forecast. */
export function chargingRobotIssue(
  robot: ChargingRobotContext | null | undefined,
  staleAfter: number,
  checkProgress = true,
): { title: string; summary: string; nextAction: string } | null {
  // Reports rendered without the newer snapshot context retain legacy behavior.
  if (robot === undefined) return null;
  const unknown = {
    title: "충전 상태 확인 대기 · 새 관측 필요",
    summary: "현재 로봇 상태를 확인할 수 없습니다.",
    nextAction: "관측 연결과 로봇·충전소의 새 정상 관측을 확인하세요.",
  };
  if (
    !robot ||
    typeof robot.status !== "string" ||
    !robot.status.trim() ||
    typeof robot.reason !== "string" ||
    (robot.operator_hold !== undefined &&
      typeof robot.operator_hold !== "boolean")
  )
    return unknown;
  if (
    ["disconnected", "stale", "unknown"].includes(robot.status) ||
    [
      "disconnected",
      "missing_or_invalid_observation",
      "stale_observation",
      "future_observation",
      "invalid_observation",
      "out_of_order_observation",
      "altered_duplicate_observation",
    ].includes(robot.reason) ||
    typeof robot.observation_age !== "number" ||
    !Number.isFinite(robot.observation_age) ||
    robot.observation_age < 0 ||
    !Number.isFinite(staleAfter) ||
    staleAfter < 0 ||
    robot.observation_age > staleAfter
  )
    return { ...unknown, summary: robotReasonLabel(robot.reason) };
  const summary = robotReasonLabel(robot.reason);
  if (
    robot.status === "fault" ||
    ["robot_fault", "station_fault", "fault"].includes(robot.reason)
  )
    return {
      title: "충전 중단 · 고장 확인 필요",
      summary,
      nextAction:
        "로봇·충전소의 고장 원인을 먼저 해소하고 새 정상 관측을 확인하세요. 고장 상태에서는 재개할 수 없습니다.",
    };
  if (["recovering", "transit_recovery"].includes(robot.status)) {
    const itemRecovery = robot.status === "recovering";
    return {
      title: `${itemRecovery ? "물품 복구 중" : "층간 이동 복구 중"} · ${checkProgress ? "충전 진행 확인 보류" : "충전 예측 참고"}`,
      summary,
      nextAction: itemRecovery
        ? "‘작업 진행과 물리 복구’에서 현재 복구 절차를 확인하세요. 충전은 복구 이후 로봇 상태로 다시 판단합니다."
        : "‘시설과 예약’에서 승강기·하차 상태를 확인하세요. 충전 진행과는 별도로 판단합니다.",
    };
  }
  if (
    robot.operator_hold ||
    ["stopped", "paused"].includes(robot.status) ||
    [
      "operator_hold",
      "stop 명령 수락",
      "stand 명령 수락",
      "sit 명령 수락",
    ].includes(robot.reason)
  )
    return {
      title: "충전 중단 · 운영자 정지",
      summary,
      nextAction:
        "정지 원인과 로봇·충전소 상태를 확인한 뒤, 사용 가능한 ‘운영 재개’를 요청하세요.",
    };
  if (
    robot.status === "recovery_required" ||
    (Object.prototype.hasOwnProperty.call(robotReasons, robot.reason) &&
      !robot.reason.endsWith(" 명령 수락"))
  )
    return {
      title: "충전 중단 · 복구 확인 필요",
      summary,
      nextAction:
        "접근 경로·접점과 로봇·충전소의 새 정상 관측을 확인한 뒤, 사용 가능한 ‘운영 재개’를 요청하세요.",
    };
  if (checkProgress && robot.status !== "charging")
    return {
      title: "충전 진행 상태 확인 필요",
      summary: `현재 로봇 상태는 ‘${robotStatusLabel(robot.status)}’입니다. 충전 예측만으로 진행이나 완료를 판단할 수 없습니다.`,
      nextAction: "로봇 상태와 시설 예약의 현재 단계를 확인하세요.",
    };
  return null;
}
export function commandFeedbackSummary(value: Record<string, unknown>): string {
  for (const key of ["reason", "message"]) {
    const detail = value[key];
    if (typeof detail === "string" && detail.trim()) return detail.trim();
  }
  const summaries: Record<string, string> = {
    sending:
      "명령을 전송하고 있습니다. 실행부의 수락은 아직 확인되지 않았습니다.",
    requested: "명령을 요청했습니다. 실행부의 수락을 확인하고 있습니다.",
    accepted:
      "실행부가 요청을 수락했습니다. 동작 완료는 아직 확인되지 않았습니다.",
    executing: "명령을 실행 중입니다. 동작 완료는 아직 확인되지 않았습니다.",
    running: "명령을 실행 중입니다. 동작 완료는 아직 확인되지 않았습니다.",
    completed: "실행부가 관측 기준으로 명령 완료를 보고했습니다.",
    rejected:
      "실행부가 명령을 거부했습니다. 현재 상태와 입력 조건을 확인하세요.",
    failed:
      "명령 수행 실패가 보고됐습니다. 로봇 상태와 사건 기록을 확인하세요.",
    expired:
      "명령의 유효 시간이 지났습니다. 현재 로봇 상태를 확인한 뒤 필요한 명령을 요청하세요.",
    superseded: "새 명령으로 교체됐습니다. 이전 동작의 완료를 뜻하지 않습니다.",
    cancelled:
      "명령 취소가 보고됐습니다. 실제 정지 여부는 로봇 관측을 확인하세요.",
    unknown:
      "요청 결과를 확인하지 못했습니다. 현재 상태와 명령 이력을 먼저 확인하세요.",
    unchanged: "실행부가 추가 변경 없이 현재 상태를 유지한다고 보고했습니다.",
  };
  return typeof value.status === "string"
    ? (summaries[value.status] ??
        "명령의 결과 상태를 아직 확인하지 못했습니다.")
    : "명령의 결과 상태를 아직 받지 못했습니다.";
}
export function formatSimulationTime(
  value: number | null | undefined,
  digits = 2,
): string {
  return typeof value === "number" && Number.isFinite(value)
    ? `${value.toFixed(digits)}초`
    : "시각 미수신";
}
export function eventIsCommand(event: RuntimeEvent): boolean {
  return (
    event.kind.startsWith("command") ||
    ["robot_resumed", "facility_call"].includes(event.kind)
  );
}
export function eventIsFailure(event: RuntimeEvent): boolean {
  return (
    ["error", "warning", "critical"].includes(event.severity) ||
    /failed|rejected|expired/.test(event.kind) ||
    ["collision", "near_miss", "fall", "damage", "fault"].includes(event.kind)
  );
}

/** Explanations describe reported evidence; suggested actions never issue commands. */
export function describeRuntimeEvent(event: RuntimeEvent): EventDescription {
  const detail = event.details ?? {};
  const original =
    event.message?.trim() ||
    "실행부가 사건을 기록했습니다. 원시 기록에서 상세 내용을 확인하세요.";
  const result: EventDescription = {
    title: eventKindLabel(event.kind),
    summary: original,
    tone:
      event.severity === "error" || /failed|rejected/.test(event.kind)
        ? "danger"
        : eventIsFailure(event)
          ? "warning"
          : "neutral",
  };
  if (event.kind === "person_pedestrian_mode") {
    const modes: Record<string, string> = {
      walking: "보행을 시작하거나 다시 이어갑니다.",
      separating: "주변 사람과 거리를 확보하며 이동합니다.",
      avoiding: "주변 개체를 피해 이동합니다.",
      yielding: "다른 개체에 진로를 양보하고 있습니다.",
      behavior_pause: "설정한 행동에 따라 잠시 멈춥니다.",
      crossing: "허용된 공간에서 로봇 진행 경로를 가로지릅니다.",
      at_destination: "선택한 목적지에 도착했습니다.",
      at_waypoint: "지정 경유지에 도착했습니다.",
      perception_hold: "새 주변 관측을 기다리고 있습니다.",
      static_clearance_hold: "통행 공간을 확보하지 못해 대기합니다.",
      route_blocked: "통행 가능한 경로를 다시 확인합니다.",
      no_allowed_destination:
        "허용 구역 안에서 가능한 목적지를 찾지 못했습니다.",
    };
    return {
      ...result,
      summary:
        modes[String(detail.mode)] ??
        "보행 상태가 바뀌었습니다. 상세 기록에서 원인을 확인하세요.",
    };
  }
  if (event.kind === "person_destination_changed")
    return {
      ...result,
      summary: "허용된 이동 공간 안에서 다음 목적지를 선택했습니다.",
    };
  if (event.kind === "person_walking_paused")
    return { ...result, summary: "설정한 행동에 따라 잠시 멈춥니다." };
  if (event.kind === "person_walking_resumed")
    return { ...result, summary: "계획한 휴식을 마치고 다시 걷습니다." };
  if (event.kind === "collision")
    return {
      ...result,
      summary:
        "개체 사이의 물리 접촉이 기록됐습니다. 접촉 기록만으로 손상을 확정하지 않습니다.",
      nextAction:
        "관련 개체와 접촉 위치를 확인한 뒤 통과 폭·경로·속도 설정을 검토하세요.",
    };
  if (event.kind === "near_miss")
    return {
      ...result,
      nextAction:
        "두 개체의 이동 공간과 안전 거리를 확인하고 통행 우선순위를 검토하세요.",
    };
  if (event.kind === "fall")
    return {
      ...result,
      nextAction:
        "로봇의 자세와 접촉 상태를 확인하세요. 복구 조건을 확인하기 전에는 이동을 재개하지 마세요.",
    };
  if (event.kind === "damage")
    return {
      ...result,
      summary:
        "물품 충격이 설정한 손상 임계값을 넘었습니다. 연구용 손상 추정이며 실제 파손 판정과 다릅니다.",
      nextAction:
        "원시 기록의 충격과 물품 손상 설정, 낙하·접촉 사건을 함께 확인하세요.",
    };
  if (event.kind === "fault" && detail.kind === "recover")
    return {
      ...result,
      title: "장애 복구 조건 적용",
      tone: "info",
      nextAction:
        "관측 연결과 정지·복구 상태를 확인하세요. 복구 조건 적용은 작업 완료나 자동 재출발을 뜻하지 않습니다.",
    };
  if (event.kind === "fault_scheduled")
    return {
      ...result,
      nextAction:
        "원시 기록에서 적용 시각과 대상, 장애 종류를 확인하세요. 예약은 장애 발생 확인과 다릅니다.",
    };
  if (event.kind === "recovery")
    return {
      ...result,
      tone: "info",
      nextAction:
        "물품과 시설 예약, 운영자 정지 상태를 확인하세요. 연결 복구만으로 작업이 완료되거나 운영 정지가 풀리지는 않습니다.",
    };
  if (event.kind === "command" || event.kind === "command_accepted") {
    const kind =
      typeof detail.kind === "string"
        ? commandKindLabel(detail.kind)
        : "로봇 동작";
    return {
      ...result,
      tone: "info",
      summary: `${kind} 요청을 실행부가 수락했습니다. 실제 동작 완료는 명령 피드백으로 확인합니다.`,
      nextAction: "관련 로봇의 최근 명령과 관측 상태를 확인하세요.",
    };
  }
  if (event.kind === "command_completed")
    return {
      ...result,
      tone: "success",
      summary:
        "실행부가 관측으로 명령 결과를 확인했습니다. 확인한 동작과 시각은 원시 기록에 표시됩니다.",
    };
  if (event.kind === "command_expired")
    return {
      ...result,
      nextAction:
        "지연·연결 상태와 명령 유효 시간을 확인하세요. 현재 상태를 확인한 뒤 필요한 명령만 새로 요청하세요.",
    };
  if (event.kind === "command_superseded")
    return {
      ...result,
      summary:
        "기존 명령이 새 요청으로 종료됐습니다. 기존 동작의 완료를 뜻하지 않습니다.",
      nextAction: "로봇 상세에서 새 명령의 상태를 확인하세요.",
    };
  if (event.kind === "robot_resumed")
    return {
      ...result,
      tone: "info",
      summary:
        "운영 재개 요청이 수락됐습니다. 이동·접점 분리·작업 완료 여부는 이후 관측으로 확인합니다.",
    };
  if (event.kind === "simulation_failed")
    return {
      ...result,
      nextAction:
        "실패 시점과 원시 기록을 보존하고 물리 설정·초기 배치를 검토하세요. 초기화하면 새 실행으로 구분됩니다.",
    };
  if (event.kind.includes("cooperation") && /failed|cancelled/.test(event.kind))
    return {
      ...result,
      nextAction:
        "참여 로봇의 물품 접촉·소유 상태와 유지된 예약을 확인하세요. 가능한 물품 복구 절차를 완료한 뒤 재시도를 결정하세요.",
    };
  if (
    /통신|관측.*(단절|지연|소실|오래)|stale|communication|heartbeat/i.test(
      original,
    ) ||
    detail.kind === "communication"
  )
    return {
      ...result,
      nextAction:
        "관련 로봇의 관측 나이·통신 지연·누락 설정을 확인하세요. 연결 복구 후에도 운영 정지와 물품 복구 상태를 확인해야 합니다.",
    };
  if (eventIsFailure(event))
    return {
      ...result,
      nextAction:
        "관련 개체의 상태와 아래 실행부 기록을 확인하고, 실패 원인에 맞는 설정 또는 복구 절차를 검토하세요.",
    };
  if (
    event.kind.endsWith("completed") ||
    event.kind === "cooperation_transferred"
  )
    result.tone = "success";
  return result;
}

/** Preserve the raw response for a details view; never equate a network error with rejection. */
export function userFacingError(error: unknown): {
  message: string;
  nextAction: string;
  raw: string;
} {
  const raw =
    error instanceof Error
      ? error.message
      : typeof error === "string"
        ? error
        : String(error ?? "알 수 없는 오류");
  const metadata =
    error && typeof error === "object"
      ? (error as { status?: unknown; uncertain?: unknown })
      : undefined;
  if (
    metadata?.uncertain === true ||
    /failed to fetch|networkerror|network error|load failed|timeout|timed out|aborterror|응답.*(?:확인하지|지연)|연결.*끊/i.test(
      raw,
    )
  )
    return {
      message: /[가-힣]/.test(raw)
        ? raw
        : "실행부의 응답을 확인하지 못했습니다.",
      nextAction:
        "연결 상태와 현재 실행·명령 상태를 먼저 확인하세요. 이미 수락된 요청일 수 있으므로 같은 동작을 바로 반복하지 마세요.",
      raw,
    };
  if (
    metadata?.status === 401 ||
    metadata?.status === 403 ||
    /unauthorized|forbidden/i.test(raw)
  )
    return {
      message: "요청에 필요한 접근 권한을 확인할 수 없습니다.",
      nextAction: "연결 대상과 인증·제어 권한을 확인한 뒤 다시 요청하세요.",
      raw,
    };
  if (error instanceof SyntaxError || /JSON.*(?:형식|구조|읽)/i.test(raw))
    return {
      message: /[가-힣]/.test(raw)
        ? raw
        : "JSON 형식으로 읽을 수 없는 내용입니다.",
      nextAction:
        "입력한 JSON이나 가져온 파일의 형식을 확인한 뒤 다시 시도하세요.",
      raw,
    };
  if (
    /통과 가능한 경로 없음|몸체·장비 공간을 만족하는 경로 없음|no (?:passable )?(?:path|route)/i.test(
      raw,
    )
  )
    return {
      message: "현재 위치에서 목표까지 통과할 수 있는 경로를 찾지 못했습니다.",
      nextAction:
        "현재 실행의 2D 도면에서 목표를 층 안의 빈 공간으로 바꾸고, 장애물·출입 제한과 몸체·장비의 여유 공간을 확인하세요. AGV는 지정 경로의 진행 방향도 확인하세요.",
      raw,
    };
  if (
    metadata?.status === 422 ||
    /validation|finite|greater than|less than|field required|입력|유한한|정수|필수 값|허용 범위/i.test(
      raw,
    )
  )
    return {
      message: /[가-힣]/.test(raw)
        ? raw
        : "입력값이 허용 조건을 만족하지 않습니다.",
      nextAction:
        "해당 입력 항목의 필수 값·단위·허용 범위를 확인하고 수정하세요.",
      raw,
    };
  return {
    message: /[가-힣]/.test(raw) ? raw : "요청을 처리하지 못했습니다.",
    nextAction:
      "현재 실행 상태와 요청 조건을 확인한 뒤 필요한 항목을 수정하세요.",
    raw,
  };
}
