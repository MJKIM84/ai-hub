---
title: "7. 화물·재고·자산 식별과 추적"
type: area
category: "B. 공통 정보·환경 모델"
area_no: 7
related_areas: [1, 6, 8, 9, 10, 17, 20]
tags: [EPCIS, SSCC, 인계 확인, VDA 5050, 자산 식별]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-003, ref-011, ref-012, ref-013, ref-014, ref-015, ref-016, ref-017, ref-018, ref-019, ref-020, ref-021, ref-022, ref-023, ref-024]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [B. 공통 정보·환경 모델](index.md) › 7. 화물·재고·자산 식별과 추적

# 7. 화물·재고·자산 식별과 추적

!!! info "소속 대분류"
    [B. 공통 정보·환경 모델](index.md) — 핵심 질문:
    로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? [분류원문]

> 상태: draft · 신뢰도: medium · 갱신일: 2026-09-25 · 마지막 실행: 2026-09-25

## 1. 한 줄 정의

제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 [분류원문]

## 2. SCM 관점의 질문

로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? [분류원문]

> 원문 주석: **7번은 SCM 관점에서 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 화물의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [분류원문]

원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]

## 3. 왜 중요한가

2절의 원문 주석이 짚듯, 로봇 위치를 추적하는 일과 화물의 위치·인계 책임을 추적하는 일은 다르다. 로봇 쪽 기록은 이미 표준 인터페이스에 있다. VDA 5050 2.0.0(2022-01)은 로봇이 싣고 있는 적재물의 식별자(loadId)·유형(loadType)·적재 위치(loadPosition)를 상태로 보고하게 한다. [사실][^ref-022] Open-RMF는 적재·하역 설비가 돌려주는 성공 결과 메시지로 적재와 하역 완료를 확인한다. [사실][^ref-023]

반면 소유·책임·점유 이전이라는 업무 맥락은 다른 계층인 EPCIS 이벤트의 source/destination 목록으로 표현한다. [사실][^ref-014][^ref-015] 그래서 로봇·설비의 완료 신호만으로는 "어떤 팔레트가 누구에게 인계됐는가"를 확정하기 어렵고, 화물 식별자와 인계 당사자·위치를 담은 이벤트와 결합해야 한다고 본다. 이는 위 사실들에서 도출한 추론이며, 두 계층을 잇는 표준 매핑은 확인되지 않았다. [추정][^ref-022][^ref-023][^ref-013][^ref-014][^ref-003]

## 4. 핵심 개념과 용어

- **SSCC(Serial Shipping Container Code, 물류 단위 일련 코드)** — 케이스·팔레트·소포처럼 보관·운송을 위해 묶인 물류 단위를 고유하게 식별하는 18자리 GS1 키다. 확장 자리·GS1 업체코드·일련 참조번호·검증 숫자로 이뤄진다. [사실][^ref-016][^ref-017]
- **GRAI(Global Returnable Asset Identifier)·GIAI(Global Individual Asset Identifier)** — GS1은 팔레트·상자·트레이·케그 같은 재사용 운반구에는 GRAI를, 컨테이너·트럭·트레일러 같은 개별 자산에는 GIAI를 쓰도록 구분한다. [사실][^ref-019][^ref-020]
- **EPC 인코딩** — GS1 EPC 태그 데이터 표준(Tag Data Standard, TDS) 1.11판은 SSCC·GRAI·SGLN·GIAI 등 GS1 키를 UHF(Ultra High Frequency) RFID(Radio Frequency Identification, 무선 주파수 식별) 태그에 싣는 인코딩(SSCC-96, GRAI-96 등)을 정의한다. [사실][^ref-021]
- **[EPCIS](../../glossary/epcis.md)(Electronic Product Code Information Services) 이벤트 유형** — EPCIS 2.0은 ObjectEvent, AggregationEvent, AssociationEvent, TransformationEvent, TransactionEvent 다섯 가지 이벤트 유형을 둔다. [사실][^ref-013]
- **집계 이벤트(AggregationEvent)** — 케이스를 팔레트에 싣거나 내리는 것처럼 상위(parent) 객체와 하위(children) 객체의 물리적 결합·분리를 기록한다. [사실][^ref-013]
- **AssociationEvent** — EPCIS 2.0에서 도입되었고, 센서를 컨테이너·팔레트 같은 자산에 붙이는 장기 연결을 기록한다. [사실][^ref-013]
- **인계 맥락(source/destination)** — 이벤트가 소유·책임·점유 이전의 일부일 때 붙인다. CBV(Core Business Vocabulary, 핵심 업무 어휘)는 그 유형으로 owning_party(소유 당사자)·possessing_party(점유 당사자)·location(위치) 세 가지를 정한다. [사실][^ref-014][^ref-015]

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 출하

**시나리오:** 포장을 마친 팔레트를 로봇이 출하 도크의 하역 설비로 운반·인계

| 항목 | 내용 |
|---|---|
| 시작 조건 | 포장을 마친 출하 팔레트가 적재 지점에서 대기하고 상위 시스템이 운반 작업을 내린다. 이 작업을 기록하는 EPCIS 이벤트의 업무 단계에는 CBV 표준 값 shipping(출하)이 있다. [사실][^ref-014] |
| 작업 대상 | SSCC가 표시된 팔레트(물류 단위). [사실][^ref-016] 팔레트 자체를 재사용 운반구로 관리하면 GRAI로 따로 식별한다. [사실][^ref-019] |
| 수행 자원 | 적재 설비가 팔레트를 싣고, 로봇이 운반하며 적재물 식별 결과를 보고하고, 하역 설비가 받는다. 바코드·RFID 판독 자체는 로봇·판독 설비 쪽 연계 대상이고, ROP는 식별 결과의 수신·대조·기록을 맡는 구조가 된다. [추정][^ref-022] |
| 제약 | GS1 Korea 자료(2019-09) 기준으로 팔레트 바코드 하단은 기단부에서 400~800mm 높이에 둔다. [사실][^ref-017] 로봇·고정 스캐너의 판독 위치는 이 높이를 전제로 설계해야 할 것으로 보인다. [추정][^ref-017] |
| 완료·인계 | 하역 설비의 IngestorResult SUCCESS [사실][^ref-023]와 로봇이 보고한 loadId [사실][^ref-022]를 팔레트의 SSCC와 대조하고, 인계 당사자·위치를 담은 이벤트로 남겨야 인계를 확정할 수 있다고 본다. 이 결합은 추론이며 표준 매핑은 확인되지 않았다. [추정][^ref-013][^ref-014] |
| 예외·성과 | 도크 도어를 모사한 RFID 포털 실험(2009년 논문)에서 팔레트 태그 판독성은 제품·포장 유형, 태그 종류·부착 위치, 적재 패턴에 따라 달라졌다. [추정][^ref-024] 판독 실패 시 인계 확정을 어떻게 처리할지는 11절의 열린 질문이다. |

다음은 설명을 위한 가상의 시나리오이다. 로봇이 출하 도크에 도착했다는 기록과, SSCC가 확인된 특정 팔레트가 하역 설비에 인계됐다는 기록은 서로 다른 사실이다.

이 영역은 표 가운데 작업 대상(어떤 식별 키로 부르는가), 완료·인계(식별 결과를 대조해 인계 이벤트로 남기는가), 예외·성과(판독이 실패하면 무엇을 인정하는가) 칸에 주로 관여한다.

## 6. 대표 접근법과 기술

### 식별 키와 데이터 캐리어

SSCC는 GS1 물류 라벨(Logistic Label)에 반드시 들어가며, 응용식별자(Application Identifier, AI) 00을 붙여 GS1-128 바코드로 표시한다. [사실][^ref-018][^ref-017] RFID를 쓰면 같은 키를 EPC 인코딩으로 태그에 싣는다(TDS 1.11판 기준). [사실][^ref-021] 한계는 판독 조건에 있다(5절 예외·성과, 8절).

### 이벤트 기반 추적

EPCIS 이벤트의 업무 단계(bizStep) 필드에는 CBV 표준 값이 들어가며, 그 가운데 receiving(입고)·putting_away(적치)·shipping(출하) 같은 창고 업무 단계가 있다. [사실][^ref-014] 이 값을 이용하면 EPCIS 이벤트를 물류 흐름 단계에 대응시킬 수 있을 것으로 보인다. [추정][^ref-014] 적재 관계는 집계 이벤트로, 인계 맥락은 source/destination 목록으로 기록한다(4절).

### 로봇 관제 인터페이스의 적재 보고

VDA 5050 2.0.0(2022-01)의 state 메시지는 loads 항목에서 loadId(바코드·RFID 등으로 식별한 고유 값이며 식별 전이면 빈 값일 수 있음)·loadType·loadPosition을 보고한다. [사실][^ref-022] pick·drop 같은 적재 처리 동작은 주문의 노드·엣지에 붙는 action으로 다루고 진행 상태를 state로 보고하는 것으로 보이나, 원문 규정인지 구현 설명인지는 미확인이다. [추정][^ref-022]

[Open-RMF](../../glossary/open-rmf.md)의 배송 작업에서는 [플릿 어댑터](../../glossary/fleet-adapter.md)가 적재 설비(dispenser)에 DispenserRequest를 보내 DispenserResult SUCCESS를 받은 뒤 로봇을 하역 지점으로 보내고, 하역 설비(ingestor)에 IngestorRequest를 보내 IngestorResult SUCCESS로 하역 완료를 확인한다. [사실][^ref-023] 두 인터페이스 모두 행동 완료를 알리며, 인계 이벤트와의 결합은 3절의 추론 단계에 머문다.

## 7. 관련 표준·프레임워크·오픈소스

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| GS1 EPCIS 2.0 (ISO/IEC 19987:2024) | 표준 | 서로 다른 애플리케이션이 기업 내·기업 간에 가시성 이벤트 데이터를 만들고 공유하게 한다. [사실][^ref-011] | ref-011, ref-003 (원문 미열람) |
| GS1 CBV (ISO/IEC 19988:2024) | 표준 | EPCIS 이벤트에 채울 어휘 요소와 표준 값을 정의한다. [사실][^ref-012][^ref-014] | ref-012, ref-014 (원문 미열람) |
| SSCC·GS1 물류 라벨 | 표준 | 물류 단위를 18자리 키로 식별하고 GS1-128로 표시한다. [사실][^ref-016][^ref-018] | ref-016, ref-018, ref-017 (원문 미열람) |
| GRAI·GIAI | 표준 | 재사용 운반구와 개별 운송 자산을 식별한다. [사실][^ref-019][^ref-020] | ref-019, ref-020 (원문 미열람) |
| EPC 태그 데이터 표준 1.11판 | 표준 | GS1 키의 RFID 인코딩을 정의한다. [사실][^ref-021] | ref-021 (원문 미열람) |
| VDA 5050 2.0.0 | 표준 | 로봇 상태 메시지로 적재물 식별 결과를 보고한다. [사실][^ref-022] | ref-022 (원문 미열람) |
| Open-RMF 워크셀(dispenser·ingestor) | 오픈소스 | 적재·하역 설비와의 요청·결과 메시지로 완료를 확인한다. [사실][^ref-023] | ref-023 (원문 미열람) |
| OpenEPCIS 문서 | 오픈소스 | EPCIS 2.0 이벤트 유형과 1.2 대비 변경점을 설명한다. [사실][^ref-013] | ref-013 (원문 미열람) |

EPCIS 2.0·CBV 2.0은 2022년 6월 GS1에서 비준되었고 JSON/JSON-LD 형식, REST API, 센서 데이터, 기존 무엇·언제·어디서·왜에 더한 '어떻게(How)' 차원을 추가했다. 비준 시점(2022년 6월)은 OpenEPCIS 문서 단일 출처이며 GS1 원문으로 교차 확인하지 못했다. [추정][^ref-013] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 8. 대표 연구와 자료

- Singh, J. 외, RFID tag readability issues with palletized loads of consumer goods(2009) — 도크 도어를 모사한 RFID 포털 실험에서 팔레트 적재 소비재의 태그 판독성이 제품·포장 유형, 태그 종류·부착 위치, 적재 패턴에 따라 달라졌다. [추정][^ref-024] 인계 확인의 예외 조건을 설계할 때 참고할 자료다.
- GS1 Korea(대한상공회의소 유통물류진흥원), SSCC 안내 자료 Vol. 21(2019-09) — SSCC 구조, GS1-128 표시, 팔레트 바코드 부착 높이(400~800mm)를 한국어로 설명한다. [사실][^ref-017]
- GS1, EPCIS and CBV Implementation Guideline — 소유·책임·점유 이전 맥락을 source/destination 목록으로 표현하는 방법을 설명한다. [사실][^ref-015]
- Open Robotics, Workcells 문서 — 적재·하역 워크셀과 요청·결과 메시지 흐름을 설명한다. [사실][^ref-023]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 보고한 적재물 식별 결과(loadId)의 수신·대조·기록 [추정][^ref-022] | 연계 대상: 바코드·RFID 태그 판독(센서 인식)과 RFID 포털의 판독 성능 [추정][^ref-022][^ref-024] |
| 시설·설비 제어 | 적재·하역 설비와 요청·결과를 주고받아 완료를 확인(Open-RMF가 이 흐름을 메시지로 둔다) [사실][^ref-023] | 연계 대상: 설비 자체의 제어 |
| 상위 업무 시스템 | 인계가 확정된 화물 식별자·위치를 업무 시스템에 되돌림 | 연계 대상: 전사 재고정책 |

[분류 원문 9장](../../about/scope-boundary.md)은 상위 업무 시스템 경계에서 ROP가 "주문·납기·재고 제약을 받아 실행하고 결과 반영"한다고 보고, 이 경계가 제품 전략에 따라 이동할 수 있다고 적는다. 이종 제조사를 연결하는 ROP라면 판독 방법은 로봇·판독 설비에 맡기고, 식별 결과의 수신·대조·기록으로 직접 범위를 한정하는 것이 이 경계에 맞는다. [추정][^ref-022]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

- [1. 주문·업무 시스템 연계](../a-business-supply-chain-design/01-order-and-business-system-integration.md) — 인계 확정 결과를 상위 업무 시스템에 반영하는 경계가 이어진다.
- [6. 지도·공간·위치 모델](06-map-space-and-location-model.md) — 인계 이벤트의 위치(location) 식별자가 공간 모델의 장소와 같은 의미여야 한다.
- [8. 실시간 세계 상태·데이터 일관성](08-real-time-world-state-and-data-consistency.md) — 로봇이 보고하는 현재 적재 상태(loads)는 현재 세계 상태의 일부다.
- [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — VDA 5050의 적재물 보고와 pick·drop 동작이 식별 결과의 입력 경로다.
- [10. 설비·건물 시스템 연동](../c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) — 적재·하역 설비와의 요청·결과 교환이 완료 확인의 한 축이다.
- [17. 로봇 간 협업·물리적 인계](../e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) — 물리적 인계 완료를 화물 식별과 결합하는 문제를 함께 다룬다.
- [20. 예외 복구·재계획·업무 연속성](../e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) — 판독 실패·오판독 때 인계 확정을 처리하는 절차로 이어진다.

## 11. 열린 질문

- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-01) 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가?
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-01) 국내 물류센터에서 SSCC 라벨이나 EPCIS 이벤트를 로봇 작업 결과(적재·하역 완료)와 연결해 운영하는 사례가 있는가?
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-01) 로봇·게이트의 바코드·RFID 판독 실패나 오판독이 생기면 인계 확정을 보류·재스캔·사람 확인 중 어떤 기준으로 처리해야 하는가?

전체 목록: [열린 질문](../../open-questions.md)

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24 (원문 미열람)
[^ref-011]: ISO/IEC, ISO/IEC 19987:2024 - Information technology — EPC Information Services (EPCIS), 2024-03, https://www.iso.org/standard/85557.html, 접근일 2026-09-25 (원문 미열람)
[^ref-012]: ISO/IEC, ISO/IEC 19988:2024 - Information technology — GS1 Core Business Vocabulary (CBV), 2024, https://www.iso.org/standard/85558.html, 접근일 2026-09-25 (원문 미열람)
[^ref-013]: OpenEPCIS, EPCIS 2.0 and EPCIS 1.2 | OpenEPCIS Docs, 미확인, https://openepcis.io/docs/epcis/, 접근일 2026-09-25 (원문 미열람)
[^ref-014]: GS1, Core Business Vocabulary (CBV) Standard, 미확인, https://ref.gs1.org/standards/cbv/, 접근일 2026-09-25 (원문 미열람)
[^ref-015]: GS1, EPCIS and CBV Implementation Guideline, 미확인, https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-016]: GS1, Serial Shipping Container Code (SSCC), 미확인, https://www.gs1.org/standards/id-keys/sscc, 접근일 2026-09-25 (원문 미열람)
[^ref-017]: GS1 Korea(대한상공회의소 유통물류진흥원), SSCC (Serial Shipping Container Code) GS1 Information Vol. 21, 2019-09, http://www.gs1kr.org/front/service/File/SSCC%20%EB%B0%9C%EA%B0%84%20%EC%9E%90%EB%A3%8C.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-018]: GS1, GS1 Logistic Label Guideline, 미확인, https://www.gs1.org/docs/tl/GS1_Logistic_Label_Guideline.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-019]: GS1, Global Returnable Asset Identifier (GRAI), 미확인, https://www.gs1.org/standards/id-keys/grai, 접근일 2026-09-25 (원문 미열람)
[^ref-020]: GS1, Which GS1 identification key should be used for individual assets used to transport goods? (GS1 GO Customer Service Portal), 미확인, https://support.gs1.org/support/solutions/articles/43000734294-which-gs1-identification-key-should-be-used-for-individual-assets-used-to-transport-goods-, 접근일 2026-09-25 (원문 미열람)
[^ref-021]: GS1, EPC Tag Data Standard (1.11판), 미확인, https://www.gs1.org/sites/default/files/docs/epc/GS1_EPC_TDS_i1_11.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-022]: VDA(Verband der Automobilindustrie), VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control, 2022-01, https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25 (원문 미열람)
[^ref-024]: Singh, J. 외, RFID tag readability issues with palletized loads of consumer goods, 2009, https://onlinelibrary.wiley.com/doi/abs/10.1002/pts.864, 접근일 2026-09-25 (원문 미열람)
