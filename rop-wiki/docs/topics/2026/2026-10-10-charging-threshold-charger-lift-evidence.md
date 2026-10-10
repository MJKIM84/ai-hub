---
title: "충전 하한과 충전소 지정, 승강기 세션 점유는 무엇이 확인됐는가"
type: topic
category: "G. 계획·최적화"
primary_area_no: 28
related_areas: [5, 15, 22, 27, 57]
tags: [충전 하한, is_charger, 승강기 세션, 공용 충전기, 배터리 열화, Open-RMF]
status: published
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-031, ref-039, ref-105, ref-286, ref-312, ref-403, ref-536, ref-1410, ref-1411, ref-1398]
last_run: 2026-10-10
version: 1
---

[홈](../../index.md) › [주제](../index.md) › 충전 하한과 충전소 지정, 승강기 세션 점유는 무엇이 확인됐는가

# 충전 하한과 충전소 지정, 승강기 세션 점유는 무엇이 확인됐는가

**주 연구영역:** [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) · **관련 영역:** [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) · **실행:** 2026-10-10-05

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 1 · 마지막 갱신: 2026-10-10 · 마지막 실행: 2026-10-10
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- VDA 5050 팩트시트의 충전 수준은 백분율 선언값이고 Open-RMF 설정의 recharge_threshold 는 0~1 비율의 운행 하한이며, 현재 Open-RMF 구현은 충전소 경유점을 is_charger 로 지정한다. [사실][^ref-031][^ref-105][^ref-1410]
- 이 위키는 ROP 가 운행 하한·충전 시작 판단·충전 목표를 제조사 선언과 별도의 운영 정책 항목으로 기록하고, 충전소 지정은 구현 기준(is_charger)으로 확인하며, Open-RMF 기능의 적용 판을 함께 남기는 편이 좋다고 본다. [의견][^ref-031][^ref-105][^ref-1410][^ref-1398]
- 두 충전 값의 우선순위 규칙은 확인한 원문 범위에서 찾지 못했고, 여러 플릿의 승강기 배분 규칙과 공용 충전기 열화 최적화의 현장 검증도 아직 확인되지 않았다. [추정][^ref-031][^ref-105][^ref-403]

## 2. 배경

로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]

이 글은 [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md)의 위 핵심 질문 아래 남아 있던 열린 질문 oq-066·oq-067·oq-068·oq-069 와, 세부영역 페이지의 두 문장(충전 하한 아래 주문 제한을 의무로 적은 문장, 충전소 속성을 두고 문서가 어긋난다고 적은 문장)을 갱신 실행 2026-10-10-05 에서 다시 확인한 결과다. 조사는 외부 조사 메모를 공식 저장소·논문 원문과 대조한 것이며 한국 자료는 포함되지 않았다.

## 3. 본문

### 충전 하한: 제조사 선언값과 운영 설정

VDA 5050 3.0.0 판(발행일 미확인)의 팩트시트 batteryCharging 객체는 임계 충전 수준(criticalLowChargingLevel)·최대 희망 충전 수준·최소 희망 충전 수준을 백분율로, 최소 충전 시간을 초로 선언하는 네 필드로 이루어진다. [사실][^ref-031] 명세는 임계 충전 수준 이하에서 관제가 충전소로 가는 주문만 보내는 것을 의무가 아닌 권고 표현으로 적는다. [사실][^ref-031] 이 위키는 이 값을 의무 문구나 모든 로봇에 공통인 충전 시작 비율로 옮기지 않고, 제조사가 로봇별로 선언하는 값으로 다뤄야 한다고 본다. [의견][^ref-031]

Open-RMF fleet_adapter_template 의 설정 예시는 recharge_threshold 0.10 을 그 아래로는 로봇이 운행하지 않는 수준으로, recharge_soc 1.0 을 충전 작업에서 채울 목표 수준으로 두며, 두 값은 권장값이 아닌 템플릿 예시값이다. [사실][^ref-105] 이 위키는 두 체계를 대조할 때 단위를 먼저 맞추고, 관제의 주문 제한 기준인 VDA 의 임계 수준과 운행 하한인 Open-RMF 값을 구분해 운행 하한·충전 시작 판단·충전 목표를 별도 정책 항목으로 기록하는 편이 좋다고 본다. [의견][^ref-031][^ref-105] 두 값 가운데 무엇을 자동으로 우선하는지에 관한 공통 조정 규칙은 확인한 두 원문에 없었으며, Open-RMF 의 다른 구성요소와 VDA 5050 의 다른 절은 조사하지 않았다. [추정][^ref-031][^ref-105]

### 충전소 경유점 지정: 문서와 구현

Open-RMF 지원 작업 문서는 충전소를 is_parking_spot 으로 설정한다고 적지만, 현재 구현의 그래프 API 와 rmf_fleet_adapter 2.14.0 파서는 주차 지점과 충전 지점을 별도 속성으로 두고 충전소를 is_charger 로 지정한다. [사실][^ref-039][^ref-536][^ref-1410] 그래프 API 는 충전 지점을 배터리 충전 수준이 임계값 아래로 떨어진 로봇이 보내지는 곳으로, 주차 지점을 비상 경보 때 로봇이 스스로 주차하는 곳으로 설명한다. [사실][^ref-536] 두 구현 자료는 같은 프로젝트의 것이라 독립 교차 확인은 아니다. 이 위키는 구현 기준으로 충전소 지정을 is_charger 로 보며, is_parking_spot 만 지정한 경유점을 충전소와 같은 뜻으로 취급하지 않는 것이 맞다고 본다. [의견][^ref-536][^ref-1410]

### 승강기 세션 메시지의 범위

Open-RMF 의 승강기 요청 메시지는 승강기 이름·요청 시각·세션 id·요청 유형(세션 종료·AGV 모드·사람 모드)·목적층·문 상태 필드로 이루어지고, 상태 메시지는 세션 종료 요청 때까지 제어권을 받은 세션 id 를 보고한다. [사실][^ref-312][^ref-286] 두 메시지에는 최대 점유 시간, 예약 시간창, 여러 요청의 목적층 묶음을 지정하는 필드가 없다. [사실][^ref-312][^ref-286] 이 위키는 세션 점유·종료 인터페이스가 공개돼 있다는 사실과 공정한 대기열·묶음 운행 같은 배분 정책이 정의돼 있다는 주장을 구별해야 한다고 보며, 메시지 정의만 본 결론이므로 승강기 감독 등 다른 구성요소에 타임아웃이나 대기열 구현이 없다는 뜻으로 넓히지 않는다. [의견][^ref-312][^ref-286]

### Open-RMF 충전·뮤텍스 기능의 판 기록

rmf_fleet_adapter 변경 이력에는 2.12.0(2026-02-23)에 충전 대기 단계 완료 발행과 다음 작업에 충전량이 모자라면 충전기로 복귀하는 변경이, 2.13.0(2026-06-15)에 뮤텍스 잠금·해제 실행에서 생길 수 있는 교착 수정이 기록돼 있다(최신 판 2.14.0 은 2026-09-26). [사실][^ref-1398] 이 위키는 충전 작업 삽입·뮤텍스 그룹을 인용할 때 적용 판과 이 수정의 포함 여부를 함께 적고, 이전 판이 모든 조건에서 교착 없이 동작했다는 근거로 쓰지 않아야 한다고 본다. 변경 이력은 수정이 있었다는 것만 보여 줄 뿐 이전 판 결함의 범위를 정량화하지 않는다. [의견][^ref-1398]

### 공용 충전기와 배터리 열화를 함께 푸는 연구

Li 외(2026-03-24, arXiv v1 프리프린트, 동료심사 미확인)는 작업 배정·서비스 순서·선택적 충전 결정·충전 방식 선택·공용 충전기 접근을 하나의 혼합 정수 계획(Mixed Integer Linear Programming, MILP)으로 함께 표현하고, 총 배터리 열화·충전기 대기·납기 지연·로봇 사이 열화 불균형을 함께 줄이는 목적함수를 둔다. [사실][^ref-403] 공용 충전기 제약은 같은 충전기의 서로 다른 충전 세션 쌍마다 순서 변수를 두어 충전 구간이 겹치지 않게 하며, 세션 집합이 모든 로봇의 세션을 포함하도록 정의돼 있어 같은 로봇의 세션 쌍도 여기에 든다(논문이 따로 명시한 문장은 아니다). [사실][^ref-403] 결과 수치는 4절 사례에 적는다.

### 물류 작업과 에너지 공급을 함께 계획하는 후보 자료

Yang 외(2026-07-27, Processes)는 냉동 컨테이너 온도 제약 아래 항만 무인운반차(Automated Guided Vehicle, AGV)의 작업 스케줄링·충전을 태양광·풍력·에너지 저장 장치(Energy Storage System, ESS)를 갖춘 항만 마이크로그리드 운영과 결합해 운영비를 최소화하는 2단계 프레임워크를 제시한 것으로 초록에 소개된다(원문 미열람). [추정][^ref-1411] 이 위키는 이 자료를 물류 작업과 에너지 공급을 함께 계획하는 충전 연구의 후보로만 두며, 원문을 열지 못했으므로 비용 절감 수치나 국내 물류센터 적용 근거로 쓰지 않는다. [의견][^ref-1411]

## 4. 현장 시나리오

**현장 유형:** 물류창고

**사례:** 가상 창고에서 로봇 4대가 공용 충전기 2대를 나눠 쓰며 작업 40건을 처리(수치 실험이며 실제 배치 아님)

다음은 Li 외(2026, 프리프린트)의 대표 수치 실험을 여섯 항목으로 옮긴 것이며, 실제 현장 사례가 아니다.

| 항목 | 내용 |
|---|---|
| 시작 조건 | 작업 40건의 배정·서비스 순서와 선택적 충전 결정을 함께 정하는 계획 문제가 주어진다. [사실][^ref-403] |
| 작업 대상 | 100×50 m 가상 창고의 작업 40건과 공용 충전기 2대다. [사실][^ref-403] |
| 수행 자원 | 동종 로봇 4대가 표준·고속 두 충전 방식 가운데 하나를 골라 충전한다. [사실][^ref-403] |
| 제약 | 같은 충전기에서 충전 세션이 서로 겹치지 않아야 한다. [사실][^ref-403] |
| 완료·인계 | 미확인 |
| 예외·성과 | 기여 요약의 규칙 기반 대비 최대 54% 열화 감소는 대표 사례 하나(로봇 4·작업 40·충전기 2)의 예시적 기대 평균(총 열화 0.214→0.098)으로 보고된 값이다. [사실][^ref-403] 실패 시 누가 복구하는지는 미확인이다. |

이 사례에서 이 영역이 관여하는 곳은 제약(공용 충전기 비중첩)과 예외·성과(열화·충전기 대기)다. 이 위키는 열화를 축약 대리 모형으로 표현한 이 예시값을 현장 배터리 수명 개선의 검증값으로 인용하지 않는다. [의견][^ref-403]

## 5. ROP 관점의 시사점

**직접 범위:**

- 이 위키는 ROP 가 제조사 선언(임계 충전 수준)과 자체 운영 설정(운행 하한·충전 목표)을 단위를 맞춰 따로 기록하고, 충전소 지정은 구현 기준(is_charger)으로 확인하는 편이 좋다고 본다. [의견][^ref-031][^ref-105][^ref-1410]
- 승강기 세션 순서·점유 한도 같은 배분 규칙은 메시지 정의에 없으므로, 이 위키는 그 규칙을 어디서 정할지가 확인할 과제로 남는다고 본다. [의견][^ref-312][^ref-286]

**연계 범위:**

- 승강기 운행과 설비 안전 제어는 분류 원문 19장의 시설·설비 제어 경계에 속하는 연계 대상이며, 이 위키는 ROP 가 세션 요청과 상태 확인까지만 맡는다고 본다. [의견][^ref-312]
- 이 위키는 항만 마이크로그리드(태양광·풍력·ESS) 운영을 ROP 직접 범위가 아닌 에너지 설비 쪽 연계 대상으로 본다. [의견][^ref-1411]

## 6. 연결되는 연구영역

- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 주 연구영역. 충전 하한·충전소·승강기 점유·공용 충전기 계획을 다룬다.
- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — 팩트시트의 batteryCharging 객체가 충전 수준을 로봇 선언으로 담는다. [사실][^ref-031]
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md) — 충전 지점·주차 지점이 교통 그래프 경유점 속성으로 정의된다. [사실][^ref-536]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 승강기 요청·상태 메시지가 설비 연동 인터페이스다. [사실][^ref-312][^ref-286]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 뮤텍스 잠금·해제 교착 수정이 통로 구간 점유 조율과 이어질 것으로 보인다. [추정][^ref-1398]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 배터리 열화 관리와 플릿 소프트웨어 판 기록이 수명주기 관리와 이어질 것으로 보인다. [추정][^ref-403][^ref-1398]

## 7. 열린 질문

- **oq-069** (상태: 해결 · 실행 2026-10-10-05) 출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot(지원 작업 문서)과 is_charger(교통 편집기 문서·데모 README) 가운데 어느 속성으로 하는가? — 답은 3절 "충전소 경유점 지정: 문서와 구현"에 있다.
- **oq-066**·**oq-067**·**oq-068** (상태: 열림) — 3절에 부분 근거만 있다.
- 새 질문 4건(공용 충전기 예약 초과 조정, SOC 추정 오차를 반영한 운영 하한 여유 검증, 열화 최적화 결과의 실물 재현 자료, 승강기 운행 시간 민감도와 실제 대기열의 관계)은 [열린 질문](../../open-questions.md)에 등록한다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-039]: Open Robotics, Currently supported Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_types.html, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-10
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-10-10
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-10-10
[^ref-403]: Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03-24, https://arxiv.org/abs/2603.22731, 접근일 2026-10-10
[^ref-536]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-10-10
[^ref-1410]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp (2.14.0), 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp, 접근일 2026-10-10
[^ref-1411]: Song Yang, Sichen Yue, Xiao Wang, Kaiyu Wang, Xin Tian, Xiao Wang (Processes, MDPI), A Two-Stage Logistics–Energy Coordinated Optimization Framework for AGV Scheduling and Charging Under Reefer Container Temperature Constraints, 2026-07-27, https://www.mdpi.com/2227-9717/14/15/2424, 접근일 2026-10-10 (원문 미열람)
[^ref-1398]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0), 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-10

## 9. 검증 노트

- 판정: 1차 조건부 승인 / 2차 통과
- 확인·미확인: 확인 27건 · 미확인 0건 · 교차 확인 0건
- 강등된 주장: 없음
- 검증자 주의: 판정: 조건부 승인 / 2차 통과(재검증). 확인 27건, 미확인 0건, 교차 확인 0건. 강등: 없음. 원문 미열람 출처: ref-1411(Yang 외, Crossref 초록만 확인). 주의: 이번 브리프는 외부 AI 조사 메모를 바꾼 것이라 이 실행 안에 검색 기록이 없고, 한국 자료도 없다. VDA 5050·Open-RMF 출처는 모두 같은 발행 주체나 같은 프로젝트의 자료라 독립 교차 확인으로 세지 않았다. VDA 5050 3.0.0 명세와 factsheet.schema(ref-228)는 모두 임계 충전 수준 이하의 주문 제한을 권고(should)로 적는다. 그래서 5절 제약 행의 '보내야 한다'를 권고 표현으로 정정했다. 호텔 연구(ref-103)는 이번 실행에서 처음 원문을 열었다. 원문 자체가 'nearly doubles'(225→500 s)라고 쓴다. Li 외(ref-403)의 최대 54% 열화 감소는 프리프린트에 실린 대표 사례 하나의 예시값이다. oq-069 해결 인정(f8·f9): 현재 구현은 충전소를 is_charger 로 지정하지만, 지원 작업 문서(ref-039)는 아직 is_parking_spot 으로 적고 있어 두 서술을 함께 싣는다. oq-066·oq-067·oq-068 은 부분 근거만 있어 열린 질문으로 남긴다. 트랙 반영 제안 4건(IDTA 02047·배터리 여권·rmf_traffic 문·승강기 표현)은 이번 브리프가 조사하지 않아 반영하지 않았다. ref-1398 는 같은 날 실행 2026-10-10-03·04 에 등록된 변경 이력 출처(ref-1487·ref-1513)와 URL 이 같아 기존 id 로 합친다. 정정 요청(corr) 없음. / 2차 통과. 드리프트 없음, [분류원문] 보존, 섹션 순서 준수, 링크 유효. 직전 2차 수정 지시 5건은 모두 이행됐다. (1) 새 분리 페이지 2026-10-10-area28-s6·s7·s8·s11 이 2026-09-25 분리 페이지로 가는 링크를 문단 안 문장으로 둔다. (2) s6·s7 끝에 새 주제 페이지 링크가 있다. (3) 2026-09-25-area16-s6 의 sources 에 ref-1410 이 들어갔고, last_run 을 갱신했으며, 각주 정의를 8. 출처 안으로 옮기고 이력 행을 더했다. (4) 새 주제 페이지 세 줄 요약 둘째 줄을 f6 범위로 좁히고 충전소 지정은 별도 구절로 썼다. (5) 항만 연계 범위 문장에 의견 주체를 밝혔다. 태그는 1차 처분과 같다. 다음 갱신에서 처리할 사항(이전 지시에 없던 지적이며 게시를 막지 않는다): 2026-09-25-area16-s6 에는 원래의 충돌 문장이 아직 남아 있어 '2026-10-10 정정' 소제목으로만 보정돼 있다. 이 페이지가 이번 입력에 들어 있었으므로 다음 갱신 때 원 문장을 정정 문장으로 바꾼다. 같은 페이지 1절의 '새 주장은 없다'와 9절의 '내용은 바꾸지 않았다'는 이번 추가분과 맞지 않으므로 함께 고친다. 파이프라인 담당 참고: 절을 다시 분리하는 코드가 이전 분리 링크 줄을 버리지 않는지 확인이 필요하다.
- 신뢰도: medium

## 10. 이력

| 날짜 | 실행 id | 변경 | 버전 |
|---|---|---|---|
| 2026-10-10 | 2026-10-10-05 | 신규 작성 | 1 |
