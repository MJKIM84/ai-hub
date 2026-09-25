---
title: "20. 예외 복구·재계획·업무 연속성"
type: area
category: "E. 협업·현장 운영"
area_no: 20
related_areas: [1, 7, 9, 11, 12, 13, 15, 18, 19, 22]
tags: [예외 복구, VDA 5050, Open-RMF, 재계획, 업무 연속성, 보상 트랜잭션]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-004, ref-031, ref-051, ref-188, ref-537, ref-572, ref-573, ref-574, ref-575, ref-576, ref-578, ref-579, ref-580, ref-581]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [E. 협업·현장 운영](index.md) › 20. 예외 복구·재계획·업무 연속성

# 20. 예외 복구·재계획·업무 연속성

!!! info "소속 대분류"
    [E. 협업·현장 운영](index.md) — 핵심 질문:
    계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 [분류원문]

## 2. SCM 관점의 질문

운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? [분류원문]

## 3. 왜 중요한가

로봇 인터페이스 표준 VDA 5050 은 교착(deadlock)과 통신 오류의 탐지·해소를 개별 로봇이 아니라 관제(fleet control)의 역할로 두므로, 고장 한 건의 처리는 현장 전체를 보는 층에서 정해야 하는 문제가 된다. [추정][^ref-031]

한 로봇의 지연·취소는 주변 로봇의 계획에도 번진다. Open-RMF 의 교통 스케줄은 지연·취소·경로 변경을 반영해 계속 바뀌는 데이터베이스이고, 충돌이 예상되면 관련 플릿 관리자 사이의 협상이 시작된다. [사실][^ref-004]

고장 로봇 하나가 전체를 멈추지 않게 하는 설계는 제품 차원에서도 다뤄진다. Element Logic 은 AutoStore 제어 소프트웨어의 XHandler 모듈이 고장 난 로봇을 넘겨받아 시스템을 멈추지 않고 오류를 처리하며, 자동 처리가 불가능하거나 충돌 위험이 있을 때만 시스템이 정지한다고 설명한다. [추정] 벤더 주장[^ref-579] Swisslog 은 로봇이 멈추면 자사 소프트웨어 SynQ 가 멈춘 로봇 아래 보관함의 재고를 다른 보관함으로 재할당해, 로봇을 정기 휴식이나 저수요 시간에 꺼낼 때까지 주문 처리를 계속한다고 설명한다(2025년 7월 기준). [추정] 벤더 주장[^ref-580]

기업 차원에서는 업무 연속성 관리가 같은 질문을 더 넓게 다룬다. 다만 기업 업무 연속성 계획(Business Continuity Plan, BCP) 체계는 ROP 직접 범위가 아니라 현장의 제한 운영·수동 전환 계획을 세울 때 참조하는 연계 대상이다(7절). [추정][^ref-575]

## 4. 핵심 개념과 용어

이 영역의 용어는 로봇 인터페이스의 중단·취소 동작과, 이미 일어난 일을 기록에서 보상·정정하는 개념으로 나뉜다. [사실][^ref-031]

자세한 내용은 주제 페이지 [20. 예외 복구·재계획·업무 연속성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area20-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 피킹 → 포장

**시나리오:** 피킹한 주문 토트를 포장대로 운반하던 로봇이 도중에 멈춤

| 항목 | 내용 |
|---|---|
| 시작 조건 | 운반 중인 로봇이 오류 수준(WARNING·URGENT·CRITICAL·FATAL)을 보고하거나 연결 상태가 CONNECTION_BROKEN 으로 바뀐다. [사실][^ref-051][^ref-031] |
| 작업 대상 | 로봇에 실린 토트. 로봇이 loads 를 보고한다면 적재물 식별번호(loadId)·종류·적재 위치·치수·무게로 어떤 화물이 실렸는지 관제가 알 수 있다(선택 필드). [사실][^ref-051] |
| 수행 자원 | 멈춘 로봇, 남은 작업을 넘겨받을 대체 로봇, 화물을 회수할 작업자, 결정을 내리는 관제. 작업 의존성·우선순위 선점·고장 복구를 함께 다루는 배정 방법이 연구돼 있다. [사실][^ref-573] |
| 제약 | 연결이 끊긴 로봇은 마지막으로 해제된 노드까지만 주문을 수행하므로, 관제가 한 번에 해제하는 범위(base)의 길이가 단절 동안 작업이 얼마나 계속되는지를 정하는 설계 변수가 될 것으로 보인다. [추정][^ref-031] |
| 완료·인계 | 회수한 화물의 위치를 다시 확인한 뒤 재고·이벤트 기록을 정정해야 완료로 인정할 수 있다. EPCIS 1.2 기준으로는 오류 선언 이벤트로 기존 기록을 정정한다. [사실][^ref-581] 회수 때 어떤 확인(스캔·무게·위치)을 요구할지는 미확인이다(11절). |
| 예외·성과 | 관제가 cancelOrder 를 보내면 로봇은 정지하고 남은 동작을 FAILED 로 보고한다. [사실][^ref-031] 멈춘 로봇의 영향을 줄이는 재고 재할당·자동 복구는 AutoStore 계열 제품의 기능으로 설명된다. [추정] 벤더 주장[^ref-579][^ref-580] 처리량·시간·비용 영향 수치는 미확인이다. |

다음은 설명을 위한 가상의 시나리오이다. 피킹을 마친 토트를 싣고 포장대로 가던 로봇이 통로에서 멈추면, 관제는 먼저 오류·연결 상태로 무엇이 일어났는지 확인하고 주문을 일시정지하거나 취소한다. 이어 로봇이 보고한 적재물 정보로 어떤 주문의 화물이 묶였는지 파악하고, 남은 작업을 다른 로봇에 넘기며, 사람이 화물을 회수한 뒤 재고 기록을 바로잡는다.

이렇게 감지 → 일시정지·취소 → 실린 화물 식별 → 남은 작업 재배정 → 물리적 회수 → 재고·이벤트 기록의 보상·정정으로 이어지는 결정 흐름으로 볼 수 있을 것으로 보인다. 다만 이 흐름을 한 절차로 정한 출처는 이번 조사에서 찾지 못했다. [추정][^ref-031][^ref-051][^ref-573][^ref-578][^ref-581]

```mermaid
flowchart LR
  detect[고장·연결 끊김 감지] --> hold[주문 일시정지·취소]
  hold --> identify[실린 화물 식별]
  identify --> reassign[남은 작업 재배정]
  reassign --> recover[화물 물리적 회수]
  recover --> correct[재고·이벤트 기록 보상·정정]
```

## 6. 대표 접근법과 기술

대표 접근법은 관제 인터페이스의 중단·취소·재계획 기능, 통신 단절 동안의 계속 운행 규칙, 실행 중 재계획 연구, 고장 허용 재배정, 기록의 보상·정정으로 나뉜다. [사실][^ref-031][^ref-537]

자세한 내용은 주제 페이지 [20. 예외 복구·재계획·업무 연속성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area20-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

예외 동작 자체는 VDA 5050·Open-RMF 가 정의하고, 업무 연속성 표준과 국내 제도는 현장 제한 운영·수동 전환 계획의 참조 틀(연계 대상)로 쓴다. [추정][^ref-031][^ref-575]

자세한 내용은 주제 페이지 [20. 예외 복구·재계획·업무 연속성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area20-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 연구는 지연에 강건한 계획 실행, 통과 순서 재스케줄, 고장 복구를 포함한 작업 배정, 온라인 재계획 네 갈래다. [사실][^ref-188][^ref-572]

- Hönig 외, Persistent and Robust Execution of MAPF Schedules in Warehouses(IEEE RA-L, 2019) — 행동 의존 그래프로 창고 다중 로봇 계획을 감속·장애물·지연에도 충돌 없이 실행하는 틀이다. [사실][^ref-188]
- Feng 외, A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution(ICAPS 2024) — 지연된 로봇의 통과 순서를 SES 로 재스케줄한다. 속도 수치는 저자 보고값이다. [사실][^ref-572]
- Kalempa 외, Multi-Robot Preemptive Task Scheduling with Fault Recovery(Sensors, 2021) — 선점 스케줄링과 고장 복구를 결합한 MRPF. [사실][^ref-573]
- Emanuelsson 외, Multiagent Rollout with Reshuffling for Warehouse Robots Path Planning(IFAC 게재, 2023) — 온라인 재계획으로 로봇 고장에 적응하는 예제를 보인다. [사실][^ref-574]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

로봇 자체 복구·안전 제어는 제조사 몫인 연계 대상이고, 이종 로봇을 잇는 ROP 는 주문 취소·재배정·수동 전환 결정과 기록 정정을 맡는 경계가 될 것으로 보인다. [추정][^ref-031][^ref-537]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 오류·연결 상태 수신, 주문 일시정지·취소, 재계획 요청·작업 수락 중지, 사용자 개입·수동 전환 결정 [추정][^ref-031][^ref-537] | 연계 대상: 장애물 회피·재위치 추정·비상정지 회로 같은 로봇 자체 복구·안전 제어 [추정][^ref-031] |
| 상위 업무 시스템 | 취소·회수 결과를 보상 원칙에 따라 기록하고 재고·이벤트 정정을 반영 [추정][^ref-578][^ref-581] | 연계 대상: 전사 BCP·BCMS 와 재해경감 체계(현장 제한 운영 계획의 참조 틀) [추정][^ref-575][^ref-576] |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

예외 복구는 명령 실행 보장, 재배정·재계획, 모니터링, 사람 개입, 재고 정정을 맡는 영역과 맞물린다. [추정][^ref-031]

자세한 내용은 주제 페이지 [20. 예외 복구·재계획·업무 연속성 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area20-s10.md)에 있다.

## 11. 열린 질문

화물 회수 뒤 재고 확인 기준, 국내 수동·제한 운영 전환 기준, 제한 운영 처리량 추정이 새로 열렸고, 기존 네 질문은 부분 근거만 있어 열림 상태를 유지한다. [의견]

자세한 내용은 주제 페이지 [20. 예외 복구·재계획·업무 연속성 — 열린 질문](../../topics/2026/2026-09-25-area20-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-188]: Hönig, W., Kiesel, S., Tinka, A., Durham, J. W., & Ayanian, N., Persistent and Robust Execution of MAPF Schedules in Warehouses, 2019-04, https://ieeexplore.ieee.org/abstract/document/8620328/, 접근일 2026-09-25 (원문 미열람)
[^ref-537]: Open Robotics (open-rmf/rmf_ros2), rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 접근일 2026-09-25
[^ref-572]: Feng, Y., Paul, A., Chen, Z., & Li, J., A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution, 2024, https://arxiv.org/abs/2403.18145, 접근일 2026-09-25 (원문 미열람)
[^ref-573]: Kalempa, V. C., Piardi, L., Limeira, M., & de Oliveira, A. S., Multi-Robot Preemptive Task Scheduling with Fault Recovery: A Novel Approach to Automatic Logistics of Smart Factories, 2021-09-30, https://www.mdpi.com/1424-8220/21/19/6536, 접근일 2026-09-25 (원문 미열람)
[^ref-574]: Emanuelsson, W., Penacho Riveiros, A., Li, Y., Johansson, K. H., & Mårtensson, J. (KTH), Multiagent Rollout with Reshuffling for Warehouse Robots Path Planning, 2023, https://arxiv.org/abs/2211.08201, 접근일 2026-09-25 (원문 미열람)
[^ref-575]: ISO, ISO 22301:2019 - Security and resilience — Business continuity management systems — Requirements, 2019, https://www.iso.org/standard/75106.html, 접근일 2026-09-25 (원문 미열람)
[^ref-576]: 행정안전부, 재해경감 우수기업 인증제도, 미확인, https://www.mois.go.kr/frt/sub/a06/b10/disasterMitigationCompanies/screen.do, 접근일 2026-09-25 (원문 미열람)
[^ref-578]: Microsoft (MicrosoftDocs/architecture-center), Compensating Transaction pattern, 2026-04-16, https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction, 접근일 2026-09-25
[^ref-579]: Element Logic, FAQ - Element Logic (AutoStore), 미확인, https://www.elementlogic.net/solutions-and-services/autostore/faq/, 접근일 2026-09-25 (원문 미열람)
[^ref-580]: Swisslog, The benefits of using AutoStore for high-throughput retail fulfillment, 2025-07, https://www.swisslog.com/en-us/blog/2025/07/benefits-of-autostore-htp, 접근일 2026-09-25 (원문 미열람)
[^ref-581]: GS1, EPC Information Services (EPCIS) Standard 1.2, 2016-09-29, https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf, 접근일 2026-09-25 (원문 미열람)
