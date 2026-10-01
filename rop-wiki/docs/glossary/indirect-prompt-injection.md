---
title: "간접 프롬프트 주입 (Indirect Prompt Injection)"
type: glossary
term_ko: 간접 프롬프트 주입
term_en: Indirect Prompt Injection
definition: 프롬프트 주입(Prompt Injection)의 하위 유형으로, 사용자가 직접 입력하지 않은 웹 페이지·파일·인식 결과 같은 외부 내용에 숨은 지시가 언어 모델의 행동을 바꾸는 공격이다.
related_areas: [52, 13]
tags: []
status: published
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1106, ref-1112]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 간접 프롬프트 주입

# 간접 프롬프트 주입 (Indirect Prompt Injection)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 간접 프롬프트 주입 | Indirect Prompt Injection | 없음 |

## 한 줄 정의

프롬프트 주입(Prompt Injection)의 하위 유형으로, 사용자가 직접 입력하지 않은 웹 페이지·파일·인식 결과 같은 외부 내용에 숨은 지시가 언어 모델의 행동을 바꾸는 공격이다. [추정][^ref-1106][^ref-1112]

## 설명

상위 용어: 프롬프트 주입(glossary/prompt-injection.md). OWASP LLM01:2025 는 사용자 입력이 직접 모델 행동을 바꾸는 직접 주입과 이를 구분한다. 다중 에이전트 로봇 시스템 연구는 인식 모듈을 거친 간접 주입이 로봇 행동을 오염시킬 수 있음을 보였다.

## 관련 영역

- [52. 통신 보호·위협 관리·감사](../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)
- [13. 대화형 기능의 신뢰·기반](../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)

## 출처

[^ref-1106]: OWASP GenAI Security Project, LLM01:2025 Prompt Injection, 미확인, https://genai.owasp.org/llmrisk/llm01-prompt-injection/, 접근일 2026-09-30
[^ref-1112]: Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv), When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems, 2026-08, https://arxiv.org/abs/2608.00747, 접근일 2026-09-30

- 참고문헌 페이지: [ref-1106](../references/ref-1106.md), [ref-1112](../references/ref-1112.md)
