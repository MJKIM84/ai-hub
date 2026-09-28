"""Anonymous visitor isolation and BYOK lifecycle; provider replies are protocol fakes.

These tests make no paid/live API calls and are not evidence of model quality.
"""
import io
import json
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from urllib.error import HTTPError

import pytest
from fastapi.testclient import TestClient
from robot_platform.visitor_api import create_personal_app, VisitorRegistry, COOKIE
from robot_platform.personal_provider import PersonalPlanningProvider
from robot_platform.assistant_provider import ProviderError
from robot_platform import assistant_provider as api_module
from robot_platform import claude_provider as claude_module

HEADERS = {'X-Robot-Request':'1'}


@pytest.fixture
def site(monkeypatch):
    monkeypatch.setenv('OPENAI_API_KEY', 'operator-key-must-never-be-used')
    monkeypatch.setenv('ANTHROPIC_API_KEY', 'operator-claude-must-never-be-used')
    registry=VisitorRegistry(max_visitors=4)
    app=create_personal_app(registry=registry)
    with TestClient(app, base_url='http://127.0.0.1', headers=HEADERS) as owner:
        yield app, registry, owner


def connect(client, key='visitor-key', **extra):
    return client.put('/api/assistant/settings', json={'provider':'api',
        'base_url':'https://api.openai.com/v1', 'model':'test-model',
        'api_key':key, 'consent':True, **extra})


def fake_openai(monkeypatch, *, error=None, during=None):
    calls=[]
    class Transport:
        def open(self, request, timeout):
            body=json.loads(request.data) if request.data else None
            calls.append((request.full_url, dict(request.header_items()), body))
            if during: during()
            if error: raise error
            if body is None:
                result={'data':[{'id':'test-model'}]}
            else:
                system=body['messages'][0]['content']
                if system.startswith('Extract draft'):
                    answer={'drafts_json':'[]','notes':'검토 필요'}
                elif system.startswith('Inspect this'):
                    answer={'candidates_json':'[]','labels_json':'[]','notes':'원본 대조 필요'}
                else:
                    answer={'answer':'기능 설명', 'references':['document:manual'],
                        'intent':{'kind':'question','goal':'질문','tasks':[]}}
                result={'id':'message-test','choices':[{'finish_reason':'stop','message':{'content':json.dumps(answer)}}]}
            return io.BytesIO(json.dumps(result).encode())
    monkeypatch.setattr(api_module,'build_opener',lambda *args: Transport())
    return calls


def test_visitors_isolate_credentials_projects_plans_and_history(site, monkeypatch):
    app, registry, a=site
    assert a.get('/api/project').status_code==401
    assert a.get('/api/session').json()['mode']=='personal_api'
    with TestClient(app, base_url='http://127.0.0.1', headers=HEADERS) as b:
        b.get('/api/session')
        assert a.cookies.get(COOKIE)!=b.cookies.get(COOKIE)
        assert not a.get('/api/assistant/settings').json()['has_key']
        assert not b.get('/api/assistant/settings').json()['has_key']
        assert connect(a).status_code==200
        assert not b.get('/api/assistant/settings').json()['has_key']
        ap=a.get('/api/project').json();bp=b.get('/api/project').json()
        ap['name']='Only visitor A'
        assert a.put('/api/project',json=ap).status_code==200
        assert b.get('/api/project').json()['name']==bp['name']
        assert a.post('/api/projects/save',json={'project':ap}).status_code==200
        assert b.get('/api/projects').json()==[]
        draft=a.post('/api/plans',json={'project':ap,'intent':{'kind':'question','goal':'question','tasks':[]}})
        assert draft.status_code==200, draft.text
        assert b.get('/api/plans/'+draft.json()['id']).status_code==404
        fake_openai(monkeypatch)
        models=a.post('/api/assistant/models/refresh').json()
        assert models['status']=='key_verified' and models['last_success'] is None
        assert b.post('/api/assistant/models/refresh').status_code==422
        for item in registry.visitors.values():
            for file in __import__('pathlib').Path(item.folder.name).rglob('*.json'):
                assert 'visitor-key' not in file.read_text()
        assert 'visitor-key' not in a.get('/api/assistant/settings').text
        assert 'operator-key' not in a.get('/api/assistant/settings').text


def test_model_connection_requires_consent_and_restricts_destinations(site):
    app, registry, c=site;c.get('/api/session')
    for extra in ({'consent':False},{'provider':'codex'}, {'base_url':'http://127.0.0.1:8000'},
                  {'base_url':'https://api.openai.com.evil.test/v1'}, {'base_url':'https://api.openai.com/v1?key=x'},
                  {'require_key':False}, {'api_key':'bad\nheader'}):
        r=connect(c,**extra)
        assert r.status_code==422, r.text
    assert c.post('/api/assistant/login').status_code==422
    assert not c.get('/api/assistant/settings').json()['has_key']
    assert connect(c).status_code==200
    assert c.put('/api/assistant/settings',json={'provider':'claude','model':'x'}).status_code==422
    assert connect(c,provider='claude',base_url='https://api.openai.com/v1').status_code==200
    p=next(iter(registry.visitors.values())).app.state.host.plan_service.provider
    assert p.api.key=='' and p.claude.key=='visitor-key'


def test_disconnect_and_expiry_keep_plans_but_remove_key(site):
    _, registry, c=site;c.get('/api/session');connect(c)
    before=c.get('/api/project').json()
    p=next(iter(registry.visitors.values())).app.state.host.plan_service.provider
    p.expires_at=time.time()-1
    registry.reap()
    state=c.get('/api/assistant/settings').json()
    assert state['status']=='key_expired' and not state['has_key']
    assert c.get('/api/project').json()==before
    connect(c)
    assert c.post('/api/assistant/disconnect').status_code==200
    assert not c.get('/api/assistant/settings').json()['has_key']
    assert c.get('/api/project').json()==before


def test_session_cookie_origin_expiry_and_capacity(site):
    app, registry, c=site
    assert c.get('/api/session',headers={'Origin':'https://evil.test'}).status_code==403
    r=c.get('/api/session')
    assert 'HttpOnly' in r.headers['set-cookie'] and 'SameSite=strict' in r.headers['set-cookie']
    assert c.put('/api/assistant/settings',json={},headers={'Origin':'https://evil.test'}).status_code==403
    item=next(iter(registry.visitors.values())); path=item.folder.name
    item.created=time.time()-registry.ttl-1
    assert c.get('/api/project').status_code==401
    registry.reap()
    assert not __import__('pathlib').Path(path).exists()
    c.get('/api/session')
    assert not c.get('/api/assistant/settings').json()['has_key']
    assert c.delete('/api/session').json()['ended']
    assert c.get('/api/project').status_code==401


def test_key_body_limit_uses_actual_bytes_and_no_cross_site_form(site):
    app, _, c=site;c.get('/api/session')
    assert c.put('/api/assistant/settings',content=b'x'*9000).status_code==413
    with TestClient(app,base_url='http://127.0.0.1') as other:
        other.cookies.update(c.cookies)
        assert other.post('/api/assistant/disconnect').status_code==403
        assert other.get('/api/session').status_code==403


def test_https_cookie_and_explicit_public_origin():
    registry=VisitorRegistry()
    app=create_personal_app(registry=registry,origins=['https://demo.example'])
    with TestClient(app,base_url='https://demo.example',headers=HEADERS) as c:
        r=c.get('/api/session')
        assert r.status_code==200 and 'Secure' in r.headers['set-cookie']
        assert c.post('/api/assistant/disconnect',headers={'Origin':'https://other.example'}).status_code==403
    with TestClient(create_personal_app(),base_url='https://unconfigured.example',headers=HEADERS) as c:
        assert c.get('/api/session').status_code==403


def test_provider_disconnect_fences_inflight_response(tmp_path,monkeypatch):
    p=PersonalPlanningProvider(tmp_path)
    p.configure({'provider':'api','model':'test-model','api_key':'visitor-key','consent':True})
    entered=threading.Event();release=threading.Event()
    def during(): entered.set();assert release.wait(3)
    fake_openai(monkeypatch,during=during)
    project={'robots':[],'environment':{'elements':[]}}
    with ThreadPoolExecutor() as pool:
        pending=pool.submit(p.interpret,project,'질문',[])
        assert entered.wait(3)
        p.disconnect();release.set()
        with pytest.raises(ProviderError): pending.result()
    assert not p.settings()['has_key'] and p.last_success is None


def test_openai_ontology_document_and_image_contracts(tmp_path,monkeypatch):
    p=PersonalPlanningProvider(tmp_path)
    p.configure({'provider':'api','model':'test-model','api_key':'visitor-key','consent':True})
    calls=fake_openai(monkeypatch)
    project={'robots':[],'environment':{'elements':[]}}
    r=p.interpret(project,'질문',[],ontology={'capabilities':[{'evidence':{'document_id':'manual'}}]})
    assert r['references']==['document:manual']
    assert calls[-1][1]['Authorization']=='Bearer visitor-key'
    doc={'id':'manual','title':'t','text':'document text','model_id':'spot','version':'1'}
    draft=p.extract_manual(doc)
    assert draft['model_execution']['provider']=='api'
    image=tmp_path/'floor.png';image.write_bytes(b'protocol-only')
    visual=p.inspect_floorplan(image,20,30)
    image_block=calls[-1][2]['messages'][1]['content'][0]
    assert image_block['type']=='image_url'
    assert visual['model_execution']['provider']=='api'
    assert 'visitor-key' not in json.dumps(visual)


@pytest.mark.parametrize('code',[401,403,429,500])
def test_provider_error_does_not_leak_key_or_fallback(site,monkeypatch,code):
    _,_,c=site;c.get('/api/session');connect(c)
    calls=fake_openai(monkeypatch,error=HTTPError('url',code,'visitor-key',{},None))
    r=c.post('/api/assistant/models/refresh')
    assert r.status_code==422 and 'visitor-key' not in r.text
    assert len(calls)==1 and c.get('/api/assistant/settings').json()['provider']=='api'


def test_request_rate_limit_prevents_unbounded_provider_calls(site,monkeypatch):
    _,_,c=site;c.get('/api/session');connect(c);calls=fake_openai(monkeypatch)
    for _ in range(10): assert c.post('/api/assistant/models/refresh').status_code==200
    assert c.post('/api/assistant/models/refresh').status_code==429
    assert len(calls)==10


def test_malformed_credential_body_is_not_reflected(site):
    _,_,c=site;c.get('/api/session')
    r=c.put('/api/assistant/settings',json='a-misplaced-private-key')
    assert r.status_code==422 and 'a-misplaced-private-key' not in r.text


def test_personal_chat_uses_own_key_keeps_question_unexecuted_and_preserves_plan_on_error(site,monkeypatch):
    _,registry,c=site;c.get('/api/session');connect(c)
    calls=fake_openai(monkeypatch)
    before=c.get('/api/state').json()
    project=c.get('/api/project').json()
    response=c.post('/api/assistant/chat',json={'project':project,'message':'가능한 기능을 설명해줘','mode':'question'})
    assert response.status_code==200,response.text
    assert calls[0][1]['Authorization']=='Bearer visitor-key'
    after=c.get('/api/state').json()
    assert after['run_id']==before['run_id'] and after['status']=='paused'
    saved=c.get('/api/plans').json()
    fake_openai(monkeypatch,error=HTTPError('url',429,'not copied',{},None))
    rejected=c.post('/api/assistant/chat',json={'project':project,'message':'다시 설명해줘'})
    assert rejected.status_code==422
    assert c.get('/api/plans').json()==saved
    assert c.get('/api/state').json()['run_id']==before['run_id']


def test_model_selection_preserves_verified_catalog(tmp_path,monkeypatch):
    p=PersonalPlanningProvider(tmp_path)
    p.configure({'provider':'api','api_key':'visitor-key','consent':True})
    fake_openai(monkeypatch)
    assert p.refresh_models()['connection_verified']
    state=p.configure({'provider':'api','model':'test-model'})
    assert state['connection_verified'] and state['models'] and state['configured']
    assert state['last_success'] is None
