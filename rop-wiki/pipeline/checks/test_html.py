"""lib/htmlcheck 단위 테스트 (공개 배포 보안 보강 1항). 실행: python3 -m unittest pipeline/checks/test_html.py"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import htmlcheck  # noqa: E402
from lib.render import _esc  # noqa: E402


class TestFindUnsafeHtml(unittest.TestCase):
    def test_allowed_passes(self):
        text = "본문<br>줄바꿈 <br/> 링크 <https://example.org/a?b=1> <mailto:x@example.invalid>\n<!-- auto:changelog:start -->\n"
        self.assertEqual(htmlcheck.find_unsafe_html(text), [])

    def test_code_is_skipped(self):
        text = "```html\n<script>alert(1)</script>\n```\n인라인 `<iframe src=x>` 도 검사 안 함\n"
        self.assertEqual(htmlcheck.find_unsafe_html(text), [])

    def test_script_and_iframe_flagged_with_line(self):
        text = "첫 줄\n둘째 <script>alert(1)</script>\n셋째 <iframe src=\"//evil\"></iframe>\n"
        errs = htmlcheck.find_unsafe_html(text)
        self.assertTrue(any(e.startswith("줄 2:") and "script" in e for e in errs), errs)
        self.assertTrue(any(e.startswith("줄 3:") and "iframe" in e for e in errs), errs)

    def test_event_attr_and_attrs_on_br(self):
        self.assertTrue(htmlcheck.find_unsafe_html("<br onload=alert(1)>"))
        self.assertTrue(htmlcheck.find_unsafe_html("<br class=x>"))

    def test_dangerous_link_schemes(self):
        self.assertTrue(htmlcheck.find_unsafe_html("[x](javascript:alert(1))"))
        self.assertTrue(htmlcheck.find_unsafe_html("[x](JavaScript:alert(1))"))
        self.assertTrue(htmlcheck.find_unsafe_html("[x](data:text/html;base64,AAAA)"))
        self.assertEqual(htmlcheck.find_unsafe_html("[x](https://example.org) [y](../a.md#s) [z](mailto:a@b.c)"), [])

    def test_prose_angle_brackets_not_tags(self):
        # "a < b" 같은 부등호, 수식은 태그가 아니다
        self.assertEqual(htmlcheck.find_unsafe_html("a < b 이고 x > y, 3 <4"), [])


class TestEscapeTags(unittest.TestCase):
    def test_keeps_allowed_and_autolinks(self):
        s = "A<br>B <https://example.org/x> C"
        self.assertEqual(htmlcheck.escape_tags(s), s)

    def test_escapes_other_tags(self):
        self.assertEqual(htmlcheck.escape_tags("<script>x</script>"), "&lt;script>x&lt;/script>")
        self.assertEqual(htmlcheck.escape_tags("<b onclick=1>"), "&lt;b onclick=1>")

    def test_table_cell_esc_uses_it(self):
        self.assertIn("&lt;img", _esc("사유: <img src=x onerror=alert(1)>"))
        self.assertIn("<https://example.org>", _esc("출처 <https://example.org>"))


if __name__ == "__main__":
    unittest.main()
