---
title: "오픈 RMF (Open-RMF)"
type: glossary
term_ko: 오픈 RMF
term_en: Open-RMF (Open Robotics Middleware Framework)
definition: Open-RMF 주행 그래프에서 한 번에 로봇 한 대만 점유할 수 있도록 묶은 경유점·차선의 집합이다.
related_areas: [6, 9, 10, 13, 15, 16]
tags: [오픈소스, ROS 2, 다중 로봇, 설비 연동]
status: published
created: 2026-09-24
updated: 2026-09-25
sources: [ref-004, ref-286, ref-312, ref-536]
version: 6
confidence: low
---

[홈](../index.md) › [용어집](index.md) › 오픈 RMF

# 오픈 RMF (Open-RMF)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 오픈 RMF | Open-RMF | Open-RMF — Open Robotics Middleware Framework(명칭 풀이 미확인). ROS 2 — Robot Operating System 2. 플릿 어댑터 — Fleet Adapter. 통용되는 한글 명칭이 없어 "오픈 RMF"로 적는다 |

## 한 줄 정의

Open-RMF 주행 그래프에서 한 번에 로봇 한 대만 점유할 수 있도록 묶은 경유점·차선의 집합이다. [추정][^ref-536]

## 설명

rmf_traffic 그래프 정의에서 경유점과 차선이 상호 배제 그룹을 속성으로 가지며, 같은 그룹의 요소는 한 번에 로봇 한 대만 점유한다(2026-09-25 확인).

## 관련 영역

- [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — 제조사 API(Application Programming Interface)를 공통 인터페이스로 변환하는 플릿 어댑터 구조의 참조 사례다.
- [10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) — 문·승강기 같은 건물 설비를 로봇 작업과 함께 조율하는 인터페이스의 참조 사례다.
- [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) — 이종 플릿 사이의 교통 조율을 다루는 구성 요소를 참조한다.
- [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) — 작업 요청을 플릿에 배정하는 구성 요소를 참조한다.

관련 용어: [플릿 어댑터 (Fleet Adapter)](fleet-adapter.md), [다중 에이전트 경로 찾기 (MAPF)](mapf.md), [DDS 보안 규격 (DDS-Security)](dds-security.md)

## 출처


- [ref-004](../references/ref-004.md)
- [표준·프레임워크 목록](../standards/index.md)
[^ref-536]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-09-25
