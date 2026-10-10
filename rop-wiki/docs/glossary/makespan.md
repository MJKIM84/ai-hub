---
title: "메이크스팬 (Makespan)"
type: glossary
term_ko: 메이크스팬
term_en: Makespan
definition: 작업 집합 전체를 끝내는 데 걸린 시간으로, 일정 최적화에서는 가장 늦게 끝나는 작업(또는 로봇)의 종료 시각을 줄이는 목적으로 쓰인다.
related_areas: [26, 25, 39]
tags: []
status: published
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-379, ref-1409]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 메이크스팬

# 메이크스팬 (Makespan)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 메이크스팬 | Makespan | 없음 |

## 한 줄 정의

작업 집합 전체를 끝내는 데 걸린 시간으로, 일정 최적화에서는 가장 늦게 끝나는 작업(또는 로봇)의 종료 시각을 줄이는 목적으로 쓰인다. [추정][^ref-379][^ref-1409]

## 설명

다중 로봇 일정 연구(예: Dai 외 2025)가 최소화 목표로 쓴다. Open-RMF rmf_task 의 BinaryPriorityCostCalculator 가 더하는 작업별 (완료 시각 − 가장 이른 시작 시각)의 합과는 다른 지표다.

## 관련 영역

- [26. 작업 순서·스케줄링](../categories/planning-and-optimization/task-sequencing-and-scheduling.md)
- [25. 작업 배정 — MRTA](../categories/planning-and-optimization/task-allocation-mrta.md)
- [39. 운영 성과 측정·개선](../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)

## 출처

[^ref-379]: Google (google/or-tools GitHub), OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver), 미확인, https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md, 접근일 2026-10-10
[^ref-1409]: Dai, W., Rai, U., Chiun, J., Cao, Y., & Sartoretti, G. (IEEE Robotics and Automation Letters), Heterogeneous Multi-robot Task Allocation and Scheduling via Reinforcement Learning, 2025-01-27, https://marmotlab.org/publications/73-RAL2025-HetMRTA.pdf, 접근일 2026-10-10 (원문 미열람)

- 참고문헌 페이지: [ref-379](../references/ref-379.md), [ref-1409](../references/ref-1409.md)
