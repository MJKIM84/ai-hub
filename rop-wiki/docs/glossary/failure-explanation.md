---
title: "실패 설명 (Failure Explanation)"
type: glossary
term_ko: 실패 설명
term_en: Failure Explanation
definition: 로봇의 실행 기록·관측을 요약해 무엇이 왜 실패했는지를 자연어로 설명하고, 그 설명을 사람의 문제 파악이나 교정 계획의 입력으로 쓰는 기법이다.
related_areas: [12, 32, 38]
tags: []
status: published
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-453]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 실패 설명

# 실패 설명 (Failure Explanation)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 실패 설명 | Failure Explanation | 없음 |

## 한 줄 정의

로봇의 실행 기록·관측을 요약해 무엇이 왜 실패했는지를 자연어로 설명하고, 그 설명을 사람의 문제 파악이나 교정 계획의 입력으로 쓰는 기법이다. [추정][^ref-453]

## 설명

REFLECT(CoRL 2023)는 다중 감각 관측에서 만든 로봇 경험의 계층적 요약을 근거로 언어 모델에 실패 원인을 묻고 그 설명으로 언어 기반 계획기가 실패를 바로잡게 하며, RoboFail 데이터셋에서 정보성 있는 실패 설명이 교정 계획을 돕는다고 보고했다.

## 관련 영역

- [12. 채팅으로 업무 지시·오케스트레이션](../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)
- [32. 예외 복구·재계획·업무 연속성](../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)
- [38. 모니터링·이상 탐지·원인 분석](../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)

## 출처

[^ref-453]: Liu, Z., Bahety, A., & Song, S. (CoRL 2023), REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction, 2023-06-27, https://arxiv.org/abs/2306.15724, 접근일 2026-09-29

- 참고문헌 페이지: [ref-453](../references/ref-453.md)
