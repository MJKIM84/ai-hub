---
title: "1. 주문·업무 시스템 연계"
type: area
category: "A. 업무·공급망 설계"
area_no: 1
related_areas: [2, 9, 12, 13, 14, 20, 28]
tags: [ISA-95, B2MML, VDA 5050, Open-RMF, 작업 지시, 주문 변경·취소]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-002, ref-031, ref-110, ref-111, ref-112, ref-113, ref-114, ref-115, ref-116, ref-117, ref-118]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [A. 업무·공급망 설계](index.md) › 1. 주문·업무 시스템 연계

# 1. 주문·업무 시스템 연계

!!! info "소속 대분류"
    [A. 업무·공급망 설계](index.md) — 핵심 질문:
    무슨 일을 왜, 얼마나 해야 하는가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 [분류원문]

## 2. SCM 관점의 질문

출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? [분류원문]

## 3. 왜 중요한가

로봇 쪽 대표 인터페이스인 VDA 5050은 상위 관제(fleet control)와 이동로봇 사이 통신만 다루고, 외부 IT 시스템(예: WMS·ERP)과의 인터페이스는 범위 밖으로 둔다. [사실][^ref-031] 그래서 창고 관리 시스템(Warehouse Management System, WMS)이나 전사적 자원관리(Enterprise Resource Planning, ERP)의 주문·변경·취소를 로봇 작업으로 옮기는 일은 로봇 규격이 대신해 주지 않는다. [추정][^ref-031]

자세한 내용은 주제 페이지 [1. 주문·업무 시스템 연계 — 왜 중요한가](../../topics/2026/2026-09-25-area01-s3.md)에 있다.

## 4. 핵심 개념과 용어

상위 업무 시스템과 로봇 인터페이스는 각자 다른 단위로 일을 부른다. 이 절은 두 쪽의 단위를 나란히 둔다.

자세한 내용은 주제 페이지 [1. 주문·업무 시스템 연계 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area01-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 피킹 → 출하

**시나리오:** 출고 우선순위가 바뀌어 피킹 중인 로봇 작업을 바꾸거나 취소한다

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 시스템이 출하 우선순위를 바꾸며 진행 중인 작업 지시를 변경·취소한다. B2MML 거래 동사에는 CHANGE·CANCEL이 있다. [사실][^ref-115] 이 변경·취소는 그 동사에 대응하는 것으로 보인다. [추정][^ref-115] 국내 벤더 설명으로는 WES가 WMS 작업 지시를 바탕으로 작업 순서를 조정하는 자리다. [추정] 벤더 주장[^ref-118] |
| 작업 대상 | 피킹 중인 주문의 화물(박스·토트)과 그 화물을 실었거나 실으러 가는 로봇 |
| 수행 자원 | 연구에서는 주문 배정(주문을 작업대에), 작업 생성, 로봇 작업 배정, 경로 계획을 서로 다른 결정으로 나눈다. [사실][^ref-117] Open-RMF는 작업을 가장 적합한 플릿 또는 특정 로봇에 맡길 수 있다. [사실][^ref-113] |
| 제약 | VDA 5050에서 진행 중 주문은 같은 orderId의 주문 갱신으로만 연장되고 이미 공개된(base) 구간은 바뀌지 않으며, 다른 orderId의 새 주문은 OTHER_ORDER_ACTIVE 오류로 거부된다. [사실][^ref-031] |
| 완료·인계 | 로봇 쪽 결과는 Open-RMF 작업 상태(canceled·completed 등)로 보고되고 [사실][^ref-112], 상위 쪽 결과 보고 단위는 작업 응답이다. [사실][^ref-116] |
| 예외·성과 | cancelOrder를 받은 로봇은 가능한 한 빨리 멈추고 예정 동작을 FAILED로 보고한다. [사실][^ref-031] 이미 화물을 싣거나 옮긴 뒤라면 되돌림 작업이 더 생길 수 있어 번역이 일대일이 아닐 것으로 보인다. [추정][^ref-115][^ref-116][^ref-031][^ref-111] 처리량·시간·비용 영향은 미확인이다. |

다음은 설명을 위한 가상의 시나리오이며 현장 수치는 넣지 않았다. 출하 마감이 당겨진 주문이 생겨 상위 시스템이 기존 피킹 작업 지시를 바꾸거나 취소한다. ROP는 이 지시를 받아 아직 공개되지 않은 경로를 갱신할지, 취소 후 다시 지시할지를 정해야 한다. [추정][^ref-031][^ref-110][^ref-111]

이 영역이 맡는 칸은 시작 조건(상위 지시 수신), 예외·성과(취소·변경의 번역), 완료·인계(결과를 작업 응답으로 되돌리기)다. 누가 되돌림 작업과 재고 반영 규칙을 정하는지는 11절의 열린 질문으로 남긴다.

## 6. 대표 접근법과 기술

진행 중인 로봇 작업을 바꾸는 방법은 로봇 인터페이스가 허용하는 갱신·취소·요청 시점 지정과, 상위 지시를 그 수단으로 옮기는 번역으로 나뉜다. [추정][^ref-031][^ref-110][^ref-111]

자세한 내용은 주제 페이지 [1. 주문·업무 시스템 연계 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area01-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

상위 업무–실행 계층과 로봇 관제 계층에 각각 요청–응답 규격이 있고, 이 영역은 그 사이에 놓인다. 목록 전체는 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| [ISA-95](../../glossary/isa-95.md) · B2MML | 표준 | ISA-95 데이터 모델의 XML 구현과 거래 동사(CHANGE·CANCEL 등, Version 0701 기준) | [^ref-114][^ref-115] |
| OPC UA for ISA-95 Part 4: Job Control (OPC 10031-4) | 표준 | 작업 지시 수신 객체의 Store·Update·Abort 등의 메서드. 온라인 참조 v2.00 기준, 원문 미열람 | [^ref-116] |
| [VDA 5050](../../glossary/vda-5050.md) 3.0.0 | 표준 | 상위 관제–이동로봇의 주문 갱신·취소·거부. 외부 IT 시스템 인터페이스는 범위 밖 | [^ref-031] |
| [Open-RMF](../../glossary/open-rmf.md) 작업 API(rmf_api_msgs) | 오픈소스 | 작업 요청·취소 요청·작업 상태 JSON 스키마와 작업 전달 방식 | [^ref-110][^ref-111][^ref-112][^ref-113] |

## 8. 대표 연구와 자료

이 영역의 연구 근거는 아직 얇고, 현재는 운영 의사결정의 분해를 다룬 논문 한 건과 규격 문서가 중심이다.

자세한 내용은 주제 페이지 [1. 주문·업무 시스템 연계 — 대표 연구와 자료](../../topics/2026/2026-09-25-area01-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 작업 지시를 받아 로봇 작업(주문·작업 요청)으로 바꾸고 진행·완료·취소 결과를 작업 응답으로 되돌린다. [추정][^ref-116][^ref-117][^ref-031] | 분류 원문 9장 표의 외부 연계 항목: "수요예측, 구매, 재무, 전사 재고정책" |

표의 따옴표 안 문구는 분류 원문 9장 표의 셀이며 전체 경계는 [범위 경계](../../about/scope-boundary.md)에 있다. 이와 별도로, 주문을 작업대·웨이브에 배정하고 재고를 할당하는 결정은 WMS·WES 등 상위 시스템 몫이고 ROP는 그 경계에 서는 것으로 보이나, 이는 원문 9장 표의 항목이 아니라 이번 조사의 추정이다(연계 대상). [추정][^ref-116][^ref-117][^ref-031] VDA 5050은 외부 IT 시스템 인터페이스를 범위 밖으로 둔다. [사실][^ref-031] 따라서 상위 연계는 ROP 쪽에서 설계해야 할 것으로 보인다. [추정][^ref-031]

다만 이 경계는 고정되지 않는다. 분류 원문은 다음과 같이 적는다.

기업 업무와 현장 운영·제어의 경계를 정리할 때는 ISA-95의 기업–제어 시스템 통합 관점이 참고가 된다. 실제 제품별로 WES·WCS·FMS·ROP의 책임은 겹칠 수 있다. [2] [분류원문]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

원문의 [2]는 참고문헌 [ref-002](../../references/ref-002.md)에 해당한다.[^ref-002]

```mermaid
flowchart LR
  upper["상위 업무 시스템(WMS·WES·ERP)"] -- "작업 지시·변경·취소" --> rop["ROP"]
  rop -- "작업 응답(진행·완료·취소 결과)" --> upper
  rop -- "주문 갱신·취소 / 작업 요청·취소" --> fleet["로봇 관제·이동로봇"]
  fleet -- "상태·작업 상태" --> rop
```

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

상위 지시를 로봇 작업으로 옮기는 일은 모델링·연동·계획·예외 처리 영역과 맞물린다.

- [2. 공정·워크플로 모델링](02-process-and-workflow-modeling.md) — 작업 지시·작업 응답의 요청–응답 순환이 작업 단계와 완료 조건 정의와 이어진다.
- [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — VDA 5050 주문 갱신과 Open-RMF 작업 요청이 번역의 로봇 쪽 끝이다.
- [12. 명령·작업 실행의 신뢰성](../c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) — 주문 거부 오류 유형과 취소 요청의 처리 결과 확인.
- [13. 작업 배정 — MRTA](../d-planning-and-optimization/13-task-allocation-mrta.md) — 주문 배정과 로봇 작업 배정의 구분.
- [14. 작업 순서·스케줄링](../d-planning-and-optimization/14-task-sequencing-and-scheduling.md) — 우선순위 변경 규칙을 담을 ROP 쪽 작업 대기열.
- [20. 예외 복구·재계획·업무 연속성](../e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) — 취소 뒤 정지와 되돌림 작업.
- [28. 표준·상호운용성·다사업자 거버넌스](../g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) — ISA-95 계열과 로봇 인터페이스 사이의 표준 매핑 문제.

## 11. 열린 질문

이번 실행에서 남은 질문은 번역 매핑과 되돌림 책임이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-08) ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가?
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-08) 로봇이 이미 화물을 싣거나 옮긴 뒤 상위 시스템이 주문을 취소·변경하면 되돌림 작업과 재고 반영을 누가 어떤 규칙으로 정하는가(국내 물류센터 사례 포함)?
- 관련 기존 질문: oq-002(국내 물류센터에서 SSCC·EPCIS 이벤트를 로봇 작업 결과와 연결해 운영하는 사례).

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-002]: ISA, Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems, 2025, https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of, 접근일 2026-09-24
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-110]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/cancel_task_request.json, 접근일 2026-09-25
[^ref-112]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25
[^ref-113]: Open Robotics, Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-25
[^ref-114]: MESA International, MESAInternational/B2MML-BatchML — README, 미확인, https://github.com/MESAInternational/B2MML-BatchML, 접근일 2026-09-25
[^ref-115]: MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd, 미확인, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd, 접근일 2026-09-25
[^ref-116]: OPC Foundation / ISA, OPC UA for ISA-95 - Part 4: Job Control (OPC 10031-4), 미확인, https://reference.opcfoundation.org/ISA95JOBCONTROL/v200/docs/, 접근일 2026-09-25 (원문 미열람)
[^ref-117]: Merschformann, M. 외, Decision Rules for Robotic Mobile Fulfillment Systems, 2018-01, https://arxiv.org/abs/1801.06703, 접근일 2026-09-25 (원문 미열람)
[^ref-118]: 씨메스(CMES Robotics), 물류 자동화 시스템을 이해하는 첫 걸음 : WES · WCS · WMS, 무엇이 다를까요?, 미확인, https://blog.cmesrobotics.ai/wes-wcs-wms, 접근일 2026-09-25 (원문 미열람)
