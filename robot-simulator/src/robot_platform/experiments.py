"""Headless repeated physical experiments and evidence-bearing exports."""
from __future__ import annotations
import csv
import hashlib
import io
import json
import math
import platform
import statistics
import sys
from pathlib import Path
from uuid import uuid4

import mujoco
import numpy as np

from . import __version__
from .runtime import Session
from .domain import Project,Policy


RECOVERY_COUNTS = ("started", "completed", "failed_or_cancelled")
RECOVERY_MEANS = ("mean_active_seconds", "mean_failure_to_recovery_seconds")
RECOVERY_FIELDS = tuple("cooperative_recovery_"+key for key in (*RECOVERY_COUNTS, *RECOVERY_MEANS))


def _recovery_metrics(metrics):
    """Flatten validated run statistics, preserving absent versus measured zero.

    Duration means describe completed recoveries only. They are unavailable if
    the run has no completions or its event counts cannot be interpreted safely.
    The original nested JSON is never modified.
    """
    values = dict.fromkeys(RECOVERY_FIELDS)
    recovery = metrics.get("cooperative_recovery")
    if not isinstance(recovery, dict):
        return values
    counts = [recovery.get(key) for key in RECOVERY_COUNTS]
    if (any(type(value) is not int or value < 0 for value in counts)
            or counts[1]+counts[2] > counts[0]):
        return values
    values.update({"cooperative_recovery_"+key:value for key,value in zip(RECOVERY_COUNTS, counts)})
    if recovery["completed"]:
        for key in RECOVERY_MEANS:
            value = recovery.get(key)
            if type(value) in (int, float) and math.isfinite(value) and value >= 0:
                values["cooperative_recovery_"+key] = value
    return values


def _recovery_summary(rows):
    """Each input run has equal weight; this is not an event-pooled mean."""
    runs = [_recovery_metrics(row) for row in rows]
    summary = {}
    for key in RECOVERY_FIELDS:
        values = [run[key] for run in runs if run[key] is not None]
        summary[key] = dict(mean=statistics.mean(values) if values else None,
            stddev=statistics.stdev(values) if len(values)>1 else None, n=len(values),
            unavailable_n=len(rows)-len(values), aggregation="per_run_statistic",
            unit="simulation_seconds" if key.removeprefix("cooperative_recovery_") in RECOVERY_MEANS else "count")
    return summary


def manifest(project):
    canonical=json.dumps(project.model_dump(),sort_keys=True,separators=(",",":"),ensure_ascii=False)
    source=Path(__file__).parent
    code_hashes={str(p.relative_to(source)):hashlib.sha256(p.read_bytes()).hexdigest() for p in source.rglob("*.py")}
    provenance=source.parents[1]/"assets/robots/spot/PROVENANCE.json"
    return dict(schema_version="1.0",project=project.model_dump(),input_sha256=hashlib.sha256(canonical.encode()).hexdigest(),source_sha256=code_hashes,robot_source=json.loads(provenance.read_text()) if provenance.exists() else None,software=dict(platform=__version__,mujoco=mujoco.__version__,numpy=np.__version__,python=sys.version,host=platform.platform()),clock="simulation seconds; wall timing recorded separately",fidelity=project.physics.fidelity,model_basis="see assets and docs/physics-foundation.md",energy_model="mechanical absolute work +20W electronics; per-robot battery_capacity_wh and route-power estimate; dual physical connector gated charge_power_w times charge_efficiency; uncalibrated research model",damage_model="single contact-step impulse threshold; uncalibrated research estimate")


def run_one(project:Project,duration:float):
    session=Session(project)
    session.status="running"
    session.step(round(duration/project.physics.timestep))
    if session.status!="failed":session.status="paused"
    return dict(run_id=session.run_id,status=session.status,manifest=manifest(project),metrics=session.metrics(),events=session.events,final_qpos=session.world.data.qpos.tolist(),tasks=session.orchestrator.task_rows(),recording=session.recording())


def compare(project:Project,seeds:list[int],policies:list[Policy],duration:float,root:Path):
    exp_id=uuid4().hex[:12]
    results=[]
    for policy in policies:
        policy_hash=hashlib.sha256(json.dumps(policy.model_dump(),sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
        for seed in seeds:
            copy=project.model_copy(deep=True);copy.physics.seed=seed;copy.policy=policy.model_copy(deep=True)
            result=run_one(copy,duration)
            folder=root/exp_id
            folder.mkdir(parents=True,exist_ok=True)
            (folder/f"run-{result['run_id']}.json").write_text(json.dumps(result,ensure_ascii=False),encoding="utf-8")
            results.append(dict(run_id=result["run_id"],policy=policy.name,policy_id=policy.id,policy_version=policy.version,policy_sha256=policy_hash,seed=seed,metrics=result["metrics"],input_sha256=result["manifest"]["input_sha256"]))
    groups=[]
    for policy in policies:
        policy_hash=hashlib.sha256(json.dumps(policy.model_dump(),sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
        if any(group["policy_sha256"]==policy_hash for group in groups):continue
        rows=[r["metrics"] for r in results if r["policy_sha256"]==policy_hash]
        summary={}
        for metric in ("completed","collisions","distance_m","energy_j","physics_realtime_factor","facility_queue_wait_seconds","charging_queue_wait_seconds","facility_fault_seconds"):
            values=[r[metric] for r in rows if r.get(metric) is not None]
            summary[metric]=dict(mean=statistics.mean(values),stddev=statistics.stdev(values) if len(values)>1 else None,n=len(values)) if values else None
        summary.update(_recovery_summary(rows))
        groups.append(dict(policy_id=policy.id,name=policy.name,policy_version=policy.version,policy_sha256=policy_hash,metrics=summary))
    result=dict(id=exp_id,name=project.name,duration=duration,seeds=seeds,runs=results,summary=groups,limitations=["실제 장비 보정 전 결과", "단일 시드는 변동성 추정 불가", "서로 다른 fidelity 결과는 같은 정확도로 간주하지 않음"])
    (root/exp_id/"summary.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    return result


def to_csv(result):
    stream=io.StringIO();fields=["run_id","policy","policy_id","policy_version","policy_sha256","seed","completed","failed","success_rate","distance_m","energy_j","charging_input_j","charging_stored_j","unserved_energy_j","collisions","falls","physics_realtime_factor","facility_queue_wait_seconds","charging_queue_wait_seconds","facility_fault_seconds",*RECOVERY_FIELDS]
    writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader()
    for run in result["runs"]:
        row={k:run.get(k,run["metrics"].get(k)) for k in fields}
        row.update(_recovery_metrics(run["metrics"]))
        writer.writerow(row)
    return stream.getvalue()
