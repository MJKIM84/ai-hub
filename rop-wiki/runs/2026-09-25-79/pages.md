# 스토리텔러 산출 2026-09-25-79

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md | draft | q4-01 답함(다섯 겹 확인 절차 가설, 신뢰도 low), 질문 표를 백로그 문구와 맞춤, 후속 질문 3건, 완료 조건 미충족·전환 아니오, 상태 줄 진행 중. 2차 수정: OWASP 발행일 표기 정정, 2절 표 백로그 일치(상태 줄이 H2 밖이라 전체 content 로 보냄) |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | 6절에 사용자 확인 질문의 q4-01 답 링크와 속성 후보를 질문으로 덧붙임(개념 추가 미반영, 초안 v0.8 유지). 2차 수정: MCP 풀어쓰기·용어집 링크, 사람 참여 루프 용어집 링크 |
| update | docs/ideas/nl-task-chatbot.md | draft | 5절에 '오해석 방지 확인 절차' 소절 추가(q4-01, 실행 2026-09-25-79), 머리 문장의 '확인 절차 미조사' 서술을 실행 기준과 함께 갱신, 명령 권한·제한 운영 기준 미조사 명시. 2차 수정: MCP 첫 등장 풀어쓰기·용어집 링크 |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6. 살아있는 산출물 링크 절 갱신: 실행 2026-09-25-79 에서 초안 v0.8 유지·개념 '사용자 확인' 제안은 6절 질문, 아이디어 2 5절에 '오해석 방지 확인 절차' 소절(q4-01) 추가. 상태 줄은 바꾸지 않음(단계 3 완료·전환 미승인) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 4 | q4-01 답함(다섯 겹 확인 절차 가설, 신뢰도 low), 후속 질문 3건, 초안 v0.8 유지(개념 '사용자 확인'은 6절 질문), 아이디어 2 5절에 오해석 방지 확인 절차 소절 추가, 트랙 개요 산출물 현황 갱신 | run 2026-09-25-79
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 4. 오해석 방지와 확인 절차: q4-01 답함(해석 게이트·제약 게이트·사람 확인·검증 뒤 반영·마지막 거절의 다섯 겹 확인 절차 가설, 신뢰도 low), 후속 질문 3건
- 대분류 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 4: 13. 작업 배정 — MRTA 에 LLM 배정 출력의 실행 전 검사와 디스패처·로봇 쪽 마지막 거절을 반영하도록 제안(q4-01)
- 세부영역 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 4: 배정 출력의 실행 전 검사(SafePlan)·무입찰 FailedToAssign·수행 불가 동작 거절을 6. 대표 접근법과 기술에 반영하도록 제안(실행 2026-09-25-79)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 과도한 에이전시 | Excessive Agency | LLM 기반 시스템이 필요 이상의 기능·권한·자율성을 가져 잘못되거나 조작된 출력이 해로운 행동으로 이어지는 위험으로, OWASP LLM Top 10(2025)의 한 항목이다. | 27, 26, 18 | ref-713 |
| new | 자동화 편향 | Automation Bias | 사람이 자동화 시스템의 출력이나 권고를 충분히 따져 보지 않고 과도하게 믿고 따르는 경향으로, 사람 승인 절차를 형식적 확인으로 만들 수 있다. | 18, 27, 25 | ref-724, ref-725 |
| new | 명시적 확인·암시적 확인 | Explicit / Implicit Confirmation | 대화 시스템이 이해한 내용을 사용자에게 직접 물어 승인받는 방식(명시적)과, 다음 응답 속에 이해한 내용을 되풀이해 보여 주고 사용자가 고치지 않으면 진행하는 방식(암시적)이다. | 18, 27 | ref-727 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-713 | OWASP Top 10 for LLM Applications 프로젝트 (OWASP GitHub) | LLM06:2025 Excessive Agency (2_0_vulns/LLM06_ExcessiveAgency.md) | 오픈소스 문서 | medium | https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md |
| ref-714 | Model Context Protocol (modelcontextprotocol GitHub) | Specification 2025-06-18 — Server Features: Tools (docs/specification/2025-06-18/server/tools.mdx) | 표준 | medium | https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/server/tools.mdx |
| ref-715 | LangChain (langchain-ai/docs GitHub) | Human-in-the-loop — LangChain docs (src/oss/langchain/human-in-the-loop.mdx) | 오픈소스 문서 | medium | https://docs.langchain.com/oss/python/langchain/human-in-the-loop |
| ref-716 | Yang, Z. 외(Brown University H2R Lab) | Plug in the Safety Chip: Enforcing Constraints for LLM-driven Robot Agents | 논문 | medium | https://arxiv.org/abs/2309.09919 |
| ref-717 | YzyLmc (Safety Chip 공식 저장소) | ltl_safety — README (Plug in the Safety Chip) | 오픈소스 문서 | medium | https://github.com/YzyLmc/ltl_safety |
| ref-718 | Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기) | Safety Guardrails for LLM-Enabled Robots | 논문 | medium | https://arxiv.org/abs/2503.07885 |
| ref-719 | KumarRobotics (RoboGuard 공식 저장소) | RoboGuard — Safety guardrails for LLM-enabled robots (GitHub README) | 오픈소스 문서 | medium | https://github.com/KumarRobotics/RoboGuard |
| ref-720 | SafePlan 저자(arXiv 2503.06892, 저자 미확인) | SafePlan: Leveraging Formal Logic and Chain-of-Thought Reasoning for Enhanced Safety in LLM-based Robotic Task Planning | 논문 | medium | https://arxiv.org/abs/2503.06892 |
| ref-721 | RichardHGL (CHI 2025 Plan-then-Execute 공식 저장소) | CHI2025_Plan-then-Execute_LLMAgent — README | 오픈소스 문서 | medium | https://github.com/RichardHGL/CHI2025_Plan-then-Execute_LLMAgent |
| ref-722 | He, G., Demartini, G., & Gadiraju, U. | Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents As A Daily Assistant | 논문 | medium | https://dl.acm.org/doi/10.1145/3706598.3713218 |
| ref-723 | arXiv 2604.04918 저자(미확인) | Comparing Human Oversight Strategies for Computer-Use Agents | 논문 | medium | https://arxiv.org/abs/2604.04918 |
| ref-724 | Future of Life Institute (artificialintelligenceact.eu, EU 규정 2024/1689 조문 게재본) | Article 14: Human Oversight \| EU Artificial Intelligence Act | 정부·연구기관 | medium | https://artificialintelligenceact.eu/article/14/ |
| ref-725 | arXiv 2502.10036 저자(미확인) | Automation Bias in the AI Act: On the Legal Implications of Attempting to De-Bias Human Oversight of AI | 논문 | medium | https://arxiv.org/abs/2502.10036 |
| ref-620 | 국가법령정보센터(법제처) | 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 (법률 제20676호, 2025-01-21) | 정부·연구기관 | medium | https://www.law.go.kr/lsInfoP.do?lsiSeq=268543 |
| ref-727 | Sagawa, H., Mitamura, T., & Nyberg, E. (INTERSPEECH 2004-ICSLP) | A comparison of confirmation styles for error handling in a speech dialog system | 논문 | medium | https://www.isca-archive.org/interspeech_2004/sagawa04_interspeech.pdf |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-350 | Ren, A. Z. 외(Google DeepMind·Princeton University, KnowNo 프로젝트) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners — project page (robot-help.github.io) | 오픈소스 문서 | medium | https://robot-help.github.io/ |
| ref-356 | Rasa Technologies (RasaHQ/rasa GitHub) | Forms — Rasa documentation (docs/docs/forms.mdx) | 오픈소스 문서 | medium | https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 논문 | medium | https://arxiv.org/abs/2604.05427 |
| ref-418 | Mecalux | Mecalux integrates generative AI into Easy WMS | 벤더 문서 | low | https://www.mecalux.com/news/generative-ai-easy-wms-mecalux |
| ref-656 | Open Robotics (open-rmf) | rmf_ros2 — rmf_task_ros2/src/rmf_task_ros2/Dispatcher.cpp | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/src/rmf_task_ros2/Dispatcher.cpp |
| ref-711 | Tang, G. 외(arXiv 2606.31339) | Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems | 논문 | medium | https://arxiv.org/abs/2606.31339 |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-01 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 작업 대상 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-01 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 수행 자원 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-01 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 제약 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-01 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 예외·성과 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-01 | 단계 4. 오해석 방지와 확인 절차 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| OWASP Top 10 for LLM Applications 2025 (LLM06 Excessive Agency) | 프레임워크 | OWASP | 27, 26, 18 | ref-713 | https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md |
| Model Context Protocol 명세 2025-06-18 (Server Features: Tools) | 표준 | Model Context Protocol (modelcontextprotocol GitHub) | 27, 26, 18 | ref-714 | https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/server/tools.mdx |
| LangChain Human-in-the-loop 미들웨어 | 오픈소스 | LangChain | 18, 27 | ref-715 | https://docs.langchain.com/oss/python/langchain/human-in-the-loop |

## 추가 조사 요청

- 단계 4 페이지 3절·6절: 명령 권한(q4-03 — 사용자별 로봇·구역·작업 권한과 지시·확인 감사 기록)과 제한 운영 기준(q4-04)을 다룰 근거가 브리프에 없어 완료 조건을 채우지 못했다. 다음 트랙 실행에서 조사가 필요하다.
- 단계 4 페이지 3절: OWASP LLM06 문서의 발행일(2024-11)을 문서 안에서 확인해야 한다.
- 단계 4 페이지 3절: EU AI Act 제14조 제4항 (b)호를 EU 공식 관보(EUR-Lex) 원문으로 확인해야 [추정]을 [사실]로 바꿀 수 있다.
- 단계 4 페이지 3절: RoboGuard(92% → 2.5% 미만)·SafePlan(90.5%, 621개) 수치와 SafePlan 저자, 감독 전략 비교 연구(arXiv 2604.04918)의 저자·조건별 결과를 원문으로 확인해야 한다.
- 단계 4 페이지 3절: 물류 관제 요원의 승인 행동(승인 지연·거부율·자동화 편향)을 잰 연구나 국내 물류센터의 채팅·음성 지시 확인 사례가 필요하다(사람 확인 한정 가설의 근거가 일상 비서·컴퓨터 사용 에이전트 조건뿐이다).
- 단계 4 페이지 3절: 인공지능기본법 제34조의 시행령 세부 조치와 Sagawa 외(2004) 확인 방식 비교의 결과 우열이 미확인이다.
- 백로그 정리: q4-09·q4-10, q3-12·q3-13, q3-09·q3-10, q5-05·q5-06, q1-05·q1-06 중복 등록 정리가 필요하다(pipeline 담당·검증 판정 요청).

## 이행한 수정 지시

- f5 수치 정정 — 단계 4 페이지 3절 RoboGuard 문장과 아이디어 2 5절 소절을 '92% → 2.5% 미만(저자 보고값, 원문 미열람)'으로 고쳤다.
- ref-718 기관 칸 — 두 페이지의 각주 정의와 reference_updates 의 org 를 'Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.'로 고치고 'IEEE RA-L 2026 채택 표기'를 병기했다.
- ref-727 기관 칸 — 세 페이지의 각주 정의와 reference_updates 의 org 를 'Sagawa, H., Mitamura, T., & Nyberg, E. (INTERSPEECH 2004-ICSLP)'로 고쳤다.
- f6 — SafePlan 문장에 '(621개, 검증 미재확인)'을 붙이고 90.5% 에 '저자 보고값, 원문 미열람'을 병기했다.
- f13 — 감독 전략 비교 문장을 [추정]으로 강등하고 '저자 미확인, 원문 미열람, 조건별 수치 미확인'을 병기했다.
- f14 — EU AI Act 제14조 문장을 [추정]으로 강등하고 'EU 공식 관보(EUR-Lex) 원문 미확인, 제3자 조문 게재본·법학 논문 기준'을 병기했다.
- f12 — '그럴듯해 보이는 계획에 대해 사용자의 신뢰가 잘못 보정되기 쉬웠다'로 재서술하고 '시뮬레이션 환경' 표현을 뺐다(단계 4 페이지·아이디어 5절).
- f21 — 사람 확인 한정 문장에 근거 가운데 감독 전략 비교 요약과 자동화 편향 인식 요구가 [추정] 수준임을 밝히고 '선택지로 보인다'로 단정을 피했다.
- f22 — 영향이 큰 작업 예시(위험 구역 진입·적재 화물 취소·일괄 정지)를 '이 위키가 든 설명용 예시(출처 없음)'로 밝혔다.
- f19 — 다섯 겹 확인 절차 문장에 단일 출처 부재와 근거 조건(가정·실험실 로봇·소프트웨어 에이전트·로봇 관제 규격)을 함께 적고, 흐름도를 이 위키가 직접 그린 mermaid 로 두었다.
- f4·f5·f7 — 로봇 쪽 안전 모듈·보호 정지 같은 안전 기능은 로봇 자체 지능·제어 경계의 연계 대상이고 ROP 는 작업·배정 수준의 제약 대조만 맡는다는 문장을 가드레일 소절 끝과 아이디어 5절에 넣었다.
- f10 — VDA 5050 로봇의 주문 거절을 로봇 쪽 기능(연계 대상)으로 쓰고 ROP 는 거절 오류를 받아 확인 절차의 마지막 결과로 처리하는 쪽만 맡는다고 서술했다.
- f17 — Mecalux 사례를 [추정] 벤더 주장으로 두고 상위 업무 시스템(WMS) 제품 기능인 연계 대상 사례로만 썼다.
- f7 — SafeGate 문장에 ISO 13482 는 개인 돌봄 로봇 안전 표준이어서 물류 적용이 미확인임을 유지했다.
- f3·용어 — 단계 4 페이지 3절에서는 처음부터 LangChain 을 [사람 참여 루프(Human-in-the-Loop, HITL)](../../glossary/human-in-the-loop.md) 링크로, MCP 를 용어집 '모델 컨텍스트 프로토콜' 링크와 풀어쓰기로 맞췄다. 첫 초안에서는 아이디어 2 5절 소절과 업무 분해·배정 설계 초안 6절 새 항목의 MCP 가 누락되어 있었고, 2차 재실행에서 두 곳의 MCP 첫 등장을 용어집 링크·풀어쓰기로 고치고 초안 6절의 LangChain 도 사람 참여 루프 용어집 링크로 맞췄다.
- 용어집 — 과도한 에이전시, 자동화 편향, 명시적 확인·암시적 확인 3건을 new 로 냈고, 자동화 편향의 EU AI Act 언급은 description 에 [추정]·원문 미확인으로 반영했다.
- 온톨로지 — 개념 '사용자 확인 (Confirmation)'은 반영하지 않고 업무 분해·배정 설계 초안 6절에 q4-01 답 링크와 속성 후보(확인 대상·확인 방식·응답·확인자·시각·보여 준 입력 요약)를 질문으로 덧붙였으며, 초안 버전은 v0.8 그대로 두고 6절만 패치했다.
- 아이디어 2 5절 — '확인 절차(단계 4)는 아직 조사되지 않았다'는 머리 서술이 실행 2026-09-25-74 기준이고 실행 2026-09-25-79 에서 q4-01 에 답했다고 밝히는 문장과 새 소절 '오해석 방지 확인 절차'를 덧붙이고, 명령 권한(q4-03)·제한 운영 기준(q4-04)이 미조사임을 명시했다.
- 단계 4 페이지 6절 — 세 행 모두 '미충족', 검증 판정 '미충족 · 미승인', '다음 단계로 전환: 아니오(명령 권한 q4-03·제한 운영 기준 q4-04 미조사, 열린 질문 q4-02~q4-12)'로 쓰고 상태 줄의 단계 상태를 '진행 중'으로 두었다.
- 참고문헌 — ref-716·ref-718·ref-720·ref-722~ref-727 과 재사용 ref-350·ref-356·ref-417·ref-418·ref-656·ref-711 의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-713·ref-714·ref-715·ref-717·ref-719·ref-721·ref-031 은 원문 열람으로 두었다.
- 세부영역 반영 제안 — 13·18·26·27 세부영역 페이지는 고치지 않고 area_reflection_proposals 와 트랙 로그 항목으로만 냈으며, 27. AI·학습·적응과 모델 운영과 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스 양쪽 연결을 단계 페이지 7절과 제안에 적었다.
- 신뢰도 — 단계 4 페이지 프런트매터 confidence 를 low 로 쓰고 q4-01 종합과 아이디어 소절을 신뢰도 낮음으로 서술했다.
- 2차: OWASP 발행일 드리프트 — 단계 4 페이지 3절 OWASP 문장의 '(2025판, 문서 기준 2024-11)'을 '(2025판, 발행일 2024-11 은 문서 안에서 확인하지 못함)'으로 고치고, 4절 남은 불확실성과 ref-713 참고문헌 요약에도 같은 한계를 적었다.
- 2차: MCP 용어 — 아이디어 2 5절 소절에서 MCP 가 처음 나오는 표의 사람 확인 행을 '[모델 컨텍스트 프로토콜](../glossary/model-context-protocol.md)(Model Context Protocol, MCP) 도구 명세'로, 업무 분해·배정 설계 초안 6절 새 항목의 'MCP 도구 명세'를 '[모델 컨텍스트 프로토콜](../../glossary/model-context-protocol.md)(Model Context Protocol, MCP) 도구 명세'로 고치고, 1차 'f3·용어' 항목의 서술을 실제 이행 내용대로 고쳤다.
- 2차: 트랙 개요 — docs/tracks/nl-task-chatbot/index.md 를 update 로 추가해 '6. 살아있는 산출물 링크' 절만 replace 패치했다. 초안 줄에 실행 2026-09-25-79 무변경(v0.8 유지, 개념 '사용자 확인' 제안은 6절 질문)을, 아이디어 줄에 5절 '오해석 방지 확인 절차' 소절(q4-01) 추가와 q4-03·q4-04 미조사를 적었다. H1 아래 상태 줄('현재 단계: 단계 3. 구현 가설 설계', '마지막 트랙 실행: 2026-09-25')은 바꾸지 않았다.
- 2차: 2절 표 — q4-05~q4-14 의 질문 칸을 백로그(q4-13·q4-14 는 이번 backlog_updates)의 질문 문구 그대로 쓰고 q4-10 의 '(q4-09와 같은 질문의 중복 등록)'을 백로그 문구로 바꿨으며, 제기 근거 칸을 finding id 만(f14, f9, f11, f13, f20, f20, f22, f23, f22, f5)으로 고쳤다. 중복 설명과 실행 id 안내는 2절 도입 문장에만 두었다.
- 2차: 트랙 로그 호칭 — track_updates.log_entry 의 '적용 대상 13·18'을 '적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스'로 고쳤다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md
- 온톨로지 초안 버전: 0.8
- 트랙 로그 항목: 답한 질문: q4-01(다섯 겹 확인 절차 가설 — 해석 게이트·제약 게이트·사람 확인·검증 뒤 반영·마지막 거절, 확인 시점은 배치(베이스 해제) 전, 사람 확인은 영향이 큰 작업에 한정, 차등 확인; 근거 f1~f25, 종합 신뢰도 low) / 새 질문: q4-13(f22), q4-14(f5), q5-10(f21) / 온톨로지 변경: 없음(v0.8 유지). 제안된 개념 '사용자 확인 (Confirmation)'(f2·f3·f16·f19)은 검증이 반영하지 않아 초안 6절 질문으로 둠 — 버전 이력 행 없음 / 완료 조건 평가: 미충족(부족: 명령 권한 q4-03·제한 운영 기준 q4-04 미조사, 확인 절차 초안은 이번에 초안 6절·아이디어 2 5절에 반영했으나 2차 검증 전) / 세부영역 반영 제안: 4개 영역 5건 — 13. 작업 배정 — MRTA(6절), 18. 사람–로봇 협업·운영 인터페이스(6절), 26. 사이버보안·접근권한·개인정보(6절), 27. AI·학습·적응과 모델 운영(6·8절, 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스 양쪽 연결) / 다음 실행 제안: q4-03(명령 권한·감사 기록), q4-04(제한 운영 기준), 이어서 q4-02. 참고: 단계 3 완료 미승인 상태에서 CLI 지정으로 단계 4 를 다룸(트랙 개요 현재 단계는 단계 3 유지), q4-09·q4-10 등 백로그 중복 정리 필요.
- 개요 진행 현황: 단계 4 진행 중 — 열린 질문 13, 답함 1, 완료 조건 미충족 (CLI 지정 실행, 단계 3 완료는 아직 미승인이라 트랙 현재 단계는 단계 3 유지)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q4-01 | 답함 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-01 | — | — | — |
| q4-13 | 열림 | — | 물류 지시에서 사람의 명시적 확인이 필요한 영향이 큰 작업(위험 구역 진입, 적재 화물 취소·되돌림, 일괄 정지, 다른 사람의 진행 작업 우선순위 변경 등)과 암시적 확인으로 충분한 일상 작업을 어떤 기준으로 가르고, 그 기준 목록은 누가 정하고 갱신하는가? (q4-01 에서 파생) (관련: q4-04) | 4 | f22 |
| q4-14 | 열림 | — | 현장 안전·권한 규칙(금지 구역, 시간대 제한, 적재 제한)을 Safety Chip·RoboGuard 처럼 시간 논리 제약으로 옮겨 작업·배정 수준에서 대조하려면, 규칙을 공간 그래프·로봇 기능 온톨로지의 어떤 개념으로 표현해야 하는가? (q4-01 에서 파생) | 4 | f5 |
| q5-10 | 열림 | — | 물류 지시 시나리오에서 관제 요원의 승인 지연 시간·거부율·수정률을 재어 승인 피로와 자동화 편향이 나타나는지, 확인 요약에 결정적 검사 결과를 함께 보이면 잘못된 지시를 멈추는 비율이 달라지는지를 어떤 실험으로 측정하는가? (q4-01 에서 파생) | 5 | f21 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 6. 대표 접근법과 기술 | LLM 이 만든 배정 결과를 실행 전에 불변·전제·사후 조건으로 검사하는 연구(SafePlan, 저자 보고·원문 미열람)와, 디스패처의 무입찰 FailedToAssign·로봇의 수행 불가 동작 거절(로봇 쪽은 연계 대상)을 마지막 거절 장치로 소개하고, 확인 화면이 배정 기준을 보여 주고 전체 기준 일관성은 결정적 배정기가 지키는 분담([추정])을 분류 원문 질문과 연결한다. 27. AI·학습·적응과 모델 운영과 양쪽 연결. |
| 18 | 6. 대표 접근법과 기술 | 승인·인자 수정·거부·직접 응답 결정을 두는 사람 참여 미들웨어(LangChain)와 명시적·암시적 확인 방식(Sagawa 외 2004), 계획 승인 사용자 연구의 신뢰 보정 문제(CHI 2025)와 [추정] 수준의 감독 전략 비교를 근거로 사람 확인을 영향이 큰 작업에 한정하는 차등 구성([추정])을 소개한다. |
| 26 | 6. 대표 접근법과 기술 | OWASP LLM Top 10(2025)의 과도한 에이전시 원인(기능·권한·자율성)과 최소 권한·완전한 중재, 모델 컨텍스트 프로토콜(MCP) 도구 명세(2025-06-18)의 입력 검증·접근 통제·감사 기록 권고를 채팅 지시 명령 권한(q4-03)의 출발점으로 소개한다. |
| 27 | 6. 대표 접근법과 기술 | LLM 로봇 계획·배정 출력의 형식 논리 가드레일(Safety Chip, RoboGuard 92% → 2.5% 미만 저자 보고, SafePlan, SafeGate)을 소개하고 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스에 연결한다. 로봇 쪽 안전 기능은 연계 대상으로 짧게 둔다. |
| 27 | 8. 대표 연구와 자료 | 사람의 관리·감독 규정으로 EU AI Act 제14조 제4항 (b)호의 자동화 편향 인식 요구([추정], 공식 관보 원문 미확인)와 한국 인공지능기본법 제34조(고영향 인공지능 사업자의 사람의 관리·감독 조치)를 자료로 추가한다. 물류 배정 AI 의 해당 여부는 oq-105. |
