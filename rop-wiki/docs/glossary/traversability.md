---
title: "통과 가능성 (Traversability)"
type: glossary
term_ko: 통과 가능성
term_en: Traversability
definition: 특정 로봇이 공간 그래프의 구역·차선·문·계단·승강기를 지나갈 수 있는지를 로봇 능력(정적 조건)으로 판정하는 통과 가능 여부이며, 문 닫힘 같은 현재 상태는 8. 실시간 세계 상태·데이터 일관성 쪽에서 따로 다룬다.
related_areas: [6, 5, 8, 13]
tags: []
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-573, ref-574, ref-461, ref-229]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 통과 가능성

# 통과 가능성 (Traversability)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 통과 가능성 | Traversability | 없음 |

## 한 줄 정의

특정 로봇이 공간 그래프의 구역·차선·문·계단·승강기를 지나갈 수 있는지를 로봇 능력(정적 조건)으로 판정하는 통과 가능 여부이며, 문 닫힘 같은 현재 상태는 8. 실시간 세계 상태·데이터 일관성 쪽에서 따로 다룬다. [추정][^ref-573][^ref-574][^ref-461][^ref-229]

## 설명

이 위키는 공간 요소의 통과 조건(문 폭·자동 구동 여부, 계단 단 높이 등)과 로봇 제공 능력 속성을 맞추는 요구–제공 능력 매칭으로 판정할 수 있다고 추정한다. 이렇게 정의한 단일 출처는 확인하지 못했다.

## 관련 영역

- [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)
- [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)
- [8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)
- [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)

## 출처

[^ref-573]: buildingSMART International, Pset_DoorCommon - IFC 4.3.2 Documentation, 미확인, https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_DoorCommon.htm, 접근일 2026-09-25 (원문 미열람)
[^ref-574]: buildingSMART International, Pset_StairCommon - IFC4.3.2.0 Documentation, 미확인, https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/Pset_StairCommon.htm, 접근일 2026-09-25 (원문 미열람)
[^ref-461]: Buildings(MDPI) 게재 논문 저자(Concordia University, 목록 미확인), Ontology for BIM-Based Robotic Navigation and Inspection Tasks, 2024, https://www.mdpi.com/2075-5309/14/8/2274, 접근일 2026-09-25 (원문 미열람)
[^ref-229]: IDTA (admin-shell-io/submodel-templates GitHub), IDTA 02020 Capability Description — README (Submodel Template, Version 1.0), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-25 (원문 미열람)

- 참고문헌 페이지: [ref-573](../references/ref-573.md), [ref-574](../references/ref-574.md), [ref-461](../references/ref-461.md), [ref-229](../references/ref-229.md)
