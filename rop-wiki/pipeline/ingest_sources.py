#!/usr/bin/env python3
"""출처 원문 수집: inbox/sources/ 의 파일과 GitHub 원문 미러를 data/source_texts/ 로 옮긴다.

기본 동작(inbox):
  1. inbox/sources/manifest.yaml 의 items 를 읽는다. 항목: file(필수), url, title, org, published, ref_id(선택).
  2. inbox/sources/<file> 에서 텍스트를 뽑는다. PDF 는 pdftotext(poppler-utils), 없으면 pypdf(별도 프로세스),
     HTML 은 html.parser, TXT·MD 등은 그대로.
  3. 참고문헌과 연결한다: ref_id 가 있으면 그 id, 없으면 docs/references/ref-*.md 의 url 이 manifest url 과 같은 것.
     연결할 참고문헌이 없으면 src-<slug> 로 저장한다(나중에 ref_id 를 적고 다시 실행하면 연결된다).
  4. data/source_texts/<key>.txt 와 data/source_texts/index.json(sha256, 글자 수, 수집일, 경로 fetched_via: inbox)을 쓴다.
  5. 연결된 참고문헌 페이지의 프런트매터를 fetched: true, fetched_via: inbox 로 바꾸고 원문 열람 표시(서지 정보 표·각주 형식·비고)를
     갱신한다. 변경 이력(data/changelog.json)에 한 줄 남긴다(--no-changelog 로 끔).
  6. 처리한 파일을 inbox/sources/processed/ 로 옮긴다.
  같은 파일을 다시 넣어도 sha256 이 같으면 아무것도 바꾸지 않는다(멱등). 이미 processed/ 로 옮긴 항목은 건너뛴다.

--mirrors: 참고문헌마다 config/source_mirrors.yaml 의 원문 미러(relation original)나 github.com blob 의 raw 경로를 실제로 받아
  같은 방식으로 저장한다(fetched_via: github_raw). 받지 못하면(네트워크 정책 등) 로그만 남긴다. --refs 로 대상을 좁힌다.

사용:
  python3 pipeline/ingest_sources.py                     # inbox 처리
  python3 pipeline/ingest_sources.py --dry-run           # 무엇을 할지 출력만
  python3 pipeline/ingest_sources.py --mirrors [--refs ref-004,ref-009]
exit: 0 정상(처리할 것이 없어도 0), 1 처리하지 못한 항목이 있음(추출 실패·파일 없음·manifest 오류), 2 인자 오류.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import frontmatter as fm  # noqa: E402
from lib import paths  # noqa: E402
from lib import sources as S  # noqa: E402

MANIFEST = "manifest.yaml"
PROCESSED = "processed"


def load_manifest(inbox: Path) -> tuple[list[dict], list[str]]:
    """manifest.yaml → (항목 목록, 오류 목록). 파일이 없으면 ([], [])."""
    f = inbox / MANIFEST
    if not f.is_file():
        return [], []
    try:
        d = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        return [], [f"{f.name} 을 읽지 못함: {e}"]
    items = d.get("items") if isinstance(d, dict) else d
    if items is None:
        return [], []
    if not isinstance(items, list):
        return [], [f"{f.name} 의 items 는 목록이어야 한다"]
    out, errs = [], []
    for i, it in enumerate(items, 1):
        if not isinstance(it, dict):
            errs.append(f"items[{i}] 는 매핑이어야 한다")
            continue
        if not it.get("file"):
            errs.append(f"items[{i}] 에 file 이 없다")
            continue
        out.append(it)
    return out, errs


def _unique_dest(d: Path, name: str) -> Path:
    dest = d / name
    n = 2
    while dest.exists():
        stem, suf = Path(name).stem, Path(name).suffix
        dest = d / f"{stem}-{n}{suf}"
        n += 1
    return dest


def sync_pending_pages(root: Path | None = None, *, today: str | None = None, dry_run: bool = False) -> tuple[list[str], list[dict]]:
    """원문 텍스트가 있는 참고문헌 페이지의 원문 열람 표시를 텍스트 색인에 맞춘다(텍스트를 먼저 받고 페이지가 나중에 생긴 경우,
    원문이 바뀌어 글자 수가 달라진 경우 포함). 바뀔 것이 없으면 페이지를 건드리지 않는다. 네트워크를 쓰지 않는다. (로그 줄, 변경 이력 항목)."""
    today = today or paths.today()
    texts = S.load_source_texts(root)
    logs, entries = [], []
    for rid, p in S.reference_pages(root).items():
        if rid not in texts:
            continue
        if dry_run:
            if S.sync_reference_page(p, root=root, today=today, texts=texts, write=False):
                logs.append(f"{rid}: 원문 텍스트({texts[rid]['path']})를 참고문헌 페이지에 반영할 예정")
            continue
        ch = S.sync_reference_page(p, root=root, today=today, texts=texts)
        if ch:
            via = S.VIA_LABELS.get(str(texts[rid].get("fetched_via")), "")
            logs.append(f"{rid}: 참고문헌 페이지에 원문 텍스트 연결 — " + "; ".join(ch))
            entries.append({"date": today, "run_id": f"ingest-{today}", "action": "갱신", "page": f"docs/references/{rid}.md",
                            "summary": f"원문 텍스트 등록({via}, {int(texts[rid].get('chars') or 0):,}자) — 원문 열람 표시"})
    return logs, entries


def process_inbox(root: Path | None = None, *, today: str | None = None, dry_run: bool = False,
                  changelog: bool = True) -> tuple[list[str], int]:
    """inbox 처리. (로그 줄, 실패 건수)."""
    lay = S.Layout(root)
    today = today or paths.today()
    inbox = lay.inbox_dir
    logs: list[str] = []
    items, errs = load_manifest(inbox)
    fails = len(errs)
    logs += [f"manifest 오류: {e}" for e in errs]
    entries: list[dict] = []
    if not items and not errs:
        logs.append(f"처리할 항목 없음({lay.rel(inbox / MANIFEST)} 의 items 가 비었거나 파일이 없다)")
    for it in items:
        name = str(it["file"])
        src = inbox / name
        if not src.is_file():
            if (inbox / PROCESSED / name).exists():
                logs.append(f"{name}: 이미 처리됨(processed/) — 건너뜀")
            else:
                logs.append(f"{name}: 파일 없음(inbox/sources/{name}) — manifest 항목만 있다")
                fails += 1
            continue
        try:
            text, method, auto_title = S.extract_text_file(src)
        except S.ExtractError as e:
            logs.append(f"{name}: 텍스트 추출 실패 — {e}. 파일은 inbox 에 남겨 둔다")
            fails += 1
            continue
        if len(text.strip()) < 20:
            logs.append(f"{name}: 추출한 텍스트가 거의 없다({len(text.strip())}자). 스캔 PDF 면 OCR 이 필요하다. 파일은 inbox 에 남겨 둔다")
            fails += 1
            continue
        url = str(it.get("url") or "")
        ref_id = str(it.get("ref_id") or "").strip() or None
        pages = S.reference_pages(root)
        if ref_id and ref_id not in pages:
            logs.append(f"{name}: ref_id {ref_id} 의 참고문헌 페이지가 아직 없다 — 텍스트만 {ref_id} 로 저장한다(페이지가 생기면 다시 실행해 연결)")
        if not ref_id and url:
            ref_id = S.find_reference_by_url(url, root)
            if ref_id:
                logs.append(f"{name}: URL 이 같은 참고문헌 {ref_id} 에 연결")
        if ref_id and ref_id in pages and url:
            meta_url = fm.read(pages[ref_id])[0].get("url")
            if meta_url and S.normalize_url(str(meta_url)) != S.normalize_url(url):
                logs.append(f"{name}: 경고 — manifest url({url})이 {ref_id} 의 url({meta_url})과 다르다. ref_id 를 따른다")
        title = str(it.get("title") or auto_title or "")
        key = ref_id or S.slug_key(title, url, text)
        item, changed = S.store_source_text(text, key=key, ref_id=ref_id, title=title, url=url, org=str(it.get("org") or ""),
                                            published=it.get("published"), fetched_via="inbox", source=f"inbox/sources/{name}",
                                            method=method, root=root, today=today, dry_run=dry_run)
        logs.append(f"{name}: {'저장' if changed else '변경 없음'} → {item['path']} ({item['chars']:,}자, {method})")
        if ref_id and ref_id in pages and not dry_run:
            ch = S.sync_reference_page(pages[ref_id], root=root, today=today)
            if ch:
                logs.append(f"{name}: 참고문헌 {ref_id} 페이지 갱신 — " + "; ".join(ch))
                entries.append({"date": today, "run_id": f"ingest-{today}", "action": "갱신",
                                "page": f"docs/references/{ref_id}.md",
                                "summary": f"원문 텍스트 등록(inbox, {item['chars']:,}자) — 원문 열람 표시"})
        elif ref_id and ref_id in pages and dry_run:
            logs.append(f"{name}: 참고문헌 {ref_id} 페이지를 fetched: true, fetched_via: inbox 로 바꿀 예정")
        if not dry_run:
            dest = _unique_dest(inbox / PROCESSED, name)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dest))
            logs.append(f"{name}: {lay.rel(dest)} 로 옮김")
    more_logs, more_entries = sync_pending_pages(root, today=today, dry_run=dry_run)
    logs += more_logs
    entries += more_entries
    if changelog and entries and not dry_run:
        S.append_changelog(entries, root)
    return logs, fails


def process_mirrors(root: Path | None = None, *, refs: list[str] | None = None, today: str | None = None,
                    dry_run: bool = False, changelog: bool = True) -> tuple[list[str], int]:
    """원문 미러 수집 + 참고문헌 페이지 동기화. (로그 줄, 실패 건수)."""
    today = today or paths.today()
    logs = S.ingest_mirror_texts(refs, root=root, today=today, dry_run=dry_run)
    fails = sum(1 for l in logs if "하나도 받지 못함" in l)
    more_logs, entries = sync_pending_pages(root, today=today, dry_run=dry_run)
    logs += more_logs
    if changelog and entries and not dry_run:
        S.append_changelog(entries, root)
    return logs, fails


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mirrors", action="store_true", help="inbox 대신 참고문헌의 GitHub 원문 미러를 받아 저장")
    ap.add_argument("--refs", default="", help="--mirrors 대상 참고문헌 id(쉼표 구분)")
    ap.add_argument("--dry-run", action="store_true", help="파일을 쓰거나 옮기지 않고 할 일만 출력")
    ap.add_argument("--no-changelog", action="store_true", help="data/changelog.json 에 기록하지 않는다")
    ap.add_argument("--root", default=None, help="위키 루트(기본: 이 스크립트 기준 위키 루트). 테스트용")
    ap.add_argument("--today", default=None, help="수집일(YYYY-MM-DD). 기본 ROP_TODAY 또는 오늘")
    args = ap.parse_args(argv)
    root = Path(args.root) if args.root else None
    refs = [x.strip() for x in args.refs.split(",") if x.strip()] or None
    if args.mirrors:
        logs, fails = process_mirrors(root, refs=refs, today=args.today, dry_run=args.dry_run, changelog=not args.no_changelog)
    else:
        if refs:
            print("[ingest_sources] --refs 는 --mirrors 와 함께 쓴다", file=sys.stderr)
            return 2
        logs, fails = process_inbox(root, today=args.today, dry_run=args.dry_run, changelog=not args.no_changelog)
    for line in logs:
        print(f"[ingest_sources] {line}")
    print(f"[ingest_sources] 완료{' (dry-run)' if args.dry_run else ''}: 로그 {len(logs)}줄, 실패 {fails}건")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
