---
title: "디지털 트윈 (Digital Twin)"
type: glossary
term_ko: 디지털 트윈
term_en: Digital Twin
definition: 물리적 대상(장비·자재·공정·설비·제품 등)을 데이터로 연결된 가상 모델로 표현한 것이다.
related_areas: [22, 8, 23]
tags: [시뮬레이션, 예측, 현재 상태]
status: draft
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 3
confidence: low
---

[홈](../index.md) › [용어집](index.md) › 디지털 트윈

# 디지털 트윈 (Digital Twin)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 디지털 트윈 | Digital Twin | 없음 |

## 한 줄 정의

물리적 대상(장비·자재·공정·설비·제품 등)을 데이터로 연결된 가상 모델로 표현한 것이다. [추정][^cand-03][^cand-13]

## 설명

이 정의는 두 자료의 검색 결과 요약에 기댄 것이다. 제조 분야에서는 국제표준화기구(ISO, International Organization for Standardization)의 ISO 23247 시리즈가 디지털 트윈 프레임워크를 정의하며, 1부(ISO 23247-1)가 개요와 일반 원칙을 다루는 것으로 검색 결과에 나타난다. [추정][^cand-03] 한국정보통신기술협회(TTA)의 정보통신용어사전은 디지털 트윈을 사물을 컴퓨터상에 동일하게 표현한 가상 모델을 만들고 현실과 데이터로 연결해 상호작용하게 하는 것으로 설명하는 것으로 검색 결과에 나타난다. [추정][^cand-13] 두 자료 모두 원문을 열지 못했다.

이 위키에서 이 말을 쓸 때 가장 중요한 것은 분류 원문이 둔 다음 구분이다.

8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]

즉 이 위키에서 "디지털 트윈"은 22. 시뮬레이션·예측용 디지털 트윈, 곧 가정한 미래를 실험하는 기능을 가리킨다. 로봇·설비·공간·화물의 현재 상태를 통합하고 지연·누락·충돌·불확실성을 관리하는 기능은 디지털 트윈이라 부르지 않고 8. 실시간 세계 상태·데이터 일관성으로 부른다. 두 기능은 같은 환경 모델과 자산 데이터를 공유할 수 있지만 목적(운영 판단 대 정책 실험), 갱신 주기, 허용되는 가정(현재 관측 대 가상 시나리오)이 다르다. [추정] ROP가 디지털 트윈을 직접 소유할지 외부 시뮬레이션 도구와 연계할지는 제품 전략에 따라 달라지며 이 위키에서는 정하지 않는다.

## 관련 영역

- [22. 시뮬레이션·예측용 디지털 트윈](../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) — 이 용어가 명칭에 포함된 세부영역이며, 가정한 미래를 실험하는 기능을 다룬다.
- [8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md) — 현재 상태를 표현하는 기능으로, 디지털 트윈과 구분해 다룬다.
- [23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) — 시뮬레이션 결과와 실기체 시험을 대조해 검증한다.

관련 용어: [산업 자동화용 민첩 로봇 경진대회 (ARIAC)](ariac.md)

## 출처

[^cand-03]: ISO, ISO 23247-1:2021 Automation systems and integration — Digital twin framework for manufacturing — Part 1: Overview and general principles, 2021, https://www.iso.org/standard/75066.html, 접근일 2026-09-24 (원문 미열람)
[^cand-13]: TTA(한국정보통신기술협회), TTA정보통신용어사전 — 디지털 트윈, 발행일 미확인, https://terms.tta.or.kr/dictionary/dictionaryView.do?word_seq=191771-1, 접근일 2026-09-24 (원문 미열람)

- cand-03, cand-13 은 검색 결과의 기관·제목·URL 로 실재만 확인한 후보 출처다. 정식 참고문헌 id 는 첫 검증 실행에서 부여하며, 그 전까지 이 출처에 기댄 주장은 [추정]으로 둔다.
- [표준·프레임워크 목록](../standards/index.md)
