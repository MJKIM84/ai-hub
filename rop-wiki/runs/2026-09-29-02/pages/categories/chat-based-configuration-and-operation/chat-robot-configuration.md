---
title: "10. 채팅으로 로봇 구성"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 10
related_areas: [4, 5, 9, 13, 20, 21, 25, 34, 35, 44, 47, 55]
tags: [연합 형성, 능력 매칭, 팩트시트, 플릿 설정, 구성 코파일럿, 차량 소요대수 산정]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-031, ref-677, ref-465, ref-818, ref-090, ref-105, ref-229, ref-819, ref-820, ref-088, ref-201, ref-821, ref-822, ref-823, ref-759, ref-674]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 10. 채팅으로 로봇 구성

# 10. 채팅으로 로봇 구성

!!! info "소속 대분류"
    [C. 채팅 기반 구성·운영](index.md) — 핵심 질문:
    맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

대화로 투입 로봇의 종류·대수·장비·위치·역할을 정하고 수행 가능 여부를 확인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 로봇 구성**: 투입할 로봇의 종류·대수·장착 장비·초기 위치·역할을 대화로 정하고, 온톨로지로 수행 가능 여부를 확인해 알려 준다
- **로봇 구성 적합성 사전 확인**: 대화로 정한 로봇 구성이 시나리오의 작업·공간·시설 조건을 채우는지 실행 전에 확인하고 부족한 능력이나 대수를 알려 준다

## 2. 핵심 질문

어떤 로봇을 몇 대, 어디에, 어떤 역할로 둘지 대화로 정하고 가능 여부를 바로 알 수 있는가? [분류원문]

## 3. 왜 중요한가

투입할 로봇의 종류·대수·장비·위치·역할을 대화로 정하려면, 대화 뒤에 언어 모델이 읽을 수 있는 능력 목록과 그 결과를 검증하는 엔진이 있어야 한다. 언어 모델 기반 다중 로봇 계획 연구가 로봇 유형별 스킬 집합을 텍스트로 모델에 주고 그 위에서 팀 구성과 역할 배정을 하는 점을 보면, 채팅으로 로봇 구성은 로봇 종류·역할을 자유 서술이 아니라 기계가 읽을 수 있는 능력 목록으로 만들어 두어야 이후 배정·계획 단계가 그것을 쓸 수 있을 것으로 보인다. [추정][^ref-090][^ref-677]

자세한 내용은 주제 페이지 [10. 채팅으로 로봇 구성 — 왜 중요한가](../../topics/2026/2026-09-29-area10-s3.md)에 있다.

## 4. 핵심 개념과 용어

**연합 형성(Coalition Formation)** — 자연어 지시를 작업 분해 → 연합 형성 → 작업 배정의 세 단계로 나누는 SMART-LLM 에서, 하나의 하위 작업을 맡을 로봇 팀을 능력에 맞춰 고르는 단계다. [사실][^ref-090] - **어포던스(Affordance)** — SayCan 은 언어 모델이 제안한 고수준 행동 후보를 스킬별 가치 함수가 현재 환경에서 실행 가능한지로 점수화해 결합하며, 이 실행 가능성 점수가 어포던스다. [사실][^ref-088]

자세한 내용은 주제 페이지 [10. 채팅으로 로봇 구성 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area10-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 물류창고

**사례:** 작업자 피킹(picker-to-parts) 창고의 피킹 단계에 협동 자율이동로봇을 몇 대 둘지 정하기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 수요 밀도와 배치 크기에 따라 발생하는 피킹 주문이 [차량 소요대수 산정(Fleet Sizing)](../../glossary/fleet-sizing.md)의 입력 요인이다. [사실][^ref-822] |
| 작업 대상 | 작업자가 상품을 집는 피킹 작업과 그 주문이다. [사실][^ref-822] |
| 수행 자원 | 작업자(피커)와 협동 자율이동로봇이며, 비용 기준 최적 로봇 대 작업자 비율은 수요에 따라 1:1 에서 2.5:1 로 옮겨 간다. [사실][^ref-822] |
| 제약 | 구독형(Robotics-as-a-Service) 과금 아래에서 작업자 유휴 비용이 로봇 유휴 비용의 약 2.5배인 비용 구조다. [사실][^ref-822] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 처리량 기준 산정은 구독형 과금에서 대수를 과대 산정하며, 배차 휴리스틱 차이는 통계적으로 유의하지 않았다. [사실][^ref-822] |

Howard 의 학위논문은 FlexSim [이산 사건 시뮬레이션](../../glossary/discrete-event-simulation.md) 27,000회, [반개방형 대기행렬](../../glossary/semi-open-queueing-network.md), XGBoost 대리모델로 이 결과를 얻었다(2026-06). [사실][^ref-822] 이 사례에서 채팅으로 로봇 구성이 관여하는 칸은 수행 자원의 대수이며, 대화는 그 값을 직접 정하는 대신 산정 결과와 비용 목적을 사용자에게 되묻는 자리가 될 것으로 보인다. [추정][^ref-822][^ref-823]

**현장 유형:** 제조 공장

**사례:** 공장의 공정 간 이송에 투입할 자율이동로봇 대수 정하기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 일일 목표 이송 횟수와 시간당 적재량이 대수를 정하는 입력이다. [추정] 벤더 주장[^ref-823] |
| 작업 대상 | 공정 사이를 오가는 이송물이며, 공정 수가 대수에 직접 영향을 준다. [추정] 벤더 주장[^ref-823] |
| 수행 자원 | 자율이동로봇이며 몇 대를 둘지가 산정 대상이다. [추정] 벤더 주장[^ref-823] |
| 제약 | 출발지–목적지 평균 이동 거리·속도와 MES·엘리베이터 등 기존 설비 연동 여부다. [추정] 벤더 주장[^ref-823] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 도입 전 전문가 인터뷰나 시뮬레이션 사전 분석이 필수이며, 투자 수익은 인건비 절감·생산성 향상으로 계산한다. [추정] 벤더 주장[^ref-823] |

이 사례의 근거는 국내 자율이동로봇 업체 폴라리스3D 의 블로그(2026-06-12)이며, 독립 출처로 확인되지 않은 벤더 주장이다. [추정] 벤더 주장[^ref-823] 대화형 구성 관점에서는 위 입력값 가운데 설비 연동 여부처럼 등록 데이터에서 읽을 수 있는 것과 목표 이송 횟수처럼 사용자에게 물어야 하는 것이 갈릴 것으로 보인다. [추정][^ref-823][^ref-105]

**현장 유형:** 병원

**사례:** 수술기구 분류 라인 4개의 라인·작업 조정을 운영자가 자연어로 요청하기(가상 라인)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 운영자가 자연어로 라인·작업 조정을 요청한다. [사실][^ref-759] |
| 작업 대상 | 가상의 수술기구 분류 라인 4개다. [사실][^ref-759] |
| 수행 자원 | 로컬 언어 모델이 구조화 요구사항과 후보 전략을 만들고, 디지털 트윈 시뮬레이션이 실행 가능성을 검증하며, 운영자가 최종 결정한다. [사실][^ref-759] |
| 제약 | 의미 정확성·시뮬레이션 실행·운영 제약 검사를 통과해야 하며, 시뮬레이션 검증은 평균 164.39초가 걸렸다. [사실][^ref-759] |
| 완료·인계 | 최종 검토에 도달한 4건이 모두 통과했고, 요청–검증 근거–결정을 잇는 추적 기록이 남는다. [사실][^ref-759] |
| 예외·성과 | 시험 사례 18건 가운데 잘못된 입력 8건 중 7건을 검증 단계에서 거부했고, 자율 전략 성공은 10건 중 3건, 배치 검증 통과율은 97.50% 였다. [사실][^ref-759] |

Ko·Lin(2026)은 이 흐름을 '제안–검증–결정'으로 부른다. [사실][^ref-759] 출처는 현장 유형을 명시하지 않으며, 수술기구 분류 라인이라는 점에서 이 위키가 병원·의료로 분류했고, 물리 로봇이 아닌 가상 라인이라는 점을 함께 둔다. [추정][^ref-759] 이 사례가 이 영역에 뜻하는 바는 잘못된 구성 요청을 실행 전 검증 단계에서 걸러 내고 결정 근거를 추적 가능하게 남기는 구조다. [추정][^ref-759]

이번 실행의 브리프에는 실외·상업 시설·가정 현장의 사례가 없다.

## 6. 대표 접근법과 기술

대화로 정한 로봇 구성이 시나리오를 수행할 수 있는지는 언어 모델 단독이 아니라 능력 모델·계획기·시뮬레이션·사람 검토를 잇는 흐름으로 확인하는 접근이 여러 연구에서 공통으로 나타난다. [추정][^ref-819][^ref-759][^ref-674]

자세한 내용은 주제 페이지 [10. 채팅으로 로봇 구성 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area10-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역이 대화로 정하려는 값의 자리는 관제가 실제로 읽는 구조에 이미 마련돼 있다. [추정][^ref-031][^ref-105]

자세한 내용은 주제 페이지 [10. 채팅으로 로봇 구성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area10-s7.md)에 있다.

## 8. 대표 연구와 자료

Kannan·Venkatesh·Min, SMART-LLM(2023) — 자연어 지시를 작업 분해·연합 형성·작업 배정으로 바꾸는 언어 모델 다중 로봇 계획 프레임워크와 벤치마크. 이 영역의 '팀 구성' 단계에 해당한다. [사실][^ref-090] - Borate 외, CoMuRoS(2025) — 중앙 작업 관리자 언어 모델과 로봇별 언어 모델을 결합한 이기종 로봇 팀 계층 계획·실행. 하드웨어 실험 성공률과 텍스트 벤치마크 정확도 최대 0.91 을 보고한다. [사실][^ref-677]

자세한 내용은 주제 페이지 [10. 채팅으로 로봇 구성 — 대표 연구와 자료](../../topics/2026/2026-09-29-area10-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 대화를 구조화 구성(종류·대수·장비·위치·역할)으로 바꾸고, 온톨로지의 요구·제공 능력으로 적합성을 확인해 부족을 알린 뒤 사람이 승인한 구성만 확정하는 일. [추정][^ref-677][^ref-088][^ref-229] | 로봇별 언어 모델이 ROS 2 기본 스킬에서 실행 코드를 만드는 일(CoMuRoS)과 스킬의 가치 함수로 현재 장면의 실행 가능성을 점수화하는 일(SayCan). [추정][^ref-677][^ref-088] |
| 시설·설비 제어 | 구성 단계에서 MES·엘리베이터 등 기존 설비 연동 여부를 제약으로 받아 대수·역할에 반영하는 일. [추정] 벤더 주장[^ref-823] | 승강기·컨베이어·설비 제어 자체. |

위 표는 분류 원문 19장의 경계를 이 영역에 맞게 고쳐 쓴 것이며, 기준은 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

이 영역에서 이종 제조사를 연결하는 ROP가 맡는 인터페이스는 대화 결과를 팩트시트·플릿 설정 같은 관제가 읽는 구조화 값으로 내는 일이고, 실행 보장은 확정 전 적합성 확인과 사람 승인일 것으로 보인다. [추정][^ref-031][^ref-105][^ref-229]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md) — 원문 주석이 로봇 구성의 엔진 짝으로 드는 영역이다. 요구·제공 능력을 같은 모델로 적는 능력 기술과 그 모델에서 계획을 만드는 연구가 이 영역의 적합성 확인 엔진이 될 것으로 보인다. [추정][^ref-229][^ref-201]

자세한 내용은 주제 페이지 [10. 채팅으로 로봇 구성 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area10-s10.md)에 있다.

## 11. 열린 질문

(id 퍼블리셔 부여 · 상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-02) 대화로 로봇 종류·대수·장비·역할을 정하고 수행 가능 여부를 판정하는 기능을 평가할 공개 벤치마크나 지표(적합성 판정 정확도, 질문 횟수, 구성 완료 시간)가 있는가? 13. 대화형 기능의 신뢰·기반의 대화형 기능 평가 항목과 함께 본다. [추정][^ref-759]

자세한 내용은 주제 페이지 [10. 채팅으로 로봇 구성 — 열린 질문](../../topics/2026/2026-09-29-area10-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-29
[^ref-677]: Borate, S., Rai B, B., Pardeshi, V., & Vadali, M., LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning, 2025-11-27, https://arxiv.org/abs/2511.22354, 접근일 2026-09-29
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09-18, https://arxiv.org/abs/2309.10062, 접근일 2026-09-29
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-29
[^ref-229]: IDTA (Industrial Digital Twin Association, admin-shell-io GitHub), IDTA 02020 Submodel Template Capability Description — README (published/Capability Description/1/0), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-29 (원문 미열람)
[^ref-819]: Valerio, D., Kogler, P., Bischof, S., Hubauer, T., & Rangwala, H., Neuro-symbolic AI for Industrial Configuration, 2026-09-24, https://arxiv.org/abs/2609.29947, 접근일 2026-09-29
[^ref-088]: Ahn, M., Brohan, A., Brown, N., Chebotar, Y. 외 (Google/Everyday Robots), Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-29
[^ref-201]: Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. (IEEE CASE 2026), From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation, 2026-06-01, https://arxiv.org/abs/2606.02167, 접근일 2026-09-29
[^ref-822]: Howard, T. L. (California Polytechnic State University, 석사논문), A Simulation, Analytical, and Machine-Learning Approach for Collaborative Autonomous Mobile Robot Fleet Sizing in Picker-to-Parts Facilities, 2026-06, https://digitalcommons.calpoly.edu/theses/3387/, 접근일 2026-09-29
[^ref-823]: 폴라리스3D(Polaris3D), AMR 도입 ROI 어떻게 계산할까? 물류 자동화 투자 회수 기간 알아보기, 2026-06-12, https://polaris3d.com/blog/trends/amr-roi-calculator/, 접근일 2026-09-29
[^ref-759]: Ko, T.-H., & Lin, C.-T., Human-AI Collaboration for Multi-Line Task Adjustment Using Local Large Language Models and a Digital Twin, 2026-09-24, https://arxiv.org/abs/2609.29061, 접근일 2026-09-29
[^ref-674]: Liu, Z., Fernandez-Ayala, V. N., Wang, T., Qin, Q., Wang, X. V., Dimarogonas, D. V., & Wang, L., Agentic Neuro-Symbolic Planning and Commissioning for Human-in-the-Loop Industrial Robotics with Digital Twins, 2026-06-06, https://arxiv.org/abs/2606.08214, 접근일 2026-09-29
