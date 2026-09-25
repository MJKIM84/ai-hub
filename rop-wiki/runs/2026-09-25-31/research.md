# 리서치 브리프 2026-09-25-31

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-31 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 12. 명령·작업 실행의 신뢰성 |
| 대분류 | C. 연결·실행 기반 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(멱등성, 주문 갱신 id, 목표 id, 상태 기계, 마지막 유언 메시지 등)
- 섹션 5. 현장 시나리오 비어 있음(운반 요청 재전송·취소·재시작 시나리오)
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(관련 기존 열린 질문 oq-014·oq-021·oq-033 이 이 영역을 관련 영역으로 둠)

## 조사 질문

1. 응답이 끊긴 운반 요청을 다시 보내면 같은 화물을 두 번 처리하지 않을까? [분류원문]
2. 로봇 인터페이스 표준(VDA 5050, ROS 2 액션, Open-RMF 작업 API)은 명령의 접수·실행·완료·취소 상태와 명령 식별자를 어떻게 정의하는가? (섹션 4·6·7 겨냥)
3. 중복 요청 방지(멱등성)를 위한 일반 표준·관행(IETF Idempotency-Key 초안, MQTT QoS)은 무엇이고, 로봇 명령 계층에 어떤 한계와 함께 적용되는가? (섹션 6·7 겨냥)
4. 시간 초과·연결 끊김을 감지하는 기법(마지막 유언 메시지, 상태 보고 주기, ROS 2 QoS deadline·liveliness)과 그 뒤의 처리 규칙은 어디까지 표준이 정하는가? (섹션 3·6 겨냥)
5. 관제 소프트웨어나 로봇이 재시작된 뒤 진행 중 작업 상태를 복원하는 방법(작업 백업, 관리형 노드 수명주기)은 어떤 것이 있고 공개 구현의 한계는 무엇인가? (섹션 6·8·11 겨냥)
6. 산업 자동화의 상태 기계 표준(OPC UA Programs, PackML, ISA-95 Job Control)과 행동 트리·사가(보상 트랜잭션) 같은 실행 구조 기법은 명령 실행 신뢰성에 어떻게 쓰이는가? (섹션 6·8·10 겨냥)
7. ROP가 직접 맡을 신뢰성 기능과 로봇 제조사·통신 계층에 맡길 기능의 경계는 무엇인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 은 이동로봇이 같은 orderUpdateId 의 주문을 다시 받았을 때 내용이 같으면 무시하고, 내용이 다르면 SAME_ORDER_UPDATE_ID 오류(WARNING)를 보고하도록 규정한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f2 | [사실] | VDA 5050 3.0.0 에서 이동로봇은 이전보다 낮은 orderUpdateId 의 주문을 받으면 새 주문을 버퍼에 받지 않고 이전 주문을 유지하며 OUTDATED_ORDER_UPDATE 오류(WARNING)를 보고한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f3 | [사실] | VDA 5050 3.0.0 에서 관제는 로봇이 상태 메시지에 싣는 주문 id·주문 갱신 id 로 주문 수용 여부를 알 수 있으며, 로봇은 상태 메시지를 관련 사건이 생길 때 또는 적어도 30초마다 발행해야 한다. | ref-031 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f4 | [사실] | VDA 5050 3.0.0 은 무선 전송이 신뢰할 수 없으므로 이미 전달한 기반(base) 경로는 바꿀 수 없고 관제는 기반이 이미 실행되었다고 가정해야 하며, 브로커와 연결이 끊긴 로봇은 주문 정보를 유지한 채 마지막으로 해제된(released) 노드까지 주문을 수행한다고 규정한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f5 | [사실] | VDA 5050 3.0.0 은 order·instantActions·state 등 대부분의 토픽에 MQTT QoS 0(최선 노력)을, connection 토픽에 QoS 1(최소 한 번)을 쓰게 하고, 로봇이 예기치 않게 끊기면 브로커가 마지막 유언(last will) 메시지로 connectionState 를 CONNECTION_BROKEN 으로 알리게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 에서 cancelOrder 즉시 동작을 받은 로봇은 가능한 한 빨리 멈추고, 실행 중인 동작이 모두 취소·종료될 때까지 cancelOrder 를 RUNNING 으로, 이동과 모든 동작이 멈춘 뒤 FINISHED 로 보고하며, 이후 관제는 취소된 주문에 갱신을 보내지 않는다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f7 | [사실] | VDA 5050 3.0.0 은 동작 상태에 실패했지만 다시 시도할 수 있음을 뜻하는 RETRIABLE 을 두고, 관제가 즉시 동작 retry 로 재시도하거나 skipRetry 로 그 동작을 FAILED 로 넘기게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f8 | [사실] | ROS 2 액션 설계는 목표(goal) id 를 액션 클라이언트만 생성하되 UUID 로 만들어 여러 클라이언트 사이 충돌을 줄이고, 목표 상태를 ACCEPTED·EXECUTING·CANCELING(진행)과 SUCCEEDED·ABORTED·CANCELED(종료)로 나누며, 서버는 결과를 설정한 시간 동안 캐시해 여러 클라이언트가 받을 수 있게 한다. | ref-588 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | Open-RMF 의 작업 파견 요청(dispatch_task_request)과 작업 요청(task_request) 스키마에는 요청자가 정하는 요청 식별자나 멱등성 키 필드가 없고, 요청 시각·우선순위·범주·설명·라벨·요청자·플릿 이름만 둔다. | ref-590, ref-125 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f10 | [추정] | Open-RMF 작업 요청 스키마에 요청자 측 식별자가 없으므로, 응답을 받지 못한 파견 요청을 그대로 다시 보내면 별개 작업이 하나 더 생길 수 있어 ROP 쪽에서 상위 요청 id 와 작업 id 의 대응을 저장해 중복을 걸러야 할 것으로 보인다. | ref-590, ref-125, ref-111 | 아니오 | low | 2026-09-25 | 적치 / 예외·성과 | — |
| f11 | [사실] | Open-RMF 의 작업 취소 요청과 작업 중단(interrupt) 요청은 작업 id(task_id)와 선택 라벨만으로 대상을 지정하며, 중단된 작업은 이후 재개 요청을 보내야 다시 진행된다. | ref-126, ref-127 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f12 | [사실] | Open-RMF 작업 상태 스키마는 queued·underway·completed·canceled·killed·failed 등 상태 값과 시작·종료 시각, 취소·강제 종료·중단 요청 기록을 담는다. | ref-111 | 아니오 | medium | 2026-09-25 | 완료·인계 | 원문 미열람 |
| f13 | [사실] | Open-RMF rmf_task 라이브러리의 실행 중 작업(Task::Active)은 순서 번호가 붙은 문자열 형태의 백업을 만들 수 있고, 취소(cancel)는 로봇을 짐 없는 상태로 되돌리게 하며, 강제 종료(kill)는 취소보다 우선해 로봇을 안전한 유휴 상태로 되돌리게 하고, 단계 건너뛰기(skip)·되감기(rewind)를 제공한다. | ref-591 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f14 | [사실] | Open-RMF 저장소 이슈 #224 는 플릿 어댑터가 재시작되면 배정된 작업이 사라진다고 지적하고, 작업 로그와 백업을 SQLite 데이터베이스에 저장해 복구하는 기능이 별도 풀 리퀘스트로 제안되었다고 적는다. | ref-600 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f15 | [사실] | IETF HTTPAPI 작업반의 Idempotency-Key 헤더 초안(RFC 가 아닌 인터넷 초안)은 클라이언트가 만든 고유 키로 서버가 같은 요청의 재시도를 알아보게 하며, 키를 다른 내용의 요청에 재사용하면 안 되고, 서버는 키 만료 정책을 공개해야 하며, 원 요청이 처리 중일 때의 재요청에는 409, 다른 내용으로 재사용한 요청에는 422 를 돌려주도록 제안한다. | ref-592 | 아니오 | medium | 2025-10-15 | — | — |
| f16 | [사실] | MQTT 5.0 의 QoS 2(정확히 한 번)는 네 단계 확인 교환으로 프로토콜 상대 사이의 정확히 한 번 전달을 보장하며, 수신 측은 PUBCOMP 를 보낼 때까지 원 PUBLISH 의 패킷 식별자를 기억해 확인 응답 손실로 다시 온 중복 PUBLISH 를 버린다. | ref-306 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f17 | [추정] | MQTT QoS 보장은 클라이언트–브로커 같은 프로토콜 상대 사이에만 적용되므로, 관제가 응답 시간 초과 뒤 새 메시지로 주문을 다시 보내는 경우의 중복은 QoS 가 아니라 VDA 5050 의 주문 id·주문 갱신 id 같은 응용 계층 식별자로 걸러야 할 것으로 보인다. | ref-306, ref-031 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f18 | [사실] | ROS 2 의 서비스 품질(QoS) 정책은 신뢰(reliable)·최선 노력(best effort) 전달, 늦게 참여한 구독자를 위해 발행자가 샘플을 보존하는 transient local 지속성, 메시지 사이 최대 간격을 정하는 deadline, 임대 기간(lease duration) 안에 살아 있음을 알리지 않으면 활성 상실로 보는 liveliness 와, 그 위반을 알리는 QoS 이벤트를 둔다. | ref-282 | 아니오 | medium | 2026-09-25 | — | — |
| f19 | [사실] | ROS 2 관리형 노드(managed node) 설계는 Unconfigured·Inactive·Active·Finalized 네 주 상태와 전이 상태를 두어, 감독 도구가 모든 구성요소가 올바르게 준비되었는지 확인한 뒤 실행을 허용하고 노드를 운영 중에 재시작·교체할 수 있게 한다. | ref-589 | 아니오 | medium | 2026-09-25 | — | — |
| f20 | [사실] | OPC UA Part 10(Programs)의 프로그램 상태 기계는 Halted·Ready·Running·Suspended 상태를 두며, Suspended 는 멈춘 지점에서 기능을 재개할 수 있는 상태이고, Halted 는 초기 상태이자 실패 또는 완료를 나타내는 종료 상태가 될 수 있다. | ref-594 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f21 | [사실] | ISA-TR88.00.02(PackML)는 기계·유닛 상태 모델로 Idle·Starting·Execute·Completing·Complete·Resetting·Holding·Held·Unholding·Suspending·Suspended·Unsuspending·Stopping·Stopped·Aborting·Aborted·Clearing 17개 상태를 정의한다. | ref-595 | 아니오 | medium | 2022 | — | 원문 미열람 |
| f22 | [사실] | 상위 작업 지시 쪽에서 OPC UA for ISA-95 Job Control 은 Store·StoreAndStart·Start·RevokeStart·Pause·Resume·Update·Abort·Stop·Cancel·Clear 메서드를, B2MML 거래 프로파일은 CHANGE·CANCEL 등 거래 동사를 정의한다. | ref-130, ref-129 | 아니오 | medium | 2024-01-31 | 시작 조건 | — |
| f23 | [사실] | 행동 트리 라이브러리 BehaviorTree.CPP 는 자식이 실패하면 지정한 횟수까지 다시 실행하는 RetryNode 와, 자식이 정해진 시간보다 오래 RUNNING 이면 중단(halt)하고 FAILURE 를 돌려주는 TimeoutNode 를 제공한다. | ref-597, ref-598 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f24 | [사실] | Colledanchise·Ögren 의 행동 트리 입문서는 행동 트리를 자율 에이전트의 작업 전환을 구조화하는 방법으로 소개하며, 모듈성과 반응성을 함께 갖춘 시스템을 만드는 효율적 방법이라고 설명한다. | ref-596 | 아니오 | medium | 2017-09 | — | 원문 미열람 |
| f25 | [사실] | Garcia-Molina·Salem(1987)의 사가(Saga)는 오래 걸리는 트랜잭션을 다른 트랜잭션과 섞여 실행될 수 있는 작은 트랜잭션의 순서로 나누고, 각 단계에 보상 트랜잭션을 두어 전부 완료되거나 부분 실행을 보상하게 하며, 보상은 의미상 되돌림이지 처음 상태 복원을 보장하지 않는다. | ref-599 | 아니오 | medium | 1987 | — | 원문 미열람 |
| f26 | [추정] | 로봇이 이미 화물을 싣거나 옮긴 물리 동작은 되돌릴 수 없으므로, 취소된 운반 작업의 복구는 사가의 보상 단계처럼 원위치 반송 같은 별도 작업을 새로 만들어 처리하는 형태가 될 것으로 보인다. | ref-599, ref-031, ref-591 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f27 | [사실] | IoT 엣지용 메시지 브로커 성능 비교 연구(arXiv 2603.21600)는 네트워크 장애 조건에서 QoS 0 의 메시지 손실이 약 6.3~6.6% 였고 QoS 1·2 는 손실이 없었다고 보고했다(저자 실험 조건). | ref-601 | 아니오 | medium | 2026-03 | 예외·성과 | 원문 미열람 |
| f28 | [추정] | VDA 5050 이 기반 경로 실행과 동작 상태 보고를 로봇에 맡기고 관제에는 식별자 규칙과 상태 해석을 맡기므로, ROP 가 직접 맡을 신뢰성 기능은 상위 요청의 중복 판별, 명령 식별자 발급·보존, 작업 상태 기계 유지, 시간 초과 판정, 재시작 뒤 상태 복원이 될 것으로 보인다. | ref-031, ref-591, ref-590 | 아니오 | low | 2026-09-25 | — | — |
| f29 | [추정] | 연계 대상: 로봇 내부의 동작 재시도, 로컬 회피, 정지 방식(선 유도 로봇의 다음 노드 정지 등)은 로봇 제조사 영역이며, ROP 는 VDA 5050 의 RETRIABLE·cancelOrder 상태처럼 그 결과를 보고받아 판단하는 쪽에 가깝다. | ref-031 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f30 | [추정] | VDA 5050 3.0.0 은 상태 메시지가 오지 않을 때 관제가 할 일을 규정하지 않으므로, 시간 초과 기준과 그 뒤 처리(재질의·일시정지·사람 호출)는 30초 상태 주기와 CONNECTION_BROKEN 알림을 입력으로 ROP 가 따로 정해야 할 것으로 보인다. | ref-031 | 아니오 | low | 2026-09-25 | 제약 | — |
| f31 | [추정] | VDA 5050 동작 상태, ROS 2 액션 목표 상태, Open-RMF 작업 상태, OPC UA 프로그램 상태, PackML 상태는 일시정지·중단·취소·실패의 구분이 서로 달라, ROP 가 상위 시스템에 되돌릴 공통 작업 상태로 옮기려면 대응 규칙이 필요할 것으로 보인다. | ref-031, ref-588, ref-111, ref-594, ref-595 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f32 | [추정] | 분류 원문 질문의 상황에서 관제가 응답이 끊긴 적치 운반 주문을 같은 주문 id·같은 주문 갱신 id·같은 내용으로 다시 보내면 VDA 5050 로봇은 이를 무시하므로 로봇 단계의 이중 실행은 막을 수 있으나, 상위 시스템이 새 요청으로 다시 보내 ROP 가 새 주문 id 를 발급하면 이 보호가 작동하지 않을 것으로 보인다. | ref-031, ref-592 | 아니오 | low | 2026-09-25 | 적치 / 예외·성과 | — |

### 근거 발췌

- **f1**: 명세 원본: 'If the content of the new order is the same as the content of the previous one, the mobile robot shall ignore the new order.' 내용이 다르면 SAME_ORDER_UPDATE_ID, level WARNING. (발행일 미확인, 확인일 기준)
- **f2**: 명세 원본: 로봇은 새 주문을 내부 버퍼에 받지 않고 이전 주문을 유지하며 'OUTDATED_ORDER_UPDATE' 유형, 'WARNING' 수준 오류를 보고한다. (발행일 미확인, 확인일 기준)
- **f3**: 명세 원본: 'The mobile robot state message shall be published when relevant events occur or at least every 30 seconds.' 수용 여부는 상태의 주문 id·주문 갱신 id 로 확인(6.6.1 절 취지, 열람 도구 요약). (발행일 미확인, 확인일 기준)
- **f4**: 명세 원본(6.1.2): 'the base cannot be changed. The fleet control shall therefore assume that the base has already been executed'. 연결 끊김 시 'keeps all the order information and fulfills the order up to the last released node'. 재부팅 후 주문 유지 규정은 찾지 못함. (발행일 미확인, 확인일 기준)
- **f5**: 명세 원본: 'the MQTT QoS level 0 (Best Effort) shall be used for the topics order, instantActions, state, ... QoS level 1 (At Least Once) shall be used for the topic connection.' 연결 상태 값 ONLINE·OFFLINE·CONNECTION_BROKEN. (발행일 미확인, 확인일 기준)
- **f6**: 명세 원본: 'the cancelOrder action shall report RUNNING until all actions are cancelled/finished ... shall report FINISHED'; 'No further order updates to the cancelled order shall be sent by the fleet control.' (발행일 미확인, 확인일 기준)
- **f7**: 명세 원본: retry 는 'retries action defined via actionId that is currently in state RETRIABLE', skipRetry 는 'skip the action ... setting action to FAILED'. 동작 상태 값 INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE. (발행일 미확인, 확인일 기준)
- **f8**: 설계 원본: 'action clients will be the sole entities responsible for generating the goal ID'; 'a UUID will be used for each goal'; 'The server should cache the result once it is ready'. 중복 목표 id 처리 규정은 문서에 없음.
- **f9**: dispatch_task_request.json 원본: 필수 필드 type·request 뿐. task_request.json 원본: unix_millis_earliest_start_time, unix_millis_request_time, priority, category, description, labels, requester, fleet_name. 같은 저장소라 독립 교차 아님. (발행일 미확인, 확인일 기준)
- **f10**: f9 의 필드 부재와 작업 상태 스키마(작업 id 기준 상태 조회)를 분류 원문 질문에 대응시킨 추론. 서버가 중복 요청을 거르는지 소스 코드로 확인하지 않음.
- **f11**: cancel_task_request.json·interrupt_task_request.json 원본: 필수 type·task_id, 선택 labels('dashboard' 또는 'app=dashboard'). 중단은 resume 요청으로 재개. 같은 저장소. (발행일 미확인, 확인일 기준)
- **f12**: task_state.json: status enum uninitialized, blocked, error, failed, queued, standby, underway, delayed, skipped, canceled, killed, completed; cancellation, killed, interruptions. 이번 실행에서 다시 열지 않음. (재인용: 2026-09-25-29)
- **f13**: Task.hpp 원본: 'The state of the task is represented by a string ... Each Backup is tagged with a sequence number.' cancel: 'return itself to an unencumbered state'; kill: 'supersedes the cancel() command'. (발행일 미확인, 확인일 기준)
- **f14**: 검색 요약: 'When a fleet adapter restarts for any reason, the assigned tasks will be lost after the restart'; 'store task logs and backup in a SQLite database'. 현재 배포판 반영 여부는 미확인. (발행일 미확인, 확인일 기준)
- **f15**: 편집본 원문: 'An idempotency key is a unique value generated by the client which the resource uses to recognize subsequent retries of the same request.' 검색 요약상 최신 게시판은 -07(2025-10-15). 요청 내용 지문(fingerprint) 비교도 제안.
- **f16**: 검색 요약: QoS 2 'guarantees delivery exactly once between protocol peers using a four-part handshake'; 수신 측이 패킷 식별자를 PUBCOMP 전까지 유지. 원문 미열람.
- **f17**: f16(프로토콜 상대 사이 보장)과 f1·f5(QoS 0 사용, 같은 갱신 id 무시 규칙)를 대응시킨 추론. 이 구분을 명시한 로봇 분야 출처는 찾지 못함.
- **f18**: 문서 원본(jazzy): Deadline 'the expected maximum amount of time between subsequent messages being published to a topic'; Lease Duration 초과 시 liveliness 상실, 'Deadline Missed'·'Liveliness Changed' 이벤트.
- **f19**: 설계 원본: 'roslaunch to ensure that all components have been instantiated correctly before it allows any component to begin executing'; 'nodes to be restarted or replaced on-line'. 전이 상태 Configuring·CleaningUp·Activating·Deactivating·ShuttingDown·ErrorProcessing.
- **f20**: 검색 요약: Suspended 'retains the ability to resume the Function at the point at which it was executing when suspended'; Halted 'can indicate either a failed or completed Program'. 원문 미열람.
- **f21**: 검색 요약: 'PackML defines 17 states in total'; 2015판과 2022판(ISA-TR88.00.02-2022)이 있음. 원문(유료) 미열람.
- **f22**: Job Control 노드셋 documentation.csv 원문(이번 실행 열람)에서 수신 객체 메서드 확인. B2MML TransactionVerb1Type 은 이번에 다시 열지 않음. 저장 중복 id 반환 코드는 부속서 B.2 에 있으나 미확인. (재인용: 2026-09-25-29)
- **f23**: retry_node.h: 'If the child returns FAILURE, this node will try again up to N times'. timeout_node.h: 'will halt() a running child if the latter has been RUNNING longer than a given time ... returns FAILURE.' 같은 저장소라 독립 교차 아님.
- **f24**: 검색 요약: BTs 'provide a way to structure the switching between different tasks in autonomous agents'; 'modular and reactive'. 원문 미열람.
- **f25**: 검색 요약: 'either all the transactions in a saga are successfully completed or compensating transactions are run to amend a partial execution'; 보상은 'semantically' 되돌림. 원문 미열람.
- **f26**: f25(보상 트랜잭션)·f4(기반 실행 가정)·f13(취소 시 짐 없는 상태로 복귀)을 대응시킨 추론. 물류 로봇에 사가를 적용한 사례는 찾지 못함(oq-021 과 연결).
- **f27**: 검색 요약: 'at QoS 0, brokers exhibit approximately 6.3-6.6% message loss under network failures, while QoS 1 and QoS 2 achieve 0% message loss.' 브로커 종류·장애 모델 등 조건 미확인. 원문 미열람.
- **f28**: f1~f7(로봇 쪽 규칙)과 f9·f13·f14(관제 소프트웨어 쪽 기능·한계)를 분류 원문 9장 '로봇 자체 지능·제어' 경계(상태·실패·완료 확인은 ROP)에 대응시킨 추론.
- **f29**: 명세의 cancelOrder 정지 방식('For line-guided mobile robots, this could be the next feasible node')과 RETRIABLE 재시도 규칙(f6·f7)을 분류 원문 9장 경계에 대응시킨 추론.
- **f30**: 명세 열람 결과 상태 미수신 시 관제 대응 규정을 찾지 못함(열람 도구 응답: 'does not specify fleet control's required response to missing state messages'). 부재 확정 아님.
- **f31**: f7·f8·f12·f20·f21 의 상태 값 비교에서 나온 추론. 예: ROS 2 는 ABORTED(서버 자체 중단)와 CANCELED(외부 요청)를 구분, Open-RMF 는 canceled·killed 구분. 공통 매핑 표준은 찾지 못함(oq-014, oq-033).
- **f32**: f1·f3 의 로봇 쪽 중복 무시 규칙과 f15 의 요청 단위 멱등성 키 개념을 SCM 질문에 대응시킨 추론. 국내 현장 사례는 찾지 못함.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 예 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-126 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/cancel_task_request.json | 아니오 |
| ref-127 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/interrupt_task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/interrupt_task_request.json | 아니오 |
| ref-129 | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 2023 | 표준 | medium | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd | 예 |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 2024-01-31 | 표준 | medium | 2026-09-25 | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL | 아니오 |
| ref-282 | Open Robotics (ROS 2 Documentation) | Quality of Service settings — ROS 2 Documentation: Jazzy | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html | 아니오 |
| ref-588 | ROS 2 Design | Actions (ROS 2 Design) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://design.ros2.org/articles/actions.html | 아니오 |
| ref-589 | ROS 2 Design | Managed nodes (ROS 2 Design: node_lifecycle) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://design.ros2.org/articles/node_lifecycle.html | 아니오 |
| ref-590 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/dispatch_task_request.json | 아니오 |
| ref-591 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/Task.hpp | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp | 아니오 |
| ref-592 | IETF HTTPAPI Working Group (Jena, J., & Dalal, S.) | The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/ietf-wg-httpapi/idempotency/blob/main/draft-ietf-httpapi-idempotency-key-header.md | 아니오 |
| ref-306 | OASIS | MQTT Version 5.0 (OASIS Standard) | 미확인 | 표준 | medium | 2026-09-25 | https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html | 예 |
| ref-594 | OPC Foundation | OPC 10000-10 UA Part 10: Programs - 4.2.4 Program states | 미확인 | 표준 | medium | 2026-09-25 | https://reference.opcfoundation.org/Core/Part10/v104/docs/4.2.4 | 예 |
| ref-595 | ISA | ISA-TR88.00.02-2022, Machine and Unit States: An implementation example of ISA-88.00.01 | 2022 | 표준 | medium | 2026-09-25 | https://www.isa.org/products/isa-tr88-00-02-2022-machine-and-unit-states-an-imp | 예 |
| ref-596 | Colledanchise, M., & Ögren, P. | Behavior Trees in Robotics and AI: An Introduction | 2017-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1709.00084 | 예 |
| ref-597 | BehaviorTree.CPP (BehaviorTree GitHub) | BehaviorTree.CPP — include/behaviortree_cpp/decorators/retry_node.h | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/BehaviorTree/BehaviorTree.CPP/blob/master/include/behaviortree_cpp/decorators/retry_node.h | 아니오 |
| ref-598 | BehaviorTree.CPP (BehaviorTree GitHub) | BehaviorTree.CPP — include/behaviortree_cpp/decorators/timeout_node.h | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/BehaviorTree/BehaviorTree.CPP/blob/master/include/behaviortree_cpp/decorators/timeout_node.h | 아니오 |
| ref-599 | Garcia-Molina, H., & Salem, K. | Sagas | 1987 | 논문 | medium | 2026-09-25 | https://dl.acm.org/doi/10.1145/38713.38742 | 예 |
| ref-600 | Open Robotics (open-rmf/rmf_ros2 GitHub) | Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/issues/224 | 예 |
| ref-601 | arXiv 2603.21600 저자(미확인) | Benchmarking Message Brokers for IoT Edge Computing: A Comprehensive Performance Study | 2026-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2603.21600 | 예 |

### 출처 요약

- **ref-031**: VDA 5050 공식 명세(main 3.0.0). 주문 갱신 id 중복·구버전 처리, 기반 실행 가정, MQTT QoS, 마지막 유언, cancelOrder, RETRIABLE·retry·skipRetry, 30초 상태 주기를 원문으로 확인.
- **ref-111**: 원문 미열람. Open-RMF 작업 상태 스키마(이번 실행에서 다시 열지 않음). 상태 값, 시작·종료 시각, 취소·강제 종료·중단 기록.
- **ref-125**: Open-RMF 작업 요청 스키마. 요청 시각·우선순위·범주·설명·라벨·요청자·플릿 이름 필드를 원문으로 확인했고 요청자 측 식별자 필드는 없다.
- **ref-126**: Open-RMF 작업 취소 요청 스키마. type·task_id 필수, labels 선택을 원문으로 확인.
- **ref-127**: Open-RMF 작업 중단 요청 스키마. type·task_id 필수, labels 선택, 재개 요청으로 다시 진행함을 원문으로 확인.
- **ref-129**: 원문 미열람. B2MML 거래 프로파일 스키마(이번 실행에서 다시 열지 않음). CHANGE·CANCEL 등 거래 동사.
- **ref-130**: OPC UA for ISA-95 Job Control 노드셋. documentation.csv 에서 작업 지시 수신 객체 메서드(Store~RevokeStart)를 확인했고, 상태 기계 상태 이름과 반환 코드는 열람 범위에서 확인하지 못했다.
- **ref-282**: ROS 2 QoS 정책 문서. 신뢰·최선 노력, transient local, deadline, liveliness·lease duration, QoS 이벤트를 문서 원본(ros2_documentation jazzy 브랜치)으로 확인.
- **ref-588**: ROS 2 액션 설계 문서. 목표 상태(ACCEPTED·EXECUTING·CANCELING·SUCCEEDED·ABORTED·CANCELED), 클라이언트의 UUID 목표 id 생성, 취소 정책, 결과 캐시·만료를 정한다.
- **ref-589**: ROS 2 관리형 노드 수명주기 설계. 네 주 상태와 여섯 전이 상태, 감독 도구에 의한 준비 확인과 운영 중 재시작·교체 목적을 정한다.
- **ref-590**: Open-RMF 작업 파견 요청 스키마. type 과 task_request 참조만 필수로 두며 요청자 측 식별자·멱등성 키 필드가 없다.
- **ref-591**: Open-RMF 작업 라이브러리의 작업 인터페이스 헤더. 실행 중 작업의 백업(순서 번호 포함), 중단·취소·강제 종료·단계 건너뛰기·되감기의 뜻을 주석으로 정한다.
- **ref-592**: 작업반 공식 저장소의 인터넷 초안 편집본(RFC 아님). 클라이언트가 만든 멱등성 키로 재시도를 식별하고, 키 재사용 금지·만료 정책·409/422/400 오류 처리를 제안한다. 검색 요약상 최신 게시판은 -07(2025-10-15).
- **ref-306**: 원문 미열람. MQTT 5.0 명세. QoS 0·1·2 전달 보장, 패킷 식별자와 PUBREC·PUBREL·PUBCOMP 교환에 의한 중복 PUBLISH 식별을 정한다.
- **ref-594**: 원문 미열람. OPC UA 프로그램 상태 기계(Halted·Ready·Running·Suspended)와 Start·Suspend·Resume·Halt 전이를 정한다.
- **ref-595**: 원문 미열람. PackML 로 알려진 기계·유닛 상태 모델 기술보고서. 17개 상태와 운전 모드를 정한다(유료 원문).
- **ref-596**: 원문 미열람. 로봇·AI 에서 행동 트리의 구조, 모듈성·반응성, 설계 원칙을 소개하는 입문서(프리프린트, 이후 책으로 출간).
- **ref-597**: 행동 트리 라이브러리의 재시도 데코레이터 헤더. 실패한 자식을 num_attempts 횟수까지 다시 실행한다.
- **ref-598**: 행동 트리 라이브러리의 시간 초과 데코레이터 헤더. 정해진 시간보다 오래 실행 중인 자식을 중단하고 FAILURE 를 돌려준다.
- **ref-599**: 원문 미열람. 오래 걸리는 트랜잭션을 작은 트랜잭션과 보상 트랜잭션의 순서로 나누는 사가 개념을 제안한 ACM SIGMOD 1987 논문.
- **ref-600**: 원문 미열람. 플릿 어댑터 재시작 시 배정 작업이 사라지는 문제와 SQLite 기반 작업 백업 제안을 다룬 프로젝트 이슈.
- **ref-601**: 원문 미열람. IoT 엣지용 메시지 브로커의 성능·신뢰성을 QoS 수준과 네트워크 장애 조건에서 비교한 프리프린트.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3(왜 중요한가): f4·f5·f14·f27·f32 — 무선 전송 불확실성, 재시작 시 작업 유실, 중복 처리 위험. 섹션 4(핵심 개념과 용어): f1·f2(주문 갱신 id), f8(목표 id·목표 상태), f15(멱등성 키), f5(마지막 유언), f18(deadline·liveliness), f25(사가·보상). 섹션 5(현장 시나리오): f32·f10(적치 운반 재전송, 예외·성과), f26(출하 취소 후 되돌림), f3·f12(완료·인계). 섹션 6(대표 접근법과 기술): 식별자 기반 중복 무시(f1·f2·f17), 멱등성 키(f15), 상태 기계(f8·f20·f21·f31), 시간 초과·활성 감지(f5·f18·f23·f30), 재시도(f7·f23), 상태 백업·복원(f13·f14·f19), 보상(f25·f26). 섹션 7(관련 표준·프레임워크·오픈소스): VDA 5050(f1~f7), ROS 2 액션·QoS·관리형 노드(f8·f18·f19), Open-RMF(f9·f11·f12·f13), MQTT 5.0(f16), IETF 초안(f15), OPC UA Programs·PackML·ISA-95 Job Control(f20·f21·f22), BehaviorTree.CPP(f23). 섹션 8(대표 연구와 자료): f24·f25·f27. 섹션 9(ROP가 직접 맡는 것과 외부와 연계하는 것): f28(직접 범위), f29(연계 대상), f17(통신 계층 보장과 응용 계층 구분). 섹션 10(다른 연구영역과의 연결): 1. 주문·업무 시스템 연계(f22), 2. 공정·워크플로 모델링(f31, oq-014), 9. 로봇·제조사 관제 연동(f1~f7, f31, oq-033), 11. 분산 시스템·통신·컴퓨팅 구조(f5·f16·f18·f27), 19. 모니터링·이상 탐지·원인 분석(f12·f31), 20. 예외 복구·재계획·업무 연속성(f7·f13·f26, oq-021). 섹션 11(열린 질문): 기존 oq-014·oq-021·oq-033 과 이번 새 질문. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 멱등성 키 | Idempotency Key | 클라이언트가 요청마다 만든 고유 값으로, 서버가 같은 요청의 재시도를 알아보고 한 번만 처리하게 하는 데 쓰인다. |
| 사가 | Saga | 오래 걸리는 작업을 작은 단계의 순서로 나누고 단계마다 보상 동작을 두어, 전부 완료되거나 부분 실행을 보상하게 하는 트랜잭션 구성 방식이다. |
| 마지막 유언 메시지 | Last Will (MQTT) | MQTT 클라이언트가 예기치 않게 끊기면 브로커가 대신 발행하도록 미리 등록해 둔 메시지로, VDA 5050 은 이를 로봇 연결 끊김(CONNECTION_BROKEN) 알림에 쓴다. |
| 관리형 노드 | Managed Node (ROS 2 Lifecycle Node) | Unconfigured·Inactive·Active·Finalized 상태와 전이를 가져 감독 도구가 준비 확인·재시작·교체를 제어할 수 있는 ROS 2 노드이다. |

## 열린 질문

새로 생긴 질문:

- 상위 시스템 요청의 중복을 판별하는 키(멱등성 키나 상위 요청 id)를 ROP 가 얼마 동안 보존해야 하는가, 운반 작업의 재전송 가능 기간에 맞춘 만료 기준을 정한 표준이나 사례가 있는가? | 관련 영역: 12. 명령·작업 실행의 신뢰성, 1. 주문·업무 시스템 연계 | 근거: f15 | 종류: 일반
- VDA 5050 로봇이 재부팅되면 받아 둔 주문을 유지하는지에 대한 규정이 명세에서 확인되지 않는데, 제조사 구현이나 공개 사례는 재부팅 뒤 주문·동작 상태를 어떻게 복원하거나 폐기하는가? | 관련 영역: 12. 명령·작업 실행의 신뢰성, 9. 로봇·제조사 관제 연동 | 근거: f4 | 종류: 일반
- Open-RMF 플릿 어댑터 재시작 시 작업 유실을 막는 작업 백업·복원 기능(SQLite 저장 제안)이 현재 배포판에 반영되었는가, 반영되었다면 복원 뒤 로봇의 실제 위치·적재 상태와 어떻게 대조하는가? | 관련 영역: 12. 명령·작업 실행의 신뢰성, 20. 예외 복구·재계획·업무 연속성 | 근거: f14 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 22 · 교차 확인: 0
- 예산 사용량: 검색 12회 · 신규 출처 14건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 표준·오픈소스마다 발행 주체 한 곳의 자료이거나 같은 저장소 안의 파일
    - f14 Open-RMF 이슈 #224 원문 미열람, 작업 백업 기능의 배포판 반영 여부 미확인
    - f16 MQTT 5.0 명세 원문 미열람(검색 요약 기준)
    - f20·f21 OPC UA Part 10, ISA-TR88.00.02 원문 미열람
    - f22 ISA-95 Job Control 상태 기계 상태 이름과 Store 메서드의 중복 id 반환 코드(부속서 B.2) 미확인
    - f27 브로커 비교 연구의 실험 조건·저자 미확인
    - f30 VDA 5050 의 상태 미수신 시 관제 대응 규정 부재는 열람 도구 응답 기준이며 부재 확정 아님
    - 국내 학술·현장 자료: 명령 중복·재시작 복원을 다룬 한국 자료를 검색 2회로 찾지 못함
- 범위 경계 위반 의심:
    - f29: 로봇 내부 재시도·정지 방식은 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이라 '연계 대상: '으로 표시함
    - f16·f27: MQTT 전달 보장·브로커 성능은 11. 분산 시스템·통신·컴퓨팅 구조와 겹치므로 12번 페이지에는 명령 중복 판단의 입력으로만 쓰도록 제안함
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 재사용 ref-031·ref-125·ref-126·ref-127·ref-130(documentation.csv)·ref-282(ros2_documentation jazzy 원본), 신규 ref-588·ref-589·ref-590·ref-591·ref-592·ref-597·ref-598. ref-130 NodeSet2.xml 은 응답이 잘려 상태 이름·반환 코드를 확인하지 못했다. task_dispatch_response.json 은 404 로 열지 못해 서버의 작업 id 부여 방식은 finding 으로 내지 않았다. 나머지 신규 7건과 재사용 ref-111·ref-129 는 원문 미열람이라 신뢰도 상한 medium. 모든 finding 신뢰도 medium 이하, 교차 확인 0건. 검색 12회/30, 신규 출처 14건/15(ref-588~ref-601, 예약 구간 안), 재사용 8건. 한국어 검색 2회에서 쓸 만한 한국 자료를 찾지 못했다(벤더 블로그·AI 요약뿐이라 출처로 넣지 않음). 행동 트리 용어는 용어집에 이미 있어 후보로 내지 않았다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음. 기존 열린 질문 oq-014·oq-021·oq-033 은 이번 조사로 해결되지 않았다(공통 상태 매핑·되돌림 규칙 표준을 찾지 못함).
