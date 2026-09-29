---
title: "로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)"
type: glossary
term_ko: 로봇–작업 적합도 행렬
term_en: Robot–Task Fitness Matrix
definition: 로봇마다 각 하위 작업을 얼마나 잘 수행할 수 있는지를 능력 기준으로 점수화한 행렬로, 언어 모델이 추정한 값을 형식 최적화기가 배정 계산에 입력으로 쓴다.
related_areas: [12, 25, 5]
tags: []
status: published
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-242]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 로봇–작업 적합도 행렬

# 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 로봇–작업 적합도 행렬 | Robot–Task Fitness Matrix | 없음 |

## 한 줄 정의

로봇마다 각 하위 작업을 얼마나 잘 수행할 수 있는지를 능력 기준으로 점수화한 행렬로, 언어 모델이 추정한 값을 형식 최적화기가 배정 계산에 입력으로 쓴다. [추정][^ref-242]

## 설명

FLEET(2025)에서 언어 모델 전단이 소요 시간·선후 관계가 붙은 작업 그래프와 함께 만들며, 형식 최적화기가 완료 시간(makespan) 최소화 문제를 풀 때 능력 매칭 근거로 쓴다. 절제 실험에서 혼합 정수 계획은 시간 구조를, 언어 모델의 능력 매칭은 특수 능력이 필요한 작업을 각각 뒷받침했다.

## 관련 영역

- [12. 채팅으로 업무 지시·오케스트레이션](../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)
- [25. 작업 배정 — MRTA](../categories/planning-and-optimization/task-allocation-mrta.md)
- [5. 로봇 능력·작업 표현](../categories/robot-ontology/robot-capability-and-task-representation.md)

## 출처

[^ref-242]: Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D., FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams, 2025-10-08, https://arxiv.org/abs/2510.07417, 접근일 2026-09-29

- 참고문헌 페이지: [ref-242](../references/ref-242.md)
