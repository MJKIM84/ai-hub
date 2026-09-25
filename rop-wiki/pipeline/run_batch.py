#!/usr/bin/env python3
"""배치 실행기(운영 전환 3부): 여러 대상을 개선된 일일 파이프라인 7단계로 한 번에 처리한다.

각 항목은 run_daily.sh 를 그대로 쓴다(대상 선정 → 리서치 → 1차 검증 → 스토리텔러(+형식 검증) → 2차 검증 → 퍼블리셔 → 일일 로그).
에이전트 단계(--until verify2)는 여러 항목을 동시에 돌리고, 퍼블리셔는 하나씩 차례로 부른다(publish.py 전역 잠금 + 이 실행기의 직렬 큐).
같은 group 의 항목(예: 같은 트랙)은 앞 항목이 게시된 뒤에 시작한다(백로그·단계가 앞 실행 결과에 달려 있기 때문).

  python3 pipeline/run_batch.py --plan plan.yaml [--concurrency 4] [--allow-no-fetch] [--max-attempts 3] [--dry-run]

plan.yaml: 항목 목록. 각 항목 키: run_type(필수), area, track, stage, question_ids, max_questions, category, topic, group, label,
  resume(이미 만든 실행 id — 에이전트 단계가 끝나기를 기다렸다가 게시만 한다. 배치를 다시 띄울 때 쓴다),
  continue(멈추거나 호출 오류로 보류된 실행 id — 있는 산출물부터 이어서 2차 검증까지 하고 게시한다).
퍼블리셔가 실패하면 게시만 한 번 다시 하고, 그래도 실패하면 항목을 새로 실행한다.
결과: runs/batches/<batch_id>.json (항목별 실행 id·상태·시도 횟수·비용·소요 시간) 과 표준 출력 요약.
한 항목이 max_attempts 번 연속 실패(보류·중단)하면 보류로 기록하고 다음 항목으로 넘어간다. 전체 배치는 멈추지 않는다.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import yaml  # noqa: E402

from lib import paths, runs  # noqa: E402

ROOT = paths.ROOT
_ID_LOCK = threading.Lock()


def _now() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def say(msg: str) -> None:
    print(f"[run_batch {_now()}] {msg}", flush=True)


def reserve_run_id(day: str, settings: dict) -> str:
    """다음 실행 id 를 폴더 생성으로 예약한다. 같은 프로세스 안은 잠금으로, 다른 프로세스(동시에 도는 배치·run_daily.sh)와는
    mkdir 의 원자성으로 겹침을 막는다 — 이미 있으면 다음 번호를 다시 계산한다."""
    with _ID_LOCK:
        for _ in range(50):
            rid = runs.new_run_id(day, settings)
            try:
                (runs.runs_root(settings) / rid).mkdir(parents=True, exist_ok=False)
                return rid
            except FileExistsError:
                time.sleep(0.2)
        raise RuntimeError("실행 id 예약 실패(50회 충돌)")


def item_args(it: dict) -> list[str]:
    a = ["--run-type", str(it["run_type"])]
    for key, flag in (("area", "--area"), ("track", "--track"), ("stage", "--stage"), ("category", "--category"),
                      ("max_questions", "--max-questions")):
        if it.get(key) not in (None, ""):
            a += [flag, str(it[key])]
    if it.get("question_ids"):
        q = it["question_ids"]
        a += ["--question-ids", ",".join(q) if isinstance(q, list) else str(q)]
    return a


class Batch:
    def __init__(self, plan: list[dict], args, settings: dict):
        self.plan = plan
        self.args = args
        self.settings = settings
        self.day = args.date or runs.today(settings)
        self.batch_id = args.batch_id or f"batch-{time.strftime('%Y%m%d-%H%M%S')}"
        self.dir = ROOT / "runs" / "batches"
        self.dir.mkdir(parents=True, exist_ok=True)
        self.report_path = self.dir / f"{self.batch_id}.json"
        self.results: list[dict] = [{"index": i, "label": it.get("label") or self._label(it), "item": it, "status": "대기",
                                     "attempts": [], "run_id": None} for i, it in enumerate(plan)]
        self.lock = threading.Lock()
        self.publish_q: list[tuple[int, str]] = []
        self.publish_cv = threading.Condition(self.lock)
        self.group_busy: dict[str, bool] = {}
        self.pending = list(range(len(plan)))
        self.active = 0
        self.done_count = 0
        self.probe_file = self.dir / f"{self.batch_id}.probe.json"

    @staticmethod
    def _label(it: dict) -> str:
        parts = [str(it.get("run_type"))]
        for k in ("area", "track", "category", "question_ids"):
            if it.get(k):
                parts.append(f"{k}={it[k]}")
        return " ".join(parts)

    def save(self) -> None:
        with self.lock:
            data = {"batch_id": self.batch_id, "date": self.day, "updated": _now(), "concurrency": self.args.concurrency,
                    "items": self.results}
        runs.write_json(self.report_path, data)

    # --- 준비: 웹 도구 점검은 배치에서 한 번만 한다 -------------------------------------------
    def probe(self) -> None:
        if self.args.probe_file and Path(self.args.probe_file).is_file():
            shutil.copy(self.args.probe_file, self.probe_file)
            say(f"웹 도구 점검 결과 재사용: {self.args.probe_file}")
            return
        say("웹 도구 점검(배치 1회)")
        subprocess.run([sys.executable, "pipeline/agent_runner.py", "probe", "--out", str(self.probe_file)], cwd=str(ROOT),
                       check=False, capture_output=True, text=True)
        say(f"점검 결과: {self.probe_file.read_text(encoding='utf-8')[:300] if self.probe_file.is_file() else '없음'}")

    # --- 항목 실행 -------------------------------------------------------------------------------
    @staticmethod
    def _run_alive(rid: str) -> bool:
        """그 실행 id 로 도는 run_daily.sh 가 있는가(배치를 다시 띄울 때 넘겨받은 실행의 에이전트 단계가 끝났는지 본다)."""
        p = subprocess.run(["pgrep", "-f", f"run_daily.sh .*--run-id {rid}( |$)"], capture_output=True, text=True)
        return bool((p.stdout or "").strip())

    def _adopt(self, idx: int, rid: str) -> None:
        """plan 항목의 resume: 이미 만든 실행(에이전트 단계 진행 중이거나 끝남)을 넘겨받아 에이전트를 다시 돌리지 않고 게시한다."""
        res = self.results[idx]
        att = {"run_id": rid, "started": _now(), "agents_exit": None, "publish_exit": None, "adopted": True}
        with self.lock:
            res["attempts"].append(att)
            res["run_id"] = rid
            res["status"] = "넘겨받은 실행 대기"
        self.save()
        say(f"[{idx}] {res['label']} → 기존 실행 {rid} 를 넘겨받음(에이전트 단계가 끝나기를 기다린다)")
        while self._run_alive(rid):
            time.sleep(15)
        rd = runs.find_run_dir(rid, self.settings)
        ok = bool(rd) and (rd / "verification2.json").is_file() and not runs.is_parked(rid, self.settings)
        att["agents_exit"] = 0 if ok else 2
        att["agents_done"] = _now()
        if ok:
            with self.lock:
                res["status"] = "퍼블리셔 대기"
                self.publish_q.append((idx, rid))
                self.publish_cv.notify_all()
            say(f"[{idx}] {rid} 넘겨받은 실행의 에이전트 단계 완료 → 퍼블리셔 대기")
        else:
            say(f"[{idx}] {rid} 넘겨받은 실행이 2차 검증까지 끝나지 않았거나 보류됐다 — 새로 실행한다")
            self._after_attempt(idx, ok=False, why="넘겨받은 실행 미완료")
        self.save()

    def _run_agents(self, idx: int) -> None:
        it = self.plan[idx]
        res = self.results[idx]
        if it.get("resume") and not res["attempts"]:
            return self._adopt(idx, str(it["resume"]))
        cont = str(it["continue"]) if it.get("continue") and not res["attempts"] else None
        if cont:
            # continue: 멈춘(또는 호출 오류로 보류된) 실행을 있는 산출물부터 이어서 2차 검증까지 한다(run_daily.sh --resume)
            rid = cont
        else:
            rid = reserve_run_id(self.day, self.settings)
            shutil.copy(self.probe_file, ROOT / "runs" / rid / "probe.json")
        att = {"run_id": rid, "started": _now(), "agents_exit": None, "publish_exit": None, "continued": bool(cont)}
        with self.lock:
            res["attempts"].append(att)
            res["run_id"] = rid
            res["status"] = "에이전트 단계 진행"
        self.save()
        if cont:
            cmd = ["bash", "pipeline/run_daily.sh", "--resume", rid, "--skip-probe", "--until", "verify2"]
        else:
            cmd = ["bash", "pipeline/run_daily.sh", "--date", self.day, "--run-id", rid, "--skip-probe", "--until", "verify2",
                   *item_args(it)]
        if self.args.allow_no_fetch:
            cmd.append("--allow-no-fetch")
        say(f"[{idx}] {res['label']} → {rid} 시작")
        log_path = self.dir / f"{self.batch_id}.{rid}.log"
        with open(log_path, "w", encoding="utf-8") as fh:
            p = subprocess.run(cmd, cwd=str(ROOT), stdout=fh, stderr=subprocess.STDOUT)
        att["agents_exit"] = p.returncode
        att["agents_done"] = _now()
        if p.returncode == 0:
            with self.lock:
                res["status"] = "퍼블리셔 대기"
                self.publish_q.append((idx, rid))
                self.publish_cv.notify_all()
            say(f"[{idx}] {rid} 에이전트 단계 완료 → 퍼블리셔 대기")
        else:
            why = {2: "보류(runs/parked/)", 3: "준비 단계 중단"}.get(p.returncode, f"실패(exit {p.returncode})")
            say(f"[{idx}] {rid} {why} — 로그 {log_path.name}")
            self._after_attempt(idx, ok=False, why=why)
        self.save()

    def _after_attempt(self, idx: int, ok: bool, why: str = "") -> None:
        it = self.plan[idx]
        res = self.results[idx]
        with self.lock:
            group = it.get("group")
            if ok:
                res["status"] = "게시"
                self.done_count += 1
                self.active -= 1
                if group:
                    self.group_busy[group] = False
            elif len(res["attempts"]) < self.args.max_attempts:
                res["status"] = f"재시도 대기({why})"
                self.pending.insert(0, idx)
                self.active -= 1
                if group:
                    self.group_busy[group] = False
            else:
                res["status"] = f"보류({self.args.max_attempts}회 연속 실패: {why})"
                self.done_count += 1
                self.active -= 1
                if group:
                    self.group_busy[group] = False
            self.publish_cv.notify_all()

    def _publisher_loop(self) -> None:
        while True:
            with self.lock:
                while not self.publish_q and self.done_count < len(self.plan):
                    self.publish_cv.wait(timeout=5)
                if not self.publish_q and self.done_count >= len(self.plan):
                    return
                idx, rid = self.publish_q.pop(0)
                self.results[idx]["status"] = "퍼블리셔 진행"
            say(f"[{idx}] {rid} 퍼블리셔 시작")
            log_path = self.dir / f"{self.batch_id}.{rid}.publish.log"
            with open(log_path, "w", encoding="utf-8") as fh:
                p = subprocess.run(["bash", "pipeline/run_daily.sh", "--resume", rid, "--step", "publish"], cwd=str(ROOT),
                                   stdout=fh, stderr=subprocess.STDOUT)
            if p.returncode != 0:
                # 퍼블리셔 실패는 먼저 게시만 한 번 다시 한다(일시적 원인 — 동시 파일 변화 등 — 이면 에이전트 단계를 다시 돌릴 필요가 없다).
                # 두 번째도 실패하면 이 시도를 실패로 보고 항목을 새로 실행한다
                say(f"[{idx}] {rid} 퍼블리셔 실패(exit {p.returncode}) — 게시만 한 번 다시 시도")
                time.sleep(15)
                with open(log_path, "a", encoding="utf-8") as fh:
                    fh.write("\n\n===== 게시 재시도 =====\n")
                    fh.flush()
                    p = subprocess.run(["bash", "pipeline/run_daily.sh", "--resume", rid, "--step", "publish"], cwd=str(ROOT),
                                       stdout=fh, stderr=subprocess.STDOUT)
            att = self.results[idx]["attempts"][-1]
            att["publish_exit"] = p.returncode
            att["published_at"] = _now()
            summ = runs.read_summary(ROOT / "runs" / rid)
            att["cost_usd"] = (summ.get("usage") or {}).get("cost_usd")
            att["duration_sec"] = summ.get("duration_sec")
            att["end_state"] = summ.get("end_state")
            if p.returncode == 0:
                say(f"[{idx}] {rid} 게시 완료 · 비용 ${att['cost_usd']} · 커밋 {summ.get('commit')}")
                self._after_attempt(idx, ok=True)
            else:
                say(f"[{idx}] {rid} 퍼블리셔 실패(exit {p.returncode}) — {log_path.name}")
                self._after_attempt(idx, ok=False, why=f"퍼블리셔 실패(exit {p.returncode})")
            self.save()

    def run(self) -> int:
        self.probe()
        self.save()
        pub = threading.Thread(target=self._publisher_loop, daemon=True)
        pub.start()
        workers: list[threading.Thread] = []
        while True:
            with self.lock:
                if self.done_count >= len(self.plan):
                    break
                start_idx = None
                if self.active < self.args.concurrency:
                    for i in list(self.pending):
                        g = self.plan[i].get("group")
                        if g and self.group_busy.get(g):
                            continue
                        start_idx = i
                        self.pending.remove(i)
                        self.active += 1
                        if g:
                            self.group_busy[g] = True
                        break
            if start_idx is not None:
                th = threading.Thread(target=self._run_agents, args=(start_idx,), daemon=True)
                th.start()
                workers.append(th)
                time.sleep(self.args.stagger)
                continue
            time.sleep(3)
        pub.join(timeout=60)
        self.save()
        ok = sum(1 for r in self.results if r["status"] == "게시")
        held = [r for r in self.results if r["status"].startswith("보류")]
        cost = sum(float(a.get("cost_usd") or 0) for r in self.results for a in r["attempts"])
        say(f"배치 완료: 게시 {ok}/{len(self.plan)} · 보류 {len(held)} · 비용 합계 ${cost:.2f} · 보고서 {self.report_path.relative_to(ROOT)}")
        for r in held:
            say(f"  보류: {r['label']} — {r['status']}")
        return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plan", required=True, help="항목 목록 YAML")
    ap.add_argument("--concurrency", type=int, default=4, help="에이전트 단계 동시 실행 수")
    ap.add_argument("--max-attempts", type=int, default=3, help="항목별 최대 시도 횟수(연속 실패 시 보류)")
    ap.add_argument("--allow-no-fetch", action="store_true", help="페이지 열람 도구가 전혀 없을 때도 진행(사용자 override)")
    ap.add_argument("--date", help="실행 날짜(기본 오늘)")
    ap.add_argument("--batch-id", help="배치 id(기본 batch-<시각>)")
    ap.add_argument("--probe-file", help="기존 probe.json 재사용")
    ap.add_argument("--stagger", type=float, default=20.0, help="항목 시작 간격(초) — 프롬프트 캐시 적중과 호출 몰림 완화")
    ap.add_argument("--dry-run", action="store_true", help="계획만 출력")
    args = ap.parse_args(argv)
    plan = yaml.safe_load(Path(args.plan).read_text(encoding="utf-8")) or []
    if isinstance(plan, dict):
        plan = plan.get("items") or []
    for i, it in enumerate(plan):
        if not isinstance(it, dict) or it.get("run_type") not in runs.RUN_TYPES:
            print(f"[run_batch] 항목 {i} 의 run_type 이 없거나 잘못됐다: {it}")
            return 2
    if args.dry_run:
        for i, it in enumerate(plan):
            print(f"{i:3d} {Batch._label(it)} group={it.get('group')}")
        return 0
    settings = runs.load_settings()
    return Batch(plan, args, settings).run()


if __name__ == "__main__":
    sys.exit(main())
