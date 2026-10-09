import * as THREE from "three";
import type { Geom } from "./types";

type Pose = { position: THREE.Vector3; rotation: THREE.Quaternion };
type Track = { from: Pose; to: Pose };
const pose = (g: Geom): Pose => ({
  position: new THREE.Vector3(...g.position),
  rotation: new THREE.Quaternion(
    g.quaternion[1],
    g.quaternion[2],
    g.quaternion[3],
    g.quaternion[0],
  ),
});

/** Display-only blending between received physical poses. No prediction or simulation writes. */
export class SceneMotion {
  private tracks = new Map<number, Track>();
  private run = "";
  private simTime = -1;
  private arrivedAt = 0;
  private duration = 0;
  private smoothing = false;

  alpha(now: number) {
    return this.duration
      ? Math.min(1, Math.max(0, (now - this.arrivedAt) / this.duration))
      : 1;
  }
  active(now: number) {
    return this.alpha(now) < 1;
  }

  receive(
    run: string,
    time: number,
    enabled: boolean,
    geoms: Geom[],
    now: number,
  ) {
    if (run === this.run && time === this.simTime && enabled === this.smoothing)
      return;
    const gap = now - this.arrivedAt;
    const smooth =
      enabled &&
      this.smoothing &&
      run === this.run &&
      time > this.simTime &&
      gap > 0 &&
      gap <= 250;
    const alpha = this.alpha(now);
    const next = new Map<number, Track>();
    for (const g of geoms) {
      if (![...g.position, ...g.quaternion].every(Number.isFinite)) continue;
      const to = pose(g),
        old = this.tracks.get(g.id);
      // Rebase on the displayed pose when packets arrive early, never queue animations.
      const from =
        smooth && old
          ? {
              position: old.from.position.clone().lerp(old.to.position, alpha),
              rotation: old.from.rotation.clone().slerp(old.to.rotation, alpha),
            }
          : to;
      next.set(g.id, { from, to });
    }
    this.tracks = next;
    this.run = run;
    this.simTime = time;
    this.smoothing = enabled;
    this.arrivedAt = now;
    this.duration = smooth ? Math.min(120, gap) : 0;
  }

  apply(id: number, object: THREE.Object3D, now: number) {
    const track = this.tracks.get(id);
    if (!track) return;
    const alpha = this.alpha(now);
    object.position.copy(track.from.position).lerp(track.to.position, alpha);
    object.quaternion.copy(track.from.rotation).slerp(track.to.rotation, alpha);
    object.updateMatrixWorld(true);
  }
}
