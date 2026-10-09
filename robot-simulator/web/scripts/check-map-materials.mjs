import assert from "node:assert/strict";
import { build } from "esbuild";
import { mkdtemp, writeFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { pathToFileURL } from "node:url";

// Node checks the same Three.js meshes without a browser or physics process.
const dir = await mkdtemp(join(tmpdir(), "map-material-check-"));
try {
  const compiled = await build({
    stdin: {
      contents:
        'export * from "./src/MapMaterials"; export * from "./src/HumanVisual"; export * as THREE from "three";',
      resolveDir: process.cwd(),
    },
    bundle: true,
    platform: "node",
    format: "esm",
    write: false,
    define: { "import.meta.env.BASE_URL": '"/"' },
  });
  const path = join(dir, "materials.mjs");
  await writeFile(path, compiled.outputFiles[0].contents);
  const { THREE, surfaceFor, mapSurfaceUVs, MapMaterials, createHumanVisual } =
    await import(pathToFileURL(path));
  const geom = {
    name: "floor/f1/0-0",
    position: [10, 5, -0.1],
    size: [2, 3, 0.1],
  };
  assert.equal(surfaceFor(geom), "floor");
  assert.equal(surfaceFor({ name: "lift/door-panel" }, "elevator"), "steel");
  assert.equal(surfaceFor({ name: "lift/platform" }, "elevator"), "tread");
  assert.equal(surfaceFor({ name: "stairs/step-0" }, "stairs"), "tread");
  assert.equal(surfaceFor({ name: "wall/shape" }, "wall"), "wall");
  assert.equal(surfaceFor({ name: "robot/chassis" }), null);
  assert.equal(surfaceFor({ name: "loading/zone" }, "loading"), null);

  const mesh = new THREE.BoxGeometry(4, 6, 0.2);
  const vertices = [...mesh.attributes.position.array],
    normals = [...mesh.attributes.normal.array];
  mapSurfaceUVs(mesh, "floor", geom);
  assert.deepEqual([...mesh.attributes.position.array], vertices);
  assert.deepEqual([...mesh.attributes.normal.array], normals);
  for (let i = 0; i < mesh.attributes.position.count; i++) {
    if (mesh.attributes.normal.getZ(i) < 0.9) continue;
    assert.equal(
      mesh.attributes.uv.getX(i),
      (mesh.attributes.position.getX(i) + 10) / 2,
    );
    assert.equal(
      mesh.attributes.uv.getY(i),
      (mesh.attributes.position.getY(i) + 5) / 2,
    );
  }

  const pending = [],
    statuses = [];
  THREE.TextureLoader.prototype.load = function (url, ok, _progress, fail) {
    const texture = new THREE.Texture();
    pending.push({ url, texture, ok, fail });
    return texture;
  };
  const library = new MapMaterials(16, (state) => statuses.push(state));
  library.load();
  assert.equal(pending.length, 5);
  const mat = new THREE.MeshStandardMaterial({ color: 0x668899 });
  library.apply(mat, "floor", true);
  assert.equal(
    mat.map,
    null,
    "unloaded image must retain a usable plain surface",
  );
  pending[0].ok();
  library.apply(mat, "floor", true);
  assert.equal(mat.map, pending[0].texture);
  assert.equal(mat.map.anisotropy, 8);
  library.apply(mat, "floor", false);
  assert.equal(mat.map, null, "diagnostic/plain mode removes the texture");
  pending[1].fail();
  assert.deepEqual(library.status.failed, ["wall"]);
  library.retry();
  assert.equal(pending.length, 6, "only failed images are requested again");
  pending[5].ok();
  assert.deepEqual(library.status.failed, []);
  assert.equal(library.status.loaded, 2);

  const human = createHumanVisual("worker");
  const motion = {
    time: 3,
    position: [2, 3, 0.85],
    speed: 0.65,
    heading: 0.4,
    distance: 1.8,
  };
  human.update(motion, false);
  const poses = human.meshes.map((m) => [
    ...m.position.toArray(),
    ...m.quaternion.toArray(),
    ...m.scale.toArray(),
  ]);
  human.setJacketTexture(pending[4].texture);
  human.update(motion, false);
  assert.deepEqual(
    human.meshes.map((m) => [
      ...m.position.toArray(),
      ...m.quaternion.toArray(),
      ...m.scale.toArray(),
    ]),
    poses,
  );
  assert.deepEqual(human.root.position.toArray(), [2, 3, 0]);
  human.setJacketTexture(null);
  human.dispose();
  const count = statuses.length;
  library.dispose();
  pending[2].ok();
  assert.equal(
    statuses.length,
    count,
    "late image load after unmount must not update the view",
  );
  mesh.dispose();
  mat.dispose();
  console.log(
    "PASS: surface classification, metre UVs, unchanged mesh/gait, loading fallback, retry, diagnostic toggle, cleanup.",
  );
} finally {
  await rm(dir, { recursive: true, force: true });
}
