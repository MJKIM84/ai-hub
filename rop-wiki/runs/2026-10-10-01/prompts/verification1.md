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
- 세부영역 반영 제안: 2건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
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

### data/area_reflection_proposals.json (대상 영역 24. 작업·워크플로 모델링 에 대한 트랙 반영 제안 2건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-09-25-51",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 2,
      "area_no": 24,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "OPC UA for ISA-95 작업 응답의 실제 시작·종료 시각·작업 상태·실적 필드(f7), BPMN 2.0.2 의 사람 수행자·잠재 담당자·자원 배정 식(f9, 원문 미열람), BPMN 기반 다중 로봇 개발 틀 FaMe(f10), Serverless Workflow DSL 의 순차·병렬 작업·시간 초과·일정(f11), 임무 기술 형식 네 가지 비교 연구(f16, 원문 미열람).",
      "status": "제안"
    },
    {
      "run_id": "2026-10-09-25",
      "date": "2026-10-09",
      "track": "chat-based-configuration-and-operation",
      "stage": 2,
      "area_no": 24,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "행동 트리 임무를 VDA 5050 주문으로 옮기는 Isaac Mission Dispatch(f16), PDDL 계획을 행동 트리로 실행하는 PlanSys2(f19), 의존 DAG(DART-LLM, f20), LTLf→행동 트리 변환(f23), 분기·동기화·순환을 표현하는 Open-RMF 진영 워크플로 다이어그램(f24·f25, Open Robotics Discourse 포럼 공지 근거)과 crossflow README(f26, 워크플로 다이어그램의 구현으로 단정하지 않음).",
      "status": "제안"
    }
  ]
}
```

### docs/categories/planning-and-optimization/task-allocation-mrta.md (요약)

```markdown
# 25. 작업 배정 — MRTA

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

작업을 로봇 또는 로봇 팀에 배정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 배정**: 능력·위치·적재량·배터리·기한을 고려해 로봇 또는 로봇 팀에 작업을 배정한다
- **이종 로봇 팀 구성**: 한 작업에 필요한 로봇 조합(운반·팔·순찰 등)을 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 13번 영역 ‘작업 배정 — MRTA’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 [옛 분류원문]

> 옛 질문: 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md (요약)

```markdown
# 26. 작업 순서·스케줄링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

순서·시간 제약·긴급 삽입을 다루고, 계속 들어오는 작업에 맞춰 다시 계획한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 순서·스케줄링**: 작업 묶음, 선후관계, 시간 제약, 작업 간 동기화, 긴급 작업 삽입을 다룬다
- **계속 들어오는 작업의 재계획**: 새 작업과 지연이 계속 생기는 조건에서 계획을 이어서 고친다

이전 분류(2026-09-24)에서 이 페이지는 옛 14번 영역 ‘작업 순서·스케줄링’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 주문 묶음, 작업 선후관계, 시간 제약, 공정 간 동기화, 긴급 작업 삽입 [옛 분류원문]

> 옛 질문: 피킹·운반·포장이 서로 기다리지 않게 어떤 순서로 실행할까? [옛 분류원문]

## 2. 핵심 질문

일이 계속 새로 들어올 때 무엇을 먼저, 언제 할지 어떻게 정할 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md (요약)

```markdown
# 27. 다중 로봇 경로·교통 관리 — MAPF

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

여러 로봇의 경로·통과 시점·우선권을 조율한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **다중 로봇 경로·교통 관리**: 여러 로봇의 경로와 통과 시점을 조율하고 혼잡·교착·우선권을 처리한다
- **이기종 로봇 간 통행 우선권**: 서로 다른 제조사의 로봇이 좁은 통로에서 만날 때 누가 양보할지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 15번 영역 ‘다중 로봇 경로·교통 관리 — MAPF’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 [옛 분류원문]

> 옛 질문: 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [옛 분류원문]

## 2. 핵심 질문

서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [분류원문]
```

### docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md (요약)

```markdown
# 28. 공용 자원·충전·에너지 최적화

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

공용 자원을 예약·배분하고 충전·에너지를 계획한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **공용 자원 예약·배분**: 승강기·작업대·대기 공간·버퍼 같은 공용 자원을 예약하고 나눈다
- **충전·에너지 계획**: 충전 시점·충전기 배정·대기열과 작업별 에너지 예산을 계획한다

이전 분류(2026-09-24)에서 이 페이지는 옛 16번 영역 ‘공용 자원·충전·에너지 최적화’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 [옛 분류원문]

> 옛 질문: 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [옛 분류원문]

## 2. 핵심 질문

로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]
```

### docs/categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md (요약)

```markdown
# 17. 작업 대상·자산 식별과 인계 추적

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 4

## 1. 한 줄 정의

물품·자산·도구 같은 작업 대상의 식별·위치·인계 책임을 추적하고, 사람에게 넘길 때 수령인을 확인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 대상 식별·추적**: 물품·자산·도구·운반구·검체·세탁물처럼 작업 대상의 식별자·위치·적재 관계를 추적한다
- **인계·책임 기록**: 누가 언제 무엇을 넘겨받았는지 관측 근거와 함께 기록한다
- **이벤트 공통 형식**: 상태·위치·이동·인계 이벤트를 공통 형식으로 주고받는다(GS1 EPCIS 등)
- **수령인 확인**: 물건을 사람에게 넘길 때 받는 사람을 PIN·카드·앱으로 확인하고 인계 기록을 남긴다

이전 분류(2026-09-24)에서 이 페이지는 옛 7번 영역 ‘화물·재고·자산 식별과 추적’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 [옛 분류원문]

> 옛 질문: 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? [옛 분류원문]

> 옛 원문 주석: **7번은 SCM 관점에서 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 화물의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [옛 분류원문]

이전 분류 기준: 원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]

## 2. 핵심 질문

로봇이 도착했을 때 실제로 무엇이 누구에게 넘겨졌는지 어떻게 확인할 것인가? [분류원문]

> 원문 주석: **17번은 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 작업 대상의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [분류원문]

원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]
```

### docs/categories/integration/robot-and-vendor-fleet-manager-integration.md (요약)

```markdown
# 20. 로봇·제조사 관제 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

제조사 API·SDK·관제 시스템과 연결하는 어댑터, 공통 명령·관측 계약, 로봇과 주고받는 통신 방식 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇·제조사 관제 연동 어댑터**: 제조사 API·SDK·관제 시스템을 연결해 명령·상태·오류를 변환하는 어댑터를 만든다
- **제어 위임 수준 결정**: 로봇을 하나씩 직접 제어할지, 제조사 관제에 임무 단위로 맡길지 정한다
- **공통 명령·관측 계약**: 단위와 시각 기준을 명시한 제조사 중립 명령·관측 형식을 정한다
- **로봇 통신 방식·메시징**: 명령·상태·지도·영상 데이터를 어떤 통신 방식(MQTT·DDS·gRPC·WebRTC 등)과 주기로 주고받을지 정하고 끊김·지연에 대비한다

이전 분류(2026-09-24)에서 이 페이지는 옛 9번 영역 ‘로봇·제조사 관제 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 [옛 분류원문]

> 옛 질문: 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? [옛 분류원문]

## 2. 핵심 질문

로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? [분류원문]
```

### docs/categories/integration/business-system-integration.md (요약)

```markdown
# 23. 업무 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

업무 요청을 받아 작업으로 바꾸고, 진행·완료를 되돌려 반영한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **업무 요청 수신·작업 변환**: 작업 요청을 만드는 업무 시스템(ERP·WMS·MES·병원 정보 시스템·호텔 객실 관리·빌딩 관리 등)에서 요청을 받아 로봇 작업으로 바꾼다
- **진행·완료 반영과 요청 변경 처리**: 작업 진행·완료를 업무 시스템에 되돌려 반영하고, 요청의 우선순위 변경·취소를 진행 중인 로봇 작업에 반영한다

이전 분류(2026-09-24)에서 이 페이지는 옛 1번 영역 ‘주문·업무 시스템 연계’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 [옛 분류원문]

> 옛 질문: 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? [옛 분류원문]

## 2. 핵심 질문

업무 시스템의 요청이 바뀌거나 취소되면 진행 중인 로봇 작업을 어떻게 바꿀 것인가? [분류원문]
```

### docs/categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md (요약)

```markdown
# 29. 명령·작업 실행의 신뢰성

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

명령 상태 관리, 중복 실행 방지, 관측 근거 완료 판정 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **명령 상태 관리**: 접수·실행·완료·취소 상태, 제어권, 시간 초과, 재시작 뒤 상태 복원을 관리한다
- **중복 실행 방지**: 응답이 끊긴 요청을 다시 보내도 같은 일을 두 번 하지 않게 한다
- **관측 근거 완료 판정**: 대기 시간이 지났다는 이유가 아니라 관측된 증거로 작업 단계의 완료를 인정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 12번 영역 ‘명령·작업 실행의 신뢰성’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 접수·실행·완료·취소 상태, 제어권, 중복 요청 방지, 시간 초과, 재시작 후 상태 복원 [옛 분류원문]

> 옛 질문: 응답이 끊긴 운반 요청을 다시 보내면 같은 화물을 두 번 처리하지 않을까? [옛 분류원문]

## 2. 핵심 질문

응답이 끊긴 명령을 다시 보내도 같은 일을 두 번 하지 않게 하려면? [분류원문]
```

### docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md (요약)

```markdown
# 38. 모니터링·이상 탐지·원인 분석

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

## 1. 한 줄 정의

감시, 로봇 건강 상태 진단, 이상 탐지, 원인 분석, 알림 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 모니터링**: 로그·이벤트·지표를 연결해 현재 운영을 감시한다
- **이상 탐지**: 평소와 다른 지연·정지·패턴을 찾아낸다
- **원인 분석**: 지연의 원인이 로봇·설비·통신·앞 작업 가운데 어디인지 가려낸다
- **알림·에스컬레이션**: 이상·지연·안전 사건을 알맞은 사람에게 알리고 필요하면 상위로 올린다
- **로봇 건강 상태 진단**: 배터리·모터·센서·통신 상태를 모아 로봇별 건강 상태를 보여 주고 이상을 알린다

이전 분류(2026-09-24)에서 이 페이지는 옛 19번 영역 ‘모니터링·이상 탐지·원인 분석’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 [옛 분류원문]

> 옛 질문: 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md (요약)

```markdown
# 39. 운영 성과 측정·개선

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-26 · 버전: 3

## 1. 한 줄 정의

지표 정의·측정, 로봇 성과와 업무 성과 구분, 운영 개선 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 성과 측정**: 처리량·완료 시간·가동률·대기 시간·에너지 같은 지표를 정의하고 측정한다
- **로봇 성과와 업무 성과 구분**: 로봇 가동률이 올라간 것이 실제 업무 성과(처리량·서비스 시간·비용)로 이어졌는지 나눠 본다
- **운영 개선**: 측정 결과로 운영 정책·배치·절차를 고치고 효과를 다시 잰다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 4번 영역 ‘성과·경제성·프로세스 개선’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 [옛 분류원문]

> 옛 질문: 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? [옛 분류원문]

## 2. 핵심 질문

로봇 가동률이 오른 것이 실제 업무 성과로 이어졌는가? [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md (요약)

```markdown
# 54. 시험·형식 검증·벤치마크

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

시험 설계·장애 주입·회귀 시험·형식 검증·벤치마크·재현 실험 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시험 설계·시험 환경**: 시뮬레이션 시험과 실기체 시험을 설계하고 시험장을 꾸린다
- **장애 주입 시험**: 고장·통신 단절·센서 오류를 일부러 넣어 대응을 확인한다
- **형식 검증**: 교착과 제약 위반이 없음을 수학적으로 검증한다
- **회귀 시험**: 업데이트 뒤 정상 상황과 장애 상황을 다시 시험한다
- **벤치마크·성능 비교**: 공개 벤치마크와 시험 환경으로 방법과 제품을 비교한다(NIST ARIAC 등)
- **재현 가능한 실험·증거 보존**: 같은 입력으로 반복 실험하고 결과와 증거를 내보낸다

이전 분류(2026-09-24)에서 이 페이지는 옛 23번 영역 ‘시험·형식 검증·벤치마크’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 [옛 분류원문]

> 옛 질문: 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [옛 분류원문]

## 2. 핵심 질문

업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 16건 / 전체 1399건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/open-questions.md (요약: 대상 영역 [24] 에 걸린 6건 / 전체 348건)

```markdown
- oq-012 [열림] 국내 물류센터는 로봇의 운반 완료와 WMS의 입고·인수 확정을 별도 단계로 두는가, 그렇다면 두 단계를 잇는 식별 키와 확정 대기 시간 기준은 무엇인가? (영역 23, 24)
- oq-013 [열림] ISA-95 세그먼트 의존 유형(B2MML DependencyType)을 입고·적치·피킹·출하 같은 창고 물류 작업의 선후관계 표현에 적용한 사례나 확장이 있는가? (영역 24, 26)
- oq-014 [열림] 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가? (영역 20, 24, 29)
- oq-137 [열림] 완료 기한·반복 주기·실패 처리 조건처럼 관제 작업 요청 스키마에 자리가 없는 시나리오 항목을 어느 층(시나리오 모델·워크플로 모델·스케줄러)이 보관하고 실행 시점에 어떻게 작업 요청으로 변환하는가? (영역 9, 24, 26, 20)
- oq-243 [열림] IEC 62559 사용 사례 템플릿이나 ISO/IEC/IEEE 29148 요구 명세 형식을 다중 로봇·로봇 오케스트레이션 사용 사례 정의에 적용한 사례가 있는가? (영역 2, 24)
- oq-345 [열림] 로봇 관제 인터페이스(VDA 5050 주문, Open-RMF 작업 요청)에 작업 사이 의존·대안 경로·기한을 표현하는 확장 제안이나 차기 판 논의가 있는가? (관련 기존 질문: oq-049, oq-137) (영역 20, 21, 24)
```

### inbox/corrections.md

````markdown
# 정정 요청함 (inbox/corrections.md)

이 파일은 위키 내용에 대한 정정 요청을 모으는 곳이다. 형식, 처리 흐름, 거부되는 경우는 docs/corrections.md(정정 요청 안내)에 있다.

- 한 요청은 `## corr-NNN` 제목으로 시작하는 블록 하나다. id 는 corr-001 부터 순서대로 늘리며, 아래 "요청 목록"에 새 블록을 덧붙인다.
- 필드는 서식의 여섯 줄(페이지, 문제 문장, 근거, 요청일, 요청자, 상태)을 그대로 쓰고 값만 채운다. 각 필드는 한 줄로 쓴다. 페이지·문제 문장·근거·요청일은 빌드 사양서 7.4 의 필드이고, 요청자·상태는 구축자가 더한 것이다. [가정]
- 상태는 요청자가 `open` 으로 쓴다. `applied`(반영됨)·`rejected`(반영하지 않음)는 퍼블리셔가 바꾸고, 그때 "처리 실행"과 "처리 메모" 줄을 덧붙인다.
- 리서치 에이전트는 다음 실행에서 이 파일 전체를 읽는다. 대상 페이지에 걸린 `open` 요청은 반드시 조사 질문에 들어가고, 내용 검증 에이전트가 1차 검증 항목 11(정정 요청 반영 여부)로 확인하며, 처리 결과는 docs/changelog.md(변경 이력)에 남는다.
- 분류 원문의 명칭·번호·정의·질문은 정정 대상이 아니다. 새 주제나 우선 영역은 config/priority.yaml 에 적는다.

## 서식

아래 블록을 복사해 "요청 목록" 끝에 붙이고, 제목의 `corr-NNN` 을 실제 id 로 바꾼 뒤 값을 채운다. 코드 펜스 안의 서식은 요청으로 읽히지 않는다(정정 요청을 읽는 스크립트는 코드 펜스 안의 `## corr-` 줄을 제외해야 한다). [가정]

```markdown
## corr-NNN

- 페이지: docs/<경로>/<파일>.md
- 문제 문장: "페이지에 있는 문장을 태그까지 그대로 옮긴다"
- 근거: 출처 URL 또는 설명
- 요청일: YYYY-MM-DD
- 요청자: 이름 또는 역할
- 상태: open
```

## 요청 목록

(아직 요청이 없다.)
````

### config/priority.yaml

```yaml
# config/priority.yaml — 사용자가 지정하는 우선 영역·주제·질문 (빌드 사양서 7.1, 7.4, 8.2)
#
# 비어 있으면 순환 규칙(config/rotation.yaml)만 따른다. 항목이 없는 키는 빈 목록([])으로 둔다.
# 네 키(areas, topics, questions, track_questions)는 빈 목록이라도 모두 있어야 하고, 항목의 필드 이름은 아래 예시와 같아야 한다.
# 항목의 뜻과 반영 시점은 config/README.md 와 docs/about/how-to-contribute.md 에 있다.
#
# 읽는 주체:
#   - pipeline/select_target.*  : areas·topics·questions 로 그날의 대상을 정한다(순환보다 우선, 7.1). questions 는 area_no 영역을 대상으로 올리고, 2주기에는 그 영역의 점수에도 더한다
#   - 리서치·검증 에이전트       : 이 파일 전문이 프롬프트의 "## 입력"에 들어간다. 대상 영역의 questions 는 조사 질문에 포함된다
#   - pipeline/select_target.*  : 트랙 실행의 대상 선정에서 track_questions 를 트랙 백로그(data/tracks/<slug>/backlog.json)에 제기 근거 "사용자"로 먼저 등록하고 그 실행의 질문으로 고른다
#   - 퍼블리셔                   : 대상 선정 뒤에 더해진 track_questions 를 같은 방식으로 등록한다(보완)
#
# area_no 는 1~67 의 세부영역 번호다(2026-09-28 개정 분류, _source/ROP_연구분야_분류.md). 사람이 읽기 쉽도록 주석에 영역 이름을 함께 적는다(예: 17. 작업 대상·자산 식별과 인계 추적).
# 지정한 항목이 처리되면 목록에서 지워도 된다. 지우지 않으면 rotation.yaml 의 priority.skip_if_targeted_within_days 가 지난 뒤 다시 우선된다.
# 우선 지정은 조사 대상을 정할 뿐 검증 규칙과 하루 예산(daily_budget)을 바꾸지 않는다.

# 세부영역을 먼저 다루게 한다. weight 는 대상 선정 점수에 더하는 가중치, reason 은 로그(target.json·일일 로그)에 남는 지정 사유다.
areas: []
# 작성 예시:
# areas:
#   - area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적
#     weight: 10            # 대상 선정 점수에 더하는 가중치
#     reason: "병원·상업 시설의 인계 확인 사례가 부족하다"

# 특정 주제로 주제 조사(run_type topic)를 실행하게 한다. area_no 는 주 연구영역이다.
topics: []
# 작성 예시:
# topics:
#   - title: "작업 대상 인계 확인에 EPCIS 이벤트를 쓰는 방법"
#     area_no: 17           # 주 연구영역: 17. 작업 대상·자산 식별과 인계 추적
#     weight: 8

# 답을 찾게 할 질문이다. area_no 영역을 areas 와 같이 순환보다 먼저 대상으로 올리고(가중치는 rotation.yaml 의 priority.question_weight), 그 영역이 대상이 되면 리서치 에이전트의 조사 질문에 포함된다.
questions: []
# 작성 예시:
# questions:
#   - question: "로봇 도착과 실제 작업 대상 인계를 어떤 이벤트로 구분해 기록하는가?"
#     area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적

# 트랙 백로그에 넣을 질문이다(8.2). 다음 트랙 실행의 대상 선정이 제기 근거 "사용자"로 백로그에 등록해 우선순위를 올린다(8.2).
# 처리 순서: 리서치 에이전트는 트랙 실행마다 현재 단계의 열린 질문 가운데 사용자 지정 → 앞 단계로 되돌아온 질문 → 오래된 순으로 1~3개를 고르므로(6.1),
# 현재 단계에 넣은 사용자 질문이 가장 앞에 온다. 사용자 질문이 여럿이면 priority(high → normal → low), 같으면 파일에 적힌 순이다 [가정].
# stage 가 현재 단계보다 앞이면 되돌아온 질문과 같이 다음 트랙 실행에서 우선 처리하고(8.2), 뒤이면 그 단계가 현재 단계가 될 때 다룬다 [가정].
track_questions: []
# 작성 예시:
# track_questions:
#   - track: manual-capability-ontology   # config/tracks/<slug>.yaml 의 slug
#     stage: 1              # 질문을 넣을 단계 번호(1 ~ 그 트랙의 단계 수: 매뉴얼 기반 로봇 기능 온톨로지 7, 채팅 기반 구성·운영 10, 건축 도면 자동 인식 5). 예: 단계 1. 기존 능력 표현 모델과 표준 조사
#     question: "산업 상호운용 규격의 팩트시트는 적재 제약을 어떤 필드로 기술하는가?"
#     priority: high        # high / normal / low. 사용자 지정 질문이 여럿일 때 고르는 순서에만 쓴다 [가정]
```

### runs/2026-10-09-27/research.md

```markdown
# 리서치 브리프 2026-10-09-27

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-27 |
| 날짜 | 2026-10-09 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 12. 채팅으로 업무 지시·오케스트레이션 |
| 대분류 | C. 채팅 기반 구성·운영 |

트랙 실행: 트랙 `chat-based-configuration-and-operation` · 단계 2 · 답한 질문 q2-05, q2-06

## 갭(비어 있거나 약한 섹션)

- 단계 2 질문 q2-05·q2-06·q2-07 열림 — target.json 지정(사용자 지정 0건, 되돌아온 질문 0건, 현재 단계 열린 질문 3건 중 오래된 순), 단계 2 페이지 3절에 {#q2-05}·{#q2-06}·{#q2-07} 소절 없음
- 단계 2 완료 조건: 업무 분해·배정 설계 초안 개념 목록 표에 작업 요구 적재물 속성·완료 조건 미확정(초안 6절 '작업 요구에 적재물 식별 … 더할 것인가' 질문 열림)
- 업무 분해·배정 설계 초안 6절: 현장 장소 용어와 경유점 이름·지도 id·WMS 로케이션 코드를 잇는 이름 대응 규칙 미정(oq-029와 겹침)
- 단계 2 페이지 2절 q2-01 항목–원천 대응표의 '대상 화물' 행: 품목 단위와 적재 단위의 대응 원천 미확인
- IEEE 1872.1-2024 본문 미열람으로 작업 모델 대조 없음(단계 2 페이지 4절 남은 불확실성)

## 조사 질문

1. 대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]
2. q2-05 지시 속 현장 장소 용어(예: 3층 출하 대기장, 2번 도크)와 공간 그래프 경유점 이름·지도 id·WMS 로케이션 코드를 대응시키는 이름 사전은 어떤 형식으로 두고 누가 관리하는가?
3. q2-06 채팅 지시의 '대상 화물'을 품목 단위(sku·수량)로 받을지 적재 단위(loadId·SSCC)로 받을지, 둘 사이 대응은 어느 시스템에서 가져오는가?
4. q2-07 IEEE 1872.1-2024 로봇 작업 표현 온톨로지는 작업 분해·선후 의존·배정 대상을 어떤 개념으로 표현하며, 업무 분해·배정 설계 초안의 업무·작업·배정 개념과 어떻게 대응하는가?
5. 실내 지도·용어 표준(IMDF, W3C SKOS, GS1 GLN 확장 성분)은 같은 장소의 정식 이름·별칭·코드를 어떤 구조로 담는가? (q2-05 의 이름 사전 형식, 단계 2 페이지 3절 겨냥)
6. 로봇이 보고하는 적재물 식별(VDA 5050 loads)과 물류 단위–품목 대응(GS1 EPCIS 집계 이벤트)은 어떤 필드로 표현되는가? (q2-06, 초안 6절 작업 요구 적재물 질문 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 교통 편집기(traffic-editor) 문서는 경유점(vertex)을 x·y·고도·이름·선택 파라미터로 저장하고 이름 기본값을 비워 두되 로봇이 작업을 끝내야 하는 경유점에는 이름을 요구하며, dock_name·pickup_dispenser·dropoff_ingestor·is_charger 같은 속성과 이름 붙은 층(L1 등)을 두고 승강기는 층을 이름으로 참조하지만, 별칭이나 다국어 이름 기능은 서술하지 않는다. | ref-079 | 아니오 | medium | 2026-10-09 | — | — |
| f2 | [사실] | Open-RMF 장소 스키마는 장소를 경유점 이름, 경유점 번호, 경유점과 방향을 담은 객체 가운데 하나로 지정한다. | ref-412 | 아니오 | medium | 2026-09-25 | — | — |
| f3 | [사실] | Open-RMF 건물 지도 그래프의 노드 메시지(GraphNode)는 x·y 좌표, 이름, 파라미터 목록을 가진다. | ref-414 | 아니오 | medium | 2026-09-25 | — | — |
| f4 | [사실] | OGC 커뮤니티 표준 IMDF 1.0.0 의 Unit 은 장소 운영 조직(Venue Organization)이 선언한 이름(name)과 그 조직이 인정하는 대체 이름(alt_name)을 언어 태그별 값 묶음(LABELS)으로 두고, 층 식별자(level_id)와 점 표현(display_point)을 함께 둔다. | ref-1393 | 아니오 | medium | 2026-10-09 | — | — |
| f5 | [사실] | W3C SKOS 권고안(2009-08-18)은 개념에 언어별 대표 이름(prefLabel), 대체 이름(altLabel), 화면에 보이지 않는 검색용 이름(hiddenLabel, 오탈자 포함)을 두고, 한 언어 태그당 대표 이름은 하나만 허용하며, 개념 체계 안에서 개념을 가리키는 코드(notation)를 따로 둔다. | ref-1394 | 아니오 | medium | 2009-08-18 | — | — |
| f6 | [사실] | GS1 은 시설 안 하위 위치(구역·선반 등)를 GLN 단독 또는 GLN 과 확장 성분(extension component)으로 식별하게 하며, 확장 성분은 물리적 위치를 가리키는 GLN 과 함께일 때만 유효하다. | ref-1400 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f7 | [사실] | Murata 외(arXiv 2509.12838, v2 2025-09-30, AROB-ISBC 2026 투고)는 사용자가 로봇마다 지정한 영역에서 학습한 공간 개념을 언어 모델의 작업 분해·다중 로봇 배정에 쓰는 틀을 제안하고, 배정 성공을 50회 중 47회(무작위 28회, 상식 기반 26회)로 보고했다(저자 보고). | ref-1398 | 아니오 | medium | 2025-09 | 수행 자원 | — |
| f8 | [추정] | q2-05 에 대해 확인한 형식을 종합하면, 이름 사전은 로봇 관제가 받는 정본 키(Open-RMF 경유점 이름·층 이름, VDA 5050 지도 id, WMS 로케이션 코드 또는 GLN·확장 성분)를 SKOS 의 notation 처럼 코드로 두고, 현장 호칭은 IMDF name·alt_name 이나 SKOS prefLabel·altLabel·hiddenLabel 같은 언어별 대표 이름·별칭으로 붙이는 형식이 선택지로 보이며, IMDF 가 이름을 장소 운영 조직이 선언하게 하듯 정본 이름은 현장 운영 조직이 정하고 ROP 는 대응표를 보관·검증하는 분담이 맞아 보인다(이 위키의 종합, 물류 현장 사례 미확인). | ref-079, ref-412, ref-414, ref-1393, ref-1394, ref-1400 | 아니오 | low | 2026-10-09 | 작업 대상 | — |
| f9 | [추정] | 이번 검색 범위(한국어·영어)에서 물류창고 현장 호칭을 로봇 경유점 이름·WMS 로케이션 코드와 잇는 이름 사전을 정한 표준이나 공개 사례, 국내 WMS 로케이션 코드(동·열·연·단) 체계의 공식 자료는 찾지 못했고, 가장 가까운 연구는 가정 환경에서 학습한 공간 개념을 쓰는 Murata 외였다(부재 확인 아님). | ref-1398, ref-079 | 아니오 | low | 2026-10-09 | — | — |
| f10 | [사실] | VDA 5050 공식 저장소의 상태 스키마(main 브랜치)는 로봇이 다루는 적재물 배열(loads)을 선택 필드로 두고, 적재물 객체에 필수 필드 없이 loadId(바코드·RFID 값 같은 고유 id, 감지했으나 식별 못 하면 빈 값)·loadType·loadPosition·boundingBoxReference·loadDimensions·weight 를 두며, 품목 코드·수량·SSCC 필드는 없다. | ref-051 | 아니오 | medium | 2026-10-09 | 작업 대상 | — |
| f11 | [사실] | Open-RMF 배송 작업의 적재물 항목은 품목 코드(sku)와 수량(quantity)을 필수로, 칸(compartment)을 선택으로 둔다. | ref-411 | 아니오 | medium | 2026-09-25 | 작업 대상 | — |
| f12 | [사실] | GS1 EPCIS 공식 저장소의 집계 이벤트(AggregationEvent) JSON 스키마는 type·action 을 필수로 두고 상위 단위 식별자(parentID, URI)와 개체 단위 하위 목록(childEPCs)·품목 수량 목록(childQuantityList)을 두며, action 이 DELETE 가 아니면 두 하위 목록 가운데 하나 이상을 비우지 않게 한다. | ref-1392 | 아니오 | medium | 2026-10-09 | 작업 대상 | — |
| f13 | [사실] | GS1 Belgium & Luxembourg 는 SSCC 를 추적할 수 있는 물류 단위(예: 여러 거래 단위를 묶은 팔레트)를 유일하게 식별하는 코드로 설명하며, 물류 단위는 같은 품목 또는 여러 품목으로 이루어질 수 있고 단위마다 SSCC 를 하나씩 붙이며, SSCC 와 내용물(품목·수량)의 연결 방식은 그 페이지에서 서술하지 않는다. | ref-1395 | 아니오 | medium | 2026-10-09 | 작업 대상 | — |
| f14 | [사실] | OPC UA for ISA-95 작업 제어 노드셋(모델 발행일 2024-01-31)의 자재 데이터형은 자재 정의 id·로트 id·하위 로트 id·수량·단위 등을 선택 필드로 둔다. | ref-130 | 아니오 | medium | 2024-01-31 | 작업 대상 | 원문 미열람 |
| f15 | [추정] | q2-06 에 대해 확인한 형식을 종합하면, 로봇 관제 인터페이스는 Open-RMF 배송이 품목 단위(sku·수량), VDA 5050 이 적재 단위(loadId)만 받고 둘 사이 대응 필드가 없으므로, ROP 작업 모델은 지시의 대상 화물을 품목 단위와 적재 단위 두 갈래로 받을 수 있게 두고 대응(어느 SSCC 단위에 어느 품목이 몇 개인가)은 EPCIS 집계 이벤트(parentID–childQuantityList)나 업무 시스템의 자재·로트 기록에서 가져오며, VDA 5050 loadId 는 SSCC 형식을 강제하지 않으므로 지시한 SSCC 와 로봇 보고 loadId 의 대조는 ROP 몫이 되는 구성이 선택지로 보인다(이 위키의 종합). | ref-411, ref-051, ref-1392, ref-130, ref-1395 | 아니오 | low | 2026-10-09 | 작업 대상 | — |
| f16 | [추정] | 연계 대상: 품목과 물류 단위의 대응(포장·적재 구성)과 재고 정본은 상위 업무 시스템(WMS 등)과 EPCIS 이벤트 저장소가 관리하는 정보이며, ROP 는 그 대응을 읽어 작업 대상을 확인하는 쪽으로 보인다(이 위키의 종합). | ref-1392, ref-130 | 아니오 | low | 2026-10-09 | 작업 대상 | — |
| f17 | [사실] | IEEE SA 는 IEEE 1872.1-2024(2024-06-18 발행)를 학습·로봇·자동화 분야의 작업 지식을 표현·추론·교환하는 온톨로지로 소개하며, 핵심 용어의 정의·속성·유형·구조·성질·제약·관계와 계층 계획기·설계자의 작업 지식 표현 방식을 다루고, 실무 구현 지침 P1872.1.1 이 따로 개발되고 있다고 밝힌다. | ref-504 | 아니오 | medium | 2024-06-18 | — | 원문 미열람 |
| f18 | [사실] | Balakirsky 외(MSEC 2017)는 로봇 작업 온톨로지 표준을 준비하는 국제 연구 그룹의 작업을 소개하며, 작업 구조(하위 클래스·범주·관계로의 분해)와 작업 공통·작업별 속성을 다루고 작업을 플랫폼·사용자와 잇는 공통 표현을 목표로 한다고 밝혔다. | ref-1396 | 아니오 | medium | 2017-06-08 | — | — |
| f19 | [사실] | Aguado 외(Frontiers in Robotics and AI 11권, 2024-07-10)는 IEEE 로봇·자동화 온톨로지 작업반의 로봇 작업 표현 하위 그룹이 목표에서 하위 목표로 가는 작업 분해를 담은 중간 수준 온톨로지를 만들고, 작업과 그 속성, 성능 관련 능력 용어, 산업 공정 작업 목록을 정의한다고 정리했다. | ref-042 | 아니오 | medium | 2024-07-10 | — | — |
| f20 | [추정] | q2-07 에 대해 공개 자료로 보면 IEEE 1872.1 계열 작업 온톨로지는 목표에서 하위 목표로 가는 분해를 핵심 구조로 두고 작업을 플랫폼(로봇)·능력과 잇는 것으로 보여 초안의 업무(목표)–작업(하위 목표·실행 단위)–배정(작업–로봇)과 대응 후보가 되지만, 표준 본문을 열람하지 못해 작업 사이 선후 의존과 배정 대상을 어떤 개념으로 표현하는지는 확인하지 못했다(이 위키의 종합). | ref-504, ref-1396, ref-042 | 아니오 | low | 2026-10-09 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-1392 | GS1 (gs1/EPCIS GitHub) | EPCIS — JSON-Schema/schemas/AggregationEvent-JSON-Schema.json | 미확인 | 표준 | high | 2026-10-09 | https://github.com/gs1/EPCIS/blob/master/JSON-Schema/schemas/AggregationEvent-JSON-Schema.json | 아니오 |
| ref-1393 | OGC (Apple Inc. 기여) | Indoor Mapping Data Format (IMDF) 1.0.0 — Unit | 미확인 | 표준 | high | 2026-10-09 | https://docs.ogc.org/cs/20-094/Unit/index.html | 아니오 |
| ref-1394 | W3C (Miles, A., & Bechhofer, S. 편집) | SKOS Simple Knowledge Organization System Reference | 2009-08-18 | 표준 | high | 2026-10-09 | https://www.w3.org/TR/skos-reference/ | 아니오 |
| ref-1395 | GS1 Belgium & Luxembourg | Logistic units | 미확인 | 표준 | medium | 2026-10-09 | https://www.gs1belu.org/en/logistic-units | 아니오 |
| ref-1396 | Balakirsky, S. B., Schlenoff, C. I., Fiorini, S. R. 외 (NIST 게시, MSEC 2017) | Towards a Robot Task Ontology Standard | 2017-06-08 | 논문 | medium | 2026-10-09 | https://www.nist.gov/publications/towards-robot-task-ontology-standard | 아니오 |
| ref-042 | Aguado, E., Gomez, V., Hernando, M., Rossi, C., & Sanz, R. (Frontiers in Robotics and AI 11) | A survey of ontology-enabled processes for dependable robot autonomy | 2024-07-10 | 논문 | high | 2026-10-09 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1377897/full | 아니오 |
| ref-1398 | Murata, K., Hasegawa, S., Ishikawa, T., Hagiwara, Y., Taniguchi, A., El Hafi, L., & Taniguchi, T. | Multi-Robot Task Planning for Multi-Object Retrieval Tasks with Distributed On-Site Knowledge via Large Language Models | 2025-09 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2509.12838 | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-1400 | GS1 | GLN extension component | 미확인 | 표준 | medium | 2026-10-09 | https://gs1.org/standards/id-keys/gln/extension-component | 예 |
| ref-411 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/event_description__payload_transfer.json | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__payload_transfer.json | 아니오 |
| ref-412 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/place.json | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/place.json | 아니오 |
| ref-414 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/GraphNode.msg | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/GraphNode.msg | 아니오 |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 2024-01-31 | 표준 | medium | 2026-10-09 | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL | 예 |
| ref-504 | IEEE Standards Association | IEEE 1872.1-2024 — IEEE Standard for Robot Task Representation | 2024-06-18 | 표준 | medium | 2026-10-09 | https://standards.ieee.org/ieee/1872.1/6993/ | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md | 2, 3, 4, 5, 6, 8, 9 | q2-05 답: f1·f2·f3·f4·f5·f6·f7·f8·f9 (신뢰도 low) / q2-06 답: f10·f11·f12·f13·f14·f15·f16 (신뢰도 low) / q2-07 부분 답: f17·f18·f19·f20 — 2절 q2-05·q2-06 답함(답한 실행 2026-10-09-27, #q2-05·#q2-06), q2-07 은 열림 유지; 3절 소제목 신설({#q2-05}: 로봇 관제 쪽 이름 f1~f3, 실내 지도·용어 표준의 이름·별칭 구조 f4·f5, GS1 하위 위치 f6(원문 미열람), 학습 공간 개념 연구 f7, 종합 f8(추정)·공백 f9 / {#q2-06}: VDA 5050 loads f10, Open-RMF 품목 단위 f11(#q2-01 기존 서술 가리킴), EPCIS 집계 이벤트 f12, SSCC f13, ISA-95 자재 f14, 종합 f15·연계 대상 f16 / {#q2-07}: 부분 답 f17~f20, 표준 본문 미열람 명시); 4절 결론·불확실성, 5절 후속 질문, 6절 완료 조건(조건 2 미충족, 전환 아니오), 8절 출처, 9절 이력 |
| update | docs/tracks/chat-based-configuration-and-operation/task-model-draft.md | 2, 6 | 트랙 산출물 갱신: track.ontology_changes(상황 개념의 대상 표현에 해석 결과 '대상 화물 참조' 짝 추가) 승인 시 2절 반영과 초안 v1.0 → v1.1(f10·f11·f12·f13). 6절 '작업 요구에 적재물 식별 … 더할 것인가' 질문에 q2-06 답(f15) 연결, '현장 장소 용어와 경유점 이름 … 이름 대응 규칙' 항목에 q2-05 답(f8) 연결, 'IEEE 1872.1-2024 … 대조하지 못했다' 항목에 부분 답(f20) 연결 |
| update | docs/ideas/chat-based-configuration-and-operation.md | 4 | 아이디어 페이지 4절: '필요한 데이터 항목과 원천' 소절의 장소·대상 화물 행 아래에 이름 사전 형식(f4·f5·f8)과 대상 화물 두 단위·대응 원천(f10·f12·f15) 소절 추가, 표준·형식 소절의 IEEE 1872.1 행 '미확인'은 지우지 않고 공개 자료 범위의 분해 구조(f18·f19·f20) 병기 |
| update | docs/categories/space-and-map-model/place-semantics-and-map-management.md | 6, 7 | 트랙 chat-based-configuration-and-operation 단계 2 반영 제안 (f1, f4, f5, f6, f8): IMDF name·alt_name, SKOS 대표·대체·숨은 이름과 notation, GLN 확장 성분을 장소 이름·별칭 사전 형식 후보로. 짝 엔진 영역 12. 채팅으로 업무 지시·오케스트레이션과 연결. 반영은 다음 해당 영역 실행에서. |
| update | docs/categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md | 7 | 트랙 chat-based-configuration-and-operation 단계 2 반영 제안 (f10, f12, f13, f15): VDA 5050 상태 loads 의 loadId(SSCC 형식 비강제)와 EPCIS 집계 이벤트의 parentID–childQuantityList, SSCC 물류 단위를 작업 대상 식별 단위 대응 근거로. |
| update | docs/categories/robot-ontology/robot-capability-and-task-representation.md | 7 | 트랙 chat-based-configuration-and-operation 단계 2 반영 제안 (f17, f18, f19): IEEE 1872.1-2024 의 공개 범위 설명(목표→하위 목표 분해, 작업–플랫폼·능력 연결, P1872.1.1 구현 지침 개발 중), 본문 미열람 명시. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 단순 지식 조직 체계 | Simple Knowledge Organization System (SKOS) | 개념에 언어별 대표 이름(prefLabel)·대체 이름(altLabel)·검색용 숨은 이름(hiddenLabel)과 코드(notation)를 붙여 용어 체계를 표현하는 W3C 권고안(2009)이다. |
| GLN 확장 성분 | GLN Extension Component | 물리적 위치를 가리키는 GS1 위치 코드(GLN)에 덧붙여 그 시설 안의 구역·선반 같은 하위 위치를 식별하는 GS1 의 코드 성분이다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 12회 · 신규 출처 10건
- 미확인 항목:
    - q2-07 부분 답: IEEE 1872.1-2024 본문(유료)과 P1872.1.1 미열람으로 작업 사이 선후 의존·배정 대상 개념의 표현 방식을 확인하지 못함
    - f6 GS1 GLN 확장 성분 페이지는 gs1.org 403 으로 원문 미열람(검색 요약 기준)
    - f17 IEEE SA 소개 페이지는 검색 요약 기준(원문 미열람)
    - ref-1396 NIST 게시 PDF 본문은 텍스트 추출 실패로 초록만 확인
    - ref-042 Frontiers 서베이는 본문 앞부분(10만 자)만 열람
    - 국내 WMS 로케이션 코드 체계(동·열·연·단) 공식 자료와 국내 물류센터의 SSCC–로봇 작업 연동 사례 미발견(부재 확인 아님)
    - IMDF LABELS 자료형의 정식 정의는 참조 절을 열지 않아 예시 기준
    - 모든 finding 교차 확인 없음(단일 출처 또는 이 위키의 종합)
- 범위 경계 위반 의심:
    - f16: 품목–물류 단위 대응과 재고 정본은 분류 원문 19장의 상위 업무 시스템 경계라 '연계 대상: '으로 표시
    - f10: 로봇의 적재물 감지·식별(바코드·RFID 판독)은 로봇 자체 지능·제어 쪽이며, ROP 근거로는 보고 필드 구조만 씀
    - f7: 공간 개념 학습은 로봇 쪽 인식 기능이며, 장소 이름을 배정에 쓰는 구조만 근거로 씀
- 한계: 스키마 불일치 재실행. 반려 사유(f5·f17 이 벤더 문서만 근거인 [사실]인데 vendor_claim 표시 없음)에 대응하려 했으나 직전 반환값이 프롬프트에 들어 있지 않아 같은 세 질문(q2-05·q2-06·q2-07)으로 브리프를 다시 구성했다. 이번 브리프에는 출처 유형 '벤더 문서'가 없고, 모든 [사실] finding 은 표준·오픈소스 문서·논문에 기대므로 vendor_claim 대상이 없다. 트랙 실행(단계 2), web_fetch_available: true · fetch_mode full. 검색 12회/40, 신규 출처 10건/20(ref-051~ref-1400, 예약 구간 안), 재사용 5건(ref-411·ref-412·ref-414·ref-130 은 이번에 다시 열지 않아 fetched false, ref-504 는 검색 요약만). gs1.org·gs1uk.org 는 403 으로 열지 못했다. 질문 선택: target.json 지정 q2-05·q2-06·q2-07(현재 단계 열린 질문 오래된 순). 답한 질문: q2-05(이름 사전 형식은 표준 원문 근거, 관리 분담·물류 적용은 종합이라 low), q2-06(필드 구조는 원문, 대응 원천 결론은 종합이라 low). q2-07 은 표준 본문 미열람으로 부분 답이며 answered_question_ids 에서 뺐다. 한국 자료: 국내 WMS 로케이션 코드·GS1 Korea SSCC 적용 자료를 한국어 검색 2회로 찾았으나 공식 자료를 찾지 못했다. 교차 규칙: L. AI·학습 기술 관련 f7 은 44. 로봇 기반 모델·언어 모델 계획과 적용 대상 25. 작업 배정 — MRTA 에 함께 연결할 수 있다. 18. 실시간 세계 상태·데이터 일관성·34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음, 입력 누락 없음, 우선 지정 질문 없음. 후속 질문 3건. 온톨로지 변경 1건(상황 개념의 대상 표현에 '대상 화물 참조' 짝, 작업 요구는 능력 온톨로지 초안 대조 전이라 건드리지 않음). 열린 질문(oq) 신규 없음: 장소 이름 대응은 oq-029·oq-201, 적재 단위 판독 불일치는 oq-003·oq-036 과 겹친다. 페이지 제안: 트랙 산출물 3건, 세부영역 반영 제안 3건(갱신 상한과 별도).

## 트랙 블록

- 트랙: chat-based-configuration-and-operation · 단계: 2
- 답한 질문 id: q2-05, q2-06

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 이름 사전의 별칭(altLabel·hiddenLabel)이 여러 장소에 겹칠 때(예: '2번 도크'가 두 층에 있음) 챗봇은 층·구역 맥락으로 좁힐지 되물을지를 어떤 규칙으로 정하고, 그 규칙을 이름 사전에 어떻게 기록하는가? (q2-05 에서 파생) (관련: q4-20, q4-07) | 4 | f8 |
| — | SSCC 같은 적재 단위로 받은 지시에서 로봇이 보고한 loadId 가 지시한 SSCC 와 다르거나 빈 값일 때 ROP 는 진행·보류·재스캔·사람 확인 가운데 무엇을 하는가? (q2-06 에서 파생) (관련: oq-003, oq-036) | 4 | f10 |
| — | IEEE 1872.1-2024 의 실무 구현 지침 P1872.1.1 이나 공개 사용 사례·OWL 파일이 있어 작업 분해·선후 의존·배정 대상 개념을 본문 없이 확인할 수 있는가? (q2-07 에서 파생) | 2 | f17 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 상황 (Situation) | f10, f11, f12, f13 | 대상 표현에 해석 결과 '대상 화물 참조'를 짝으로 더한다: 품목 단위(sku·GTIN 과 수량, Open-RMF 배송 f11) / 적재 단위(SSCC 또는 로봇 보고 loadId, VDA 5050 loads f10, SSCC 물류 단위 f13). 장소 표현–공간 노드 참조 짝(v0.4)과 같은 방식이다. 두 단위 사이 대응 원천(EPCIS 집계 이벤트 f12, 업무 시스템)은 추정 근거(f15)라 정의에 넣지 않고 메모로만 둔다. 작업 요구의 적재물 속성(초안 6절 질문)은 능력 온톨로지 초안과 대조하지 않았으므로 건드리지 않는다. 기존 상태 '확정' 유지. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 업무 분해·배정 설계 초안 개념 목록 표에 작업 요구 적재물 속성·완료 조건 미확정
    - q2-07 부분 답(IEEE 1872.1-2024 본문 미열람)
    - q2-05·q2-06 답과 아이디어 페이지 4절 반영은 검증 승인 전
```

### runs/2026-10-09-26/research.md

```markdown
# 리서치 브리프 2026-10-09-26

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-26 |
| 날짜 | 2026-10-09 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 14. 도면·BIM에서 지도 만들기 |
| 대분류 | D. 공간·지도 모델 |

트랙 실행: 트랙 `floorplan-recognition` · 단계 2 · 답한 질문 q2-04, q2-06

## 갭(비어 있거나 약한 섹션)

- 되돌아온 단계 1 질문 q1-08 조사 중(실행 2026-10-09-21 부분 답), 단계 2 질문 q2-04·q2-06 열림 — target.json 지정(사용자 지정 0건, 되돌아온 질문 1건, 현재 단계 열린 질문 6건 중 오래된 순). 같은 세 질문을 다룬 실행 2026-10-09-24 는 1차 검증 조건부 승인 뒤 스토리텔러 실패로 보류되어 반영되지 않음
- 단계 2 페이지 2절 표에서 q2-04·q2-06 미답, 3절에 {#q2-04}·{#q2-06} 소제목 없음
- 단계 2 페이지 q2-02 비교표 래스터 열 '엘리베이터: 공개 데이터셋 라벨 미확인(추정)' 칸과 아이디어 페이지 3절 데이터셋 비교표의 CubiCasa5K '계단 있음' 칸이 클래스 목록 원문·공식 코드로 확인되지 않음
- 공간 그래프 스키마 초안 6절: '로봇 충전소는 이번에 확인한 IFC 4.3 유형 값에 없어' 항목(q2-06)이 콘센트·전기기기 유형 열거 두 개만 근거로 함 — 전기 저장 장치 유형 열거는 미확인
- 단계 2 완료 조건: 관계(엣지) 쪽 표준 대응이 공간 그래프 스키마 초안에 없음 — 이번 실행 밖
- 14. 도면·BIM에서 지도 만들기 섹션 7. 관련 표준·프레임워크·오픈소스 — IDS·사용자 정의 속성 세트 같은 BIM 납품 요구 수단 없음, 섹션 11 oq-197 미해결

## 조사 질문

1. 이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? [분류원문]
2. q2-04 AI Hub 건축 도면 데이터와 CubiCasa5K 의 클래스 목록에 계단·엘리베이터가 포함되는지, 그리고 상업적 이용 조건은 무엇인가?
3. q2-06 로봇 충전소·작업 스테이션처럼 IFC 4.3 표준 유형 값에 없는 운영 시설을 BIM 에 담으려면 사용자 정의 유형·속성 세트로 표현해야 하는가, 이를 정한 IDS·속성 세트 관례나 사례가 있는가? (q1-03 에서 파생)
4. q1-08 국내 물류센터에서 로봇 도입 시 지도 작성·충전소 등 공용 자원 등록·제조사별 좌표 정렬에 든 시간을 단계별로 공개한 공공·학술 자료나 사례가 있는가? (q1-04 에서 파생)
5. AI허브 원 이용정책은 데이터 가공·재배포, 학습 모델의 상업적 이용, 국외 이용을 어떻게 정하며 2차 기술(공공데이터포털)과 무엇이 다른가? (q2-04 이용 조건, 섹션 11 oq-197 겨냥)
6. IFC 4.3 의 전기 저장 장치 유형 열거(충전기 값 포함), 프록시·USERDEFINED·속성 세트 명명 규칙과 IDS 1.0 의 엔터티·속성 패싯·값 제한은 표준 밖 운영 시설을 납품 요구로 기술하는 데 무엇을 제공하는가? (단계 2 페이지 3절, 14. 도면·BIM에서 지도 만들기 섹션 7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | AI Hub 건축 도면 데이터의 라벨은 구조 8종(여닫이문·미닫이문·기타문, 여닫이창·미닫이창·기타창, 철근콘크리트벽·기타벽), 공간 12종(거실·침실·주방·현관·발코니·화장실·실외기룸·드레스룸·기타(다목적공간)·엘리베이터홀·계단실·엘리베이터), 객체 5종(변기·세면대·싱크대·욕조·가스레인지)이며, 계단 단독 클래스는 없고 충전 위치 같은 로봇 운영 클래스도 없다. | ref-1012 | 아니오 | medium | 2023-12 | 작업 대상 | — |
| f2 | [사실] | AI Hub 건축 도면 데이터 소개 페이지는 내국인만 데이터 신청이 가능하고 승인 뒤 API 로 내려받게 한다고 적지만, 이 데이터셋에 고유한 라이선스·상업적 이용 문구는 두지 않고 상단 메뉴의 이용정책 링크와 하단 이용약관 링크만 둔다. | ref-1012 | 아니오 | medium | 2026-10-09 | — | — |
| f3 | [사실] | AI Hub 건축 도면 데이터의 도면 48,033장은 모두 주거 유형(아파트 38,521, 연립다세대 4,859, 단독주택 4,653)이다. | ref-1012 | 아니오 | medium | 2023-07-26 | 작업 대상 | — |
| f4 | [사실] | AI허브 데이터 이용정책 원문은 개방 AI데이터를 영리·비영리 연구·개발 목적으로 활용할 수 있다고 하면서도 인공지능 학습모델의 학습용으로만 쓰게 하고, 데이터셋 판매 등 상업적 이용은 수행기관과 별도 협의하게 하며, 승인 없이 다른 법인·단체·개인에게 열람·제공·양도·대여·판매하지 못하게 하고, 한국지능정보사회진흥원 사업결과임을 2차적 저작물에도 밝히게 하며, 국외에 소재하는 법인·단체·개인의 이용에는 별도 합의를 요구한다. | ref-1421 | 아니오 | medium | 2026-10-09 | — | — |
| f5 | [사실] | 공공데이터포털의 경기도 고양시 AI 학습용 샘플 데이터 페이지(다른 데이터셋)는 AI허브 데이터의 이용 조건을 'AI허브 데이터로 학습한 AI 모델·서비스는 자유롭게 배포·활용 가능하고 영리적 판매·활용도 제한하지 않으나 AI허브 데이터 사용을 명시해야 하며, NIA·구축기업과 사전 협의한 경우 외에는 데이터를 재가공해 배포하는 행위는 원칙적으로 불가'로 옮겨 적는다. | ref-1424 | 아니오 | medium | 2026-06-16 | — | — |
| f6 | [추정] | q2-04 의 AI Hub 이용 조건을 종합하면, 원 이용정책은 데이터 자체의 제3자 제공·판매와 국외 주체 이용을 제한하고 상업적 판매는 별도 협의로 두되 학습 모델의 배포·상업 이용은 직접 말하지 않으며, 학습 모델의 영리 활용을 명시적으로 허용하는 문구는 다른 데이터셋을 다룬 2차 기술에서만 확인되므로, 상용 ROP 가 이 데이터로 학습한 도면 인식 모델을 쓰는 것은 가능해 보이나 데이터의 가공·재배포·해외 활용은 별도 합의가 필요하고 모델 배포 조건도 운영기관 확인이 필요해 보인다(법적 판단 아님). | ref-1421, ref-1424, ref-1012 | 아니오 | low | 2026-10-09 | — | — |
| f7 | [사실] | CubiCasa5K 데이터셋의 Zenodo 레코드(1.0 판, 2019-03-28 게시)는 라이선스를 Creative Commons Attribution Non Commercial Share Alike 4.0 International(CC BY-NC-SA 4.0)로 표기한다. | ref-1422 | 아니오 | medium | 2019-03-28 | — | — |
| f8 | [사실] | CubiCasa5K 공식 코드(floortrans/loaders/house.py)는 SVG 요소의 class 속성('Space <방 이름>')에서 방 이름을 읽고 원 방 범주 목록에 Elevator(21)·StairWell(53)·Stairs(64)를 두지만, 학습용 매핑(rooms_selected·room_name_map)에서 Elevator·StairWell 을 일반 방(값 11, 'Room')으로 합치고 Stairs 는 매핑에 없으며 그 처리 블록은 주석 처리해, 기본 학습 라벨에는 계단·엘리베이터가 따로 남지 않는다. | ref-1423 | 아니오 | medium | 2026-10-09 | — | — |
| f9 | [사실] | CubiCasa5K 공식 저장소 README 는 5,000장·80개 이상 범주의 다각형 주석과 SVG 를 실행 중 파싱하는 선택지를 적지만 계단·엘리베이터와 라이선스는 언급하지 않는다. | ref-062 | 아니오 | medium | 2026-10-09 | — | — |
| f10 | [추정] | q2-04 에 대해 확인한 자료를 종합하면, AI Hub 건축 도면 데이터는 엘리베이터·엘리베이터홀·계단실을 공간 클래스로 두지만(계단 단독 클래스 없음, 주거 도면 기준) CubiCasa5K 는 원 주석 범주(코드가 읽는 SVG class 이름)에 엘리베이터·계단실·계단이 있어도 공식 학습 매핑에서는 일반 방으로 합치거나 쓰지 않으므로, 기존 위키의 'CubiCasa5K 계단 라벨 있음'은 원 주석 범주 수준의 서술로 보이고, 승강기·계단 영역을 바로 학습할 수 있는 공개 라벨은 AI Hub 쪽이며, CubiCasa5K 는 비상업(CC BY-NC-SA 4.0) 조건이라 상용 이용에는 권리자의 별도 허락이 필요할 것으로 보이고(법적 판단 아님), 두 자료 모두 충전 위치 라벨은 없는 것으로 보인다. | ref-1012, ref-1423, ref-1422, ref-1421 | 아니오 | low | 2026-10-09 | 작업 대상 | — |
| f11 | [사실] | IFC 4.3 문서(개발 브랜치)는 IfcBuildingElementProxy 를 IfcBuiltElement 하위 유형과 같은 기능을 하는 프록시로 정의해 명세가 아직 정의하지 않은 특수 건축 요소의 교환과 응용이 의미 정의에 대응시킬 수 없는 요소에 쓰게 하고, PredefinedType 을 USERDEFINED 로 두면 ObjectType 을 반드시 주게 하며, IFC4.3.0.0 부터는 공간 자리표시·예비 공간 용도로 쓰지 말고 IfcVirtualElement 를 쓰라고 한다. | ref-1425 | 아니오 | medium | 2026-10-09 | — | — |
| f12 | [사실] | IFC 4.3 문서의 IfcTransportElement 에도 PredefinedType 이 USERDEFINED 이면 상속받은 ObjectType 을 제공하도록 하는 형식 제약(CorrectPredefinedType)이 있다. | ref-213 | 아니오 | medium | 2026-10-09 | — | — |
| f13 | [사실] | IFC 4.3 문서(개발 브랜치)는 IfcElectricFlowStorageDevice 를 전기 에너지를 저장하고 점진적으로 내보낼 수 있는 장치로 정의하고(IFC4 신규 엔터티), 충전용 입력 포트와 출력 포트를 두며, PredefinedType 이 USERDEFINED 이면 ObjectType 을 요구한다. | ref-1428 | 아니오 | medium | 2026-10-09 | — | — |
| f14 | [사실] | IFC 4.3 의 전기 저장 장치 유형 열거(IfcElectricFlowStorageDeviceTypeEnum, 개발 브랜치)는 BATTERY·UPS 등과 함께 RECHARGER 값을 두고 이를 2차 전지나 충전식 배터리에 전류를 흘려 에너지를 넣는 충전기로 정의하지만, 차량·로봇 충전은 언급하지 않는다. | ref-1427 | 아니오 | medium | 2026-10-09 | — | — |
| f15 | [사실] | buildingSMART 의 IFC 4.3.2 개발 문서는 RECHARGER 유형의 IfcElectricFlowStorageDevice·IfcElectricFlowStorageDeviceType 에 쓰는 속성 세트 Pset_ElectricFlowStorageDeviceTypeRecharger 를 두며, 그 속성은 공급 정격 전류(NominalSupplyCurrent) 하나뿐이고 변경 이력에 IFC4.3_ADD2 신규 자원으로 적혀 있다(작업 초안 표기). | ref-1429 | 아니오 | medium | 2026-10-08 | — | — |
| f16 | [사실] | IFC 4.3 의 콘센트 유형 열거(IfcOutletTypeEnum)와 전기기기 유형 열거(IfcElectricApplianceTypeEnum)에는 차량·로봇 충전 설비를 뜻하는 값이 없고 USERDEFINED·NOTDEFINED 가 남는다. | ref-214, ref-215 | 아니오 | medium | 2026-10-09 | — | — |
| f17 | [사실] | IFC 4.3 문서의 IfcPropertySet 은 'Pset_' 접두어를 명세에 정의된 속성 세트에만 쓰고 사용자 정의 속성 세트는 이름에 넣지 않게 하며, 속성 세트는 개별 객체에는 IfcRelDefinesByProperties(역속성 DefinesOccurrence)로, 유형 객체에는 직접 연결(역속성 DefinesType)로 붙여 같은 유형의 모든 객체가 공유하게 한다. | ref-1426 | 아니오 | medium | 2026-10-09 | — | — |
| f18 | [사실] | buildingSMART 는 정보 전달 명세(Information Delivery Specification, IDS)를 정보 요구사항을 컴퓨터가 해석할 수 있는 형태로 정의해 IFC 모델의 자동 적합성 검사를 가능하게 하는 표준으로 소개하며, 2024-06-01 승인된 IDS 1.0 으로 객체·분류·재료·속성·값의 전달을 지정하게 하되 기하 정보는 다루지 않고, bSDD 를 IDS 작성 때 쓸 수 있는 공유 속성 라이브러리로 설명한다. | ref-1430 | 아니오 | medium | 2024-06-01 | — | — |
| f19 | [사실] | IDS 사용자 매뉴얼은 명세를 적용 대상(applicability)과 요구(requirements) 두 부분으로 나누고 둘 다 엔터티·속성(attribute)·분류·속성(property)·재료·부분(partOf) 패싯으로 구성하게 하며, 값 제한으로 열거·패턴(정규식)·범위·길이를 지원한다. | ref-1431, ref-1434 | 아니오 | medium | 2026-10-09 | — | — |
| f20 | [사실] | IDS 엔터티 패싯은 IFC 클래스 이름과 선택적 predefinedType 을 검사하며, predefinedType 에 표준 값뿐 아니라 사용자 정의 문자열도 쓸 수 있고, 객체의 PredefinedType 이 USERDEFINED 이면 ObjectType(유형 객체면 ElementType) 값을 읽어 대조하므로 USERDEFINED 와 ObjectType 으로 표현한 사용자 정의 유형도 납품 요구로 검사할 수 있다. | ref-1432 | 아니오 | medium | 2026-10-09 | — | — |
| f21 | [사실] | IDS 속성 패싯은 사용자 정의 속성 세트·속성을 허용하되 'Pset_'·'Qto_' 접두어는 표준 세트에만 쓰게 하고, 요구의 기수를 필수(REQUIRED)·선택(OPTIONAL)·금지(PROHIBITED)로 두며, 측정값은 SI 단위로 다루고 특정 단위를 요구할 수 없다. | ref-1433 | 아니오 | medium | 2026-10-09 | — | — |
| f22 | [사실] | 뉴질랜드 Masterspec 의 Open BIM Object standard(OBOS) V1.0 은 IFC4 Add2 에 맞는 IfcElementType 이 없는 객체를 IfcExportAs 를 IfcBuildingElementProxy 로, IfcExportType 을 USERDEFINED 로 내보내고 객체 유형을 설명하는 이름을 'ElementType' 속성에 넣도록 정하며, 이는 로봇 충전소를 대상으로 한 규정이 아니다. | ref-1435 | 아니오 | medium | 2026-10-09 | — | — |
| f23 | [사실] | Pauwels·de Koning·Hendrikx·Torta(Advanced Engineering Informatics 56, 101959, 2023-04)는 BIM 모델에서 건물 데이터 로컬 저장소를 거쳐 로봇으로 가는 RDF·JSON 데이터 흐름을 만들었고(연계 대상: 그 데이터로 대학 건물에서 표준 주행 스택으로 한 주행 시험), 건물 데이터 모델을 더 신뢰할 수 있게 표준화하려면 모델링 가이드라인과 로봇 세계 모델이 필요하다고 제시했다. | ref-1436 | 아니오 | medium | 2023-04 | 기타 / 작업 대상 | — |
| f24 | [추정] | q2-06 에 대해 확인한 규칙을 종합하면, IFC 4.3 에는 배터리 충전기 일반을 뜻하는 전기 저장 장치 유형 값 RECHARGER(공급 정격 전류만 담는 속성 세트, IFC4.3_ADD2 개발 문서)가 있어 로봇 충전기 본체의 표준 후보가 될 수 있으나 도킹 이름·접근 자세 같은 로봇 운영 정보는 표준 속성에 없으므로, 충전 위치·작업 스테이션의 운영 속성은 'Pset_' 접두어가 없는 프로젝트 속성 세트에 담고, 맞는 유형이 없을 때는 관련 엔터티나 IfcBuildingElementProxy 의 USERDEFINED·ObjectType 으로 유형을 나타내며, 이를 IDS 의 엔터티 패싯(사용자 정의 predefinedType)·속성 패싯(필수 기수)·값 제한으로 납품 요구로 적어 검사하는 경로가 표준이 허용하는 것으로 보이나, 로봇 충전소·작업 스테이션용 공개 IDS·속성 세트·bSDD 분류 관례나 실제 사례는 이번 검색 범위에서 찾지 못했다(부재 확인 아님). | ref-1427, ref-1429, ref-1428, ref-1426, ref-1425, ref-213, ref-1430, ref-1432, ref-1433, ref-1434, ref-1435, ref-1436 | 아니오 | low | 2026-10-09 | — | — |
| f25 | [추정] | 연계 대상: Robotics 24/7 기사(2025-03-12)는 AMR 현장 설정(commissioning)이 흔히 수개월의 수작업이 드는 병목이라고 서술하고, RGo Robotics 가 3D 비전 기반 지능형 지도 작성으로 현장 설정 기간을 수개월에서 며칠로 줄인다고 밝혔다고 전하나, 도면(CAD) 사용 언급은 없다. | ref-1437 | 아니오 | low | 2025-03-12 | 예외·성과 | 벤더 주장 |
| f26 | [추정] | q1-08 에 대해 이번 실행의 추가 검색(한국어 4회, 한국로봇산업진흥원 실증·국내 물류센터 도입 기사 대상 포함)에서도 국내 물류센터의 지도 작성·공용 자원 등록·제조사별 좌표 정렬 시간을 단계별로 공개한 공공·학술 자료를 찾지 못했고(부재 확인 아님), 새로 확인한 것은 해외 업체의 현장 설정 기간 단축 주장뿐이라 q1-08 은 여전히 부분적으로만 답할 수 있는 것으로 보인다. | ref-1437 | 아니오 | low | 2026-10-09 | 물류창고 / 예외·성과 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1012 | AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주) | 건축 도면 데이터 | 2023-07-26 | 정부·연구기관 | high | 2026-10-09 | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465 | 아니오 |
| ref-062 | CubiCasa (Kalervo, A. 외) | CubiCasa5k — README (CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis) | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/CubiCasa/CubiCasa5k | 아니오 |
| ref-213 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcTransportElement (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md | 아니오 |
| ref-214 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcOutletTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcOutletTypeEnum.md | 아니오 |
| ref-215 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcElectricApplianceTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcElectricApplianceTypeEnum.md | 아니오 |
| ref-1421 | AI Hub (한국지능정보사회진흥원) | AI 허브 이용정책 (데이터 이용정책) | 미확인 | 정부·연구기관 | high | 2026-10-09 | https://www.aihub.or.kr/intrcn/guid/usagepolicy.do?currMenu=151&topMenu=105 | 아니오 |
| ref-1422 | Zenodo (CubiCasa) | CubiCasa5k | 2019-03-28 | 오픈소스 문서 | high | 2026-10-09 | https://zenodo.org/record/2613548 | 아니오 |
| ref-1423 | CubiCasa (CubiCasa/CubiCasa5k GitHub) | CubiCasa5k — floortrans/loaders/house.py | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/CubiCasa/CubiCasa5k/blob/master/floortrans/loaders/house.py | 아니오 |
| ref-1424 | 경기도 고양시(공공데이터포털) | 경기도 고양시_어린이 음성맥락 인식률 향상을 위한 방송 음성 및 자연어 처리(AI학습용)_20240105 | 2025-08-16 | 정부·연구기관 | medium | 2026-10-09 | https://www.data.go.kr/data/15146382/fileData.do | 아니오 |
| ref-1425 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcBuildingElementProxy (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | 표준 | high | 2026-10-09 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcBuildingElementProxy.md | 아니오 |
| ref-1426 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcPropertySet (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | 표준 | high | 2026-10-09 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcKernel/Entities/IfcPropertySet.md | 아니오 |
| ref-1427 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcElectricFlowStorageDeviceTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | 표준 | high | 2026-10-09 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcElectricFlowStorageDeviceTypeEnum.md | 아니오 |
| ref-1428 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcElectricFlowStorageDevice (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | 표준 | high | 2026-10-09 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Entities/IfcElectricFlowStorageDevice.md | 아니오 |
| ref-1429 | buildingSMART International | Pset_ElectricFlowStorageDeviceTypeRecharger — IFC 4.3.2.0 documentation (IFC4X3_ADD2 development build) | 미확인 | 표준 | medium | 2026-10-09 | https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_ElectricFlowStorageDeviceTypeRecharger.htm | 아니오 |
| ref-1430 | buildingSMART International | Information Delivery Specification (IDS) | 미확인 | 표준 | high | 2026-10-09 | https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specification-ids/ | 아니오 |
| ref-1431 | buildingSMART (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/README.md | 미확인 | 표준 | high | 2026-10-09 | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/README.md | 아니오 |
| ref-1432 | buildingSMART (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/entity-facet.md | 미확인 | 표준 | high | 2026-10-09 | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/entity-facet.md | 아니오 |
| ref-1433 | buildingSMART (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/property-facet.md | 미확인 | 표준 | high | 2026-10-09 | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/property-facet.md | 아니오 |
| ref-1434 | buildingSMART (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/restrictions.md | 미확인 | 표준 | high | 2026-10-09 | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/restrictions.md | 아니오 |
| ref-1435 | Construction Information Limited (Masterspec, 뉴질랜드) | 4.0 Object Properties & Property Grouping — 4.3 IFC properties (Open BIM Object standard (OBOS) V1.0) | 미확인 | 업계 보고서 | medium | 2026-10-09 | https://masterspec.co.nz/43-IFC-Properties/7266/ | 아니오 |
| ref-1436 | Pauwels, P., de Koning, R., Hendrikx, B., & Torta, E. (Advanced Engineering Informatics 56, 101959) | Live semantic data from building digital twins for robot navigation: Overview of data transfer methods | 2023-04 | 논문 | medium | 2026-10-09 | https://research.tue.nl/en/publications/live-semantic-data-from-building-digital-twins-for-robot-navigati/ | 아니오 |
| ref-1437 | Robotics 24/7 | RGo Robotics introduces AI-powered Intelligent Mapping system | 2025-03-12 | 기사 | low | 2026-10-09 | https://www.robotics247.com/article/rgo-robotics-introduces-ai-powered-intelligent-mapping-system | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md | 2, 3, 4, 5, 6, 8, 9 | q2-04 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10 (신뢰도 medium) / q2-06 답: f11·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21·f22·f23·f24 (신뢰도 low) / q1-08 부분 답: f25·f26 — 2절 q2-04·q2-06 답함(답한 실행 2026-10-09-26, #q2-04·#q2-06), 3절 소제목 신설({#q2-04}: AI Hub 라벨·주거 구성·신청 조건 f1·f2·f3, 원 이용정책 f4 와 2차 기술 f5 를 나눠 적고 종합 f6(법적 판단 아님), CubiCasa5K 라이선스·코드상 원 범주와 학습 매핑 f7·f8·f9, 종합 f10 / {#q2-06}: 프록시·USERDEFINED·ObjectType f11·f12(IfcTransportElement 한정), 전기 저장 장치 RECHARGER 값과 속성 세트 f13·f14·f15(새 근거), 콘센트·전기기기 열거 f16, 사용자 정의 속성 세트 f17, IDS f18~f21, 실무 관례 f22(IFC4 Add2, 로봇 대상 아님), 연구 f23(연계 대상 표시), 종합 f24), q2-02 비교표 래스터 열 엘리베이터 칸을 f1(ref-1012)로 갱신하고 CubiCasa5K 계단 칸은 지우지 말고 '원 주석 범주 기준, 공식 학습 매핑에서는 계단 제외·계단실·엘리베이터는 일반 방'(f8) 병기, 충전 위치 칸에 RECHARGER 존재(f14) 병기, 4절 결론·불확실성, 5절 후속 질문, 6절 완료 조건(두 행 미충족, 전환 아니오), 8절 출처, 9절 이력. q1-08 본문은 단계 1 페이지에 싣는다. |
| update | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md | 2, 3, 8, 9 | 트랙 산출물 갱신: q1-08 부분 답: f25·f26 — 3절 {#q1-08} 소절에 해외 업체의 현장 설정 기간 단축 주장(f25, 벤더 주장·연계 대상, '수개월 수작업 병목'은 기사 서술과 구분)과 이번 추가 검색에서도 국내 단계별 시간 자료를 찾지 못했다는 점(f26) 추가, 2절 q1-08 상태는 조사 중 유지. |
| update | docs/ideas/floorplan-recognition.md | 3, 4 | 아이디어 페이지 3절: 공개 데이터셋 비교표 CubiCasa5K 행 '계단 있음, 엘리베이터 미확인'을 지우지 않고 원 주석 범주(Elevator·StairWell·Stairs)와 공식 학습 매핑 차이(f8)·라이선스 CC BY-NC-SA 4.0(f7) 병기, AI Hub 행 '엘리베이터·계단 미확인'·'접근 조건 미확인'을 f1·f2·f4 로 갱신(ref-1012·ref-1421, ref-074 새로 인용하지 않음). 아이디어 페이지 4절: BIM(IFC 4.3) 소절의 '충전 설비 값 없음' 문장 뒤에 전기 저장 장치 RECHARGER 값·속성 세트(f13·f14·f15)를 더하고, 표준 밖 운영 시설의 IFC 표현 경로와 IDS 납품 요구(f11·f17·f20·f21·f22, 종합 f24 추정) 소절 추가. |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | 2, 6 | 트랙 산출물 갱신: track.ontology_changes(충전 위치에 'BIM 표현(후보)' 속성: IfcElectricFlowStorageDevice RECHARGER 또는 USERDEFINED·ObjectType·프록시, 운영 속성은 Pset_ 접두어 없는 프로젝트 속성 세트)가 승인되면 2절 반영과 초안 v1.3 인상(f11·f13·f14·f15·f16·f17·f22). 6절 '로봇 충전소는 이번에 확인한 IFC 4.3 유형 값(개발 브랜치 기준)에 없어' 항목은 콘센트·전기기기 열거 기준이었음을 밝히고 RECHARGER 근거(f14·f15)와 IDS 납품 요구 방식(f24, 추정)을 근거 보강으로 덧붙임. |
| update | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md | 7, 8, 11 | 트랙 floorplan-recognition 단계 2 반영 제안 (f1, f3, f7, f8, f14, f17, f18, f20, f24): 7절에 IDS 1.0 과 IFC 프록시·사용자 정의 속성 세트·RECHARGER 유형 값을 BIM 입력 요구 수단으로, 8절에 AI Hub·CubiCasa5K 의 계단·엘리베이터 라벨과 라이선스, 11절에 oq-197 해결 근거(f1·f3). 반영은 다음 해당 영역 실행에서. |
| update | docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md | 8 | 트랙 floorplan-recognition 단계 2 반영 제안 (f1, f4, f6, f7, f8, f10): 교차 규칙(도면 해석은 14. 도면·BIM에서 지도 만들기에 적용)에 따라 도면 해석 학습 데이터의 클래스 구성(공식 학습 매핑에서 엘리베이터·계단실이 일반 방으로 합쳐짐)과 이용 조건(비상업 라이선스, AI허브 원 이용정책)을 45. 문서·도면·장면 이해와 14. 도면·BIM에서 지도 만들기 양쪽에 연결. |
| update | docs/categories/integration/interoperability-standards-and-conformance.md | 7 | 트랙 floorplan-recognition 단계 2 반영 제안 (f17, f18, f19, f20, f21, f22): IDS 1.0(2024-06-01 승인)의 패싯·값 제한·기수 구조와 IFC 사용자 정의 속성 세트 명명 규칙을 BIM 데이터 교환 요구·적합성 검사 수단으로. |
| update | docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md | 7 | 트랙 floorplan-recognition 단계 2 반영 제안 (f4, f5, f6, f7): 공공 AI 학습 데이터(AI허브)의 원 이용정책과 2차 기술의 차이, 비상업 라이선스(CC BY-NC-SA 4.0) 평면도 데이터셋의 상용 이용 제약을 학습 데이터 라이선스 사례로(법적 판단 아님). |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| buildingSMART 데이터 사전 | buildingSMART Data Dictionary (bSDD) | buildingSMART 가 정보 전달 명세(IDS)를 작성할 때 가져다 쓸 수 있는 공유 용어·속성 라이브러리로 설명하는 데이터 사전 서비스다. |
| 건물 요소 프록시 | Building Element Proxy (IfcBuildingElementProxy) | IFC 명세가 아직 정의하지 않았거나 응용이 의미 정의에 대응시킬 수 없는 건축 요소를 교환하는 IFC 엔터티로, PredefinedType 을 USERDEFINED 로 두면 ObjectType 으로 유형 이름을 적어야 한다. |
| 사용자 정의 속성 세트 | User-defined Property Set | IFC 명세에 선언되지 않은 프로젝트·조직 고유의 속성 묶음으로, 표준 세트에만 쓰는 'Pset_' 접두어 없이 이름을 짓고 IfcRelDefinesByProperties 나 유형 객체 연결로 객체에 붙인다. |

## 열린 질문

새로 생긴 질문:

- CubiCasa5K 원 SVG 주석에는 계단(Stairs)·계단실(StairWell)·엘리베이터(Elevator) 범주가 실제로 몇 개 들어 있으며, 공식 학습 매핑이 이를 일반 방으로 합치거나 빼는 상태에서 기존 위키의 'CubiCasa5K 계단 라벨 있음' 서술은 원 주석 범주 기준으로 고쳐 써야 하는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해 | 근거: f8 | 종류: 일반
- AI허브 원 이용정책은 학습 모델의 배포·상업적 이용을 직접 말하지 않고 '학습용으로만'과 '영리·비영리 연구개발 활용'을 함께 적는데, 건축 도면 데이터로 학습한 도면 인식 모델을 상용 서비스로 배포하는 것이 허용되는지와 데이터셋별 별도 조건이 있는지를 운영기관 확인으로 정할 수 있는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 59. 법·규제·보험·라이선스 | 근거: f6 | 종류: 일반
- 국내 공공건축 BIM 납품 기준(건설산업 BIM 시행지침 등)이나 로봇 친화형 건축물 인증이 로봇 충전 공간·작업 스테이션을 BIM 객체·속성으로 납품하도록 요구하거나 그 IDS·속성 세트를 정한 사례가 있는가? (관련 기존 질문: oq-199) | 관련 영역: 14. 도면·BIM에서 지도 만들기, 21. 상호운용 표준·적합성 | 근거: f24 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- oq-197

## 자체 점검

- 출처 수: 22 · 교차 확인: 0
- 예산 사용량: 검색 10회 · 신규 출처 17건
- 미확인 항목:
    - q1-08 부분 답: 국내 물류센터의 지도 작성·공용 자원 등록·좌표 정렬 단계별 소요 시간 공개 자료 여전히 없음(이번 한국어 검색 4회 포함)
    - AI허브 이용정책 페이지의 발행일·판 미확인, 건축 도면 데이터에 데이터셋별 별도 이용 조건이 있는지 미확인
    - CubiCasa5K 원 SVG 주석의 계단·엘리베이터 실제 주석 개수 미확인(코드 범주 기준 관찰), arXiv 논문 PDF 는 바이너리라 본문 미열람
    - Pset_ElectricFlowStorageDeviceTypeRecharger 는 IFC4.3 ADD2 개발 빌드(작업 초안) 문서이며 게시판 IFC 4.3 ADD2 공식판 포함 여부 미확인
    - 로봇 충전소·작업 스테이션용 공개 IDS·속성 세트·bSDD 분류 사례는 이번 검색 범위에서 찾지 못함(부재 확인 아님), 작업 스테이션에 대응하는 IFC 유형 값은 조사하지 않음
    - eCAADe 2025 KIT 예고 논문(JuBot)은 KIT 서지 검색에서 다른 논문(BIM-LCA)만 확인되어 제목·저자를 확인하지 못해 출처로 쓰지 않음
    - ref-1436 Pauwels 외는 초록만 열람
    - 모든 finding 교차 확인 없음(단일 출처 또는 이 위키의 종합)
- 범위 경계 위반 의심:
    - f25: 3D 비전 기반 지도 작성은 분류 원문 19장 '로봇 자체 지능·제어' 연계 영역이라 '연계 대상: '으로 표시하고 현장 설정 기간 주장 근거로만 씀(벤더 주장)
    - f23: BIM 기반 주행 시험은 로봇 쪽 연계 대상으로 괄호 안에 표시하고, BIM→로봇 데이터 흐름과 모델링 가이드라인 필요성만 ROP 근거로 씀
    - f13~f15: 충전기 전기 설비 자체(충전 제어)는 시설·설비 제어 쪽이며, BIM 에서 충전 위치를 표현·식별하는 수단으로만 씀
- 한계: 트랙 실행(단계 2), web_fetch_available: true · fetch_mode full. 검색 10회/40, 신규 출처 17건/20(ref-1421~ref-1437, 예약 구간 안), 재사용 5건(ref-1012 webfetch 재열람, ref-062·ref-214·ref-215 github_raw 재열람, ref-213 inbox 원문). 같은 세 질문을 다룬 보류 실행 2026-10-09-24 의 브리프와 그 1차 검증 수정 지시를 출발점으로 원문을 다시 열어 확인했다. 보류 실행의 출처 id(ref-1427~ref-1438)는 참고문헌 목록에 없고 이번 예약 구간과 겹쳐 새 id 로 다시 부여했다(같은 URL 이면 퍼블리셔가 합침). 1차 검증 수정 지시 반영: eCAADe 2025 근거 삭제(재확인 시도 실패), f9→f10 의 '상용 쓸 수 없음'을 '권리자 별도 허락 필요(법적 판단 아님)'로, 이용정책 링크 표현 수정(f2), 공공데이터포털 기준일은 원문에서 수정일 2026-06-16 을 확인해 as_of 로 씀(f5), IfcPropertySet 연결 표현을 원문(DefinesOccurrence·DefinesType)으로(f17), IfcTransportElement 제약은 한 엔터티로 한정(f12), OBOS 는 IFC4 Add2·로봇 대상 아님 명시(f22), Pauwels 주행 시험은 연계 대상 표시·디지털 트윈은 건물 데이터 저장소 의미(f23), RGo 기사 서술과 벤더 주장 구분(f25). 새로 더한 근거: AI허브 원 이용정책 열람(f4, 보류 실행에서는 열람 실패), IFC 4.3 전기 저장 장치 RECHARGER 값·속성 세트(f13~f15 — 기존 위키의 '충전 설비 값 없음'은 콘센트·전기기기 열거 두 개 기준이었음), IDS 엔터티 패싯의 USERDEFINED·ObjectType 대조와 속성 패싯 기수·값 제한(f19~f21). 질문 선택: target.json 지정 q1-08(되돌아온 단계 1 질문)·q2-04·q2-06. 답한 질문: q2-04(클래스·이용 조건 모두 원문 확인, 종합은 low), q2-06(표준 규칙은 원문, 로봇 운영 시설용 관례·사례는 찾지 못해 종합 low). q1-08 은 새 국내 근거가 없어 부분 답으로 두고 answered_question_ids 에서 뺐다. oq-197 해결 근거: f1·f3(AI Hub 라벨에 충전 위치 같은 로봇 운영 클래스 없음, 도면 48,033장 모두 주거 유형). CubiCasa5K 계단 라벨 서술 충돌은 공식 코드가 원 주석 범주(Stairs·StairWell·Elevator)를 읽으면서 학습 매핑에서 합치거나 뺀다는 점(f8)으로 '수준 차이'로 설명되어 출처 충돌이 아닌 일반 열린 질문(실제 주석 개수)으로 올렸다. 한국 자료: AI Hub 데이터셋 페이지·이용정책(ref-1012·ref-1421), 공공데이터포털(ref-1424). 교차 규칙: 학습 데이터 근거(f1·f7·f8·f10)는 45. 문서·도면·장면 이해와 14. 도면·BIM에서 지도 만들기 양쪽에 반영 제안. 18. 실시간 세계 상태·데이터 일관성·34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음(f23 의 디지털 트윈은 건물 데이터 저장소 의미로만 인용). 정정 요청 없음. 입력 누락 없음. 후속 질문 3건. 온톨로지 변경 1건 제안(충전 위치 'BIM 표현(후보)' 속성). 페이지 제안: 트랙 산출물 4건(단계 2·단계 1 페이지, 아이디어 페이지, 스키마 초안), 세부영역 반영 제안 4건(갱신 상한과 별도).

## 트랙 블록

- 트랙: floorplan-recognition · 단계: 2
- 답한 질문 id: q2-04, q2-06

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | ROP 가 BIM 납품 요구로 쓸 로봇 운영 시설용 IDS(충전 위치는 IfcElectricFlowStorageDevice RECHARGER 또는 관련 엔터티·IfcBuildingElementProxy 의 USERDEFINED·ObjectType 값으로, 작업 스테이션은 대응 유형을 정한 뒤, 'Pset_' 가 아닌 프로젝트 속성 세트에 접근 자세·도킹 이름·상호작용 노드 속성을 REQUIRED 로 요구하는 형태)를 어떤 항목으로 정의하며, 설계·시공 측이 그 값을 채울 수 있는가, 채울 수 없으면 어느 단계에서 누가 보완하는가? (q2-06 에서 파생) | 3 | f24 |
| — | 로봇 충전기를 IFC 4.3 의 전기 저장 장치 유형 값 RECHARGER(배터리 충전기 일반 정의, 속성은 공급 정격 전류뿐)로 표현할지 USERDEFINED·ObjectType 으로 표현할지 정하는 기준은 무엇이며, 실무 IFC 모델에서 로봇·차량 충전기가 실제로 어느 쪽으로 내보내지는가? (q2-06 에서 파생) (관련: q2-09) | 2 | f14 |
| — | AI Hub 건축 도면 데이터의 엘리베이터·엘리베이터홀·계단실 라벨(아파트 코어 기준)로 학습한 모델이 물류센터·병원 같은 비주거 도면의 화물용 승강기·계단실을 얼마나 인식하는가, 라벨 정의서는 계단실과 엘리베이터 영역을 어떤 기준으로 그리는가? (q2-04 에서 파생) (관련: q2-10, oq-341) | 2 | f1 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 충전 위치 (Charging Location) | f11, f13, f14, f15, f16, f17, f22 | 속성 'BIM 표현(후보)'을 더한다: 후보 1) IFC 4.3 전기 저장 장치 IfcElectricFlowStorageDevice 의 PredefinedType RECHARGER(배터리 충전기 일반 정의, 차량·로봇 언급 없음, 속성 세트 Pset_ElectricFlowStorageDeviceTypeRecharger 는 공급 정격 전류만 담는 IFC4.3_ADD2 개발 문서, f13·f14·f15), 후보 2) 맞는 유형이 없을 때 관련 엔터티 또는 IfcBuildingElementProxy 의 USERDEFINED 와 ObjectType 값(f11, 실무 관례 f22, 콘센트·전기기기 열거에는 충전 값 없음 f16). 도킹 이름·접근 자세 같은 운영 속성은 'Pset_' 접두어가 없는 프로젝트 속성 세트(f17). 기존 속성(위치·수·접근 지점)과 충돌하지 않는다. 기존 6절 '로봇 충전소는 IFC 4.3 유형 값에 없어' 항목은 콘센트·전기기기 열거 기준이었으므로 RECHARGER 근거로 보강이 필요하다. IDS 납품 요구 방식(f24)은 추정이라 정의에 넣지 않고 6절 질문으로 둔다. 작업 스테이션에는 적용하지 않는다(대응 유형 미조사). |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 표준과 대응시킨 관계(엣지) 유형이 공간 그래프 스키마 초안의 관계 목록 표에 없음
    - q2-04·q2-06 답은 검증 승인 전이며 아이디어 3. 건축 도면 자동 인식 4절에 아직 반영되지 않음
    - 단계 2 열린 질문 q2-07·q2-08·q2-09·q2-10 미답
    - 되돌아온 단계 1 질문 q1-08 부분 답으로 남음
```

### runs/2026-09-25-61/research.md

```markdown
# 리서치 브리프 2026-09-25-61

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-61 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 24. 자산·소프트웨어 수명주기 관리 |
| 대분류 | F. 도입·검증·유지관리 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(예지보전·상태 기반 정비, 배터리 건강 상태, 소프트웨어 명판, 패치 관리, 지도 버전)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음(상태 감시·고장 예측, 배터리 열화 인지 배정, OTA 배포·롤백, 관리형 노드)
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(대상 영역에 걸린 열린 질문 0건, 정정 요청 0건)

## 조사 질문

1. 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]
2. 로봇 상호운용 규격(VDA 5050, MassRobotics AMR 상호운용 표준)은 펌웨어·소프트웨어·지도 버전과 배터리 건강 상태를 어떤 필드로 보고하며, 버전 호환성 규칙은 무엇인가? (섹션 4·6·7 겨냥)
3. 고장 예측·정비(상태 감시, 예지보전)와 자산 관리의 표준·대표 연구는 무엇인가(ISO 17359, ISO 55000, 산업용 로봇 상태 감시 검토 논문)? (섹션 3·7·8 겨냥)
4. 배터리 열화를 플릿 운영(작업 배정·충전)에 반영하는 접근은 무엇인가? (섹션 5·6 겨냥)
5. 로봇 소프트웨어 배포·복구(무선 업데이트, 롤백, 관리형 노드, 배포판 지원 종료)와 패치 관리 표준은 무엇인가? (섹션 6·7 겨냥)
6. 펌웨어·설정 변경이 안전 재평가·규제상 '실질적 변경'에 해당하는 조건은 무엇이며 한국 인증 제도는 어떻게 다루는가? (섹션 3·9·11 겨냥, 한국 자료 우선)
7. ROP 가 직접 맡을 수명주기 관리 범위와 제조사·설비에 맡길 범위는 어떻게 나뉘는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 은 지도를 지도 식별자(mapId)와 지도 버전(mapVersion)의 조합으로 식별하고, 즉시 동작 downloadMap·enableMap·deleteMap 으로 지도 내려받기·활성화·삭제를 지시하며, 같은 mapId 에서는 한 번에 한 버전만 활성화되게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 은 의미적 버전 체계를 써서 주 버전 변경은 새 필수 필드 도입 같은 호환성을 깨는 변경, 부 버전은 기능 추가, 수 버전은 작은 수정으로 규정하고, MQTT 토픽 경로에 주 버전(v3 등)을 넣는다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f3 | [사실] | VDA 5050 3.0.0 에서 로봇이 사용할 수 없는 선택 필드가 담긴 주문을 받으면 오류 유형 UNSUPPORTED_PARAMETER 를 수준 CRITICAL 로 보고하도록 되어 있어, 판 차이로 생긴 미지원 기능이 실행 시점 오류로 드러난다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f4 | [사실] | VDA 5050 팩트시트 스키마는 mobileRobotConfiguration.versions 배열에 로봇에서 도는 하드웨어·소프트웨어 버전(예: softwareVersion)을 키–값으로 담고, batteryCharging 블록에 임계 저충전 수준·희망 최소·최대 충전 수준·최소 충전 시간을 담는다. | ref-228 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | VDA 5050 상태(state) 스키마는 전원 정보로 충전 상태(stateOfCharge), 원래 용량 대비 배터리 상태(batteryHealth), 충전 중 여부, 현재 충전 상태로 갈 수 있는 추정 거리(range)를, 지도 정보로 mapId·mapVersion·mapStatus 를 로봇이 보고하게 한다. | ref-051 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f6 | [추정] | MassRobotics AMR 상호운용 표준 JSON 스키마는 제조사명·모델·일련번호, 배터리 잔량 비율, 남은 가동 시간, 오류 코드 목록을 담지만 소프트웨어·펌웨어 버전 필드는 명시적으로 두지 않은 것으로 보인다. | ref-230 | 아니오 | medium | 2026-09-25 | — | — |
| f7 | [추정] | VDA 5050 은 소프트웨어 버전을 팩트시트에, 지도 버전을 상태 메시지에 두지만 MassRobotics 스키마는 버전 필드가 없어, 여러 규격이 섞인 플릿에서는 ROP 가 로봇별 버전 목록을 별도로 유지해야 할 것으로 보인다. | ref-228, ref-051, ref-230 | 아니오 | low | 2026-09-25 | — | — |
| f8 | [사실] | ROS 2 관리형 노드 설계는 미구성·비활성·활성·종료의 네 주 상태와 구성·활성화·비활성화·정리·종료 전이를 두어, 실행 전에 구성 요소가 올바로 초기화됐는지 확인하고 실행 중 노드를 교체·재시작할 수 있게 한다. | ref-364 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | ROS 2 배포판 지원 정책(REP 2000)에 따르면 장기 지원판은 5년, 비장기 지원판은 1.5년 지원되며, Humble 은 2022-05~2027-05, Jazzy 는 2024-05~2029-05, Kilted 는 2025-05~2026-11 이 지원 기간이다. | ref-752 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | rmf_simulation 저장소는 지원 대상으로 Gazebo Classic 11(지원 2025년 1월 종료)과 Gazebo Fortress 를 적어, 오케스트레이션 검증용 시뮬레이션 환경도 시뮬레이터 판 교체에 따른 수명주기 관리 대상이다. | ref-523 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f11 | [사실] | IDTA 02007 소프트웨어 명판(Nameplate for Software in Manufacturing) 서브모델은 업데이트·패치 관리·라이선스 관리·감사를 위해 소프트웨어 제품과 설치 인스턴스 정보를 통일된 형태로 표현하며, 버전(주·부·개정·빌드), 배포일·빌드일·설치일, 설치 경로·체크섬, 설치된 버전과 구성 경로 같은 속성을 둔다. | ref-753 | 아니오 | medium | 2026-09-25 | — | — |
| f12 | [사실] | ISO 17359:2018 은 기계의 상태 감시 프로그램을 세울 때의 일반 절차 지침을 주며, 진동·온도·유량·오염·전력·속도 같은 변수를 쓰고 상태 감시·진단 표준군의 상위 문서 역할을 한다. | ref-754 | 아니오 | medium | 2018 | — | 원문 미열람 |
| f13 | [사실] | ISO 55000:2024(제2판, 2024년 7월, ISO/TC 251)는 자산 관리의 개요·원칙·용어를 정하고 ISO 55000:2014 를 대체하며, 자산에 하드웨어·소프트웨어·설비를 포함하고 수명주기 단계별로 자산의 필요와 성능을 평가하게 한다. | ref-755 | 아니오 | medium | 2024-07 | — | 원문 미열람 |
| f14 | [사실] | Lei 외(2025)의 검토 논문은 산업용 로봇의 고장 모드와 근본 원인, 데이터 수집 전략과 센서, 모델 기반·데이터 기반 상태 감시·고장 진단 기술을 상태 기반 정비 구현 관점에서 정리했다. | ref-757 | 아니오 | medium | 2025 | — | 원문 미열람 |
| f15 | [사실] | 2026년 3월 arXiv 프리프린트 'Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots'는 작업 배정·서비스 순서·충전 여부·충전 모드·충전기 접근을 함께 최적화해 플릿 전체의 배터리 열화를 균형 있게 나누는 정식화를 제안했고, 급속 충전에 따른 사이클 열화와 높은 충전 상태로 대기할 때의 달력 열화를 근사 열화 지표로 반영했다. | ref-403 | 아니오 | medium | 2026-03 | 수행 자원 | 원문 미열람 |
| f16 | [사실] | IEC TR 62443-2-3:2015 는 산업 자동화·제어 시스템의 패치 관리 프로그램을 운영하는 자산 소유자와 제품 공급자에 대한 요구를 기술하고, 공급자–소유자 간 패치 정보 교환 형식과 패치 개발·배포·설치 활동을 정의하며, 보안 외 패치·업데이트에도 적용될 수 있다고 적는다. | ref-758 | 아니오 | medium | 2015-06 | — | 원문 미열람 |
| f17 | [사실] | EU 기계 규정 (EU) 2023/1230 은 2027-01-20 부터 적용되며, 시장에 나온 기계에 대한 물리적 또는 디지털 변경이 새 위험을 만들거나 기존 위험을 키워 새 보호 조치가 필요하면 '실질적 변경'으로 정의해, 동작을 바꾸는 소프트웨어 업데이트가 이 판단 대상이 될 수 있다. | ref-759 | 아니오 | medium | 2023-06 | — | 원문 미열람 |
| f18 | [추정] | AWS 샘플 저장소의 ROS 2 플릿 무선 펌웨어 업데이트 참조 구현은 IoT Jobs·Greengrass v2·Docker 로 배포를 지시·추적하고 플릿 색인으로 기기별 펌웨어 버전을 조회하며, 실패한 업데이트를 이전의 검증된 버전으로 자동 복귀시킨다고 밝히지만 운영용이 아닌 참조 구현이다. | ref-760 | 아니오 | low | 2026-09-25 | — | 벤더 주장 |
| f19 | [사실] | 2026-07-22 판교에서 열린 SDR(Software Defined Robot) 차세대 로봇 공통 플랫폼 기술개발 3차년도 착수 워크숍에서 KIST 휴머노이드연구센터가 클라우드 기반 SDR 공통 서비스 프레임워크를 소개했고, 이 플랫폼은 무선 업데이트(OTA)로 로봇 소프트웨어를 갱신하고 기능을 추가하는 것을 목표로 한다고 보도됐다. | ref-761 | 아니오 | low | 2026-07-23 | — | 원문 미열람 |
| f20 | [의견] | 국내 로봇 안전 컨설팅 업체의 위험성평가 가이드는 같은 모델로 교체해도 제어기 펌웨어 버전·안전 기능 파라미터·엔드이펙터 재장착에 따른 정밀도가 달라질 수 있어 기존 위험성평가의 조건 변경에 해당하므로 변경 범위 재평가와 검증 문서 갱신이 필요하다고 권고한다. | ref-763 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f21 | [사실] | 한국로봇사용자협회의 협동로봇 설치 작업장 안전인증은 협동운전 산업용 로봇 시스템이 ISO 10218-2 를 준수하는지 심사하며, 인증서 발급일로부터 2년 주기로 정기 심사한다. | ref-762 | 아니오 | low | 2026-09-25 | 제약 | 원문 미열람 |
| f22 | [추정] | 분류 원문 질문 '제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까?'에 대해, 확인한 자료로는 로봇별 소프트웨어 버전(VDA 5050 팩트시트 versions, 소프트웨어 명판)을 그 로봇이 쓰이는 현장·기능과 연결해 두고, 규격 주 버전 변경·팩트시트 기능 선언 변화·안전 파라미터 변화·지도 버전 변화를 재검증 촉발 조건으로 삼는 방식이 가능해 보이지만, 이 영향 범위 산정을 규정한 공개 절차는 찾지 못했다. | ref-031, ref-228, ref-753, ref-763 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f23 | [추정] | ROP 가 직접 맡을 수명주기 관리 몫은 로봇·어댑터·지도·모델의 버전 목록 유지, 로봇이 보고하는 배터리 상태·오류를 배정·충전 계획에 반영, 업데이트를 운영 시간대·일부 로봇 단위로 나눠 배포하고 실패 시 복구를 조율, 지도 버전 활성화 시점 동기화로 보인다. | ref-031, ref-051, ref-364, ref-760 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f24 | [추정] | 연계 대상: 펌웨어 내용 자체, 관절·감속기 같은 기계 부품의 고장 진단·잔여 수명 예측, 배터리 관리 시스템(BMS) 내부의 열화 추정은 로봇 제조사·설비 쪽 영역이고, ROP 는 그 결과(배터리 상태 값·오류 코드·정비 필요 신호)를 받는 쪽으로 보인다. | ref-757, ref-051, ref-230 | 아니오 | low | 2026-09-25 | — | — |
| f25 | [추정] | 출하 마감 전 집중 시간대에 배터리 상태(batteryHealth)가 낮아진 로봇은 같은 충전 상태에서도 추정 도달 거리(range)가 짧아질 수 있어, 배터리 열화가 작업 배정·충전 계획의 제약으로 작용하는 것으로 보인다. | ref-051, ref-403 | 아니오 | low | 2026-09-25 | 출하 / 제약 | — |
| f26 | [추정] | 적치 구역의 랙 배치가 바뀌면 플릿 제어가 새 mapVersion 을 로봇에 내려받게 한 뒤 enableMap 으로 전환해야 하고, 같은 mapId 에 한 버전만 활성화되므로 전환 시점과 진행 중 주문의 정리가 적치 작업 재개의 시작 조건이 되는 것으로 보인다. | ref-031 | 아니오 | low | 2026-09-25 | 적치 / 시작 조건 | — |
| f27 | [의견] | 24. 자산·소프트웨어 수명주기 관리는 업데이트 뒤 회귀·장애 시험(23. 시험·형식 검증·벤치마크), 시뮬레이션 환경의 판 관리(22. 시뮬레이션·예측용 디지털 트윈), 보안 패치(26. 사이버보안·접근권한·개인정보), 변경 후 안전 재평가(25. 안전·위험 관리), 배터리 열화를 반영한 충전(16. 공용 자원·충전·에너지 최적화)과 맞물리는 것으로 보인다. | ref-523, ref-758, ref-403, ref-763 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-364 | Open Robotics (ROS 2 Design) | Managed nodes (ROS 2 Design: node_lifecycle) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://design.ros2.org/articles/node_lifecycle.html | 아니오 |
| ref-752 | Open Robotics (ROS REP) | REP 2000 -- ROS 2 Releases and Target Platforms | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://www.ros.org/reps/rep-2000.html | 아니오 |
| ref-753 | IDTA (admin-shell-io/id GitHub) | IDTA SoftwareNameplate 1/0 — README (Nameplate for Software in Manufacturing) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/id/blob/master/idta/SoftwareNameplate/1/0/README.md | 아니오 |
| ref-754 | ISO | ISO 17359:2018 - Condition monitoring and diagnostics of machines — General guidelines | 2018 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/71194.html | 예 |
| ref-755 | ISO | ISO 55000:2024 - Asset management — Vocabulary, overview and principles | 2024-07 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83053.html | 예 |
| ref-403 | arXiv (저자 미확인) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 2026-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2603.22731 | 예 |
| ref-757 | Lei, Y., Liu, H., Li, N. 외 | Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301) | 2025 | 논문 | medium | 2026-09-25 | https://link.springer.com/article/10.1007/s11431-024-2810-2 | 예 |
| ref-758 | IEC | IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment | 2015-06 | 표준 | medium | 2026-09-25 | https://webstore.iec.ch/en/publication/22811 | 예 |
| ref-759 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 2023-06 | 정부·연구기관 | medium | 2026-09-25 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 예 |
| ref-760 | Amazon Web Services (aws-samples GitHub) | ros2-ota-firmware-updates — README | 미확인 | 벤더 문서 | low | 2026-09-25 | https://github.com/aws-samples/ros2-ota-firmware-updates | 아니오 |
| ref-761 | 네이트 뉴스(원 매체 미확인) | 클라우드 기반 OTA로 로봇이 진화하다…2026 SDR 과제 킥오프 워크숍 현장 | 2026-07-23 | 기사 | low | 2026-09-25 | https://m.news.nate.com/view/20260723n24828 | 예 |
| ref-762 | 한국로봇사용자협회 | 협동로봇 설치 작업장 안전인증 안내 | 미확인 | 업계 보고서 | medium | 2026-09-25 | https://www.korua.or.kr/inspect/inspectInfo.do | 예 |
| ref-763 | 세이프틱스(Safetics) | 로봇 시스템 위험성평가 가이드 | 미확인 | 벤더 문서 | low | 2026-09-25 | https://doc.safetics.io/insight-risk-assessment/ | 예 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-523 | Open Robotics (open-rmf) | rmf_simulation — README | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_simulation | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절 왜 중요한가: f17(디지털 변경도 실질적 변경 판단 대상), f9(배포판 지원 종료), f22(분류 원문 질문 — 추정) / 4절 핵심 개념: f13(자산·수명주기), f12(상태 감시), f5(배터리 상태), f11(소프트웨어 명판), f16(패치 관리), f1(지도 버전) / 5절 현장 시나리오: f26(적치·시작 조건), f25(출하·제약), f20·f21(교체 후 재평가, 의견·국내 제도) / 6절 대표 접근법: f14(상태 감시·고장 진단), f15(열화 인지 스케줄링), f8(관리형 노드), f18(OTA·롤백, 벤더 주장 병기), f19(국내 SDR 과제) / 7절 표준·오픈소스: f1~f5(VDA 5050), f6(MassRobotics), f11(IDTA 02007), f12·f13·f16·f17, f9·f10 / 8절 대표 연구: f14·f15 / 9절 경계: f23(ROP 직접), f24('연계 대상') / 10절 연결: f27(23. 시험·형식 검증·벤치마크, 22. 시뮬레이션·예측용 디지털 트윈, 26. 사이버보안·접근권한·개인정보, 25. 안전·위험 관리, 16. 공용 자원·충전·에너지 최적화), f7·f4(21. 온보딩·설정·현장 시운전, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스), f26(6. 지도·공간·위치 모델) / 11절: open_questions_new 4건. 벤더 주장 f18 은 [추정]+'벤더 주장', f20 은 [의견]. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 예지보전 | Predictive Maintenance (PdM) | 설비의 상태 데이터로 고장 시점을 예측해 고장 전에 정비를 계획하는 정비 방식이다. |
| 상태 기반 정비 | Condition-Based Maintenance (CBM) | 정해진 주기 대신 상태 감시로 확인한 설비 상태에 따라 정비 여부와 시점을 정하는 정비 방식이다. |
| 배터리 건강 상태 | State of Health (SOH) | 배터리의 현재 용량·성능을 새 배터리 대비 비율로 나타낸 값으로, VDA 5050 상태 메시지의 batteryHealth 가 이에 해당한다. |
| 소프트웨어 명판 | Software Nameplate (IDTA 02007) | 자산관리셸에서 소프트웨어 제품과 설치 인스턴스의 식별·버전·설치 정보를 통일된 형태로 기술하는 서브모델이다. |
| 무선 업데이트 | Over-the-Air Update (OTA) | 기기를 회수하지 않고 네트워크로 소프트웨어·펌웨어를 내려받아 갱신하는 방식이다. |

## 열린 질문

새로 생긴 질문:

- 제조사 펌웨어가 바뀔 때 어느 현장·기능을 다시 검증할지 영향 범위를 산정하는 공개 절차나 표준이 있는가? | 관련 영역: 24. 자산·소프트웨어 수명주기 관리, 23. 시험·형식 검증·벤치마크 | 근거: f22 | 종류: 일반
- VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가? | 관련 영역: 24. 자산·소프트웨어 수명주기 관리, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f2 | 종류: 일반
- 국내 협동로봇 설치 작업장 안전인증에서 제어기 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정으로 확인할 수 있는가? | 관련 영역: 24. 자산·소프트웨어 수명주기 관리, 25. 안전·위험 관리 | 근거: f21 | 종류: 일반
- EU 기계 규정의 실질적 변경 판단이 로봇 동작을 바꾸는 오케스트레이션 정책·어댑터 업데이트에도 적용되는가? | 관련 영역: 24. 자산·소프트웨어 수명주기 관리, 25. 안전·위험 관리 | 근거: f17 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 0
- 예산 사용량: 검색 17회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처)
    - f6: MassRobotics 스키마의 버전 필드 부재는 요약 판독 기준이라 추정으로 둠
    - f17: EU 2023/1230 조문 원문 미열람, 제조사가 예정한 업데이트의 취급은 2차 해설에만 있어 finding 에서 제외
    - f19: 원 매체와 SDR 과제 공식 자료 미확인
    - f20·f21: 검색 요약 문장의 출처 귀속(세이프틱스/한국로봇사용자협회)을 원문으로 확인하지 못함
    - ref-403 저자, ref-031·ref-051·ref-753 발행일 미확인
    - f22: 펌웨어 변경 영향 범위 산정 공개 절차 찾지 못함
- 범위 경계 위반 의심:
    - f24: 감속기·관절 진단, BMS 내부 열화 추정은 분류 원문 9장 '로봇 자체 지능·제어' 쪽이므로 '연계 대상:'으로 표시
    - f14·f15: 부품 진단·열화 모델 연구는 ROP 가 결과를 받아 쓰는 근거로만 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: ref-031·ref-051·ref-364·ref-752·ref-753·ref-760 과 재사용 ref-228·ref-230. 나머지는 검색 요약 기준(신뢰도 상한 medium). 검색 17회/30, 신규 출처 15건/15(ref-031~ref-763, 예약 구간 안) — 신규 출처 예산에 도달해 ISO 13374, ISO 10218-1:2025(사이버보안 요구 추가), CISA SBOM, ICAN-Deploy(카나리 배포 프리프린트)는 출처로 넣지 않음. 재사용 3건: ref-228·ref-230(2026-09-25-57 브리프 값), ref-523(2026-09-25-56 브리프 값, 이번에 다시 열지 않음). 교차 확인 0건. 한국 자료: 한국로봇사용자협회 안전인증(ref-762), 세이프틱스 가이드(ref-763, 의견), SDR 과제 보도(ref-761). 27. AI·학습·적응과 모델 운영 관련 finding 없음(모델 버전 관리는 일반 수명주기 관점으로만 다룸). 8·22 구분: f10 은 시뮬레이션 환경의 판 관리로만 서술. 정정 요청 없음, 대상 영역 열린 질문 0건.
```

### data/source_texts/ref-023.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
## Workcells

Currently RMF has 2 types of sample workcells, namely: `Dispenser` and `Ingestor`.

| Message Types | ROS2 Topic | Description |
|---------------|------------|-------------|
| `rmf_dispenser_msgs/DispenserRequest` | `/dispenser_reqeusts` | Direct requests subscribed by the dispenser node |
| `rmf_dispenser_msgs/DispenserResult` | `/dispenser_results` |  Result of a dispenser request, published by the dispenser  |
| `rmf_dispenser_msgs/DispenserState` | `/dispenser_states` |  State of the dispenser published by the dispenser periodically |
| `rmf_ingestor_msgs/IngestorRequest` | `/ingestor_requests` |  Direct requests subscribed by the ingestor node |
| `rmf_ingestor_msgs/IngestorResult` | `/ingestor_results` |  Result of a ingestor request, published by the ingestor |
| `rmf_ingestor_msgs/IngestorState` | `/ingestor_states` |  State of the dispenser published by the ingestor periodically |

In `rmf_demos` world, both `TeleportDispenser` and `TeleportIngestor`
[plugins](https://github.com/open-rmf/rmf_simulation/tree/main/rmf_robot_sim_gz_plugins/src) act as workcell adapter nodes.

Workcells currently work alongside with Delivery Task. In `fleet_adapter.lauch.xml`,
`perform_deliveries` needs to be `true` for the robot to accept a delivery task.

A Full Delivery:
1) The robot will first move to the `pickup_waypoint`
2) Requests a `DispenserRequest` till receives a `DispenserResult`. (Done Dispensing)
3) Continue delivery and moves to `dropoff_waypoint`
4) Requests a `IngestorRequest` till receives a `IngestorResult`. (Done Ingesting)
```

### data/source_texts/ref-031.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
![logo](./assets/logo.png)

# Interface for the Communication between Mobile Robots and a Fleet Control

## VDA 5050

## Version 3.0.0

![Fleet control system and mobile robots](./assets/csagv.png)

# Disclaimer
The following explanations are intended to provide guidance for implementing an interface that enables communication between mobile robots and a fleet management system. They are intended to be freely accessible to all users and are non-binding. Any party choosing to apply these guidelines is responsible for ensuring their correct and appropriate use in each specific case.
Users must consider the applicable state of the art at the time the guidelines are applied. The use of these proposals does not relieve any party of responsibility for its own actions. These statements do not claim to be exhaustive, nor do they constitute an authoritative interpretation of existing laws. They do not replace the need to review and comply with relevant policies, legislation, or regulations.
In addition, the specific characteristics of the respective products and their various potential applications must be considered. All users act at their own risk. Any liability on the part of the VDA and VDMA or any individuals involved in the development or application of these proposals is excluded.
If you identify any inaccuracies in the application of these proposals or potential risks of misinterpretation, please notify the VDA immediately so that any necessary corrections can be made.

**Publisher**
Verband der Automobilindustrie e. V. (VDA)
Behrenstraße 35, 10117 Berlin,
Germany
www.vda.de

**Copyright**
Association of the Automotive Industry (VDA)
Reproduction and any other form of reproduction is only permitted with specification of the source.

Version 3.0.0

## Table of contents
[0 Foreword](#0-foreword)<br>
[1 Introduction](#1-introduction)<br>
[2 Scope](#2-scope)<br>
[3 Definitions](#3-definitions)<br>
  [3.1 Mobile Robot](#31-mobile-robot)<br>
  [3.2 Moving](#32-moving)<br>
  [3.3 Driving](#33-driving)<br>
  [3.4 Automatic driving](#34-automatic-driving)<br>
  [3.5 Manual driving](#35-manual-driving)<br>
  [3.6 Line-guided mobile robot](#36-line-guided-mobile-robot)<br>
  [3.7 Freely navigating mobile robot](#37-freely-navigating-mobile-robot)<br>
[4 Transport protocol](#4-transport-protocol)<br>
  [4.1 Connection handling, security and QoS](#41-connection-handling-security-and-qos)<br>
  [4.2 Topic levels](#42-topic-levels)<br>
  [4.3 Topics for communication](#43-topics-for-communication)<br>
[5 Process and content of communication](#5-process-and-content-of-communication)<br>
  [5.1 General](#51-general)<br>
  [5.2 Implementation Phase](#52-implementation-phase)<br>
  [5.3 Functions of the fleet control](#53-functions-of-the-fleet-control)<br>
  [5.4 Functions of the mobile robots](#54-functions-of-the-mobile-robots)<br>
[6 Protocol specification](#6-protocol-specification)<br>
  [6.1 Order](#61-order)<br>
    [6.1.1 Concept and logic](#611-concept-and-logic)<br>
    [6.1.2 Orders and order updates](#612-orders-and-order-update)<br>
    [6.1.3 Order cancellation](#613-order-cancellation)<br>
    [6.1.4 Order rejection](#614-order-rejection)<br>
    [6.1.5 Corridors](#615-corridors)<br>
  [6.2 Actions](#62-actions)<br>
    [6.2.1 Instant actions](#621-instant-actions)<br>
    [6.2.2 Action blocking types and sequence](#622-action-blocking-types-and-sequence)<br>
    [6.2.3 Predefined actions](#623-predefined-actions)<br>
  [6.3 Maps](#63-maps)<br>
    [6.3.1 Map distribution](#631-map-distribution)<br>
    [6.3.2 Maps in mobile robot state](#632-maps-in-the-mobile-robot-state)<br>
    [6.3.3 Map download](#633-map-download)<br>
    [6.3.4 Enable downloaded maps](#634-enable-downloaded-maps)<br>
    [6.3.5 Delete maps on the mobile robot](#635-delete-maps-on-the-mobile-robot)<br>
  [6.4 Zones](#64-zones)<br>
    [6.4.1 Zone types](#641-zone-types)<br>
    [6.4.2 Zone set transfer](#642-zone-set-transfer)<br>
    [6.4.3 Communication for interactive zones](#643-communication-for-interactive-zones)<br>
    [6.4.4 Interaction between zones](#644-interactions-between-zones)<br>
    [6.4.5 Error handling within zones](#645-error-handling-within-zones)<br>
  [6.5 Connection](#65-connection)<br>
  [6.6 State](#66-state)<br>
    [6.6.1 Concept and logic](#661-concept-and-logic)<br>
    [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges)<br>
    [6.6.3 Base request](#663-base-request)<br>
    [6.6.4 Information](#664-information)<br>
    [6.6.5 Errors](#665-errors)<br>
    [6.6.6 Operating Mode](#666-operating-mode)<br>
    [6.6.7 Clearing the order on the mobile robot](#667-clearing-the-order-on-the-mobile-robot)<br>
    [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)<br>
    [6.6.9 Action states](#669-action-states)<br>
    [6.6.10 Request use of Corridors](#6610-request-use-of-corridors)<br>
  [6.7 Visualization](#67-visualization)<br>
  [6.8 Sharing of planned paths for freely navigating mobile robots](#68-sharing-of-planned-paths-for-freely-navigating-mobile-robots)<br>
  [6.9 Request/response mechanism](#69-requestresponse-mechanism)<br>
  [6.10 Factsheet](#610-factsheet)<br>
[7 Message specification](#7-message-specification)<br>
  [7.1 Symbols of the tables and meaning of formatting](#71-symbols-of-the-tables-and-meaning-of-formatting)<br>
    [7.1.1 Optional fields](#711-optional-fields)<br>
    [7.1.2 Permitted characters and field lengths](#712-permitted-characters-and-field-lengths)<br>
    [7.1.3 Notation of fields, topics and enumerations](#713-notation-of-fields-topics-and-enumerations)<br>
    [7.1.4 JSON data types](#714-json-data-types)<br>
  [7.2 Protocol header](#72-protocol-header)<br>
  [7.3 Implementation of the order message](#73-implementation-of-the-order-message)<br>
    [7.3.1 Format of action parameters](#731-format-of-action-parameters)<br>
  [7.4 Implementation of the instantAction message](#74-implementation-of-the-instantaction-message)<br>
  [7.5 Implementation of the response message](#75-implementation-of-the-response-message)<br>
  [7.6 Implementation of the zoneSet message](#76-implementation-of-the-zoneset-message)<br>
  [7.7 Implementation of the connection message](#77-implementation-of-the-connection-message)<br>
  [7.8 Implementation of the state message](#78-implementation-of-the-state-message)<br>
  [7.9 Implementation of the visualization message](#79-implementation-of-the-visualization-message)<br>
  [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message)<br>

# 0 Foreword

The specification for this interface has been jointly developed by the Verband der Automobilindustrie e. V. (VDA) and the VDMA e. V. (Mechanical Engineering Industry Association).
The VDA represents the German automotive sector, including OEMs and Tier‑1/Tier‑n suppliers, and contributes its expertise in vehicle architectures, system integration, and safety‑critical communication.
The VDMA represents companies across the European mechanical and plant engineering industry and brings extensive knowledge in automation technology, machinery interoperability, and production system standardization.
Both organizations collaborate to ensure that the interface specification reflects current engineering requirements, supports robust and scalable system integration, and enables consistent data exchange across heterogeneous environments. Their joint development process emphasizes harmonized communication models, compatibility with established industrial standards, and long‑term maintainability of cross‑domain interfaces. This cooperation ensures that the resulting specification can be reliably implemented in automotive, machinery, and mixed‑industry applications, supporting high interoperability, operational safety, and future-proof system architectures.
The Institute for Material Handling and Logistics (IFL) at Karlsruhe Institute of Technology (KIT) is part of the department of mechanical engineering and focuses on combining research, teaching, and industrial application. Its interdisciplinary team works on future logistics challenges, including material flow analysis, automation, robotics, digitalization, AI, sustainability, and system design.
The Institute has been commissioned by the VDA and the VDMA to oversee the development of the VDA 5050. It contributes to this process by taking the lead in development, supporting issue review, and managing the official GitHub repository.

# 1 Introduction
This recommendation describes the communication interface for exchanging information between central fleet control and mobile robots.
The objective of this recommendation is to support the integration and efficient operation of mobile robot fleets under the supervision of a centralized fleet control system. This is achieved through the implementation of a standardized, vendor neutral communication interface that ensures interoperability between the fleet control system and individual mobile robots.
Various national technical guidelines and legal frameworks may offer general orientation in this context. They could provide indicative information on aspects such as planning, operation, safety, or coordination of automated systems. In addition, national standards and regulatory provisions may help ensure that technical processes and terminology are considered within a consistent overall framework.
The recommendation uses a semantic versioning schema. Major version changes (x.0.0) typically involve breaking changes, such as the introduction of new non optional fields. Minor version changes (3.x.0) generally introduce new features, for example the addition of an optional parameter for visualization. Patch version changes (3.0.x) usually address smaller corrections, such as fixing typographical errors in the documentation.
Stakeholders are invited to submit proposals for modifications or enhancements to the interface. Such proposals shall be submitted via the GitHub repository at: <https://github.com/vda5050/vda5050>.

# 2 Scope

This document describes a standardized and vendor-neutral communication interface between a fleet control system and mobile robots. Its purpose is to provide a common reference that supports interoperability in environments where multiple mobile robots operate under the coordination of a fleet control system. The use of this specification is optional and non-binding, and its application is at the discretion of the respective stakeholders.

The objectives of this specification are:

- to reduce complexity when connecting mobile robots to a fleet control system.
- to enable the coordinated operation of heterogeneous mobile robot fleets from different manufacturers within a shared physical environment.
- to provide a generic and domain independent set of interface definitions applicable to mobile robots with varying navigation principles, physical dimensions, load handling or manipulation capabilities, and autonomy levels.

This specification does not address the following topics:

- Safety Requirements: This document does not define functional, operational, or system safety requirements and shall not be regarded or applied as a safety standard.
- Traffic Management Logic: Strategies, algorithms, or decision making processes for traffic coordination (e.g., routing, prioritization, congestion handling, or deadlock resolution) are not included.
- Other Communication Interfaces: Interfaces unrelated to the communication between a fleet control system and mobile robots are excluded, such as interfaces to peripheral equipment, infrastructure components, or external IT systems.
- Project Coordination and Implementation Procedures: Project management activities, integration methodologies, commissioning workflows, validation and acceptance procedures, and similar organizational processes are not covered.
- Operational Responsibilities: This document does not allocate responsibilities among operators, system integrators, vehicle manufacturers, or fleet control providers with respect to planning, operation, maintenance, or safety.
- Cybersecurity Measures: Mechanisms, technologies, or processes for secure communication or data protection are not specified.

# 3 Definitions
The following terms and definitions apply for the purposes of this document. Terms that are not officially defined by standardization organizations may be interpreted differently in other contexts.

## 3.1 Mobile Robot
A driverless system for material transport primarily in operational settings, controlled by automation independently of their level of autonomy [Source ISO 3691-4]

## 3.2 Moving
State in which a mobile robot or any of its components undergoes a change in spatial position or orientation, including movement of wheels, load handling devices, or the robot body.

## 3.3 Driving
Operating state in which the mobile robot has a non zero translational and/or rotational velocity.

## 3.4 Automatic driving
Driving state in which the mobile robot operates without human intervention.

## 3.5 Manual driving
Driving state in which the mobile robot operates under direct human control.

## 3.6 Line-guided mobile robot
Mobile robots that follow predefined trajectories. Predefined trajectories are sent by fleet control as part of the order or defined on the robot, either explicitly or implicitly as the direct connection between nodes.

## 3.7 Freely navigating mobile robot
Mobile robots that plan their own trajectories. If fleet control sends a trajectory within the order, the robot shall follow this trajectory.

# 4 Transport protocol

Communication is expected to be done via wireless networks, considering the effects of connection failures and potential loss of messages.

The message protocol is Message Queuing Telemetry Transport (MQTT), which is to be used in combination with a JSON format.
MQTT 3.1.1 is the minimum required version for compatibility.
MQTT allows the distribution of messages to subchannels, which are called "topics".
Participants in the MQTT network subscribe to these topics and receive information that concerns them.

The JSON format allows for future extensions of the protocol with additional parameters as well as validation against schemas.

### 4.1 Connection handling, security and QoS

The MQTT protocol provides the option of setting a last will message for a client.
If the client disconnects unexpectedly for any reason, the last will is distributed by the broker to other subscribed clients.
The use of this feature is described in Section [6.5 Connection](#65-connection).

If the mobile robot disconnects from the broker, it keeps all the order information and fulfills the order up to the last released node.
…(발췌: 전체 207,642자 중 앞 14,754자)
```

### data/source_texts/ref-044.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
@prefix cbv:   <https://ref.gs1.org/cbv/> .
@prefix epcis: <https://ref.gs1.org/epcis/> .
@prefix gs1:   <https://gs1.org/voc/> .

@prefix dct:    <http://purl.org/dc/terms/> .
@prefix owl:    <http://www.w3.org/2002/07/owl#> .
@prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <http://schema.org/> .
@prefix skos:   <http://www.w3.org/2004/02/skos/core#> .
@prefix sw:     <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix vann:   <http://purl.org/vocab/vann/> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .

#################### Ontology

cbv: a owl:Ontology;
  rdfs:label "CBV Ontology";
  rdfs:comment """The Comprehensive Business Vocabulary defines various enumerations used by EPCIS.""";
  dct:creator <https://gs1.org/>;
  dct:publisher <https://gs1.org/>;
  dct:created  "2021-06-01"^^xsd:date;
  dct:modified "2021-09-30"^^xsd:date;
  # dct:issued   "2021-06-30"^^xsd:date; # after release
  rdfs:seeAlso epcis:, gs1: ;
  owl:versionInfo "2.0";
  vann:preferredNamespaceUri "https://ref.gs1.org/cbv/";
  vann:preferredNamespacePrefix "cbv".

<https://gs1.org/> a schema:Organization;
  schema:name "GS1";
  schema:description "GS1 is an international organization that sets the global standards in transport and logistics".

#################### Business Transaction Type

cbv:BTT  a                owl:Class , rdfs:Class ;
        rdfs:comment      "These identifiers may be used to populate the type attribute of a bizTransaction element in an EPCIS event."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Business Transaction Type"@en ;
        rdfs:subClassOf   cbv:TypeCode ;
        sw:term_status    "stable" .

cbv:BTT-bol  a            cbv:BTT ;
        rdfs:comment      "A document issued by a carrier to a shipper, listing and acknowledging receipt of goods for transport and specifying terms of delivery."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Bill of Lading"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:bol> ;
        sw:term_status    "stable" .

cbv:BTT-cert  a           cbv:BTT ;
        rdfs:comment      "A document confirming certain characteristics of an object (e.g. product), person, or organisation, typically issued by a third party."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Certificate"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:cert> ;
        sw:term_status    "stable" .

cbv:BTT-desadv  a         cbv:BTT ;
        rdfs:comment      "A document/message by means of which the seller or consignor informs the consignee about the despatch of goods. \nAlso called an 'Advanced Shipment Notice', but the value `desadv` is always used regardless of local nomenclature."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Despatch Advice"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:desadv> ;
        sw:term_status    "stable" .

cbv:BTT-inv  a            cbv:BTT ;
        rdfs:comment      "A document/message claiming payment for goods or services supplied under conditions agreed by the seller and buyer."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Invoice"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:inv> ;
        sw:term_status    "stable" .

cbv:BTT-pedigree  a       cbv:BTT ;
        rdfs:comment      "A record that traces the ownership or custody and transactions of a product as it moves among various trading partners."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Pedigree"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:pedigree> ;
        sw:term_status    "stable" .

cbv:BTT-po  a             cbv:BTT ;
        rdfs:comment      "A document/message that specifies details for goods and services ordered under conditions agreed by the seller and buyer."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Purchase Order"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:po> ;
        sw:term_status    "stable" .

cbv:BTT-poc  a            cbv:BTT ;
        rdfs:comment      "A document that provides confirmation from an external supplier to the request of a purchaser to deliver a specified quantity of material, or perform a specified service, at a specified price within a specified time. \n(Sometimes internally referred to as a 'Sales Order'.)"@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Purchase Order Confirmation"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:poc> ;
        sw:term_status    "stable" .

cbv:BTT-prodorder  a      cbv:BTT ;
        rdfs:comment      "An organisation-internal document or message issued by a producer that initiates a manufacturing process of goods."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Production Order"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:prodorder> ;
        sw:term_status    "stable" .

cbv:BTT-recadv  a         cbv:BTT ;
        rdfs:comment      "A document/message that provides the receiver of the shipment the capability to inform the shipper of actual goods received, compared to what was advised as being sent."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Receiving Advice"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:recadv> ;
        sw:term_status    "stable" .

cbv:BTT-rma  a            cbv:BTT ;
        rdfs:comment      "A document issued by the seller that authorises a buyer to return merchandise for credit determination."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Return Merchandise Authorisation"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:rma> ;
        sw:term_status    "stable" .

cbv:BTT-testprd  a        cbv:BTT ;
        rdfs:comment      "A document that provides a formal specification of a sequence of instructions for the purpose of verifying one or several criteria."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Test Procedure"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:testprd> ;
        sw:term_status    "stable" .

cbv:BTT-testres  a        cbv:BTT ;
        rdfs:comment      "A document that includes the outcome of the execution of a given test procedure."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Test Result"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:testres> ;
        sw:term_status    "stable" .

cbv:BTT-upevt  a        cbv:BTT ;
        rdfs:comment      "Event ID URI(s) of event(s) provided by an upstream supplier, such as packing and shipping events (e.g., as the basis for the inferred completeness of inbound aggregations)."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Upstream EPCIS Event"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:upevt> ;
        sw:term_status    "stable" .

#################### Business Step

cbv:BizStep  a            owl:Class , rdfs:Class ;
        rdfs:comment      "These identifiers populate the bizStep field in an EPCIS event."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Business Step ID"@en ;
        rdfs:subClassOf   cbv:TypeCode ;
        sw:term_status    "stable" .

cbv:BizStep-accepting
        a                 cbv:BizStep ;
        rdfs:comment      "Denotes a specific activity within a business process where an object changes possession and/or ownership."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "accepting"@en ;
        owl:sameAs        <urn:epcglobal:cbv:bizstep:accepting> ;
        sw:term_status    "stable" ;
        skos:example      "Retailer X unloads a pallet on to the receiving dock. The numbers of cases on the pallet are counted. The pallets are disaggregated from the shipping conveyance. The quantity is verified against the delivery document (Freight Bill or Bill of Lading), notating any over, short or damaged product at the time of delivery. Typically this process releases freight payment and completes the contractual agreement with the carrier of delivering the product/assets to a specified location.\nA parcel carrier drops off five boxes at Distributor Y's DC. A person on the Receiving Dock signs that they accept the five boxes from the parcel carrier.\nA wholesaler is assigned a lot of fish at a fish auction, verifies the quantity and acknowledges receipt.\nA manufacturer's fork lift driver scans the IDs of components which have been removed from a consignment warehouse. In doing so, the components are added to the manufacturer's inventory."@en .

cbv:BizStep-arriving  a   cbv:BizStep ;
        rdfs:comment      "Denotes a specific activity within a business process where an object arrives at a location."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "arriving"@en ;
        owl:sameAs        <urn:epcglobal:cbv:bizstep:arriving> ;
        sw:term_status    "stable" ;
        skos:example      "Truckload of a shipment arrives into a yard. Shipment has not yet been received or accepted."@en .

cbv:BizStep-assembling
        a                 cbv:BizStep ;
        rdfs:comment      "Denotes an activity within a business process whereby one or more objects are combined to create a new finished product. \nIn contrast to transformation, in the output of `assembling` the original objects are still recognisable and/or the process is reversible; hence, `assembling` would be used preferably in an Association Event or, alternatively, an Aggregation Event, but not a Transformation Event."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "assembling"@en ;
        owl:sameAs        <urn:epcglobal:cbv:bizstep:assembling> ;
        sw:term_status    "stable" ;
        skos:example      "Computer parts (hard drive, battery, RAM) assembled into a consumer ready computer\nMaintenance, repair and overhaul processes involving components added to an assembly comprised of multiple parts.\nHealthcare kitting: a surgical kit including drug, syringe, and gauze are combined to create a new 'product': a *kit*."@en .

cbv:BizStep-collecting
        a                 cbv:BizStep ;
        rdfs:comment      "Denotes a specific activity within a business process where an object is picked up and collected for future disposal, recycling or re-used."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "collecting"@en ;
        owl:sameAs        <urn:epcglobal:cbv:bizstep:collecting> ;
        sw:term_status    "stable" ;
        skos:example      "An organisation picks up disposed consumer electronics in an end of life state from various different organisations. After the goods are picked up, they typically are brought back and received into a Collection Centre\nRented or leased pallets are picked up and brought to a collection centre."@en .

cbv:BizStep-commissioning
        a                 cbv:BizStep ;
        rdfs:comment      "Process of associating an instance-level identifier (such as an EPC) with a specific object, or the process of associating a class-level identifier, not previously used, with one or more objects. \nA tag may have been encoded and applied in this step, or may have been previously encoded. \n`commissioning` is applied to this association of object and serialised identifier, regardless of industry/sector; it encompasses sector-specific process steps including, but not limited to: \n- catching (of fish), \n- harvesting (of fruit/vegetable), \n- picking (of fruit/vegetables), \n- producing (on an automated line), \n- slaughtering (of livestock). \nIn the case of a class-level identifier, `commissioning` differs from `creating_class_instance` in that `commissioning` always indicates that this is the first use of the class-level identifier, whereas `creating_class_instance` does not specify whether the class-level identifier has been used before."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "commissioning"@en ;
        owl:sameAs        <urn:epcglobal:cbv:bizstep:commissioning> ;
        sw:term_status    "stable" ;
        skos:example      "On a packaging line, an encoded EPC is applied to a case and associated to the product.\nAn individual virtual document (e.g. digital coupon, digital voucher, etc.) is assigned an EPC.\nOne hundred bottles of a particular batch of pharmaceutical product are produced, those being the first bottles of that batch to be produced.\nSides of beef are transformed into individual packaged steaks. This may be an EPCIS 1.2 TransformationEvent if the input sides of beef are also tracked."@en .

cbv:BizStep-consigning
        a                 cbv:BizStep ;
        rdfs:comment      "Indicates the overall process of `staging_outbound`, `loading`, `departing`, and `accepting`. \nIt may be used when more granular process step information is unknown or inaccessible. \nThe use of `consigning` is mutually exclusive from the use of `staging_outbound`, `loading`, `departing`, and `accepting`. \nNote: This business step is similar to `shipping`, but includes a change of possession and/or ownership at the outbound side."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "consigning"@en ;
        owl:sameAs        <urn:epcglobal:cbv:bizstep:consigning> ;
        sw:term_status    "stable" ;
        skos:example      "A wholesaler comes aboard a fishing vessel, selects and buys boxes of fish, and brings them to his premises. \nA manufacturer retrieves components from a consignment warehouse for use in its assembly line. In the logical second of leaving the consignment warehouse, the components pass into the ownership of the manufacturer.\nA manufacturer stages products for loading, loads them into a container, the container is sealed, and the container departs. Ownership transfers to the receiver sometime during this overall process. If this is done in a single step, then business step `consigning` is used."@en .
…(발췌: 전체 69,067자 중 앞 13,923자)
```

### data/source_texts/ref-049.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
builtin_interfaces/Time time

# A unique ID for the request which this result is for
string request_guid

# The unique ID of the workcell that this result was sent from
string source_guid

# Different basic result statuses
uint8 status
uint8 ACKNOWLEDGED=0
uint8 SUCCESS=1
uint8 FAILED=2

# below are custom workcell message fields
```

### data/source_texts/ref-110.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Supporting a new Task in RMF

With the release of [RMF Task V2](https://github.com/open-rmf/rmf_task/pull/39), users can now construct custom tasks according to their specific needs. Different combination or sequence of robotic tasks can be dispatched to a specified robot or to the best available fleet based on the users' preferences.

The new flexible task system introduces the concept of a Phase. A task is an object that generates phases. In other words, a task is typically made up of a series or combination of phases as its building blocks. For example, a delivery task would require a robot to complete the following steps:
1. Move from its current waypoint to a pick-up location
2. Pick up the delivery payload
3. Move from the pick up location to the drop-off location
4. Drop off the payload
5. Move back to the initial starting waypoint

Each of these steps can be considered a Phase. Users can use the following public API phases to construct their own tasks:
- [`GoToPlace`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__go_to_place.json)
- [`PickUp`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__pickup.json)
- [`DropOff`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__dropoff.json)
- [`PerformAction`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__perform_action.json)

Additional phase descriptions, including those supporting the public API phases, are defined and listed [here](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter/schemas). They will be useful for building your own custom task.

Certain tasks may require specific phases that are not mentioned above. For example, if a delivery task involves the robot moving from the first to second level, it would require a `RequestLift` phase. Such phases are used by RMF internally and automatically added to a task when necessary, so users do not need to worry about them when creating their custom tasks.

## Building a Custom Task

Users can build and send their own tasks by publishing [`ApiRequest`](https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/ApiRequest.msg) messages. You will need to fill in the `request_id` and `json_msg` fields according to the types of phases that make up the task, as well as whether the task is intended for a specific robot or the best available fleet. You may follow these steps to construct your own task:

1. Create an `ApiRequest` publisher that sends task requests via the `/task_api_requests` topic.
2. Fill in the `request_id` field with a unique string ID that can be used to identify the task.
3. For the `json_msg` field,
    - Use the [`robot_task_request`](https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_task_request.json) schema and fill in the JSON payload type with `"robot_task_request"` to send a task request to a specific robot
    - Use the [`dispatch_task_request`](https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/dispatch_task_request.json) schema and fill in the JSON payload type with `"dispatch_task_request"` to send a task request to the best available fleet
    - The `request` fields for these objects follow the [`task_request`](https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json) schema
4. Populate the object fields with the required information.
    - The `category` and `description` fields under the `task_request` schema take in the string name of the task and the task description respectively. The JSON schema for these descriptions can be found [here](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter/schemas). There are currently four task descriptions available:
      - [**Clean**](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/task_description__clean.json): create your own clean task, requires the [`Clean`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__clean.json) phase description
      - [**Compose**](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/task_description__compose.json): create your own custom task that may comprise of a sequence of phases, requires descriptions for the relevant phases
      - [**Delivery**](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/task_description__delivery.json): create your own delivery task, requires the [`PickUp`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__pickup.json) and [`DropOff`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__dropoff.json) phase descriptions
      - [**Patrol**](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/task_description__patrol.json): create your own patrol task, requires the [`Place`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/place.json) description to indicate where you would like your robot to go to
5. Publish the `ApiRequest`!

#### Examples of JSON Task Requests
For a **Clean** `dispatch_task_request`:
```
{
  "type": "dispatch_task_request",
  "request": {
    "unix_millis_earliest_start_time": start_time,
    "category": "clean",
    "description": {
      "zone": "clean_lobby"
    }
  }
}
```

For a **Compose** `robot_task_request` that commands a specific robot to go to a place, followed by performing a `teleop` action:
```
{
  "type": "robot_task_request",
  "robot": "tinyRobot1",
  "fleet": "tinyRobot",
  "request": {
    "category": "compose",
    "description": {
      "category": "teleop",
      "phases": [
        {"activity": {
          "category": "sequence",
          "description": {
            "activities": [
              {"category": "go_to_place",
               "description": "coe"
              },
              {"category": "perform_action",
                "description": {"category": "teleop", "description": "coe"}
              }
            ]
          }
        }}
      ]
    }
  }
}
```

For a **Delivery** `dispatch_task_request`:
```
{
  "type": "dispatch_task_request",
  "request": {
    "category": "delivery",
    "description": {
      "pickup": {
        "place": "pantry",
        "handler": "coke_dispenser",
        "payload": [
          {"sku": "coke",
           "quantity": 1}
        ]
      },
      "dropoff": {
        "place": "hardware_2",
        "handler": "coke_ingestor",
        "payload": [
          {"sku": "coke",
           "quantity": 1}
        ]
      }
    }
  }
}
```

For a **Patrol** `robot_task_request`:
```
{
  "type": "robot_task_request",
  "robot": "tinyRobot1",
  "fleet": "tinyRobot",
  "request": {
    "category": "patrol",
    "description": {
      "places": ["pantry", "lounge"],
      "rounds": 2
    }
  }
}
```

Some examples of composed task requests can be found [here](https://github.com/open-rmf/rmf_demos/pull/122) as reference. They can be used with `rmf_demos`. Feel free to modify these files according to your own application.

## Task Management Control

You may take additional control over your tasks by sending requests to RMF to cancel a task or skip a phase. A full list of JSON schemas for such requests are defined [here](https://github.com/open-rmf/rmf_api_msgs/tree/main/rmf_api_msgs/schemas).
````

### data/source_texts/ref-111.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_state.json",
  "title": "Task State",
  "description": "The state of a task",
  "type": "object",
  "properties": {
    "booking": { "$ref": "#/$defs/booking" },
    "category": { "$ref": "#/$defs/category" },
    "detail": { "$ref": "#/$defs/detail" },
    "unix_millis_start_time": { "type": "integer" },
    "unix_millis_finish_time": { "type": "integer" },
    "original_estimate_millis": { "$ref": "#/$defs/estimate_millis" },
    "estimate_millis": { "$ref": "#/$defs/estimate_millis" },
    "assigned_to": {
      "description": "Which agent (robot) is the task assigned to",
      "type": "object",
      "properties": {
        "group": { "type": "string" },
        "name": { "type": "string" }
      },
      "required": ["group", "name"]
    },
    "status": { "$ref": "#/$defs/status" },
    "dispatch": { "$ref": "#/$defs/dispatch" },
    "phases": {
      "description": "A dictionary of the states of the phases of the task. The keys (property names) are phase IDs, which are integers.",
      "type": "object",
      "additionalProperties": { "$ref": "#/$defs/phase" }
    },
    "completed": {
      "description": "An array of the IDs of completed phases of this task",
      "type": "array",
      "items": { "$ref": "#/$defs/id" }
    },
    "active": {
      "description": "The ID of the active phase for this task",
      "$ref": "#/$defs/id"
    },
    "pending": {
      "description": "An array of the pending phases of this task",
      "type": "array",
      "items": { "$ref": "#/$defs/id" }
    },
    "interruptions": {
      "description": "A dictionary of interruptions that have been applied to this task. The keys (property names) are the unique token of the interruption request.",
      "type": "object",
      "additionalProperties": { "$ref": "#/$defs/interruption" }
    },
    "cancellation": {
      "description": "If the task was cancelled, this will describe information about the request.",
      "type": "object",
      "properties": {
        "unix_millis_request_time": {
          "description": "The time that the cancellation request arrived",
          "type": "integer"
        },
        "labels": {
          "description": "Labels to describe the cancel request, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
          "type": "array",
          "items": { "type": "string" }
        }
      },
      "required": ["unix_millis_request_time", "labels"]
    },
    "killed": {
      "description": "If the task was killed, this will describe information about the request.",
      "type": "object",
      "properties": {
        "unix_millis_request_time": {
          "description": "The time that the cancellation request arrived",
          "type": "integer"
        },
        "labels": {
          "description": "Labels to describe the kill request, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
          "type": "array",
          "items": { "type": "string" }
        }
      },
      "required": ["unix_millis_request_time", "labels"]
    }
  },
  "required": ["booking"],
  "$defs": {
    "phase": {
      "description": "Information about a phase",
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/id" },
        "category": { "$ref": "#/$defs/category" },
        "detail": { "$ref": "#/$defs/detail" },
        "unix_millis_start_time": { "type": "integer" },
        "unix_millis_finish_time": { "type": "integer" },
        "original_estimate_millis": { "$ref": "#/$defs/estimate_millis" },
        "estimate_millis": { "$ref": "#/$defs/estimate_millis" },
        "final_event_id": { "$ref": "#/$defs/id" },
        "events": {
          "description": "A dictionary of events for this phase. The keys (property names) are the event IDs, which are integers.",
          "type": "object",
          "additionalProperties": { "$ref": "#/$defs/event_state" }
        },
        "skip_requests": {
          "description": "Information about any skip requests that have been received",
          "type": "object",
          "additionalProperties": { "$ref": "#/$defs/skip_phase_request" }
        }
      },
      "required": ["id"]
    },
    "booking": {
      "description": "Information about how a task was booked",
      "type": "object",
      "properties": {
        "id": {
          "description": "The unique identifier for this task",
          "type": "string"
        },
        "unix_millis_earliest_start_time": { "type": "integer" },
        "unix_millis_request_time": { "type": "integer" },
        "priority": {
          "description": "Priority information about this task",
          "anyOf": [
            { "type": "object" },
            { "type": "string" }
          ]
        },
        "labels": {
          "description": "Information about how and why this task was booked, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
          "type": "array",
          "items": { "type": "string" }
        },
        "requester": {
          "description": "(Optional) An identifier for the entity that requested this task",
          "type": "string"
        }
      },
      "required": ["id"]
    },
    "id": {
      "type": "integer",
      "minimum": 0
    },
    "category": {
      "description": "The category of this task or phase",
      "type": "string"
    },
    "detail": {
      "description": "Detailed information about a task, phase, or event",
      "anyOf": [
        { "type": "object" },
        { "type": "array" },
        { "type": "string" }
      ]
    },
    "estimate_millis": {
      "description": "An estimate, in milliseconds, of how long the subject will take to complete",
      "type": "integer",
      "minimum": 0
    },
    "event_state": {
      "description": "The current state of an event",
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/id" },
        "status": { "$ref": "#/$defs/status"},
        "name": {
          "description": "The brief name of the event",
          "type": "string"
        },
        "detail": {
          "description": "Detailed information about the event",
          "$ref": "#/$defs/detail"
        },
        "deps": {
          "description": "This event may depend on other events. This array contains the IDs of those other event dependencies.",
          "type": "array",
          "items": {
            "description": "The IDs of events that this event depends on. Event IDs are isolated within the scope of this task phase.",
            "type": "integer",
            "minimum": 0
          }
        }
      },
      "required": ["id"]
    },
    "status": {
      "description": "A simple token representing how the task is proceeding",
      "type": "string",
      "enum": ["uninitialized", "blocked", "error", "failed", "queued", "standby", "underway", "delayed", "skipped", "canceled", "killed", "completed"]
    },
    "dispatch": {
      "description": "Information about how this task is being dispatched",
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": ["queued", "selected", "dispatched", "failed_to_assign", "canceled_in_flight"]
        },
        "assignment": {
          "type": "object",
          "properties": {
            "fleet_name": { "type": "string" },
            "expected_robot_name": { "type": "string" }
          }
        },
        "errors": {
          "type": "array",
          "items": { "$ref": "error.json" }
        }
      },
      "required": ["status"]
    },
    "interruption": {
      "description": "Task interruption information",
      "type": "object",
      "properties": {
        "unix_millis_request_time": {
          "description": "The time that the interruption request arrived",
          "type": "integer"
        },
        "labels": {
          "description": "Labels to describe the purpose of the interruption, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
          "type": "array",
          "items": { "type": "string" }
        },
        "resumed_by": {
          "description": "Information about the resume request that ended this interruption. This field will be missing if the interruption is still active.",
          "type": "object",
          "properties": {
            "unix_millis_request_time": {
              "description": "The time that the resume request arrived",
              "type": "integer"
            },
            "labels": {
              "description": "Labels to describe the resume request, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["unix_millis_resume_time", "labels"]
        }
      },
      "required": ["unix_millis_request_time", "labels"]
    },
    "skip_phase_request": {
      "description": "Information about a request to skip a phase",
      "type": "object",
      "properties": {
        "unix_millis_request_time": {
          "description": "The time that the skip request arrived",
          "type": "integer"
        },
        "labels": {
          "description": "Labels to describe the purpose of the skip request, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
          "type": "array",
          "items": { "type": "string" }
        },
        "undo": {
          "description": "Information about an undo skip request that applied to this request",
          "type": "object",
          "properties": {
            "unix_millis_request_time": {
              "description": "The time that the undo skip request arrived",
              "type": "integer"
            },
            "labels": {
              "description": "Labels to describe the undo skip request, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["unix_millis_request_time", "labels"]
        }
      },
      "required": ["unix_millis_request_time", "labels"]
    }
  }
}
```

### data/source_texts/ref-117.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
<?xml version="1.0"?>
<xsd:schema xmlns="http://www.mesa.org/xml/B2MML" xmlns:Extended="http://www.mesa.org/xml/B2MML-AllExtensions" xmlns:xsd="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.mesa.org/xml/B2MML" elementFormDefault="qualified" attributeFormDefault="unqualified">
    <!-- Include the Core Components schema in the default namespace  -->
    <xsd:include schemaLocation="B2MML-CoreComponents.xsd"/>
    <!-- Include the InformationObject schema with InformationObjectType for OperationsRecordEntryTemplateType in the default namespace  -->
    <xsd:include schemaLocation="B2MML-InformationObject.xsd"/>
    <!-- Import the Common Extension Schema                 -->
    <xsd:import namespace="http://www.mesa.org/xml/B2MML-AllExtensions"
                schemaLocation="B2MML-AllExtensions.xsd"/>
    <xsd:annotation>
        <xsd:documentation>

        Copyright 2023 MESA International, Version 0701
        All Rights Reserved. http://www.mesa.org

        This MESA International work (including specifications, documents,
        software, and related items) referred to as the Business To
        Manufacturing Markup Language (B2MML) is provided by the copyright
        holders under the following license.

        Permission to use, copy, modify, or redistribute this Work and its
        documentation, with or without modification, for any purpose and
        without fee or royalty is hereby granted provided MESA International
        is acknowledged as the originator of this Work using the
        following statement:

        "The Business To Manufacturing Markup Language (B2MML) is used
        courtesy of MESA International."

        In no event shall MESA International, its members, or any
        third party be liable for any costs, expenses, losses, damages or
        injuries incurred by use of the Work or as a result of this
        agreement.

        Based upon the ANSI/ISA-95.00.02-2018 Enterprise-Control System
        Integration Part 2: Object Model Attributes Standard and the
        ANSI/ISA-95.00.05-2018 Enterprise-Control System Integration
        Part 5: Business to Manufacturing Transactions.
   </xsd:documentation>
   <xsd:documentation>
      Revision history maintained in GitHub
   </xsd:documentation>

    </xsd:annotation>
    <!--  - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   -->
    <!--  B2MML Common Component Elements - - - - - - - - - - - - -   -->
    <!--  - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   -->

    <!--     -->
    <xsd:complexType name="AnyGenericValueType">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="currencyID"                type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="currencyCodeListVersionID" type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="encodingCode"              type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="format"                    type="xsd:string"           use="optional"/>
                <xsd:attribute name="characterSetCode"          type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="listID"                    type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="listAgencyID"              type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="listAgencyName"            type="xsd:string"           use="optional"/>
                <xsd:attribute name="listName"                  type="xsd:string"           use="optional"/>
                <xsd:attribute name="listVersionID"             type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="languageID"                type="xsd:language"         use="optional"/>
                <xsd:attribute name="languageLocaleID"          type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="listURI"                   type="xsd:anyURI"           use="optional"/>
                <xsd:attribute name="listSchemaURI"             type="xsd:anyURI"           use="optional"/>
                <xsd:attribute name="mimeCode"                  type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="name"                      type="xsd:string"           use="optional"/>
                <xsd:attribute name="schemaID"                  type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="schemaName"                type="xsd:string"           use="optional"/>
                <xsd:attribute name="schemaAgencyID"            type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="schemaAgencyName"          type="xsd:string"           use="optional"/>
                <xsd:attribute name="schemaVersionID"           type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="schemaDataURI"             type="xsd:anyURI" use="optional"/>
                <xsd:attribute name="schemaURI"                 type="xsd:anyURI" use="optional"/>
                <xsd:attribute name="unitCode"                  type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="unitCodeListID"            type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="unitCodeListAgencyID"      type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="unitCodeListAgencyName"    type="xsd:string" use="optional"/>
                <xsd:attribute name="unitCodeListVersionID"     type="xsd:normalizedString" use="optional"/>
                <xsd:attribute name="filename"                  type="xsd:string" use="optional"/>
                <xsd:attribute name="uri"                       type="xsd:anyURI" use="optional"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="AssemblyRelationship1Type">
        <xsd:simpleContent>
            <xsd:restriction base="CodeType">
                <xsd:enumeration value="Permanent"/>
                <xsd:enumeration value="Transient"/>
                <xsd:enumeration value="Other"/>
            </xsd:restriction>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="AssemblyRelationshipType">
		<xsd:annotation>
			<xsd:documentation>
Defines the type of the relationships.
Defined types are
- Permanent: an assembly that is not intended to be split during the production process;
- Transient: a temporary assembly using during production, such as a pallet of different materials or a batch kit.
			</xsd:documentation>
		</xsd:annotation>
         <xsd:simpleContent>
            <xsd:extension base="AssemblyRelationship1Type">
                <xsd:attribute name="OtherValue"               type="xsd:string"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="AssemblyType1Type">
        <xsd:simpleContent>
            <xsd:restriction base="CodeType">
                <xsd:enumeration value="Physical"/>
                <xsd:enumeration value="Logical"/>
                <xsd:enumeration value="Other"/>
            </xsd:restriction>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="AssemblyTypeType">
		<xsd:annotation>
			<xsd:documentation>
Defines the type of the assembly.
Defined types are
- physical: the components of the assembly are physically connected or in the same area.
- logical: the components of the assembly are not necessarily physically connected or in the same area.
			</xsd:documentation>
		</xsd:annotation>
         <xsd:simpleContent>
            <xsd:extension base="AssemblyType1Type">
                <xsd:attribute name="OtherValue"                type="xsd:string"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="CapabilityType1Type">
        <xsd:simpleContent>
            <xsd:restriction base="CodeType">
                <xsd:enumeration value="Used"/>
                <xsd:enumeration value="Unused"/>
                <xsd:enumeration value="Total"/>
                <xsd:enumeration value="Committed"/>
                <xsd:enumeration value="Available"/>
                <xsd:enumeration value="Unattainable"/>
                <xsd:enumeration value="Other"/>
            </xsd:restriction>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="CapabilityTypeType">
		<xsd:annotation>
			<xsd:documentation>
Defines the type of capability.
Defined values are
- Committed: capacity that is committed for future productive use;
- Unattainable: capacity that is not attainable for future productive use given the equipment condition, equipment utilization, personnel availability or material availability;
- Available: capacity that is available for additional future productive use;
- Used: a historical value that defines the portion of the capacity with acceptable quality;
- Unused: a historical value that defines the portion of the capacity that was not used or had unacceptable quality; and
- Total: the sum of used and unused capability or the sum of available, unattainable and committed capability.
            </xsd:documentation>
		</xsd:annotation>
        <xsd:simpleContent>
            <xsd:extension base="CapabilityType1Type">
                <xsd:attribute name="OtherValue"               type="xsd:string"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="CauseType">
        <xsd:simpleContent>
            <xsd:restriction base="CodeType"/>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="ClassPropertyTypeType">
		<xsd:annotation>
			<xsd:documentation>
Defines the type of the property. Defined types are
- ClassType: the property value is defined for the class and there is no value associated with an instance;
- InstanceType: the property value of the class is undefined; and
- DefaultType: the property value is defined for the class as the default instance value, but individual instances of the class may redefine specific values.
			</xsd:documentation>
		</xsd:annotation>
        <xsd:simpleContent>
            <xsd:restriction base="CodeType">
                <xsd:enumeration value="ClassType"/>
                <xsd:enumeration value="InstanceType"/>
                <xsd:enumeration value="DefaultType"/>
                <xsd:enumeration value="Other"/>
            </xsd:restriction>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="ConfidenceFactorType">
        <xsd:simpleContent>
            <xsd:restriction base="IdentifierType"/>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="DataType1Type">
        <xsd:simpleContent>
            <xsd:restriction base="CodeType">
                <xsd:enumeration value="Amount"/>
                <!-- UN/CEFACT Core Component Type -->
                <xsd:enumeration value="BinaryObject"/>
                <!-- UN/CEFACT Core Component Type -->
                <xsd:enumeration value="Code"/>
                <!-- UN/CEFACT Core Component Type -->
                <xsd:enumeration value="DateTime"/>
                <!-- UN/CEFACT Core Component Type -->
                <xsd:enumeration value="Identifier"/>
                <!-- UN/CEFACT Core Component Type -->
                <xsd:enumeration value="Indicator"/>
                <!-- UN/CEFACT Core Component Type -->
                <xsd:enumeration value="Measure"/>
                <!-- UN/CEFACT Core Component Type -->
                <xsd:enumeration value="Numeric"/>
                <!-- UN/CEFACT Core Component Type -->
                <xsd:enumeration value="Quantity"/>
                <!-- UN/CEFACT Core Component Type -->
                <xsd:enumeration value="Text"/>
                <!-- UN/CEFACT Core Component Type -->
                <xsd:enumeration value="string"/>
                <xsd:enumeration value="byte"/>
                <xsd:enumeration value="unsignedByte"/>
                <xsd:enumeration value="binary"/>
                <xsd:enumeration value="integer"/>
                <xsd:enumeration value="positiveInteger"/>
                <xsd:enumeration value="negativeInteger"/>
                <xsd:enumeration value="nonNegativeInteger"/>
                <xsd:enumeration value="nonPositiveInteger"/>
                <xsd:enumeration value="int"/>
                <xsd:enumeration value="unsignedInt"/>
                <xsd:enumeration value="long"/>
                <xsd:enumeration value="unsignedLong"/>
                <xsd:enumeration value="short"/>
                <xsd:enumeration value="unsignedShort"/>
                <xsd:enumeration value="decimal"/>
                <xsd:enumeration value="float"/>
                <xsd:enumeration value="double"/>
                <xsd:enumeration value="boolean"/>
                <xsd:enumeration value="time"/>
                <xsd:enumeration value="timeInstant"/>
                <xsd:enumeration value="timePeriod"/>
                <xsd:enumeration value="duration"/>
                <xsd:enumeration value="date"/>
                <xsd:enumeration value="dateTime"/>
                <xsd:enumeration value="month"/>
                <xsd:enumeration value="year"/>
                <xsd:enumeration value="century"/>
                <xsd:enumeration value="recurringDay"/>
                <xsd:enumeration value="recurringDate"/>
                <xsd:enumeration value="recurringDuration"/>
                <xsd:enumeration value="Name"/>
                <xsd:enumeration value="QName"/>
                <xsd:enumeration value="NCName"/>
                <xsd:enumeration value="uriReference"/>
                <xsd:enumeration value="language"/>
                <xsd:enumeration value="ID"/>
                <xsd:enumeration value="IDREF"/>
                <xsd:enumeration value="IDREFS"/>
                <xsd:enumeration value="ENTITY"/>
                <xsd:enumeration value="ENTITIES"/>
                <xsd:enumeration value="NOTATION"/>
                <xsd:enumeration value="NMTOKEN"/>
                <xsd:enumeration value="NMTOKENS"/>
                <xsd:enumeration value="Enumeration"/>
                <xsd:enumeration value="SVG"/>
                <xsd:enumeration value="Other"/>
            </xsd:restriction>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="DataTypeType">
        <xsd:simpleContent>
            <xsd:extension base="DataType1Type">
                <xsd:attribute name="OtherValue" type="xsd:string"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="DefinitionTypeType">
		<xsd:annotation>
			<xsd:documentation>
Defines the type of the definition of a process segment, operations definition, or operations segment.
Defined types are:
-	Pattern: a segment or definition used as a template for other segments or definitions;
-	Instance: a segment or definition that may be directly scheduled and tracked.
			</xsd:documentation>
		</xsd:annotation>
        <xsd:simpleContent>
            <xsd:restriction base="CodeType">
                <xsd:enumeration value="Pattern"/>
                <xsd:enumeration value="Instance"/>
            </xsd:restriction>
        </xsd:simpleContent>
    </xsd:complexType>

     <!--     -->
    <xsd:complexType name="Dependency1Type">
        <xsd:simpleContent>
            <xsd:restriction base="CodeType">
                <xsd:enumeration value="NotFollow"/>
                <xsd:enumeration value="PossibleParallel"/>
                <xsd:enumeration value="NotInParallel"/>
                <xsd:enumeration value="AtStart"/>
                <xsd:enumeration value="AfterStart"/>
                <xsd:enumeration value="AfterEnd"/>
                <xsd:enumeration value="NoLaterAfterStart"/>
                <xsd:enumeration value="NoEarlierAfterStart"/>
                <xsd:enumeration value="NoLaterAfterEnd"/>
                <xsd:enumeration value="NoEarlierAfterEnd"/>
                <xsd:enumeration value="Other"/>
            </xsd:restriction>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="DependencyType">
		<xsd:annotation>
			<xsd:documentation>
Defines an execution dependency constraint of two elements.
Defined values are (explained using dependency type between element A and element B)
- at start: start B at A start;
- after start: start B after A start;
- after end: start B after A end;
- not follow: B cannot follow A;
- possible parallel: B may run in parallel to A;
- not in parallel: B may not run in parallel to A;
- no later after start: start B no later than dependency factor after A start:
- no earlier after start: start B no earlier than dependency factor after A start;
- no later after end: start B no later than dependency factor after A end;
- no earlier after end: B no earlier than dependency factor after A end.
			</xsd:documentation>
		</xsd:annotation>
        <xsd:simpleContent>
            <xsd:extension base="Dependency1Type">
                <xsd:attribute name="OtherValue"             type="xsd:string"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="Disposition1Type">
        <xsd:simpleContent>
            <xsd:restriction base="CodeType">
                <xsd:enumeration value="Planned"/>
                <xsd:enumeration value="In-Process"/>
                <xsd:enumeration value="Restricted"/>
                <xsd:enumeration value="UnRestricted"/>
                <xsd:enumeration value="Closed"/>
                <xsd:enumeration value="Other"/>
            </xsd:restriction>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="DispositionType">
		<xsd:annotation>
			<xsd:documentation>
Defines Planning and logistics disposition of a material lot or assembly of material lots.
Defined values for the disposition of a material lot are
- Planned: a material lot that does not yet physically exist, is assigned to an operations request (segment requirement) or work request (Part 4 object) or job order (Part 4 object);
- In process: the material lot is in the process of being worked on;
- Restricted: a material lot is not permitted for normal use due to a restriction condition.
	EXAMPLE 5 A material lot can be awaiting a quality decision or a material lot can be physically inaccessible.
- Unrestricted:  material lot is permitted for normal use without restriction; and
- Closed:   material lot has been reconciled as completely consumed, sold or disposed of.
			</xsd:documentation>
		</xsd:annotation>
          <xsd:simpleContent>
            <xsd:extension base="Disposition1Type">
                <xsd:attribute name="OtherValue" type="xsd:string"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="DescriptionType">
        <xsd:simpleContent>
            <xsd:restriction base="TextType"/>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:simpleType name="DurationType">
        <xsd:restriction base="xsd:duration"/>
    </xsd:simpleType>

    <!--     -->
    <xsd:complexType name="EnterpriseFunction1Type">
        <xsd:simpleContent>
            <xsd:restriction base="CodeType">
                <xsd:enumeration value="Order processing"/>
                <xsd:enumeration value="Operations scheduling"/>
                <xsd:enumeration value="Production control"/>
                <xsd:enumeration value="Material and energy control"/>
                <xsd:enumeration value="Procurement"/>
                <xsd:enumeration value="Quality assurance"/>
		        <xsd:enumeration value="Product inventory control"/>
                <xsd:enumeration value="product cost accounting"/>
                <xsd:enumeration value="Product shipping administration"/>
                <xsd:enumeration value="Maintenance management"/>
		        <xsd:enumeration value="Marketing and sales"/>
                <xsd:enumeration value="Research and Development"/>
                <xsd:enumeration value="Engineering"/>
                <xsd:enumeration value="Other"/>
            </xsd:restriction>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="EnterpriseFunctionType">
		<xsd:annotation>
			<xsd:documentation>
Defines the enterprise function of the operations event publisher.
Defined values from Part 1 Functional Model are
order processing, operations scheduling, production control, material and energy control,
procurement, quality assurance, product inventory control, product cost accounting,
product shipping administration, maintenance management, marketing and sales, RD, and engineering.
			</xsd:documentation>
		</xsd:annotation>
         <xsd:simpleContent>
            <xsd:extension base="EnterpriseFunction1Type">
                <xsd:attribute name="OtherValue"                type="xsd:string"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="EquipmentAssetMappingType">
        <xsd:sequence>
            <xsd:element name="EquipmentID"                    type="IdentifierType"/>
            <xsd:element name="PhysicalAssetID"                type="IdentifierType"/>
			<xsd:element name="HierarchyScope"                 type = "HierarchyScopeType"    minOccurs = "0"/>
            <xsd:element name="StartTime"                      type="DateTimeType"            minOccurs="0"/>
            <xsd:element name="EndTime"                        type="DateTimeType"            minOccurs="0"/>
            <xsd:group ref="Extended:EquipmentAssetMapping"                                   minOccurs="0" maxOccurs="1"/>
        </xsd:sequence>
    </xsd:complexType>

    <!--     -->
    <xsd:complexType name="EquipmentLevel1Type">
        <xsd:simpleContent>
            <xsd:restriction base="CodeType">
                <xsd:enumeration value="Enterprise"/>
                <xsd:enumeration value="Site"/>
                <xsd:enumeration value="Area"/>
                <xsd:enumeration value="ProcessCell"/>
                <xsd:enumeration value="Unit"/>
                <xsd:enumeration value="ProductionLine"/>
                <xsd:enumeration value="WorkCell"/>
                <xsd:enumeration value="ProductionUnit"/>
                <xsd:enumeration value="StorageZone"/>
                <xsd:enumeration value="StorageUnit"/>
                <xsd:enumeration value="WorkCenter"/>
                <xsd:enumeration value="WorkUnit"/>
                <xsd:enumeration value="EquipmentModule"/>
                <xsd:enumeration value="ControlModule"/>
                <xsd:enumeration value="Other"/>
            </xsd:restriction>
        </xsd:simpleContent>
    </xsd:complexType>
…(발췌: 전체 102,673자 중 앞 23,376자)
```

### data/source_texts/ref-118.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
<?xml version = "1.0" encoding = "UTF-8"?>

<xsd:schema     xmlns:xsd               = "http://www.w3.org/2001/XMLSchema"
                targetNamespace         = "http://www.mesa.org/xml/B2MML"
                xmlns                   = "http://www.mesa.org/xml/B2MML"
                xmlns:Extended          = "http://www.mesa.org/xml/B2MML-AllExtensions"
                elementFormDefault      = "qualified"
                attributeFormDefault    = "unqualified">

<!-- Import the Extension Schema         -->

<xsd:import     namespace="http://www.mesa.org/xml/B2MML-AllExtensions"
                schemaLocation="B2MML-AllExtensions.xsd"/>

<!-- Include the Common schema   -->

  <xsd:include schemaLocation = "B2MML-Common.xsd"/>

<xsd:annotation>
   <xsd:documentation>

        Copyright 2023 MESA International, Version 0701
        All Rights Reserved. http://www.mesa.org

        This MESA International work (including specifications, documents,
        software, and related items) referred to as the Business To
        Manufacturing Markup Language (B2MML) is provided by the copyright
        holders under the following license.

        Permission to use, copy, modify, or redistribute this Work and its
        documentation, with or without modification, for any purpose and
        without fee or royalty is hereby granted provided MESA International
        is acknowledged as the originator of this Work using the
        following statement:

        "The Business To Manufacturing Markup Language (B2MML) is used
        courtesy of MESA International."

        In no event shall MESA International, its members, or any
        third party be liable for any costs, expenses, losses, damages or
        injuries incurred by use of the Work or as a result of this
        agreement.

        Based upon the ANSI/ISA-95.00.02-2018 Enterprise-Control System
        Integration Part 2: Object Model Attributes Standard and the
        ANSI/ISA-95.00.05-2018 Enterprise-Control System Integration
        Part 5: Business to Manufacturing Transactions.
   </xsd:documentation>

   <xsd:documentation>
      Revision history maintained in GitHub
   </xsd:documentation>

</xsd:annotation>

<!-- Global Elements -->

  <xsd:element  name = "OperationsDefinitionInformation"   type = "OperationsDefinitionInformationType" />
  <xsd:element  name = "OperationsDefinition"              type = "OperationsDefinitionType" />
  <xsd:element  name = "OperationsSegment"                 type = "OperationsSegmentType" />
  <xsd:element  name = "OperationsMaterialBill"            type = "OperationsMaterialBillType" />

<!-- Transaction Elements -->
  <xsd:element name = "GetOperationsDefinitionInformation"         type = "GetOperationsDefinitionInformationType"/>
  <xsd:element name = "ShowOperationsDefinitionInformation"        type = "ShowOperationsDefinitionInformationType"/>
  <xsd:element name = "ProcessOperationsDefinitionInformation"     type = "ProcessOperationsDefinitionInformationType"/>
  <xsd:element name = "AcknowledgeOperationsDefinitionInformation" type = "AcknowledgeOperationsDefinitionInformationType"/>
  <xsd:element name = "ChangeOperationsDefinitionInformation"      type = "ChangeOperationsDefinitionInformationType"/>
  <xsd:element name = "RespondOperationsDefinitionInformation"     type = "RespondOperationsDefinitionInformationType"/>
  <xsd:element name = "CancelOperationsDefinitionInformation"      type = "CancelOperationsDefinitionInformationType"/>
  <xsd:element name = "SyncOperationsDefinitionInformation"        type = "SyncOperationsDefinitionInformationType"/>

  <xsd:element name = "GetOperationsDefinition"            type = "GetOperationsDefinitionType"/>
  <xsd:element name = "ShowOperationsDefinition"           type = "ShowOperationsDefinitionType"/>
  <xsd:element name = "ProcessOperationsDefinition"        type = "ProcessOperationsDefinitionType"/>
  <xsd:element name = "AcknowledgeOperationsDefinition"    type = "AcknowledgeOperationsDefinitionType"/>
  <xsd:element name = "ChangeOperationsDefinition"         type = "ChangeOperationsDefinitionType"/>
  <xsd:element name = "RespondOperationsDefinition"        type = "RespondOperationsDefinitionType"/>
  <xsd:element name = "CancelOperationsDefinition"         type = "CancelOperationsDefinitionType"/>
  <xsd:element name = "SyncOperationsDefinition"           type = "SyncOperationsDefinitionType"/>

  <xsd:element name = "GetOperationsMaterialBill"            type = "GetOperationsMaterialBillType"/>
  <xsd:element name = "ShowOperationsMaterialBill"           type = "ShowOperationsMaterialBillType"/>
  <xsd:element name = "ProcessOperationsMaterialBill"        type = "ProcessOperationsMaterialBillType"/>
  <xsd:element name = "AcknowledgeOperationsMaterialBill"    type = "AcknowledgeOperationsMaterialBillType"/>
  <xsd:element name = "ChangeOperationsMaterialBill"         type = "ChangeOperationsMaterialBillType"/>
  <xsd:element name = "RespondOperationsMaterialBill"        type = "RespondOperationsMaterialBillType"/>
  <xsd:element name = "CancelOperationsMaterialBill"         type = "CancelOperationsMaterialBillType"/>
  <xsd:element name = "SyncOperationsMaterialBill"           type = "SyncOperationsMaterialBillType"/>
<!-- Simple & Complex Types  -->

  <xsd:complexType name = "OperationsDefinitionInformationType">
    <xsd:sequence>
      <xsd:element name = "ID"                          type = "IdentifierType"/>
      <xsd:element name = "Description"                 type = "DescriptionType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "HierarchyScope"              type = "HierarchyScopeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "PublishedDate"               type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "OperationsDefinition"        type = "OperationsDefinitionType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "OperationsSegment"           type = "OperationsSegmentType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "OperationsMaterialBill"      type = "OperationsMaterialBillType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:group   ref  = "Extended:OperationsDefinitionInformation" minOccurs = "0"/>
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name = "OperationsDefinitionType">
    <xsd:sequence>
      <xsd:element name = "ID"                          type = "IdentifierType"/>
      <xsd:element name = "Description"                 type = "DescriptionType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "Version"                     type = "IdentifierType"
                                                        minOccurs = "0"/>
      <xsd:element name = "PublishedDate"               type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "EffectiveStartDate"          type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "EffectiveEndDate"            type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "HierarchyScope"              type = "HierarchyScopeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "OperationsType"              type = "OperationsTypeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "DefinitionType"              type = "DefinitionTypeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "OperationsSegment"           type = "OperationsSegmentType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "BillOfMaterialsID"           type = "IdentifierType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "WorkMasterSourceID"          type = "IdentifierType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "BillOfResourcesID"           type = "IdentifierType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "OperationsMaterialBillID"    type = "IdentifierType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "OperationsDefinitionPatternID"
                                                        type = "IdentifierType"
                                                        minOccurs = "0"/>
      <xsd:group   ref  = "Extended:OperationsDefinition"  minOccurs = "0"/>
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name = "OperationsMaterialBillType">
    <xsd:sequence>
      <xsd:element name = "ID"                          type = "IdentifierType"/>
      <xsd:element name = "Description"                 type = "DescriptionType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "Version"                     type = "IdentifierType"
                                                        minOccurs = "0"/>
      <xsd:element name = "PublishedDate"               type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "EffectiveStartDate"          type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "EffectiveEndDate"            type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "HierarchyScope"              type = "HierarchyScopeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "UseType"                     type = "CodeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "OperationsMaterialBillItem"  type = "OperationsMaterialBillItemType"
                                                        minOccurs = "0" maxOccurs="unbounded"/>
      <xsd:element name = "BillOfMaterialsID"           type = "IdentifierType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:group   ref  = "Extended:OperationsMaterialBill"  minOccurs = "0"/>
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name = "OperationsMaterialBillItemType">
    <xsd:sequence>
      <xsd:element name = "ID"                          type = "IdentifierType"/>
      <xsd:element name = "Description"                 type = "DescriptionType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "Version"                     type = "IdentifierType"
                                                        minOccurs = "0"/>
      <xsd:element name = "PublishedDate"               type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "EffectiveStartDate"          type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "EffectiveEndDate"            type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "UseType"                     type = "CodeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "HierarchyScope"              type = "HierarchyScopeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "AssemblyBillOfMaterialItem"  type = "OperationsMaterialBillItemType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "AssemblyType"                type = "AssemblyTypeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "AssemblyRelationship"        type = "AssemblyRelationshipType"
                                                        minOccurs = "0"/>
      <xsd:element name = "MaterialSpecificationID"     type = "IdentifierType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "Quantity"                    type = "QuantityValueType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:group   ref  = "Extended:OperationsMaterialBillItem"  minOccurs = "0"/>
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name = "OperationsSegmentType">
    <xsd:sequence>
      <xsd:element name = "ID"                          type = "IdentifierType"/>
      <xsd:element name = "Description"                 type = "DescriptionType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "Version"                     type = "IdentifierType"
                                                        minOccurs = "0"/>
      <xsd:element name = "PublishedDate"               type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "EffectiveStartDate"          type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "EffectiveEndDate"            type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "OperationsType"              type = "OperationsTypeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "DefinitionType"              type = "DefinitionTypeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "HierarchyScope"              type = "HierarchyScopeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "Duration"                    type = "DurationType"
                                                        minOccurs = "0"/>
      <xsd:element name = "ProcessSegmentID"            type = "IdentifierType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "BillOfMaterialsID"           type = "IdentifierType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "WorkMasterSourceID"          type = "IdentifierType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "BillOfResourcesID"           type = "IdentifierType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "OperationsMaterialBillID"    type = "IdentifierType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "OperationsSegmentPatternID"  type = "IdentifierType"
                                                        minOccurs = "0"/>
      <xsd:element name = "ParameterSpecification"      type = "ParameterType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "PersonnelSpecification"      type = "OpPersonnelSpecificationType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "EquipmentSpecification"      type = "OpEquipmentSpecificationType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "PhysicalAssetSpecification"  type = "OpPhysicalAssetSpecificationType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "MaterialSpecification"       type = "OpMaterialSpecificationType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "SegmentDependency"           type = "SegmentDependencyType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "DependentOperationsSegmentID"
                                                        type = "IdentifierType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "OperationsSegmentChild"      type = "OperationsSegmentType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:group   ref  = "Extended:OperationsSegment"  minOccurs = "0"/>
    </xsd:sequence>
  </xsd:complexType>

<!-- - - - - - - - - - - - - - - - - - - - - -->
<!-- OperationsInformation Transaction Types -->
<!-- - - - - - - - - - - - - - - - - - - - - -->

  <xsd:complexType name = "GetOperationsDefinitionInformationType">
   <xsd:sequence>
      <xsd:element name = "ApplicationArea"     type = "TransApplicationAreaType"/>
      <xsd:element name = "DataArea">
         <xsd:complexType>
            <xsd:sequence>
              <xsd:element name = "Get"         type = "TransGetType"/>
              <xsd:element name = "OperationsDefinitionInformation"
                                                type = "OperationsDefinitionInformationType"
                                                minOccurs = "1"
                                                maxOccurs = "unbounded"/>
            </xsd:sequence>
         </xsd:complexType>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name = "releaseID"           type="xsd:normalizedString"     use="required"/>
    <xsd:attribute name = "versionID"           type="xsd:normalizedString"     use="optional"/>
  </xsd:complexType>

  <xsd:complexType name = "ShowOperationsDefinitionInformationType">
    <xsd:sequence>
      <xsd:element name = "ApplicationArea"     type = "TransApplicationAreaType"/>
      <xsd:element name = "DataArea">
         <xsd:complexType>
            <xsd:sequence>
              <xsd:element name = "Show"        type = "TransShowType"/>
              <xsd:element name = "OperationsDefinitionInformation"
                                                type = "OperationsDefinitionInformationType"
                                                minOccurs = "1"
                                                maxOccurs = "unbounded"/>
            </xsd:sequence>
         </xsd:complexType>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name = "releaseID"           type="xsd:normalizedString"     use="required"/>
    <xsd:attribute name = "versionID"           type="xsd:normalizedString"     use="optional"/>
  </xsd:complexType>

  <xsd:complexType name = "ProcessOperationsDefinitionInformationType">
    <xsd:sequence>
      <xsd:element name = "ApplicationArea"     type = "TransApplicationAreaType"/>
      <xsd:element name = "DataArea">
         <xsd:complexType>
            <xsd:sequence>
              <xsd:element name = "Process"     type = "TransProcessType"/>
              <xsd:element name = "OperationsDefinitionInformation"
                                                type = "OperationsDefinitionInformationType"
                                                minOccurs = "1"
                                                maxOccurs = "unbounded"/>
            </xsd:sequence>
         </xsd:complexType>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name = "releaseID"           type="xsd:normalizedString"     use="required"/>
    <xsd:attribute name = "versionID"           type="xsd:normalizedString"     use="optional"/>
  </xsd:complexType>

  <xsd:complexType name = "AcknowledgeOperationsDefinitionInformationType">
    <xsd:sequence>
      <xsd:element name = "ApplicationArea"     type = "TransApplicationAreaType"/>
      <xsd:element name = "DataArea">
         <xsd:complexType>
            <xsd:sequence>
              <xsd:element name = "Acknowledge" type = "TransAcknowledgeType"/>
              <xsd:element name = "OperationsDefinitionInformation"
                                                type = "OperationsDefinitionInformationType"
                                                minOccurs = "1"
                                                maxOccurs = "unbounded"/>
            </xsd:sequence>
         </xsd:complexType>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name = "releaseID"           type="xsd:normalizedString"     use="required"/>
    <xsd:attribute name = "versionID"           type="xsd:normalizedString"     use="optional"/>
  </xsd:complexType>

  <xsd:complexType name = "ChangeOperationsDefinitionInformationType">
    <xsd:sequence>
      <xsd:element name = "ApplicationArea"     type = "TransApplicationAreaType"/>
      <xsd:element name = "DataArea">
         <xsd:complexType>
            <xsd:sequence>
              <xsd:element name = "Change"      type = "TransChangeType"/>
              <xsd:element name = "OperationsDefinitionInformation"
                                                type = "OperationsDefinitionInformationType"
                                                minOccurs = "1"
                                                maxOccurs = "unbounded"/>
            </xsd:sequence>
         </xsd:complexType>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name = "releaseID"           type="xsd:normalizedString"     use="required"/>
    <xsd:attribute name = "versionID"           type="xsd:normalizedString"     use="optional"/>
  </xsd:complexType>

  <xsd:complexType name = "RespondOperationsDefinitionInformationType">
    <xsd:sequence>
      <xsd:element name = "ApplicationArea"     type = "TransApplicationAreaType"/>
      <xsd:element name = "DataArea">
         <xsd:complexType>
            <xsd:sequence>
              <xsd:element name = "Respond"     type = "TransRespondType"/>
              <xsd:element name = "OperationsDefinitionInformation"
                                                type = "OperationsDefinitionInformationType"
                                                minOccurs = "1"
                                                maxOccurs = "unbounded"/>
            </xsd:sequence>
         </xsd:complexType>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name = "releaseID"           type="xsd:normalizedString"     use="required"/>
    <xsd:attribute name = "versionID"           type="xsd:normalizedString"     use="optional"/>
  </xsd:complexType>
…(발췌: 전체 40,423자 중 앞 23,445자)
```

### data/source_texts/ref-366.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
/*
 * Copyright (C) 2021 Open Source Robotics Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
*/

#ifndef RMF_TASK__TASK_HPP
#define RMF_TASK__TASK_HPP

#include <rmf_task/Header.hpp>
#include <rmf_task/Phase.hpp>
#include <rmf_task/detail/Backup.hpp>
#include <rmf_task/detail/Resume.hpp>
#include <rmf_task/Constraints.hpp>
#include <rmf_task/Parameters.hpp>
#include <rmf_task/State.hpp>
#include <rmf_task/Estimate.hpp>
#include <rmf_task/Priority.hpp>

#include <rmf_traffic/Time.hpp>

#include <memory>
#include <optional>
#include <functional>

namespace rmf_task {

//==============================================================================
/// Pure abstract interface for an executable Task
class Task
{
public:

  // Declarations
  class Booking;
  using ConstBookingPtr = std::shared_ptr<const Booking>;

  class Tag;
  using ConstTagPtr = std::shared_ptr<const Tag>;

  class Model;
  using ConstModelPtr = std::shared_ptr<const Model>;

  class Description;
  using ConstDescriptionPtr = std::shared_ptr<const Description>;

  class Active;
  using ActivePtr = std::shared_ptr<Active>;
};

//==============================================================================
/// Basic information about how the task was booked, e.g. what its name is,
/// when it should start, and what its priority is.
class Task::Booking
{
public:

  /// Constructor
  ///
  /// \param[in] id
  ///   The identity of the booking
  ///
  /// \param[in] earliest_start_time
  ///   The earliest time that the task may begin
  ///
  /// \param[in] priority
  ///   The priority of the booking
  ///
  /// \param[in] automatic
  ///   Whether this booking was automatically generated
  ///
  /// \param[in] labels
  ///   Labels to describe the purpose of the task dispatch request.
  Booking(
    std::string id,
    rmf_traffic::Time earliest_start_time,
    ConstPriorityPtr priority,
    bool automatic = false,
    const std::vector<std::string>& labels = {});

  /// Constructor
  ///
  /// \param[in] id
  ///   The identity of the booking.
  ///
  /// \param[in] earliest_start_time
  ///   The earliest time that the task may begin.
  ///
  /// \param[in] priority
  ///   The priority of the booking.
  ///
  /// \param[in] requester
  ///   The identifier of the entity that requested this task.
  ///
  /// \param[in] request_time
  ///   The time that this task was booked.
  ///
  /// \param[in] automatic
  ///   Whether this booking was automatically generated, default value as
  ///   false.
  ///
  /// \param[in] labels
  ///   Labels to describe the purpose of the task dispatch request.
  Booking(
    std::string id,
    rmf_traffic::Time earliest_start_time,
    ConstPriorityPtr priority,
    const std::string& requester,
    rmf_traffic::Time request_time,
    bool automatic = false,
    const std::vector<std::string>& labels = {});

  /// The unique id for this booking.
  const std::string& id() const;

  /// Get the earliest time that this booking may begin.
  rmf_traffic::Time earliest_start_time() const;

  /// Get the priority of this booking.
  ConstPriorityPtr priority() const;

  /// Get the identifier of the entity that requested this booking. Returns a
  /// nullopt if no requester was defined.
  std::optional<std::string> requester() const;

  /// Get the time that this booking was requested. Returns a nullopt if no
  /// request time was defined.
  std::optional<rmf_traffic::Time> request_time() const;

  // Returns true if this booking was automatically generated.
  bool automatic() const;

  /// Get the labels that describe the purpose of the task dispatch request.
  std::vector<std::string> labels() const;

  class Implementation;
private:
  rmf_utils::impl_ptr<Implementation> _pimpl;
};

//==============================================================================
/// Basic static information about the task.
class Task::Tag
{
public:

  /// Constructor
  Tag(
    ConstBookingPtr booking_,
    Header header_);

  /// The booking information of the request that this Task is carrying out
  const ConstBookingPtr& booking() const;

  /// The header for this Task
  const Header& header() const;

  class Implementation;
private:
  rmf_utils::impl_ptr<Implementation> _pimpl;
};

//==============================================================================
/// An abstract interface for computing the estimate and invariant durations
/// of this request
class Task::Model
{
public:

  /// Estimate the state of the robot when the task is finished along with
  /// the time the robot has to wait before commencing the task
  virtual std::optional<Estimate> estimate_finish(
    const State& initial_state,
    const Constraints& task_planning_constraints,
    const TravelEstimator& travel_estimator) const = 0;

  /// Estimate the invariant component of the task's duration
  virtual rmf_traffic::Duration invariant_duration() const = 0;

  virtual ~Model() = default;
};

//==============================================================================
/// An abstract interface to define the specifics of this task. This
/// implemented description will differentiate this task from others.
class Task::Description
{
public:

  /// Generate a Model for the task based on the unique traits of this
  /// description
  ///
  /// \param[in] earliest_start_time
  ///   The earliest time this task should begin execution. This is usually
  ///   the requested start time for the task.
  ///
  /// \param[in] parameters
  ///   The parameters that describe this AGV
  virtual ConstModelPtr make_model(
    rmf_traffic::Time earliest_start_time,
    const Parameters& parameters) const = 0;

  struct Info
  {
    std::string category;
    std::string detail;
  };

  /// Generate a plain text info description for the task, given the predicted
  /// initial state and the task planning parameters.
  ///
  /// \param[in] initial_state
  ///   The predicted initial state for the task
  ///
  /// \param[in] parameters
  ///   The task planning parameters
  virtual Info generate_info(
    const State& initial_state,
    const Parameters& parameters) const = 0;

  // Virtual destructor
  virtual ~Description() = default;
};

//==============================================================================
class Task::Active
{
public:
  /// Backup data for the task. The state of the task is represented by a
  /// string. The meaning and format of the string is up to the Task
  /// implementation to decide.
  ///
  /// Each Backup is tagged with a sequence number. As the Task makes progress,
  /// it can issue new Backups with higher sequence numbers. Only the Backup
  /// with the highest sequence number will be kept.
  using Backup = detail::Backup;

  /// Get a quick overview status of how the task is going
  virtual Event::Status status_overview() const = 0;

  /// Check if this task is finished, which could include successful completion
  /// or cancellation.
  virtual bool finished() const = 0;

  /// Descriptions of the phases that have been completed
  virtual const std::vector<Phase::ConstCompletedPtr>&
  completed_phases() const = 0;

  /// Interface for the phase that is currently active
  virtual Phase::ConstActivePtr active_phase() const = 0;

  /// Time that the current active phase started
  virtual std::optional<rmf_traffic::Time> active_phase_start_time() const = 0;

  /// Descriptions of the phases that are expected in the future
  virtual const std::vector<Phase::Pending>& pending_phases() const = 0;

  /// The tag of this Task
  virtual const ConstTagPtr& tag() const = 0;

  /// Estimate the overall finishing time of the task
  virtual rmf_traffic::Duration estimate_remaining_time() const = 0;

  /// Get a backup for this Task
  virtual Backup backup() const = 0;

  /// The Resume class keeps track of when the Task is allowed to Resume.
  /// You can either call the Resume object's operator() or let the object
  /// expire to tell the Task that it may resume.
  using Resume = detail::Resume;

  /// Tell this Task that it needs to be interrupted. An interruption means
  /// the robot may be commanded to do other tasks before this task resumes.
  ///
  /// Interruptions may occur to allow operators to take manual control of the
  /// robot, or to engage automatic behaviors in response to emergencies, e.g.
  /// fire alarms or code blues.
  ///
  /// \param[in] task_is_interrupted
  ///   This callback will be triggered when the Task has reached a state where
  ///   it is okay to start issuing other commands to the robot.
  ///
  /// \return an object to inform the Task when it is allowed to resume.
  virtual Resume interrupt(std::function<void()> task_is_interrupted) = 0;

  // TODO(MXG): Should we have a pause() interface? It would be the same as
  // interrupt() except without the expectation that the robot will do any other
  // task before resuming.

  /// Tell the Task that it has been canceled. The behavior that follows a
  /// cancellation will vary between different Tasks, but generally it means
  /// that the robot should no longer try to complete its Task and should
  /// instead try to return itself to an unencumbered state as quickly as
  /// possible.
  ///
  /// The Task may continue to perform some phases after being canceled. The
  /// pending_phases are likely to change after the Task is canceled, being
  /// replaced with phases that will help to relieve the robot so it can
  /// return to an unencumbered state.
  ///
  /// The Task should continue to be tracked as normal. When its finished
  /// callback is triggered, the cancellation is complete.
  virtual void cancel() = 0;

  /// Kill this Task. The behavior that follows a kill will vary between
  /// different Tasks, but generally it means that the robot should be returned
  /// to a safe idle state as soon as possible, even if it remains encumbered by
  /// something related to this Task.
  ///
  /// The Task should continue to be tracked as normal. When its finished
  /// callback is triggered, the killing is complete.
  ///
  /// The kill() command supersedes the cancel() command. Calling cancel() after
  /// calling kill() will have no effect.
  virtual void kill() = 0;

  /// Skip a specific phase within the task. This can be issued by operators if
  /// manual intervention is needed to unblock a task.
  ///
  /// If a pending phase is specified, that phase will be skipped when the Task
  /// reaches it.
  ///
  /// \param[in] phase_id
  ///   The ID of the phase that should be skipped.
  ///
  /// \param[in] value
  ///   True if the phase should be skipped, false otherwise.
  virtual void skip(uint64_t phase_id, bool value = true) = 0;

  /// Rewind the Task to a specific phase. This can be issued by operators if
  /// a phase did not actually go as intended and needs to be repeated.
  ///
  /// It is possible that the Task will rewind further back than the specified
  /// phase_id if the specified phase depends on an earlier one. This is up to
  /// the discretion of the Task implementation.
  virtual void rewind(uint64_t phase_id) = 0;

  // Virtual destructor
  virtual ~Active() = default;

protected:

  /// Used by classes that inherit the Task interface to create a Resumer object
  ///
  /// \param[in] callback
  ///   Provide the callback that should be triggered when the Task is allowed
  ///   to resume
  static Resume make_resumer(std::function<void()> callback);
};

} // namespace rmf_task

#endif // RMF_TASK__TASK_HPP
```
