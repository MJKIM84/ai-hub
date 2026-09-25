#!/usr/bin/env python3
"""실행별 품질·비용 지표(운영 전환 완료 보고의 개선 전후 비교표). 모델 호출 없음.

  python3 pipeline/report_metrics.py [run_id ...] [--since 2026-09-25-03] [--json out.json] [--md out.md]

지표(실행마다)
- 원문 열람 출처: research.json sources 가운데 fetched true (개선 전 실행은 fetched 필드가 없고 source_unopened true → 0)
- 교차 확인: verification.json(1차) claim_checks 가운데 cross_checked true(검증 에이전트가 서로 독립인 두 출처를 직접 확인한 것)
- 다중 출처 finding: research.json findings 가운데 source_ids 가 2개 이상인 것(독립성은 따지지 않는다)
- 퍼블리셔 실패: timings.json 의 '퍼블리셔' 단계 가운데 결과가 성공이 아닌 것
- 재작성: 스토리텔러 호출 수 − 1 (2차 검증 수정 지시 재작성 + 형식 수정 재작성). 형식 수정만 따로 센다
- 비용: usage.json total.cost_usd, 없으면 prompts/*.response.json 의 total_cost_usd 합(점검 호출 제외)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import runs  # noqa: E402


def run_metrics(rd: Path) -> dict:
    rid = rd.name
    target = runs.read_json(rd / "target.json", {}) or {}
    summ = runs.read_summary(rd)
    research = runs.read_json(rd / "research.json", {}) or {}
    v1 = runs.read_json(rd / "verification.json", {}) or {}
    timings = runs.read_json(rd / "timings.json", {}) or {}
    usage = runs.read_json(rd / "usage.json", None)
    sources = research.get("sources") or []
    fetched = sum(1 for s in sources if s.get("fetched") is True)
    cross = sum(1 for c in (v1.get("claim_checks") or []) if c.get("cross_checked") is True)
    multi = sum(1 for f in research.get("findings") or [] if len(set(f.get("source_ids") or [])) >= 2)
    steps = timings.get("steps") or []
    pub_fail = sum(1 for s in steps if str(s.get("step")) == "퍼블리셔" and not str(s.get("result", "")).startswith("성공"))
    prompts = sorted((rd / "prompts").glob("storyteller*.md")) if (rd / "prompts").is_dir() else []
    story_calls = len([p for p in prompts if not p.name.endswith(".meta.json")])
    format_fix = len([p for p in prompts if "formatfix" in p.name])
    if usage and (usage.get("total") or {}).get("cost_usd") is not None:
        cost = float(usage["total"]["cost_usd"])
        calls = int(usage["total"].get("calls") or 0)
    else:
        cost, calls = 0.0, 0
        for f in sorted((rd / "prompts").glob("*.response.json")) if (rd / "prompts").is_dir() else []:
            d = runs.read_json(f, {}) or {}
            cost += float(d.get("total_cost_usd") or 0)
            calls += 1
    t = target.get("target") or {}
    tr = target.get("track") or {}
    return {
        "run_id": rid, "run_type": target.get("run_type"), "area_no": t.get("area_no"), "track": tr.get("slug"),
        "category": t.get("category_letter"), "published": bool(summ.get("published")), "parked": bool(summ.get("parked")),
        "sources": len(sources), "fetched_sources": fetched, "cross_checked": cross, "multi_source_findings": multi,
        "findings": len(research.get("findings") or []), "claims": len(v1.get("claim_checks") or []),
        "publisher_failures": pub_fail, "rewrites": max(story_calls - 1, 0), "format_fix_rewrites": format_fix,
        "cost_usd": round(cost, 4), "calls": calls, "duration_sec": summ.get("duration_sec"),
    }


def aggregate(rows: list[dict]) -> dict:
    n = len(rows) or 1
    def avg(k):
        return round(sum(float(r.get(k) or 0) for r in rows) / n, 2)
    return {"runs": len(rows), "published": sum(1 for r in rows if r["published"]),
            "fetched_sources_avg": avg("fetched_sources"), "fetched_sources_total": sum(r["fetched_sources"] for r in rows),
            "sources_avg": avg("sources"), "cross_checked_avg": avg("cross_checked"),
            "multi_source_findings_avg": avg("multi_source_findings"), "findings_avg": avg("findings"),
            "cross_checked_total": sum(r["cross_checked"] for r in rows),
            "publisher_failures_total": sum(r["publisher_failures"] for r in rows), "publisher_failures_avg": avg("publisher_failures"),
            "rewrites_avg": avg("rewrites"), "rewrites_total": sum(r["rewrites"] for r in rows),
            "cost_avg": avg("cost_usd"), "cost_total": round(sum(float(r["cost_usd"]) for r in rows), 2),
            "duration_avg_min": round(sum(float(r.get("duration_sec") or 0) for r in rows) / n / 60, 1)}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_ids", nargs="*")
    ap.add_argument("--since", help="이 실행 id 이후(포함)의 모든 실행")
    ap.add_argument("--json")
    ap.add_argument("--md")
    args = ap.parse_args(argv)
    settings = runs.load_settings()
    ids = list(args.run_ids)
    if args.since:
        ids += [r for r in runs.list_run_ids(settings) if r >= args.since and r not in ids]
    rows = []
    for rid in ids:
        rd = runs.find_run_dir(rid, settings)
        if rd:
            rows.append(run_metrics(rd))
    agg = aggregate(rows)
    out = {"runs": rows, "aggregate": agg}
    if args.json:
        runs.write_json(args.json, out)
    lines = ["| 실행 | 유형 | 대상 | 게시 | 출처 | 원문 열람 | 다중 출처 finding | 교차 확인(검증) | 퍼블리셔 실패 | 재작성(형식) | 비용 $ | 분 |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        tgt = r["track"] or (f"영역 {r['area_no']}" if r["area_no"] else (f"대분류 {r['category']}" if r["category"] else "-"))
        lines.append(f"| {r['run_id']} | {r['run_type']} | {tgt} | {'예' if r['published'] else ('보류' if r['parked'] else '아니오')} | "
                     f"{r['sources']} | {r['fetched_sources']} | {r['multi_source_findings']}/{r['findings']} | {r['cross_checked']} | {r['publisher_failures']} | "
                     f"{r['rewrites']}({r['format_fix_rewrites']}) | {r['cost_usd']:.2f} | {round(float(r.get('duration_sec') or 0) / 60, 1)} |")
    lines.append("")
    lines.append("합계·평균: " + json.dumps(agg, ensure_ascii=False))
    text = "\n".join(lines) + "\n"
    if args.md:
        Path(args.md).write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
