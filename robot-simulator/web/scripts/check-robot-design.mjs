import assert from "node:assert/strict";
import { build } from "esbuild";
import { mkdtemp, writeFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { pathToFileURL } from "node:url";

const dir = await mkdtemp(join(tmpdir(), "robot-design-check-"));
try {
  const compiled = await build({
    stdin: {
      contents:
        'export * from "./src/RobotDesign"; export * as THREE from "three";',
      resolveDir: process.cwd(),
    },
    bundle: true,
    platform: "node",
    format: "esm",
    write: false,
  });
  const path = join(dir, "design.mjs");
  await writeFile(path, compiled.outputFiles[0].contents);
  const { THREE, RobotDesigns, robotLiveries } = await import(
    pathToFileURL(path)
  );
  const designs = new RobotDesigns();
  const g = {
    id: 1,
    entity_id: "r1",
    name: "r1/chassis",
    type: 6,
    size: [0.4, 0.325, 0.1],
    position: [4, 5, 0.3],
    quaternion: [1, 0, 0, 0],
    rgba: [0.3, 0.4, 0.4, 1],
  };
  const unchanged = JSON.stringify(g);
  const mesh = new THREE.Mesh(
    new THREE.BoxGeometry(0.8, 0.65, 0.2),
    new THREE.MeshStandardMaterial(),
  );
  const vertices = [...mesh.geometry.attributes.position.array];
  mesh.position.fromArray(g.position);
  for (const model of Object.keys(robotLiveries)) {
    designs.apply(mesh, g, model, true, false);
    assert.equal(mesh.children.length, 1);
    assert.equal(mesh.material.visible, false);
    const bounds = new THREE.Box3().setFromObject(mesh.children[0]);
    const size = bounds.getSize(new THREE.Vector3());
    assert.ok(
      size.x <= 0.81 && size.y <= 0.66 && size.z <= 0.21,
      `${model}: decoration must fit the chassis envelope within 5 mm`,
    );
    assert.deepEqual([...mesh.geometry.attributes.position.array], vertices);
    assert.equal(
      JSON.stringify(g),
      unchanged,
      "input physical state must be immutable",
    );
    designs.apply(mesh, g, model, false, true);
    assert.equal(
      mesh.material.visible,
      true,
      "diagnostics must expose the source geometry",
    );
    assert.equal(mesh.children[0].visible, false);
  }
  designs.apply(mesh, g, "amr", true, false);
  const liveSkin = mesh.children[0];
  designs.apply(mesh, g, "amr", true, false);
  assert.equal(
    mesh.children[0],
    liveSkin,
    "state frames must reuse the same meshes",
  );
  const child = liveSkin.children[0];
  mesh.position.set(7, 8, 3.5);
  mesh.quaternion.setFromAxisAngle(new THREE.Vector3(0, 0, 1), 1.3);
  mesh.updateMatrixWorld(true);
  const expected = mesh.localToWorld(child.position.clone());
  assert.ok(
    child.getWorldPosition(new THREE.Vector3()).distanceTo(expected) < 1e-10,
    "visual body must follow actual position and orientation",
  );
  const ray = new THREE.Raycaster(
    new THREE.Vector3(7, 8, 5),
    new THREE.Vector3(0, 0, -1),
  );
  const hits = ray.intersectObjects([mesh], true);
  assert.ok(
    hits.some((hit) => hit.object.userData.entityId === "r1"),
    "decorative surfaces must preserve entity picking",
  );

  let disposed = 0;
  liveSkin.traverse((obj) => {
    if (obj.isMesh) obj.geometry.addEventListener("dispose", () => disposed++);
  });
  designs.retain(new Set());
  assert.equal(mesh.children.length, 0);
  assert.equal(mesh.material.visible, true);
  assert.ok(disposed > 0, "retired runs must release GPU geometry");
  for (const [name, model] of [
    ["r1/chassis", "spot"],
    ["r1/initial-payload", "amr"],
    ["r1/equipment-0", "amr"],
    ["r1/chassis", "new-model"],
  ]) {
    designs.apply(mesh, { ...g, name }, model, true, false);
    assert.equal(
      mesh.children.length,
      0,
      "Spot, cargo, mounted equipment and unknown models must stay unchanged",
    );
  }

  for (const [name, type, geometry, size] of [
    [
      "r1/arm-link-2",
      3,
      new THREE.CapsuleGeometry(0.045, 0.35).rotateX(Math.PI / 2),
      [0.045, 0.175, 0],
    ],
    [
      "r1/finger-shape-left",
      6,
      new THREE.BoxGeometry(0.08, 0.024, 0.14),
      [0.04, 0.012, 0.07],
    ],
    [
      "r1/left-tire",
      5,
      new THREE.CylinderGeometry(0.12, 0.12, 0.07).rotateX(Math.PI / 2),
      [0.12, 0.035, 0],
    ],
  ]) {
    const part = new THREE.Mesh(geometry, new THREE.MeshStandardMaterial());
    designs.apply(
      part,
      { ...g, name, type, size },
      "mobile_manipulator",
      true,
      false,
    );
    part.position.set(0.2, 0.6, 1.3);
    part.quaternion.setFromEuler(new THREE.Euler(0.8, 0.5, 1.1));
    part.updateMatrixWorld(true);
    const skin = part.children[0];
    const actual = new THREE.Quaternion();
    skin.getWorldQuaternion(actual);
    assert.ok(
      actual.angleTo(part.quaternion) < 1e-7,
      "arm, finger and tire must inherit observed articulation, with no time animation",
    );
    designs.dispose();
    part.geometry.dispose();
    part.material.dispose();
  }
  // Ball contact can roll on every axis; its mounting bracket must stay with the chassis.
  const caster = new THREE.Mesh(
    new THREE.SphereGeometry(0.07),
    new THREE.MeshStandardMaterial(),
  );
  const casterGeom = {
    ...g,
    id: 2,
    name: "r1/caster-1",
    type: 2,
    size: [0.07, 0, 0],
  };
  const casterSource = JSON.stringify(casterGeom);
  const bodyQ = new THREE.Quaternion().setFromEuler(
    new THREE.Euler(0.08, -0.12, 1.2),
  );
  const chassis = { ...g, quaternion: [bodyQ.w, bodyQ.x, bodyQ.y, bodyQ.z] };
  caster.position.set(4.3, 5, 0.07);
  for (const spin of [0, 1.4, 3.1]) {
    caster.quaternion.setFromEuler(new THREE.Euler(spin, spin * 0.7, -spin));
    designs.apply(caster, casterGeom, "amr", true, false, chassis);
    const cover = caster.children[0];
    assert.ok(
      cover.getWorldQuaternion(new THREE.Quaternion()).angleTo(bodyQ) < 1e-7,
      "fork must stay chassis-aligned while the contact sphere spins",
    );
    assert.ok(
      cover.getWorldPosition(new THREE.Vector3()).distanceTo(caster.position) <
        1e-10,
      "caster cover must keep the observed contact centre",
    );
    const wheel = cover.getObjectByName("caster-wheel-cover");
    wheel.geometry.computeBoundingBox();
    assert.ok(
      Math.abs(wheel.geometry.boundingBox.min.z + 0.07) < 1e-7,
      "wheel must preserve the spherical support's contact height",
    );
  }
  assert.equal(JSON.stringify(casterGeom), casterSource);
  designs.apply(caster, casterGeom, "amr", false, false, chassis);
  assert.equal(caster.material.visible, true);
  assert.equal(caster.children[0].visible, false);
  designs.apply(caster, casterGeom, "amr", true, false);
  assert.equal(
    caster.children.length,
    0,
    "missing chassis pose must retain the source sphere",
  );
  assert.equal(caster.material.visible, true);
  caster.geometry.dispose();
  caster.material.dispose();
  designs.dispose();
  mesh.geometry.dispose();
  mesh.material.dispose();
  console.log(
    "PASS: six robot designs, envelope bounds, physical-state immutability, live pose/joint inheritance, chassis-aligned caster covers/contact height/fallback, selection, diagnostics, reuse and GPU cleanup; Spot/cargo/equipment preserved.",
  );
} finally {
  await rm(dir, { recursive: true, force: true });
}
