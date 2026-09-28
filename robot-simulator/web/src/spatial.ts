/**
 * Route a physical base/support height to the highest landing already reached.
 * The 6 cm landing tolerance matches the physical view; midpoint travel stays
 * on the lower floor in either direction. Callers convert geometry centers to
 * the entity's base or supporting surface before calling this function.
 */
export function floorAtHeight(
  floors: readonly { id: string; elevation: number }[],
  z: number | null | undefined,
  fallback?: string,
): string | undefined {
  const ordered = floors
    .filter((floor) => Number.isFinite(floor.elevation))
    .sort((a, b) => b.elevation - a.elevation);
  const lowest = ordered.at(-1)?.id;
  if (z == null || !Number.isFinite(z)) return fallback ?? lowest;
  return (
    ordered.find((floor) => z >= floor.elevation - 0.06)?.id ??
    lowest ??
    fallback
  );
}

/** Convert a known entity anchor's world-space center to its physical base. */
export function floorAtGeometryBase(
  floors: readonly { id: string; elevation: number }[],
  geometry: { position: readonly number[] } | undefined,
  centerOffset: number,
  fallback?: string,
): string | undefined {
  const center = geometry?.position[2];
  return floorAtHeight(
    floors,
    center == null ? undefined : center - centerOffset,
    fallback,
  );
}

type Vector3Like = { x: number; y: number; z: number };

/** Fit a Y-up plan into the viewport area left unobstructed by its overlays. */
export function fitPlanBounds(
  bounds: { left: number; right: number; bottom: number; top: number },
  viewport: { width: number; height: number },
  insets: { left: number; right: number; top: number; bottom: number },
): { x: number; y: number; height: number } {
  const availableWidth = Math.max(
    1,
    viewport.width - insets.left - insets.right,
  );
  const availableHeight = Math.max(
    1,
    viewport.height - insets.top - insets.bottom,
  );
  const scale = Math.min(
    availableWidth / Math.max(0.001, bounds.right - bounds.left),
    availableHeight / Math.max(0.001, bounds.top - bounds.bottom),
  );
  return {
    x:
      (bounds.left + bounds.right) / 2 +
      (insets.right - insets.left) / (2 * scale),
    y:
      (bounds.bottom + bounds.top) / 2 +
      (insets.top - insets.bottom) / (2 * scale),
    height: viewport.height / scale,
  };
}

/** Distance from an AABB center that fits all eight corners in a Z-up camera. */
export function perspectiveBoxDistance(
  halfSize: Vector3Like,
  cameraDirection: Vector3Like,
  verticalFovDegrees: number,
  aspect: number,
  near = 0.02,
  padding = 1.1,
): number {
  const length = Math.hypot(
    cameraDirection.x,
    cameraDirection.y,
    cameraDirection.z,
  );
  const back = length
    ? {
        x: cameraDirection.x / length,
        y: cameraDirection.y / length,
        z: cameraDirection.z / length,
      }
    : { x: 0, y: -1, z: 0 };
  const horizontal = Math.hypot(back.x, back.y);
  const right = horizontal
    ? { x: -back.y / horizontal, y: back.x / horizontal, z: 0 }
    : { x: 1, y: 0, z: 0 };
  const up = {
    x: back.y * right.z - back.z * right.y,
    y: back.z * right.x - back.x * right.z,
    z: back.x * right.y - back.y * right.x,
  };
  const verticalTangent = Math.tan((verticalFovDegrees * Math.PI) / 360);
  const horizontalTangent = verticalTangent * aspect;
  let distance = near * 2;
  for (const sx of [-1, 1])
    for (const sy of [-1, 1])
      for (const sz of [-1, 1]) {
        const x = sx * halfSize.x,
          y = sy * halfSize.y,
          z = sz * halfSize.z;
        const across = x * right.x + y * right.y + z * right.z;
        const vertical = x * up.x + y * up.y + z * up.z;
        const depth = x * back.x + y * back.y + z * back.z;
        // Each corner's forward depth is distance - depth. Keep both projected
        // axes within 1 / padding, and the closest corner beyond the near plane.
        distance = Math.max(
          distance,
          depth + (padding * Math.abs(across)) / horizontalTangent,
          depth + (padding * Math.abs(vertical)) / verticalTangent,
          depth + near * 2,
        );
      }
  return distance;
}
