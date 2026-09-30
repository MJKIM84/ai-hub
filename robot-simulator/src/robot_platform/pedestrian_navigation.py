"""Continuous planar pedestrian clearance on the approved static map.

No facility passenger controller exists for pedestrians: doors, stairs, ramps
and elevators are conservatively unavailable. This never changes a body pose.
"""
from __future__ import annotations
import heapq
import math
from .navigation import radius


def xy(pose):
    if hasattr(pose, 'model_dump'):
        pose = pose.model_dump()
    try:
        point = float(pose['x']), float(pose['y'])
    except (KeyError, TypeError, ValueError, OverflowError):
        return None
    return point if all(math.isfinite(v) for v in point) else None


def validate_pedestrian_placements(project):
    """Reject impossible new-behavior spawns before creating a physics world.

    Legacy scenes remain accepted. Mixed pairs are checked whenever either
    person uses the opt-in behavior; no authored original is relocated here.
    """
    for index,person in enumerate(project.people):
        if person.behavior is not None or project.policy.pedestrian_avoidance is not None:
            if abs(person.pose.z)>1e-6 or not PedestrianNavigator(project.environment,person).valid_pose(person.pose):
                raise ValueError(f'보행자 {person.id}: 초기 위치가 허용된 평면 통행 공간 밖입니다')
            for robot in project.robots:
                if robot.floor_id==person.floor_id and math.hypot(robot.pose.x-person.pose.x,robot.pose.y-person.pose.y)<radius(robot)+.27:
                    raise ValueError(f'보행자 {person.id}: 로봇 {robot.id}과 초기 배치가 겹칩니다')
        for other in project.people[:index]:
            if person.behavior is None and other.behavior is None and project.policy.pedestrian_avoidance is None:continue
            if person.floor_id==other.floor_id and math.hypot(other.pose.x-person.pose.x,other.pose.y-person.pose.y)<.49:
                raise ValueError(f'보행자 {person.id}: 다른 보행자와 초기 배치가 겹칩니다')
class PedestrianNavigator:
    RADIUS = .27  # actual torso radius .22 m + 5 cm map clearance
    BLOCKED = {'wall','column','shelf','workbench','conveyor','obstacle','restricted',
               'door','stairs','ramp','elevator','charger','dock'}

    def __init__(self, environment, person, resolution=.3):
        self.floor = next(f for f in environment.floors if f.id == person.floor_id)
        self.floor_id = person.floor_id
        self.resolution = resolution
        self.obstacles, self.zones, self.directions = [], [], []
        behavior = person.behavior
        selected = set(behavior.allowed_zone_ids) if behavior else set()
        for e in environment.elements:
            if e.floor_id != person.floor_id:
                continue
            rect = (e.pose.x,e.pose.y,math.cos(e.pose.yaw),math.sin(e.pose.yaw),e.size.x/2,e.size.y/2)
            if e.kind in self.BLOCKED and not (e.kind == 'restricted' and e.pedestrian_access):
                self.obstacles.append(rect)
            if e.id in selected:
                self.zones.append(rect)
            if e.kind == 'one_way':
                self.directions.append(rect)
        # Raster-derived rooms may be nested. Selecting a broad reviewed room
        # must not silently authorize roaming through a separate inset room.
        # The exclusion is applied to both spawn validation and every walking
        # segment, with the same body clearance as ordinary obstacles.
        topology = environment.reviewed_topology or {}
        elements = {e.id: e for e in environment.elements if e.floor_id == person.floor_id}
        excluded = set()
        for overlap in topology.get('overlapping_zones', []):
            if overlap.get('floor_id') != person.floor_id or overlap.get('smaller_covered_ratio', 0) < .99:
                continue
            left, right = elements.get(overlap.get('first_id')), elements.get(overlap.get('second_id'))
            if left is None or right is None:
                continue
            smaller, larger = sorted((left, right), key=lambda e: e.size.x * e.size.y)
            if larger.id in selected and smaller.id not in selected and smaller.id not in excluded:
                e = smaller
                self.obstacles.append((e.pose.x, e.pose.y, math.cos(e.pose.yaw),
                                       math.sin(e.pose.yaw), e.size.x/2, e.size.y/2))
                excluded.add(e.id)
        self.require_zones = bool(selected)

    @staticmethod
    def local(point, rect):
        x,y,c,s,*_ = rect
        return c*(point[0]-x)+s*(point[1]-y), -s*(point[0]-x)+c*(point[1]-y)

    @staticmethod
    def interval(a,b,hx,hy):
        lo,hi = 0.,1.
        if hx < 0 or hy < 0:
            return None
        for start,end,half in zip(a,b,(hx,hy)):
            delta=end-start
            if delta == 0:
                if abs(start)>half:return None
            else:
                u,v=(-half-start)/delta,(half-start)/delta
                lo,hi=max(lo,min(u,v)),min(hi,max(u,v))
                if lo>hi:return None
        return lo,hi

    def segment_clear(self, start, goal):
        a,b=xy(start),xy(goal)
        if a is None or b is None:return False
        r=self.RADIUS
        if not all(r <= p[0] <= self.floor.width-r and r <= p[1] <= self.floor.depth-r for p in (a,b)):
            return False
        for rect in self.obstacles:
            u,v=self.local(a,rect),self.local(b,rect)
            if self.interval(u,v,rect[4]+r,rect[5]+r) is not None:return False
        for rect in self.directions:
            u,v=self.local(a,rect),self.local(b,rect)
            if v[0] < u[0] and self.interval(u,v,rect[4],rect[5]) is not None:return False
        if self.require_zones:
            intervals=[]
            for rect in self.zones:
                hit=self.interval(self.local(a,rect),self.local(b,rect),rect[4]-r,rect[5]-r)
                if hit is not None:intervals.append(hit)
            end=0.
            for lo,hi in sorted(intervals):
                if lo>end:return False
                end=max(end,hi)
                if end>=1:return True
            return False
        return True

    def valid_pose(self, pose):
        return self.segment_clear(pose,pose)

    def path(self, start, goal):
        a,b=xy(start),xy(goal)
        if a is None or b is None or not self.valid_pose(start) or not self.valid_pose(goal):return None
        target=dict(x=b[0],y=b[1],z=0.,yaw=0.)
        if self.segment_clear(start,goal):return [target]
        res=self.resolution
        src=(round(a[0]/res),round(a[1]/res));dst=(round(b[0]/res),round(b[1]/res))
        moves=((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
        point=lambda cell:dict(x=cell[0]*res,y=cell[1]*res,z=0.,yaw=0.)
        queue=[];cost={};prev={}
        for dx,dy in ((0,0),*moves):
            cell=(src[0]+dx,src[1]+dy);p=point(cell)
            if self.segment_clear(start,p):
                distance=math.dist(a,xy(p));cost[cell]=distance;prev[cell]=None
                heapq.heappush(queue,(distance+math.dist(xy(p),b),distance,cell))
        visits=0
        while queue and visits<50000:
            _,distance,current=heapq.heappop(queue)
            if distance!=cost[current]:continue
            visits+=1;p=point(current)
            if max(abs(current[0]-dst[0]),abs(current[1]-dst[1]))<=1 and self.segment_clear(p,target):
                cells=[current]
                while prev[cells[-1]] is not None:cells.append(prev[cells[-1]])
                route=[point(cell) for cell in reversed(cells)]+[target]
                # Remove only corners whose complete shortcut is allowed.
                short=[];anchor=dict(x=a[0],y=a[1]);index=0
                while index<len(route):
                    far=index
                    while far+1<len(route) and self.segment_clear(anchor,route[far+1]):far+=1
                    anchor=route[far];short.append(anchor);index=far+1
                return short
            for dx,dy in moves:
                nxt=(current[0]+dx,current[1]+dy);q=point(nxt)
                if not self.segment_clear(p,q):continue
                new=distance+res*math.hypot(dx,dy)
                if new<cost.get(nxt,math.inf):
                    cost[nxt]=new;prev[nxt]=current
                    heapq.heappush(queue,(new+math.dist(xy(q),b),new,nxt))
        return None
