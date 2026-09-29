import { test } from 'node:test';
import assert from 'node:assert/strict';
import { identity, newIdentity, ownerHash, settings, slotNames, allowedOrigin, COOKIE } from '../lib/session-policy.mjs';
import { launch } from '../lib/runtime.mjs';
import handler from '../api/session.mjs';
const config = {daily:2, concurrent:2, minutes:30, snapshot:'snapshot-test',access:{secret:'a'.repeat(64)}};
function fake(overrides={}) {
  return {find:async()=>({items:[]}),load:async x=>x,create:async x=>({...x,stop:async()=>{}}),start:async x=>({url:x.name}),...overrides};
}
test('only a full random browser credential is accepted; owner tags do not reveal it',()=>{
  const token=newIdentity(); assert.equal(identity(`other=x; ${COOKIE}=${token}`),token);
  assert.equal(identity(`${COOKIE}=../../someone`),null); assert.notEqual(ownerHash(token),token);
});
test('creation policy rejects unlimited or malformed environment values',()=>{
  assert.equal(settings({}).daily,10);
  for (const value of ['0','21','2.5','no']) assert.throws(()=>settings({ROBOT_DAILY_SESSIONS:value}));
});
test('mutations require exact HTTPS same origin',()=>{
  const headers={host:'robot.example',origin:'https://robot.example'};
  assert.ok(allowedOrigin({headers}));
  for(const origin of [undefined,'https://evil.example','http://robot.example']) assert.ok(!allowedOrigin({headers:{...headers,origin}}));
  assert.ok(!allowedOrigin({headers:{...headers,'sec-fetch-site':'cross-site'}}));
});
test('unique slots roll over on UTC day and stay bounded',()=>{
  assert.deepEqual(slotNames(2,new Date('2026-09-29T00:00:00Z')),['rop-20260929-00','rop-20260929-01']);
});
test('an existing session is reused without creating or rebooting it',async()=>{
  const result=await launch('a',config,fake({find:async()=>({items:[],item:{name:'mine',tags:{access:'password-v1'}}}),wait:async()=>({url:'mine'}),create:async()=>assert.fail(),start:async()=>assert.fail()}));
  assert.ok(result.url.startsWith('mine/access/start#entry='));
});
test('active capacity does not allocate another machine',async()=>{
  const result=await launch('a',config,fake({find:async()=>({items:[{status:'running'},{status:'pending'}]}),create:async()=>assert.fail()}));
  assert.equal(result.status,429);
});
test('stopped slots still count toward the daily ceiling and are never resumed',async()=>{
  const result=await launch('a',config,fake({find:async()=>({items:slotNames(2).map(name=>({name,status:'stopped'}))}),create:async()=>assert.fail()}));
  assert.equal(result.status,429);
});
test('concurrent creation conflicts cannot allocate beyond named daily slots',async()=>{
  let attempts=0;
  const result=await launch('a',config,fake({create:async()=>{attempts++;throw {response:{status:409}};}}));
  assert.equal(attempts,2); assert.equal(result.status,429);
});
test('failed readiness stops the newly created machine',async()=>{
  let stopped=false;
  await assert.rejects(launch('a',config,fake({create:async options=>{assert.equal(options.persistent,false);assert.equal(options.timeout,1800000);return {stop:async()=>{stopped=true;}};},start:async()=>{throw Error('failed');}})));
  assert.ok(stopped);
});
test('no public snapshot means no allocation',async()=>{
  assert.equal((await launch('a',{...config,snapshot:''},fake({create:async()=>assert.fail()}))).status,503);
});
function response(){return {headers:{},setHeader(k,v){this.headers[k]=v;},status(n){this.code=n;return this;},json(x){this.body=x;return this;}};}
test('first status request only sets a secure cookie; it never allocates',async()=>{
  const res=response();await handler({method:'GET',headers:{}},res);
  assert.equal(res.code,200);assert.equal(res.body.session,null);
  assert.match(res.headers['Set-Cookie'],/HttpOnly; Secure; SameSite=Strict/);
});
test('cross origin start is rejected before any cloud call',async()=>{
  const res=response();await handler({method:'POST',headers:{host:'robot.example',origin:'https://evil.example'}},res);assert.equal(res.code,403);
});

test('legacy runtimes require explicit user termination; never silently discard or claim protected access',async()=>{
 const result=await launch('a',config,fake({find:async()=>({items:[],item:{name:'legacy',tags:{}}}),load:async()=>assert.fail(),create:async()=>assert.fail()}));
 assert.equal(result.status,409);assert.match(result.error,/결과를 저장/);
});
