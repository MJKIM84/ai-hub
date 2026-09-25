# 스토리텔러 산출 2026-09-25-99

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md | draft | q5-02 답함(3절 {#q5-02} 소제목 신설: 네 층 가상 시험 구성·한계), 후속 질문 q5-13~q5-15, 2·4·5·6·8·9절 갱신, 7절에 22. 시뮬레이션·예측용 디지털 트윈 추가. 2차: 단계 상태 줄을 열린 질문 12건·답한 질문 2건으로 고치고 SafeAgentBench 10% 출처 문장을 README·초록으로 나눠 고침(상태 줄 때문에 전체 content 로 보냄) |
| update | docs/ideas/nl-task-chatbot.md | draft | 6절에 '검증 절차: 가상 현장·가상 로봇 시나리오 시험' 소절 신설(네 층 구성 표·Mermaid 도식, f18~f21 추정, 근거 f1·f2·f4·f7(강등)·f8·f9·f10·f15), 새 각주 11건(2차 재실행에서 변경 없음) |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 2차: '6. 살아있는 산출물 링크' 절만 갱신 — 아이디어 2 항목에 q5-02 답(검증 절차 소절) 반영과 실행 2026-09-25-99 의 지정 질문 처리 서술 추가, 초안 변경 없음 실행 목록에 2026-09-25-99 추가(현재 단계 표기·상태 줄은 그대로) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 5 | q5-02 답함(가상 현장·가상 로봇 네 층 시험 구성과 한계, 추정 중심), 아이디어 2 6절 검증 절차 소절 신설, 트랙 개요 6절 갱신, 후속 질문 3건 | run 2026-09-25-99
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 5: q5-02(가상 현장·가상 로봇으로 지시 시나리오를 시험하는 방법과 한계) 답함, 지시·실행·교란·반복 네 층 시험 구성(추정)과 후속 질문 3건
- 대분류 최근 업데이트: 2026-09-25 — D. 계획·최적화: 트랙 자연어 업무 지시 챗봇 단계 5 q5-02 답함, 13. 작업 배정 — MRTA 에 가상 현장에서 최근접 배정 기준선과 ROP 배정을 같은 지시 흐름·교란으로 비교하는 설계 반영 제안
- 세부영역 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 트랙 자연어 업무 지시 챗봇 단계 5 q5-02 답함, '6. 대표 접근법과 기술' 절에 가상 현장 비교 설계(창고 레이아웃 자체 구축 필요) 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 사용자 시뮬레이터 | User Simulator | 대화형 에이전트를 평가할 때 목표와 정보를 가진 사용자를 규칙이나 LLM 으로 모사해 에이전트와 대화하게 하는 구성 요소다. | 23, 27, 18 | ref-741, ref-742, ref-743 |
| new | pass^k 지표 | pass^k | 같은 과제를 독립적으로 k번 시행했을 때 모든 시행이 성공할 확률을 추정해 에이전트 행동의 일관성을 재는 지표다. | 23, 27 | ref-741, ref-742 |
| new | 현실 격차 | Reality Gap (Sim-to-Real Gap) | 시뮬레이션의 추상화·근사 때문에 생기는 시뮬레이션과 실제 환경 사이의 동역학·인식·구동 차이로, 시뮬레이션 결과를 현실로 옮기는 것을 어렵게 한다. | 22, 23 | ref-744 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 논문 | medium | https://arxiv.org/abs/2604.05427 |
| ref-623 | Agrawal, A. 외 | RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments | 논문 | medium | https://arxiv.org/abs/2209.05738 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/simulation.html |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — README | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_demos |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC documentation — Challenges (ref-008 ARIAC 문서와 같은 문서 사이트의 challenges 페이지) | 정부·연구기관 | medium | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html |
| ref-741 | Yao, S. 외(Sierra, τ-bench 저자) | τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | 논문 | medium | https://arxiv.org/abs/2406.12045 |
| ref-742 | sierra-research (tau-bench GitHub) | tau-bench — README | 오픈소스 문서 | medium | https://github.com/sierra-research/tau-bench |
| ref-743 | Lost in Simulation 저자(arXiv 2601.17087, 게재처 미확인) | Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations | 논문 | medium | https://arxiv.org/abs/2601.17087 |
| ref-744 | Aljalbout, E. 외(University of Zurich·NVIDIA·University of Washington) | The Reality Gap in Robotics: Challenges, Solutions, and Best Practices | 논문 | medium | https://arxiv.org/abs/2510.20808 |
| ref-407 | gpue (vda5050-sim GitHub) | vda5050-sim — Standards-compliant VDA5050 (v3.0.0) robot fleet simulator (README) | 오픈소스 문서 | medium | https://github.com/gpue/vda5050-sim |
| ref-746 | coatyio (vda-5050-lib.js GitHub) | vda-5050-lib.js — Universal VDA 5050 library for Node.js and browsers (README) | 오픈소스 문서 | medium | https://github.com/coatyio/vda-5050-lib.js |
| ref-747 | Wu, J., Lu, C., Arrieta, A., & Ali, S. 외(Simula Research Laboratory·Mondragon University·PAL Robotics) | Vision Language Model-based Testing of Industrial Autonomous Mobile Robots | 논문 | medium | https://arxiv.org/abs/2508.02338 |
| ref-748 | Yin, S. 외(SafeAgentBench 저자) | SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents | 논문 | medium | https://arxiv.org/abs/2412.13178 |
| ref-749 | shengyin1224 (SafeAgentBench 공식 저장소) | SafeAgentBench — README | 오픈소스 문서 | medium | https://github.com/shengyin1224/SafeAgentBench |
| ref-750 | Atil, B. 외 | Non-Determinism of "Deterministic" LLM Settings | 논문 | medium | https://arxiv.org/abs/2408.04667 |
| ref-751 | 인더스트리뉴스 | 다임리서치, 가상검증 기술로 물류자동화 실현 | 기사 | low | https://www.industrynews.co.kr/news/articleView.html?idxno=56677 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내 물류센터 로봇 관제 도입에서 디지털 트윈·가상 로봇으로 관제 소프트웨어를 사전 검증한 결과를 실제 시운전 결과와 비교해 공개한 사례가 있는가? (관련 기존 질문: oq-094) | 22, 21 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-02 | 단계 5. 검증 방법과 가설 판정 |
| 피킹 | 작업 대상 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-02 | 단계 5. 검증 방법과 가설 판정 |
| 피킹 | 수행 자원 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-02 | 단계 5. 검증 방법과 가설 판정 |
| 피킹 | 제약 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-02 | 단계 5. 검증 방법과 가설 판정 |
| 피킹 | 완료·인계 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-02 | 단계 5. 검증 방법과 가설 판정 |
| 피킹 | 예외·성과 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-02 | 단계 5. 검증 방법과 가설 판정 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| vda5050-sim (VDA 5050 가상 로봇 플릿 시뮬레이터) | 오픈소스 | gpue (vda5050-sim GitHub, 개인 저장소) | 23, 22, 9 | ref-407 | https://github.com/gpue/vda5050-sim |
| vda-5050-lib.js (가상 AGV 어댑터 포함 VDA 5050 라이브러리) | 오픈소스 | coatyio | 23, 9 | ref-746 | https://github.com/coatyio/vda-5050-lib.js |
| τ-bench (도구–에이전트–사용자 상호작용 벤치마크) | 평가 프로그램 | sierra-research | 23, 27, 18 | ref-742 | https://github.com/sierra-research/tau-bench |
| SafeAgentBench (LLM 체화 에이전트 안전 계획 벤치마크) | 평가 프로그램 | SafeAgentBench 저자(shengyin1224 공식 저장소) | 23, 25, 27 | ref-749 | https://github.com/shengyin1224/SafeAgentBench |

## 추가 조사 요청

- q5-03(가설 1~3 판정): 단계 1~4 결과로 가설을 판정할 근거 정리가 필요하다(단계 5 완료 조건의 가설 판정표).
- 단계 5 완료 조건의 '사용자에게 제안하는 실험 계획': 가상 현장 시험(네 층)을 실험 계획 E5-xx 로 옮길 때 필요한 공개 창고 레이아웃·지시 시나리오 자료가 필요하다.
- 트랙 정의 current_stage(1), 트랙 개요 상태 줄(단계 3), 이번 지정 단계(5)가 서로 다르다. 트랙 데이터 확인이 필요하다(검증 노트 지적).
- 아이디어 2 페이지 끝의 기존 [^ref-111] 정의 줄에는 이번 실행 기준 원문 미열람 표시가 없다. 이번 패치는 아이디어 페이지에서 ref-111 을 인용하지 않았으며, 기존 줄 정비는 다음 갱신에서 판단한다.
- 백로그 중복 등록 정리(q3-09·q3-10, q3-12·q3-13, q4-09·q4-10, q1-05·q1-06)가 필요하다(브리프 참고).

## 이행한 수정 지시

- f7 강등 — 단계 5 페이지 3절 교란 층과 아이디어 6절에서 ARIAC 문장을 [추정]으로 쓰고 '컨베이어·전압 시험기 고장·고우선순위 주문은 START_TIME, 진공 도구 고장은 GRASP_OCCURRENCE' 로 고쳤다.
- f18·f24 교란 층 표현 — 네 층 표·설명용 시나리오·아이디어 6절에서 '시작 시각 또는 발생 조건을 정한 교란 주입'으로 쓰고, 교란 주입 첫 등장 시 용어집 장애 주입(Fault Injection) 페이지를 링크했다.
- f3 — 월드 목록의 '병원'을 README 표기대로 '클리닉(Clinic World)'으로 고쳤다.
- f4 — 'README 가 VDA 5050 3.0.0 준수를 표명하는(저장소 자기 표명, 적합성 시험 결과 미확인)'으로 쓰고, 개인 저장소·README 에 작성자·소속 없음을 4절 불확실성에 적었다.
- f12·f13 — 출처 충돌로 쓰지 않고 69%·5%(가장 나은 기준 에이전트)와 10%(가장 안전 의식이 높은 기준 에이전트, 세부 위험 과제)를 별개 지표로 함께 제시했다(저자 보고, 가정 환경).
- SafeAgentBench 거부율 출처 충돌 열린 질문은 open_question_updates 에 등록하지 않았다.
- f21 — '출처 충돌이라 수치 없이'라는 전제를 빼고 5%·10% 를 각각의 조건과 함께 참조했으며 문장은 [추정]을 유지했다.
- f9 — 'arXiv 2601.17087(2026-01), 게재처 미확인(ICLR 2026·ACL 2026 목록이 모두 검색됨)'으로 쓰고 수치에 '(저자 보고, 원문 미열람)'을 병기했다(각주 기관 표기도 게재처 미확인으로 고침).
- f10 — 'arXiv 2510.20808(2025-10), Annual Review of Control, Robotics, and Autonomous Systems 2026 게재, 권 미확인'으로 본문·각주·참고문헌 요약을 고쳤다.
- f15 — '(저자 보고, 원문 미열람)'을 병기하고 Eval4NLP 2025 게재판 제목을 각주와 4절 불확실성에 적었으며 수치는 arXiv 판 기준임을 밝혔다.
- f16 — 근거를 'arXiv 2604.05427 초록 검색 요약 기준'으로 고치고 230개 과제·시나리오 30개·실기 실험은 유지, 실기 규모 미확인을 적었으며 기존 각주 ref-417 을 재사용했다.
- f17 — 본문에서 '[추정] 벤더 주장'과 '챗봇 지시 시험에 쓴 사례 아님'을 유지하고, 22. 시뮬레이션·예측용 디지털 트윈 반영 제안 문안에도 벤더 주장 표기를 넣었다.
- f14·f19 — RVSG 와 시험 경계 서술에서 로봇 쪽 주행·회피·파지 시험을 '연계 대상:'으로 표시하고 ROP 쪽 시험을 지시 해석·배정·일정·예외 처리 결정에 한정했다.
- f22 — 가상 현장 시험은 22. 시뮬레이션·예측용 디지털 트윈과 23. 시험·형식 검증·벤치마크의 기능, 초기 상태는 8. 실시간 세계 상태·데이터 일관성의 스냅숏이나 고정 시험 상태로 쓰되 결과를 현재 상태에 반영하지 않는 구분을 그대로 옮겼다.
- f23 — 비교 설계는 q5-01 답(#q5-01)으로 연결해 반복하지 않고 같은 지시 흐름·교란 재생과 창고 레이아웃 자체 구축 필요만 더했으며, 창고 실측 비교 부재는 oq-052 로 연결했다(새 질문 미등록).
- 국내 디지털 트윈 사전 검증 대 시운전 비교 질문을 '(관련 기존 질문: oq-094)'를 붙여 open_question_updates 에 new 로 등록했다.
- 각주 — 단계 5 페이지 8절을 다시 써 ref-111·ref-417·ref-623·ref-741·ref-743·ref-744·ref-747·ref-748·ref-750·ref-751 에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었으며, github_raw 로 연 ref-406·ref-104·ref-528·ref-742·ref-407·ref-746·ref-749 는 표시 없이, ref-031 은 기존 각주 줄을 그대로 썼다.
- ref-528 — 각주·참고문헌의 기관을 'NIST (usnistgov/ARIAC_docs)'로 두고 제목에 ref-008 ARIAC 문서와 같은 문서 사이트의 challenges 페이지임을 밝혔다(별도 id 유지).
- 단계 5 페이지 2절 — q5-02 를 답함(2026-09-25-99, #q5-02)으로 바꾸고 3절에 '### q5-02 … {#q5-02}' 소제목을 신설했으며, q5-13·q5-14·q5-15 를 2절·5절 표에 열림으로 넣었다(제기 근거 f23·f20·f15, 실행 2026-09-25-99).
- 단계 5 페이지 4절 — 네 층 구성이 이 위키의 종합이며 근거가 소매·항공 대화, 가상 AGV, 호텔·클리닉·제조 데모, 제조 키팅 조건이라 물류 지시 조건이 아님, 교차 확인 0건, vda5050-sim 은 개인 저장소 자기 표명임을 남은 불확실성에 적었다.
- 단계 5 페이지 6절 — 세 행을 '미충족 · 미승인'으로, 첫 행 근거를 지시 문구대로 쓰고, 전환 줄을 '아니오(가설 판정표 q5-03·실험 계획 미작성, 막힌 질문 q5-03~q5-05·q5-07~q5-15 열림, 앞 단계 3·4 완료 미승인)'로 썼다. stage_transition 은 넣지 않았고 트랙 개요의 현재 단계 표기는 고치지 않았다.
- 아이디어 2 6절 — '검증 절차: 가상 현장·가상 로봇 시나리오 시험' 소절을 신설해 f18~f21 을 [추정]으로 싣고 근거 f1·f2·f4·f7(강등 반영)·f8·f9·f10·f15 를 두었으며, 평가 지표 소절과 링크로 잇고 가설 판정·실험 계획이 미조사임을 적었다. 도식은 Mermaid 로 직접 그렸다.
- 세부영역 반영 제안 — 23·22·13 페이지는 고치지 않고 area_reflection_proposals 와 트랙 로그 '세부영역 반영 제안'으로만 냈으며, 모의 사용자·LLM 비결정성(f8·f9·f15·f20)은 27. AI·학습·적응과 모델 운영 연결로도 명시하고 f7 은 [추정]으로 적었다.
- 용어 — 현실 격차·사용자 시뮬레이터·pass^k 지표를 glossary_updates 에 new 로 내고 설명에 디지털 트윈·장애 주입·회귀 시험과의 연결을 적었다.
- 2차: 단계 5 페이지 상태 줄 — H1 아래 줄을 '열린 질문: 12건 · 답한 질문: 2건'으로 고쳤고, 이 줄은 절 패치로 보낼 수 없어 단계 5 페이지를 patches 대신 전체 content 로 보냈다.
- 2차: 트랙 개요 6절 — docs/tracks/nl-task-chatbot/index.md 를 pages 에 넣어 '6. 살아있는 산출물 링크' 절만 replace 패치로 고쳤다. 아이디어 2 항목의 q5-02 미조사 문장을 지시 문구(검증 절차 소절 추가, 가설 판정 q5-03 미조사)로 바꾸고, 지정 질문으로 뒤 단계를 다룬 실행에 2026-09-25-99 를 더했으며, 초안 변경 없음 실행 목록에 2026-09-25-99 를 더했다. 현재 단계 표기(단계 3)와 H1 아래 상태 줄은 두었다.
- 2차: SafeAgentBench 문장 — 단계 5 페이지 q5-02 '위험 지시 시험과 시나리오 생성' 둘째 항목 첫 문장을 '공식 README 는 가장 나은 기준 에이전트의 안전 과제 성공률 69%·위험 과제 거부율 5%를 적고, 논문 초록은 이와 함께 가장 안전 의식이 높은 기준 에이전트의 세부(detailed) 위험 과제 거부율 10%를 적는다'로 바꿨고 태그 [사실]과 각주 ref-749·ref-748 은 유지했다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md
- 온톨로지 초안 버전: 0.8
- 트랙 로그 항목: 답한 질문: q5-02(가상 현장·가상 로봇으로 지시 시나리오를 시험하는 방법과 한계; f1~f25, f7 사실 → 추정 강등) / 새 질문: q5-13(f23), q5-14(f20), q5-15(f15) / 온톨로지 변경: 없음(업무 분해·배정 설계 초안 v0.8 유지 — 가상 현장 시험 절차는 작업 모델의 개념·관계가 아니라 검증 방법) / 완료 조건 평가: 미충족(부족: 가설 판정표 q5-03, 사용자에게 제안하는 실험 계획; 검증 절차는 추정 중심으로 처음 실림; 앞 단계 3·4 완료 미승인) / 세부영역 반영 제안: 23. 시험·형식 검증·벤치마크, 22. 시뮬레이션·예측용 디지털 트윈, 13. 작업 배정 — MRTA, 27. AI·학습·적응과 모델 운영 4건(모두 6. 대표 접근법과 기술; f7 은 [추정], f17 은 [추정] 벤더 주장) / 다음 실행 제안: q5-03(가설 판정), 이어서 실험 계획 제안, 또는 트랙 현재 단계 3 의 열린 질문(q3-05~q3-15)
- 개요 진행 현황: 단계 5 진행 중(트랙 현재 단계는 단계 3 유지) — 열린 질문 12, 답함 2, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q5-02 | 답함 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-02 | — | — | — |
| q5-13 | 열림 | — | 가상 현장 시험에 쓸 창고 레이아웃(피킹 구역·도크·승강기·충전기)과 지시 시나리오 집합(정상·교란·위험·권한 밖 지시)을 q5-04 의 지시–정답 쌍과 어떻게 묶어 구성하고, 시나리오 수와 교란 조합의 범위를 어떤 기준으로 정하는가? (q5-02 에서 파생) | 5 | f23 |
| q5-14 | 열림 | — | LLM 모의 관리자로 얻은 챗봇 성과를 실제 관제 요원·현장 관리자 소수 표본의 시험으로 보정하려면 표본 규모와 비교 지표(성공률, 되묻기 횟수, 오배정)를 어떻게 정하는가? (q5-02 에서 파생) (관련: q5-10) | 5 | f20 |
| q5-15 | 열림 | — | LLM 비결정성을 고려해 모델·프롬프트 변경 뒤 회귀 시험에서 같은 시나리오를 몇 번 반복하고(pass^k 의 k), 어떤 분포 차이를 합격·불합격 기준으로 삼는가? (q5-02 에서 파생) | 5 | f15 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 23 | 6. 대표 접근법과 기술 | 지시 시나리오 시험의 네 층 구성(추정): 표준 인터페이스 가상 로봇(vda5050-sim, 자기 표명·직선 운동학)과 시작 시각 또는 발생 조건을 정한 장애 주입(ARIAC, [추정]), LLM 모의 사용자 대화와 끝 상태 채점·pass^k(τ-bench), 모의 사용자의 체계적 보정 오차(Lost in Simulation), 위험 지시 시험(SafeAgentBench 5%·10% 별개 지표), 시나리오 생성 시험(RVSG, 로봇 쪽은 연계 대상), LLM 비결정성에 따른 반복 시행(Atil 외). 교차 규칙에 따라 모의 사용자·비결정성은 27. AI·학습·적응과 모델 운영과 연결. |
| 22 | 6. 대표 접근법과 기술 | Open-RMF 다중 플릿 시뮬레이션의 모사 범위(문·승강기·워크셀·군중)와 slotcar 의 장애물 없는 경로 가정, 창고 전용 데모 월드 부재, 현실 격차 리뷰(Aljalbout 외, 권 미확인), 국내 관제 디지털 트윈 xDT([추정] 벤더 주장, 챗봇 지시 시험 사례 아님). 지시 시나리오 재현은 가정한 미래 실험이며 초기 상태는 8. 실시간 세계 상태·데이터 일관성의 스냅숏에서 받되 결과를 현재 상태에 반영하지 않는 구분. |
| 13 | 6. 대표 접근법과 기술 | 가상 현장에서 같은 지시 흐름과 같은 교란을 최근접 배정 기준선과 ROP 배정(해법기 기반)에 똑같이 재생해 총 이동 지연·납기 지연을 비교하는 설계(추정). 공개 데모에 창고 레이아웃이 없어 자체 구축 필요, 창고 실측 비교 부재는 oq-052. 27. AI·학습·적응과 모델 운영과 양쪽 연결. |
| 27 | 6. 대표 접근법과 기술 | LLM 기반 챗봇 평가 방법: LLM 모의 사용자와 끝 상태 채점·pass^k(τ-bench), 모의 사용자가 실제 사용자 성과를 체계적으로 틀리게 추정한다는 보고(Lost in Simulation, 게재처 미확인), 결정적 설정에서도 LLM 정확도가 반복 실행마다 달라진다는 보고(Atil 외, arXiv 판 기준). 모의 관리자 결과의 실제 표본 보정과 반복 분포 보고는 추정. 적용 대상 13. 작업 배정 — MRTA·23. 시험·형식 검증·벤치마크와 연결. |
