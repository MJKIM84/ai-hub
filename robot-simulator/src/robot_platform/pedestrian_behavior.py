"""Seeded simulation-time goals, stops and crossings within approved space."""
import hashlib
import math
import random
from .pedestrian_navigation import PedestrianNavigator


class FreeWalking:
    def __init__(self, person, environment, seed):
        self.person=person;self.config=person.behavior
        self.navigator=PedestrianNavigator(environment,person)
        effective_seed=seed if self.config.seed is None else self.config.seed
        digest=hashlib.sha256(f'{effective_seed}\0{person.id}\0free-walking-v1'.encode()).digest()
        self.rng=random.Random(int.from_bytes(digest[:16],'big'))
        self.destination=None;self.route=[];self.speed=0.;self.started=False
        self.next_stop=self.next_change=self.next_cross=math.inf
        self.paused_until=None;self.next_plan=0.;self.route_index=0;self.crossing=False

    def wait(self, rate):
        return self.rng.expovariate(rate) if rate else math.inf

    def select(self, position, reading, now, events, cross=False):
        config=self.config;start=dict(x=position[0],y=position[1])
        candidates=[]
        if cross:
            moving=[n for n in reading['neighbors'] if n.get('kind')=='robot' and math.hypot(*n['velocity'][:2])>.05]
            if moving:
                actor=min(moving,key=lambda n:math.dist(position[:2],n['position'][:2]))
                vx,vy=actor['velocity'][:2];speed=math.hypot(vx,vy);nx,ny=-vy/speed,vx/speed
                side=1 if (position[0]-actor['position'][0])*nx+(position[1]-actor['position'][1])*ny>=0 else -1
                offset=actor['radius']+.9
                candidates=[dict(x=actor['position'][0]+vx-side*offset*nx,
                                 y=actor['position'][1]+vy-side*offset*ny,z=0.,yaw=0.)]
        elif config.mode in ('route','destinations'):
            choices=self.person.path if config.mode=='route' else config.destinations
            if choices:
                if config.mode=='route':
                    candidates=[choices[self.route_index%len(choices)].model_dump()]
                    self.route_index+=1
                else:
                    candidates=[p.model_dump() for p in choices]
                    self.rng.shuffle(candidates)
        else:
            r=self.navigator.RADIUS;f=self.navigator.floor
            candidates=[dict(x=self.rng.uniform(r,f.width-r),y=self.rng.uniform(r,f.depth-r),z=0.,yaw=0.) for _ in range(32)]
        for goal in candidates:
            if math.hypot(goal['x']-position[0],goal['y']-position[1])<.25:continue
            if abs(goal.get('z',0))>1e-6:continue
            route=self.navigator.path(start,goal)
            if route:
                self.destination=goal;self.route=route;self.crossing=cross
                self.speed=self.rng.uniform(config.speed_min_m_s,config.speed_max_m_s)
                events.append(dict(type='destination_changed',time=now,destination=dict(goal),
                                   behavior='crossing' if cross else config.mode,speed_m_s=self.speed))
                return True
        self.next_plan=now+1.
        return False

    def nominal(self, position, reading, now, events):
        c=self.config
        if now<c.start_delay_s:
            return (0.,0.),'scheduled_start'
        if not self.started:
            self.started=True;self.next_stop=now+self.wait(c.stop_rate_per_s)
            self.next_change=now+self.wait(c.destination_change_rate_per_s)
            self.next_cross=now+self.wait(c.crossing_rate_per_s)
        if not self.navigator.valid_pose(dict(x=position[0],y=position[1])):
            return (0.,0.),'outside_allowed_space'
        if self.paused_until is not None:
            if now<self.paused_until:return (0.,0.),'behavior_pause'
            events.append(dict(type='walking_resumed',time=now))
            self.paused_until=None;self.next_stop=now+self.wait(c.stop_rate_per_s)
        if now>=self.next_stop:
            duration=self.rng.uniform(c.stop_duration_min_s,c.stop_duration_max_s)
            self.paused_until=now+duration
            events.append(dict(type='walking_paused',time=now,duration=duration))
            return (0.,0.),'behavior_pause'
        if now>=self.next_cross:
            self.next_cross=now+self.wait(c.crossing_rate_per_s)
            self.select(position,reading,now,events,cross=True)
        if now>=self.next_change:
            self.next_change=now+self.wait(c.destination_change_rate_per_s)
            self.select(position,reading,now,events)
        start=dict(x=position[0],y=position[1])
        while self.route and math.hypot(self.route[0]['x']-position[0],self.route[0]['y']-position[1])<.08:
            if len(self.route)>1 and not self.navigator.segment_clear(start,self.route[1]):break
            self.route.pop(0)
        if not self.route:
            if now<self.next_plan or not self.select(position,reading,now,events):
                arrived=self.destination is not None and math.hypot(self.destination['x']-position[0],self.destination['y']-position[1])<.3
                return (0.,0.),'at_destination' if arrived else 'no_allowed_destination'
        target=self.route[0];dx,dy=target['x']-position[0],target['y']-position[1];distance=math.hypot(dx,dy)
        if not self.navigator.segment_clear(start,target):
            self.route=[];self.next_plan=now+1.
            return (0.,0.),'route_blocked'
        speed=min(self.speed,distance/.4)
        return (speed*dx/distance,speed*dy/distance) if distance else (0.,0.),'crossing' if self.crossing else 'walking'

    def constrain(self, position, velocity):
        start=dict(x=position[0],y=position[1])
        end=dict(x=start['x']+velocity[0]*.5,y=start['y']+velocity[1]*.5)
        return velocity if self.navigator.segment_clear(start,end) else (0.,0.)
