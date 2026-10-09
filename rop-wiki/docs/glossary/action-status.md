---
title: "동작 상태 (Action Status (VDA 5050 actionStatus))"
type: glossary
term_ko: 동작 상태
term_en: Action Status (VDA 5050 actionStatus)
definition: VDA 5050 에서 로봇이 받은 각 동작의 진행을 INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE 값으로 플릿 관제에 보고하는 상태 값이다.
related_areas: [37, 20, 29]
tags: []
status: published
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-031]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 동작 상태

# 동작 상태 (Action Status (VDA 5050 actionStatus))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 동작 상태 | Action Status (VDA 5050 actionStatus) | VDA 5050 actionStatus — Action Status |

## 한 줄 정의

VDA 5050 에서 로봇이 받은 각 동작의 진행을 INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE 값으로 플릿 관제에 보고하는 상태 값이다. [추정][^ref-031]

## 설명

VDA 5050 3.0.0 기준이다. logReport 즉시 동작에서는 보고서가 저장되면 FINISHED 와 함께 저장된 로그 이름을 동작 상태로 보고한다.

## 관련 영역

- [37. 관제 화면·실행 기록](../categories/field-operations-and-monitoring/control-screen-and-execution-records.md)
- [20. 로봇·제조사 관제 연동](../categories/integration/robot-and-vendor-fleet-manager-integration.md)
- [29. 명령·작업 실행의 신뢰성](../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md)

## 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09

- 참고문헌 페이지: [ref-031](../references/ref-031.md)
