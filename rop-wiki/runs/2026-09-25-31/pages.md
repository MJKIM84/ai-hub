# 스토리텔러 산출 2026-09-25-31

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md | draft | 섹션 3~11 신규 작성(명령 식별자·중복 무시, 멱등성 키, 상태 기계, 시간 초과, 재시도·취소·보상, 재시작 복원, 적치 재전송 시나리오), 페이지 상태 표식 추가, 조건부 승인 수정 11건 이행 |
| create | docs/topics/2026/2026-09-25-area12-s6.md | draft | 자동 분리: 12. 명령·작업 실행의 신뢰성 의 "6. 대표 접근법과 기술" 절(3,046자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area12-s7.md | draft | 자동 분리: 12. 명령·작업 실행의 신뢰성 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,355자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area12-s4.md | draft | 자동 분리: 12. 명령·작업 실행의 신뢰성 의 "4. 핵심 개념과 용어" 절(1,163자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area12-s11.md | draft | 자동 분리: 12. 명령·작업 실행의 신뢰성 의 "11. 열린 질문" 절(1,032자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area12-s8.md | draft | 자동 분리: 12. 명령·작업 실행의 신뢰성 의 "8. 대표 연구와 자료" 절(735자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 12. 명령·작업 실행의 신뢰성 | 섹션 3~11 신규 작성(주문 갱신 id 중복 무시, 멱등성 키, 상태 기계, 시간 초과, 재시도·취소·보상, 재시작 복원, 적치 재전송 시나리오), 조건부 승인 수정 11건 이행 | run 2026-09-25-31
- 홈 최근 업데이트: 2026-09-25 — 12. 명령·작업 실행의 신뢰성: 영역 심화 초안 작성(VDA 5050 주문 갱신 id 중복 무시, 멱등성 키, 작업 상태 기계, 시간 초과, 재시작 복원, 적치 재전송 시나리오)
- 대분류 최근 업데이트: 2026-09-25 — 12. 명령·작업 실행의 신뢰성: 섹션 3~11 신규 작성, 1. 주문·업무 시스템 연계·9. 로봇·제조사 관제 연동·11. 분산 시스템·통신·컴퓨팅 구조·20. 예외 복구·재계획·업무 연속성과 연결
- 세부영역 최근 업데이트: 2026-09-25 — 12. 명령·작업 실행의 신뢰성: 섹션 3~11 신규 작성, 조건부 승인 수정 11건 이행, 새 열린 질문 3건

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 멱등성 키 | Idempotency Key | 클라이언트가 요청마다 만든 고유 값으로, 서버가 같은 요청의 재시도를 알아보고 한 번만 처리하게 하는 데 쓰인다. | 12, 1 | ref-592 |
| new | 사가 | Saga | 오래 걸리는 작업을 작은 단계의 순서로 나누고 단계마다 보상 동작을 두어, 전부 완료되거나 부분 실행을 보상하게 하는 트랜잭션 구성 방식이다. | 12, 20 | ref-599 |
| new | 마지막 유언 메시지 | Last Will (MQTT) | MQTT 클라이언트가 예기치 않게 끊기면 브로커가 대신 발행하도록 미리 등록해 둔 메시지로, VDA 5050 은 이를 로봇 연결 끊김(CONNECTION_BROKEN) 알림에 쓴다. | 12, 9, 11 | ref-031, ref-306 |
| new | 관리형 노드 | Managed Node (ROS 2 Lifecycle Node) | Unconfigured·Inactive·Active·Finalized 상태와 전이를 가져 감독 도구가 준비 확인·재시작·교체를 제어할 수 있는 ROS 2 노드이다. | 12, 24 | ref-589 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-126 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/cancel_task_request.json |
| ref-127 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/interrupt_task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/interrupt_task_request.json |
| ref-129 | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 표준 | medium | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 표준 | medium | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL |
| ref-282 | Open Robotics (ROS 2 Documentation) | Quality of Service settings — ROS 2 Documentation: Jazzy | 오픈소스 문서 | high | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html |
| ref-306 | OASIS | MQTT Version 5.0 | 표준 | medium | https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html |
| ref-588 | ROS 2 Design | Actions (ROS 2 Design) | 오픈소스 문서 | high | https://design.ros2.org/articles/actions.html |
| ref-589 | ROS 2 Design | Managed nodes (ROS 2 Design: node_lifecycle) | 오픈소스 문서 | high | https://design.ros2.org/articles/node_lifecycle.html |
| ref-590 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_request.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/dispatch_task_request.json |
| ref-591 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/Task.hpp | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp |
| ref-592 | IETF HTTPAPI Working Group (Jena, J., & Dalal, S.) | The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header) | 표준 | medium | https://github.com/ietf-wg-httpapi/idempotency/blob/main/draft-ietf-httpapi-idempotency-key-header.md |
| ref-594 | OPC Foundation | OPC 10000-10 UA Part 10: Programs - 4.2.4 Program states | 표준 | medium | https://reference.opcfoundation.org/Core/Part10/v104/docs/4.2.4 |
| ref-595 | ISA | ISA-TR88.00.02-2022, Machine and Unit States: An implementation example of ISA-88.00.01 | 표준 | medium | https://www.isa.org/products/isa-tr88-00-02-2022-machine-and-unit-states-an-imp |
| ref-596 | Colledanchise, M., & Ögren, P. | Behavior Trees in Robotics and AI: An Introduction | 논문 | medium | https://arxiv.org/abs/1709.00084 |
| ref-597 | BehaviorTree.CPP (BehaviorTree GitHub) | BehaviorTree.CPP — include/behaviortree_cpp/decorators/retry_node.h | 오픈소스 문서 | high | https://github.com/BehaviorTree/BehaviorTree.CPP/blob/master/include/behaviortree_cpp/decorators/retry_node.h |
| ref-598 | BehaviorTree.CPP (BehaviorTree GitHub) | BehaviorTree.CPP — include/behaviortree_cpp/decorators/timeout_node.h | 오픈소스 문서 | high | https://github.com/BehaviorTree/BehaviorTree.CPP/blob/master/include/behaviortree_cpp/decorators/timeout_node.h |
| ref-599 | Garcia-Molina, H., & Salem, K. | Sagas | 논문 | medium | https://dl.acm.org/doi/10.1145/38713.38742 |
| ref-600 | Open Robotics (open-rmf/rmf_ros2 GitHub) | Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2 | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_ros2/issues/224 |
| ref-601 | Paul, T. C., Lertpongrujikorn, P., Nguyen, H. D., & Amini Salehi, M. | Benchmarking Message Brokers for IoT Edge Computing: A Comprehensive Performance Study | 논문 | medium | https://arxiv.org/abs/2603.21600 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 상위 시스템 요청의 중복을 판별하는 키(멱등성 키나 상위 요청 id)를 ROP 가 얼마 동안 보존해야 하는가, 운반 작업의 재전송 가능 기간에 맞춘 만료 기준을 정한 표준이나 사례가 있는가? | 12, 1 | 열림 | — |
| new | — | VDA 5050 로봇이 재부팅되면 받아 둔 주문을 유지하는지에 대한 규정이 명세에서 확인되지 않는데, 제조사 구현이나 공개 사례는 재부팅 뒤 주문·동작 상태를 어떻게 복원하거나 폐기하는가? | 12, 9 | 열림 | — |
| new | — | Open-RMF 플릿 어댑터 재시작 시 작업 유실을 막는 작업 백업·복원 기능(SQLite 저장 제안)이 현재 배포판에 반영되었는가, 반영되었다면 복원 뒤 로봇의 실제 위치·적재 상태와 어떻게 대조하는가? | 12, 20 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 적치 | 시작 조건 | docs/categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 12. 명령·작업 실행의 신뢰성 |
| 적치 | 작업 대상 | docs/categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 12. 명령·작업 실행의 신뢰성 |
| 적치 | 수행 자원 | docs/categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 12. 명령·작업 실행의 신뢰성 |
| 적치 | 제약 | docs/categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 12. 명령·작업 실행의 신뢰성 |
| 적치 | 완료·인계 | docs/categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 12. 명령·작업 실행의 신뢰성 |
| 적치 | 예외·성과 | docs/categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 12. 명령·작업 실행의 신뢰성 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ROS 2 액션 설계(Actions) | 프레임워크 | ROS 2 Design | 12, 9 | ref-588 | https://design.ros2.org/articles/actions.html |
| ROS 2 관리형 노드 수명주기(Managed nodes) | 프레임워크 | ROS 2 Design | 12, 24 | ref-589 | https://design.ros2.org/articles/node_lifecycle.html |
| Open-RMF rmf_task | 오픈소스 | Open Robotics (open-rmf) | 12, 20 | ref-591 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp |
| IETF Idempotency-Key HTTP 헤더 초안(draft-ietf-httpapi-idempotency-key-header) | 표준 | IETF HTTPAPI Working Group | 12, 1 | ref-592 | https://github.com/ietf-wg-httpapi/idempotency/blob/main/draft-ietf-httpapi-idempotency-key-header.md |
| OPC UA Part 10: Programs (v1.04) | 표준 | OPC Foundation | 12 | ref-594 | https://reference.opcfoundation.org/Core/Part10/v104/docs/4.2.4 |
| ISA-TR88.00.02 Machine and Unit States (PackML) | 표준 | ISA | 12 | ref-595 | https://www.isa.org/products/isa-tr88-00-02-2022-machine-and-unit-states-an-imp |
| BehaviorTree.CPP | 오픈소스 | BehaviorTree (GitHub) | 12 | ref-597 | https://github.com/BehaviorTree/BehaviorTree.CPP/blob/master/include/behaviortree_cpp/decorators/retry_node.h |

## 추가 조사 요청

- 5절·6절: Open-RMF 서버(rmf-web API 서버·작업 파견기)가 같은 내용의 중복 파견 요청을 거르는지와 작업 id 부여 방식(task_dispatch_response.json 은 404 로 열지 못함)을 소스 코드로 확인해야 한다. 재전송 시 별개 작업 생성 여부가 현재 추정이다.
- 6절·11절: VDA 5050 로봇의 재부팅 뒤 주문 유지·폐기 규정과 상태 미수신 시 관제 대응 규정의 존재 여부를 명세 전체로 확인해야 한다(현재 발췌 범위에서 찾지 못함, 부재 확정 아님).
- 7절: ISA-95 Job Control 상태 기계 상태 이름과 Store 메서드의 중복 id 반환 코드(부속서 B.2), PackML 17개 상태를 발행 기관 자료로 확인해야 한다.
- 3절·5절: 명령 중복·재시작 복원을 다룬 한국 현장·학술 자료가 없다. 국내 물류센터 WMS–로봇 관제 연동에서 재전송·중복 처리 사례를 찾아야 한다.
- 전반: 모든 사실 주장이 단일 발행 주체 자료이고 교차 확인이 0건이다. 주문 갱신 id 중복 무시 규칙과 결과 캐시 같은 핵심 주장을 독립 출처(구현 문서·논문)로 교차 확인해야 한다.

## 이행한 수정 지시

- f21 강등 — 6절 상태 기계 문단과 7절 표 PackML 행을 [추정]으로 쓰고 'ISA 원문 미열람, 상태 목록은 발행 기관 자료로 미확인'과 2015판·2022판을 병기했다.
- f27 강등 — 8절 브로커 비교 연구 항목을 [추정]으로 쓰고 '저자 보고값(MQTT 브로커 5종, MTTF 30초·MTTR 5초 장애 모델)이며 원문 미열람'을 병기했다.
- ref-601 — reference_updates 와 각주의 기관을 'Paul, T. C., Lertpongrujikorn, P., Nguyen, H. D., & Amini Salehi, M.'로, 발행일을 2026-03-23 으로 고쳤다.
- ref-593 — 새 참고문헌으로 등록하지 않고 f16·f17 문장의 각주를 기존 ref-306(OASIS, MQTT Version 5.0)으로 바꿨으며 reference_updates 에서 ref-593 을 뺐다.
- f9 — 6절 멱등성 키 문단에 가장 이른 시작 시각(unix_millis_earliest_start_time)을 넣고 작업 요청의 필수 필드가 category·description 뿐이라고 썼다.
- f20 — 6절 상태 기계 문단과 7절 표에 OPC UA Part 10 의 판(v1.04 참조 페이지 기준)을 적었다.
- 각주 — ref-129, ref-306, ref-594, ref-595, ref-596, ref-599, ref-600, ref-601 의 각주 정의에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다. ref-111 은 기존 참고문헌 행(high, 원문 미열람 표시 없음)을 그대로 재사용했다.
- 인용 — 페이지 전체에서 출처 원문 직접 인용을 쓰지 않고 ref-031 을 포함한 모든 출처를 요약·재서술했다.
- f16·f27 — 6절에서 MQTT 전달 보장을 중복 판단의 입력으로만 짧게 쓰고 8절 브로커 연구도 입력으로만 참고한다고 밝혔으며, 6절과 10절에서 11. 분산 시스템·통신·컴퓨팅 구조로 연결했다.
- f30 — 5절 제약 칸과 6절 시간 초과 문단에 '상태 미수신 시 관제 대응 규정을 명세 발췌 범위에서 찾지 못함(부재 확정 아님)' 단서를 유지했다.
- f31 — PackML 부분을 [추정] 근거로만 써서 6절 상태 대응 규칙 문장을 [추정]으로 두고 [사실]로 쓰지 않았다.
- 분량 초과 자동 분리: 12. 명령·작업 실행의 신뢰성 본문 10,392자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,780자
