# 스토리텔러 산출 2026-09-25-71

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md | draft | q3-02 답함(3절 {#q3-02} 소제목 신설: 여섯 단계 입력·출력, 결정적 구성 요소·검증 게이트·도구 노출 경계, 피킹 시나리오), 2·4·5·6·7·8·9절 갱신, 후속 질문 3건. 2차 수정: 절 밖 상태 줄을 고치려고 전체 페이지로 보냄 — 상태 줄 '답한 질문: 2건', 6절 전환 줄 질문 범위 q3-03~q3-12 |
| update | docs/ideas/nl-task-chatbot.md | draft | 5절에 '처리 흐름과 핵심 구성 요소' 소절 신설(q3-02, 실행 2026-09-25-71), 절 안내 문장 갱신, 5절 각주 정의에 새 출처 추가·원문 미열람 표기 보완(2차 수정 대상 아님, 변경 없음) |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | 초안 v0.6 → v0.7: 배정 개념의 배정 산출 방식에 값 후보 '입찰 비교' 추가(f1, 상태 확정 유지), 1절 버전 설명 추가, 6절에 거부된 제안(실행 가능성 판정·검증 기록) 질문 2건 추가. 2차 수정: 절 밖 H1 을 고치려고 전체 페이지로 보냄 — H1 '(v0.7)' |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6절 살아있는 산출물: 초안 현재 버전 v0.7(v0.6·v0.7 내역), 아이디어 2 5절 작성 현황 갱신. H1 아래 트랙 상태 줄의 현재 단계는 2차 검증 참고대로 config 의 current_stage(단계 1)와 맞춰 두고 바꾸지 않음(공식 현재 단계는 사용자 결정 사항) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 3 | q3-02 답함(처리 흐름 여섯 단계의 입력·출력과 결정적 구성 요소·검증 게이트 배치, 신뢰도 low), 업무 분해·배정 설계 초안 v0.6 → v0.7(배정 산출 방식 '입찰 비교'), 후속 질문 3건, 1차 수정 지시 15건·2차 수정 지시 3건 이행 | run 2026-09-25-71
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 3: 지시 해석부터 진행 관리까지 여섯 단계의 입력·출력과, LLM 제안 뒤마다 결정적 검증을 두는 배치를 정리(q3-02, 추정·신뢰도 low)
- 대분류 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA(자연어 업무 지시 챗봇 트랙 단계 3): 능력 판정을 배정기 독립 입력으로 넘기고 입찰 비교·최적화가 배정하는 처리 흐름 가설과 반영 제안
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 모델 컨텍스트 프로토콜 | Model Context Protocol (MCP) | LLM 이 외부 시스템의 상태를 조회하고 정해진 도구로 동작을 수행하도록 도구·자원을 구조화해 노출하는 개방형 연결 규약이다. | 27, 26, 18 | ref-679 |
| new | 신경-기호 AI | Neuro-symbolic AI | LLM 같은 신경망 모델의 유연한 해석·생성과 계획기·검증기 같은 기호적(규칙·논리 기반) 구성 요소의 결정적 검사를 결합하는 AI 구성 방식이다. | 27, 13 | ref-674, ref-586 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-674 | Liu, Z., Fernandez-Ayala, V. N., Wang, T., Qin, Q., Wang, X. V., Dimarogonas, D. V., & Wang, L.(KTH) | Agentic Neuro-Symbolic Planning and Commissioning for Human-in-the-Loop Industrial Robotics with Digital Twins | 논문 | medium | https://arxiv.org/abs/2606.08214 |
| ref-675 | Pesjak, D., & Žabkar, J. | Robot Planning via LLM Proposals and Symbolic Verification | 논문 | medium | https://www.mdpi.com/2504-4990/8/1/22 |
| ref-676 | Pesjak, D. (minigrid-crewai 공식 저장소) | minigrid-crewai — Sense–Plan–Code–Act (SPCA) framework (GitHub README) | 오픈소스 문서 | medium | https://github.com/DrejcPesjak/minigrid-crewai |
| ref-677 | Tang, G. 외(arXiv 2606.31339) | Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems | 논문 | medium | https://arxiv.org/abs/2606.31339 |
| ref-678 | CoMuRoS 저자(arXiv 2511.22354, Frontiers in Robotics and AI 게재) | LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning | 논문 | medium | https://arxiv.org/abs/2511.22354 |
| ref-679 | robotmcp (ROS-MCP-Server 공식 저장소) | ros-mcp-server — Connect AI models like Claude & GPT with robots using MCP and ROS (GitHub README) | 오픈소스 문서 | medium | https://github.com/robotmcp/ros-mcp-server |
| ref-680 | Park, J., & Kim, J. S.(소속 미확인) | STRAP-LLM: structured task allocation and planning for heterogeneous robots using large language models | 논문 | medium | https://link.springer.com/article/10.1007/s11370-025-00676-0 |
| ref-376 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/task.html |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 논문 | medium | https://doi.org/10.3390/electronics15163562 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 논문 | medium | https://arxiv.org/abs/2604.05427 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp |
| ref-404 | Open Robotics (open-rmf) | rmf_task — README | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_task |
| ref-166 | Obata, K., Aoki, T., Horii, T., Taniguchi, T., & Nagai, T. | LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning | 논문 | medium | https://arxiv.org/abs/2410.21040 |
| ref-180 | 이종록, 황정훈, 박민철(한국전자기술연구원) | LLM 기반 로봇관제시스템의 Agent AI 구축 | 논문 | medium | https://d2j16w31g89z0j.cloudfront.net/site/2026w/abs/0560-YDVVV.pdf |
| ref-356 | Rasa Technologies (RasaHQ/rasa GitHub) | Forms — Rasa documentation (docs/docs/forms.mdx) | 오픈소스 문서 | medium | https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx |
| ref-586 | Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S., Saldyt, L., & Murthy, A. | LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks | 논문 | medium | https://arxiv.org/abs/2402.01817 |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-02 | 단계 3. 구현 가설 설계 |
| 피킹 | 작업 대상 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-02 | 단계 3. 구현 가설 설계 |
| 피킹 | 수행 자원 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-02 | 단계 3. 구현 가설 설계 |
| 피킹 | 제약 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-02 | 단계 3. 구현 가설 설계 |
| 피킹 | 완료·인계 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-02 | 단계 3. 구현 가설 설계 |
| 피킹 | 예외·성과 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-02 | 단계 3. 구현 가설 설계 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 단계 3 페이지 3절 q3-02·초안 6절: Electronics 2026 ReasonerOutput 의 필드 구성과 저자를 원문으로 확인해야 한다 — 능력 판정을 플릿 단위·로봇 단위 중 어느 단위로 배정기에 넘기는지(q3-12) 판단하는 데 필요하다.
- 단계 3 페이지 3절: SDI(arXiv 2606.08214) 원문에서 실패 복구 경로 설정·디지털 트윈 검토의 구현 세부와 절제 실험 조건(그룹별 결과)을 확인해야 한다 — 현재 '세부 미확인'으로 두었다.
- 단계 3 페이지 3절: SPCA 논문(MAKE 8(1) 22) 원문에서 Plan 단계 구성별 결과를 확인해야 한다 — README 와 논문 요약의 서술 차이 때문에 추정으로 두었다.
- 단계 3 페이지 3절: CoMuRoS 저자 목록·정답률 지표 정의, STRAP-LLM 의 게재 연도·수치·비교 대상·저자 소속이 미확인이다.
- 아이디어 2 5절(완료 조건): '다른 아이디어와의 연결'(능력 질의의 아이디어 1 산출물 연결, 장소 슬롯의 아이디어 3 공간 노드 해석)을 근거 finding 과 함께 조사해야 단계 3 완료 조건 첫 행을 채울 수 있다.
- 실험 페이지(완료 조건): 단계 3 실험 계획 제안(예: q5-07 처럼 결정적 검증기와 LLM 비평자를 물류 지시 시나리오로 비교)을 다음 트랙 실행에서 다룰 수 있도록 필요한 공개 물류 지시 시나리오 자료가 필요하다.
- 파이프라인 담당 요청: 차등 갱신(patches)으로는 H2 절 밖의 머리 줄(단계 페이지 상태 줄, 초안 H1 버전, 트랙 개요 상태 줄)을 고칠 수 없어 이번 재실행에서 해당 두 페이지를 전체 content 로 보냈다. 머리 줄 패치 경로가 필요하다.

## 이행한 수정 지시

- f8 강등 — 단계 3 페이지 3절과 아이디어 2 5절에서 SPCA 문장을 [추정]으로 쓰고, README 는 Plan 단계를 PDDL·LLM·하이브리드 가운데 고르는 틀로 적으며 'LLM→PDDL→휴리스틱 계획기→두 번째 LLM 코드 생성·컴파일·시뮬레이션 검증'은 그 하이브리드 구성을 원문 미열람 논문 요약 기준으로 서술한 것임을 밝혔다.
- f7 조건 병기 — 98.1%→3.8% 문장마다 '그룹 A–D 의 52개 명령 부분집합, 같은 방식으로 프롬프트한 LLM 으로 바꾼 조건의 저자 보고값, 독립 재현 미확인, 원문 미열람'을 붙였다(단계 3 페이지 3절·시나리오 표, 아이디어 2 5절).
- f6 — LangGraph·Unity3D 이름을 빼고 '실패 복구 경로 설정과 사람 검토용 디지털 트윈의 구현 세부는 재확인되지 않았다(세부 미확인)'로 쓰고, 디지털 트윈은 사람 검토용 시각화로만 다루며 22. 시뮬레이션·예측용 디지털 트윈이나 8. 실시간 세계 상태·데이터 일관성의 기능으로 보지 않는다고 명시했다.
- f9 — 제안 주체를 '에이전트·휴리스틱·최적화 모듈의 제안'으로 고치고 평가 조건(실내 공장 시나리오, 원격 건설 벤치마크, 검색 요약 기준)을 병기했으며, 원격 건설은 업종별 조건의 연계 대상으로 적었다. f18 종합 문장에도 같은 정정을 반영했다.
- f10·f19 — '정답률(correctness) 최대 0.91(22개 시나리오·54개 작업·약 20대 로봇 벤치마크, 저자 보고)'로 썼고 '재계획 세트 5개 시나리오 1.0' 수치는 어디에도 쓰지 않았다.
- f15 — STRAP-LLM 문장에 '(저자 보고; 수치·비교 대상·저자 소속·게재 연도는 미확인)'을 붙였고 reference_updates 의 ref-680 published 를 null 로, 각주 발행일을 '미확인'으로 두었다.
- f11 — SafeGate 문장 뒤에 ISO 13482 가 개인 돌봄 로봇 안전 표준이라 물류 이동로봇 적용은 미확인이며 안전 판정 자체를 ROP 직접 범위로 단정하지 않는다고 병기했다(단계 3 페이지·아이디어 2 5절).
- 배정 수정 승인 — 업무 분해·배정 설계 초안 2절 배정 행의 배정 산출 방식 값 후보에 '입찰 비교'를 더하고 정의·근거 칸에 ref-376 각주(finding f1, 실행 2026-09-25-71)를 붙였으며 상태는 확정 유지, 초안 버전을 0.6 → 0.7 로 올렸다(프런트매터 ontology_version·track_updates.ontology_draft_version; H1 은 절 밖이라 diff_summary 에 수정 필요를 적었다).
- 실행 가능성 판정 추가 거부 — 초안 2·3절에 넣지 않고 6절에 미해결 모델링 질문으로 두고 거부 사유(원문 미열람 단일 출처, 능력 온톨로지 초안과 대조 불가, 관계 재구성 근거 없음)를 적었다.
- 검증 기록 추가 거부 — 초안 2절에 넣지 않고 6절에 질문으로 두고, 배정 속성 '확인 여부'·사용자 확인 질문(q4-01·q4-04)과 겹쳐 경계가 정해지지 않았고 근거가 원문 미열람·추정이라는 사유를 적었다.
- q3-02 답함 — 단계 3 페이지 2절에서 q3-02 를 답함(답한 실행 2026-09-25-71, 답 위치 #q3-02)으로 바꾸고 3절에 '### q3-02 … {#q3-02}' 소제목을 두었으며, 3절 첫 단락과 4절 결론에 신뢰도 low 와 이 위키의 종합(f17·f18 추정)임을 적었다.
- 새 질문 3건 등록 — q3-12(f4)에 '(관련: oq-053)', q4-09(f20)에 '(관련: q4-03)'을 병기하고 q5-07(f7)과 함께 5절 표와 backlog_updates 에 냈다.
- 원문 미열람 표기 — 단계 3 페이지 8절을 다시 써서 ref-377, ref-404, ref-111, ref-236, ref-166, ref-417, ref-180, ref-356, ref-586, ref-674, ref-675, ref-677, ref-678, ref-680 의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 ref-376·ref-676·ref-679 는 표기하지 않았다. 아이디어 2 5절의 ref-404·ref-377 정의에도 붙였고, reference_updates 의 ref-674·675·677·678·680 에 source_unopened: true 를 넣었다. 패치하지 않은 절(아이디어 2 3절의 ref-356, 7절 뒤의 ref-111, 초안 7절 뒤 각주)의 기존 정의는 이번 패치 범위 밖이라 손대지 않았다.
- 26. 사이버보안·접근권한·개인정보 반영 제안 — area_reflection_proposals 에서 로봇 토픽·액션 직접 제어는 분류 원문 9장 '로봇 자체 지능·제어' 경계의 연계 대상으로 짧게 두고, ROP 가 상위 도구만 노출해야 한다는 판단은 [추정]으로만 적었다. 단계 3 페이지·아이디어 2 5절 본문도 같게 썼다.
- 완료 조건 표 — 단계 3 페이지 6절에서 아이디어 2 5절 행을 처리 흐름은 실렸으나 다른 아이디어와의 연결이 없어 '미충족 · 미승인'으로 두고, 표 아래 줄을 '다음 단계로 전환: 아니오(실험 계획 없음, 열린 질문 q3-03~q3-11)'로 썼다.
- docs/tracks/nl-task-chatbot/task-model-draft.md: 각주 정의 4개를 참고문헌에서 만들어 붙임: ref-236, ref-376, ref-674, ref-677
- 2차: 단계 3 페이지 상태 줄 — 절 밖 줄이라 페이지 전체를 content 로 보내며 H1 아래 상태 줄의 '답한 질문: 1건'을 '답한 질문: 2건'으로 고쳤다(열린 질문 10건은 그대로).
- 2차: 초안 H1 — 페이지 전체를 content 로 보내며 H1 을 '업무 분해·배정 설계 초안 (v0.7)'로 고쳐 프런트매터 ontology_version '0.7'·track_updates.ontology_draft_version '0.7'과 맞췄다(auto:page-status 마커 사이는 퍼블리셔 영역이라 손대지 않음).
- 2차: 단계 3 페이지 6절 전환 줄 — '다음 단계로 전환: 아니오(아이디어 2 5절 다른 아이디어와의 연결 없음, 실험 계획 없음, 열린 질문 q3-03~q3-12)'로 고쳤고, log_entry 의 완료 조건 평가와 같은 범위(q3-03~q3-12)로 맞췄다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md
- 온톨로지 초안 버전: 0.7
- 트랙 로그 항목: 답한 질문: q3-02(지시 해석·작업 분해·능력 질의·배정·스케줄링·진행 관리 여섯 단계의 입력·출력과 결정적 구성 요소·검증 게이트 배치, 근거 f1~f23, 신뢰도 low — 이 위키의 종합) / 새 질문: q3-12(f4, 관련 oq-053), q4-09(f20, 관련 q4-03), q5-07(f7) / 온톨로지 변경: v0.6 → v0.7: 개념 '배정 (Assignment)' 속성 '배정 산출 방식'에 값 후보 '입찰 비교' 추가(f1, 상태 확정 유지, 근거 실행 2026-09-25-71); 거부: 개념 '실행 가능성 판정'(f4·f17), '검증 기록'(f9·f6·f18) → 초안 6절 질문 / 완료 조건 평가: 미충족(부족: 아이디어 2 5절의 다른 아이디어와의 연결, 실험 계획, 열린 질문 q3-03~q3-12) / 세부영역 반영 제안: 13. 작업 배정 — MRTA, 27. AI·학습·적응과 모델 운영(2건), 26. 사이버보안·접근권한·개인정보, 5. 로봇 능력·작업 온톨로지 — 5건 / 다음 실행 제안: q3-03, q3-04, 단계 3 실험 계획 제안(q5-07 방향), 백로그 중복 정리(q3-09·q3-10, q5-05·q5-06, q1-05·q1-06) / 비고: 2차 수정에서 절 밖 머리 줄(단계 3 상태 줄, 초안 H1)을 고치려고 두 페이지를 전체 content 로 보냈다. 이번 실행은 CLI 로 단계 3 을 지정한 강제 실행이며 config 의 current_stage 는 1 이라, 트랙 개요 상태 줄의 공식 현재 단계는 사용자 결정 사항으로 남긴다
- 개요 진행 현황: 단계 3 진행 중 — 열린 질문 10, 답함 2, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q3-02 | 답함 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-02 | — | — | — |
| q3-12 | 열림 | — | ROP 가 온톨로지 기반 실행 가능성 판정(배정기 독립 출력)으로 후보를 거른 뒤 Open-RMF 처럼 플릿 단위 입찰로 배정할 때, 판정은 플릿 단위로 넘기는가 로봇 단위로 넘기는가, 제조사 관제가 플릿 안에서 다시 로봇을 고르면 판정 결과와 어긋날 때 누가 조정하는가? (q3-02 에서 파생) (관련: oq-053) | 3 | f4 |
| q4-09 | 열림 | — | 채팅 LLM 에 노출할 도구를 작업 요청 제출 같은 상위 도구로 한정할 때, 어떤 도구 목록과 사용자별 권한을 두어야 능력 질의·배정·검증 게이트를 우회하지 않는가? (q3-02 에서 파생) (관련: q4-03) | 4 | f20 |
| q5-07 | 열림 | — | SDI 절제 실험처럼 결정적 검증기를 LLM 비평자로 바꿨을 때의 성공률 차이를 물류 지시(피킹·운반·출하) 시나리오로 재면 어떤 결과가 나오며, 어느 단계의 검증기가 가장 큰 차이를 만드는가? (q3-02 에서 파생) | 5 | f7 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 6. 대표 접근법과 기술 | 트랙 자연어 업무 지시 챗봇 단계 3(실행 2026-09-25-71): 온톨로지 기반 실행 가능성 판정 결과를 배정기에 묶이지 않는 ReasonerOutput 으로 넘기는 방법(Electronics 2026, ref-236, 원문 미열람), Open-RMF 입찰 비교가 배정 단계에 놓이는 위치(ref-376), LiP-LLM 처럼 LLM 이 분해하고 선형계획이 배정하는 분담(ref-166), 지시 해석–능력 판정–결정적 배정 흐름과 분류 원문 SCM 질문의 연결은 목적 기준에 달렸다는 판단([추정]). 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽에 연결한다. |
| 27 | 6. 대표 접근법과 기술 | 트랙 단계 3(실행 2026-09-25-71): 신경-기호 구조 — SDI(LLM 은 언어 이해만, 검증·순서·실행은 결정적, ref-674), SPCA(Plan 단계 PDDL·LLM·하이브리드 수용, 하이브리드 파이프라인은 [추정], ref-675·ref-676), 관리형 블랙보드(에이전트·휴리스틱·최적화 모듈 제안을 결정적 검증·원자적 반영으로만 수용, ref-677), LLM 출력 반영 직전 단계 경계마다 검증 게이트를 두는 배치([추정]). 적용 대상 13. 작업 배정 — MRTA 와 함께 연결한다. |
| 27 | 8. 대표 연구와 자료 | SDI 기호 검증기 절제 실험: 검증기를 같은 방식으로 프롬프트한 LLM 으로 바꾸면 성공률 98.1%→3.8%(그룹 A–D 52개 명령 부분집합, 저자 보고값, 독립 재현 미확인, 원문 미열람, ref-674). |
| 26 | 6. 대표 접근법과 기술 | LLM 에 로봇을 도구로 노출하는 방식: ROS-MCP-Server 는 rosbridge 로 토픽·서비스·액션·파라미터를 MCP 도구로 노출하고 README 에 현재 권한 장치 설명이 없다(ref-679, 확인일 2026-09-25), 국내 KETI 연구는 LangChain 도구를 ROS 2 인터페이스로 정의했다(ref-180). 로봇 토픽·액션 직접 제어는 분류 원문 9장 '로봇 자체 지능·제어' 경계의 연계 대상이며, ROP 는 검증 파이프라인으로 들어가는 상위 도구만 노출해야 할 것으로 보인다는 판단은 [추정]으로만 둔다. |
| 5 | 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) | 온톨로지 기반 실행 가능성 판정(다축 능력 조건·적재 상태 도달 가능성) 결과를 배정기 독립 출력(ReasonerOutput)으로 13. 작업 배정 — MRTA 에 넘기는 연결(Electronics 2026, ref-236, 원문 미열람). |
