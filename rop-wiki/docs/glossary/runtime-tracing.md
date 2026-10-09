---
title: "런타임 추적 (Runtime Tracing (ros2_tracing))"
type: glossary
term_ko: 런타임 추적
term_en: Runtime Tracing (ros2_tracing)
definition: 실행 중인 소프트웨어 내부의 콜백·메시지 전달 같은 실행 정보를 저부하 추적기로 기록하는 방법으로, ROS 2 에서는 LTTng 기반 ros2_tracing 이 이를 제공한다.
related_areas: [38, 43]
tags: []
status: published
confidence: medium
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1032, ref-447]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 런타임 추적

# 런타임 추적 (Runtime Tracing (ros2_tracing))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 런타임 추적 | Runtime Tracing (ros2_tracing) | 없음 |

## 한 줄 정의

실행 중인 소프트웨어 내부의 콜백·메시지 전달 같은 실행 정보를 저부하 추적기로 기록하는 방법으로, ROS 2 에서는 LTTng 기반 ros2_tracing 이 이를 제공한다. [추정][^ref-1032][^ref-447]

## 설명

기존 용어 '분산 추적'이 플랫폼 서비스 사이의 요청 흐름(OpenTelemetry 등)을 다루는 것과 달리, 런타임 추적은 ROS 2 런타임 내부라는 다른 계층의 실행 정보를 모은다. 두 계층을 작업 식별자로 잇는 공개 사례는 미확인이다.

## 관련 영역

- [38. 모니터링·이상 탐지·원인 분석](../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)
- [43. 데이터·관측성·배포](../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)

## 출처

[^ref-1032]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L 7(3), arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-10-09
[^ref-447]: OpenTelemetry (CNCF), OpenTelemetry Specification — Overview, 미확인, https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md, 접근일 2026-10-09

- 참고문헌 페이지: [ref-1032](../references/ref-1032.md), [ref-447](../references/ref-447.md)
