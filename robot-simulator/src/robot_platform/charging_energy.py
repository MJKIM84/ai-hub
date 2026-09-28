"""Configured charging queue estimates; observations and static routes only.

These are scheduling estimates, not measured watts or deadline guarantees. The
simulator's 20 W electronics demand is explicit; motor/traffic/fault variation
can increase real consumption and delay. No estimate grants a connector.
"""
from copy import deepcopy
import math

from .motion_limits import route_timing, translation_time

VERSION = 'observed-charging-energy-1'
IDLE_POWER_W = 20.
RESERVE_SECONDS = 5.


def distance(a,b):
    return math.hypot(b['x']-a['x'],b['y']-a['y'])


def travel(robot, policy, start, path, final_yaw=None, environment=None, floor_id=None, *, preserve_corners=False):
    """Static approach/clearance timing with the existing one-second allowance."""
    # Validate the original path before removing reached points. Otherwise a
    # malformed near-zero point (for example a boolean coordinate) could vanish
    # before the shared timing helper returns its fail-closed unknown result.
    timing = route_timing(robot, policy, environment, start, path, floor_id,
                          final_yaw=final_yaw, cap=.3)
    if not timing['known']:
        return dict(timing, energy_j=None)
    # The controller discards already reached leading waypoints before choosing
    # a direction. Sensor jitter at staging is not an out-and-back turn. Keep
    # generic route_timing's exact positive-leg contract unchanged.
    remaining = list(path)
    while remaining and distance(start, remaining[0]) < .08 and (not preserve_corners or len(remaining)==1):
        remaining.pop(0)
    if len(remaining) != len(path):
        timing = route_timing(robot, policy, environment, start, remaining, floor_id,
                              final_yaw=final_yaw, cap=.3)
        if not timing['known']:
            return dict(timing, energy_j=None)
    allowance = 1. if timing['distance_m'] > .08 else 0.
    seconds = timing['seconds'] + allowance
    energy = seconds * robot.estimated_drive_power_w
    if not math.isfinite(seconds) or not math.isfinite(energy):
        return dict(timing, known=False, reason='nonfinite_travel_energy', seconds=None, energy_j=None)
    return dict(timing, arrival_allowance_seconds=allowance, seconds=seconds, energy_j=energy)


class ChargingEnergy:
    def __init__(self,control):self.control=control

    def handoff_estimate(self,robot):
        """Known stop protocol stages, not a bounded worst-case queue promise."""
        physics=self.control.project.physics
        dwell=self.control.manager.confirmation_time
        robot_confirmation=math.ceil(dwell*robot.sensors.rate_hz-1e-12)/robot.sensors.rate_hz
        station_confirmation=math.ceil(dwell*physics.control_hz-1e-12)/physics.control_hz
        stages=dict(command_dispatch_seconds=1/physics.orchestration_hz,
                    stop_communication_seconds=robot.sensors.communication_delay,
                    first_robot_sample_seconds=1/robot.sensors.rate_hz,
                    observation_delivery_seconds=robot.sensors.observation_delay+robot.sensors.communication_delay,
                    manager_update_seconds=1/physics.control_hz,
                    confirmation_seconds=max(robot_confirmation,station_confirmation))
        return dict(stages,seconds=sum(stages.values()),
                    basis='Configured cadence and normal delay estimate for delivered stop plus fresh confirmation; excludes unbounded dropout, traffic, faults and scheduling variation')

    def own_approach(self, robot, observation, path, geometry, floor_id=None):
        c = self.control
        floor = floor_id or c.owner._floor(observation['pose']['z'])
        route = travel(robot, c.owner.policy, observation['pose'], path,
                       geometry['staging']['yaw'], c.project.environment, floor, preserve_corners=True)
        dock = translation_time(robot, c.owner.policy, c.project.environment,
                                geometry['staging'], [geometry['target']], floor, cap=.06)
        if not route['known'] or not dock['known']:
            failed = route if not route['known'] else dock
            return dict(known=False, reason=failed['reason'], approach_time=route, dock_time=dock,
                        approach_seconds=None, dock_seconds=None, approach_energy_j=None,
                        dock_energy_j=None, estimated_drive_j=None)
        latency = robot.sensors.observation_delay + robot.sensors.communication_delay + 1 / robot.sensors.rate_hz
        dock_seconds = dock['seconds'] + c.manager.confirmation_time + 2 * latency
        dock_j = dock_seconds * robot.estimated_drive_power_w
        total_j = route['energy_j'] + dock_j
        if not all(math.isfinite(value) for value in (dock_seconds, dock_j, total_j)):
            return dict(known=False, reason='nonfinite_approach_energy', approach_time=route, dock_time=dock,
                        approach_seconds=None, dock_seconds=None, approach_energy_j=None,
                        dock_energy_j=None, estimated_drive_j=None)
        return dict(known=True, reason=None, route_distance_m=route['distance_m'],
                    dock_distance_m=dock['distance_m'], approach_time=route, dock_time=dock,
                    approach_seconds=route['seconds'], dock_seconds=dock_seconds,
                    approach_energy_j=route['energy_j'], dock_energy_j=dock_j,
                    estimated_drive_j=total_j)

    def _service(self,rid,eid,phase,wait_seconds,now):
        c=self.control;owner=c.owner;robot=owner.robots[rid]
        obs=c.energy_observations.get(rid)
        if obs is None:return None,c.energy_observation_errors.get(rid,'missing_robot_observation')
        if obs['fault']!='none' or obs['battery']<=0 or obs.get('upright',0)<.45:return None,'predecessor_not_operational'
        state=owner.robot_states[rid];plan=c.plans.get(rid,{})
        if state['operator_hold'] or plan.get('interrupted') or phase=='fault':return None,'predecessor_requires_explicit_recovery'
        station=c.manager.stations[eid]
        request=next((req for req in [station.active,*station.queue]
                      if req is not None and req.robot_id==rid and req.station_id==eid),None)
        if request is None:
            planned=c.manager.requests.get(plan.get('request_id'))
            if planned is not None and planned.robot_id==rid and planned.station_id==eid:
                request=planned
        target_percent=request.target_percent if request is not None else owner.policy.charge_until
        geometry=c.geometry.get((rid,eid))
        if geometry is None:return None,'missing_predecessor_geometry'
        floor=owner._floor(obs['pose']['z']);staging=geometry['staging'];target=geometry['target']
        if phase=='clearing':
            parking=plan.get('parking')
            if parking is None:return None,'missing_clearance_target'
            path=c._exit_route(robot,obs,parking,floor,now,plan,live=False)
            if path is None:return None,'clearance_route_unavailable'
            clear=travel(robot,owner.policy,obs['pose'],path,parking['yaw'],c.project.environment,floor,preserve_corners=True)
            if not clear['known']:return None,clear['reason']
            return dict(robot_id=rid,phase=phase,robot_sampled_at=obs['sampled_at'],target_percent=target_percent,approach_seconds=0.,dock_seconds=0.,charge_seconds=0.,undock_seconds=0.,clearance_seconds=clear['seconds']+.3,handoff_seconds=0.,seconds=clear['seconds']+.3),None
        active=c.manager.stations[eid].active
        if active and active.robot_id==rid and active.handoff_pending:return None,'predecessor_stop_confirmation_pending'
        if phase not in ('queued','approach','dock','charging','undock'):return None,'unknown_predecessor_phase'
        approach_seconds=dock_seconds=precharge_j=0.
        if phase in ('queued','approach'):
            path,traffic_reason=c.traffic.route(robot,obs,staging,floor,eid,now,planning=True)
            if path is None:return None,traffic_reason or 'predecessor_approach_unavailable'
            own=self.own_approach(robot,obs,path,geometry,floor)
            if not own['known']:return None,own['reason']
            approach_seconds=own['approach_seconds'];dock_seconds=own['dock_seconds'];precharge_j=own['estimated_drive_j']
        elif phase=='dock':
            dock=translation_time(robot,owner.policy,c.project.environment,obs['pose'],[target],floor,cap=.06)
            if not dock['known']:return None,dock['reason']
            dock_seconds=dock['seconds']+c.manager.confirmation_time+2*(robot.sensors.observation_delay+robot.sensors.communication_delay+1/robot.sensors.rate_hz)
            precharge_j=dock_seconds*robot.estimated_drive_power_w
        element=c.manager.elements[eid]
        # Use declared total-drive demand as a seating allowance. It remains an
        # estimate, not a sensor measurement or upper bound on arbitrary loads.
        net=element.facility.charge_power_w*element.facility.charge_efficiency-robot.estimated_drive_power_w
        if net<=0 and phase!='undock':return None,'nonpositive_estimated_net_charge_power'
        capacity_j=robot.battery_capacity_wh*3600
        if not math.isfinite(capacity_j) or capacity_j<=0:return None,'nonfinite_battery_capacity'
        energy_at_contact=obs['battery']/100*capacity_j-precharge_j-wait_seconds*IDLE_POWER_W
        if not math.isfinite(energy_at_contact):return None,'nonfinite_precharge_energy'
        if energy_at_contact<0 and phase in ('queued','approach','dock'):return None,'predecessor_energy_shortfall'
        charge_seconds=0. if phase=='undock' else max(0.,target_percent/100*capacity_j-energy_at_contact)/net
        undock_start=obs['pose'] if phase=='undock' else target
        undock=translation_time(robot,owner.policy,c.project.environment,undock_start,[staging],floor,cap=.12)
        if not undock['known']:return None,undock['reason']
        undock_seconds=undock['seconds']+1.+c.manager.confirmation_time
        exit_plan=dict(plan,geometry=geometry,origin=plan.get('origin',obs['pose']))
        parking=c._parking(rid,{'pose':staging},exit_plan,now,consider_occupancy=False)
        if parking is None:return None,'predecessor_clearance_unavailable'
        path=c._exit_route(robot,{'pose':staging},parking,floor,now,exit_plan,live=False)
        if path is None:return None,'predecessor_clearance_unavailable'
        clear=travel(robot,owner.policy,staging,path,parking['yaw'],c.project.environment,floor,preserve_corners=True)
        if not clear['known']:return None,clear['reason']
        handoff=self.handoff_estimate(robot)
        row=dict(robot_id=rid,phase=phase,robot_sampled_at=obs['sampled_at'],target_percent=target_percent,approach_seconds=approach_seconds,dock_seconds=dock_seconds,charge_seconds=charge_seconds,undock_seconds=undock_seconds,handoff_seconds=handoff['seconds'],handoff_estimate=handoff,clearance_seconds=clear['seconds']+.3,estimated_net_charge_power_w=net,undock_time=undock,clearance_time=clear)
        row['seconds']=sum(row[key]for key in ('approach_seconds','dock_seconds','charge_seconds','undock_seconds','handoff_seconds','clearance_seconds'))
        if not math.isfinite(row['seconds']) or not math.isfinite(net):return None,'nonfinite_service_time'
        return row,None

    def queue(self,eid,rid,now):
        c=self.control;station=c.manager.stations[eid]
        result=dict(known=True,queue_wait_seconds=0.,wait_energy_j=0.,ahead=[],reason=None,version=VERSION,
                    basis='Configured-power estimate; 20 W idle electronics; predecessor configured drive power deducted from charging input×efficiency; not hardware-calibrated or a worst-case bound')
        def unknown(reason):
            result.update(known=False,queue_wait_seconds=None,wait_energy_j=None,reason=reason);return result
        if station.fault_latched:return unknown('station_requires_explicit_recovery')
        if c.energy_station_errors.get(eid):return unknown(c.energy_station_errors[eid])
        reading=c.station_observations.get(eid)
        if reading is None:return unknown('missing_station_observation')
        if reading is not None:
            stamp=reading.get('sampled_at')
            if not isinstance(stamp,(int,float)) or not math.isfinite(stamp) or stamp>now or now-stamp>c.owner.policy.stale_after:return unknown('station_observation_not_fresh')
            if reading.get('fault') is not False:return unknown('station_fault_or_invalid_observation')
        order=[]
        for other,plan in sorted(c.plans.items(),key=lambda pair:pair[1]['requested_at']):
            if plan['station_id']!=eid:continue
            if plan.get('clearing'):
                order.append((other,'clearing'))
            else:
                request=c.manager.requests.get(plan.get('request_id'))
                # Only an actual completed undock leaves a pending exit here.
                # A request cancelled while queued never occupied staging.
                if request and request.phase=='done':order.append((other,'clearance_pending'))
        if station.active:order.append((station.active.robot_id,station.active.phase))
        order.extend((req.robot_id,req.phase)for req in station.queue)
        if order and reading is None:return unknown('missing_station_observation')
        seen=set()
        for other,phase in order:
            if other==rid:break
            if other in seen:continue
            seen.add(other)
            if phase=='clearance_pending':return unknown('predecessor_clearance_unavailable')
            row,error=self._service(other,eid,phase,result['queue_wait_seconds'],now)
            if error:return unknown(error)
            result['ahead'].append(row);result['queue_wait_seconds']+=row['seconds']
            if not math.isfinite(result['queue_wait_seconds']):return unknown('nonfinite_queue_time')
        result['wait_energy_j']=result['queue_wait_seconds']*IDLE_POWER_W
        if not math.isfinite(result['wait_energy_j']):return unknown('nonfinite_queue_energy')
        return result
