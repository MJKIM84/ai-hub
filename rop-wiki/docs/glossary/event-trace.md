---
title: "사건 트레이스 (Event Trace)"
type: glossary
term_ko: 사건 트레이스
term_en: Event Trace
definition: 시스템이나 시뮬레이터가 실행 중에 낸 사건을 시각 순서대로 기록한 구조화 목록으로, 재현 결과를 실제 기록이나 제약과 대조하는 데 쓴다.
related_areas: [11, 36, 54]
tags: []
status: published
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-825]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 사건 트레이스

# 사건 트레이스 (Event Trace)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 사건 트레이스 | Event Trace | 없음 |

## 한 줄 정의

시스템이나 시뮬레이터가 실행 중에 낸 사건을 시각 순서대로 기록한 구조화 목록으로, 재현 결과를 실제 기록이나 제약과 대조하는 데 쓴다. [추정][^ref-825]

## 설명

Chen 외(2026)는 자연어 사양에서 생성한 이산 사건 시스템 명세(Discrete Event System Specification, DEVS) 시뮬레이터가 내는 구조화 사건 트레이스를 사양에서 도출한 시간·인과·의미 제약과 대조해 검증하는 벤치마크를 제안했다. 11. 채팅으로 실제 상황 시뮬레이션 재현의 재현 충실도 확인이 이 대조에 기댄다.

## 관련 영역

- [11. 채팅으로 실제 상황 시뮬레이션 재현](../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md)
- [36. 가상 시운전·실제 상황 재현](../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md)
- [54. 시험·형식 검증·벤치마크](../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)

## 출처

[^ref-825]: Chen, Z., Zhuang, H., Li, Z., & Li, C., Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism, 2026-03-04, https://arxiv.org/abs/2603.03784, 접근일 2026-09-29

- 참고문헌 페이지: [ref-825](../references/ref-825.md)
