import math
from pathlib import Path

from .domain import Project, Environment, Floor, Element, Size, Pose, FacilitySettings, RobotInstance, Task, Person, Item


TEMPLATES = [
    {"id":"warehouse-cooperation","name":"물류 시설 · 협업 운반·보행자 교차","group":"복합 시나리오","description":"로봇 5대·이동 보행자 3명 · 상차 → 작업대 인계 → 재상차 → 출고, Spot 병행 순찰 · 완료 또는 360초에 정지"},
    {"id":"multifloor-cargo","name":"다층 물품 업무 · 상차·재인수·최종 인계","group":"복합 시나리오"},
    {"id":"elevator-pedestrian-60s","name":"엘리베이터·보행자 회피 · 60초","group":"기능 시험"},
    {"id":"hotel","name":"호텔","group":"환경 예제"},
    {"id":"apartment","name":"아파트","group":"환경 예제"},
    {"id":"warehouse","name":"물류 시설","group":"환경 예제"},
    {"id":"factory","name":"스마트 공장","group":"환경 예제"},
    {"id":"elevator-patrol","name":"엘리베이터 층간 순찰","group":"작업 예제"},
    {"id":"cooperative-handoff","name":"로봇 간 물품 인계","group":"작업 예제"},
    {"id":"cooperative-loading","name":"파지·상차·운반·인수","group":"작업 예제"},
    {"id":"cooperative-loading-3kg","name":"3kg 물품 협업 상차","group":"작업 예제"},
    {"id":"arm-pick-place","name":"로봇 팔 집기·놓기","group":"작업 예제"},
    {"id":"planning-cooperation-pedestrians","name":"승인 계획·물품 인계·통로 순찰","group":"작업 예제"},
    {"id":"charging-patrol","name":"AMR 충전 후 순찰 · 연구 예제","group":"작업 예제"},
]

FILE_EXAMPLES = {"elevator-pedestrian-60s", "elevator-patrol", "cooperative-handoff",
                 "cooperative-loading", "cooperative-loading-3kg", "arm-pick-place",
                 "planning-cooperation-pedestrians", "charging-patrol"}


def example(template_id="hotel") -> Project:
    if template_id == 'warehouse-cooperation':
        from .warehouse_scenario import warehouse_cooperation
        return warehouse_cooperation()
    if template_id == 'multifloor-cargo':
        from .multifloor_scenario import cargo_scenario
        return cargo_scenario()
    if template_id in FILE_EXAMPLES:
        return Project.model_validate_json((Path(__file__).resolve().parents[2]/"examples"/f"{template_id}.json").read_text(encoding="utf-8"))
    name = next((x["name"] for x in TEMPLATES if x["id"] == template_id), None)
    if name is None:
        raise ValueError("없는 예제 환경")
    floors = [Floor(id="floor-1",name="1층",width=24,depth=18), Floor(id="floor-2",name="2층",elevation=3.2,width=24,depth=18)]
    elements = []

    def element(kind, x, y, sx, sy, sz, label, **kwargs):
        el = Element(id=f"{kind}-{len(elements)}",kind=kind,name=label,floor_id="floor-1",pose=Pose(x=x,y=y),size=Size(x=sx,y=sy,z=sz),**kwargs)
        elements.append(el)
        return el

    for x,y,sx,sy in [(12,0,24,.15),(12,18,24,.15),(0,9,.15,18),(24,9,.15,18)]:
        element("wall",x,y,sx,sy,2.7,"외벽")
    if template_id in ("hotel","apartment"):
        for x in (5,9,13,17):
            element("room",x,14,3.7,5,2.7,f"{'객실' if template_id == 'hotel' else '세대'} {int(x)}")
            element("wall",x-1.9,14,.12,5,2.7,"공간 구획")
            element("door",x,11.5,1,.12,2.2,"자동문")
        element("corridor",10,10,18,2,0.02,"공용 복도")
    elif template_id == "warehouse":
        for x in (7,11,15,19):
            element("shelf",x,13,1.2,6,2.4,"적재 선반")
        element("loading",3,15,3,2,0.03,"상하차 구역")
    else:
        for x in (7,12,17):
            element("workbench",x,13,2,1.2,0.7,"공정 작업대")
        element("conveyor",12,16,9,0.8,0.65,"이송 컨베이어")
    element("charger",21,3,1.2,1.2,0.025,"충전소",facility=FacilitySettings(capacity=1))
    element("dock",21,5,1.2,1.2,0.025,"도킹 스테이션")
    # Authored east service aisle: the AGV's real charger staging point is
    # (19.488, 3). Approach it eastbound, along the charger axis: a lateral
    # 80mm waypoint arrival tolerance must not enter a 60mm docking corridor.
    # The downstream waiting point clears the largest robot's envelope.
    waiting = element("waiting",19.488,6.2,2,2,0.01,"충전 후 경로 대기")
    waiting.pose.yaw = math.pi/2
    element("stairs",21,13,2,5,3.2,"층간 계단",step_height=.16)
    element("elevator",21,8.8,2,2,3.2,"공용 승강기",facility=FacilitySettings(served_floors=[f.id for f in floors],capacity=2,max_load=350))
    element("ramp",16,8,3,1.5,.3,"시험 경사로",slope=.1)
    robots = []
    agv_route = [Pose(x=x,y=y,yaw=yaw) for x,y,yaw in
        [(18,3,0.),(19.488,3,0.),(19.488,6.2,math.pi/2),
         (18,6.2,math.pi),(18,3,0.)]]
    specs = [("spot",2,2),("spot",2,4),("delivery",5,2),("amr",5,4),("agv",18,3),("logistics",8,4),("arm",12,6),("mobile_manipulator",11,2)]
    for i,(model,x,y) in enumerate(specs):
        robots.append(RobotInstance(id=f"robot-{i+1}",name=f"{'Spot' if model == 'spot' else model.upper()} {i+1:02}",model_id=model,
            pose=Pose(x=x,y=y),agv_route=agv_route if model=="agv" else []))
    tasks = [Task(id=f"task-{i+1}",name=f"{r.name} 점검 이동",kind="patrol",preferred_robot=r.id,destination=Pose(x=r.pose.x+2,y=r.pose.y+1),priority=5+i) for i,r in enumerate(robots) if r.model_id not in ("arm","agv")]
    tasks.append(Task(id="agv-route",name="AGV 충전 복귀 순환 경로",kind="patrol",preferred_robot="robot-5",destination=Pose(x=18,y=6.2,yaw=math.pi)))
    return Project(id=f"example-{template_id}",name=f"{name} · 혼합 로봇 실험",environment=Environment(id=f"env-{template_id}",name=name,floors=floors,elements=elements),robots=robots,tasks=tasks,people=[Person(id="person-1",name="보행자 01",pose=Pose(x=3,y=8),path=[Pose(x=3,y=8),Pose(x=13,y=8)],speed=.6)],items=[Item(id="item-1",name="검증 물품",pose=Pose(x=12.5,y=6,z=.8))])
