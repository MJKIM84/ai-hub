"""Explicitly synthetic, parameterized open-workspace drafts; no run mutations."""
from uuid import uuid4
from pydantic import BaseModel, ConfigDict, Field, model_validator
from .domain import Project, Environment, Floor, Element, Pose, Size, FacilitySettings, RobotInstance


class SampleFloor(BaseModel):
    model_config=ConfigDict(extra='forbid')
    name:str=Field(min_length=1,max_length=80)
    spaces:list[str]=Field(min_length=1,max_length=6)


class SampleRequest(BaseModel):
    model_config=ConfigDict(extra='forbid')
    name:str=Field(default='대화용 시험 환경',min_length=1,max_length=100)
    floors:list[SampleFloor]=Field(min_length=1,max_length=3)
    width_m:float=Field(default=16,ge=12,le=40)
    depth_m:float=Field(default=12,ge=10,le=30)
    floor_height_m:float=Field(default=3.2,ge=3,le=6)
    elevator:bool=False

    @model_validator(mode='after')
    def names(self):
        if any(not name.strip() for floor in self.floors for name in floor.spaces):
            raise ValueError('공간 이름을 입력하세요')
        if any(len(set(floor.spaces))!=len(floor.spaces) for floor in self.floors):
            raise ValueError('같은 층의 공간 이름은 구분하세요')
        return self


def create_sample(spec:SampleRequest):
    key=uuid4().hex
    floors=[Floor(id=f'floor-{i+1}',name=f.name,elevation=i*spec.floor_height_m,width=spec.width_m,depth=spec.depth_m) for i,f in enumerate(spec.floors)]
    elements=[]
    for floor,definition in zip(floors,spec.floors):
        elements.append(Element(id=f'{floor.id}-hall',name=f'{floor.name} 공용 통로',kind='corridor',floor_id=floor.id,
            pose=Pose(x=spec.width_m/2,y=3),size=Size(x=spec.width_m-2,y=4,z=.01)))
        span=(spec.width_m-2)/len(definition.spaces)
        for i,name in enumerate(definition.spaces):
            elements.append(Element(id=f'{floor.id}-space-{i+1}',name=name,kind='room',floor_id=floor.id,
                pose=Pose(x=1+span*(i+.5),y=spec.depth_m-2),size=Size(x=span-.2,y=3,z=.01)))
    if spec.elevator and len(floors)>1:
        elements.append(Element(id='sample-lift',name='시험 승강기',kind='elevator',floor_id=floors[0].id,
            pose=Pose(x=spec.width_m/2,y=spec.depth_m/2),size=Size(x=2,y=2,z=spec.floor_height_m),
            facility=FacilitySettings(capacity=1,max_load=500,speed=.4,door_duration=2,served_floors=[f.id for f in floors])))
    return Project(id='scenario-sample-'+key,name='가상 샘플 · '+spec.name,
        environment=Environment(id='synthetic-'+key,name='가상 샘플 · 칸막이 없는 작업 구역',floors=floors,elements=elements),
        robots=[RobotInstance(id='sample-amr',name='샘플 AMR',model_id='amr',floor_id=floors[0].id,pose=Pose(x=2,y=2))],tasks=[])
