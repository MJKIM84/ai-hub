---
title: "전자 제품 코드 정보 서비스 (EPCIS)"
type: glossary
term_ko: 전자 제품 코드 정보 서비스
term_en: Electronic Product Code Information Services (EPCIS)
definition: GS1이 정한, 제품·자산의 상태·위치·이동·인계에 관한 이벤트를 기록하고 공유하기 위한 표준이다.
related_areas: [7, 2, 17]
tags: [표준, GS1, 추적, 인계 확인]
status: draft
created: 2026-09-24
updated: 2026-09-24
sources: [ref-003]
version: 3
---

[홈](../index.md) › [용어집](index.md) › 전자 제품 코드 정보 서비스

# 전자 제품 코드 정보 서비스 (EPCIS)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 전자 제품 코드 정보 서비스 | Electronic Product Code Information Services | EPCIS |

## 한 줄 정의

GS1이 정한, 제품·자산의 상태·위치·이동·인계에 관한 이벤트를 기록하고 공유하기 위한 표준이다. [사실][^ref-003]

## 설명

분류 원문은 7. 화물·재고·자산 식별과 추적을 설명하며 EPCIS를 다음과 같이 인용한다.

**7번은 SCM 관점에서 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 화물의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [분류원문][^ref-003]

원문 12장이 가리키는 GS1 자료의 제목은 "EPCIS and CBV Linked Data Model"이다. [사실][^ref-003] 제목에 함께 나오는 CBV(Core Business Vocabulary)의 내용과 EPCIS의 현행 판본은 원문을 열지 못해 미확인이다. EPCIS가 국제표준화기구(ISO, International Organization for Standardization)와 국제전기기술위원회(IEC, International Electrotechnical Commission)의 국제 표준 ISO/IEC 19987로도 채택되었다는 설명은 검색 결과에 나타나지만 이 역시 원문 미열람이다. [추정][^cand-11]

ROP 맥락에서 EPCIS가 중요한 이유는 원문이 지적한 대로 로봇의 위치와 화물의 인계 책임이 서로 다른 것이기 때문이다. 로봇이 목적지에 도착했다는 사실은 로봇 관제가 알려 주지만, 어떤 팔레트가 누구에게 넘어갔는지는 별도의 이벤트로 기록해야 상위 업무 시스템의 재고 변경을 인정할 수 있다. EPCIS의 이벤트 모델은 그 인계 이벤트를 창고 관리 시스템(WMS, Warehouse Management System)이나 거래 상대와 같은 의미로 주고받는 참고 모델이 된다. [추정] ROP가 이벤트를 직접 생성할지, WMS가 생성하고 ROP는 근거 데이터만 넘길지는 제품 전략에 따라 달라지므로 이 위키에서는 정하지 않는다.

## 관련 영역

- [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) — 화물·운반구의 식별과 인계 이력을 연결하는 이벤트 모델의 참고 표준이다.
- [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) — 운반 완료와 인수 확인·재고 반영 완료를 잇는 완료 조건을 이벤트로 정의할 때 참조한다.
- [17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) — 로봇 사이의 물리적 인계를 확인하고 기록하는 이벤트의 형식을 논의할 때 참조한다.

관련 용어: [WES/WCS/WMS/MES/TMS](wes-wcs-wms-mes-tms.md)

## 출처

[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24 (원문 미열람)
[^cand-11]: ISO/IEC, ISO/IEC 19987 Information technology — EPC Information Services (EPCIS), 발행일 미확인, https://www.iso.org/standard/85557.html, 접근일 2026-09-24 (원문 미열람)

- [ref-003](../references/ref-003.md)
- cand-11 은 검색 결과의 기관·제목·URL 로 실재만 확인한 후보 출처다. 정식 참고문헌 id 는 첫 검증 실행에서 부여하며, 그 전까지 이 출처에 기댄 주장은 [추정]으로 둔다.
- [표준·프레임워크 목록](../standards/index.md)
