"""Reported facility times follow actual manager transitions in a live Session."""
import csv
import io
import pytest

from robot_platform.domain import Element, FaultInjection, Pose, Project, RobotInstance, SensorSettings
from robot_platform.experiments import compare, to_csv
from robot_platform.runtime import Session


def queue_session():
    return Session(Project(
        environment={'elements': [Element(id='charge', kind='charger', floor_id='floor-1', pose=Pose(x=4.5,y=3))]},
        robots=[
            RobotInstance(id='first',model_id='amr',pose=Pose(x=3.038,y=3),battery=19,battery_capacity_wh=4,sensors=SensorSettings(position_noise=0,yaw_noise=0)),
            RobotInstance(id='second',model_id='delivery',pose=Pose(x=2,y=5.5),battery=19,battery_capacity_wh=4,sensors=SensorSettings(position_noise=0,yaw_noise=0)),
        ]))


def test_actual_fifo_wait_is_robot_time_and_snapshot_does_not_double_count():
    session=queue_session()
    assert session.metrics()['facility_queue_wait_seconds']==0
    first_queued=None
    first_reserved=None
    for _ in range(1000):
        before=session.time
        session.step(1)
        if 'second' in session.facility_states['charge']['queue'] and first_queued is None:
            first_queued=before
        if 'first' in session.facility_states['charge'].get('reserved_by',[]) and first_reserved is None:
            first_reserved=before
    assert first_queued is not None
    metrics=session.metrics()
    assert metrics['charging_queue_wait_seconds']==pytest.approx(session.time-first_queued,abs=1e-8)
    assert metrics['facility_queue_wait_seconds']==pytest.approx(metrics['charging_queue_wait_seconds'])
    assert metrics['per_robot']['second']['charging_queue_wait_seconds']==pytest.approx(metrics['charging_queue_wait_seconds'])
    assert metrics['per_robot']['first']['facility_queue_wait_seconds']==0
    facility=metrics['facilities']['charge']
    assert first_reserved is not None
    assert facility['reserved_seconds']==pytest.approx(session.time-first_reserved,abs=1e-8)
    assert facility['occupied_seconds']==0
    assert facility['completed_queue_wait_count']==0
    assert facility['completed_queue_wait_mean_seconds'] is None
    assert session.metrics()['facilities']==metrics['facilities']
    assert session.snapshot(include_geometry=False)['metrics']['facilities']==metrics['facilities']
    assert session.recording()['metrics']['facilities']==metrics['facilities']


def test_facility_fault_accumulates_separately_from_queue_wait():
    session=queue_session()
    session.step(1000)
    before=session.metrics()['charging_queue_wait_seconds']
    session.inject(FaultInjection(target_id='charge',kind='facility'))
    session.step(500)
    metrics=session.metrics()
    assert metrics['facility_fault_seconds']==pytest.approx(1.,abs=1e-8)
    assert metrics['facilities']['charge']['fault_seconds']==pytest.approx(1.,abs=1e-8)
    assert metrics['charging_queue_wait_seconds']==pytest.approx(before+1.,abs=1e-8)


def test_comparison_json_and_csv_include_facility_times_and_charge_energy(tmp_path):
    session=queue_session()
    result=compare(session.project,[1],[session.project.policy],.5,tmp_path)
    metric=result['runs'][0]['metrics']
    assert result['summary'][0]['metrics']['charging_queue_wait_seconds']['mean']==metric['charging_queue_wait_seconds']
    row=next(csv.DictReader(io.StringIO(to_csv(result))))
    for key in ('facility_queue_wait_seconds','charging_queue_wait_seconds','facility_fault_seconds','charging_input_j','charging_stored_j','unserved_energy_j'):
        assert float(row[key])==pytest.approx(metric[key])
