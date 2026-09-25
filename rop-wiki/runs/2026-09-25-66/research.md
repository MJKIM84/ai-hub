# 리서치 브리프 2026-09-25-66

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-66 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 13. 작업 배정 — MRTA |
| 대분류 | D. 계획·최적화 |

트랙 실행: 트랙 `nl-task-chatbot` · 단계 3 · 답한 질문 q3-01

## 갭(비어 있거나 약한 섹션)

- 단계 3 질문 q3-01 열림(target.json 지정, CLI 지정 질문 id). 단계 3 페이지 3~6·8절 비어 있음(단계 3 첫 실행)
- 완료 조건: 아이디어 2. 자연어 업무 지시 챗봇 5절(구현 가설)에 처리 흐름·핵심 구성 요소 없음
- 완료 조건: 업무 분해·배정 설계 초안의 일정(Schedule) 개념이 '초안' 상태이고 계산 주체(6절 질문 '일정을 누가 계산하는가')가 미정
- 완료 조건: 실험 페이지에 단계 3 실험 계획 없음
- 14. 작업 순서·스케줄링 페이지에 LLM 직접 스케줄 생성과 최적화 해법 결합의 비교 근거 없음
- 27. AI·학습·적응과 모델 운영 페이지 seed 상태: LLM 의 스케줄링 적용 기준 근거 없음

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. q3-01 스케줄링 결정은 LLM과 최적화 엔진 중 어디에 맡기는가?
3. LLM 이 스케줄을 직접 생성할 때 제약 만족(실행 가능성)과 최적성은 해법기 대비 어느 수준이며, 어떤 조건에서 무너지는가? (단계 3 페이지 3절, 14. 작업 순서·스케줄링 겨냥)
4. LLM 이 문제를 정식화·인스턴스화하고 해법기·계획기가 푸는 결합 구조(LLM+P, OptiMUS, LAPPI 등)는 역할을 어떻게 나누는가? (27. AI·학습·적응과 모델 운영 겨냥)
5. 실시간 재스케줄링에서 LLM 추론 지연을 어떻게 다루는가(규칙·휴리스틱을 LLM 이 오프라인으로 만들고 결정적 실행기가 쓰는 구조)? (20. 예외 복구·재계획·업무 연속성 연결)
6. 기존 로봇 오케스트레이션 도구(Open-RMF rmf_task, VDA 5050 관제 기능)는 스케줄링·충전 삽입을 어떤 구성 요소에 두는가? (9. 로봇·제조사 관제 연동, 16. 공용 자원·충전·에너지 최적화 연결)
7. 국내에 LLM 과 최적화 엔진의 스케줄링 역할 분담을 다룬 연구·사례가 있는가? (한국 자료 우선 규칙)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF rmf_task 의 TaskPlanner 는 플릿 안의 작업과 로봇을 받아 요청된 시작 시각을 지키며 작업이 가장 짧게 끝나도록 로봇별 작업 순서를 정하고, 배터리 같은 자원 제약을 고려해 필요하면 충전 작업을 일정에 자동으로 끼워 넣는다. | ref-404, ref-377 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f2 | [사실] | rmf_task TaskPlanner 는 최적성을 보장하지 않지만 빠른 탐욕(greedy) 방식과 최적성을 보장하지만 오래 걸릴 수 있는 A* 기반 방식 가운데 하나로 배정을 풀고, 비용 계산기를 지정하지 않으면 BinaryPriorityCostCalculator 를 쓰며, 각 로봇의 배정 끝에 수행할 마무리 작업(예: 충전)을 만드는 요청 생성기를 옵션으로 받는다. | ref-377 | 아니오 | medium | 2026-09-25 | — | — |
| f3 | [사실] | Open-RMF 에서는 디스패처가 입찰 공고를 보내면 각 플릿 어댑터가 TaskPlanner 로 비용을 계산해 입찰하고, 디스패처가 가장 빨리 끝나는 것·가장 낮은 비용 같은 설정 기준으로 비교해 작업을 줄 플릿을 정한다. | ref-376 | 아니오 | medium | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f4 | [사실] | VDA 5050 3.0.0 은 관제의 최소 기능으로 주문 배정, 에너지 관리(충전 주문이 운반 주문을 중단할 수 있음), 교통 제어를 두면서도 경로·우선순위·혼잡 처리 같은 교통 관리 전략·알고리즘은 범위에서 제외해, 배정·일정 결정 로직을 관제 구현에 맡긴다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f5 | [사실] | LLM+P 는 LLM 이 자연어 계획 문제를 PDDL 문제 파일로 바꾸고 고전 계획기 Fast Downward 가 계획을 구하는 구조이며, LLM 이 계획을 직접 내는 방식(LLM-as-Planner)과 문맥 예시 유무를 바꾼 기준선을 barman·blocksworld 등 7개 도메인에서 비교한다. | ref-091 | 아니오 | medium | 2026-09-25 | — | — |
| f6 | [사실] | LLM+P 논문 저자들은 GPT-4 기반 실험에서 LLM+P 가 LLM-as-Planner 보다 훨씬 많은 계획 문제를 풀었고, LLM 이 계획을 직접 내는 방식은 공간 관계가 복잡한 문제에서 완전히 실패했으며, 문맥 예시가 없으면 LLM+P 도 실패했다고 보고했다. | ref-092 | 아니오 | medium | 2023-04 | — | 원문 미열람 |
| f7 | [의견] | Kambhampati 외(ICML 2024 입장 논문)는 자기회귀 LLM 이 혼자서는 계획이나 자기 검증을 하지 못한다고 보고, LLM 을 근사적 아이디어 생성기로 두고 외부 모델 기반 검증기·비평자와 양방향으로 결합하는 LLM-Modulo 틀을 제안한다. | ref-674 | 아니오 | medium | 2024-02 | — | 원문 미열람 |
| f8 | [사실] | ConstraintBench 저자들은 10개 운영과학 영역에서 LLM 이 제약 최적화 문제를 직접 풀게 했을 때 가장 좋은 모델의 실행 가능 해 비율이 65.0%였고, 실행 가능한 해는 Gurobi 최적값의 평균 89~96% 수준이었지만 실행 가능성과 최적성을 함께 만족한 비율은 어느 모델도 30.5%를 넘지 못했으며 영역별 실행 가능 비율은 0.8~85.0%였다고 보고했다. | ref-675 | 아니오 | medium | 2026-02 | 예외·성과 | 원문 미열람 |
| f9 | [사실] | R-ConstraintBench 저자들은 자원 제약 프로젝트 스케줄링 문제(RCPSP)에서 강한 LLM 도 선후 제약만 있을 때는 실행 가능성이 천장에 가깝지만 정지 시간·시간창·배타(disjunctive) 제약이 함께 걸리면 실행 가능성이 급락하며, 병목은 그래프 깊이가 아니라 제약 사이의 상호작용이라고 보고했다. | ref-676 | 아니오 | medium | 2025-08 | 제약 | 원문 미열람 |
| f10 | [사실] | SCHEDBench 저자들은 작업장·자원 제약 프로젝트·간호사 근무·시간표 스케줄링 1,132개 사례로 13개 LLM 을 평가해, 같은 문제를 다른 문장 표현으로 주면 실행 가능 비율이 떨어지고 제약 위반이 달라지며 제약 순서 바꾸기에 가장 민감했다고 보고했다. | ref-677 | 아니오 | medium | 2026-08 | 예외·성과 | 원문 미열람 |
| f11 | [사실] | Starjob 저자들은 작업장 스케줄링 문제(JSSP) 13만 개 사례를 자연어로 기술한 지도 학습 데이터셋으로 Llama 8B 를 미세 조정하면 실행 가능한 스케줄을 생성하고 우선순위 디스패치 규칙과 초기 신경망 방법(L2D)보다 DMU 평균 15.36%, Taillard 평균 7.85% 개선된다고 보고했다. | ref-678 | 아니오 | medium | 2025-03 | — | 원문 미열람 |
| f12 | [사실] | DynaSchedBench 저자들은 동적 유연 작업장 스케줄링에서 LLM 스케줄러에 전체 구조 정보를 주면 간결한 통계 요약을 줄 때보다 성능이 나빠졌고(1.66% 대 0.65%), 도구를 쓰는 탐색은 토큰 비용이 약 3배인데 성능은 더 낮았으며, 현재 LLM 은 참된 최적화기보다 정교한 휴리스틱처럼 동작한다고 보고했다. | ref-682 | 아니오 | medium | 2026-05 | 예외·성과 | 원문 미열람 |
| f13 | [사실] | RACE-Sched 는 LLM 추론 지연이 산업 제어의 밀리초 단위 결정 주기와 맞지 않는다고 보고, 실시간 디스패치는 저지연 기호 휴리스틱이 맡고 병렬 흐름에서 LLM 이 규칙을 합성·검증·진화시킨 뒤 샌드박스 시험을 거쳐 제어 루프를 막지 않는 원자적 갱신으로 배포하는 이중 흐름 구조를 제안했다. | ref-683 | 아니오 | medium | 2026-05 | 예외·성과 | 원문 미열람 |
| f14 | [사실] | Li·Li(칭화대)는 동적 생산·AGV 스케줄링의 이산 사건 시뮬레이션에서 LLM 관리 에이전트가 시뮬레이션 사건 기록으로 병목 가설을 세우고 편집 에이전트가 규칙 기반 정책 코드를 고치는 휴리스틱 설계 틀을 제안했으며, 결과 정책이 수리계획·휴리스틱·메타휴리스틱 기준선보다 나았다고 보고했다. | ref-684 | 아니오 | medium | 2026-08 | — | 원문 미열람 |
| f15 | [사실] | OptiMUS 는 LLM 이 자연어 문제 기술에서 (혼합 정수) 선형 계획 모델을 정식화하고 Gurobi 파이썬 API 코드로 옮겨 MIP 해법기가 최적해를 구하게 하는 구조이며, 순차형(v1)에서 에이전트형(v2), 검색 증강·대규모 기법(v3)으로 발전했고 각 LLM 구성 요소에 오류 검사 모듈을 둔다. | ref-679, ref-680 | 아니오 | medium | 2024-07 | — | — |
| f16 | [사실] | LAPPI 는 LLM 이 자연어 대화로 사용자의 모호한 선호를 후보 항목·선호 점수·제약으로 바꿔 최적화 문제를 인스턴스화하고 풀이는 기존 최적화 해법기에 맡기는 대화형 최적화 방식이며, 여행 계획 사용자 연구에서 기존 방식과 프롬프트만 쓴 방식보다 나은 실행 가능 계획을 냈다고 저자가 보고했다. | ref-681 | 아니오 | medium | 2025-12 | 시작 조건 | 원문 미열람 |
| f17 | [사실] | 운영과학(OR)에서의 LLM 적용을 정리한 서베이(Wang·Li)는 기존 방법을 자동 모델링, 보조 최적화(휴리스틱·알고리즘 설계), 직접 풀이의 세 경로로 나누고, 의미–구조 대응의 불안정, 일반화·해석 가능성 한계, 평가 체계 부족, 산업 배치 장벽을 과제로 든다. | ref-686 | 아니오 | medium | 2025-09 | — | 원문 미열람 |
| f18 | [사실] | PortAgent 는 자동화 컨테이너 터미널의 차량 디스패칭 시스템을 새 터미널로 옮기는 작업을 LLM 가상 전문가 팀(지식 검색·모델러·코더·디버거)이 자동화하는 방식으로, LLM 이 개별 배차 결정을 내리기보다 디스패칭 모델과 코드를 만들고 디버거가 정적 분석·샌드박스 실행으로 오류를 검사·수정한다. | ref-685 | 아니오 | medium | 2025-12 | — | 원문 미열람 |
| f19 | [사실] | Powell 외(Journal of Intelligent Information Systems 63권, 2025)는 스케줄링 시스템이 낸 결과를 사람에게 설명하는 텍스트를 LLM 의 추론(사고 사슬 프롬프트)으로 생성하는 방법을 연구했다. | ref-687 | 아니오 | medium | 2025 | — | 원문 미열람 |
| f20 | [사실] | Saha 외(arXiv 2605.15486)는 건설 로봇 작업 스케줄링에서 LLM 에 에이전트 행동 능력과 목표를 주고 생성 LLM(GPT-4)과 감독 LLM(Gemma 3·Llama 4·Mistral 7B)이 함께 스케줄을 만드는, 해법기 없이 LLM 이 일정을 직접 산출하는 틀을 제안했다. | ref-689 | 아니오 | medium | 2026-05 | — | 원문 미열람 |
| f21 | [사실] | 다중 로봇 LLM 연구 가운데 LiP-LLM(선형계획), PIP-LLM(정수계획), FLEET(makespan 최소화), Peng 외(MILP)는 LLM 이 의존 그래프·적합도·제약을 정식화하고 배정·일정은 결정적 해법이 푸는 분담을 쓴다. | ref-166, ref-181, ref-242, ref-167 | 아니오 | medium | 2025-10 | 수행 자원 | 원문 미열람 |
| f22 | [추정] | q3-01 에 대해, 확인한 자료로는 LLM 이 스케줄을 직접 만들면 제약이 겹치거나 표현이 바뀔 때 실행 가능성이 흔들리므로(ConstraintBench, R-ConstraintBench, SCHEDBench, DynaSchedBench), ROP 에서는 순서·시각·충전 삽입 같은 스케줄링 결정은 rmf_task 같은 결정적 최적화·계획 해법이 맡고 LLM 은 지시에서 목적·제약·기한을 뽑아 문제를 인스턴스화하는 일(LLM+P, OptiMUS, LAPPI)과 결과 설명을 맡는 분담이 근거가 가장 많은 것으로 보인다. | ref-675, ref-676, ref-677, ref-682, ref-377, ref-092, ref-679, ref-681, ref-687 | 아니오 | low | 2026-09-25 | — | — |
| f23 | [추정] | 직접 생성의 반례로, 미세 조정한 LLM 이 작업장 스케줄링에서 규칙·초기 신경망 방법을 앞섰다는 보고(Starjob)와 LLM 두 개가 건설 로봇 스케줄을 직접 만든 연구가 있어, LLM 직접 스케줄링이 배제되는 것은 아니지만 그 비교 대상이 정확 해법기가 아니거나 확인되지 않아 해법기 대체의 근거로는 약한 것으로 보인다. | ref-678, ref-689, ref-675 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f24 | [추정] | 진행 중 고장·새 지시 같은 동적 사건에 대한 재스케줄링은 LLM 추론 지연 때문에 결정 루프 안에 LLM 을 두기 어렵고, RACE-Sched·Li·Li 처럼 LLM 은 규칙·정책을 루프 밖에서 만들어 시뮬레이션·샌드박스 검증을 거쳐 반영하며 실시간 재계산은 해법기(rmf_task 의 충전 삽입·재배정)가 맡는 구조가 ROP 의 선택지로 보인다. | ref-683, ref-684, ref-377, ref-674 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f25 | [추정] | 분류 원문 질문(가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가)과 관련해, 전체 이익은 완료 시각·비용 같은 명시적 목적함수를 최적화하는 해법(rmf_task, 선형·정수계획)이 계산·비교할 수 있지만, LLM 직접 배정·스케줄은 실행 가능하더라도 최적성과 함께 만족하는 비율이 낮게 보고되어 전체 이익을 보장하는 수단으로 쓰기 어려운 것으로 보인다. | ref-377, ref-166, ref-675 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f26 | [추정] | 출하 마감 전에 채팅으로 긴급 출고 지시가 들어오면, LLM 은 지시에서 기한·우선순위를 뽑아 문제 인스턴스(제약·목적 가중치)로 바꾸고 해법기가 충전 삽입을 포함한 일정을 다시 계산한 뒤 LLM 이 바뀐 일정과 이유를 설명하는 흐름이 가능해 보인다. | ref-681, ref-377, ref-687 | 아니오 | low | 2026-09-25 | 출하 / 제약 | — |
| f27 | [추정] | 이번에 확인한 LLM 스케줄링 근거의 평가 환경은 작업장·프로젝트·근무표 스케줄링, 운영과학 일반 문제, 건설 로봇, 컨테이너 터미널, 여행 계획이었고, 이종 제조사 창고 로봇 플릿에서 LLM 직접 스케줄과 해법기를 비교한 자료는 검색 범위에서 찾지 못했다(부재의 확인은 아님). | ref-675, ref-676, ref-677, ref-678, ref-689, ref-685, ref-681 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

- **f1**: README: planner "solves the problem of optimal allocation of tasks among available robots", 충전 작업 자동 삽입("automatically injects recharging tasks"). 같은 저장소의 README·헤더라 독립 교차 아님 (발행일 미확인, 확인일 기준)
- **f2**: TaskPlanner.hpp Options 주석: greedy "Optimality is not guaranteed but the solution time may be faster" / A* "guarantees optimality but may take longer to solve" (발행일 미확인, 확인일 기준)
- **f3**: BidNotice → BidProposal(비용) → DispatchRequest, 평가 기준은 fastest to finish, lowest cost 등으로 설정 가능 (재인용: 2026-09-25-33)
- **f4**: 5.3 절: "Energy management: Charging orders can interrupt transfer orders". 2절 범위 제외: Traffic Management Logic(routing, prioritization, congestion handling …) (VDA 5050 3.0.0, main 브랜치, 발행일 미확인, 확인일 기준)
- **f5**: README: 계획기 Fast-Downward, 기준선 "llm -> plan does not generate pddl" 대 제안 "llm + context -> p.pddl", 도메인 7개 (발행일 미확인, 확인일 기준)
- **f6**: 저자 보고: GPT-4 가 만든 PDDL 을 Fast Downward(SEQ-OPT-FDSS-1, LAMA, 탐색 한도 200초)에 넘김. 검색 요약 기준, 원문 미열람
- **f7**: 입장 논문(position paper)의 주장. LLM 은 계획기 자체가 아니라 외부 검증기와 결합된 생성기 역할이라는 평가. 검색 요약 기준, 원문 미열람
- **f8**: 저자 보고값, 정답은 Gurobi 로 산출. 실패 유형: 소요 시간 제약 오해, 존재하지 않는 개체 생성(entity hallucination). 검색 요약 기준, 원문 미열람
- **f9**: 저자 보고, 데이터센터 이전 시나리오로 예시. 합성 난이도 증가 결과가 현장형 시나리오로 옮겨지지 않는다고도 밝힘. 검색 요약 기준, 원문 미열람
- **f10**: 저자 보고: LLM 이 완성 스케줄을 직접 내게 하고 영역별 검사기로 제약을 검사. 의미가 같은 표현에 불변이지 않음. 검색 요약 기준, 원문 미열람
- **f11**: 저자 보고값, 비교 대상은 우선순위 디스패치 규칙·L2D 이며 정확 해법기(OR-Tools 등)와의 비교는 검색 요약에서 확인되지 않음. 원문 미열람
- **f12**: 저자 보고값(지표의 정의는 검색 요약에서 미확인). 'observability paradox'로 명명. 검색 요약 기준, 원문 미열람
- **f13**: Reactive Stream(휴리스틱 실시간 디스패치) / Deliberative Stream(LLM 규칙 합성). 동적 유연 작업장 벤치마크에서 DRL·LLM 기준선보다 낫다는 것은 저자 보고. 검색 요약 기준, 원문 미열람
- **f14**: 저자 보고(2026-08 프리프린트). LLM 은 개별 스케줄이 아니라 정책(코드)을 설계하고, 평가는 반복 시뮬레이션으로 한다. 검색 요약 기준, 원문 미열람
- **f15**: README: V1 "Sequential work-flow implementation. Suitable for small and medium-sized problems." 논문(0.3)은 LaTeX 모델→gurobipy 코드→실행으로 최적해 출력. 같은 저자 계열이라 독립 교차 아님
- **f16**: 저자 보고, 여행 계획 조건. '맥락 이해'와 '풀이 논리'를 분리해 LLM 을 해법기가 아니라 문제 인스턴스화 인터페이스로 쓴다는 설계. 검색 요약 기준, 원문 미열람
- **f17**: 서베이의 세 경로: automatic modeling / auxiliary optimization / direct solving. 검색 요약 기준, 원문 미열람
- **f18**: 저자 주장 특징: 항만 전문가 불필요, 적은 데이터, 빠른 배치(2025-12 프리프린트). 성능 수치는 검색 요약에서 미확인. 원문 미열람
- **f19**: LLM 이 스케줄을 만드는 것이 아니라 스케줄링 시스템 출력의 정당화 설명을 만드는 역할. 63권 1287–1337쪽. 검색 요약 기준, 원문 미열람
- **f20**: 시간 효율·자원 활용을 함께 고려한 배정 전략이라고 저자가 밝힘. 해법기 대비 정량 비교는 검색 요약에서 미확인. 원문 미열람
- **f21**: 각 논문의 방법 서술 요약(저자별 단일 출처, 원문 미열람) (재인용: 2026-09-25-21)
- **f22**: 이 위키의 종합. 반례로 좁은 문제(JSSP)에 미세 조정한 LLM 이 실행 가능 스케줄을 낸 보고(Starjob)가 있으나 정확 해법기와의 비교는 미확인
- **f23**: 이 위키의 종합. Starjob 비교 대상은 PDR·L2D, Saha 외는 해법기 비교 미확인, ConstraintBench 는 Gurobi 기준
- **f24**: 이 위키의 종합. 물류 로봇 플릿에서 허용 가능한 LLM 지연 한계를 잰 자료는 찾지 못함
- **f25**: 이 위키의 종합. ConstraintBench 결합 만족 30.5% 이하는 저자 보고값이며 운영과학 일반 문제 조건
- **f26**: 설명용 시나리오 구성(이 위키의 추론). LAPPI 인스턴스화, rmf_task 재계획·충전 삽입, 스케줄 설명 생성 연구를 대응시킴
- **f27**: 이 위키의 관찰. 한국어 검색 3회에서도 해당 국내 자료를 찾지 못함

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-674 | Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S., Saldyt, L., & Murthy, A. | LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks | 2024-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2402.01817 | 예 |
| ref-675 | ConstraintBench 저자(arXiv 2602.22465, 저자 미확인) | ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization | 2026-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2602.22465 | 예 |
| ref-676 | Jain, R. 외(R-ConstraintBench 저자) | R-ConstraintBench: Evaluating LLMs on NP-Complete Scheduling | 2025-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2508.15204 | 예 |
| ref-677 | SCHEDBench 저자(arXiv 2608.00991, 저자 미확인) | SCHEDBench: A Benchmark for Evaluating LLM Constraint Faithfulness in Natural-Language Combinatorial Scheduling | 2026-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2608.00991 | 예 |
| ref-678 | Starjob 저자(arXiv 2503.01877, 저자 미확인) | Starjob: Dataset for LLM-Driven Job Shop Scheduling | 2025-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2503.01877 | 예 |
| ref-679 | teshnizi (OptiMUS 공식 저장소) | OptiMUS — Optimization Modeling Using mip Solvers and large language models (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/teshnizi/OptiMUS | 아니오 |
| ref-680 | AhmadiTeshnizi, A. 외(OptiMUS 저자) | OptiMUS-0.3: Using Large Language Models to Model and Solve Optimization Problems at Scale | 2024-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2407.19633 | 예 |
| ref-681 | Nakagawa, M., Koyama, Y. 외(OMRON SINIC X, LAPPI 저자) | LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation | 2025-12 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2512.14138 | 예 |
| ref-682 | DynaSchedBench 저자(arXiv 2605.27566, 저자 미확인) | DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents | 2026-05 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2605.27566 | 예 |
| ref-683 | RACE-Sched 저자(arXiv 2605.29262, 저자 미확인) | Harmonizing Real-Time Constraints and Long-Horizon Reasoning: An Asynchronous Agentic Framework for Dynamic Scheduling | 2026-05 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2605.29262 | 예 |
| ref-684 | Li, J., & Li, C.(칭화대학교 산업공학과) | LLM-Guided Heuristic Design from Simulation Traces: A Case Study in Dynamic Production and AGV Scheduling | 2026-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2608.09343 | 예 |
| ref-685 | Hu, J., Li, J., Lin, W., Jia, P., Ji, Y., & Lai, J. | PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals | 2025-12 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2512.14417 | 예 |
| ref-686 | Wang, Y., & Li, K. | Large Language Models in Operations Research: Methods, Applications, and Challenges | 2025-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2509.18180 | 예 |
| ref-687 | Powell, C. 외(University of Strathclyde) | Generating textual explanations for scheduling systems leveraging the reasoning capabilities of large language models | 2025 | 논문 | medium | 2026-09-25 | https://link.springer.com/article/10.1007/s10844-025-00940-w | 예 |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp | 아니오 |
| ref-689 | Saha, S., Das, S., Duan, H., & Liu, X.-Y. | Hybrid LLM-based Intelligent Framework for Robot Task Scheduling | 2026-05 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2605.15486 | 예 |
| ref-404 | Open Robotics (open-rmf) | rmf_task — README | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_task | 아니오 |
| ref-376 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task.html | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-091 | Cranial-XIX (LLM+P 저자) | llm-pddl — LLM+P: Empowering Large Language Models with Optimal Planning Proficiency (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/Cranial-XIX/llm-pddl | 아니오 |
| ref-092 | Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P. | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2304.11477 | 예 |
| ref-166 | Obata, K., Aoki, T., Horii, T., Taniguchi, T., & Nagai, T. | LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning | 2024-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2410.21040 | 예 |
| ref-167 | Peng, M., Chen, Z., Yang, J., Huang, J., Shi, Z., Liu, Q., Li, X., & Gao, L. | Automatic MILP Model Construction for Multi-Robot Task Allocation and Scheduling Based on Large Language Models | 2025-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2503.13813 | 예 |
| ref-181 | Shi, G., Wu, Y., Kumar, V., & Sukhatme, G. S. | PIP-LLM: Integrating PDDL-Integer Programming with LLMs for Coordinating Multi-Robot Teams Using Natural Language | 2025-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2510.22784 | 예 |
| ref-242 | Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D.(JHU APL·JHU·DEVCOM ARL) | FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams | 2025-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2510.07417 | 예 |

### 출처 요약

- **ref-674**: 원문 미열람. ICML 2024 입장 논문. LLM 단독 계획·자기 검증의 한계를 주장하고 외부 검증기와 결합하는 LLM-Modulo 틀을 제안.
- **ref-675**: 원문 미열람. 10개 운영과학 영역에서 LLM 직접 풀이의 실행 가능성·최적성을 Gurobi 정답과 비교한 벤치마크.
- **ref-676**: 원문 미열람. 자원 제약 프로젝트 스케줄링에서 제약을 늘려 가며 LLM 실행 가능성이 무너지는 지점을 평가.
- **ref-677**: 원문 미열람. 1,132개 스케줄링 사례로 13개 LLM 의 직접 스케줄 생성이 문장 표현 변화에 얼마나 흔들리는지 평가.
- **ref-678**: 원문 미열람. 작업장 스케줄링 13만 사례 자연어 데이터셋과 미세 조정 Llama 8B 의 직접 스케줄 생성 결과.
- **ref-679**: LLM 이 자연어 문제를 MIP 모델로 정식화하고 해법기로 푸는 OptiMUS 의 판별 구성과 NLP4LP 데이터셋 안내.
- **ref-680**: 원문 미열람. LaTeX 모델→gurobipy 코드→실행으로 최적해를 내는 OptiMUS-0.3 과 오류 검사 모듈.
- **ref-681**: 원문 미열람. LLM 이 대화로 최적화 문제를 인스턴스화하고 해법기가 푸는 대화형 최적화(IEEE 학술지 게재 기록 있음).
- **ref-682**: 원문 미열람. 동적 유연 작업장 스케줄링에서 LLM 스케줄러의 관측 정보 수준별 성능과 도구 탐색 비용을 평가.
- **ref-683**: 원문 미열람. 실시간 휴리스틱 디스패치와 LLM 규칙 합성을 분리한 비동기 이중 흐름 스케줄링 틀.
- **ref-684**: 원문 미열람. 시뮬레이션 사건 기록으로 LLM 에이전트가 생산·AGV 스케줄링 휴리스틱 코드를 개선하는 틀.
- **ref-685**: 원문 미열람. LLM 가상 전문가 팀이 컨테이너 터미널 차량 디스패칭 시스템의 이전(모델·코드 작성·디버깅)을 자동화.
- **ref-686**: 원문 미열람. 운영과학의 LLM 적용을 자동 모델링·보조 최적화·직접 풀이로 분류한 서베이.
- **ref-687**: 원문 미열람. Journal of Intelligent Information Systems 63권. 스케줄링 시스템 출력의 설명문을 LLM 으로 생성.
- **ref-377**: TaskPlanner API 헤더. 탐욕·A* 풀이 옵션, 비용 계산기 기본값, 마무리(충전) 요청 생성기, plan 함수를 정의.
- **ref-689**: 원문 미열람. 생성·감독 LLM 두 개로 건설 로봇 작업 스케줄을 직접 만드는 틀.
- **ref-404**: rmf_task 의 작업 배정·순서 계획(TaskPlanner)과 충전 작업 자동 삽입을 소개하는 README.
- **ref-376**: 원문 미열람. 이번 실행에서 다시 열지 않음. 디스패처–플릿 어댑터 입찰 기반 작업 배정 설명.
- **ref-031**: VDA 5050 3.0.0 명세 원문(입력 원문 텍스트). 범위·관제 기능·주문·동작을 규정.
- **ref-091**: LLM+P 공식 저장소 README. Fast Downward 계획기, 7개 도메인, 비교 방법 구성.
- **ref-092**: 원문 미열람. LLM 이 PDDL 을 만들고 고전 계획기가 푸는 LLM+P 와 LLM-as-Planner 비교.
- **ref-166**: 원문 미열람. LLM 의존 그래프 + 선형계획 배정.
- **ref-167**: 원문 미열람. 자연어 작업 기술을 MILP 모델·코드로 바꾸는 다중 로봇 배정·스케줄링.
- **ref-181**: 원문 미열람. 팀 수준 PDDL 계획 뒤 정수계획으로 로봇 배정.
- **ref-242**: 원문 미열람. LLM 작업 그래프·적합도 행렬 + makespan 최소화 형식적 뒷단.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md | 2, 3, 4, 5, 6, 8, 9 | q3-01 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21·f22·f23·f24·f25·f26·f27 (신뢰도 low) — 2절 q3-01 상태 답함, 3절 q3-01 소제목 신설({#q3-01}): 오케스트레이션 도구의 스케줄링 위치(rmf_task f1·f2, Open-RMF 입찰 f3, VDA 5050 관제 기능 f4), LLM 직접 스케줄 생성의 한계(f8·f9·f10·f12, 입장 f7 의견)와 반례(f11·f20, f23), LLM+해법기 결합(LLM+P f5·f6, OptiMUS f15, LAPPI f16, 다중 로봇 f21, 서베이 f17), 루프 밖 규칙·정책 설계(f13·f14·f18), 설명 생성(f19), 분담 종합(f22)·동적 재스케줄링(f24)·SCM 질문 연결(f25)·출하 시나리오(f26)·물류 근거 공백(f27) / 4절 결론·불확실성 / 5절 후속 질문 / 6절 완료 조건 현황 / 8절 출처 / 9절 이력 |
| update | docs/ideas/nl-task-chatbot.md | 5 | 아이디어 페이지 5절(트랙 산출물): '스케줄링 결정의 분담' 소절 신설 — 분담 가설 f22(추정), 근거 f8·f9·f10·f12·f15·f16·f21·f1, 반례 f23, 동적 재스케줄링 f24, 설명 역할 f19. 처리 흐름 전체(q3-02)·되묻기(q3-03)·지시 변경(q3-04)은 미조사임을 명시 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | 2, 6 | 트랙 산출물 갱신: track.ontology_changes(일정 개념에 '일정 산출 방식' 속성)가 승인되면 2절 반영과 초안 버전 인상(f1·f2·f13·f14·f15·f21). 6절 '일정을 누가 계산하는가' 질문에 q3-01 답(f22) 연결, 목적 가중치 전달 인터페이스는 질문으로 유지 |
| update | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md | 6 | 트랙 nl-task-chatbot 단계 3 반영 제안 (f1, f2, f8, f9, f10, f12, f13, f22, f24): rmf_task 의 순서 계획·충전 삽입, LLM 직접 스케줄 생성의 실행 가능성 한계 벤치마크, 루프 밖 LLM 규칙 합성 구조. 27. AI·학습·적응과 모델 운영과 양쪽 연결 |
| update | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md | 6 | 트랙 nl-task-chatbot 단계 3 반영 제안 (f2, f3, f21, f25): TaskPlanner 탐욕·A* 선택과 비용 계산기, LLM 정식화+해법기 배정 분담, 분류 원문 질문과 목적함수 기반 전체 최적 비교 |
| update | docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md | 6, 8 | 트랙 nl-task-chatbot 단계 3 반영 제안 (f7, f8, f15, f16, f17, f19): LLM-Modulo(의견), 직접 풀이 한계 벤치마크, OptiMUS·LAPPI 의 정식화·인스턴스화 역할, 운영과학 LLM 서베이 세 경로, 스케줄 설명 생성. 적용 대상 13. 작업 배정 — MRTA·14. 작업 순서·스케줄링과 함께 연결 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 작업장 스케줄링 문제 | Job Shop Scheduling Problem (JSSP) | 여러 작업이 정해진 순서로 여러 기계를 거칠 때 기계별 작업 순서를 정해 전체 완료 시간 같은 목표를 최소화하는 대표적 조합 최적화 스케줄링 문제이다. |
| 자원 제약 프로젝트 스케줄링 문제 | Resource-Constrained Project Scheduling Problem (RCPSP) | 선후 관계가 있는 활동들을 한정된 자원 용량 안에서 시작 시각을 정해 배치하는 스케줄링 문제로, 실행 가능한 일정을 찾는 것 자체가 어려운 NP-난해 문제이다. |
| LLM-모듈로 프레임워크 | LLM-Modulo Framework | LLM 을 계획의 후보를 내는 생성기로 두고 외부 모델 기반 검증기·비평자가 후보를 검사해 되먹임하는 LLM–기호 시스템 결합 구조이다. |

## 열린 질문

새로 생긴 질문:

- 창고 이동로봇 플릿의 재배정·재스케줄링 주기에서 LLM 추론 지연이 허용되는 한계를 측정했거나, LLM 을 결정 루프 밖에 둔 운영 사례가 있는가? | 관련 영역: 14. 작업 순서·스케줄링, 27. AI·학습·적응과 모델 운영 | 근거: f13 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 25 · 교차 확인: 0
- 예산 사용량: 검색 25회 · 신규 출처 16건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 연구마다 단일 논문 또는 같은 저장소의 README·헤더
    - f6·f8~f14·f16~f20 수치와 방법은 저자 보고, 검색 요약 기준 원문 미열람
    - f11 Starjob 의 정확 해법기(OR-Tools 등) 비교 여부 미확인
    - f12 DynaSchedBench 수치(1.66%·0.65%)의 지표 정의 미확인
    - f18 PortAgent 성능 수치 미확인
    - f20 Saha 외의 해법기 대비 정량 비교 미확인
    - ref-675·ref-677·ref-678·ref-682·ref-683 저자 목록, ref-687 공저자 전체 미확인
    - f27 물류 플릿 비교 자료의 부재는 검색 범위 관찰이며 부재 확인 아님
    - rmf_task TaskPlanner 의 BinaryPriorityCostCalculator 비용 정의 세부 미확인
- 범위 경계 위반 의심:
    - f18: 컨테이너 터미널 차량 디스패칭은 분류 원문 9장의 업종별 조건·거점 간 운송과 가까울 수 있어, 방법론 사례(LLM 이 디스패칭 시스템을 구성)로만 쓰고 ROP 직접 범위처럼 서술하지 않도록 제안
    - f20: 건설 로봇 사례라 방법 사례로만 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. 원문을 연 출처: 신규 ref-679(OptiMUS README)·ref-377(rmf_task TaskPlanner.hpp)은 github_raw, 재사용 ref-404(rmf_task README)·ref-091(LLM+P README)는 github_raw, ref-031 은 입력 원문 텍스트(inbox). 나머지 신규 14건과 재사용 ref-376·ref-092·ref-166·ref-167·ref-181·ref-242 는 원문 미열람(신뢰도 상한 medium). 이번 실행에서는 모든 출처·finding 신뢰도를 medium 이하로 두었다. 검색 25회/40, 신규 출처 16건/20(ref-674~ref-689, 예약 구간 안), 재사용 9건. 질문 선택: target.json 지정 q3-01 1건. q3-01 은 오케스트레이션 도구 구조(사실)와 LLM 스케줄링 벤치마크·결합 연구(사실)로 답했으나, ROP 의 분담(f22·f24~f26)은 이 위키의 종합이고 근거가 물류 플릿이 아닌 조건이라 질문 종합 신뢰도를 low 로 두었다. 한국 자료: 한국어 검색 3회에서 LLM 과 최적화 엔진의 스케줄링 분담을 다룬 국내 연구·사례를 찾지 못했다. 교차 규칙: LLM 스케줄링·배정 finding 은 27. AI·학습·적응과 모델 운영과 적용 대상 13. 작업 배정 — MRTA·14. 작업 순서·스케줄링 양쪽에 반영 제안했다. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈: 시뮬레이션은 LLM 규칙 검증 도구(f14)로만 언급했고 두 영역을 섞지 않았다. 정정 요청 없음. 새 일반 열린 질문 1건(LLM 지연 한계). 후속 질문 3건. 온톨로지 변경 제안 1건(일정 개념). 백로그 참고: q3-09·q3-10, q5-05·q5-06 이 중복 등록되어 정리 필요.

## 트랙 블록

- 트랙: nl-task-chatbot · 단계: 3
- 답한 질문 id: q3-01

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 채팅 지시에서 LLM 이 뽑은 기한·우선순위·선호(목적 가중치)를 rmf_task 비용 계산기나 MILP 목적함수·제약으로 넘기는 인터페이스는 어떤 형식으로 두고, LAPPI 처럼 사용자가 결과를 보고 가중치를 고치는 반복을 어떻게 설계하는가? (q3-01 에서 파생) | 3 | f16 |
| — | RACE-Sched·Li·Li 처럼 LLM 이 루프 밖에서 만든 배정·스케줄 규칙을 시뮬레이션·샌드박스에서 검증한 뒤 운영 정책으로 반영할 때, 어떤 검증 기준을 통과해야 반영을 허용하는가? (q3-01 에서 파생) | 4 | f13 |
| — | ConstraintBench 처럼 해법기 최적해를 정답으로 두고 LLM 직접 스케줄의 실행 가능성·최적성 결합 비율을 재는 방식을 물류 창고 배정·스케줄링 시나리오로 옮기면, 제약 상호작용(충전·시간창·공용 자원)에 따라 결과가 어떻게 달라지는가? (q3-01 에서 파생) | 5 | f8 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 일정 (Schedule) | f1, f2, f13, f14, f15, f21 | 주요 속성에 '일정 산출 방식'을 더한다. 값 후보: 최적화·계획 해법(rmf_task 탐욕·A* f1·f2, 선형·정수계획·MILP·makespan 최소화 f21, MIP 해법기 f15) / LLM 이 만든 규칙·휴리스틱을 결정적 실행기가 적용(f13·f14). 'LLM 직접 생성' 값은 실행 가능성 한계 보고(f8~f10)가 있어 값 후보로만 둘지 검증 판단. 배정 개념의 '배정 산출 방식'과 같은 구조이며 기존 속성(작업 순서, 시작·종료 예정 시각, 갱신 이유)과 충돌하지 않는다. 계산 주체를 정하는 초안 6절 질문('일정을 누가 계산하는가')의 근거가 된다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 처리 흐름·핵심 구성 요소·다른 아이디어와의 연결이 아이디어 2. 자연어 업무 지시 챗봇 5절에 아직 실리지 않음(이번은 스케줄링 분담 소절만 제안, 처리 흐름 q3-02 미조사)
    - 업무 분해·배정 설계 초안의 단계 3 근거 갱신은 이번 온톨로지 변경 검증 승인 전
    - 실험 페이지에 사용자에게 제안하는 실험 계획 없음
    - 열린 질문 q3-02~q3-10
