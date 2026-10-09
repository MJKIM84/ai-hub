"""MJCF composition and physical truth. Runtime motion only through actuators/forces."""
from __future__ import annotations

import copy
import math
import xml.etree.ElementTree as ET
from pathlib import Path

import mujoco
import numpy as np

from .catalog import model_by_id
from .domain import Project

ROOT = Path(__file__).resolve().parents[2]
SPOT = ROOT / "assets/robots/spot"
GEOM_TYPES = {0:"plane",1:"hfield",2:"sphere",3:"capsule",4:"ellipsoid",5:"cylinder",6:"box",7:"mesh",8:"sdf"}


def vec(values):
    return " ".join(str(float(v)) for v in values)


def node(parent, tag, **attrs):
    return ET.SubElement(parent,tag,{k:str(v) for k,v in attrs.items()})


def quat_yaw(yaw):
    return [math.cos(yaw/2),0,0,math.sin(yaw/2)]


def yaw_of(q):
    w,x,y,z=q
    return math.atan2(2*(w*z+x*y),1-2*(y*y+z*z))


class PhysicsWorld:
    def __init__(self, project: Project):
        self.project = project.model_copy(deep=True)
        self.floor_heights = {f.id:f.elevation for f in project.environment.floors}
        self.robot_body_names: dict[str,str] = {}
        self.initial_joints: dict[str,float] = {}
        self.entity_types = {r.id:"robot" for r in project.robots} | {p.id:"person" for p in project.people} | {i.id:"item" for i in project.items} | {e.id:"facility" for e in project.environment.elements}
        self.xml = self._build()
        self.model = mujoco.MjModel.from_xml_string(self.xml)
        self.data = mujoco.MjData(self.model)
        # Initial conditions only; never used by runtime commands.
        for name,value in self.initial_joints.items():
            j=self.model.joint(name)
            self.data.qpos[j.qposadr[0]]=value
        mujoco.mj_forward(self.model,self.data)
        self.robot_bodies={key:self.model.body(name).id for key,name in self.robot_body_names.items()}
        self._joint_observations={rid:[(self.model.joint(j).name.split('/',1)[1],int(self.model.jnt_qposadr[j]))
            for j in range(self.model.njnt) if self.model.joint(j).name.startswith(rid+'/')
            and int(self.model.jnt_type[j]) not in (int(mujoco.mjtJoint.mjJNT_FREE),int(mujoco.mjtJoint.mjJNT_BALL))]
            for rid in self.robot_bodies}
        self._geom_entity_ids=[self.entity_for_geom(gid) for gid in range(self.model.ngeom)]
        self.controllers={}
        self.arm_controllers={}
        self.controller_errors={}
        if any(r.model_id=="spot" for r in project.robots):
            from .controllers.spot import SpotController
            for r in project.robots:
                if r.model_id=="spot":
                    self.controllers[r.id]=SpotController(self.model,robot_id=r.id)
        from .controllers.manipulation import ManipulationController
        for r in project.robots:
            if r.model_id in ("arm","mobile_manipulator"):
                self.arm_controllers[r.id]=ManipulationController(self.model,r.id)
        self.commands={r.id:dict(v=0.,w=0.,mode="stand") for r in project.robots}
        self._gains=self.model.actuator_gainprm.copy()
        self._biases=self.model.actuator_biasprm.copy()
        self._actuators={r.id:[a for a in range(self.model.nu) if self.model.actuator(a).name.startswith(r.id+"/")] for r in project.robots}
        self._control_elapsed=1/project.physics.control_hz
        self._facilities={e.id:e for e in self.project.environment.elements if e.kind=="elevator"}
        self._facility_commands={eid:dict(lift_target=0.,door_target=0.,hold=True,max_speed=e.facility.speed,door_duration=e.facility.door_duration) for eid,e in self._facilities.items()}
        self._facility_references={eid:{"lift":0.,"doors":{name:0. for name in self._door_names(e)}} for eid,e in self._facilities.items()}
        self._chargers={e.id:e for e in self.project.environment.elements if e.kind in ("charger","dock")}
        self._charging_robots={r.id:r for r in self.project.robots if model_by_id(r.model_id)["locomotion"] in ("differential","guided")}
        self._robot_charge_pads={self.model.geom(f"{rid}/charge-{side}").id:(rid,side) for rid in self._charging_robots for side in ("left","right")}
        self._station_charge_pads={self.model.geom(f"{eid}/pad-{side}").id:(eid,side) for eid in self._chargers for side in ("left","right")}

    def _build(self):
        p=self.project
        root=ET.Element("mujoco",model=p.name)
        node(root,"compiler",angle="radian",autolimits="true")
        node(root,"option",timestep=p.physics.timestep,gravity="0 0 -9.81",integrator="implicitfast",cone="elliptic",impratio=p.physics.impratio,iterations="100" if p.physics.fidelity=="detailed" else "30")
        default=node(root,"default")
        node(default,"geom",friction="0.8 0.005 0.0001",solref="0.01 1")
        node(default,"joint",damping="0.1",armature="0.01")
        asset=node(root,"asset")
        world=node(root,"worldbody")
        actuator=node(root,"actuator")
        contact=node(root,"contact")
        self.eq=node(root,"equality")
        node(world,"light",pos="5 5 15",dir="0 0 -1")
        spot=None
        if any(r.model_id=="spot" for r in p.robots):
            spot=ET.parse(SPOT/"spot.xml").getroot()
            for child in spot.find("asset"):
                c=copy.deepcopy(child)
                if c.tag=="mesh":
                    c.set("file",str(SPOT/"assets"/c.get("file")))
                asset.append(c)
            for child in spot.find("default"):
                default.append(copy.deepcopy(child))
        for floor in p.environment.floors:
            # Upper-floor slabs have genuine openings at vertical links.
            holes=[]
            for e in p.environment.elements:
                bottom=self.floor_heights[e.floor_id]+e.pose.z
                shaft_floor=e.kind=="elevator" and (floor.id in e.facility.served_floors or bottom<=floor.elevation<=bottom+e.size.z+.1)
                stair_floor=e.kind=="stairs" and bottom<floor.elevation<=bottom+e.size.z+.1
                if shaft_floor or stair_floor:
                    # Axis-aligned conservative cutout covers rotated connections.
                    clearance=.24 if e.kind=="elevator" else 0
                    extent_x=abs(math.cos(e.pose.yaw))*(e.size.x+clearance)+abs(math.sin(e.pose.yaw))*(e.size.y+clearance)
                    extent_y=abs(math.sin(e.pose.yaw))*(e.size.x+clearance)+abs(math.cos(e.pose.yaw))*(e.size.y+clearance)
                    holes.append((e.pose.x-extent_x/2,e.pose.x+extent_x/2,e.pose.y-extent_y/2,e.pose.y+extent_y/2))
            xs=sorted({0.,floor.width,*[max(0,min(floor.width,v)) for h in holes for v in h[:2]]})
            ys=sorted({0.,floor.depth,*[max(0,min(floor.depth,v)) for h in holes for v in h[2:]]})
            for i,(x0,x1) in enumerate(zip(xs,xs[1:])):
                for j,(y0,y1) in enumerate(zip(ys,ys[1:])):
                    x,y=(x0+x1)/2,(y0+y1)/2
                    if any(a<x<b and c<y<d for a,b,c,d in holes): continue
                    node(world,"geom",name=f"floor/{floor.id}/{i}-{j}",type="box",size=vec([(x1-x0)/2,(y1-y0)/2,.1]),pos=vec([x,y,floor.elevation-.1]),rgba="0.86 0.86 0.80 1")
        for e in p.environment.elements:
            z=self.floor_heights[e.floor_id]+e.pose.z
            body=node(world,"body",name=f"{e.id}/body",pos=vec([e.pose.x,e.pose.y,z]),quat=vec(quat_yaw(e.pose.yaw)))
            sx,sy,sz=e.size.x,e.size.y,e.size.z
            common=dict(friction=f"{e.friction} 0.005 0.0001")
            if e.kind in ("room","corridor","opening","restricted","speed_zone","one_way","waiting","entrance","loading","charger","dock"):
                colors={"opening":"0.16 0.67 0.50 0.35","restricted":"0.8 0.3 0.2 0.25","charger":"0.25 0.65 0.42 0.7","dock":"0.35 0.5 0.7 0.6"}
                node(body,"geom",name=f"{e.id}/zone",type="box",size=vec([sx/2,sy/2,.007]),pos="0 0 .008",contype="0",conaffinity="0",rgba=colors.get(e.kind,"0.55 0.65 0.65 0.15"))
                if e.kind in ("charger","dock"):
                    # Authored research contact interface: x=0 is the station
                    # connection plane, approached by driving along +local X.
                    pitch=min(.20,sy*.25)
                    half_width=min(.10,sy*.15)
                    for side,sign in (("left",1),("right",-1)):
                        node(body,"geom",name=f"{e.id}/pad-{side}",type="box",size=vec([.02,half_width,.05]),pos=vec([0,sign*pitch,.30]),rgba=".80 .62 .20 1",friction=".35 .005 .0001")
                    node(body,"geom",name=f"{e.id}/mount",type="box",size=vec([.05,sy/2,.12]),pos=".09 0 .30",rgba=".26 .34 .36 1",**common)
            elif e.kind=="stairs":
                n=max(1,math.ceil(sz/e.step_height))
                for k in range(n):
                    h=sz*(k+1)/n
                    node(body,"geom",name=f"{e.id}/step-{k}",type="box",size=vec([sx/2,sy/n/2,h/2]),pos=vec([0,-sy/2+sy/n*(k+.5),h/2]),rgba="0.55 0.57 0.55 1",**common)
            elif e.kind=="ramp":
                # A thin tilted rigid slab; height and slope remain explicit inputs.
                node(body,"geom",name=f"{e.id}/ramp",type="box",size=vec([sx/2,sy/2,.06]),pos=vec([0,0,max(.06,abs(math.sin(e.slope))*sx/2)]),euler=vec([0,-e.slope,0]),rgba="0.55 0.60 0.58 1",**common)
            elif e.kind=="door":
                # Imported drawings identify an aperture, not a door leaf or
                # its mechanism. Use an explicit roll-up simulation default:
                # lifting the leaf clears the whole reviewed opening without
                # pushing it into the adjacent confirmed wall geometry.
                from .door_geometry import door_geometry
                geometry=door_geometry(e,p.environment.id)
                imported=p.environment.id.startswith("floorplan-")
                travel=geometry['travel']
                node(body,"joint",name=f"{e.id}/slide",type="slide",axis=geometry['axis'],range=f"0 {travel}",damping="20")
                # The confirmed wall is cut at the opening boundary. Leave a
                # small leaf-to-jamb clearance so MuJoCo contact friction does
                # not weld the rising panel to those adjacent wall fragments.
                panel_half=[max(.01,sx/2-.04),max(.01,sy/2-.04),sz/2] if imported else [sx/2,sy/2,sz/2]
                node(body,"geom",name=f"{e.id}/panel",type="box",size=vec(panel_half),pos=vec([0,0,sz/2]),mass="20",rgba="0.5 0.6 0.62 0.8",**common)
                node(actuator,"position",name=f"{e.id}/motor",joint=f"{e.id}/slide",kp="1500",kv="100",ctrlrange=f"0 {travel}",forcerange="-500 500")
            elif e.kind=="elevator":
                max_z=max((self.floor_heights[f] for f in e.facility.served_floors),default=z+sz)-z
                node(body,"joint",name=f"{e.id}/lift",type="slide",axis="0 0 1",range=f"0 {max(.1,max_z)}",damping="100")
                node(body,"geom",name=f"{e.id}/platform",type="box",size=vec([sx/2,sy/2,.07]),pos="0 0 -.07",mass="150",rgba="0.37 0.43 0.42 1",**common)
                node(actuator,"position",name=f"{e.id}/motor",joint=f"{e.id}/lift",kp="30000",kv="3500",ctrlrange=f"0 {max(.1,max_z)}",forcerange="-30000 30000")
                node(actuator,"motor",name=f"{e.id}/support",joint=f"{e.id}/lift",gear="1",ctrlrange="-30000 30000",forcerange="-30000 30000")
                for side in (-1,1):
                    node(body,"geom",name=f"{e.id}/wall-{side}",type="box",size=vec([.05,sy/2,1.1]),pos=vec([side*(sx/2+.05),0,1.1]),mass="10",rgba="0.55 0.63 0.64 0.25")
                # Authored sliding car and landing doors. The 2 cm bottom
                # clearance prevents a kinematically constrained panel from
                # binding against a floor slab at floating-point zero gap.
                door_specs=[(f"{e.id}/door",body,[0,-sy/2+.05,0],0.)]
                for floor in (e.facility.served_floors or [e.floor_id]):
                    front=-sy/2-.18
                    door_specs.append((f"{e.id}/landing-{floor}",world,[e.pose.x-math.sin(e.pose.yaw)*front,e.pose.y+math.cos(e.pose.yaw)*front,self.floor_heights[floor]],e.pose.yaw))
                    # Bridge the slab cutout to within 4 mm of the cabin front.
                    # A .12 m unsupported seam can trap a .12 m-radius wheel.
                    # Keep the sill entirely outside the swept cabin platform;
                    # extend through the conservative AABB hole for rotated cars.
                    c,s=abs(math.cos(e.pose.yaw)),abs(math.sin(e.pose.yaw))
                    cut_x=c*(sx+.24)+s*(sy+.24)
                    cut_y=s*(sx+.24)+c*(sy+.24)
                    outer=(s*cut_x+c*cut_y)/2+.004
                    inner=sy/2+.004
                    length=max(.01,outer-inner)
                    sill_y=-(outer+inner)/2
                    sill=node(world,"body",name=f"{e.id}/sill-{floor}",pos=vec([e.pose.x-math.sin(e.pose.yaw)*sill_y,e.pose.y+math.cos(e.pose.yaw)*sill_y,self.floor_heights[floor]]),quat=vec(quat_yaw(e.pose.yaw)))
                    node(sill,"geom",name=f"floor/{floor}/sill-{e.id}",type="box",size=vec([max(.02,sx/2-.05),length/2,.06]),pos="0 0 -.06",rgba=".62 .65 .64 1",**common)
                for prefix,parent,position,yaw in door_specs:
                    panel=node(parent,"body",name=prefix+"-body",pos=vec(position),quat=vec(quat_yaw(yaw)))
                    node(panel,"joint",name=prefix,type="slide",axis="1 0 0",range=f"0 {sx+.1}",damping="12")
                    node(panel,"geom",name=prefix+"-panel",type="box",size=vec([sx/2,.025,1.05]),pos="0 0 1.07",mass="10",rgba=".5 .6 .65 .7")
                    node(actuator,"position",name=prefix+"-motor",joint=prefix,kp="2000",kv="120",ctrlrange=f"0 {sx+.1}",forcerange="-300 300")
            else:
                if e.dynamic:
                    node(body,"freejoint",name=f"{e.id}/free")
                node(body,"geom",name=f"{e.id}/shape",type="box",size=vec([sx/2,sy/2,sz/2]),pos=vec([0,0,sz/2]),mass=e.mass,rgba="0.55 0.59 0.58 1",**common)
        for r in p.robots:
            spec=model_by_id(r.model_id)
            z=self.floor_heights[r.floor_id]+r.pose.z
            if r.model_id=="spot":
                b=copy.deepcopy(spot.find("worldbody/body"))
                for light in list(b.iter("light")):
                    # All source lights are direct body children.
                    if light in list(b): b.remove(light)
                self._prefix(b,r.id)
                b.set("pos",vec([r.pose.x,r.pose.y,z+.6]))
                b.set("quat",vec(quat_yaw(r.pose.yaw)))
                world.append(b)
                self.robot_body_names[r.id]=f"{r.id}/body"
                for a in spot.find("actuator"):
                    c=copy.deepcopy(a); self._prefix(c,r.id); actuator.append(c)
                if spot.find("contact") is not None:
                    for a in spot.find("contact"):
                        c=copy.deepcopy(a); self._prefix(c,r.id); contact.append(c)
                home=spot.find("keyframe/key")
                angles=[float(x) for x in home.get("qpos").split()][7:]
                joints=[j for j in b.iter("joint")]
                for j,angle in zip(joints,angles): self.initial_joints[j.get("name")]=angle
                for i,equipment in enumerate(r.equipment):
                    attached=node(b,"body",name=f"{r.id}/equipment-body-{i}",pos=vec([0,0,.15+equipment.size.z/2]))
                    node(attached,"geom",name=f"{r.id}/equipment-{i}",type="box",size=vec([equipment.size.x/2,equipment.size.y/2,equipment.size.z/2]),mass=equipment.mass,rgba="0.3 0.35 0.36 1")
                if r.payload_mass:
                    payload=node(b,"body",name=f"{r.id}/payload-body",pos="0 0 .25")
                    node(payload,"geom",name=f"{r.id}/initial-payload",type="box",size=".2 .2 .1",mass=r.payload_mass,rgba=".65 .48 .3 1")
            else:
                self._research_robot(world,actuator,r,spec,z)
        for p in self.project.people:
            body=node(world,"body",name=f"{p.id}/body",pos=vec([p.pose.x,p.pose.y,self.floor_heights[p.floor_id]+.85]))
            for axis,vector in (("x","1 0 0"),("y","0 1 0")):
                node(body,"joint",name=f"{p.id}/{axis}",type="slide",axis=vector,damping="5")
                node(actuator,"velocity",name=f"{p.id}/{axis}-motor",joint=f"{p.id}/{axis}",kv="150",forcerange="-150 150")
            node(body,"geom",name=f"{p.id}/torso",type="capsule",size=".22 .6",mass=p.mass,rgba="0.70 0.43 0.34 1")
        for item in self.project.items:
            b=node(world,"body",name=f"{item.id}/body",pos=vec([item.pose.x,item.pose.y,self.floor_heights[item.floor_id]+item.pose.z+item.size.z/2]),quat=vec(quat_yaw(item.pose.yaw)))
            node(b,"freejoint",name=f"{item.id}/free")
            node(b,"geom",name=f"{item.id}/shape",type="box",size=vec([item.size.x/2,item.size.y/2,item.size.z/2]),mass=item.mass,friction=f"{item.friction} .01 .001",rgba="0.68 0.49 0.27 1")
        return ET.tostring(root,encoding="unicode")

    @staticmethod
    def _prefix(element,prefix):
        for e in element.iter():
            for attr in ("name","joint","body1","body2","site","target"):
                if attr in e.attrib: e.set(attr,prefix+"/"+e.get(attr))

    def _research_robot(self,world,actuator,r,spec,z):
        sx,sy=spec["size"]["x"],spec["size"]["y"]
        mobile=spec["locomotion"]!="fixed"
        body=node(world,"body",name=f"{r.id}/body",pos=vec([r.pose.x,r.pose.y,z+(.30 if mobile else 0)]),quat=vec(quat_yaw(r.pose.yaw)))
        self.robot_body_names[r.id]=f"{r.id}/body"
        if mobile: node(body,"freejoint",name=f"{r.id}/free")
        arm_mass=8.5 if r.model_id in ("arm","mobile_manipulator") else 0.
        wheel_mass=spec["mass"]*.26 if mobile else 0.
        cargo_mass=spec["mass"]*.09 if r.model_id=="delivery" else 0.
        contact_mass=.10 if mobile else 0.
        chassis_mass=spec["mass"]-arm_mass-wheel_mass-cargo_mass-contact_mass
        node(body,"geom",name=f"{r.id}/chassis",type="box",size=vec([sx/2,sy/2,.1]),pos=vec([0,0,0 if mobile else .15]),mass=chassis_mass,rgba="0.31 0.44 0.47 1")
        if mobile:
            # Two 50 g sprung pads are included in, rather than added to, the
            # authored catalog mass. Their travel is entirely joint dynamics.
            for side,sign in (("left",1),("right",-1)):
                pad=node(body,"body",name=f"{r.id}/charge-{side}-body",pos=vec([sx/2+.045,sign*sy*.28,0]))
                node(pad,"joint",name=f"{r.id}/charge-{side}-spring",type="slide",axis="1 0 0",range="-.03 0",stiffness="600",springref="0",damping="4",armature=".001")
                node(pad,"geom",name=f"{r.id}/charge-{side}",type="box",size=".012 .025 .03",mass=".05",friction=".35 .005 .0001",rgba=".82 .65 .21 1")
            for side,sign in (("left",1),("right",-1)):
                wheel=node(body,"body",name=f"{r.id}/{side}-wheel",pos=vec([0,sign*(sy/2+.025),-.18]))
                node(wheel,"joint",name=f"{r.id}/{side}",axis="0 1 0",damping=".1")
                node(wheel,"geom",name=f"{r.id}/{side}-tire",type="cylinder",size=".12 .035",euler="1.57079632679 0 0",mass=spec["mass"]*.10,friction="1 .005 .0001",rgba="0.12 0.16 0.17 1")
                node(actuator,"velocity",name=f"{r.id}/{side}-motor",joint=f"{r.id}/{side}",kv="40",ctrlrange="-15 15",forcerange="-25 25")
            for sign in (-1,1):
                caster=node(body,"body",name=f"{r.id}/caster-body-{sign}",pos=vec([sign*(sx/2-.07),0,-.23]))
                node(caster,"joint",name=f"{r.id}/caster-ball-{sign}",type="ball",damping=".002",armature=".001")
                node(caster,"geom",name=f"{r.id}/caster-{sign}",type="sphere",size=".07",mass=spec["mass"]*.03,friction=".8 .005 .0001",rgba="0.2 0.2 0.2 1")
            if r.model_id=="delivery":
                node(body,"geom",name=f"{r.id}/cargo-box",type="box",size=vec([sx*.4,sy*.4,.17]),pos="0 0 .27",mass=spec["mass"]*.09,rgba="0.76 0.77 0.68 1")
            if r.payload_mass:
                node(body,"geom",name=f"{r.id}/initial-payload",type="box",size=".18 .18 .1",pos="0 0 .3",mass=r.payload_mass,rgba=".65 .48 .30 1")
        if r.model_id in ("arm","mobile_manipulator"):
            previous=node(body,"body",name=f"{r.id}/arm-base",pos=vec([0,0,.18 if mobile else .3]))
            lengths=[.15,.4,.35,.16]
            for i,length in enumerate(lengths):
                part=node(previous,"body",name=f"{r.id}/link-{i}",pos=vec([0,0,0 if i==0 else lengths[i-1]]))
                node(part,"joint",name=f"{r.id}/arm-{i}",axis="0 0 1" if i==0 else "0 1 0",range="-2.8 2.8",damping="2")
                node(part,"geom",name=f"{r.id}/arm-link-{i}",type="capsule",fromto=vec([0,0,0,0,0,length]),size=".045",mass="2",rgba="0.79 0.62 0.27 1")
                node(actuator,"position",name=f"{r.id}/arm-motor-{i}",joint=f"{r.id}/arm-{i}",kp="300",kv="30",ctrlrange="-2.8 2.8",forcerange="-80 80")
                previous=part
            gripper=node(previous,"body",name=f"{r.id}/gripper",pos="0 0 .16")
            node(gripper,"geom",name=f"{r.id}/palm",type="box",size=".05 .07 .025",mass=".3",rgba=".2 .25 .25 1")
            for side,sign in (("left",1),("right",-1)):
                finger=node(gripper,"body",name=f"{r.id}/finger-{side}",pos=vec([0,sign*.03,.06]))
                node(finger,"joint",name=f"{r.id}/grip-{side}",type="slide",axis=vec([0,sign,0]),range="0 .10",damping="1")
                node(finger,"geom",name=f"{r.id}/finger-shape-{side}",type="box",size=".04 .012 .07",mass=".1",friction="1.2 .01 .001",rgba=".2 .25 .25 1")
                node(actuator,"position",name=f"{r.id}/grip-motor-{side}",joint=f"{r.id}/grip-{side}",kp=r.gripper_kp,kv="10",ctrlrange="0 .10",forcerange="-30 30")
        for i,e in enumerate(r.equipment):
            node(body,"geom",name=f"{r.id}/equipment-{i}",type="box",size=vec([e.size.x/2,e.size.y/2,e.size.z/2]),pos=vec([0,0,.2+e.size.z/2]),mass=e.mass,rgba=".4 .45 .4 1")

    def command(self,robot_id,v=0.,w=0.,mode="stand"):
        if robot_id not in self.commands: raise ValueError("없는 로봇")
        self.commands[robot_id]=dict(v=float(v),w=float(w),mode=mode)
        if mode=="stop" and robot_id in self.arm_controllers and self.arm_controllers[robot_id].target is not None:
            self.arm_controllers[robot_id].hold(self.data)

    def support_geometry(self,robot_id):
        """Static authored body-frame support, never an observed load claim."""
        robot=next(r for r in self.project.robots if r.id==robot_id)
        if robot.model_id not in ('amr','delivery','agv','logistics'):
            raise ValueError('이 로봇의 검증 대상 적재 지지면 계약이 없습니다')
        trays=[(i,e) for i,e in enumerate(robot.equipment) if e.kind=='cargo_tray']
        if len(trays)>1:raise ValueError('복수 지지면 선택 계약이 필요합니다')
        name=f'{robot_id}/equipment-{trays[0][0]}' if trays else f'{robot_id}/chassis'
        geom=self.model.geom(name)
        if int(geom.bodyid[0])!=self.robot_bodies[robot_id]:raise ValueError('지지면이 몸체에 고정되지 않았습니다')
        position=geom.pos.copy();position[2]+=geom.size[2]
        capacity=min(model_by_id(robot.model_id)['max_payload'],trays[0][1].capacity if trays else 3.)
        return dict(support_geom=name,support_size=(geom.size[:2]*2).tolist(),support_top_offset=position.tolist(),max_payload=capacity)

    def docking_geometry(self,robot_id,station_id):
        """Authored front-contact targets in the observed robot body frame.

        Target requests 15 mm spring compression; staging is one metre behind.
        Neither this geometry nor proximity is evidence of electrical contact.
        """
        if robot_id not in self._charging_robots:
            raise ValueError("검증 대상 충전 접점 모델이 없는 로봇입니다")
        e=self._chargers[station_id]
        robot=self._charging_robots[robot_id]
        length=model_by_id(robot.model_id)["size"]["x"]
        x=-length/2-.062
        c,s=math.cos(e.pose.yaw),math.sin(e.pose.yaw)
        def pose(local_x):
            return dict(x=e.pose.x+c*local_x,y=e.pose.y+s*local_x,z=self.floor_heights[e.floor_id]+e.pose.z+.30,yaw=e.pose.yaw)
        return dict(staging=pose(x-1.),target=pose(x),station_local_bounds=dict(min=[-.02,-e.size.y/2,.18],max=[.14,e.size.y/2,.42]))

    def charger_observations(self,time=None):
        """Ideal physical contact sensors, not electrical/charging success.

        Matching left/left and right/right geom pairs are accumulated separately.
        Wrong-side contacts, a nearby chassis, or an unsupported robot model
        cannot assert a connected pair. All forces come from mj_contactForce.
        """
        sampled_at=float(self.data.time if time is None else time)
        rows={eid:dict(sampled_at=sampled_at,fault=e.facility.fault,contacts={},sensor_model="ideal_dual_pad_contact_force_alignment_relative_velocity") for eid,e in self._chargers.items()}
        for eid,e in self._chargers.items():
            sid=self.model.body(eid+"/body").id
            rotation=self.data.xmat[sid].reshape(3,3)
            station_velocity=np.zeros(6)
            mujoco.mj_objectVelocity(self.model,self.data,mujoco.mjtObj.mjOBJ_BODY,sid,station_velocity,0)
            for rid,r in self._charging_robots.items():
                bid=self.robot_bodies[rid]
                local=rotation.T@(self.data.xpos[bid]-self.data.xpos[sid])
                yaw_error=(yaw_of(self.data.xquat[bid])-e.pose.yaw+math.pi)%(2*math.pi)-math.pi
                speeds=[]
                for side in ("left","right"):
                    pad=self.model.body(f"{rid}/charge-{side}-body").id
                    velocity=np.zeros(6)
                    mujoco.mj_objectVelocity(self.model,self.data,mujoco.mjtObj.mjOBJ_BODY,pad,velocity,0)
                    speeds.append(float(np.linalg.norm(velocity[3:]-station_velocity[3:])))
                rows[eid]["contacts"][rid]=dict(left=False,right=False,normal_force=0.,left_force=0.,right_force=0.,
                    aligned=bool(abs(local[1])<=.035 and abs(local[2]-.30)<=.035 and abs(yaw_error)<=.08 and self.data.xmat[bid][8]>.98),
                    relative_speed=max(speeds),contact_pairs=[])
        for index in range(self.data.ncon):
            contact=self.data.contact[index]
            g1,g2=int(contact.geom1),int(contact.geom2)
            if g1 in self._robot_charge_pads and g2 in self._station_charge_pads:rg,sg=g1,g2
            elif g2 in self._robot_charge_pads and g1 in self._station_charge_pads:rg,sg=g2,g1
            else:continue
            rid,robot_side=self._robot_charge_pads[rg]
            eid,station_side=self._station_charge_pads[sg]
            wrench=np.zeros(6)
            mujoco.mj_contactForce(self.model,self.data,index,wrench)
            normal=max(0.,float(wrench[0]))
            reading=rows[eid]["contacts"][rid]
            reading["contact_pairs"].append(dict(robot_geom=self.model.geom(rg).name,station_geom=self.model.geom(sg).name,robot_side=robot_side,station_side=station_side,normal_force=normal,position=contact.pos.tolist(),distance=float(contact.dist)))
            if robot_side==station_side:reading[robot_side+"_force"]+=normal
        for row in rows.values():
            for reading in row["contacts"].values():
                reading["left"]=reading["left_force"]>=.2
                reading["right"]=reading["right_force"]>=.2
                reading["normal_force"]=reading["left_force"]+reading["right_force"]
        return rows

    @staticmethod
    def _door_names(element):
        return [f"{element.id}/door"]+[f"{element.id}/landing-{floor}" for floor in (element.facility.served_floors or [element.floor_id])]

    def facility_command(self,elevator_id,command):
        """Receive actuator intentions. This method never changes body poses."""
        e=self._facilities[elevator_id]
        values={key:float(command[key]) for key in ("lift_target","door_target","max_speed","door_duration")}
        if not all(math.isfinite(v) for v in values.values()) or values["max_speed"]<=0 or values["door_duration"]<=0:
            raise ValueError("승강기 명령 값이 잘못되었습니다")
        joint=self.model.joint(elevator_id+"/lift")
        lo,hi=self.model.jnt_range[joint.id]
        values["lift_target"]=float(np.clip(values["lift_target"],lo,hi))
        values["door_target"]=float(np.clip(values["door_target"],0,1))
        values["max_speed"]=min(values["max_speed"],e.facility.speed)
        values["hold"]=bool(command.get("hold",False))
        self._facility_commands[elevator_id]=values

    def command_facility(self,elevator_id,**command):
        """Keyword-form adapter matching the runtime robot command interface."""
        self.facility_command(elevator_id,command)

    def _cabin_entities(self,e):
        """Ideal volume detector and model-mass inventory, not a load-cell model."""
        cabin=self.model.body(e.id+"/body").id
        origin=self.data.xpos[cabin]
        rotation=self.data.xmat[cabin].reshape(3,3)
        entities=[]
        candidates=[(r.id,"robot") for r in self.project.robots]+[(p.id,"person") for p in self.project.people]+[(i.id,"item") for i in self.project.items]+[(x.id,"obstacle") for x in self.project.environment.elements if x.dynamic and x.id!=e.id]
        for eid,kind in candidates:
            bid=self.model.body(eid+"/body").id
            local=rotation.T@(self.data.xpos[bid]-origin)
            if abs(local[0])<e.size.x/2 and abs(local[1])<e.size.y/2 and -.1<local[2]<2.2:
                entities.append((eid,kind,float(self.model.body_subtreemass[bid])))
        return entities

    def facility_observations(self,time=None):
        """Explicit ideal facility sensors; callers apply delay/dropout separately.

        Occupancy comes from physical body centres inside the cabin volume;
        reservations are never consulted. Items contribute load but not passenger
        count. Door obstruction uses actual collision forces, not a timer.
        """
        sampled_at=float(self.data.time if time is None else time)
        contacts=self.contacts() if self._facilities else []
        rows={}
        for eid,e in self._facilities.items():
            joint=self.model.joint(eid+"/lift")
            position=float(self.data.qpos[joint.qposadr[0]])
            velocity=float(self.data.qvel[joint.dofadr[0]])
            fractions={name:float(np.clip(self.data.qpos[self.model.joint(name).qposadr[0]]/(e.size.x+.1),0,1)) for name in self._door_names(e)}
            cabin_z=self.floor_heights[e.floor_id]+e.pose.z+position
            landing=next((floor for floor in (e.facility.served_floors or [e.floor_id]) if abs(cabin_z-self.floor_heights[floor])<=.025),None)
            fraction=fractions[eid+"/door"]
            if landing is not None:fraction=min(fraction,fractions[f"{eid}/landing-{landing}"])
            door_geoms={name+"-panel" for name in self._door_names(e)}
            blocked=any(c["force"]>1. and ((c["geom_a"] in door_geoms and c["b"]!="floor") or (c["geom_b"] in door_geoms and c["a"]!="floor")) for c in contacts)
            entities=self._cabin_entities(e)
            rows[eid]=dict(sampled_at=sampled_at,position=position,velocity=velocity,door_fraction=fraction,door_blocked=blocked,
                           occupants=sorted(key for key,kind,_ in entities if kind in ("robot","person")),load_kg=sum(mass for _,_,mass in entities),
                           fault=e.facility.fault,landing_floor=landing,door_fractions=fractions,sensor_model="ideal_joint_encoders_contact_switch_volume_occupancy_model_mass_inventory")
        return rows

    def _update_facilities(self,dt):
        for eid,e in self._facilities.items():
            command=self._facility_commands[eid]
            reference=self._facility_references[eid]
            joint=self.model.joint(eid+"/lift")
            position=float(self.data.qpos[joint.qposadr[0]])
            target=position if e.facility.fault or not e.facility.automatic else command["lift_target"]
            delta=command["max_speed"]*dt
            reference["lift"]+=float(np.clip(target-reference["lift"],-delta,delta))
            self.data.ctrl[self.model.actuator(eid+"/motor").id]=reference["lift"]
            cabin=self.model.body(eid+"/body").id
            load=sum(mass for _,_,mass in self._cabin_entities(e))
            self.data.ctrl[self.model.actuator(eid+"/support").id]=(float(self.model.body_subtreemass[cabin])+load)*abs(float(self.model.opt.gravity[2]))
            cabin_z=self.floor_heights[e.floor_id]+e.pose.z+position
            for name in self._door_names(e):
                landing_open=name==eid+"/door" or any(name==f"{eid}/landing-{floor}" and abs(cabin_z-self.floor_heights[floor])<=.025 for floor in (e.facility.served_floors or [e.floor_id]))
                target=command["door_target"]*(e.size.x+.1) if landing_open else 0.
                delta=(e.size.x+.1)/command["door_duration"]*dt
                reference["doors"][name]+=float(np.clip(target-reference["doors"][name],-delta,delta))
                self.data.ctrl[self.model.actuator(name+"-motor").id]=reference["doors"][name]
    def set_power(self,robot_id,powered):
        """Local actuator power state; loss removes drive force, not momentum."""
        if not hasattr(self,"powered"):self.powered={r.id:r.battery>0 for r in self.project.robots}
        self.powered[robot_id]=bool(powered)
        if not powered:self.command(robot_id,mode="stop")

    def step(self):
        dt=self.model.opt.timestep
        if self._control_elapsed+1e-12>=1/self.project.physics.control_hz:
            elapsed=self._control_elapsed
            self._control_elapsed=0.
            for r in self.project.robots:
                if not getattr(self,"powered",{}).get(r.id,r.battery>0):continue
                cmd=self.commands[r.id]
                if r.id in self.controllers:
                    self.controllers[r.id].update(self.data,vx=cmd["v"],vy=0,yaw_rate=cmd["w"],mode=cmd["mode"],dt=elapsed)
                elif r.model_id!="arm":
                    track=model_by_id(r.model_id)["size"]["y"]+.05
                    for side,sign in (("left",-1),("right",1)):
                        self.data.ctrl[self.model.actuator(f"{r.id}/{side}-motor").id]=(cmd["v"]+sign*cmd["w"]*track/2)/.12
                if r.id in self.arm_controllers:
                    try:
                        self.arm_controllers[r.id].update(self.data,dt=elapsed)
                        self.controller_errors.pop(r.id,None)
                    except ValueError as error:
                        self.controller_errors[r.id]=str(error)
            for r in self.project.robots:
                disabled=r.fault=="motor" or not getattr(self,"powered",{}).get(r.id,r.battery>0)
                for a in self._actuators[r.id]:
                    self.model.actuator_gainprm[a]=0 if disabled else self._gains[a]
                    self.model.actuator_biasprm[a]=0 if disabled else self._biases[a]
        self._update_facilities(dt)
        mujoco.mj_step(self.model,self.data)
        self._control_elapsed+=dt

    def truth(self,robot_id):
        b=self.robot_bodies[robot_id]
        pos=self.data.xpos[b]; q=self.data.xquat[b]
        vel=np.zeros(6)
        mujoco.mj_objectVelocity(self.model,self.data,mujoco.mjtObj.mjOBJ_BODY,b,vel,0)
        joints={name:float(self.data.qpos[address]) for name,address in self._joint_observations[robot_id]}
        return dict(pose=dict(x=float(pos[0]),y=float(pos[1]),z=float(pos[2]),yaw=yaw_of(q)),quaternion=q.tolist(),velocity=vel[3:].tolist(),angular_velocity=vel[:3].tolist(),upright=float(self.data.xmat[b][8]),joints=joints)

    def entity_for_geom(self,gid):
        if hasattr(self,'_geom_entity_ids'):return self._geom_entity_ids[gid]
        name=self.model.geom(gid).name or ""
        if name.startswith("floor/"): return "floor"
        bid=self.model.geom_bodyid[gid]
        while bid:
            entity=(self.model.body(bid).name or "").split("/")[0]
            if entity in self.entity_types:return entity
            bid=self.model.body_parentid[bid]
        return name.split("/")[0]

    def contacts(self):
        rows=[]
        for i in range(self.data.ncon):
            c=self.data.contact[i]
            a,b=self.entity_for_geom(c.geom1),self.entity_for_geom(c.geom2)
            if a==b: continue
            force=np.zeros(6); mujoco.mj_contactForce(self.model,self.data,i,force)
            # Contact frame axes are rows, normal points geom1 -> geom2.
            # mj_contactForce is the wrench on geom2 in that contact frame.
            force_on_b=c.frame.reshape(3,3).T@force[:3]
            rows.append(dict(a=a,b=b,geom_a=self.model.geom(c.geom1).name,geom_b=self.model.geom(c.geom2).name,position=c.pos.tolist(),force=float(np.linalg.norm(force[:3])),force_on_b_world=force_on_b.tolist(),impulse=float(np.linalg.norm(force[:3])*self.model.opt.timestep),distance=float(c.dist)))
        return rows

    def geometries(self):
        rows=[]
        for gid in range(self.model.ngeom):
            if self.model.geom_group[gid]==3:continue
            matrix=self.data.geom_xmat[gid]; q=np.empty(4);mujoco.mju_mat2Quat(q,matrix)
            name=self.model.geom(gid).name or f"geom-{gid}"
            material=int(self.model.geom_matid[gid])
            rgba=self.model.mat_rgba[material] if material>=0 else self.model.geom_rgba[gid]
            rows.append(dict(id=gid,name=name,entity_id=self.entity_for_geom(gid),type=GEOM_TYPES[int(self.model.geom_type[gid])],size=self.model.geom_size[gid].tolist(),position=self.data.geom_xpos[gid].tolist(),quaternion=q.tolist(),rgba=rgba.tolist(),mesh_id=int(self.model.geom_dataid[gid]) if int(self.model.geom_type[gid])==int(mujoco.mjtGeom.mjGEOM_MESH) else None))
        return rows

    def meshes(self):
        rows=[]
        for i in range(self.model.nmesh):
            v,n=self.model.mesh_vertadr[i],self.model.mesh_vertnum[i]
            f,m=self.model.mesh_faceadr[i],self.model.mesh_facenum[i]
            rows.append(dict(id=i,vertices=self.model.mesh_vert[v:v+n].flatten().tolist(),faces=self.model.mesh_face[f:f+m].flatten().tolist()))
        return rows

    def range_scan(self,robot_id,beams=24,max_range=10.):
        """Research planar lidar. Rays query collision geometry in the actual scene."""
        bid=self.robot_bodies[robot_id]
        rotation=self.data.xmat[bid].reshape(3,3)
        origin=self.data.xpos[bid]+rotation@np.array([.15,0,.4])
        mask=np.array([1,1,0,1,1,1],dtype=np.uint8)
        angles=np.linspace(-math.pi,math.pi,beams,endpoint=False)
        distances=[]
        for angle in angles:
            direction=rotation@np.array([math.cos(angle),math.sin(angle),0.])
            start=origin.copy();travelled=0.;hit=np.array([-1],dtype=np.int32)
            distance=max_range
            for _ in range(30):
                length=mujoco.mj_ray(self.model,self.data,start,direction,mask,1,-1,hit)
                if length<0 or travelled+length>max_range:break
                if self.entity_for_geom(int(hit[0]))!=robot_id:
                    distance=travelled+float(length);break
                travelled+=float(length)+.002
                start=origin+direction*travelled
            distances.append(distance)
        return dict(angles=angles.tolist(),ranges=distances,max_range=max_range,frame="robot_sensor",mount_position=[.15,0,.4],model="planar geometric rays; no material reflectance")

    def tracked_people(self,robot_id,max_range=6.):
        """Simplified visible-person sensor, using real geometry for occlusion.

        This is not camera recognition. Runtime sends it through the robot's
        observation bus (sampling, noise, dropout and delivery delay).
        """
        bid=self.robot_bodies[robot_id]
        origin=self.data.xpos[bid]+self.data.xmat[bid].reshape(3,3)@np.array([0,0,.4])
        mask=np.array([1,1,0,1,1,1],dtype=np.uint8);rows=[]
        robot_z=self.data.xpos[bid][2]
        floor_id=min(self.floor_heights,key=lambda key:abs(self.floor_heights[key]+.35-robot_z))
        for person in self.project.people:
            if person.floor_id!=floor_id:continue
            body=self.model.body(person.id+'/body').id;position=self.data.xpos[body]
            delta=position-origin;length=float(np.linalg.norm(delta))
            if length>max_range or length<1e-6:continue
            direction=delta/length;start=origin.copy();travelled=0.;visible=False
            hit=np.array([-1],dtype=np.int32)
            for _ in range(60):
                distance=mujoco.mj_ray(self.model,self.data,start,direction,mask,1,-1,hit)
                if distance<0:break
                entity=self.entity_for_geom(int(hit[0]))
                if entity==person.id:visible=True;break
                if entity!=robot_id:break
                travelled+=float(distance)+.002
                start=origin+direction*travelled
                if travelled>length:break
            if visible:
                velocity=np.zeros(6);mujoco.mj_objectVelocity(self.model,self.data,mujoco.mjtObj.mjOBJ_BODY,body,velocity,0)
                rows.append(dict(id=person.id,position=position.tolist(),velocity=velocity[3:].tolist(),
                                 radius=.22,floor_id=person.floor_id))
        return rows

    def tracked_items(self,robot_id,max_range=3.):
        """Explicit ideal fiducial tracker; known item tags, range and occlusion gate."""
        b=self.robot_bodies[robot_id]
        origin=self.data.xpos[b]+self.data.xmat[b].reshape(3,3)@np.array([0,0,.45])
        mask=np.array([1,1,0,1,1,1],dtype=np.uint8)
        rows=[]
        for item in self.project.items:
            body=self.model.body(item.id+"/body").id
            position=self.data.xpos[body]
            delta=position-origin;length=float(np.linalg.norm(delta))
            if length>max_range or length<1e-6:continue
            direction=delta/length;start=origin.copy();travelled=0.;visible=False
            hit=np.array([-1],dtype=np.int32)
            for _ in range(30):
                distance=mujoco.mj_ray(self.model,self.data,start,direction,mask,1,-1,hit)
                if distance<0:break
                entity=self.entity_for_geom(int(hit[0]))
                if entity==item.id:visible=True;break
                if entity!=robot_id:break
                travelled+=float(distance)+.002
                start=origin+direction*travelled
                if travelled>length:break
            if visible:
                velocity=np.zeros(6);mujoco.mj_objectVelocity(self.model,self.data,mujoco.mjtObj.mjOBJ_BODY,body,velocity,0)
                rows.append(dict(id=item.id,position=position.tolist(),velocity=velocity[3:].tolist(),
                    quaternion=self.data.xquat[body].tolist(),angular_velocity=velocity[:3].tolist(),
                    orientation_sensor_model="ideal_visible_tag_orientation",orientation_noise_std_rad=0.,
                    sensor_model="ideal_tag_tracker",max_range=max_range))
        return rows
