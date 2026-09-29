"""Actual Session speed is visible through every state/control response.

TestClient is intentionally used without the lifespan context: these checks call
real API handlers and real Sessions but do not start the background wall clock.
Only an explicit step request advances physics, so paused invariants are exact.
"""
from fastapi.testclient import TestClient
import pytest

from robot_platform.api import create_app


@pytest.fixture
def client(tmp_path):
    app = create_app(tmp_path)
    with_socketless_client = TestClient(app)
    try:
        yield with_socketless_client
    finally:
        with_socketless_client.close()


def control(client, action, **fields):
    response = client.post("/api/control", json={"action": action, **fields})
    assert response.status_code == 200, response.text
    result = response.json()
    assert result["speed"] == client.app.state.host.session.speed
    assert client.get("/api/state").json()["speed"] == result["speed"]
    return result


def test_initial_state_and_geometry_free_snapshot_report_actual_speed(client):
    state = client.get("/api/state").json()
    assert state["speed"] == 1.
    assert state["status"] == "paused"
    compact = client.app.state.host.session.snapshot(include_geometry=False)
    assert compact["speed"] == state["speed"]
    assert compact["geoms"] == []


def test_paused_speed_change_does_not_advance_or_resume_simulation(client):
    before = client.get("/api/state").json()
    changed = control(client, "pause", speed=.5)
    assert changed["speed"] == .5
    assert changed["status"] == "paused"
    assert changed["run_id"] == before["run_id"]
    assert changed["sim_time"] == before["sim_time"]
    assert changed["geoms"] == before["geoms"]
    assert changed["events"] == before["events"]


def test_running_speed_and_fresh_client_read_remain_consistent(client):
    started = control(client, "resume", speed=4.)
    assert started["status"] == "running" and started["speed"] == 4.
    # A new browser/client has no local dropdown state to carry over.
    another_client = TestClient(client.app)
    try:
        reloaded = another_client.get("/api/state").json()
        assert reloaded["run_id"] == started["run_id"]
        assert reloaded["speed"] == 4.
    finally:
        another_client.close()
    paused = control(client, "pause")
    assert paused["status"] == "paused" and paused["speed"] == 4.


@pytest.mark.parametrize("speed", [0., -1., 20.01])
def test_rejected_speed_keeps_previous_actual_multiplier(client, speed):
    before = control(client, "pause", speed=2.)
    response = client.post("/api/control", json={"action": "pause", "speed": speed})
    assert response.status_code == 422
    after = client.get("/api/state").json()
    assert after["speed"] == 2.
    assert after["run_id"] == before["run_id"]
    assert after["sim_time"] == before["sim_time"]


def test_reset_reports_new_session_default_not_previous_requested_speed(client):
    before = control(client, "pause", speed=4.)
    reset = control(client, "reset", speed=4.)
    assert reset["run_id"] != before["run_id"]
    assert reset["status"] == "paused"
    assert reset["speed"] == 1.
    assert reset["sim_time"] == 0.


def test_apply_recreates_default_speed_and_step_returns_actual_multiplier(client):
    before = control(client, "pause", speed=4.)
    project = client.get("/api/project").json()
    applied = client.put("/api/project", json=project)
    assert applied.status_code == 200, applied.text
    state = client.get("/api/state").json()
    assert state["run_id"] != before["run_id"]
    assert state["speed"] == 1.
    assert state["status"] == "paused"
    stepped = control(client, "step", speed=.25, steps=2)
    assert stepped["speed"] == .25 and stepped["status"] == "paused"
    assert stepped["sim_time"] == pytest.approx(2 * project["physics"]["timestep"])
