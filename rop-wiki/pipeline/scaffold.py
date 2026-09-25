#!/usr/bin/env python3
"""위키 뼈대(시드 페이지) 생성기.

기본 실행: 페이지 생성(이미 있으면 건드리지 않음) → data 시드 생성(없을 때만)
          → refresh_all_auto_regions() → write_mkdocs_yml()
옵션:
  --force            이미 있는 페이지도 덮어쓴다(data/*.json 은 건드리지 않는다)
  --reset-data       data/{open_questions,changelog,flow_matrix}.json 을 시드로 되돌린다(상태 데이터 초기화)
  --refresh-auto     페이지 생성 없이 refresh_all_auto_regions() + write_mkdocs_yml() 만 실행
  --apply-url-check  data/url_check.json(check_urls.py 결과)을 참고문헌 페이지에 반영한다: url_status, 열린 GitHub 원문 미러의
                     텍스트 저장(data/source_texts) → fetched·원문 열람 표시. 신뢰도 상한은 원문 열람(fetched)일 때만 푼다
                     (--no-changelog 이면 data/changelog.json 에 쓰지 않는다)
  --verbose          바뀐 파일을 출력

퍼블리셔(pipeline/publish.*)는 사이트 빌드 직전에 반드시 `--refresh-auto` 와 같은 일
(refresh_all_auto_regions() + write_mkdocs_yml())을 실행해야 한다. 다른 담당이 페이지 title 을 바꾸거나
페이지를 추가하면 mkdocs.yml 과 auto 영역이 낡아 protect_source.py 의 내비 검사가 실패한다.

원문에서 옮기는 문장은 손으로 쓰지 않고 lib/source.py 파서가 읽은 값을 그대로 출력한다.
[분류원문] 태그가 붙는 줄에는 원문 문장(또는 표 셀)만 두고 위키 문구를 섞지 않는다
(protect_source.check_tagged_lines 가 docs 전체의 태그 줄을 원문과 대조한다).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import autoregion as ar  # noqa: E402
from lib import frontmatter as fm  # noqa: E402
from lib import paths  # noqa: E402
from lib.korean import topic_particle  # noqa: E402
from lib.nav import write_mkdocs_yml  # noqa: E402
from lib.render import refresh_all_auto_regions  # noqa: E402
from lib.source import Reference, load_source  # noqa: E402
from lib.verbatim import TAG, tag_blocks, tag_line  # noqa: E402

DOCS = paths.DOCS
DATA = paths.DATA
SRC = load_source()
TODAY = paths.today()
BUILD_RUN_ID = f"build-{TODAY}"
TRACK_SLUG = "manual-capability-ontology"   # 사양서 0장 tracks 설정값

# 참고문헌 유형·신뢰도 (사양서 4.7·6.1 유형 분류, 원문 12장 항목 순서)
REF_TYPES: dict[int, str] = {
    1: "표준", 2: "기사", 3: "표준", 4: "오픈소스 문서", 5: "논문", 6: "논문",
    7: "정부·연구기관", 8: "정부·연구기관", 9: "오픈소스 문서", 10: "오픈소스 문서",
}
REF_RELIABILITY: dict[str, str] = {
    "표준": "high", "논문": "high", "정부·연구기관": "high", "오픈소스 문서": "high", "기사": "medium",
}
# 원문 미열람(URL 열림 미확인) 출처에는 유형 기준값과 무관하게 high 를 주지 않는다(medium 상한).
# 공통 규약: 페이지 열람이 막힌 환경에서는 모든 출처에 "원문 미열람"을 표시하고 신뢰도 high 를 주지 않는다. [가정]
REF_UNVERIFIED_CAP = "medium"
URL_CHECK_FILE = DATA / "url_check.json"   # pipeline/checks/check_urls.py --json 의 저장 위치 [가정]

AREA_SECTIONS: list[str] = [
    "1. 한 줄 정의",
    "2. SCM 관점의 질문",
    "3. 왜 중요한가",
    "4. 핵심 개념과 용어",
    "5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)",
    "6. 대표 접근법과 기술",
    "7. 관련 표준·프레임워크·오픈소스",
    "8. 대표 연구와 자료",
    "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)",
    "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
    "11. 열린 질문",
    "12. 최근 업데이트 (자동)",
    "13. 참고 자료 (각주)",
]
NOT_WRITTEN = "아직 작성되지 않음"

VERBOSE = False
FORCE = False
_written: list[str] = []


# --- 공통 도우미 ---------------------------------------------------------------------

def log(msg: str) -> None:
    if VERBOSE:
        print(msg)


def meta(title: str, type_: str, status: str = "published", **extra) -> dict:
    m = {"title": title, "type": type_}
    m.update(extra)
    m.update({"status": status, "created": TODAY, "updated": TODAY, "version": 1})
    # 보기 좋은 순서: title, type, (추가), status, created, updated, version
    order = ["title", "type", *[k for k in extra], "status", "created", "updated", "version"]
    return {k: m[k] for k in order}


def emit(rel: str, page_meta: dict, body: str) -> bool:
    """docs 기준 상대 경로에 페이지를 쓴다. 이미 있으면 --force 없이는 건드리지 않는다."""
    p = DOCS / rel
    if p.exists() and not FORCE:
        log(f"[skip] {rel} (이미 있음)")
        return False
    fm.write(p, page_meta, body)
    _written.append(f"docs/{rel}")
    log(f"[write] docs/{rel}")
    return True


def L(from_rel: str, to_rel: str, text: str) -> str:
    """페이지 위치 기준 상대 링크."""
    return f"[{text}]({paths.rel_link(from_rel, to_rel)})"


def crumb(from_rel: str, *parts: tuple[str, str | None]) -> str:
    """이동 경로 줄. parts: (라벨, docs 기준 경로 | None=현재 페이지)."""
    items = [L(from_rel, "index.md", "홈")]
    for label, rel in parts:
        items.append(L(from_rel, rel, label) if rel else label)
    return " › ".join(items)


def ref_link(from_rel: str, ref: Reference) -> str:
    return L(from_rel, f"references/{ref.id}.md", ref.id)


def citation_note(from_rel: str, text: str, with_footnote: bool = True) -> tuple[str, list[Reference]]:
    """본문의 원문 각주 [n] 을 참고문헌 ref-00n 으로 안내하는 문장과 참조 목록."""
    refs = [SRC.reference(n) for n in SRC.citations(text)]
    if not refs:
        return "", []
    parts = []
    for r in refs:
        # 조사 '은/는' 은 숫자 읽기의 받침 여부로 고른다: [1]은, [2]는, [4]는, [10]은
        s = f"원문의 [{r.n}]{topic_particle(r.n)} 참고문헌 {ref_link(from_rel, r)}에 해당한다."
        if with_footnote:
            s += f"[^{r.id}]"
        parts.append(s)
    return " ".join(parts), refs


def footnotes(refs: list[Reference]) -> str:
    return "\n".join(r.footnote(TODAY) for r in refs)


def area_link(from_rel: str, no: int) -> str:
    return L(from_rel, paths.area_rel_path(no), SRC.area(no).title)


def cat_link(from_rel: str, letter: str) -> str:
    return L(from_rel, paths.category_index_rel(letter), SRC.category(letter).title)


# --- 홈 -------------------------------------------------------------------------

def build_home() -> None:
    rel = "index.md"
    cats = SRC.categories
    header = ["대분류", "핵심 질문", "세부영역", "대분류 페이지", "세부 연구영역"]
    rows = []
    for row in SRC.overview_table_rows:
        letter = row["category_title"][0]
        cat = SRC.category(letter)
        areas = "<br>".join(area_link(rel, no) for no in cat.area_nos)
        rows.append(f"| {row['category_title']} | {row['core_question']} | {row['area_range']} | {cat_link(rel, letter)} | {areas} |")
    table = "| " + " | ".join(header) + " |\n|" + "---|" * len(header) + "\n" + "\n".join(rows)

    # 9장 표의 두 셀을 이어 붙인 요약 줄이다. 원문에 이 줄 자체는 없으므로 [분류원문] 태그를 붙이지 않는다.
    scope_lines = "\n".join(f"- {r['경계']} — {r['external']}" for r in SRC.scope_rows)
    cite_sentence, _ = citation_note(rel, SRC.scor_paragraph, with_footnote=False)

    first_area, last_area = SRC.area(paths.AREA_NOS[0]).title, SRC.area(paths.AREA_NOS[-1]).title
    # 이동 경로 규약은 모든 docs 페이지에 적용된다. 홈은 경로가 "홈" 한 단어뿐이므로 링크 없이 그 단어만 둔다.
    body = f"""홈

# ROP 연구 위키

SCM(공급망 관리, Supply Chain Management) 관점에서 로봇 오케스트레이션 플랫폼(Robot Orchestration Platform, ROP)의 연구 범위를 정리하고, 리서치·내용 검증·스토리텔러 에이전트가 매일 한 영역씩 조사한 내용을 쌓아 가는 연구 위키다.

## ROP란 무엇인가

{tag_line(SRC.rop_definition_sentence)}

{tag_line(SRC.scor_paragraph)}

SCOR(Supply Chain Operations Reference)의 오케스트레이션은 계획부터 반품까지 공급망 프로세스 전체를 하나로 조정하는 상위 개념이고, 로봇 오케스트레이션은 그 가운데 물리적인 작업이 실제로 일어나는 구간에서 로봇과 현장 설비의 행동을 연결하는 실행 계층이다. [의견] 따라서 이 위키에서 ROP는 SCOR의 오케스트레이션을 대체하는 것이 아니라, 업무 시스템의 계획을 현장 행동으로 옮기고 그 결과를 다시 업무 시스템에 되돌려 주는 역할로 다룬다. [의견] {cite_sentence} 자세한 설명은 {L(rel, "about/what-is-rop.md", "SCM 관점의 ROP란 무엇인가")}에 있다.

## 이 위키가 다루는 범위

이 위키는 7개 대분류와 28개 세부 연구영역을 뼈대로 한다. 분류 원문은 이 분류의 성격을 다음과 같이 밝힌다.

{tag_line(SRC.scope_disclaimer_sentence)}

대분류·세부영역의 명칭·번호·정의·질문은 원문 그대로 쓰며 바꾸지 않는다. 새 세부영역이 필요해 보이면 분류를 바꾸지 않고 {L(rel, "open-questions.md", "열린 질문")}에 "분류 확장 제안"으로 기록한다.

## 대분류 표

아래 표의 대분류·핵심 질문·세부영역 열은 원문 1장의 표를 그대로 옮긴 것이고, 대분류 페이지와 세부 연구영역 열은 위키에서 덧붙인 것이다.

{table}

{TAG}

## 다루지 않는 것

ROP가 직접 소유하지 않고 외부 시스템과 연계하는 영역을 원문 9장은 다섯 가지 경계로 정리한다. 아래 목록은 원문 9장 표의 "경계" 열과 "주로 연계할 외부 영역" 열을 위키에서 한 줄씩 이어 붙인 요약이다. 셀의 문구는 원문과 같지만 이 줄 자체는 원문에 없는 문장이므로 `[분류원문]` 태그를 붙이지 않는다.

{scope_lines}

이 영역들은 ROP가 직접 만들지 않고 "연계 대상"으로 다룬다. 원문 9장의 표 전체(ROP에서 다룰 내용 열 포함)와 이 경계가 제품 전략에 따라 이동할 수 있다는 원문 설명은 {L(rel, "about/scope-boundary.md", "ROP가 직접 소유할 범위와 외부 연계 경계")}에 원문 그대로 있다.

## 콘텐츠가 만들어지는 방식

세 에이전트가 매일 1회 한 영역을 다룬다. 리서치 에이전트가 근거 있는 조사 브리프를 만들고, 내용 검증 에이전트가 출처의 실재와 주장–출처 일치를 검증해 게시 가능 여부를 판정하며, 스토리텔러 에이전트가 검증을 통과한 브리프만으로 페이지를 쓴다. 마지막으로 퍼블리셔 스크립트가 원문 보호·링크·프런트매터 검사를 거쳐 위키에 반영한다. 첫 주기(28회)는 세부영역 {first_area}부터 {last_area}까지 번호순으로 본문을 채우고, 그 뒤에는 오래된 영역·열린 질문·비어 있는 매트릭스 칸을 기준으로 대상을 고른다. 각 에이전트의 역할·입력·출력과 사람이 개입하는 지점은 {L(rel, "about/agents.md", "에이전트 소개")}에 있다.

## 진행 중인 중점 연구 트랙

트랙은 분류를 바꾸지 않고 여러 세부영역을 가로지르는 집중 연구 프로그램이다. 아래 현황은 퍼블리셔가 자동으로 갱신한다.

{ar.wrap("home-track-status")}

## 표기 범례

페이지 상태는 프런트매터 `status` 로 표시한다.

| 상태 | 의미 |
|---|---|
| seed | 원문 정의만 있고 본문이 없음 |
| draft | 스토리텔러 초안, 2차 검증 전 |
| verified | 2차 검증 통과, 게시 대기 |
| published | 게시됨 |
| needs_update | 정정 요청이 있거나 기준일이 오래되어 재검증 필요 |
| deprecated | 대체되었거나 더 이상 유효하지 않음. 대체 페이지 링크 필수 |

신뢰도(`confidence`)는 내용 검증 에이전트가 부여한다. high 는 핵심 주장이 2개 이상의 독립 출처로 확인된 것, medium 은 단일 출처이거나 벤더·기사 중심인 것, low 는 추정·의견 비중이 높은 것이다.

본문의 주장에는 태그를 붙인다. `[사실]`은 출처로 확인된 주장, `[추정]`은 근거는 있으나 확인이 부족한 주장(벤더 주장 포함), `[의견]`은 작성자의 해석이다. `[분류원문]`은 분류 원문에서 한 글자도 바꾸지 않고 옮긴 문장, `[가설]`은 중점 연구 트랙에서 검증할 가설, `[사용자 실험]`은 사용자가 직접 수행한 실험 결과다. 출처는 `[^ref-001]` 형식의 각주로 붙인다. 자세한 읽는 법은 {L(rel, "about/reading-guide.md", "읽기 가이드")}에 있다.

## 최근 업데이트

{ar.wrap("home-recent")}

## 시작하기 좋은 페이지

- {L(rel, "about/research-method.md", "SCM 관점의 연구 시작 방법")} — 물류 흐름 7단계와 여섯 항목으로 기술을 교차해 보는 방법
- {L(rel, "flow-matrix.md", "물류 흐름 매트릭스")} — 입고부터 반품까지 각 단계에서 어떤 페이지가 어떤 항목을 다루는지
- {L(rel, f"tracks/{TRACK_SLUG}/index.md", "매뉴얼 기반 로봇 기능 온톨로지 트랙 개요")} — 진행 중인 중점 연구 트랙
- {L(rel, "glossary/index.md", "용어집")} — SCOR, ISA-95, EPCIS, Open-RMF, MRTA, MAPF 같은 용어의 한 줄 정의
- {L(rel, "open-questions.md", "열린 질문")} — 아직 답하지 못한 질문과 그 상태

## 정정과 요청

틀린 문장, 오래된 사실, 우선 조사할 주제가 있으면 {L(rel, "about/how-to-contribute.md", "기여·정정 방법")}의 절차를 따른다. 정정 요청은 다음 실행의 검증 항목에 포함되고, 처리 결과는 {L(rel, "changelog.md", "변경 이력")}에 남는다.
"""
    emit(rel, meta("ROP 연구 위키", "home"), body)


# --- 소개 -------------------------------------------------------------------------

def build_about() -> None:
    # 1) SCM 관점의 ROP란 무엇인가 — 원문 1장 전체
    rel = "about/what-is-rop.md"
    ch1 = SRC.chapter_text(1)
    cite_sentence, refs = citation_note(rel, ch1)
    body = f"""{crumb(rel, ("SCM 관점의 ROP란 무엇인가", None))}

# SCM 관점의 ROP란 무엇인가

이 페이지는 분류 원문 1장 "전체 관점"을 그대로 옮긴 것이다. ASCM(Association for Supply Chain Management)의 SCOR(Supply Chain Operations Reference)가 공급망 프로세스의 범위를, ISA-95 가 기업 업무와 제조 운영·제어의 통합 경계를 참고 기준으로 제시하는 가운데, 원문은 ROP를 "물리적인 작업이 발생하는 부분을 연결하는 역할"로 본다. 즉 ROP는 SCOR 오케스트레이션 전체를 대체하는 것이 아니라, 그 계획을 로봇과 현장 설비의 실제 행동으로 옮기고 결과를 업무 시스템에 되돌려 주는 실행 플랫폼이다. [의견]

아래 본문과 표는 원문 그대로이며 `[분류원문]`으로 표시한다. 원문의 `[n]` 표기는 원문 12장 참고 자료의 n번 항목이며, 이 위키의 참고문헌 `ref-00n` 페이지에 해당한다.

## 원문 1장. 전체 관점

{tag_blocks(ch1).rstrip()}

## 원문 각주와 참고문헌

{cite_sentence} 참고문헌 전체 목록은 {L(rel, "references/index.md", "참고문헌")}에 있다.

## 관련 페이지

- {L(rel, "about/scope-boundary.md", "ROP가 직접 소유할 범위와 외부 연계 경계")}
- {L(rel, "about/research-method.md", "SCM 관점의 연구 시작 방법")}
- {L(rel, "about/idea-mapping.md", "논의한 아이디어의 연구영역 매핑")}
- 대분류 페이지: {", ".join(cat_link(rel, c.letter) for c in SRC.categories)}

## 참고 자료

{footnotes(refs)}
"""
    emit(rel, meta("SCM 관점의 ROP란 무엇인가", "about"), body)

    # 2) ROP가 직접 소유할 범위와 외부 연계 경계 — 원문 9장
    rel = "about/scope-boundary.md"
    body = f"""{crumb(rel, ("ROP가 직접 소유할 범위와 외부 연계 경계", None))}

# ROP가 직접 소유할 범위와 외부 연계 경계

이 페이지는 분류 원문 9장을 표와 설명 문단(경계가 제품 전략에 따라 이동한다는 문단 포함)까지 그대로 옮긴 것이다. 위키의 모든 페이지는 범위 판단을 이 장을 기준으로 하며, "주로 연계할 외부 영역"에 속하는 내용은 ROP 직접 범위처럼 서술하지 않고 연계 대상으로 짧게 다룬다.

## 원문 9장. ROP가 직접 소유할 범위와 외부 연계 경계

{tag_blocks(SRC.chapter_text(9)).rstrip()}

## 관련 페이지

- {L(rel, "about/what-is-rop.md", "SCM 관점의 ROP란 무엇인가")}
- 세부영역 페이지의 "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)" 섹션이 이 경계를 영역별로 적용한다.
"""
    emit(rel, meta("ROP가 직접 소유할 범위와 외부 연계 경계", "about"), body)

    # 3) SCM 관점의 연구 시작 방법 — 원문 11장
    rel = "about/research-method.md"
    body = f"""{crumb(rel, ("SCM 관점의 연구 시작 방법", None))}

# SCM 관점의 연구 시작 방법

이 페이지는 분류 원문 11장을 그대로 옮긴 것이다. 물류 흐름 7단계(입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품)와 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과)을 교차한 표가 {L(rel, "flow-matrix.md", "물류 흐름 매트릭스")}이며, 스토리텔러 에이전트가 쓰는 현장 시나리오는 이 여섯 항목으로 구성한다.

## 원문 11장. SCM 관점의 연구 시작 방법

{tag_blocks(SRC.chapter_text(11)).rstrip()}

## 관련 페이지

- {L(rel, "flow-matrix.md", "물류 흐름 매트릭스")} — 7단계 × 여섯 항목의 채움 현황과 관련 페이지 링크
- {L(rel, "about/scope-boundary.md", "ROP가 직접 소유할 범위와 외부 연계 경계")}
"""
    emit(rel, meta("SCM 관점의 연구 시작 방법", "about"), body)

    # 4) 논의한 아이디어의 연구영역 매핑 — 원문 10장
    rel = "about/idea-mapping.md"
    related_lines = []
    for row in SRC.idea_rows:
        links = []
        for cell in (row["primary"], row["related"]):
            for m in re.finditer(r"(?<![\d.])(\d{1,2})(?=[.+])", cell):
                no = int(m.group(1))
                if no in SRC.areas and area_link(rel, no) not in links:
                    links.append(area_link(rel, no))
            rm = re.search(r"([A-G])~([A-G])", cell)
            if rm:
                for letter in paths.CATEGORY_LETTERS:
                    if rm.group(1) <= letter <= rm.group(2):
                        links.append(cat_link(rel, letter))
        related_lines.append(f"- {row['idea']}: " + ", ".join(links))
    body = f"""{crumb(rel, ("논의한 아이디어의 연구영역 매핑", None))}

# 논의한 아이디어의 연구영역 매핑

이 페이지는 분류 원문 10장의 표를 그대로 옮긴 것이다. 표 안의 영역 표기는 원문 그대로 두고, 각 아이디어가 언급하는 세부영역·대분류 페이지 링크를 표 아래 "관련 페이지"에 따로 둔다. 첫 번째 아이디어(매뉴얼 기반 로봇 온톨로지)는 중점 연구 트랙 {L(rel, f"tracks/{TRACK_SLUG}/index.md", "매뉴얼 기반 로봇 기능 온톨로지")}로 진행 중이다.

## 원문 10장. 논의한 아이디어의 연구영역 매핑

{tag_blocks(SRC.chapter_text(10)).rstrip()}

## 관련 페이지

{chr(10).join(related_lines)}
"""
    emit(rel, meta("논의한 아이디어의 연구영역 매핑", "about"), body)


# --- 대분류 -----------------------------------------------------------------------

def build_categories() -> None:
    for cat in SRC.categories:
        rel = paths.category_index_rel(cat.letter)
        notes_text = "\n\n".join(tag_line(n) for n in cat.notes) if cat.notes else "(원문에 표 아래 설명 문단이 없다.)"
        cite_sentence, refs = citation_note(rel, "\n".join(cat.notes))
        ref_section = ""
        if refs:
            ref_section = f"""
## 참고 자료

{cite_sentence}

{footnotes(refs)}
"""
        body = f"""{crumb(rel, (cat.title, None))}

# {cat.title}

## 핵심 질문

{tag_line(cat.core_question)}

## 개요

{tag_line(cat.intro_paragraph)}

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·SCM 관점의 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

{ar.wrap("category-area-table")}

## 이 대분류의 핵심 포인트

{notes_text}

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 최근 업데이트

{ar.wrap("category-recent")}
{ref_section}"""
        emit(rel, meta(cat.title, "category", status="seed"), body)


# --- 세부영역 -----------------------------------------------------------------------

def build_areas() -> None:
    for no in paths.AREA_NOS:
        a = SRC.area(no)
        cat = SRC.category(a.category_letter)
        rel = paths.area_rel_path(no)
        notes = SRC.area_notes(no)
        quote = ""
        refs: list[Reference] = []
        if notes:
            quotes = []
            for n in notes:
                lines = n.split("\n")
                lines[-1] = tag_line(lines[-1])
                quotes.append("> 원문 주석: " + "\n> ".join(lines))
            quote = "\n\n" + "\n\n".join(quotes)
            cite_sentence, refs = citation_note(rel, "\n".join(notes))
            if cite_sentence:
                quote += "\n\n" + cite_sentence
        sections = [f"## {AREA_SECTIONS[0]}\n\n{tag_line(a.what)}",
                    f"## {AREA_SECTIONS[1]}\n\n{tag_line(a.question)}{quote}"]
        for title in AREA_SECTIONS[2:11]:
            sections.append(f"## {title}\n\n{NOT_WRITTEN}")
        sections.append(f"## {AREA_SECTIONS[11]}\n\n{ar.wrap('area-recent')}")
        sections.append(f"## {AREA_SECTIONS[12]}\n\n" + (footnotes(refs) if refs else "(아직 각주가 없다. 본문이 작성되면 출처 각주를 여기에 둔다.)"))
        body = f"""{crumb(rel, (cat.title, paths.category_index_rel(cat.letter)), (a.title, None))}

# {a.title}

!!! info "소속 대분류"
    {L(rel, paths.category_index_rel(cat.letter), cat.title)} — 핵심 질문:
    {tag_line(cat.core_question)}

{chr(10).join(s + chr(10) for s in sections)}"""
        page_meta = meta(a.title, "area", status="seed", category=cat.title, area_no=no,
                         related_areas=[], tags=[])
        page_meta["sources"] = []
        # 순서: title,type,category,area_no,related_areas,tags,status,created,updated,sources,version
        ordered = {k: page_meta[k] for k in ["title", "type", "category", "area_no", "related_areas", "tags",
                                             "status", "created", "updated", "sources", "version"]}
        emit(rel, ordered, body)


# --- 참고문헌 -----------------------------------------------------------------------

def load_url_check() -> tuple[str | None, dict[str, dict]]:
    """data/url_check.json → (확인 시각(YYYY-MM-DD), {ref_id: 항목}). 없으면 (None, {}).
    새 형식(items 가 {ref_id: {status, …}})과 구 형식(items 목록, result 필드)을 모두 받는다(lib/sources.load_url_check).
    항목에는 구 형식 호환용 result(열림이면 "열림")를 채워 둔다."""
    from lib import sources  # 지연 import: 기본 scaffold 경로는 이 모듈을 쓰지 않는다
    uc = sources.load_url_check(path=URL_CHECK_FILE)
    items = {rid: {**it, "ref_id": rid, "result": it.get("result") or ("열림" if it.get("status") == "열림" else it.get("status"))}
             for rid, it in (uc.get("items") or {}).items()}
    checked = str(uc.get("checked_at") or "")[:10] or None
    return checked, items


def ref_access(stype: str, checked: str | None, item: dict | None) -> dict:
    """참고문헌의 신뢰도·원문 열람 표기. URL 열림이 확인되면 유형 기준 신뢰도, 아니면 medium 상한 + 원문 미열람."""
    by_type = REF_RELIABILITY[stype]
    verified = bool(item and item.get("result") == "열림")
    if verified:
        return {
            "verified": True, "checked": checked, "reliability": by_type, "by_type": by_type,
            "reliability_cell": f"{by_type} (유형 기준)",
            "access_cell": f"확인 ({checked}, URL 열림)",
            "accessed_cell": f"{checked}",
            "note": f"원문 열람: 확인. {checked} 에 pipeline/checks/check_urls.py 로 URL 이 열리는 것을 확인했다. "
                    f"신뢰도는 유형 기준값 {by_type} 을 적용한다. 기관·제목·발행일의 원문 대조는 내용 검증 에이전트가 "
                    "이 출처를 인용하는 실행에서 수행한다.",
        }
    reliability = REF_UNVERIFIED_CAP if by_type == "high" else by_type
    cap_note = f"유형 기준 {by_type}, 원문 미열람으로 {REF_UNVERIFIED_CAP} 상한" if by_type != reliability \
        else f"유형 기준 {by_type}"
    return {
        "verified": False, "checked": checked, "reliability": reliability, "by_type": by_type,
        "reliability_cell": f"{reliability} ({cap_note})",
        "access_cell": "미확인 — 원문 미열람 (구축 환경의 네트워크 정책으로 URL 을 열지 못함)",
        "accessed_cell": f"{TODAY} (열람 시도일, 원문 미열람)",
        "note": "원문 열람: 미확인(원문 미열람). 구축 환경의 네트워크 정책으로 URL 을 열지 못해 기관·제목·발행일을 "
                f"원문과 대조하지 못했다. 신뢰도는 유형 기준값이 {by_type} 이지만 원문 열람이 확인될 때까지 "
                f"{REF_UNVERIFIED_CAP} 상한을 적용한다. 외부 접속이 가능한 환경에서 "
                "`ROP_CHECK_URLS=1 bash pipeline/checks/run_all.sh` 를 실행하면 결과가 `data/url_check.json` 에 남고, "
                "`python3 pipeline/scaffold.py --apply-url-check` 가 이 페이지에 반영한다.",
    }


REF_ACCESS_ROWS = ("신뢰도", "원문 열람", "접근일")


def build_references() -> None:
    rel = "references/index.md"
    body = f"""{crumb(rel, ("참고문헌", None))}

# 참고문헌

이 위키가 인용한 출처의 목록이다. 출처마다 id, 기관, 제목, 발행일, URL, 유형, 신뢰도, 접근일, 요약, 인용된 페이지를 개별 페이지에 둔다. 시드 10건(ref-001 ~ ref-010)은 분류 원문 12장의 참고 자료 1~10번에 그대로 대응한다. 새 출처는 리서치 에이전트가 제안하고 내용 검증 에이전트가 실재를 확인한 뒤 퍼블리셔가 추가한다.

신뢰도는 출처 유형을 기준으로 한다. 표준·정부·연구기관·논문·오픈소스 공식 문서는 high, 기사·보도자료·벤더 문서는 medium 이며, 내용 검증 에이전트가 원문을 열어 확인하면 조정할 수 있다. 다만 URL 을 열어 확인하지 못한 출처(원문 미열람)에는 유형과 무관하게 high 를 주지 않고 {REF_UNVERIFIED_CAP} 상한을 적용한다. 시드 10건은 구축 환경의 네트워크 정책으로 URL 을 열지 못했으므로 모두 원문 미열람 상태이며, 각 페이지의 "원문 열람" 행에 그 사실을 적어 둔다. 외부 접속이 가능한 환경에서 `ROP_CHECK_URLS=1 bash pipeline/checks/run_all.sh` 를 실행한 뒤 `python3 pipeline/scaffold.py --apply-url-check` 를 실행하면 열림이 확인된 출처의 신뢰도가 유형 기준값으로 올라간다.

## 목록

{ar.wrap("references-index")}
"""
    emit(rel, meta("참고문헌", "reference", subtype="index"), body)

    checked, items = load_url_check()
    for ref in SRC.references:
        rel = f"references/{ref.id}.md"
        stype = REF_TYPES[ref.n]
        acc = ref_access(stype, checked, items.get(ref.id))
        body = f"""{crumb(rel, ("참고문헌", "references/index.md"), (ref.id, None))}

# {ref.id} — {ref.title}

| 항목 | 값 |
|---|---|
| id | {ref.id} |
| 기관 | {ref.org} |
| 제목 | {ref.title} |
| 발행일 | {ref.published} |
| URL | <{ref.url}> |
| 유형 | {stype} |
| 신뢰도 | {acc["reliability_cell"]} |
| 원문 열람 | {acc["access_cell"]} |
| 접근일 | {acc["accessed_cell"]} |

## 요약

원문 12장 항목의 설명 문구가 이 출처의 한두 문장 요약이다. 항목 전체를 원문 그대로 옮기면 다음과 같다.

{tag_line(ref.raw)}

{acc["note"]}

## 인용된 페이지

이 출처를 프런트매터 `sources` 또는 각주 `[^{ref.id}]` 로 인용했거나 이 페이지로 링크한 페이지의 목록이다. 퍼블리셔가 docs 전체를 스캔해 자동으로 갱신한다.

{ar.wrap("reference-cited-pages")}

## 각주 형식

이 출처를 인용할 때 쓰는 각주 정의는 다음과 같다.

```
{ref.footnote(TODAY)}
```
"""
        page_meta = {
            "title": f"{ref.id} — {ref.title}", "type": "reference", "ref_id": ref.id, "org": ref.org,
            "ref_title": ref.title, "url": ref.url, "source_type": stype,
            "reliability": acc["reliability"], "reliability_by_type": acc["by_type"],
            "url_verified": acc["verified"], "url_checked": acc["checked"] if acc["verified"] else None,
            "published": ref.published, "accessed": TODAY, "related_areas": [],
            "status": "seed", "created": TODAY, "updated": TODAY, "version": 1,
        }
        if not acc["verified"]:
            page_meta.pop("url_checked")
        emit(rel, page_meta, body)


def apply_url_check(changelog: bool = True) -> list[str]:
    """data/url_check.json(pipeline/checks/check_urls.py 결과)을 참고문헌 페이지에 반영한다. 바뀐 페이지 목록을 돌려준다.

    1. 정본 URL 이 열리지 않았지만 GitHub 원문 미러(relation original)가 열린 참고문헌은 미러 원문을 받아
       data/source_texts/<ref_id>.txt 에 저장한다(fetched_via: github_raw). 받지 못하면 원문 미열람으로 남는다.
    2. 모든 참고문헌 페이지를 lib/sources.sync_reference_page 로 맞춘다: 프런트매터 url_status·url_checked(·URL 이 열리면 url_verified),
       원문 텍스트가 있으면 fetched·fetched_via·source_text, 서지 정보 표의 원문 열람 행, 각주 형식 줄, 비고 절의 원문 열람 상태 표.
       신뢰도의 medium 상한은 원문을 실제로 열람(fetched)했을 때만 푼다 — URL 이 열리는 것만으로는 풀지 않는다(원문 열람 규칙, apply_fetch_caps 와 같은 기준).
    3. 바뀐 페이지는 updated 를 오늘로, version 을 +1 한다. changelog 이면 data/changelog.json 에 항목을 남긴다. 그 뒤 main() 이 auto 영역을 다시 채운다."""
    from lib import sources
    uc = sources.load_url_check(path=URL_CHECK_FILE)
    if not uc.get("items"):
        print(f"[scaffold] {URL_CHECK_FILE.relative_to(paths.ROOT)} 이 없거나 비어 있다. "
              "먼저 `python3 pipeline/checks/check_urls.py` 를 실행한다(결과는 data/url_check.json).")
        return []
    for line in sources.ingest_mirror_texts(None, url_check=uc, only_open=True, today=TODAY):
        log(f"[mirror] {line}")
    texts = sources.load_source_texts()
    changed: list[str] = []
    entries: list[dict] = []
    for p in sorted((DOCS / "references").glob("ref-*.md")):
        notes = sources.sync_reference_page(p, url_check=uc, texts=texts, today=TODAY)
        if not notes:
            continue
        rel = f"docs/{p.relative_to(DOCS).as_posix()}"
        changed.append(rel)
        rid = p.stem
        it = (uc.get("items") or {}).get(rid) or {}
        summary = f"URL 확인 반영({it.get('status') or '결과 없음'}, {str(uc.get('checked_at') or '')[:10]})"
        if rid in texts and any(n.startswith("fetched:") for n in notes):
            summary += f", 원문 열람 표시({sources.VIA_LABELS.get(str(texts[rid].get('fetched_via')), '')})"
        rel_note = next((n for n in notes if n.startswith("신뢰도")), None)
        if rel_note:
            summary += f", {rel_note}"
        entries.append({"date": TODAY, "run_id": f"url-check-{TODAY}", "action": "갱신", "page": rel, "summary": summary})
        log(f"[write] {rel} ({'; '.join(notes)})")
    if changelog and entries:
        sources.append_changelog(entries)
    return changed


# --- 용어집·횡단·색인 ----------------------------------------------------------------

def build_glossary_index() -> None:
    rel = "glossary/index.md"
    body = f"""{crumb(rel, ("용어집", None))}

# 용어집

이 위키에서 쓰는 용어의 한글·영문 표기와 한 줄 정의를 모은다. 용어마다 개별 페이지에 설명, 관련 연구영역, 출처를 둔다. 시드 용어는 SCOR, ISA-95, EPCIS, Open-RMF, Fleet Adapter, WES/WCS/WMS/MES/TMS, MRTA, MAPF, Lifelong MAPF, Multi-Agent Pickup and Delivery, ARIAC, DDS-Security, 디지털 트윈이다. 새 용어는 스토리텔러 에이전트가 제안하고 퍼블리셔가 반영한다.

아래 표는 용어 페이지의 프런트매터(term_ko, term_en, definition, related_areas)에서 자동으로 만든다.

## 용어 목록

{ar.wrap("glossary-index")}
"""
    emit(rel, meta("용어집", "glossary", subtype="index"), body)


def build_cross_pages() -> None:
    rel = "flow-matrix.md"
    body = f"""{crumb(rel, ("물류 흐름 매트릭스", None))}

# 물류 흐름 매트릭스

행은 원문 11장의 물류 흐름 7단계(입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품), 열은 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과)이다. 각 칸에는 그 단계·항목을 다룬 페이지의 링크를 두고, 아직 다룬 페이지가 없으면 "비어 있음"으로 표시한다. 스토리텔러 에이전트가 현장 시나리오를 쓸 때 다룬 칸을 출력하고, 퍼블리셔가 `data/flow_matrix.json` 에 반영해 이 표를 다시 그린다.

이 매트릭스는 기술 목록에 실제 물류 흐름을 교차해 보는 도구다. 채움률이 낮은 단계·항목은 대상 선정에서 가산점을 받아 먼저 조사된다. 방법 설명은 {L(rel, "about/research-method.md", "SCM 관점의 연구 시작 방법")}에 있다.

## 매트릭스

{ar.wrap("flow-matrix")}
"""
    emit(rel, meta("물류 흐름 매트릭스", "matrix"), body)

    rel = "open-questions.md"
    body = f"""{crumb(rel, ("열린 질문", None))}

# 열린 질문

아직 해결되지 않은 질문의 목록이다. 질문마다 관련 영역, 제기일, 제기한 실행, 상태(열림 / 조사 중 / 해결 / 보류), 해결 시 링크를 둔다. 세 에이전트 모두 질문을 제기할 수 있고, 해결 판정은 내용 검증 에이전트가 한다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시한 뒤 여기에 올린다. 새 세부영역이 필요해 보이면 분류를 바꾸지 않고 "분류 확장 제안"으로 여기에 기록한다.

중점 연구 트랙 전용 질문은 트랙의 질문 백로그에 두고, 여기에는 링크만 둔다. 이 표는 `data/open_questions.json` 에서 자동으로 만든다.

## 목록

{ar.wrap("open-questions")}
"""
    emit(rel, meta("열린 질문", "questions"), body)

    rel = "changelog.md"
    body = f"""{crumb(rel, ("변경 이력", None))}

# 변경 이력

날짜별로 생성·갱신·폐기된 페이지, 실행 id, 한 줄 요약을 기록한다. 퍼블리셔가 `data/changelog.json` 에서 자동으로 만든다. 정정 요청의 처리 결과도 여기에 남는다.

## 이력

{ar.wrap("changelog")}
"""
    emit(rel, meta("변경 이력", "changelog"), body)

    rel = "metrics.md"
    body = f"""{crumb(rel, ("운영 지표", None))}

# 운영 지표

영역별 페이지 상태 분포, 검증 통과율, 반려·보류 건수, 출처 유형 분포, 물류 흐름 매트릭스 채움률, 마지막 갱신이 오래된 영역을 퍼블리셔가 계산한다. 원천은 페이지 프런트매터(status, updated), `data/changelog.json`, `data/flow_matrix.json`, `runs/<run_id>/summary.json`, 참고문헌 페이지의 `source_type` 이다.

## 지표

{ar.wrap("metrics")}
"""
    emit(rel, meta("운영 지표", "metrics"), body)


def build_indexes() -> None:
    rel = "topics/index.md"
    body = f"""{crumb(rel, ("주제", None))}

# 주제 페이지 목록

주제 페이지는 파이프라인 2주기부터 매일 생성되는 글이다. 하나의 주 연구영역과 0개 이상의 관련 영역을 갖고, 세 줄 요약 → 배경 → 본문 → 현장 시나리오 → ROP 관점의 시사점 → 연결되는 연구영역 → 열린 질문 → 출처 → 검증 노트 → 이력 순서로 구성된다. 중점 연구 트랙 실행에서 나온 주제 페이지는 프런트매터에 `track` 을 갖고 트랙 단계 페이지에서 링크된다.

파일은 `docs/topics/YYYY/YYYY-MM-DD-slug.md` 에 두며, 아래 목록은 프런트매터에서 자동으로 만든다.

## 목록

{ar.wrap("topics-index")}
"""
    emit(rel, meta("주제", "topic", subtype="index"), body)

    rel = "logs/index.md"
    body = f"""{crumb(rel, ("로그", None))}

# 운영 로그

일일 로그(`logs/daily/YYYY-MM-DD.md`)는 실행 id, 날짜, 실행 유형, 대상 영역, 단계별 결과와 소요 시간, 검증 판정, 생성·갱신 페이지, 신규 출처 수, 반려·보류 사유, 예산 사용량, 다음 실행 메모를 담는다. 주간 정리(`logs/weekly/YYYY-Www.md`)는 이번 주 다룬 영역, 새로 확인된 사실, 강등·폐기된 주장, 열린 질문 변동, 다음 주 후보를 담는다. 둘 다 파이프라인이 자동으로 만든다.

## 목록

{ar.wrap("logs-index")}
"""
    emit(rel, meta("로그", "log", subtype="index"), body)


# --- data 시드 -------------------------------------------------------------------------

RESET_DATA = False


def seed_data() -> None:
    """data/*.json 시드. 상태 데이터이므로 --force 로도 덮어쓰지 않고 --reset-data 일 때만 되돌린다."""
    DATA.mkdir(parents=True, exist_ok=True)
    seeds = {
        "open_questions.json": {"items": []},
        "changelog.json": {"items": [{
            "date": TODAY, "run_id": BUILD_RUN_ID, "action": "생성", "page": "docs/",
            "summary": "위키 뼈대 생성(홈·소개·대분류·세부영역·횡단·트랙 시드)",
        }]},
        "flow_matrix.json": {"steps": paths.FLOW_STEPS, "items": paths.FLOW_ITEMS, "cells": {}},
    }
    for name, obj in seeds.items():
        p = DATA / name
        if p.exists() and not RESET_DATA:
            log(f"[skip] data/{name} (이미 있음, --reset-data 로만 되돌린다)")
            continue
        p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        _written.append(f"data/{name}")
        log(f"[write] data/{name}")


# --- 실행 -----------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    global VERBOSE, FORCE, RESET_DATA
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--force", action="store_true", help="이미 있는 페이지도 덮어쓴다(data/*.json 제외)")
    ap.add_argument("--reset-data", action="store_true", help="data/{open_questions,changelog,flow_matrix}.json 을 시드로 되돌린다")
    ap.add_argument("--refresh-auto", action="store_true", help="auto 영역 갱신과 mkdocs.yml 생성만 실행")
    ap.add_argument("--apply-url-check", action="store_true", help="data/url_check.json 을 참고문헌 페이지에 반영")
    ap.add_argument("--no-changelog", action="store_true", help="--apply-url-check 가 data/changelog.json 에 기록하지 않게 한다")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args(argv)
    VERBOSE, FORCE, RESET_DATA = args.verbose, args.force, args.reset_data

    if args.apply_url_check:
        changed = apply_url_check(changelog=not args.no_changelog)
        print(f"[scaffold] URL 확인·원문 열람 반영: 참고문헌 {len(changed)}개 페이지")
    elif not args.refresh_auto:
        build_home()
        build_about()
        build_categories()
        build_areas()
        build_references()
        build_glossary_index()
        build_cross_pages()
        build_indexes()
        seed_data()
        print(f"[scaffold] 페이지·데이터 {len(_written)}개 생성 (기존 파일은 건드리지 않음{', --force' if FORCE else ''})")
    changed = refresh_all_auto_regions(verbose=VERBOSE)
    print(f"[scaffold] auto 영역 갱신: {len(changed)}개 페이지")
    p = write_mkdocs_yml()
    print(f"[scaffold] {p.relative_to(paths.ROOT)} 생성")
    return 0


if __name__ == "__main__":
    sys.exit(main())
