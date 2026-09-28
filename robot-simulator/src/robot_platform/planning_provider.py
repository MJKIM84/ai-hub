"""Explicit provider selection. Codex ChatGPT is the default; never fail over."""
import json
from .assistant_provider import AssistantProvider, ProviderError
from .codex_provider import CodexProvider
from .claude_provider import ClaudeProvider


class PlanningProvider:
    def __init__(self, folder):
        self.path = folder / 'planning-provider.json'
        self.kind = json.loads(self.path.read_text()).get('provider', 'codex') if self.path.exists() else 'codex'
        self.codex = CodexProvider(folder)
        self.api = AssistantProvider(folder)
        self.claude = ClaudeProvider(folder)

    def _selected(self):
        return {'codex': self.codex, 'claude': self.claude, 'api': self.api}[self.kind]

    @property
    def last_result(self):
        return getattr(self._selected(),"last_result",None)

    @property
    def last_success(self):
        return self._selected().last_success

    def settings(self):
        if self.kind == 'codex': return self.codex.settings()
        if self.kind == 'claude': return self.claude.settings()
        return dict(self.api.settings(), provider='api', automatic_api_fallback=False)

    def configure(self, value):
        # Legacy clients explicitly sending an API URL retain their chosen transport.
        kind = value.get('provider', 'api' if 'base_url' in value else 'codex')
        if kind not in ('codex', 'claude', 'api'): raise ProviderError('지원하지 않는 모델 연결 방식입니다.')
        if self.codex.operation.locked() or self.claude.operation.locked() or self.api.operation.locked():
            raise ProviderError('모델 응답을 먼저 완료하거나 취소하세요.')
        if kind == 'codex':
            result = self.codex.settings() if set(value) == {'provider'} else self.codex.configure(value)
        elif kind == 'claude': result = self.claude.configure(value)
        else: result = self.api.configure({k: v for k, v in value.items() if k != 'provider'})
        self.kind = kind
        self.path.write_text(json.dumps({'provider': kind}))
        return dict(result, provider=kind, automatic_api_fallback=False)

    def interpret(self, project, message, catalog, previous_intent=None, history=None, **kwargs):
        if self.kind == 'codex': return self.codex.interpret(project, message, catalog, previous_intent, history, **kwargs)
        if self.kind == 'claude':
            return self.claude.interpret(project, message, catalog, previous_intent, history, **kwargs)
        # Include provenance context for the explicitly chosen API provider too.
        context = dict(project, capability_ontology=kwargs.get('ontology'),spatial_ontology=kwargs.get('spatial'))
        return self.api.interpret(context, message, catalog, previous_intent, history)

    def extract_manual(self, document, *, processed_characters=0):
        if self.kind=='codex':
            return self.codex.extract_manual(document,processed_characters=processed_characters)
        if self.kind=='claude':
            return self.claude.extract_manual(document,processed_characters=processed_characters)
        return self.api.extract_manual(document,processed_characters=processed_characters)

    def inspect_floorplan(self, image_path, width, height):
        if self.kind=='codex': return self.codex.inspect_floorplan(image_path,width,height)
        if self.kind=='claude': return self.claude.inspect_floorplan(image_path,width,height)
        return self.api.inspect_floorplan(image_path,width,height)

    def login(self): return self.codex.login()
    def cancel_login(self, login_id): return self.codex.cancel_login(login_id)
    def refresh_models(self):
        if self.kind == 'codex': return self.codex.settings()
        return self._selected().refresh_models()
    def cancel(self): return self._selected().cancel() if hasattr(self._selected(), 'cancel') else {'cancelled': False}
    def disconnect(self):
        if self.kind == 'codex': raise ProviderError('로컬 Codex 로그인은 Codex에서 해제하세요.')
        return dict(self._selected().disconnect(), provider=self.kind)
    def close(self): self.codex.close(); self.claude.close(); self.api.close()
