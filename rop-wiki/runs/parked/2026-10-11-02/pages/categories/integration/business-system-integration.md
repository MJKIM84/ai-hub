---
title: "23. 업무 시스템 연동"
type: area
category: "F. 연동"
area_no: 23
related_areas: [12, 20, 21, 22, 24, 25, 26, 29, 30, 32, 38, 44, 61, 62, 63]
tags: [주문 갱신, 작업 취소, 취소 결과 통지, 출고 우선순위, ISA-95, Open-RMF]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-10-11
sources: [ref-002, ref-031, ref-111, ref-125, ref-129, ref-130, ref-131, ref-132, ref-133, ref-134, ref-135, ref-136, ref-137, ref-869, ref-1341, ref-1453, ref-1454, ref-1455, ref-1456, ref-1457, ref-1458, ref-1459, ref-1460, ref-1461, ref-1462, ref-1463]
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
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
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

로봇 관제 인터페이스 표준인 VDA 5050 3.0.0은 관제(fleet control)와 이동로봇 사이의 통신만 다루고, 외부 IT 시스템 같은 다른 인터페이스와 교통 관리 로직은 범위 밖에 둔다(2026-09-25 확인). [사실][^ref-031] 그래서 ERP·WMS·MES 같은 상위 시스템의 주문과 변경을 로봇 작업으로 옮기는 일은 로봇 표준이 대신해 주지 않는다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 왜 중요한가](../../topics/2026/2026-10-11-area23-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역을 읽는 데 필요한 용어는 로봇 쪽의 주문·작업 표현과 상위 시스템 쪽의 작업 지시 표현으로 나뉜다. 업무 시스템 약어는 [WES·WCS·WMS·MES·TMS](../../glossary/wes-wcs-wms-mes-tms.md)를 참고한다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 핵심 개념과 용어](../../topics/2026/2026-10-11-area23-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

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

**국내 사례(현장 유형: 물류창고).** 국내에서는 2025년 1월 테크타카가 자사 WMS 와 플로틱의 오더 피킹용 자율주행로봇 30대를 연동하는 자동화 모델을 남이천 물류센터에서 실증하는 협력을 발표했다고 보도됐다. 이는 협력 발표이며 실증 결과는 미확인이다. [사실][^ref-137] 1차 출처인 아르고(테크타카)의 2025-01-21 공식 발표는 자사 WMS 와 플로틱 자율주행로봇을 연동한 자동화 모델을 설계해 남이천 물류센터에서 실증하고, 수행 자원으로 플로틱이 오더 피킹 특화 로봇 30대를 지원한다고 밝힌다. [추정][^ref-1459] 같은 발표에서 플로틱 대표는 앞선 실증사업에서 수작업으로 20분 이상 걸리던 오더 피킹을 10분 이내로 줄였다고 말했으나, 이는 앞선 실증의 성과이며 남이천 30대 사업의 결과가 아니고 측정 조건도 공개되지 않았다. [추정] 벤더 주장[^ref-1459]

**현장 유형:** 제조 공장

**사례:** 신공장의 자재 입고부터 완제품 출하까지 공장 물류를 창고 제어 시스템으로 조율 (HD현대일렉트릭 청주 배전캠퍼스, 공급자 설명)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 공개 자료에서 확인되지 않음(생산계획 변경 승인 규칙 미공개) |
| 작업 대상 | 자재 입고·보관, 생산라인 공급, 완제품 이송·출하로 이어지는 공장 물류 [추정] 벤더 주장[^ref-1460] |
| 수행 자원 | AMR·ACR·디팔레타이징 로봇과, 이를 조율하는 창고 제어 시스템(Warehouse Control System, WCS)·SCADA(감시 제어·데이터 수집) 기반 통합 관제 [추정] 벤더 주장[^ref-1460] |
| 제약 | 공개 자료에서 확인되지 않음 |
| 완료·인계 | 공개 자료에서 확인되지 않음 |
| 예외·성과 | 공개 자료에서 확인되지 않음(공급자 설명의 성과 수치는 채택하지 않음) |

LG CNS 는 2026-07-16 고객 사례에서 HD현대일렉트릭 청주 배전캠퍼스 신공장에 자재 입고·보관·생산라인 공급·완제품 이송·출하를 조율하는 WCS 와 SCADA 기반 통합 관제를 구축했다고 설명하지만, 연결한 제조사 수·API·주문 상관키·생산계획 변경 승인 규칙은 공개하지 않는다. [추정] 벤더 주장[^ref-1460] WCS·SCADA 를 통한 설비 제어와 통합 관제는 이 영역의 연계 대상이며([22. 설비·건물 시스템 연동](facility-and-building-system-integration.md), [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)), 여기서는 생산 쪽 요청을 실행 작업으로 조율하는 역할의 예로만 본다.

**현장 유형:** 병원

**사례:** 병원에서 중환자실(Intensive Care Unit, ICU) 시료를 검사실로 운반한 뒤 인수 확인을 거쳐 로봇을 복귀시킴 (Tartu 대학병원 현장 시험)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 이번 조사에서 다루지 않음 |
| 작업 대상 | 이번 조사에서 다루지 않음 |
| 수행 자원 | 병원 안 운반 실증은 PAL Robotics TIAGo 1대로 했고, TIAGo·Clearpath Jackal 두 이기종 로봇을 RMF(Open-RMF)로 관리하는 능력은 별도 시험 환경에서 검증했으며, 병원 안에는 여러 배송 로봇을 아직 적용하지 않았다. [사실][^ref-869] |
| 제약 | 이번 조사에서 다루지 않음 |
| 완료·인계 | 로봇이 검사실에 도착하면 직원이 화면 버튼으로 시료를 모두 꺼냈음을 확인하고, [인제스터(디스펜서·인제스터)](../../glossary/dispenser-ingestor.md)가 RMF 에 인수 완료를 알린 뒤에야 로봇을 ICU 로 되돌리는 요청이 나간다. [사실][^ref-869] |
| 예외·성과 | 이번 조사에서 다루지 않음 |

이 현장 시험(2022-08-23 발행 논문)에서 로봇의 도착은 곧 업무 완료가 아니었다. 도착 뒤 사람의 인수 확인이 인제스터를 거쳐 관제에 전달돼야 다음 요청이 나갔으므로, 도착 확인과 업무상 인수 확인을 별도 단계로 둔 예다. [사실][^ref-869] 해외 병원 한 곳의 시험이며, 국내 물류센터의 입고·인수 확정 기준은 [열린 질문](../../open-questions.md) oq-012 로 남아 있다.

## 6. 대표 접근법과 기술

로봇 인터페이스가 제공하는 변경 수단은 주문 갱신·일시정지·취소·중단·되감기 정도이므로, 우선순위 변경 규칙과 상위 지시의 번역은 ROP 쪽 대기열·재계획 로직이 맡아야 할 것으로 보인다. [추정][^ref-031][^ref-125] 아래는 이번 조사에서 확인한 수단과 연구 접근이다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area23-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이번 조사에서 확인한 관련 규격은 로봇 쪽 VDA 5050 3.0.0·Open-RMF 작업 API, 상위 쪽 B2MML·OPC UA for ISA-95 Job Control·ISA-95 Part 1, 업무 범위 쪽 SCOR DS 이다. [사실][^ref-031][^ref-129] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area23-s7.md)에 있다.

## 8. 대표 연구와 자료

이번 조사에서 확인한 자료는 동적 주문 피킹 연구와 웨이브리스 출고 지시 연구, 다제조사 플릿 관리 사례, 국내 WMS–로봇 연동 발표이다. [사실][^ref-132][^ref-134]

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 대표 연구와 자료](../../topics/2026/2026-10-11-area23-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 우선순위·시작 시각·마감을 담은 작업 요청을 받아 로봇 작업으로 바꾸고, 진행 중 작업의 재정렬·수정 규칙을 적용하며, 진행·완료·취소 결과를 되돌린다 [추정][^ref-135][^ref-002][^ref-125] | 주문 접수, 출고 지시 방식(웨이브·웨이브리스), 출고 우선순위 결정(ERP·WMS·WES) |
| 로봇 자체 지능·제어 | 제조사 관제에 주문 갱신·일시정지·취소·재지시를 보내고 상태·실패·완료를 확인한다 | 주행·정지와 동작의 실제 실행, 취소할 수 없는 동작의 수행 |
| 시설·설비 제어 | 공장·창고 쪽 작업 요청을 실행 작업으로 받아 진행 상태를 확인한다 | WCS·SCADA 를 통한 설비 제어와 통합 관제 |

연계 대상: 주문 접수·출고 지시 방식과 출고 우선순위 결정은 ERP·WMS·WES 같은 상위 업무 시스템의 몫이고, ROP는 그 결과를 작업 요청의 우선순위·시작 시각·마감 제약으로 받아 로봇 작업으로 바꾸고 결과를 되돌리는 경계에 서는 것으로 보인다. [추정][^ref-135][^ref-134][^ref-002][^ref-125] VDA 5050 은 외부 IT 인터페이스를 범위 밖에 둔다. [사실][^ref-031] 따라서 상위 시스템과의 번역 계층은 ROP 쪽 인터페이스 설계 과제가 될 것으로 보인다. [추정][^ref-031]

**응답과 결과의 구분.** Open-RMF 의 취소 응답은 요청 처리의 성패와 오류만 담고 [사실][^ref-1454][^ref-1455], 폐기된 SAP Warehouse Robotics FMS 연동 계약은 취소됨(CANCELLED)과 취소 불가를 서로 다른 통지로 알린다. [사실][^ref-1456] 구축자 의견으로는 ROP 가 상위 시스템과 주고받는 정보를 접수 응답·진행 통지·취소 결과·업무 확정으로 나눠 두는 것이 좋아 보인다. [의견][^ref-1456][^ref-1453][^ref-1454]

**도착과 인수 확인.** Tartu 대학병원 현장 시험은 로봇 도착 뒤 직원의 인수 확인이 인제스터를 거쳐 관제에 전달된 다음에야 복귀 요청을 냈다. [사실][^ref-869] 도착 확인과 업무상 인수 확인을 별도 단계로 둔 예이며, 국내 물류센터의 기준은 oq-012 로 남아 있다.

**새 접점의 범위.** 공개된 Mission Dispatch MCP 서버는 조회·등록·좌표 이동 도구를 두고 취소 도구는 두지 않는다. [사실][^ref-1341] 구축자 의견으로는 이런 공개 코드를 업무 요청 접점으로 쓰려면 주문 ID 대응·허용 상태 검사·실행 전 승인·결과 대조·취소를 따로 확인해야 하며, 다사업자 WMS 운영 검증으로 볼 수 없다. [의견][^ref-1341][^ref-1463]

**설비 제어는 연계 대상.** 구축자 의견으로는 5절 제조 공장 사례의 WCS·SCADA 기반 설비 제어·통합 관제를 분류 원문 19장 ‘시설·설비 제어’ 경계의 연계 대상으로 보고, 이 영역에서는 생산 쪽 요청을 실행 작업으로 조율하는 역할의 예로만 다루는 것이 맞아 보인다. [의견][^ref-1460]

이 경계는 제품 전략에 따라 이동할 수 있다. 자세한 기준은 [범위 경계](../../about/scope-boundary.md) 페이지에 있으며, 이종 제조사를 연결하는 ROP라면 로봇 동작 실행은 제조사에 맡기고 변경 지시의 번역과 결과 확인을 맡는 구도가 된다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md) — ISA-95 작업 지시와 Open-RMF 작업 상태를 업무 단계와 잇는 문제를 함께 다루며, 같은 출처(작업 상태 스키마, task_new)를 공유한다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 다른 연구영역과의 연결](../../topics/2026/2026-10-11-area23-s10.md)에 있다.

## 11. 열린 질문

2026-09-25 실행이 새로 연 질문은 출고 우선순위 재정렬 설계(oq-019), 상위 작업 지시와 로봇 인터페이스 사이 매핑(oq-020), 적재 후 취소의 되돌림 규칙(oq-021)이다. 2026-10-11 실행은 아래 질문에 부분 근거만 보탰고, 해결된 질문은 없다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 열린 질문](../../topics/2026/2026-10-11-area23-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [23. 업무 시스템 연동](business-system-integration.md) — 섹션 3~11 신규 작성(자동 분리 반영). 2차 수정: 각주 ref-138·ref-182 → ref-110·ref-111, 5절 시작 조건·9절 마지막 문장 사실/추정 분리, 9절 표 태그 추가, 7·8절 첫 문장 목록 서술로 변경, sources 에서 미인용 ref-131 제외 (실행 2026-09-25-13)
- 2026-09-25 · 생성 · [23. 업무 시스템 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area01-s4.md) — 자동 분리: 1. 주문·업무 시스템 연계 의 "4. 핵심 개념과 용어" 절. 2차 수정: 각주 ref-182 → ref-111 (실행 2026-09-25-13)
- 2026-09-25 · 생성 · [23. 업무 시스템 연동 — 대표 연구와 자료](../../topics/2026/2026-09-25-area01-s8.md) — 자동 분리: 1. 주문·업무 시스템 연계 의 "8. 대표 연구와 자료" 절. 2차 수정: 첫 문장을 '이번 조사에서 확인한 자료는 … 이다'로 변경 (실행 2026-09-25-13)
- 2026-09-25 · 생성 · [23. 업무 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area01-s6.md) — 자동 분리: 1. 주문·업무 시스템 연계 의 "6. 대표 접근법과 기술" 절. 2차 수정: 각주 ref-138 → ref-110, 번역 절 마지막 문장 사실/추정 분리 (실행 2026-09-25-13)
- 2026-09-25 · 생성 · [23. 업무 시스템 연동 — 열린 질문](../../topics/2026/2026-09-25-area01-s11.md) — 자동 분리: 1. 주문·업무 시스템 연계 의 "11. 열린 질문" 절(2차 수정 없음) (실행 2026-09-25-13)
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
[^ref-1341]: NVIDIA (nvidia-isaac GitHub), isaac_mission_dispatch — README, 미확인, https://github.com/nvidia-isaac/isaac_mission_dispatch, 접근일 2026-10-11
[^ref-1453]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/dispatch_task_response.json, 접근일 2026-10-11
[^ref-1454]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/cancel_task_response.json, 접근일 2026-10-11
[^ref-1455]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/simple_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/simple_response.json, 접근일 2026-10-11
[^ref-1456]: SAP, APIs for Integration via Fleet Management Systems (API for Integration with Fleet Management Systems (Deprecated)), 2024-07-10, https://help.sap.com/doc/a02ad3695d5845fca1678810cb83562b/LATEST/en-US/379d6d880e5d4007b3751618080da80f_1.pdf, 접근일 2026-10-11
[^ref-1459]: 아르고 풀필먼트(테크타카), 아르고, 플로틱과 로봇 기반 물류 생산성 향상 실증 본격 실시, 2025-01-21, https://blog.argoport.com/pr-robotcooperation250121, 접근일 2026-10-11
[^ref-1460]: LG CNS, 로봇 기반 물류 자동화와 통합 관제로 HD현대일렉트릭 신공장의 새로운 운영 체계를 구축하다, 2026-07-16, https://www.lgcns.com/kr/moa/customer-story/detail.smartlogistics-robotic-logistics-2607-1, 접근일 2026-10-11
[^ref-1463]: robotmcp, demos-ros-mcp-server — Example 1: Tugbot Warehouse Simulation (Ignition Gazebo) README, 미확인, https://github.com/robotmcp/demos-ros-mcp-server/blob/edbc642849bdde1187771a15e557ec9e219184a5/1_Gazebo_Tugbot/README.md, 접근일 2026-10-11
