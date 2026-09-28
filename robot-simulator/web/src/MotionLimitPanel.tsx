/** @jsxImportSource react */
import type { MotionLimitReport, Project } from "./types";

const nonnegative = (value: unknown): value is number =>
  typeof value === "number" && Number.isFinite(value) && value >= 0;
const number = (value: number | null | undefined, unit: string) => {
  if (!nonnegative(value)) return "확인 불가";
  if (value > 0 && value < 0.001) return `0.001 ${unit} 미만`;
  return `${value.toLocaleString("ko-KR", { maximumFractionDigits: 3 })} ${unit}`;
};
const reasons: Record<string, string> = {
  missing_or_stale_motion_observation: "새 위치 관측이 필요합니다.",
  invalid_motion_observation_or_configuration:
    "위치 관측 또는 이동 제한 설정을 확인해야 합니다.",
};

export default function MotionLimitPanel({
  report,
  project,
  now,
  live,
}: {
  report?: MotionLimitReport | null;
  // App supplies the current run's project, never an unapplied local draft.
  project: Project | null;
  now: number;
  live: boolean;
}) {
  const supported = report?.version === "observed-motion-limit-v1";
  const validTimes =
    supported &&
    nonnegative(now) &&
    nonnegative(report.sampled_at) &&
    nonnegative(report.assessed_at) &&
    report.sampled_at <= report.assessed_at &&
    report.assessed_at <= now;
  const freshnessKnown = nonnegative(project?.policy.stale_after);
  const stale =
    validTimes &&
    freshnessKnown &&
    now - report.sampled_at! > project!.policy.stale_after;
  const known =
    supported &&
    report.status === "known" &&
    nonnegative(report.limit_m_s) &&
    [
      report.model_limit_m_s,
      report.robot_limit_m_s,
      report.policy_limit_m_s,
    ].every(nonnegative) &&
    report.limit_m_s <=
      Math.min(
        report.model_limit_m_s,
        report.robot_limit_m_s,
        report.policy_limit_m_s,
      ) +
        1e-9;
  const current = live && validTimes && freshnessKnown && !stale && known;
  const previous = supported && (!live || stale);
  const zoneNames =
    known && validTimes && project
      ? report.zone_ids.map(
          (id) =>
            project.environment.elements.find(
              (element) => element.id === id && element.kind === "speed_zone",
            )?.name ?? id,
        )
      : null;
  return (
    <div className="motion-limit">
      <dl className="kv">
        <dt>관측 위치의 이동 상한</dt>
        <dd>{number(current ? report.limit_m_s : null, "m/s")}</dd>
      </dl>
      {!current && (
        <p className="motion-limit-status">
          {!live
            ? "연결 확인 필요 · 현재 상한 확인 불가"
            : !report
              ? "이동 상한 관측 수신 대기"
              : !freshnessKnown
                ? "현재 실행의 적용 기준 확인 대기"
                : previous
                  ? "이전 관측 · 새 위치 관측 필요"
                  : (report.reason && reasons[report.reason]) ||
                    "현재 위치의 이동 상한을 판단할 관측이 필요합니다."}
        </p>
      )}
      <details>
        <summary>이동 상한의 적용 기준</summary>
        {previous && (
          <p className="muted">아래는 마지막으로 수신한 보고의 기준입니다.</p>
        )}
        <dl className="kv">
          <dt>로봇 설정</dt>
          <dd>{number(supported ? report.robot_limit_m_s : null, "m/s")}</dd>
          <dt>운영 정책</dt>
          <dd>{number(supported ? report.policy_limit_m_s : null, "m/s")}</dd>
          <dt>모델 상한</dt>
          <dd>{number(supported ? report.model_limit_m_s : null, "m/s")}</dd>
          <dt>적용 구역</dt>
          <dd>
            {zoneNames
              ? zoneNames.length
                ? zoneNames.join(" · ")
                : "해당 위치의 제한 구역 없음"
              : "확인 불가"}
          </dd>
          <dt>관측 / 판단 시각</dt>
          <dd>
            {validTimes
              ? `${number(report.sampled_at, "s")} / ${number(report.assessed_at, "s")}`
              : "확인 불가"}
          </dd>
        </dl>
        <p className="muted">
          로봇·정책·모델·구역 제한 중 가장 낮은 값을 앞뒤 이동 명령에
          적용합니다. 로봇 중심의 관측 위치에 적용합니다. 실제 속도는
          지연·관성의 영향을 받으며, 도킹 등 동작별 제한이 더 낮을 수 있습니다.
        </p>
      </details>
    </div>
  );
}
