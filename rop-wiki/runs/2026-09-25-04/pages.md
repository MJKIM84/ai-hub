# 스토리텔러 산출 2026-09-25-04

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md | draft | q1-01 답함(분해 접근 여섯 유형·접근별 내용·사람에게 남는 일), 후속 질문 q1-05, 완료 조건 미충족, 출처 17건(2차 재실행에서 내용 변경 없음) |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | 초안 v0 → v0.1: 개념 로봇 팀(Coalition) 확정 추가(f9), 거부된 제안 3건을 6절 미해결 모델링 질문으로(2차: 6절 일곱 접근 범위 한정, Lang2LTL 서술 수정, PDDL·LTL 풀어쓰기) |
| update | docs/ideas/nl-task-chatbot.md | draft | 3절 선행 연구 쪽 작성(분해 결과 형태 여섯 유형, 사람에게 남는 일, 물류 적용 한계), 제품 사례 미조사 명시(2차: 표의 PDDL·LTL 풀어쓰기, 둘째·셋째 항목에 '이 위키의 정리' 표시) |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 상태 줄 마지막 트랙 실행 2026-09-25, 6절 초안 버전 v0.1 반영(2차 재실행에서 내용 변경 없음) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 1 | q1-01 답함(자연어 지시 분해 접근 여섯 유형), 후속 질문 q1-05, 업무 분해·배정 설계 초안 v0.1(로봇 팀 추가) | run 2026-09-25-04
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 1: 자연어 지시를 작업으로 분해하는 기존 접근을 여섯 유형으로 정리(q1-01 답함), 업무 분해·배정 설계 초안 v0.1
- 대분류 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 자연어 업무 지시 챗봇 트랙이 LLM 기반 분해·팀 구성·할당 연구(SMART-LLM, DART-LLM)를 반영 제안
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 작업 분해 | Task Decomposition | 상위 지시나 목표를 로봇이 실행할 수 있는 하위 작업·동작의 순서나 구조로 나누는 일이다. | 13, 14, 2, 27 | ref-066, ref-062 |
| new | 행동 트리 | Behavior Tree | 로봇 동작과 조건 확인을 트리 노드로 조합해 실행 구조를 표현하는 형식이다. | 12, 27, 13 | ref-061 |
| new | 선형 시간 논리 | Linear Temporal Logic (LTL) | 작업의 순서·시간 제약을 명확한 의미로 기술하는 형식 논리이다. | 27, 23, 13 | ref-055, ref-056 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-069 | Google Research | SayCan (google-research/saycan README) | 오픈소스 문서 | high | https://github.com/google-research/google-research/blob/master/saycan/README.md |
| ref-070 | Ahn, M. 외(Google) | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 논문 | medium | https://arxiv.org/abs/2204.01691 |
| ref-053 | NVIDIA Research (NVlabs) | progprompt-vh — ProgPrompt: Generating Situated Robot Task Plans using Large Language Models (GitHub README) | 오픈소스 문서 | high | https://github.com/NVlabs/progprompt-vh |
| ref-054 | Singh, I. 외 | ProgPrompt: Generating Situated Robot Task Plans using Large Language Models | 논문 | medium | https://arxiv.org/abs/2209.11302 |
| ref-055 | Brown University H2R Lab | Lang2LTL — Code for paper Lang2LTL: Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments (GitHub README) | 오픈소스 문서 | high | https://github.com/h2r/Lang2LTL |
| ref-056 | Liu, J. X. 외 | Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments | 논문 | medium | https://arxiv.org/abs/2302.11649 |
| ref-057 | Tellex, S. 외 | Understanding Natural Language Commands for Robotic Navigation and Mobile Manipulation | 논문 | medium | https://ojs.aaai.org/index.php/AAAI/article/view/7979 |
| ref-058 | Cohen, V., Liu, J. X., Mooney, R., Tellex, S., & Watkins, D. | A Survey of Robotic Language Grounding: Tradeoffs between Symbols and Embeddings | 논문 | medium | https://www.ijcai.org/proceedings/2024/885 |
| ref-059 | Wang, Y. 외(DART-LLM 저자) | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 논문 | medium | https://arxiv.org/abs/2411.09022 |
| ref-061 | Izzo, R. A., Bardaro, G., & Matteucci, M. (Politecnico di Milano AIRLab) | BTGenBot: Behavior Tree Generation for Robotic Tasks with Lightweight LLMs | 논문 | medium | https://arxiv.org/abs/2403.12761 |
| ref-062 | SMARTlab-Purdue (Purdue University) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (GitHub README) | 오픈소스 문서 | high | https://github.com/SMARTlab-Purdue/SMART-LLM |
| ref-063 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 논문 | medium | https://arxiv.org/abs/2309.10062 |
| ref-064 | Cranial-XIX (LLM+P 저자) | llm-pddl — LLM+P: Empowering Large Language Models with Optimal Planning Proficiency (GitHub README) | 오픈소스 문서 | high | https://github.com/Cranial-XIX/llm-pddl |
| ref-065 | Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P. | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 논문 | medium | https://arxiv.org/abs/2304.11477 |
| ref-066 | Huang, W., Abbeel, P., Pathak, D., & Mordatch, I. | Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents | 논문 | medium | https://proceedings.mlr.press/v162/huang22a.html |
| ref-067 | Huang, W. (language-planner 공식 저장소) | language-planner — Official Code for "Language Models as Zero-Shot Planners" (GitHub README) | 오픈소스 문서 | high | https://github.com/huangwl18/language-planner |
| ref-068 | Google Research | Code as Policies: Language Model Programs for Embodied Control (google-research/code_as_policies README) | 오픈소스 문서 | high | https://github.com/google-research/google-research/blob/master/code_as_policies/README.md |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 단계 1 q1-02·q1-03: LLM 을 로봇 작업 계획·배정에 쓴 제품 사례와 채팅·음성 지시 운영 인터페이스 제품의 확인·승인 방식 — 아이디어 2 3절 제품 사례와 단계 1 완료 조건에 필요
- 단계 1 q1-04: 자연어 지시에서 장소·화물·긴급도·기한을 뽑고 빠진 정보를 되묻는 방법 — 단계 1 남은 시작 질문
- 단계 1 q1-05: 물류·창고 현장 지시를 다룬 LLM 작업 분해 연구(예: 검색에 제목만 보인 산업 다중 로봇 연구의 내용 확인) — 물류 적용 한계 판단에 필요
- 국내(한국) 연구기관·학회의 자연어 지시 작업 분해 연구 — 한국 자료 우선 규칙
- SMART-LLM 논문 본문의 할당 방식(최적화 사용 여부) 원문 확인 — 13. 작업 배정 — MRTA 반영 제안의 근거 보강
- 각 접근(SayCan, LLM+P, Lang2LTL 등)의 독립 출처 교차 확인 — 현재 논문과 README 가 같은 저자 계열이라 교차 확인 0건
- next_ref_id 산정 오류(브리프 ref-044~ref-052 가 기존 참고문헌과 충돌) 확인 — pipeline 담당 요청. 1차 검증은 ref-051·ref-052 충돌을 놓쳐 퍼블리셔 사전 검사에서 ref-069·ref-070 으로 추가 재부여했다

## 이행한 수정 지시

- 참고문헌 id 재부여 — ref-044→ref-062, ref-045→ref-063, ref-046→ref-064, ref-047→ref-065, ref-048→ref-066, ref-049→ref-067, ref-050→ref-068 로 모든 페이지 각주·프런트매터 sources·reference_updates 에 일관되게 적용했다.
- f4 근거 — ProgPrompt 설명의 각주를 ref-054(원문 미열람)로 하고 ref-053 은 공식 코드 저장소 공개 사실에만 달았으며, f13·f14 의 ProgPrompt 근거도 ref-054 로 적었다.
- f14 범위 한정 — 단계 1 3절·아이디어 3절에서 'Huang 외, SayCan, ProgPrompt, Code as Policies, LLM+P, Lang2LTL, SMART-LLM 일곱 접근은'으로 한정해 [추정]으로 썼다.
- f16 한정 — '공식 저장소 README 기준으로 확인되지 않으며 논문 본문의 할당 세부는 미확인이다'로 고쳐 [추정]으로 썼다.
- f13·f14·f15·f17 — 모두 '이 위키의 정리(추론)'임을 밝히고 [추정] 유지, f15 에 '이번 검색 범위, 부재의 확인은 아님'을 남기고 IMR-LLM 은 본문에 쓰지 않았다.
- f12 — [의견] 태그를 유지하고 '서베이 저자들(Cohen 외, IJCAI-24)의 평가'로 밝혔다.
- f3·f7·f8 수치 — 101개 과업·약 두 배, 21개 환경·52개 명령, 9개 과업을 본문에서 뺐고 f8 은 '70억 파라미터 이하'만 썼다.
- f5 기준일 — Code as Policies 문장에 '확인일 2026-09-25 기준 공식 README'로 적었다.
- f1 흐름 — flow_matrix_updates 를 빈 배열로 두어 출하·시작 조건 칸을 넣지 않았다.
- 원문 미열람 표시 — 논문 출처(ref-054, 056, 057, 058, 059, 061, 063, 065, 066, 070) 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, README 7건(ref-053, 055, 062, 064, 067, 068, 069)은 미열람 표시를 하지 않았다.
- 직접 인용 — 모든 출처를 재서술만 했고 ref-058 을 포함해 직접 인용을 두지 않았다.
- 용어 — PDDL 을 '계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)'로 쓰고 glossary/pddl.md 에 링크했으며, 행동 트리·선형 시간 논리 정의를 지시 문구대로 줄여 glossary_updates 에 냈다.
- 온톨로지 변경 — 로봇 팀(Coalition)만 2절에 '확정'으로 추가하고 H1·프런트매터 ontology_version·track_updates.ontology_draft_version 을 0.1 로 맞췄으며(상태 표식은 auto 영역이라 퍼블리셔 갱신), 허용 동작 목록·형식 작업 명세·선행 의존 관계는 6절 미해결 모델링 질문으로 두었다.
- q2-02 중복 질문 — backlog_updates 에 넣지 않고 단계 1 5절에 중복으로 제외했다고만 적었다.
- q4-02 중복 질문 — backlog_updates 에 넣지 않았다.
- q1-05 — 지시한 문장으로 줄여 단계 1 질문(근거 f15)으로 백로그와 단계 1 2절·5절에 등록했다.
- 단계 1 페이지 — q1-01 답함(#q1-01, 소제목 {#q1-01}), 6절 두 조건 '미충족', 검증 판정 '미충족 · 미승인', 전환 줄을 지시 문구대로 썼고 트랙 개요 상태 줄을 '현재 단계: 단계 1. 선행 연구·제품 사례 조사 · 마지막 트랙 실행: 2026-09-25'로 고쳤다.
- 아이디어 2 3절 — 선행 연구 쪽만 쓰고 제품 사례(q1-02·q1-03)는 아직 조사되지 않았음을 절 머리와 '제품 사례' 소제목에 밝혔다.
- 세부영역 반영 — 13. 작업 배정 — MRTA·27. AI·학습·적응과 모델 운영 페이지는 고치지 않고 area_reflection_proposals 로만 냈고, 27 제안에 13 과의 양쪽 연결을 밝혔으며 가치 함수·제어 기본 동작·객체 검출은 접지 방식 설명으로만 쓰고 센서 인식·파지·모터 제어는 연계 대상으로 짧게 두었다.
- 형식 검증: 퍼블리셔 사전 검사가 지적한 참고문헌 id 충돌을 고쳤다 — ref-051(SayCan README)→ref-069, ref-052(SayCan 논문)→ref-070 으로 단계 1 페이지·아이디어 2 3절 패치의 각주·각주 정의·프런트매터 sources, reference_updates, area_reflection_proposals 에 일관되게 적용했다. 주장·태그·판정은 바꾸지 않았다.
- 2차: 업무 분해·배정 설계 초안 6절 '허용 동작 목록' 항목 — 'Huang 외, SayCan, ProgPrompt, Code as Policies, LLM+P, Lang2LTL, SMART-LLM 일곱 접근은 사람이 미리 정한 허용 동작·가용 동작·기술 목록 안에서 분해하는 것으로 보인다(이 위키의 정리)'로 범위를 한정하고 [추정]을 유지했다.
- 2차: 업무 분해·배정 설계 초안 6절 첫 항목 — '조사한 일곱 LLM 기반 접근에서는 실행 단위를 사람이 미리 정해 둔다는 정리가 나왔다'로 한정했다.
- 2차: 업무 분해·배정 설계 초안 6절 '형식 작업 명세' 항목 — 'LLM+P는 자연어 문제를 PDDL 문제 파일로 바꿔 고전 계획기에 넘기고, Lang2LTL은 명령을 LTL 식으로 옮긴다. [사실]'로 고쳤고, PDDL 은 '[계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)](../../glossary/pddl.md)', LTL 은 '선형 시간 논리(Linear Temporal Logic, LTL)'로 풀어 썼다.
- 2차: 아이디어 2 3절 표 — '[계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)](../glossary/pddl.md) 문제 파일, 선형 시간 논리(Linear Temporal Logic, LTL) 식'으로 고쳤다.
- 2차: 아이디어 2 3절 '무엇을 자동화하고 무엇을 사람에게 남기는가'의 둘째 항목(형식 명세 경유 구조)과 셋째 항목(평가 환경) 끝 태그 앞에 '(이 위키의 정리)'를 붙였다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md
- 온톨로지 초안 버전: 0.1
- 트랙 로그 항목: 답한 질문: q1-01(f1~f17) / 새 질문: q1-05(f15); 중복 2건(q2-02, q4-02와 겹침) 제외 / 온톨로지 변경: v0 → v0.1: 개념 '로봇 팀 (Coalition)' 추가(f9, 실행 2026-09-25-04). 거부 3건(허용 동작 목록, 형식 작업 명세, 작업 / 선행 의존한다 / 작업)은 6절 미해결 모델링 질문으로 / 완료 조건 평가: 미충족(부족: 제품 사례 미조사로 아이디어 2 3절 비교 미완, 지시 분해 유형 목록 초안 미반영) / 세부영역 반영 제안: 13. 작업 배정 — MRTA 2건, 27. AI·학습·적응과 모델 운영 2건 / 다음 실행 제안: q1-02, q1-03
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 4, 답함 1, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-01 | 답함 | docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md#q1-01 | — | — | — |
| q1-05 | 열림 | — | 물류·창고 현장 지시를 다룬 LLM 작업 분해 연구가 있는가, 가정용 시뮬레이터 결과를 물류 지시로 옮길 때 무엇이 달라지는가? | 1 | f15 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 6. 대표 접근법과 기술 | 학습 기반 배차의 한 갈래로 LLM 기반 분해·팀 구성·할당 파이프라인을 소개: SMART-LLM(분해→팀 구성→할당을 프로그램형 few-shot 프롬프트로 수행, 할당 최적화는 README 기준 미확인 [추정]), DART-LLM(하위 작업 의존 DAG와 배정 모듈). 27. AI·학습·적응과 모델 운영과 양쪽 연결. 근거 ref-062, ref-063, ref-059. |
| 13 | 8. 대표 연구와 자료 | SMART-LLM(Kannan 외 2023, 공식 README와 논문, 4개 난이도 범주 벤치마크), DART-LLM(2024 프리프린트)을 대표 연구로 등록. 근거 ref-062, ref-063, ref-059. |
| 27 | 6. 대표 접근법과 기술 | LLM 출력을 실행 전에 접지·점검하는 방법: 기술 가치 함수(SayCan), 고전 계획기에 PDDL 넘김(LLM+P), LTL 식 변환(Lang2LTL). 형식 명세 경유 구조가 오해석 방지와 이어진다는 [추정]. 적용 대상 13. 작업 배정 — MRTA와 양쪽 연결(교차 규칙: 학습 기반 배차). 센서 인식·제어는 연계 대상. 근거 ref-069, ref-070, ref-064, ref-065, ref-055, ref-056. |
| 27 | 8. 대표 연구와 자료 | Cohen 외(IJCAI-24) 로봇 언어 접지 서베이(형식 표현–임베딩 스펙트럼, 장단점 평가는 [의견])와 Huang 외(ICML 2022), SayCan, LLM+P, Lang2LTL을 대표 자료로 등록하고 13. 작업 배정 — MRTA 페이지와 연결. 근거 ref-058, ref-066, ref-069, ref-064, ref-055. |
