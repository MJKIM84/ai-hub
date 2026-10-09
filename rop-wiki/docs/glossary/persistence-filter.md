---
title: "지속성 필터 (Persistence Filter)"
type: glossary
term_ko: 지속성 필터
term_en: Persistence Filter
definition: 반정적 환경의 특징이 마지막 관측 뒤에도 아직 남아 있을 확률을 시간에 따라 재귀적으로 계산하는 베이즈 추정기다.
related_areas: [18, 15]
tags: []
status: published
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1279, ref-1280]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 지속성 필터

# 지속성 필터 (Persistence Filter)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 지속성 필터 | Persistence Filter | 없음 |

## 한 줄 정의

반정적 환경의 특징이 마지막 관측 뒤에도 아직 남아 있을 확률을 시간에 따라 재귀적으로 계산하는 베이즈 추정기다. [추정][^ref-1279][^ref-1280]

## 설명

Rosen·Mason·Leonard(ICRA 2016)가 제시했고, Perpetua(2025)는 지속성 필터와 출현 필터를 혼합해 특징의 소멸·재출현을 함께 추정한다. 확인한 적용 대상은 로봇 지도의 특징이며 설비 상태 적용 사례는 확인되지 않았다.

## 관련 영역

- [18. 실시간 세계 상태·데이터 일관성](../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md)
- [15. 지도·공간·위치 모델](../categories/space-and-map-model/map-space-and-location-model.md)

## 출처

[^ref-1279]: Rosen, D. M., Mason, J., & Leonard, J. J. (MIT DSpace; ICRA 2016), Towards lifelong feature-based mapping in semi-static environments, 2016-06, https://dspace.mit.edu/handle/1721.1/107620, 접근일 2026-10-09
[^ref-1280]: Saavedra-Ruiz, M., Nashed, S. B., Gauthier, C., & Paull, L. (arXiv; IROS 2025 채택 표기), Perpetua: Multi-Hypothesis Persistence Modeling for Semi-Static Environments, 2025-07-24, https://arxiv.org/abs/2507.18808, 접근일 2026-10-09

- 참고문헌 페이지: [ref-1279](../references/ref-1279.md), [ref-1280](../references/ref-1280.md)
