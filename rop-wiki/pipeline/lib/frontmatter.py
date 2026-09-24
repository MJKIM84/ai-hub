"""YAML 프런트매터 읽기·쓰기와 필수 필드 상수(사양서 5.1·5.2).

- read(path) -> (meta, body). 날짜 값은 항상 ISO 문자열로 돌려준다.
- write(path, meta, body). ISO 날짜 문자열은 따옴표 없는 날짜로, title/category 는 큰따옴표로 쓴다.
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
]

STATUS_VALUES: list[str] = ["seed", "draft", "verified", "published", "needs_update", "deprecated"]

CONFIDENCE_VALUES: list[str] = ["high", "medium", "low"]

TRACK_SUBTYPES: list[str] = ["comparison", "matrix", "evaluation", "experiments"]

# type 별 추가 필수 필드. subtype: index 인 목록 페이지(topics/index.md 등)는 면제한다. [가정]
TYPE_REQUIRED: dict[str, list[str]] = {
    "area": ["category", "area_no"],
    "topic": ["primary_area_no"],
    "glossary": ["term_ko", "definition"],
    "reference": ["ref_id", "org", "url", "source_type", "reliability", "published", "accessed"],
    "track": ["track"],
    "track-stage": ["track", "stage"],
    "ontology-draft": ["track"],
    "track-log": ["track"],
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
        if isinstance(v, str) and _ISO_DATE.match(v):
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
    if t == "track" and "subtype" in meta and meta["subtype"] not in TRACK_SUBTYPES + ["index"]:
        errs.append(f"track subtype 값 오류: {meta['subtype']!r}")
    if meta.get("subtype") != "index":
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
