#!/usr/bin/env python3
"""docs 전체의 raw HTML 검사 (공개 배포 보안 보강 1항).

md_in_html 로 raw HTML 이 그대로 렌더링되므로, 허용 목록(<br>, 오토링크, HTML 주석) 밖의 태그·이벤트 속성·
javascript:/data: 링크 대상이 docs 에 있으면 오류로 보고 exit 1. 규칙은 pipeline/lib/htmlcheck.py 한 곳에 있고,
게시 전 에이전트 산출물은 pipeline/validate_run.py --stage pages 가 같은 규칙으로 막는다.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import htmlcheck, paths  # noqa: E402


def main() -> int:
    errors: list[str] = []
    files = sorted(paths.DOCS.rglob("*.md"))
    for p in files:
        rel = p.relative_to(paths.DOCS).as_posix()
        for e in htmlcheck.find_unsafe_html(p.read_text(encoding="utf-8")):
            errors.append(f"{rel}: {e}")
    if errors:
        print(f"[check_html] 오류 {len(errors)}건 (파일 {len(files)}개 검사)")
        for e in errors:
            print("-", e)
        return 1
    print(f"[check_html] 통과: 파일 {len(files)}개, 허용 목록 밖의 raw HTML 없음")
    return 0


if __name__ == "__main__":
    sys.exit(main())
