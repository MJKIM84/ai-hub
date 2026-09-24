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
SOURCE_FILE: Path = ROOT / "_source" / "ROP_SCM_연구분야_분류.md"
MKDOCS_YML: Path = ROOT / "mkdocs.yml"
SOURCE_HASH_FILE: Path = ROOT / "pipeline" / "checks" / "source.sha256"

# 대분류 폴더 slug (docs/categories/<slug>/index.md)
CATEGORY_SLUGS: dict[str, str] = {
    "A": "a-business-supply-chain-design",
    "B": "b-common-information-and-environment-model",
    "C": "c-connectivity-and-execution-foundation",
    "D": "d-planning-and-optimization",
    "E": "e-collaboration-and-field-operations",
    "F": "f-deployment-verification-and-maintenance",
    "G": "g-safety-security-intelligence-and-governance",
}
CATEGORY_LETTERS: list[str] = list(CATEGORY_SLUGS)

# 대분류별 세부영역 번호 범위 (포함)
CATEGORY_AREA_RANGES: dict[str, tuple[int, int]] = {
    "A": (1, 4), "B": (5, 8), "C": (9, 12), "D": (13, 16),
    "E": (17, 20), "F": (21, 24), "G": (25, 28),
}

# 세부영역 파일 slug (확장자 제외)
AREA_SLUGS: dict[int, str] = {
    1: "01-order-and-business-system-integration",
    2: "02-process-and-workflow-modeling",
    3: "03-capacity-site-and-facility-planning",
    4: "04-performance-economics-and-process-improvement",
    5: "05-robot-capability-and-task-ontology",
    6: "06-map-space-and-location-model",
    7: "07-cargo-inventory-and-asset-identification-and-tracking",
    8: "08-real-time-world-state-and-data-consistency",
    9: "09-robot-and-vendor-fleet-manager-integration",
    10: "10-facility-and-building-system-integration",
    11: "11-distributed-systems-communication-and-computing",
    12: "12-command-and-task-execution-reliability",
    13: "13-task-allocation-mrta",
    14: "14-task-sequencing-and-scheduling",
    15: "15-multi-robot-path-and-traffic-management-mapf",
    16: "16-shared-resource-charging-and-energy-optimization",
    17: "17-robot-to-robot-collaboration-and-physical-handover",
    18: "18-human-robot-collaboration-and-operator-interface",
    19: "19-monitoring-anomaly-detection-and-root-cause-analysis",
    20: "20-exception-recovery-replanning-and-business-continuity",
    21: "21-onboarding-configuration-and-commissioning",
    22: "22-simulation-and-predictive-digital-twin",
    23: "23-testing-formal-verification-and-benchmarking",
    24: "24-asset-and-software-lifecycle-management",
    25: "25-safety-and-risk-management",
    26: "26-cybersecurity-access-control-and-privacy",
    27: "27-ai-learning-adaptation-and-model-operations",
    28: "28-standards-interoperability-and-multi-vendor-governance",
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

# 물류 흐름 매트릭스 축 (원문 11장)
FLOW_STEPS: list[str] = ["입고", "적치", "보충", "피킹", "포장", "출하", "반품"]
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
