"""Real snapshots over a bounded test stream; no simulated model responses."""
import asyncio
import json

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from robot_platform.api import create_app
from robot_platform.runtime import Session
from robot_platform import state_stream
from robot_platform.visitor_api import create_personal_app, VisitorRegistry


def decode(text):
    return [json.loads(line[6:]) for line in text.splitlines() if line.startswith('data: ')]


def test_frames_preserve_physics_and_restart_base_after_reset(tmp_path):
    app = create_app(tmp_path)
    host = app.state.host

    async def check():
        frames = state_stream.state_events(host)
        first = decode(await anext(frames))[0]
        before = first['state']
        with host.lock:
            host.session.step(5)
        second = decode(await anext(frames))[0]
        assert not second['full'] and second['base_sequence'] == before['state_sequence']
        merged = before | second['state']
        actual = host.snapshot()
        assert merged['geoms'] == actual['geoms']
        assert merged['sim_time'] == actual['sim_time'] > before['sim_time']
        assert merged['state_sequence'] < actual['state_sequence']
        assert merged['robots'] == actual['robots']
        # Stream reads do not advance a paused simulation.
        assert host.session.time == actual['sim_time']
        with host.lock:
            host.session = Session(host.session.project)
        reset = decode(await anext(frames))[0]
        assert reset['full'] and reset['base_sequence'] is None
        assert reset['state']['run_id'] != before['run_id']
        assert reset['state']['sim_time'] == 0
        host.stop.set()
        with pytest.raises(StopAsyncIteration): await anext(frames)
        await frames.aclose()
    asyncio.run(check())


def test_stream_disconnect_releases_capacity(tmp_path):
    app = create_app(tmp_path)
    host = app.state.host
    endpoint = next(route.endpoint for route in app.routes if route.path == '/api/state/stream')
    first, second = endpoint(), endpoint()
    assert host.state_streams == 2
    with pytest.raises(HTTPException) as error: endpoint()
    assert error.value.status_code == 429

    async def check():
        await anext(first.body_iterator)
        await first.body_iterator.aclose()
        await first.background()
        assert host.state_streams == 1
        # Disconnection before the first frame is covered by response cleanup.
        await second.background()
        assert host.state_streams == 0
    asyncio.run(check())


def test_stream_keeps_visitor_isolation_and_origin_checks(monkeypatch):
    original = state_stream.state_events
    def bounded(host): return original(host, lifetime=.02)
    monkeypatch.setattr(state_stream, 'state_events', bounded)
    registry = VisitorRegistry(max_visitors=2)
    app = create_personal_app(registry=registry, origins=('https://stream.example',))
    with TestClient(app, base_url='https://stream.example') as first:
        assert first.get('/api/state/stream').status_code == 401
        assert first.get('/api/session', headers={'X-Robot-Request':'1'}).status_code == 200
        assert first.get('/api/state/stream', headers={'Origin':'https://other.example'}).status_code == 403
        response = first.get('/api/state/stream')
        assert response.headers['content-type'].startswith('text/event-stream')
        assert 'content-encoding' not in response.headers  # no gzip buffering SSE
        frame = decode(response.text)[0]
        assert frame['full']
        assert frame['state']['run_id'] == first.get('/api/state').json()['run_id']
        with TestClient(app, base_url='https://stream.example') as second:
            assert second.get('/api/session', headers={'X-Robot-Request':'1'}).status_code == 200
            other = decode(second.get('/api/state/stream').text)[0]['state']
            assert other['run_id'] != frame['state']['run_id']
            assert other['state_source'] != frame['state']['state_source']
        assert all(item.active == 0 and item.app.state.host.state_streams == 0 for item in registry.visitors.values())
