---
title: "파놉틱 품질 (Panoptic Quality (PQ))"
type: glossary
term_ko: 파놉틱 품질
term_en: Panoptic Quality (PQ)
definition: 매칭된 인스턴스의 평균 IoU(분할 품질)와 TP/(TP+0.5FP+0.5FN)(인식 품질)의 곱으로, 요소를 맞게 찾았는지와 모양을 정확히 잡았는지를 함께 재는 지표다.
related_areas: [27, 6]
tags: []
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-067]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 파놉틱 품질

# 파놉틱 품질 (Panoptic Quality (PQ))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 파놉틱 품질 | Panoptic Quality (PQ) | PQ — Panoptic Quality |

## 한 줄 정의

매칭된 인스턴스의 평균 IoU(분할 품질)와 TP/(TP+0.5FP+0.5FN)(인식 품질)의 곱으로, 요소를 맞게 찾았는지와 모양을 정확히 잡았는지를 함께 재는 지표다. [추정][^ref-067]

## 설명

FloorPlanCAD 계열의 파놉틱 심볼 스포팅은 의미 라벨이 같고 IoU 가 0.5 를 넘으면 예측 심볼을 정답과 매칭한다.

## 관련 영역

- [27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)
- [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)

## 출처

[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P., FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-05, https://arxiv.org/abs/2105.07147, 접근일 2026-09-25 (원문 미열람)

- 참고문헌 페이지: [ref-067](../references/ref-067.md)
