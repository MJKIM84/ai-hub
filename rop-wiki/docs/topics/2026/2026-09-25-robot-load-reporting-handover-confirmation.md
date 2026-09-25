---
title: "로봇 관제 인터페이스의 적재·하역 보고와 화물 인계 확인"
type: topic
category: "B. 공통 정보·환경 모델"
primary_area_no: 7
related_areas: [9, 10, 17]
tags: [VDA 5050, Open-RMF, 인계 확인, 적재물 식별]
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-003, ref-013, ref-014, ref-015, ref-016, ref-022, ref-023]
last_run: 2026-09-25
version: 1
---

[홈](../../index.md) › [주제](../index.md) › 로봇 관제 인터페이스의 적재·하역 보고와 화물 인계 확인

# 로봇 관제 인터페이스의 적재·하역 보고와 화물 인계 확인

**주 연구영역:** [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) · **관련 영역:** [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [17. 로봇 간 협업·물리적 인계](../../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) · **실행:** 2026-09-25-01

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 1 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 독일자동차산업협회(Verband der Automobilindustrie, VDA)의 VDA 5050은 로봇이 싣고 있는 적재물의 식별 결과를, Open-RMF(Open Robotics Middleware Framework)는 적재·하역 설비의 성공 결과를 메시지로 다룬다. [사실][^ref-022][^ref-023]
- ROP는 이 보고를 받아 화물 식별자와 대조하고 기록하는 역할을 맡는 구조가 될 것으로 보인다. [추정][^ref-022]
- 로봇의 완료 신호와 EPCIS(Electronic Product Code Information Services) 인계 이벤트를 잇는 표준 매핑은 확인되지 않았다. [추정][^ref-013][^ref-014]

## 2. 배경

[7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)의 SCM 관점 질문, 곧 로봇이 도착했을 때 실제로 어떤 팔레트가 인계됐는지를 확인하는 문제에서 출발했다. 영역 페이지의 분량 기준에 따라 그 페이지 6절의 로봇 관제 인터페이스 내용을 이 페이지로 옮겼다.

## 3. 본문

### VDA 5050의 적재물 보고

VDA 5050은 무인 운반차(Automated Guided Vehicle, AGV)와 상위 관제 사이의 통신 권고안이다. [사실][^ref-022] 2.0.0판(2022-01)의 state 메시지는 loads 항목에서 loadId(바코드·RFID(Radio Frequency Identification) 등으로 식별한 값, 식별 전이면 빈 값 가능)·loadType·loadPosition을 보고한다. [사실][^ref-022] pick·drop 같은 적재 동작은 주문의 노드·엣지에 붙는 action으로 다루고 진행 상태를 state로 보고하는 것으로 보이나, 원문 규정인지 구현 라이브러리 설명인지는 미확인이다. [추정][^ref-022]

### Open-RMF의 적재·하역 결과

Open-RMF 배송(Delivery) 작업에서 [플릿 어댑터](../../glossary/fleet-adapter.md)는 적재 설비(dispenser)에 DispenserRequest를 보내 DispenserResult SUCCESS를 받은 뒤 로봇을 하역 지점으로 보내고, 하역 설비(ingestor)에 IngestorRequest를 보내 IngestorResult SUCCESS로 하역 완료를 확인한다. [사실][^ref-023]

### 행동 완료와 화물 인계

[EPCIS](../../glossary/epcis.md) 이벤트는 소유·책임·점유 이전의 업무 맥락을 source/destination 목록으로 붙이고, CBV(Core Business Vocabulary, 핵심 업무 어휘)는 그 유형으로 owning_party·possessing_party·location을 정한다. [사실][^ref-014][^ref-015]

따라서 두 인터페이스의 완료 신호는 로봇·설비의 행동 완료를 알릴 뿐이며, 어떤 팔레트가 누구에게 인계됐는지 확정하려면 SSCC(Serial Shipping Container Code, 물류 단위 일련 코드) 같은 화물 식별자와 인계 당사자·위치를 담은 이벤트와 결합해야 한다고 본다. 이는 위 사실에서 도출한 추론이며 두 계층을 잇는 표준 매핑은 확인되지 않았다. [추정][^ref-022][^ref-023][^ref-013][^ref-014][^ref-003]

## 4. 현장 시나리오

**물류 흐름 단계:** 출하

**시나리오:** 로봇이 팔레트를 하역 설비에 내려놓고 인계를 확정

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | SSCC가 표시된 팔레트. [사실][^ref-016] |
| 수행 자원 | 적재 설비(dispenser)가 싣고, 로봇이 운반하며 loadId를 보고하고, 하역 설비(ingestor)가 받는다. 판독 자체는 연계 대상이다. [추정][^ref-022][^ref-023] |
| 제약 | 해당 없음 |
| 완료·인계 | IngestorResult SUCCESS [사실][^ref-023]와 loadId [사실][^ref-022]를 SSCC와 대조해 인계 이벤트로 남겨야 인계를 확정할 수 있다고 본다. 3절의 추론이며 표준 매핑은 확인되지 않았다. [추정][^ref-014] |
| 예외·성과 | 해당 없음 |

다음은 설명을 위한 가상의 시나리오이다. 하역 설비의 결과 메시지를 받았다는 기록과 SSCC가 확인된 팔레트가 인계됐다는 기록을 서로 다른 사실로 다룬다.

## 5. ROP 관점의 시사점

**직접 범위:** 로봇이 보고한 식별 결과(loadId)와 설비의 결과 메시지를 받아 화물 식별자와 대조하고 기록하는 일이다. [추정][^ref-022][^ref-023]

**연계 범위:** 연계 대상: 바코드·RFID 판독 자체(센서 인식)는 로봇·판독 설비 쪽 기능이며, VDA 5050은 식별 결과를 상태로 보고하는 인터페이스만 정한다. [추정][^ref-022] 설비 자체의 제어도 [범위 경계](../../about/scope-boundary.md)에 따라 연계 대상이다.

## 6. 연결되는 연구영역

- [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) — 주 연구영역, 화물 식별과 인계 이력
- [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — VDA 5050 적재물 보고
- [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) — 적재·하역 설비의 요청·결과
- [17. 로봇 간 협업·물리적 인계](../../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) — 행동 완료와 인계 확정의 결합

## 7. 열린 질문

- (상태: 열림) 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가?

전체 목록: [열린 질문](../../open-questions.md)

## 8. 출처

[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24 (원문 미열람)
[^ref-013]: OpenEPCIS, EPCIS 2.0 and EPCIS 1.2 | OpenEPCIS Docs, 미확인, https://openepcis.io/docs/epcis/, 접근일 2026-09-25 (원문 미열람)
[^ref-014]: GS1, Core Business Vocabulary (CBV) Standard, 미확인, https://ref.gs1.org/standards/cbv/, 접근일 2026-09-25 (원문 미열람)
[^ref-015]: GS1, EPCIS and CBV Implementation Guideline, 미확인, https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-016]: GS1, Serial Shipping Container Code (SSCC), 미확인, https://www.gs1.org/standards/id-keys/sscc, 접근일 2026-09-25 (원문 미열람)
[^ref-022]: VDA(Verband der Automobilindustrie), VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control, 2022-01, https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

- 판정: 1차 조건부 승인 / 2차 통과
- 확인·미확인·교차 확인: 확인 17건, 미확인 3건(f6, f17, f18), 교차 확인 0건(실행 전체 claim_checks 기준)
- 강등된 주장: f6 사실 → 추정, f17 사실 → 추정(이 페이지에는 쓰지 않음)
- 검증자 주의: 판정: 1차 조건부 승인 / 2차 통과. 이번 실행은 원문 열람이 차단된 환경에서 검증됐다. 확인 17건, 미확인 3건(f6, f17, f18), 교차 확인 0건. 강등: f6 사실 → 추정, f17 사실 → 추정. 삭제: f18. f4·f5·f8·f11·f14 는 검증 스니펫으로 확인되지 않은 구절만 뺐다. 원문 미열람 출처: ref-003, ref-011, ref-012, ref-013, ref-014, ref-015, ref-016, ref-017, ref-018, ref-019, ref-020, ref-021, ref-022, ref-023, ref-024(모두 검색 결과의 기관·제목·URL 일치로 실재를 확인함). 미사용 출처 ref-025 는 제외됐다. 주의: 표준 근거가 대부분 GS1 계열(ISO/IEC 판 포함)이라 서로 독립된 교차 확인이 없다. f17 의 지게차 속도 효과는 원문 재확인이 필요하다. EPC 태그 데이터 표준은 1.11판 기준이다. 로봇 완료 신호와 EPCIS 인계 이벤트의 결합(f19)은 추론이다. 한국 자료는 GS1 Korea 1건(2019-09)뿐이다. 정정 요청: 해당 없음. / 2차 통과(재검증 2회차). 드리프트 없음, [분류원문] 보존, 섹션 순서 준수, 링크 유효. 직전 2차 지시 2건이 이행됐다. (1) 분량: 6절 로봇 적재·하역 보고(f14·f15·f16)를 주제 페이지 docs/topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md 로 옮기고 링크했다(신규 주제 예산 1건 안). 3~11절은 검증자 추정 약 3,600~3,950자로 4,000자 안이다. (2) 7절 약어: 'JSON 계열 형식·웹 API'로 바꿨고 [추정][^ref-013]과 단일 출처 병기를 유지했다. 영역 페이지: admonition 세 줄·1절·2절·원문 주석 인용 블록이 시드와 글자 단위로 같고, H2 13개가 정본과 같으며, auto 마커 내용이 보존됐고, 각주 15건의 정의·사용·프런트매터 sources 가 일치한다. 주제 페이지: H2 10개가 정본과 같고, 각주 7건과 sources·reference_updates cited_by 가 일치하며, 모든 태그가 1차 처분(f14 축소, f15·f19·f20 추정)과 같고, 검증 노트는 '1차 조건부 승인 / 2차 대기'와 1차 문구 그대로다. 주제 페이지 1~7절은 약 2,400~2,500자(추정)로 상한 가까이에 있으니 퍼블리셔 분량 검사로 확인한다. 사소한 표기 의견(수정 지시 아님): 영역 페이지 5절 표 아래 '다음은 설명을 위한 가상의 시나리오이다.' 뒤에 서술이 없어 다음 갱신 때 '위 시나리오는 …'으로 고치기를 권한다. 11절과 주제 페이지 7절의 열린 질문에는 oq id 가 없으므로 퍼블리셔가 id 를 부여하면 템플릿 형식('**oq-NNN**')으로 맞추기를 권한다. 주제 페이지 9절 둘째 줄의 머리말은 템플릿 문구('확인·미확인:')와 조금 다르다. 2차 검증은 웹 도구를 쓰지 않았다.
- 신뢰도: medium

## 10. 이력

| 날짜 | 실행 id | 변경 | 버전 |
|---|---|---|---|
| 2026-09-25 | 2026-09-25-01 | 신규 작성(7. 화물·재고·자산 식별과 추적 6절에서 분리) | 1 |
