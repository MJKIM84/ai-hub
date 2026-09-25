#!/usr/bin/env python3
"""에이전트 산출물 형식 검증(운영 전환 1-2). 에이전트 호출 직후 run_daily.sh 가 부른다. 모델 호출 없음.

  python3 pipeline/validate_run.py <run_id> --stage research|verification1|verification2|pages

- research: 출처별 원문 열람 여부(fetched)를 확정하고 못 연 출처의 신뢰도 상한을 코드로 강제한다(lib.sources.apply_fetch_caps).
  바꾼 값은 research.json 에 쓰고 사람이 읽는 research.md 를 다시 만든다. 형식 오류가 아니므로 항상 exit 0.
- verification1 / verification2: 스키마 밖 교차 검사(정정 요청 거절 id 가 이번 실행의 정정 요청인지 등). 오류면 exit 1.
- pages: ① 차등 갱신 패치를 현재 페이지에 적용해 전체 페이지를 만든다 ② 세부영역 본문이 분량 기준을 넘으면 넘치는 절을
  주제 페이지로 자동 분리한다(내용을 줄이지 않는다) ③ 페이지별 형식 검사 ④ 퍼블리셔 2~4단계 사전 검사(--precheck).
  오류가 있으면 runs/<id>/format_check.json·format_check.md 에 적고 exit 1 → run_daily.sh 가 오류를 붙여 스토리텔러에 형식 수정을 요청한다.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import frontmatter as fm  # noqa: E402
from lib import paths, runs  # noqa: E402
from lib import validate as V  # noqa: E402

ROOT = paths.ROOT


def _log(rd: Path, settings: dict, msg: str) -> None:
    try:
        runs.RunLog(rd, settings).log(msg, step="형식 검증")
    except Exception:  # noqa: BLE001
        pass
    print(f"[validate] {msg}")


def stage_research(rd: Path, settings: dict) -> int:
    data = runs.read_json(rd / "research.json", None)
    if data is None:
        print("[validate] research.json 없음")
        return 2
    changes: list[str] = []
    probe = runs.read_json(rd / "probe.json", {}) or {}
    try:
        from lib import sources as S  # 원문 열람 흐름(inbox/sources, GitHub raw 미러)
        for src in data.get("sources", []):
            # 에이전트가 raw.githubusercontent.com 을 WebFetch 로 열고 경로를 webfetch 로 적은 경우 github_raw 로 본다
            if src.get("fetched_via") == "webfetch" and S.is_raw_github(str(src.get("fetch_url") or "")):
                src["fetched_via"] = "github_raw"
        changes = S.apply_fetch_caps(data, web_fetch_available=probe.get("web_fetch_available")) or []
    except ImportError:
        # sources 모듈이 없으면 최소 규칙만 적용: fetched 가 없으면 false, 못 연 출처·그 출처만 쓴 주장은 medium 상한
        for s in data.get("sources", []):
            s.setdefault("fetched", False)
            if not s.get("fetched") and s.get("reliability") == "high":
                s["reliability"] = "medium"
                changes.append(f"{s.get('id')}: 원문 미열람 출처의 신뢰도 high → medium")
        fetched = {s.get("id") for s in data.get("sources", []) if s.get("fetched")}
        for f in data.get("findings", []):
            if f.get("confidence") == "high" and not (set(f.get("source_ids") or []) & fetched):
                f["confidence"] = "medium"
                changes.append(f"{f.get('id')}: 근거 출처를 모두 원문 미열람 → 신뢰도 high → medium")
    n_fetched = sum(1 for s in data.get("sources", []) if s.get("fetched"))
    runs.write_json(rd / "research.json", data)
    try:
        import render_run_md
        render_run_md.render_run(rd, "research")
    except Exception:  # noqa: BLE001
        pass
    report = {"stage": "research", "ok": True, "fetched_sources": n_fetched, "total_sources": len(data.get("sources", [])),
              "caps_applied": changes}
    runs.write_json(rd / "checks" / "research.json", report)
    _log(rd, settings, f"리서치 산출물 검사: 출처 {report['total_sources']}건 중 원문 열람 {n_fetched}건 · 신뢰도 상한 적용 {len(changes)}건")
    for c in changes[:30]:
        _log(rd, settings, f"  - {c}")
    return 0


def stage_verification(rd: Path, settings: dict, which: str) -> int:
    name = "verification.json" if which == "verification1" else "verification2.json"
    v = runs.read_json(rd / name, None)
    target = runs.read_json(rd / "target.json", {}) or {}
    if v is None:
        print(f"[validate] {name} 없음")
        return 2
    errs: list[str] = []
    fixed: list[str] = []
    corr_ids = {c.get("id") for c in target.get("corrections") or []}
    # 이번 실행의 정정 요청이 아닌 id 는 코드가 뺀다(판단이 필요 없는 정리). 퍼블리셔도 대상 요청만 처리한다
    keep_rej = [r for r in v.get("corrections_rejected") or [] if r.get("id") in corr_ids]
    keep_app = [i for i in v.get("corrections_applied") or [] if i in corr_ids]
    dropped = [r.get("id") for r in v.get("corrections_rejected") or [] if r.get("id") not in corr_ids]
    dropped += [i for i in v.get("corrections_applied") or [] if i not in corr_ids]
    if dropped:
        v["corrections_rejected"], v["corrections_applied"] = keep_rej, keep_app
        runs.write_json(rd / name, v)
        fixed.append(f"이번 실행의 정정 요청이 아닌 id 를 뺐다: {sorted(set(dropped))} (target.json corrections: {sorted(corr_ids) or '없음'})")
    both = set(v.get("corrections_applied") or []) & {r.get("id") for r in v.get("corrections_rejected") or []}
    if both:
        errs.append(f"같은 정정 요청을 반영과 거절에 모두 넣었다: {sorted(both)}")
    report = {"stage": which, "ok": not errs, "errors": errs, "fixed": fixed}
    for f in fixed:
        _log(rd, settings, f"  - {f}")
    runs.write_json(rd / "checks" / f"{which}.json", report)
    _log(rd, settings, f"{'1차' if which == 'verification1' else '2차'} 검증 산출물 검사: {'통과' if not errs else f'오류 {len(errs)}건'}")
    return 0 if not errs else 1


def _write_page(rd: Path, repo_path: str, text: str) -> None:
    runs.write_text(rd / "pages" / paths.docs_rel(repo_path), text if text.endswith("\n") else text + "\n")


def stage_pages(rd: Path, settings: dict, run_id: str) -> int:
    pages = runs.read_json(rd / "pages.json", None)
    target = runs.read_json(rd / "target.json", {}) or {}
    if pages is None:
        print("[validate] pages.json 없음")
        return 2
    errors: list[str] = []
    patched: list[str] = []
    splits: list[dict] = []
    day = str(target.get("date") or run_id[:10])
    limit = int(settings.get("area_body_char_limit") or 4000)

    # ① 차등 갱신 패치 적용 + 기계적 마무리(프런트매터 version·updated·status, 빠진 각주 정의)
    research = runs.read_json(rd / "research.json", {}) or {}
    run_refs = {s["id"]: s for s in research.get("sources", []) if s.get("id")}
    for r in pages.get("reference_updates") or []:
        if r.get("id"):
            run_refs.setdefault(r["id"], r)
    for pg in pages.get("pages", []):
        if pg.get("patches"):
            cur = ROOT / pg["path"]
            if not cur.is_file():
                errors.append(f"{pg['path']}: 패치를 적용할 현재 페이지가 없다(새 페이지는 content 로 보낸다)")
                continue
            prior = cur.read_text(encoding="utf-8")
            try:
                new = V.apply_patches(prior, pg["patches"])
            except ValueError as e:
                errors.append(f"{pg['path']}: {e}")
                continue
            explicit = {}
            for p in pg["patches"]:
                explicit.update(p.get("frontmatter") or {})
            new, done = V.complete_patched_page(new, prior, day, run_refs, explicit)
            for d in done:
                pages.setdefault("fixes_applied", []).append(f"{pg['path']}: {d}")
            _write_page(rd, pg["path"], new)
            patched.append(f"{pg['path']} ({len(pg['patches'])}개 절)")
            pg["_patched"] = True

    # ② 세부영역 분량 초과 → 주제 페이지 자동 분리
    topic_h2 = V.expected_h2("topic")
    for pg in list(pages.get("pages", [])):
        src = rd / "pages" / paths.docs_rel(pg.get("path", ""))
        if not src.is_file():
            continue
        text = src.read_text(encoding="utf-8")
        try:
            meta, body = fm.parse(text)
        except Exception:  # noqa: BLE001
            continue
        if meta.get("type") != "area":
            continue
        chars = V.area_body_chars(body)
        if chars <= limit:
            continue
        new_area, topics = V.split_oversized_area(pg["path"], text, limit, pages.get("outline") or [], run_id, day, topic_h2)
        if not topics:
            continue
        _write_page(rd, pg["path"], new_area)
        for tp in topics:
            _write_page(rd, tp["path"], tp["content"])
            pages["pages"].append({"path": tp["path"], "action": "create", "status": "draft",
                                   "diff_summary": f"자동 분리: {meta.get('title')} 의 \"{tp['section']}\" 절({tp['chars']:,}자)을 옮겼다"})
            splits.append({"from": pg["path"], "section": tp["section"], "to": tp["path"], "chars": tp["chars"]})
        after = V.area_body_chars(fm.parse(new_area)[1])
        note = (f"분량 초과 자동 분리: {meta.get('title')} 본문 {chars:,}자 > 기준 {limit:,}자 → "
                f"{len(topics)}개 절을 주제 페이지로 옮김, 남은 본문 {after:,}자")
        pages.setdefault("fixes_applied", []).append(note)

    # ②-b 참조가 없는 각주 정의는 뺀다(엄격 빌드가 'footnote never referenced' 로 실패한다 — 판단이 필요 없는 정리, 3부 배치 세부영역 27)
    for pg in pages.get("pages", []):
        src = rd / "pages" / paths.docs_rel(pg.get("path", ""))
        if src.is_file():
            t = src.read_text(encoding="utf-8")
            n = V._drop_unused_defs(t)
            if n != t:
                src.write_text(n, encoding="utf-8")
                pages.setdefault("fixes_applied", []).append(f"{pg.get('path')}: 참조가 없는 각주 정의를 뺐다")

    # ③ 페이지별 형식 검사
    for pg in pages.get("pages", []):
        rel = paths.docs_rel(pg.get("path", ""))
        src = rd / "pages" / rel
        if not src.is_file():
            errors.append(f"{pg.get('path')}: pages/ 에 파일이 없다")
            continue
        for e in V.check_page(rel, src.read_text(encoding="utf-8")):
            errors.append(f"{pg.get('path')}: {e}")

    # pages.json 갱신(패치 표시 제거, 분리 페이지 추가)
    stored = json.loads(json.dumps(pages, ensure_ascii=False))
    for pg in stored.get("pages", []):
        pg.pop("_patched", None)
    runs.write_json(rd / "pages.json", stored)

    # ④ 퍼블리셔 2~4단계 사전 검사
    if not errors:
        p = subprocess.run([sys.executable, "pipeline/publish.py", run_id, "--precheck"], cwd=str(ROOT),
                           capture_output=True, text=True)
        if p.returncode != 0:
            out = (p.stdout or "") + (p.stderr or "")
            lines = [l.strip() for l in out.splitlines() if l.strip() and not l.startswith("[publish] 스냅숏")]
            errs = [l for l in lines if l.startswith("- ") or "실패" in l][:40]
            errors += [f"퍼블리셔 사전 검사: {e}" for e in (errs or lines[-10:])]

    report = {"stage": "pages", "ok": not errors, "errors": errors, "patched": patched, "splits": splits,
              "area_body_limit": limit}
    runs.write_json(rd / "checks" / "pages.json", report)
    md = ["# 형식 검증 결과(pages)", "", f"- 판정: {'통과' if not errors else f'오류 {len(errors)}건'}"]
    if patched:
        md += ["- 차등 갱신 패치 적용:"] + [f"    - {x}" for x in patched]
    if splits:
        md += ["- 분량 초과 자동 분리:"] + [f"    - {s['from']} \"{s['section']}\" → {s['to']} ({s['chars']:,}자)" for s in splits]
    if errors:
        md += ["- 오류:"] + [f"    - {e}" for e in errors]
    runs.write_text(rd / "format_check.md", "\n".join(md) + "\n")
    note = " · ".join(x for x in ((f"패치 적용 {len(patched)}건" if patched else ""), (f"자동 분리 {len(splits)}건" if splits else "")) if x)
    runs.write_text(rd / "checks" / "pages_note.txt", note)
    _log(rd, settings, f"원고 형식 검사: {'통과' if not errors else f'오류 {len(errors)}건'}"
         + (f" · 패치 적용 {len(patched)}건" if patched else "") + (f" · 자동 분리 {len(splits)}건" if splits else ""))
    for e in errors[:20]:
        _log(rd, settings, f"  - {e[:300]}")
    return 0 if not errors else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_id")
    ap.add_argument("--stage", required=True, choices=["research", "verification1", "verification2", "pages"])
    args = ap.parse_args(argv)
    settings = runs.load_settings()
    rd = runs.find_run_dir(args.run_id, settings)
    if not rd:
        print(f"[validate] 실행 폴더 없음: {args.run_id}")
        return 2
    if args.stage == "research":
        return stage_research(rd, settings)
    if args.stage in ("verification1", "verification2"):
        return stage_verification(rd, settings, args.stage)
    return stage_pages(rd, settings, args.run_id)


if __name__ == "__main__":
    sys.exit(main())
