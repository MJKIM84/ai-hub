"""Local compiler approval -> observed incident -> recovery -> second task.

No LLM call: validates the structured contract and physical execution only.
"""
import json
from pathlib import Path
import threading
from types import SimpleNamespace
from uuid import uuid4
from robot_platform.domain import Project, RobotInstance, Pose, Element, Size, Person, PersonBehavior
from robot_platform.runtime import Session
from robot_platform.plan_service import PlanService, ApproveRequest
from robot_platform.experiments import manifest


def run(offset,folder):
    p=Project(id=f'incident-flow-{offset}',name='두 구역 순찰 · 관측 사건 통신 장애',
        robots=[RobotInstance(id='amr',model_id='amr',pose=Pose(x=2,y=2))],
        people=[Person(id='pedestrian',pose=Pose(x=5,y=5),behavior=PersonBehavior(
            mode='destinations',destinations=[Pose(x=5,y=5),Pose(x=7,y=5)],speed_min_m_s=.5,speed_max_m_s=.5))],
        environment={'elements':[
            Element(floor_id='floor-1',id='first',name='첫 확인 구역',kind='room',pose=Pose(x=3,y=2),size=Size(x=1,y=1,z=.01)),
            Element(floor_id='floor-1',id='second',name='후속 구역',kind='room',pose=Pose(x=5+offset,y=2),size=Size(x=1,y=1,z=.01)),
            Element(floor_id='floor-1',id='charger',kind='charger',pose=Pose(x=8,y=8),size=Size(x=1.2,y=1.2,z=.025))]},auto_stop_after_seconds=60)
    host=SimpleNamespace(lock=threading.RLock(),session=Session(p));service=PlanService(host,folder/'plans')
    intent=dict(kind='plan',goal='첫 구역 후 통신 장애를 복구하고 후속 구역 순찰',tasks=[
        dict(id='first-task',kind='patrol',robot_id='amr',destination_id='first',dwell=.2),
        dict(id='second-task',kind='patrol',robot_id='amr',destination_id='second',predecessor_ids=['first-task'],dwell=.2)],
        faults=[dict(target_id='amr',kind='communication',time=0,duration=2,auto_recover=True,
                     trigger=dict(kind='task_status',task_id='first-task',status='completed'))])
    plan=service.draft(p,intent,dict(robot_ids=['amr']))
    if not plan['compiled']['can_approve']:raise AssertionError(plan['compiled']['blockers'])
    service.approve(plan['id'],ApproveRequest(version=plan['version'],plan_hash=plan['plan_hash'],
        source_project_hash=plan['source_project_hash'],project=p,request_id='incident-'+plan['id']))
    session=host.session;before=manifest(session.project)
    while session.status=='running':session.step(100)
    result=dict(manifest=before,final=session.snapshot(False),events=session.events)
    folder.mkdir(parents=True,exist_ok=True);(folder/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(offset,session.status,session.time,[(t['id'],t['status'],t.get('reason')) for t in session.orchestrator.task_rows()],flush=True)
    assert session.status=='completed'
    assert [e['kind'] for e in session.events if e['kind'] in ('incident_triggered','incident_released')]==['incident_triggered','incident_released']
    assert all(t['status']=='completed' for t in session.orchestrator.task_rows())


if __name__=='__main__':
    folder=Path('reports/resilience')/uuid4().hex
    print(folder,flush=True)
    for offset in (0,1):run(offset,folder/f'incident-{offset}')
