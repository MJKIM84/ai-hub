---
title: "다중 에이전트 경로 찾기 (MAPF)"
type: glossary
term_ko: 다중 에이전트 경로 찾기
term_en: Multi-Agent Path Finding (MAPF)
definition: 여러 에이전트(로봇)가 각자의 출발지에서 목적지까지 서로 충돌하지 않고 동시에 따라갈 수 있는 경로들을 계획하는 문제이다.
related_areas: [15, 6, 16]
tags: [경로 계획, 다중 로봇, 교통 관리]
status: draft
created: 2026-09-24
updated: 2026-09-24
sources: [ref-005, ref-006]
version: 3
---

[홈](../index.md) › [용어집](index.md) › 다중 에이전트 경로 찾기

# 다중 에이전트 경로 찾기 (MAPF)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 다중 에이전트 경로 찾기 | Multi-Agent Path Finding | MAPF — Multi-Agent Path Finding. "Multi-Agent Pathfinding"으로도 쓴다 |

## 한 줄 정의

여러 에이전트(로봇)가 각자의 출발지에서 목적지까지 서로 충돌하지 않고 동시에 따라갈 수 있는 경로들을 계획하는 문제이다. [추정][^cand-02]

## 설명

분류 원문은 15. 다중 로봇 경로·교통 관리 — MAPF를 다음과 같이 정의하고 묻는다.

여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 [분류원문]

서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [분류원문]

MAPF의 정의·변형·벤치마크를 정리한 문헌으로는 Stern 등(2019)의 논문이 검색 결과에 나타난다. [추정][^cand-02] 논문 원문은 열지 못했으므로 정의의 세부와 변형의 목록은 미확인이다.

분류 원문은 정해진 목적지까지 한 번 이동하는 문제와 지속적으로 주문이 들어오는 운영을 구분하고, 후자를 다루는 연구로 [지속형 다중 에이전트 경로 찾기](lifelong-mapf.md)와 [다중 에이전트 픽업·배송](multi-agent-pickup-and-delivery.md)을 든다.

SCM에서는 **작업이 계속 새로 들어오는 조건**이 중요하다. 정해진 목적지까지 한 번 이동하는 문제와 지속적으로 주문이 들어오는 운영은 다르다. 이를 다루는 연구가 *Lifelong MAPF*, *Multi-Agent Pickup and Delivery*이다. [5][6] [분류원문][^ref-005][^ref-006]

ROP 맥락에서는 두 가지 현실 조건이 더해진다. 실제 로봇은 크기·속도·정지 거리가 다르고 계획한 시점에 정확히 도착하지 않으며, 이종 제조사 로봇의 경로를 ROP가 직접 정할 수 있는지는 각 제조사 관제가 경로 제어를 얼마나 열어 주느냐([플릿 어댑터](fleet-adapter.md)의 범주)에 달려 있다. [추정] 따라서 원문의 질문이 묻는 양보 규칙은 알고리즘 문제인 동시에 연동·거버넌스 문제다. [추정]

## 관련 영역

- [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) — 이 용어가 명칭에 포함된 세부영역이다.
- [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) — 경로 계획의 바탕이 되는 이동 공간과 로봇별 좌표계 정렬을 다룬다.
- [16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) — 승강기·좁은 통로·대기 공간 같은 공용 자원의 예약이 경로 조율과 맞물린다.

관련 용어: [지속형 다중 에이전트 경로 찾기 (Lifelong MAPF)](lifelong-mapf.md), [다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery)](multi-agent-pickup-and-delivery.md), [플릿 어댑터 (Fleet Adapter)](fleet-adapter.md)

## 출처

[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2020, https://arxiv.org/abs/2005.07371, 접근일 2026-09-24 (원문 미열람)
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-24 (원문 미열람)
[^cand-02]: Stern, R., Sturtevant, N. R., Felner, A., Koenig, S., Ma, H., Walker, T. T., Li, J., Atzmon, D., Cohen, L., Kumar, T. K. S., Barták, R., & Boyarski, E., Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks (SoCS 2019), 2019, https://arxiv.org/abs/1906.08291, 접근일 2026-09-24 (원문 미열람)

- [ref-005](../references/ref-005.md), [ref-006](../references/ref-006.md)
- cand-02 는 검색 결과의 저자·제목·URL 로 실재만 확인한 후보 출처다. 정식 참고문헌 id 는 첫 검증 실행에서 부여하며, 그 전까지 이 출처에 기댄 주장은 [추정]으로 둔다.
- [표준·프레임워크 목록](../standards/index.md)
