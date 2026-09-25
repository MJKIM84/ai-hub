# 리서치 브리프 2026-09-25-00

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-00 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 13. 작업 배정 — MRTA |
| 대분류 | D. 계획·최적화 |

트랙 실행: 트랙 `nl-task-chatbot` · 단계 5 · 답한 질문 q5-03

## 갭(비어 있거나 약한 섹션)

- 단계 5 질문 q5-03 열림(target.json CLI 지정 질문)
- 완료 조건: 가설 판정표가 트랙 개요 '3. 가설과 판정 상태'에 실리지 않음(가설 1~3 모두 미판정)
- 완료 조건: 사용자에게 제안하는 실험 계획이 실험 페이지에 없음
- 단계 5 페이지 3절에 q5-03 소절 없음, 4절 결론에 가설 판정 근거 없음
- 아이디어 2. 자연어 업무 지시 챗봇 페이지 6절에 가설 판정 소절 없음
- 앞 단계 3·4 완료가 승인되지 않아 '단계 1~4의 결과'가 대부분 추정·신뢰도 low 문헌 종합임

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. q5-03 가설 1~3은 단계 1~4의 결과로 어떻게 판정되는가?
3. 가설 1(정해진 작업 모델로 먼저 구조화하면 LLM이 로봇 명령을 직접 만드는 방식보다 잘못된 배정이 줄어든다)을 지지·반박하는 구조화 중간 표현 대 직접 생성 비교 연구가 있는가? (단계 5 페이지 3절, 트랙 개요 3절 겨냥)
4. 가설 2(적합한 로봇 선택을 온톨로지 질의에 맡기면 배정 근거를 설명·재현할 수 있다)를 뒷받침하는 온톨로지 기반 배정의 재현성·설명 가능성 평가 자료가 있는가? (트랙 개요 3절 겨냥)
5. 가설 3(스케줄링은 최적화 엔진, LLM은 해석·확인·설명)을 지지·반박하는 LLM 배정기 대 MILP·LP 배정기 비교 결과가 있는가? (트랙 개요 3절, 13. 작업 배정 — MRTA 섹션 6 겨냥)
6. 가설 판정을 문헌 근거와 ROP 자체 실험 근거로 나눠 기록하려면 판정 기준·비교군·지표를 어떻게 두는가? (실험 페이지 계획 제안 겨냥)
7. 국내(한국) 연구에서 자연어 지시 로봇 배정의 구조화·최적화 분담을 실험으로 비교한 자료가 있는가? (한국 자료 우선 규칙)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | NRTrans 는 자연어 과제와 로봇 제어 프로그램 사이에 작은 로봇 스킬 언어(RSL)를 두고 컴파일러 검증과 오류 피드백 루프를 거치게 해, 25개 과제·5개 LLM 평가에서 ProgPrompt 기준선보다 평균 성공률을 53.6% 높였다고 저자들이 보고했다. | ref-748 | 아니오 | medium | 2025-08 | — | 원문 미열람 |
| f2 | [사실] | LiP-LLM 저자들은 LLM 기반 배정이 추적 한계로 어려움을 겪은 반면 선형계획 배정은 배정 실패가 거의 없었다고 보고했다. | ref-166 | 아니오 | medium | 2024-10 | — | 원문 미열람 |
| f3 | [사실] | Liu 외(KTH)의 Specifier–Designer–Inspector 구조에서 기호 검증기를 같은 방식으로 프롬프트한 LLM 비평자로 바꾸면 성공률이 98.1%에서 3.8%로 떨어졌다고 저자들이 보고했다. | ref-674 | 아니오 | medium | 2026-06 | — | 원문 미열람 |
| f4 | [사실] | ConstraintBench 저자들은 10개 운영과학 영역 200개 과제에서 가장 좋은 모델의 실행 가능 해 비율이 65.0%였고 실행 가능성과 최적성을 함께 만족한 비율은 어느 모델도 30.5%를 넘지 못했다고 보고했다. | ref-592 | 아니오 | medium | 2026-02 | — | 원문 미열람 |
| f5 | [사실] | SCHEDBench 저자들은 같은 스케줄링 문제를 의미가 같은 다른 문장 표현으로 주면 LLM 의 실행 가능 비율이 떨어지고 제약 위반이 달라진다고 보고했다. | ref-594 | 아니오 | medium | 2026-08 | — | 원문 미열람 |
| f6 | [사실] | RobotFleet 는 LLM 기반 배정기와 능력 제약 아래 최대 작업 부하를 최소화하는 MILP 배정기를 바꿔 끼울 수 있게 두며, 저자들은 MILP 배정기가 대체로 유휴 시간을 줄였고 모든 목표를 한 프롬프트로 계획하는 방식은 유휴 시간이 컸으나 의존 그래프(DAG) 구조를 넣으면 줄었다고 보고했다. | ref-749, ref-750 | 아니오 | medium | 2025-10 | — | — |
| f7 | [사실] | Electronics(2026-08-11) 논문은 로봇·작업·장소 의미 모델에 대한 실행 가능성 판정 결과를 배정기에 묶이지 않는 ReasonerOutput 으로 정형화하고, 4개 시나리오·3개 플릿 구성·4개 배정기 실험과 3개 규모별 200개 무작위 사례 절제 실험에서 이 출력이 공통 실행 가능성 제약으로 일관되게 작동했다고 보고했다. | ref-236 | 아니오 | medium | 2026-08-11 | — | 원문 미열람 |
| f8 | [사실] | Kluge-Wilkes 외는 이종 조립 자원의 능력을 기술하는 온톨로지(CAPILANO)와 능력 기반 배정 방법을 연결하고, 자동 배정이 시간이 덜 들고 재현 가능한 결과를 낸다고 보고했으며 온톨로지 일관성은 HermiT 추론기와 ROMEO 방법으로 확인했다. | ref-237 | 아니오 | medium | 2022 | — | 원문 미열람 |
| f9 | [사실] | CE-MRS 는 다중 로봇 해를 대조적으로 설명하며, 22명 참가 대면 사용자 연구에서 사용자가 명세 오류를 찾아 고치는 능력이 좋아졌다고 저자들이 보고했다. | ref-662 | 아니오 | medium | 2024-10 | — | 원문 미열람 |
| f10 | [사실] | CoMuRoS 는 작업 관리자 LLM 이 해석·배정·재계획을 맡는 구조로 22개 시나리오·54개 작업·약 20대 로봇 벤치마크에서 정답률 최대 0.91을 보고해, LLM 이 배정을 직접 맡는 방식도 실험실 조건에서 높은 정답률을 낸 사례다. | ref-677 | 아니오 | medium | 2025-11 | — | 원문 미열람 |
| f11 | [추정] | LLM 이 건설 로봇 작업을 직접 배정한 LTAA 연구는 전통 기법을 앞섰다는 요약과 동적 계획법이 더 높았다는 요약이 충돌해, 가설 2·3의 반례로 쓸 수 있는지 확정되지 않았다. | ref-168 | 아니오 | low | 2025-12 | — | 원문 미열람 |
| f12 | [의견] | Kambhampati 외는 LLM 이 스스로 계획을 세우지는 못하지만 외부 검증기와 결합한 LLM-모듈로 틀에서는 계획을 도울 수 있다고 주장한다. | ref-586 | 아니오 | medium | 2024-02 | — | 원문 미열람 |
| f13 | [추정] | 가설 1~3은 모두 두 방식의 비교를 주장하므로, 판정에는 같은 지시 집합·같은 가상 현장·같은 교란에서 비교군을 나란히 재는 통제 비교가 필요해 보인다: 가설 1은 작업 모델 구조화 뒤 배정 대 LLM 직접 명령 생성(오배정률·실행 가능 배정 비율), 가설 2는 온톨로지 질의 배정 대 LLM 판단 배정(같은 입력 반복 시 배정 일치율, 근거 추적 비율), 가설 3은 해법기 일정 대 LLM 일정(실행 가능 비율, 최적성 간격, 재스케줄 뒤 시작 시각 편차, 반복 시행 분산). | ref-748, ref-749, ref-592, ref-236, ref-746, ref-740 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | 원문 미열람 |
| f14 | [추정] | 현재 문헌 근거만으로 보면 세 가설 모두 방향은 지지되지만 근거가 가정·실험실·산업 셀·운영과학 일반 조건이고 물류 창고 조건 비교가 없으므로, 판정표에는 '문헌 근거 수준: 부분 지지'와 'ROP 실험 판정: 미판정'을 나눠 적는 편이 맞아 보인다. | ref-748, ref-166, ref-674, ref-592, ref-594, ref-749, ref-236, ref-237, ref-677 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f15 | [추정] | 가설 3의 '운영이 더 안정적'이라는 표현은 확인한 자료에서 직접 측정되지 않았고 관련 근거는 LLM 스케줄의 표현 민감성(SCHEDBench)과 반복 실행 변동(Atil 외)뿐이어서, 판정 전에 안정성을 일정 안정성·실행 가능 비율 분산 같은 지표로 정의해야 할 것으로 보인다. | ref-594, ref-746 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f16 | [추정] | 13. 작업 배정 — MRTA 의 분류 원문 질문(최근접 배정의 전체 유리성)은 가설 3의 판정 실험에 최근접 배정 기준선을 세 번째 비교군으로 넣으면 같은 실험에서 함께 잴 수 있어 보인다. | ref-749, ref-592 | 아니오 | low | 2026-09-25 | 피킹 / 수행 자원 | 원문 미열람 |

### 근거 발췌

- **f1**: RSL 프로그램이 컴파일러를 통과해야 제어 프로그램이 되고 오류 메시지를 LLM 에 되먹임; 25개 과제·5개 LLM, ProgPrompt 대비 성공률 평균 +53.6%, 2B 모델로 92%(저자 보고, 검색 요약 기준, 로봇 과제 조건)
- **f2**: LLM 이 기술 목록·의존 그래프를 만들고 배정은 선형계획으로 풂; LP 배정은 실패가 거의 없음(저자 보고, 실험 조건 미확인) (재인용: 2026-09-25-21)
- **f3**: 그룹 A–D 52개 명령 부분집합 조건의 절제 실험, 98.1% → 3.8%(저자 보고, 산업용 로봇 셀 조건) (재인용: 2026-09-25-71)
- **f4**: LLM 이 제약 최적화 문제를 직접 풀 때 실행 가능 65.0%, 실행 가능·최적(솔버 기준 0.1% 이내) 동시 만족 30.5% 이하(저자 보고, 운영과학 일반 조건) (재인용: 2026-09-25-66)
- **f5**: 자연어 조합 스케줄링에서 표현 바꿔 쓰기에 따른 제약 충실도 변화(저자 보고) (재인용: 2026-09-25-66)
- **f6**: README: 배정 방식 'LLM-based reasoning' 과 'MILP', 계획기 Monolithic Prompt·Big DAG·Per-Goal DAG(원문 열람). 유휴 시간 비교는 논문 검색 요약 기준, 저자 보고. README 와 논문은 같은 저자라 독립 교차 아님
- **f7**: 선언적 추론과 절차적 평가를 결합한 하이브리드 추론, allocator-independent ReasonerOutput; 4 시나리오·3 플릿 구성·4 배정기, 규모별 200개 무작위 사례(저자 보고, 검색 요약 기준)
- **f8**: 라인리스 모바일 조립 시스템 조건; 'automatic allocation requires less time and provides reproducible results'(검색 요약 기준, 저자 보고)
- **f9**: 수색·구조 영역, IEEE RA-L 9권 2024, 22명 사용자 연구(저자 보고) (재인용: 2026-09-25-74)
- **f10**: 실험실 이종 로봇 팀, correctness 최대 0.91(저자 보고); 결정적 배정기와 같은 조건 비교는 확인되지 않음 (재인용: 2026-09-25-71)
- **f11**: 열린 질문 oq-030 의 출처 충돌이 해소되지 않음(원문 미열람) (재인용: 2026-09-25-21)
- **f12**: 입장 논문(2024-02): 생성–검증 루프에서 결정적 검증기가 정확성을 보증하는 역할
- **f13**: 이 위키의 종합. 근거: 구조화 대 직접 생성 비교(NRTrans), 배정기 교체 설계(RobotFleet), 실행 가능성–최적성 분리(ConstraintBench), 배정기 독립 판정(ReasonerOutput), 결정적 설정에서도 LLM 정확도 최대 15% 변동(Atil 외), 모의 사용자 보정 오차(Lost in Simulation)
- **f14**: 가설 1: 구조화·검증기 쪽이 우세(f1·f3·f6). 가설 2: 재현성은 온톨로지 배정에서 보고(f7·f8), 설명 가능성은 온톨로지 기반 설명을 직접 잰 자료 미확인. 가설 3: 실행 가능성은 해법기 우세(f2·f4·f6), '운영 안정성'은 직접 측정 자료 없음. 반례 f10·f11
- **f15**: 안정성 정의는 출처에 없음. 단계 5 q5-01 의 일정 품질 지표(시작 시각 편차)와 q5-02 의 반복 층(pass^k)을 판정 지표로 쓰는 방향의 추론
- **f16**: 배정기를 바꿔 끼우는 구조(RobotFleet)와 해법기 기준값 비교(ConstraintBench)에서 도출한 설계 추론; 창고 실측 비교 부재는 oq-052

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-748 | arXiv 2508.19074 저자(미확인) | An LLM-powered Natural-to-Robotic Language Translation Framework with Correctness Guarantees | 2025-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2508.19074 | 예 |
| ref-749 | Gupta, R. 외(RobotFleet 저자, arXiv 2510.10379) | RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning | 2025-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2510.10379 | 예 |
| ref-750 | therohangupta (RobotFleet 공식 저장소) | robot-fleet — RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/therohangupta/robot-fleet | 아니오 |
| ref-166 | Obata, K., Aoki, T., Horii, T., Taniguchi, T., & Nagai, T. | LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning | 2024-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2410.21040 | 예 |
| ref-674 | Liu, Z., Fernandez-Ayala, V. N., Wang, T., Qin, Q., Wang, X. V., Dimarogonas, D. V., & Wang, L.(KTH) | Agentic Neuro-Symbolic Planning and Commissioning for Human-in-the-Loop Industrial Robotics with Digital Twins | 2026-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2606.08214 | 예 |
| ref-592 | ConstraintBench 저자(arXiv 2602.22465, 저자 미확인) | ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization | 2026-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2602.22465 | 예 |
| ref-594 | SCHEDBench 저자(arXiv 2608.00991, 저자 미확인) | SCHEDBench: A Benchmark for Evaluating LLM Constraint Faithfulness in Natural-Language Combinatorial Scheduling | 2026-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2608.00991 | 예 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 2026-08-11 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/electronics15163562 | 예 |
| ref-237 | Kluge-Wilkes, A. 외(RWTH Aachen WZL) | Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems | 2022 | 논문 | medium | 2026-09-25 | https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems | 예 |
| ref-662 | Schneider, E. 외(CE-MRS 저자) | CE-MRS: Contrastive Explanations for Multi-Robot Systems | 2024-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2410.08408 | 예 |
| ref-677 | CoMuRoS 저자(arXiv 2511.22354, Frontiers in Robotics and AI 게재) | LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning | 2025-11 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2511.22354 | 예 |
| ref-168 | Kaitha, S., & Yu, S. 외(arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 2025-12 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2512.02810 | 예 |
| ref-740 | Lost in Simulation 저자(arXiv 2601.17087, 게재처 미확인) | Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations | 2026-01 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2601.17087 | 예 |
| ref-746 | Atil, B. 외 | Non-Determinism of "Deterministic" LLM Settings | 2024-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2408.04667 | 예 |
| ref-586 | Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S., Saldyt, L., & Murthy, A. | LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks | 2024-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2402.01817 | 예 |

### 출처 요약

- **ref-748**: 원문 미열람. NRTrans: 로봇 스킬 언어(RSL)와 컴파일러·디버거로 LLM 생성 로봇 프로그램의 정확성을 보장하고 ProgPrompt 대비 성공률 향상을 보고.
- **ref-749**: 원문 미열람. LLM 계획기 3종과 LLM·MILP 배정기를 바꿔 끼우는 다중 로봇 작업 계획 프레임워크, 유휴 시간 비교 보고.
- **ref-750**: README 가 배정 방식(LLM 기반 추론, MILP)과 계획기(Monolithic Prompt, Big DAG, Per-Goal DAG)를 제시. 비교 결과는 README 에 없음.
- **ref-166**: 원문 미열람. LLM 이 의존 그래프를 만들고 선형계획으로 배정.
- **ref-674**: 원문 미열람. 결정적 검증기 구조와 LLM 비평자 대체 절제 실험.
- **ref-592**: 원문 미열람. LLM 직접 최적화의 실행 가능성·최적성 평가.
- **ref-594**: 원문 미열람. 자연어 스케줄링에서 LLM 의 제약 충실도와 표현 민감성 평가.
- **ref-236**: 원문 미열람. 배정기 독립 실행 가능성 판정(ReasonerOutput)과 여러 배정기 실험.
- **ref-237**: 원문 미열람. 능력 온톨로지(CAPILANO) 기반 자원 배정, 재현 가능한 자동 배정 보고.
- **ref-662**: 원문 미열람. 다중 로봇 해의 대조적 설명과 사용자 연구.
- **ref-677**: 원문 미열람. LLM 작업 관리자가 해석·배정·재계획을 맡는 구조.
- **ref-168**: 원문 미열람. LLM 배정과 전통 최적화 비교(요약 간 출처 충돌, oq-030).
- **ref-740**: 원문 미열람. LLM 모의 사용자의 체계적 보정 오차.
- **ref-746**: 원문 미열람. 결정적 설정 LLM 의 반복 실행 정확도 변동.
- **ref-586**: 원문 미열람. LLM 과 외부 검증기를 결합하는 LLM-모듈로 틀을 주장하는 입장 논문.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md | 2, 3, 4, 5, 6, 9 | q5-03 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16 (신뢰도 low) — 질문 목록 q5-03 상태, 3절 q5-03 소절(가설별 지지·반례 근거 f1~f12, 통제 비교 설계 f13, 문헌 근거 수준과 ROP 실험 판정의 분리 f14, 안정성 정의 공백 f15, 분류 원문 질문 결합 f16), 4절 결론·불확실성, 5절 후속 질문, 6절 완료 조건 현황, 9절 이력 갱신 |
| update | docs/tracks/nl-task-chatbot/index.md | 3 | 트랙 산출물 갱신(완료 조건 '가설 판정표'): 검증이 승인하면 가설 1~3 판정 칸에 '문헌 근거 수준: 부분 지지(f14), ROP 실험 판정: 미판정'과 근거 단계·실행 id 를 적는 안. 최종 판정은 검증 몫 |
| update | docs/tracks/nl-task-chatbot/experiments.md | 2 | 트랙 산출물(단계 5 stage_artifacts): 가설 판정 통제 비교 실험 계획 제안 근거 f13·f15·f16(비교군: 구조화 대 직접 생성, 온톨로지 질의 대 LLM 판단, 해법기 대 LLM 일정 대 최근접 기준선). 계획 문안은 스토리텔러 몫 |
| update | docs/ideas/nl-task-chatbot.md | 6 | 아이디어 페이지 6절: 가설 판정 소절(f13·f14, 근거 f1·f4·f6·f7·f8, 반례 f10·f11) |
| update | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md | 6 | 트랙 nl-task-chatbot 단계 5 반영 제안 (f2, f6, f7, f10, f16): LLM 배정기와 MILP·LP 배정기 비교 보고, 배정기 독립 실행 가능성 판정, 최근접 기준선을 넣은 비교 설계. 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽 연결 |
| update | docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md | 6 | 트랙 nl-task-chatbot 단계 5 반영 제안 (f1, f3, f12): LLM 출력을 구조화 언어·결정적 검증기로 거치게 하는 방식의 효과 보고, LLM-모듈로 틀. 적용 대상 영역 13. 작업 배정 — MRTA 와 함께 연결 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 로봇 스킬 언어 | Robot Skill Language (RSL) | 자연어 과제와 로봇 제어 프로그램 사이에 두는 작은 고수준 언어로, 컴파일러가 LLM 이 생성한 프로그램의 정확성을 검사한 뒤에만 제어 프로그램으로 변환한다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 9회 · 신규 출처 3건
- 미확인 항목:
    - f1 NRTrans 수치(+53.6%, 92%)와 저자 목록 원문 미확인
    - f6 RobotFleet 유휴 시간 비교 수치 미확인(논문 원문 미열람, README 에 결과 없음)
    - f7 ReasonerOutput 실험 세부 결과 수치 미확인
    - f8 Kluge-Wilkes 재현성 주장의 실험 조건 미확인
    - f14 가설 2의 '설명 가능성'을 온톨로지 배정에서 직접 잰 자료를 찾지 못함
    - f15 가설 3의 '운영 안정성'을 직접 잰 자료를 찾지 못함
    - 물류 창고 조건에서 세 가설의 비교를 실측한 자료를 찾지 못함(부재의 확인 아님)
    - 국내 연구: 한국어 검색 2회에서 해당 비교 연구를 찾지 못함
- 범위 경계 위반 의심:
    - 없음
- 한계: run_id 주의: 실행 컨텍스트의 run_id 는 2026-09-25-100 이나 스키마 패턴(끝 두 자리)이 이를 거부해 2026-09-25-00 으로 적었다. 퍼블리셔가 실제 run_id 2026-09-25-100 으로 대응시켜야 한다. web_fetch_available: false · fetch_mode mirror_only. 신규 출처 3건(ref-748~ref-750) 가운데 RobotFleet README(ref-750)만 raw.githubusercontent.com 으로 원문을 열었고, 논문은 모두 검색 요약 범위만 사용해 신뢰도 상한 medium. 재사용 출처 12건은 이번 실행에서 다시 열지 않음. 교차 확인 0건(RobotFleet 논문·README 는 같은 저자). 검색 9회/40, 신규 출처 3건/20. 질문 선택: target.json CLI 지정 q5-03. q5-03 은 '판정 방법'과 '현재 문헌 근거 수준'으로 답했으며, 가설의 최종 판정은 ROP 자체 실험 근거가 없어 내지 않았다(판정은 검증 몫). 앞 단계 3·4 완료가 승인되지 않은 상태에서 지정 질문으로 단계 5를 다뤘다. 온톨로지 변경 없음: 가설 판정 방법과 판정 근거는 작업 모델의 개념·관계가 아니라 검증 방법이므로 업무 분해·배정 설계 초안 v0.8 유지. 후속 질문 3건. 교차 규칙: LLM 배정 관련 finding 은 13. 작업 배정 — MRTA 와 27. AI·학습·적응과 모델 운영 양쪽에 반영 제안. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다.

## 트랙 블록

- 트랙: nl-task-chatbot · 단계: 5
- 답한 질문 id: q5-03

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 가설 1 판정 실험의 비교군 'LLM 이 로봇 명령을 직접 만드는 방식'을 어느 인터페이스 수준(VDA 5050 주문, Open-RMF 작업 요청, 로봇 도구 호출)으로 정의하고, 두 방식의 오배정을 같은 기준으로 어떻게 판정하는가? (q5-03 에서 파생) | 5 | f13 |
| — | 가설 2의 '배정 근거 설명 가능성'을 배정 근거가 온톨로지의 능력·제약으로 추적되는 비율이나 사람 평가자의 이해도 같은 측정 지표로 어떻게 정의하고, 재현성은 같은 입력 반복 시 배정 일치율로 재도 되는가? (q5-03 에서 파생) | 5 | f14 |
| — | 가설 3의 '운영이 더 안정적'을 일정 안정성(재스케줄 뒤 시작 시각 편차), 실행 가능 비율의 반복 시행 분산, 표현 바꿔 쓰기에 대한 민감도 가운데 무엇으로 정의해 판정하는가? (q5-03 에서 파생) (관련: q5-15) | 5 | f15 |

### 온톨로지 초안 변경 제안

- 없음

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 가설 판정표가 트랙 개요 3절에 아직 실리지 않음(판정안은 검증 승인 전, ROP 실험 근거 없음)
    - 사용자에게 제안하는 실험 계획이 실험 페이지에 아직 없음
    - q5-04, q5-05, q5-07~q5-15 열림
    - 앞 단계 3·4 완료 미승인
