---
title: "오류 선언 (Error Declaration (EPCIS errorDeclaration))"
type: glossary
term_ko: 오류 선언
term_en: Error Declaration (EPCIS errorDeclaration)
definition: 앞선 EPCIS 이벤트의 내용이 틀렸음을 선언 시각·사유·정정 이벤트 id 와 함께 기록해 원 기록을 지우지 않고 바로잡게 하는 EPCIS 요소이다.
related_areas: [8, 7]
tags: []
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-045, ref-044]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 오류 선언

# 오류 선언 (Error Declaration (EPCIS errorDeclaration))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 오류 선언 | Error Declaration (EPCIS errorDeclaration) | EPCIS errorDeclaration — Error Declaration |

## 한 줄 정의

앞선 EPCIS 이벤트의 내용이 틀렸음을 선언 시각·사유·정정 이벤트 id 와 함께 기록해 원 기록을 지우지 않고 바로잡게 하는 EPCIS 요소이다. [추정][^ref-045][^ref-044]

## 설명

사유는 CBV 어휘 did_not_occur·incorrect_data 로 적는다. 용어집 EPCIS 항목(epcis.md)과 연결된다.

## 관련 영역

- [8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)
- [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)

## 출처

[^ref-045]: GS1, gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl, 접근일 2026-09-25
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-09-25

- 참고문헌 페이지: [ref-045](../references/ref-045.md), [ref-044](../references/ref-044.md)
