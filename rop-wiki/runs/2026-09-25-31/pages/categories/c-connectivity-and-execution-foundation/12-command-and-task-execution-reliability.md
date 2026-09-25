---
title: "12. 명령·작업 실행의 신뢰성"
type: area
category: "C. 연결·실행 기반"
area_no: 12
related_areas: [1, 2, 9, 11, 19, 20]
tags: [VDA 5050, 멱등성, 작업 상태 기계, 시간 초과, 재시작 복원]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-031, ref-111, ref-125, ref-126, ref-127, ref-129, ref-130, ref-282, ref-306, ref-363, ref-364, ref-365, ref-366, ref-367, ref-368, ref-369, ref-370, ref-371, ref-372, ref-373, ref-374, ref-375]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [C. 연결·실행 기반](index.md) › 12. 명령·작업 실행의 신뢰성

# 12. 명령·작업 실행의 신뢰성

!!! info "소속 대분류"
    [C. 연결·실행 기반](index.md) — 핵심 질문:
    계획한 작업을 실제 장비가 확실하게 수행하게 하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

접수·실행·완료·취소 상태, 제어권, 중복 요청 방지, 시간 초과, 재시작 후 상태 복원 [분류원문]

## 2. SCM 관점의 질문

응답이 끊긴 운반 요청을 다시 보내면 같은 화물을 두 번 처리하지 않을까? [분류원문]

## 3. 왜 중요한가

로봇 명령은 무선망을 거쳐 전달되고 관제·로봇 어느 쪽이든 재시작될 수 있으므로, 명령의 접수와 완료를 따로 확인하는 장치가 없으면 2절의 질문처럼 같은 화물을 두 번 옮기거나 진행 중 작업을 잃을 수 있다. [추정][^ref-031][^ref-374]

VDA 5050 3.0.0 은 무선 전송을 신뢰할 수 없다는 전제에서, 이미 로봇에 넘긴 기반(base) 경로는 바꿀 수 없고 관제는 그 경로가 이미 실행됐다고 가정해야 한다고 정한다. [사실][^ref-031] 브로커와 연결이 끊긴 로봇도 주문 정보를 유지한 채 마지막으로 해제된(released) 노드까지 주문을 수행한다. [사실][^ref-031] 따라서 관제가 응답을 받지 못했다는 사실만으로 작업이 실행되지 않았다고 판단할 수는 없다. [추정][^ref-031]

재시작도 같은 문제를 낳는다. Open-RMF 저장소 이슈 #224 는 플릿 어댑터가 재시작되면 배정된 작업이 사라진다고 지적하고, 작업 로그와 백업을 SQLite 데이터베이스에 저장해 복구하는 기능이 별도 풀 리퀘스트로 제안되었다고 적는다(현재 배포판 반영 여부는 미확인). [사실][^ref-374]

반대로 응답이 끊긴 요청을 그대로 다시 보내면 중복 실행 위험이 생긴다. 로봇 쪽에 같은 주문의 재수신을 무시하는 규칙이 있어도, 상위 시스템이 새 요청으로 다시 보내 ROP 가 새 주문 id 를 발급하면 그 보호가 작동하지 않을 것으로 보인다. [추정][^ref-031][^ref-367]

## 4. 핵심 개념과 용어

대표 규격마다 명령을 구분하는 식별자와 상태 값을 따로 정한다: VDA 5050 은 주문 id·주문 갱신 id 를, ROS 2 액션은 클라이언트가 만든 UUID 목표 id 를 쓴다. [사실][^ref-031][^ref-363]

자세한 내용은 주제 페이지 [12. 명령·작업 실행의 신뢰성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area12-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

다음은 설명을 위한 가상의 시나리오이다.

**물류 흐름 단계:** 적치

**시나리오:** 입고 검수를 마친 팔레트를 보관 위치로 옮기는 운반 주문의 응답이 끊겨 다시 보내는 상황

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 시스템(WMS)이 입고 확정된 팔레트의 적치를 요청하고, ROP 가 이를 로봇 운반 주문으로 바꿔 보낸다. Open-RMF 작업 요청 스키마에는 요청자가 정하는 요청 식별자 필드가 없다. [사실][^ref-365][^ref-125] |
| 작업 대상 | 팔레트 1개와 그 운반 주문(주문 id·주문 갱신 id)이다. |
| 수행 자원 | ROP 는 요청 수신·주문 발급·상태 판정을, 로봇은 주행·적재·하역과 상태 보고를 맡는다. 연계 대상: 로봇 내부의 동작 재시도·정지 방식은 제조사 영역으로 보인다. [추정][^ref-031] |
| 제약 | 이미 넘긴 기반 경로는 바꿀 수 없고 관제는 그것이 실행됐다고 가정해야 한다. [사실][^ref-031] 상태 메시지가 오지 않을 때 관제가 할 일은 명세 발췌 범위에서 찾지 못했다(부재 확정 아님). [추정][^ref-031] |
| 완료·인계 | 로봇은 상태 메시지를 관련 사건이 생길 때 또는 적어도 30초마다 발행해야 하고, 관제는 그 안의 주문 id·주문 갱신 id 로 수용 여부를 안다. [사실][^ref-031] Open-RMF 작업 상태는 completed 등 상태 값과 시작·종료 시각을 담는다. [사실][^ref-111] |
| 예외·성과 | 같은 주문 id·같은 갱신 id·같은 내용으로 다시 보내면 로봇은 무시하지만, 상위 시스템이 새 요청으로 보내 ROP 가 새 주문 id 를 발급하면 이 보호가 작동하지 않을 것으로 보인다. [추정][^ref-031][^ref-367] |

관제가 적치 운반 주문을 보낸 뒤 로봇 상태 메시지에서 그 주문 id·주문 갱신 id 를 보지 못하면, 주문이 전달되지 않은 것인지 이미 실행 중인지 바로 구분할 수 없다. 같은 식별자로 다시 보내는 것은 VDA 5050 로봇 쪽에서 무시되므로 안전하지만, 같은 적치 요청이 새 요청으로 들어오면 두 번째 운반 주문이 생길 수 있다. [추정][^ref-031][^ref-367]

Open-RMF 를 쓰는 경우 응답을 받지 못한 파견 요청을 그대로 다시 보내면 별개 작업이 하나 더 생길 수 있어, ROP 쪽에서 상위 요청 id 와 작업 id 의 대응을 저장해 중복을 걸러야 할 것으로 보인다(서버 쪽 중복 필터링은 미확인). [추정][^ref-365][^ref-125][^ref-111] 이 시나리오에서 이 영역이 관여하는 칸은 주로 시작 조건(요청 식별), 완료·인계(상태 판정), 예외·성과(재전송 처리)다.

## 6. 대표 접근법과 기술

명령 실행 신뢰성의 기법은 식별자로 중복 거르기, 요청 단위 멱등성 키, 상태 기계, 시간 초과 감지, 재시도·취소·보상, 상태 저장과 재시작 복원으로 나눌 수 있다. [추정][^ref-031][^ref-366]

자세한 내용은 주제 페이지 [12. 명령·작업 실행의 신뢰성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area12-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

아래 표는 명령 식별자·상태·재시도·끊김 감지를 정한 표준과 공개 구현을 정리한 것이다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [12. 명령·작업 실행의 신뢰성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area12-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 학술 자료는 실행 구조(행동 트리·사가)와 메시지 전달 신뢰성 측정이 중심이며, 사가를 물류 로봇에 적용한 사례는 이번 조사에서 찾지 못했다. [추정][^ref-370][^ref-373]

자세한 내용은 주제 페이지 [12. 명령·작업 실행의 신뢰성 — 대표 연구와 자료](../../topics/2026/2026-09-25-area12-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

이 영역에서 ROP 는 명령 식별자와 작업 상태를 관리하는 쪽이고, 로봇 내부의 동작 복구는 제조사에 맡기는 쪽에 가까운 것으로 보인다. [추정][^ref-031][^ref-366]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 명령 식별자 발급·보존, 작업 상태 기계 유지, 시간 초과 판정, 재시작 뒤 상태 복원, 로봇이 보고한 RETRIABLE·cancelOrder 상태의 해석 [추정][^ref-031][^ref-366][^ref-365] | 연계 대상: 로봇 내부의 동작 재시도, 로컬 회피, 정지 방식(선 유도 로봇의 다음 노드 정지 등) [추정][^ref-031] |
| 상위 업무 시스템 | 상위 요청의 중복 판별(상위 요청 id 와 작업 id 의 대응 보존), 완료·취소 결과 반영 [추정][^ref-367][^ref-365] | 연계 대상: 작업 지시의 발행·변경·취소는 상위 쪽 규격(ISA-95 Job Control 메서드, B2MML 거래 동사)으로 표현된다 [사실][^ref-130][^ref-129] |

통신 계층(MQTT QoS, ROS 2 QoS)은 전달 보장과 끊김 신호를 제공할 뿐 업무 요청 단위의 중복을 판단하지 않으므로, ROP 는 이를 입력으로 받아 응용 계층에서 중복·시간 초과를 판정해야 할 것으로 보인다. [추정][^ref-306][^ref-031]

분류 원문 9장은 이 경계가 제품 전략에 따라 이동할 수 있고, 이종 제조사를 연결하는 ROP 는 로봇 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다고 본다([범위 경계](../../about/scope-boundary.md)).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

명령 신뢰성은 상위 요청을 받는 쪽, 로봇·통신 쪽, 실패 뒤 처리 쪽에 모두 걸쳐 있다. [추정][^ref-031][^ref-130]

- [1. 주문·업무 시스템 연계](../a-business-supply-chain-design/01-order-and-business-system-integration.md) — 상위 작업 지시의 저장·시작·취소 메서드와 거래 동사가 ROP 가 받는 요청의 식별·취소 단위가 될 것으로 보인다. [추정][^ref-130][^ref-129]
- [2. 공정·워크플로 모델링](../a-business-supply-chain-design/02-process-and-workflow-modeling.md) — 업무 프로세스 단계 상태와 로봇 작업 상태를 맞추는 대응 규칙 문제(oq-014)를 공유한다. [추정][^ref-111]
- [9. 로봇·제조사 관제 연동](09-robot-and-vendor-fleet-manager-integration.md) — VDA 5050 주문 id·동작 상태 규칙을 어댑터가 옮기며, 공통 상태·오류 어휘 문제(oq-033)를 공유한다. [추정][^ref-031]
- [11. 분산 시스템·통신·컴퓨팅 구조](11-distributed-systems-communication-and-computing.md) — MQTT·ROS 2 QoS 전달 보장과 브로커 손실률 같은 통신 계층 내용은 그 영역에서 다루고, 이 영역은 이를 중복·시간 초과 판단의 입력으로만 쓴다. [추정][^ref-306][^ref-282][^ref-375]
- [19. 모니터링·이상 탐지·원인 분석](../e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) — 작업 상태 기록(취소·강제 종료·중단)이 이상 탐지와 원인 분석의 입력이 될 것으로 보인다. [추정][^ref-111]
- [20. 예외 복구·재계획·업무 연속성](../e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) — 재시도·취소·보상 작업과 재시작 뒤 복원이 예외 복구 절차로 이어지며, 화물을 옮긴 뒤 취소된 주문의 되돌림 규칙(oq-021)을 공유한다. [추정][^ref-366][^ref-373]

## 11. 열린 질문

공통 작업 상태 매핑과 되돌림 규칙은 이번 조사에서도 표준을 찾지 못했고, 중복 키 보존 기간과 재시작 뒤 복원 방식은 새 질문으로 올린다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [12. 명령·작업 실행의 신뢰성 — 열린 질문](../../topics/2026/2026-09-25-area12-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25
[^ref-129]: MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd, 접근일 2026-09-25 (원문 미열람)
[^ref-130]: OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv), 2024-01-31, https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL, 접근일 2026-09-25
[^ref-282]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-09-25
[^ref-306]: OASIS, MQTT Version 5.0, 2019-03, https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html, 접근일 2026-09-25 (원문 미열람)
[^ref-363]: ROS 2 Design, Actions (ROS 2 Design), 미확인, https://design.ros2.org/articles/actions.html, 접근일 2026-09-25
[^ref-365]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/dispatch_task_request.json, 접근일 2026-09-25
[^ref-366]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/Task.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp, 접근일 2026-09-25
[^ref-367]: IETF HTTPAPI Working Group (Jena, J., & Dalal, S.), The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header), 미확인, https://github.com/ietf-wg-httpapi/idempotency/blob/main/draft-ietf-httpapi-idempotency-key-header.md, 접근일 2026-09-25
[^ref-370]: Colledanchise, M., & Ögren, P., Behavior Trees in Robotics and AI: An Introduction, 2017-09, https://arxiv.org/abs/1709.00084, 접근일 2026-09-25 (원문 미열람)
[^ref-373]: Garcia-Molina, H., & Salem, K., Sagas, 1987, https://dl.acm.org/doi/10.1145/38713.38742, 접근일 2026-09-25 (원문 미열람)
[^ref-374]: Open Robotics (open-rmf/rmf_ros2 GitHub), Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2, 미확인, https://github.com/open-rmf/rmf_ros2/issues/224, 접근일 2026-09-25 (원문 미열람)
[^ref-375]: Paul, T. C., Lertpongrujikorn, P., Nguyen, H. D., & Amini Salehi, M., Benchmarking Message Brokers for IoT Edge Computing: A Comprehensive Performance Study, 2026-03-23, https://arxiv.org/abs/2603.21600, 접근일 2026-09-25 (원문 미열람)
