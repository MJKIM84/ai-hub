---
title: "다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery)"
type: glossary
term_ko: 다중 에이전트 픽업·배송
term_en: Multi-Agent Pickup and Delivery (MAPD)
definition: 픽업 위치와 배송 위치가 있는 작업이 온라인으로 계속 들어올 때, 에이전트에 작업을 배정하고 충돌 없는 경로를 함께 계획하는 문제이다.
related_areas: [13, 15, 14]
tags: [작업 배정, 경로 계획, 픽업·배송]
status: draft
created: 2026-09-24
updated: 2026-09-24
sources: [ref-006]
version: 3
confidence: medium
---

[홈](../index.md) › [용어집](index.md) › 다중 에이전트 픽업·배송

# 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 다중 에이전트 픽업·배송 | Multi-Agent Pickup and Delivery | MAPD — Multi-Agent Pickup and Delivery |

## 한 줄 정의

픽업 위치와 배송 위치가 있는 작업이 온라인으로 계속 들어올 때, 에이전트에 작업을 배정하고 충돌 없는 경로를 함께 계획하는 문제이다. [사실][^ref-006]

## 설명

분류 원문은 D. 계획·최적화의 설명에서 이 개념을 Lifelong MAPF와 나란히 든다.

SCM에서는 **작업이 계속 새로 들어오는 조건**이 중요하다. 정해진 목적지까지 한 번 이동하는 문제와 지속적으로 주문이 들어오는 운영은 다르다. 이를 다루는 연구가 *Lifelong MAPF*, *Multi-Agent Pickup and Delivery*이다. [5][6] [분류원문][^ref-005][^ref-006]

원문 12장은 Ma 등(2017)의 논문 "Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks"를 온라인 픽업·배송 작업의 배정과 충돌 없는 이동 연구로 요약한다. [사실][^ref-006] 이 요약을 따르면 MAPD는 작업 배정(MRTA, Multi-Robot Task Allocation)과 경로 계획(MAPF, Multi-Agent Path Finding)을 결합해 다루는 문제로 읽을 수 있다. [추정][^ref-006] 논문의 문제 정의 세부와 알고리즘은 원문을 열지 못해 미확인이다.

ROP 맥락에서 MAPD는 원문 11장이 예로 든 작업(피킹한 박스를 포장대로 운반하는 일)과 바로 맞닿는다. 그 예시에서 로봇 배정과 경로는 MAPD가 다루는 부분이고, 포장대 수용능력·화물 식별·인계 확인·고장 복구는 학술 MAPD가 보통 가정하지 않는 조건이다. [추정] 따라서 ROP에서는 적재량·배터리·설비 대기·인계 확인 같은 제약을 더한 확장 문제로 보아야 한다. [추정]

## 관련 영역

- [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) — 온라인으로 들어오는 픽업·배송 작업을 로봇에 배정하는 부분이다.
- [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) — 배정된 작업의 충돌 없는 경로를 계획하는 부분이다.
- [14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) — 픽업·배송 작업의 순서와 긴급 작업 삽입이 배정·경로 결정과 맞물린다.

관련 용어: [다중 로봇 작업 배정 (MRTA)](mrta.md), [다중 에이전트 경로 찾기 (MAPF)](mapf.md), [지속형 다중 에이전트 경로 찾기 (Lifelong MAPF)](lifelong-mapf.md)

## 출처

[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2020, https://arxiv.org/abs/2005.07371, 접근일 2026-09-24 (원문 미열람)
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-24 (원문 미열람)

- [ref-005](../references/ref-005.md), [ref-006](../references/ref-006.md)
- [표준·프레임워크 목록](../standards/index.md)
