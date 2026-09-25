"""다중 트랙·확장 아이디어·페이지 상태 단일 원천 단위 테스트 (운영 전환: 확장 아이디어 3종 편입, 2026-09-25).

실행: python3 -m unittest pipeline/checks/test_tracks.py
검사 대상
- config/tracks/*.yaml: 새 트랙 2개(nl-task-chatbot, floorplan-recognition)와 첫 트랙의 필수 키, 단계·초안·아이디어 페이지 존재
- data/tracks/<slug>/backlog.json: id 형식·중복·단계 일치, 항목 키(스키마) 동일, 사용자 요청 시작 질문 포함
- 내비게이션: 트랙 3개(첫 트랙이 맨 앞) + "확장 아이디어" 섹션(트랙 바로 다음, 주제 앞, 색인 → 아이디어 3개)
- auto:area-tracks(세부영역 5. 로봇 능력·작업 온톨로지의 관련 연구 트랙 링크), auto:idea-area-map, auto:idea-areas, auto:idea-backlog
- auto:page-status(프런트매터 값으로 상태 줄) 와 status_line_violations, check_frontmatter 의 본문 상태 줄 반려
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import yaml  # noqa: E402

from lib import autoregion as ar  # noqa: E402
from lib import frontmatter as fm  # noqa: E402
from lib import paths  # noqa: E402
from lib import render  # noqa: E402
from lib.nav import build_nav, flatten_nav  # noqa: E402
from lib.source import load_source  # noqa: E402

FIRST = "manual-capability-ontology"
NEW_TRACKS = ["nl-task-chatbot", "floorplan-recognition"]
ALL_TRACKS = [FIRST, *NEW_TRACKS]
REQUIRED_KEYS = ["slug", "name", "status", "primary_area", "related_areas", "current_stage", "stages", "stage_names",
                 "stage_pages", "runs_per_week", "budget", "order", "draft_page", "draft_title", "draft_template",
                 "draft_versions", "idea_no", "idea_name", "idea_page", "idea_areas", "idea_area_notes",
                 "glossary_targets", "research_goals", "stage_artifacts"]
BACKLOG_KEYS = {"id", "question", "stage", "origin", "status", "answered_run_id", "answer_link", "created"}
BACKLOG_OPTIONAL = {"origin_run_id"}
STATUSES = {"열림", "조사 중", "답함", "보류", "폐기"}
# 사용자 요청의 시작 질문(문구 그대로, 끝의 물음표만 더함) — 아이디어별 3개
REQUEST_QUESTIONS = {
    FIRST: ["매뉴얼에서 능력과 제약을 추출할 때 가장 자주 틀리는 유형은 무엇인가?",
            "\"이 작업을 할 수 있는 로봇\" 질의를 어떤 형식으로 표현하는가?"],   # 첫 질문은 q1-01 과 같아 새로 만들지 않았다
    "nl-task-chatbot": ["자연어 지시를 작업 단위로 분해하는 기존 접근은 무엇이 있는가?",
                        "LLM의 잘못된 해석이 로봇 배정으로 이어지지 않게 하는 확인 절차는 어떻게 두는가?",
                        "스케줄링 결정은 LLM과 최적화 엔진 중 어디에 맡기는가?"],
    "floorplan-recognition": ["평면도에서 벽·문·엘리베이터·계단을 인식하는 공개 데이터셋과 모델은 무엇이 있는가?",
                              "인식 결과를 로봇 내비게이션 지도로 바꿀 때 필요한 보정은 무엇인가?",
                              "공간 그래프를 표현하는 기존 표준(예: BIM·IFC, 실내 공간 표준)은 무엇이 있는가?"],
}
IDEA_SECTIONS = ["1. 문제 정의", "2. 관련 세부 연구영역", "3. 선행 연구·제품 사례", "4. 필요한 데이터와 표준",
                 "5. 구현 가설", "6. 검증 방법", "7. 미해결 질문 백로그"]


def _load_script(name: str):
    path = Path(__file__).resolve().parent / f"{name}.py"
    spec = importlib.util.spec_from_file_location(f"_t_{name}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _cfg(slug: str) -> dict:
    return yaml.safe_load(paths.track_config(slug).read_text(encoding="utf-8"))


class TestTrackConfigs(unittest.TestCase):
    def test_required_keys_and_files(self):
        for slug in ALL_TRACKS:
            cfg = _cfg(slug)
            for k in REQUIRED_KEYS:
                self.assertIn(k, cfg, f"{slug}.yaml 에 {k} 없음")
            self.assertEqual(cfg["slug"], slug)
            self.assertEqual(cfg["status"], "active")
            self.assertIsNone(cfg["runs_per_week"], "runs_per_week 는 비워 settings.track_runs_per_week 를 따른다")
            n = int(cfg["stages"])
            self.assertEqual(sorted(int(k) for k in cfg["stage_names"]), list(range(1, n + 1)))
            self.assertEqual(sorted(int(k) for k in cfg["stage_pages"]), list(range(1, n + 1)))
            for k, f in cfg["stage_pages"].items():
                meta, _ = fm.read(paths.track_dir(slug) / f)
                self.assertEqual(meta.get("title"), f"단계 {k}. {cfg['stage_names'][k]}", f"{slug} 단계 {k} 제목")
                self.assertEqual(int(meta.get("stage")), int(k))
            self.assertTrue((paths.track_dir(slug) / cfg["draft_page"]).is_file())
            meta, _ = fm.read(paths.track_dir(slug) / cfg["draft_page"])
            self.assertEqual(meta.get("title"), cfg["draft_title"])
            self.assertEqual(meta.get("type"), "ontology-draft")
            self.assertTrue((paths.ROOT / "templates" / cfg["draft_template"]).is_file())
            self.assertTrue(paths.track_draft_versions(slug).is_file())
            self.assertTrue((paths.ROOT / cfg["idea_page"]).is_file(), cfg["idea_page"])
            self.assertTrue(6 <= len(cfg["glossary_targets"]) <= 10, f"{slug} glossary_targets 6~10개")
            for n_area in [cfg["primary_area"], *cfg["related_areas"]]:
                self.assertIn(int(n_area), paths.AREA_NOS)
            ia = cfg["idea_areas"]
            mapped = set(ia["primary"]) | set(ia["related"])
            self.assertFalse(set(ia["primary"]) & set(ia["related"]), "● 와 ○ 가 겹친다")
            self.assertEqual(mapped, set(cfg["related_areas"]) | {cfg["primary_area"]},
                             f"{slug}: idea_areas 와 primary_area+related_areas 가 다르다")
            self.assertEqual(set(int(k) for k in cfg["idea_area_notes"]), mapped, f"{slug}: 매핑 근거가 빠진 영역")
            for fname in [f for fs in cfg["stage_artifacts"].values() for f in fs]:
                self.assertTrue((paths.track_dir(slug) / fname).is_file(), f"{slug}/{fname}")

    def test_new_tracks_shape(self):
        for slug in NEW_TRACKS:
            cfg = _cfg(slug)
            self.assertEqual(cfg["stages"], 5)
            self.assertEqual(cfg["current_stage"], 1)
            self.assertEqual(cfg["stage_names"][1], "선행 연구·제품 사례 조사")
            self.assertEqual(cfg["stage_names"][5], "검증 방법과 가설 판정")
            for f in ("index.md", "question-backlog.md", "log.md", "experiments.md"):
                self.assertTrue((paths.track_dir(slug) / f).is_file(), f"{slug}/{f}")
        self.assertEqual(_cfg("nl-task-chatbot")["stage_names"][4], "오해석 방지와 확인 절차")
        self.assertEqual(_cfg("floorplan-recognition")["stage_names"][4], "지도 변환 보정과 현장 정합")

    def test_first_track_goals_and_scope(self):
        cfg = _cfg(FIRST)
        self.assertEqual(len(cfg["research_goals"]), 5)
        self.assertTrue(cfg["research_goals"][3].startswith("작업 할당 질의"))
        self.assertTrue(cfg["research_goals"][4].startswith("신규 로봇 온보딩 시 능력 정의 초안 자동 생성"))
        self.assertEqual(cfg["scope_capabilities"], ["이동", "계단", "적재", "도어 조작", "충전"])
        text = (paths.track_dir(FIRST) / "index.md").read_text(encoding="utf-8")
        self.assertIn("4. 작업 할당 질의:", text)
        self.assertIn("5. 신규 로봇 온보딩 시 능력 정의 초안 자동 생성:", text)
        # 첫 트랙은 기본값(온톨로지 초안)과 같은 초안·버전 파일을 선언한다 → 출력이 바뀌지 않는다
        self.assertEqual(paths.track_page_order(FIRST), paths.TRACK_PAGE_ORDER)
        self.assertEqual(paths.track_draft_versions(FIRST).name, "ontology_versions.json")

    def test_track_order(self):
        self.assertEqual(paths.ordered_track_slugs()[:3], ALL_TRACKS)
        self.assertEqual(render.track_slugs()[:3], ALL_TRACKS)
        self.assertEqual(paths.idea_page_rels(), ["ideas/robot-capability-ontology.md", "ideas/nl-task-chatbot.md",
                                                  "ideas/floorplan-recognition.md"])


class TestBacklogs(unittest.TestCase):
    def test_ids_unique_and_well_formed(self):
        for slug in ALL_TRACKS:
            cfg = _cfg(slug)
            items = json.loads(paths.track_backlog(slug).read_text(encoding="utf-8"))["items"]
            ids = [b["id"] for b in items]
            self.assertEqual(len(ids), len(set(ids)), f"{slug}: id 중복")
            for b in items:
                self.assertRegex(b["id"], r"^q\d-\d\d$")
                self.assertEqual(int(b["id"][1]), int(b["stage"]), f"{slug} {b['id']}: id 의 단계와 stage 가 다름")
                self.assertTrue(1 <= int(b["stage"]) <= int(cfg["stages"]))
                self.assertIn(b["status"], STATUSES)
                self.assertTrue(b["origin"] == "사용자" or re.fullmatch(r"f\d+", str(b["origin"])), b["origin"])
                self.assertTrue(BACKLOG_KEYS <= set(b) <= BACKLOG_KEYS | BACKLOG_OPTIONAL, f"{slug} {b['id']}: 키 {set(b)}")
                self.assertRegex(b["created"], r"^\d{4}-\d{2}-\d{2}$")

    def test_request_questions_present(self):
        for slug, qs in REQUEST_QUESTIONS.items():
            items = json.loads(paths.track_backlog(slug).read_text(encoding="utf-8"))["items"]
            texts = {b["question"]: b for b in items}
            for q in qs:
                self.assertIn(q, texts, f"{slug}: 사용자 요청 질문 없음: {q}")
                self.assertEqual(texts[q]["origin"], "사용자")

    def test_new_track_seed_sizes(self):
        for slug in NEW_TRACKS:
            cfg = _cfg(slug)
            items = json.loads(paths.track_backlog(slug).read_text(encoding="utf-8"))["items"]
            # 시작 질문(제기 근거 "사용자")만 센다. 실행이 더한 후속 질문(제기 근거 finding id)과 답함·조사 중 상태 변화는 정상 운영이다
            seed = [b for b in items if b["origin"] == "사용자"]
            for n in range(1, int(cfg["stages"]) + 1):
                k = sum(1 for b in seed if int(b["stage"]) == n)
                self.assertTrue(3 <= k <= 5, f"{slug} 단계 {n} 시작 질문 {k}개(3~5개여야 한다)")
            self.assertTrue(all(b["status"] in ("열림", "조사 중", "답함", "보류", "폐기") or str(b["status"]).startswith("보류") for b in items))

    def test_first_track_additions(self):
        items = {b["id"]: b for b in json.loads(paths.track_backlog(FIRST).read_text(encoding="utf-8"))["items"]}
        for qid in ("q3-07", "q3-08", "q4-07", "q4-08", "q5-06", "q7-02"):
            self.assertIn(qid, items)
            self.assertEqual(items[qid]["origin"], "사용자")
        # "로봇 능력을 표현하는 기존 온톨로지·표준"은 q1-01 과 같은 질문이라 중복 등록하지 않았다
        self.assertFalse(any("로봇 능력을 표현하는 기존 온톨로지·표준" in b["question"] for b in items.values()))


class TestNav(unittest.TestCase):
    def test_tracks_and_ideas_sections(self):
        nav = build_nav()
        top = [next(iter(i)) if isinstance(i, dict) else i for i in nav]
        self.assertIn("중점 연구 트랙", top)
        self.assertIn("확장 아이디어", top)
        t = top.index("중점 연구 트랙")
        self.assertEqual(top[t + 1], "확장 아이디어", "확장 아이디어는 중점 연구 트랙 바로 다음")
        if "주제" in top:
            self.assertLess(top.index("확장 아이디어"), top.index("주제"))
        tracks = nav[t]["중점 연구 트랙"]
        got = [re.match(r"tracks/([^/]+)/", flatten_nav([i])[0][1]).group(1) for i in tracks]
        self.assertEqual(got[:3], ALL_TRACKS, "첫 트랙이 맨 앞, 이어서 새 트랙 2개")
        ideas = [p for _, p in flatten_nav([nav[t + 1]])]
        self.assertEqual(ideas[:4], ["ideas/index.md", "ideas/robot-capability-ontology.md", "ideas/nl-task-chatbot.md",
                                     "ideas/floorplan-recognition.md"])

    def test_track_children_use_draft_page(self):
        nav = build_nav()
        tracks = next(v for i in nav if isinstance(i, dict) for k, v in i.items() if k == "중점 연구 트랙")
        for slug, item in zip(ALL_TRACKS, tracks):
            names = [p.split("/", 2)[2] for _, p in flatten_nav([item])]
            draft = _cfg(slug)["draft_page"]
            stages = [n for n in names if n.startswith("stage-")]
            self.assertEqual(names[0], "index.md")
            self.assertEqual(names.index(draft), len(stages) + 1, f"{slug}: 초안이 단계 바로 다음에 있어야 한다")
            self.assertLess(names.index(draft), names.index("question-backlog.md"))

    def test_protect_source_structure_check(self):
        ps = _load_script("protect_source")
        nav = build_nav()
        self.assertEqual(ps.check_nav_structure(nav), [])
        kinds = [ps._nav_kind(i) for i in nav]
        bad = list(nav)
        i = kinds.index("ideas")
        bad.insert(kinds.index("topics"), bad.pop(i))          # 확장 아이디어를 주제 뒤로
        self.assertTrue(any("ideas" in e for e in ps.check_nav_structure(bad)))
        bad2 = list(nav)
        bad2[0], bad2[1] = bad2[1], bad2[0]                     # 4.8 원문 순서(홈 → 소개)를 뒤집는다
        self.assertTrue(any("4.8 순서" in e for e in ps.check_nav_structure(bad2)))
        bad3 = list(nav)
        t = kinds.index("tracks")
        sec = dict(bad3[t])
        k = next(iter(sec))
        sec[k] = list(reversed(sec[k]))                         # 첫 트랙이 맨 앞이 아님
        bad3[t] = sec
        self.assertTrue(any("첫 트랙" in e for e in ps.check_nav_structure(bad3)))


class TestAreaTracksAndIdeas(unittest.TestCase):
    def test_area5_links(self):
        rel = paths.area_rel_path(5)
        out = render.render_for("area-tracks", rel, {"type": "area", "area_no": 5})
        self.assertTrue(out.startswith('!!! note "관련 연구 트랙"'))
        for slug in ALL_TRACKS:
            self.assertIn(f"../../tracks/{slug}/index.md", out)
        for page in ("robot-capability-ontology", "nl-task-chatbot", "floorplan-recognition"):
            self.assertIn(f"../../ideas/{page}.md", out)
        self.assertIn("[매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 중심 영역(●)", out)
        self.assertIn("[자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○)", out)
        self.assertIn("아이디어 1. 로봇 기능 온톨로지", out)
        # 페이지의 영역이 렌더 결과와 같다(scaffold --refresh-auto 반영 여부)
        text = paths.area_file(5).read_text(encoding="utf-8")
        self.assertEqual(ar.get_region(text, "area-tracks"), out)

    def test_area_regions_placed_before_section1(self):
        """28개 세부영역 페이지 모두 소속 대분류 admonition 바로 아래, 1절 앞에 area-tracks 영역이 있다."""
        for no in paths.AREA_NOS:
            text = paths.area_file(no).read_text(encoding="utf-8")
            self.assertTrue(ar.has_region(text, "area-tracks"), no)
            self.assertLess(text.index("<!-- auto:area-tracks:start -->"), text.index("## 1. 한 줄 정의"))
            self.assertLess(text.index('!!! info "소속 대분류"'), text.index("<!-- auto:area-tracks:start -->"))
        # 어느 트랙과도 연결되지 않은 영역(4. 성과·경제성·프로세스 개선)은 빈 영역
        self.assertEqual(render.render_area_tracks(4), "")

    def test_idea_area_map(self):
        out = render.render_for("idea-area-map", "ideas/index.md", {"type": "idea", "subtype": "index"})
        src = load_source()
        rows = [l for l in out.split("\n") if l.startswith("| [")]
        self.assertEqual(len(rows), 28)
        for no in paths.AREA_NOS:
            self.assertIn(f"[{src.area(no).title}](", out)     # 번호와 이름을 함께 쓴 링크
        for slug in ALL_TRACKS:
            ia = _cfg(slug)["idea_areas"]
            label = render.idea_label(_cfg(slug))
            self.assertIn(f"- {label}: ● {len(ia['primary'])}개 · ○ {len(ia['related'])}개", out)
        row5 = next(r for r in rows if "[5. 로봇 능력·작업 온톨로지]" in r)
        self.assertEqual([c.strip() for c in row5.strip().strip("|").split("|")[2:]], ["●", "○", "○"])
        row6 = next(r for r in rows if "[6. 지도·공간·위치 모델]" in r)
        self.assertEqual([c.strip() for c in row6.strip().strip("|").split("|")[2:]], ["", "○", "●"])

    def test_idea_pages(self):
        for slug in ALL_TRACKS:
            cfg = _cfg(slug)
            p = paths.ROOT / cfg["idea_page"]
            meta, body = fm.read(p)
            self.assertEqual(meta["type"], "idea")
            self.assertEqual(meta["track"], slug)
            self.assertIn(meta["status"], ("seed", "draft", "published", "verified", "needs_update"))   # 트랙 실행이 게시하면 seed 가 아니다
            heads = [l[3:].strip() for l in body.split("\n") if l.startswith("## ")]
            self.assertEqual(heads, IDEA_SECTIONS, p.name)
            self.assertIn(cfg["idea_definition"], body, "1절에 아이디어 정의 문구 그대로")
            for key in ("page-status", "idea-areas", "idea-backlog"):
                self.assertTrue(ar.has_region(body, key), f"{p.name}: auto:{key} 없음")
            backlog = render.render_for("idea-backlog", paths.docs_rel(p), meta)
            self.assertIn("| 상태 | id | 질문 |", backlog)
            self.assertIn("열림", backlog)
        meta, _ = fm.read(paths.DOCS / "ideas" / "index.md")
        self.assertEqual((meta["type"], meta.get("subtype")), ("idea", "index"))
        self.assertEqual(fm.validate(meta), [])

    def test_draft_version_history_generalized(self):
        for slug in NEW_TRACKS:
            out = render.render_ontology_version_history(slug)
            self.assertIn("| 0 | 2026-09-25 |", out)
        first = render.render_ontology_version_history(FIRST)
        self.assertIn("| 0.1 | 2026-09-25 |", first)

    def test_home_lists_all_tracks(self):
        out = render.render_for("home-track-status", "index.md", {"type": "home"})
        rows = [l for l in out.split("\n") if l.startswith("| ") and not l.startswith("| 트랙 |")]
        self.assertEqual([r.split("|")[1].strip() for r in rows][:3],
                         ["매뉴얼 기반 로봇 기능 온톨로지", "자연어 업무 지시 챗봇", "건축 도면 자동 인식"])


class TestPageStatus(unittest.TestCase):
    META = {"title": "x", "type": "topic", "status": "published", "confidence": "medium", "version": 3,
            "updated": "2026-09-25", "last_run": "2026-09-24"}

    def test_render_from_frontmatter(self):
        self.assertIn("page-status", ar.AUTO_KEYS)
        out = render.render_for("page-status", "topics/2026/x.md", dict(self.META))
        self.assertEqual(out, "> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 3 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-24")
        out = render.render_page_status("topics/2026/x.md", {"status": "seed", "version": 1, "updated": "2026-09-25"})
        self.assertIn("신뢰도: 미부여", out)
        self.assertIn("마지막 실행: 없음", out)

    def test_draft_version_label(self):
        out = render.render_page_status("tracks/manual-capability-ontology/ontology-draft.md",
                                        {"track": FIRST, "ontology_version": "0.1", **self.META})
        self.assertTrue(out.startswith("> 온톨로지 버전: v0.1 · 페이지 상태: published"))
        out = render.render_page_status("tracks/nl-task-chatbot/task-model-draft.md",
                                        {"track": "nl-task-chatbot", "ontology_version": "0", **self.META})
        self.assertTrue(out.startswith("> 초안 버전: v0 · 페이지 상태:"))

    def test_pages_match_frontmatter(self):
        """page-status 영역이 있는 모든 페이지에서 영역 내용이 그 페이지 프런트매터의 렌더 결과와 같다."""
        n = 0
        for p in sorted(paths.DOCS.rglob("*.md")):
            text = p.read_text(encoding="utf-8")
            if not ar.has_region(text, "page-status"):
                continue
            meta, _ = fm.parse(text)
            rel = p.relative_to(paths.DOCS).as_posix()
            self.assertEqual(ar.get_region(text, "page-status"), render.render_page_status(rel, meta), rel)
            n += 1
        self.assertGreaterEqual(n, 3)

    def test_status_line_violations(self):
        body = "\n".join([
            "[홈](../index.md) › x", "", "# x", "",
            "> 상태: draft · 신뢰도: medium · 갱신일: 2026-09-25",               # 2026-09-25 전의 주제·세부영역 상태 줄
            "> 온톨로지 버전: v0.1 · 페이지 상태: draft · 신뢰도: medium",        # 온톨로지 초안의 손으로 쓴 줄
            "상태: published",
            "**상태:** seed",
            "<!-- auto:page-status:start -->", "> 페이지 상태: draft · 신뢰도: medium", "<!-- auto:page-status:end -->",
            "```", "> 상태: draft", "```",
            "- (상태: 열림) 질문", "- 상태: open", "> 단계 상태: 대기 · 열린 질문: 3건", "> 트랙 상태: active",
            "`페이지 상태:` 는 인라인 코드 설명",
        ])
        v = render.status_line_violations(body)
        self.assertEqual(len(v), 4, v)
        self.assertTrue(v[0].startswith("본문 5행: > 상태: draft"))
        self.assertTrue(any("온톨로지 버전" in x for x in v))
        self.assertEqual(render.status_line_violations("# x\n\n본문\n"), [])

    def test_no_violations_in_docs(self):
        for p in sorted(paths.DOCS.rglob("*.md")):
            _, body = fm.read(p)
            self.assertEqual(render.status_line_violations(body), [], p.relative_to(paths.DOCS).as_posix())

    def test_check_frontmatter_fails_on_body_status_line(self):
        cf = _load_script("check_frontmatter")
        page = ("---\ntitle: \"시험\"\ntype: about\nstatus: published\ncreated: 2026-09-25\nupdated: 2026-09-25\nversion: 1\n---\n\n"
                "[홈](../index.md) › 시험\n\n# 시험\n\n{status}\n\n본문이다.\n")
        saved = paths.DOCS
        try:
            with tempfile.TemporaryDirectory() as d:
                docs = Path(d) / "docs"
                (docs / "about").mkdir(parents=True)
                target = docs / "about" / "x.md"
                paths.DOCS = docs

                def run() -> tuple[int, str]:
                    buf = io.StringIO()
                    with contextlib.redirect_stdout(buf):
                        rc = cf.main()
                    return rc, buf.getvalue()

                target.write_text(page.format(status="> 상태: published · 신뢰도: medium · 갱신일: 2026-09-25"), encoding="utf-8")
                rc, out = run()
                self.assertEqual(rc, 1, "손으로 쓴 상태 줄이 있으면 실패해야 한다")
                self.assertIn("손으로 쓴 페이지 상태 줄", out)
                target.write_text(page.format(status="> 온톨로지 버전: v0 · 페이지 상태: seed"), encoding="utf-8")
                self.assertEqual(run()[0], 1)
                target.write_text(page.format(status="<!-- auto:page-status:start -->\n> 페이지 상태: published\n"
                                                     "<!-- auto:page-status:end -->"), encoding="utf-8")
                self.assertEqual(run()[0], 0, "page-status 영역 안의 상태 줄은 통과")
        finally:
            paths.DOCS = saved


if __name__ == "__main__":
    unittest.main()
