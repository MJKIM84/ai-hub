---
title: "MQTT 서비스 품질 수준 (MQTT Quality of Service (QoS) Level)"
type: glossary
term_ko: MQTT 서비스 품질 수준
term_en: MQTT Quality of Service (QoS) Level
definition: MQTT 에서 메시지 전달 보장 수준을 고르는 설정으로, VDA 5050 3.0.0 은 대부분 주제에 최선 노력(QoS 0)을, 연결 상태 주제에 최소 한 번(QoS 1)을 쓴다.
related_areas: [41, 20, 42, 29]
tags: []
status: published
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-031]
version: 1
---

[홈](../index.md) › [용어집](index.md) › MQTT 서비스 품질 수준

# MQTT 서비스 품질 수준 (MQTT Quality of Service (QoS) Level)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| MQTT 서비스 품질 수준 | MQTT Quality of Service (QoS) Level | 없음 |

## 한 줄 정의

MQTT 에서 메시지 전달 보장 수준을 고르는 설정으로, VDA 5050 3.0.0 은 대부분 주제에 최선 노력(QoS 0)을, 연결 상태 주제에 최소 한 번(QoS 1)을 쓴다. [추정][^ref-031]

## 설명

VDA 5050 3.0.0 은 통신 부하를 줄이려고 order·state 등 주제에 QoS 0 을, connection 주제에 QoS 1 을 쓴다. 이번 출처는 QoS 0·1 만 다루며 그 밖의 수준은 이 항목에서 다루지 않는다.

## 관련 영역

- [41. 플랫폼 아키텍처·외부 API](../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md)
- [20. 로봇·제조사 관제 연동](../categories/integration/robot-and-vendor-fleet-manager-integration.md)
- [42. 분산 시스템·통신·컴퓨팅 구조](../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)
- [29. 명령·작업 실행의 신뢰성](../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md)

## 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09

- 참고문헌 페이지: [ref-031](../references/ref-031.md)
