"""Gate a public sandbox with a short-lived, single-use launcher handoff.

No administrator password is sent to or stored in the runtime image. Only the
launcher can mint handoffs using the per-runtime signing key supplied at boot.
"""
import base64
import hashlib
import hmac
import json
import re
import secrets
import threading
import time

from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse

COOKIE = '__Host-rop_runtime'
LAUNCHER = 'https://robot-lab-seven.vercel.app/'


def sign(data, secret):
    body = base64.urlsafe_b64encode(json.dumps(data, separators=(',', ':')).encode()).decode().rstrip('=')
    mac = base64.urlsafe_b64encode(hmac.new(secret.encode(), body.encode(), hashlib.sha256).digest()).decode().rstrip('=')
    return body + '.' + mac


def verify(value, secret, now):
    if not isinstance(value, str) or len(value) > 2048:
        return None
    try:
        body, mac = value.split('.')
        if not re.fullmatch(r'[A-Za-z0-9_-]+', body) or not re.fullmatch(r'[A-Za-z0-9_-]{43}', mac):
            return None
        expected = base64.urlsafe_b64encode(hmac.new(secret.encode(), body.encode(), hashlib.sha256).digest()).decode().rstrip('=')
        if not hmac.compare_digest(expected, mac):
            return None
        data = json.loads(base64.urlsafe_b64decode(body + '=' * (-len(body) % 4)))
        if not isinstance(data, dict) or not isinstance(data.get('exp'), (int, float)) or data['exp'] <= now:
            return None
        return data
    except (ValueError, TypeError, UnicodeError):
        return None


class EntryGate:
    def __init__(self, app, secret, origins, ttl=1800):
        self.app, self.secret, self.origins, self.ttl = app, secret, set(origins), ttl
        self.used = {}
        self.lock = threading.Lock()

    async def __call__(self, scope, receive, send):
        if scope['type'] not in ('http', 'websocket'):
            return await self.app(scope, receive, send)
        req = Request(scope) if scope['type'] == 'http' else None
        if req is None:
            return await send({'type':'websocket.close', 'code':1008})
        now = time.time()
        origin = f'{req.url.scheme}://{req.url.netloc}'
        headers = {'Cache-Control':'no-store','Referrer-Policy':'no-referrer','X-Content-Type-Options':'nosniff','X-Frame-Options':'DENY'}
        async def reply(status, detail):
            return await JSONResponse({'detail':detail},status_code=status,headers=headers)(scope,receive,send)
        if scope['path'] == '/healthz' and scope['method'] == 'GET':
            return await JSONResponse({'status':'ok','mode':'personal_api','access_required':True},headers=headers)(scope,receive,send)
        if origin not in self.origins:
            return await reply(403,'허용되지 않은 시뮬레이터 주소입니다.')
        if scope['path'] == '/access/enter':
            if (scope['method'] != 'POST' or req.headers.get('origin') != origin
                    or req.headers.get('sec-fetch-site') == 'cross-site'
                    or not req.headers.get('content-type','').startswith('application/json')):
                return await reply(403,'시뮬레이션 시작 화면에서 다시 입장해 주세요.')
            raw = bytearray()
            while True:
                part = await receive()
                if part['type'] == 'http.disconnect': return
                raw.extend(part.get('body',b''))
                if len(raw) > 4096: return await reply(413,'입장 요청이 너무 큽니다.')
                if not part.get('more_body',False): break
            try:
                payload = json.loads(raw)
                ticket = verify(payload.get('ticket'),self.secret,now) if isinstance(payload,dict) else None
            except (ValueError,UnicodeError): ticket = None
            if (not ticket or ticket.get('kind') != 'handoff' or ticket.get('aud') != origin
                    or ticket['exp'] > now + 120 or not re.fullmatch(r'[a-f0-9]{32}',str(ticket.get('nonce','')))):
                return await reply(401,'입장 요청이 만료되었거나 유효하지 않습니다. 시작 화면에서 다시 입장해 주세요.')
            with self.lock:
                self.used = {key:expiry for key,expiry in self.used.items() if expiry > now}
                if ticket['nonce'] in self.used: accepted = False
                else:
                    self.used[ticket['nonce']] = ticket['exp']
                    accepted = True
            if not accepted: return await reply(401,'이미 사용한 입장 요청입니다. 시작 화면에서 다시 입장해 주세요.')
            response = JSONResponse({'authenticated':True},headers=headers)
            response.set_cookie(COOKIE,sign({'kind':'runtime','aud':origin,'exp':int(now)+self.ttl},self.secret),
                                httponly=True,secure=True,samesite='strict',max_age=self.ttl,path='/')
            return await response(scope,receive,send)
        cookie = verify(req.cookies.get(COOKIE),self.secret,now)
        if scope['path'] != '/access/start' and cookie and cookie.get('kind') == 'runtime' and cookie.get('aud') == origin:
            return await self.app(scope,receive,send)
        if scope['path'] not in ('/', '/access/start') or scope['method'] != 'GET':
            return await reply(401,'비밀번호 확인이 필요합니다. 시뮬레이션 시작 화면에서 입장해 주세요.')
        nonce = secrets.token_urlsafe(16)
        headers['Content-Security-Policy'] = f"default-src 'none'; script-src 'nonce-{nonce}'; style-src 'unsafe-inline'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'"
        page = '''<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ROBOT LAB · 입장 확인</title><style>body{font:16px/1.7 system-ui;background:#f5f7fa;color:#182838;max-width:520px;margin:15vh auto;padding:24px}a{color:#175dd7}h1{font-size:26px}</style>
<h1>시뮬레이션 입장 확인</h1><p id="status" role="status">시작 화면에서 비밀번호를 입력해 주세요.</p><a href="''' + LAUNCHER + '''">시뮬레이션 시작 화면으로</a>
<script nonce="''' + nonce + '''">
const ticket=new URLSearchParams(location.hash.slice(1)).get('entry');
history.replaceState(null,'','/');
if(ticket){document.querySelector('#status').textContent='입장 확인 중…';fetch('/access/enter',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({ticket}),credentials:'same-origin'}).then(async r=>{if(!r.ok)throw Error((await r.json()).detail);location.replace('/');}).catch(e=>{document.querySelector('#status').textContent=e.message||'연결에 실패했습니다. 시작 화면에서 다시 시도해 주세요.';});}
</script></html>'''
        return await HTMLResponse(page,headers=headers)(scope,receive,send)
