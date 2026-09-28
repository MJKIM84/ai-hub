/** @jsxImportSource react */
import type { ConsumptionMeterReport } from "./types";
import { consumptionMeterView, consumptionNumber } from "./consumptionMeter";

const labels = {
  waiting: "소비 관측 수신 대기",
  ready: "수신한 관측 구간의 평균 소비",
  first: "첫 관측 수신 · 평균 계산에 다음 관측 필요",
  stale: "이전 관측 · 새 소비 관측 필요",
  invalid: "관측 이상 · 현재 소비 확인 불가",
  offline: "연결 확인 필요 · 현재 소비 확인 불가",
  mismatch: "현재 실행의 소비 관측 수신 대기",
};
const reasons: Record<string, string> = {
  missing_observation: "로봇 관측이 없어 새 소비량을 확인할 수 없습니다.",
  missing_meter: "수신한 관측에 소비 계측값이 없습니다.",
  meter_identity_mismatch: "계측값의 실행 또는 로봇 정보가 일치하지 않습니다.",
  invalid_meter_time: "계측 시각과 관측 수신 순서를 확인해야 합니다.",
  invalid_meter_counter: "소비 계측값에 유효하지 않은 수치가 있습니다.",
  inconsistent_meter_counter: "요구·공급·충전 누적량이 서로 맞지 않습니다.",
  reordered_or_changed_meter: "계측 순서나 같은 시각의 보고가 달라졌습니다.",
  decreasing_meter_counter: "누적 계측값이 이전 관측보다 감소했습니다.",
  invalid_observation_time: "관측 시각을 확인해야 합니다.",
  invalid_report_time: "소비 보고의 실행 시각을 확인해야 합니다.",
};

export default function EnergyConsumptionPanel({
  report,
  runId,
  robotId,
  now,
  live,
  staleAfter,
}: {
  report?: ConsumptionMeterReport | null;
  runId?: string;
  robotId: string;
  now: number;
  live: boolean;
  staleAfter?: number;
}) {
  const view = consumptionMeterView(report, {
    runId,
    robotId,
    now,
    live,
    staleAfter,
  });
  const { accepted, interval } = view;
  const counters = accepted?.counters;
  const historical = !["ready", "first"].includes(view.mode);
  const unserved = counters?.unserved_j ?? 0;
  const wh = (joules: number | undefined) =>
    consumptionNumber(joules == null ? null : joules / 3600, "Wh");
  return (
    <section
      className={`energy-consumption ${historical || unserved > 0 ? "needs-attention" : ""}`}
      aria-label="관측 소비량"
    >
      <h3>관측 소비량</h3>
      <p className="energy-consumption-status">{labels[view.mode]}</p>
      {view.mode === "invalid" && (
        <p>
          {(report?.reason && reasons[report.reason]) ||
            "새 소비 관측의 시각과 수치를 확인해야 합니다."}
        </p>
      )}
      <dl className="kv">
        <dt>평균 소비전력</dt>
        <dd>{consumptionNumber(view.averageW, "W", 1)}</dd>
        <dt>{historical ? "누적 소비 · 이전 관측" : "누적 소비"}</dt>
        <dd>{wh(counters?.drawn_j)}</dd>
        <dt>{historical ? "마지막 수신 구간" : "평균 계산 구간"}</dt>
        <dd>
          {interval
            ? `${consumptionNumber(interval.start_at, "s")} – ${consumptionNumber(interval.end_at, "s")}`
            : "구간 확인 불가"}
        </dd>
        <dt>관측 경과</dt>
        <dd>{consumptionNumber(view.age, "s")}</dd>
      </dl>
      {unserved > 0 && (
        <p className="energy-consumption-warning">
          {historical ? "이전 관측에 " : ""}배터리가 공급하지 못한 에너지{" "}
          {consumptionNumber(unserved, "J")}. 실제 소비와 요구량이 다릅니다.
        </p>
      )}
      <details>
        <summary>계측 범위와 예측 설정</summary>
        <p className="muted">
          연구용 소비 계측입니다. 관측은 통신 지연·누락의 영향을 받습니다.
          평균은 위 구간에서 배터리가 공급한 에너지로 계산하며, 순간 전력이나
          앞으로의 소비 상한을 뜻하지 않습니다.
        </p>
        {historical && accepted && (
          <p className="muted">
            아래 누적값은 마지막으로 확인한 관측입니다. 현재 값으로 사용하지
            마세요.
          </p>
        )}
        <dl className="kv">
          <dt>누적 요구 에너지</dt>
          <dd>{wh(counters?.demand_j)}</dd>
          <dt>누적 미공급 에너지</dt>
          <dd>{wh(counters?.unserved_j)}</dd>
          <dt>누적 충전 입력</dt>
          <dd>{wh(counters?.charging_input_j)}</dd>
          <dt>누적 충전 저장</dt>
          <dd>{wh(counters?.charging_stored_j)}</dd>
          <dt>관측 시각</dt>
          <dd>{consumptionNumber(accepted?.sampled_at, "s")}</dd>
          <dt>수신 시각</dt>
          <dd>{consumptionNumber(accepted?.received_at, "s")}</dd>
          <dt>예측용 설정 소비전력</dt>
          <dd>{consumptionNumber(view.configuredW, "W", 1)}</dd>
        </dl>
        <p className="muted">
          누적값은 이번 실행 시작부터 관측 시각까지의 값입니다. 충전 입력과
          소비를 별도로 기록하므로 배터리 잔량의 변화와 다를 수 있습니다.
          시각·경과 시간은 실행 시계 기준입니다.
        </p>
        <p className="muted">
          예측용 설정은 앞으로의 작업·충전 이동에 사용하는 값입니다. 관측
          소비량으로 자동 보정하지 않습니다.
        </p>
      </details>
    </section>
  );
}
