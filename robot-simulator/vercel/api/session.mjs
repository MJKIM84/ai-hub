import { accessSettings, authorized } from '../lib/access.mjs';
import { COOKIE, identity, newIdentity, settings, allowedOrigin, publicSession } from '../lib/session-policy.mjs';
import { findSession, loadSession, launch, stop } from '../lib/runtime.mjs';

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  const send = (status, body) => res.status(status).json(body);
  if (!['GET', 'POST', 'DELETE'].includes(req.method)) return send(405, {error: '지원하지 않는 요청입니다.'});
  if (req.method !== 'GET' && !allowedOrigin(req)) return send(403, {error: '시뮬레이션 시작 화면에서 다시 시도해 주세요.'});
  const access = accessSettings();
  let token = identity(req.headers.cookie);
  if (!token) {
    if (req.method !== 'GET') return send(401, {error: '페이지를 새로고침한 뒤 다시 시작해 주세요.'});
    token = newIdentity();
    res.setHeader('Set-Cookie', `${COOKIE}=${token}; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=86400`);
    return send(200, {session: null, minutes: settings().minutes, requiresPassword:true});
  }
  if (!access) return send(503, {error:'입장 설정을 준비 중입니다. 잠시 후 다시 시도해 주세요.'});
  if (!authorized(req.headers.cookie,token,access)) {
    if (req.method === 'GET') return send(200,{session:null,minutes:settings().minutes,requiresPassword:true});
    return send(401,{error:'비밀번호를 먼저 확인해 주세요.',requiresPassword:true});
  }
  try {
    if (req.method === 'GET') {
      const {item} = await findSession(token);
      const sandbox = item ? await loadSession(item) : null;
      return send(200, {session: sandbox ? publicSession(sandbox) : null, minutes: settings().minutes});
    }
    if (req.method === 'DELETE') { await stop(token); return send(200, {ended: true}); }
    const result = await launch(token, {...settings(), access});
    return send(result.status || 200, result.error ? {error: result.error} : {session: result});
  } catch (error) {
    // Do not expose provider responses, tokens, environment or uploaded data in public errors/logs.
    console.error('Sandbox operation failed', {status: error?.response?.status, type: error?.name});
    return send(503, {error: '실행 공간 연결에 실패했습니다. 잠시 후 다시 시도해 주세요.'});
  }
}
