# 스토리텔러 산출 2026-09-25-77

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md | draft | q3-04 답함(3절 소제목 {#q3-04} 신설, 변경 유형별 조작 표·도식, 출하 시나리오), 2절 질문 목록 갱신과 q3-15 추가, 4절 결론 추가, 후속 질문 3건, 6절 완료 조건 미충족·전환 아니오(q3-05~q3-15), 7절 반영 제안, 8절 각주 12건 추가, 9절 이력 행 추가. 2차 수정: 전문으로 보내 H1 아래 단계 상태 줄을 답한 질문 4건·열린 질문 10건으로 갱신, 전환 줄 막힌 질문 범위를 q3-05~q3-15 로 고침 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | 초안 v0.7 → v0.8: 지시 개념에 속성 '변경 유형'·'원 지시 참조', 작업 개념에 속성 '변경 허용 상태'·'취소 시 보상 활동' 추가, 두 개념 초안 → 확정; 6절에 q3-04 답 연결과 경계 규칙·보상 작업 승인 주체 질문 추가. 2차 수정: 전문으로 보내 H1 을 '(v0.8)' 로 고쳐 프런트매터·JSON 버전과 맞춤 |
| update | docs/ideas/nl-task-chatbot.md | draft | 5절에 '지시 변경 반영' 소절 신설(q3-04, 실행 2026-09-25-77): 단계 3 시작 질문 4개가 모두 답해졌음과 다른 아이디어와의 연결은 여전히 구조 언급 수준(완료 조건 미충족)임을 명시, 새 각주 10건(2차 수정 대상 아님, 변경 없음) |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6. 살아있는 산출물 링크: 초안 현재 버전 v0.8(실행 2026-09-25-77 지시·작업 개념 확정)과 아이디어 2 5절의 지시 변경 반영(q3-04) 반영(2차 수정 대상 아님, 변경 없음) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 3 | q3-04 답함(지시 변경 반영: 변경 유형별 조작·변경 허용 상태·사건 기반 재스케줄링·보상 작업), 업무 분해·배정 설계 초안 v0.7 → v0.8, 후속 질문 3건 | run 2026-09-25-77
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 3: 진행 중 작업의 지시 변경(추가·수정·철회) 반영 방식을 정리하고(q3-04, 신뢰도 low) 업무 분해·배정 설계 초안을 v0.8 로 갱신
- 대분류 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA(트랙 자연어 업무 지시 챗봇 단계 3): 지시 변경 때 재배정 범위(Open-RMF 현재 구현은 같은 플릿 한정)와 사건 기반 재스케줄링 분담(추정)을 트랙 단계 페이지에 정리, 세부영역 반영 제안
- 세부영역 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 트랙 자연어 업무 지시 챗봇 q3-04 에서 긴급 지시·우선순위 변경 시 남은 요청 재배정과 Open-RMF 재배정 범위를 '6. 대표 접근법과 기술' 반영 제안으로 냄

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 사건 기반 재스케줄링 | Event-driven Rescheduling | 고장·긴급 주문·지시 변경 같은 사건이 생길 때마다 기존 일정을 다시 계산하는 재스케줄링 정책으로, 정해진 주기마다 다시 짜는 주기적 재스케줄링과 구분된다. | 14, 20, 13 | ref-718 |
| new | 동결 구간 | Frozen Horizon (Frozen Zone) | 계획 구간 가운데 가까운 시각의 일정을 고정해 재계산에서 바꾸지 않는 구간으로, 잦은 재계획이 일정을 흔드는 것을 줄이려고 둔다. | 14, 1, 20 | ref-719 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-126 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/cancel_task_request.json |
| ref-127 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/interrupt_task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/interrupt_task_request.json |
| ref-715 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/skip_phase_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/skip_phase_request.json |
| ref-537 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp |
| ref-717 | OPC Foundation | OPC UA for ISA-95 - Part 4: Job Control (OPC 10031-4) — 6 ISA-95 Data Representation Model | 표준 | medium | https://reference.opcfoundation.org/ISA95JOBCONTROL/v200/docs/6 |
| ref-718 | Vieira, G. E., Herrmann, J. W., & Lin, E. (Journal of Scheduling 6(1), 35-58) | Rescheduling Manufacturing Systems: A Framework of Strategies, Policies, and Methods | 논문 | medium | https://link.springer.com/article/10.1023/A:1022235519958 |
| ref-719 | Sridharan, S. V., Berry, W. L., & Udayabhanu, V. (Management Science 33(9), 1137-1149) | Freezing the Master Production Schedule Under Rolling Planning Horizons | 논문 | medium | https://pubsonline.informs.org/doi/10.1287/mnsc.33.9.1137 |
| ref-720 | InterruptBench 저자(arXiv 2604.00892, 저자 미확인) | When Users Change Their Mind: Evaluating Interruptible Agents in Long-Horizon Web Navigation | 논문 | medium | https://arxiv.org/abs/2604.00892 |
| ref-373 | Garcia-Molina, H., & Salem, K. (ACM SIGMOD 1987) | Sagas | 논문 | medium | https://dl.acm.org/doi/10.1145/38713.38742 |
| ref-722 | Rasa Technologies (RasaHQ/rasa-calm-demo GitHub) | rasa-calm-demo — data/flows/patterns.yml | 오픈소스 문서 | medium | https://github.com/RasaHQ/rasa-calm-demo/blob/main/data/flows/patterns.yml |
| ref-723 | 양진홍, 유남현(한국정보전자통신기술학회논문지 18(3), 155-171) | AI 기반 멀티 에이전트 시스템 제조 환경 도입 방법론 연구(A Study on the Methodology for Implementing AI-based Multi-Agent Systems in Manufacturing Environments) | 논문 | medium | https://www.koreascience.kr/article/JAKO202519736002981.page |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-495 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/task_description__compose.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/task_description__compose.json |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-677 | CoMuRoS 저자(arXiv 2511.22354, Frontiers in Robotics and AI 게재) | LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning | 논문 | medium | https://arxiv.org/abs/2511.22354 |
| ref-611 | RACE-Sched 저자(arXiv 2605.29262, 저자 미확인) | Harmonizing Real-Time Constraints and Long-Horizon Reasoning: An Asynchronous Agentic Framework for Dynamic Scheduling | 논문 | medium | https://arxiv.org/abs/2605.29262 |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 시작 조건 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-04 | 단계 3. 구현 가설 설계 — q3-04 지시 변경 반영 |
| 출하 | 작업 대상 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-04 | 단계 3. 구현 가설 설계 — q3-04 지시 변경 반영 |
| 출하 | 수행 자원 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-04 | 단계 3. 구현 가설 설계 — q3-04 지시 변경 반영 |
| 출하 | 제약 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-04 | 단계 3. 구현 가설 설계 — q3-04 지시 변경 반영 |
| 출하 | 완료·인계 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-04 | 단계 3. 구현 가설 설계 — q3-04 지시 변경 반영 |
| 출하 | 예외·성과 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-04 | 단계 3. 구현 가설 설계 — q3-04 지시 변경 반영 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Rasa CALM 대화 복구 패턴(rasa-calm-demo patterns.yml) | 오픈소스 | Rasa Technologies | 18, 27 | ref-722 | https://github.com/RasaHQ/rasa-calm-demo/blob/main/data/flows/patterns.yml |

## 추가 조사 요청

- 단계 3 완료 조건(아이디어 2 5절의 다른 아이디어와의 연결): 변경 허용 상태·취소 시 보상 활동·배정 실패 원인이 아이디어 1 로봇 기능 온톨로지(취소 가능한 동작, 선언·운용 능력)와 아이디어 3 공간 그래프(장소 후보)의 어떤 개념과 이어지는지 근거 finding 이 필요하다 — 현재는 구조 언급 수준이라 완료 조건이 미충족이다.
- Open-RMF 에서 새 작업 요청이 들어올 때 이미 대기 중인 작업의 배정이 함께 재계산되는지(재입찰·재계획 범위)와 제출된 작업의 우선순위 변경 요청 형식이 rmf_api_msgs 스키마 전체 목록에 있는지 확인이 필요하다 — q3-04 소절의 f7 이 연 파일 범위의 부재 관찰에 그친다.
- OPC UA for ISA-95 Part 4 작업 제어의 Pause·Resume 메서드와 발행일을 원문(또는 노드셋 ref-130)으로 재확인해 q3-04 소절의 [추정] 문장을 확정할 근거가 필요하다.
- 물류 창고 로봇에 준 지시를 도중에 바꾸는 상황(취소·우선순위 변경)의 연구나 국내 물류 사례가 필요하다 — 현재 근거는 제조·웹 탐색·실험실 조건뿐이다.
- 용어집 페이지 event-driven-rescheduling·frozen-horizon 이 퍼블리셔로 생성된 뒤 다음 실행에서 단계 3 페이지 q3-04 소절의 두 용어에 용어집 링크를 다시 걸 수 있다(이번 재작성에서는 아직 없는 페이지라 링크를 뺐다).

## 이행한 수정 지시

- f17 강등 — 단계 3 페이지 3절 q3-04 소절의 국내 연구 문장을 [추정]으로 쓰고 '(원문 미열람, 검색 요약 기준, 재스케줄링 요청 구조는 검증 검색에서 재확인되지 않음)'을 병기했다.
- ref-723 서지 — 단계 3 페이지 8절 각주와 reference_updates 에 저자 양진홍·유남현, 국문 제목 'AI 기반 멀티 에이전트 시스템 제조 환경 도입 방법론 연구', 발행 2025-06 을 반영했다.
- f10 — Update·Abort(및 확인된 Start·RevokeStart)만 [사실]로 쓰고 Pause·Resume 은 별도 [추정] 문장에 '(검색 요약 기준, 검증 재확인 못함)'으로 표시했으며 ref-717 발행일은 '미확인'으로 두었다(단계 페이지·초안·아이디어 페이지).
- f11 — 주기적·사건 기반 정책과 전략·정책·방법 틀을 확인된 내용으로 쓰고, 혼합 정책·수선/재생성 구분·환경 축 문장에 '(원문 미열람, 검색 요약 기준)'을 병기했다.
- f12 — '넓은 운영 조건(저자 보고, 시뮬레이션)'으로 서술하고 재고생산 조건은 미확인이라고 표시했다.
- f8 — deployment_time 을 '로봇이 이 배정의 실행을 시작하는 시각'으로 고쳐 썼다.
- f9 — Commission::decommission() 을 본문에 쓰지 않았고 같은 플릿 한정에 '헤더 주석이 밝힌 현재 구현 기준'을 병기했다.
- f2 — 로봇의 정지·동작 취소·완료 실행을 분류 원문 9장 로봇 자체 지능·제어 경계의 연계 대상으로, ROP 는 cancelOrder 지시와 결과(actionState·오류) 반영만 맡는 것으로 별도 문장에 썼다.
- f6 — 새 문장으로 반복하지 않고 f7 문장 안에 단계 2 페이지 q2-01 소절 링크와 기존 각주 ref-125 를 재사용했다.
- f18 — RACE-Sched 는 q3-01 소절 링크와 ref-611 로 가리키는 한 줄만 두고 같은 서술을 반복하지 않았다.
- f20·f23 — [추정]을 유지하고 동결 구간 근거가 기준생산계획 조건이라 로봇 작업 적용이 미확인임과, 되돌림 뒤 재고 반영은 상위 업무 시스템 경계의 연계 대상으로 oq-021 에 연결됨을 단계 페이지·초안 6절·아이디어 페이지에 남겼다.
- f14 — '실험실 이종 로봇 팀 조건, 저자 보고, Frontiers in Robotics and AI 2026-08-04 게재'를 병기했다.
- f15·f24 — InterruptBench 가 웹 탐색 조건이라 로봇·물류 지시 적용은 미확인임을 해당 문장 뒤에 병기했다(단계 페이지·초안·아이디어 페이지).
- f21·f25 — 본문에서 열린 질문 oq-104(f21)와 oq-053(f25)을 연결했다.
- 각주 정의 — ref-717·ref-718·ref-719·ref-720·ref-373·ref-723 의 새 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고(ref-677·ref-611 은 기존 정의에 이미 표시), reference_updates 해당 항목에 source_unopened: true 를 넣었다.
- ref-031 — 단계 페이지·초안·아이디어 페이지 모두 기존 ref-031 각주 정의를 그대로 재사용하고 새로 정의하지 않았다.
- 온톨로지(지시) — 초안 2절 지시 행에 속성 '변경 유형'(새 지시 / 추가 / 수정 / 철회, 근거 f15·f16)과 '원 지시 참조'(후보)를 더하고 상태를 초안 → 확정으로 바꿨으며, 별도 기록 이력 방식(f22)은 정의에 넣지 않고 6절에 q3-04 답 링크와 함께 [추정]으로 적었다.
- 온톨로지(작업) — 초안 2절 작업 행에 속성 '변경 허용 상태'(외부 표현 원천 후보 VDA 5050 베이스·호라이즌, Open-RMF 단계, ISA-95 상태)와 '취소 시 보상 활동'(on_cancel)을 더해 확정으로 바꾸고, 진행 상태가 아닌 작업 속성임을 표 아래에 밝혔으며, 경계 결정 규칙(f20)과 보상 작업 승인 주체는 6절 질문으로 두었고, 초안 버전을 0.7 → 0.8 로 올려 프런트매터 ontology_version·JSON ontology_draft_version 을 맞췄다(H1 은 2차 수정에서 전문으로 맞춤).
- 단계 3 페이지 — 2절 q3-04 상태를 답함(답한 실행 2026-09-25-77, 답 위치 #q3-04)으로, 3절에 '### q3-04 … {#q3-04}' 소제목을 두었고, 6절 완료 조건은 미충족, 표 아래 줄은 '다음 단계로 전환: 아니오(…)'로 썼다(막힌 질문 범위는 2차 수정에서 q3-05~q3-15 로 고침).
- 아이디어 2 5절 — '지시 변경 반영' 소절에 단계 3 시작 질문 4개가 모두 답해졌다고 쓰고, 다른 아이디어와의 연결은 구조 언급 수준이라 완료 조건이 미충족임을 명시했다.
- 새 질문 3건 — q3-15(단계 3, f20), q4-12(단계 4, f23, '(관련: oq-021, q4-11)' 유지), q5-09(단계 5, f15)를 backlog_updates 와 단계 페이지 5절에 등록했다.
- 용어 — cancelOrder 는 용어집 '주문 취소 즉시 동작', 사가·보상 트랜잭션은 기존 용어집 항목에 링크했고, '사건 기반 재스케줄링'·'동결 구간'을 glossary_updates 에 신규로 냈다.
- 형식 검증 재작성 — 단계 3 페이지 q3-04 소절에서 아직 생성되지 않은 용어집 페이지 링크 ../../glossary/event-driven-rescheduling.md·../../glossary/frozen-horizon.md 두 곳을 링크 없는 용어(영문 병기)로 바꿨다. 내용·태그·각주는 바꾸지 않았다.
- 2차: 초안 H1 버전 — task-model-draft.md 를 patches 대신 전문(content)으로 보내 H1 을 '# 업무 분해·배정 설계 초안 (v0.8)' 로 고쳐 프런트매터 ontology_version '0.8'·track_updates.ontology_draft_version '0.8' 과 맞췄다(page-status 자동 영역 내용은 손대지 않음).
- 2차: 단계 상태 줄 — stage-3-implementation-hypothesis.md 를 전문으로 보내 H1 아래 줄을 '> 단계 상태: 진행 중 · 열린 질문: 10건 · 답한 질문: 4건 · 완료 조건: 미충족 · 마지막 실행: 2026-09-25' 로 고쳤고, log_entry 비고의 '갱신하지 못했다' 문구를 갱신 완료로 바꾸고 백로그 기준 열린 질문 11건(q3-13 중복 포함)을 병기했다.
- 2차: 전환 줄 — 단계 3 페이지 6절 표 아래 줄을 '다음 단계로 전환: 아니오(아이디어 2 5절 다른 아이디어와의 연결 미완, 실험 계획 없음, 열린 질문 q3-05~q3-15)' 로 고치고 log_entry 완료 조건 평가 문구(q3-05~q3-15)와 맞췄다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md
- 온톨로지 초안 버전: 0.8
- 트랙 로그 항목: 답한 질문: q3-04(진행 중 작업의 지시 변경 반영 — 변경 유형별 조작, 변경 허용 상태, 사건 기반 재스케줄링 분담, 이력, 보상 작업, 변경 확인; 이 위키의 종합, 신뢰도 low) / 새 질문: q3-15(단계 3, f20), q4-12(단계 4, f23, 관련 oq-021·q4-11), q5-09(단계 5, f15) / 온톨로지 변경: v0.7 → v0.8: 개념 '지시'에 속성 '변경 유형'(f15·f16·f19)·'원 지시 참조'(후보, f22) 추가·초안 → 확정, 개념 '작업'에 속성 '변경 허용 상태'(f1·f4·f10·f20)·'취소 시 보상 활동'(f5·f23) 추가·초안 → 확정, 근거 실행 2026-09-25-77; 거부 없음(이력 방식 f22, 경계 결정 규칙 f20, 보상 작업 승인 주체는 초안 6절 질문) / 완료 조건 평가: 미충족(부족: 아이디어 2 5절의 다른 아이디어와의 연결이 구조 언급 수준, 실험 계획 없음, 열린 질문 q3-05~q3-15) / 세부영역 반영 제안: 13. 작업 배정 — MRTA, 14. 작업 순서·스케줄링, 20. 예외 복구·재계획·업무 연속성, 12. 명령·작업 실행의 신뢰성, 1. 주문·업무 시스템 연계, 27. AI·학습·적응과 모델 운영, 18. 사람–로봇 협업·운영 인터페이스 7건 / 다음 실행 제안: 단계 3 완료 조건을 위해 다른 아이디어와의 연결 근거 조사(q3-06·q3-12), q3-15, 백로그 중복(q3-09·q3-10, q3-12·q3-13, q4-09·q4-10, q5-05·q5-06, q1-05·q1-06) 정리 / 비고: 단계 페이지 H1 아래 단계 상태 줄을 2차 수정에서 전문으로 갱신했다(단계 페이지 2절 표 기준 열린 질문 10건·답한 질문 4건; 백로그 기준으로는 중복 등록 q3-13 을 포함해 열린 질문 11건). 초안 H1 도 2차 수정에서 전문으로 '(v0.8)' 로 맞췄다. 형식 검증 재작성에서 아직 없는 용어집 페이지 링크 2건을 뺐다.
- 개요 진행 현황: 단계 3 진행 중 — 열린 질문 11(백로그 기준, 중복 q3-13 포함; 단계 페이지 표 기준 10), 답함 4, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q3-04 | 답함 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-04 | — | — | — |
| q3-15 | 열림 | — | 로봇 작업의 변경 허용 상태(바꿀 수 없는 부분과 바꿀 수 있는 부분)의 경계를 어디에 둘 것인가 — VDA 5050 베이스를 얼마나 앞서 풀어 줄지, Open-RMF 단계 가운데 어디부터 동결할지, 기준생산계획의 동결 구간처럼 시간으로 둘지 단계로 둘지에 따라 지시 변경 반영 가능 범위와 이동 연속성은 어떻게 달라지는가? (q3-04 에서 파생) | 3 | f20 |
| q4-12 | 열림 | — | 화물을 이미 실었거나 옮긴 작업을 채팅으로 취소할 때 되돌림 보상 작업의 생성·실행을 누가 승인하고, 지시 변경 요약 확인(무엇을 취소하고 무엇이 영향받는가)은 어떤 형식으로 보여 주는가? (q3-04 에서 파생) (관련: oq-021, q4-11) | 4 | f23 |
| q5-09 | 열림 | — | InterruptBench 의 추가·수정·철회 끼어들기 유형을 물류 지시(피킹·운반·출하) 시나리오로 옮겨, 챗봇이 변경을 올바른 작업에 적용하는 비율과 재계획 뒤 일정 변동량을 어떤 지표로 재는가? (q3-04 에서 파생) | 5 | f15 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 6. 대표 접근법과 기술 | 긴급 지시·우선순위 변경 때 처음 가장 가까웠던 로봇이 이미 묶여 있을 수 있어 남은 요청 전체를 다시 배정해야 전체 목적을 따를 수 있으나(추정), Open-RMF RobotUpdateHandle 의 재배정은 현재 구현 기준 같은 플릿 안으로 한정되고(사실, ref-537) rmf_task plan() 이 현재 로봇 상태와 요청 집합으로 배정을 새로 생성한다(사실, ref-377). oq-053 연결. |
| 14 | 6. 대표 접근법과 기술 | 재스케줄링 정책(주기적·사건 기반, 혼합은 검색 요약 기준)과 방법(수선·재생성, 검색 요약 기준)의 분류 틀(ref-718), 기준생산계획 동결 구간의 비용 영향(저자 보고, ref-719, 로봇 적용 미확인), 작업 계획기 재실행으로 일정 갱신과 LLM 을 결정 루프 밖에 두는 분담(추정, oq-104). 27. AI·학습·적응과 모델 운영과 양쪽 연결. |
| 20 | 6. 대표 접근법과 기술 | 진행 중 작업 취소 때 VDA 5050 cancelOrder 의 로봇 쪽 동작(취소 불가 동작은 끝까지 수행, 연계 대상, ref-031), Open-RMF 단계별 취소 시 활동 on_cancel(ref-495)과 사가 보상 트랜잭션(ref-373), 화물 적재 뒤 취소의 되돌림 보상 작업(추정, oq-021). |
| 12 | 6. 대표 접근법과 기술 | VDA 5050 베이스 불변·호라이즌 갱신과 취소 절차도 통신 한계로 신뢰할 수 없다는 명세 서술(ref-031), Open-RMF 취소·중단·단계 건너뛰기 요청 형식(ref-126~ref-715)과 작업 상태의 취소·중단 기록(ref-111). |
| 1 | 7. 관련 표준·프레임워크·오픈소스 | OPC UA for ISA-95 Part 4 작업 제어는 작업 지시를 실행 전 상태에서만 Update 로 바꾸고 실행 중·중단·미시작 작업 지시는 Abort 로 Aborted 상태로 보낸다(원문 미열람, ref-717, Pause·Resume 은 재확인 못함). 지시 변경 반영 규칙의 업무 시스템 쪽 기준. |
| 27 | 8. 대표 연구와 자료 | 교차 규칙에 따라 LLM 에이전트의 사용자 끼어들기(추가·수정·철회) 적응 한계를 보고한 InterruptBench(웹 탐색 조건, 저자 보고, ref-720)와 채팅 의도 변경이 재계획·재배정을 촉발하는 CoMuRoS(실험실 조건, ref-677)를 적용 대상 13. 작업 배정 — MRTA·14. 작업 순서·스케줄링과 함께 연결. |
| 18 | 6. 대표 접근법과 기술 | 대화 복구 패턴(슬롯 수정 확인, 흐름 취소 메타 흐름, Rasa CALM 공식 데모, ref-722)과 지시 변경 적용 전 대상 작업·변경 유형·영향을 요약해 확인받는 절차(추정). |
