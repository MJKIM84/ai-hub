"""Built textures must be served as images, never the SPA HTML fallback."""
from pathlib import Path
import time

import pytest
from fastapi.testclient import TestClient

from robot_platform import api, visitor_api
from robot_platform.cloud import create_cloud_app
from robot_platform.entry_gate import sign


@pytest.mark.parametrize('mode', ['local', 'cloud'])
def test_built_materials_are_images_and_cloud_gate_still_applies(tmp_path, monkeypatch, mode):
    source = Path(__file__).resolve().parents[1] / 'web/public/materials/industrial-v1/floor-epoxy.jpg'
    texture = source.read_bytes()
    dist = tmp_path / 'web/dist'
    material = dist / 'materials/industrial-v1/floor-epoxy.jpg'
    material.parent.mkdir(parents=True)
    material.write_bytes(texture)
    (dist / 'index.html').write_text('<html>App shell</html>')
    module = api if mode == 'local' else visitor_api
    monkeypatch.setattr(module, '__file__', str(tmp_path / 'src/robot_platform/module.py'))
    origin, secret = 'https://materials.example', 'a' * 64
    if mode == 'cloud':
        monkeypatch.setenv('ROBOT_PUBLIC_ORIGINS', origin)
        monkeypatch.setenv('ROBOT_ENTRY_REQUIRED', '1')
        monkeypatch.setenv('ROBOT_ENTRY_SECRET', secret)
        app = create_cloud_app()
    else:
        app = api.create_app(data_dir=tmp_path / 'data')
    route = '/materials/industrial-v1/floor-epoxy.jpg'
    with TestClient(app, base_url=origin) as client:
        if mode == 'cloud':
            assert client.get(route).status_code == 401
            ticket = sign(dict(kind='handoff', aud=origin, exp=time.time()+90, nonce='b'*32), secret)
            assert client.post('/access/enter', headers={'Origin':origin}, json={'ticket':ticket}).status_code == 200
        response = client.get(route)
        assert response.status_code == 200
        assert response.headers['content-type'] == 'image/jpeg'
        assert response.content == texture
        assert client.get('/materials/industrial-v1/missing.jpg').status_code == 404
        assert 'App shell' in client.get('/workspace').text
        if mode == 'cloud':
            assert not app.state.visitors.visitors
