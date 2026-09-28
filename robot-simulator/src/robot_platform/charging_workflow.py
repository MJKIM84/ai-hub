"""Read-only charging lifecycle telemetry; never plans or authorizes motion.

Only observe() updates this reporter's own bounded history. Manager completion
means connector release, not clearance or subsequent task success. Durations
measure observed controller states; elapsed time alone never implies deadlock.
"""
from collections import OrderedDict
from copy import deepcopy
import math


VERSION = "charging-workflow-v1"
BLOCKED_REASONS = frozenset((
    "guided_approach_occupied", "approach_traffic_blocked",
    "clearance_traffic_blocked", "parking_blocks_service",
))


def _number(value):
    try:
        return (not isinstance(value, bool) and isinstance(value, (int, float))
                and math.isfinite(value) and value >= 0)
    except OverflowError:
        return False


def _elapsed(now, start):
    return now - start if _number(now) and _number(start) and start <= now else None


def _pose(value):
    if not isinstance(value, dict):
        return None
    try:
        if any(isinstance(value.get(k), bool) or not isinstance(value.get(k), (int, float))
               or not math.isfinite(value[k]) for k in ("x", "y", "z", "yaw")):
            return None
    except OverflowError:
        return None
    return {k: value[k] for k in ("x", "y", "z", "yaw")}


def _counter(value):
    return value if isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 2**53-1 else None


class ChargingWorkflow:
    """Snapshot only existing facts from ChargingControl, not simulator truth."""
    history_limit = 32

    def __init__(self, control):
        self.control = control
        self._reports = {}
        self._history = {}
        self._last_now = None

    def _observation(self, rid, now):
        c = self.control
        obs = c.energy_observations.get(rid)
        error = c.energy_observation_errors.get(rid)
        if not isinstance(obs, dict) or error or obs.get("robot_id") != rid:
            return dict(status="unknown", sampled_at=None, age_seconds=None,
                        battery_percent=None, pose=None, reason=error or "missing_accepted_observation"), None
        stamp = obs.get("sampled_at")
        age = _elapsed(now, stamp)
        battery = obs.get("battery")
        pose = _pose(obs.get("pose"))
        if age is None or not _number(battery) or battery > 100 or pose is None:
            return dict(status="unknown", sampled_at=None, age_seconds=None,
                        battery_percent=None, pose=None, reason="invalid_accepted_observation"), None
        current = _number(c.owner.policy.stale_after) and age <= c.owner.policy.stale_after
        return dict(status="current" if current else "stale", sampled_at=stamp,
                    age_seconds=age, battery_percent=battery, pose=pose,
                    reason=None if current else "stale_observation"), obs if current else None

    def _request(self, rid, plan):
        c = self.control
        req = c.manager.requests.get(plan.get("request_id"))
        if req is not None and req.robot_id == rid and req.station_id == plan.get("station_id"):
            return req, True
        previous = [r for r in c.manager.requests.values() if r.robot_id == rid and _number(r.requested_at)]
        return (max(previous, key=lambda r: r.requested_at), False) if previous else (None, False)

    def _task_after_clearance(self, rid, clearance):
        if not clearance:
            return dict(status="not_observed", task_id=None, started_at=None, completed_at=None)
        completed = clearance["completed_at"]
        rows = [t for t in self.control.owner.tasks.values()
                if t.get("robot_id") == rid and _number(t.get("started_at"))
                and t["started_at"] >= completed]
        if not rows:
            return dict(status="awaiting_assignment", task_id=None, started_at=None, completed_at=None)
        task = min(rows, key=lambda t: (t["started_at"], str(t.get("id", ""))))
        return dict(status=task.get("status", "unknown"), task_id=task.get("id"),
                    started_at=task["started_at"], completed_at=task.get("completed_at"),
                    reason=task.get("reason"), basis="first_recorded_assignment_after_clearance")

    def _ownership(self, rid, station_id, state, plan):
        c = self.control
        station = c.manager.stations.get(station_id)
        egress = []
        for owner_id, entry in c.plans.items():
            target = _pose(entry.get("parking") or entry.get("egress_target"))
            if target is not None:
                egress.append(dict(robot_id=owner_id, request_id=entry.get("request_id"),
                    station_id=entry.get("station_id"), target=target,
                    floor_id=entry.get("parking_floor_id", entry.get("egress_floor_id")),
                    clearing=entry.get("clearing") is True, interrupted=entry.get("interrupted") is True))
        resources = [{"resource": resource, "robot_ids": list(owners)}
                     for resource, owners in c.owner.reservations.owners.items() if rid in owners]
        path = state.get("path", [])
        # A structural attribution, explicitly not an ownership authorization.
        path_owner = ("none" if not path else "facility" if state.get("trip") else
                      "charging" if plan and state.get("status") == "charging" else
                      "task" if state.get("task_id") else
                      "manual" if state.get("status") == "manual" else "unknown")
        return dict(connector_robot_id=station.active.robot_id if station and station.active else None,
                    queue_robot_ids=[r.robot_id for r in station.queue] if station else [],
                    occupants=list(station.occupants) if station else [],
                    station_fault=station.fault if station else None,
                    station_fault_latched=bool(station and station.fault_latched),
                    egress_reservations=egress, resources=resources,
                    path_owner=path_owner, path_waypoint_count=len(path),
                    path_owner_basis="controller_state_and_active_plan")

    def _collect(self, rid, now, previous):
        c = self.control
        state = c.owner.robot_states[rid]
        plan = c.plans.get(rid, {})
        req, current_request = self._request(rid, plan)
        obs_report, obs = self._observation(rid, now)
        summary = state.get("charging_energy") or {}
        traffic_reason = plan.get("traffic_reason")
        traffic_status = ("blocked" if traffic_reason in BLOCKED_REASONS else
                          "unknown" if traffic_reason else summary.get("access_status", "unknown"))
        if traffic_status not in ("available", "blocked", "unknown"):
            traffic_status = "unknown"
        # Queue membership is a normal wait; neither a duration nor zero path
        # is sufficient evidence of a traffic blockage.
        stage = "idle"
        if obs is None:
            stage = "observation_wait"
        elif state.get("operator_hold") or state.get("status") in ("fault", "recovery_required"):
            stage = "interrupted"
        elif state.get("status") in ("recovering", "transit_recovery"):
            stage = "other_recovery"
        elif plan:
            if plan.get("interrupted"):
                stage = "interrupted"
            elif plan.get("clearing"):
                stage = "clearing"
            elif current_request:
                stage = "stop_handoff" if req.handoff_pending else req.phase
            else:
                stage = "unknown"
        elif summary.get("admission_status"):
            stage = "request_wait"
        elif state.get("status") in ("working", "manipulating", "cooperating"):
            stage = "task_running"
        stage_key = (stage, req.id if current_request else None)
        since = previous.get("stage_since") if previous and previous.get("_stage_key") == stage_key else now
        since_basis = "first_observed_controller_stage"
        if stage == "clearing" and _elapsed(now, plan.get("clearance_started_at")) is not None:
            since, since_basis = plan["clearance_started_at"], "controller_clearance_started_at"
        elif current_request and stage == req.phase and _elapsed(now, req.phase_since) is not None:
            since, since_basis = req.phase_since, "manager_phase_since"
        station_id = plan.get("station_id") or (req.station_id if req else summary.get("selected_station_id"))
        request = None
        if req:
            phase_limit = c.manager.phase_timeouts.get(req.phase)
            request = dict(request_id=req.id, station_id=req.station_id, current=current_request,
                status=req.status, phase=req.phase, reason=req.reason, requested_at=req.requested_at,
                phase_since=req.phase_since, elapsed_seconds=_elapsed(now, req.requested_at),
                phase_elapsed_seconds=_elapsed(now, req.phase_since), target_percent=req.target_percent,
                stop_pending=req.handoff_pending, stop_delivered_at=req.stop_delivered_at,
                cancel_requested=req.cancel_requested, attempts=_counter(getattr(req, "attempts", None)),
                limits=dict(phase_timeout_seconds=phase_limit, contact_timeout_seconds=c.manager.near_contact_timeout,
                            clearance_timeout_seconds=c.manager.phase_timeouts.get("approach"),
                            approach_budget=deepcopy(plan.get("approach_budget"))))
        departure = c.departure_history.get(rid)
        clearance = None
        if departure and _elapsed(now, departure.get("completed_at")) is not None:
            clearance = dict(completed_at=departure["completed_at"],
                request_id=(departure.get("target_plan") or {}).get("request_id"),
                battery_percent=departure.get("battery"), pose=_pose(departure.get("pose")),
                basis="controller_observed_clearance")
        ownership = self._ownership(rid, station_id, state, plan)
        resume_applicable = bool(state.get("operator_hold") or (plan and state.get("status") == "recovery_required"))
        blocked = ("fresh_observation_required" if obs is None else
                   "healthy_observation_required" if obs.get("fault") != "none" or obs.get("battery", 0) <= 0
                   or not _number(obs.get("upright")) or obs["upright"] < .45 else
                   "item_recovery_required" if any(r["resource"].startswith("item:") for r in ownership["resources"]) else None)
        return dict(version=VERSION, robot_id=rid, assessed_at=now, current=obs is not None,
            observation=obs_report, stage=stage, stage_since=since, stage_since_basis=since_basis,
            elapsed_seconds=_elapsed(now, since),
            reason=state.get("reason"), robot_status=state.get("status"), operator_hold=bool(state.get("operator_hold")),
            request=request, station_id=station_id,
            traffic=dict(status=traffic_status, reason=traffic_reason or summary.get("reason"),
                source="active_plan" if traffic_reason else "energy_assessment",
                replan_attempts=_counter(plan.get("replan_attempts")), last_replan_at=plan.get("last_replan_at"),
                blocking_robot_ids=deepcopy(plan.get("blocking_robot_ids", [])),
                need_trigger_percent=summary.get("need_trigger_percent")),
            waiting_classification=("normal_queue" if current_request and req.phase == "queued" else
                                    "explicit_traffic_block" if traffic_status == "blocked" else
                                    "observation_unknown" if obs is None else "no_explicit_block"),
            ownership=ownership, clearance=clearance,
            task_after_clearance=self._task_after_clearance(rid, clearance),
            current_task_id=state.get("task_id"),
            recovery=dict(resume_applicable=resume_applicable, blocked_reason=blocked,
                          attempts=_counter(plan.get("recovery_attempts")),
                          server_rechecks_required=True, automatic_yield_supported=False),
            _stage_key=stage_key)

    def observe(self, now):
        if not _number(now) or (self._last_now is not None and now < self._last_now):
            return
        for rid in self.control.owner.robots:
            report = self._collect(rid, now, self._reports.get(rid))
            cycles = self._history.setdefault(rid, OrderedDict())
            req = report["request"]
            if req:
                entry = cycles.setdefault(req["request_id"], dict(request_id=req["request_id"], first_seen_at=now))
                entry.update(station_id=req["station_id"], requested_at=req["requested_at"],
                             status=req["status"], phase=req["phase"], target_percent=req["target_percent"], last_seen_at=now)
            clearance = report["clearance"]
            if clearance and clearance["request_id"] in cycles:
                entry = cycles[clearance["request_id"]]
                entry["clearance_completed_at"] = clearance["completed_at"]
                entry["task_after_clearance"] = deepcopy(report["task_after_clearance"])
            while len(cycles) > self.history_limit:
                cycles.popitem(last=False)
            report["cycles"] = deepcopy(list(cycles.values()))
            report["history_limit"] = self.history_limit
            self._reports[rid] = report
        self._last_now = now

    def snapshot(self, rid, now):
        stored = self._reports.get(rid)
        if stored is None:
            return None
        report = deepcopy(stored)
        report.pop("_stage_key", None)
        report["report_age_seconds"] = _elapsed(now, report["assessed_at"])
        fresh = (report["report_age_seconds"] is not None
                 and _number(self.control.owner.policy.stale_after)
                 and report["report_age_seconds"] <= self.control.owner.policy.stale_after)
        if not fresh or _elapsed(now, report["observation"]["sampled_at"]) is None:
            report["current"] = False
        elif now - report["observation"]["sampled_at"] > self.control.owner.policy.stale_after:
            report["current"] = False
            report["observation"]["status"] = "stale"
        report["observation"]["age_seconds"] = _elapsed(now, report["observation"]["sampled_at"])
        if not report["current"]:
            report["recovery"]["blocked_reason"] = "fresh_observation_required"
        return report
