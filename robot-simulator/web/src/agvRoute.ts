import type { Pose } from "./types";

// Configuration guidance only. No obstacle, route execution, or physics verdict.
const finite = (value: unknown): value is number =>
  typeof value === "number" && Number.isFinite(value);
const sameXY = (a: Pose, b: Pose) =>
  finite(a.x) &&
  finite(a.y) &&
  finite(b.x) &&
  finite(b.y) &&
  Math.hypot(a.x - b.x, a.y - b.y) <= 1e-6;

export function agvRouteGuidance(points: readonly Pose[]) {
  const closed =
    points.length > 1 && sameXY(points[0], points[points.length - 1]);
  const issues: string[] = [];
  if (points.length < 2)
    issues.push("경유점을 2개 이상 입력하세요. 입력한 순서가 진행 방향입니다.");
  points.forEach((point, index) => {
    if (![point.x, point.y, point.z, point.yaw].every(finite))
      issues.push(
        `${index + 1}번 점의 좌표와 방향을 유한한 숫자로 입력하세요.`,
      );
    else if (point.z !== 0)
      issues.push(
        `${index + 1}번 점의 Z는 ${point.z}m입니다. 같은 층 경로의 Z를 0으로 맞추세요.`,
      );
    for (let earlier = 0; earlier < index; earlier++) {
      if (!sameXY(points[earlier], point)) continue;
      if (closed && earlier === 0 && index === points.length - 1 && index > 1)
        continue;
      issues.push(
        `${earlier + 1}번과 ${index + 1}번 점의 XY가 겹칩니다. 첫 점의 마지막 반복 외에는 중복 점을 수정하거나 제거하세요.`,
      );
    }
  });
  if (closed && points.length < 4)
    issues.push(
      "순환 경로는 서로 다른 점 3개 이상을 거친 뒤 첫 점으로 연결하세요.",
    );
  return { closed, issues };
}

export type AgvRouteEdit =
  | { kind: "point"; index: number; axis: "x" | "y" | "yaw"; value: number }
  | { kind: "add"; placement: Pose }
  | { kind: "first-at-placement"; placement: Pose }
  | { kind: "move"; index: number; direction: -1 | 1 }
  | { kind: "remove"; index: number }
  | { kind: "close" }
  | { kind: "zero-height" };

export function editAgvRoute(
  points: readonly Pose[],
  edit: AgvRouteEdit,
): Pose[] {
  const next = points.map((point) => ({ ...point }));
  const closed = agvRouteGuidance(points).closed;
  if (edit.kind === "point") {
    if (!finite(edit.value)) throw new Error("유한한 숫자를 입력하세요.");
    if (next[edit.index]) next[edit.index][edit.axis] = edit.value;
  } else if (edit.kind === "add") {
    const after = next[closed ? next.length - 2 : next.length - 1];
    const point = after
      ? {
          x: after.x + Math.cos(after.yaw),
          y: after.y + Math.sin(after.yaw),
          z: 0,
          yaw: after.yaw,
        }
      : { ...edit.placement, z: 0 };
    next.splice(closed ? next.length - 1 : next.length, 0, point);
  } else if (edit.kind === "first-at-placement") {
    const point = { ...edit.placement, z: 0 };
    if (next.length) next[0] = point;
    else next.push(point);
    if (closed) next[next.length - 1] = { ...point };
  } else if (edit.kind === "move") {
    const to = edit.index + edit.direction;
    if (next[edit.index] && next[to])
      [next[edit.index], next[to]] = [next[to], next[edit.index]];
  } else if (edit.kind === "remove") {
    if (edit.index >= 0 && edit.index < next.length) next.splice(edit.index, 1);
  } else if (edit.kind === "close") {
    if (!closed && next.length >= 3) next.push({ ...next[0] });
  } else {
    next.forEach((point) => {
      point.z = 0;
    });
  }
  return next;
}
