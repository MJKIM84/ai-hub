---
title: "사가 (Saga)"
type: glossary
term_ko: 사가
term_en: Saga
definition: 오래 걸리는 작업을 작은 단계의 순서로 나누고 단계마다 보상 동작을 두어, 전부 완료되거나 부분 실행을 보상하게 하는 트랜잭션 구성 방식이다.
related_areas: [12, 20]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-373]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 사가

# 사가 (Saga)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 사가 | Saga | 없음 |

## 한 줄 정의

오래 걸리는 작업을 작은 단계의 순서로 나누고 단계마다 보상 동작을 두어, 전부 완료되거나 부분 실행을 보상하게 하는 트랜잭션 구성 방식이다. [추정][^ref-373]

## 설명

Garcia-Molina·Salem(1987)이 제안했으며, 보상은 의미상의 되돌림이지 처음 상태 복원을 보장하지 않는다.

## 관련 영역

- [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)
- [20. 예외 복구·재계획·업무 연속성](../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)

## 출처

[^ref-373]: Garcia-Molina, H., & Salem, K., Sagas, 1987, https://dl.acm.org/doi/10.1145/38713.38742, 접근일 2026-09-25 (원문 미열람)

- 참고문헌 페이지: [ref-373](../references/ref-373.md)
