import time
import pytest
from fastapi.testclient import TestClient
from robot_platform.cloud import create_cloud_app
from robot_platform.entry_gate import sign

KEY='a'*64
ORIGIN='https://run.example'

def setup(monkeypatch):
    monkeypatch.setenv('ROBOT_PUBLIC_ORIGINS',ORIGIN)
    monkeypatch.setenv('ROBOT_ENTRY_REQUIRED','1')
    monkeypatch.setenv('ROBOT_ENTRY_SECRET',KEY)
    return create_cloud_app()

def ticket(**values):
    return sign(dict(kind='handoff',aud=ORIGIN,exp=time.time()+90,nonce='b'*32,**values),KEY)

def test_runtime_key_is_required_when_gate_enabled(monkeypatch):
    monkeypatch.setenv('ROBOT_PUBLIC_ORIGINS',ORIGIN)
    monkeypatch.setenv('ROBOT_ENTRY_REQUIRED','1')
    monkeypatch.delenv('ROBOT_ENTRY_SECRET',raising=False)
    with pytest.raises(ValueError,match='signing key'):create_cloud_app()

def test_direct_runtime_url_and_api_are_locked_until_single_use_handoff(monkeypatch):
    app=setup(monkeypatch)
    with TestClient(app,base_url=ORIGIN) as c:
        assert c.get('/healthz').json()['access_required'] is True
        assert '비밀번호' in c.get('/').text
        for route in ['/api/session','/api/project','/api/state','/api/state/stream','/assets/app.js']:
            assert c.get(route,headers={'X-Robot-Request':'1'}).status_code==401
        assert not app.state.visitors.visitors
        h={'Origin':ORIGIN}
        assert c.post('/access/enter',headers=h,json={'ticket':'invalid'}).status_code==401
        valid=ticket()
        assert c.post('/access/enter',headers={'Origin':'https://evil.example'},json={'ticket':valid}).status_code==403
        response=c.post('/access/enter',headers=h,json={'ticket':valid})
        assert response.status_code==200
        assert all(x in response.headers['set-cookie'] for x in ['HttpOnly','Secure','SameSite=strict'])
        assert c.post('/access/enter',headers=h,json={'ticket':valid}).status_code==401
        assert c.get('/api/session',headers={'X-Robot-Request':'1'}).status_code==200
        assert len(c.get('/api/project').json()['robots'])==5
        with TestClient(app,base_url=ORIGIN) as outsider:
            assert outsider.get('/api/state').status_code==401
        c.cookies.clear()
        for data in [dict(kind='handoff',aud=ORIGIN,exp=time.time()-1,nonce='c'*32),dict(kind='handoff',aud='https://other.example',exp=time.time()+90,nonce='c'*32)]:
            assert c.post('/access/enter',headers=h,json={'ticket':sign(data,KEY)}).status_code==401
        assert c.get('/api/state').status_code==401
