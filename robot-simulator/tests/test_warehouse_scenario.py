from robot_platform.domain import Project
from robot_platform.templates import example


def test_warehouse_sample_preserves_geometry_and_physical_cargo_dependencies():
    source = example("warehouse")
    sample = example("warehouse-cooperation")
    geometry = {e.id: e.model_dump() for e in sample.environment.elements}
    assert all(geometry[e.id] == e.model_dump() for e in source.environment.elements)
    assert len(sample.robots) == 5 and len(sample.people) == 3
    assert sample.policy.pedestrian_avoidance.desired_clearance_m == .5
    tasks = {t.id: t for t in sample.tasks}
    assert tasks["return-delivery"].predecessor_ids == ["delivery"]
    assert tasks["return-delivery"].source == tasks["delivery"].destination
    assert tasks["delivery"].item_id == tasks["return-delivery"].item_id
    assert tasks["delivery"].cooperation.receiver_id == tasks["return-delivery"].cooperation.donor_id
    assert tasks["spot-return"].predecessor_ids == ["spot-patrol"]
    assert tasks["spot-patrol"].predecessor_ids == []
    for person in sample.people:
        assert person.speed > 0
        assert len(person.behavior.destinations) == 2
    assert Project.model_validate_json(sample.model_dump_json()) == sample


def test_each_template_load_has_independent_configuration():
    changed = example("warehouse-cooperation")
    changed.tasks[0].destination.x += .5
    assert example("warehouse-cooperation").tasks[0].destination.x == 8.95
    assert example("warehouse").id == "example-warehouse"
