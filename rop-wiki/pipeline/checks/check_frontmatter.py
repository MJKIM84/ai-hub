#!/usr/bin/env python3
"""프런트매터 검사 (사양서 6.4 의 2단계, 5.1·5.2).

모든 docs 페이지에 대해 프런트매터 존재, 필수 필드(title,type,status,created,updated,version),
type·status·confidence 허용 값, type 별 추가 필수 필드, 날짜 형식을 검사한다.
또한 모든 docs 페이지(홈 포함)의 본문 첫 줄이 이동 경로("홈 › …" 또는 "[홈](…) › …")인지 검사한다.
홈은 경로가 "홈" 한 단어뿐이므로 링크 없는 "홈" 한 줄이면 된다. 오류가 있으면 exit 1.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import frontmatter as fm  # noqa: E402
from lib import paths  # noqa: E402


def main() -> int:
    errors: list[str] = []
    files = sorted(paths.DOCS.rglob("*.md"))
    for p in files:
        rel = p.relative_to(paths.DOCS).as_posix()
        text = p.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{rel}: 프런트매터 없음")
            continue
        try:
            meta, body = fm.parse(text)
        except Exception as e:
            errors.append(f"{rel}: 프런트매터 파싱 실패: {e}")
            continue
        for e in fm.validate(meta, rel):
            errors.append(f"{rel}: {e}")
        first = next((l for l in body.split("\n") if l.strip()), "")
        if not (first.startswith("홈") or first.startswith("[홈](")):
            errors.append(f"{rel}: 본문 첫 줄이 이동 경로('홈 › …')가 아님: {first[:40]!r}")
    if errors:
        print(f"[check_frontmatter] 오류 {len(errors)}건 (파일 {len(files)}개 검사)")
        for e in errors:
            print("-", e)
        return 1
    print(f"[check_frontmatter] 통과: 파일 {len(files)}개")
    return 0


if __name__ == "__main__":
    sys.exit(main())
