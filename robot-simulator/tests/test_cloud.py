"""Deployment checks: no external model calls and no real robot connection."""
import pytest
from fastapi.testclient import TestClient

from robot_platform.cloud import create_cloud_app, public_origins


@pytest.fixture(autouse=True)
def clear_cloud_environment(monkeypatch):
    for key in ('ROBOT_PUBLIC_ORIGINS', 'RAILWAY_PUBLIC_DOMAIN', 'ROBOT_MAX_VISITORS',
                'ROBOT_VISITOR_TTL_SECONDS', 'ROBOT_KEY_TTL_SECONDS'):
        monkeypatch.delenv(key, raising=False)


def test_missing_public_origin_fails_before_allocating_world():
    with pytest.raises(ValueError, match='Set ROBOT_PUBLIC_ORIGINS'):
        create_cloud_app()


@pytest.mark.parametrize('origin', [
    'http://example.com', 'https://example.com/path', 'https://user:pass@example.com',
    'https://*.example.com', 'https://example.com?token=x', 'https://example.com#x',
    'https://example.com:not-a-port',
])
def test_invalid_public_origin_rejected(monkeypatch, origin):
    monkeypatch.setenv('ROBOT_PUBLIC_ORIGINS', origin)
    with pytest.raises(ValueError):
        create_cloud_app()


def test_railway_domain_and_explicit_override(monkeypatch):
    monkeypatch.setenv('RAILWAY_PUBLIC_DOMAIN', 'robot.example.up.railway.app')
    assert public_origins() == ('https://robot.example.up.railway.app',)
    monkeypatch.setenv('ROBOT_PUBLIC_ORIGINS', 'https://robots.example.com')
    assert public_origins() == ('https://robots.example.com',)


@pytest.mark.parametrize('key,value', [
    ('ROBOT_MAX_VISITORS','0'), ('ROBOT_MAX_VISITORS','99'),
    ('ROBOT_VISITOR_TTL_SECONDS','0'), ('ROBOT_KEY_TTL_SECONDS','99999'),
])
def test_resource_bounds(monkeypatch, key, value):
    monkeypatch.setenv('ROBOT_PUBLIC_ORIGINS', 'https://demo.example')
    monkeypatch.setenv(key, value)
    with pytest.raises(ValueError, match=key):
        create_cloud_app()


def test_health_initial_scene_physics_isolation_and_capacity(monkeypatch):
    monkeypatch.setenv('ROBOT_PUBLIC_ORIGINS', 'https://demo.example')
    monkeypatch.setenv('OPENAI_API_KEY', 'operator-key-must-not-be-used')
    app = create_cloud_app()
    registry = app.state.visitors
    headers = {'X-Robot-Request':'1'}
    with TestClient(app, base_url='https://demo.example', headers=headers) as first:
        assert first.get('/healthz').json() == {'status':'ok','mode':'personal_api'}
        assert len(registry.visitors) == 0
        response = first.get('/api/session')
        assert response.status_code == 200
        assert 'Secure' in response.headers['set-cookie']
        assert 'HttpOnly' in response.headers['set-cookie']
        project = first.get('/api/project').json()
        assert project['id'] == 'scenario-multifloor-cargo'
        assert len(project['environment']['floors']) == 2
        assert len(project['robots']) == 5
        assert len(project['people']) == 3
        assert len(project['items']) == 1
        assert any(robot['model_id']=='spot' for robot in project['robots'])
        assert not first.get('/api/assistant/settings').json()['has_key']
        assert first.post('/api/assistant/login').status_code == 422
        before = first.get('/api/state').json()
        assert before['status'] == 'paused'
        after = first.post('/api/control', json={'action':'step','steps':20}).json()
        assert after['sim_time'] > before['sim_time']
        assert after['status'] != 'failed'
        scene = first.get('/api/scene', headers={'Accept-Encoding':'gzip'})
        assert scene.status_code == 200
        assert scene.headers['content-encoding'] == 'gzip'
        assert int(scene.headers['content-length']) < len(scene.content)
        assert scene.json()['run_id'] == after['run_id']
        assert scene.json()['meshes']
        with TestClient(app, base_url='https://demo.example', headers=headers) as second:
            assert second.get('/api/session').status_code == 200
            other = second.get('/api/state').json()
            assert other['run_id'] != after['run_id']
            assert other['sim_time'] == 0
            with TestClient(app, base_url='https://demo.example', headers=headers) as third:
                assert third.get('/api/session').status_code == 503
    assert not registry.visitors
