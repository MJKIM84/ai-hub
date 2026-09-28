---
title: "지도 정합 (Map Alignment)"
type: glossary
term_ko: 지도 정합
term_en: Map Alignment
definition: 서로 다른 로봇·도면의 지도 좌표계를 대응점으로 구한 회전·축척·이동 변환으로 공통 좌표계에 맞추는 일이다.
related_areas: [15, 20, 55]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-153, ref-105, ref-079]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 지도 정합

# 지도 정합 (Map Alignment)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 지도 정합 | Map Alignment | 없음 |

## 한 줄 정의

서로 다른 로봇·도면의 지도 좌표계를 대응점으로 구한 회전·축척·이동 변환으로 공통 좌표계에 맞추는 일이다. [추정][^ref-153][^ref-105][^ref-079]

## 설명

Open-RMF 플릿 어댑터는 층별 기준 좌표 쌍으로 변환과 오차를 추정하고 대응 경유점 4개 이상을 권하며, traffic-editor 는 층 기준점 2쌍 이상으로 층 사이 변환을 구한다.

## 관련 영역

- [15. 지도·공간·위치 모델](../categories/space-and-map-model/map-space-and-location-model.md)
- [20. 로봇·제조사 관제 연동](../categories/integration/robot-and-vendor-fleet-manager-integration.md)
- [55. 현장 조사·설치·시운전](../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)

## 출처

[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25

- 참고문헌 페이지: [ref-153](../references/ref-153.md), [ref-105](../references/ref-105.md), [ref-079](../references/ref-079.md)
