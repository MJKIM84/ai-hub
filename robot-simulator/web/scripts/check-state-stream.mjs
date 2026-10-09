import assert from 'node:assert/strict';
import { build } from 'esbuild';
import { mkdtemp,writeFile,rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';
const dir=await mkdtemp(join(tmpdir(),'state-stream-'));
try {
 const result=await build({entryPoints:['src/StateStream.ts'],bundle:true,platform:'node',format:'esm',write:false});
 const file=join(dir,'stream.mjs');await writeFile(file,result.outputFiles[0].contents);
 const {mergeStateFrame,isNewerState,openStateStream}=await import(pathToFileURL(file));
 const state={run_id:'one',state_source:'server',state_sequence:1,sim_time:0,status:'running',geoms:[{id:2}],robots:[],events:['kept']};
 const first=mergeStateFrame(null,{full:true,state});
 const next=mergeStateFrame(first,{full:false,base_sequence:1,state:{state_sequence:2,sim_time:.1}});
 assert.equal(first.sim_time,0,'immutable preceding physical snapshot');
 assert.equal(next.sim_time,.1);assert.equal(next.geoms,first.geoms);assert.equal(next.events,first.events);
 assert.throws(()=>mergeStateFrame(null,{full:false,base_sequence:1,state:{state_sequence:2}}));
 assert.throws(()=>mergeStateFrame(next,{full:false,base_sequence:1,state:{state_sequence:3}}));
 assert.equal(isNewerState(next,first),false,'late GET/stream response cannot restore earlier state');
 const reset={...state,run_id:'two',state_sequence:3,sim_time:0,status:'paused'};
 assert.equal(isNewerState(next,reset),true);
 assert.equal(isNewerState(reset,next),false,'old run packet cannot undo reset');
 assert.equal(mergeStateFrame(next,{full:true,state:reset}).run_id,'two');
 const delivered=[],connections=[];
 class FakeEventSource {
  constructor(url){assert.equal(url,'/api/state/stream');this.closed=false;connections.push(this);}
  close(){this.closed=true;}
  send(frame){this.onmessage?.({data:JSON.stringify(frame)});}
 }
 globalThis.EventSource=FakeEventSource;
 const stream=openStateStream(s=>delivered.push(s));const source=connections[0];
 source.onopen();source.send({full:true,state});assert.equal(stream.healthy(),true);
 source.send({full:false,base_sequence:1,state:{state_sequence:2,status:'paused'}});
 assert.equal(delivered.at(-1).status,'paused');
 source.onerror();assert.equal(stream.healthy(),false,'network failure enables GET fallback');
 source.onopen();source.send({full:true,state:reset});assert.equal(delivered.at(-1).run_id,'two');
 stream.close();source.send({full:true,state:{...state,state_sequence:9}});
 assert.equal(delivered.length,3,'closed connection cannot publish late messages');
 const broken=openStateStream(()=>assert.fail('invalid delta must not publish'));
 connections[1].send({full:false,base_sequence:30,state:{state_sequence:31}});
 assert.equal(broken.expired(),true);assert.equal(connections[1].closed,true);
 console.log('PASS: full/delta state, immutable snapshots, ordering, reset, pause, reconnect, closed-stream fencing and fallback.');
} finally {await rm(dir,{recursive:true,force:true});}
