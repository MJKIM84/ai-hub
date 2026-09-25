---
title: "유사 변환 (Similarity Transformation)"
type: glossary
term_ko: 유사 변환
term_en: Similarity Transformation
definition: 회전·이동·균일 축척만으로 한 좌표계의 점을 다른 좌표계로 옮기는 변환으로, 대응점 쌍에서 최소제곱으로 추정해 도면·관제 지도와 제조사 로봇 지도를 맞추는 데 쓴다.
related_areas: [6, 21, 9]
tags: []
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-153, ref-668, ref-669]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 유사 변환

# 유사 변환 (Similarity Transformation)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 유사 변환 | Similarity Transformation | 없음 |

## 한 줄 정의

회전·이동·균일 축척만으로 한 좌표계의 점을 다른 좌표계로 옮기는 변환으로, 대응점 쌍에서 최소제곱으로 추정해 도면·관제 지도와 제조사 로봇 지도를 맞추는 데 쓴다. [추정][^ref-153][^ref-668][^ref-669]

## 설명

Open-RMF 플릿 어댑터 튜토리얼은 층마다 대응 경유점(최소 4쌍 권장)으로 이 변환을 추정하고 변환 오차 추정값을 기록하게 한다. 반사 없는 유사 변환의 최소제곱 해는 Umeyama(1991)가 제시했다.

## 관련 영역

- [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)
- [21. 온보딩·설정·현장 시운전](../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)
- [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)

## 출처

[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-668]: Palonen, A. (axelpale/nudged GitHub), nudged — README (Affine transformation estimator e.g. for multi-touch gestures and calibration), 미확인, https://github.com/axelpale/nudged, 접근일 2026-09-25
[^ref-669]: Umeyama, S. (IEEE Transactions on Pattern Analysis and Machine Intelligence 13(4), 376-380), Least-Squares Estimation of Transformation Parameters Between Two Point Patterns, 1991, https://ieeexplore.ieee.org/document/88573/, 접근일 2026-09-25 (원문 미열람)

- 참고문헌 페이지: [ref-153](../references/ref-153.md), [ref-668](../references/ref-668.md), [ref-669](../references/ref-669.md)
