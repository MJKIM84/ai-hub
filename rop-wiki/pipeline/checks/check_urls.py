#!/usr/bin/env python3
"""참고문헌 URL 열림 확인 (사양서 9장 완료 기준 3, 선택 실행).

docs/references/ref-*.md 프런트매터의 url 에 HEAD 요청(거부되면 GET)을 보내 상태 코드를 기록한다.
- 2xx·3xx: 열림 / 4xx·5xx: 오류(상태 코드 기록) / 연결·프록시·시간 초과 등 예외: 미확인(사유 기록)
- 네트워크 정책으로 외부 접속이 막힌 환경에서는 전부 "미확인"이 되며, 이는 파일의 결함이 아니므로
  기본 실행에서는 exit 0 이다. --strict 를 주면 열림이 아닌 항목이 하나라도 있을 때 exit 1.
- --json <path> 로 결과를 저장한다(퍼블리셔 로그·주간 정리의 링크 유효성 점검 입력용).
사용: python3 pipeline/checks/check_urls.py [--strict] [--timeout 15] [--json runs/<id>/url_check.json]
run_all.sh 는 환경변수 ROP_CHECK_URLS=1 일 때만 이 검사를 실행한다.
"""
from __future__ import annotations

import argparse
import json
import os
import ssl
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import frontmatter as fm  # noqa: E402
from lib import paths  # noqa: E402

UA = "rop-wiki-check-urls/1.0 (+pipeline/checks/check_urls.py)"


def _ssl_context() -> ssl.SSLContext:
    cafile = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE")
    try:
        return ssl.create_default_context(cafile=cafile) if cafile and Path(cafile).is_file() else ssl.create_default_context()
    except (ssl.SSLError, OSError):
        return ssl.create_default_context()


def probe(url: str, timeout: float, ctx: ssl.SSLContext) -> dict:
    """한 URL 을 HEAD → (405/403/501 이면) GET 으로 확인한다."""
    result = {"url": url, "status": None, "result": "미확인", "detail": ""}
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
                result.update(status=r.status, result="열림", detail=f"{method} {r.status}", final_url=r.geturl())
                return result
        except urllib.error.HTTPError as e:
            result.update(status=e.code, detail=f"{method} {e.code} {e.reason}")
            if method == "HEAD" and e.code in (403, 405, 501):
                continue
            result["result"] = "오류"
            return result
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
            reason = getattr(e, "reason", None) or e
            result.update(result="미확인", detail=f"{method} 실패: {reason}")
            return result
    return result


def load_reference_urls() -> list[tuple[str, str]]:
    out = []
    for p in sorted((paths.DOCS / "references").glob("ref-*.md")):
        try:
            meta, _ = fm.read(p)
        except Exception:
            continue
        if meta.get("url"):
            out.append((str(meta.get("ref_id") or p.stem), str(meta["url"])))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true", help="열림이 아닌 항목이 있으면 exit 1")
    ap.add_argument("--timeout", type=float, default=15.0)
    ap.add_argument("--json", dest="json_path", help="결과를 JSON 으로 저장할 경로")
    args = ap.parse_args(argv)

    refs = load_reference_urls()
    if not refs:
        print("[check_urls] 참고문헌 페이지(docs/references/ref-*.md)가 없다")
        return 1 if args.strict else 0
    ctx = _ssl_context()
    rows = []
    for ref_id, url in refs:
        r = probe(url, args.timeout, ctx)
        r["ref_id"] = ref_id
        rows.append(r)
        print(f"- {ref_id}: {r['result']} ({r['detail']}) {url}")
    counts = {k: sum(1 for r in rows if r["result"] == k) for k in ("열림", "오류", "미확인")}
    checked = datetime.now().astimezone().isoformat(timespec="seconds")
    print(f"[check_urls] {len(rows)}건: 열림 {counts['열림']} · 오류 {counts['오류']} · 미확인 {counts['미확인']} (확인 시각 {checked})")
    if counts["미확인"] == len(rows):
        print("[check_urls] 모든 요청이 실패했다. 네트워크 정책(프록시 차단)일 가능성이 크며, 이 경우 완료 기준 3의 'URL 열림'은 미확인으로 기록한다.")
    if args.json_path:
        out = Path(args.json_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps({"checked_at": checked, "counts": counts, "items": rows}, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")
        print(f"[check_urls] 저장: {out}")
    if args.strict and counts["열림"] != len(rows):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
