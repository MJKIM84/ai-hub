"""Run the authored sample without model calls or real robot connections."""
import json
from pathlib import Path
import time

from robot_platform.experiments import manifest
from robot_platform.runtime import Session
from robot_platform.templates import example


def main():
    project = example("warehouse-cooperation")
    session = Session(project)
    session.status = "running"
    start = time.monotonic()
    trace = []
    while session.status == "running":
        session.step(round(1 / project.physics.timestep))
        state = session.snapshot(False)
        trace.append(dict(time=session.time, robots=[dict(id=r["id"], pose=r["pose"],
            status=r["status"], reason=r["reason"]) for r in state["robots"]],
            people=state["people"], items=state["items"],
            tasks=[dict(id=t["id"], status=t["status"]) for t in state["tasks"]]))
        if len(trace) % 20 == 0:
            print(round(session.time, 2), [(t["id"], t["status"]) for t in state["tasks"]], flush=True)
    result = dict(manifest=manifest(project), wall_seconds=time.monotonic()-start,
        final=session.snapshot(False), events=session.events, trace=trace)
    folder = Path("docs/validation/warehouse-zone-relay")
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"run-{session.run_id}.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(path, session.status, session.time, flush=True)
    print(json.dumps(session.metrics(), ensure_ascii=False), flush=True)
    assert session.status == "completed", "Failure details preserved in result"
    rows = {t["id"]: t for t in result["final"]["tasks"]}
    for before, after in [("delivery", "inbound-clear"), ("inbound-clear", "outbound-approach"),
                          ("outbound-approach", "return-delivery")]:
        assert rows[before]["completed_at"] <= rows[after]["started_at"]
    loaded = [e for e in session.events if e["kind"] == "cooperation_loaded"]
    assert len(loaded) == 2
    clearance = session.metrics()["pedestrian_min_clearance_m"]
    assert all(value is not None and value >= .5 for value in clearance.values())
    for person in project.people:
        ys = [frame["people"][person.id]["actual_position"][1] for frame in trace]
        assert max(ys)-min(ys) > 1, "A stationary pedestrian is not a crossing test"
    avoidance = [e for e in session.events if e["kind"] == "pedestrian_avoidance"
                 and e["entity_id"] in ("cart", "outbound-cart")]
    assert any(e["details"].get("mode") == "waiting" for e in avoidance)
    assert any(e["details"].get("previous") == "waiting" and
               e["details"].get("mode") == "resuming" for e in avoidance)
    assert not any(e["kind"] == "collision" and
                   (e["details"].get("a", "").startswith("crossing-") or
                    e["details"].get("b", "").startswith("crossing-"))
                   for e in session.events)


if __name__ == "__main__":
    main()
