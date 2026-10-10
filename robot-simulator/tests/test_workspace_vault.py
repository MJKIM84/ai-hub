import base64
from copy import deepcopy
import hashlib
import json
import pytest
from fastapi.testclient import TestClient
from robot_platform.api import create_app
from robot_platform.workspace_vault import WorkspaceVault, capture, validate_bundle
from robot_platform.runtime import Session
from robot_platform.domain import Project


def bundle():
    return dict(format='robot-workspace-v1',project=Project().model_dump(),files={},recording={},semantics='historical')


def test_reopen_versions_roles_and_conflicting_writes(tmp_path):
    path=tmp_path/'permanent.db';store=WorkspaceVault(path)
    first=store.save('owner',bundle());key=first['id']
    reopened=WorkspaceVault(path)
    assert reopened.read('owner',key)['revision']==1
    assert reopened.list('other')==[]
    with pytest.raises(PermissionError):reopened.read('other',key)
    reopened.grant('owner',key,'reader','reader')
    assert reopened.read('reader',key)['role']=='reader'
    with pytest.raises(PermissionError):reopened.read('reader',key,execute=True)
    with pytest.raises(PermissionError):reopened.save('reader',bundle(),key,1)
    reopened.grant('owner',key,'editor','editor')
    assert reopened.save('editor',bundle(),key,1)['revision']==2
    with pytest.raises(ValueError,match='최신'):reopened.save('owner',bundle(),key,1)
    assert reopened.read('owner',key,1)['revision']==1
    with pytest.raises(PermissionError):reopened.grant('editor',key,'other','editor')


@pytest.mark.parametrize('name',['../key.json','/tmp/key.json','plans/provider-settings.json','plans/ontology/../../token.json','projects/x/../1.json'])
def test_forbidden_archive_paths(name):
    b=bundle();b['files'][name]=base64.b64encode(b'{}').decode()
    with pytest.raises(ValueError):validate_bundle(b)


def test_capture_excludes_auth_and_provider_settings(tmp_path):
    plans=tmp_path/'plans';plans.mkdir()
    for name in ('assistant-settings.json','planning-provider.json','credentials.json'):
        (plans/name).write_text('{"api_key":"must-not-leave"}')
    ontology=plans/'ontology';ontology.mkdir();(ontology/('a'*32+'.json')).write_text('{"quote":"manual"}')
    s=Session(Project());b=capture(tmp_path,s)
    assert len(b['files'])==1
    assert 'must-not-leave' not in json.dumps(b)


def test_account_api_restart_restore_is_paused_and_never_replays_approval(tmp_path,monkeypatch):
    accounts=tmp_path/'accounts.json';accounts.write_text(json.dumps([
        dict(subject='alice',sha256=hashlib.sha256(b'a'*40).hexdigest()),
        dict(subject='bob',sha256=hashlib.sha256(b'b'*40).hexdigest())]))
    monkeypatch.setenv('ROBOT_VAULT_DB',str(tmp_path/'durable'/'vault.db'))
    monkeypatch.setenv('ROBOT_VAULT_ACCOUNTS_FILE',str(accounts))
    a={'Authorization':'Bearer '+'a'*40};b={'Authorization':'Bearer '+'b'*40}
    first=TestClient(create_app(tmp_path/'first'))
    assert first.get('/api/vault').status_code==401
    saved=first.post('/api/vault',headers=a,json={});assert saved.status_code==200,saved.text
    key=saved.json()['id']
    assert first.post(f'/api/vault/{key}/share',headers=a,json={'subject':'bob','role':'reader'}).status_code==200
    fresh=TestClient(create_app(tmp_path/'new-server'))
    assert fresh.get('/api/vault',headers=a).json()['spaces'][0]['id']==key
    assert fresh.post(f'/api/vault/{key}/restore',headers=b).status_code==403
    restored=fresh.post(f'/api/vault/{key}/restore',headers=a)
    assert restored.status_code==200,restored.text
    assert restored.json()['status']=='paused'
    assert restored.json()['project']['revision']==fresh.app.state.host.session.project.revision
    assert fresh.app.state.host.session.time==0
    assert fresh.app.state.host.plan_service.active is None
    first.close();fresh.close()
