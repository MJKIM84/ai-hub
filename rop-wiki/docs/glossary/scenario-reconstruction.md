---
title: "시나리오 재구성 (Scenario Reconstruction)"
type: glossary
term_ko: 시나리오 재구성
term_en: Scenario Reconstruction
definition: 사고 보고서·운영 기록 같은 실제 상황의 기록에서 정보를 추출해 시뮬레이터에서 다시 실행할 수 있는 시나리오로 만드는 일이다.
related_areas: [11, 33, 36]
tags: []
status: published
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-834, ref-835]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 시나리오 재구성

# 시나리오 재구성 (Scenario Reconstruction)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 시나리오 재구성 | Scenario Reconstruction | 없음 |

## 한 줄 정의

사고 보고서·운영 기록 같은 실제 상황의 기록에서 정보를 추출해 시뮬레이터에서 다시 실행할 수 있는 시나리오로 만드는 일이다. [추정][^ref-834][^ref-835]

## 설명

SoVAR(ASE 2024)와 OmniTester(2024)가 언어 모델로 사고 보고서 텍스트에서 시나리오를 재구성해 자율주행 시험 시뮬레이터에서 재현했다. 정보 추출 정확도와 지도 대응의 한계가 보고되어, 11. 채팅으로 실제 상황 시뮬레이션 재현에서는 사람 확인과 실제 기록 우선 입력이 필요한 것으로 본다.

## 관련 영역

- [11. 채팅으로 실제 상황 시뮬레이션 재현](../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md)
- [33. 시나리오 모델·편집](../categories/design-and-simulation/scenario-model-and-editing.md)
- [36. 가상 시운전·실제 상황 재현](../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md)

## 출처

[^ref-834]: Guo, A., Zhou, Y., Tian, H. 외 (ASE 2024), SoVAR: Building Generalizable Scenarios from Accident Reports for Autonomous Driving Testing, 2024-09-12, https://arxiv.org/abs/2409.08081, 접근일 2026-09-29
[^ref-835]: Lu, Q., Wang, X., Jiang, Y., Zhao, G., Ma, M., & Feng, S., Multimodal Large Language Model Driven Scenario Testing for Autonomous Vehicles, 2024-09-10, https://arxiv.org/abs/2409.06450, 접근일 2026-09-29

- 참고문헌 페이지: [ref-834](../references/ref-834.md), [ref-835](../references/ref-835.md)
