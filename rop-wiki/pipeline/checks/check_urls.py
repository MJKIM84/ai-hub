#!/usr/bin/env python3
"""참고문헌 URL 열림 확인 (사양서 9장 완료 기준 3, 주간 정리의 링크·출처 유효성 점검).

docs/references/ref-*.md 프런트매터의 url 을 모두 확인하고 네 가지로 나눈다.
- 열림      : 2xx·3xx
- 없음      : 404·410
- 정책 차단 : 이그레스 프록시가 막음(CONNECT 403/407 "Tunnel connection failed", 평문 HTTP 403 + x-deny-reason,
              "Host not in allowlist", GitHub "not enabled for this session")
- 오류      : 시간 초과·DNS·TLS·그 밖의 HTTP 상태(사이트 자체의 403·5xx 포함)
정본 URL 이 열리지 않으면(정책 차단·오류·없음) config/source_mirrors.yaml 의 GitHub raw 미러(또는 github.com blob 의 raw 경로)를
확인해 mirror·mirror_status·mirror_relation 을 남긴다. 차단 여부는 코드에 적지 않고 매번 실제로 요청해 판정한다(네트워크 정책은 바뀔 수 있다).

결과: data/url_check.json (기본. --json 으로 다른 경로, --no-write 로 저장 안 함)
  {"checked_at", "counts": {열림, 없음, 정책 차단, 오류, 미러 열림}, "items": {ref_id: {url, status, http, detail, mirror, mirror_status, mirror_relation}}}
표준 출력: 한국어 요약 표와 마지막 줄 "[check_urls] N건: 열림 n · 없음 n · 정책 차단 n · 오류 n · 미러 열림 n (확인 시각 …)".
exit 0. --strict 이면 열림이 아닌 항목이 하나라도 있을 때 exit 1.
반영: `python3 pipeline/scaffold.py --apply-url-check` 가 결과를 참고문헌 페이지(url_status, 원문 미러 텍스트 → fetched)에 적는다.
사용: python3 pipeline/checks/check_urls.py [--strict] [--timeout 15] [--json PATH | --no-write] [--no-mirror] [--refs ref-001,ref-004]
"""
from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import frontmatter as fm  # noqa: E402
from lib import paths  # noqa: E402
from lib import sources  # noqa: E402

UA = "rop-wiki-check-urls/2.0 (+pipeline/checks/check_urls.py)"
STATUSES = sources.URL_STATUSES   # ("열림", "없음", "정책 차단", "오류")

# 프록시·게이트웨이 거부로 보는 표지(대소문자 무시). 사이트 자체의 403 과 구분하는 데 쓴다.
_POLICY_ERROR = re.compile(r"tunnel connection failed:\s*(403|407)|proxy authentication required|"
                           r"CONNECT.*(403|407)", re.I)
_POLICY_BODY = re.compile(r"host not in allowlist|not enabled for this session|egress (settings|policy)|"
                          r"blocked by (the )?(network|egress|proxy) policy", re.I)


def classify(http_status: int | None = None, error: BaseException | str | None = None,
             headers: dict | None = None, body: bytes | str | None = None) -> tuple[str, str]:
    """응답 하나를 (상태, 설명)으로 나눈다. 상태는 열림 | 없음 | 정책 차단 | 오류.

    http_status: HTTP 상태 코드(응답을 받았을 때), error: 예외 또는 메시지(응답이 없을 때), headers·body: 403 판정용."""
    hdrs = {str(k).lower(): str(v) for k, v in (headers or {}).items()}
    text = body.decode("utf-8", "replace") if isinstance(body, (bytes, bytearray)) else str(body or "")
    if http_status is not None:
        if 200 <= http_status < 400:
            return "열림", f"HTTP {http_status}"
        if http_status in (404, 410):
            return "없음", f"HTTP {http_status}"
        if http_status in (403, 407) and ("x-deny-reason" in hdrs or _POLICY_BODY.search(text)):
            why = hdrs.get("x-deny-reason") or _POLICY_BODY.search(text).group(0)
            return "정책 차단", f"HTTP {http_status} 네트워크 정책 거부({why})"
        if http_status == 407:
            return "정책 차단", "HTTP 407 프록시 인증 필요"
        return "오류", f"HTTP {http_status}"
    msg = str(getattr(error, "reason", None) or error or "")
    if _POLICY_ERROR.search(msg):
        return "정책 차단", f"프록시 CONNECT 거부({msg})"
    if isinstance(error, (TimeoutError,)) or "timed out" in msg.lower():
        return "오류", f"시간 초과({msg})"
    return "오류", msg or "알 수 없는 오류"


def _ssl_context() -> ssl.SSLContext:
    return sources._ssl_context()


def probe(url: str, timeout: float = 15.0, ctx: ssl.SSLContext | None = None, urlopen=urllib.request.urlopen) -> dict:
    """URL 하나를 HEAD(→ 403·405·501 이면 GET)로 확인한다. {status, http, detail}. urlopen 은 테스트용 주입 지점."""
    ctx = ctx or _ssl_context()
    last = {"status": "오류", "http": None, "detail": ""}
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with urlopen(req, timeout=timeout, context=ctx) as r:
                code = getattr(r, "status", None) or r.getcode()
                st, detail = classify(http_status=code)
                return {"status": st, "http": code, "detail": f"{method} {detail}"}
        except urllib.error.HTTPError as e:
            body = b""
            try:
                body = e.read(4096) if method == "GET" else b""
            except Exception:  # noqa: BLE001
                body = b""
            st, detail = classify(http_status=e.code, headers=dict(e.headers or {}), body=body)
            last = {"status": st, "http": e.code, "detail": f"{method} {detail}"}
            if method == "HEAD" and st == "오류" and e.code in (403, 405, 501):
                continue   # HEAD 를 거부하는 사이트가 있다 → GET 으로 다시(본문으로 정책 거부 여부도 본다)
            return last
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
            st, detail = classify(error=e)
            return {"status": st, "http": None, "detail": f"{method} {detail}"}
    return last


def load_reference_urls(refs: list[str] | None = None) -> list[tuple[str, str]]:
    out = []
    for p in sorted((paths.DOCS / "references").glob("ref-*.md")):
        try:
            meta, _ = fm.read(p)
        except Exception:  # noqa: BLE001
            continue
        rid = str(meta.get("ref_id") or p.stem)
        if meta.get("url") and (not refs or rid in refs):
            out.append((rid, str(meta["url"])))
    return out


def check_one(ref_id: str, url: str, timeout: float, ctx, use_mirror: bool = True, urlopen=urllib.request.urlopen) -> dict:
    """정본 URL 을 확인하고, 열리지 않으면 미러를 확인한다(원문 미러 우선, 첫 번째로 열리는 것)."""
    r = probe(url, timeout, ctx, urlopen=urlopen)
    item = {"url": url, "status": r["status"], "http": r["http"], "detail": r["detail"],
            "mirror": None, "mirror_status": None, "mirror_relation": None}
    if not use_mirror:
        return item
    entries = sources.mirror_entries(url)
    if not entries:
        return item
    # 대표 미러: 원문(relation original) 항목의 첫 raw URL, 없으면 가장 구체적인 항목의 첫 raw URL
    ordered = [e for e in entries if e.get("relation") == "original"] + [e for e in entries if e.get("relation") != "original"]
    first = ordered[0]
    item["mirror"], item["mirror_relation"] = first["raw_urls"][0], first.get("relation")
    if r["status"] == "열림":
        return item   # 정본이 열리면 미러는 기록만 하고 확인하지 않는다
    tried = []
    for e in ordered[:3]:
        raw = e["raw_urls"][0]
        if raw in tried:
            continue
        tried.append(raw)
        m = probe(raw, timeout, ctx, urlopen=urlopen)
        item.update(mirror=raw, mirror_status=m["status"], mirror_relation=e.get("relation"))
        if m["status"] == "열림":
            break
    return item


def _row(rid: str, it: dict) -> str:
    http = str(it.get("http") or "-")
    mirror = "-"
    if it.get("mirror"):
        rel = {"original": "원문", "official_artifact": "공식 산출물", "related": "관련"}.get(it.get("mirror_relation") or "", "")
        mirror = f"{it.get('mirror_status') or '확인 안 함'}({rel})"
    return f"| {rid} | {it['status']} | {http} | {mirror} | {it['url']} |"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true", help="열림이 아닌 항목이 있으면 exit 1")
    ap.add_argument("--timeout", type=float, default=15.0)
    ap.add_argument("--json", dest="json_path", default=None, help="결과 JSON 경로(기본 data/url_check.json)")
    ap.add_argument("--no-write", action="store_true", help="결과 파일을 쓰지 않는다")
    ap.add_argument("--no-mirror", action="store_true", help="GitHub 미러를 확인하지 않는다")
    ap.add_argument("--refs", default="", help="확인할 참고문헌 id(쉼표 구분). 기본은 전부")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args(argv)

    refs = load_reference_urls([x.strip() for x in args.refs.split(",") if x.strip()] or None)
    if not refs:
        print("[check_urls] 참고문헌 페이지(docs/references/ref-*.md)가 없다")
        return 1 if args.strict else 0
    ctx = _ssl_context()
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        results = list(ex.map(lambda t: (t[0], check_one(t[0], t[1], args.timeout, ctx, not args.no_mirror)), refs))
    items = {rid: it for rid, it in results}
    checked = sources.now_iso()
    uc = {"checked_at": checked, "items": items}
    counts = sources.url_check_counts(uc)
    uc = {"checked_at": checked, "counts": counts, "items": items}

    print("| 참고문헌 | 상태 | HTTP | GitHub 미러 | URL |")
    print("|---|---|---|---|---|")
    for rid, it in items.items():
        print(_row(rid, it))
    for rid, it in items.items():
        if it["status"] != "열림":
            print(f"  - {rid}: {it['detail']}" + (f" / 미러 {it['mirror_status']}: {it['mirror']}" if it.get("mirror_status") else ""))
    print(f"[check_urls] {len(items)}건: 열림 {counts['열림']} · 없음 {counts['없음']} · 정책 차단 {counts['정책 차단']} · "
          f"오류 {counts['오류']} · 미러 열림 {counts['미러 열림']} (확인 시각 {checked})")
    if counts["정책 차단"]:
        print(f"[check_urls] 정책 차단 {counts['정책 차단']}건은 이 실행 환경의 네트워크 정책이 막은 것이다(파일 결함 아님). "
              "원문은 GitHub 미러(미러 열림)나 inbox/sources/ 로 연다.")
    if not args.no_write:
        out = Path(args.json_path) if args.json_path else paths.DATA / "url_check.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(uc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        try:
            shown = out.resolve().relative_to(paths.ROOT)
        except ValueError:
            shown = out
        print(f"[check_urls] 저장: {shown}")
    if args.strict and counts["열림"] != len(items):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
