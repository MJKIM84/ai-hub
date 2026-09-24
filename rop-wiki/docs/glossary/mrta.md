---
title: "다중 로봇 작업 배정 (MRTA)"
type: glossary
term_ko: 다중 로봇 작업 배정
term_en: Multi-Robot Task Allocation (MRTA)
definition: 여러 로봇과 여러 작업이 있을 때 어떤 로봇(또는 로봇 팀)이 어떤 작업을 맡을지 정하는 문제이다.
related_areas: [13, 5, 14, 16]
tags: [작업 배정, 다중 로봇, 최적화]
status: draft
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 3
confidence: low
---

[홈](../index.md) › [용어집](index.md) › 다중 로봇 작업 배정

# 다중 로봇 작업 배정 (MRTA)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 다중 로봇 작업 배정 | Multi-Robot Task Allocation | MRTA — Multi-Robot Task Allocation |

## 한 줄 정의

여러 로봇과 여러 작업이 있을 때 어떤 로봇(또는 로봇 팀)이 어떤 작업을 맡을지 정하는 문제이다. [추정][^cand-01]

## 설명

분류 원문은 13. 작업 배정 — MRTA를 다음과 같이 정의하고 묻는다.

능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 [분류원문]

가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]

이 용어의 대표 문헌으로는 Gerkey와 Matarić(2004)의 논문이 검색 결과에 나타나며, MRTA 문제의 형식적 분석과 분류 체계를 제시한 것으로 소개된다. [추정][^cand-01] 논문 원문은 열지 못했으므로 분류 체계의 축과 정의는 미확인이다.

ROP 맥락에서 MRTA는 계획·최적화의 입구다. 원문 정의가 든 능력·위치·적재량·배터리·납기 가운데 능력은 5. 로봇 능력·작업 온톨로지, 위치·배터리는 8. 실시간 세계 상태·데이터 일관성, 납기는 1. 주문·업무 시스템 연계가 제공하는 입력이다. [추정] 작업이 계속 새로 들어오는 조건에서 배정과 경로 계획을 함께 다루는 문제는 [다중 에이전트 픽업·배송](multi-agent-pickup-and-delivery.md)으로 이어지고, 학습 기반 배차는 27. AI·학습·적응과 모델 운영의 방법이 이 영역에 적용되는 경우다.

## 관련 영역

- [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) — 이 용어가 명칭에 포함된 세부영역이다.
- [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) — 능력 기반 배정의 입력이 되는 공통 능력 모델을 다룬다.
- [14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) — 배정된 작업의 순서와 시간 제약을 함께 결정해야 한다.
- [16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) — 배터리·충전 시점이 배정 제약으로 들어온다.

관련 용어: [다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery)](multi-agent-pickup-and-delivery.md), [다중 에이전트 경로 찾기 (MAPF)](mapf.md)

## 출처

[^cand-01]: Gerkey, B. P. & Matarić, M. J., A Formal Analysis and Taxonomy of Task Allocation in Multi-Robot Systems (The International Journal of Robotics Research 23(9)), 2004, https://journals.sagepub.com/doi/10.1177/0278364904045564, 접근일 2026-09-24 (원문 미열람)

- cand-01 은 검색 결과의 저자·제목·URL 로 실재만 확인한 후보 출처다. 정식 참고문헌 id 는 첫 검증 실행에서 부여하며, 그 전까지 이 출처에 기댄 주장은 [추정]으로 둔다.
- [표준·프레임워크 목록](../standards/index.md)
