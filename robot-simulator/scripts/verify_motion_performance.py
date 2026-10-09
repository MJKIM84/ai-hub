"""Bounded local motion measurements; no hardware or model-service calls."""
from pathlib import Path
import json, time, math
from robot_platform.domain import Project, Environment, Floor, RobotInstance, Pose, Task, Policy
from robot_platform.templates import example
from robot_platform.physics import PhysicsWorld
from robot_platform.runtime import Session
from robot_platform.controllers.spot import SpotController

OUT = Path(__file__).resolve().parents[1] / 'docs/validation/motion-performance-2026-10-09'
def project():
    return Project(environment=Environment(floors=[Floor(id='floor-1',width=50,depth=20)]),
        robots=[RobotInstance(id='s',model_id='spot',pose=Pose(x=3,y=10),max_speed=1.)],policy=Policy(speed_limit=1.))

def main():
    results={'controller':SpotController.VERSION,'spot':[], 'routes':[]}
    for speed in (.4,.8,1.):
        w=PhysicsWorld(project());samples=[]
        for i in range(10000):
            active=500<=i<7000
            w.command('s',v=speed if active else 0,w=0,mode='walk' if active else 'stop');w.step()
            if i%50==0:
                t=w.truth('s');samples.append(dict(t=w.data.time,**t['pose'],vx=t['velocity'][0],speed=math.hypot(*t['velocity'][:2]),upright=t['upright']))
        cruise=[t['vx'] for t in samples if 8<t['t']<14]
        results['spot'].append(dict(command_m_s=speed,mean_m_s=sum(cruise)/len(cruise),min_upright=min(t['upright'] for t in samples),stop_speed=samples[-1]['speed'],samples=samples))
    for target in ((10,10,0),(9,14,1.57)):
        p=project();p.tasks=[Task(id='move',preferred_robot='s',destination=Pose(x=target[0],y=target[1],yaw=target[2]),timeout=45,dwell=.3)]
        s=Session(p,stop_when_tasks_terminal=True);s.status='running';samples=[]
        while s.status=='running' and s.time<46:
            s.step(100);t=s.world.truth('s');samples.append(dict(t=s.time,**t['pose'],speed=math.hypot(*t['velocity'][:2]),upright=t['upright'],reason=s.orchestrator.robot_states['s']['reason']))
        results['routes'].append(dict(target=target,sim_s=s.time,tasks=s.orchestrator.task_rows(),metrics=s.metrics(),samples=samples))
    p=Project.model_validate_json((OUT/'crossing-project.json').read_text());s=Session(p,stop_when_tasks_terminal=True);s.status='running';samples=[]
    while s.status=='running' and s.time<60:
        s.step(100);samples.append(dict(time=s.time,robot=s.world.truth('s'),person=s.snapshot(include_geometry=False)['people']['p'],reason=s.orchestrator.robot_states['s']['reason']))
    results['crossing']=dict(sim_s=s.time,tasks=s.orchestrator.task_rows(),metrics=s.metrics(),samples=samples)
    p=example('warehouse');s=Session(p);s.status='running';samples=[]
    while s.time<60 and s.orchestrator.tasks['task-1']['status']!='completed':
        s.step(500);samples.append(dict(time=s.time,robot=s.world.truth('robot-1'),reason=s.orchestrator.robot_states['robot-1']['reason']))
    results['warehouse_peer_arrival']=dict(sim_s=s.time,tasks=s.orchestrator.task_rows(),metrics=s.metrics(),samples=samples)
    p=Project.model_validate_json((OUT/'baseline-project.json').read_text());s=Session(p);start=time.perf_counter();s.step(1000);elapsed=time.perf_counter()-start
    results['warehouse']=dict(sim_s=s.time,wall_s=elapsed,factor=s.time/elapsed,steps=1000,robots=8,people=1,seed=42)
    (OUT/'after.json').write_text(json.dumps(results,indent=2))
    summary={**results,'spot':[{k:v for k,v in r.items() if k!='samples'} for r in results['spot']],
        'routes':[{k:v for k,v in r.items() if k not in ('samples','metrics')} for r in results['routes']]}
    for name in ('crossing','warehouse_peer_arrival'):
        summary[name]={k:v for k,v in results[name].items() if k not in ('samples','metrics')}
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
