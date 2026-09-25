"""data/*.json · docs 프런트매터 · runs/*/summary.json · config/tracks/*.yaml 에서
자동 갱신 영역(auto:<key>) 본문을 만드는 렌더러.

각 render_* 함수는 해당 auto 마커 안에 들어갈 마크다운 문자열을 돌려준다.
page_rel 은 그 영역이 들어갈 페이지의 docs 기준 상대 경로이며 링크 계산에 쓴다.
refresh_all_auto_regions() 는 docs 전체를 순회해 마커가 있는 페이지의 영역을 다시 채운다
(마커 없는 파일은 건너뛰고, 마커 밖 본문은 건드리지 않는다).

데이터 형식
- data/open_questions.json : {"items":[{"id","question","areas":[7],"raised","run_id","status","link"}]}
- data/changelog.json      : {"items":[{"date","run_id","action","page","summary"}]}
- data/flow_matrix.json    : {"steps":[…],"items":[…],"cells":{"피킹|완료·인계":[{"link","title","run_id"}]}}
- data/tracks/<slug>/backlog.json : {"items":[{"id","question","stage","origin","status","answered_run_id","answer_link","created"}]}
- data/tracks/<slug>/log.json     : {"items":[{"run_id","date","stage","stage_name","stage_page","run_id_cell","stage_cell",
                                     "answered_questions","new_questions","ontology_change","completion_assessment",
                                     "area_reflection_proposals","next_run_proposal", …}]} — 트랙 로그(auto:track-log)의 원천.
                                     셀 값은 로그 페이지(tracks/<slug>/log.md) 위치 기준 상대 링크를 담은 마크다운이다 [가정]
- runs/<run_id>/summary.json : {run_id,date,run_type,target,verdict_first,verdict_second,pages_created,
                                pages_updated,new_sources,parked,budget_used,duration_sec}
- config/tracks/<slug>.yaml : slug,name,status,current_stage,stages,
                              stage_names{n: 이름}, stage_pages{n: 파일명}(선택 [가정]),
                              order(트랙 표시 순서), draft_page·draft_title·draft_versions(살아있는 초안 페이지와 버전 이력 원천),
                              idea_no·idea_name·idea_page·idea_areas{primary,related}·idea_area_notes{n: 근거}(확장 아이디어 매핑) [가정]
"""
from __future__ import annotations

import json
import re
from collections import Counter, OrderedDict
from datetime import date
from pathlib import Path

import yaml

from . import autoregion as ar
from . import frontmatter as fm
from . import paths
from .paths import CONFIG, DATA, DOCS, RUNS
from .source import load_source

EMPTY = "비어 있음"
STATUS_ORDER = fm.STATUS_VALUES


# --- 데이터 읽기 --------------------------------------------------------------------

def _load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def load_open_questions() -> list[dict]:
    return _load_json(DATA / "open_questions.json", {}).get("items", []) or []


def load_changelog() -> list[dict]:
    return _load_json(DATA / "changelog.json", {}).get("items", []) or []


def load_flow_matrix() -> dict:
    d = _load_json(DATA / "flow_matrix.json", {})
    d.setdefault("steps", paths.FLOW_STEPS)
    d.setdefault("items", paths.FLOW_ITEMS)
    d.setdefault("cells", {})
    return d


def load_backlog(slug: str) -> list[dict]:
    return _load_json(paths.track_backlog(slug), {}).get("items", []) or []


def load_track_config(slug: str) -> dict | None:
    p = paths.track_config(slug)
    if not p.is_file():
        return None
    try:
        return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return None


def track_slugs() -> list[str]:
    """트랙 slug 목록. 트랙 정의의 order 순(첫 트랙이 맨 앞), 정의 없는 docs/tracks/<slug>/ 는 뒤에 slug 순(paths.ordered_track_slugs)."""
    return paths.ordered_track_slugs()


def load_run_summaries() -> list[dict]:
    out = []
    if not RUNS.is_dir():
        return out
    for p in sorted(RUNS.glob("*/summary.json")):
        if p.parent.name == "parked":
            continue
        d = _load_json(p, None)
        if isinstance(d, dict):
            d.setdefault("run_id", p.parent.name)
            out.append(d)
    return out


def parked_count() -> int:
    d = RUNS / "parked"
    if not d.is_dir():
        return 0
    return sum(1 for p in d.iterdir() if p.is_dir() or p.suffix == ".json")


_PAGE_CACHE: dict | None = None


def all_pages(refresh: bool = False) -> list[tuple[str, dict]]:
    """docs 안 모든 .md 의 (docs 기준 경로, 프런트매터) 목록."""
    global _PAGE_CACHE
    if _PAGE_CACHE is None or refresh:
        pages = []
        for p in sorted(DOCS.rglob("*.md")):
            try:
                meta, _ = fm.read(p)
            except Exception:
                meta = {}
            pages.append((p.relative_to(DOCS).as_posix(), meta))
        _PAGE_CACHE = pages
    return _PAGE_CACHE


# --- 공통 도우미 ---------------------------------------------------------------------

_FOOT_REF_TEXT = re.compile(r"(?<!`)\[\^([^\]\s]+)\](?!:)")


_TAG_PAREN_TEXT = re.compile(r"(\[(?:사실|추정|의견|분류원문|가설|사용자 실험)\])\(")


def neutralize_footnotes(s) -> str:
    """에이전트 산출물의 자유 텍스트(검증 노트·수정 지시·로그 항목 등)를 로그·자동 영역에 옮길 때 쓴다.
    그 텍스트 안의 각주 참조 표기 `[^ref-013]` 는 옮겨 간 페이지에 정의가 없어 check_links 의 '정의 없는 각주'
    오류가 되므로 인라인 코드로 감싸 글자 그대로 보이게 한다(인라인 코드 안은 각주 검사·렌더 대상이 아니다)."""
    out = _FOOT_REF_TEXT.sub(lambda m: f"`[^{m.group(1)}]`", str(s if s is not None else ""))
    # 사실 표기 태그 바로 뒤 괄호(`[사실](근거 ref-186 …)`)는 마크다운 링크로 읽혀 깨진 링크가 된다(3부 배치 세부영역 8 게시 실패).
    # 옮겨 온 에이전트 문장에서는 태그와 괄호 사이를 띄운다
    return _TAG_PAREN_TEXT.sub(lambda m: f"{m.group(1)} (", out)


_MD_LINK = re.compile(r"(?<!!)\[([^\]\n]+)\]\(([^)\s#]+\.md)(#[^)\s]*)?\)")


def fix_relative_links(text: str, page_rel: str) -> str:
    """page_rel(docs 기준 경로) 페이지에 옮겨 적은 글의 상대 링크를 바로잡는다. 에이전트 문장 안의 링크는 원래 다른 페이지 기준으로
    적혀 있어(예: 아이디어 페이지 기준 ../glossary/x.md) 일일 로그(logs/daily/)에서는 깨진다(3부 배치 트랙 2 게시 실패).
    이 페이지 기준으로 없는 대상은 docs 기준 경로(앞의 ../ 를 뗀 것)로 찾아 다시 쓰고, 그래도 없으면 링크를 풀어 글자만 남긴다."""
    import posixpath
    base = posixpath.dirname(page_rel)

    def repl(m):
        label, target, anchor = m.group(1), m.group(2), m.group(3) or ""
        if re.match(r"^[a-z]+:", target):
            return m.group(0)
        here = posixpath.normpath(posixpath.join(base, target))
        if (DOCS / here).is_file():
            return m.group(0)
        stripped = re.sub(r"^(\.\./)+", "", target)
        cand = [stripped] + ([stripped.split("docs/", 1)[1]] if "docs/" in stripped else [])
        for c in cand:
            if (DOCS / c).is_file():
                return f"[{label}]({posixpath.relpath(c, base or '.')}{anchor})"
        return label
    return _MD_LINK.sub(repl, text)


def _esc(s) -> str:
    """표 셀용 이스케이프. 각주 참조 표기는 인라인 코드로 바꾼다(neutralize_footnotes)."""
    return neutralize_footnotes(s).replace("|", "\\|").replace("\n", " ")


def _table(header: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for r in rows:
        lines.append("| " + " | ".join(_esc(c) for c in r) + " |")
    return "\n".join(lines)


def _link(page_rel: str, target: str | None, text: str | None = None) -> str:
    """target("docs/…" 또는 docs 기준 경로)으로의 상대 링크. 대상이 없으면 링크 없이 텍스트만."""
    if not target:
        return text or ""
    if re.match(r"^[a-z]+://", target):
        return f"[{text or target}]({target})"
    target, _, anchor = target.partition("#")          # 앵커는 파일 존재 확인에서 떼고 링크에 다시 붙인다
    frag = f"#{anchor}" if anchor else ""
    rel = paths.docs_rel(target)
    if rel.endswith("/") or rel == "":
        rel = rel + "index.md"
    if (DOCS / rel).is_dir():
        rel = rel + "/index.md"
    if not (DOCS / rel).is_file():
        return text or rel
    return f"[{text or _title_of(rel)}]({paths.rel_link(page_rel, rel)}{frag})"


def _title_of(rel: str) -> str:
    for r, meta in all_pages():
        if r == rel:
            return str(meta.get("title") or rel)
    return rel


def _page_label(page_rel: str, page: str | None) -> str:
    """변경 이력 항목의 page 를 제목 링크로. 디렉터리("docs/")나 없는 페이지는 경로 텍스트 그대로."""
    if not page:
        return ""
    rel = paths.docs_rel(page)
    if rel.endswith("/") or rel == "" or (DOCS / rel).is_dir():
        return page
    return _link(page_rel, page) if (DOCS / rel).is_file() else page


def area_label(no: int) -> str:
    try:
        return load_source().area(int(no)).title
    except (KeyError, ValueError):
        return str(no)


def area_link(page_rel: str, no: int) -> str:
    return _link(page_rel, paths.area_rel_path(int(no)), area_label(no))


def category_label(letter: str) -> str:
    return load_source().category(letter).title


def _areas_cell(page_rel: str, nos) -> str:
    nos = nos or []
    if isinstance(nos, (int, str)):
        nos = [nos]
    return "<br>".join(area_link(page_rel, n) for n in nos if str(n).isdigit()) or "—"


def _days_since(iso: str, today: str) -> int | None:
    try:
        return (date.fromisoformat(today) - date.fromisoformat(str(iso))).days
    except (TypeError, ValueError):
        return None


# --- 열린 질문 / 변경 이력 / 흐름 매트릭스 ------------------------------------------------

def render_open_questions(page_rel: str = "open-questions.md") -> str:
    items = load_open_questions()
    parts: list[str] = []
    if not items:
        parts.append("아직 등록된 열린 질문이 없다. 에이전트 실행이 시작되면 이 표가 채워진다.")
    else:
        rows = []
        for q in items:
            rows.append([
                q.get("id", ""), q.get("question", ""), _areas_cell(page_rel, q.get("areas")),
                q.get("raised", ""), q.get("run_id", ""), q.get("status", ""),
                _link(page_rel, q.get("link"), "링크") if q.get("link") else "—",
            ])
        parts.append(_table(["id", "질문", "관련 영역", "제기일", "제기한 실행", "상태", "해결 시 링크"], rows))
        c = Counter(q.get("status", "") for q in items)
        parts.append("")
        parts.append("상태별 건수: " + ", ".join(f"{k} {v}건" for k, v in c.items()))
    # 트랙 전용 질문은 트랙 백로그에 두고 여기에는 링크만 둔다
    links = []
    for slug in track_slugs():
        rel = f"tracks/{slug}/question-backlog.md"
        if (DOCS / rel).is_file():
            cfg = load_track_config(slug) or {}
            name = cfg.get("name") or _title_of(f"tracks/{slug}/index.md")
            open_n = sum(1 for b in load_backlog(slug) if b.get("status") in ("열림", "조사 중"))
            links.append(f"- {name}: {_link(page_rel, rel, '질문 백로그')} (열린 질문 {open_n}건)")
    parts.append("")
    parts.append("**트랙 전용 질문(트랙 백로그)**")
    parts.append("")
    parts.append("\n".join(links) if links else "- 등록된 트랙 백로그가 없다.")
    return "\n".join(parts)


def render_changelog(page_rel: str = "changelog.md") -> str:
    items = load_changelog()
    if not items:
        return "아직 기록된 변경이 없다."
    by_date: "OrderedDict[str, list[dict]]" = OrderedDict()
    for it in sorted(items, key=lambda x: (str(x.get("date", "")), str(x.get("run_id", ""))), reverse=True):
        by_date.setdefault(str(it.get("date", "")), []).append(it)
    parts = []
    for d, its in by_date.items():
        parts.append(f"### {d}")
        parts.append("")
        rows = [[it.get("run_id", ""), it.get("action", ""),
                 _link(page_rel, it.get("page"), it.get("page")), it.get("summary", "")] for it in its]
        parts.append(_table(["실행 id", "동작", "페이지", "요약"], rows))
        parts.append("")
    return "\n".join(parts).rstrip("\n")


def flow_fill_counts() -> tuple[int, int]:
    d = load_flow_matrix()
    total = len(d["steps"]) * len(d["items"])
    filled = sum(1 for k, v in d["cells"].items() if v)
    return filled, total


def render_flow_matrix(page_rel: str = "flow-matrix.md") -> str:
    d = load_flow_matrix()
    steps, items, cells = d["steps"], d["items"], d["cells"]
    rows = []
    for step in steps:
        row = [f"**{step}**"]
        for item in items:
            entries = cells.get(f"{step}|{item}") or []
            if not entries:
                row.append(EMPTY)
            else:
                row.append("<br>".join(_link(page_rel, e.get("link"), e.get("title") or e.get("link")) for e in entries))
        rows.append(row)
    filled, total = flow_fill_counts()
    return _table(["물류 단계 / 항목", *items], rows) + f"\n\n아직 채워지지 않은 칸은 \"{EMPTY}\"으로 표시한다. 채움률: {filled}/{total} 칸."


# --- 운영 지표 ----------------------------------------------------------------------

def render_metrics(page_rel: str = "metrics.md", today: str | None = None) -> str:
    today = today or paths.today()
    src = load_source()
    pages = all_pages(refresh=True)
    parts: list[str] = [f"기준일: {today}", ""]

    # 1. 영역별 페이지 상태 분포 (대분류별 표)
    parts.append("### 영역별 페이지 상태 분포")
    parts.append("")
    by_cat: dict[str, Counter] = {c.letter: Counter() for c in src.categories}
    area_meta: dict[int, dict] = {}
    for rel, meta in pages:
        t = meta.get("type")
        no = meta.get("area_no") if t == "area" else meta.get("primary_area_no") if t == "topic" else None
        if no is None:
            continue
        try:
            letter = paths.category_letter_of(int(no))
        except ValueError:
            continue
        by_cat[letter][str(meta.get("status", "미상"))] += 1
        if t == "area":
            area_meta[int(no)] = meta
    rows = []
    for c in src.categories:
        cnt = by_cat[c.letter]
        rows.append([_link(page_rel, paths.category_index_rel(c.letter), c.title),
                     *[str(cnt.get(s, 0)) for s in STATUS_ORDER], str(sum(cnt.values()))])
    parts.append(_table(["대분류", *STATUS_ORDER, "합계"], rows))
    parts.append("")
    parts.append("세부영역 페이지와 그 영역을 주 영역으로 하는 주제 페이지를 함께 센다.")
    parts.append("")
    for c in src.categories:
        parts.append(f"**{c.title}**")
        parts.append("")
        rows = []
        for no in c.area_nos:
            m = area_meta.get(no, {})
            rows.append([area_link(page_rel, no), m.get("status", "없음"), m.get("confidence", "—") or "—",
                         m.get("updated", "—"), str(m.get("version", "—"))])
        parts.append(_table(["세부영역", "상태", "신뢰도", "마지막 갱신", "버전"], rows))
        parts.append("")

    # 2. 검증 통과율, 3. 반려·보류 건수
    runs = load_run_summaries()
    parts.append("### 검증 통과율")
    parts.append("")
    if not runs:
        parts.append("실행 기록(runs/*/summary.json)이 없다.")
    else:
        passed = sum(1 for r in runs if r.get("verdict_second") == "통과"
                     or (not r.get("verdict_second") and r.get("verdict_first") in ("승인", "조건부 승인")))
        parts.append(f"- 실행 {len(runs)}회 중 최종 통과 {passed}회 (통과율 {passed / len(runs):.0%})")
        first = Counter(str(r.get("verdict_first", "미상")) for r in runs)
        second = Counter(str(r.get("verdict_second", "미상")) for r in runs)
        parts.append("- 1차 검증 판정: " + ", ".join(f"{k} {v}" for k, v in first.items()))
        parts.append("- 2차 검증 판정: " + ", ".join(f"{k} {v}" for k, v in second.items()))
    parts.append("")
    parts.append("### 반려·보류 건수")
    parts.append("")
    rejected = sum(1 for r in runs if r.get("verdict_first") == "반려")
    failed2 = sum(1 for r in runs if r.get("verdict_second") in ("불통과", "수정 후 재검증"))
    parked = sum(1 for r in runs if r.get("parked")) 
    parts.append(f"- 1차 반려 {rejected}건, 2차 불통과·재검증 {failed2}건")
    parts.append(f"- 보류(runs/parked) {max(parked, parked_count())}건")
    parts.append("")

    # 4. 출처 유형 분포
    parts.append("### 출처 유형 분포")
    parts.append("")
    types = Counter(str(meta.get("source_type", "미상")) for rel, meta in pages
                    if meta.get("type") == "reference" and meta.get("subtype") != "index")
    rel_c = Counter(str(meta.get("reliability", "미상")) for rel, meta in pages
                    if meta.get("type") == "reference" and meta.get("subtype") != "index")
    if not types:
        parts.append("등록된 참고문헌이 없다.")
    else:
        parts.append(_table(["유형", "건수"], [[k, str(v)] for k, v in types.most_common()]))
        parts.append("")
        parts.append("신뢰도: " + ", ".join(f"{k} {v}건" for k, v in rel_c.most_common()))
    parts.append("")

    # 5. 매트릭스 채움률
    filled, total = flow_fill_counts()
    parts.append("### 물류 흐름 매트릭스 채움률")
    parts.append("")
    parts.append(f"- {filled}/{total} 칸 ({filled / total:.0%}) — {_link(page_rel, 'flow-matrix.md', '흐름 매트릭스')}")
    parts.append("")

    # 6. 마지막 갱신이 오래된 영역 상위 5
    parts.append("### 마지막 갱신이 오래된 영역 상위 5")
    parts.append("")
    stale = []
    for no, m in area_meta.items():
        d = _days_since(m.get("updated", ""), today)
        stale.append((d if d is not None else 10**6, no, m))
    stale.sort(key=lambda x: (-x[0], x[1]))
    rows = [[area_link(page_rel, no), m.get("updated", "—"), str(d) if d < 10**6 else "미상", m.get("status", "—")]
            for d, no, m in stale[:5]]
    parts.append(_table(["세부영역", "마지막 갱신", "경과일", "상태"], rows) if rows else "세부영역 페이지가 없다.")
    return "\n".join(parts).rstrip("\n")


# --- 홈 -------------------------------------------------------------------------

def render_home_recent(n: int = 5, page_rel: str = "index.md") -> str:
    items = load_changelog()
    if not items:
        return "아직 기록된 업데이트가 없다."
    items = sorted(items, key=lambda x: (str(x.get("date", "")), str(x.get("run_id", ""))), reverse=True)[:n]
    lines = [f"- {it.get('date', '')} · {it.get('action', '')} · {_page_label(page_rel, it.get('page'))} — {it.get('summary', '')} (실행 {it.get('run_id', '')})"
             for it in items]
    lines.append(f"- 전체 목록: {_link(page_rel, 'changelog.md', '변경 이력')}")
    return "\n".join(lines)


def _latest_answered(backlog: list[dict]) -> dict | None:
    answered = [b for b in backlog if b.get("status") == "답함"]
    if not answered:
        return None
    return sorted(answered, key=lambda b: (str(b.get("answered_run_id") or ""), str(b.get("id"))))[-1]


def render_home_track_status(page_rel: str = "index.md") -> str:
    slugs = track_slugs()
    if not slugs:
        return "트랙 없음"
    rows = []
    for slug in slugs:
        cfg = load_track_config(slug)
        name = (cfg or {}).get("name") or _title_of(f"tracks/{slug}/index.md")
        backlog = load_backlog(slug)
        open_n = sum(1 for b in backlog if b.get("status") in ("열림", "조사 중"))
        last = _latest_answered(backlog)
        if last:
            q = f"{last.get('id')} — {last.get('question')}"
            if last.get("answer_link"):
                q += f" ({_link(page_rel, last['answer_link'], '답')})"
        else:
            q = "아직 없음"
        if cfg is None:
            stage = "미상"
        else:
            # 공통 호칭 규약: 단계도 번호와 이름을 함께 쓴다("단계 1. 기존 능력 표현 모델과 표준 조사")
            try:
                cur = int(cfg.get("current_stage", 1))
            except (TypeError, ValueError):
                cur = 1
            label = _stage_label(slug, cur, cfg)
            sf = _stage_file(slug, cur, cfg)
            stage = (_link(page_rel, sf, label) if sf else label) + f" ({cur} / {cfg.get('stages', '?')})"
        status = "미상(config 없음)" if cfg is None else str(cfg.get("status", "미상"))
        rows.append([name, stage, status, str(open_n), q, _link(page_rel, f"tracks/{slug}/index.md", "트랙 개요")])
    return _table(["트랙", "현재 단계", "상태", "열린 질문 수", "최근 답한 질문", "개요"], rows)


# --- 대분류·세부영역 -------------------------------------------------------------------

def _changelog_for(pred, n: int) -> list[dict]:
    items = [it for it in load_changelog() if pred(str(it.get("page", "")))]
    return sorted(items, key=lambda x: (str(x.get("date", "")), str(x.get("run_id", ""))), reverse=True)[:n]


def _recent_lines(items: list[dict], page_rel: str) -> str:
    if not items:
        return "아직 기록된 업데이트가 없다."
    return "\n".join(
        f"- {it.get('date', '')} · {it.get('action', '')} · {_page_label(page_rel, it.get('page'))} — {it.get('summary', '')} (실행 {it.get('run_id', '')})"
        for it in items)


def render_category_recent(letter: str, page_rel: str | None = None, n: int = 5) -> str:
    page_rel = page_rel or paths.category_index_rel(letter)
    prefix = f"docs/{paths.category_rel_dir(letter)}/"
    topic_of_cat = {rel for rel, meta in all_pages() if meta.get("type") == "topic"
                    and str(meta.get("primary_area_no", "")).isdigit()
                    and paths.category_letter_of(int(meta["primary_area_no"])) == letter}
    items = _changelog_for(lambda p: p.startswith(prefix) or paths.docs_rel(p) in topic_of_cat, n)
    return _recent_lines(items, page_rel)


def render_area_recent(no: int, page_rel: str | None = None, n: int = 5) -> str:
    no = int(no)
    page_rel = page_rel or paths.area_rel_path(no)
    mine = paths.area_repo_path(no)
    topics = {rel for rel, meta in all_pages() if meta.get("type") == "topic"
              and str(meta.get("primary_area_no", "")) == str(no)}
    items = _changelog_for(lambda p: p == mine or paths.docs_rel(p) in topics, n)
    return _recent_lines(items, page_rel)


def render_category_area_table(letter: str, page_rel: str | None = None) -> str:
    """대분류 페이지의 세부 연구영역 표: 원문 3열 그대로 + 페이지 링크 열 + 현재 상태 열."""
    src = load_source()
    cat = src.category(letter)
    page_rel = page_rel or paths.category_index_rel(letter)
    status_of = {int(meta.get("area_no")): meta.get("status", "없음") for rel, meta in all_pages(refresh=True)
                 if meta.get("type") == "area" and str(meta.get("area_no", "")).isdigit()}
    header = [*cat.table_header, "페이지", "현재 상태"]
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for a in cat.table_rows:
        link = _link(page_rel, paths.area_rel_path(a.no), a.title)
        lines.append(f"| {a.title_cell} | {a.what} | {a.question} | {link} | {status_of.get(a.no, '없음')} |")
    lines.append("")
    lines.append("[분류원문]")
    return "\n".join(lines)


# --- 용어집·참고문헌·표준·주제·로그 색인 ----------------------------------------------------

def render_glossary_index(page_rel: str = "glossary/index.md") -> str:
    rows = []
    for rel, meta in all_pages(refresh=True):
        if meta.get("type") != "glossary" or meta.get("subtype") == "index" or rel == "glossary/index.md":
            continue
        rows.append([_link(page_rel, rel, meta.get("term_ko") or meta.get("title") or rel),
                     meta.get("term_en", "—") or "—", meta.get("definition", "—") or "—",
                     _areas_cell(page_rel, meta.get("related_areas"))])
    if not rows:
        return "아직 등록된 용어가 없다."
    rows.sort(key=lambda r: r[0])
    return _table(["용어(한글)", "용어(영문)", "한 줄 정의", "관련 영역"], rows)


def render_references_index(page_rel: str = "references/index.md") -> str:
    rows = []
    for rel, meta in all_pages(refresh=True):
        if meta.get("type") != "reference" or meta.get("subtype") == "index" or rel == "references/index.md":
            continue
        rows.append([_link(page_rel, rel, meta.get("ref_id") or rel), meta.get("org", "—"),
                     meta.get("ref_title") or meta.get("title", "—"), str(meta.get("published", "미확인")),
                     meta.get("source_type", "—"), meta.get("reliability", "—"), str(meta.get("accessed", "—")),
                     f"<{meta['url']}>" if meta.get("url") else "—"])
    if not rows:
        return "아직 등록된 참고문헌이 없다."
    rows.sort(key=lambda r: r[0])
    return _table(["id", "기관", "제목", "발행일", "유형", "신뢰도", "접근일", "URL"], rows)


def render_standards_table(page_rel: str = "standards/index.md") -> str | None:
    """표준·프레임워크 표. data/standards.json 이 있으면 그 항목으로, 없으면 docs/standards/*.md
    프런트매터로 만든다. 둘 다 없으면 None(영역을 그대로 둔다). [가정]"""
    items = _load_json(DATA / "standards.json", {}).get("items")
    rows = []
    if items:
        for it in items:
            rows.append([it.get("name", ""), it.get("org", ""), it.get("kind", ""),
                         _areas_cell(page_rel, it.get("related_areas")),
                         _link(page_rel, f"references/{it['ref_id']}.md", it["ref_id"]) if it.get("ref_id") else "—",
                         f"<{it['url']}>" if it.get("url") else "—"])
    else:
        for rel, meta in all_pages(refresh=True):
            if meta.get("type") != "standard" or rel == "standards/index.md":
                continue
            rows.append([_link(page_rel, rel, meta.get("title", rel)), meta.get("org", "—"),
                         meta.get("kind", meta.get("standard_type", "—")), _areas_cell(page_rel, meta.get("related_areas")),
                         _link(page_rel, f"references/{meta['ref_id']}.md", meta["ref_id"]) if meta.get("ref_id") else "—",
                         f"<{meta['url']}>" if meta.get("url") else "—"])
    if not rows:
        return None
    return _table(["이름", "기관", "종류", "관련 영역", "참고문헌", "URL"], rows)


def render_topics_index(page_rel: str = "topics/index.md") -> str:
    rows = []
    for rel, meta in all_pages(refresh=True):
        if meta.get("type") != "topic" or meta.get("subtype") == "index" or rel == "topics/index.md":
            continue
        m = re.match(r"topics/\d{4}/(\d{4}-\d{2}-\d{2})", rel)
        d = m.group(1) if m else str(meta.get("created", ""))
        rows.append([d, _link(page_rel, rel, meta.get("title", rel)),
                     _areas_cell(page_rel, meta.get("primary_area_no")), meta.get("status", "—"),
                     meta.get("confidence", "—") or "—", meta.get("track", "—") or "—"])
    if not rows:
        return "아직 작성된 주제 페이지가 없다. 파이프라인 2주기부터 생성된다."
    rows.sort(key=lambda r: r[0], reverse=True)
    return _table(["날짜", "제목", "주 연구영역", "상태", "신뢰도", "트랙"], rows)


_FENCE = re.compile(r"^(```|~~~).*?^\1[ \t]*$", re.M | re.S)


def render_reference_cited_pages(ref_id: str, page_rel: str) -> str:
    """참고문헌 페이지의 "인용된 페이지" 목록. 다음 중 하나면 인용한 것으로 본다 [가정]:
    프런트매터 sources 에 ref_id 가 있음 / 본문(코드 펜스 제외)에 각주 참조 [^ref_id] 가 있음 /
    references/<ref_id>.md 로 가는 링크가 있음. 참고문헌 폴더의 페이지(자기 자신·색인)는 제외한다."""
    if not ref_id:
        return "- 아직 없음"
    foot = re.compile(r"\[\^" + re.escape(str(ref_id)) + r"\](?!:)")
    link = re.compile(r"\]\([^)\s]*references/" + re.escape(str(ref_id)) + r"\.md(?:[#?][^)\s]*)?\)")
    lines = []
    for rel, meta in all_pages():
        if rel == page_rel or rel.startswith("references/"):
            continue
        hit = str(ref_id) in [str(s) for s in (meta.get("sources") or [])]
        if not hit:
            try:
                body = _FENCE.sub("", (DOCS / rel).read_text(encoding="utf-8"))
            except OSError:
                continue
            hit = bool(foot.search(body) or link.search(body))
        if hit:
            lines.append(f"- {_link(page_rel, rel, str(meta.get('title') or rel))}")
    return "\n".join(lines) if lines else "- 아직 없음"


def render_logs_index(page_rel: str = "logs/index.md") -> str:
    daily = sorted((rel for rel, meta in all_pages(refresh=True) if rel.startswith("logs/daily/")), reverse=True)
    weekly = sorted((rel for rel, meta in all_pages() if rel.startswith("logs/weekly/")), reverse=True)
    parts = ["**일일 로그**", ""]
    parts += [f"- {_link(page_rel, r)}" for r in daily] or ["- 아직 없음"]
    parts += ["", "**주간 정리**", ""]
    parts += [f"- {_link(page_rel, r)}" for r in weekly] or ["- 아직 없음"]
    return "\n".join(parts)


# --- 트랙 ------------------------------------------------------------------------

def render_backlog(slug: str, page_rel: str | None = None) -> str:
    page_rel = page_rel or f"tracks/{slug}/question-backlog.md"
    items = load_backlog(slug)
    if not items:
        return "백로그가 비어 있다(data/tracks/<slug>/backlog.json 없음 또는 항목 없음)."
    cfg = load_track_config(slug) or {}
    rows = []
    for b in sorted(items, key=lambda b: (int(b.get("stage") or 0), str(b.get("id")))):
        st = b.get("stage")
        stage_cell = _stage_label(slug, int(st), cfg) if str(st).isdigit() else str(st or "")   # 번호와 이름을 함께 쓴다(항목 호칭)
        rows.append([b.get("id", ""), b.get("question", ""), stage_cell, b.get("origin", ""),
                     b.get("status", ""), b.get("answered_run_id") or "—",
                     _link(page_rel, b.get("answer_link"), "답") if b.get("answer_link") else "—",
                     b.get("created", "")])
    c = Counter(b.get("status", "") for b in items)
    return _table(["id", "질문", "단계", "제기 근거", "상태", "답한 실행", "답 링크", "제기일"], rows) + \
        "\n\n상태별 건수: " + ", ".join(f"{k} {v}건" for k, v in c.items())


def _stage_file(slug: str, n: int, cfg: dict | None = None) -> str | None:
    """단계 n 의 페이지(docs 기준 경로). config 의 stage_pages[n] → tracks/<slug>/stage-<n>-*.md 순으로 찾는다."""
    d = DOCS / "tracks" / slug
    pages = (cfg if cfg is not None else load_track_config(slug) or {}).get("stage_pages") or {}
    name = pages.get(n) or pages.get(str(n))
    if name and (d / str(name)).is_file():
        return f"tracks/{slug}/{name}"
    if d.is_dir():
        for p in sorted(d.glob(f"stage-{n}-*.md")):
            return p.relative_to(DOCS).as_posix()
    return None


def _stage_label(slug: str, n: int, cfg: dict | None = None) -> str:
    """단계 표기. 번호와 이름을 함께 쓴다("단계 1. 기존 능력 표현 모델과 표준 조사").
    단계 페이지의 title → config 의 stage_names[n] → "단계 n" 순으로 고른다."""
    for rel, meta in all_pages():
        if rel.startswith(f"tracks/{slug}/stage-{n}-") and meta.get("title"):
            return str(meta["title"])
    names = (cfg if cfg is not None else load_track_config(slug) or {}).get("stage_names") or {}
    name = names.get(n) or names.get(str(n))
    return f"단계 {n}. {name}" if name else f"단계 {n}"


def render_track_progress(slug: str, page_rel: str | None = None) -> str:
    page_rel = page_rel or f"tracks/{slug}/index.md"
    cfg = load_track_config(slug)
    if cfg is None:
        return "트랙 정의(config/tracks/<slug>.yaml)가 없다."
    stages = int(cfg.get("stages", 7))
    cur = int(cfg.get("current_stage", 1))
    completion = cfg.get("stage_completion") or {}       # {1: true, …} [가정]
    stage_status = cfg.get("stage_status") or {}         # {1: "완료", …} [가정]
    backlog = load_backlog(slug)
    rows = []
    for n in range(1, stages + 1):
        open_n = sum(1 for b in backlog if int(b.get("stage") or 0) == n and b.get("status") in ("열림", "조사 중"))
        st = stage_status.get(n) or ("완료" if n < cur else "진행 중" if n == cur else "대기")
        if cfg.get("status") == "done":
            st = stage_status.get(n) or "완료"
        met = completion.get(n)
        met_s = "충족" if met is True else "미충족" if met is False else ("충족" if n < cur else "미충족")
        label = _stage_label(slug, n, cfg)
        sf = _stage_file(slug, n, cfg)
        rows.append([_link(page_rel, sf, label) if sf else label, st, str(open_n), met_s])
    return _table(["단계", "상태", "열린 질문 수", "완료 조건 충족 여부"], rows) + \
        f"\n\n현재 단계: {_stage_label(slug, cur, cfg)} ({cur} / {stages}) · 트랙 상태: {cfg.get('status', '미상')}"


def render_track_recent_runs(slug: str, page_rel: str | None = None, n: int = 5) -> str:
    page_rel = page_rel or f"tracks/{slug}/index.md"
    runs = []
    for r in load_run_summaries():
        if r.get("run_type") != "track":
            continue
        t = r.get("target") or {}
        t_slug = t.get("slug") or t.get("track") if isinstance(t, dict) else str(t)
        if t_slug == slug:
            runs.append(r)
    if not runs:
        return "아직 트랙 실행 기록이 없다."
    runs.sort(key=lambda r: (str(r.get("date", "")), str(r.get("run_id", ""))), reverse=True)
    cfg = load_track_config(slug) or {}
    rows = []
    for r in runs[:n]:
        t = r.get("target") or {}
        stage = t.get("stage", "—") if isinstance(t, dict) else "—"
        stage_cell = _stage_label(slug, int(stage), cfg) if str(stage).isdigit() else str(stage)   # 번호와 이름을 함께 쓴다(항목 호칭)
        log_rel = f"logs/daily/{r.get('date', '')}.md"
        rows.append([r.get("run_id", ""), r.get("date", ""), stage_cell,
                     f"{r.get('verdict_first', '—')} / {r.get('verdict_second', '—')}",
                     f"{r.get('pages_created', 0)} / {r.get('pages_updated', 0)}",
                     _link(page_rel, log_rel, "로그") if (DOCS / log_rel).is_file() else "—"])
    return _table(["실행 id", "날짜", "단계", "판정(1차 / 2차)", "생성 / 갱신", "일일 로그"], rows)


def render_ontology_version_history(slug: str, page_rel: str | None = None) -> str | None:
    """살아있는 초안(첫 트랙은 온톨로지 초안)의 버전 이력. 원천은 트랙 정의의 draft_versions
    (없으면 data/tracks/<slug>/ontology_versions.json, {"items":[{"version","date","changes","run_id"}]}) 이며
    파일이 있을 때만 렌더링한다. 키 이름(ontology-version-history)은 첫 트랙과의 호환을 위해 모든 트랙의 초안에 그대로 쓴다. [가정]"""
    items = _load_json(paths.track_draft_versions(slug), {}).get("items")
    if not items:
        return None
    rows = [[str(it.get("version", "")), str(it.get("date", "")), it.get("changes", ""), it.get("run_id", "")]
            for it in items]
    return _table(["버전", "날짜", "변경 내용", "근거 실행 id"], rows)


def load_track_log(slug: str) -> list[dict]:
    return _load_json(DATA / "tracks" / slug / "log.json", {}).get("items", []) or []


# 트랙 로그 한 실행의 여덟 항목(사양서 5.4 트랙 로그): (표의 항목 이름, log.json 의 키)
TRACK_LOG_ROWS: list[tuple[str, str]] = [
    ("실행 id", "run_id_cell"), ("단계", "stage_cell"), ("답한 질문", "answered_questions"), ("새 질문", "new_questions"),
    ("온톨로지 변경", "ontology_change"), ("완료 조건 평가", "completion_assessment"),
    ("세부영역 반영 제안", "area_reflection_proposals"), ("다음 실행 제안", "next_run_proposal"),
]


def render_track_log(slug: str, page_rel: str | None = None) -> str:
    """트랙 로그의 "실행 기록"(auto:track-log). data/tracks/<slug>/log.json 항목을 최신순(날짜 내림차순, 같은 날짜면
    나중에 추가된 항목이 먼저)으로, 실행마다 "### 실행 <id> — 단계 <n>. <이름>" 소제목과 여덟 항목 표 하나로 만든다.
    셀 값은 log.json 에 저장된 마크다운(로그 페이지 기준 상대 링크 포함)을 그대로 쓰므로 이 영역은 tracks/<slug>/log.md 에만 둔다."""
    items = load_track_log(slug)
    if not items:
        return "아직 트랙 실행 기록이 없다."
    cfg = load_track_config(slug) or {}
    names = cfg.get("stage_names") or {}
    order = sorted(enumerate(items), key=lambda x: (str(x[1].get("date") or ""), x[0]), reverse=True)
    blocks = []
    for _, e in order:
        st = e.get("stage")
        name = e.get("stage_name") or (names.get(st) or names.get(str(st)) if st is not None else None)
        if name:
            label = f"단계 {st}. {name}"
        elif str(st).isdigit():
            label = _stage_label(slug, int(st), cfg)
        else:
            label = f"단계 {st}" if st is not None else "단계 미상"
        fallback = {
            "run_id_cell": e.get("run_id") or "",
            "stage_cell": f"[{label}]({e['stage_page']})" if e.get("stage_page") else label,
        }
        lines = [f"### 실행 {e.get('run_id', '')} — {label}", "", "| 항목 | 내용 |", "|---|---|"]
        for head, key in TRACK_LOG_ROWS:
            lines.append(f"| {head} | {_esc(e.get(key) or fallback.get(key) or '없음')} |")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


# --- 확장 아이디어·세부영역의 관련 연구 트랙 ------------------------------------------------------

IDEA_MARKS = {"primary": "●", "related": "○"}
IDEA_ROLE_LABELS = {"primary": "중심 영역", "related": "함께 필요한 영역"}


def _int_list(v) -> list[int]:
    if v is None:
        return []
    if isinstance(v, (int, str)):
        v = [v]
    return [int(x) for x in v if str(x).strip().isdigit()]


def idea_mapping(slug: str, cfg: dict | None = None) -> dict[int, str]:
    """트랙 정의의 아이디어 매핑 {영역 번호: "primary" | "related"}. idea_areas 가 없으면 빈 dict."""
    cfg = (load_track_config(slug) or {}) if cfg is None else cfg
    ia = cfg.get("idea_areas") or {}
    out: dict[int, str] = {}
    for n in _int_list(ia.get("related")):
        out[n] = "related"
    for n in _int_list(ia.get("primary")):
        out[n] = "primary"
    return out


def idea_label(cfg: dict) -> str:
    """아이디어 호칭: "아이디어 n. 이름"."""
    n, name = cfg.get("idea_no"), cfg.get("idea_name")
    if n and name:
        return f"아이디어 {n}. {name}"
    return str(name or cfg.get("name") or "")


def _idea_rel(cfg: dict) -> str | None:
    return paths.idea_page_rel(cfg)


def idea_tracks() -> list[tuple[str, dict]]:
    """아이디어 페이지(idea_page)를 가진 트랙 (slug, 정의) 목록. 트랙 순서."""
    out = []
    for slug in track_slugs():
        cfg = load_track_config(slug) or {}
        if cfg.get("idea_page"):
            out.append((slug, cfg))
    return out


def area_track_links(no: int) -> list[tuple[str, dict, str]]:
    """세부영역 no 와 연결된 트랙 (slug, 정의, 역할) 목록. 역할은 "primary"(primary_area 이거나 아이디어 매핑 ●) 또는
    "related"(related_areas 에 있거나 아이디어 매핑 ○)."""
    no = int(no)
    out = []
    for slug in track_slugs():
        cfg = load_track_config(slug)
        if not cfg:
            continue
        mapping = idea_mapping(slug, cfg)
        prim = _int_list(cfg.get("primary_area"))
        if no in prim or mapping.get(no) == "primary":
            role = "primary"
        elif no in _int_list(cfg.get("related_areas")) or mapping.get(no) == "related":
            role = "related"
        else:
            continue
        out.append((slug, cfg, role))
    return out


def render_area_tracks(no: int, page_rel: str | None = None) -> str:
    """세부영역 페이지 머리의 "관련 연구 트랙" 안내(auto:area-tracks). 연결된 트랙이 없으면 빈 문자열."""
    no = int(no)
    page_rel = page_rel or paths.area_rel_path(no)
    links = area_track_links(no)
    if not links:
        return ""
    lines = ['!!! note "관련 연구 트랙"',
             f"    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은"
             f" 이 페이지에 반영하도록 제안된다. 전체 매핑은 {_link(page_rel, paths.IDEAS_INDEX, '확장 아이디어 연결 구조')}에 있다.",
             ""]
    for slug, cfg, role in links:
        name = cfg.get("name") or _title_of(f"tracks/{slug}/index.md")
        item = f"    - {_link(page_rel, f'tracks/{slug}/index.md', str(name))} — {IDEA_ROLE_LABELS[role]}({IDEA_MARKS[role]})"
        st = str(cfg.get("status") or "")
        if st and st != "active":
            item += f", 트랙 상태 {st}"
        irel = _idea_rel(cfg)
        if irel:
            item += f" · 확장 아이디어: {_link(page_rel, irel, idea_label(cfg))}"
        lines.append(item)
    return "\n".join(lines)


def render_idea_area_map(page_rel: str = paths.IDEAS_INDEX) -> str:
    """28개 세부영역 × 확장 아이디어 매핑표(auto:idea-area-map). 칸: ● 중심 영역 / ○ 함께 필요한 영역 / 빈칸."""
    tracks = idea_tracks()
    if not tracks:
        return "아이디어 매핑이 없다(config/tracks/*.yaml 의 idea_page·idea_areas 없음)."
    maps = [idea_mapping(slug, cfg) for slug, cfg in tracks]
    header = ["대분류", "세부 연구영역"] + [_link(page_rel, _idea_rel(cfg), idea_label(cfg)) for _, cfg in tracks]
    rows = []
    for no in paths.AREA_NOS:
        letter = paths.category_letter_of(no)
        rows.append([_link(page_rel, paths.category_index_rel(letter), category_label(letter)), area_link(page_rel, no)]
                    + [IDEA_MARKS.get(m.get(no, ""), "") for m in maps])
    lines = [_table(header, rows), "", "● 중심 영역 · ○ 함께 필요한 영역 · 빈칸은 직접 연결 없음. 영역 수:", ""]
    for (slug, cfg), m in zip(tracks, maps):
        p = sum(1 for v in m.values() if v == "primary")
        r = sum(1 for v in m.values() if v == "related")
        lines.append(f"- {idea_label(cfg)}: ● {p}개 · ○ {r}개 · 합계 {p + r}개 영역 "
                     f"({_link(page_rel, f'tracks/{slug}/index.md', '트랙 개요')})")
    return "\n".join(lines)


def render_idea_areas(slug: str, page_rel: str | None = None) -> str:
    """아이디어 페이지 "2. 관련 세부 연구영역"(auto:idea-areas): 매핑표 기준 중심·함께 필요한 영역 목록과 근거."""
    cfg = load_track_config(slug) or {}
    page_rel = page_rel or (_idea_rel(cfg) or paths.IDEAS_INDEX)
    m = idea_mapping(slug, cfg)
    if not m:
        return "매핑이 없다(트랙 정의의 idea_areas 없음)."
    notes = cfg.get("idea_area_notes") or {}
    parts = []
    for role in ("primary", "related"):
        nos = sorted(n for n, r in m.items() if r == role)
        if not nos:
            continue
        parts += [f"**{IDEA_ROLE_LABELS[role]}({IDEA_MARKS[role]})**", ""]
        for n in nos:
            note = notes.get(n) or notes.get(str(n))
            parts.append(f"- {area_link(page_rel, n)}" + (f" — {note}" if note else ""))
        parts.append("")
    parts.append(f"매핑 전체와 다른 아이디어와의 비교는 {_link(page_rel, paths.IDEAS_INDEX, '확장 아이디어 연결 구조')}의 매핑표에 있다.")
    return "\n".join(parts)


BACKLOG_STATUS_ORDER = ["열림", "조사 중", "답함", "보류", "폐기"]


def render_idea_backlog(slug: str, page_rel: str | None = None) -> str:
    """아이디어 페이지 "7. 미해결 질문 백로그"(auto:idea-backlog): 트랙 백로그를 상태(열림 → 조사 중 → 답함 → 보류 → 폐기) 순으로."""
    cfg = load_track_config(slug) or {}
    page_rel = page_rel or (_idea_rel(cfg) or paths.IDEAS_INDEX)
    items = load_backlog(slug)
    backlog_rel = f"tracks/{slug}/question-backlog.md"
    if not items:
        return f"백로그가 비어 있다({_link(page_rel, backlog_rel, '질문 백로그')})."
    c = Counter(b.get("status", "") for b in items)
    summary = " · ".join(f"{k} {c[k]}건" for k in BACKLOG_STATUS_ORDER if c.get(k))
    others = [k for k in c if k not in BACKLOG_STATUS_ORDER]
    if others:
        summary += " · " + " · ".join(f"{k} {c[k]}건" for k in others)

    def key(b):
        st = b.get("status", "")
        rank = BACKLOG_STATUS_ORDER.index(st) if st in BACKLOG_STATUS_ORDER else len(BACKLOG_STATUS_ORDER)
        return (rank, int(b.get("stage") or 0) if str(b.get("stage")).isdigit() else 0, str(b.get("id")))

    rows = []
    for b in sorted(items, key=key):
        st = b.get("stage")
        label = _stage_label(slug, int(st), cfg) if str(st).isdigit() else str(st or "")
        sf = _stage_file(slug, int(st), cfg) if str(st).isdigit() else None
        rows.append([b.get("status", ""), b.get("id", ""), b.get("question", ""),
                     _link(page_rel, sf, label) if sf else label, b.get("origin", ""),
                     _link(page_rel, b.get("answer_link"), "답") if b.get("answer_link") else "—"])
    head = (f"원천: {_link(page_rel, backlog_rel, '질문 백로그')}"
            f"({_link(page_rel, f'tracks/{slug}/index.md', str(cfg.get('name') or slug))} 트랙) · {summary}")
    return head + "\n\n" + _table(["상태", "id", "질문", "단계", "제기 근거", "답"], rows)


# --- 페이지 상태 줄(단일 원천: 프런트매터) -------------------------------------------------------

def render_page_status(page_rel: str, meta: dict) -> str:
    """본문 상태 줄(auto:page-status). 프런트매터의 status·confidence·version·updated·last_run 에서 한 줄을 만든다.
    초안 페이지(ontology_version 이 있는 페이지)는 앞에 초안 버전을 붙인다. 라벨은 트랙 정의의 draft_version_label
    (없으면 "온톨로지 버전"). deprecated 면 replaced_by 링크를 덧붙인다. [가정]"""
    parts = []
    ov = meta.get("ontology_version")
    if ov not in (None, ""):
        slug = _slug_from(page_rel, meta)
        label = (load_track_config(slug) or {}).get("draft_version_label") if slug else None
        parts.append(f"{label or '온톨로지 버전'}: v{ov}")
    parts += [f"페이지 상태: {meta.get('status') or '미상'}",
              f"신뢰도: {meta.get('confidence') or '미부여'}",
              f"페이지 버전: {meta.get('version') if meta.get('version') not in (None, '') else '미상'}",
              f"마지막 갱신: {meta.get('updated') or '미상'}",
              f"마지막 실행: {meta.get('last_run') or '없음'}"]
    if meta.get("status") == "deprecated" and meta.get("replaced_by"):
        parts.append(f"대체 페이지: {_link(page_rel, str(meta['replaced_by']))}")
    return "> " + " · ".join(parts)


_STATUS_WORDS = "|".join(re.escape(s) for s in fm.STATUS_VALUES)
_PAGE_STATUS_TEXT = re.compile(r"페이지\s*상태\s*[:：]")
_STATUS_LINE = re.compile(r"^\s*(?:>\s*)*(?:\*\*)?상태(?:\*\*)?\s*[:：]\s*(?:\*\*)?\s*`?(?:" + _STATUS_WORDS + r")\b")
_FENCE_LINE = re.compile(r"^\s*(```|~~~)")
_INLINE_CODE = re.compile(r"`[^`\n]*`")


def status_line_violations(body: str) -> list[str]:
    """본문(프런트매터 제외)에서 auto:page-status 영역 밖에 손으로 쓴 페이지 상태 줄을 찾는다.
    잡는 것: "페이지 상태:"가 들어 있는 줄, 그리고 "상태:" 또는 "> 상태:"로 시작하고 값이 페이지 상태 값
    (seed|draft|verified|published|needs_update|deprecated)인 줄. 코드 펜스 안과 인라인 코드 안은 보지 않는다.
    돌려주는 값: "본문 <n>행: <줄>" 목록(비어 있으면 통과). check_frontmatter 와 스토리텔러 산출물 검사가 같은 규칙을 쓴다."""
    out: list[str] = []
    start, end = ar.start_marker("page-status"), ar.end_marker("page-status")
    in_region = False
    fence = None
    for n, line in enumerate(body.split("\n"), 1):
        if start in line:
            in_region = end not in line.split(start, 1)[1]
            continue
        if in_region:
            if end in line:
                in_region = False
            continue
        m = _FENCE_LINE.match(line)
        if m:
            if fence is None:
                fence = m.group(1)
            elif m.group(1) == fence:
                fence = None
            continue
        if fence:
            continue
        text = _INLINE_CODE.sub("", line)
        if _PAGE_STATUS_TEXT.search(text) or _STATUS_LINE.match(text):
            out.append(f"본문 {n}행: {line.strip()[:120]}")
    return out


# --- 전체 갱신 -----------------------------------------------------------------------

def _slug_from(rel: str, meta: dict) -> str | None:
    if meta.get("track"):
        return str(meta["track"])
    m = re.match(r"tracks/([^/]+)/", rel)
    return m.group(1) if m else None


def _letter_from(rel: str, meta: dict) -> str | None:
    t = str(meta.get("title", ""))
    if meta.get("type") == "category" and t[:1] in paths.CATEGORY_SLUGS:
        return t[0]
    m = re.match(r"categories/([a-g])-", rel)
    return m.group(1).upper() if m else None


def render_for(key: str, page_rel: str, meta: dict) -> str | None:
    """키와 페이지 문맥으로 영역 본문을 만든다. None 이면 영역을 그대로 둔다."""
    if key == "home-track-status":
        return render_home_track_status(page_rel)
    if key == "home-recent":
        return render_home_recent(page_rel=page_rel)
    if key == "category-recent":
        letter = _letter_from(page_rel, meta)
        return render_category_recent(letter, page_rel) if letter else None
    if key == "category-area-table":
        letter = _letter_from(page_rel, meta)
        return render_category_area_table(letter, page_rel) if letter else None
    if key == "area-recent":
        no = meta.get("area_no")
        return render_area_recent(int(no), page_rel) if str(no).isdigit() else None
    if key == "track-progress":
        slug = _slug_from(page_rel, meta)
        return render_track_progress(slug, page_rel) if slug else None
    if key == "track-recent-runs":
        slug = _slug_from(page_rel, meta)
        return render_track_recent_runs(slug, page_rel) if slug else None
    if key == "backlog":
        slug = _slug_from(page_rel, meta)
        return render_backlog(slug, page_rel) if slug else None
    if key == "ontology-version-history":
        slug = _slug_from(page_rel, meta)
        return render_ontology_version_history(slug, page_rel) if slug else None
    if key == "track-log":
        slug = _slug_from(page_rel, meta)
        return render_track_log(slug, page_rel) if slug else None
    if key == "open-questions":
        return render_open_questions(page_rel)
    if key == "changelog":
        return render_changelog(page_rel)
    if key == "flow-matrix":
        return render_flow_matrix(page_rel)
    if key == "metrics":
        return render_metrics(page_rel)
    if key == "glossary-index":
        return render_glossary_index(page_rel)
    if key == "references-index":
        return render_references_index(page_rel)
    if key == "reference-cited-pages":
        ref_id = meta.get("ref_id") or (re.match(r"references/(ref-\d+)\.md$", page_rel) or [None, None])[1]
        return render_reference_cited_pages(str(ref_id), page_rel) if ref_id else None
    if key == "standards-table":
        return render_standards_table(page_rel)
    if key == "topics-index":
        return render_topics_index(page_rel)
    if key == "logs-index":
        return render_logs_index(page_rel)
    if key == "area-tracks":
        no = meta.get("area_no")
        return render_area_tracks(int(no), page_rel) if str(no).isdigit() else None
    if key == "idea-area-map":
        return render_idea_area_map(page_rel)
    if key == "idea-areas":
        slug = _slug_from(page_rel, meta)
        return render_idea_areas(slug, page_rel) if slug else None
    if key == "idea-backlog":
        slug = _slug_from(page_rel, meta)
        return render_idea_backlog(slug, page_rel) if slug else None
    if key == "page-status":
        return render_page_status(page_rel, meta)
    return None


class AutoRegionError(RuntimeError):
    """strict 모드에서 자동 갱신 영역을 다시 만들지 못했을 때(렌더 예외 또는 등록되지 않은 키)."""

    def __init__(self, failures: list[str]):
        self.failures = failures
        super().__init__("자동 갱신 영역 렌더 실패 %d건:\n" % len(failures) + "\n".join(f"  - {f}" for f in failures[:40]))


LAST_FAILURES: list[str] = []   # 마지막 refresh_all_auto_regions() 호출의 실패 목록(strict 가 아닐 때 호출자가 확인한다)


def refresh_all_auto_regions(verbose: bool = False, strict: bool = False) -> list[str]:
    """docs 전체를 순회해 마커가 있는 페이지의 영역을 다시 채운다. 바뀐 파일 목록을 돌려준다.

    렌더 실패(예외)와 AUTO_KEYS 에 없는 키는 (페이지, 키, 사유) 로 모아 LAST_FAILURES 에 남긴다.
    strict=True 면 실패가 하나라도 있을 때 아무 파일도 쓰지 않고 AutoRegionError 를 올린다(퍼블리셔 5·8단계: 사양서 6.4
    "하나라도 실패하면 반영하지 않는다" — 낡은 영역을 그대로 둔 채 빌드·커밋하지 않도록). strict=False(기본, scaffold 등)는
    실패한 영역만 그대로 두고 나머지를 갱신한다."""
    all_pages(refresh=True)
    changed: list[str] = []
    failures: list[str] = []
    pending: list[tuple[Path, str, str, list[str]]] = []
    for p in sorted(DOCS.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        keys = ar.list_regions(text)
        if not keys:
            continue
        rel = p.relative_to(DOCS).as_posix()
        meta, _ = fm.parse(text)
        new_text = text
        for key in keys:
            if key not in ar.AUTO_KEYS:
                failures.append(f"{rel} auto:{key}: 등록되지 않은 키(pipeline/lib/autoregion.py 의 AUTO_KEYS 에 없음)")
                continue
            try:
                content = render_for(key, rel, meta)
            except Exception as e:  # 렌더 실패는 해당 영역만 건너뛰고 기록한다
                failures.append(f"{rel} auto:{key}: {type(e).__name__}: {e}")
                if verbose:
                    print(f"[render] {rel} auto:{key} 실패: {e}")
                continue
            if content is None:
                continue
            # 자동 영역에는 각주 정의가 없으므로, 에이전트 텍스트에 섞인 각주 참조 표기는 인라인 코드로 바꾼다
            new_text = ar.replace_region(new_text, key, neutralize_footnotes(content))
        if new_text != text:
            pending.append((p, new_text, rel, keys))
    LAST_FAILURES[:] = failures
    if strict and failures:
        raise AutoRegionError(failures)
    for p, new_text, rel, keys in pending:
        p.write_text(new_text, encoding="utf-8")
        changed.append(rel)
        if verbose:
            print(f"[render] 갱신: {rel} ({', '.join(keys)})")
    all_pages(refresh=True)
    return changed
