#!/usr/bin/env python3
"""개념 재정립 A~C 단계 문서 생성·검증 (루프 프롬프트 4~6장).

data/structure.yaml, data/items_*.yaml, data/mapping.yaml, data/loop_log.yaml(있으면)을 읽어
01_list.md, 02_categories.md, 03_mapping.md, 04_verify.md 를 이 폴더에 다시 만든다.
검증 6항목을 계산해 04에 쓰고, 하나라도 실패하면 종료 코드 1을 돌려준다.
숫자(항목 수, 옛 경로, 링크 파일 수, 출처 수)는 데이터와 docs/ 를 직접 세서 쓴다. 문서를 손으로 고치지 않는다.

실행: python3 rop-wiki/_work/scope/build_scope.py
"""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
WIKI = HERE.parents[1]
DOCS = WIKI / "docs"
DATA = HERE / "data"
TODAY = "2026-09-28"
BANNED = ["SCM", "SCOR", "공급망 관점"]
# 검사 4 보조 지표: 항목 이름·정의 문구에 나오는 현장 용어(현장 유형 칸이 ‘전체’여도 문구가 한 현장에 치우칠 수 있어서 따로 센다)
SITE_TERMS = {
    "물류창고": ["창고", "물류", "피킹", "입고", "출하", "재고", "화물", "팔레트", "적치", "보충", "포장"],
    "제조 공장": ["공장", "공정", "라인", "생산"],
    "병원": ["병원", "환자", "검체", "약품", "간호", "감염"],
    "상업 시설": ["호텔", "객실", "식당", "매장", "쇼핑", "서빙"],
    "가정": ["가정", "집안일", "거주자", "공동주택", "아파트"],
    "실외": ["실외", "보도", "캠퍼스", "위성", "GIS", "도로"],
}
GEN = "이 문서는 `build_scope.py`가 `data/*.yaml`에서 만든다. 고칠 때는 데이터를 고치고 다시 생성한다."


# ---------------------------------------------------------------- 읽기
def load():
    st = yaml.safe_load((DATA / "structure.yaml").read_text(encoding="utf-8"))
    items: list[dict] = []
    for p in sorted(DATA.glob("items_*.yaml")):
        items += yaml.safe_load(p.read_text(encoding="utf-8")) or []
    mp = yaml.safe_load((DATA / "mapping.yaml").read_text(encoding="utf-8"))
    lp = DATA / "loop_log.yaml"
    log = (yaml.safe_load(lp.read_text(encoding="utf-8")) or []) if lp.exists() else []
    return st, items, mp, log


def cell(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


def join(xs, sep=", ") -> str:
    return sep.join(str(x) for x in xs) if xs else "-"


def pct(n: int, d: int) -> str:
    return f"{(100.0 * n / d):.1f}%" if d else "-"


# ---------------------------------------------------------------- 계산
class Model:
    def __init__(self, st, items, mp, log):
        self.st, self.items, self.mp, self.log = st, items, mp, log
        self.cats = {c["id"]: c for c in st["categories"]}
        self.cat_order = [c["id"] for c in st["categories"]]
        self.areas = {a["id"]: a for a in st["areas"]}
        self.area_order = [a["id"] for a in st["areas"]]
        self.items_by_area = defaultdict(list)
        for it in items:
            self.items_by_area[it["area"]].append(it)
        self.areas_by_cat = defaultdict(list)
        for a in st["areas"]:
            self.areas_by_cat[a["cat"]].append(a)
        self.succ = {c["id"]: c["successor"] for c in mp["old_categories"]}
        self.old_cat_by_id = {c["id"]: c for c in mp["old_categories"]}
        # 디스크에서 옛 경로 찾기
        self.old_area_path = {}
        for p in sorted((DOCS / "categories").glob("*/[0-9][0-9]-*.md")):
            self.old_area_path[int(p.name[:2])] = p.relative_to(DOCS).as_posix()
        self.old_cat_path = {}
        for c in mp["old_categories"]:
            p = DOCS / "categories" / c["slug"] / "index.md"
            self.old_cat_path[c["id"]] = p.relative_to(DOCS).as_posix() if p.exists() else None

    def cat_of(self, area_id):
        return self.cats[self.areas[area_id]["cat"]]

    def area_label(self, aid):
        return f"{aid} {self.areas[aid]['name']}"

    def new_area_path(self, aid):
        a = self.areas[aid]
        return f"categories/{self.cats[a['cat']]['slug']}/{a['slug']}.md"

    def new_cat_path(self, cid):
        return f"categories/{self.cats[cid]['slug']}/index.md"

    def area_action(self, oa):
        new = self.areas[oa["main"]]
        if oa.get("parts"):
            return "분할"
        if new["name"] != oa["name"]:
            return "이름 변경"
        if new["cat"] == self.succ[oa["cat"]]:
            return "유지"
        return "이동"

    def area_origin(self, aid):
        mains = [oa['num'] for oa in self.mp["old_areas"] if oa["main"] == aid]
        parts = [oa['num'] for oa in self.mp["old_areas"] if aid in (oa.get("parts") or [])]
        if mains:
            return "계승", mains, parts
        if parts:
            return "일부에서 시작", mains, parts
        return "신규", mains, parts


def consistency(m: Model) -> list[str]:
    errs: list[str] = []
    st, items, mp = m.st, m.items, m.mp
    lens = st["lenses"]
    for k, n in Counter(i["id"] for i in items).items():
        if n > 1:
            errs.append(f"항목 id 중복: {k}")
    for key in ("id", "slug"):
        for k, n in Counter(c[key] for c in st["categories"]).items():
            if n > 1:
                errs.append(f"카테고리 {key} 중복: {k}")
        for k, n in Counter(a[key] for a in st["areas"]).items():
            if n > 1:
                errs.append(f"영역 {key} 중복: {k}")
    for a in st["areas"]:
        if a["cat"] not in m.cats:
            errs.append(f"영역 {a['id']}: 없는 카테고리 {a['cat']}")
    must_cat = {"온톨로지": "B", "채팅": "C"}
    for it in items:
        iid = it["id"]
        if it["area"] not in m.areas:
            errs.append(f"{iid}: 없는 영역 {it['area']}")
            continue
        for fld, key in (("who", "누가"), ("when", "언제"), ("what", "무엇")):
            for v in it.get(fld) or []:
                if v not in lens[key]:
                    errs.append(f"{iid}: {key} 렌즈에 없는 값 '{v}'")
        site = it.get("site") or []
        if not site:
            errs.append(f"{iid}: 현장 유형이 비어 있다")
        if "전체" in site and len(site) > 1:
            errs.append(f"{iid}: ‘전체’와 특정 현장을 함께 적었다")
        for v in site:
            if v != "전체" and v not in lens["어디"]:
                errs.append(f"{iid}: 어디 렌즈에 없는 값 '{v}'")
        if not it.get("who") or not it.get("when"):
            errs.append(f"{iid}: 관련 역할 또는 시기가 비어 있다")
        must = it.get("must") or ""
        if must:
            allowed = st["mandatory"][must]["required"] + st["mandatory"][must]["extra"]
            if it.get("sub") not in allowed:
                errs.append(f"{iid}: 필수({must}) 하위 항목 '{it.get('sub')}'이 목록에 없다")
            if m.areas[it["area"]]["cat"] != must_cat[must]:
                errs.append(f"{iid}: 필수({must}) 항목이 {must_cat[must]} 밖({it['area']})에 있다")
        if it.get("origin") not in ("필수", "기존", "신규"):
            errs.append(f"{iid}: origin 값 오류")
        for fld in ("name", "def", "out"):
            if not str(it.get(fld) or "").strip():
                errs.append(f"{iid}: {fld} 비어 있음")
    for aid in m.area_order:
        if not m.items_by_area.get(aid):
            errs.append(f"영역 {aid}에 항목이 없다")
    for cid in m.cat_order:
        if not m.areas_by_cat.get(cid):
            errs.append(f"카테고리 {cid}에 영역이 없다")
    for oa in mp["old_areas"]:
        if oa["main"] not in m.areas:
            errs.append(f"옛 영역 {oa['num']}: 없는 새 영역 {oa['main']}")
        for p in oa.get("parts") or []:
            if p not in m.areas:
                errs.append(f"옛 영역 {oa['num']}: 없는 새 영역 {p}")
    for oc in mp["old_categories"]:
        if oc["successor"] not in m.cats:
            errs.append(f"옛 대분류 {oc['id']}: 없는 새 카테고리 {oc['successor']}")
    mains = Counter(oa["main"] for oa in mp["old_areas"])
    for k, n in mains.items():
        if n > 1:
            errs.append(f"새 영역 {k}이 옛 영역 {n}개의 주 대상이다(병합) — 처리 종류 계산 규칙을 확인할 것")
    return errs


def disk_counts(m: Model) -> dict:
    """주소 영향·링크 갱신 범위를 docs/ 에서 센다."""
    old_slugs = [c["slug"] for c in m.mp["old_categories"]]
    link_files = 0
    for p in DOCS.rglob("*.md"):
        t = p.read_text(encoding="utf-8")
        if any(s in t for s in old_slugs):
            link_files += 1
    topics = sum(1 for p in (DOCS / "topics").rglob("*.md")
                 if re.search(r"^primary_area_no:", p.read_text(encoding="utf-8"), re.M))
    area_no_pages = sum(1 for p in DOCS.rglob("*.md")
                        if re.search(r"^(area_no|primary_area_no|related_areas):", p.read_text(encoding="utf-8"), re.M))

    def track_pages(slug):
        d = DOCS / "tracks" / slug
        return sorted(d.glob("*.md")) if d.is_dir() else []

    def uniq_refs(paths):
        s = set()
        for p in paths:
            s |= set(re.findall(r"ref-\d{3,}", p.read_text(encoding="utf-8")))
        return len(s)

    chat = track_pages("nl-task-chatbot")
    fp = track_pages("floorplan-recognition")
    return {
        "link_files": link_files,
        "topics_with_primary": topics,
        "pages_with_area_fields": area_no_pages,
        "chat_pages": len(chat),
        "chat_stage_refs": uniq_refs([p for p in chat if p.name.startswith("stage-")]),
        "fp_pages": len(fp),
        "fp_stage_refs": uniq_refs([p for p in fp if p.name.startswith("stage-")]),
        "track_configs": len(list((WIKI / "config" / "tracks").glob("*.yaml"))),
        "idea_pages": len(list((DOCS / "ideas").glob("*.md"))),
        "flow_matrix": (DOCS / "flow-matrix.md").exists(),
    }


# ---------------------------------------------------------------- 01
ITEM_HEAD = ("| id | 이름 | 한 줄 정의 | 산출물 또는 책임 | 관련 역할 | 시기 | 종류 | 현장 유형 | 근거 | 필수 | 배치(B단계) |\n"
             "|---|---|---|---|---|---|---|---|---|---|---|")


def item_row(m: Model, it: dict) -> str:
    must = f"필수({it['must']}·{it['sub']})" if it.get("must") else "-"
    return "| " + " | ".join(cell(x) for x in [
        it["id"], it["name"], it["def"], it["out"], join(it.get("who")), join(it.get("when")),
        join(it.get("what")), join(it.get("site")), join(it.get("basis"), "; "), must, it["area"],
    ]) + " |"


def lens_counts(m: Model):
    st = m.st
    res = {}
    for key, fld in (("누가", "who"), ("언제", "when"), ("무엇", "what")):
        res[key] = {v: [i["id"] for i in m.items if v in (i.get(fld) or [])] for v in st["lenses"][key]}
    res["어디"] = {v: [i["id"] for i in m.items if v in (i.get("site") or [])] for v in st["lenses"]["어디"]}
    return res


def render_list(m: Model) -> str:
    st, items = m.st, m.items
    L = []
    L.append("# 01. 리스트업 — 로봇 오케스트레이션 플랫폼을 구현하고 운영하는 데 관여하는 모든 일\n")
    L.append(f"> 작성 {TODAY} · 루프 프롬프트 A단계 · 다음 문서: [02. 카테고리화](02_categories.md)  \n> {GEN}\n")
    L.append("## 0. 이 문서\n")
    L.append("이 위키의 개념은 **로봇 오케스트레이션 플랫폼(ROP)을 구현하고 운영하는 데 관여하는 모든 일을 처음부터 끝까지 빠짐없이 리스트업하고, "
             "그 리스트를 카테고리로 묶고, 카테고리마다 연구·기사·업체 발표를 모으는 기술 지형도**다. 이 문서는 그 첫 단계인 리스트업 결과다.\n")
    L.append("‘처음부터 끝까지’는 정해진 순서가 아니라 빠뜨리는 일 없이 전부라는 뜻이다. 그래서 항목을 렌즈 순서로 배열하지 않고, "
             "입력 출처 순서(필수 항목 → 기존 입력 → 새로 나열)로 적었다. 카테고리는 이 목록에서 [02](02_categories.md)가 만든다.\n")
    L.append("## 1. 방법\n")
    L.append("입력은 세 가지다.\n")
    L.append("1. **기존 입력**: 현재 분류 원문의 28개 세부영역과 9장(책임 경계)·11장(물류 흐름), 트랙 3개, 확장 아이디어 3개, "
             "로봇 시뮬레이터 코드(`robot-simulator/`, PR #12). 초안으로만 취급했고, 물류에 한정된 표현(주문·공정·거점·화물·재고)은 현장 전반으로 넓혀 적었다.")
    L.append("2. **필수 항목 두 개**: 온톨로지 기능(이기종 로봇 등록·능력 표현·시스템과 로봇의 연동)과 채팅 기능(맵 작성·시나리오 구성·로봇 구성·"
             "실제 상황 시뮬레이션 재현, 그리고 업무 지시). 하위 항목까지 나눠 적었다.")
    L.append("3. **백지에서 새로 나열한 항목**: 기존 입력이 직접 다루지 않는 일. 아래 네 렌즈로 빠짐을 찾았다.\n")
    L.append("빠짐을 찾는 렌즈 네 개는 체크리스트로만 쓴다(축이 아니다). 렌즈 값마다 항목이 몇 개인지는 4절에 있다.\n")
    L.append("| 렌즈 | 값 |\n|---|---|")
    L.append("| 누가 | " + join([f"{v}({st['role_labels'][v]})" if v in st['role_labels'] else v for v in st["lenses"]["누가"]]) + " |")
    for k in ("언제", "무엇", "어디"):
        L.append(f"| {k} | " + join(st["lenses"][k]) + " |")
    L.append("")
    L.append("항목 형식은 루프 프롬프트 4장의 여덟 칸(id·이름·한 줄 정의·산출물 또는 책임·관련 역할·현장 유형·근거·필수 여부)에, "
             "렌즈 점검용 두 칸(시기·종류)과 B단계에서 붙인 배치(영역 id) 칸을 더했다.\n")
    L.append("근거 표기: ‘원문 N’은 현재 분류 원문의 세부영역 N, ‘원문 N장’은 원문의 N장, ‘트랙 온톨로지·챗봇·도면’은 `config/tracks/`의 세 트랙, "
             "‘시뮬레이터 X’는 `robot-simulator/`의 해당 코드, ‘사용자 09-28’은 이번 대화의 사용자 요구, [가정]은 구축자 해석이다.\n")
    # 요약
    n = len(items)
    by_origin = Counter(i["origin"] for i in items)
    onto = [i for i in items if i.get("must") == "온톨로지"]
    chat = [i for i in items if i.get("must") == "채팅"]
    sub_o = Counter(i["sub"] for i in onto)
    sub_c = Counter(i["sub"] for i in chat)
    whole = sum(1 for i in items if i.get("site") == ["전체"])
    L.append("## 2. 요약\n")
    L.append("| 구분 | 항목 수 |\n|---|---|")
    L.append(f"| 전체 항목 | **{n}** |")
    L.append(f"| 필수 — 온톨로지 | {len(onto)} (" + join([f"{k} {sub_o.get(k, 0)}" for k in st['mandatory']['온톨로지']['required'] + st['mandatory']['온톨로지']['extra']]) + ") |")
    L.append(f"| 필수 — 채팅 | {len(chat)} (" + join([f"{k} {sub_c.get(k, 0)}" for k in st['mandatory']['채팅']['required'] + st['mandatory']['채팅']['extra']]) + ") |")
    L.append(f"| 기존 입력에서 나온 항목 | {by_origin.get('기존', 0)} |")
    L.append(f"| 백지에서 새로 나열한 항목 | {by_origin.get('신규', 0)} |")
    L.append(f"| 현장 유형 ‘전체’(모든 현장 공통) | {whole} ({pct(whole, n)}) |")
    L.append(f"| 특정 현장에만 해당 | {n - whole} ({pct(n - whole, n)}) |")
    L.append("")
    L.append("## 3. 항목 표\n")
    sections = [
        ("3.1 필수 — 온톨로지 (이기종 로봇 등록·능력 표현·시스템과 로봇의 연동)", lambda i: i.get("must") == "온톨로지"),
        ("3.2 필수 — 채팅 (맵 작성·시나리오 구성·로봇 구성·실제 상황 시뮬레이션 재현·업무 지시)", lambda i: i.get("must") == "채팅"),
        ("3.3 기존 입력에서 나온 항목", lambda i: not i.get("must") and i["origin"] == "기존"),
        ("3.4 백지에서 새로 나열한 항목", lambda i: not i.get("must") and i["origin"] == "신규"),
    ]
    for title, pred in sections:
        rows = [i for i in items if pred(i)]
        L.append(f"### {title}\n")
        L.append(f"{len(rows)}개.\n")
        L.append(ITEM_HEAD)
        for it in rows:
            L.append(item_row(m, it))
        L.append("")
    L.append("## 4. 렌즈 점검표\n")
    L.append("렌즈 값마다 그 값이 붙은 항목 수다. ‘어디’는 특정 현장 값이 붙은 항목만 센다(‘전체’ 항목은 모든 현장에 해당한다). 판정은 [04](04_verify.md) 검사 1에 있다.\n")
    L.append("| 렌즈 | 값 | 항목 수 | 예 |\n|---|---|---|---|")
    lc = lens_counts(m)
    for key in ("누가", "언제", "무엇", "어디"):
        for v, ids in lc[key].items():
            L.append(f"| {key} | {v} | {len(ids)} | {join(ids[:6])}{' …' if len(ids) > 6 else ''} |")
    L.append("")
    L.append("## 5. [가정]\n")
    L.append("이 단계의 [가정]은 멈춤 1 보고와 함께 [04 검증](04_verify.md) 9절에 한데 모았다.\n")
    return "\n".join(L)


# ---------------------------------------------------------------- 02
def render_categories(m: Model) -> str:
    st = m.st
    L = []
    L.append("# 02. 카테고리화 — 리스트에서 아래에서 위로\n")
    L.append(f"> 작성 {TODAY} · 루프 프롬프트 B단계 · 입력: [01. 리스트업](01_list.md) · 다음 문서: [03. 매핑](03_mapping.md)  \n> {GEN}\n")
    L.append("## 0. 만든 방법\n")
    L.append(f"1. 항목 {len(m.items)}개를 같은 일을 하는 것끼리 먼저 **영역**으로 묶었다(영역 {len(m.areas)}개). 영역 하나가 앞으로 위키 페이지 하나가 된다.")
    L.append(f"2. 영역을 핵심 질문이 같은 것끼리 **카테고리**로 묶었다(카테고리 {len(m.cats)}개). 기준은 두 가지다. 플랫폼이 이 일을 못 하면 무엇이 안 되는가가 같은가, 모을 출처가 비슷한가.")
    L.append("3. 필수 두 항목(온톨로지, 채팅)은 카테고리 이름과 영역 이름에 그대로 드러냈다(B, C).")
    L.append("4. 카테고리 개수는 미리 정하지 않았다. 카테고리마다 묶은 이유를 적었다.")
    L.append("5. 표시 순서는 읽는 흐름을 따른다. 기획 다음에 필수 두 카테고리를 두고, 이어서 플랫폼이 세상을 이해하는 방법(공간, 사물·사람), 연결(연동), 결정과 실행, 사람이 쓰는 방식(설계, 운영), 기반(인프라, AI), 지키는 것(안전, 보안), 현장에 넣고 유지하는 일, 규칙, 현장 유형별 적용 순이다. 순서는 표시용이며 축이 아니다.\n")
    L.append("## 1. 카테고리 한눈에\n")
    L.append("| 카테고리 | 한 줄 정의 | 영역 | 항목 | 필수 |\n|---|---|---|---|---|")
    for cid in m.cat_order:
        c = m.cats[cid]
        n_items = sum(len(m.items_by_area[a["id"]]) for a in m.areas_by_cat[cid])
        L.append(f"| **{cid}. {cell(c['full_name'])}** | {cell(c['def'])} | {len(m.areas_by_cat[cid])} | {n_items} | {'필수' if c['must'] else '-'} |")
    L.append(f"| 합계 | | {len(m.areas)} | {len(m.items)} | |")
    L.append("")
    L.append("## 2. 필수 두 항목의 위치\n")
    L.append("| 필수 항목 | 하위 항목 | 영역 | 항목 |\n|---|---|---|---|")
    for must, cid in (("온톨로지", "B"), ("채팅", "C")):
        for sub in st["mandatory"][must]["required"] + st["mandatory"][must]["extra"]:
            its = [i for i in m.items if i.get("must") == must and i.get("sub") == sub]
            areas = sorted({i["area"] for i in its})
            req = "(필수 하위)" if sub in st["mandatory"][must]["required"] else "(추가)"
            L.append(f"| {must} | {sub} {req} | {join([m.area_label(a) for a in areas])} | {join([i['id'] + ' ' + i['name'] for i in its])} |")
    L.append("")
    L.append("채팅 카테고리의 영역은 대화 인터페이스 쪽 일이다. 대화가 부르는 엔진은 다른 카테고리에 있고 서로 연결한다: 맵 작성 → D(공간·지도 모델), "
             "시나리오 구성·실제 상황 재현 → I(설계·시뮬레이션), 로봇 구성 → B(로봇 온톨로지), 업무 지시 → G(계획·최적화)·H(실행·협업·예외 복구).\n")
    L.append("## 3. 카테고리별 상세\n")
    for cid in m.cat_order:
        c = m.cats[cid]
        L.append(f"### {cid}. {c['full_name']}" + (" [필수]" if c["must"] else "") + "\n")
        L.append(f"- **한 줄 정의**: {c['def']}")
        L.append(f"- **포함 기준**: {c['include']}")
        L.append(f"- **핵심 질문**: {c['question']}")
        L.append(f"- **이 일을 못 하면**: {c['if_missing']}")
        L.append(f"- **묶은 이유**: {c['why']}\n")
        L.append("모을 출처 유형 예시(수집 대상 후보이며, 수집 때 원문을 열어 확인한다):\n")
        L.append("| 출처 유형 | 예 |\n|---|---|")
        for s in c["sources"]:
            L.append(f"| {cell(s['type'])} | {cell(s['ex'])} |")
        L.append("")
        L.append("| 영역 | 정의 | 항목 |\n|---|---|---|")
        for a in m.areas_by_cat[cid]:
            its = m.items_by_area[a["id"]]
            L.append(f"| **{a['id']} {cell(a['name'])}** | {cell(a['def'])} | " + cell(join([i['id'] + ' ' + i['name'] for i in its])) + " |")
        L.append("")
    return "\n".join(L)


# ---------------------------------------------------------------- 03
def render_mapping(m: Model, dc: dict) -> str:
    mp = m.mp
    L = []
    oas = mp["old_areas"]
    act = Counter(m.area_action(oa) for oa in oas)
    origin = Counter(m.area_origin(a)[0] for a in m.area_order)
    oc_act = Counter(c["action"] for c in mp["old_categories"])
    succ_set = {c["successor"] for c in mp["old_categories"]}
    u1_base = sum(1 for v in m.old_cat_path.values() if v) + len(m.old_area_path)
    L.append("# 03. 매핑 — 옛 구조에서 새 구조로\n")
    L.append(f"> 작성 {TODAY} · 루프 프롬프트 B단계 · 입력: [02. 카테고리화](02_categories.md) · 다음 문서: [04. 검증](04_verify.md)  \n> {GEN}\n")
    L.append("이 문서는 옛 이름을 그대로 인용한다(무엇이 어디로 가는지 보여 주는 문서이기 때문이다). 새 구조의 이름·정의는 [02](02_categories.md)가 기준이다.\n")
    L.append("## 0. 요약\n")
    L.append("| 대상 | 결과 |\n|---|---|")
    L.append(f"| 대분류 {len(mp['old_categories'])}개 → 카테고리 {len(m.cats)}개 | " + join([f"{k} {v}" for k, v in oc_act.items()]) +
             f". 새 카테고리 가운데 옛 대분류를 잇는 것 {len(succ_set)}, 신규 {len(m.cats) - len(succ_set)} |")
    L.append(f"| 세부영역 {len(oas)}개 → 영역 {len(m.areas)}개 | " + join([f"{k} {act.get(k, 0)}" for k in ('유지', '이동', '이름 변경', '분할')]) +
             f", 병합 0. 갈 곳 없는 옛 영역 0 |")
    L.append(f"| 새 영역 {len(m.areas)}개의 출처 | 옛 영역을 주로 잇는 것 {origin.get('계승', 0)}, 옛 영역 일부에서 시작 {origin.get('일부에서 시작', 0)}, 신규 {origin.get('신규', 0)} |")
    L.append("| 트랙 3개 | 유지 1(온톨로지), 확장·이름 변경 1(챗봇 → 채팅 기반 구성·운영), 두 안 1(도면 인식) |")
    L.append("| 확장 아이디어 | 유지 3(연결 구조 페이지 포함), 이름 변경·정의 확장 1(아이디어 2) |")
    L.append(f"| 주소가 바뀌는 기존 페이지 | 안 1: 최소 {u1_base}, 선택에 따라 최대 {u1_base + dc['chat_pages'] + 1 + dc['fp_pages']}. 안 2: 0 (6절) |")
    L.append("")
    L.append("처리 종류는 스크립트가 계산한다: 일부가 다른 영역으로 가면 **분할**, 이름이 바뀌면 **이름 변경**, 이름이 같고 이어받는 카테고리로 가면 **유지**, "
             "이름이 같고 다른 카테고리로 가면 **이동**. 옛 영역 둘 이상이 한 영역으로 합쳐지는 **병합**은 이번 안에 없다.\n")
    L.append("## 1. 대분류 7개\n")
    L.append("| 옛 대분류 | 옛 경로 | 처리 | 잇는 새 카테고리 | 영역이 가는 곳 |\n|---|---|---|---|---|")
    for c in mp["old_categories"]:
        s = m.cats[c["successor"]]
        L.append(f"| {c['id']}. {cell(c['name'])} | `{m.old_cat_path.get(c['id']) or '(없음)'}` | {c['action']} | {s['id']}. {cell(s['full_name'])} | {cell(c['note'])} |")
    L.append("")
    L.append("## 2. 세부영역 28개\n")
    L.append("| 옛 영역 | 옛 경로 | 처리 | 주 영역(새) | 일부가 가는 곳 | 안 1 새 경로 | 비고 |\n|---|---|---|---|---|---|---|")
    for oa in oas:
        L.append("| " + " | ".join([
            f"{oa['num']}. {cell(oa['name'])}", f"`{m.old_area_path.get(oa['num'], '(없음)')}`", m.area_action(oa),
            cell(m.area_label(oa["main"])), cell(join([m.area_label(p) for p in oa.get("parts") or []])),
            f"`{m.new_area_path(oa['main'])}`", cell(oa.get("note", "-")),
        ]) + " |")
    L.append("")
    L.append(f"## 3. 새 영역 {len(m.areas)}개의 출처\n")
    L.append("| 새 영역 | 카테고리 | 구분 | 옛 영역(주) | 옛 영역(일부) | 기존 페이지에서 가져올 것 | 항목 수 |\n|---|---|---|---|---|---|---|")
    seeds = mp.get("seeds") or {}
    for aid in m.area_order:
        kind, mains, parts = m.area_origin(aid)
        a = m.areas[aid]
        L.append(f"| {aid} {cell(a['name'])} | {a['cat']} | {kind} | {join(mains)} | {join(parts)} | {cell(join(seeds.get(aid, []), '; '))} | {len(m.items_by_area[aid])} |")
    L.append("")
    L.append("## 4. 트랙 개편안 (멈춤 1에서 결정)\n")
    for t in mp["tracks"]:
        L.append(f"### {t['name']} (`{t['slug']}`) — {t['action']}\n")
        L.append(f"- 중심 영역: 옛 {t['old_primary']} → 새 {m.area_label(t['new_primary'])}")
        if t.get("proposal"):
            L.append(f"- 제안: {t['proposal']}")
        if t.get("new_name"):
            L.append(f"- 새 이름: {t['new_name']} (주소 정책 안 1이면 슬러그 `{t['new_slug']}`, 안 2이면 `{t['slug']}` 유지)")
        if t["slug"] == "nl-task-chatbot":
            L.append(f"- 현재 페이지 {dc['chat_pages']}개, 단계 1~5 페이지의 고유 출처 {dc['chat_stage_refs']}개.\n")
            for key in ("layout_a", "layout_b"):
                lay = t[key]
                L.append(f"단계 배치 — {lay['label']}:\n")
                for s in lay["stages"]:
                    L.append(f"- {s}")
                L.append(f"\n{lay['note']}\n")
        if t["slug"] == "floorplan-recognition":
            L.append(f"- 현재 페이지 {dc['fp_pages']}개, 단계 1~5 페이지의 고유 출처 {dc['fp_stage_refs']}개.\n")
            L.append(f"1. {t['option_ga']}")
            L.append(f"2. {t['option_na']}\n")
        else:
            L.append("")
    L.append("## 5. 확장 아이디어와 기타 페이지\n")
    L.append("| 페이지 | 처리 | 내용 |\n|---|---|---|")
    for i in mp["ideas"]:
        extra = f" → {i['new_name']}" if i.get("new_name") else ""
        L.append(f"| `{i['page']}` ({cell(i['name'])}) | {i['action']}{cell(extra)} | {cell(i['note'])} |")
    for o in mp["other_pages"]:
        L.append(f"| `{o['page']}` | {o['action']} | {cell(o['note'])} |")
    L.append("")
    L.append("## 6. 주소(URL) 영향\n")
    up = mp["url_policy"]
    L.append(f"- {up['option_1']}")
    L.append(f"- {up['option_2']}\n")
    L.append("| 바뀌는 기존 페이지 | 안 1 | 안 2 |\n|---|---|---|")
    ncat = sum(1 for v in m.old_cat_path.values() if v)
    L.append(f"| 대분류 페이지 | {ncat} | 0 |")
    L.append(f"| 세부영역 페이지 | {len(m.old_area_path)} | 0 |")
    L.append(f"| 챗봇 트랙 페이지(슬러그를 새 이름으로 바꿀 때) | {dc['chat_pages']} | 0 |")
    L.append(f"| 흐름 매트릭스 페이지(이름을 바꿀 때) | {1 if dc['flow_matrix'] else 0} | 0 |")
    L.append(f"| 도면 트랙 페이지((가) 합치기를 고를 때) | {dc['fp_pages']} | 0 |")
    L.append(f"| **합계** | 최소 {ncat + len(m.old_area_path)}, 최대 {ncat + len(m.old_area_path) + dc['chat_pages'] + 1 + dc['fp_pages']} | 0 |")
    L.append("")
    L.append(f"새로 생기는 페이지: 영역 {len(m.areas) - len(m.old_area_path)}개(옛 영역을 잇지 않는 영역), 카테고리 페이지 {len(m.cats) - len(succ_set)}개.\n")
    L.append(f"링크 갱신 범위: 옛 대분류 슬러그를 본문에 담은 파일 {dc['link_files']}개. 안 1이면 스크립트로 새 경로로 바꾸고, 안 2이면 이름이 바뀐 영역의 링크 글자만 바꾼다. "
             f"영역 번호 필드(area_no·primary_area_no·related_areas)가 있는 페이지 {dc['pages_with_area_fields']}개(그중 주제 페이지 {dc['topics_with_primary']}개)는 "
             "두 안 모두 새 영역 ID로 바꾼다. 주제·용어·참고문헌 페이지 자체의 주소는 바뀌지 않는다.\n")
    L.append("### 안 1 리다이렉트 목록 (옛 경로 → 새 경로)\n")
    L.append("| 옛 경로 | 새 경로 |\n|---|---|")
    for c in mp["old_categories"]:
        if m.old_cat_path.get(c["id"]):
            L.append(f"| `{m.old_cat_path[c['id']]}` | `{m.new_cat_path(c['successor'])}` |")
    for oa in oas:
        L.append(f"| `{m.old_area_path.get(oa['num'], '(없음)')}` | `{m.new_area_path(oa['main'])}` |")
    L.append("")
    L.append("## 7. 수정 단계(D)에서 이 매핑을 쓰는 방법\n")
    L.append("페이지 이동·이름 변경·번호 재부여는 손으로 하지 않는다. D2 스크립트가 `data/mapping.yaml`의 `old_areas`(main·parts)와 "
             "`data/structure.yaml`의 `slug`를 읽어 새 페이지 뼈대, 본문·각주 이동, 링크 갱신, 리다이렉트 설정을 한 번에 만든다. "
             "분할은 원 페이지의 절을 항목이 속한 영역으로 나누고, 원 페이지 자리에는 요약과 링크를 남긴다.\n")
    return "\n".join(L)


# ---------------------------------------------------------------- 04
def run_checks(m: Model, texts: dict, dc: dict) -> list[dict]:
    st, items, mp = m.st, m.items, m.mp
    res = []
    # 1 렌즈 빠짐
    lc = lens_counts(m)
    empty = [f"{k}:{v}" for k in lc for v, ids in lc[k].items() if not ids]
    res.append(dict(no=1, name="렌즈 빠짐", crit="네 렌즈의 모든 값에 항목이 최소 1개(‘어디’는 그 현장 값이 붙은 항목)",
                    ok=not empty, value=("빈 값 없음" if not empty else "빈 값: " + join(empty)),
                    detail=lc))
    # 2 필수 항목
    rows = []
    ok2 = True
    for must, cid in (("온톨로지", "B"), ("채팅", "C")):
        c = m.cats[cid]
        names = [c["full_name"]] + [a["name"] for a in m.areas_by_cat[cid]]
        for sub in st["mandatory"][must]["required"]:
            n = sum(1 for i in items if i.get("must") == must and i.get("sub") == sub)
            shown = [x for x in names if sub in x]
            good = n >= 1 and bool(shown)
            ok2 &= good
            rows.append((must, sub, n, shown, good))
    res.append(dict(no=2, name="필수 항목", crit="채팅: 맵 작성·시나리오 구성·로봇 구성·시뮬레이션 재현 4가지, 온톨로지: 등록·능력 표현·연동 3가지가 모두 항목으로 있고 카테고리·영역 이름에 드러난다",
                    ok=ok2, value=f"채팅 {sum(1 for r in rows if r[0] == '채팅' and r[4])}/4, 온톨로지 {sum(1 for r in rows if r[0] == '온톨로지' and r[4])}/3", detail=rows))
    # 3 SCM 제거
    counts = {f: {w: texts[f].count(w) for w in BANNED} for f in ("01_list.md", "02_categories.md")}
    extra = {f: texts[f].count("공급망") for f in ("01_list.md", "02_categories.md")}
    total = sum(sum(v.values()) for v in counts.values())
    res.append(dict(no=3, name="SCM 제거", crit="새 리스트(01)·카테고리 정의와 핵심 질문(02)에 ‘SCM’, ‘SCOR’, ‘공급망 관점’ 0회",
                    ok=total == 0, value=f"{total}회", detail=(counts, extra)))
    # 4 현장 편중
    n = len(items)
    whole = sum(1 for i in items if i.get("site") == ["전체"])
    spec = Counter(v for i in items if i.get("site") != ["전체"] for v in i["site"])
    logi_only = sum(1 for i in items if i.get("site") == ["물류창고"])
    wording = {k: [i["id"] for i in items if any(w in (i["name"] + " " + i["def"]) for w in ws)] for k, ws in SITE_TERMS.items()}
    res.append(dict(no=4, name="현장 편중", crit="특정 현장에만 해당하는 항목 비율을 표시하고, 모든 현장 공통 항목이 다수(절반 초과)",
                    ok=whole * 2 > n, value=f"공통 {whole}/{n} ({pct(whole, n)}), 물류창고 전용 {logi_only} ({pct(logi_only, n)})",
                    detail=(whole, spec, logi_only, n, wording)))
    # 5 내용 유실
    mapped = {oa['num'] for oa in mp["old_areas"]}
    on_disk = set(m.old_area_path)
    miss_area = sorted(on_disk - mapped)
    no_dest = [oa['num'] for oa in mp["old_areas"] if oa["main"] not in m.areas]
    miss_cat = [c["id"] for c in mp["old_categories"] if c["successor"] not in m.cats]
    track_ok = len(mp["tracks"]) == dc["track_configs"]
    idea_ok = len(mp["ideas"]) == dc["idea_pages"]
    lost = len(miss_area) + len(no_dest) + len(miss_cat) + (0 if track_ok else 1) + (0 if idea_ok else 1)
    res.append(dict(no=5, name="내용 유실", crit="기존 28영역 전부 매핑표에 행이 있고 갈 곳이 있다(갈 곳 없는 항목 0). 대분류·트랙·아이디어도 모두 행이 있다",
                    ok=lost == 0 and len(on_disk) == 28,
                    value=f"옛 영역 {len(mapped & on_disk)}/{len(on_disk)} 매핑, 갈 곳 없음 {len(miss_area) + len(no_dest)}",
                    detail=dict(on_disk=len(on_disk), mapped=len(mapped), miss_area=miss_area, no_dest=no_dest, miss_cat=miss_cat,
                                tracks=(len(mp['tracks']), dc['track_configs']), ideas=(len(mp['ideas']), dc['idea_pages']),
                                cats=(len(mp['old_categories']), sum(1 for v in m.old_cat_path.values() if v)))))
    # 6 수집 가능성
    core = set(st["source_types_core"])
    per = []
    for cid in m.cat_order:
        types = [s["type"] for s in m.cats[cid]["sources"]]
        per.append((cid, len(set(types) & core), len(set(types)), types))
    bad = [p for p in per if p[1] < 2]
    res.append(dict(no=6, name="수집 가능성", crit="카테고리마다 출처 유형 예시 2종 이상(연구·기사·업체 발표 가운데 2종 이상)",
                    ok=not bad, value=f"{len(per) - len(bad)}/{len(per)} 카테고리 통과", detail=per))
    return res


def render_verify(m: Model, checks: list[dict], cons: list[str], dc: dict) -> str:
    L = []
    L.append("# 04. 검증 — 멈춤 1 전에 통과해야 하는 6항목\n")
    L.append(f"> 작성 {TODAY} · 루프 프롬프트 C단계 · 입력: [01](01_list.md) [02](02_categories.md) [03](03_mapping.md)  \n> {GEN}\n")
    all_ok = all(c["ok"] for c in checks) and not cons
    L.append("## 0. 결과\n")
    L.append(f"**{'전부 통과' if all_ok else '실패 있음'}** — 검사 6개 중 {sum(1 for c in checks if c['ok'])}개 통과, 데이터 일관성 오류 {len(cons)}건.\n")
    L.append("| # | 검사 | 통과 기준 | 결과 | 측정값 |\n|---|---|---|---|---|")
    for c in checks:
        L.append(f"| {c['no']} | {c['name']} | {cell(c['crit'])} | {'통과' if c['ok'] else '실패'} | {cell(c['value'])} |")
    L.append("")
    # 상세
    c1, c2, c3, c4, c5, c6 = checks
    L.append("## 1. 렌즈 빠짐\n")
    L.append("| 렌즈 | 값 | 항목 수 |\n|---|---|---|")
    for key, vals in c1["detail"].items():
        for v, ids in vals.items():
            L.append(f"| {key} | {v} | {len(ids)} |")
    L.append("\n의도적으로 비운 칸: 없음. ‘무엇’ 렌즈가 비어 있는 항목(동향 조사·조달·교육·현장 적용 등)은 기술 종류가 아닌 일이라 비워 두었다(9절 [가정]).\n")
    L.append("## 2. 필수 항목\n")
    L.append("| 필수 항목 | 하위 항목 | 항목 수 | 이름에 드러난 곳 | 결과 |\n|---|---|---|---|---|")
    for must, sub, n, shown, good in c2["detail"]:
        L.append(f"| {must} | {sub} | {n} | {cell(join(shown, ' / '))} | {'통과' if good else '실패'} |")
    extra_chat = sum(1 for i in m.items if i.get("must") == "채팅" and i.get("sub") == "업무 지시")
    L.append(f"\n채팅은 네 가지에 더해 ‘업무 지시·오케스트레이션’({extra_chat}개 항목, C5)도 필수로 넣었다. 사용자가 앞선 설명에서 ‘로봇을 오케스트레이션 하는 기능’을 함께 들었기 때문이다.\n")
    L.append("## 3. SCM 제거\n")
    counts, extra = c3["detail"]
    L.append("| 문서 | " + " | ".join(f"‘{w}’" for w in BANNED) + " | 참고: ‘공급망’ |\n|---|" + "---|" * len(BANNED) + "---|")
    for f, v in counts.items():
        L.append(f"| {f} | " + " | ".join(str(v[w]) for w in BANNED) + f" | {extra[f]} |")
    L.append("\n03은 옛 이름을 인용하는 매핑 문서이고 04는 검사 기준 자체를 적으므로 검사 대상이 아니다. 위키 전체에서 이 말을 없애는 일은 수정 단계(D)와 검증 루프(E)의 몫이다.\n")
    L.append("## 4. 현장 편중\n")
    whole, spec, logi_only, n, wording = c4["detail"]
    L.append("| 현장 유형 | 항목 수 | 비율 |\n|---|---|---|")
    L.append(f"| 전체(모든 현장 공통) | {whole} | {pct(whole, n)} |")
    for v in m.st["lenses"]["어디"]:
        L.append(f"| {v}에만 해당 | {spec.get(v, 0)} | {pct(spec.get(v, 0), n)} |")
    L.append(f"\n물류창고에만 해당하는 항목은 {logi_only}개({pct(logi_only, n)})다. 기존 물류 흐름 7단계 내용은 이 항목(Q1 물류창고)의 사례로 남긴다. "
             "목록 단계의 편중은 없앴지만, 옛 페이지 본문의 물류 편중(현장 시나리오 절)은 수정 단계에서 ‘적용 사례(현장 유형 명시)’로 바꿔야 풀린다.\n")
    L.append("보조 지표 — 항목 이름·정의 문구에 현장 용어가 나오는 항목 수(현장 유형 칸이 ‘전체’여도 예시가 한 현장에 몰릴 수 있어 따로 센다. 판정에는 쓰지 않는다):\n")
    L.append("| 현장 | 용어 | 항목 수 | 항목 |\n|---|---|---|---|")
    for k, ids in wording.items():
        L.append(f"| {k} | {cell(join(SITE_TERMS[k], '·'))} | {len(ids)} | {cell(join(ids))} |")
    L.append("")
    L.append("## 5. 내용 유실\n")
    d = c5["detail"]
    L.append("| 대상 | 디스크 | 매핑 행 | 갈 곳 없음 |\n|---|---|---|---|")
    L.append(f"| 옛 세부영역 페이지 | {d['on_disk']} | {d['mapped']} | {len(d['miss_area']) + len(d['no_dest'])} |")
    L.append(f"| 옛 대분류 페이지 | {d['cats'][1]} | {d['cats'][0]} | {len(d['miss_cat'])} |")
    L.append(f"| 트랙 설정 | {d['tracks'][1]} | {d['tracks'][0]} | 0 |")
    L.append(f"| 확장 아이디어 페이지 | {d['ideas'][1]} | {d['ideas'][0]} | 0 |")
    L.append("\n옛 영역 28개 모두 주 영역이 있고, 분할된 9개는 나머지 부분이 가는 영역까지 적었다([03](03_mapping.md) 2절).\n")
    L.append("## 6. 수집 가능성\n")
    L.append("| 카테고리 | 연구·기사·업체 발표 중 | 출처 유형 수 | 유형 |\n|---|---|---|---|")
    for cid, ncore, ntype, types in c6["detail"]:
        L.append(f"| {cid}. {cell(m.cats[cid]['name'])} | {ncore} | {ntype} | {cell(join(types))} |")
    L.append("")
    L.append("## 7. 데이터 일관성 (추가 검사)\n")
    if cons:
        L.append("\n".join(f"- {e}" for e in cons) + "\n")
    else:
        L.append("오류 0건. 항목 id·영역·카테고리·슬러그 중복 없음, 모든 항목에 영역 1개, 모든 영역에 항목 1개 이상, 필수 항목은 B·C 안에만 있음, "
                 "렌즈 값이 모두 정의된 값, 매핑의 새 영역이 모두 존재.\n")
    L.append("## 8. 반복 기록\n")
    L.append("루프 프롬프트 6장: 실패하면 A 또는 B로 돌아가 최대 3회 반복한다.\n")
    if m.log:
        L.append("| 회차 | 결과 | 실패·발견 | 고친 것 |\n|---|---|---|---|")
        for e in m.log:
            L.append(f"| {e['run']} | {cell(e['result'])} | {cell(e.get('found', '-'))} | {cell(e.get('fixed', '-'))} |")
    else:
        L.append("기록 없음(첫 실행).")
    L.append("")
    L.append("## 9. [가정] 목록 (멈춤 1 보고용)\n")
    for i, a in enumerate(m.mp["assumptions"], 1):
        L.append(f"{i}. {a}")
    L.append("")
    return "\n".join(L)


# ---------------------------------------------------------------- main
def main() -> int:
    st, items, mp, log = load()
    m = Model(st, items, mp, log)
    cons = consistency(m)
    dc = disk_counts(m)
    texts = {
        "01_list.md": render_list(m),
        "02_categories.md": render_categories(m),
        "03_mapping.md": render_mapping(m, dc),
    }
    checks = run_checks(m, texts, dc)
    texts["04_verify.md"] = render_verify(m, checks, cons, dc)
    for name, t in texts.items():
        (HERE / name).write_text(t.rstrip() + "\n", encoding="utf-8")
    ok = all(c["ok"] for c in checks) and not cons
    print(f"항목 {len(items)} · 영역 {len(m.areas)} · 카테고리 {len(m.cats)} · 일관성 오류 {len(cons)}")
    for c in checks:
        print(f"  검사 {c['no']} {c['name']}: {'통과' if c['ok'] else '실패'} — {c['value']}")
    for e in cons[:20]:
        print("  일관성:", e)
    act = Counter(m.area_action(oa) for oa in mp["old_areas"])
    origin = Counter(m.area_origin(a)[0] for a in m.area_order)
    print("  옛 영역 처리:", dict(act), "· 새 영역 출처:", dict(origin))
    print("  디스크:", dc)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
