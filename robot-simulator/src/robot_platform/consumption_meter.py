"""Read-only consumption telemetry from delivered, run-scoped observations.

This ideal research meter counts the simulator's existing energy integrals.
It neither estimates future demand nor supplies evidence to motion/charging
admission. Interval averages span observation gaps and are not peak power.
"""
from copy import deepcopy
import math

VERSION = 'research-consumption-v1'
COUNTERS = ('demand_j', 'drawn_j', 'unserved_j', 'charging_input_j', 'charging_stored_j')


def _number(value):
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return False
    try:
        return math.isfinite(value) and value >= 0
    except OverflowError:
        return False


class ConsumptionObservations:
    def __init__(self, run_id, robots, stale_after):
        self.run_id = run_id
        self.robots = {robot.id: robot for robot in robots}
        self.stale_after = stale_after
        self._accepted = {}
        self._errors = {}
        self._now = None

    def observe(self, now, observations):
        if not _number(now) or (self._now is not None and now < self._now):
            self._errors = {rid: 'invalid_observation_time' for rid in self.robots}
            return
        self._now = now
        for rid in self.robots:
            observation = observations.get(rid) if isinstance(observations, dict) else None
            previous = self._accepted.get(rid)
            if not isinstance(observation, dict):
                self._errors[rid] = 'missing_observation' if previous else 'waiting_for_observation'
                continue
            sensors = observation.get('sensors')
            meter = sensors.get('consumption_meter') if isinstance(sensors, dict) else None
            if not isinstance(meter, dict):
                self._errors[rid] = 'missing_meter'
                continue
            stamp, received = observation.get('sampled_at'), observation.get('received_at')
            if (observation.get('robot_id') != rid or meter.get('robot_id') != rid
                    or meter.get('run_id') != self.run_id or meter.get('version') != VERSION):
                self._errors[rid] = 'meter_identity_mismatch'
                continue
            if (not _number(stamp) or not _number(received) or not _number(meter.get('sampled_at'))
                    or stamp != meter['sampled_at'] or stamp > received or received > now + 1e-9):
                self._errors[rid] = 'invalid_meter_time'
                continue
            if any(not _number(meter.get(key)) for key in COUNTERS):
                self._errors[rid] = 'invalid_meter_counter'
                continue
            counters = {key: meter[key] for key in COUNTERS}
            supplied_and_unserved = counters['drawn_j'] + counters['unserved_j']
            if (not _number(supplied_and_unserved)
                    or not math.isclose(counters['demand_j'], supplied_and_unserved, rel_tol=1e-9, abs_tol=1e-7)
                    or counters['charging_stored_j'] > counters['charging_input_j'] + 1e-7):
                self._errors[rid] = 'inconsistent_meter_counter'
                continue
            signature = (stamp, received, *(counters[key] for key in COUNTERS))
            if previous:
                if stamp < previous['sampled_at'] or (stamp == previous['sampled_at'] and signature != previous['signature']):
                    self._errors[rid] = 'reordered_or_changed_meter'
                    continue
                if any(counters[key] < previous['counters'][key] for key in COUNTERS):
                    self._errors[rid] = 'decreasing_meter_counter'
                    continue
            if now - stamp > self.stale_after:
                self._errors[rid] = 'stale_observation'
                continue
            self._errors.pop(rid, None)
            if previous and stamp == previous['sampled_at']:
                continue  # A replayed sample is not a new measurement interval.
            interval = None
            if previous:
                seconds = stamp - previous['sampled_at']
                if not _number(seconds) or seconds <= 0:
                    self._errors[rid] = 'invalid_meter_interval'
                    continue
                interval = dict(start_at=previous['sampled_at'], end_at=stamp, seconds=seconds,
                    demand_w=(counters['demand_j'] - previous['counters']['demand_j']) / seconds,
                    drawn_w=(counters['drawn_j'] - previous['counters']['drawn_j']) / seconds)
                if not all(_number(interval[key]) for key in ('seconds', 'demand_w', 'drawn_w')):
                    self._errors[rid] = 'invalid_meter_interval'
                    continue
            self._accepted[rid] = dict(sampled_at=stamp, received_at=received,
                counters=counters, interval=interval, signature=signature)

    def report(self, robot_id, now):
        """Read without advancing counters or using current simulator truth."""
        robot = self.robots[robot_id]
        previous = self._accepted.get(robot_id)
        reason = self._errors.get(robot_id)
        valid_now = _number(now) and (self._now is None or now >= self._now)
        if not valid_now:
            status, reason = 'invalid', 'invalid_report_time'
        elif reason == 'waiting_for_observation' or (previous is None and reason is None):
            status = 'waiting'
        elif reason == 'stale_observation' or (reason is None and previous and now - previous['sampled_at'] > self.stale_after):
            status, reason = 'stale', 'stale_observation'
        elif reason:
            status = 'invalid'
        else:
            status = 'ready'
        return dict(version=VERSION, run_id=self.run_id, robot_id=robot_id, status=status, reason=reason,
            sampled_at=previous['sampled_at'] if previous else None,
            received_at=previous['received_at'] if previous else None,
            counters=deepcopy(previous['counters']) if previous else None,
            interval=deepcopy(previous['interval']) if previous and status == 'ready' else None,
            configured_drive_power_w=robot.estimated_drive_power_w)
