---
title: "최적성 간격 (Optimality Gap)"
type: glossary
term_ko: 최적성 간격
term_en: Optimality Gap
definition: 어떤 해의 목적함수 값이 최적값(또는 해법기가 찾은 최선 값·하한)과 얼마나 떨어져 있는지를 비율로 나타낸 값으로, 실행 가능한 해의 품질을 재는 데 쓴다.
related_areas: [13, 14, 23, 27]
tags: []
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-592]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 최적성 간격

# 최적성 간격 (Optimality Gap)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 최적성 간격 | Optimality Gap | 없음 |

## 한 줄 정의

어떤 해의 목적함수 값이 최적값(또는 해법기가 찾은 최선 값·하한)과 얼마나 떨어져 있는지를 비율로 나타낸 값으로, 실행 가능한 해의 품질을 재는 데 쓴다. [추정][^ref-592]

## 설명

ConstraintBench 는 LLM 직접 풀이를 해법기 최적값 기준으로 실행 가능성과 최적성을 따로 채점했다(운영과학 일반 조건, 원문 미열람). 관련 용어: 혼합 정수 계획.

## 관련 영역

- [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)
- [14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)
- [23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)
- [27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 출처

[^ref-592]: ConstraintBench 저자(arXiv 2602.22465, 저자 미확인), ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization, 2026-02, https://arxiv.org/abs/2602.22465, 접근일 2026-09-25 (원문 미열람)

- 참고문헌 페이지: [ref-592](../references/ref-592.md)
