#!/usr/bin/env python3
"""대상 선정 (사양서 7.1 · 7.3 · 8.2, 규칙 데이터는 config/rotation.yaml · config/priority.yaml).

선정 순서(rotation.precedence, 위에서 아래로 처음 맞는 규칙):
  track_day → monthly_recheck → weekly_review → priority → cycle1 → cycle2
- track_day: 오늘 요일이 track_days(주당 트랙 실행 횟수만큼 앞에서부터)에 있고 활성 트랙이 있으면 트랙 실행.
  트랙이 여럿이면 번갈아(직전 트랙 실행의 다음 트랙). 현재 단계와 이번에 다룰 백로그 질문 id 1~3개를 고른다:
  priority.track_questions 지정 → 앞 단계로 되돌아온 질문(stage < current_stage 이고 열림) → 오래된 순.
- monthly_recheck: 이달 첫 실행(이전 실행이 있을 때만; 트랙 실행일과 겹쳐 미뤄진 경우 다음 비트랙 실행). '이달 첫 실행'은 게시까지 간
  비트랙 실행(CLI 로 run_type 을 지정한 드라이런·재현 실행 포함) 또는 monthly_recheck 실행으로 센다. 중단·보류된 실행과 트랙 실행은
  세지 않는다 [가정 — 사용자 결정 항목, RUN.md 9절].
- weekly_review: 매 weekly_review_every(7)번째 실행(미뤄진 경우 포함). 실행 번호는 runs/ 와 runs/parked/ 의 실행 id 수.
- priority: priority.yaml 의 areas·topics·questions(최근 skip_if_targeted_within_days 안에 다룬 항목은 건너뜀).
- cycle1: status seed 인 최저 번호 세부영역 → area_deep_dive.
- cycle2: 점수 = 마지막 갱신 경과일 + 열린 질문 수 + 비어 있는 매트릭스 칸 수 + 우선 가중치 − 최근 7일 감점, 동점이면 번호순 → topic.
- 정정 요청(inbox/corrections.md 의 open 항목)이 있으면 그 페이지의 갱신을 당일 작업에 포함한다(target.json 의 corrections).
- 같은 영역이 exclude_after_consecutive_parks(3)회 연속 보류되면 대상 선정에서 제외하고 사용자 검토 요청을
  data/open_questions.json 에 올린다(priority.areas 에 지정하면 제외가 풀린다).

출력: runs/<run_id>/target.json
  {run_id, date, run_type, forced, target{area_no, area_name, category}, track{slug, stage, question_ids, …}|null,
   corrections[], budget{…}, selection_rationale, …}
CLI 오버라이드(드라이런용): --date, --run-type, --area, --track, --stage, --question-ids, --run-id, --stdout, --no-side-effects
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import frontmatter as fm  # noqa: E402
from lib import paths, runs  # noqa: E402
from lib.render import load_backlog, load_flow_matrix, load_open_questions  # noqa: E402
from lib.source import load_source  # noqa: E402

DEFAULT_PRECEDENCE = ["track_day", "monthly_recheck", "weekly_review", "priority", "cycle1", "cycle2"]
OPEN_STATES = ("열림", "조사 중")


# --- 이력 ------------------------------------------------------------------------------

def load_history(settings: dict) -> list[dict]:
    """runs/ 와 runs/parked/ 의 실행 이력(target.json + summary.json). 실행 id 순, number 는 1부터."""
    out = []
    for i, rid in enumerate(runs.list_run_ids(settings), start=1):
        d = runs.find_run_dir(rid, settings)
        t = runs.read_json(d / "target.json", {}) or {}
        s = runs.read_summary(d)
        tgt = t.get("target") or {}
        out.append({
            "run_id": rid, "number": i, "date": t.get("date") or rid[:10], "run_type": t.get("run_type") or s.get("run_type"),
            "area_no": tgt.get("area_no"), "track": (t.get("track") or {}).get("slug") if t.get("track") else None,
            "topic": t.get("topic"), "priority_questions": t.get("priority_questions") or [],
            "parked": bool(s.get("parked")) or runs.is_parked(rid, settings), "published": bool(s.get("published")),
            "forced": bool(t.get("forced")),   # CLI 로 run_type 을 지정한 실행(드라이런·재현). 기록용이며 '이달 첫 실행' 판정에서 빼지 않는다
        })
    return out


def _within_days(h_date: str, day: str, days: int) -> bool:
    try:
        d0, d1 = date.fromisoformat(h_date), date.fromisoformat(day)
    except ValueError:
        return False
    return d1 - timedelta(days=days) <= d0 < d1


# --- 세부영역 상태·제외 ---------------------------------------------------------------------

def area_statuses() -> dict[int, dict]:
    out = {}
    for no in paths.AREA_NOS:
        try:
            meta, _ = fm.read(paths.area_file(no))
        except Exception:
            meta = {}
        out[no] = meta
    return out


def excluded_areas(history: list[dict], rotation: dict, priority: dict) -> list[int]:
    n = int(rotation.get("exclude_after_consecutive_parks") or 3)
    lifted = {int(a.get("area_no")) for a in priority.get("areas", []) if str(a.get("area_no", "")).isdigit()}
    out = []
    for no in paths.AREA_NOS:
        mine = [h for h in history if h.get("run_type") != "track" and h.get("area_no") == no]
        streak = 0
        for h in reversed(mine):
            if h["parked"]:
                streak += 1
            else:
                break
        if streak >= n and no not in lifted:
            out.append(no)
    return out


def register_review_requests(excluded: list[int], day: str, run_id: str, rotation: dict) -> list[str]:
    """제외된 영역마다 사용자 검토 요청을 data/open_questions.json 에 올린다(이미 있으면 건너뜀). 등록한 id 목록."""
    src = load_source()
    p = paths.DATA / "open_questions.json"
    data = runs.read_json(p, {"items": []}) or {"items": []}
    items = data.setdefault("items", [])
    n = int(rotation.get("exclude_after_consecutive_parks") or 3)
    added = []
    for no in excluded:
        marker = f"사용자 검토 요청: {src.area(no).title}"
        if any(str(q.get("question", "")).startswith(marker) and q.get("status") in OPEN_STATES + ("보류",) for q in items):
            continue
        nums = [int(m.group(1)) for q in items for m in [re.match(r"^oq-(\d+)$", str(q.get("id", "")))] if m]
        qid = f"oq-{(max(nums) + 1) if nums else 1:03d}"
        items.append({
            "id": qid,
            "question": f"{marker} 이 {n}회 연속 보류(runs/parked/)되어 대상 선정에서 제외했다. 보류 사유를 검토하고 재투입·폐기 여부와 조사 힌트를 정한 뒤, 다시 다루려면 config/priority.yaml 의 areas 에 지정한다(사양서 7.3).",
            "areas": [no], "raised": day, "run_id": run_id, "status": "열림", "link": None,
        })
        added.append(qid)
    if added:
        runs.write_json(p, data)
    return added


# --- 트랙 ------------------------------------------------------------------------------

def active_tracks(settings: dict) -> list[tuple[str, dict]]:
    out = []
    for slug in settings.get("tracks") or []:
        cfg = runs.load_track_config(str(slug))
        if cfg and str(cfg.get("status", "active")) == "active":
            out.append((str(slug), cfg))
    return out


def track_runs_per_week(settings: dict, tracks: list[tuple[str, dict]]) -> tuple[int, list[str]]:
    warnings = []
    vals = []
    for slug, cfg in tracks:
        v = cfg.get("runs_per_week")
        if v not in (None, ""):
            vals.append(int(v))
    default = int(settings.get("track_runs_per_week") or 2)
    if not vals:
        return default, warnings
    if len(set(vals)) > 1:
        warnings.append(f"활성 트랙의 runs_per_week 가 서로 다르다 {vals}: 가장 큰 값을 쓴다")
    return max(vals), warnings


def is_track_day(day: str, rotation: dict, rpw: int) -> tuple[bool, list[str]]:
    warnings = []
    if rpw >= 7:
        return True, warnings
    days = [str(x) for x in (rotation.get("track_days") or [])]
    if len(days) < rpw:
        warnings.append(f"track_days({days})가 주당 트랙 실행 횟수({rpw})보다 짧다: 있는 요일만 쓴다")
    use = days[:rpw]
    return runs.weekday_name(day) in use, warnings


def pick_track(settings: dict, tracks: list[tuple[str, dict]], history: list[dict], override: str | None) -> tuple[str, dict]:
    if override:
        cfg = runs.load_track_config(override)
        if not cfg:
            raise SystemExit(f"[select_target] 트랙 정의 없음: config/tracks/{override}.yaml")
        return override, cfg
    slugs = [s for s, _ in tracks]
    last = next((h["track"] for h in reversed(history) if h.get("run_type") == "track" and h.get("track") in slugs), None)
    if last is None or len(slugs) == 1:
        return tracks[0]
    idx = (slugs.index(last) + 1) % len(slugs)
    return tracks[idx]


def _prio_rank(v) -> int:
    return {"high": 0, "normal": 1, "low": 2}.get(str(v or "normal").lower(), 1)


def pick_track_questions(slug: str, cfg: dict, priority: dict, stage: int, override_ids: list[str] | None,
                         max_n: int = 3) -> tuple[list[str], list[str], str]:
    backlog = load_backlog(slug)
    by_id = {b.get("id"): b for b in backlog}
    if override_ids:
        return [q for q in override_ids if q], [], "CLI 지정 질문 id"
    open_items = [b for b in backlog if b.get("status") in OPEN_STATES]
    user_qs = [q for q in priority.get("track_questions", []) if str(q.get("track", "")) == slug]
    user_qs.sort(key=lambda q: _prio_rank(q.get("priority")))  # 안정 정렬: 같은 우선순위면 파일 순
    chosen: list[str] = []
    unmatched: list[str] = []
    for q in user_qs:
        try:
            q_stage = int(q.get("stage") or stage)
        except (TypeError, ValueError):
            q_stage = stage
        if q_stage > stage:
            continue  # 뒤 단계의 사용자 질문은 그 단계가 될 때 다룬다 [가정]
        text = str(q.get("question", "")).strip()
        hit = by_id.get(q.get("id")) if q.get("id") else None
        if not hit:
            hit = next((b for b in backlog if str(b.get("question", "")).strip() == text), None)
        if hit and hit.get("status") in OPEN_STATES + ("보류",):
            if hit["id"] not in chosen:
                chosen.append(hit["id"])
        elif not hit and text:
            unmatched.append(text)
    def _age(b):
        return (str(b.get("created") or ""), str(b.get("id") or ""))
    returned = sorted((b for b in open_items if int(b.get("stage") or 0) < stage), key=_age)
    current = sorted((b for b in open_items if int(b.get("stage") or 0) == stage), key=_age)
    for b in returned + current:
        if b["id"] not in chosen:
            chosen.append(b["id"])
    rationale = (f"사용자 지정 {sum(1 for c in chosen[:max_n] if any(str(q.get('question','')).strip() == str(by_id.get(c, {}).get('question','')).strip() or q.get('id') == c for q in user_qs))}건, "
                 f"되돌아온 질문 {sum(1 for c in chosen[:max_n] if int(by_id.get(c, {}).get('stage') or 0) < stage)}건, "
                 f"현재 단계 열린 질문 {len(current)}건 중 오래된 순")
    return chosen[:max_n], unmatched, rationale


# --- 우선 지정·주기 -------------------------------------------------------------------------

def pick_priority(priority: dict, rotation: dict, history: list[dict], day: str, statuses: dict[int, dict],
                  excluded: list[int]) -> dict | None:
    pr = rotation.get("priority") or {}
    skip_days = int(pr.get("skip_if_targeted_within_days") or 7)
    qw = float(pr.get("question_weight") or 3)
    recent = [h for h in history if h.get("run_type") != "track" and _within_days(h["date"], day, skip_days)]
    cands = []
    for i, a in enumerate(priority.get("areas", [])):
        no = a.get("area_no")
        if not str(no).isdigit() or not 1 <= int(no) <= 28:
            continue
        no = int(no)
        if any(h.get("area_no") == no for h in recent):
            continue
        cands.append((float(a.get("weight") or 0), 0, i, {"kind": "areas", "area_no": no, "reason": a.get("reason"), "weight": a.get("weight")}))
    for i, t in enumerate(priority.get("topics", [])):
        no = t.get("area_no")
        if not str(no).isdigit() or not 1 <= int(no) <= 28 or not t.get("title"):
            continue
        if any(h.get("topic") == t.get("title") for h in recent):
            continue
        cands.append((float(t.get("weight") or 0), 1, i, {"kind": "topics", "area_no": int(no), "title": t.get("title"), "weight": t.get("weight")}))
    for i, q in enumerate(priority.get("questions", [])):
        no = q.get("area_no")
        if not str(no).isdigit() or not 1 <= int(no) <= 28 or not q.get("question"):
            continue
        if any(q.get("question") in (h.get("priority_questions") or []) for h in recent):
            continue
        cands.append((qw, 2, i, {"kind": "questions", "area_no": int(no), "question": q.get("question"), "weight": qw}))
    if not cands:
        return None
    cands.sort(key=lambda c: (-c[0], c[1], c[2]))
    _, _, _, item = cands[0]
    no = item["area_no"]
    if item["kind"] != "areas" and no in excluded:
        # 제외 영역은 areas 지정으로만 풀린다 [가정]
        return None
    seed = statuses.get(no, {}).get("status") == "seed"
    rt = "topic" if item["kind"] == "topics" else ("area_deep_dive" if seed else "topic")
    item["run_type"] = rt
    item["questions"] = [q.get("question") for q in priority.get("questions", []) if q.get("area_no") == no and q.get("question")]
    return item


def cycle1_pick(statuses: dict[int, dict], rotation: dict, excluded: list[int]) -> int | None:
    order = [int(x) for x in ((rotation.get("cycle1") or {}).get("order") or paths.AREA_NOS)]
    for no in order:
        if no in excluded:
            continue
        if statuses.get(no, {}).get("status") == "seed":
            return no
    return None


def cycle2_scores(statuses: dict[int, dict], rotation: dict, priority: dict, history: list[dict], day: str,
                  excluded: list[int]) -> list[tuple[float, int, dict]]:
    sc = rotation.get("scoring") or {}
    w = sc.get("weights") or {}
    w_days, w_oq, w_cells, w_pri = (float(w.get(k, 1)) for k in ("days_since_update", "open_questions", "empty_matrix_cells", "priority_weight"))
    pen_days = int(sc.get("recent_penalty_days") or 7)
    pen = float(sc.get("recent_penalty") or 5)
    qw = float((rotation.get("priority") or {}).get("question_weight") or 3)
    oq = load_open_questions()
    fmx = load_flow_matrix()
    total_cells = len(fmx["steps"]) * len(fmx["items"])
    recent_areas = {h.get("area_no") for h in history if h.get("run_type") != "track" and _within_days(h["date"], day, pen_days)}
    out = []
    for no in paths.AREA_NOS:
        if no in excluded:
            continue
        meta = statuses.get(no, {})
        try:
            days = (date.fromisoformat(day) - date.fromisoformat(str(meta.get("updated")))).days
        except (TypeError, ValueError):
            days = 0
        n_oq = sum(1 for q in oq if q.get("status") in OPEN_STATES and no in [int(x) for x in (q.get("areas") or []) if str(x).isdigit()])
        mine = paths.area_repo_path(no)
        filled = sum(1 for v in fmx["cells"].values() if any(str(e.get("link", "")).split("#")[0] == mine for e in (v or [])))
        empty = total_cells - filled
        pw = sum(float(a.get("weight") or 0) for a in priority.get("areas", []) if a.get("area_no") == no)
        pw += sum(float(t.get("weight") or 0) for t in priority.get("topics", []) if t.get("area_no") == no)
        pw += qw * sum(1 for q in priority.get("questions", []) if q.get("area_no") == no)
        penalty = pen if no in recent_areas else 0.0
        score = w_days * days + w_oq * n_oq + w_cells * empty + w_pri * pw - penalty
        out.append((score, no, {"days_since_update": days, "open_questions": n_oq, "empty_matrix_cells": empty,
                                "priority_weight": pw, "recent_penalty": penalty, "score": score}))
    out.sort(key=lambda x: (-x[0], x[1]))
    return out


def periodic_due(history: list[dict], run_number: int, day: str, rotation: dict) -> tuple[bool, bool, bool, bool]:
    """(monthly_due, monthly_deferred, weekly_due, weekly_deferred)."""
    every = int(rotation.get("weekly_review_every") or 7)
    prev = [h for h in history if h["number"] < run_number]
    this_month = [h for h in prev if str(h["date"])[:7] == day[:7]]
    # 월간 재검증(7.1 "매월 첫 실행"): 이달의 이전 실행 가운데 '이달 첫 실행'으로 셀 수 있는 것 — 게시(published)까지 간 비트랙 실행
    # 또는 run_type 이 monthly_recheck 인 실행 — 이 없으면 due 다. 준비·검증 단계에서 중단·보류된 실행(published false, run_type 이
    # 비어 있거나 기본값)과 트랙 실행은 이달 첫 실행으로 세지 않는다(트랙 실행뿐이면 미뤄진 것). CLI 로 run_type 을 지정한 실행(forced,
    # 9장 단계 3 의 드라이런)도 게시까지 갔으면 이달 첫 실행으로 센다 — 빼면 드라이런 뒤 첫 정규 비트랙 실행이 재검증할 게시 페이지가
    # 거의 없는 상태에서 월간 재검증이 되어 1주기 시작이 하루 늦어진다 [가정 — 사용자 결정 항목, RUN.md 9절].
    counted = [h for h in this_month
               if h.get("run_type") == "monthly_recheck"
               or (h.get("published") and h.get("run_type") != "track")]
    monthly = False
    monthly_deferred = False
    if prev and not counted:
        monthly = True
        monthly_deferred = bool(this_month)
    weekly = False
    weekly_deferred = False
    k = (run_number // every) * every
    if k >= every and not any(h.get("run_type") == "weekly_review" and h["number"] >= k for h in prev):
        weekly = True
        weekly_deferred = k != run_number
    return monthly, monthly_deferred, weekly, weekly_deferred


# --- 정정 요청 -------------------------------------------------------------------------------

def corrections_for(run_type: str, rotation: dict, budget: dict) -> tuple[list[dict], list[str]]:
    cfg = rotation.get("corrections") or {}
    notes = []
    if not cfg.get("include_update", True):
        return [], notes
    applies = cfg.get("applies_to") or ["area_deep_dive", "topic", "update", "monthly_recheck"]
    opened = runs.open_corrections()
    if not opened:
        return [], notes
    if run_type not in applies:
        notes.append(f"정정 요청 {len(opened)}건은 실행 유형 {run_type} 에 붙이지 않는다(applies_to 밖)")
        return [], notes
    limit = int(budget.get("page_updates") or 2)
    out, pages = [], []
    for c in opened:
        if c["page"] not in pages:
            if len(pages) >= limit:
                notes.append(f"정정 요청 {c['id']} 는 하루 갱신 상한({limit})을 넘어 다음 실행으로 넘긴다")
                continue
            pages.append(c["page"])
        out.append({"id": c["id"], "page": c["page"], "sentence": c["sentence"], "evidence": c["evidence"], "requested": c["requested"]})
    return out, notes


# --- 선정 -----------------------------------------------------------------------------

def select(day: str, run_id: str, settings: dict, rotation: dict, priority: dict, history: list[dict],
           override: dict, side_effects: bool = True) -> dict:
    src = load_source()
    statuses = area_statuses()
    excluded = excluded_areas(history, rotation, priority)
    notes: list[str] = []
    review_ids: list[str] = []
    if excluded and side_effects:
        review_ids = register_review_requests(excluded, day, run_id, rotation)
    if excluded:
        notes.append(f"3회 연속 보류로 제외한 영역: {', '.join(src.area(n).title for n in excluded)}" + (f" (열린 질문 {', '.join(review_ids)} 등록)" if review_ids else ""))

    all_ids = sorted(set(runs.list_run_ids(settings)) | {run_id})
    run_number = all_ids.index(run_id) + 1
    monthly, monthly_def, weekly, weekly_def = periodic_due(history, run_number, day, rotation)

    tracks = active_tracks(settings)
    rpw, w = track_runs_per_week(settings, tracks)
    notes += w
    track_today, w = is_track_day(day, rotation, rpw) if tracks else (False, [])
    notes += w

    precedence = [str(x) for x in (rotation.get("precedence") or DEFAULT_PRECEDENCE)]
    forced = override.get("run_type")
    run_type: str | None = None
    area_no: int | None = None
    topic: str | None = None
    track_block: dict | None = None
    prio_reason = None
    prio_questions: list[str] = []
    why = ""

    def area_target(no):
        return runs.area_of(no)

    def do_track():
        nonlocal track_block, area_no, why
        if not tracks and not override.get("track"):
            raise SystemExit("[select_target] 활성 트랙이 없다")
        slug, cfg = pick_track(settings, tracks, history, override.get("track"))
        stage = int(override.get("stage") or cfg.get("current_stage") or 1)
        qids, unmatched, qwhy = pick_track_questions(slug, cfg, priority, stage, override.get("question_ids"))
        names = cfg.get("stage_names") or {}
        track_block = {"slug": slug, "name": cfg.get("name"), "stage": stage, "stages": int(cfg.get("stages") or 7),
                       "stage_name": names.get(stage) or names.get(str(stage)) or "", "question_ids": qids,
                       "user_questions": unmatched, "runs_per_week": rpw, "question_rationale": qwhy}
        area_no = int(override.get("area") or cfg.get("primary_area") or 5)
        why = f"트랙 실행일({runs.weekday_name(day)}, track_days 앞 {rpw}개) → 트랙 {slug} 단계 {stage}, 질문 {', '.join(qids) or '없음'} ({qwhy})"

    if forced:
        run_type = forced
        if forced == "track":
            do_track()
        elif forced in ("weekly_review", "monthly_recheck"):
            area_no = int(override["area"]) if override.get("area") else None
        else:
            area_no = int(override["area"]) if override.get("area") else None
            if area_no is None:
                no = cycle1_pick(statuses, rotation, excluded)
                if no is None:
                    scores = cycle2_scores(statuses, rotation, priority, history, day, excluded)
                    no = scores[0][1] if scores else 1
                area_no = no
            topic = override.get("topic")
        why = f"CLI 지정 run_type={forced}" + (f", area={area_no}" if area_no else "") + (f"; {why}" if why else "")
    else:
        for rule in precedence:
            if rule == "track_day" and tracks and track_today:
                run_type = "track"
                do_track()
                if monthly or weekly:
                    notes.append("이달 첫 실행·매 7번째 실행이 트랙 실행일과 겹쳐 정기 실행을 다음 비트랙 실행으로 미룬다(deferred_periodic_runs)")
                break
            if rule == "monthly_recheck" and monthly:
                run_type = "monthly_recheck"
                why = "이달 첫 실행" + ("(트랙 실행일과 겹쳐 미뤄진 것)" if monthly_def else "") + " → 월간 재검증"
                break
            if rule == "weekly_review" and weekly:
                run_type = "weekly_review"
                why = f"{run_number}번째 실행(매 {rotation.get('weekly_review_every', 7)}번째" + (", 미뤄진 것" if weekly_def else "") + ") → 주간 정리"
                break
            if rule == "priority":
                if not (rotation.get("priority") or {}).get("overrides_rotation", True):
                    continue
                item = pick_priority(priority, rotation, history, day, statuses, excluded)
                if item:
                    run_type = item["run_type"]
                    area_no = item["area_no"]
                    topic = item.get("title") or (item.get("question") if item["kind"] == "questions" and run_type == "topic" else None)
                    prio_reason = item.get("reason") or f"priority.yaml {item['kind']} 지정"
                    prio_questions = item.get("questions") or []
                    why = f"우선 지정({item['kind']}, 가중치 {item.get('weight')}) → {run_type}"
                    break
            if rule == "cycle1":
                no = cycle1_pick(statuses, rotation, excluded)
                if no is not None:
                    run_type = str((rotation.get("cycle1") or {}).get("run_type") or "area_deep_dive")
                    area_no = no
                    why = f"1주기: status seed 인 최저 번호 영역 → {run_type}"
                    break
            if rule == "cycle2":
                scores = cycle2_scores(statuses, rotation, priority, history, day, excluded)
                if scores:
                    run_type = str((rotation.get("cycle2") or {}).get("default_run_type") or "topic")
                    area_no = scores[0][1]
                    det = scores[0][2]
                    prio_questions = [q.get("question") for q in priority.get("questions", []) if q.get("area_no") == area_no and q.get("question")]
                    why = (f"2주기 점수 최고 영역(점수 {det['score']:.0f} = 경과일 {det['days_since_update']} + 열린 질문 {det['open_questions']} "
                           f"+ 빈 매트릭스 칸 {det['empty_matrix_cells']} + 우선 가중치 {det['priority_weight']:.0f} − 최근 감점 {det['recent_penalty']:.0f}) → {run_type}")
                    break
        if run_type is None:
            raise SystemExit("[select_target] 어느 규칙에도 맞지 않아 대상을 정하지 못했다(제외 영역이 전부인가?)")

    track_cfg = runs.load_track_config(track_block["slug"]) if track_block else None
    budget = runs.budget_for(settings, run_type, track_cfg)
    corrections, cn = corrections_for(run_type, rotation, budget)
    notes += cn
    target = area_target(area_no) if area_no else {"area_no": None, "area_name": None, "category": None}
    return {
        "run_id": run_id, "date": day, "weekday": runs.weekday_name(day), "run_number": run_number,
        "run_type": run_type, "forced": bool(forced), "target": target, "topic": topic, "track": track_block,
        "corrections": corrections, "budget": budget,
        "priority_reason": prio_reason, "priority_questions": prio_questions,
        "excluded_areas": excluded,
        "deferred": {"monthly_recheck": monthly and run_type == "track", "weekly_review": weekly and run_type == "track"},
        "selection_rationale": why + ((" · " + " · ".join(notes)) if notes else ""),
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", help="실행 날짜 YYYY-MM-DD (기본: settings.timezone 의 오늘 또는 ROP_TODAY)")
    ap.add_argument("--run-id", help="실행 id(기본: <date>-<NN> 자동 부여)")
    ap.add_argument("--run-type", choices=runs.RUN_TYPES)
    ap.add_argument("--area", type=int, help="세부영역 번호 1~28")
    ap.add_argument("--track", help="트랙 slug")
    ap.add_argument("--stage", type=int, help="트랙 단계")
    ap.add_argument("--question-ids", help="쉼표로 구분한 백로그 질문 id (예 q1-01,q1-02)")
    ap.add_argument("--topic", help="주제 제목(run_type topic 지정 시)")
    ap.add_argument("--out", help="출력 경로(기본 runs/<run_id>/target.json)")
    ap.add_argument("--stdout", action="store_true", help="파일에 쓰지 않고 표준 출력에만 낸다")
    ap.add_argument("--no-side-effects", action="store_true", help="data/open_questions.json 에 검토 요청을 등록하지 않는다")
    args = ap.parse_args(argv)

    settings = runs.load_settings()
    rotation = runs.load_rotation()
    priority = runs.load_priority()
    day = args.date or runs.today(settings)
    if not runs.DATE_RE.match(day):
        print(f"[select_target] 날짜 형식 오류: {day}")
        return 2
    if args.area is not None and not 1 <= args.area <= 28:
        print(f"[select_target] 세부영역 번호 범위 밖: {args.area}")
        return 2
    run_id = args.run_id or runs.new_run_id(day, settings)
    history = load_history(settings)
    override = {"run_type": args.run_type, "area": args.area, "track": args.track, "stage": args.stage, "topic": args.topic,
                "question_ids": [q.strip() for q in args.question_ids.split(",")] if args.question_ids else None}
    target = select(day, run_id, settings, rotation, priority, history, override, side_effects=not (args.stdout or args.no_side_effects))
    text = json.dumps(target, ensure_ascii=False, indent=2)
    if args.stdout:
        print(text)
        return 0
    out = Path(args.out) if args.out else runs.run_dir(run_id, settings) / "target.json"
    runs.write_text(out, text + "\n")
    print(f"[select_target] {run_id} {target['run_type']}({runs.RUN_TYPE_KO.get(target['run_type'])}) "
          f"{target['target'].get('area_name') or '영역 없음'} → {out.relative_to(paths.ROOT) if out.is_absolute() else out}")
    print(f"[select_target] 근거: {target['selection_rationale']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
