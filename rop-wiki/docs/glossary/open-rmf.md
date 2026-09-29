---
title: "오픈 RMF (Open-RMF)"
type: glossary
term_ko: 오픈 RMF
term_en: Open-RMF (Open Robotics Middleware Framework)
definition: 2D 평면도 이미지 위에 층·벽·꼭짓점·플릿별 차선·문·승강기를 그려 제조사 중립 빌딩 맵(.building.yaml)을 만드는 Open-RMF 의 GUI 편집 도구이다.
related_areas: [8, 15, 20, 22, 25, 27, 28]
tags: [오픈소스, ROS 2, 다중 로봇, 설비 연동]
status: published
created: 2026-09-24
updated: 2026-09-29
sources: [ref-004, ref-079, ref-286, ref-312, ref-536]
version: 7
confidence: medium
---

[홈](../index.md) › [용어집](index.md) › 오픈 RMF

# 오픈 RMF (Open-RMF)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 오픈 RMF | Open-RMF | Open-RMF — Open Robotics Middleware Framework(명칭 풀이 미확인). ROS 2 — Robot Operating System 2. 플릿 어댑터 — Fleet Adapter. 통용되는 한글 명칭이 없어 "오픈 RMF"로 적는다 |

## 한 줄 정의

2D 평면도 이미지 위에 층·벽·꼭짓점·플릿별 차선·문·승강기를 그려 제조사 중립 빌딩 맵(.building.yaml)을 만드는 Open-RMF 의 GUI 편집 도구이다. [추정][^ref-079]

## 설명

층의 축척은 실제 거리를 아는 두 점 사이에 측정선을 긋고 물리 거리를 미터로 입력해 정한다. 꼭짓점에 충전소·주차·도킹 속성을 줄 수 있고 문은 여닫이·양여닫이·미닫이·양미닫이 4종이다.

## 관련 영역

- [20. 로봇·제조사 관제 연동](../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 제조사 API(Application Programming Interface)를 공통 인터페이스로 변환하는 플릿 어댑터 구조의 참조 사례다.
- [22. 설비·건물 시스템 연동](../categories/integration/facility-and-building-system-integration.md) — 문·승강기 같은 건물 설비를 로봇 작업과 함께 조율하는 인터페이스의 참조 사례다.
- [27. 다중 로봇 경로·교통 관리 — MAPF](../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 이종 플릿 사이의 교통 조율을 다루는 구성 요소를 참조한다.
- [25. 작업 배정 — MRTA](../categories/planning-and-optimization/task-allocation-mrta.md) — 작업 요청을 플릿에 배정하는 구성 요소를 참조한다.

관련 용어: [플릿 어댑터 (Fleet Adapter)](fleet-adapter.md), [다중 에이전트 경로 찾기 (MAPF)](mapf.md), [DDS 보안 규격 (DDS-Security)](dds-security.md)

## 출처

- [ref-004](../references/ref-004.md)
- [표준·프레임워크 목록](../standards/index.md)
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-29
