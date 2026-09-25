"""에이전트 산출물 형식 검증(운영 전환 1-2)과 분량 초과 절의 자동 분리(1-3), 차등 갱신 패치 적용(1-5).

모델 호출 없이 코드로 하는 검사만 모았다. run_daily.sh 가 에이전트 호출 직후 pipeline/validate_run.py 로 부르고,
실패하면 오류 목록을 붙여 같은 에이전트에 형식 수정 재작성을 요청한다. 퍼블리셔는 이 검사를 통과한 산출물만 받는다.

공개 함수
- expected_h2(page_type) -> list[str] | None       템플릿이 정한 H2 절 제목 목록
- h2_titles(body) -> list[str]                      본문의 H2 제목(코드 펜스 제외)
- check_page(rel, text) -> list[str]                페이지 한 개의 형식 오류
- area_body_chars(body) -> int                      세부영역 3~11절 본문 글자 수(각주 참조·태그·링크 URL·주석 제외)
- section_chars(body) -> dict[str, int]             절별 글자 수
- apply_patches(current_text, patches) -> str       절 단위 패치를 현재 페이지에 적용
- split_oversized_area(...) -> (area_text, [topic pages])   분량 초과 절을 주제 페이지로 분리
"""
from __future__ import annotations

import re
from pathlib import Path

from . import frontmatter as fm
from . import paths

ROOT = paths.ROOT
TEMPLATES = ROOT / "templates"

TEMPLATE_FOR_TYPE = {
    "area": "area.md", "topic": "topic.md", "category": "category.md", "track-stage": "track-stage.md",
    "ontology-draft": "ontology-draft.md",
}
# 트랙 개요(type track, subtype 없음)도 템플릿 절 구성을 따른다
TRACK_OVERVIEW_TEMPLATE = "track-overview.md"

_FENCE = re.compile(r"^(```|~~~).*?^\1[ \t]*$", re.M | re.S)
_COMMENT = re.compile(r"<!--.*?-->", re.S)
_INLINE_CODE = re.compile(r"`[^`\n]*`")
_H2 = re.compile(r"^## (.+?)\s*$", re.M)
FOOT_REF = re.compile(r"\[\^([^\]\s]+)\](?!:)")
FOOT_DEF = re.compile(r"^\[\^([^\]\s]+)\]:", re.M)
TAG_PAREN = re.compile(r"\[(사실|추정|의견|분류원문|가설|사용자 실험)\]\(")
STATUS_VALUES = "seed|draft|verified|published|needs_update|deprecated"
_STATUS_LINE = re.compile(rf"^(?:>\s*)?(?:페이지\s*)?상태\s*:\s*`?({STATUS_VALUES})\b", re.M)
_PAGE_STATUS_REGION = re.compile(r"<!-- auto:page-status:start -->.*?<!-- auto:page-status:end -->", re.S)
_TAG = re.compile(r"\[(사실|추정|의견|분류원문|가설|사용자 실험)\]")
_LINK_URL = re.compile(r"\]\([^)]*\)")

AREA_BODY_SECTIONS = [str(n) for n in range(3, 12)]
# 자동 분리 대상에서 뺀 절: 5(현장 시나리오 — 흐름 매트릭스 앵커의 기준), 9(ROP 직접 범위 — 페이지의 핵심 판단)
AREA_NO_SPLIT = {"5", "9"}


# --- 절 구조 ---------------------------------------------------------------------------------

def _strip_code(text: str) -> str:
    return _FENCE.sub("", text)


def h2_titles(body: str) -> list[str]:
    return [m.group(1).strip() for m in _H2.finditer(_strip_code(body))]


def expected_h2(page_type: str, subtype: str | None = None) -> list[str] | None:
    if page_type == "track" and not subtype:
        fname = TRACK_OVERVIEW_TEMPLATE
    else:
        fname = TEMPLATE_FOR_TYPE.get(page_type or "")
    if not fname or subtype == "index":
        return None
    p = TEMPLATES / fname
    if not p.is_file():
        return None
    text = _COMMENT.sub("", p.read_text(encoding="utf-8"))
    titles = [t for t in h2_titles(text) if "{{" not in t]
    return titles or None


def split_sections(body: str) -> list[tuple[str | None, str]]:
    """본문을 [(H2 제목 또는 None(첫 H2 앞), 절 텍스트(제목 줄 포함))] 로 나눈다. 코드 펜스 안의 ## 는 제목으로 보지 않는다."""
    masked = _FENCE.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), body)
    starts = [(m.start(), m.group(1).strip()) for m in _H2.finditer(masked)]
    out: list[tuple[str | None, str]] = []
    if not starts:
        return [(None, body)]
    if starts[0][0] > 0:
        out.append((None, body[:starts[0][0]]))
    for i, (pos, title) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(body)
        out.append((title, body[pos:end]))
    return out


def section_no(title: str | None) -> str | None:
    m = re.match(r"^(\d+)\.", title or "")
    return m.group(1) if m else None


def plain_len(text: str) -> int:
    t = _COMMENT.sub("", _strip_code(text))
    t = FOOT_DEF.sub("", t)
    t = FOOT_REF.sub("", t)
    t = _TAG.sub("", t)
    t = _LINK_URL.sub("]", t)
    t = re.sub(r"^#+ .*$", "", t, flags=re.M)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return len(t.strip())


def section_chars(body: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for title, text in split_sections(body):
        no = section_no(title)
        if no:
            first_nl = text.find("\n")
            out[no] = plain_len(text[first_nl + 1:] if first_nl >= 0 else "")
    return out


def area_body_chars(body: str) -> int:
    sc = section_chars(body)
    return sum(v for k, v in sc.items() if k in AREA_BODY_SECTIONS)


# --- 페이지 형식 검사 ------------------------------------------------------------------------

def status_line_violations(body: str) -> list[str]:
    """본문에 페이지 상태를 직접 쓴 줄(자동 영역 page-status 밖). 상태는 프런트매터 한 곳에만 둔다(1-4).
    check_frontmatter.py 와 같은 규칙을 쓰도록 lib.render.status_line_violations 에 맡긴다(없으면 아래 간이 규칙)."""
    try:
        from .render import status_line_violations as _render_rule
        return _render_rule(body)
    except ImportError:
        pass
    outside = _PAGE_STATUS_REGION.sub("", _COMMENT.sub(lambda m: m.group(0) if "auto:page-status" in m.group(0) else "", body))
    outside = _strip_code(outside)
    return [m.group(0).strip() for m in _STATUS_LINE.finditer(outside)]


def footnote_problems(body: str) -> list[str]:
    scrub = _INLINE_CODE.sub("", _strip_code(body))
    refs = set(FOOT_REF.findall(scrub))
    defs = set(FOOT_DEF.findall(scrub))
    errs = [f"각주 [^{r}] 참조는 있으나 정의가 없다" for r in sorted(refs - defs)]
    return errs


def check_page(rel: str, text: str, strict_sections: bool = True) -> list[str]:
    """페이지 한 개의 형식 오류 목록. rel 은 docs 기준 경로(표시용)."""
    errs: list[str] = []
    if "{{" in text:
        errs.append("템플릿 자리 표시({{ }})가 남아 있다")
    if not text.startswith("---\n"):
        errs.append("프런트매터로 시작하지 않는다")
        return errs
    try:
        meta, body = fm.parse(text)
    except Exception as e:  # noqa: BLE001
        return [f"프런트매터 파싱 실패: {e}"]
    for e in fm.validate(meta, rel):
        errs.append(e)
    first = next((l for l in body.split("\n") if l.strip()), "")
    if not fm.BREADCRUMB_RE.match(first.strip()):
        errs.append("본문 첫 줄이 이동 경로('[홈](…) › …')가 아니다")
    scrub = _INLINE_CODE.sub("", _strip_code(body))
    for m in TAG_PAREN.finditer(scrub):
        s = scrub[max(0, m.start() - 30): m.end() + 30].replace("\n", " ")
        errs.append(f"사실 표기 태그 바로 뒤에 여는 괄호가 붙어 링크로 읽힌다: …{s}… (태그 뒤에는 각주만 붙이고 괄호 설명은 태그 앞에 쓴다)")
    for s in status_line_violations(body):
        errs.append(f"본문에 페이지 상태를 직접 썼다: '{s}' — 상태는 프런트매터 한 곳에만 둔다(자동 영역 page-status 가 표시한다)")
    errs += footnote_problems(body)
    if strict_sections:
        exp = expected_h2(str(meta.get("type") or ""), meta.get("subtype"))
        if exp:
            got = h2_titles(body)
            if got[: len(exp)] != exp:
                errs.append(f"H2 절 제목·순서가 템플릿과 다르다. 기대: {exp} / 실제: {got}")
    return errs


# --- 차등 갱신 패치 ----------------------------------------------------------------------------

def _norm_title(t: str) -> str:
    return re.sub(r"\s+", " ", (t or "").strip())


def apply_patches(current_text: str, patches: list[dict]) -> str:
    """절 단위 패치를 적용한다. section 은 H2 제목 전체(공백 정규화 비교), 없으면 번호 접두('6.')로도 찾는다.
    action replace 는 제목 줄을 남기고 본문을 바꾸며, append 는 본문 끝에 덧붙인다. frontmatter 가 있으면 그 필드를 바꾼다.
    찾지 못한 절은 ValueError."""
    meta, body = fm.parse(current_text)
    parts = split_sections(body)
    for p in patches:
        want = _norm_title(p.get("section", ""))
        want_no = section_no(want)
        idx = next((i for i, (t, _) in enumerate(parts) if t and _norm_title(t) == want), None)
        if idx is None and want_no:
            idx = next((i for i, (t, _) in enumerate(parts) if t and section_no(t) == want_no), None)
        if idx is None:
            raise ValueError(f"패치 대상 절을 찾지 못했다: '{p.get('section')}'")
        title, text = parts[idx]
        head, _, rest = text.partition("\n")
        new_body = (p.get("content") or "").strip("\n")
        if p.get("action") == "append":
            new_text = head + "\n" + rest.rstrip("\n") + "\n\n" + new_body + "\n\n"
        else:
            new_text = head + "\n\n" + new_body + "\n\n"
        parts[idx] = (title, new_text)
        for k, v in (p.get("frontmatter") or {}).items():
            meta[k] = v
    new_body_text = "".join(t for _, t in parts)
    new_body_text = re.sub(r"\n{3,}", "\n\n", new_body_text).rstrip("\n") + "\n"
    return fm.dumps(meta, new_body_text)


def footnote_line(ref: dict) -> str:
    """각주 정의 한 줄(publish._footnote_line 과 같은 형식)."""
    pub = ref.get("published")
    pub = str(pub) if pub not in (None, "", "미확인", "발행일 미확인") else "미확인"
    unopened = ref.get("source_unopened") if "fetched" not in ref else not ref.get("fetched")
    tail = " (원문 미열람)" if unopened else ""
    return f"[^{ref['id']}]: {ref.get('org', '')}, {ref.get('title', '')}, {pub}, {ref.get('url', '')}, 접근일 {ref.get('accessed', '')}{tail}"


def _ref_lookup(ref_id: str, run_refs: dict) -> dict | None:
    if ref_id in run_refs:
        return run_refs[ref_id]
    pth = paths.DOCS / "references" / f"{ref_id}.md"
    if not pth.is_file():
        return None
    meta, _ = fm.read(pth)
    return {"id": ref_id, "org": meta.get("org", ""), "title": meta.get("ref_title") or meta.get("title", ""),
            "published": meta.get("published"), "url": meta.get("url", ""), "accessed": meta.get("accessed", ""),
            "fetched": bool(meta.get("fetched"))}


def complete_patched_page(text: str, prior_text: str, day: str, run_refs: dict, explicit_fm: dict | None = None) -> tuple[str, list[str]]:
    """차등 갱신 패치를 적용한 페이지의 기계적 마무리(판단이 필요 없는 부분, 운영 전환 1-5).
    ① 프런트매터: version 을 기존 +1, updated 를 실행 날짜, status 를 draft 로(패치가 명시한 값은 그대로 둔다)
    ② 본문에 참조만 있고 정의가 없는 각주([^ref-NNN])의 정의 줄을 이번 실행의 출처 또는 참고문헌 페이지에서 만들어 페이지 끝에 붙인다.
    반환: (새 텍스트, 처리 메모)."""
    notes: list[str] = []
    explicit_fm = explicit_fm or {}
    meta, body = fm.parse(text)
    prior, _ = fm.parse(prior_text)
    try:
        pv = int(prior.get("version") or 0)
    except (TypeError, ValueError):
        pv = 0
    if "version" not in explicit_fm:
        meta["version"] = pv + 1
    if "updated" not in explicit_fm:
        meta["updated"] = day
    if "status" not in explicit_fm:
        meta["status"] = "draft"
    scrub = _INLINE_CODE.sub("", _strip_code(body))
    missing = sorted(set(FOOT_REF.findall(scrub)) - set(FOOT_DEF.findall(scrub)))
    added = []
    for rid in missing:
        ref = _ref_lookup(rid, run_refs) if re.match(r"^ref-\d{3,}$", rid) else None
        if ref:
            added.append(footnote_line(dict(ref, id=rid)))
    if added:
        body = body.rstrip("\n") + "\n\n" + "\n".join(added) + "\n"
        notes.append(f"각주 정의 {len(added)}개를 참고문헌에서 만들어 붙임: {', '.join(a.split(']')[0][2:] for a in added)}")
    return fm.dumps(meta, body), notes


# --- 분량 초과 절 자동 분리 -------------------------------------------------------------------

def _first_sentence(text: str) -> str:
    """절 본문의 첫 문장(태그·각주 포함). 요약이 없을 때 대신 쓴다."""
    t = _COMMENT.sub("", text).strip()
    for para in re.split(r"\n\s*\n", t):
        para = para.strip()
        if not para or para.startswith(("|", "#", "```", "!!!", ">")):
            continue
        para = re.sub(r"^[-*]\s+", "", para)
        m = re.search(r"^(.+?다\.(?:\s*\[(?:사실|추정|의견|분류원문|가설|사용자 실험)\])?(?:\[\^[^\]]+\])*)", para, re.S)
        return (m.group(1) if m else para.split("\n")[0]).strip()
    return ""


def _lead_sentences(text: str, max_sentences: int = 2, max_chars: int = 300) -> str:
    """절 본문 첫 문단의 앞 문장들(태그·각주 포함, 최대 max_sentences 문장·max_chars 자)."""
    first = _first_sentence(text)
    if not first:
        return ""
    out = first
    rest_src = _COMMENT.sub("", text).strip()
    pos = rest_src.find(first)
    if pos >= 0 and max_sentences > 1:
        rest = rest_src[pos + len(first):]
        para_end = re.search(r"\n\s*\n", rest)
        rest = (rest[:para_end.start()] if para_end else rest).strip()
        m = re.search(r"^(.+?다\.(?:\s*\[(?:사실|추정|의견|분류원문|가설|사용자 실험)\])?(?:\[\^[^\]]+\])*)", rest, re.S)
        if m and len(out) + 1 + len(m.group(1)) <= max_chars:
            out = out + " " + m.group(1).strip()
    return out


def _footnote_defs(body: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in body.split("\n"):
        m = re.match(r"^\[\^([^\]\s]+)\]:(.*)$", line)
        if m:
            out[m.group(1)] = line
    return out


def _drop_unused_defs(body: str) -> str:
    scrub_lines = [l for l in body.split("\n") if not re.match(r"^\[\^[^\]\s]+\]:", l)]
    used = set(FOOT_REF.findall(_INLINE_CODE.sub("", "\n".join(scrub_lines))))
    kept = [l for l in body.split("\n") if not (re.match(r"^\[\^([^\]\s]+)\]:", l) and re.match(r"^\[\^([^\]\s]+)\]:", l).group(1) not in used)]
    return "\n".join(kept)


def split_oversized_area(area_rel: str, area_text: str, limit: int, outline: list[dict], run_id: str, day: str,
                         topic_template_h2: list[str] | None = None) -> tuple[str, list[dict]]:
    """세부영역 페이지의 3~11절 본문이 limit 을 넘으면, 큰 절부터(5·9절 제외) 주제 페이지로 옮기고 원 절에는
    요약(그 절의 첫 문장, 최대 두 문장)과 링크만 남긴다. 내용을 줄이거나 새로 쓰지 않는다.
    반환: (새 세부영역 페이지 텍스트, [{path(repo 기준), content, section, chars}])."""
    meta, body = fm.parse(area_text)
    if area_body_chars(body) <= limit:
        return area_text, []
    area_no = int(meta.get("area_no"))
    area_title = str(meta.get("title"))
    summaries = {}
    for o in outline or []:
        if paths.docs_rel(o.get("path", "")) == paths.docs_rel(area_rel):
            summaries[section_no(o.get("section")) or _norm_title(o.get("section"))] = (o.get("summary") or "").strip()
    defs = _footnote_defs(body)
    topics: list[dict] = []
    year = day[:4]
    area_docs_rel = paths.docs_rel(area_rel)
    while area_body_chars(body) > limit:
        sc = section_chars(body)
        cands = [(v, k) for k, v in sc.items() if k in AREA_BODY_SECTIONS and k not in AREA_NO_SPLIT
                 and not any(t["section_no"] == k for t in topics) and v > 400]
        if not cands:
            break
        _, no = max(cands)
        parts = split_sections(body)
        idx = next(i for i, (t, _) in enumerate(parts) if section_no(t) == no)
        title, text = parts[idx]
        head, _, sec_body = text.partition("\n")
        sec_body = sec_body.strip("\n")
        sec_name = re.sub(r"^\d+\.\s*", "", title)
        sec_name_short = re.sub(r"\s*\(.*\)\s*$", "", sec_name)
        slug = f"{day}-area{area_no:02d}-s{no}"
        k = 2
        while (paths.DOCS / "topics" / year / f"{slug}.md").exists():   # 같은 날 같은 절을 다시 분리하면 번호를 붙인다
            slug = f"{day}-area{area_no:02d}-s{no}-{k}"
            k += 1
        topic_repo = f"docs/topics/{year}/{slug}.md"
        topic_docs = f"topics/{year}/{slug}.md"
        link_from_area = paths.rel_link(area_docs_rel, topic_docs)
        # 원 절에 남기는 요약은 그 절의 첫 문장(최대 두 문장, 300자) — 이미 쓴 독자용 본문이다. outline 의 summary 는 예산 계획용이라
        # 편집 설명("…를 더하고 연결한다")이 섞일 수 있어 본문에 싣지 않는다(검증 실행 1의 2차 검증 지적). 첫 문장을 못 찾을 때만 쓴다.
        summary = _lead_sentences(sec_body) or summaries.get(no) or ""
        t_title = f"{area_title} — {sec_name_short}"
        used_refs = sorted(set(FOOT_REF.findall(_INLINE_CODE.sub("", sec_body))))
        link_to_area = paths.rel_link(topic_docs, area_docs_rel)
        related = [x for x in (meta.get("related_areas") or []) if str(x).isdigit()]
        rel_links = []
        for n in related:
            try:
                ameta, _ = fm.read(paths.area_file(int(n)))
                rel_links.append(f"[{ameta.get('title')}]({paths.rel_link(topic_docs, paths.area_rel_path(int(n)))})")
            except Exception:  # noqa: BLE001
                continue
        h2 = topic_template_h2 or expected_h2("topic") or [
            "1. 세 줄 요약", "2. 배경", "3. 본문", "4. 현장 시나리오", "5. ROP 관점의 시사점", "6. 연결되는 연구영역",
            "7. 열린 질문", "8. 출처", "9. 검증 노트", "10. 이력"]
        sec_anchor = lambda n: next((t for t in h2_titles(body) if section_no(t) == n), "")  # noqa: E731
        bodies = {
            0: f"- {summary}\n- 이 페이지는 [{area_title}]({link_to_area}) 페이지의 \"{sec_name_short}\" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.",
            1: f"[{area_title}]({link_to_area}) 페이지를 쓰는 과정에서 \"{sec_name}\" 절의 분량이 세부영역 페이지 기준({limit:,}자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.",
            2: sec_body,
            3: f"현장 시나리오는 원 페이지의 [{sec_anchor('5') or '5. 현장 시나리오'}]({link_to_area}) 절에 있다.",
            4: f"ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [{sec_anchor('9') or '9절'}]({link_to_area}) 절에 있다.",
            5: "- 주 연구영역: " + f"[{area_title}]({link_to_area})" + ("\n- 관련 영역: " + ", ".join(rel_links) if rel_links else ""),
            6: f"열린 질문은 원 페이지의 [{sec_anchor('11') or '11. 열린 질문'}]({link_to_area}) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.",
            7: "\n".join(defs[r] for r in used_refs if r in defs) or "이 절에는 각주가 없다.",
            8: f"원 페이지와 함께 실행 {run_id} 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.",
            9: f"| 날짜 | 실행 id | 변경 |\n|---|---|---|\n| {day} | {run_id} | {area_title} 의 \"{sec_name_short}\" 절에서 분리 |",
        }
        crumb = f"[홈](../../index.md) › [주제](../index.md) › {t_title}"
        tmeta = {
            "title": t_title, "type": "topic", "category": meta.get("category"), "primary_area_no": area_no,
            "related_areas": related, "tags": ["분리 페이지"], "status": "draft", "confidence": meta.get("confidence") or "medium",
            "created": day, "updated": day, "sources": used_refs, "last_run": day, "version": 1,
            "split_from": f"{area_rel}#{no}",
        }
        tbody = [crumb, "", f"# {t_title}", "", "<!-- auto:page-status:start -->", "<!-- auto:page-status:end -->", ""]
        for i, t in enumerate(h2):
            tbody += [f"## {t}", "", bodies.get(i, ""), ""]
        topic_text = fm.dumps(tmeta, "\n".join(tbody).rstrip("\n") + "\n")
        topics.append({"path": topic_repo, "content": topic_text, "section": title, "section_no": no, "chars": sc[no]})
        new_sec = f"{head}\n\n{summary}\n\n자세한 내용은 주제 페이지 [{t_title}]({link_from_area})에 있다.\n\n"
        parts[idx] = (title, new_sec)
        body = "".join(t for _, t in parts)
    body = _drop_unused_defs(body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return fm.dumps(meta, body), topics
