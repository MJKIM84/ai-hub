---
title: "공급망 운영 참조 모델 (SCOR)"
type: glossary
term_ko: 공급망 운영 참조 모델
term_en: Supply Chain Operations Reference (SCOR)
definition: ASCM이 관리하는 공급망 프로세스 참조 모델로, 공급망을 계획·주문·조달·생산/가공·이행·반품 프로세스와 이를 아우르는 오케스트레이션 프로세스로 기술한다.
related_areas: [23, 24, 39]
tags: [공급망, ASCM, 프로세스 참조 모델]
status: draft
created: 2026-09-24
updated: 2026-09-24
sources: [ref-001]
version: 3
confidence: medium
---

[홈](../index.md) › [용어집](index.md) › 공급망 운영 참조 모델

# 공급망 운영 참조 모델 (SCOR)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 공급망 운영 참조 모델 | Supply Chain Operations Reference | SCOR — Supply Chain Operations Reference. 관리 기관은 ASCM(Association for Supply Chain Management)이다. 개정 전 원문 12장이 가리키는 현행 자료의 이름은 SCOR Digital Standard(SCOR DS)이다 |

## 한 줄 정의

ASCM이 관리하는 공급망 프로세스 참조 모델로, 공급망을 계획·주문·조달·생산/가공·이행·반품 프로세스와 이를 아우르는 오케스트레이션 프로세스로 기술한다. [사실][^ref-001]

## 설명

개정 전 분류 원문(2026-09-24)은 이 위키의 출발점에서 SCOR를 다음과 같이 소개했다. 2026-09-28에 개정한 분류는 이 틀을 쓰지 않고, 로봇 오케스트레이션 플랫폼을 구현하고 운영하는 일 전체를 기준으로 한다. SCOR는 업무 프로세스 참조 모델의 하나로만 다룬다.

ASCM의 SCOR는 계획·주문·조달·생산/가공·이행·반품과 이를 아우르는 Orchestrate를 다룬다. **ROP는 이 중 물리적인 작업이 발생하는 부분을 연결하는 역할**로 접근할 수 있다. SCOR의 공급망 오케스트레이션과 로봇 오케스트레이션은 범위가 다르다. [1] [옛 분류원문][^ref-001]

이름이 같아도 SCOR의 오케스트레이션과 ROP의 로봇 오케스트레이션은 층이 다르다. 앞의 것은 공급망 전체를 아우르는 프로세스 수준의 통합이고, 뒤의 것은 주문·물류·생산 계획에서 나온 작업을 로봇과 설비의 실제 행동으로 바꾸고 결과를 되돌리는 실행 수준의 조율이다. [추정] 이 위키는 두 층을 섞지 않기 위해 SCOR 프로세스 이름을 업무 요구를 서술하는 상위 어휘로만 쓰고, 현장 작업 단계는 24. 작업·워크플로 모델링의 어휘로 쓴다.

SCOR DS의 현행 판본·발행 연도와 자료의 접근 조건(회원제·유료 여부)은 이번 구축에서 원문을 열지 못해 미확인이다.

## 관련 영역

- [23. 업무 시스템 연동](../categories/integration/business-system-integration.md) — SCOR의 주문·이행 프로세스에서 나오는 요청을 로봇 작업으로 바꾸고 결과를 되돌리는 접점이다.
- [24. 작업·워크플로 모델링](../categories/planning-and-optimization/task-and-workflow-modeling.md) — SCOR 프로세스를 입고·적치·피킹·포장 같은 현장 작업 단계로 분해할 때 상위 어휘가 된다.
- [39. 운영 성과 측정·개선](../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) — 로봇 개별 성능과 공급망 전체 성과를 구분해 볼 때 참조한다.

관련 용어: [기업–제어 시스템 통합 표준 (ISA-95)](isa-95.md), [WES/WCS/WMS/MES/TMS](wes-wcs-wms-mes-tms.md)

## 출처

[^ref-001]: ASCM, SCOR Digital Standard, 미확인, https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/, 접근일 2026-09-24 (원문 미열람)

- [ref-001](../references/ref-001.md)
- [표준·프레임워크 목록](../standards/index.md)
