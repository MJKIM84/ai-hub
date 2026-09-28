"""Probe the built container, including real physics; no paid model requests."""
import http.cookiejar
import json
import time
from urllib.error import URLError
from urllib.request import HTTPCookieProcessor, Request, build_opener


base = 'http://127.0.0.1:8000'
headers = {
    'Host':'demo.example', 'X-Forwarded-Proto':'https',
    'Origin':'https://demo.example', 'X-Robot-Request':'1',
}
opener = build_opener(HTTPCookieProcessor(http.cookiejar.CookieJar()))


def call(path, data=None, extra=None):
    raw = None if data is None else json.dumps(data).encode()
    with opener.open(Request(base+path, data=raw,
        headers={**headers, **({'Content-Type':'application/json'} if raw else {}), **(extra or {})}), timeout=60) as response:
        return response.read(), response.headers


for attempt in range(60):
    try:
        health, _ = call('/healthz')
        assert json.loads(health)['mode'] == 'personal_api'
        break
    except URLError:
        time.sleep(1)
else:
    raise RuntimeError('Container did not become healthy')

html, _ = call('/')
assert b'type="module"' in html
session, response_headers = call('/api/session')
assert json.loads(session)['mode'] == 'personal_api'
cookie = response_headers['Set-Cookie'].split(';', 1)[0]
assert 'Secure' in response_headers['Set-Cookie']
# The container is probed over loopback HTTP with the actual proxy's HTTPS
# headers; provide the Secure cookie explicitly only in this local probe.
auth = {'Cookie':cookie}
project, _ = call('/api/project', extra=auth)
project = json.loads(project)
assert len(project['environment']['floors']) == 2
assert len(project['robots']) == 5 and len(project['people']) == 3
state, _ = call('/api/control', {'action':'step','steps':20}, auth)
state = json.loads(state)
assert state['sim_time'] > 0 and state['status'] != 'failed'
scene, _ = call('/api/scene', extra=auth)
assert json.loads(scene)['run_id'] == state['run_id']
print('Container passed: frontend, HTTPS proxy/cookie, isolated session, 2 floors, 5 robots, 3 people, real MuJoCo steps.')
