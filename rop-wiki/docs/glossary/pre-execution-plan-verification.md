---
title: "사전 실행 계획 검증 (Pre-execution Plan Verification)"
type: glossary
term_ko: 사전 실행 계획 검증
term_en: Pre-execution Plan Verification
definition: 언어 모델이나 계획기가 만든 로봇 작업 계획을 실행하기 전에 논리 일관성·누락 단계·제약 위반을 자동으로 검사해 잘못된 계획이 로봇 동작으로 이어지지 않게 하는 절차다.
related_areas: [12, 13, 44, 54]
tags: []
status: published
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-753]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 사전 실행 계획 검증

# 사전 실행 계획 검증 (Pre-execution Plan Verification)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 사전 실행 계획 검증 | Pre-execution Plan Verification | 없음 |

## 한 줄 정의

언어 모델이나 계획기가 만든 로봇 작업 계획을 실행하기 전에 논리 일관성·누락 단계·제약 위반을 자동으로 검사해 잘못된 계획이 로봇 동작으로 이어지지 않게 하는 절차다. [추정][^ref-753]

## 설명

VerifyLLM(IROS 2025)은 자연어 지시를 선형 시간 논리(LTL)로 옮긴 뒤 언어 모델 추론으로 행동 순서열의 논리적 일관성과 빠진 단계를 실행 전에 찾는 2단계 검증 모듈이며, 가정 작업 데이터셋으로 평가하고 코드를 공개했다. 분류 원문의 "사람이 확인·승인한 계획만 실행" 앞단에서 승인자의 검토 부담을 줄이는 자동 관문으로 쓸 수 있다는 것이 구축자 추정이다.

## 관련 영역

- [12. 채팅으로 업무 지시·오케스트레이션](../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)
- [13. 대화형 기능의 신뢰·기반](../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)
- [44. 로봇 기반 모델·언어 모델 계획](../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md)
- [54. 시험·형식 검증·벤치마크](../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)

## 출처

[^ref-753]: Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025), VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots, 2025-07-07, https://arxiv.org/abs/2507.05118, 접근일 2026-09-29

- 참고문헌 페이지: [ref-753](../references/ref-753.md)
