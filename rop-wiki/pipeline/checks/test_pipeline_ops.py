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

    def test_split_oversized_area(self):
        long = "\n\n".join(f"긴 설명 문장 {i}번이다. [사실][^ref-003]" for i in range(120))
        text = _area_page({"6. 대표 접근법과 기술": long})
        new, topics = V.split_oversized_area(paths.area_repo_path(7), text, 4000,
                                             [{"path": paths.area_repo_path(7), "section": "6. 대표 접근법과 기술",
                                               "budget_chars": 800, "summary": "요약 문장이다. [사실][^ref-003]"}],
                                             "2026-09-25-99", "2026-09-26")
        self.assertEqual(len(topics), 1)
        self.assertIn("요약 문장이다", new)
        self.assertLessEqual(V.area_body_chars(fm.parse(new)[1]), 4000)
        t = topics[0]
        self.assertTrue(t["path"].startswith("docs/topics/2026/2026-09-26-area07-s6"))
        self.assertEqual(V.check_page(paths.docs_rel(t["path"]), t["content"]), [])
        self.assertIn("긴 설명 문장 119번이다", t["content"])
        self.assertEqual(V.footnote_problems(fm.parse(new)[1]), [])

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
