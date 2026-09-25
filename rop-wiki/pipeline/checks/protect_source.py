#!/usr/bin/env python3
"""원문 보호 검사 (사양서 6.4 의 3단계).

검사 항목
1. _source/ 원문의 sha256 이 pipeline/checks/source.sha256 과 같은지(변조 여부). --write-hash 로 해시 파일 생성.
2. 28개 세부영역 페이지: 프런트매터 title/category, 13개 섹션 제목·순서, 섹션 1·2의 [분류원문] 문장,
   "> 원문 주석:" 인용 블록, 상단 admonition 의 핵심 질문을 파서 값과 글자 단위로 대조.
3. 7개 대분류 페이지: 핵심 질문·개요·세부 연구영역 표(원문 3열)·핵심 포인트 문단 대조.
   섹션은 4.3 의 여섯 개 뒤에 번호 없는 "참고 자료"(각주 정의) 하나만 더 둘 수 있다. [가정]
4. 홈·소개 4페이지: 원문 1·9·10·11장의 모든 줄과 정의·범위 문장이 그대로 들어 있는지.
5. docs 전체(모든 페이지 유형): [분류원문] 태그가 붙은 줄은 모두 원문의 줄 또는 표 셀과 글자 단위로 같아야 한다
   (원문에 없는 합성 문장이나 위키 문구가 섞인 줄에 태그를 붙이는 것을 막는다). 비교 전에 제거하는 것은
   구조 표식뿐이다: 들여쓰기, 인용 블록 표식(>), 태그 뒤에 붙은 각주 참조("[분류원문][^ref-003]"),
   세부영역 페이지 인용 블록의 고정 라벨 "원문 주석: "(2번 검사가 요구하는 형식). 표 아래 단독 태그 줄은 제외한다.
6. mkdocs.yml: 내비 라벨의 대분류·세부영역 명칭 대조 + 파일 전체가 현재 파일시스템 기준 nav.render_mkdocs_yml()
   결과와 같은지(4.8 순서·누락 페이지). 다르면 `python3 pipeline/scaffold.py --refresh-auto` 로 재생성한다.
   그리고 내비 구조 자체를 검사한다(check_nav_structure): 사양서 4.8 원문 순서(홈 → 소개 → 대분류 A~G → 중점 연구 트랙 →
   주제 → 용어집 → 참고문헌 → 표준·프레임워크 → 열린 질문 → 흐름 매트릭스 → 변경 이력 → 운영 지표 → 로그)는 그대로 지켜야 하고,
   4.8 목록 밖의 "확장 아이디어"는 중점 연구 트랙 바로 다음(주제 앞), "정정 요청 안내"는 맨 뒤에만 올 수 있다.
   중점 연구 트랙 아래는 트랙 정의의 order 순(첫 트랙 manual-capability-ontology 가 맨 앞)이고, 트랙마다 개요 → 단계(번호순) →
   초안(draft_page) → 비교표·매트릭스·평가 절차 → 질문 백로그 → 로그 → 실험 순이며, 확장 아이디어 아래는 색인 → 아이디어 페이지(트랙 순)다.
불일치 시 diff 를 출력하고 exit 1.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import re
import sys
from collections import OrderedDict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import frontmatter as fm  # noqa: E402
from lib import paths  # noqa: E402
from lib.nav import build_nav, flatten_nav, load_mkdocs_yml, render_mkdocs_yml  # noqa: E402
from lib.source import load_source, split_cells  # noqa: E402
from lib.verbatim import TAG, strip_tags, untag  # noqa: E402

SRC = load_source()
CATEGORY_EXTRA_SECTIONS = ["참고 자료"]   # 여섯 섹션 뒤에 허용하는 번호 없는 보조 절(각주 정의) [가정]
AREA_SECTIONS = [
    "1. 한 줄 정의", "2. SCM 관점의 질문", "3. 왜 중요한가", "4. 핵심 개념과 용어",
    "5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)", "6. 대표 접근법과 기술",
    "7. 관련 표준·프레임워크·오픈소스", "8. 대표 연구와 자료",
    "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)",
    "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)", "11. 열린 질문",
    "12. 최근 업데이트 (자동)", "13. 참고 자료 (각주)",
]
CATEGORY_SECTIONS = ["핵심 질문", "개요", "세부 연구영역", "이 대분류의 핵심 포인트", "다른 대분류와의 연결", "최근 업데이트"]


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_hash(write: bool) -> list[str]:
    digest = sha256_of(paths.SOURCE_FILE)
    rel = paths.SOURCE_FILE.relative_to(paths.ROOT).as_posix()
    if write:
        paths.SOURCE_HASH_FILE.write_text(f"{digest}  {rel}\n", encoding="utf-8")
        print(f"[hash] 기록: {paths.SOURCE_HASH_FILE.relative_to(paths.ROOT)} = {digest[:16]}…")
        return []
    if not paths.SOURCE_HASH_FILE.exists():
        return [f"해시 파일 없음: {paths.SOURCE_HASH_FILE.relative_to(paths.ROOT)} (--write-hash 로 생성)"]
    recorded = paths.SOURCE_HASH_FILE.read_text(encoding="utf-8").split()[0]
    if recorded != digest:
        return [f"원문 변조 의심: sha256 불일치 (기록 {recorded[:16]}… / 현재 {digest[:16]}…) — {rel}"]
    return []


def sections(body: str) -> "OrderedDict[str, list[str]]":
    """'## ' 제목으로 나눈 섹션. 제목 앞부분(preamble)은 키 ''."""
    out: "OrderedDict[str, list[str]]" = OrderedDict()
    cur = ""
    out[cur] = []
    for line in body.split("\n"):
        if line.startswith("## "):
            cur = line[3:].strip()
            out[cur] = []
        else:
            out[cur].append(line)
    return out


def content_lines(lines: list[str]) -> list[str]:
    return [l for l in lines if l.strip()]


def diff(expected: str, actual: str, label: str, expected_label: str = "원문(파서)") -> str:
    d = difflib.unified_diff(expected.split("\n"), actual.split("\n"), expected_label, label, lineterm="", n=0)
    return "\n".join(d)


def check_area(no: int) -> list[str]:
    errs: list[str] = []
    a = SRC.area(no)
    cat = SRC.category_of(no)
    rel = paths.area_rel_path(no)
    p = paths.DOCS / rel
    if not p.exists():
        return [f"{rel}: 파일 없음"]
    meta, body = fm.read(p)
    if meta.get("title") != a.title:
        errs.append(f"{rel}: title 불일치\n{diff(a.title, str(meta.get('title')), 'title')}")
    if meta.get("category") != cat.title:
        errs.append(f"{rel}: category 불일치\n{diff(cat.title, str(meta.get('category')), 'category')}")
    if str(meta.get("area_no")) != str(no):
        errs.append(f"{rel}: area_no 불일치 ({meta.get('area_no')} != {no})")
    if meta.get("type") != "area":
        errs.append(f"{rel}: type 이 area 가 아님")
    secs = sections(body)
    heads = [h for h in secs if h]
    if heads != AREA_SECTIONS:
        errs.append(f"{rel}: 섹션 제목·순서 불일치\n{diff(chr(10).join(AREA_SECTIONS), chr(10).join(heads), '섹션')}")
        return errs
    # 상단 admonition: 소속 대분류 + 핵심 질문
    pre = "\n".join(secs[""])
    if f"# {a.title}" not in pre.split("\n"):
        errs.append(f"{rel}: H1 제목이 '{a.title}' 이 아님")
    if cat.core_question + " " + TAG not in pre:
        errs.append(f"{rel}: 상단 admonition 에 핵심 질문 원문이 없음\n  기대: {cat.core_question} {TAG}")
    if cat.title not in pre:
        errs.append(f"{rel}: 상단에 소속 대분류 '{cat.title}' 표기가 없음")
    # 섹션 1·2
    s1 = content_lines(secs[AREA_SECTIONS[0]])
    exp1 = a.what + " " + TAG
    if not s1 or s1[0] != exp1:
        errs.append(f"{rel}: 섹션 1 정의 불일치\n{diff(exp1, s1[0] if s1 else '', '섹션 1')}")
    s2 = content_lines(secs[AREA_SECTIONS[1]])
    exp2 = a.question + " " + TAG
    if not s2 or s2[0] != exp2:
        errs.append(f"{rel}: 섹션 2 질문 불일치\n{diff(exp2, s2[0] if s2 else '', '섹션 2')}")
    # 원문 주석 인용 블록
    quotes: list[str] = []
    cur: list[str] = []
    for line in secs[AREA_SECTIONS[1]] + [""]:
        if line.startswith(">"):
            cur.append(line[1:].lstrip(" "))
        elif cur:
            quotes.append("\n".join(cur))
            cur = []
    got = []
    for q in quotes:
        if not q.startswith("원문 주석: "):
            errs.append(f"{rel}: 인용 블록이 '원문 주석: ' 로 시작하지 않음: {q[:40]!r}")
            continue
        got.append(untag(q[len("원문 주석: "):]))
    exp_notes = SRC.area_notes(no)
    if got != exp_notes:
        errs.append(f"{rel}: 원문 주석 인용 불일치\n{diff(chr(10).join(exp_notes), chr(10).join(got), '원문 주석')}")
    return errs


def check_category(letter: str) -> list[str]:
    errs: list[str] = []
    cat = SRC.category(letter)
    rel = paths.category_index_rel(letter)
    p = paths.DOCS / rel
    if not p.exists():
        return [f"{rel}: 파일 없음"]
    meta, body = fm.read(p)
    if meta.get("title") != cat.title:
        errs.append(f"{rel}: title 불일치\n{diff(cat.title, str(meta.get('title')), 'title')}")
    if meta.get("type") != "category":
        errs.append(f"{rel}: type 이 category 가 아님")
    secs = sections(body)
    heads = [h for h in secs if h]
    n = len(CATEGORY_SECTIONS)
    if heads[:n] != CATEGORY_SECTIONS or heads[n:] not in ([], CATEGORY_EXTRA_SECTIONS):
        exp = CATEGORY_SECTIONS + CATEGORY_EXTRA_SECTIONS
        errs.append(f"{rel}: 섹션 제목·순서 불일치(허용: 4.3 여섯 섹션 + 선택적 '참고 자료')\n"
                    f"{diff(chr(10).join(exp), chr(10).join(heads), '섹션')}")
        return errs
    if f"# {cat.title}" not in secs[""]:
        errs.append(f"{rel}: H1 제목이 '{cat.title}' 이 아님")
    q = content_lines(secs["핵심 질문"])
    exp = cat.core_question + " " + TAG
    if not q or q[0] != exp:
        errs.append(f"{rel}: 핵심 질문 불일치\n{diff(exp, q[0] if q else '', '핵심 질문')}")
    o = content_lines(secs["개요"])
    exp = cat.intro_paragraph + " " + TAG
    if not o or o[0] != exp:
        errs.append(f"{rel}: 개요 불일치\n{diff(exp, o[0] if o else '', '개요')}")
    # 표: 원문 3열 대조
    rows = [l for l in secs["세부 연구영역"] if l.startswith("|")]
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    cells = [c for c in cells if not all(re.fullmatch(r":?-+:?", x) for x in c)]
    if not cells or cells[0][:3] != cat.table_header:
        errs.append(f"{rel}: 표 머리글 불일치: {cells[0][:3] if cells else None} != {cat.table_header}")
    got_rows = [c[:3] for c in cells[1:]]
    exp_rows = [[a.title_cell, a.what, a.question] for a in cat.table_rows]
    if got_rows != exp_rows:
        errs.append(f"{rel}: 세부 연구영역 표 불일치\n" + diff(
            chr(10).join(" | ".join(r) for r in exp_rows), chr(10).join(" | ".join(r) for r in got_rows), "표"))
    if TAG not in [l.strip() for l in secs["세부 연구영역"]]:
        errs.append(f"{rel}: 세부 연구영역 표 아래 {TAG} 줄이 없음")
    # 핵심 포인트
    pts = [untag(l) for l in content_lines(secs["이 대분류의 핵심 포인트"]) if l.endswith(" " + TAG)]
    if pts != cat.notes:
        errs.append(f"{rel}: 핵심 포인트 문단 불일치\n{diff(chr(10).join(cat.notes), chr(10).join(pts), '핵심 포인트')}")
    return errs


def check_verbatim_page(rel: str, chapter_no: int, extra_lines: list[str] | None = None) -> list[str]:
    p = paths.DOCS / rel
    if not p.exists():
        return [f"{rel}: 파일 없음"]
    _, body = fm.read(p)
    page_lines = set(strip_tags(body).split("\n"))
    missing = []
    for line in SRC.chapter_text(chapter_no).split("\n"):
        if line.strip() and line not in page_lines:
            missing.append(line)
    for line in extra_lines or []:
        if line not in page_lines:
            missing.append(line)
    if missing:
        return [f"{rel}: 원문 {chapter_no}장 줄 {len(missing)}개가 없거나 바뀜:\n" + "\n".join(f"  - {m}" for m in missing)]
    return []


def check_home() -> list[str]:
    rel = "index.md"
    p = paths.DOCS / rel
    if not p.exists():
        return [f"{rel}: 파일 없음"]
    _, body = fm.read(p)
    lines = strip_tags(body).split("\n")
    errs = []
    for label, exp in [("정의 문장", SRC.rop_definition_sentence), ("SCOR 문단", SRC.scor_paragraph),
                       ("범위 문장", SRC.scope_disclaimer_sentence)]:
        if exp not in lines:
            errs.append(f"{rel}: {label}이 원문 그대로 들어 있지 않음\n  기대: {exp}")
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines if l.startswith("| ") and ". " in l]
    got = {r[0]: r[:3] for r in rows if r and r[0][:1] in paths.CATEGORY_SLUGS and r[0][1:3] == ". "}
    for r in SRC.overview_table_rows:
        exp = [r["category_title"], r["core_question"], r["area_range"]]
        if got.get(r["category_title"]) != exp:
            errs.append(f"{rel}: 대분류 표 행 불일치\n{diff(' | '.join(exp), ' | '.join(got.get(r['category_title'], [])), '홈 표')}")
    return errs


def _source_lines_and_cells() -> set[str]:
    """원문의 모든 줄과 표 셀(태그가 붙은 줄이 이 집합에 있어야 한다)."""
    out: set[str] = set()
    for line in SRC.raw.split("\n"):
        out.add(line)
        if line.lstrip().startswith("|"):
            out.update(split_cells(line))
    # 사양서 4.1 이 따로 인용하라고 지정한 머리말 속 범위 문장(한 줄의 일부)
    out.add(SRC.scope_disclaimer_sentence)
    out.discard("")
    return out


_FOOTNOTE_TAIL = re.compile(r"(\[\^[^\]\s]+\])+$")
_FENCE = re.compile(r"^(```|~~~).*?^\1[ \t]*$", re.M | re.S)
QUOTE_LABELS = ("원문 주석: ",)   # 세부영역 페이지 인용 블록의 고정 라벨(check_area 가 요구하는 형식)


def tagged_text(line: str) -> str | None:
    """줄이 [분류원문] 태그 줄이면 구조 표식(들여쓰기, 인용 표식, 태그 뒤 각주, 고정 라벨)을 벗긴 원문 후보를,
    아니면(태그 없음 또는 표 아래 단독 태그 줄) None 을 돌려준다."""
    s = line.strip()
    while s.startswith(">"):
        s = s[1:].lstrip()
    s = _FOOTNOTE_TAIL.sub("", s).rstrip()
    if s == TAG or not s.endswith(" " + TAG):
        return None
    text = untag(s)
    for label in QUOTE_LABELS:
        if text.startswith(label):
            text = text[len(label):]
    return text


def check_tagged_lines(rel: str, allowed: set[str] | None = None) -> list[str]:
    """[분류원문] 태그가 붙은 줄(표 아래 단독 태그 줄 제외)이 모두 원문의 줄 또는 표 셀과 글자 단위로 같은지.
    코드 펜스 안(예시)은 검사하지 않는다."""
    p = paths.DOCS / rel
    if not p.exists():
        return [f"{rel}: 파일 없음"]
    _, body = fm.read(p)
    allowed = _source_lines_and_cells() if allowed is None else allowed
    bad = []
    for line in _FENCE.sub("", body).split("\n"):
        text = tagged_text(line)
        if text is not None and text not in allowed:
            bad.append(line)
    if bad:
        return [f"{rel}: 원문에 없는 문장에 {TAG} 태그가 붙어 있음 {len(bad)}줄:\n" + "\n".join(f"  - {b}" for b in bad)]
    return []


def all_doc_rels() -> list[str]:
    return [p.relative_to(paths.DOCS).as_posix() for p in sorted(paths.DOCS.rglob("*.md"))]


# 사양서 4.8 의 상위 순서(원문 그대로). 이 순서는 새 섹션이 생겨도 바꾸지 않는다
SPEC_48_ORDER = ["home", "about", *[f"cat:{l}" for l in paths.CATEGORY_LETTERS], "tracks", "topics", "glossary",
                 "references", "standards", "open-questions", "flow-matrix", "changelog", "metrics", "logs"]
# 4.8 목록 밖 섹션 → 바로 앞에 와야 하는 섹션 [가정]
NAV_EXTRA_AFTER = {"ideas": "tracks"}
NAV_TRAILING = ["corrections"]            # 4.8 목록 밖, 맨 뒤(로그 다음)에만 [가정]
FIRST_TRACK = "manual-capability-ontology"  # 첫 트랙(사양서 8.1). 트랙이 늘어도 맨 앞


def _nav_kind(item) -> str | None:
    """상위 내비 항목의 종류(경로에서 판단)."""
    pairs = flatten_nav([item])
    if not pairs:
        return None
    path = pairs[0][1]
    top = path.split("/", 1)[0]
    if path == "index.md":
        return "home"
    if top == "categories":
        m = re.match(r"categories/([a-g])-", path)
        return f"cat:{m.group(1).upper()}" if m else None
    if path.endswith(".md") and "/" not in path:
        return path[:-3]
    return {"about": "about", "tracks": "tracks", "ideas": "ideas", "topics": "topics", "glossary": "glossary",
            "references": "references", "standards": "standards", "logs": "logs"}.get(top)


def check_nav_structure(nav: list) -> list[str]:
    """내비 구조 검사: 4.8 원문 순서 보존 + 확장 아이디어 위치 + 트랙·아이디어 하위 순서."""
    errs: list[str] = []
    kinds = [_nav_kind(i) for i in nav]
    unknown = [str(next(iter(i))) if isinstance(i, dict) else str(i) for i, k in zip(nav, kinds)
               if k is None or (k not in SPEC_48_ORDER and k not in NAV_EXTRA_AFTER and k not in NAV_TRAILING)]
    if unknown:
        errs.append(f"mkdocs.yml: 4.8 순서에 없는 상위 내비 항목: {unknown}")
    if len(set(kinds)) != len(kinds):
        errs.append(f"mkdocs.yml: 상위 내비 항목이 중복됨: {kinds}")
    core = [k for k in kinds if k in SPEC_48_ORDER]
    if [SPEC_48_ORDER.index(k) for k in core] != sorted(SPEC_48_ORDER.index(k) for k in core):
        errs.append(f"mkdocs.yml: 사양서 4.8 순서가 바뀜 — 기대 순서 {[k for k in SPEC_48_ORDER if k in core]}, 실제 {core}")
    for extra, after in NAV_EXTRA_AFTER.items():
        if extra in kinds:
            i = kinds.index(extra)
            if i == 0 or kinds[i - 1] != after:
                errs.append(f"mkdocs.yml: '{extra}' 섹션은 '{after}' 바로 다음에 와야 한다(4.8 순서 사이에 끼우지 않는다): {kinds}")
    for t in NAV_TRAILING:
        if t in kinds and kinds[-1] != t:
            errs.append(f"mkdocs.yml: '{t}' 는 내비 맨 뒤에만 둔다: {kinds}")
    # 중점 연구 트랙: 트랙 정의 order 순, 첫 트랙이 맨 앞, 트랙마다 하위 순서
    if "tracks" in kinds:
        section = next(iter(nav[kinds.index("tracks")].values()))
        got_slugs = []
        for item in section:
            ps = [p for _, p in flatten_nav([item])]
            m = re.match(r"tracks/([^/]+)/", ps[0]) if ps else None
            got_slugs.append(m.group(1) if m else None)
        exp_slugs = [s for s in paths.ordered_track_slugs() if (paths.DOCS / "tracks" / s).is_dir()]
        if got_slugs != exp_slugs:
            errs.append(f"mkdocs.yml: 중점 연구 트랙 순서가 트랙 정의(order)와 다름: 기대 {exp_slugs}, 실제 {got_slugs}")
        if FIRST_TRACK in exp_slugs and got_slugs[:1] != [FIRST_TRACK]:
            errs.append(f"mkdocs.yml: 첫 트랙({FIRST_TRACK})이 중점 연구 트랙 맨 앞에 있어야 한다: {got_slugs}")
        for slug, item in zip(got_slugs, section):
            if not slug:
                continue
            names = [p.split("/", 2)[2] for _, p in flatten_nav([item]) if p.startswith(f"tracks/{slug}/")]
            stages = [n for n in names if n.startswith("stage-")]
            order = ["index.md", *stages, *paths.track_page_order(slug)[1:]]
            known = [n for n in names if n in order]
            if names[:1] != ["index.md"]:
                errs.append(f"mkdocs.yml: 트랙 {slug} 의 첫 항목이 개요(index.md)가 아님: {names[:1]}")
            if [order.index(n) for n in known] != sorted(order.index(n) for n in known):
                errs.append(f"mkdocs.yml: 트랙 {slug} 하위 순서가 4.8(개요 → 단계 → 초안 → 산출물 → 백로그 → 로그 → 실험)과 다름: {names}")
            nums = [int(re.match(r"stage-(\d+)", n).group(1)) for n in stages]
            if nums != sorted(nums):
                errs.append(f"mkdocs.yml: 트랙 {slug} 단계 페이지가 번호순이 아님: {stages}")
    # 확장 아이디어: 색인 → 아이디어 페이지(트랙 순)
    if "ideas" in kinds:
        got = [p for _, p in flatten_nav([nav[kinds.index("ideas")]])]
        exp = [paths.IDEAS_INDEX] + [r for r in paths.idea_page_rels() if (paths.DOCS / r).is_file()]
        if got[:len(exp)] != exp:
            errs.append(f"mkdocs.yml: 확장 아이디어 하위 순서가 다름: 기대 {exp}, 실제 {got}")
    return errs


def check_nav() -> list[str]:
    if not paths.MKDOCS_YML.exists():
        return ["mkdocs.yml 없음"]
    cfg = load_mkdocs_yml()
    pairs = flatten_nav(cfg.get("nav") or [])
    by_path = {path: label for label, path in pairs}
    errs = []
    # 파일 전체가 현재 파일시스템 기준 생성 결과와 같은가 (4.8 순서, 누락 페이지, 템플릿)
    actual = paths.MKDOCS_YML.read_text(encoding="utf-8")
    if actual != render_mkdocs_yml():
        exp_pairs = flatten_nav(build_nav())
        hint = "`python3 pipeline/scaffold.py --refresh-auto` 로 mkdocs.yml 을 재생성한다"
        if exp_pairs != pairs:
            fmt = lambda ps: "\n".join(f"{l or ''}: {p}" for l, p in ps)  # noqa: E731
            errs.append(f"mkdocs.yml: 내비게이션이 현재 페이지 기준 생성 결과(사양서 4.8 순서)와 다름 — {hint}\n"
                        f"{diff(fmt(exp_pairs), fmt(pairs), 'mkdocs.yml nav', 'nav.build_nav() 생성 결과')}")
        else:
            errs.append(f"mkdocs.yml: nav 밖의 설정이 pipeline/lib/nav.py 의 템플릿과 다름 — {hint}")
    for cat in SRC.categories:
        idx = paths.category_index_rel(cat.letter)
        if idx not in by_path:
            errs.append(f"mkdocs.yml: 내비에 {idx} 없음")
        elif by_path[idx] != cat.title:
            errs.append(f"mkdocs.yml: 대분류 라벨 불일치 {by_path[idx]!r} != {cat.title!r}")
    for no in paths.AREA_NOS:
        rel = paths.area_rel_path(no)
        if rel not in by_path:
            errs.append(f"mkdocs.yml: 내비에 {rel} 없음")
        elif by_path[rel] != SRC.area(no).title:
            errs.append(f"mkdocs.yml: 세부영역 라벨 불일치 {by_path[rel]!r} != {SRC.area(no).title!r}")
    # 구조 검사는 저장된 mkdocs.yml 과 생성기(build_nav) 결과 둘 다에 적용한다(생성기 자체의 순서 회귀도 잡는다)
    errs += check_nav_structure(cfg.get("nav") or [])
    errs += [f"[생성기] {e}" for e in check_nav_structure(build_nav())]
    return errs


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write-hash", action="store_true", help="원문 sha256 을 기록한다")
    ap.add_argument("--skip-nav", action="store_true", help="mkdocs.yml 내비 검사를 건너뛴다")
    args = ap.parse_args(argv)

    errs: list[str] = []
    errs += check_hash(args.write_hash)
    for no in paths.AREA_NOS:
        errs += check_area(no)
    for letter in paths.CATEGORY_LETTERS:
        errs += check_category(letter)
    errs += check_home()
    errs += check_verbatim_page("about/what-is-rop.md", 1)
    errs += check_verbatim_page("about/scope-boundary.md", 9)
    errs += check_verbatim_page("about/idea-mapping.md", 10)
    errs += check_verbatim_page("about/research-method.md", 11)
    allowed = _source_lines_and_cells()
    rels = all_doc_rels()
    for rel in rels:
        errs += check_tagged_lines(rel, allowed)
    if not args.skip_nav:
        errs += check_nav()

    if errs:
        print(f"[protect_source] 불일치 {len(errs)}건")
        for e in errs:
            print("-", e)
        return 1
    print(f"[protect_source] 통과: 세부영역 28 · 대분류 7 · 홈·소개 5 · 태그 줄 원문 대조(docs 전체 {len(rels)}개 페이지) · "
          "내비(라벨·4.8 순서·재생성 일치) · 원문 해시")
    return 0


if __name__ == "__main__":
    sys.exit(main())
