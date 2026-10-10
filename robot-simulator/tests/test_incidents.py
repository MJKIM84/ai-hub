import pytest
from robot_platform.domain import FaultInjection, FaultTrigger, Project
from robot_platform.incidents import IncidentScheduler
from robot_platform.templates import example


def test_observed_completion_only_and_exactly_once_across_pause():
    f=FaultInjection(target_id='r',kind='communication',duration=3,auto_recover=True,
                     trigger=FaultTrigger(kind='task_status',task_id='load'))
    s=IncidentScheduler()
    assert not s.tick(1,[f],{'load':{'status':'running'}},[])
    actions=s.tick(2,[f],{'load':{'status':'completed','completed_at':2}},[])
    assert actions[0][1]['evidence']['task_id']=='load'
    for _ in range(5):assert not s.tick(2,[f],{'load':{'status':'completed'}},[])
    assert not s.tick(4.9,[f],{},[])
    assert s.tick(5,[f],{},[])[0][0].kind=='recover'
    assert not s.tick(9,[f],{'load':{'status':'completed'}},[])
    assert s.snapshot([f])[0]['count']==1


def test_new_fault_is_not_cleared_by_old_release_timer():
    first=FaultInjection(target_id='r',kind='communication',duration=3,auto_recover=True)
    later=FaultInjection(target_id='r',kind='motor',time=1)
    s=IncidentScheduler()
    s.tick(0,[first,later],{},[]);s.tick(1,[first,later],{},[])
    assert not s.tick(4,[first,later],{},[])


def test_repeat_consumes_distinct_matching_event_sequence_numbers():
    f=FaultInjection(target_id='r',kind='push',max_occurrences=2,
        trigger=FaultTrigger(kind='event',task_id='load',event_kind='cooperation_loaded'))
    s=IncidentScheduler()
    events=[dict(seq=1,time=1,kind='cooperation_loaded',entity_id='r',details={'task_id':'other'})]
    assert not s.tick(1,[f],{},events)
    events.append(dict(seq=2,time=2,kind='cooperation_loaded',entity_id='r',details={'task_id':'load'}))
    assert len(s.tick(2,[f],{},events))==1
    assert not s.tick(2,[f],{},events)
    events.append(dict(seq=3,time=3,kind='cooperation_loaded',entity_id='r',details={'task_id':'load'}))
    assert len(s.tick(3,[f],{},events))==1
    events.append(dict(seq=4,time=4,kind='cooperation_loaded',entity_id='r',details={'task_id':'load'}))
    assert not s.tick(4,[f],{},events)


def test_invalid_trigger_reference_and_non_reversible_recovery_rejected():
    p=example('hotel').model_dump()
    p['faults']=[dict(target_id=p['robots'][0]['id'],kind='communication',
                      trigger=dict(kind='task_status',task_id='missing'))]
    with pytest.raises(ValueError,match='조건 작업'):Project.model_validate(p)
    with pytest.raises(ValueError,match='자동 해제'):FaultInjection(target_id='r',kind='battery',auto_recover=True)


def test_runtime_incident_and_release_come_from_same_session():
    from robot_platform.runtime import Session
    p=example('hotel');p.tasks=[];p.people=[]
    target=p.robots[0].id
    p.faults=[FaultInjection(target_id=target,kind='communication',duration=.02,auto_recover=True)]
    session=Session(p);session.step(20)
    assert session.robot_faults[target]=='none'
    events=[e for e in session.events if e['kind'].startswith('incident_')]
    assert [e['kind'] for e in events]==['incident_triggered','incident_released']
    assert session.snapshot(False)['incidents'][0]['count']==1


def test_auto_fault_cannot_erase_preexisting_fault():
    from robot_platform.runtime import Session
    p=example('hotel');p.tasks=[];p.people=[];p.robots[0].fault='motor'
    p.faults=[FaultInjection(target_id=p.robots[0].id,kind='communication',duration=.01,auto_recover=True)]
    s=Session(p);s.step(20)
    assert s.robot_faults[p.robots[0].id]=='motor'
    assert s.snapshot(False)['incidents'][0]['phase']=='blocked'


def test_simultaneous_auto_fault_does_not_cancel_the_accepted_release():
    first=FaultInjection(target_id='r',kind='communication',duration=2,auto_recover=True)
    second=FaultInjection(target_id='r',kind='motor',duration=1,auto_recover=True)
    s=IncidentScheduler()
    actions=s.tick(0,[first,second],{},[],{'r':'none'})
    assert [a[1]['phase'] for a in actions]==['triggered','blocked']
    assert not s.tick(1,[first,second],{},[],{'r':'communication'})
    assert s.tick(2,[first,second],{},[],{'r':'communication'})[0][1]['phase']=='released'
    preexisting=IncidentScheduler()
    assert all(a[1]['phase']=='blocked' for a in preexisting.tick(0,[first,second],{},[],{'r':'sensor'}))
    assert not preexisting.tick(3,[first,second],{},[],{'r':'sensor'})
