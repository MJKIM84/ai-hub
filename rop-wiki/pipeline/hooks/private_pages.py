"""mkdocs 훅 — 스터디(docs/field-research/) 잠금 페이지의 빌드 처리.

mkdocs.yml 의 `hooks:` 에 등록된다(pipeline/lib/nav.py 의 템플릿). 두 가지 일을 한다.

1. 암호화된 원문 끼워 넣기: 프런트매터 private_source 가 가리키는 파일(_private/<slug>.md.enc, rop-wiki 기준 경로)을
   환경 변수 ROP_STUDY_PASSWORD 로 복호화해 틀 페이지의 MARKER 자리에 넣는다(없으면 본문 끝에). 비밀번호가 없는 빌드
   (로컬 미리보기 등)에서는 본문 대신 안내문을 넣는다. 배포 워크플로는 비밀번호가 없으면 빌드를 중단한다.
2. 잠금 페이지의 새는 곳 막기: docs/field-research/ 아래 페이지는 mkdocs-encryptcontent-plugin 이 본문 HTML 을
   잠그지만, 목차(오른쪽 사이드바·모바일 서랍)와 meta description 은 플러그인이 건드리지 않아 소제목이 그대로 보인다.
   그래서 템플릿을 그리기 전에 목차를 비우고 description 을 지운다. 검색 색인 제외는 페이지 프런트매터의
   `search: exclude: true`(mkdocs-material)가 맡는다.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from mkdocs.structure.toc import TableOfContents

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))

from private_pages import ENV, MARKER, NOTICE, decrypt  # noqa: E402

LOCKED_PREFIX = "field-research/"   # docs 기준. 이 아래의 모든 페이지가 잠금 대상이다


def _locked(page) -> bool:
    return str(page.file.src_path).replace("\\", "/").startswith(LOCKED_PREFIX)


def on_page_markdown(markdown: str, page, config, files):
    src = page.meta.get("private_source")
    if not src:
        return markdown
    path = ROOT / str(src)
    if not path.is_file():
        raise FileNotFoundError(f"{page.file.src_path}: private_source 가 가리키는 암호문이 없다: {src}")
    password = os.environ.get(ENV, "")
    body = decrypt(path.read_text(encoding="utf-8"), password) if password else NOTICE
    if MARKER in markdown:
        return markdown.replace(MARKER, body, 1)
    return markdown.rstrip("\n") + "\n\n" + body + "\n"


def on_page_context(context, page, config, nav):
    if _locked(page):
        page.toc = TableOfContents([])
        page.meta.pop("description", None)
    return context
