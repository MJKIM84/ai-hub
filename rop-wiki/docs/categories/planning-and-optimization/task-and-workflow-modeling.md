---
title: "24. 작업·워크플로 모델링"
type: area
category: "G. 계획·최적화"
area_no: 24
related_areas: [17, 20, 23, 26, 29, 32, 38, 39, 54, 67]
tags: [BPMN, ISA-95, 완료 조건, 인수 확인, 워크플로 넷, Open-RMF]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-10-10
sources: [ref-023, ref-031, ref-044, ref-049, ref-110, ref-111, ref-112, ref-113, ref-116, ref-117, ref-118, ref-119, ref-121, ref-123, ref-124, ref-366, ref-404, ref-502, ref-1400, ref-1398, ref-1401]
last_run: 2026-10-10
version: 3
---

[홈](../../index.md) › [G. 계획·최적화](index.md) › 24. 작업·워크플로 모델링

# 24. 작업·워크플로 모델링

!!! info "소속 대분류"
    [G. 계획·최적화](index.md) — 핵심 질문:
    누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 3 · 마지막 갱신: 2026-10-10 · 마지막 실행: 2026-10-10
<!-- auto:page-status:end -->

## 1. 한 줄 정의

현장 업무를 단계·선후관계·완료 조건으로 정의하고, 계획과 실행이 따를 운영 정책을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업·워크플로 모델링**: 현장 업무(운반·배송·순찰·점검·조작·서비스 등)를 단계·선후관계·완료 조건으로 분해해 정의한다
- **동작 완료와 업무 완료 연결**: 로봇의 동작 완료(도착·내려놓음)와 업무 완료(인수 확인·기록 반영)를 구분해 잇는다
- **운영 정책 설정**: 우선순위·운영 시간·구역 규칙·충전 기준 같은 운영 정책을 설정하고 버전으로 관리해 계획과 실행이 따르게 한다

이전 분류(2026-09-24)에서 이 페이지는 옛 2번 영역 ‘공정·워크플로 모델링’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 [옛 분류원문]

> 옛 질문: ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? [옛 분류원문]

## 2. 핵심 질문

현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? [분류원문]

## 3. 왜 중요한가

로봇 관제 규격의 하역 완료와 업무 어휘의 인수·재고 반영은 서로 다른 원문이 각각 정의한다(2026-10-10 확인). [사실][^ref-044][^ref-031][^ref-049]

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 왜 중요한가](../../topics/2026/2026-10-10-area24-s3.md)에 있다.

## 4. 핵심 개념과 용어

작업 단계와 완료 조건을 표현하는 데 쓰이는 핵심 용어는 다음과 같다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area02-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오 1·2는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 물류창고 밖의 사례는 아래 사례 3(현장 유형: 기타)에 있다.

다음은 설명을 위한 가상의 시나리오이며, 로봇의 완료 신호와 업무상 완료가 어디서 갈리는지를 보인다.

### 시나리오 1

**물류 흐름 단계:** 입고 → 적치

**시나리오:** 도크에서 하역된 입고 팔레트를 로봇이 하역 지점(워크셀)으로 운반해 인계하고, 입고 확정 뒤 보관 구역에 적치

| 항목 | 내용 |
|---|---|
| 시작 조건 | 입고 예정 화물이 도크에 도착해 상위 업무 시스템(WMS)이 입고 운반 작업을 요청한다. |
| 작업 대상 | 입고 팔레트와 그 화물 식별자. 이 식별자나 작업 id가 로봇 작업과 업무 확인을 잇는 키가 된다. |
| 수행 자원 | 로봇은 운반·하역을, 하역 지점 워크셀은 하역 결과 보고를, WMS는 인수 확인과 재고 반영을 맡는다. Open-RMF 배송 작업에서 로봇은 하역 지점에서 IngestorResult를 받을 때까지 IngestorRequest를 보낸다. [사실][^ref-023][^ref-049] |
| 제약 | 검수 종료 후 적치 시작, 같은 도크의 상차·하차 병행 금지, 하역 종료 후 일정 시간 안의 입고 확정 같은 선후·병행·시간 제약. ISA-95 세그먼트 의존 유형(AfterEnd, NotInParallel, NoLaterAfterEnd)으로 이런 제약을 단순 순서보다 세밀하게 표현할 수 있을 것으로 보이지만, ISA-95는 제조 운영 관리 표준이며 창고 작업에 적용한 사례는 확인하지 못했다. [추정][^ref-117][^ref-118] |
| 완료·인계 | VDA 5050 3.0.0은 drop 동작 완료를 적재물이 이동로봇을 떠나고 로봇이 새 적재 상태를 보고한 때로 정의한다. [사실][^ref-031] IngestorResult의 기본 정의 필드는 시각·요청 id·워크셀 id·상태(ACKNOWLEDGED, SUCCESS, FAILED)이며, 이 기본 필드에는 수령자 재고 편입 여부가 없다. [사실][^ref-049] 따라서 입고 완료와 재고 변경은 CBV receiving에 해당하는 WMS 인수 확인이 따로 있어야 인정할 수 있을 것으로 보인다(적용 표준·사례 미확인). [추정][^ref-031][^ref-049][^ref-044] |
| 예외·성과 | 인수 확인이 오지 않거나 하역이 실패하면 공정은 대기하거나 예외로 분기해야 한다. [추정][^ref-044][^ref-119] Open-RMF 작업 상태 스키마는 failed·canceled·delayed 등 작업 상태와 단계별 이벤트·소요 시간 추정값을 보고한다. [사실][^ref-111] 처리량·시간·비용 영향은 미확인이다. |

로봇이 팔레트를 내려놓으면 로봇 쪽 작업은 끝나지만, 이 시점을 곧바로 CBV arriving이나 receiving으로 단정하지 않고 어느 업무 단계에 해당하는지는 WMS 같은 업무 측 확인으로 정하는 것이 적절하다는 것이 이 위키의 판단이다. [의견][^ref-044][^ref-031] BPMN 모델에서 로봇 운반을 하나의 작업 단계로 두고 그 뒤에 WMS 인수 확인 메시지를 기다리는 수신 단계를 두어 작업 id나 화물 식별자로 상관시키면, 두 완료를 서로 다른 완료 조건을 가진 연속 단계로 표현할 수 있을 것으로 보인다(이 구성을 물류 로봇에 적용한 표준·사례는 확인하지 못했다). [추정][^ref-112][^ref-113][^ref-044]

입고 확정이 나야 적치 작업이 시작되므로, 적치 단계의 선후 제약은 입고 단계의 완료 조건에 기대게 된다. [추정][^ref-117][^ref-118]

### 시나리오 2

**물류 흐름 단계:** 출하

**시나리오:** 출하 대기 화물을 로봇이 출하 도크로 운반해 인도

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 포장을 마친 출하 화물 |
| 수행 자원 | 해당 없음 |
| 제약 | 해당 없음 |
| 완료·인계 | 로봇의 drop 완료는 화물의 물리적 인도까지만 가리킨다. [사실][^ref-031] 업무상 이행의 끝은 SCOR B2C 이행의 마지막 단계 F1.11 배송 증빙 또는 고객 인수 확보이다. [사실][^ref-123] |
| 예외·성과 | 해당 없음 |

출하에서도 로봇 작업 완료와 고객 인수 사이에 업무 단계가 남는다. [추정][^ref-031][^ref-123]

### 사례 3 — 물류창고 밖: 농업·지상 로봇 협업 시뮬레이션

**현장 유형:** 기타

**사례:** 농업·지상 로봇 협업 시뮬레이션에서 BPMN 협업 모델로 다중 로봇 임무를 실행하는 공개 예제(FaMe, [67. 기타 현장](../site-type-applications/other-sites.md))

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 모델링 지침은 로봇을 풀(Pool), 임무를 프로세스(Process), 동작을 활동(Activity)으로 나타낸다. [사실][^ref-1400] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

이 사례는 물류창고 밖의 공개 작업 모델링 예제다. FaMe 연구팀(University of Camerino PROS Lab)은 공식 페이지(2022-05-03 게시)에서 지상 로봇 협업과 농업 두 시나리오의 시뮬레이션 패키지와 엔진 패키지의 빌드·실행 절차(colcon build, ros2 launch)를 공개한다. [사실][^ref-1400] FaMe는 BPMN 협업 다이어그램으로 다중 로봇 임무를 정의하고 모델링·구성·실행 단계를 거쳐 각 로봇에서 ROS 2 위에 그 협업을 직접 실행하는 공개 프레임워크다. [사실][^ref-1400] 같은 지침은 병렬 동작을 AND 게이트웨이, 내부 선택을 XOR 게이트웨이, 시간 대기를 타이머 이벤트, 실행 오류를 오류 이벤트로 표현하게 한다. [사실][^ref-1400] 이 예제가 다루는 작업 대상(물건·공간·정보·사람)과 시작 조건·제약·완료 조건·예외 처리의 구체 내용, 시나리오가 실외 현장인지는 공식 페이지에서 확인하지 못해 현장 유형을 기타로 둔다.

이 예제는 시뮬레이션 재현 자료이며 현장 운영 성능 근거가 아니므로, 국내 상용 운영 실적이나 현장 성능 근거로 분류하지 않는 편이 좋다는 것이 이 위키의 판단이다. [의견][^ref-1400]

## 6. 대표 접근법과 기술

이 위키는 이 영역의 관련 접근법을 업무 프로세스 표기(BPMN), 제조 운영 표준의 세그먼트 의존(ISA-95·B2MML), 로봇 오케스트레이션의 작업 단계 구성(Open-RMF), 형식적 설계 점검(워크플로 넷)의 네 갈래로 정리한다. [의견][^ref-112][^ref-117][^ref-110][^ref-121]

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 대표 접근법과 기술](../../topics/2026/2026-10-10-area24-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역과 관련된 표준·오픈소스는 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-10-area24-s7.md)에 있다.

## 8. 대표 연구와 자료

로봇 작업을 업무 프로세스 형식으로 기술·실행하고 그 실행 기록을 분석하는 연구가 대표 자료다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 대표 연구와 자료](../../topics/2026/2026-10-10-area24-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이 영역에서 ROP는 업무 단계와 로봇 작업 단위 사이의 순서·대기·완료 조건을 맡고, 재고 확정과 로봇 내부 동작 흐름은 연계 대상으로 두는 구조가 경계와 맞아 보인다. [추정][^ref-044][^ref-119][^ref-116]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 운반 완료 이벤트를 전달하고 인수 확인을 기다리거나 예외로 분기하는 공정 단계 [추정][^ref-044][^ref-119] | 연계 대상: 수령자 재고 반영(CBV receiving)과 재고 운영 관리(IEC 62264-3) — WMS·MES 재고 확정 [추정][^ref-044][^ref-119] |
| 로봇 자체 지능·제어 | 업무 단계(BPMN·ISA-95·SCOR 수준)와 로봇 작업 단위(Open-RMF 단계, VDA 5050 동작) 사이의 순서·대기·완료 조건 [추정][^ref-112][^ref-110] | 연계 대상: 로봇 내부 동작 흐름(행동 트리·상태 기계로 구현되는 주행·파지 등) — 제조사 [추정][^ref-116] |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

두 층의 상태를 잇는 표준 매핑은 확인하지 못했으므로 위 표는 표준 정의를 엮은 추정이다. [추정][^ref-110][^ref-031] 경계의 전체 기준은 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

공정 모델의 단계와 완료 조건은 업무 시스템·식별·관제·실행 신뢰성·스케줄링·분석·검증 영역과 맞물린다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area02-s10.md)에 있다.

2026-10-10 보강으로 더한 연결:

- [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 취소 요청과 취소 후 정리 완료, 보상 단계의 구분(6절 보강)이 예외 복구 절차와 이어진다.
- [67. 기타 현장](../site-type-applications/other-sites.md) — 농업·지상 로봇 협업 시뮬레이션 사례(5절 사례 3)의 현장 유형이다.
- 기존 연결 가운데 [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)은 하역 완료와 인수·재고 반영의 구분(3절)으로, [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)은 VDA 5050 blockingType의 병행 제약(7절 보강)으로 이어진다.

## 11. 열린 질문

이 영역에서 아직 답하지 못한 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 열린 질문](../../topics/2026/2026-10-10-area24-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-10-10 · 갱신 · [24. 작업·워크플로 모델링](task-and-workflow-modeling.md) — 3절 첫 문단을 원문 정의(CBV 세 단계·VDA 5050 3.0.0 drop FINISHED·IngestorResult 기본 필드)와 [의견]으로 나눠 다시 씀, 5절 시나리오 1 문장 수정·IngestorResult 범위 한정과 사례 3(현장 유형 기타, FaMe, 작업 대상 미확인) 추가, 6·7·8·11절 보강(각 보강 소절 첫 줄에 2026-09-25 분리 주제 페이지 링크 유지)과 10절 연결 덧붙임, 13절 각주 갱신(ref-031·ref-044·ref-049 접근일, ref-116 발행일·접근일·열람)과 새 각주 1건(ref-1400). ref-366·ref-404·ref-502·ref-1398·ref-1401 는 자동 분리 뒤 분리 주제 페이지의 출처 절에만 남는다 (실행 2026-10-10-01)
- 2026-10-10 · 생성 · [24. 작업·워크플로 모델링 — 열린 질문](../../topics/2026/2026-10-10-area24-s11.md) — 자동 분리: 24. 작업·워크플로 모델링 의 "11. 열린 질문" 절(1,498자)을 옮겼다 (실행 2026-10-10-01)
- 2026-10-10 · 생성 · [24. 작업·워크플로 모델링 — 대표 접근법과 기술](../../topics/2026/2026-10-10-area24-s6.md) — 자동 분리: 24. 작업·워크플로 모델링 의 "6. 대표 접근법과 기술" 절(1,442자)을 옮겼다 (실행 2026-10-10-01)
- 2026-10-10 · 생성 · [24. 작업·워크플로 모델링 — 왜 중요한가](../../topics/2026/2026-10-10-area24-s3.md) — 자동 분리: 24. 작업·워크플로 모델링 의 "3. 왜 중요한가" 절(1,339자)을 옮겼다 (실행 2026-10-10-01)
- 2026-10-10 · 생성 · [24. 작업·워크플로 모델링 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-10-area24-s7.md) — 자동 분리: 24. 작업·워크플로 모델링 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,291자)을 옮겼다 (실행 2026-10-10-01)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-10-10
[^ref-049]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg, 접근일 2026-10-10
[^ref-110]: Open Robotics, Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-25
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25
[^ref-112]: OMG(Object Management Group), About the Business Process Model And Notation Specification Version 2.0, 미확인, https://www.omg.org/spec/BPMN/2.0/About-BPMN, 접근일 2026-09-25 (원문 미열람)
[^ref-113]: Camunda, Messages | Camunda 8 Docs (camunda-docs: docs/components/concepts/messages.md), 미확인, https://docs.camunda.io/docs/components/concepts/messages/, 접근일 2026-09-25
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03-16, https://arxiv.org/abs/2603.15427, 접근일 2026-10-10
[^ref-117]: MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd, 접근일 2026-09-25
[^ref-118]: MESA International, B2MML-BatchML — Schema/B2MML-OperationsDefinition.xsd, 미확인, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-OperationsDefinition.xsd, 접근일 2026-09-25
[^ref-119]: IEC / ISO, IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management, 2016, https://www.iso.org/standard/67480.html, 접근일 2026-09-25 (원문 미열람)
[^ref-121]: Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022), The complexity of soundness in workflow nets, 2022, https://arxiv.org/abs/2201.05588, 접근일 2026-09-25 (원문 미열람)
[^ref-123]: ASCM, SCOR Model — Fulfill F1.3 Pick Product, 미확인, https://scor.ascm.org/processes/fulfill/F1.3, 접근일 2026-09-25 (원문 미열람)
[^ref-1400]: University of Camerino PROS Lab, FaMe — A BPMN-driven Framework for Multi-Robot System Development (공식 페이지·사용 지침), 2022-05-03, https://pros.unicam.it/fame/, 접근일 2026-10-10
