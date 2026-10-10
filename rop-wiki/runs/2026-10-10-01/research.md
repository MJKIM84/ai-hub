# 리서치 브리프 2026-10-10-01

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-01 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 24. 작업·워크플로 모델링 |
| 대분류 | G. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 — 첫 문단이 drop 완료·IngestorResult SUCCESS 를 CBV arriving 수준이라고 [추정]으로 묶어, 각 규격 정의(CBV 세 단계, VDA 5050 표 5, IngestorResult 기본 필드)의 원문 위치와 범위가 드러나지 않음
- 섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 가상 시나리오 2건뿐이고 다른 현장 유형(농업·지상 로봇 협업 등)의 공개 작업 모델링 사례가 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — BPMN 메시지 대기 근거가 벤더 문서(Camunda, ref-113)와 미열람 소개 페이지(ref-112)뿐이고, 취소 후 정리·보상, rmf_task_sequence 의 단계·이벤트 구성이 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — VDA 5050 3.0.0 의 blockingType(SINGLE 추가)과 rmf_fleet_adapter 의 최근 변경(2026-09-26)이 반영되지 않음
- 섹션 8. 대표 연구와 자료(주제 페이지로 분리) — Filippone 외(ref-116)가 원문 미열람 상태로 2026-03 초판 표기만 있고 연구 방법·게재처가 없음
- 섹션 11. 열린 질문(주제 페이지로 분리) — oq-001·oq-014 에 근거가 붙지 않았음

## 조사 질문

1. 현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? [분류원문]
2. 로봇의 하역 완료 신호(VDA 5050 drop FINISHED, IngestorResult SUCCESS)와 GS1 CBV 업무 단계(arriving·accepting·receiving)는 원문 정의상 어떻게 다른가? (섹션 3 겨냥)
3. 인수 확인 대기·상관·시간 초과를 BPMN 규범 원문은 어떤 요소로 정의하며, 취소 후 정리와 보상은 어떻게 다루는가? (섹션 6 겨냥)
4. Open-RMF rmf_task_sequence 는 작업을 어떤 단계·이벤트로 구성하며, 최근 변경(단계 건너뛰기)은 무엇인가? (섹션 6·7 겨냥)
5. VDA 5050 3.0.0 은 동작의 병행 가능성(blockingType)에서 무엇이 바뀌었는가? (섹션 7 겨냥)
6. oq-001 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가? (섹션 11 겨냥)
7. oq-014 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가? (섹션 5·8·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | GS1 핵심 업무 어휘(CBV) 2.0 온톨로지는 arriving 을 물체가 위치에 도착하는 활동, accepting 을 점유 또는 소유가 바뀌는 활동, receiving 을 위치에서 수령되어 수령자 재고에 편입되는 활동으로 구분하고, receiving 의 사용은 arriving·accepting 의 사용과 상호 배타적이라고 적는다. | ref-044 | 아니오 | medium | 2026-10-10 | 완료·인계 | — |
| f2 | [사실] | VDA 5050 3.0.0 은 미리 정의된 drop 동작의 FINISHED 상태를 하역이 끝나 적재물이 이동로봇을 떠나고 로봇이 새 적재 상태를 보고한 때로 정의한다. | ref-031 | 아니오 | medium | 2026-10-10 | 완료·인계 | — |
| f3 | [사실] | Open-RMF IngestorResult 메시지의 기본 정의 필드(time·request_guid·source_guid·status, status 는 ACKNOWLEDGED·SUCCESS·FAILED)에는 수령자 재고 편입 여부를 나타내는 필드가 없다. | ref-049 | 아니오 | medium | 2026-10-10 | 완료·인계 | — |
| f4 | [의견] | 로봇의 하역 완료(drop FINISHED, IngestorResult SUCCESS)를 특정 CBV 업무 단계와 자동으로 동일시하지 말고, 해당 업무의 인수·재고 확정 조건을 별도 완료 조건으로 모델링하는 편이 타당하다. | ref-044, ref-031, ref-049 | 아니오 | medium | 2026-10-10 | 완료·인계 | — |
| f5 | [사실] | BPMN 2.0.2 규범 문서는 외부 참여자의 메시지가 도착하면 완료되는 수신 작업(Receive Task), 메시지를 프로세스 인스턴스에 연결하는 상관 키(CorrelationKey), 지연·시간 조건을 표현하는 타이머 이벤트(Timer Event)를 정의한다. | ref-502 | 아니오 | medium | 2026-10-10 | — | — |
| f6 | [추정] | 운반 뒤 인수 확인 메시지를 기다리고 시간 초과 시 분기하는 구조는 BPMN 규범 요소(수신 작업·상관 키·타이머 이벤트)로 표현할 수 있어 특정 벤더 엔진에 한정되지 않지만, 로봇 작업 식별자나 화물 식별자를 어떤 상관 키로 쓸지는 구현에서 정해야 하는 것으로 보인다. | ref-502, ref-1423 | 아니오 | medium | 2026-10-10 | — | — |
| f7 | [사실] | FaMe 연구팀(University of Camerino PROS Lab)은 공식 페이지에서 지상 로봇 협업(ground vehicle cooperation)과 농업(agriculture scenario) 두 시나리오의 시뮬레이션 패키지와 엔진 패키지 빌드·실행 절차(colcon build, ros2 launch)를 공개한다. | ref-1423 | 아니오 | medium | 2026-10-10 | 기타 | — |
| f8 | [사실] | FaMe 모델링 지침은 로봇을 풀(Pool), 임무를 프로세스(Process), 동작을 활동(Activity)으로 나타내고, 병렬 동작은 AND 게이트웨이, 내부 선택은 XOR 게이트웨이, 시간 대기는 타이머 이벤트, 실행 오류는 오류 이벤트로 표현하게 한다. | ref-1423 | 아니오 | medium | 2026-10-10 | 기타 / 수행 자원 | — |
| f9 | [의견] | FaMe 예제는 창고 밖(농업·지상 로봇 협업)의 작업 모델링 사례로 5절에 추가할 수 있지만, 시뮬레이션 실험이므로 국내 상용 운영 실적이나 현장 성능 근거로 분류하지 않는 편이 좋다. | ref-1423 | 아니오 | low | 2026-10-10 | 기타 | — |
| f10 | [사실] | Open-RMF rmf_task 의 Task::Active::cancel() 주석은 취소 뒤에도 작업이 로봇을 짐 없는 상태로 되돌리기 위한 단계를 계속 수행할 수 있고(대기 단계가 그런 단계로 바뀔 수 있음), 완료 콜백이 호출되어야 취소가 끝난다고 설명한다. | ref-366 | 아니오 | medium | 2026-10-10 | 예외·성과 | — |
| f11 | [사실] | BPMN 2.0.2 는 이미 성공적으로 완료한 단계의 효과를 되돌리는 보상(Compensation)을 별도 개념으로 정의한다. | ref-502 | 아니오 | medium | 2026-10-10 | 예외·성과 | — |
| f12 | [의견] | 워크플로에는 취소 요청과 취소 후 정리 완료를 서로 다른 상태로 나누고, 실제 물건의 이동을 되돌릴 수 있는지에 따라 보상 단계를 따로 정의하는 편이 좋다. | ref-502, ref-366 | 아니오 | medium | 2026-10-10 | 예외·성과 | — |
| f13 | [사실] | Open-RMF rmf_task_sequence::Task 는 작업 완료를 위해 순서대로 실행할 단계(Phase)의 연쇄이고, 각 단계는 이벤트(Event)들로 구성되며, 모델은 rmf_task_sequence 에, 실제 로봇 명령 구현은 rmf_fleet_adapter 에 둔다. | ref-404 | 아니오 | medium | 2026-10-10 | — | — |
| f14 | [사실] | rmf_task README 는 rmf_task_sequence 가 기본 제공하는 이벤트로 Bundle, DropOff, GoToPlace, PerformAction, PickUp, Placeholder, WaitFor 일곱 가지를 열거한다. | ref-404 | 아니오 | medium | 2026-10-10 | — | — |
| f15 | [추정] | 기본 이벤트 목록과 단계 연쇄 구조만으로는 rmf_task_sequence 를 임의의 업무 병렬 분기·합류를 실행하는 범용 BPMN 엔진으로 보기 어려워 보인다. | ref-502, ref-404 | 아니오 | low | 2026-10-10 | — | — |
| f16 | [사실] | VDA 5050 3.0.0 은 동작의 blockingType 을 NONE·SINGLE·SOFT·HARD 네 값으로 두며, SINGLE 은 주행은 허용하되 다른 동작의 병렬 실행은 허용하지 않고 HARD 는 그 시점에 허용되는 유일한 동작이다. | ref-031 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f17 | [사실] | VDA 5050 2.1.0 명세의 blockingType 은 NONE·SOFT·HARD 세 값뿐이어서, SINGLE 은 3.0.0 에서 추가된 값이다. | ref-031, ref-1425 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f18 | [의견] | 주행과 작업 활동의 동시 수행 가능성을 공정 모델의 제약으로 표현할 때 VDA 5050 의 SINGLE 과 HARD 를 구별해 다루는 편이 좋다. | ref-031 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f19 | [사실] | Open-RMF rmf_fleet_adapter 패키지 2.14.0(2026-09-26) 변경 이력에는 단계 건너뛰기 요청의 키를 고친 항목 'Fix phase key for skip requests (#543)' 이 있다. | ref-1424 | 아니오 | medium | 2026-10-10 | — | — |
| f20 | [의견] | 단계 건너뛰기를 운영 정책에 넣는 구현은 rmf_fleet_adapter 패키지 버전과 건너뛰기 요청 스키마를 함께 기록해 두는 편이 좋다. | ref-1424, ref-366 | 아니오 | low | 2026-10-10 | — | — |
| f21 | [사실] | Filippone·Pettinari·Pelliccione 의 비교 연구(arXiv 2603.15427, v1 2026-03-16, v2 2026-08-17, Journal ref IEEE Transactions on Software Engineering (2026))는 행동 트리·상태 기계·계층적 작업 네트워크(HTN)·BPMN 을 제어 구조·임무 개념 표현(표현력)·도구 지원 기준으로 비교한다. | ref-116 | 아니오 | medium | 2026-10-10 | — | — |
| f22 | [사실] | 이 연구는 2026년 1월 4주 동안 83명에게 설문을 요청해 29개 완성 응답(응답률 34.94%)을 받고 일부 참여자와 후속 인터뷰(3명 실시간, 1명 서면)를 했으며, 같은 로봇 현장에서 형식별 처리량을 측정한 성능 비교가 아니라 분석 비교를 전문가 설문으로 검증한 연구다. | ref-116 | 아니오 | medium | 2026-10-10 | — | — |
| f23 | [의견] | Filippone 외 비교 연구는 임무 기술 형식 선택의 검토 자료로 쓰되, 특정 형식이 항상 우수하다는 결론으로 옮기지 않는 편이 좋다. | ref-116 | 아니오 | medium | 2026-10-10 | — | — |
| f24 | [사실] | FaMe 는 BPMN 협업 다이어그램으로 다중 로봇 임무를 정의하고 모델링·구성·실행 단계를 거쳐 각 로봇에서 ROS 2 위에 그 협업을 직접 실행하는 공개 프레임워크이며, 구성 단계에서 신호 이벤트의 type 속성에 ROS 메시지 형을 지정해 BPMN 이벤트와 ROS 메시지를 잇는다. | ref-1423 | 아니오 | medium | 2026-10-10 | — | — |
| f25 | [의견] | FaMe 는 BPMN 과 ROS 2 를 잇는 공개 구현이지만 Open-RMF 작업 상태나 VDA 5050 동작 상태와 BPMN 단계 상태 사이의 표준 매핑으로 볼 근거는 확인하지 못했으므로, oq-014 는 열린 상태로 두는 것이 맞다. | ref-1423, ref-031, ref-404 | 아니오 | medium | 2026-10-10 | — | — |
| f26 | [추정] | 확인한 원문들(CBV.ttl, VDA 5050 3.0.0, IngestorResult.msg)은 로봇 동작 완료와 업무 단계 각각의 정의까지만 제공하며, 로봇 하역 완료를 EPCIS 인계 이벤트로 옮기는 표준 변환은 확인되지 않는다. | ref-044, ref-031, ref-049 | 아니오 | medium | 2026-10-10 | — | — |
| f27 | [의견] | VDA 5050 drop 완료를 곧바로 CBV arriving 또는 receiving 으로 단정하지 않고, 업무 측 확인으로 어느 단계인지 정하는 수준까지만 oq-001 의 답을 보강하는 것이 적절하다. | ref-044, ref-031 | 아니오 | medium | 2026-10-10 | — | — |

### 근거 발췌

- **f1**: CBV.ttl BizStep-arriving "an object arrives at a location", BizStep-accepting "changes possession and/or ownership", BizStep-receiving "is being received at a location and is added to the receiver's inventory. The use of `receiving` is mutually exclusive from the use of `arriving` and `accepting`." (rdfs:comment, 2021-09-30 판, 확인일 기준)
- **f2**: 3.0.0 태그 명세 §6.2.3.2 Action states, Table 5 'Expected behavior in action states of predefined actions'의 drop 행 FINISHED 칸: "Drop has been done. Load has left the mobile robot and mobile robot reports new load state." (확인일 기준)
- **f3**: IngestorResult.msg: builtin_interfaces/Time time, string request_guid, string source_guid, uint8 status (ACKNOWLEDGED=0, SUCCESS=1, FAILED=2). 끝에 '# below are custom workcell message fields' 주석이 있어 워크셀별 추가 필드는 열려 있으므로 범위를 기본 정의 필드로 한정했다 (발행일 미확인, 확인일 기준)
- **f4**: f1~f3 의 정의를 대조한 판단. 세 규격 사이 공식 변환 매핑은 발견하지 못했다. CBV 가 receiving 과 arriving·accepting 을 상호 배타적으로 설명하므로 한 이벤트에 세 의미를 동시에 붙이는 근거로 쓰지 않는다. 3절 기존 [추정] 문장(ref-031·ref-049·ref-044)의 근거 범위를 좁히는 보완
- **f5**: OMG formal/2013-12-09(발행 2014-01). §10.3.3 Tasks(인쇄 p.159) "A Receive Task is a simple Task that is designed to wait for a Message to arrive from an external Participant ... Once the Message has been received, the Task is completed." §8.4.2 Correlation 의 CorrelationKey, §10.5.4 Intermediate Event 의 Timer(정상 흐름에서 지연 장치로 동작) (확인일 기준)
- **f6**: f5 의 규범 정의와 FaMe 모델링 지침 G5(Delays and timers via timer events)·G4(Execution errors via error events)·CONFIGURATION(signal event 의 type 을 ROS 메시지 형으로 지정)를 엮은 추정. 6절 분리 페이지의 기존 Camunda 근거 문장(ref-113, 벤더 주장)을 보완한다. Camunda 고유의 TTL·중복 거부 동작은 BPMN 표준의 보장으로 확대하지 않는다. 로봇 인수 확인에 적용한 사례는 미확인
- **f7**: FaMe 페이지 'Reproducing the simulation': "Download a simulation package (s.a. ground vehicle cooperation or agriculture scenario) and the engine package" 후 colcon build·ros2 launch·splitter 실행. 요구사항 Ubuntu 20.04+, ROS2 Foxy+, Gazebo(실제 로봇 실행에는 불필요). 페이지 게시일 2022-05-03. 현장 유형은 농업·지상 로봇 협업 시뮬레이션이며 실외 현장 운영 여부는 페이지에 명시 없음
- **f8**: MODELING 지침: G1 Robots as pools, G2 Mission as a process, G2.1 Actions as activities, G2.3 Concurrent behaviors by means of AND gateways, G2.4 Internal choices as XOR gateways, G4 Execution errors via error events, G5 Delays and timers via timer events (G1~G7). 기존 ref-503(FaMe GitHub README)·ref-114(Corradini 외 논문)와 같은 연구팀 자료이므로 독립 교차 확인으로 세지 않는다
- **f9**: 공식 페이지는 시뮬레이션 재현 절차와 모델링 지침을 제시한다. 연구팀의 실물 실험 사진이 있다는 메모 서술은 시뮬레이션 성능을 현장 성능으로 환산하는 근거로 쓰지 않았다. 국내 운영 실적은 확인 못 함
- **f10**: Task.hpp cancel(): "The Task may continue to perform some phases after being canceled. The pending_phases are likely to change after the Task is canceled, being replaced with phases that will help to relieve the robot ..." "When its finished callback is triggered, the cancellation is complete." kill() 은 cancel() 에 우선한다 (발행일 미확인, 확인일 기준)
- **f11**: §10.7 Compensation: "Compensation is concerned with undoing steps that were already successfully completed, because their results and possibly side effects are no longer desired and need to be reversed." (formal/2013-12-09, 확인일 기준)
- **f12**: f10·f11 근거. 두 자료가 같은 상태 체계를 공유한다는 뜻은 아니며, 공통으로 취소와 사후 처리를 구별한다는 설계 근거다. rmf_task README 도 단계마다 취소·중단 시 반응을 지정할 수 있다고 적는다
- **f13**: rmf_task README rmf_task_sequence 절: "a task to be composed of a sequence of phases that need to be executed in-order ... A phase inturn may be composed of a set of Events." Usage 절: 모델 구현은 rmf_task_sequence, Active 구현은 rmf_fleet_adapter; fleet adapter 는 현재 rmf_task_sequence 의 단계 연쇄 작업만 지원 (발행일 미확인, 확인일 기준)
- **f14**: README rmf_task_sequence 절 이벤트 목록(알파벳순): Bundle, DropOff, GoToPlace, PerformAction, PickUp, Placeholder, WaitFor — 메모는 Placeholder 를 빠뜨렸으나 검증에서 7개로 정정 (확인일 기준)
- **f15**: f13·f14 와 BPMN 게이트웨이 개념의 대조. 지원 이벤트의 존재와 임의 업무 그래프 지원은 구분했다. Bundle 의 정확한 병렬·합류 의미는 원문에서 확인하지 않았다
- **f16**: 3.0.0 태그 명세 §6.2.2 Action blocking types and sequence, Table 3(주행·병렬 실행에 따른 blocking type 정의); 필드 표 "'SINGLE': allows driving but no other actions; 'SOFT': allows other actions but not driving; 'HARD': is the only allowed action at that time." (발표일은 근거 미확인이라 적지 않음)
- **f17**: 2.1.0 태그 명세: blockingType "Enum {'NONE', 'SOFT', 'HARD'}", "Actions can have three distinct blocking types, described in Table 3." 2.1.0 본문에 SINGLE 문자열 없음. 3.0.0 은 "four distinct blocking types"(§6.2.2). 같은 발행 계열 두 판의 대조이며 독립 교차 확인은 아니다. 릴리스 노트 페이지는 원문 미확인이라 근거에서 뺐다
- **f18**: f16 의 정의(SINGLE 은 주행 허용, HARD 는 유일 동작)에서 끌어낸 모델링 권고. 메모는 이 문장을 [사실]로 달았으나 '구별해야 한다'는 판단이라 의견으로 분리
- **f19**: rmf_ros2 2.14.0 태그의 rmf_fleet_adapter/CHANGELOG.rst '2.14.0 (2026-09-26)' 절: "Fix phase key for skip requests (#543)". 고친 키의 실제 이름은 변경 이력만으로 확인하지 않았다. 개별 패키지 버전이며 Open-RMF 전체 배포판 버전이 아니다
- **f20**: f19 의 변경과 Task.hpp skip(phase_id, value) — 운영자가 수동 개입으로 특정 단계를 건너뛰게 하는 API — 를 근거로 한 운영 권고
- **f21**: arXiv abs 페이지 "Submitted on 16 Mar 2026 (v1), last revised 17 Aug 2026 (this version, v2)", Journal ref "IEEE Transactions on Software Engineering (2026)". v2 본문 §IV~VI 비교, 표 II(제어 구조)·IV·VI·VII 확인 (확인일 기준)
- **f22**: v2 §III: "29 complete responses out of 83 invitations, corresponding to a response rate of 34.94%"(2026-01, 4주), "Three participants ... were interviewed in live sessions, while one ... provided written responses". 결과는 completeness·correctness·alignment 리커트 평가. 같은 논문의 재열람이며 독립 교차 확인 아님
- **f23**: f22 의 연구 방법(분석 비교 + 전문가 설문)과 §VII 타당성 위협 절을 근거로 한 판단
- **f24**: FaMe 페이지 Framework Description: "allows the definition of an MRS mission using BPMN Collaborations and the execution of the system exploiting the ROS2 framework ... modeling, configuration, and enactment"; "The enactment phase executes the BPMN collaboration directly on each involved robot." CONFIGURATION > Signal Events: "Add a property named type, with a value equal to the ROS message type". oq-014 부분 근거
- **f25**: FaMe 페이지·VDA 5050 3.0.0 명세·rmf_task README 어디에도 서로의 상태를 대응시키는 매핑 절이 없음. oq-014 부분 답변
- **f26**: oq-001 부분 답변. 세 원문 어디에도 상대 규격을 참조하는 매핑 절이 없다. 공개 구현 사례 검색은 이번 메모 범위에서 하지 않았으므로 '없음'이 아니라 '확인 못 함'
- **f27**: f1·f2 와 CBV 의 receiving 상호 배타 규정을 근거로 한 판단. oq-001 은 열린 상태 유지

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | 표준 | high | 2026-10-10 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-10 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg | 아니오 |
| ref-502 | OMG(Object Management Group) | Business Process Model and Notation (BPMN), Version 2.0.2 | 2014-01 | 표준 | high | 2026-10-10 | https://www.omg.org/spec/BPMN/2.0.2/ | 아니오 |
| ref-1423 | University of Camerino PROS Lab | FaMe — A BPMN-driven Framework for Multi-Robot System Development (공식 페이지·사용 지침) | 2022-05-03 | 정부·연구기관 | medium | 2026-10-10 | https://pros.unicam.it/fame/ | 아니오 |
| ref-366 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/Task.hpp | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp | 아니오 |
| ref-404 | Open Robotics (open-rmf) | rmf_task — README | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_task | 아니오 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03-16 | 논문 | medium | 2026-10-10 | https://arxiv.org/abs/2603.15427 | 아니오 |
| ref-1424 | Open Robotics (open-rmf) | rmf_ros2 (tag 2.14.0) — rmf_fleet_adapter/CHANGELOG.rst | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |
| ref-1425 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 (tag 2.1.0) — VDA5050_EN.md | 미확인 | 표준 | high | 2026-10-10 | https://github.com/VDA5050/VDA5050/blob/2.1.0/VDA5050_EN.md | 아니오 |

### 출처 요약

- **ref-044**: GS1 CBV 2.0 온톨로지. arriving·accepting·receiving 등 업무 단계(BizStep)의 정의와 receiving 의 상호 배타 규정을 담는다.
- **ref-031**: VDA 5050 공식 명세 본문. 이번에는 3.0.0 태그 고정판을 열어 §6.2.2 표 3(blockingType 네 값, SINGLE)과 §6.2.3.2 표 5(drop FINISHED 정의)를 확인했다. 발표일은 근거 미확인.
- **ref-049**: Open-RMF 하역 워크셀 결과 메시지 정의. 기본 필드는 time·request_guid·source_guid·status(ACKNOWLEDGED·SUCCESS·FAILED)이고 워크셀별 추가 필드 주석이 있다.
- **ref-502**: BPMN 2.0.2 규범 문서(formal/2013-12-09). 수신 작업(§10.3.3, 인쇄 p.159)·상관 키(§8.4.2)·타이머 등 중간 이벤트(§10.5.4)·보상(§10.7)을 정의한다.
- **ref-1423**: FaMe 연구팀의 공식 페이지. 지상 로봇 협업·농업 시뮬레이션 재현 절차, BPMN 모델링 지침 G1~G7, 구성 절차(신호 이벤트와 ROS 메시지 형 연결)를 제시한다. 기존 ref-503(GitHub README)·ref-114(논문)와 같은 연구팀 자료다.
- **ref-366**: Open-RMF 작업 인터페이스 헤더. Task::Active 의 cancel()·kill()·skip() 의 의미(취소 후 정리 단계, 완료 콜백으로 취소 종료)를 주석으로 설명한다.
- **ref-404**: rmf_task 저장소 README. rmf_task_sequence 의 단계·이벤트 구조와 기본 이벤트 7종(Bundle·DropOff·GoToPlace·PerformAction·PickUp·Placeholder·WaitFor), 모델과 실행 구현의 위치를 설명한다.
- **ref-116**: 행동 트리·상태 기계·HTN·BPMN 을 제어 구조·표현력·도구 지원으로 비교하고 전문가 설문(83명 요청, 29개 응답)과 후속 인터뷰로 검증한 연구. v1 2026-03-16, v2 2026-08-17, Journal ref IEEE Transactions on Software Engineering (2026). 이번에 v2 본문을 열람했다.
- **ref-1424**: rmf_fleet_adapter 패키지 변경 이력. 2.14.0(2026-09-26) 절에 단계 건너뛰기 요청 키 수정(#543) 항목이 있다.
- **ref-1425**: VDA 5050 2.1.0 명세 본문. blockingType 을 NONE·SOFT·HARD 세 값으로 정의해 3.0.0 의 SINGLE 추가를 대조하는 근거가 된다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/task-and-workflow-modeling.md | 3, 5, 6, 7, 8, 11 | 갱신(차등, 외부 조사 메모 변환): 섹션 3 — 첫 문단의 근거를 원문 정의로 구체화: CBV 세 단계(f1), drop FINISHED 표 5(f2), IngestorResult 기본 필드 범위(f3), 별도 완료 조건 권고(f4, 의견) / 섹션 5 — 창고 밖 사례로 FaMe 농업·지상 로봇 협업 시뮬레이션(f7·f8, site_type 기타)과 분류 한계(f9) 추가 / 섹션 6(주제 페이지 2026-09-25-area02-s6 요약) — BPMN 규범 근거로 수신 작업·상관 키·타이머(f5·f6, 기존 Camunda 문장 보완), 취소 후 정리·보상(f10~f12), rmf_task_sequence 단계·이벤트 7종(f13~f15) / 섹션 7(주제 페이지 2026-09-25-area02-s7 요약) — VDA 5050 3.0.0 blockingType SINGLE(f16·f17, 발표일 언급 없음)과 SINGLE·HARD 구별 권고(f18, 의견), rmf_fleet_adapter 2.14.0 단계 건너뛰기 키 수정(f19·f20); 표의 BPMN 행을 2.0.2 규범판(ref-502)으로 보강 / 섹션 8(주제 페이지 2026-09-25-area02-s8 요약) — Filippone 외(ref-116) 항목을 v2·게재처·연구 방법으로 보강(f21~f23); FaMe 항목(ref-114)은 기존 내용 확인 / 섹션 11(주제 페이지 2026-09-25-area02-s11) — oq-014 부분 근거(f24·f25), oq-001 부분 근거(f26·f27), 새 질문 3건. 섹션 4·9·10 은 바꾸지 않는다. 다음 실행 후보: 32. 예외 복구·재계획·업무 연속성(f10~f12), 20. 로봇·제조사 관제 연동(f16~f18), 17. 작업 대상·자산 식별과 인계 추적(f1~f4). |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 수신 작업 | Receive Task (BPMN) | 외부 참여자가 보낸 메시지가 도착할 때까지 기다리다가 메시지를 받으면 완료되는 BPMN 작업 유형이다. |
| 보상 | Compensation (BPMN) | 이미 성공적으로 끝난 단계의 결과가 더는 필요 없을 때 그 효과를 되돌리는 처리를 별도 활동으로 표현하는 BPMN 개념이다. |

## 열린 질문

새로 생긴 질문:

- 로봇이 이미 하역한 뒤 작업이 취소되면, 로봇 쪽 정리 단계 완료와 업무상 인수 취소(재고 반영 취소)를 어떤 완료 조건으로 나눠야 하는가? | 관련 영역: 24. 작업·워크플로 모델링, 32. 예외 복구·재계획·업무 연속성 | 근거: f10 | 종류: 일반
- Open-RMF rmf_task_sequence 의 Bundle 이벤트와 BPMN 병렬 게이트웨이 합류의 의미 차이를 자동으로 검사하거나 변환하는 공개 도구가 있는가? | 관련 영역: 24. 작업·워크플로 모델링, 54. 시험·형식 검증·벤치마크 | 근거: f15 | 종류: 일반
- 운영 정책 버전이 바뀔 때 이미 시작한 워크플로 인스턴스가 이전 정책을 유지하는지 새 정책으로 옮기는지에 대한 공개 운영 기준이 있는가? | 관련 영역: 24. 작업·워크플로 모델링, 57. 자산·소프트웨어 수명주기 관리 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 10 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 3건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-01/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - VDA 5050 3.0.0 의 발표일(메모의 2026-03-19)은 근거를 확인하지 못해 적지 않았고(ref-031 published null), 릴리스 노트 페이지(메모 n10)는 원문 확인이 안 돼 출처에서 뺐다
    - f19: 'Fix phase key for skip requests (#543)' 에서 고친 키의 실제 이름은 변경 이력만으로 확인하지 않았다(#543 본문 미열람)
    - f15: rmf_task_sequence Bundle 이벤트의 병렬·합류 의미는 API 문서를 열지 않아 미확인
    - f7~f9: FaMe 시뮬레이션 시나리오가 실외 현장인지, 실물 로봇 실험의 규모는 공식 페이지에서 확인하지 못했다(site_type 기타)
    - f26: 로봇 하역 완료를 EPCIS 이벤트로 옮기는 공개 구현 사례는 이번 메모 범위에서 검색하지 않았다(확인 못 함)
    - ref-1425(VDA 5050 2.1.0) 발행일 미확인
- 범위 경계 위반 의심:
    - f16~f18: VDA 5050 blockingType 은 로봇·제조사 관제 인터페이스(20. 로봇·제조사 관제 연동) 쪽 정의이므로 이 영역에서는 공정 모델의 병행 제약 근거로만 쓴다
    - f10~f12: 취소·보상 처리 절차는 32. 예외 복구·재계획·업무 연속성과 겹치며, 이 영역에서는 워크플로의 상태·완료 조건 구분으로 한정한다
    - f1~f4: 재고 확정(CBV receiving)은 상위 업무 시스템(WMS) 연계 대상이며 ROP 는 완료 조건 구분과 대기만 맡는다
- 한계: 외부 조사 변환이라 검색·열람 집계 없음(queries 0 은 실제 검색 수가 아니다). web_fetch_available: true. 신규 출처 3건(ref-1423~ref-1425, 예약 구간 ref-1423~ref-1452 안), 기존 id 재사용 7건(ref-044·ref-031·ref-049·ref-502·ref-366·ref-404·ref-116). 메모의 출처 10개 중 n10(VDA 5050 3.0.0 릴리스 노트)은 원문 미확인으로 제외하고, SINGLE 추가의 대조 근거로 VDA 5050 2.1.0 명세(ref-1425)를 더했다. 메모의 n2(3.0.0 태그 명세)는 main 판 ref-031 과 같은 문서로 보아 ref-031 에 3.0.0 태그 raw 경로를 fetch_url 로 적었고, n4(BPMN 2.0.2 PDF)는 ref-502 와 같은 문서다. 검증 수정 반영: SINGLE 정의는 사실(f16)·'구별해야 한다'는 의견(f18)으로 분리, 발표일 삭제, IngestorResult 범위를 기본 정의 필드로 한정(f3), rmf_task_sequence 이벤트 7개(Placeholder 포함, f14), 변경 이력 키 이름 단정 안 함(f19), Filippone 외 v1·v2 날짜와 IEEE TSE 게재 정보 추가(f21), drop FINISHED 근거 위치 §6.2.3.2 표 5(f2), BPMN 2.0.2 서지(formal/2013-12-09, 2014-01)와 절 위치(f5·f11), FaMe 공식 페이지는 ref-503·ref-114 와 같은 연구팀 자료라 독립 교차 확인으로 세지 않음(f8). 교차 확인 0건이며 사실 finding 은 단일 출처라 신뢰도 medium 이하. 현장 유형 사례 finding 은 FaMe 농업·지상 로봇 협업 시뮬레이션(f7~f9, 기타)뿐이다. 열린 질문 해결 제안 없음: oq-001(f26·f27)·oq-014(f24·f25) 부분 근거만 냈다. oq-012·oq-013 근거 없음. 국내 자료 없음.
