---
title: "보상 트랜잭션 (Compensating Transaction)"
type: glossary
term_ko: 보상 트랜잭션
term_en: Compensating Transaction
definition: 여러 단계로 이루어진 작업이 도중에 실패했을 때 이미 완료된 단계의 효과를 업무 규칙에 맞게 되돌리는 작업이다.
related_areas: [20, 1, 12]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-489]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 보상 트랜잭션

# 보상 트랜잭션 (Compensating Transaction)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 보상 트랜잭션 | Compensating Transaction | 없음 |

## 한 줄 정의

여러 단계로 이루어진 작업이 도중에 실패했을 때 이미 완료된 단계의 효과를 업무 규칙에 맞게 되돌리는 작업이다. [추정][^ref-489]

## 설명

원래 상태를 그대로 복원하는 것이 아니라 보정하며, 보상 자체가 실패할 수 있으므로 단계를 멱등 명령으로 정의하고 진행 상황을 기록해 실패 지점부터 재개하라고 권한다. 소프트웨어 설계 패턴이며 물리 작업·재고 되돌림 적용은 추정 단계다.

## 관련 영역

- [20. 예외 복구·재계획·업무 연속성](../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)
- [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)
- [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)

## 출처

[^ref-489]: Microsoft (MicrosoftDocs/architecture-center), Compensating Transaction pattern, 2026-04-16, https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction, 접근일 2026-09-25

- 참고문헌 페이지: [ref-489](../references/ref-489.md)
