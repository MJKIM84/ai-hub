"""출처 원문 처리(pipeline/lib/sources.py, pipeline/ingest_sources.py, pipeline/checks/check_urls.py) 단위 테스트.

실행: python3 -m unittest pipeline/checks/test_sources.py
네트워크를 쓰지 않는다(URL 확인은 가짜 urlopen 으로 흉내 낸다). 파일은 임시 폴더에만 만든다.
"""
from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import unittest
import urllib.error
from email.message import Message
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import frontmatter as fm  # noqa: E402
from lib import sources as S  # noqa: E402


def _load_script(name: str):
    base = Path(__file__).resolve().parents[1]
    path = base / f"{name}.py" if (base / f"{name}.py").is_file() else base / "checks" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(f"_t_{name}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


MIRRORS_YAML = """
version: 1
mirrors:
- name: 책 전체
  match: https://books.example.org/guide
  raw_urls: [https://raw.githubusercontent.com/ex/guide/main/src/SUMMARY.md]
  repo: ex/guide
  relation: original
- name: 책 한 장
  match: https://books.example.org/guide/chapter-1.html
  raw_urls: [https://raw.githubusercontent.com/ex/guide/main/src/chapter-1.md]
  repo: ex/guide
  relation: original
- name: 표준 스키마
  match: [https://std.example.org/spec, https://std.example.org/spec-alt]
  raw_urls: [https://raw.githubusercontent.com/ex/spec/main/schema.json]
  repo: ex/spec
  relation: official_artifact
- name: 호스트 전체
  match: host.example.net
  raw_urls: [https://raw.githubusercontent.com/ex/host/main/README.md]
  repo: ex/host
  relation: related
"""


def _ref_page(ref_id: str, url: str, source_type: str = "표준", reliability: str = "medium") -> str:
    meta = {"title": f"{ref_id} — Sample", "type": "reference", "ref_id": ref_id, "ref_title": "Sample", "org": "Example Org",
            "published": "2024", "url": url, "source_type": source_type, "reliability": reliability, "url_verified": False,
            "accessed": "2026-09-24", "related_areas": [], "tags": [], "status": "published", "created": "2026-09-24",
            "updated": "2026-09-24", "version": 1}
    body = "\n".join([
        f"[홈](../index.md) › [참고문헌](index.md) › {ref_id}", "", f"# {ref_id} — Sample", "",
        "## 서지 정보", "", "| 항목 | 값 |", "|---|---|", f"| id | {ref_id} |", "| 기관 | Example Org |", "| 제목 | Sample |",
        "| 발행일 | 2024 |", f"| URL | <{url}> |", f"| 유형 | {source_type} |", f"| 신뢰도 | {reliability} |",
        "| 원문 열람 | 미확인 — 원문 미열람 |", "| 접근일 | 2026-09-24 (원문 미열람) |", "",
        "## 요약", "", "원문 미열람. 예시 출처.", "",
        "## 인용된 페이지", "", "<!-- auto:reference-cited-pages:start -->", "- 아직 없음", "<!-- auto:reference-cited-pages:end -->", "",
        "## 각주 형식", "", "```", f"[^{ref_id}]: Example Org, Sample, 2024, {url}, 접근일 2026-09-24 (원문 미열람)", "```", "",
        "## 비고", "", "원문 미열람(페이지 열람이 차단된 환경에서 검색 결과의 기관·제목·URL 일치로 실재를 확인했다). 신뢰도는 medium 이 상한이다.", "",
    ])
    return fm.dumps(meta, body)


class TmpWiki:
    """임시 위키 루트(config/source_mirrors.yaml, docs/references, inbox/sources, data)."""

    def __init__(self):
        self._td = tempfile.TemporaryDirectory()
        self.root = Path(self._td.name)
        (self.root / "config").mkdir()
        (self.root / "config" / "source_mirrors.yaml").write_text(MIRRORS_YAML, encoding="utf-8")
        (self.root / "docs" / "references").mkdir(parents=True)
        (self.root / "inbox" / "sources").mkdir(parents=True)
        (self.root / "data").mkdir()
        (self.root / "data" / "changelog.json").write_text('{"items": []}\n', encoding="utf-8")

    def add_ref(self, ref_id: str, url: str, **kw) -> Path:
        p = self.root / "docs" / "references" / f"{ref_id}.md"
        p.write_text(_ref_page(ref_id, url, **kw), encoding="utf-8")
        return p

    def close(self):
        self._td.cleanup()


# --- 원문 열람 상한 -------------------------------------------------------------------------------

def _research(sources, findings):
    return {"run_id": "2026-09-25-01", "sources": sources, "findings": findings}


def _src(i, reliability="high", **kw):
    d = {"id": i, "org": "O", "title": "T", "published": None, "url": f"https://example.com/{i}", "type": "표준",
         "reliability": reliability, "accessed": "2026-09-25", "summary": "s"}
    d.update(kw)
    return d


def _finding(fid, ids, confidence="high"):
    return {"id": fid, "claim": "c", "tag": "사실", "source_ids": ids, "cross_checked": len(ids) > 1, "confidence": confidence,
            "evidence_excerpt": "", "as_of": "2026", "flow_step": None, "flow_item": None}


class TestApplyFetchCaps(unittest.TestCase):
    def setUp(self):
        self.w = TmpWiki()

    def tearDown(self):
        self.w.close()

    def test_unfetched_source_high_capped(self):
        r = _research([_src("ref-011")], [])
        logs = S.apply_fetch_caps(r, root=self.w.root, source_texts={})
        s = r["sources"][0]
        self.assertIs(s["fetched"], False)
        self.assertIsNone(s["fetched_via"])
        self.assertIs(s["source_unopened"], True)
        self.assertEqual(s["reliability"], "medium")
        self.assertTrue(any("ref-011" in l and "medium" in l for l in logs))

    def test_finding_high_with_one_source_capped(self):
        r = _research([_src("ref-011", fetched=True, fetched_via="webfetch")], [_finding("f1", ["ref-011"])])
        logs = S.apply_fetch_caps(r, root=self.w.root, source_texts={})
        self.assertIs(r["sources"][0]["fetched"], True)
        self.assertEqual(r["sources"][0]["reliability"], "high")
        self.assertEqual(r["findings"][0]["confidence"], "medium")
        self.assertTrue(any(l.startswith("발견 사항 f1") for l in logs))

    def test_finding_high_all_unfetched_capped(self):
        r = _research([_src("ref-011"), _src("ref-012")], [_finding("f1", ["ref-011", "ref-012"])])
        S.apply_fetch_caps(r, root=self.w.root, source_texts={})
        self.assertEqual(r["findings"][0]["confidence"], "medium")
        self.assertIs(r["findings"][0]["source_unopened"], True)

    def test_mixed_ok_keeps_high(self):
        r = _research([_src("ref-011", fetched=True, fetched_via="webfetch"), _src("ref-012", reliability="medium")],
                      [_finding("f1", ["ref-011", "ref-012"]), _finding("f2", ["ref-012"], confidence="medium")])
        logs = S.apply_fetch_caps(r, root=self.w.root, source_texts={})
        self.assertEqual(r["findings"][0]["confidence"], "high")
        self.assertEqual(r["findings"][1]["confidence"], "medium")
        self.assertIs(r["sources"][1]["fetched"], False)
        self.assertFalse(any(l.startswith("발견 사항") for l in logs))

    def test_duplicate_source_ids_count_once(self):
        r = _research([_src("ref-011", fetched=True, fetched_via="webfetch")], [_finding("f1", ["ref-011", "ref-011"])])
        S.apply_fetch_caps(r, root=self.w.root, source_texts={})
        self.assertEqual(r["findings"][0]["confidence"], "medium")

    def test_source_text_counts_as_fetched(self):
        texts = {"ref-012": {"path": "data/source_texts/ref-012.txt", "fetched_via": "inbox", "url": "https://example.com/ref-012"}}
        r = _research([_src("ref-011", fetched=True, fetched_via="webfetch"), _src("ref-012")],
                      [_finding("f1", ["ref-011", "ref-012"])])
        S.apply_fetch_caps(r, root=self.w.root, source_texts=texts)
        self.assertIs(r["sources"][1]["fetched"], True)
        self.assertEqual(r["sources"][1]["fetched_via"], "inbox")
        self.assertEqual(r["sources"][1]["reliability"], "high")
        self.assertEqual(r["findings"][0]["confidence"], "high")

    def test_webfetch_claim_rejected_when_fetch_unavailable(self):
        r = _research([_src("ref-011", fetched=True, fetched_via="webfetch")], [])
        logs = S.apply_fetch_caps(r, root=self.w.root, source_texts={}, web_fetch_available=False)
        self.assertIs(r["sources"][0]["fetched"], False)
        self.assertEqual(r["sources"][0]["reliability"], "medium")
        self.assertTrue(any("web_fetch_available" in l for l in logs))

    def test_github_raw_claims(self):
        ok = _src("ref-011", url="https://books.example.org/guide/chapter-1.html", fetched=True, fetched_via="github_raw",
                  fetch_url="https://raw.githubusercontent.com/ex/guide/main/src/chapter-1.md")
        artifact = _src("ref-012", url="https://std.example.org/spec/", fetched=True, fetched_via="github_raw",
                        fetch_url="https://raw.githubusercontent.com/ex/spec/main/schema.json")
        no_path = _src("ref-013", url="https://nowhere.example.com/x", fetched=True, fetched_via="github_raw")
        r = _research([ok, artifact, no_path], [])
        logs = S.apply_fetch_caps(r, root=self.w.root, source_texts={}, web_fetch_available=False)
        self.assertEqual([s["fetched"] for s in r["sources"]], [True, False, False])
        self.assertEqual(r["sources"][0]["fetched_via"], "github_raw")
        self.assertTrue(any("ref-012" in l and "공식 산출물" in l for l in logs))

    def test_source_unopened_conflict(self):
        r = _research([_src("ref-011", fetched=True, fetched_via="webfetch", source_unopened=True)], [])
        S.apply_fetch_caps(r, root=self.w.root, source_texts={})
        self.assertIs(r["sources"][0]["fetched"], False)

    def test_fetch_label(self):
        self.assertEqual(S.fetch_label({"fetched": True, "fetched_via": "github_raw"}), "원문 열람(GitHub raw 미러)")
        self.assertEqual(S.fetch_label({"fetched": True, "fetched_via": "inbox"}), "원문 열람(사용자 제공 파일(inbox))")
        self.assertEqual(S.fetch_label({"fetched": False}), "원문 미열람")
        self.assertEqual(S.fetch_label({}), "원문 미열람")


# --- 미러 --------------------------------------------------------------------------------------------

class TestMirrors(unittest.TestCase):
    def setUp(self):
        self.w = TmpWiki()

    def tearDown(self):
        self.w.close()

    def test_longest_match_first(self):
        got = S.mirror_for("https://books.example.org/guide/chapter-1.html#part", root=self.w.root)
        self.assertEqual(got, ["https://raw.githubusercontent.com/ex/guide/main/src/chapter-1.md",
                               "https://raw.githubusercontent.com/ex/guide/main/src/SUMMARY.md"])

    def test_normalization_and_boundaries(self):
        self.assertTrue(S.mirror_for("http://www.books.example.org/guide/", root=self.w.root))
        self.assertEqual(S.mirror_for("https://books.example.org/guidebook", root=self.w.root), [])
        self.assertEqual(S.mirror_for("https://std.example.org/spec-alt/v2", root=self.w.root),
                         ["https://raw.githubusercontent.com/ex/spec/main/schema.json"])
        self.assertEqual(S.mirror_for("https://host.example.net/any/page", root=self.w.root),
                         ["https://raw.githubusercontent.com/ex/host/main/README.md"])
        self.assertTrue(S.url_matches("https://a.example/doc.html", "https://a.example/doc"))
        self.assertEqual(S.mirror_for("https://unknown.example/", root=self.w.root), [])

    def test_github_blob_derived(self):
        url = "https://github.com/Org/Repo/blob/main/docs/Spec%20v1.md"
        self.assertEqual(S.github_blob_to_raw(url), "https://raw.githubusercontent.com/Org/Repo/main/docs/Spec%20v1.md")
        self.assertEqual(S.mirror_for(url, root=self.w.root)[0], "https://raw.githubusercontent.com/Org/Repo/main/docs/Spec%20v1.md")
        self.assertIsNone(S.github_blob_to_raw("https://github.com/Org/Repo"))

    def test_relation(self):
        e = S.mirror_entries("https://std.example.org/spec", root=self.w.root)
        self.assertEqual(e[0]["relation"], "official_artifact")
        self.assertEqual(S.original_mirror_for("https://std.example.org/spec", root=self.w.root), [])
        self.assertEqual(S.original_mirror_for("https://books.example.org/guide/chapter-1.html", root=self.w.root),
                         ["https://raw.githubusercontent.com/ex/guide/main/src/chapter-1.md"])

    def test_repo_mirror_file_is_valid(self):
        mirrors = S.load_mirrors()
        self.assertGreaterEqual(len(mirrors), 20)
        for e in mirrors:
            self.assertIn(e["relation"], S.MIRROR_RELATIONS)
            for r in e["raw_urls"]:
                self.assertTrue(r.startswith("https://raw.githubusercontent.com/"), r)
        self.assertEqual(S.mirror_for("https://osrf.github.io/ros2multirobotbook/rmf-core.html")[0],
                         "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/rmf-core.md")


# --- 원문 텍스트 수집(inbox) --------------------------------------------------------------------------

SAMPLE_HTML = """<!doctype html><html><head><title>Sample Standard</title><style>body{color:red}</style>
<script>var secret = 1;</script></head><body><nav>menu</nav><h1>Sample Standard</h1>
<p>The robot <b>shall</b> report its state &amp; position.</p><ul><li>item one</li><li>item two</li></ul>
<pre>code  block</pre></body></html>"""


class TestIngest(unittest.TestCase):
    def setUp(self):
        self.w = TmpWiki()
        self.ingest = _load_script("ingest_sources")

    def tearDown(self):
        self.w.close()

    def test_html_to_text(self):
        text, title = S.html_to_text(SAMPLE_HTML)
        self.assertEqual(title, "Sample Standard")
        self.assertIn("# Sample Standard", text)
        self.assertIn("The robot shall report its state & position.", text)
        self.assertIn("- item one", text)
        self.assertIn("code  block", text)
        self.assertNotIn("secret", text)
        self.assertNotIn("color:red", text)

    def test_inbox_html_and_txt(self):
        ref = self.w.add_ref("ref-001", "https://std.example.org/sample/")
        inbox = self.w.root / "inbox" / "sources"
        (inbox / "sample.html").write_text(SAMPLE_HTML, encoding="utf-8")
        (inbox / "notes.txt").write_text("Field notes about AMR charging.\r\n\r\n\r\nSecond paragraph.  \n", encoding="utf-8")
        (inbox / "manifest.yaml").write_text(
            "items:\n"
            "  - file: sample.html\n    url: http://www.std.example.org/sample\n    title: Sample Standard\n    org: Example Org\n    published: 2024\n"
            "  - file: notes.txt\n    url: https://blog.example.com/notes\n    title: Field Notes\n", encoding="utf-8")
        logs, fails = self.ingest.process_inbox(self.w.root, today="2026-09-25")
        self.assertEqual(fails, 0, logs)
        texts = S.load_source_texts(self.w.root)
        self.assertIn("ref-001", texts)
        self.assertIn("src-field-notes", texts)
        t1 = texts["ref-001"]
        self.assertEqual(t1["fetched_via"], "inbox")
        self.assertEqual(t1["path"], "data/source_texts/ref-001.txt")
        self.assertEqual(len(t1["sha256"]), 64)
        body = (self.w.root / t1["path"]).read_text(encoding="utf-8")
        self.assertEqual(t1["chars"], len(body))
        self.assertIn("shall report", body)
        notes = (self.w.root / texts["src-field-notes"]["path"]).read_text(encoding="utf-8")
        self.assertEqual(notes, "Field notes about AMR charging.\n\nSecond paragraph.\n")
        self.assertIsNone(texts["src-field-notes"]["ref_id"])
        # 참고문헌 페이지 갱신
        meta, page = fm.read(ref)
        self.assertIs(meta["fetched"], True)
        self.assertEqual(meta["fetched_via"], "inbox")
        self.assertEqual(meta["source_text"], "data/source_texts/ref-001.txt")
        self.assertEqual(meta["reliability"], "high")
        self.assertEqual(meta["version"], 2)
        self.assertIn("| 원문 열람 | 확인 — 원문 열람(사용자 제공 파일(inbox)) |", page)
        self.assertIn(", 접근일 2026-09-25\n", page)
        self.assertNotIn("접근일 2026-09-24 (원문 미열람)", page)
        self.assertIn(S.FETCH_BLOCK_START, page)
        self.assertIn("등록 당시 기록: 원문 미열람(", page)
        self.assertIn("<!-- auto:reference-cited-pages:start -->", page)
        # 파일 이동과 변경 이력
        self.assertFalse((inbox / "sample.html").exists())
        self.assertTrue((inbox / "processed" / "sample.html").is_file())
        self.assertTrue((inbox / "processed" / "notes.txt").is_file())
        cl = json.loads((self.w.root / "data" / "changelog.json").read_text(encoding="utf-8"))
        self.assertEqual([it["page"] for it in cl["items"]], ["docs/references/ref-001.md"])
        # 멱등: 다시 실행해도 바뀌지 않는다
        index_before = (self.w.root / "data" / "source_texts" / "index.json").read_text(encoding="utf-8")
        page_before = ref.read_text(encoding="utf-8")
        logs2, fails2 = self.ingest.process_inbox(self.w.root, today="2026-09-26")
        self.assertEqual(fails2, 0)
        self.assertTrue(any("이미 처리됨" in l for l in logs2))
        self.assertEqual((self.w.root / "data" / "source_texts" / "index.json").read_text(encoding="utf-8"), index_before)
        self.assertEqual(ref.read_text(encoding="utf-8"), page_before)

    def test_ref_id_and_missing_file(self):
        self.w.add_ref("ref-002", "https://other.example.org/doc")
        inbox = self.w.root / "inbox" / "sources"
        (inbox / "doc.md").write_text("# Doc Title\n\nBody text for the linked reference document.\n", encoding="utf-8")
        (inbox / "manifest.yaml").write_text(
            "items:\n  - file: doc.md\n    ref_id: ref-002\n  - file: missing.pdf\n    url: https://x.example/y\n", encoding="utf-8")
        logs, fails = self.ingest.process_inbox(self.w.root, today="2026-09-25", changelog=False)
        self.assertEqual(fails, 1)
        self.assertTrue(any("missing.pdf" in l and "파일 없음" in l for l in logs))
        self.assertEqual(S.load_source_texts(self.w.root)["ref-002"]["title"], "Doc Title")
        self.assertIs(fm.read(self.w.root / "docs" / "references" / "ref-002.md")[0]["fetched"], True)

    def test_dry_run_changes_nothing(self):
        self.w.add_ref("ref-001", "https://std.example.org/sample/")
        inbox = self.w.root / "inbox" / "sources"
        (inbox / "a.txt").write_text("Plain text source body long enough.\n", encoding="utf-8")
        (inbox / "manifest.yaml").write_text("items:\n  - file: a.txt\n    url: https://std.example.org/sample\n", encoding="utf-8")
        logs, fails = self.ingest.process_inbox(self.w.root, today="2026-09-25", dry_run=True)
        self.assertEqual(fails, 0)
        self.assertTrue((inbox / "a.txt").is_file())
        self.assertFalse((self.w.root / "data" / "source_texts").exists())

    def test_pdf_extraction_when_available(self):
        pdf = self.w.root / "tiny.pdf"
        pdf.write_bytes(_tiny_pdf("Hello PDF source"))
        try:
            text, method, _ = S.extract_text_file(pdf)
        except S.ExtractError as e:
            self.skipTest(f"PDF 도구 없음: {e}")
        self.assertIn("Hello PDF source", text)
        self.assertIn(method, ("pdftotext", "pypdf"))

    def test_select_texts_for_prompt(self):
        for key, body in (("ref-001", "Alpha " * 400), ("ref-002", "unrelated " * 50 + "charging station " + "x " * 50),
                          ("ref-003", "nothing here")):
            S.store_source_text(body, key=key, ref_id=key, title=key, url=f"https://e.example/{key}", fetched_via="inbox",
                                root=self.w.root, today="2026-09-25")
        got = S.select_texts_for_prompt(["ref-001", "ref-009"], ["charging"], 1800, root=self.w.root, min_share=500)
        self.assertEqual([k for k, _ in got], ["ref-001", "ref-002"])
        self.assertLessEqual(sum(len(t) for _, t in got), 1800 + 200)
        self.assertIn("charging station", got[1][1])
        self.assertIn("### data/source_texts/ref-001.txt", S.format_texts_for_prompt(got, root=self.w.root))
        self.assertIsNone(S.source_text_excerpt("ref-404", 100, root=self.w.root))
        self.assertIn("발췌", S.source_text_excerpt("ref-001", 100, root=self.w.root))


def _tiny_pdf(text: str) -> bytes:
    """텍스트 한 줄짜리 최소 PDF(Helvetica)."""
    stream = f"BT /F1 12 Tf 72 720 Td ({text}) Tj ET".encode("latin-1")
    objs = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>",
        b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    out = io.BytesIO()
    out.write(b"%PDF-1.4\n")
    offsets = []
    for i, o in enumerate(objs, 1):
        offsets.append(out.tell())
        out.write(f"{i} 0 obj\n".encode() + o + b"\nendobj\n")
    xref = out.tell()
    out.write(f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n".encode())
    for off in offsets:
        out.write(f"{off:010d} 00000 n \n".encode())
    out.write(f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    return out.getvalue()


# --- URL 확인 ---------------------------------------------------------------------------------------

class _Resp:
    def __init__(self, status):
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def getcode(self):
        return self.status


def _http_error(url, code, headers=None, body=b""):
    h = Message()
    for k, v in (headers or {}).items():
        h[k] = v
    return urllib.error.HTTPError(url, code, "x", h, io.BytesIO(body))


class FakeOpen:
    """URL·메서드별로 정해 둔 응답(상태 코드 int, 예외)을 돌려주는 가짜 urlopen."""

    def __init__(self, table):
        self.table = table
        self.calls = []

    def __call__(self, req, timeout=None, context=None):
        key = (req.full_url, req.get_method())
        self.calls.append(key)
        r = self.table.get(key, self.table.get(req.full_url))
        if isinstance(r, BaseException):
            raise r
        if callable(r):
            raise r(req.full_url)
        return _Resp(r)


class TestUrlCheck(unittest.TestCase):
    def setUp(self):
        self.cu = _load_script("check_urls")

    def test_classify(self):
        c = self.cu.classify
        self.assertEqual(c(http_status=200)[0], "열림")
        self.assertEqual(c(http_status=301)[0], "열림")
        self.assertEqual(c(http_status=404)[0], "없음")
        self.assertEqual(c(http_status=410)[0], "없음")
        self.assertEqual(c(http_status=403, headers={"X-Deny-Reason": "host_not_allowed"})[0], "정책 차단")
        self.assertEqual(c(http_status=403, body=b'{"message":"GitHub access to this repository is not enabled for this session."}')[0],
                         "정책 차단")
        self.assertEqual(c(http_status=403, body=b"Host not in allowlist: a.example")[0], "정책 차단")
        self.assertEqual(c(http_status=403, body=b"<html>Forbidden by site</html>")[0], "오류")
        self.assertEqual(c(http_status=500)[0], "오류")
        self.assertEqual(c(error=urllib.error.URLError(OSError("Tunnel connection failed: 403 Forbidden")))[0], "정책 차단")
        self.assertEqual(c(error=TimeoutError("timed out"))[0], "오류")
        self.assertEqual(c(error=urllib.error.URLError("[Errno -2] Name or service not known"))[0], "오류")

    def test_probe_paths(self):
        u1, u2, u3, u4 = "https://a.example/1", "https://b.example/2", "https://c.example/3", "https://d.example/4"
        fake = FakeOpen({
            (u1, "HEAD"): 200,
            (u2, "HEAD"): urllib.error.URLError(OSError("Tunnel connection failed: 403 Forbidden")),
            (u3, "HEAD"): _http_error(u3, 403),
            (u3, "GET"): _http_error(u3, 403, body=b'{"message":"GitHub access to this repository is not enabled for this session."}'),
            (u4, "HEAD"): _http_error(u4, 405),
            (u4, "GET"): _http_error(u4, 404),
        })
        self.assertEqual(self.cu.probe(u1, urlopen=fake)["status"], "열림")
        self.assertEqual(self.cu.probe(u2, urlopen=fake)["status"], "정책 차단")
        r3 = self.cu.probe(u3, urlopen=fake)
        self.assertEqual((r3["status"], r3["http"]), ("정책 차단", 403))
        self.assertEqual(self.cu.probe(u4, urlopen=fake)["status"], "없음")
        self.assertNotIn((u2, "GET"), fake.calls)

    def test_check_one_uses_mirror(self):
        url = "https://osrf.github.io/ros2multirobotbook/rmf-core.html"
        raw = "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/rmf-core.md"
        fake = FakeOpen({(url, "HEAD"): urllib.error.URLError(OSError("Tunnel connection failed: 403 Forbidden")), (raw, "HEAD"): 200})
        it = self.cu.check_one("ref-004", url, 5, None, urlopen=fake)
        self.assertEqual((it["status"], it["mirror"], it["mirror_status"], it["mirror_relation"]), ("정책 차단", raw, "열림", "original"))
        fake2 = FakeOpen({(url, "HEAD"): 200})
        it2 = self.cu.check_one("ref-004", url, 5, None, urlopen=fake2)
        self.assertEqual((it2["status"], it2["mirror_status"]), ("열림", None))
        self.assertEqual(fake2.calls, [(url, "HEAD")])

    def test_load_url_check_legacy_and_summary(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "url_check.json"
            p.write_text(json.dumps({"checked_at": "2026-09-24T10:00:00+09:00", "items": [
                {"ref_id": "ref-001", "url": "u1", "status": 200, "result": "열림"},
                {"ref_id": "ref-002", "url": "u2", "status": 404, "result": "오류"},
                {"ref_id": "ref-003", "url": "u3", "status": None, "result": "미확인"}]}), encoding="utf-8")
            uc = S.load_url_check(path=p)
        self.assertEqual({k: v["status"] for k, v in uc["items"].items()}, {"ref-001": "열림", "ref-002": "없음", "ref-003": "오류"})
        c = S.url_check_counts(uc)
        self.assertEqual((c["열림"], c["없음"], c["오류"], c["정책 차단"]), (1, 1, 1, 0))
        self.assertIn("참고문헌 URL 3건: 열림 1 · 없음 1 · 정책 차단 0 · 오류 1", S.url_check_summary_line(uc))


class TestReferencePageSync(unittest.TestCase):
    def setUp(self):
        self.w = TmpWiki()

    def tearDown(self):
        self.w.close()

    def test_sync_url_status_and_block(self):
        p = self.w.add_ref("ref-005", "https://books.example.org/guide/chapter-1.html", source_type="오픈소스 문서")
        uc = {"checked_at": "2026-09-25T09:00:00+09:00", "items": {"ref-005": {
            "url": "https://books.example.org/guide/chapter-1.html", "status": "정책 차단", "http": None,
            "detail": "HEAD 프록시 CONNECT 거부", "mirror": "https://raw.githubusercontent.com/ex/guide/main/src/chapter-1.md",
            "mirror_status": "열림", "mirror_relation": "original"}}}
        changes = S.sync_reference_page(p, root=self.w.root, today="2026-09-25", url_check=uc, texts={})
        self.assertTrue(changes)
        meta, body = fm.read(p)
        self.assertEqual((meta["fetched"], meta["fetched_via"], meta["url_status"]), (False, None, "정책 차단"))
        self.assertEqual(meta["reliability"], "medium")
        self.assertIn("| URL 확인 | 정책 차단 (2026-09-25", body)
        self.assertIn("| GitHub 미러 확인 | 열림 (2026-09-25, 같은 문서의 원본)", body)
        self.assertIn("접근일 2026-09-24 (원문 미열람)", body)
        self.assertEqual(S.sync_reference_page(p, root=self.w.root, today="2026-09-26", url_check=uc, texts={}), [])
        block = S.render_reference_fetch_status({"ref_id": "ref-005", "fetched": False}, root=self.w.root, url_check=uc, texts={})
        self.assertTrue(block.startswith(S.FETCH_BLOCK_START) and block.endswith(S.FETCH_BLOCK_END))
        self.assertIn("| 원문 열람 | 원문 미열람 |", block)

    def test_legacy_opened_page_stays_fetched(self):
        p = self.w.add_ref("ref-006", "https://legacy.example.org/doc")
        meta, body = fm.read(p)
        meta["url_verified"] = True
        fm.write(p, meta, body.replace("| 원문 열람 | 미확인 — 원문 미열람 |", "| 원문 열람 | 확인 |"))
        S.sync_reference_page(p, root=self.w.root, today="2026-09-25", url_check={"items": {}}, texts={})
        meta2, body2 = fm.read(p)
        self.assertEqual((meta2["fetched"], meta2["fetched_via"]), (True, "webfetch"))
        self.assertIn("| 원문 열람 | 확인 — 원문 열람(웹 열람(WebFetch)) |", body2)


if __name__ == "__main__":
    unittest.main()
