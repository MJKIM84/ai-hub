#!/usr/bin/env python3
"""D2: 옛 구조(7대분류·28영역) → 새 구조(17대분류·67영역) 페이지 이관. 한 번만 실행한다.

하는 일
1. 매핑표(data/mapping.yaml)대로 옛 영역 28개·대분류 7개 페이지를 새 경로로 옮긴다(git mv).
   챗봇 트랙(nl-task-chatbot → chat-based-configuration-and-operation), 아이디어 2 페이지, 흐름 매트릭스(→ site-matrix.md)도 옮긴다.
2. docs 전체의 상대 링크를 옛 위치 기준으로 풀어 새 경로로 다시 쓰고, 바뀐 절 제목의 앵커를 고친다.
3. 영역 번호 필드(area_no, primary_area_no, related_areas)와 대분류 필드를 새 번호·이름으로 바꾼다.
4. 옛 영역 제목 문자열("7. 화물·재고·자산 식별과 추적")을 새 주 영역 제목으로 바꾼다(원문 태그 줄 제외).
5. 새 원문에 없고 옛 원문에 있는 [분류원문] 줄은 [옛 분류원문]으로 바꾼다(문장은 그대로).
6. 옮긴 영역·대분류 페이지의 머리·1·2절을 새 원문으로 다시 쓰고, 옛 정의·질문·주석은 [옛 분류원문]으로 남긴다.
7. data/*.json, data/tracks, config/tracks 의 경로·번호를 바꾸고, 리다이렉트 표(data/redirects.json)를 쓴다.
"""
from __future__ import annotations

import json
import posixpath
import re
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
WIKI = HERE.parents[1]
sys.path.insert(0, str(WIKI / "pipeline"))
from lib import frontmatter as fm  # noqa: E402
from lib import paths  # noqa: E402
from lib.source import load_source, parse, split_cells  # noqa: E402
from lib.verbatim import TAG, TAG_OLD, tag_line  # noqa: E402

DOCS = paths.DOCS
SRC = load_source()
OLD = parse(paths.OLD_SOURCE_FILE.read_text(encoding="utf-8"), paths.OLD_SOURCE_FILE)
TODAY = "2026-09-28"
DATA_W = HERE / "data"
st = yaml.safe_load((DATA_W / "structure.yaml").read_text(encoding="utf-8"))
mp = yaml.safe_load((DATA_W / "mapping.yaml").read_text(encoding="utf-8"))
items = []
for p in sorted(DATA_W.glob("items_*.yaml")):
    items += yaml.safe_load(p.read_text(encoding="utf-8"))
NUM = json.loads((DATA_W / "numbering.json").read_text(encoding="utf-8"))["area_no"]
AREA_ID = {v: k for k, v in NUM.items()}
OLD_MAIN = {oa["num"]: NUM[oa["main"]] for oa in mp["old_areas"]}
OLD_PARTS = {oa["num"]: [NUM[p] for p in (oa.get("parts") or [])] for oa in mp["old_areas"]}
SUCC = {oc["id"]: oc["successor"] for oc in mp["old_categories"]}
OLD_CAT_SLUG = {oc["id"]: oc["slug"] for oc in mp["old_categories"]}
CHAT_OLD, CHAT_NEW = "nl-task-chatbot", "chat-based-configuration-and-operation"

ANCHORS = {
    "2-scm-관점의-질문": "2-핵심-질문",
    "5-현장-시나리오-물류-흐름의-어느-단계인지-명시": "5-적용-사례-현장-유형-명시",
    "9-rop가-직접-맡는-것과-외부와-연계하는-것-부록-a-9장-기준": "9-rop가-직접-맡는-것과-외부와-연계하는-것-책임-경계-기준",
}
HEADS = {
    "## 2. SCM 관점의 질문": "## 2. 핵심 질문",
    "## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)": "## 5. 적용 사례 (현장 유형 명시)",
    "## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)": "## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
}

# ---------------------------------------------------------------- 경로 표
OLD_AREA_REL = {int(p.name[:2]): p.relative_to(DOCS).as_posix()
                for p in sorted((DOCS / "categories").glob("*/[0-9][0-9]-*.md"))}
PATHMAP: dict[str, str] = {}
for no, rel in OLD_AREA_REL.items():
    PATHMAP[rel] = paths.area_rel_path(OLD_MAIN[no])
for letter, slug in OLD_CAT_SLUG.items():
    PATHMAP[f"categories/{slug}/index.md"] = paths.category_index_rel(SUCC[letter])
for p in sorted((DOCS / "tracks" / CHAT_OLD).glob("*.md")):
    PATHMAP[f"tracks/{CHAT_OLD}/{p.name}"] = f"tracks/{CHAT_NEW}/{p.name}"
PATHMAP["ideas/nl-task-chatbot.md"] = f"ideas/{CHAT_NEW}.md"
PATHMAP["flow-matrix.md"] = "site-matrix.md"
INV = {v: k for k, v in PATHMAP.items()}


def git(*a):
    subprocess.run(["git", *a], cwd=WIKI, check=True)


def move_files():
    for old, new in PATHMAP.items():
        src, dst = DOCS / old, DOCS / new
        if not src.exists():
            raise SystemExit(f"없음: {old}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        git("mv", str(src), str(dst))
    for d in list((DOCS / "categories").iterdir()) + [DOCS / "tracks" / CHAT_OLD]:
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()
    for base in ("data/tracks", "config/tracks"):
        pass
    git("mv", f"data/tracks/{CHAT_OLD}", f"data/tracks/{CHAT_NEW}")
    git("mv", f"config/tracks/{CHAT_OLD}.yaml", f"config/tracks/{CHAT_NEW}.yaml")


# ---------------------------------------------------------------- 텍스트 변환
LINK = re.compile(r"(\]\()(<?)([^)\s>]+)(>?)((?:\s+\"[^\"]*\")?\))")


def rewrite_links(text: str, new_rel: str) -> str:
    old_rel = INV.get(new_rel, new_rel)
    old_dir = posixpath.dirname(old_rel)
    new_dir = posixpath.dirname(new_rel)

    def rep(m):
        target = m.group(3)
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#") or target.startswith("/"):
            if target.startswith("#") and new_rel in INV:
                frag = target[1:]
                return m.group(1) + m.group(2) + "#" + ANCHORS.get(frag, frag) + m.group(4) + m.group(5)
            return m.group(0)
        path, _, frag = target.partition("#")
        if not path.endswith(".md") and not path.endswith("/"):
            return m.group(0)
        resolved = posixpath.normpath(posixpath.join(old_dir, path))
        tgt_new = PATHMAP.get(resolved, resolved)
        rel = posixpath.relpath(tgt_new, new_dir or ".")
        if frag:
            frag = ANCHORS.get(frag, frag)
            rel += "#" + frag
        return m.group(1) + m.group(2) + rel + m.group(4) + m.group(5)

    return LINK.sub(rep, text)


def rewrite_path_strings(text: str) -> str:
    for old, new in sorted(PATHMAP.items(), key=lambda kv: -len(kv[0])):
        text = text.replace(old, new)
    for a, b in ANCHORS.items():
        text = text.replace("#" + a, "#" + b)
    return text


OLD_TITLES = {OLD.area(n).title: SRC.area(OLD_MAIN[n]).title for n in range(1, 29)}
TITLE_RE = re.compile("(?<![0-9])(" + "|".join(re.escape(t) for t in sorted(OLD_TITLES, key=len, reverse=True)) + ")")


def replace_titles(text: str) -> str:
    out = []
    for line in text.split("\n"):
        if TAG in line or TAG_OLD in line:
            out.append(line)
        else:
            out.append(TITLE_RE.sub(lambda m: OLD_TITLES[m.group(1)], line))
    return "\n".join(out)


def lines_and_cells(src) -> set[str]:
    s = set()
    for line in src.raw.split("\n"):
        s.add(line)
        if line.lstrip().startswith("|"):
            s.update(split_cells(line))
    s.add(src.scope_disclaimer_sentence)
    s.discard("")
    return s


NEW_SET, OLD_SET = lines_and_cells(SRC), lines_and_cells(OLD)
_FOOT = re.compile(r"(\[\^[^\]\s]+\])+$")


def retag(text: str) -> str:
    out = text.split("\n")
    for i, line in enumerate(out):
        s = line.strip()
        while s.startswith(">"):
            s = s[1:].lstrip()
        s2 = _FOOT.sub("", s).rstrip()
        if s2 == TAG:
            # 표 아래 단독 태그: 바로 위 표의 셀이 새 원문에 없으면 옛 태그
            j = i - 1
            while j >= 0 and not out[j].strip():
                j -= 1
            cells = []
            while j >= 0 and out[j].lstrip().startswith("|"):
                cells += split_cells(out[j]); j -= 1
            cells = [c for c in cells if c and not re.fullmatch(r":?-+:?", c)]
            if cells and any(c not in NEW_SET for c in cells) and all(c in OLD_SET or "[" in c for c in cells[:3]):
                out[i] = line.replace(TAG, TAG_OLD)
            continue
        if not s2.endswith(" " + TAG):
            continue
        body = s2[: -len(TAG) - 1]
        for label in ("원문 주석: ",):
            if body.startswith(label):
                body = body[len(label):]
        if body in NEW_SET:
            continue
        if body in OLD_SET:
            k = line.rfind(" " + TAG)
            out[i] = line[:k] + " " + TAG_OLD + line[k + 1 + len(TAG):]
    return "\n".join(out)


def remap_nos(v):
    if v is None:
        return v
    if isinstance(v, list):
        out = []
        for x in v:
            if str(x).isdigit() and int(x) in OLD_MAIN:
                n = OLD_MAIN[int(x)]
                if n not in out:
                    out.append(n)
        return sorted(out)
    if str(v).isdigit() and int(v) in OLD_MAIN:
        return OLD_MAIN[int(v)]
    return v


OLD_CAT_TITLES = {c.title: c.letter for c in OLD.categories}


def update_meta(meta: dict, new_rel: str) -> dict:
    if meta.get("related_areas") is not None:
        meta["related_areas"] = remap_nos(meta["related_areas"])
    if meta.get("primary_area_no") not in (None, ""):
        meta["primary_area_no"] = remap_nos(meta["primary_area_no"])
        if meta.get("type") == "topic":
            meta["category"] = SRC.category_of(int(meta["primary_area_no"])).title
    if meta.get("type") == "area" and meta.get("area_no"):
        n = OLD_MAIN[int(meta["area_no"])]
        meta["area_no"] = n
        meta["title"] = SRC.area(n).title
        meta["category"] = SRC.category_of(n).title
    for k in ("split_from", "idea_page", "stage_page"):
        if isinstance(meta.get(k), str):
            meta[k] = rewrite_path_strings(meta[k])
    if meta.get("track") == CHAT_OLD:
        meta["track"] = CHAT_NEW
    return meta


# ---------------------------------------------------------------- 영역·대분류 페이지 머리 재작성
def L(from_rel, to_rel, text):
    return f"[{text}]({paths.rel_link(from_rel, to_rel)})"


def citation(from_rel, text):
    refs = [SRC.reference(n) for n in SRC.citations(text)]
    parts = [f"원문의 [{r.n}]{'은' if r.n in (1, 3, 6, 7, 8, 10) else '는'} 참고문헌 {L(from_rel, f'references/{r.id}.md', r.id)}에 해당한다.[^{r.id}]" for r in refs]
    return " ".join(parts), refs


def area_items_block(no):
    aid = AREA_ID[no]
    its = [i for i in items if i["area"] == aid]
    lines = ["이 영역이 다루는 일(2026-09-28 리스트업 기준):", ""]
    lines += [f"- **{i['name']}**: {i['def']}" for i in its]
    return "\n".join(lines)


def split_sections(body):
    secs, cur, order = {"": []}, "", [""]
    for line in body.split("\n"):
        if line.startswith("## "):
            cur = line
            secs[cur] = []
            order.append(cur)
        else:
            secs[cur].append(line)
    return order, secs


def rebuild_area_body(new_rel, old_no, body):
    no = OLD_MAIN[old_no]
    a, cat = SRC.area(no), SRC.category_of(no)
    oa, ocat = OLD.area(old_no), OLD.category_of(old_no)
    order, secs = split_sections(body)
    pre = secs[""]
    auto_start = next((i for i, l in enumerate(pre) if l.startswith("<!-- auto:")), len(pre))
    kept = "\n".join(pre[auto_start:]).strip("\n")
    cat_rel = paths.category_index_rel(cat.letter)
    head = [f"[홈]({paths.rel_link(new_rel, 'index.md')}) › {L(new_rel, cat_rel, cat.title)} › {a.title}", "",
            f"# {a.title}", "", '!!! info "소속 대분류"',
            f"    {L(new_rel, cat_rel, cat.title)} — 핵심 질문:", f"    {tag_line(cat.core_question)}", ""]
    if kept:
        head += [kept, ""]
    # 1절
    s1 = [tag_line(a.what), "", area_items_block(no), ""]
    parts = OLD_PARTS[old_no]
    if parts:
        s1 += ["이전 분류의 이 영역 가운데 일부는 새 분류에서 " + ", ".join(L(new_rel, paths.area_rel_path(p), SRC.area(p).title) for p in parts)
               + "(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.", ""]
    s1 += [f"이전 분류(2026-09-24)에서 이 페이지는 옛 {old_no}번 영역 ‘{oa.name}’(옛 대분류 {ocat.letter}. {ocat.name})이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.", "",
           f"> 옛 정의: {oa.what} {TAG_OLD}", "", f"> 옛 질문: {oa.question} {TAG_OLD}", ""]
    for n in OLD.area_notes(old_no):
        s1 += ["> 옛 원문 주석: " + n + " " + TAG_OLD, ""]
    old_cites = [l for l in secs.get("## 2. SCM 관점의 질문", []) if l.startswith("원문의 [")]
    for l in old_cites:
        s1 += ["이전 분류 기준: " + l, ""]
    # 2절
    s2 = [tag_line(a.question), ""]
    notes = SRC.area_notes(no)
    for n in notes:
        s2 += ["> 원문 주석: " + tag_line(n), ""]
    cite, refs = citation(new_rel, "\n".join(notes))
    if cite:
        s2 += [cite, ""]
    out = head + ["## 1. 한 줄 정의", ""] + s1 + ["## 2. 핵심 질문", ""] + s2
    for h in order[1:]:
        if h in ("## 1. 한 줄 정의", "## 2. SCM 관점의 질문"):
            continue
        content = secs[h]
        nh = HEADS.get(h, h)
        if nh.startswith("## 5.") and any(l.strip() and l.strip() != "아직 작성되지 않음" for l in content):
            content = ["", "> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다."] + content
        if nh.startswith("## 13."):
            have = "\n".join(content)
            add = [r.footnote(TODAY) for r in refs if f"[^{r.id}]:" not in have]
            if add:
                content = content + add + [""]
        out += [nh] + content
    return "\n".join(out)


def rebuild_category_body(new_rel, old_letter, body):
    cat = SRC.category(SUCC[old_letter])
    ocat = OLD.category(old_letter)
    order, secs = split_sections(body)
    pre = secs[""]
    auto_start = next((i for i, l in enumerate(pre) if l.startswith("<!-- auto:")), len(pre))
    kept = "\n".join(pre[auto_start:]).strip("\n")
    head = [f"[홈]({paths.rel_link(new_rel, 'index.md')}) › {cat.title}", "", f"# {cat.title}", ""]
    if kept:
        head += [kept, ""]
    notes = "\n\n".join(tag_line(n) for n in cat.notes)
    cite, refs = citation(new_rel, "\n".join(cat.notes))
    link_body = [l for l in secs.get("## 다른 대분류와의 연결", [])]
    has_old = any(l.strip() and "아직 작성되지 않음" not in l for l in link_body)
    recent = "\n".join(secs.get("## 최근 업데이트", [])).strip("\n")
    old_refs = "\n".join(l for l in secs.get("## 참고 자료", []) if l.startswith("[^")).strip("\n")
    out = head + ["## 핵심 질문", "", tag_line(cat.core_question), "", "## 개요", "", tag_line(cat.intro_paragraph), "",
                  "## 세부 연구영역", "",
                  "표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.", "",
                  "<!-- auto:category-area-table:start -->", "<!-- auto:category-area-table:end -->", "",
                  "## 이 대분류의 핵심 포인트", "", notes, "", "## 다른 대분류와의 연결", ""]
    if has_old:
        out += [f"> **이전 분류 기준 내용.** 아래는 이전 분류(7개 대분류)에서 {ocat.title} 페이지에 2026-09-25 작성한 연결이다. 대분류 이름은 그때의 것이고, 링크는 새 영역 페이지로 옮겨 두었다. 새 17개 대분류 기준의 연결은 이어지는 조사에서 다시 쓴다.", ""]
        out += link_body
    else:
        out += ["아직 작성되지 않음(에이전트가 채운다).", ""]
    out += ["## 최근 업데이트", "", recent, "", "## 참고 자료", ""]
    if cite:
        out += [cite, ""]
    new_defs = [r.footnote(TODAY) for r in refs if f"[^{r.id}]:" not in old_refs]
    out += new_defs + ([""] if new_defs else []) + ([old_refs] if old_refs else [])
    return "\n".join(out).rstrip("\n") + "\n"


# ---------------------------------------------------------------- 실행
def main():
    if (DOCS / "site-matrix.md").exists():
        raise SystemExit("이미 이관됨")
    move_files()
    moved_area = {PATHMAP[rel]: no for no, rel in OLD_AREA_REL.items()}
    moved_cat = {PATHMAP[f"categories/{slug}/index.md"]: letter for letter, slug in OLD_CAT_SLUG.items()}
    n = 0
    for p in sorted(DOCS.rglob("*.md")):
        rel = p.relative_to(DOCS).as_posix()
        raw = p.read_text(encoding="utf-8")
        meta, body = fm.read(p)
        body = rewrite_links(body, rel)
        body = rewrite_path_strings(body)
        body = retag(body)
        if rel in moved_area:
            body = rebuild_area_body(rel, moved_area[rel], body)
        elif rel in moved_cat:
            body = rebuild_category_body(rel, moved_cat[rel], body)
            meta["title"] = SRC.category(SUCC[moved_cat[rel]]).title
        body = replace_titles(body)
        if meta:
            meta = update_meta(meta, rel)
            if isinstance(meta.get("title"), str):
                meta["title"] = replace_titles(meta["title"])
            fm.write(p, meta, body)
        else:
            p.write_text(body, encoding="utf-8")
        if p.read_text(encoding="utf-8") != raw:
            n += 1
    print("pages changed", n)
    # data
    for f in list((WIKI / "data").glob("*.json")) + list((WIKI / "data" / "tracks").rglob("*.json")):
        t = f.read_text(encoding="utf-8")
        d = json.loads(rewrite_path_strings(t).replace(CHAT_OLD, CHAT_NEW))
        its = d.get("items") if isinstance(d, dict) else None
        for it in its or []:
            if not isinstance(it, dict):
                continue
            for k in ("areas", "related_areas"):
                if isinstance(it.get(k), list):
                    it[k] = remap_nos(it[k])
            if it.get("area_no") not in (None, ""):
                it["area_no"] = remap_nos(it["area_no"])
        f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    redirects = {k: v for k, v in PATHMAP.items()}
    (WIKI / "data" / "redirects.json").write_text(json.dumps(redirects, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    items_by_no = {}
    for i in items:
        items_by_no.setdefault(NUM[i["area"]], []).append({"id": i["id"], "name": i["name"], "def": i["def"]})
    lineage = {}
    for oa in mp["old_areas"]:
        lineage.setdefault(NUM[oa["main"]], {"main_old": [], "part_old": []})["main_old"].append(oa["num"])
        for pp in oa.get("parts") or []:
            lineage.setdefault(NUM[pp], {"main_old": [], "part_old": []})["part_old"].append(oa["num"])
    (WIKI / "data" / "area_items.json").write_text(json.dumps({"source": "_work/scope (2026-09-28 리스트업)", "areas": {str(k): v for k, v in sorted(items_by_no.items())}}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (WIKI / "data" / "area_lineage.json").write_text(json.dumps({"note": "새 영역 번호 → 옛 영역 번호(main_old: 본문을 이어받음, part_old: 일부에서 시작)", "old_titles": {str(n): OLD.area(n).title for n in range(1, 29)}, "areas": {str(k): v for k, v in sorted(lineage.items())}}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("data done")


if __name__ == "__main__":
    main()
