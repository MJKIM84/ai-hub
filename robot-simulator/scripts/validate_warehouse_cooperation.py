"""Run the authored sample without model calls or real robot connections."""
import argparse
import gzip
import json
from copy import deepcopy
from pathlib import Path
import time

from robot_platform.experiments import manifest
from robot_platform.runtime import Session
from robot_platform.templates import example


def main():
    project = example("warehouse-cooperation")
    initial_manifest = manifest(project)
    session = Session(project)
    session.status = "running"
    start = time.monotonic()
    trace = []
    while session.status == "running":
        session.step(round(1 / project.physics.timestep))
        state = session.snapshot(False)
        trace.append(dict(time=session.time, robots=[dict(id=r["id"], pose=r["pose"],
            status=r["status"], reason=r["reason"],
            path=deepcopy(session.orchestrator.robot_states[r["id"]].get("path", [])),
            command=dict(session.world.commands.get(r["id"], {}))) for r in state["robots"]],
            people=state["people"], items=state["items"],
            tasks=[dict(id=t["id"], status=t["status"]) for t in state["tasks"]]))
        if len(trace) % 20 == 0:
            print(round(session.time, 2), [(t["id"], t["status"]) for t in state["tasks"]], flush=True)
    final_manifest = manifest(project)
    result = dict(manifest=initial_manifest,
        source_unchanged_during_run=initial_manifest['source_sha256'] == final_manifest['source_sha256'],
        wall_seconds=time.monotonic()-start,
        final=session.snapshot(False), events=session.events, trace=trace)
    folder = Path("docs/validation/warehouse-zone-relay")
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"run-{session.run_id}.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(path, session.status, session.time, flush=True)
    print(json.dumps(session.metrics(), ensure_ascii=False), flush=True)
    check_result(result, project)


def check_result(result, project):
    assert result['source_unchanged_during_run'], "Source changed during validation; result retained"
    assert result['final']['status'] == "completed", "Failure details preserved in result"
    trace, events = result['trace'], result['events']
    rows = {t["id"]: t for t in result["final"]["tasks"]}
    for before, after in [("delivery", "inbound-depart"), ("inbound-depart", "inbound-clear"), ("inbound-clear", "outbound-approach"),
                          ("outbound-approach", "return-delivery")]:
        assert rows[before]["completed_at"] <= rows[after]["started_at"]
    positions = {rid: [next(r for r in frame["robots"] if r["id"] == rid)["pose"]["x"]
                       for frame in trace] for rid in ("cart", "outbound-cart")}
    assert max(positions["cart"]) < 12, "Inbound carrier entered the outbound-only zone"
    assert min(positions["outbound-cart"]) > 8, "Outbound carrier entered the inbound-only zone"
    loaded = [e for e in events if e["kind"] == "cooperation_loaded"]
    assert [e["entity_id"] for e in loaded] == ["cart", "outbound-cart"]
    clearance = result["final"]["metrics"]["pedestrian_min_clearance_m"]
    assert all(value is not None and value >= .5 for value in clearance.values())
    for person in project.people:
        ys = [frame["people"][person.id]["actual_position"][1] for frame in trace]
        assert max(ys)-min(ys) > 1, "A stationary pedestrian is not a crossing test"
    avoidance = [e for e in events if e["kind"] == "pedestrian_avoidance"
                 and e["entity_id"] in ("cart", "outbound-cart")]
    assert any(e["details"].get("mode") == "waiting" for e in avoidance)
    assert any(e["details"].get("previous") == "waiting" and
               e["details"].get("mode") == "resuming" for e in avoidance)
    robot_ids = {r.id for r in project.robots}
    assert not any(e["kind"] == "collision" and e["details"].get("a") in robot_ids
                   and e["details"].get("b") in robot_ids for e in events), "Robot body contacts preserved in result"
    assert not any(e["kind"] == "collision" and
                   (e["details"].get("a", "").startswith("crossing-") or
                    e["details"].get("b", "").startswith("crossing-"))
                   for e in events)


def check_browser_recording(path):
    """Apply the same acceptance checks to a real browser-started API recording.

    Reading recorded qpos is replay analysis, not a new physics run. No pose,
    item custody, task status or success criterion is changed.
    """
    from robot_platform.domain import Project
    from robot_platform.physics import PhysicsWorld
    result = json.loads(gzip.decompress(path.read_bytes()) if path.suffix == '.gz' else path.read_bytes())
    recording = result['recording']
    project = Project.model_validate(recording['project'])
    assert project == example('warehouse-cooperation'), 'Sample conditions changed'
    assert result['final']['run_id'] == recording['run_id']
    assert result['manifest']['source_sha256'] == manifest(project)['source_sha256'], 'Recording belongs to a different source version'
    world = PhysicsWorld(project)
    axes = {p.id: (int(world.model.joint(f'{p.id}/x').qposadr[0]),
                   int(world.model.joint(f'{p.id}/y').qposadr[0])) for p in project.people}
    result['events'] = recording['events']
    result['trace'] = [dict(time=f['time'],
        robots=[dict(id=rid,pose=pose) for rid,pose in f['robots'].items()],
        people={p.id:dict(actual_position=[p.pose.x+f['qpos'][axes[p.id][0]],
                    p.pose.y+f['qpos'][axes[p.id][1]],0]) for p in project.people})
        for f in recording['frames']]
    check_result(result, project)
    print(json.dumps(dict(status='passed',run_id=recording['run_id'],
        sim_seconds=result['final']['sim_time'],completed=result['final']['metrics']['completed'],
        pedestrian_min_clearance_m=result['final']['metrics']['pedestrian_min_clearance_m']),ensure_ascii=False))


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--recording',type=Path,help='Validate a saved browser/API recording without another simulation')
    args=parser.parse_args()
    if args.recording:check_browser_recording(args.recording)
    else:main()
