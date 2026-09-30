---
title: "지도 버전 (Map Version (VDA 5050 mapId / mapVersion))"
type: glossary
term_ko: 지도 버전
term_en: Map Version (VDA 5050 mapId / mapVersion)
definition: 같은 작업 공간 구역을 가리키는 지도 식별자(mapId)에 붙는 갱신 표시로, VDA 5050 3.0.0 에서는 관제가 내려받게 한 여러 버전 가운데 같은 mapId 에서 한 버전만 활성화해 로봇이 쓰게 한다.
related_areas: [16, 15, 57]
tags: []
status: published
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 지도 버전

# 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 지도 버전 | Map Version (VDA 5050 mapId / mapVersion) | 없음 |

## 한 줄 정의

같은 작업 공간 구역을 가리키는 지도 식별자(mapId)에 붙는 갱신 표시로, VDA 5050 3.0.0 에서는 관제가 내려받게 한 여러 버전 가운데 같은 mapId 에서 한 버전만 활성화해 로봇이 쓰게 한다. [추정][^ref-031]

## 설명

VDA 5050 3.0.0(공식 저장소 main, 확인일 2026-09-30)에서 지도 상태는 ENABLED·DISABLED 이며 관제가 downloadMap·enableMap·deleteMap 즉시 동작으로 관리한다.

## 관련 영역

- [16. 장소 의미·지도 관리](../categories/space-and-map-model/place-semantics-and-map-management.md)
- [15. 지도·공간·위치 모델](../categories/space-and-map-model/map-space-and-location-model.md)
- [57. 자산·소프트웨어 수명주기 관리](../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30

- 참고문헌 페이지: [ref-031](../references/ref-031.md)
