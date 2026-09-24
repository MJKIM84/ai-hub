"""분류 원문(_source/ROP_SCM_연구분야_분류.md) 파서.

원문에서 옮기는 문장은 사람이 손으로 쓰지 않고 이 파서가 읽은 값을 그대로 출력해
글자 단위 일치를 보장한다. 파서는 표의 굵게(**…**)를 제목(title)에서만 제거하고,
셀 본문·문단은 원문 그대로 둔다. 원문의 각주 표기 "[3]" 같은 것도 그대로 보존한다.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

from .paths import SOURCE_FILE
from .verbatim import split_blocks, strip_bold

_CHAPTER = re.compile(r"^## (\d+)\. (.*)$")
_CAT_HEADING = re.compile(r"^([A-G]) — (.+)$")
_AREA_TITLE = re.compile(r"^(\d+)\. (.+)$")
_NBUN = re.compile(r"(\d+(?:·\d+)*)번")
_CITE = re.compile(r"\[(\d+)\]")
_REF_LINE = re.compile(r"^(?P<n>\d+)\. (?P<org>.+?) \[(?P<title>[^\]]+)\]\((?P<url>[^)]+)\)(?P<rest>.*)$")
_REF_REST = re.compile(r"^(?:, (?P<year>\d{4}))?\.\s*(?P<note>.*)$")
_DISCLAIMER = re.compile(r"공식 단일 분류가 아니라[^\n]*?의미는 아니다\.")


def _is_sep_row(cells: list[str]) -> bool:
    return all(re.fullmatch(r":?-+:?", c) for c in cells)


def split_cells(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def parse_table(block: list[str]) -> tuple[list[str], list[list[str]]]:
    """표 블록 → (헤더 셀, 본문 행 목록). 구분선 행은 제외한다."""
    rows = [split_cells(l) for l in block if l.lstrip().startswith("|")]
    header = rows[0] if rows else []
    body = [r for r in rows[1:] if not _is_sep_row(r)]
    return header, body


@dataclass
class Area:
    no: int
    name: str
    title: str              # "7. 화물·재고·자산 식별과 추적" (굵게 제거)
    title_cell: str         # "**7. 화물·재고·자산 식별과 추적**" (원문 셀 그대로)
    what: str               # 무엇을 연구하는가 (원문 셀 그대로)
    question: str           # SCM 관점의 질문 (원문 셀 그대로)
    category_letter: str


@dataclass
class Category:
    letter: str
    name: str
    title: str              # "A. 업무·공급망 설계" (1장 표 표기)
    heading: str            # "A — 업무·공급망 설계" (장 제목 표기)
    chapter_no: int
    core_question: str      # 1장 표 문장 그대로
    area_range: str         # 1장 표 "1–4" 그대로
    area_nos: list[int]
    intro_paragraph: str    # 표 앞 첫 문단, 원문 그대로(굵게 포함)
    table_header: list[str]
    table_rows: list[Area]
    notes: list[str]        # 표 아래 문단들, 원문 그대로


@dataclass
class Reference:
    n: int
    org: str
    title: str
    url: str
    note: str
    year: int | None
    raw: str                # 원문 목록 줄 그대로("1. ASCM. [SCOR …](…). … 참고.")

    @property
    def id(self) -> str:
        return f"ref-{self.n:03d}"

    @property
    def published(self) -> str:
        return str(self.year) if self.year else "미확인"

    def footnote(self, accessed: str) -> str:
        """각주 정의 한 줄: "[^ref-003]: 기관, 제목, 발행일, URL, 접근일"."""
        return f"[^{self.id}]: {self.org}, {self.title}, {self.published}, {self.url}, 접근일 {accessed}"


@dataclass
class Source:
    path: Path
    raw: str
    doc_title: str
    header_block: str                       # 1장 앞 머리말(제목 줄 제외) 원문
    chapters: dict[int, tuple[str, str]]    # n -> (heading, body)
    categories: list[Category] = field(default_factory=list)
    areas: dict[int, Area] = field(default_factory=dict)
    references: list[Reference] = field(default_factory=list)
    overview_table_header: list[str] = field(default_factory=list)
    overview_table_rows: list[dict] = field(default_factory=list)   # category_title, core_question, area_range
    rop_definition_sentence: str = ""
    scor_paragraph: str = ""
    scope_disclaimer_sentence: str = ""
    scope_table_header: list[str] = field(default_factory=list)
    scope_rows: list[dict] = field(default_factory=list)            # 경계, rop, external
    idea_table_header: list[str] = field(default_factory=list)
    idea_rows: list[dict] = field(default_factory=list)             # idea, primary, related
    references_intro: str = ""

    # --- 조회 ---------------------------------------------------------------
    def chapter_text(self, n: int) -> str:
        """원문 n장 본문(제목 제외). 앞뒤 빈 줄만 제거하고 나머지는 원문 그대로."""
        return self.chapters[n][1]

    def chapter_heading(self, n: int) -> str:
        return self.chapters[n][0]

    def category(self, letter: str) -> Category:
        for c in self.categories:
            if c.letter == letter:
                return c
        raise KeyError(letter)

    def category_of(self, no: int) -> Category:
        return self.category(self.areas[int(no)].category_letter)

    def area(self, no: int) -> Area:
        return self.areas[int(no)]

    def reference(self, n: int) -> Reference:
        for r in self.references:
            if r.n == int(n):
                return r
        raise KeyError(n)

    def area_notes(self, no: int) -> list[str]:
        """표 아래 문단 중 "N번" 패턴으로 이 세부영역을 명시적으로 언급하는 문단(원문 그대로)."""
        no = int(no)
        out: list[str] = []
        for cat in self.categories:
            for para in cat.notes:
                if no in mentioned_area_nos(para):
                    out.append(para)
        return out

    def notes_without_area(self) -> dict[str, list[str]]:
        """어떤 세부영역도 명시하지 않는 문단(대분류 핵심 포인트에만 두는 문단)."""
        return {c.letter: [p for p in c.notes if not mentioned_area_nos(p)] for c in self.categories}

    @staticmethod
    def citations(text: str) -> list[int]:
        """본문에 있는 원문 각주 표기 [n] 의 n 목록(등장 순, 중복 제거)."""
        seen: list[int] = []
        for m in _CITE.finditer(text):
            n = int(m.group(1))
            if n not in seen:
                seen.append(n)
        return seen


def mentioned_area_nos(paragraph: str) -> list[int]:
    """문단에서 "7번", "5·21번" 처럼 명시적으로 언급된 세부영역 번호(등장 순, 중복 제거)."""
    out: list[int] = []
    for m in _NBUN.finditer(paragraph):
        for part in m.group(1).split("·"):
            n = int(part)
            if n not in out:
                out.append(n)
    return out


def _split_chapters(raw: str) -> tuple[str, dict[int, tuple[str, str]]]:
    lines = raw.split("\n")
    header: list[str] = []
    chapters: dict[int, tuple[str, str]] = {}
    cur_no: int | None = None
    cur_head = ""
    cur: list[str] = []

    def flush():
        if cur_no is not None:
            chapters[cur_no] = (cur_head, "\n".join(cur).strip("\n"))

    for line in lines:
        m = _CHAPTER.match(line)
        if m:
            flush()
            cur_no = int(m.group(1))
            cur_head = m.group(2)
            cur = []
        elif cur_no is None:
            header.append(line)
        else:
            cur.append(line)
    flush()
    return "\n".join(header), chapters


def parse(raw: str, path: Path = SOURCE_FILE) -> Source:
    header, chapters = _split_chapters(raw)
    title_m = re.search(r"^# (.+)$", header, re.M)
    doc_title = title_m.group(1).strip() if title_m else ""
    header_block = "\n".join(l for l in header.split("\n") if not l.startswith("# ")).strip("\n")
    src = Source(path=path, raw=raw, doc_title=doc_title, header_block=header_block, chapters=chapters)

    dm = _DISCLAIMER.search(header)
    src.scope_disclaimer_sentence = dm.group(0) if dm else ""

    # 1장: 정의 문장, 개요 표, SCOR 문단
    ch1 = src.chapter_text(1)
    blocks1 = split_blocks(ch1)
    src.rop_definition_sentence = "\n".join(blocks1[0])
    for b in blocks1:
        if b[0].lstrip().startswith("|"):
            hdr, rows = parse_table(b)
            src.overview_table_header = hdr
            src.overview_table_rows = [
                {"category_title": r[0], "core_question": r[1], "area_range": r[2]} for r in rows
            ]
        elif b[0].startswith("ASCM의 SCOR"):
            src.scor_paragraph = "\n".join(b)
    overview_by_letter = {r["category_title"][0]: r for r in src.overview_table_rows}

    # 2~8장: 대분류
    for n in sorted(chapters):
        heading = src.chapter_heading(n)
        cm = _CAT_HEADING.match(heading)
        if not cm:
            continue
        letter, name = cm.group(1), cm.group(2)
        blocks = split_blocks(src.chapter_text(n))
        intro = ""
        table_header: list[str] = []
        areas: list[Area] = []
        notes: list[str] = []
        seen_table = False
        for b in blocks:
            if b[0].lstrip().startswith("|"):
                table_header, rows = parse_table(b)
                for r in rows:
                    t = strip_bold(r[0])
                    am = _AREA_TITLE.match(t)
                    if not am:
                        raise ValueError(f"세부영역 제목 형식 오류: {r[0]!r}")
                    areas.append(Area(
                        no=int(am.group(1)), name=am.group(2), title=t, title_cell=r[0],
                        what=r[1], question=r[2], category_letter=letter,
                    ))
                seen_table = True
            elif not seen_table and not intro:
                intro = "\n".join(b)
            else:
                notes.append("\n".join(b))
        ov = overview_by_letter[letter]
        cat = Category(
            letter=letter, name=name, title=ov["category_title"], heading=heading, chapter_no=n,
            core_question=ov["core_question"], area_range=ov["area_range"],
            area_nos=[a.no for a in areas], intro_paragraph=intro,
            table_header=table_header, table_rows=areas, notes=notes,
        )
        src.categories.append(cat)
        for a in areas:
            src.areas[a.no] = a

    # 9장: 범위 경계 표
    for b in split_blocks(src.chapter_text(9)):
        if b[0].lstrip().startswith("|"):
            hdr, rows = parse_table(b)
            src.scope_table_header = hdr
            src.scope_rows = [{"경계": r[0], "rop": r[1], "external": r[2]} for r in rows]

    # 10장: 아이디어 매핑 표
    for b in split_blocks(src.chapter_text(10)):
        if b[0].lstrip().startswith("|"):
            hdr, rows = parse_table(b)
            src.idea_table_header = hdr
            src.idea_rows = [{"idea": r[0], "primary": r[1], "related": r[2]} for r in rows]

    # 12장: 참고 자료
    blocks12 = split_blocks(src.chapter_text(12))
    if blocks12 and not re.match(r"^\d+\. ", blocks12[0][0]):
        src.references_intro = "\n".join(blocks12[0])
    for b in blocks12:
        for line in b:
            m = _REF_LINE.match(line)
            if not m:
                continue
            rest = _REF_REST.match(m.group("rest"))
            if not rest:
                raise ValueError(f"참고 자료 줄 형식 오류: {line!r}")
            org_raw = m.group("org")
            org = org_raw if re.search(r" [A-Z]\.$", org_raw) else org_raw.rstrip(".")
            src.references.append(Reference(
                n=int(m.group("n")), org=org, title=m.group("title"), url=m.group("url"),
                note=rest.group("note").strip(), year=int(rest.group("year")) if rest.group("year") else None,
                raw=line,
            ))
    return src


@lru_cache(maxsize=4)
def load_source(path: Path | str = SOURCE_FILE) -> Source:
    p = Path(path)
    return parse(p.read_text(encoding="utf-8"), p)
