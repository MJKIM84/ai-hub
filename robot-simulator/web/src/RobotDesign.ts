import * as THREE from "three";
import { RoundedBoxGeometry } from "three/addons/geometries/RoundedBoxGeometry.js";
import type { Geom } from "./types";

// Research-model livery. Never used by physics, allocation or capability checks.
export const robotLiveries = {
  amr: { color: 0x2776c8, shell: 0xe5e9e6, label: "AMR", deck: 0x34414a },
  agv: { color: 0xe6ad31, shell: 0xd9a331, label: "AGV", deck: 0x354048 },
  delivery: {
    color: 0x198f88,
    shell: 0xebece3,
    label: "DELIVERY",
    deck: 0xe0e4dc,
  },
  logistics: {
    color: 0xc96b36,
    shell: 0xd9dedb,
    label: "CARGO",
    deck: 0x49545c,
  },
  arm: { color: 0xe48d35, shell: 0x48555e, label: "ARM", deck: 0x36414a },
  mobile_manipulator: {
    color: 0x488f94,
    shell: 0xdfe6e3,
    label: "MOBILE ARM",
    deck: 0x34474d,
  },
} as const;
type Model = keyof typeof robotLiveries;
type Part =
  "chassis" | "cargo-box" | "tire" | "caster" | "link" | "palm" | "finger";

export function robotDesignPart(g: Geom, model: string): Part | null {
  if (!Object.prototype.hasOwnProperty.call(robotLiveries, model)) return null;
  if (!g.name.startsWith(`${g.entity_id}/`)) return null;
  const part = g.name.slice(g.entity_id.length + 1);
  const kind =
    typeof g.type === "number"
      ? [
          "plane",
          "hfield",
          "sphere",
          "capsule",
          "ellipsoid",
          "cylinder",
          "box",
          "mesh",
        ][g.type]
      : g.type.replace("mjGEOM_", "").toLowerCase();
  if (kind === "box" && ["chassis", "cargo-box", "palm"].includes(part))
    return part as Part;
  if (kind === "box" && /^finger-shape-(left|right)$/.test(part))
    return "finger";
  if (kind === "capsule" && /^arm-link-\d+$/.test(part)) return "link";
  if (kind === "cylinder" && /^(left|right)-tire$/.test(part)) return "tire";
  if (kind === "sphere" && /^caster-(-1|1)$/.test(part)) return "caster";
  return null; // Payloads, equipment, Spot meshes and unknown geometry stay authoritative.
}

type Skin = {
  root: THREE.Group;
  update: (selected: boolean) => void;
  dispose: () => void;
};

function makeSkin(g: Geom, model: Model, part: Part): Skin {
  const root = new THREE.Group();
  root.name = `${g.name}/visual-design`;
  const style = robotLiveries[model];
  const textures: THREE.Texture[] = [];
  const mats = {
    shell: new THREE.MeshStandardMaterial({
      color: style.shell,
      roughness: 0.42,
      metalness: 0.18,
    }),
    accent: new THREE.MeshStandardMaterial({
      color: style.color,
      roughness: 0.43,
      metalness: 0.14,
    }),
    dark: new THREE.MeshStandardMaterial({
      color: 0x232e35,
      roughness: 0.74,
      metalness: 0.12,
    }),
    rubber: new THREE.MeshStandardMaterial({
      color: 0x1b252b,
      roughness: 0.94,
    }),
    metal: new THREE.MeshStandardMaterial({
      color: 0xa4b4bb,
      roughness: 0.35,
      metalness: 0.7,
    }),
    deck: new THREE.MeshStandardMaterial({
      color: style.deck,
      roughness: 0.82,
      metalness: 0.12,
    }),
  };
  type Finish = keyof typeof mats;
  const add = (
    geometry: THREE.BufferGeometry,
    finish: Finish,
    x = 0,
    y = 0,
    z = 0,
  ) => {
    const mesh = new THREE.Mesh(geometry, mats[finish]);
    mesh.position.set(x, y, z);
    mesh.userData.entityId = g.entity_id;
    root.add(mesh);
    return mesh;
  };
  const box = (
    w: number,
    d: number,
    h: number,
    finish: Finish,
    x = 0,
    y = 0,
    z = 0,
    radius = 0.009,
  ) =>
    add(
      new RoundedBoxGeometry(w, d, h, 2, Math.min(radius, w / 3, d / 3, h / 3)),
      finish,
      x,
      y,
      z,
    );
  const disk = (
    r: number,
    depth: number,
    finish: Finish,
    x = 0,
    y = 0,
    z = 0,
  ) =>
    add(
      new THREE.CylinderGeometry(r, r, depth, 20).rotateX(Math.PI / 2),
      finish,
      x,
      y,
      z,
    );
  const [a, b, c] = g.size;

  const label = (text: string, width: number, height: number, z: number) => {
    // The mark identifies a research robot role, not a manufacturer or a live sensor.
    if (typeof document === "undefined") return;
    const canvas = document.createElement("canvas");
    canvas.width = 512;
    canvas.height = 128;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;
    ctx.fillStyle = "#26333c";
    ctx.fillRect(0, 0, 512, 128);
    ctx.fillStyle = "#e8eeed";
    ctx.font = "600 66px sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(text, 256, 67, 472);
    const texture = new THREE.CanvasTexture(canvas);
    texture.colorSpace = THREE.SRGBColorSpace;
    textures.push(texture);
    const mesh = new THREE.Mesh(
      new THREE.PlaneGeometry(width, height),
      new THREE.MeshBasicMaterial({ map: texture, side: THREE.DoubleSide }),
    );
    mesh.position.set(-a * 0.28, 0, z);
    mesh.userData.entityId = g.entity_id;
    root.add(mesh);
  };

  if (part === "chassis") {
    // All body panels fit the existing box. The contact envelope is not enlarged.
    box(a * 2, b * 2, c * 0.6, "dark", 0, 0, -c * 0.65, 0.024);
    box(a * 1.97, b * 1.94, c * 1.36, "shell", 0, 0, c * 0.29, 0.032);
    // Recessed dark load deck and coloured side rails make the front/role readable.
    box(a * 1.55, b * 1.65, 0.008, "deck", -a * 0.08, 0, c - 0.005);
    for (const sign of [-1, 1]) {
      box(
        a * 1.58,
        0.018,
        c * 0.37,
        "accent",
        -a * 0.06,
        sign * (b - 0.012),
        c * 0.21,
      );
      for (let i = 0; i < 4; i++)
        box(
          a * 0.1,
          0.004,
          c * 0.18,
          "dark",
          -a * 0.65 + i * a * 0.15,
          sign * (b - 0.001),
          c * 0.25,
        );
      // Inset front face marking; no fictitious camera or active indicator state.
      box(
        0.012,
        b * 0.42,
        c * 0.23,
        "metal",
        a - 0.009,
        sign * b * 0.53,
        c * 0.35,
      );
    }
    box(0.01, b * 0.6, c * 0.6, "dark", a - 0.004, 0, -c * 0.15);
    if (model === "agv") {
      for (const x of [-a * 0.82, a * 0.82])
        for (let i = -3; i <= 3; i++) {
          const stripe = box(
            a * 0.11,
            b * 0.18,
            0.003,
            "dark",
            x,
            i * b * 0.23,
            c + 0.001,
          );
          stripe.rotation.z = -0.35;
        }
    } else if (model === "logistics") {
      for (let i = -2; i <= 2; i++)
        box(a * 1.5, b * 0.075, 0.004, "metal", -a * 0.08, i * b * 0.27, c);
    } else if (model === "arm") {
      disk(Math.min(a, b) * 0.65, 0.006, "accent", 0, 0, c);
      for (const x of [-a * 0.77, a * 0.77])
        for (const y of [-b * 0.77, b * 0.77])
          disk(0.018, 0.005, "metal", x, y, c);
    }
    label(style.label, a * 1.03, Math.min(b * 0.4, 0.09), c + 0.004);
  } else if (part === "cargo-box") {
    box(a * 2, b * 2, c * 2, "shell", 0, 0, 0, 0.025);
    // Closed compartment follows the real cargo-box geometry; no animated fake door.
    for (const sign of [-1, 1]) {
      box(a * 1.72, 0.006, c * 1.61, "accent", 0, sign * (b - 0.001), 0, 0.016);
      box(a * 0.13, 0.009, c * 0.56, "dark", a * 0.55, sign * b, c * 0.05);
    }
    label("DELIVERY", a * 1.4, b * 0.44, c + 0.001);
  } else if (part === "tire") {
    disk(a, b * 2, "rubber");
    for (const sign of [-1, 1]) {
      disk(a * 0.69, 0.006, "metal", 0, 0, sign * (b - 0.002));
      disk(a * 0.23, 0.009, "dark", 0, 0, sign * (b - 0.002));
      for (let i = 0; i < 6; i++) {
        const theta = (i * Math.PI) / 3;
        disk(
          a * 0.055,
          0.008,
          "dark",
          a * 0.46 * Math.cos(theta),
          a * 0.46 * Math.sin(theta),
          sign * (b - 0.001),
        );
      }
    }
    // Geom quaternion supplies wheel rotation. Never animate from time or commands.
  } else if (part === "caster") {
    // A wheel-and-fork cover for the research model's spherical contact support.
    // Same contact height/radius; the fork is chassis-aligned, never ball-aligned.
    // Axially symmetric surfaces avoid inventing wheel rotation or caster steering.
    const wheel = add(new THREE.CylinderGeometry(a, a, a * 0.62, 32), "rubber");
    wheel.name = "caster-wheel-cover";
    for (const sign of [-1, 1]) {
      const hub = add(
        new THREE.CylinderGeometry(a * 0.53, a * 0.53, a * 0.04, 24),
        "metal",
        0,
        sign * a * 0.32,
        0,
      );
      hub.name = "caster-hub";
      // The arms extend from the observed contact centre to the chassis underside.
      box(
        a * 0.48,
        a * 0.12,
        a * 1.7,
        "metal",
        0,
        sign * a * 0.46,
        a * 0.69,
        a * 0.07,
      );
    }
    add(new THREE.CylinderGeometry(a * 0.18, a * 0.18, a * 1.08, 16), "dark");
    const mount = box(
      a * 1.15,
      a * 1.18,
      a * 0.22,
      "dark",
      0,
      0,
      a * 1.72,
      a * 0.07,
    );
    mount.name = "caster-mount";
  } else if (part === "link") {
    add(
      new THREE.CapsuleGeometry(a, b * 2, 5, 12).rotateX(Math.PI / 2),
      "accent",
    );
    for (const sign of [-1, 1]) {
      disk(a * 1.003, Math.min(0.034, b * 0.35), "dark", 0, 0, sign * b * 0.83);
      disk(a * 1.005, 0.005, "metal", 0, 0, sign * b * 0.62);
    }
    box(a * 0.75, 0.004, b * 0.95, "shell", 0, -a + 0.003, 0, 0.003);
  } else {
    box(
      a * 2,
      b * 2,
      c * 2,
      part === "palm" ? "metal" : "dark",
      0,
      0,
      0,
      0.005,
    );
    if (part === "finger")
      box(a * 1.6, 0.002, c * 1.28, "rubber", 0, b - 0.001, c * 0.1, 0.001);
  }

  return {
    root,
    update(selected) {
      Object.values(mats).forEach((mat) =>
        mat.emissive.setHex(selected ? 0x0b1c32 : 0),
      );
    },
    dispose() {
      root.removeFromParent();
      const materials = new Set<THREE.Material>(Object.values(mats));
      root.traverse((object) => {
        if (!(object instanceof THREE.Mesh)) return;
        object.geometry.dispose();
        materials.add(object.material as THREE.Material);
      });
      materials.forEach((material) => material.dispose());
      textures.forEach((texture) => texture.dispose());
    },
  };
}

/** Visuals follow actual geoms. Caster covers use contact position + chassis orientation. */
export class RobotDesigns {
  private entries = new Map<
    number,
    { mesh: THREE.Mesh; key: string; skin: Skin }
  >();

  apply(
    mesh: THREE.Mesh,
    g: Geom,
    model: string,
    enabled: boolean,
    selected: boolean,
    chassis?: Geom,
  ) {
    let part = robotDesignPart(g, model);
    if (
      part === "caster" &&
      (!chassis ||
        chassis.entity_id !== g.entity_id ||
        chassis.quaternion.length !== 4 ||
        !chassis.quaternion.every(Number.isFinite))
    )
      part = null; // Preserve the diagnostic sphere if its chassis pose is unavailable.
    const key = `${model}:${part}:${g.size.join(",")}`;
    let entry = this.entries.get(g.id);
    if (entry && (entry.key !== key || entry.mesh !== mesh)) {
      entry.skin.dispose();
      (entry.mesh.material as THREE.Material).visible = true;
      this.entries.delete(g.id);
      entry = undefined;
    }
    if (!part) return;
    if (!entry) {
      const skin = makeSkin(g, model as Model, part);
      mesh.add(skin.root);
      entry = { mesh, key, skin };
      this.entries.set(g.id, entry);
    }
    entry.skin.root.visible = enabled;
    if (part === "caster" && chassis) {
      const [w, x, y, z] = chassis.quaternion;
      // Counteract the ball joint's unrestricted spin: a mounting fork cannot tumble.
      entry.skin.root.quaternion
        .copy(mesh.quaternion)
        .invert()
        .multiply(new THREE.Quaternion(x, y, z, w));
    }
    entry.skin.update(selected);
    (mesh.material as THREE.Material).visible = !enabled;
    mesh.updateMatrixWorld(true);
  }

  retain(live: Set<number>) {
    for (const [id, entry] of this.entries)
      if (!live.has(id)) {
        entry.skin.dispose();
        (entry.mesh.material as THREE.Material).visible = true;
        this.entries.delete(id);
      }
  }

  dispose() {
    this.retain(new Set());
  }
}
