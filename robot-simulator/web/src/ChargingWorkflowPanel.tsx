/** @jsxImportSource react */
import type { ConsumptionMeterReport, Project } from "./types";
import { consumptionMeterView, consumptionNumber } from "./consumptionMeter";
import {
  chargingRobotIssue,
  robotReasonLabel,
  type ChargingRobotContext,
} from "./uiMessages";
import {
  chargingStages,
  trafficReasons,
  workflowIsCurrent,
  type ChargingWorkflowReport,
} from "./chargingWorkflow";

const quantity = (value: unknown, unit: string) =>
  typeof value === "number" && Number.isFinite(value) && value >= 0
    ? `${value.toLocaleString("ko-KR", { maximumFractionDigits: 1 })} ${unit}`
    : "미확인";
const taskLabels: Record<string, string> = {
  not_observed: "통로 비움 완료 보고 없음",
  awaiting_assignment: "통로 비움 확인 · 다음 작업 배정 대기",
  running: "통로 비움 후 배정된 작업 진행 중",
  completed: "통로 비움 후 배정된 작업 완료 보고",
  waiting: "통로 비움 후 배정된 작업 대기",
  failed: "통로 비움 후 배정된 작업 실패",
  cancelled: "통로 비움 후 배정된 작업 취소",
};
const observationOrFaultReasons = [
  "robot_fault",
  "station_fault",
  "fault",
  "disconnected",
  "missing_or_invalid_observation",
  "stale_observation",
  "future_observation",
  "invalid_observation",
  "out_of_order_observation",
  "altered_duplicate_observation",
];

export default function ChargingWorkflowPanel({
  report,
  robotId,
  project,
  now,
  live,
  runId,
  consumption,
  onResume,
  resumeAllowed = false,
  busy = false,
  robotState,
}: {
  report?: ChargingWorkflowReport | null;
  robotId: string;
  project: Project;
  now: number;
  live: boolean;
  runId?: string;
  consumption?: ConsumptionMeterReport | null;
  onResume?: () => void;
  resumeAllowed?: boolean;
  busy?: boolean;
  robotState?: ChargingRobotContext | null;
}) {
  if (!report) return null;
  if (
    report.version !== "charging-workflow-v1" ||
    report.robot_id !== robotId ||
    !report.observation ||
    !report.ownership ||
    !report.traffic ||
    !report.recovery ||
    !report.task_after_clearance ||
    !Array.isArray(report.ownership.queue_robot_ids) ||
    !Array.isArray(report.ownership.egress_reservations)
  )
    return (
      <section
        className="charging-workflow needs-attention"
        aria-label="충전 실행 상태"
      >
        <h3>충전 실행 상태</h3>
        <p>충전 진행 보고를 확인해야 합니다.</p>
      </section>
    );
  const reportCurrent = workflowIsCurrent(
    report,
    robotId,
    now,
    project.policy.stale_after,
    live,
  );
  const operationIssue = chargingRobotIssue(
    robotState,
    project.policy.stale_after,
    false,
  );
  const contextMismatch =
    robotState != null &&
    (robotState.status !== report.robot_status ||
      !!robotState.operator_hold !== report.operator_hold);
  const current = reportCurrent && !contextMismatch;
  const justStopped =
    contextMismatch &&
    !observationOrFaultReasons.includes(robotState?.reason ?? "") &&
    ![
      "fault",
      "disconnected",
      "stale",
      "unknown",
      "recovering",
      "transit_recovery",
    ].includes(robotState?.status ?? "") &&
    (robotState?.operator_hold || robotState?.status === "stopped");
  const stageTitle = !live
    ? "이전 충전 상태 · 새 관측 필요"
    : justStopped
      ? robotState?.reason === "stop 명령 수락"
        ? "정지 요청 수락 · 새 진행 보고 대기"
        : "운영자 정지 · 새 진행 보고 대기"
      : operationIssue
        ? operationIssue.title
        : contextMismatch
          ? "충전 진행 보고 갱신 대기"
          : current
            ? (chargingStages[report.stage] ?? "충전 단계 확인 필요")
            : "이전 충전 상태 · 새 관측 필요";
  const name = (id: string) =>
    project.robots.find((r) => r.id === id)?.name ?? id;
  const station = report.station_id
    ? `${project.environment.elements.find((e) => e.id === report.station_id)?.name || "충전소"} · ${report.station_id}`
    : "아직 선택되지 않음";
  const req = report.request;
  const explicitBlock = report.traffic.status === "blocked";
  const interrupted = ["interrupted", "fault", "observation_wait"].includes(
    report.stage,
  );
  const queueIndex = report.ownership.queue_robot_ids.indexOf(robotId);
  const clearance = report.clearance;
  const clearanceKnown =
    !!clearance &&
    Number.isFinite(clearance.completed_at) &&
    clearance.completed_at >= 0 &&
    clearance.completed_at <= now;
  const task = report.task_after_clearance;
  const ownEgress = report.ownership.egress_reservations.filter(
    (entry) => entry.robot_id === robotId,
  );
  const meter = consumptionMeterView(consumption, {
    runId,
    robotId,
    now,
    live,
    staleAfter: project.policy.stale_after,
  });
  const counters = ["ready", "first"].includes(meter.mode)
    ? meter.accepted?.counters
    : null;
  const chargedWh = (value: number | undefined) =>
    consumptionNumber(value == null ? null : value / 3600, "Wh");
  const resumeApplicable =
    report.recovery.resume_applicable ||
    !!robotState?.operator_hold ||
    (robotState?.status === "recovery_required" && !!req?.current);
  const latestHealthy =
    robotState === undefined ||
    (!!robotState &&
      ![
        "fault",
        "disconnected",
        "stale",
        "unknown",
        "recovering",
        "transit_recovery",
      ].includes(robotState.status) &&
      typeof robotState.observation_age === "number" &&
      Number.isFinite(robotState.observation_age) &&
      robotState.observation_age >= 0 &&
      robotState.observation_age <= project.policy.stale_after &&
      !observationOrFaultReasons.includes(robotState.reason));
  const canResume =
    reportCurrent &&
    latestHealthy &&
    resumeApplicable &&
    !report.recovery.blocked_reason &&
    resumeAllowed &&
    !busy &&
    !!onResume;
  const queueWait =
    report.waiting_classification === "normal_queue" && queueIndex >= 0;
  const trafficReason =
    report.traffic.reason && trafficReasons[report.traffic.reason];
  return (
    <section
      className={`charging-workflow ${!current || operationIssue || explicitBlock || interrupted ? "needs-attention" : ""}`}
      aria-label="충전 실행 상태"
    >
      <h3>충전 실행 상태</h3>
      <p className="charging-workflow-stage">{stageTitle}</p>
      {!reportCurrent && <p>연결과 새 관측을 확인하세요.</p>}
      {(operationIssue || trafficReason || report.reason) &&
        (!queueWait || operationIssue) && (
          <p className="charging-workflow-reason">
            {!current && !operationIssue && "마지막 사유: "}
            {operationIssue?.summary ||
              trafficReason ||
              (report.reason && trafficReasons[report.reason]) ||
              robotReasonLabel(report.reason)}
          </p>
        )}
      {queueWait && current && !operationIssue && (
        <p>앞 로봇의 충전과 통로 비움을 기다립니다.</p>
      )}
      <dl className="kv">
        <dt>{current ? "대상 충전소" : "마지막 대상 충전소"}</dt>
        <dd>{station}</dd>
        {queueIndex >= 0 && (
          <>
            <dt>{current ? "대기열 순번" : "마지막 대기열 순번"}</dt>
            <dd>{queueIndex + 1}번째 · 접점 사용 로봇 제외</dd>
          </>
        )}
        {req && (
          <>
            <dt>
              {!current
                ? "마지막 예약 목표"
                : req.current
                  ? "이번 예약 목표"
                  : "이전 예약 목표"}
            </dt>
            <dd>{quantity(req.target_percent, "%")}</dd>
          </>
        )}
        <dt>누적 충전 입력</dt>
        <dd>{chargedWh(counters?.charging_input_j)}</dd>
        <dt>누적 배터리 저장</dt>
        <dd>{chargedWh(counters?.charging_stored_j)}</dd>
      </dl>
      <p className="muted">
        이번 실행 전체의 관측 누적량입니다. 현재 충전 회차의 양과 다를 수
        있습니다.
      </p>
      {explicitBlock && report.recovery.automatic_yield_supported === false && (
        <p className="muted">
          자동 주차 양보: 미지원. 주변 로봇의 상태와 현재 통로를 확인하세요.
        </p>
      )}
      {resumeApplicable && (
        <div className="charging-workflow-recovery">
          <strong>운영 재개</strong>
          <p>
            {!reportCurrent || !latestHealthy
              ? "새 관측을 받은 뒤 재개 가능 여부를 확인하세요."
              : report.recovery.blocked_reason
                ? (trafficReasons[report.recovery.blocked_reason] ??
                  "복구 조건 확인이 필요합니다.")
                : "원인과 통로를 확인한 뒤 운영 재개를 요청하세요."}
          </p>
          <button
            disabled={!canResume}
            onClick={() => {
              if (canResume) onResume?.();
            }}
            title={
              !reportCurrent || !latestHealthy
                ? "새 관측을 수신한 뒤 사용할 수 있습니다."
                : busy
                  ? "진행 중인 요청의 응답을 기다립니다."
                  : report.recovery.blocked_reason
                    ? (trafficReasons[report.recovery.blocked_reason] ??
                      "복구 조건을 확인하세요.")
                    : !resumeAllowed
                      ? "현재 상태에서 운영 재개를 요청할 수 없습니다."
                      : "실행부가 복구 조건을 확인합니다. 취소한 작업은 다시 생성되지 않습니다."
            }
          >
            {busy ? "요청 처리 중…" : "운영 재개"}
          </button>
          <p className="muted">
            요청 수락은 충전 재개·통로 비움·작업 완료와 다릅니다.
          </p>
        </div>
      )}
      {clearanceKnown && (
        <div className="charging-workflow-task">
          <strong>
            {req?.current && req.request_id !== clearance.request_id
              ? "직전 충전 이후 작업"
              : "충전 이후 작업"}
          </strong>
          <p>
            {(!current || operationIssue) && "이전 작업 기록: "}
            {taskLabels[task.status] ?? "이후 작업 상태 확인 필요"}
          </p>
          {task.task_id && (
            <p>
              {project.tasks.find((entry) => entry.id === task.task_id)?.name ??
                task.task_id}
            </p>
          )}
        </div>
      )}
      <details>
        <summary>충전 단계·예약·복구 기록</summary>
        <dl className="kv">
          <dt>단계 경과 · 보고 시점</dt>
          <dd>{quantity(report.elapsed_seconds, "초")}</dd>
          <dt>현재 통행 공간</dt>
          <dd>
            {!current
              ? "새 보고 확인 필요"
              : explicitBlock
                ? "확보 대기"
                : report.traffic.status === "available"
                  ? "접근 가능 보고"
                  : "판단 정보 확인 필요"}
          </dd>
          {explicitBlock && (
            <>
              <dt>통행 공간 관련 로봇</dt>
              <dd>
                {report.traffic.blocking_robot_ids?.length
                  ? report.traffic.blocking_robot_ids.map(name).join(", ")
                  : "실행부에서 식별하지 않음"}
              </dd>
            </>
          )}
          <dt>충전 필요 기준</dt>
          <dd>{quantity(report.traffic.need_trigger_percent, "%")}</dd>
          <dt>실제 경로 조회 횟수</dt>
          <dd>{quantity(report.traffic.replan_attempts, "회")}</dd>
          <dt>마지막 경로 조회</dt>
          <dd>{quantity(report.traffic.last_replan_at, "초")}</dd>
          <dt>접점 예약 로봇</dt>
          <dd>
            {report.ownership.connector_robot_id
              ? name(report.ownership.connector_robot_id)
              : "없음"}
          </dd>
          <dt>대기 순서</dt>
          <dd>
            {report.ownership.queue_robot_ids.map(name).join(" → ") || "없음"}
          </dd>
          <dt>내 통로 비움 공간</dt>
          <dd>{ownEgress.length ? "예약 유지" : "현재 예약 없음"}</dd>
          <dt>현재 이동 경로 용도</dt>
          <dd>
            {{
              none: "이동 경로 없음",
              charging: "충전 절차",
              task: "배정 작업",
              facility: "시설 이동",
              manual: "수동 이동",
              unknown: "확인 필요",
            }[report.ownership.path_owner] ?? "확인 필요"}
          </dd>
          <dt>명시적 재개 횟수</dt>
          <dd>{quantity(report.recovery.attempts, "회")}</dd>
          {req && (
            <>
              <dt>접점 반납 전 정지 확인</dt>
              <dd>{req.stop_pending ? "확인 대기" : "현재 대기 보고 없음"}</dd>
              <dt>단계 제한 시간</dt>
              <dd>
                {quantity(
                  report.stage === "clearing"
                    ? req.limits?.clearance_timeout_seconds
                    : req.limits?.phase_timeout_seconds,
                  "초",
                )}
              </dd>
              <dt>예약 식별자</dt>
              <dd>{req.request_id}</dd>
            </>
          )}
          <dt>보고 수집 시각</dt>
          <dd>{quantity(report.assessed_at, "초")}</dd>
          <dt>로봇 관측 시각</dt>
          <dd>{quantity(report.observation.sampled_at, "초")}</dd>
        </dl>
        <p className="muted">
          충전 필요 기준과 통행 공간 확보 여부는 별도로 확인합니다. 제한 시간은
          실행부 설정이며 경과 시간만으로 정체를 판단하지 않습니다.
        </p>
      </details>
      <details>
        <summary>최근 통로 비움과 이후 작업</summary>
        <p>
          {clearanceKnown
            ? `${quantity(clearance.completed_at, "초")}에 통로 비움 확인`
            : "통로 비움 완료 보고 없음"}
        </p>
        {clearanceKnown && (
          <>
            <p>{taskLabels[task.status] ?? "이후 작업 상태 확인 필요"}</p>
            {task.task_id && (
              <p>
                {project.tasks.find((entry) => entry.id === task.task_id)
                  ?.name ?? task.task_id}
              </p>
            )}
            <p className="muted">
              최근 완료 요청: {clearance.request_id ?? "식별자 미수신"}. 현재
              예약과 다른 회차일 수 있습니다.
            </p>
          </>
        )}
        <p className="muted">
          접점 반납, 통로 비움, 이후 작업 배정과 완료를 각각 확인합니다.
        </p>
      </details>
      <details>
        <summary>원시 진행 보고</summary>
        <pre>{JSON.stringify(report, null, 2)}</pre>
      </details>
    </section>
  );
}
