import * as THREE from "three";
import { perspectiveBoxDistance } from "./spatial";
import type { Floor, Pose } from "./types";

export type CameraSnapshot = {
  position: [number, number, number];
  target: [number, number, number];
  up: [number, number, number];
  floorId: string;
};
export type CameraTravel = {
  from: CameraSnapshot;
  to: CameraSnapshot;
  started: number;
  duration: number;
};
export function copyView(view: CameraSnapshot): CameraSnapshot {
  return {
    ...view,
    position: [...view.position],
    target: [...view.target],
    up: [...view.up],
  };
}
export function sampleTravel(
  travel: CameraTravel,
  now: number,
): { view: CameraSnapshot; done: boolean } {
  const progress =
    travel.duration <= 0
      ? 1
      : Math.max(0, Math.min(1, (now - travel.started) / travel.duration));
  const t = progress * progress * (3 - 2 * progress);
  const lerp = (a: number[], b: number[]) =>
    a.map((value, i) => value + (b[i] - value) * t) as [number, number, number];
  return {
    view: {
      floorId: travel.to.floorId,
      position: lerp(travel.from.position, travel.to.position),
      target: lerp(travel.from.target, travel.to.target),
      up: lerp(travel.from.up, travel.to.up),
    },
    done: progress === 1,
  };
}
export function segmentHitsBox(
  from: THREE.Vector3,
  to: THREE.Vector3,
  box: THREE.Box3,
): boolean {
  if (box.isEmpty()) return false;
  if (box.containsPoint(from) || box.containsPoint(to)) return true;
  const delta = to.clone().sub(from),
    length = delta.length();
  if (!length) return false;
  const hit = new THREE.Ray(
    from.clone(),
    delta.divideScalar(length),
  ).intersectBox(box, new THREE.Vector3());
  return !!hit && hit.distanceTo(from) < length;
}
/** World-space, received mesh bounds only. No robot state or command is modified. */
export function robotFocusView(
  bounds: THREE.Box3,
  yaw: number,
  floorId: string,
  fov: number,
  aspect: number,
  near: number,
  occluders: THREE.Box3[] = [],
): CameraSnapshot | null {
  if (
    bounds.isEmpty() ||
    ![
      ...bounds.min.toArray(),
      ...bounds.max.toArray(),
      yaw,
      fov,
      aspect,
      near,
    ].every(Number.isFinite) ||
    aspect <= 0 ||
    fov <= 0 ||
    fov >= 180 ||
    near <= 0
  )
    return null;
  const target = bounds.getCenter(new THREE.Vector3()),
    half = bounds.getSize(new THREE.Vector3()).multiplyScalar(0.5);
  let best: { position: THREE.Vector3; score: number } | undefined;
  // +X is the robot's forward axis. Prefer a front quarter view, then test
  // the other front quarter / a higher view against received wall geometry.
  for (const [index, [angle, rise]] of [
    [-Math.PI / 4, 0.7],
    [Math.PI / 4, 0.7],
    [-Math.PI / 3, 1.2],
    [Math.PI / 3, 1.2],
    [0, 1.4],
  ].entries()) {
    const direction = new THREE.Vector3(
      Math.cos(yaw + angle),
      Math.sin(yaw + angle),
      rise,
    ).normalize();
    const distance = Math.max(
      0.65,
      perspectiveBoxDistance(half, direction, fov, aspect, near, 1.65),
    );
    const position = target.clone().addScaledVector(direction, distance);
    const score =
      occluders.reduce(
        (total, box) =>
          total +
          (box.containsPoint(position) ? 10 : 0) +
          (segmentHitsBox(position, target, box) ? 1 : 0),
        0,
      ) *
        100 +
      index;
    if (!best || score < best.score) best = { position, score };
  }
  return {
    position: best!.position.toArray() as [number, number, number],
    target: target.toArray() as [number, number, number],
    up: [0, 0, 1],
    floorId,
  };
}

/** A local cutaway around a lift, with both real floor elevations in frame. */
export function floorPairView(
  source: Floor,
  destination: Floor,
  anchor: Pick<Pose, "x" | "y">,
  robot: Pick<Pose, "x" | "y" | "z"> | null,
  fov: number,
  aspect: number,
  near: number,
): CameraSnapshot {
  const centerX = anchor.x,
    centerY = anchor.y;
  const spanX = Math.min(
    4,
    Math.max(2.8, Math.min(source.width, destination.width) / 2),
  );
  const spanY = Math.min(
    4,
    Math.max(2.8, Math.min(source.depth, destination.depth) / 2),
  );
  const bounds = new THREE.Box3(
    new THREE.Vector3(
      Math.max(0, centerX - spanX),
      Math.max(0, centerY - spanY),
      Math.min(source.elevation, destination.elevation) - 0.15,
    ),
    new THREE.Vector3(
      Math.min(Math.max(source.width, destination.width), centerX + spanX),
      Math.min(Math.max(source.depth, destination.depth), centerY + spanY),
      Math.max(source.elevation, destination.elevation) + 2.5,
    ),
  );
  if (robot)
    bounds.expandByPoint(new THREE.Vector3(robot.x, robot.y, robot.z + 0.45));
  const target = bounds.getCenter(new THREE.Vector3());
  const direction = new THREE.Vector3(0.8, -1.05, 0.65).normalize();
  const distance = Math.max(
    6,
    perspectiveBoxDistance(
      bounds.getSize(new THREE.Vector3()).multiplyScalar(0.5),
      direction,
      fov,
      aspect,
      near,
      1.15,
    ),
  );
  return {
    position: target.clone().addScaledVector(direction, distance).toArray() as [
      number,
      number,
      number,
    ],
    target: target.toArray() as [number, number, number],
    up: [0, 0, 1],
    floorId: source.id,
  };
}
export type ClickGesture = {
  x: number;
  y: number;
  maxExcursion: number;
  started: number;
  pointerId: number;
};
export function advanceClick(
  gesture: ClickGesture,
  x: number,
  y: number,
): ClickGesture {
  return {
    ...gesture,
    maxExcursion: Math.max(
      gesture.maxExcursion,
      Math.hypot(x - gesture.x, y - gesture.y),
    ),
  };
}
export function isClick(
  gesture: ClickGesture,
  pointerId: number,
  now: number,
): boolean {
  return (
    pointerId === gesture.pointerId &&
    gesture.maxExcursion <= 5 &&
    now - gesture.started <= 700 &&
    now >= gesture.started
  );
}
