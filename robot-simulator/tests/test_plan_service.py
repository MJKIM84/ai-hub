"""Approval/persistence tests with real compiler, Project, Session and API handlers.

TestClient deliberately does not run lifespan/background physics. Explicit step
is the only physics advance. Chat HTTP replies below are protocol unit mocks,
not an assertion that a natural-language model was connected or understood text.
"""
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
import io
import json
import threading
from types import SimpleNamespace

from fastapi import HTTPException
from fastapi.testclient import TestClient
import pytest

from robot_platform.api import create_app
from robot_platform.domain import Element, Environment, Floor, Pose, Project, RobotInstance, Size, Task
from robot_platform.plan_service import PlanService, ApproveRequest
from robot_platform.ontology import FIELDS
from robot_platform.runtime import Session
from robot_platform import assistant_provider


def small_project():
    return Project(id='approval-test',name='독립 승인 검사',
        robots=[RobotInstance(id='amr',model_id='amr',pose=Pose(x=2,y=2))],
        environment={'id':'map','elements':[
            Element(id='destination',name='실제 목적지',kind='room',floor_id='floor-1',
                pose=Pose(x=4,y=4),size=Size(x=3,y=3,z=.01))]})


def test_incident_target_excluded_from_fleet_prevents_approval(tmp_path):
    project=small_project()
    project.robots.append(RobotInstance(id='other',model_id='amr',pose=Pose(x=10,y=10)))
    host=SimpleNamespace(lock=threading.RLock(),session=Session(project))
    service=PlanService(host,tmp_path/'plans')
    intent=dict(kind='plan',goal='돌발 상황을 포함한 순찰',
        tasks=[dict(id='patrol',kind='patrol',robot_id='amr',destination_id='destination')],
        faults=[dict(time=0,target_id='other',kind='communication',duration=2,
            auto_recover=True,trigger=dict(kind='task_status',task_id='patrol',status='completed'))])
    plan=service.draft(project,intent,{'robot_ids':['amr']})
    assert not plan['compiled']['can_approve']
    assert any(row['code']=='incident_target_excluded' for row in plan['compiled']['blockers'])
    assert plan['intent']['faults']==intent['faults']


def test_plan_revisions_remain_in_history_after_revision(tmp_path):
    project=small_project()
    host=SimpleNamespace(lock=threading.RLock(),session=Session(project))
    service=PlanService(host,tmp_path/'plans')
    intent=dict(kind='plan',goal='목적지 순찰',tasks=[dict(kind='patrol',robot_id='amr',destination_id='destination')])
    first=service.draft(project,intent,{'robot_ids':['amr']})
    revised=service.draft(project,intent,{'robot_ids':['amr']},previous=service.load(first['id']))
    assert revised['version']==first['version']+1
    assert [row['version'] for row in service.versions(first['id'])]==[revised['version'],first['version']]
    assert service.load_version(first['id'],first['version'])['plan_hash']==first['plan_hash']


def test_occupied_destination_offers_recomputed_approval_choices(tmp_path):
    project=Project(id='conflict',environment=Environment(id='floorplan-conflict',floors=[Floor(id='f',width=12,depth=13)],
        elements=[Element(id='a',kind='room',floor_id='f',pose=Pose(x=2.5,y=5),size=Size(x=4,y=4)),
                  Element(id='b',kind='room',floor_id='f',pose=Pose(x=7,y=5),size=Size(x=4,y=4)),
                  Element(id='c',kind='room',floor_id='f',pose=Pose(x=7,y=9),size=Size(x=4,y=4)),
                  Element(id='d',kind='door',floor_id='f',pose=Pose(x=4.75,y=5),size=Size(x=1,y=2)),
                  Element(id='e',kind='door',floor_id='f',pose=Pose(x=7,y=7),size=Size(x=2,y=1))]),
        robots=[RobotInstance(id='r1',model_id='amr',floor_id='f',pose=Pose(x=2.5,y=5)),
                RobotInstance(id='r2',model_id='amr',floor_id='f',pose=Pose(x=7,y=5))])
    topology={'connections':[dict(from_id='a',to_id='b',via='d',condition='reviewed_door',width_m=2),
                             dict(from_id='b',to_id='c',via='e',condition='reviewed_door',width_m=2)]}
    request=dict(kind='plan',goal='순차 공간 순찰',tasks=[
        dict(id='one',kind='patrol',robot_id='r1',destination_id='b',source_id='a'),
        dict(id='two',kind='patrol',robot_id='r2',destination_id='c',source_id='b',predecessor_ids=['one'])])
    original=project.model_dump(mode='json')
    for kind in ('waiting_position','alternate_destination','task_order'):
        host=SimpleNamespace(lock=threading.RLock(),session=Session(project))
        service=PlanService(host,tmp_path/kind)
        service.floorplans.context=lambda _:dict(status='confirmed',graph=topology)
        blocked=service.draft(project,request,{'robot_ids':['r1','r2']})
        assert not blocked['compiled']['can_approve'] and not blocked['approval']
        options=blocked['compiled']['blockers'][0]['resolution_options']
        assert {option['kind'] for option in options}=={'waiting_position','alternate_destination','task_order'}
        option=next(option for option in options if option['kind']==kind)
        stale=dict(option,x=999)
        rejected=service.compile(project,request,{'robot_ids':['r1','r2'],'occupancy_resolution':stale})
        assert not rejected['can_approve'] and rejected['blockers'][-1]['code']=='occupancy_resolution_stale'
        revised=service.draft(project,request,{'robot_ids':['r1','r2'],'occupancy_resolution':option},
                              previous=service.load(blocked['id']))
        assert revised['version']==blocked['version']+1 and revised['compiled']['can_approve']
        assert revised['compiled']['occupancy_resolution']==option and host.session.time==0
        assert project.model_dump(mode='json')==original
        receipt=service.approve(revised['id'],approval(revised,project,'resolution-'+kind))
        assert receipt['version']==revised['version'] and host.session.project.model_dump(mode='json')==revised['compiled']['project']
        if kind=='waiting_position':assert host.session.project.robots[1].pose.x!=7
        if kind=='alternate_destination':assert host.session.project.tasks[0].destination.x!=7
        if kind=='task_order':assert host.session.project.tasks[0].id=='two'
        while host.session.time<120 and any(task['status'] not in ('completed','failed')
                                            for task in host.session.snapshot()['tasks']):
            host.session.step(500)
        completed=host.session.snapshot()
        assert [task['status'] for task in completed['tasks']]==['completed','completed'], (kind,
            [(r['id'],r['pose'],r.get('state'),r.get('waiting_reason')) for r in completed['robots']],
            [(t['id'],t['status'],t.get('waiting_reason')) for t in completed['tasks']])
        assert completed['metrics']['collisions']==completed['metrics']['near_misses']==0


@pytest.mark.parametrize('existing',[False,True])
def test_reviewed_route_detour_is_recompiled_and_only_executed_after_approval(tmp_path,existing):
    project=Project(id='route-detour',environment=Environment(id='map',floors=[Floor(id='f',width=12,depth=10)],
        elements=[Element(id='room',kind='room',floor_id='f',pose=Pose(x=6,y=5),size=Size(x=11,y=9))]),
        robots=[RobotInstance(id='r1',model_id='amr',floor_id='f',pose=Pose(x=2,y=5)),
                RobotInstance(id='r2',model_id='amr',floor_id='f',pose=Pose(x=6,y=5))],
        tasks=[Task(id='existing',kind='patrol',floor_id='f',preferred_robot='r1',
                    destination=Pose(x=10,y=5))] if existing else [])
    request=dict(kind='plan',goal='대기 로봇을 피해 같은 공간 순찰',tasks=[
        dict(existing_task_id='existing') if existing else
        dict(kind='patrol',robot_id='r1',source_id='room',destination_id='room',
             destination_xy={'x':10,'y':5})])
    host=SimpleNamespace(lock=threading.RLock(),session=Session(project))
    service=PlanService(host,tmp_path/'detour')
    service.floorplans.context=lambda _:dict(status='confirmed',graph={'connections':[]})
    blocked=service.draft(project,request,{'robot_ids':['r1']})
    assert not blocked['compiled']['can_approve'] and host.session.time==0
    blocker=next(b for b in blocked['compiled']['blockers'] if b['code']=='route_occupied_by_waiting_robot')
    option=next(o for o in blocker['resolution_options'] if o['kind']=='route_detour')
    revised=service.draft(project,request,{'robot_ids':['r1'],'occupancy_resolution':option},
                          previous=service.load(blocked['id']))
    assert revised['compiled']['can_approve'] and revised['version']==blocked['version']+1
    assert host.session.time==0 and not revised['approval']
    receipt=service.approve(revised['id'],approval(revised,project,'detour-approval'))
    assert receipt['version']==revised['version']
    task=host.session.project.tasks[0]
    assert [(p.x,p.y) for p in task.approved_route]==[(p['x'],p['y']) for p in option['points']]
    route=host.session.orchestrator._task_route(host.session.project.robots[0],
        {'pose':{'x':2,'y':5,'z':.3}},task)
    assert [(p['x'],p['y']) for p in route]==[(p['x'],p['y']) for p in option['points']]
    task_id='existing' if existing else 'intent-task-1'
    while host.session.time<40 and host.session.orchestrator.tasks[task_id]['status'] not in ('completed','failed'):
        host.session.step(500)
    snapshot=host.session.snapshot()
    assert snapshot['tasks'][0]['status']=='completed'
    assert snapshot['metrics']['collisions']==snapshot['metrics']['near_misses']==0


def test_reviewed_stairs_do_not_grant_robot_floor_transfer():
    project=Project(id='stair-only',robots=[RobotInstance(id='amr',model_id='amr',floor_id='floor-1',pose=Pose(x=2,y=2))],
        environment=Environment(id='floorplan-reviewed',floors=[Floor(id='floor-1'),Floor(id='floor-2',elevation=3.2)],
            elements=[Element(id='lower',kind='room',floor_id='floor-1',pose=Pose(x=2,y=2),size=Size(x=2,y=2,z=.01)),
                      Element(id='upper',kind='room',floor_id='floor-2',pose=Pose(x=2,y=2,z=3.2),size=Size(x=2,y=2,z=.01)),
                      Element(id='stairs',kind='stairs',floor_id='floor-1',pose=Pose(x=3,y=2),size=Size(x=1,y=1,z=3.2))]))
    service=PlanService.__new__(PlanService)
    service.floorplans=SimpleNamespace(context=lambda _:dict(status='confirmed',graph={'connections':[
        {'from_id':'lower','to_id':'upper','via':'stairs','condition':'reviewed_both_landings'}]}))
    compiled={'kind':'plan','can_approve':True,'steps':[{'id':'task','robot_ids':['amr'],'floor_id':'floor-2',
        'source':{'x':2,'y':2,'z':0},'destination':{'x':2,'y':2,'z':3.2},'valid':True}]}
    result=service._spatial_validate(project,compiled)
    assert not result['can_approve'] and not result['steps'][0]['valid']
    assert result['blockers'][0]['code']=='floorplan_stairs_execution_unsupported'
    assert project.robots[0].floor_id=='floor-1' and project.robots[0].pose.z==0


def intent(kind='plan'):
    return dict(kind=kind,goal='실제 목적지 순찰',tasks=[dict(kind='patrol',destination_id='destination')])


@pytest.fixture(autouse=True)
def no_external_model(monkeypatch):
    for key in ('ROBOT_LLM_BASE_URL','ROBOT_LLM_MODEL','OPENAI_BASE_URL','OPENAI_MODEL','OPENAI_API_KEY'):
        monkeypatch.delenv(key,raising=False)
    monkeypatch.setattr(assistant_provider,'build_opener',lambda *a:pytest.fail('unexpected external model request'))
    # ChatGPT is now the default. Keep this unauthenticated fixture independent
    # of the developer machine's real Codex credentials; assertions are unchanged.
    from robot_platform.codex_provider import AppServer, CodexError
    def disconnected(*args,**kwargs):
        raise CodexError("login_required","ChatGPT 인증이 필요합니다.")
    monkeypatch.setattr(AppServer,"call",disconnected)


@pytest.fixture
def service(tmp_path):
    host=SimpleNamespace(lock=threading.RLock(),session=Session(small_project()))
    return PlanService(host,tmp_path/'plans')


@pytest.fixture
def client(tmp_path):
    app=create_app(tmp_path)
    app.state.host.session=Session(small_project())
    with_socketless_client=TestClient(app,raise_server_exceptions=False)
    try:yield with_socketless_client
    finally:with_socketless_client.close()


def signature(session):
    return (session.run_id,session.status,session.time,session.world.data.qpos.tobytes(),
        session.world.data.qvel.tobytes(),session.project.model_dump_json(),deepcopy(session.orchestrator.task_rows()))


def draft(service,kind='plan'):
    result=service.draft(service.host.session.project,intent(kind))
    if kind=='plan':assert result['compiled']['can_approve'],result['compiled']
    return result


def approval(row,project,request_id='unit-approval-0001'):
    return ApproveRequest(version=row['version'],plan_hash=row['plan_hash'],source_project_hash=row['source_project_hash'],project=project,request_id=request_id)


def api_draft(client,kind='plan'):
    project=client.app.state.host.session.project.model_dump(mode='json')
    response=client.post('/api/plans',json={'project':project,'intent':intent(kind)})
    assert response.status_code==200,response.text
    return response.json(),project


def api_approve(client,row,project,request_id='unit-approval-0001'):
    return client.post(f"/api/plans/{row['id']}/approve",json=approval(row,Project.model_validate(project),request_id).model_dump(mode='json'))


def protocol_reply(monkeypatch,response,before_reply=None):
    """Only mock external HTTP transport; provider parser and service are real."""
    raw=json.dumps({'choices':[{'message':{'content':json.dumps(response)}}]}).encode()
    class Opener:
        def open(self,request,timeout):
            if before_reply:before_reply()
            return io.BytesIO(raw)
    monkeypatch.setattr(assistant_provider,'build_opener',lambda *handlers:Opener())


def configure_protocol(service):
    service.provider.configure(dict(base_url='http://127.0.0.1:9999/v1',model='unit-protocol-only',require_key=False))


def test_draft_computes_executable_preview_without_touching_session_or_editor(service):
    before=signature(service.host.session);p=service.host.session.project;original=p.model_dump()
    row=service.draft(p,intent(),{'robot_ids':['amr']})
    assert row['compiled']['can_approve'] and row['compiled']['project']['tasks']
    assert row['approval'] is None and service.active is None
    assert signature(service.host.session)==before and p.model_dump()==original
    assert 'source_project' not in row and 'runtime_binding' not in row
    stored=service.load(row['id']);assert stored['source_project']==original


def test_restored_plan_source_check_distinguishes_same_project_from_changes(client):
    row,project=api_draft(client)
    endpoint=f"/api/plans/{row['id']}/source-check"
    assert 'source_project' not in client.get(f"/api/plans/{row['id']}").json()
    assert client.post(endpoint,json={'version':row['version'],'project':project}).json()=={'matches':True}
    edited=deepcopy(project)
    edited['robots'][0]['pose']['x']+=.1
    assert client.post(endpoint,json={'version':row['version'],'project':edited}).json()=={'matches':False}
    assert client.post(endpoint,json={'version':row['version']+1,'project':project}).json()=={'matches':False}


def test_question_is_persisted_analysis_and_cannot_be_approved(service):
    before=signature(service.host.session);row=draft(service,'question')
    assert row['compiled']['kind']=='question' and not row['compiled']['can_approve']
    assert row['compiled']['project'] is None
    with pytest.raises(HTTPException) as error:service.approve(row['id'],approval(row,service.host.session.project))
    assert error.value.status_code==422 and signature(service.host.session)==before
    assert not list(service.folder.glob('approval-*.json'))


def test_approved_plan_creates_one_real_session_with_the_exact_compiled_configuration(service):
    old=service.host.session;row=draft(service)
    receipt=service.approve(row['id'],approval(row,old.project))
    actual=service.host.session
    assert actual is not old and actual.run_id==receipt['run_id'] and actual.status=='running'
    assert actual.project.model_dump(mode='json')==row['compiled']['project']
    assert actual.time==0 and receipt['status']=='accepted'
    assert actual.orchestrator.task_rows() and all(t['status']!='completed' for t in actual.orchestrator.task_rows())
    assert [e['kind'] for e in actual.events].count('plan_approved')==1
    assert json.loads((service.folder/f"result-{row['id']}.json").read_text())['snapshot']['run_id']==receipt['run_id']


def test_robot_replacement_requires_new_approval_and_changes_actual_assignment(tmp_path):
    p=small_project()
    p.robots.append(RobotInstance(id='amr-b',model_id='amr',pose=Pose(x=2,y=7)))
    host=SimpleNamespace(lock=threading.RLock(),session=Session(p))
    service=PlanService(host,tmp_path/'replacement')
    request=dict(kind='plan',goal='목적지 순찰',tasks=[dict(kind='patrol',robot_id='amr',destination_id='destination')])
    original=service.draft(p,request)
    assert original['compiled']['can_approve'] and original['compiled']['selected_robot_ids']==['amr']
    before=signature(host.session)
    revised=service.draft(p,request,{'robot_ids':['amr-b'],'task_robot_ids':{'intent-task-1':'amr-b'}},
                          previous=service.load(original['id']))
    assert revised['version']==original['version']+1 and revised['plan_hash']!=original['plan_hash']
    assert revised['compiled']['can_approve'] and signature(host.session)==before
    with pytest.raises(HTTPException) as error:
        service.approve(original['id'],approval(original,p))
    assert error.value.status_code==409 and signature(host.session)==before
    receipt=service.approve(revised['id'],approval(revised,p,'replacement-approval'))
    assert receipt['version']==revised['version']
    assert [r.id for r in host.session.project.robots]==['amr-b']
    assert host.session.project.tasks[0].preferred_robot=='amr-b'


def test_duplicate_same_and_new_request_ids_cannot_restart_an_approved_plan(service):
    old=service.host.session;row=draft(service);request=approval(row,old.project)
    first=service.approve(row['id'],request);actual=service.host.session
    actual.step(2);before=signature(actual)
    for duplicate in (request,approval(row,old.project,'another-request-0002')):
        response=service.approve(row['id'],duplicate)
        assert response['replayed'] and response['live'] and response['run_id']==first['run_id']
        assert service.host.session is actual and signature(actual)==before
    assert [e['kind'] for e in actual.events].count('plan_approved')==1


@pytest.mark.parametrize('terminal',['completed','failed','timed_out'])
def test_terminal_execution_requires_fresh_plan_approval_and_keeps_result(service,terminal):
    source=service.host.session.project
    first=draft(service)
    receipt=service.approve(first['id'],approval(first,source))
    previous=service.host.session
    previous.status=terminal
    service.checkpoint(force=True)
    repeated=service.approve(first['id'],approval(first,source,'terminal-duplicate'))
    assert repeated['run_id']==receipt['run_id'] and service.host.session is previous
    revised=service.draft(source,first['intent'],first['selection'],previous=service.load(first['id']))
    assert service.host.session is previous and not revised['approval']
    approved=service.approve(revised['id'],approval(revised,source,'terminal-new-revision'))
    assert approved['run_id']!=receipt['run_id']
    saved=service.result_for_run(first['id'],receipt['run_id'])
    assert saved['result']['snapshot']['status']==terminal


def test_concurrent_approval_clicks_create_only_one_actual_session(service):
    row=draft(service);request=approval(row,service.host.session.project)
    with ThreadPoolExecutor(max_workers=6) as pool:
        receipts=list(pool.map(lambda _:service.approve(row['id'],request),range(6)))
    assert len({r['run_id'] for r in receipts})==1
    assert sum(not r['replayed'] for r in receipts)==1
    assert [e['kind'] for e in service.host.session.events].count('plan_approved')==1


def test_request_id_cannot_be_rebound_to_a_different_plan(service):
    p=service.host.session.project;first=draft(service);second=draft(service)
    service.approve(first['id'],approval(first,p));before=signature(service.host.session)
    with pytest.raises(HTTPException) as error:service.approve(second['id'],approval(second,p))
    assert error.value.status_code==409 and signature(service.host.session)==before


@pytest.mark.parametrize('change',['editor','version','plan_hash','source_hash','runtime','running'])
def test_changed_editor_or_plan_or_runtime_rejects_without_creating_a_session(service,change):
    row=draft(service);p=service.host.session.project.model_copy(deep=True);request=approval(row,p)
    if change=='editor':request.project.name='편집 후 변경'
    elif change=='version':request.version+=1
    elif change=='plan_hash':request.plan_hash='wrong'
    elif change=='source_hash':request.source_project_hash='wrong'
    elif change=='runtime':service.host.session=Session(p)
    elif change=='running':service.host.session.status='running'
    before=signature(service.host.session)
    with pytest.raises(HTTPException) as error:service.approve(row['id'],request)
    assert error.value.status_code==409 and signature(service.host.session)==before
    assert not list(service.folder.glob('approval-*.json'))


def test_revision_invalidates_old_approval_and_archives_exact_prior_draft(client):
    row,p=api_draft(client);before=signature(client.app.state.host.session)
    revised=client.post(f"/api/plans/{row['id']}/revise",json={'version':1,'project':p,'selection':{'robot_ids':['amr'],'pedestrians':{'include':False,'total':0}}})
    assert revised.status_code==200,revised.text
    current=revised.json();assert current['version']==2 and current['plan_hash']!=row['plan_hash']
    assert api_approve(client,row,p).status_code==409
    assert signature(client.app.state.host.session)==before
    path=client.app.state.host.plan_service.folder/'revisions'/f"{row['id']}-1.json"
    assert json.loads(path.read_text())['plan_hash']==row['plan_hash']
    assert client.post(f"/api/plans/{row['id']}/revise",json={'version':1,'project':p,'selection':{}}).status_code==409


def test_approved_amendment_pauses_original_requires_reapproval_and_does_not_relaunch_on_old_receipt(client):
    row,p=api_draft(client);receipt=api_approve(client,row,p).json();host=client.app.state.host
    original=host.session
    revised=client.post(f"/api/plans/{row['id']}/revise",json={'version':1,'project':p,'selection':{'robot_ids':['amr']}})
    assert revised.status_code==200,revised.text
    assert host.session is original and original.status=='paused' and host.plan_service.amendment_required
    assert revised.json()['previous_approvals'][0]['run_id']==receipt['run_id']
    assert client.post('/api/control',json={'action':'resume'}).status_code==409
    replay=api_approve(client,row,p).json();assert replay['replayed'] and host.session is original and original.status=='paused'
    new=api_approve(client,revised.json(),p,'new-version-approval').json()
    assert new['run_id']!=receipt['run_id'] and host.session.status=='running' and not host.plan_service.amendment_required


def test_stopped_result_and_approved_input_survive_service_restart_without_reexecution(client):
    row,p=api_draft(client);receipt=api_approve(client,row,p).json();host=client.app.state.host
    host.session.step(4)
    stopped=client.post(f"/api/plans/{row['id']}/stop",json={"run_id":client.app.state.host.session.run_id})
    assert stopped.status_code==200 and host.session.status=='paused'
    assert host.plan_service.active is None
    recording=host.plan_service.folder/f"recording-{row['id']}.json"
    assert recording.exists() and json.loads(recording.read_text())['run_id']==receipt['run_id']
    reloaded_host=SimpleNamespace(lock=threading.RLock(),session=Session(small_project()))
    reloaded=PlanService(reloaded_host,host.plan_service.folder);before=signature(reloaded_host.session)
    replay=reloaded.approve(row['id'],approval(row,Project.model_validate(p)))
    assert replay['replayed'] and not replay['live'] and signature(reloaded_host.session)==before
    result=reloaded.result(row['id']);assert not result['live'] and not result['hardware_validation']
    assert result['result']['snapshot']['sim_time']==pytest.approx(.008)
    assert result['approval']['plan_hash']==row['plan_hash']


def test_unconfigured_chat_returns_explicit_error_and_does_not_create_a_draft_or_run(client):
    host=client.app.state.host;before=signature(host.session)
    response=client.post('/api/assistant/chat',json={'project':host.session.project.model_dump(mode='json'),'message':'실제 목적지로 이동해줘'})
    assert response.status_code==422 and '인증' in response.text
    assert signature(host.session)==before and client.get('/api/plans').json()==[]


def test_new_map_starts_a_separate_model_conversation(client,monkeypatch):
    row,old_project=api_draft(client)
    revised=deepcopy(old_project)
    revised['environment']['id']='another-reviewed-map'
    host=client.app.state.host
    seen=[]
    def reply(project,message,catalog,prior_intent,prior_conversation,**kwargs):
        seen.append((prior_intent,prior_conversation,kwargs['conversation_key']))
        return dict(answer='새 지도 기준 계획',references=[],intent=intent())
    monkeypatch.setattr(host.plan_service.provider,'interpret',reply)
    response=client.post('/api/assistant/chat',json={
        'project':revised,'plan_id':row['id'],'message':'새 지도에서 다시 계획해줘'})
    assert response.status_code==200,response.text
    proposal=response.json()
    assert proposal['id']!=row['id'] and proposal['version']==1
    assert seen[0][0] is None and seen[0][1] is None
    assert proposal['conversation_key']==seen[0][2]
    assert host.plan_service.load(row['id'])['version']==row['version']
    assert proposal['source_environment_id']=='another-reviewed-map'
    assert proposal['source_environment_version']==revised['environment']['version']


def test_question_about_active_plan_never_replaces_approval_or_changes_running_session(client,monkeypatch):
    row,p=api_draft(client);receipt=api_approve(client,row,p).json();host=client.app.state.host
    configure_protocol(host.plan_service)
    protocol_reply(monkeypatch,dict(answer='설명입니다',references=['amr'],intent=intent('question')))
    before=signature(host.session)
    response=client.post('/api/assistant/chat',json={'project':p,'plan_id':row['id'],'message':'어떻게 실행되나요?'})
    assert response.status_code==200,response.text
    assert response.json()['id']!=row['id'] and response.json()['compiled']['kind']=='question'
    assert signature(host.session)==before
    assert host.plan_service.load(row['id'])['approval']['run_id']==receipt['run_id']


def test_explicit_question_mode_overrides_model_plan_without_execution(client,monkeypatch):
    host=client.app.state.host;configure_protocol(host.plan_service)
    protocol_reply(monkeypatch,dict(answer='초안 제안',references=['amr'],intent=intent()))
    before=signature(host.session)
    response=client.post('/api/assistant/chat',json={'project':host.session.project.model_dump(mode='json'),'message':'분석만 요청','mode':'question'})
    assert response.status_code==200,response.text
    assert response.json()['compiled']['kind']=='question' and not response.json()['compiled']['can_approve']
    assert signature(host.session)==before


def test_question_keeps_model_citations_distinct_from_query_matched_documents(client,monkeypatch):
    host=client.app.state.host
    ontology=host.plan_service.ontology
    ontology.onboard_model({'id':'turtlebot3_burger','name':'ROBOTIS TurtleBot3 Burger'})
    source='# Manual\n## Navigation\n```capability\n'+json.dumps({
        'key':'inspect','name':'Navigation','meaning':'Navigation requires a reviewed map.',
        'parameters':[],'sdk_mapping':None})+'\n```\n'
    doc=ontology.register(dict(title='TurtleBot3 Navigation manual',model_id='turtlebot3_burger',
        version='r1',source_url='',text=source))
    cap=next(c for c in ontology.analyze(doc['id'])['capabilities'] if c['document_id']==doc['id'])
    ontology.review_capability(doc['id'],cap['id'],dict(status='confirmed',
        feature={key:deepcopy(cap[key]) for key in FIELDS},note='원문 대조'))
    def answer(project,message,catalog,prior_intent,prior_conversation,**kwargs):
        return dict(answer='등록한 Navigation 문서를 검토하세요.',references=[],
                    intent=dict(kind='question',goal=message,tasks=[]))
    monkeypatch.setattr(host.plan_service.provider,'interpret',answer)
    before=signature(host.session)
    reply=client.post('/api/assistant/chat',json={'project':host.session.project.model_dump(mode='json'),
        'message':'TurtleBot3 Navigation 기능이 있나요?','mode':'question'})
    assert reply.status_code==200,reply.text
    assistant=reply.json()['conversation'][-1]
    assert assistant['references']==[]
    assert assistant['related_documents']==[{'id':doc['id'],'title':'TurtleBot3 Navigation manual',
                                              'version':'r1'}]
    assert reply.json()['compiled']['kind']=='question' and signature(host.session)==before


def test_chat_rebases_inherited_robot_selection_after_new_placement(client,monkeypatch):
    row,old_project=api_draft(client)
    selected=client.post(f"/api/plans/{row['id']}/revise",json={
        'version':row['version'],'project':old_project,'selection':{'robot_ids':['amr'],
        'pedestrians':{'include':True,'total':1}}})
    assert selected.status_code==200,selected.text
    updated=selected.json()
    project=deepcopy(old_project)
    project['robots'][0]['id']='replacement-amr'
    host=client.app.state.host
    configure_protocol(host.plan_service)
    protocol_reply(monkeypatch,dict(answer='새 배치의 로봇으로 순찰',references=[],intent=intent()))
    response=client.post('/api/assistant/chat',json={
        'project':project,'plan_id':updated['id'],'message':'새 배치에서 순찰해줘'})
    assert response.status_code==200,response.text
    plan=response.json()
    assert plan['compiled']['can_approve']
    assert plan['compiled']['selected_robot_ids']==['replacement-amr']
    assert plan['selection']['pedestrians']=={'include':True,'total':1}


def test_plan_ids_and_request_ids_cannot_escape_the_persistence_folder(service):
    with pytest.raises(HTTPException) as error:service.load('../outside')
    assert error.value.status_code==404
    from pydantic import ValidationError
    row=draft(service)
    with pytest.raises(ValidationError):approval(row,service.host.session.project,'../../outside')


@pytest.mark.parametrize('action',['reset','task_cancel','robot_command','facility_target','project_change'])
def test_mutations_outside_approval_pause_and_preserve_physical_state(service,action):
    row=draft(service);service.approve(row['id'],approval(row,service.host.session.project));session=service.host.session
    before=signature(session)
    with pytest.raises(HTTPException) as error:service.guard(action)
    assert error.value.status_code==409 and session.status=='paused' and service.amendment_required
    after=signature(session);assert after[0]==before[0] and after[2:]==before[2:]
    assert any(e['kind']=='plan_amendment_required' for e in session.events)


def test_step_cannot_bypass_a_pending_reapproval_gate(client):
    row,p=api_draft(client);api_approve(client,row,p);host=client.app.state.host
    client.post(f"/api/plans/{row['id']}/revise",json={'version':1,'project':p,'selection':{'robot_ids':['amr']}})
    before=signature(host.session)
    response=client.post('/api/control',json={'action':'step','steps':1})
    assert response.status_code==409,response.text
    assert signature(host.session)==before


def test_model_reply_loaded_before_approval_cannot_overwrite_it_without_pausing(client,monkeypatch):
    row,p=api_draft(client);host=client.app.state.host;configure_protocol(host.plan_service)
    approved=[]
    def approve_while_provider_is_in_flight():
        approved.append(host.plan_service.approve(row['id'],approval(row,Project.model_validate(p),'during-model-wait')))
    changed=intent();changed['goal']='보행자를 제외하고 순찰'
    protocol_reply(monkeypatch,dict(answer='변경 초안',references=['amr'],intent=changed,selection={'pedestrians':{'include':False,'total':0}}),approve_while_provider_is_in_flight)
    response=client.post('/api/assistant/chat',json={'project':p,'plan_id':row['id'],'message':'사람 없이 계획해줘'})
    assert approved
    assert response.status_code in (200,409),response.text
    record=host.plan_service.load(row['id'])
    if response.status_code==200:
        assert host.session.status=='paused' and host.plan_service.amendment_required
        assert record['previous_approvals'][0]['run_id']==approved[0]['run_id']
    else:
        assert record['approval']['run_id']==approved[0]['run_id']


def test_delayed_model_reply_cannot_overwrite_a_more_recent_selection_revision(client,monkeypatch):
    row,p=api_draft(client);host=client.app.state.host;configure_protocol(host.plan_service);latest=[]
    def revise_while_provider_is_in_flight():
        latest.append(host.plan_service.draft(Project.model_validate(p),intent(),{'robot_ids':['amr'],'pedestrians':{'include':False,'total':0}},previous=host.plan_service.load(row['id'])))
    changed=intent();changed['goal']='오래된 모델 결과'
    protocol_reply(monkeypatch,dict(answer='늦은 응답',references=[],intent=changed),revise_while_provider_is_in_flight)
    response=client.post('/api/assistant/chat',json={'project':p,'plan_id':row['id'],'message':'새 계획'})
    assert response.status_code==409,response.text
    assert host.plan_service.load(row['id'])['plan_hash']==latest[0]['plan_hash']


def test_amendment_preserves_each_approved_runs_result_instead_of_overwriting_history(service):
    source=service.host.session.project;row=draft(service)
    first=service.approve(row['id'],approval(row,source))
    service.host.session.step(4)
    revised=service.draft(source,intent(),{'robot_ids':['amr'],'pedestrians':{'include':False,'total':0}},previous=service.load(row['id']))
    second=service.approve(revised['id'],approval(revised,source,'second-approved-run'))
    assert first['run_id']!=second['run_id']
    snapshots=[]
    for path in service.folder.rglob('*.json'):
        record=json.loads(path.read_text())
        if isinstance(record,dict) and isinstance(record.get('snapshot'),dict):snapshots.append(record['snapshot'])
    by_run={snapshot['run_id']:snapshot for snapshot in snapshots}
    assert first['run_id'] in by_run,'a later approved revision must not erase the earlier run result'
    assert by_run[first['run_id']]['sim_time']==pytest.approx(.008)
    assert second['run_id'] in by_run
    history=service.result_for_run(row['id'],first['run_id'])
    assert history['approval']['version']==1 and not history['live']
    assert history['result']['snapshot']['sim_time']==pytest.approx(.008)
    assert history['current_plan_version']==2
    with pytest.raises(HTTPException) as unknown:
        service.result_for_run(row['id'],'0'*32)
    assert unknown.value.status_code==404


def test_invalid_model_nested_identifier_produces_explanation_not_internal_server_error(client,monkeypatch):
    host=client.app.state.host;configure_protocol(host.plan_service)
    invalid=intent();invalid['tasks'][0]['destination_id']=['destination']
    protocol_reply(monkeypatch,dict(answer='잘못된 구조',references=[],intent=invalid))
    before=signature(host.session)
    response=client.post('/api/assistant/chat',json={'project':host.session.project.model_dump(mode='json'),'message':'순찰 계획'})
    assert response.status_code in (200,422),response.text
    if response.status_code==200:
        compiled=response.json()['compiled']
        assert not compiled['can_approve'] and compiled['project'] is None and compiled['blockers']
    assert signature(host.session)==before


def test_duplicate_approval_with_a_new_request_id_still_binds_that_id_to_the_same_plan(service):
    source=service.host.session.project;first=draft(service)
    service.approve(first['id'],approval(first,source,'first-request-id'))
    duplicate=service.approve(first['id'],approval(first,source,'duplicate-request-id'))
    assert duplicate['replayed']
    service.host.session.status='paused'
    second=draft(service)
    before=signature(service.host.session)
    with pytest.raises(HTTPException) as error:
        service.approve(second['id'],approval(second,service.host.session.project,'duplicate-request-id'))
    assert error.value.status_code==409
    assert signature(service.host.session)==before


@pytest.mark.parametrize('action',['start','resume','step'])
def test_stopped_approved_run_cannot_restart_through_generic_control(client,action):
    row,p=api_draft(client);api_approve(client,row,p);host=client.app.state.host
    assert client.post(f"/api/plans/{row['id']}/stop",json={"run_id":client.app.state.host.session.run_id}).status_code==200
    before=signature(host.session)
    response=client.post('/api/control',json={'action':action})
    assert response.status_code==409,response.text
    assert signature(host.session)==before


def test_scoped_plan_pause_resume_returns_the_exact_bound_session_and_does_not_advance_physics(client):
    row,p=api_draft(client);receipt=api_approve(client,row,p).json();host=client.app.state.host
    endpoint=f"/api/plans/{row['id']}/control"
    before=signature(host.session)
    paused=client.post(endpoint,json={'run_id':receipt['run_id'],'action':'pause'})
    assert paused.status_code==200,paused.text
    assert paused.json()['run_id']==receipt['run_id'] and paused.json()['status']=='paused'
    assert signature(host.session)[2:]==before[2:]
    resumed=client.post(endpoint,json={'run_id':receipt['run_id'],'action':'resume'})
    assert resumed.status_code==200,resumed.text
    assert resumed.json()['status']=='running' and resumed.json()['sim_time']==before[2]
    assert signature(host.session)==before


@pytest.mark.parametrize('mismatch',['run','plan'])
def test_stale_plan_controls_cannot_pause_another_actual_run(client,mismatch):
    row,p=api_draft(client);other,_=api_draft(client);receipt=api_approve(client,row,p).json();host=client.app.state.host
    before=signature(host.session)
    requested_plan=other['id'] if mismatch=='plan' else row['id']
    requested_run='different-historical-run' if mismatch=='run' else receipt['run_id']
    response=client.post(f"/api/plans/{requested_plan}/control",json={'run_id':requested_run,'action':'pause'})
    assert response.status_code==409,response.text
    assert signature(host.session)==before


def test_scoped_resume_respects_amendment_gate_and_stopped_state(client):
    row,p=api_draft(client);receipt=api_approve(client,row,p).json();host=client.app.state.host
    client.post(f"/api/plans/{row['id']}/revise",json={'version':1,'project':p,'selection':{'robot_ids':['amr']}})
    before=signature(host.session)
    endpoint=f"/api/plans/{row['id']}/control"
    assert client.post(endpoint,json={'run_id':receipt['run_id'],'action':'resume'}).status_code==409
    assert signature(host.session)==before
    assert client.post(f"/api/plans/{row['id']}/stop",json={"run_id":client.app.state.host.session.run_id}).status_code==200
    stopped=signature(host.session)
    assert client.post(endpoint,json={'run_id':receipt['run_id'],'action':'resume'}).status_code==409
    assert signature(host.session)==stopped


@pytest.mark.parametrize('status',['running','paused','completed','failed','timed_out'])
def test_approved_reset_rewinds_identical_configuration_and_archives_previous_run(client,status):
    row,p=api_draft(client);receipt=api_approve(client,row,p).json();host=client.app.state.host
    previous=host.session
    previous.stop_when_tasks_terminal=True
    initial=previous.world.data.qpos.tolist()
    previous.step(10);previous.status=status;previous.speed=4.
    previous_time=previous.time;project=previous.project.model_dump(mode='json')
    response=client.post(f"/api/plans/{row['id']}/reset",json={'run_id':receipt['run_id']})
    assert response.status_code==200,response.text
    reset=response.json();current=host.session
    assert current is not previous and current.run_id==reset['run_id']!=receipt['run_id']
    assert current.time==0 and current.status=='paused' and current.speed==1.
    assert current.world.data.qpos.tolist()==initial
    assert current.project.model_dump(mode='json')==project and current.stop_when_tasks_terminal
    assert current.frames==[] and current.collision_count==0 and current.near_count==0
    assert reset['version']==receipt['version'] and reset['plan_hash']==receipt['plan_hash']
    assert reset['reset_of']==receipt['run_id']
    saved=client.get(f"/api/plans/{row['id']}/runs/{receipt['run_id']}").json()
    assert saved['result']['snapshot']['sim_time']==previous_time
    assert saved['result']['snapshot']['status']==('paused' if status=='running' else status)
    recording=host.plan_service.folder/'recordings'/f"{receipt['run_id']}.json"
    archived=json.loads(recording.read_text());expected=previous.recording()
    # Process-wide peak RSS can rise after the archived snapshot. All physical
    # frames, events, task outcomes and other metrics must remain identical.
    archived['metrics'].pop('peak_process_memory_native')
    expected['metrics'].pop('peak_process_memory_native')
    assert archived==expected
    # Old controls and old approval requests must never start the new session.
    assert client.post(f"/api/plans/{row['id']}/control",json={'run_id':receipt['run_id'],'action':'resume'}).status_code==409
    repeated=api_approve(client,row,p).json()
    assert repeated['replayed'] and not repeated['live'] and repeated['run_id']==receipt['run_id']
    assert current.status=='paused' and current.time==0
    resumed=client.post(f"/api/plans/{row['id']}/control",json={'run_id':reset['run_id'],'action':'resume'})
    assert resumed.status_code==200 and host.session.status=='running'


def test_approved_reset_retry_is_idempotent_and_cannot_rewind_a_later_run(client):
    row,p=api_draft(client);receipt=api_approve(client,row,p).json();host=client.app.state.host
    endpoint=f"/api/plans/{row['id']}/reset";body={'run_id':receipt['run_id']}
    first=client.post(endpoint,json=body).json();current=host.session
    current.step(3);before=signature(current)
    repeated=client.post(endpoint,json=body)
    assert repeated.status_code==200 and repeated.json()['replayed']
    assert repeated.json()['run_id']==first['run_id'] and signature(host.session)==before
    second=client.post(endpoint,json={'run_id':first['run_id']}).json()
    assert second['run_id']!=first['run_id']
    before=signature(host.session)
    assert client.post(endpoint,json=body).status_code==409
    assert signature(host.session)==before


def test_approved_reset_cannot_bypass_changed_plan_or_change_project(client):
    row,p=api_draft(client);receipt=api_approve(client,row,p).json();host=client.app.state.host
    endpoint=f"/api/plans/{row['id']}/reset"
    before=signature(host.session)
    assert client.post(endpoint,json={'run_id':receipt['run_id'],'project':p}).status_code==422
    assert signature(host.session)==before
    revised=client.post(f"/api/plans/{row['id']}/revise",json={'version':1,'project':p,'selection':{'robot_ids':['amr']}})
    assert revised.status_code==200
    before=signature(host.session)
    assert client.post(endpoint,json={'run_id':receipt['run_id']}).status_code==409
    assert signature(host.session)==before and host.plan_service.amendment_required


@pytest.mark.parametrize('terminal',['completed','failed','timed_out'])
def test_pause_speed_and_rejected_mutation_preserve_terminal_result(client,terminal):
    row,p=api_draft(client);receipt=api_approve(client,row,p).json();host=client.app.state.host
    host.session.status=terminal;before=signature(host.session)
    response=client.post('/api/control',json={'action':'pause','speed':2.})
    assert response.status_code==200 and response.json()['status']==terminal
    response=client.post(f"/api/plans/{row['id']}/control",json={'run_id':receipt['run_id'],'action':'pause'})
    assert response.status_code==200 and response.json()['status']==terminal
    assert client.post('/api/control',json={'action':'step','steps':1}).status_code==409
    assert signature(host.session)==before
    assert client.post('/api/control',json={'action':'reset'}).status_code==409
    assert host.session.status==terminal


@pytest.mark.parametrize('replacement',['reset','editor'])
@pytest.mark.parametrize('amended',[False,True])
def test_explicit_new_manual_run_after_plan_stop_is_allowed_and_does_not_resume_old_run(client,replacement,amended):
    row,p=api_draft(client);receipt=api_approve(client,row,p).json();host=client.app.state.host
    if amended:
        response=client.post(f"/api/plans/{row['id']}/revise",json={'version':1,'project':p,'selection':{'robot_ids':['amr']}})
        assert response.status_code==200
    client.post(f"/api/plans/{row['id']}/stop",json={"run_id":client.app.state.host.session.run_id})
    replaced=client.post('/api/control',json={'action':'reset'}) if replacement=='reset' else client.put('/api/project',json=p)
    assert replaced.status_code==200,replaced.text
    new_run=host.session.run_id
    assert new_run!=receipt['run_id'] and host.session.status=='paused'
    response=client.post('/api/control',json={'action':'resume'})
    assert response.status_code==200,response.text
    assert host.session.run_id==new_run


@pytest.mark.parametrize('stale_body',[True,False])
def test_old_or_missing_run_id_cannot_stop_new_revision_execution(client,stale_body):
    row,p=api_draft(client);first=api_approve(client,row,p).json();host=client.app.state.host
    revised=client.post(f"/api/plans/{row['id']}/revise",json={'version':1,'project':p,'selection':{'robot_ids':['amr']}}).json()
    second=api_approve(client,revised,p,'revised-run-approval').json()
    assert second['run_id']!=first['run_id']
    before=signature(host.session)
    body={'run_id':first['run_id']} if stale_body else {}
    response=client.post(f"/api/plans/{row['id']}/stop",json=body)
    assert response.status_code==409,response.text
    assert signature(host.session)==before


def test_stopping_two_versions_preserves_each_full_run_recording(client):
    row,p=api_draft(client);first=api_approve(client,row,p).json();host=client.app.state.host
    host.session.step(4)
    response=client.post(f"/api/plans/{row['id']}/stop",json={'run_id':first['run_id']})
    assert response.status_code==200,response.text
    expected_first=deepcopy(host.session.recording())
    first_path=host.plan_service.folder/'recordings'/f"{first['run_id']}.json"
    assert first_path.exists(),'Stopping must archive the full run before a later version can replace it'
    first_bytes=first_path.read_bytes()
    assert json.loads(first_bytes)==expected_first

    revised=client.post(f"/api/plans/{row['id']}/revise",json={'version':1,'project':p,'selection':{'robot_ids':['amr']}})
    assert revised.status_code==200,revised.text
    approved=api_approve(client,revised.json(),p,'second-stopped-version')
    assert approved.status_code==200,approved.text
    second=approved.json();assert second['run_id']!=first['run_id']
    host.session.step(7)
    response=client.post(f"/api/plans/{row['id']}/stop",json={'run_id':second['run_id']})
    assert response.status_code==200,response.text
    second_path=host.plan_service.folder/'recordings'/f"{second['run_id']}.json"
    expected_second=deepcopy(host.session.recording())
    assert first_path.read_bytes()==first_bytes
    assert json.loads(second_path.read_text())==expected_second
    assert expected_first!=expected_second
    assert json.loads((host.plan_service.folder/f"recording-{row['id']}.json").read_text())==expected_second

    # A fresh service can still inspect both immutable histories without reexecution.
    reloaded_host=SimpleNamespace(lock=threading.RLock(),session=Session(small_project()))
    reloaded=PlanService(reloaded_host,host.plan_service.folder);before=signature(reloaded_host.session)
    assert json.loads((reloaded.folder/'recordings'/first_path.name).read_text())==expected_first
    assert json.loads((reloaded.folder/'recordings'/second_path.name).read_text())==expected_second
    assert signature(reloaded_host.session)==before


def test_model_empty_tasks_cannot_reuse_old_selection_to_approve_a_clarification(client,monkeypatch):
    row,p=api_draft(client);host=client.app.state.host;configure_protocol(host.plan_service)
    selected=client.post(f"/api/plans/{row['id']}/revise",json={'version':1,'project':p,'selection':{'robot_ids':['amr']}})
    assert selected.status_code==200,selected.text
    protocol_reply(monkeypatch,dict(answer='어느 목적지를 순찰할까요?',references=[],
        intent={'kind':'plan','goal':'목적지를 확인한 뒤 순찰','tasks':[]}))
    before=signature(host.session)
    response=client.post('/api/assistant/chat',json={'project':p,'plan_id':row['id'],'message':'다른 곳으로 변경해줘'})
    assert response.status_code==200,response.text
    proposal=response.json()
    assert proposal['selection']['robot_ids']==['amr']
    assert proposal['compiled']['clarifications'] and not proposal['compiled']['can_approve']
    assert signature(host.session)==before
    rejected=api_approve(client,proposal,p,'empty-model-clarification')
    assert rejected.status_code==422,rejected.text
    assert signature(host.session)==before and host.plan_service.active is None
    assert not list(host.plan_service.folder.glob('approval-*.json'))


def test_model_empty_tasks_keeps_its_actual_reason_instead_of_claiming_missing_destination(client,monkeypatch):
    host=client.app.state.host;configure_protocol(host.plan_service)
    project=host.session.project.model_dump(mode='json')
    protocol_reply(monkeypatch,dict(answer='출입구가 좁아 이 로봇의 통과를 제안하지 않습니다.',references=[],
        intent={'kind':'plan','goal':'오른쪽 방 순찰','tasks':[],
                'clarifications':['문 개구 폭과 로봇 통과 조건을 검토해 주세요.']}))
    response=client.post('/api/assistant/chat',json={'project':project,'message':'오른쪽 방을 순찰해줘'})
    assert response.status_code==200,response.text
    proposal=response.json()
    assert proposal['intent']['clarifications']==['문 개구 폭과 로봇 통과 조건을 검토해 주세요.']
    assert not proposal['compiled']['can_approve'] and host.session.time==0


def test_explicit_model_clarification_blocks_even_an_otherwise_executable_task(client,monkeypatch):
    host=client.app.state.host;configure_protocol(host.plan_service)
    p=host.session.project.model_dump(mode='json');before=signature(host.session)
    pending=intent();pending['clarifications']=['운행 시간을 먼저 선택해 주세요.']
    protocol_reply(monkeypatch,dict(answer='운행 시간 확인이 필요합니다.',references=['destination'],intent=pending))
    response=client.post('/api/assistant/chat',json={'project':p,'message':'목적지를 순찰하되 시간은 나중에 정할게'})
    assert response.status_code==200,response.text
    proposal=response.json()
    assert proposal['compiled']['clarifications'] and not proposal['compiled']['can_approve']
    assert api_approve(client,proposal,p,'explicit-clarification').status_code==422
    assert signature(host.session)==before


def test_manual_structured_empty_scenario_with_explicit_selection_remains_approvable(client):
    host=client.app.state.host;p=host.session.project.model_dump(mode='json');before=signature(host.session)
    response=client.post('/api/plans',json={'project':p,
        'intent':{'kind':'plan','goal':'작업 없이 로봇 구성을 관찰','tasks':[]},'selection':{'robot_ids':['amr']}})
    assert response.status_code==200,response.text
    proposal=response.json()
    assert proposal['origin']=='manual_structured' and proposal['compiled']['can_approve']
    assert not proposal['compiled']['clarifications'] and signature(host.session)==before
    approved=api_approve(client,proposal,p,'manual-empty-scenario')
    assert approved.status_code==200,approved.text
    assert host.session.run_id!=before[0] and host.session.project.tasks==[]


def test_malformed_clarification_items_are_rejected_by_model_boundary_and_compiler(client,monkeypatch):
    host=client.app.state.host;configure_protocol(host.plan_service)
    p=host.session.project.model_dump(mode='json');before=signature(host.session)
    malformed=intent();malformed['clarifications']=[{'question':'목적지?'}]
    protocol_reply(monkeypatch,dict(answer='잘못된 확인 구조',references=[],intent=malformed))
    response=client.post('/api/assistant/chat',json={'project':p,'message':'계획해줘'})
    assert response.status_code==422,response.text
    assert host.plan_service.provider.last_success is None
    compiled=host.plan_service.compile(host.session.project,malformed,{'robot_ids':['amr']})
    assert not compiled['can_approve'] and compiled['blockers']
    assert signature(host.session)==before and not client.get('/api/plans').json()
