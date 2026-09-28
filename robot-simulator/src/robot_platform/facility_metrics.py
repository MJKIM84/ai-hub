"""Time integrals of complete elevator/charger manager snapshots.

These are observed manager-state durations, not inferred physical standstill,
enqueue timestamps, electrical utilization, or operator repair response times.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
import math


_PHASES = {
    'elevator': {'idle', 'closing_empty', 'positioning', 'opening_board', 'boarding',
                 'closing_depart', 'moving', 'opening_exit', 'alighting', 'opening_call', 'fault'},
    'charger': {'idle', 'approach', 'dock', 'charging', 'undock', 'fault'},
}
_STATUSES = {
    'elevator': {'queued', 'reserved', 'boarded', 'completed', 'cancelled'},
    'charger': {'queued', 'running', 'interrupted', 'completed', 'cancelled'},
}


def _time(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
        raise ValueError('time must be a finite nonnegative number')
    return float(value)


def _identifier(value, label):
    if not isinstance(value, str) or not value:
        raise ValueError(label+' must be a nonempty string')
    return value


def _ids(value, label):
    if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
        raise ValueError(label+' must be a list of nonempty robot-id strings')
    if len(set(value)) != len(value):
        raise ValueError(label+' contains duplicate robot ids')
    return tuple(value)


def _normalize(eid, row, kind):
    if row is None:
        return None
    if not isinstance(row, dict):
        raise ValueError(eid+' state must be a dictionary or None (unknown)')
    required = {'phase', 'queue', 'reserved_by', 'occupants', 'fault', 'requests'}
    if required-set(row):
        raise ValueError(eid+' state missing fields: '+', '.join(sorted(required-set(row))))
    if not isinstance(row['phase'], str) or row['phase'] not in _PHASES[kind]:
        raise ValueError(eid+' has an unsupported '+kind+' phase')
    if row.get('kind', kind) != kind:
        raise ValueError(eid+' state kind does not match metrics kind')
    queue, reserved, occupants = (_ids(row[key], eid+'.'+key) for key in ('queue', 'reserved_by', 'occupants'))
    if set(queue)&set(reserved):
        raise ValueError(eid+' robot cannot be queued and reserved simultaneously')
    if kind == 'charger' and len(reserved)>1:
        raise ValueError(eid+' charger has more than one reservation')
    fault = row['fault']
    if fault is not None and type(fault) is not bool and not isinstance(fault, str):
        raise ValueError(eid+'.fault must be None, bool, or a fault-code string')
    latched = row.get('fault_latched', False)
    if type(latched) is not bool:
        raise ValueError(eid+'.fault_latched must be bool')
    if not isinstance(row['requests'], list):
        raise ValueError(eid+'.requests must be a list of request receipts')
    requests = {}
    for item in row['requests']:
        if not isinstance(item, dict) or not {'request_id', 'robot_id', 'status'}<=item.keys():
            raise ValueError(eid+' malformed request receipt')
        request_id = _identifier(item['request_id'], 'request_id')
        rid = _identifier(item['robot_id'], 'robot_id')
        if request_id in requests or not isinstance(item['status'], str) or item['status'] not in _STATUSES[kind]:
            raise ValueError(eid+' duplicate request id or unsupported request status')
        if item.get('station_id', eid) != eid:
            raise ValueError(eid+' request belongs to another station')
        requests[request_id] = {'robot_id': rid, 'status': item['status']}
    queued = {rid: [qid for qid, request in requests.items()
                    if request['robot_id']==rid and request['status']=='queued'] for rid in queue}
    if any(len(ids)!=1 for ids in queued.values()) or {r['robot_id'] for r in requests.values() if r['status']=='queued'}!=set(queue):
        raise ValueError(eid+' queue must match exactly one queued request per robot')
    for rid in reserved:
        active = [r for r in requests.values() if r['robot_id']==rid and r['status'] not in ('queued', 'completed', 'cancelled')]
        if len(active)!=1:
            raise ValueError(eid+' reservation must match exactly one active request')
    return {'phase': row['phase'], 'queue': queue, 'reserved_by': reserved, 'occupants': occupants,
            'fault_active': row['phase']=='fault' or bool(fault) or latched, 'fault': fault,
            'requests': requests, 'queued_requests': {rid: ids[0] for rid, ids in queued.items()}}


@dataclass
class _Facility:
    started_at: float
    state: dict | None = None
    known_seconds: float = 0.
    unknown_seconds: float = 0.
    reserved_seconds: float = 0.
    occupied_seconds: float = 0.
    reserved_robot_seconds: float = 0.
    occupied_robot_seconds: float = 0.
    fault_seconds: float = 0.
    robots: dict = field(default_factory=dict)
    waits: list = field(default_factory=list)
    open_waits: dict = field(default_factory=dict)
    faults: list = field(default_factory=list)
    open_fault: dict | None = None
    intervals: list = field(default_factory=list)
    request_robots: dict = field(default_factory=dict)


def _robot_row():
    return {'reserved_seconds': 0., 'occupied_seconds': 0., 'facility_fault_exposure_seconds': 0.}


def _close(interval, now, status, reason):
    interval.update(ended_at=now, status=status, end_reason=reason)


def _intervals(rows, now):
    result = deepcopy(rows)
    for row in result:
        row['observed_seconds'] = (now if row['ended_at'] is None else row['ended_at'])-row['started_at']
        row['right_censored'] = row['status'] in ('open', 'unknown')
        row['eligible_for_completed_statistics'] = row['status']=='completed' and not row['left_censored']
    return result


def _wait_statistics(rows):
    eligible = [row['observed_seconds'] for row in rows if row['eligible_for_completed_statistics']]
    return {
        'queue_wait_seconds': sum(row['observed_seconds'] for row in rows),
        'completed_queue_wait_count': len(eligible),
        'completed_queue_wait_mean_seconds': sum(eligible)/len(eligible) if eligible else None,
        'completed_queue_wait_max_seconds': max(eligible, default=None),
        'granted_queue_wait_count': sum(row['status']=='completed' for row in rows),
        'cancelled_queue_wait_count': sum(row['status']=='cancelled' for row in rows),
        'cancelled_queue_wait_seconds': sum(row['observed_seconds'] for row in rows if row['status']=='cancelled'),
        'open_queue_wait_count': sum(row['status']=='open' for row in rows),
        'open_queue_wait_seconds': sum(row['observed_seconds'] for row in rows if row['status']=='open'),
        'unknown_queue_wait_count': sum(row['status']=='unknown' for row in rows),
        'left_censored_queue_wait_count': sum(row['left_censored'] for row in rows),
        'censored_queue_wait_count': sum(row['left_censored'] or row['right_censored'] for row in rows),
        'censored_queue_wait_seconds': sum(row['observed_seconds'] for row in rows if row['left_censored'] or row['right_censored']),
    }


class FacilityMetrics:
    """Integrate one manager's complete snapshots on its simulation clock.

    ``update`` timestamps must strictly increase. ``snapshot`` is read-only and
    extends the last state to its supplied time without committing that future.
    Missing facilities become unknown; missing keys inside a state are errors.
    """
    VERSION = 'observed-facility-metrics-0.1'

    def __init__(self, kind, facility_ids=None):
        if not isinstance(kind, str) or kind not in _PHASES:
            raise ValueError('kind must be elevator or charger')
        if isinstance(facility_ids, str):
            raise ValueError('facility_ids must be an iterable of complete facility ids')
        self.kind = kind
        self._configured = tuple(_identifier(eid, 'facility id') for eid in (facility_ids or []))
        if len(set(self._configured)) != len(self._configured):
            raise ValueError('duplicate facility id')
        self._facilities = {}
        self._last_update = None

    def _integrate(self, now):
        dt = 0. if self._last_update is None else now-self._last_update
        for facility in self._facilities.values():
            state = facility.state
            if state is None:
                facility.unknown_seconds += dt
                continue
            facility.known_seconds += dt
            facility.reserved_seconds += bool(state['reserved_by'])*dt
            facility.occupied_seconds += bool(state['occupants'])*dt
            facility.reserved_robot_seconds += len(state['reserved_by'])*dt
            facility.occupied_robot_seconds += len(state['occupants'])*dt
            facility.fault_seconds += state['fault_active']*dt
            for rid in set(state['queue'])|set(state['reserved_by'])|set(state['occupants']):
                robot = facility.robots.setdefault(rid, _robot_row())
                robot['reserved_seconds'] += (rid in state['reserved_by'])*dt
                robot['occupied_seconds'] += (rid in state['occupants'])*dt
                robot['facility_fault_exposure_seconds'] += state['fault_active']*dt

    def update(self, now, states):
        now = _time(now)
        if self._last_update is not None and now<=self._last_update:
            raise ValueError('update timestamps must strictly increase; duplicate/reordered update rejected')
        if not isinstance(states, dict):
            raise ValueError('states must be the complete manager states dictionary')
        # Validate every row before mutating any counters or timeline.
        normalized = {_identifier(eid, 'facility id'): _normalize(eid, row, self.kind) for eid, row in states.items()}
        for eid, state in normalized.items():
            if state is None or eid not in self._facilities:continue
            identities = self._facilities[eid].request_robots
            if any(qid in identities and identities[qid]!=request['robot_id'] for qid, request in state['requests'].items()):
                raise ValueError(eid+' request id changed robot identity')
        self._integrate(now)
        for eid in set(self._configured)|set(normalized):
            if eid not in self._facilities:
                self._facilities[eid] = _Facility(started_at=now)
        for eid, facility in self._facilities.items():
            previous, state = facility.state, normalized.get(eid)
            for rid, interval in list(facility.open_waits.items()):
                if state is not None and state['queued_requests'].get(rid)==interval['request_id']:
                    continue
                request = state['requests'].get(interval['request_id']) if state is not None else None
                if request and request['status']=='cancelled':
                    outcome, reason = 'cancelled', 'request_cancelled'
                elif request and request['status'] not in ('queued', 'cancelled'):
                    outcome, reason = 'completed', 'request_advanced_beyond_queue'
                else:
                    outcome, reason = 'unknown', 'state_missing' if state is None else 'request_or_queue_membership_disappeared'
                _close(interval, now, outcome, reason)
                del facility.open_waits[rid]
            if state is not None:
                facility.request_robots.update({qid:request['robot_id'] for qid,request in state['requests'].items()})
                for rid, request_id in state['queued_requests'].items():
                    if rid not in facility.open_waits:
                        interval = {'facility_id': eid, 'robot_id': rid, 'request_id': request_id, 'started_at': now,
                                    'ended_at': None, 'status': 'open', 'end_reason': None, 'left_censored': previous is None}
                        facility.waits.append(interval);facility.open_waits[rid] = interval
                for rid in set(state['queue'])|set(state['reserved_by'])|set(state['occupants']):
                    facility.robots.setdefault(rid, _robot_row())
            if facility.open_fault is not None and (state is None or not state['fault_active']):
                _close(facility.open_fault, now, 'unknown' if state is None else 'completed',
                       'state_missing' if state is None else 'first_nonfault_manager_state')
                facility.open_fault = None
            if state is not None and state['fault_active'] and facility.open_fault is None:
                interval = {'facility_id': eid, 'started_at': now, 'ended_at': None, 'status': 'open',
                            'end_reason': None, 'left_censored': previous is None, 'initial_fault': state['fault']}
                facility.faults.append(interval);facility.open_fault = interval
            segment = {'phase': state['phase'], 'queue': list(state['queue']), 'reserved_by': list(state['reserved_by']),
                       'occupants': list(state['occupants']), 'fault_active': state['fault_active']} if state is not None else {'phase': 'unknown', 'queue': None, 'reserved_by': None, 'occupants': None, 'fault_active': None}
            if not facility.intervals or any(facility.intervals[-1][key]!=value for key, value in segment.items()):
                if facility.intervals:facility.intervals[-1]['ended_at'] = now
                facility.intervals.append(dict(segment, started_at=now, ended_at=None))
            facility.state = state
        self._last_update = now

    def snapshot(self, now):
        now = _time(now)
        if self._last_update is not None and now<self._last_update:
            raise ValueError('snapshot cannot precede the last update')
        projected = deepcopy(self)
        projected._integrate(now)
        facilities, robots, all_waits, all_faults = {}, {}, [], []
        numeric = ('known_seconds', 'unknown_seconds', 'reserved_seconds', 'occupied_seconds',
                   'reserved_robot_seconds', 'occupied_robot_seconds', 'fault_seconds')
        totals = {key: 0. for key in numeric}
        for eid, facility in sorted(projected._facilities.items()):
            waits, faults = _intervals(facility.waits, now), _intervals(facility.faults, now)
            row = {key: getattr(facility, key) for key in numeric}
            row.update(_wait_statistics(waits))
            recoveries = [item['observed_seconds'] for item in faults if item['eligible_for_completed_statistics']]
            row.update(kind=self.kind, started_at=facility.started_at, state='unknown' if facility.state is None else facility.state['phase'],
                       occupancy_basis='manager_reported_occupants_zero_order_hold', occupancy_freshness_verified=False,
                       reserved_utilization=row['reserved_seconds']/row['known_seconds'] if row['known_seconds'] else None,
                       occupied_utilization=row['occupied_seconds']/row['known_seconds'] if row['known_seconds'] else None,
                       completed_recovery_count=len(recoveries), mean_recovery_seconds=sum(recoveries)/len(recoveries) if recoveries else None,
                       max_recovery_seconds=max(recoveries, default=None), open_fault_count=sum(item['status']=='open' for item in faults),
                       censored_fault_count=sum(item['left_censored'] or item['right_censored'] for item in faults),
                       queue_wait_intervals=waits, fault_intervals=faults, state_intervals=deepcopy(facility.intervals), robots={})
            for segment in row['state_intervals']:
                segment['observed_seconds'] = (now if segment['ended_at'] is None else segment['ended_at'])-segment['started_at']
            for rid, values in sorted(facility.robots.items()):
                own_waits = [item for item in waits if item['robot_id']==rid]
                row['robots'][rid] = dict(values, **_wait_statistics(own_waits), queue_wait_intervals=own_waits)
                combined = robots.setdefault(rid, dict(_robot_row(), facilities={}, queue_wait_intervals=[]))
                combined['facilities'][eid] = deepcopy(row['robots'][rid])
                combined['queue_wait_intervals'].extend(deepcopy(own_waits))
                for key in _robot_row():combined[key] += values[key]
            facilities[eid] = row
            all_waits.extend(waits);all_faults.extend(faults)
            for key in numeric:totals[key] += row[key]
        for row in robots.values():row.update(_wait_statistics(row['queue_wait_intervals']))
        totals.update(_wait_statistics(all_waits))
        recoveries = [row['observed_seconds'] for row in all_faults if row['eligible_for_completed_statistics']]
        totals.update(completed_recovery_count=len(recoveries), mean_recovery_seconds=sum(recoveries)/len(recoveries) if recoveries else None,
                      max_recovery_seconds=max(recoveries, default=None))
        return {'version': self.VERSION, 'kind': self.kind, 'as_of': now, 'last_update_at': self._last_update,
                'facilities': facilities, 'robots': robots, 'totals': totals}
