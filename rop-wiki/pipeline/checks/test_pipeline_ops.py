"""운영 전환(1부) 기능 테스트: 형식 검증·자동 분리·차등 패치·참고문헌 id 재배정·트랙 가중 선택·대분류 연결 선정·
시스템 프롬프트 캐시·사용량 기록, 그리고 드라이런 퍼블리셔 실패 회귀 입력."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from lib import frontmatter as fm  # noqa: E402
from lib import paths, runs  # noqa: E402
from lib import validate as V  # noqa: E402

FIX = HERE / "fixtures" / "regressions"
AREA7 = paths.ROOT / paths.area_repo_path(7)


def _area_page(extra_sections: dict[str, str]) -> str:
    """area 7 페이지를 바탕으로 특정 절 본문을 바꾼 시험 페이지."""
    text = AREA7.read_text(encoding="utf-8")
    meta, body = fm.parse(text)
    patches = [{"section": k, "action": "replace", "content": v} for k, v in extra_sections.items()]
    return V.apply_patches(fm.dumps(meta, body), patches) if patches else text


class TestValidate(unittest.TestCase):
    def test_expected_h2_area_and_topic(self):
        self.assertEqual(len(V.expected_h2("area")), 13)
        self.assertEqual(V.expected_h2("topic")[0], "1. 세 줄 요약")
        self.assertIsNone(V.expected_h2("topic", "index"))

    def test_tag_paren_regression(self):
        text = (FIX / "dr2_tag_paren_page.md").read_text(encoding="utf-8")
        errs = V.check_page("tracks/x/ontology-draft.md", text, strict_sections=False)
        self.assertTrue(any("괄호" in e for e in errs), errs)

    def test_status_line_detected(self):
        body = "[홈](../index.md) › x\n\n# t\n\n> 상태: draft · 신뢰도: medium\n"
        self.assertEqual(len(V.status_line_violations(body)), 1)
        ok = "# t\n\n<!-- auto:page-status:start -->\n상태: published\n<!-- auto:page-status:end -->\n"
        self.assertEqual(V.status_line_violations(ok), [])

    def test_footnote_without_definition(self):
        self.assertTrue(V.footnote_problems("문장 [사실][^ref-999]\n"))
        self.assertFalse(V.footnote_problems("문장 [사실][^ref-1]\n\n[^ref-1]: x\n"))
        self.assertFalse(V.footnote_problems("인라인 `[^ref-9]` 코드는 제외\n"))

    def test_h2_order_violation(self):
        text = AREA7.read_text(encoding="utf-8").replace("## 4. 핵심 개념과 용어", "## 4. 핵심 개념")
        errs = V.check_page(paths.area_rel_path(7), text)
        self.assertTrue(any("H2 절 제목" in e for e in errs))

    def test_apply_patches(self):
        new = V.apply_patches(AREA7.read_text(encoding="utf-8"),
                              [{"section": "11. 열린 질문", "action": "append", "content": "- 새 질문 [추정]"},
                               {"section": "6.", "action": "replace", "content": "교체 본문 [추정]"}])
        _, body = fm.parse(new)
        self.assertIn("- 새 질문 [추정]", body)
        self.assertIn("교체 본문 [추정]", body)
        self.assertEqual(V.h2_titles(body), V.h2_titles(fm.parse(AREA7.read_text(encoding="utf-8"))[1]))
        with self.assertRaises(ValueError):
            V.apply_patches(AREA7.read_text(encoding="utf-8"), [{"section": "99. 없음", "action": "replace", "content": "x"}])

    def test_complete_patched_page(self):
        prior = AREA7.read_text(encoding="utf-8")
        pv = int(fm.parse(prior)[0]["version"])
        new = V.apply_patches(prior, [{"section": "11. 열린 질문", "action": "append", "content": "- 질문 [추정][^ref-777]"}])
        ref = {"id": "ref-777", "org": "기관", "title": "제목", "published": None, "url": "https://example.org", "accessed": "2026-09-25",
               "fetched": False}
        out, notes = V.complete_patched_page(new, prior, "2026-09-30", {"ref-777": ref})
        meta, body = fm.parse(out)
        self.assertEqual(meta["version"], pv + 1)
        self.assertEqual(str(meta["updated"]), "2026-09-30")
        self.assertEqual(meta["status"], "draft")
        self.assertIn("[^ref-777]: 기관, 제목, 미확인, https://example.org, 접근일 2026-09-25 (원문 미열람)", body)
        self.assertFalse(V.footnote_problems(body))
        out2, _ = V.complete_patched_page(new, prior, "2026-09-30", {"ref-777": ref}, {"status": "needs_update"})
        self.assertEqual(fm.parse(out2)[0]["status"], fm.parse(new)[0]["status"])

    def test_split_oversized_area(self):
        long = "\n\n".join(f"긴 설명 문장 {i}번이다. [사실][^ref-003]" for i in range(120))
        text = _area_page({"6. 대표 접근법과 기술": long})
        new, topics = V.split_oversized_area(paths.area_repo_path(7), text, 4000,
                                             [{"path": paths.area_repo_path(7), "section": "6. 대표 접근법과 기술",
                                               "budget_chars": 800, "summary": "요약 문장이다. [사실][^ref-003]"}],
                                             "2026-09-25-99", "2026-09-26")
        self.assertEqual(len(topics), 1)
        self.assertIn("긴 설명 문장 0번이다. [사실][^ref-003]\n\n자세한 내용은", new)   # 원 절에는 그 절 첫 문장(outline summary 가 아님)
        self.assertNotIn("요약 문장이다", new)
        self.assertLessEqual(V.area_body_chars(fm.parse(new)[1]), 4000)
        t = topics[0]
        self.assertTrue(t["path"].startswith("docs/topics/2026/2026-09-26-area07-s6"))
        self.assertEqual(V.check_page(paths.docs_rel(t["path"]), t["content"]), [])
        self.assertIn("긴 설명 문장 119번이다", t["content"])
        self.assertEqual(V.footnote_problems(fm.parse(new)[1]), [])

    def test_split_name_collision_gets_suffix(self):
        text = _area_page({"6. 대표 접근법과 기술": "\n\n".join(f"긴 설명 문장 {i}번이다. [사실][^ref-003]" for i in range(250))})
        # 실제 docs/ 를 건드리지 않는다(배치 퍼블리셔가 docs 를 검사하는 중에 임시 파일이 생겼다 사라지면 게시가 실패한다).
        # 이름 충돌 검사는 paths.DOCS 기준이므로 임시 폴더로 바꿔 끼운다
        orig = paths.DOCS
        with tempfile.TemporaryDirectory() as td:
            taken = Path(td) / "topics" / "2099" / "2099-01-01-area07-s6.md"
            taken.parent.mkdir(parents=True)
            taken.write_text("x", encoding="utf-8")
            paths.DOCS = Path(td)
            try:
                _, topics = V.split_oversized_area(paths.area_repo_path(7), text, 4000, [], "2099-01-01-01", "2099-01-01")
            finally:
                paths.DOCS = orig
        self.assertEqual(topics[0]["path"], "docs/topics/2099/2099-01-01-area07-s6-2.md")

    def test_small_area_not_split(self):
        text = AREA7.read_text(encoding="utf-8")
        new, topics = V.split_oversized_area(paths.area_repo_path(7), text, 100000, [], "r", "2026-09-26")
        self.assertEqual(topics, [])
        self.assertEqual(new, text)


class TestRegressions(unittest.TestCase):
    def test_daily_log_footnote_neutralized(self):
        from lib.render import neutralize_footnotes
        text = (FIX / "dr1_daily_log_note.md").read_text(encoding="utf-8")
        out = neutralize_footnotes(text)
        self.assertEqual(V.footnote_problems(out), [])
        self.assertIn("`[^ref-013]`", out)

    def test_rolled_back_page_not_linked(self):
        import publish
        fx = json.loads((FIX / "dr1_rolled_back_page.json").read_text(encoding="utf-8"))
        cell = publish.daily_log_page_cell(fx["log_rel"], fx["path"], fx["title"])
        self.assertNotIn("](", cell)
        self.assertIn("미반영", cell)
        cell2 = publish.daily_log_page_cell(fx["log_rel"], paths.area_repo_path(7), "7")
        self.assertIn("](", cell2)

    def test_korean_anchor_and_explicit_id(self):
        import markdown
        from pymdownx.slugs import slugify
        md = markdown.Markdown(extensions=["toc", "attr_list"],
                               extension_configs={"toc": {"slugify": slugify(case="lower")}})
        html = md.convert((FIX / "dr1_korean_anchor.md").read_text(encoding="utf-8"))
        self.assertIn('id="5-현장-시나리오-물류-흐름의-어느-단계인지-명시"', html)
        self.assertIn('id="q1-01"', html)
        self.assertIn("pymdownx.slugs.slugify", (paths.ROOT / "mkdocs.yml").read_text(encoding="utf-8"))

    def test_anchored_link_rendered(self):
        from lib.render import _link
        out = _link("flow-matrix.md", paths.area_repo_path(7) + "#5-현장-시나리오", "7")
        self.assertIn("#5-현장-시나리오", out)
        self.assertIn("](", out)


class TestPublishHelpers(unittest.TestCase):
    def test_compute_ref_mapping(self):
        import publish
        existing = {"ref-044": "a.org/x", "ref-045": "b.org/y"}
        run = {"ref-044": "c.org/z", "ref-046": "b.org/y", "ref-047": "d.org/w"}
        m = publish.compute_ref_mapping(existing, run)
        self.assertEqual(m["ref-046"], "ref-045")      # 같은 URL → 기존 id 재사용
        self.assertEqual(m["ref-044"], "ref-048")      # id 충돌 → 다음 빈 번호
        self.assertNotIn("ref-047", m)

    def test_merge_three_clean_and_conflict(self):
        import publish
        base = "# t\n\n## 1. a\n\n가\n\n## 2. b\n\n나\n\n## 3. c\n\n다\n"
        ours = base.replace("가\n", "가 (이번 실행)\n")
        theirs = base.replace("다\n", "다 (다른 실행)\n")
        ok, merged = publish.merge_three(ours, base, theirs)
        self.assertTrue(ok)
        self.assertIn("가 (이번 실행)", merged)
        self.assertIn("다 (다른 실행)", merged)
        ok2, merged2 = publish.merge_three(base.replace("나\n", "나1\n"), base, base.replace("나\n", "나2\n"))
        self.assertFalse(ok2)
        self.assertIn("<<<<<<<", merged2)

    def test_ref_mapping_floor(self):
        import publish
        m = publish.compute_ref_mapping({"ref-001": "a.org"}, {"ref-001": "b.org"}, floor=150)
        self.assertEqual(m["ref-001"], "ref-151")      # 다른 실행이 예약한 구간(~ref-150) 위로 옮긴다

    def test_reserve_reference_block(self):
        orig = (runs.REF_BLOCK_FILE, runs.existing_reference_ids, runs.find_run_dir, runs.read_summary, runs.is_parked)
        with tempfile.TemporaryDirectory() as td:
            state = {"r1": {}, "r2": {}, "r3": {}}          # 실행별 summary(게시 여부)
            runs.REF_BLOCK_FILE = Path(td) / "blocks.json"
            runs.existing_reference_ids = lambda: ["ref-001", "ref-040"]
            runs.find_run_dir = lambda rid, settings=None: Path(td) / rid if rid in state else None
            runs.read_summary = lambda d: state.get(Path(d).name, {})
            runs.is_parked = lambda rid, settings=None: False
            try:
                a = runs.reserve_reference_block("r1", size=10)
                b = runs.reserve_reference_block("r2", size=10)
                again = runs.reserve_reference_block("r1", size=10)
                self.assertEqual(runs.active_reference_blocks(exclude="r1"), [(51, 60)])
                state["r1"] = {"published": True}             # 게시된 실행의 구간은 풀린다
                c = runs.reserve_reference_block("r3", size=10)
                self.assertEqual(runs.active_reference_blocks(exclude="r3"), [(51, 60)])
            finally:
                (runs.REF_BLOCK_FILE, runs.existing_reference_ids, runs.find_run_dir, runs.read_summary, runs.is_parked) = orig
        self.assertEqual(a, ("ref-041", "ref-050"))
        self.assertEqual(b, ("ref-051", "ref-060"))     # 겹치지 않는다
        self.assertEqual(again, a)                        # 같은 실행은 같은 구간
        self.assertEqual(c, ("ref-041", "ref-050"))     # 첫 맞춤: 풀린 구간(r1)을 다시 쓰고, 남은 예약(r2 51~60)과는 겹치지 않는다

    def test_compact_ref_mapping(self):
        import publish
        ex = {"ref-001": "a", "ref-002": "b", "ref-004": "d"}
        run = {"ref-150": "x", "ref-151": "y", "ref-152": "b", "ref-153": "z"}
        m = publish.compact_ref_mapping(ex, run, publish.compute_ref_mapping(ex, run), [(5, 6)])
        self.assertEqual(m, {"ref-152": "ref-002", "ref-150": "ref-003", "ref-151": "ref-007", "ref-153": "ref-008"})

    def _transition(self, slug: str, from_stage: int, to_stage: int, stages: int):
        """퍼블리셔 단계 전환(_transition_stage)을 임시 복사한 트랙 설정에 적용하고 결과 설정을 돌려준다."""
        import yaml

        import publish
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / f"{slug}.yaml"
            tmp.write_text(paths.track_config(slug).read_text(encoding="utf-8"), encoding="utf-8")
            pub = object.__new__(publish.Publisher)
            pub.notes, changes = [], []
            pub._changelog_item = lambda *a: changes.append(a)
            orig = paths.track_config
            paths.track_config = lambda s: tmp
            try:
                pub._transition_stage(slug, from_stage, to_stage, stages, "시험")
            finally:
                paths.track_config = orig
            return yaml.safe_load(tmp.read_text(encoding="utf-8")), pub, changes

    def test_stage_transition_advances_and_records(self):
        cfg, pub, changes = self._transition("nl-task-chatbot", 1, 2, 5)
        self.assertEqual(cfg["current_stage"], 2)
        self.assertEqual(cfg["stage_status"][1], "완료")
        self.assertEqual(cfg["stage_status"][2], "진행 중")
        self.assertIs(cfg["stage_completion"][1], True)
        self.assertNotEqual(cfg["status"], "done")
        self.assertTrue(pub.stage_transition_done)
        self.assertTrue(any("단계 1 → 단계 2" in n for n in pub.notes), pub.notes)
        self.assertEqual(len(changes), 1)

    def test_stage_transition_last_stage_marks_done(self):
        cfg, _, _ = self._transition("floorplan-recognition", 5, 6, 5)
        self.assertEqual(cfg["current_stage"], 5)
        self.assertEqual(cfg["status"], "done")
        self.assertEqual(cfg["stage_status"][5], "완료")


class TestPreviousResearch(unittest.TestCase):
    def test_same_target(self):
        import agent_runner as A
        def mk(td, name, t):
            d = Path(td) / name
            d.mkdir()
            (d / "target.json").write_text(json.dumps(t, ensure_ascii=False), encoding="utf-8")
            return d
        area4 = {"target": {"area_no": 4, "category_letter": "A"}, "track": None}
        with tempfile.TemporaryDirectory() as td:
            same = mk(td, "a", {"target": {"area_no": 4, "category_letter": "A"}})
            sibling = mk(td, "b", {"target": {"area_no": 1, "category_letter": "A"}})    # 같은 대분류의 다른 영역은 다른 대상
            track = mk(td, "c", {"target": {"area_no": 5}, "track": {"slug": "x"}})
            cat = mk(td, "d", {"target": {"area_no": None, "category_letter": "A"}})
            self.assertTrue(A._same_target(same, area4))
            self.assertFalse(A._same_target(sibling, area4))
            self.assertFalse(A._same_target(track, area4))
            self.assertFalse(A._same_target(cat, area4))
            self.assertTrue(A._same_target(cat, {"target": {"area_no": None, "category_letter": "A"}}))
            self.assertTrue(A._same_target(track, {"target": {"area_no": 13}, "track": {"slug": "x"}}))


class TestPromptSlimming(unittest.TestCase):
    def test_brief_digest(self):
        import agent_runner as A
        text = "# b\n\n## 발견 사항\n\n| f1 |\n\n### 근거 발췌\n\n긴 발췌\n\n## 출처\n\n| ref-1 |\n\n### 출처 요약\n\n요약\n\n## 페이지 제안\n\n제안\n"
        d = A._brief_digest(text)
        self.assertNotIn("긴 발췌", d)
        self.assertNotIn("요약\n\n## 페이지", d)
        self.assertIn("| f1 |", d)
        self.assertIn("| ref-1 |", d)
        self.assertIn("제안", d)

    def test_index_inputs_compact_for_area(self):
        import agent_runner as A
        out = A._index_inputs({"run_type": "area_deep_dive", "target": {"area_no": 7, "category_letter": "B"}}, None)
        labels = [l for l, _ in out]
        self.assertTrue(any(l.startswith("docs/references/index.md (요약") for l in labels))
        refs = dict(out)[labels[0]]
        self.assertIn("ref-022", refs)              # 7번 페이지가 인용한 출처
        full = A._index_inputs({"run_type": "weekly_review", "target": {}}, None)
        lab = [l for l, _ in full]
        self.assertTrue(any(l.startswith("docs/references/index.md (요약형 전체") for l in lab), lab)   # 주간·월간은 요약형 전체 목록(D-047)
        self.assertIn("docs/open-questions.md", lab)


class TestDailyLogLinks(unittest.TestCase):
    def test_fix_relative_links(self):
        from lib.render import fix_relative_links
        g = next(p for p in sorted((paths.DOCS / "glossary").glob("*.md")) if p.name != "index.md")
        txt = f"[용어](../glossary/{g.name}) · [없는 것](../glossary/zz-none.md) · [외부](https://example.org/a.md)"
        out = fix_relative_links(txt, "logs/daily/2026-09-25.md")
        self.assertIn(f"[용어](../../glossary/{g.name})", out)    # 일일 로그 기준 경로로 다시 씀
        self.assertIn("없는 것", out)
        self.assertNotIn("zz-none.md", out)                          # 찾지 못한 링크는 글자만 남김
        self.assertIn("(https://example.org/a.md)", out)


class TestRunIds(unittest.TestCase):
    def test_three_digit_run_numbers(self):
        self.assertTrue(runs.RUN_ID_RE.match("2026-09-25-100"))
        ids = ["2026-09-25-100", "2026-09-25-11", "2026-09-25-99", "2026-09-24-120"]
        self.assertEqual(sorted(ids, key=runs.run_id_key), ["2026-09-24-120", "2026-09-25-11", "2026-09-25-99", "2026-09-25-100"])
        import json as _j
        for f in ("research", "pages", "verification"):
            pat = _j.loads((paths.ROOT / "schemas" / f"{f}.schema.json").read_text(encoding="utf-8"))["properties"]["run_id"]["pattern"]
            import re as _re
            self.assertTrue(_re.match(pat, "2026-09-25-100"), f)


class TestSelection(unittest.TestCase):
    def test_weighted_track_pick(self):
        import select_target as S
        tracks = [("a", {}), ("b", {}), ("c", {})]
        hist = [{"run_type": "track", "track": "a", "published": True, "parked": False},
                {"run_type": "track", "track": "b", "published": True, "parked": False}]
        slug, _ = S.pick_track({"track_weights": {"a": 1, "b": 1, "c": 1}}, tracks, hist, None)
        self.assertEqual(slug, "c")
        slug, _ = S.pick_track({"track_weights": {"a": 3, "b": 1, "c": 0.5}}, tracks,
                               hist + [{"run_type": "track", "track": "c", "published": True, "parked": False}], None)
        self.assertEqual(slug, "a")

    def test_category_link_pick_none_while_seed_areas(self):
        import select_target as S
        statuses = {n: {"status": "seed"} for n in range(1, 29)}
        self.assertIsNone(S.category_link_pick(statuses))


class TestRunner(unittest.TestCase):
    def test_system_prompt_file_stable(self):
        import agent_runner as A
        p1, s1 = A.system_prompt_file("verifier")
        p2, s2 = A.system_prompt_file("verifier")
        self.assertEqual((p1, s1), (p2, s2))
        self.assertIn("shared-rules", "agents/shared-rules.md")
        cmd = A.claude_cmd({"model": "m"}, "verifier", {"type": "object"}, system_file=p1)
        self.assertIn("--append-system-prompt-file", cmd)
        up = A.build_prompt("verifier", {"run_id": "x"}, [("a.md", "b")])
        self.assertNotIn("# 에이전트 공통 규칙", up)

    def test_record_usage(self):
        import agent_runner as A
        with tempfile.TemporaryDirectory() as d:
            env = {"usage": {"input_tokens": 2, "cache_creation_input_tokens": 100, "cache_read_input_tokens": 50,
                             "output_tokens": 10}, "total_cost_usd": 0.5, "_elapsed_sec": 3}
            A.record_usage(Path(d), "research", "researcher", env)
            A.record_usage(Path(d), "verification1", "verifier", env)
            data = json.loads((Path(d) / "usage.json").read_text(encoding="utf-8"))
            self.assertEqual(data["total"]["calls"], 2)
            self.assertAlmostEqual(data["total"]["cost_usd"], 1.0)

    def test_semantic_content_or_patches(self):
        base = {"pages": [{"path": "docs/x.md", "action": "update", "status": "draft", "diff_summary": "d"}]}
        self.assertTrue(runs.semantic_checks("pages", base, "update", returned=True))
        ok = {"pages": [{"path": "docs/x.md", "action": "update", "status": "draft", "diff_summary": "d",
                         "patches": [{"section": "6.", "action": "replace", "content": "c"}]}]}
        self.assertFalse(runs.semantic_checks("pages", ok, "update", returned=True))


if __name__ == "__main__":
    unittest.main()
