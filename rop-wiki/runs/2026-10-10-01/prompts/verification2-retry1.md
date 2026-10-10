(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-10-01
- date: 2026-10-10
- run_type: update (갱신)
- 대상: 24. 작업·워크플로 모델링 (G. 계획·최적화)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- verification_stage: second
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- retry_count: 1
- max_retries: 2

## 입력

### runs/2026-10-10-01/target.json

```json
{
  "run_id": "2026-10-10-01",
  "date": "2026-10-10",
  "weekday": "Sat",
  "run_number": 161,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 24,
    "area_name": "24. 작업·워크플로 모델링",
    "category": "G. 계획·최적화",
    "category_letter": "G"
  },
  "topic": null,
  "track": null,
  "corrections": [],
  "budget": {
    "max_search_queries": 30,
    "max_sources_per_run": 15,
    "new_topic_pages": 1,
    "page_updates": 2,
    "max_retries": 2
  },
  "priority_reason": null,
  "priority_questions": [],
  "excluded_areas": [],
  "lifted_areas": [],
  "deferred": {
    "monthly_recheck": false,
    "weekly_review": false
  },
  "selection_rationale": "CLI 지정 run_type=update, area=24"
}
```

### runs/2026-10-10-01/research.json

```json
{
  "run_id": "2026-10-10-01",
  "date": "2026-10-10",
  "run_type": "update",
  "target": {
    "area_no": 24,
    "area_name": "24. 작업·워크플로 모델링",
    "category": "G. 계획·최적화"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 — 첫 문단이 drop 완료·IngestorResult SUCCESS 를 CBV arriving 수준이라고 [추정]으로 묶어, 각 규격 정의(CBV 세 단계, VDA 5050 표 5, IngestorResult 기본 필드)의 원문 위치와 범위가 드러나지 않음",
    "섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 가상 시나리오 2건뿐이고 다른 현장 유형(농업·지상 로봇 협업 등)의 공개 작업 모델링 사례가 없음",
    "섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — BPMN 메시지 대기 근거가 벤더 문서(Camunda, ref-113)와 미열람 소개 페이지(ref-112)뿐이고, 취소 후 정리·보상, rmf_task_sequence 의 단계·이벤트 구성이 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — VDA 5050 3.0.0 의 blockingType(SINGLE 추가)과 rmf_fleet_adapter 의 최근 변경(2026-09-26)이 반영되지 않음",
    "섹션 8. 대표 연구와 자료(주제 페이지로 분리) — Filippone 외(ref-116)가 원문 미열람 상태로 2026-03 초판 표기만 있고 연구 방법·게재처가 없음",
    "섹션 11. 열린 질문(주제 페이지로 분리) — oq-001·oq-014 에 근거가 붙지 않았음"
  ],
  "research_questions": [
    "현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? [분류원문]",
    "로봇의 하역 완료 신호(VDA 5050 drop FINISHED, IngestorResult SUCCESS)와 GS1 CBV 업무 단계(arriving·accepting·receiving)는 원문 정의상 어떻게 다른가? (섹션 3 겨냥)",
    "인수 확인 대기·상관·시간 초과를 BPMN 규범 원문은 어떤 요소로 정의하며, 취소 후 정리와 보상은 어떻게 다루는가? (섹션 6 겨냥)",
    "Open-RMF rmf_task_sequence 는 작업을 어떤 단계·이벤트로 구성하며, 최근 변경(단계 건너뛰기)은 무엇인가? (섹션 6·7 겨냥)",
    "VDA 5050 3.0.0 은 동작의 병행 가능성(blockingType)에서 무엇이 바뀌었는가? (섹션 7 겨냥)",
    "oq-001 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가? (섹션 11 겨냥)",
    "oq-014 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가? (섹션 5·8·11 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "GS1 핵심 업무 어휘(CBV) 2.0 온톨로지는 arriving 을 물체가 위치에 도착하는 활동, accepting 을 점유 또는 소유가 바뀌는 활동, receiving 을 위치에서 수령되어 수령자 재고에 편입되는 활동으로 구분하고, receiving 의 사용은 arriving·accepting 의 사용과 상호 배타적이라고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-044"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "CBV.ttl BizStep-arriving \"an object arrives at a location\", BizStep-accepting \"changes possession and/or ownership\", BizStep-receiving \"is being received at a location and is added to the receiver's inventory. The use of `receiving` is mutually exclusive from the use of `arriving` and `accepting`.\" (rdfs:comment, 2021-09-30 판, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f2",
      "claim": "VDA 5050 3.0.0 은 미리 정의된 drop 동작의 FINISHED 상태를 하역이 끝나 적재물이 이동로봇을 떠나고 로봇이 새 적재 상태를 보고한 때로 정의한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3.0.0 태그 명세 §6.2.3.2 Action states, Table 5 'Expected behavior in action states of predefined actions'의 drop 행 FINISHED 칸: \"Drop has been done. Load has left the mobile robot and mobile robot reports new load state.\" (확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f3",
      "claim": "Open-RMF IngestorResult 메시지의 기본 정의 필드(time·request_guid·source_guid·status, status 는 ACKNOWLEDGED·SUCCESS·FAILED)에는 수령자 재고 편입 여부를 나타내는 필드가 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-049"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IngestorResult.msg: builtin_interfaces/Time time, string request_guid, string source_guid, uint8 status (ACKNOWLEDGED=0, SUCCESS=1, FAILED=2). 끝에 '# below are custom workcell message fields' 주석이 있어 워크셀별 추가 필드는 열려 있으므로 범위를 기본 정의 필드로 한정했다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f4",
      "claim": "로봇의 하역 완료(drop FINISHED, IngestorResult SUCCESS)를 특정 CBV 업무 단계와 자동으로 동일시하지 말고, 해당 업무의 인수·재고 확정 조건을 별도 완료 조건으로 모델링하는 편이 타당하다.",
      "tag": "의견",
      "source_ids": [
        "ref-044",
        "ref-031",
        "ref-049"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f1~f3 의 정의를 대조한 판단. 세 규격 사이 공식 변환 매핑은 발견하지 못했다. CBV 가 receiving 과 arriving·accepting 을 상호 배타적으로 설명하므로 한 이벤트에 세 의미를 동시에 붙이는 근거로 쓰지 않는다. 3절 기존 [추정] 문장(ref-031·ref-049·ref-044)의 근거 범위를 좁히는 보완",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f5",
      "claim": "BPMN 2.0.2 규범 문서는 외부 참여자의 메시지가 도착하면 완료되는 수신 작업(Receive Task), 메시지를 프로세스 인스턴스에 연결하는 상관 키(CorrelationKey), 지연·시간 조건을 표현하는 타이머 이벤트(Timer Event)를 정의한다.",
      "tag": "사실",
      "source_ids": [
        "ref-502"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "OMG formal/2013-12-09(발행 2014-01). §10.3.3 Tasks(인쇄 p.159) \"A Receive Task is a simple Task that is designed to wait for a Message to arrive from an external Participant ... Once the Message has been received, the Task is completed.\" §8.4.2 Correlation 의 CorrelationKey, §10.5.4 Intermediate Event 의 Timer(정상 흐름에서 지연 장치로 동작) (확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "운반 뒤 인수 확인 메시지를 기다리고 시간 초과 시 분기하는 구조는 BPMN 규범 요소(수신 작업·상관 키·타이머 이벤트)로 표현할 수 있어 특정 벤더 엔진에 한정되지 않지만, 로봇 작업 식별자나 화물 식별자를 어떤 상관 키로 쓸지는 구현에서 정해야 하는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-502",
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f5 의 규범 정의와 FaMe 모델링 지침 G5(Delays and timers via timer events)·G4(Execution errors via error events)·CONFIGURATION(signal event 의 type 을 ROS 메시지 형으로 지정)를 엮은 추정. 6절 분리 페이지의 기존 Camunda 근거 문장(ref-113, 벤더 주장)을 보완한다. Camunda 고유의 TTL·중복 거부 동작은 BPMN 표준의 보장으로 확대하지 않는다. 로봇 인수 확인에 적용한 사례는 미확인",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "FaMe 연구팀(University of Camerino PROS Lab)은 공식 페이지에서 지상 로봇 협업(ground vehicle cooperation)과 농업(agriculture scenario) 두 시나리오의 시뮬레이션 패키지와 엔진 패키지 빌드·실행 절차(colcon build, ros2 launch)를 공개한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "FaMe 페이지 'Reproducing the simulation': \"Download a simulation package (s.a. ground vehicle cooperation or agriculture scenario) and the engine package\" 후 colcon build·ros2 launch·splitter 실행. 요구사항 Ubuntu 20.04+, ROS2 Foxy+, Gazebo(실제 로봇 실행에는 불필요). 페이지 게시일 2022-05-03. 현장 유형은 농업·지상 로봇 협업 시뮬레이션이며 실외 현장 운영 여부는 페이지에 명시 없음",
      "as_of": "2026-10-10",
      "site_type": "기타",
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "FaMe 모델링 지침은 로봇을 풀(Pool), 임무를 프로세스(Process), 동작을 활동(Activity)으로 나타내고, 병렬 동작은 AND 게이트웨이, 내부 선택은 XOR 게이트웨이, 시간 대기는 타이머 이벤트, 실행 오류는 오류 이벤트로 표현하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "MODELING 지침: G1 Robots as pools, G2 Mission as a process, G2.1 Actions as activities, G2.3 Concurrent behaviors by means of AND gateways, G2.4 Internal choices as XOR gateways, G4 Execution errors via error events, G5 Delays and timers via timer events (G1~G7). 기존 ref-503(FaMe GitHub README)·ref-114(Corradini 외 논문)와 같은 연구팀 자료이므로 독립 교차 확인으로 세지 않는다",
      "as_of": "2026-10-10",
      "site_type": "기타",
      "flow_item": "수행 자원"
    },
    {
      "id": "f9",
      "claim": "FaMe 예제는 창고 밖(농업·지상 로봇 협업)의 작업 모델링 사례로 5절에 추가할 수 있지만, 시뮬레이션 실험이므로 국내 상용 운영 실적이나 현장 성능 근거로 분류하지 않는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "공식 페이지는 시뮬레이션 재현 절차와 모델링 지침을 제시한다. 연구팀의 실물 실험 사진이 있다는 메모 서술은 시뮬레이션 성능을 현장 성능으로 환산하는 근거로 쓰지 않았다. 국내 운영 실적은 확인 못 함",
      "as_of": "2026-10-10",
      "site_type": "기타",
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "Open-RMF rmf_task 의 Task::Active::cancel() 주석은 취소 뒤에도 작업이 로봇을 짐 없는 상태로 되돌리기 위한 단계를 계속 수행할 수 있고(대기 단계가 그런 단계로 바뀔 수 있음), 완료 콜백이 호출되어야 취소가 끝난다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-366"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Task.hpp cancel(): \"The Task may continue to perform some phases after being canceled. The pending_phases are likely to change after the Task is canceled, being replaced with phases that will help to relieve the robot ...\" \"When its finished callback is triggered, the cancellation is complete.\" kill() 은 cancel() 에 우선한다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f11",
      "claim": "BPMN 2.0.2 는 이미 성공적으로 완료한 단계의 효과를 되돌리는 보상(Compensation)을 별도 개념으로 정의한다.",
      "tag": "사실",
      "source_ids": [
        "ref-502"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§10.7 Compensation: \"Compensation is concerned with undoing steps that were already successfully completed, because their results and possibly side effects are no longer desired and need to be reversed.\" (formal/2013-12-09, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f12",
      "claim": "워크플로에는 취소 요청과 취소 후 정리 완료를 서로 다른 상태로 나누고, 실제 물건의 이동을 되돌릴 수 있는지에 따라 보상 단계를 따로 정의하는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-502",
        "ref-366"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f10·f11 근거. 두 자료가 같은 상태 체계를 공유한다는 뜻은 아니며, 공통으로 취소와 사후 처리를 구별한다는 설계 근거다. rmf_task README 도 단계마다 취소·중단 시 반응을 지정할 수 있다고 적는다",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "Open-RMF rmf_task_sequence::Task 는 작업 완료를 위해 순서대로 실행할 단계(Phase)의 연쇄이고, 각 단계는 이벤트(Event)들로 구성되며, 모델은 rmf_task_sequence 에, 실제 로봇 명령 구현은 rmf_fleet_adapter 에 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-404"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "rmf_task README rmf_task_sequence 절: \"a task to be composed of a sequence of phases that need to be executed in-order ... A phase inturn may be composed of a set of Events.\" Usage 절: 모델 구현은 rmf_task_sequence, Active 구현은 rmf_fleet_adapter; fleet adapter 는 현재 rmf_task_sequence 의 단계 연쇄 작업만 지원 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "rmf_task README 는 rmf_task_sequence 가 기본 제공하는 이벤트로 Bundle, DropOff, GoToPlace, PerformAction, PickUp, Placeholder, WaitFor 일곱 가지를 열거한다.",
      "tag": "사실",
      "source_ids": [
        "ref-404"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README rmf_task_sequence 절 이벤트 목록(알파벳순): Bundle, DropOff, GoToPlace, PerformAction, PickUp, Placeholder, WaitFor — 메모는 Placeholder 를 빠뜨렸으나 검증에서 7개로 정정 (확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "기본 이벤트 목록과 단계 연쇄 구조만으로는 rmf_task_sequence 를 임의의 업무 병렬 분기·합류를 실행하는 범용 BPMN 엔진으로 보기 어려워 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-502",
        "ref-404"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f13·f14 와 BPMN 게이트웨이 개념의 대조. 지원 이벤트의 존재와 임의 업무 그래프 지원은 구분했다. Bundle 의 정확한 병렬·합류 의미는 원문에서 확인하지 않았다",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "VDA 5050 3.0.0 은 동작의 blockingType 을 NONE·SINGLE·SOFT·HARD 네 값으로 두며, SINGLE 은 주행은 허용하되 다른 동작의 병렬 실행은 허용하지 않고 HARD 는 그 시점에 허용되는 유일한 동작이다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3.0.0 태그 명세 §6.2.2 Action blocking types and sequence, Table 3(주행·병렬 실행에 따른 blocking type 정의); 필드 표 \"'SINGLE': allows driving but no other actions; 'SOFT': allows other actions but not driving; 'HARD': is the only allowed action at that time.\" (발표일은 근거 미확인이라 적지 않음)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f17",
      "claim": "VDA 5050 2.1.0 명세의 blockingType 은 NONE·SOFT·HARD 세 값뿐이어서, SINGLE 은 3.0.0 에서 추가된 값이다.",
      "tag": "사실",
      "source_ids": [
        "ref-031",
        "ref-1425"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2.1.0 태그 명세: blockingType \"Enum {'NONE', 'SOFT', 'HARD'}\", \"Actions can have three distinct blocking types, described in Table 3.\" 2.1.0 본문에 SINGLE 문자열 없음. 3.0.0 은 \"four distinct blocking types\"(§6.2.2). 같은 발행 계열 두 판의 대조이며 독립 교차 확인은 아니다. 릴리스 노트 페이지는 원문 미확인이라 근거에서 뺐다",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f18",
      "claim": "주행과 작업 활동의 동시 수행 가능성을 공정 모델의 제약으로 표현할 때 VDA 5050 의 SINGLE 과 HARD 를 구별해 다루는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f16 의 정의(SINGLE 은 주행 허용, HARD 는 유일 동작)에서 끌어낸 모델링 권고. 메모는 이 문장을 [사실]로 달았으나 '구별해야 한다'는 판단이라 의견으로 분리",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f19",
      "claim": "Open-RMF rmf_fleet_adapter 패키지 2.14.0(2026-09-26) 변경 이력에는 단계 건너뛰기 요청의 키를 고친 항목 'Fix phase key for skip requests (#543)' 이 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1424"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "rmf_ros2 2.14.0 태그의 rmf_fleet_adapter/CHANGELOG.rst '2.14.0 (2026-09-26)' 절: \"Fix phase key for skip requests (#543)\". 고친 키의 실제 이름은 변경 이력만으로 확인하지 않았다. 개별 패키지 버전이며 Open-RMF 전체 배포판 버전이 아니다",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "단계 건너뛰기를 운영 정책에 넣는 구현은 rmf_fleet_adapter 패키지 버전과 건너뛰기 요청 스키마를 함께 기록해 두는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1424",
        "ref-366"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f19 의 변경과 Task.hpp skip(phase_id, value) — 운영자가 수동 개입으로 특정 단계를 건너뛰게 하는 API — 를 근거로 한 운영 권고",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "Filippone·Pettinari·Pelliccione 의 비교 연구(arXiv 2603.15427, v1 2026-03-16, v2 2026-08-17, Journal ref IEEE Transactions on Software Engineering (2026))는 행동 트리·상태 기계·계층적 작업 네트워크(HTN)·BPMN 을 제어 구조·임무 개념 표현(표현력)·도구 지원 기준으로 비교한다.",
      "tag": "사실",
      "source_ids": [
        "ref-116"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv abs 페이지 \"Submitted on 16 Mar 2026 (v1), last revised 17 Aug 2026 (this version, v2)\", Journal ref \"IEEE Transactions on Software Engineering (2026)\". v2 본문 §IV~VI 비교, 표 II(제어 구조)·IV·VI·VII 확인 (확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "이 연구는 2026년 1월 4주 동안 83명에게 설문을 요청해 29개 완성 응답(응답률 34.94%)을 받고 일부 참여자와 후속 인터뷰(3명 실시간, 1명 서면)를 했으며, 같은 로봇 현장에서 형식별 처리량을 측정한 성능 비교가 아니라 분석 비교를 전문가 설문으로 검증한 연구다.",
      "tag": "사실",
      "source_ids": [
        "ref-116"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v2 §III: \"29 complete responses out of 83 invitations, corresponding to a response rate of 34.94%\"(2026-01, 4주), \"Three participants ... were interviewed in live sessions, while one ... provided written responses\". 결과는 completeness·correctness·alignment 리커트 평가. 같은 논문의 재열람이며 독립 교차 확인 아님",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "Filippone 외 비교 연구는 임무 기술 형식 선택의 검토 자료로 쓰되, 특정 형식이 항상 우수하다는 결론으로 옮기지 않는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-116"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f22 의 연구 방법(분석 비교 + 전문가 설문)과 §VII 타당성 위협 절을 근거로 한 판단",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "FaMe 는 BPMN 협업 다이어그램으로 다중 로봇 임무를 정의하고 모델링·구성·실행 단계를 거쳐 각 로봇에서 ROS 2 위에 그 협업을 직접 실행하는 공개 프레임워크이며, 구성 단계에서 신호 이벤트의 type 속성에 ROS 메시지 형을 지정해 BPMN 이벤트와 ROS 메시지를 잇는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "FaMe 페이지 Framework Description: \"allows the definition of an MRS mission using BPMN Collaborations and the execution of the system exploiting the ROS2 framework ... modeling, configuration, and enactment\"; \"The enactment phase executes the BPMN collaboration directly on each involved robot.\" CONFIGURATION > Signal Events: \"Add a property named type, with a value equal to the ROS message type\". oq-014 부분 근거",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "FaMe 는 BPMN 과 ROS 2 를 잇는 공개 구현이지만 Open-RMF 작업 상태나 VDA 5050 동작 상태와 BPMN 단계 상태 사이의 표준 매핑으로 볼 근거는 확인하지 못했으므로, oq-014 는 열린 상태로 두는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1423",
        "ref-031",
        "ref-404"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "FaMe 페이지·VDA 5050 3.0.0 명세·rmf_task README 어디에도 서로의 상태를 대응시키는 매핑 절이 없음. oq-014 부분 답변",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "확인한 원문들(CBV.ttl, VDA 5050 3.0.0, IngestorResult.msg)은 로봇 동작 완료와 업무 단계 각각의 정의까지만 제공하며, 로봇 하역 완료를 EPCIS 인계 이벤트로 옮기는 표준 변환은 확인되지 않는다.",
      "tag": "추정",
      "source_ids": [
        "ref-044",
        "ref-031",
        "ref-049"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "oq-001 부분 답변. 세 원문 어디에도 상대 규격을 참조하는 매핑 절이 없다. 공개 구현 사례 검색은 이번 메모 범위에서 하지 않았으므로 '없음'이 아니라 '확인 못 함'",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "VDA 5050 drop 완료를 곧바로 CBV arriving 또는 receiving 으로 단정하지 않고, 업무 측 확인으로 어느 단계인지 정하는 수준까지만 oq-001 의 답을 보강하는 것이 적절하다.",
      "tag": "의견",
      "source_ids": [
        "ref-044",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f1·f2 와 CBV 의 receiving 상호 배타 규정을 근거로 한 판단. oq-001 은 열린 상태 유지",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-044",
      "org": "GS1",
      "title": "gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0)",
      "published": "2021-09-30",
      "url": "https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "GS1 CBV 2.0 온톨로지. arriving·accepting·receiving 등 업무 단계(BizStep)의 정의와 receiving 의 상호 배타 규정을 담는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/gs1/EPCIS/master/Ontology/CBV.ttl",
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "VDA 5050 공식 명세 본문. 이번에는 3.0.0 태그 고정판을 열어 §6.2.2 표 3(blockingType 네 값, SINGLE)과 §6.2.3.2 표 5(drop FINISHED 정의)를 확인했다. 발표일은 근거 미확인.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/3.0.0/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-049",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 하역 워크셀 결과 메시지 정의. 기본 필드는 time·request_guid·source_guid·status(ACKNOWLEDGED·SUCCESS·FAILED)이고 워크셀별 추가 필드 주석이 있다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_internal_msgs/main/rmf_ingestor_msgs/msg/IngestorResult.msg",
      "source_unopened": false
    },
    {
      "id": "ref-502",
      "org": "OMG(Object Management Group)",
      "title": "Business Process Model and Notation (BPMN), Version 2.0.2",
      "published": "2014-01",
      "url": "https://www.omg.org/spec/BPMN/2.0.2/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "BPMN 2.0.2 규범 문서(formal/2013-12-09). 수신 작업(§10.3.3, 인쇄 p.159)·상관 키(§8.4.2)·타이머 등 중간 이벤트(§10.5.4)·보상(§10.7)을 정의한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.omg.org/spec/BPMN/2.0.2/PDF",
      "source_unopened": false
    },
    {
      "id": "ref-1423",
      "org": "University of Camerino PROS Lab",
      "title": "FaMe — A BPMN-driven Framework for Multi-Robot System Development (공식 페이지·사용 지침)",
      "published": "2022-05-03",
      "url": "https://pros.unicam.it/fame/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "FaMe 연구팀의 공식 페이지. 지상 로봇 협업·농업 시뮬레이션 재현 절차, BPMN 모델링 지침 G1~G7, 구성 절차(신호 이벤트와 ROS 메시지 형 연결)를 제시한다. 기존 ref-503(GitHub README)·ref-114(논문)와 같은 연구팀 자료다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-366",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_task — rmf_task/include/rmf_task/Task.hpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 작업 인터페이스 헤더. Task::Active 의 cancel()·kill()·skip() 의 의미(취소 후 정리 단계, 완료 콜백으로 취소 종료)를 주석으로 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_task/main/rmf_task/include/rmf_task/Task.hpp",
      "source_unopened": false
    },
    {
      "id": "ref-404",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_task — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_task",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_task 저장소 README. rmf_task_sequence 의 단계·이벤트 구조와 기본 이벤트 7종(Bundle·DropOff·GoToPlace·PerformAction·PickUp·Placeholder·WaitFor), 모델과 실행 구현의 위치를 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_task/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-116",
      "org": "Filippone, G., Pettinari, S., & Pelliccione, P.",
      "title": "Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis",
      "published": "2026-03-16",
      "url": "https://arxiv.org/abs/2603.15427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "행동 트리·상태 기계·HTN·BPMN 을 제어 구조·표현력·도구 지원으로 비교하고 전문가 설문(83명 요청, 29개 응답)과 후속 인터뷰로 검증한 연구. v1 2026-03-16, v2 2026-08-17, Journal ref IEEE Transactions on Software Engineering (2026). 이번에 v2 본문을 열람했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2603.15427v2",
      "source_unopened": false
    },
    {
      "id": "ref-1424",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 (tag 2.14.0) — rmf_fleet_adapter/CHANGELOG.rst",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 패키지 변경 이력. 2.14.0(2026-09-26) 절에 단계 건너뛰기 요청 키 수정(#543) 항목이 있다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "source_unopened": false
    },
    {
      "id": "ref-1425",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 (tag 2.1.0) — VDA5050_EN.md",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/2.1.0/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "VDA 5050 2.1.0 명세 본문. blockingType 을 NONE·SOFT·HARD 세 값으로 정의해 3.0.0 의 SINGLE 추가를 대조하는 근거가 된다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/2.1.0/VDA5050_EN.md",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/planning-and-optimization/task-and-workflow-modeling.md",
      "sections": [
        "3",
        "5",
        "6",
        "7",
        "8",
        "11"
      ],
      "rationale": "갱신(차등, 외부 조사 메모 변환): 섹션 3 — 첫 문단의 근거를 원문 정의로 구체화: CBV 세 단계(f1), drop FINISHED 표 5(f2), IngestorResult 기본 필드 범위(f3), 별도 완료 조건 권고(f4, 의견) / 섹션 5 — 창고 밖 사례로 FaMe 농업·지상 로봇 협업 시뮬레이션(f7·f8, site_type 기타)과 분류 한계(f9) 추가 / 섹션 6(주제 페이지 2026-09-25-area02-s6 요약) — BPMN 규범 근거로 수신 작업·상관 키·타이머(f5·f6, 기존 Camunda 문장 보완), 취소 후 정리·보상(f10~f12), rmf_task_sequence 단계·이벤트 7종(f13~f15) / 섹션 7(주제 페이지 2026-09-25-area02-s7 요약) — VDA 5050 3.0.0 blockingType SINGLE(f16·f17, 발표일 언급 없음)과 SINGLE·HARD 구별 권고(f18, 의견), rmf_fleet_adapter 2.14.0 단계 건너뛰기 키 수정(f19·f20); 표의 BPMN 행을 2.0.2 규범판(ref-502)으로 보강 / 섹션 8(주제 페이지 2026-09-25-area02-s8 요약) — Filippone 외(ref-116) 항목을 v2·게재처·연구 방법으로 보강(f21~f23); FaMe 항목(ref-114)은 기존 내용 확인 / 섹션 11(주제 페이지 2026-09-25-area02-s11) — oq-014 부분 근거(f24·f25), oq-001 부분 근거(f26·f27), 새 질문 3건. 섹션 4·9·10 은 바꾸지 않는다. 다음 실행 후보: 32. 예외 복구·재계획·업무 연속성(f10~f12), 20. 로봇·제조사 관제 연동(f16~f18), 17. 작업 대상·자산 식별과 인계 추적(f1~f4)."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "수신 작업",
      "term_en": "Receive Task (BPMN)",
      "definition": "외부 참여자가 보낸 메시지가 도착할 때까지 기다리다가 메시지를 받으면 완료되는 BPMN 작업 유형이다."
    },
    {
      "term_ko": "보상",
      "term_en": "Compensation (BPMN)",
      "definition": "이미 성공적으로 끝난 단계의 결과가 더는 필요 없을 때 그 효과를 되돌리는 처리를 별도 활동으로 표현하는 BPMN 개념이다."
    }
  ],
  "open_questions_new": [
    "로봇이 이미 하역한 뒤 작업이 취소되면, 로봇 쪽 정리 단계 완료와 업무상 인수 취소(재고 반영 취소)를 어떤 완료 조건으로 나눠야 하는가? | 관련 영역: 24. 작업·워크플로 모델링, 32. 예외 복구·재계획·업무 연속성 | 근거: f10 | 종류: 일반",
    "Open-RMF rmf_task_sequence 의 Bundle 이벤트와 BPMN 병렬 게이트웨이 합류의 의미 차이를 자동으로 검사하거나 변환하는 공개 도구가 있는가? | 관련 영역: 24. 작업·워크플로 모델링, 54. 시험·형식 검증·벤치마크 | 근거: f15 | 종류: 일반",
    "운영 정책 버전이 바뀔 때 이미 시작한 워크플로 인스턴스가 이전 정책을 유지하는지 새 정책으로 옮기는지에 대한 공개 운영 기준이 있는가? | 관련 영역: 24. 작업·워크플로 모델링, 57. 자산·소프트웨어 수명주기 관리 | 근거: f20 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 10,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-01/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.",
      "VDA 5050 3.0.0 의 발표일(메모의 2026-03-19)은 근거를 확인하지 못해 적지 않았고(ref-031 published null), 릴리스 노트 페이지(메모 n10)는 원문 확인이 안 돼 출처에서 뺐다",
      "f19: 'Fix phase key for skip requests (#543)' 에서 고친 키의 실제 이름은 변경 이력만으로 확인하지 않았다(#543 본문 미열람)",
      "f15: rmf_task_sequence Bundle 이벤트의 병렬·합류 의미는 API 문서를 열지 않아 미확인",
      "f7~f9: FaMe 시뮬레이션 시나리오가 실외 현장인지, 실물 로봇 실험의 규모는 공식 페이지에서 확인하지 못했다(site_type 기타)",
      "f26: 로봇 하역 완료를 EPCIS 이벤트로 옮기는 공개 구현 사례는 이번 메모 범위에서 검색하지 않았다(확인 못 함)",
      "ref-1425(VDA 5050 2.1.0) 발행일 미확인"
    ],
    "scope_violations": [
      "f16~f18: VDA 5050 blockingType 은 로봇·제조사 관제 인터페이스(20. 로봇·제조사 관제 연동) 쪽 정의이므로 이 영역에서는 공정 모델의 병행 제약 근거로만 쓴다",
      "f10~f12: 취소·보상 처리 절차는 32. 예외 복구·재계획·업무 연속성과 겹치며, 이 영역에서는 워크플로의 상태·완료 조건 구분으로 한정한다",
      "f1~f4: 재고 확정(CBV receiving)은 상위 업무 시스템(WMS) 연계 대상이며 ROP 는 완료 조건 구분과 대기만 맡는다"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 3
    },
    "limits": "외부 조사 변환이라 검색·열람 집계 없음(queries 0 은 실제 검색 수가 아니다). web_fetch_available: true. 신규 출처 3건(ref-1423~ref-1425, 예약 구간 ref-1423~ref-1452 안), 기존 id 재사용 7건(ref-044·ref-031·ref-049·ref-502·ref-366·ref-404·ref-116). 메모의 출처 10개 중 n10(VDA 5050 3.0.0 릴리스 노트)은 원문 미확인으로 제외하고, SINGLE 추가의 대조 근거로 VDA 5050 2.1.0 명세(ref-1425)를 더했다. 메모의 n2(3.0.0 태그 명세)는 main 판 ref-031 과 같은 문서로 보아 ref-031 에 3.0.0 태그 raw 경로를 fetch_url 로 적었고, n4(BPMN 2.0.2 PDF)는 ref-502 와 같은 문서다. 검증 수정 반영: SINGLE 정의는 사실(f16)·'구별해야 한다'는 의견(f18)으로 분리, 발표일 삭제, IngestorResult 범위를 기본 정의 필드로 한정(f3), rmf_task_sequence 이벤트 7개(Placeholder 포함, f14), 변경 이력 키 이름 단정 안 함(f19), Filippone 외 v1·v2 날짜와 IEEE TSE 게재 정보 추가(f21), drop FINISHED 근거 위치 §6.2.3.2 표 5(f2), BPMN 2.0.2 서지(formal/2013-12-09, 2014-01)와 절 위치(f5·f11), FaMe 공식 페이지는 ref-503·ref-114 와 같은 연구팀 자료라 독립 교차 확인으로 세지 않음(f8). 교차 확인 0건이며 사실 finding 은 단일 출처라 신뢰도 medium 이하. 현장 유형 사례 finding 은 FaMe 농업·지상 로봇 협업 시뮬레이션(f7~f9, 기타)뿐이다. 열린 질문 해결 제안 없음: oq-001(f26·f27)·oq-014(f24·f25) 부분 근거만 냈다. oq-012·oq-013 근거 없음. 국내 자료 없음."
  }
}
```

### runs/2026-10-10-01/verification.json

```json
{
  "run_id": "2026-10-10-01",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문(data/source_texts/ref-044)과 raw CBV.ttl 재열람에서 arriving·accepting·receiving 의 rdfs:comment 와 receiving 상호 배타 문장 일치. dct:modified 2021-09-30, versionInfo 2.0. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: VDA 5050 3.0.0 태그 명세 §6.2.3.2 Action states 표 5의 drop 행 FINISHED 문구 일치. 발표일 미확인 유지."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: IngestorResult.msg 원문의 기본 필드(time·request_guid·source_guid·status ACKNOWLEDGED/SUCCESS/FAILED)와 끝의 custom workcell 필드 주석 일치. 범위를 기본 정의 필드로 한정한 표현이 적절하다. 발행일 미확인."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f1~f3 정의 대조에서 나온 이 위키의 판단이다. 누구의 의견인지('이 위키의 판단') 밝혀야 한다. 기존 3절 첫 문단 [추정] 문장('arriving 수준')과 5절 시나리오 1의 'arriving에 가깝다' 문장의 근거 범위를 좁히는 내용이라 해당 문장 수정이 필요하다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(일부 간접): OMG 사양 페이지에서 BPMN 2.0.2, formal/13-12-09, 2014년 1월 발행을 확인했다. 검증자 WebFetch 로는 PDF 본문 텍스트를 추출하지 못했고, 수신 작업 정의 문장은 BPMN 2.0.2 §10.3.3 을 인용한 2차 자료(Flowable 문서) 검색 결과로 대조했다. CorrelationKey(§8.4.2)·Timer(§10.5.4)의 절 번호는 검증자가 원문으로 확인하지 못했다. 리서치는 fetched true 로 기록했다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: FaMe 모델링 지침 G4·G5 와 구성 절(신호 이벤트 type 속성에 ROS 메시지 형)은 공식 페이지에서 확인했다. Camunda 고유 동작을 표준 보장으로 넓히지 않는 한정과 '로봇 인수 확인 적용 사례 미확인'을 본문에 남겨야 한다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: FaMe 공식 페이지 'Reproducing the simulation'에 ground vehicle cooperation·agriculture scenario 패키지, 엔진 패키지, colcon build·launch·splitter 절차가 있다. 요구사항 Ubuntu 20.04+, ROS2 Foxy+, Gazebo(실제 로봇에는 불필요), NodeJS. 게시일 2022-05-03. 브리프 출처 항목의 fetch_url 이 null 이다(R-1, 아래 노트 참조)."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: G1 Robots as pools, G2 Mission as a process, G2.1 Actions as activities, G2.3 AND gateways, G2.4 XOR gateways, G4 error events, G5 timer events 의 제목이 페이지와 같다. 같은 연구팀 자료(ref-503·ref-114)라 독립 교차 확인이 아니라는 브리프 판단도 맞다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: 시뮬레이션 재현 절차만 공개돼 있다는 점과 맞는다. '이 위키의 판단'임을 밝히고 현장 성능 근거로 쓰지 않는다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Task.hpp 원문(입력 source_texts)의 cancel() 주석(취소 뒤 일부 단계 계속, pending_phases 가 로봇을 짐 없는 상태로 되돌리는 단계로 바뀔 수 있음, finished 콜백으로 취소 종료), kill() 이 cancel() 에 우선함이 일치. 발행일 미확인."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(일부 간접): 보상 정의 문장은 검증자가 PDF 텍스트로 대조하지 못했다. BPMN 보상 개념을 같은 취지로 옮긴 2차 자료(Camunda·No Magic 문서) 검색 결과와는 일치한다. §10.7 절 번호는 검증자가 확인하지 못했다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f10·f11 과 rmf_task README('단계마다 취소·중단 시 반응을 지정할 수 있다')로 뒷받침된다. 두 체계가 같은 상태 체계라는 뜻이 아니라는 한정을 유지하고 '이 위키의 판단'임을 밝힌다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: rmf_task README 원문에 단계의 순서 실행, 단계의 이벤트 구성, 모델 구현은 rmf_task_sequence·Active 구현은 rmf_fleet_adapter, fleet adapter 는 현재 rmf_task_sequence 단계 연쇄 작업만 지원한다는 문장이 있다. 발행일 미확인."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README 이벤트 목록이 Bundle·DropOff·GoToPlace·PerformAction·PickUp·Placeholder·WaitFor 일곱 가지로 일치한다('presently available' — 현재 기준)."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지(low): Bundle 의 병렬·합류 의미는 원문 미확인이므로 본문에 '미확인'을 남긴다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 3.0.0 태그 명세 §6.2.2 'four distinct blocking types'·표 3(병렬 실행·자동 주행 허용 여부)과 §7.3 action 표 blockingType 설명(SINGLE: allows driving but no other actions; HARD: is the only allowed action at that time) 일치."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 2.1.0 태그 명세 blockingType Enum {'NONE','SOFT','HARD'}와 'three distinct blocking types' 일치, SINGLE 없음. 같은 발행 계열 두 판의 대조이므로 독립 교차 확인이 아니다. 2.1.0 과 3.0.0 사이 다른 판을 확인하지 않았으므로 '3.0.0 에서 추가'가 아니라 '2.1.0 명세에는 없고 3.0.0 명세에는 있다'로 적어야 한다(수정 지시)."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f16 정의에서 끌어낸 이 위키의 모델링 권고다. 출처를 밝힌다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: rmf_ros2 2.14.0 태그 rmf_fleet_adapter/CHANGELOG.rst 첫 절 '2.14.0 (2026-09-26)'에 'Fix phase key for skip requests (#543)' 항목 있음. 고친 키 이름은 미확인, 개별 패키지 버전이라는 한정 유지."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지(low): f19 와 Task.hpp skip(phase_id, value)(운영자 수동 개입용) 근거의 운영 권고다. '이 위키의 판단'임을 밝힌다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv abs 페이지에서 제목·저자, v1 2026-03-16·v2 2026-08-17, Journal ref IEEE Transactions on Software Engineering (2026), 네 형식(BT·SM·HTN·BPMN)을 제어 구조·표현력·도구 지원으로 비교한다는 초록을 확인했다. 기존 페이지 각주 ref-116(2026-03, 원문 미열람)은 고쳐야 한다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: v2 HTML §III-C 에서 '2026년 1월 4주', '83 invitations 중 29 complete responses, 34.94%', 실시간 인터뷰 3명·서면 응답 1명을 확인했다. 로봇 처리량 측정 서술은 없다. 같은 논문이라 독립 교차 확인이 아니다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: 연구 방법(분석 비교 + 전문가 검증)으로 뒷받침된다. §VII 이 Threats to Validity 임은 확인했으나 그 내용은 검증자가 읽지 않았다. '이 위키의 판단'임을 밝힌다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: FaMe 페이지의 BPMN 협업으로 MRS 임무 정의·ROS2 실행, modeling·configuration·enactment 세 단계, 각 로봇에서 협업 직접 실행, 신호 이벤트 type 속성에 ROS 메시지 형(예 std_msgs/msg/Bool) 지정 일치. oq-014 부분 근거로만 쓴다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: 세 원문에 상호 상태 매핑 절이 없다는 판단이며 oq-014 는 열린 상태로 둔다. '이 위키의 판단'임을 밝힌다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 공개 구현 사례는 검색하지 않았으므로 '없음'이 아니라 '확인 못 함'으로 쓴다. oq-001 해결로 바꾸지 않는다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f1·f2 와 receiving 상호 배타 규정에 근거한다. 기존 5절 시나리오 1 문장('이 시점은 CBV로 보면 arriving에 가깝다')과 어긋나지 않도록 그 문장을 고쳐야 한다(수정 지시)."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": []
  },
  "duplication": {
    "ok": false,
    "overlaps": [
      "f4·f27 이 기존 3절 첫 문단 [추정] 문장('완료 신호는 GS1 CBV의 arriving 수준의 물리적 인도만 나타내고', ref-031·ref-049·ref-044)과 5절 시나리오 1 문장('이 시점은 CBV로 보면 arriving에 가깝다')의 근거 범위를 좁힌다 — 기존 문장 수정 대상",
      "f5·f6 이 6절 분리 주제 페이지의 기존 BPMN 메시지 대기 근거(ref-112 원문 미열람, ref-113 Camunda 벤더 문서)와 같은 주장을 다룬다 — 기존 각주는 유지하고 ref-502 를 더한다",
      "f7·f8·f24(ref-1423 FaMe 공식 페이지)는 기존 ref-503(FaMe GitHub README)·ref-114(Corradini 외 논문)와 같은 연구팀 자료다 — 독립 교차 확인으로 세지 않는다",
      "f21~f23 은 기존 8절 분리 주제 페이지의 ref-116 항목(2026-03, 원문 미열람)을 보강한다 — 같은 ref-116 을 재사용한다",
      "트랙 반영 제안(실행 2026-09-25-51)의 FaMe(f10)·임무 기술 형식 비교 연구(f16) 항목이 이번 f24·f21~f23 과 겹친다",
      "ref-1423·ref-1424·ref-1425 는 실행 2026-10-09-26 브리프가 다른 출처(CubiCasa5k house.py, 공공데이터포털 고양시 페이지, IFC IfcBuildingElementProxy)에 준 id 와 같다 — 그 실행이 게시됐으면 참고문헌 id 충돌"
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "용어 후보 '보상 (Compensation (BPMN))'이 기존 용어 compensating-transaction '보상 트랜잭션 (Compensating Transaction)'과 한글 표기가 겹친다 — 같은 개념이 아니므로 구분되는 표기로 등록하고 서로 연결해야 한다"
    ]
  },
  "quotation_check": {
    "ok": true,
    "issues": [
      "evidence_excerpt 에 같은 출처의 원문 구절이 여러 개 들어 있다(ref-044 는 f1 에 세 구절, ref-031 은 f2·f16 에, ref-502 는 f5·f11 에). 페이지 본문에서는 출처당 직접 인용 1회 이하로 제한하고 나머지는 재서술해야 한다"
    ]
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "3절 첫 문단: 기존 [추정] 문장('…GS1 CBV의 arriving 수준의 물리적 인도만 나타내고…')을 고친다. 하역 완료 신호를 특정 CBV 단계와 같다고 보는 표현을 빼고, f1 [사실][^ref-044](arriving·accepting·receiving 정의와 receiving 의 상호 배타), f2 [사실][^ref-031](3.0.0 §6.2.3.2 표 5 drop FINISHED), f3 [사실][^ref-049](기본 정의 필드 한정)로 나눠 적는다. 그 뒤에 f4 를 [의견](이 위키의 판단)으로 덧붙이고 '이 구성을 적용한 표준·사례는 확인하지 못했다' 한정을 유지한다 — f4 가 기존 문장의 근거 범위를 좁힌다.",
    "5절 시나리오 1: '이 시점은 CBV로 보면 arriving에 가깝다' 문장을 f27 [의견]과 맞게 바꾼다. 로봇 drop 완료를 곧바로 arriving 이나 receiving 으로 단정하지 않고, 어느 업무 단계인지는 업무 측 확인으로 정한다고 쓴다 — 기존 [추정]과 f27 의 판단이 어긋난다.",
    "5절: 창고 밖 사례를 새 소절로 추가한다. 현장 유형 '기타'(농업·지상 로봇 협업 시뮬레이션, 67. 기타 현장)를 밝히고 f7·f8 을 여섯 항목에 놓는다. 근거가 없는 항목(시작 조건·제약·완료·인계·예외·성과 등)은 '미확인'으로 두고, f9 는 [의견](이 위키의 판단)으로 '시뮬레이션 재현 자료이며 현장 운영 성능 근거가 아니다'를 적는다. site_matrix_updates 의 site_type 은 '기타'로 한다.",
    "f17: '3.0.0 에서 추가된 값'을 '2.1.0 명세에는 없고 3.0.0 명세에는 있다'로 고친다 — 두 판 사이 다른 판을 확인하지 않았다. 같은 발행 계열 두 판의 대조이므로 교차 확인으로 표시하지 않는다.",
    "f4·f9·f12·f18·f20·f23·f25·f27 의 [의견] 문장마다 '이 위키의 판단'임을 밝힌다 — 공통 규칙 5항은 의견의 주체를 밝히게 한다.",
    "8절 분리 주제 페이지와 13절 각주의 ref-116: 발행일을 2026-03-16 으로, 접근일을 2026-10-10 으로 고치고 '(원문 미열람)'을 뺀다(이번에 v2 본문 열람 확인). 본문에는 v2(2026-08-17)·IEEE Transactions on Software Engineering (2026) 게재 정보와 f22 의 연구 방법(설문 83명 요청·29개 응답, 인터뷰 3명·서면 1명, 로봇 처리량 측정 아님)을 적는다.",
    "ref-031 을 인용하는 새 문장(f2·f16): 3.0.0 태그판 기준임을 본문에 밝히고(main 브랜치 판과 다를 수 있음) 발표일은 쓰지 않는다. 각주 접근일은 2026-10-10 으로 고친다.",
    "f19·f20: '개별 패키지 rmf_fleet_adapter 2.14.0(2026-09-26)'으로 적고 Open-RMF 배포판 버전으로 쓰지 않는다. 고친 키의 이름은 '미확인'으로 둔다.",
    "f15·f26: 각각 'Bundle 의 병렬·합류 의미 원문 미확인', '공개 구현 사례는 검색하지 않아 확인 못 함' 한정을 본문에 남긴다. '없다'로 단정하지 않는다.",
    "범위 경계: f1~f4·f26·f27 에서 수령자 재고 편입(CBV receiving)과 EPCIS 이벤트 생성·재고 확정은 '연계 대상: 상위 업무 시스템(WMS 등)'으로 표시한다. ROP 몫은 완료 조건 구분과 대기·분기로 한정한다(분류 원문 19장 상위 업무 시스템 경계).",
    "연결: f16~f18 은 20. 로봇·제조사 관제 연동, f10~f12 는 32. 예외 복구·재계획·업무 연속성, f1~f4 는 17. 작업 대상·자산 식별과 인계 추적과 연결한다. 이 영역 본문에서는 공정 모델의 병행 제약과 완료·취소 상태 구분으로만 쓴다 — 세부영역 번호와 이름을 함께 적는다.",
    "6절 분리 주제 페이지(2026-09-25-area02-s6): 기존 Camunda 문장(ref-113)과 ref-112 각주는 지우지 않는다. BPMN 2.0.2 규범 근거 f5(ref-502)·f6 을 더하고, Camunda 고유의 TTL·중복 거부 동작을 BPMN 표준의 보장으로 넓히지 않는다.",
    "7절 분리 주제 페이지(2026-09-25-area02-s7): 표의 BPMN 행에 ref-502(OMG, BPMN 2.0.2, formal/13-12-09, 2014-01)를 더한다. VDA 5050 blockingType(f16·f17)과 rmf_fleet_adapter 2.14.0(f19)을 기준일과 함께 적는다.",
    "트랙 반영 제안 2건: 이번 브리프 finding 으로 뒷받침되는 FaMe(f7·f8·f24)와 임무 기술 형식 비교 연구(f21~f23)만 반영한다. 나머지 항목(OPC UA for ISA-95 작업 응답, BPMN 2.0.2 사람 수행자·자원 배정, Serverless Workflow DSL, Isaac Mission Dispatch, PlanSys2, DART-LLM, LTLf→행동 트리, Open-RMF 워크플로 다이어그램, crossflow)은 이번 실행에서 검증하지 않았으므로 본문에 넣지 않고 '제안' 상태로 남긴다.",
    "11절 분리 주제 페이지(2026-09-25-area02-s11)와 open_question_updates: oq-001(f26·f27)·oq-014(f24·f25)는 '열림'을 유지하고 부분 근거만 단다. open_questions_new 3건은 관련 영역(24. 작업·워크플로 모델링, 32. 예외 복구·재계획·업무 연속성 / 54. 시험·형식 검증·벤치마크 / 57. 자산·소프트웨어 수명주기 관리)을 번호와 이름으로 옮겨 등록한다.",
    "glossary_updates: '수신 작업 (Receive Task (BPMN))'은 신규 등록한다. '보상' 후보는 기존 '보상 트랜잭션 (Compensating Transaction)'과 구분되도록 'BPMN 보상 (Compensation (BPMN))'처럼 표기하고, 정의에 보상 트랜잭션과의 관계를 연결로 적는다.",
    "인용: 페이지 본문의 직접 인용은 출처당 1회 이하로 한다(ref-044·ref-031·ref-502 는 여러 구절이 브리프에 있음). 나머지는 재서술한다.",
    "reference_updates 의 ref-1423·ref-1424·ref-1425: 브리프 id 를 그대로 쓴다. 다만 이 셋은 실행 2026-10-09-26 브리프가 다른 출처에 준 id 와 같으므로, changelog_entry 비고에 'id 충돌 여부 퍼블리셔 확인 필요'를 남긴다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 27건, 미확인 0건, 교차 확인 0건. 강등: 없음(f17 은 표현 정정 지시). 원문 미열람 출처: 없음. 다만 BPMN 2.0.2 PDF(ref-502)는 검증자 도구로 본문 텍스트를 추출하지 못했다. OMG 사양 페이지(formal/13-12-09, 2014-01)와 §10.3.3 을 인용한 2차 자료로 대조했고, f5·f11 의 절 번호는 검증자가 원문으로 확인하지 못했다. 브리프 ref-1423 은 fetched true 인데 fetch_url 이 null 이다(검증자가 https://pros.unicam.it/fame/ 를 열어 확인). 주의: 사실 주장은 모두 단일 출처(표준·오픈소스 원문)다. 이번 리서치는 외부 조사 메모를 변환한 것이라 검색 0회이고 한국어 검색과 국내 자료가 없다(공통 규칙 8 미충족, 다음 갱신에서 보강 필요). 창고 밖 사례는 FaMe 농업·지상 로봇 협업 시뮬레이션(현장 유형 기타) 하나뿐이며 현장 운영 성능 근거가 아니다. oq-001·oq-014 는 부분 근거만 있어 열림을 유지한다(해결 인정 없음). 트랙 반영 제안 2건 가운데 FaMe·임무 기술 형식 비교 연구만 반영하고, 나머지는 검증되지 않아 제안으로 남긴다. ref-1423~ref-1425 는 실행 2026-10-09-26 브리프의 다른 출처 id 와 겹쳐 퍼블리셔 확인이 필요하다. 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-10-10-01/pages.json

```json
{
  "run_id": "2026-10-10-01",
  "outline": [
    {
      "path": "docs/categories/planning-and-optimization/task-and-workflow-modeling.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 1400,
      "summary": "로봇 관제 규격의 하역 완료와 업무 어휘의 인수·재고 반영은 서로 다른 원문이 각각 정의한다(2026-10-10 확인). [사실][^ref-044][^ref-031][^ref-049] 하역 완료를 특정 CBV 단계와 자동으로 같다고 보지 않고 인수·재고 확정을 별도 완료 조건으로 두는 것이 이 위키의 판단이다. [의견][^ref-044][^ref-031][^ref-049]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-and-workflow-modeling.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 3300,
      "summary": "물류창고 가상 시나리오 2건(입고 → 적치, 출하)은 유지하되 drop 완료를 CBV 단계로 단정하지 않도록 고치고, 현장 유형 기타(농업·지상 로봇 협업 시뮬레이션, FaMe) 사례를 더한다. [사실][^ref-1423]",
      "planned_findings": [
        "f3",
        "f7",
        "f8",
        "f9",
        "f24",
        "f27"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-and-workflow-modeling.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1600,
      "summary": "BPMN 2.0.2 규범 문서는 수신 작업·상관 키·타이머 이벤트와 보상을 정의한다. [사실][^ref-502] Open-RMF rmf_task_sequence 작업은 단계의 연쇄이고 단계는 이벤트로 구성된다. [사실][^ref-404]",
      "planned_findings": [
        "f5",
        "f6",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f15"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-and-workflow-modeling.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1400,
      "summary": "VDA 5050 3.0.0 태그판은 blockingType 을 NONE·SINGLE·SOFT·HARD 네 값으로 둔다. [사실][^ref-031] 개별 패키지 rmf_fleet_adapter 2.14.0(2026-09-26)에 단계 건너뛰기 요청 키 수정이 있다. [사실][^ref-1424]",
      "planned_findings": [
        "f16",
        "f17",
        "f18",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-and-workflow-modeling.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 900,
      "summary": "Filippone 외 비교 연구(v2 2026-08-17, IEEE TSE 2026)는 네 임무 기술 형식을 분석 비교하고 전문가 설문으로 검증했다. [사실][^ref-116] FaMe 는 BPMN 협업을 ROS 2 위에서 직접 실행한다. [사실][^ref-1423]",
      "planned_findings": [
        "f21",
        "f22",
        "f23",
        "f24"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-and-workflow-modeling.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 450,
      "summary": "32. 예외 복구·재계획·업무 연속성과 67. 기타 현장을 연결에 더하고 17·20번 연결 근거를 짚는다.",
      "planned_findings": [
        "f10",
        "f12",
        "f7",
        "f16"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-and-workflow-modeling.md",
      "section": "11. 열린 질문",
      "budget_chars": 1100,
      "summary": "oq-001·oq-014 는 부분 근거만 더하고 열림을 유지한다. [추정][^ref-044][^ref-031][^ref-049] 새 질문 3건을 올린다.",
      "planned_findings": [
        "f24",
        "f25",
        "f26",
        "f27"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/planning-and-optimization/task-and-workflow-modeling.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "3절 첫 문단을 원문 정의(CBV 세 단계·VDA 5050 3.0.0 drop FINISHED·IngestorResult 기본 필드)와 [의견]으로 나눠 다시 씀, 5절 시나리오 1 문장 수정·IngestorResult 범위 한정과 사례 3(현장 유형 기타, FaMe, 작업 대상 미확인) 추가, 6·7·8·11절 보강(각 보강 소절 첫 줄에 2026-09-25 분리 주제 페이지 링크 유지)과 10절 연결 덧붙임, 13절 각주 갱신(ref-031·ref-044·ref-049 접근일, ref-116 발행일·접근일·열람)과 새 각주 1건(ref-1423). ref-366·ref-404·ref-502·ref-1424·ref-1425 는 자동 분리 뒤 분리 주제 페이지의 출처 절에만 남는다",
      "patches": [
        {
          "section": "3. 왜 중요한가",
          "action": "replace",
          "frontmatter": {
            "related_areas": [
              17,
              20,
              23,
              26,
              29,
              32,
              38,
              39,
              54,
              67
            ],
            "sources": [
              "ref-023",
              "ref-031",
              "ref-044",
              "ref-049",
              "ref-110",
              "ref-111",
              "ref-112",
              "ref-113",
              "ref-116",
              "ref-117",
              "ref-118",
              "ref-119",
              "ref-121",
              "ref-123",
              "ref-124",
              "ref-366",
              "ref-404",
              "ref-502",
              "ref-1423",
              "ref-1424",
              "ref-1425"
            ],
            "last_run": "2026-10-10"
          },
          "content": "(절 본문 생략 — runs/2026-10-10-01/pages/categories/planning-and-optimization/task-and-workflow-modeling.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-01/pages/categories/planning-and-optimization/task-and-workflow-modeling.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-01/pages/categories/planning-and-optimization/task-and-workflow-modeling.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-01/pages/categories/planning-and-optimization/task-and-workflow-modeling.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-01/pages/categories/planning-and-optimization/task-and-workflow-modeling.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-01/pages/categories/planning-and-optimization/task-and-workflow-modeling.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-01/pages/categories/planning-and-optimization/task-and-workflow-modeling.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-01/pages/categories/planning-and-optimization/task-and-workflow-modeling.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-10-area24-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 24. 작업·워크플로 모델링 의 \"11. 열린 질문\" 절(1,498자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area24-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 24. 작업·워크플로 모델링 의 \"6. 대표 접근법과 기술\" 절(1,442자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area24-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 24. 작업·워크플로 모델링 의 \"3. 왜 중요한가\" 절(1,339자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area24-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 24. 작업·워크플로 모델링 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,291자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area24-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 24. 작업·워크플로 모델링 의 \"8. 대표 연구와 자료\" 절(886자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-10 | 24. 작업·워크플로 모델링 | 3절 하역 완료와 인수·재고 반영을 원문 정의별로 분리, 5절 시나리오 1 문장 수정과 사례 3(현장 유형 기타) 추가, 6·7·8·10·11절 보강(BPMN 2.0.2·취소 후 정리·rmf_task_sequence·VDA 5050 blockingType·rmf_fleet_adapter 2.14.0·Filippone 외 v2·FaMe, 2026-09-25 분리 주제 페이지 링크 유지), 13절 각주 갱신. 비고: ref-1423~ref-1425 는 실행 2026-10-09-26 브리프의 다른 출처 id 와 같아 id 충돌 여부 퍼블리셔 확인 필요 | run 2026-10-10-01",
  "index_updates": {
    "home_recent": "2026-10-10 — 24. 작업·워크플로 모델링: 로봇 하역 완료와 업무상 인수·재고 반영의 원문 정의를 나누고, 기타 현장(농업·지상 로봇 협업 시뮬레이션) 사례와 BPMN 2.0.2·rmf_task_sequence·VDA 5050 3.0.0 blockingType 근거를 보강",
    "category_recent": "2026-10-10 — 24. 작업·워크플로 모델링: 3절 완료 신호 정의 분리, 5절 기타 현장 사례 추가, 6·7·8·10·11절 보강과 각주 갱신",
    "area_recent": "2026-10-10 — 24. 작업·워크플로 모델링: 3절 첫 문단을 CBV·VDA 5050 3.0.0·IngestorResult 원문 정의와 [의견]으로 다시 쓰고, 5절 사례 3(현장 유형 기타, FaMe)과 6·7·8·10·11절 보강을 더함(2026-09-25 분리 주제 페이지 링크 유지)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "receive-task-bpmn",
      "term_ko": "수신 작업",
      "term_en": "Receive Task (BPMN)",
      "definition": "외부 참여자가 보낸 메시지가 도착할 때까지 기다리다가 메시지를 받으면 완료되는 BPMN 작업 유형이다.",
      "description": "BPMN 2.0.2 규범 문서가 정의한다. 메시지를 프로세스 인스턴스에 연결하는 상관 키(CorrelationKey), 시간 조건을 표현하는 타이머 이벤트와 함께 쓰면 운반 뒤 인수 확인을 기다리고 시간 초과 시 분기하는 구조를 표현할 수 있다.",
      "related_areas": [
        24
      ],
      "sources": [
        "ref-502"
      ]
    },
    {
      "action": "new",
      "slug": "bpmn-compensation",
      "term_ko": "BPMN 보상",
      "term_en": "Compensation (BPMN)",
      "definition": "이미 성공적으로 끝난 단계의 결과가 더는 필요 없을 때 그 효과를 되돌리는 처리를 별도 활동으로 표현하는 BPMN 개념이다.",
      "description": "BPMN 2.0.2 규범 문서가 정의하는 프로세스 모델 요소다. 한글 표기가 비슷한 용어집 항목 '보상 트랜잭션 (Compensating Transaction)'(compensating-transaction)과 같은 개념이 아니므로 구분해 쓰고, 두 항목을 서로 연결해 참고한다.",
      "related_areas": [
        24,
        32
      ],
      "sources": [
        "ref-502"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-044",
      "org": "GS1",
      "title": "gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0)",
      "published": "2021-09-30",
      "url": "https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "GS1 CBV 2.0 온톨로지. arriving·accepting·receiving 등 업무 단계(BizStep)의 정의와 receiving 의 상호 배타 규정을 담는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-and-workflow-modeling.md"
      ]
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "VDA 5050 공식 명세 본문. 이번에는 3.0.0 태그 고정판을 열어 §6.2.2 표 3(blockingType 네 값, SINGLE)과 §6.2.3.2 표 5(drop FINISHED 정의)를 확인했다. 발표일은 근거 미확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-and-workflow-modeling.md"
      ]
    },
    {
      "id": "ref-049",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 하역 워크셀 결과 메시지 정의. 기본 필드는 time·request_guid·source_guid·status(ACKNOWLEDGED·SUCCESS·FAILED)이고 워크셀별 추가 필드 주석이 있다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-and-workflow-modeling.md"
      ]
    },
    {
      "id": "ref-502",
      "org": "OMG(Object Management Group)",
      "title": "Business Process Model and Notation (BPMN), Version 2.0.2",
      "published": "2014-01",
      "url": "https://www.omg.org/spec/BPMN/2.0.2/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "BPMN 2.0.2 규범 문서(formal/2013-12-09). 수신 작업·상관 키·타이머 등 중간 이벤트·보상을 정의한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-and-workflow-modeling.md"
      ]
    },
    {
      "id": "ref-1423",
      "org": "University of Camerino PROS Lab",
      "title": "FaMe — A BPMN-driven Framework for Multi-Robot System Development (공식 페이지·사용 지침)",
      "published": "2022-05-03",
      "url": "https://pros.unicam.it/fame/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "FaMe 연구팀의 공식 페이지. 지상 로봇 협업·농업 시뮬레이션 재현 절차, BPMN 모델링 지침 G1~G7, 구성 절차(신호 이벤트와 ROS 메시지 형 연결)를 제시한다. 기존 ref-503(GitHub README)·ref-114(논문)와 같은 연구팀 자료다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-and-workflow-modeling.md"
      ]
    },
    {
      "id": "ref-366",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_task — rmf_task/include/rmf_task/Task.hpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 작업 인터페이스 헤더. Task::Active 의 cancel()·kill()·skip() 의 의미(취소 후 정리 단계, 완료 콜백으로 취소 종료)를 주석으로 설명한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-and-workflow-modeling.md"
      ]
    },
    {
      "id": "ref-404",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_task — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_task",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_task 저장소 README. rmf_task_sequence 의 단계·이벤트 구조와 기본 이벤트 7종(Bundle·DropOff·GoToPlace·PerformAction·PickUp·Placeholder·WaitFor), 모델과 실행 구현의 위치를 설명한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-and-workflow-modeling.md"
      ]
    },
    {
      "id": "ref-116",
      "org": "Filippone, G., Pettinari, S., & Pelliccione, P.",
      "title": "Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis",
      "published": "2026-03-16",
      "url": "https://arxiv.org/abs/2603.15427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "행동 트리·상태 기계·HTN·BPMN 을 제어 구조·표현력·도구 지원으로 비교하고 전문가 설문(83명 요청, 29개 응답)과 후속 인터뷰로 검증한 연구. v1 2026-03-16, v2 2026-08-17, Journal ref IEEE Transactions on Software Engineering (2026). 이번에 v2 본문을 열람했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-and-workflow-modeling.md"
      ]
    },
    {
      "id": "ref-1424",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 (tag 2.14.0) — rmf_fleet_adapter/CHANGELOG.rst",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 패키지 변경 이력. 2.14.0(2026-09-26) 절에 단계 건너뛰기 요청 키 수정(#543) 항목이 있다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-and-workflow-modeling.md"
      ]
    },
    {
      "id": "ref-1425",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 (tag 2.1.0) — VDA5050_EN.md",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/2.1.0/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "VDA 5050 2.1.0 명세 본문. blockingType 을 NONE·SOFT·HARD 세 값으로 정의해 3.0.0 의 SINGLE 과 대조하는 근거가 된다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-and-workflow-modeling.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "로봇이 이미 하역한 뒤 작업이 취소되면, 로봇 쪽 정리 단계 완료와 업무상 인수 취소(재고 반영 취소)를 어떤 완료 조건으로 나눠야 하는가?",
      "areas": [
        24,
        32
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "Open-RMF rmf_task_sequence 의 Bundle 이벤트와 BPMN 병렬 게이트웨이 합류의 의미 차이를 자동으로 검사하거나 변환하는 공개 도구가 있는가?",
      "areas": [
        24,
        54
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "운영 정책 버전이 바뀔 때 이미 시작한 워크플로 인스턴스가 이전 정책을 유지하는지 새 정책으로 옮기는지에 대한 공개 운영 기준이 있는가?",
      "areas": [
        24,
        57
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-optimization/task-and-workflow-modeling.md#5-적용-사례-현장-유형-명시",
      "title": "24. 작업·워크플로 모델링"
    },
    {
      "site_type": "물류창고",
      "item": "완료·인계",
      "link": "docs/categories/planning-and-optimization/task-and-workflow-modeling.md#5-적용-사례-현장-유형-명시",
      "title": "24. 작업·워크플로 모델링"
    }
  ],
  "standards_updates": [
    {
      "name": "BPMN 2.0.2 (OMG formal/13-12-09)",
      "kind": "표준",
      "org": "OMG(Object Management Group)",
      "url": "https://www.omg.org/spec/BPMN/2.0.2/",
      "related_areas": [
        24
      ],
      "summary": "2014-01 발행 BPMN 규범 문서. 수신 작업·상관 키·타이머 이벤트·보상을 정의해 인수 확인 대기와 취소 후 처리를 프로세스 모델로 표현하는 근거가 된다.",
      "ref_id": "ref-502"
    }
  ],
  "additional_research_requests": [
    "분리 주제 페이지(2026-09-25-area02-s6·s7·s8·s11) 본문이 입력에 없고 하루 갱신 상한(2)도 있어 직접 고치지 못했다(예산으로 미룸). 다음 갱신 실행에서 이 페이지들을 입력으로 넣어 s8 의 ref-116 각주(발행일 2026-03 → 2026-03-16, 접근일 2026-10-10, '원문 미열람' 삭제)와 s7 표의 BPMN 행(ref-502 추가)을 고쳐야 한다. 이번 보강은 세부영역 6·7·8·11절에 더했고, 각 보강 소절 첫 줄에 이 페이지들로 가는 링크를 두었다.",
    "3·5절: 한국어 검색과 국내 자료(국내 물류센터·제조 현장의 운반 완료와 인수 확정 분리, 작업 모델링 사례)가 없다. 공통 규칙 8 충족을 위해 다음 갱신에서 보강이 필요하다.",
    "5절: 병원·제조 공장·상업 시설 등 다른 현장 유형의 실제 작업 모델링 사례가 없다. 시작 조건·제약·완료·인계·예외·성과를 채울 공개 사례가 필요하다.",
    "5절 사례 3: FaMe 농업·지상 로봇 협업 시나리오의 작업 대상(물건·공간·정보·사람), 시작 조건·제약·완료 조건·예외 처리, 실외 현장 여부, 실물 로봇 실험 규모를 확인할 원문(시나리오 패키지·논문)이 필요하다.",
    "6절: rmf_task_sequence Bundle 이벤트의 병렬·합류 의미를 API 문서 원문으로 확인해야 한다(f15 한정 해소).",
    "7절: rmf_fleet_adapter #543 에서 고친 단계 건너뛰기 요청 키의 실제 이름을 풀 리퀘스트 원문으로 확인해야 한다.",
    "11절 oq-001: 로봇 하역 완료를 EPCIS 인계 이벤트로 옮기는 공개 구현 사례를 실제로 검색해야 한다(이번 브리프는 검색하지 않아 '확인 못 함').",
    "트랙 반영 제안 2건 가운데 이번 브리프로 뒷받침되지 않은 항목(OPC UA for ISA-95 작업 응답, BPMN 2.0.2 사람 수행자·자원 배정, Serverless Workflow DSL, Isaac Mission Dispatch, PlanSys2, DART-LLM, LTLf→행동 트리, Open-RMF 워크플로 다이어그램, crossflow)은 다음 실행에서 검증한 뒤 반영해야 한다."
  ],
  "fixes_applied": [
    "3절 첫 문단 — 기존 [추정] 문장('arriving 수준의 물리적 인도')을 지우고 f1 [사실][^ref-044]·f2 [사실][^ref-031](3.0.0 §6.2.3.2 표 5)·f3 [사실][^ref-049](기본 정의 필드 한정)로 나눠 적은 뒤 f4 를 [의견](이 위키의 판단)으로 덧붙이고 '이 구성을 적용한 표준·사례는 확인하지 못했다' 한정을 유지했다.",
    "5절 시나리오 1 — 'CBV로 보면 arriving에 가깝다' 문장을 f27 [의견]으로 바꿔 drop 완료를 arriving·receiving 으로 단정하지 않고 업무 측(WMS) 확인으로 단계를 정한다고 썼다(완료·인계 칸의 IngestorResult 문장도 f3 대로 기본 정의 필드로 한정했다).",
    "5절 — 사례 3(현장 유형 기타, 농업·지상 로봇 협업 시뮬레이션, 67. 기타 현장 링크)을 새로 두고 f7·f8·f24 를 작업 대상·수행 자원·서술에 놓았으며, 시작 조건·제약·완료·인계·예외·성과는 '미확인'으로 두고 f9 를 [의견](이 위키의 판단)으로 적었다. site_matrix_updates 의 site_type 은 '기타'로 냈다.",
    "f17 — 7절 보강에서 'SINGLE 은 2.1.0 명세에는 없고 3.0.0 명세에는 있다'로 쓰고, 두 판 사이 다른 판 미확인과 같은 발행 계열 두 판의 대조라 교차 확인이 아님을 밝혔다.",
    "의견 주체 — f4·f9·f12·f18·f20·f23·f25·f27 을 쓴 [의견] 문장마다 '이 위키의 판단이다'를 넣었다(3·5·6·7·8·11절).",
    "ref-116 — 세부영역 13절 각주를 발행일 2026-03-16·접근일 2026-10-10 으로 고치고 '(원문 미열람)'을 뺐으며, 8절 보강에 v2(2026-08-17)·IEEE Transactions on Software Engineering (2026) 게재 정보와 f22 연구 방법(83명 요청·29개 응답, 인터뷰 3명·서면 1명, 처리량 측정 아님)을 적었다. 8절 분리 주제 페이지(2026-09-25-area02-s8)는 본문이 입력에 없고 갱신 상한이 있어 직접 고치지 못해 reference_updates 로 참고문헌 ref-116 을 갱신하고 additional_research_requests 에 남겼다.",
    "ref-031 — 새 문장(3절 f2, 7절 f16)에 '3.0.0 태그판(main 브랜치 판과 다를 수 있다)'을 밝히고 발표일은 쓰지 않았으며, 13절 각주 접근일을 2026-10-10 으로 고쳤다.",
    "f19·f20 — 7절 보강에 '개별 패키지 rmf_fleet_adapter 2.14.0(2026-09-26)'으로 적고 Open-RMF 배포판 버전이 아니라고 밝혔으며, 고친 키의 이름은 '미확인'으로 두었다.",
    "f15·f26 — 6절에 'Bundle 이벤트의 병렬·합류 의미는 원문 미확인', 11절 oq-001 에 '공개 구현 사례는 검색하지 않아 확인 못 함' 한정을 남기고 '없다'로 단정하지 않았다.",
    "범위 경계 — 3절과 11절에 수령자 재고 편입(CBV receiving)·EPCIS 이벤트 생성·재고 확정을 '연계 대상: 상위 업무 시스템(WMS 등)'으로 표시하고 ROP 몫을 완료 조건 구분과 대기·분기로 한정했다.",
    "연결 — f16~f18 은 7절에서 20. 로봇·제조사 관제 연동, f10~f12 는 6절에서 32. 예외 복구·재계획·업무 연속성, f1~f4 는 3절에서 17. 작업 대상·자산 식별과 인계 추적과 번호·이름으로 연결하고 10절에 덧붙였으며 프런트매터 related_areas 에 32·67 을 더했다.",
    "6절 분리 주제 페이지 — 본문이 입력에 없어 해당 페이지는 고치지 않고(기존 Camunda 문장 ref-113 과 ref-112 각주는 그 페이지와 5절에 그대로 남음) 세부영역 6절에 f5(ref-502)·f6 을 덧붙였으며, Camunda 고유의 메시지 보존 시간·중복 거부 동작을 BPMN 표준 보장으로 넓히지 않는다고 적었다.",
    "7절 분리 주제 페이지 — 그 페이지 표는 입력에 없어 고치지 못하고, 세부영역 7절에 BPMN 2.0.2(ref-502, formal/13-12-09, 2014-01) 행을 포함한 보강 표를 더했으며 VDA 5050 blockingType(f16·f17)과 rmf_fleet_adapter 2.14.0(f19)을 기준일과 함께 적었다.",
    "트랙 반영 제안 2건 — 이번 브리프로 뒷받침되는 FaMe(f7·f8·f24, 5·8·11절)와 임무 기술 형식 비교 연구(f21~f23, 8절)만 반영하고, 나머지 항목은 본문에 넣지 않고 '제안'으로 남겼다(additional_research_requests 에 기록).",
    "11절과 open_question_updates — oq-001(f26·f27)·oq-014(f24·f25)는 '열림'을 유지한 채 11절에 부분 근거만 달았고(상태가 바뀌지 않아 update 는 내지 않음), 새 질문 3건을 관련 영역 24·32 / 24·54 / 24·57 로 등록했다.",
    "glossary_updates — '수신 작업 (Receive Task (BPMN))'을 신규로, 보상 후보는 'BPMN 보상 (Compensation (BPMN))'으로 표기하고 설명에 기존 '보상 트랜잭션 (Compensating Transaction)'과 다른 개념임과 연결을 적었다.",
    "인용 — 페이지 본문에 출처 원문의 직접 인용을 넣지 않고 모두 재서술했다(ref-044·ref-031·ref-502 포함).",
    "reference_updates 의 ref-1423·ref-1424·ref-1425 — 브리프 id 를 그대로 쓰고 changelog_entry 비고에 'id 충돌 여부 퍼블리셔 확인 필요'를 남겼다.",
    "2차: 기존 분리 주제 페이지 링크 복원 — 6·7·8·11절 패치를 append 에서 replace 로 바꿔 각 절의 기존 첫 문장을 유지하고, '### 2026-10-10 보강' 소절 첫 줄에 '이전 정리(2026-09-25)는 [24. 작업·워크플로 모델링 — 대표 접근법과 기술 / 관련 표준·프레임워크·오픈소스 / 대표 연구와 자료 / 열린 질문](../../topics/2026/2026-09-25-area02-s6·s7·s8·s11.md)에 있다.' 줄을 두어 자동 분리 뒤에도 링크가 남게 했다.",
    "2차: 5절 사례 3 작업 대상 칸 — '미확인'으로 바꾸고 f24 문장(FaMe 의 모델링·구성·실행과 ROS 2 위 직접 실행, [사실][^ref-1423])을 표 아래 서술 문단으로 옮겼으며, 서술의 미확인 목록에 작업 대상을 더했다. site_matrix_updates 에서 {기타, 작업 대상}을 빼고 {기타, 수행 자원}은 유지했다.",
    "2차: 6절 보강 첫 문단의 Camunda 구절 — 구체 동작 이름(메시지 보존 시간·중복 거부)을 빼고 '이전 정리의 기존 Camunda 근거 문장이 서술한 엔진 고유 동작'으로만 가리켰다.",
    "2차: pages[0].diff_summary — '새 각주 6건'을 '새 각주 1건(ref-1423)'으로 고치고 ref-366·ref-404·ref-502·ref-1424·ref-1425 는 자동 분리 뒤 분리 주제 페이지의 출처 절에만 남는다고 적었다.",
    "분량 초과 자동 분리: 24. 작업·워크플로 모델링 본문 10,315자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 4,459자"
  ]
}
```

### runs/2026-10-10-01/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/planning-and-optimization/task-and-workflow-modeling.md (8개 절)
- 분량 초과 자동 분리:
    - docs/categories/planning-and-optimization/task-and-workflow-modeling.md "11. 열린 질문" → docs/topics/2026/2026-10-10-area24-s11.md (1,498자)
    - docs/categories/planning-and-optimization/task-and-workflow-modeling.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-10-area24-s6.md (1,442자)
    - docs/categories/planning-and-optimization/task-and-workflow-modeling.md "3. 왜 중요한가" → docs/topics/2026/2026-10-10-area24-s3.md (1,339자)
    - docs/categories/planning-and-optimization/task-and-workflow-modeling.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-10-area24-s7.md (1,291자)
    - docs/categories/planning-and-optimization/task-and-workflow-modeling.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-10-area24-s8.md (886자)
```

### runs/2026-10-10-01/pages/categories/planning-and-optimization/task-and-workflow-modeling.md

```markdown
---
title: "24. 작업·워크플로 모델링"
type: area
category: "G. 계획·최적화"
area_no: 24
related_areas: [17, 20, 23, 26, 29, 32, 38, 39, 54, 67]
tags: [BPMN, ISA-95, 완료 조건, 인수 확인, 워크플로 넷, Open-RMF]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-10-10
sources: [ref-023, ref-031, ref-044, ref-049, ref-110, ref-111, ref-112, ref-113, ref-116, ref-117, ref-118, ref-119, ref-121, ref-123, ref-124, ref-366, ref-404, ref-502, ref-1423, ref-1424, ref-1425]
last_run: 2026-10-10
version: 3
---

[홈](../../index.md) › [G. 계획·최적화](index.md) › 24. 작업·워크플로 모델링

# 24. 작업·워크플로 모델링

!!! info "소속 대분류"
    [G. 계획·최적화](index.md) — 핵심 질문:
    누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 한 줄 정의

현장 업무를 단계·선후관계·완료 조건으로 정의하고, 계획과 실행이 따를 운영 정책을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업·워크플로 모델링**: 현장 업무(운반·배송·순찰·점검·조작·서비스 등)를 단계·선후관계·완료 조건으로 분해해 정의한다
- **동작 완료와 업무 완료 연결**: 로봇의 동작 완료(도착·내려놓음)와 업무 완료(인수 확인·기록 반영)를 구분해 잇는다
- **운영 정책 설정**: 우선순위·운영 시간·구역 규칙·충전 기준 같은 운영 정책을 설정하고 버전으로 관리해 계획과 실행이 따르게 한다

이전 분류(2026-09-24)에서 이 페이지는 옛 2번 영역 ‘공정·워크플로 모델링’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 [옛 분류원문]

> 옛 질문: ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? [옛 분류원문]

## 2. 핵심 질문

현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? [분류원문]

## 3. 왜 중요한가

로봇 관제 규격의 하역 완료와 업무 어휘의 인수·재고 반영은 서로 다른 원문이 각각 정의한다(2026-10-10 확인). [사실][^ref-044][^ref-031][^ref-049]

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 왜 중요한가](../../topics/2026/2026-10-10-area24-s3.md)에 있다.

## 4. 핵심 개념과 용어

작업 단계와 완료 조건을 표현하는 데 쓰이는 핵심 용어는 다음과 같다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area02-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오 1·2는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 물류창고 밖의 사례는 아래 사례 3(현장 유형: 기타)에 있다.

다음은 설명을 위한 가상의 시나리오이며, 로봇의 완료 신호와 업무상 완료가 어디서 갈리는지를 보인다.

### 시나리오 1

**물류 흐름 단계:** 입고 → 적치

**시나리오:** 도크에서 하역된 입고 팔레트를 로봇이 하역 지점(워크셀)으로 운반해 인계하고, 입고 확정 뒤 보관 구역에 적치

| 항목 | 내용 |
|---|---|
| 시작 조건 | 입고 예정 화물이 도크에 도착해 상위 업무 시스템(WMS)이 입고 운반 작업을 요청한다. |
| 작업 대상 | 입고 팔레트와 그 화물 식별자. 이 식별자나 작업 id가 로봇 작업과 업무 확인을 잇는 키가 된다. |
| 수행 자원 | 로봇은 운반·하역을, 하역 지점 워크셀은 하역 결과 보고를, WMS는 인수 확인과 재고 반영을 맡는다. Open-RMF 배송 작업에서 로봇은 하역 지점에서 IngestorResult를 받을 때까지 IngestorRequest를 보낸다. [사실][^ref-023][^ref-049] |
| 제약 | 검수 종료 후 적치 시작, 같은 도크의 상차·하차 병행 금지, 하역 종료 후 일정 시간 안의 입고 확정 같은 선후·병행·시간 제약. ISA-95 세그먼트 의존 유형(AfterEnd, NotInParallel, NoLaterAfterEnd)으로 이런 제약을 단순 순서보다 세밀하게 표현할 수 있을 것으로 보이지만, ISA-95는 제조 운영 관리 표준이며 창고 작업에 적용한 사례는 확인하지 못했다. [추정][^ref-117][^ref-118] |
| 완료·인계 | VDA 5050 3.0.0은 drop 동작 완료를 적재물이 이동로봇을 떠나고 로봇이 새 적재 상태를 보고한 때로 정의한다. [사실][^ref-031] IngestorResult의 기본 정의 필드는 시각·요청 id·워크셀 id·상태(ACKNOWLEDGED, SUCCESS, FAILED)이며, 이 기본 필드에는 수령자 재고 편입 여부가 없다. [사실][^ref-049] 따라서 입고 완료와 재고 변경은 CBV receiving에 해당하는 WMS 인수 확인이 따로 있어야 인정할 수 있을 것으로 보인다(적용 표준·사례 미확인). [추정][^ref-031][^ref-049][^ref-044] |
| 예외·성과 | 인수 확인이 오지 않거나 하역이 실패하면 공정은 대기하거나 예외로 분기해야 한다. [추정][^ref-044][^ref-119] Open-RMF 작업 상태 스키마는 failed·canceled·delayed 등 작업 상태와 단계별 이벤트·소요 시간 추정값을 보고한다. [사실][^ref-111] 처리량·시간·비용 영향은 미확인이다. |

로봇이 팔레트를 내려놓으면 로봇 쪽 작업은 끝나지만, 이 시점을 곧바로 CBV arriving이나 receiving으로 단정하지 않고 어느 업무 단계에 해당하는지는 WMS 같은 업무 측 확인으로 정하는 것이 적절하다는 것이 이 위키의 판단이다. [의견][^ref-044][^ref-031] BPMN 모델에서 로봇 운반을 하나의 작업 단계로 두고 그 뒤에 WMS 인수 확인 메시지를 기다리는 수신 단계를 두어 작업 id나 화물 식별자로 상관시키면, 두 완료를 서로 다른 완료 조건을 가진 연속 단계로 표현할 수 있을 것으로 보인다(이 구성을 물류 로봇에 적용한 표준·사례는 확인하지 못했다). [추정][^ref-112][^ref-113][^ref-044]

입고 확정이 나야 적치 작업이 시작되므로, 적치 단계의 선후 제약은 입고 단계의 완료 조건에 기대게 된다. [추정][^ref-117][^ref-118]

### 시나리오 2

**물류 흐름 단계:** 출하

**시나리오:** 출하 대기 화물을 로봇이 출하 도크로 운반해 인도

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 포장을 마친 출하 화물 |
| 수행 자원 | 해당 없음 |
| 제약 | 해당 없음 |
| 완료·인계 | 로봇의 drop 완료는 화물의 물리적 인도까지만 가리킨다. [사실][^ref-031] 업무상 이행의 끝은 SCOR B2C 이행의 마지막 단계 F1.11 배송 증빙 또는 고객 인수 확보이다. [사실][^ref-123] |
| 예외·성과 | 해당 없음 |

출하에서도 로봇 작업 완료와 고객 인수 사이에 업무 단계가 남는다. [추정][^ref-031][^ref-123]

### 사례 3 — 물류창고 밖: 농업·지상 로봇 협업 시뮬레이션

**현장 유형:** 기타

**사례:** 농업·지상 로봇 협업 시뮬레이션에서 BPMN 협업 모델로 다중 로봇 임무를 실행하는 공개 예제(FaMe, [67. 기타 현장](../site-type-applications/other-sites.md))

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 모델링 지침은 로봇을 풀(Pool), 임무를 프로세스(Process), 동작을 활동(Activity)으로 나타낸다. [사실][^ref-1423] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

이 사례는 물류창고 밖의 공개 작업 모델링 예제다. FaMe 연구팀(University of Camerino PROS Lab)은 공식 페이지(2022-05-03 게시)에서 지상 로봇 협업과 농업 두 시나리오의 시뮬레이션 패키지와 엔진 패키지의 빌드·실행 절차(colcon build, ros2 launch)를 공개한다. [사실][^ref-1423] FaMe는 BPMN 협업 다이어그램으로 다중 로봇 임무를 정의하고 모델링·구성·실행 단계를 거쳐 각 로봇에서 ROS 2 위에 그 협업을 직접 실행하는 공개 프레임워크다. [사실][^ref-1423] 같은 지침은 병렬 동작을 AND 게이트웨이, 내부 선택을 XOR 게이트웨이, 시간 대기를 타이머 이벤트, 실행 오류를 오류 이벤트로 표현하게 한다. [사실][^ref-1423] 이 예제가 다루는 작업 대상(물건·공간·정보·사람)과 시작 조건·제약·완료 조건·예외 처리의 구체 내용, 시나리오가 실외 현장인지는 공식 페이지에서 확인하지 못해 현장 유형을 기타로 둔다.

이 예제는 시뮬레이션 재현 자료이며 현장 운영 성능 근거가 아니므로, 국내 상용 운영 실적이나 현장 성능 근거로 분류하지 않는 편이 좋다는 것이 이 위키의 판단이다. [의견][^ref-1423]

## 6. 대표 접근법과 기술

이 위키는 이 영역의 관련 접근법을 업무 프로세스 표기(BPMN), 제조 운영 표준의 세그먼트 의존(ISA-95·B2MML), 로봇 오케스트레이션의 작업 단계 구성(Open-RMF), 형식적 설계 점검(워크플로 넷)의 네 갈래로 정리한다. [의견][^ref-112][^ref-117][^ref-110][^ref-121]

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 대표 접근법과 기술](../../topics/2026/2026-10-10-area24-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역과 관련된 표준·오픈소스는 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-10-area24-s7.md)에 있다.

## 8. 대표 연구와 자료

로봇 작업을 업무 프로세스 형식으로 기술·실행하고 그 실행 기록을 분석하는 연구가 대표 자료다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 대표 연구와 자료](../../topics/2026/2026-10-10-area24-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이 영역에서 ROP는 업무 단계와 로봇 작업 단위 사이의 순서·대기·완료 조건을 맡고, 재고 확정과 로봇 내부 동작 흐름은 연계 대상으로 두는 구조가 경계와 맞아 보인다. [추정][^ref-044][^ref-119][^ref-116]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 운반 완료 이벤트를 전달하고 인수 확인을 기다리거나 예외로 분기하는 공정 단계 [추정][^ref-044][^ref-119] | 연계 대상: 수령자 재고 반영(CBV receiving)과 재고 운영 관리(IEC 62264-3) — WMS·MES 재고 확정 [추정][^ref-044][^ref-119] |
| 로봇 자체 지능·제어 | 업무 단계(BPMN·ISA-95·SCOR 수준)와 로봇 작업 단위(Open-RMF 단계, VDA 5050 동작) 사이의 순서·대기·완료 조건 [추정][^ref-112][^ref-110] | 연계 대상: 로봇 내부 동작 흐름(행동 트리·상태 기계로 구현되는 주행·파지 등) — 제조사 [추정][^ref-116] |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

두 층의 상태를 잇는 표준 매핑은 확인하지 못했으므로 위 표는 표준 정의를 엮은 추정이다. [추정][^ref-110][^ref-031] 경계의 전체 기준은 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

공정 모델의 단계와 완료 조건은 업무 시스템·식별·관제·실행 신뢰성·스케줄링·분석·검증 영역과 맞물린다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area02-s10.md)에 있다.

2026-10-10 보강으로 더한 연결:

- [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 취소 요청과 취소 후 정리 완료, 보상 단계의 구분(6절 보강)이 예외 복구 절차와 이어진다.
- [67. 기타 현장](../site-type-applications/other-sites.md) — 농업·지상 로봇 협업 시뮬레이션 사례(5절 사례 3)의 현장 유형이다.
- 기존 연결 가운데 [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)은 하역 완료와 인수·재고 반영의 구분(3절)으로, [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)은 VDA 5050 blockingType의 병행 제약(7절 보강)으로 이어진다.

## 11. 열린 질문

이 영역에서 아직 답하지 못한 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 열린 질문](../../topics/2026/2026-10-10-area24-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [24. 작업·워크플로 모델링](task-and-workflow-modeling.md) — 섹션 3~11 신규 작성(BPMN·ISA-95/B2MML·Open-RMF 작업 단계·CBV 업무 단계·워크플로 넷·OCEL 2.0, 입고 → 적치·출하 시나리오), 페이지 상태 자동 영역 추가. 2차 수정: 5절 태그 강등 2건·예외 칸 태그 추가, 6절 요약 [의견], 프런트매터 sources 정리 (실행 2026-09-25-09)
- 2026-09-25 · 생성 · [24. 작업·워크플로 모델링 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area02-s4.md) — 자동 분리: 2. 공정·워크플로 모델링 의 "4. 핵심 개념과 용어" 절을 옮겼다. 2차 수정: ref-120 각주와 건전성의 교착·라이브락 문장을 빼고 ref-121 근거 문장으로 줄였다 (실행 2026-09-25-09)
- 2026-09-25 · 생성 · [24. 작업·워크플로 모델링 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area02-s6.md) — 자동 분리: 2. 공정·워크플로 모델링 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 첫 문장을 [의견] 정리로 바꾸고 ref-120 문장을 ref-121 근거 문장으로 줄였다 (실행 2026-09-25-09)
- 2026-09-25 · 생성 · [24. 작업·워크플로 모델링 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area02-s7.md) — 자동 분리: 2. 공정·워크플로 모델링 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,105자)을 옮겼다 (실행 2026-09-25-09)
- 2026-09-25 · 생성 · [24. 작업·워크플로 모델링 — 대표 연구와 자료](../../topics/2026/2026-09-25-area02-s8.md) — 자동 분리: 2. 공정·워크플로 모델링 의 "8. 대표 연구와 자료" 절(870자)을 옮겼다 (실행 2026-09-25-09)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-10-10
[^ref-049]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg, 접근일 2026-10-10
[^ref-110]: Open Robotics, Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-25
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25
[^ref-112]: OMG(Object Management Group), About the Business Process Model And Notation Specification Version 2.0, 미확인, https://www.omg.org/spec/BPMN/2.0/About-BPMN, 접근일 2026-09-25 (원문 미열람)
[^ref-113]: Camunda, Messages | Camunda 8 Docs (camunda-docs: docs/components/concepts/messages.md), 미확인, https://docs.camunda.io/docs/components/concepts/messages/, 접근일 2026-09-25
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03-16, https://arxiv.org/abs/2603.15427, 접근일 2026-10-10
[^ref-117]: MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd, 접근일 2026-09-25
[^ref-118]: MESA International, B2MML-BatchML — Schema/B2MML-OperationsDefinition.xsd, 미확인, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-OperationsDefinition.xsd, 접근일 2026-09-25
[^ref-119]: IEC / ISO, IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management, 2016, https://www.iso.org/standard/67480.html, 접근일 2026-09-25 (원문 미열람)
[^ref-121]: Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022), The complexity of soundness in workflow nets, 2022, https://arxiv.org/abs/2201.05588, 접근일 2026-09-25 (원문 미열람)
[^ref-123]: ASCM, SCOR Model — Fulfill F1.3 Pick Product, 미확인, https://scor.ascm.org/processes/fulfill/F1.3, 접근일 2026-09-25 (원문 미열람)
[^ref-1423]: University of Camerino PROS Lab, FaMe — A BPMN-driven Framework for Multi-Robot System Development (공식 페이지·사용 지침), 2022-05-03, https://pros.unicam.it/fame/, 접근일 2026-10-10
```

### docs/categories/planning-and-optimization/task-and-workflow-modeling.md

```markdown
---
title: "24. 작업·워크플로 모델링"
type: area
category: "G. 계획·최적화"
area_no: 24
related_areas: [17, 20, 23, 26, 29, 38, 39, 54]
tags: [BPMN, ISA-95, 완료 조건, 인수 확인, 워크플로 넷, Open-RMF]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-023, ref-031, ref-044, ref-049, ref-110, ref-111, ref-112, ref-113, ref-116, ref-117, ref-118, ref-119, ref-121, ref-123, ref-124]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [G. 계획·최적화](index.md) › 24. 작업·워크플로 모델링

# 24. 작업·워크플로 모델링

!!! info "소속 대분류"
    [G. 계획·최적화](index.md) — 핵심 질문:
    누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 한 줄 정의

현장 업무를 단계·선후관계·완료 조건으로 정의하고, 계획과 실행이 따를 운영 정책을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업·워크플로 모델링**: 현장 업무(운반·배송·순찰·점검·조작·서비스 등)를 단계·선후관계·완료 조건으로 분해해 정의한다
- **동작 완료와 업무 완료 연결**: 로봇의 동작 완료(도착·내려놓음)와 업무 완료(인수 확인·기록 반영)를 구분해 잇는다
- **운영 정책 설정**: 우선순위·운영 시간·구역 규칙·충전 기준 같은 운영 정책을 설정하고 버전으로 관리해 계획과 실행이 따르게 한다

이전 분류(2026-09-24)에서 이 페이지는 옛 2번 영역 ‘공정·워크플로 모델링’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 [옛 분류원문]

> 옛 질문: ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? [옛 분류원문]

## 2. 핵심 질문

현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? [분류원문]

## 3. 왜 중요한가

로봇 관제 규격의 완료 신호(VDA 5050 drop 완료, Open-RMF IngestorResult SUCCESS)는 GS1 CBV의 arriving 수준의 물리적 인도만 나타내고 수령자 재고 반영(receiving)과 점유·소유 변경(accepting)은 다른 규격이 정의하므로, 공정 모델은 ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 서로 다른 단계와 완료 조건으로 두고 둘을 잇는 식별 키를 명시해야 할 것으로 보인다(이 구성을 적용한 표준·사례는 확인하지 못했다). [추정][^ref-031][^ref-049][^ref-044]

공급망 참조 모델도 업무 완료를 로봇 동작이 아니라 인수 시점에 둔다. ASCM SCOR 모델의 B2C 이행(F1)은 F1.3 Pick Product 같은 단계를 거쳐 마지막 단계인 F1.11 Obtain Proof of Delivery or Customer Acceptance(배송 증빙 또는 고객 인수 확보)로 끝난다(2026-09-25 확인). [사실][^ref-123]

국내 제도도 물류센터를 처리 과정 단위로 나누어 본다. 국토교통부 스마트물류센터 인증은 입고·보관·피킹·출고 등 물류처리 과정별 첨단·자동화 정도를 보는 기능영역과, 시설의 구조적 성능·정보시스템 도입 수준 등을 보는 기반영역으로 평가해 1~5등급을 부여한다(2026-09-25 확인). [사실][^ref-124]

## 4. 핵심 개념과 용어

작업 단계와 완료 조건을 표현하는 데 쓰이는 핵심 용어는 다음과 같다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area02-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

다음은 설명을 위한 가상의 시나리오이며, 로봇의 완료 신호와 업무상 완료가 어디서 갈리는지를 보인다.

### 시나리오 1

**물류 흐름 단계:** 입고 → 적치

**시나리오:** 도크에서 하역된 입고 팔레트를 로봇이 하역 지점(워크셀)으로 운반해 인계하고, 입고 확정 뒤 보관 구역에 적치

| 항목 | 내용 |
|---|---|
| 시작 조건 | 입고 예정 화물이 도크에 도착해 상위 업무 시스템(WMS)이 입고 운반 작업을 요청한다. |
| 작업 대상 | 입고 팔레트와 그 화물 식별자. 이 식별자나 작업 id가 로봇 작업과 업무 확인을 잇는 키가 된다. |
| 수행 자원 | 로봇은 운반·하역을, 하역 지점 워크셀은 하역 결과 보고를, WMS는 인수 확인과 재고 반영을 맡는다. Open-RMF 배송 작업에서 로봇은 하역 지점에서 IngestorResult를 받을 때까지 IngestorRequest를 보낸다. [사실][^ref-023][^ref-049] |
| 제약 | 검수 종료 후 적치 시작, 같은 도크의 상차·하차 병행 금지, 하역 종료 후 일정 시간 안의 입고 확정 같은 선후·병행·시간 제약. ISA-95 세그먼트 의존 유형(AfterEnd, NotInParallel, NoLaterAfterEnd)으로 이런 제약을 단순 순서보다 세밀하게 표현할 수 있을 것으로 보이지만, ISA-95는 제조 운영 관리 표준이며 창고 작업에 적용한 사례는 확인하지 못했다. [추정][^ref-117][^ref-118] |
| 완료·인계 | VDA 5050 3.0.0은 drop 동작 완료를 적재물이 이동로봇을 떠나고 로봇이 새 적재 상태를 보고한 때로 정의한다. [사실][^ref-031] IngestorResult는 요청 id·워크셀 id·상태(ACKNOWLEDGED, SUCCESS, FAILED)만 담는다. [사실][^ref-049] 따라서 입고 완료와 재고 변경은 CBV receiving에 해당하는 WMS 인수 확인이 따로 있어야 인정할 수 있을 것으로 보인다(적용 표준·사례 미확인). [추정][^ref-031][^ref-049][^ref-044] |
| 예외·성과 | 인수 확인이 오지 않거나 하역이 실패하면 공정은 대기하거나 예외로 분기해야 한다. [추정][^ref-044][^ref-119] Open-RMF 작업 상태 스키마는 failed·canceled·delayed 등 작업 상태와 단계별 이벤트·소요 시간 추정값을 보고한다. [사실][^ref-111] 처리량·시간·비용 영향은 미확인이다. |

로봇이 팔레트를 내려놓으면 로봇 쪽 작업은 끝나지만, 이 시점은 CBV로 보면 arriving에 가깝다. [추정][^ref-031][^ref-049][^ref-044] BPMN 모델에서 로봇 운반을 하나의 작업 단계로 두고 그 뒤에 WMS 인수 확인 메시지를 기다리는 수신 단계를 두어 작업 id나 화물 식별자로 상관시키면, 두 완료를 서로 다른 완료 조건을 가진 연속 단계로 표현할 수 있을 것으로 보인다(이 구성을 물류 로봇에 적용한 표준·사례는 확인하지 못했다). [추정][^ref-112][^ref-113][^ref-044]

입고 확정이 나야 적치 작업이 시작되므로, 적치 단계의 선후 제약은 입고 단계의 완료 조건에 기대게 된다. [추정][^ref-117][^ref-118]

### 시나리오 2

**물류 흐름 단계:** 출하

**시나리오:** 출하 대기 화물을 로봇이 출하 도크로 운반해 인도

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 포장을 마친 출하 화물 |
| 수행 자원 | 해당 없음 |
| 제약 | 해당 없음 |
| 완료·인계 | 로봇의 drop 완료는 화물의 물리적 인도까지만 가리킨다. [사실][^ref-031] 업무상 이행의 끝은 SCOR B2C 이행의 마지막 단계 F1.11 배송 증빙 또는 고객 인수 확보이다. [사실][^ref-123] |
| 예외·성과 | 해당 없음 |

출하에서도 로봇 작업 완료와 고객 인수 사이에 업무 단계가 남는다. [추정][^ref-031][^ref-123]

## 6. 대표 접근법과 기술

이 위키는 이 영역의 관련 접근법을 업무 프로세스 표기(BPMN), 제조 운영 표준의 세그먼트 의존(ISA-95·B2MML), 로봇 오케스트레이션의 작업 단계 구성(Open-RMF), 형식적 설계 점검(워크플로 넷)의 네 갈래로 정리한다. [의견][^ref-112][^ref-117][^ref-110][^ref-121]

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area02-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역과 관련된 표준·오픈소스는 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area02-s7.md)에 있다.

## 8. 대표 연구와 자료

로봇 작업을 업무 프로세스 형식으로 기술·실행하고 그 실행 기록을 분석하는 연구가 대표 자료다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 대표 연구와 자료](../../topics/2026/2026-09-25-area02-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이 영역에서 ROP는 업무 단계와 로봇 작업 단위 사이의 순서·대기·완료 조건을 맡고, 재고 확정과 로봇 내부 동작 흐름은 연계 대상으로 두는 구조가 경계와 맞아 보인다. [추정][^ref-044][^ref-119][^ref-116]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 운반 완료 이벤트를 전달하고 인수 확인을 기다리거나 예외로 분기하는 공정 단계 [추정][^ref-044][^ref-119] | 연계 대상: 수령자 재고 반영(CBV receiving)과 재고 운영 관리(IEC 62264-3) — WMS·MES 재고 확정 [추정][^ref-044][^ref-119] |
| 로봇 자체 지능·제어 | 업무 단계(BPMN·ISA-95·SCOR 수준)와 로봇 작업 단위(Open-RMF 단계, VDA 5050 동작) 사이의 순서·대기·완료 조건 [추정][^ref-112][^ref-110] | 연계 대상: 로봇 내부 동작 흐름(행동 트리·상태 기계로 구현되는 주행·파지 등) — 제조사 [추정][^ref-116] |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

두 층의 상태를 잇는 표준 매핑은 확인하지 못했으므로 위 표는 표준 정의를 엮은 추정이다. [추정][^ref-110][^ref-031] 경계의 전체 기준은 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

공정 모델의 단계와 완료 조건은 업무 시스템·식별·관제·실행 신뢰성·스케줄링·분석·검증 영역과 맞물린다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area02-s10.md)에 있다.

## 11. 열린 질문

이 영역에서 아직 답하지 못한 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [24. 작업·워크플로 모델링 — 열린 질문](../../topics/2026/2026-09-25-area02-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [24. 작업·워크플로 모델링](task-and-workflow-modeling.md) — 섹션 3~11 신규 작성(BPMN·ISA-95/B2MML·Open-RMF 작업 단계·CBV 업무 단계·워크플로 넷·OCEL 2.0, 입고 → 적치·출하 시나리오), 페이지 상태 자동 영역 추가. 2차 수정: 5절 태그 강등 2건·예외 칸 태그 추가, 6절 요약 [의견], 프런트매터 sources 정리 (실행 2026-09-25-09)
- 2026-09-25 · 생성 · [24. 작업·워크플로 모델링 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area02-s4.md) — 자동 분리: 2. 공정·워크플로 모델링 의 "4. 핵심 개념과 용어" 절을 옮겼다. 2차 수정: ref-120 각주와 건전성의 교착·라이브락 문장을 빼고 ref-121 근거 문장으로 줄였다 (실행 2026-09-25-09)
- 2026-09-25 · 생성 · [24. 작업·워크플로 모델링 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area02-s6.md) — 자동 분리: 2. 공정·워크플로 모델링 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 첫 문장을 [의견] 정리로 바꾸고 ref-120 문장을 ref-121 근거 문장으로 줄였다 (실행 2026-09-25-09)
- 2026-09-25 · 생성 · [24. 작업·워크플로 모델링 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area02-s7.md) — 자동 분리: 2. 공정·워크플로 모델링 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,105자)을 옮겼다 (실행 2026-09-25-09)
- 2026-09-25 · 생성 · [24. 작업·워크플로 모델링 — 대표 연구와 자료](../../topics/2026/2026-09-25-area02-s8.md) — 자동 분리: 2. 공정·워크플로 모델링 의 "8. 대표 연구와 자료" 절(870자)을 옮겼다 (실행 2026-09-25-09)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-09-25
[^ref-049]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg, 접근일 2026-09-25
[^ref-110]: Open Robotics, Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-25
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25
[^ref-112]: OMG(Object Management Group), About the Business Process Model And Notation Specification Version 2.0, 미확인, https://www.omg.org/spec/BPMN/2.0/About-BPMN, 접근일 2026-09-25 (원문 미열람)
[^ref-113]: Camunda, Messages | Camunda 8 Docs (camunda-docs: docs/components/concepts/messages.md), 미확인, https://docs.camunda.io/docs/components/concepts/messages/, 접근일 2026-09-25
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-25 (원문 미열람)
[^ref-117]: MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd, 접근일 2026-09-25
[^ref-118]: MESA International, B2MML-BatchML — Schema/B2MML-OperationsDefinition.xsd, 미확인, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-OperationsDefinition.xsd, 접근일 2026-09-25
[^ref-119]: IEC / ISO, IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management, 2016, https://www.iso.org/standard/67480.html, 접근일 2026-09-25 (원문 미열람)
[^ref-121]: Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022), The complexity of soundness in workflow nets, 2022, https://arxiv.org/abs/2201.05588, 접근일 2026-09-25 (원문 미열람)
[^ref-123]: ASCM, SCOR Model — Fulfill F1.3 Pick Product, 미확인, https://scor.ascm.org/processes/fulfill/F1.3, 접근일 2026-09-25 (원문 미열람)
[^ref-124]: 국가물류통합정보센터(국토교통부), 스마트물류센터 인증제 안내, 미확인, https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW, 접근일 2026-09-25 (원문 미열람)
```

### runs/2026-10-10-01/pages/topics/2026/2026-10-10-area24-s11.md

```markdown
---
title: "24. 작업·워크플로 모델링 — 열린 질문"
type: topic
category: "G. 계획·최적화"
primary_area_no: 24
related_areas: [17, 20, 23, 26, 29, 32, 38, 39, 54, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-031, ref-044, ref-049, ref-1423, ref-404]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-and-workflow-modeling.md#11
---

[홈](../../index.md) › [주제](../index.md) › 24. 작업·워크플로 모델링 — 열린 질문

# 24. 작업·워크플로 모델링 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에서 아직 답하지 못한 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에서 아직 답하지 못한 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

### 2026-10-10 보강

이전 정리(2026-09-25)는 [24. 작업·워크플로 모델링 — 열린 질문](2026-09-25-area02-s11.md)에 있다.

- **oq-001** (상태: 열림 · 부분 근거 2026-10-10 · 실행 2026-10-10-01) 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가? 확인한 원문(CBV.ttl, VDA 5050 3.0.0 태그판, IngestorResult.msg)은 로봇 동작 완료와 업무 단계 각각의 정의까지만 제공하며, 로봇 하역 완료를 EPCIS 인계 이벤트로 옮기는 표준 변환은 확인되지 않는다(공개 구현 사례는 검색하지 않아 확인 못 함). [추정][^ref-044][^ref-031][^ref-049] drop 완료를 곧바로 CBV arriving이나 receiving으로 단정하지 않고 업무 측 확인으로 어느 단계인지 정하는 수준까지만 답을 보강하는 것이 적절하다는 것이 이 위키의 판단이다. [의견][^ref-044][^ref-031] EPCIS 이벤트 생성과 재고 확정은 연계 대상: 상위 업무 시스템(WMS 등)이다.
- **oq-014** (상태: 열림 · 부분 근거 2026-10-10 · 실행 2026-10-10-01) 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가? FaMe는 BPMN 협업 다이어그램을 각 로봇에서 ROS 2 위에 실행하는 공개 구현으로, 신호 이벤트의 type 속성에 ROS 메시지 형을 지정해 BPMN 이벤트와 ROS 메시지를 잇는다. [사실][^ref-1423] 그러나 Open-RMF 작업 상태나 VDA 5050 동작 상태와 BPMN 단계 상태 사이의 표준 매핑으로 볼 근거는 확인하지 못했으므로 이 질문은 열린 상태로 두는 것이 맞다는 것이 이 위키의 판단이다. [의견][^ref-1423][^ref-031][^ref-404]

새로 올린 질문(번호는 [열린 질문](../../open-questions.md) 목록에서 부여한다):

- (상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-01) 로봇이 이미 하역한 뒤 작업이 취소되면, 로봇 쪽 정리 단계 완료와 업무상 인수 취소(재고 반영 취소)를 어떤 완료 조건으로 나눠야 하는가? (24. 작업·워크플로 모델링, 32. 예외 복구·재계획·업무 연속성과 관련)
- (상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-01) Open-RMF rmf_task_sequence의 Bundle 이벤트와 BPMN 병렬 게이트웨이 합류의 의미 차이를 자동으로 검사하거나 변환하는 공개 도구가 있는가? (24. 작업·워크플로 모델링, 54. 시험·형식 검증·벤치마크와 관련)
- (상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-01) 운영 정책 버전이 바뀔 때 이미 시작한 워크플로 인스턴스가 이전 정책을 유지하는지 새 정책으로 옮기는지에 대한 공개 운영 기준이 있는가? (24. 작업·워크플로 모델링, 57. 자산·소프트웨어 수명주기 관리와 관련)

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md)
- 관련 영역: [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-10-10
[^ref-049]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg, 접근일 2026-10-10
[^ref-1423]: University of Camerino PROS Lab, FaMe — A BPMN-driven Framework for Multi-Robot System Development (공식 페이지·사용 지침), 2022-05-03, https://pros.unicam.it/fame/, 접근일 2026-10-10
[^ref-404]: Open Robotics (open-rmf), rmf_task — README, 미확인, https://github.com/open-rmf/rmf_task, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-01 | 24. 작업·워크플로 모델링 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-10-01/pages/topics/2026/2026-10-10-area24-s6.md

```markdown
---
title: "24. 작업·워크플로 모델링 — 대표 접근법과 기술"
type: topic
category: "G. 계획·최적화"
primary_area_no: 24
related_areas: [17, 20, 23, 26, 29, 32, 38, 39, 54, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-110, ref-112, ref-117, ref-121, ref-1423, ref-366, ref-404, ref-502]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-and-workflow-modeling.md#6
---

[홈](../../index.md) › [주제](../index.md) › 24. 작업·워크플로 모델링 — 대표 접근법과 기술

# 24. 작업·워크플로 모델링 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 위키는 이 영역의 관련 접근법을 업무 프로세스 표기(BPMN), 제조 운영 표준의 세그먼트 의존(ISA-95·B2MML), 로봇 오케스트레이션의 작업 단계 구성(Open-RMF), 형식적 설계 점검(워크플로 넷)의 네 갈래로 정리한다. [의견][^ref-112][^ref-117][^ref-110][^ref-121]
- 이 페이지는 [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 위키는 이 영역의 관련 접근법을 업무 프로세스 표기(BPMN), 제조 운영 표준의 세그먼트 의존(ISA-95·B2MML), 로봇 오케스트레이션의 작업 단계 구성(Open-RMF), 형식적 설계 점검(워크플로 넷)의 네 갈래로 정리한다. [의견][^ref-112][^ref-117][^ref-110][^ref-121]

### 2026-10-10 보강: BPMN 규범 근거, 취소 후 정리, Open-RMF 단계 구성

이전 정리(2026-09-25)는 [24. 작업·워크플로 모델링 — 대표 접근법과 기술](2026-09-25-area02-s6.md)에 있다.

BPMN 2.0.2 규범 문서(OMG formal/13-12-09, 2014-01 발행)는 외부 참여자의 메시지가 도착하면 완료되는 수신 작업(Receive Task), 메시지를 프로세스 인스턴스에 연결하는 상관 키(CorrelationKey), 지연·시간 조건을 표현하는 타이머 이벤트(Timer Event)를 정의한다. [사실][^ref-502] 따라서 운반 뒤 인수 확인 메시지를 기다리고 시간 초과 시 분기하는 구조는 특정 벤더 엔진에 한정되지 않고 BPMN 규범 요소로 표현할 수 있지만, 로봇 작업 식별자나 화물 식별자를 어떤 상관 키로 쓸지는 구현에서 정해야 하는 것으로 보인다. [추정][^ref-502][^ref-1423] 이전 정리의 기존 Camunda 근거 문장이 서술한 엔진 고유 동작은 BPMN 표준이 보장하는 것으로 넓히지 않으며, 이 구조를 로봇 인수 확인에 적용한 사례는 확인하지 못했다.

#### 취소와 보상의 구분

Open-RMF rmf_task의 작업 인터페이스(Task.hpp) 주석은 취소 뒤에도 작업이 로봇을 짐 없는 상태로 되돌리기 위한 단계를 계속 수행할 수 있고(남은 대기 단계가 그런 단계로 바뀔 수 있다), 완료 콜백이 호출되어야 취소가 끝난다고 설명한다(2026-10-10 확인). [사실][^ref-366] BPMN 2.0.2는 이미 성공적으로 끝난 단계의 효과를 되돌리는 보상(Compensation)을 별도 개념으로 정의한다. [사실][^ref-502] 두 자료가 같은 상태 체계를 공유한다는 뜻은 아니지만, 워크플로에서 취소 요청과 취소 후 정리 완료를 서로 다른 상태로 나누고 실제 물건의 이동을 되돌릴 수 있는지에 따라 보상 단계를 따로 정의하는 편이 좋다는 것이 이 위키의 판단이다. [의견][^ref-502][^ref-366] 복구 절차 자체는 [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)에서 다루고, 이 영역은 워크플로의 취소·완료 상태 구분으로 한정한다.

#### Open-RMF rmf_task_sequence의 단계·이벤트

rmf_task README에 따르면 rmf_task_sequence의 작업은 순서대로 실행할 단계(Phase)의 연쇄이고 각 단계는 이벤트(Event)들로 구성되며, 작업 모델은 rmf_task_sequence에, 실제 로봇 명령 구현은 rmf_fleet_adapter에 둔다. [사실][^ref-404] 같은 README는 현재 기본 제공 이벤트로 Bundle, DropOff, GoToPlace, PerformAction, PickUp, Placeholder, WaitFor 일곱 가지를 든다(2026-10-10 확인). [사실][^ref-404] 이 기본 이벤트 목록과 단계 연쇄 구조만으로는 rmf_task_sequence를 임의의 업무 병렬 분기·합류를 실행하는 범용 BPMN 엔진으로 보기 어려워 보인다(Bundle 이벤트의 병렬·합류 의미는 원문 미확인). [추정][^ref-502][^ref-404]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md)
- 관련 영역: [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-110]: Open Robotics, Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-25
[^ref-112]: OMG(Object Management Group), About the Business Process Model And Notation Specification Version 2.0, 미확인, https://www.omg.org/spec/BPMN/2.0/About-BPMN, 접근일 2026-09-25 (원문 미열람)
[^ref-117]: MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd, 접근일 2026-09-25
[^ref-121]: Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022), The complexity of soundness in workflow nets, 2022, https://arxiv.org/abs/2201.05588, 접근일 2026-09-25 (원문 미열람)
[^ref-1423]: University of Camerino PROS Lab, FaMe — A BPMN-driven Framework for Multi-Robot System Development (공식 페이지·사용 지침), 2022-05-03, https://pros.unicam.it/fame/, 접근일 2026-10-10
[^ref-366]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/Task.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp, 접근일 2026-10-10
[^ref-404]: Open Robotics (open-rmf), rmf_task — README, 미확인, https://github.com/open-rmf/rmf_task, 접근일 2026-10-10
[^ref-502]: OMG(Object Management Group), Business Process Model and Notation (BPMN), Version 2.0.2, 2014-01, https://www.omg.org/spec/BPMN/2.0.2/, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-01 | 24. 작업·워크플로 모델링 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-10-01/pages/topics/2026/2026-10-10-area24-s3.md

```markdown
---
title: "24. 작업·워크플로 모델링 — 왜 중요한가"
type: topic
category: "G. 계획·최적화"
primary_area_no: 24
related_areas: [17, 20, 23, 26, 29, 32, 38, 39, 54, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-031, ref-044, ref-049, ref-123, ref-124]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-and-workflow-modeling.md#3
---

[홈](../../index.md) › [주제](../index.md) › 24. 작업·워크플로 모델링 — 왜 중요한가

# 24. 작업·워크플로 모델링 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇 관제 규격의 하역 완료와 업무 어휘의 인수·재고 반영은 서로 다른 원문이 각각 정의한다(2026-10-10 확인). [사실][^ref-044][^ref-031][^ref-049]
- 이 페이지는 [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇 관제 규격의 하역 완료와 업무 어휘의 인수·재고 반영은 서로 다른 원문이 각각 정의한다(2026-10-10 확인). [사실][^ref-044][^ref-031][^ref-049]

- GS1 핵심 업무 어휘(Core Business Vocabulary, CBV) 2.0 온톨로지(2021-09-30 판)는 arriving을 물체가 어떤 위치에 도착하는 활동, accepting을 점유나 소유가 바뀌는 활동, receiving을 위치에서 수령되어 수령자 재고에 더해지는 활동으로 구분하고, receiving을 쓰는 것은 arriving·accepting을 쓰는 것과 상호 배타적이라고 적는다. [사실][^ref-044]
- VDA 5050 명세의 3.0.0 태그판(main 브랜치 판과 다를 수 있다)은 미리 정의된 drop 동작의 완료(FINISHED) 상태를, 하역이 끝나 적재물이 이동로봇을 떠나고 로봇이 새 적재 상태를 보고한 때로 정의한다(§6.2.3.2 표 5). [사실][^ref-031]
- Open-RMF의 하역 워크셀 결과 메시지 IngestorResult는 기본 정의 필드로 시각·요청 id·워크셀 id·상태(ACKNOWLEDGED·SUCCESS·FAILED)를 두며, 이 기본 필드에는 수령자 재고 편입 여부를 나타내는 항목이 없다(워크셀별 추가 필드 자리는 열려 있다). [사실][^ref-049]

세 정의를 대조하면, 로봇의 하역 완료(drop 완료, IngestorResult SUCCESS)를 특정 CBV 업무 단계와 자동으로 같다고 보지 말고 해당 업무의 인수·재고 확정 조건을 별도 완료 조건으로 모델링하는 편이 타당하다는 것이 이 위키의 판단이다(이 구성을 적용한 표준·사례는 확인하지 못했다). [의견][^ref-044][^ref-031][^ref-049] 수령자 재고 편입(CBV receiving)과 재고 확정은 연계 대상: 상위 업무 시스템(창고 관리 시스템(Warehouse Management System, WMS) 등)이고, ROP 몫은 두 완료 조건의 구분과 인수 확인 대기·분기로 한정된다는 것도 이 위키의 판단이다. [의견][^ref-044] 작업 대상의 인계 기록은 [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)과 이어진다.

공급망 참조 모델도 업무 완료를 로봇 동작이 아니라 인수 시점에 둔다. ASCM SCOR 모델의 B2C 이행(F1)은 F1.3 Pick Product 같은 단계를 거쳐 마지막 단계인 F1.11 Obtain Proof of Delivery or Customer Acceptance(배송 증빙 또는 고객 인수 확보)로 끝난다(2026-09-25 확인). [사실][^ref-123]

국내 제도도 물류센터를 처리 과정 단위로 나누어 본다. 국토교통부 스마트물류센터 인증은 입고·보관·피킹·출고 등 물류처리 과정별 첨단·자동화 정도를 보는 기능영역과, 시설의 구조적 성능·정보시스템 도입 수준 등을 보는 기반영역으로 평가해 1~5등급을 부여한다(2026-09-25 확인). [사실][^ref-124]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md)
- 관련 영역: [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-10-10
[^ref-049]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg, 접근일 2026-10-10
[^ref-123]: ASCM, SCOR Model — Fulfill F1.3 Pick Product, 미확인, https://scor.ascm.org/processes/fulfill/F1.3, 접근일 2026-09-25 (원문 미열람)
[^ref-124]: 국가물류통합정보센터(국토교통부), 스마트물류센터 인증제 안내, 미확인, https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-01 | 24. 작업·워크플로 모델링 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-10-10-01/pages/topics/2026/2026-10-10-area24-s7.md

```markdown
---
title: "24. 작업·워크플로 모델링 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "G. 계획·최적화"
primary_area_no: 24
related_areas: [17, 20, 23, 26, 29, 32, 38, 39, 54, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-031, ref-1423, ref-1424, ref-1425, ref-366, ref-404, ref-502]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-and-workflow-modeling.md#7
---

[홈](../../index.md) › [주제](../index.md) › 24. 작업·워크플로 모델링 — 관련 표준·프레임워크·오픈소스

# 24. 작업·워크플로 모델링 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역과 관련된 표준·오픈소스는 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역과 관련된 표준·오픈소스는 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

### 2026-10-10 보강: 규범판·판 차이·패키지 변경

이전 정리(2026-09-25)는 [24. 작업·워크플로 모델링 — 관련 표준·프레임워크·오픈소스](2026-09-25-area02-s7.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| BPMN 2.0.2 (OMG formal/13-12-09, 2014-01) | 표준 | 수신 작업·상관 키·타이머 이벤트·보상을 규범으로 정의해 인수 확인 대기와 취소 후 처리 표현의 근거가 된다 | [사실][^ref-502] |
| VDA 5050 3.0.0 태그판 | 표준 | 동작의 blockingType으로 주행과 다른 동작의 병행 가능 여부를 정한다 | [사실][^ref-031] |
| Open-RMF rmf_task (rmf_task_sequence) | 오픈소스 | 작업을 단계·이벤트의 연쇄로 구성한다 | [사실][^ref-404] |
| Open-RMF rmf_fleet_adapter (rmf_ros2, 패키지 2.14.0) | 오픈소스 | rmf_task_sequence 작업의 실제 로봇 명령 구현을 맡는다 | [사실][^ref-404][^ref-1424] |
| FaMe | 프레임워크 | BPMN 협업 다이어그램을 각 로봇에서 ROS 2 위에 실행한다 | [사실][^ref-1423] |

VDA 5050 명세 3.0.0 태그판(main 브랜치 판과 다를 수 있음, 2026-10-10 확인)은 동작의 blockingType을 NONE·SINGLE·SOFT·HARD 네 값으로 두며, SINGLE은 주행은 허용하되 다른 동작의 병렬 실행은 허용하지 않고 HARD는 그 시점에 허용되는 유일한 동작이다. [사실][^ref-031] 2.1.0 태그판 명세의 blockingType은 NONE·SOFT·HARD 세 값이어서, SINGLE은 2.1.0 명세에는 없고 3.0.0 명세에는 있다(두 판 사이의 다른 판은 확인하지 않았고, 같은 발행 계열 두 판의 대조라 교차 확인이 아니다). [사실][^ref-031][^ref-1425] 공정 모델에서 주행과 작업 활동의 동시 수행 가능성을 제약으로 표현할 때는 SINGLE과 HARD를 구별해 다루는 편이 좋다는 것이 이 위키의 판단이다. [의견][^ref-031] blockingType은 [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 쪽 인터페이스 정의이며, 이 영역에서는 공정 모델의 병행 제약 근거로만 쓴다.

개별 패키지 rmf_fleet_adapter 2.14.0(2026-09-26)의 변경 이력에는 단계 건너뛰기 요청의 키를 고친 항목(#543)이 있다. 이 버전은 Open-RMF 배포판 버전이 아니며, 고친 키의 이름은 미확인이다. [사실][^ref-1424] 단계 건너뛰기를 운영 정책에 넣는 구현은 rmf_fleet_adapter 패키지 버전과 건너뛰기 요청 스키마를 함께 기록해 두는 편이 좋다는 것이 이 위키의 판단이다. [의견][^ref-1424][^ref-366]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md)
- 관련 영역: [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-1423]: University of Camerino PROS Lab, FaMe — A BPMN-driven Framework for Multi-Robot System Development (공식 페이지·사용 지침), 2022-05-03, https://pros.unicam.it/fame/, 접근일 2026-10-10
[^ref-1424]: Open Robotics (open-rmf), rmf_ros2 (tag 2.14.0) — rmf_fleet_adapter/CHANGELOG.rst, 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-10
[^ref-1425]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 (tag 2.1.0) — VDA5050_EN.md, 미확인, https://github.com/VDA5050/VDA5050/blob/2.1.0/VDA5050_EN.md, 접근일 2026-10-10
[^ref-366]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/Task.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp, 접근일 2026-10-10
[^ref-404]: Open Robotics (open-rmf), rmf_task — README, 미확인, https://github.com/open-rmf/rmf_task, 접근일 2026-10-10
[^ref-502]: OMG(Object Management Group), Business Process Model and Notation (BPMN), Version 2.0.2, 2014-01, https://www.omg.org/spec/BPMN/2.0.2/, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-01 | 24. 작업·워크플로 모델링 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-10-01/pages/topics/2026/2026-10-10-area24-s8.md

```markdown
---
title: "24. 작업·워크플로 모델링 — 대표 연구와 자료"
type: topic
category: "G. 계획·최적화"
primary_area_no: 24
related_areas: [17, 20, 23, 26, 29, 32, 38, 39, 54, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-116, ref-1423]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-and-workflow-modeling.md#8
---

[홈](../../index.md) › [주제](../index.md) › 24. 작업·워크플로 모델링 — 대표 연구와 자료

# 24. 작업·워크플로 모델링 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇 작업을 업무 프로세스 형식으로 기술·실행하고 그 실행 기록을 분석하는 연구가 대표 자료다.
- 이 페이지는 [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇 작업을 업무 프로세스 형식으로 기술·실행하고 그 실행 기록을 분석하는 연구가 대표 자료다.

### 2026-10-10 보강

이전 정리(2026-09-25)는 [24. 작업·워크플로 모델링 — 대표 연구와 자료](2026-09-25-area02-s8.md)에 있다.

- Filippone·Pettinari·Pelliccione, Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis(arXiv 2603.15427, v1 2026-03-16, v2 2026-08-17, IEEE Transactions on Software Engineering (2026) 게재 정보) — 행동 트리·상태 기계·계층적 작업 네트워크(Hierarchical Task Network, HTN)·BPMN을 제어 구조, 임무 개념 표현(표현력), 도구 지원 기준으로 비교한다. [사실][^ref-116] 2026년 1월 4주 동안 83명에게 설문을 요청해 29개 완성 응답(응답률 34.94%)을 받고 일부 참여자와 후속 인터뷰(실시간 3명, 서면 1명)를 했으며, 같은 로봇 현장에서 형식별 처리량을 측정한 성능 비교가 아니라 분석 비교를 전문가 설문으로 검증한 연구다. [사실][^ref-116] 따라서 임무 기술 형식 선택의 검토 자료로 쓰되, 특정 형식이 항상 우수하다는 결론으로 옮기지 않는 편이 좋다는 것이 이 위키의 판단이다. [의견][^ref-116]
- University of Camerino PROS Lab, FaMe 공식 페이지·사용 지침(2022-05-03 게시) — BPMN 협업 다이어그램으로 다중 로봇 임무를 정의하고 모델링·구성·실행 단계를 거쳐 각 로봇에서 ROS 2 위에 그 협업을 직접 실행하는 공개 프레임워크이며, 구성 단계에서 신호 이벤트의 type 속성에 ROS 메시지 형을 지정해 BPMN 이벤트와 ROS 메시지를 잇는다. [사실][^ref-1423]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md)
- 관련 영역: [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-and-workflow-modeling.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03-16, https://arxiv.org/abs/2603.15427, 접근일 2026-10-10
[^ref-1423]: University of Camerino PROS Lab, FaMe — A BPMN-driven Framework for Multi-Robot System Development (공식 페이지·사용 지침), 2022-05-03, https://pros.unicam.it/fame/, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-01 | 24. 작업·워크플로 모델링 의 "대표 연구와 자료" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 16건 / 전체 1401건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 2026-09-25 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 2026-09-25 | 예 |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg | 2026-09-25 | 예 |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/task_new.html | 2026-09-25 | 예 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 2026-09-25 | 예 |
| ref-112 | OMG(Object Management Group) | About the Business Process Model And Notation Specification Version 2.0 | 미확인 | https://www.omg.org/spec/BPMN/2.0/About-BPMN | 2026-09-25 | 아니오 |
| ref-113 | Camunda | Messages | Camunda 8 Docs (camunda-docs: docs/components/concepts/messages.md) | 미확인 | https://docs.camunda.io/docs/components/concepts/messages/ | 2026-09-25 | 예 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | https://arxiv.org/abs/2603.15427 | 2026-09-25 | 아니오 |
| ref-117 | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 2023 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd | 2026-09-25 | 예 |
| ref-118 | MESA International | B2MML-BatchML — Schema/B2MML-OperationsDefinition.xsd | 미확인 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-OperationsDefinition.xsd | 2026-09-25 | 예 |
| ref-119 | IEC / ISO | IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management | 2016 | https://www.iso.org/standard/67480.html | 2026-09-25 | 아니오 |
| ref-120 | Boniardi, F., Valada, A., Mohan, R., Caselitz, T., & Burgard, W. | Robot Localization in Floor Plans Using a Room Layout Edge Extraction Network | 2019-03 | https://arxiv.org/abs/1903.01804 | 2026-09-25 | 아니오 |
| ref-121 | Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022) | The complexity of soundness in workflow nets | 2022 | https://arxiv.org/abs/2201.05588 | 2026-09-25 | 아니오 |
| ref-123 | ASCM | SCOR Model — Fulfill F1.3 Pick Product | 미확인 | https://scor.ascm.org/processes/fulfill/F1.3 | 2026-09-25 | 아니오 |
| ref-124 | 국가물류통합정보센터(국토교통부) | 스마트물류센터 인증제 안내 | 미확인 | https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW | 2026-09-25 | 아니오 |
```

### docs/glossary/index.md (요약: 용어 396개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- 4d-scene-graph: 4차원 장면 그래프 (4D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- abstract-and-concrete-scenario: 추상 시나리오·구체 시나리오 (Abstract Scenario / Concrete Scenario)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- action-status: 동작 상태 (Action Status (VDA 5050 actionStatus))
- actively-exploited-vulnerability: 적극 악용 취약점 (Actively Exploited Vulnerability (EU Cyber Resilience Act))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alarm-management: 경보 관리 (Alarm Management (ANSI/ISA 18.2))
- alert-tier: 경보 등급 (Alert Tier (Open-RMF Alert))
- almere-model: 알메러 모델 (Almere Model)
- alternative-name: 대체 이름 (Alternative Name (IMDF alt_name))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- api-deprecation-policy: API 폐기 정책 (API Deprecation Policy)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- as-planned-vs-as-built-deviation: 설계–준공 편차 (As-planned vs As-built Deviation)
- asam-openscenario: 오픈시나리오 (ASAM OpenSCENARIO)
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- asyncapi-specification: AsyncAPI 명세 (AsyncAPI Specification)
- attribute-based-access-control: 속성 기반 접근 통제 (Attribute-Based Access Control (ABAC))
- audit-trail: 감사 추적 (Audit Trail)
- automatic-recording-of-events: 자동 사건 기록 (Automatic Recording of Events (Logs, EU AI Act Article 12))
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- average-displacement-error: 평균 변위 오차 (Average Displacement Error (ADE))
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-domain-definition-language: 행동 영역 정의 언어 (Behavior Domain Definition Language (BDDL))
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- brainless-robot: 브레인리스 로봇 (Brainless Robot)
- building-element-proxy: 건물 요소 프록시 (Building Element Proxy (IfcBuildingElementProxy))
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
- buildingsmart-data-dictionary: buildingSMART 데이터 사전 (buildingSMART Data Dictionary (bSDD))
- business-continuity-management-system: 업무 연속성 관리 시스템 (Business Continuity Management System (BCMS))
- business-location: 업무 위치 (Business Location (EPCIS bizLocation))
- cap-theorem: CAP 정리 (CAP Theorem)
- capabilities-skills-services: 능력·스킬·서비스 모델 (Capabilities, Skills and Services (CSS) Model)
- capability-based-task-allocation: 능력 기반 작업 배정 (Capability-based Task Allocation)
- capability-description-submodel: 능력 기술 서브모델 (Capability Description Submodel (IDTA 02020))
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- cell-based-production: 셀 생산 방식 (Cell-based Production)
- clarification-question: 명확화 질문 (Clarification Question (Follow-up Clarification))
- cloud-robotics: 클라우드 로보틱스 (Cloud Robotics)
- coalition-formation: 연합 형성 (Coalition Formation)
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- common-coordinate-system: 공통 좌표계 (Common Coordinate System (CCS, ISO 21423))
- common-data-environment: 공통 데이터 환경 (Common Data Environment (CDE))
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
- competency-question: 역량 질문 (Competency Question (CQ))
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM))
- configuration-copilot: 구성 코파일럿 (Configuration Copilot)
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformal-prediction: 등각 예측 (Conformal Prediction)
- conformance-test: 적합성 시험 (Conformance Test)
- confused-deputy: 혼란된 대리인 (Confused Deputy)
- connection-state: 연결 상태 (Connection State (VDA 5050 connectionState))
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- constrained-decoding: 제약 디코딩 (Constrained Decoding)
- contrastive-explanation: 대조적 설명 (Contrastive Explanation)
- control-barrier-function: 제어 장벽 함수 (Control Barrier Function (CBF))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD))
- costmap: 비용 지도 (Costmap)
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-embodiment-learning: 교차 형태 학습 (Cross-embodiment Learning)
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- curb-cut: 연석 경사로 (Curb Cut (Curb Ramp))
- cyber-resilience-act: 사이버복원력법 (Cyber Resilience Act (CRA))
- data-holder: 데이터 보유자 (Data Holder (EU Data Act))
- data-provenance: 데이터 출처 추적 (Data Provenance (W3C PROV))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- decision-focused-learning: 결정 중심 학습 (Decision-Focused Learning)
- digital-nameplate: 디지털 명판 (Digital Nameplate (IDTA 02006))
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- document-layout-analysis: 문서 레이아웃 분석 (Document Layout Analysis)
- domain-shift: 도메인 이동 (Domain Shift)
- door-to-door-robot-delivery: 도어 투 도어 로봇 배송 (Door-to-Door Robot Delivery)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- dual-system-architecture: 이중 시스템 구조 (Dual-system Architecture (System 1 / System 2))
- eclass: ECLASS (ECLASS)
- edit-cost: 편집 비용 (Edit Cost)
- elevator-operating-rate: 승강기 가동률 (Elevator Operating Rate (EOR))
- empanelment-programme: 등재 프로그램 (Empanelment Programme)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- ethical-black-box: 윤리적 블랙박스 (Ethical Black Box (EBB))
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explainable-mapf: 설명 가능한 다중 에이전트 경로 찾기 (Explainable Multi-Agent Path Finding (Explainable MAPF))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
- face-obfuscation: 얼굴 가림 (Face Obfuscation)
- failure-explanation: 실패 설명 (Failure Explanation)
- falsification: 반증 기반 시험 (Falsification)
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- filter-mask: 필터 마스크 (Filter Mask (Nav2 costmap filter))
- finops: 핀옵스 (FinOps)
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- frozen-horizon: 동결 구간 (Frozen Horizon (Frozen Zone))
- generalized-voronoi-graph: 일반화 보로노이 그래프 (Generalized Voronoi Graph (GVG))
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- gln-extension-component: GLN 확장 성분 (GLN Extension Component)
- goal-condition: 목표 조건 (Goal Condition)
- goods-to-person: 상품-대-사람 (Goods-to-Person (GTP))
- grade-certainty-of-evidence: 근거 확실성 등급 (GRADE (Grading of Recommendations, Assessment, Development and Evaluation))
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- graph-edit-distance: 그래프 편집 거리 (Graph Edit Distance (GED))
- guidance-graph: 안내 그래프 (Guidance Graph)
- hallucination: 환각 (Hallucination)
- hardware-in-the-loop: 하드웨어 인 더 루프 (Hardware-in-the-Loop (HiL))
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- hmi-philosophy: HMI 철학 (HMI Philosophy (ISA-TR101.01))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- human-motion-trajectory-prediction: 사람 움직임 궤적 예측 (Human Motion Trajectory Prediction)
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- i-pass-handoff-program: I-PASS 인계 프로그램 (I-PASS Handoff Program)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- imitation-learning: 모방 학습 (Imitation Learning)
- indirect-prompt-injection: 간접 프롬프트 주입 (Indirect Prompt Injection)
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- industrial-data: 산업데이터 (Industrial Data)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- infrastructure-mounted-sensing: 인프라 장착 센서 (Infrastructure-mounted Sensing)
- integrity-risk: 무결성 위험 (Integrity Risk)
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- irreducible-infeasible-subset: 기약 불능 제약 집합 (Irreducible Infeasible Subset (IIS))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- it-ot-convergence: IT/OT 융합 (IT/OT Convergence)
- jailbreak: 탈옥 (Jailbreak)
- job-shop-scheduling-problem: 작업장 스케줄링 문제 (Job Shop Scheduling Problem (JSSP))
- joint-goal-accuracy: 결합 목표 정확도 (Joint Goal Accuracy (JGA))
- json-schema: JSON 스키마 (JSON Schema)
- keystroke-level-model: 키 입력 수준 모델 (Keystroke-Level Model (KLM))
- kiosk-accessibility: 무인정보단말기 접근성 (Kiosk Accessibility (Unmanned Information Terminal Accessibility))
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lease-expiry: 허가 만료 시각 (Lease Expiry (VDA 5050 leaseExpiry))
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- life-cycle-costing: 수명주기 비용 분석 (Life Cycle Costing (LCC, IEC 60300-3-3))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic-on-finite-traces: 유한 트레이스 선형 시간 논리 (Linear Temporal Logic on Finite Traces (LTLf))
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- localization-score: 위치추정 품질 점수 (Localization Score (VDA 5050 localizationScore))
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- management-of-change: 변경 관리 (Management of Change (MOC))
- map-alignment: 지도 정합 (Map Alignment)
- map-distribution: 지도 배포 (Map Distribution (VDA 5050 downloadMap / enableMap / deleteMap))
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- maps-of-dynamics: 움직임 지도 (Maps of Dynamics (MoD))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
- mcap: MCAP (MCAP)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mission-specification-pattern: 미션 명세 패턴 (Mission Specification Pattern)
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))
- model-contractual-terms: 모델 계약 조항 (Model Contractual Terms (MCTs))
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- models-and-simulations-credibility-assessment: 모델·시뮬레이션 신뢰도 평가 (Models and Simulations Credibility Assessment (NASA-STD-7009))
- mqtt-last-will: MQTT 유언 메시지 (MQTT Last Will (Will Message))
- mqtt-quality-of-service-level: MQTT 서비스 품질 수준 (MQTT Quality of Service (QoS) Level)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- oauth2-client-credentials-grant: 클라이언트 자격 증명 흐름 (OAuth 2.0 Client Credentials Grant (Machine-to-Machine))
- observability: 관측성 (Observability)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- online-simulation: 온라인 시뮬레이션 (Online Simulation)
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
- opentelemetry: 오픈텔레메트리 (OpenTelemetry (OTel))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- operational-state: 운용 상태 (Operational State (MassRobotics statusReport operationalState))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- original-instructions: 원본 설명서 (Original Instructions)
- outdoor-mobile-robot-operational-safety-certification: 실외이동로봇 운행안전인증 (Outdoor Mobile Robot Operational Safety Certification)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pay-per-pick: 피킹량 기반 과금 (Pay-per-pick)
- payback-period: 투자 회수 기간 (Payback Period)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- persistence-filter: 지속성 필터 (Persistence Filter)
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- phased-rollout: 단계적 배포 (Phased Rollout (Staged Rollout))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- post-occupancy-evaluation: 사용 후 평가 (Post-Occupancy Evaluation (POE))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- precision-time-protocol: 정밀 시간 프로토콜 (Precision Time Protocol (PTP))
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- presumption-of-conformity: 적합성 추정 (Presumption of Conformity)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- product-liability: 제조물책임 (Product Liability)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
- pseudonymisation: 가명처리 (Pseudonymisation)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- raw-video-regulatory-sandbox-exemption: 영상정보 원본 활용 규제샌드박스 실증특례 (Regulatory Sandbox Special Demonstration Exemption for Raw Video Use)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- remote-attestation: 원격 증명 (Remote Attestation)
- remote-controlled-small-vehicle: 원격 조작형 소형차 (Remote-controlled Small Vehicle (遠隔操作型小型車))
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robot-as-a-service: 서비스형 로봇 (Robot-as-a-Service (RaaS))
- robot-density: 로봇 밀도 (Robot Density)
- robot-foundation-model: 로봇 기반 모델 (Robot Foundation Model)
- robot-friendly-building-certification: 로봇 친화형 건축물 인증 (Robot-Friendly Building Certification)
- robot-standard-process-model: 로봇활용 표준공정모델 (Robot Standard Process Model (Korea))
- robot-task-fitness-matrix: 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)
- robotic-middleware-for-healthcare: 의료 로봇 미들웨어 RoMi-H (Robotic Middleware for Healthcare (RoMi-H))
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- role-ambiguity: 역할 모호성 (Role Ambiguity)
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-tracing: 런타임 추적 (Runtime Tracing (ros2_tracing))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- safety-guardrail: 안전 가드레일 (Safety Guardrail (LLM-enabled robots))
- safety-state-report: 안전 상태 보고 (Safety State (VDA 5050 safetyState))
- saga: 사가 (Saga)
- scan-vs-bim: 스캔 대 BIM 비교 (Scan-vs-BIM)
- scenario-reconstruction: 시나리오 재구성 (Scenario Reconstruction)
- schedule-stability: 일정 안정성 (Schedule Stability)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- security-level-iec-62443: 보안 수준 (Security Level (SL, IEC 62443))
- self-driving-laboratory: 자율 실험실 (Self-driving Laboratory (Autonomous Laboratory))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-map: 의미 지도 (Semantic Map)
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- service-triad: 서비스 삼자 관계 (Service Triad (service robot, customer, frontline employee))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shift-handover: 교대 인수인계 (Shift Handover)
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- sila-2: SiLA 2 (Standardization in Lab Automation 2 (SiLA 2))
- sim-vs-real-correlation-coefficient: 시뮬레이션–현실 상관 계수 (Sim-vs-Real Correlation Coefficient (SRCC))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- simulation-description-format: 시뮬레이션 기술 형식 (Simulation Description Format (SDFormat))
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-awareness: 상황 인식 (Situation Awareness (SA))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- skos: 단순 지식 조직 체계 (Simple Knowledge Organization System (SKOS))
- slot-filling: 슬롯 채우기 (Slot Filling)
- slotcar: 슬롯카 모델 (Slotcar (Open-RMF simulated robot plugin))
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- social-force-model: 사회적 힘 모델 (Social Force Model)
- social-robot-navigation: 사회적 내비게이션 (Social Robot Navigation (Human-aware Navigation))
- soft-landings: 소프트 랜딩 (Soft Landings (BSRIA BG 54))
- software-bill-of-materials: 소프트웨어 자재명세서 (Software Bill of Materials (SBOM))
- software-in-the-loop: 소프트웨어 인 더 루프 (Software-in-the-Loop (SiL))
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- source-grounding: 출처 근거 연결 (Source Grounding)
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
- space-graph: 공간 그래프 (Space Graph)
- speed-and-separation-monitoring: 속도·분리 감시 (Speed and Separation Monitoring (SSM))
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- stakeholder-requirements-specification: 이해관계자 요구사항 명세 (Stakeholder Requirements Specification (StRS))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- state-script: 상태 스크립트 (State Script (Mender))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- strict-schema: 엄격 스키마 (Strict Schema (deprecated elements removed))
- stride-threat-classification: STRIDE 위협 분류 (STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege))
- structured-output: 구조화 출력 (Structured Output)
- substantial-modification: 실질적 변경 (Substantial Modification)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- surrogate-model: 대리 모델 (Surrogate Model)
- synchronization-loss: 동기화 손실 (Synchronization Loss)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
- tamper-evident-log: 변조 탐지 로그 (Tamper-evident Log)
- task-decomposition: 작업 분해 (Task Decomposition)
- task-dependency-graph: 작업 의존 그래프 (Task Dependency Graph (Dependency DAG))
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- total-cost-of-ownership: 총소유비용 (Total Cost of Ownership (TCO))
- trace-context: 추적 문맥 (Trace Context (W3C traceparent / tracestate))
- transparency-level-ieee-7001: 자율 시스템 투명성 수준 (Transparency Level (IEEE 7001-2021))
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
- user-defined-property-set: 사용자 정의 속성 세트 (User-defined Property Set)
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- utaut: 통합 기술 수용 이론 (Unified Theory of Acceptance and Use of Technology (UTAUT))
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050-hibernation: 절전 모드 (Hibernation (VDA 5050 startHibernation / HIBERNATING))
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- wireless-safety-rated-emergency-stop: 무선 안전 비상정지 (Wireless Safety-rated Emergency Stop)
- workflow-diagram: 워크플로 다이어그램 (Workflow Diagram (Open-RMF 상호운용 관심 그룹 제안))
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [24] 에 걸린 6건 / 전체 350건)

```markdown
- oq-012 [열림] 국내 물류센터는 로봇의 운반 완료와 WMS의 입고·인수 확정을 별도 단계로 두는가, 그렇다면 두 단계를 잇는 식별 키와 확정 대기 시간 기준은 무엇인가? (영역 23, 24)
- oq-013 [열림] ISA-95 세그먼트 의존 유형(B2MML DependencyType)을 입고·적치·피킹·출하 같은 창고 물류 작업의 선후관계 표현에 적용한 사례나 확장이 있는가? (영역 24, 26)
- oq-014 [열림] 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가? (영역 20, 24, 29)
- oq-137 [열림] 완료 기한·반복 주기·실패 처리 조건처럼 관제 작업 요청 스키마에 자리가 없는 시나리오 항목을 어느 층(시나리오 모델·워크플로 모델·스케줄러)이 보관하고 실행 시점에 어떻게 작업 요청으로 변환하는가? (영역 9, 24, 26, 20)
- oq-243 [열림] IEC 62559 사용 사례 템플릿이나 ISO/IEC/IEEE 29148 요구 명세 형식을 다중 로봇·로봇 오케스트레이션 사용 사례 정의에 적용한 사례가 있는가? (영역 2, 24)
- oq-345 [열림] 로봇 관제 인터페이스(VDA 5050 주문, Open-RMF 작업 요청)에 작업 사이 의존·대안 경로·기한을 표현하는 확장 제안이나 차기 판 논의가 있는가? (관련 기존 질문: oq-049, oq-137) (영역 20, 21, 24)
```

### runs/2026-10-10-01/verification2.json

```json
{
  "run_id": "2026-10-10-01",
  "stage": "second",
  "verdict": "수정 후 재검증",
  "claim_checks": [],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": []
  },
  "duplication": {
    "ok": false,
    "overlaps": [
      "세부영역 6·7·8·11절이 append 패치 뒤 자동 분리되면서 기존 분리 주제 페이지(2026-09-25-area02-s6·s7·s8·s11)로 가는 '자세한 내용은 주제 페이지 […]에 있다.' 줄이 새 분리 페이지(2026-10-10-area24-s6·s7·s8·s11)에 옮겨지지 않았다. 그래서 기존 페이지의 검증된 내용(6절 Camunda·ISA-95·워크플로 넷 서술과 ref-112·ref-113, 7절 표준 표, 8절 FaMe ref-114 등 연구 목록, 11절 oq-012·oq-013 등)이 세부영역 페이지와 새 분리 페이지 어디에서도 링크되지 않는다",
      "기존 8절 분리 페이지(2026-09-25-area02-s8)의 ref-116 각주(2026-03, 원문 미열람)가 이번에 갱신한 참고문헌 ref-116(2026-03-16, 열람)과 다르다. 스토리텔러가 additional_research_requests 로 다음 갱신에 넘겼다",
      "ref-1423·ref-1424·ref-1425 와 실행 2026-10-09-26 브리프의 다른 출처 id 가 겹치는지 아직 확인하지 않았다(changelog_entry 비고에 남김, 퍼블리셔 확인 필요)"
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true,
    "issues": []
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "세부영역 6·7·8·11절(머리말 제외 각 절 patch, action replace): 이번 갱신으로 기존 분리 주제 페이지로 가는 링크가 사라졌다(1차 지시 '6절 분리 주제 페이지의 기존 Camunda 문장(ref-113)과 ref-112 각주는 지우지 않는다'가 실질적으로 지켜지지 않음). 각 절의 '### 2026-10-10 보강' 소절 첫 줄에 기존 페이지 링크를 둔다. 예: '이전 정리(2026-09-25)는 [24. 작업·워크플로 모델링 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area02-s6.md)에 있다.' 7절은 '— 관련 표준·프레임워크·오픈소스'(2026-09-25-area02-s7.md), 8절은 '— 대표 연구와 자료'(2026-09-25-area02-s8.md), 11절은 '— 열린 질문'(2026-09-25-area02-s11.md)으로 같은 형식을 쓴다. 이 상대 경로는 세부영역 페이지와 docs/topics/2026/ 분리 페이지에서 모두 유효하므로 자동 분리 뒤에도 링크가 남는다.",
    "5절 사례 3 표의 작업 대상 칸: 'BPMN 협업 다이어그램으로 정의한 다중 로봇 임무(정보)'와 f24 문장은 FaMe 프레임워크의 실행 방식에 관한 내용이다. 이 시나리오가 다루는 물건·공간·정보·사람이 아니고, 브리프(f7·f8·f24)에도 이 시나리오의 작업 대상은 나오지 않는다. 작업 대상 칸은 '미확인'으로 두고, f24 문장([사실][^ref-1423])은 표 아래 서술 문단으로 옮긴다. site_matrix_updates 에서 {site_type: 기타, item: 작업 대상} 항목을 빼고, {기타, 수행 자원} 항목은 그대로 둔다.",
    "6절 보강 첫 문단(분리 페이지 2026-10-10-area24-s6)의 'Camunda 문서의 고유 동작(메시지 보존 시간·중복 거부)' 구절은 벤더 기능을 서술하는데 태그·각주가 없다. 기존 각주 [^ref-113]을 붙이고 '벤더 주장'을 병기한다. 또는 구체 동작 이름을 빼고 '기존 Camunda 근거 문장'으로만 가리킨다.",
    "pages.json pages[0].diff_summary 의 '13절 … 새 각주 6건'을 실제 상태로 고친다. 세부영역 13절에 새로 들어간 각주는 ref-1423 1건이고, ref-366·ref-404·ref-502·ref-1424·ref-1425 는 분리 주제 페이지의 출처 절에만 있다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 27건, 미확인 0건, 교차 확인 0건. 강등: 없음(f17 은 표현만 정정: '2.1.0 명세에는 없고 3.0.0 명세에는 있다'). 원문 미열람 출처: 없음. 다만 BPMN 2.0.2 PDF(ref-502)는 1차 검증자 도구로 본문을 추출하지 못해 OMG 사양 페이지와 2차 자료로 대조했다. f5·f11 의 절 번호는 원문으로 확인하지 못했다. 주의: 사실 주장은 모두 단일 출처(표준·오픈소스 원문)다. 이번 리서치는 외부 조사 메모를 변환한 것이어서 한국어 검색과 국내 자료가 없다. 창고 밖 사례는 FaMe 농업·지상 로봇 협업 시뮬레이션(현장 유형 기타) 하나이며 현장 운영 성능 근거가 아니다. oq-001·oq-014 는 부분 근거만 있어 열림을 유지한다. ref-1423~ref-1425 는 실행 2026-10-09-26 의 다른 출처 id 와 겹치는지 퍼블리셔가 확인해야 한다. 정정 요청 없음. 2차: 드리프트 없음(브리프 밖 사실·수치 추가 없음, [의견] 문장마다 '이 위키의 판단' 명시, 범위 경계 '연계 대상: 상위 업무 시스템' 표시 이행). [분류원문] 보존, 섹션 순서 준수. 링크는 대상 경로가 유효하지만 고칠 점이 있다. 자동 분리 과정에서 기존 분리 페이지 2026-09-25-area02-s6·s7·s8·s11 로 가는 링크 줄이 빠져 그 페이지들이 고립됐으므로 링크 복원을 지시했다(분리 코드가 '자세한 내용은 주제 페이지' 줄을 옮기지 않는 듯하다. pipeline 담당 확인 필요). 5절 사례 3 의 작업 대상 칸은 근거가 없어 '미확인'으로 되돌리고 매트릭스 칸을 빼도록 지시했다. 기존 s6·s7·s8 페이지의 ref-116 각주·BPMN 행 보강은 다음 갱신으로 넘겼다. 세부영역 프런트매터 sources 에는 분리 페이지에서만 인용하는 출처(ref-124·ref-366·ref-404·ref-502·ref-1424·ref-1425)가 함께 들어 있다(형식 검증 통과, 참고 사항).",
  "retry_reason": null
}
```
