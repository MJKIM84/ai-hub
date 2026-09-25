---
title: "운용 모드 (Operating Mode (VDA 5050 operatingMode))"
type: glossary
term_ko: 운용 모드
term_en: Operating Mode (VDA 5050 operatingMode)
definition: VDA 5050 에서 이동로봇이 관제 주문을 자동 실행하는지, HMI가 주행 속도를 제어하는지, 운영자가 제어를 넘겨받았는지 등을 알리는 상태 값이다.
related_areas: [9, 18]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-051, ref-031]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 운용 모드

# 운용 모드 (Operating Mode (VDA 5050 operatingMode))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 운용 모드 | Operating Mode (VDA 5050 operatingMode) | VDA 5050 operatingMode — Operating Mode |

## 한 줄 정의

VDA 5050 에서 이동로봇이 관제 주문을 자동 실행하는지, HMI가 주행 속도를 제어하는지, 운영자가 제어를 넘겨받았는지 등을 알리는 상태 값이다. [추정][^ref-051][^ref-031]

## 설명

상태 메시지의 operatingMode 는 STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN 일곱 값이다(2026-09-25 확인).

## 관련 영역

- [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)
- [18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)

## 출처

[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25

- 참고문헌 페이지: [ref-051](../references/ref-051.md), [ref-031](../references/ref-031.md)
