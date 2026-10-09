---
title: "생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)"
type: glossary
term_ko: 생성형 AI 의미 규약
term_en: OpenTelemetry GenAI Semantic Conventions
definition: 생성형 AI 클라이언트·에이전트·도구 호출·MCP 의 스팬·지표·이벤트 이름과 속성을 정한 OpenTelemetry 규약으로, 2026-10 확인 시점에 지표는 개발(Development) 단계다.
related_areas: [43, 13]
tags: []
status: published
confidence: medium
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1239, ref-1240]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 생성형 AI 의미 규약

# 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 생성형 AI 의미 규약 | OpenTelemetry GenAI Semantic Conventions | 없음 |

## 한 줄 정의

생성형 AI 클라이언트·에이전트·도구 호출·MCP 의 스팬·지표·이벤트 이름과 속성을 정한 OpenTelemetry 규약으로, 2026-10 확인 시점에 지표는 개발(Development) 단계다. [추정][^ref-1239][^ref-1240]

## 설명

별도 저장소(semantic-conventions-genai)로 옮겨졌고, 지표 문서는 에이전트 호출 시간·추론 호출 수·도구 호출 수·도구 실행 시간 등 지표를 모두 개발 단계로 두며 토큰 지표는 별도 문서의 gen_ai.client.inference.usage.* 로 안내한다(확인일 2026-10-09). 이름이 바뀔 수 있다(oq-212).

## 관련 영역

- [43. 데이터·관측성·배포](../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)
- [13. 대화형 기능의 신뢰·기반](../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)

## 출처

[^ref-1239]: OpenTelemetry (open-telemetry/semantic-conventions-genai GitHub), semantic-conventions-genai — README, 미확인, https://github.com/open-telemetry/semantic-conventions-genai, 접근일 2026-10-09
[^ref-1240]: OpenTelemetry (open-telemetry/semantic-conventions-genai GitHub), Semantic conventions for generative AI metrics (docs/gen-ai/gen-ai-metrics.md), 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-metrics.md, 접근일 2026-10-09

- 참고문헌 페이지: [ref-1239](../references/ref-1239.md), [ref-1240](../references/ref-1240.md)
