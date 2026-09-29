---
title: "C. 채팅 기반 구성·운영"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › C. 채팅 기반 구성·운영

# C. 채팅 기반 구성·운영

## 핵심 질문

맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? [분류원문]

## 개요

채팅으로 맵을 그리고, 시나리오를 구성하고, 로봇을 구성하고, 실제 상황을 시뮬레이션으로 재현하고, 업무를 지시·관리하는 대화형 기능 전체와 그 신뢰 기반. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **8. 채팅으로 맵 작성** | 대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다 | 공간을 말로 설명하거나 도면을 올리는 것만으로 쓸 수 있는 지도를 만들 수 있는가? | [8. 채팅으로 맵 작성](chat-map-authoring.md) | published |
| **9. 채팅으로 시나리오 구성** | 대화로 할 일·물품·사람·순서·기한·실패 처리 조건을 정한다 | 할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? | [9. 채팅으로 시나리오 구성](chat-scenario-composition.md) | seed |
| **10. 채팅으로 로봇 구성** | 대화로 투입 로봇의 종류·대수·장비·위치·역할을 정하고 수행 가능 여부를 확인한다 | 어떤 로봇을 몇 대, 어디에, 어떤 역할로 둘지 대화로 정하고 가능 여부를 바로 알 수 있는가? | [10. 채팅으로 로봇 구성](chat-robot-configuration.md) | seed |
| **11. 채팅으로 실제 상황 시뮬레이션 재현** | 실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 | 실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? | [11. 채팅으로 실제 상황 시뮬레이션 재현](chat-real-situation-simulation-replay.md) | seed |
| **12. 채팅으로 업무 지시·오케스트레이션** | 대화로 일을 지시하면 분해·배정·일정을 계획으로 제안하고, 승인 뒤 실행하며 진행 상황을 설명한다 | 대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? | [12. 채팅으로 업무 지시·오케스트레이션](chat-task-instruction-and-orchestration.md) | seed |
| **13. 대화형 기능의 신뢰·기반** | 오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 | 언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? | [13. 대화형 기능의 신뢰·기반](conversational-trust-and-foundations.md) | seed |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

대화 결과는 실행 명령이 아니라 계획이다. **사람이 확인·승인한 계획만 실행**되어야 언어 모델의 잘못된 해석이 로봇 동작으로 이어지지 않는다. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 15건이다(논문 11건 · 기사·보고서 0건 · 업체 발표 1건 · 표준·오픈소스·기관 자료 3건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-813](../../references/ref-813.md) — Qin, S., Weber, R. E., & Lu, X., Tokenization Allows Multimodal Large Language Models to Understand, Generate and Edit Architectural Floor Plans (발행 2026-03-12)
- [ref-163](../../references/ref-163.md) — 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 (발행 2026)
- [ref-786](../../references/ref-786.md) — Rajendran Kathirvel, R. S., Chavis, Z. A., Guy, S. J., & Desingh, K., SENT Map -- Semantically Enhanced Topological Maps with Foundation Models (발행 2025-11-05)
- [ref-812](../../references/ref-812.md) — Rodionov, F., Eldesokey, A., Birsak, M., Femiani, J., Ghanem, B., & Wonka, P., FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations (발행 2025-07-10)
- [ref-083](../../references/ref-083.md) — Zhang, J. 외, Generation of Indoor Open Street Maps for Robot Navigation from CAD Files (발행 2025-07)
- [ref-785](../../references/ref-785.md) — Deguchi, H., Shibata, K., & Taguchi, S. (Toyota Central R&D Labs), Language to Map: Topological map generation from natural language path instructions (발행 2024-03-15)
- [ref-815](../../references/ref-815.md) — Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등), Holodeck: Language Guided Generation of 3D Embodied AI Environments (발행 2023-12-14)
- [ref-787](../../references/ref-787.md) — Leng, S., Zhou, Y., Dupty, M. H., Lee, W. S., Joyce, S. C., & Lu, W., Tell2Design: A Dataset for Language-Guided Floor Plan Generation (발행 2023)
- [ref-811](../../references/ref-811.md) — 김영재, 김세윤, 김홍준 (대한공간정보학회지), 공공 맵 데이터를 이용한 자율주행 이동 로봇의 전역 경로 계획용 지도 생성 방법에 관한 연구 (발행 2022-06)
- [ref-816](../../references/ref-816.md) — Doğan, F. I., Torre, I., & Leite, I. (ACM/IEEE HRI 2022), Asking Follow-Up Clarifications to Resolve Ambiguities in Human-Robot Conversation (발행 2022-03)
- 그 밖에 1건

**기사·보고서**

- 아직 없음

**업체 발표**

- [ref-817](../../references/ref-817.md) — 모빌리오(Mobilio), [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 관제를 웹 화면 하나로 끝내는 방법 (발행 2026-08-24)

**표준·오픈소스·기관 자료**

- [ref-046](../../references/ref-046.md) — VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) (발행 2023-09)
- [ref-104](../../references/ref-104.md) — Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README) (발행 미확인)
- [ref-079](../../references/ref-079.md) — Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2 (발행 미확인)
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-29 · 갱신 · [8. 채팅으로 맵 작성](chat-map-authoring.md) — 3~11절 신규 작성(seed → draft), 출처 15건, 열린 질문 3건, 현장 유형 사례 3건(병원·제조 공장·실외). 2차 재검증 수정 지시 이행: 10절 14. 도면·BIM에서 지도 만들기 항목을 사실 문장과 추정 문장으로 나눔(태그 상향 해소) (실행 2026-09-29-01)
- 2026-09-29 · 생성 · [8. 채팅으로 맵 작성 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area08-s6.md) — 자동 분리: 8. 채팅으로 맵 작성 의 "6. 대표 접근법과 기술" 절(1,767자)을 옮겼다(2차 재검증에서 변경 없음) (실행 2026-09-29-01)
- 2026-09-29 · 생성 · [8. 채팅으로 맵 작성 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area08-s4.md) — 자동 분리: 8. 채팅으로 맵 작성 의 "4. 핵심 개념과 용어" 절(1,091자)을 옮겼다(2차 재검증에서 변경 없음) (실행 2026-09-29-01)
- 2026-09-29 · 생성 · [8. 채팅으로 맵 작성 — 대표 연구와 자료](../../topics/2026/2026-09-29-area08-s8.md) — 자동 분리: 8. 채팅으로 맵 작성 의 "8. 대표 연구와 자료" 절(979자)을 옮겼다(2차 재검증에서 변경 없음) (실행 2026-09-29-01)
- 2026-09-29 · 생성 · [8. 채팅으로 맵 작성 — 왜 중요한가](../../topics/2026/2026-09-29-area08-s3.md) — 자동 분리: 8. 채팅으로 맵 작성 의 "3. 왜 중요한가" 절(742자)을 옮겼다. 2차 재검증 수정: 3절의 태그 없는 판단 문장 2건에 [추정]·[의견] 태그와 각주를 붙이고 sources·출처에 ref-785·ref-786·ref-788 추가 (실행 2026-09-29-01)
<!-- auto:category-recent:end -->
