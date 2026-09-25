"""mkdocs 내비게이션 생성(사양서 4.8 순서)과 mkdocs.yml 작성.

- build_nav(): 파일시스템에 존재하는 페이지만으로 nav 구조(list)를 만든다.
  라벨은 각 파일 프런트매터의 title(원문 명칭 그대로)이다.
- write_mkdocs_yml(): 문자열 템플릿 + nav 의 yaml.safe_dump 결과로 mkdocs.yml 전체를 쓴다.
  (markdown_extensions 에 !!python/name 태그가 있어 yaml.dump 로 전체를 만들지 않는다.)
- load_mkdocs_yml(): !!python/name / !ENV 태그를 문자열로 읽는 안전한 로더.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

from . import frontmatter as fm
from . import paths
from .paths import DOCS, MKDOCS_YML

SITE_NAME = "ROP 연구 위키"
SITE_DESCRIPTION = "SCM 관점의 로봇 오케스트레이션 플랫폼 연구"
TRACKS_LABEL = "중점 연구 트랙"
IDEAS_LABEL = "확장 아이디어"      # 사양서 4.8 목록 밖의 구축자 추가 섹션 [가정]

MKDOCS_TEMPLATE = """# 이 파일은 pipeline/lib/nav.py 의 write_mkdocs_yml() 이 생성한다. 손으로 고치지 말 것.
# 내비게이션 순서는 사양서 4.8 로 고정: 홈 → 소개 → 대분류 A~G → 중점 연구 트랙 → 주제 → 용어집 →
# 참고문헌 → 표준·프레임워크 → 열린 질문 → 흐름 매트릭스 → 변경 이력 → 운영 지표 → 로그.
# 4.8 에 없는 "확장 아이디어"(docs/ideas/)는 중점 연구 트랙 바로 다음, 주제 앞에 둔다(4.8 순서는 그대로). [가정]
# 4.7 의 횡단 페이지 "정정 요청 안내"는 4.8 순서 목록에 없으므로 그 순서를 끊지 않도록 맨 뒤(로그 다음)에 둔다. [가정]
site_name: {site_name}
site_description: {site_description}
docs_dir: docs
site_dir: site
use_directory_urls: true

theme:
  name: material
  language: ko
  features:
    - navigation.indexes
    - navigation.top
    - search.suggest
    - content.code.copy
    - toc.follow

markdown_extensions:
  - footnotes
  - admonition
  - sane_lists          # 참고문헌 페이지의 원문 12장 항목("5. …")이 원문 번호 그대로(start=5) 렌더링되게 한다
  - pymdownx.details
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - tables
  - toc:
      permalink: true
      slugify: !!python/object/apply:pymdownx.slugs.slugify
        kwds:
          case: lower
  - attr_list
  - md_in_html
  - pymdownx.tabbed:
      alternate_style: true

plugins:
  - search

validation:
  nav:
    omitted_files: warn
    not_found: warn
    absolute_links: warn
  links:
    not_found: warn
    anchors: warn
    absolute_links: warn
    unrecognized_links: warn

nav:
{nav}"""


def _title(rel: str) -> str:
    """docs 기준 상대 경로의 프런트매터 title. 없으면 파일 이름."""
    p = DOCS / rel
    try:
        meta, _ = fm.read(p)
        t = meta.get("title")
        if t:
            return str(t)
    except Exception:
        pass
    return p.stem


def _exists(rel: str) -> bool:
    return (DOCS / rel).is_file()


def _md_files(rel_dir: str, exclude_index: bool = True) -> list[str]:
    d = DOCS / rel_dir
    if not d.is_dir():
        return []
    out = []
    for p in sorted(d.glob("*.md")):
        if exclude_index and p.name == "index.md":
            continue
        out.append(f"{rel_dir}/{p.name}")
    return out


def _page(rel: str) -> dict:
    return {_title(rel): rel}


def _section_with_index(label: str, index_rel: str, children: list) -> dict:
    """navigation.indexes 용 섹션: 첫 항목이 라벨 없는 index.md 경로."""
    return {label: [index_rel, *children]}


def _stage_no(name: str) -> int:
    m = re.match(r"stage-(\d+)", name)
    return int(m.group(1)) if m else 999


def _track_children(slug: str) -> list:
    rel_dir = f"tracks/{slug}"
    d = DOCS / rel_dir
    stage_files = sorted((p.name for p in d.glob("stage-*.md")), key=_stage_no)
    # 초안 페이지는 트랙 정의의 draft_page(없으면 ontology-draft.md) 자리에 온다
    order = ["index.md", *stage_files, *paths.track_page_order(slug)[1:]]
    known = set(order)
    extras = sorted(p.name for p in d.glob("*.md") if p.name not in known)
    children = []
    for name in order[1:] + extras:
        rel = f"{rel_dir}/{name}"
        if _exists(rel):
            children.append(_page(rel))
    return children


def build_nav() -> list:
    nav: list = []

    # 1. 홈
    if _exists("index.md"):
        nav.append({"홈": "index.md"})

    # 2. 소개 (4.2 표 순서, 나머지는 파일명순)
    about = [f"about/{n}.md" for n in paths.ABOUT_ORDER if _exists(f"about/{n}.md")]
    known = set(about)
    about += [r for r in _md_files("about", exclude_index=False) if r not in known]
    if about:
        nav.append({"소개": [_page(r) for r in about]})

    # 3. 대분류 A~G (index.md 를 섹션 인덱스로, 하위에 세부영역 번호순)
    for letter in paths.CATEGORY_LETTERS:
        idx = paths.category_index_rel(letter)
        if not _exists(idx):
            continue
        children = [_page(paths.area_rel_path(no)) for no in paths.area_nos_of(letter)
                    if _exists(paths.area_rel_path(no))]
        nav.append(_section_with_index(_title(idx), idx, children))

    # 4. 중점 연구 트랙 — 트랙 정의의 order 순(첫 트랙이 맨 앞, 이어서 추가된 트랙). 정의 없는 폴더는 뒤에 slug 순
    tracks_dir = DOCS / "tracks"
    track_items = []
    if tracks_dir.is_dir():
        for slug in paths.ordered_track_slugs():
            if not (tracks_dir / slug).is_dir():
                continue
            idx = f"tracks/{slug}/index.md"
            children = _track_children(slug)
            if _exists(idx):
                track_items.append(_section_with_index(_title(idx), idx, children))
            elif children:
                track_items.append({slug: children})
    if track_items:
        nav.append({TRACKS_LABEL: track_items})

    # 4-1. 확장 아이디어 (4.8 목록 밖의 구축자 추가 섹션 [가정]) — 색인 → 트랙 순서대로 아이디어 페이지 → 나머지 파일명순
    ideas = [r for r in paths.idea_page_rels() if _exists(r)]
    known = set(ideas) | {paths.IDEAS_INDEX}
    ideas += [r for r in _md_files(paths.IDEAS_DIR) if r not in known]
    if _exists(paths.IDEAS_INDEX):
        nav.append(_section_with_index(IDEAS_LABEL, paths.IDEAS_INDEX, [_page(r) for r in ideas]))
    elif ideas:
        nav.append({IDEAS_LABEL: [_page(r) for r in ideas]})

    # 5. 주제 (연도별 하위, 최신 우선)
    topics_dir = DOCS / "topics"
    if topics_dir.is_dir():
        items: list = []
        if _exists("topics/index.md"):
            items.append("topics/index.md")
        years = sorted((p for p in topics_dir.iterdir() if p.is_dir() and p.name.isdigit()),
                       key=lambda p: p.name, reverse=True)
        for y in years:
            files = sorted((p.name for p in y.glob("*.md")), reverse=True)
            pages = [_page(f"topics/{y.name}/{n}") for n in files]
            if pages:
                items.append({y.name: pages})
        if items:
            nav.append({"주제": items})

    # 6. 용어집
    if _exists("glossary/index.md"):
        terms = sorted(_md_files("glossary"), key=_title)
        nav.append(_section_with_index(_title("glossary/index.md"), "glossary/index.md",
                                       [_page(r) for r in terms]))

    # 7. 참고문헌
    if _exists("references/index.md"):
        refs = _md_files("references")
        nav.append(_section_with_index(_title("references/index.md"), "references/index.md",
                                       [_page(r) for r in refs]))

    # 8. 표준·프레임워크
    if _exists("standards/index.md"):
        others = _md_files("standards")
        if others:
            nav.append(_section_with_index(_title("standards/index.md"), "standards/index.md",
                                           [_page(r) for r in others]))
        else:
            nav.append(_page("standards/index.md"))

    # 9~12. 열린 질문 → 흐름 매트릭스 → 변경 이력 → 운영 지표
    for rel in ("open-questions.md", "flow-matrix.md", "changelog.md", "metrics.md"):
        if _exists(rel):
            nav.append(_page(rel))

    # 13. 로그 (index, 일일, 주간 — 최신 우선)
    if (DOCS / "logs").is_dir():
        items = []
        if _exists("logs/index.md"):
            items.append("logs/index.md")
        daily = sorted(_md_files("logs/daily"), reverse=True)
        weekly = sorted(_md_files("logs/weekly"), reverse=True)
        if daily:
            items.append({"일일 로그": [_page(r) for r in daily]})
        if weekly:
            items.append({"주간 정리": [_page(r) for r in weekly]})
        if items:
            nav.append({"로그": items})

    # 14. 정정 요청 안내 — 4.7 의 횡단 페이지이지만 4.8 순서 목록에는 없다. 4.8 의 순서를 글자 그대로
    #     유지하기 위해 목록 끝(로그 다음)에 덧붙인다. [가정]
    if _exists("corrections.md"):
        nav.append(_page("corrections.md"))
    return nav


def nav_yaml(nav: list) -> str:
    return yaml.safe_dump(nav, allow_unicode=True, sort_keys=False, default_flow_style=False, width=1000)


def render_mkdocs_yml(nav: list | None = None) -> str:
    nav = build_nav() if nav is None else nav
    indented = "".join("  " + line + "\n" for line in nav_yaml(nav).rstrip("\n").split("\n"))
    return MKDOCS_TEMPLATE.format(site_name=SITE_NAME, site_description=SITE_DESCRIPTION, nav=indented)


def write_mkdocs_yml(path: Path = MKDOCS_YML) -> Path:
    text = render_mkdocs_yml()
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")
    return path


def mkdocs_yml_is_current(path: Path = MKDOCS_YML) -> bool:
    """저장된 mkdocs.yml 이 현재 파일시스템 기준 render_mkdocs_yml() 결과와 같은지(검사 스크립트용)."""
    return path.is_file() and path.read_text(encoding="utf-8") == render_mkdocs_yml()


class MkdocsLoader(yaml.SafeLoader):
    """!!python/name:… 와 !ENV 태그를 문자열로 읽는 로더(검사 스크립트용)."""


MkdocsLoader.add_multi_constructor("tag:yaml.org,2002:python/", lambda loader, suffix, node: f"python/{suffix}")
MkdocsLoader.add_constructor("!ENV", lambda loader, node: loader.construct_scalar(node) if isinstance(node, yaml.ScalarNode) else None)


def load_mkdocs_yml(path: Path = MKDOCS_YML) -> dict:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=MkdocsLoader)


def flatten_nav(nav: list, labels: list[tuple[str | None, str]] | None = None) -> list[tuple[str | None, str]]:
    """nav 를 (라벨, 경로) 목록으로 편다. 섹션 인덱스(라벨 없는 경로)는 (None, 경로)."""
    out = labels if labels is not None else []
    for item in nav:
        if isinstance(item, str):
            out.append((None, item))
        elif isinstance(item, dict):
            for label, value in item.items():
                if isinstance(value, str):
                    out.append((label, value))
                else:
                    # 섹션: 첫 항목이 경로 문자열이면 섹션 라벨이 그 페이지의 라벨이다
                    if value and isinstance(value[0], str):
                        out.append((label, value[0]))
                        flatten_nav(value[1:], out)
                    else:
                        flatten_nav(value, out)
    return out
