/** @jsxImportSource react */
import type {
  ChargingEnergyReport,
  ChargingServiceTarget,
  Project,
} from "./types";
import { chargingRobotIssue, type ChargingRobotContext } from "./uiMessages";

const statuses: Record<string, string> = {
  unknown: "예측 불가 · 관측과 경로 확인 필요",
  insufficient: "충전소 도달 예상 에너지 부족",
  charge_early: "업무·대기·이동을 고려한 충전 기준 도달",
  sufficient: "현재 예측상 충전 이동 여유 있음",
  queued: "예약 대기 중 · 대기 소비량 재계산",
  in_progress: "예약 진행 중 · 접점과 이동 상태 확인",
  policy_insufficient: "충전 종료 기준으로 업무 예비량 확보 어려움",
};
const reasons: Record<string, string> = {
  charge_request_cancelled:
    "이동 전 충전 예약을 취소했습니다. 명시적으로 운영을 재개하면 다시 계획합니다.",
  energy_shortfall:
    "대기와 충전 접촉까지 필요한 예상량이 현재 잔량보다 많습니다.",
  station_incompatible_or_unavailable:
    "이 로봇이 이용할 수 없거나 현재 사용할 수 없는 충전소입니다.",
  nonpositive_estimated_net_charge_power:
    "설정된 소비전력을 고려하면 충전 중 배터리 증가를 예상할 수 없습니다.",
  approach_route_unavailable: "충전 접근 지점까지 연결되는 경로가 없습니다.",
  staging_not_authored_waypoint:
    "충전 접근 지점을 AGV 지정 경유점에 포함해야 합니다.",
  invalid_guided_route: "AGV 지정 경로를 수정해야 합니다.",
  clearance_route_unavailable: "충전 후 접근 통로를 비울 경로가 없습니다.",
  dock_branch_blocked: "충전 접점으로 들어가는 구간이 막혀 있습니다.",
  predecessor_not_operational: "먼저 예약한 로봇이 정상 운행 상태가 아닙니다.",
  predecessor_requires_explicit_recovery:
    "먼저 예약한 로봇의 명시적 운영 재개가 필요합니다.",
  predecessor_stop_confirmation_pending:
    "먼저 예약한 로봇의 정지 명령 전달과 새 접점 분리·정지 관측을 확인하고 있습니다.",
  predecessor_energy_shortfall:
    "먼저 예약한 로봇도 충전 접촉 전 에너지가 부족할 것으로 예상됩니다.",
  predecessor_approach_unavailable:
    "먼저 예약한 로봇의 접근 경로를 찾을 수 없습니다.",
  predecessor_clearance_unavailable:
    "먼저 예약한 로봇이 통로를 비울 경로를 찾을 수 없습니다.",
  missing_robot_observation: "먼저 예약한 로봇의 관측을 아직 받지 못했습니다.",
  missing_predecessor_geometry:
    "먼저 예약한 로봇의 충전 접근 위치를 확인할 수 없습니다.",
  missing_clearance_target:
    "선행 로봇이 통로를 비울 목적지를 확인할 수 없습니다.",
  unknown_predecessor_phase:
    "먼저 예약한 로봇의 충전 진행 단계를 확인할 수 없습니다.",
  station_requires_explicit_recovery:
    "충전소의 고장을 확인하고 명시적으로 복구해야 합니다.",
  missing_or_stale_robot_observation: "로봇의 새 관측이 필요합니다.",
  invalid_robot_energy_observation:
    "로봇의 배터리·위치 관측값을 확인해야 합니다.",
  reordered_or_changed_robot_observation:
    "로봇 관측 순서나 동일 시각의 보고 내용이 일치하지 않습니다.",
  missing_station_observation: "충전소 관측을 아직 받지 못했습니다.",
  station_observation_not_fresh: "충전소의 새 관측이 필요합니다.",
  invalid_station_observation: "충전소 관측값을 확인해야 합니다.",
  reordered_or_changed_station_observation:
    "충전소 관측 순서나 동일 시각의 보고 내용이 일치하지 않습니다.",
  station_fault_or_invalid_observation:
    "충전소 고장 또는 관측 이상을 확인해야 합니다.",
};
const number = (value: number | null | undefined, unit: string) =>
  typeof value === "number" && Number.isFinite(value)
    ? `${value.toLocaleString("ko-KR", { maximumFractionDigits: 1 })} ${unit}`
    : "예측 불가";
const reasonText = (code?: string | null) =>
  code
    ? (reasons[code] ??
      targetReasons[code] ??
      "예측에 필요한 정보가 부족합니다. 원시 보고에서 원인을 확인하세요.")
    : null;
const targetReasons: Record<string, string> = {
  fixed_policy_target: "설정한 충전 종료값을 사용합니다.",
  no_eligible_planned_task:
    "계산할 예정 작업이 없어 통로 비움과 최소 예비량만 반영했습니다.",
  exit_route_unavailable: "충전 후 통로를 비울 경로가 필요합니다.",
  unknown_exit_energy: "접점 분리와 통로 비움 소비량을 계산할 수 없습니다.",
  task_energy_unavailable:
    "예정 작업과 이후 충전 복귀 소비량을 계산할 수 없습니다.",
  target_exceeds_capacity:
    "계산한 충전 목표가 100%를 넘어 예약을 보류합니다. 작업 조건을 조정하거나 충전 목표 방식을 ‘설정값에서 종료’로 변경하세요.",
  nonfinite_target_energy:
    "충전 목표 계산값을 확인할 수 없어 예약을 보류합니다.",
  missing_or_stale_target_observation:
    "충전 목표를 계산할 새 관측이 필요합니다.",
  invalid_target_mode: "충전 목표 방식 설정을 확인하세요.",
};
const nonnegative = (value: unknown): value is number =>
  typeof value === "number" && Number.isFinite(value) && value >= 0;
const percent = (value: unknown): value is number =>
  nonnegative(value) && value <= 100;
const nullableId = (value: unknown) =>
  value === null || (typeof value === "string" && value.trim().length > 0);
const serviceShape = (value: unknown): value is ChargingServiceTarget => {
  if (!value || typeof value !== "object" || Array.isArray(value)) return false;
  const row = value as Record<string, unknown>;
  return (
    row.version === "charging-service-target-v1" &&
    ["ready", "unknown", "infeasible"].includes(row.status as string) &&
    [null, "fixed", "task_budget", "reserve_only"].includes(
      row.purpose as string | null,
    ) &&
    (row.target_percent === null || percent(row.target_percent)) &&
    (row.required_reserve_percent === null ||
      nonnegative(row.required_reserve_percent)) &&
    (row.next_charge_trigger_percent === null ||
      nonnegative(row.next_charge_trigger_percent)) &&
    nonnegative(row.assessed_at) &&
    (row.sampled_at === null || nonnegative(row.sampled_at)) &&
    nullableId(row.station_id) &&
    nullableId(row.request_id) &&
    (row.reason === null || typeof row.reason === "string")
  );
};
const serviceReasons: Record<string, string> = {
  basic_reserve_without_task_admission:
    "통로 비움과 다음 충전 예비량을 반영한 기본 충전 목표입니다. 예정 작업의 실행 가능 여부는 별도로 확인합니다.",
  reserve_target_exceeds_capacity:
    "계산한 기본 예비량이 100%를 넘어 충전 예약을 보류합니다. 통로 비움·충전 복귀 경로와 소비 조건을 조정하세요.",
  next_charge_energy_unavailable:
    "통로를 비운 뒤 다음 충전에 필요한 소비량을 계산할 수 없어 예약을 보류합니다.",
  nonfinite_reserve_energy:
    "기본 예비량 계산값을 확인할 수 없어 충전 예약을 보류합니다.",
  service_energy_unavailable: "충전에 필요한 기본 예비량을 확인해야 합니다.",
};
const taskReasons: Record<string, string> = {
  target_exceeds_capacity:
    "계산한 업무 필요 목표가 100%를 넘어 업무 예측을 보류합니다. 기본 충전 목표는 별도로 확인하며, 작업 조건을 조정하세요.",
  nonfinite_target_energy:
    "업무 목표 계산값을 확인할 수 없어 업무 예측을 보류합니다.",
};

export default function ChargingEnergyPanel({
  report,
  project,
  now,
  live,
  reservedStationId,
  robotState,
}: {
  report: ChargingEnergyReport;
  project: Project;
  now: number;
  live: boolean;
  reservedStationId?: string | null;
  robotState?: ChargingRobotContext | null;
}) {
  const operationIssue = chargingRobotIssue(
    robotState,
    project.policy.stale_after,
    ["queued", "in_progress"].includes(report.status) ||
      !!report.target_plan?.request_id,
  );
  const operationBlocked = !!operationIssue;
  const otherRecovery = ["recovering", "transit_recovery"].includes(
    robotState?.status ?? "",
  );
  const reportTimesValid =
    nonnegative(now) &&
    nonnegative(project.policy.stale_after) &&
    nonnegative(report.sampled_at) &&
    nonnegative(report.assessed_at) &&
    report.sampled_at <= report.assessed_at &&
    report.assessed_at <= now;
  const old =
    !live ||
    !reportTimesValid ||
    now - report.assessed_at > project.policy.stale_after ||
    now - report.sampled_at! > project.policy.stale_after;
  const selected = report.candidates.find(
    (row) =>
      row.station_id === (reservedStationId ?? report.selected_station_id),
  );
  const waitingUnknown = report.status === "queued" && !selected?.known;
  const exitOccupied = report.admission_status === "waiting_for_egress";
  const targetWaiting = report.admission_status === "waiting_for_target";
  const target = report.target_plan;
  const targetSupported = target?.version === "charging-target-plan-v1";
  const targetTimesValid =
    targetSupported &&
    nonnegative(now) &&
    nonnegative(target.sampled_at) &&
    nonnegative(target.assessed_at) &&
    target.sampled_at <= target.assessed_at &&
    target.assessed_at <= now;
  const targetCommitted =
    targetSupported &&
    typeof target.request_id === "string" &&
    !!target.request_id;
  // A reserved goal is fixed at acceptance. Fresh parent reports retain that
  // goal without relabelling its original calculation as a new calculation.
  const targetCurrent =
    !old &&
    !operationBlocked &&
    targetTimesValid &&
    (targetCommitted ||
      (now - target.sampled_at! <= project.policy.stale_after &&
        now - target.assessed_at <= project.policy.stale_after));
  const targetReady =
    targetSupported &&
    target.status === "ready" &&
    percent(target.configured_target_percent) &&
    percent(target.target_percent) &&
    target.target_percent >= target.configured_target_percent &&
    (target.mode === "task_budget" ||
      (target.mode === "fixed" &&
        target.target_percent === target.configured_target_percent));
  const targetBlocked = targetSupported && targetCurrent && !targetReady;
  const targetReservationHeld =
    targetSupported && targetTimesValid && target.status === "infeasible";
  const targetOverCapacity =
    targetReservationHeld &&
    nonnegative(target.required_target_percent) &&
    target.required_target_percent > 100;
  const targetTaskName =
    targetSupported && target.task_id
      ? target.task_name ||
        project.tasks.find((task) => task.id === target.task_id)?.name ||
        target.task_id
      : "대상 작업 없음";
  const stationId = reservedStationId ?? report.selected_station_id;
  const hasService = target?.service_target !== undefined;
  const rawService = target?.service_target;
  const service = serviceShape(rawService) ? rawService : null;
  const serviceLinked = !!(
    service &&
    targetSupported &&
    nullableId(target.request_id) &&
    service.request_id === target.request_id &&
    service.assessed_at === target.assessed_at &&
    service.sampled_at === target.sampled_at &&
    (target.station_id === undefined ||
      service.station_id === target.station_id) &&
    (!stationId || service.station_id === stationId)
  );
  const serviceTimesValid = !!(
    serviceLinked &&
    service &&
    nonnegative(service.sampled_at) &&
    service.sampled_at <= service.assessed_at &&
    service.assessed_at <= now
  );
  const serviceReady = !!(
    serviceLinked &&
    service &&
    target &&
    service.status === "ready" &&
    service.station_id &&
    percent(service.target_percent) &&
    percent(target.configured_target_percent) &&
    service.target_percent >= target.configured_target_percent &&
    (service.purpose === "fixed"
      ? target.mode === "fixed" &&
        targetReady &&
        service.target_percent === target.target_percent
      : target.mode === "task_budget" &&
        nonnegative(service.required_reserve_percent) &&
        service.required_reserve_percent >= target.configured_target_percent &&
        service.target_percent >= service.required_reserve_percent &&
        nonnegative(service.next_charge_trigger_percent) &&
        nonnegative(target.exit_energy_j) &&
        (service.purpose === "task_budget"
          ? targetReady &&
            !!target.task_id &&
            service.target_percent ===
              Math.max(target.target_percent!, service.required_reserve_percent)
          : service.purpose === "reserve_only" &&
            service.target_percent === service.required_reserve_percent &&
            ((target.status === "infeasible" &&
              target.reason === "target_exceeds_capacity") ||
              (target.status === "unknown" &&
                target.reason === "task_energy_unavailable") ||
              (target.status === "ready" &&
                target.task_id === null &&
                target.reason === "no_eligible_planned_task"))))
  );
  const serviceValid = !!(
    serviceLinked &&
    service &&
    (service.status === "ready"
      ? serviceReady
      : service.target_percent === null && service.purpose === null)
  );
  const serviceCommitted = !!(serviceValid && service?.request_id);
  const serviceCurrent = !!(
    !old &&
    !operationBlocked &&
    serviceValid &&
    serviceTimesValid &&
    service &&
    (serviceCommitted ||
      (now - service.sampled_at! <= project.policy.stale_after &&
        now - service.assessed_at <= project.policy.stale_after))
  );
  const serviceActive =
    serviceCurrent &&
    serviceReady &&
    serviceCommitted &&
    !targetWaiting &&
    !exitOccupied &&
    !report.reason &&
    ["queued", "in_progress", "charge_early"].includes(report.status);
  const reserveOnly = service?.purpose === "reserve_only";
  const serviceHeading =
    !serviceValid || !serviceTimesValid
      ? "충전 목표 보고 확인 필요"
      : !serviceCurrent
        ? "이전 목표 계산 · 새 보고 확인 필요"
        : report.reason === "charge_request_cancelled"
          ? "충전 예약 취소 · 운영 재개 필요"
          : !serviceReady || targetWaiting
            ? service?.status === "infeasible"
              ? "충전 예약 보류 · 기본 예비량이 용량 초과"
              : "충전 목표 확인 대기 · 예약 보류"
            : serviceActive
              ? reserveOnly
                ? report.status === "queued"
                  ? "기본 충전 예약 대기 · 업무 예측 보류"
                  : "기본 충전 예약 진행 · 업무 예측 보류"
                : statuses[report.status]
              : serviceCommitted
                ? ["queued", "in_progress", "charge_early"].includes(
                    report.status,
                  )
                  ? "충전 예약 상태 확인 필요"
                  : (statuses[report.status] ?? "충전 예약 상태 확인 필요")
                : report.status === "sufficient"
                  ? `${reserveOnly ? "기본 충전" : "충전"} 목표 검토 · 충전 요청 기준 대기`
                  : `${reserveOnly ? "기본 충전" : "충전"} 목표 검토 · 예약 전`;
  const displayReason = (code: string) =>
    otherRecovery && code === "charge_request_cancelled"
      ? "이전 충전 예약은 취소되었습니다. 현재 복구 절차를 먼저 확인하세요."
      : hasService
        ? (serviceReasons[code] ?? taskReasons[code] ?? reasonText(code))
        : reasonText(code);
  const stationName = (id: string) =>
    project.environment.elements.find((element) => element.id === id)?.name ??
    id;
  const warning =
    old ||
    operationBlocked ||
    (hasService
      ? !serviceCurrent || !serviceReady || reserveOnly
      : targetBlocked) ||
    targetWaiting ||
    exitOccupied ||
    waitingUnknown ||
    ["unknown", "insufficient", "policy_insufficient"].includes(report.status);
  return (
    <section
      className={`charging-energy ${warning ? "needs-attention" : ""}`}
      aria-label="충전 준비 예측"
    >
      <h3>충전 준비 예측</h3>
      <p className="charging-energy-status">
        {!live
          ? "이전 예측 · 새 관측 수신 후 확인"
          : operationIssue
            ? operationIssue.title
            : old
              ? "이전 예측 · 새 관측 수신 후 확인"
              : exitOccupied
                ? "충전 예약 보류 · 복귀 공간 확보 대기"
                : hasService
                  ? serviceHeading
                  : targetWaiting
                    ? targetSupported && target.status === "infeasible"
                      ? "충전 예약 보류 · 계산 목표가 용량 초과"
                      : "충전 목표 확인 대기 · 예약 보류"
                    : targetBlocked
                      ? target?.status === "infeasible"
                        ? "충전 예약 보류 · 계산 목표가 용량 초과"
                        : "충전 예약 보류 · 목표량 확인 필요"
                      : waitingUnknown
                        ? "예약 대기 중 · 소요량 예측 보류"
                        : (statuses[report.status] ?? "예측 상태 확인 필요")}
      </p>
      {operationIssue && (
        <>
          <p>
            {!live && "마지막 로봇 보고: "}
            {operationIssue.summary}
          </p>
          <p>
            {live
              ? operationIssue.nextAction
              : "연결 복구 후 로봇·충전소 상태와 새 관측을 확인하세요."}
          </p>
          {(targetCommitted || serviceCommitted) && (
            <p className="muted">
              아래 목표는 예약 수락 당시 계산입니다. 현재 충전 진행이나 완료를
              뜻하지 않습니다.
            </p>
          )}
        </>
      )}
      {exitOccupied && !old && !operationBlocked && (
        <p>
          충전 후 이동할 공간이 확보되지 않아 아직 예약하지 않았습니다. 점유
          상태와 복귀 경로를 확인하세요.
        </p>
      )}
      {targetWaiting && !old && !operationBlocked && (
        <p>
          충전 목표를 확인 중이라 아직 예약하지 않았습니다.{" "}
          {hasService
            ? "통로 비움과 다음 충전 예비량을 확인하세요."
            : "목표량과 예정 작업의 예비량을 확인하세요."}
        </p>
      )}
      {report.reason && (
        <p>
          {(old || operationBlocked) && "이전 예측의 판단: "}
          {displayReason(report.reason)}
        </p>
      )}
      <dl className="kv">
        {stationId && (
          <>
            <dt>
              {operationBlocked && (targetCommitted || serviceCommitted)
                ? "수락 당시 충전소"
                : reservedStationId && (!hasService || serviceActive)
                  ? "예약 충전소"
                  : "검토한 충전소"}
            </dt>
            <dd>{stationName(stationId)}</dd>
          </>
        )}
        {selected && (
          <>
            <dt>
              {operationBlocked
                ? "재개 후 대기 예상"
                : exitOccupied
                  ? "공간 확보 대기"
                  : targetWaiting
                    ? "충전 목표 확인 대기"
                    : "접근 전 대기 예상"}
            </dt>
            <dd>
              {operationBlocked || exitOccupied || targetWaiting
                ? "종료 시각 예측 불가"
                : number(selected.queue_wait_seconds, "s")}
            </dd>
          </>
        )}
        {(!reservedStationId || (hasService && !serviceCommitted)) &&
          report.trigger_percent != null && (
            <>
              <dt>충전 요청 기준</dt>
              <dd>{number(report.trigger_percent, "%")}</dd>
            </>
          )}
      </dl>
      <details>
        <summary>충전 목표의 적용 기준</summary>
        {hasService && (
          <>
            <h4>
              {operationBlocked
                ? serviceCommitted
                  ? "예약 당시 목표의 기록"
                  : "검토한 충전 목표의 기록"
                : "충전 예약에 적용할 목표"}
            </h4>
            <dl className="kv">
              <dt>충전 목적</dt>
              <dd>
                {serviceValid
                  ? service?.purpose === "fixed"
                    ? "설정값 충전"
                    : service?.purpose === "task_budget"
                      ? "예정 작업 예비량 충전"
                      : service?.purpose === "reserve_only"
                        ? "기본 예비량 충전 · 업무는 별도 판단"
                        : "예측 불가"
                  : "보고 확인 필요"}
              </dd>
              <dt>
                {operationBlocked && serviceCommitted
                  ? "이전 수락 목표"
                  : operationBlocked &&
                      !old &&
                      serviceValid &&
                      serviceTimesValid
                    ? "참고용 검토 목표"
                    : !serviceCurrent
                      ? "이전 충전 목표"
                      : serviceCommitted
                        ? "예약 시 결정 목표"
                        : "검토한 충전 목표"}
              </dt>
              <dd>
                {serviceValid && serviceTimesValid
                  ? serviceReady
                    ? number(service?.target_percent, "%")
                    : service?.status === "infeasible"
                      ? "예약 보류"
                      : "예측 불가"
                  : "예측 불가"}
              </dd>
              <dt>통로 비움·다음 충전 예비량</dt>
              <dd>
                {serviceValid &&
                serviceTimesValid &&
                nonnegative(service?.required_reserve_percent) &&
                service.required_reserve_percent > 100 &&
                number(service.required_reserve_percent, "%") === "100 %"
                  ? "100 % 초과"
                  : number(
                      serviceValid && serviceTimesValid
                        ? service?.required_reserve_percent
                        : null,
                      "%",
                    )}
              </dd>
              <dt>통로 비움 후 다음 충전 기준</dt>
              <dd>
                {number(
                  serviceValid && serviceTimesValid
                    ? service?.next_charge_trigger_percent
                    : null,
                  "%",
                )}
              </dd>
              <dt>충전 목표 계산 시각</dt>
              <dd>
                {number(
                  serviceValid && serviceTimesValid
                    ? service?.assessed_at
                    : null,
                  "s",
                )}
              </dd>
            </dl>
            {!serviceValid || !serviceTimesValid ? (
              <p>
                충전 목표 보고를 확인해야 합니다. 현재 예약이나 진행 여부를
                판단할 수 없습니다.
              </p>
            ) : (
              <>
                {!serviceCurrent && (
                  <p>
                    {operationBlocked && !old && !serviceCommitted
                      ? "현재 로봇의 복구·정지 상태와 구분해 참고할 계산입니다. 충전 예약이 확정된 것은 아닙니다."
                      : "이전 계산입니다. 현재 충전 목표와 예약 상태는 새 보고와 연결 상태를 확인하세요."}
                  </p>
                )}
                {service?.reason && (
                  <p>
                    {!serviceCurrent && "계산 당시 판단: "}
                    {serviceReasons[service.reason] ??
                      targetReasons[service.reason] ??
                      "충전 목표의 계산 근거를 확인하세요."}
                  </p>
                )}
                {serviceCurrent && serviceReady && !serviceCommitted && (
                  <p>
                    {report.status === "sufficient"
                      ? "충전 요청 기준에 도달하기 전의 검토값입니다. "
                      : "검토한 목표입니다. "}
                    아직 충전 예약이 확정된 것은 아닙니다.
                  </p>
                )}
              </>
            )}
            <h4>
              {target?.mode === "fixed"
                ? "설정 목표의 기준"
                : "예정 작업의 예측"}
            </h4>
          </>
        )}
        <dl className="kv">
          <dt>목표 방식</dt>
          <dd>
            {(targetSupported
              ? target.mode
              : (project.policy.charge_target_mode ?? "fixed")) ===
            "task_budget"
              ? "예정 작업에 맞춰 충전"
              : "설정값에서 종료"}
          </dd>
          <dt>설정 종료값</dt>
          <dd>
            {number(
              targetSupported
                ? percent(target.configured_target_percent)
                  ? target.configured_target_percent
                  : null
                : project.policy.charge_until,
              "%",
            )}
          </dd>
          {targetOverCapacity && (
            <>
              <dt>
                {hasService
                  ? targetCurrent
                    ? "계산된 업무 필요 목표"
                    : "이전 계산된 업무 필요 목표"
                  : targetCurrent
                    ? "계산된 필요 목표"
                    : "이전 계산된 필요 목표"}
              </dt>
              <dd>
                {number(target.required_target_percent, "%") === "100 %"
                  ? "100 % 초과"
                  : number(target.required_target_percent, "%")}
              </dd>
            </>
          )}
          <dt>
            {hasService
              ? target?.mode === "fixed"
                ? targetCurrent
                  ? "설정 목표"
                  : "이전 설정 목표"
                : targetCurrent
                  ? "업무 예측 목표"
                  : "이전 업무 예측 목표"
              : operationBlocked && targetCommitted
                ? "이전 수락 목표"
                : operationBlocked && !old && targetTimesValid
                  ? "참고용 검토 목표"
                  : targetReservationHeld
                    ? targetCurrent
                      ? "예약 목표"
                      : "이전 예약 판단"
                    : !targetCurrent && targetSupported
                      ? "이전 계산 목표"
                      : targetCommitted
                        ? "예약 시 결정 목표"
                        : "검토한 충전 목표"}
          </dt>
          <dd>
            {hasService && targetReservationHeld
              ? "업무 예측 보류"
              : targetReservationHeld
                ? "예약 보류"
                : number(
                    targetReady && targetTimesValid
                      ? target.target_percent
                      : null,
                    "%",
                  )}
          </dd>
          <dt>대상 작업</dt>
          <dd>{targetSupported ? targetTaskName : "보고 대기"}</dd>
          <dt>분리·통로 비움 예산</dt>
          <dd>
            {number(
              targetSupported && nonnegative(target.exit_energy_j)
                ? target.exit_energy_j
                : null,
              "J",
            )}
          </dd>
          <dt>이후 작업·충전 복귀·예비량</dt>
          <dd>
            {number(
              targetSupported && nonnegative(target.task_required_percent)
                ? target.task_required_percent
                : null,
              "%",
            )}
          </dd>
          <dt>목표 계산 시각</dt>
          <dd>{number(targetTimesValid ? target.assessed_at : null, "s")}</dd>
        </dl>
        {!targetSupported ? (
          <p>충전 목표 보고를 기다리고 있습니다.</p>
        ) : (
          <>
            {!targetCurrent && (
              <p>
                {hasService
                  ? "이전 업무 계산입니다. 현재 업무 예측은 새 보고와 연결 상태를 확인하세요."
                  : "이전 계산입니다. 현재 예약 목표는 새 보고와 연결 상태를 확인하세요."}
              </p>
            )}
            {target.reason && (
              <p>
                {!targetCurrent && "계산 당시 판단: "}
                {(hasService ? taskReasons[target.reason] : null) ??
                  targetReasons[target.reason] ??
                  "충전 목표의 계산 근거를 확인하세요. 자세한 원인은 원시 보고에 있습니다."}
              </p>
            )}
            {!hasService &&
              targetCurrent &&
              !targetCommitted &&
              targetReady && (
                <p>검토한 목표이며 아직 충전 예약이 확정된 것은 아닙니다.</p>
              )}
          </>
        )}
        <p className="muted">
          예정 작업 방식은 설정 종료값을 최소 목표로 사용합니다. 예약 때 계산한
          목표는 작업 배정이나 실제 완료를 보장하지 않습니다.
        </p>
      </details>
      <details>
        <summary>계산 근거 · 후보 {report.candidates.length}곳</summary>
        <p className="muted">
          설정값에 따른 추정입니다. 실제 소비량·대기 종료 시각을 보장하지
          않습니다. 대기 소비는 20 W, 충전 중 증가량은 입력×효율에서 설정된
          소비전력을 뺀 값으로 계산합니다.
        </p>
        <p className="muted">
          관측 {number(report.sampled_at, "s")} · 계산{" "}
          {number(report.assessed_at, "s")} · 현재 실행 시각 기준
        </p>
        {report.task_needed_percent != null && (
          <p className="muted">
            업무 예비량 기준 {number(report.task_needed_percent, "%")} · 충전
            경로 기준 {number(report.route_trigger_percent, "%")}.{" "}
            {hasService && !serviceValid
              ? "보고된 기준값입니다. 실제 요청 기준은 충전 목표 보고를 확인하세요."
              : hasService && reserveOnly
                ? "업무 예비량은 별도 예측입니다. 기본 충전 요청 기준에는 충전 경로와 최소 잔량을 반영합니다."
                : "현재 요청 기준에는 두 조건을 함께 반영합니다."}
          </p>
        )}
        {report.candidates.length === 0 && (
          <p>
            {report.status === "in_progress" &&
            !old &&
            !operationBlocked &&
            (!hasService || serviceActive)
              ? "이미 예약한 충전·분리·통로 이동은 실행 상태에서 확인하세요."
              : "현재 평가된 충전소 후보가 없습니다."}
          </p>
        )}
        {report.candidates.map((row) => (
          <div className="charging-energy-candidate" key={row.station_id}>
            <strong>{stationName(row.station_id)}</strong>
            <small className="muted"> · {row.station_id}</small>
            <span>
              {!row.known
                ? " · 예측 불가"
                : row.feasible
                  ? old
                    ? " · 이전 예상량 충족"
                    : " · 예상량 충족"
                  : old
                    ? " · 이전 예상량 부족"
                    : " · 예상량 부족"}
            </span>
            {row.reason && <p>{reasonText(row.reason)}</p>}
            <dl className="kv">
              <dt>대기 시간</dt>
              <dd>{number(row.queue_wait_seconds, "s")}</dd>
              <dt>대기 소비</dt>
              <dd>{number(row.wait_energy_j, "J")}</dd>
              <dt>접근 / 도킹 소비</dt>
              <dd>
                {number(row.approach_energy_j, "J")} /{" "}
                {number(row.dock_energy_j, "J")}
              </dd>
              <dt>접촉 전 필요량</dt>
              <dd>{number(row.required_before_contact_j, "J")}</dd>
              <dt>관측 잔량</dt>
              <dd>{number(row.available_j, "J")}</dd>
              <dt>예상 부족량</dt>
              <dd>{number(row.shortfall_j, "J")}</dd>
            </dl>
            {!!row.queue_forecast?.ahead.length && (
              <p className="muted">
                선행 예약:{" "}
                {row.queue_forecast.ahead
                  .map(
                    (entry) =>
                      project.robots.find(
                        (robot) => robot.id === entry.robot_id,
                      )?.name ?? entry.robot_id,
                  )
                  .join(" → ")}
                . 접점 분리 후 통로를 비우는 시간도 포함합니다.
              </p>
            )}
          </div>
        ))}
        <details>
          <summary>원시 예측 보고</summary>
          <pre>{JSON.stringify(report, null, 2)}</pre>
        </details>
      </details>
      <p className="muted">
        충전 성공은 실제 접점·입력 전력·분리 관측으로 확인합니다.
      </p>
    </section>
  );
}
