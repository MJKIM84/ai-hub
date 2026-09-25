---
title: "목표 조건 (Goal Condition)"
type: glossary
term_ko: 목표 조건
term_en: Goal Condition
definition: 작업이 끝났을 때 환경이 만족해야 하는 상태 조건의 집합으로, 지시 수행 벤치마크에서 계획·실행 결과가 맞았는지를 판정하는 정답으로 쓰인다.
related_areas: [23, 27, 13]
tags: []
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-540, ref-090, ref-544]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 목표 조건

# 목표 조건 (Goal Condition)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 목표 조건 | Goal Condition | 없음 |

## 한 줄 정의

작업이 끝났을 때 환경이 만족해야 하는 상태 조건의 집합으로, 지시 수행 벤치마크에서 계획·실행 결과가 맞았는지를 판정하는 정답으로 쓰인다. [추정][^ref-540][^ref-090][^ref-544]

## 설명

ALFRED 는 작업별 PDDL 목표 조건으로 전문가 시연을 만들고, SMART-LLM 은 정답 최종 상태 조건 대비 목표 조건 재현율(GCR)로, MAT-THOR 는 작업마다 정답 목표 조건을 붙여 평가한다(논문 기준, 원문 미열람).

## 관련 영역

- [23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)
- [27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)
- [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)

## 출처

[^ref-540]: Shridhar, M. 외, ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks, 2020, https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html, 접근일 2026-09-25 (원문 미열람)
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09, https://arxiv.org/abs/2309.10062, 접근일 2026-09-25 (원문 미열람)
[^ref-544]: Zhang, X. 외(LaMMA-P 저자), LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner, 2024-09, https://arxiv.org/abs/2409.20560, 접근일 2026-09-25 (원문 미열람)

- 참고문헌 페이지: [ref-540](../references/ref-540.md), [ref-090](../references/ref-090.md), [ref-544](../references/ref-544.md)
