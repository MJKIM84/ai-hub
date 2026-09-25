---
title: "22. 시뮬레이션·예측용 디지털 트윈"
type: area
category: "F. 도입·검증·유지관리"
area_no: 22
related_areas: [4, 6, 8, 9, 13, 15, 20, 21, 23, 24, 27, 28]
tags: [디지털 트윈, 이산 사건 시뮬레이션, ISO 23247, Open-RMF 시뮬레이션, 시나리오 실험]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-241, ref-267, ref-398, ref-402, ref-659, ref-660, ref-661, ref-662, ref-663, ref-664, ref-665, ref-666, ref-667, ref-668, ref-669, ref-670, ref-671, ref-672, ref-673]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [F. 도입·검증·유지관리](index.md) › 22. 시뮬레이션·예측용 디지털 트윈

# 22. 시뮬레이션·예측용 디지털 트윈

!!! info "소속 대분류"
    [F. 도입·검증·유지관리](index.md) — 핵심 질문:
    새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 [분류원문]

## 2. SCM 관점의 질문

성수기 주문량이 늘면 어디가 먼저 막힐까? [분류원문]

> 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]

## 3. 왜 중요한가

시뮬레이션·예측용 디지털 트윈은 실제 운영을 방해하지 않고 개선안을 먼저 시험하는 도구로 쓰일 수 있어, 2절의 성수기 병목 질문에 실제 성수기가 오기 전에 답하는 수단이 된다. [추정][^ref-666]

Coelho 외(2021)는 사내 물류 시뮬레이션 모델이 현실을 대표하면 실제 운영을 방해하지 않고 개선안을 시험하는 디지털 트윈화 도구로 쓰일 수 있다고 보고했다. [사실][^ref-666] 로봇 플릿 쪽에서는 Open-RMF 문서가 물리 시뮬레이터를 쓰면 배터리 소모나 충돌 비용 없이 시나리오를 반복하고, 드문 예외 상황을 탐색하고, 현장 배치 전에 장시간 검증을 할 수 있다고 설명한다(확인일 2026-09-25). [사실][^ref-667]

공급망 수준에서도 Le·Fan(2024)은 COVID-19 이후 위험·교란 관리에서 디지털 트윈의 이점이 뚜렷해졌다고 보고 물류·공급망 디지털 트윈 개념 틀을 제안했다. [사실][^ref-665] 다만 같은 검토는 실제 데이터로 검증한 논문이 소수이고 대다수가 생성 데이터를 쓴다고 보고해, 예측이 현장에서 얼마나 맞는지는 아직 확인할 과제로 남는다. [사실][^ref-665]

## 4. 핵심 개념과 용어

이 위키는 디지털 트윈을 용도로 나눈다: 현재 상태를 표현하는 것은 8. 실시간 세계 상태·데이터 일관성, 그 모델을 이용해 가정한 미래를 실험하는 것은 이 영역이다. 분류 원문은 이렇게 적는다.

자세한 내용은 주제 페이지 [22. 시뮬레이션·예측용 디지털 트윈 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area22-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 피킹

**시나리오:** 성수기 주문 증가를 앞두고 피킹 배정 규칙과 로봇 대수를 가상 환경에서 비교

| 항목 | 내용 |
|---|---|
| 시작 조건 | 성수기 주문·물동량 전망이 시나리오 입력으로 들어온다. 이 전망은 상위 업무 시스템의 수요예측에서 받는 입력으로 보인다(연계 대상). [추정][^ref-665][^ref-673] |
| 작업 대상 | 가정한 성수기 주문의 피킹 작업(가상 환경 안의 주문·운반 흐름) |
| 수행 자원 | 시뮬레이션된 로봇(slotcar 단순화 모델)과 문·승강기 설비 플러그인이 ROP의 요청에 응답한다. [사실][^ref-667][^ref-668] ROP는 자기 배정·교통·충전 정책을 이 가상 플릿·설비에 그대로 실행해 보는 것으로 보인다. [추정][^ref-667][^ref-668] |
| 제약 | 주문 도착량·배정 규칙·자원 수(로봇·작업대)를 바꿔 처리량과 대기를 비교하는 방식으로 어디가 먼저 막히는지 본다. [추정][^ref-398][^ref-669] 경로망 배치도 시뮬레이션으로 설계하는 연구가 있다. [사실][^ref-267] |
| 완료·인계 | 시뮬레이션 결과는 업무 완료나 재고 변경으로 인정되지 않는다. 채택안의 변경 후 동작 확인은 23. 시험·형식 검증·벤치마크로 넘긴다는 구분은 구축자 의견이다. [의견][^ref-667] |
| 예외·성과 | Merschformann 외(2019)의 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. [사실][^ref-398] 예측이 실제와 맞는지는 실데이터 검증이 부족해 미확인이다. [사실][^ref-665] |

다음은 설명을 위한 가상의 시나리오이다. 물류센터 운영자가 성수기 전에 피킹 구역에서 어느 자원이 먼저 포화되는지 알고 싶어 한다. 이미 공개된 이산 사건 시뮬레이션 연구·도구는 이런 질문에 도착량·규칙·자원 수를 바꿔 결과를 비교하는 방식으로 답한다. 다만 ROP 오케스트레이션 정책 자체를 성수기 시나리오로 시험한 공개 물류센터 사례는 이번 조사 범위에서 찾지 못했다. [추정][^ref-398][^ref-669][^ref-666][^ref-664]

국내에서는 CJ대한통운이 2021-11-22 현실 물류센터와 같은 가상 물류센터를 12월부터 단계적으로 구축해 2023년 AI·알고리즘을 적용한 디지털 트윈을 완성하겠다는 계획을 발표했고, 작업 동선·재고 배치·설비 효율 최적화와 장비 고장·피킹 오류·상품 파손 원인의 사전 파악을 목표로 들었다. [추정] 벤더 주장[^ref-672]

## 6. 대표 접근법과 기술

대표 접근은 이산 사건 시뮬레이션, 같은 코드를 쓰는 물리 시뮬레이터, 도면·스캔에서 초기 모델을 만드는 방법이다. [사실][^ref-664][^ref-667]

자세한 내용은 주제 페이지 [22. 시뮬레이션·예측용 디지털 트윈 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area22-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

표준으로는 제조용 디지털 트윈 프레임워크 ISO 23247(국내 KS X ISO 23247)이 있고, 오픈소스로는 Open-RMF 시뮬레이션·RAWSim-O·OFacT가 이 영역의 실험 도구다. [사실][^ref-659][^ref-667]

자세한 내용은 주제 페이지 [22. 시뮬레이션·예측용 디지털 트윈 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area22-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 개념 구분, 물류 DES와 디지털 트윈의 결합, 물류·공급망 디지털 트윈 검토, 모델 검증 틀, 스캔 기반 자동 생성 연구다. [사실][^ref-663][^ref-665]

자세한 내용은 주제 페이지 [22. 시뮬레이션·예측용 디지털 트윈 — 대표 연구와 자료](../../topics/2026/2026-09-25-area22-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

ROP가 직접 맡는 몫은 자기 작업 배정·교통·충전 정책과 설비 요청을 시뮬레이션된 플릿·설비에 대해 그대로 실행해 보는 것으로 보인다. [추정][^ref-667][^ref-668]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 경로 요청을 받는 단순화 로봇 모델에 자기 배정·교통·충전 정책을 실행해 보는 것 [추정][^ref-667][^ref-668] | 연계 대상: 센서 인식·로컬 회피 같은 로봇 자체 거동의 충실도, 센서 시뮬레이션·합성 데이터·물리 AI는 제조사·시뮬레이터 제공자 영역 [추정][^ref-667][^ref-673] |
| 시설·설비 제어 | 문·승강기 요청을 시뮬레이션 설비 플러그인에 보내고 응답을 받는 흐름의 시험 [추정][^ref-667] | 연계 대상: 실제 승강기·컨베이어·PLC·설비 안전 제어([범위 경계](../../about/scope-boundary.md)) |
| 상위 업무 시스템 | 주문 도착량·배정 규칙·자원 수를 바꿔 처리량·대기를 비교하는 시나리오 실험 [추정][^ref-398][^ref-669] | 연계 대상: 시나리오의 주문·물동량 전망은 수요예측에서 받는 입력 [추정][^ref-665] |

Open-RMF 시뮬레이션의 로봇 모델은 경로 요청을 받아 레일식으로 움직이는 단순화 모델이어서, ROP 시뮬레이션은 로봇 거동보다 플릿 조율·설비 상호작용 실험에 초점이 맞는 것으로 보인다. [추정][^ref-667][^ref-668] 센서 시뮬레이션·합성 데이터를 앞세운 제품 소개는 벤더 주장이며 ROP 직접 범위가 아니다. [추정] 벤더 주장[^ref-673] 경계는 제품 전략에 따라 움직일 수 있으므로 [범위 경계](../../about/scope-boundary.md) 페이지를 함께 본다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 현재 상태 모델(8. 실시간 세계 상태·데이터 일관성)을 받아 미래를 실험하고, 그 결과를 시험·배정·교통·수명주기 영역으로 넘긴다. 아래 연결은 이 절의 각 문장 태그대로 읽는다.

자세한 내용은 주제 페이지 [22. 시뮬레이션·예측용 디지털 트윈 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area22-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 이번 실행에서 새로 올렸다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-56) 물류센터에서 로봇 오케스트레이션 정책을 디지털 트윈으로 미리 시험한 뒤 실제 처리량과 비교해 예측 오차를 공개한 사례(특히 국내 사례)가 있는가? 실데이터 검증 논문이 소수라는 검토가 배경이다.[^ref-665]
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-56) 제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가?[^ref-661]
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-56) 제조사 로봇을 단순화 모델(레일식 주행 등)로 시뮬레이션할 때 실제 거동과의 차이가 처리량·병목 예측에 주는 오차를 어떤 데이터로 보정하는가?[^ref-668]

2절의 질문 가운데 ROP 정책을 성수기 시나리오로 시험한 공개 물류센터 사례는 이번 조사에서 찾지 못해 미확인으로 남긴다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems, 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-659]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010140724, 접근일 2026-09-25 (원문 미열람)
[^ref-661]: ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition, 2026, https://www.iso.org/standard/87426.html, 접근일 2026-09-25 (원문 미열람)
[^ref-663]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-09-25 (원문 미열람)
[^ref-664]: Agalianos, K., Ponis, S. T., Aretoulaki, E., & Plakas, G., Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics, 2020, https://www.sciencedirect.com/science/article/pii/S2351978920320990, 접근일 2026-09-25 (원문 미열람)
[^ref-665]: Le, T. V., & Fan, R., Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921, 접근일 2026-09-25 (원문 미열람)
[^ref-666]: Coelho, F., Relvas, S., & Barbosa-Póvoa, A. P., Simulation-based decision support tool for in-house logistics: the basis for a digital twin, 2021, https://www.sciencedirect.com/science/article/abs/pii/S0360835220307646, 접근일 2026-09-25 (원문 미열람)
[^ref-667]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25
[^ref-668]: Open Robotics (open-rmf), rmf_simulation — README, 미확인, https://github.com/open-rmf/rmf_simulation, 접근일 2026-09-25
[^ref-669]: Merschformann, M. (merschformann GitHub), RAWSim-O — A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-09-25
[^ref-672]: CJ대한통운, 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료), 2021-11, https://www.cjlogistics.com/ko/newsroom/news/NR_00000905, 접근일 2026-09-25 (원문 미열람)
[^ref-673]: NVIDIA, NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins, 미확인, https://blogs.nvidia.com/blog/mega-omniverse-blueprint, 접근일 2026-09-25 (원문 미열람)
