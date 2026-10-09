"""Read-only state delivery, independent of the network round-trip duration.

Every frame comes from one locked physical snapshot. Top-level deltas avoid
resending unchanged event histories and configuration; a new connection/run
always starts with a full frame. There is no simulation control in this route.
"""
import asyncio
import json
import time

from fastapi import HTTPException
from starlette.background import BackgroundTask
from starlette.responses import StreamingResponse


async def state_events(host, *, lifetime=90):
    previous, previous_sequence, previous_run = {}, None, None
    deadline = time.monotonic() + lifetime
    while not host.stop.is_set() and time.monotonic() < deadline:
        started = time.monotonic()
        snapshot = await asyncio.to_thread(host.snapshot)
        encoded = {key: json.dumps(value, separators=(',', ':'), ensure_ascii=False)
                   for key, value in snapshot.items()}
        full = snapshot['run_id'] != previous_run
        changed = encoded if full else {key: value for key, value in encoded.items()
                                       if previous.get(key) != value}
        data = '{' + ','.join(json.dumps(key)+':'+value for key, value in changed.items()) + '}'
        frame = ('{"full":'+str(full).lower()+',"base_sequence":'
                 +json.dumps(None if full else previous_sequence)+',"state":'+data+'}')
        yield 'retry: 500\ndata: ' + frame + '\n\n'
        previous, previous_sequence, previous_run = encoded, snapshot['state_sequence'], snapshot['run_id']
        hz = max(1, min(20, snapshot.get('render_hz', 20))) if snapshot['status'] == 'running' else 4
        # No queued catch-up frames after slow clients: sample the latest state.
        await asyncio.sleep(max(.001, 1/hz - (time.monotonic()-started)))


def install_state_stream(app, host):
    @app.get('/api/state/stream')
    def stream():
        with host.lock:
            if host.state_streams >= 2:
                raise HTTPException(429, '실시간 연결이 많습니다. 다른 탭을 닫으면 다시 연결합니다.')
            host.state_streams += 1
        released = False

        def release():
            nonlocal released
            with host.lock:
                if not released:
                    host.state_streams -= 1
                    released = True

        async def frames():
            try:
                async for frame in state_events(host):
                    yield frame
            finally:
                release()

        return StreamingResponse(frames(), media_type='text/event-stream',
            headers={'Cache-Control':'no-store', 'X-Accel-Buffering':'no'},
            background=BackgroundTask(release))
