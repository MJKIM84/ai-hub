---
title: "주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))"
type: glossary
term_ko: 주문 취소 즉시 동작
term_en: cancelOrder (VDA 5050 instant action)
definition: VDA 5050 에서 관제가 보내면 로봇이 가능한 한 빨리 정지하고 남은 동작을 실패로 보고한 뒤 유휴 상태가 되게 하는 즉시 동작이다.
related_areas: [20, 9, 12]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 주문 취소 즉시 동작

# 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 주문 취소 즉시 동작 | cancelOrder (VDA 5050 instant action) | VDA 5050 instant action — cancelOrder |

## 한 줄 정의

VDA 5050 에서 관제가 보내면 로봇이 가능한 한 빨리 정지하고 남은 동작을 실패로 보고한 뒤 유휴 상태가 되게 하는 즉시 동작이다. [추정][^ref-031]

## 설명

VDA 5050 3.0.0 기준. 예정 동작은 FAILED, 정지 뒤 cancelOrder 는 FINISHED 로 보고한다.

## 관련 영역

- [20. 예외 복구·재계획·업무 연속성](../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)
- [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)
- [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)

## 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25

- 참고문헌 페이지: [ref-031](../references/ref-031.md)
