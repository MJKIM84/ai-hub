---
title: "8. 실시간 세계 상태·데이터 일관성"
type: area
category: "B. 공통 정보·환경 모델"
area_no: 8
related_areas: [22, 7, 10, 9, 11, 15, 6, 19]
tags: [세계 상태, 정보 나이, 오래된 상태, 시각·품질 표시, 정정 이벤트, 디지털 섀도]
status: draft
confidence: low
created: 2026-09-24
updated: 2026-09-25
sources: [ref-004, ref-030, ref-031, ref-044, ref-045, ref-051, ref-148, ref-182, ref-183, ref-184, ref-185, ref-186, ref-187, ref-188, ref-189, ref-190, ref-191, ref-192, ref-193, ref-194, ref-195, ref-196]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [B. 공통 정보·환경 모델](index.md) › 8. 실시간 세계 상태·데이터 일관성

# 8. 실시간 세계 상태·데이터 일관성

!!! info "소속 대분류"
    [B. 공통 정보·환경 모델](index.md) — 핵심 질문:
    로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 [분류원문]

## 2. SCM 관점의 질문

문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? [분류원문]

> 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]

## 3. 왜 중요한가

확인한 로봇·설비 인터페이스는 상태에 시각을 붙이고 주기적으로 보내는 장치를 두지만 대상별로 얼마나 오래된 정보까지 믿을지는 정하지 않으므로, 이 위키는 ROP가 그 판단 규칙을 스스로 가져야 할 것으로 본다. [추정][^ref-031][^ref-184]

2절의 질문을 표준에 비춰 보면 빈 곳이 드러난다. VDA 5050 3.0.0 은 로봇 상태 메시지를 주문 수신·적재 변화·오류·운전 상태 변화 같은 사건이 생길 때와 적어도 30초마다 보내게 한다(2026-09-25 확인). [사실][^ref-031] 반면 Open-RMF 의 문 상태 메시지에는 시각·문 이름·현재 모드만 있고, 이번에 연 문·승강기 연동 문서 범위에서는 발행 주기나 오래된 상태를 판정하는 규칙을 찾지 못했다. [추정][^ref-184][^ref-185]

확인한 표준들로 볼 때, 30초 전의 '문 열림' 정보로 통과를 확정해도 되는지는 표준이 답하지 않으므로 ROP가 문·승강기 같은 대상마다 허용 경과 시간을 정하고, 넘으면 통과를 확정하기 전에 설비 어댑터에 다시 요청·확인하는 규칙을 가져야 할 것으로 보인다. [추정][^ref-183][^ref-188][^ref-189] 허용 경과 시간의 값을 정한 출처는 찾지 못했다(11절).

기록과 실물의 차이도 같은 문제다. DeHoratius·Raman(2008)은 한 소매업체 37개 매장의 재고 기록 약 37만 건을 조사해 65%가 실물과 맞지 않았다고 보고했으며, 이는 물류센터가 아니라 소매 매장 조건의 수치다. [사실][^ref-192] 이 연구로 볼 때 이 위키는 ROP의 화물 상태가 WMS(Warehouse Management System, 창고 관리 시스템) 기록을 그대로 참값으로 두지 말고, 로봇이 보고한 적재물 식별 같은 관측을 대조 근거로 함께 보관해 불일치를 드러내야 할 것으로 본다. [추정][^ref-192][^ref-051]

## 4. 핵심 개념과 용어

세계 상태의 값마다 '언제 성립했고 언제 기록됐는가', '얼마나 믿을 수 있는가', '틀렸을 때 어떻게 바로잡는가'를 함께 표현해야 할 것으로 보이며, 아래 용어는 확인한 표준·연구가 이를 표현하는 방식이다. [추정][^ref-045][^ref-182]

자세한 내용은 주제 페이지 [8. 실시간 세계 상태·데이터 일관성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area08-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

다음은 설명을 위한 가상의 시나리오이다.

**물류 흐름 단계:** 입고 → 적치

**시나리오:** 입고 판독을 마친 팔레트를 방화문과 화물 승강기를 거쳐 다른 층 보관 구역으로 옮긴다

| 항목 | 내용 |
|---|---|
| 시작 조건 | 입고 판독이 끝난 팔레트에 대해 상위 시스템이 적치 작업을 요청한다. 로봇 관제는 로봇 상태를 주문 수신 같은 사건 때와 적어도 30초마다 받는다. [사실][^ref-031] |
| 작업 대상 | 입고 팔레트. 입고 RFID 판독 스트림에는 놓친 판독과 잘못된 판독이 섞일 수 있다. [사실][^ref-194] 로봇 상태 메시지는 취급 중인 적재물(loads)을 담는다. [사실][^ref-051] |
| 수행 자원 | 이동로봇은 시각·위치·상태·문제 목록·배터리를 보고한다(Open-RMF API 기준). [사실][^ref-148] 문·승강기는 Open-RMF 구성에서 어댑터가 요청을 감독하며, 설비 자체 제어는 연계 대상이다. [사실][^ref-184][^ref-185] |
| 제약 | 문 상태는 시각·문 이름·현재 모드만 담고 [사실][^ref-186] 승강기 상태는 운영 모드와 제어권 세션 id 를 담는다. [사실][^ref-187] 이 위키는 대상별 허용 경과 시간을 넘은 상태로는 통과를 확정하지 않는 규칙이 필요할 것으로 본다. [추정][^ref-183][^ref-188] |
| 완료·인계 | 적치 완료는 사건이 일어난 시각과 기록된 시각을 나눠 남길 수 있다(EPCIS 방식). [사실][^ref-045] 잘못 보고된 완료는 덮어쓰지 않고 정정 기록을 덧붙이는 편이 추적에 유리할 것으로 보인다. [추정][^ref-045][^ref-044] |
| 예외·성과 | 로봇 연결이 예기치 않게 끊기면 MQTT 브로커가 CONNECTION_BROKEN 을 대신 발행한다(VDA 5050). [사실][^ref-031] 처리량·시간·비용 영향을 잰 자료는 미확인이다. |

로봇이 방화문 앞에 도착했을 때 ROP가 가진 문 상태에는 시각만 붙어 있다. 그 시각이 허용 경과 시간을 넘었다면, 이 위키가 제안하는 규칙에 따라 ROP는 통과를 확정하기 전에 문 어댑터에 다시 요청하고 새 상태를 확인한다. [추정][^ref-184][^ref-189] 승강기에서는 제어권 세션을 받은 뒤에만 층간 이동을 진행한다. [추정][^ref-187]

적치 완료 보고가 도착하면 ROP는 로봇이 보고한 적재물 식별과 입고 판독 결과를 대조한다. 둘이 어긋나면 기존 기록을 지우지 않고 불일치와 정정 근거를 함께 남겨, 뒤에 인계 분쟁이 생겨도 원 기록을 추적할 수 있게 하는 것이 이 위키의 제안이다. [추정][^ref-051][^ref-045]

## 6. 대표 접근법과 기술

확인한 자료 가운데 Eclipse Sparkplug 는 오래된 상태의 처리 규칙을 명시한다: 호스트 애플리케이션은 에지 노드의 NDEATH 를 받거나 MQTT 서버와 연결을 잃으면 관련 측정값을 모두 STALE 로 표시하고, 0~255 순번(seq)으로 순서 뒤바뀜을 감지해 재정렬 대기 시간이 지나도 빠진 메시지가 오지 않으면 재탄생(Rebirth) 요청으로 전체 상태를 다시 받는다. [사실][^ref-188]

자세한 내용은 주제 페이지 [8. 실시간 세계 상태·데이터 일관성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area08-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

세계 상태의 시각·품질·연결 상태를 표현하는 방식은 로봇 관제·설비 연동·메시지 계층·사건 기록 표준마다 다르며, 아래 표는 이번에 확인한 범위를 정리한다. [사실][^ref-031][^ref-188]

자세한 내용은 주제 페이지 [8. 실시간 세계 상태·데이터 일관성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area08-s7.md)에 있다.

## 8. 대표 연구와 자료

세계 상태의 신선도·기록 정확도·판독 오류·복제 일관성을 다룬 연구가 이 영역의 대표 자료이며, 대부분 원문을 열지 못해 검색 요약 범위에서 확인했다. [사실][^ref-189][^ref-192]

자세한 내용은 주제 페이지 [8. 실시간 세계 상태·데이터 일관성 — 대표 연구와 자료](../../topics/2026/2026-09-25-area08-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

이 위키는 ROP의 직접 범위를 로봇 관제 인터페이스의 로봇 상태, 설비 어댑터의 문·승강기 상태, EPCIS 같은 업무 이벤트를 시각·품질 정보와 함께 하나의 세계 상태로 모으고 불일치를 드러내는 일로, 설비 자체 제어와 센서 융합은 외부에 맡기는 경계로 본다. [추정][^ref-031][^ref-184][^ref-045]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 보고한 위치추정 여부·품질 점수·편차 범위와 보고 시각을 받아 그 위치를 얼마나 믿을지 판단한다. [추정][^ref-051] | 연계 대상: 위치추정과 그 품질 계산, 센서 인식 |
| 시설·설비 제어 | 문·승강기 상태 확인, 사용 요청, 인계 확인, 허용 경과 시간을 넘은 상태의 재요청·확인을 맡는다. [추정][^ref-184][^ref-185] | 연계 대상: 문·승강기 자체 제어와 설비 안전 제어 |
| 상위 업무 시스템 | WMS 기록과 로봇 관측의 불일치를 드러내고 정정 기록을 덧붙여 보관한다. [추정][^ref-192][^ref-045] | 연계 대상: 전사 재고정책 |

문·승강기 어댑터가 요청을 감독하는 구조는 Open-RMF 의 구성이다. [사실][^ref-184][^ref-185] 이 위키는 이를 ROP가 설비를 직접 제어한다는 뜻으로 보지 않고, ROP의 몫을 상태 확인·요청·인계로 한정한다. [추정][^ref-184][^ref-185] 경계가 제품 전략에 따라 이동할 수 있다는 전제는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역과 22. 시뮬레이션·예측용 디지털 트윈의 구분은 2절의 원문 주석을 따르며, Kritzinger 외(2018)의 디지털 섀도 분류와 NIST 해설이 전하는 ISO 23247 의 '동기화된 표현' 정의로 볼 때 이 영역의 현재 상태 표현은 현장에서 자동 갱신되는 표현에 가깝고 그 표현을 복제해 가정한 미래를 실험하는 쪽은 22. 시뮬레이션·예측용 디지털 트윈의 몫으로 나누는 것이 원문 구분과 맞을 것으로 보인다. [추정][^ref-191][^ref-190]

자세한 내용은 주제 페이지 [8. 실시간 세계 상태·데이터 일관성 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area08-s10.md)에 있다.

## 11. 열린 질문

이 영역에서 새로 제기한 질문 4건과 이미 이 영역에 걸린 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [8. 실시간 세계 상태·데이터 일관성 — 열린 질문](../../topics/2026/2026-09-25-area08-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-09-25
[^ref-045]: GS1, gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25
[^ref-182]: OPC Foundation, OPC Unified Architecture – Part 4: Services - 7.11 DataValue, 미확인, https://reference.opcfoundation.org/specs/OPC-10000-4/7.11, 접근일 2026-09-25 (원문 미열람)
[^ref-183]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-09-25
[^ref-184]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-09-25
[^ref-185]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25
[^ref-186]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorState.msg, 접근일 2026-09-25
[^ref-187]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-188]: Eclipse Foundation (eclipse-sparkplug GitHub), Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc), 미확인, https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc, 접근일 2026-09-25
[^ref-189]: Yates, R. D., Sun, Y., Brown, D. R., Kaul, S. K., Modiano, E., & Ulukus, S., Age of Information: An Introduction and Survey, 2021-05, https://arxiv.org/abs/2007.08564, 접근일 2026-09-25 (원문 미열람)
[^ref-190]: NIST, DIGITAL TWINS FOR ADVANCED MANUFACTURING: THE STANDARDIZED APPROACH, 미확인, https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417, 접근일 2026-09-25 (원문 미열람)
[^ref-191]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-09-25 (원문 미열람)
[^ref-192]: DeHoratius, N., & Raman, A., Inventory Record Inaccuracy: An Empirical Analysis, 2008, https://pubsonline.informs.org/doi/10.1287/mnsc.1070.0789, 접근일 2026-09-25 (원문 미열람)
[^ref-194]: Massawe, L. V. 외(Sensors), Reducing False Negative Reads in RFID Data Streams Using an Adaptive Sliding-Window Approach, 2012, https://doi.org/10.3390/s120404187, 접근일 2026-09-25 (원문 미열람)
