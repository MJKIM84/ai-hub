"""Pure directed same-floor polylines for the authored research AGV.

Route coordinates are floor-local (z=0). A repeated first point explicitly closes
one loop. No implicit reverse, off-route connector, branch or crossing choice.
Pose tolerance is a tracking corridor, not permission to change the route input.
"""
from copy import deepcopy
import math

VERSION='directed-guided-route-1'
TRACK_TOLERANCE_M=.10
ARRIVAL_TOLERANCE_M=.08

class GuidedRouteError(ValueError):
    def __init__(self,code):
        self.code=code
        super().__init__('AGV 지정 경로: '+code)

def _xy(p):
    try:
        values=tuple(float(p[k]) for k in ('x','y'))
    except (KeyError,TypeError,ValueError):raise GuidedRouteError('invalid_pose')
    if not all(math.isfinite(v) for v in values):raise GuidedRouteError('invalid_pose')
    return values

def _distance(a,b):
    return math.hypot(a['x']-b['x'],a['y']-b['y'])

def _cross(a,b,c):
    return (b['x']-a['x'])*(c['y']-a['y'])-(b['y']-a['y'])*(c['x']-a['x'])

def _intersects(a,b,c,d):
    # Inclusive intersection also rejects nonadjacent touching/overlapping edges.
    if max(min(a['x'],b['x']),min(c['x'],d['x']))>min(max(a['x'],b['x']),max(c['x'],d['x']))+1e-9:return False
    if max(min(a['y'],b['y']),min(c['y'],d['y']))>min(max(a['y'],b['y']),max(c['y'],d['y']))+1e-9:return False
    return _cross(a,b,c)*_cross(a,b,d)<=1e-12 and _cross(c,d,a)*_cross(c,d,b)<=1e-12

class DirectedRoute:
    def __init__(self,points):
        self.points=deepcopy(points)
        if len(points)<2:raise GuidedRouteError('at_least_two_points_required')
        for point in self.points:
            _xy(point)
            if not math.isfinite(point.get('z',0.)) or abs(point.get('z',0.))>1e-6:
                raise GuidedRouteError('same_floor_z_zero_required')
        self.closed=_distance(points[0],points[-1])<=1e-6
        self.lengths=[_distance(a,b) for a,b in zip(points,points[1:])]
        if any(v<1e-6 for v in self.lengths):raise GuidedRouteError('duplicate_consecutive_point')
        unique=self.points[:-1] if self.closed else self.points
        for i,a in enumerate(unique):
            if any(_distance(a,b)<1e-6 for b in unique[i+1:]):raise GuidedRouteError('duplicate_point')
        for i,(a,b) in enumerate(zip(points,points[1:])):
            for j in range(i+1,len(points)-1):
                c,d=points[j:j+2]
                if j==i+1 or (self.closed and i==0 and j==len(points)-2):
                    # Adjacent collinear reversal overlaps the same physical edge.
                    if abs(_cross(a,b,d))<1e-9 and abs(_cross(a,b,c))<1e-9 and (b['x']-a['x'])*(d['x']-c['x'])+(b['y']-a['y'])*(d['y']-c['y'])<0:
                        raise GuidedRouteError('reversed_overlapping_edge')
                    continue
                if _intersects(a,b,c,d):raise GuidedRouteError('self_intersection')
        self.cumulative=[0.]
        for length in self.lengths:self.cumulative.append(self.cumulative[-1]+length)
        self.total=self.cumulative[-1]

    def locate(self,pose,tolerance=TRACK_TOLERANCE_M):
        x,y=_xy(pose);candidates=[]
        for edge,(a,b,length) in enumerate(zip(self.points,self.points[1:],self.lengths)):
            fraction=max(0.,min(1.,((x-a['x'])*(b['x']-a['x'])+(y-a['y'])*(b['y']-a['y']))/(length*length)))
            px=a['x']+fraction*(b['x']-a['x']);py=a['y']+fraction*(b['y']-a['y'])
            gap=math.hypot(x-px,y-py)
            if gap<=tolerance+1e-9:candidates.append(dict(edge=edge,fraction=fraction,distance_along_m=self.cumulative[edge]+fraction*length,cross_track_m=gap,projection={'x':px,'y':py}))
        if not candidates:raise GuidedRouteError('pose_off_route')
        best=min(candidates,key=lambda row:(row['cross_track_m'],-row['distance_along_m']))
        for other in candidates:
            separation=abs(other['distance_along_m']-best['distance_along_m'])
            if self.closed:separation=min(separation,self.total-separation)
            if separation>2*tolerance+1e-6:raise GuidedRouteError('ambiguous_projection')
        if self.closed and best['distance_along_m']>=self.total-1e-9:
            best=dict(best,edge=0,fraction=0.,distance_along_m=0.)
        return best

    def path(self,start,target):
        begin=self.locate(start);goal=self.locate(target,tolerance=1e-6)
        distance=goal['distance_along_m']-begin['distance_along_m']
        if _distance(start,target)<=ARRIVAL_TOLERANCE_M:
            return dict(points=[deepcopy(target)],start=begin,goal=goal,closed=self.closed,distance_m=_distance(start,target),wraps=False,version=VERSION)
        if distance< -1e-6:
            if not self.closed:raise GuidedRouteError('goal_behind_open_route')
            distance+=self.total
        end=begin['distance_along_m']+max(0.,distance)
        waypoints=[]
        for lap in (0,1) if self.closed else (0,):
            for index,along in enumerate(self.cumulative[1:],1):
                at=along+lap*self.total
                if begin['distance_along_m']+1e-8<at<=end+1e-8:
                    waypoints.append(deepcopy(self.points[index]))
        if waypoints and _distance(waypoints[-1],target)<1e-8:waypoints[-1]=deepcopy(target)
        else:waypoints.append(deepcopy(target))
        return dict(points=waypoints,start=begin,goal=goal,closed=self.closed,distance_m=max(0.,distance),wraps=end>self.total+1e-8,version=VERSION)

    def waypoint(self,pose):
        return next((i for i,p in enumerate(self.points[:-1] if self.closed else self.points) if _distance(p,pose)<=1e-6),None)
