---
title: "점유 격자 지도 (Occupancy Grid Map (OGM))"
type: glossary
term_ko: 점유 격자 지도
term_en: Occupancy Grid Map (OGM)
definition: 공간을 일정 크기 칸으로 나누고 칸마다 점유·빈 공간·미지 여부를 적어 로봇 위치추정과 경로계획에 쓰는 지도 표현이다.
related_areas: [6]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-081, ref-082]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 점유 격자 지도

# 점유 격자 지도 (Occupancy Grid Map (OGM))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 점유 격자 지도 | Occupancy Grid Map (OGM) | OGM — Occupancy Grid Map |

## 한 줄 정의

공간을 일정 크기 칸으로 나누고 칸마다 점유·빈 공간·미지 여부를 적어 로봇 위치추정과 경로계획에 쓰는 지도 표현이다. [추정][^ref-081][^ref-082]

## 설명

BIM(IFC) 모델에서 구조 요소만 담은 2D 점유 격자 지도를 자동 생성하는 연구가 있고, 이런 격자 지도를 포즈 그래프 지도로 바꾸는 오픈소스 도구(Ogm2Pgbm)가 있다.

## 관련 영역

- [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)

## 출처

[^ref-081]: Vega-Torres, M. A. 외, Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments, 2023-08, https://arxiv.org/abs/2308.05443, 접근일 2026-09-25 (원문 미열람)
[^ref-082]: Vega-Torres, M. A. (MigVega GitHub), Ogm2Pgbm — README (Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments), 미확인, https://github.com/MigVega/Ogm2Pgbm, 접근일 2026-09-25

- 참고문헌 페이지: [ref-081](../references/ref-081.md), [ref-082](../references/ref-082.md)
