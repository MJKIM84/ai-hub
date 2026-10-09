---
title: "추적 문맥 (Trace Context (W3C traceparent / tracestate))"
type: glossary
term_ko: 추적 문맥
term_en: Trace Context (W3C traceparent / tracestate)
definition: 분산 추적에서 요청이 여러 서비스를 거칠 때 같은 추적에 속함을 알리도록 trace-id·parent-id·플래그를 traceparent·tracestate 로 전달하는 W3C 표준 형식이다.
related_areas: [43, 38, 21]
tags: []
status: published
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1325]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 추적 문맥

# 추적 문맥 (Trace Context (W3C traceparent / tracestate))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 추적 문맥 | Trace Context (W3C traceparent / tracestate) | 없음 |

## 한 줄 정의

분산 추적에서 요청이 여러 서비스를 거칠 때 같은 추적에 속함을 알리도록 trace-id·parent-id·플래그를 traceparent·tracestate 로 전달하는 W3C 표준 형식이다. [추정][^ref-1325]

## 설명

W3C 권고안(2021-11-23)은 HTTP 에 대한 형식을 정하고, 다른 통신 프로토콜의 직렬화는 확장·외부 명세에 맡긴다.

## 관련 영역

- [43. 데이터·관측성·배포](../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)
- [38. 모니터링·이상 탐지·원인 분석](../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)
- [21. 상호운용 표준·적합성](../categories/integration/interoperability-standards-and-conformance.md)

## 출처

[^ref-1325]: W3C, Trace Context, 2021-11-23, https://www.w3.org/TR/trace-context/, 접근일 2026-10-09

- 참고문헌 페이지: [ref-1325](../references/ref-1325.md)
