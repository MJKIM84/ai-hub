import assert from 'node:assert/strict';
import { build } from 'esbuild';
import { mkdtemp,writeFile,rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';
const dir=await mkdtemp(join(tmpdir(),'scene-motion-'));
try {
 const result=await build({stdin:{contents:'export * from "./src/SceneMotion"; export * as THREE from "three";',resolveDir:process.cwd()},bundle:true,platform:'node',format:'esm',write:false});
 const file=join(dir,'motion.mjs');await writeFile(file,result.outputFiles[0].contents);
 const {SceneMotion,THREE}=await import(pathToFileURL(file));
 const motion=new SceneMotion(),mesh=new THREE.Object3D();
 const geom=(x,q=[1,0,0,0])=>({id:1,position:[x,0,0],quaternion:q});
 const input=[geom(.1,[0,0,0,1])],original=JSON.stringify(input);
 motion.receive('run',0,true,[geom(0)],0);
 motion.receive('run',.1,true,input,50);
 motion.apply(1,mesh,75);assert.equal(mesh.position.x,.05);
 assert.ok(Math.abs(mesh.quaternion.angleTo(new THREE.Quaternion())-Math.PI/2)<1e-7);
 motion.receive('run',.2,true,[geom(.2)],75);motion.apply(1,mesh,75);
 assert.equal(mesh.position.x,.05,'early packet must not jump backwards or queue motion');
 motion.apply(1,mesh,1000);assert.equal(mesh.position.x,.2,'no extrapolation after disconnect');assert.equal(motion.active(1000),false);
 motion.receive('run',.2,false,[geom(.2)],1010);motion.apply(1,mesh,1010);assert.equal(mesh.position.x,.2,'pause/diagnostic snaps to received truth');
 motion.receive('new-run',0,true,[geom(9)],1020);motion.apply(1,mesh,1020);assert.equal(mesh.position.x,9,'reset must never interpolate between runs');
 motion.receive('new-run',1,true,[geom(10)],2000);motion.apply(1,mesh,2000);assert.equal(mesh.position.x,10,'stale gap does not animate invented travel');
 assert.equal(JSON.stringify(input),original,'physical input untouched');
 console.log('PASS: continuous packet blending, quaternion slerp, no extrapolation, pause/diagnostics/reset/disconnection, immutable physics input.');
} finally {await rm(dir,{recursive:true,force:true});}
