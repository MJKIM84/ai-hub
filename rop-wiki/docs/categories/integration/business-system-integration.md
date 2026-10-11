---
title: "23. 업무 시스템 연동"
type: area
category: "F. 연동"
area_no: 23
related_areas: [12, 20, 21, 22, 24, 25, 26, 29, 30, 32, 38, 44, 61, 62, 63]
tags: [주문 갱신, 작업 취소, 출고 우선순위, ISA-95, VDA 5050, Open-RMF]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-10-11
sources: [ref-002, ref-031, ref-111, ref-125, ref-126, ref-127, ref-128, ref-129, ref-130, ref-131, ref-132, ref-133, ref-134, ref-135, ref-136, ref-137, ref-869, ref-1341, ref-1441, ref-1445, ref-1446, ref-1447, ref-1448, ref-1449, ref-1450, ref-1451, ref-1452, ref-1453, ref-1454]
last_run: 2026-10-11
version: 3
---

[홈](../../index.md) › [F. 연동](index.md) › 23. 업무 시스템 연동

# 23. 업무 시스템 연동

!!! info "소속 대분류"
    [F. 연동](index.md) — 핵심 질문:
    제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 3 · 마지막 갱신: 2026-10-11 · 마지막 실행: 2026-10-11
<!-- auto:page-status:end -->

## 1. 한 줄 정의

업무 요청을 받아 작업으로 바꾸고, 진행·완료를 되돌려 반영한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **업무 요청 수신·작업 변환**: 작업 요청을 만드는 업무 시스템(ERP·WMS·MES·병원 정보 시스템·호텔 객실 관리·빌딩 관리 등)에서 요청을 받아 로봇 작업으로 바꾼다
- **진행·완료 반영과 요청 변경 처리**: 작업 진행·완료를 업무 시스템에 되돌려 반영하고, 요청의 우선순위 변경·취소를 진행 중인 로봇 작업에 반영한다

이전 분류(2026-09-24)에서 이 페이지는 옛 1번 영역 ‘주문·업무 시스템 연계’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 [옛 분류원문]

> 옛 질문: 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? [옛 분류원문]

## 2. 핵심 질문

업무 시스템의 요청이 바뀌거나 취소되면 진행 중인 로봇 작업을 어떻게 바꿀 것인가? [분류원문]

## 3. 왜 중요한가

로봇 관제 인터페이스 표준인 VDA 5050 3.0.0은 관제(fleet control)와 이동로봇 사이의 통신만 다루고, 외부 IT 시스템 같은 다른 인터페이스와 교통 관리 로직은 범위 밖에 둔다(2026-09-25 확인). [사실][^ref-031] 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 왜 중요한가 (2026-09-25)](../../topics/2026/2026-09-25-area01-s3.md) — 그 페이지의 GreenAuto(Lopes 외) REST·MQTT 서술은 2026-10-11 정정 대상이며, 정정 내용은 아래 소절에 있다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 왜 중요한가](../../topics/2026/2026-10-11-area23-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역을 읽는 데 필요한 용어는 로봇 쪽의 주문·작업 표현과 상위 시스템 쪽의 작업 지시 표현으로 나뉜다. 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 핵심 개념과 용어 (2026-09-25)](../../topics/2026/2026-09-25-area01-s4.md) — 그 페이지의 ref-131 '원문 미열람'·'상태 전이는 원문 미열람' 표시는 2026-10-11 원문 확인으로 해제 대상이며, 확인 내용은 아래 소절에 있다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 핵심 개념과 용어](../../topics/2026/2026-10-11-area23-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 첫 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 2026-10-11 실행에서 병원·제조 공장 사례와 물류창고 개념검증 사례를 그 뒤에 더했다.

**물류 흐름 단계:** 피킹 → 출하

**시나리오:** 출하 마감이 당겨진 주문 때문에 진행 중인 피킹 운반 작업을 바꾼다

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 시스템(WMS·WES)이 운송 마감이 당겨진 출고 주문의 우선순위를 올리고 변경을 ROP에 보낸다. B2MML 거래 프로파일은 CHANGE·CANCEL 같은 거래 동사를, OPC UA for ISA-95 Job Control 은 Update·Pause·Abort 같은 메서드를 정의한다. [사실][^ref-129][^ref-130] 창고 상위 시스템의 변경이 이런 형태로 올 수 있을 것으로 보인다. [추정][^ref-129][^ref-130] |
| 작업 대상 | 피킹된 토트·박스와 이를 실은 AMR 운반 작업 |
| 수행 자원 | 작업자가 피킹하고 AMR 이 운반하는 협업 구성(동적 주문 피킹 연구의 설정과 같다). [사실][^ref-132] ROP는 작업을 조정하고 제조사 관제가 로봇을 움직인다. |
| 제약 | VDA 5050 에서는 이미 공개된 base 구간을 바꿀 수 없고 [사실][^ref-031], 진행 중에 다른 orderId 의 새 주문을 보내면 로봇이 OTHER_ORDER_ACTIVE 로 거부한다. [사실][^ref-031] 주문 메시지에서 우선순위 필드는 확인되지 않았다. [추정][^ref-031] |
| 완료·인계 | 로봇 쪽 작업 상태(completed·canceled 등)를 받아 상위 시스템에 완료·취소 결과를 되돌려야 업무 완료로 인정한다. Open-RMF 작업 상태는 이런 상태 값과 취소·중단 정보를 담는다. [사실][^ref-111] |
| 예외·성과 | cancelOrder 를 보내도 취소할 수 없는 동작은 끝날 때까지 계속된다. [사실][^ref-031] 이미 화물을 실은 뒤라면 되돌림 작업이 추가로 필요할 것으로 보인다. [추정][^ref-031][^ref-129] 진행 중 사이클 수정은 완료 시간을 줄일 수 있지만 교란 비용을 조건으로 판단해야 할 것으로 보인다. [추정][^ref-132][^ref-133] |

다음은 설명을 위한 가상의 시나리오이다. 오후 운송 마감이 앞당겨진 주문이 생기자 WMS가 그 주문의 우선순위를 올린다. 해당 주문의 박스를 실은 AMR 은 이미 다른 주문의 포장대로 향하고 있고, 새 주문을 따로 보내면 거부되므로 ROP는 공개되지 않은 경로 구간을 주문 갱신으로 바꾸거나, 일시정지 후 취소하고 다시 지시하는 방법 가운데 하나를 골라야 한다.

어느 쪽을 고를지는 로봇 인터페이스가 정해 주지 않는다. 출고 우선순위가 바뀔 때 어떤 작업을 끊고 무엇을 먼저 할지 정하는 규칙은 ROP 쪽 작업 대기열·재계획 로직이 맡아야 할 것으로 보인다. [추정][^ref-031][^ref-125]

국내에서는 2025년 1월 테크타카가 자사 WMS 와 플로틱의 오더 피킹용 자율주행로봇 30대를 연동하는 자동화 모델을 남이천 물류센터에서 실증하는 협력을 발표했다고 보도됐다. 이는 협력 발표이며 실증 결과는 미확인이다. [사실][^ref-137] 같은 사건의 1차 출처인 아르고(테크타카)의 2025-01-21 업체 발표는 자사 WMS 와 플로틱 자율주행로봇을 연동한 자동화 모델을 설계해 남이천 물류센터에서 실증하고, 플로틱이 오더 피킹 특화 로봇 30대를 지원한다고 밝혔다. [추정] 업체 발표[^ref-1450] 같은 발표에서 플로틱 대표가 말한, 수작업으로 20분 이상 걸리던 오더 피킹을 10분 이내로 줄였다는 성과는 앞선 실증사업에 대한 업체 주장이며 남이천 30대 사업의 성과가 아니고 측정 조건도 공개되지 않았다. [추정] 벤더 주장[^ref-1450] 남이천 실증의 시험 기간과 결과는 여전히 미확인이다.

### 병원: 검사실 도착 뒤 인수 확인을 거쳐 로봇을 되돌림

**현장 유형:** 병원

**사례:** Tartu 대학병원에서 ICU 시료를 검사실로 운반한 뒤, 직원의 인수 확인을 거쳐 로봇을 ICU 로 되돌림

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(이번에 확인한 범위는 검사실 도착 뒤 단계이며, 운반 요청이 어디서 어떻게 만들어지는지는 이번 브리프에서 확인하지 않았다) |
| 작업 대상 | ICU 에서 검사실로 옮긴 시료와, 시료를 꺼낸 뒤 비게 되는 로봇의 운반함 [사실][^ref-869] |
| 수행 자원 | PAL Robotics TIAGo 1대가 운반하고, 검사실 직원이 화면 버튼으로 확인하며, [인제스터](../../glossary/dispenser-ingestor.md)가 Open-RMF 에 인수 완료를 알린다. TIAGo·Clearpath Jackal 두 이기종 로봇을 RMF 로 관리하는 능력은 별도 시험 환경에서 검증했고, 병원 안에는 여러 배송 로봇을 아직 적용하지 않았다. [사실][^ref-869] |
| 제약 | 미확인(이번 브리프에서 시간·구역·권한 제약을 확인하지 않았다) |
| 완료·인계 | 직원이 시료를 모두 꺼냈음을 화면 버튼으로 확인하고 인제스터가 RMF 에 인수 완료를 알린 뒤에야, 로봇을 ICU 로 되돌리는 요청이 나간다. [사실][^ref-869] |
| 예외·성과 | 미확인 |

이 실증은 로봇이 검사실에 도착한 것과 사람이 시료를 인수한 것을 서로 다른 단계로 두고, 인수 확인을 다음 작업(복귀)의 조건으로 썼다. [사실][^ref-869] 업무 시스템 연동에서 운반 완료와 업무상 인수 확정을 나눠 다루는 해외 사례이며, 국내 기준은 미확인이다(oq-012). 병원 안 운반은 로봇 1대로 했으므로 병원 내 이기종 플릿 상시 운영 사례로 볼 수 없다.

### 제조 공장: 입고부터 출하까지 생산 물류 조율

**현장 유형:** 제조 공장

**사례:** HD현대일렉트릭 청주 배전캠퍼스 신공장의 생산 물류 자동화

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(생산계획 변경을 작업으로 바꾸는 승인 규칙은 공개되지 않았다) |
| 작업 대상 | 자재 입고·보관·생산라인 공급·완제품 이송·출하로 이어지는 공장 안 물류 [추정] 벤더 주장[^ref-1451] |
| 수행 자원 | AMR·ACR 같은 물류 로봇과 이를 조율하는 창고 제어 시스템(WCS)·SCADA 기반 통합 제어·관제. WCS·SCADA 의 설비 제어·관제는 연계 대상이다. [추정] 벤더 주장[^ref-1451] |
| 제약 | 미확인(다제조사 수·API·주문 상관키는 공개되지 않았다) |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(공급자가 제시한 성과 수치는 채택하지 않았다) |

LG CNS 고객 사례(2026-07-16)는 신공장의 입고부터 출하까지 생산 물류를 WCS 와 SCADA 기반 통합 관제로 조율했다고 설명하는 공급자 단독 설명이다. [추정] 벤더 주장[^ref-1451] 이 영역에서는 생산 물류를 실행 작업으로 조율하는 제조 공장 사례로만 보고, WCS·SCADA 의 설비 제어·관제는 [22. 설비·건물 시스템 연동](facility-and-building-system-integration.md)과 [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)의 연계 대상으로 둔다.

### 물류창고: 업무 시스템 문맥을 받는 휴머노이드 개념검증

**현장 유형:** 물류창고

**사례:** Bosch·Aimbo 개념검증에서 SAP EWM 의 업무 문맥을 받아 창고 작업을 수행

| 항목 | 내용 |
|---|---|
| 시작 조건 | SAP EWM 의 배송 정보·주문 우선순위·보관 위치가 실시간 업무 문맥으로 로봇에 전달된다. [추정] 벤더 주장[^ref-1453] |
| 작업 대상 | 창고 작업(구체 품목과 작업 단위는 미확인) |
| 수행 자원 | Aimbo 의 휴머노이드 Anigon 1대. 파지 같은 물리 작업 수행은 로봇 자체 지능·제어의 연계 대상이다. [추정] 벤더 주장[^ref-1453] |
| 제약 | 탐색 단계의 개념검증으로, 전용 beta·test 시스템 환경에서 검증됐다. [추정] 벤더 주장[^ref-1453] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

SAP 뉴스(2025-11-05 게시)가 소개한 Bosch·Aimbo 공동 개념검증은 단일 Anigon 으로 beta·test 환경에서 검증한 탐색 단계 사업이며, 실시일과 생산 운영 전환 여부는 미확인이다. [추정] 벤더 주장[^ref-1453] 이 영역에서는 업무 시스템의 업무 객체를 로봇 작업 문맥으로 넘기는 해석 계층의 예로만 보고, 휴머노이드의 작업 수행 방식은 [44. 로봇 기반 모델·언어 모델 계획](../ai-and-learning/robot-foundation-models-and-llm-planning.md)에서 다룬다.

## 6. 대표 접근법과 기술

로봇 인터페이스가 제공하는 변경 수단은 주문 갱신·일시정지·취소·중단·되감기 정도이므로, 우선순위 변경 규칙과 상위 지시의 번역은 ROP 쪽 대기열·재계획 로직이 맡아야 할 것으로 보인다. [추정][^ref-031][^ref-125] 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 대표 접근법과 기술 (2026-09-25)](../../topics/2026/2026-09-25-area01-s6.md) — 그 페이지에 VDA 5050 변경 수단과 Open-RMF 중단·되감기 같은 기존 확인 내용이 있다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area23-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이번 조사에서 확인한 관련 규격은 로봇 쪽 VDA 5050 3.0.0·Open-RMF 작업 API, 상위 쪽 B2MML·OPC UA for ISA-95 Job Control·ISA-95 Part 1, 업무 범위 쪽 SCOR DS 이다. [사실][^ref-031][^ref-129]

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area23-s7.md)에 있다.

## 8. 대표 연구와 자료

이번 조사에서 확인한 자료는 동적 주문 피킹 연구와 웨이브리스 출고 지시 연구, 다제조사 플릿 관리 사례, 국내 WMS–로봇 연동 발표이다. [사실][^ref-132][^ref-134] 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 대표 연구와 자료 (2026-09-25)](../../topics/2026/2026-09-25-area01-s8.md) — 그 페이지의 GreenAuto(Lopes 외) REST·MQTT 서술은 2026-10-11 정정 대상이며, 정정 내용은 아래 항목에 있다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 대표 연구와 자료](../../topics/2026/2026-10-11-area23-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 우선순위·시작 시각·마감을 담은 작업 요청을 받아 로봇 작업으로 바꾸고, 진행 중 작업의 재정렬·수정 규칙을 적용하며, 진행·완료·취소 결과를 되돌린다 [추정][^ref-135][^ref-002][^ref-125] | 주문 접수, 출고 지시 방식(웨이브·웨이브리스), 출고 우선순위 결정(ERP·WMS·WES) |
| 상위 업무 시스템(요청 변경·결과 보고) | 취소 요청의 응답과 별도로 작업 상태를 관측해 실제 취소 결과를 확인하고 되돌린다 [추정][^ref-1445][^ref-1446] | 우선순위 변경을 허용하는 작업 상태·권한과 대기 큐 정렬 규칙(예: Ready·Held·Created 상태 제한, LSD 정렬) [추정] 벤더 주장[^ref-1448][^ref-1449] |
| 로봇 자체 지능·제어 | 제조사 관제에 주문 갱신·일시정지·취소·재지시를 보내고 상태·실패·완료를 확인한다 | 주행·정지와 동작의 실제 실행, 취소할 수 없는 동작의 수행 |
| 로봇 자체 지능·제어(휴머노이드 작업) | 업무 객체(주문 우선순위·보관 위치)를 작업 문맥으로 넘기는 해석 계층 | 파지 같은 물리 작업 수행 [추정] 벤더 주장[^ref-1453] |
| 시설·설비 제어 | 생산 물류 작업의 요청·상태 확인과 결과 반영 | WCS·SCADA 기반 설비 제어·관제(제조 공장 사례) [추정] 벤더 주장[^ref-1451] |
| 업종별 조건 | 로봇 도착 통지와 수령인의 인수 확인을 서로 다른 완료 단계로 받는다. 근거 사례: Tartu 대학병원 실증은 직원 확인과 인제스터의 인수 완료 통지 뒤에야 복귀 요청을 냈다 [사실][^ref-869] | 의료 등 업종별 전문 요구사항 |

연계 대상: 주문 접수·출고 지시 방식과 출고 우선순위 결정은 ERP·WMS·WES 같은 상위 업무 시스템의 몫이고, ROP는 그 결과를 작업 요청의 우선순위·시작 시각·마감 제약으로 받아 로봇 작업으로 바꾸고 결과를 되돌리는 경계에 서는 것으로 보인다. [추정][^ref-135][^ref-134][^ref-002][^ref-125] VDA 5050 은 외부 IT 인터페이스를 범위 밖에 둔다. [사실][^ref-031] 따라서 상위 시스템과의 번역 계층은 ROP 쪽 인터페이스 설계 과제가 될 것으로 보인다. [추정][^ref-031]

구축자 의견: 업무 시스템–관제 인터페이스를 비교할 때는 접수 응답, 진행 통지(콜백·상태), 취소 결과, 업무 확정을 따로 보는 것이 좋아 보인다. [의견][^ref-1447][^ref-1441][^ref-1445] 우선순위 변경 허용 범위는 WMS 쪽 규칙이므로 ROP 는 그 결과를 받는 쪽에 서고, 제조 공장의 WCS·SCADA 관제는 [22. 설비·건물 시스템 연동](facility-and-building-system-integration.md)·[38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)의 연계 대상으로 둔다. 대화형 접점인 [모델 컨텍스트 프로토콜](../../glossary/model-context-protocol.md)(Model Context Protocol, MCP)의 도구 범위와 업무 요구의 차이는 [23. 업무 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area23-s6.md)에 적었다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자세한 기준은 [범위 경계](../../about/scope-boundary.md) 페이지에 있으며, 이종 제조사를 연결하는 ROP라면 로봇 동작 실행은 제조사에 맡기고 변경 지시의 번역과 결과 확인을 맡는 구도가 된다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md) — ISA-95 작업 지시와 Open-RMF 작업 상태를 업무 단계와 잇는 문제를 함께 다루며, 같은 출처(작업 상태 스키마, task_new)를 공유한다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 다른 연구영역과의 연결](../../topics/2026/2026-10-11-area23-s10.md)에 있다.

## 11. 열린 질문

2026-09-25 실행에서 새로 열린 질문 세 개는 [열린 질문](../../open-questions.md) 목록의 oq-019(출고 우선순위 재정렬 설계), oq-020(상위 작업 지시와 로봇 인터페이스 사이 매핑), oq-021(적재 후 취소의 되돌림 규칙)이다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 열린 질문](../../topics/2026/2026-10-11-area23-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-10-11 · 갱신 · [23. 업무 시스템 연동](business-system-integration.md) — 차등 갱신: 3·8절 GreenAuto(Lopes 외) REST·MQTT·VDA 5050 연동을 계획(미가동)으로 정정·ref-136 서지 정정; 4절 OPC Job Control 2.00.0 갱신·취소·정지·Completed/Closed 조건(원문 확인, 트랙 반영 제안 3 일부); 5절 국내 문단 1차 출처 병기와 병원·제조 공장·물류창고 사례 추가; 6절 응답·취소 결과 분리, SAP 폐기 FMS API, WMS 우선순위 규칙(연계 대상), 업무 객체 해석, MCP 접점 범위; 7절 표 추가; 9절 경계 행 추가·MCP 첫 등장 풀어쓰기; 10절 연결 8건 추가; 11절 부분 근거·새 질문 3건; 3·4·6·7·8·11절에 2026-09-25 주제 페이지 링크 복원(2차 수정); 13절 각주 갱신 (실행 2026-10-11-02)
- 2026-10-11 · 생성 · [23. 업무 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area23-s6.md) — 자동 분리: 23. 업무 시스템 연동 의 "6. 대표 접근법과 기술" 절(3,712자)을 옮겼다 (실행 2026-10-11-02)
- 2026-10-11 · 생성 · [23. 업무 시스템 연동 — 열린 질문](../../topics/2026/2026-10-11-area23-s11.md) — 자동 분리: 23. 업무 시스템 연동 의 "11. 열린 질문" 절(2,250자)을 옮겼다 (실행 2026-10-11-02)
- 2026-10-11 · 생성 · [23. 업무 시스템 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area23-s7.md) — 자동 분리: 23. 업무 시스템 연동 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,793자)을 옮겼다 (실행 2026-10-11-02)
- 2026-10-11 · 생성 · [23. 업무 시스템 연동 — 대표 연구와 자료](../../topics/2026/2026-10-11-area23-s8.md) — 자동 분리: 23. 업무 시스템 연동 의 "8. 대표 연구와 자료" 절(1,623자)을 옮겼다 (실행 2026-10-11-02)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-002]: ISA, Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems, 2025-04-10, https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of, 접근일 2026-09-25 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25
[^ref-129]: MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd, 접근일 2026-09-25
[^ref-130]: OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv), 2024-01-31, https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL, 접근일 2026-09-25
[^ref-132]: Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations, 2025, https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231, 접근일 2026-09-25 (원문 미열람)
[^ref-133]: Lorenz, Otto, & Gendreau (Networks, Wiley), Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization?, 2025-05, https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281, 접근일 2026-10-11
[^ref-134]: Gallien, J., & Weber, T. G., To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter, 2010, https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291, 접근일 2026-09-25 (원문 미열람)
[^ref-135]: ASCM, SCOR Digital Standard — Introduction and Front Matter (SCOR Version 14.0, 2025), 2025, https://www.ascm.org/globalassets/ascm_website_assets/docs/scor/intro-and-front-matter-scor-digital-standard-2025.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-137]: 머니투데이, 물류센터 관리시스템에 로봇 연동…"물류 자동화 새 표준 만든다", 2025-01, https://news.mt.co.kr/mtview.php?no=2025012116183583251, 접근일 2026-09-25 (원문 미열람)
[^ref-869]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-10-11
[^ref-1441]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/dispatch_task_response.json, 접근일 2026-10-11
[^ref-1445]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/cancel_task_response.json, 접근일 2026-10-11
[^ref-1446]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/simple_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/simple_response.json, 접근일 2026-10-11
[^ref-1447]: SAP, APIs for Integration via Fleet Management Systems (API for Integration with Fleet Management Systems (Deprecated); LATEST URL, 확보본 2024-07-10 기준), 2024-07-10, https://help.sap.com/doc/a02ad3695d5845fca1678810cb83562b/LATEST/en-US/379d6d880e5d4007b3751618080da80f_1.pdf, 접근일 2026-10-11
[^ref-1448]: Oracle, WMS REST API Guide — Change Priority (Oracle Warehouse Management Cloud 26c), 2026-08-14, https://docs.oracle.com/en/cloud/saas/warehouse-management/26c/owmre/change-priority.html, 접근일 2026-10-11
[^ref-1449]: SAP, End-User Information for Integration via Integration Services (SAP Warehouse Robotics, Document Version 2308; LATEST URL, 판 2308 기준), 2023-08-19, https://help.sap.com/doc/f08ea8f8686c46e89f1d7ed121f19d68/LATEST/en-US/b82aa9c86bd74777b86ec7f5766252d0.pdf, 접근일 2026-10-11
[^ref-1450]: 아르고 풀필먼트(테크타카), 아르고, 플로틱과 로봇 기반 물류 생산성 향상 실증 본격 실시, 2025-01-21, https://blog.argoport.com/pr-robotcooperation250121, 접근일 2026-10-11
[^ref-1451]: LG CNS, 로봇 기반 물류 자동화와 통합 관제로 HD현대일렉트릭 신공장의 새로운 운영 체계를 구축하다, 2026-07-16, https://www.lgcns.com/kr/moa/customer-story/detail.smartlogistics-robotic-logistics-2607-1, 접근일 2026-10-11
[^ref-1453]: SAP (Lukasz Ostrowski, SAP News Center), How SAP Brings Business AI into the Physical World: New Robotics Pilots Across Warehouse, Manufacturing, and Inspection Use Cases, 2025-11-05, https://news.sap.com/2025/11/sap-physical-ai-partnerships-new-robotics-pilots/, 접근일 2026-10-11
