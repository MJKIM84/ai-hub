---
title: "클릭 수 지표 (Number of Clicks (NoC))"
type: glossary
term_ko: 클릭 수 지표
term_en: Number of Clicks (NoC)
definition: '대화형 주석·분할에서 목표 정확도(예: IoU 90%)에 이르거나 예측을 고치는 데 필요한 평균 사용자 클릭 수로, 사람 노력을 재는 지표다.'
related_areas: [23, 27]
tags: []
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-792, ref-795]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 클릭 수 지표

# 클릭 수 지표 (Number of Clicks (NoC))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 클릭 수 지표 | Number of Clicks (NoC) | NoC — Number of Clicks |

## 한 줄 정의

대화형 주석·분할에서 목표 정확도(예: IoU 90%)에 이르거나 예측을 고치는 데 필요한 평균 사용자 클릭 수로, 사람 노력을 재는 지표다. [추정][^ref-792][^ref-795]

## 설명

NoC@90 처럼 목표 IoU 를 붙여 쓰며 보통 최대 클릭 수(예: 20회)를 상한으로 둔다. Polygon-RNN 계열은 임계값을 넘는 꼭짓점을 고치는 가상 주석자의 수정 횟수로 잰다.

## 관련 영역

- [23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)
- [27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 출처

[^ref-792]: Forte, M., Price, B., Cohen, S., Xu, N., & Pitié, F. (arXiv 2003.07932), Getting to 99% Accuracy in Interactive Segmentation, 2020-03, https://arxiv.org/abs/2003.07932, 접근일 2026-09-25 (원문 미열람)
[^ref-795]: Acuna, D., Ling, H., Kar, A., & Fidler, S. (CVPR 2018), Efficient Interactive Annotation of Segmentation Datasets with Polygon-RNN++, 2018-03, https://arxiv.org/abs/1803.09693, 접근일 2026-09-25 (원문 미열람)

- 참고문헌 페이지: [ref-792](../references/ref-792.md), [ref-795](../references/ref-795.md)
