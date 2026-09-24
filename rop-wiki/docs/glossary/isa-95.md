---
title: "기업–제어 시스템 통합 표준 (ISA-95)"
type: glossary
term_ko: 기업–제어 시스템 통합 표준
term_en: ISA-95 Enterprise-Control System Integration
definition: 국제자동화협회(ISA)가 제정한, 기업 업무 시스템과 제조 운영·제어 시스템의 통합을 다루는 표준 시리즈이다.
related_areas: [1, 2, 28]
tags: [표준, ISA, 기업–제어 통합]
status: draft
created: 2026-09-24
updated: 2026-09-24
sources: [ref-002]
version: 3
---

[홈](../index.md) › [용어집](index.md) › 기업–제어 시스템 통합 표준

# 기업–제어 시스템 통합 표준 (ISA-95)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 기업–제어 시스템 통합 표준 | Enterprise-Control System Integration | ISA-95 — ANSI(American National Standards Institute)/ISA-95. 제정 기관은 국제자동화협회(ISA, International Society of Automation)이다. 통용되는 한글 명칭이 없어 영문 부제를 옮겼다 |

## 한 줄 정의

국제자동화협회(ISA)가 제정한, 기업 업무 시스템과 제조 운영·제어 시스템의 통합을 다루는 표준 시리즈이다. [사실][^ref-002]

## 설명

분류 원문은 ISA-95를 기업 업무와 현장 운영·제어의 경계를 정리하는 참고 관점으로 인용한다.

기업 업무와 현장 운영·제어의 경계를 정리할 때는 ISA-95의 기업–제어 시스템 통합 관점이 참고가 된다. 실제 제품별로 WES·WCS·FMS·ROP의 책임은 겹칠 수 있다. [2] [분류원문][^ref-002]

이 위키가 인용한 ref-002는 표준 본문이 아니라 ISA가 2025년에 낸 보도자료다. [사실][^ref-002] 보도자료가 알리는 개정판이 시리즈의 어느 부(part)이며 무엇이 바뀌었는지는 보도자료와 표준 본문을 열지 못해 미확인이다. 국제전기기술위원회(IEC, International Electrotechnical Commission)의 국제 표준 IEC 62264와의 대응 관계도 미확인이다. ISA95 위원회 소개 페이지는 이 표준이 퍼듀 참조 모델(Purdue Reference Model)에 바탕을 두고 기업 기능과 제조 제어 기능 사이의 정보 교환을 정의한다고 설명하는 것으로 검색 결과에 나타난다. [추정][^cand-04]

ROP를 ISA-95의 관점으로 보면 업무 시스템과 현장 장비 제어 사이에서 실행을 맡는 층에 해당한다. [추정] 다만 원문이 밝힌 대로 창고 실행 시스템(WES, Warehouse Execution System)·창고 제어 시스템(WCS, Warehouse Control System)·플릿 관리 시스템(FMS, Fleet Management System)·ROP의 책임은 제품마다 겹칠 수 있으므로, 이 위키는 ISA-95의 계층을 경계를 고정하는 규칙이 아니라 경계를 논의하는 공통 언어로 쓴다. 원문의 FMS는 문맥상 로봇 플릿 관리 시스템, 곧 제조사 관제를 가리키는 것으로 읽는다. [가정] WES·WCS는 [WES/WCS/WMS/MES/TMS](wes-wcs-wms-mes-tms.md)에서 다룬다.

## 관련 영역

- [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) — 업무 시스템에서 받은 주문·재고·생산 요청과 결과 반영의 경계를 ISA-95 관점으로 정리한다.
- [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) — 업무 단계와 현장 작업 단계의 분리 지점을 정할 때 참조한다.
- [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) — 업무 시스템·ROP·설비 제어 사이의 책임 분담을 표준 어휘로 논의한다.

관련 용어: [공급망 운영 참조 모델 (SCOR)](scor.md), [WES/WCS/WMS/MES/TMS](wes-wcs-wms-mes-tms.md)

## 출처

[^ref-002]: ISA, Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems, 2025, https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of, 접근일 2026-09-24 (원문 미열람)
[^cand-04]: ISA, ISA95, Enterprise-Control System Integration (ISA95 표준 위원회 소개), 발행일 미확인, https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa95, 접근일 2026-09-24 (원문 미열람)

- [ref-002](../references/ref-002.md)
- cand-04 는 검색 결과의 기관·제목·URL 로 실재만 확인한 후보 출처다. 정식 참고문헌 id 는 첫 검증 실행에서 부여하며, 그 전까지 이 출처에 기댄 주장은 [추정]으로 둔다.
- [표준·프레임워크 목록](../standards/index.md)
