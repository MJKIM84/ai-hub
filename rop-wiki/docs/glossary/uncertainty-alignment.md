---
title: "불확실도 정렬 (Uncertainty Alignment)"
type: glossary
term_ko: 불확실도 정렬
term_en: Uncertainty Alignment
definition: 언어 모델 계획기가 자신의 불확실도를 통계적으로 보정해 확신이 없을 때만 사람에게 되묻도록 맞추는 것이다.
related_areas: [9, 13, 44]
tags: []
status: published
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-351]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 불확실도 정렬

# 불확실도 정렬 (Uncertainty Alignment)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 불확실도 정렬 | Uncertainty Alignment | 없음 |

## 한 줄 정의

언어 모델 계획기가 자신의 불확실도를 통계적으로 보정해 확신이 없을 때만 사람에게 되묻도록 맞추는 것이다. [추정][^ref-351]

## 설명

KnowNo(Ren 외, CoRL 2023)는 [등각 예측](conformal-prediction.md)으로 후보 행동의 예측 집합을 만들고, 집합이 하나로 좁혀지면 자율 실행하고 여러 개가 남으면 사람에게 되묻는다. 등각 예측의 정의는 기존 용어집 항목 등각 예측을 따르며 여기서 다시 정의하지 않는다.

## 관련 영역

- [9. 채팅으로 시나리오 구성](../categories/chat-based-configuration-and-operation/chat-scenario-composition.md)
- [13. 대화형 기능의 신뢰·기반](../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)
- [44. 로봇 기반 모델·언어 모델 계획](../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md)

## 출처

[^ref-351]: Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023), Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-09-04, https://arxiv.org/abs/2307.01928, 접근일 2026-09-29

- 참고문헌 페이지: [ref-351](../references/ref-351.md)
