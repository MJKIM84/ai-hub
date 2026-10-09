"""Safety/semantics of speed and hot-path changes; timings are recorded separately."""
import math
import pytest
from robot_platform.catalog import models,model_by_id,model_footprint
from robot_platform.domain import RobotInstance,Equipment,Size,Project,Environment,Floor,Pose,Task,Policy,Person,PedestrianAvoidance
from robot_platform.navigation import Planner,radius
from robot_platform.physics import PhysicsWorld
from robot_platform.templates import example
from robot_platform.orchestration import Orchestrator
from robot_platform.runtime import Session

def test_catalog_lookup_does_not_share_mutable_state():
    for row in models():
        assert row==model_by_id(row['id'])
        assert tuple(row['size'][key] for key in ('x','y'))==model_footprint(row['id'])
    spec=model_by_id('spot');spec['size']['x']=0;spec['limitations'].append('mutated')
    assert model_by_id('spot')['size']['x']>0
    assert 'mutated' not in model_by_id('spot')['limitations']

def test_planner_cache_never_survives_equipment_or_map_edits():
    p=example('warehouse');planner=Planner(p.environment);r=p.robots[2]
    assert not planner.blocked(5,5,'floor-1',r)
    r.equipment=[Equipment(kind='cargo_tray',mass=1,size=Size(x=12,y=12,z=.1),capacity=1)]
    assert radius(r)>8
    assert planner.path(dict(x=5,y=5),dict(x=6,y=5),'floor-1',r) is None
    r.equipment=[]
    assert planner.path(dict(x=5,y=5),dict(x=6,y=5),'floor-1',r)
    p.environment.floors[0].width=4
    assert planner.path(dict(x=5,y=5),dict(x=6,y=5),'floor-1',r) is None

@pytest.mark.parametrize('speed',[.4,1.])
def test_spot_actuator_gait_tracks_speed_and_stops_without_base_writes(speed):
    p=Project(environment=Environment(floors=[Floor(id='floor-1',width=40,depth=20)]),robots=[RobotInstance(id='s',model_id='spot',pose=Pose(x=3,y=10))])
    w=PhysicsWorld(p);cruise=[];upright=[]
    for i in range(10000):
        active=500<=i<7000
        w.command('s',v=speed if active else 0,w=0,mode='walk' if active else 'stop');w.step()
        if i%50==0:
            truth=w.truth('s');upright.append(truth['upright'])
            if 4000<i<7000:cruise.append(truth['velocity'][0])
    assert sum(cruise)/len(cruise)==pytest.approx(speed,abs=.12)
    assert min(upright)>.98
    assert math.hypot(*w.truth('s')['velocity'][:2])<.03

def test_spot_does_not_consume_peer_route_goal_outside_its_tighter_tolerance():
    r=RobotInstance(id='s',model_id='spot',pose=Pose(x=2,y=2),max_speed=1.)
    t=Task(id='move',preferred_robot='s',destination=Pose(x=4,y=2))
    c=Orchestrator(Project(robots=[r],tasks=[t]),lambda *args:None)
    obs=dict(robot_id='s',sampled_at=1.,pose=dict(x=2.,y=2.,z=.45,yaw=0.),
             fault='none',battery=100.,upright=1.,velocity=[0.,0.,0.],angular_velocity=[0.,0.,0.],sensors={})
    c.tick(1.,{'s':obs})
    c.robot_states['s'].update(peer_route=True,path=[t.destination.model_dump()])
    obs.update(sampled_at=1.2);obs['pose']['x']=3.92
    c.tick(1.2,{'s':obs})
    assert c.robot_states['s']['path']
    assert c.tasks['move']['arrival_at'] is None

def test_faster_spot_yields_to_moving_person_then_completes_with_clearance():
    p=Project(environment=Environment(floors=[Floor(id='floor-1',width=30,depth=20)]),
        robots=[RobotInstance(id='s',model_id='spot',pose=Pose(x=3,y=10),max_speed=1.)],
        policy=Policy(speed_limit=1.,pedestrian_avoidance=PedestrianAvoidance(strategy='yield')),
        tasks=[Task(id='move',preferred_robot='s',destination=Pose(x=10,y=10),timeout=60,dwell=.5)],
        people=[Person(id='p',pose=Pose(x=7,y=8),path=[Pose(x=7,y=8),Pose(x=7,y=13)],speed=.6)])
    s=Session(p,stop_when_tasks_terminal=True);s.status='running'
    while s.status=='running' and s.time<60:s.step(100)
    metrics=s.metrics()
    assert s.orchestrator.tasks['move']['status']=='completed'
    assert metrics['per_robot']['s']['waiting_seconds']>0
    assert metrics['pedestrian_min_clearance_m']['s']>=.5
    assert metrics['collisions']==metrics['near_misses']==metrics['falls']==0
    assert s.snapshot(include_geometry=False)['people']['p']['actual_position'][1]>9
