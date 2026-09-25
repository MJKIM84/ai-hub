# 스토리텔러 산출 2026-09-25-85

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md | draft | q4-04 답함(되묻기·사람 승인·실행 보류 전환 기준, 신뢰도 low), 후속 질문 q4-19, 4·6·8·9절 갱신 |
| update | docs/ideas/nl-task-chatbot.md | draft | 5절에 '제한 운영으로 넘기는 기준' 소절 추가(q4-04, 신뢰도 low) |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | 6절 '사용자 확인' 질문에 q4-04 답 연결(초안 v0.9 유지, 온톨로지 변경 없음) |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6절에 실행 2026-09-25-85(q4-04 답, 초안 v0.9 유지) 한 줄 추가 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 4 | q4-04 답함(되묻기·사람 승인·실행 보류 전환 기준, 신뢰도 low), 후속 질문 q4-19, 아이디어 2 5절 소절 추가, 초안 v0.9 유지 | run 2026-09-25-85
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 4. 오해석 방지와 확인 절차: q4-04 답함(제한 운영으로 넘기는 되묻기·사람 승인·실행 보류 기준, 이 위키의 종합, 신뢰도 low)
- 대분류 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA(자연어 업무 지시 챗봇 트랙): 되묻기·승인·보류 중 배정을 확정하지 않고 해소 시점 상태로 배정하는 분담을 반영 제안
- 세부영역 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 트랙 자연어 업무 지시 챗봇 q4-04 에서 제한 운영 중 배정 시점 분담을 6. 대표 접근법과 기술에 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 완전 정보의 기대 가치 | Expected Value of Perfect Information (EVPI) | 불확실한 값을 정확히 알게 될 때 기대되는 결정 결과의 개선량으로, 되물을 질문을 고를 때 질문 비용과 비교하는 기준으로 쓰인다. | 27, 18 | ref-664 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-350 | Ren, A. Z. 외(Google DeepMind·Princeton University, KnowNo 프로젝트) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners — project page (robot-help.github.io) | 오픈소스 문서 | medium | https://robot-help.github.io/ |
| ref-352 | Park, J. 외(고려대학교·연세대학교·Google Research, CLARA 프로젝트) | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents — project page (clararobot.github.io) | 오픈소스 문서 | medium | https://clararobot.github.io/ |
| ref-353 | Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S. | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents | 논문 | medium | https://arxiv.org/abs/2306.10376 |
| ref-355 | Ivanova, A. 외(AmbiK 저자, dblp 기록 기준) | AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment | 논문 | medium | https://aclanthology.org/2025.acl-long.1593/ |
| ref-356 | Rasa Technologies (RasaHQ/rasa GitHub) | Forms — Rasa documentation (docs/docs/forms.mdx) | 오픈소스 문서 | medium | https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx |
| ref-658 | Rasa Technologies (RasaHQ/rasa GitHub) | Fallback and Human Handoff — Rasa documentation (docs/docs/fallback-handoff.mdx) | 오픈소스 문서 | medium | https://github.com/RasaHQ/rasa/blob/main/docs/docs/fallback-handoff.mdx |
| ref-663 | Liang, K. 외(Introspective Planning 저자) | Introspective Planning: Aligning Robots' Uncertainty with Inherent Task Ambiguity | 논문 | medium | https://arxiv.org/abs/2402.06529 |
| ref-664 | Suri, M. 외(University of Maryland·Adobe Research) | Structured Uncertainty guided Clarification for LLM Agents | 논문 | medium | https://arxiv.org/abs/2511.08798 |
| ref-695 | OWASP Top 10 for LLM Applications 프로젝트 (OWASP GitHub) | LLM06:2025 Excessive Agency (2_0_vulns/LLM06_ExcessiveAgency.md) | 오픈소스 문서 | medium | https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md |
| ref-696 | Model Context Protocol (modelcontextprotocol GitHub) | Specification 2025-06-18 — Server Features: Tools (docs/specification/2025-06-18/server/tools.mdx) | 표준 | medium | https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/server/tools.mdx |
| ref-697 | LangChain (langchain-ai/docs GitHub) | Human-in-the-loop — LangChain docs (src/oss/langchain/human-in-the-loop.mdx) | 오픈소스 문서 | medium | https://docs.langchain.com/oss/python/langchain/human-in-the-loop |
| ref-713 | He, G., Demartini, G., & Gadiraju, U. | Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents As A Daily Assistant | 논문 | medium | https://dl.acm.org/doi/10.1145/3706598.3713218 |
| ref-714 | arXiv 2604.04918 저자(미확인) | Comparing Human Oversight Strategies for Computer-Use Agents | 논문 | medium | https://arxiv.org/abs/2604.04918 |
| ref-715 | Future of Life Institute (artificialintelligenceact.eu, EU 규정 2024/1689 조문 게재본) | Article 14: Human Oversight \| EU Artificial Intelligence Act | 정부·연구기관 | medium | https://artificialintelligenceact.eu/article/14/ |
| ref-717 | Sagawa, H., Mitamura, T., & Nyberg, E. (INTERSPEECH 2004-ICSLP) | A comparison of confirmation styles for error handling in a speech dialog system | 논문 | medium | https://www.isca-archive.org/interspeech_2004/sagawa04_interspeech.pdf |
| ref-620 | 국가법령정보센터(과학기술정보통신부) | 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 | 정부·연구기관 | medium | https://www.law.go.kr/lsInfoP.do?lsiSeq=268543 |
| ref-656 | Open Robotics (open-rmf) | rmf_ros2 — rmf_task_ros2/src/rmf_task_ros2/Dispatcher.cpp | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/src/rmf_task_ros2/Dispatcher.cpp |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-04 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 작업 대상 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-04 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 수행 자원 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-04 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 제약 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-04 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 예외·성과 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-04 | 단계 4. 오해석 방지와 확인 절차 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- pipeline 담당: 단계 4 페이지 H1 아래 상태 줄('> 단계 상태: … · 답한 질문: n건 …')은 H2 절 밖이라 patches 로 고칠 수 없다. 이번 실행으로 답한 질문이 3건에서 4건으로 바뀌었으므로(열린 질문 15건, 진행 중, 미충족은 그대로) 퍼블리셔가 백로그에서 이 줄을 다시 쓰거나 H2 앞 머리 영역에 대한 패치를 허용하도록 요청한다.
- 물류 창고 로봇 채팅 지시에서 되묻기·사람 승인·실행 보류로 넘기는 기준을 평가한 연구·국내 사례(단계 4 페이지 q4-04 절과 18. 사람–로봇 협업·운영 인터페이스 6절에 필요): 이번 실행은 신규 검색 0회라 물류 조건 근거가 없어 전환 기준이 이 위키의 종합(신뢰도 low)에 머문다.
- 보류 지연이 배정 품질·납기에 주는 영향을 잰 자료(q4-04 분류 원문 질문 연결과 13. 작업 배정 — MRTA 6절에 필요): 확인하지 못했다.
- Sagawa 외(2004)의 명시적·최종·암시적 확인 비교 결과의 우열·수치(q4-04 암시적 확인 경로의 근거로 필요): 원문 미열람으로 미확인이다.

## 이행한 수정 지시

- f22 수정 — 단계 4 페이지 q4-04 설명용 시나리오의 제약 칸에서 '이미 화물을 실은 경우'를 배치 전 보류가 아니라 일시 정지·트리거 대기로 멈추는 경로(로봇 쪽 실행은 연계 대상)로 고치고, 풀어 준 베이스는 실행된 것으로 가정해야 한다는 근거를 함께 적었다.
- 범위 경계 문장 — q4-04 '실행 보류의 수단' 소절에 '로봇의 일시 정지·대기·재시도 실행은 분류 원문 9장 로봇 자체 지능·제어 경계의 연계 대상이며 ROP 는 보류 지시와 시간 초과 판단(취소·사람 인계)만 맡는다'를 [추정][^ref-031] 로 두었다.
- f11 INTERVENED — '관제는 주문·주문 갱신은 보낼 수 있으나 순간 동작은 cancelOrder 만 보낼 수 있다'로 순간 동작 한정을 유지해 썼다.
- 중복 방지 — f7·f8·f9·f12·f13·f14·f15·f16·f20 은 q4-04 절에서 한두 문장 요지만 두고 [q4-01 답](#q4-01)으로 연결했으며, 기존 각주 ref-695·696·697·713·714·715·620·717 을 재사용했다.
- f6 — Rasa 폴백 문장을 [사실]로 두고 '사람 인계는 기본 동작이 아니라 최종 폴백의 예시이며 채널별로 사용자가 구현한다'는 한정을 넣었다. 아이디어 페이지 5절의 기존 [추정] 문장은 고치지 않았고, 단계 4 페이지 9. 이력 행에 'ref-658 원문 확인으로 [사실] 유지' 메모를 남겼다.
- f4·f5·f12 — 수치·결과 뒤에 '저자 보고값, 원문 미열람'과 조건(도구 호출 / 주방 텍스트 작업 / 일상 비서 시뮬레이션)을 적었다.
- f14·f15 — f14 는 [추정]으로 두고 'EUR-Lex 원문 미확인·고위험 해당 여부 미확인'을, f15 는 '시행령 세부 미확인, 고영향 해당 여부는 oq-105'를 함께 적었다.
- f17·f18·f20·f21·f23 — 문장마다 '이 위키의 종합'과 물류 조건 근거가 없다는 점을 밝혔고 q4-04 답의 종합 신뢰도를 low 로 적었으며, 세 경로 전환 기준 표 아래에 '이 위키가 구성한 가설 표이며 출처의 표를 옮긴 것이 아니다'를 넣었다.
- f23 — 근거 공백 소절에 '이번 실행은 신규 검색 없이 기존 참고문헌만 재사용했고, 검색 범위 관찰은 이전 실행(2026-09-25-79·81·83) 기준'이라고 적었다.
- 각주 — 단계 4 페이지 8절에서 ref-031 을 뺀 이번 실행 출처의 각주 정의에 ' (원문 미열람)'을 달았다(ref-695·696·697 에 새로 추가, ref-352·353·355·658·663·664 는 새로 정의). reference_updates 에는 ref-031 만 source_unopened false 이고 나머지는 true 다.
- 중복 질문 — '불확실성 점수만으로 되묻기를 정하는 방식과 규칙을 함께 쓰는 방식의 비교' 질문은 q4-07·q5-08 과 겹쳐 backlog_updates 에 넣지 않았고, 단계 4 페이지 5절 표 아래에 중복으로 제외했다고 적었다.
- 새 질문 — 보류 시간 한계 질문을 q4-19 로 단계 4 에 등록했다(origin f19, 2·5절 표와 backlog_updates).
- task-model-draft.md — ontology_version 0.9 와 H1·버전 이력은 그대로 두고, 6절에 q4-04 답(f17·f19, 추정)을 '사용자 확인' 질문에 잇는 항목만 덧붙였다(ontology_draft_version '0.9').
- 단계 4 페이지 6절 — '제한 운영 기준' 행을 q4-04 답을 근거로 적고 충족 여부는 '미충족', 검증 판정은 '미충족 · 미승인'으로 두었다. 표 아래 줄은 '다음 단계로 전환: 아니오(완료 조건 반영이 추정 근거·검증 승인 전, 열린 질문 q4-05~q4-18)'로 썼다. 상태 줄은 H2 밖이라 패치가 닿지 않는다. 단계 상태 '진행 중'은 그대로이고, '답한 질문 3건→4건'은 퍼블리셔가 갱신하도록 additional_research_requests 에 요청했다(4. 결론·2절 표에서는 q4-04 가 답함으로 표시된다).
- 세부영역 반영 제안 — 13. 작업 배정 — MRTA, 18. 사람–로봇 협업·운영 인터페이스, 27. AI·학습·적응과 모델 운영 페이지는 직접 고치지 않고 area_reflection_proposals 로만 냈다. 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 적용 대상 영역을 양쪽에서 잇는다는 점도 적었다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md
- 온톨로지 초안 버전: 0.9
- 트랙 로그 항목: 답한 질문: q4-04(되묻기·사람 승인·실행 보류로 넘기는 기준, f1~f23, 이 위키의 종합, 신뢰도 low; 재실행 1회차, 신규 검색 0회) / 새 질문: q4-19(보류 시간 한계, f19). 불확실성 점수 대 규칙 병행 비교 질문은 q4-07·q5-08 과 중복이라 제외 / 온톨로지 변경: 없음(v0.9 유지, q4-04 답을 초안 6절 '사용자 확인' 질문에 연결) / 완료 조건 평가: 미충족(부족: 실행 전 검증 단계·명령 권한·제한 운영 기준 초안이 추정 근거이고 검증 승인 전; 열린 질문 q4-05~q4-19; q4-09·q4-10 중복 정리 필요) / 세부영역 반영 제안: 13. 작업 배정 — MRTA, 18. 사람–로봇 협업·운영 인터페이스, 27. AI·학습·적응과 모델 운영 3건 / 다음 실행 제안: q4-13(영향이 큰 작업 목록 기준) 또는 q4-19(보류 시간 한계)
- 개요 진행 현황: 단계 4 진행 중(지정 질문 실행, 현재 단계는 단계 3 유지) — 열린 질문 15, 답함 4, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q4-04 | 답함 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-04 | — | — | — |
| q4-19 | 열림 | — | 실행 보류로 넘긴 지시의 보류 시간 한계(승인자 무응답·되묻기 무응답)를 작업의 기한·출하 마감과 어떻게 연동하고, 한계를 넘으면 취소·사람 작업 전환·다른 승인자 인계 가운데 무엇으로 넘기는가? (q4-04 에서 파생) (관련: q4-11, q4-13) | 4 | f19 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 6. 대표 접근법과 기술 | 트랙 자연어 업무 지시 챗봇 q4-04(f19·f21, 추정): 해석 되묻기·사람 승인·실행 보류 동안에는 배정을 확정하지 않고, 해소 뒤 그 시점 로봇 상태로 배정을 계산하는 분담을 둔다. 실행 보류는 VDA 5050 베이스를 풀어 주기 전에 걸어야 한다. 분류 원문 질문(가장 가까운 로봇)과의 연결도 적는다. 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽에서 잇는다. |
| 18 | 6. 대표 접근법과 기술 | 트랙 자연어 업무 지시 챗봇 q4-04(f6·f9·f17·f20): Rasa 신뢰도 문턱 폴백과 두 단계 폴백(사람 인계는 최종 폴백의 예시), LangChain 승인·수정·거부 중단점을 적는다. 되묻기·사람 승인·실행 보류로 넘기는 기준과, 명시적 승인을 영향이 큰 작업으로 한정해 승인 피로를 줄이는 선택지(이 위키의 종합, 추정)를 함께 둔다. |
| 27 | 6. 대표 접근법과 기술 | 트랙 자연어 업무 지시 챗봇 q4-04(f1·f3·f4·f5·f18): 불확실성 기반 되묻기 기준(KnowNo 등각 예측, 내성적 계획, SAGE-Agent EVPI, 저자 보고값)과 AmbiK 모호성 탐지 한계를 적고, 불확실성 점수와 규칙 조건을 함께 쓰는 선택지(추정)를 둔다. 적용 대상인 13. 작업 배정 — MRTA와 18. 사람–로봇 협업·운영 인터페이스에 함께 연결한다. |
