"""Directed guided routing and charging allocation boundaries without truth."""
from copy import deepcopy
import math
import pytest
from robot_platform.domain import Project,RobotInstance,Element,Pose,Size,Task,Policy
from robot_platform.orchestration import Orchestrator


def setup(closed=True,with_charger=True):
    points=[(3,2),(3,4),(3,6),(3,7),(1.3,7),(1.3,2),(3,2)] if closed else [(3,2),(3,4)]
    elements=[Element(id='wait',kind='waiting',floor_id='floor-1',pose=Pose(x=3,y=6,yaw=math.pi/2))]
    if with_charger:elements.append(Element(id='c',kind='charger',floor_id='floor-1',pose=Pose(x=4.512,y=4),size=Size(x=1,y=1,z=.5)))
    p=Project(robots=[RobotInstance(id='g',model_id='agv',pose=Pose(x=3,y=2,yaw=math.pi/2),agv_route=[Pose(x=x,y=y) for x,y in points],battery_capacity_wh=8)],environment={'elements':elements},policy=Policy(charge_until=60),tasks=[Task(id='task',destination=Pose(x=3,y=4 if not closed else 7,yaw=math.pi/2),dwell=.1)])
    o=Orchestrator(p,lambda *args:None)
    geometry={'staging':dict(x=3.,y=4.,z=.3,yaw=0.),'target':dict(x=4.,y=4.,z=.3,yaw=0.)}
    if with_charger:
        o.charging.configure({('g','c'):geometry})
        o.charging.station_observations={'c':dict(sampled_at=1.,fault=False,contacts={})}
    obs=dict(robot_id='g',sampled_at=1.,pose=dict(x=3.,y=2.,z=.3,yaw=math.pi/2),fault='none',battery=100,upright=1.,velocity=[0.,0.,0.],angular_velocity=[0.,0.,0.],sensors={})
    return p,o,obs,geometry


def test_nonterminal_staging_and_downstream_clearance_proven_before_reservation():
    p,o,obs,g=setup();obs['battery']=19
    o.tick(1.,{'g':obs})
    plan=o.charging.plans['g']
    assert plan['guided_approach']['goal']['distance_along_m']==2
    assert plan['guided_approach']['points']==[g['staging']]
    parked=o.charging._parking('g',dict(pose=g['staging']),plan,1.)
    assert parked['x']==3 and parked['y']==6
    assert math.hypot(parked['x']-g['staging']['x'],parked['y']-g['staging']['y'])>1.76
    assert len(o.charging.manager.requests)==1


def test_no_downstream_parking_rejects_open_endpoint_before_acquiring_connector():
    p,o,obs,_=setup(closed=False);obs['battery']=19
    o.tick(1,{'g':obs})
    assert not o.charging.plans and not o.charging.manager.requests
    assert o.robot_states['g']['status']=='idle'


def test_staging_must_be_an_explicit_route_waypoint():
    p,o,obs,g=setup();obs['battery']=19
    o.charging.geometry[('g','c')]['staging']['y']=3
    o.tick(1,{'g':obs})
    assert not o.charging.manager.requests


def test_return_route_unavailable_is_not_a_zero_distance_energy_pass():
    p,o,obs,_=setup(closed=False)
    o.tick(1,{'g':obs})
    record=o.tasks['task']
    assert record['status']=='waiting' and '순방향' in record['reason']
    assert record['energy_budget']['return_route_required']
    assert not record['energy_budget']['return_route_available']
    assert not o.count['g']


def test_no_charger_scene_keeps_existing_one_way_task_support():
    p,o,obs,_=setup(closed=False,with_charger=False)
    o.tick(1,{'g':obs})
    assert o.tasks['task']['status']=='running'


def test_one_way_zone_forbids_reverse_directed_segment():
    p,o,obs,g=setup()
    o.project.environment.elements.append(Element(id='one',kind='one_way',floor_id='floor-1',pose=Pose(x=3,y=3,yaw=-math.pi/2),size=Size(x=2,y=2,z=.01)))
    assert o._route(p.robots[0],obs,g['staging'],'floor-1') is None
    assert o.guided_rejections['g']=='opposite_one_way'


def test_route_budget_is_read_only_and_progress_only_uses_fresh_observations():
    p,o,obs,g=setup()
    o._observe_guided_progress(p.robots[0],obs,1)
    original=deepcopy(o.guided_progress)
    for stamp,now in [(1,1.5),(.9,1.5),(2,1.5),(float('nan'),1.5),(1.1,3.)]:
        newer=deepcopy(obs);newer['sampled_at']=stamp;newer['pose']['y']=5
        o._observe_guided_progress(p.robots[0],newer,now)
        assert o.guided_progress==original
    route=o._route(p.robots[0],obs,p.tasks[0].destination.model_dump(),'floor-1')
    budget=o.charging.task_budget(p.robots[0],p.tasks[0],obs,route)
    assert budget['guided_return']['route_distance_m']==pytest.approx(10.4)
    assert budget['guided_return']['dock_distance_m']==budget['guided_return']['undock_distance_m']==1
    assert budget['guided_return']['clearance_distance_m']==2
    assert o.guided_progress==original


def test_empty_path_is_not_actual_xy_arrival():
    p,o,obs,_=setup(with_charger=False);o.tick(1,{'g':obs})
    state=o.robot_states['g'];record=o.tasks['task']
    state['path']=[];record['arrival_at']=0.
    obs['sampled_at']=1.2;obs['pose'].update(y=6.7)
    command=o.tick(1.2,{'g':obs})['g']
    assert record['status']=='running' and record['arrival_at'] is None
    assert state['path']==[p.tasks[0].destination.model_dump()]
    assert command['v']==0


def test_clearing_dwell_rejects_duplicate_future_reordered_and_stale_samples():
    p,o,obs,g=setup();obs['battery']=19;o.tick(1,{'g':obs})
    plan=o.charging.plans['g'];plan.update(clearing=True,parking=dict(x=3,y=6,z=.3,yaw=math.pi/2))
    obs['pose'].update(y=6);obs['sampled_at']=2.
    o.charging.prepare(2.,{'g':obs})
    assert plan['clear_since']==2.
    o.charging.prepare(2.4,{'g':obs})
    assert 'g' in o.charging.plans
    invalid=deepcopy(obs);invalid['sampled_at']=3.
    o.charging.prepare(2.4,{'g':invalid});assert plan['clear_since'] is None
    invalid['sampled_at']=1.9;o.charging.prepare(2.4,{'g':invalid});assert plan['clear_since'] is None
    obs['sampled_at']=2.5;o.charging.prepare(2.5,{'g':obs});assert plan['clear_since']==2.5
    o.charging.prepare(4.,{'g':obs});assert plan['clear_since'] is None
    obs['sampled_at']=4.1;o.charging.prepare(4.1,{'g':obs})
    obs['sampled_at']=4.45;o.charging.prepare(4.45,{'g':obs})
    assert 'g' not in o.charging.plans


def test_reordered_or_changed_duplicate_pose_cannot_reuse_cached_on_route():
    p,o,obs,_=setup(with_charger=False)
    assert o.tick(1,{'g':obs})['g']['v']>0
    for stamp in (.9,1.):
        wrong=deepcopy(obs);wrong['sampled_at']=stamp;wrong['pose']['x']=4
        wrong['pose']['yaw']=math.atan2(5,-1)
        command=o.tick(1.1,{'g':wrong})['g']
        assert command['v']==command['w']==0


def test_task_arrival_dwell_requires_advancing_source_time_and_resets_after_gap():
    p,o,obs,_=setup(with_charger=False);p.tasks[0].dwell=.5;o.tasks['task']['spec'].dwell=.5
    o.tick(1,{'g':obs})
    obs['sampled_at']=2;obs['pose']['y']=7
    o.robot_states['g']['path']=[]
    o.tick(2,{'g':obs});o.tick(2.6,{'g':obs})
    assert o.tasks['task']['status']=='running'
    obs['sampled_at']=2.8;o.tick(2.8,{'g':obs})
    assert o.tasks['task']['arrival_at']==2.8
    for stamp in (3.,3.2,3.4):
        obs['sampled_at']=stamp;o.tick(stamp,{'g':obs})
    assert o.tasks['task']['status']=='completed'


def test_reordered_charging_motion_cannot_drive_from_unapproved_pose():
    p,o,obs,g=setup();obs['battery']=19;o.tick(1,{'g':obs})
    o.charging.intentions={'g':dict(action='approach')}
    assert o.charging.command('g',obs,1)['v']>0
    wrong=deepcopy(obs);wrong['sampled_at']=.9;wrong['pose']['y']=3
    command=o.charging.command('g',wrong,1.1)
    assert command['v']==command['w']==0


def test_explicit_resume_replans_instead_of_reusing_stop_cleared_route():
    p,o,obs,_=setup();obs['battery']=19;o.tick(1,{'g':obs})
    plan=o.charging.plans['g'];plan.update(route_started=True,clearing=True,clear_since=1.,clear_sampled_at=1.,parking=dict(x=3,y=6,z=.3,yaw=math.pi/2))
    station=o.charging.manager.stations['c'];station.active=station.queue.popleft()
    station.active.status='active';station.active.phase='approach'
    o.charging.interrupt('g','operator_hold')
    assert plan['clear_since'] is None
    o.charging.recover('g')
    assert 'g' in o.charging.plans
    assert not plan['route_started'] and plan['clear_since'] is None
    assert 'clear_sampled_at' not in plan
    o.robot_states['g']['path']=[]
    obs['sampled_at']=1.2;obs['pose']['y']=2.5
    o.charging.command('g',obs,1.2)
    assert o.robot_states['g']['path'][0]['y']==4


@pytest.mark.parametrize("offset",[-.07,.07])
@pytest.mark.parametrize("clearing",[False,True])
def test_guided_charging_final_tolerance_does_not_reinsert_consumed_goal(offset,clearing):
    p,o,obs,g=setup();obs['battery']=19;o.tick(1.,{'g':obs})
    plan=o.charging.plans['g'];plan['route_started']=True
    target=dict(x=3.,y=6. if clearing else 4.,z=.3,yaw=math.pi/2)
    if clearing:plan.update(clearing=True,parking=target)
    else:plan['geometry']['staging']=target
    o.charging.intentions={'g':dict(action='approach')}
    state=o.robot_states['g'];state['path']=[]
    obs['sampled_at']=1.2;obs['pose'].update(x=3.,y=target['y']+offset,yaw=math.pi/2)
    command=o.charging.command('g',obs,1.2)
    assert state['path']==[]
    assert command['v']==command['w']==0
    assert not plan.get('interrupted')


@pytest.mark.parametrize("charging",[False,True])
def test_passed_within_tolerance_vertex_is_not_reinserted_by_route_projection(charging):
    p,o,obs,_=setup(with_charger=charging)
    if charging:obs['battery']=19
    o.tick(1.,{'g':obs})
    obs['sampled_at']=1.2;obs['pose'].update(x=3.038,y=3.9995)
    state=o.robot_states['g']
    if charging:
        o.charging.plans['g'].update(route_started=True,clearing=True,parking=dict(x=3.,y=6.,z=.3,yaw=math.pi/2))
        state['path']=[dict(x=3.,y=4.,z=0.,yaw=math.pi/2),dict(x=3.,y=6.,z=.3,yaw=math.pi/2)]
        command=o.charging.command('g',obs,1.2)
    else:command=o.tick(1.2,{'g':obs})['g']
    assert state['path'][0]['y']==6.
    assert command['v']>0
    assert not any(point['y']==4 for point in state['path'])
