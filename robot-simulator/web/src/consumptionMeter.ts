import type { ConsumptionMeterReport } from "./types";

export type ConsumptionMeterMode =
  "waiting" | "ready" | "first" | "stale" | "invalid" | "offline" | "mismatch";

const nonnegative = (value: unknown): value is number =>
  typeof value === "number" && Number.isFinite(value) && value >= 0;

export function consumptionMeterView(
  report: ConsumptionMeterReport | null | undefined,
  context: {
    runId?: string;
    robotId: string;
    now: number;
    live: boolean;
    staleAfter?: number;
  },
): {
  mode: ConsumptionMeterMode;
  accepted: ConsumptionMeterReport | null;
  age: number | null;
  interval: ConsumptionMeterReport["interval"];
  averageW: number | null;
  configuredW: number | null;
} {
  let configuredW: number | null = null;
  const empty = (mode: ConsumptionMeterMode) => ({
    mode,
    accepted: null,
    age: null,
    interval: null,
    averageW: null,
    configuredW,
  });
  if (!report) return empty(context.live ? "waiting" : "offline");
  if (
    !context.runId ||
    report.run_id !== context.runId ||
    report.robot_id !== context.robotId
  )
    return empty("mismatch");
  if (report.version !== "research-consumption-v1") return empty("invalid");
  configuredW = nonnegative(report.configured_drive_power_w)
    ? report.configured_drive_power_w
    : null;
  if (!report.counters)
    return empty(
      !context.live
        ? "offline"
        : report.status === "waiting"
          ? "waiting"
          : "invalid",
    );
  if (
    ![
      report.counters.demand_j,
      report.counters.drawn_j,
      report.counters.unserved_j,
      report.counters.charging_input_j,
      report.counters.charging_stored_j,
    ].every(nonnegative) ||
    !nonnegative(context.now) ||
    !nonnegative(report.sampled_at) ||
    !nonnegative(report.received_at) ||
    report.sampled_at > report.received_at ||
    report.received_at > context.now
  )
    return empty("invalid");

  const age = context.now - report.sampled_at;
  const candidate = report.interval;
  const interval =
    candidate &&
    [
      candidate.start_at,
      candidate.end_at,
      candidate.seconds,
      candidate.demand_w,
      candidate.drawn_w,
    ].every(nonnegative) &&
    candidate.seconds > 0 &&
    candidate.start_at < candidate.end_at &&
    Math.abs(candidate.end_at - report.sampled_at) < 1e-6 &&
    Math.abs(candidate.end_at - candidate.start_at - candidate.seconds) < 1e-6
      ? candidate
      : null;
  const mode: ConsumptionMeterMode = !context.live
    ? "offline"
    : report.status === "invalid" ||
        (candidate != null && interval == null) ||
        !["ready", "stale"].includes(report.status)
      ? "invalid"
      : report.status === "stale" ||
          !nonnegative(context.staleAfter) ||
          age > context.staleAfter
        ? "stale"
        : interval
          ? "ready"
          : "first";
  return {
    mode,
    accepted: report,
    age,
    interval: report.status === "invalid" ? null : interval,
    averageW: mode === "ready" ? interval!.drawn_w : null,
    configuredW,
  };
}

export function consumptionNumber(
  value: number | null | undefined,
  unit: string,
  digits = 3,
) {
  if (!nonnegative(value)) return "확인 불가";
  const minimum = 10 ** -digits;
  if (value > 0 && value < minimum) return `${minimum} ${unit} 미만`;
  return `${value.toLocaleString("ko-KR", { maximumFractionDigits: digits })} ${unit}`;
}
