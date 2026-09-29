---
title: "프롬프트 주입 (Prompt Injection)"
type: glossary
term_ko: 프롬프트 주입
term_en: Prompt Injection
definition: 사용자 입력이나 모델이 읽는 문서·도구 설명에 숨긴 지시로 언어 모델의 행동을 의도치 않게 바꾸는 공격으로, 도구를 부르는 에이전트에서는 무단 동작으로 이어질 수 있다.
related_areas: [13, 52, 12]
tags: []
status: published
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-855, ref-856]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 프롬프트 주입

# 프롬프트 주입 (Prompt Injection)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 프롬프트 주입 | Prompt Injection | 없음 |

## 한 줄 정의

사용자 입력이나 모델이 읽는 문서·도구 설명에 숨긴 지시로 언어 모델의 행동을 의도치 않게 바꾸는 공격으로, 도구를 부르는 에이전트에서는 무단 동작으로 이어질 수 있다. [추정][^ref-855][^ref-856]

## 설명

OWASP 2025년판 LLM 응용 프로그램 Top 10 의 첫 항목(LLM01). MCP 명세는 도구 설명·주석을 신뢰 서버에서 온 것이 아니면 신뢰하지 말라고 적어 주입 경로를 좁힌다.

## 관련 영역

- [13. 대화형 기능의 신뢰·기반](../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)
- [52. 통신 보호·위협 관리·감사](../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)
- [12. 채팅으로 업무 지시·오케스트레이션](../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)

## 출처

[^ref-855]: OWASP GenAI Security Project, OWASP Top 10 for LLM Applications 2025, 2025, https://genai.owasp.org/llm-top-10/, 접근일 2026-09-29
[^ref-856]: Model Context Protocol (Anthropic 주도 오픈소스 프로젝트), Specification — Model Context Protocol (2025-06-18), 2025-06-18, https://modelcontextprotocol.io/specification/2025-06-18, 접근일 2026-09-29

- 참고문헌 페이지: [ref-855](../references/ref-855.md), [ref-856](../references/ref-856.md)
