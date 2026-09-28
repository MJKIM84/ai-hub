"""Sampled noisy observation bus. No live reference to the simulator is exposed."""
from collections import deque
from copy import deepcopy
import numpy as np


class ObservationBus:
    def __init__(self, project):
        self.rng=np.random.default_rng(project.physics.seed)
        self.settings={r.id:r.sensors for r in project.robots}
        self.last_sample={r.id:-float("inf") for r in project.robots}
        self.pending={r.id:deque() for r in project.robots}
        self.latest={}

    def sample(self, robot_id, time, truth, battery, fault, sensors=None):
        config=self.settings[robot_id]
        if time-self.last_sample[robot_id]+1e-12 < 1/config.rate_hz:return
        self.last_sample[robot_id]=time
        if fault in ("communication","sensor") or self.rng.random()<config.dropout:return
        observation=deepcopy(truth)
        for key in ("x","y","z"):
            observation["pose"][key]+=float(self.rng.normal(0,config.position_noise))
        observation["pose"]["yaw"]+=float(self.rng.normal(0,config.yaw_noise))
        observation.update(robot_id=robot_id,sampled_at=time,battery=battery,fault=fault,sensors=deepcopy(sensors or {}))
        lidar=observation["sensors"].get("lidar")
        if isinstance(lidar,dict):
            lidar["ranges"]=[float(np.clip(x+self.rng.normal(0,config.position_noise),0,lidar["max_range"])) for x in lidar["ranges"]]
            lidar["noise_std_m"]=config.position_noise
        for item in observation["sensors"].get("items",[]):
            item["position"]=[float(x+self.rng.normal(0,config.position_noise)) for x in item["position"]]
            item["position_noise_std_m"]=config.position_noise
        # This opt-in sensor consumes no extra random values for legacy runs.
        pedestrians=observation['sensors'].get('pedestrians')
        if isinstance(pedestrians,dict):
            for person in pedestrians.get('people',[]):
                person['position']=[float(x+self.rng.normal(0,config.position_noise)) for x in person['position']]
                person['position_noise_std_m']=config.position_noise
            pedestrians['sampled_at']=time
        deliver_at=time+config.observation_delay+config.communication_delay
        self.pending[robot_id].append((deliver_at,observation))

    def deliver(self,time):
        for robot_id,queue in self.pending.items():
            while queue and queue[0][0]<=time+1e-12:
                received_at,obs=queue.popleft()
                obs["received_at"]=received_at
                self.latest[robot_id]=obs
        return deepcopy(self.latest)
