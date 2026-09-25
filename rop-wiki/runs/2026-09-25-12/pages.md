# 스토리텔러 산출 2026-09-25-12

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md | draft | q1-02 답함(3절 소제목 신설), q1-06 행 추가, 4~7절·출처·이력 갱신, 후속 질문 q3-05 1건. 2차 수정: 4절 결론에서 RAI 제외(ROSA·한국전자기술연구원만 [사실]), LaMMA-P 배정 주체 한정. H1 아래 단계 상태 줄(열린 4건·답한 2건)이 H2 밖이라 전체 content로 보냄 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | v0.1 → v0.2: 개념 배정에 속성 '배정 산출 방식'(LLM 직접 추론 / 선형계획·MILP 같은 최적화 해법) 추가, 초안 → 확정, '규칙' 값은 6절 질문. 2차 수정: 배정 정의 칸의 MILP 첫 등장을 풀어 씀. H1 버전 표기를 바꿔야 해서 전체 content로 보냄 |
| update | docs/ideas/nl-task-chatbot.md | draft | 3절 갱신: LLM 담당 범위 세 방식, LLM+최적화 결합 연구, 공개 에이전트 프레임워크, 운영 제품 사례(벤더 주장) 추가 |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6절 살아있는 산출물 링크: 초안 v0.2, 아이디어 2 3절에 제품 사례(벤더 주장) 반영 현황 갱신. 상태 줄은 바뀌지 않음(현재 단계·마지막 실행 동일) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 1 | q1-02 답함(LLM 담당 범위 세 방식, LLM+최적화 결합 연구, 공개 에이전트 프레임워크, 운영 제품 사례 벤더 주장), 업무 분해·배정 설계 초안 v0.1 → v0.2, 아이디어 2 3절 제품 사례 추가; 출처 id 재부여 대응표 ref-144→ref-125, ref-145→ref-126, ref-146→ref-127, ref-147→ref-128, ref-148→ref-129, ref-149→ref-130, ref-150→ref-131, ref-151→ref-132, ref-152→ref-133, ref-153→ref-134, ref-154→ref-135, ref-155→ref-136, ref-156→ref-137, ref-157→ref-138, ref-158→ref-139, ref-159→ref-140, ref-160→ref-141, ref-161→ref-142, ref-162→ref-143 | run 2026-09-25-12
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 1: q1-02 답함(LLM이 맡는 범위 세 방식, LLM+선형계획·MILP 배정 연구, 공개 에이전트 프레임워크, 운영 제품 사례는 벤더 주장), 업무 분해·배정 설계 초안 v0.2
- 대분류 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 자연어 업무 지시 챗봇 트랙 단계 1에서 LLM 직접 배정과 LLM 정식화+선형계획·MILP 배정 연구를 조사하고 이 영역 6·8절 반영을 제안
- 세부영역 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 트랙 자연어 업무 지시 챗봇 단계 1(실행 2026-09-25-12)이 LLM 기반 배정의 두 방식(LLM 직접 배정 대 LLM 정식화+선형계획·MILP·계획기)을 6. 대표 접근법과 기술·8. 대표 연구와 자료에 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | LLM 에이전트 | LLM Agent | 대규모 언어 모델이 사람이 정해 준 도구·함수(로봇 API, 조회 기능 등)를 골라 호출하며 여러 단계로 작업을 수행하도록 구성한 소프트웨어이다. | 27, 13, 18 | ref-134, ref-135, ref-143 |
| new | 혼합 정수 선형 계획 | Mixed Integer Linear Programming (MILP) | 일부 결정 변수가 정수여야 하는 선형 목적함수·선형 제약 최적화 문제로, 작업 배정·스케줄링 같은 조합 결정을 정식화하고 해법기로 푸는 데 쓰인다. | 13, 14 | ref-129 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-125 | TASL Lab (LaMMA-P 저자) | LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner (GitHub README) | 오픈소스 문서 | high | https://github.com/tasl-lab/LaMMA-P |
| ref-126 | Zhang, X. 외(LaMMA-P 저자) | LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner | 논문 | medium | https://arxiv.org/abs/2409.20560 |
| ref-127 | Autonomous Robots 게재 서베이(arXiv 2502.03814) 저자 | Large Language Models for Multi-Robot Systems: A Survey | 논문 | medium | https://arxiv.org/abs/2502.03814 |
| ref-128 | Obata, K. 외(Taniguchi 연구실) | LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning | 논문 | medium | https://arxiv.org/abs/2410.21040 |
| ref-129 | Peng, M., Chen, Z., Yang, J., Huang, J., Shi, Z., Liu, Q., Li, X., & Gao, L. | Automatic MILP Model Construction for Multi-Robot Task Allocation and Scheduling Based on Large Language Models | 논문 | medium | https://arxiv.org/abs/2503.13813 |
| ref-130 | arXiv 2512.02810 저자(미확인) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 논문 | medium | https://arxiv.org/abs/2512.02810 |
| ref-131 | SHAILAB-IPEC (COHERENT 저자) | COHERENT: Collaboration of Heterogeneous Multi-Robot System with Large Language Models (GitHub README) | 오픈소스 문서 | high | https://github.com/SHAILAB-IPEC/COHERENT |
| ref-132 | Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. | IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models | 논문 | medium | https://arxiv.org/abs/2603.02669 |
| ref-133 | Su, X. (IMR-LLM 공식 저장소) | IMR-LLM-Code — Industrial Multi-Robot Task Planning and Program Generation using Large Language Models (ICRA 2026) (GitHub README) | 오픈소스 문서 | high | https://github.com/XiangyuSu611/IMR-LLM-Code |
| ref-134 | NASA Jet Propulsion Laboratory (nasa-jpl) | ROSA — ROS Agent (GitHub README) | 오픈소스 문서 | high | https://github.com/nasa-jpl/rosa |
| ref-135 | NASA Jet Propulsion Laboratory (nasa-jpl) | Custom Agents · nasa-jpl/rosa Wiki | 오픈소스 문서 | high | https://github.com/nasa-jpl/rosa/wiki/Custom-Agents |
| ref-136 | Microsoft | PromptCraft-Robotics (GitHub README) | 오픈소스 문서 | high | https://github.com/microsoft/PromptCraft-Robotics |
| ref-137 | Vemprala, S. 외(Microsoft) | ChatGPT for Robotics: Design Principles and Model Abilities | 논문 | medium | https://arxiv.org/abs/2306.17582 |
| ref-138 | Robotec.ai (RobotecAI) | RAI — vendor agnostic agentic framework for Physical AI robotics (GitHub README) | 오픈소스 문서 | high | https://github.com/RobotecAI/rai |
| ref-139 | InOrbit.AI (RoboticsTomorrow 게재 보도자료) | InOrbit Unveils RobOps Copilot for AI-Powered Robot Optimization at Automate 2024 | 벤더 문서 | low | https://www.roboticstomorrow.com/news/2024/05/01/inorbit-unveils-robops-copilot-for-ai-powered-robot-optimization-at-automate-2024/22505/ |
| ref-140 | InOrbit.AI (RoboticsTomorrow 게재 보도자료) | InOrbit.AI Demonstrates the Future of Multi-Vendor Robot Orchestration and Physical AI at Automate 2026 | 벤더 문서 | low | https://www.roboticstomorrow.com/news/2026/06/22/inorbitai-demonstrates-the-future-of-multi-vendor-robot-orchestration-and-physical-ai-at-automate-2026/26757/ |
| ref-141 | Formant (Business Wire 보도자료) | Formant F3 Brings Generative AI and Agentic Reasoning to Robot Ops | 벤더 문서 | low | https://www.businesswire.com/news/home/20250630008190/en/Formant-F3-Brings-Generative-AI-and-Agentic-Reasoning-to-Robot-Ops |
| ref-142 | 와우테일 | 다임리서치, 중기부-인텔 '인지니어스' 글로벌 협업 기업 선정 | 기사 | low | https://wowtale.net/2026/08/27/263530/ |
| ref-143 | 이종록, 황정훈, 박민철(한국전자기술연구원) | LLM 기반 로봇관제시스템의 Agent AI 구축 | 논문 | medium | https://d2j16w31g89z0j.cloudfront.net/site/2026w/abs/0560-YDVVV.pdf |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 단계 1 페이지 3절·아이디어 2 페이지 3절 제품 사례: InOrbit RobOps Copilot·Formant F3의 자연어 미션 실행이 미리 정의된 미션 호출인지 지시의 새 분해인지와 실행 전 확인·승인·권한 장치를 제품 문서(보도자료가 아닌 공식 문서)로 확인해야 한다 — 현재 벤더 보도자료 검색 요약뿐이며 q1-03 조사와 함께 다룬다.
- 단계 1 페이지 4절: LTAA(arXiv 2512.02810) 원문의 비교 결과(동적 계획법·Q-러닝·DQN 대비 완료율)와 데이터 출처(TEACh 표기)를 확인해야 한다 — 검증 검색에서 요약끼리 엇갈려 비교 우위를 쓰지 못했다(q3-05와 연결).
- 단계 1 페이지 3절: LiP-LLM·Peng 외 원문의 실험 환경·비교 대상과 배정 오류 감소 수치를 확인해야 한다 — 저자 보고값의 평가 조건이 미확인이다.
- 단계 1 페이지 3·4절: RAI가 도구·함수 정의로 에이전트의 행동 범위를 정하는 구조인지 공식 문서로 확인해야 한다 — 2차 검증에서 f13이 이를 뒷받침하지 않는다고 판정되어 결론에서 RAI를 뺐다.
- 단계 1 페이지 3절: 한국전자기술연구원 초록(ref-143)의 학술대회 이름·발표일과, LA-RCS(arXiv 2505.18214) 등 국내 저자 LLM 로봇 관제 연구의 내용 확인이 필요하다 — 한국 자료 우선 규칙.
- 퍼블리셔·pipeline 담당: 이번 브리프의 신규 출처 id(ref-144~ref-162)를 ref-125~ref-143으로 일대일 재부여했다(2차 검증은 1차가 든 충돌 예가 입력 색인과 맞지 않는다고 지적했으나 재부여 id는 현재 색인과 겹치지 않음을 확인). 다음 실행의 next_ref_id는 ref-144 이후여야 한다.
- 트랙 백로그 정리: q1-05와 q1-06이 사실상 같은 질문이라는 검증 지적이 있다. 둘 중 하나를 폐기하거나 병합할지 다음 트랙 실행에서 판단이 필요하다.

## 이행한 수정 지시

- 출처 id 재부여 — 신규 출처 19건을 ref-144~ref-162에서 ref-125~ref-143으로 일대일(각 -19) 재부여하고 단계 1·초안·아이디어 페이지의 본문 각주, 각주 정의, 프런트매터 sources, reference_updates에 같은 대응표를 적용했으며 대응표를 changelog_entry에 남겼다.
- ref-059 — 이번 실행에서 새로 쓴 문장·각주와 reference_updates에 넣지 않았다(단계 1 페이지 q1-01의 기존 인용과 그 각주 정의만 유지).
- f8 — [추정]으로 강등하고 '비교 기법보다 높았다'를 삭제했으며, '저자들은 로봇 전문화가 강한 설정에서 작업 완료율 77%를 보고했다'와 '동적 계획법 0.95 등 비교 결과의 세부와 TEACh 데이터 출처 표기는 원문 미확인'으로만 썼다.
- f17 — '로봇 직접 제어로 응답' 구절을 삭제하고 단계 1·아이디어 페이지에서 자연어 질의응답·시각화와 상시 에이전트의 감시·분석·권고만 [추정] 벤더 주장으로 썼다.
- f2·f4·f5·f8 — 수치·결과 문장마다 같은 문장이나 바로 뒤 문장에 '저자 보고값, 독립 재현 미확인'과 평가 조건(f2 AI2-THOR 기반 가정 작업 MAT-THOR, f4 평가 조건 원문 미확인, f5 제조 생산 제약, f8 건설 작업 시나리오)을 적었다.
- f1 — 여섯 모듈 이름 문장에는 ref-126(arXiv 검색 요약, 원문 미열람) 각주만 달고, ref-125(README)는 LLM 분해·배정과 Fast Downward 계획 구조, MAT-THOR 수치의 근거로만 썼다.
- f6 — 선언 그래프·결정적 해법·공정 트리·IMR-Bench 서술에는 ref-132 각주를 달고, ref-133(README)은 논문 제목과 ICRA 2026 게재 표기의 근거로만 썼다.
- f15·f16·f17·f18·f20 — 단계 1 페이지 3절·4절과 아이디어 2 페이지 3절 제품 사례의 모든 해당 문장에 [추정]과 '벤더 주장'을 병기했고, 다임리서치 기사의 고객사·공정 수와 마케팅 표현은 넣지 않았으며, 18. 사람–로봇 협업·운영 인터페이스 반영 제안 요약에도 벤더 주장을 명시했다.
- 원문 미열람 표시 — ref-126·127·128·129·130·132·137·139·140·141·142·143의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates에 source_unopened: true를 넣었다(원문을 연 README 7건은 false).
- 용어 — 새로 쓴 본문에서 '과업'을 '작업'(작업 분해, 작업 배정, 장기 작업)으로 통일하고, disjunctive graph는 첫 등장 때 '선언 그래프(disjunctive graph)'로 병기했으며, MILP는 페이지와 용어집 모두 '혼합 정수 선형 계획(Mixed Integer Linear Programming, MILP)'으로 맞췄다.
- 온톨로지 변경 일부 승인 — 배정 행에 '선택 근거'와 별도인 속성 '배정 산출 방식'(값: LLM 직접 추론 f7, 선형계획·MILP 같은 최적화 해법 f3·f5)을 더하고 상태를 초안 → 확정으로 바꿨으며, '규칙' 값은 넣지 않고 6절 미해결 모델링 질문으로 두었고, 초안 버전을 H1(v0.2)·프런트매터 ontology_version '0.2'·JSON ontology_draft_version '0.2'로 맞췄다(상태 줄은 auto:page-status 영역이라 퍼블리셔가 프런트매터에서 채운다).
- 새 질문 중복 — '운영 제품의 자연어 미션 실행 … 확인·권한 장치' 질문은 backlog_updates에 넣지 않고, 미리 정의된 미션 호출 대 새 분해의 구분이 미확인이라는 점을 단계 1 페이지 4절 남은 불확실성에 f20 근거(ref-140·ref-141 각주)로 적었다.
- 단계 1 페이지 6절 — 완료 조건 두 행을 모두 '미충족', 검증 판정 칸을 '미충족 · 미승인'으로 쓰고 표 아래 줄을 지시 문구 그대로 '다음 단계로 전환: 아니오(아이디어 2 3절 제품 사례의 확인·승인(q1-03) 미조사, 지시 분해 접근 유형 목록 초안 미반영, 열린 질문 q1-03·q1-04·q1-05·q1-06)'으로 썼다.
- 세부영역 페이지 — 13. 작업 배정 — MRTA, 27. AI·학습·적응과 모델 운영, 18. 사람–로봇 협업·운영 인터페이스 페이지는 pages에 넣지 않고 area_reflection_proposals로만 냈으며, 13과 27의 제안 요약에 교차 규칙에 따른 양쪽 연결을 표시했다.
- 2차: RAI [사실] 드리프트 — 단계 1 페이지 4절 결론의 해당 bullet에서 RAI와 [^ref-138]을 빼고 '사람이 정한 도구로 LLM 에이전트의 행동 범위를 정하는 공개 프레임워크(ROSA)와 국내 연구 사례(한국전자기술연구원)가 있다. [사실][^ref-134][^ref-143]'로 고쳤으며, RAI를 방식 3에 넣은 분류는 3절의 [추정] 3분류 문장에만 남겼다.
- 2차: LaMMA-P 배정 주체 — 단계 1 페이지 4절 결론의 LLM 정식화 + 결정적 해법 bullet에서 사례 괄호를 '(LiP-LLM, Peng 외, IMR-LLM, LaMMA-P(LaMMA-P는 계획 단계만 계획기가 맡고 배정은 LLM이 맡는다))'로 한정해 3절 표·본문의 '방식 1과 방식 2에 걸친다'와 맞췄다.
- 2차: MILP 첫 등장 표기 — 업무 분해·배정 설계 초안 2절 배정 행 정의 칸의 '혼합 정수 선형 계획(MILP)'을 '혼합 정수 선형 계획(Mixed Integer Linear Programming, MILP)'으로 고쳐 용어집 등록명·단계 1 페이지 표기와 같은 문자열로 맞췄다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md
- 온톨로지 초안 버전: 0.2
- 트랙 로그 항목: 답한 질문: q1-02(LLM 담당 범위 세 방식 f19, 서베이 네 층 f9, LLM+결정적 해법 f1·f2·f3·f4·f5·f6, LLM 직접 배정 f7·f8(f8 강등), 도구 기반 명령 생성 f10·f11·f12·f13·f14, 운영 제품 f15·f16·f17(구절 삭제)·f18·f20 벤더 주장, 평가 환경 한계 f21) / 새 질문: q3-05(단계 3, 근거 f8). '운영 제품 미션 실행의 호출·분해·확인 장치' 질문은 q1-03과 중복으로 미등록, 호출 대 분해 미확인은 단계 1 4절에 기록 / 온톨로지 변경: v0.1 → v0.2: 개념 '배정 (Assignment)'에 속성 '배정 산출 방식'(값: LLM 직접 추론 f7, 선형계획·MILP 같은 최적화 해법 f3·f5) 추가, 초안 → 확정. 거부: 같은 변경의 '규칙' 값(근거 finding 없음, 6절 질문으로) / 완료 조건 평가: 미충족(부족: 아이디어 2 3절 제품 사례의 확인·승인 비교(q1-03) 미조사, 지시 분해 접근 유형 목록이 업무 분해·배정 설계 초안에 미반영, 열린 질문 q1-03·q1-04·q1-05·q1-06) / 세부영역 반영 제안: 13. 작업 배정 — MRTA 3건, 27. AI·학습·적응과 모델 운영 3건, 18. 사람–로봇 협업·운영 인터페이스 2건 / 출처 id 재부여: ref-144~ref-162 → ref-125~ref-143 / 2차 수정 반영: 결론에서 RAI [사실] 제외, LaMMA-P 배정 주체 한정, 초안 MILP 첫 등장 풀어 씀 / 다음 실행 제안: q1-03(채팅·음성 지시 제품의 확인·승인), q1-04, q1-05·q1-06 중복 정리
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 4(q1-03·q1-04·q1-05·q1-06), 답함 2(q1-01·q1-02), 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-02 | 답함 | docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md#q1-02 | — | — | — |
| q3-05 | 열림 | — | 같은 다중 로봇 배정 작업에서 LLM이 직접 배정하는 방식과 LLM이 정식화하고 선형계획·MILP 해법기가 배정하는 방식을 배정 오류율·일정 품질·계산 시간으로 비교한 연구가 있는가? (q1-02 에서 파생) | 3 | f8 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 6. 대표 접근법과 기술 | LLM 기반 배정의 두 방식: (1) LLM이 분해와 배정을 모두 하는 방식(SMART-LLM, COHERENT), (2) LLM이 의존 그래프·MILP 정식화·PDDL 문제를 만들고 선형계획·MILP 해법기·계획기가 배정·계획을 맡는 방식(LiP-LLM, Peng 외, IMR-LLM; LaMMA-P는 배정은 LLM, 계획만 계획기). 이 구분은 위키의 정리([추정]). 학습 기반 배차 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽 연결. 근거 ref-131, ref-128, ref-129, ref-125, ref-132 (실행 2026-09-25-12). |
| 13 | 8. 대표 연구와 자료 | LaMMA-P(MAT-THOR 가정 작업에서 성공률 105%·효율 36% 향상, 저자 보고값), LiP-LLM(선형계획 배정, 저자 보고, 조건 미확인), Peng 외(제조 생산 제약에서 제약 추출 82%·MILP 코드 생성 90%, 저자 보고값), COHERENT, LTAA(건설 시나리오 77% 완료율 저자 보고, 비교 우위는 요약이 엇갈려 미확인, [추정]). 물류 지시를 다룬 연구는 이번 검색 범위에서 찾지 못함. |
| 13 | 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) | 27. AI·학습·적응과 모델 운영(LLM 기반 배정은 학습 기반 배차 교차 규칙 적용 대상)과 14. 작업 순서·스케줄링(Peng 외의 MILP 배정·스케줄링 정식화) 연결. |
| 27 | 6. 대표 접근법과 기술 | LLM 다중 로봇 서베이의 네 층 분류(상위 작업 배정, 중간 동작 계획, 저수준 동작 생성, 사람 개입)와 사람이 정한 도구·함수 안에서 LLM 에이전트가 명령·코드를 생성하는 방식(ChatGPT for Robotics, ROSA, 한국전자기술연구원 사례; RAI를 이 방식에 넣는 것은 위키의 [추정] 분류). ROSA 공개 문서 두 건에는 실행 전 사람 확인·권한 제한 설명이 없었음([추정], 부재 확인 아님). 적용 대상 13. 작업 배정 — MRTA와 양쪽 연결. 근거 ref-127, ref-136, ref-137, ref-134, ref-135, ref-138, ref-143. |
| 27 | 7. 관련 표준·프레임워크·오픈소스 | 공개 LLM 에이전트 프레임워크: ROSA(NASA JPL, LangChain 기반, ROS 1·ROS 2), RAI(Robotec.ai, ROS 2 제조사 무관, Apache 2.0), PromptCraft-Robotics(Microsoft 프롬프트 사례 저장소). 근거 ref-134, ref-138, ref-136(확인일 2026-09-25). |
| 27 | 8. 대표 연구와 자료 | Large Language Models for Multi-Robot Systems: A Survey(Autonomous Robots 게재, ref-127), ChatGPT for Robotics(Microsoft, ref-137), 한국전자기술연구원 LLM 기반 로봇관제 Agent AI 초록(ref-143, 학술대회 이름·일자 미확인). |
| 18 | 6. 대표 접근법과 기술 | 로봇 운영 제품의 자연어·음성 인터페이스: InOrbit RobOps Copilot(2024 데이터 질의·설명, 2026 미션 실행 포함), Formant F3(자연어 질의응답·시각화, 상시 에이전트 감시·분석·권고), 다임리서치 다비스(개발 중, 2027년 상반기 출시 계획). 모두 [추정] 벤더 주장이며 실행 전 확인·승인 절차는 공개 자료에서 미확인. 근거 ref-139, ref-140, ref-141, ref-142. |
| 18 | 11. 열린 질문 | 운영 제품의 자연어 미션 실행이 미리 정의된 미션 호출인지 새 분해인지, 실행 전 확인·승인을 어떻게 받는지 미확인(트랙 백로그 q1-03에서 조사). |
