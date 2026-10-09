# 스토리텔러 산출 2026-10-09-25

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md | draft | q2-04 답함(3절 '### q2-04' 소절 신설, 중간 표현별 대응표는 이 위키 구성), 상태 줄·2절·4절·5절(q3-17)·6절(검증 판정 행별: 조건 1 충족·미승인, 조건 2 미충족·미승인, 전환 아니오)·7절·8절·9절 갱신 |
| update | docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md | draft | 되돌아온 질문 q1-05·q1-06 답함(3절 두 소제목, 신뢰도 low, 물류창고 사례 표), 상태 줄·프런트매터 sources(6건 추가)·2절(도입 문단 q1-01 출처 서술 유지)·4절·5절(q1-05 답함, q4-20·q5-20 추가)·6절 전환 줄·8절·9절(이력 표 맨 위 행, 버전 6) 갱신 |
| update | docs/tracks/chat-based-configuration-and-operation/task-model-draft.md | draft | 초안 v0.9 → v1.0: 작업 개념 속성 '선후관계'를 작업 사이 선행 의존(표현 형식 후보: 의존 그래프)으로 정리하고 외부 표현 메모 추가(상태 확정 유지, 관계 추가 없음), 6절에 q2-04 답 링크와 질문 2건 추가 |
| update | docs/ideas/chat-based-configuration-and-operation.md | draft | 3절에 물류·산업 지향 연구 갱신 소절(G3 서술은 실행 2026-09-25 기준임을 밝힘), 4절에 '중간 표현과 로봇 관제 인터페이스 대응' 소절 추가(결론은 추정) |
| update | docs/tracks/chat-based-configuration-and-operation/index.md | draft | 상태 줄을 '현재 단계: 단계 2. 필요한 데이터와 표준 조사 · 마지막 트랙 실행: 2026-10-09'로 고치고, 6절에 '현재 단계는 단계 3' 서술이 각 실행 시점 기준임과 실행 2026-10-09-25 결과를 덧붙임 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | 채팅 기반 구성·운영 단계 2 | q1-05·q1-06(물류·산업 지향 LLM 작업 분해 연구, 물류 지시 데이터셋)과 q2-04(중간 표현과 VDA 5050 주문·Open-RMF 작업 요청 대응) 답함, 새 질문 3건, 업무 분해·배정 설계 초안 v0.9 → v1.0, 1차 조건부 승인 수정 23건·2차 수정 7건 이행 | run 2026-10-09-25
- 홈 최근 업데이트: 2026-10-09 — 채팅 기반 구성·운영 단계 2: 되돌아온 질문 q1-05·q1-06(물류·산업 지향 LLM 작업 분해 연구는 시뮬레이션·초록·시제품 수준)과 q2-04(의존 DAG 를 작업 모델에 두고 잎 작업만 주문·작업 요청으로 내보내는 구성, 추정)에 답하고 업무 분해·배정 설계 초안을 v1.0 으로 갱신
- 대분류 최근 업데이트: 2026-10-09 — 채팅 기반 구성·운영 트랙(12. 채팅으로 업무 지시·오케스트레이션 중심): 물류·창고 지시 LLM 분해 연구와 중간 표현(의존 DAG·PDDL·행동 트리·LTL·워크플로 다이어그램)의 로봇 관제 인터페이스 대응을 단계 1·2 페이지에 정리, 12·24·25·61 세부영역 반영 제안
- 세부영역 최근 업데이트: 2026-10-09 — 12. 채팅으로 업무 지시·오케스트레이션: 트랙 실행 2026-10-09-25 에서 5절 물류창고 사례 후보(SAP EWM 연동 시제품, 동료심사 전·원문 미열람), 6절 의존 DAG 잎 단위 송출 구조, 7절 Isaac Mission Dispatch·PlanSys2 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 유한 트레이스 선형 시간 논리 | Linear Temporal Logic on Finite Traces (LTLf) | 기존 용어 '선형 시간 논리(LTL)'를 끝이 있는 실행 궤적에 맞게 바꾼 변형으로, '언젠가'·'항상'·'다음' 같은 시간 조건으로 끝이 있는 로봇 임무를 명세하는 데 쓰인다. | 12, 24, 44, 54 | ref-1399, ref-1400 |
| new | 작업 의존 그래프 | Task Dependency Graph (Dependency DAG) | 하위 작업을 노드로, 먼저 끝나야 하는 선행 관계를 방향 간선으로 둔 방향 비순환 그래프로, 로봇 행동 단위인 '행동 의존 그래프(ADG)'와 달리 하위 작업 단위이며 '선후 제약'을 표현하고 실행기는 위상 순서대로 의존이 풀린 작업부터 실행한다. | 12, 24, 26 | ref-059 |
| new | 워크플로 다이어그램 | Workflow Diagram (Open-RMF 상호운용 관심 그룹 제안) | Open-RMF 진영이 제안한, 그래픽 다이어그램으로 나타낼 수 있는 워크플로를 사람이 읽을 수 있는 JSON 스키마로 정의한 형식으로, 행동 트리로 표현하기 어려운 분기·동기화·순환을 담고 실행 전에 빌드 오류를 검사한다. crossflow 와의 관계는 미확인이다. | 12, 24 | ref-1403, ref-1404 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-1391 | Göbel, K., Lorang, P., Staderini, V., & Zips, P. (AIT Austrian Institute of Technology, IFAC PapersOnline 59(18)) | Integrating LLMs and Classical Planning for Pallet Logistics: A Case Study | 논문 | medium | https://publications.ait.ac.at/de/publications/integrating-llms-and-classical-planning-for-pallet-logistics-a-ca/ |
| ref-1392 | Chen, Y., Arkin, J., Zhang, Y., Roy, N., & Fan, C. (MIT, ICRA 2024) | Scalable Multi-Robot Collaboration with Large Language Models: Centralized or Decentralized Systems? | 논문 | high | https://arxiv.org/abs/2309.15943 |
| ref-1393 | Research Square 프리프린트(저자 미확인) | An Intelligent Warehouse Execution Framework Integrating SAP Extended WarehouseManagement, Large Language Models, SAP Business Technology Platform, and Autonomous Mobile Robots | 논문 | low | https://www.researchsquare.com/article/rs-10351090 |
| ref-1394 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/event_description__sequence.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__sequence.json |
| ref-1395 | NVIDIA (nvidia-isaac GitHub) | isaac_mission_dispatch — README | 오픈소스 문서 | high | https://github.com/nvidia-isaac/isaac_mission_dispatch |
| ref-1396 | NVIDIA (nvidia-isaac GitHub) | isaac_mission_control — README | 오픈소스 문서 | medium | https://github.com/nvidia-isaac/isaac_mission_control |
| ref-1397 | PlanSys2 (ROS 2 Planning System 프로젝트) | PlanSys2 Design | 오픈소스 문서 | high | https://plansys2.github.io/design/index.html |
| ref-1398 | Xu, S., Luo, X., Huang, Y., Leng, L., Liu, R., & Liu, C. | Nl2Hltl2Plan: Scaling Up Natural Language Understanding for Multi-Robots Through Hierarchical Temporal Logic Task Representation | 논문 | medium | https://arxiv.org/abs/2408.08188 |
| ref-1399 | Luo, X., & Liu, C. (IEEE Transactions on Robotics 2025 게재 예정 표기) | Simultaneous Task Allocation and Planning for Multi-Robots under Hierarchical Temporal Logic Specifications | 논문 | medium | https://arxiv.org/abs/2401.04003 |
| ref-1400 | Neupane, A., Mercer, E. G., & Goodrich, M. A. (AAMAS 2023 ARMS 워크숍) | Designing Behavior Trees from Goal-Oriented LTLf Formulas | 논문 | medium | https://arxiv.org/abs/2307.06399 |
| ref-1401 | Keramat, F., Salimi, S., & Westerlund, T. | Decentralized Intent-Based Multi-Robot Task Planner with LLM Oracles on Hyperledger Fabric | 논문 | medium | https://arxiv.org/abs/2602.08421 |
| ref-1402 | Choe, D. B., Sangeetha, S. V., Emanuel, S., Chiu, C.-Y., Coogan, S., & Kousik, S. | Seeing, Saying, Solving: An LLM-to-TL Framework for Cooperative Robots | 논문 | medium | https://arxiv.org/abs/2505.13376 |
| ref-1403 | Open Source Robotics Alliance Interoperability SIG, Open Robotics Discourse | Interoperability Interest Group August 01, 2024: Multi-Agent Process Workflows | 오픈소스 문서 | medium | https://discourse.openrobotics.org/t/interoperability-interest-group-august-01-2024-multi-agent-process-workflows/38794 |
| ref-1404 | Open Source Robotics Alliance Interoperability SIG, Open Robotics Discourse | Interoperability Interest Group June 5, 2025: Execution of Workflow Diagrams | 오픈소스 문서 | medium | https://discourse.openrobotics.org/t/interoperability-interest-group-june-5-2025-execution-of-workflow-diagrams/44032 |
| ref-1405 | Open Robotics (open-rmf GitHub) | crossflow — README | 오픈소스 문서 | high | https://github.com/open-rmf/crossflow |
| ref-413 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/task_new.html |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-181 | Shi, G., Wu, Y., Kumar, V., & Sukhatme, G. S. | PIP-LLM: Integrating PDDL-Integer Programming with LLMs for Coordinating Multi-Robot Teams Using Natural Language | 논문 | medium | https://arxiv.org/abs/2510.22784 |
| ref-059 | Wang, Y. 외(DART-LLM 저자) | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 논문 | medium | https://arxiv.org/abs/2411.09022 |
| ref-780 | 강건·강서연·배정찬(KAIST, 대한산업공학회 추계학술대회 논문집) | 제조 물류 로봇에서의 대규모 언어 모델(LLM)을 활용한 로봇 협업 인터페이스 구축 | 논문 | medium | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11609734 |
| ref-170 | Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. | IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models | 논문 | medium | https://arxiv.org/abs/2603.02669 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 로봇 관제 인터페이스(VDA 5050 주문, Open-RMF 작업 요청)에 작업 사이 의존·대안 경로·기한을 표현하는 확장 제안이나 차기 판 논의가 있는가? (관련 기존 질문: oq-049, oq-137) | 20, 21, 24 | 열림 | — |

## 현장 유형 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| NVIDIA Isaac Mission Dispatch | 오픈소스 | NVIDIA (nvidia-isaac) | 12, 20, 24 | ref-1395 | https://github.com/nvidia-isaac/isaac_mission_dispatch |
| NVIDIA Isaac Mission Control | 오픈소스 | NVIDIA (nvidia-isaac) | 12, 20, 23 | ref-1396 | https://github.com/nvidia-isaac/isaac_mission_control |
| PlanSys2 (ROS 2 Planning System) | 오픈소스 | PlanSys2 프로젝트 | 12, 24, 26 | ref-1397 | https://plansys2.github.io/design/index.html |
| crossflow | 오픈소스 | Open Robotics (open-rmf) | 12, 24 | ref-1405 | https://github.com/open-rmf/crossflow |

## 추가 조사 요청

- 단계 1. 선행 연구·제품 사례 조사 페이지 본문이 원래 입력에 없어 재실행에서는 이전 초안(pages/…)을 기준으로 2·5·6·9절을 replace 로 고쳤다. 퍼블리셔 점검에서 2절 도입 문단·6절 완료 조건 표·9절 이력 표가 원본 페이지와 맞는지 확인이 필요하다.
- 단계 2 완료 조건 2 를 채우려면 업무 분해·배정 설계 초안의 작업 요구 적재물 속성(적재물 식별·유형·치수·중량)과 업무 완료 조건의 표현 원천(작업 상태 스키마·EPCIS 이벤트) 근거가 필요하다(q2-05·q2-06·q2-07).
- q2-04 답의 보강: Open-RMF 플릿 어댑터 schemas 디렉터리 전체에서 병렬·분기 활동 범주 유무, 워크플로 다이어그램 JSON 스키마 원문과 차세대 Open-RMF 와의 공식 관계, 의존 DAG 잎 단위 송출을 물류 플릿에 적용한 사례가 필요하다.
- 단계 1 q1-05 물류창고 사례(SAP EWM 연동 프리프린트)의 원문 열람으로 저자·게시일·제약·예외 처리·정량 결과·실제 운영 여부를 확인해야 여섯 항목 중 제약·예외·성과 칸을 채우고, 세부영역 페이지 5절 반영 때 현장 유형 매트릭스에 올릴 수 있다.
- 국내 물류 자연어 로봇 지시 근거(oq-142): KAIST 2023 대한산업공학회 발표의 초록·본문 확인이 필요하다.
- Chen 외 Warehouse 시나리오의 로봇 수별 성공률 수치, IMR-Bench·SkillChain-RTD 의 규모·정답 형식·공개 여부가 확인되면 q1-06·q5-20 답을 보강할 수 있다.
- 파이프라인 담당 요청: 참고문헌 id ref-1397~ref-1405 가 실행 2026-10-09-23 의 다른 출처와 겹치는지 등록 전에 확인하고, 충돌하면 새 id 를 부여해 단계 2 페이지·업무 분해·배정 설계 초안·아이디어 2 페이지의 각주·프런트매터 sources·reference_updates 를 함께 바꿔야 한다.
- 트랙 정의 담당 요청: 트랙 개요 상태 줄(단계 2)과 자동 진행 표·config/tracks/chat-based-configuration-and-operation.yaml 의 current_stage(1)가 다르므로 current_stage 값을 확인해야 한다.

## 이행한 수정 지시

- 참고문헌 id 충돌 — 브리프 id 를 그대로 쓰고, reference_updates 의 ref-1397~ref-1405 summary 끝에 '참고문헌 id 충돌 확인 필요' 비고를 넣었으며 additional_research_requests 에 파이프라인 담당 확인 요청을 적었다.
- f5 문구 — 단계 1 q1-05 소절·아이디어 2 페이지 3절에서 'MILP 로 후보 도우미마다 경로·시간 비용을 계산하고 요청 로봇이 가장 낮은 비용의 제안을 고르는', '최근접 로봇 선택 대비 약 26% 효율 향상'으로 쓰고 '저자 보고, 시뮬레이션, 동료심사 게재처 미확인'을 병기했다(25. 작업 배정 — MRTA 반영 제안도 같은 문구).
- f6 문구 — 단계 1 q1-05 와 아이디어 2 페이지 3절에서 '산업 시나리오의 엄격한 순서 제약과 복잡한 의존이 가정·조작 과제와 다른 새로운 도전이라고 본다'로 썼다.
- f9 문구 — (2)를 '공간 추론과 긴 계획이 필요한 과제(팔레트 물류)와 엄격한 순서 제약이 있는 과제(산업 제조)에서'로 고치고 [추정]·이 위키의 종합 표시를 유지했다(단계 1 q1-05, 아이디어 2 페이지 3절).
- f12 — 'VDA 5050 공식 저장소의 주문 스키마(main 브랜치, 3.0.0 판, 확인일 2026-10-09)'로 판·기준일을 밝혔고, 기한·우선순위 부재(f12·f15)는 단계 2 페이지 #q2-01, deps 범위(f14)는 #q2-02 를 가리키게 하고 기존 각주 ref-413·ref-125·ref-111 을 재사용했다.
- f7 — 단계 1 q1-05 에서 '동료심사 전 프리프린트의 시제품 구조(원문 미열람, 실제 창고 운영 여부 미확인)'로 밝히고 SAP EWM 은 분류 원문 19장의 상위 업무 시스템(연계 대상), ROP 몫은 작업 수신과 완료 확정 반영이라고 적었으며, 물류창고 사례 표에서 제약·예외·성과를 '미확인'으로 두고 검색 요약 밖 수치를 넣지 않았다. 각주 접근일 뒤에 ' (원문 미열람)'을, reference_updates 의 ref-1393 에 source_unopened: true 를 넣었고 12. 채팅으로 업무 지시·오케스트레이션·61. 물류창고 반영 제안에도 같은 조건을 적었다.
- f8 — '2023-11 대한산업공학회 추계학술대회 논문집(75–89쪽)에 KAIST 강건·강서연·배정찬이 발표(서지 기준, 내용 미확인)' 수준의 [추정]으로만 썼고, 각주 기관 칸에 세 저자와 KAIST 를 적고 ' (원문 미열람)'을 붙였으며 ref-780 에 source_unopened: true 를 넣었다. 제조 공장 사례로 사례 절·site_matrix_updates 에 넣지 않았다.
- f16·f17·f19·f20·f5 범위 — 단계 2 q2-04 와 아이디어 2 페이지 4절에 로봇 쪽 주행·행동·스킬 실행을 '연계 대상: 로봇 자체 지능·제어'로 짧게 적고, ROP 설계 근거는 주문·작업 요청으로 내보내는 경계와 위상 순서 집행 구조로 한정했다. f5 의 VLM 충돌 감지·지게차 주행도 단계 1 q1-05 에서 연계 대상으로 적었다.
- f18 — Isaac Mission Control 서술을 모든 페이지에서 '[추정] 벤더 주장'으로 쓰고 SAP EWM 작업 변환을 사실로 서술하지 않았다.
- f24~f26·f30 — 근거가 Open Robotics Discourse 포럼 공지(작성자 grey)와 crossflow README 임을 단계 2·초안·아이디어 2 페이지 본문에 밝히고, README 가 워크플로 다이어그램·차세대 Open-RMF 와의 관계를 서술하지 않아 crossflow 를 그 구현으로 단정하지 않는다고 적었다.
- 용어집 — '워크플로 다이어그램' 영문 칸을 'Workflow Diagram (Open-RMF 상호운용 관심 그룹 제안)'으로 쓰고 정의 끝에 crossflow 와의 관계 미확인을 적었으며, LTLf 는 기존 용어 '선형 시간 논리'(linear-temporal-logic)에, '작업 의존 그래프'는 '행동 의존 그래프'(action-dependency-graph)·'선후 제약'(precedence-constraint)에 설명 링크로 연결했다.
- ref-110 각주 — 참고문헌 색인의 형식 그대로 '[^ref-110]: Open Robotics, Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-25'로 단계 2 페이지·아이디어 2 페이지에 썼다.
- 단계 1 페이지 — 3절에 '### q1-05 … {#q1-05}'와 '### q1-06 … {#q1-06}' 두 소제목을 두고(q1-06 은 q1-05 를 가리키고 f10·f11 만 더함), 2절 표의 두 질문을 답함(2026-10-09-25, #q1-05·#q1-06)으로 바꾸었으며, 두 답의 신뢰도 low 와 '실제 물류센터 운영 평가는 확인하지 못함'을 명시했다.
- 단계 2 페이지 — 2절 표의 q2-04 를 답함(2026-10-09-25, #q2-04)으로 바꾸고 3절에 '### q2-04 … {#q2-04}' 소절을 두었으며, 중간 표현별 대응표가 이 위키의 구성이고 출처 표를 옮긴 것이 아니라고 적고 [추정](f27~f30)으로 표시했다. 상태 줄을 '열린 질문: 3건 · 답한 질문: 4건'으로 맞췄다.
- 단계 2 페이지 6절 — 완료 조건 1 충족, 완료 조건 2 미충족, 아래 줄 '다음 단계로 전환: 아니오(작업 요구 적재물 속성·완료 조건 미확정, 열린 질문 q2-05·q2-06·q2-07)'로 쓰고 상태 줄 단계 상태 '진행 중', 완료 조건 '미충족'으로 두었다(검증 판정 칸은 2차 지시에 따라 행별로 정리).
- 트랙 개요 — 머리말 패치로 상태 줄을 '현재 단계: 단계 2. 필요한 데이터와 표준 조사 · 마지막 트랙 실행: 2026-10-09'로 고쳤고, 6절의 '현재 단계는 단계 3 으로 둔다' 문장들은 지우지 않고 각 실행 시점 기준임을 밝히는 항목을 덧붙였다.
- 온톨로지 변경 — 작업(Task) 행의 속성 '선후관계'를 '선후관계(작업 사이 선행 의존; 표현 형식 후보: 의존 그래프)'로 고치고, 외부 표현 메모로 f12·f14·f16·f20 을 [사실]로, '작업 사이 의존은 작업 모델이 보유하고 잎 작업만 내보내는 구성이 선택지로 보인다'를 [추정](f27) 메모로 적었다. 관계는 추가하지 않았고 상태는 확정을 유지했다.
- 초안 6절 — '작업 사이 선행 의존을 관계로 드러낼 것인가' 질문은 닫지 않고 q2-04 답 링크(stage-2-data-and-standards.md#q2-04, f27·f28)를 덧붙였으며, 'LTL 계열을 명세 검사층으로 둘 것인가'(f29, 관련: q4-14, oq-302, oq-314)와 '작업 사이 제어 흐름을 행동 트리·의존 DAG·워크플로 다이어그램 가운데 무엇으로 보관할 것인가'(f30) 질문을 더했다.
- 초안 버전 — 프런트매터 ontology_version·H1 '(v1.0)'·track_updates.ontology_draft_version 을 '1.0'으로 맞추고, 1절과 log_entry 의 온톨로지 변경(버전 이력 행 내용)에 '1.0 은 0.1 증가 규칙에 따른 번호이며 완성판을 뜻하지 않는다'를 적었다.
- 아이디어 2 페이지 — 3절의 'G3뿐이었다' 문장은 지우지 않고, 3절 끝에 그 서술이 (실행 2026-09-25 기준)임을 밝히는 갱신 소절을 덧붙여 실행 2026-10-09-25 의 물류·산업 지향 연구(f1~f6, 모두 시뮬레이션·도메인 실험·초록 수준)와 EWM 연동 시제품 프리프린트(f7, 원문 미열람)를 적었다(f9·f11 은 [추정]). 4절에 '중간 표현과 로봇 관제 인터페이스 대응' 소절을 더하고 결론(f27~f30)을 [추정]으로 썼다.
- 세부영역 반영 — 12. 채팅으로 업무 지시·오케스트레이션, 24. 작업·워크플로 모델링, 25. 작업 배정 — MRTA, 61. 물류창고 페이지는 직접 고치지 않고 area_reflection_proposals 와 트랙 로그의 '세부영역 반영 제안'으로만 남겼다. 12 제안에 5절 '물류창고·제조 공장·상업 시설 사례 확인되지 않음' 문장 갱신 필요(f7)를, 25 제안에 f5 가 시뮬레이션·프리프린트 조건의 저자 보고임을 적고, 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링을 함께 연결했다.
- open_question_updates — 새 열린 질문의 question 에서 필드 문자열을 떼고 끝에 '(관련 기존 질문: oq-049, oq-137)'을 남겼으며 areas 를 [20, 21, 24]로 두었다.
- 새 백로그 질문 — 세 건을 브리프의 단계(3·4·5)와 관련 표기(q3-08·q3-15 / q2-05·q4-07 / q5-04)를 그대로 쓴 질문 문장으로 q3-17·q4-20·q5-20 id 를 붙여 내고 origin 을 각각 f17·f4·f11 로 두었다.
- 2차: 단계 1 페이지 프런트매터 — 머리말 패치의 frontmatter 에 sources 를 넣어 기존 목록에 ref-1391, ref-1392, ref-1393, ref-1401, ref-1402, ref-780 을 더했다.
- 2차: 단계 1 페이지 2절 도입 문단 — 'q1-01은 사용자 요청의 시작 질문 문구 그대로이고, q1-02~q1-04는 구축자가 이 단계의 밝힐 것에서 정한 시작 질문이다. [가정]'으로 되돌리고, q1-05·q1-06 은 되돌아온 질문으로 뜻이 겹치며 실행 2026-10-09-25 에서 둘 다 답했다는 문장으로 바꿨다.
- 2차: 단계 1 페이지 5절 — replace 패치로 기존 후속 질문 표의 q1-05 행 상태를 '답함'으로 고치고, 아래 서술에 q1-05 가 실행 2026-10-09-25 에서 답해졌다는 문장을 더했다(q4-20·q5-20 표는 유지).
- 2차: 단계 1 페이지 6절 — replace 패치로 표 아래 줄을 '다음 단계로 전환: 아니오(지시 분해 접근 유형 목록이 업무 분해·배정 설계 초안에 미반영)'로 고쳤다.
- 2차: 단계 1 페이지 9절 — replace 패치로 따로 붙였던 '실행 2026-10-09-25 이력:' 표를 없애고, 기존 이력 표 맨 위에 '| 2026-10-09 | 2026-10-09-25 | q1-05, q1-06(같은 실행에서 단계 2 의 q2-04 도 답함) | q4-20, q5-20 | v0.9 → v1.0(단계 2 q2-04 근거) | 6 |' 행을 넣었다.
- 2차: 단계 2 페이지 6절 — 첫 행(완료 조건 1)의 검증 판정 칸을 '충족 · 미승인'으로 고쳤고, 완료 조건 2 행('미충족 · 미승인'), 아래 전환 줄, 상태 줄은 그대로 두었다.
- 2차: site_matrix_updates — 트랙 단계 페이지를 가리키던 물류창고 네 항목을 지우고 빈 배열로 두었다. 이 사례는 area_reflection_proposals 의 12. 채팅으로 업무 지시·오케스트레이션·61. 물류창고 반영 제안을 거쳐 세부영역 페이지 5절에 반영될 때 매트릭스에 올린다.

## 트랙 갱신

- 단계 페이지: docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md
- 온톨로지 초안 버전: 1.0
- 트랙 로그 항목: 답한 질문: q1-05(물류·산업 지향 LLM 작업 분해 연구와 가정→물류 차이, 신뢰도 low, 단계 1 #q1-05), q1-06(물류 지시–작업 데이터셋 미발견, 신뢰도 low, 단계 1 #q1-06), q2-04(중간 표현과 VDA 5050 주문·Open-RMF 작업 요청 대응, 신뢰도 low, 단계 2 #q2-04) — 되돌아온 단계 1 질문이 답해져 단계 1 의 재개 사유 해소 / 새 질문: q3-17(f17), q4-20(f4), q5-20(f11) / 온톨로지 변경: v0.9 → v1.0: 개념 '작업 (Task)' 속성 '선후관계'를 '선후관계(작업 사이 선행 의존; 표현 형식 후보: 의존 그래프)'로 정리하고 외부 표현 메모 추가(f12·f14·f16·f20 사실, 잎 단위 송출 구성은 f27 추정 메모), 관계 추가 없음, 상태 확정 유지, 초안 6절 '선행 의존을 관계로 드러낼 것인가' 질문 유지 및 질문 2건 추가(f29 LTL 검사층, f30 제어 흐름 보관 형식), 근거 실행 2026-10-09-25 — 1.0 은 0.1 증가 규칙에 따른 번호이며 완성판을 뜻하지 않는다 / 완료 조건 평가: 미충족(부족: 업무 분해·배정 설계 초안 개념 목록 표의 작업 요구 적재물 속성·완료 조건 미확정, 막힌 질문 q2-05·q2-06·q2-07; 검증 판정 미충족·전환 미승인) / 세부영역 반영 제안: 12. 채팅으로 업무 지시·오케스트레이션 3건(5·6·7절), 24. 작업·워크플로 모델링 1건, 25. 작업 배정 — MRTA 1건, 61. 물류창고 1건(교차 규칙 44. 로봇 기반 모델·언어 모델 계획, 47. AI·학습·적응과 모델 운영, 26. 작업 순서·스케줄링 연결) / 다음 실행 제안: q2-05, q2-06, q2-07(단계 2 완료 조건 2 관련)
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 3, 답함 4, 완료 조건 미충족 (되돌아온 단계 1 질문 q1-05·q1-06 답함으로 단계 1 열린 질문 0, 업무 분해·배정 설계 초안 v1.0)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-05 | 답함 | docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md#q1-05 | — | — | — |
| q1-06 | 답함 | docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md#q1-06 | — | — | — |
| q2-04 | 답함 | docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md#q2-04 | — | — | — |
| q3-17 | 열림 | — | 행동 트리의 selector 같은 대안 경로나 Open-RMF 워크플로 다이어그램의 분기·동기화 같은 제어 흐름을 VDA 5050 주문(한 줄 노드–간선)과 Open-RMF 순차 단계로 옮길 때, ROP 는 그 흐름을 자체 실행기에 두고 잎 작업만 주문·작업 요청으로 하나씩 내보내야 하는가, 그때 제어 흐름 변경에 따른 취소·재제출 비용과 로봇 이동 연속성은 어떻게 되는가? (q2-04 에서 파생) (관련: q3-08, q3-15) | 3 | f17 |
| q4-20 | 열림 | — | PIP-LLM 에서 오탈자가 새 품목·새 선반으로 해석된 것처럼, 물류 지시 속 품목 코드·선반·도크 식별자의 표기 오류를 이름 사전과 대조해 정규화할지 되물을지 정하는 기준은 무엇인가? (q1-05 에서 파생) (관련: q2-05, q4-07) | 4 | f4 |
| q5-20 | 열림 | — | 팔레트 물류 PDDL 도메인(IFAC 2025), PIP-LLM 창고 과제 10개, 창고 동기 지게차 도움 요청 시뮬레이션 같은 과제 집합이 공개되어 있어 물류 지시 평가 자료의 출발점으로 쓸 수 있는가? (q1-06 에서 파생) (관련: q5-04) | 5 | f11 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 12 | 5. 적용 사례 (현장 유형 명시) | 5절 '물류창고·제조 공장·상업 시설에서 대화로 로봇 업무를 지시한 사례는 확인되지 않았다' 문장의 갱신 필요(f7, 실행 2026-10-09-25): 물류창고 사례 후보로 SAP EWM 연동 시제품(동료심사 전 프리프린트의 시제품 구조, 원문 미열람, 실제 창고 운영 여부 미확인 — 자연어 명령→LLM→EWM 창고 작업→자율이동로봇, QR 저장 칸 확인 뒤 EWM 확정). SAP EWM 은 분류 원문 19장의 상위 업무 시스템(연계 대상)이며 ROP 몫은 작업 수신과 완료 확정 반영. 여섯 항목 가운데 제약·예외·성과는 미확인, 검색 요약 밖 수치 금지. 반영 때 현장 유형 매트릭스(물류창고 × 시작 조건·작업 대상·수행 자원·완료·인계)에 올린다. 국내 사례(oq-142)는 KAIST 2023 학술대회 서지만 확인되어 미해결. |
| 12 | 6. 대표 접근법과 기술 | 의존 DAG(DART-LLM, f20)를 작업 모델에 두고 잎 작업만 Open-RMF 작업 요청·VDA 5050 주문으로 하나씩 내보내며 의존·순서는 ROP 실행기가 보유하는 구성(f27, 추정)과, 옮길 때 빠지는 항목(작업 사이 의존·대안 경로·기한·지시 원문·배정 근거·확인 여부, f28 추정). 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 짝 엔진 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링을 함께 연결. |
| 12 | 7. 관련 표준·프레임워크·오픈소스 | NVIDIA Isaac Mission Dispatch(행동 트리 잎별 VDA 5050 주문 송출, 구조 변경은 취소·재제출, f16·f17), PlanSys2(PDDL 계획→계획 그래프→행동 트리 실행, f19), Isaac Mission Control(SAP EWM 작업 변환 등은 [추정] 벤더 주장, f18). 로봇 쪽 주행·행동 실행은 로봇 자체 지능·제어의 연계 대상으로 짧게. |
| 24 | 7. 관련 표준·프레임워크·오픈소스 | 행동 트리 임무를 VDA 5050 주문으로 옮기는 Isaac Mission Dispatch(f16), PDDL 계획을 행동 트리로 실행하는 PlanSys2(f19), 의존 DAG(DART-LLM, f20), LTLf→행동 트리 변환(f23), 분기·동기화·순환을 표현하는 Open-RMF 진영 워크플로 다이어그램(f24·f25, Open Robotics Discourse 포럼 공지 근거)과 crossflow README(f26, 워크플로 다이어그램의 구현으로 단정하지 않음). |
| 25 | 8. 대표 연구와 자료 | 핵심 질문 '가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가?'와 관련해 Choe 외(arXiv 2505.13376): 창고 동기 지게차 6대 격자 시뮬레이션 100회에서 MILP 로 후보 도우미마다 경로·시간 비용을 계산하고 요청 로봇이 최저 비용 제안을 고른 시스템 전체 영향 기준 선택이 최근접 로봇 선택 대비 약 26% 효율 향상, 최근접 선택이 최적과 일치한 비율 42%(저자 보고, 시뮬레이션·프리프린트 조건, 동료심사 게재처 미확인, f5). 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획과 연결. |
| 61 | 6. 대표 접근법과 기술 | 물류·창고 지시를 다룬 LLM 작업 분해 연구(팔레트 물류 PDDL 하이브리드 f1, 창고 격자 시나리오 f2, PIP-LLM Gazebo 창고 과제 f3, 창고 동기 지게차 도움 요청 f5 — 모두 시뮬레이션·도메인 실험 조건 저자 보고), SAP EWM 연동 시제품(f7, 동료심사 전·원문 미열람, 실제 운영 여부 미확인), 공개 물류 지시–작업 데이터셋 미발견(f11, 추정·부재 확인 아님). |
