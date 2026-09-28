---
title: "기업–제어 시스템 통합 표준 (ISA-95)"
type: glossary
term_ko: 기업–제어 시스템 통합 표준
term_en: ISA-95 Enterprise-Control System Integration
definition: ISA-95 계열에서 하위 실행 계층이 수행할 작업 단위의 요청으로, OPC UA for ISA-95 Job Control 은 이를 저장·시작·갱신·일시정지·중단하는 메서드를 둔다.
related_areas: [21, 23, 24]
tags: [표준, ISA, 기업–제어 통합]
status: published
created: 2026-09-24
updated: 2026-09-25
sources: [ref-002, ref-130, ref-131]
version: 4
confidence: medium
---

[홈](../index.md) › [용어집](index.md) › 기업–제어 시스템 통합 표준

# 기업–제어 시스템 통합 표준 (ISA-95)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 기업–제어 시스템 통합 표준 | Enterprise-Control System Integration | ISA-95. ANSI(American National Standards Institute)/ISA-95 표기의 근거는 미확인이다. 제정 기관은 국제자동화협회(ISA, International Society of Automation)이다. 통용되는 한글 명칭이 없어 영문 부제를 옮겼다 |

## 한 줄 정의

ISA-95 계열에서 하위 실행 계층이 수행할 작업 단위의 요청으로, OPC UA for ISA-95 Job Control 은 이를 저장·시작·갱신·일시정지·중단하는 메서드를 둔다. [추정][^ref-130][^ref-131]

## 설명

OPC UA for ISA-95 Job Control(판 2.0.0, 2024-01-31)은 Store·StoreAndStart·Start·RevokeStart·Pause·Resume·Stop·Update·Abort·Cancel·Clear 메서드와 작업 지시·작업 응답 데이터형을 정의한다. 명세는 Pause 로 Interrupted, Resume 으로 Running, Abort 로 Aborted 상태 전이를 둔다.

## 관련 영역

- [23. 업무 시스템 연동](../categories/integration/business-system-integration.md) — 업무 시스템에서 받은 주문·재고·생산 요청과 결과 반영의 경계를 ISA-95 관점으로 정리한다.
- [24. 작업·워크플로 모델링](../categories/planning-and-optimization/task-and-workflow-modeling.md) — 업무 단계와 현장 작업 단계의 분리 지점을 정할 때 참조한다.
- [21. 상호운용 표준·적합성](../categories/integration/interoperability-standards-and-conformance.md) — 업무 시스템·ROP·설비 제어 사이의 책임 분담을 표준 어휘로 논의한다.

관련 용어: [공급망 운영 참조 모델 (SCOR)](scor.md), [WES/WCS/WMS/MES/TMS](wes-wcs-wms-mes-tms.md)

## 출처


- [ref-002](../references/ref-002.md)
- cand-04 는 검색 결과의 기관·제목·URL 로 실재만 확인한 후보 출처다. 정식 참고문헌 id 는 첫 검증 실행에서 부여하며, 그 전까지 이 출처에 기댄 주장은 [추정]으로 둔다.
- [표준·프레임워크 목록](../standards/index.md)
[^ref-130]: OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv), 2024-01-31, https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL, 접근일 2026-09-25
[^ref-131]: OPC Foundation / ISA, OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4), 미확인, https://reference.opcfoundation.org/specs/OPC-10031-4/6.2, 접근일 2026-09-25 (원문 미열람)
