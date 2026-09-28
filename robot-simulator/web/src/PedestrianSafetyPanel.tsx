/** @jsxImportSource react */
import type { Project } from "./types";
import { robotReasonLabel } from "./uiMessages";

export interface PedestrianAvoidanceReport {
  version: string;
  mode: string;
  reason: string;
  assessed_at: number;
  sampled_at?: number | null;
  desired_clearance_m: number;
  blocked_since: number | null;
  blocked_seconds: number;
  sensor_model?: string;
  observed_min_clearance_m?: number | null;
  effective_stop_distance_m?: number | null;
  visible_person_ids?: string[];
  person_id?: string;
  predicted_min_clearance_m?: number | null;
}

const finite = (value: unknown): value is number =>
  typeof value === "number" && Number.isFinite(value);
const nonnegative = (value: unknown): value is number =>
  finite(value) && value >= 0;
const object = (value: unknown): Record<string, unknown> | null =>
  value !== null && typeof value === "object" && !Array.isArray(value)
    ? (value as Record<string, unknown>)
    : null;
const quantity = (value: unknown, unit: string) => {
  if (!finite(value)) return "확인 불가";
  if (value > 0 && value < 0.001) return `0.001 ${unit} 미만`;
  if (value < 0 && value > -0.001) return `−0.001 ${unit} 초과 · 음수`;
  return `${value.toLocaleString("ko-KR", { maximumFractionDigits: 3 })} ${unit}`;
};
const modes: Record<string, string> = {
  clear: "관측 기준 · 통행 방해 없음",
  resuming: "관측 기준 · 경로 재개 판단",
  slowing: "사람 근처 · 이동 명령 감속",
  yielding: "사람 통행 대기 · 정지 명령",
  waiting: "통로 확보 대기 · 정지 명령",
  detouring: "우회 경로 준비 · 아직 우회 완료 아님",
  detour_align: "이동을 멈추고 우회 방향 정렬",
  observation_hold: "새 사람 관측 대기 · 정지 명령",
  blocked_failed: "통로 차단 시간 초과 · 운영 재개 확인 필요",
};

export default function PedestrianSafetyPanel({
  report,
  metrics,
  robotId,
  project,
  now,
  live,
  robotStatus,
  robotReason,
  operatorHold,
}: {
  report?: PedestrianAvoidanceReport | null;
  metrics?: unknown;
  robotId: string;
  // Both project and metrics must belong to the current run, not an editor draft.
  project: Project | null;
  now: number;
  live: boolean;
  robotStatus?: string;
  robotReason?: string;
  operatorHold?: boolean;
}) {
  const desired = project?.policy.pedestrian_avoidance?.desired_clearance_m;
  const configured = nonnegative(desired);
  const staleAfter = project?.policy.stale_after;
  const freshnessKnown = nonnegative(staleAfter) && nonnegative(now);
  const supported = report?.version === "observed-pedestrian-avoidance-v1";
  const assessedFresh =
    supported &&
    freshnessKnown &&
    nonnegative(report.assessed_at) &&
    report.assessed_at <= now &&
    now - report.assessed_at <= staleAfter;
  const sampledFresh =
    assessedFresh &&
    nonnegative(report.sampled_at) &&
    report.sampled_at <= report.assessed_at &&
    now - report.sampled_at <= staleAfter;
  const disconnected =
    !live || ["disconnected", "stale", "unknown"].includes(robotStatus ?? "");
  const current =
    !disconnected &&
    configured &&
    assessedFresh &&
    nonnegative(report.desired_clearance_m) &&
    Math.abs(report.desired_clearance_m - desired) <= 1e-9 &&
    Object.hasOwn(modes, report.mode) &&
    (sampledFresh ||
      ["observation_hold", "blocked_failed"].includes(report.mode));
  const distancesCurrent =
    current &&
    sampledFresh &&
    !["observation_hold", "blocked_failed"].includes(report.mode);
  const visible =
    distancesCurrent &&
    Array.isArray(report.visible_person_ids) &&
    report.visible_person_ids.every((id) => typeof id === "string")
      ? report.visible_person_ids
      : null;
  const observed = distancesCurrent ? report.observed_min_clearance_m : null;
  const evaluation = object(metrics);
  const minima = object(evaluation?.actual_min_clearance_m);
  const actualKnown =
    configured &&
    nonnegative(evaluation?.desired_clearance_m) &&
    Math.abs(evaluation.desired_clearance_m - desired) <= 1e-9 &&
    minima !== null &&
    Object.hasOwn(minima, robotId) &&
    finite(minima[robotId]);
  const actual = actualKnown ? (minima![robotId] as number) : null;
  const belowDesired = actual !== null && configured && actual < desired;
  const recovery =
    robotStatus === "recovery_required" ||
    (current && report.mode === "blocked_failed");
  const otherRecovery = ["recovering", "transit_recovery"].includes(
    robotStatus ?? "",
  );
  const headline = disconnected
    ? "연결 확인 필요 · 현재 회피 상태 확인 불가"
    : robotStatus === "fault"
      ? "로봇 고장 · 회피 진행 확인 보류"
      : recovery
        ? "복구 대기 · 통로와 로봇 상태 확인 필요"
        : otherRecovery
          ? `${robotStatus === "recovering" ? "물품" : "층간 이동"} 복구 중 · 회피 보고 참고`
          : operatorHold
            ? "운영자 정지 유지 · 회피 보고 참고"
            : !project
              ? "현재 실행의 적용 기준 확인 대기"
              : !configured
                ? "보행자 회피 설정 없음"
                : current
                  ? modes[report.mode]
                  : report
                    ? "이전 또는 확인할 수 없는 보고 · 새 관측 필요"
                    : "보행자 회피 보고 수신 대기";
  const blockedSeconds =
    current && nonnegative(report.blocked_seconds)
      ? report.blocked_seconds
      : null;
  const primaryReason =
    live &&
    (recovery || otherRecovery || robotStatus === "fault" || operatorHold)
      ? robotReasonLabel(robotReason)
      : null;
  const personName =
    current && report.person_id
      ? (project?.people.find((person) => person.id === report.person_id)
          ?.name ?? report.person_id)
      : null;
  return (
    <div className="motion-limit">
      <p className="motion-limit-status">{headline}</p>
      {primaryReason && <p>{primaryReason}</p>}
      {current && report.reason && report.reason !== primaryReason && (
        <p>회피 보고: {report.reason}</p>
      )}
      <dl className="kv">
        <dt>설정한 목표 간격</dt>
        <dd>{quantity(configured ? desired : null, "m")}</dd>
        <dt>최근 관측의 최소 간격</dt>
        <dd>
          {finite(observed)
            ? quantity(observed, "m")
            : visible?.length === 0
              ? "관측된 사람 없음"
              : "확인 불가"}
        </dd>
        <dt>실행 중 실제 최소 간격</dt>
        <dd>
          {actual === null ? "기록 없음" : quantity(actual, "m")}
          {!live && actual !== null ? " · 마지막 수신 기록" : ""}
        </dd>
        <dt>차단 상태 지속 시간</dt>
        <dd>{quantity(blockedSeconds, "s")}</dd>
      </dl>
      {belowDesired && (
        <p className="motion-limit-status">
          목표 간격 미달 기록이 있습니다. 현재 거리나 충돌 여부를 뜻하지
          않습니다.
        </p>
      )}
      {recovery && live && (
        <p>
          통로와 목적지, 로봇 상태를 확인한 뒤 운영 재개를 요청하세요. 사람이
          사라져도 자동 복구 완료로 판단하지 않습니다. 지속 시간에는 복구 대기가
          포함될 수 있습니다.
        </p>
      )}
      <details>
        <summary>관측과 평가 기준</summary>
        <dl className="kv">
          <dt>관측된 사람</dt>
          <dd>{visible ? `${visible.length}명` : "확인 불가"}</dd>
          <dt>주요 회피 대상</dt>
          <dd>{personName ?? "현재 대상 확인 불가"}</dd>
          <dt>예측 최소 간격 · 최대 2초</dt>
          <dd>
            {quantity(
              distancesCurrent ? report.predicted_min_clearance_m : null,
              "m",
            )}
          </dd>
          <dt>현재 정지 판단 간격</dt>
          <dd>
            {quantity(
              distancesCurrent && nonnegative(report.effective_stop_distance_m)
                ? report.effective_stop_distance_m
                : null,
              "m",
            )}
          </dd>
          <dt>관측 / 판단 시각</dt>
          <dd>
            {supported
              ? `${quantity(nonnegative(report.sampled_at) ? report.sampled_at : null, "s")} / ${quantity(nonnegative(report.assessed_at) ? report.assessed_at : null, "s")}`
              : "확인 불가"}
          </dd>
        </dl>
        {!current && supported && (
          <p className="muted">
            시각은 마지막 보고의 기록이며 현재 회피 진행을 뜻하지 않습니다.
          </p>
        )}
        <p className="muted">
          관측 간격은 지연·잡음·가림의 영향을 받습니다. 관측된 사람이 없어도
          주변에 사람이 없다는 뜻은 아닙니다. 정지 판단 간격은 관측 속도와
          지연을 반영하며 실제 정지를 보장하지 않습니다.
        </p>
        <p className="muted">
          실제 최소 간격은 이 실행에서 같은 층의 로봇 외접 원과 사람 몸통 원
          사이 거리를 누적한 평가 기록입니다. 제어 입력으로 사용하지 않습니다.
          음수는 이 원들의 겹침이며, 실제 접촉 여부는 사건 기록에서 확인하세요.
        </p>
      </details>
    </div>
  );
}
