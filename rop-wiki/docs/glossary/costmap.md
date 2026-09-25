---
title: "비용 지도 (Costmap)"
type: glossary
term_ko: 비용 지도
term_en: Costmap
definition: 로봇 경로 계획을 위해 점유 격자 지도 위에 장애물, 로봇 외형에 따른 여유(인플레이션), 필터 마스크로 적용한 금지 구역·속도 제한 같은 비용을 칸마다 매긴 격자 지도다.
related_areas: [6, 15]
tags: []
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-644]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 비용 지도

# 비용 지도 (Costmap)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 비용 지도 | Costmap | 없음 |

## 한 줄 정의

로봇 경로 계획을 위해 점유 격자 지도 위에 장애물, 로봇 외형에 따른 여유(인플레이션), 필터 마스크로 적용한 금지 구역·속도 제한 같은 비용을 칸마다 매긴 격자 지도다. [추정][^ref-644]

## 설명

Nav2 의 costmap_2d 패키지가 대표 구현이다. 점유 격자 지도가 칸의 점유 여부를 나타낸다면 비용 지도는 그 위에 통과 비용을 매긴다. 비용 지도 생성과 인플레이션은 로봇 쪽 내비게이션 스택 기능이며 ROP 에서는 연계 대상이다.

## 관련 영역

- [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)
- [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)

## 출처

[^ref-644]: ROS Navigation (ros-navigation/navigation2 GitHub), nav2_costmap_2d — README, 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_costmap_2d/README.md, 접근일 2026-09-25

- 참고문헌 페이지: [ref-644](../references/ref-644.md)
