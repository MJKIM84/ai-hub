---
title: "4차원 장면 그래프 (4D Scene Graph)"
type: glossary
term_ko: 4차원 장면 그래프
term_en: 4D Scene Graph
definition: 3차원 장면 그래프(3D Scene Graph)의 장소·물체 노드에 시간 축을 더해 사람 존재나 흐름 같은 시간에 따라 변하는 상태를 함께 표현·예측하는 표현이다.
related_areas: [19, 16, 46]
tags: []
status: published
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1294]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 4차원 장면 그래프

# 4차원 장면 그래프 (4D Scene Graph)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 4차원 장면 그래프 | 4D Scene Graph | 없음 |

## 한 줄 정의

3차원 장면 그래프(3D Scene Graph)의 장소·물체 노드에 시간 축을 더해 사람 존재나 흐름 같은 시간에 따라 변하는 상태를 함께 표현·예측하는 표현이다. [추정][^ref-1294]

## 설명

기존 용어 3차원 장면 그래프(3d-scene-graph)를 시간 축으로 확장한 것이다. Kairos(Catalano 외, 2026-09-23, 동료심사 전 프리프린트)는 복셀마다 사람 존재율과 이동 방향 분포를 두고 미래 시각을 예측해 주행 노드 단위로 모은다.

## 관련 영역

- [19. 사람·보행자 모델](../categories/objects-people-and-live-state/people-and-pedestrian-model.md)
- [16. 장소 의미·지도 관리](../categories/space-and-map-model/place-semantics-and-map-management.md)
- [46. 예측·학습 기반 최적화](../categories/ai-and-learning/prediction-and-learning-based-optimization.md)

## 출처

[^ref-1294]: Catalano, I., Placed, J. A., Civera, J., & Peña Queralta, J. (arXiv), Kairos: Grounded Forecasting of Presence and Directional Flow in 4D Scene Graphs, 2026-09-23, https://arxiv.org/abs/2609.27467, 접근일 2026-10-09

- 참고문헌 페이지: [ref-1294](../references/ref-1294.md)
