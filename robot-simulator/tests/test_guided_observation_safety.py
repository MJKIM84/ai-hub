"""Directed AGV decisions use accepted source observations, not tick repetition.

These tests execute only the decision layer with explicit sensor fixtures.
They do not simulate an AGV or claim physical route/charging completion.
"""
from copy import deepcopy
from math import atan2, pi

import pytest

from robot_platform.domain import Element, Pose, Project, RobotInstance, Task
from robot_platform.orchestration import Orchestrator


def scenario():
    robot = RobotInstance(id='guided', model_id='agv', pose=Pose(x=2, y=2, yaw=pi/2),
                          agv_route=[Pose(x=2, y=2), Pose(x=2, y=5)])
    task = Task(id='patrol', kind='patrol', preferred_robot=robot.id,
                destination=Pose(x=2, y=4, yaw=pi/2), dwell=.5)
    events = []
    control = Orchestrator(Project(robots=[robot], tasks=[task]), lambda *args: events.append(args))
    obs = dict(robot_id=robot.id, sampled_at=1., pose=dict(x=2., y=2., z=.3, yaw=pi/2),
               fault='none', battery=100., upright=1., velocity=[0., 0., 0.],
               angular_velocity=[0., 0., 0.], sensors={})
    first = control.tick(1., {robot.id: obs})
    assert first[robot.id]['v'] > 0
    assert control.tasks[task.id]['status'] == 'running'
    return control, obs, events


def stopped(command):
    assert command['v'] == 0. and command['w'] == 0.


@pytest.mark.parametrize('stamp', [.9, 1.], ids=['reordered', 'altered-duplicate'])
def test_prior_on_route_cache_cannot_authorize_off_route_observation(stamp):
    control, obs, events = scenario()
    obs.update(sampled_at=stamp)
    obs['pose'].update(x=3., yaw=atan2(2., -1.))
    path = deepcopy(control.robot_states['guided']['path'])
    command = control.tick(1.1, {'guided': obs})['guided']
    stopped(command)
    assert control.robot_states['guided']['path'] == path
    assert control.tasks['patrol']['arrival_at'] is None
    assert not any(event[0] == 'task_completed' for event in events)


@pytest.mark.parametrize('stamp', [.9, 1.], ids=['reordered', 'altered-duplicate'])
def test_unaccepted_observation_at_goal_cannot_consume_waypoint_or_start_dwell(stamp):
    control, obs, events = scenario()
    path = deepcopy(control.robot_states['guided']['path'])
    obs.update(sampled_at=stamp)
    obs['pose']['y'] = 4.
    stopped(control.tick(1.1, {'guided': obs})['guided'])
    assert control.robot_states['guided']['path'] == path
    assert control.tasks['patrol']['arrival_at'] is None
    assert control.tasks['patrol']['status'] == 'running'
    assert not any(event[0] == 'task_completed' for event in events)


def test_repeated_valid_goal_sample_cannot_earn_source_time_dwell():
    control, obs, events = scenario()
    obs.update(sampled_at=2.)
    obs['pose']['y'] = 4.
    control.tick(2., {'guided': obs})
    assert control.tasks['patrol']['status'] == 'running'
    # All repeats are still within the configured one-second freshness bound.
    for now in (2.1, 2.3, 2.5, 2.6):
        stopped(control.tick(now, {'guided': obs})['guided'])
        assert control.tasks['patrol']['status'] == 'running'
        assert control.tasks['patrol']['completed_at'] is None
    assert not any(event[0] == 'task_completed' for event in events)


def test_fresh_goal_samples_can_complete_with_observed_stationary_dwell():
    control, obs, events = scenario()
    obs['pose']['y'] = 4.
    for stamp in (2., 2.1, 2.2, 2.3, 2.4):
        obs['sampled_at'] = stamp
        stopped(control.tick(stamp, {'guided': obs})['guided'])
        assert control.tasks['patrol']['status'] == 'running'
    obs['sampled_at'] = 2.6
    stopped(control.tick(2.6, {'guided': obs})['guided'])
    assert control.tasks['patrol']['status'] == 'completed'
    assert sum(event[0] == 'task_completed' for event in events) == 1


def test_late_old_goal_sample_does_not_hide_fresh_sample_away_from_goal():
    control, obs, events = scenario()
    obs.update(sampled_at=2.)
    obs['pose']['y'] = 4.
    old_goal = deepcopy(obs)
    control.tick(2., {'guided': obs})
    obs.update(sampled_at=2.2)
    obs['pose']['y'] = 3.8
    control.tick(2.2, {'guided': obs})
    stopped(control.tick(2.6, {'guided': old_goal})['guided'])
    assert control.tasks['patrol']['status'] == 'running'
    assert control.tasks['patrol']['completed_at'] is None
    assert not any(event[0] == 'task_completed' for event in events)


def active_guided_path(points, goal, mode):
    """Supply explicit charging intentions; only motion routing is under test.

    A real request supplies identity for interruption. Synthetic approach/clear
    phase fixtures do not claim connector grant, charging, or physical release.
    """
    initial = Pose(x=points[0][0], y=points[0][1], yaw=pi/2)
    robot = RobotInstance(id='guided', model_id='agv', pose=initial,
                          agv_route=[Pose(x=x, y=y) for x, y in points])
    target = Pose(x=goal[0], y=goal[1], yaw=pi/2)
    tasks = [Task(id='patrol', kind='patrol', preferred_robot=robot.id,
                  destination=target, dwell=.5)] if mode == 'work' else []
    # Put the station off the selected authored legs. Its explicit one-metre
    # connector branch is not used by any of these approach/clearance commands.
    stage = initial if mode == 'clearing' else target
    elements = ([] if mode == 'work' else [Element(id='charger', kind='charger', floor_id=robot.floor_id,
        pose=Pose(x=stage.x-1.512, y=stage.y, yaw=pi))])
    control = Orchestrator(Project(robots=[robot], tasks=tasks,
                                  environment={'elements': elements}), lambda *args: None)
    obs = dict(robot_id=robot.id, sampled_at=1., pose=dict(initial.model_dump(), z=.3),
               fault='none', battery=100., upright=1., velocity=[0., 0., 0.],
               angular_velocity=[0., 0., 0.], sensors={})
    if mode != 'work':
        geometry = dict(staging=dict(stage.model_dump(), z=.3, yaw=pi),
                        target=dict(stage.model_dump(), x=stage.x-1., z=.3, yaw=pi))
        receipt = control.charging.manager.request('charger', robot.id, 1., geometry)
        control.charging.plans[robot.id] = dict(station_id='charger', geometry=geometry,
            request_id=receipt['request_id'], route_started=False, requested_at=1.,
            origin=deepcopy(obs['pose']))
        control.charging.intentions[robot.id] = dict(action='approach', phase='approach')
        control.robot_states[robot.id]['status'] = 'charging'
        if mode == 'clearing':
            control.charging.plans[robot.id].update(clearing=True, parking=dict(target.model_dump(), z=.3))
    first = control.tick(1., {robot.id: obs})[robot.id]
    assert first['v'] > 0
    return control, obs


def xy_path(control):
    return [(point['x'], point['y']) for point in control.robot_states['guided']['path']]


@pytest.mark.parametrize('mode', ['work', 'approach', 'clearing'])
def test_passing_an_intermediate_collinear_point_never_drives_back_to_it(mode):
    control, obs = active_guided_path([(2, 2), (2, 4), (2, 6), (2, 7)], (2, 7), mode)
    assert xy_path(control) == [(2, 4), (2, 6), (2, 7)]
    obs.update(sampled_at=1.2)
    obs['pose'].update(y=4.2, yaw=-pi/2)
    command = control.tick(1.2, {'guided': obs})['guided']
    assert command['v'] == 0.  # Face the remaining northbound leg before driving.
    assert xy_path(control) == [(2, 6), (2, 7)]
    obs.update(sampled_at=1.4)
    obs['pose']['yaw'] = pi/2
    assert control.tick(1.4, {'guided': obs})['guided']['v'] > 0


@pytest.mark.parametrize('mode', ['work', 'approach', 'clearing'])
def test_replanning_after_a_corner_keeps_the_next_authored_corner_instead_of_a_goal_chord(mode):
    control, obs = active_guided_path([(2, 2), (2, 4), (4, 4), (4, 6)], (4, 6), mode)
    obs.update(sampled_at=1.2)
    obs['pose'].update(x=2.2, y=4., yaw=pi)
    command = control.tick(1.2, {'guided': obs})['guided']
    assert command['v'] == 0.
    assert xy_path(control) == [(4, 4), (4, 6)]
    obs.update(sampled_at=1.4)
    obs['pose']['yaw'] = 0.
    command = control.tick(1.4, {'guided': obs})['guided']
    assert command['v'] > 0 and command['w'] == pytest.approx(0.)


@pytest.mark.parametrize('mode', ['work', 'approach', 'clearing'])
def test_a_corner_not_yet_reached_is_not_discarded_by_remaining_route_checks(mode):
    control, obs = active_guided_path([(2, 2), (2, 4), (4, 4), (4, 6)], (4, 6), mode)
    obs.update(sampled_at=1.2)
    obs['pose'].update(y=3.9)
    command = control.tick(1.2, {'guided': obs})['guided']
    assert xy_path(control) == [(2, 4), (4, 4), (4, 6)]
    assert command['v'] > 0 and command['w'] == pytest.approx(0.)


@pytest.mark.parametrize('mode', ['work', 'approach', 'clearing'])
@pytest.mark.parametrize('observed_y', [3.921, 3.99947, 4.001],
                         ids=['inside-before', 'physical-regression-position', 'just-after'])
def test_a_reached_intermediate_point_is_not_reinserted_by_forward_replanning(mode, observed_y):
    control, obs = active_guided_path([(2, 2), (2, 4), (2, 6), (2, 7)], (2, 7), mode)
    obs['pose']['y'] = observed_y
    # Fresh stationary sensor fixtures at the same accepted position must keep
    # the forward command. Tick repetition must not resurrect the reached y4.
    for stamp in (1.2, 1.4, 1.6):
        obs['sampled_at'] = stamp
        command = control.tick(stamp, {'guided': obs})['guided']
        assert xy_path(control) == [(2, 6), (2, 7)]
        assert command['v'] > 0 and command['w'] == pytest.approx(0.)
        if mode != 'work':
            assert not control.charging.plans['guided'].get('interrupted', False)


@pytest.mark.parametrize('mode', ['work', 'approach', 'clearing'])
def test_closed_route_reapproaches_a_passed_goal_only_through_all_remaining_vertices(mode):
    points = [(2, 2), (2, 3), (2, 4), (2, 6), (5, 6), (5, 2), (2, 2)]
    control, obs = active_guided_path(points, (2, 3), mode)
    obs.update(sampled_at=1.2)
    obs['pose'].update(y=4.2, yaw=-pi/2)
    command = control.tick(1.2, {'guided': obs})['guided']
    assert command['v'] == 0.
    assert xy_path(control) == [(2, 6), (5, 6), (5, 2), (2, 2), (2, 3)]


@pytest.mark.parametrize('mode', ['work', 'approach', 'clearing'])
@pytest.mark.parametrize('stamp', [.9, 1.], ids=['reordered', 'altered-duplicate'])
def test_unaccepted_passed_waypoint_observation_cannot_replan_any_guided_motion(mode, stamp):
    control, obs = active_guided_path([(2, 2), (2, 4), (2, 6), (2, 7)], (2, 7), mode)
    before = xy_path(control)
    obs.update(sampled_at=stamp)
    obs['pose'].update(y=4.2, yaw=-pi/2)
    stopped(control.tick(1.1, {'guided': obs})['guided'])
    assert xy_path(control) == before
