import * as THREE from "three";

export type HumanMotion = {
  time: number;
  position: [number, number, number];
  speed: number;
  heading: number;
  distance: number;
};

/** Read-only visual sampling. Controller velocity requests never enter this port. */
export function sampleHumanMotion(
  previous: HumanMotion | undefined,
  position: number[],
  simTime: number,
  actualVelocity?: number[],
  actualHeading?: number | null,
  initialHeading = 0,
): HumanMotion | null {
  if (position.length !== 3 || ![...position, simTime].every(Number.isFinite))
    return null;
  const point = [...position] as [number, number, number];
  if (previous && simTime === previous.time)
    return { ...previous, position: point };
  const dt = previous ? simTime - previous.time : 0;
  const travelled =
    previous && dt > 0
      ? Math.hypot(
          position[0] - previous.position[0],
          position[1] - previous.position[1],
        )
      : 0;
  const velocity =
    actualVelocity?.length === 3 && actualVelocity.every(Number.isFinite)
      ? actualVelocity
      : previous && dt > 0
        ? [
            (position[0] - previous.position[0]) / dt,
            (position[1] - previous.position[1]) / dt,
            0,
          ]
        : [0, 0, 0];
  const speed = Math.hypot(velocity[0], velocity[1]);
  const heading =
    speed > 0.01
      ? Math.atan2(velocity[1], velocity[0])
      : typeof actualHeading === "number" && Number.isFinite(actualHeading)
        ? actualHeading
        : (previous?.heading ??
          (Number.isFinite(initialHeading) ? initialHeading : 0));
  return {
    time: simTime,
    position: point,
    speed,
    heading,
    distance: (previous && dt > 0 ? previous.distance : 0) + travelled,
  };
}

/** A visual gait, not a joint physics/contact result. Feet remain above the base. */
export function humanGait(motion: HumanMotion) {
  const amount = motion.speed <= 0.02 ? 0 : Math.min(1, motion.speed / 1.15);
  const phase = (motion.distance / 1.1) * Math.PI * 2;
  return {
    leftX: Math.sin(phase) * 0.24 * amount,
    rightX: -Math.sin(phase) * 0.24 * amount,
    leftLift: Math.max(0, Math.cos(phase)) * 0.085 * amount,
    rightLift: Math.max(0, -Math.cos(phase)) * 0.085 * amount,
    armSwing: Math.sin(phase) * 0.28 * amount,
  };
}

export interface HumanVisual {
  root: THREE.Group;
  meshes: THREE.Mesh[];
  update: (motion: HumanMotion, selected: boolean) => void;
  dispose: () => void;
}

/** Native, clothed 1.70 m visual human. No external asset or loading fallback. */
export function createHumanVisual(id: string): HumanVisual {
  const root = new THREE.Group();
  root.name = `${id}/human-visual`;
  const meshes: THREE.Mesh[] = [];
  const colors = [0x45668a, 0x60775c, 0x98704f, 0x775f83];
  const seed = [...id].reduce((n, c) => n + c.charCodeAt(0), 0);
  const materials = {
    jacket: new THREE.MeshStandardMaterial({
      color: colors[seed % colors.length],
      roughness: 0.92,
    }),
    trousers: new THREE.MeshStandardMaterial({
      color: 0x303d50,
      roughness: 0.95,
    }),
    skin: new THREE.MeshStandardMaterial({
      color: [0xc98f69, 0xad795b, 0xe0b295][seed % 3],
      roughness: 0.88,
    }),
    hair: new THREE.MeshStandardMaterial({ color: 0x352d2a, roughness: 1 }),
    shoe: new THREE.MeshStandardMaterial({ color: 0x27303b, roughness: 0.92 }),
    trim: new THREE.MeshStandardMaterial({ color: 0xd7dbe0, roughness: 0.9 }),
  };
  const add = (
    name: string,
    geometry: THREE.BufferGeometry,
    material: THREE.Material,
    position: number[],
  ) => {
    const mesh = new THREE.Mesh(geometry, material);
    mesh.name = `${id}/visual/${name}`;
    mesh.position.fromArray(position);
    mesh.userData = {
      entityId: id,
      selectable: true,
      sourceOpacity: 1,
      humanVisual: true,
    };
    root.add(mesh);
    meshes.push(mesh);
    return mesh;
  };
  const oval = (
    name: string,
    radii: number[],
    position: number[],
    material: THREE.Material,
  ) =>
    add(
      name,
      new THREE.SphereGeometry(1, 16, 10).scale(radii[0], radii[1], radii[2]),
      material,
      position,
    );
  const cylinder = (name: string, material: THREE.Material) =>
    add(
      name,
      new THREE.CylinderGeometry(1, 1, 1, 12).rotateX(Math.PI / 2),
      material,
      [0, 0, 0],
    );
  const segment = (
    mesh: THREE.Mesh,
    from: THREE.Vector3,
    to: THREE.Vector3,
    radius: number,
  ) => {
    const delta = to.clone().sub(from);
    mesh.position.copy(from).add(to).multiplyScalar(0.5);
    mesh.quaternion.setFromUnitVectors(
      new THREE.Vector3(0, 0, 1),
      delta.clone().normalize(),
    );
    mesh.scale.set(radius, radius, delta.length());
  };
  oval("trouser-waist", [0.14, 0.18, 0.13], [0, 0, 0.91], materials.trousers);
  add(
    "jacket",
    new THREE.CylinderGeometry(0.23, 0.175, 0.46, 12)
      .rotateX(Math.PI / 2)
      .scale(0.66, 1, 1),
    materials.jacket,
    [0, 0, 1.2],
  );
  add(
    "zipper",
    new THREE.BoxGeometry(0.008, 0.012, 0.37),
    materials.trim,
    [0.147, 0, 1.2],
  );
  oval("collar", [0.088, 0.115, 0.032], [0, 0, 1.423], materials.jacket);
  oval("neck", [0.06, 0.06, 0.075], [0, 0, 1.455], materials.skin);
  oval("head", [0.107, 0.115, 0.143], [0, 0, 1.555], materials.skin);
  oval("hair", [0.109, 0.117, 0.07], [-0.018, 0, 1.639], materials.hair);
  oval("nose", [0.033, 0.023, 0.035], [0.101, 0, 1.56], materials.skin);
  for (const side of [-1, 1]) {
    oval(
      `ear-${side}`,
      [0.025, 0.021, 0.046],
      [-0.006, side * 0.112, 1.555],
      materials.skin,
    );
    oval(
      `eye-${side}`,
      [0.006, 0.013, 0.009],
      [0.099, side * 0.042, 1.59],
      materials.hair,
    );
  }
  const legs = [-1, 1].map((side) => ({
    side,
    thigh: cylinder(`thigh-${side}`, materials.trousers),
    shin: cylinder(`shin-${side}`, materials.trousers),
    shoe: oval(
      `shoe-${side}`,
      [0.155, 0.082, 0.065],
      [0.075, side * 0.1, 0.065],
      materials.shoe,
    ),
    sole: oval(
      `sole-${side}`,
      [0.158, 0.084, 0.013],
      [0.075, side * 0.1, 0.014],
      materials.trim,
    ),
  }));
  const arms = [-1, 1].map((side) => ({
    side,
    upper: cylinder(`upper-arm-${side}`, materials.jacket),
    lower: cylinder(`forearm-${side}`, materials.jacket),
    hand: oval(
      `hand-${side}`,
      [0.042, 0.036, 0.08],
      [0, side * 0.27, 0.85],
      materials.skin,
    ),
    thumb: oval(
      `thumb-${side}`,
      [0.025, 0.021, 0.045],
      [0, side * 0.27, 0.85],
      materials.skin,
    ),
  }));
  const update = (motion: HumanMotion, selected: boolean) => {
    // The API/geom torso origin is 0.85 m above the physical floor; no body write.
    root.position.set(
      motion.position[0],
      motion.position[1],
      motion.position[2] - 0.85,
    );
    root.rotation.z = motion.heading;
    const gait = humanGait(motion);
    for (const leg of legs) {
      const step = leg.side === 1 ? gait.leftX : gait.rightX;
      const lift = leg.side === 1 ? gait.leftLift : gait.rightLift;
      const hip = new THREE.Vector3(0, leg.side * 0.1, 0.885);
      const ankle = new THREE.Vector3(step, leg.side * 0.1, 0.13 + lift);
      const delta = ankle.clone().sub(hip),
        length = delta.length();
      const bend = Math.sqrt(Math.max(0, 0.415 ** 2 - (length / 2) ** 2));
      const knee = hip
        .clone()
        .add(ankle)
        .multiplyScalar(0.5)
        .addScaledVector(
          new THREE.Vector3(-delta.z, 0, delta.x).normalize(),
          bend,
        );
      segment(leg.thigh, hip, knee, 0.08);
      segment(leg.shin, knee, ankle, 0.064);
      leg.shoe.position.set(step + 0.075, leg.side * 0.1, 0.065 + lift);
      leg.sole.position.set(step + 0.075, leg.side * 0.1, 0.014 + lift);
    }
    for (const arm of arms) {
      const swing = -arm.side * gait.armSwing;
      const shoulder = new THREE.Vector3(0, arm.side * 0.225, 1.36);
      const elbow = new THREE.Vector3(swing * 0.6, arm.side * 0.26, 1.105);
      const wrist = new THREE.Vector3(
        swing + 0.055,
        arm.side * 0.275,
        0.9 + Math.abs(swing) * 0.18,
      );
      segment(arm.upper, shoulder, elbow, 0.068);
      segment(arm.lower, elbow, wrist, 0.054);
      arm.hand.position.copy(wrist).add(new THREE.Vector3(0.012, 0, -0.06));
      arm.thumb.position
        .copy(wrist)
        .add(new THREE.Vector3(0.043, -arm.side * 0.025, -0.045));
    }
    for (const material of Object.values(materials))
      material.emissive.setHex(selected ? 0x101d31 : 0);
    root.updateMatrixWorld(true);
  };
  update(
    { time: 0, position: [0, 0, 0.85], speed: 0, heading: 0, distance: 0 },
    false,
  );
  return {
    root,
    meshes,
    update,
    dispose: () => {
      meshes.forEach((mesh) => mesh.geometry.dispose());
      Object.values(materials).forEach((material) => material.dispose());
    },
  };
}
