---
title: "오픈 RMF (Open-RMF)"
type: glossary
term_ko: 오픈 RMF
term_en: Open-RMF (Open Robotics Middleware Framework)
definition: ROS 2 기반의 다중 로봇 조율 프레임워크로, 제조사별 플릿 어댑터와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결하고 작업·교통을 조율한다.
related_areas: [9, 10, 15, 13]
tags: [오픈소스, ROS 2, 다중 로봇, 설비 연동]
status: draft
created: 2026-09-24
updated: 2026-09-24
sources: [ref-004]
version: 3
confidence: medium
---

[홈](../index.md) › [용어집](index.md) › 오픈 RMF

# 오픈 RMF (Open-RMF)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 오픈 RMF | Open-RMF | Open-RMF — Open Robotics Middleware Framework(명칭 풀이 미확인). ROS 2 — Robot Operating System 2. 플릿 어댑터 — Fleet Adapter. 통용되는 한글 명칭이 없어 "오픈 RMF"로 적는다 |

## 한 줄 정의

ROS 2 기반의 다중 로봇 조율 프레임워크로, 제조사별 플릿 어댑터와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결하고 작업·교통을 조율한다. [사실][^ref-004]

## 설명

분류 원문은 C. 연결·실행 기반을 설명하며 Open-RMF를 로봇 연결과 시설 연결을 함께 보는 사례로 인용한다.

Open-RMF도 제조사별 Fleet Adapter와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결한다. **로봇 연결과 시설 연결을 함께 보는 것**이 필요하다. [4] [분류원문][^ref-004]

원문 12장은 Open Robotics의 문서 "Programming Multiple Robots with ROS 2"의 RMF Core 개요를 작업·교통 조율, Fleet Adapter, 설비 연동 구조의 참고 자료로 든다. [사실][^ref-004] 문서의 기준 버전과 갱신일, 지원 로봇 범위, 조율 성능, 대규모 물류센터 적용 사례는 이번 구축에서 확인하지 않았다(미확인). 따라서 이 위키는 Open-RMF의 성능에 관한 주장을 싣지 않는다.

ROP 맥락에서 Open-RMF는 9. 로봇·제조사 관제 연동, 10. 설비·건물 시스템 연동, 15. 다중 로봇 경로·교통 관리 — MAPF가 한 구조 안에서 어떻게 맞물리는지 보여 주는 참조 구현이다. [추정] 로봇 쪽 연결을 맡는 부품은 [플릿 어댑터](fleet-adapter.md)에서 따로 다룬다. ROP가 Open-RMF를 구성 요소로 채택할지 구조만 참고할지는 제품 전략의 문제이며 이 위키에서는 정하지 않는다.

## 관련 영역

- [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — 제조사 API(Application Programming Interface)를 공통 인터페이스로 변환하는 플릿 어댑터 구조의 참조 사례다.
- [10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) — 문·승강기 같은 건물 설비를 로봇 작업과 함께 조율하는 인터페이스의 참조 사례다.
- [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) — 이종 플릿 사이의 교통 조율을 다루는 구성 요소를 참조한다.
- [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) — 작업 요청을 플릿에 배정하는 구성 요소를 참조한다.

관련 용어: [플릿 어댑터 (Fleet Adapter)](fleet-adapter.md), [다중 에이전트 경로 찾기 (MAPF)](mapf.md), [DDS 보안 규격 (DDS-Security)](dds-security.md)

## 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-24 (원문 미열람)

- [ref-004](../references/ref-004.md)
- [표준·프레임워크 목록](../standards/index.md)
