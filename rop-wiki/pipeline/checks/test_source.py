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
from lib.source import load_source, mentioned_area_nos  # noqa: E402
from lib.verbatim import strip_tags, tag_blocks  # noqa: E402

SRC = load_source()


class TestStructure(unittest.TestCase):
    def test_counts(self):
        self.assertEqual(len(SRC.categories), 7)
        self.assertEqual(len(SRC.areas), 28)
        self.assertEqual(sorted(SRC.areas), list(range(1, 29)))
        self.assertEqual(len(SRC.references), 10)
        self.assertEqual([r.n for r in SRC.references], list(range(1, 11)))
        self.assertEqual(sorted(SRC.chapters), list(range(1, 13)))

    def test_category_titles_and_letters(self):
        self.assertEqual([c.letter for c in SRC.categories], list("ABCDEFG"))
        for c in SRC.categories:
            self.assertEqual(c.title, f"{c.letter}. {c.name}")
            self.assertTrue(c.core_question.endswith("?"), c.core_question)
            self.assertTrue(c.intro_paragraph)
            self.assertEqual(len(c.table_rows), 4)
            lo, hi = paths.CATEGORY_AREA_RANGES[c.letter]
            self.assertEqual(c.area_nos, list(range(lo, hi + 1)))
            self.assertEqual(c.area_range, f"{lo}–{hi}")
            self.assertEqual(c.table_header, ["세부 연구영역", "무엇을 연구하는가", "SCM 관점의 질문"])
        self.assertEqual(SRC.category("B").title, "B. 공통 정보·환경 모델")
        self.assertEqual(SRC.category("B").core_question, "로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가?")

    def test_area_title_format(self):
        for no, a in SRC.areas.items():
            self.assertEqual(a.no, no)
            self.assertRegex(a.title, r"^\d+\. .+$")
            self.assertEqual(a.title, f"{no}. {a.name}")
            self.assertEqual(a.title_cell, f"**{a.title}**")
            self.assertNotIn("**", a.title)
            self.assertTrue(a.what and a.question)
            self.assertEqual(a.category_letter, paths.category_letter_of(no))
        self.assertEqual(SRC.area(7).title, "7. 화물·재고·자산 식별과 추적")
        self.assertEqual(SRC.area(7).what, "제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결")
        self.assertEqual(SRC.area(7).question, "로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가?")
        self.assertEqual(SRC.area(13).title, "13. 작업 배정 — MRTA")

    def test_header_sentences(self):
        self.assertEqual(SRC.doc_title, "SCM 관점의 로봇 오케스트레이션 플랫폼 연구분야")
        self.assertTrue(SRC.rop_definition_sentence.startswith("SCM 관점에서 ROP는 **"))
        self.assertTrue(SRC.rop_definition_sentence.endswith("실행 플랫폼**으로 볼 수 있다."))
        self.assertEqual(
            SRC.scope_disclaimer_sentence,
            "공식 단일 분류가 아니라 공급망 프레임워크·로봇 연구·실제 플랫폼 구조를 종합한 연구 범위 점검용 분류이며, 모든 항목을 직접 개발한다는 의미는 아니다.",
        )
        self.assertTrue(SRC.scor_paragraph.startswith("ASCM의 SCOR는"))
        self.assertTrue(SRC.scor_paragraph.endswith("[1]"))

    def test_overview_table(self):
        self.assertEqual(SRC.overview_table_header, ["대분류", "핵심 질문", "세부영역"])
        self.assertEqual(len(SRC.overview_table_rows), 7)
        self.assertEqual(SRC.overview_table_rows[0]["category_title"], "A. 업무·공급망 설계")
        self.assertEqual(SRC.overview_table_rows[6]["area_range"], "25–28")

    def test_scope_and_idea_tables(self):
        self.assertEqual(len(SRC.scope_rows), 5)
        self.assertEqual(SRC.scope_rows[0]["경계"], "**상위 업무 시스템**")
        self.assertEqual(SRC.scope_table_header, ["경계", "ROP에서 다룰 내용", "주로 연계할 외부 영역"])
        self.assertEqual(len(SRC.idea_rows), 4)
        self.assertEqual(SRC.idea_rows[0]["idea"], "매뉴얼 기반 로봇 온톨로지")
        self.assertEqual(SRC.idea_table_header, ["아이디어", "중심 연구영역", "함께 필요한 영역"])

    def test_references(self):
        r1 = SRC.reference(1)
        self.assertEqual((r1.id, r1.org, r1.title), ("ref-001", "ASCM", "SCOR Digital Standard"))
        self.assertEqual(r1.url, "https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/")
        self.assertEqual(r1.note, "공급망 프로세스 범위 참고.")
        self.assertIsNone(r1.year)
        self.assertEqual(r1.published, "미확인")
        self.assertEqual(SRC.reference(2).year, 2025)
        self.assertEqual(SRC.reference(5).year, 2020)
        self.assertEqual(SRC.reference(6).year, 2017)
        self.assertEqual(SRC.reference(3).org, "GS1")
        self.assertTrue(SRC.reference(5).org.endswith("& Koenig, S."))
        self.assertEqual(SRC.reference(10).org, "ROS 2 Design")
        self.assertEqual(SRC.reference(10).url, "https://design.ros2.org/articles/ros2_threat_model.html")
        for r in SRC.references:
            self.assertTrue(r.note.endswith("."), r.note)
            self.assertIn(r.raw, SRC.chapter_text(12))
        self.assertTrue(SRC.references_intro.startswith("아래는 앞선 답변에서"))
        self.assertEqual(
            r1.footnote("2026-09-24"),
            "[^ref-001]: ASCM, SCOR Digital Standard, 미확인, https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/, 접근일 2026-09-24",
        )


class TestNotesMapping(unittest.TestCase):
    EXPECTED = {
        "**7번은 SCM 관점에서": [7],
        "6번에는 지도 생성뿐": [6],
        "17번의 협업은": [17],
        "8번의 실시간 모델이": [8, 22],
        "27번의 AI는": [27, 5, 21, 6, 13, 19],
    }

    def test_mentioned_area_nos(self):
        self.assertEqual(mentioned_area_nos("매뉴얼 해석은 5·21번, 도면 해석은 6번"), [5, 21, 6])
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
        self.assertEqual(len(SRC.area_notes(7)), 1)
        self.assertTrue(SRC.area_notes(7)[0].startswith("**7번은"))
        self.assertIn("[3]", SRC.area_notes(7)[0])
        self.assertEqual(len(SRC.area_notes(6)), 2)   # "6번에는 …" + "27번의 AI는 … 6번 …"
        self.assertEqual(len(SRC.area_notes(22)), 1)
        self.assertEqual(len(SRC.area_notes(8)), 1)
        self.assertEqual(len(SRC.area_notes(27)), 1)
        for no in (5, 21, 13, 19):
            self.assertEqual(len(SRC.area_notes(no)), 1, no)
        for no in (1, 2, 3, 4, 9, 10, 11, 12, 14, 15, 16, 18, 20, 23, 24, 25, 26, 28):
            self.assertEqual(SRC.area_notes(no), [], no)
        # 세부영역을 명시하지 않는 문단은 대분류 핵심 포인트에만 남는다
        rest = SRC.notes_without_area()
        self.assertEqual(len(rest["A"]), 2)
        self.assertEqual(len(rest["B"]), 0)
        self.assertEqual(len(rest["C"]), 1)
        self.assertEqual(len(rest["D"]), 1)
        self.assertEqual(len(rest["G"]), 1)

    def test_citations(self):
        self.assertEqual(SRC.citations(SRC.chapter_text(5)), [5, 6])
        self.assertEqual(SRC.citations(SRC.chapter_text(8)), [9, 10])
        self.assertEqual(SRC.citations(SRC.chapter_text(1)), [1])
        self.assertEqual(SRC.citations("[^ref-003] 와 [3]"), [3])


class TestVerbatim(unittest.TestCase):
    def test_chapter_text_is_verbatim(self):
        for n in range(1, 13):
            self.assertIn(SRC.chapter_text(n), SRC.raw)

    def test_tag_roundtrip(self):
        for n in (1, 9, 10, 11):
            text = SRC.chapter_text(n)
            tagged = tag_blocks(text)
            self.assertIn("[분류원문]", tagged)
            self.assertEqual(strip_tags(tagged).strip("\n"), text)
            for line in text.split("\n"):
                if line.strip():
                    self.assertIn(line, strip_tags(tagged).split("\n"))


if __name__ == "__main__":
    unittest.main()
