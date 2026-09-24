#!/usr/bin/env python3
"""내부 링크·각주 검사 (사양서 6.4 의 4단계).

- docs 안 모든 .md 의 상대 링크(.md 등 로컬 파일, 앵커·외부 URL 제외)가 실제 파일을 가리키는지
- 각주 참조 [^id] 에 정의 [^id]: 가 있는지 (없으면 오류), 정의만 있고 참조가 없으면 경고
- 절대 경로 링크(/…)는 mkdocs 가 경고하므로 오류로 본다
깨진 것 목록을 출력하고 exit 1.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import paths  # noqa: E402

LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FOOT_REF = re.compile(r"\[\^([^\]\s]+)\](?!:)")
FOOT_DEF = re.compile(r"^\[\^([^\]\s]+)\]:", re.M)
FENCE = re.compile(r"^(```|~~~).*?^\1[ \t]*$", re.M | re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")
EXTERNAL = ("http://", "https://", "mailto:", "tel:", "ftp://")


def scan(p: Path) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    rel = p.relative_to(paths.DOCS).as_posix()
    text = p.read_text(encoding="utf-8")
    scrubbed = INLINE_CODE.sub("", FENCE.sub("", text))
    for m in LINK.finditer(scrubbed):
        target = m.group(3)
        if target.startswith(EXTERNAL) or target.startswith("#") or target.startswith("<"):
            continue
        if target.startswith("/"):
            errors.append(f"{rel}: 절대 경로 링크 {target}")
            continue
        path_part = target.split("#", 1)[0].split("?", 1)[0]
        if not path_part:
            continue
        dest = (p.parent / path_part).resolve()
        if dest.is_dir():
            errors.append(f"{rel}: 디렉터리를 가리키는 링크 {target} (index.md 까지 써야 한다)")
        elif not dest.is_file():
            errors.append(f"{rel}: 깨진 링크 {target}")
    refs = set(FOOT_REF.findall(scrubbed))
    defs = set(FOOT_DEF.findall(scrubbed))   # 코드 펜스 안의 예시 정의는 제외
    for r in sorted(refs - defs):
        errors.append(f"{rel}: 각주 [^{r}] 참조는 있으나 정의가 없음")
    for d in sorted(defs - refs):
        warnings.append(f"{rel}: 각주 [^{d}] 정의만 있고 참조가 없음")
    return errors, warnings


def main() -> int:
    errors, warnings = [], []
    files = sorted(paths.DOCS.rglob("*.md"))
    for p in files:
        e, w = scan(p)
        errors += e
        warnings += w
    for w in warnings:
        print("[warn]", w)
    if errors:
        print(f"[check_links] 오류 {len(errors)}건 (파일 {len(files)}개 검사)")
        for e in errors:
            print("-", e)
        return 1
    print(f"[check_links] 통과: 파일 {len(files)}개, 경고 {len(warnings)}건")
    return 0


if __name__ == "__main__":
    sys.exit(main())
