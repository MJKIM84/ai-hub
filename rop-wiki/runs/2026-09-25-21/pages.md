# 스토리텔러 산출 2026-09-25-21

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md | draft | q1-02 답함(3절 q1-02 소제목 추가), 2·4·5·6·7·8·9절 갱신, 후속 질문 q3-05·q3-06. H1 아래 상태 줄(답한 질문 1건 → 2건)은 절 패치로 고칠 수 없어 퍼블리셔 처리 요청 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | 초안 v0.1 → v0.2: 배정 개념에 속성 '배정 산출 방식' 추가·확정(f3·f5·f7·f8·f9), '규칙' 값은 6절 질문으로. H1 버전 표기를 바꿔야 해서 전체 content 로 보냄 |
| update | docs/ideas/nl-task-chatbot.md | draft | 3절 갱신: LLM 담당 범위와 LLM·최적화 결합 선행 연구, 제품 사례 소절(공개 에이전트 프레임워크, 로봇 운영 제품 — 벤더 주장) 작성, q1-03 미조사 명시 |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6절 살아있는 산출물 링크 갱신(초안 v0.2, 아이디어 2 3절 제품 사례 작성). 상태 줄은 값 변화 없음 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 1 | q1-02 답함(LLM 담당 범위 세 방식, LLM 정식화와 최적화 배정 연구, 로봇 운영 제품 사례는 벤더 주장), 업무 분해·배정 설계 초안 v0.1 → v0.2, 새 질문 2건 | run 2026-09-25-21
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 1: q1-02 답함(LLM이 맡는 범위 세 방식과 로봇 운영 제품 사례, 제품은 벤더 주장), 업무 분해·배정 설계 초안 v0.2
- 대분류 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 트랙 자연어 업무 지시 챗봇이 LLM 정식화와 선형계획·정수계획·MILP 배정을 결합한 연구를 확인하고 이 영역 6·8절 반영을 제안
- 세부영역 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 트랙 자연어 업무 지시 챗봇 단계 1(실행 2026-09-25-21)이 LLM 직접 배정과 LLM 정식화 + 최적화 배정의 두 방식을 확인, 6. 대표 접근법과 기술·8. 대표 연구와 자료 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | LLM 에이전트 | LLM Agent | 대규모 언어 모델이 사람이 정해 준 도구·함수(로봇 API, 조회 기능 등)를 골라 호출하며 여러 단계로 작업을 수행하도록 구성한 소프트웨어이다. | 27, 13, 18 | ref-295, ref-296, ref-299 |
| new | 혼합 정수 계획 | Mixed Integer Linear Programming (MILP) | 일부 결정 변수가 정수여야 하는 선형 목적함수·선형 제약 최적화 문제로, 작업 배정·스케줄링 같은 조합 결정을 정식화해 해법기로 푸는 데 쓰인다. | 13, 14, 27 | ref-291 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-089 | SMARTlab-Purdue (Purdue University) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (GitHub README) | 오픈소스 문서 | medium | https://github.com/SMARTlab-Purdue/SMART-LLM |
| ref-091 | Cranial-XIX (LLM+P 저자) | llm-pddl — LLM+P: Empowering Large Language Models with Optimal Planning Proficiency (GitHub README) | 오픈소스 문서 | medium | https://github.com/Cranial-XIX/llm-pddl |
| ref-288 | TASL Lab (LaMMA-P 저자) | LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner (GitHub README) | 오픈소스 문서 | medium | https://github.com/tasl-lab/LaMMA-P |
| ref-289 | Autonomous Robots 게재 서베이(arXiv 2502.03814) 저자 | Large Language Models for Multi-Robot Systems: A Survey | 논문 | medium | https://arxiv.org/abs/2502.03814 |
| ref-290 | Obata, K., Aoki, T., Horii, T., Taniguchi, T., & Nagai, T. | LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning | 논문 | medium | https://arxiv.org/abs/2410.21040 |
| ref-291 | Peng, M., Chen, Z., Yang, J., Huang, J., Shi, Z., Liu, Q., Li, X., & Gao, L. | Automatic MILP Model Construction for Multi-Robot Task Allocation and Scheduling Based on Large Language Models | 논문 | medium | https://arxiv.org/abs/2503.13813 |
| ref-292 | Kaitha, S., & Yu, S. 외(arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 논문 | medium | https://arxiv.org/abs/2512.02810 |
| ref-293 | SHAILAB-IPEC (COHERENT 저자) | COHERENT: Collaboration of Heterogeneous Multi-Robot System with Large Language Models (GitHub README) | 오픈소스 문서 | medium | https://github.com/SHAILAB-IPEC/COHERENT |
| ref-294 | Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. | IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models | 논문 | medium | https://arxiv.org/abs/2603.02669 |
| ref-295 | NASA Jet Propulsion Laboratory (nasa-jpl) | ROSA — ROS Agent (GitHub README) | 오픈소스 문서 | medium | https://github.com/nasa-jpl/rosa |
| ref-296 | NASA Jet Propulsion Laboratory (nasa-jpl) | Custom Agents · nasa-jpl/rosa Wiki | 오픈소스 문서 | medium | https://github.com/nasa-jpl/rosa/wiki/Custom-Agents |
| ref-297 | Microsoft | PromptCraft-Robotics (GitHub README) | 오픈소스 문서 | medium | https://github.com/microsoft/PromptCraft-Robotics |
| ref-298 | Vemprala, S., Bonatti, R., Bucker, A., & Kapoor, A. (Microsoft) | ChatGPT for Robotics: Design Principles and Model Abilities | 논문 | medium | https://arxiv.org/abs/2306.17582 |
| ref-299 | Robotec.ai (RobotecAI) | RAI — vendor agnostic agentic framework for Physical AI robotics (GitHub README) | 오픈소스 문서 | medium | https://github.com/RobotecAI/rai |
| ref-300 | InOrbit.AI | InOrbit Unveils RobOps Copilot for AI-Powered Robot Optimization at Automate 2024 | 벤더 문서 | low | https://www.inorbit.ai/press/inorbit-robops-copilot |
| ref-301 | InOrbit.AI (RoboticsTomorrow 게재 보도자료) | InOrbit.AI Demonstrates the Future of Multi-Vendor Robot Orchestration and Physical AI at Automate 2026 | 벤더 문서 | low | https://www.roboticstomorrow.com/news/2026/06/22/inorbitai-demonstrates-the-future-of-multi-vendor-robot-orchestration-and-physical-ai-at-automate-2026/26757/ |
| ref-302 | Formant (Business Wire 보도자료) | Formant F3 Brings Generative AI and Agentic Reasoning to Robot Ops | 벤더 문서 | low | https://www.businesswire.com/news/home/20250630008190/en/Formant-F3-Brings-Generative-AI-and-Agentic-Reasoning-to-Robot-Ops |
| ref-303 | 와우테일 | 다임리서치, 중기부-인텔 '인지니어스' 글로벌 협업 기업 선정 | 기사 | low | https://wowtale.net/2026/08/27/263530/ |
| ref-304 | 이종록, 황정훈, 박민철(한국전자기술연구원) | LLM 기반 로봇관제시스템의 Agent AI 구축 | 논문 | medium | https://d2j16w31g89z0j.cloudfront.net/site/2026w/abs/0560-YDVVV.pdf |
| ref-305 | Shi, G., Wu, Y., Kumar, V., & Sukhatme, G. S. | PIP-LLM: Integrating PDDL-Integer Programming with LLMs for Coordinating Multi-Robot Teams Using Natural Language | 논문 | medium | https://arxiv.org/abs/2510.22784 |
| ref-306 | Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D.(JHU APL·JHU·DEVCOM ARL) | FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams | 논문 | medium | https://arxiv.org/abs/2510.07417 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 출처 충돌: LTAA(arXiv 2512.02810) 초록 요약은 로봇 전문화가 강한 설정에서 LLM 배정이 작업 완료율 77%로 전통 기법을 모두 앞섰다고 하지만, 다른 2차 요약은 동적 계획법의 완료율이 더 높다고 적는다. 어느 쪽이 원문 결과인가? | 13, 27 | 열림 | — |

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ROSA (ROS Agent) | 오픈소스 | NASA Jet Propulsion Laboratory | 27, 18 | ref-295 | https://github.com/nasa-jpl/rosa |
| RAI | 오픈소스 | Robotec.ai | 27, 18 | ref-299 | https://github.com/RobotecAI/rai |

## 추가 조사 요청

- pipeline 요청: 단계 1 페이지 H1 아래 상태 줄('답한 질문: 1건')은 절 패치로 고칠 수 없다. 이번 실행 반영 후 값은 '단계 상태: 진행 중 · 열린 질문: 4건 · 답한 질문: 2건 · 완료 조건: 미충족 · 마지막 실행: 2026-09-25'이므로 퍼블리셔가 백로그로 다시 계산하거나 H2 밖 머리 영역 패치를 지원해 주기 바란다.
- pipeline 요청: 업무 분해·배정 설계 초안은 1차 검증이 H1 버전 표기 '(v0.2)' 갱신을 지시해 절 패치 대신 전체 content 로 보냈다. 초안 H1 버전 표기를 ontology_version 에서 자동으로 맞추는 처리가 있으면 patches 로 돌아갈 수 있다.
- 단계 1 페이지 3절 q1-02: LTAA(ref-292) 원문의 비교 결과(동적 계획법 대비 완료율)를 원문으로 확인해 출처 충돌 열린 질문을 해소할 필요가 있다.
- 단계 1 페이지 3절 q1-02: LiP-LLM(ref-290)의 '배정 실패가 거의 없음' 결과의 실험 조건과 LaMMA-P 논문(arXiv 2409.20560)의 모듈 구성을 원문으로 확인할 필요가 있다.
- 단계 1 페이지 3절 q1-02: PIP-LLM(ref-305)의 창고 작업 적용 여부를 논문 원문으로 확인할 필요가 있다(q1-05·q1-06 연결).
- 백로그 정리: q1-05와 q1-06은 같은 질문의 중복 등록이다(실행 2026-09-25-21 검증 지적). 하나를 폐기하거나 병합하는 결정이 필요하다.
- 단계 1 완료 조건: 채팅·음성 지시 제품의 확인·승인 방식(q1-03)과 지시 분해 접근 유형 목록의 업무 분해·배정 설계 초안 반영(검증 승인 필요)이 남아 있다.

## 이행한 수정 지시

- ref-305 기관·발행일 — 단계 1 페이지·아이디어 2 페이지·설계 초안의 각주 정의와 reference_updates 의 기관을 'Shi, G., Wu, Y., Kumar, V., & Sukhatme, G. S.', 발행일을 2025-10으로 적었다.
- ref-306 기관 — 세 페이지의 각주 정의와 reference_updates 의 기관을 확인된 저자 목록과 소속(JHU APL·JHU·DEVCOM ARL)으로 적었다.
- 원문 미열람 표시 — 지시된 15개 출처의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙였고(ref-089·ref-091은 기존 각주 줄에 표시를 더함), reference_updates 에 source_unopened: true 를 넣었다.
- f2·f4·f5·f10 수치 조건 — 단계 1 페이지 3절과 아이디어 2 페이지 3절에서 수치·비교 결과마다 같은 문장이나 바로 뒤 문장에 '저자 보고값, 독립 재현 미확인'과 평가 조건(MAT-THOR·AI2-THOR 가정 작업, 실험 조건 미확인, 항공기 외피 제조·makespan 최소화, TEACh 건설 작업)을 적었다.
- f10 출처 충돌 — 두 요약을 모두 [추정]으로 제시하고 한쪽을 고르지 않았으며, 동적 계획법 완료율 '0.95'는 본문과 열린 질문 문장에서 뺐다.
- f12 각주 — 고수준 함수 라이브러리로 코드 합성 서술에는 ref-298만, PromptCraft 저장소·AirSim 시뮬레이터 공개 서술에는 ref-297만 달았다.
- f17~f20·f22 벤더 주장 — 단계 1 페이지 제품 사례, 아이디어 2 페이지 제품 사례의 모든 문장에 [추정]과 '벤더 주장'을 병기했고 18. 사람–로봇 협업·운영 인터페이스 반영 제안에도 벤더 주장임을 적었다. 마케팅 표현과 기사 속 고객사·공정 수는 넣지 않았고 다비스는 '개발 계획'임을 밝혔다.
- f14·f15 한정 — 확인·권한 장치 서술을 'README·위키(연 문서) 범위에서 설명이 없다'로 한정하고 부재를 단정하지 않았다.
- f23 — PIP-LLM의 창고 작업 언급을 '일반 검색 요약에만 있고 논문 요약에서는 확인되지 않아 미확인'으로 쓰고, 검색 범위의 결과이며 부재의 확인이 아님을 밝혔다.
- f21 — 세 방식이 이 위키의 정리이며 단일 출처가 없다는 점과 q1-01의 여섯 유형(분해 결과 형태)과 축(LLM 담당 범위)이 다르다는 점을 단계 1 페이지 3절과 아이디어 2 페이지 3절에 적었다.
- 용어 — 새 본문에서 '과업' 대신 '작업'을 썼고, '선언 그래프'는 첫 등장 때 disjunctive graph 를 병기했으며, MILP 는 첫 등장 때 '혼합 정수 계획(Mixed Integer Linear Programming, MILP)'으로 썼다.
- 온톨로지 변경 — 배정 행에 별도 속성 '배정 산출 방식'(값 후보 LLM 직접 추론 f9 / 최적화 해법 f3·f5·f7·f8)을 더하고 상태를 확정으로 바꿨으며, '규칙' 값은 6절 질문으로 두었다. H1 '(v0.2)', 프런트매터 ontology_version '0.2', track_updates.ontology_draft_version '0.2' 를 맞췄다(H1 을 바꾸기 위해 초안 페이지는 전체 content 로 보냈고, 상태 줄은 auto:page-status 마커라 퍼블리셔가 프런트매터 값으로 채운다).
- 새 질문 2건 — backlog_updates 에 q3-05(origin f10), q3-06(origin f8)을 단계 3으로 등록하고 단계 1 페이지 5절에도 적었다.
- 단계 1 페이지 — 2절 q1-02를 답함(실행 2026-09-25-21, 답 위치 #q1-02)으로 바꾸고, 3절에 '### q1-02 … {#q1-02}' 소제목을 두었으며, 4절 남은 불확실성에 운영 제품 미션 호출·새 분해 여부와 실행 전 확인·권한 장치 미확인(f22, q1-03과 연결)을 적었다.
- 단계 1 페이지 6절 — 두 완료 조건의 검증 판정 칸을 '미충족 · 미승인'으로, 표 아래 줄을 지시 문구 그대로 '다음 단계로 전환: 아니오(…)'로 썼다. H1 아래 상태 줄의 완료 조건은 기존 값 '미충족' 그대로다.
- 세부영역 페이지 — 13. 작업 배정 — MRTA, 27. AI·학습·적응과 모델 운영, 18. 사람–로봇 협업·운영 인터페이스 페이지는 고치지 않고 area_reflection_proposals 로만 냈으며, 13과 27의 10절 제안에 교차 규칙(학습 기반 배차)에 따른 상호 연결을 적었다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md
- 온톨로지 초안 버전: 0.2
- 트랙 로그 항목: 답한 질문: q1-02(LLM 담당 범위 세 방식, LLM 정식화 + 선형계획·정수계획·MILP·makespan 최소화 배정 연구, 도구·API 기반 에이전트, 로봇 운영 제품 사례 — 제품은 모두 벤더 주장; 근거 f1~f24) / 새 질문: q3-05(f10), q3-06(f8) / 온톨로지 변경: v0.1 → v0.2: 개념 '배정 (Assignment)'에 속성 '배정 산출 방식'(값 후보 LLM 직접 추론 f9 / 최적화 해법(선형계획·정수계획·MILP·makespan 최소화) f3·f5·f7·f8) 추가, 상태 초안 → 확정, 근거 실행 2026-09-25-21; 거부: 값 '규칙'(근거 finding 없음, 6절 질문으로) / 완료 조건 평가: 미충족(부족: 채팅·음성 지시 제품의 확인·승인 비교 q1-03 미조사, 지시 분해 접근 유형 목록이 업무 분해·배정 설계 초안에 미반영) / 세부영역 반영 제안: 13. 작업 배정 — MRTA 4건, 27. AI·학습·적응과 모델 운영 3건, 18. 사람–로봇 협업·운영 인터페이스 1건 / 다음 실행 제안: q1-03, q1-04, q1-05·q1-06 중복 정리
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 4, 답함 2, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-02 | 답함 | docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md#q1-02 | — | — | — |
| q3-05 | 열림 | — | 같은 다중 로봇 배정 작업에서 LLM이 직접 배정하는 방식과 LLM이 정식화하고 선형계획·정수계획·MILP 해법기가 배정하는 방식을 배정 오류율·일정 품질·계산 시간으로 비교한 연구가 있는가, 창고 작업에서도 같은 결과가 나오는가? (q1-02 에서 파생) | 3 | f10 |
| q3-06 | 열림 | — | FLEET처럼 LLM이 만든 로봇–작업 적합도 행렬 대신 로봇 기능 온톨로지 질의(능력·제약 대조)로 적합도를 정해 최적화 해법기에 넘기면 배정 근거의 설명·재현성이 달라지는가, 이를 시도한 연구가 있는가? (q1-02 에서 파생) | 3 | f8 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 6. 대표 접근법과 기술 | LLM 기반 배정의 두 방식: LLM이 분해와 배정을 함께 맡는 방식(COHERENT, LTAA, SMART-LLM)과 LLM이 의존 그래프·정식화를 만들고 선형계획(LiP-LLM)·정수계획(PIP-LLM)·makespan 최소화(FLEET)·MILP(Peng 외) 해법이 배정·일정을 맡는 방식. SCM 질문 '가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가?'와 연결해 LLM은 해석·정식화, 전체 최적 배정은 해법기가 맡는 분담의 선행 근거로 제시([추정], 창고 비교 연구 없음). 수치는 저자 보고값 조건 병기. |
| 13 | 8. 대표 연구와 자료 | LaMMA-P(ref-288), LiP-LLM(ref-290), PIP-LLM(ref-305), FLEET(ref-306), Peng 외(ref-291), COHERENT(ref-293), LTAA(ref-292, 출처 충돌 병기), IMR-LLM(ref-294). |
| 13 | 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) | 교차 규칙(학습 기반 배차)에 따라 27. AI·학습·적응과 모델 운영과 연결: LLM 기반 배정 방법은 27. AI·학습·적응과 모델 운영의 연구 방법이 이 영역에 적용된 것이다. |
| 13 | 11. 열린 질문 | LTAA의 LLM 배정 비교 우위에 관한 출처 충돌, 창고 현장에서 최근접 배정과 LLM·최적화 배정을 비교한 연구 부재(q3-05와 연결). |
| 27 | 6. 대표 접근법과 기술 | LLM 다중 로봇 서베이의 네 층 분류(상위 작업 배정·중간 동작 계획·저수준 동작 생성·사람 개입)와 과제(수학적 추론 한계·환각·지연·벤치마크 부족), 사람이 정한 도구·함수 목록 안에서 명령·코드를 생성하는 LLM 에이전트(ChatGPT for Robotics, ROSA, RAI, 한국전자기술연구원 사례)와 연 문서 범위에서 실행 전 확인·권한 장치 설명이 없다는 관찰([추정]). |
| 27 | 8. 대표 연구와 자료 | LLM 다중 로봇 서베이(ref-289), ChatGPT for Robotics(ref-298)와 PromptCraft(ref-297), ROSA(ref-295·ref-296), RAI(ref-299), 한국전자기술연구원 초록(ref-304). |
| 27 | 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) | 교차 규칙에 따라 적용 대상 13. 작업 배정 — MRTA(학습 기반 배차)와 연결: LLM 직접 배정과 LLM 정식화 + 최적화 배정 연구. |
| 18 | 6. 대표 접근법과 기술 | 로봇 운영 제품의 자연어·음성 인터페이스: InOrbit RobOps Copilot(2024 질의·설명, 2026 미션 실행), Formant F3, 다임리서치 다비스(개발 계획). 모두 [추정] 벤더 주장이며 미션 정의 방식과 실행 전 확인·승인 절차는 미확인(q1-03에서 조사). |
