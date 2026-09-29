---
title: "스킬 인터페이스 (Skill Interface)"
type: glossary
term_ko: 스킬 인터페이스
term_en: Skill Interface
definition: '능력·스킬·서비스 모델에서 스킬을 외부에서 제어하기 위해 반드시 두는 접점(예: OPC UA 서버)으로, 스킬 구현과 분리되어 같은 스킬을 여러 프로토콜로 노출할 수 있게 한다.'
related_areas: [5, 6, 20]
tags: []
status: published
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-878]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 스킬 인터페이스

# 스킬 인터페이스 (Skill Interface)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 스킬 인터페이스 | Skill Interface | 없음 |

## 한 줄 정의

능력·스킬·서비스 모델에서 스킬을 외부에서 제어하기 위해 반드시 두는 접점(예: OPC UA 서버)으로, 스킬 구현과 분리되어 같은 스킬을 여러 프로토콜로 노출할 수 있게 한다. [추정][^ref-878]

## 설명

Plattform Industrie 4.0 의 능력·스킬·서비스 참조 모델을 구현한 CSS 온톨로지는 스킬마다 스킬 인터페이스를 가져야 한다고 둔다. ROP 는 이 접점을 호출해 상태·실패·완료를 확인하고, 스킬 내부 구현은 제조사 쪽 연계 대상으로 둔다.

## 관련 영역

- [5. 로봇 능력·작업 표현](../categories/robot-ontology/robot-capability-and-task-representation.md)
- [6. 온톨로지 기반 시스템·로봇 연동](../categories/robot-ontology/ontology-based-system-and-robot-integration.md)
- [20. 로봇·제조사 관제 연동](../categories/integration/robot-and-vendor-fleet-manager-integration.md)

## 출처

[^ref-878]: CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) GitHub 공식 저장소, CSS — An ontology for the Capability, Skill and Service model of Plattform Industrie 4.0 (README), 미확인, https://github.com/CaSkade-Automation/CSS, 접근일 2026-09-29

- 참고문헌 페이지: [ref-878](../references/ref-878.md)
