"""Anonymous, isolated personal-API workspaces; local owner data is never mounted."""
from __future__ import annotations
import asyncio
from collections import deque
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
import hashlib
import os
from pathlib import Path
import secrets
import tempfile
import threading
import time
from urllib.parse import urlsplit

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse, FileResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.gzip import GZipMiddleware

from .api import create_app
from .personal_provider import PersonalPlanningProvider

COOKIE = 'rop_visitor'


@dataclass
class Visitor:
    app: object
    folder: object
    created: float
    workspace_id: str
    active: int = 0
    closing: bool = False
    calls: deque = field(default_factory=deque)
    model_calls: deque = field(default_factory=deque)


class VisitorRegistry:
    def __init__(self, *, ttl=14400, key_ttl=1800, max_visitors=8, api_urls=('https://api.openai.com/v1',), initial_template='hotel'):
        self.ttl, self.key_ttl, self.max_visitors = ttl, key_ttl, max_visitors
        self.api_urls = api_urls
        self.initial_template = initial_template
        self.visitors = {}
        self.lock = threading.RLock()
        self.model_active = 0

    def create(self):
        with self.lock:
            self.reap()
            if len(self.visitors) >= self.max_visitors:
                return None, None
            folder = tempfile.TemporaryDirectory(prefix='robot-visitor-')
            try:
                app = create_app(Path(folder.name), initial_template=self.initial_template, provider_factory=lambda p:
                    PersonalPlanningProvider(p, api_urls=self.api_urls, key_ttl=self.key_ttl))
            except Exception:
                folder.cleanup()
                raise
            token = secrets.token_urlsafe(32)
            item = Visitor(app, folder, time.time(), secrets.token_hex(8))
            self.visitors[hashlib.sha256(token.encode()).hexdigest()] = item
            app.state.host.thread.start()
            return token, item

    def get(self, token):
        with self.lock:
            item = self.visitors.get(hashlib.sha256((token or '').encode()).hexdigest())
            if item and not item.closing and time.time() < item.created + self.ttl:
                return item
        return None

    def retire(self, item):
        item.closing = True
        item.app.state.host.stop.set()
        item.app.state.host.plan_service.provider.close()

    def reap(self):
        with self.lock:
            for identity, item in list(self.visitors.items()):
                item.app.state.host.plan_service.provider.expire()
                if time.time() >= item.created + self.ttl:
                    self.retire(item)
                if item.closing and not item.active:
                    item.app.state.host.thread.join(timeout=2)
                    if not item.app.state.host.thread.is_alive():
                        item.folder.cleanup()
                        del self.visitors[identity]

    def close(self):
        with self.lock:
            for item in self.visitors.values(): self.retire(item)
            self.reap()


class VisitorMiddleware:
    def __init__(self, app, registry, origins):
        self.app, self.registry = app, registry
        self.origins = set(origins)

    async def __call__(self, scope, receive, send):
        if scope['type'] != 'http' or not scope['path'].startswith('/api/'):
            return await self.app(scope, receive, send)
        req = Request(scope, receive)
        async def reply(status, message):
            await JSONResponse({'detail': message}, status_code=status,
                headers={'Cache-Control':'no-store'})(scope, receive, send)
        # Public deployment must declare exact HTTPS origins; loopback works without extra setup.
        origin = req.headers.get('origin')
        host = urlsplit(str(req.url)).hostname
        effective_origin = f'{req.url.scheme}://{req.url.netloc}'
        allowed = self.origins or ({effective_origin} if host in ('localhost','127.0.0.1','::1') else set())
        if (effective_origin not in allowed or (origin and origin not in allowed)
                or req.headers.get('sec-fetch-site') == 'cross-site'):
            return await reply(403, '이 사이트에서 시작한 요청만 허용합니다.')
        if scope['method'] not in ('GET','HEAD') and not origin and req.headers.get('x-robot-request') != '1':
            return await reply(403, '요청 출처를 확인할 수 없습니다. 앱에서 다시 시도하세요.')
        async def safe_send(message):
            if message['type'] == 'http.response.start':
                message['headers'] = list(message.get('headers', [])) + [
                    (b'cache-control',b'no-store'), (b'x-content-type-options',b'nosniff')]
            await send(message)
        token = req.cookies.get(COOKIE)
        item = self.registry.get(token)
        if req.url.path == '/api/session' and scope['method'] == 'GET':
            if req.headers.get('x-robot-request') != '1':
                return await reply(403, '앱에서 체험 공간을 열어주세요.')
            if item is None:
                token, item = await asyncio.to_thread(self.registry.create)
                if item is None:
                    return await reply(503, '체험 공간이 모두 사용 중입니다. 잠시 후 다시 시도하세요.')
            response = JSONResponse({'mode':'personal_api', 'workspace_id':item.workspace_id,
                'expires_at':item.created+self.registry.ttl, 'key_ttl_seconds':self.registry.key_ttl})
            response.set_cookie(COOKIE, token, httponly=True, secure=req.url.scheme=='https',
                samesite='strict', max_age=max(1,int(item.created+self.registry.ttl-time.time())), path='/')
            return await response(scope, receive, safe_send)
        if item is None:
            return await reply(401, '체험 시간이 끝났거나 서버가 다시 시작됐습니다. 필요한 결과를 내려받고 새로고침해 새 체험 공간을 여세요.')
        if req.url.path == '/api/session' and scope['method'] == 'DELETE':
            with self.registry.lock: self.registry.retire(item)
            await asyncio.to_thread(self.registry.reap)
            response = JSONResponse({'ended':True})
            response.delete_cookie(COOKIE, path='/')
            return await response(scope, receive, safe_send)
        model_call = (req.url.path in ('/api/assistant/chat','/api/assistant/models/refresh')
                      or req.url.path.endswith(('/extract/model','/inspect')))
        mutation = scope['method'] not in ('GET','HEAD')
        with self.registry.lock:
            now = time.time()
            for calls in (item.calls, item.model_calls):
                while calls and calls[0] < now-60: calls.popleft()
            limited = (item.active >= 12 or (mutation and len(item.calls)>=60)
                       or (model_call and (len(item.model_calls)>=10 or self.registry.model_active>=2)))
            if not limited:
                item.active += 1
                if mutation: item.calls.append(now)
                if model_call:
                    item.model_calls.append(now)
                    self.registry.model_active += 1
        if limited: return await reply(429, '요청이 많습니다. 진행 중인 작업이 끝난 뒤 잠시 후 다시 시도하세요.')
        try:
            item.app.state.host.plan_service.provider.expire()
            # Count actual bytes before parsers allocate buffers; Content-Length is not trusted.
            limit = 8192 if req.url.path == '/api/assistant/settings' else 20_000_000
            chunks = bytearray()
            if mutation:
                try:
                    async with asyncio.timeout(30):
                        async for chunk in req.stream():
                            if len(chunks) + len(chunk) > limit:
                                return await reply(413, '요청이 너무 큽니다. 파일 또는 내용을 줄여주세요.')
                            chunks.extend(chunk)
                except TimeoutError:
                    return await reply(408, '업로드 시간이 초과됐습니다. 다시 시도하세요.')
            sent = False
            async def buffered_receive():
                nonlocal sent
                if not sent:
                    sent = True
                    return {'type':'http.request', 'body':bytes(chunks), 'more_body':False}
                return await receive()
            await item.app(scope, buffered_receive if mutation else receive, safe_send)
        finally:
            with self.registry.lock:
                item.active -= 1
                if model_call: self.registry.model_active -= 1
            await asyncio.to_thread(self.registry.reap)


def create_personal_app(*, registry=None, origins=None):
    registry = registry or VisitorRegistry(api_urls=tuple(filter(None,
        (url.strip().rstrip('/') for url in os.getenv('ROBOT_PERSONAL_API_URLS','https://api.openai.com/v1').split(',')))))
    origins = origins if origins is not None else tuple(filter(None, os.getenv('ROBOT_PUBLIC_ORIGINS','').split(',')))
    if any(not origin.startswith('https://') for origin in origins):
        raise ValueError('공개 개인 API 모드의 사이트 주소는 HTTPS여야 합니다.')
    @asynccontextmanager
    async def lifespan(app):
        async def sweep():
            while True:
                await asyncio.sleep(15)
                await asyncio.to_thread(registry.reap)
        task = asyncio.create_task(sweep())
        try: yield
        finally:
            task.cancel()
            try: await task
            except asyncio.CancelledError: pass
            await asyncio.to_thread(registry.close)
    app = FastAPI(lifespan=lifespan, docs_url=None, redoc_url=None, openapi_url=None)
    app.state.visitors = registry
    app.add_middleware(VisitorMiddleware, registry=registry, origins=origins)
    # Scene meshes are large; compress at the outer layer so visitor-routed
    # responses are included as well as the static shell.
    app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=3)
    @app.get('/healthz')
    def health():
        # Hosting probes must not allocate a robot world or a visitor session.
        return JSONResponse({'status':'ok', 'mode':'personal_api'}, headers={'Cache-Control':'no-store'})
    dist = Path(__file__).resolve().parents[2]/'web/dist'
    if (dist/'assets').exists(): app.mount('/assets', StaticFiles(directory=dist/'assets'), name='assets')
    @app.get('/{path:path}')
    def index(path:str):
        return FileResponse(dist/'index.html', headers={'Cache-Control':'no-cache'})
    return app
