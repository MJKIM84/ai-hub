"""원문 인용 블록에 [분류원문] 태그를 붙이고(tag_blocks) 벗기는(strip_tags) 도우미.

규약
- 문단·목록 항목: 마지막 줄 끝에 " [분류원문]" 을 붙인다.
- 표: 표 바로 아래 빈 줄을 두고 "[분류원문]" 한 줄을 둔다.
- 원문 글자는 한 글자도 바꾸지 않는다. 태그를 벗기면 원문과 같은 줄이 나온다.
"""
from __future__ import annotations

import re

TAG = "[분류원문]"
_TAG_SUFFIX = " " + TAG
_BOLD = re.compile(r"\*\*(.+?)\*\*")


def strip_bold(s: str) -> str:
    """굵게 표시(**…**)만 제거한다. 제목 셀 전용."""
    return _BOLD.sub(r"\1", s)


def tag_line(line: str) -> str:
    return line + _TAG_SUFFIX


def _is_table_line(line: str) -> bool:
    return line.lstrip().startswith("|")


def _is_list_line(line: str) -> bool:
    return re.match(r"^\s*(\d+\.|[-*+])\s+", line) is not None


def split_blocks(text: str) -> list[list[str]]:
    """빈 줄로 구분된 블록(줄 목록) 배열을 만든다. 각 줄은 원문 그대로."""
    blocks: list[list[str]] = []
    cur: list[str] = []
    for line in text.split("\n"):
        if line.strip() == "":
            if cur:
                blocks.append(cur)
                cur = []
        else:
            cur.append(line)
    if cur:
        blocks.append(cur)
    return blocks


def tag_blocks(text: str) -> str:
    """원문 본문(여러 블록)에 규약대로 태그를 붙인 마크다운을 돌려준다."""
    out: list[str] = []
    for block in split_blocks(text):
        if _is_table_line(block[0]):
            out.append("\n".join(block))
            out.append("")
            out.append(TAG)
        elif all(_is_list_line(l) for l in block):
            out.append("\n".join(tag_line(l) for l in block))
        else:
            lines = list(block)
            lines[-1] = tag_line(lines[-1])
            out.append("\n".join(lines))
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def strip_tags(text: str) -> str:
    """태그를 벗겨 원문 비교용 문자열을 만든다. 태그만 있는 줄은 제거한다."""
    lines: list[str] = []
    for line in text.split("\n"):
        if line.strip() == TAG:
            # 표 아래 태그 줄과 그 앞의 빈 줄(tag_blocks 가 넣은 것)을 함께 제거한다
            if lines and lines[-1].strip() == "":
                lines.pop()
            continue
        if line.endswith(_TAG_SUFFIX):
            line = line[: -len(_TAG_SUFFIX)]
        lines.append(line)
    return "\n".join(lines)


def untag(line: str) -> str:
    """한 줄에서 끝의 태그를 벗긴다."""
    return line[: -len(_TAG_SUFFIX)] if line.endswith(_TAG_SUFFIX) else line
