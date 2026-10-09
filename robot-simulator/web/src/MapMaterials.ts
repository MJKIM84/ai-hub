import * as THREE from "three";
import type { Geom } from "./types";

export const materialAssets = {
  floor: "floor-epoxy",
  wall: "wall-panel",
  steel: "elevator-steel",
  tread: "stair-grip",
  jacket: "worker-jacket",
} as const;
export type Surface = keyof typeof materialAssets;
export interface MaterialLoadStatus {
  loaded: number;
  failed: Surface[];
  total: number;
}

// Only existing, identified surfaces receive decoration. Zone markers, sensors,
// robots and cargo keep their simulation colors and geometry.
export function surfaceFor(
  g: Pick<Geom, "name">,
  kind?: string,
): Surface | null {
  if (g.name.startsWith("floor/"))
    return g.name.includes("/sill-") ? "steel" : "floor";
  if (kind === "wall" || kind === "column") return "wall";
  if (kind === "stairs" || kind === "ramp") return "tread";
  if (kind === "elevator")
    return g.name.endsWith("/platform") ? "tread" : "steel";
  if (kind === "door") return "steel";
  return null;
}

const profiles = {
  floor: { tile: 2, roughness: 0.88, metalness: 0 },
  wall: { tile: 2.4, roughness: 0.8, metalness: 0.02 },
  steel: { tile: 1.2, roughness: 0.48, metalness: 0.28 },
  tread: { tile: 0.8, roughness: 0.78, metalness: 0.18 },
  jacket: { tile: 1, roughness: 0.92, metalness: 0 },
};

/** Metre-based UVs on the existing mesh; never modify vertex positions/normals.
 * Floor fragments share world XY so elevator cut-outs do not restart a tile.
 * Other surfaces use local coordinates so their material moves with the body.
 */
export function mapSurfaceUVs(
  geometry: THREE.BufferGeometry,
  surface: Surface,
  g: Geom,
) {
  const p = geometry.getAttribute("position");
  const n = geometry.getAttribute("normal");
  if (!p || !n) return;
  const values = new Float32Array(p.count * 2);
  const tile = profiles[surface].tile;
  for (let i = 0; i < p.count; i++) {
    const x = p.getX(i),
      y = p.getY(i),
      z = p.getZ(i);
    const nx = Math.abs(n.getX(i)),
      ny = Math.abs(n.getY(i)),
      nz = Math.abs(n.getZ(i));
    let u: number, v: number;
    if (nz >= nx && nz >= ny) {
      u = x + (surface === "floor" ? g.position[0] : 0);
      v = y + (surface === "floor" ? g.position[1] : 0);
    } else {
      u = nx > ny ? y : x;
      v = z;
    }
    values[i * 2] = u / tile;
    values[i * 2 + 1] = v / tile;
  }
  geometry.setAttribute("uv", new THREE.BufferAttribute(values, 2));
}

/** One texture per surface, owned by a single 3D view (including GPU cleanup). */
export class MapMaterials {
  private entries = new Map<
    Surface,
    { texture: THREE.Texture; ready: boolean }
  >();
  private failed = new Set<Surface>();
  private disposed = false;
  constructor(
    private anisotropy: number,
    private changed: (status: MaterialLoadStatus) => void,
  ) {}

  get status(): MaterialLoadStatus {
    return {
      loaded: [...this.entries.values()].filter((e) => e.ready).length,
      failed: [...this.failed],
      total: Object.keys(materialAssets).length,
    };
  }

  load() {
    for (const key of Object.keys(materialAssets) as Surface[]) {
      if (this.entries.has(key)) continue;
      const texture = new THREE.TextureLoader().load(
        `${import.meta.env.BASE_URL}materials/industrial-v1/${materialAssets[key]}.jpg`,
        () => {
          if (this.disposed) {
            texture.dispose();
            return;
          }
          this.entries.get(key)!.ready = true;
          this.changed(this.status);
        },
        undefined,
        () => {
          if (this.disposed) return;
          this.failed.add(key);
          this.changed(this.status);
        },
      );
      texture.colorSpace = THREE.SRGBColorSpace;
      texture.wrapS = THREE.RepeatWrapping;
      texture.wrapT =
        key === "jacket" ? THREE.ClampToEdgeWrapping : THREE.RepeatWrapping;
      texture.anisotropy = Math.min(8, this.anisotropy);
      texture.name = materialAssets[key];
      this.entries.set(key, { texture, ready: false });
    }
  }

  get(key: Surface): THREE.Texture | null {
    const entry = this.entries.get(key);
    return entry?.ready ? entry.texture : null;
  }

  apply(
    material: THREE.MeshStandardMaterial,
    surface: Surface | null,
    enabled: boolean,
  ) {
    const map = surface && enabled ? this.get(surface) : null;
    if (material.map !== map) {
      material.map = map;
      material.needsUpdate = true;
    }
    if (map && surface) {
      material.color.setHex(0xffffff);
      material.roughness = profiles[surface].roughness;
      material.metalness = profiles[surface].metalness;
    } else {
      material.roughness = 0.76;
      material.metalness = 0.04;
    }
  }

  retry() {
    for (const key of this.failed) {
      this.entries.get(key)?.texture.dispose();
      this.entries.delete(key);
    }
    this.failed.clear();
    this.changed(this.status);
    this.load();
  }

  dispose() {
    this.disposed = true;
    this.entries.forEach((entry) => entry.texture.dispose());
    this.entries.clear();
  }
}
