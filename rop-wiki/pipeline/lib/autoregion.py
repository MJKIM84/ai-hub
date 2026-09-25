"""자동 갱신 영역 규약.

퍼블리셔가 다시 쓰는 부분은 반드시
    <!-- auto:<key>:start -->
    …
    <!-- auto:<key>:end -->
사이에 둔다. 마커 밖의 본문은 스크립트가 건드리지 않는다.
"""
from __future__ import annotations

import re

AUTO_KEYS: list[str] = [
    "home-track-status", "home-recent", "category-recent", "area-recent",
    "track-progress", "track-recent-runs", "backlog", "open-questions",
    "changelog", "flow-matrix", "metrics", "glossary-index", "references-index",
    "standards-table", "topics-index", "logs-index", "ontology-version-history",
    # 백본 추가 키 [가정]: 대분류 페이지의 세부 연구영역 표(현재 상태 열 갱신용)
    "category-area-table",
    # 백본 추가 키 [가정]: 참고문헌 페이지의 "인용된 페이지" 목록(docs 전체의 sources·[^ref-id]·링크를 스캔)
    "reference-cited-pages",
    # 파이프라인 추가 키 [가정]: 트랙 로그 페이지(docs/tracks/<slug>/log.md)의 "실행 기록" 절. 원천은 data/tracks/<slug>/log.json 이고
    # 퍼블리셔가 트랙 실행마다 항목을 더한 뒤 refresh_all_auto_regions() 가 최신순으로 다시 만든다(사양서 4.6 트랙 로그 갱신 주체: 퍼블리셔)
    "track-log",
    # 확장 아이디어·다중 트랙 추가 키 [가정]
    # - area-tracks: 세부영역 페이지 머리(소속 대분류 admonition 아래)의 "관련 연구 트랙" 안내. 원천은 config/tracks/*.yaml 의
    #   primary_area·related_areas·idea_areas. 연결된 트랙이 없으면 빈 영역
    # - idea-area-map: 확장 아이디어 색인(docs/ideas/index.md)의 28개 세부영역 × 아이디어 매핑표(●/○). 원천은 트랙 정의의 idea_areas
    # - idea-areas: 아이디어 페이지 "2. 관련 세부 연구영역"의 매핑 목록(●/○와 근거). 원천은 idea_areas·idea_area_notes
    # - idea-backlog: 아이디어 페이지 "7. 미해결 질문 백로그". 원천은 data/tracks/<slug>/backlog.json(열림·조사 중·답함 …)
    # - page-status: 본문 상태 줄의 단일 원천. 프런트매터(status·confidence·version·updated·last_run)에서 한 줄을 만든다.
    #   본문에 손으로 쓴 상태 줄("페이지 상태:", "> 상태: draft …")은 check_frontmatter 가 오류로 본다
    "area-tracks", "idea-area-map", "idea-areas", "idea-backlog", "page-status",
]

_START = "<!-- auto:{key}:start -->"
_END = "<!-- auto:{key}:end -->"
_ANY = re.compile(r"<!-- auto:([a-z0-9-]+):start -->")


def start_marker(key: str) -> str:
    return _START.format(key=key)


def end_marker(key: str) -> str:
    return _END.format(key=key)


def wrap(key: str, content: str = "") -> str:
    """마커로 감싼 영역 문자열을 만든다(페이지 생성용)."""
    body = content.strip("\n")
    inner = ("\n" + body + "\n") if body else "\n"
    return f"{start_marker(key)}{inner}{end_marker(key)}"


def _pattern(key: str) -> re.Pattern:
    return re.compile(re.escape(start_marker(key)) + r"(.*?)" + re.escape(end_marker(key)), re.S)


def has_region(text: str, key: str) -> bool:
    return _pattern(key).search(text) is not None


def list_regions(text: str) -> list[str]:
    """본문에 있는 auto 키 목록(등장 순서)."""
    return _ANY.findall(text)


def get_region(text: str, key: str):
    """영역 본문(마커 제외, 앞뒤 개행 제거). 없으면 None."""
    m = _pattern(key).search(text)
    if not m:
        return None
    return m.group(1).strip("\n")


def replace_region(text: str, key: str, new_content: str) -> str:
    """영역 본문을 new_content 로 바꾼다. 마커가 없으면 KeyError."""
    pat = _pattern(key)
    if not pat.search(text):
        raise KeyError(f"auto 영역 없음: {key}")
    body = new_content.strip("\n")
    inner = ("\n" + body + "\n") if body else "\n"
    # 치환 문자열의 백슬래시 해석을 피하기 위해 함수로 치환
    return pat.sub(lambda m: start_marker(key) + inner + end_marker(key), text, count=1)
