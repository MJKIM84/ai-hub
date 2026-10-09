---
title: "절전 모드 (Hibernation (VDA 5050 startHibernation / HIBERNATING))"
type: glossary
term_ko: 절전 모드
term_en: Hibernation (VDA 5050 startHibernation / HIBERNATING)
definition: VDA 5050 에서 로봇이 브로커 연결은 유지하되 상태 메시지 발행을 멈추고 연결 상태를 HIBERNATING 으로 알리며 활성 주문을 지운 채 정지해 있다가, stopHibernation 을 받거나 배터리가 위급할 때나 설정한 기상 시각(wakeUpTime)이 되면 스스로 벗어날 수 있는 통신 감축 상태다.
related_areas: [42, 28]
tags: []
status: published
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-031]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 절전 모드

# 절전 모드 (Hibernation (VDA 5050 startHibernation / HIBERNATING))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 절전 모드 | Hibernation (VDA 5050 startHibernation / HIBERNATING) | 없음 |

## 한 줄 정의

VDA 5050 에서 로봇이 브로커 연결은 유지하되 상태 메시지 발행을 멈추고 연결 상태를 HIBERNATING 으로 알리며 활성 주문을 지운 채 정지해 있다가, stopHibernation 을 받거나 배터리가 위급할 때나 설정한 기상 시각(wakeUpTime)이 되면 스스로 벗어날 수 있는 통신 감축 상태다. [추정][^ref-031]

## 설명

VDA 5050 3.0.0 의 startHibernation 즉시 동작으로 들어간다. 이 상태의 로봇은 stopHibernation 에만 응답한다. 42. 분산 시스템·통신·컴퓨팅 구조에서는 통신 감축 장치로, 28. 공용 자원·충전·에너지 최적화에서는 배터리 측면으로 다룬다.

## 관련 영역

- [42. 분산 시스템·통신·컴퓨팅 구조](../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)
- [28. 공용 자원·충전·에너지 최적화](../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md)

## 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09

- 참고문헌 페이지: [ref-031](../references/ref-031.md)
