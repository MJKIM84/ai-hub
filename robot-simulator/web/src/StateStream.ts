import type { RunState } from "./types";

export type StateFrame = { full: boolean; base_sequence: number | null; state: Partial<RunState> };

export function mergeStateFrame(previous: RunState | null, frame: StateFrame): RunState {
  const patch = frame.state;
  if (!Number.isSafeInteger(patch.state_sequence))
    throw new Error("상태 순서가 없습니다.");
  if (!frame.full && (!previous || previous.state_sequence !== frame.base_sequence))
    throw new Error("상태 기준이 달라 다시 연결합니다.");
  const next = frame.full ? patch : { ...previous, ...patch };
  if (!next.state_source || !next.run_id || !Array.isArray(next.geoms) || !Array.isArray(next.robots) ||
      !Number.isFinite(next.sim_time) || !next.status)
    throw new Error("불완전한 실행 상태입니다.");
  return next as RunState;
}

export function isNewerState(current: RunState | null, next: RunState) {
  return !current || !next.state_source || current.state_source !== next.state_source ||
    next.state_sequence! > (current.state_sequence ?? -1);
}

/** One read-only connection. Unsupported/disconnected servers retain GET fallback. */
export function openStateStream(onState: (state: RunState) => void) {
  const source = new EventSource("/api/state/stream");
  let previous: RunState | null = null;
  let receivedAt = 0;
  let closed = false;
  const openedAt = performance.now();
  source.onopen = () => { previous = null; };
  source.onmessage = (event) => {
    if (closed) return;
    try {
      previous = mergeStateFrame(previous, JSON.parse(event.data));
      receivedAt = performance.now();
      onState(previous);
    } catch {
      closed = true;
      source.close();
    }
  };
  source.onerror = () => { receivedAt = 0; };
  return {
    healthy: () => !closed && receivedAt > 0 && performance.now()-receivedAt < 2000,
    expired: () => closed || performance.now()-(receivedAt || openedAt) > 5000,
    close: () => { closed = true; source.close(); },
  };
}
