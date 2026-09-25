---
title: "해제 구역 (Release Zone)"
type: glossary
term_ko: 해제 구역
term_en: Release Zone
definition: VDA 5050 3.0.0 에서 관제의 진입 허가를 받아야 이동로봇이 들어갈 수 있는 구역이다.
related_areas: [10, 9, 15]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 해제 구역

# 해제 구역 (Release Zone)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 해제 구역 | Release Zone | 없음 |

## 한 줄 정의

VDA 5050 3.0.0 에서 관제의 진입 허가를 받아야 이동로봇이 들어갈 수 있는 구역이다. [추정][^ref-031]

## 설명

로봇이 zoneRequests 로 진입을 요청하면 관제가 허가·대기·철회·거절로 답하고, 허가가 철회·만료될 때의 행동은 releaseLossBehavior(정지·계속·대피)로 정한다.

## 관련 영역

- [10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)
- [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)
- [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)

## 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25

- 참고문헌 페이지: [ref-031](../references/ref-031.md)
