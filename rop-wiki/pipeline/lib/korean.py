"""한국어 조사 선택 도우미.

숫자 뒤에 붙는 주제 조사 '은/는' 을 숫자 읽기(일·이·삼·사·오·육·칠·팔·구·십)의 받침 여부로 고른다.
예: "[1]은", "[2]는", "[3]은", "[4]는", "[10]은", "[12]는".
"""
from __future__ import annotations

# 마지막 자리 숫자의 한국어 읽기가 받침으로 끝나는지 (0 은 십·백·천 등으로 읽어 받침이 있다)
_FINAL_HAS_BATCHIM: dict[int, bool] = {
    0: True,   # 십, 백, 천 …
    1: True,   # 일
    2: False,  # 이
    3: True,   # 삼
    4: False,  # 사
    5: False,  # 오
    6: True,   # 육
    7: True,   # 칠
    8: True,   # 팔
    9: False,  # 구
}


def number_has_batchim(n: int) -> bool:
    """정수 n 을 한자어 숫자로 읽었을 때 마지막 음절에 받침이 있는지."""
    return _FINAL_HAS_BATCHIM[abs(int(n)) % 10]


def topic_particle(n: int) -> str:
    """숫자 n 뒤의 주제 조사: 받침이 있으면 '은', 없으면 '는'."""
    return "은" if number_has_batchim(n) else "는"
