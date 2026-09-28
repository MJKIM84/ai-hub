"""분류 원문 파서 단위 테스트 (표준 unittest).

실행: python3 -m unittest pipeline/checks/test_source.py
"""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import paths  # noqa: E402
from lib.source import load_source, mentioned_area_nos, parse  # noqa: E402
from lib.verbatim import strip_tags, tag_blocks  # noqa: E402

SRC = load_source()


class TestStructure(unittest.TestCase):
    """2026-09-28 개정 원문(17개 대분류·67개 세부영역) 기준."""

    def test_counts(self):
        self.assertEqual(len(SRC.categories), 17)
        self.assertEqual(len(SRC.areas), 67)
        self.assertEqual(sorted(SRC.areas), list(range(1, 68)))
        self.assertEqual(len(SRC.references), 10)
        self.assertEqual([r.n for r in SRC.references], list(range(1, 11)))
        self.assertEqual(sorted(SRC.chapters), list(range(1, 23)))
        self.assertEqual((SRC.scope_chapter, SRC.idea_chapter, SRC.method_chapter, SRC.refs_chapter), (19, 20, 21, 22))

    def test_category_titles_and_letters(self):
        self.assertEqual([c.letter for c in SRC.categories], list("ABCDEFGHIJKLMNOPQ"))
        self.assertEqual(paths.CATEGORY_LETTERS, list("ABCDEFGHIJKLMNOPQ"))
        for c in SRC.categories:
            self.assertEqual(c.title, f"{c.letter}. {c.name}")
            self.assertTrue(c.core_question.endswith("?"), c.core_question)
            self.assertTrue(c.intro_paragraph)
            lo, hi = paths.CATEGORY_AREA_RANGES[c.letter]
            self.assertEqual(c.area_nos, list(range(lo, hi + 1)))
            self.assertEqual(c.area_range, f"{lo}–{hi}" if hi > lo else f"{lo}")
            self.assertEqual(c.table_header, ["세부 연구영역", "무엇을 연구하는가", "핵심 질문"])
        # 필수 두 대분류는 이름을 줄이지 않는다
        self.assertEqual(SRC.category("B").title, "B. 로봇 온톨로지")
        self.assertEqual(SRC.category("C").title, "C. 채팅 기반 구성·운영")
        self.assertEqual([SRC.area(n).name for n in SRC.category("B").area_nos],
                         ["이기종 로봇 등록", "로봇 능력·작업 표현", "온톨로지 기반 시스템·로봇 연동", "온톨로지 검증·변경 관리"])
        self.assertEqual([SRC.area(n).name for n in SRC.category("C").area_nos],
                         ["채팅으로 맵 작성", "채팅으로 시나리오 구성", "채팅으로 로봇 구성",
                          "채팅으로 실제 상황 시뮬레이션 재현", "채팅으로 업무 지시·오케스트레이션", "대화형 기능의 신뢰·기반"])

    def test_area_title_format(self):
        for no, a in SRC.areas.items():
            self.assertEqual(a.no, no)
            self.assertRegex(a.title, r"^\d+\. .+$")
            self.assertEqual(a.title, f"{no}. {a.name}")
            self.assertEqual(a.title_cell, f"**{a.title}**")
            self.assertNotIn("**", a.title)
            self.assertTrue(a.what and a.question)
            self.assertTrue(a.question.endswith("?"), a.question)
            self.assertEqual(a.category_letter, paths.category_letter_of(no))
            self.assertIn(no, paths.AREA_SLUGS)
        self.assertEqual(SRC.area(17).title, "17. 작업 대상·자산 식별과 인계 추적")
        self.assertEqual(SRC.area(25).title, "25. 작업 배정 — MRTA")
        self.assertEqual(SRC.area(61).title, "61. 물류창고")

    def test_header_sentences(self):
        self.assertEqual(SRC.doc_title, "로봇 오케스트레이션 플랫폼 연구분야")
        self.assertTrue(SRC.rop_definition_sentence.startswith("ROP는 **"))
        self.assertTrue(SRC.rop_definition_sentence.endswith("플랫폼**으로 볼 수 있다."))
        self.assertTrue(SRC.scope_disclaimer_sentence.startswith("공식 단일 분류가 아니라"))
        self.assertTrue(SRC.scope_disclaimer_sentence.endswith("의미는 아니다."))
        self.assertEqual(SRC.scor_paragraph, "")
        for word in ("SCM", "공급망 관점"):
            self.assertNotIn(word, SRC.raw.split("## 22.")[0], word)

    def test_overview_table(self):
        self.assertEqual(SRC.overview_table_header, ["대분류", "핵심 질문", "세부영역"])
        self.assertEqual(len(SRC.overview_table_rows), 17)
        self.assertEqual(SRC.overview_table_rows[0]["category_title"], "A. 기획·사업")
        self.assertEqual(SRC.overview_table_rows[-1]["area_range"], "61–67")

    def test_scope_and_idea_tables(self):
        self.assertEqual(len(SRC.scope_rows), 5)
        self.assertEqual(SRC.scope_rows[0]["경계"], "**상위 업무 시스템**")
        self.assertEqual(SRC.scope_table_header, ["경계", "ROP에서 다룰 내용", "주로 연계할 외부 영역"])
        self.assertEqual([r["idea"] for r in SRC.idea_rows],
                         ["로봇 기능 온톨로지", "채팅 기반 구성·운영", "건축 도면 자동 인식", "로봇과 건물 조건을 함께 판단"])
        self.assertEqual(SRC.idea_table_header, ["아이디어", "중심 연구영역", "함께 필요한 영역"])

    def test_references(self):
        r1 = SRC.reference(1)
        self.assertEqual((r1.id, r1.org, r1.title), ("ref-001", "ASCM", "SCOR Digital Standard"))
        self.assertEqual(r1.url, "https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/")
        self.assertIsNone(r1.year)
        self.assertEqual(r1.published, "미확인")
        self.assertEqual(SRC.reference(2).year, 2025)
        self.assertEqual(SRC.reference(5).year, 2020)
        self.assertEqual(SRC.reference(6).year, 2017)
        self.assertEqual(SRC.reference(3).org, "GS1")
        self.assertTrue(SRC.reference(5).org.endswith("& Koenig, S."))
        self.assertEqual(SRC.reference(10).org, "ROS 2 Design")
        for r in SRC.references:
            self.assertTrue(r.note.endswith("."), r.note)
            self.assertIn(r.raw, SRC.chapter_text(SRC.refs_chapter))
        self.assertTrue(SRC.references_intro.startswith("아래는 분류 해설에서"))

    def test_old_source_archive_still_parses(self):
        """보관한 개정 전 원문([옛 분류원문] 대조용)은 같은 파서로 7개 대분류·28개 영역으로 읽힌다."""
        old = parse(paths.OLD_SOURCE_FILE.read_text(encoding="utf-8"), paths.OLD_SOURCE_FILE)
        self.assertEqual((len(old.categories), len(old.areas)), (7, 28))
        self.assertEqual((old.scope_chapter, old.idea_chapter, old.method_chapter, old.refs_chapter), (9, 10, 11, 12))
        self.assertEqual(old.area(7).title, "7. 화물·재고·자산 식별과 추적")


class TestNotesMapping(unittest.TestCase):
    EXPECTED = {
        "채팅 기능은 대화가 부르는 엔진과": [14, 15, 33, 36, 5, 25, 26],
        "지도는 한 번 만들고 끝나지 않는다": [14, 15, 16],
        "**17번은 특히 빠뜨리기 쉽다.**": [17],
        "30번의 협업은": [30],
        "18번의 실시간 모델이": [18, 34],
        "AI는 특정 기능 하나에만": [4, 55, 14, 25, 38],
    }

    def test_mentioned_area_nos(self):
        self.assertEqual(mentioned_area_nos("매뉴얼 해석은 4·55번, 도면 해석은 14번"), [4, 55, 14])
        self.assertEqual(mentioned_area_nos("30초 전이라면"), [])

    def test_note_paragraph_mapping(self):
        found = {}
        for cat in SRC.categories:
            for para in cat.notes:
                nos = mentioned_area_nos(para)
                for prefix, expected in self.EXPECTED.items():
                    if para.startswith(prefix):
                        found[prefix] = nos
                        self.assertEqual(nos, expected, para)
                if not any(para.startswith(p) for p in self.EXPECTED):
                    self.assertEqual(nos, [], f"예상 밖의 세부영역 언급: {para!r}")
        self.assertEqual(set(found), set(self.EXPECTED))

    def test_area_notes(self):
        self.assertEqual(len(SRC.area_notes(17)), 1)
        self.assertTrue(SRC.area_notes(17)[0].startswith("**17번은"))
        self.assertIn("[3]", SRC.area_notes(17)[0])
        self.assertEqual(len(SRC.area_notes(14)), 3)
        self.assertEqual(len(SRC.area_notes(25)), 2)
        for no in (1, 2, 3, 8, 13, 61, 67):
            self.assertEqual(SRC.area_notes(no), [], no)
        rest = SRC.notes_without_area()
        self.assertEqual(len(rest["F"]), 2)
        self.assertEqual(len(rest["D"]), 0)

    def test_citations(self):
        self.assertEqual(SRC.citations(SRC.chapter_text(8)), [5, 6])     # G. 계획·최적화
        self.assertEqual(SRC.citations(SRC.chapter_text(15)), [9, 10])   # N. 보안·개인정보
        self.assertEqual(SRC.citations(SRC.chapter_text(1)), [])
        self.assertEqual(SRC.citations("[^ref-003] 와 [3]"), [3])


class TestVerbatim(unittest.TestCase):
    def test_chapter_text_is_verbatim(self):
        for n in range(1, 23):
            self.assertIn(SRC.chapter_text(n), SRC.raw)

    def test_tag_roundtrip(self):
        for n in (1, SRC.scope_chapter, SRC.idea_chapter, SRC.method_chapter):
            text = SRC.chapter_text(n)
            tagged = tag_blocks(text)
            self.assertIn("[분류원문]", tagged)
            self.assertEqual(strip_tags(tagged).strip("\n"), text)
            for line in text.split("\n"):
                if line.strip():
                    self.assertIn(line, strip_tags(tagged).split("\n"))


if __name__ == "__main__":
    unittest.main()
