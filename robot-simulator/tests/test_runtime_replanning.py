from copy import deepcopy
import pytest
from robot_platform.domain import Project, RobotInstance, Pose, Task
from robot_platform.runtime import Session
from robot_platform.runtime_replanning import RuntimeReplanning


def scene():
    p=Project(robots=[RobotInstance(id='a',model_id='amr',pose=Pose(x=2,y=2)),
                      RobotInstance(id='b',model_id='amr',pose=Pose(x=2,y=5))],
              tasks=[Task(id='patrol',preferred_robot='a',destination=Pose(x=8,y=5),release_time=100)])
    s=Session(p);s.step(150);return s


def test_reassign_requires_new_approval_preserves_physics_and_deduplicates():
    s=scene();service=RuntimeReplanning()
    pose=s.world.data.qpos.copy();custody=deepcopy(s.item_custody)
    p=service.prepare(s,'patrol')
    assert s.status=='paused'
    assert s.orchestrator.tasks['patrol']['spec'].preferred_robot=='a'
    assert 'assign-b' in [o['id'] for o in p['options']]
    receipt=service.approve(s,p['id'],'assign-b','request-1234')
    assert (s.world.data.qpos==pose).all() and s.item_custody==custody
    assert s.orchestrator.tasks['patrol']['spec'].preferred_robot=='b'
    assert service.approve(s,p['id'],'assign-b','request-1234')==receipt
    assert len([e for e in s.events if e['kind']=='replan_approved'])==1
    with pytest.raises(ValueError):service.approve(s,p['id'],'wait','request-1234')


def test_changed_state_and_forged_option_rejected():
    s=scene();service=RuntimeReplanning();p=service.prepare(s,'patrol')
    with pytest.raises(ValueError,match='검증한'):service.approve(s,p['id'],'fake','request-1234')
    s.robot_faults['b']='communication'
    with pytest.raises(ValueError,match='변경'):service.approve(s,p['id'],'assign-b','request-1234')
    assert s.orchestrator.tasks['patrol']['spec'].preferred_robot=='a'


def test_bounded_wait_returns_to_review_without_reconstructing_run():
    s=scene();service=RuntimeReplanning();run_id=s.run_id
    p=service.prepare(s,'patrol',.02);service.approve(s,p['id'],'wait','request-1234')
    s.step(100)
    assert s.status=='paused' and s.run_id==run_id
    assert any(e['kind']=='replan_attention_required' for e in s.events)


def test_no_role_replacement_for_started_or_cargo_task():
    s=scene();s.orchestrator.tasks['patrol'].update(status='running',started_at=s.time,robot_id='a')
    p=RuntimeReplanning().prepare(s,'patrol')
    assert [o['id'] for o in p['options']]==['wait']


def test_fixed_arm_envelope_is_included_in_return_route():
    from robot_platform.templates import example
    from robot_platform.orchestration import Orchestrator
    from robot_platform.plan_validation import initial_observation
    from robot_platform.navigation import radius, path_clear_of_disks
    p=example('warehouse-cooperation');o=Orchestrator(p,lambda *args:None)
    o.last_observations={r.id:initial_observation(p,r) for r in p.robots}
    robot=o.robots['cart'];obs=o.last_observations['cart'];obs['pose'].update(x=11.16,y=3,yaw=0)
    path=o._route(robot,obs,dict(x=7.4,y=6),'floor-1')
    peer=o.last_observations['receiver']['pose']
    disk=(peer['x'],peer['y'],radius(robot)+radius(o.robots['receiver'])+p.policy.safety_distance)
    assert path and path_clear_of_disks(obs['pose'],path,[disk])


def test_loaded_departure_uses_observed_heading_and_requires_donor_release():
    from robot_platform.templates import example
    from robot_platform.plan_validation import initial_observation
    p=example('warehouse-cooperation');s=Session(p);o=s.orchestrator;c=s.cooperative
    task=next(t for t in p.tasks if t.id=='return-delivery');rid='outbound-cart'
    observations={r.id:initial_observation(p,r) for r in p.robots}
    for obs in observations.values():
        obs['sensors']={'contacts':[], 'lidar':{'angles':[0.], 'ranges':[10.]}}
    observations[rid]['pose'].update(x=9.8025,y=2.9935,z=.3,yaw=.06532)
    feedback={'finger_contacts':[], 'bilateral_contact':False}
    observations['receiver']['sensors']['manipulation']={task.item_id:feedback}
    o.robot_states[rid]['task_id']=task.id
    c.executions[task.id]=dict(terminal=False,released=False,loading_committed=True,
        participants={'carrier':rid,'donor':'receiver','receiver':'final-arm'},
        result={'hold':False,'navigation_target':task.cooperation.carrier_destination.model_dump()},
        route=[task.cooperation.carrier_destination.model_dump()])
    before=deepcopy(observations)
    command=c.base_command(rid,0,observations)
    assert command['v']>0 and command['w']==0
    assert observations==before  # control must not move the measured pose
    feedback['bilateral_contact']=True
    assert c.base_command(rid,0,observations)['v']==0
    feedback['bilateral_contact']=False
    observations[rid]['sensors']['lidar']['ranges']=[.01]
    assert c.base_command(rid,0,observations)['v']==0
