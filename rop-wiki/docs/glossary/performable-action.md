---
title: "수행 가능 동작 (Performable Action (Open-RMF perform_action))"
type: glossary
term_ko: 수행 가능 동작
term_en: Performable Action (Open-RMF perform_action)
definition: Open-RMF 에서 플릿이 지원한다고 선언한 사용자 정의 동작으로, 플릿 어댑터가 수락 여부를 판단하고 실행하는 동안 관제는 로봇 제어를 넘기고 교통 협상에서 제외한다.
related_areas: [6, 20]
tags: []
status: published
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-876]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 수행 가능 동작

# 수행 가능 동작 (Performable Action (Open-RMF perform_action))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 수행 가능 동작 | Performable Action (Open-RMF perform_action) | 없음 |

## 한 줄 정의

Open-RMF 에서 플릿이 지원한다고 선언한 사용자 정의 동작으로, 플릿 어댑터가 수락 여부를 판단하고 실행하는 동안 관제는 로봇 제어를 넘기고 교통 협상에서 제외한다. [추정][^ref-876]

## 설명

플릿 설정의 action_categories 로 선언하고, add_performable_action 의 consider 콜백이 수락 여부를 정하며 set_action_executor 가 실행을 맡는다. 문 열기·승강기 사용은 사용자 정의 동작의 범위에 들어가지 않고 플랫폼이 맡는다.

## 관련 영역

- [6. 온톨로지 기반 시스템·로봇 연동](../categories/robot-ontology/ontology-based-system-and-robot-integration.md)
- [20. 로봇·제조사 관제 연동](../categories/integration/robot-and-vendor-fleet-manager-integration.md)

## 출처

[^ref-876]: Open Robotics (Programming Multiple Robots with ROS 2), User-defined Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_userdefined.html, 접근일 2026-09-29

- 참고문헌 페이지: [ref-876](../references/ref-876.md)
