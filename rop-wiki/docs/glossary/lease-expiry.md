---
title: "허가 만료 시각 (Lease Expiry (VDA 5050 leaseExpiry))"
type: glossary
term_ko: 허가 만료 시각
term_en: Lease Expiry (VDA 5050 leaseExpiry)
definition: VDA 5050 에서 관제가 구역·간선 사용 허가에 붙이는 만료 시각으로, 이 시각이 지나면 허가는 무효가 되어 요청 상태가 EXPIRED 로 바뀐다.
related_areas: [18, 20, 27]
tags: []
status: published
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-031]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 허가 만료 시각

# 허가 만료 시각 (Lease Expiry (VDA 5050 leaseExpiry))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 허가 만료 시각 | Lease Expiry (VDA 5050 leaseExpiry) | VDA 5050 leaseExpiry — Lease Expiry |

## 한 줄 정의

VDA 5050 에서 관제가 구역·간선 사용 허가에 붙이는 만료 시각으로, 이 시각이 지나면 허가는 무효가 되어 요청 상태가 EXPIRED 로 바뀐다. [추정][^ref-031]

## 설명

관제는 같은 requestId 로 새 만료 시각을 보내 허가를 연장한다(VDA 5050 3.0.0).

## 관련 영역

- [18. 실시간 세계 상태·데이터 일관성](../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md)
- [20. 로봇·제조사 관제 연동](../categories/integration/robot-and-vendor-fleet-manager-integration.md)
- [27. 다중 로봇 경로·교통 관리 — MAPF](../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)

## 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09

- 참고문헌 페이지: [ref-031](../references/ref-031.md)
