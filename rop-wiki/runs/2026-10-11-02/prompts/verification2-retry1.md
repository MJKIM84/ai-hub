(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-11-02
- date: 2026-10-11
- run_type: update (갱신)
- 대상: 23. 업무 시스템 연동 (F. 연동)
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

### runs/2026-10-11-02/target.json

```json
{
  "run_id": "2026-10-11-02",
  "date": "2026-10-11",
  "weekday": "Sun",
  "run_number": 168,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 23,
    "area_name": "23. 업무 시스템 연동",
    "category": "F. 연동",
    "category_letter": "F"
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
  "selection_rationale": "CLI 지정 run_type=update, area=23"
}
```

### runs/2026-10-11-02/research.json

```json
{
  "run_id": "2026-10-11-02",
  "date": "2026-10-11",
  "run_type": "update",
  "target": {
    "area_no": 23,
    "area_name": "23. 업무 시스템 연동",
    "category": "F. 연동"
  },
  "gaps": [
    "섹션 3. 왜 중요한가(주제 페이지 2026-09-25-area01-s3) — 39행 '확인한 연동 사례는 자체 REST·MQTT 인터페이스를 썼다'가 근거(ref-136) 원문과 다름: REST·MQTT 는 미래 확장 계획(미가동)",
    "섹션 4. 핵심 개념과 용어(2026-09-25-area01-s4) — OPC Job Control 은 메서드 이름 나열뿐이고 Update 의 전부 교체, Cancel 의 시작 전 조건, Stop→Ended, Completed·Closed 구분, 2.0 비호환이 없음(ref-131 원문 미열람)",
    "섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 시나리오 하나와 국내 협력 보도(ref-137, 2차 보도·원문 미열람)뿐이고 1차 출처·제조 공장·병원 인계 확인 사례가 없음",
    "섹션 6. 대표 접근법과 기술(2026-09-25-area01-s6) — 요청 응답과 상태 통지·취소 결과의 구분, WMS 쪽 우선순위 변경 허용 범위, MCP 같은 새 접점의 실제 범위 근거가 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스(2026-09-25-area01-s7) — OPC Job Control 2.0 의 1.0 비호환, Open-RMF 응답 스키마, 업무 시스템–로봇 연동 제품 API(SAP Warehouse Robotics·Oracle WMS)와 Mission Dispatch MCP 미반영",
    "섹션 8. 대표 연구와 자료(2026-09-25-area01-s8) — GreenAuto(ref-136) 저자 미확인·REST·MQTT 가동 여부 오기, Lorenz 외(ref-133) 적용 조건 미기재, 국내 발표의 1차 출처 없음",
    "섹션 11. 열린 질문 — oq-019·oq-020·oq-021·oq-002·oq-012 와 연관 oq-046·oq-141·oq-351·oq-365 의 부분 근거 미반영",
    "정정 요청 없음(외부 조사 검증에서 나온 정정만 반영)"
  ],
  "research_questions": [
    "업무 시스템의 요청이 바뀌거나 취소되면 진행 중인 로봇 작업을 어떻게 바꿀 것인가? [분류원문]",
    "oq-020 ISA-95 작업 지시 표준(OPC UA for ISA-95 Job Control)은 갱신·취소·중단·완료를 어떤 상태 조건으로 구별하는가? (섹션 4·6·7 겨냥)",
    "oq-021·oq-351 업무 시스템–관제 연동 계약은 취소 요청의 응답과 실제 취소 결과·취소 불가를 어떻게 나눠 알리는가? (섹션 6·9 겨냥)",
    "oq-019 WMS 는 우선순위 변경을 어떤 작업 상태·권한에서 허용하고, 대기열 정렬 기준은 무엇인가? (섹션 5·6 겨냥)",
    "기존 8절 자료(GreenAuto, Lorenz 외, 국내 협력 발표)의 구현 범위·적용 조건·1차 출처는 원문에서 무엇으로 확인되는가? (섹션 3·5·8 겨냥)",
    "oq-141 MCP·업무 객체 해석 같은 최근 접점은 공개 코드·문서에서 실제로 무엇을 제공하는가? (섹션 6·7 겨냥)",
    "oq-012 로봇 도착과 업무상 인수 확인을 별도 단계로 둔 현장 사례가 있는가? (섹션 5·9 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "OPC 10031-4(OPC UA for ISA-95 Part 4: Job Control) 2.00.0 의 Update 메서드는 아직 시작하지 않은 작업 지시를 새 지시 정보로 갱신하며, 이전에 저장된 정보를 모두 교체한다.",
      "tag": "사실",
      "source_ids": [
        "ref-131"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§6.2.1.9 Update Method: \"This Method updates an existing job order that has not yet been started, with the new order information. All previously stored information is replaced.\" 기존 위키(2026-09-25-area01-s4 40행)는 메서드 이름만 나열",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "같은 명세의 Cancel 메서드는 시작하지 않은(AllowedToStart 또는 NotAllowedToStart) 작업 지시를 취소하고 저장된 정보를 지우며, 성공하면 JobOrderList 에 그 JobOrderID 의 작업 지시가 남지 않아야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-131"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§6.2.1.12 Cancel Method: 시작 전(AllowedToStart·NotAllowedToStart) 작업 지시를 취소하고 \"removes the stored information\". 성공 후 JobOrderList 에 해당 JobOrderID 가 없어야 함(shall)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f3",
      "claim": "같은 명세의 Stop 메서드는 시작된 작업 지시를 멈추며, 성공하면 작업 지시는 Ended 상태여야 한다(Abort 가 Aborted 로 바꾸는 것과 구별된다).",
      "tag": "사실",
      "source_ids": [
        "ref-131"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§6.2.1.11 Stop Method: \"After successful execution of the method, job order in the JobOrderList shall be in state Ended.\" Abort→Aborted(§6.2.1.10)는 기존 위키 s4 40행에 있어 새로 넣지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f4",
      "claim": "같은 명세에서 Ended 의 하위 상태 Completed 는 작업 지시의 실행이 끝난 상태이고, Closed 는 완료 뒤 더 이상 후처리도 하지 않는 상태로 구분된다.",
      "tag": "사실",
      "source_ids": [
        "ref-131"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§6.2.4 표 45: Completed \"has been completed and is no longer in execution\", Closed \"completed and no further post processing is performed\". §6.2.1: Ended 하위 상태는 결과 수신 전 후처리 필요 여부를 드러낼 수 있음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f5",
      "claim": "Job Control 2.0 은 1.0 과 호환되지 않는 변경(breaking changes)을 담고 새 namespace 를 정의해, 이전 응용이 필요하면 두 모델을 함께 지원할 수 있게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-131"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§1 Scope: \"Version 2.0 ... is not compatible with version 1.0 ... defines a new namespace\". OPC 공식 판 목록의 현행 2.00.0·2024-01-31 표시는 기존 위키 s4·s7 에 있어 새로 넣지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "업무 쪽 '취소'를 로봇 명령 하나로 옮기기 전에 작업의 현재 상태(시작 전·실행 중·종료 후), 지울 기록과 남길 이력, 실행 종료 뒤 후처리 여부를 먼저 정해야 할 것으로 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-131"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1~f4 에서 도출: OPC Job Control 은 시작 전 취소(Cancel, 기록 제거)·실행 중 종료(Stop→Ended, Abort→Aborted)·완료와 후처리 종료(Completed·Closed)를 서로 다른 메서드·상태로 둔다. 이 상태와 VDA 5050·Open-RMF 상태의 표준 매핑은 확인 못 함(oq-020)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "Open-RMF rmf_api_msgs 의 dispatch_task_response 스키마는 성공 분기(success=true)에서 success 와 작업 상태(task_state 를 따르는 state)를 필수로 요구하고, 실패 분기(success=false)에는 실패 이유를 담는 errors 배열을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1453"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "커밋 e9b7630 고정본 dispatch_task_response.json: oneOf[0].required = [\"success\",\"state\"], state 는 $ref task_state.json; oneOf[1] 은 success=false 와 errors(error.json 배열). 실패 분기에는 required 없음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "같은 저장소의 cancel_task_response 스키마는 자체 필드 없이 simple_response 를 참조하며, simple_response 는 성공이면 success=true 만, 실패면 success=false 와 errors 를 필수로 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1454",
        "ref-1455"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "cancel_task_response.json: \"$ref\": \"simple_response.json\". simple_response.json 설명 'only indicates success and describes any errors', 실패 분기 required [success, errors]. 취소 요청의 type·task_id 필수는 기존 위키 s6 에 있음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "따라서 Open-RMF 의 취소 응답은 요청 처리의 성패만 알리고, 작업이 실제로 멈춰 canceled 상태가 됐는지는 작업 상태(task_state)를 따로 관측해 확인해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1454",
        "ref-1455"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f8 에서 도출. 작업 상태의 canceled·completed 값은 기존 위키 s4 42행(ref-111). 스키마만으로 응답과 실제 정지의 시간 관계·중복 요청 효과는 확인 못 함",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f10",
      "claim": "SAP Warehouse Robotics(SAP BTP 기반 제품, SAP EWM 과 다른 제품)의 2024-07-10 자 'APIs for Integration via Fleet Management Systems' 문서는 제조사 관제(FMS) 연동 API 를 Deprecated 로 표시한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1456",
        "ref-1458"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤더 주장: ref-1456 §1 제목 '(Deprecated)'와 주석 \"This API is deprecated.\"; 문서일 2024-07-10. ref-1458 §1: SAP Warehouse Robotics 는 SAP BTP 위에 만든 제품이며 SAP EWM 사용자가 로봇을 통합하는 데 쓴다",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f11",
      "claim": "같은 SAP Warehouse Robotics FMS 연동 문서는 시스템 설계를 단순하게 하려고 FMS 가 요청에 대한 응답을 관련 콜백 메서드 호출보다 먼저 돌려주도록 요구한다(요청→응답→콜백 순서).",
      "tag": "추정",
      "source_ids": [
        "ref-1456"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤더 주장: §1.5 p7: \"SAP Warehouse Robotics requires the response to be returned before calling the relevant API method for callback message.\" 이후 1 요청, 2 응답, 3 콜백 순서를 그림으로 설명",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f12",
      "claim": "같은 문서의 취소 절차에서 FMS 는 로봇 작업 취소에 성공하면 Update Robot Task Status 로 taskStatus 를 CANCELLED 로 알리고, 취소할 수 없으면 별도 메서드 Update Robot Task Cancelation Status 로 알린다.",
      "tag": "추정",
      "source_ids": [
        "ref-1456"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤더 주장: §1.6.2 Cancel Robot Tasks p12: 취소되면 Update Robot Task Status(\"taskStatus\"=\"CANCELLED\"), 취소 불가면 Update Robot Task Cancelation Status 호출. CANCELLED 일 때 작업 phase·상태는 null(§1.6.1)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f13",
      "claim": "같은 문서의 공통 메시지는 UUID 형식의 messageId 를 필수로 두고, 작업 처리 예시는 이와 별도인 robotTaskId 로 로봇 작업을 가리켜 메시지 식별과 작업 식별을 나눈다.",
      "tag": "추정",
      "source_ids": [
        "ref-1456"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤더 주장: §1.3 Common Messages: messageId 필수, 'Message ID in UUID format'. §1.6.1 예시 본문에 robotTaskId. 실제 운영의 중복 제거·재시도 보장(exactly-once)은 문서에 없음(oq-046 관련)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f14",
      "claim": "업무 시스템–관제 인터페이스를 비교할 때 '접수 응답', '진행 통지(콜백·상태)', '취소 결과', '업무 확정'을 따로 보는 것이 좋아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-1456",
        "ref-1453",
        "ref-1454"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f7·f8·f11·f12 에서 도출: SAP 의 폐기된 FMS 계약과 Open-RMF 응답 스키마 모두 요청 응답과 이후 상태 통지를 나눈다. SAP 현재 권장 연동 경로의 계약은 확인 못 함",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "Oracle WMS Cloud 26c REST API 의 Change Task Priority API 는 Ready·Held·Created 상태인 작업의 우선순위만 바꿀 수 있다고 명시한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1457"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤더 주장: Change Priority 문서 도입 문단: \"change the priority of a task which is in Ready, Held or Created s status\". 작업 ID 또는 작업 번호로 POST 호출. 문서 ID G55063-04, Release 26C",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "제약",
      "vendor_claim": true
    },
    {
      "id": "f16",
      "claim": "같은 API 는 외부 시스템이 다른 작업의 긴급도에 따라 작업 우선순위를 바꿀 수 있게 하되, Task/Change task priority 권한이 켜져 있을 때만 쓸 수 있다.",
      "tag": "추정",
      "source_ids": [
        "ref-1457"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤더 주장: 도입 문단: 외부 시스템도 긴급도에 따라 하나 이상의 작업 우선순위 변경 가능, 단 'Task/Change task priority Permission' 활성 시에만. 요청 본문 priority 는 정수 코드(예 3, 20)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "제약",
      "vendor_claim": true
    },
    {
      "id": "f17",
      "claim": "SAP Warehouse Robotics 의 integration services 경로 문서(판 2308)는 로봇 배정 최적화를 켜지 않으면 로봇이 속한 자원 그룹의 큐 순서를 따르고(첫 큐를 끝내야 다음 큐), 큐 안의 창고 오더를 latest starting date(LSD) 순으로, LSD 가 없으면 생성 시각 순으로 정렬한다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1458"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤더 주장: §2 Warehouse Order Processing p4: 최적화 미사용 시 queue sequence 확인, \"sorts the warehouse orders in a queue by the latest starting dates (LSDs). If there are no LSDs, ... by the creation time\". 최적화 사용 시에도 LSD 로 먼저 정렬. FMS API(ref-1456)와 다른 연동 경로",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "제약",
      "vendor_claim": true
    },
    {
      "id": "f18",
      "claim": "우선순위 변경 가능 여부는 업무 작업의 상태와 로봇 실행 단계에 대해 따로 검사하고, 대기열 재정렬과 진행 중 작업 선점은 별도 정책으로 두는 것이 좋아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-1457",
        "ref-1458"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f15~f17 에서 도출: Oracle 은 시작 전 상태(Ready·Held·Created)만 변경을 허용하고, SAP 통합 서비스는 대기 큐 안 정렬 규칙만 밝힌다. 진행 중 Open-RMF 작업의 재정렬 방법과 업체 간 우선순위 숫자의 대응은 확인 못 함(oq-019)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "Lopes 외(Applied Sciences 2025, GreenAuto)는 플릿 관리 시스템과 IIoT 시스템의 통신이 당시 구현에서 아직 활성화되지 않았다고 명시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-136"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§5.2 그림 10 설명(p11): \"the communication with IIoT systems is not yet active in the current implementation\"",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "같은 문단은 MES·ERP 에 로봇 위치·상태·이벤트 같은 정형 데이터를 내주는 REST API, AMR 의 실시간 이벤트 발행을 위한 MQTT broker, VDA 5050 연동을 모두 미래 확장으로 설계했다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-136"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "p11: 그림 하단 층은 \"this future capability\"로 REST API(MES·ERP 용)와 MQTT broker(\"intended to enable real-time event publishing from the AMRs\")를 포함; VDA 5050 도 \"future integration\"",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "같은 논문 §4 에서 플릿 관리 시스템 개발에 쓴 로봇은 서로 다른 제조사의 AMR 2대와 AGV 1대(ABB ASTI TriBot)였다.",
      "tag": "사실",
      "source_ids": [
        "ref-136"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4 Robot System Description p6: \"Three mobile robots ... consisting of two AMRs and one AGV, from different brands\". §6.2 의 최대 20대 동시 감시와의 관계는 확인 못 함(oq-365)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f22",
      "claim": "정정: Lopes 외 논문은 REST·MQTT 연동을 사용했다고 하지 않고 MES·ERP용 REST API 와 AMR 실시간 이벤트·IIoT용 MQTT broker 를 미래 확장 계획(당시 미가동)으로 두므로, 2026-09-25-area01-s3.md 39행 '확인한 연동 사례는 자체 REST·MQTT 인터페이스를 썼다'와 s8 42행 GreenAuto 문장은 '계획(미가동)'으로 고쳐야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-136"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f19·f20 근거. s3 39행 [추정][^ref-136], s8 42행 '로봇 이벤트는 MQTT 로 발행하며 ... 설계했다고 기술한다' [사실][^ref-136]. 원문 p11 'not yet active', 'future capability'. 저자 '미확인'도 17명으로 정정",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "Lorenz·Otto·Gendreau(Networks 2025)의 온라인 주문 묶음·순서·경로 문제(OOBSRP) 모델은 피커 한 명이 맡는 피킹 구역 하나를 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-133"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§2 p160: \"OOBSRP considers one picking zone of a single picker.\" 복수 피커·주문 납기 확장은 §5 향후 연구로 둠",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "같은 연구의 로봇 카트(Robot) 조건은 피커가 배치를 마치면 빈 로봇을 바로 쓸 수 있다고 가정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-133"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§2 p160: \"assume that an empty robot is immediately available for the picker after she has completed a batch\". 근거로 피커당 로봇 2대면 대개 대기가 없다는 선행 연구를 듦",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "같은 연구의 계산실험(§4·§4.2)은 개입형 재최적화인 Pcart·Robot 두 시스템만 대상으로 OBSRP* 인스턴스 2,600개를 만들어 그중 2,380개 이상을 최적으로 풀고 Reopt 결과와 비교했으며, §4.1 은 데이터 생성 절이다.",
      "tag": "사실",
      "source_ids": [
        "ref-133"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4 서두 p168: \"we create 2600 OBSRP* instances and solve more than 2380 of those to optimality\", 개입형 Pcart·Robot 으로 한정. §4.1: 2 시스템 × 10 설정 × 13 주문 크기 × 10 = 2,600. 결과는 §4.2",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "Lorenz 외 결과는 상위 계획 갱신 정책을 비교하는 참고로 두되, 다수 피커·로봇 대기·메시지 멱등성·재고 확정 같은 연동 조건의 검증 근거로 쓰지 않는 것이 맞아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-133"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f23~f25 에서 도출: 단일 피커·단일 구역, 빈 로봇 즉시 가용 가정, 생성 인스턴스 계산실험. 기존 위키 s8 40행의 점근적 최적성 서술에 조건을 덧붙이는 것이며 결과를 부정하지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "아르고(테크타카)는 2025-01-21 발표에서 자사 WMS 와 플로틱 자율주행로봇을 연동한 자동화 모델을 설계해 남이천 물류센터에서 실증하고, 플로틱이 오더 피킹 특화 로봇 30대를 지원한다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-1459"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "아르고 공식 블로그 발표(Jan 21, 2025) 본문: '남이천 물류센터에서 실증한다. 이를 위해 플로틱은 오더 피킹 작업에 특화된 로봇 30대를 지원한다'. 기존 ref-137 보도와 같은 사건의 1차 출처이며 실증 결과는 미확인",
      "as_of": "2026-10-11",
      "site_type": "물류창고",
      "flow_item": "수행 자원"
    },
    {
      "id": "f28",
      "claim": "같은 발표에서 플로틱 대표는 앞선 실증사업에서 수작업으로 20분 이상 걸리던 오더 피킹을 10분 이내로 줄였다고 말했으나, 이는 남이천 30대 사업의 성과가 아니다.",
      "tag": "추정",
      "source_ids": [
        "ref-1459"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: '앞서 실증사업에서도 수작업으로 20분 이상 소요되는 오더 피킹 작업을 10분 이내로 단축'. 측정 조건·현장·기간 미공개, 남이천 사업의 완료 결과로 합치지 않음",
      "as_of": "2026-10-11",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f29",
      "claim": "LG CNS 는 2026-07-16 고객 사례에서 HD현대일렉트릭 청주 배전캠퍼스 신공장에 자재 입고·보관·생산라인 공급·완제품 이송·출하를 조율하는 창고 제어 시스템(WCS)과 SCADA 기반 통합 관제를 구축했다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1460"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Solution 2 'WCS와 SCADA 기반 통합 제어·관제 체계 구축'. AMR·ACR·디팔레타이징 로봇 구성 설명은 있으나 다제조사 수, API, 주문 상관키, 생산계획 변경 승인 규칙은 공개되지 않음",
      "as_of": "2026-10-11",
      "site_type": "제조 공장",
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f30",
      "claim": "SAP Architecture Center 의 참조구조 'Warehouse Pick & Place with Embodied AI Robotics'(2026-05-12 갱신)는 이송 오더를 만들고 관리하지만 물건을 집지는 못하는 디지털 warehouse AI agents 와 구별되는 Embodied AI agents 의 세 가지 주요 skill 중 하나로 업무 객체의 의미 이해(WMS 데이터 속성이 물리 작업 실행에 뜻하는 바, 예: 주문 우선순위·취급 요건)를 든다.",
      "tag": "추정",
      "source_ids": [
        "ref-1461"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤더 주장: 'Last updated on May 12, 2026'. Key Components: \"Embodied AI agents for warehouse operations have three main skills\" 중 'Semantic Understanding of Business Objects'. 최초 발행일 미확인",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f31",
      "claim": "SAP 뉴스(2025-11-05 게시, 2026-06-18 수정)는 Bosch·Aimbo 공동 개념검증에서 Aimbo 의 휴머노이드 Anigon 1대가 SAP EWM 의 배송 정보·주문 우선순위·보관 위치를 실시간 업무 문맥으로 받아 창고 작업을 수행했고, 이 사업은 탐색 단계로 전용 beta·test 시스템 환경에서 검증됐다고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-1462"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 'Enabling autonomous warehouse execution at Bosch' 절, \"a single Anigon unit\", \"validated in dedicated beta and test system environments\". 사례 실시일 미확인, 생산 운영·다제조사 WMS 확정의 근거 아님",
      "as_of": "2026-10-11",
      "site_type": "물류창고",
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f32",
      "claim": "NVIDIA Isaac Mission Dispatch README(커밋 56455eb 고정본)의 Latest Update 표는 2026-03 에 Mission Dispatch MCP 추가를, 2026-08 에 VDA5050 3.0 지원과 generic action node 추가를 기록한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1341"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Latest Update 표: '2026-08 | VDA5050 3.0 support, add generic action node.', '2026-03 | Mission Dispatch MCP, VDA5050 2.2 map distribution updates, ARM64 support'. 연월 표기까지만 사용 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f33",
      "claim": "같은 커밋의 Mission Dispatch MCP 서버는 도구 11개(로봇 상태·미션 상태·미션 중 로봇·유휴 로봇·플릿 요약·로봇 건강 점검·미션 큐·최근 실패 조회, 연결 시험, 로봇 등록, 좌표 이동 미션 전송)를 등록하며, 미션 취소 도구는 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1341"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "mission-dispatch-mcp server.py list_tools: GET_ROBOT_STATUS·GET_MISSION_STATUS·GET_ROBOTS_ON_MISSIONS·GET_IDLE_ROBOTS·GET_FLEET_SUMMARY·CHECK_ROBOT_HEALTH·GET_MISSION_QUEUE·GET_RECENT_FAILURES·TEST_CONNECTION·CREATE_ROBOT·DISPATCH_MISSION. cancel 도구 없음. 코드 실행은 안 함",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "같은 MCP 서버의 이동 미션 핸들러(_handle_dispatch_mission)는 queries.py 의 dispatch_move_mission 을 호출하고, 이 함수는 경유점 하나짜리 route 미션 트리와 timeout·deadline 을 담아 Mission Dispatch REST API 의 mission 경로로 POST 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1341"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "server.py _handle_dispatch_mission → md_client.dispatch_move_mission(robot, x, y, theta, name); queries.py: data 에 mission_tree(route waypoints 1개)·timeout·deadline·needs_canceled=False, `return self._post_request(\"mission\", data)`",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f35",
      "claim": "robotmcp 의 demos-ros-mcp-server 예제 1 README 는 Ubuntu 22.04·ROS 2 Humble·Ignition Gazebo Fortress 에서 ROS-MCP 서버로 창고 시뮬레이션 속 Tugbot 1대를 자연어로 이동시키고 라이다·주행거리 센서와 위치를 조회하는 예시를 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1463"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "커밋 edbc642 고정본 1_Gazebo_Tugbot/README.md 'Tested On': ROS 2 Humble, Ignition Gazebo Fortress. 'Sample Prompts': 이동·정지, 토픽 조회, /scan·odometry 조회. 단일 로봇 시뮬레이션이며 업무 시스템 연동은 없음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f36",
      "claim": "MCP 를 업무 요청의 접점으로 평가할 때는 공개 코드가 주는 도구 범위(조회·등록·좌표 이동, 취소 없음)와 업무 요구(주문 ID 대응·허용 상태 검사·실행 전 승인·결과 대조·취소)를 따로 확인해야 하며, 공개 코드의 존재를 다사업자 WMS 주문·재고 처리의 운영 검증으로 볼 수 없다.",
      "tag": "의견",
      "source_ids": [
        "ref-1341",
        "ref-1463"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f33~f35 에서 도출. Mission Dispatch 의 일반 REST 미션 서비스와 MCP 가 노출하는 도구 범위는 다르다. 실행 전 승인 관문 위치는 확인 못 함(oq-141)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f37",
      "claim": "Tartu 대학병원 실증의 시료 운반 절차에서는 로봇이 실험실에 도착하면 직원이 화면 버튼으로 시료를 모두 꺼냈음을 확인하고 ingestor 가 RMF 에 인수 완료를 알린 뒤에야 로봇을 ICU 로 되돌리는 요청이 나간다.",
      "tag": "사실",
      "source_ids": [
        "ref-869"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§3.1 그림 8·표 1 step 8~13: 9 'User presses a button ... confirming that all items are removed from the bin', 10 ingestor 가 RMF 에 완료 통지, 11 ICU 복귀 요청, 13 ICU 도착. ICU→검사실 운반 자체는 기존 위키에 있음",
      "as_of": "2026-10-11",
      "site_type": "병원",
      "flow_item": "완료·인계"
    },
    {
      "id": "f38",
      "claim": "같은 논문은 병원 안 운반 실증을 PAL Robotics TIAGo 1대로 했고, TIAGo·Clearpath Jackal 두 이기종 로봇을 RMF 로 관리하는 능력은 별도 시험 환경에서 검증했으며, 병원 안에는 여러 배송 로봇을 아직 적용하지 않았다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-869"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4 'Increasing the number and diversity of robots': 시험 환경에서 TIAGo·Jackal 검증, \"we are yet to apply multiple delivery robots inside the Hospital\". 병원 내 이기종 플릿 상시 운영 사례가 아님",
      "as_of": "2026-10-11",
      "site_type": "병원",
      "flow_item": "수행 자원"
    }
  ],
  "sources": [
    {
      "id": "ref-131",
      "org": "OPC Foundation / ISA",
      "title": "OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4)",
      "published": "2024-01-31",
      "url": "https://reference.opcfoundation.org/specs/OPC-10031-4/6.2",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "OPC 10031-4 Job Control 2.00.0 명세. 이번에 전체 판(§1 Scope, §6.2.1.9~12 Update·Abort·Stop·Cancel, §6.2.4 표 45)을 원문 대조했고, 공식 판 목록의 현행 2.00.0·2024-01-31 표시를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://reference.opcfoundation.org/specs/OPC-10031-4/full",
      "source_unopened": false
    },
    {
      "id": "ref-1453",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_response.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/dispatch_task_response.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Open-RMF 작업 배정 요청 응답 스키마(커밋 e9b7630 고정본). 성공 분기는 success·state(task_state) 필수, 실패 분기는 errors 배열을 둔다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/dispatch_task_response.json",
      "source_unopened": false
    },
    {
      "id": "ref-1454",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_response.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/cancel_task_response.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Open-RMF 작업 취소 요청 응답 스키마(커밋 e9b7630 고정본). 자체 필드 없이 simple_response.json 을 참조한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/cancel_task_response.json",
      "source_unopened": false
    },
    {
      "id": "ref-1455",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/simple_response.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/simple_response.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "성공 여부와 오류만 알리는 Open-RMF 응답 틀 스키마(커밋 e9b7630 고정본). 성공이면 success=true, 실패면 success=false 와 errors 가 필수다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/simple_response.json",
      "source_unopened": false
    },
    {
      "id": "ref-1456",
      "org": "SAP",
      "title": "APIs for Integration via Fleet Management Systems (API for Integration with Fleet Management Systems (Deprecated))",
      "published": "2024-07-10",
      "url": "https://help.sap.com/doc/a02ad3695d5845fca1678810cb83562b/LATEST/en-US/379d6d880e5d4007b3751618080da80f_1.pdf",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "SAP Warehouse Robotics(SAP BTP 기반)와 제조사 관제(FMS)를 잇는 폐기(Deprecated) API 문서. 요청→응답→콜백 순서, messageId, 취소 성공(CANCELLED)·취소 불가 통지 메서드를 정의한다. LATEST URL 이라 확보본(2024-07-10) 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1457",
      "org": "Oracle",
      "title": "WMS REST API Guide — Change Priority (Oracle Warehouse Management Cloud 26c)",
      "published": "2026-08-14",
      "url": "https://docs.oracle.com/en/cloud/saas/warehouse-management/26c/owmre/change-priority.html",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "Oracle WMS Cloud 26c 의 작업 우선순위 변경 API 문서(문서 ID G55063-04, Release 26C; 날짜는 페이지 메타데이터 dcterms.created). Ready·Held·Created 상태 작업만 변경할 수 있고 Task/Change task priority 권한이 필요하다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1458",
      "org": "SAP",
      "title": "End-User Information for Integration via Integration Services (SAP Warehouse Robotics, Document Version 2308)",
      "published": "2023-08-19",
      "url": "https://help.sap.com/doc/f08ea8f8686c46e89f1d7ed121f19d68/LATEST/en-US/b82aa9c86bd74777b86ec7f5766252d0.pdf",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "SAP Warehouse Robotics(SAP BTP 기반, SAP EWM 사용자의 로봇 통합 제품)의 integration services 경로 사용자 문서. 최적화 미사용 시 큐 순서와 LSD·생성 시각 정렬 규칙을 설명한다. LATEST URL 이라 확보본(판 2308) 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1459",
      "org": "아르고 풀필먼트(테크타카)",
      "title": "아르고, 플로틱과 로봇 기반 물류 생산성 향상 실증 본격 실시",
      "published": "2025-01-21",
      "url": "https://blog.argoport.com/pr-robotcooperation250121",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "테크타카(아르고)의 공식 발표. 자사 WMS 와 플로틱 로봇 연동 자동화 모델을 남이천 물류센터에서 실증하고 플로틱이 오더 피킹 로봇 30대를 지원한다고 밝힌다. 기존 ref-137 보도의 1차 출처다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1460",
      "org": "LG CNS",
      "title": "로봇 기반 물류 자동화와 통합 관제로 HD현대일렉트릭 신공장의 새로운 운영 체계를 구축하다",
      "published": "2026-07-16",
      "url": "https://www.lgcns.com/kr/moa/customer-story/detail.smartlogistics-robotic-logistics-2607-1",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "LG CNS 고객 사례. HD현대일렉트릭 청주 배전캠퍼스 신공장에 AMR·ACR 기반 물류 자동화와 WCS·SCADA 통합 제어·관제를 구축했다고 설명한다(공급자 단독 설명).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1461",
      "org": "SAP Architecture Center",
      "title": "Warehouse Pick & Place with Embodied AI Robotics",
      "published": null,
      "url": "https://architecture.learning.sap.com/docs/ref-arch/7e4168",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "SAP 참조구조(2026-05-12 갱신, 최초 발행일 미확인). 디지털 warehouse AI agents 와 구별되는 Embodied AI agents 의 세 가지 주요 skill(업무 객체의 의미 이해 포함)을 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1462",
      "org": "SAP (Lukasz Ostrowski, SAP News Center)",
      "title": "How SAP Brings Business AI into the Physical World: New Robotics Pilots Across Warehouse, Manufacturing, and Inspection Use Cases",
      "published": "2025-11-05",
      "url": "https://news.sap.com/2025/11/sap-physical-ai-partnerships-new-robotics-pilots/",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "SAP 로봇 파일럿 소개 뉴스(게시 2025-11-05, 수정 2026-06-18 article:modified_time). Bosch·Aimbo 단일 Anigon 개념검증 등 파트너 사례를 공급자 관점에서 소개한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1463",
      "org": "robotmcp",
      "title": "demos-ros-mcp-server — Example 1: Tugbot Warehouse Simulation (Ignition Gazebo) README",
      "published": null,
      "url": "https://github.com/robotmcp/demos-ros-mcp-server/blob/edbc642849bdde1187771a15e557ec9e219184a5/1_Gazebo_Tugbot/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "ROS-MCP 서버로 Gazebo 창고 시뮬레이션의 Tugbot 1대를 자연어로 이동·센서 조회하는 데모 README(커밋 edbc642 고정본, 커밋일 미확인).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/robotmcp/demos-ros-mcp-server/edbc642849bdde1187771a15e557ec9e219184a5/1_Gazebo_Tugbot/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-136",
      "org": "Lopes, D., Pereira, T., Gonçalves, A. 외 (저자 17명; Applied Sciences, MDPI)",
      "title": "Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector",
      "published": "2025-06-27",
      "url": "https://www.mdpi.com/2076-3417/15/13/7235",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Applied Sciences 15(13) 7235, DOI 10.3390/app15137235, 저자 17명(David Lopes 외). 자동차 부문 GreenAuto 다제조사 플릿 감시 시스템으로, IIoT·MES·ERP 연동은 미래 확장(미가동)이다. 기존 ref-136 저자 '미확인' 정정.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://mdpi-res.com/d_attachment/applsci/applsci-15-07235/article_deploy/applsci-15-07235.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-133",
      "org": "Lorenz, Otto, & Gendreau (Networks, Wiley)",
      "title": "Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization?",
      "published": "2025-05",
      "url": "https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Networks 86(2):157–173, 저자 3명(Catherine Lorenz, Alena Otto, Michel Gendreau), 심사 승인 2025-04-07, 온라인 발행 2025-05(일자 미확인). 이번에 대학 저장소(mediaTUM) PDF 로 §2·§4 를 원문 대조했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://mediatum.ub.tum.de/doc/1835706/document.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-1341",
      "org": "NVIDIA (nvidia-isaac GitHub)",
      "title": "isaac_mission_dispatch — README",
      "published": null,
      "url": "https://github.com/nvidia-isaac/isaac_mission_dispatch",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "VDA 5050 기반 미션 배포 서비스 README. 이번에 커밋 56455eb 고정본의 Latest Update 표와 Mission Dispatch MCP 코드(server.py·queries.py)·MCP 튜토리얼을 확인했다(커밋일 미확인).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/nvidia-isaac/isaac_mission_dispatch/56455eb757173cb6c0babe2e52cfb2a8e3a8bdee/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-869",
      "org": "Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Tartu 대학병원에서 Open-RMF 로 TIAGo 가 ICU 혈액 시료를 검사실로 운반한 현장 시험. 이번에 표 1 의 인수 확인 후 ICU 복귀 절차와 §4 의 TIAGo·Jackal 별도 시험 환경 검증을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/integration/business-system-integration.md",
      "sections": [
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11"
      ],
      "rationale": "갱신(차등). 대상 문장은 실제 위키 위치로 적는다(메모가 가리킨 로컬 보존본은 저장소에 없음). 섹션 3(주제 페이지 2026-09-25-area01-s3) — 39행 '확인한 연동 사례는 자체 REST·MQTT 인터페이스를 썼다 [추정][^ref-136]'를 'MES·ERP용 REST API, AMR 실시간 이벤트·IIoT용 MQTT broker 는 계획(미가동)'으로 정정(f22, 근거 f19·f20). / 섹션 4(2026-09-25-area01-s4 40행 작업 지시 항목) — Update 전부 교체(f1), Cancel 시작 전 조건·기록 제거(f2), Stop→Ended(f3), Completed·Closed 구분(f4); ref-131 원문 열람으로 '(원문 미열람)' 해제. Abort→Aborted·메서드 목록·2.00.0 2024-01-31 은 기존 내용 확인(s4 40행·s7 44행)으로 중복 추가 안 함. / 섹션 5 — 국내 문단(본문 88행·s8 43행)에 1차 출처 ref-1459 병기와 '30대 지원 발표, 20분 이상→10분 이내는 앞선 실증 성과'(f27·f28, 벤더 주장), 제조 공장 사례 LG CNS WCS·SCADA(f29, 벤더 주장), 병원 인계 확인 후 ICU 복귀·TIAGo 1대/Jackal 별도 시험(f37·f38; ICU→검사실 운반은 ref-869 기존 내용 확인), Bosch·Aimbo 단일 Anigon 개념검증(f31, 벤더 주장·beta/test 환경). / 섹션 6(2026-09-25-area01-s6) — 취소 번역 전 상태 확인(f6), Open-RMF 배정 응답 success·state 필수(f7)와 취소 응답 simple_response 참조(f8)·관측 분리(f9), SAP Warehouse Robotics FMS API(폐기)의 응답-콜백 순서·취소 결과 통지·messageId/robotTaskId(f10~f13, 제품명은 SAP Warehouse Robotics(SAP BTP 기반)로 쓰고 EWM 과 구별), 인터페이스 비교 열(f14), 우선순위 변경 허용 상태·권한·LSD 정렬(f15~f18), Mission Dispatch MCP 도구 범위·이동 경로·Tugbot 시뮬레이션(f33~f36). priority 의 fleet 스키마 일치·cancel 요청 type·task_id 필수·task_state 상태 열거는 기존 내용 확인(s6 43행·s4 42행), phase별 취소 반응(rmf_task README ref-404·Task.hpp ref-366)은 2026-10-10 area24-s6·채팅 트랙 stage-3 에 있어 넣지 않음. / 섹션 7(2026-09-25-area01-s7 표) — OPC Job Control 행에 2.0 의 1.0 비호환·새 namespace(f5)와 '상태 전이는 원문 미열람' 해제, Open-RMF 행에 dispatch·cancel 응답 스키마(f7·f8), 새 행: SAP Warehouse Robotics FMS API(폐기, f10), Oracle WMS Change Priority API(f15·f16), Mission Dispatch MCP(2026-03)·VDA5050 3.0 지원(2026-08) 기록(f32), SAP Embodied AI 참조구조(f30). ISA-95 Part 1 2025 발행 발표(ref-002)는 기존 내용 확인으로 넣지 않음. GS1 CBV 2.0 receiving·arriving·accepting·unloading 은 area02·17·24 와 EPCIS 인계 페이지(ref-044)에 있어 넣지 않음. / 섹션 8(2026-09-25-area01-s8) — 42행 GreenAuto 항목 저자 17명·발행일로 서지 정정, 'REST·MQTT·VDA 5050 은 미래 확장(미가동), 개발 대상 AMR 2·AGV 1'(f19~f22; 최대 20대·120 ms 는 2026-10-10 area20-s8 기존 내용 확인), 40행 Lorenz 항목에 단일 피커·단일 구역, 빈 로봇 즉시 가용 가정, §4·§4.2 의 Pcart·Robot 2,600개 중 2,380개 이상 최적 풀이 범위 추가(f23~f26, 기존 결과는 유지), 43행 머니투데이 항목에 1차 출처(f27·f28). / 섹션 9 — 접수 응답·진행 통지·취소 결과·업무 확정 분리(f9·f14), 도착과 인수 확인 분리(f37), MCP 도구 범위와 업무 요구 분리(f36)를 책임 경계 근거로. / 섹션 10 — 12. 채팅으로 업무 지시·오케스트레이션(f33~f36, oq-141), 63. 병원·의료(f37·f38), 62. 제조 공장(f29), 26. 작업 순서·스케줄링(f17·f23~f26) 연결 보강. / 섹션 11(2026-09-25-area01-s11) — '새 질문' 세 개를 실제 id 로 표기(39행 oq-019, 40행 oq-020, 41행 oq-021). 부분 근거(해결 아님): oq-019 ← f15~f18, oq-020 ← f1~f6·f7, oq-021(·oq-351) ← f8·f9·f12, oq-012 ← f37(해외 사례, 국내 기준 미확인), oq-365 ← f21, oq-046 ← f11·f13, oq-141 ← f33·f36. oq-002 는 이번 근거 없음(미해결). 새 질문 3건. 다음 실행 후보: 12. 채팅으로 업무 지시·오케스트레이션(MCP 도구 범위 f33~f36), 26. 작업 순서·스케줄링(Lorenz 적용 조건 f23~f25)."
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "아르고(테크타카)–플로틱 남이천 물류센터 협력(오더 피킹 로봇 30대 지원 발표) 이후 실증의 시험 기간·성공 기준·완료 결과가 공개됐는가? | 관련 영역: 23. 업무 시스템 연동, 61. 물류창고 | 근거: f27 | 종류: 일반",
    "Yu·Srinivas(2025) 동적 주문 피킹 논문 원문의 실험 조건과 서지(권·호·쪽)로 기존 위키의 AOCT·ATT·AWTD 결과 서술을 재검증하면 그대로 맞는가? | 관련 영역: 23. 업무 시스템 연동, 26. 작업 순서·스케줄링 | 근거: ref-132 | 종류: 일반",
    "ISA-95 Part 1(ANSI/ISA-95.00.01-2025) 규격 본문에서 바뀐 조항은 무엇이며, OPC UA for ISA-95 Job Control 2.0·B2MML 과의 관계를 바꾸는가? | 관련 영역: 23. 업무 시스템 연동, 21. 상호운용 표준·적합성 | 근거: ref-002 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 16,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-02/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.",
      "GitHub 고정 커밋의 커밋일(rmf_api_msgs e9b7630 2026-09-19, rmf_task 3a6af29 2026-09-25, demos-ros-mcp-server edbc642 2026-07-09, isaac_mission_dispatch 56455eb 2026-09-15)은 확인 불가(403)라 published null",
      "ref-1461(SAP 참조구조)의 최초 발행일 미확인(갱신 2026-05-12 만 확인), ref-133 온라인 발행 일자 미확인(2025-05 까지만)",
      "f31: Bosch·Aimbo 개념검증의 실시일과 생산 운영 여부 미확인(뉴스 게시 2025-11-05, 수정 2026-06-18)",
      "f27·f28: 남이천 30대 실증의 시험 기간·결과 미확인, '20분 이상→10분 이내'의 측정 조건 미공개",
      "f29: LG CNS 사례의 다제조사 수·API·주문 상관키·생산계획 변경 승인 규칙 미공개, 성과 수치는 채택하지 않음",
      "f21: GreenAuto 개발 3대와 §6.2 최대 20대 동시 감시의 실물/가상 구성·기간 미확인(oq-365). F20b(주된 역할은 통합 감시, 수집 데이터에 task progress 포함)는 기존 area20 서술과 겹쳐 finding 으로 넣지 않음",
      "f9·f13: 취소 응답과 실제 정지의 시간 관계, 중복 요청 효과, SAP 현재 권장 연동 경로의 API 계약과 폐기 API 의 대체 관계는 확인 못 함(oq-046 관련)",
      "oq-020: ISA-95 JobOrderID·JobResponse 와 VDA 5050 orderId·Open-RMF booking.id 의 공개 매핑 명세는 찾지 못함",
      "oq-002: 국내 로봇 적재·하역 결과에 SSCC·EPCIS 를 연결한 운영 사례 없음. GS1 Korea SSCC 설명 페이지(메모 n16)는 물류 단위 식별 정의뿐이고 기존 ref-017 과 겹쳐 출처로 넣지 않음",
      "oq-012·oq-021: 국내 WMS 입고·인수 확정의 상관키·시간 초과 기준과 적재 후 취소의 반송·재고 반제 결정권자는 확인 못 함",
      "oq-141: MCP 경유 다사업자 WMS 주문·재고 처리의 운영 결과·권한·실패 복구 시험은 찾지 못함",
      "ISA-95 Part 1 2025 규격 본문은 유료라 미열람(ISA 발표 ref-002 는 원문 확인됐으나 내용이 기존 s7 과 같아 finding 없음)",
      "벤더 문서(SAP Warehouse Robotics·Oracle WMS Cloud·SAP Architecture Center)만 근거인 f10~f13·f15~f17·f30 은 원문 대조로 문서 내용은 확인했으나, 저장소 규칙(6.2 항목 13)에 따라 독립 출처 교차 확인 전까지 vendor_claim: true·[추정]으로 낮췄다(2026-10-11 재투입)."
    ],
    "scope_violations": [
      "f29: WCS·SCADA 통합 관제는 22. 설비·건물 시스템 연동·38. 모니터링과 겹치므로 이 영역에는 생산계획→실행 작업 조율 역할의 예로만 씀",
      "f30·f31: Embodied AI 휴머노이드 작업 수행은 44. 로봇 기반 모델·언어 모델 계획 쪽 내용이라 업무 객체 해석 계층의 근거로만 씀",
      "f33~f36: MCP 도구 노출은 12. 채팅으로 업무 지시·오케스트레이션과 겹치므로 업무 요청 접점 범위 판단으로 한정",
      "f23~f26: 재최적화 알고리즘의 최적성은 26. 작업 순서·스케줄링 쪽 내용이라 적용 조건만 씀",
      "f37·f38: 병원 인계 절차는 63. 병원·의료·30. 로봇 간 협업·물리적 인계와 겹치므로 도착과 인수 확인 분리 근거로만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 11
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(queries 0 은 집계 없음을 뜻함). 신규 출처 11건(ref-1453, ref-1454, ref-1455, ref-1456, ref-1457, ref-1458, ref-1459, ref-1460, ref-1461, ref-1462, ref-1463, 예약 구간 ref-1453~ref-1482 안, 한도 15 이내), 재사용 5건. 메모 출처 매핑(검증 결과 E절): n1→ref-131, n2→ref-1453(dispatch_task_response)·ref-1454(cancel_task_response)·ref-1455(simple_response) 신규(task_request ref-125·cancel_task_request ref-126·task_state ref-111·README ref-1028 은 해당 내용이 기존 위키에 있어 이번 finding 에 쓰지 않음), n3→ref-404(K03 중복이라 미사용), n4→ref-1456, n5→ref-1457, n6→ref-014(K06 중복이라 미사용), n7→ref-1459(기존 2차 보도 ref-137 과 같은 사건), n8→ref-1460, n9→ref-136, n10→ref-133, n11→ref-1461, n12→ref-1462, n13→ref-1463, n14→ref-1341, n15→ref-869, n16 미사용, n17→ref-002(중복이라 미사용), n18→ref-1458. 검증 수정 반영: 위키 중복(K03 전체, K06 전체, F04, F06, F08 task_id, F09 상태 열거, F29, F31)은 finding 으로 넣지 않고 rationale 에 '기존 내용 확인'으로만; GreenAuto 는 'MES·ERP용 REST API, AMR 실시간 이벤트·IIoT용 MQTT broker 는 계획(미가동)'으로(메모 요약의 'MES·ERP용 REST/MQTT' 바로잡음) 하고 s3 39행·s8 42행 정정 finding(f22) 추가; F23 은 §4·§4.2 와 Pcart·Robot 2,600개 중 2,380개 이상 최적 풀이 범위로; K09 는 '20분 이상→10분 이내'(메모의 '10분 미만' 정정); F24 는 디지털 warehouse AI agents 와 구별되는 Embodied AI agents 의 세 skill 중 하나로; SAP 제품명은 SAP Warehouse Robotics(SAP BTP 기반)로 쓰고 EWM 과 구별; n12 수정일 2026-06-18; ref-136 저자 17명·2025-06-27·Appl. Sci. 15(13) 7235 로 정정; ref-133 published 2025-05; 메모의 출처 집계(기존 5·새 13)는 틀려 기존 9·새 9(메모 단위)로 바로잡음. 교차 확인 0건: Open-RMF 스키마 세 파일은 같은 프로젝트, SAP 문서 셋은 같은 회사, Oracle·SAP 은 서로 다른 기능이라 같은 주장의 교차 확인이 아니다. 벤더 주장(f28·f29·f31)은 vendor_claim·추정·'벤더 주장: ' 표시, 아르고 협력 발표(f27)는 추정. 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-019 근거 f15~f18, oq-020 근거 f1~f7, oq-021·oq-351 근거 f8·f9·f12, oq-012 근거 f37, oq-365 근거 f21, oq-046 근거 f11·f13, oq-141 근거 f33·f36, oq-002 근거 없음. 메모 새 질문 U01~U11 가운데 기존 질문과 겹치는 U01(oq-020)·U02(oq-019)·U03(oq-021·oq-351)·U04(oq-002)·U05(oq-012)·U07(oq-365)·U09(oq-046)·U10(oq-141)은 새로 만들지 않고 U06·U08·U11 만 올렸다. 현장 유형 사례 finding: 물류창고(f27·f28·f31), 제조 공장(f29), 병원(f37·f38). 국내 자료는 아르고 발표(ref-1459)와 LG CNS 사례(ref-1460). 용어 후보 없음. 입력 누락 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-10-11-02/verification.json

```json
{
  "run_id": "2026-10-11-02",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: reference.opcfoundation.org OPC-10031-4 §6.2.1.9 에 'updates an existing job order that has not yet been started' 와 'All previously stored information is replaced' 가 있다. 판 v2.00.0 표시 확인. 페이지에 발행일 표기는 없어 2024-01-31 은 리서치가 본 공식 판 목록 값이다. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §6.2.1.12 에 시작하지 않은(AllowedToStart·NotAllowedToStart) 작업 지시를 취소하고 저장 정보를 지운다는 문장이 있고, 성공 뒤 JobOrderList 에 그 JobOrderID 가 없어야 한다(shall)는 문장도 있다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §6.2.1.11 Stop 은 시작된 작업 지시를 멈추고, 성공하면 Ended 상태여야 한다. §6.2.1.10 Abort 원문은 'aborts a job order' 뿐이고 대상 상태 범위가 적혀 있지 않다(트랙 반영 제안 3의 '미시작도 Abort' 부분은 확인 못 함)."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §6.2.4 표 45 의 Completed·Closed 정의가 브리프 발췌와 일치한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: OPC-10031-4 §1 Scope 에 2.0 이 1.0 과 호환되지 않고 새 namespace 를 정의한다는 문장이 있다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. f1~f4 에서 이끈 판단이며 '구축자 의견'으로 표시해야 한다. VDA 5050·Open-RMF 상태와의 매핑은 미확인(oq-020)."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 커밋 e9b7630 고정본 raw 를 열었다. oneOf[0] 은 required [success, state], state 는 task_state.json 참조, oneOf[1] 은 success=false·errors 이고 required 가 없다. 커밋일 미확인."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: cancel_task_response.json 은 simple_response.json 을 참조한다. simple_response 의 설명 문구(only indicates success and describes any errors)와 실패 분기 required [success, errors] 도 확인했다. ref-1454·ref-1455 는 같은 저장소이므로 교차 확인으로 보지 않는다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 스키마 구조에서 이끈 추론이다. 응답과 실제 정지의 시간 관계는 미확인이며, 본문에서 Open-RMF 문서가 그렇게 명시한다고 쓰지 않는다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정·벤더 주장 유지. help.sap.com PDF(LATEST URL)는 응답이 왔지만 압축 스트림이라 검증에서 본문을 해독하지 못했다. 검색에서는 SAP Warehouse Robotics 의 FMS 연동 API 문서가 실재함만 확인했고, 폐기(Deprecated) 표시는 독립 출처로 확인되지 않았다(SAP 블로그 검색 결과에는 폐기 공지가 없음). 판단은 브리프 발췌에 기댄다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정·벤더 주장 유지. 검증에서 PDF 본문을 해독하지 못해 브리프 발췌로만 판단했다. 폐기된 API 의 규칙이므로 현재 권장 경로의 계약으로 일반화하지 않는다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정·벤더 주장 유지. 검증에서 PDF 본문은 재대조하지 못했다(브리프 발췌 §1.6.2 기준)."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정·벤더 주장 유지. 검증에서 PDF 본문은 재대조하지 못했다. 중복 제거나 재시도 보장 같은 운영 보장은 문서에 없다는 단서를 유지한다(oq-046)."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. '구축자 의견'으로 표시해야 한다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Oracle WMS Cloud 26c Change Priority 도입 문단에 Ready·Held·Created 상태에서만 변경할 수 있다고 적혀 있다(원문 오타 'Created s status'). 벤더 주장으로 둔다. 발행일 2026-08-14(dcterms.created)는 검증에서 확인하지 못했다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 같은 문단에 외부 시스템도 다른 작업의 긴급도에 따라 우선순위를 바꿀 수 있고, Task/Change task priority 권한이 켜져 있을 때만 쓸 수 있다고 적혀 있다. 벤더 주장. 범위 경계상 WMS(연계 대상) 쪽 동작으로 서술한다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정·벤더 주장 유지. help.sap.com PDF(판 2308, LATEST URL)를 검증에서 해독하지 못했고, 검색에서도 LSD 정렬 규칙은 확인되지 않았다. 판단은 브리프 발췌에 기댄다. 연계 대상(WMS·SAP 통합 서비스)의 규칙으로 서술한다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. '구축자 의견'으로 표시해야 한다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "열람 실패: mdpi.com 은 403 이었고, mdpi-res PDF 는 압축 스트림이라 검증에서 본문을 해독하지 못했다(원문 미열람(검증 예산·형식)). Crossref 로 실재와 서지(Applied Sciences 15(13) 7235, 2025-06-27, 저자 17명)를 확인했다. 초록의 'future expansions' 문구는 주장과 어긋나지 않는다. 판단은 브리프의 p11 발췌에 기대며 high 불가."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f19 와 같다. 검증에서 본문 p11 은 재대조하지 못했다. 초록과 Crossref 서지의 일치까지만 확인했다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f19 와 같다(본문 §4 는 재대조 못 함). 검색에서 ISEC 문서가 ABB/ASTI TriBOT 5000 AGV 를 다룬다는 점은 보여 주제와 어긋나지 않는다. 개발 3대와 §6.2 의 최대 20대 감시의 관계는 미확인(oq-365)."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "정정 finding. 근거 f19·f20 은 검증에서 본문 재대조가 안 됐으나, 정정 방향(사용함 → 계획·미가동)은 보수적이고 초록의 'future expansions' 와 맞는다. 저자 17명은 Crossref 로 확인했다. 기존 s8 42행의 [사실] 문장(MQTT 발행)도 함께 고쳐야 한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: mediaTUM PDF 는 검증 환경에서 봇 차단(Anubis)이었다. 같은 논문의 arXiv 판(2409.12619, HTML)에서 'OOBSRP considers one picking zone of a single picker' 를 확인했다. 쪽수 p160 은 저널판 기준이라 대조하지 못했다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 판에서 빈 로봇이 배치 완료 직후 곧바로 가용하다는 가정과, 피커당 로봇 2대면 대개 대기가 없다는 선행 연구 근거를 확인했다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 판에서 인스턴스 2,600개(2 시스템 × 10 설정 × 13 주문 크기 × 10), 2,380개 이상 최적 풀이, 개입형 Pcart·Robot 한정을 확인했다. 저널판 쪽수는 대조하지 못했다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. '구축자 의견'으로 표시하고 기존 결과는 유지한다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 아르고 블로그(2025-01-21)에 남이천 물류센터 실증, 플로틱의 오더 피킹 로봇 30대 지원이 적혀 있다. ref-137(머니투데이)은 같은 발표를 옮긴 보도라 독립 출처가 아니다. 업체 발표이므로 추정 유지. 실증 결과는 미확인."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 플로틱 대표 인용문 '20분 이상 → 10분 이내 단축'은 앞선 실증사업에 대한 것이다. 벤더 주장이며 측정 조건은 공개되지 않았다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: LG CNS 고객 사례(2026-07-16)에 HD현대일렉트릭 청주 배전캠퍼스 신공장의 WCS·SCADA 통합 제어·관제가 있고, 공정 범위(입고·보관·라인 공급·완제품 이송·출하)가 일치한다. 벤더 주장. WCS·SCADA 는 연계 대상(22·38번)으로 다룬다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 2026-05-12 갱신 표시, Embodied AI agents 의 세 가지 skill 가운데 'Semantic Understanding of Business Objects' 가 있고, 디지털 warehouse AI agents 와 구별하는 서술이 있다. 벤더 주장. 최초 발행일은 미확인."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Anigon 1대, EWM 의 배송 정보·우선순위·보관 위치, beta·test 환경 검증, 탐색 단계, 게시 2025-11-05 를 확인했다. 수정일 2026-06-18 은 검증 열람에서 보이지 않아 미확인이다. 벤더 주장."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 커밋 56455eb 고정본 README 의 Latest Update 표에 2026-08 'VDA5050 3.0 support, add generic action node.'와 2026-03 'Mission Dispatch MCP …' 행이 있다."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정: 등록된 출처 ref-1341 은 README 이고 fetch_url 도 README 뿐이다. README 에는 MCP 도구 목록이 없고 MCP 코드 경로도 적혀 있지 않다. server.py 의 경로가 기록되지 않았고, 검증에서 추정한 경로(packages/mission-dispatch-mcp, mission-dispatch-mcp)는 404, GitHub 트리 조회는 403 이었다. 검색에서도 도구 이름이 확인되지 않았다."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정: f33 과 같은 이유다. server.py·queries.py 의 경로가 브리프에 기록되지 않았고 검증에서 열지 못했다. 등록 출처(README)는 핸들러 동작을 뒷받침하지 않는다."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: edbc642 고정본 README 에 Ubuntu 22.04, ROS 2 Humble, Ignition Gazebo Fortress, 창고 시뮬레이션의 Tugbot 1대, 이동·정지·토픽·/scan·오도메트리 예시 프롬프트가 있다. 업무 시스템 연동은 없다. 커밋일 미확인."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. '구축자 의견'으로 표시한다. 근거 f33(도구 범위·취소 도구 없음)이 추정으로 강등됐으므로 '공개 코드가 취소를 제공하지 않는다'를 확정 사실처럼 쓰지 않는다."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Frontiers 원문 표 1 step 8~13 의 순서를 확인했다. 사용자가 버튼으로 빈 상태를 확인하면(9) 인제스터가 RMF 에 완료를 알리고(10) ICU 복귀를 요청하며(11) ICU 에 도착한다(13)."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §4 에 TIAGo·Jackal 을 시험 환경에서 검증한 것과 'we are yet to apply multiple delivery robots inside the Hospital' 이 있다."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": false,
    "issues": [
      "f15·f16·f17·f18: 우선순위 변경 허용 상태·권한·대기 큐 정렬 규칙은 상위 업무 시스템(WMS·SAP 통합 서비스) 쪽 동작이다. '연계 대상'의 사례로 서술하고, ROP 는 그 결과를 받아 진행 중 작업에 반영하는 쪽으로 쓴다.",
      "f29: WCS·SCADA 통합 제어·관제는 설비 제어·관제(22. 설비·건물 시스템 연동, 38. 모니터링·이상 탐지·원인 분석) 쪽 연계 대상이다. 23번에서는 생산계획을 실행 작업으로 조율하는 제조 공장 사례로만 짧게 쓴다.",
      "f30·f31: 휴머노이드의 물리 작업 수행(파지 등)은 로봇 자체 지능·제어의 연계 대상이다. 업무 객체 해석 계층의 근거로만 쓰고 44. 로봇 기반 모델·언어 모델 계획에 연결한다."
    ]
  },
  "duplication": {
    "ok": false,
    "overlaps": [
      "f27·f28 은 기존 5절 국내 문단·s8 43행의 ref-137(머니투데이 보도)과 같은 사건이다. 새 문장을 따로 만들지 않고 기존 문단에 1차 출처 ref-1459 를 병기한다.",
      "f19~f22 는 기존 s3 39행·s8 42행의 ref-136 문장과 충돌한다(사용함 vs 계획·미가동). 정정 대상이며, 각주 ref-136 서지(저자 미확인)도 고친다.",
      "f1~f5 는 s4 40행·s7 의 ref-131(원문 미열람) 항목과 겹친다. 새 각주 없이 ref-131 을 재사용하고 미열람 표시를 해제한다.",
      "트랙 반영 제안 3(2026-09-25-77, ref-681)은 같은 명세(OPC 10031-4 작업 제어)를 가리킨다. 같은 주장에는 이번에 원문을 확인한 ref-131 을 쓴다.",
      "f21 의 개발 3대는 20. 로봇·제조사 관제 연동 페이지의 최대 20대 동시 감시 서술(2026-10-10)과 관계가 미확인이다(oq-365). 둘을 합치지 않는다."
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "FMS: 브리프는 '제조사 관제(FMS)'로 쓴다. 용어집 표기는 '플릿 관리 시스템 (Fleet Management System (FMS))'이다.",
      "ingestor(f37): 용어집 표기는 '디스펜서·인제스터 (Dispenser / Ingestor)'이므로 '인제스터'로 쓴다.",
      "MCP: 용어집 표기는 '모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))'이다."
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f33·f34: 태그를 [사실]에서 [추정]으로 강등하고, 공개 코드의 파일 경로가 출처에 기록되지 않아 검증에서 다시 확인하지 못했다는 단서를 같은 문장에 붙인다. 이유: 등록 출처 ref-1341 은 README 이고, README 에는 MCP 도구 목록·핸들러 내용이 없다. '도구 11개'·'취소 도구 없음'은 이 추정 문장 안에서만 쓴다.",
    "f6·f14·f18·f26·f36: 모든 [의견] 문장에 누구의 의견인지 밝힌다('구축자 의견:'으로 시작). 이유: 사실 표기 규칙상 의견의 주체를 밝혀야 한다.",
    "f10~f13·f15~f17·f28~f31: [추정]에 '벤더 주장'을 함께 적는다. f27 은 '업체 발표'임을 밝힌다. 이유: 근거가 모두 제조사·공급자 문서이고 독립 확인이 없다.",
    "f10~f13: 폐기(Deprecated)로 표시된 SAP Warehouse Robotics(SAP BTP 기반 제품, SAP EWM 과 구별) FMS 연동 API 의 규칙이라고 밝힌다. 현재 권장 연동 경로의 계약으로 일반화하지 않는다. 각주에는 'LATEST URL, 확보본 2024-07-10 기준'을 적는다(ref-1458 은 '판 2308 기준'). 이유: URL 이 최신판을 가리켜 내용이 바뀔 수 있다.",
    "f15~f18: 6·9절에서 우선순위 변경 허용 상태·권한·LSD 정렬은 연계 대상인 상위 업무 시스템(WMS) 쪽 규칙으로 서술한다. ROP 직접 범위처럼 쓰지 않는다. 이유: 분류 원문 19장 '상위 업무 시스템' 경계.",
    "f29: 5절 제조 공장 사례로만 짧게 쓰고, WCS·SCADA 통합 관제는 연계 대상으로 표시해 22. 설비·건물 시스템 연동, 38. 모니터링·이상 탐지·원인 분석과 연결한다. 이유: 설비 제어·관제는 외부 연계 영역이다.",
    "f30·f31: 업무 객체 해석 계층의 근거로만 쓰고, 로봇의 물리 작업 수행은 연계 대상으로 44. 로봇 기반 모델·언어 모델 계획과 연결한다. f31 은 '탐색 단계, beta·test 환경 검증, 단일 Anigon' 단서를 유지한다. 이유: 로봇 자체 지능·제어는 외부 연계 영역이고, 개념검증을 운영 사례로 오인하지 않게 한다.",
    "ref-1462 각주와 본문에는 게시일 2025-11-05 만 적고 수정일 2026-06-18 은 뺀다. 이유: 검증 열람에서 수정일 표시를 확인하지 못했다.",
    "f19~f22: s3 39행 '확인한 연동 사례는 자체 REST·MQTT 인터페이스를 썼다'와 s8 42행의 MQTT 발행 [사실] 문장을 'MES·ERP용 REST API 와 AMR 실시간 이벤트·IIoT용 MQTT broker, VDA 5050 연동은 계획(당시 미가동)'으로 고친다. ref-136 각주는 'Lopes, D., Pereira, T., Gonçalves, A. 외(저자 17명), Applied Sciences 15(13) 7235, 2025-06-27, 접근일 2026-10-11'로 바꾼다. 이유: 원문(브리프 발췌)·Crossref 서지와 기존 문장이 다르다.",
    "f21: '개발 대상 AMR 2대·AGV 1대(서로 다른 제조사)'라고만 쓰고, 20. 로봇·제조사 관제 연동 페이지의 최대 20대 동시 감시와의 관계는 미확인(oq-365)으로 둔다. 이유: 두 수치를 합치면 근거가 없다.",
    "ref-131 각주: 발행일을 2024-01-31 로, 접근일을 2026-10-11 로 바꾸고 '(원문 미열람)'을 뗀다. s4·s7 의 '상태 전이는 원문 미열람' 표기도 해제한다. 이유: 이번 실행에서 원문(§1, §6.2.1, §6.2.4)을 열어 확인했다.",
    "트랙 반영 제안 3(2026-09-25-77): Update 가 시작 전 작업 지시에만 적용된다는 부분만 f1 근거로 ref-131 각주를 달아 반영한다. 'Abort 가 실행 중·중단·미시작 작업 지시를 Aborted 로 보낸다'와 Pause·Resume 은 넣지 않는다. 이유: 검증에서 연 Abort 원문에는 대상 상태 범위가 적혀 있지 않다.",
    "트랙 반영 제안 1(작업 지시의 선택 필드, 2026-09-25-37)과 제안 2(Mecalux Easy WMS 대화형 비서, 2026-09-25-37)는 이번 페이지에 반영하지 않는다. additional_research_requests 에 23. 업무 시스템 연동의 다음 실행 후보로 넘긴다. 이유: 브리프에 이를 뒷받침하는 finding 이 없다.",
    "5절 국내 문단: 기존 ref-137 문장에 1차 출처 ref-1459 를 병기한다. '30대 지원 발표'와 '20분 이상 → 10분 이내는 앞선 실증의 업체 주장(벤더 주장)'을 구분하고 남이천 실증 결과 미확인을 유지한다. 이유: f27·f28 의 범위.",
    "5절 적용 사례: 새 사례마다 현장 유형을 하나씩 밝힌다(제조 공장: f29, 병원: f37·f38, 물류창고: f31·f27). f38 의 '병원 안 운반은 TIAGo 1대, 이기종 관리는 별도 시험 환경'을 사례 안에 적는다. site_matrix_updates 는 실제로 채운 칸과 맞춘다. 이유: 원문 21장 형식과 과장 방지.",
    "ref-133(Lorenz 외): 본문에는 쪽수(p160·p168) 대신 절 번호(§2, §4)만 쓴다. 각주 발행일은 2025-05 로 적고 '(원문 미열람)'을 뗀다. 이유: 검증은 저널판이 아니라 같은 논문의 arXiv 판으로 내용을 확인해 쪽수를 대조하지 못했다.",
    "용어: FMS 는 '플릿 관리 시스템(Fleet Management System, FMS)', f37 의 ingestor 는 '인제스터', MCP 는 첫 등장에서 '모델 컨텍스트 프로토콜(Model Context Protocol, MCP)'로 용어집 표기를 따른다. 이유: 용어집과 충돌한다.",
    "출처 원문 직접 인용은 출처마다 1회 이하로 하고, 특히 ref-131 의 여러 조항은 요약·재서술한다. 이유: 인용 길이 규칙.",
    "11절: oq-019·oq-020·oq-021·oq-012·oq-365·oq-046·oq-141 에는 부분 근거만 적고 모두 열림을 유지한다. oq-002 는 이번 근거 없음으로 둔다. 이유: 해결 제안이 없고 답이 되는 finding 이 부분적이다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 36건, 미확인 2건, 교차 확인 0건. 강등: f33 사실 → 추정, f34 사실 → 추정(등록 출처 ref-1341 은 README 이고 MCP 코드 파일 경로가 기록되지 않아 검증에서 재확인하지 못함). 원문 미열람 출처: 없음. 다만 검증 쪽에서 본문을 다시 대조하지 못한 출처가 있다. ref-136 은 MDPI 403·PDF 압축 해독 실패로 Crossref 서지와 초록까지만 확인했다. ref-1456·ref-1458 은 SAP PDF 압축으로 실재만 확인했다. ref-133 은 mediaTUM 이 봇 차단이라 같은 논문의 arXiv 판으로 확인했다. ref-131·ref-1453~ref-1455·ref-1457·ref-1459~ref-1463·ref-869·ref-1341(README) 는 원문으로 확인했다. 주의: 핵심 사실(OPC UA for ISA-95 Job Control 2.00.0 의 Update·Cancel·Stop·Completed/Closed, Open-RMF 응답 스키마)은 모두 단일 출처다. SAP Warehouse Robotics·Oracle WMS·LG CNS·SAP 참조구조·Bosch–Aimbo 사례는 벤더 주장이며, SAP FMS API 는 폐기 표시 문서다. GreenAuto(Lopes 외)의 REST·MQTT·VDA 5050 연동은 계획(미가동)으로 정정한다. Tartu 병원 실증은 병원 안에서 로봇 1대로 했다. 트랙 반영 제안 3건 가운데 제안 3은 Update 시작 전 조건만 반영하고, 제안 1·2는 근거 finding 이 없어 다음 실행으로 넘긴다. 새 열린 질문 2·3의 근거(ref-132·ref-002)는 브리프 sources 밖이지만 기존 페이지 각주를 재사용한 것으로 인정했다. 열린 질문 해결 인정 없음. 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-10-11-02/pages.json

```json
{
  "run_id": "2026-10-11-02",
  "outline": [
    {
      "path": "docs/categories/integration/business-system-integration.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 800,
      "summary": "VDA 5050 3.0.0 은 외부 IT 인터페이스를 범위 밖에 둔다 [사실][^ref-031]. 2026-09-25 주제 페이지 링크를 되살리고, 다제조사 플릿 사례(Lopes 외)의 MES·ERP용 REST·MQTT 연동은 계획(당시 미가동)이었다는 정정을 덧붙인다 [사실][^ref-136].",
      "planned_findings": [
        "f19",
        "f20",
        "f22"
      ]
    },
    {
      "path": "docs/categories/integration/business-system-integration.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1200,
      "summary": "OPC UA for ISA-95 Job Control 2.00.0 은 갱신(시작 전·전부 교체), 취소(시작 전·기록 제거), 정지(Ended), Completed·Closed 를 서로 다른 조건으로 둔다 [사실][^ref-131].",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5"
      ]
    },
    {
      "path": "docs/categories/integration/business-system-integration.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 3600,
      "summary": "기존 물류창고 시나리오를 유지하고 국내 발표에 1차 출처를 병기했다 [추정] 업체 발표[^ref-1459]. 병원(Tartu 인수 확인 뒤 복귀) [사실][^ref-869], 제조 공장(LG CNS WCS·SCADA) [추정] 벤더 주장[^ref-1460], 물류창고(Bosch·Aimbo 개념검증) [추정] 벤더 주장[^ref-1462] 사례를 더한다.",
      "planned_findings": [
        "f27",
        "f28",
        "f29",
        "f31",
        "f37",
        "f38"
      ]
    },
    {
      "path": "docs/categories/integration/business-system-integration.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 3400,
      "summary": "Open-RMF 취소 응답은 성패만 알려 실제 취소는 작업 상태로 확인해야 할 것으로 보인다 [추정][^ref-1454][^ref-1455]. 우선순위 변경 허용 범위는 WMS 쪽 규칙이며 [추정] 벤더 주장[^ref-1457], MCP 접점의 도구 범위는 업무 요구와 따로 봐야 한다 [의견][^ref-1341].",
      "planned_findings": [
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17",
        "f18",
        "f30",
        "f32",
        "f33",
        "f34",
        "f35",
        "f36"
      ]
    },
    {
      "path": "docs/categories/integration/business-system-integration.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1600,
      "summary": "OPC Job Control 2.0 의 1.0 비호환 [사실][^ref-131], Open-RMF 응답 스키마 [사실][^ref-1453], SAP·Oracle 벤더 API, Mission Dispatch MCP 기록 [사실][^ref-1341]을 표로 더한다.",
      "planned_findings": [
        "f5",
        "f7",
        "f8",
        "f10",
        "f15",
        "f30",
        "f32",
        "f35"
      ]
    },
    {
      "path": "docs/categories/integration/business-system-integration.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1600,
      "summary": "GreenAuto 서지·미가동 정정 [사실][^ref-136], Lorenz 외 적용 조건(단일 피커·빈 로봇 즉시 가용) [사실][^ref-133], 아르고 1차 발표와 Tartu 병원 실증을 더한다.",
      "planned_findings": [
        "f19",
        "f20",
        "f21",
        "f22",
        "f23",
        "f24",
        "f25",
        "f26",
        "f27",
        "f37"
      ]
    },
    {
      "path": "docs/categories/integration/business-system-integration.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1800,
      "summary": "요청 변경·결과 보고, 휴머노이드 물리 작업, 설비 제어, 업종별 인수 확인 행을 더해 WMS 규칙·WCS·SCADA·로봇 물리 작업을 연계 대상으로 나눈다 [추정][^ref-1454].",
      "planned_findings": [
        "f9",
        "f14",
        "f15",
        "f16",
        "f17",
        "f29",
        "f31",
        "f37"
      ]
    },
    {
      "path": "docs/categories/integration/business-system-integration.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1500,
      "summary": "12. 채팅으로 업무 지시·오케스트레이션, 22·30·38·44번과 61·62·63번 현장 유형 영역을 연결한다.",
      "planned_findings": [
        "f29",
        "f30",
        "f31",
        "f33",
        "f37"
      ]
    },
    {
      "path": "docs/categories/integration/business-system-integration.md",
      "section": "11. 열린 질문",
      "budget_chars": 1900,
      "summary": "oq-019·oq-020·oq-021·oq-012·oq-046·oq-141·oq-365 에 부분 근거만 적고 모두 열림 유지, oq-002 는 근거 없음, 새 질문 3건을 올린다.",
      "planned_findings": [
        "f1",
        "f7",
        "f8",
        "f9",
        "f12",
        "f13",
        "f15",
        "f17",
        "f21",
        "f33",
        "f37"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/integration/business-system-integration.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "차등 갱신: 3·8절 GreenAuto(Lopes 외) REST·MQTT·VDA 5050 연동을 계획(미가동)으로 정정·ref-136 서지 정정; 4절 OPC Job Control 2.00.0 갱신·취소·정지·Completed/Closed 조건(원문 확인, 트랙 반영 제안 3 일부); 5절 국내 문단 1차 출처 병기와 병원·제조 공장·물류창고 사례 추가; 6절 응답·취소 결과 분리, SAP 폐기 FMS API, WMS 우선순위 규칙(연계 대상), 업무 객체 해석, MCP 접점 범위; 7절 표 추가; 9절 경계 행 추가·MCP 첫 등장 풀어쓰기; 10절 연결 8건 추가; 11절 부분 근거·새 질문 3건; 3·4·6·7·8·11절에 2026-09-25 주제 페이지 링크 복원(2차 수정); 13절 각주 갱신",
      "patches": [
        {
          "section": "3. 왜 중요한가",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-02/pages/categories/integration/business-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "4. 핵심 개념과 용어",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-02/pages/categories/integration/business-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-02/pages/categories/integration/business-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-02/pages/categories/integration/business-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-02/pages/categories/integration/business-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-02/pages/categories/integration/business-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-02/pages/categories/integration/business-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-02/pages/categories/integration/business-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-02/pages/categories/integration/business-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "frontmatter": {
            "related_areas": [
              12,
              20,
              21,
              22,
              24,
              25,
              26,
              29,
              30,
              32,
              38,
              44,
              61,
              62,
              63
            ],
            "sources": [
              "ref-002",
              "ref-031",
              "ref-111",
              "ref-125",
              "ref-126",
              "ref-127",
              "ref-128",
              "ref-129",
              "ref-130",
              "ref-131",
              "ref-132",
              "ref-133",
              "ref-134",
              "ref-135",
              "ref-136",
              "ref-137",
              "ref-869",
              "ref-1341",
              "ref-1453",
              "ref-1454",
              "ref-1455",
              "ref-1456",
              "ref-1457",
              "ref-1458",
              "ref-1459",
              "ref-1460",
              "ref-1461",
              "ref-1462",
              "ref-1463"
            ],
            "confidence": "medium",
            "last_run": "2026-10-11"
          },
          "content": "(절 본문 생략 — runs/2026-10-11-02/pages/categories/integration/business-system-integration.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-11-area23-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 23. 업무 시스템 연동 의 \"6. 대표 접근법과 기술\" 절(3,712자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area23-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 23. 업무 시스템 연동 의 \"11. 열린 질문\" 절(2,250자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area23-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 23. 업무 시스템 연동 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,793자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area23-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 23. 업무 시스템 연동 의 \"8. 대표 연구와 자료\" 절(1,623자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area23-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 23. 업무 시스템 연동 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,310자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area23-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 23. 업무 시스템 연동 의 \"4. 핵심 개념과 용어\" 절(1,034자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area23-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 23. 업무 시스템 연동 의 \"3. 왜 중요한가\" 절(675자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-11 | 23. 업무 시스템 연동 | 차등 갱신: 3·8절 GreenAuto REST·MQTT·VDA 5050 연동을 계획(미가동)으로 정정·ref-136 서지 정정, 4·6·7절 OPC Job Control 상태 조건·응답과 취소 결과 분리·WMS 우선순위 규칙(연계 대상, 벤더 주장)·MCP 접점 범위, 5절 병원·제조 공장·물류창고 사례, 9·10·11절 보강, 2026-09-25 주제 페이지 링크 복원 | run 2026-10-11-02",
  "index_updates": {
    "home_recent": "2026-10-11 — 23. 업무 시스템 연동: OPC UA for ISA-95 Job Control 상태 조건·Open-RMF 응답 스키마·WMS 우선순위 규칙(벤더 주장)·MCP 접점 범위를 더하고, 병원·제조 공장·물류창고 사례와 GreenAuto 연동 '계획(미가동)' 정정을 반영",
    "category_recent": "2026-10-11 — 23. 업무 시스템 연동: 접수 응답·진행 통지·취소 결과 분리 근거, 우선순위 변경 허용 범위(WMS 쪽, 연계 대상), 병원 인수 확인·제조 공장 WCS·SCADA·물류창고 개념검증 사례 추가, GreenAuto 정정",
    "area_recent": "2026-10-11 — 23. 업무 시스템 연동: 3·8절 GreenAuto 정정, 4절 Job Control 갱신·취소·정지·완료 조건, 5절 병원·제조 공장·물류창고 사례, 6·7절 응답 분리·우선순위 규칙·MCP 범위, 9~11절 보강, 2026-09-25 주제 페이지 링크 유지"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-131",
      "org": "OPC Foundation / ISA",
      "title": "OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4)",
      "published": "2024-01-31",
      "url": "https://reference.opcfoundation.org/specs/OPC-10031-4/6.2",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "OPC 10031-4 Job Control 2.00.0 명세. 2026-10-11 실행에서 전체 판(§1 Scope, §6.2.1.9~12 Update·Abort·Stop·Cancel, §6.2.4 표 45)을 원문 대조했고, 공식 판 목록의 현행 2.00.0·2024-01-31 표시를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-133",
      "org": "Lorenz, Otto, & Gendreau (Networks, Wiley)",
      "title": "Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization?",
      "published": "2025-05",
      "url": "https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Networks 86(2):157–173, 저자 3명(Catherine Lorenz, Alena Otto, Michel Gendreau), 온라인 발행 2025-05(일자 미확인). 단일 피커·단일 피킹 구역 모델, 빈 로봇 즉시 가용 가정, 개입형 Pcart·Robot 인스턴스 2,600개 계산실험을 원문(§2·§4)으로 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-136",
      "org": "Lopes, D., Pereira, T., Gonçalves, A. 외 (저자 17명; Applied Sciences, MDPI)",
      "title": "Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector",
      "published": "2025-06-27",
      "url": "https://www.mdpi.com/2076-3417/15/13/7235",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Applied Sciences 15(13) 7235, DOI 10.3390/app15137235, 저자 17명(David Lopes 외). 자동차 부문 GreenAuto 다제조사 플릿 감시 시스템으로, IIoT·MES·ERP 연동(REST API·MQTT broker)과 VDA 5050 연동은 미래 확장(당시 미가동)이다. 기존 저자 '미확인' 정정.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-869",
      "org": "Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Tartu 대학병원에서 Open-RMF 로 TIAGo 가 ICU 혈액 시료를 검사실로 운반한 현장 시험. 표 1 의 인수 확인 후 ICU 복귀 절차와 §4 의 TIAGo·Jackal 별도 시험 환경 검증을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-1341",
      "org": "NVIDIA (nvidia-isaac GitHub)",
      "title": "isaac_mission_dispatch — README",
      "published": null,
      "url": "https://github.com/nvidia-isaac/isaac_mission_dispatch",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "VDA 5050 기반 미션 배포 서비스 README. 커밋 56455eb 고정본의 Latest Update 표(2026-03 Mission Dispatch MCP, 2026-08 VDA5050 3.0 지원)를 확인했다. MCP 코드 내용은 경로 미기록으로 검증 재확인이 안 됐다(커밋일 미확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-1453",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_response.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/dispatch_task_response.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Open-RMF 작업 배정 요청 응답 스키마(커밋 e9b7630 고정본). 성공 분기는 success·state(task_state) 필수, 실패 분기는 errors 배열을 둔다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-1454",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_response.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/cancel_task_response.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Open-RMF 작업 취소 요청 응답 스키마(커밋 e9b7630 고정본). 자체 필드 없이 simple_response.json 을 참조한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-1455",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/simple_response.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/simple_response.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "성공 여부와 오류만 알리는 Open-RMF 응답 틀 스키마(커밋 e9b7630 고정본). 성공이면 success=true, 실패면 success=false 와 errors 가 필수다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-1456",
      "org": "SAP",
      "title": "APIs for Integration via Fleet Management Systems (API for Integration with Fleet Management Systems (Deprecated))",
      "published": "2024-07-10",
      "url": "https://help.sap.com/doc/a02ad3695d5845fca1678810cb83562b/LATEST/en-US/379d6d880e5d4007b3751618080da80f_1.pdf",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "SAP Warehouse Robotics(SAP BTP 기반, SAP EWM 과 구별)와 플릿 관리 시스템(FMS)을 잇는 폐기(Deprecated) 표시 API 문서. 요청→응답→콜백 순서, messageId, 취소 성공(CANCELLED)·취소 불가 통지 메서드를 정의한다. LATEST URL 이라 확보본(2024-07-10) 기준.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-1457",
      "org": "Oracle",
      "title": "WMS REST API Guide — Change Priority (Oracle Warehouse Management Cloud 26c)",
      "published": "2026-08-14",
      "url": "https://docs.oracle.com/en/cloud/saas/warehouse-management/26c/owmre/change-priority.html",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "Oracle WMS Cloud 26c 의 작업 우선순위 변경 API 문서(문서 ID G55063-04, Release 26C; 날짜는 페이지 메타데이터 dcterms.created). Ready·Held·Created 상태 작업만 변경할 수 있고 Task/Change task priority 권한이 필요하다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-1458",
      "org": "SAP",
      "title": "End-User Information for Integration via Integration Services (SAP Warehouse Robotics, Document Version 2308)",
      "published": "2023-08-19",
      "url": "https://help.sap.com/doc/f08ea8f8686c46e89f1d7ed121f19d68/LATEST/en-US/b82aa9c86bd74777b86ec7f5766252d0.pdf",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "SAP Warehouse Robotics(SAP BTP 기반, SAP EWM 사용자의 로봇 통합 제품)의 integration services 경로 사용자 문서. 최적화 미사용 시 큐 순서와 LSD·생성 시각 정렬 규칙을 설명한다. LATEST URL 이라 확보본(판 2308) 기준.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-1459",
      "org": "아르고 풀필먼트(테크타카)",
      "title": "아르고, 플로틱과 로봇 기반 물류 생산성 향상 실증 본격 실시",
      "published": "2025-01-21",
      "url": "https://blog.argoport.com/pr-robotcooperation250121",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "테크타카(아르고)의 공식 업체 발표. 자사 WMS 와 플로틱 로봇 연동 자동화 모델을 남이천 물류센터에서 실증하고 플로틱이 오더 피킹 로봇 30대를 지원한다고 밝힌다. 기존 ref-137 보도의 1차 출처이며 실증 결과는 미확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-1460",
      "org": "LG CNS",
      "title": "로봇 기반 물류 자동화와 통합 관제로 HD현대일렉트릭 신공장의 새로운 운영 체계를 구축하다",
      "published": "2026-07-16",
      "url": "https://www.lgcns.com/kr/moa/customer-story/detail.smartlogistics-robotic-logistics-2607-1",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "LG CNS 고객 사례. HD현대일렉트릭 청주 배전캠퍼스 신공장에 AMR·ACR 기반 물류 자동화와 WCS·SCADA 통합 제어·관제를 구축했다고 설명한다(공급자 단독 설명).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-1461",
      "org": "SAP Architecture Center",
      "title": "Warehouse Pick & Place with Embodied AI Robotics",
      "published": null,
      "url": "https://architecture.learning.sap.com/docs/ref-arch/7e4168",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "SAP 참조구조(2026-05-12 갱신, 최초 발행일 미확인). 디지털 창고 AI 에이전트와 구별되는 체화(Embodied) AI 에이전트의 세 가지 주요 skill(업무 객체의 의미 이해 포함)을 설명한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-1462",
      "org": "SAP (Lukasz Ostrowski, SAP News Center)",
      "title": "How SAP Brings Business AI into the Physical World: New Robotics Pilots Across Warehouse, Manufacturing, and Inspection Use Cases",
      "published": "2025-11-05",
      "url": "https://news.sap.com/2025/11/sap-physical-ai-partnerships-new-robotics-pilots/",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "SAP 로봇 파일럿 소개 뉴스(게시 2025-11-05). Bosch·Aimbo 단일 Anigon 개념검증(탐색 단계, beta·test 환경 검증) 등 파트너 사례를 공급자 관점에서 소개한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    },
    {
      "id": "ref-1463",
      "org": "robotmcp",
      "title": "demos-ros-mcp-server — Example 1: Tugbot Warehouse Simulation (Ignition Gazebo) README",
      "published": null,
      "url": "https://github.com/robotmcp/demos-ros-mcp-server/blob/edbc642849bdde1187771a15e557ec9e219184a5/1_Gazebo_Tugbot/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "ROS-MCP 서버로 Gazebo 창고 시뮬레이션의 Tugbot 1대를 자연어로 이동·센서 조회하는 데모 README(커밋 edbc642 고정본, 커밋일 미확인). 업무 시스템 연동은 없다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/business-system-integration.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "아르고(테크타카)–플로틱 남이천 물류센터 협력(오더 피킹 로봇 30대 지원 발표) 이후 실증의 시험 기간·성공 기준·완료 결과가 공개됐는가?",
      "areas": [
        23,
        61
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "Yu·Srinivas(2025) 동적 주문 피킹 논문 원문의 실험 조건과 서지(권·호·쪽)로 기존 위키의 AOCT·ATT·AWTD 결과 서술을 재검증하면 그대로 맞는가?",
      "areas": [
        23,
        26
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "ISA-95 Part 1(ANSI/ISA-95.00.01-2025) 규격 본문에서 바뀐 조항은 무엇이며, OPC UA for ISA-95 Job Control 2.0·B2MML 과의 관계를 바꾸는가?",
      "areas": [
        23,
        21
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "23. 업무 시스템 연동"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "23. 업무 시스템 연동"
    },
    {
      "site_type": "병원",
      "item": "완료·인계",
      "link": "docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "23. 업무 시스템 연동"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "23. 업무 시스템 연동"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "23. 업무 시스템 연동"
    },
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "23. 업무 시스템 연동"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "23. 업무 시스템 연동"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "23. 업무 시스템 연동"
    }
  ],
  "standards_updates": [
    {
      "name": "Open-RMF 작업 배정·취소 응답 스키마(rmf_api_msgs dispatch_task_response·cancel_task_response·simple_response)",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/dispatch_task_response.json",
      "related_areas": [
        23,
        29
      ],
      "summary": "배정 응답은 성공 시 success·state(task_state) 필수, 실패 시 errors 배열을 두고, 취소 응답은 simple_response 를 참조해 성패와 오류만 알린다(커밋 e9b7630 고정본, 2026-10-11 확인).",
      "ref_id": "ref-1453"
    }
  ],
  "additional_research_requests": [
    "3·4·7·8절 주제 페이지 정정(f19~f22, ref-131·ref-136): docs/topics/2026/2026-09-25-area01-s3.md 39행 '확인한 연동 사례는 자체 REST·MQTT 인터페이스를 썼다'와 docs/topics/2026/2026-09-25-area01-s8.md 42행 GreenAuto(MQTT 발행) [사실] 문장, 두 페이지의 ref-136 각주(저자 미확인), 2026-09-25-area01-s4·s7 의 ref-131 '원문 미열람'·'상태 전이는 원문 미열람' 표시를 직접 고치려면 해당 주제 페이지 본문이 입력으로 필요하다. 이번 실행에는 입력이 없어 세부영역 페이지 3·4·7·8절에 정정 문단과 2026-09-25 주제 페이지 링크(정정 대상 안내 포함)를 두었다. 다음 갱신 실행에서 네 주제 페이지를 입력에 넣어 차등 갱신하도록 요청한다.",
    "7절(트랙 반영 제안 1, 실행 2026-09-25-37): OPC UA for ISA-95 작업 제어 노드셋의 작업 지시에서 작업 지시 id 만 필수이고 종료 시각·우선순위·자재 요구가 선택 필드라는 점을 뒷받침하는 finding 이 이번 브리프에 없어 반영하지 않았다. 23. 업무 시스템 연동의 다음 실행 후보로 원문 확인을 요청한다.",
    "6절(트랙 반영 제안 2, 실행 2026-09-25-37): Mecalux Easy WMS 대화형 비서(긴급 주문 출고·통로 잠금 해제를 실행 전 요약·확인 후 수행, 벤더 주장)를 연계 대상 사례로 쓰려면 이번 브리프에 finding 이 필요하다. 다음 실행 후보로 넘긴다.",
    "6절(f33·f34 재검증): NVIDIA Isaac Mission Dispatch MCP 서버의 server.py·queries.py 고정 커밋 경로를 출처로 기록해 도구 11개·취소 도구 부재·이동 미션 POST 경로를 다시 확인하면 [사실]로 쓸 수 있다.",
    "6·11절: SAP Warehouse Robotics 의 현재 권장 연동 경로의 API 계약(요청 응답·콜백·취소 결과 통지)과 폐기된 FMS API 의 대체 관계가 필요하다(oq-021·oq-046).",
    "5절 병원 사례: Tartu 대학병원 실증(ref-869) 표 1 의 앞 단계(운반 요청 생성)와 시간·구역 제약, 실패 시 복구 방식을 브리프로 확인하면 시작 조건·제약·예외·성과 칸을 채울 수 있다.",
    "5절 물류창고 사례: Bosch·Aimbo 개념검증의 실시일, 완료 확인 방식, 생산 운영 전환 여부를 확인할 독립 출처가 필요하다."
  ],
  "fixes_applied": [
    "f33·f34 강등 — 6절 'MCP 같은 새 접점의 실제 범위' 소제목의 두 문장을 [추정][^ref-1341]로 쓰고 각 문장 안에 '공개 코드의 파일 경로가 출처에 기록되지 않아 검증에서 다시 확인하지 못했다'는 단서를 붙였으며, '도구 11개'·'미션 취소 도구 없음'은 그 추정 문장 안에서만 썼다(7절 Mission Dispatch 행은 f32 만, 11절 oq-141 은 '추정 수준'으로 서술).",
    "[의견] 주체 표시 — f6·f14·f18·f26·f36 을 쓴 모든 [의견] 문장(6절 4건, 8절 Lorenz 항목, 9절 f14 반복)을 '구축자 의견:'으로 시작했다.",
    "벤더 주장 병기 — f10~f13·f15~f17·f28~f31 을 쓴 모든 문장(5·6·7·9·11절)을 '[추정] 벤더 주장[^ref-…]'로 썼고, f27 은 5·8절에서 '업체 발표'로 밝혀 '[추정] 업체 발표[^ref-1459]'로 썼다.",
    "f10~f13 범위 — 6·7절에서 SAP Warehouse Robotics(SAP BTP 기반 제품, SAP EWM 과 구별)의 폐기(Deprecated) 표시 FMS 연동 API 규칙이라고 밝히고 현재 권장 연동 경로로 일반화하지 않는다고 적었다. ref-1456 각주 제목에 'LATEST URL, 확보본 2024-07-10 기준', ref-1458 각주에 'LATEST URL, 판 2308 기준'을 넣었다.",
    "f15~f18 경계 — 6절 소제목을 '우선순위 변경 허용 범위: 업무 시스템 쪽 규칙(연계 대상)'으로 두고 Oracle·SAP 규칙을 WMS 쪽 규칙으로 서술했으며, 9절에서는 이를 '외부와 연계하는 것' 칸에 두고 ROP 는 결과를 받는 쪽으로 썼다.",
    "f29 — 5절 제조 공장 사례로만 짧게 쓰고 WCS·SCADA 통합 관제를 연계 대상으로 표시해 22. 설비·건물 시스템 연동, 38. 모니터링·이상 탐지·원인 분석과 연결했다(5·9·10절).",
    "f30·f31 — 6절 '업무 객체 해석 계층'과 5절 물류창고 사례에서 업무 객체 해석 계층의 근거로만 쓰고, 물리 작업 수행은 연계 대상으로 44. 로봇 기반 모델·언어 모델 계획과 연결했다. f31 은 '탐색 단계, beta·test 환경 검증, 단일 Anigon' 단서를 표와 서술에 유지했다.",
    "ref-1462 — 본문(5절)과 각주에 게시일 2025-11-05 만 적고 수정일은 넣지 않았다(reference_updates 요약에서도 뺐다).",
    "f19~f22 정정 — 세부영역 페이지 3절에 정정 소절, 8절에 GreenAuto 정정 항목을 두어 'MES·ERP용 REST API 와 AMR 실시간 이벤트·IIoT용 MQTT broker, VDA 5050 연동은 계획(당시 미가동)'으로 고쳤고, ref-136 각주를 'Lopes, D., Pereira, T., Gonçalves, A. 외(저자 17명) … Applied Sciences 15(13) 7235, 2025-06-27, … 접근일 2026-10-11'로 바꿨다. 주제 페이지 s3 39행·s8 42행 본문은 입력에 없어 직접 고치지 못했으므로 부분 이행이며, 다음 갱신 실행 요청을 additional_research_requests 에 적었다.",
    "f21 — 8절·11절에서 '개발 대상은 서로 다른 제조사의 AMR 2대·AGV 1대'라고만 쓰고, 20. 로봇·제조사 관제 연동 페이지의 최대 20대 동시 감시와의 관계는 미확인(oq-365)으로 두었다.",
    "ref-131 각주 — 발행일 2024-01-31, 접근일 2026-10-11 로 바꾸고 '(원문 미열람)'을 떼었으며, 4절에 주제 페이지 s4·s7 의 '원문 미열람'·'상태 전이는 원문 미열람' 표시가 이번 원문 확인으로 해제 대상임을 적었다.",
    "트랙 반영 제안 3 — 4절 Update 항목(시작 전 작업 지시에만 적용, f1)을 ref-131 각주로 반영하고 7절 끝에 반영 범위를 밝혔다. Abort 대상 상태 범위와 Pause·Resume 은 넣지 않았다.",
    "트랙 반영 제안 1·2 — 페이지에 반영하지 않고 additional_research_requests 에 23. 업무 시스템 연동의 다음 실행 후보로 넘겼다.",
    "5절 국내 문단 — 기존 ref-137 문장을 유지하고 1차 출처 ref-1459 를 병기했으며, '30대 지원 발표'([추정] 업체 발표)와 '20분 이상 → 10분 이내는 앞선 실증의 업체 주장'([추정] 벤더 주장)을 나누고 남이천 실증 결과 미확인을 유지했다.",
    "5절 적용 사례 — 새 사례마다 현장 유형을 하나씩 밝혔다(병원: f37·f38, 제조 공장: f29, 물류창고: f31, 기존 물류창고 문단: f27). 병원 사례 수행 자원 칸과 서술에 '병원 안 운반은 TIAGo 1대, 이기종 관리는 별도 시험 환경'을 적었고, site_matrix_updates 는 실제로 채운 칸(병원 3, 제조 공장 2, 물류창고 3)만 냈다.",
    "ref-133 — 8절 본문에 쪽수 대신 §2·§4 만 썼고, 각주 발행일을 2025-05 로, 접근일을 2026-10-11 로 바꾸고 '(원문 미열람)'을 뗐다.",
    "용어 — FMS 는 6절 첫 등장에서 '플릿 관리 시스템(Fleet Management System, FMS)'(용어집 링크), ingestor 는 '인제스터'(용어집 링크), MCP 는 6절 첫 등장에서 '모델 컨텍스트 프로토콜(Model Context Protocol, MCP)'(용어집 링크)로 썼다.",
    "직접 인용 — 출처 원문 직접 인용을 쓰지 않았고, ref-131 의 여러 조항은 4절에서 모두 요약·재서술했다.",
    "11절 — oq-019·oq-020·oq-021(oq-351 포함)·oq-012·oq-365·oq-046·oq-141 에 부분 근거만 적고 모두 '상태: 열림'으로 유지했으며, oq-002 는 '이번 실행에서 근거를 찾지 못했다'로 두었다. 상태 변경 open_question_updates 는 내지 않았다.",
    "2차: 3·4·6·7·8·11절 링크 복원 — 여섯 절을 replace 패치로 바꿔 각 절 첫 문단의 둘째 문장으로 '2026-09-25 실행까지의 내용: [<절 제목> (2026-09-25)](../../topics/2026/2026-09-25-area01-s3.md·-s4.md·-s6.md·-s7.md·-s8.md·-s11.md)' 줄을 넣었다. 자동 분리가 원 절에 첫 문단의 앞 두 문장을 남기므로 그 안에 두었고, 원래 첫 문단의 둘째 문장(3절 '그래서 …', 4절 약어 안내, 6절 '아래는 …', 7절 표준 목록 안내, 11절 '2026-10-11 실행은 …')은 문구를 바꾸지 않고 바로 다음 문단으로 옮겼다. '자세한 내용은 주제 페이지' 문구는 쓰지 않았고 11절의 기존 그 문구 줄은 새 링크 줄로 대체했다.",
    "2차: 3·8절의 2026-09-25-area01-s3.md·-s8.md 링크 줄에 'GreenAuto(Lopes 외) REST·MQTT 서술은 2026-10-11 정정 대상이며 정정 내용은 아래에 있다'는 안내를, 4절(과 같은 표시가 있는 7절)의 2026-09-25-area01-s4.md·-s7.md 링크 줄에 'ref-131 원문 미열람·상태 전이는 원문 미열람 표시는 해제 대상'이라는 안내를 붙였다. 3절 정정 소절·4절 확인 소절·8절 GreenAuto 정정 항목의 '연결된 주제 페이지'는 각각 2026-09-25-area01-s3·s4(및 s7)·s8 주제 페이지 링크로 바꿨다.",
    "2차: 9절 '대화형 접점(MCP)'을 '대화형 접점인 [모델 컨텍스트 프로토콜](../../glossary/model-context-protocol.md)(Model Context Protocol, MCP)'로 풀어 쓰고, '6절에 적었다'를 [23. 업무 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area23-s6.md) 링크로 바꿨다.",
    "분량 초과 자동 분리: 23. 업무 시스템 연동 본문 17,538자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 6,769자"
  ]
}
```

### runs/2026-10-11-02/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/integration/business-system-integration.md (10개 절)
- 분량 초과 자동 분리:
    - docs/categories/integration/business-system-integration.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-11-area23-s6.md (3,712자)
    - docs/categories/integration/business-system-integration.md "11. 열린 질문" → docs/topics/2026/2026-10-11-area23-s11.md (2,250자)
    - docs/categories/integration/business-system-integration.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-11-area23-s7.md (1,793자)
    - docs/categories/integration/business-system-integration.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-11-area23-s8.md (1,623자)
    - docs/categories/integration/business-system-integration.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-11-area23-s10.md (1,310자)
    - docs/categories/integration/business-system-integration.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-10-11-area23-s4.md (1,034자)
    - docs/categories/integration/business-system-integration.md "3. 왜 중요한가" → docs/topics/2026/2026-10-11-area23-s3.md (675자)
```

### runs/2026-10-11-02/pages/categories/integration/business-system-integration.md

```markdown
---
title: "23. 업무 시스템 연동"
type: area
category: "F. 연동"
area_no: 23
related_areas: [12, 20, 21, 22, 24, 25, 26, 29, 30, 32, 38, 44, 61, 62, 63]
tags: [주문 갱신, 작업 취소, 출고 우선순위, ISA-95, VDA 5050, Open-RMF]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-10-11
sources: [ref-002, ref-031, ref-111, ref-125, ref-126, ref-127, ref-128, ref-129, ref-130, ref-131, ref-132, ref-133, ref-134, ref-135, ref-136, ref-137, ref-869, ref-1341, ref-1453, ref-1454, ref-1455, ref-1456, ref-1457, ref-1458, ref-1459, ref-1460, ref-1461, ref-1462, ref-1463]
last_run: 2026-10-11
version: 3
---

[홈](../../index.md) › [F. 연동](index.md) › 23. 업무 시스템 연동

# 23. 업무 시스템 연동

!!! info "소속 대분류"
    [F. 연동](index.md) — 핵심 질문:
    제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

로봇 관제 인터페이스 표준인 VDA 5050 3.0.0은 관제(fleet control)와 이동로봇 사이의 통신만 다루고, 외부 IT 시스템 같은 다른 인터페이스와 교통 관리 로직은 범위 밖에 둔다(2026-09-25 확인). [사실][^ref-031] 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 왜 중요한가 (2026-09-25)](../../topics/2026/2026-09-25-area01-s3.md) — 그 페이지의 GreenAuto(Lopes 외) REST·MQTT 서술은 2026-10-11 정정 대상이며, 정정 내용은 아래 소절에 있다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 왜 중요한가](../../topics/2026/2026-10-11-area23-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역을 읽는 데 필요한 용어는 로봇 쪽의 주문·작업 표현과 상위 시스템 쪽의 작업 지시 표현으로 나뉜다. 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 핵심 개념과 용어 (2026-09-25)](../../topics/2026/2026-09-25-area01-s4.md) — 그 페이지의 ref-131 '원문 미열람'·'상태 전이는 원문 미열람' 표시는 2026-10-11 원문 확인으로 해제 대상이며, 확인 내용은 아래 소절에 있다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 핵심 개념과 용어](../../topics/2026/2026-10-11-area23-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 첫 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 2026-10-11 실행에서 병원·제조 공장 사례와 물류창고 개념검증 사례를 그 뒤에 더했다.

**물류 흐름 단계:** 피킹 → 출하

**시나리오:** 출하 마감이 당겨진 주문 때문에 진행 중인 피킹 운반 작업을 바꾼다

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 시스템(WMS·WES)이 운송 마감이 당겨진 출고 주문의 우선순위를 올리고 변경을 ROP에 보낸다. B2MML 거래 프로파일은 CHANGE·CANCEL 같은 거래 동사를, OPC UA for ISA-95 Job Control 은 Update·Pause·Abort 같은 메서드를 정의한다. [사실][^ref-129][^ref-130] 창고 상위 시스템의 변경이 이런 형태로 올 수 있을 것으로 보인다. [추정][^ref-129][^ref-130] |
| 작업 대상 | 피킹된 토트·박스와 이를 실은 AMR 운반 작업 |
| 수행 자원 | 작업자가 피킹하고 AMR 이 운반하는 협업 구성(동적 주문 피킹 연구의 설정과 같다). [사실][^ref-132] ROP는 작업을 조정하고 제조사 관제가 로봇을 움직인다. |
| 제약 | VDA 5050 에서는 이미 공개된 base 구간을 바꿀 수 없고 [사실][^ref-031], 진행 중에 다른 orderId 의 새 주문을 보내면 로봇이 OTHER_ORDER_ACTIVE 로 거부한다. [사실][^ref-031] 주문 메시지에서 우선순위 필드는 확인되지 않았다. [추정][^ref-031] |
| 완료·인계 | 로봇 쪽 작업 상태(completed·canceled 등)를 받아 상위 시스템에 완료·취소 결과를 되돌려야 업무 완료로 인정한다. Open-RMF 작업 상태는 이런 상태 값과 취소·중단 정보를 담는다. [사실][^ref-111] |
| 예외·성과 | cancelOrder 를 보내도 취소할 수 없는 동작은 끝날 때까지 계속된다. [사실][^ref-031] 이미 화물을 실은 뒤라면 되돌림 작업이 추가로 필요할 것으로 보인다. [추정][^ref-031][^ref-129] 진행 중 사이클 수정은 완료 시간을 줄일 수 있지만 교란 비용을 조건으로 판단해야 할 것으로 보인다. [추정][^ref-132][^ref-133] |

다음은 설명을 위한 가상의 시나리오이다. 오후 운송 마감이 앞당겨진 주문이 생기자 WMS가 그 주문의 우선순위를 올린다. 해당 주문의 박스를 실은 AMR 은 이미 다른 주문의 포장대로 향하고 있고, 새 주문을 따로 보내면 거부되므로 ROP는 공개되지 않은 경로 구간을 주문 갱신으로 바꾸거나, 일시정지 후 취소하고 다시 지시하는 방법 가운데 하나를 골라야 한다.

어느 쪽을 고를지는 로봇 인터페이스가 정해 주지 않는다. 출고 우선순위가 바뀔 때 어떤 작업을 끊고 무엇을 먼저 할지 정하는 규칙은 ROP 쪽 작업 대기열·재계획 로직이 맡아야 할 것으로 보인다. [추정][^ref-031][^ref-125]

국내에서는 2025년 1월 테크타카가 자사 WMS 와 플로틱의 오더 피킹용 자율주행로봇 30대를 연동하는 자동화 모델을 남이천 물류센터에서 실증하는 협력을 발표했다고 보도됐다. 이는 협력 발표이며 실증 결과는 미확인이다. [사실][^ref-137] 같은 사건의 1차 출처인 아르고(테크타카)의 2025-01-21 업체 발표는 자사 WMS 와 플로틱 자율주행로봇을 연동한 자동화 모델을 설계해 남이천 물류센터에서 실증하고, 플로틱이 오더 피킹 특화 로봇 30대를 지원한다고 밝혔다. [추정] 업체 발표[^ref-1459] 같은 발표에서 플로틱 대표가 말한, 수작업으로 20분 이상 걸리던 오더 피킹을 10분 이내로 줄였다는 성과는 앞선 실증사업에 대한 업체 주장이며 남이천 30대 사업의 성과가 아니고 측정 조건도 공개되지 않았다. [추정] 벤더 주장[^ref-1459] 남이천 실증의 시험 기간과 결과는 여전히 미확인이다.

### 병원: 검사실 도착 뒤 인수 확인을 거쳐 로봇을 되돌림

**현장 유형:** 병원

**사례:** Tartu 대학병원에서 ICU 시료를 검사실로 운반한 뒤, 직원의 인수 확인을 거쳐 로봇을 ICU 로 되돌림

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(이번에 확인한 범위는 검사실 도착 뒤 단계이며, 운반 요청이 어디서 어떻게 만들어지는지는 이번 브리프에서 확인하지 않았다) |
| 작업 대상 | ICU 에서 검사실로 옮긴 시료와, 시료를 꺼낸 뒤 비게 되는 로봇의 운반함 [사실][^ref-869] |
| 수행 자원 | PAL Robotics TIAGo 1대가 운반하고, 검사실 직원이 화면 버튼으로 확인하며, [인제스터](../../glossary/dispenser-ingestor.md)가 Open-RMF 에 인수 완료를 알린다. TIAGo·Clearpath Jackal 두 이기종 로봇을 RMF 로 관리하는 능력은 별도 시험 환경에서 검증했고, 병원 안에는 여러 배송 로봇을 아직 적용하지 않았다. [사실][^ref-869] |
| 제약 | 미확인(이번 브리프에서 시간·구역·권한 제약을 확인하지 않았다) |
| 완료·인계 | 직원이 시료를 모두 꺼냈음을 화면 버튼으로 확인하고 인제스터가 RMF 에 인수 완료를 알린 뒤에야, 로봇을 ICU 로 되돌리는 요청이 나간다. [사실][^ref-869] |
| 예외·성과 | 미확인 |

이 실증은 로봇이 검사실에 도착한 것과 사람이 시료를 인수한 것을 서로 다른 단계로 두고, 인수 확인을 다음 작업(복귀)의 조건으로 썼다. [사실][^ref-869] 업무 시스템 연동에서 운반 완료와 업무상 인수 확정을 나눠 다루는 해외 사례이며, 국내 기준은 미확인이다(oq-012). 병원 안 운반은 로봇 1대로 했으므로 병원 내 이기종 플릿 상시 운영 사례로 볼 수 없다.

### 제조 공장: 입고부터 출하까지 생산 물류 조율

**현장 유형:** 제조 공장

**사례:** HD현대일렉트릭 청주 배전캠퍼스 신공장의 생산 물류 자동화

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(생산계획 변경을 작업으로 바꾸는 승인 규칙은 공개되지 않았다) |
| 작업 대상 | 자재 입고·보관·생산라인 공급·완제품 이송·출하로 이어지는 공장 안 물류 [추정] 벤더 주장[^ref-1460] |
| 수행 자원 | AMR·ACR 같은 물류 로봇과 이를 조율하는 창고 제어 시스템(WCS)·SCADA 기반 통합 제어·관제. WCS·SCADA 의 설비 제어·관제는 연계 대상이다. [추정] 벤더 주장[^ref-1460] |
| 제약 | 미확인(다제조사 수·API·주문 상관키는 공개되지 않았다) |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(공급자가 제시한 성과 수치는 채택하지 않았다) |

LG CNS 고객 사례(2026-07-16)는 신공장의 입고부터 출하까지 생산 물류를 WCS 와 SCADA 기반 통합 관제로 조율했다고 설명하는 공급자 단독 설명이다. [추정] 벤더 주장[^ref-1460] 이 영역에서는 생산 물류를 실행 작업으로 조율하는 제조 공장 사례로만 보고, WCS·SCADA 의 설비 제어·관제는 [22. 설비·건물 시스템 연동](facility-and-building-system-integration.md)과 [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)의 연계 대상으로 둔다.

### 물류창고: 업무 시스템 문맥을 받는 휴머노이드 개념검증

**현장 유형:** 물류창고

**사례:** Bosch·Aimbo 개념검증에서 SAP EWM 의 업무 문맥을 받아 창고 작업을 수행

| 항목 | 내용 |
|---|---|
| 시작 조건 | SAP EWM 의 배송 정보·주문 우선순위·보관 위치가 실시간 업무 문맥으로 로봇에 전달된다. [추정] 벤더 주장[^ref-1462] |
| 작업 대상 | 창고 작업(구체 품목과 작업 단위는 미확인) |
| 수행 자원 | Aimbo 의 휴머노이드 Anigon 1대. 파지 같은 물리 작업 수행은 로봇 자체 지능·제어의 연계 대상이다. [추정] 벤더 주장[^ref-1462] |
| 제약 | 탐색 단계의 개념검증으로, 전용 beta·test 시스템 환경에서 검증됐다. [추정] 벤더 주장[^ref-1462] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

SAP 뉴스(2025-11-05 게시)가 소개한 Bosch·Aimbo 공동 개념검증은 단일 Anigon 으로 beta·test 환경에서 검증한 탐색 단계 사업이며, 실시일과 생산 운영 전환 여부는 미확인이다. [추정] 벤더 주장[^ref-1462] 이 영역에서는 업무 시스템의 업무 객체를 로봇 작업 문맥으로 넘기는 해석 계층의 예로만 보고, 휴머노이드의 작업 수행 방식은 [44. 로봇 기반 모델·언어 모델 계획](../ai-and-learning/robot-foundation-models-and-llm-planning.md)에서 다룬다.

## 6. 대표 접근법과 기술

로봇 인터페이스가 제공하는 변경 수단은 주문 갱신·일시정지·취소·중단·되감기 정도이므로, 우선순위 변경 규칙과 상위 지시의 번역은 ROP 쪽 대기열·재계획 로직이 맡아야 할 것으로 보인다. [추정][^ref-031][^ref-125] 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 대표 접근법과 기술 (2026-09-25)](../../topics/2026/2026-09-25-area01-s6.md) — 그 페이지에 VDA 5050 변경 수단과 Open-RMF 중단·되감기 같은 기존 확인 내용이 있다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area23-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이번 조사에서 확인한 관련 규격은 로봇 쪽 VDA 5050 3.0.0·Open-RMF 작업 API, 상위 쪽 B2MML·OPC UA for ISA-95 Job Control·ISA-95 Part 1, 업무 범위 쪽 SCOR DS 이다. [사실][^ref-031][^ref-129]

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area23-s7.md)에 있다.

## 8. 대표 연구와 자료

이번 조사에서 확인한 자료는 동적 주문 피킹 연구와 웨이브리스 출고 지시 연구, 다제조사 플릿 관리 사례, 국내 WMS–로봇 연동 발표이다. [사실][^ref-132][^ref-134] 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 대표 연구와 자료 (2026-09-25)](../../topics/2026/2026-09-25-area01-s8.md) — 그 페이지의 GreenAuto(Lopes 외) REST·MQTT 서술은 2026-10-11 정정 대상이며, 정정 내용은 아래 항목에 있다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 대표 연구와 자료](../../topics/2026/2026-10-11-area23-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 우선순위·시작 시각·마감을 담은 작업 요청을 받아 로봇 작업으로 바꾸고, 진행 중 작업의 재정렬·수정 규칙을 적용하며, 진행·완료·취소 결과를 되돌린다 [추정][^ref-135][^ref-002][^ref-125] | 주문 접수, 출고 지시 방식(웨이브·웨이브리스), 출고 우선순위 결정(ERP·WMS·WES) |
| 상위 업무 시스템(요청 변경·결과 보고) | 취소 요청의 응답과 별도로 작업 상태를 관측해 실제 취소 결과를 확인하고 되돌린다 [추정][^ref-1454][^ref-1455] | 우선순위 변경을 허용하는 작업 상태·권한과 대기 큐 정렬 규칙(예: Ready·Held·Created 상태 제한, LSD 정렬) [추정] 벤더 주장[^ref-1457][^ref-1458] |
| 로봇 자체 지능·제어 | 제조사 관제에 주문 갱신·일시정지·취소·재지시를 보내고 상태·실패·완료를 확인한다 | 주행·정지와 동작의 실제 실행, 취소할 수 없는 동작의 수행 |
| 로봇 자체 지능·제어(휴머노이드 작업) | 업무 객체(주문 우선순위·보관 위치)를 작업 문맥으로 넘기는 해석 계층 | 파지 같은 물리 작업 수행 [추정] 벤더 주장[^ref-1462] |
| 시설·설비 제어 | 생산 물류 작업의 요청·상태 확인과 결과 반영 | WCS·SCADA 기반 설비 제어·관제(제조 공장 사례) [추정] 벤더 주장[^ref-1460] |
| 업종별 조건 | 로봇 도착 통지와 수령인의 인수 확인을 서로 다른 완료 단계로 받는다. 근거 사례: Tartu 대학병원 실증은 직원 확인과 인제스터의 인수 완료 통지 뒤에야 복귀 요청을 냈다 [사실][^ref-869] | 의료 등 업종별 전문 요구사항 |

연계 대상: 주문 접수·출고 지시 방식과 출고 우선순위 결정은 ERP·WMS·WES 같은 상위 업무 시스템의 몫이고, ROP는 그 결과를 작업 요청의 우선순위·시작 시각·마감 제약으로 받아 로봇 작업으로 바꾸고 결과를 되돌리는 경계에 서는 것으로 보인다. [추정][^ref-135][^ref-134][^ref-002][^ref-125] VDA 5050 은 외부 IT 인터페이스를 범위 밖에 둔다. [사실][^ref-031] 따라서 상위 시스템과의 번역 계층은 ROP 쪽 인터페이스 설계 과제가 될 것으로 보인다. [추정][^ref-031]

구축자 의견: 업무 시스템–관제 인터페이스를 비교할 때는 접수 응답, 진행 통지(콜백·상태), 취소 결과, 업무 확정을 따로 보는 것이 좋아 보인다. [의견][^ref-1456][^ref-1453][^ref-1454] 우선순위 변경 허용 범위는 WMS 쪽 규칙이므로 ROP 는 그 결과를 받는 쪽에 서고, 제조 공장의 WCS·SCADA 관제는 [22. 설비·건물 시스템 연동](facility-and-building-system-integration.md)·[38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)의 연계 대상으로 둔다. 대화형 접점인 [모델 컨텍스트 프로토콜](../../glossary/model-context-protocol.md)(Model Context Protocol, MCP)의 도구 범위와 업무 요구의 차이는 [23. 업무 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area23-s6.md)에 적었다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자세한 기준은 [범위 경계](../../about/scope-boundary.md) 페이지에 있으며, 이종 제조사를 연결하는 ROP라면 로봇 동작 실행은 제조사에 맡기고 변경 지시의 번역과 결과 확인을 맡는 구도가 된다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md) — ISA-95 작업 지시와 Open-RMF 작업 상태를 업무 단계와 잇는 문제를 함께 다루며, 같은 출처(작업 상태 스키마, task_new)를 공유한다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 다른 연구영역과의 연결](../../topics/2026/2026-10-11-area23-s10.md)에 있다.

## 11. 열린 질문

2026-09-25 실행에서 새로 열린 질문 세 개는 [열린 질문](../../open-questions.md) 목록의 oq-019(출고 우선순위 재정렬 설계), oq-020(상위 작업 지시와 로봇 인터페이스 사이 매핑), oq-021(적재 후 취소의 되돌림 규칙)이다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 열린 질문](../../topics/2026/2026-10-11-area23-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [23. 업무 시스템 연동](business-system-integration.md) — 섹션 3~11 신규 작성(자동 분리 반영). 2차 수정: 각주 ref-138·ref-182 → ref-110·ref-111, 5절 시작 조건·9절 마지막 문장 사실/추정 분리, 9절 표 태그 추가, 7·8절 첫 문장 목록 서술로 변경, sources 에서 미인용 ref-131 제외 (실행 2026-09-25-13)
- 2026-09-25 · 생성 · [23. 업무 시스템 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area01-s4.md) — 자동 분리: 1. 주문·업무 시스템 연계 의 "4. 핵심 개념과 용어" 절. 2차 수정: 각주 ref-182 → ref-111 (실행 2026-09-25-13)
- 2026-09-25 · 생성 · [23. 업무 시스템 연동 — 대표 연구와 자료](../../topics/2026/2026-09-25-area01-s8.md) — 자동 분리: 1. 주문·업무 시스템 연계 의 "8. 대표 연구와 자료" 절. 2차 수정: 첫 문장을 '이번 조사에서 확인한 자료는 … 이다'로 변경 (실행 2026-09-25-13)
- 2026-09-25 · 생성 · [23. 업무 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area01-s6.md) — 자동 분리: 1. 주문·업무 시스템 연계 의 "6. 대표 접근법과 기술" 절. 2차 수정: 각주 ref-138 → ref-110, 번역 절 마지막 문장 사실/추정 분리 (실행 2026-09-25-13)
- 2026-09-25 · 생성 · [23. 업무 시스템 연동 — 열린 질문](../../topics/2026/2026-09-25-area01-s11.md) — 자동 분리: 1. 주문·업무 시스템 연계 의 "11. 열린 질문" 절(2차 수정 없음) (실행 2026-09-25-13)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-002]: ISA, Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems, 2025-04-10, https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of, 접근일 2026-09-25 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25
[^ref-129]: MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd, 접근일 2026-09-25
[^ref-130]: OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv), 2024-01-31, https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL, 접근일 2026-09-25
[^ref-132]: Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations, 2025, https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231, 접근일 2026-09-25 (원문 미열람)
[^ref-133]: Lorenz, Otto, & Gendreau (Networks, Wiley), Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization?, 2025-05, https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281, 접근일 2026-10-11
[^ref-134]: Gallien, J., & Weber, T. G., To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter, 2010, https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291, 접근일 2026-09-25 (원문 미열람)
[^ref-135]: ASCM, SCOR Digital Standard — Introduction and Front Matter (SCOR Version 14.0, 2025), 2025, https://www.ascm.org/globalassets/ascm_website_assets/docs/scor/intro-and-front-matter-scor-digital-standard-2025.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-137]: 머니투데이, 물류센터 관리시스템에 로봇 연동…"물류 자동화 새 표준 만든다", 2025-01, https://news.mt.co.kr/mtview.php?no=2025012116183583251, 접근일 2026-09-25 (원문 미열람)
[^ref-869]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-10-11
[^ref-1453]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/dispatch_task_response.json, 접근일 2026-10-11
[^ref-1454]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/cancel_task_response.json, 접근일 2026-10-11
[^ref-1455]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/simple_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/simple_response.json, 접근일 2026-10-11
[^ref-1456]: SAP, APIs for Integration via Fleet Management Systems (API for Integration with Fleet Management Systems (Deprecated); LATEST URL, 확보본 2024-07-10 기준), 2024-07-10, https://help.sap.com/doc/a02ad3695d5845fca1678810cb83562b/LATEST/en-US/379d6d880e5d4007b3751618080da80f_1.pdf, 접근일 2026-10-11
[^ref-1457]: Oracle, WMS REST API Guide — Change Priority (Oracle Warehouse Management Cloud 26c), 2026-08-14, https://docs.oracle.com/en/cloud/saas/warehouse-management/26c/owmre/change-priority.html, 접근일 2026-10-11
[^ref-1458]: SAP, End-User Information for Integration via Integration Services (SAP Warehouse Robotics, Document Version 2308; LATEST URL, 판 2308 기준), 2023-08-19, https://help.sap.com/doc/f08ea8f8686c46e89f1d7ed121f19d68/LATEST/en-US/b82aa9c86bd74777b86ec7f5766252d0.pdf, 접근일 2026-10-11
[^ref-1459]: 아르고 풀필먼트(테크타카), 아르고, 플로틱과 로봇 기반 물류 생산성 향상 실증 본격 실시, 2025-01-21, https://blog.argoport.com/pr-robotcooperation250121, 접근일 2026-10-11
[^ref-1460]: LG CNS, 로봇 기반 물류 자동화와 통합 관제로 HD현대일렉트릭 신공장의 새로운 운영 체계를 구축하다, 2026-07-16, https://www.lgcns.com/kr/moa/customer-story/detail.smartlogistics-robotic-logistics-2607-1, 접근일 2026-10-11
[^ref-1462]: SAP (Lukasz Ostrowski, SAP News Center), How SAP Brings Business AI into the Physical World: New Robotics Pilots Across Warehouse, Manufacturing, and Inspection Use Cases, 2025-11-05, https://news.sap.com/2025/11/sap-physical-ai-partnerships-new-robotics-pilots/, 접근일 2026-10-11
```

### docs/categories/integration/business-system-integration.md

```markdown
---
title: "23. 업무 시스템 연동"
type: area
category: "F. 연동"
area_no: 23
related_areas: [20, 21, 24, 25, 26, 29, 32]
tags: [주문 갱신, 작업 취소, 출고 우선순위, ISA-95, VDA 5050, Open-RMF]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-002, ref-031, ref-111, ref-125, ref-126, ref-127, ref-128, ref-129, ref-130, ref-132, ref-133, ref-134, ref-135, ref-136, ref-137]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [F. 연동](index.md) › 23. 업무 시스템 연동

# 23. 업무 시스템 연동

!!! info "소속 대분류"
    [F. 연동](index.md) — 핵심 질문:
    제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

로봇 관제 인터페이스 표준인 VDA 5050 3.0.0은 관제(fleet control)와 이동로봇 사이의 통신만 다루고, 외부 IT 시스템 같은 다른 인터페이스와 교통 관리 로직은 범위 밖에 둔다(2026-09-25 확인). [사실][^ref-031] 그래서 ERP·WMS·MES 같은 상위 시스템의 주문과 변경을 로봇 작업으로 옮기는 일은 로봇 표준이 대신해 주지 않는다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 왜 중요한가](../../topics/2026/2026-09-25-area01-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역을 읽는 데 필요한 용어는 로봇 쪽의 주문·작업 표현과 상위 시스템 쪽의 작업 지시 표현으로 나뉜다. 업무 시스템 약어는 [WES·WCS·WMS·MES·TMS](../../glossary/wes-wcs-wms-mes-tms.md)를 참고한다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area01-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹 → 출하

**시나리오:** 출하 마감이 당겨진 주문 때문에 진행 중인 피킹 운반 작업을 바꾼다

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 시스템(WMS·WES)이 운송 마감이 당겨진 출고 주문의 우선순위를 올리고 변경을 ROP에 보낸다. B2MML 거래 프로파일은 CHANGE·CANCEL 같은 거래 동사를, OPC UA for ISA-95 Job Control 은 Update·Pause·Abort 같은 메서드를 정의한다. [사실][^ref-129][^ref-130] 창고 상위 시스템의 변경이 이런 형태로 올 수 있을 것으로 보인다. [추정][^ref-129][^ref-130] |
| 작업 대상 | 피킹된 토트·박스와 이를 실은 AMR 운반 작업 |
| 수행 자원 | 작업자가 피킹하고 AMR 이 운반하는 협업 구성(동적 주문 피킹 연구의 설정과 같다). [사실][^ref-132] ROP는 작업을 조정하고 제조사 관제가 로봇을 움직인다. |
| 제약 | VDA 5050 에서는 이미 공개된 base 구간을 바꿀 수 없고 [사실][^ref-031], 진행 중에 다른 orderId 의 새 주문을 보내면 로봇이 OTHER_ORDER_ACTIVE 로 거부한다. [사실][^ref-031] 주문 메시지에서 우선순위 필드는 확인되지 않았다. [추정][^ref-031] |
| 완료·인계 | 로봇 쪽 작업 상태(completed·canceled 등)를 받아 상위 시스템에 완료·취소 결과를 되돌려야 업무 완료로 인정한다. Open-RMF 작업 상태는 이런 상태 값과 취소·중단 정보를 담는다. [사실][^ref-111] |
| 예외·성과 | cancelOrder 를 보내도 취소할 수 없는 동작은 끝날 때까지 계속된다. [사실][^ref-031] 이미 화물을 실은 뒤라면 되돌림 작업이 추가로 필요할 것으로 보인다. [추정][^ref-031][^ref-129] 진행 중 사이클 수정은 완료 시간을 줄일 수 있지만 교란 비용을 조건으로 판단해야 할 것으로 보인다. [추정][^ref-132][^ref-133] |

다음은 설명을 위한 가상의 시나리오이다. 오후 운송 마감이 앞당겨진 주문이 생기자 WMS가 그 주문의 우선순위를 올린다. 해당 주문의 박스를 실은 AMR 은 이미 다른 주문의 포장대로 향하고 있고, 새 주문을 따로 보내면 거부되므로 ROP는 공개되지 않은 경로 구간을 주문 갱신으로 바꾸거나, 일시정지 후 취소하고 다시 지시하는 방법 가운데 하나를 골라야 한다.

어느 쪽을 고를지는 로봇 인터페이스가 정해 주지 않는다. 출고 우선순위가 바뀔 때 어떤 작업을 끊고 무엇을 먼저 할지 정하는 규칙은 ROP 쪽 작업 대기열·재계획 로직이 맡아야 할 것으로 보인다. [추정][^ref-031][^ref-125]

국내에서는 2025년 1월 테크타카가 자사 WMS 와 플로틱의 오더 피킹용 자율주행로봇 30대를 연동하는 자동화 모델을 남이천 물류센터에서 실증하는 협력을 발표했다고 보도됐다. 이는 협력 발표이며 실증 결과는 미확인이다. [사실][^ref-137]

## 6. 대표 접근법과 기술

로봇 인터페이스가 제공하는 변경 수단은 주문 갱신·일시정지·취소·중단·되감기 정도이므로, 우선순위 변경 규칙과 상위 지시의 번역은 ROP 쪽 대기열·재계획 로직이 맡아야 할 것으로 보인다. [추정][^ref-031][^ref-125] 아래는 이번 조사에서 확인한 수단과 연구 접근이다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area01-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이번 조사에서 확인한 관련 규격은 로봇 쪽 VDA 5050 3.0.0·Open-RMF 작업 API, 상위 쪽 B2MML·OPC UA for ISA-95 Job Control·ISA-95 Part 1, 업무 범위 쪽 SCOR DS 이다. [사실][^ref-031][^ref-129] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area01-s7.md)에 있다.

## 8. 대표 연구와 자료

이번 조사에서 확인한 자료는 동적 주문 피킹 연구와 웨이브리스 출고 지시 연구, 다제조사 플릿 관리 사례, 국내 WMS–로봇 연동 발표이다. [사실][^ref-132][^ref-134]

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 대표 연구와 자료](../../topics/2026/2026-09-25-area01-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 우선순위·시작 시각·마감을 담은 작업 요청을 받아 로봇 작업으로 바꾸고, 진행 중 작업의 재정렬·수정 규칙을 적용하며, 진행·완료·취소 결과를 되돌린다 [추정][^ref-135][^ref-002][^ref-125] | 주문 접수, 출고 지시 방식(웨이브·웨이브리스), 출고 우선순위 결정(ERP·WMS·WES) |
| 로봇 자체 지능·제어 | 제조사 관제에 주문 갱신·일시정지·취소·재지시를 보내고 상태·실패·완료를 확인한다 | 주행·정지와 동작의 실제 실행, 취소할 수 없는 동작의 수행 |

연계 대상: 주문 접수·출고 지시 방식과 출고 우선순위 결정은 ERP·WMS·WES 같은 상위 업무 시스템의 몫이고, ROP는 그 결과를 작업 요청의 우선순위·시작 시각·마감 제약으로 받아 로봇 작업으로 바꾸고 결과를 되돌리는 경계에 서는 것으로 보인다. [추정][^ref-135][^ref-134][^ref-002][^ref-125] VDA 5050 은 외부 IT 인터페이스를 범위 밖에 둔다. [사실][^ref-031] 따라서 상위 시스템과의 번역 계층은 ROP 쪽 인터페이스 설계 과제가 될 것으로 보인다. [추정][^ref-031]

이 경계는 제품 전략에 따라 이동할 수 있다. 자세한 기준은 [범위 경계](../../about/scope-boundary.md) 페이지에 있으며, 이종 제조사를 연결하는 ROP라면 로봇 동작 실행은 제조사에 맡기고 변경 지시의 번역과 결과 확인을 맡는 구도가 된다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

- [24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md) — ISA-95 작업 지시와 Open-RMF 작업 상태를 업무 단계와 잇는 문제를 함께 다루며, 같은 출처(작업 상태 스키마, task_new)를 공유한다.
- [20. 로봇·제조사 관제 연동](robot-and-vendor-fleet-manager-integration.md) — VDA 5050 주문 갱신·취소와 Open-RMF 작업 요청은 제조사 관제와의 인터페이스 자체다.
- [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md) — 새 주문 거부(OTHER_ORDER_ACTIVE)와 취소·중단·되감기 요청의 처리 결과 확인이 실행 신뢰성과 이어진다.
- [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md) — 가장 적합한 플릿에 작업을 맡기는 요청 방식과 AMR 가용성에 따른 개입 전략이 배정 문제와 겹친다.
- [26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md) — 출고 우선순위 변경에 따른 대기열 재정렬과 동적 재최적화가 순서 결정 문제다.
- [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 적재 후 취소의 되돌림 작업과 취소 불가 동작 처리가 복구·재계획 과제다.
- [21. 상호운용 표준·적합성](interoperability-standards-and-conformance.md) — ISA-95 계열과 로봇 인터페이스 사이 표준 매핑이 확인되지 않은 점이 상호운용성 과제다.

## 11. 열린 질문

출고 우선순위 재정렬 설계, 상위 작업 지시와 로봇 인터페이스 사이 매핑, 적재 후 취소의 되돌림 규칙이 이번 실행에서 새로 열린 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [23. 업무 시스템 연동 — 열린 질문](../../topics/2026/2026-09-25-area01-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [23. 업무 시스템 연동](business-system-integration.md) — 섹션 3~11 신규 작성(자동 분리 반영). 2차 수정: 각주 ref-138·ref-182 → ref-110·ref-111, 5절 시작 조건·9절 마지막 문장 사실/추정 분리, 9절 표 태그 추가, 7·8절 첫 문장 목록 서술로 변경, sources 에서 미인용 ref-131 제외 (실행 2026-09-25-13)
- 2026-09-25 · 생성 · [23. 업무 시스템 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area01-s4.md) — 자동 분리: 1. 주문·업무 시스템 연계 의 "4. 핵심 개념과 용어" 절. 2차 수정: 각주 ref-182 → ref-111 (실행 2026-09-25-13)
- 2026-09-25 · 생성 · [23. 업무 시스템 연동 — 대표 연구와 자료](../../topics/2026/2026-09-25-area01-s8.md) — 자동 분리: 1. 주문·업무 시스템 연계 의 "8. 대표 연구와 자료" 절. 2차 수정: 첫 문장을 '이번 조사에서 확인한 자료는 … 이다'로 변경 (실행 2026-09-25-13)
- 2026-09-25 · 생성 · [23. 업무 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area01-s6.md) — 자동 분리: 1. 주문·업무 시스템 연계 의 "6. 대표 접근법과 기술" 절. 2차 수정: 각주 ref-138 → ref-110, 번역 절 마지막 문장 사실/추정 분리 (실행 2026-09-25-13)
- 2026-09-25 · 생성 · [23. 업무 시스템 연동 — 열린 질문](../../topics/2026/2026-09-25-area01-s11.md) — 자동 분리: 1. 주문·업무 시스템 연계 의 "11. 열린 질문" 절(2차 수정 없음) (실행 2026-09-25-13)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-002]: ISA, Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems, 2025-04-10, https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of, 접근일 2026-09-25 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25
[^ref-129]: MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd, 접근일 2026-09-25
[^ref-130]: OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv), 2024-01-31, https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL, 접근일 2026-09-25
[^ref-132]: Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations, 2025, https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231, 접근일 2026-09-25 (원문 미열람)
[^ref-133]: Lorenz, Otto, & Gendreau (Networks, Wiley), Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization?, 2025, https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281, 접근일 2026-09-25 (원문 미열람)
[^ref-134]: Gallien, J., & Weber, T. G., To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter, 2010, https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291, 접근일 2026-09-25 (원문 미열람)
[^ref-135]: ASCM, SCOR Digital Standard — Introduction and Front Matter (SCOR Version 14.0, 2025), 2025, https://www.ascm.org/globalassets/ascm_website_assets/docs/scor/intro-and-front-matter-scor-digital-standard-2025.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-137]: 머니투데이, 물류센터 관리시스템에 로봇 연동…"물류 자동화 새 표준 만든다", 2025-01, https://news.mt.co.kr/mtview.php?no=2025012116183583251, 접근일 2026-09-25 (원문 미열람)
```

### runs/2026-10-11-02/pages/topics/2026/2026-10-11-area23-s6.md

```markdown
---
title: "23. 업무 시스템 연동 — 대표 접근법과 기술"
type: topic
category: "F. 연동"
primary_area_no: 23
related_areas: [12, 20, 21, 22, 24, 25, 26, 29, 30, 32, 38, 44, 61, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-125, ref-131, ref-1341, ref-1453, ref-1454, ref-1455, ref-1456, ref-1457, ref-1458, ref-1461, ref-1463]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/business-system-integration.md#6
---

[홈](../../index.md) › [주제](../index.md) › 23. 업무 시스템 연동 — 대표 접근법과 기술

# 23. 업무 시스템 연동 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇 인터페이스가 제공하는 변경 수단은 주문 갱신·일시정지·취소·중단·되감기 정도이므로, 우선순위 변경 규칙과 상위 지시의 번역은 ROP 쪽 대기열·재계획 로직이 맡아야 할 것으로 보인다. [추정][^ref-031][^ref-125] 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 대표 접근법과 기술 (2026-09-25)](2026-09-25-area01-s6.md) — 그 페이지에 VDA 5050 변경 수단과 Open-RMF 중단·되감기 같은 기존 확인 내용이 있다.
- 이 페이지는 [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇 인터페이스가 제공하는 변경 수단은 주문 갱신·일시정지·취소·중단·되감기 정도이므로, 우선순위 변경 규칙과 상위 지시의 번역은 ROP 쪽 대기열·재계획 로직이 맡아야 할 것으로 보인다. [추정][^ref-031][^ref-125] 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 대표 접근법과 기술 (2026-09-25)](2026-09-25-area01-s6.md) — 그 페이지에 VDA 5050 변경 수단과 Open-RMF 중단·되감기 같은 기존 확인 내용이 있다.

아래는 이번 조사에서 확인한 수단과 연구 접근이다.

### 2026-10-11 보강: 접수 응답과 실제 진행·취소 결과의 분리

Open-RMF rmf_api_msgs 의 작업 배정 응답 스키마(커밋 e9b7630 고정본, 2026-10-11 확인)는 성공이면 success 와 작업 상태(task_state 를 따르는 state)를 필수로 요구하고, 실패면 실패 이유를 담는 errors 배열을 둔다. [사실][^ref-1453] 같은 저장소의 취소 응답 스키마는 자체 필드 없이 simple_response 를 참조하며, simple_response 는 성공이면 success=true 만, 실패면 success=false 와 errors 를 필수로 요구한다. [사실][^ref-1454][^ref-1455] 따라서 Open-RMF 의 취소 응답은 요청 처리의 성패만 알리고, 작업이 실제로 멈춰 canceled 상태가 됐는지는 작업 상태(task_state)를 따로 관측해 확인해야 할 것으로 보인다. [추정][^ref-1454][^ref-1455] 응답과 실제 정지의 시간 관계와 중복 요청의 효과는 미확인이다.

SAP Warehouse Robotics(SAP BTP 위에 만든 제품으로 SAP EWM 과 구별된다)의 [플릿 관리 시스템](../../glossary/fleet-management-system.md)(Fleet Management System, FMS) 연동 API 문서는 이 API 를 폐기(Deprecated)로 표시한다(LATEST URL, 확보본 2024-07-10 기준). [추정] 벤더 주장[^ref-1456][^ref-1458] 아래 세 규칙은 모두 이 폐기 표시된 API 의 것이며, SAP 의 현재 권장 연동 경로의 계약으로 일반화하지 않는다(현재 경로의 계약은 미확인).

- FMS 는 요청에 대한 응답을 관련 콜백 메서드 호출보다 먼저 돌려줘야 한다(요청 → 응답 → 콜백 순서). [추정] 벤더 주장[^ref-1456]
- 취소에 성공하면 Update Robot Task Status 로 taskStatus 를 CANCELLED 로 알리고, 취소할 수 없으면 별도 메서드 Update Robot Task Cancelation Status 로 알린다. [추정] 벤더 주장[^ref-1456]
- 공통 메시지는 UUID 형식의 messageId 를 필수로 두고 작업은 이와 별도인 robotTaskId 로 가리켜 메시지 식별과 작업 식별을 나누며, 중복 제거나 재시도 보장 같은 운영 보장은 문서에 없다. [추정] 벤더 주장[^ref-1456]

구축자 의견: 업무 시스템–관제 인터페이스를 비교할 때는 접수 응답, 진행 통지(콜백·상태), 취소 결과, 업무 확정을 따로 보는 것이 좋아 보인다. [의견][^ref-1456][^ref-1453][^ref-1454]

### 업무 '취소'를 로봇 명령으로 옮기기 전의 상태 확인

구축자 의견: 업무 쪽 '취소'를 로봇 명령 하나로 옮기기 전에 작업의 현재 상태(시작 전·실행 중·종료 후), 지울 기록과 남길 이력, 실행 종료 뒤 후처리 여부를 먼저 정해야 할 것으로 보이며, 그 근거는 OPC UA for ISA-95 Job Control 이 시작 전 취소·실행 중 정지·완료 뒤 종결을 서로 다른 메서드와 상태로 둔다는 점이다(4절). [의견][^ref-131] 이 상태들과 VDA 5050·Open-RMF 상태 사이의 표준 매핑은 확인하지 못했다(oq-020).

### 우선순위 변경 허용 범위: 업무 시스템 쪽 규칙(연계 대상)

우선순위 변경을 언제 허용하고 대기열을 어떤 순서로 정렬할지는 아래처럼 연계 대상인 상위 업무 시스템(WMS) 쪽에서 정하는 규칙이다.

- Oracle WMS Cloud 26c REST API 의 작업 우선순위 변경 API 는 Ready·Held·Created 상태인 작업의 우선순위만 바꿀 수 있다고 명시한다. [추정] 벤더 주장[^ref-1457]
- 같은 API 는 외부 시스템이 다른 작업의 긴급도에 따라 우선순위를 바꿀 수 있게 하되, Task/Change task priority 권한이 켜져 있을 때만 쓰게 한다. [추정] 벤더 주장[^ref-1457]
- SAP Warehouse Robotics 의 integration services 경로 문서(판 2308 기준)는 로봇 배정 최적화를 켜지 않으면 로봇이 속한 자원 그룹의 큐 순서를 따르고(첫 큐를 끝내야 다음 큐), 큐 안의 창고 오더를 latest starting date(LSD) 순으로, LSD 가 없으면 생성 시각 순으로 정렬한다고 설명하며, 이 경로는 위 FMS API 와 다른 연동 경로다. [추정] 벤더 주장[^ref-1458]

구축자 의견: ROP 쪽에서는 업무 시스템이 허용해 바꾼 우선순위를 받되, 변경 가능 여부를 업무 작업의 상태와 로봇 실행 단계에 대해 따로 검사하고, 대기열 재정렬과 진행 중 작업 선점은 별도 정책으로 두는 것이 좋아 보인다. [의견][^ref-1457][^ref-1458] 진행 중 Open-RMF 작업의 재정렬 방법과 업체 간 우선순위 숫자의 대응은 미확인이다(oq-019).

### 업무 객체 해석 계층

SAP Architecture Center 의 참조구조 'Warehouse Pick & Place with Embodied AI Robotics'(2026-05-12 갱신)는 이송 오더를 만들고 관리하지만 물건을 집지는 못하는 디지털 창고 AI 에이전트와 구별해, 체화(Embodied) AI 에이전트의 세 가지 주요 skill 가운데 하나로 업무 객체의 의미 이해(WMS 데이터 속성, 예를 들어 주문 우선순위·취급 요건이 물리 작업 실행에 뜻하는 바)를 든다. [추정] 벤더 주장[^ref-1461] 이 영역에서는 이를 업무 객체를 로봇 작업 문맥으로 옮기는 해석 계층의 근거로만 보고, 로봇의 물리 작업 수행은 연계 대상으로 [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md)에서 다룬다. 개념검증 사례는 5절의 물류창고 사례(Bosch·Aimbo)에 있다.

### 모델 컨텍스트 프로토콜(MCP) 같은 새 접점의 실제 범위

NVIDIA Isaac Mission Dispatch README(커밋 56455eb 고정본)의 갱신 표는 2026-03 에 Mission Dispatch MCP 추가를, 2026-08 에 VDA5050 3.0 지원과 generic action node 추가를 기록한다. [사실][^ref-1341] 같은 커밋의 Mission Dispatch [모델 컨텍스트 프로토콜](../../glossary/model-context-protocol.md)(Model Context Protocol, MCP) 서버는 도구 11개(로봇 상태·미션 상태·미션 중 로봇·유휴 로봇·플릿 요약·로봇 건강 점검·미션 큐·최근 실패 조회, 연결 시험, 로봇 등록, 좌표 이동 미션 전송)를 등록하고 미션 취소 도구는 두지 않는 것으로 보이나, 공개 코드의 파일 경로가 출처에 기록되지 않아 검증에서 다시 확인하지 못했다. [추정][^ref-1341] 이 서버의 이동 미션 처리는 경유점 하나짜리 route 미션 트리와 timeout·deadline 을 담아 Mission Dispatch REST API 의 mission 경로로 POST 하는 것으로 보이나, 이 역시 코드 파일 경로가 출처에 기록되지 않아 검증에서 다시 확인하지 못했다. [추정][^ref-1341]

robotmcp 의 demos-ros-mcp-server 예제 1 README(커밋 edbc642 고정본)는 Ubuntu 22.04·ROS 2 Humble·Ignition Gazebo Fortress 에서 ROS-MCP 서버로 창고 시뮬레이션 속 Tugbot 1대를 자연어로 이동시키고 라이다·주행거리 센서와 위치를 조회하는 예시를 설명하며, 업무 시스템 연동은 다루지 않는다. [사실][^ref-1463]

구축자 의견: MCP 를 업무 요청의 접점으로 평가할 때는 공개 코드가 주는 도구 범위(조회·등록·좌표 이동)와 업무 요구(주문 id 대응·허용 상태 검사·실행 전 승인·결과 대조·취소)를 따로 확인해야 하며, 공개 코드의 존재를 다사업자 WMS 주문·재고 처리의 운영 검증으로 볼 수 없다. [의견][^ref-1341][^ref-1463] 대화로 업무를 지시하는 일 자체는 [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)에서 다룬다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/business-system-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/business-system-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/business-system-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25
[^ref-131]: OPC Foundation / ISA, OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4), 2024-01-31, https://reference.opcfoundation.org/specs/OPC-10031-4/6.2, 접근일 2026-10-11
[^ref-1341]: NVIDIA (nvidia-isaac GitHub), isaac_mission_dispatch — README, 미확인, https://github.com/nvidia-isaac/isaac_mission_dispatch, 접근일 2026-10-11
[^ref-1453]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/dispatch_task_response.json, 접근일 2026-10-11
[^ref-1454]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/cancel_task_response.json, 접근일 2026-10-11
[^ref-1455]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/simple_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/simple_response.json, 접근일 2026-10-11
[^ref-1456]: SAP, APIs for Integration via Fleet Management Systems (API for Integration with Fleet Management Systems (Deprecated); LATEST URL, 확보본 2024-07-10 기준), 2024-07-10, https://help.sap.com/doc/a02ad3695d5845fca1678810cb83562b/LATEST/en-US/379d6d880e5d4007b3751618080da80f_1.pdf, 접근일 2026-10-11
[^ref-1457]: Oracle, WMS REST API Guide — Change Priority (Oracle Warehouse Management Cloud 26c), 2026-08-14, https://docs.oracle.com/en/cloud/saas/warehouse-management/26c/owmre/change-priority.html, 접근일 2026-10-11
[^ref-1458]: SAP, End-User Information for Integration via Integration Services (SAP Warehouse Robotics, Document Version 2308; LATEST URL, 판 2308 기준), 2023-08-19, https://help.sap.com/doc/f08ea8f8686c46e89f1d7ed121f19d68/LATEST/en-US/b82aa9c86bd74777b86ec7f5766252d0.pdf, 접근일 2026-10-11
[^ref-1461]: SAP Architecture Center, Warehouse Pick & Place with Embodied AI Robotics, 미확인, https://architecture.learning.sap.com/docs/ref-arch/7e4168, 접근일 2026-10-11
[^ref-1463]: robotmcp, demos-ros-mcp-server — Example 1: Tugbot Warehouse Simulation (Ignition Gazebo) README, 미확인, https://github.com/robotmcp/demos-ros-mcp-server/blob/edbc642849bdde1187771a15e557ec9e219184a5/1_Gazebo_Tugbot/README.md, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-02 | 23. 업무 시스템 연동 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-11-02/pages/topics/2026/2026-10-11-area23-s11.md

```markdown
---
title: "23. 업무 시스템 연동 — 열린 질문"
type: topic
category: "F. 연동"
primary_area_no: 23
related_areas: [12, 20, 21, 22, 24, 25, 26, 29, 30, 32, 38, 44, 61, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-131, ref-1341, ref-136, ref-1453, ref-1454, ref-1455, ref-1456, ref-1457, ref-1458, ref-869]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/business-system-integration.md#11
---

[홈](../../index.md) › [주제](../index.md) › 23. 업무 시스템 연동 — 열린 질문

# 23. 업무 시스템 연동 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 2026-09-25 실행에서 새로 열린 질문 세 개는 [열린 질문](../../open-questions.md) 목록의 oq-019(출고 우선순위 재정렬 설계), oq-020(상위 작업 지시와 로봇 인터페이스 사이 매핑), oq-021(적재 후 취소의 되돌림 규칙)이다.
- 이 페이지는 [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

2026-09-25 실행에서 새로 열린 질문 세 개는 [열린 질문](../../open-questions.md) 목록의 oq-019(출고 우선순위 재정렬 설계), oq-020(상위 작업 지시와 로봇 인터페이스 사이 매핑), oq-021(적재 후 취소의 되돌림 규칙)이다. 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 열린 질문 (2026-09-25)](2026-09-25-area01-s11.md)

2026-10-11 실행은 아래 질문에 부분 근거를 더했으나 해결로 인정된 질문은 없고, 모두 열림 상태를 유지한다.

### 부분 근거를 더한 질문 (2026-10-11)

- **oq-019** (상태: 열림) 상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가? — 부분 근거: WMS 쪽에는 시작 전 상태(Ready·Held·Created)와 권한으로 우선순위 변경을 제한하는 규칙이 있다. [추정] 벤더 주장[^ref-1457] 대기 큐를 LSD·생성 시각 순으로 정렬하는 규칙도 있다. [추정] 벤더 주장[^ref-1458] 진행 중 Open-RMF 작업의 재정렬 방법과 업체 간 우선순위 숫자의 대응은 미확인이다.
- **oq-020** (상태: 열림) ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? — 부분 근거: OPC UA for ISA-95 Job Control 2.00.0 의 갱신·취소·정지·완료 조건을 원문으로 확인했다(4절). [사실][^ref-131] Open-RMF 배정 응답이 성공 시 작업 상태를 함께 돌려준다는 점도 확인했다. [사실][^ref-1453] 두 쪽을 잇는 공개 매핑 명세는 찾지 못했다.
- **oq-021** (상태: 열림) 로봇이 이미 화물을 싣거나 옮긴 뒤 상위 시스템이 주문을 취소·변경하면 되돌림 작업과 재고 반영을 누가 어떤 규칙으로 정하는가(국내 물류센터 사례 포함)? — 부분 근거(oq-351 에도 해당): 폐기 표시된 SAP Warehouse Robotics FMS 연동 API 는 취소 성공과 취소 불가를 서로 다른 메서드로 알린다. [추정] 벤더 주장[^ref-1456] Open-RMF 취소 응답은 성패만 알려 실제 취소는 작업 상태로 확인해야 할 것으로 보인다. [추정][^ref-1454][^ref-1455] 적재 후 취소의 반송·재고 반제 결정권자는 미확인이다.
- **oq-012** (상태: 열림) 국내 물류센터는 로봇의 운반 완료와 WMS의 입고·인수 확정을 별도 단계로 두는가, 그렇다면 두 단계를 잇는 식별 키와 확정 대기 시간 기준은 무엇인가? — 부분 근거: Tartu 대학병원 실증은 로봇 도착과 직원의 인수 확인을 별도 단계로 두었다. [사실][^ref-869] 해외 병원 사례이며 국내 WMS 입고·인수 확정의 식별 키·대기 시간 기준은 미확인이다.
- **oq-046** (상태: 열림) 상위 시스템 요청의 중복을 판별하는 키를 ROP 가 얼마 동안 보존해야 하는가? — 부분 근거: 폐기 표시된 SAP FMS 연동 API 는 UUID 형식 messageId 와 별도의 robotTaskId 로 메시지 식별과 작업 식별을 나누지만, 중복 제거·재시도 보장은 문서에 없다. [추정] 벤더 주장[^ref-1456] 보존 기간 기준은 미확인이다.
- **oq-141** (상태: 열림, 질문 문장은 열린 질문 목록 참고) — 부분 근거: Mission Dispatch MCP 서버의 도구 범위(조회·등록·좌표 이동)는 공개 코드 경로가 기록되지 않아 추정 수준에서만 확인됐다. [추정][^ref-1341] MCP 경유 다사업자 WMS 주문·재고 처리의 운영 결과·권한·실패 복구 시험은 찾지 못했다.
- **oq-365** (상태: 열림, 질문 문장은 열린 질문 목록 참고) — 부분 근거: GreenAuto 개발 대상은 서로 다른 제조사의 AMR 2대·AGV 1대였다. [사실][^ref-136] 최대 20대 동시 감시 서술과의 관계는 미확인이다.
- **oq-002** (상태: 열림) 국내 물류센터에서 SSCC 라벨이나 EPCIS 이벤트를 로봇 작업 결과(적재·하역 완료)와 연결해 운영하는 사례가 있는가? — 이번 실행에서 근거를 찾지 못했다.

### 새로 올린 질문 (2026-10-11, 번호는 열린 질문 목록에서 부여)

- 아르고(테크타카)–플로틱 남이천 물류센터 협력(오더 피킹 로봇 30대 지원 발표) 이후 실증의 시험 기간·성공 기준·완료 결과가 공개됐는가?
- Yu·Srinivas(2025) 동적 주문 피킹 논문 원문의 실험 조건과 서지(권·호·쪽)로 기존 위키의 AOCT·ATT·AWTD 결과 서술을 재검증하면 그대로 맞는가?
- ISA-95 Part 1(ANSI/ISA-95.00.01-2025) 규격 본문에서 바뀐 조항은 무엇이며, OPC UA for ISA-95 Job Control 2.0·B2MML 과의 관계를 바꾸는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/business-system-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/business-system-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/business-system-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-131]: OPC Foundation / ISA, OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4), 2024-01-31, https://reference.opcfoundation.org/specs/OPC-10031-4/6.2, 접근일 2026-10-11
[^ref-1341]: NVIDIA (nvidia-isaac GitHub), isaac_mission_dispatch — README, 미확인, https://github.com/nvidia-isaac/isaac_mission_dispatch, 접근일 2026-10-11
[^ref-136]: Lopes, D., Pereira, T., Gonçalves, A. 외(저자 17명), Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector (Applied Sciences 15(13) 7235), 2025-06-27, https://www.mdpi.com/2076-3417/15/13/7235, 접근일 2026-10-11
[^ref-1453]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/dispatch_task_response.json, 접근일 2026-10-11
[^ref-1454]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/cancel_task_response.json, 접근일 2026-10-11
[^ref-1455]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/simple_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/simple_response.json, 접근일 2026-10-11
[^ref-1456]: SAP, APIs for Integration via Fleet Management Systems (API for Integration with Fleet Management Systems (Deprecated); LATEST URL, 확보본 2024-07-10 기준), 2024-07-10, https://help.sap.com/doc/a02ad3695d5845fca1678810cb83562b/LATEST/en-US/379d6d880e5d4007b3751618080da80f_1.pdf, 접근일 2026-10-11
[^ref-1457]: Oracle, WMS REST API Guide — Change Priority (Oracle Warehouse Management Cloud 26c), 2026-08-14, https://docs.oracle.com/en/cloud/saas/warehouse-management/26c/owmre/change-priority.html, 접근일 2026-10-11
[^ref-1458]: SAP, End-User Information for Integration via Integration Services (SAP Warehouse Robotics, Document Version 2308; LATEST URL, 판 2308 기준), 2023-08-19, https://help.sap.com/doc/f08ea8f8686c46e89f1d7ed121f19d68/LATEST/en-US/b82aa9c86bd74777b86ec7f5766252d0.pdf, 접근일 2026-10-11
[^ref-869]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-02 | 23. 업무 시스템 연동 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-11-02/pages/topics/2026/2026-10-11-area23-s7.md

```markdown
---
title: "23. 업무 시스템 연동 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "F. 연동"
primary_area_no: 23
related_areas: [12, 20, 21, 22, 24, 25, 26, 29, 30, 32, 38, 44, 61, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-129, ref-131, ref-1341, ref-1453, ref-1454, ref-1455, ref-1456, ref-1457, ref-1458, ref-1461, ref-1463]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/business-system-integration.md#7
---

[홈](../../index.md) › [주제](../index.md) › 23. 업무 시스템 연동 — 관련 표준·프레임워크·오픈소스

# 23. 업무 시스템 연동 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 조사에서 확인한 관련 규격은 로봇 쪽 VDA 5050 3.0.0·Open-RMF 작업 API, 상위 쪽 B2MML·OPC UA for ISA-95 Job Control·ISA-95 Part 1, 업무 범위 쪽 SCOR DS 이다. [사실][^ref-031][^ref-129]
- 이 페이지는 [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 조사에서 확인한 관련 규격은 로봇 쪽 VDA 5050 3.0.0·Open-RMF 작업 API, 상위 쪽 B2MML·OPC UA for ISA-95 Job Control·ISA-95 Part 1, 업무 범위 쪽 SCOR DS 이다. [사실][^ref-031][^ref-129] 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 관련 표준·프레임워크·오픈소스 (2026-09-25)](2026-09-25-area01-s7.md) — 그 페이지의 ref-131 '원문 미열람'·'상태 전이는 원문 미열람' 표시는 2026-10-11 원문 확인으로 해제 대상이다.

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

### 2026-10-11 추가 항목

아래 항목은 이번 실행에서 원문으로 확인한 표준·오픈소스와 벤더 자료다. 벤더 API·참조구조는 표준이 아니며, 우선순위·큐 규칙은 연계 대상인 업무 시스템 쪽 동작이다.

| 이름 | 유형 | 이 영역과의 관계(근거) |
|---|---|---|
| OPC UA for ISA-95 Part 4: Job Control (OPC 10031-4) 2.00.0 | 표준 | 2.0 판은 1.0 과 호환되지 않는 변경을 담고 새 namespace 를 정의하며, 갱신은 시작 전 작업 지시에만 적용된다(상태 조건은 4절). [사실][^ref-131] |
| Open-RMF rmf_api_msgs 배정·취소 응답 스키마(dispatch_task_response·cancel_task_response·simple_response) | 오픈소스 | 배정 응답은 성공 시 success·state 필수, 실패 시 errors 배열을 두고, 취소 응답은 simple_response 를 참조해 성패와 오류만 알린다. [사실][^ref-1453][^ref-1454][^ref-1455] |
| SAP Warehouse Robotics FMS 연동 API(폐기 표시) | 벤더 API | SAP BTP 기반 제품(SAP EWM 과 구별)의 FMS 연동 API 로 요청 → 응답 → 콜백 순서와 취소 성공·취소 불가 통지를 정의하지만, 문서가 폐기(Deprecated)로 표시한다(LATEST URL, 확보본 2024-07-10 기준). [추정] 벤더 주장[^ref-1456] |
| SAP Warehouse Robotics integration services 사용자 문서(판 2308) | 벤더 문서 | 최적화를 쓰지 않을 때의 큐 순서와 LSD·생성 시각 정렬 규칙을 설명한다(업무 시스템 쪽 규칙). [추정] 벤더 주장[^ref-1458] |
| Oracle WMS Cloud 26c REST API Change Priority | 벤더 API | Ready·Held·Created 상태 작업만, Task/Change task priority 권한이 있을 때 우선순위를 바꾸게 한다(업무 시스템 쪽 규칙). [추정] 벤더 주장[^ref-1457] |
| NVIDIA Isaac Mission Dispatch | 오픈소스 | README 갱신 표가 2026-03 Mission Dispatch MCP 추가와 2026-08 VDA5050 3.0 지원을 기록한다. [사실][^ref-1341] |
| SAP 참조구조 Warehouse Pick & Place with Embodied AI Robotics | 벤더 참조구조 | 체화 AI 에이전트의 skill 가운데 하나로 업무 객체의 의미 이해를 든다(2026-05-12 갱신). [추정] 벤더 주장[^ref-1461] |
| robotmcp demos-ros-mcp-server 예제 1 | 오픈소스 | ROS-MCP 서버로 시뮬레이션 속 로봇 1대를 자연어로 움직이는 데모이며 업무 시스템 연동은 없다. [사실][^ref-1463] |

채팅 기반 구성·운영 트랙의 반영 제안(실행 2026-09-25-77) 가운데 갱신이 시작 전 작업 지시에만 적용된다는 부분은 이번 원문 확인으로 반영했다. 같은 제안의 Abort 대상 상태 범위와 Pause·Resume 은 원문에서 확인되지 않아 넣지 않았다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/business-system-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/business-system-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/business-system-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-129]: MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd, 접근일 2026-09-25
[^ref-131]: OPC Foundation / ISA, OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4), 2024-01-31, https://reference.opcfoundation.org/specs/OPC-10031-4/6.2, 접근일 2026-10-11
[^ref-1341]: NVIDIA (nvidia-isaac GitHub), isaac_mission_dispatch — README, 미확인, https://github.com/nvidia-isaac/isaac_mission_dispatch, 접근일 2026-10-11
[^ref-1453]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/dispatch_task_response.json, 접근일 2026-10-11
[^ref-1454]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/cancel_task_response.json, 접근일 2026-10-11
[^ref-1455]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/simple_response.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/simple_response.json, 접근일 2026-10-11
[^ref-1456]: SAP, APIs for Integration via Fleet Management Systems (API for Integration with Fleet Management Systems (Deprecated); LATEST URL, 확보본 2024-07-10 기준), 2024-07-10, https://help.sap.com/doc/a02ad3695d5845fca1678810cb83562b/LATEST/en-US/379d6d880e5d4007b3751618080da80f_1.pdf, 접근일 2026-10-11
[^ref-1457]: Oracle, WMS REST API Guide — Change Priority (Oracle Warehouse Management Cloud 26c), 2026-08-14, https://docs.oracle.com/en/cloud/saas/warehouse-management/26c/owmre/change-priority.html, 접근일 2026-10-11
[^ref-1458]: SAP, End-User Information for Integration via Integration Services (SAP Warehouse Robotics, Document Version 2308; LATEST URL, 판 2308 기준), 2023-08-19, https://help.sap.com/doc/f08ea8f8686c46e89f1d7ed121f19d68/LATEST/en-US/b82aa9c86bd74777b86ec7f5766252d0.pdf, 접근일 2026-10-11
[^ref-1461]: SAP Architecture Center, Warehouse Pick & Place with Embodied AI Robotics, 미확인, https://architecture.learning.sap.com/docs/ref-arch/7e4168, 접근일 2026-10-11
[^ref-1463]: robotmcp, demos-ros-mcp-server — Example 1: Tugbot Warehouse Simulation (Ignition Gazebo) README, 미확인, https://github.com/robotmcp/demos-ros-mcp-server/blob/edbc642849bdde1187771a15e557ec9e219184a5/1_Gazebo_Tugbot/README.md, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-02 | 23. 업무 시스템 연동 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-11-02/pages/topics/2026/2026-10-11-area23-s8.md

```markdown
---
title: "23. 업무 시스템 연동 — 대표 연구와 자료"
type: topic
category: "F. 연동"
primary_area_no: 23
related_areas: [12, 20, 21, 22, 24, 25, 26, 29, 30, 32, 38, 44, 61, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-132, ref-133, ref-134, ref-136, ref-1459, ref-869]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/business-system-integration.md#8
---

[홈](../../index.md) › [주제](../index.md) › 23. 업무 시스템 연동 — 대표 연구와 자료

# 23. 업무 시스템 연동 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 조사에서 확인한 자료는 동적 주문 피킹 연구와 웨이브리스 출고 지시 연구, 다제조사 플릿 관리 사례, 국내 WMS–로봇 연동 발표이다. [사실][^ref-132][^ref-134] 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 대표 연구와 자료 (2026-09-25)](2026-09-25-area01-s8.md) — 그 페이지의 GreenAuto(Lopes 외) REST·MQTT 서술은 2026-10-11 정정 대상이며, 정정 내용은 아래 항목에 있다.
- 이 페이지는 [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 조사에서 확인한 자료는 동적 주문 피킹 연구와 웨이브리스 출고 지시 연구, 다제조사 플릿 관리 사례, 국내 WMS–로봇 연동 발표이다. [사실][^ref-132][^ref-134] 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 대표 연구와 자료 (2026-09-25)](2026-09-25-area01-s8.md) — 그 페이지의 GreenAuto(Lopes 외) REST·MQTT 서술은 2026-10-11 정정 대상이며, 정정 내용은 아래 항목에 있다.

### 2026-10-11 보강·정정

이번 실행은 기존 자료 두 건의 서지와 적용 조건을 원문으로 바로잡고, 국내 발표의 1차 출처와 병원 실증 자료를 더했다.

- Lopes, D., Pereira, T., Gonçalves, A. 외(저자 17명), Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency(Applied Sciences, 2025-06-27) — 정정: [2026-09-25 실행의 '대표 연구와 자료' 주제 페이지](2026-09-25-area01-s8.md)가 로봇 이벤트를 MQTT 로 발행한다고 적은 것과 달리, MES·ERP용 REST API 와 AMR 실시간 이벤트·IIoT용 MQTT broker, VDA 5050 연동은 미래 확장 계획(당시 미가동)이며 플릿 관리 시스템과 IIoT 시스템의 통신은 당시 구현에서 아직 활성화되지 않았다. [사실][^ref-136] 개발 대상은 서로 다른 제조사의 AMR 2대·AGV 1대였다. [사실][^ref-136] 이 수치와 [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 페이지의 최대 20대 동시 감시 서술의 관계는 미확인이다(oq-365).
- Lorenz, Otto, & Gendreau, Picking Operations in Warehouses With Dynamically Arriving Orders(Networks, 2025-05) — 적용 조건 보강: §2 의 온라인 주문 묶음·순서·경로 문제(OOBSRP) 모델은 피커 한 명이 맡는 피킹 구역 하나를 다룬다. [사실][^ref-133] 로봇 카트 조건은 피커가 배치를 마치면 빈 로봇을 바로 쓸 수 있다고 가정한다. [사실][^ref-133] §4 계산실험은 개입형 재최적화인 Pcart·Robot 두 시스템만 대상으로 OBSRP\* 인스턴스 2,600개를 만들어 2,380개 이상을 최적으로 풀고 Reopt 결과와 비교했다. [사실][^ref-133] 구축자 의견: 이 결과는 상위 계획 갱신 정책을 비교하는 참고로 두되, 다수 피커·로봇 대기·메시지 멱등성·재고 확정 같은 연동 조건의 검증 근거로 쓰지 않는 것이 맞아 보인다. [의견][^ref-133] 기존 결과 서술은 그대로 둔다.
- 아르고(테크타카), 아르고, 플로틱과 로봇 기반 물류 생산성 향상 실증 본격 실시(2025-01-21) — 남이천 물류센터 실증과 오더 피킹 로봇 30대 지원을 밝힌 업체 발표로, 기존 머니투데이 보도의 1차 출처다(5절). [추정] 업체 발표[^ref-1459]
- Valner 외, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test(Frontiers in Robotics and AI, 2022-08-23) — Tartu 대학병원 현장 시험에서 로봇이 검사실에 도착한 뒤 직원의 화면 버튼 확인과 인제스터의 인수 완료 통지를 거쳐야 ICU 복귀 요청이 나가며, 병원 안 운반은 TIAGo 1대로 했다(5절). [사실][^ref-869]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/business-system-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/business-system-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/business-system-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-132]: Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations, 2025, https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231, 접근일 2026-09-25 (원문 미열람)
[^ref-133]: Lorenz, Otto, & Gendreau (Networks, Wiley), Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization?, 2025-05, https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281, 접근일 2026-10-11
[^ref-134]: Gallien, J., & Weber, T. G., To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter, 2010, https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291, 접근일 2026-09-25 (원문 미열람)
[^ref-136]: Lopes, D., Pereira, T., Gonçalves, A. 외(저자 17명), Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector (Applied Sciences 15(13) 7235), 2025-06-27, https://www.mdpi.com/2076-3417/15/13/7235, 접근일 2026-10-11
[^ref-1459]: 아르고 풀필먼트(테크타카), 아르고, 플로틱과 로봇 기반 물류 생산성 향상 실증 본격 실시, 2025-01-21, https://blog.argoport.com/pr-robotcooperation250121, 접근일 2026-10-11
[^ref-869]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-02 | 23. 업무 시스템 연동 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-11-02/pages/topics/2026/2026-10-11-area23-s10.md

```markdown
---
title: "23. 업무 시스템 연동 — 다른 연구영역과의 연결"
type: topic
category: "F. 연동"
primary_area_no: 23
related_areas: [12, 20, 21, 22, 24, 25, 26, 29, 30, 32, 38, 44, 61, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: []
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/business-system-integration.md#10
---

[홈](../../index.md) › [주제](../index.md) › 23. 업무 시스템 연동 — 다른 연구영역과의 연결

# 23. 업무 시스템 연동 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) — ISA-95 작업 지시와 Open-RMF 작업 상태를 업무 단계와 잇는 문제를 함께 다루며, 같은 출처(작업 상태 스키마, task_new)를 공유한다.
- 이 페이지는 [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) — ISA-95 작업 지시와 Open-RMF 작업 상태를 업무 단계와 잇는 문제를 함께 다루며, 같은 출처(작업 상태 스키마, task_new)를 공유한다.
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — VDA 5050 주문 갱신·취소와 Open-RMF 작업 요청은 제조사 관제와의 인터페이스 자체다.
- [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md) — 새 주문 거부(OTHER_ORDER_ACTIVE)와 취소·중단·되감기 요청의 처리 결과 확인이 실행 신뢰성과 이어진다.
- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 가장 적합한 플릿에 작업을 맡기는 요청 방식과 AMR 가용성에 따른 개입 전략이 배정 문제와 겹친다.
- [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) — 출고 우선순위 변경에 따른 대기열 재정렬과 동적 재최적화가 순서 결정 문제다. WMS 쪽 대기 큐 정렬 규칙(LSD·생성 시각)과 Lorenz 외 재최적화 연구의 적용 조건(단일 피커·단일 구역)도 이 영역과 함께 본다.
- [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 적재 후 취소의 되돌림 작업과 취소 불가 동작 처리가 복구·재계획 과제다.
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — ISA-95 계열과 로봇 인터페이스 사이 표준 매핑이 확인되지 않은 점이 상호운용성 과제다.
- [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) — 모델 컨텍스트 프로토콜(Model Context Protocol, MCP) 같은 대화형 접점이 실제로 노출하는 도구 범위와 업무 요구(승인·취소·결과 대조)의 차이를 함께 다룬다. 짝이 되는 엔진은 25. 작업 배정 — MRTA와 26. 작업 순서·스케줄링이다.
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 제조 공장 사례의 WCS·SCADA 설비 제어는 그 영역의 연계 대상이다.
- [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md) — 병원 사례의 인제스터 인수 확인처럼 도착과 인수를 나누는 인계 단계가 업무 완료 판단과 이어진다.
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) — 제조 공장 사례의 SCADA 기반 통합 관제는 관제 쪽에서 다룬다.
- [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) — 업무 객체 문맥을 받아 작업하는 체화 AI·휴머노이드의 작업 수행은 그 영역의 내용이며, 이 영역은 업무 객체 해석 계층만 다룬다.
- [61. 물류창고](../../categories/site-type-applications/warehouse.md) — 아르고–플로틱 실증 발표와 Bosch·Aimbo 개념검증이 물류창고 현장의 업무 시스템 연동 사례다.
- [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md) — HD현대일렉트릭 신공장의 생산 물류 조율 사례다.
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — Tartu 대학병원 시료 운반의 인수 확인 절차가 병원 현장의 완료·인계 사례다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/business-system-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/business-system-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/business-system-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-02 | 23. 업무 시스템 연동 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-10-11-02/pages/topics/2026/2026-10-11-area23-s4.md

```markdown
---
title: "23. 업무 시스템 연동 — 핵심 개념과 용어"
type: topic
category: "F. 연동"
primary_area_no: 23
related_areas: [12, 20, 21, 22, 24, 25, 26, 29, 30, 32, 38, 44, 61, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-131]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/business-system-integration.md#4
---

[홈](../../index.md) › [주제](../index.md) › 23. 업무 시스템 연동 — 핵심 개념과 용어

# 23. 업무 시스템 연동 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역을 읽는 데 필요한 용어는 로봇 쪽의 주문·작업 표현과 상위 시스템 쪽의 작업 지시 표현으로 나뉜다. 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 핵심 개념과 용어 (2026-09-25)](2026-09-25-area01-s4.md) — 그 페이지의 ref-131 '원문 미열람'·'상태 전이는 원문 미열람' 표시는 2026-10-11 원문 확인으로 해제 대상이며, 확인 내용은 아래 소절에 있다.
- 이 페이지는 [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역을 읽는 데 필요한 용어는 로봇 쪽의 주문·작업 표현과 상위 시스템 쪽의 작업 지시 표현으로 나뉜다. 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 핵심 개념과 용어 (2026-09-25)](2026-09-25-area01-s4.md) — 그 페이지의 ref-131 '원문 미열람'·'상태 전이는 원문 미열람' 표시는 2026-10-11 원문 확인으로 해제 대상이며, 확인 내용은 아래 소절에 있다.

업무 시스템 약어는 [WES·WCS·WMS·MES·TMS](../../glossary/wes-wcs-wms-mes-tms.md)를 참고한다.

### OPC UA for ISA-95 Job Control 2.00.0 의 갱신·취소·종료 조건 (2026-10-11 원문 확인)

이번 실행에서 OPC 10031-4 명세 원문(§1, §6.2.1, §6.2.4)을 열어, [2026-09-25 실행의 '핵심 개념과 용어' 주제 페이지](2026-09-25-area01-s4.md)가 메서드 이름만 적었던 작업 지시(job order) 변경 수단의 상태 조건을 확인했다. 이 확인으로 그 페이지와 [2026-09-25 실행의 '관련 표준·프레임워크·오픈소스' 주제 페이지](2026-09-25-area01-s7.md)의 ref-131 '원문 미열람'·'상태 전이는 원문 미열람' 표시는 해제 대상이다.

- **갱신(Update)** — 아직 시작하지 않은 작업 지시만 새 지시 정보로 갱신하며, 이전에 저장된 정보는 모두 교체된다. [사실][^ref-131]
- **취소(Cancel)** — 시작 전 상태(AllowedToStart·NotAllowedToStart)의 작업 지시를 취소하고 저장된 정보를 지운다. 성공하면 작업 지시 목록(JobOrderList)에 그 작업 지시 id 가 남지 않아야 한다. [사실][^ref-131]
- **정지(Stop)** — 이미 시작된 작업 지시를 멈추며, 성공하면 작업 지시는 Ended 상태가 된다. Abort 가 작업 지시를 Aborted 상태로 바꾸는 것과 구별된다. [사실][^ref-131]
- **완료(Completed)·종결(Closed)** — 둘 다 Ended 의 하위 상태로, Completed 는 실행이 끝난 상태이고 Closed 는 완료 뒤 후처리도 더 하지 않는 상태다. [사실][^ref-131]
- **2.0 판의 비호환** — Job Control 2.0 은 1.0 과 호환되지 않는 변경을 담고 새 namespace 를 정의해, 이전 응용이 필요하면 두 모델을 함께 지원할 수 있게 한다. [사실][^ref-131]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/business-system-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/business-system-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/business-system-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-131]: OPC Foundation / ISA, OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4), 2024-01-31, https://reference.opcfoundation.org/specs/OPC-10031-4/6.2, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-02 | 23. 업무 시스템 연동 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-10-11-02/pages/topics/2026/2026-10-11-area23-s3.md

```markdown
---
title: "23. 업무 시스템 연동 — 왜 중요한가"
type: topic
category: "F. 연동"
primary_area_no: 23
related_areas: [12, 20, 21, 22, 24, 25, 26, 29, 30, 32, 38, 44, 61, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-136]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/business-system-integration.md#3
---

[홈](../../index.md) › [주제](../index.md) › 23. 업무 시스템 연동 — 왜 중요한가

# 23. 업무 시스템 연동 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇 관제 인터페이스 표준인 VDA 5050 3.0.0은 관제(fleet control)와 이동로봇 사이의 통신만 다루고, 외부 IT 시스템 같은 다른 인터페이스와 교통 관리 로직은 범위 밖에 둔다(2026-09-25 확인). [사실][^ref-031] 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 왜 중요한가 (2026-09-25)](2026-09-25-area01-s3.md) — 그 페이지의 GreenAuto(Lopes 외) REST·MQTT 서술은 2026-10-11 정정 대상이며, 정정 내용은 아래 소절에 있다.
- 이 페이지는 [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇 관제 인터페이스 표준인 VDA 5050 3.0.0은 관제(fleet control)와 이동로봇 사이의 통신만 다루고, 외부 IT 시스템 같은 다른 인터페이스와 교통 관리 로직은 범위 밖에 둔다(2026-09-25 확인). [사실][^ref-031] 2026-09-25 실행까지의 내용: [23. 업무 시스템 연동 — 왜 중요한가 (2026-09-25)](2026-09-25-area01-s3.md) — 그 페이지의 GreenAuto(Lopes 외) REST·MQTT 서술은 2026-10-11 정정 대상이며, 정정 내용은 아래 소절에 있다.

그래서 ERP·WMS·MES 같은 상위 시스템의 주문과 변경을 로봇 작업으로 옮기는 일은 로봇 표준이 대신해 주지 않는다.

### 2026-10-11 정정: 다제조사 플릿 사례의 업무 시스템 연동은 계획 단계였다

[2026-09-25 실행의 '왜 중요한가' 주제 페이지](2026-09-25-area01-s3.md)에 있는 '확인한 연동 사례는 자체 REST·MQTT 인터페이스를 썼다'는 문장은 근거 논문과 다르므로 다음처럼 고친다. Lopes 외(2025)는 MES·ERP 에 로봇 위치·상태·이벤트를 내주는 REST API, AMR 실시간 이벤트·IIoT 용 MQTT broker, VDA 5050 연동을 모두 미래 확장으로 설계했고(당시 미가동), 플릿 관리 시스템과 IIoT 시스템의 통신은 당시 구현에서 아직 활성화되지 않았다고 밝힌다. [사실][^ref-136] 곧 서로 다른 제조사의 로봇을 한데 관리한 이 사례에서도 업무 시스템과의 연동은 구현이 아니라 계획으로 남아 있었다. [사실][^ref-136]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/business-system-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/business-system-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/business-system-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-136]: Lopes, D., Pereira, T., Gonçalves, A. 외(저자 17명), Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector (Applied Sciences 15(13) 7235), 2025-06-27, https://www.mdpi.com/2076-3417/15/13/7235, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-02 | 23. 업무 시스템 연동 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 19건 / 전체 1443건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-002 | ISA | Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems | 2025 | https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of | 2026-09-24 | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/task_new.html | 2026-09-25 | 예 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 2026-09-25 | 예 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 2026-09-25 | 예 |
| ref-126 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_request.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/cancel_task_request.json | 2026-09-25 | 예 |
| ref-127 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/interrupt_task_request.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/interrupt_task_request.json | 2026-09-25 | 예 |
| ref-128 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/rewind_task_request.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/rewind_task_request.json | 2026-09-25 | 예 |
| ref-129 | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 2023 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd | 2026-09-25 | 예 |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 2024-01-31 | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL | 2026-09-25 | 아니오 |
| ref-131 | OPC Foundation / ISA | OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4) | 미확인 | https://reference.opcfoundation.org/specs/OPC-10031-4/6.2 | 2026-09-25 | 아니오 |
| ref-132 | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 2025 | https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231 | 2026-09-25 | 아니오 |
| ref-133 | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 2025 | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 | 2026-09-25 | 아니오 |
| ref-134 | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 2010 | https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291 | 2026-09-25 | 아니오 |
| ref-135 | ASCM | SCOR Digital Standard — Introduction and Front Matter (SCOR Version 14.0, 2025) | 2025 | https://www.ascm.org/globalassets/ascm_website_assets/docs/scor/intro-and-front-matter-scor-digital-standard-2025.pdf | 2026-09-25 | 아니오 |
| ref-136 | Applied Sciences(MDPI) 게재 논문 저자(미확인) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 2025 | https://www.mdpi.com/2076-3417/15/13/7235 | 2026-09-25 | 아니오 |
| ref-137 | 머니투데이 | 물류센터 관리시스템에 로봇 연동…"물류 자동화 새 표준 만든다" | 2025-01 | https://news.mt.co.kr/mtview.php?no=2025012116183583251 | 2026-09-25 | 아니오 |
| ref-138 | 국가표준인증통합정보시스템(KSSN) | KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 미확인 | https://www.kssn.net/search/stddetail.do?itemNo=K001010147546 | 2026-09-25 | 아니오 |
| ref-182 | ECLASS e.V. | Neuer Content für ECLASS Release 15.0 | 미확인 | https://eclass.eu/aktuelles/news/neuer-content-fuer-eclass-release-150 | 2026-09-25 | 아니오 |
```

### docs/glossary/index.md (요약: 용어 399개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- makespan: 메이크스팬 (Makespan)
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
- minimum-cost-flow: 최소 비용 흐름 (Minimum-Cost Flow)
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
- satisfiability-modulo-theories: 이론 모듈로 만족 가능성 (Satisfiability Modulo Theories (SMT))
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

### docs/open-questions.md (요약: 대상 영역 [23] 에 걸린 17건 / 전체 377건)

```markdown
- oq-002 [열림] 국내 물류센터에서 SSCC 라벨이나 EPCIS 이벤트를 로봇 작업 결과(적재·하역 완료)와 연결해 운영하는 사례가 있는가? (영역 17, 23)
- oq-012 [열림] 국내 물류센터는 로봇의 운반 완료와 WMS의 입고·인수 확정을 별도 단계로 두는가, 그렇다면 두 단계를 잇는 식별 키와 확정 대기 시간 기준은 무엇인가? (영역 23, 24)
- oq-015 [열림] 로봇 상태 기록(작업 중·유휴·충전·오류)과 WMS·ERP의 주문 이행 지표(완전 주문 이행률, 주문 이행 사이클 타임)를 같은 기간·같은 주문 단위로 연결해 로봇 도입이 출하량·비용 개선으로 이어졌는지 검증한 공개 사례가 있는가? (영역 23, 39)
- oq-019 [열림] 상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가? (영역 23, 26)
- oq-020 [열림] ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? (영역 20, 21, 23)
- oq-021 [열림] 로봇이 이미 화물을 싣거나 옮긴 뒤 상위 시스템이 주문을 취소·변경하면 되돌림 작업과 재고 반영을 누가 어떤 규칙으로 정하는가(국내 물류센터 사례 포함)? (영역 23, 32)
- oq-038 [열림] 외부망이 끊겨 클라우드 WMS 와 단절된 동안 현장 ROP 가 이미 받은 주문·작업을 어디까지 계속 실행하고, 재연결 뒤 재고·완료 기록을 어떻게 맞추는지 정한 국내 물류센터 운영 기준이나 사례가 있는가? (영역 23, 32, 42)
- oq-046 [열림] 상위 시스템 요청의 중복을 판별하는 키(멱등성 키나 상위 요청 id)를 ROP 가 얼마 동안 보존해야 하는가, 운반 작업의 재전송 가능 기간에 맞춘 만료 기준을 정한 표준이나 사례가 있는가? (영역 23, 29)
- oq-054 [열림] 출하 마감·납기 같은 상위 업무 제약을 배정 목적함수(완료 시각 최소화, 비용 최소화)와 어떻게 결합하는지 정한 공개 설계나 창고 사례가 있는가? (관련 기존 질문: oq-019) (영역 23, 25, 26)
- oq-114 [열림] 로봇 관제가 배정 실패(수행 가능한 로봇·플릿 없음)를 WMS 등 상위 업무 시스템에 어떤 필드로 되돌리고, 상위 시스템이 이를 사람 작업 지시로 전환하는 표준이나 국내 물류센터 사례가 있는가? (영역 23, 25)
- oq-164 [열림] 스마트물류센터 인증 심사기준의 정보시스템 항목(WMS 150점, WCS/MCS 50점)에서 이기종 로봇 오케스트레이션 계층은 어느 항목으로 평가되며 인증 심사가 로봇 플릿 관제 기능을 따로 보는가? (영역 61, 23)
- oq-168 [열림] 생산 관리 시스템(MES)이 로봇 플릿에 내는 운송·공정 작업 요청과 완료 보고에 ISA-95 의 작업 요청·작업 응답 모델을 실제로 쓴 공개 사례나 표준 매핑이 있는가? (영역 62, 23)
- oq-177 [열림] 호텔 객실 배송 로봇이 객실 관리 시스템(PMS)이나 객실 전화에서 요청을 받고 배송 완료를 되돌려 주는 표준 인터페이스나 공개된 연동 구조가 있는가? (영역 64, 23)
- oq-184 [열림] 공동주택 배송로봇의 수령 확인(주문자만 꺼낼 수 있는 방식)은 어떤 인증 수단(비밀번호·앱·QR)으로 이루어지며, 그 결과가 배달 앱·택배사 시스템에 완료 이벤트로 어떻게 돌아가는가? (영역 65, 17, 23)
- oq-194 [열림] 플랜트·변전소 점검 로봇이 얻은 계기값·열화상·이상 판정은 설비 보전 시스템의 작업 지시·점검 기록으로 어떤 형식과 승인 절차를 거쳐 돌아가는가? (영역 67, 23, 38)
- oq-223 [열림] 46. 예측·학습 기반 최적화의 수요 예측(작업 요청·물동량 예측)과 분류 원문 19장이 외부 연계로 둔 수요예측(상위 업무 시스템)의 경계를 어떻게 나눌 것인가? (영역 46, 23)
- oq-296 [열림] 전자의무기록 주문이 로봇 작업 요청을 자동으로 만드는 병원 연동에서 주문 취소·변경을 진행 중인 로봇 작업에 반영하고 결과를 기록에 되돌린 공개 사례가 있는가? (영역 40, 23, 63)
```

### runs/2026-10-11-02/verification2.json

```json
{
  "run_id": "2026-10-11-02",
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
      "3·4·6·7·8·11절: 자동 분리 뒤 세부영역 페이지의 '자세한 내용은 주제 페이지 …' 줄이 2026-09-25 주제 페이지(2026-09-25-area01-s3·s4·s6·s7·s8·s11)에서 새 주제 페이지(2026-10-11-area23-s3·s4·s6·s7·s8·s11)로 바뀌었다. 옮긴 절 본문에도 옛 링크가 없다. 그래서 검증을 거친 기존 상세 내용(VDA 5050 변경 수단, Open-RMF 중단·되감기, OPC 메서드 목록, 8절 자료 목록 등)이 세부영역 페이지에서 끊긴다. 같은 제목('23. 업무 시스템 연동 — 왜 중요한가' 등)의 주제 페이지가 두 개씩 생긴다.",
      "2026-09-25-area01-s3 39행과 2026-09-25-area01-s8 42행의 GreenAuto(ref-136) 서술은 이번 정정(f19~f22)과 충돌하는 채로 게시돼 있다. 새 주제 페이지 s3·s8 은 그 페이지를 '연결된 주제 페이지'라고만 부르고 링크하지 않는다. 그래서 독자는 정정 대상 문장과 정정 문장을 함께 볼 수 없다."
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "3·4·6·7·8·11절 패치(append·replace content): 각 절에 대응하는 2026-09-25 주제 페이지로 가는 링크 줄을 하나씩 다시 넣는다. 대상은 ../../topics/2026/2026-09-25-area01-s3.md · -s4.md · -s6.md · -s7.md · -s8.md · -s11.md 이다. 자동 분리가 '자세한 내용은 주제 페이지 …' 줄을 새 링크로 바꾸므로 그 문구는 쓰지 말고 다른 문구로 쓴다(예: '2026-09-25 실행까지의 내용: [제목](경로)'). 이유: 지금 산출물은 검증·게시된 기존 상세 내용을 세부영역 페이지에서 끊어 버린다. 자동 분리 주제 페이지가 원 절 내용을 그대로 옮기지 않았다(옛 링크 줄 누락).",
    "3·8절 패치: 위에서 다시 넣는 2026-09-25-area01-s3.md·-s8.md 링크 줄에, 그 페이지의 GreenAuto(Lopes 외) REST·MQTT 서술이 2026-10-11 정정 대상이라는 안내를 같은 줄에 붙인다. 4절도 같은 방식으로 2026-09-25-area01-s4.md 링크 줄에 ref-131 '원문 미열람' 표시가 해제 대상이라는 안내를 붙인다. 새 내용(정정 소절·4절 확인 소절·8절 정정 항목)에서 '연결된 주제 페이지'라고만 쓴 곳은 해당 2026-09-25 주제 페이지로 가는 링크로 바꾼다. 이유: 1차 수정 지시(f19~f22 정정)를 주제 페이지 본문에 직접 반영하지 못했다(부분 이행). 그러니 정정 대상 문장과 정정 문장을 독자가 서로 찾아갈 수 있어야 한다.",
    "9절 패치: 이 페이지 본문에서 MCP 가 처음 나오는 곳('대화형 접점(MCP)')을 '모델 컨텍스트 프로토콜(Model Context Protocol, MCP)'로 풀어 쓰고 용어집(../../glossary/model-context-protocol.md)을 링크한다. 같은 문단의 '6절에 적었다'는 2026-10-11-area23-s6.md 링크로 바꾼다. 이유: 약어는 첫 등장에서 풀어 써야 하는데, 6절 본문이 주제 페이지로 옮겨져 세부영역 페이지에서는 9절이 첫 등장이 됐다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 36건, 미확인 2건, 교차 확인 0건. 강등: f33 사실 → 추정, f34 사실 → 추정. 등록 출처 ref-1341 은 README 이고 MCP 코드 파일 경로가 기록되지 않아 검증에서 재확인하지 못했다. 원문 미열람 출처: 없음. 다만 검증 쪽에서 본문을 다시 대조하지 못한 출처가 있다. ref-136 은 Crossref 서지와 초록까지만, ref-1456·ref-1458 은 실재만 확인했다. ref-133 은 같은 논문의 arXiv 판으로 확인했다. 주의: OPC UA for ISA-95 Job Control 2.00.0 의 상태 조건과 Open-RMF 응답 스키마는 단일 출처다. SAP Warehouse Robotics·Oracle WMS·LG CNS·SAP 참조구조·Bosch–Aimbo 사례는 벤더 주장이고, SAP FMS API 는 폐기 표시 문서다. GreenAuto 의 REST·MQTT·VDA 5050 연동은 계획(미가동)으로 정정했다. Tartu 병원 실증은 병원 안에서 로봇 1대로 했다. 트랙 반영 제안 3은 Update 시작 전 조건만 반영했고, 제안 1·2는 다음 실행으로 넘긴다. 열린 질문 해결 인정 없음. 정정 요청 없음. / 2차 수정 후 재검증. 드리프트 없음. 1차 수정 지시 19건 이행을 확인했고, f19~f22 의 2026-09-25 주제 페이지 본문 정정만 입력 부재로 부분 이행이다. [분류원문] 보존, 섹션 순서 준수, 링크 대상은 유효하다. 다만 자동 분리가 기존 2026-09-25 주제 페이지 여섯 개로 가는 링크를 없애 기존 상세 내용과 정정 대상 문장이 세부영역 페이지에서 끊겼다. 링크 복원과 MCP 첫 등장 풀어쓰기를 지시했다. 운영 요청 세 가지: (1) pipeline 담당은 자동 분리 코드가 기존 '자세한 내용은 주제 페이지' 링크를 지우지 않게 고친다. (2) 같은 절의 주제 페이지가 이미 있으면 새 주제 페이지 제목을 구별되게 붙인다(예: 날짜 병기). (3) 다음 23. 업무 시스템 연동 갱신 실행에서 2026-09-25-area01-s3·s4·s7·s8 을 입력에 넣어 GreenAuto 서술과 ref-131·ref-136 각주를 직접 고친다.",
  "retry_reason": null
}
```
