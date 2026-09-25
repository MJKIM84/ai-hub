---
title: "공간 그래프 (Space Graph)"
type: glossary
term_ko: 공간 그래프
term_en: Space Graph
definition: 방·복도 같은 공간을 노드로, 문·공유 경계·계단·엘리베이터 같은 연결을 엣지로 두어 건물 실내의 연결 관계를 나타내는 그래프로, IndoorGML 의 쌍대 그래프가 대표적 표준 표현이다.
related_areas: [6, 15, 28]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-331, ref-332]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 공간 그래프

# 공간 그래프 (Space Graph)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 공간 그래프 | Space Graph | 없음 |

## 한 줄 정의

방·복도 같은 공간을 노드로, 문·공유 경계·계단·엘리베이터 같은 연결을 엣지로 두어 건물 실내의 연결 관계를 나타내는 그래프로, IndoorGML 의 쌍대 그래프가 대표적 표준 표현이다. [추정][^ref-331][^ref-332]

## 설명

IndoorGML 은 3차원 공간(셀)을 쌍대 공간의 노드로, 두 공간이 공유하는 경계면을 엣지로 바꾸어 공간 연결 그래프를 만든다. 이 위키의 건축 도면 자동 인식 트랙은 공간 그래프 스키마 초안에서 개념·관계를 정한다.

## 관련 영역

- [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)
- [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)
- [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 출처

[^ref-331]: OGC (Open Geospatial Consortium), OGC IndoorGML 2.0 Part 1 – Conceptual Model (22-045r5), 2025-08, https://docs.ogc.org/is/22-045r5/22-045r5.html, 접근일 2026-09-25 (원문 미열람)
[^ref-332]: OGC (Open Geospatial Consortium), OGC Publishes IndoorGML 2.0 Part 1 Conceptual Model Standard, 2025-08-28, https://www.ogc.org/announcement/ogc-publishes-indoorgml-2-0-part-1-conceptual-model-standard/, 접근일 2026-09-25 (원문 미열람)

- 참고문헌 페이지: [ref-331](../references/ref-331.md), [ref-332](../references/ref-332.md)
