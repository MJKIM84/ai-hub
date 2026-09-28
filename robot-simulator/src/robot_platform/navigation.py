"""Footprint-inflated A* on explicit environment geometry, not hidden robot truth."""
import heapq
import math
from collections.abc import Mapping
from .catalog import model_by_id


def radius(robot):
    spec=model_by_id(robot.model_id)
    x,y=spec["size"]["x"],spec["size"]["y"]
    for e in robot.equipment:
        x=max(x,e.size.x);y=max(y,e.size.y)
    if robot.model_id in ("arm","mobile_manipulator"):return max(math.hypot(x,y)/2,.95)
    return math.hypot(x,y)/2


def _finite(value):
    try:
        return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
    except OverflowError:
        return False


def _point_xy(point):
    if not isinstance(point, Mapping):
        return None
    if not all(_finite(point.get(key)) for key in ('x', 'y')):
        return None
    if any(key in point and not _finite(point[key]) for key in ('z', 'yaw')):
        return None
    return float(point['x']), float(point['y'])


def _disks(peer_disks):
    if not isinstance(peer_disks, (tuple, list)):
        return None
    result = []
    for disk in peer_disks:
        if (not isinstance(disk, (tuple, list)) or len(disk) != 3
                or not all(_finite(value) for value in disk) or disk[2] < 0):
            return None
        result.append(tuple(float(value) for value in disk))
    return tuple(result)


def _segment_clear_of_disks(start, end, disks):
    dx, dy = end[0] - start[0], end[1] - start[1]
    length = math.hypot(dx, dy)
    if not math.isfinite(length):
        return False
    for x, y, clearance in disks:
        rx, ry = x - start[0], y - start[1]
        if not all(math.isfinite(value) for value in (rx, ry)):
            return False
        if length:
            ux, uy = dx / length, dy / length
            projection = rx * ux + ry * uy
            if not math.isfinite(projection):
                return False
            along = min(length, max(0., projection))
            distance = math.hypot(rx - along * ux, ry - along * uy)
        else:
            distance = math.hypot(rx, ry)
        # The required distance is inclusive. No metric epsilon expands a disk.
        if not math.isfinite(distance) or distance < clearance:
            return False
    return True


def path_clear_of_disks(start, points, peer_disks):
    """Check every XY segment against immutable center-clearance disks.

    Exact tangency is allowed. Invalid coordinates, disks or arithmetic fail
    closed, including a start inside an occupied disk and an empty route.
    """
    disks = _disks(peer_disks)
    first = _point_xy(start)
    if disks is None or first is None or not isinstance(points, (list, tuple)):
        return False
    if not _segment_clear_of_disks(first, first, disks):
        return False
    previous = first
    for point in points:
        current = _point_xy(point)
        if current is None or not _segment_clear_of_disks(previous, current, disks):
            return False
        previous = current
    return True


def _enters_open_rectangle(start, end, bounds):
    """Whether a segment enters an open rectangle (matching blocked())."""
    low, high = 0., 1.
    for a, b, minimum, maximum in zip(start, end, bounds[::2], bounds[1::2]):
        delta = b - a
        if delta == 0:
            if not minimum < a < maximum:
                return False
            continue
        t0, t1 = (minimum - a) / delta, (maximum - a) / delta
        low, high = max(low, min(t0, t1)), min(high, max(t0, t1))
        if low >= high:
            return False
    return low < high


class Planner:
    def __init__(self,environment,resolution=.35):
        self.environment=environment
        self.resolution=resolution
        self.floors={f.id:f for f in environment.floors}

    def blocked(self,x,y,floor_id,robot,margin=.1,ignore_element=None):
        clearance=radius(robot)+margin
        f=self.floors[floor_id]
        if not clearance<x<f.width-clearance or not clearance<y<f.depth-clearance:return True
        for e in self.environment.elements:
            if e.id==ignore_element:continue
            if e.floor_id!=floor_id and not (e.kind=="elevator" and floor_id in e.facility.served_floors):continue
            if e.kind=="restricted" and robot.group in e.allowed_groups:continue
            if e.kind not in ("wall","column","shelf","workbench","conveyor","obstacle","restricted","stairs","elevator","charger","dock"):continue
            dx,dy=x-e.pose.x,y-e.pose.y
            c,s=math.cos(e.pose.yaw),math.sin(e.pose.yaw)
            lx,ly=c*dx+s*dy,-s*dx+c*dy
            if e.kind in ('charger','dock'):
                # Physical contact/backplate bounds, not the painted zone size.
                if -.02-clearance<lx<.14+clearance and abs(ly)<e.size.y/2+clearance:return True
                continue
            if abs(lx)<e.size.x/2+clearance and abs(ly)<e.size.y/2+clearance:return True
        return False

    def _reviewed_edge_validator(self, floor_id, robot):
        topology = self.environment.reviewed_topology
        if topology is None:
            return None
        elements = {e.id:e for e in self.environment.elements}
        zones = [e for e in elements.values() if e.floor_id == floor_id and e.kind in ('room','corridor')]
        clearance = radius(robot) + .1
        neighbors = {}
        portals = []
        connected_zone_pairs = set()
        for edge in topology.get('connections', []):
            if edge.get('condition') not in ('reviewed_door','reviewed_opening'):
                continue
            aperture = elements.get(edge.get('via'))
            a, b = elements.get(edge.get('from_id')), elements.get(edge.get('to_id'))
            if (aperture is None or aperture.floor_id != floor_id or aperture.kind not in ('door','opening')
                    or a not in zones or b not in zones or edge.get('width_m',0) < 2*clearance):
                continue
            portals.append(aperture)
            connected_zone_pairs.add(frozenset((a.id,b.id)))
            for zone in (a,b):
                neighbors.setdefault(aperture.id,set()).add(zone.id)
                neighbors.setdefault(zone.id,set()).add(aperture.id)
        protected_insets = []
        for overlap in topology.get('overlapping_zones', []):
            a, b = elements.get(overlap.get('first_id')), elements.get(overlap.get('second_id'))
            if (a not in zones or b not in zones or
                    frozenset((a.id,b.id)) in connected_zone_pairs):
                continue
            smaller, larger = sorted((a,b),key=lambda zone:zone.size.x*zone.size.y)
            protected_insets.append((smaller,larger.id))

        def inside(element, point, padding=0.):
            dx, dy = point[0]-element.pose.x, point[1]-element.pose.y
            c, s = math.cos(element.pose.yaw), math.sin(element.pose.yaw)
            return (abs(c*dx+s*dy) <= element.size.x/2+padding and
                    abs(-s*dx+c*dy) <= element.size.y/2+padding)

        def available(point):
            containing = [e for e in zones if inside(e,point)]
            # Raster-derived boxes can overlap. Keep both memberships only
            # when this robot can use a reviewed connection between those
            # exact zones. A broad room never authorizes travel through an
            # inset room whose door is absent or too narrow for this robot.
            if containing:
                minimum = min(e.size.x * e.size.y for e in containing)
                specific = {e.id for e in containing if e.size.x * e.size.y <= minimum + 1e-9}
                nodes = set(specific)
                nodes.update(e.id for e in containing
                             if any(frozenset((e.id,other)) in connected_zone_pairs for other in specific))
                for inset, larger_id in protected_insets:
                    if inside(inset,point,clearance):
                        nodes.discard(larger_id)
            else:
                nodes = set()
            # The same 15 cm contact tolerance used when building the graph
            # bridges rasterized room boundaries and a reviewed aperture.
            nodes.update(e.id for e in portals if inside(e,point,.15))
            return nodes

        def edge_clear(start, end):
            reached = available(start)
            if not reached:
                return False
            length = math.dist(start,end)
            if not math.isfinite(length):
                return False
            count=max(1,math.ceil(length/.04))
            for index in range(1,count+1):
                t=index/count
                nodes=available((start[0]+(end[0]-start[0])*t,start[1]+(end[1]-start[1])*t))
                reached &= nodes
                if not reached:
                    return False
                pending=list(reached)
                while pending:
                    for neighbor in neighbors.get(pending.pop(),()):
                        if neighbor in nodes and neighbor not in reached:
                            reached.add(neighbor);pending.append(neighbor)
            return bool(reached)
        return edge_clear

    def path(self,start,goal,floor_id,robot,*,peer_disks=()):
        disks = _disks(peer_disks)
        if disks is None:
            return None
        if disks or self.environment.reviewed_topology is not None:
            route=self._path_with_peer_disks(start,goal,floor_id,robot,disks)
            if route is None and self.environment.reviewed_topology is not None and self.resolution>.2:
                # A reviewed door may leave a narrow but valid centre line
                # between footprint-inflated wall ends. Retry on a finer grid;
                # the same continuous collision/topology checks still decide
                # every candidate edge, so this never relaxes clearance.
                route=Planner(self.environment,resolution=.2)._path_with_peer_disks(
                    start,goal,floor_id,robot,disks)
            return route
        # Preserve the existing no-peer route, including its tie-breaking and
        # historical final-point tolerance, byte-for-byte in the branch below.
        if self.blocked(goal["x"],goal["y"],floor_id,robot):return None
        res=self.resolution
        src=(round(start["x"]/res),round(start["y"]/res)); dst=(round(goal["x"]/res),round(goal["y"]/res))
        queue=[(0.,src)]; cost={src:0.};previous={}
        moves=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        while queue:
            _,current=heapq.heappop(queue)
            if current==dst:
                cells=[dst]
                while cells[-1]!=src:cells.append(previous[cells[-1]])
                cells.reverse()
                points=[dict(x=x*res,y=y*res,z=self.floors[floor_id].elevation,yaw=0) for x,y in cells[1:]]
                if not points or math.hypot(points[-1]["x"]-goal["x"],points[-1]["y"]-goal["y"])>.03:points.append(dict(goal))
                return points
            for dx,dy in moves:
                nxt=(current[0]+dx,current[1]+dy)
                if self.blocked(nxt[0]*res,nxt[1]*res,floor_id,robot):continue
                if dx and dy and (self.blocked((current[0]+dx)*res,current[1]*res,floor_id,robot) or self.blocked(current[0]*res,(current[1]+dy)*res,floor_id,robot)):continue
                # One-way zones constrain actual edge direction in their local forward axis.
                forbidden=False
                for e in self.environment.elements:
                    if e.kind=="one_way" and e.floor_id==floor_id and abs(current[0]*res-e.pose.x)<e.size.x/2 and abs(current[1]*res-e.pose.y)<e.size.y/2:
                        if dx*math.cos(e.pose.yaw)+dy*math.sin(e.pose.yaw)<0:forbidden=True
                if forbidden:continue
                new_cost=cost[current]+math.hypot(dx,dy)
                if new_cost<cost.get(nxt,float("inf")):
                    cost[nxt]=new_cost;previous[nxt]=current
                    heapq.heappush(queue,(new_cost+math.hypot(nxt[0]-dst[0],nxt[1]-dst[1]),nxt))
        return None

    def _edge_validator(self,floor_id,robot,disks):
        """Compile the same continuous edge rules for planning and resuming."""
        if floor_id not in self.floors:
            return None
        floor = self.floors[floor_id]
        if not all(_finite(value) for value in (floor.width, floor.depth, floor.elevation)):
            return None
        clearance = radius(robot) + .1
        reviewed_clear = self._reviewed_edge_validator(floor_id,robot)
        if not _finite(clearance) or clearance < 0:
            return None
        rectangles, directions = [], []
        for element in self.environment.elements:
            if element.floor_id != floor_id and not (element.kind == 'elevator' and floor_id in element.facility.served_floors):
                continue
            if element.kind == 'restricted' and robot.group in element.allowed_groups:
                continue
            x, y, yaw = element.pose.x, element.pose.y, element.pose.yaw
            sx, sy = element.size.x, element.size.y
            if not all(_finite(value) for value in (x,y,yaw,sx,sy)):
                return None
            c, s = math.cos(yaw), math.sin(yaw)
            if element.kind == 'one_way':
                directions.append((x-sx/2,x+sx/2,y-sy/2,y+sy/2,c,s))
            if element.kind not in ('wall','column','shelf','workbench','conveyor','obstacle','restricted','stairs','elevator','charger','dock'):
                continue
            bounds = (-.02-clearance,.14+clearance,-sy/2-clearance,sy/2+clearance) if element.kind in ('charger','dock') else (-sx/2-clearance,sx/2+clearance,-sy/2-clearance,sy/2+clearance)
            rectangles.append((x,y,c,s,bounds))

        def edge_clear(p,q):
            if not all(clearance < point[0] < floor.width-clearance and clearance < point[1] < floor.depth-clearance for point in (p,q)):
                return False
            if reviewed_clear is not None and not reviewed_clear(p,q):
                return False
            if not _segment_clear_of_disks(p,q,disks):
                return False
            for x,y,c,s,bounds in rectangles:
                local = tuple((c*(point[0]-x)+s*(point[1]-y),-s*(point[0]-x)+c*(point[1]-y)) for point in (p,q))
                if not all(math.isfinite(value) for point in local for value in point):
                    return False
                if _enters_open_rectangle(*local,bounds):
                    return False
            for *bounds,c,s in directions:
                forward = (q[0]-p[0])*c + (q[1]-p[1])*s
                if not math.isfinite(forward) or (forward < 0 and _enters_open_rectangle(p,q,bounds)):
                    return False
            return True

        return edge_clear

    def path_clear(self,start,points,floor_id,robot,*,peer_disks=()):
        """Validate a fixed polyline without replanning or changing its points.

        The observed start-to-first-point join is included. Static footprint,
        one-way direction, floor boundaries and optional peer clearances use
        the same continuous rules as observed-peer planning. Unknown inputs
        fail closed. An empty polyline still validates the occupied start.
        """
        first, disks = _point_xy(start), _disks(peer_disks)
        if first is None or disks is None or not isinstance(points,(list,tuple)):
            return False
        edge_clear = self._edge_validator(floor_id,robot,disks)
        if edge_clear is None or not edge_clear(first,first):
            return False
        previous = first
        for point in points:
            current = _point_xy(point)
            if current is None or not edge_clear(previous,current):
                return False
            previous = current
        return True

    def _path_with_peer_disks(self,start,goal,floor_id,robot,disks):
        a, b = _point_xy(start), _point_xy(goal)
        res = self.resolution
        if (a is None or b is None or floor_id not in self.floors
                or not _finite(res) or res <= 0
                or not _segment_clear_of_disks(a,a,disks)
                or not _segment_clear_of_disks(b,b,disks)):
            return None
        floor = self.floors[floor_id]
        edge_clear = self._edge_validator(floor_id,robot,disks)
        if edge_clear is None:
            return None

        if not edge_clear(a,a) or not edge_clear(b,b):
            return None
        if edge_clear(a,b):
            return [dict(goal)]
        coordinates = (*a,*b)
        if not all(math.isfinite(value/res) for value in coordinates):
            return None
        src = tuple(round(value/res) for value in a)
        dst = tuple(round(value/res) for value in b)
        moves = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
        queue, cost, previous = [], {}, {}
        def position(cell):
            return cell[0]*res,cell[1]*res
        # The graph source is the observed pose, never its rounded grid cell.
        # Each seed must be reachable from that exact pose by a checked edge.
        for dx,dy in ((0,0),*moves):
            cell = (src[0]+dx,src[1]+dy)
            point = position(cell)
            if edge_clear(a,point):
                distance = math.dist(a,point)
                cost[cell],previous[cell] = distance,None
                heapq.heappush(queue,(distance+math.dist(point,b),distance,cell))
        while queue:
            _,travelled,current = heapq.heappop(queue)
            if travelled != cost[current]:
                continue
            point = position(current)
            if abs(current[0]-dst[0]) <= 1 and abs(current[1]-dst[1]) <= 1 and edge_clear(point,b):
                cells = [current]
                while previous[cells[-1]] is not None:
                    cells.append(previous[cells[-1]])
                cells.reverse()
                points = [dict(x=position(cell)[0],y=position(cell)[1],z=floor.elevation,yaw=0) for cell in cells]
                if position(cells[-1]) == b:
                    points.pop()
                points.append(dict(goal))
                return points if path_clear_of_disks(start,points,disks) else None
            for dx,dy in moves:
                nxt = (current[0]+dx,current[1]+dy)
                target = position(nxt)
                if not edge_clear(point,target):
                    continue
                if dx and dy and (self.blocked((current[0]+dx)*res,current[1]*res,floor_id,robot) or self.blocked(current[0]*res,(current[1]+dy)*res,floor_id,robot)):
                    continue
                distance = travelled+math.dist(point,target)
                if distance < cost.get(nxt,math.inf):
                    cost[nxt],previous[nxt] = distance,current
                    heapq.heappush(queue,(distance+math.dist(target,b),distance,nxt))
        return None
