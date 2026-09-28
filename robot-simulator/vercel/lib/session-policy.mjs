import { createHash, randomBytes } from 'node:crypto';

export const COOKIE = '__Host-rop_launch';
export function identity(cookie = '') {
  const token = cookie.split(';').map(x => x.trim()).find(x => x.startsWith(`${COOKIE}=`))?.slice(COOKIE.length + 1);
  return token && /^[a-f0-9]{64}$/.test(token) ? token : null;
}
export const newIdentity = () => randomBytes(32).toString('hex');
export const ownerHash = token => createHash('sha256').update(token).digest('hex');
export function settings(env = process.env) {
  function number(key, fallback, min, max) {
    const n = Number(env[key] || fallback);
    if (!Number.isInteger(n) || n < min || n > max) throw new Error(`Invalid ${key}`);
    return n;
  }
  return {
    daily: number('ROBOT_DAILY_SESSIONS', 10, 1, 20),
    concurrent: number('ROBOT_CONCURRENT_SESSIONS', 2, 1, 4),
    minutes: number('ROBOT_SESSION_MINUTES', 30, 10, 30),
    snapshot: env.ROBOT_SNAPSHOT_ID,
  };
}
export const dayPrefix = (now = new Date()) => `rop-${now.toISOString().slice(0, 10).replaceAll('-', '')}-`;
export const slotNames = (count, now) => Array.from({length: count}, (_, i) => `${dayPrefix(now)}${String(i).padStart(2, '0')}`);
export const isActive = item => ['pending', 'running', 'stopping'].includes(item.status);
export function allowedOrigin(req) {
  const origin = req.headers.origin;
  return typeof origin === 'string' && origin === `https://${req.headers.host}` && req.headers['sec-fetch-site'] !== 'cross-site';
}
export const errorStatus = error => error?.response?.status;
export function publicSession(sandbox) {
  return {url: sandbox.domain(8000), expiresAt: sandbox.expiresAt?.toISOString() ?? null};
}
