"""백본 라이브러리(paths, frontmatter, autoregion, nav, render) 단위 테스트.

실행: python3 -m unittest pipeline/checks/test_lib.py
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import autoregion as ar  # noqa: E402
from lib import frontmatter as fm  # noqa: E402
from lib import paths  # noqa: E402
from lib.korean import topic_particle  # noqa: E402
from lib.nav import _title, build_nav, flatten_nav, load_mkdocs_yml, mkdocs_yml_is_current, render_mkdocs_yml  # noqa: E402
from lib.render import load_track_config, render_flow_matrix, render_for, track_slugs  # noqa: E402


def _load_script(name: str):
    """pipeline/<name>.py 또는 pipeline/checks/<name>.py 를 모듈로 읽는다(검사 스크립트는 패키지가 아니다)."""
    import importlib.util
    base = Path(__file__).resolve().parents[1]
    path = base / f"{name}.py" if (base / f"{name}.py").is_file() else base / "checks" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestPaths(unittest.TestCase):
    def test_root_and_slugs(self):
        self.assertTrue((paths.ROOT / "_source").is_dir())
        self.assertEqual(len(paths.AREA_SLUGS), 28)
        self.assertEqual(len(paths.CATEGORY_SLUGS), 7)
        self.assertEqual(paths.category_letter_of(7), "B")
        self.assertEqual(paths.area_rel_path(7),
                         "categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md")
        self.assertEqual(paths.area_repo_path(1), "docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md")
        self.assertEqual(paths.docs_rel("docs/index.md"), "index.md")
        for no, slug in paths.AREA_SLUGS.items():
            self.assertTrue(slug.startswith(f"{no:02d}-"))

    def test_rel_link(self):
        self.assertEqual(paths.rel_link("index.md", "about/what-is-rop.md"), "about/what-is-rop.md")
        self.assertEqual(paths.rel_link("categories/b-x/07-y.md", "references/ref-003.md"), "../../references/ref-003.md")
        self.assertEqual(paths.rel_link("tracks/t/index.md", "categories/b-x/05-y.md"), "../../categories/b-x/05-y.md")
        self.assertEqual(paths.rel_link("categories/b-x/07-y.md", "categories/b-x/index.md"), "index.md")


class TestFrontmatter(unittest.TestCase):
    def test_roundtrip(self):
        meta = {"title": "7. 화물·재고·자산 식별과 추적", "type": "area", "category": "B. 공통 정보·환경 모델",
                "area_no": 7, "related_areas": [8, 12], "tags": ["EPCIS"], "status": "seed",
                "created": "2026-09-24", "updated": "2026-09-24", "version": 1}
        text = fm.dumps(meta, "본문\n")
        self.assertIn('title: "7. 화물·재고·자산 식별과 추적"', text)
        self.assertIn("created: 2026-09-24", text)
        self.assertIn("related_areas: [8, 12]", text)
        back, body = fm.parse(text)
        self.assertEqual(back, meta)
        self.assertEqual(body.strip(), "본문")
        self.assertEqual(fm.validate(back), [])

    def test_validate(self):
        errs = fm.validate({"title": "x", "type": "nope", "status": "bad", "created": "2026/09/24"})
        self.assertTrue(any("type 값 오류" in e for e in errs))
        self.assertTrue(any("status 값 오류" in e for e in errs))
        self.assertTrue(any("created" in e for e in errs))
        self.assertTrue(any("updated" in e for e in errs))
        errs = fm.validate({"title": "x", "type": "topic", "status": "draft", "created": "2026-09-24",
                            "updated": "2026-09-24", "version": 1})
        self.assertTrue(any("primary_area_no" in e for e in errs))
        self.assertEqual(fm.validate({"title": "x", "type": "topic", "subtype": "index", "status": "published",
                                      "created": "2026-09-24", "updated": "2026-09-24", "version": 1}), [])


class TestAutoregion(unittest.TestCase):
    def test_wrap_get_replace(self):
        text = "앞\n\n" + ar.wrap("home-recent", "옛 내용") + "\n\n뒤\n"
        self.assertEqual(ar.get_region(text, "home-recent"), "옛 내용")
        self.assertEqual(ar.list_regions(text), ["home-recent"])
        new = ar.replace_region(text, "home-recent", "- 새 항목 \\1 백슬래시")
        self.assertIn("- 새 항목 \\1 백슬래시", new)
        self.assertTrue(new.startswith("앞\n\n<!-- auto:home-recent:start -->\n"))
        self.assertTrue(new.endswith("<!-- auto:home-recent:end -->\n\n뒤\n"))
        self.assertIsNone(ar.get_region(text, "metrics"))
        with self.assertRaises(KeyError):
            ar.replace_region(text, "metrics", "x")
        self.assertEqual(ar.wrap("k"), "<!-- auto:k:start -->\n<!-- auto:k:end -->")


class TestVerbatimChecks(unittest.TestCase):
    def test_tagged_text_strips_only_structure(self):
        """태그 줄 대조는 구조 표식(들여쓰기·인용 표식·태그 뒤 각주·"원문 주석: " 라벨)만 벗기고 본문은 그대로 둔다."""
        ps = _load_script("protect_source")
        q = "로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가?"
        self.assertEqual(ps.tagged_text(f"    {q} [분류원문]"), q)
        self.assertEqual(ps.tagged_text(f"> {q} [분류원문][^ref-003][^ref-004]"), q)
        self.assertEqual(ps.tagged_text(f"> 원문 주석: {q} [분류원문]"), q)
        self.assertEqual(ps.tagged_text(f"핵심 질문: {q} [분류원문]"), f"핵심 질문: {q}")   # 위키 문구는 벗기지 않는다
        self.assertIsNone(ps.tagged_text("[분류원문]"))          # 표 아래 단독 태그 줄
        self.assertIsNone(ps.tagged_text(f"{q} [사실][^ref-003]"))
        allowed = ps._source_lines_and_cells()
        self.assertIn(q, allowed)
        self.assertNotIn(f"핵심 질문: {q}", allowed)

    def test_reference_reliability_cap(self):
        """원문 미열람 출처는 유형 기준이 high 라도 medium 상한, URL 열림이 확인되면 유형 기준값."""
        sc = _load_script("scaffold")
        unverified = sc.ref_access("표준", None, None)
        self.assertEqual((unverified["reliability"], unverified["by_type"], unverified["verified"]), ("medium", "high", False))
        self.assertIn("원문 미열람", unverified["access_cell"])
        verified = sc.ref_access("표준", "2026-09-25", {"result": "열림"})
        self.assertEqual((verified["reliability"], verified["verified"]), ("high", True))
        self.assertEqual(sc.ref_access("기사", "2026-09-25", {"result": "열림"})["reliability"], "medium")
        self.assertEqual(sc.ref_access("논문", "2026-09-25", {"result": "오류"})["reliability"], "medium")


class TestKorean(unittest.TestCase):
    def test_topic_particle(self):
        expected = {1: "은", 2: "는", 3: "은", 4: "는", 5: "는", 6: "은", 7: "은", 8: "은", 9: "는", 10: "은",
                    11: "은", 12: "는", 20: "은", 24: "는"}
        for n, josa in expected.items():
            self.assertEqual(topic_particle(n), josa, n)


class TestNavAndRender(unittest.TestCase):
    CATEGORY_TITLES = ["A. 업무·공급망 설계", "B. 공통 정보·환경 모델", "C. 연결·실행 기반", "D. 계획·최적화",
                       "E. 협업·현장 운영", "F. 도입·검증·유지관리", "G. 안전·보안·지능·거버넌스"]

    def test_nav_order_and_labels(self):
        """사양서 4.8 의 상위 순서 전체: 홈 → 소개 → 대분류 A~G → 중점 연구 트랙 → 주제 → 용어집 → 참고문헌 →
        표준·프레임워크 → 열린 질문 → 흐름 매트릭스 → 변경 이력 → 운영 지표 → 로그.
        4.8 목록에 없는 "정정 요청 안내"는 그 순서를 끊지 않도록 맨 뒤(로그 다음)에 온다. [가정]"""
        nav = build_nav()
        top = [next(iter(i)) if isinstance(i, dict) else i for i in nav]
        docs = paths.DOCS
        expected = ["홈", "소개", *self.CATEGORY_TITLES]
        if (docs / "tracks").is_dir() and any(p.is_dir() for p in (docs / "tracks").iterdir()):
            expected.append("중점 연구 트랙")
        if (docs / "topics").is_dir():
            expected.append("주제")
        for rel in ("glossary/index.md", "references/index.md", "standards/index.md", "open-questions.md",
                    "flow-matrix.md", "changelog.md", "metrics.md"):
            if (docs / rel).is_file():
                expected.append(_title(rel))
        if (docs / "logs").is_dir():
            expected.append("로그")
        if (docs / "corrections.md").is_file():
            expected.append(_title("corrections.md"))
        self.assertEqual(top, expected)
        # 4.8 의 "운영 지표 → 로그" 인접 순서가 끊기지 않는다
        if "로그" in top and _title("metrics.md") in top:
            self.assertEqual(top.index("로그"), top.index(_title("metrics.md")) + 1)
        pairs = dict((p, l) for l, p in flatten_nav(nav))
        self.assertEqual(pairs.get(paths.area_rel_path(13)), "13. 작업 배정 — MRTA")
        for letter, title in zip(paths.CATEGORY_LETTERS, self.CATEGORY_TITLES):
            self.assertEqual(pairs.get(paths.category_index_rel(letter)), title)
        # 소개 하위 7개는 4.2 표 순서
        about = next(v for i in nav if isinstance(i, dict) for k, v in i.items() if k == "소개")
        about_paths = [next(iter(p.values())) for p in about]
        present = [f"about/{n}.md" for n in paths.ABOUT_ORDER if (docs / f"about/{n}.md").is_file()]
        self.assertEqual(about_paths[:len(present)], present)
        text = render_mkdocs_yml(nav)
        self.assertIn("!!python/name:pymdownx.superfences.fence_code_format", text)
        self.assertIn("  - 홈: index.md", text)
        self.assertIn("omitted_files: warn", text)

    def test_nav_track_children_order(self):
        """트랙 하위: 개요 → 단계 1~7 → 온톨로지 초안 → 비교표·매트릭스·평가 절차 → 질문 백로그 → 로그 → 실험."""
        slugs = [p.name for p in sorted((paths.DOCS / "tracks").iterdir()) if p.is_dir()] if (paths.DOCS / "tracks").is_dir() else []
        if not slugs:
            self.skipTest("트랙 페이지 없음")
        nav = build_nav()
        tracks = next(v for i in nav if isinstance(i, dict) for k, v in i.items() if k == "중점 연구 트랙")
        slug = slugs[0]
        section = next(v for i in tracks for k, v in i.items())
        got = [p for l, p in flatten_nav(section if isinstance(section, list) else [section])]
        prefix = f"tracks/{slug}/"
        names = [p[len(prefix):] for p in got if p.startswith(prefix)]
        stage_names = [n for n in names if n.startswith("stage-")]
        expected = ["index.md", *stage_names, *paths.TRACK_PAGE_ORDER[1:]]
        expected = [n for n in expected if (paths.DOCS / prefix / n).is_file()]
        self.assertEqual(names[:len(expected)], expected)
        self.assertEqual([int(n.split("-")[1]) for n in stage_names], sorted(int(n.split("-")[1]) for n in stage_names))

    def test_load_mkdocs_yml(self):
        if not paths.MKDOCS_YML.exists():
            self.skipTest("mkdocs.yml 없음")
        cfg = load_mkdocs_yml()
        self.assertEqual(cfg["site_name"], "ROP 연구 위키")
        self.assertIn("nav", cfg)
        self.assertTrue(mkdocs_yml_is_current(),
                        "mkdocs.yml 이 현재 페이지 기준 생성 결과와 다르다: python3 pipeline/scaffold.py --refresh-auto")

    def test_track_render_links_and_stage_names(self):
        slugs = [s for s in track_slugs() if load_track_config(s)]
        if not slugs:
            self.skipTest("트랙 정의 없음")
        slug = slugs[0]
        page_rel = f"tracks/{slug}/index.md"
        progress = render_for("track-progress", page_rel, {"track": slug, "type": "track"})
        self.assertIsInstance(progress, str)
        rows = [l for l in progress.split("\n") if l.startswith("| ") and not l.startswith("| 단계 |")]
        self.assertTrue(rows)
        self.assertTrue(all("](" in r for r in rows), "단계 열이 단계 페이지 링크여야 한다")
        self.assertTrue(all(r.split("|")[1].strip().startswith("[단계 ") for r in rows), "단계는 번호와 이름을 함께 쓴다")
        home = render_for("home-track-status", "index.md", {"type": "home"})
        self.assertIn("| 트랙 |", home)
        self.assertIn("[단계 ", home)
        self.assertIn(f"tracks/{slug}/index.md", home)

    def test_reference_cited_pages(self):
        if not (paths.DOCS / "references" / "ref-002.md").is_file():
            self.skipTest("ref-002 없음")
        out = render_for("reference-cited-pages", "references/ref-002.md", {"ref_id": "ref-002"})
        self.assertIsInstance(out, str)
        self.assertIn(paths.category_index_rel("A").split("/")[-2], out)   # A 대분류 핵심 포인트가 [2] 를 인용
        self.assertNotIn("references/index.md", out)

    def test_render(self):
        m = render_flow_matrix()
        rows = [l for l in m.split("\n") if l.startswith("| **")]
        self.assertEqual(len(rows), 7)
        cells = [c.strip() for r in rows for c in r.strip().strip("|").split("|")[1:]]
        self.assertEqual(len(cells), 42)
        self.assertTrue(all(c == "비어 있음" or "](" in c for c in cells))
        self.assertIn("| **입고** |", m)
        self.assertIsNone(render_for("unknown-key", "index.md", {}))
        self.assertIsInstance(render_for("metrics", "metrics.md", {}), str)


if __name__ == "__main__":
    unittest.main()
