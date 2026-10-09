---
title: "작업 의존 그래프 (Task Dependency Graph (Dependency DAG))"
type: glossary
term_ko: 작업 의존 그래프
term_en: Task Dependency Graph (Dependency DAG)
definition: 하위 작업을 노드로, 먼저 끝나야 하는 선행 관계를 방향 간선으로 둔 방향 비순환 그래프로, 로봇 행동 단위인 '행동 의존 그래프(ADG)'와 달리 하위 작업 단위이며 '선후 제약'을 표현하고 실행기는 위상 순서대로 의존이 풀린 작업부터 실행한다.
related_areas: [12, 24, 26]
tags: []
status: published
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-059]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 작업 의존 그래프

# 작업 의존 그래프 (Task Dependency Graph (Dependency DAG))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 작업 의존 그래프 | Task Dependency Graph (Dependency DAG) | Dependency DAG — Task Dependency Graph |

## 한 줄 정의

하위 작업을 노드로, 먼저 끝나야 하는 선행 관계를 방향 간선으로 둔 방향 비순환 그래프로, 로봇 행동 단위인 '행동 의존 그래프(ADG)'와 달리 하위 작업 단위이며 '선후 제약'을 표현하고 실행기는 위상 순서대로 의존이 풀린 작업부터 실행한다. [추정][^ref-059]

## 설명

관련 용어: [행동 의존 그래프](action-dependency-graph.md), [선후 제약](precedence-constraint.md). DART-LLM 은 LLM 이 하위 작업 의존 DAG 를 구조화 출력으로 내고 위상 순서와 병렬로 실행한다.

## 관련 영역

- [12. 채팅으로 업무 지시·오케스트레이션](../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)
- [24. 작업·워크플로 모델링](../categories/planning-and-optimization/task-and-workflow-modeling.md)
- [26. 작업 순서·스케줄링](../categories/planning-and-optimization/task-sequencing-and-scheduling.md)

## 출처

[^ref-059]: Wang, Y. 외(DART-LLM 저자), DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models, 2024-11, https://arxiv.org/abs/2411.09022, 접근일 2026-10-09

- 참고문헌 페이지: [ref-059](../references/ref-059.md)
