---
title: "메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))"
type: glossary
term_ko: 메시지 큐잉 원격 측정 전송
term_en: Message Queuing Telemetry Transport (MQTT)
definition: 브로커를 거쳐 토픽 단위로 메시지를 발행·구독하는 경량 메시징 프로토콜로, VDA 5050이 관제와 이동로봇 사이 통신에 쓴다.
related_areas: [9, 11]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 메시지 큐잉 원격 측정 전송

# 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 메시지 큐잉 원격 측정 전송 | Message Queuing Telemetry Transport (MQTT) | MQTT — Message Queuing Telemetry Transport |

## 한 줄 정의

브로커를 거쳐 토픽 단위로 메시지를 발행·구독하는 경량 메시징 프로토콜로, VDA 5050이 관제와 이동로봇 사이 통신에 쓴다. [추정][^ref-031]

## 설명

VDA 5050 3.0.0은 최소 3.1.1판을 요구하고, 로봇이 연결 시 설정한 유언 메시지(last will)로 비정상 단절을 관제에 알린다.

## 관련 영역

- [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)
- [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)

## 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25

- 참고문헌 페이지: [ref-031](../references/ref-031.md)
