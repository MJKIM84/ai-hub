import { useEffect, useRef, useState } from "react";
import type { RunState } from "./types";

/** Wall-clock playback progress, distinct from robot metres/second or CPU throughput. */
export function PlaybackRate({
  state,
  live,
}: {
  state: RunState | null;
  live: boolean;
}) {
  const samples = useRef<{
    run: string;
    points: { wall: number; sim: number }[];
  }>({ run: "", points: [] });
  const [rate, setRate] = useState<number | null>(null);
  useEffect(() => {
    if (!live || !state || state.status !== "running") {
      samples.current.points = [];
      setRate(null);
      return;
    }
    const now = performance.now();
    if (samples.current.run !== state.run_id)
      samples.current = { run: state.run_id, points: [] };
    const points = samples.current.points;
    points.push({ wall: now, sim: state.sim_time });
    while (points.length > 2 && now - points[0].wall > 3000) points.shift();
    const elapsed = now - points[0].wall;
    if (elapsed >= 1000)
      setRate((state.sim_time - points[0].sim) / (elapsed / 1000));
  }, [state?.run_id, state?.sim_time, state?.status, live]);
  if (rate === null) return null;
  return (
    <small
      className="muted"
      title="최근 수신한 시뮬레이션 시간 ÷ 실제 경과 시간. 로봇 주행 속도(m/s)와 별개입니다."
    >
      {rate < (state?.speed ?? 1) * 0.8 ? "계산 지연 · " : ""}실제{" "}
      {rate.toFixed(2)}×
    </small>
  );
}
