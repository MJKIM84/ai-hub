#!/usr/bin/env python3
"""runs/<run_id>/ 의 JSON 산출물을 사람이 읽는 마크다운으로 렌더링한다.

- research.json      → research.md      (리서치 브리프, 사양서 6.1 "사람이 읽는 research.md")
- verification.json  → verification.md  (1차 검증 판정, 6.2)
- verification2.json → verification2.md (2차 검증 판정) [가정: 파일 이름은 실행 규약의 runs/ 목록을 따른다]
- pages.json         → pages.md         (스토리텔러 산출 요약; 선택 [가정])

publish.py 와 run_daily.sh(agent_runner.py) 가 함수를 호출하고, 사람이 직접 다시 만들 때는
  python3 pipeline/render_run_md.py <run_id 또는 실행 폴더> [--only research|verification|verification2|pages]
로 실행한다. 렌더링은 JSON 값을 표와 목록으로 옮길 뿐 내용을 더하거나 판단하지 않는다.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import runs  # noqa: E402


def _cell(v) -> str:
    if v is None:
        return "—"
    if isinstance(v, bool):
        return "예" if v else "아니오"
    if isinstance(v, list):
        return ", ".join(str(x) for x in v) if v else "—"
    return str(v).replace("|", "\\|").replace("\n", " ")


def _table(header: list[str], rows: list[list]) -> str:
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for r in rows:
        lines.append("| " + " | ".join(_cell(c) for c in r) + " |")
    return "\n".join(lines)


def _bullets(items, empty: str = "없음") -> str:
    items = [x for x in (items or []) if x not in (None, "")]
    return "\n".join(f"- {_cell(x) if not isinstance(x, str) else x}" for x in items) if items else f"- {empty}"


def render_research_md(d: dict) -> str:
    t = d.get("target") or {}
    parts = [f"# 리서치 브리프 {d.get('run_id', '')}", ""]
    parts.append(_table(["항목", "값"], [
        ["실행 id", d.get("run_id")], ["날짜", d.get("date")],
        ["실행 유형", f"{d.get('run_type')} ({runs.RUN_TYPE_KO.get(d.get('run_type'), '')})"],
        ["대상 영역", t.get("area_name") or "해당 없음"], ["대분류", t.get("category") or "해당 없음"],
    ]))
    tr = d.get("track")
    if tr:
        parts += ["", "트랙 실행: " + f"트랙 `{tr.get('slug')}` · 단계 {tr.get('stage')} · 답한 질문 {_cell(tr.get('answered_question_ids'))}"]
    parts += ["", "## 갭(비어 있거나 약한 섹션)", "", _bullets(d.get("gaps"))]
    parts += ["", "## 조사 질문", ""]
    rq = d.get("research_questions") or []
    parts.append("\n".join(f"{i + 1}. {q}" for i, q in enumerate(rq)) if rq else "- 없음")
    parts += ["", "## 발견 사항", ""]
    fs = d.get("findings") or []
    if fs:
        rows = []
        for f in fs:
            flags = []
            if f.get("source_unopened"):
                flags.append("원문 미열람")
            if f.get("vendor_claim"):
                flags.append("벤더 주장")
            rows.append([f.get("id"), f"[{f.get('tag')}]", f.get("claim"), f.get("source_ids"), f.get("cross_checked"),
                         f.get("confidence"), f.get("as_of"),
                         " / ".join(x for x in (f.get("flow_step"), f.get("flow_item")) if x) or "—", ", ".join(flags) or "—"])
        parts.append(_table(["id", "태그", "주장", "출처", "교차 확인", "신뢰도", "기준일", "흐름 단계 / 항목", "표시"], rows))
        parts += ["", "### 근거 발췌", ""]
        for f in fs:
            parts.append(f"- **{f.get('id')}**: {f.get('evidence_excerpt', '')}")
    else:
        parts.append("- 없음")
    parts += ["", "## 출처", ""]
    ss = d.get("sources") or []
    if ss:
        parts.append(_table(["id", "기관", "제목", "발행일", "유형", "신뢰도", "접근일", "URL", "원문 미열람"],
                            [[s.get("id"), s.get("org"), s.get("title"), s.get("published") or "미확인", s.get("type"),
                              s.get("reliability"), s.get("accessed"), s.get("url"), s.get("source_unopened", False)] for s in ss]))
        parts += ["", "### 출처 요약", ""]
        for s in ss:
            parts.append(f"- **{s.get('id')}**: {s.get('summary', '')}")
    else:
        parts.append("- 없음")
    parts += ["", "## 페이지 제안", ""]
    pp = d.get("page_proposals") or []
    parts.append(_table(["동작", "경로", "섹션", "이유"], [[p.get("action"), p.get("path"), p.get("sections"), p.get("rationale")] for p in pp]) if pp else "- 없음")
    parts += ["", "## 용어 후보", ""]
    gc = d.get("glossary_candidates") or []
    parts.append(_table(["용어(한글)", "용어(영문)", "한 줄 정의"], [[g.get("term_ko"), g.get("term_en"), g.get("definition")] for g in gc]) if gc else "- 없음")
    parts += ["", "## 열린 질문", "", "새로 생긴 질문:", "", _bullets(d.get("open_questions_new")), "",
              "해결 제안(판정은 검증 에이전트):", "", _bullets(d.get("open_questions_resolved"))]
    sc = d.get("self_check") or {}
    bu = sc.get("budget_used") or {}
    parts += ["", "## 자체 점검", "",
              f"- 출처 수: {sc.get('source_count', '—')} · 교차 확인: {sc.get('cross_checked_count', '—')}",
              f"- 예산 사용량: 검색 {bu.get('queries', '—')}회 · 신규 출처 {bu.get('sources', '—')}건",
              "- 미확인 항목:", _bullets(sc.get("unverified")).replace("\n- ", "\n    - ").replace("- ", "    - ", 1),
              "- 범위 경계 위반 의심:", _bullets(sc.get("scope_violations")).replace("\n- ", "\n    - ").replace("- ", "    - ", 1),
              f"- 한계: {sc.get('limits', '—')}"]
    if tr:
        parts += ["", "## 트랙 블록", "",
                  f"- 트랙: {tr.get('slug')} · 단계: {tr.get('stage')}",
                  f"- 답한 질문 id: {_cell(tr.get('answered_question_ids'))}",
                  "", "### 새 질문", ""]
        nq = tr.get("new_questions") or []
        parts.append(_table(["제안 id", "질문", "보낼 단계", "근거 finding"],
                            [[q.get("id") or "—", q.get("question"), q.get("stage"), q.get("rationale_finding_id")] for q in nq]) if nq else "- 없음")
        parts += ["", "### 온톨로지 초안 변경 제안", ""]
        oc = tr.get("ontology_changes") or []
        parts.append(_table(["동작", "종류", "이름", "근거 finding", "설명"],
                            [[c.get("op"), c.get("kind"), c.get("name"), c.get("evidence_finding_ids"), c.get("description") or "—"] for c in oc]) if oc else "- 없음")
        sa = tr.get("stage_completion_self_assessment") or {}
        parts += ["", "### 단계 완료 조건 자체 평가", "",
                  f"- 충족 여부(자체 평가): {'충족' if sa.get('met') else '미충족'}",
                  "- 못 채운 조건:", _bullets(sa.get("missing")).replace("\n- ", "\n    - ").replace("- ", "    - ", 1)]
    return "\n".join(parts).rstrip("\n") + "\n"


def render_verification_md(d: dict, label: str | None = None) -> str:
    stage = d.get("stage")
    label = label or ("1차 검증(브리프)" if stage == "first" else "2차 검증(서술)" if stage == "second" else "검증")
    parts = [f"# {label} {d.get('run_id', '')}", "",
             f"**판정: {d.get('verdict', '—')}** · 신뢰도: {d.get('confidence', '—')}", ""]
    if d.get("retry_reason"):
        parts += ["재작업 사유(retry_reason):", "", f"> {d['retry_reason']}", ""]
    parts += ["## 주장별 검증", ""]
    cc = d.get("claim_checks") or []
    parts.append(_table(["finding", "출처 실재", "주장 뒷받침", "교차 확인", "태그 처분", "메모"],
                        [[c.get("finding_id"), c.get("source_exists"), c.get("supports_claim"), c.get("cross_checked"),
                          c.get("tag_decision"), c.get("note")] for c in cc]) if cc else "- 없음(2차 검증은 브리프 밖 주장만 다룬다)")
    cf = d.get("category_fit") or {}
    sb = d.get("scope_boundary") or {}
    du = d.get("duplication") or {}
    te = d.get("terminology") or {}
    qc = d.get("quotation_check") or {}
    parts += ["", "## 항목별 결과", "",
              _table(["항목", "결과", "내용"], [
                  ["분류 적합성", cf.get("ok"), f"재배치: {cf.get('reassign_to')}" if cf.get("reassign_to") else "—"],
                  ["범위 경계", sb.get("ok"), sb.get("issues")],
                  ["중복·모순", du.get("ok"), du.get("overlaps")],
                  ["용어 일관성", te.get("ok"), te.get("conflicts")],
                  ["인용 길이·저작권", qc.get("ok"), qc.get("issues")],
                  ["정정 요청 반영", "—", d.get("corrections_applied")],
              ])]
    parts += ["", "## 수정 지시(required_fixes)", "", _bullets(d.get("required_fixes"))]
    parts += ["", "## 검증 노트", "", d.get("verification_note") or "—"]
    tc = d.get("track_checks")
    if tc:
        parts += ["", "## 트랙 추가 검증", "",
                  _table(["항목", "결과"], [
                      ["표준 출처(발행 기관 자료)", tc.get("standard_sources_ok")],
                      ["벤더 주장 표기", tc.get("vendor_claims_tagged")],
                      ["온톨로지 변경 근거", tc.get("ontology_changes_grounded")],
                      ["백로그 중복 질문", tc.get("backlog_duplicates")],
                      ["단계 태그 문제", tc.get("stage_tag_issues")],
                      ["완전성 표현", tc.get("completeness_wording_ok")],
                      ["단계 완료 판정", "충족" if tc.get("stage_complete") else "미충족"],
                      ["단계 전환 승인", "예" if tc.get("stage_transition_approved") else "아니오"],
                  ])]
    return "\n".join(parts).rstrip("\n") + "\n"


def render_pages_md(d: dict) -> str:
    parts = [f"# 스토리텔러 산출 {d.get('run_id', '')}", "", "## 페이지", ""]
    pg = d.get("pages") or []
    parts.append(_table(["동작", "경로", "상태", "변경 요약"], [[p.get("action"), p.get("path"), p.get("status"), p.get("diff_summary")] for p in pg]))
    iu = d.get("index_updates") or {}
    parts += ["", "## 변경 이력·색인", "", f"- 변경 이력: {d.get('changelog_entry', '—')}",
              f"- 홈 최근 업데이트: {iu.get('home_recent', '—')}", f"- 대분류 최근 업데이트: {iu.get('category_recent', '—')}",
              f"- 세부영역 최근 업데이트: {iu.get('area_recent', '—')}"]
    parts += ["", "## 용어집 갱신", ""]
    gl = d.get("glossary_updates") or []
    parts.append(_table(["동작", "용어(한글)", "용어(영문)", "한 줄 정의", "관련 영역", "출처"],
                        [[g.get("action", "new"), g.get("term_ko"), g.get("term_en"), g.get("definition"), g.get("related_areas"), g.get("sources")] for g in gl]) if gl else "- 없음")
    parts += ["", "## 참고문헌 갱신", ""]
    rf = d.get("reference_updates") or []
    parts.append(_table(["id", "기관", "제목", "유형", "신뢰도", "URL"], [[r.get("id"), r.get("org"), r.get("title"), r.get("type"), r.get("reliability"), r.get("url")] for r in rf]) if rf else "- 없음")
    parts += ["", "## 열린 질문 갱신", ""]
    oq = d.get("open_question_updates") or []
    parts.append(_table(["동작", "id", "질문", "영역", "상태", "링크"], [[q.get("action"), q.get("id") or "—", q.get("question"), q.get("areas"), q.get("status"), q.get("link")] for q in oq]) if oq else "- 없음")
    parts += ["", "## 흐름 매트릭스 갱신", ""]
    fmu = d.get("flow_matrix_updates") or []
    parts.append(_table(["단계", "항목", "링크", "제목"], [[f.get("step"), f.get("item"), f.get("link"), f.get("title") or "—"] for f in fmu]) if fmu else "- 없음")
    parts += ["", "## 표준·프레임워크 갱신", ""]
    su = d.get("standards_updates") or []
    parts.append(_table(["이름", "종류", "기관", "관련 영역", "참고문헌", "URL"], [[s.get("name"), s.get("kind"), s.get("org"), s.get("related_areas"), s.get("ref_id") or "—", s.get("url")] for s in su]) if su else "- 없음")
    parts += ["", "## 추가 조사 요청", "", _bullets(d.get("additional_research_requests")),
              "", "## 이행한 수정 지시", "", _bullets(d.get("fixes_applied"))]
    tu = d.get("track_updates")
    if tu:
        parts += ["", "## 트랙 갱신", "",
                  f"- 단계 페이지: {tu.get('stage_page')}", f"- 온톨로지 초안 버전: {tu.get('ontology_draft_version')}",
                  f"- 트랙 로그 항목: {tu.get('log_entry')}", f"- 개요 진행 현황: {tu.get('overview_progress')}"]
        st = tu.get("stage_transition")
        if st:
            parts.append(f"- 단계 전환: 단계 {st.get('to_stage')} — {st.get('reason')}")
        bu = tu.get("backlog_updates") or []
        parts += ["", "### 백로그 갱신", ""]
        parts.append(_table(["id", "상태", "답 링크", "질문(새 질문)", "단계", "제기 근거"],
                            [[b.get("id"), b.get("status"), b.get("answer_link"), b.get("question") or "—", b.get("stage") or "—", b.get("origin") or "—"] for b in bu]) if bu else "- 없음")
        arp = d.get("area_reflection_proposals") or []
        parts += ["", "### 세부영역 반영 제안", ""]
        parts.append(_table(["세부영역 번호", "절", "요약"], [[a.get("area_no"), a.get("section"), a.get("summary")] for a in arp]) if arp else "- 없음")
    return "\n".join(parts).rstrip("\n") + "\n"


RENDERERS = {
    "research": ("research.json", "research.md", render_research_md),
    "verification": ("verification.json", "verification.md", lambda d: render_verification_md(d, "1차 검증(브리프)")),
    "verification2": ("verification2.json", "verification2.md", lambda d: render_verification_md(d, "2차 검증(서술)")),
    "pages": ("pages.json", "pages.md", render_pages_md),
}


def render_run(run_directory: Path, only: str | None = None) -> list[Path]:
    out = []
    for key, (src, dst, fn) in RENDERERS.items():
        if only and key != only:
            continue
        p = run_directory / src
        if not p.is_file():
            continue
        data = runs.read_json(p)
        out.append(runs.write_text(run_directory / dst, fn(data)))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run", help="실행 id(runs/<id> 또는 runs/parked/<id>) 또는 실행 폴더 경로")
    ap.add_argument("--only", choices=list(RENDERERS))
    args = ap.parse_args(argv)
    d = Path(args.run)
    if not d.is_dir():
        d = runs.find_run_dir(args.run)
    if not d or not d.is_dir():
        print(f"[render_run_md] 실행 폴더를 찾을 수 없다: {args.run}")
        return 1
    written = render_run(d, args.only)
    for p in written:
        print(f"[render_run_md] 저장: {p}")
    if not written:
        print("[render_run_md] 렌더링할 JSON 이 없다")
    return 0


if __name__ == "__main__":
    sys.exit(main())
