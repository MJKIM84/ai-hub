from robot_platform.domain import Project
from robot_platform.templates import example


def test_warehouse_sample_preserves_geometry_and_physical_cargo_dependencies():
    source = example("warehouse")
    sample = example("warehouse-cooperation")
    geometry = {e.id: e.model_dump() for e in sample.environment.elements}
    assert all(geometry[e.id] == e.model_dump() for e in source.environment.elements)
    assert len(sample.robots) == 6 and len(sample.people) == 3
    assert sample.policy.pedestrian_avoidance.desired_clearance_m == .5
    tasks = {t.id: t for t in sample.tasks}
    assert tasks["return-delivery"].predecessor_ids == ["delivery", "inbound-clear", "outbound-approach"]
    assert tasks["inbound-clear"].predecessor_ids == ["delivery"]
    assert tasks["outbound-approach"].predecessor_ids == ["inbound-clear"]
    assert tasks["delivery"].cooperation.carrier_id != tasks["return-delivery"].cooperation.carrier_id
    assert tasks["return-delivery"].source == tasks["delivery"].destination
    assert tasks["delivery"].item_id == tasks["return-delivery"].item_id
    assert tasks["delivery"].cooperation.receiver_id == tasks["return-delivery"].cooperation.donor_id
    assert tasks["spot-return"].predecessor_ids == ["spot-patrol"]
    assert tasks["spot-patrol"].predecessor_ids == []
    for person in sample.people:
        assert person.speed > 0
        assert len(person.behavior.destinations) == 2
    assert Project.model_validate_json(sample.model_dump_json()) == sample


def test_carriers_cannot_plan_inside_the_other_operating_zone():
    from robot_platform.navigation import Planner
    sample = example("warehouse-cooperation")
    planner = Planner(sample.environment)
    inbound = next(r for r in sample.robots if r.id == "cart")
    outbound = next(r for r in sample.robots if r.id == "outbound-cart")
    assert planner.blocked(13, 2, "floor-1", inbound)
    assert planner.blocked(5, 2, "floor-1", outbound)
    from robot_platform.pedestrian_navigation import PedestrianNavigator, validate_pedestrian_placements
    validate_pedestrian_placements(sample)
    person = sample.people[0]
    assert PedestrianNavigator(sample.environment, person).valid_pose(person.pose)
    zone = next(e for e in sample.environment.elements if e.id == "inbound-zone")
    zone.pedestrian_access = False
    assert not PedestrianNavigator(sample.environment, person).valid_pose(person.pose)


def test_each_template_load_has_independent_configuration():
    changed = example("warehouse-cooperation")
    changed.tasks[0].destination.x += .5
    assert example("warehouse-cooperation").tasks[0].destination.x == 8.95
    assert example("warehouse").id == "example-warehouse"


def test_loading_approach_requires_reserved_donor_and_observed_arrival():
    import pytest
    from robot_platform.runtime import Session
    sample = example("warehouse-cooperation")
    task = sample.tasks[0].model_copy(deep=True)
    raw = task.cooperation.model_dump()
    raw.update(carrier_loading_pose={"x": 2.5165, "y": 3, "z": 0, "yaw": 0}, donor_id=None)
    with pytest.raises(ValueError, match="상차 접근"):
        type(task.cooperation).model_validate(raw)
    # The same loading pose as the sample's stationary first carrier isolates
    # arrival gating from the long relay simulation. No item state is patched.
    from robot_platform.domain import Pose
    task.cooperation.carrier_loading_pose = Pose(x=2.5165,y=3)
    sample.tasks = [task]
    session = Session(sample)
    session.status = "running"
    session.step(500)
    arrival = [e for e in session.events if e["kind"] == "cooperation_loading_arrived"]
    assert len(arrival) == 1
    assert session.cooperative.executions[task.id]["loading_approach_done"]
    assert not session.cooperative.executions[task.id]["loading_committed"]
    assert not any(e["kind"] == "cooperation_loaded" for e in session.events)


def test_cancelled_loading_approach_holds_carrier_and_keeps_recovery_reservation():
    from robot_platform.domain import Pose
    from robot_platform.runtime import Session
    sample = example("warehouse-cooperation")
    task = sample.tasks[0].model_copy(deep=True)
    task.cooperation.carrier_loading_pose = Pose(x=3.5,y=3)
    sample.tasks = [task]
    session = Session(sample)
    session.status = "running"
    session.step(500)
    execution = session.cooperative.executions[task.id]
    assert not execution['loading_approach_done']
    assert not execution['loading_committed']
    session.cooperative.terminate(task.id,session.time,'사용자 취소',cancelled=True)
    command = session.cooperative.base_command('cart',session.time,session.observations)
    assert command['v'] == command['w'] == 0
    assert execution['terminal'] and not execution['released']
    assert session.orchestrator.tasks[task.id]['status'] == 'cancelled'
