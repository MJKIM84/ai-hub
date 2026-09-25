---
title: "실험"
type: track
subtype: experiments
track: nl-task-chatbot
status: draft
created: 2026-09-25
updated: 2026-09-25
version: 2
sources: [ref-748, ref-674, ref-749, ref-592, ref-594, ref-236, ref-237, ref-746, ref-740]
---

[홈](../../index.md) › 중점 연구 트랙 › [자연어 업무 지시 챗봇](index.md) › 실험

# 실험

이 페이지는 중점 연구 트랙 [자연어 업무 지시 챗봇](index.md)에서 스토리텔러 에이전트가 제안한 실험 계획과, 사용자가 직접 수행해 저장소의 `experiments/` 폴더에 넣은 실험 결과의 요약을 모은다. 선택 페이지이며, 실험이 없어도 트랙은 진행된다.

## 실험 규칙

- 실험은 사용자가 직접 수행한다. 에이전트는 계획을 제안하고, 사용자가 넣은 결과를 읽어 반영한다.
- 이 트랙에서 계획은 단계 3·5에서 제안한다(트랙 정의의 `stage_artifacts`). [가정]
- 결과는 `experiments/<날짜>-<이름>/`에 넣고 `README.md` 머리에 트랙(`nl-task-chatbot`), 단계, 답하려는 질문 id를 적는다. 다음 트랙 실행에서 `[사용자 실험]` 태그로 반영되며, `[사실]`로 올라가려면 내용 검증 에이전트의 판정이 필요하다.
- 계획 형식(계획 번호 `E<단계>-<두 자리>`, 목적, 방법, 측정 지표와 조건, 필요한 자료, 제안한 실행 id, 상태)과 결과 입력 형식은 첫 트랙의 [실험](../manual-capability-ontology/experiments.md) 페이지와 [기여·정정 방법](../../about/how-to-contribute.md)을 따른다.

## 제안된 실험 계획

아래 세 계획은 실행 2026-09-25-100 에서 [단계 5 의 q5-03 답](stage-5-verification-and-hypotheses.md#q5-03)을 근거로 제안한 가설 판정용 통제 비교다. 세 가설 모두 두 방식의 비교를 주장하므로, 같은 지시 집합·같은 가상 현장·같은 교란에서 비교군을 나란히 재는 설계가 필요해 보인다. [추정][^ref-748][^ref-749][^ref-592][^ref-236][^ref-746][^ref-740] 이 설계는 이 위키의 추론이며, 목표 수치와 표본 규모는 근거가 없어 정하지 않았다. 가상 현장·가상 로봇 구성은 [q5-02 답](stage-5-verification-and-hypotheses.md#q5-02)의 네 층 시험을 따른다. 결과는 `experiments/<날짜>-<이름>/`에 넣는다.

### E5-01 가설 1 판정: 작업 모델 구조화 뒤 배정 대 LLM 직접 명령 생성

- 목적: 가설 1(작업 모델로 먼저 구조화하면 LLM 이 로봇 명령을 직접 만드는 방식보다 잘못된 배정이 줄어든다)의 ROP 실험 판정 근거를 얻는다.
- 방법: 같은 물류 지시 집합을 (가) [업무 분해·배정 설계 초안](task-model-draft.md)의 작업 모델로 구조화한 뒤 결정적 검사와 배정을 거치는 방식과 (나) LLM 이 로봇 명령을 직접 만드는 방식에 똑같이 넣는다. 구조화 중간 표현과 컴파일러 검증을 둔 쪽이 LLM 직접 생성 기준선보다 성공률이 높았다는 보고(로봇 프로그램 생성 조건)와 결정적 검증기를 LLM 비평자로 바꾸면 성공률이 크게 떨어졌다는 보고(산업용 로봇 셀 조건)를 물류 배정으로 옮긴 설계다. [추정][^ref-748][^ref-674] 비교군 (나)를 어느 인터페이스 수준으로 둘지는 [질문 백로그](question-backlog.md)의 q5-16 에서 정한다.
- 측정 지표와 조건: 오배정률, 실행 가능 배정 비율, 같은 시나리오 반복 시 시행 분포(pass^k). [추정][^ref-748][^ref-746] 같은 지시·같은 교란·같은 초기 상태.
- 필요한 자료: 물류 지시–정답 쌍(q5-04), 창고 레이아웃과 시나리오 집합(q5-13), 가상 로봇 플릿.
- 제안한 실행 id: 2026-09-25-100
- 상태: 제안

### E5-02 가설 2 판정: 온톨로지 질의 배정 대 LLM 판단 배정

- 목적: 가설 2(온톨로지 질의에 맡기면 배정 근거를 설명·재현할 수 있다)의 ROP 실험 판정 근거를 얻는다. 온톨로지 질의 배정과 LLM 판단 배정을 같은 조건에서 비교한 문헌 근거는 찾지 못했다(재현성 보고는 수작업 배정 대비). [추정][^ref-237][^ref-236]
- 방법: 같은 작업 요구 집합을 (가) 로봇 능력·제약 대조로 실행 가능성을 판정한 뒤 배정하는 방식과 (나) LLM 이 로봇을 판단해 고르는 방식에 여러 번 반복해 넣는다.
- 측정 지표와 조건: 같은 입력 반복 시 배정 일치율, 배정 근거가 능력·제약으로 추적되는 비율. [추정][^ref-236][^ref-746] 설명 가능성의 측정 정의는 q5-17 에서 정한다.
- 필요한 자료: 로봇 능력·제약 정보(아이디어 1 의 로봇 기능 온톨로지 또는 대리 원천), 작업 요구 집합.
- 제안한 실행 id: 2026-09-25-100
- 상태: 제안

### E5-03 가설 3 판정과 분류 원문 질문: 해법기 일정 대 LLM 일정 대 최근접 기준선

- 목적: 가설 3(스케줄링은 최적화 엔진, LLM 은 해석·확인·설명을 맡는 분담이 운영을 더 안정적으로 만든다)의 ROP 실험 판정 근거를 얻고, 13. 작업 배정 — MRTA 의 SCM 관점 질문(가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가)을 같은 실험에서 함께 잰다.
- 방법: 같은 지시 흐름과 같은 교란을 (가) 해법기 배정·일정, (나) LLM 배정·일정, (다) 최근접 배정 기준선에 똑같이 재생한다. 배정기를 바꿔 끼우는 구조와 해법기 기준값 비교에서 도출한 설계다. [추정][^ref-749][^ref-592]
- 측정 지표와 조건: 실행 가능 비율, 해법기 기준값 대비 최적성 간격, 재스케줄 뒤 시작 시각 편차, 반복 시행 분산, 문장 표현 바꿔 쓰기에 대한 민감도. [추정][^ref-592][^ref-594][^ref-746] '운영 안정성'은 문헌에서 직접 측정되지 않아 q5-18 에서 정의를 정한 뒤 판정한다.
- 필요한 자료: 해법기 기준값(q5-05, q5-12), 창고 레이아웃과 교란 조합(q5-13).
- 제안한 실행 id: 2026-09-25-100
- 상태: 제안

### 세 계획의 공통 조건

- LLM 모의 관리자로 지시를 넣는 경우, 모의 사용자가 실제 사용자 성과를 체계적으로 틀리게 추정할 수 있다는 보고가 있어 실제 관리자 소수 표본으로 보정하는 편이 맞아 보인다(q5-14). [추정][^ref-740]
- 결과는 '문헌 근거 수준'과 구분되는 'ROP 실험 판정'의 근거로 쓰며, `[사용자 실험]` 태그로 반영된 뒤 내용 검증 에이전트가 판정한다.

[^ref-748]: arXiv 2508.19074 저자(미확인), An LLM-powered Natural-to-Robotic Language Translation Framework with Correctness Guarantees, 2025-08, https://arxiv.org/abs/2508.19074, 접근일 2026-09-25 (원문 미열람)
[^ref-674]: Liu, Z., Fernandez-Ayala, V. N., Wang, T., Qin, Q., Wang, X. V., Dimarogonas, D. V., & Wang, L.(KTH), Agentic Neuro-Symbolic Planning and Commissioning for Human-in-the-Loop Industrial Robotics with Digital Twins, 2026-06, https://arxiv.org/abs/2606.08214, 접근일 2026-09-25 (원문 미열람)
[^ref-749]: Gupta, R. 외(RobotFleet 저자, arXiv 2510.10379), RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning, 2025-10, https://arxiv.org/abs/2510.10379, 접근일 2026-09-25 (원문 미열람)
[^ref-592]: ConstraintBench 저자(arXiv 2602.22465, 저자 미확인), ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization, 2026-02, https://arxiv.org/abs/2602.22465, 접근일 2026-09-25 (원문 미열람)
[^ref-594]: SCHEDBench 저자(arXiv 2608.00991, 저자 미확인), SCHEDBench: A Benchmark for Evaluating LLM Constraint Faithfulness in Natural-Language Combinatorial Scheduling, 2026-08, https://arxiv.org/abs/2608.00991, 접근일 2026-09-25 (원문 미열람)
[^ref-236]: Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation, 2026-08-11, https://doi.org/10.3390/electronics15163562, 접근일 2026-09-25 (원문 미열람)
[^ref-237]: Kluge-Wilkes, A. 외(RWTH Aachen WZL), Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems, 2022, https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-746]: Atil, B. 외, Non-Determinism of "Deterministic" LLM Settings (Eval4NLP 2025 게재판 제목: Non-Determinism of "Deterministic" LLM System Settings in Hosted Environments, 수치는 arXiv 판 기준), 2024-08, https://arxiv.org/abs/2408.04667, 접근일 2026-09-25 (원문 미열람)
[^ref-740]: Lost in Simulation 저자(arXiv 2601.17087, 게재처 미확인), Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations, 2026-01, https://arxiv.org/abs/2601.17087, 접근일 2026-09-25 (원문 미열람)

## 사용자 실험 결과 요약

아직 없음.
