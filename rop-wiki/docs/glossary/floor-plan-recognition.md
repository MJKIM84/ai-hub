---
title: "평면도 인식 (Floor Plan Recognition)"
type: glossary
term_ko: 평면도 인식
term_en: Floor Plan Recognition
definition: 평면도 이미지나 CAD 도면에서 벽·문·창문·계단 같은 건축 요소와 방 영역·유형을 자동으로 찾아내 구조화하는 작업이다.
related_areas: [6, 27]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-062, ref-064, ref-066, ref-070]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 평면도 인식

# 평면도 인식 (Floor Plan Recognition)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 평면도 인식 | Floor Plan Recognition | 없음 |

## 한 줄 정의

평면도 이미지나 CAD 도면에서 벽·문·창문·계단 같은 건축 요소와 방 영역·유형을 자동으로 찾아내 구조화하는 작업이다. [추정][^ref-062][^ref-064][^ref-066][^ref-070]

## 설명

래스터 이미지 데이터셋(CubiCasa5K, R2V 등), 벡터 CAD 데이터셋(FloorPlanCAD, ArchCAD-400K), 그래프 출력형 데이터셋(Raster-to-Graph, ResPlan)이 공개되어 있다. 도면 해석은 27. AI·학습·적응과 모델 운영의 방법이 6. 지도·공간·위치 모델에 적용되는 경우다.

## 관련 영역

- [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)
- [27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 출처

[^ref-062]: CubiCasa (Kalervo, A. 외), CubiCasa5k — README (CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis), 미확인, https://github.com/CubiCasa/CubiCasa5k, 접근일 2026-09-25
[^ref-064]: Zeng, Z., Li, X., Yu, Y. K., & Fu, C.-W., DeepFloorplan — README (Deep Floor Plan Recognition using a Multi-task Network with Room-boundary-Guided Attention), 2019, https://github.com/zlzeng/DeepFloorplan, 접근일 2026-09-25
[^ref-066]: FloorPlanCAD 프로젝트(Fan, Z. 외), FloorPlanCAD Dataset — project page (floorplancad.github.io index.md), 2021, https://floorplancad.github.io/, 접근일 2026-09-25
[^ref-070]: Hu, S. 외, Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer), 2024, https://github.com/SizheHu/Raster-to-Graph, 접근일 2026-09-25

- 참고문헌 페이지: [ref-062](../references/ref-062.md), [ref-064](../references/ref-064.md), [ref-066](../references/ref-066.md), [ref-070](../references/ref-070.md)
