"""Visitor-owned API credentials. No process environment credentials or Codex access."""
import threading
import time
from urllib.parse import urlsplit

from .assistant_provider import AssistantProvider, ProviderError
from .claude_provider import ClaudeProvider
from .planning_provider import PlanningProvider


class PersonalPlanningProvider(PlanningProvider):
    def __init__(self, folder, *, api_urls=('https://api.openai.com/v1',), key_ttl=1800):
        self.api = AssistantProvider(folder, use_environment=False)
        self.claude = ClaudeProvider(folder, use_environment=False)
        self.kind = 'api'
        self.allowed_urls = tuple(api_urls)
        for url in self.allowed_urls:
            parts = urlsplit(url)
            if parts.scheme != 'https' or not parts.hostname or parts.username or parts.password or parts.query or parts.fragment:
                raise ValueError('개인 API 모드에는 운영자가 허용한 HTTPS 주소가 필요합니다.')
        self.api.base_url = self.allowed_urls[0]
        self.api.require_key = True
        self.key_ttl = key_ttl
        self.expires_at = None
        self.expired = False
        self.guard = threading.RLock()

    def _selected(self):
        return self.claude if self.kind == "claude" else self.api

    def expire(self):
        with self.guard:
            if self.expires_at and time.time() >= self.expires_at:
                self.disconnect()
                self.expired = True

    def settings(self):
        with self.guard:
            self.expire()
            state = super().settings()
            if not state.get('has_key'):
                state['reason'] = '개인 API 키를 연결하면 사용 가능한 모델을 확인할 수 있습니다.'
            elif not state.get('model'):
                state['reason'] = '사용할 모델을 선택하고 적용하세요.'
            if self.expired:
                state.update(status='key_expired', reason='API 키 보관 시간이 끝났습니다. 키를 다시 연결하세요. 작업과 계획은 유지됩니다.')
            return dict(state, personal_api=True, key_storage='visitor_memory',
                        key_expires_at=self.expires_at, key_ttl_seconds=self.key_ttl,
                        api_urls=list(self.allowed_urls), automatic_api_fallback=False)

    def configure(self, value):
        with self.guard:
            self.expire()
            if not isinstance(value, dict) or set(value) - {'provider','base_url','model','api_key','workspace_id','consent'}:
                raise ProviderError('개인 연결 설정 형식을 확인하세요.')
            kind = value.get('provider')
            if kind not in ('api', 'claude'):
                raise ProviderError('개인 체험에서는 OpenAI 호환 API 또는 Claude API 키를 연결하세요.')
            for name in ('base_url', 'model', 'api_key', 'workspace_id'):
                if name in value and (not isinstance(value[name], str) or len(value[name]) > (512 if name == 'api_key' else 256)
                                      or any(ord(c) < 32 or ord(c) > 126 for c in value[name])):
                    raise ProviderError('연결 정보의 형식과 길이를 확인하세요.')
            url = value.get('base_url', self.api.base_url).rstrip('/')
            if kind == 'api' and url not in self.allowed_urls:
                raise ProviderError('운영자가 허용한 모델 서비스만 연결할 수 있습니다.')
            changing = kind != self.kind or (kind == 'api' and url != self.api.base_url)
            key = value.get('api_key')
            if changing and not key:
                raise ProviderError('새 모델 서비스의 개인 API 키를 입력하세요.')
            if key is not None and (not key.strip() or value.get('consent') is not True):
                raise ProviderError('API 키를 입력하고 사용료·전송 안내를 확인하세요.')
            if not key and not self._selected().key:
                raise ProviderError('개인 API 키를 입력하세요.')
            if self.api.operation.locked() or self.claude.operation.locked():
                raise ProviderError('응답이 끝날 때까지 기다리거나 연결을 해제하세요.')
            payload = {k:v for k,v in value.items() if k != 'consent'}
            if kind == 'api':
                payload.pop('provider', None)
                payload.pop('workspace_id', None)
                payload.update(base_url=url, require_key=True)
            else:
                payload.pop('base_url', None)
            target = self.api if kind == 'api' else self.claude
            target.configure(payload)
            if changing:
                (self.api if kind == 'claude' else self.claude).disconnect()
            self.kind = kind
            if key:
                self.expires_at = time.time() + self.key_ttl
                self.expired = False
            return self.settings()

    def login(self):
        raise ProviderError('개인 체험에서는 계정 비밀번호나 Codex 로그인을 받지 않습니다. API 키를 연결하세요.')

    def cancel_login(self, login_id):
        return self.login()

    def disconnect(self):
        with self.guard:
            busy = self.api.operation.locked() or self.claude.operation.locked()
            self.api.disconnect()
            self.claude.disconnect()
            self.expires_at = None
            self.expired = False
            return dict(self.settings(), remote_stop_confirmed=False if busy else None)

    def close(self):
        self.disconnect()
