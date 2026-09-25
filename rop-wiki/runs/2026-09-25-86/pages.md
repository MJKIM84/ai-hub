# 스토리텔러 산출 2026-09-25-86

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md | draft | q5-03 답함(판정 절차·판정 값 규칙·가설별 근거·잠정 판정표·필요 실험), 2절에 q5-16~q5-19 추가, 후속 질문 2건(q5-19, q3-16), 완료 조건 현황·상태 줄 갱신 |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 3절 가설 판정 칸을 부분 지지(잠정)로 갱신(단계 5 · 실행 2026-09-25-86), 판정 규칙 단락·변경 기록 추가, 6절에 실행 기록 추가, 8절에 판정 근거 각주 |
| update | docs/ideas/nl-task-chatbot.md | draft | 6절에 '가설 판정 절차' 소절 추가(확실성 평가·TRL 보조 축·판정 값 규칙·잠정 판정 요약·필요 실험, 추정 중심) |
| update | docs/tracks/nl-task-chatbot/experiments.md | draft | '제안된 실험 계획' 절에 E5-01~E5-03 을 제안(사용자 수행 대기)으로 추가 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 5 | q5-03 답함: 가설 판정 절차·규칙과 잠정 판정(가설 1~3 부분 지지(잠정)), 실험 계획 E5-01~E5-03 제안 | run 2026-09-25-86
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 5: q5-03 답함, 가설 1~3 잠정 부분 지지 판정표와 제안 실험 E5-01~E5-03(이 위키의 종합, 신뢰도 low)
- 대분류 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 5: 13. 작업 배정 — MRTA 관련 LLM 직접 배정 대 해법기 배정 근거로 가설 1~3 잠정 부분 지지 판정(반영 제안)
- 세부영역 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 트랙 자연어 업무 지시 챗봇 단계 5 에서 LLM 직접 배정 대 해법기 배정 비교와 최근접 기준선 실험을 6. 대표 접근법과 기술 반영 제안으로 냄

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 절제 실험 | Ablation Study | 시스템의 한 구성 요소를 빼거나 다른 것으로 바꿔 성능 변화를 재어 그 구성 요소의 기여를 확인하는 실험이다. | 23, 27 | ref-674 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-807 | Cochrane | Chapter 14: Completing ‘Summary of findings’ tables and grading the certainty of the evidence | 정부·연구기관 | medium | https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14 |
| ref-809 | NASA ESTO | Definition Of Technology Readiness Levels | 정부·연구기관 | medium | https://esto.nasa.gov/files/trl_definitions.pdf |
| ref-813 | Gupta, R. 외(RobotFleet 저자, arXiv 2510.10379) | RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning | 논문 | medium | https://arxiv.org/abs/2510.10379 |
| ref-814 | therohangupta (RobotFleet 공식 저장소) | robot-fleet — RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning (GitHub README) | 오픈소스 문서 | medium | https://github.com/therohangupta/robot-fleet |
| ref-815 | Garrabé, É., Teixeira, P., Khoramshahi, M., & Doncieux, S. | Enhancing Robustness in Language-Driven Robotics: A Modular Approach to Failure Reduction | 논문 | medium | https://arxiv.org/abs/2411.05474 |
| ref-816 | 강건(대한산업공학회 추계학술대회 논문집) | 제조 물류 로봇에서의 대규모 언어 모델(LLM)을 활용한 로봇 협업 인터페이스 구축 | 논문 | low | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11609734 |
| ref-166 | Obata, K., Aoki, T., Horii, T., Taniguchi, T., & Nagai, T. | LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning | 논문 | medium | https://arxiv.org/abs/2410.21040 |
| ref-674 | Liu, Z., Fernandez-Ayala, V. N., Wang, T., Qin, Q., Wang, X. V., Dimarogonas, D. V., & Wang, L.(KTH) | Agentic Neuro-Symbolic Planning and Commissioning for Human-in-the-Loop Industrial Robotics with Digital Twins | 논문 | medium | https://arxiv.org/abs/2606.08214 |
| ref-592 | ConstraintBench 저자(arXiv 2602.22465, 저자 미확인) | ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization | 논문 | medium | https://arxiv.org/abs/2602.22465 |
| ref-594 | SCHEDBench 저자(arXiv 2608.00991, 저자 미확인) | SCHEDBench: A Benchmark for Evaluating LLM Constraint Faithfulness in Natural-Language Combinatorial Scheduling | 논문 | medium | https://arxiv.org/abs/2608.00991 |
| ref-611 | RACE-Sched 저자(arXiv 2605.29262, 저자 미확인) | Harmonizing Real-Time Constraints and Long-Horizon Reasoning: An Asynchronous Agentic Framework for Dynamic Scheduling | 논문 | medium | https://arxiv.org/abs/2605.29262 |
| ref-612 | Li, J., & Li, C.(소속 미확인) | LLM-Guided Heuristic Design from Simulation Traces: A Case Study in Dynamic Production and AGV Scheduling | 논문 | medium | https://arxiv.org/abs/2608.09343 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 논문 | medium | https://doi.org/10.3390/electronics15163562 |
| ref-041 | Naqvi, M. R. 외(Scientific Reports) | Ontology-driven integration of advertised and operational capabilities in robots | 논문 | medium | https://www.nature.com/articles/s41598-025-16649-3 |
| ref-746 | Atil, B. 외 | Non-Determinism of "Deterministic" LLM Settings | 논문 | medium | https://arxiv.org/abs/2408.04667 |
| ref-359 | Wang, W. 외 | Learning to Ask: When LLM Agents Meet Unclear Instruction | 논문 | medium | https://arxiv.org/abs/2409.00557 |
| ref-677 | CoMuRoS 저자(arXiv 2511.22354, Frontiers in Robotics and AI 게재) | LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning | 논문 | medium | https://arxiv.org/abs/2511.22354 |
| ref-168 | Kaitha, S., & Yu, S. 외(arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 논문 | medium | https://arxiv.org/abs/2512.02810 |
| ref-734 | Rangsaritratsamee, R., Ferrell Jr., W. G., & Kurz, M. B.(Computers & Industrial Engineering 46) | Dynamic rescheduling that simultaneously considers efficiency and stability | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0360835203000950 |
| ref-400 | International Journal of Planning and Scheduling 게재 논문(저자 미확인) | Automated guided vehicle dispatching based on combinatorial optimisation to minimise job waiting time on shop floors | 논문 | medium | https://www.inderscience.com/info/inarticle.php?artid=103016 |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 수행 자원 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-03 | 단계 5. 검증 방법과 가설 판정 |
| 피킹 | 예외·성과 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-03 | 단계 5. 검증 방법과 가설 판정 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| RobotFleet (LLM·MILP 작업 배정기를 둔 중앙 다중 로봇 계획 틀) | 오픈소스 | therohangupta (RobotFleet 공식 저장소) | 13, 27 | ref-814 | https://github.com/therohangupta/robot-fleet |

## 추가 조사 요청

- 단계 5 페이지 3절 q5-03 가설 3 근거: RobotFleet 논문(arXiv 2510.10379)의 LLM 배정기 대 MILP 배정기 비교 결과 수치 — README 에 없고 논문 원문 미열람이라 본문에 넣지 못했다
- 단계 5 페이지 3절 q5-03 가설 1 근거: Garrabé 외(arXiv 2411.05474)의 모듈형 구조 대 code-as-policies 성공률 수치 — 검색 요약에 수치가 없어 '높았다'로만 썼다
- 단계 5 페이지 3절 q5-03 근거 공백: 국내 학술대회 논문(강건, 2023-11, DBpia NODE11609734)의 초록·결과 — 서지만 확인되어 판정 근거로 쓰지 못했다
- q5-19: 가설별 하위 주장을 q5-01 지표와 문턱으로 조작적으로 정의한 선행 사례 — 판정 규칙이 이 위키의 종합(추정)에 머물러 있다
- 단계 5 페이지 상태 줄은 차등 갱신(patches)으로 고칠 수 없는 H1 아래 줄이어서 이 페이지만 전체 content 로 보냈다. 단계 페이지 상태 줄을 자동 영역으로 두거나 패치 대상으로 허용할지 pipeline 담당의 판단을 요청한다

## 이행한 수정 지시

- 트랙 개요 3절 판정 기재 — 가설 1~3 판정 칸을 '부분 지지(잠정)'으로, 근거 칸을 '단계 5 · 실행 2026-09-25-86 · 확실성 낮음'(가설 2는 '확실성 매우 낮음~낮음')과 단계 페이지 링크로 고쳤고, 가설 문장의 [가설] 태그는 그대로 두었다
- f16·f17·f18·f19·f20·f21·f22·f24 추정 유지 — 단계 페이지 3·4절, 아이디어 페이지 6절, 트랙 개요 3절, 실험 페이지에서 모두 [추정]으로 두고 '이 위키의 종합'을 병기했다
- f19 설명 가능성 — 단계 페이지 잠정 판정표·가설 2 서술, 트랙 개요 3절, 아이디어 페이지 판정표에 '설명 가능성 하위 주장은 직접 근거가 없어 미판정이고 부분 지지는 재현성 쪽 간접 근거에만 기댄다'를 적었다
- f6 분리 — CoMuRoS 정답률 0.91 은 [사실](저자 보고)로, LTAA 는 두 2차 요약을 모두 제시한 [추정] 문장으로 나누고 oq-030 에 연결했다
- f13 조건 병기 — 단계 페이지 가설 3 반례·판정 서술, 트랙 개요 3절, 아이디어 페이지, 13. 작업 배정 — MRTA 반영 제안에 '제조·AGV 시뮬레이션 조건, 저자 보고, 롤링 MILP 는 AGV 운송 하위 문제의 추상화, 물류 창고 적용 미확인'을 적었다
- f4 연계 대상 — Garrabé 외 문장 뒤에 조작 과제의 접지·재시도를 '연계 대상(로봇 자체 지능·제어)'으로 밝히고 구조 비교의 근거로만 쓴다고 적었다
- f15 독립성 — RobotFleet 논문과 README 는 같은 저자라 독립 교차가 아니며 LLM 대 MILP 비교 결과는 미확인이라고 본문과 남은 불확실성에 적었다
- 각주 원문 미열람 — ref-814 를 뺀 이번 브리프 출처(ref-807·812·813·815·816 과 재사용 출처)의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true(ref-814 는 false)를 넣었다
- experiments.md 제안된 실험 계획 — E5-01~E5-03 을 '제안(사용자 수행 대기)' 상태로 싣고 결과·수치 없이 f21·f22 근거를 [추정]으로 두었으며, E5-03 에 최근접 배정 기준선을 넣었고 H2 제목은 그대로 두었다
- 단계 5 페이지 6절 — 세 완료 조건의 검증 판정 칸을 모두 '미승인'으로 두고 전환 줄을 지시 문구대로(이번 새 질문 id q5-19 를 괄호로 병기) 썼으며, 상태 줄을 진행 중·미충족으로 두고 2절 표에 q5-16~q5-18(과 새 질문 q5-19)을 넣어 열린 질문 15건·답한 질문 3건으로 맞췄다
- 트랙 개요 상태 줄 — 현재 단계 '단계 3. 구현 가설 설계', 마지막 트랙 실행 2026-09-25 를 그대로 유지했고 track_updates.stage_transition 은 넣지 않았다
- 업무 분해·배정 설계 초안 — 온톨로지 변경이 없어 pages 에 넣지 않았고 ontology_draft_version 은 '0.9' 를 유지했다

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md
- 온톨로지 초안 버전: 0.9
- 트랙 로그 항목: 답한 질문: q5-03(판정 절차·판정 값 규칙·가설별 근거·잠정 판정표: 가설 1~3 모두 부분 지지(잠정), 이 위키의 종합, 신뢰도 low) / 새 질문: q5-19(단계 5, f17), q3-16(단계 3, f13) / 온톨로지 변경: 없음(업무 분해·배정 설계 초안 v0.9 유지, 가설 판정은 작업 모델의 개념·관계가 아니라 검증 방법) / 완료 조건 평가: 미충족(부족: 평가 지표·검증 절차 조건 미충족 유지, 가설 판정표·실험 계획은 잠정으로 실었으나 검증 판정 전, 앞 단계 3·4 완료 미승인) / 세부영역 반영 제안: 13. 작업 배정 — MRTA, 23. 시험·형식 검증·벤치마크, 27. AI·학습·적응과 모델 운영 3건(모두 6. 대표 접근법과 기술) / 다음 실행 제안: 현재 단계 3 의 q3-16·q3-05, 또는 단계 5 의 q5-19·q5-05
- 개요 진행 현황: 단계 3 진행 중(현재 단계 유지, 단계 전환 미승인) — 이번 실행은 지정 질문으로 단계 5 의 q5-03 답함; 단계 5 열린 질문 15, 답함 3, 완료 조건 미충족; 트랙 개요 3절에 가설 1~3 부분 지지(잠정) 기재, 실험 E5-01~E5-03 제안

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q5-03 | 답함 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-03 | — | — | — |
| q5-19 | 열림 | — | 가설 판정표에서 '잘못된 배정'(가설 1), '설명·재현 가능'(가설 2), '운영 안정성'(가설 3)을 q5-01 의 어떤 지표와 문턱으로 조작적으로 정의해야 지지·부분 지지·기각을 가를 수 있는가? (q5-03 에서 파생) | 5 | f17 |
| q3-16 | 열림 | — | LLM 이 루프 밖에서 설계한 규칙이 롤링 MILP 를 앞선 보고를 고려할 때, 가설 3 의 '최적화 엔진'을 해법기로 한정할지 검증을 거친 결정적 규칙 실행기까지 넓힐지, 그에 따라 스케줄링 분담 설계를 어떻게 바꾸는가? (q5-03 에서 파생) (관련: q4-08) | 3 | f13 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 6. 대표 접근법과 기술 | LLM 직접 배정 대 해법기 배정 비교 근거(LiP-LLM 선형계획 배정의 배정 실패 거의 없음, 시뮬레이션 과제·저자 보고; RobotFleet 은 LLM·MILP 배정기를 두나 같은 저자 자료이고 비교 결과 미확인)와 반례(CoMuRoS 정답률 최대 0.91, 실험실 텍스트 벤치마크; LTAA 는 2차 요약 충돌 oq-030), LLM 설계 규칙이 롤링 MILP 를 앞선 보고(제조·AGV 시뮬레이션 조건, 저자 보고, 롤링 MILP 는 AGV 운송 하위 문제의 추상화, 물류 창고 적용 미확인), 최근접 배정 기준선을 둔 판정 실험 설계(추정). 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽 연결 |
| 23 | 6. 대표 접근법과 기술 | GRADE 식 확실성 평가(결과별 네 수준, 다섯 영역 하향)와 TRL 4·5 구분을 보조 축으로 써서 기술 가설을 하위 주장별로 판정하는 방법과 판정 값 규칙(지지·부분 지지·기각·미판정) — 이 위키의 종합(추정), 판정 규칙을 직접 정한 출처 없음 |
| 27 | 6. 대표 접근법과 기술 | 모듈형 접지 구조가 직접 코드 생성 기준선보다 조작 과제 성공률이 높았다는 보고(원인: 접지 부족·개루프 실행, 로봇 자체 지능·제어는 연계 대상), 기호 검증기를 LLM 으로 바꾼 절제 실험의 성공률 급락(98.1%→3.8%, 산업 셀·저자 보고), 결정적 설정 LLM 의 반복 정확도 변동(최대 15%), LLM 이 루프 밖에서 설계한 스케줄링 규칙(제조·AGV 시뮬레이션). 적용 대상 13. 작업 배정 — MRTA 와 함께 연결 |
