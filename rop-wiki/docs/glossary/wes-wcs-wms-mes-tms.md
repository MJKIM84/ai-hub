---
title: "WES/WCS/WMS/MES/TMS"
type: glossary
term_ko: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템
term_en: Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System
definition: 창고·생산·운송의 주문·재고·설비·공정을 관리하거나 실행하는 업무·실행 시스템 계열의 약어이며, ROP는 이들에서 작업 요청을 받아 로봇 작업으로 바꾸고 결과를 되돌려 주는 관계에 있다.
related_areas: [1, 2, 10]
tags: [업무 시스템, WMS, WES, WCS, MES, TMS]
status: draft
created: 2026-09-24
updated: 2026-09-24
sources: [ref-002]
version: 3
confidence: medium
---

[홈](../index.md) › [용어집](index.md) › WES/WCS/WMS/MES/TMS

# WES/WCS/WMS/MES/TMS

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 창고 관리 시스템 | Warehouse Management System | WMS |
| 창고 실행 시스템 | Warehouse Execution System | WES |
| 창고 제어 시스템 | Warehouse Control System | WCS |
| 제조 실행 시스템 | Manufacturing Execution System | MES |
| 운송 관리 시스템 | Transportation Management System | TMS |

이 위키의 용어집 시드 목록이 다섯 약어를 한 항목으로 묶고 있어 한 페이지에서 각각 풀어 쓴다. 약어마다 따로 페이지가 필요해지면 나누어 만든다.

## 한 줄 정의

창고·생산·운송의 주문·재고·설비·공정을 관리하거나 실행하는 업무·실행 시스템 계열의 약어이며, ROP는 이들에서 작업 요청을 받아 로봇 작업으로 바꾸고 결과를 되돌려 주는 관계에 있다. [추정]

## 설명

분류 원문은 1. 주문·업무 시스템 연계의 정의에서 이 시스템들을 한꺼번에 들고, A. 업무·공급망 설계의 설명에서 책임의 겹침을 지적한다.

ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 [분류원문]

기업 업무와 현장 운영·제어의 경계를 정리할 때는 ISA-95의 기업–제어 시스템 통합 관점이 참고가 된다. 실제 제품별로 WES·WCS·FMS·ROP의 책임은 겹칠 수 있다. [2] [분류원문][^ref-002]

원문에 함께 나오는 ERP(Enterprise Resource Planning, 전사적 자원 관리)는 회계·구매·재고·생산 같은 전사 업무를 통합 관리하는 시스템 범주다. 협회·표준 기관의 정의는 미확인이다. [추정] FMS는 문맥상 로봇 플릿 관리 시스템(Fleet Management System), 곧 제조사 관제를 가리키는 것으로 읽는다. [가정] 두 약어는 이 항목의 범위 밖이므로 여기서는 풀어 쓰기만 한다.

다섯 약어는 단일 표준 정의가 있는 용어가 아니라 제품 범주의 이름이다. [추정] 통용되는 뜻은 다음과 같다. 협회 자료의 설명은 검색 결과로만 확인했고 원문은 열지 못했다.

- **WMS(창고 관리 시스템)**: 창고 안의 작업 흐름과 물품 보관을 관리하는 응용 시스템. [추정][^cand-06]
- **WCS(창고 제어 시스템)**: 컨베이어·자동창고 같은 자동화 설비를 실시간으로 제어하며 WMS와 설비 사이를 잇는 소프트웨어. [추정][^cand-07]
- **WES(창고 실행 시스템)**: WMS와 WCS 사이에서 창고 각 구역의 작업 흐름을 조정하는 소프트웨어. 제품에 따라 WMS나 WCS의 기능을 함께 담기도 한다. [추정][^cand-08]
- **MES(제조 실행 시스템)**: 제조 현장에서 작업 지시부터 완제품까지 생산 실행을 관리하는 시스템 범주. 협회·표준 기관의 정의는 미확인이다. [추정]
- **TMS(운송 관리 시스템)**: 출하 이후의 운송 계획·배차·운송사 선정·운임을 다루는 시스템 범주. 협회·표준 기관의 정의는 미확인이다. [추정]

ROP와 이들 시스템의 책임 경계는 [ROP가 직접 소유할 범위와 외부 연계 경계](../about/scope-boundary.md)에 원문 그대로 정리되어 있다. 그 표를 따르면 WMS·WES·MES는 작업 요청의 출처이자 완료 결과를 되돌려 주는 상대이고, TMS가 다루는 배차·운송계획·운임은 ROP가 입출고 시간과 인계를 맞추는 연계 대상이다. [추정] WCS와 ROP는 설비 제어와 로봇 조율이라는 인접한 역할을 맡으므로 원문이 지적한 대로 책임이 겹칠 수 있고, 어느 쪽이 컨베이어 준비와 로봇 도착을 맞추는지는 현장마다 정해야 한다. [추정]

## 관련 영역

- [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) — 이 시스템들의 주문·재고·생산 요청을 로봇 작업으로 바꾸고 변경·취소·완료를 되돌리는 영역이다.
- [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) — WMS·WES가 정의하는 업무 단계와 로봇 작업 단계의 선후관계·완료 조건을 맞추는 영역이다.
- [10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) — WCS가 제어하는 컨베이어·자동창고와 로봇 작업을 연계하는 영역이다.

관련 용어: [기업–제어 시스템 통합 표준 (ISA-95)](isa-95.md), [공급망 운영 참조 모델 (SCOR)](scor.md), [전자 제품 코드 정보 서비스 (EPCIS)](epcis.md)

## 출처

[^ref-002]: ISA, Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems, 2025, https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of, 접근일 2026-09-24 (원문 미열람)
[^cand-06]: ASCM, A Guide To Warehouse Management & Management Systems, 발행일 미확인, https://www.ascm.org/topics/warehouse-management-wms-explained/, 접근일 2026-09-24 (원문 미열람)
[^cand-07]: MHI, What is WCS? (MHI Blog), 발행일 미확인, https://www.mhi.org/blog/126051/what-is-wcs, 접근일 2026-09-24 (원문 미열람)
[^cand-08]: MHI, Warehouse Execution Software Implementation (MHI Blog), 발행일 미확인, https://www.mhi.org/blog/66378/warehouse-execution-software-implementation, 접근일 2026-09-24 (원문 미열람)

- [ref-002](../references/ref-002.md)
- cand-06, cand-07, cand-08 은 검색 결과의 기관·제목·URL 로 실재만 확인한 후보 출처다. 정식 참고문헌 id 는 첫 검증 실행에서 부여하며, 그 전까지 이 출처에 기댄 주장은 [추정]으로 둔다.
- [표준·프레임워크 목록](../standards/index.md)
