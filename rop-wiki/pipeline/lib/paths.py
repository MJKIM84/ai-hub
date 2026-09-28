"""저장소 경로와 슬러그 규약.

경로 규약은 빌드 사양서 3장에 고정돼 있으며 바꾸지 않는다.
ROOT 는 이 파일(pipeline/lib/paths.py) 기준 상위 2단계, 즉 위키 루트다.
"""
from __future__ import annotations

import os
from datetime import date
from pathlib import Path, PurePosixPath

ROOT: Path = Path(__file__).resolve().parents[2]
DOCS: Path = ROOT / "docs"
DATA: Path = ROOT / "data"
RUNS: Path = ROOT / "runs"
CONFIG: Path = ROOT / "config"
SOURCE_FILE: Path = ROOT / "_source" / "ROP_연구분야_분류.md"
# 2026-09-28 개정 전 원문(보관본). [옛 분류원문] 태그 줄은 이 파일과 대조한다
OLD_SOURCE_FILE: Path = ROOT / "_source" / "archive" / "ROP_SCM_연구분야_분류_2026-09-24.md"
MKDOCS_YML: Path = ROOT / "mkdocs.yml"
SOURCE_HASH_FILE: Path = ROOT / "pipeline" / "checks" / "source.sha256"

# 대분류 폴더 slug (docs/categories/<slug>/index.md). 2026-09-28 개정: 17개 대분류, 문자 접두어 없는 slug
CATEGORY_SLUGS: dict[str, str] = {
    "A": "planning-and-business",
    "B": "robot-ontology",
    "C": "chat-based-configuration-and-operation",
    "D": "space-and-map-model",
    "E": "objects-people-and-live-state",
    "F": "integration",
    "G": "planning-and-optimization",
    "H": "execution-collaboration-and-recovery",
    "I": "design-and-simulation",
    "J": "field-operations-and-monitoring",
    "K": "platform-architecture-and-infrastructure",
    "L": "ai-and-learning",
    "M": "safety",
    "N": "security-and-privacy",
    "O": "verification-deployment-and-lifecycle",
    "P": "governance-law-and-society",
    "Q": "site-type-applications",
}
CATEGORY_LETTERS: list[str] = list(CATEGORY_SLUGS)

# 대분류별 세부영역 번호 범위 (포함)
CATEGORY_AREA_RANGES: dict[str, tuple[int, int]] = {
    "A": (1, 3),
    "B": (4, 7),
    "C": (8, 13),
    "D": (14, 16),
    "E": (17, 19),
    "F": (20, 23),
    "G": (24, 28),
    "H": (29, 32),
    "I": (33, 36),
    "J": (37, 40),
    "K": (41, 43),
    "L": (44, 47),
    "M": (48, 50),
    "N": (51, 53),
    "O": (54, 57),
    "P": (58, 60),
    "Q": (61, 67),
}

# 세부영역 파일 slug (확장자 제외). 2026-09-28 개정: 67개 영역, 번호 접두어 없는 slug(번호가 바뀌어도 주소 유지)
AREA_SLUGS: dict[int, str] = {
    1: "technology-market-and-vendor-trends",
    2: "use-cases-requirements-and-scope",
    3: "economics-procurement-and-business-models",
    4: "heterogeneous-robot-registration",
    5: "robot-capability-and-task-representation",
    6: "ontology-based-system-and-robot-integration",
    7: "ontology-verification-and-change-management",
    8: "chat-map-authoring",
    9: "chat-scenario-composition",
    10: "chat-robot-configuration",
    11: "chat-real-situation-simulation-replay",
    12: "chat-task-instruction-and-orchestration",
    13: "conversational-trust-and-foundations",
    14: "maps-from-floor-plans-and-bim",
    15: "map-space-and-location-model",
    16: "place-semantics-and-map-management",
    17: "work-object-and-asset-identification-and-handover-tracking",
    18: "real-time-world-state-and-data-consistency",
    19: "people-and-pedestrian-model",
    20: "robot-and-vendor-fleet-manager-integration",
    21: "interoperability-standards-and-conformance",
    22: "facility-and-building-system-integration",
    23: "business-system-integration",
    24: "task-and-workflow-modeling",
    25: "task-allocation-mrta",
    26: "task-sequencing-and-scheduling",
    27: "multi-robot-path-and-traffic-management-mapf",
    28: "shared-resource-charging-and-energy-optimization",
    29: "command-and-task-execution-reliability",
    30: "robot-to-robot-collaboration-and-physical-handover",
    31: "human-robot-collaboration",
    32: "exception-recovery-replanning-and-business-continuity",
    33: "scenario-model-and-editing",
    34: "simulation-and-predictive-digital-twin",
    35: "capacity-sizing-and-layout-design",
    36: "virtual-commissioning-and-real-situation-replay",
    37: "control-screen-and-execution-records",
    38: "monitoring-anomaly-detection-and-root-cause-analysis",
    39: "operational-performance-measurement-and-improvement",
    40: "operating-procedures-and-request-channels",
    41: "platform-architecture-and-external-api",
    42: "distributed-systems-communication-and-computing",
    43: "data-observability-and-deployment",
    44: "robot-foundation-models-and-llm-planning",
    45: "document-drawing-and-scene-understanding",
    46: "prediction-and-learning-based-optimization",
    47: "ai-learning-adaptation-and-model-operations",
    48: "safety-and-risk-management",
    49: "human-proximity-safety",
    50: "safety-standards-certification-and-incident-investigation",
    51: "authentication-authorization-and-isolation",
    52: "communication-protection-threat-management-and-audit",
    53: "privacy-and-video-data",
    54: "testing-formal-verification-and-benchmarking",
    55: "site-survey-installation-and-commissioning",
    56: "operations-handover-scale-out-and-training",
    57: "asset-and-software-lifecycle-management",
    58: "multi-party-responsibility-contracts-and-data",
    59: "law-regulation-insurance-and-licensing",
    60: "labor-acceptance-and-accessibility",
    61: "warehouse",
    62: "manufacturing-plant",
    63: "hospital-and-healthcare",
    64: "commercial-facilities",
    65: "home-and-apartment",
    66: "outdoor",
    67: "other-sites",
}
AREA_NOS: list[int] = sorted(AREA_SLUGS)

# 소개 페이지 순서 (사양서 4.2 표 순서)
ABOUT_ORDER: list[str] = [
    "what-is-rop", "scope-boundary", "research-method", "idea-mapping",
    "agents", "reading-guide", "how-to-contribute",
]

# 트랙 페이지 순서 (사양서 4.8)
TRACK_PAGE_ORDER: list[str] = [
    "index.md",
    # stage-1 ~ stage-7 은 glob 으로 사이에 끼운다
    "ontology-draft.md", "model-standard-comparison.md", "document-type-matrix.md",
    "evaluation-and-verification.md", "question-backlog.md", "log.md", "experiments.md",
]

# 트랙마다 자기 살아있는 초안 페이지를 config/tracks/<slug>.yaml 의 draft_page 로 선언한다 [가정].
# 선언이 없으면 첫 트랙의 규약(ontology-draft.md · ontology_versions.json)을 쓴다.
DEFAULT_DRAFT_PAGE: str = "ontology-draft.md"
DEFAULT_DRAFT_VERSIONS: str = "ontology_versions.json"

# 확장 아이디어 섹션(docs/ideas/). 색인 다음에 트랙 정의의 idea_page 가 트랙 순서(order)대로 온다 [가정]
IDEAS_DIR: str = "ideas"
IDEAS_INDEX: str = "ideas/index.md"

# 현장 유형 × 대분류 적용 사례 매트릭스의 축 (원문 21장 연구 방법)
SITE_TYPES: list[str] = ["물류창고", "제조 공장", "병원", "상업 시설", "가정", "실외", "기타"]
# 적용 사례마다 채우는 여섯 항목 (원문 21장)
FLOW_ITEMS: list[str] = ["시작 조건", "작업 대상", "수행 자원", "제약", "완료·인계", "예외·성과"]


def today() -> str:
    """오늘 날짜(ISO). 환경변수 ROP_TODAY 가 있으면 그 값을 쓴다(재현 가능한 빌드용)."""
    return os.environ.get("ROP_TODAY") or date.today().isoformat()


def category_letter_of(no: int) -> str:
    for letter, (lo, hi) in CATEGORY_AREA_RANGES.items():
        if lo <= int(no) <= hi:
            return letter
    raise ValueError(f"세부영역 번호 범위 밖: {no}")


def area_nos_of(letter: str) -> list[int]:
    lo, hi = CATEGORY_AREA_RANGES[letter]
    return list(range(lo, hi + 1))


# --- docs 기준 상대 경로 (문자열, posix) -------------------------------------

def category_rel_dir(letter: str) -> str:
    return f"categories/{CATEGORY_SLUGS[letter]}"


def category_index_rel(letter: str) -> str:
    return f"{category_rel_dir(letter)}/index.md"


def area_rel_path(no: int) -> str:
    letter = category_letter_of(no)
    return f"{category_rel_dir(letter)}/{AREA_SLUGS[int(no)]}.md"


def area_repo_path(no: int) -> str:
    """저장소 루트 기준 경로("docs/…"). data/*.json 의 link/page 필드 형식."""
    return f"docs/{area_rel_path(no)}"


def category_repo_path(letter: str) -> str:
    return f"docs/{category_index_rel(letter)}"


# --- 절대 경로 ------------------------------------------------------------------

def category_dir(letter: str) -> Path:
    return DOCS / "categories" / CATEGORY_SLUGS[letter]


def category_index(letter: str) -> Path:
    return category_dir(letter) / "index.md"


def area_file(no: int) -> Path:
    return DOCS / area_rel_path(no)


def track_dir(slug: str) -> Path:
    return DOCS / "tracks" / slug


def track_config(slug: str) -> Path:
    return CONFIG / "tracks" / f"{slug}.yaml"


def track_backlog(slug: str) -> Path:
    return DATA / "tracks" / slug / "backlog.json"


# --- 트랙 정의 읽기(여러 트랙 공통) ---------------------------------------------------------

def read_track_config(slug: str) -> dict:
    """config/tracks/<slug>.yaml 을 읽는다. 없거나 깨졌으면 빈 dict."""
    import yaml  # 지연 import: paths 는 가벼운 모듈로 둔다
    p = track_config(slug)
    if not p.is_file():
        return {}
    try:
        data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def _order_key(slug: str, cfg: dict) -> tuple:
    try:
        order = int(cfg.get("order"))
    except (TypeError, ValueError):
        order = 10_000
    return (order, slug)


def ordered_track_slugs() -> list[str]:
    """트랙 slug 목록. config/tracks/*.yaml 을 order 값(없으면 뒤로), 같으면 slug 순으로 정렬하고,
    정의 파일 없이 docs/tracks/<slug>/ 만 있는 트랙을 그 뒤에 slug 순으로 붙인다.
    첫 트랙(manual-capability-ontology)은 order: 1 이라 언제나 맨 앞이다 [가정]."""
    slugs: list[str] = []
    d = CONFIG / "tracks"
    if d.is_dir():
        pairs = [(p.stem, read_track_config(p.stem)) for p in d.glob("*.yaml")]
        slugs = [s for s, _ in sorted(pairs, key=lambda x: _order_key(*x))]
    t = DOCS / "tracks"
    if t.is_dir():
        slugs += [p.name for p in sorted(t.iterdir()) if p.is_dir() and p.name not in slugs]
    return slugs


def track_draft_page(slug: str, cfg: dict | None = None) -> str:
    """트랙의 살아있는 초안 페이지 파일명(docs/tracks/<slug>/ 아래). yaml 의 draft_page, 없으면 ontology-draft.md."""
    cfg = read_track_config(slug) if cfg is None else cfg
    return str(cfg.get("draft_page") or DEFAULT_DRAFT_PAGE)


def track_draft_rel(slug: str, cfg: dict | None = None) -> str:
    """초안 페이지의 docs 기준 경로."""
    return f"tracks/{slug}/{track_draft_page(slug, cfg)}"


def track_draft_versions(slug: str, cfg: dict | None = None) -> Path:
    """초안 버전 이력 원천 데이터(data/tracks/<slug>/<draft_versions>). 없으면 ontology_versions.json."""
    cfg = read_track_config(slug) if cfg is None else cfg
    return DATA / "tracks" / slug / str(cfg.get("draft_versions") or DEFAULT_DRAFT_VERSIONS)


def track_page_order(slug: str, cfg: dict | None = None) -> list[str]:
    """트랙 하위 페이지 순서(사양서 4.8: 개요 → 단계 → 초안 → 비교표·매트릭스·평가 절차 → 질문 백로그 → 로그 → 실험).
    TRACK_PAGE_ORDER 의 ontology-draft.md 자리를 그 트랙의 draft_page 로 바꾼 목록이다(첫 트랙은 TRACK_PAGE_ORDER 그대로)."""
    draft = track_draft_page(slug, cfg)
    return [draft if n == DEFAULT_DRAFT_PAGE else n for n in TRACK_PAGE_ORDER]


def idea_page_rels() -> list[str]:
    """확장 아이디어 페이지(docs 기준 경로) 목록. 트랙 순서대로 각 트랙 정의의 idea_page 를 모은다(색인 제외)."""
    out: list[str] = []
    for slug in ordered_track_slugs():
        rel = idea_page_rel(read_track_config(slug))
        if rel and rel not in out:
            out.append(rel)
    return out


def idea_page_rel(cfg: dict) -> str | None:
    """트랙 정의의 idea_page("docs/ideas/x.md", "ideas/x.md", "x.md" 모두 허용)를 docs 기준 경로로."""
    page = (cfg or {}).get("idea_page")
    if not page:
        return None
    rel = docs_rel(str(page))
    return rel if "/" in rel else f"{IDEAS_DIR}/{rel}"


# --- 경로 변환 도우미 ---------------------------------------------------------------

def docs_rel(path: Path | str) -> str:
    """절대 경로 또는 "docs/…" 경로를 docs 기준 posix 상대 경로로 바꾼다."""
    p = Path(path)
    if p.is_absolute():
        return p.resolve().relative_to(DOCS.resolve()).as_posix()
    s = p.as_posix()
    if s.startswith("docs/"):
        return s[len("docs/"):]
    return s


def rel_link(from_rel: str, to_rel: str) -> str:
    """docs 기준 상대 경로 두 개 사이의 마크다운 링크 경로를 만든다.

    rel_link("index.md", "about/what-is-rop.md") -> "about/what-is-rop.md"
    rel_link("categories/b-x/07-y.md", "references/ref-003.md") -> "../../references/ref-003.md"
    """
    from_dir = PurePosixPath(docs_rel(from_rel)).parent
    to = PurePosixPath(docs_rel(to_rel))
    return os.path.relpath(str(to), start=str(from_dir) if str(from_dir) != "." else ".").replace(os.sep, "/")


def is_under(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False
