import { identity, allowedOrigin } from '../lib/session-policy.mjs';
import { accessSettings, verifyPassword, accessCookie } from '../lib/access.mjs';

export default async function handler(req,res) {
  res.setHeader('Cache-Control','no-store');
  const send=(status,body)=>res.status(status).json(body);
  if(req.method!=='POST')return send(405,{error:'지원하지 않는 요청입니다.'});
  if(!allowedOrigin(req))return send(403,{error:'시뮬레이션 시작 화면에서 다시 시도해 주세요.'});
  const config=accessSettings();
  if(!config)return send(503,{error:'입장 설정을 준비 중입니다. 잠시 후 다시 시도해 주세요.'});
  const token=identity(req.headers.cookie);
  if(!token)return send(401,{error:'페이지를 새로고침한 뒤 다시 시도해 주세요.'});
  if(!req.headers['content-type']?.startsWith('application/json') || !req.body || Object.keys(req.body).some(k=>k!=='password'))
    return send(400,{error:'비밀번호를 입력해 주세요.'});
  if(!await verifyPassword(req.body.password,config))return send(401,{error:'비밀번호가 일치하지 않습니다. 다시 입력해 주세요.'});
  res.setHeader('Set-Cookie',accessCookie(token,config));
  return send(200,{authenticated:true});
}
