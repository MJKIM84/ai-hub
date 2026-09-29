import { createHmac, randomBytes, scrypt, timingSafeEqual } from 'node:crypto';
import { promisify } from 'node:util';
const derive = promisify(scrypt);
export const ACCESS_COOKIE = '__Host-rop_access';
const TTL = 1800;
const version = config => createHmac('sha256',config.secret).update(config.hash).digest('hex');
export function accessSettings(env = process.env) {
  const hash = env.ROBOT_ACCESS_PASSWORD_HASH || '';
  const secret = env.ROBOT_ACCESS_SECRET || '';
  if (!/^scrypt:[a-f0-9]{32}:[a-f0-9]{128}$/.test(hash) || !/^[a-f0-9]{64}$/.test(secret)) return null;
  return {hash, secret};
}
export async function verifyPassword(password, config) {
  if (!config || typeof password !== 'string' || password.length < 1 || password.length > 128) return false;
  const [,salt,expected] = config.hash.split(':');
  const actual = await derive(password, Buffer.from(salt,'hex'),64);
  return timingSafeEqual(actual,Buffer.from(expected,'hex'));
}
export function sign(value, secret) {
  const body = Buffer.from(JSON.stringify(value)).toString('base64url');
  return `${body}.${createHmac('sha256',secret).update(body).digest('base64url')}`;
}
export function verify(value, secret, now = Date.now()/1000) {
  if (typeof value !== 'string' || value.length > 2048) return null;
  const [body,mac,...extra] = value.split('.');
  if (!body || !mac || extra.length) return null;
  const expected = createHmac('sha256',secret).update(body).digest('base64url');
  if (mac.length !== expected.length || !timingSafeEqual(Buffer.from(mac),Buffer.from(expected))) return null;
  try {const data=JSON.parse(Buffer.from(body,'base64url')); return Number.isFinite(data.exp) && data.exp > now ? data : null;}
  catch {return null;}
}
export function authorized(cookie, identity, config, now) {
  if (!config || !identity) return false;
  const value = (cookie || '').split(';').map(x=>x.trim()).find(x=>x.startsWith(`${ACCESS_COOKIE}=`))?.slice(ACCESS_COOKIE.length+1);
  const data=verify(value,config.secret,now);
  return data?.owner===identity && data?.kind==='entry' && data?.version===version(config);
}
export function accessCookie(identity, config, now=Date.now()/1000) {
  const value=sign({kind:'entry',owner:identity,version:version(config),exp:Math.floor(now)+TTL},config.secret);
  return `${ACCESS_COOKIE}=${value}; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=${TTL}`;
}
export function runtimeSecret(identity, name, secret) {
  if (!/^[a-f0-9]{64}$/.test(secret || '')) throw Error('Access configuration missing');
  return createHmac('sha256',secret).update(`runtime:${identity}:${name}`).digest('hex');
}
export function runtimeEntry(session, identity, name, config, now=Date.now()/1000) {
  const secret=runtimeSecret(identity,name,config.secret);
  const ticket=sign({kind:'handoff',aud:session.url,exp:Math.floor(now)+90,nonce:randomBytes(16).toString('hex')},secret);
  return {...session,url:`${session.url}/access/start#entry=${ticket}`};
}
