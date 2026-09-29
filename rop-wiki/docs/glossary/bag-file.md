---
title: "백 파일 (Bag File (rosbag2))"
type: glossary
term_ko: 백 파일
term_en: Bag File (rosbag2)
definition: ROS 2 에서 토픽 메시지를 시각과 함께 저장한 기록 파일로, 나중에 재생해 로봇 소프트웨어를 실제 하드웨어 없이 시험·디버깅하는 데 쓴다.
related_areas: [11, 36, 43]
tags: []
status: published
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-831]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 백 파일

# 백 파일 (Bag File (rosbag2))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 백 파일 | Bag File (rosbag2) | rosbag2 — Bag File |

## 한 줄 정의

ROS 2 에서 토픽 메시지를 시각과 함께 저장한 기록 파일로, 나중에 재생해 로봇 소프트웨어를 실제 하드웨어 없이 시험·디버깅하는 데 쓴다. [추정][^ref-831]

## 설명

rosbag2 는 ros2 bag record 로 기록하고 ros2 bag play 로 재생 속도·시작 시점·토픽 선택·반복·/clock 발행 옵션을 두어 재생하며 MCAP·SQLite3 저장 형식을 지원한다. 로봇 한 대의 통신 기록을 재생하는 로봇 자체 지능·제어 쪽 도구이며, 플릿 수준 실제 상황 재현과는 층이 다르다.

## 관련 영역

- [11. 채팅으로 실제 상황 시뮬레이션 재현](../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md)
- [36. 가상 시운전·실제 상황 재현](../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md)
- [43. 데이터·관측성·배포](../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)

## 출처

[^ref-831]: ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications), 미확인, https://github.com/ros2/rosbag2, 접근일 2026-09-29

- 참고문헌 페이지: [ref-831](../references/ref-831.md)
