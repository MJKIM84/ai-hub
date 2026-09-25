"""YAML 프런트매터 읽기·쓰기와 필수 필드 상수(사양서 5.1·5.2).

- read(path) -> (meta, body). 날짜 값은 항상 ISO 문자열로 돌려준다.
- write(path, meta, body). 날짜 필드(DATE_KEYS)의 ISO 날짜 문자열은 따옴표 없는 날짜로, title/category 는 큰따옴표로 쓴다.
  날짜 필드가 아닌 값은 ISO 날짜 모양이어도 문자열로 남긴다(예: 일일 로그의 title "2026-09-25").
"""
from __future__ import annotations

import re
from datetime import date, datetime
from pathlib import Path

import yaml

REQUIRED: list[str] = ["title", "type", "status", "created", "updated", "version"]

TYPE_VALUES: list[str] = [
    "home", "about", "category", "area", "topic", "glossary", "reference", "standard",
    "questions", "matrix", "changelog", "metrics", "log", "track", "track-stage",
    "ontology-draft", "track-log",
    # 구축자 추가 유형 [가정]: 확장 아이디어 페이지(docs/ideas/). 색인(ideas/index.md)은 subtype: index
    "idea",
]

STATUS_VALUES: list[str] = ["seed", "draft", "verified", "published", "needs_update", "deprecated"]

CONFIDENCE_VALUES: list[str] = ["high", "medium", "low"]

TRACK_SUBTYPES: list[str] = ["comparison", "matrix", "evaluation", "experiments"]

# subtype: index(색인 페이지)를 둘 수 있는 type. 이 type 의 색인 페이지(glossary/index.md, references/index.md, standards/index.md,
# topics/index.md, logs/index.md)만 아래 유형별 추가 필수 필드를 면제한다 [가정]
INDEX_SUBTYPE_TYPES: list[str] = ["glossary", "reference", "standard", "topic", "log", "idea"]

# 프런트매터 날짜 필드. dumps() 는 이 키의 ISO 날짜 문자열만 따옴표 없는 날짜로 쓴다
DATE_KEYS: tuple[str, ...] = ("created", "updated", "accessed", "last_run", "published")

# 본문 첫 줄의 이동 경로(공통 컨텍스트, 사양서 4.8): "[홈](…) › …" 또는 홈 페이지의 "홈" 한 단어
BREADCRUMB_RE = re.compile(r"^(\[홈\]\([^)\s]+\)|홈)( › .+)?$")

# type 별 추가 필수 필드. subtype: index 인 목록 페이지(topics/index.md 등, INDEX_SUBTYPE_TYPES)는 면제한다. [가정]
TYPE_REQUIRED: dict[str, list[str]] = {
    "area": ["category", "area_no"],
    "topic": ["primary_area_no"],
    "glossary": ["term_ko", "definition"],
    "reference": ["ref_id", "org", "url", "source_type", "reliability", "published", "accessed"],
    "track": ["track"],
    "track-stage": ["track", "stage"],
    "ontology-draft": ["track"],
    "track-log": ["track"],
    "idea": ["track"],          # 아이디어 페이지는 그 아이디어를 연구하는 트랙 slug 를 가진다(색인은 면제) [가정]
}

_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_FM = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)


class _Quoted(str):
    """큰따옴표로 출력할 문자열."""


def _quoted_representer(dumper: yaml.SafeDumper, data: _Quoted):
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style='"')


class _Dumper(yaml.SafeDumper):
    pass


_Dumper.add_representer(_Quoted, _quoted_representer)


def _normalize_loaded(meta: dict) -> dict:
    out = {}
    for k, v in meta.items():
        if isinstance(v, datetime):
            v = v.date().isoformat()
        elif isinstance(v, date):
            v = v.isoformat()
        out[k] = v
    return out


def parse(text: str) -> tuple[dict, str]:
    """문자열에서 (meta, body) 를 분리한다. 프런트매터가 없으면 ({}, text)."""
    m = _FM.match(text)
    if not m:
        return {}, text
    meta = yaml.safe_load(m.group(1)) or {}
    if not isinstance(meta, dict):
        raise ValueError("프런트매터가 매핑이 아니다")
    return _normalize_loaded(meta), text[m.end():]


def read(path: Path | str) -> tuple[dict, str]:
    return parse(Path(path).read_text(encoding="utf-8"))


def dumps(meta: dict, body: str) -> str:
    prepared = {}
    for k, v in meta.items():
        if k in DATE_KEYS and isinstance(v, str) and _ISO_DATE.match(v):
            v = date.fromisoformat(v)
        elif k in ("title", "category") and isinstance(v, str):
            v = _Quoted(v)
        prepared[k] = v
    fm = yaml.dump(
        prepared, Dumper=_Dumper, allow_unicode=True, sort_keys=False,
        default_flow_style=None, width=1000,
    )
    body = body.lstrip("\n")
    return f"---\n{fm}---\n\n{body}" if body else f"---\n{fm}---\n"


def write(path: Path | str, meta: dict, body: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(dumps(meta, body), encoding="utf-8")


def validate(meta: dict, path: str = "") -> list[str]:
    """필수 필드·허용 값 검사. 문제 목록을 돌려준다(비어 있으면 통과)."""
    errs: list[str] = []
    for k in REQUIRED:
        if k not in meta or meta[k] in (None, ""):
            errs.append(f"필수 필드 없음: {k}")
    t = meta.get("type")
    if t is not None and t not in TYPE_VALUES:
        errs.append(f"type 값 오류: {t!r}")
    s = meta.get("status")
    if s is not None and s not in STATUS_VALUES:
        errs.append(f"status 값 오류: {s!r}")
    c = meta.get("confidence")
    if c is not None and c not in CONFIDENCE_VALUES:
        errs.append(f"confidence 값 오류: {c!r}")
    for k in ("created", "updated", "accessed", "last_run"):
        v = meta.get(k)
        if v is not None and not (isinstance(v, str) and _ISO_DATE.match(v)):
            errs.append(f"{k} 는 YYYY-MM-DD 형식이어야 한다: {v!r}")
    v = meta.get("version")
    if v is not None and not isinstance(v, (int, float, str)):
        errs.append(f"version 값 오류: {v!r}")
    sub = meta.get("subtype")
    if t == "track" and "subtype" in meta and sub not in TRACK_SUBTYPES + ["index"]:
        errs.append(f"track subtype 값 오류: {sub!r}")
    elif t != "track" and "subtype" in meta:
        if sub != "index":
            errs.append(f"subtype 값 오류: type={t} 에는 subtype: index 만 쓸 수 있다({sub!r})")
        elif t not in INDEX_SUBTYPE_TYPES:
            errs.append(f"subtype: index 는 색인 페이지 유형({', '.join(INDEX_SUBTYPE_TYPES)})에만 쓴다(type={t})")
    index_exempt = sub == "index" and t in INDEX_SUBTYPE_TYPES + ["track"]
    if not index_exempt:
        for k in TYPE_REQUIRED.get(t, []):
            if k not in meta or meta[k] in (None, ""):
                errs.append(f"type={t} 추가 필수 필드 없음: {k}")
    if t == "area":
        try:
            int(meta.get("area_no"))
        except (TypeError, ValueError):
            errs.append(f"area_no 는 정수여야 한다: {meta.get('area_no')!r}")
    if s == "deprecated" and not meta.get("replaced_by"):
        errs.append("deprecated 페이지는 replaced_by(대체 페이지 링크)가 필요하다")
    return errs
