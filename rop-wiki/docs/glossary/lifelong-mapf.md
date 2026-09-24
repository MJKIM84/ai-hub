---
title: "지속형 다중 에이전트 경로 찾기 (Lifelong MAPF)"
type: glossary
term_ko: 지속형 다중 에이전트 경로 찾기
term_en: Lifelong Multi-Agent Path Finding (Lifelong MAPF)
definition: 에이전트가 목적지에 도착하면 곧바로 새 목적지를 받아 계속 이동하는 조건에서 충돌 없는 경로를 계속 계획하는 MAPF의 변형이다.
related_areas: [15, 14, 13]
tags: [경로 계획, 지속 운영, 창고]
status: draft
created: 2026-09-24
updated: 2026-09-24
sources: [ref-005, ref-006]
version: 3
---

[홈](../index.md) › [용어집](index.md) › 지속형 다중 에이전트 경로 찾기

# 지속형 다중 에이전트 경로 찾기 (Lifelong MAPF)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 지속형 다중 에이전트 경로 찾기 | Lifelong Multi-Agent Path Finding | Lifelong MAPF. MAPF는 다중 에이전트 경로 찾기(Multi-Agent Path Finding)의 약어다. 통용되는 한글 명칭이 없어 "지속형"으로 옮겼다 |

## 한 줄 정의

에이전트가 목적지에 도착하면 곧바로 새 목적지를 받아 계속 이동하는 조건에서 충돌 없는 경로를 계속 계획하는 MAPF의 변형이다. [사실][^ref-005]

## 설명

분류 원문은 D. 계획·최적화의 설명에서 이 개념을 든다.

SCM에서는 **작업이 계속 새로 들어오는 조건**이 중요하다. 정해진 목적지까지 한 번 이동하는 문제와 지속적으로 주문이 들어오는 운영은 다르다. 이를 다루는 연구가 *Lifelong MAPF*, *Multi-Agent Pickup and Delivery*이다. [5][6] [분류원문][^ref-005][^ref-006]

원문 12장은 Li 등(2020)의 논문을 지속적으로 목표가 들어오는 다중 로봇 경로 계획 연구로, Ma 등(2017)의 논문을 온라인 픽업·배송 작업의 배정과 충돌 없는 이동 연구로 요약한다. [사실][^ref-005][^ref-006] 두 논문의 방법(계획 주기, 시간 창, 알고리즘)은 원문을 열지 못해 미확인이다.

ROP 맥락에서 이 용어는 물류센터의 교통 관리가 한 번의 계획으로 끝나지 않는다는 점을 드러낸다. 주문이 계속 들어오면 경로 계획은 13. 작업 배정 — MRTA의 배정 결과와 14. 작업 순서·스케줄링의 순서 결정에 맞물려 계속 갱신되어야 하고, 로봇의 위치·상태 변화를 8. 실시간 세계 상태·데이터 일관성에서 받아야 한다. [추정] 작업에 픽업 위치와 배송 위치가 함께 있는 경우는 [다중 에이전트 픽업·배송](multi-agent-pickup-and-delivery.md)으로 다룬다.

## 관련 영역

- [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) — 지속 운영 조건의 경로·교통 조율 문제를 다룬다.
- [14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) — 계속 들어오는 작업의 순서와 긴급 작업 삽입이 경로 계획의 입력이 된다.
- [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) — 어느 로봇이 다음 목적지를 받을지가 경로 계획과 함께 결정된다.

관련 용어: [다중 에이전트 경로 찾기 (MAPF)](mapf.md), [다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery)](multi-agent-pickup-and-delivery.md)

## 출처

[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2020, https://arxiv.org/abs/2005.07371, 접근일 2026-09-24 (원문 미열람)
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-24 (원문 미열람)

- [ref-005](../references/ref-005.md), [ref-006](../references/ref-006.md)
- [표준·프레임워크 목록](../standards/index.md)
