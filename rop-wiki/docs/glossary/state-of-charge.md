---
title: "충전 상태 (State of Charge (SOC))"
type: glossary
term_ko: 충전 상태
term_en: State of Charge (SOC)
definition: 배터리에 남은 충전량을 전체 용량 대비 비율(%)로 나타낸 값으로, VDA 5050 상태 메시지의 stateOfCharge 와 Open-RMF 배터리 갱신이 이 값을 쓴다.
related_areas: [16, 8, 9]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-051, ref-537]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 충전 상태

# 충전 상태 (State of Charge (SOC))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 충전 상태 | State of Charge (SOC) | SOC — State of Charge |

## 한 줄 정의

배터리에 남은 충전량을 전체 용량 대비 비율(%)로 나타낸 값으로, VDA 5050 상태 메시지의 stateOfCharge 와 Open-RMF 배터리 갱신이 이 값을 쓴다. [추정][^ref-051][^ref-537]

## 설명

VDA 5050 상태 메시지의 powerSupply 는 충전 상태 외에 충전 중 여부·전압·전류·건강 상태·주행 가능 거리를 담으며, 좋음·나쁨만 아는 로봇은 80%·20%로 보고한다.

## 관련 영역

- [16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)
- [8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)
- [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)

## 출처

[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-537]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 접근일 2026-09-25

- 참고문헌 페이지: [ref-051](../references/ref-051.md), [ref-537](../references/ref-537.md)
