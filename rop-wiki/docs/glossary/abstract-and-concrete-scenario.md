---
title: "추상 시나리오·구체 시나리오 (Abstract Scenario / Concrete Scenario)"
type: glossary
term_ko: 추상 시나리오·구체 시나리오
term_en: Abstract Scenario / Concrete Scenario
definition: 매개변수와 변형 범위만 정한 시나리오(추상)와 모든 값이 하나로 정해져 바로 실행할 수 있는 시나리오 인스턴스(구체)를 구분하는 말로, 시험 도구가 추상 시나리오를 여러 구체 시나리오로 펼쳐 실행한다.
related_areas: [33, 54]
tags: []
status: published
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1307, ref-1304]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 추상 시나리오·구체 시나리오

# 추상 시나리오·구체 시나리오 (Abstract Scenario / Concrete Scenario)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 추상 시나리오·구체 시나리오 | Abstract Scenario / Concrete Scenario | 없음 |

## 한 줄 정의

매개변수와 변형 범위만 정한 시나리오(추상)와 모든 값이 하나로 정해져 바로 실행할 수 있는 시나리오 인스턴스(구체)를 구분하는 말로, 시험 도구가 추상 시나리오를 여러 구체 시나리오로 펼쳐 실행한다. [추정][^ref-1307][^ref-1304]

## 설명

RoboVAST 는 OpenSCENARIO DSL 추상 시나리오와 변형 파일을 구체 시험 구성(scenario.config)으로 해석하고, Scenario Execution for Robotics 는 매개변수 값 목록을 조합마다 하나의 실행 시나리오로 펼친다.

## 관련 영역

- [33. 시나리오 모델·편집](../categories/design-and-simulation/scenario-model-and-editing.md)
- [54. 시험·형식 검증·벤치마크](../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)

## 출처

[^ref-1307]: Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. (arXiv, ERAS 2026 채택), Replicable Simulation-Based Robot Validation through Provenance, 2026-05-28, https://arxiv.org/abs/2605.29973, 접근일 2026-10-09
[^ref-1304]: Pasch, F., Mirus, F., Zhang, Y., & Scholl, K.-U. (Intel Labs 외, arXiv), Scenario Execution for Robotics: A generic, backend-agnostic library for running reproducible robotics experiments and tests, 2024-09-11, https://arxiv.org/abs/2409.07080, 접근일 2026-10-09

- 참고문헌 페이지: [ref-1307](../references/ref-1307.md), [ref-1304](../references/ref-1304.md)
