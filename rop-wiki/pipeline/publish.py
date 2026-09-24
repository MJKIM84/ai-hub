#!/usr/bin/env python3
"""퍼블리셔 (사양서 6.4, 스크립트이며 LLM 이 아니다).

  python3 pipeline/publish.py <run_id> [--check-only | --dry-run | --log-only] [--no-build] [--no-commit]

사양서 6.4 의 9단계 번호를 그대로 쓴다. 순서대로 실행하고 하나라도 실패하면 반영하지 않는다.
 1.  스키마 검증(research/verification/verification2/pages + 참조 무결성·트랙 조건)
 1b. 판정 확인(1단계의 일부): 1차 승인|조건부 승인 그리고 2차 통과 가 아니면 즉시 중단
 2.  프런트매터 필수 필드 검증(pages/) + 반영 전 사전 검사(참고문헌 id 충돌, 온톨로지 버전 대조, deprecated 의 replaced_by)
     — 5단계 안에서 실패해 부분 반영이 남지 않도록 스냅숏 이전에 실패시킨다
 3.  원문 보호 검사: pages/ 를 docs 에 복사한 상태에서 checks/protect_source.py (실패 시 스냅숏에서 원복)
 4.  내부 링크·각주 검사(checks/check_links.py) + 프런트매터·이동 경로 검사(checks/check_frontmatter.py)
 5.  반영: 페이지 status published·updated·last_run·version, 용어집·참고문헌·표준·열린 질문·흐름 매트릭스·변경 이력,
     트랙(백로그·새 질문·트랙 로그·온톨로지 버전 이력·단계 전환·세부영역 반영 제안), 정정 요청 상태,
     자동 갱신 영역(refresh_all_auto_regions) + mkdocs.yml(write_mkdocs_yml) → 최종 검사 → (예비) 일일 로그·요약
 6.  사이트 빌드(settings.site_build_cmd) — 실패하면 스냅숏으로 docs/data/config/tracks/mkdocs.yml/inbox 를 되돌리고 로그에 남긴다
 7.  git 커밋(settings.git_commit) — "run(<date>): <실행 유형 한국어> <대상 영역 이름> — 생성 n/갱신 n"
 8.  일일 로그 docs/logs/daily/<date>.md 확정 + runs/<run_id>/summary.json → 재빌드 → 커밋 수정(amend).
     재빌드가 실패하면 확정 로그 변경분만 되돌리고 amend 를 건너뛴다
 9.  알림(notify 가 none 이 아니면 자리만)

실패 처리: 스냅숏(runs/<run_id>/backup/) 이후 어느 단계에서든 PublishError 가 나면 커밋 전이면 스냅숏으로 되돌린다.
스냅숏 복원은 git checkout 을 쓰지 않는다(사용자의 미커밋 inbox/corrections.md·config/tracks 수정을 보존한다).

옵션
  --check-only : 1단계(스키마·판정 확인)만 확인하고 끝낸다(schemas/examples 로 드라이 체크 가능)
  --dry-run    : 1~4단계를 실행하되 docs 를 원래대로 되돌리고 반영하지 않는다
  --log-only   : 보류·중단된 실행의 일일 로그와 summary.json 만 쓴다(runs/parked/ 도 찾는다)
  --no-build / --no-commit : 6·7단계를 건너뛴다(시험용)
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import autoregion as ar  # noqa: E402
from lib import frontmatter as fm  # noqa: E402
from lib import paths, runs  # noqa: E402
from lib.nav import write_mkdocs_yml  # noqa: E402
from lib.render import load_backlog, refresh_all_auto_regions  # noqa: E402
from lib.source import load_source  # noqa: E402
import render_run_md  # noqa: E402

ROOT = paths.ROOT
CHECKS = ROOT / "pipeline" / "checks"
SNAPSHOT_ITEMS = ["docs", "data", "config/tracks", "mkdocs.yml", "inbox/corrections.md"]
FINAL_SNAPSHOT_ITEMS = ["docs", "mkdocs.yml"]   # 8단계 확정 로그 재빌드 실패 시 되돌릴 범위(확정 로그·자동 영역·내비만 바뀐다)
TRACK_PAGE_TYPES = {"track", "track-stage", "ontology-draft", "track-log", "questions"}
OPEN_STATES = ("열림", "조사 중")
RUN_TYPE_UNSET = "미선정"   # target.json 이 없는(대상 선정 전에 중단된) 실행의 실행 유형 표시


class PublishError(RuntimeError):
    pass


def _run_check(script: str, *args: str) -> tuple[int, str]:
    p = subprocess.run([sys.executable, str(CHECKS / script), *args], capture_output=True, text=True, cwd=str(ROOT))
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def _slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", str(text or "").lower()).strip("-")
    return re.sub(r"-{2,}", "-", s)


def _short(s, n=80) -> str:
    s = str(s or "")
    return s if len(s) <= n else s[:n].rstrip() + "…"


def _norm_term(s) -> str:
    """용어 비교용 정규화: 소문자, 공백·구두점 제거(한글·영숫자만 남긴다)."""
    return re.sub(r"[^0-9a-z가-힣]+", "", str(s or "").lower())


def _term_keys(*terms) -> set[str]:
    """용어 문자열들에서 비교 키 집합을 만든다. "Electronic Product Code Information Services (EPCIS)" 처럼
    괄호 약어가 붙은 표기는 전체·괄호 앞·괄호 안을 모두 키로 삼아, 약어만 주거나 풀어 쓴 이름만 준 경우도 같은 용어로 본다."""
    keys: set[str] = set()
    for t in terms:
        t = str(t or "").strip()
        if not t:
            continue
        keys.add(_norm_term(t))
        m = re.match(r"^(.*?)\s*\(([^()]+)\)\s*$", t)
        if m:
            keys.add(_norm_term(m.group(1)))
            keys.add(_norm_term(m.group(2)))
    keys.discard("")
    return keys


def _footnote_line(ref: dict) -> str:
    pub = ref.get("published")
    pub = str(pub) if pub not in (None, "", "미확인") else "발행일 미확인"
    tail = " (원문 미열람)" if ref.get("source_unopened") else ""
    return f"[^{ref['id']}]: {ref.get('org', '')}, {ref.get('title', '')}, {pub}, {ref.get('url', '')}, 접근일 {ref.get('accessed', '')}{tail}"


def _ref_from_page(ref_id: str) -> dict | None:
    p = paths.DOCS / "references" / f"{ref_id}.md"
    if not p.is_file():
        return None
    meta, _ = fm.read(p)
    return {"id": ref_id, "org": meta.get("org", ""), "title": meta.get("ref_title") or meta.get("title", ""),
            "published": meta.get("published"), "url": meta.get("url", ""), "accessed": meta.get("accessed", ""),
            "source_unopened": meta.get("url_verified") is False}


class Publisher:
    def __init__(self, run_id: str, settings: dict, args):
        self.run_id = run_id
        self.settings = settings
        self.args = args
        self.rd = runs.find_run_dir(run_id, settings)
        if not self.rd:
            raise PublishError(f"실행 폴더 없음: runs/{run_id}")
        self.log = runs.RunLog(self.rd, settings)
        self.log.ensure(run_id)
        self.t0 = time.time()
        self.target = runs.read_json(self.rd / "target.json", {}) or {}
        self.date = self.target.get("date") or run_id[:10]
        os.environ.setdefault("ROP_TODAY", self.date)
        # target.json 이 없으면(대상 선정 전 중단) 실행 유형은 None 으로 두고 로그에는 "미선정", summary.json 에는 null 로 쓴다
        self.run_type = self.target.get("run_type") or None
        self.track = self.target.get("track") if self.run_type == "track" else None
        self.track_cfg = runs.load_track_config(self.track["slug"]) if self.track else None
        self.research = runs.read_json(self.rd / "research.json", None)
        self.v1 = runs.read_json(self.rd / "verification.json", None)
        self.v2 = runs.read_json(self.rd / "verification2.json", None)
        self.pages = runs.read_json(self.rd / "pages.json", None)
        self.backup = self.rd / "backup"
        self.snapshotted = False
        self.restored = False
        self.copied: list[Path] = []
        self.existing_refs_before = set(runs.existing_reference_ids())
        self.notes: list[str] = []
        self.counts = {"create": 0, "update": 0, "deprecate": 0, "glossary": 0, "references": 0, "standards": 0,
                       "open_questions": 0, "flow_cells": 0, "backlog": 0, "corrections": 0}
        self.committed = False
        self.commit_hash = None
        self.built = False
        self.src = load_source()

    # --- 공통 ------------------------------------------------------------------------
    def info(self, msg: str, step: str = "퍼블리셔") -> None:
        self.log.log(msg, step=step)
        print(f"[publish] {msg}")

    def run_type_label(self) -> str:
        """실행 유형의 한국어 표시. target.json 이 없으면 '미선정'."""
        if not self.run_type:
            return RUN_TYPE_UNSET
        return runs.RUN_TYPE_KO.get(self.run_type, self.run_type)

    def page_rel(self, pg: dict) -> str:
        return paths.docs_rel(pg.get("path", ""))

    def page_src(self, pg: dict) -> Path:
        return self.rd / "pages" / self.page_rel(pg)

    def page_dst(self, pg: dict) -> Path:
        return paths.DOCS / self.page_rel(pg)

    # --- 1. 스키마 검증 -----------------------------------------------------------------
    def step1_schema(self) -> None:
        missing = [n for n, d in (("research.json", self.research), ("verification.json", self.v1),
                                  ("verification2.json", self.v2), ("pages.json", self.pages)) if d is None]
        if missing:
            raise PublishError(f"1단계 스키마 검증: 산출물 없음 {missing}")
        errs = []
        for kind, data, label in (("research", self.research, "research.json"), ("verification", self.v1, "verification.json"),
                                  ("verification", self.v2, "verification2.json"), ("pages", self.pages, "pages.json")):
            errs += [f"{label} {e}" for e in runs.validate(kind, data)]
        if errs:
            raise PublishError("1단계 스키마 검증 실패:\n" + "\n".join(f"  - {e}" for e in errs[:40]))
        errs += [f"research.json {e}" for e in runs.semantic_checks("research", self.research, self.run_type, self.track_cfg)]
        errs += [f"verification.json {e}" for e in runs.semantic_checks("verification", self.v1, self.run_type, self.track_cfg, self.research)]
        errs += [f"verification2.json {e}" for e in runs.semantic_checks("verification", self.v2, self.run_type, self.track_cfg, self.research)]
        errs += [f"pages.json {e}" for e in runs.semantic_checks("pages", self.pages, self.run_type, self.track_cfg)]
        for f, label in ((self.v1, "verification.json"), (self.v2, "verification2.json"), (self.pages, "pages.json")):
            if f.get("run_id") != self.run_id:
                errs.append(f"{label}: run_id {f.get('run_id')!r} 가 {self.run_id!r} 와 다르다")
        if self.v1.get("stage") != "first":
            errs.append("verification.json 의 stage 가 first 가 아니다")
        if self.v2.get("stage") != "second":
            errs.append("verification2.json 의 stage 가 second 가 아니다")
        if self.research.get("run_id") != self.run_id:
            errs.append(f"research.json: run_id {self.research.get('run_id')!r} 가 {self.run_id!r} 와 다르다")
        if not self.args.check_only:
            for pg in self.pages.get("pages", []):
                if not self.page_src(pg).is_file():
                    errs.append(f"pages/ 에 파일 없음: {self.page_src(pg).relative_to(ROOT)}")
        if errs:
            raise PublishError("1단계 스키마 밖 검사 실패:\n" + "\n".join(f"  - {e}" for e in errs[:40]))
        render_run_md.render_run(self.rd)  # 사람이 읽는 research.md·verification.md·verification2.md·pages.md 를 최신으로
        self.info("1단계 스키마 검증 통과 (research, verification, verification2, pages)")

    # --- 1b. 판정 확인(1단계의 일부) ------------------------------------------------------------
    def step1b_verdicts(self) -> None:
        a, b = self.v1.get("verdict"), self.v2.get("verdict")
        if a not in ("승인", "조건부 승인"):
            raise PublishError(f"1단계(판정 확인): 1차 검증 판정이 승인·조건부 승인이 아니다({a}) — 반영하지 않는다")
        if b != "통과":
            raise PublishError(f"1단계(판정 확인): 2차 검증 판정이 통과가 아니다({b}) — 반영하지 않는다")
        self.info(f"1단계 판정 확인 통과 (1차 {a} / 2차 {b} · 신뢰도 {self.v2.get('confidence')})")

    # --- 2. 프런트매터 + 반영 전 사전 검사 --------------------------------------------------------
    def _preapply_checks(self) -> list[str]:
        """5단계(반영) 안에서 실패하면 부분 반영이 남으므로, 반영 중에 PublishError 를 내던 조건을 스냅숏 이전에 미리 검사한다.
        - 참고문헌 id 충돌(reference_updates 의 id 가 docs/references/ 에 다른 URL 로 이미 있음)
        - 온톨로지 버전 불일치(pages.json track_updates.ontology_draft_version 과 온톨로지 초안 페이지의 ontology_version)
        - deprecated 페이지의 replaced_by 없음(pages.json status 가 deprecated 인 경우 포함)"""
        errs: list[str] = []
        for r in self.pages.get("reference_updates") or []:
            rid = str(r.get("id", ""))
            p = paths.DOCS / "references" / f"{rid}.md"
            if p.is_file():
                try:
                    meta, _ = fm.read(p)
                except Exception:
                    continue
                if str(meta.get("url", "")).rstrip("/") != str(r.get("url", "")).rstrip("/"):
                    errs.append(f"참고문헌 id 충돌: {rid} 는 이미 다른 출처({meta.get('url')})에 쓰였다. 브리프의 출처 id 를 다음 번호로 다시 부여해야 한다")
        for pg in self.pages.get("pages", []):
            if pg.get("status") == "deprecated":
                try:
                    meta, _ = fm.read(self.page_src(pg))
                except Exception:
                    continue
                if not meta.get("replaced_by"):
                    errs.append(f"{self.page_rel(pg)}: pages.json status 가 deprecated 인데 프런트매터에 replaced_by(대체 페이지 링크)가 없다")
        if self.track:
            tu = self.pages.get("track_updates") or {}
            new_version = str(tu.get("ontology_draft_version") or "")
            od_rel = f"tracks/{self.track['slug']}/ontology-draft.md"
            cand = self.rd / "pages" / od_rel
            if not cand.is_file():
                cand = paths.DOCS / od_rel
            if new_version and cand.is_file():
                try:
                    m, _ = fm.read(cand)
                    page_version = str(m.get("ontology_version", ""))
                except Exception:
                    page_version = None
                if page_version is not None and page_version != new_version:
                    errs.append(f"온톨로지 버전 불일치: pages.json ontology_draft_version {new_version!r} != {od_rel} ontology_version {page_version!r}")
        return errs

    def step2_frontmatter(self) -> None:
        errs = []
        for pg in self.pages.get("pages", []):
            rel = self.page_rel(pg)
            text = self.page_src(pg).read_text(encoding="utf-8")
            if "{{" in text:
                errs.append(f"{rel}: 템플릿 자리 표시({{{{ }}}})가 남아 있다")
            try:
                meta, body = fm.parse(text)
            except Exception as e:
                errs.append(f"{rel}: 프런트매터 파싱 실패: {e}")
                continue
            if not text.startswith("---\n"):
                errs.append(f"{rel}: 프런트매터 없음")
            for e in fm.validate(meta, rel):
                errs.append(f"{rel}: {e}")
            first = next((l for l in body.split("\n") if l.strip()), "")
            if not (first.startswith("홈") or first.startswith("[홈](")):
                errs.append(f"{rel}: 본문 첫 줄이 이동 경로('홈 › …')가 아님")
            exists = self.page_dst(pg).is_file()
            if pg.get("action") == "create" and exists:
                errs.append(f"{rel}: action create 인데 docs 에 이미 있다")
            if pg.get("action") == "update" and not exists:
                errs.append(f"{rel}: action update 인데 docs 에 없다")
            if pg.get("status") not in ("draft", "needs_update", "deprecated", "verified", "published"):
                errs.append(f"{rel}: pages.json status 값 {pg.get('status')!r}")
        errs += self._preapply_checks()
        if errs:
            raise PublishError("2단계 프런트매터 검증 실패:\n" + "\n".join(f"  - {e}" for e in errs[:40]))
        self.info(f"2단계 프런트매터 검증 통과 (페이지 {len(self.pages.get('pages', []))}개, 반영 전 사전 검사 포함)")

    # --- 스냅숏·복사·원복 ------------------------------------------------------------------
    def snapshot(self) -> None:
        if self.snapshotted:
            return
        if self.backup.exists():
            shutil.rmtree(self.backup)
        for item in SNAPSHOT_ITEMS:
            src = ROOT / item
            dst = self.backup / item
            if src.is_dir():
                shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__"))
            elif src.is_file():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
        self.snapshotted = True
        self.info(f"스냅숏 저장: {self.backup.relative_to(ROOT)} ({', '.join(SNAPSHOT_ITEMS)})")

    @staticmethod
    def _copy_back(backup_dir: Path, items: list[str]) -> None:
        for item in items:
            src = backup_dir / item
            dst = ROOT / item
            if src.is_dir():
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
            elif src.is_file():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)

    def restore(self, why: str) -> None:
        """스냅숏(runs/<run_id>/backup/)으로 docs/data/config/tracks/mkdocs.yml/inbox/corrections.md 를 되돌린다.
        스냅숏은 실행 직전 상태(사용자가 커밋하지 않은 inbox/corrections.md·config/tracks 수정 포함)를 보존하므로
        git checkout 은 쓰지 않는다(HEAD 로 덮어쓰면 사용자의 미커밋 입력을 잃는다; 커밋은 7단계이므로 그 전에는 되돌릴 커밋도 없다).
        한 번 되돌린 뒤에는 다시 부르지 않는다(멱등)."""
        if not self.snapshotted or self.restored:
            return
        if not self.backup.exists():
            self.info(f"원복 불가: {why} — 스냅숏 {self.backup.relative_to(ROOT)} 이 없다(커밋 단계에서 이미 지웠다)")
            return
        self._copy_back(self.backup, SNAPSHOT_ITEMS)
        self.restored = True
        self.info(f"원복: {why} — docs/data/config/tracks/mkdocs.yml/inbox/corrections.md 를 스냅숏으로 되돌렸다")

    def copy_pages(self) -> None:
        for pg in self.pages.get("pages", []):
            dst = self.page_dst(pg)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(self.page_src(pg), dst)
            self.copied.append(dst)

    def drop_backup(self) -> None:
        if self.backup.exists():
            shutil.rmtree(self.backup, ignore_errors=True)

    # --- 3·4. 원문 보호·링크 검사 ---------------------------------------------------------------
    def step3_protect(self) -> None:
        self.snapshot()
        self.copy_pages()
        code, out = _run_check("protect_source.py", "--skip-nav")
        if code != 0:
            self.restore("3단계 원문 보호 검사 실패")
            raise PublishError("3단계 원문 보호 검사 실패:\n" + out[-4000:])
        self.info("3단계 원문 보호 검사 통과 (protect_source.py --skip-nav)")

    def step4_links(self) -> None:
        code, out = _run_check("check_links.py")
        if code != 0:
            self.restore("4단계 링크·각주 검사 실패")
            raise PublishError("4단계 내부 링크·각주 검사 실패:\n" + out[-4000:])
        code, out2 = _run_check("check_frontmatter.py")
        if code != 0:
            self.restore("4단계 프런트매터 검사 실패")
            raise PublishError("4단계 프런트매터·이동 경로 검사(docs 전체) 실패:\n" + out2[-4000:])
        self.info("4단계 내부 링크·각주 검사 통과 (check_links.py, check_frontmatter.py)")

    # --- 5. 반영 ------------------------------------------------------------------------------
    def _finalize_page_meta(self, pg: dict) -> None:
        dst = self.page_dst(pg)
        meta, body = fm.read(dst)
        old_meta = {}
        old = self.backup / "docs" / self.page_rel(pg)
        if old.is_file():
            try:
                old_meta, _ = fm.read(old)
            except Exception:
                old_meta = {}
        status = pg.get("status") or meta.get("status")
        if status in ("needs_update", "deprecated"):
            meta["status"] = status
        else:
            meta["status"] = "published"
        meta["updated"] = self.date
        if "last_run" in meta or meta.get("type") in ("area", "topic", "track", "track-stage", "ontology-draft"):
            meta["last_run"] = self.date
        if not meta.get("created"):
            meta["created"] = self.date
        try:
            old_v = int(old_meta.get("version") or 0)
        except (TypeError, ValueError):
            old_v = 0
        try:
            new_v = int(meta.get("version") or 0)
        except (TypeError, ValueError):
            new_v = 0
        if pg.get("action") == "update" and new_v <= old_v:
            meta["version"] = old_v + 1
            self.notes.append(f"{self.page_rel(pg)}: version 을 {old_v + 1} 로 올렸다(초안 {new_v})")
        elif new_v < 1:
            meta["version"] = 1
        # 2차 검증이 확정한 신뢰도를 신뢰도 필드가 있는 페이지에 적는다(6.2 "confidence 는 여기서 확정") [가정]
        if "confidence" in meta and self.v2.get("confidence"):
            meta["confidence"] = self.v2["confidence"]
        # 주제 페이지 9. 검증 노트: "2차 대기" → 2차 판정, "검증자 주의" → 2차 검증 노트 (storyteller.md 6절·verifier.md 11절 요청) [가정]
        if meta.get("type") == "topic":
            body = body.replace("/ 2차 대기", f"/ 2차 {self.v2.get('verdict')}")
            if self.v2.get("verification_note"):
                body = re.sub(r"^(- 검증자 주의:).*$", lambda m: f"{m.group(1)} {self.v2['verification_note']}", body, count=1, flags=re.M)
        if meta.get("status") == "deprecated" and not meta.get("replaced_by"):
            raise PublishError(f"{self.page_rel(pg)}: deprecated 페이지에 replaced_by 가 없다")
        fm.write(dst, meta, body)
        action = pg.get("action")
        if meta["status"] == "deprecated":
            self.counts["deprecate"] += 1
        elif action == "create":
            self.counts["create"] += 1
        else:
            self.counts["update"] += 1

    def _glossary_pages(self) -> list[tuple[str, dict]]:
        """docs/glossary/*.md (색인 제외) 의 (slug, 프런트매터) 목록."""
        out = []
        for p in sorted((paths.DOCS / "glossary").glob("*.md")):
            if p.name == "index.md":
                continue
            try:
                meta, _ = fm.read(p)
            except Exception:
                continue
            if meta.get("subtype") == "index":
                continue
            out.append((p.stem, meta))
        return out

    def _glossary_index_terms(self) -> list[tuple[str, str, str]]:
        """docs/glossary/index.md 의 용어 목록 표에서 (slug, 용어 한글, 용어 영문). 색인은 페이지에서 자동 생성되지만,
        시드 색인이 손으로 쓰인 경우에 대비해 색인의 용어명도 중복 검사에 넣는다."""
        p = paths.DOCS / "glossary" / "index.md"
        if not p.is_file():
            return []
        out = []
        for line in p.read_text(encoding="utf-8").split("\n"):
            m = re.match(r"^\|\s*\[([^\]]+)\]\(([a-z0-9-]+)\.md\)\s*\|\s*([^|]*)\|", line)
            if m:
                out.append((m.group(2), m.group(1).strip(), m.group(3).strip()))
        return out

    def _find_glossary_page(self, g: dict) -> str | None:
        """같은 용어의 기존 페이지 slug 를 찾는다. slug 일치 → 프런트매터 term_ko·term_en(대소문자·공백·괄호 약어 무시) 일치
        → 색인 표의 용어명 일치 순. 없으면 None (그때만 새 파일을 만든다)."""
        pages = self._glossary_pages()
        slugs = {s for s, _ in pages}
        if g.get("slug") and g["slug"] in slugs:
            return g["slug"]
        keys = _term_keys(g.get("term_ko"), g.get("term_en"))
        if not keys:
            return None
        for slug, meta in pages:
            if keys & _term_keys(meta.get("term_ko"), meta.get("term_en"), meta.get("title")):
                return slug
        for slug, ko, en in self._glossary_index_terms():
            if keys & _term_keys(ko, en):
                return slug
        return None

    def _apply_glossary(self) -> None:
        for g in self.pages.get("glossary_updates") or []:
            existing_slug = self._find_glossary_page(g)
            if existing_slug and existing_slug != g.get("slug"):
                self.notes.append(f"용어집 '{g.get('term_ko')}' ({g.get('term_en')}) 은 기존 페이지 glossary/{existing_slug}.md 와 같은 용어로 보고 갱신했다(중복 생성 방지)")
            slug = existing_slug or g.get("slug") or _slugify(g.get("term_en")) or _slugify(g.get("term_ko")) or f"term-{len(list((paths.DOCS / 'glossary').glob('*.md')))}"
            dst = paths.DOCS / "glossary" / f"{slug}.md"
            rel = f"glossary/{slug}.md"
            existed = dst.is_file()
            sources = [s for s in (g.get("sources") or []) if re.match(r"^ref-\d{3}$", str(s))]
            refs = []
            for s in sources:
                r = self._ref_data(s)
                if r:
                    refs.append(r)
            tag = "[사실]" if refs else "[추정]"
            foot = "".join(f"[^{r['id']}]" for r in refs)
            one_line = f"{g['definition']} {tag}{foot}"
            related = [int(x) for x in (g.get("related_areas") or []) if str(x).isdigit()]
            area_lines = "\n".join(f"- [{self.src.area(n).title}]({paths.rel_link(rel, paths.area_rel_path(n))})" for n in related) or "- 아직 없음"
            foot_lines = "\n".join(_footnote_line(r) for r in refs)
            ref_links = ", ".join("[{0}]({1})".format(r["id"], paths.rel_link(rel, "references/" + r["id"] + ".md")) for r in refs)
            src_section = (foot_lines + ("\n\n- 참고문헌 페이지: " + ref_links if ref_links else "")) if refs else "출처 미기재(리서치 브리프의 용어 후보이며 정의를 뒷받침하는 참고문헌 id 가 없어 [추정]으로 둔다)."
            if dst.is_file():
                meta, body = fm.read(dst)
                meta.update({"definition": g["definition"], "updated": self.date, "version": int(meta.get("version") or 0) + 1,
                             "status": "published"})
                if related:
                    meta["related_areas"] = sorted(set([int(x) for x in (meta.get("related_areas") or []) if str(x).isdigit()] + related))
                if sources:
                    meta["sources"] = sorted(set([str(x) for x in (meta.get("sources") or [])] + sources))
                if self.v2.get("confidence"):
                    meta["confidence"] = self.v2["confidence"]
                secs = runs.split_sections(body)
                new_secs = []
                for h, txt in secs:
                    if h == "한 줄 정의":
                        txt = one_line
                    elif h == "설명" and g.get("description"):
                        txt = g["description"]
                    elif h == "출처" and refs:
                        existing = txt
                        for line in foot_lines.split("\n"):
                            if line and line.split(":")[0] not in existing:
                                existing += ("\n" if existing else "") + line
                        txt = existing
                    new_secs.append((h, txt))
                body = "\n\n".join(([new_secs[0][1]] if new_secs[0][1] else []) + [f"## {h}\n\n{t}" for h, t in new_secs[1:]]) + "\n"
                fm.write(dst, meta, body)
                self.notes.append(f"용어집 갱신: {rel}")
            else:
                meta = {"title": f"{g['term_ko']} ({g['term_en']})", "type": "glossary", "term_ko": g["term_ko"], "term_en": g["term_en"],
                        "definition": g["definition"], "related_areas": related, "tags": [], "status": "published"}
                if self.v2.get("confidence"):
                    meta["confidence"] = self.v2["confidence"]
                meta.update({"created": self.date, "updated": self.date, "sources": sources, "version": 1})
                abbr = "없음"
                m = re.search(r"\(([A-Za-z0-9 .-]+)\)\s*$", g["term_en"])
                if m:
                    abbr = f"{m.group(1)} — {g['term_en'][:m.start()].strip()}"
                body = "\n".join([
                    f"[홈](../index.md) › [용어집](index.md) › {g['term_ko']}", "",
                    f"# {g['term_ko']} ({g['term_en']})", "",
                    "## 용어", "", "| 한글 | 영문 | 약어와 풀어 쓴 이름 |", "|---|---|---|",
                    f"| {g['term_ko']} | {g['term_en']} | {abbr} |", "",
                    "## 한 줄 정의", "", one_line, "",
                    "## 설명", "", g.get("description") or "아직 작성되지 않음", "",
                    "## 관련 영역", "", area_lines, "",
                    "## 출처", "", src_section, "",
                ])
                fm.write(dst, meta, body)
                self.notes.append(f"용어집 생성: {rel}")
            self.counts["glossary"] += 1
            self._changelog_item("갱신" if existed else "생성", f"docs/{rel}", f"용어집 항목 {g['term_ko']}")

    def _ref_data(self, ref_id: str) -> dict | None:
        for r in (self.pages.get("reference_updates") or []) + (self.research.get("sources") or []):
            if r.get("id") == ref_id:
                return r
        return _ref_from_page(ref_id)

    def _apply_references(self) -> None:
        for r in self.pages.get("reference_updates") or []:
            rid = r["id"]
            dst = paths.DOCS / "references" / f"{rid}.md"
            if dst.is_file():
                meta, _ = fm.read(dst)
                same = (str(meta.get("url", "")).rstrip("/") == str(r.get("url", "")).rstrip("/"))
                if not same:
                    raise PublishError(f"참고문헌 id 충돌: {rid} 는 이미 다른 출처({meta.get('url')})에 쓰였다. 브리프의 출처 id 를 다음 번호로 다시 부여해야 한다")
                continue  # 기존 참고문헌: 인용된 페이지 목록은 auto 영역이 다시 만든다
            rel = f"references/{rid}.md"
            pub = r.get("published")
            pub_s = str(pub) if pub not in (None, "") else "미확인"
            unopened = bool(r.get("source_unopened"))
            meta = {"title": f"{rid} — {r['title']}", "type": "reference", "ref_id": rid, "ref_title": r["title"], "org": r["org"],
                    "published": pub_s, "url": r["url"], "source_type": r["type"], "reliability": r["reliability"],
                    "url_verified": not unopened, "accessed": r["accessed"], "related_areas": [], "tags": [],
                    "status": "published", "created": self.date, "updated": self.date, "version": 1}
            note = ("원문 미열람(페이지 열람이 차단된 환경에서 검색 결과의 기관·제목·URL 일치로 실재를 확인했다). 신뢰도는 medium 이 상한이다."
                    if unopened else "내용 검증 에이전트가 출처 실재성과 주장 뒷받침 여부를 확인했다.")
            body = "\n".join([
                f"[홈](../index.md) › [참고문헌](index.md) › {rid}", "",
                f"# {rid} — {r['title']}", "",
                "## 서지 정보", "", "| 항목 | 값 |", "|---|---|",
                f"| id | {rid} |", f"| 기관 | {r['org']} |", f"| 제목 | {r['title']} |", f"| 발행일 | {pub_s} |",
                f"| URL | <{r['url']}> |", f"| 유형 | {r['type']} |", f"| 신뢰도 | {r['reliability']} |",
                f"| 원문 열람 | {'미확인 — 원문 미열람' if unopened else '확인'} |", f"| 접근일 | {r['accessed']}{' (원문 미열람)' if unopened else ''} |", "",
                "## 요약", "", r.get("summary", ""), "", f"등록 실행: {self.run_id} · 검증: 1차 {self.v1.get('verdict')} / 2차 {self.v2.get('verdict')}", "",
                "## 인용된 페이지", "",
                f"이 출처를 프런트매터 `sources` 또는 각주 `[^{rid}]` 로 인용했거나 이 페이지로 링크한 페이지의 목록이다. 퍼블리셔가 docs 전체를 스캔해 자동으로 갱신한다.", "",
                ar.wrap("reference-cited-pages", "- 아직 없음"), "",
                "## 각주 형식", "", "이 출처를 인용할 때 쓰는 각주 정의는 다음과 같다.", "", "```", _footnote_line({**r, "id": rid}), "```", "",
                "## 비고", "", note, "",
            ])
            fm.write(dst, meta, body)
            self.counts["references"] += 1
            self._changelog_item("생성", f"docs/{rel}", f"참고문헌 {rid} 등록: {_short(r['title'], 60)}")
            self.notes.append(f"참고문헌 생성: {rel}")

    def _apply_standards(self) -> None:
        items = self.pages.get("standards_updates") or []
        if not items:
            return
        p = paths.DATA / "standards.json"
        data = runs.read_json(p, {"items": []}) or {"items": []}
        for s in items:
            row = {"name": s["name"], "org": s["org"], "kind": s["kind"], "related_areas": s["related_areas"], "url": s["url"],
                   "summary": s.get("summary", ""), "ref_id": s.get("ref_id"), "run_id": self.run_id, "date": self.date}
            existing = next((it for it in data["items"] if it.get("name") == s["name"]), None)
            if existing:
                existing.update(row)
            else:
                data["items"].append(row)
            self.counts["standards"] += 1
        runs.write_json(p, data)
        self._changelog_item("갱신", "docs/standards/index.md", f"표준·프레임워크 {self.counts['standards']}건 추가·갱신")

    def _apply_open_questions(self) -> None:
        items = self.pages.get("open_question_updates") or []
        if not items:
            return
        p = paths.DATA / "open_questions.json"
        data = runs.read_json(p, {"items": []}) or {"items": []}
        rows = data.setdefault("items", [])

        def next_id():
            nums = [int(m.group(1)) for q in rows for m in [re.match(r"^oq-(\d+)$", str(q.get("id", "")))] if m]
            return f"oq-{(max(nums) + 1) if nums else 1:03d}"
        for u in items:
            if u.get("action") == "update" and u.get("id"):
                row = next((q for q in rows if q.get("id") == u["id"]), None)
                if row is None:
                    self.notes.append(f"열린 질문 {u['id']} 가 없어 새 항목으로 등록했다")
                    row = {"id": next_id(), "raised": self.date, "run_id": self.run_id}
                    rows.append(row)
                row.update({"question": u["question"], "areas": u["areas"], "status": u["status"], "link": u.get("link")})
                if u["status"] == "해결":
                    row["resolved_run_id"] = self.run_id
            else:
                dup = next((q for q in rows if str(q.get("question", "")).strip() == str(u["question"]).strip()), None)
                if dup:
                    dup.update({"status": u["status"], "link": u.get("link") or dup.get("link"), "areas": u["areas"]})
                    self.notes.append(f"열린 질문 중복(같은 문장)으로 {dup['id']} 를 갱신했다")
                    continue
                rows.append({"id": next_id(), "question": u["question"], "areas": u["areas"], "raised": self.date,
                             "run_id": self.run_id, "status": u["status"], "link": u.get("link")})
            self.counts["open_questions"] += 1
        runs.write_json(p, data)

    def _apply_flow_matrix(self) -> None:
        items = self.pages.get("flow_matrix_updates") or []
        if not items:
            return
        p = paths.DATA / "flow_matrix.json"
        data = runs.read_json(p, {}) or {}
        data.setdefault("steps", paths.FLOW_STEPS)
        data.setdefault("items", paths.FLOW_ITEMS)
        cells = data.setdefault("cells", {})
        for u in items:
            key = f"{u['step']}|{u['item']}"
            entries = cells.setdefault(key, [])
            title = u.get("title") or self._title_of(u["link"])
            hit = next((e for e in entries if e.get("link") == u["link"]), None)
            if hit:
                hit.update({"title": title, "run_id": self.run_id})
            else:
                entries.append({"link": u["link"], "title": title, "run_id": self.run_id})
            self.counts["flow_cells"] += 1
        runs.write_json(p, data)

    def _title_of(self, link: str) -> str:
        rel = paths.docs_rel(str(link).split("#")[0])
        p = paths.DOCS / rel
        if p.is_file():
            try:
                meta, _ = fm.read(p)
                return str(meta.get("title") or rel)
            except Exception:
                pass
        return rel

    def _changelog_item(self, action: str, page: str, summary: str) -> None:
        self._changelog_rows.append({"date": self.date, "run_id": self.run_id, "action": action, "page": page, "summary": summary})

    def _apply_changelog(self) -> None:
        p = paths.DATA / "changelog.json"
        data = runs.read_json(p, {"items": []}) or {"items": []}
        rows = data.setdefault("items", [])
        page_rows = []
        for pg in self.pages.get("pages", []):
            action = "폐기" if pg.get("status") == "deprecated" else ("생성" if pg.get("action") == "create" else "갱신")
            page_rows.append({"date": self.date, "run_id": self.run_id, "action": action, "page": pg["path"], "summary": pg.get("diff_summary", "")})
        entry = self.pages.get("changelog_entry", "")
        parts = [x.strip() for x in entry.split("|")]
        summary = f"{parts[1]}: {parts[2]}" if len(parts) >= 4 else entry
        primary = self.pages["pages"][0]["path"] if self.pages.get("pages") else "docs/"
        rows.extend(page_rows)
        rows.append({"date": self.date, "run_id": self.run_id, "action": "요약", "page": primary, "summary": summary})
        rows.extend(self._changelog_rows)
        runs.write_json(p, data)

    def _apply_corrections(self) -> None:
        ids = list(dict.fromkeys((self.v1.get("corrections_applied") or []) + (self.v2.get("corrections_applied") or [])))
        if not ids:
            return
        text = runs.read_text(runs.INBOX_CORRECTIONS, "")
        known = {c["id"]: c for c in runs.parse_corrections(text)}
        fixes = "; ".join((self.pages.get("fixes_applied") or [])[:3])
        for cid in ids:
            c = known.get(cid)
            if not c:
                self.notes.append(f"정정 요청 {cid} 가 inbox/corrections.md 에 없다")
                continue
            memo = _short(fixes or self.v1.get("verification_note", ""), 160) or "반영"
            text = runs.update_correction_block(text, cid, "applied", self.run_id, memo)
            self._changelog_item("정정", c["page"] or primary_page(self.pages), f"정정 요청 {cid} 반영")
            self.counts["corrections"] += 1
        runs.write_text(runs.INBOX_CORRECTIONS, text)

    # --- 트랙 ---------------------------------------------------------------------------
    def _apply_track(self) -> None:
        tu = self.pages.get("track_updates") or {}
        slug = self.track["slug"]
        stage = int(self.track.get("stage") or 1)
        cfg = self.track_cfg or {}
        bp = paths.track_backlog(slug)
        data = runs.read_json(bp, {"items": []}) or {"items": []}
        items = data.setdefault("items", [])
        by_id = {b.get("id"): b for b in items}
        texts = {str(b.get("question", "")).strip(): b for b in items}

        def next_qid(st: int) -> str:
            nums = [int(b["id"].split("-")[1]) for b in items if re.match(rf"^q{st}-\d{{2}}$", str(b.get("id", "")))]
            return f"q{st}-{(max(nums) + 1) if nums else 1:02d}"

        # (0) priority.yaml 의 track_questions 를 제기 근거 "사용자"로 등록 (8.2)
        for q in runs.load_priority().get("track_questions", []):
            if str(q.get("track", "")) != slug or not q.get("question"):
                continue
            t = str(q["question"]).strip()
            if t in texts or (q.get("id") and q["id"] in by_id):
                continue
            try:
                st = int(q.get("stage") or stage)
            except (TypeError, ValueError):
                st = stage
            row = {"id": next_qid(st), "question": t, "stage": st, "origin": "사용자", "status": "열림",
                   "answered_run_id": None, "answer_link": None, "created": self.date, "origin_run_id": None,
                   "priority": q.get("priority") or "normal"}
            items.append(row); by_id[row["id"]] = row; texts[t] = row
            self.counts["backlog"] += 1
            self.notes.append(f"사용자 지정 트랙 질문 등록: {row['id']}")
        # (1) backlog_updates
        for u in tu.get("backlog_updates") or []:
            row = by_id.get(u["id"])
            if row is None and u.get("question") and str(u["question"]).strip() in texts:
                row = texts[str(u["question"]).strip()]
                self.notes.append(f"백로그 {u['id']} 는 같은 문장의 {row['id']} 로 처리했다")
            if row is None:
                if not (u.get("question") and u.get("stage")):
                    self.notes.append(f"백로그 {u['id']} 가 없고 새 질문 정보(question·stage)도 없어 건너뛴다")
                    continue
                qid = u["id"] if not re.match(r"^q\d+-\d{2}$", u["id"]) or u["id"] not in by_id else next_qid(int(u["stage"]))
                if int(u["stage"]) != int(qid.split("-")[0][1:]):
                    qid = next_qid(int(u["stage"]))
                row = {"id": qid, "question": u["question"], "stage": int(u["stage"]), "origin": u.get("origin") or "사용자",
                       "status": u["status"], "answered_run_id": None, "answer_link": u.get("answer_link"),
                       "created": self.date, "origin_run_id": self.run_id}
                items.append(row); by_id[qid] = row; texts[str(u["question"]).strip()] = row
            else:
                row["status"] = u["status"]
                if u.get("answer_link"):
                    row["answer_link"] = u["answer_link"]
                if u["status"] == "답함" and not row.get("answered_run_id"):
                    row["answered_run_id"] = self.run_id
            self.counts["backlog"] += 1
        # (2) research.track.new_questions 가운데 검증 통과분(중복·단계 태그 문제 제외, 위에서 아직 안 넣은 것)
        tc1 = self.v1.get("track_checks") or {}
        tc2 = self.v2.get("track_checks") or {}
        dup_texts = {str(x).strip() for x in (tc1.get("backlog_duplicates") or []) + (tc2.get("backlog_duplicates") or [])}
        tag_issue = {str(x).strip() for x in (tc1.get("stage_tag_issues") or []) + (tc2.get("stage_tag_issues") or [])}
        for nq in (self.research.get("track") or {}).get("new_questions") or []:
            t = str(nq.get("question", "")).strip()
            if not t or t in texts:
                continue
            if any(t in d or d in t for d in dup_texts) or any(t in s or s in t for s in tag_issue):
                self.notes.append(f"새 질문 제외(검증 판정): {_short(t, 60)}")
                continue
            st = int(nq.get("stage") or stage)
            qid = nq.get("id") if nq.get("id") and nq["id"] not in by_id and nq["id"].startswith(f"q{st}-") else next_qid(st)
            row = {"id": qid, "question": t, "stage": st, "origin": nq.get("rationale_finding_id") or "사용자", "status": "열림",
                   "answered_run_id": None, "answer_link": None, "created": self.date, "origin_run_id": self.run_id}
            items.append(row); by_id[qid] = row; texts[t] = row
            self.counts["backlog"] += 1
        runs.write_json(bp, data)
        self._changelog_item("갱신", f"docs/tracks/{slug}/question-backlog.md", f"백로그 항목 {self.counts['backlog']}건 갱신")

        # (3) 온톨로지 버전: pages.json 의 ontology_draft_version 과 페이지 프런트매터 ontology_version 대조, 버전 이력 추가
        od_rel = f"tracks/{slug}/ontology-draft.md"
        od_page = paths.DOCS / od_rel
        new_version = str(tu.get("ontology_draft_version", ""))
        page_version = None
        if od_page.is_file():
            m, _ = fm.read(od_page)
            page_version = str(m.get("ontology_version", ""))
        if page_version is not None and new_version and page_version != new_version:
            raise PublishError(f"온톨로지 버전 불일치: pages.json ontology_draft_version {new_version!r} != {od_rel} ontology_version {page_version!r}")
        old_version = None
        old_od = self.backup / "docs" / od_rel
        if old_od.is_file():
            m, _ = fm.read(old_od)
            old_version = str(m.get("ontology_version", ""))
        if new_version and old_version is not None and new_version != old_version:
            vp = paths.DATA / "tracks" / slug / "ontology_versions.json"
            vdata = runs.read_json(vp, {"items": []}) or {"items": []}
            changes = _log_segment(tu.get("log_entry", ""), "온톨로지 변경") or f"v{old_version} → v{new_version}"
            vdata.setdefault("items", []).append({"version": new_version, "date": self.date, "changes": changes, "run_id": self.run_id})
            runs.write_json(vp, vdata)
            self.notes.append(f"온톨로지 초안 버전 v{old_version} → v{new_version} (버전 이력 추가)")
        # (4) 세부영역 반영 제안 누적
        arp = self.pages.get("area_reflection_proposals") or []
        if arp:
            ap_path = paths.DATA / "area_reflection_proposals.json"
            adata = runs.read_json(ap_path, {"items": []}) or {"items": []}
            for a in arp:
                adata.setdefault("items", []).append({"run_id": self.run_id, "date": self.date, "track": slug, "stage": stage,
                                                      "area_no": a["area_no"], "section": a["section"], "summary": a["summary"], "status": "제안"})
            runs.write_json(ap_path, adata)
        # (5) 단계 전환 (2차 검증의 stage_transition_approved 가 최종; 없으면 1차)
        st = tu.get("stage_transition")
        approved = tc2.get("stage_transition_approved") if "stage_transition_approved" in tc2 else tc1.get("stage_transition_approved")
        self.stage_transition_done = False
        if st and approved is True:
            self._transition_stage(slug, stage, int(st["to_stage"]), int(cfg.get("stages") or 7), st.get("reason", ""))
        elif st and not approved:
            self.notes.append("stage_transition 이 있으나 검증이 단계 전환을 승인하지 않아 반영하지 않았다")
        # (6) 트랙 로그
        self._append_track_log(slug, stage, tu, tc1, tc2, old_version, new_version)

    def _transition_stage(self, slug: str, from_stage: int, to_stage: int, stages: int, reason: str) -> None:
        p = paths.track_config(slug)
        text = p.read_text(encoding="utf-8")
        cur = yaml_load_safe(text)
        done = to_stage > stages
        new_stage = min(to_stage, stages)
        text = re.sub(r"^(current_stage:\s*)\d+", lambda m: f"{m.group(1)}{new_stage}", text, count=1, flags=re.M)
        if done:
            text = re.sub(r"^(status:\s*)\S+", lambda m: f"{m.group(1)}done", text, count=1, flags=re.M)
        status_map = {int(k): v for k, v in ((cur.get("stage_status") or {}).items())} if isinstance(cur.get("stage_status"), dict) else {}
        comp_map = {int(k): v for k, v in ((cur.get("stage_completion") or {}).items())} if isinstance(cur.get("stage_completion"), dict) else {}
        status_map[from_stage] = "완료"
        comp_map[from_stage] = True
        if not done:
            status_map[new_stage] = "진행 중"
        block = ("# --- 퍼블리셔 기록(자동 갱신, 단계 전환 시) — 시작 ---\n"
                 f"stage_status: {{{', '.join(f'{k}: {v}' for k, v in sorted(status_map.items()))}}}\n"
                 f"stage_completion: {{{', '.join(f'{k}: {str(v).lower()}' for k, v in sorted(comp_map.items()))}}}\n"
                 "# --- 퍼블리셔 기록 끝 ---\n")
        pat = re.compile(r"# --- 퍼블리셔 기록\(자동 갱신, 단계 전환 시\) — 시작 ---\n.*?# --- 퍼블리셔 기록 끝 ---\n", re.S)
        text = pat.sub(lambda m: block, text) if pat.search(text) else text.rstrip("\n") + "\n\n" + block
        p.write_text(text, encoding="utf-8")
        self.stage_transition_done = True
        self.notes.append(f"단계 전환: 단계 {from_stage} → {'done' if done else f'단계 {new_stage}'} ({reason}) — config/tracks/{slug}.yaml 갱신")
        self._changelog_item("갱신", f"docs/tracks/{slug}/index.md", f"단계 {from_stage} 완료, {'트랙 done' if done else f'단계 {new_stage} 로 전환'}")

    def _append_track_log(self, slug, stage, tu, tc1, tc2, old_version, new_version) -> None:
        cfg = self.track_cfg or {}
        names = cfg.get("stage_names") or {}
        stage_name = names.get(stage) or names.get(str(stage)) or ""
        stage_pages = cfg.get("stage_pages") or {}
        stage_file = stage_pages.get(stage) or stage_pages.get(str(stage)) or Path(tu.get("stage_page", "")).name
        backlog = load_backlog(slug)
        by_id = {b["id"]: b for b in backlog}
        tr = self.research.get("track") or {}
        answered = tr.get("answered_question_ids") or []
        ans_cells = []
        for q in answered:
            b = by_id.get(q, {})
            link = b.get("answer_link")
            a = f"{q} — {_short(b.get('question', ''), 60)}"
            if link:
                a += f" ([답]({paths.rel_link(f'tracks/{slug}/log.md', paths.docs_rel(link.split('#')[0]))}{'#' + link.split('#', 1)[1] if '#' in link else ''}))"
            ans_cells.append(a)
        answered_cell = "; ".join(ans_cells) if ans_cells else "없음(" + (_log_segment(self.research.get("self_check", {}).get("limits", ""), "답한 질문 없음") or "이유 미기재") + ")"
        new_ids = [b["id"] for b in backlog if b.get("origin_run_id") == self.run_id]
        new_cell = "; ".join(f"{b['id']} — {_short(b.get('question', ''), 60)} (단계 {b.get('stage')}. {names.get(b.get('stage')) or names.get(str(b.get('stage'))) or ''}, 근거 {b.get('origin')})"
                            for b in backlog if b["id"] in new_ids) or ("없음(" + (_log_segment(self.research.get("self_check", {}).get("limits", ""), "후속 질문 없음") or "이유 미기재") + ")")
        onto_seg = _log_segment(tu.get("log_entry", ""), "온톨로지 변경")
        if new_version and old_version is not None and new_version != old_version:
            onto_cell = f"v{old_version} → v{new_version}: {onto_seg or '변경 내용은 온톨로지 초안 페이지 참고'} · 검증 승인: {'예' if (tc2.get('ontology_changes_grounded', tc1.get('ontology_changes_grounded'))) else '미상'}"
        elif not onto_seg or onto_seg.startswith(("없음", "변경 없음")):
            onto_cell = f"변경 없음({onto_seg or '승인·반영된 변경 없음'})" if onto_seg else "변경 없음(승인·반영된 변경 없음)"
        else:
            onto_cell = f"버전 변경 없음(v{new_version or old_version}; 승인·반영된 변경 없음. 로그 항목의 제안: {onto_seg})"
        sa = tr.get("stage_completion_self_assessment") or {}
        comp_cell = (f"자체 평가: {'충족' if sa.get('met') else '미충족' + ('(' + ', '.join(sa.get('missing') or []) + ')' if sa.get('missing') else '')}"
                     f" · 검증 판정: {'충족' if tc2.get('stage_complete', tc1.get('stage_complete')) else '미충족'}"
                     f" · 단계 전환: {'예' if getattr(self, 'stage_transition_done', False) else '아니오'}")
        arp = self.pages.get("area_reflection_proposals") or []
        arp_cell = "; ".join(f"{self.src.area(a['area_no']).title} — {a['section']}: {_short(a['summary'], 80)}" for a in arp) or "없음"
        next_cell = _log_segment(tu.get("log_entry", ""), "다음 실행") or _log_segment(tu.get("log_entry", ""), "다음 실행 제안") or "다음 트랙 실행에서 현재 단계의 열린 질문을 오래된 순으로 고른다"
        daily_link = f"../../logs/daily/{self.date}.md"
        entry = {
            "run_id": self.run_id, "date": self.date, "stage": stage, "stage_name": stage_name, "stage_page": stage_file,
            "daily_log": daily_link, "run_id_cell": f"{self.run_id} ([일일 로그]({daily_link}))",
            "stage_cell": f"[단계 {stage}. {stage_name}]({stage_file}) — 트랙 상태 {cfg.get('status', 'active')}, 현재 단계 {stage}",
            "answered_questions": answered_cell, "new_questions": new_cell, "ontology_change": onto_cell,
            "completion_assessment": comp_cell, "area_reflection_proposals": arp_cell, "next_run_proposal": next_cell,
            "log_entry": tu.get("log_entry", ""), "overview_progress": tu.get("overview_progress", ""),
        }
        lp = paths.DATA / "tracks" / slug / "log.json"
        ldata = runs.read_json(lp, {"items": []}) or {"items": []}
        ldata.setdefault("items", []).append(entry)
        runs.write_json(lp, ldata)
        block = "\n".join([
            f"### 실행 {self.run_id} — 단계 {stage}. {stage_name}", "",
            "| 항목 | 내용 |", "|---|---|",
            f"| 실행 id | {entry['run_id_cell']} |", f"| 단계 | {entry['stage_cell']} |",
            f"| 답한 질문 | {_esc(answered_cell)} |", f"| 새 질문 | {_esc(new_cell)} |", f"| 온톨로지 변경 | {_esc(onto_cell)} |",
            f"| 완료 조건 평가 | {_esc(comp_cell)} |", f"| 세부영역 반영 제안 | {_esc(arp_cell)} |", f"| 다음 실행 제안 | {_esc(next_cell)} |",
        ])
        page = paths.DOCS / "tracks" / slug / "log.md"
        if page.is_file():
            meta, body = fm.read(page)
            if "<!-- append-below -->" in body:
                body = body.replace("<!-- append-below -->", "<!-- append-below -->\n\n" + block + "\n", 1)
            elif ar.has_region(body, "track-log"):
                cur = ar.get_region(body, "track-log") or ""
                body = ar.replace_region(body, "track-log", block + ("\n\n" + cur if cur.strip() else ""))
            else:
                body = body.rstrip("\n") + "\n\n" + block + "\n"
            meta["updated"] = self.date
            meta["version"] = int(meta.get("version") or 0) + 1
            fm.write(page, meta, body)
            self._changelog_item("갱신", f"docs/tracks/{slug}/log.md", f"트랙 로그 항목 추가(단계 {stage})")

    # --- 5단계 본체 -------------------------------------------------------------------------
    def step5_apply(self) -> None:
        self._changelog_rows: list[dict] = []
        for pg in self.pages.get("pages", []):
            self._finalize_page_meta(pg)
        self._apply_references()
        self._apply_glossary()
        self._apply_standards()
        self._apply_open_questions()
        self._apply_flow_matrix()
        if self.track:
            self._apply_track()
        self._apply_corrections()
        self._apply_changelog()
        self.write_daily_log_and_summary(final=False)
        changed = refresh_all_auto_regions()
        write_mkdocs_yml()
        code, out = _run_check("protect_source.py")
        if code != 0:
            self.restore("5단계 반영 뒤 최종 원문 보호 검사 실패")
            raise PublishError("5단계 최종 원문 보호 검사(내비 포함) 실패:\n" + out[-4000:])
        code, out = _run_check("check_links.py")
        if code != 0:
            self.restore("5단계 반영 뒤 링크 검사 실패")
            raise PublishError("5단계 반영 뒤 링크·각주 검사 실패:\n" + out[-4000:])
        code, out = _run_check("check_frontmatter.py")
        if code != 0:
            self.restore("5단계 반영 뒤 프런트매터 검사 실패")
            raise PublishError("5단계 반영 뒤 프런트매터 검사 실패:\n" + out[-4000:])
        self.info(f"5단계 반영 완료: 페이지 생성 {self.counts['create']}/갱신 {self.counts['update']}/폐기 {self.counts['deprecate']}, "
                  f"용어 {self.counts['glossary']}, 참고문헌 {self.counts['references']}, 표준 {self.counts['standards']}, 열린 질문 {self.counts['open_questions']}, "
                  f"매트릭스 칸 {self.counts['flow_cells']}, 백로그 {self.counts['backlog']}, 정정 {self.counts['corrections']}; auto 영역 갱신 {len(changed)}개 페이지, mkdocs.yml 갱신")

    # --- 6. 빌드 ---------------------------------------------------------------------------
    def _build_cmd(self) -> str:
        return str(self.settings.get("site_build_cmd") or "mkdocs build --strict")

    def step6_build(self) -> None:
        if self.args.no_build:
            self.info("6단계 사이트 빌드 건너뜀(--no-build)")
            return
        cmd = self._build_cmd()
        t = time.time()
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=str(ROOT))
        out = (p.stdout or "") + (p.stderr or "")
        (self.rd / "build.log").write_text(out, encoding="utf-8")
        if p.returncode != 0:
            self.restore("6단계 사이트 빌드 실패")
            raise PublishError(f"6단계 사이트 빌드 실패(exit {p.returncode}, {runs.fmt_duration(time.time() - t)}): 롤백했다. 출력(runs/<run_id>/build.log):\n" + out[-3000:])
        self.built = True
        self.info(f"6단계 사이트 빌드 성공 ({shlex.quote(cmd)}, {runs.fmt_duration(time.time() - t)})")

    # --- 7. 커밋 ---------------------------------------------------------------------------
    def _git_paths(self) -> tuple[Path, list[str]]:
        repo = runs.repo_root(self.settings)
        rel = ROOT.resolve().relative_to(repo).as_posix()
        rel = "" if rel == "." else rel + "/"
        items = [f"{rel}docs", f"{rel}data", f"{rel}config", f"{rel}mkdocs.yml", f"{rel}inbox",
                 f"{rel}{self.rd.resolve().relative_to(ROOT.resolve()).as_posix()}"]
        return repo, items

    def commit_message(self) -> str:
        t = self.target.get("target") or {}
        name = t.get("area_name") or ""
        if self.run_type == "track" and self.track:
            name = f"{name} ({self.track.get('name') or self.track.get('slug')} 단계 {self.track.get('stage')})"
        if self.run_type == "weekly_review":
            name = f"주간 정리 {runs.iso_week(self.date)}"
        if self.run_type == "monthly_recheck" and not name:
            name = "월간 재검증"
        return f"run({self.date}): {self.run_type_label()} {name} — 생성 {self.counts['create']}/갱신 {self.counts['update'] + self.counts['deprecate']}"

    def _git(self, repo: Path, *args: str) -> subprocess.CompletedProcess:
        ident = []
        chk = subprocess.run(["git", "-C", str(repo), "config", "user.name"], capture_output=True, text=True)
        if not (chk.stdout or "").strip():
            ident = ["-c", "user.name=ROP 연구 위키 퍼블리셔", "-c", "user.email=rop-wiki@localhost"]
        return subprocess.run(["git", "-C", str(repo), *ident, *args], capture_output=True, text=True)

    def step7_commit(self, amend: bool = False) -> None:
        if self.args.no_commit or not self.settings.get("git_commit", True):
            self.info("7단계 커밋 건너뜀(git_commit false 또는 --no-commit)")
            return
        repo, items = self._git_paths()
        if not (repo / ".git").exists():
            self.notes.append(f"git 저장소가 아니어서 커밋하지 않았다: {repo}")
            self.info(f"7단계 커밋 건너뜀: git 저장소 아님 {repo}")
            return
        # 스냅숏은 runs/<run_id>/backup/ 에 있어 커밋에 들어가지 않도록 여기서 지운다. 이 뒤의 실패(git add·commit)는
        # 빌드까지 성공한 상태이므로 파일을 반영된 채 두고 실패로 기록한다(RUN.md 4절) [가정]
        self.drop_backup()
        existing = [i for i in items if (repo / i).exists()]
        add = self._git(repo, "add", "-A", "--", *existing)
        if add.returncode != 0:
            raise PublishError(f"7단계 git add 실패: {add.stderr[-800:]}")
        diff = self._git(repo, "diff", "--cached", "--quiet")
        if diff.returncode == 0 and not amend:
            self.info("7단계 커밋: 변경 없음(스테이지 비어 있음)")
            return
        args = ["commit", "-q", "-m", self.commit_message()]
        if amend:
            args = ["commit", "-q", "--amend", "--no-edit"]
        c = self._git(repo, *args)
        if c.returncode != 0:
            raise PublishError(f"7단계 git commit 실패: {(c.stderr or c.stdout)[-800:]}")
        h = self._git(repo, "rev-parse", "--short", "HEAD")
        self.commit_hash = (h.stdout or "").strip()
        self.committed = True
        self.info(f"7단계 커밋 {'수정(amend)' if amend else '완료'}: {self.commit_hash} — {self.commit_message()}")
        if self.settings.get("git_push"):
            p = self._git(repo, "push")
            if p.returncode != 0:
                self.notes.append(f"git push 실패: {(p.stderr or '')[-300:]}")
                self.info("git push 실패(로그 참고)")
            else:
                self.info("git push 완료")

    # --- 8·9. 일일 로그·요약·알림 ------------------------------------------------------------------
    def _retries(self, prefix: str) -> tuple[int, list[str]]:
        files = sorted(self.rd.glob(f"{prefix}.attempt*.json"))
        reasons = []
        for f in files:
            d = runs.read_json(f, {}) or {}
            reasons.append(f"{f.name}: {d.get('verdict')} — {_short(d.get('retry_reason') or '; '.join(d.get('required_fixes') or []), 160)}")
        return len(files), reasons

    def summary_data(self, end_state: str, published: bool) -> dict:
        t = self.target.get("target") or {}
        tgt = {"area_no": t.get("area_no"), "area_name": t.get("area_name"), "category": t.get("category")}
        if self.track:
            tgt.update({"slug": self.track.get("slug"), "stage": self.track.get("stage"), "question_ids": self.track.get("question_ids")})
        used = (self.research or {}).get("self_check", {}).get("budget_used") if self.research else None
        new_sources = 0
        if self.research:
            new_sources = sum(1 for s in self.research.get("sources", []) if s.get("id") not in self.existing_refs_before)
        r1, _ = self._retries("verification")
        r2, _ = self._retries("verification2")
        timings = self.log.timings()
        total = sum((v.get("seconds") or 0) for v in timings.values()) + (time.time() - self.t0)
        prev = runs.read_summary(self.rd)
        # 보류 표시: 게시에 성공한 실행은 parked 를 False 로 확정한다(재투입된 실행이 select_target 의 연속 보류 횟수에 계속 세어지지 않도록).
        # 실행 폴더가 runs/parked/ 에 있으면(보류 상태) 그대로 True 다.
        parked = False if published else (bool(prev.get("parked")) or runs.is_parked(self.run_id, self.settings))
        data = {
            "run_id": self.run_id, "date": self.date, "run_type": self.run_type, "target": tgt,
            "verdict_first": (self.v1 or {}).get("verdict"), "verdict_second": (self.v2 or {}).get("verdict"),
            "confidence": (self.v2 or self.v1 or {}).get("confidence"),
            "pages_created": self.counts["create"], "pages_updated": self.counts["update"] + self.counts["deprecate"],
            "new_sources": new_sources, "parked": parked, "published": published,
            "committed": self.committed, "commit": self.commit_hash, "built": self.built,
            "budget_used": used, "budget": self.target.get("budget"), "duration_sec": round(total, 1),
            "first_retries": r1, "second_retries": r2, "end_state": end_state,
            "changelog_entry": (self.pages or {}).get("changelog_entry"), "notes": self.notes,
            "counts": self.counts, "updated_at": runs.now_str(self.settings),
        }
        if parked and prev.get("park_reason"):
            data["park_reason"] = prev["park_reason"]
        # 재투입(runs/parked/ → runs/)된 실행은 이전 보류 사유를 별도 키로 이어받는다(lib/runs.py unpark)
        for k in ("resumed_from_park_reason", "resumed_at"):
            if prev.get(k):
                data[k] = prev[k]
        if not parked and prev.get("park_reason") and not data.get("resumed_from_park_reason"):
            data["resumed_from_park_reason"] = prev["park_reason"]
        return data

    def daily_block(self, end_state: str) -> str:
        t = self.target.get("target") or {}
        rt = self.run_type
        log_rel = f"logs/daily/{self.date}.md"
        if self.track:
            names = (self.track_cfg or {}).get("stage_names") or {}
            sn = names.get(self.track.get("stage")) or names.get(str(self.track.get("stage"))) or ""
            target_cell = (f"트랙 {self.track.get('name') or self.track.get('slug')} · 단계 {self.track.get('stage')}. {sn} · 질문 "
                           f"{', '.join(self.track.get('question_ids') or []) or '없음'} · 중심 영역 [{t.get('area_name')}]({paths.rel_link(log_rel, paths.area_rel_path(int(t['area_no'])))})"
                           if t.get("area_no") else f"트랙 {self.track.get('slug')}")
        elif t.get("area_no"):
            target_cell = f"[{t.get('area_name')}]({paths.rel_link(log_rel, paths.area_rel_path(int(t['area_no'])))})"
            if self.target.get("topic"):
                target_cell += f" · 주제: {self.target['topic']}"
        elif not self.target:
            target_cell = "미선정(대상 선정 전에 중단)"
        else:
            target_cell = f"해당 없음({self.run_type_label()})"
        timings = self.log.timings()
        rows = []
        for name in runs.STEP_NAMES:
            if name == "퍼블리셔":
                res = "성공" if end_state.startswith("게시") else ("실패" if "퍼블리셔" in end_state else "건너뜀")
                rows.append(f"| 퍼블리셔 | {res} | {runs.fmt_duration(time.time() - self.t0)} | {_esc('; '.join(self.notes[-3:]) or '—')} |")
                continue
            v = timings.get(name)
            if v:
                rows.append(f"| {name} | {v.get('result')} | {runs.fmt_duration(v.get('seconds'))} | {_esc(v.get('note') or '—')} |")
            else:
                rows.append(f"| {name} | 건너뜀 | — | 실행되지 않음 |")
        total = sum((v.get("seconds") or 0) for v in timings.values()) + (time.time() - self.t0)
        rows.append(f"| 합계 | | {runs.fmt_duration(total)} | |")
        r1, reasons1 = self._retries("verification")
        r2, reasons2 = self._retries("verification2")
        tc = (self.v2 or {}).get("track_checks") or (self.v1 or {}).get("track_checks")
        track_note = f" · 단계 완료 판정: {'충족' if tc.get('stage_complete') else '미충족'} · 단계 전환 승인: {'예' if tc.get('stage_transition_approved') else '아니오'}" if tc else ""
        pages_rows = []
        for pg in (self.pages or {}).get("pages", []):
            kind = "폐기" if pg.get("status") == "deprecated" else ("생성" if pg.get("action") == "create" else "갱신")
            title = self._title_of(pg["path"])
            pages_rows.append(f"| {kind} | [{_esc(title)}]({paths.rel_link(log_rel, paths.docs_rel(pg['path']))}) | {_esc(pg.get('diff_summary', ''))} |")
        side = ", ".join(f"{k} {v}건" for k, v in (("용어집", self.counts["glossary"]), ("참고문헌", self.counts["references"]), ("표준", self.counts["standards"]),
                                                 ("열린 질문", self.counts["open_questions"]), ("흐름 매트릭스 칸", self.counts["flow_cells"]),
                                                 ("트랙 백로그", self.counts["backlog"]), ("정정 요청", self.counts["corrections"])) if v)
        if side and end_state.startswith("게시"):
            pages_rows.append(f"| 부수 갱신 | 색인·홈·대분류 자동 영역, {side} | 퍼블리셔 반영 |")
        pages_table = "\n".join(["| 구분 | 페이지 | 변경 요약 |", "|---|---|---|", *pages_rows]) if pages_rows else "없음"
        srcs = (self.research or {}).get("sources", []) if self.research else []
        new_ids = sorted(s["id"] for s in srcs if s.get("id") not in self.existing_refs_before)
        reused = len(srcs) - len(new_ids)
        cross = sum(1 for c in (self.v1 or {}).get("claim_checks", []) if c.get("cross_checked")) if self.v1 else sum(1 for f in (self.research or {}).get("findings", []) if f.get("cross_checked"))
        unopened = sum(1 for s in srcs if s.get("source_unopened"))
        src_line = (f"- 신규 출처: {len(new_ids)}건" + (f" ({new_ids[0]} ~ {new_ids[-1]})" if new_ids else "") +
                    f" · 재사용 출처: {reused}건 · 교차 확인: {cross}건 · 원문 미열람: {unopened}건") if self.research else "- 없음(리서치 미실행)"
        park_lines = []
        park_lines += [f"- 1차 재조사 {r1}회: " + " / ".join(reasons1)] if reasons1 else []
        park_lines += [f"- 2차 재작성 {r2}회: " + " / ".join(reasons2)] if reasons2 else []
        prev = runs.read_summary(self.rd)
        now_parked = runs.is_parked(self.run_id, self.settings) or ("보류" in end_state)
        if now_parked or (prev.get("parked") and not end_state.startswith("게시")):
            park_lines.append(f"- 보류: runs/parked/{self.run_id}/ — {prev.get('park_reason') or end_state}")
        elif prev.get("resumed_from_park_reason") or prev.get("park_reason"):
            park_lines.append(f"- 재투입: 이전에 보류됐던 실행을 runs/parked/ 에서 되돌려 이어갔다 — 이전 보류 사유: {prev.get('resumed_from_park_reason') or prev.get('park_reason')}")
        if self.target.get("excluded_areas"):
            park_lines.append("- 3회 연속 보류로 대상 선정에서 제외한 영역: " + ", ".join(self.src.area(n).title for n in self.target["excluded_areas"]) + " (열린 질문에 사용자 검토 요청 등록)")
        if "중단" in end_state:
            park_lines.append(f"- 중단: {end_state}")
        park = "\n".join(park_lines) if park_lines else "없음"
        b = self.target.get("budget") or {}
        used = (self.research or {}).get("self_check", {}).get("budget_used", {}) if self.research else {}
        limits_text = str((self.research or {}).get("self_check", {}).get("limits", "")) if self.research else ""

        def over(u, lim):
            if u is None or lim is None:
                return "—"
            if u > lim:
                return "초과"
            if u == lim:
                return "도달(부분 결과)" if ("예산" in limits_text or "도달" in limits_text) else "도달"
            return "아니오"
        n_topic = sum(1 for pg in (self.pages or {}).get("pages", []) if pg.get("action") == "create" and "/topics/" in pg.get("path", ""))
        n_upd = sum(1 for pg in (self.pages or {}).get("pages", []) if pg.get("action") == "update" and "/tracks/" not in pg.get("path", "") and "/logs/" not in pg.get("path", ""))
        retries = r1 + r2
        budget_table = "\n".join([
            "| 항목 | 사용 | 상한 | 초과 여부 |", "|---|---|---|---|",
            f"| 검색 횟수 | {used.get('queries', '—')} | {b.get('max_search_queries', '—')} | {over(used.get('queries'), b.get('max_search_queries'))} |",
            f"| 신규 출처 | {used.get('sources', '—')} | {b.get('max_sources_per_run', '—')} | {over(used.get('sources'), b.get('max_sources_per_run'))} |",
            f"| 신규 주제 페이지 | {n_topic} | {b.get('new_topic_pages', '—')} | {over(n_topic, b.get('new_topic_pages'))} |",
            f"| 기존 페이지 갱신 | {n_upd} | {b.get('page_updates', '—')} | {over(n_upd, b.get('page_updates'))} |",
            f"| 재작업(검증 반려 후) | {retries} | {b.get('max_retries', '—')} | {over(retries, b.get('max_retries'))} |",
        ])
        nxt = []
        for x in (self.pages or {}).get("additional_research_requests", []) if self.pages else []:
            nxt.append(f"- 추가 조사 요청: {x}")
        remaining = [c["id"] for c in runs.open_corrections()]
        if remaining:
            nxt.append(f"- 미해결 정정 요청: {', '.join(remaining)}")
        if self.counts["open_questions"]:
            nxt.append(f"- 열린 질문 갱신 {self.counts['open_questions']}건")
        if self.track and self.pages and self.pages.get("track_updates"):
            tu = self.pages["track_updates"]
            nxt.append(f"- 트랙 다음 실행: {_log_segment(tu.get('log_entry', ''), '다음 실행') or _log_segment(tu.get('log_entry', ''), '다음 실행 제안') or tu.get('overview_progress', '')}")
        probe = runs.read_json(self.rd / "probe.json", {}) or {}
        if probe and not probe.get("web_fetch_available", True):
            nxt.append("- 환경: web_fetch_available: false (페이지 열람 차단, 모든 출처 원문 미열람·신뢰도 medium 상한)")
        if self.notes:
            nxt.append("- 퍼블리셔 메모: " + " / ".join(_esc(n) for n in self.notes[:6]))
        next_notes = "\n".join(nxt) if nxt else "없음"
        return "\n".join([
            f"## 실행 {self.run_id}", "",
            "### 실행 개요", "",
            "| 항목 | 값 |", "|---|---|",
            f"| 실행 id | {self.run_id} |", f"| 날짜 | {self.date} |",
            f"| 실행 유형 | {(rt + '(' + runs.RUN_TYPE_KO.get(rt, '') + ')') if rt else RUN_TYPE_UNSET + '(대상 선정 전에 중단)'} |",
            f"| 대상 영역 | {target_cell} |", f"| 종료 상태 | {_esc(end_state)} |", "",
            "### 단계별 결과와 소요 시간", "",
            "| 단계 | 결과 | 소요 시간 | 비고 |", "|---|---|---|---|", *rows, "",
            "### 검증 판정", "",
            f"- 1차 검증: {(self.v1 or {}).get('verdict') or '없음'} (재시도 {r1}회)",
            f"- 2차 검증: {(self.v2 or {}).get('verdict') or '없음'} (재시도 {r2}회){track_note}",
            f"- 확정 신뢰도: {(self.v2 or self.v1 or {}).get('confidence') or '없음'}",
            f"- 검증 노트: {(self.v2 or self.v1 or {}).get('verification_note') or '없음'}", "",
            "### 생성·갱신 페이지", "", pages_table, "",
            "### 신규 출처 수", "", src_line, "",
            "### 반려·보류 사유", "", park, "",
            "### 예산 사용량", "", budget_table, "",
            "### 다음 실행 메모", "", next_notes, "",
        ])

    def write_daily_log_and_summary(self, final: bool, end_state: str | None = None, published: bool | None = None) -> None:
        if end_state is None:
            end_state = "게시 완료" if final else "게시 진행 중(퍼블리셔 5단계 이후 결과는 확정 로그에서 갱신)"
        if published is None:
            published = final
        path = paths.DOCS / "logs" / "daily" / f"{self.date}.md"
        block = self.daily_block(end_state)
        title = f"{self.date} 일일 로그"
        head = "\n".join([f"[홈](../../index.md) › [로그](../index.md) › {self.date}", "", f"# {title}", ""])
        marker_re = re.compile(rf"^## 실행 {re.escape(self.run_id)}\s*$", re.M)
        if path.is_file():
            meta, body = fm.read(path)
            m = marker_re.search(body)
            if m:
                nxt = re.compile(r"^## 실행 ", re.M).search(body, m.end())
                end = nxt.start() if nxt else len(body)
                body = body[:m.start()] + block + body[end:]
            else:
                h1 = re.search(r"^# .*$", body, re.M)
                pos = h1.end() + 1 if h1 else 0
                body = body[:pos] + "\n" + block + body[pos:]
                meta["version"] = int(meta.get("version") or 0) + 1
            tags = [str(x) for x in (meta.get("tags") or [])]
            if self.run_type and self.run_type not in tags:
                tags.append(self.run_type)
            meta.update({"tags": tags, "updated": self.date})
        else:
            meta = {"title": title, "type": "log", "tags": [self.run_type] if self.run_type else [], "status": "published",
                    "created": self.date, "updated": self.date, "version": 1}
            body = head + "\n" + block
        fm.write(path, meta, body)
        runs.write_json(self.rd / "summary.json", self.summary_data(end_state, published))
        if final:
            self.info(f"8단계 일일 로그 저장: docs/logs/daily/{self.date}.md · summary.json (종료 상태: {end_state})")

    def step8_daily_log(self) -> bool:
        """확정 일일 로그·summary.json 을 쓰고 auto 영역·mkdocs.yml 을 다시 만든 뒤 재빌드하고 커밋을 수정(amend)한다.
        재빌드가 실패하면 확정 로그 변경분(docs, mkdocs.yml)만 8단계 직전 스냅숏으로 되돌리고 amend 를 건너뛴다
        (빌드가 깨진 상태를 커밋에 넣지 않는다, 6.4 "빌드 실패 시 롤백"). 5~7단계의 반영·커밋은 유지한다."""
        final_backup = self.rd / "backup-final"
        if final_backup.exists():
            shutil.rmtree(final_backup)
        for item in FINAL_SNAPSHOT_ITEMS:
            src = ROOT / item
            dst = final_backup / item
            if src.is_dir():
                shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__"))
            elif src.is_file():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
        self.write_daily_log_and_summary(final=True, end_state="게시 완료", published=True)
        refresh_all_auto_regions()
        write_mkdocs_yml()
        ok = True
        if not self.args.no_build:
            cmd = self._build_cmd()
            p = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=str(ROOT))
            out = (p.stdout or "") + (p.stderr or "")
            if p.returncode != 0:
                ok = False
                (self.rd / "build-final.log").write_text(out, encoding="utf-8")
                self._copy_back(final_backup, FINAL_SNAPSHOT_ITEMS)
                note = ("확정 로그 재빌드 실패·되돌림: 일일 로그·자동 영역·mkdocs.yml 을 6단계 빌드 시점으로 되돌리고 커밋 수정(amend)을 건너뛰었다. "
                        f"5~7단계의 반영과 커밋은 유지한다. 출력은 runs/{self.run_id}/build-final.log. 원인을 고친 뒤 "
                        f"'bash pipeline/run_daily.sh --resume {self.run_id} --step log' 로 확정 로그를 다시 쓴다")
                self.notes.append(note)
                self.info("8단계: " + note)
                runs.write_summary(self.rd, final_log_rebuild_failed=True, notes=self.notes)
                p2 = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=str(ROOT))
                self.info(f"8단계: 되돌린 상태의 재빌드 {'성공' if p2.returncode == 0 else '실패(exit ' + str(p2.returncode) + ')'}")
            else:
                self.info("8단계 확정 로그 반영 뒤 사이트 재빌드 성공")
        shutil.rmtree(final_backup, ignore_errors=True)
        if ok and self.committed:
            self.step7_commit(amend=True)
        return ok

    def step9_notify(self) -> None:
        notify = str(self.settings.get("notify") or "none")
        if notify != "none":
            self.info(f"9단계 알림({notify}): 자리만 있음 — 발송은 구현되지 않았다 [가정]")
        self.drop_backup()

    # --- 실행 ---------------------------------------------------------------------------------
    def publish(self) -> int:
        self.info(f"퍼블리셔 시작: {self.run_id} ({self.run_type_label()})")
        try:
            self.step1_schema()
            self.step1b_verdicts()
            if self.args.check_only:
                self.info("--check-only: 1단계(스키마·판정 확인)까지 확인했다(반영하지 않음)")
                return 0
            self.step2_frontmatter()
            self.step3_protect()
            self.step4_links()
            if self.args.dry_run:
                self.restore("--dry-run: 검사만 하고 되돌린다")
                self.drop_backup()
                self.info("--dry-run: 1~4단계 통과, docs 원복")
                return 0
            self.step5_apply()
            self.step6_build()
            self.step7_commit()
            self.step8_daily_log()
            self.step9_notify()
            self.info(f"퍼블리셔 완료: 생성 {self.counts['create']}/갱신 {self.counts['update'] + self.counts['deprecate']} · {runs.fmt_duration(time.time() - self.t0)}")
            return 0
        except PublishError as e:
            self.info(f"실패: {e}")
            # 6.4 "하나라도 실패하면 반영하지 않는다": 스냅숏 이후·커밋 전의 실패(5단계 안의 실패 포함)는 스냅숏으로 되돌린다.
            # 3·4·6단계는 자기 자리에서 restore 를 이미 불렀고(멱등), 5단계 안의 PublishError 는 여기서 되돌린다.
            if self.snapshotted and not self.committed and not self.args.dry_run:
                self.restore(f"퍼블리셔 실패({_short(str(e).splitlines()[0], 80)})")
            if not (self.args.check_only or self.args.dry_run):
                try:
                    self.write_daily_log_and_summary(final=True, end_state=f"중단(퍼블리셔: {_short(str(e).splitlines()[0], 120)})", published=False)
                    refresh_all_auto_regions()
                    write_mkdocs_yml()
                except Exception as e2:  # 로그 기록 실패는 원래 오류를 가리지 않는다
                    self.info(f"실패 로그 기록 중 오류: {e2}")
            self.drop_backup()
            return 1

    def log_only(self) -> int:
        prev = runs.read_summary(self.rd)
        end_state = prev.get("end_state") or ("보류(runs/parked/)" if prev.get("parked") else "중단")
        self.write_daily_log_and_summary(final=True, end_state=end_state, published=bool(prev.get("published")))
        refresh_all_auto_regions()
        write_mkdocs_yml()
        if not self.args.no_build:
            cmd = self._build_cmd()
            p = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=str(ROOT))
            if p.returncode != 0:
                self.info("--log-only: 사이트 빌드 실패(로그 페이지 반영은 유지): " + ((p.stdout or "") + (p.stderr or ""))[-300:])
            else:
                self.built = True
        if not self.args.no_commit and self.settings.get("git_commit", True):
            repo, items = self._git_paths()
            if (repo / ".git").exists():
                existing = [i for i in items if (repo / i).exists()]
                self._git(repo, "add", "-A", "--", *existing)
                if self._git(repo, "diff", "--cached", "--quiet").returncode != 0:
                    t = self.target.get("target") or {}
                    # 보류·중단 실행의 커밋도 6.4 의 형식("run(DATE): <실행 유형> <대상 영역 이름> — 생성 n/갱신 n")을 지키고
                    # 종료 상태를 괄호로 덧붙인다. 사양서는 보류·중단 실행의 커밋 형식을 정하지 않았다 [가정 — RUN.md 8절]
                    try:
                        n_c, n_u = int(prev.get("pages_created") or 0), int(prev.get("pages_updated") or 0)
                    except (TypeError, ValueError):
                        n_c, n_u = 0, 0
                    state = str(end_state).split("(")[0].strip() or "중단"
                    msg = f"run({self.date}): {self.run_type_label()} {t.get('area_name') or ''} — 생성 {n_c}/갱신 {n_u} ({state})".replace("  ", " ")
                    c = self._git(repo, "commit", "-q", "-m", msg)
                    if c.returncode == 0:
                        self.committed = True
                        self.commit_hash = (self._git(repo, "rev-parse", "--short", "HEAD").stdout or "").strip()
                        self.info(f"로그 커밋: {self.commit_hash} — {msg}")
                        runs.write_summary(self.rd, committed=True, commit=self.commit_hash)
        return 0


def primary_page(pages: dict) -> str:
    return pages["pages"][0]["path"] if pages.get("pages") else "docs/"


def _esc(s) -> str:
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ")


def _log_segment(entry: str, label: str) -> str:
    """'답한 질문: … / 새 질문: … / 온톨로지 변경: …' 형식의 log_entry 에서 label 부분만 꺼낸다."""
    if not entry:
        return ""
    for seg in re.split(r"\s/\s", str(entry)):
        seg = seg.strip()
        if seg.startswith(label):
            rest = seg[len(label):].lstrip(" :：")
            return rest.strip()
    return ""


def yaml_load_safe(text: str) -> dict:
    import yaml
    try:
        return yaml.safe_load(text) or {}
    except yaml.YAMLError:
        return {}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_id")
    ap.add_argument("--check-only", action="store_true", help="1단계(스키마·판정 확인)만 확인")
    ap.add_argument("--dry-run", action="store_true", help="1~4단계만 실행하고 docs 를 되돌린다")
    ap.add_argument("--log-only", action="store_true", help="보류·중단된 실행의 일일 로그·summary.json 만 쓴다")
    ap.add_argument("--no-build", action="store_true", help="6단계 사이트 빌드(와 8단계 재빌드)를 건너뛴다")
    ap.add_argument("--no-commit", action="store_true", help="7단계 커밋(과 8단계 amend)을 건너뛴다")
    args = ap.parse_args(argv)
    try:
        settings = runs.load_settings()
    except Exception as e:
        print(f"[publish] 설정 로드 실패: {e}")
        return 2
    try:
        pub = Publisher(args.run_id, settings, args)
    except PublishError as e:
        print(f"[publish] {e}")
        return 2
    if args.log_only:
        return pub.log_only()
    return pub.publish()


if __name__ == "__main__":
    sys.exit(main())
