---
title: "안전 가드레일 (Safety Guardrail (LLM-enabled robots))"
type: glossary
term_ko: 안전 가드레일
term_en: Safety Guardrail (LLM-enabled robots)
definition: 언어 모델이 제안한 로봇 계획을 실행 전에 안전 규칙에 비추어 검사하고 위험한 부분을 막거나 고치는 별도의 감독 계층으로, RoboGuard 는 안전 규칙을 시간 논리 제약으로 바꿔 제어 합성으로 계획을 수정한다.
related_areas: [13, 12, 48]
tags: []
status: published
confidence: medium
created: 2026-10-09
updated: 2026-10-09
sources: [ref-700]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 안전 가드레일

# 안전 가드레일 (Safety Guardrail (LLM-enabled robots))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 안전 가드레일 | Safety Guardrail (LLM-enabled robots) | LLM-enabled robots — Safety Guardrail |

## 한 줄 정의

언어 모델이 제안한 로봇 계획을 실행 전에 안전 규칙에 비추어 검사하고 위험한 부분을 막거나 고치는 별도의 감독 계층으로, RoboGuard 는 안전 규칙을 시간 논리 제약으로 바꿔 제어 합성으로 계획을 수정한다. [추정][^ref-700]

## 설명

RoboGuard(arXiv v2 2026-03-03 초록)는 공격 프롬프트에서 격리된 신뢰 근간 언어 모델이 안전 규칙을 접지하고 시간 논리 제어 합성으로 위험 계획을 고치는 2단계 구조를 제안했다. 위험 계획 실행 감소 수치는 프리프린트 단일 출처의 저자 보고값이며 판에 따라 다르다.

## 관련 영역

- [13. 대화형 기능의 신뢰·기반](../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)
- [12. 채팅으로 업무 지시·오케스트레이션](../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)
- [48. 안전·위험 관리](../categories/safety/safety-and-risk-management.md)

## 출처

[^ref-700]: Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H., Safety Guardrails for LLM-Enabled Robots, 2025-03-10, https://arxiv.org/abs/2503.07885, 접근일 2026-10-09

- 참고문헌 페이지: [ref-700](../references/ref-700.md)
