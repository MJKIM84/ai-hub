"""Persisted drafts and exactly-once approval into the existing Session engine."""
from __future__ import annotations
import copy
import hashlib
import json
import math
import re
import subprocess
import tempfile
from urllib.parse import unquote
import time
import uuid
from pathlib import Path
from fastapi import HTTPException, Request
from fastapi.responses import FileResponse
from starlette.concurrency import run_in_threadpool
from pydantic import BaseModel, Field, ConfigDict
from .assistant_provider import ProviderError
from .planning_provider import PlanningProvider
from .ontology import OntologyStore
from .scenario_samples import SampleRequest, create_sample
from .floorplans import FloorplanStore
from .floorplans import _image_words
from .catalog import models
from .domain import Project
from .runtime import Session


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def write_json(path, value):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(value, ensure_ascii=False, allow_nan=False))
    temp.replace(path)


def _pdf_document_text(path):
    """Extract source pages without confusing OCR guesses with PDF text.

    OCR is review material only. A failed page remains visible in the import
    coverage and cannot silently become a document-confirmed capability.
    """
    try:
        info=subprocess.run(['pdfinfo',str(path)],capture_output=True,check=True,timeout=20).stdout.decode('utf-8','replace')
        match=re.search(r'^Pages:\s*(\d+)\s*$',info,re.M)
        count=int(match.group(1)) if match else 0
        if not 1<=count<=80:
            raise ValueError('PDF는 1~80쪽을 지원합니다. 더 긴 문서는 검토할 범위로 분리하세요')
        extracted=subprocess.run(['pdftotext','-raw',str(path),'-'],capture_output=True,
                                 check=True,timeout=45).stdout.decode('utf-8','replace').split('\f')
    except (OSError,subprocess.CalledProcessError,subprocess.TimeoutExpired) as error:
        raise ValueError('PDF를 읽지 못했습니다. 파일 형식과 암호 설정을 확인하세요') from error
    pages=[];coverage=[];ocr_count=0
    for number in range(1,count+1):
        source=extracted[number-1].strip() if number<=len(extracted) else ''
        status='pdf_text' if len(source)>=80 else 'unreadable'
        text=source
        reason=None
        if len(source)<80:
            ocr_count+=1
            if ocr_count>20:
                raise ValueError('OCR이 필요한 페이지가 20쪽을 넘습니다. 검토 범위로 PDF를 나누어 등록하세요')
            with tempfile.TemporaryDirectory() as folder:
                prefix=str(Path(folder)/'page')
                try:
                    subprocess.run(['pdftoppm','-f',str(number),'-l',str(number),'-r','160',
                                    '-singlefile','-png',str(path),prefix],capture_output=True,
                                   check=True,timeout=45)
                    raster=Path(prefix+'.png')
                    dimensions=subprocess.run(['ffprobe','-v','error','-show_entries','stream=width,height',
                                               '-of','csv=p=0',str(raster)],capture_output=True,
                                              check=True,timeout=10).stdout.decode().strip().split(',')
                    width,height=(int(value) for value in dimensions[:2])
                    if width*height>25_000_000:raise ValueError('OCR 이미지가 너무 큽니다')
                    words,engine=_image_words(raster,width,height)
                except (OSError,subprocess.CalledProcessError,subprocess.TimeoutExpired,ValueError):
                    words=[];engine='로컬 OCR 실패'
            if words:
                # Preserve reading order as a reviewable text approximation;
                # tiled OCR may repeat a line with its first letter clipped.
                # Multi-column pages still need comparison with the PDF.
                unique=[]
                for row in sorted(words,key=lambda row:(row.get('ocr_region')!='full',-len(row['text']))):
                    box=row['bbox_px']
                    if any((min(box[2],old['bbox_px'][2])-max(box[0],old['bbox_px'][0])) /
                           max(1,min(box[2]-box[0],old['bbox_px'][2]-old['bbox_px'][0]))>.7 and
                           (min(box[3],old['bbox_px'][3])-max(box[1],old['bbox_px'][1])) /
                           max(1,min(box[3]-box[1],old['bbox_px'][3]-old['bbox_px'][1]))>.6
                           for old in unique):
                        continue
                    unique.append(row)
                unique.sort(key=lambda row:(round(row['bbox_px'][1]/18),row['bbox_px'][0]))
                draft='\n'.join(row['text'].strip() for row in unique if row['text'].strip())
                text=(source+'\n\nOCR draft (not source-verified):\n' if source else '')+draft
                status='local_ocr_review_required'
            elif source:
                status='short_pdf_text_review_required'
            else:
                status='unreadable'
                reason=('이 환경에 로컬 OCR 도구가 없습니다. 텍스트 계층이 있는 PDF나 원문 텍스트를 등록하세요'
                        if '도구 없음' in engine else '로컬 OCR에서 문자를 읽지 못했습니다. 원본 페이지나 더 선명한 파일을 확인하세요')
        if text:
            label='PDF text layer' if status=='pdf_text' else (
                'local OCR; source comparison required' if status=='local_ocr_review_required' else
                'short PDF text; source comparison required')
            pages.append(f'## PDF page {number} · {label}\n{text}')
        coverage.append(dict(page=number,status=status,characters=len(text),reason=reason,
                             extraction='macOS Vision' if status=='local_ocr_review_required' else
                             ('PDF text layer' if source else 'unreadable')))
    if not pages:
        raise ValueError(coverage[0].get('reason') or '텍스트를 추출하거나 OCR로 읽은 페이지가 없습니다. 원본 PDF를 확인하세요')
    return '\n\n'.join(pages),coverage


class DraftRequest(BaseModel):
    model_config = ConfigDict(extra='forbid')
    project: Project
    intent: dict
    selection: dict | None = None


class ReviseRequest(BaseModel):
    model_config = ConfigDict(extra='forbid')
    version: int
    project: Project
    selection: dict


class SourceCheckRequest(BaseModel):
    model_config = ConfigDict(extra='forbid')
    version: int
    project: Project


class ApproveRequest(BaseModel):
    model_config = ConfigDict(extra='forbid')
    version: int
    plan_hash: str
    source_project_hash: str
    project: Project
    request_id: str = Field(min_length=8, max_length=128, pattern=r'^[A-Za-z0-9_-]+$')


class ChatRequest(BaseModel):
    model_config = ConfigDict(extra='forbid')
    project: Project
    message: str = Field(min_length=1,max_length=12000)
    plan_id: str | None = None
    mode: str = Field(default='auto',pattern=r'^(auto|question|plan|design)$')
    version: int | None = None
    answers: dict[str,str] = Field(default_factory=dict, max_length=4)
    selection: dict | None = None


class PlanService:
    def __init__(self, host, folder, *, provider_factory=None):
        self.host, self.folder = host, folder
        folder.mkdir(parents=True,exist_ok=True)
        self.provider = (provider_factory or PlanningProvider)(folder)
        self.ontology = OntologyStore(folder / "ontology")
        self.floorplans = FloorplanStore(folder / "floorplans")
        self.active = None
        self.stopped_run_id = None
        self.last_checkpoint = 0.
        self.amendment_required = False

    def path(self, plan_id):
        if not re.fullmatch(r'[0-9a-f]{32}', plan_id):
            raise HTTPException(404,'계획을 찾을 수 없습니다.')
        return self.folder / f'{plan_id}.json'

    def load(self, plan_id):
        path = self.path(plan_id)
        if not path.exists():
            raise HTTPException(404,'계획을 찾을 수 없습니다.')
        return json.loads(path.read_text())

    def save(self, record):
        write_json(self.path(record['id']),record)
        history=self.folder/'history'/record['id']
        history.mkdir(parents=True,exist_ok=True)
        write_json(history/f"{record['version']}.json",record)

    def versions(self, plan_id):
        current=self.load(plan_id)
        history=self.folder/'history'/plan_id
        rows=[]
        for path in sorted((p for p in history.glob('*.json') if p.stem.isdigit()),
                           key=lambda p:int(p.stem),reverse=True) if history.exists() else []:
            rows.append(json.loads(path.read_text()))
        if not any(row.get('version')==current['version'] for row in rows):
            rows.insert(0,current)
        return rows

    def load_version(self, plan_id, version):
        self.path(plan_id)  # Validate the identifier before constructing a history path.
        if type(version) is not int or version<1:
            raise HTTPException(404,'계획 버전을 찾을 수 없습니다.')
        path=self.folder/'history'/plan_id/f'{version}.json'
        if path.exists():return json.loads(path.read_text())
        current=self.load(plan_id)
        if current['version']==version:return current
        raise HTTPException(404,'계획 버전을 찾을 수 없습니다.')

    def compile(self, project, intent, selection):
        from .intent_planning import compile_plan
        selection=copy.deepcopy(selection or {})
        resolution=selection.pop('occupancy_resolution',None)
        execution_intent = {k:v for k,v in intent.items() if k not in ("capability_requests", "scenario")} if isinstance(intent,dict) else intent
        if isinstance(intent,dict) and intent.get('scenario'):
            from .scenario_dialogue import blocking_questions
            execution_intent=copy.deepcopy(execution_intent)
            execution_intent['clarifications']=list(dict.fromkeys(execution_intent.get('clarifications',[])+blocking_questions(intent)))
        has_capability_requests=isinstance(intent,dict) and 'capability_requests' in intent
        capability_requests=copy.deepcopy(intent['capability_requests']) if has_capability_requests else None
        spatial=self.floorplans.context(project)
        planning_project=project.model_copy(deep=True)
        if spatial and spatial['status'] in ('confirmed','user_edited'):
            # Route validation and the eventual Session must use the same
            # reviewed connections, including after edits to a saved map.
            planning_project.environment.reviewed_topology=spatial['graph']
        def build(candidate_project,candidate_intent):
            compiled=compile_plan(candidate_project,candidate_intent,selection=selection,
                                  ontology_support=self.ontology.execution_index())
            validation_intent=copy.deepcopy(candidate_intent)
            if has_capability_requests and isinstance(validation_intent,dict):
                validation_intent['capability_requests']=capability_requests
            compiled=self.ontology.validate_plan(candidate_project,validation_intent,compiled)
            compiled=self._spatial_validate(candidate_project,compiled,candidate_intent)
            if isinstance(intent,dict) and 'scenario' in intent:
                compiled['execution_policy']={'stop_when_tasks_terminal':True,'basis':'승인된 전체 단계가 종료되면 시뮬레이션 자동 정지; 실패를 성공으로 처리하지 않음'}
            return compiled
        baseline=build(planning_project,execution_intent)
        if resolution is None:return baseline
        offered=[option for blocker in baseline.get('blockers',[])
                 for option in blocker.get('resolution_options',[])]
        if not isinstance(resolution,dict) or resolution not in offered:
            baseline.setdefault('blockers',[]).append(dict(code='occupancy_resolution_stale',
                message='선택한 점유 변경안이 현재 계획·지도와 다릅니다',suggestion='최신 계획에서 대기 위치·순서·목적지 변경안을 다시 선택하세요'))
            baseline['can_approve']=False;baseline['status']='blocked'
            return baseline
        effective=copy.deepcopy(execution_intent)
        kind=resolution['kind']
        def requested_task(task_id):
            return next((task for index,task in enumerate(effective.get('tasks',[]))
                         if (task.get('id') or task.get('existing_task_id') or f'intent-task-{index+1}')==task_id),None)
        if kind=='waiting_position':
            robot=next(r for r in planning_project.robots if r.id==resolution['robot_id'])
            robot.pose.x=resolution['x'];robot.pose.y=resolution['y']
        elif kind=='task_order':
            before=requested_task(resolution['blocked_task_id'])
            after=requested_task(resolution['waiting_task_id'])
            if before is None or after is None:
                baseline.setdefault('blockers',[]).append(dict(code='occupancy_resolution_stale',
                    message='작업 순서를 바꿀 대상이 현재 계획에 없습니다',suggestion='최신 계획을 다시 계산하세요'))
                baseline['can_approve']=False;baseline['status']='blocked';return baseline
            before_id=resolution['blocked_task_id'];after_id=resolution['waiting_task_id']
            after['predecessor_ids']=[key for key in after.get('predecessor_ids',[]) if key!=before_id]
            before['predecessor_ids']=sorted(set(before.get('predecessor_ids',[])+[after_id]))
        elif kind=='alternate_destination':
            task=requested_task(resolution['task_id'])
            if task is None:
                baseline.setdefault('blockers',[]).append(dict(code='occupancy_resolution_stale',
                    message='변경할 작업이 현재 계획에 없습니다',suggestion='최신 계획을 다시 계산하세요'))
                baseline['can_approve']=False;baseline['status']='blocked';return baseline
            task['destination_xy']={'x':resolution['x'],'y':resolution['y']}
            if resolution.get('points'):
                task['route_points']=copy.deepcopy(resolution['points'])
        elif kind=='reachable_zone':
            task=requested_task(resolution['task_id'])
            if task is None or task.get('existing_task_id') or task.get('kind') not in ('patrol','inspect'):
                baseline.setdefault('blockers',[]).append(dict(code='occupancy_resolution_stale',
                    message='원래 작업을 다른 공간으로 바꾸는 변경안은 현재 새 순찰·점검 요청에 적용할 수 없습니다',
                    suggestion='최신 계획에서 검토된 대체 구역을 다시 선택하세요'))
                baseline['can_approve']=False;baseline['status']='blocked';return baseline
            task['destination_id']=resolution['destination_id']
            task['destination_xy']={'x':resolution['x'],'y':resolution['y']}
            task.pop('route_points',None)
            # The original request remains in the stored intent. The heading
            # shown for the approvable revision must describe what this new
            # task actually does, not repeat the unreachable destination.
            effective['goal']='대체 작업 · '+resolution['label']
        elif kind=='route_detour':
            task=requested_task(resolution['task_id'])
            if task is None:
                baseline.setdefault('blockers',[]).append(dict(code='occupancy_resolution_stale',
                    message='변경할 작업이 현재 계획에 없습니다',suggestion='최신 계획을 다시 계산하세요'))
                baseline['can_approve']=False;baseline['status']='blocked';return baseline
            task['route_points']=copy.deepcopy(resolution['points'])
        # The change is part of the selected plan version, never a mutation of
        # the editor project or a running session before final approval.
        revised=build(planning_project,effective)
        revised['occupancy_resolution']=resolution
        return revised

    def _spatial_validate(self, project, compiled, requested_intent=None):
        from .navigation import Planner, radius
        spatial=self.floorplans.context(project)
        if spatial is None: return compiled
        compiled['spatial_ontology']=spatial
        if spatial['status'] not in ('confirmed','user_edited'):
            compiled.setdefault('blockers',[]).append(dict(code='floorplan_source_stale',message=spatial['reason']))
        elif compiled.get('kind')=='plan':
            requested_tasks={task.get('id') or f'intent-task-{index+1}':task
                             for index,task in enumerate((requested_intent or {}).get('tasks',[]))
                             if isinstance(task,dict)}
            robot_index={robot.id:robot for robot in project.robots}
            def containing_zone(x,y,floor_id):
                zones=[element for element in project.environment.elements
                       if element.kind in ('room','corridor') and element.floor_id==floor_id
                       and abs(element.pose.x-x)<=element.size.x/2
                       and abs(element.pose.y-y)<=element.size.y/2]
                return min(zones,key=lambda element:element.size.x*element.size.y) if zones else None
            def graph_bottleneck(source_id,destination_id):
                if not source_id or not destination_id:return None
                widths={source_id:float('inf')}
                frontier=[source_id]
                while frontier:
                    current=frontier.pop()
                    for edge in spatial['graph']['connections']:
                        if edge.get('via')=='stairs':continue
                        if current==edge['from_id']:neighbor=edge['to_id']
                        elif current==edge['to_id']:neighbor=edge['from_id']
                        else:continue
                        capacity=min(widths[current],edge.get('width_m',0))
                        if capacity>widths.get(neighbor,0):
                            widths[neighbor]=capacity;frontier.append(neighbor)
                return widths.get(destination_id)
            def reachable_zone_choice(task_id,request,robot):
                """Offer an honest smaller task, never pretend it reached the requested room."""
                if (not robot or request.get('kind') not in ('patrol','inspect')
                        or request.get('existing_task_id')):
                    return None
                source_zone=containing_zone(robot.pose.x,robot.pose.y,robot.floor_id)
                if not source_zone:return None
                if request.get('source_id') and request['source_id']!=source_zone.id:
                    return None
                destination=next((element for element in project.environment.elements
                                  if element.id==request.get('destination_id')),None)
                planner=Planner(project.environment)
                start=robot.pose.model_dump(mode='json')
                for dx,dy in ((.75,0),(0,.75),(-.75,0),(0,-.75),
                              (1.1,0),(0,1.1),(-1.1,0),(0,-1.1)):
                    x=round(source_zone.pose.x+dx,2);y=round(source_zone.pose.y+dy,2)
                    if (abs(x-source_zone.pose.x)>source_zone.size.x/2 or
                            abs(y-source_zone.pose.y)>source_zone.size.y/2 or
                            planner.blocked(x,y,robot.floor_id,robot)):
                        continue
                    point=dict(x=x,y=y,z=start['z'],yaw=0)
                    if planner.path(start,point,robot.floor_id,robot):
                        return dict(kind='reachable_zone',task_id=task_id,
                                    robot_id=robot.id,
                                    destination_id=source_zone.id,x=x,y=y,
                                    label=(f'원래 목적 공간 {destination.name if destination else "(미확인)"}은 방문하지 않고 '
                                           f'{source_zone.name}의 ({x:.2f}, {y:.2f}) m까지 수행'))
                return None
            for blocker in compiled.get('blockers',[]):
                if blocker.get('code')=='route_unavailable':
                    task=requested_tasks.get(blocker.get('task_id'),{})
                    robot=robot_index.get(blocker.get('robot_id'))
                    source_zone=containing_zone(robot.pose.x,robot.pose.y,robot.floor_id) if robot else None
                    source_id=task.get('source_id') or (source_zone.id if source_zone else None)
                    destination_id=task.get('destination_id')
                    if not destination_id and robot and isinstance(task.get('destination_xy'),dict):
                        point=task['destination_xy']
                        if isinstance(point.get('x'),(int,float)) and isinstance(point.get('y'),(int,float)):
                            destination_zone=containing_zone(point['x'],point['y'],robot.floor_id)
                            destination_id=destination_zone.id if destination_zone else None
                    bottleneck=graph_bottleneck(source_id,destination_id)
                    required=2*(radius(robot)+.1) if robot else None
                    if bottleneck is not None and required is not None and bottleneck<required:
                        blocker['message']=(f'검토된 공간 연결의 최대 병목 개구 {bottleneck:.2f} m가 '
                                            f'{robot.name}의 물리 경로 필요 폭 {required:.2f} m보다 좁습니다')
                        blocker['suggestion']='폭·능력이 맞는 로봇과 검토된 다른 출입 경로를 확인하세요. 출발 측 범위만 수행하는 변경안은 원래 목적 공간을 방문하지 않으며 새 승인이 필요합니다. 벽 삭제나 로봇 크기 축소로 통과 처리하지 않습니다.'
                        blocker.update(aperture_width_m=bottleneck,required_width_m=required)
                        choice=reachable_zone_choice(blocker.get('task_id'),task,robot)
                        if choice:blocker['resolution_options']=[choice]
                    else:
                        blocker['message']='공간 연결은 검토됐지만 이 로봇이 확정된 벽·문 주변과 크기·방향 제한을 모두 만족하는 물리 경로를 찾지 못했습니다'
                        blocker['suggestion']='원본 도면의 문 개구부·양쪽 벽과 로봇 통과 폭을 확인하거나 다른 로봇·목적지를 선택하세요. 공간 그래프의 문 연결만으로 통행 가능하다고 판단하지 않습니다'
                    for option in compiled.get('robot_options',[]):
                        for rejection in option.get('task_rejections',[]):
                            for related in rejection.get('blockers',[]):
                                if related.get('code')=='route_unavailable' and related.get('task_id')==blocker.get('task_id') and related.get('robot_id')==blocker.get('robot_id'):
                                    related.update({key:blocker[key] for key in ('message','suggestion')})
            zones=[e for e in project.environment.elements if e.kind in ('room','corridor')]
            robots={robot.id:robot for robot in project.robots}
            robot_last_floor={robot.id:robot.floor_id for robot in project.robots}
            steps_by_robot={robot.id:[] for robot in project.robots}
            steps_by_id={step['id']:step for step in compiled.get('steps',[])}
            for candidate in steps_by_id.values():
                for robot_id in candidate.get('robot_ids',[]):
                    if robot_id in steps_by_robot:
                        steps_by_robot[robot_id].append(candidate)
            def waits_for(candidate, prerequisite_id, seen=None):
                if seen is None: seen=set()
                for dependency_id in candidate.get('dependencies',[]):
                    if dependency_id==prerequisite_id:return True
                    if dependency_id not in seen and dependency_id in steps_by_id:
                        seen.add(dependency_id)
                        if waits_for(steps_by_id[dependency_id],prerequisite_id,seen):return True
                return False
            route_project=Project.model_validate(compiled['project']) if compiled.get('project') else None
            route_planner=Planner(route_project.environment) if route_project else None
            route_robots={robot.id:robot for robot in route_project.robots} if route_project else {}
            edges=spatial['graph']['connections']
            # Stair geometry remains visible in the ontology, but the current
            # robot execution system only implements elevator floor trips.
            traversable={e.id for e in zones}
            traversable.update(e.id for e in project.environment.elements if e.kind=='elevator')
            def reachable_from(start, minimum_width=0):
                adjacency={node:set() for node in traversable}
                for edge in edges:
                    # The surveyed connection must also admit this robot's
                    # inflated footprint. A narrow aperture cannot become a
                    # route merely because the two rooms are graph neighbors.
                    if edge.get('via')=='stairs':
                        continue
                    if (edge.get('condition') in ('reviewed_door','reviewed_opening')
                            and edge.get('width_m',0) < minimum_width):
                        continue
                    if edge['from_id'] in adjacency and edge['to_id'] in adjacency:
                        adjacency[edge['from_id']].add(edge['to_id'])
                        adjacency[edge['to_id']].add(edge['from_id'])
                reached={start} if start else set()
                frontier=list(reached)
                while frontier:
                    for neighbor in adjacency.get(frontier.pop(),()):
                        if neighbor not in reached:
                            reached.add(neighbor);frontier.append(neighbor)
                return reached
            def zone(point,floor_id):
                matching=[e for e in zones if e.floor_id==floor_id and
                          abs(e.pose.x-point['x'])<=e.size.x/2 and
                          abs(e.pose.y-point['y'])<=e.size.y/2]
                return min(matching,key=lambda e:e.size.x*e.size.y).id if matching else None
            for step in compiled.get('steps',[]):
                assigned=next((rid for rid in step.get('robot_ids',[]) if rid in robots),None)
                source_floor=robot_last_floor.get(assigned,step['floor_id'])
                start=zone(step['source'],source_floor)
                end=zone(step['destination'],step['floor_id'])
                requested_destination=requested_tasks.get(step['id'],{}).get('destination_id')
                if isinstance(requested_destination,str) and requested_destination in {element.id for element in zones} and end!=requested_destination:
                    named=next(element.name for element in zones if element.id==requested_destination)
                    actual=next((element.name for element in zones if element.id==end),'확정 공간 밖')
                    compiled.setdefault('blockers',[]).append(dict(
                        code='floorplan_destination_zone_mismatch',task_id=step['id'],
                        message=f'지정 좌표는 요청한 {named}이 아니라 {actual}에 속합니다',
                        suggestion='원본에서 공간 경계와 목적지를 확인한 뒤, 실제로 요청한 공간 안의 도착점을 새 계획으로 선택하세요'))
                    step['valid']=False
                # The existing physical planner inflates its circular robot
                # footprint by 0.1 m on each side.
                required_width=2*(radius(robots[assigned])+.1) if assigned else 0
                reachable=reachable_from(start,required_width)
                if not start or not end or end not in reachable:
                    stair_only=(source_floor!=step['floor_id']
                        and any(edge.get('via')=='stairs' for edge in edges)
                        and not any(e.kind=='elevator' for e in project.environment.elements))
                    narrow=bool(start and end and end in reachable_from(start))
                    boundary_widths=[edge['width_m'] for edge in edges
                                     if edge.get('condition') in ('reviewed_door','reviewed_opening')
                                     and edge.get('width_m',0)<required_width
                                     and ((edge['from_id'] in reachable)!=(edge['to_id'] in reachable))]
                    target_widths=[edge['width_m'] for edge in edges
                                   if edge.get('condition') in ('reviewed_door','reviewed_opening')
                                   and edge.get('width_m',0)<required_width and end in (edge['from_id'],edge['to_id'])
                                   and (edge['from_id'] in reachable or edge['to_id'] in reachable)]
                    widest_boundary=max(target_widths or boundary_widths,default=None)
                    narrower_robots=[robot.name for robot in project.robots
                                     if robot.id!=assigned and robot.floor_id==source_floor
                                     and widest_boundary is not None
                                     and 2*(radius(robot)+.1)<=widest_boundary]
                    requested=requested_tasks.get(step['id'],{})
                    choice=reachable_zone_choice(step['id'],requested,robots.get(assigned)) if narrow else None
                    if narrow:
                        width_note=(f'{"목적 공간에 직접 이어지는" if target_widths else "접근 가능 구역 경계의"} 검토 개구 중 가장 넓은 후보도 {widest_boundary:.2f} m입니다. '
                                    if widest_boundary is not None else '')
                        robot_note=(f'폭만 맞는 현재 배치 로봇: {", ".join(narrower_robots)}. 능력·장비·전체 경로는 다시 검사해야 합니다. '
                                    if narrower_robots else '현재 배치 로봇 중 통과 폭을 만족하는 대안은 확인되지 않았습니다. ')
                        suggestion=(width_note+robot_note+
                                    '출발 측의 검토된 접근 공간으로 목적지를 바꾸거나 원본에서 다른 출입 경로를 확인하세요. '
                                    '축소 변경안은 원래 목적 공간 방문을 수행하지 않으므로 별도 승인이 필요합니다. '
                                    '실측 축척·개구가 없으면 실제 건물의 통과 가능성을 단정할 수 없습니다.')
                    else:
                        suggestion='도면의 방·복도·문·승강기 착지점과 통과 폭을 검토하세요'
                    compiled.setdefault('blockers',[]).append(dict(
                        code='floorplan_stairs_execution_unsupported' if stair_only else 'floorplan_aperture_too_narrow' if narrow else 'floorplan_disconnected',
                        task_id=step['id'],
                        message=('도면의 계단 연결은 확인됐지만 현재 로봇 실행기는 계단 층간 이동을 지원하지 않습니다. 로봇 위치를 다른 층으로 바꾸지 않습니다'
                                 if stair_only else f'확정한 문·개방 통로가 로봇의 필요 통과 폭 {required_width:.2f} m보다 좁습니다'
                                 if narrow else '확정한 공간 그래프에서 출발지와 목적지를 문 또는 실행 가능한 승강기로 연결할 수 없습니다'),
                        suggestion=('각 층에 배치된 로봇으로 층별 작업을 계획하거나, 지원되는 승강기와 실행 기능을 확인하세요'
                                    if stair_only else suggestion),
                        resolution_options=[choice] if choice else []))
                    step['valid']=False
                elif assigned:
                    # An idle robot at the target cannot yield, and a robot
                    # whose every task depends on this step cannot leave until
                    # the target is reached. Reject that circular wait before
                    # the user approves a run; route planning ignores peers.
                    target=step['destination']
                    for other in project.robots:
                        if other.id==assigned or other.floor_id!=step['floor_id']:
                            continue
                        other_steps=steps_by_robot[other.id]
                        if other_steps and not all(waits_for(item,step['id']) for item in other_steps):
                            continue
                        clearance=radius(robots[assigned])+radius(other)+project.policy.safety_distance
                        arrival_tolerance=.22
                        separation=math.hypot(other.pose.x-target['x'],other.pose.y-target['y'])
                        if separation < clearance-arrival_tolerance:
                            options=[]
                            moving=route_robots.get(assigned)
                            waiting=route_robots.get(other.id)
                            # Offer only locations verified against the same
                            # wall geometry and peer clearance as the plan.
                            if moving and waiting and route_planner and zone(other.pose.model_dump(),other.floor_id)==end:
                                for distance in (clearance+.35,clearance+.65,clearance+.95):
                                    for angle in (0,math.pi/2,math.pi,3*math.pi/2,math.pi/4,3*math.pi/4,5*math.pi/4,7*math.pi/4):
                                        x=round(target['x']+distance*math.cos(angle),2)
                                        y=round(target['y']+distance*math.sin(angle),2)
                                        if zone(dict(x=x,y=y),other.floor_id)!=end or route_planner.blocked(x,y,other.floor_id,waiting):
                                            continue
                                        if any(peer.id!=other.id and peer.floor_id==other.floor_id and
                                               math.hypot(peer.pose.x-x,peer.pose.y-y)<radius(peer)+radius(other)+project.policy.safety_distance
                                               for peer in project.robots):
                                            continue
                                        if route_planner.path(step['source'],target,step['floor_id'],moving,
                                                              peer_disks=[(x,y,clearance)]):
                                            options.append(dict(kind='waiting_position',robot_id=other.id,x=x,y=y,
                                                label=f'{other.name} 대기 위치를 같은 공간의 ({x:.2f}, {y:.2f}) m로 변경'))
                                            break
                                    if options:break
                                for distance in (clearance+.35,clearance+.65,clearance+.95):
                                    for angle in (0,math.pi/2,math.pi,3*math.pi/2,math.pi/4,3*math.pi/4,5*math.pi/4,7*math.pi/4):
                                        x=round(target['x']+distance*math.cos(angle),2)
                                        y=round(target['y']+distance*math.sin(angle),2)
                                        alternative=dict(target,x=x,y=y)
                                        if zone(alternative,step['floor_id'])!=end:
                                            continue
                                        alternate_route=route_planner.path(step['source'],alternative,step['floor_id'],moving,
                                                                           peer_disks=[(other.pose.x,other.pose.y,clearance)])
                                        if alternate_route and len(alternate_route)<=100:
                                            options.append(dict(kind='alternate_destination',task_id=step['id'],x=x,y=y,
                                                points=[{'x':point['x'],'y':point['y']} for point in alternate_route],
                                                label=f'같은 목적 공간의 ({x:.2f}, {y:.2f}) m로 도착 지점·경로 변경'))
                                            break
                                    if any(option['kind']=='alternate_destination' for option in options):break
                            if (len(other_steps)==1 and other_steps[0].get('valid') and
                                    other_steps[0].get('dependencies')==[step['id']] and
                                    math.hypot(robots[assigned].pose.x-other_steps[0]['destination']['x'],
                                               robots[assigned].pose.y-other_steps[0]['destination']['y'])>=clearance-arrival_tolerance):
                                options.append(dict(kind='task_order',blocked_task_id=step['id'],
                                    waiting_task_id=other_steps[0]['id'],
                                    label=f'{other.name}의 후속 작업을 먼저 실행해 목적지를 비움'))
                            compiled.setdefault('blockers',[]).append(dict(
                                code='destination_occupied_by_waiting_robot',task_id=step['id'],
                                robot_id=other.id,
                                message=f'{other.name}의 초기 위치가 목적지를 점유합니다. 선행 작업 완료 전에는 이 로봇이 비킬 수 없어 도착이 불가능합니다',
                                suggestion='목적지 자체를 점유하므로 경유 경로만 바꿔서는 도착할 수 없습니다. 대기 위치·작업 순서·같은 공간의 다른 도착점과 경로를 검토하세요. 변경안은 새 계획으로 계산한 뒤 다시 승인해야 합니다',
                                resolution_options=options))
                            step['valid']=False
                    route_robot=route_robots.get(assigned)
                    if source_floor==step['floor_id'] and route_robot and route_planner:
                        route=step.get('waypoints')
                        checked=isinstance(route,list) and route_planner.path_clear(
                            step['source'],route,step['floor_id'],route_robot)
                        if not checked:
                            compiled.setdefault('blockers',[]).append(dict(
                                code='floorplan_route_unreviewed',task_id=step['id'],
                                message='예상 경로가 확정 공간·문·개방 통로 안에 머무르지 않습니다',
                                suggestion='원본 도면에서 경유 공간과 출입구를 검토하거나 목적지를 바꾸세요'))
                            step['valid']=False
                        else:
                            apertures={e.id:e for e in project.environment.elements if e.kind in ('door','opening')}
                            def near(aperture, point):
                                dx,dy=point['x']-aperture.pose.x,point['y']-aperture.pose.y
                                c,s=math.cos(aperture.pose.yaw),math.sin(aperture.pose.yaw)
                                return (abs(c*dx+s*dy)<=aperture.size.x/2+.15 and
                                        abs(-s*dx+c*dy)<=aperture.size.y/2+.15)
                            def crosses(aperture):
                                points=[step['source'],*route]
                                for a,b in zip(points,points[1:]):
                                    samples=max(1,math.ceil(math.hypot(b['x']-a['x'],b['y']-a['y'])/.05))
                                    if any(near(aperture,dict(x=a['x']+(b['x']-a['x'])*i/samples,
                                                              y=a['y']+(b['y']-a['y'])*i/samples))
                                           for i in range(samples+1)):
                                        return True
                                return False
                            used=[dict(id=edge['via'],name=apertures[edge['via']].name,
                                       kind=edge['condition'],width_m=edge['width_m'])
                                  for edge in edges if edge.get('via') in apertures and
                                  crosses(apertures[edge['via']])]
                            step['spatial_review']=dict(status='validated',source_zone_id=start,
                                                        destination_zone_id=end,
                                                        required_width_m=round(required_width,3),
                                                        reviewed_apertures=used)
                            # An idle peer may block the interior of the
                            # reviewed route even when the destination is
                            # clear. Offer only a continuously checked route
                            # outside that peer's full safety envelope;
                            # approval recompiles the task with those points.
                            for other in (project.robots if step.get('valid') and
                                          step.get('kind') in ('patrol','inspect') else []):
                                if other.id==assigned or other.floor_id!=step['floor_id']:
                                    continue
                                other_steps=steps_by_robot[other.id]
                                if other_steps and not all(waits_for(item,step['id']) for item in other_steps):
                                    continue
                                clearance=radius(robots[assigned])+radius(other)+project.policy.safety_distance
                                if math.hypot(other.pose.x-step['destination']['x'],other.pose.y-step['destination']['y'])<clearance:
                                    continue  # The destination blocker above owns this case.
                                disk=[(other.pose.x,other.pose.y,clearance)]
                                if route_planner.path_clear(step['source'],route,step['floor_id'],route_robot,peer_disks=disk):
                                    continue
                                alternative=route_planner.path(step['source'],step['destination'],step['floor_id'],route_robot,peer_disks=disk)
                                options=[]
                                if alternative and len(alternative)<=100 and route_planner.path_clear(
                                        step['source'],alternative,step['floor_id'],route_robot,peer_disks=disk):
                                    options.append(dict(kind='route_detour',task_id=step['id'],
                                        points=[{'x':point['x'],'y':point['y']} for point in alternative],
                                        label=f'{other.name}을 피해 검토된 {len(alternative)}개 경유점으로 우회'))
                                waiting=route_robots.get(other.id)
                                other_zone=zone(other.pose.model_dump(),other.floor_id)
                                if waiting and other_zone:
                                    for distance in (clearance+.35,clearance+.7,clearance+1.05):
                                        for angle in (0,math.pi/2,math.pi,3*math.pi/2,math.pi/4,3*math.pi/4,5*math.pi/4,7*math.pi/4):
                                            x=round(other.pose.x+distance*math.cos(angle),2)
                                            y=round(other.pose.y+distance*math.sin(angle),2)
                                            candidate=dict(x=x,y=y)
                                            if (zone(candidate,other.floor_id)!=other_zone
                                                    or route_planner.blocked(x,y,other.floor_id,waiting)
                                                    or any(peer.id!=other.id and peer.floor_id==other.floor_id and
                                                           math.hypot(peer.pose.x-x,peer.pose.y-y)<radius(peer)+radius(other)+project.policy.safety_distance
                                                           for peer in project.robots)):
                                                continue
                                            if route_planner.path_clear(step['source'],route,step['floor_id'],route_robot,
                                                                        peer_disks=[(x,y,clearance)]):
                                                options.append(dict(kind='waiting_position',robot_id=other.id,x=x,y=y,
                                                    label=f'{other.name}의 초기 대기 위치를 같은 공간의 ({x:.2f}, {y:.2f}) m로 변경'))
                                                break
                                        if any(option['kind']=='waiting_position' for option in options):break
                                if (len(other_steps)==1 and other_steps[0].get('valid') and
                                        step['id'] in other_steps[0].get('dependencies',[])):
                                    future=other_steps[0]['destination']
                                    if route_planner.path_clear(step['source'],route,step['floor_id'],route_robot,
                                        peer_disks=[(future['x'],future['y'],clearance)]):
                                        options.append(dict(kind='task_order',blocked_task_id=step['id'],
                                            waiting_task_id=other_steps[0]['id'],
                                            label=f'{other.name}의 후속 작업을 먼저 실행해 경로를 비움'))
                                if not options:
                                    for distance in (clearance+.4,clearance+.8,clearance+1.2):
                                        for angle in (0,math.pi/2,math.pi,3*math.pi/2,math.pi/4,3*math.pi/4,5*math.pi/4,7*math.pi/4):
                                            x=round(step['destination']['x']+distance*math.cos(angle),2)
                                            y=round(step['destination']['y']+distance*math.sin(angle),2)
                                            target=dict(step['destination'],x=x,y=y)
                                            if zone(target,step['floor_id'])!=end:continue
                                            candidate_route=route_planner.path(step['source'],target,step['floor_id'],route_robot,
                                                                               peer_disks=disk)
                                            if candidate_route and len(candidate_route)<=100:
                                                options.append(dict(kind='alternate_destination',task_id=step['id'],x=x,y=y,
                                                    points=[{'x':point['x'],'y':point['y']} for point in candidate_route],
                                                    label=f'같은 목적 공간의 ({x:.2f}, {y:.2f}) m로 도착점·경로 변경'))
                                                break
                                        if options:break
                                compiled.setdefault('blockers',[]).append(dict(
                                    code='route_occupied_by_waiting_robot',task_id=step['id'],robot_id=other.id,
                                    message=f'{other.name}이 승인 전 경로 중간을 점유합니다',
                                    suggestion=('검토된 우회 경로를 선택해 새 계획을 계산하고 승인하세요' if options else
                                                '검토된 우회·대기 위치·작업 순서·도착점 변경을 확인하지 못했습니다. 지도와 초기 배치를 다시 검토하세요'),
                                    resolution_options=options))
                                step['valid']=False
                                break
                    robot_last_floor[assigned]=step['floor_id']
        if compiled.get('blockers'):
            compiled['can_approve']=False
            compiled['status']='analysis' if compiled.get('kind')=='question' else 'blocked'
        return compiled

    def public(self, record):
        source=record.get('source_project',{}).get('environment',{})
        return {**{k:v for k,v in record.items() if k not in {'source_project','runtime_binding'}},
                'source_project_revision':record.get('source_project',{}).get('revision'),
                'source_environment_id':source.get('id'),
                'source_environment_name':source.get('name'),
                'source_environment_version':source.get('version')}

    def draft(self, project, intent, selection=None, *, previous=None, conversation=None, origin='manual_structured', model_execution=None, conversation_key=None):
        compiled = self.compile(project,intent,selection)
        with self.host.lock:
            if previous:
                current=self.load(previous['id'])
                if any(current.get(k)!=previous.get(k) for k in ('version','plan_hash','approval')):
                    raise HTTPException(409,'응답을 기다리는 동안 계획이 갱신·승인되었습니다. 최신 계획을 다시 불러오세요.')
            if previous and previous.get('approval') and self.active == previous['id']:
                if self.host.session.status not in ('completed','failed','timed_out'):
                    self.host.session.status = 'paused'
                    self.amendment_required = True
                    self.host.session.emit('plan_amendment_required',None,'계획 변경안을 검토 중입니다. 새 버전 승인 전까지 일시 정지합니다.',{})
                self.checkpoint(force=True)
            source = project.model_dump(mode='json')
            record = {'id':previous['id'] if previous else uuid.uuid4().hex,
                      'version':previous['version'] + 1 if previous else 1,
                      'created_at':time.time(), 'origin':origin, 'intent':intent,
                      'conversation_key':conversation_key or (previous or {}).get('conversation_key',project.id),
                      'model_execution':copy.deepcopy(model_execution or (previous or {}).get('model_execution')),
                      'input_receipt':copy.deepcopy((previous or {}).get('input_receipt')),
                      'model_proposal':copy.deepcopy((previous or {}).get('model_proposal')),
                      'conversation':conversation if conversation is not None else (previous or {}).get('conversation',[]),
                      'source_project':source, 'source_project_hash':digest(source),
                      'runtime_binding':{'run_id':self.host.session.run_id,'project_hash':digest(self.host.session.project.model_dump(mode='json'))},
                      'compiled':compiled, 'selection':selection or {},
                      'approval':None, 'previous_approvals':(previous or {}).get('previous_approvals',[]) + ([(previous['approval'])] if previous and previous.get('approval') else [])}
            record['plan_hash'] = digest({'intent':intent,'source':source,'selection':selection or {},'compiled':compiled})
            # Archive prior revision so the exact approved configuration remains retrievable.
            if previous:
                archive=self.folder/'revisions';archive.mkdir(exist_ok=True)
                write_json(archive/f"{previous['id']}-{previous['version']}.json",previous)
            self.save(record)
            return self.public(record)

    def approve(self, plan_id, request):
        with self.host.lock:
            journal = self.folder / ('approval-' + request.request_id + '.json')
            signature = digest({'id':plan_id, 'version':request.version,'hash':request.plan_hash,'source':request.source_project_hash,'project':request.project.model_dump(mode='json')})
            if journal.exists():
                prior = json.loads(journal.read_text())
                if prior['signature'] != signature:
                    raise HTTPException(409,'동일한 요청 번호에 서로 다른 계획을 사용할 수 없습니다.')
                return dict(prior['receipt'], replayed=True, live=self.host.session.run_id == prior['receipt']['run_id'])
            record = self.load(plan_id)
            if record['version'] != request.version or record['plan_hash'] != request.plan_hash:
                raise HTTPException(409,'계획이 변경되었습니다. 최신 버전을 확인하고 승인하세요.')
            if request.source_project_hash != record['source_project_hash'] or digest(request.project.model_dump(mode='json')) != record['source_project_hash']:
                raise HTTPException(409,'편집 환경이 초안 이후 변경되었습니다. 계획을 다시 계산하세요.')
            if record.get('approval'):
                # A different request ID still cannot launch the same plan twice.
                write_json(journal,{'signature':signature,'receipt':record['approval']})
                return dict(record['approval'],replayed=True,live=self.host.session.run_id == record['approval']['run_id'])
            source = record['runtime_binding']
            if source != {'run_id':self.host.session.run_id,'project_hash':digest(self.host.session.project.model_dump(mode='json'))}:
                raise HTTPException(409,'연결된 실행 환경이 변경되었습니다. 계획을 다시 계산하세요.')
            if self.host.session.status not in ('paused','completed','failed','timed_out'):
                raise HTTPException(409,'현재 실행을 일시 정지한 뒤 승인하세요.')
            compiled = self.compile(request.project, record['intent'],record['selection'])
            if not compiled.get('can_approve') or compiled.get('kind') == 'question' or not compiled.get('project'):
                raise HTTPException(422,{'message':'실행 조건을 충족하지 못했습니다.','blockers':compiled.get('blockers',[]),'clarifications':compiled.get('clarifications',[])})
            if digest(compiled) != digest(record['compiled']):
                raise HTTPException(409,'실행 검증 결과가 달라졌습니다. 계획을 갱신하세요.')
            candidate = Session(Project.model_validate(compiled['project']),
                                stop_when_tasks_terminal=compiled.get('execution_policy',{}).get('stop_when_tasks_terminal',False))
            receipt = {'plan_id':plan_id,'version':record['version'],'plan_hash':record['plan_hash'],
                       'run_id':candidate.run_id,'approved_at':time.time(),'status':'accepted',
                       'initialization':'editor_initial_conditions', 'request_id':request.request_id}
            # Persist intent before the sole runtime mutation. On restart journal is historical, never replayed.
            write_json(journal,{'signature':signature,'receipt':receipt})
            record['approval']=receipt
            self.save(record)
            if self.active:
                self.checkpoint(force=True)
                recordings=self.folder/'recordings';recordings.mkdir(exist_ok=True)
                write_json(recordings/(self.host.session.run_id+'.json'),self.host.session.recording())
            self.host.session=candidate
            self.active=plan_id
            self.amendment_required=False
            candidate.emit('plan_approved',None,'승인한 계획으로 새 실험을 시작했습니다. 작업 완료는 실행 결과에서 확인하세요.',receipt)
            candidate.status='running'
            self.checkpoint(force=True)
            return dict(receipt,replayed=False,live=True)

    def guard(self, action):
        if self.active:
            self.host.session.status='paused'
            self.amendment_required=True
            self.host.session.emit('plan_amendment_required',None,'승인 범위를 바꾸는 조작입니다. 계획 도우미에서 변경안을 승인하세요.',{'action':action})
            self.checkpoint(force=True)
            raise HTTPException(409,'승인한 실행을 일시 정지했습니다. 계획 도우미에서 변경안을 계산하고 다시 승인하세요.')

    def checkpoint(self, force=False):
        if not self.active:
            return
        if not force and time.monotonic()-self.last_checkpoint < 5:
            return
        self.last_checkpoint=time.monotonic()
        s=self.host.session
        # Runtime snapshot contains measured task states, metrics and bounded event history.
        result={'plan_id':self.active,'run_id':s.run_id,'snapshot':s.snapshot(), 'saved_at':time.time()}
        write_json(self.folder/('result-'+self.active+'.json'),result)
        runs=self.folder/'runs';runs.mkdir(exist_ok=True)
        write_json(runs/(s.run_id+'.json'),result)
        record=self.load(self.active)
        if record.get('approval'):
            self.ontology.record_execution(record['compiled'],result['snapshot'],record['approval'])

    def result(self, plan_id):
        with self.host.lock:
            record=self.load(plan_id)
            if self.active==plan_id:
                self.checkpoint(force=True)
            path=self.folder/('result-'+plan_id+'.json')
            return {'approval':record.get('approval'),'result':json.loads(path.read_text()) if path.exists() else None,
                    'live':self.active==plan_id,'hardware_validation':False}

    def result_for_run(self, plan_id, run_id):
        if not re.fullmatch(r'[0-9a-f]{32}',run_id):
            raise HTTPException(404,'승인된 실행을 찾을 수 없습니다.')
        with self.host.lock:
            record=self.load(plan_id)
            approvals=[record.get('approval'),*record.get('previous_approvals',[])]
            approval=next((item for item in approvals if item and item.get('run_id')==run_id),None)
            if approval is None:
                raise HTTPException(404,'이 계획에서 승인한 실행을 찾을 수 없습니다.')
            live=self.active==plan_id and self.host.session.run_id==run_id
            if live:self.checkpoint(force=True)
            path=self.folder/'runs'/(run_id+'.json')
            return {'approval':approval,'result':json.loads(path.read_text()) if path.exists() else None,
                    'live':live,'current_plan_version':record['version'],'hardware_validation':False}


def install_plan_routes(app,host,folder, *, provider_factory=None):
    service=PlanService(host,folder, provider_factory=provider_factory)
    host.plan_service=service

    @app.get('/api/assistant/settings')
    def settings():return dict(service.provider.settings(),scenario_dialogue_version=1)

    @app.put('/api/assistant/settings')
    def configure(body:dict):return service.provider.configure(body)

    @app.post('/api/assistant/disconnect')
    def disconnect_assistant():return service.provider.disconnect()

    @app.post('/api/assistant/models/refresh')
    def refresh_assistant_models():return service.provider.refresh_models()

    @app.post('/api/assistant/login')
    def login():return service.provider.login()

    @app.post('/api/assistant/login/cancel')
    def cancel_login(body:dict):
        login_id=body.get('login_id')
        if not isinstance(login_id,str) or not login_id:raise HTTPException(422,'로그인 요청 번호가 필요합니다.')
        return service.provider.cancel_login(login_id)

    @app.post('/api/assistant/cancel')
    def cancel_model():return service.provider.cancel()

    @app.get('/api/ontology')
    def ontology():return service.ontology.snapshot()

    @app.post('/api/ontology/models')
    def onboard_documentation_model(body:dict):return service.ontology.onboard_model(body)

    @app.post('/api/ontology/documents')
    def register_document(body:dict):return service.ontology.register(body)

    @app.post('/api/ontology/documents/{document_id}/analyze')
    def analyze_document(document_id:str):return service.ontology.analyze(document_id)

    @app.post('/api/ontology/documents/{document_id}/extract/model')
    def model_extract_document(document_id:str):
        path=service.ontology._path(document_id)
        if not path.exists():raise HTTPException(404,'등록 문서를 찾을 수 없습니다')
        document=service.ontology._load_document(path)
        if document.get('integrity',{}).get('status')=='rejected':
            raise HTTPException(422,'원문 무결성을 확인할 수 없습니다')
        previous=document.get('model_drafts',{})
        cursor=previous.get('processed_characters',0) if previous.get('source_sha256')==document['sha256'] else 0
        if type(cursor) is not int:cursor=0
        if cursor>=len(document['text']):
            raise HTTPException(409,'이 문서는 모델에 전체 범위를 전달했습니다. 남은 검토 초안을 확인하세요.')
        response=service.provider.extract_manual(document,processed_characters=cursor)
        return service.ontology.save_model_drafts(document_id,response)

    @app.post('/api/ontology/documents/file')
    async def register_document_file(request:Request):
        model_id=request.headers.get('x-model-id','')
        version=request.headers.get('x-document-version','')
        title=Path(unquote(request.headers.get('x-filename','robot-manual.pdf'))).name[:300]
        source_url=request.headers.get('x-source-url','')
        content=await request.body()
        if not content.startswith(b'%PDF-') or len(content)>20_000_000:
            raise HTTPException(422,'20MB 이하의 PDF 문서를 선택하세요')
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'manual.pdf';path.write_bytes(content)
            try:
                text,coverage=await run_in_threadpool(_pdf_document_text,path)
            except ValueError as error:
                raise HTTPException(422,str(error)) from None
        document=service.ontology.register(dict(title=title,model_id=model_id,version=version,
                                                source_url=source_url,text=text))
        try:
            return service.ontology.attach_pdf_source(document['id'],content,coverage)
        except ValueError as error:
            raise HTTPException(409,str(error)) from None

    @app.get('/api/ontology/documents/{document_id}/source')
    def ontology_source(document_id:str):
        service.ontology._path(document_id)
        source=service.ontology.folder/(document_id+'.pdf')
        if not source.exists():raise HTTPException(404,'원본 PDF가 없습니다')
        return FileResponse(source,media_type='application/pdf',filename='robot-manual.pdf')

    @app.put('/api/ontology/documents/{document_id}/capabilities/{capability_id}/review')
    def review_capability(document_id:str,capability_id:str,body:dict):
        return service.ontology.review_capability(document_id,capability_id,body)

    @app.put('/api/ontology/documents/{document_id}/facts')
    def review_document_fact(document_id:str,body:dict):
        return service.ontology.review_fact(document_id,body)

    @app.put('/api/ontology/documents/{document_id}/capabilities/{capability_id}/simulation-binding')
    def bind_simulation_capability(document_id:str,capability_id:str,body:dict):
        return service.ontology.bind_simulation(document_id,capability_id,body)

    @app.get('/api/floorplans')
    def floorplans():return service.floorplans.list()

    @app.get('/api/floorplans/{plan_id}/versions')
    def floorplan_versions(plan_id:str):return service.floorplans.versions(plan_id)

    @app.post('/api/floorplans/{plan_id}/versions/{revision}/resume')
    def resume_floorplan(plan_id:str,revision:int):return service.floorplans.resume(plan_id,revision)

    @app.post('/api/floorplans')
    async def register_floorplan(request:Request):
        if int(request.headers.get('content-length','0') or 0)>20_000_000:
            raise HTTPException(413,'도면은 20MB 이하여야 합니다')
        content=await request.body()
        return service.floorplans.register(request.headers.get('x-filename','도면'),content)

    @app.get('/api/floorplans/{plan_id}')
    def get_floorplan(plan_id:str):return service.floorplans.get(plan_id)

    @app.get('/api/floorplans/{plan_id}/pages/{number}/image')
    def floorplan_image(plan_id:str,number:int):return FileResponse(service.floorplans.image(plan_id,number))

    @app.post('/api/floorplans/{plan_id}/pages/{number}/ocr/retry')
    def retry_floorplan_ocr(plan_id:str,number:int,body:dict):
        if set(body)!={'revision'} or type(body['revision']) is not int:
            raise HTTPException(422,'도면 검토 버전이 필요합니다')
        return service.floorplans.retry_ocr(plan_id,body['revision'],number)

    @app.post('/api/floorplans/{plan_id}/pages/{number}/geometry/retry')
    def retry_floorplan_geometry(plan_id:str,number:int,body:dict):
        if set(body)!={'revision'} or type(body['revision']) is not int:
            raise HTTPException(422,'도면 검토 버전이 필요합니다')
        return service.floorplans.retry_geometry(plan_id,body['revision'],number)

    @app.post('/api/floorplans/{plan_id}/pages/{number}/inspect')
    def inspect_floorplan_image(plan_id:str,number:int,body:dict):
        if set(body)!={'revision'} or type(body['revision']) is not int:
            raise HTTPException(422,'도면 검토 버전이 필요합니다')
        plan=service.floorplans.get(plan_id)
        if plan['revision']!=body['revision']:
            raise HTTPException(409,'도면이 변경됐습니다. 최신 검토 버전을 다시 불러오세요')
        image=service.floorplans.image(plan_id,number)
        page=plan['pages'][number-1]
        response=service.provider.inspect_floorplan(image,page['width_px'],page['height_px'])
        return service.floorplans.save_visual_drafts(plan_id,body['revision'],number,response)

    @app.put('/api/floorplans/{plan_id}/review')
    def review_floorplan(plan_id:str,body:dict):return service.floorplans.review(plan_id,body)

    @app.post('/api/floorplans/{plan_id}/split')
    def split_floorplan(plan_id:str,body:dict):return service.floorplans.split_page_into_floors(plan_id,body)

    @app.post('/api/floorplans/{plan_id}/generate')
    def generate_floorplan(plan_id:str,body:dict):
        if set(body)!={'revision','project'}:raise HTTPException(422,'도면 버전과 프로젝트가 필요합니다')
        project=Project.model_validate(body['project'])
        return service.floorplans.generate(plan_id,body['revision'],project)

    @app.post('/api/assistant/chat')
    def chat(body:ChatRequest):
        previous=service.load(body.plan_id) if body.plan_id else None
        # A conversation about a different confirmed map must not silently
        # supply old room names, routes, or approvals to the new request.
        environment_hash=digest(body.project.environment.model_dump(mode='json'))
        conversation_key=body.project.id+':'+environment_hash
        previous_environment=(previous or {}).get('source_project',{}).get('environment')
        if body.mode!='design' and previous and (not isinstance(previous_environment,dict)
                         or digest(previous_environment)!=environment_hash):
            previous=None
        if body.mode=='design' and previous and body.version!=previous['version']:
            raise HTTPException(409,'초안 버전이 변경되었습니다. 최신 대화를 다시 열어주세요.')
        from .scenario_dialogue import answered_state, merge_dialogue, merge_selection
        try:
            scenario_state=answered_state((previous or {}).get('intent'),body.answers)
        except ValueError as error:
            raise HTTPException(422,str(error)) from None
        context_project=body.project.model_dump(mode='json')
        input_selection=merge_selection((previous or {}).get('selection'),body.selection)
        if body.mode=='design':
            # Expose actual compiler findings, rather than asking the model to
            # infer built-in grippers/supports from optional equipment arrays.
            check_tasks=(previous or {}).get('intent',{}).get('tasks') or [dict(existing_task_id=t.id) for t in body.project.tasks]
            static_check=service.compile(body.project,dict(kind='plan',goal='입력 근거 점검',tasks=check_tasks),input_selection)
            with host.lock:
                snapshot=host.session.snapshot(include_geometry=False) if service.active and previous and service.active==previous['id'] else None
            context_project['scenario_designer']={
                'state':scenario_state,'selection':input_selection,
                'map_changed':previous_environment is not None and digest(previous_environment)!=environment_hash,
                'runtime':{key:snapshot[key] for key in ('run_id','sim_time','status','tasks','robots','people','items','metrics')} if snapshot else None,
                'answers':body.answers,
                'static_execution_check':{
                    'basis':'existing deterministic compiler; not physical execution success',
                    'blockers':static_check.get('blockers',[]),
                    'steps':[{k:row.get(k) for k in ('id','name','kind','robot_ids','valid','resources','dependencies','confirmation')} for row in static_check.get('steps',[])],
                    'map_basis':'reviewed_floorplan' if body.project.environment.id.startswith('floorplan-') else 'authored_or_synthetic_environment',
                    'note':'Optional equipment=[] does not remove the implemented native arm gripper or carrier body support. Static validation checks their actual simulator contract; contact/custody are still observed only during execution.'},
                'executor_limits':{'cross_floor_cargo':'contact-supported carrier, compatible automatic elevator and distinct source loader / destination receiver',
                    'item_reacquisition':'dependent observed placement; explicit matching source, loading floor and reachable donor',
                    'human_item_teleport':False,'human_confirmation':'only explicit external human checks; never substitute for robotic item work'},
            }
        ontology_context=service.ontology.context(body.project,body.message)
        response=service.provider.interpret(context_project,body.message,models(),
                 (previous or {}).get('intent'),(previous or {}).get('conversation'),
                 ontology=ontology_context,spatial=service.floorplans.context(body.project),
                 conversation_key=conversation_key)
        intent=response['intent']
        if body.mode=='question':intent['kind']='question'
        if intent['kind']=='plan' and not intent.get('tasks') and not intent.get('clarifications') and not (body.mode=='design' and (intent.get('scenario',{}).get('questions') or (previous or {}).get('intent',{}).get('tasks'))):
            intent['clarifications']=[
                '모델이 실행 작업을 제안하지 않았습니다. 위 답변의 이유를 확인하고 필요한 로봇·목적지·도면 연결을 수정한 뒤 다시 요청하세요. 승인과 실행은 보류됩니다.'
                if response.get('answer') else
                '실행할 작업이 정해지지 않았습니다. 대상과 실제 출발지·목적지를 알려주세요.']
        user_content=body.message
        if body.answers:
            asked={q['id']:q['prompt'] for q in ((previous or {}).get('intent',{}).get('scenario',{}).get('questions',[]))}
            user_content+='\n\n'+'\n'.join(asked.get(key,key)+': '+value for key,value in body.answers.items())
        conversation=(previous or {}).get('conversation',[])+[{'role':'user','content':user_content},
                 {'role':'assistant','content':response['answer'],'references':response['references'],
                  'related_documents':ontology_context.get('related_documents',[]) if intent['kind']=='question' else []}]
        if body.mode=='design' and intent['kind']=='question' and previous:
            # Runtime questions append a read-only answer without invalidating approval.
            with host.lock:
                current=service.load(previous['id'])
                if current['version']!=previous['version'] or current['plan_hash']!=previous['plan_hash']:
                    raise HTTPException(409,'응답 중 초안이 변경되었습니다. 최신 대화를 여세요.')
                current['conversation']=conversation
                runtime=context_project.get('scenario_designer',{}).get('runtime')
                if runtime:
                    current['conversation'][-1]['runtime_basis']={key:runtime[key] for key in ('run_id','sim_time','status')}
                current['last_question_model_execution']=response.get('model_execution')
                service.save(current)
                return service.public(current)
        if body.mode=='design':
            try:
                intent=merge_dialogue((previous or {}).get('intent'),intent,scenario_state)
            except ValueError as error:
                raise HTTPException(422,'시나리오 변경 형식을 확인하세요: '+str(error)) from None
        # A question may reference a previous plan but never replaces its executable approval.
        proposal_previous=previous if intent['kind']=='plan' else None
        selection=input_selection
        # A conversation can outlive an edited map or a fresh robot placement.
        # Preserve pedestrian choices, but never carry retired robot identities
        # into a new executable draft. The compiler will choose the minimum
        # valid set again unless the model explicitly proposes a new selection.
        current_robot_ids={robot.id for robot in body.project.robots}
        inherited_ids=selection.get('robot_ids')
        if isinstance(inherited_ids,list) and any(robot_id not in current_robot_ids for robot_id in inherited_ids):
            selection.pop('robot_ids',None)
        if isinstance(selection.get('task_robot_ids'),dict):
            requested_tasks=intent.get('tasks')
            current_tasks={task.get('id') or task.get('existing_task_id') or f'intent-task-{index+1}'
                           for index,task in enumerate(requested_tasks if isinstance(requested_tasks,list) else [])
                           if isinstance(task,dict)}
            selection['task_robot_ids']={task_id:robot_id
                for task_id,robot_id in selection['task_robot_ids'].items()
                if task_id in current_tasks and robot_id in current_robot_ids}
            if not selection['task_robot_ids']:
                selection.pop('task_robot_ids')
        proposal_selection=response.get('selection',{})
        if not isinstance(proposal_selection,dict):raise HTTPException(422,'모델의 구성 선택 형식이 잘못되었습니다.')
        selection=merge_selection(selection,proposal_selection)
        with host.lock:
            result=service.draft(body.project,intent,selection,previous=proposal_previous,
                                 conversation=conversation,origin='model',model_execution=response.get('model_execution'),
                                 conversation_key=conversation_key)
            record=service.load(result['id'])
            record['model_proposal']=copy.deepcopy(response)
            record['input_receipt']={'project_hash':digest(body.project.model_dump(mode='json')),
                'map_id':body.project.environment.id,'map_version':body.project.environment.version,
                'selection':selection,'question_answers':body.answers,
                'ontology_hash':digest(ontology_context),'model_execution':response.get('model_execution'),
                'runtime_run_id':(context_project.get('scenario_designer',{}).get('runtime') or {}).get('run_id'),
                'runtime_sim_time':(context_project.get('scenario_designer',{}).get('runtime') or {}).get('sim_time'),
                'basis':'실제 전송 입력의 버전 요약; 모델 답변의 사실성을 보증하는 표시는 아님'}
            service.save(record)
            return service.public(record)

    @app.post('/api/plans')
    def draft(body:DraftRequest):
        return service.draft(body.project,body.intent,body.selection)

    @app.get('/api/plans')
    def plans():
        rows=[]
        for path in service.folder.glob('*.json'):
            if re.fullmatch(r'[0-9a-f]{32}',path.stem):
                for r in service.versions(path.stem):
                    rows.append({k:r.get(k) for k in ('id','version','created_at','intent','approval','origin','recovered_from')})
        return sorted(rows,key=lambda r:r['created_at'],reverse=True)

    @app.get('/api/plans/{plan_id}/versions/{version}')
    def plan_version(plan_id:str,version:int):return service.public(service.load_version(plan_id,version))

    @app.get('/api/plans/{plan_id}')
    def get(plan_id:str):return service.public(service.load(plan_id))

    @app.post('/api/plans/{plan_id}/source-check')
    def source_check(plan_id:str,body:SourceCheckRequest):
        record=service.load(plan_id)
        return dict(matches=(record['version']==body.version and
                             digest(body.project.model_dump(mode='json'))==record['source_project_hash']))

    @app.post('/api/plans/{plan_id}/revise')
    def revise(plan_id:str,body:ReviseRequest):
        with host.lock:
            previous=service.load(plan_id)
            if previous['version']!=body.version:raise HTTPException(409,'최신 계획을 다시 불러오세요.')
            intent=copy.deepcopy(previous['intent']);conversation=previous.get('conversation',[])
            changed=[]
            if body.project.model_dump(mode='json')!=previous['source_project']:changed.append('지도·로봇·물품 등 현재 편집 구성')
            if body.selection!=previous['selection']:changed.append('참여 로봇·보행자·회피 선택')
            if changed and intent.get('scenario') is not None:
                note='화면에서 '+', '.join(changed)+'을 변경하고 다시 검증했습니다. 최신 실행 구성은 작업 단계와 지도 미리보기에서 확인하세요. 이전 승인에는 자동 반영하지 않습니다.'
                intent['scenario']['changes']=[note]
                conversation=[*conversation,{'role':'user','content':'[화면 구성 변경] '+note}]
            return service.draft(body.project,intent,body.selection,previous=previous,origin=previous['origin'],conversation=conversation)

    @app.post('/api/scenarios/sample')
    def scenario_sample(body:SampleRequest):
        project=create_sample(body)
        folder=service.folder/'sample-drafts';folder.mkdir(exist_ok=True)
        record={'project':project.model_dump(mode='json'),'inputs':body.model_dump(),
            'basis':'user_selected_synthetic_defaults','limits':['실제 도면에서 인식한 환경이 아닙니다','칸막이 없는 작업 구역입니다. 물품·참여자·작업은 별도 구성하세요','시설 성능·치수는 시험 입력입니다'],'created_at':time.time()}
        write_json(folder/(project.id+'.json'),record)
        return record

    @app.post('/api/plans/{plan_id}/scenario')
    def scenario_edit(plan_id:str,body:dict):
        if set(body)-{'version','project','selection','task_id','destination_id'}:
            raise HTTPException(422,'지원하지 않는 시나리오 수정입니다')
        with host.lock:
            old=service.load(plan_id)
            if body.get('version')!=old['version']:raise HTTPException(409,'최신 초안을 다시 여세요')
            project=Project.model_validate(body['project'])
            intent=copy.deepcopy(old['intent'])
            conversation=old.get('conversation',[])
            if body.get('task_id'):
                task=next((t for t in intent.get('tasks',[]) if t.get('id')==body['task_id']),None)
                destination=next((e for e in project.environment.elements if e.id==body.get('destination_id')),None)
                if task is None or destination is None or task.get('existing_task_id'):
                    raise HTTPException(422,'수정할 단계와 현재 지도 장소를 선택하세요')
                task['destination_id']=destination.id
                task.pop('destination_xy',None);task.pop('route_points',None)
                note=task.get('name',task['id'])+' 목적지 → '+destination.name+'; 이전 경유점을 지우고 경로·실행 조건을 다시 검사합니다.'
                intent.setdefault('scenario',{})['changes']=[note]
                conversation=[*conversation,{'role':'user','content':'[지도에서 장소 변경] '+note}]
                # A prior human-check criterion can name a place/coordinate.
                # Do not silently reuse it at another physical location.
                if task.get('confirmation'):
                    q=dict(id='confirm-location-'+task['id'],field='confirmation-'+task['id'],
                        prompt='목적지가 '+destination.name+'(으)로 바뀌었습니다. 이 장소에서 수행할 확인 내용과 완료 기준을 알려주세요.',options=[])
                    questions=intent['scenario'].setdefault('questions',[])
                    intent['scenario']['questions']=[x for x in questions if x['id']!=q['id']]+[q]
            return service.draft(project,intent,body.get('selection',old['selection']),previous=old,origin=old['origin'],conversation=conversation)

    @app.post('/api/plans/{plan_id}/confirm')
    def confirm_step(plan_id:str,body:dict):
        if set(body)!={'run_id','version','task_id','note'}:raise HTTPException(422,'실행·승인 버전·단계·확인 내용을 입력하세요')
        if not isinstance(body['note'],str) or not body['note'].strip() or len(body['note'])>1000:
            raise HTTPException(422,'현장에서 확인한 내용을 1~1,000자로 입력하세요')
        with host.lock:
            record=service.load(plan_id)
            approval=record.get('approval') or {}
            if service.active!=plan_id or body['run_id']!=host.session.run_id or body['version']!=approval.get('version') or service.amendment_required or host.session.status!='running':
                raise HTTPException(409,'현재 실행 중인 승인 버전에서만 확인할 수 있습니다')
            try:result=host.session.orchestrator.confirm_step(body['task_id'],host.session.time,body['note'])
            except ValueError as error:raise HTTPException(409,str(error)) from None
            service.checkpoint(force=True)
            return result

    @app.post('/api/plans/{plan_id}/approve')
    def approve(plan_id:str,body:ApproveRequest):return service.approve(plan_id,body)

    @app.get('/api/plans/{plan_id}/result')
    def result(plan_id:str):return service.result(plan_id)

    @app.get('/api/plans/{plan_id}/runs/{run_id}')
    def approved_run_result(plan_id:str,run_id:str):return service.result_for_run(plan_id,run_id)

    @app.post('/api/plans/{plan_id}/control')
    def plan_control(plan_id:str,body:dict):
        with host.lock:
            if service.active!=plan_id or body.get('run_id')!=host.session.run_id:
                raise HTTPException(409,'현재 실행 중인 승인 계획과 일치하지 않습니다. 상태를 다시 확인하세요.')
            action=body.get('action')
            if action not in ('pause','resume'):raise HTTPException(422,'일시 정지 또는 재개를 선택하세요.')
            if action=='resume' and (service.amendment_required or host.session.status in ('failed','completed','timed_out')):
                raise HTTPException(409,'계획 변경 또는 실패를 해결한 뒤 새 계획을 승인하세요.')
            host.session.status='paused' if action=='pause' else 'running'
            service.checkpoint(force=True)
            return host.session.snapshot()

    @app.post('/api/plans/{plan_id}/stop')
    def stop(plan_id:str,body:dict):
        with host.lock:
            if service.active!=plan_id or body.get('run_id')!=host.session.run_id:raise HTTPException(409,'현재 실행 중인 계획과 실행 번호가 일치하지 않습니다.')
            terminal=host.session.status in ('completed','failed','timed_out')
            if not terminal:host.session.status='paused'
            host.session.emit('plan_recording_saved' if terminal else 'plan_stopped',None,
                '종료 상태와 실행 기록을 보존합니다.' if terminal else '사용자가 실험을 중단했습니다. 미완료 작업은 완료 처리하지 않습니다.',{})
            service.checkpoint(force=True)
            recording=host.session.recording()
            write_json(service.folder/('recording-'+plan_id+'.json'),recording)
            recordings=service.folder/'recordings';recordings.mkdir(exist_ok=True)
            write_json(recordings/(host.session.run_id+'.json'),recording)
            service.stopped_run_id=host.session.run_id
            service.active=None
            return {'status':'stopped','run_id':host.session.run_id}
