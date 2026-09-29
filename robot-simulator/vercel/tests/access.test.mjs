import {test} from 'node:test';
import assert from 'node:assert/strict';
import {scryptSync} from 'node:crypto';
import {accessSettings,verifyPassword,accessCookie,authorized,sign,verify,runtimeEntry,runtimeSecret} from '../lib/access.mjs';
import access from '../api/access.mjs';
import session from '../api/session.mjs';
import {COOKIE} from '../lib/session-policy.mjs';
const salt='d'.repeat(32), password='test-only-long-password';
const hash=`scrypt:${salt}:${scryptSync(password,Buffer.from(salt,'hex'),64).toString('hex')}`;
const config={hash,secret:'b'.repeat(64)}, identity='c'.repeat(64);
const headers={host:'robot.example',origin:'https://robot.example','content-type':'application/json',cookie:`${COOKIE}=${identity}`};
const response=()=>({headers:{},setHeader(k,v){this.headers[k]=v;},status(n){this.code=n;return this;},json(x){this.body=x;return this;}});
test('password verifier fails closed, supports no default, and rejects incorrect/malformed values',async()=>{
 assert.equal(accessSettings({}),null);assert.ok(await verifyPassword(password,config));
 for(const p of ['wrong','',null,{},'x'.repeat(129)])assert.equal(await verifyPassword(p,config),false);
});
test('signed access expires, binds to the anonymous identity, and is invalidated by password rotation',()=>{
 const cookie=accessCookie(identity,config,1000);
 assert.ok(authorized(cookie,identity,config,1001));assert.ok(!authorized(cookie,'d'.repeat(64),config,1001));
 assert.ok(!authorized(cookie,identity,config,2800));assert.ok(!authorized(cookie,identity,{...config,hash:hash+'x'},1001));
 const raw=JSON.parse(Buffer.from(cookie.split('=')[1].split('.')[0],'base64url'));
 assert.notEqual(raw.version,hash);assert.ok(!JSON.stringify(raw).includes(password));
 assert.match(cookie,/HttpOnly; Secure; SameSite=Strict/);
 assert.equal(verify(sign({exp:2000},config.secret)+'x',config.secret,1000),null);
});
test('runtime tickets expire quickly, are unique, and are scoped to the runtime and browser',()=>{
 const a=runtimeEntry({url:'https://run.example'},identity,'sandbox-a',config,1000);
 const b=runtimeEntry({url:'https://run.example'},identity,'sandbox-a',config,1000);
 assert.notEqual(a.url,b.url);
 const ticket=a.url.split('#entry=')[1], key=runtimeSecret(identity,'sandbox-a',config.secret);
 assert.equal(verify(ticket,key,1001).aud,'https://run.example');assert.equal(verify(ticket,key,1090),null);
 assert.equal(verify(ticket,runtimeSecret(identity,'sandbox-b',config.secret),1001),null);
});
test('HTTP access verifies before setting a session; locked session API never allocates or exposes runtime URLs',async()=>{
 const oldHash=process.env.ROBOT_ACCESS_PASSWORD_HASH,oldSecret=process.env.ROBOT_ACCESS_SECRET;
 process.env.ROBOT_ACCESS_PASSWORD_HASH=hash;process.env.ROBOT_ACCESS_SECRET=config.secret;
 try{
  let res=response();await session({method:'GET',headers},res);assert.equal(res.body.requiresPassword,true);assert.equal(res.body.session,null);
  for(const method of ['POST','DELETE']){res=response();await session({method,headers},res);assert.equal(res.code,401);}
  res=response();await access({method:'POST',headers,body:{password:'wrong'}},res);assert.equal(res.code,401);assert.equal(res.headers['Set-Cookie'],undefined);
  res=response();await access({method:'POST',headers:{...headers,origin:'https://evil.example'},body:{password}},res);assert.equal(res.code,403);
  res=response();await access({method:'POST',headers,body:{password}},res);assert.equal(res.code,200);assert.ok(authorized(res.headers['Set-Cookie'],identity,config));
  delete process.env.ROBOT_ACCESS_PASSWORD_HASH;res=response();await session({method:'POST',headers},res);assert.equal(res.code,503);
 }finally{if(oldHash===undefined)delete process.env.ROBOT_ACCESS_PASSWORD_HASH;else process.env.ROBOT_ACCESS_PASSWORD_HASH=oldHash;if(oldSecret===undefined)delete process.env.ROBOT_ACCESS_SECRET;else process.env.ROBOT_ACCESS_SECRET=oldSecret;}
});
