---
title: "운용 상태 (Operational State (MassRobotics statusReport operationalState))"
type: glossary
term_ko: 운용 상태
term_en: Operational State (MassRobotics statusReport operationalState)
definition: MassRobotics AMR 상호운용 표준의 상태 보고에서 로봇이 지금 주행·대기·충전·사람 대기·수동 조작 중 어느 상태인지를 아홉 값 가운데 하나로 알리는 필드다.
related_areas: [37, 20, 21]
tags: []
status: published
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-253]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 운용 상태

# 운용 상태 (Operational State (MassRobotics statusReport operationalState))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 운용 상태 | Operational State (MassRobotics statusReport operationalState) | MassRobotics statusReport operationalState — Operational State |

## 한 줄 정의

MassRobotics AMR 상호운용 표준의 상태 보고에서 로봇이 지금 주행·대기·충전·사람 대기·수동 조작 중 어느 상태인지를 아홉 값 가운데 하나로 알리는 필드다. [추정][^ref-253]

## 설명

값은 navigating·idle·disabled·offline·charging·waitingHumanEvent·waitingExternalEvent·waitingInternalEvent·manualOverride 이며 statusReport 의 필수 항목이다. 이름이 비슷한 기존 용어 '운용 모드'(Operating Mode, VDA 5050 operatingMode)와는 다른 개념으로, 운용 상태는 MassRobotics 상태 보고가 로봇 단위로 알리는 상태 값이다.

## 관련 영역

- [37. 관제 화면·실행 기록](../categories/field-operations-and-monitoring/control-screen-and-execution-records.md)
- [20. 로봇·제조사 관제 연동](../categories/integration/robot-and-vendor-fleet-manager-integration.md)
- [21. 상호운용 표준·적합성](../categories/integration/interoperability-standards-and-conformance.md)

## 출처

[^ref-253]: MassRobotics (MassRobotics-AMR/AMR_Interop_Standard), AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-10-09 (원문 미열람)

- 참고문헌 페이지: [ref-253](../references/ref-253.md)
