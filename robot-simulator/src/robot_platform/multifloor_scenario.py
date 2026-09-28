"""Authored research scenario inputs. No special execution or success logic.

All tasks use the ordinary dependency scheduler, contact workflows and lift.
Changing final_bay moves the final station and its authored rendezvous together.
"""
import json
import math
from pathlib import Path

from .domain import Project


def cargo_scenario(*, final_bay_x=13.5):
    root = Path(__file__).resolve().parents[2]
    data = json.loads((root/'examples/cooperative-loading.json').read_text())
    data.update(id='scenario-multifloor-cargo', name='다층 물품 업무 · 상차부터 최종 인계까지')
    data['environment'].update(id='environment-multifloor-cargo', name='가상 물류 작업장 · 2개 층')
    for f in data['environment']['floors']:f.update(width=20,depth=12)
    data['environment']['floors'].append(dict(id='floor-2',name='2층 작업·인계',elevation=3.2,width=20,depth=12))
    data['environment']['floors'][0]['name']='1층 창고·순찰'
    elements = data['environment']['elements']
    lift = json.loads((root/'examples/elevator-pedestrian-60s.json').read_text())['environment']['elements'][0]
    elements.append(lift)
    def element(key,kind,name,floor,x,y,sx,sy,sz=.01,**extra):
        row=dict(id=key,kind=kind,name=name,floor_id=floor,pose=dict(x=x,y=y),size=dict(x=sx,y=sy,z=sz))
        row.update(extra);elements.append(row);return row
    for floor in ('floor-1','floor-2'):
        for index,(x,y,sx,sy) in enumerate(((10,.1,20,.2),(10,11.9,20,.2),(.1,6,.2,12),(19.9,6,.2,12))):
            element(f'{floor}-outer-{index}','wall','외벽',floor,x,y,sx,sy,2.7)
    element('warehouse','room','창고','floor-1',1.9,3,3,4)
    element('warehouse-source','loading','물품 수령 위치','floor-1',1.9,3.55,.35,.4)
    element('hall-1','corridor','1층 공유 복도','floor-1',6,2.7,5,3)
    element('hall-2','corridor','2층 공유 복도','floor-2',6.7,2.7,5.8,3)
    for floor in ('floor-1','floor-2'):
        element(f'{floor}-walking','corridor','보행 구역 · 문 작동 범위 제외',floor,6.2,2,5,2.6)
    element('workroom','room','작업실','floor-2',9.3,3.3,3,4)
    element('handoff-zone','room','최종 인계 구역','floor-2',final_bay_x,3.3,3,4)
    element('worktable','workbench','작업실 작업대','floor-2',8.95,4.0,.4,.4,.20)
    element('handoff-table','workbench','최종 물품 받침','floor-2',final_bay_x-.55,4.0,.4,.4,.20)
    element('work-rendezvous','waiting','작업실 운반차 인계 위치','floor-2',9.848,3,.6,.6,
            pose=dict(x=9.848,y=3,z=.3,yaw=0))
    element('final-rendezvous','waiting','최종 운반차 인계 위치','floor-2',final_bay_x+.348,3,.6,.6,
            pose=dict(x=final_bay_x+.348,y=3,z=.3,yaw=0))
    element('spot-patrol-area','corridor','Spot 순찰 복도','floor-1',10,9,16,3)
    element('patrol-end','waiting','Spot 순찰 종점','floor-1',10,9,1,1)
    for floor,x in (('floor-1',3.6),('floor-2',11.3)):
        element(f'{floor}-partition-low','wall','문 아래 경계',floor,x,.65,.15,1.3,2.7)
        element(f'{floor}-partition-high','wall','문 위 경계',floor,x,6.1,.15,3.8,2.7)
        element(f'{floor}-door','door','공유 통로 자동문',floor,x,3,2.4,.12,2.2,
                pose=dict(x=x-.18,y=3,yaw=math.pi/2),facility=dict(door_motion='lateral'))
    element('storage-obstacle','obstacle','창고 보관함','floor-1',1.8,6.2,1.2,.8,1.2)
    element('work-obstacle','obstacle','작업실 보관함','floor-2',9.5,6.2,1.2,.8,1.2)
    robots=data['robots']
    robots[0]['name']='창고 상차 팔'
    robots[1]['name']='물품 운반 AMR'
    robots[2].update(name='작업실 조작 팔',floor_id='floor-2')
    robots[2]['pose']['x']=9.5
    final=json.loads(json.dumps(robots[2]));final.update(id='final-arm',name='최종 인계 팔')
    final['pose']['x']=final_bay_x;robots.append(final)
    robots.append(dict(id='spot-patrol',name='Spot 병행 순찰',model_id='spot',floor_id='floor-1',
        pose=dict(x=7,y=9),max_speed=.25,sensors=dict(position_noise=0,yaw_noise=0)))
    first=data['tasks'][0]
    first.update(name='창고 상차 → 승강기 → 작업대 배치',floor_id='floor-2',timeout=360,retries=0,
                 destination=dict(x=8.95,y=4.0,z=.20))
    first['cooperation'].update(source_floor_id='floor-1',workspace_id='workroom',carrier_destination=dict(x=9.848,y=3,z=.3,yaw=0))
    data['tasks'].append(dict(id='return-delivery',name='작업대 재인수 → 최종 인계',kind='retrieve',floor_id='floor-2',
        item_id='box',source=dict(x=8.95,y=4.0,z=.20),destination=dict(x=final_bay_x-.55,y=4.0,z=.20),
        predecessor_ids=['delivery'],timeout=180,retries=0,
        cooperation=dict(carrier_id='cart',donor_id='receiver',receiver_id='final-arm',source_floor_id='floor-2',
            workspace_id='handoff-zone',loading_offset=[-.248,.17],carrier_destination=dict(x=final_bay_x+.348,y=3,z=.3,yaw=0))))
    data['tasks'].append(dict(id='spot-patrol',name='Spot 복도 이동·도착 관측',kind='patrol',floor_id='floor-1',
        preferred_robot='spot-patrol',destination=dict(x=10,y=9),dwell=2,timeout=180,retries=0))
    data['people']=[dict(id=key,name=name,floor_id=floor,pose=dict(x=x,y=y),speed=.65,
        behavior=dict(mode='destinations',allowed_zone_ids=[f'{floor}-walking'],destinations=[dict(x=x,y=1.1),dict(x=x,y=3.0)],
                      speed_min_m_s=.5,speed_max_m_s=.8,stop_rate_per_s=.035,
                      stop_duration_min_s=1,stop_duration_max_s=2.5,crossing_rate_per_s=.02,seed=seed))
        for key,name,floor,x,y,seed in [('walker-1','창고 통로 보행자','floor-1',4.3,1.1,11),
                                      ('walker-2','승강장 교차 보행자','floor-2',6,1.2,23),
                                      ('walker-3','작업실 통로 보행자','floor-2',8,1.3,37)]]
    data['policy']['pedestrian_avoidance']=dict(desired_clearance_m=.5)
    data['items'][0]['name']='시험 물품 · 1kg 상자'
    return Project.model_validate(data)
