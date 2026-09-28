"""Explicit task-budget charging targets from a reserved future exit pose.

This planner uses accepted observations and static scheduling estimates only.
It predicts one pending task; it neither assigns that task nor guarantees its
future availability, completion time, consumption or reservation.
"""
from copy import deepcopy
import math

from .catalog import model_by_id
from .charging_energy import travel
from .motion_limits import translation_time

VERSION = 'charging-target-plan-v1'
SERVICE_VERSION = 'charging-service-target-v1'


def finite(value):
    try:
        return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
    except OverflowError:
        return False


def service_ready(plan, configured_target):
    """Validate the independent service result before requesting a connector."""
    service = plan.get('service_target') or {}
    target = service.get('target_percent')
    if (service.get('version') != SERVICE_VERSION or service.get('status') != 'ready'
            or not finite(target) or not configured_target <= target <= 100):
        return False
    purpose = service.get('purpose')
    if purpose == 'fixed':
        return plan.get('mode') == 'fixed' and plan.get('status') == 'ready' and target == plan.get('target_percent') == configured_target
    reserve = service.get('required_reserve_percent')
    trigger = service.get('next_charge_trigger_percent')
    if (plan.get('mode') != 'task_budget' or not finite(reserve) or not configured_target <= reserve <= target
            or not finite(trigger) or trigger < 0 or not finite(plan.get('exit_energy_j'))
            or plan['exit_energy_j'] < 0):
        return False
    if purpose == 'task_budget':
        return (plan.get('status') == 'ready' and plan.get('task_id') is not None
            and finite(plan.get('target_percent')) and target == max(plan['target_percent'], reserve))
    return (purpose == 'reserve_only' and target == reserve and
        ((plan.get('status') == 'infeasible' and plan.get('reason') == 'target_exceeds_capacity')
         or (plan.get('status') == 'unknown' and plan.get('reason') == 'task_energy_unavailable')
         or (plan.get('status') == 'ready' and plan.get('task_id') is None
             and plan.get('reason') == 'no_eligible_planned_task')))


def plan_target(control, robot, observation, geometry, exit_target, exit_route, now):
    owner = control.owner
    mode = owner.policy.charge_target_mode
    stamp = observation.get('sampled_at') if isinstance(observation, dict) else None
    result = dict(version=VERSION, mode=mode, status='unknown',
        configured_target_percent=owner.policy.charge_until, target_percent=None,
        assessed_at=now, sampled_at=stamp if finite(stamp) else None, request_id=None,
        task_id=None, task_name=None, exit_energy_j=None, task_required_percent=None,
        reason=None, exit_target=deepcopy(exit_target),
        basis='Static prediction from reserved clearance pose. Upcoming task is not assigned; actual observation, eligibility and energy are checked again after clearance.')
    service = dict(version=SERVICE_VERSION, status='unknown', purpose=None,
        target_percent=None, required_reserve_percent=None, next_charge_trigger_percent=None,
        assessed_at=now, sampled_at=result['sampled_at'], request_id=None, station_id=None,
        reason='service_energy_unavailable')
    result['service_target'] = service

    def finish():
        # The work forecast stays intact even when only basic charging is
        # possible. A separate, known exit-and-return budget authorizes that
        # service; an unavailable task is never silently declared feasible.
        reserve = service['required_reserve_percent']
        if service['status'] != 'ready' or not finite(reserve):
            return result
        if result['status'] == 'ready' and result['task_id'] is not None:
            service.update(purpose='task_budget',
                target_percent=max(result['target_percent'], reserve), reason=None)
        elif result['reason'] in ('task_energy_unavailable', 'target_exceeds_capacity', 'no_eligible_planned_task'):
            service.update(purpose='reserve_only', target_percent=reserve,
                reason='basic_reserve_without_task_admission')
        else:
            service.update(status='unknown', purpose=None, target_percent=None,
                reason=result['reason'] or 'service_energy_unavailable')
        return result

    def unknown(reason, detail=None):
        result.update(status='unknown', target_percent=None, reason=reason)
        if detail:result['detail_reason'] = detail
        if service['reason'] == 'service_energy_unavailable':
            service['reason'] = reason
        return finish()

    if mode == 'fixed':
        result.update(status='ready', target_percent=owner.policy.charge_until, reason='fixed_policy_target')
        service.update(status='ready', purpose='fixed', target_percent=owner.policy.charge_until,
            reason='fixed_policy_target')
        return result
    if mode != 'task_budget':
        return unknown('invalid_target_mode')
    if (not finite(now) or not finite(stamp) or stamp < 0 or stamp > now
            or now-stamp > owner.policy.stale_after
            or control.energy_observations.get(robot.id) != observation):
        return unknown('missing_or_stale_target_observation')
    if exit_target is None or exit_route is None:
        return unknown('exit_route_unavailable')
    capacity = robot.battery_capacity_wh * 3600
    if not finite(capacity) or capacity <= 0:
        return unknown('nonfinite_target_energy')
    floor = owner._floor(geometry['staging']['z'])
    undock = translation_time(robot, owner.policy, control.project.environment,
        geometry['target'], [geometry['staging']], floor, cap=.12)
    clear = travel(robot, owner.policy, geometry['staging'], exit_route,
        exit_target['yaw'], control.project.environment, floor, preserve_corners=True)
    if not undock['known'] or not clear['known']:
        return unknown('unknown_exit_energy', (undock if not undock['known'] else clear)['reason'])
    handoff = control.energy.handoff_estimate(robot)
    exit_seconds = undock['seconds'] + 1. + control.manager.confirmation_time + handoff['seconds'] + clear['seconds'] + control.manager.confirmation_time
    exit_energy = exit_seconds * robot.estimated_drive_power_w
    if not finite(exit_energy):
        return unknown('nonfinite_target_energy')
    result.update(exit_energy_j=exit_energy, exit_seconds=exit_seconds,
        exit_time=dict(undock=undock, clearance=clear, handoff=handoff))
    projected = deepcopy(observation)
    projected.update(pose=deepcopy(exit_target), battery=100.)
    # Planner diagnostics about a future pose must not replace current route
    # rejection state. No sensor sample, actual pose or task state is changed.
    rejections = deepcopy(owner.guided_rejections)
    try:
        next_candidates = control._energy_candidates(robot, projected, now, floor, live_traffic=False)
        known = [row for row in next_candidates if row.get('known') and finite(row.get('trigger_percent'))]
        service['next_charge_candidates'] = [{key:deepcopy(value) for key,value in row.items()
            if key not in ('path','geometry','parking')} for row in next_candidates]
        if known:
            next_charge = min(known, key=lambda row:(row['trigger_percent'],row['station_id']))
            reserve = max(owner.policy.charge_until,
                exit_energy/capacity*100 + max(owner.policy.charge_below,next_charge['trigger_percent']))
            service.update(required_reserve_percent=reserve,
                next_charge_trigger_percent=next_charge['trigger_percent'],
                next_station_id=next_charge['station_id'])
            if finite(reserve) and reserve <= 100:
                service.update(status='ready', reason=None)
            elif finite(reserve):
                service.update(status='infeasible', reason='reserve_target_exceeds_capacity')
            else:
                service['reason']='nonfinite_reserve_energy'
        else:
            service['reason']='next_charge_energy_unavailable'
        pending = [row for row in owner.tasks.values() if row['status'] in ('pending','waiting')]
        pending.sort(key=lambda row:(row['spec'].deadline if owner.policy.assignment=='deadline' and row['spec'].deadline is not None else -row['spec'].priority,
            row['spec'].release_time,row['id']))
        required = owner.policy.charge_below
        selected = None
        for row in pending:
            task = row['spec']
            if task.deadline is not None and now > task.deadline:continue
            if any(owner.tasks[p]['status'] in ('failed','cancelled') for p in task.predecessor_ids):continue
            if task.cooperation:
                if task.cooperation.carrier_id != robot.id:continue
                if task.kind not in model_by_id(robot.model_id)['capabilities']:continue
                if task.floor_id != floor:continue
                destination = task.cooperation.carrier_destination
                trip = None
            else:
                if owner._eligible(robot,task,projected,now):continue
                destination = task.destination
                trip = owner._trip_plan(robot,projected,task) if task.floor_id != floor else None
            route = trip['route'] if trip else [] if task.kind=='manipulate' else owner._route(robot,projected,destination.model_dump(),task.floor_id)
            result.update(task_id=task.id,task_name=task.name,task_release_time=task.release_time)
            if route is None:return unknown('task_energy_unavailable','projected_task_route_unavailable')
            budget = control.task_budget(robot,task,observation,route,trip,projected_start=exit_target)
            if not budget.get('energy_estimate_valid') or not finite(budget.get('required_percent')):
                return unknown('task_energy_unavailable',budget.get('reason'))
            required = budget['required_percent']
            selected = budget
            break
        target = max(owner.policy.charge_until, required + exit_energy/capacity*100)
        if not finite(target):return unknown('nonfinite_target_energy')
        result.update(task_required_percent=required, required_target_percent=target,
            task_work_j=selected['estimated_work_j'] if selected else None,
            task_return_j=selected['estimated_return_j'] if selected else None)
        if target > 100:
            result.update(status='infeasible',reason='target_exceeds_capacity')
            return finish()
        result.update(status='ready',target_percent=target,
            reason=None if selected else 'no_eligible_planned_task')
        return finish()
    finally:
        owner.guided_rejections.clear()
        owner.guided_rejections.update(rejections)
