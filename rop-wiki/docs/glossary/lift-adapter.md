---
title: "승강기 어댑터 (Lift Adapter)"
type: glossary
term_ko: 승강기 어댑터
term_en: Lift Adapter
definition: Open-RMF 에서 플릿 어댑터·핵심 시스템의 승강기 요청을 받아 적절할 때만 승강기 노드에 전달하는 감독 구성요소이다.
related_areas: [10, 12, 16]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-284]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 승강기 어댑터

# 승강기 어댑터 (Lift Adapter)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 승강기 어댑터 | Lift Adapter | 없음 |

## 한 줄 정의

Open-RMF 에서 플릿 어댑터·핵심 시스템의 승강기 요청을 받아 적절할 때만 승강기 노드에 전달하는 감독 구성요소이다. [추정][^ref-284]

## 설명

어댑터를 거치지 않고 승강기 노드에 직접 보낸 요청은 무효가 된다. 승강기 노드는 OPC 같은 프로토콜로 승강기 제어기와 통신한다.

## 관련 영역

- [10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)
- [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)
- [16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)

## 출처

[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25

- 참고문헌 페이지: [ref-284](../references/ref-284.md)
