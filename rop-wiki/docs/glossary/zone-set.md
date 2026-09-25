---
title: "구역 집합 (Zone Set (VDA 5050 zoneSet))"
type: glossary
term_ko: 구역 집합
term_en: Zone Set (VDA 5050 zoneSet)
definition: 하나의 지도(mapId)에 붙는 다각형 구역들의 묶음으로, 구역마다 통행 금지·진입 허가·속도 제한·우선·벌점·방향 같은 유형과 파라미터를 둔다.
related_areas: [6, 15, 28]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-442, ref-031]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 구역 집합

# 구역 집합 (Zone Set (VDA 5050 zoneSet))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 구역 집합 | Zone Set (VDA 5050 zoneSet) | VDA 5050 zoneSet — Zone Set |

## 한 줄 정의

하나의 지도(mapId)에 붙는 다각형 구역들의 묶음으로, 구역마다 통행 금지·진입 허가·속도 제한·우선·벌점·방향 같은 유형과 파라미터를 둔다. [추정][^ref-442][^ref-031]

## 설명

VDA 5050 3.0.0 에서 구역 집합은 구역 집합 식별자·지도 식별자·구역 목록을 갖고, 각 구역은 꼭짓점 3개 이상의 다각형과 10종 유형(BLOCKED·LINE_GUIDED·RELEASE·COORDINATED_REPLANNING·SPEED_LIMIT·ACTION·PRIORITY·PENALTY·DIRECTED·BIDIRECTED) 가운데 하나로 표현되며 zoneSet 토픽이나 downloadZoneSet 동작으로 전달된다. 한 지도에 활성 구역 집합은 하나다. 관련 용어: [해제 구역](release-zone.md), [VDA 5050](vda-5050.md), [레이아웃 교환 형식](layout-interchange-format.md), [점유 격자 지도](occupancy-grid-map.md).

## 관련 영역

- [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)
- [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)
- [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 출처

[^ref-442]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/zoneSet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/zoneSet.schema, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25

- 참고문헌 페이지: [ref-442](../references/ref-442.md), [ref-031](../references/ref-031.md)
