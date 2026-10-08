"""Real Session docking, electrical interlocks, energy and workflow recovery."""
from copy import deepcopy
from pathlib import Path
import runpy

import pytest

from robot_platform.domain import FaultInjection
from robot_platform.runtime import Session

PROBE=runpy.run_path(str(Path(__file__).resolve().parents[1]/'scripts/charging_integration_probe.py'))


def charging_session():
    session=Session(PROBE['project'](with_task=False))
    assert PROBE['until'](session,lambda s:s.charge_power['robot']>0,seconds=40)
    return session


@pytest.mark.parametrize('kind,seed',[('amr',1),('delivery',2)])
def test_autonomous_low_battery_contact_charge_undock_idle_and_work_again(kind,seed):
    result=PROBE['run_case'](kind,seed)
    assert result['passed'],result['transitions']
    assert result['powered_physics_steps']>100
    phases=[row['phase'] for row in result['transitions']]
    assert all(phase in phases for phase in ('approach','dock','charging','undock','idle'))
    assert result['peak_battery_percent']>=40
    assert result['idle_after_charge']
    assert result['tasks'][0]['status']=='completed'
    assert result['final_power_w']==0
    assert not result['final_connector']['left'] and not result['final_connector']['right']
    completed=next(e for e in result['events'] if e['kind']=='charging_completed')
    assigned=next(e for e in result['events'] if e['kind']=='assignment')
    assert completed['seq']<assigned['seq']
    assert result['max_energy_balance_error_j']<1e-6
    assert result['metrics']['charging_stored_j']==pytest.approx(result['metrics']['charging_input_j']*.9,abs=1e-7)
    assert not any(result['warnings'])


def test_insufficient_post_charge_task_reserve_waits_without_recharge_loop():
    result=PROBE['insufficient_energy_case']()
    assert result['passed'],result
    assert result['task']['status']=='waiting'
    assert '조정 필요' in result['robot_state']['reason']
    assert len(result['requests'])==1


def test_fifo_charging_clears_both_robots_with_per_physics_step_interlocks():
    result=PROBE['queue_case'](seconds=180.)
    assert result['passed'],result['last_20_seconds']
    assert result['completed_at']['robot']<result['completed_at']['second']<=180
    audits=result['physical_step_audits']
    assert audits['physics_steps_checked']==round(result['sim_time']/audits['timestep_seconds'])
    assert audits['maximum_simultaneously_powered']==1
    assert all(audits[key]==0 for key in ('simultaneous_power_steps','unsafe_contact_power_steps','unreserved_power_steps','robot_robot_contact_steps','fifo_violation_steps'))
    assert [row['robot_id'] for row in audits['reservation_grants'][:2]]==['robot','second']
    assert audits['first_power_at']['second']>result['completed_at']['robot']
    assert all(steps>100 for steps in audits['powered_steps'].values())
    assert len(result['completion_evidence'])==2
    for evidence in result['completion_evidence'].values():
        assert evidence['position_error_m']<.08
        assert evidence['yaw_error_rad']<.1
        assert evidence['observed_speed_m_s']<.04
        assert evidence['power_w']==0
        assert not evidence['physical_connector']['left'] and not evidence['physical_connector']['right']
    assert result['metrics']['collisions']==0
    assert not any(result['warnings'])


def test_forged_enable_without_physical_contacts_cannot_add_energy():
    session=Session(PROBE['project'](with_task=False,battery=50))
    session.step(500)
    session.orchestrator.charging.power_requests={'robot':{'station_id':'charge','power_w':1e9}}
    before=session.batteries['robot']
    for _ in range(100):
        session.world.step()
        session._evaluate()  # Exercise the local interlock with retained forged enable.
        assert session.charge_power['robot']==0
    assert session.charge_input['robot']==session.charge_stored['robot']==0
    assert session.batteries['robot']<before


def test_physical_contact_loss_cuts_power_before_delayed_sensor_changes():
    session=charging_session()
    old=deepcopy(session.observations['robot'])
    assert old['sensors']['docking']['charge']['left'] and old['sensors']['docking']['charge']['right']
    # Simulate a paused upstream sensor/controller, retaining its old enable.
    # The local electrical interlock still runs at every physical timestep.
    session.next_sensor=session.time+1
    session.next_orchestration=session.time+1
    session.world.command('robot',v=-.15,mode='drive')
    observed_gap=False
    for _ in range(300):
        session.step(1)
        physical=PROBE['physical_connector'](session)
        if not PROBE['connector_safe'](physical):
            assert session.charge_power['robot']==0
        if not physical['left'] and not physical['right']:
            observed_gap=True
            assert session.observations['robot']['sampled_at']==old['sampled_at']
            assert session.observations['robot']['sensors']['docking']['charge']['left']
    assert observed_gap


@pytest.mark.parametrize('fault',['facility','communication','operator_stop'])
def test_fault_or_operator_stop_cuts_power_and_explicit_recovery_reconfirms(fault):
    session=charging_session()
    before=session.charge_input['robot']
    if fault=='operator_stop':session.command('robot','stop')
    else:session.inject(FaultInjection(target_id='charge' if fault=='facility' else 'robot',kind=fault))
    session.step(1)
    assert session.charge_power['robot']==0
    assert session.charge_input['robot']==before
    session.step(600)
    assert session.charge_input['robot']==before
    if fault!='operator_stop':
        session.inject(FaultInjection(target_id='charge' if fault=='facility' else 'robot',kind='recover'))
        session.step(200)
        if fault=='communication':
            assert session.charge_power['robot']==0
            assert session.charge_input['robot']==before
    assert session.resume_robot('robot')['status']=='accepted'
    assert PROBE['until'](session,lambda s:s.charge_power['robot']>0,seconds=15),session.facility_states['charge']
    assert PROBE['connector_safe'](PROBE['physical_connector'](session))


@pytest.mark.parametrize('timestamp_case',['stale','future','nonfinite','missing'])
def test_charging_motion_controller_rejects_invalid_observation_time_directly(timestamp_case):
    session=Session(PROBE['project'](with_task=False))
    assert PROBE['until'](session,lambda s:s.facility_states['charge'].get('phase')=='dock',seconds=5)
    observation=deepcopy(session.observations['robot'])
    assert session.orchestrator.charging.command('robot',observation,session.time)['v']>0
    now=session.time
    if timestamp_case=='stale':now+=session.project.policy.stale_after+.1
    elif timestamp_case=='future':observation['sampled_at']=now+.001
    elif timestamp_case=='nonfinite':observation['sampled_at']=float('nan')
    else:observation.pop('sampled_at')
    command=session.orchestrator.charging.command('robot',observation,now)
    assert command['v']==0 and command['w']==0


def test_stale_robot_sensor_stream_stops_request_and_requires_recovery():
    session=charging_session()
    session.bus.settings['robot'].dropout=1.
    session.step(600)
    assert session.time-session.observations['robot']['sampled_at']>session.project.policy.stale_after
    assert session.charge_power['robot']==0
    assert session.orchestrator.charging.manager.stations['charge'].fault_latched
    session.bus.settings['robot'].dropout=0.
    session.step(200)
    assert session.charge_power['robot']==0
    assert session.resume_robot('robot')['status']=='accepted'
    assert PROBE['until'](session,lambda s:s.charge_power['robot']>0,seconds=15)


def test_default_400wh_capacity_uses_same_conservative_energy_accounting():
    p=PROBE['project'](with_task=False,capacity=400.,battery=19.99,charge_until=20.1)
    session=Session(p)
    assert PROBE['until'](session,lambda s:s.charge_input['robot']>40,seconds=40)
    capacity_j=400*3600
    actual=session.batteries['robot']/100*capacity_j
    expected=19.99/100*capacity_j-session.energy['robot']+session.charge_stored['robot']
    assert actual==pytest.approx(expected,abs=1e-5)
    assert session.charge_stored['robot']==pytest.approx(session.charge_input['robot']*.9,abs=1e-7)
