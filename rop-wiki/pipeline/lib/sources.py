"""출처 원문 처리 공용 모듈 — 원문 미러, 원문 텍스트, 원문 열람 상한, 참고문헌 페이지의 열람 상태.

표준 라이브러리 + pyyaml 만 쓴다. 네트워크가 막혔는지는 이 모듈이 가정하지 않는다(실행할 때 check_urls.py 가 확인한다).

공개 API
- mirror_for(url) -> list[str]                원문 미러(raw.githubusercontent.com) URL. config/source_mirrors.yaml + github.com blob 변환
- mirror_entries(url) -> list[dict]           위와 같되 relation(original|official_artifact|related)·repo·note 까지
- load_source_texts() -> dict[key, meta]      data/source_texts/index.json (key 는 ref_id, 참고문헌과 연결되지 않은 텍스트는 src-<slug>)
- source_text_excerpt(ref_id, max_chars) -> str | None
- select_texts_for_prompt(ref_ids, keywords, max_total_chars) -> list[(key, text)]   인용 중인 출처 먼저, 그다음 키워드 일치
- format_texts_for_prompt(pairs) -> str      위 결과를 프롬프트 입력 절(### 소제목 + 코드 펜스)로
- apply_fetch_caps(research) -> list[str]    원문 열람 여부로 신뢰도 상한을 코드로 강제한다(제자리 수정, 한국어 로그 줄 반환)
- fetch_label(meta) -> str                   "원문 열람(<경로>)" 또는 "원문 미열람"
- render_reference_fetch_status(ref_meta) -> str   참고문헌 페이지의 원문 열람 상태 블록(마크다운)
- load_url_check(), url_check_counts(), url_check_summary_line()   data/url_check.json 읽기(구 형식 호환)
- extract_text_file(path), store_source_text(...), ingest_url(...), ingest_mirror_texts(...), sync_reference_page(...)
  inbox/sources 수집(pipeline/ingest_sources.py)과 scaffold.py --apply-url-check 가 쓰는 하위 함수

원문 열람(fetched)의 뜻: 출처 본문을 실제로 읽었다(에이전트 WebFetch, raw.githubusercontent.com 의 같은 문서 원본,
사람이 inbox/sources 에 넣은 파일). 검색 결과 요약만 봤거나, URL 이 열리는지만 확인했거나, 같은 표준의 다른 산출물(스키마·온톨로지)을
연 것은 원문 열람이 아니다. 원문 미열람 출처의 신뢰도는 medium 이 상한이다.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import ssl
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

import yaml

from . import frontmatter as fm
from . import paths

# --- 상수 -------------------------------------------------------------------------------------

FETCHED_VIA: tuple[str, ...] = ("webfetch", "github_raw", "inbox")
VIA_LABELS: dict[str, str] = {
    "webfetch": "웹 열람(WebFetch)",
    "github_raw": "GitHub raw 미러",
    "inbox": "사용자 제공 파일(inbox)",
}
URL_STATUSES: tuple[str, ...] = ("열림", "없음", "정책 차단", "오류")
MIRROR_RELATIONS: tuple[str, ...] = ("original", "official_artifact", "related")
RELATION_LABELS: dict[str, str] = {
    "original": "같은 문서의 원본",
    "official_artifact": "공식 산출물(정본 페이지 본문 아님)",
    "related": "관련 자료(정본 문서 아님)",
}
# 원문 미열람 출처의 신뢰도 상한과 출처 유형별 기준값(scaffold.py REF_RELIABILITY 와 같은 값 + 사양서 6.1 유형 7종)
CAP = "medium"
RELIABILITY_ORDER: dict[str, int] = {"low": 0, "medium": 1, "high": 2}
RELIABILITY_BY_TYPE: dict[str, str] = {
    "표준": "high", "논문": "high", "정부·연구기관": "high", "오픈소스 문서": "high",
    "업계 보고서": "medium", "벤더 문서": "medium", "기사": "medium",
}
RAW_HOST = "raw.githubusercontent.com"

# 참고문헌 페이지의 원문 열람 상태 블록 마커. auto: 접두어가 아니므로 퍼블리셔의 자동 영역(AUTO_KEYS) 검사 대상이 아니며,
# 이 모듈(sync_reference_page)만 마커 사이를 다시 쓴다.
FETCH_BLOCK_START = "<!-- source-fetch:start -->"
FETCH_BLOCK_END = "<!-- source-fetch:end -->"
_FETCH_BLOCK_RE = re.compile(re.escape(FETCH_BLOCK_START) + r".*?" + re.escape(FETCH_BLOCK_END), re.S)

TEXT_SUFFIXES = {".txt", ".md", ".markdown", ".rst", ".adoc", ".ttl", ".owl", ".xml", ".json", ".jsonld", ".yaml", ".yml",
                 ".csv", ".schema", ".tex"}
HTML_SUFFIXES = {".html", ".htm", ".xhtml"}
PDF_SUFFIXES = {".pdf"}
_KEY_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{0,80}$")
_REF_RE = re.compile(r"^ref-\d{3,}$")
UA = "rop-wiki-sources/1.0 (+pipeline/lib/sources.py)"


# --- 경로 ------------------------------------------------------------------------------------

class Layout:
    """위키 루트 기준 경로 묶음. 테스트는 임시 폴더를 root 로 준다."""

    def __init__(self, root: Path | str | None = None):
        self.root = Path(root) if root else paths.ROOT

    @property
    def mirrors_file(self) -> Path:
        return self.root / "config" / "source_mirrors.yaml"

    @property
    def texts_dir(self) -> Path:
        return self.root / "data" / "source_texts"

    @property
    def texts_index(self) -> Path:
        return self.texts_dir / "index.json"

    @property
    def url_check_file(self) -> Path:
        return self.root / "data" / "url_check.json"

    @property
    def references_dir(self) -> Path:
        return self.root / "docs" / "references"

    @property
    def inbox_dir(self) -> Path:
        return self.root / "inbox" / "sources"

    @property
    def changelog_file(self) -> Path:
        return self.root / "data" / "changelog.json"

    def rel(self, p: Path) -> str:
        try:
            return Path(p).resolve().relative_to(self.root.resolve()).as_posix()
        except ValueError:
            return Path(p).as_posix()


def _today(today: str | None = None) -> str:
    return today or paths.today()


# --- URL 정규화와 미러 ----------------------------------------------------------------------------

def normalize_url(url: str) -> str:
    """비교용 정규형: scheme·www.·#조각·끝 슬래시를 떼고, 호스트는 소문자, 경로는 퍼센트 인코딩을 푼다. 호스트만 준 값도 받는다."""
    u = str(url or "").strip()
    if not u:
        return ""
    parts = urllib.parse.urlsplit(u if "://" in u else "//" + u)
    host = (parts.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    try:
        port = parts.port
    except ValueError:
        port = None
    hostport = host + (f":{port}" if port and port not in (80, 443) else "")
    path = urllib.parse.unquote(parts.path or "").rstrip("/")
    q = f"?{parts.query}" if parts.query else ""
    return f"{hostport}{path}{q}"


def url_matches(url: str, match: str) -> bool:
    """match(정본 URL 접두어 또는 호스트)가 url 을 덮는가. 경로 경계(/ ? 또는 끝)에서만 접두어로 인정한다."""
    nu, nm = normalize_url(url), normalize_url(match)
    if not nu or not nm:
        return False
    if nu == nm or nu in (nm + ".html", nm + ".htm"):
        return True
    return nu.startswith(nm + "/") or nu.startswith(nm + "?")


def github_blob_to_raw(url: str) -> str | None:
    """github.com/<owner>/<repo>/(blob|raw)/<ref>/<path> → raw.githubusercontent.com/<owner>/<repo>/<ref>/<path>. 아니면 None."""
    p = urllib.parse.urlsplit(str(url or "").strip())
    if (p.hostname or "").lower() not in ("github.com", "www.github.com"):
        return None
    seg = [s for s in p.path.split("/") if s]
    if len(seg) >= 5 and seg[2] in ("blob", "raw"):
        return f"https://{RAW_HOST}/{seg[0]}/{seg[1]}/{'/'.join(seg[3:])}"
    return None


def is_raw_github(url: str) -> bool:
    return (urllib.parse.urlsplit(str(url or "")).hostname or "").lower() == RAW_HOST


_MIRROR_CACHE: dict[str, tuple[float, list[dict]]] = {}


def load_mirrors(root: Path | str | None = None) -> list[dict]:
    """config/source_mirrors.yaml 의 mirrors 목록(항목마다 match 는 목록으로 맞춘다). 파일이 없거나 깨졌으면 []."""
    f = Layout(root).mirrors_file
    try:
        mtime = f.stat().st_mtime
    except OSError:
        return []
    key = str(f)
    hit = _MIRROR_CACHE.get(key)
    if hit and hit[0] == mtime:
        return hit[1]
    try:
        d = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        return []
    out: list[dict] = []
    for e in d.get("mirrors") or []:
        if not isinstance(e, dict):
            continue
        m = e.get("match")
        matches = [str(x) for x in (m if isinstance(m, list) else [m]) if x]
        raws = [str(x) for x in e.get("raw_urls") or [] if x]
        if not matches or not raws:
            continue
        rel = str(e.get("relation") or "official_artifact")
        out.append({**e, "match": matches, "raw_urls": raws,
                    "relation": rel if rel in MIRROR_RELATIONS else "official_artifact"})
    _MIRROR_CACHE[key] = (mtime, out)
    return out


def mirror_entries(url: str, root: Path | str | None = None) -> list[dict]:
    """url 에 맞는 미러 항목. 구체적인(긴) match 가 먼저다. github.com blob URL 은 변환한 raw 경로를 relation original 로 맨 앞에 둔다.
    relation original 은 match 가 url 과 정확히 같을 때(끝 슬래시·.html 차이 무시)만 유지한다. 접두어로만 맞으면(같은 사이트의 다른 페이지)
    related 로 낮추고 declared_relation 에 원래 값을 남긴다. 각 항목: {name, match(맞은 값), raw_urls, repo, ref, relation, note}."""
    out: list[dict] = []
    derived = github_blob_to_raw(url)
    if derived:
        out.append({"name": "GitHub blob → raw", "match": url, "raw_urls": [derived], "repo": "/".join(derived.split("/")[3:5]),
                    "ref": derived.split("/")[5] if len(derived.split("/")) > 5 else "", "relation": "original",
                    "note": "github.com 파일 URL 을 같은 파일의 raw 경로로 바꾼 것", "_len": 10 ** 6})
    nu = normalize_url(url)
    for e in load_mirrors(root):
        best = max((len(normalize_url(m)) for m in e["match"] if url_matches(url, m)), default=0)
        if best:
            hit = next(m for m in e["match"] if url_matches(url, m) and len(normalize_url(m)) == best)
            row = {**{k: v for k, v in e.items() if k != "match"}, "match": hit, "_len": best}
            nm = normalize_url(hit)
            if row.get("relation") == "original" and nu not in (nm, nm + ".html", nm + ".htm"):
                # 접두어로만 맞은 original 항목(같은 사이트의 다른 페이지)은 그 URL 의 원문이 아니다
                row["declared_relation"], row["relation"] = "original", "related"
            out.append(row)
    out.sort(key=lambda x: -x["_len"])
    for x in out:
        x.pop("_len", None)
    return out


def mirror_for(url: str, root: Path | str | None = None) -> list[str]:
    """url(정본 페이지)의 원문 미러 raw URL 목록(구체적인 항목의 대표 원문이 먼저, 중복 제거). 없으면 []."""
    seen: list[str] = []
    for e in mirror_entries(url, root):
        for r in e["raw_urls"]:
            if r not in seen:
                seen.append(r)
    return seen


def original_mirror_for(url: str, root: Path | str | None = None) -> list[str]:
    """relation original(같은 문서의 원본) 미러만."""
    seen: list[str] = []
    for e in mirror_entries(url, root):
        if e.get("relation") == "original":
            for r in e["raw_urls"][:1]:
                if r not in seen:
                    seen.append(r)
    return seen


def mirror_relation(url: str, raw_url: str, root: Path | str | None = None) -> str | None:
    """raw_url 이 url 의 미러 목록에 있으면 그 relation, 없으면 None."""
    for e in mirror_entries(url, root):
        if raw_url in e["raw_urls"]:
            return e.get("relation")
    return None


# --- 원문 텍스트 색인 ------------------------------------------------------------------------------

def _read_index(root: Path | str | None = None) -> dict:
    f = Layout(root).texts_index
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"version": 1, "updated": None, "items": {}}
    if not isinstance(d, dict):
        return {"version": 1, "updated": None, "items": {}}
    d.setdefault("items", {})
    return d


def _write_index(d: dict, root: Path | str | None = None) -> None:
    f = Layout(root).texts_index
    f.parent.mkdir(parents=True, exist_ok=True)
    d["items"] = dict(sorted(d.get("items", {}).items()))
    f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_source_texts(root: Path | str | None = None) -> dict[str, dict]:
    """data/source_texts/index.json → {key: {path, title, url, fetched_via, chars, sha256, ingested, ref_id, org, published, source, method}}.
    key 는 ref_id(참고문헌과 연결된 텍스트) 또는 src-<slug>. 텍스트 파일이 없는 항목은 뺀다."""
    lay = Layout(root)
    out: dict[str, dict] = {}
    for k, v in _read_index(root).get("items", {}).items():
        if not isinstance(v, dict):
            continue
        p = lay.root / str(v.get("path") or "")
        if v.get("path") and p.is_file():
            out[k] = dict(v)
    return out


def _text_of(meta: dict, root: Path | str | None = None) -> str:
    try:
        return (Layout(root).root / meta["path"]).read_text(encoding="utf-8")
    except (OSError, KeyError):
        return ""


def _text_for_source(src: dict, texts: dict[str, dict]) -> dict | None:
    """출처(id, url)에 해당하는 원문 텍스트 색인 항목. id 가 먼저, 없으면 URL 정규형 일치."""
    sid = str(src.get("id") or src.get("ref_id") or "")
    if sid and sid in texts:
        return texts[sid]
    nu = normalize_url(src.get("url") or "")
    if nu:
        for meta in texts.values():
            if normalize_url(meta.get("url") or "") == nu:
                return meta
    return None


def _cut(text: str, max_chars: int) -> str:
    if max_chars <= 0:
        return ""
    if len(text) <= max_chars:
        return text
    cut = text.rfind("\n\n", 0, max_chars)
    if cut < max_chars * 0.6:
        cut = text.rfind("\n", 0, max_chars)
    if cut < max_chars * 0.6:
        cut = max_chars
    return text[:cut].rstrip() + f"\n…(발췌: 전체 {len(text):,}자 중 앞 {cut:,}자)"


def source_text_excerpt(ref_id: str, max_chars: int, root: Path | str | None = None) -> str | None:
    """ref_id(또는 src-<slug>)의 원문 텍스트 앞부분(max_chars 이내, 문단 경계에서 자름). 텍스트가 없으면 None."""
    meta = load_source_texts(root).get(ref_id)
    if not meta:
        return None
    text = _text_of(meta, root)
    return _cut(text, max_chars) if text else None


def _keyword_windows(text: str, keywords: list[str], max_chars: int, radius: int = 400) -> str:
    low = text.lower()
    spans: list[tuple[int, int]] = []
    for k in keywords:
        start = 0
        while True:
            i = low.find(k, start)
            if i < 0:
                break
            spans.append((max(0, i - radius), min(len(text), i + len(k) + radius)))
            start = i + len(k)
            if len(spans) > 200:
                break
    if not spans:
        return _cut(text, max_chars)
    spans.sort()
    merged: list[list[int]] = []
    for a, b in spans:
        if merged and a <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    parts, used = [], 0
    for a, b in merged:
        chunk = text[a:b].strip()
        if used + len(chunk) > max_chars:
            chunk = chunk[: max(0, max_chars - used)]
        if not chunk:
            break
        parts.append(chunk)
        used += len(chunk) + 3
        if used >= max_chars:
            break
    return (" … ".join(parts) + f"\n…(키워드 주변 발췌: 전체 {len(text):,}자)").strip()


def select_texts_for_prompt(ref_ids: list[str], keywords: list[str], max_total_chars: int,
                            root: Path | str | None = None, min_share: int = 1500) -> list[tuple[str, str]]:
    """리서치·검증 에이전트 입력에 넣을 원문 텍스트 발췌. 인용 중인 출처(ref_ids 순서) 먼저, 그다음 키워드가 많이 나오는 텍스트.
    전체 글자 수는 max_total_chars 이내다. 항목마다 남은 예산을 남은 항목 수로 나눈 몫(최소 min_share)을 준다.
    인용 출처는 앞부분, 키워드 일치 텍스트는 키워드 주변 발췌다. 반환: [(key, 발췌 텍스트)]."""
    texts = load_source_texts(root)
    if not texts or max_total_chars <= 0:
        return []
    order: list[tuple[str, str]] = []
    for rid in ref_ids or []:
        if rid in texts and all(rid != k for k, _ in order):
            order.append((rid, "cited"))
    kws = [k.strip().lower() for k in keywords or [] if k and k.strip()]
    if kws:
        scored = []
        for key, meta in texts.items():
            if any(key == k for k, _ in order):
                continue
            body = _text_of(meta, root).lower()
            title = str(meta.get("title") or "").lower()
            score = sum(body.count(k) for k in kws) + 5 * sum(1 for k in kws if k in title)
            if score:
                scored.append((score, key))
        scored.sort(key=lambda x: (-x[0], x[1]))
        order += [(k, "keyword") for _, k in scored]
    out: list[tuple[str, str]] = []
    remaining = max_total_chars
    for i, (key, why) in enumerate(order):
        if remaining < 200:
            break
        share = max(remaining // (len(order) - i), min(remaining, min_share))
        text = _text_of(texts[key], root)
        chunk = _cut(text, share) if why == "cited" else _keyword_windows(text, kws, share)
        if len(chunk) > share + 120:
            chunk = chunk[:share]
        if chunk.strip():
            out.append((key, chunk))
            remaining -= len(chunk)
    return out


def format_texts_for_prompt(pairs: list[tuple[str, str]], root: Path | str | None = None) -> str:
    """select_texts_for_prompt 결과를 프롬프트 입력 절로: 항목마다 `### data/source_texts/<key>.txt (원문 텍스트: …)` + 코드 펜스."""
    texts = load_source_texts(root)
    blocks = []
    for key, text in pairs:
        meta = texts.get(key, {})
        via = VIA_LABELS.get(str(meta.get("fetched_via")), str(meta.get("fetched_via") or "미상"))
        head = (f"### {meta.get('path') or key} (원문 텍스트: {key} — {meta.get('title') or '제목 미상'}, {meta.get('url') or 'URL 없음'}, "
                f"{via}, 수집 {meta.get('ingested') or '미상'}, 전체 {int(meta.get('chars') or 0):,}자)")
        fence = "```"
        while fence in text:
            fence += "`"
        blocks.append(f"{head}\n\n{fence}text\n{text}\n{fence}")
    return "\n\n".join(blocks)


# --- 원문 열람 상한 --------------------------------------------------------------------------------

def _lower_to_cap(value: str | None) -> bool:
    return RELIABILITY_ORDER.get(str(value), -1) > RELIABILITY_ORDER[CAP]


def _agent_fetch(src: dict, web_fetch_available: bool | None, root) -> tuple[bool, str | None, str | None]:
    """에이전트가 표시한 열람을 받아들일지. (열람 인정, 경로, 인정하지 않은 사유)."""
    via = src.get("fetched_via")
    fetched_flag = src.get("fetched")
    claimed = fetched_flag is True or (fetched_flag is None and via in ("webfetch", "github_raw"))
    if not claimed:
        return False, None, None
    if src.get("source_unopened") is True:
        return False, None, "fetched 표시와 source_unopened: true 가 충돌한다(미열람으로 본다)"
    furl = str(src.get("fetch_url") or "")
    if via not in FETCHED_VIA:
        via = "github_raw" if (is_raw_github(furl) or is_raw_github(src.get("url") or "")) else "webfetch"
    if via == "webfetch":
        if web_fetch_available is False:
            return False, None, "페이지 열람 도구를 쓸 수 없는 실행(web_fetch_available: false)의 WebFetch 열람 표시"
        return True, "webfetch", None
    if via == "github_raw":
        url = str(src.get("url") or "")
        if furl:
            if not is_raw_github(furl) and not github_blob_to_raw(furl):
                return False, None, f"fetch_url 이 GitHub raw 경로가 아니다({furl})"
            rel = mirror_relation(url, furl, root)
            if rel in ("official_artifact", "related"):
                return False, None, (f"연 파일({furl})은 {RELATION_LABELS[rel]}이다 — 정본 문서의 원문 열람으로 치지 않는다. "
                                     "연 파일을 github.com/…/blob/… URL 의 별도 출처로 인용하면 원문 열람으로 인정된다")
            return True, "github_raw", None
        if is_raw_github(url) or github_blob_to_raw(url) or original_mirror_for(url, root):
            return True, "github_raw", None
        return False, None, "GitHub raw 열람 표시가 있으나 fetch_url 이 없고 원문 미러(relation original)도 없다"
    return False, None, "inbox 열람 표시가 있으나 data/source_texts 에 원문 텍스트가 없다"


def apply_fetch_caps(research: dict, *, root: Path | str | None = None, source_texts: dict | None = None,
                     web_fetch_available: bool | None = None) -> list[str]:
    """원문 열람 규칙을 코드로 강제한다(research 를 제자리에서 고친다). 바뀐 내용마다 한국어 로그 한 줄을 돌려준다.

    1. sources[] 마다 fetched(bool)·fetched_via·source_unopened 를 정한다. fetched 는 에이전트가 WebFetch·GitHub raw 원문으로 열었다고
       표시했고 그 표시가 받아들여지거나(_agent_fetch), data/source_texts 에 그 출처의 원문 텍스트가 있을 때만 true 다.
    2. fetched false 인 출처의 reliability 는 medium 이 상한이다.
    3. findings[] 의 source_ids 가 모두 미열람이면 confidence 는 medium 이 상한이다.
    4. confidence high 인 finding 은 서로 다른 출처 2개 이상, 그중 열람한 출처 1개 이상을 인용해야 한다. 아니면 medium 으로 내린다.
    """
    logs: list[str] = []
    texts = load_source_texts(root) if source_texts is None else source_texts
    sources = [s for s in research.get("sources") or [] if isinstance(s, dict)]
    by_id: dict[str, dict] = {}
    for s in sources:
        sid = str(s.get("id") or "?")
        ok, via, why = _agent_fetch(s, web_fetch_available, root)
        text_meta = _text_for_source(s, texts)
        by_text = False
        if not ok and text_meta:
            ok, via, by_text = True, str(text_meta.get("fetched_via") or "inbox"), True
        before = s.get("fetched")
        s["fetched"] = bool(ok)
        s["fetched_via"] = via if ok else None
        s["source_unopened"] = not ok
        if by_text:
            extra = f"(에이전트 표시는 인정하지 않음 — {why})" if why else ""
            logs.append(f"출처 {sid}: data/source_texts 의 원문 텍스트({text_meta.get('path')})가 있어 fetched true({via}){extra}")
        elif why:
            logs.append(f"출처 {sid}: 원문 열람 표시를 인정하지 않음 — {why}. fetched false 로 둔다")
        elif before is None and not ok:
            logs.append(f"출처 {sid}: 원문 열람 표시 없음 → fetched false(원문 미열람)")
        if not ok and _lower_to_cap(s.get("reliability")):
            logs.append(f"출처 {sid}: 원문 미열람이라 신뢰도 {s.get('reliability')} → {CAP}")
            s["reliability"] = CAP
        by_id[sid] = s

    def fetched_id(i: str) -> bool:
        if i in by_id:
            return bool(by_id[i].get("fetched"))
        return i in texts

    for f in research.get("findings") or []:
        if not isinstance(f, dict):
            continue
        fid = str(f.get("id") or "?")
        ids = list(dict.fromkeys(str(x) for x in f.get("source_ids") or []))
        opened = [i for i in ids if fetched_id(i)]
        if ids:
            want_unopened = not opened
            if f.get("source_unopened") is not want_unopened and (want_unopened or "source_unopened" in f):
                f["source_unopened"] = want_unopened
        if f.get("confidence") == "high":
            reason = None
            if ids and not opened:
                reason = f"근거 출처({', '.join(ids)})가 모두 원문 미열람"
            elif len(ids) < 2:
                reason = f"서로 다른 근거 출처가 {len(ids)}개뿐(high 는 2개 이상, 그중 원문 열람 1개 이상)"
            elif not opened:
                reason = "원문을 연 근거 출처가 없음"
            if reason:
                f["confidence"] = CAP
                logs.append(f"발견 사항 {fid}: {reason} → 신뢰도 high → {CAP}")
    return logs


def fetch_label(meta: dict) -> str:
    """출처(research sources 항목) 또는 참고문헌 프런트매터 → "원문 열람(<경로>)" 또는 "원문 미열람"."""
    if meta and meta.get("fetched") is True:
        via = str(meta.get("fetched_via") or "")
        return f"원문 열람({VIA_LABELS.get(via, via or '경로 미상')})"
    return "원문 미열람"


# --- URL 확인 결과(data/url_check.json) ------------------------------------------------------------

_LEGACY_STATUS = {"열림": "열림", "오류": "오류", "미확인": "오류"}


def load_url_check(root: Path | str | None = None, path: Path | str | None = None) -> dict:
    """data/url_check.json → {"checked_at": str|None, "items": {ref_id: {url,status,http,detail,mirror,mirror_status,...}}}.
    구 형식(items 가 목록이고 result 필드)도 받아 새 형식으로 바꾼다. 없으면 빈 items."""
    f = Path(path) if path else Layout(root).url_check_file
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"checked_at": None, "items": {}}
    items = d.get("items") or {}
    if isinstance(items, list):
        conv = {}
        for it in items:
            if not isinstance(it, dict) or not it.get("ref_id"):
                continue
            http = it.get("status") if isinstance(it.get("status"), int) else None
            st = _LEGACY_STATUS.get(str(it.get("result")), "오류")
            if http in (404, 410):
                st = "없음"
            conv[str(it["ref_id"])] = {"url": it.get("url"), "status": st, "http": http, "detail": it.get("detail", ""),
                                       "mirror": None, "mirror_status": None}
        items = conv
    return {"checked_at": d.get("checked_at"), "items": items, "counts": d.get("counts"), "mirror_counts": d.get("mirror_counts")}


def url_check_counts(uc: dict) -> dict[str, int]:
    """상태별 건수 {열림, 없음, 정책 차단, 오류, 미러 열림}."""
    items = (uc or {}).get("items") or {}
    vals = list(items.values()) if isinstance(items, dict) else list(items)
    c = {k: sum(1 for it in vals if isinstance(it, dict) and it.get("status") == k) for k in URL_STATUSES}
    c["미러 열림"] = sum(1 for it in vals if isinstance(it, dict) and it.get("mirror_status") == "열림")
    return c


def url_check_summary_line(uc: dict) -> str:
    """일일 로그·요약용 한 줄: "참고문헌 URL 43건: 열림 n · 없음 n · 정책 차단 n · 오류 n (미러 열림 n, 확인 YYYY-MM-DD)"."""
    items = (uc or {}).get("items") or {}
    c = url_check_counts(uc)
    when = str((uc or {}).get("checked_at") or "")[:10] or "미상"
    return (f"참고문헌 URL {len(items)}건: 열림 {c['열림']} · 없음 {c['없음']} · 정책 차단 {c['정책 차단']} · 오류 {c['오류']} "
            f"(미러 열림 {c['미러 열림']}, 확인 {when})")


# --- 참고문헌 페이지 표시 --------------------------------------------------------------------------

def _md_cell(s) -> str:
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ")


def render_reference_fetch_status(ref_meta: dict, *, root: Path | str | None = None, url_check: dict | None = None,
                                  texts: dict | None = None) -> str:
    """참고문헌 페이지(비고 절)에 넣는 원문 열람 상태 블록. 마커(FETCH_BLOCK_START/END) 포함.
    원문 열람 여부·열람 경로·원문 텍스트, URL 확인 결과·날짜와 미러 확인 결과(data/url_check.json)를 표로 보여 준다."""
    ref_id = str(ref_meta.get("ref_id") or "")
    uc = load_url_check(root) if url_check is None else url_check
    texts = load_source_texts(root) if texts is None else texts
    item = (uc.get("items") or {}).get(ref_id) or {}
    when = str(item.get("checked_at") or uc.get("checked_at") or "")[:10]
    tmeta = texts.get(ref_id) if ref_id else None
    rows = [("원문 열람", fetch_label(ref_meta))]
    if ref_meta.get("fetched") is True:
        path_url = (tmeta or {}).get("source") if (tmeta or {}).get("fetched_via") == "github_raw" else None
        path_url = path_url or ref_meta.get("fetch_url") or (item.get("mirror") if ref_meta.get("fetched_via") == "github_raw" else None)
        via_label = VIA_LABELS.get(str(ref_meta.get("fetched_via")), "경로 미상")
        rows.append(("열람 경로", f"{via_label} <{path_url}>" if path_url and str(path_url).startswith("http") else via_label))
    else:
        rows.append(("열람 경로", "없음"))
    if tmeta:
        rows.append(("원문 텍스트", f"`{tmeta.get('path')}` ({int(tmeta.get('chars') or 0):,}자, 수집 {tmeta.get('ingested') or '미상'})"))
    else:
        rows.append(("원문 텍스트", "없음"))
    if item:
        http = f"HTTP {item.get('http')}" if item.get("http") else "HTTP 응답 없음"
        detail = _md_cell(item.get("detail") or "")
        rows.append(("URL 확인", f"{item.get('status') or '미확인'} ({when}, {http}{', ' + detail if detail else ''})"))
        if item.get("mirror"):
            rel = RELATION_LABELS.get(str(item.get("mirror_relation") or ""), "")
            ms = item.get("mirror_status") or "확인 안 함"
            rows.append(("GitHub 미러 확인", f"{ms} ({when}{', ' + rel if rel else ''}) <{item.get('mirror')}>"))
        else:
            rows.append(("GitHub 미러 확인", "등록된 미러 없음(config/source_mirrors.yaml)"))
    else:
        rows.append(("URL 확인", "미확인(data/url_check.json 에 결과 없음)"))
    table = "\n".join(["| 항목 | 값 |", "|---|---|"] + [f"| {k} | {v} |" for k, v in rows])
    note = ("원문 열람 상태는 스크립트가 기록한다(pipeline/lib/sources.py). URL 확인은 `python3 pipeline/checks/check_urls.py`, "
            "반영은 `python3 pipeline/scaffold.py --apply-url-check`, 사람이 넣은 원문은 `python3 pipeline/ingest_sources.py` 로 갱신한다.")
    return f"{FETCH_BLOCK_START}\n원문 열람 상태:\n\n{table}\n\n{note}\n{FETCH_BLOCK_END}"


def _set_table_row(body: str, key: str, value: str, after: str | None = None) -> str:
    pat = re.compile(rf"^\| {re.escape(key)} \| .* \|$", re.M)
    line = f"| {key} | {value} |"
    if pat.search(body):
        return pat.sub(lambda _m: line, body, count=1)
    if after:
        pat_after = re.compile(rf"^\| {re.escape(after)} \| .* \|$", re.M)
        m = pat_after.search(body)
        if m:
            return body[: m.end()] + "\n" + line + body[m.end():]
    return body


def _get_table_row(body: str, key: str) -> str | None:
    m = re.search(rf"^\| {re.escape(key)} \| (.*) \|$", body, re.M)
    return m.group(1) if m else None


def _set_fetch_block(body: str, block: str) -> str:
    if _FETCH_BLOCK_RE.search(body):
        return _FETCH_BLOCK_RE.sub(lambda _m: block, body, count=1)
    m = re.search(r"^## 비고\s*$", body, re.M)
    if not m:
        return body.rstrip("\n") + f"\n\n## 비고\n\n{block}\n"
    nxt = re.search(r"^## ", body[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(body)
    section = body[m.end():end].rstrip("\n")
    return body[: m.end()] + section + f"\n\n{block}\n" + ("\n" + body[end:] if nxt else "")


_FOOT_LINE = re.compile(r"^(\[\^(ref-\d{3,})\]: .*?, 접근일 )(\d{4}-\d{2}-\d{2})( \(원문 미열람\))?[ \t]*$", re.M)


def _set_footnote_line(body: str, fetched: bool, accessed: str | None) -> str:
    def rep(m: re.Match) -> str:
        date = accessed if (fetched and accessed) else m.group(3)
        return f"{m.group(1)}{date}" + ("" if fetched else " (원문 미열람)")
    return _FOOT_LINE.sub(rep, body)


_UNOPENED_NOTE = re.compile(r"^(원문 미열람\(|원문 열람: 미확인)")


def _mark_unopened_notes_as_history(body: str, via: str | None, date: str) -> str:
    """원문을 열람하게 된 페이지에서, 상태 블록 밖의 '원문 미열람' 비고 문단을 지우지 않고 "등록 당시 기록"으로 바꾼다(사실 보존)."""
    label = VIA_LABELS.get(str(via), "경로 미상")
    out, in_block = [], False
    for line in body.split("\n"):
        if line.strip() == FETCH_BLOCK_START:
            in_block = True
        elif line.strip() == FETCH_BLOCK_END:
            in_block = False
        elif not in_block and _UNOPENED_NOTE.match(line):
            line = f"등록 당시 기록: {line} → {date} 에 {label} 경로로 원문을 열람했다(아래 원문 열람 상태 표)."
        out.append(line)
    return "\n".join(out)


def _insert_after(meta: dict, anchor_keys: list[str], new: dict) -> dict:
    """프런트매터에 new 키를 anchor 뒤에 넣는다(이미 있으면 그 자리에서 값만 바꾼다). 값이 None 인 키도 남긴다."""
    out: dict = {}
    anchor = next((k for k in anchor_keys if k in meta), None)
    pending = {k: v for k, v in new.items() if k not in meta}
    for k, v in meta.items():
        out[k] = new.get(k, v) if k in new else v
        if k == anchor:
            out.update(pending)
            pending = {}
    out.update(pending)
    return out


def reference_pages(root: Path | str | None = None) -> dict[str, Path]:
    """{ref_id: 경로} (docs/references/ref-*.md)."""
    out = {}
    for p in sorted(Layout(root).references_dir.glob("ref-*.md")):
        out[p.stem] = p
    return out


def find_reference_by_url(url: str, root: Path | str | None = None) -> str | None:
    """URL 정규형이 같은 참고문헌 id. 없으면 None."""
    nu = normalize_url(url)
    if not nu:
        return None
    for rid, p in reference_pages(root).items():
        try:
            meta, _ = fm.read(p)
        except Exception:  # noqa: BLE001
            continue
        if normalize_url(str(meta.get("url") or "")) == nu:
            return str(meta.get("ref_id") or rid)
    return None


def sync_reference_page(page: Path | str, *, root: Path | str | None = None, today: str | None = None,
                        url_check: dict | None = None, texts: dict | None = None, bump: bool = True,
                        write: bool = True) -> list[str]:
    """참고문헌 페이지 한 개의 원문 열람 표시를 원천(data/source_texts, data/url_check.json, 기존 fetched 표시)에 맞춘다.

    프런트매터: fetched, fetched_via, source_text, url_status, url_checked, url_verified(URL 열림이면 true), reliability(원문 열람이면
    유형 기준값, 미열람이면 medium 상한). 본문: 서지 정보 표의 원문 열람·신뢰도·접근일 행, 각주 형식 줄의 접근일과 " (원문 미열람)",
    비고 절의 원문 열람 상태 블록. 바뀐 것이 있으면 updated 를 오늘로, bump 이면 version 을 올린다. 바뀐 내용 목록을 돌려준다."""
    p = Path(page)
    today = _today(today)
    uc = load_url_check(root) if url_check is None else url_check
    texts = load_source_texts(root) if texts is None else texts
    meta, body = fm.read(p)
    ref_id = str(meta.get("ref_id") or p.stem)
    changes: list[str] = []
    tmeta = texts.get(ref_id)
    item = (uc.get("items") or {}).get(ref_id) or {}

    was_fetched = meta.get("fetched") is True
    if "fetched" not in meta and meta.get("url_verified") is True and (_get_table_row(body, "원문 열람") or "").startswith("확인"):
        # 구 형식: fetched 필드가 생기기 전 퍼블리셔는 에이전트가 원문을 연 출처를 url_verified: true·"원문 열람 | 확인"으로 적었다
        was_fetched = True
        meta = {**meta, "fetched_via": meta.get("fetched_via") or "webfetch"}
    fetched = was_fetched or bool(tmeta)
    via = meta.get("fetched_via") if was_fetched and meta.get("fetched_via") in FETCHED_VIA else None
    if fetched and not via:
        via = str((tmeta or {}).get("fetched_via") or "inbox")
    new: dict = {"fetched": fetched, "fetched_via": via if fetched else None}
    if tmeta:
        new["source_text"] = tmeta.get("path")
    if item:
        new["url_status"] = item.get("status")
        new["url_checked"] = str(item.get("checked_at") or uc.get("checked_at") or "")[:10] or None
        if item.get("status") == "열림":
            new["url_verified"] = True
    elif "url_status" not in meta:
        new["url_status"] = None
    stype = str(meta.get("source_type") or "")
    by_type = RELIABILITY_BY_TYPE.get(stype)
    rel_before = meta.get("reliability")
    if fetched and not was_fetched and by_type and RELIABILITY_ORDER.get(str(rel_before), -1) < RELIABILITY_ORDER[by_type] \
            and (meta.get("reliability_by_type") or rel_before == CAP):
        new["reliability"] = by_type
        new["reliability_by_type"] = by_type
        changes.append(f"신뢰도 {rel_before} → {by_type}(원문 열람으로 medium 상한 해제, 유형 기준값)")
    elif not fetched and _lower_to_cap(rel_before):
        new["reliability"] = CAP
        changes.append(f"신뢰도 {rel_before} → {CAP}(원문 미열람 상한)")
    accessed = None
    if fetched and not was_fetched:
        accessed = str((tmeta or {}).get("ingested") or today)
        new["accessed"] = accessed
    new_meta = _insert_after(meta, ["url_verified", "accessed", "url"], new)
    if not fetched:
        new_meta.pop("source_text", None)
    for k in ("fetched", "fetched_via", "url_status", "source_text"):
        if meta.get(k) != new_meta.get(k) or (k == "fetched" and "fetched" not in meta):
            changes.append(f"{k}: {meta.get(k)!r} → {new_meta.get(k)!r}")

    new_body = body
    cur_row = _get_table_row(new_body, "원문 열람") or ""
    if fetched or not cur_row.startswith("미확인 — 원문 미열람"):   # 미열람 행에 붙은 기존 설명(괄호)은 그대로 둔다
        new_body = _set_table_row(new_body, "원문 열람",
                                  f"확인 — {fetch_label(new_meta)}" if fetched else "미확인 — 원문 미열람", after="신뢰도")
    if "reliability" in new and new["reliability"] != rel_before:
        cell = f"{new['reliability']} (유형 기준, 원문 열람)" if fetched else f"{CAP} (원문 미열람 상한)"
        new_body = _set_table_row(new_body, "신뢰도", cell)
    if accessed:
        new_body = _set_table_row(new_body, "접근일", f"{accessed} ({VIA_LABELS.get(str(new_meta.get('fetched_via')), '경로 미상')}로 원문 열람)")
    new_body = _set_footnote_line(new_body, fetched, accessed or (str(new_meta.get("accessed") or "") if fetched else None))
    if fetched:
        new_body = _mark_unopened_notes_as_history(new_body, new_meta.get("fetched_via"),
                                                   str((tmeta or {}).get("ingested") or new_meta.get("accessed") or today))
    new_body = _set_fetch_block(new_body, render_reference_fetch_status({**new_meta, "ref_id": ref_id}, root=root, url_check=uc, texts=texts))
    if new_meta == meta and new_body == body:
        return []
    if new_body != body:
        changes.append("본문: 원문 열람 표시 갱신")
    new_meta["updated"] = today
    if bump:
        try:
            new_meta["version"] = int(new_meta.get("version", 1)) + 1
        except (TypeError, ValueError):
            new_meta["version"] = 2
    if write:
        fm.write(p, new_meta, new_body)
    return changes


# --- 텍스트 추출 -----------------------------------------------------------------------------------

class _HTMLText(HTMLParser):
    BLOCK = {"p", "div", "br", "ul", "ol", "table", "tr", "section", "article", "header", "footer", "main", "nav", "aside",
             "blockquote", "dl", "dd", "dt", "hr", "figure", "figcaption", "caption", "thead", "tbody", "form"}
    SKIP = {"script", "style", "noscript", "template", "svg", "head"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip = 0
        self.pre = 0
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._in_title = True
            return
        if tag in self.SKIP:
            self.skip += 1
            return
        if tag == "pre":
            self.pre += 1
            self.parts.append("\n\n")
        elif re.fullmatch(r"h[1-6]", tag):
            self.parts.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag in ("td", "th"):
            self.parts.append(" | ")
        elif tag in self.BLOCK:
            self.parts.append("\n\n" if tag in ("p", "div", "section", "article", "table", "blockquote") else "\n")

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
            return
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if tag == "pre":
            self.pre = max(0, self.pre - 1)
            self.parts.append("\n\n")
        elif re.fullmatch(r"h[1-6]", tag) or tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if self._in_title:
            self.title += data
            return
        if self.skip:
            return
        self.parts.append(data if self.pre else re.sub(r"\s+", " ", data))


def html_to_text(html: str) -> tuple[str, str]:
    """HTML → (본문 텍스트, <title>). html.parser 만 쓴다(script·style·head 제외, 제목은 # 표시, 목록은 - 표시)."""
    p = _HTMLText()
    p.feed(html)
    p.close()
    return normalize_text("".join(p.parts)), re.sub(r"\s+", " ", p.title).strip()


def normalize_text(text: str) -> str:
    t = text.replace("\r\n", "\n").replace("\r", "\n").replace("\f", "\n\n").replace("\u00a0", " ")
    t = "\n".join(line.rstrip() for line in t.split("\n"))
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip() + "\n" if t.strip() else ""


class ExtractError(Exception):
    pass


_PYPDF_SNIPPET = r"""
import sys
# 시스템 cryptography 가 import 중 패닉하는 환경이 있어 막는다(암호화 PDF 는 풀지 못한다). ROP_PYPDF_CRYPTO=1 이면 막지 않는다.
import os
if os.environ.get("ROP_PYPDF_CRYPTO") != "1":
    sys.modules.setdefault("cryptography", None)
from pypdf import PdfReader
r = PdfReader(sys.argv[1])
out = []
for page in r.pages:
    try:
        out.append(page.extract_text() or "")
    except Exception:
        out.append("")
sys.stdout.write("\n\f\n".join(out))
"""


def pdf_to_text(path: Path | str) -> tuple[str, str]:
    """PDF → (텍스트, 방법). pdftotext(poppler-utils)가 있으면 그것, 없거나 실패하면 pypdf 를 별도 프로세스로(패닉 격리) 쓴다.
    둘 다 안 되면 ExtractError."""
    p = str(path)
    errors = []
    exe = shutil.which("pdftotext")
    if exe:
        try:
            r = subprocess.run([exe, "-enc", "UTF-8", "-q", p, "-"], capture_output=True, timeout=300)
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout.decode("utf-8", "replace"), "pdftotext"
            errors.append(f"pdftotext exit {r.returncode}")
        except (OSError, subprocess.TimeoutExpired) as e:
            errors.append(f"pdftotext 실패: {e}")
    else:
        errors.append("pdftotext 없음")
    try:
        r = subprocess.run([sys.executable, "-c", _PYPDF_SNIPPET, p], capture_output=True, timeout=600)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.decode("utf-8", "replace"), "pypdf"
        tail = r.stderr.decode("utf-8", "replace").strip().splitlines()[-1:] or [""]
        errors.append(f"pypdf exit {r.returncode}: {tail[0][:200]}")
    except (OSError, subprocess.TimeoutExpired) as e:
        errors.append(f"pypdf 실패: {e}")
    raise ExtractError("PDF 텍스트 추출 실패(" + "; ".join(errors) + "). poppler-utils(pdftotext) 또는 pypdf 를 설치한다. "
                       "스캔 이미지 PDF 는 텍스트가 없어 OCR 이 필요하다")


def _decode(data: bytes) -> str:
    for enc in ("utf-8-sig", "utf-8"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            pass
    for enc in ("cp949", "latin-1"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            pass
    return data.decode("utf-8", "replace")


def extract_text_file(path: Path | str) -> tuple[str, str, str]:
    """파일 → (정규화한 텍스트, 방법, 추정 제목). PDF·HTML·텍스트류(.txt .md .rst …)를 받는다. 모르는 확장자는 ExtractError."""
    p = Path(path)
    suf = p.suffix.lower()
    if suf in PDF_SUFFIXES:
        text, method = pdf_to_text(p)
        return normalize_text(text), method, ""
    data = p.read_bytes()
    if suf in HTML_SUFFIXES:
        text, title = html_to_text(_decode(data))
        return text, "html.parser", title
    if suf in TEXT_SUFFIXES or not suf:
        text = _decode(data)
        m = re.search(r"^#\s+(.+)$", text, re.M) if suf in (".md", ".markdown") else None
        return normalize_text(text), "text", (m.group(1).strip() if m else "")
    raise ExtractError(f"지원하지 않는 형식: {p.name} (PDF·HTML·TXT·MD 등 텍스트 파일만)")


# --- 저장 -------------------------------------------------------------------------------------------

def slug_key(title: str = "", url: str = "", text: str = "") -> str:
    """참고문헌과 연결되지 않은 텍스트의 key: src-<영문 slug> (영문이 없으면 src-<sha256 앞 10자>)."""
    base = title or ""
    if not re.search(r"[A-Za-z0-9]", base) and url:
        base = urllib.parse.urlsplit(url).path.rsplit("/", 1)[-1] or urllib.parse.urlsplit(url).hostname or ""
    s = re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")[:60].strip("-")
    if not s:
        s = hashlib.sha256((title + url + text[:2000]).encode("utf-8")).hexdigest()[:10]
    return f"src-{s}"


def store_source_text(text: str, *, key: str, ref_id: str | None = None, title: str = "", url: str = "", org: str = "",
                      published=None, fetched_via: str = "inbox", source: str = "", method: str = "",
                      root: Path | str | None = None, today: str | None = None, dry_run: bool = False) -> tuple[dict, bool]:
    """정규화한 텍스트를 data/source_texts/<key>.txt 에 쓰고 index.json 을 갱신한다. 같은 내용(sha256)이 이미 있으면 쓰지 않는다.
    반환: (색인 항목, 바뀌었는가)."""
    if not _KEY_RE.match(key):
        raise ValueError(f"잘못된 key: {key!r} (소문자·숫자·-._)")
    if fetched_via not in FETCHED_VIA:
        raise ValueError(f"fetched_via 는 {FETCHED_VIA} 중 하나: {fetched_via!r}")
    lay = Layout(root)
    text = normalize_text(text)
    if not text.strip():
        raise ExtractError("빈 텍스트")
    if str(published or "").strip() in ("", "미확인", "발행일 미확인", "None"):
        published = None
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
    target = lay.texts_dir / f"{key}.txt"
    idx = _read_index(root)
    old = idx["items"].get(key) or {}
    item = {
        "ref_id": ref_id, "path": f"data/source_texts/{key}.txt",
        "title": title or old.get("title") or "", "url": url or old.get("url") or "", "org": org or old.get("org") or "",
        "published": published if published is not None else (old.get("published") if old.get("published") not in ("미확인",) else None),
        "fetched_via": fetched_via, "source": source or old.get("source") or "", "method": method or old.get("method") or "",
        "chars": len(text), "sha256": sha, "ingested": old.get("ingested") if old.get("sha256") == sha else _today(today),
    }
    same = old.get("sha256") == sha and target.is_file() and all(old.get(k) == item.get(k) for k in item)
    if same:
        return old, False
    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        if not (old.get("sha256") == sha and target.is_file()):
            target.write_text(text, encoding="utf-8")
        idx["items"][key] = item
        idx["updated"] = _today(today)
        _write_index(idx, root)
    return item, True


def _ssl_context() -> ssl.SSLContext:
    cafile = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE")
    try:
        if cafile and Path(cafile).is_file():
            return ssl.create_default_context(cafile=cafile)
    except (ssl.SSLError, OSError):
        pass
    return ssl.create_default_context()


def fetch_url_text(url: str, timeout: float = 60.0) -> tuple[str, str, str]:
    """URL 을 받아 (정규화한 텍스트, 방법, 추정 제목). HTML 은 html.parser, PDF 는 pdf_to_text. 실패하면 예외(urllib.error.* 또는 ExtractError)."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout, context=_ssl_context()) as r:
        data = r.read()
        ctype = (r.headers.get("Content-Type") or "").lower()
    path = urllib.parse.urlsplit(url).path.lower()
    if "pdf" in ctype or path.endswith(".pdf") or data[:5] == b"%PDF-":
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tf:
            tf.write(data)
            tmp = tf.name
        try:
            text, method = pdf_to_text(tmp)
        finally:
            os.unlink(tmp)
        return normalize_text(text), method, ""
    body = _decode(data)
    if "html" in ctype and not path.endswith((".md", ".rst", ".txt", ".ttl")) or path.endswith(tuple(HTML_SUFFIXES)):
        text, title = html_to_text(body)
        return text, "html.parser", title
    m = re.search(r"^#\s+(.+)$", body, re.M) if path.endswith(".md") else None
    return normalize_text(body), "text", (m.group(1).strip() if m else "")


def ingest_url(url: str, *, ref_id: str | None, fetched_via: str = "github_raw", title: str = "", canonical_url: str = "",
               org: str = "", published=None, root: Path | str | None = None, today: str | None = None,
               dry_run: bool = False) -> tuple[dict, bool]:
    """URL(보통 raw.githubusercontent.com 원문 미러)의 텍스트를 받아 저장한다. canonical_url 은 색인의 url(정본 주소)."""
    text, method, auto_title = fetch_url_text(url)
    key = ref_id or slug_key(title or auto_title, canonical_url or url, text)
    return store_source_text(text, key=key, ref_id=ref_id, title=title or auto_title, url=canonical_url or url, org=org,
                             published=published, fetched_via=fetched_via, source=url, method=method, root=root, today=today,
                             dry_run=dry_run)


def ingest_mirror_texts(ref_ids: list[str] | None = None, *, root: Path | str | None = None, today: str | None = None,
                        url_check: dict | None = None, only_open: bool = False, dry_run: bool = False) -> list[str]:
    """참고문헌마다 원문 미러(relation original)의 텍스트를 받아 data/source_texts 에 저장한다(fetched_via github_raw).
    only_open 이면 url_check 에서 미러가 열림으로 확인된 참고문헌만. 받지 못하면 로그만 남긴다. 반환: 한국어 로그 줄."""
    logs: list[str] = []
    uc = load_url_check(root) if url_check is None else url_check
    for rid, p in reference_pages(root).items():
        if ref_ids and rid not in ref_ids:
            continue
        try:
            meta, _ = fm.read(p)
        except Exception as e:  # noqa: BLE001
            logs.append(f"{rid}: 프런트매터를 읽지 못함({e})")
            continue
        url = str(meta.get("url") or "")
        item = (uc.get("items") or {}).get(rid) or {}
        if only_open and not (item.get("mirror_status") == "열림" and item.get("mirror_relation") == "original"):
            continue
        cands = original_mirror_for(url, root)
        if not cands:
            if ref_ids:
                logs.append(f"{rid}: 원문 미러(relation original)가 없다 — 건너뜀")
            continue
        done = False
        for raw in cands:
            try:
                got, changed = ingest_url(raw, ref_id=rid, fetched_via="github_raw", title=str(meta.get("ref_title") or ""),
                                          canonical_url=url, org=str(meta.get("org") or ""), published=meta.get("published"),
                                          root=root, today=today, dry_run=dry_run)
            except (urllib.error.URLError, OSError, ExtractError, ValueError) as e:
                logs.append(f"{rid}: 미러 {raw} 를 받지 못함({getattr(e, 'reason', e)})")
                continue
            logs.append(f"{rid}: 원문 미러 {'저장' if changed else '변경 없음'} {raw} → {got['path']} ({got['chars']:,}자)")
            done = True
            break
        if not done:
            logs.append(f"{rid}: 원문 미러를 하나도 받지 못함 — 원문 미열람 상태 유지")
    return logs


def append_changelog(entries: list[dict], root: Path | str | None = None) -> None:
    """data/changelog.json items 에 항목을 더한다(scaffold.py apply_url_check 와 같은 형식)."""
    if not entries:
        return
    f = Layout(root).changelog_file
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        d = {"items": []}
    d.setdefault("items", []).extend(entries)
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def now_iso() -> str:
    """현재 시각(ISO, Asia/Seoul — 위키의 날짜 기준 시간대). 시간대 자료가 없으면 시스템 시간대."""
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(ZoneInfo("Asia/Seoul")).isoformat(timespec="seconds")
    except Exception:  # noqa: BLE001
        return datetime.now().astimezone().isoformat(timespec="seconds")
