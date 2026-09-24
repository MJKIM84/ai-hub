---
title: "플릿 어댑터 (Fleet Adapter)"
type: glossary
term_ko: 플릿 어댑터
term_en: Fleet Adapter
definition: Open-RMF에서 제조사별 로봇 플릿(같은 관제 아래 묶인 로봇 무리)을 연결하기 위해 두는 제조사별 연결 구성요소이다.
related_areas: [9, 5, 12, 21]
tags: [Open-RMF, 어댑터, 제조사 관제]
status: draft
created: 2026-09-24
updated: 2026-09-24
sources: [ref-004]
version: 3
---

[홈](../index.md) › [용어집](index.md) › 플릿 어댑터

# 플릿 어댑터 (Fleet Adapter)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 플릿 어댑터 | Fleet Adapter | 없음. 플릿(fleet)은 같은 제조사 관제 아래 묶인 로봇 무리를 뜻한다 |

## 한 줄 정의

Open-RMF에서 제조사별 로봇 플릿(같은 관제 아래 묶인 로봇 무리)을 연결하기 위해 두는 제조사별 연결 구성요소이다. [사실][^ref-004]

## 설명

분류 원문은 Open-RMF의 구조를 설명하며 플릿 어댑터를 로봇 쪽 연결을 맡는 부품으로 든다.

Open-RMF도 제조사별 Fleet Adapter와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결한다. **로봇 연결과 시설 연결을 함께 보는 것**이 필요하다. [4] [분류원문][^ref-004]

Open-RMF 문서의 플릿 통합 장은 제조사 관제가 허용하는 제어 수준에 따라 어댑터를 범주로 나누며, 검색 결과에는 관제가 로봇의 경로를 지정·변경할 수 있는 Full Control 범주와 로봇 상태만 읽는 Read Only 범주가 나타난다. [추정][^cand-10] 범주의 정확한 정의와 그 밖의 범주는 원문을 열지 못해 미확인이다.

ROP 맥락에서 플릿 어댑터는 9. 로봇·제조사 관제 연동의 SCM 관점의 질문과 직결된다.

개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? [분류원문]

어댑터 범주가 갈리는 이유는 제조사 관제가 경로·속도·정지 같은 제어권을 어디까지 열어 주느냐가 제조사마다 다르기 때문이며, ROP가 맡을 수 있는 교통 조율과 실행 보장의 수준도 그에 따라 달라진다. [추정] 어댑터가 로봇 기능을 어떤 형식으로 기술하는지는 중점 연구 트랙 [매뉴얼 기반 로봇 기능 온톨로지](../tracks/manual-capability-ontology/index.md)의 단계 1에서 산업 규격 후보의 하나로 조사한다.

## 관련 영역

- [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — 제조사 API(Application Programming Interface)·SDK(Software Development Kit)·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터의 대표 사례다.
- [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) — 어댑터가 노출하는 기능 기술 형식이 능력 온톨로지의 비교 대상이 된다.
- [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) — 어댑터를 거치는 명령의 접수·실행·완료·취소 상태와 제어권 문제가 여기서 다뤄진다.
- [21. 온보딩·설정·현장 시운전](../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) — 새 제조사를 추가할 때 어댑터를 만들고 설정하는 반복 작업이 온보딩 비용의 큰 부분이다.

관련 용어: [오픈 RMF (Open-RMF)](open-rmf.md)

## 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-24 (원문 미열람)
[^cand-10]: Open Robotics, Mobile Robot Fleet Integration — Programming Multiple Robots with ROS 2, 발행일 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-09-24 (원문 미열람)

- [ref-004](../references/ref-004.md)
- cand-10 은 검색 결과의 기관·제목·URL 로 실재만 확인한 후보 출처다. 정식 참고문헌 id 는 첫 검증 실행에서 부여하며, 그 전까지 이 출처에 기댄 주장은 [추정]으로 둔다.
- [표준·프레임워크 목록](../standards/index.md)
