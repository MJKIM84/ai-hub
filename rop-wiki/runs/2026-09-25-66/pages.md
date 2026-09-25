# 스토리텔러 산출 2026-09-25-66

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md | draft | q3-01 답함(3절 #q3-01 신설), 2절에 q3-05~q3-11 추가, 후속 질문 2건, 완료 조건(초안 갱신만 충족), 상태 줄 갱신. 2차 수정: 6절 초안 갱신 행 충족으로 정정, 전환 줄 q3-02~q3-11, 시나리오 예외·성과 칸에 ConstraintBench 조건 병기 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | 초안 v0.5 → v0.6: 일정(Schedule) 개념에 속성 '일정 산출 방식' 추가·초안 → 확정(f1·f2·f13·f14·f15·f21), 6절 '일정을 누가 계산하는가'에 q3-01 답 연결(해결로 닫지 않음), 값 후보 'LLM 직접 생성'을 6절 질문으로 추가(2차 수정 대상 아님, 변경 없음) |
| update | docs/ideas/nl-task-chatbot.md | draft | 5절 구현 가설에 '스케줄링 결정의 분담' 소절 신설(q3-01, 실행 2026-09-25-66). 2차 수정: 새 각주 정의 12개를 5절 끝에 직접 두고 ref-681 기관을 Kuroki 외로, ref-684 소속을 '소속 미확인'으로 고침 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 3 | q3-01 답함(스케줄링은 결정적 해법, LLM 은 인스턴스화·설명 분담 가설, 신뢰도 low), 업무 분해·배정 설계 초안 v0.5 → v0.6(일정 산출 방식), 아이디어 2 5절에 분담 소절, 후속 질문 2건 | run 2026-09-25-66
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 3. 구현 가설 설계: q3-01 답함 — 스케줄링 결정은 결정적 최적화·계획 해법, LLM 은 문제 인스턴스화와 결과 설명을 맡는 분담 가설(신뢰도 low), 업무 분해·배정 설계 초안 v0.6
- 대분류 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 자연어 업무 지시 챗봇 트랙 단계 3에서 rmf_task 작업 계획기와 LLM 직접 스케줄 생성의 한계를 조사하고 13. 작업 배정 — MRTA·14. 작업 순서·스케줄링 반영 제안
- 세부영역 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 트랙 자연어 업무 지시 챗봇 단계 3(q3-01)에서 TaskPlanner 탐욕·A* 선택, LLM 정식화+해법기 배정 분담, 분류 원문 질문과의 연결을 6. 대표 접근법과 기술 반영 제안으로 냄

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 작업장 스케줄링 문제 | Job Shop Scheduling Problem (JSSP) | 여러 작업이 정해진 순서로 여러 기계를 거칠 때 기계별 작업 순서를 정해 전체 완료 시간 같은 목표를 최소화하는 대표적 조합 최적화 스케줄링 문제이다. | 14, 27 | ref-678 |
| new | 자원 제약 프로젝트 스케줄링 문제 | Resource-Constrained Project Scheduling Problem (RCPSP) | 선후 관계가 있는 활동들을 한정된 자원 용량 안에서 시작 시각을 정해 배치하는 스케줄링 문제로, 실행 가능한 일정을 찾는 것 자체가 어려운 NP-난해 문제이다. | 14, 27 | ref-676 |
| new | LLM-모듈로 프레임워크 | LLM-Modulo Framework | LLM 을 계획의 후보를 내는 생성기로 두고 외부 모델 기반 검증기·비평자가 후보를 검사해 되먹임하는 LLM–기호 시스템 결합 구조이다. | 27, 14 | ref-674 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-674 | Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S., Saldyt, L., & Murthy, A. | LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks | 논문 | medium | https://arxiv.org/abs/2402.01817 |
| ref-675 | ConstraintBench 저자(arXiv 2602.22465, 저자 미확인) | ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization | 논문 | medium | https://arxiv.org/abs/2602.22465 |
| ref-676 | Jain, R. 외(R-ConstraintBench 저자) | R-ConstraintBench: Evaluating LLMs on NP-Complete Scheduling | 논문 | medium | https://arxiv.org/abs/2508.15204 |
| ref-677 | SCHEDBench 저자(arXiv 2608.00991, 저자 미확인) | SCHEDBench: A Benchmark for Evaluating LLM Constraint Faithfulness in Natural-Language Combinatorial Scheduling | 논문 | medium | https://arxiv.org/abs/2608.00991 |
| ref-678 | Starjob 저자(arXiv 2503.01877, 저자 미확인) | Starjob: Dataset for LLM-Driven Job Shop Scheduling | 논문 | medium | https://arxiv.org/abs/2503.01877 |
| ref-679 | teshnizi (OptiMUS 공식 저장소) | OptiMUS — Optimization Modeling Using mip Solvers and large language models (GitHub README) | 오픈소스 문서 | medium | https://github.com/teshnizi/OptiMUS |
| ref-680 | AhmadiTeshnizi, A. 외(OptiMUS 저자) | OptiMUS-0.3: Using Large Language Models to Model and Solve Optimization Problems at Scale | 논문 | medium | https://arxiv.org/abs/2407.19633 |
| ref-681 | Kuroki, S., Nakagawa, M., Yoshida, S., Koyama, Y., & Kozuno, T.(OMRON SINIC X 등, IEEE Access 2026) | LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation | 논문 | medium | https://arxiv.org/abs/2512.14138 |
| ref-682 | DynaSchedBench 저자(arXiv 2605.27566, 저자 미확인) | DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents | 논문 | medium | https://arxiv.org/abs/2605.27566 |
| ref-683 | RACE-Sched 저자(arXiv 2605.29262, 저자 미확인) | Harmonizing Real-Time Constraints and Long-Horizon Reasoning: An Asynchronous Agentic Framework for Dynamic Scheduling | 논문 | medium | https://arxiv.org/abs/2605.29262 |
| ref-684 | Li, J., & Li, C.(소속 미확인) | LLM-Guided Heuristic Design from Simulation Traces: A Case Study in Dynamic Production and AGV Scheduling | 논문 | medium | https://arxiv.org/abs/2608.09343 |
| ref-685 | Hu, J., Li, J., Lin, W., Jia, P., Ji, Y., & Lai, J. | PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals | 논문 | medium | https://arxiv.org/abs/2512.14417 |
| ref-686 | Wang, Y., & Li, K. | Large Language Models in Operations Research: Methods, Applications, and Challenges | 논문 | medium | https://arxiv.org/abs/2509.18180 |
| ref-687 | Powell, C. 외(University of Strathclyde) | Generating textual explanations for scheduling systems leveraging the reasoning capabilities of large language models | 논문 | medium | https://link.springer.com/article/10.1007/s10844-025-00940-w |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp |
| ref-689 | Saha, S., Das, S., Duan, H., & Liu, X.-Y. | Hybrid LLM-based Intelligent Framework for Robot Task Scheduling | 논문 | medium | https://arxiv.org/abs/2605.15486 |
| ref-404 | Open Robotics (open-rmf) | rmf_task — README | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_task |
| ref-376 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/task.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-091 | Cranial-XIX (LLM+P 저자) | llm-pddl — LLM+P: Empowering Large Language Models with Optimal Planning Proficiency (GitHub README) | 오픈소스 문서 | medium | https://github.com/Cranial-XIX/llm-pddl |
| ref-092 | Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P. | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 논문 | medium | https://arxiv.org/abs/2304.11477 |
| ref-166 | Obata, K., Aoki, T., Horii, T., Taniguchi, T., & Nagai, T. | LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning | 논문 | medium | https://arxiv.org/abs/2410.21040 |
| ref-167 | Peng, M., Chen, Z., Yang, J., Huang, J., Shi, Z., Liu, Q., Li, X., & Gao, L. | Automatic MILP Model Construction for Multi-Robot Task Allocation and Scheduling Based on Large Language Models | 논문 | medium | https://arxiv.org/abs/2503.13813 |
| ref-181 | Shi, G., Wu, Y., Kumar, V., & Sukhatme, G. S. | PIP-LLM: Integrating PDDL-Integer Programming with LLMs for Coordinating Multi-Robot Teams Using Natural Language | 논문 | medium | https://arxiv.org/abs/2510.22784 |
| ref-242 | Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D.(JHU APL·JHU·DEVCOM ARL) | FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams | 논문 | medium | https://arxiv.org/abs/2510.07417 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 창고 이동로봇 플릿의 재배정·재스케줄링 주기에서 LLM 추론 지연이 허용되는 한계를 측정했거나, LLM 을 결정 루프 밖에 둔 운영 사례가 있는가? | 14, 27 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 시작 조건 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-01 | 단계 3. 구현 가설 설계 |
| 출하 | 작업 대상 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-01 | 단계 3. 구현 가설 설계 |
| 출하 | 수행 자원 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-01 | 단계 3. 구현 가설 설계 |
| 출하 | 제약 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-01 | 단계 3. 구현 가설 설계 |
| 출하 | 예외·성과 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-01 | 단계 3. 구현 가설 설계 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 단계 3 페이지 3절(q3-01): ConstraintBench(ref-675) 원문에서 영역별 실행 가능 비율(검색 요약 간 0.8~85.0% 대 0.8~83.3% 불일치)과 해법 최적값 대비 비율(89~96%)을 확인할 필요가 있다 — 이번 페이지에서는 수치를 쓰지 않았다.
- 단계 3 페이지 3절: R-ConstraintBench(ref-676)의 결론(복합 제약에서 실행 가능성 급락, 병목은 제약 상호작용)과 LLM+P 논문(ref-092)의 결과 구절을 원문으로 재확인해야 [사실]로 쓸 수 있다.
- 단계 3 페이지 3절·4절: SCHEDBench 의 평가 모델 수와 가장 민감한 변형 유형, DynaSchedBench 수치(1.66%·0.65%)의 지표 정의, Starjob 의 정확 해법기(OR-Tools 등) 비교 여부가 미확인이다.
- 단계 3 페이지 3절: rmf_task 의 재배정 기능 문서와 BinaryPriorityCostCalculator 의 비용 정의를 공식 저장소에서 확인할 필요가 있다(동적 재스케줄링 분담 근거).
- 아이디어 2 5절 완료 조건: 처리 흐름 전체와 단계별 입력·출력(q3-02)을 조사해야 단계 3 완료 조건을 채울 수 있다.
- 실험 페이지(단계 3 완료 조건): 사용자에게 제안할 실험 계획(예: 창고 시나리오에서 LLM 인스턴스화+해법기와 LLM 직접 스케줄 비교)의 근거가 되는 finding 이 브리프에 없어 이번에 계획을 쓰지 않았다(q5-05 와 연계).

## 이행한 수정 지시

- f2 '(예: 충전)' 제거 — 단계 3 페이지의 TaskPlanner.hpp(ref-377) 문장에서 충전 예시를 빼고 '마무리 작업'으로만 썼으며, 충전 작업 자동 삽입은 README(ref-404) 각주만 단 별도 문장으로 옮겼다(아이디어 페이지·시나리오도 같음).
- f4 분리 — 관제 최소 기능·충전 주문의 운반 주문 중단·교통 관리 로직 범위 제외는 [사실][^ref-031], '배정·일정 결정 로직은 관제 구현에 맡겨진 것으로 보인다'는 별도 [추정][^ref-031] 문장으로 나누고, 13. 작업 배정 — MRTA 페이지의 '배정 알고리즘을 규정하지 않는다'와 어긋나지 않게 썼다.
- f6 강등 — LLM+P 결과 문장을 [추정]으로 쓰고 'LLM+P 논문 저자 보고, 원문 미열람'을 병기했다.
- f8 수치 정리 — 영역별 비율 수치를 쓰지 않고 '편차가 크다고 보고되었으나 수치는 검색 요약마다 달라 미확인'으로 썼으며, 89~96% 는 삭제하고 30.5% 에 '솔버 기준 0.1% 이내', '6개 모델·200개 과제, 저자 보고값'을 병기했다.
- f9 강등 — R-ConstraintBench 문장을 [추정]으로 쓰고 '저자 보고, 원문 미열람·검증 미재확인'을 병기했다.
- f10 — '13개 LLM'과 '제약 순서 바꾸기에 가장 민감'을 본문에서 빼고 '평가한 모델 수와 가장 민감한 변형 유형은 미확인'으로 표시했다.
- f12 — '참된 최적화기보다 정교한 휴리스틱처럼 동작' 구절을 뺐고, 1.66% 대 0.65%·약 3배 토큰 비용은 저자 보고값으로 두되 '지표 정의 미확인'을 병기했다.
- f13 — '샌드박스 시험·원자적 갱신 배포'를 빼고 'LLM 이 규칙을 합성·검증·진화시킨다'로 줄였으며 '규칙을 운영에 반영하는 방식의 세부는 미확인'을 적었다.
- f14 — 본문과 각주·참고문헌 항목의 저자 소속을 '소속 미확인'으로 바꿨다.
- f15 — README(ref-679)가 확인하는 v1~v3 구성과 MIP·LP 해법기 사용을 [사실][^ref-679] 문장으로, Gurobi 파이썬 API 코드와 오류 검사 모듈은 ref-680(원문 미열람) 요약 기준임을 밝힌 별도 문장으로 구분했다.
- f16·ref-681 — 본문 표기를 'Kuroki 외, IEEE Access 2026'으로 쓰고 각주 정의와 reference_updates 의 기관을 'Kuroki, S., Nakagawa, M., Yoshida, S., Koyama, Y., & Kozuno, T.(OMRON SINIC X 등, IEEE Access 2026)'로 고쳤다.
- f18 — 문장 앞에 '연계 대상:'을 붙이고 방법 사례로만 서술했으며 디버거의 검사 방식 세부를 미확인으로 표시했다.
- f19 — '63권 1287–1337쪽'을 본문에서 뺐고 참고문헌 요약에서도 권·쪽수를 뺐다.
- f20 — '건설 로봇 사례로' 시작하고 분류 원문 9장의 업종별 조건 연계 대상이어서 방법 사례로만 다룬다고 밝혔다.
- f24 — 'rmf_task 의 재배정'을 쓰지 않고 [추정] 문장 안에서 '충전 삽입 등'으로만 쓰며 '재배정 기능은 문서에서 확인하지 않았다'를 덧붙였다.
- 인용 — ref-377·ref-404 는 페이지에서 직접 인용 없이 모두 재서술했다.
- 각주 — 원문 미열람 19개 출처의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-679·ref-377·ref-404·ref-091·ref-031·ref-376 은 원문 열람 출처(source_unopened: false, 각주 표시 없음)로 두었다.
- 온톨로지 — 업무 분해·배정 설계 초안의 일정(Schedule) 개념에 속성 '일정 산출 방식'(최적화·계획 해법 / LLM 이 만든 규칙·휴리스틱을 결정적 실행기가 적용)을 더하고 상태를 초안 → 확정, 초안 버전을 0.5 → 0.6(프런트매터·H1·ontology_draft_version)으로 올렸으며, 'LLM 직접 생성' 값은 넣지 않고 6절 질문(관련 f11·f20·f23)으로 두었다.
- 초안 6절 — '일정을 누가 계산하는가' 질문에 q3-01 답([추정], 신뢰도 low)과 단계 3 페이지 링크를 연결하되 물류 플릿 근거가 없어 해결로 닫지 않는다고 적었다.
- 새 질문 3(ConstraintBench 방식 물류 측정)은 q5-05 중복이므로 backlog_updates 에 넣지 않고 단계 3 페이지 5절에 제외 사유만 적었다.
- q3-01 — 백로그와 단계 페이지 2절에서 답함(답한 실행 2026-09-25-66, 답 위치 #q3-01, 3절 '### q3-01 … {#q3-01}')으로 처리했고, 6절 완료 조건 세 항목을 모두 '미충족'으로, 표 아래 줄을 '다음 단계로 전환: 아니오(아이디어 2 5절 처리 흐름·구성 요소 미작성, 실험 계획 없음, 열린 질문 q3-02~q3-10)'로 썼다.
- 트랙 개요 — 현재 단계(단계 1. 선행 연구·제품 사례 조사)를 바꾸지 않았고, 마지막 트랙 실행이 이미 2026-09-25 로 되어 있어 개요 페이지는 내용 변경이 없으므로 pages 에 넣지 않았다(overview_progress 에 CLI 지정 단계 3 실행임을 적음).
- 2차: 아이디어 페이지 ref-681 각주 — 5절 패치 끝에 각주 정의를 직접 두고 기관을 'Kuroki, S., Nakagawa, M., Yoshida, S., Koyama, Y., & Kozuno, T.(OMRON SINIC X 등, IEEE Access 2026)'로 고쳤다.
- 2차: 아이디어 페이지 ref-684 각주 — 같은 위치의 각주 정의에서 '(칭화대학교 산업공학과)'를 '(소속 미확인)'으로 고쳤다(나머지 새 각주 10개도 참고문헌 항목과 같은 값으로 5절 끝에 함께 두었다).
- 2차: 단계 3 페이지 6절 두 번째 행 — 충족 여부 '충족', 근거 '이번 실행에서 일정 개념에 속성 일정 산출 방식을 더해 v0.6 으로 갱신(f1·f2·f13·f14·f15·f21)', 검증 판정 '충족'으로 고쳤고 나머지 두 행과 상태 줄의 '완료 조건: 미충족'은 그대로 두었다.
- 2차: 단계 3 페이지 6절 아래 줄 — '다음 단계로 전환: 아니오(아이디어 2 5절 처리 흐름·구성 요소 미작성, 실험 계획 없음, 열린 질문 q3-02~q3-11)'로 고쳤다.
- 2차: 단계 3 페이지 3절 시나리오 표 예외·성과 칸 — ConstraintBench 문장에 '(운영과학 일반 제약 최적화 문제, 솔버 기준 0.1% 이내 조건의 저자 보고값)'을 덧붙였다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md
- 온톨로지 초안 버전: 0.6
- 트랙 로그 항목: 답한 질문: q3-01(단계 3. 구현 가설 설계 3절 #q3-01, 근거 f1~f27, 신뢰도 low — 스케줄링 결정은 결정적 최적화·계획 해법, LLM 은 문제 인스턴스화·결과 설명을 맡는 분담 가설) / 새 질문: q3-11(f16), q4-08(f13); ConstraintBench 방식 물류 측정 질문은 q5-05(및 q3-05)와 중복으로 제외 / 온톨로지 변경: v0.5 → v0.6: 개념 '일정 (Schedule)'에 속성 '일정 산출 방식'(최적화·계획 해법 / LLM 이 만든 규칙·휴리스틱을 결정적 실행기가 적용) 추가, 초안 → 확정(f1·f2·f13·f14·f15·f21, 근거 실행 2026-09-25-66); 값 후보 'LLM 직접 생성' 거부 → 6절 질문(관련 f11·f20·f23) / 완료 조건 평가: 미충족(부족: 아이디어 2 5절 처리 흐름·핵심 구성 요소·다른 아이디어와의 연결, 실험 페이지 실험 계획; 초안 v0.6 갱신 조건은 충족; 열린 질문 q3-02~q3-11) / 세부영역 반영 제안: 14. 작업 순서·스케줄링, 13. 작업 배정 — MRTA, 27. AI·학습·적응과 모델 운영(2건), 20. 예외 복구·재계획·업무 연속성 — 5건 / 다음 실행 제안: q3-02, q3-03, q3-04. 참고: 이번 실행은 CLI 지정 단계 3 실행이며 트랙 개요의 현재 단계는 단계 1 유지. 백로그 중복 q3-09/q3-10, q5-05/q5-06 정리 필요.
- 개요 진행 현황: 단계 3 진행 중 — 열린 질문 10, 답함 1, 완료 조건 미충족(초안 갱신 조건만 충족) (CLI 지정 단계 3 실행, 트랙 개요의 현재 단계 표시는 단계 1 유지)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q3-01 | 답함 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-01 | — | — | — |
| q3-11 | 열림 | — | 채팅 지시에서 LLM 이 뽑은 기한·우선순위·선호(목적 가중치)를 rmf_task 비용 계산기나 MILP 목적함수·제약으로 넘기는 인터페이스는 어떤 형식으로 두고, LAPPI 처럼 사용자가 결과를 보고 가중치를 고치는 반복을 어떻게 설계하는가? (q3-01 에서 파생) | 3 | f16 |
| q4-08 | 열림 | — | RACE-Sched·Li·Li 처럼 LLM 이 루프 밖에서 만든 배정·스케줄 규칙을 시뮬레이션·샌드박스에서 검증한 뒤 운영 정책으로 반영할 때, 어떤 검증 기준을 통과해야 반영을 허용하는가? (q3-01 에서 파생) | 4 | f13 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 14 | 6. 대표 접근법과 기술 | rmf_task 작업 계획기의 순서 계획(요청 시작 시각 준수, 탐욕·A* 선택)과 README 기준 충전 작업 자동 삽입(f1·f2), LLM 직접 스케줄 생성의 실행 가능성 한계 벤치마크(ConstraintBench 65.0%·30.5% 조건 병기 f8, SCHEDBench 표현 민감성 f10, DynaSchedBench f12, R-ConstraintBench [추정] f9), LLM 을 결정 루프 밖에 두고 규칙을 합성하는 RACE-Sched(f13)와 분담 가설(f22·f24 [추정]). 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽에 연결한다. |
| 13 | 6. 대표 접근법과 기술 | TaskPlanner 의 탐욕(최적성 미보장)·A*(최적성 보장) 선택과 기본 비용 계산기 BinaryPriorityCostCalculator(f2), LLM 정식화+선형·정수계획·MILP·makespan 최소화 해법 배정 분담(f21), 분류 원문 질문 '가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가?'와 목적함수 기반 해법의 비교 가능성([추정] f25, 30.5% 조건 병기). |
| 27 | 6. 대표 접근법과 기술 | LLM-모듈로 틀(Kambhampati 외, [의견] f7), LLM 을 해법기가 아니라 정식화·인스턴스화 인터페이스로 쓰는 OptiMUS(f15)·LAPPI(f16, Kuroki 외), 스케줄링 결과의 설명문을 LLM 으로 생성하는 연구(f19). 적용 대상 13. 작업 배정 — MRTA·14. 작업 순서·스케줄링과 함께 연결한다. |
| 27 | 8. 대표 연구와 자료 | 운영과학 LLM 적용 서베이(Wang·Li, 자동 모델링·보조 최적화·직접 풀이의 세 경로, f17)와 LLM 직접 풀이 벤치마크 ConstraintBench(f8)·SCHEDBench(f10)를 대표 자료 후보로 제안한다(원문 미열람). |
| 20 | 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) | 동적 재스케줄링에서 LLM 추론 지연 때문에 LLM 을 결정 루프 밖에 두고 규칙·정책을 만들어 시뮬레이션·검증 뒤 반영하는 구조(RACE-Sched f13, Li·Li f14, 종합 f24 [추정])가 14. 작업 순서·스케줄링·27. AI·학습·적응과 모델 운영과 이어진다. 시뮬레이션은 정책 검증 도구로만 다룬다. |
