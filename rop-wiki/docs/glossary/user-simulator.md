---
title: "사용자 시뮬레이터 (User Simulator)"
type: glossary
term_ko: 사용자 시뮬레이터
term_en: User Simulator
definition: 대화형 에이전트를 평가할 때 목표와 정보를 가진 사용자를 규칙이나 LLM 으로 모사해 에이전트와 대화하게 하는 구성 요소다.
related_areas: [23, 27, 18]
tags: []
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-738, ref-739, ref-740]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 사용자 시뮬레이터

# 사용자 시뮬레이터 (User Simulator)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 사용자 시뮬레이터 | User Simulator | 없음 |

## 한 줄 정의

대화형 에이전트를 평가할 때 목표와 정보를 가진 사용자를 규칙이나 LLM 으로 모사해 에이전트와 대화하게 하는 구성 요소다. [추정][^ref-738][^ref-739][^ref-740]

## 설명

τ-bench 는 LLM 모의 사용자와 에이전트의 대화 끝 상태를 목표 상태와 비교해 채점한다. 모의 사용자 LLM 에 따라 성공률이 달라지고 체계적 보정 오차가 있다는 저자 보고가 있다. 관련 용어: 장애 주입(fault-injection), 회귀 시험(regression-testing).

## 관련 영역

- [23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)
- [27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)
- [18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)

## 출처

[^ref-738]: Yao, S. 외(Sierra, τ-bench 저자), τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains, 2024-06, https://arxiv.org/abs/2406.12045, 접근일 2026-09-25 (원문 미열람)
[^ref-739]: sierra-research (tau-bench GitHub), tau-bench — README, 미확인, https://github.com/sierra-research/tau-bench, 접근일 2026-09-25
[^ref-740]: Lost in Simulation 저자(arXiv 2601.17087, 게재처 미확인), Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations, 2026-01, https://arxiv.org/abs/2601.17087, 접근일 2026-09-25 (원문 미열람)

- 참고문헌 페이지: [ref-738](../references/ref-738.md), [ref-739](../references/ref-739.md), [ref-740](../references/ref-740.md)
