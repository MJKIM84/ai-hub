"""마크다운 본문의 raw HTML 검사 (공개 배포 보안 보강 1항).

mkdocs.yml 의 md_in_html 확장 때문에 마크다운 안의 raw HTML 이 그대로 페이지에 렌더링된다. 위키 본문은
에이전트 산출물(runs/<id>/pages/)과 사람이 넣는 정정 요청·원문(inbox/)에서 오므로, 외부 텍스트가 프롬프트를
거쳐 <script> 같은 태그로 새어 나오지 않도록 두 곳에서 같은 규칙으로 막는다:
  - pipeline/validate_run.py --stage pages : 게시 전 에이전트 산출물 (게이트)
  - pipeline/checks/check_html.py          : docs/ 전체 (저장소 검사, run_all.sh)

허용: <br>, <br/>(줄바꿈), 오토링크 <https://…> <http://…> <mailto:…>, HTML 주석 <!-- … -->(auto 마커).
그 외 태그, on*= 속성, javascript:/vbscript:/data: 링크 대상은 오류. 코드 펜스·인라인 코드 안은 검사하지 않는다.
[가정: 현재 docs 에는 <br> 과 오토링크 외의 raw HTML 이 없어 허용 목록을 이렇게 좁혔다. 필요하면 ALLOWED_TAGS 에 더한다]
"""
from __future__ import annotations

import re

ALLOWED_TAGS = {"br"}

_FENCE = re.compile(r"^(```|~~~).*?^\1[ \t]*$", re.M | re.S)
_INLINE_CODE = re.compile(r"`[^`\n]*`")
_COMMENT = re.compile(r"<!--.*?-->", re.S)
_AUTOLINK = re.compile(r"<(?:https?://|mailto:)[^>\s]*>")
# 태그 이름 뒤에는 공백·/·> 만 온다: runs/<run_id>/ 같은 자리표시자는 태그가 아니다
# HTML 은 "<" 바로 뒤에 이름이 와야 태그다: "a < b" 같은 부등호는 태그가 아니다
_TAG = re.compile(r"<(/?)([A-Za-z][A-Za-z0-9-]*)(?=[\s/>])([^<>]*)>")
_EVENT_ATTR = re.compile(r"\son[a-z]+\s*=", re.I)
_LINK_TARGET = re.compile(r"\]\(\s*<?\s*([a-zA-Z][a-zA-Z0-9+.-]*):", re.I)
_DANGEROUS_SCHEMES = {"javascript", "vbscript", "data"}


def _blank(m: re.Match) -> str:
    """검사에서 뺄 구간을 같은 줄 수의 공백으로 바꿔 줄 번호를 보존한다."""
    return re.sub(r"[^\n]", " ", m.group(0))


def scrub(text: str) -> str:
    text = _FENCE.sub(_blank, text)
    text = _COMMENT.sub(_blank, text)
    text = _INLINE_CODE.sub(_blank, text)
    text = _AUTOLINK.sub(_blank, text)
    return text


def find_unsafe_html(text: str) -> list[str]:
    """허용되지 않은 raw HTML·위험한 링크 대상을 "줄 N: 설명" 목록으로 돌려준다. 비어 있으면 통과."""
    out: list[str] = []
    s = scrub(text)
    for m in _TAG.finditer(s):
        line = s.count("\n", 0, m.start()) + 1
        name = m.group(2).lower()
        attrs = (m.group(3) or "").rstrip()
        if attrs.endswith("/"):          # <br/> 같은 자기 닫힘
            attrs = attrs[:-1].rstrip()
        if name not in ALLOWED_TAGS:
            out.append(f"줄 {line}: 허용되지 않은 HTML 태그 <{m.group(1)}{name}>")
        elif _EVENT_ATTR.search(" " + attrs):
            out.append(f"줄 {line}: <{name}> 에 이벤트 속성(on*=)이 있다")
        elif attrs.strip():
            out.append(f"줄 {line}: <{name}> 에 속성이 있다({attrs.strip()[:40]})")
    for m in _LINK_TARGET.finditer(s):
        if m.group(1).lower() in _DANGEROUS_SCHEMES:
            line = s.count("\n", 0, m.start()) + 1
            out.append(f"줄 {line}: 링크 대상 스킴 {m.group(1).lower()}: 는 허용하지 않는다")
    return out


def escape_tags(cell: str) -> str:
    """표 셀 등 데이터에서 온 짧은 문자열용: 허용 태그·오토링크는 두고 태그 모양의 '<' 만 &lt; 로 바꾼다."""
    def rep(m: re.Match) -> str:
        name = m.group(2).lower()
        if name in ALLOWED_TAGS and not (m.group(3) or "").strip().rstrip("/").strip():
            return m.group(0)
        return "&lt;" + m.group(0)[1:]
    parts = []
    last = 0
    for a in _AUTOLINK.finditer(cell):
        parts.append(_TAG.sub(rep, cell[last:a.start()]))
        parts.append(a.group(0))
        last = a.end()
    parts.append(_TAG.sub(rep, cell[last:]))
    return "".join(parts)
