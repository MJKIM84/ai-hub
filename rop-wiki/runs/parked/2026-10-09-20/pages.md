# 스토리텔러 산출 2026-10-09-20

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md | draft | q2-04 답함(3절 소절 추가), 2절 표·4절·5절(q3-17)·6절 전환 줄·9절 이력 갱신, 프런트매터 last_run·sources 갱신. H1 아래 상태 줄은 패치로 바꿀 수 없어 퍼블리셔 반영 요청 |
| update | docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md | draft | 되돌아온 질문 q1-05·q1-06 답을 3절 두 소절로 추가, 4절 추가 결론·불확실성, 5절 후속 질문 q4-20·q5-20, last_run 갱신. 2절 표·상태 줄·5절 기존 행·9절 행·sources 는 게시본이 입력에 없어 미반영 |
| update | docs/tracks/chat-based-configuration-and-operation/task-model-draft.md | draft | 초안 v0.9 → v1.0: 작업(Task) 속성 '선후관계'를 작업 사이 선행 의존으로 정리(표현 형식 후보: 의존 그래프), 외부 표현 메모 추가(상태 확정 유지), 6절에 q2-04 답 연결과 LTL 명세 검사층 질문 추가. H1 '(v1.0)'은 패치로 바꿀 수 없어 퍼블리셔 반영 요청 |
| update | docs/ideas/chat-based-configuration-and-operation.md | draft | 3절에 물류 지향 LLM 작업 분해 연구 소절(실행 2026-09-25 기준 서술 명시, f1~f9), 4절에 중간 표현과 로봇 관제 인터페이스 대응 소절(f10~f24) 추가 |
| update | docs/tracks/chat-based-configuration-and-operation/index.md | draft | 6절에 실행 2026-10-09-20 기록 추가('현재 단계는 단계 3' 서술이 이전 실행 시점 기준임을 밝힘), last_run 갱신. H1 아래 상태 줄은 패치로 바꿀 수 없어 퍼블리셔 반영 요청 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | 채팅 기반 구성·운영 단계 2 | q1-05·q1-06·q2-04 답함, 업무 분해·배정 설계 초안 v0.9 → v1.0(작업 선후관계 정리), 새 질문 3건(q3-17·q4-20·q5-20), 아이디어 페이지 3·4절 갱신 | run 2026-10-09-20
- 홈 최근 업데이트: 2026-10-09 — 채팅 기반 구성·운영 단계 2: 물류 지향 LLM 분해 연구(q1-05·q1-06)와 중간 표현의 로봇 관제 인터페이스 대응(q2-04)에 답함, 업무 분해·배정 설계 초안 v1.0
- 대분류 최근 업데이트: 2026-10-09 — 12. 채팅으로 업무 지시·오케스트레이션: 채팅 기반 구성·운영 트랙 단계 2 실행에서 의존 DAG·행동 트리·LTL 중간 표현과 VDA 5050 주문·Open-RMF 작업 요청 대응을 정리(신뢰도 low)
- 세부영역 최근 업데이트: 2026-10-09 — 12. 채팅으로 업무 지시·오케스트레이션: 트랙 반영 제안 4건(5절 물류창고 사례, 6절 중간 표현·의존 DAG 실행, 7절 Isaac Mission Dispatch·PlanSys2, 10절 44·47·25·26 연결)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 유한 트레이스 선형 시간 논리 | Linear Temporal Logic on Finite Traces (LTLf) | 유한한 길이의 실행 궤적에 대해 '언젠가', '항상', '다음' 같은 시간 조건을 표현하는 선형 시간 논리의 변형으로, 끝이 있는 로봇 임무 명세에 쓰인다. | 12, 24, 44, 54 | ref-1345, ref-1346 |
| new | 작업 의존 그래프 | Task Dependency Graph (Dependency DAG) | 하위 작업을 노드로, 먼저 끝나야 하는 선행 관계를 방향 간선으로 둔 방향 비순환 그래프로, 실행기는 위상 순서에 따라 의존이 풀린 작업부터 실행한다. | 12, 24, 26 | ref-059, ref-1343 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-1337 | Göbel, K., Lorang, P., Staderini, V., & Zips, P. (AIT Austrian Institute of Technology, IFAC PapersOnline 59(18)) | Integrating LLMs and Classical Planning for Pallet Logistics: A Case Study | 논문 | medium | https://publications.ait.ac.at/de/publications/integrating-llms-and-classical-planning-for-pallet-logistics-a-ca/ |
| ref-1338 | Chen, Y., Arkin, J., Zhang, Y., Roy, N., & Fan, C. (MIT, ICRA 2024 게재, 열람 판 arXiv v2 2024-03) | Scalable Multi-Robot Collaboration with Large Language Models: Centralized or Decentralized Systems? | 논문 | high | https://arxiv.org/abs/2309.15943 |
| ref-1339 | Research Square 프리프린트(저자 미확인) | An Intelligent Warehouse Execution Framework Integrating SAP Extended WarehouseManagement, Large Language Models, SAP Business Technology Platform, and Autonomous Mobile Robots | 논문 | low | https://www.researchsquare.com/article/rs-10351090 |
| ref-1340 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/event_description__sequence.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__sequence.json |
| ref-1341 | NVIDIA (nvidia-isaac GitHub) | isaac_mission_dispatch — README | 오픈소스 문서 | high | https://github.com/nvidia-isaac/isaac_mission_dispatch |
| ref-1342 | NVIDIA (nvidia-isaac GitHub) | isaac_mission_control — README | 오픈소스 문서 | medium | https://github.com/nvidia-isaac/isaac_mission_control |
| ref-1343 | PlanSys2 (ROS 2 Planning System 프로젝트) | PlanSys2 Design | 오픈소스 문서 | high | https://plansys2.github.io/design/index.html |
| ref-1344 | Xu, S., Luo, X., Huang, Y., Leng, L., Liu, R., & Liu, C. | Nl2Hltl2Plan: Scaling Up Natural Language Understanding for Multi-Robots Through Hierarchical Temporal Logic Task Representation | 논문 | medium | https://arxiv.org/abs/2408.08188 |
| ref-1345 | Luo, X., & Liu, C. (IEEE Transactions on Robotics 2025 게재 표기) | Simultaneous Task Allocation and Planning for Multi-Robots under Hierarchical Temporal Logic Specifications | 논문 | medium | https://arxiv.org/abs/2401.04003 |
| ref-1346 | Neupane, A., Mercer, E. G., & Goodrich, M. A. (AAMAS 2023 ARMS 워크숍) | Designing Behavior Trees from Goal-Oriented LTLf Formulas | 논문 | medium | https://arxiv.org/abs/2307.06399 |
| ref-1347 | Valmeekam, K., Marquez, M., Olmo, A., Sreedharan, S., & Kambhampati, S. (NeurIPS 2023 Datasets and Benchmarks) | PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change | 논문 | medium | https://arxiv.org/abs/2206.10498 |
| ref-181 | Shi, G., Wu, Y., Kumar, V., & Sukhatme, G. S. | PIP-LLM: Integrating PDDL-Integer Programming with LLMs for Coordinating Multi-Robot Teams Using Natural Language | 논문 | medium | https://arxiv.org/abs/2510.22784 |
| ref-059 | Wang, Y. 외(DART-LLM 저자) | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 논문 | medium | https://arxiv.org/abs/2411.09022 |
| ref-413 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/task_new.html |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-780 | 강건·강서연·배정찬(KAIST, 대한산업공학회 추계학술대회 논문집) | 제조 물류 로봇에서의 대규모 언어 모델(LLM)을 활용한 로봇 협업 인터페이스 구축 | 논문 | medium | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11609734 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 로봇 관제 인터페이스(VDA 5050 주문, Open-RMF 작업 요청)에 작업 사이 의존·대안 경로·기한을 표현하는 확장 제안이나 차기 판 논의가 있는가? (관련 기존 질문: oq-049, oq-137) | 20, 21, 24 | 열림 | — |

## 현장 유형 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| NVIDIA Isaac Mission Dispatch (행동 트리 임무를 VDA 5050 주문으로 보내는 임무 배치 서비스) | 오픈소스 | NVIDIA | 12, 20, 24 | ref-1341 | https://github.com/nvidia-isaac/isaac_mission_dispatch |
| NVIDIA Isaac Mission Control (플릿 관리 서비스) | 오픈소스 | NVIDIA | 12, 20, 23 | ref-1342 | https://github.com/nvidia-isaac/isaac_mission_control |
| PlanSys2 (ROS 2 Planning System) | 오픈소스 | PlanSys2 프로젝트 | 24, 26, 44 | ref-1343 | https://plansys2.github.io/design/index.html |

## 추가 조사 요청

- 입력 누락(pipeline/run_daily·agent_runner.py 담당): 단계 1 게시본 docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md 가 이번 재실행 입력에 없어 2절 표의 q1-05·q1-06 상태·답한 실행 id·답 위치 칸과 중복 등록 메모, 5절 기존 q1-05 행의 상태, 6절 전환 줄, 9절 이력 행, 프런트매터 sources 를 고치지 못했다. 같은 이유로 직전 초안 runs/2026-10-09-20/pages/ 의 단계 1·초안·아이디어·개요 파일도 입력에 없어 브리프에서 다시 썼다.
- patches 로 표현할 수 없는 항목(퍼블리셔 또는 patch 적용 코드 담당): patches 는 H2 절 본문만 바꾸므로 H1 아래 줄을 바꾸지 못한다. 다음 값을 반영해 달라 — 단계 2 상태 줄 '> 단계 상태: 진행 중 · 열린 질문: 3건 · 답한 질문: 4건 · 완료 조건: 미충족 · 마지막 실행: 2026-10-09'; 단계 1 상태 줄 '열린 질문: 0건 · 답한 질문: 6건 · 마지막 실행: 2026-10-09'(단계 상태·완료 조건은 기존 값 유지); 트랙 개요 상태 줄 '> 트랙 상태: active · 현재 단계: 단계 2. 필요한 데이터와 표준 조사 · 마지막 트랙 실행: 2026-10-09'; 업무 분해·배정 설계 초안 H1 '# 업무 분해·배정 설계 초안 (v1.0)'.
- 단계 1 9절에 넣을 행: '| 2026-10-09 | 2026-10-09-20 | q1-05, q1-06 | q4-20, q5-20 | 없음(v0.9 → v1.0 변경 근거는 단계 2 의 q2-04) | 6 |'. 단계 1 4절의 기존 '물류·창고 지시를 다룬 LLM 분해 연구는 확인되지 않았다' 줄 끝에는 '(실행 2026-09-25 기준)'을 덧붙여야 한다(이번에는 같은 절 끝에 시점 기준을 밝히는 문장을 덧붙였다). 단계 1 프런트매터 sources 에는 ref-1337, ref-1338, ref-1339, ref-1347, ref-780 을 더해야 한다.
- SAP EWM 연동 프리프린트(ref-1339)의 저자·게시일·실제 창고 운영 여부와 KAIST 2023 발표(ref-780)의 초록·본문: 12. 채팅으로 업무 지시·오케스트레이션 5절과 61. 물류창고의 물류창고·제조 공장 사례의 여섯 항목(제약·예외·성과)을 채우려면 원문 열람이 필요하다.

## 이행한 수정 지시

- f1 문구 축소 — 단계 1 q1-05 소절과 아이디어 3절에서 '신뢰할 수 있고 실행 가능한 계획을 만드는 데 어려움을 겪는다'로 씀
- f2 조건 병기 — 단계 1 q1-05 소절에 저자 보고·2D 격자 시뮬레이션·로봇 수별 10회·합 40회를 적고, reference_updates 의 ref-1338 기관 칸에 ICRA 2024 게재·v2 2024-03 을 넣음
- f6 범위 축소 — 단계 1 q1-05 소절에 서지 기준(내용 미확인) [추정]으로만 쓰고 ref-780 기관 칸에 저자 세 명과 KAIST 를 넣었으며 source_unopened true 로 표시
- f6 제조 공장 사례 제외 — 5절 적용 사례·site_matrix_updates 에 넣지 않음
- f7 한정 — 단계 1 q1-05 소절에 IPC 계열 도메인 벤치마크로만 쓰고 창고 물류 지시 근거로 쓰지 않는다고 밝힘
- f8 절 삭제 — '로봇 수 증가 시 성공률 하락' 절을 빼고 각주에서 ref-1347 을 뺀 [추정] 종합으로 씀
- f15 경유점 서술 제외 — 단계 2 q2-04 소절에 경유점 건너뛰기·마지막 경유점 서술을 넣지 않음
- f16 벤더 주장 — 단계 2 q2-04 와 아이디어 4절에서 [추정] 벤더 주장으로 유지, SAP EWM 변환을 사실로 쓰지 않음
- f18 조건 병기 — 질의응답 LLM 지명 조건과 건설 기계 시나리오를 단계 2 q2-04 와 아이디어 4절에 적음
- f19 — 개선 대상을 '작업 배정과 계획의 비용'으로 적고 저자 보고·게재처 미확인 병기
- f5 반영 제안 — 12. 채팅으로 업무 지시·오케스트레이션과 61. 물류창고 반영 제안에 동료심사 전 시제품, 연계 대상 SAP EWM, ROP 몫, 제약·예외·성과 미확인, 수치 제외를 적음
- f14·f15·f17·f18 경계 — 단계 2 q2-04 소절에 '연계 대상: 로봇 자체 지능·제어' 문장을 두고 ROP 근거는 내보내기 경계와 위상 순서 집행만 씀
- f10·f12·f13 중복 — q2-04 소절에서 기한·우선순위·deps 관찰을 반복하지 않고 #q2-01·#q2-02 를 가리키며 ref-413·ref-111·ref-125 를 재사용
- ref-110 각주 — 참고문헌 색인 제목 'Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2' 로 reference_updates 를 냄(각주 정의는 patch 적용 코드가 참고문헌에서 채움)
- 아이디어 3절 — 기존 G3 문장을 지우지 않고 3절 끝 새 소절에서 그 문장이 실행 2026-09-25 기준임을 밝히고 실행 2026-10-09-20 갱신 문장(f1~f5)을 덧붙임(문장 끝 직접 덧붙임은 patches 로 불가)
- 단계 1 두 소제목 — 3절에 '### q1-05 … {#q1-05}'·'### q1-06 … {#q1-06}'(q1-06 은 q1-05 를 가리키고 f9 만 더함)을 두고 신뢰도 low·실제 물류센터 운영 평가 미확인을 명시
- 단계 2 q2-04 — 2절 표를 답함(2026-10-09-20, #q2-04)으로 바꾸고 3절에 소절을 두었으며 대응표가 이 위키의 구성임을 [추정]으로 밝힘
- 단계 2 6절 — 완료 조건 1 충족, 2 미충족, 전환 줄 '아니오(작업 요구 적재물 속성·완료 조건 미확정, 열린 질문 q2-05·q2-06·q2-07)'로 씀. H1 아래 상태 줄은 patches 로 바꿀 수 없어 미이행, additional_research_requests 에 값을 적음
- 트랙 개요 — 6절에 '현재 단계는 단계 3' 서술이 이전 실행 시점 기준임을 밝히는 항목을 덧붙이고 last_run 갱신. 상태 줄은 patches 로 바꿀 수 없어 미이행, 값을 additional_research_requests 에 적음
- 온톨로지 변경 — 초안 2절 작업(Task) 행의 속성을 '선후관계(작업 사이 선행 의존; 표현 형식 후보: 의존 그래프)'로 고치고 외부 표현 메모를 [사실](f10·f12·f14·f18), 선택지 메모를 [추정](f22)으로 적음, 상태 확정 유지
- 초안 6절 — '작업 사이 선행 의존' 질문을 닫지 않고 q2-04 답 링크(f22·f23)를 덧붙였으며 'LTL 계열을 명세 검사층으로 둘 것인가'(f24, 관련 q4-14) 질문을 더함
- 버전 1.0 — 프런트매터 ontology_version·track_updates.ontology_draft_version 을 '1.0'으로 맞추고 log_entry·1절에 '1.0 은 0.1 증가 규칙에 따른 번호이며 완성판을 뜻하지 않는다'를 적음. H1 '(v1.0)'은 patches 로 바꿀 수 없어 미이행, additional_research_requests 에 적음
- LTLf 검사층 질문 — backlog_updates 에 넣지 않고 근거 f24 를 q4-14 에 연결한다고 단계 2 5절·log_entry 에 적음
- 오탈자 정규화 질문 — 단계 4 의 q4-20 으로 등록하고 끝에 '(관련: q2-05, q4-07)'을 붙임
- 관련 꼬리 — q3-17 에 '(관련: q3-08, q3-15)', q5-20 에 '(관련: q5-04)'를 붙임
- open_question_updates — 새 질문 끝에 '(관련 기존 질문: oq-049, oq-137)'을 붙이고 areas [20, 21, 24] 로 둠
- 용어집 — LTLf 를 linear-temporal-logic 에 연결하고, 작업 의존 그래프에 행동 의존 그래프와의 차이·선후 제약과의 관계를 한 문장으로 덧붙임
- 세부영역 반영 — 세부영역 페이지를 고치지 않고 area_reflection_proposals(12 네 건, 24, 61)와 log_entry 로만 남겼으며 12 제안에 5절 문장 갱신 필요와 44·47·25·26 연결을 적음
- 2차: 전체 되살림 — 직전 초안 파일이 입력에 없어(입력의 pages.json 은 빈 패치, pages/ 는 변경 전 단계 2 본문) 브리프·1차 판정에서 다시 썼고, storyteller 부록 R-3 대로 다섯 페이지를 patches 로 보냄
- 2차: 단계 2 빈 패치 삭제 — 2·3·4·5·6·9절 patches 와 프런트매터 last_run 2026-10-09 로 바꿈(전체 content 대신 R-3 의 patches 사용)
- 2차: 단계 2 상태 줄 — 미이행(patches 는 H1 아래 줄을 바꿀 수 없음), 프런트매터 last_run·sources(새 출처 10건 포함)는 이행
- 2차: 단계 1 q1-05 번호 — 새로 쓴 소절에서 '(1) … (2) …'로 매김
- 2차: 단계 1 2절 복원·칸 갱신 — 미이행(단계 1 게시본 입력 없음), 빠진 경로를 additional_research_requests 에 적음
- 2차: 단계 1 프런트매터 — last_run 2026-10-09 이행, sources 는 기존 목록이 입력에 없어 덮어쓰면 기존 id 를 잃으므로 미이행
- 2차: 단계 1 상태 줄 — 미이행(patches 불가, 게시본 없음)
- 2차: 단계 1 5절 q1-05 행·6절 전환 줄 — 미이행(원문 없음). 5절에는 새 후속 질문 q4-20·q5-20 표를 덧붙임
- 2차: 단계 1 9절 행 — 미이행(원문 없음), 행 내용을 additional_research_requests 에 적음
- 2차: 단계 1 4절 시점 표시 — 4절 끝에 '실행 2026-09-25 기준'임을 밝히는 문장을 덧붙임(기존 줄 끝 직접 수정은 원문이 없어 불가)
- 2차: 초안 v1.0 — 2절 작업 행 수정·프런트매터·ontology_draft_version '1.0' 이행, H1 은 patches 불가로 미이행
- 2차: backlog_updates — q1-05·q1-06·q2-04 답함과 새 질문 q3-17·q4-20·q5-20 등록
- 2차: log_entry·overview_progress·changelog_entry·index_updates — 실제 이행 결과로 씀
- 2차: 트랙 개요 — 6절 덧붙임 이행, 상태 줄 미이행(patches 불가)
- 2차: 아이디어 3·4절 — 이행
- 2차: reference_updates — ref-1337~ref-1347 등록, ref-1339·ref-780 에 source_unopened true
- 2차: glossary_updates·open_question_updates·area_reflection_proposals — 이행
- 2차: fixes_applied — 항목별 이행·미이행을 보고하고, 미이행 원인(입력 누락, patches 의 H1 영역 제한)을 additional_research_requests 에 적음
- docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md: 각주 정의 10개를 참고문헌에서 만들어 붙임: ref-059, ref-110, ref-1340, ref-1341, ref-1342, ref-1343, ref-1344, ref-1345, ref-1346, ref-181
- docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md: 각주 정의 5개를 참고문헌에서 만들어 붙임: ref-1337, ref-1338, ref-1339, ref-1347, ref-780
- docs/tracks/chat-based-configuration-and-operation/task-model-draft.md: 각주 정의 4개를 참고문헌에서 만들어 붙임: ref-1341, ref-1344, ref-1345, ref-1346
- docs/ideas/chat-based-configuration-and-operation.md: 각주 정의 9개를 참고문헌에서 만들어 붙임: ref-1337, ref-1338, ref-1339, ref-1341, ref-1342, ref-1343, ref-1344, ref-1345, ref-1346

## 트랙 갱신

- 단계 페이지: docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md
- 온톨로지 초안 버전: 1.0
- 트랙 로그 항목: 답한 질문: q1-05·q1-06(단계 1. 선행 연구·제품 사례 조사로 되돌아온 질문, f1~f9, 신뢰도 low), q2-04(f10~f24, 신뢰도 low) / 새 질문: q3-17(f15, 단계 3. 업무 지시 구현 가설 설계), q4-20(f4, 단계 4. 오해석 방지와 확인 절차), q5-20(f9, 단계 5. 업무 지시 검증과 가설 판정); LTLf 검사층 질문은 q4-14·oq-302·oq-314 와 중복이라 등록하지 않고 근거 f24 를 q4-14 에 연결 / 온톨로지 변경: v0.9 → v1.0: 개념 '작업 (Task)' 속성 '선후관계'를 작업 사이 선행 의존으로 정리(표현 형식 후보: 의존 그래프), 외부 표현 메모 추가(f10·f12·f14·f18, 추정 메모 f22), 상태 확정 유지, 거부 없음 — 1.0 은 0.1 증가 규칙에 따른 번호이며 완성판을 뜻하지 않는다, 근거 실행 2026-10-09-20 / 완료 조건 평가: 미충족(부족: 업무 분해·배정 설계 초안 개념 목록 표의 작업 요구 적재물 속성·완료 조건 미확정, 막힌 질문 q2-05·q2-06·q2-07) / 세부영역 반영 제안: 12. 채팅으로 업무 지시·오케스트레이션 4건, 24. 작업·워크플로 모델링 1건, 61. 물류창고 1건 / 다음 실행 제안: q2-05·q2-06·q2-07
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 3, 답함 4, 완료 조건 미충족 (실행 2026-10-09-20 에서 q2-04 와 앞 단계로 되돌아온 q1-05·q1-06 에 답함, 업무 분해·배정 설계 초안 v1.0)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-05 | 답함 | docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md#q1-05 | — | — | — |
| q1-06 | 답함 | docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md#q1-06 | — | — | — |
| q2-04 | 답함 | docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md#q2-04 | — | — | — |
| q3-17 | 열림 | — | 행동 트리의 selector 같은 대안 경로·제어 흐름을 VDA 5050 주문(한 줄 노드–간선)과 Open-RMF 순차 단계로 옮길 때, ROP 는 그 흐름을 자체 실행기에 두고 잎 작업만 주문·작업 요청으로 하나씩 내보내야 하는가, 그때 제어 흐름 변경에 따른 취소·재제출 비용과 로봇 이동 연속성은 어떻게 되는가? (q2-04 에서 파생) (관련: q3-08, q3-15) | 3 | f15 |
| q4-20 | 열림 | — | PIP-LLM 에서 오탈자가 새 품목·새 선반으로 해석된 것처럼, 물류 지시 속 품목 코드·선반·도크 식별자의 표기 오류를 이름 사전(q2-05)과 대조해 정규화할지 되물을지 정하는 기준은 무엇인가? (q1-05 에서 파생) (관련: q2-05, q4-07) | 4 | f4 |
| q5-20 | 열림 | — | 팔레트 물류 PDDL 도메인(IFAC 2025)이나 PIP-LLM 창고 과제 10개 같은 물류 과제 집합이 공개되어 있어 물류 지시 평가 자료(q5-04)의 출발점으로 쓸 수 있는가? (q1-06 에서 파생) (관련: q5-04) | 5 | f9 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 12 | 5. 적용 사례 (현장 유형 명시) | 현장 유형 물류창고 사례로 SAP EWM 연동 시제품(f5)을 더하고 '물류창고·제조 공장·상업 시설 사례 미확인' 문장을 갱신한다. 동료심사 전 프리프린트의 시제품(Raspberry Pi 기반 로봇) 구조이며 실제 창고 운영 여부 미확인, 원문 미열람. SAP EWM 은 분류 원문 19장의 상위 업무 시스템(연계 대상)이고 ROP 몫은 작업 수신과 완료 확정 반영이다. 여섯 항목 가운데 제약·예외·성과는 미확인으로 두고 검색 요약의 수치는 넣지 않는다. 제조 공장(KAIST 2023 발표, f6)은 내용 미확인이라 사례로 넣지 않는다. |
| 12 | 6. 대표 접근법과 기술 | 중간 표현(의존 DAG·PDDL 계획·행동 트리·LTL)과 VDA 5050 주문·Open-RMF 작업 요청의 대응(f17·f18·f22·f23, 이 위키의 종합·신뢰도 low): 잎 작업만 주문·작업 요청으로 내보내고 의존·대안 경로·기한은 ROP 작업 모델과 실행기가 보유하는 구성. 로봇 쪽 주행·스킬 실행은 연계 대상. |
| 12 | 7. 관련 표준·프레임워크·오픈소스 | NVIDIA Isaac Mission Dispatch(행동 트리 route·action 잎마다 VDA 5050 주문, 제어 흐름 변경은 취소·재제출, f14·f15), Isaac Mission Control(SAP EWM 작업 변환은 벤더 주장, f16), PlanSys2(PDDL 계획→의존 그래프 기반 행동 트리, f17). |
| 12 | 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) | 교차 규칙에 따라 LLM 의존 그래프·LTL 명세 연구(f18~f21)를 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과, 적용 대상인 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링에 함께 연결한다. |
| 24 | 7. 관련 표준·프레임워크·오픈소스 | 행동 트리 임무를 VDA 5050 주문으로 옮기는 Isaac Mission Dispatch(f14), PDDL 계획을 행동 트리로 실행하는 PlanSys2(f17), 하위 작업 의존 DAG(DART-LLM, f18), LTLf→행동 트리 변환(f21). 로봇 쪽 실행은 연계 대상. |
| 61 | 6. 대표 접근법과 기술 | 물류·창고 지시를 다룬 LLM 작업 분해 연구: 팔레트 물류 PDDL 하이브리드(f1, 초록 기준), 창고 착안 격자 시나리오(f2, 저자 보고), PIP-LLM Gazebo 창고 과제(f3, 저자 보고), SAP EWM 연동 시제품 프리프린트(f5, 원문 미열람·실제 운영 미확인) — 모두 시뮬레이션·시제품 조건. 공개 물류 지시–작업 데이터셋은 검색 범위에서 찾지 못함(f9, 부재의 확인 아님). |
