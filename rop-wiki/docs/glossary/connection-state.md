---
title: "연결 상태 (Connection State (VDA 5050 connectionState))"
type: glossary
term_ko: 연결 상태
term_en: Connection State (VDA 5050 connectionState)
definition: VDA 5050 에서 로봇과 메시지 브로커 사이 연결을 ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 가운데 하나로 알리는 값이며, 예기치 않은 끊김은 유언 메시지로 전달된다.
related_areas: [38, 20]
tags: []
status: published
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-449]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 연결 상태

# 연결 상태 (Connection State (VDA 5050 connectionState))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 연결 상태 | Connection State (VDA 5050 connectionState) | VDA 5050 connectionState — Connection State |

## 한 줄 정의

VDA 5050 에서 로봇과 메시지 브로커 사이 연결을 ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 가운데 하나로 알리는 값이며, 예기치 않은 끊김은 유언 메시지로 전달된다. [추정][^ref-449]

## 설명

질서 있는 종료 때는 OFFLINE, 예기치 않은 끊김은 브로커가 유언 메시지로 CONNECTION_BROKEN 을 알리고, HIBERNATING 은 연결은 살아 있으나 상태 메시지를 보내지 않는 절전·통신 감축 모드다.

## 관련 영역

- [38. 모니터링·이상 탐지·원인 분석](../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)
- [20. 로봇·제조사 관제 연동](../categories/integration/robot-and-vendor-fleet-manager-integration.md)

## 출처

[^ref-449]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/connection.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema, 접근일 2026-10-09

- 참고문헌 페이지: [ref-449](../references/ref-449.md)
