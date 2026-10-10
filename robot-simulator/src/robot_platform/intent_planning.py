"""Deterministic structured intent -> reviewable, non-executing project draft.

Natural-language interpretation belongs to the configured provider. This module
does not infer entities from text, call Session, or change an editor/run project.
"""
from copy import deepcopy
from itertools import combinations
import json
import math
import random

from pydantic import ValidationError

from .catalog import model_by_id
from .domain import CooperativeTask, Person, PersonBehavior, Pose, Project, Task
from .navigation import radius
from .plan_validation import availability, finite, fixed_base_blocked, initial_footprints_overlap, initial_observation, issue, planning_context, validate_task

VERSION = 'intent-plan-v1'
KINDS = ('patrol', 'inspect', 'delivery', 'transport', 'handoff', 'retrieve', 'load', 'unload')


def _inside(element, pose):
    dx, dy = pose.x-element.pose.x, pose.y-element.pose.y
    c, s = math.cos(element.pose.yaw), math.sin(element.pose.yaw)
    return abs(c*dx+s*dy) <= element.size.x/2 and abs(-s*dx+c*dy) <= element.size.y/2


def _build_tasks(project, intent, blockers, clarifications):
    elements = {e.id: e for e in project.environment.elements}
    existing = {t.id: t for t in project.tasks}
    robots = {r.id: r for r in project.robots}
    items = {i.id: i for i in project.items}
    requests = intent.get('tasks')
    if requests is None:
        requests = [dict(existing_task_id=t.id) for t in project.tasks]
    if not isinstance(requests, list) or len(requests) > 100:
        blockers.append(issue('invalid_tasks', '작업 목록은 최대 100개의 구조화된 항목이어야 합니다'))
        return []
    result = []
    for index, request in enumerate(requests):
        if not isinstance(request, dict):
            blockers.append(issue('invalid_task', '작업 항목 형식을 확인하세요'))
            continue
        unknown = set(request)-{'id', 'existing_task_id', 'kind', 'destination_id', 'destination_xy', 'route_points', 'source_id', 'item_id', 'robot_id', 'predecessor_ids', 'cooperation', 'name', 'timeout', 'dwell', 'confirmation', 'quantity', 'interval', 'retries', 'condition'}
        if unknown:
            blockers.append(issue('unknown_task_fields', '지원하지 않는 작업 필드: '+', '.join(sorted(unknown))))
            continue
        if request.get('existing_task_id') is not None:
            task = existing.get(request['existing_task_id'])
            if task is None:
                clarifications.append(issue('unknown_task', '선택한 기존 작업이 없습니다: '+str(request['existing_task_id'])))
                continue
            amendments=set(request)-{'existing_task_id'}
            if amendments-{'destination_xy','route_points','predecessor_ids'}:
                blockers.append(issue('ambiguous_existing_task', '기존 작업 참조와 새 작업 수정 필드를 함께 사용할 수 없습니다'))
                continue
            updated=task.model_dump(mode='json')
            destination_pose=task.destination.model_copy(deep=True)
            if 'destination_xy' in request:
                point=request['destination_xy']
                original_zones=[element for element in elements.values()
                                if element.kind in ('room','corridor') and element.floor_id==task.floor_id
                                and _inside(element,task.destination)]
                if (task.kind not in ('patrol','inspect') or not isinstance(point,dict)
                        or set(point)!={'x','y'}
                        or not all(finite(value) and not isinstance(value,bool) for value in point.values())):
                    blockers.append(issue('invalid_destination_override','순찰·점검 목적지 변경은 공간 안의 X·Y 좌표 두 개가 필요합니다'))
                    continue
                destination_pose=destination_pose.model_copy(update={'x':float(point['x']),'y':float(point['y'])})
                if not any(_inside(zone,destination_pose) for zone in original_zones):
                    blockers.append(issue('destination_outside_zone','변경한 목적지가 검토된 원래 목적 공간 밖에 있습니다'))
                    continue
                updated['destination']=destination_pose.model_dump(mode='json')
                if 'route_points' not in request:
                    updated['approved_route']=[]
            if 'route_points' in request:
                points=request['route_points']
                if (task.kind not in ('patrol','inspect') or not isinstance(points,list)
                        or not 1<=len(points)<=100
                        or any(not isinstance(point,dict) or set(point)!={'x','y'}
                               or not all(finite(value) and not isinstance(value,bool) for value in point.values())
                               for point in points)
                        or math.hypot(float(points[-1]['x'])-destination_pose.x,
                                      float(points[-1]['y'])-destination_pose.y)>.001):
                    blockers.append(issue('invalid_route_points','승인 경로는 실제 목적지로 끝나는 최대 100개의 유한한 X·Y 좌표가 필요합니다'))
                    continue
                updated['approved_route']=[destination_pose.model_copy(update={
                    'x':float(point['x']),'y':float(point['y'])}).model_dump(mode='json') for point in points]
            if 'predecessor_ids' in request:
                updated['predecessor_ids']=request['predecessor_ids']
            try:
                result.append(Task.model_validate(updated))
            except (ValidationError,ValueError,TypeError) as error:
                blockers.append(issue('invalid_task','기존 작업 변경 조건을 확인하세요: '+str(error)))
            continue
        kind = request.get('kind')
        if kind not in KINDS:
            clarifications.append(issue('task_kind_required', '순찰·점검·배송·운반·인계 중 작업 종류를 지정하세요'))
            continue
        destination = elements.get(request.get('destination_id'))
        if destination is None:
            clarifications.append(issue('destination_required', '실제 지도에 있는 목적지 식별자를 선택하세요'))
            continue
        destination_pose=destination.pose.model_copy(deep=True)
        if kind in ('delivery','transport','handoff','retrieve','load','unload') and destination.kind == 'workbench':
            destination_pose.z += destination.size.z
        if 'destination_xy' in request:
            point=request['destination_xy']
            if (request.get('kind') not in ('patrol','inspect') or not isinstance(point,dict)
                    or set(point)!={'x','y'} or not all(finite(v) and not isinstance(v,bool) for v in point.values())):
                blockers.append(issue('invalid_destination_override','순찰·점검 목적지 변경은 공간 안의 X·Y 좌표 두 개가 필요합니다'))
                continue
            destination_pose=destination_pose.model_copy(update={'x':float(point['x']),'y':float(point['y'])})
            if not _inside(destination,destination_pose):
                blockers.append(issue('destination_outside_zone','변경한 목적지가 검토된 원래 목적 공간 밖에 있습니다'))
                continue
        approved_route=[]
        if 'route_points' in request:
            points=request['route_points']
            if (kind not in ('patrol','inspect') or not isinstance(points,list) or not 1<=len(points)<=100
                    or any(not isinstance(point,dict) or set(point)!={'x','y'}
                           or not all(finite(v) and not isinstance(v,bool) for v in point.values()) for point in points)
                    or math.hypot(float(points[-1]['x'])-destination_pose.x,float(points[-1]['y'])-destination_pose.y)>.001):
                blockers.append(issue('invalid_route_points','승인 경로는 실제 목적지로 끝나는 최대 100개의 유한한 X·Y 좌표가 필요합니다'))
                continue
            approved_route=[destination_pose.model_copy(update={'x':float(point['x']),'y':float(point['y'])}) for point in points]
        item = items.get(request.get('item_id'))
        if request.get('item_id') and item is None:
            clarifications.append(issue('unknown_item', '지정한 물품이 현재 프로젝트에 없습니다'))
            continue
        if kind in ('delivery', 'transport', 'handoff') and item is None:
            clarifications.append(issue('item_required', '운반할 실제 물품을 선택하세요'))
            continue
        rid = request.get('robot_id')
        if rid is not None and rid not in robots:
            clarifications.append(issue('unknown_robot', '지정한 로봇이 현재 프로젝트에 없습니다: '+str(rid)))
            continue
        source = elements.get(request.get('source_id'))
        if request.get('source_id') is not None and source is None:
            clarifications.append(issue('unknown_source', '지정한 출발 장소가 현재 지도에 없습니다'))
            continue
        source_pose = item.pose.model_copy(deep=True) if source and item else None
        if source and item and (source.floor_id != item.floor_id or not _inside(source, item.pose)):
            if request.get('predecessor_ids') and (request.get('cooperation') or {}).get('donor_id'):
                # The sequential compiler below must match this to a prior
                # observed-placement contract, never merely a named location.
                source_pose = source.pose.model_copy(deep=True)
                if source.kind == 'workbench':source_pose.z += source.size.z
            else:
                blockers.append(issue('item_source_mismatch', '물품의 실제 초기 위치가 지정한 출발 구역 안에 있지 않습니다'))
        cooperation = request.get('cooperation')
        if cooperation is not None:
            if not isinstance(cooperation, dict) or set(cooperation)-{'carrier_id', 'receiver_id', 'donor_id', 'workspace_id', 'carrier_destination_id','loading_offset'}:
                blockers.append(issue('invalid_cooperation', '협업 역할과 실제 인계 장소 형식을 확인하세요'))
                continue
            role_ids = [cooperation.get(k) for k in ('carrier_id', 'receiver_id')]
            if cooperation.get('donor_id'):
                role_ids.append(cooperation['donor_id'])
            if any(r not in robots for r in role_ids) or len(set(role_ids)) != len(role_ids):
                clarifications.append(issue('cooperation_roles', '서로 다른 실제 운반·인수·선택적 상차 로봇을 지정하세요'))
                continue
            workspace = elements.get(cooperation.get('workspace_id'))
            meet = elements.get(cooperation.get('carrier_destination_id'))
            if workspace is None or meet is None:
                clarifications.append(issue('cooperation_place', '실제 작업 공간과 운반 로봇의 인계 위치를 선택하세요'))
                continue
            if workspace.floor_id != destination.floor_id or meet.floor_id != destination.floor_id:
                blockers.append(issue('cooperation_place_floor', '작업 공간·인계 위치·물품 목적지는 같은 층이어야 합니다'))
                continue
            cooperation = CooperativeTask(carrier_id=role_ids[0], receiver_id=role_ids[1],
                donor_id=request['cooperation'].get('donor_id'), workspace_id=workspace.id,
                source_floor_id=source.floor_id if source else item.floor_id if item else None,
                loading_offset=request['cooperation'].get('loading_offset',[0.,0.]),
                carrier_destination=meet.pose.model_copy(deep=True))
        elif kind in ('delivery', 'transport', 'handoff'):
            clarifications.append(issue('cooperation_required', '물품 작업의 운반·인수 역할과 인계 위치가 필요합니다', suggestion='실제 협업 설정을 가진 기존 작업을 선택할 수도 있습니다'))
        try:
            if any(key in request and (not finite(request[key]) or isinstance(request[key],bool)) for key in ('timeout','dwell')):
                raise ValueError('시간은 유한한 숫자여야 합니다')
            for key, limit in (('quantity',10),('retries',3)):
                if key in request and (type(request[key]) is not int or not (1 if key=='quantity' else 0)<=request[key]<=limit):
                    raise ValueError('반복은 1~10회, 재시도는 0~3회여야 합니다')
            if 'interval' in request and (not finite(request['interval']) or not 0<=request['interval']<=3600):
                raise ValueError('반복 간격은 0~3600초여야 합니다')
            task = Task(id=request.get('id', f'intent-task-{index+1}'), name=request.get('name', f'{destination.name} {kind}'),
                        kind=kind, destination=destination_pose, approved_route=approved_route, floor_id=destination.floor_id,
                        source=source_pose,
                        item_id=item.id if item else None, preferred_robot=rid,
                        predecessor_ids=request.get('predecessor_ids', []), cooperation=cooperation,
                        timeout=request.get('timeout', 120.), dwell=request.get('dwell', 1.),
                        confirmation=request.get('confirmation'), condition=request.get('condition'), quantity=request.get('quantity',1),
                        interval=request.get('interval',0), retries=request.get('retries',1))
            result.append(task)
        except (ValidationError, ValueError, TypeError) as error:
            blockers.append(issue('invalid_task', '작업 조건을 확인하세요: '+str(error)))
    return result


def _minimum_cover(requirements, limit=None):
    """Minimum count for independent roles; explicit cooperative roles stay fixed."""
    groups = [set(r['eligible_robot_ids']) for r in requirements]
    if any(not g for g in groups):
        return []
    ids = sorted(set().union(*groups)) if groups else []
    for count in range(len(ids)+1):
        if limit is not None and count > limit:
            break
        # Large fleets use a conservative greedy draft, never a false minimum.
        if len(ids) > 18:
            selected, remaining = [], groups.copy()
            while remaining:
                candidate = min(ids, key=lambda rid: (-sum(rid in g for g in remaining), rid))
                selected.append(candidate)
                remaining = [g for g in remaining if candidate not in g]
            return selected
        for selected in combinations(ids, count):
            if all(set(selected) & group for group in groups):
                return list(selected)
    return []


def _people(project, options, blockers):
    existing_count = len(project.people)
    if options is None:
        options = {}
    if not isinstance(options, dict):
        blockers.append(issue('invalid_pedestrians', '보행자 설정 형식을 확인하세요'))
        return [], {}
    unknown = set(options)-{'include', 'total', 'seed', 'allowed_floor_ids', 'zone_ids', 'behavior'}
    if unknown:
        blockers.append(issue('unknown_pedestrian_fields', '지원하지 않는 보행자 설정: '+', '.join(sorted(unknown))))
    behavior_patch = deepcopy(options.get('behavior', {}))
    if not isinstance(behavior_patch, dict):
        blockers.append(issue('pedestrian_behavior', '보행자 행동 설정 형식을 확인하세요'))
        return [], {}
    include = options.get('include', True)
    total = options.get('total', existing_count)
    seed = options.get('seed', behavior_patch.get('seed') if behavior_patch.get('seed') is not None else project.physics.seed)
    if not isinstance(include, bool) or type(total) is not int or not 0 <= total <= 200 or type(seed) is not int or not 0 <= seed <= 2**32-1:
        blockers.append(issue('invalid_pedestrian_count', '보행자 포함 여부, 0~200명 총인원, 0~4294967295 정수 시드를 확인하세요'))
        return [], {}
    if not include:
        total = 0
    floors = {f.id: f for f in project.environment.floors}
    allowed = options.get('allowed_floor_ids', behavior_patch.get('allowed_floor_ids') or sorted(floors))
    zones = options.get('zone_ids', behavior_patch.get('allowed_zone_ids', []))
    elements = {e.id: e for e in project.environment.elements}
    if not isinstance(allowed, list) or not allowed or any(not isinstance(f, str) or f not in floors for f in allowed):
        blockers.append(issue('pedestrian_floor', '보행자 이동 가능 층을 실제 층에서 선택하세요'))
        return [], {}
    if not isinstance(zones, list) or any(not isinstance(z, str) or z not in elements or elements[z].floor_id not in allowed or elements[z].kind not in ('room','corridor','waiting','entrance','loading') for z in zones):
        blockers.append(issue('pedestrian_zone', '보행자 배치 구역은 허용 층의 실제 통행 구역이어야 합니다'))
        return [], {}
    allowed = sorted(set(allowed)); zones = sorted(set(zones))
    reviewed_zones = (project.environment.id.startswith('floorplan-') and
                      'zone_ids' not in options and 'allowed_zone_ids' not in behavior_patch)
    if reviewed_zones:
        # A calibrated floorplan may be much larger than its reviewed rooms.
        # Sampling the whole floor can put a person into an unreviewed void.
        zones = sorted(e.id for e in elements.values() if e.floor_id in allowed and
                       e.kind in ('room', 'corridor'))
        if total and not zones:
            blockers.append(issue('pedestrian_zone', '도면에서 보행자가 들어갈 방·복도를 먼저 확정하세요'))
            return [], {}
    if not options:
        from .pedestrian_navigation import PedestrianNavigator
        retained = [p.model_copy(deep=True) for p in project.people]
        for index,person in enumerate(retained):
            navigator = PedestrianNavigator(project.environment,person)
            if abs(person.pose.z)>1e-6:
                blockers.append(issue('pedestrian_height','현재 보행자 초기조건은 평면 높이 z=0이어야 합니다: '+person.id))
            if not navigator.valid_pose(person.pose):
                blockers.append(issue('existing_pedestrian_placement','기존 보행자 초기 위치가 통행 가능 공간 밖입니다: '+person.id))
            if any(r.floor_id==person.floor_id and math.hypot(r.pose.x-person.pose.x,r.pose.y-person.pose.y)<radius(r)+.32 for r in project.robots):
                blockers.append(issue('existing_pedestrian_overlap','기존 보행자와 선택 로봇의 초기 여유가 부족합니다: '+person.id))
            if any(p.floor_id==person.floor_id and math.hypot(p.pose.x-person.pose.x,p.pose.y-person.pose.y)<.64 for p in retained[:index]):
                blockers.append(issue('existing_pedestrian_overlap','기존 보행자의 초기 위치가 겹칩니다: '+person.id))
            previous=person.pose
            for target in person.path:
                if abs(target.z)>1e-6 or not navigator.segment_clear(previous,target):
                    blockers.append(issue('pedestrian_route_unavailable','기존 보행자 경로가 벽·허용 구역·층 조건을 만족하지 못합니다: '+person.id))
                    break
                previous=target
            if len(person.path)>1 and not navigator.segment_clear(person.path[-1],person.path[0]):
                blockers.append(issue('pedestrian_route_unavailable','기존 보행자 반복 경로의 마지막 연결을 통과할 수 없습니다: '+person.id))
        return retained,dict(include=True,total=len(retained),seed=seed,existing_count=existing_count,
            retained_count=len(retained),added_count=0,allowed_floor_ids=allowed,zone_ids=zones,behavior=None,
            placements=[dict(id=p.id,source='existing',floor_id=p.floor_id,pose=p.pose.model_dump(),relocated=False) for p in retained],
            basis='별도 보행자 선택이 없어 기존 초기 배치와 행동을 그대로 복사')
    for key,option,expected in (('allowed_floor_ids','allowed_floor_ids',allowed),('allowed_zone_ids','zone_ids',zones)):
        if option in options and key in behavior_patch and sorted(set(behavior_patch[key]))!=expected:
            blockers.append(issue('pedestrian_behavior_conflict','전체 보행자 선택과 개별 행동의 허용 구역 설정이 서로 다릅니다'))
            return [], {}
    if 'seed' in options and behavior_patch.get('seed') is not None and behavior_patch['seed']!=seed:
        blockers.append(issue('pedestrian_behavior_conflict','전체 배치 시드와 행동 시드를 같은 보행자 설정에서 지정하세요'))
        return [], {}
    behavior = dict(mode='free_roam', allowed_floor_ids=allowed, allowed_zone_ids=zones, seed=seed)
    behavior.update(behavior_patch)
    if 'allowed_floor_ids' in options: behavior['allowed_floor_ids']=allowed
    if 'zone_ids' in options: behavior['allowed_zone_ids']=zones
    if 'seed' in options: behavior['seed']=seed
    preserve_existing = not behavior_patch and not any(k in options for k in ('seed','allowed_floor_ids','zone_ids'))
    if total == 0:
        try:
            PersonBehavior.model_validate(behavior)
        except (ValidationError,ValueError,TypeError) as error:
            blockers.append(issue('pedestrian_behavior','보행자 행동 설정이 유효하지 않습니다: '+str(error)))
            return [], {}
        return [], dict(include=include, total=0, seed=seed, existing_count=existing_count,
                        retained_count=0, added_count=0, placements=[], allowed_floor_ids=allowed, zone_ids=zones,
                        behavior=behavior, basis='편집 원본의 사람은 보존하고 이번 실행 사본에서만 제외')
    try:
        from .pedestrian_navigation import PedestrianNavigator
    except ImportError:
        blockers.append(issue('pedestrian_planner_unavailable', '보행자 정적 경로 검증기를 사용할 수 없습니다'))
        return [], {}
    rng = random.Random(seed)
    used_ids = {x.id for x in project.robots+project.items} | set(elements)
    placed, placements = [], []
    for index in range(total):
        existing = project.people[index] if index < existing_count else None
        if existing:
            data = existing.model_dump()
        else:
            pid = f'intent-person-{index+1}'
            while pid in used_ids or any(p.id == pid for p in project.people):
                pid += '-new'
            data = dict(id=pid, name=f'보행자 {index+1}', pose=dict(x=0., y=0., z=0., yaw=0.))
        if existing and preserve_existing:
            individual = deepcopy(data['behavior'])
        elif existing:
            individual = deepcopy(data['behavior']) if data['behavior'] is not None else dict(behavior)
            if data['behavior'] is None and 'mode' not in behavior_patch:
                # Legacy people follow their authored route (or stand with no
                # route); a seed/zone edit must not invent random destinations.
                individual.update(mode='route',speed_min_m_s=existing.speed,speed_max_m_s=existing.speed,
                                  stop_rate_per_s=0.,destination_change_rate_per_s=0.,crossing_rate_per_s=0.)
            individual.update(behavior_patch)
            if 'allowed_floor_ids' in options: individual['allowed_floor_ids']=allowed
            if 'zone_ids' in options: individual['allowed_zone_ids']=zones
            if 'seed' in options or behavior_patch.get('seed') is not None:
                individual['seed']=(seed+index) % (2**32)
        else:
            individual=deepcopy(behavior)
            individual['seed']=(seed+index) % (2**32)
        person_floors = (individual or {}).get('allowed_floor_ids') or ([existing.floor_id] if existing and preserve_existing else allowed)
        person_zones = (individual or {}).get('allowed_zone_ids', [])
        if any(f not in floors for f in person_floors) or any(z not in elements or elements[z].floor_id not in person_floors for z in person_zones):
            blockers.append(issue('pedestrian_behavior','개별 보행자의 층·구역 조건이 실제 지도와 맞지 않습니다'))
            break
        floor_id = existing.floor_id if existing and existing.floor_id in person_floors else person_floors[index % len(person_floors)]
        floor_zones = [elements[z] for z in person_zones if elements[z].floor_id == floor_id]
        if person_zones and not floor_zones:
            floor_id = elements[person_zones[index % len(person_zones)]].floor_id
            floor_zones = [elements[z] for z in person_zones if elements[z].floor_id == floor_id]
        data.update(floor_id=floor_id, behavior=individual)
        mode=(individual or {}).get('mode')
        if mode=='route':
            if not existing or (not existing.path and not (existing.behavior is None and 'mode' not in behavior_patch)):
                blockers.append(issue('pedestrian_route_required','고정 경로 모드에는 실제 기존 보행자의 경로가 필요합니다',suggestion='자유 배회 또는 유효한 목적지 모드를 선택하세요'))
                break
        elif 'mode' in behavior_patch:
            data['path'] = []
        try:
            person = Person.model_validate(data)
            navigator = PedestrianNavigator(project.environment, person)
        except (ValidationError, ValueError, TypeError) as error:
            blockers.append(issue('pedestrian_behavior', '보행자 행동 설정이 유효하지 않습니다: '+str(error)))
            break
        found = None
        for attempt in range(1 if existing and preserve_existing else 2500):
            if attempt == 0 and existing and existing.floor_id == floor_id:
                pose = existing.pose.model_copy(deep=True)
            elif floor_zones:
                zone = floor_zones[rng.randrange(len(floor_zones))]
                x, y = rng.uniform(-zone.size.x/2, zone.size.x/2), rng.uniform(-zone.size.y/2, zone.size.y/2)
                c, s = math.cos(zone.pose.yaw), math.sin(zone.pose.yaw)
                pose = Pose(x=zone.pose.x+c*x-s*y, y=zone.pose.y+s*x+c*y, yaw=rng.uniform(-math.pi, math.pi))
            else:
                floor = floors[floor_id]
                pose = Pose(x=rng.uniform(0, floor.width), y=rng.uniform(0, floor.depth), yaw=rng.uniform(-math.pi, math.pi))
            if not navigator.valid_pose(pose.model_dump()):
                continue
            if any(r.floor_id == floor_id and math.hypot(r.pose.x-pose.x, r.pose.y-pose.y) < radius(r)+.32 for r in project.robots):
                continue
            if any(p.floor_id == floor_id and math.hypot(p.pose.x-pose.x, p.pose.y-pose.y) < .64 for p in placed):
                continue
            found = pose
            break
        if found is None:
            blockers.append(issue('pedestrian_placement_unavailable', f'요청한 {total}명을 배치할 통행 가능 공간을 확보하지 못했습니다', suggestion='인원을 줄이거나 배치 구역을 넓히세요'))
            break
        person.pose = found
        if abs(found.z)>1e-6:
            blockers.append(issue('pedestrian_height','현재 보행자 초기조건은 평면 높이 z=0이어야 합니다: '+person.id))
            break
        if (person.behavior and person.behavior.mode=='route') or (person.behavior is None and person.path):
            previous=found
            valid=True
            for target in person.path:
                if abs(target.z)>1e-6 or not navigator.segment_clear(previous,target):
                    valid=False;break
                previous=target
            if len(person.path)>1 and not navigator.segment_clear(person.path[-1],person.path[0]):
                valid=False
            if not valid:
                blockers.append(issue('pedestrian_route_unavailable','선택한 고정 보행 경로에 통행 불가 구간이 있습니다'))
                break
        if person.behavior and person.behavior.mode=='destinations':
            if any(not navigator.valid_pose(target) or navigator.path(found,target) is None for target in person.behavior.destinations):
                blockers.append(issue('pedestrian_destination_unavailable','보행 목적지 중 현재 허용 공간에서 도달할 수 없는 지점이 있습니다'))
                break
        placed.append(person); used_ids.add(person.id)
        placements.append(dict(id=person.id, source='existing' if existing else 'added', floor_id=floor_id,
                               pose=found.model_dump(), relocated=bool(existing and (existing.floor_id != floor_id or existing.pose != found))))
    return placed, dict(include=include, total=total, seed=seed, existing_count=existing_count,
                        retained_count=min(total,existing_count), added_count=max(0,total-existing_count),
                        placements=placements, allowed_floor_ids=allowed, zone_ids=zones, behavior=deepcopy(behavior_patch) or None,
                        individual_behaviors={p.id:p.behavior.model_dump() if p.behavior else None for p in placed},
                        basis='기존 인원의 개별 행동·경로·구역·시드는 명시적으로 선택한 필드만 변경; 새 인원에 기본값 적용. 층간 보행은 지원하지 않음')


def _compile_plan(project: Project, intent: dict, selection: dict | None = None,
                  observations: dict | None = None, ontology_support: dict | None = None) -> dict:
    """Return a draft only. Approval, identity and persistence belong to API."""
    blockers, clarifications = [], []
    project = project.model_copy(deep=True)
    result = dict(version=VERSION, kind='plan', status='blocked', can_approve=False,
                  goal='', project=None, steps=[], requirements=[], alternatives=[], recommendations=[],
                  robot_options=[], selected_robot_ids=[], selection={}, pedestrians={}, blockers=blockers,
                  clarifications=clarifications, assumptions=[], resources=[], preview={}, analysis={},
                  execution_basis='편집 초기조건에서 새 실험 시작; 현재 실행의 위치·배치 변경 또는 재개가 아님')
    try:
        json.dumps([intent, selection, observations], allow_nan=False)
    except (ValueError, TypeError, OverflowError):
        blockers.append(issue('invalid_json', '계획 입력에는 유한한 JSON 값만 사용할 수 있습니다'))
        return result
    if not isinstance(intent, dict) or intent.get('kind') not in ('question', 'plan'):
        blockers.append(issue('invalid_intent', '요청 종류 question/plan을 지정하세요'))
        return result
    if set(intent)-{'kind', 'goal', 'tasks', 'assumptions', 'constraints', 'clarifications', 'faults'}:
        blockers.append(issue('unknown_intent_fields', '지원하지 않는 요청 필드가 있습니다'))
    if not isinstance(intent.get('goal', ''), str):
        blockers.append(issue('invalid_goal', '이해한 목표는 문자열이어야 합니다'))
        return result
    pending=intent.get('clarifications',[])
    if not isinstance(pending,list) or any(not isinstance(item,str) or not item.strip() for item in pending):
        blockers.append(issue('invalid_clarifications','미확정 조건은 비어 있지 않은 설명 목록이어야 합니다'))
        return result
    clarifications.extend(issue('requested_clarification',item) for item in pending)
    result.update(kind=intent['kind'], goal=intent.get('goal', ''))
    selection = deepcopy({} if selection is None else selection)
    if not isinstance(selection, dict) or set(selection)-{'robot_ids', 'task_robot_ids', 'pedestrians', 'pedestrian_avoidance'}:
        blockers.append(issue('invalid_selection', '로봇·보행자 선택 형식을 확인하세요'))
        return result
    task_robot_ids = selection.get('task_robot_ids', {})
    if (not isinstance(task_robot_ids, dict) or
            any(not isinstance(task_id, str) or not isinstance(robot_id, str)
                for task_id, robot_id in task_robot_ids.items())):
        blockers.append(issue('invalid_task_robot_selection', '작업별 대체 로봇은 작업·로봇 식별자로 선택하세요'))
        return result
    constraints = intent.get('constraints', {})
    if not isinstance(constraints, dict) or set(constraints)-{'max_robots'}:
        blockers.append(issue('invalid_constraints', '지원하는 조건은 max_robots입니다'))
        return result
    maximum = constraints.get('max_robots')
    if maximum is not None and (type(maximum) is not int or maximum < 0):
        blockers.append(issue('invalid_robot_limit', '최대 로봇 수는 0 이상의 정수여야 합니다'))
        return result
    if 'pedestrian_avoidance' in selection:
        try:
            project.policy = type(project.policy).model_validate(dict(project.policy.model_dump(), pedestrian_avoidance=selection['pedestrian_avoidance']))
        except (ValueError, TypeError) as error:
            blockers.append(issue('invalid_avoidance_policy', '사람 회피 설정을 확인하세요: '+str(error)))
    tasks = _build_tasks(project, intent, blockers, clarifications)
    if sum(t.quantity for t in tasks)>100:
        blockers.append(issue('too_many_steps','반복을 포함한 작업 단계는 100개 이하로 나누어 계획하세요'))
        return result
    last_instance = {t.id: t.id if t.quantity==1 else f'{t.id}~{t.quantity}' for t in tasks}
    expanded = []
    for task in tasks:
        for number in range(task.quantity):
            copy = task.model_copy(deep=True)
            copy.id = task.id if number==0 else f'{task.id}~{number+1}'
            copy.predecessor_ids = [last_instance.get(key,key) for key in task.predecessor_ids]
            if copy.condition:copy.condition.task_id=last_instance.get(copy.condition.task_id,copy.condition.task_id)
            if number:
                copy.predecessor_ids.append(task.id if number==1 else f'{task.id}~{number}')
            copy.release_time += number*task.interval
            copy.quantity = 1; copy.interval = 0.
            expanded.append(copy)
    tasks = expanded
    raw = project.model_dump(); raw['tasks'] = [t.model_dump() for t in tasks]
    if 'faults' in intent:
        raw['faults'] = intent['faults']
    try:
        project = Project.model_validate(raw)
    except (ValueError, TypeError) as error:
        blockers.append(issue('invalid_task_graph', '작업 관계·층·참여 로봇 설정 오류: '+str(error)))
        return result
    # A predecessor may appear later in the user's list. Compile in stable
    # topological order before adding shared-robot/item serialization edges.
    ordered, pending = [], list(tasks)
    while pending:
        ready = next(t for t in pending if set(t.predecessor_ids) <= {p.id for p in ordered})
        ordered.append(ready); pending.remove(ready)
    tasks = ordered
    owner = planning_context(project)
    by_id = {r.id: r for r in project.robots}
    if set(task_robot_ids)-{task.id for task in tasks} or set(task_robot_ids.values())-set(by_id):
        blockers.append(issue('invalid_task_robot_selection', '현재 계획에 없는 작업·로봇은 대체 선택할 수 없습니다'))
        return result
    if any(task.cooperation and task.id in task_robot_ids for task in tasks):
        blockers.append(issue('invalid_task_robot_selection', '협업 역할 변경은 새 역할 계획과 별도 승인이 필요합니다'))
        return result
    def documented_executor(robot_id, key):
        robot=by_id[robot_id]
        return ontology_support is None or key in ontology_support.get(robot.model_id,())
    requirements, evaluations = [], {}
    for task in tasks:
        if task.cooperation:
            c = task.cooperation
            roles = [('carrier',c.carrier_id),('receiver',c.receiver_id)] + ([('donor',c.donor_id)] if c.donor_id else [])
            for role, rid in roles:
                capability='transport' if role=='carrier' else 'manipulate'
                executable=documented_executor(rid,capability)
                requirements.append(dict(id=task.id+':'+role, task_id=task.id, capability=role, min_count=1,
                    eligible_robot_ids=[rid] if executable else [], locked_robot_ids=[rid] if executable else [],
                    reason='기존 또는 명시된 협업 역할; 서로 다른 로봇의 동시 참여 필요'))
                if not executable:
                    blockers.append(issue('ontology_execution_unavailable',rid+': '+capability+' 기능의 문서 근거와 시뮬레이션 연결을 확인할 수 없습니다',task_id=task.id))
            evaluations[(task.id,c.carrier_id)] = validate_task(project,task,by_id[c.carrier_id],observations=observations,owner=owner)
        else:
            preferred_robot = task_robot_ids.get(task.id, task.preferred_robot)
            candidates = [r for r in project.robots if not preferred_robot or r.id == preferred_robot]
            # A model-selected robot limits assignment, but must not hide why
            # another robot could or could not perform the same task.
            checks = {r.id: validate_task(project,task,r,observations=observations,owner=owner) for r in project.robots}
            for r in project.robots:
                if not documented_executor(r.id,task.kind):
                    checks[r.id]['blockers'].append(issue('ontology_execution_unavailable',
                        r.id+': '+task.kind+' 기능의 문서 근거와 시뮬레이션 연결을 확인할 수 없습니다',task_id=task.id))
                    checks[r.id]['valid']=False
            evaluations.update({(task.id,rid):row for rid,row in checks.items()})
            eligible = sorted(r.id for r in candidates if checks[r.id]['valid'])
            alternatives = sorted(rid for rid, row in checks.items() if row['valid'])
            requirements.append(dict(id=task.id+':operator',task_id=task.id,capability=task.kind,min_count=1,
                eligible_robot_ids=eligible,alternative_robot_ids=alternatives,
                locked_robot_ids=eligible if len(eligible)==1 else [],
                reason='사용자가 선택한 대체 로봇' if task.id in task_robot_ids else
                    '지시에서 지정한 로봇' if task.preferred_robot else
                    '작업 능력·초기 배터리·장비·지도 경로를 만족하는 로봇 1대'))
            if not eligible:
                relevant = candidates if preferred_robot else [r for r in candidates if task.kind in model_by_id(r.model_id)['capabilities']]
                if not relevant:
                    blockers.append(issue('capability_missing','요청 능력을 가진 실제 로봇이 없습니다',task_id=task.id))
                for r in relevant:
                    blockers.extend(checks[r.id]['blockers'])
    selected = selection.get('robot_ids')
    if selected is None:
        selected = _minimum_cover(requirements,maximum) if requirements else sorted(by_id)
    if not isinstance(selected,list) or any(not isinstance(r,str) or r not in by_id for r in selected) or len(set(selected))!=len(selected):
        blockers.append(issue('unknown_selected_robot','선택 목록에는 중복 없는 실제 로봇 식별자만 사용할 수 있습니다'))
        selected = []
    selected = sorted(selected)
    if maximum is not None and len(selected)>maximum:
        blockers.append(issue('robot_limit_exceeded','선택한 로봇 수가 요청한 최대 수를 초과합니다'))
    for req in requirements:
        req['selected_robot_ids'] = sorted(set(req['eligible_robot_ids'])&set(selected))
        if not req['selected_robot_ids']:
            executable_options=req['eligible_robot_ids']
            blockers.append(issue('required_capability_excluded',
                ('필수 역할의 실행 가능한 로봇을 아직 선택하지 않았습니다: '+req['capability']
                 if executable_options else
                 '현재 배치 로봇 중 능력·장비·상태·지도 경로를 모두 만족하는 작업 후보가 없습니다: '+req['capability']),
                task_id=req['task_id'],
                suggestion=('표시된 실행 가능한 대체 로봇 중 한 대를 선택하세요' if executable_options else
                            '위 로봇별 제외 이유를 확인하고 장비·위치·목적지·도면 연결을 수정한 뒤 다시 계산하세요')))
    # Revalidate from the execution copy: excluded robots cannot be needed by
    # charging forecasts, collaboration, faults, assignments or task sources.
    for fault in project.faults:
        if fault.target_id in by_id and fault.target_id not in selected:
            blockers.append(issue('incident_target_excluded',
                '돌발 상황의 대상 로봇이 구성에서 제외되었습니다: '+fault.target_id,
                suggestion='해당 로봇을 선택하거나 돌발 상황을 명시적으로 수정한 뒤 다시 검토하세요'))
    raw = project.model_dump(); raw['robots'] = [by_id[r].model_dump() for r in selected]
    raw['faults'] = [f.model_dump() for f in project.faults if f.target_id not in by_id or f.target_id in selected]
    executable_tasks = [t for t in tasks if not t.cooperation or all(r in selected for r in (t.cooperation.carrier_id,t.cooperation.receiver_id,*([t.cooperation.donor_id] if t.cooperation.donor_id else [])))]
    assignments, last_use, projected, energy_left = {}, {}, {}, {}
    for task in executable_tasks:
        if task.cooperation:
            assignments[task.id] = task.cooperation.carrier_id
        else:
            permitted = next((r['selected_robot_ids'] for r in requirements if r['task_id']==task.id),[])
            if not permitted:
                continue
            assignments[task.id] = min(permitted,key=lambda rid:(sum(v==rid for v in assignments.values()),rid))
        task.preferred_robot = assignments[task.id]
    raw['tasks'] = [t.model_dump() for t in executable_tasks if t.id in assignments]
    try:
        draft = Project.model_validate(raw)
    except (ValueError, TypeError) as error:
        blockers.append(issue('excluded_dependency', '제외한 로봇 또는 누락 작업에 의존하는 실행 구성입니다: '+str(error)))
        result.update(requirements=requirements, selected_robot_ids=selected,
                      selection=dict(robot_ids=selected), status='analysis' if intent['kind']=='question' else 'blocked')
        return result
    draft_owner = planning_context(draft)
    for index, robot in enumerate(draft.robots):
        if (fixed_base_blocked(draft,robot) if model_by_id(robot.model_id)['locomotion']=='fixed'
                else draft_owner.planner.blocked(robot.pose.x,robot.pose.y,robot.floor_id,robot)):
            blockers.append(issue('initial_robot_clearance','선택 로봇의 초기 위치에 정적 지도 여유가 없습니다',robot_id=robot.id))
        for other in draft.robots[index+1:]:
            if initial_footprints_overlap(robot,other):
                blockers.append(issue('initial_robot_overlap','선택 로봇의 초기 몸체·장비 평면이 겹칩니다: '+robot.id+', '+other.id))
    steps, resources, moved_items = [], set(), {}
    for task in draft.tasks:
        rid = task.preferred_robot
        participants = [rid]
        if task.cooperation:
            participants += [task.cooperation.receiver_id]+([task.cooperation.donor_id] if task.cooperation.donor_id else [])
        # Serialize reuse while retaining user predecessors. Independent steps
        # can still run in parallel. Project validation rejects cycles below.
        keys = participants+(['item:'+task.item_id] if task.item_id else [])
        def exclusive_prior(prior_id):
            prior=next((t for t in draft.tasks if t.id==prior_id),None)
            return bool(prior and prior.condition and task.condition and prior.condition.task_id==task.condition.task_id and prior.condition.outcome!=task.condition.outcome)
        task.predecessor_ids = sorted(set(task.predecessor_ids+[last_use[k] for k in keys if k in last_use and not exclusive_prior(last_use[k])]))
        for key in keys:
            last_use[key] = task.id
        check = validate_task(draft,task,by_id[rid],observations=observations,owner=draft_owner,
                              start=projected.get(rid),battery=energy_left.get(rid))
        if task.cooperation and task.item_id in moved_items:
            prior=moved_items[task.item_id]
            source=task.source
            matches=bool(task.cooperation.donor_id and task.cooperation.source_floor_id==prior.floor_id and source
                         and math.dist([source.x,source.y,source.z],[prior.destination.x,prior.destination.y,prior.destination.z])<.001)
            if not matches:
                check['blockers'].append(issue('item_custody_sequence_unknown','재인수에는 선행 배치와 일치하는 상차 층·물품 위치·상차 로봇이 필요합니다',task_id=task.id,suggestion='선행 배치 지점과 작업대의 실제 지지 높이를 출발 위치로 지정하세요'))
        elif task.cooperation and task.source:
            item=next(i for i in draft.items if i.id==task.item_id)
            if (task.cooperation.source_floor_id or task.floor_id)!=item.floor_id or math.dist(
                    [task.source.x,task.source.y,task.source.z],[item.pose.x,item.pose.y,item.pose.z])>.05:
                check['blockers'].append(issue('item_source_mismatch','출발 물품의 초기 위치 또는 선행 배치 근거가 일치하지 않습니다',task_id=task.id))
        if task.cooperation and rid in projected and math.hypot(projected[rid]['x']-by_id[rid].pose.x,projected[rid]['y']-by_id[rid].pose.y)>.08:
            if not (task.cooperation.source_floor_id and task.cooperation.donor_id and task.source):
                check['blockers'].append(issue('cooperation_reposition_unknown','이전 이동 후의 상차·초기 지지 위치에 대한 협업 계획이 필요합니다',task_id=task.id))
        if task.cooperation:
            moved_items[task.item_id]=task
        check['valid'] = not check['blockers']
        evaluations[(task.id,rid)]=check
        blockers.extend(check['blockers']); resources.update(check['resources'])
        # A resource appearing in two independently assigned routes is not
        # made safe merely by hiding it from parallel_with. Materialize the
        # one-at-a-time order in the executable Task graph. The task list is
        # already topologically ordered, so a predecessor here cannot cycle.
        for resource in check['resources']:
            if resource in last_use and last_use[resource] != task.id and last_use[resource] not in task.predecessor_ids and not exclusive_prior(last_use[resource]):
                task.predecessor_ids.append(last_use[resource])
            last_use[resource] = task.id
        task.predecessor_ids.sort()
        destination = task.cooperation.carrier_destination if task.cooperation else task.destination
        initial = projected.get(rid,initial_observation(draft,by_id[rid])['pose'])
        if check['energy'] and finite(check['energy'].get('estimated_work_j')):
            consumed = check['energy']['estimated_work_j']/(by_id[rid].battery_capacity_wh*3600)*100
            energy_left[rid] = energy_left.get(rid,by_id[rid].battery)-consumed
        projected[rid] = dict(destination.model_dump(),z=draft_owner.planner.floors[task.floor_id].elevation+.3)
        steps.append(dict(number=len(steps)+1,id=task.id,name=task.name,kind=task.kind,
            robot_ids=participants,roles=task.cooperation.model_dump() if task.cooperation else {'operator':rid},
            dependencies=task.predecessor_ids.copy(),parallel_with=[],source=deepcopy(initial),destination=task.destination.model_dump(),
            floor_id=task.floor_id,item_id=task.item_id,waypoints=check['route'],resources=check['resources'],
            route_legs=check['route_legs'],trip=check['trip'],
            item_source=task.source.model_dump() if task.source else None,
            confirmation=task.confirmation.model_dump() if task.confirmation else None,
            condition=task.condition.model_dump() if task.condition else None,
            completion_criterion='위치·정지 관측 후 사용자 확인' if task.confirmation else '물리 실행기의 관측 결과',
            retry_limit=task.retries, timeout_s=task.timeout,
            energy=check['energy'],valid=check['valid'],failure_behavior='관측·접촉·회피 조건 불충족 시 기존 실행기의 정지·대기·실패·명시적 복구 유지'))
    ancestors={}
    for step in steps:
        ancestors[step['id']] = set(step['dependencies']).union(*(ancestors[key] for key in step['dependencies']))
    for step in steps:
        step['parallel_with'] = [other['id'] for other in steps if other['id']!=step['id'] and other['id'] not in ancestors[step['id']] and step['id'] not in ancestors[other['id']] and not set(step['robot_ids'])&set(other['robot_ids']) and not set(step['resources'])&set(other['resources'])]
    people, people_report = _people(draft,selection.get('pedestrians'),blockers)
    if people_report:
        elements_by_id = {element.id: element for element in draft.environment.elements}
        excluded = {}
        for overlap in (draft.environment.reviewed_topology or {}).get('overlapping_zones', []):
            if overlap.get('smaller_covered_ratio', 0) < .99:
                continue
            left = elements_by_id.get(overlap.get('first_id'))
            right = elements_by_id.get(overlap.get('second_id'))
            if left is None or right is None or left.floor_id != right.floor_id:
                continue
            smaller, larger = sorted((left, right), key=lambda zone: zone.size.x * zone.size.y)
            if any(person.floor_id == smaller.floor_id and person.behavior and
                   larger.id in person.behavior.allowed_zone_ids and
                   smaller.id not in person.behavior.allowed_zone_ids for person in people):
                excluded[smaller.id] = dict(id=smaller.id,name=smaller.name,floor_id=smaller.floor_id)
        people_report['excluded_nested_zones'] = list(excluded.values())
    raw = draft.model_dump(); raw['people'] = [p.model_dump() for p in people]
    # A removed person cannot remain a fault-injection dependency either.
    removed_people = {p.id for p in project.people}-{p.id for p in people}
    raw['faults'] = [f for f in raw['faults'] if f['target_id'] not in removed_people]
    try:
        draft = Project.model_validate(raw)
    except (ValueError,TypeError) as error:
        blockers.append(issue('invalid_compiled_graph','최종 실행 구성의 관계를 확인하세요: '+str(error)))
    locked = set().union(*(set(r['locked_robot_ids']) for r in requirements)) if requirements else set()
    for robot in project.robots:
        eligible_for = [r['task_id'] for r in requirements if robot.id in r['eligible_robot_ids']]
        result['robot_options'].append(dict(id=robot.id,name=robot.name,model_id=robot.model_id,
            count=1,selected=robot.id in selected,locked=robot.id in locked,minimum_count=1 if robot.id in locked else 0,
            available=availability(project,robot,observations) is None,availability_reason=availability(project,robot,observations),
            capabilities=[key for key in model_by_id(robot.model_id)['capabilities'] if documented_executor(robot.id,key)],
            roles=[s['id'] for s in steps if robot.id in s['robot_ids']],
            eligible_for=eligible_for,task_rejections=[dict(task_id=tid,blockers=row['blockers']) for (tid,rid),row in evaluations.items() if rid==robot.id and row['blockers']],
            reason='필수 역할의 유일한 현재 대안 또는 명시 로봇' if robot.id in locked else '동등 능력 대체 선택 가능' if eligible_for else
                '현재 작업 조건을 충족하지 못해 배정 불가' if any(rid==robot.id and row['blockers'] for (_,rid),row in evaluations.items()) else
                '현재 계획에서 다른 로봇이 지정됨 · 변경하려면 새 계획 필요'))
    for req in requirements:
        choices=req.get('alternative_robot_ids',req['eligible_robot_ids'])
        if len(choices)>1:
            result['alternatives'].append(dict(requirement_id=req['id'],robot_ids=choices,minimum_count=1))
    for robot in project.robots:
        tasks_for = [r['task_id'] for r in requirements if robot.id in r['eligible_robot_ids']]
        if robot.id not in selected and len(tasks_for)>1:
            result['recommendations'].append(dict(robot_id=robot.id,basis='계획 단계의 정성 추정',comparison='현재 최소 구성의 순차 작업 대비 별도 참여 로봇 추가',reason='독립 작업을 나눌 후보입니다. 선택 시 경로·에너지·자원 충돌을 다시 계산합니다',measured=False,improvement_percent=None))
    assumptions = ['편집 초기조건에서 새 실험을 시작합니다. 현재 실행의 배치·작업은 승인 전 바꾸지 않습니다.',
                   '정적 예측에는 실제 동적 지연·충돌·파지 성공 보증이 없습니다. 실행 중 기존 관측·예약·복구 조건을 적용합니다.',
                   '협업 팔 반경·중량·적재 지지면은 정적으로 확인하며, 정확한 팔 기구학·접촉·물품 소유권은 실행 중 기존 제어기가 다시 확인합니다.',
                   '보행자 이동 때마다 재승인하지 않으며 로봇·목적지·회피 기준 변경은 새 계획 승인이 필요합니다.']
    if observations is None:
        assumptions.append('현재 가용성은 편집된 장애·배터리 초기값 기준입니다. 실제 실행 상태 관측으로 확인한 값이 아닙니다.')
    supplied = intent.get('assumptions',[])
    if isinstance(supplied,list) and all(isinstance(a,str) for a in supplied):
        assumptions += ['사용자가 검토할 가정: '+a for a in supplied]
    else:
        blockers.append(issue('invalid_assumptions','가정은 문자열 목록이어야 합니다'))
    if not tasks and not selection:
        clarifications.append(issue('goal_details_required','실행할 기존 작업 또는 보행자·로봇 구성을 선택하세요'))
    result.update(steps=steps,requirements=requirements,selected_robot_ids=selected,pedestrians=people_report,
                  selection=dict(robot_ids=selected,pedestrians=deepcopy(selection.get('pedestrians',{})),
                                 **({'task_robot_ids':deepcopy(task_robot_ids)} if task_robot_ids else {}),
                                 **({'pedestrian_avoidance':deepcopy(selection['pedestrian_avoidance'])} if 'pedestrian_avoidance' in selection else {})),
                  assumptions=assumptions,resources=sorted(resources),
                  preview=dict(routes=[dict(task_id=s['id'],robot_id=s['robot_ids'][0],floor_id=leg['floor_id'],points=[leg['start'],*leg['points']]) for s in steps for leg in s['route_legs']],people=people_report.get('placements',[]),robots=[r.model_dump() for r in draft.robots]),
                  analysis=dict(minimum_robot_count=None if any(not r['eligible_robot_ids'] for r in requirements) else len(_minimum_cover(requirements)),minimum_is_exact=len(project.robots)<=18 and all(r['eligible_robot_ids'] for r in requirements),
                                available_robot_count=sum(o['available'] for o in result['robot_options']),executor_basis='검토된 온톨로지 실행 연결·현재 장비·경로·에너지 조회' if ontology_support is not None else '실제 카탈로그·경로·기존 실행 계약 조회',estimated=True))
    if intent['kind']=='question':
        result.update(status='analysis',can_approve=False,project=None)
    else:
        result.update(status='blocked' if blockers else 'clarification' if clarifications else 'ready',
                      can_approve=not blockers and not clarifications,project=draft.model_dump())
    return deepcopy(result)


def compile_plan(project: Project, intent: dict, selection: dict | None = None,
                 observations: dict | None = None, ontology_support: dict | None = None) -> dict:
    """Untrusted structured inputs fail closed without executing anything."""
    try:
        return _compile_plan(project, intent, selection, observations, ontology_support)
    except (ValidationError, ValueError, TypeError, KeyError, IndexError, OverflowError) as error:
        return dict(version=VERSION, kind=intent.get('kind','plan') if isinstance(intent,dict) else 'plan',
                    status='blocked',can_approve=False,goal='',project=None,steps=[],requirements=[],
                    alternatives=[],recommendations=[],robot_options=[],selected_robot_ids=[],selection={},
                    pedestrians={},blockers=[issue('invalid_plan_input','계획 입력을 확인하세요: '+str(error))],
                    clarifications=[],assumptions=[],resources=[],preview={},analysis={},
                    execution_basis='편집 초기조건에서 새 실험 시작; 실행 상태 변경 없음')
