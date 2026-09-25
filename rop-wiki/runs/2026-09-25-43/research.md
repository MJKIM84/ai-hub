# 리서치 브리프 2026-09-25-43

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-43 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 13. 작업 배정 — MRTA |
| 대분류 | D. 계획·최적화 |

트랙 실행: 트랙 `nl-task-chatbot` · 단계 2 · 답한 질문 q2-02

## 갭(비어 있거나 약한 섹션)

- 단계 2 질문 q2-02 열림(target.json 지정, CLI 지정 질문 id). 단계 2 페이지 3절에 q2-02 소제목 없음
- 완료 조건: 아이디어 2. 자연어 업무 지시 챗봇 페이지 4절에 표준·형식 목록 비교 없음(q2-01 데이터 항목만 실림)
- 완료 조건: 업무 분해·배정 설계 초안의 진행 상태·배정 개념 속성이 외부 표현 형식과 대조되지 않음
- 13. 작업 배정 — MRTA 페이지 섹션 7. 관련 표준·프레임워크·오픈소스에 배정 결과(누구에게 배정했는가)를 기록하는 형식 근거 없음

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. q2-02 분해한 작업과 배정 결과를 표현하는 기존 표준·형식(작업·미션 기술, 워크플로 기술)은 무엇이 있고, ROP의 작업 모델에 비해 무엇이 빠지는가?
3. 로봇 관제 쪽 형식(Open-RMF 복합 작업·작업 상태, VDA 5050 주문, MassRobotics 상태 보고)은 작업의 단계 구조와 배정 결과를 어떤 필드로 표현하는가? (단계 2 페이지 3절, 13. 작업 배정 — MRTA 섹션 7 겨냥)
4. 업무·워크플로 쪽 형식(ISA-95 작업 지시·작업 응답, BPMN 2.0 수행자, Serverless Workflow)은 작업 구조·수행 자원·기한을 어떻게 표현하는가? (1. 주문·업무 시스템 연계, 2. 공정·워크플로 모델링 연결)
5. 로봇 계획·실행 표현(HDDL 계층 작업 네트워크, 행동 트리 XML)은 분해 구조와 순서를 어떻게 기술하고, 로봇 임무 기술에 합의된 표준 형식이 있는가? (14. 작업 순서·스케줄링 연결)
6. 서로 다른 로봇·플릿의 작업 선후를 표준 형식 안에서 표현·집행할 수단이 있는가? (oq-049 관련)
7. 국내에 로봇 작업·임무 기술 형식을 정한 KS 표준이나 연구가 있는가? (한국 자료 우선 규칙)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 복합(compose) 작업 기술 스키마는 순서가 있는 단계(phases) 배열을 유일한 필수 필드로 두고, 각 단계는 활동(activity: 범주와 플릿이 지원하는 스키마에 맞는 기술)을 필수로, 취소 시 실행할 활동 목록(on_cancel)을 선택으로 두며, 한 단계 안의 여러 활동은 Sequence 활동으로 묶게 한다. | ref-569 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | Open-RMF 작업 상태 스키마는 예약 정보(booking)만 필수로 두고, 배정 결과를 로봇 그룹(플릿)과 이름으로 된 assigned_to 필드로, 배정 과정을 queued·selected·dispatched·failed_to_assign·canceled_in_flight 값의 dispatch 상태로, 진행을 uninitialized·blocked·queued·underway·delayed·completed·canceled·failed 등의 status 값과 단계별 상태·예상 소요 시간으로 표현한다. | ref-111 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f3 | [추정] | 이번에 연 Open-RMF 복합 작업·작업 상태 스키마에서는 배정 결과가 '어느 로봇인가'만 기록되고 배정 근거(선택 이유·산출 방식)·사용자 확인 여부·다른 작업과의 선행 의존을 담는 필드는 확인되지 않아, 이 항목은 ROP 의 작업 모델이 따로 보유해야 할 것으로 보인다. | ref-569, ref-111 | 아니오 | low | 2026-09-25 | — | — |
| f4 | [사실] | VDA 5050 3.0.0 은 관제의 최소 기능으로 주문의 이동로봇 배정을 두지만, 주문 자체는 로봇 한 대가 지나갈 노드–간선 그래프 구간이며 전체 운반 작업은 orderId·orderUpdateId 로 이어진 여러 하위 주문으로 나뉠 수 있어, 업무·작업 수준의 구조나 배정 근거를 담는 메시지는 두지 않는다. | ref-031 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f5 | [사실] | VDA 5050 3.0.0 의 사전 정의 동작 waitForTrigger 는 이동로봇이 관제(FLEET_CONTROL)나 로봇 자체 입력(LOCAL)의 트리거를 기다리게 하고, 관제는 제3 시스템에서 기다리던 과정이 끝났다는 정보를 받으면 순간 동작 trigger 로 이를 풀며, 시간 초과 처리와 주문 취소는 관제가 맡는다. | ref-031 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f6 | [사실] | MassRobotics AMR 상호운용 표준의 JSON 스키마는 로봇이 내보내는 식별 보고와 상태 보고만 정의하고 로봇에 작업을 보내는 메시지는 두지 않으며, 상태 보고에 운용 상태(navigating, idle, charging, waitingHumanEvent 등)와 목적지(destinations)·단기 경로를 담는다. | ref-230, ref-253 | 아니오 | medium | 2026-09-25 | — | — |
| f7 | [사실] | OPC UA for ISA-95 작업 제어 노드셋의 작업 응답 데이터형은 작업 응답 id·연결된 작업 지시 id·실제 시작·종료 시각·작업 상태와 인원·설비·물리 자산·자재의 실적(Actuals)을 두고, 설비 데이터형의 ID 는 설비 클래스 또는 개별 설비를 가리킬 수 있다. | ref-130 | 아니오 | medium | 2024-01-31 | 완료·인계 | — |
| f8 | [추정] | 이번에 연 ISA-95 작업 제어 노드셋의 작업 지시·작업 응답 데이터형에서는 작업 지시 사이의 선행·의존 관계를 담는 필드가 확인되지 않았다. | ref-130 | 아니오 | low | 2026-09-25 | — | — |
| f9 | [사실] | OMG BPMN 2.0.2 명세는 활동을 수행하거나 책임지는 자원을 수행자(Performer, 10.3.2절)로 정의하고, 사람 수행자(HumanPerformer)와 잠재 담당자(PotentialOwner) 같은 특수화와 자원 배정 식(resourceAssignmentExpression)으로 활동을 맡을 자원을 지정하게 한다. | ref-573 | 아니오 | medium | 2014-01 | 수행 자원 | 원문 미열람 |
| f10 | [사실] | Corradini 외(2023)는 BPMN 2.0 협업 다이어그램으로 다중 로봇 시스템의 협력 행동을 모델링·설정·실행하는 틀을 제안했다. | ref-114 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f11 | [사실] | CNCF 의 Serverless Workflow(Open Workflow Specification) DSL 1.0.x 는 YAML·JSON 으로 워크플로를 기술하며 call·do(순차)·fork(병렬)·switch·wait·emit·listen·raise·try·set·run 같은 작업 유형과 시간 초과·일정(cron·every·after) 표현을 둔다. | ref-570 | 아니오 | medium | 2026-09-25 | — | — |
| f12 | [추정] | 이번에 연 Serverless Workflow DSL 문서에서는 작업을 특정 수행자·자원에 배정하거나 우선순위·기한을 표현하는 개념이 확인되지 않았다. | ref-570 | 아니오 | low | 2026-09-25 | — | — |
| f13 | [사실] | BehaviorTree.CPP 는 행동 트리를 실행 시 불러오는 XML 기반 도메인 특화 언어로 정의하고, 사용자 정의 노드를 정적으로 링크하거나 플러그인으로 불러오며, 비동기 동작을 기본으로 지원한다. | ref-571 | 아니오 | medium | 2026-09-25 | — | — |
| f14 | [사실] | HDDL(Höller 외, AAAI 2020)은 PDDL 을 확장해 기본 작업·복합 작업과 복합 작업을 하위 작업 네트워크로 나누는 분해 방법, 하위 작업의 부분·전체 순서를 기술하는 계층적 작업 네트워크(HTN) 계획 언어로, 2020년 국제 계획 경진대회 계층 계획 부문의 공통 언어로 만들어졌다. | ref-572 | 아니오 | medium | 2019-11 | — | 원문 미열람 |
| f15 | [의견] | Filippone 외(2026)는 단일·다중 로봇 시스템의 임무 기술에 표준이나 널리 합의된 형식이 없고, 행동 트리·상태 기계·계층적 작업 네트워크·BPMN 이 정도를 달리하며 쓰인다고 평가한다. | ref-116 | 아니오 | medium | 2026-03 | — | 원문 미열람 |
| f16 | [추정] | q2-02 에 대해 이번에 확인한 형식을 업무 분해·배정 설계 초안과 대조하면, 로봇 관제 형식(Open-RMF, VDA 5050)은 작업 단계·배정 결과·진행 상태를, 업무 형식(ISA-95 작업 지시·응답)은 기한·우선순위·자원 요구·실적을, 워크플로 형식(BPMN, Serverless Workflow)과 계획 언어(HDDL, 행동 트리)는 분해·순서 구조를 담지만, 지시 원문과 상황 값의 출처, 배정 근거·산출 방식, 사용자 확인 여부를 함께 담는 형식은 찾지 못해 ROP 는 이 항목을 자체 작업 모델에 두고 외부 형식으로 옮겨야 할 것으로 보인다. | ref-569, ref-111, ref-031, ref-130, ref-573, ref-570, ref-572, ref-571 | 아니오 | low | 2026-09-25 | — | — |
| f17 | [추정] | 확인한 형식 가운데 서로 다른 로봇·플릿 작업 사이의 선행 의존을 필드로 표현하는 것은 없었고, VDA 5050 의 waitForTrigger–trigger 처럼 관제가 다른 과정의 완료를 받아 로봇을 풀어 주는 동작이 플릿 사이 동기화 수단으로 쓰일 수 있어 보이나, 그 집행은 관제(ROP) 몫으로 남는다. | ref-031, ref-569, ref-130 | 아니오 | low | 2026-09-25 | 피킹 / 제약 | — |
| f18 | [추정] | 분류 원문 질문(가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가)과 관련해, 표준 형식의 배정 결과(Open-RMF assigned_to·dispatch 상태, ISA-95 설비 실적)는 누가 맡았는지만 남기므로, 최근접 배정과 다른 배정 기준의 전체 효과를 사후에 비교하려면 ROP 가 배정 근거·목적함수 값을 별도로 기록해야 할 것으로 보인다. | ref-111, ref-130 | 아니오 | low | 2026-09-25 | 예외·성과 | — |

### 근거 발췌

- **f1**: task_description__compose.json 원본(github_raw): required phases(minItems 1), phase 는 activity 필수·on_cancel 선택. 'If there should be multiple activities within a phase, then use a Sequence activity.' (발행일 미확인, 확인일 기준)
- **f2**: task_state.json 원본(github_raw): assigned_to 'Which agent (robot) is the task assigned to'(group, name 필수); dispatch status enum; status enum 12종; estimate_millis, phases. (발행일 미확인, 확인일 기준)
- **f3**: f1·f2 필드 목록에서 도출한 이 위키의 추론. 부재 관찰은 두 스키마 범위이며 rmf_task 내부 구현은 확인하지 않음(oq-049 관련).
- **f4**: VDA5050_EN.md 3.0.0 원문(inbox): 5.3 'Assignment of orders to the mobile robots'; 6.1 'An order message does not necessarily describe the full transport order'. (발행일 미확인, 확인일 기준)
- **f5**: VDA5050_EN.md 3.0.0 원문(inbox) 표 4: trigger 'Typically, this occurs when the fleet control system receives information from a third-party system indicating that the process the mobile robot was waiting for has completed.'
- **f6**: AMR_Interop_Standard.json 원본(github_raw): Identity Report·Status Report 두 유형, operationalState enum 9종, destinations 'Target destination(s) of AGV'. README 는 'tasking / availability' 공유를 목적으로 언급. 같은 발행 주체. (발행일 미확인, 확인일 기준)
- **f7**: NodeSet2.xml 원본(github_raw): ISA95JobResponseDataType JobResponseID, JobOrderID, StartTime·EndTime 'actual', JobState, EquipmentActuals 등; ISA95EquipmentDataType ID 'An identification of an EquipmentClass or Equipment'.
- **f8**: NodeSet2.xml 열람 응답 기준의 부재 관찰이며 부재 확인 아님. 세그먼트 의존은 B2MML 쪽에 있음(oq-013 관련).
- **f9**: 검색 요약: 명세 PDF 목차의 10.3.2 'Performer'; Performer 는 사람에 한정되지 않으며 PotentialOwner 는 User Task 를 맡을 수 있는 후보를 나타낸다(구현 문서 요약 포함). 원문 미열람.
- **f10**: 검색 요약: 'framework for modeling, configuring and enacting the cooperative behaviors of multi-robot systems through collaboration diagrams' (Robotics and Autonomous Systems). 원문 미열람.
- **f11**: dsl.md 원본(github_raw): 'platform-agnostic workflow orchestration', Do 'subtasks to perform in sequence', Fork 'to perform in parallel', 문서 표기 DSL 1.0.3. (발행일 미확인, 확인일 기준)
- **f12**: dsl.md 열람 응답 기준의 부재 관찰. 시간 초과는 있으나 마감 시각 개념은 확인되지 않음. 부재 확인 아님.
- **f13**: README 원본(github_raw): 'a domain specific scripting language based on XML' that 'can be loaded at run-time'; ROS 2(colcon) 빌드 지원. 다중 로봇 배정 언급 없음. (발행일 미확인, 확인일 기준)
- **f14**: 검색 요약: HDDL 'based on PDDL 2.1', IPC 2020 계층 계획 트랙용 표준 언어, compound task·method 선언, ':ordering' 절로 부분·전체 순서. 원문 미열람.
- **f15**: 검색 요약(arXiv 2603.15427v2): 'there is no standard or widely accepted formalism for specifying missions in single- or multi-robot systems'. 원문 미열람.
- **f16**: f1~f14 를 초안 2절 개념(지시·상황·업무·작업·배정·진행 상태)에 대응시킨 이 위키의 정리. 이 대응을 제시한 단일 출처는 확인하지 못함. 검색 범위의 결과이며 부재 확인 아님.
- **f17**: f3·f5·f8 에서 도출한 추론. 이를 플릿 사이 선후 집행에 쓴 사례는 확인하지 못함(oq-049 관련).
- **f18**: f2·f7 을 13. 작업 배정 — MRTA 의 SCM 질문에 대응시킨 추론. 배정 근거 기록을 권고한 출처는 확인하지 못함(oq-052 관련).

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 2024-01-31 | 표준 | medium | 2026-09-25 | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | high | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-253 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — README | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard | 예 |
| ref-114 | Corradini, F., Pettinari, S., Re, B., Rossi, L., & Tiezzi, F. | A BPMN-driven framework for Multi-Robot System development | 2023 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0921889022002111 | 예 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2603.15427 | 예 |
| ref-569 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/task_description__compose.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/task_description__compose.json | 아니오 |
| ref-570 | CNCF Serverless Workflow (serverlessworkflow/specification GitHub) | Serverless Workflow Specification — dsl.md (DSL 1.0) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/serverlessworkflow/specification/blob/main/dsl.md | 아니오 |
| ref-571 | BehaviorTree.CPP (BehaviorTree GitHub) | BehaviorTree.CPP — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/BehaviorTree/BehaviorTree.CPP | 아니오 |
| ref-572 | Höller, D., Behnke, G., Bercher, P., Biundo, S., Fiorino, H., Pellier, D., & Alford, R. | HDDL – A Language to Describe Hierarchical Planning Problems | 2019-11 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1911.05499 | 예 |
| ref-573 | OMG(Object Management Group) | Business Process Model and Notation (BPMN), Version 2.0.2 | 2014-01 | 표준 | medium | 2026-09-25 | https://www.omg.org/spec/BPMN/2.0.2/PDF | 예 |

### 출처 요약

- **ref-031**: VDA 5050 3.0.0 명세 원문. 이번 실행은 관제 기능(주문 배정), 주문 구조·하위 주문 분할, waitForTrigger·trigger 동작을 입력 원문 텍스트로 확인했다.
- **ref-111**: Open-RMF 작업 상태 스키마. 예약, 배정 대상(assigned_to), 배정 과정(dispatch) 상태, 진행 상태 값, 단계 상태, 예상 소요 시간 필드를 원문으로 확인했다.
- **ref-130**: OPC UA for ISA-95 작업 제어 노드셋. 이번 실행은 작업 응답·설비·인원 데이터형 필드를 NodeSet2.xml 원문으로 확인했다.
- **ref-230**: MassRobotics AMR 상호운용 표준 JSON 스키마. 식별 보고·상태 보고 두 메시지와 운용 상태·목적지 필드를 원문으로 확인했다.
- **ref-253**: MassRobotics AMR 상호운용 표준 저장소 README. 위치·속도·상태·작업 가용성 등 정보 공유를 목적으로 적는다.
- **ref-114**: 원문 미열람. BPMN 2.0 협업 다이어그램으로 다중 로봇 시스템의 협력 행동을 모델링·설정·실행하는 틀을 제안한 논문.
- **ref-116**: 원문 미열람. 행동 트리·상태 기계·계층적 작업 네트워크·BPMN 등 로봇 임무 기술 형식을 비교한 프리프린트.
- **ref-569**: Open-RMF 복합 작업 기술 스키마. 순서가 있는 단계 배열, 단계별 활동과 취소 시 활동을 원문으로 확인했다.
- **ref-570**: 플랫폼 중립 워크플로 기술 DSL 문서. YAML·JSON 형식, 작업 유형(순차·병렬·분기·대기·이벤트·오류 처리), 시간 초과·일정 표현을 원문으로 확인했다.
- **ref-571**: 행동 트리 C++ 라이브러리 README. XML 기반 트리 정의의 실행 시 적재, 플러그인 노드, 비동기 동작 지원을 원문으로 확인했다.
- **ref-572**: 원문 미열람. PDDL 을 확장해 계층적 작업 네트워크 계획 문제(기본·복합 작업, 분해 방법, 순서)를 기술하는 HDDL 을 제안한 논문(AAAI 2020 발표, 저자 목록은 검색 기록 기준).
- **ref-573**: 원문 미열람. OMG BPMN 2.0.2 명세 PDF. 활동 수행 자원(Performer, 10.3.2절)과 사람 수행자·자원 배정 식을 정의한다(검색 요약 기준).

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md | 2, 3, 4, 5, 6, 8, 9 | q2-02 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18 (신뢰도 low) — 2절 q2-02 상태 답함, 3절 q2-02 소제목 신설({#q2-02}): 로봇 관제 형식(Open-RMF 복합 작업·작업 상태 f1·f2, VDA 5050 주문·waitForTrigger f4·f5, MassRobotics 상태 보고만 f6), 업무 형식(ISA-95 작업 응답 f7·f8), 워크플로 형식(BPMN 수행자 f9·f10, Serverless Workflow f11·f12), 계획·실행 표현(HDDL f14, 행동 트리 XML f13), 합의된 임무 기술 표준 부재 평가(f15 의견), 초안 대비 빠진 항목(f16·f3), 플릿 사이 선후(f17), SCM 질문 연결(f18) / 4절 결론·불확실성 / 5절 후속 질문 / 6절 완료 조건 현황 / 8절 출처 / 9절 이력 |
| update | docs/ideas/nl-task-chatbot.md | 4 | 아이디어 페이지 4절: '작업·배정 결과를 표현하는 표준·형식' 소절 신설 — 형식 비교표(f1·f2·f4·f6·f7·f9·f11·f13·f14), 초안 대비 빠진 항목(f16·f3, 추정), 합의된 임무 기술 표준 부재 평가(f15 의견). 평가 데이터(q2-03)는 미조사임을 명시 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | 2, 6 | 트랙 산출물 갱신: track.ontology_changes(진행 상태 값 원천, 배정 결과의 외부 표현 대응)가 승인되면 2절 반영과 초안 버전 인상(f2·f4·f7·f16). 미승인 부분과 플릿 사이 선행 의존(f17)은 6절 질문으로 |
| update | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md | 7 | 트랙 nl-task-chatbot 단계 2 반영 제안 (f2, f4, f18): Open-RMF 작업 상태의 배정 결과(assigned_to)·배정 과정(dispatch) 상태, VDA 5050 의 배정 기능과 주문 단위, 배정 근거 기록 필요와 분류 원문 질문 연결 |
| update | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md | 7 | 트랙 nl-task-chatbot 단계 2 반영 제안 (f7, f9, f10, f11, f15): ISA-95 작업 응답의 실적 필드, BPMN 수행자와 다중 로봇 BPMN 틀, Serverless Workflow, 임무 기술 형식에 합의된 표준이 없다는 평가 |
| update | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md | 7 | 트랙 nl-task-chatbot 단계 2 반영 제안 (f1, f5, f14, f17): Open-RMF 복합 작업의 단계 순서, HDDL 의 하위 작업 순서 표현, VDA 5050 waitForTrigger 를 통한 플릿 사이 동기화 가능성(oq-049 관련) |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 계층적 작업 네트워크 | Hierarchical Task Network (HTN) | 복합 작업을 미리 정한 분해 방법으로 하위 작업 네트워크로 나누어 결국 실행 가능한 기본 작업의 순서에 이르게 하는 자동 계획 방식이다. |
| 계층 도메인 정의 언어 | Hierarchical Domain Definition Language (HDDL) | PDDL 을 확장해 기본 작업·복합 작업·분해 방법과 하위 작업의 순서를 기술하는 계층적 작업 네트워크 계획 문제의 공통 기술 언어이다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 12 · 교차 확인: 0
- 예산 사용량: 검색 7회 · 신규 출처 5건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 형식마다 단일 공식 파일이거나 같은 발행 주체의 스키마·README 쌍
    - f9 BPMN 수행자 정의는 명세 PDF 원문 미열람(검색 요약·구현 문서 요약 범위)
    - f14 HDDL 저자 목록·발행 형태는 검색 기록 기준
    - f3·f8·f12 는 연 문서 범위의 부재 관찰이며 부재 확인 아님
    - f17 waitForTrigger 를 플릿 사이 선후 집행에 쓴 사례 미확인
    - ISA-95 작업 지시 상태 기계의 상태 이름은 이번 열람 응답에서 확인하지 못함
    - 한국어 검색 2회에서 로봇 작업·임무 기술 형식을 정한 KS 표준이나 국내 연구를 찾지 못함
- 범위 경계 위반 의심:
    - 없음
- 한계: web_fetch_available: false · fetch_mode mirror_only. 원문을 연 출처: 신규 ref-569(Open-RMF 복합 작업)·ref-570(Serverless Workflow DSL)·ref-571(BehaviorTree.CPP README)는 github_raw, 재사용 ref-111·ref-130·ref-230·ref-253 은 github_raw, ref-031 은 입력 원문 텍스트(inbox). 신규 ref-572(HDDL)·ref-573(BPMN 2.0.2 PDF)와 재사용 ref-114·ref-116 은 원문 미열람(신뢰도 상한 medium). 검색 7회/40, 신규 출처 5건/20(ref-569~ref-573, 예약 구간 안), 재사용 7건. 교차 확인 0건. 질문 선택: target.json 지정 q2-02 1건. q2-02 는 로봇 관제·업무·워크플로·계획 언어 형식의 필드 관찰로 답했으나, 초안 대비 빠진 항목(f16)은 이 위키의 대응 추론이라 질문 종합 신뢰도를 low 로 두었다. 한국 자료: 한국어 검색 2회에서 KS 로봇 작업 지시·임무 기술 표준을 찾지 못함(KS B ISO 8373·10218 등 용어·안전 표준만 확인되어 넣지 않음). 교차 규칙: 이번 finding 은 LLM 방법이 아니라 표현 형식이라 27. AI·학습·적응과 모델 운영 반영은 제안하지 않았다. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음. 새 일반 열린 질문 없음: 플릿 사이 선후는 기존 oq-049, 배정 비교 실측은 oq-052 와 겹친다. 용어 후보 2건(f14 근거). 트랙 glossary_targets 가운데 용어집에 없는 '사람 확인 루프'는 이번 finding 근거가 없어 내지 않았다. 후속 질문 2건. 온톨로지 변경 제안 2건.

## 트랙 블록

- 트랙: nl-task-chatbot · 단계: 2
- 답한 질문 id: q2-02

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | ROP 가 업무→작업 분해 구조를 내부에 둘 때 BPMN·Serverless Workflow·HDDL 같은 기존 형식을 표준 표현으로 채택할지, 자체 작업 모델 스키마를 두고 Open-RMF 복합 작업·VDA 5050 주문으로 변환할지, 변환 때 배정 근거·확인 여부는 어디에 남기는가? (q2-02 에서 파생) | 3 | f16 |
| — | Open-RMF 복합 작업의 단계와 VDA 5050 waitForTrigger–trigger 를 조합해 제조사가 다른 플릿 사이 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 집행할 수 있는가, 트리거 누락·시간 초과 때 누가 복구하는가? (q2-02 에서 파생) | 3 | f17 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 진행 상태 (Progress) | f2, f7 | 속성 '상태 값'에 외부 표현 원천 후보를 적는다: Open-RMF 작업 상태 status 값(queued·underway·delayed·completed·canceled·failed 등)과 배정 과정 dispatch 값(queued·selected·dispatched·failed_to_assign), ISA-95 작업 응답의 JobState·실제 시작·종료 시각. 초안의 '접수·실행·완료·취소' 네 값과의 대응 규칙은 6절 질문으로 둔다. |
| modify | concept | 배정 (Assignment) | f2, f4, f3, f18 | 배정 결과의 외부 표현 대응을 메모로 단다: Open-RMF 는 assigned_to(플릿 그룹·로봇 이름)로, VDA 5050 은 주문을 보내는 로봇 토픽으로 배정 대상만 표현하고 선택 근거·배정 산출 방식·확인 여부 필드는 없어 작업 모델이 보유한다. 기존 속성과 충돌하지 않는 메모 수준 제안이다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 필요한 데이터 항목과 표준·형식 목록이 아이디어 2. 자연어 업무 지시 챗봇 4절에 아직 실리지 않음(이번 제안 반영 전)
    - 작업 모델의 정보 항목이 업무 분해·배정 설계 초안 개념 목록 표에 일부만 반영됨(작업 요구 적재물 속성·완료 조건 미확정)
    - 열린 질문 q2-03, q2-04, q2-05, q2-06
