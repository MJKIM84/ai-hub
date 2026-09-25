---
title: "배터리 건강 상태 (State of Health (SOH))"
type: glossary
term_ko: 배터리 건강 상태
term_en: State of Health (SOH)
definition: 배터리의 현재 용량·성능을 새 배터리 대비 비율로 나타낸 값으로, VDA 5050 상태 메시지의 batteryHealth 가 이에 해당한다.
related_areas: [24, 16]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-051]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 배터리 건강 상태

# 배터리 건강 상태 (State of Health (SOH))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 배터리 건강 상태 | State of Health (SOH) | SOH — State of Health |

## 한 줄 정의

배터리의 현재 용량·성능을 새 배터리 대비 비율로 나타낸 값으로, VDA 5050 상태 메시지의 batteryHealth 가 이에 해당한다. [추정][^ref-051]

## 설명

VDA 5050 상태 스키마는 충전 상태(stateOfCharge)와 별도로 batteryHealth 와 추정 도달 거리(range)를 로봇이 보고하게 한다.

## 관련 영역

- [24. 자산·소프트웨어 수명주기 관리](../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md)
- [16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)

## 출처

[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25

- 참고문헌 페이지: [ref-051](../references/ref-051.md)
