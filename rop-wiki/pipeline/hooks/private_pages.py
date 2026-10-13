"""mkdocs 훅 — 스터디(docs/field-research/) 잠금 페이지의 빌드 처리.

mkdocs.yml 의 `hooks:` 에 등록된다(pipeline/lib/nav.py 의 템플릿). 세 가지 일을 한다.

0. 잠금 비밀번호 확정(on_config, 플러그인보다 먼저 실행): mkdocs.yml 의 `study: !ENV [ROP_STUDY_PASSWORD, '<기본값>']` 은
   환경 변수가 "있지만 비어 있을 때" 빈 값이 되고, 값이 숫자만이면 YAML 이 정수로 읽어 플러그인이 멈춘다. 그래서
   password_inventory 의 값을 effective_password()(환경 변수 → config/ops.yaml publish.study_password 순)의 문자열로
   다시 넣는다. 둘 다 없으면 빌드를 멈춘다(잠금 없이 공개되는 일을 막는다). 어느 쪽을 썼는지 INFO 로그에 남긴다(값은 남기지 않는다).
1. 암호화된 원문 끼워 넣기: 프런트매터 private_source 가 가리키는 파일(_private/<slug>.md.enc, rop-wiki 기준 경로)을
   같은 비밀번호로 복호화해 틀 페이지의 MARKER 자리에 넣는다(없으면 본문 끝에). 비밀번호가 없는 빌드에서는 본문 대신
   안내문을 넣는다.
2. 잠금 페이지의 새는 곳 막기: docs/field-research/ 아래 페이지는 mkdocs-encryptcontent-plugin 이 본문 HTML 을
   잠그지만, 목차(오른쪽 사이드바·모바일 서랍)와 meta description 은 플러그인이 건드리지 않아 소제목이 그대로 보인다.
   그래서 템플릿을 그리기 전에 목차를 비우고 description 을 지운다. 검색 색인 제외는 페이지 프런트매터의
   `search: exclude: true`(mkdocs-material)가 맡는다.
"""
from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

from mkdocs.plugins import event_priority
from mkdocs.structure.toc import TableOfContents

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))

from private_pages import ENV, MARKER, NOTICE, decrypt, effective_password  # noqa: E402

LOCKED_PREFIX = "field-research/"   # docs 기준. 이 아래의 모든 페이지가 잠금 대상이다
PLUGIN = "encryptcontent"
log = logging.getLogger("mkdocs.plugins.private_pages")


def resolve_password_inventory(inventory: dict) -> str:
    """password_inventory 의 단일 비밀번호 항목을 effective_password() 문자열로 바꾼다. 쓴 출처를 돌려준다.
    목록·사용자별 사전 형태의 항목은 건드리지 않는다. 비밀번호가 없으면 ValueError."""
    password = effective_password()
    source = f"환경 변수 {ENV}" if os.environ.get(ENV, "") else "config/ops.yaml publish.study_password"
    for level, value in list(inventory.items()):
        if isinstance(value, (list, dict)):
            continue
        if not password:
            raise ValueError(f"스터디 잠금 비밀번호가 없다(level '{level}'): 환경 변수 {ENV} 또는 "
                             "config/ops.yaml 의 publish.study_password 에 둔다(README 5C)")
        inventory[level] = password
    return source


@event_priority(100)   # encryptcontent 플러그인의 on_config 보다 먼저
def on_config(config):
    plugin = config.plugins.get(PLUGIN) if hasattr(config.plugins, "get") else None
    if plugin is None:
        return config
    source = resolve_password_inventory(plugin.config["password_inventory"])
    log.info(f"스터디 잠금 비밀번호 출처: {source}")
    return config


def _locked(page) -> bool:
    return str(page.file.src_path).replace("\\", "/").startswith(LOCKED_PREFIX)


def on_page_markdown(markdown: str, page, config, files):
    src = page.meta.get("private_source")
    if not src:
        return markdown
    path = ROOT / str(src)
    if not path.is_file():
        raise FileNotFoundError(f"{page.file.src_path}: private_source 가 가리키는 암호문이 없다: {src}")
    password = effective_password()
    body = decrypt(path.read_text(encoding="utf-8"), password) if password else NOTICE
    if MARKER in markdown:
        return markdown.replace(MARKER, body, 1)
    return markdown.rstrip("\n") + "\n\n" + body + "\n"


def on_page_context(context, page, config, nav):
    if _locked(page):
        page.toc = TableOfContents([])
        page.meta.pop("description", None)
    return context
