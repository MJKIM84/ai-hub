"""실행 산출물(runs/)·설정·실행 로그·요약·스키마 검사 도우미와 셸(run_daily.sh)용 CLI.

파이프라인 실행 스크립트(pipeline/run_daily.sh, select_target.py, agent_runner.py, publish.py,
render_run_md.py)가 함께 쓰는 공통 함수를 모은다. 기존 백본 라이브러리(paths, frontmatter,
autoregion, nav, render, source)는 고치지 않고 여기서만 import 해 쓴다.

폴더 규약(사양서 3장): runs/<DATE>-<NN>/ (target.json, research.json, research.md, verification.json,
verification.md, verification2.json, verification2.md, pages/, pages.json, prompts/, log.md, summary.json),
runs/parked/<DATE>-<NN>/ (보류 산출물). 이 모듈이 더 두는 파일 [가정]: timings.json(단계별 소요 시간),
probe.json(웹 도구 점검 결과), docs_tree.txt(docs/ 페이지 경로 목록), backup/(퍼블리셔 롤백용 스냅숏).

셸에서 쓰는 CLI (위키 루트에서):
  python3 pipeline/lib/runs.py today
  python3 pipeline/lib/runs.py new-run-id --date 2026-09-24
  python3 pipeline/lib/runs.py step --run-id <id> --step 리서치 --result 성공 --seconds 123 --note "…"
  python3 pipeline/lib/runs.py log --run-id <id> --msg "…" [--step 준비]
  python3 pipeline/lib/runs.py park --run-id <id> --reason "…"
  python3 pipeline/lib/runs.py unpark --run-id <id>        # 재투입: runs/parked/<id> → runs/<id>, summary 의 보류 표시 해제
  python3 pipeline/lib/runs.py jsonget --file runs/<id>/verification.json --key verdict [--default x]
  python3 pipeline/lib/runs.py jsonset --file runs/<id>/probe.json --set web_fetch_override=true …
  python3 pipeline/lib/runs.py setting --key daily_budget.max_retries
  python3 pipeline/lib/runs.py docs-tree --run-id <id>
  python3 pipeline/lib/runs.py run-dir --run-id <id>
  python3 pipeline/lib/runs.py summary --run-id <id> --set key=value …
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import shutil
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import yaml

try:  # 패키지(lib.runs)로 import 될 때
    from . import frontmatter as fm
    from . import paths
except ImportError:  # python3 pipeline/lib/runs.py 로 직접 실행될 때
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from lib import frontmatter as fm  # type: ignore
    from lib import paths  # type: ignore

ROOT = paths.ROOT
SCHEMA_DIR = ROOT / "schemas"
AGENTS_DIR = ROOT / "agents"
TEMPLATES_DIR = ROOT / "templates"
INBOX_CORRECTIONS = ROOT / "inbox" / "corrections.md"
EXPERIMENTS_DIR = ROOT / "experiments"

RUN_ID_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{2,}$")


def run_id_key(rid: str) -> tuple:
    """실행 id 정렬 키(날짜, 번호). 같은 날 100번째 실행(…-100)이 …-11 앞에 오지 않게 번호를 정수로 비교한다."""
    m = re.match(r"^(\d{4}-\d{2}-\d{2})-(\d+)$", str(rid))
    return (m.group(1), int(m.group(2))) if m else (str(rid), 0)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

RUN_TYPES = ["area_deep_dive", "topic", "update", "weekly_review", "monthly_recheck", "track", "category_link"]
RUN_TYPE_KO = {
    "area_deep_dive": "영역 심화", "topic": "주제 조사", "update": "갱신",
    "weekly_review": "주간 정리", "monthly_recheck": "월간 재검증", "track": "트랙 실행",
    "category_link": "대분류 연결",
}
# 일일 로그 "단계별 결과와 소요 시간" 표의 행 순서. "링크·출처 점검"은 주간 정리(7.1)에서 run_daily.sh 가 리서치 전에 수행하는 단계이며
# 실행되지 않은 날은 표에 행을 두지 않는다(OPTIONAL_STEPS)
STEP_NAMES = ["준비", "대상 선정", "링크·출처 점검", "리서치", "1차 검증", "스토리텔러", "형식 검증", "2차 검증", "퍼블리셔"]
OPTIONAL_STEPS = {"링크·출처 점검", "형식 검증"}
ROLES = ["researcher", "verifier", "storyteller"]
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

DEFAULT_SETTINGS: dict = {
    "wiki_name": "ROP 연구 위키",
    "tracks": ["manual-capability-ontology"],
    "track_runs_per_week": 2,
    "daily_budget": {
        "new_topic_pages": 1, "page_updates": 2, "max_sources_per_run": 15, "max_search_queries": 30,
        "max_retries": 2, "track_max_sources_per_run": 20, "track_max_search_queries": 40,
    },
    "notify": "none",
    "web_tools_required": True,
    "repo_root": "..",
    "claude_bin": "claude",
    "model": "",
    "max_turns": {"researcher": 60, "verifier": 40, "storyteller": 8},
    "agent_timeout_sec": 1800,
    "allowed_tools": {"researcher": ["WebSearch", "WebFetch"], "verifier": ["WebSearch", "WebFetch"], "storyteller": []},
    "site_build_cmd": "mkdocs build --strict",
    "git_commit": True,
    "git_push": False,
    "timezone": "Asia/Seoul",
    "web_fetch_probe_url": "https://ref.gs1.org/epcis/",
    "web_fetch_required": True,
    "runs_dir": "runs",
    "data_dir": "data",
}


# --- YAML·설정 ---------------------------------------------------------------------

def load_yaml(path: Path | str, default=None):
    p = Path(path)
    if not p.is_file():
        return default
    with p.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return default if data is None else data


def _merge(base: dict, over: dict) -> dict:
    out = copy.deepcopy(base)
    for k, v in (over or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _merge(out[k], v)
        else:
            out[k] = v
    return out


def load_settings() -> dict:
    """config/settings.yaml 을 읽어 기본값과 합친다. 파일이 없거나 YAML 오류면 예외(준비 단계에서 중단)."""
    p = paths.CONFIG / "settings.yaml"
    if not p.is_file():
        raise FileNotFoundError(f"설정 파일 없음: {p}")
    data = load_yaml(p, {})
    if not isinstance(data, dict):
        raise ValueError(f"설정 파일이 매핑이 아니다: {p}")
    return _merge(DEFAULT_SETTINGS, data)


def load_rotation() -> dict:
    return load_yaml(paths.CONFIG / "rotation.yaml", {}) or {}


def load_priority() -> dict:
    d = load_yaml(paths.CONFIG / "priority.yaml", {}) or {}
    for k in ("areas", "topics", "questions", "track_questions"):
        if not isinstance(d.get(k), list):
            d[k] = []
    return d


def load_track_config(slug: str) -> dict | None:
    p = paths.track_config(slug)
    return load_yaml(p, None) if p.is_file() else None


def repo_root(settings: dict | None = None) -> Path:
    settings = settings or load_settings()
    return (ROOT / str(settings.get("repo_root") or "..")).resolve()


def runs_root(settings: dict | None = None) -> Path:
    settings = settings or DEFAULT_SETTINGS
    return ROOT / str(settings.get("runs_dir") or "runs")


def parked_root(settings: dict | None = None) -> Path:
    return runs_root(settings) / "parked"


# --- 날짜·시각 ---------------------------------------------------------------------

def tzinfo(settings: dict | None = None):
    from zoneinfo import ZoneInfo
    name = (settings or DEFAULT_SETTINGS).get("timezone") or "Asia/Seoul"
    try:
        return ZoneInfo(str(name))
    except Exception:
        return ZoneInfo("UTC")


def today(settings: dict | None = None) -> str:
    """오늘(ISO). 환경변수 ROP_TODAY 가 있으면 그 값(재현·드라이런용). 없으면 settings.timezone 의 오늘."""
    env = os.environ.get("ROP_TODAY")
    if env and DATE_RE.match(env):
        return env
    return datetime.now(tzinfo(settings)).date().isoformat()


def now_str(settings: dict | None = None) -> str:
    return datetime.now(tzinfo(settings)).strftime("%Y-%m-%d %H:%M:%S %Z")


def weekday_name(iso: str) -> str:
    return WEEKDAYS[date.fromisoformat(iso).weekday()]


def iso_week(iso: str) -> str:
    y, w, _ = date.fromisoformat(iso).isocalendar()
    return f"{y}-W{w:02d}"


def fmt_duration(seconds) -> str:
    try:
        s = int(round(float(seconds)))
    except (TypeError, ValueError):
        return "미상"
    if s < 60:
        return f"{s}초"
    m, sec = divmod(s, 60)
    if m < 60:
        return f"{m}분 {sec}초"
    h, m = divmod(m, 60)
    return f"{h}시간 {m}분 {sec}초"


# --- 실행 id·폴더 -------------------------------------------------------------------

def list_run_ids(settings: dict | None = None, include_parked: bool = True) -> list[str]:
    ids: set[str] = set()
    root = runs_root(settings)
    if root.is_dir():
        for p in root.iterdir():
            if p.is_dir() and RUN_ID_RE.match(p.name):
                ids.add(p.name)
    if include_parked and parked_root(settings).is_dir():
        for p in parked_root(settings).iterdir():
            if p.is_dir() and RUN_ID_RE.match(p.name):
                ids.add(p.name)
    return sorted(ids, key=run_id_key)


def new_run_id(day: str, settings: dict | None = None) -> str:
    """<date>-<NN>. 같은 날 두 번째 실행은 02 (runs/ 와 runs/parked/ 를 함께 센다)."""
    n = 1
    existing = {i for i in list_run_ids(settings) if i.startswith(day + "-")}
    while f"{day}-{n:02d}" in existing:
        n += 1
    return f"{day}-{n:02d}"


def run_dir(run_id: str, settings: dict | None = None) -> Path:
    return runs_root(settings) / run_id


def parked_dir(run_id: str, settings: dict | None = None) -> Path:
    return parked_root(settings) / run_id


def find_run_dir(run_id: str, settings: dict | None = None) -> Path | None:
    for p in (run_dir(run_id, settings), parked_dir(run_id, settings)):
        if p.is_dir():
            return p
    return None


def is_parked(run_id: str, settings: dict | None = None) -> bool:
    return parked_dir(run_id, settings).is_dir()


def is_discarded(run_id: str, settings: dict | None = None) -> bool:
    """사용자가 폐기한 보류 실행인가(7.4 "재투입 또는 폐기"): runs/parked/<run_id>/DISCARDED 파일이 있다(RUN.md 5절).
    폐기한 실행의 브리프는 다음 실행의 입력(최근 실행의 research.md)에 넣지 않는다. 연속 보류 횟수에는 그대로 센다
    (제외 해제는 config/priority.yaml 의 areas 지정으로 한다) [가정]."""
    return (parked_dir(run_id, settings) / "DISCARDED").is_file()


# --- JSON·텍스트 ----------------------------------------------------------------------

def read_json(path: Path | str, default=None):
    p = Path(path)
    if not p.is_file():
        return default
    with p.open(encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path | str, data) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return p


def read_text(path: Path | str, default: str = "") -> str:
    p = Path(path)
    return p.read_text(encoding="utf-8") if p.is_file() else default


def write_text(path: Path | str, text: str) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def get_path(data, dotted: str, default=None):
    cur = data
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        elif isinstance(cur, list) and part.isdigit() and int(part) < len(cur):
            cur = cur[int(part)]
        else:
            return default
    return cur


# --- 실행 로그(log.md)·소요 시간(timings.json) -----------------------------------------------

class RunLog:
    """runs/<run_id>/log.md 에 시각과 함께 한 줄씩 덧붙이고, 단계별 소요 시간을 timings.json 에 남긴다."""

    def __init__(self, run_directory: Path, settings: dict | None = None):
        self.dir = Path(run_directory)
        self.path = self.dir / "log.md"
        self.timings_path = self.dir / "timings.json"
        self.settings = settings

    def ensure(self, run_id: str) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text(f"# 실행 로그 {run_id}\n\n", encoding="utf-8")

    def log(self, msg: str, step: str | None = None) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        tag = f"[{step}] " if step else ""
        line = f"- {now_str(self.settings)} {tag}{msg}\n"
        with self.path.open("a", encoding="utf-8") as f:
            f.write(line)

    def step(self, step: str, result: str, seconds=None, note: str = "") -> None:
        dur = fmt_duration(seconds) if seconds is not None else ""
        self.log(f"결과: {result}" + (f" · 소요 {dur}" if dur else "") + (f" · {note}" if note else ""), step=step)
        data = read_json(self.timings_path, {"steps": []}) or {"steps": []}
        data.setdefault("steps", []).append({
            "step": step, "result": result, "seconds": float(seconds) if seconds is not None else None,
            "note": note, "at": now_str(self.settings),
        })
        write_json(self.timings_path, data)

    def timings(self) -> dict[str, dict]:
        """단계 이름 → 마지막 기록(결과·소요·비고). 같은 단계가 여러 번이면 소요 시간은 합산하고 결과는 마지막 것."""
        out: dict[str, dict] = {}
        for it in (read_json(self.timings_path, {}) or {}).get("steps", []):
            name = it.get("step")
            prev = out.get(name)
            total = (prev.get("seconds") or 0 if prev else 0) + (it.get("seconds") or 0)
            notes = [n for n in ([prev.get("note")] if prev else []) if n]
            if it.get("note"):
                notes.append(it["note"])
            out[name] = {"result": it.get("result"), "seconds": total, "note": " / ".join(notes), "count": (prev.get("count", 0) if prev else 0) + 1}
        return out


# --- 요약(summary.json) ----------------------------------------------------------------

def read_summary(run_directory: Path) -> dict:
    return read_json(Path(run_directory) / "summary.json", {}) or {}


def write_summary(run_directory: Path, **fields) -> dict:
    data = read_summary(run_directory)
    data.update(fields)
    write_json(Path(run_directory) / "summary.json", data)
    return data


def park_run(run_id: str, reason: str, settings: dict | None = None) -> Path:
    """runs/<run_id>/ 를 runs/parked/<run_id>/ 로 옮기고 로그·요약에 남긴다. 이미 보류 상태면 그대로 둔다."""
    src = run_dir(run_id, settings)
    dst = parked_dir(run_id, settings)
    if src.is_dir():
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            shutil.rmtree(dst)
        shutil.move(str(src), str(dst))
    elif not dst.is_dir():
        raise FileNotFoundError(f"실행 폴더 없음: {src}")
    log = RunLog(dst, settings)
    log.log(f"보류(runs/parked/{run_id}/): {reason}", step="보류")
    write_summary(dst, run_id=run_id, parked=True, park_reason=reason, published=False, end_state="보류(runs/parked/)")
    return dst


def unpark_run(run_id: str, settings: dict | None = None) -> Path:
    """재투입(7.4): runs/parked/<run_id>/ 를 runs/<run_id>/ 로 되돌리고 summary.json 의 보류 표시를 지운다.
    parked → false, end_state → 재투입, park_reason 은 resumed_from_park_reason 으로 옮긴다(보류 이력은 log.md 와 이 키에 남는다).
    이렇게 해야 재투입 뒤 게시까지 간 실행이 select_target 의 연속 보류 횟수에 세어지지 않고, 일일 로그에 '보류' 줄이 붙지 않는다.
    이미 runs/<run_id>/ 에 있으면(보류 폴더가 없으면) summary 만 정리한다."""
    src = parked_dir(run_id, settings)
    dst = run_dir(run_id, settings)
    if src.is_dir():
        if dst.exists():
            raise FileExistsError(f"runs/{run_id} 와 runs/parked/{run_id} 가 둘 다 있다. 하나를 정리한 뒤 다시 시도한다")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
    elif not dst.is_dir():
        raise FileNotFoundError(f"실행 폴더 없음: {src} / {dst}")
    prev = read_summary(dst)
    fields: dict = {"parked": False, "end_state": "재투입", "resumed_at": now_str(settings)}
    if prev.get("park_reason"):
        fields["resumed_from_park_reason"] = prev["park_reason"]
    data = read_summary(dst)
    data.pop("park_reason", None)
    data.update(fields)
    data.setdefault("run_id", run_id)
    write_json(dst / "summary.json", data)
    log = RunLog(dst, settings)
    log.log(f"재투입: runs/parked/{run_id}/ → runs/{run_id}/ (이전 보류 사유: {prev.get('park_reason') or '기록 없음'})", step="재투입")
    return dst


# --- 트랙 백로그: 사용자 지정 질문 등록 ---------------------------------------------------------------

def register_user_track_questions(items: list[dict], slug: str, default_stage: int, day: str,
                                  priority: dict | None = None) -> list[dict]:
    """config/priority.yaml 의 track_questions 가운데 이 트랙(slug) 질문으로 백로그 항목(items)에 없는 것을 제기 근거 "사용자"로
    더한다(8.2 "사용자는 track_questions 에 질문을 넣어 우선순위를 올린다"). 같은 문장(앞뒤 공백 무시)이나 같은 id 가 있으면
    건너뛴다. items 를 고치고 더한 행 목록을 돌려준다. select_target.py(트랙 실행의 대상 선정 — 그 실행에서 바로 question_ids 로
    고를 수 있게)와 publish.py(5단계, 대상 선정에서 등록하지 못한 경우의 보완)가 함께 쓴다."""
    prio = priority if priority is not None else load_priority()
    texts = {str(b.get("question", "")).strip() for b in items}
    ids = {b.get("id") for b in items}
    added: list[dict] = []
    for q in prio.get("track_questions", []) or []:
        if str(q.get("track", "")) != slug or not q.get("question"):
            continue
        text = str(q["question"]).strip()
        if text in texts or (q.get("id") and q["id"] in ids):
            continue
        try:
            st = int(q.get("stage") or default_stage)
        except (TypeError, ValueError):
            st = int(default_stage)
        nums = [int(str(b["id"]).split("-")[1]) for b in items if re.match(rf"^q{st}-\d{{2}}$", str(b.get("id", "")))]
        qid = f"q{st}-{(max(nums) + 1) if nums else 1:02d}"
        row = {"id": qid, "question": text, "stage": st, "origin": "사용자", "status": "열림",
               "answered_run_id": None, "answer_link": None, "created": day, "origin_run_id": None,
               "priority": q.get("priority") or "normal"}
        items.append(row)
        texts.add(text)
        ids.add(qid)
        added.append(row)
    return added


# --- 정정 요청(inbox/corrections.md) -----------------------------------------------------------

_FENCE = re.compile(r"^(```|~~~).*?^\1[ \t]*$", re.M | re.S)
_CORR_HEAD = re.compile(r"^## (corr-\d{3,})[ \t]*$", re.M)
_CORR_FIELDS = {
    "페이지": "page", "문제 문장": "sentence", "근거": "evidence", "요청일": "requested",
    "요청자": "requester", "상태": "status", "처리 실행": "handled_run", "처리 메모": "memo",
}


def parse_corrections(text: str | None = None) -> list[dict]:
    """inbox/corrections.md 의 `## corr-NNN` 블록을 읽는다(코드 펜스 안은 제외). 상태 기본값은 open."""
    if text is None:
        text = read_text(INBOX_CORRECTIONS, "")
    scrubbed = _FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    heads = list(_CORR_HEAD.finditer(scrubbed))
    out = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(scrubbed)
        block = scrubbed[m.end():end]
        item = {"id": m.group(1), "page": "", "sentence": "", "evidence": "", "requested": "", "requester": "",
                "status": "open", "handled_run": "", "memo": ""}
        for line in block.split("\n"):
            lm = re.match(r"^\s*[-*]\s*([^:：]+)\s*[:：]\s*(.*)$", line)
            if not lm:
                continue
            key = _CORR_FIELDS.get(lm.group(1).strip())
            if key:
                item[key] = lm.group(2).strip()
        item["page"] = item["page"].strip("`").strip()
        item["status"] = (item["status"] or "open").strip("`").lower()
        out.append(item)
    return out


def open_corrections(text: str | None = None) -> list[dict]:
    return [c for c in parse_corrections(text) if c["status"] == "open"]


def update_correction_block(text: str, corr_id: str, status: str, run_id: str, memo: str) -> str:
    """corr_id 블록의 상태 줄을 바꾸고 처리 실행·처리 메모 줄을 덧붙인다(있으면 바꾼다). 블록이 없으면 원문 그대로."""
    head = re.compile(rf"^## {re.escape(corr_id)}[ \t]*$", re.M)
    m = head.search(text)
    if not m:
        return text
    nxt = re.compile(r"^## ", re.M).search(text, m.end())
    end = nxt.start() if nxt else len(text)
    block = text[m.end():end]
    lines = block.split("\n")
    done = {"status": False, "run": False, "memo": False}
    for i, line in enumerate(lines):
        if re.match(r"^\s*[-*]\s*상태\s*[:：]", line):
            lines[i] = f"- 상태: {status}"
            done["status"] = True
        elif re.match(r"^\s*[-*]\s*처리 실행\s*[:：]", line):
            lines[i] = f"- 처리 실행: {run_id}"
            done["run"] = True
        elif re.match(r"^\s*[-*]\s*처리 메모\s*[:：]", line):
            lines[i] = f"- 처리 메모: {memo}"
            done["memo"] = True
    # 마지막 목록 줄 뒤에 없는 줄을 추가한다
    last_list = max((i for i, l in enumerate(lines) if re.match(r"^\s*[-*]\s", l)), default=-1)
    add = []
    if not done["status"]:
        add.append(f"- 상태: {status}")
    if not done["run"]:
        add.append(f"- 처리 실행: {run_id}")
    if not done["memo"]:
        add.append(f"- 처리 메모: {memo}")
    if add:
        lines[last_list + 1:last_list + 1] = add
    return text[:m.end()] + "\n".join(lines) + text[end:]


# --- docs 도우미 ------------------------------------------------------------------------

def docs_tree() -> list[str]:
    return sorted(p.relative_to(paths.DOCS).as_posix() for p in paths.DOCS.rglob("*.md"))


def split_sections(body: str) -> list[tuple[str, str]]:
    """'## ' 제목 기준으로 (제목, 본문) 목록. 제목 앞부분은 ('', 본문)."""
    out: list[tuple[str, list[str]]] = [("", [])]
    for line in body.split("\n"):
        if line.startswith("## "):
            out.append((line[3:].strip(), []))
        else:
            out[-1][1].append(line)
    return [(h, "\n".join(ls).strip("\n")) for h, ls in out]


def area_summary(no: int) -> str:
    """관련 영역 페이지 요약: 제목·대분류·상태와 섹션 1·2(원문 정의·질문)."""
    p = paths.area_file(int(no))
    if not p.is_file():
        return f"(페이지 없음: {paths.area_repo_path(int(no))})"
    meta, body = fm.read(p)
    secs = dict(split_sections(body))
    parts = [f"# {meta.get('title', '')}", "",
             f"소속 대분류: {meta.get('category', '')} · 상태: {meta.get('status', '')} · 신뢰도: {meta.get('confidence', '—')} · 마지막 갱신: {meta.get('updated', '')} · 버전: {meta.get('version', '')}",
             ""]
    for h, txt in secs.items():
        if h.startswith("1. ") or h.startswith("2. "):
            parts += [f"## {h}", "", txt, ""]
    return "\n".join(parts).rstrip("\n") + "\n"


def area_of(no: int) -> dict:
    """세부영역 번호 → {area_no, area_name, category}(원문 명칭)."""
    from .source import load_source  # type: ignore
    src = load_source()
    a = src.area(int(no))
    return {"area_no": int(no), "area_name": a.title, "category": src.category_of(int(no)).title}


def existing_reference_ids() -> list[str]:
    return sorted(p.stem for p in (paths.DOCS / "references").glob("ref-*.md"))


def next_reference_id() -> str:
    nums = [int(i.split("-")[1]) for i in existing_reference_ids()]
    return f"ref-{(max(nums) + 1) if nums else 1:03d}"


REF_BLOCK_FILE = ROOT / "runs" / ".cache" / "ref_id_blocks.json"


def reserve_reference_block(run_id: str, size: int = 30) -> tuple[str, str]:
    """이 실행 전용 참고문헌 id 구간을 예약한다(병렬 배치에서 두 실행이 같은 '다음 id'를 받아 게시 직전 번호가 바뀌고, 그 사이 다른 실행이
    먼저 게시해 검증 에이전트가 엉뚱한 참고문헌과 대조하는 일을 막는다 — 3부 배치 트랙 1 첫 실행 보류). 같은 실행이 다시 부르면 같은 구간.
    시작 번호 = 게시된 최대 번호 + 1 부터 다른 실행의 예약 구간과 겹치지 않는 가장 낮은 곳(첫 맞춤). 게시 직전 압축(publish.compact_ref_mapping)이
    빈 번호를 메운다. 반환: (첫 id, 끝 id)."""
    import fcntl
    REF_BLOCK_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(str(REF_BLOCK_FILE) + ".lock", "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        data = _prune_ref_blocks(read_json(REF_BLOCK_FILE, {}) or {}, keep=run_id)
        if run_id in data:
            a, b = data[run_id]
        else:
            nums = [int(i.split("-")[1]) for i in existing_reference_ids()]
            a = (max(nums) if nums else 0) + 1
            # 첫 맞춤: 게시된 최대 번호 위에서 다른 실행의 예약 구간과 겹치지 않는 가장 낮은 구간(끝없이 커지지 않게)
            blocks = sorted((int(x), int(y)) for x, y in data.values())
            moved = True
            while moved:
                moved = False
                for x, y in blocks:
                    if a <= y and a + size - 1 >= x:
                        a = y + 1
                        moved = True
            b = a + size - 1
            data[run_id] = [a, b]
        write_json(REF_BLOCK_FILE, data)
    return f"ref-{a:03d}", f"ref-{b:03d}"


def _prune_ref_blocks(data: dict, keep: str | None = None) -> dict:
    """게시·보류됐거나 폴더가 없는 실행의 예약 구간을 푼다(예약 번호가 실행 수 × 구간 크기만큼 끝없이 커지지 않게)."""
    out = {}
    for rid, v in data.items():
        if rid == keep:
            out[rid] = v
            continue
        d = find_run_dir(rid)
        if not d:
            continue
        s = read_summary(d)
        # 끝난 실행(게시·보류·퍼블리셔 실패 등 end_state 가 적힌 실행)의 구간은 푼다. 실패한 실행의 구간을 남겨 두면 그 번호대가 영영 빈다
        if s.get("published") or s.get("parked") or s.get("end_state") or is_parked(rid):
            continue
        out[rid] = v
    return out


def active_reference_blocks(exclude: str | None = None) -> list[tuple[int, int]]:
    """아직 게시·보류되지 않은 다른 실행들의 예약 구간 [(시작, 끝)]."""
    data = _prune_ref_blocks(read_json(REF_BLOCK_FILE, {}) or {})
    return [(int(a), int(b)) for rid, (a, b) in data.items() if rid != exclude]


# --- 예산 -----------------------------------------------------------------------------

def budget_for(settings: dict, run_type: str, track_cfg: dict | None = None) -> dict:
    b = settings.get("daily_budget") or {}
    out = {
        "max_search_queries": int(b.get("max_search_queries", 30)),
        "max_sources_per_run": int(b.get("max_sources_per_run", 15)),
        "new_topic_pages": int(b.get("new_topic_pages", 1)),
        "page_updates": int(b.get("page_updates", 2)),
        "max_retries": int(b.get("max_retries", 2)),
    }
    if run_type == "track":
        out["max_search_queries"] = int(b.get("track_max_search_queries", 40))
        out["max_sources_per_run"] = int(b.get("track_max_sources_per_run", 20))
        tb = (track_cfg or {}).get("budget") or {}
        if isinstance(tb, dict):
            if tb.get("max_search_queries"):
                out["max_search_queries"] = int(tb["max_search_queries"])
            if tb.get("max_sources_per_run"):
                out["max_sources_per_run"] = int(tb["max_sources_per_run"])
    return out


# --- 스키마 -------------------------------------------------------------------------------

_SCHEMA_FILES = {"research": "research.schema.json", "verification": "verification.schema.json", "pages": "pages.schema.json"}


def load_schema(kind: str) -> dict:
    return read_json(SCHEMA_DIR / _SCHEMA_FILES[kind])


def returned_pages_schema(schema: dict) -> dict:
    """스토리텔러 반환값용 변형. 페이지마다 content(전체 페이지) 또는 patches(차등 갱신: 바꿀 절만) 가운데 하나가 있어야 한다 —
    JSON Schema 의 anyOf 는 CLI 제약으로 쓰지 않고 semantic_checks("pages", returned=True) 가 검사한다(운영 전환 1-5)."""
    s = copy.deepcopy(schema)
    s.pop("$defs", None)
    return s


def validate(kind: str, data, returned: bool = False) -> list[str]:
    """jsonschema 로 검사해 오류 문자열 목록을 돌려준다(비어 있으면 통과)."""
    from jsonschema import Draft202012Validator
    schema = load_schema(kind)
    if kind == "pages" and returned:
        schema = returned_pages_schema(schema)
    errs = []
    for e in sorted(Draft202012Validator(schema).iter_errors(data), key=lambda e: list(map(str, e.absolute_path))):
        loc = "/".join(str(x) for x in e.absolute_path) or "(root)"
        errs.append(f"{loc}: {e.message}")
    return errs


_ARRAY_KW = {"minItems", "maxItems", "items", "uniqueItems", "prefixItems", "contains"}
_OBJECT_KW = {"properties", "required", "additionalProperties", "patternProperties", "minProperties", "maxProperties", "propertyNames"}
_STRING_KW = {"minLength", "maxLength", "pattern", "format"}


def _normalize_cli_node(node):
    if isinstance(node, list):
        return [_normalize_cli_node(n) for n in node]
    if not isinstance(node, dict):
        return node
    out = {}
    for k, v in node.items():
        if k in ("$schema", "$id", "$defs", "definitions", "$comment"):
            continue
        out[k] = _normalize_cli_node(v)
    if "type" not in out and "$ref" not in out:
        keys = set(out)
        if keys & _ARRAY_KW:
            out["type"] = "array"
        elif keys & _OBJECT_KW:
            out["type"] = "object"
        elif keys & _STRING_KW:
            out["type"] = "string"
    return out


def cli_schema(schema: dict) -> dict:
    """claude -p --json-schema 에 넘길 수 있는 형태로 바꾼다(실험으로 확인한 제약):
    - `$schema`(draft 2020-12 URL)·`$id`·`$defs` 는 CLI 가 거부하므로 뺀다.
    - CLI 의 Ajv 가 strictTypes 모드라 minItems/properties 등이 있는 하위 스키마에 type 이 없으면 거부한다 → type 을 보충한다.
    - API 의 구조화 출력은 최상위 allOf/oneOf/anyOf 를 지원하지 않는다 → 최상위 조건 규칙(if/then)은 뺀다.
      뺀 규칙은 스크립트가 원본 스키마로 validate() 해 그대로 검사한다."""
    s = _normalize_cli_node(copy.deepcopy(schema))
    for k in ("allOf", "oneOf", "anyOf", "if", "then", "else"):
        s.pop(k, None)
    return s


# --- 스키마 밖 검사(참조 무결성·트랙 조건, schemas/README.md "공통 규칙") ---------------------------

_QID = re.compile(r"^q([1-9][0-9]?)-\d{2}$")
_STAGE_PAGE = re.compile(r"^docs/tracks/([a-z0-9-]+)/stage-([1-9][0-9]?)-[a-z0-9-]+\.md$")


def _stages_of(track_cfg: dict | None) -> int | None:
    try:
        return int((track_cfg or {}).get("stages"))
    except (TypeError, ValueError):
        return None


def semantic_checks(kind: str, data: dict, run_type: str | None = None, track_cfg: dict | None = None,
                    research: dict | None = None, returned: bool = False) -> list[str]:
    """JSON Schema 로 표현할 수 없는 검사. 오류 문자열 목록(비어 있으면 통과)."""
    errs: list[str] = []
    stages = _stages_of(track_cfg)
    is_track = run_type == "track"

    def stage_ok(n, where):
        try:
            n = int(n)
        except (TypeError, ValueError):
            errs.append(f"{where}: 단계 번호가 정수가 아니다: {n!r}")
            return
        if n < 1 or (stages and n > stages):
            errs.append(f"{where}: 단계 {n} 이 트랙 정의의 범위(1~{stages}) 밖이다")

    if kind == "research":
        if run_type and data.get("run_type") != run_type:
            errs.append(f"run_type 불일치: research.json {data.get('run_type')!r} != target {run_type!r}")
        fids = [f.get("id") for f in data.get("findings", [])]
        dup = {x for x in fids if fids.count(x) > 1}
        if dup:
            errs.append(f"finding id 중복: {sorted(dup)}")
        sids = {s.get("id") for s in data.get("sources", [])}
        stype = {s.get("id"): s.get("type") for s in data.get("sources", [])}
        for f in data.get("findings", []):
            missing = [s for s in f.get("source_ids", []) if s not in sids]
            if missing:
                errs.append(f"finding {f.get('id')}: sources 에 없는 출처 id {missing}")
            if f.get("tag") == "사실" and f.get("source_ids") and not f.get("vendor_claim") \
                    and all(stype.get(s) == "벤더 문서" for s in f.get("source_ids", [])):
                errs.append(f"finding {f.get('id')}: 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시가 없다(6.2 항목 13)")
        t = data.get("track")
        if is_track and not t:
            errs.append("트랙 실행인데 research.json 에 track 블록이 없다")
        if run_type and not is_track and t is not None:   # 부록 B.1 "track 블록은 트랙 실행에만 넣는다"(verification·pages 검사와 같이 양방향)
            errs.append("트랙 실행이 아닌데 research.json 에 track 블록이 있다")
        if t:
            if track_cfg and t.get("slug") != track_cfg.get("slug"):
                errs.append(f"track.slug 불일치: {t.get('slug')!r} != {track_cfg.get('slug')!r}")
            stage_ok(t.get("stage"), "track.stage")
            for q in t.get("answered_question_ids", []):
                m = _QID.match(str(q))
                if m:
                    stage_ok(int(m.group(1)), f"answered_question_ids {q}")
            for i, nq in enumerate(t.get("new_questions", [])):
                stage_ok(nq.get("stage"), f"new_questions[{i}].stage")
                if nq.get("rationale_finding_id") and nq["rationale_finding_id"] not in fids:
                    errs.append(f"new_questions[{i}]: 근거 finding {nq['rationale_finding_id']} 가 findings 에 없다")
            for i, oc in enumerate(t.get("ontology_changes", [])):
                bad = [x for x in oc.get("evidence_finding_ids", []) if x not in fids]
                if bad:
                    errs.append(f"ontology_changes[{i}]: 근거 finding {bad} 가 findings 에 없다")
            if not t.get("answered_question_ids") and "답한 질문 없음" not in str(get_path(data, "self_check.limits", "")):
                errs.append("트랙 실행에서 답한 질문이 0개인데 self_check.limits 에 '답한 질문 없음: <이유>' 가 없다")

    elif kind == "verification":
        tc = data.get("track_checks")
        if is_track and tc is None:
            errs.append("트랙 실행인데 verification.json 에 track_checks 가 없다")
        if not is_track and tc is not None:
            errs.append("트랙 실행이 아닌데 verification.json 에 track_checks 가 있다")
        if research:
            fids = {f.get("id") for f in research.get("findings", [])}
            for c in data.get("claim_checks", []):
                if c.get("finding_id") not in fids:
                    errs.append(f"claim_checks: finding {c.get('finding_id')} 가 research.json 에 없다")

    elif kind == "pages":
        for i, pg in enumerate(data.get("pages", [])):
            has_c, has_p = pg.get("content") is not None, bool(pg.get("patches"))
            if returned and not (has_c or has_p):
                errs.append(f"pages[{i}] {pg.get('path')}: content(전체 페이지)와 patches(바꿀 절) 가 모두 없다")
            if has_c and has_p:
                errs.append(f"pages[{i}] {pg.get('path')}: content 와 patches 를 함께 보냈다(하나만)")
            if has_p and pg.get("action") == "create":
                errs.append(f"pages[{i}] {pg.get('path')}: 새 페이지(action create)는 patches 가 아니라 content 로 보낸다")
        tu = data.get("track_updates")
        arp = data.get("area_reflection_proposals")
        if is_track and tu is None:
            errs.append("트랙 실행인데 pages.json 에 track_updates 가 없다")
        if is_track and arp is None:
            errs.append("트랙 실행인데 pages.json 에 area_reflection_proposals 가 없다(없으면 빈 배열)")
        if not is_track and tu is not None:
            errs.append("트랙 실행이 아닌데 pages.json 에 track_updates 가 있다")
        if not is_track and arp is not None:
            errs.append("트랙 실행이 아닌데 pages.json 에 area_reflection_proposals 가 있다")
        seen = set()
        for i, pg in enumerate(data.get("pages", [])):
            path = pg.get("path", "")
            if path in seen:
                errs.append(f"pages[{i}]: 경로 중복 {path}")
            seen.add(path)
            c = pg.get("content")
            if c is not None:
                if "{{" in c:
                    errs.append(f"pages[{i}] {path}: 템플릿 자리 표시({{{{ }}}})가 남아 있다")
                if not c.startswith("---"):
                    errs.append(f"pages[{i}] {path}: content 가 프런트매터로 시작하지 않는다")
        if tu:
            m = _STAGE_PAGE.match(tu.get("stage_page", ""))
            if m:
                if track_cfg and m.group(1) != track_cfg.get("slug"):
                    errs.append(f"track_updates.stage_page 의 트랙 slug {m.group(1)!r} 가 {track_cfg.get('slug')!r} 와 다르다")
                stage_ok(int(m.group(2)), "track_updates.stage_page")
            for i, b in enumerate(tu.get("backlog_updates", [])):
                qm = _QID.match(str(b.get("id", "")))
                if qm:
                    stage_ok(int(qm.group(1)), f"backlog_updates[{i}].id")
                if b.get("stage") is not None:
                    stage_ok(b.get("stage"), f"backlog_updates[{i}].stage")
            st = tu.get("stage_transition")
            if st:
                try:
                    to = int(st.get("to_stage"))
                    if to < 1 or (stages and to > stages + 1):
                        errs.append(f"stage_transition.to_stage {to} 가 범위(1~{stages + 1 if stages else '?'}) 밖이다")
                except (TypeError, ValueError):
                    errs.append("stage_transition.to_stage 가 정수가 아니다")
    return errs


# --- CLI ---------------------------------------------------------------------------------

def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description="runs/ 도우미 CLI (run_daily.sh 용)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("today")
    p = sub.add_parser("new-run-id"); p.add_argument("--date")
    p = sub.add_parser("step"); p.add_argument("--run-id", required=True); p.add_argument("--step", required=True)
    p.add_argument("--result", required=True); p.add_argument("--seconds", type=float); p.add_argument("--note", default="")
    p = sub.add_parser("log"); p.add_argument("--run-id", required=True); p.add_argument("--msg", required=True); p.add_argument("--step")
    p = sub.add_parser("park"); p.add_argument("--run-id", required=True); p.add_argument("--reason", required=True)
    p = sub.add_parser("unpark"); p.add_argument("--run-id", required=True)
    p = sub.add_parser("jsonget"); p.add_argument("--file", required=True); p.add_argument("--key", required=True); p.add_argument("--default", default="")
    p = sub.add_parser("jsonset"); p.add_argument("--file", required=True); p.add_argument("--set", nargs="*", default=[])
    p = sub.add_parser("setting"); p.add_argument("--key", required=True); p.add_argument("--default", default="")
    p = sub.add_parser("docs-tree"); p.add_argument("--run-id", required=True)
    p = sub.add_parser("run-dir"); p.add_argument("--run-id", required=True)
    p = sub.add_parser("summary"); p.add_argument("--run-id", required=True); p.add_argument("--set", nargs="*", default=[])
    p = sub.add_parser("budget-check"); p.add_argument("--run-id", required=True)
    args = ap.parse_args(argv)

    settings = None
    try:
        settings = load_settings()
    except Exception:
        settings = DEFAULT_SETTINGS

    if args.cmd == "today":
        print(today(settings))
    elif args.cmd == "new-run-id":
        print(new_run_id(args.date or today(settings), settings))
    elif args.cmd == "step":
        d = find_run_dir(args.run_id, settings) or run_dir(args.run_id, settings)
        log = RunLog(d, settings); log.ensure(args.run_id)
        log.step(args.step, args.result, args.seconds, args.note)
    elif args.cmd == "log":
        d = find_run_dir(args.run_id, settings) or run_dir(args.run_id, settings)
        log = RunLog(d, settings); log.ensure(args.run_id)
        log.log(args.msg, args.step)
    elif args.cmd == "park":
        print(park_run(args.run_id, args.reason, settings))
    elif args.cmd == "unpark":
        print(unpark_run(args.run_id, settings))
    elif args.cmd == "jsonget":
        data = read_json(args.file, None)
        v = get_path(data, args.key, None) if data is not None else None
        if v is None:
            print(args.default)
        elif isinstance(v, (dict, list)):
            print(json.dumps(v, ensure_ascii=False))
        elif isinstance(v, bool):
            print("true" if v else "false")
        else:
            print(v)
    elif args.cmd == "jsonset":
        # 최상위 키만 고친다(값 true/false/null/정수는 그 형식으로, 나머지는 문자열). run_daily.sh 가 probe.json 에 override 를 남길 때 쓴다
        data = read_json(args.file, {}) or {}
        for kv in args.set:
            k, _, v = kv.partition("=")
            data[k] = {"true": True, "false": False, "null": None}.get(v, int(v) if re.fullmatch(r"-?\d+", v) else v)
        write_json(args.file, data)
    elif args.cmd == "setting":
        v = get_path(settings, args.key, None)
        if v is None:
            print(args.default)
        elif isinstance(v, (dict, list)):
            print(json.dumps(v, ensure_ascii=False))
        elif isinstance(v, bool):
            print("true" if v else "false")
        else:
            print(v)
    elif args.cmd == "docs-tree":
        d = find_run_dir(args.run_id, settings) or run_dir(args.run_id, settings)
        p = write_text(d / "docs_tree.txt", "\n".join(docs_tree()) + "\n")
        print(p)
    elif args.cmd == "run-dir":
        d = find_run_dir(args.run_id, settings)
        if not d:
            print("", end="")
            return 1
        print(d)
    elif args.cmd == "summary":
        d = find_run_dir(args.run_id, settings) or run_dir(args.run_id, settings)
        fields = {}
        for kv in args.set:
            k, _, v = kv.partition("=")
            if v in ("true", "false"):
                fields[k] = v == "true"
            elif re.fullmatch(r"-?\d+", v):
                fields[k] = int(v)
            elif re.fullmatch(r"-?\d+\.\d+", v):
                fields[k] = float(v)
            else:
                fields[k] = v
        write_summary(d, run_id=args.run_id, **fields)
    elif args.cmd == "budget-check":
        # research.json 의 self_check.budget_used 를 target.json 의 budget 과 비교해 초과·도달을 출력한다(7.3)
        d = find_run_dir(args.run_id, settings) or run_dir(args.run_id, settings)
        target = read_json(d / "target.json", {}) or {}
        research = read_json(d / "research.json", {}) or {}
        budget = target.get("budget") or {}
        used = get_path(research, "self_check.budget_used", {}) or {}
        msgs = []
        for used_key, limit_key, label in (("queries", "max_search_queries", "검색 횟수"), ("sources", "max_sources_per_run", "신규 출처")):
            u, lim = used.get(used_key), budget.get(limit_key)
            if u is None or lim is None:
                continue
            if u > lim:
                msgs.append(f"{label} 초과: {u}/{lim} (부분 결과로 진행)")
            elif u == lim:
                msgs.append(f"{label} 도달: {u}/{lim} (부분 결과로 진행)")
        print("; ".join(msgs) if msgs else "예산 안")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
