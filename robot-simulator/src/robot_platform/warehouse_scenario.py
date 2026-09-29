"""Warehouse sample composed from ordinary physical cargo and patrol tasks.

The warehouse geometry is reused unchanged. Stations and pedestrian zones are
authored sample inputs, not geometry inferred from a drawing.
"""
from types import SimpleNamespace
from .domain import Element, Person, Pose, Project, Size, Task
from .multifloor_scenario import cargo_scenario


def warehouse_cooperation():
    from .templates import example

    warehouse = example("warehouse")
    cargo = cargo_scenario()
    # Assemble related references together, then validate the whole project.
    project = SimpleNamespace(**{name: getattr(cargo, name) for name in Project.model_fields})
    project.environment = warehouse.environment
    project.id = "example-warehouse-cooperation"
    project.name = "물류 시설 · 구역별 AMR 교대"
    project.revision = 2
    project.environment.id = "env-warehouse-cooperation"
    project.environment.name = "물류 시설 · 입고·작업대·출고"
    project.robots = cargo.robots
    project.items = cargo.items
    project.tasks = cargo.tasks
    project.policy = cargo.policy
    project.physics = cargo.physics
    project.auto_stop_after_seconds = 360
    for robot in project.robots:
        robot.floor_id = "floor-1"
    for task in project.tasks:
        task.floor_id = "floor-1"
        if task.cooperation:
            task.cooperation.source_floor_id = "floor-1"
    project.tasks[0].name = "입고 상차 → 공유 통로 운반 → 작업대 하차"
    project.tasks[1].name = "작업대 재상차 → 출고 운반 → 최종 하차"
    project.tasks[0].timeout = 240
    project.robots[0].name = "입고 상차 팔"
    project.robots[1].name = "입고 구역 AMR A"
    project.robots[1].group = "입고"
    project.robots[2].name = "작업대 인계 팔"
    project.robots[3].name = "출고 하차 팔"
    project.robots[4].pose = Pose(x=3, y=8)
    project.robots[4].group = "순찰"
    for robot in (project.robots[0], project.robots[2], project.robots[3]):
        robot.group = "인계"
    outbound = project.robots[1].model_copy(deep=True, update=dict(
        id="outbound-cart", name="출고 구역 AMR B", group="출고", pose=Pose(x=13, y=1.2)))
    project.robots.append(outbound)
    project.tasks[0].name = "AMR A · 입고 상차 → 공용 작업대 인계"
    project.tasks[1].name = "AMR B · 작업대 인수 → 출고 운반·하차"
    project.tasks[1].cooperation.carrier_id = "outbound-cart"
    project.tasks[1].cooperation.carrier_loading_pose = Pose(x=9.848, y=3, yaw=0)
    project.tasks[1].predecessor_ids = ["delivery", "inbound-clear", "outbound-approach"]
    project.tasks.extend([
        Task(id="inbound-clear", name="AMR A · 인계 완료 후 입고 구역 복귀",
             kind="patrol", preferred_robot="cart", predecessor_ids=["delivery"],
             destination=Pose(x=7.4, y=6), dwell=1, timeout=120, retries=0),
        Task(id="outbound-approach", name="AMR B · A 복귀 확인 후 공용 작업대 접근",
             kind="patrol", preferred_robot="outbound-cart", predecessor_ids=["inbound-clear"],
             destination=Pose(x=9, y=1.5, yaw=0), dwell=1, timeout=120, retries=0),
    ])
    project.tasks[2].name = "Spot 입고 선반 순찰 · 이동·도착"
    project.tasks[2].destination = Pose(x=3, y=14)
    project.tasks.append(Task(id="spot-return", name="Spot 순찰 복귀 · 이동·도착",
        kind="patrol", preferred_robot="spot-patrol", floor_id="floor-1",
        predecessor_ids=["spot-patrol"], destination=Pose(x=5, y=8),
        dwell=2, timeout=180, retries=0))
    station_ids = {"warehouse", "warehouse-source", "workroom", "handoff-zone",
                   "worktable", "handoff-table", "work-rendezvous", "final-rendezvous"}
    for source in cargo.environment.elements:
        if source.id in station_ids:
            station = source.model_copy(deep=True)
            station.floor_id = "floor-1"
            project.environment.elements.append(station)
    project.environment.elements.append(Element(id="warehouse-shared-aisle",
        name="운반·보행 공유 통로", kind="corridor", floor_id="floor-1",
        pose=Pose(x=8, y=3), size=Size(x=10, y=5.2, z=.01)))
    project.environment.elements.extend([
        Element(id="inbound-zone", name="입고 전용 · AMR A", kind="restricted", floor_id="floor-1",
                pose=Pose(x=4, y=9), size=Size(x=8, y=18, z=.01),
                allowed_groups=["입고", "인계", "순찰"], pedestrian_access=True),
        Element(id="outbound-zone", name="출고 전용 · AMR B", kind="restricted", floor_id="floor-1",
                pose=Pose(x=17.5, y=9), size=Size(x=13, y=18, z=.01),
                allowed_groups=["출고", "인계", "순찰"], pedestrian_access=True),
        Element(id="shared-handoff-zone", name="공용 인계 · A 퇴장 후 B 진입", kind="loading",
                floor_id="floor-1", pose=Pose(x=9.5, y=3.5), size=Size(x=3, y=5, z=.01)),
    ])
    # The west fleet must also have a reachable service station inside its own
    # permission boundary. Keep the existing east station and energy checks.
    inlet_station = next(e for e in warehouse.environment.elements if e.kind == "charger")
    project.environment.elements.append(inlet_station.model_copy(deep=True, update=dict(
        id="inbound-charger", name="입고 구역 충전소", pose=Pose(x=5, y=6))))
    project.people = [Person.model_validate(dict(id=f"crossing-{i}", name=f"교차 보행자 {i}",
        floor_id="floor-1", pose=dict(x=x, y=1.1), speed=.65,
        behavior=dict(mode="destinations", allowed_zone_ids=["warehouse-shared-aisle"],
            destinations=[dict(x=x, y=1.1), dict(x=x, y=4.8)],
            speed_min_m_s=.5, speed_max_m_s=.8, stop_rate_per_s=.035,
            stop_duration_min_s=1, stop_duration_max_s=2.5,
            crossing_rate_per_s=.02, seed=seed)))
        for i, (x, seed) in enumerate([(5, 11), (7, 23), (11, 37)], start=1)]
    # Revalidate cross-references after composition; the normal executor owns
    # dependencies, contact completion, avoidance, waiting and resource release.
    return Project.model_validate(vars(project))
