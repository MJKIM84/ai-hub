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
- 세부영역 반영 제안: 3건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
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

### data/area_reflection_proposals.json (대상 영역 23. 업무 시스템 연동 에 대한 트랙 반영 제안 3건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-09-25-37",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 2,
      "area_no": 23,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "OPC UA for ISA-95 작업 제어 노드셋(2024-01-31)의 작업 지시는 작업 지시 id 만 필수이고 종료 시각·우선순위·자재 요구가 선택 필드여서, 채팅 지시의 기한·대상 화물 원천 후보가 된다(f7). 로봇 인터페이스에는 기한 필드가 없어 작업 모델이 기한을 보유해야 한다는 추론(f15, [추정], oq-019 연결).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-37",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 2,
      "area_no": 23,
      "section": "6. 대표 접근법과 기술",
      "summary": "상위 업무 시스템(WMS) 쪽 제품 사례: Mecalux Easy WMS 의 대화형 비서가 긴급 주문 출고·통로 잠금 해제를 채팅 요청으로 실행하되 실행 전 요약·확인을 받는다([추정] 벤더 주장, f13). ROP 기능이 아니라 연계 대상의 사례로만 서술.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-77",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 3,
      "area_no": 23,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "OPC UA for ISA-95 Part 4 작업 제어는 작업 지시를 실행 전 상태에서만 Update 로 바꾸고 실행 중·중단·미시작 작업 지시는 Abort 로 Aborted 상태로 보낸다(원문 미열람, ref-681, Pause·Resume 은 재확인 못함). 지시 변경 반영 규칙의 업무 시스템 쪽 기준.",
      "status": "제안"
    }
  ]
}
```

### docs/categories/integration/robot-and-vendor-fleet-manager-integration.md (요약)

```markdown
# 20. 로봇·제조사 관제 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

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

### docs/categories/integration/interoperability-standards-and-conformance.md (요약)

```markdown
# 21. 상호운용 표준·적합성

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-11 · 버전: 3

## 1. 한 줄 정의

로봇 상호운용 표준을 채택·변환하고 적합성을 시험한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상호운용 표준 채택**: VDA 5050·MassRobotics 상호운용 표준·Open-RMF·ROS 2·OPC UA 같은 표준을 채택하고 서로 변환한다
- **적합성 시험**: 표준과 연동 규격을 지키는지 시험한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 28번 영역 ‘표준·상호운용성·다사업자 거버넌스’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [옛 분류원문]

> 옛 질문: 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [옛 분류원문]

## 2. 핵심 질문

어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]
```

### docs/categories/integration/facility-and-building-system-integration.md (요약)

```markdown
# 22. 설비·건물 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

문·승강기·출입통제·컨베이어·PLC·고정 센서와 작업을 연계한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **설비·건물 연동**: 문·승강기·출입통제·컨베이어·자동창고·PLC·빌딩 관리 시스템과 작업을 연계한다
- **승강기·문 예약과 연동**: 승강기와 문을 예약하고 로봇의 진입과 설비 상태를 맞물려 확인한다
- **로봇–설비 작업 동기화**: 컨베이어·작업대 준비와 로봇 도착처럼 설비와 로봇의 시점을 맞춘다
- **IoT·고정 센서 연동**: 고정 카메라·출입 센서·환경 센서처럼 로봇 밖의 센서 데이터를 연결한다

이전 분류(2026-09-24)에서 이 페이지는 옛 10번 영역 ‘설비·건물 시스템 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 [옛 분류원문]

> 옛 질문: 컨베이어 준비와 로봇 도착을 어떻게 맞출까? [옛 분류원문]

## 2. 핵심 질문

문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/planning-and-optimization/task-and-workflow-modeling.md (요약)

```markdown
# 24. 작업·워크플로 모델링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

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
```

### docs/categories/planning-and-optimization/task-allocation-mrta.md (요약)

```markdown
# 25. 작업 배정 — MRTA

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

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

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

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

### docs/categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md (요약)

```markdown
# 32. 예외 복구·재계획·업무 연속성

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

고장·통신 단절·누락에 대한 복구와 제한 운영 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **예외 복구**: 고장·통신 단절·물품 누락·긴급 요청에 재배정·우회·수동 처리·제한 운영을 결정한다
- **제한 운영·업무 연속성**: 일부 장비가 멈춰도 업무를 이어 가는 운영 수준과 절차를 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 20번 영역 ‘예외 복구·재계획·업무 연속성’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 [옛 분류원문]

> 옛 질문: 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? [옛 분류원문]

## 2. 핵심 질문

작업 중 로봇이 고장 나면 남은 일은 누가 어떻게 이어받는가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 19건 / 전체 1430건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/open-questions.md (요약: 대상 영역 [23] 에 걸린 17건 / 전체 371건)

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

### runs/2026-10-11-01/research.md

```markdown
# 리서치 브리프 2026-10-11-01

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-11-01 |
| 날짜 | 2026-10-11 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 21. 상호운용 표준·적합성 |
| 대분류 | F. 연동 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 수행 자원 칸이 'VDA 5050 3.0.0 에서 주문 배정·경로 계산…은 관제 쪽'으로 경로 계산을 모든 로봇에 일반화함(원문은 선 유도 로봇). 물류창고 외 현장 유형 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — '제조사가 자체 인증하거나' 문장의 근거 없음(정정 필요). 선택 필드·재전송·취소 후 갱신을 확인하는 동작 시험 방법 없음. OTTO 인증 발표 각주가 원문 미열람
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — VDA 5050 행 발행일 표기, MassRobotics 행 '원문 미열람', OPC 행 '자체·독립 시험소 인증' 표현. 3.0.0 태그 스키마 끝 쉼표, OPC UA Robotics 서버 Facet, KS B ISO 22166-202 미반영. 트랙 반영 제안(2026-10-09-26, 건축 도면 자동 인식 단계 2: IDS 1.0 을 BIM 데이터 교환 요구·적합성 검사 수단으로) 미처리
- 섹션 8. 대표 연구와 자료 — vda5050-lab 원문 미열람 표시, VDA 5050 통신 평가 논문 없음
- 섹션 10. 다른 연구영역과의 연결 — 42. 분산 시스템·통신·컴퓨팅 구조, 14. 도면·BIM에서 지도 만들기 연결 없음
- 섹션 11. 열린 질문 — oq-005·oq-055·oq-091·oq-026 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]
2. oq-005 VDA 5050 3.0.0 의 날짜는 공식 저장소 명세·카탈로그·보도자료·참여 업체 발표에서 각각 무엇으로 표시되는가? (섹션 7·11 겨냥)
3. oq-055 VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 도구·벤더 간 인증·전시 시연·인정 시험소 인증을 연동 승인 근거로 어떻게 구분해 쓸 수 있는가? (섹션 6·8·11 겨냥)
4. oq-091 VDA 5050 3.0.0 태그의 JSON 스키마를 시험 입력으로 그대로 쓸 수 있는가? (섹션 7·11 겨냥)
5. oq-026 KS B 7321-2 와 KS B ISO 22166-202 는 국가표준 목록에서 무엇으로 확인되는가? TTAK.KO-10.1295-Part8 은 공식 목록에서 확인되는가? (섹션 7·11 겨냥, 한국 자료 우선)
6. 트랙 반영 제안 2026-10-09-26: IDS 1.0(buildingSMART)의 적용 대상·요구 구조·패싯·값 제한은 발행 기관 자료로 무엇이며, 21. 상호운용 표준·적합성의 적합성 검사 수단으로 볼 수 있는가? (섹션 7·10 겨냥)
7. 기존 문장 점검: VDA 5050 3.0.0 은 경로 계산을 어느 로봇에 대해 관제 책임으로 두는가, OPC Foundation 은 제조사 자체 인증을 허용하는가? (섹션 5·6·7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA5050 공식 저장소의 3.0.0 명세 마크다운 표지는 판을 'Version 3.0.0'으로만 적고 날짜를 적지 않으며, VDA 가 배포하는 PDF 표지의 날짜 표기는 이번 실행에서 PDF 본문 텍스트를 읽지 못해 확인하지 못했다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f2 | [의견] | 구축자 의견: 21번 7절 표 VDA 5050 행의 발행일은 단일 날짜로 확정하지 않고 '미확인'을 유지하되, VDA 카탈로그 표시일(2026-03-17)과 보도자료 날짜(2026-04-20)가 서로 다르다는 점은 20번 주제 페이지의 날짜 절로 연결하고, PDF 표지의 'March 2026' 표기는 원문 확인 전까지 [추정]으로 두는 것이 맞다. | ref-1412, ref-032, ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f3 | [사실] | VDA 5050 3.0.0 §5.3 의 관제 기능 목록은 경로 계산을 일반 기능이 아니라 선 유도(line-guided) 이동로봇의 경로 계산·안내로 적고, §5.4 는 이동로봇 기능을 선 유도형과 자유 주행형(freely navigating)의 경로 실행으로 나눠 서술한다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f4 | [사실] | VDA 의 3.0 발표 보도자료는 자율도가 높은 이동로봇이 지정된 경유점 사이 경로를 스스로 계획해 상세 경로 계획이 로봇에서 이뤄지고, 그 경로를 경로 공유(path sharing)로 중앙 관제와 공유하는 구성을 설명한다. | ref-032 | 아니오 | medium | 2026-04-20 | — | — |
| f5 | [의견] | 구축자 의견: 21번 본문 5절 수행 자원 칸과 분리 7절 본문의 '주문 배정·경로 계산·…은 관제 쪽' 문장은 '선 유도 로봇의 경로 계산·안내'로 고치고, 자유 주행 로봇은 상세 경로를 스스로 계획해 공유할 수 있음을 병기해 모든 이동로봇의 상세 경로를 관제가 계산한다고 일반화하지 않는 것이 맞다. | ref-031, ref-032 | 아니오 | medium | 2026-10-11 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 §7.1.1 은 로봇이 받은 선택(optional) 필드를 무시해서는 안 되고 쓸 수 없으면 UNSUPPORTED_PARAMETER(CRITICAL)로 알리게 하며, 관제(fleet control)에는 로봇이 지원하는 선택 필드만 보내도록 의무를 둔다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f7 | [사실] | VDA 5050 3.0.0 은 연동 시험의 기대값으로 쓸 응답을 조항으로 정한다: 지원하지 않는 선택 파라미터가 든 주문은 UNSUPPORTED_PARAMETER(CRITICAL)로 거절, 같은 orderUpdateId 재전송은 내용이 같으면 무시하고 다르면 SAME_ORDER_UPDATE_ID(WARNING)를 보고하며 이전 주문을 계속, 취소된 주문의 후속 갱신은 ORDER_UPDATE_FOLLOWING_CANCEL(WARNING). | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f8 | [의견] | 구축자 의견: 로봇 연동 승인에는 버전 문자열 확인에 더해 (1) 미지원 선택 필드 주문 거절, (2) 같은 번호·같은 내용 재전송 무시, (3) 같은 번호·다른 내용 재전송 경고, (4) 취소 후 갱신 경고, (5) 관제가 로봇 factsheet 가 지원한다고 밝힌 선택 필드만 보내는지를 확인하는 동작 시험표를 두고, 수신 직전 주문 상태와 관측 로그 누락 여부를 함께 보존하는 것이 좋다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f9 | [사실] | VDA5050 공식 저장소 3.0.0 태그의 json_schemas/order.schema·factsheet.schema·visualization.schema 에는 닫는 괄호 바로 앞에 쉼표가 오는 끝 쉼표(trailing comma)가 있어 엄격한 JSON 으로 읽히지 않으며, main 브랜치의 order.schema 는 같은 자리(궤적 제어점 weight 속성)에 끝 쉼표가 없다. | ref-1430, ref-1431, ref-1432, ref-413 | 아니오 | medium | 2026-10-11 | — | — |
| f12 | [의견] | 구축자 의견: VDA 5050 3.0.0 을 시험 입력으로 쓸 때는 '공식 태그'와 '파싱 가능한 시험 입력'을 따로 확인하고, 수정한 스키마를 쓰면 원본과의 차이·수정 근거·해시를 보존하며 main 브랜치 내용을 설명 없이 섞지 않는 것이 좋다. | ref-1430, ref-413 | 아니오 | medium | 2026-10-11 | — | — |
| f13 | [사실] | vda5050-lab README(커밋 4a1a812)는 현재 판 v0.2.0 을 개발자 프리뷰(Developer Preview)로 부르며 오프라인 진단 구현과 범위가 제한된 합성 시연을 담는다고 설명하고, 공개 알파나 인증 주장이 아니며 실제 고객 기록·외부 시험 대상(DUT)·실물 하드웨어 실행을 검증하지 않았다고 밝힌다. | ref-408 | 아니오 | medium | 2026-10-11 | — | — |
| f14 | [의견] | 구축자 의견: vda5050-lab 은 MQTT 기록 진단의 보조 도구 후보로만 두고, 그 판정을 구매·연동 승인 전체의 대체물로 쓰지 않는 것이 맞다. | ref-408 | 아니오 | medium | 2026-10-11 | — | — |
| f15 | [사실] | OPC Foundation 'How to Certify' 는 제조사가 인증 시험 전에 가능한 많은 시험을 미리 해 보도록 권고하고, 재단이 제공하는 적합성 시험 도구(compliance test tools)는 시험소가 시험에 쓰는 도구라고 설명한다. | ref-705 | 아니오 | medium | 2026-10-11 | — | — |
| f16 | [사실] | OPC Foundation 인증 개요 페이지는 인증 제품이 재단이 인정한 인증 시험소에서 시험을 거쳤다고 설명하고, 인증된 SDK 를 쓴 응용도 공식 인증 제품이 되려면 각자 인증 시험을 받아야 한다고 밝힌다. | ref-1434 | 아니오 | medium | 2026-10-11 | — | — |
| f17 | [사실] | 확인한 OPC Foundation 인증 안내 두 페이지에는 제조사가 스스로 인증하는(self-certification) 경로가 없으므로, 21번 분리 6절의 '제조사가 자체 인증하거나'와 분리 7절 표 OPC 행의 '자체·독립 시험소 인증'은 이 두 출처로 뒷받침되지 않는 표현이다. | ref-705, ref-1434 | 아니오 | medium | 2026-10-11 | — | — |
| f18 | [의견] | 구축자 의견: OPC 적합성 체계는 '제조사의 적합성 시험 도구 사전 점검(권고)'과 '인정 시험소 인증'을 구분하는 문장으로 고치고, 이 구조를 VDA 5050 의 인증 체계로 그대로 옮겨 쓰지 않는 것이 맞다. | ref-705, ref-1434 | 아니오 | medium | 2026-10-11 | — | — |
| f19 | [사실] | MassRobotics AMR_Interop_Standard.json(커밋 f9357a4)의 최상위 oneOf 는 identityReport 와 statusReport 두 정의만 참조하고, 위치(location) 정의는 x·y·angle·planarDatum 네 필드를 모두 필수로 두며, 명령·주문·작업 메시지 정의는 없다. | ref-230 | 아니오 | medium | 2026-10-11 | — | — |
| f20 | [의견] | 구축자 의견: MassRobotics 보고 메시지(신원·상태) 교환만으로 작업 명령 호환성이나 좌표계 정합을 확보했다고 주장하지 않는 것이 맞다. | ref-230 | 아니오 | medium | 2026-10-11 | — | — |
| f21 | [사실] | OPC 40010-1(OPC UA for Robotics Part 1) 1.02판 §11.2.2 는 서버 기능 묶음(Facet)을 기본(Base)·운전(MDS Operation)·자산관리 확장(AM Extended)·상태감시 확장(CM Extended) 넷으로 나누고, 표 124~127 에서 각 적합성 단위를 필수(M)·선택(O)으로 구분한다. | ref-034 | 아니오 | medium | 2025-09-08 | — | — |
| f22 | [의견] | 구축자 의견: 연동 요구에는 'OPC UA 지원' 대신 OPC UA Robotics 판·서버 Facet·선택 단위·인증 범위를 적게 하고, 이 정보모델을 VDA 5050 주문 스키마와 일대일로 자동 변환할 수 있다고 보지 않는 것이 좋다. | ref-034 | 아니오 | medium | 2026-10-11 | — | — |
| f24 | [사실] | 국가표준인증통합정보시스템(KSSN) 상세 페이지에는 KS B 7321-2 '로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델'이 실려 있으나, 이번 열람에서는 번호와 제목만 보였고 제정일·국제표준 부합화·고시 정보는 보이지 않았다. | ref-138 | 아니오 | medium | 2026-10-11 | — | — |
| f25 | [사실] | KSSN 상세 페이지에는 KS B 7321-2 와 별도로 KS B ISO 22166-202 '로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델'이 실려 있으나, 제정일·부합화 수준(IDT 여부)·고시 정보는 이번 열람에서 보이지 않았다. | ref-1435 | 아니오 | medium | 2026-10-11 | — | — |
| f26 | [의견] | 구축자 의견: oq-026 은 열림을 유지하고, KS B ISO 22166-202 가 국가표준 목록에 따로 있다는 점만 확인할 거리로 남기며, 그 제정일·부합화 수준과 KS B 7321-2 와의 대체 관계, 국내 적용 사례는 미확인으로 둔다. | ref-138, ref-1435 | 아니오 | low | 2026-10-11 | — | — |
| f30 | [추정] | OTTO by Rockwell Automation 은 2026-04-09 보도자료에서 OTTO 100·600·1200·1500 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 관제 소프트웨어 업체와 인증을 마쳤다고 밝혔으나, 시험한 프로토콜 판·시험 항목·시험 기관은 밝히지 않는다. | ref-608 | 아니오 | low | 2026-04-09 | — | 벤더 주장 |
| f31 | [사실] | VDMA 의 Mesh-Up 2025 안내는 automatica 2025(뮌헨, 2025-06-24~27) 전시장에서 9개 기업이 참여하고 MHP 가 상위 관제를 맡아, 여러 이동로봇이 작업대를 공급하는 양식화한 생산 라인을 보여 주는 혼합 플릿 시연(전시 시연이며 실제 공장 배치가 아님)을 설명한다. | ref-1436 | 아니오 | medium | 2026-10-11 | 제조 공장 / 수행 자원 | — |
| f32 | [사실] | 같은 Mesh-Up 2025 안내(automatica 2025 전시 시연, 실제 공장 배치 아님)는 관제 소프트웨어 공급자를 바꿔 고를 수 있는 점을 전시장에서 실시간으로 시연하지는 않는다고 밝힌다. | ref-1436 | 아니오 | medium | 2026-10-11 | 제조 공장 / 예외·성과 | — |
| f33 | [의견] | 구축자 의견: Mesh-Up 같은 전시 시연은 5절 '제조 공장' 현장 유형의 혼합 플릿 구성 예로만 쓰고 표 머리와 각 칸에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 밝히며, 실제 도입 사례나 현장 관제 교체가 검증된 근거로 세지 않는 것이 맞다. | ref-1436 | 아니오 | medium | 2026-10-11 | 제조 공장 | — |
| f34 | [사실] | Wagner 외(제22회 IEEE WFCS 2026)는 표준이 원격 조작(teleoperation)을 기본으로 다루지 않는다고 보고 VDA 5050 원격 조작 확장과 재현 평가용 VDA 5050 트래픽 생성기를 제안하며, VDA 5050 메시지·미들웨어 전송·Open RAN 무선 링크를 잇는 구성에서 지연과 통신 오버헤드를 평가한다. | ref-1437 | 아니오 | medium | 2026-04 | — | — |
| f36 | [사실] | TU Dortmund 통신망 연구실의 논문 소개(2026-04-24)는 이 평가가 재현성 높은 가상 무선(virtual-radio) 시험대와 실제 무선(over-the-air) 검증 구성을 함께 썼다고 설명하며, 정량 결과와 로봇 대수는 소개문에 없다. | ref-1438 | 아니오 | medium | 2026-04-24 | — | — |
| f37 | [의견] | 구축자 의견: 21번에서는 Wagner 외 연구를 VDA 5050 통신 부하·지연 평가로 소개하되 적합성 시험과 구별하고, 상세 네트워크 설계는 42. 분산 시스템·통신·컴퓨팅 구조 연결로만 두는 것이 맞다. | ref-1437, ref-1438 | 아니오 | medium | 2026-10-11 | — | — |
| f38 | [의견] | 구축자 의견: VDA 5050 연동 승인의 근거는 제3자 도구의 자체 진단, 벤더 간 인증 발표, 전시 시연, 인정 시험소 인증을 서로 다른 근거 수준으로 나눠 기록하는 것이 맞다. | ref-408, ref-608, ref-1436, ref-705, ref-1434 | 아니오 | medium | 2026-10-11 | — | — |
| f39 | [추정] | VDA 5050 작업반 참여 업체인 Idealworks 는 2026년 3월 소식 글에서 VDMA·VDA 가 2월 17일 3.0.0 판을 정식 채택했고 이어 법적 승인 절차를 거쳤다고 적어, VDA 공식 자료의 날짜 표시(카탈로그 2026-03-17·보도자료 2026-04-20)와 또 다른 날짜를 제시한다. | ref-1442 | 아니오 | low | 2026-03 | — | — |
| f40 | [사실] | buildingSMART 는 정보 전달 명세(Information Delivery Specification, IDS)를 2024-06-01 승인된 공식 표준으로 소개하고, 데이터 요구를 기계가 읽을 수 있게 기술해 IFC 모델의 적합성을 자동으로 검사할 수 있게 한다고 설명하며, 1.0 이전 판은 공식 표준이 아니라고 밝힌다. | ref-1439 | 아니오 | medium | 2024-06-01 | — | — |
| f41 | [사실] | IDS 공식 사용자 설명서는 IDS 파일이 하나 이상의 명세(specification)로 이루어지고 각 명세가 적용 대상(applicability)과 요구(requirements)를 가지며, 둘 다 엔터티·속성(attribute)·분류·속성 값(property)·재료·소속(partOf) 패싯으로 구성되고, 받는 쪽이 IDS 와 IFC 를 함께 불러 검사해 불일치 보고를 얻는다고 설명한다. | ref-1362 | 아니오 | medium | 2026-10-11 | — | — |
| f42 | [사실] | IDS 사용자 설명서는 패싯 파라미터에 단순 값 대신 열거(enumeration)·패턴(pattern)·범위(bounds)·길이(length)의 복합 제한을 걸 수 있다고 설명한다. | ref-1365 | 아니오 | medium | 2026-10-11 | — | — |
| f43 | [사실] | IDS 공식 저장소의 문서 안내는 소프트웨어 구현의 IDS 읽기·검사 기능이 올바른지 확인하기 위한 .ids·.ifc 쌍 250개 이상의 시험 파일 묶음을 TestCases 폴더에 둔다고 설명한다. | ref-1443 | 아니오 | medium | 2026-10-11 | — | — |
| f44 | [의견] | 구축자 의견: 21번 7절에는 IDS 1.0 을 '건물 정보 모델(IFC) 데이터 교환 요구의 적합성 검사 수단'으로 짧게 두고, 검사 도구 자체도 공식 시험 파일 묶음으로 확인할 수 있다는 점을 적되, 로봇–관제 메시지 적합성 시험과는 구별하며, 로봇 지도용 BIM 객체·속성 요구의 세부는 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙에 두는 것이 맞다. | ref-1439, ref-1362, ref-1443 | 아니오 | medium | 2026-10-11 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04-20 | 표준 | medium | 2026-10-11 | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN | 아니오 |
| ref-1412 | VDA(Verband der Automobilindustrie) | VDA 5050 | 2026-03-17 | 표준 | medium | 2026-10-11 | https://www.vda.de/en/news/publications/publication/vda-5050 | 아니오 |
| ref-1430 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema (tag 3.0.0) | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/order.schema | 아니오 |
| ref-1431 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema (tag 3.0.0) | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/factsheet.schema | 아니오 |
| ref-1432 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/visualization.schema (tag 3.0.0) | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/visualization.schema | 아니오 |
| ref-413 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema (main) | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema | 아니오 |
| ref-408 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 미확인 | 오픈소스 문서 | medium | 2026-10-11 | https://github.com/ekusiadadus/vda5050-lab | 아니오 |
| ref-705 | OPC Foundation | How to Certify - OPC Foundation | 미확인 | 표준 | medium | 2026-10-11 | https://opcfoundation.org/certification/how-to-certify/ | 아니오 |
| ref-1434 | OPC Foundation | Overview & Benefits — OPC Foundation Certification | 미확인 | 표준 | medium | 2026-10-11 | https://opcfoundation.org/certification/overview-benefits/ | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | high | 2026-10-11 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-034 | OPC Foundation / VDMA | OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration | 2025-09-08 | 표준 | high | 2026-10-11 | https://reference.opcfoundation.org/specs/OPC-40010-1 | 아니오 |
| ref-138 | 국가표준인증통합정보시스템(KSSN) | KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 미확인 | 표준 | medium | 2026-10-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010147546 | 아니오 |
| ref-1435 | 국가표준인증통합정보시스템(KSSN) | KS B ISO 22166-202 로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델 | 미확인 | 표준 | medium | 2026-10-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010158171 | 아니오 |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 2026-04-09 | 벤더 문서 | low | 2026-10-11 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 아니오 |
| ref-1436 | VDMA | Mobile Robots in Production: Mesh-Up 2025 | 미확인 | 업계 보고서 | medium | 2026-10-11 | https://www.vdma.eu/en/mesh-up | 아니오 |
| ref-1437 | Wagner, N. A., Toenning, L., Lünsch, D., Jost, J., Wietfeld, C., Detzner, P. | Teleoperating Mobile Robots via VDA 5050 – A First Middleware Evaluation within Open Industrial Networks | 2026-04 | 논문 | medium | 2026-10-11 | https://doi.org/10.1109/WFCS67029.2026.11511549 | 아니오 |
| ref-1438 | TU Dortmund, Communication Networks Institute (ComNets) | Interoperable Teleoperation of Mobile Robots in Intralogistics: Joint Paper Demonstrates End-to-End Network Co-Design for Smart Industries | 2026-04-24 | 정부·연구기관 | medium | 2026-10-11 | https://comnets.etit.tu-dortmund.de/details/interoperable-teleoperation-of-mobile-robots-in-intralogistics-joint-paper-demonstrates-end-to-end-network-co-design-for-smart-industries-63558/ | 아니오 |
| ref-1439 | buildingSMART International | Information Delivery Specification (IDS) | 미확인 | 표준 | high | 2026-10-11 | https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specifications-ids/ | 아니오 |
| ref-1362 | buildingSMART International (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/README.md | 미확인 | 표준 | high | 2026-10-11 | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/README.md | 아니오 |
| ref-1365 | buildingSMART International (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/restrictions.md | 미확인 | 표준 | high | 2026-10-11 | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/restrictions.md | 아니오 |
| ref-1443 | buildingSMART International (buildingSMART/IDS GitHub) | IDS — Documentation/README.md | 미확인 | 표준 | high | 2026-10-11 | https://github.com/buildingSMART/IDS/blob/development/Documentation/README.md | 아니오 |
| ref-1442 | idealworks | VDA 5050 3.0.0 release (March 2026) | 2026-03 | 벤더 문서 | low | 2026-10-11 | https://idealworks.com/en/news/vda5050-300-release-march-2026 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/integration/interoperability-standards-and-conformance.md | 5, 6, 7, 8, 10, 11 | 갱신(차등): 섹션 5 — 본문 수행 자원 칸의 '경로 계산'을 '선 유도 로봇의 경로 계산·안내'로 정정(f3·f5), 자유 주행 로봇의 경로 자체 계획·공유 병기(f4; 예정 경로 공유 세부는 2026-10-10-area27-s7 41~45행 연결). 현장 유형 보완: '제조 공장' 사례로 Mesh-Up 2025(f31·f32) — 표 머리와 각 칸에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 밝히고 매트릭스에서 도입 사례로 세지 않음(f33) / 섹션 6(분리 2026-09-25-area28-s6) — 「적합성 시험과 인증」첫 문단 '제조사가 자체 인증하거나' 정정(f15~f18: 적합성 시험 도구(compliance test tools) 사전 준비는 권고, 인증은 인정 시험소, SDK 응용도 개별 시험; 'CTT' 약어는 쓰지 않음). OTTO 문단에 날짜 2026-04-09·기종 4개·'등' 표기 보강, 각주 원문 미열람 해소(f30, 벤더 주장 유지). 선택 필드·재전송·취소 후 갱신 동작 시험표(f6·f7·f8; 재전송 규칙 자체는 2026-10-09-area41-s6 56행·command-and-task-execution-reliability.md 90행 연결). 근거 수준 구분(f38) / 섹션 7(분리 2026-09-25-area28-s7) — VDA 5050 행: 단일 발행일 미확인 유지, 저장소 명세 표지는 날짜 없음(f1), 날짜 비교는 2026-10-10-area20-s7「VDA 5050 3.0.0의 날짜 표시」로 연결하고 PDF 표지 'March 2026'은 [추정] 유지(f2), Idealworks 의 2026-02-17 채택 서술은 벤더 문서 추정으로만(f39). 본문 첫 문단 '주문 배정·경로 계산…' 정정(f3·f5). OPC 행 '자체·독립 시험소 인증' → '인정 시험소 인증(시험 도구는 사전 점검용)'(f17). MassRobotics 행 '(원문 미열람)' 해소와 location 필수 4필드·명령 메시지 부재(f19·f20). 3.0.0 태그 스키마 끝 쉼표 주의사항(f9 사실, 행·열 번호는 싣지 않음; 출처는 태그 파일 ref-1430~ref-1432 와 main 파일 ref-413, f12). OPC UA Robotics 서버 Facet 표 124~127(f21·f22). 국내 표준: KS B 7321-2·KS B ISO 22166-202 는 국가표준 목록 번호·제목만(f24·f25), 제정일·부합화는 미확인(f26). 트랙 반영 제안 2026-10-09-26(건축 도면 자동 인식 단계 2, IDS 1.0 → 7절) 처리: IDS 1.0 공식 표준(2024-06-01)·명세/적용 대상/요구 구조·패싯 여섯 종류·값 제한 네 종류·구현 검증용 시험 파일 묶음을 'BIM 데이터 교환 요구의 적합성 검사 수단'으로 짧게(f40~f44); 제안 요약의 기수·사용자 정의 속성 세트 명명 규칙·OBOS 프록시 관례는 원문 미확인이라 반영하지 않고 다음 실행 후보 / 섹션 8 — vda5050-lab 항목에 v0.2.0 개발자 프리뷰·인증 주장 아님 반영, 각주 '(원문 미열람)' 해소(f13·f14). Wagner 외 WFCS 2026 통신 평가 논문 추가(f34·f36, 적합성 시험과 구별 f37; 원격 조작 표기는 용어집 따름) / 섹션 10 — 42. 분산 시스템·통신·컴퓨팅 구조 연결(f37), 14. 도면·BIM에서 지도 만들기 연결(IDS, f44) / 섹션 11 — oq-005(f1·f2·f39), oq-055(f13~f18·f30·f38), oq-091(f9·f12), oq-026(f24~f26) 부분 근거, 모두 열림 유지. oq-111 은 이번에 새 근거 없음(TTA·KOROS 원문 미확인). 새 질문 2건. 후속 정리(이번 대상 아님): categories/governance-law-and-society/index.md 70행 '경로 계산' 일반화, ref-705 참고문헌 요약의 '자체 인증' 표현, ref-608 발행일 2026-04-09. |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- VDA 5050 3.0.0 태그 스키마의 끝 쉼표를 고친 수정본을 연동 시험에 쓸 때 공식 PDF·태그와의 차이를 누가 승인하고 어떤 회귀 시험으로 확인하는가? | 관련 영역: 21. 상호운용 표준·적합성, 57. 자산·소프트웨어 수명주기 관리 | 근거: f9 | 종류: 일반
- VDA 5050 2.x·3.x 판이 섞인 플릿을 실제 현장에서 전환하면서 판별 스키마 차이와 시험 입력을 어떻게 검증했는지 공개한 기록이 있는가? (관련 기존 질문: oq-091) | 관련 영역: 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성 | 근거: f12 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 23 · 교차 확인: 0
- 예산 사용량: 검색 5회 · 신규 출처 14건
- 미확인 항목:
    - VDA 5050 3.0.0 VDA 배포 PDF 표지의 'March 2026' 표기: WebFetch 가 압축 PDF 본문 텍스트를 읽지 못해 대조 불가(103쪽·A4 만 확인) — 출처 항목으로 넣지 않고 f2 에서 [추정] 유지를 제안
    - f9: 끝 쉼표의 정확한 행·열 번호와 main 브랜치 factsheet·visualization 스키마의 수정 여부는 확인하지 않음(main 은 order.schema 만 확인)
    - f24·f25: KSSN 상세 페이지에서 번호·제목만 보여 제정일·부합화(IDT 여부)·고시번호·쪽수 미확인
    - TTAK.KO-10.1295-Part8: 웹 검색에서 찾지 못했고 이전 브리프의 TTA 목록 URL 은 검증에서 HTTP 400 — 출처·finding 에서 뺌
    - KOROS 1148-8:2025 제정일과 TTA 표준과의 관계: 원문 봇 차단으로 미확인 — finding 에서 뺌
    - ISO 21423 단계·범위: iso.org 미열람 — 21번에는 새로 쓰지 않음
    - VDA5050 이슈 #660: 실재 미확인 — 출처에서 뺌
    - Wagner 외 본문의 평가 시나리오(로봇 수·주문 시간·원격 조작 구간)와 향후 과제 문구: 저자 공개본 PDF 텍스트를 읽지 못해 미확인
    - IDS 의 기수(필수·선택·금지), 사용자 정의 속성 세트 명명 규칙, 뉴질랜드 OBOS 프록시 관례(트랙 반영 제안 요약 항목): 이번에 원문으로 확인하지 못함
    - f39: Idealworks 의 2026-02-17 채택 서술은 VDA 자료로 확인되지 않음
    - VDA·VDMA 공인 적합성 인증 제도의 존재·부재(oq-055)는 확정 못 함
- 범위 경계 위반 의심:
    - f31~f33: Mesh-Up 2025 는 automatica 2025 전시 시연이며 실제 공장 배치가 아님. site_type '제조 공장'은 시연이 겨냥한 현장 유형을 뜻함
    - f34~f37: 무선망·Open RAN 통신 평가는 42. 분산 시스템·통신·컴퓨팅 구조 쪽 내용이라 21번에는 적합성 시험과 구별되는 통신 평가 연구로만 씀
    - f21·f22: OPC UA Robotics 정보모델은 4. 이기종 로봇 등록에서 이미 다루므로 21번에는 Facet·인증 범위 요구만 씀
    - f40~f44: IDS 는 건물 정보 모델 데이터 교환 표준으로 14. 도면·BIM에서 지도 만들기·건축 도면 자동 인식 트랙 쪽 내용이 많으므로 21번에는 적합성 검사 수단으로만 짧게 씀
- 한계: 재실행 1회차. 반려 사유 1(신규 참고문헌 id 충돌): 직전 실행 2026-10-10-06 이 같은 예약 구간에서 쓴 ref-1424~ref-1428 과 기존 출처 ref-1429(Franke 외)를 피해 신규 출처를 예약 구간 안의 ref-1430~ref-1443 으로 다시 매겼다. VDA 카탈로그는 기존 id ref-1412 을 재사용하고(이전 브리프의 ref-1412 표기 철회), OPC 개요는 ref-1434, Mesh-Up 은 ref-1436, Wagner 외는 ref-1437 로 옮겼다. 이전 브리프의 ref-1424(이슈 #660)·ref-1425(TTA 목록)·ref-1426(KSSN, 이제 ref-1435)·ref-1428·ref-1429 할당은 모두 없앴다. 실행 컨텍스트의 next_ref_id(ref-1412)가 이미 사용 중이라 구간 안 미사용 번호를 썼다 — pipeline/agent_runner.py 의 next_ref_id 계산 확인 필요. (관련 finding: f9·f16·f25·f31·f34) 반려 사유 2(원문 열람 재현 실패): ref-1412 PDF 는 이번에도 텍스트를 읽지 못해 출처에서 빼고 f1 을 저장소 마크다운 표지 사실로 바꿨다(관련 finding: f1·f2). KSSN 두 페이지는 다시 열었으나 번호·제목만 보여 f24·f25 를 그 범위의 사실로 줄이고 f26 은 열린 질문 유지 의견으로 바꿨다. TTA 목록은 웹 검색으로도 확인 못 해 f28 을 지웠다. Wagner 외는 PDF 텍스트를 읽지 못해 f35 를 지우고, f36 은 연구실 소개문(ref-1438)으로 확인한 가상 무선·실제 무선 구분만 남겼다. f10(파서별 행·열 번호)은 재현 근거가 없어 지웠다. 이번에 fetched: true 로 적은 출처는 모두 이번 실행에서 WebFetch 또는 raw 경로로 다시 열었고(ref-031 은 입력 원문 텍스트 + 3.0.0 태그 raw), fetch_url 이 다른 경우 적었다. 반려 사유 3(미확인 출처·전언 finding): ref-1424(이슈 #660)를 출처에서 빼고 f11·f23·f27 을 지웠으며, ref-159·ref-710 은 근거 finding 이 없어 sources 에서 뺐다. f29 는 지웠다(oq-111 열림 유지). 반려 사유 4(트랙 반영 제안 미처리): buildingSMART 공식 페이지와 공식 저장소 문서로 IDS 1.0 을 조사해 f40~f44 를 냈고 7절 반영안을 rationale 에 적었다. 제안 요약의 기수·사용자 정의 속성 세트·OBOS 프록시는 확인 못 해 다음 실행 후보로 남긴다. required_fixes 대응: [의견]은 모두 claim 첫머리에 '구축자 의견: '을 붙였다. f9 출처를 확인한 태그 파일별 항목(ref-1430~ref-1432)과 main 파일(ref-413)로 바꾸고 ref-051 은 뺐다. f13 은 'Developer Preview'로 재서술하고 'Synthetic Demo Preview' 인용을 없앴다. f21 표 번호를 124~127 로 고쳤다. ref-608 발행일을 2026-04-09 로 고쳤다. f31~f33 에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 넣었다. 새 열린 질문 가운데 TTA–KOROS 질문은 뺐고, 2.x·3.x 전환 질문의 근거를 f12 와 oq-091 로 바꿨다. 용어: '원격 조작' 표기, 'CTT' 대신 '적합성 시험 도구(compliance test tools)'. 열린 질문 해결 제안 없음: oq-005 근거 f1·f2·f39, oq-055 근거 f13~f18·f30·f38, oq-091 근거 f9·f12, oq-026 근거 f24~f26 (모두 부분 근거). 검색 5회/30, 신규 출처 14건/15. 재사용 9건(ref-031·ref-032·ref-1412·ref-408·ref-705·ref-230·ref-034·ref-138·ref-608, 모두 이번에 다시 엶). IDS 관련 URL 이 트랙 실행에서 이미 등록됐다면 퍼블리셔가 같은 URL 로 합쳐야 한다(참고문헌 목록 요약본에 없어 확인 못 함). 교차 확인 0건(VDA 계열 자료, 같은 저장소 파일, OPC 두 페이지는 각각 같은 기관). 정정 요청 없음. 용어 후보 없음(정보 전달 명세·적합성 시험·원격 조작은 용어집에 있음).
```

### runs/2026-10-10-06/research.md

```markdown
# 리서치 브리프 2026-10-10-06

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-06 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 20. 로봇·제조사 관제 연동 |
| 대분류 | F. 연동 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 — IO-AMRs 과제 문장(ref-258)이 원문 미열람이고 주관 기관·과제 단계(계획인지 완료인지)가 없음
- 섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 출하 시나리오 하나뿐이고 '수행 자원' 행이 추정이며 직접 제어·위임 비교 자료 없음(oq-031). 연동 위치와 제어 수준을 나눠 보는 기준, 상업 시설·전시 시연 사례 없음
- 섹션 6. 대표 접근법과 기술 — 연결 단절 시 실행 의미와 상태 분리, 신호등 수준 연동의 정지 시간 전제·교착 시 사람 개입(oq-032), 상태·오류 변환의 실제 필드 매핑 사례(oq-033) 근거가 약함
- 섹션 7. 관련 표준·프레임워크·오픈소스 — VDA 5050 3.0.0 발행일 미확인(oq-005), 공개 구현(free_fleet·ros_amr_interop·vda-5050-lib.js)의 판별 지원 범위와 Open-RMF 구역 기능의 개발 상태 미반영
- 섹션 8. 대표 연구와 자료 — Lopes 외 논문(ref-136) 저자 미확인·120 ms 지표 명칭과 측정 조건 미확인, Franke 외(ref-1429) 원문 미열람·워크숍 구성 미기재
- 섹션 10. 다른 연구영역과의 연결 — 21. 상호운용 표준·적합성(ISO 21423 단계), 47. AI·학습·적응과 모델 운영(MCP 연동)과의 연결 없음
- 섹션 11. 열린 질문 — oq-005·oq-031·oq-032·oq-033 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? [분류원문]
2. oq-005 VDA 5050 3.0.0 의 발행일은 공식 자료에서 무엇으로 표시되는가? (섹션 7·11 겨냥)
3. oq-032 제조사 관제가 일시정지·재개만 허용하는 신호등 수준 연동에서 정지·교착 처리의 전제는 무엇인가? (섹션 6·11 겨냥)
4. oq-033 공개 구현은 로봇 상태·오류를 표준 필드로 어떻게 옮기는가? (섹션 6·11 겨냥)
5. oq-031 직접 제어와 제조사 관제 위임을 고르는 기준이나 비교 자료가 있는가? (섹션 5·11 겨냥)
6. 기존 8절·3절 연구 자료(Lopes 외, Franke 외, IO-AMRs)의 서지·측정 조건·단계는 원문에서 무엇으로 확인되는가? (섹션 3·8 겨냥)
7. VDA 5050·Open-RMF 공개 구현의 판별 지원 범위와 개발 중 기능은 무엇인가? (섹션 7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 보도자료 'Version 3.0 of VDA 5050 released'의 본문 날짜는 2026-04-20(Berlin, April 20, 2026)이며, 보도자료 URL 은 260421 계열이다. | ref-032 | 아니오 | medium | 2026-10-10 | — | — |
| f2 | [사실] | VDA 발행물 카탈로그의 VDA 5050 Version 3.0.0 항목은 날짜를 2026-03-17(March 17, 2026)로 표시한다. | ref-1423 | 아니오 | medium | 2026-10-10 | — | — |
| f3 | [사실] | VDA 가 배포하는 VDA 5050 3.0.0 공식 PDF 의 표지는 판 표기를 'Version 3.0.0, March 2026'으로 적어 월 단위(2026-03)까지만 밝힌다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f4 | [사실] | VDA 의 공식 자료 세 가지가 VDA 5050 3.0.0 의 날짜를 서로 다르게 표시한다: 카탈로그 2026-03-17, 보도자료 본문 2026-04-20, 명세 표지 2026-03. | ref-1423, ref-032, ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f5 | [의견] | VDA 5050 3.0.0 의 발행일은 하나로 확정하지 않고 서지에는 판 표기의 월(2026-03)을 적으며, 카탈로그 표시일(2026-03-17)과 보도자료 날짜(2026-04-20)는 주석으로 함께 남기는 것이 맞아 보인다(oq-005 부분 답변). | ref-031, ref-032, ref-1423 | 아니오 | low | 2026-10-10 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 §4.1 은 로봇이 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고 마지막으로 해제된 노드까지 주문을 수행한다고 정한다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f7 | [사실] | VDA 5050 3.0.0 은 주문에 딸린 동작·즉시 동작·구역 동작의 상태를 상태 메시지의 actionStates·instantActionStates·zoneActionStates 세 배열로 나눠 보고하게 하며, 구역 동작의 예정 상태 보고는 선택 사항이다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f8 | [의견] | 로봇이 단절 중에도 해제된 노드까지 주행을 이어 가므로(f6) ROP 어댑터는 연결 단절(connection 상태)을 곧 정지로 해석하지 말고, 연결 상태와 동작 실패(동작 상태 배열의 FAILED)를 별도 상태로 보존해 단절 시 실행 의미와 상태를 분리하는 것이 좋아 보인다. | ref-031 | 아니오 | low | 2026-10-10 | — | — |
| f9 | [사실] | Open-RMF EasyTrafficLight API(rmf_fleet_adapter 2.14.0)의 moving_from() 경고는 로봇이 다음 체크포인트에서 멈출 시간이 있을 때만, 곧 정지 명령의 통신 지연과 로봇 최대 감속을 감안해 호출하라고 하며, 이를 어기면 MovingError·WaitingError 가 나고 교통 흐름이 끊기거나 교착될 수 있다고 적는다. | ref-1424 | 아니오 | medium | 2026-10-10 | — | — |
| f10 | [사실] | 같은 헤더의 Blocker 설명은 해결할 수 없는 충돌로 교착이 생기면 RMF 교통 협상 시스템이 충돌 참여자를 충분히 제어하지 못하므로 사람 개입이 필요할 수 있다고 적는다. | ref-1424 | 아니오 | medium | 2026-10-10 | — | — |
| f11 | [의견] | 신호등 수준으로 붙는 제조사 플릿의 연동 계약에는 정지 명령의 유무만이 아니라 정지 가능 시간(통신 지연·최대 감속)과 정지 확인 응답, 교착 시 사람 개입 경로를 함께 적는 것이 좋아 보이며, 제어 수준별 교통 성능을 같은 조건에서 비교한 자료는 여전히 찾지 못했다(oq-032 부분 근거). | ref-1424 | 아니오 | low | 2026-10-10 | — | — |
| f12 | [의견] | 신호등 연동을 평가·재현할 때는 쓰는 rmf_fleet_adapter 패키지 판을 함께 기록하는 것이 좋아 보인다. 2.14.0(2026-09-26) 변경 이력에 EasyTrafficLight 의 플릿 상태 발행 수정(#525)과 누적 지연 계산 수정(#524)이 들어 있기 때문이다. | ref-1398 | 아니오 | low | 2026-10-10 | — | — |
| f13 | [추정] | InOrbit 개발자 문서는 InOrbit 이 제어하는 로봇 플릿을 RMF core 에 잇는 오픈소스 전체 제어(full control) 플릿 어댑터를 제공해 여러 제조사 로봇의 중앙 교통 조정을 가능하게 한다고 밝힌다. | ref-1029 | 아니오 | low | 2026-10-10 | — | 벤더 주장 |
| f14 | [의견] | 연동 위치(제조사 관제 API 를 거치는지, 로봇에 직접 붙는지)와 제어 수준(전체 제어인지)은 따로 판단해 별도 항목으로 기록하고, 제어 권한은 경로 지정·교체, 정지, 진행 상태 반환으로 나눠 적는 것이 좋아 보인다(oq-031 판단 기준 보강). | ref-251, ref-1029 | 아니오 | low | 2026-10-10 | — | — |
| f15 | [사실] | Lopes 외(Applied Sciences 2025, 15(13), 7235, 2025-06-27) 논문은 본문 §6.2 에서 로봇 상태의 평균 갱신 간격(average update interval)을 약 120 ms, 사용자 화면 지연을 1초 미만으로 보고하며, 초록은 같은 값을 'average latency'로 표현한다. | ref-136 | 아니오 | medium | 2026-10-10 | — | — |
| f16 | [사실] | 같은 논문은 실험 시험 중 AMR·AGV 를 포함해 최대 20대를 화면·서버 성능의 큰 저하 없이 동시에 감시할 수 있었고 시험 기간 서버 가동률이 99.5% 이상이었다고 보고한다. | ref-136 | 아니오 | medium | 2026-10-10 | — | — |
| f17 | [사실] | 같은 논문의 §5.3(로봇 지도 작성·연결) 시험은 코임브라 공학연구소 기계공학과의 약 500 m² 실험실에서 수행됐으며, 120 ms·20대 결과를 어디서 측정했는지는 논문에 명시돼 있지 않다. | ref-136 | 아니오 | medium | 2026-10-10 | — | — |
| f18 | [의견] | Lopes 외의 결과는 자동차 공장 적용을 목표로 한 실험실 연구의 감시 성능이므로, 자동차 공장의 장기 운영 지연이나 20대 동시 주행 제어 성능으로 인용하지 않고, 기존 '작업 상태 갱신 평균 지연 120 ms' 표현은 '로봇 상태 평균 갱신 간격 약 120 ms'로 고치는 것이 맞아 보인다. | ref-136 | 아니오 | low | 2026-10-10 | — | — |
| f19 | [사실] | Franke 외(Logistics Journal: Proceedings No.19, 2023-10-11) 연구는 2023년 봄 소프트웨어 기업 2곳·하드웨어 제조사 3곳·창고 사용자 1곳 등 여섯 회사가 참여한 워크숍으로 VDA 5050 개념에 기반한 새 표준 인터페이스 요구를 수집했다. | ref-1429 | 아니오 | medium | 2026-10-10 | — | — |
| f20 | [의견] | Franke 외 연구는 연동 요구 분석 자료로 분류하고, 실물 플릿을 비교한 실험이 아니므로 직접 제어와 제조사 관제 위임의 처리량 비교 근거로 쓰지 않는 것이 맞아 보인다. | ref-1429 | 아니오 | low | 2026-10-10 | — | — |
| f21 | [사실] | ARM Institute 의 IO-AMRs 과제 소개는 주관 기관을 Siemens Technology 로, 협력 기관을 FedEx·Yaskawa Motoman·Waypoint Robotics·University of Memphis 로 적는다. | ref-258 | 아니오 | medium | 2026-10-10 | — | — |
| f22 | [사실] | IO-AMRs 과제 소개는 다중 지도 관리자·연결 계층·전역 플릿 관리자를 이전 ARM 지원 과제의 산출물을 활용해 만들 '계획'으로 서술해, 이 과제가 소개 시점에 계획 단계였음을 보여 준다. | ref-258 | 아니오 | medium | 2026-10-10 | — | — |
| f23 | [의견] | IO-AMRs 소개는 과제 목표의 근거로만 쓰고 달성한 운영 성과의 근거로 쓰지 않으며, 3절의 목표 문장에는 주관 기관과 계획 단계라는 범위만 보태는 것이 맞아 보인다. | ref-258 | 아니오 | low | 2026-10-10 | — | — |
| f24 | [추정] | Open-RMF rmf_ros2 PR #516 'Add GoToZone feature'는 구역 이름을 받아 구역 안 경유점을 예약하는 기능을 제안하며 2026-10-10 기준 미병합 상태인 것으로 보이나, 이번 환경에서 PR 원문과 상태를 직접 확인하지 못했다. | ref-1425 | 아니오 | low | 2026-10-10 | — | 원문 미열람 |
| f25 | [사실] | Open Robotics Discourse 의 2026-05-04 Interop SIG 공지는 CHART 가 RMF-2.0 프로젝트로 개발한 새 기능을 단계적으로 공개하며 첫 단계가 시설 '구역(zones)' 관리 기능이고, 공지 시점에 이 기능이 검토 중(currently undergoing review)이라고 밝힌다. | ref-1426 | 아니오 | medium | 2026-10-10 | — | — |
| f26 | [의견] | 어댑터 기능 목록을 정리할 때는 배포판(태그)에 든 기능과 검토 중인 기능(예: Open-RMF 구역 기능)을 구분해 적는 것이 좋아 보인다. | ref-1426, ref-1425 | 아니오 | low | 2026-10-10 | — | — |
| f27 | [사실] | ros_amr_interop 1.1.1 의 MassRobotics 송신 예제 설정은 ROS 토픽 /we_b_robots/mode(std_msgs/String)를 operationalState 에, /troubleshooting/errorcodes 를 errorCodes 에 연결하고, 오류 코드는 쉼표로 구분한 문자열로 받아 MassRobotics 표준이 요구하는 배열로 바꾼다고 주석에 적는다. | ref-255 | 아니오 | medium | 2026-10-10 | — | — |
| f28 | [사실] | MassRobotics AMR 상호운용 표준 1.0 태그의 JSON 스키마는 상태 보고(statusReport)의 필수 필드를 uuid·timestamp·operationalState·location 넷으로 둔다. | ref-230 | 아니오 | medium | 2026-10-10 | — | — |
| f29 | [의견] | ros_amr_interop 예제는 ROS→MassRobotics 한 방향의 운용 상태·오류 매핑 사례일 뿐이므로 Open-RMF·VDA 5050·MassRobotics 세 체계의 공통 상태·오류 어휘 표준으로 일반화하지 않는 것이 맞아 보이며, 세 체계를 함께 다루는 표준 매핑은 이번에도 확인하지 못했다(oq-033 부분 근거). | ref-255, ref-230 | 아니오 | low | 2026-10-10 | — | — |
| f30 | [사실] | free_fleet 1.3.0 태그의 README 는 메시지를 CycloneDDS 의 dds_idlc 로 FleetMessages.idl 에서 생성한다고 설명하고, ROS 1·ROS 2 양쪽의 cyclonedds 판을 같게 맞춰야 한다고 권고하며, DDS 를 쓰지 않는 새 판을 준비 중이라고 적는다. | ref-256 | 아니오 | medium | 2026-10-10 | — | — |
| f31 | [의견] | 위키의 free_fleet 설명(현재 기본 브랜치의 zenoh 기반 Nav2·Nav1 어댑터)과 과거 태그 1.3.0 의 CycloneDDS 기반 설치 절차는 섞지 않고 판을 밝혀 적는 것이 좋아 보인다. | ref-256 | 아니오 | low | 2026-10-10 | — | — |
| f32 | [사실] | vda-5050-lib.js 의 v1.7.0(2026-04-29) 변경 이력은 VDA 5050 3.0 지원을 추가하며 새 Topic.ZoneSet·Topic.Responses 토픽, VdaVersion 의 '3.0.0', 3.0 용 사전 컴파일 검증기와 타입을 넣었다고 적는다. | ref-742 | 아니오 | medium | 2026-10-10 | — | — |
| f33 | [의견] | 어댑터에 VDA 5050 라이브러리를 쓸 때는 라이브러리 판과 지원 규격 판을 함께 고정하는 것이 좋아 보이며, 라이브러리가 선언한 3.0 지원은 제조사 로봇과의 적합성·실물 호환성 검증으로 세지 않는 것이 맞아 보인다. | ref-742 | 아니오 | low | 2026-10-10 | — | — |
| f34 | [추정] | InOrbit 은 Automate 2026 시연에서 Ati Robotics·Kärcher·Neura Robotics·Omron·Peer Robotics·Quasi Robotics·Unitree 7개사 로봇이 공유 공간에서 함께 임무를 수행하고, Slamcore·Guide Robotics 의 실시간 위치 추적(RTLS)으로 수동 차량까지 묶어 InOrbit 을 포함해 10개사가 협업했다고 밝힌다. | ref-1427 | 아니오 | low | 2026-10-10 | 기타 | 벤더 주장 |
| f35 | [의견] | Automate 2026 시연의 '10개사'는 참여 기업 수(로봇 7·위치 추적 2·InOrbit 1)이지 로봇 대수나 AMR 제조사 수가 아니므로, 상용 운영 사례가 아닌 전시 시연으로 분류하는 것이 맞아 보인다. | ref-1427 | 아니오 | low | 2026-10-10 | 기타 | — |
| f36 | [추정] | 카카오모빌리티는 2024년 로보티즈와 업무협약을 맺고 신라스테이 서초·반얀트리 클럽 앤 스파 서울 등 호텔에 상용 로봇 배송 서비스를 적용해 왔다고 발표했다(2026-03-16). | ref-1428, ref-1200 | 아니오 | low | 2026-10-10 | 상업 시설 | 벤더 주장 |
| f37 | [의견] | 카카오모빌리티–로보티즈 호텔 사례는 국내 플랫폼–로봇 제조사 연동 사례로 분류하되, 제어 위임 방식·API·로봇 대수가 공개되지 않아 한 현장에서 여러 제조사 플릿을 함께 운영한 증거나 직접 제어·위임 비교 근거(oq-031)로는 쓰지 않는 것이 맞아 보인다. | ref-1428, ref-1200 | 아니오 | low | 2026-10-10 | 상업 시설 | — |
| f38 | [추정] | 연계 대상: ISO 21423(산업용 이동로봇 통신·상호운용) 공식 카탈로그가 2026-10-10 기준 '60.00 Under publication' 단계를 표시한다는 외부 메모의 기록이 있으나, iso.org 가 403 으로 막혀 이번에 직접 확인하지 못했다. | ref-159 | 아니오 | low | 2026-10-10 | — | 원문 미열람 |
| f39 | [사실] | Open Robotics Discourse 의 Interop SIG 2026-07-02 세션 공지는 Open-RMF REST API 를 언어 모델이 호출할 수 있는 MCP 도구로 노출하는 서버와, 영어 명령을 다단계 RMF 임무로 바꿔 NVIDIA Isaac Sim 창고의 로봇이 Nav2 로 실행하는 에이전트(Nayantra)를 발표한다고 알린다. | ref-854 | 아니오 | medium | 2026-10-10 | — | — |
| f40 | [의견] | MCP 로 Open-RMF REST API 를 노출하는 시연은 47. AI·학습·적응과 모델 운영(및 12. 채팅으로 업무 지시·오케스트레이션)과의 연결 지점으로 제안할 만하나, 시뮬레이션 창고 시연이므로 실물 다사업자 플릿의 안정성 근거로 쓰지 않는 것이 맞아 보인다. | ref-854 | 아니오 | low | 2026-10-10 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-10 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04-20 | 표준 | medium | 2026-10-10 | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN | 아니오 |
| ref-1423 | VDA(Verband der Automobilindustrie) | VDA 5050 | 2026-03-17 | 표준 | medium | 2026-10-10 | https://www.vda.de/en/news/publications/publication/vda-5050 | 아니오 |
| ref-251 | Open Robotics | Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://osrf.github.io/ros2multirobotbook/integration_fleets.html | 아니오 |
| ref-1029 | InOrbit | Contents — InOrbit Developer Portal | 미확인 | 벤더 문서 | medium | 2026-10-10 | https://developer.inorbit.ai/docs | 아니오 |
| ref-1424 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp | 아니오 |
| ref-1398 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |
| ref-136 | Lopes, D., Pereira, T., Gonçalves, A. 외 17명 (Polytechnic University of Coimbra 등; Applied Sciences, MDPI) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 2025-06-27 | 논문 | medium | 2026-10-10 | https://www.mdpi.com/2076-3417/15/13/7235 | 아니오 |
| ref-1429 | Franke, S., Lünsch, D., Jost, J., & Roidl, M. | Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept | 2023-10-11 | 논문 | medium | 2026-10-10 | https://proc.logistics-journal.de/article/download/1067/1036/8465 | 아니오 |
| ref-258 | ARM Institute | Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs) | 미확인 | 정부·연구기관 | medium | 2026-10-10 | https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/ | 아니오 |
| ref-1425 | chart-singapore / CHART (open-rmf/rmf_ros2 GitHub) | Add GoToZone feature (rmf_ros2 pull request #516) | 미확인 | 오픈소스 문서 | medium | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/pull/516 | 예 |
| ref-1426 | Open Robotics Discourse (OSRA Interop SIG) | Interop SIG, 7 May 2026: Open-RMF Upcoming Zone Feature | 2026-05-04 | 오픈소스 문서 | medium | 2026-10-10 | https://discourse.openrobotics.org/t/interop-sig-7-may-2026-open-rmf-upcoming-zone-feature/54490 | 아니오 |
| ref-255 | InOrbit (inorbit-ai GitHub) | ros_amr_interop — README (ROS packages for AMR interoperability: VDA5050 connector, MassRobotics AMR sender) | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/inorbit-ai/ros_amr_interop | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | high | 2026-10-10 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-256 | Open Robotics (open-rmf) | free_fleet — README (A free fleet management system) | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/free_fleet | 아니오 |
| ref-742 | coatyio (vda-5050-lib.js GitHub) | vda-5050-lib.js — Universal VDA 5050 library for Node.js and browsers (README) | 미확인 | 오픈소스 문서 | medium | 2026-10-10 | https://github.com/coatyio/vda-5050-lib.js | 아니오 |
| ref-1427 | InOrbit.AI | 10 Companies around the World Collaborate to Showcase Robot Orchestration at Automate 2026 | 미확인 | 벤더 문서 | low | 2026-10-10 | https://www.inorbit.ai/automate-2026 | 아니오 |
| ref-1428 | 카카오모빌리티 | 카카오모빌리티, 국내 로봇 기업 협력해 ’플랫폼 기반 로봇 생태계 확장’ 지속 | 2026-03-16 | 벤더 문서 | low | 2026-10-10 | https://www.kakaomobility.com/newsroom/detail/%EC%B9%B4%EC%B9%B4%EC%98%A4%EB%AA%A8%EB%B9%8C%EB%A6%AC%ED%8B%B0-%EA%B5%AD%EB%82%B4-%EB%A1%9C%EB%B4%87-%EA%B8%B0%EC%97%85-%ED%98%91%EB%A0%A5%ED%95%B4-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EA%B8%B0%EB%B0%98-%EB%A1%9C%EB%B4%87-%EC%83%9D%ED%83%9C%EA%B3%84-%ED%99%95%EC%9E%A5-%EC%A7%80%EC%86%8D-361 | 아니오 |
| ref-1200 | 아시아경제 | 호텔 룸서비스도 카카오모빌리티 로봇이…"가동률 ... (제목 일부만 확인) | 2026-03-16 | 기사 | low | 2026-10-10 | https://view.asiae.co.kr/article/2026031610244491183 | 아니오 |
| ref-159 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 미확인 | 표준 | medium | 2026-10-10 | https://www.iso.org/standard/86749.html | 예 |
| ref-854 | Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse | Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 2026-06-25 | 오픈소스 문서 | medium | 2026-10-10 | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/integration/robot-and-vendor-fleet-manager-integration.md | 3, 5, 6, 7, 8, 10, 11 | 갱신(차등): 섹션 3 — IO-AMRs 목표 문장(기존 내용 확인)에 주관 기관 Siemens Technology·협력 기관과 '계획 단계' 범위만 보탬(f21·f22·f23). / 섹션 5 — 연동 위치와 제어 수준을 따로 기록하는 기준(f14, InOrbit 문서 f13 은 벤더 주장 보강 근거로만; 제조사 관제 API 경유 전체 제어 조건은 '제약' 행 ref-251 에 이미 있어 중복 추가 안 함), 새 사례 두 개: 전시 시연(현장 유형 기타, f34·f35, 벤더 주장), 국내 호텔(현장 유형 상업 시설, f36·f37, 벤더 주장; 2. 사용 사례·요구·책임 범위의 ref-1200 사례와 같은 건이므로 '플랫폼–제조사 연동 사례' 분류 관점만 짧게). / 섹션 6(주제 페이지 2026-09-25-area09-s6 요약) — VDA 연결 단절 시 실행 의미와 상태 분리(f6~f8; '마지막으로 해제된 노드' 번역어는 대분류 개요와 같게, f6 사실은 개요에 이미 있으므로 영역 20 에는 상태 분리 관점으로), 신호등 연동의 정지 시간 전제·교착 시 사람 개입(f9~f11), 상태·오류 변환표 절에 ros_amr_interop→MassRobotics 필드 매핑 사례(f27~f29). / 섹션 7(주제 페이지 2026-09-25-area09-s7 표) — VDA 5050 3.0.0 행의 '정확한 발행일 미확인'을 공식 자료 세 날짜 표시로 교체(f1~f5), Open-RMF 신호등 연동 평가 시 패키지 판 기록(f12; 2.14.0 수정 사실은 27. 다중 로봇 경로·교통 관리 — MAPF 에 이미 있음), Open-RMF 구역 기능 개발 상태(f24 추정·f25·f26), free_fleet 1.3.0 판 구분(f30·f31), vda-5050-lib.js v1.7.0 3.0 지원(f32·f33). / 섹션 8(주제 페이지 2026-09-25-area09-s8) — Lopes 외 항목의 저자 '미확인'을 17명 저자·DOI 로, '작업 상태 갱신 평균 지연 120 ms'를 '로봇 상태 평균 갱신 간격 약 120 ms'로 정정하고 20대 감시·§5.3 실험실 범위 추가(f15~f18), Franke 외 항목에 워크숍 구성과 서지 보강(f19·f20). / 섹션 10(주제 페이지 2026-09-25-area09-s10) — 21. 상호운용 표준·적합성: ISO 21423 단계 기록은 추정으로 연결 제안 수준(f38, oq-027 과 겹치므로 링크만), 47. AI·학습·적응과 모델 운영·12. 채팅으로 업무 지시·오케스트레이션: MCP 로 Open-RMF REST API 노출 시연(f39·f40, oq-141 관련). / 섹션 11(주제 페이지 2026-09-25-area09-s11) — 분리 페이지의 '신규' 세 질문을 실제 id 로 표기(oq-031·oq-032·oq-033), 부분 근거: oq-005 ← f1~f5, oq-032 ← f9~f11, oq-033 ← f27~f29, oq-031 ← f14·f20·f37(답 아님, 판단 기준만). 모두 열림 유지. 새 질문 5건. 다음 실행 후보: 21. 상호운용 표준·적합성(ISO 21423 발행 확인, f38), 27. 다중 로봇 경로·교통 관리 — MAPF(신호등 연동 교착, f9~f11). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- Lopes 외 논문이 보고한 로봇 상태 평균 갱신 간격 약 120 ms 와 최대 20대 동시 감시는 어디서 어떤 로봇 구성·시험 기간·측정 지점(타임스탬프 정의)으로 측정했는가? | 관련 영역: 20. 로봇·제조사 관제 연동, 37. 관제 화면·실행 기록 | 근거: f15 | 종류: 일반
- ARM Institute IO-AMRs 과제의 완료 보고서·공개 코드·실물 로봇 대수와 정량 결과는 공개됐는가? | 관련 영역: 20. 로봇·제조사 관제 연동 | 근거: f22 | 종류: 일반
- zenoh 기반 free_fleet 어댑터에 대응하는 배포 태그와 지원 조합(ROS 2 배포판·Nav2·zenoh 판) 시험표는 무엇인가? | 관련 영역: 20. 로봇·제조사 관제 연동, 42. 분산 시스템·통신·컴퓨팅 구조 | 근거: f30 | 종류: 일반
- InOrbit 의 Automate 2026 다중 제조사 시연에서 실제 투입된 로봇 대수와 임무 실패·재시도 기록이 공개됐는가? | 관련 영역: 20. 로봇·제조사 관제 연동 | 근거: f34 | 종류: 일반
- 카카오모빌리티–로보티즈 호텔 배송 서비스에서 플랫폼은 로봇을 직접 제어하는가, 로보티즈 관제에 임무 단위로 맡기는가, 그 연동 API 와 로봇 대수·운영 기간은 공개됐는가? | 관련 영역: 20. 로봇·제조사 관제 연동, 64. 상업 시설 | 근거: f36 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 21 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 6건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-06/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - VDA 5050 3.0.0 GitHub 릴리스 설명의 'March 19th, 2026'과 게시 시각(published_at)은 이 환경에서 확인하지 못해 출처로 넣지 않았다(발행일 null 유지).
    - f24: GoToZone PR #516(ref-1425)의 설명·미병합 상태는 GitHub 접근 차단으로 원문 대조 실패. 간접 근거로 2026-05-04 SIG 공지(ref-1426, f25)만 사실로 둠
    - f38: ISO 21423 카탈로그의 '60.00 Under publication' 단계는 iso.org 403 으로 확인 실패(ref-159 원문 미열람)
    - f15~f17: Lopes 외 120 ms·20대 결과의 측정 장소·로봇 구성·시험 기간은 논문에 명시돼 있지 않음
    - f30: free_fleet 1.3.0 태그 커밋일 미확인(published null)
    - f34·f36: Automate 2026 시연과 카카오모빌리티 호텔 사례는 벤더 발표만 있고 독립 확인 없음(ref-1200 은 보도자료를 옮긴 기사)
    - oq-031: 국내 물류센터의 직접 제어·위임 비중·비용·처리량 비교 자료는 이번에도 찾지 못함
- 범위 경계 위반 의심:
    - f38: ISO 21423 은 21. 상호운용 표준·적합성 쪽 내용이므로 claim 을 '연계 대상: '으로 시작하고 10절 연결 제안 수준으로만 씀
    - f9~f11: 신호등 연동의 교착 처리는 27. 다중 로봇 경로·교통 관리 — MAPF 와 겹치므로 영역 20 에는 연동 계약 관점으로 한정
    - f39·f40: MCP·언어 모델 연동은 47. AI·학습·적응과 모델 운영·12. 채팅으로 업무 지시·오케스트레이션 쪽 내용이라 연결 제안으로만 씀
    - f36·f37: 호텔 사례의 업무 범위는 2. 사용 사례·요구·책임 범위·64. 상업 시설에 이미 있으므로 영역 20 에는 연동 사례 분류만
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(queries 0 은 집계 없음을 뜻함). 신규 출처 6건(ref-1423, ref-1424, ref-1425, ref-1426, ref-1427, ref-1428, 예약 구간 ref-1423~ref-1452 안), 재사용 15건. 메모 출처 매핑: n1·VDA 공식 PDF→ref-031, n3→ref-032, n4→ref-1423(신규), n5→ref-251, n6→ref-1424(신규, 위키에 EasyTrafficLight.hpp 출처 없음), n7→ref-136, n8→ref-1429, n9→ref-258, n10→ref-1398, n11→ref-1425(신규, 미열람), n12→ref-742, n13→ref-255, n14→ref-230, n15→ref-256, n16→ref-1427(신규; 기존 ref-177 은 RoboticsTomorrow 게재 보도자료라 다른 문서), n17→ref-1428(신규, 카카오모빌리티 보도자료 원문)+ref-1200(같은 내용을 옮긴 아시아경제 기사, 이번에 재열람해 호텔 이름 확인), n18→ref-854, n19→ref-159, n20→ref-1029. n2(GitHub 릴리스)는 넣지 않음. 간접 근거로 SIG 공지 ref-1426(신규) 추가. 검증 수정 반영: VDA 날짜는 세 공식 표시가 다르다는 것을 사실로, 하나로 확정하지 않는 것은 의견으로(f4·f5); 상태 배열 근거를 §6.6.9·§7.8 로(§7.7 아님, f7); '마지막으로 해제된 노드' 번역어를 대분류 개요와 맞춤(f6); Lopes 120 ms 를 '평균 갱신 간격'으로, 실험실 범위를 §5.3 지도 작성·연결 작업으로 좁힘(f15~f17); Franke 근거 쪽수 p.5(f19); IO-AMRs 는 주관 기관·계획 단계만 새로(f21·f22); 제조사 관제 API 경유 전체 제어는 5절 '제약' 행 기존 내용이라 중복 추가 안 함(f13 은 보강); EasyTrafficLight 2.14.0 수정은 의견으로만(f12); GoToZone PR·ISO 21423 단계는 추정·미열람(f24·f38); Automate·호텔은 벤더 주장·추정 유지. 교차 확인 0건: VDA 날짜 세 자료는 모두 VDA 계열, Open-RMF 헤더·변경 이력은 같은 프로젝트, ref-1200 은 ref-1428 을 옮긴 기사라 독립 출처가 아니다. 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-005 근거 f1~f5, oq-032 근거 f9~f11, oq-033 근거 f27~f29, oq-031 판단 기준 f14·f20·f37. 분리 페이지 11절의 '신규' 세 질문은 oq-031·oq-032·oq-033 이다. 메모의 새 질문 U1~U11 가운데 기존 질문과 겹치는 U1(oq-005)·U2(oq-031)·U3(oq-032)·U4(oq-033)·U11(oq-141 과 겹침)과 본문 근거가 없는 U6 은 빼고 U5·U7·U8·U9·U10 을 다듬어 5건을 올렸다. 현장 유형 사례 finding: 상업 시설(호텔, f36·f37), 기타(전시 시연, f34·f35). 용어 후보 없음(플릿 어댑터·VDA 5050·오픈 RMF 는 용어집에 있음). 입력 누락 없음. 우선 지정 질문 없음.
```

### runs/2026-09-25-59/research.md

```markdown
# 리서치 브리프 2026-09-25-59

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-59 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 23. 시험·형식 검증·벤치마크 |
| 대분류 | F. 도입·검증·유지관리 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(장애 주입·회귀 시험·형식 검증·런타임 검증·벤치마크 구분 필요)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음(22. 시뮬레이션·예측용 디지털 트윈과의 목적 구분 필요)
- 섹션 11. 열린 질문 비어 있음(대상 영역 열린 질문 oq-055·oq-058·oq-063·oq-077 반영 필요)

## 조사 질문

1. 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]
2. 로봇 시스템 시험에서 장애 주입·시나리오 기반 시뮬레이션 시험·회귀 시험은 어떤 도구와 방식으로 이루어지며 실무의 어려움은 무엇인가? (섹션 3·4·6 겨냥)
3. 다중 로봇·AGV 시스템의 교착·제약 위반을 형식 검증(모델 검사, BDD 기반 분석)과 런타임 검증으로 확인하는 연구·도구는 무엇인가? (섹션 6·8 겨냥)
4. 다중 로봇 경로·작업 배정 알고리즘과 로봇 작업 능력을 비교하는 벤치마크·대회(MAPF 벤치마크, League of Robot Runners, NIST ARIAC)는 무엇을 어떻게 측정하며, 격자 가정 성과가 실제 처리량으로 이어지는가? (섹션 7·8 겨냥, oq-058)
5. 이동로봇·무인운반차의 안전·성능 시험을 정하는 표준(ISO 3691-4, ASTM F45, KS B ISO 18646)과 국내 시험기관(한국로봇산업진흥원)의 시험 항목은 무엇인가? (섹션 7·9 겨냥, 한국 자료 우선)
6. VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? (oq-055, 섹션 9·11 겨냥)
7. ROP 가 직접 맡을 시험 범위(오케스트레이션 논리·인터페이스·장애 대응)와 제조사·시험기관에 맡길 범위(로봇 자체 안전·주행 성능)는 어떻게 나뉘는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | NIST ARIAC 2025 문서는 경진 중 컨베이어 정지, 전압 시험기 데이터 중단, 진공 공구 파지 실패, 고우선 주문 투입을 '민첩성 도전 과제'로 주입해 시스템의 장애 감지·복구와 긴급 요청 대응을 시험한다. | ref-629 | 아니오 | medium | 2025 | 예외·성과 | — |
| f2 | [사실] | NIST ARIAC 2025 채점은 제출한 키트·모듈의 완료 비율로 기본 점수를 주고 시간 안 완료·고우선 주문 신속 처리·센서 예산 준수 등에 가점을, 충돌·정상 부품 낙하·잘못된 위치 배치 등에 감점을 준 뒤, 시행별 상위 2회 평균 실행 점수(80%)와 심사위원 평가(20%)를 합친다. | ref-630 | 아니오 | medium | 2025 | 예외·성과 | — |
| f3 | [추정] | ARIAC 가 장애를 시험 중에 계획적으로 주입하고 완료·시간·비용(센서 예산)·위반을 한 점수로 묶는 방식은, 물류 현장 오케스트레이션의 회귀 시험에서도 장애 시나리오와 처리량·시간·비용 지표를 함께 판정 기준으로 두는 틀로 옮겨 쓸 수 있을 것으로 보인다. | ref-629, ref-630 | 아니오 | low | 2025 | 예외·성과 | — |
| f4 | [사실] | Luckcuck 외(2019)의 자율 로봇 형식 명세·검증 조사 논문은 자율 로봇 시스템이 복잡하고 혼성적이며 안전 필수인 경우가 많아, 시험과 시뮬레이션만으로는 정확성 보장이나 인증 근거로 충분하지 않다고 보고 형식 방법의 과제·형식체계·접근법을 분류했다. | ref-631 | 아니오 | medium | 2019-09 | — | 원문 미열람 |
| f5 | [사실] | von Berg·Aichernig·Wedenik(FM 2026 사례 연구)은 정해진 경로망을 따라 움직이는 창고 AGV 시스템을 세 가지 방식으로 전이 시스템에 인코딩하고 이진 결정 다이어그램(BDD)으로 기호적 분석해, 합성 레이아웃과 실제 레이아웃 모두에서 교착 회피를 수행했다. | ref-643 | 아니오 | medium | 2026-05 | 제약 | 원문 미열람 |
| f6 | [사실] | Afzal 외(ICST 2020)는 로봇 실무자 면담으로 로봇 시스템 시험 실무 12가지와 어려움 9가지를 도출해 실세계 복잡성, 커뮤니티와 표준, 구성요소 통합의 세 주제로 묶었고, 이를 로봇 시스템 시험에 초점을 맞춘 첫 연구로 소개했다. | ref-632 | 아니오 | medium | 2020 | — | 원문 미열람 |
| f7 | [사실] | ros2_fault_injection 은 ROS 2 토픽을 *_raw 로 돌려 받아 편향·잡음·지연·누락·명령 정지 같은 장애를 넣어 다시 발행하고, 서비스 강제 실패와 좌표 변환 손상도 지원하며, YAML 시나리오의 단정(assertion)으로 합격·불합격을 내고 헤드리스 실행기가 종료 코드로 지속적 통합(CI)에 결과를 넘긴다. | ref-633 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f8 | [추정] | 연계 대상: ros2_fault_injection 이 기본으로 다루는 오도메트리·레이저 스캔·IMU 등 센서 신호 장애는 로봇 자체 인식·주행의 견고성 시험에 해당하고, ROP 쪽 장애 주입은 같은 프록시 방식을 관제 명령·상태 메시지와 설비 응답 수준에 적용하는 형태가 될 것으로 보인다. | ref-633 | 아니오 | low | 2026-09-25 | — | — |
| f9 | [사실] | ROSMonitoring 은 YAML 설정으로 ROS 토픽·서비스를 관찰하는 감시 노드를 생성하며, 온라인 모드에서는 외부 판정기(oracle)의 판정을 받아 위반 메시지를 기록하거나 걸러 내고 오프라인 모드에서는 사건만 기록하는 명세 형식 비종속 런타임 검증 틀로 ROS 1·ROS 2 를 모두 지원한다. | ref-634 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f10 | [사실] | Open-RMF 시뮬레이션 문서는 시뮬레이션에 쓴 코드를 실제 시스템에서 수정 없이 실행하므로 시뮬레이션의 반복 가능한 시나리오로 버그 수정을 확인하고, 드물지만 심각한 예외 상황과 장시간 운전을 배치 전에 시험할 수 있다고 설명한다. | ref-406 | 아니오 | medium | 2026-09-25 | — | — |
| f11 | [사실] | Stern 외(2019)는 다중 에이전트 경로 찾기(MAPF) 논문마다 가정과 목적함수가 달라 기준선 비교가 어렵다는 문제를 들어 공통 용어를 정리하고 새 격자 기반 벤치마크를 소개했다. | ref-186 | 아니오 | medium | 2019 | — | 원문 미열람 |
| f12 | [사실] | League of Robot Runners 는 Amazon Robotics 가 후원하는 다중 로봇 조율 대회로, MAPF 의 핵심 과제를 찾고 벤치마크 인스턴스를 만들어 최신 성과를 추적하는 것을 목표로 하며 로봇 동역학·지속형 계획·작업 배정·실시간 실행을 창고 물류 같은 응용을 겨냥해 다룬다. | ref-636 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f13 | [사실] | LSMART(2026)는 기존 MAPF·지속형 MAPF 연구가 단순화한 운동 모델과 완전한 실행·통신을 가정한다는 한계를 들어, AGV 플릿 관리 시스템(FMS) 안에서 임의의 MAPF 알고리즘을 평가하는 오픈소스 시뮬레이터를 내고 언제 계획할지·어떻게 계획할지·계획 실패 시 어떻게 복구할지를 비교했다. | ref-637 | 아니오 | medium | 2026-02 | 예외·성과 | 원문 미열람 |
| f14 | [사실] | 연계 대상: ISO 3691-4:2023 은 AGV·AMR 을 포함한 무인 산업용 차량과 그 시스템의 안전 요구사항과 검증 수단을 정하며, 사람 감지 시험·안정성 시험과 부속서의 검증 절차를 포함한다. | ref-470 | 아니오 | medium | 2023 | 제약 | 원문 미열람 |
| f15 | [사실] | 연계 대상: ASTM F45 위원회(무인 자동 유도 산업 차량)는 용어·권고 관행·시험 방법을 개발하며 환경 영향, 도킹·주행, 물체 감지·보호, 통신·통합 분과를 두고, NIST 가 이 표준 개발에 참여한다. | ref-639 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f16 | [사실] | 연계 대상: KS B ISO 18646 시리즈는 서비스 로봇의 성능 기준과 관련 시험 방법을 KS 로 부합화한 것으로, 제1부는 바퀴형 로봇의 이동 능력을 다루고 주행·조작 등을 다루는 다른 부가 함께 있다. | ref-640 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f17 | [사실] | 한국로봇산업진흥원은 로봇 시험평가에 KS·ISO·IEC·CISPR 등 표준 시험 방법을 적용하고, 경사 노면·특수 노면·계단·주행 내구 같은 로봇 주행 성능 시험을 수행한다. | ref-641 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f18 | [추정] | OTTO by Rockwell Automation 은 자사 AMR 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 대응 인트라로지스틱스 소프트웨어 업체들과 인증을 마쳤다고 발표했다. | ref-642 | 아니오 | low | 2026-09-25 | — | 원문 미열람, 벤더 주장 |
| f19 | [추정] | oq-055 관련: 이번 조사에서 VDA 5050 공식 인증 기관이나 공식 적합성 시험 절차는 확인하지 못했고, 확인된 인증은 로봇 제조사와 관제 소프트웨어 업체 사이의 쌍별 연동 인증 형태여서, ROP 는 새 로봇 연동마다 자체 인수 시험을 두어야 할 것으로 보인다. | ref-642 | 아니오 | low | 2026-09-25 | 완료·인계 | 원문 미열람 |
| f20 | [의견] | Open-RMF 시뮬레이션이 강조하는 시나리오 반복·예외 상황 탐색 환경은 22. 시뮬레이션·예측용 디지털 트윈과 공유되지만, 22. 시뮬레이션·예측용 디지털 트윈은 운영 정책·수요 변화의 효과 예측을, 23. 시험·형식 검증·벤치마크는 변경 후 동작 확인을 목적으로 나누는 것이 분류 원문 정의에 맞아 보인다. | ref-406 | 아니오 | low | 2026-09-25 | — | — |
| f21 | [추정] | 분류 원문 질문 '업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가?'에 대해, 확인한 자료로 보면 반복 가능한 시뮬레이션 시나리오에 장애 주입과 합격 판정 단정을 붙여 지속적 통합에서 매 변경마다 다시 돌리는 방식이 답이 될 것으로 보이나, 물류 오케스트레이션 소프트웨어에 이를 적용해 결과를 공개한 현장 사례는 찾지 못했다. | ref-629, ref-633, ref-406 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f22 | [추정] | 시나리오 예시(가상): 피킹 단계에서 플릿 어댑터를 업데이트한 뒤, 운반 중인 로봇이 멈추는 장애를 주입하고 작업이 재배정되는지와 완료 확인 전에는 재고 변경이 확정되지 않는지를 단정으로 확인하는 회귀 시험을 구성할 수 있을 것으로 보인다. | ref-629, ref-633 | 아니오 | low | 2026-09-25 | 피킹 / 완료·인계 | — |
| f23 | [추정] | ROP 가 직접 맡을 시험 몫은 작업 배정·교통 관리 논리의 교착·제약 위반 검증, 관제 인터페이스 적합성, 장애 주입 시 재배정·복구 동작의 회귀 시험, 운영 중 런타임 감시로 보인다. | ref-643, ref-633, ref-634, ref-406 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f24 | [추정] | 연계 대상: 로봇 자체의 사람 감지·안정성 같은 안전 검증(ISO 3691-4)과 주행·도킹·이동 성능 시험(ASTM F45, KS B ISO 18646, 한국로봇산업진흥원 주행 성능 시험)은 제조사와 시험기관 영역이고, ROP 는 그 결과를 로봇 등록·배정 조건의 입력으로 받는 쪽으로 보인다. | ref-470, ref-639, ref-640, ref-641 | 아니오 | low | 2026-09-25 | 제약 | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-629 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 2025 | 정부·연구기관 | high | 2026-09-25 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 아니오 |
| ref-630 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Scoring | 2025 | 정부·연구기관 | high | 2026-09-25 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scoring.html | 아니오 |
| ref-631 | Luckcuck, M., Farrell, M., Dennis, L. A., Dixon, C., & Fisher, M. | Formal Specification and Verification of Autonomous Robotic Systems: A Survey | 2019-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1807.00048 | 예 |
| ref-632 | Afzal, A., Le Goues, C., Hilton, M., & Timperley, C. S. | A Study on Challenges of Testing Robotic Systems | 2020 | 논문 | medium | 2026-09-25 | https://www.computer.org/csdl/proceedings-article/icst/2020/09159069/1m3oOVjQnIc | 예 |
| ref-633 | reeceholland (ros2_fault_injection GitHub) | ros2_fault_injection — README | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/reeceholland/ros2_fault_injection | 아니오 |
| ref-634 | University of Liverpool Autonomy and Verification (ROSMonitoring GitHub) | ROSMonitoring: a Runtime Verification Framework for ROS — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/autonomy-and-verification-uol/ROSMonitoring | 아니오 |
| ref-186 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 2019 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1906.08291 | 예 |
| ref-636 | IDM Lab (USC) 게재 초록, 저자 미확인 | The League of Robot Runners: Competition Goals, Designs, and Implementation [System Demonstration] | 2024 | 논문 | medium | 2026-09-25 | https://idm-lab.org/bib/abstracts/Koen24p.html | 예 |
| ref-637 | arXiv 게재 논문(저자 미확인) | Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems | 2026-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2602.15721 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-639 | NIST | ASTM Committee F45 on Driverless Automatic Guided Industrial Vehicles | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.nist.gov/programs-projects/astm-committee-f45-driverless-automatic-guided-industrial-vehicles | 예 |
| ref-640 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113281 | 예 |
| ref-641 | 한국로봇산업진흥원(KIRIA) | 시험평가 \| KIRIA 첨단로봇 실증지원 디지털 플랫폼 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://kiria.org/rp/kiria/tva/inr/page.dn | 예 |
| ref-642 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 미확인 | 벤더 문서 | low | 2026-09-25 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 예 |
| ref-643 | von Berg, B., Aichernig, B. K., & Wedenik, F. | BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper) | 2026-05 | 논문 | medium | 2026-09-25 | https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16 | 예 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절 왜 중요한가: f4(시험·시뮬레이션만으로 불충분), f6(로봇 시험의 어려움), f10(배치 전 반복 시험), f13(격자 가정과 현실 실행의 차이) / 4절 핵심 개념: 장애 주입(f1·f7), 회귀 시험과 CI(f7·f21), 형식 검증·교착(f4·f5), 런타임 검증(f9), 벤치마크(f11·f12) / 5절 현장 시나리오: f22(피킹·완료·인계, 가상 구성안임을 명시), f21(분류 원문 질문, 추정) / 6절 대표 접근법: f1·f3(장애 주입형 시험), f5(BDD 교착 분석), f7·f8(장애 주입 도구), f9(런타임 검증), f10(시뮬레이션 회귀), f13(현실적 MAPF 평가) / 7절 표준·오픈소스: f14(ISO 3691-4), f15(ASTM F45), f16(KS B ISO 18646), f17(한국로봇산업진흥원), f7·f9·f10(오픈소스), f1·f2(NIST ARIAC) / 8절 대표 연구: f4·f5·f6·f11·f12·f13 / 9절 경계: f23(ROP 직접), f8·f14·f15·f16·f24('연계 대상') / 10절 연결: 22. 시뮬레이션·예측용 디지털 트윈(f20), 15. 다중 로봇 경로·교통 관리 — MAPF(f5·f11~f13), 12. 명령·작업 실행의 신뢰성과 19. 모니터링·이상 탐지·원인 분석(f9), 24. 자산·소프트웨어 수명주기 관리(f21, 업데이트 후 재검증), 25. 안전·위험 관리(f14), 9. 로봇·제조사 관제 연동과 28. 표준·상호운용성·다사업자 거버넌스(f18·f19), 20. 예외 복구·재계획·업무 연속성(f13 복구 설계) / 11절 열린 질문: oq-055(f18·f19 부분 근거), oq-058(f13 부분 근거), oq-063, oq-077, open_questions_new 3건. f18 은 [추정]+'벤더 주장' 병기. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 장애 주입 | Fault Injection | 시험 중 센서 신호·메시지·서비스·장비에 지연, 누락, 고장 같은 장애를 계획적으로 넣어 시스템이 장애를 감지하고 복구하는지 확인하는 시험 기법이다. |
| 회귀 시험 | Regression Testing | 소프트웨어나 설정을 바꾼 뒤 기존에 통과하던 정상·장애 시나리오를 다시 실행해 변경이 기존 동작을 깨뜨리지 않았는지 확인하는 시험이다. |
| 런타임 검증 | Runtime Verification | 실행 중인 시스템의 사건을 감시기로 관찰해 명세한 성질의 위반을 판정하고 기록하거나 차단하는 검증 기법이다. |
| 모델 검사 | Model Checking | 시스템을 상태 전이 모델로 표현하고 교착 부재 같은 성질이 도달 가능한 모든 상태에서 성립하는지 자동으로 확인하는 형식 검증 기법이다. |

## 열린 질문

새로 생긴 질문:

- 로봇 제조사 펌웨어나 플릿 어댑터를 업데이트한 뒤 회귀 시험의 최소 기준으로 삼을 장애 시나리오 집합에 대해 공개된 기준이나 국내 사례가 있는가? | 관련 영역: 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리 | 근거: f21 | 종류: 일반
- BDD·모델 검사 같은 교착 부재 형식 검증을 대규모 창고 레이아웃과 동적 작업 배정에 적용하면 계산 규모의 한계는 어디이며 운영 중 재검증에 쓸 수 있는가? | 관련 영역: 23. 시험·형식 검증·벤치마크, 15. 다중 로봇 경로·교통 관리 — MAPF | 근거: f5 | 종류: 일반
- 국내 시험기관(한국로봇산업진흥원 등)의 로봇 시험 항목에 다중 로봇 관제·오케스트레이션 소프트웨어 수준의 시험이 포함되는가, 없다면 누가 그 기준을 정하는가? | 관련 영역: 23. 시험·형식 검증·벤치마크, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f17 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 22회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처)
    - f5·f11·f12·f13: 논문 원문 미열람, 초록·검색 요약 범위
    - f14: ISO 3691-4 부속서 검증 절차 세부 미확인(유료 표준)
    - f15: F3244 등 개별 ASTM 시험 방법 내용 미확인
    - f16: KS B ISO 18646 각 부의 KS 제정일·판 미확인
    - f18: OTTO 인증의 시험 항목·주체 미확인(벤더 주장)
    - f19: VDA 5050 공식 적합성 시험 절차의 부재 여부 미확인(검색 요약에 VDMA 가 시험 환경을 계획한다는 언급이 있었으나 출처가 명확하지 않아 쓰지 않음)
    - ref-636·ref-637 저자 미확인
    - ref-633 라이선스 미확인
- 범위 경계 위반 의심:
    - f8·f14·f15·f16·f24: 로봇 자체 센서 인식·주행 성능·차량 안전 시험은 분류 원문 9장 '로봇 자체 지능·제어' 쪽 외부 연계 영역이므로 '연계 대상:'으로 표시
    - f22: 가상 시나리오 구성안이며 실제 사례로 서술하지 않도록 claim 에 '시나리오 예시(가상)' 표기
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: ref-629·ref-630(NIST ARIAC 2025 challenges·scoring, 미러 목록 경로), ref-633(ros2_fault_injection), ref-634(ROSMonitoring), ref-406(재사용, Open-RMF 시뮬레이션 장). 나머지 11건은 검색 요약 기준(신뢰도 상한 medium). IntelLabs scenario_execution README raw 경로는 main·jazzy 모두 404 라 출처로 넣지 않았다. League of Robot Runners Start-Kit README 는 열었으나 평가 지표가 없어 쓰지 않았다. 검색 22회/30, 신규 출처 15건/15(ref-629~ref-643, 예약 구간 안)로 신규 출처 예산에 도달해 Scenario Execution for Robotics(arXiv 2409.07080), Timed Rebeca 기반 ROS 2 다중 로봇 모델 검사(arXiv 2511.15227), KTL 로봇시험인증센터, arculus VDA 5050 적합성 시험 도구는 출처로 넣지 않았다. 재사용 1건: ref-406(2026-09-25-56 브리프 값 사용). 참고문헌 목록 전체 값이 입력에 없어 ref-007(NIST 협업 로봇 성능)·ref-008(NIST ARIAC)의 기존 값을 재사용하지 못하고 ARIAC 는 개별 페이지 URL 로 새 id 를 붙였다(퍼블리셔 대조 필요). 열린 질문: oq-055 는 f18·f19, oq-058 은 f13 이 부분 근거일 뿐 해결로 보지 않았고, oq-063·oq-077 은 이번에 조사하지 못했다. 한국 자료: KS B ISO 18646(ref-640), 한국로봇산업진흥원(ref-641). 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 섞지 않았고, 22. 시뮬레이션·예측용 디지털 트윈과의 목적 구분은 f20(의견)으로만 냈다. 정정 요청 없음.
```

### data/source_texts/ref-031.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
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

To reduce the communication overhead, the MQTT QoS level 0 (Best Effort) shall be used for the topics `order`, `instantActions`, `state`, `factsheet`, `zoneSet`, `responses` and `visualization`. QoS level 1 (At Least Once) shall be used for the topic `connection`.

Protocol security needs to be taken into account by broker configuration, but is not addressed within this guideline.

### 4.2 Topic levels

The MQTT topic structure is not strictly defined due to the mandatory topic structure of cloud providers.
For a cloud-based MQTT broker the topic structure might have to be adapted individually, but it should roughly follow the proposed structure.
The topic names defined in the following sections are mandatory.

For a local broker the MQTT topic levels are suggested as followed:

**interfaceName/majorVersion/manufacturer/serialNumber/topic**

Example:
```
vda5050/v3/KIT/0001/order
```

MQTT Topic Level | Data type | Description
---|---|---
interfaceName | string | Name of the used interface
majorVersion | string | Major version number of the VDA 5050 recommendation, preceded by "v"
manufacturer | string | Manufacturer of the mobile robot.
serialNumber | string | Unique mobile robot serial number consisting of the following characters: <br>A-Z <br>a-z <br>0-9 <br>_ <br>. <br>: <br>-
topic | string | Topic (e.g., order or state) see Section [4.4 Topics for Communication](#43-topics-for-communication)

>Table 1 Explanation of suggested MQTT topic levels

Since the `/` character is used to define topic hierarchies, it shall not be used in any of the aforementioned fields.
Wildcard characters `+` and `#` as well as the character `$` that is reserved for broker internal topics should not be used either.

### 4.3 Topics for communication

The protocol uses the following topics for information exchange between fleet control and mobile robots.
…(발췌: 전체 207,642자 중 앞 16,621자)
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

### data/source_texts/ref-125.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_request.json",
  "title": "Task Request",
  "description": "Describe a task request",
  "type": "object",
  "properties": {
    "unix_millis_earliest_start_time": {
      "description": "(Optional) The earliest time that this task may start",
      "type": "integer"
    },
    "unix_millis_request_time": {
      "description": "(Optional) The time that this request was initiated",
      "type": "integer"
    },
    "priority": {
      "description": "(Optional) The priority of this task. This must match a priority schema supported by a fleet.",
      "type": "object"
    },
    "category": { "type": "string" },
    "description": {
      "description": "A description of the task. This must match a schema supported by a fleet for the category of this task request."
    },
    "labels": {
      "description": "Labels to describe the purpose of the task dispatch request, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
      "type": "array",
      "items": { "type": "string" }
    },
    "requester": {
      "description": "(Optional) An identifier for the entity that requested this task",
      "type": "string"
    },
    "fleet_name": {
      "description": "(Optional) The name of the fleet, or an array of fleet names, allowed to perform this task. If specified, only the named fleet(s) will bid for this task.",
      "oneOf": [
        { "type": "string" },
        { "type": "array", "items": { "type": "string" } }
      ]
    }
  },
  "required": ["category", "description"]
}
```

### data/source_texts/ref-126.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/cancel_task_request.json",
  "title": "Cancel Task Request",
  "description": "Ask for a task to be canceled.",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a task cancellation request",
      "type": "string",
      "enum": ["cancel_task_request"]
    },
    "task_id": {
      "description": "Specify the task ID to cancel",
      "type": "string"
    },
    "labels": {
      "description": "Labels to describe the purpose of the cancellation, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["type", "task_id"]
}
```

### data/source_texts/ref-127.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/interrupt_task_request.json",
  "title": "Task Interruption Request",
  "description": "Ask for a task to be interrupted. An interrupted task will resume its task later when a resume_task_requested is sent.",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a task interruption request",
      "type": "string",
      "enum": ["interrupt_task_request"]
    },
    "task_id": {
      "description": "Specify the task ID to interrupt",
      "type": "string"
    },
    "labels": {
      "description": "Labels to describe the purpose of the interruption, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["type", "task_id"]
}
```

### data/source_texts/ref-128.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/rewind_task_request.json",
  "title": "Task Rewind Request",
  "description": "Ask for a task to rewind itself to an earlier phase.",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a task rewind request",
      "type": "string",
      "enum": ["rewind_task_request"]
    },
    "task_id": {
      "description": "Specify the ID of the task that should rewind",
      "type": "string"
    },
    "phase_id": {
      "description": "Specify the phase that should be rewound to. The task will restart at the beginning of this phase.",
      "type": "integer",
      "minimum": 0
    }
  },
  "required": ["type", "task_id", "phase_id"]
}
```

### data/source_texts/ref-129.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

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

  <xsd:element name = "TransactionProfile"              type = "TransactionProfileType" />

<!-- Transaction Elements -->
  <xsd:element name = "GetTransactionProfile"           type = "GetTransactionProfileType"/>
  <xsd:element name = "ShowTransactionProfile"          type = "ShowTransactionProfileType"/>

<!-- Simple & Complex Types  -->

  <xsd:complexType name = "TransactionProfileType">
    <xsd:sequence>
      <xsd:element name = "ID"                          type = "IdentifierType"/>
      <xsd:element name = "Description"                 type = "DescriptionType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "HierarchyScope"              type = "HierarchyScopeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "PublishedDate"               type = "DateTimeType"
                                                        minOccurs = "0"/>
      <xsd:element name = "SupportedAction"             type = "SupportedActionType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:group   ref  = "Extended:TransactionProfile" minOccurs = "0" maxOccurs = "1"/>
    </xsd:sequence>
    <xsd:attribute name = "releaseID"                   type="xsd:normalizedString"     use="required"/>
    <xsd:attribute name = "versionID"                   type="xsd:normalizedString"     use="optional"/>
  </xsd:complexType>

  <xsd:complexType name = "SupportedActionType">
    <xsd:sequence>
      <xsd:element name = "ID"                          type = "IdentifierType"/>
      <xsd:element name = "Description"                 type = "DescriptionType"
                                                        minOccurs = "0" maxOccurs = "unbounded"/>
      <xsd:element name = "TransactionVerb"             type = "TransactionVerbType"/>
      <xsd:element name = "TransactionNoun"             type = "TransactionNounType"/>
      <xsd:element name = "InformationUser"             type = "IndicatorType" minOccurs = "0"/>
      <xsd:element name = "InformationProvider"         type = "IndicatorType" minOccurs = "0"/>
      <xsd:element name = "InformationSender"           type = "IndicatorType" minOccurs = "0"/>
      <xsd:element name = "InformationReceiver"         type = "IndicatorType" minOccurs = "0"/>
      <xsd:element name = "ObjectWildcardSupported"     type = "IndicatorType" minOccurs = "0"/>
      <xsd:element name = "PropertyWildcardSupported"   type = "IndicatorType" minOccurs = "0"/>
      <xsd:group   ref  = "Extended:SupportedAction"    minOccurs = "0" maxOccurs = "1"/>
    </xsd:sequence>
    <xsd:attribute name = "releaseID"                   type="xsd:normalizedString"     use="required"/>
    <xsd:attribute name = "versionID"                   type="xsd:normalizedString"     use="optional"/>
  </xsd:complexType>

        <xsd:complexType name = "TransactionNoun1Type">
          <xsd:simpleContent>
                <xsd:restriction base="CodeType">
          <!-- Personnel Model -->
                        <xsd:enumeration value="PERSON"/>
                        <xsd:enumeration value="PERSONNEL CLASS"/>
                        <xsd:enumeration value="PERSONNEL INFORMATION"/>
          <!-- Equipment Model -->
                        <xsd:enumeration value="EQUIPMENT"/>
                        <xsd:enumeration value="EQUIPMENT CAPABILITY TEST"/>
                        <xsd:enumeration value="EQUIPMENT CLASS"/>
                        <xsd:enumeration value="EQUIPMENT INFORMATION"/>
          <!-- Physical Asset Model -->
                        <xsd:enumeration value="PHYSICAL ASSET"/>
                        <xsd:enumeration value="PHYSICAL ASSET CLASS"/>
                        <xsd:enumeration value="PHYSICAL ASSET INFORMATION"/>
          <!-- Master Data Profile Model -->
                        <xsd:enumeration value="MASTER DATA PROFILE"/>
          <!-- Material Model -->
                        <xsd:enumeration value="MATERIAL CLASS"/>
                        <xsd:enumeration value="MATERIAL DEFINITION"/>
                        <xsd:enumeration value="MATERIAL LOT"/>
                        <xsd:enumeration value="MATERIAL INFORMATION"/>
                        <xsd:enumeration value="MATERIAL SUBLOT"/>
          <!-- Process Segment Model -->
                        <xsd:enumeration value="PROCESS SEGMENT"/>
                        <xsd:enumeration value="PROCESS INFORMATION"/>
          <!-- Opertional Location Model -->
                        <xsd:enumeration value="OPERATIONAL LOCATION"/>
                        <xsd:enumeration value="OPERATIONAL LOCATION CLASS"/>
                        <xsd:enumeration value="OPERATIONAL LOCATION INFORMATION"/>
          <!-- Operations Definition Model -->
                        <xsd:enumeration value="OPERATIONS DEFINITION"/>
                        <xsd:enumeration value="OPERATIONS SEGMENT"/>
                        <xsd:enumeration value="OPERATIONS DEFINITION INFORMATION"/>
          <!-- Operations Event Model -->
                        <xsd:enumeration value="OPERATIONS EVENT"/>
                        <xsd:enumeration value="OPERATIONS EVENT CLASS"/>
                        <xsd:enumeration value="OPERATIONS EVENT DEFINITION"/>
                        <xsd:enumeration value="OPERATIONS EVENT INFORMATION"/>
          <!-- Operations Schedule Model -->
                        <xsd:enumeration value="OPERATIONS SCHEDULE"/>
                        <xsd:enumeration value="OPERATIONS REQUEST"/>
                        <xsd:enumeration value="SEGMENT REQUIREMENT"/>
          <!-- Operations Performance Model -->
                        <xsd:enumeration value="OPERATIONS PERFORMANCE"/>
                        <xsd:enumeration value="OPERATIONS RESPONSE"/>
          <!-- Operations Capability Model -->
                        <xsd:enumeration value="OPERATIONS CAPABILITY"/>
                        <xsd:enumeration value="OPERATIONS CAPABILITY INFORMATION"/>
          <!-- Resource Relationship Network Model -->
                        <xsd:enumeration value="RESOURCE RELATIONSHIP NETWORK"/>
                        <xsd:enumeration value="RESOURCE NETWORK CONNECTION TYPE"/>
                        <xsd:enumeration value="RESOURCE NETWORK CONNECTION INFORMATION"/>
          <!-- Test Specification Model -->
                        <xsd:enumeration value="TEST SPECIFICATION"/>
                        <xsd:enumeration value="TEST SPECIFICATION INFORMATION"/>
          <!-- Transaction Profile Model -->
                        <xsd:enumeration value="TRANSACTION PROFILE"/>
          <!-- Work Alert Model -->
                        <xsd:enumeration value="WORK ALERT"/>
                        <xsd:enumeration value="WORK ALERT DEFINITION"/>
                        <xsd:enumeration value="WORK ALERT INFORMATION"/>
          <!-- Work Calendar Model -->
                        <xsd:enumeration value="WORK CALENDAR"/>
                        <xsd:enumeration value="WORK CALENDAR DEFINITION"/>
                        <xsd:enumeration value="WORK CALENDAR INFORMATION"/>
          <!-- Work Capability Model -->
                        <xsd:enumeration value="WORK CAPABILITY"/>
                        <xsd:enumeration value="WORK MASTER CAPABILITY"/>
                        <xsd:enumeration value="WORK CAPABILITY INFORMATION"/>
          <!-- Work Definition Model -->
                        <xsd:enumeration value="WORK DEFINITION INFORMATION"/>
                        <xsd:enumeration value="WORK DIRECTIVE"/>
                        <xsd:enumeration value="WORK MASTER"/>
          <!-- Work Performance Model -->
                        <xsd:enumeration value="WORK PERFORMANCE"/>
                        <xsd:enumeration value="WORK RESPONSE"/>
                        <xsd:enumeration value="JOB RESPONSE"/>
                        <xsd:enumeration value="JOB RESPONSE LIST"/>
          <!-- Work Record Model -->
                        <xsd:enumeration value="WORK RECORD"/>
                        <xsd:enumeration value="WORK RECORD SPECIFICATION"/>
          <!-- Work Schedule Model -->
                        <xsd:enumeration value="WORK SCHEDULE"/>
                        <xsd:enumeration value="WORK REQUEST"/>
                        <xsd:enumeration value="JOB LIST"/>
                        <xsd:enumeration value="JOB ORDER"/>
          <!-- Workflow Model -->
                        <xsd:enumeration value="WORKFLOW INFORMATION"/>
                        <xsd:enumeration value="WORKFLOW SPECIFICATION"/>
                        <xsd:enumeration value="WORKFLOW SPECIFICATION NODE"/>
                        <xsd:enumeration value="WORKFLOW SPECIFICATION CONNECTION TYPE"/>
          <!-- BatchInformation -->
                        <xsd:enumeration value="BATCH INFORMATION"/>
                        <xsd:enumeration value="MASTER RECIPE"/>
                        <xsd:enumeration value="CONTROL RECIPE"/>
                        <xsd:enumeration value="RECIPE BUILDING BLOCK"/>
                        <xsd:enumeration value="BATCH LIST"/>
          <!-- BatchInformation -->
                        <xsd:enumeration value="BATCH PRODUCTION RECORD"/>
          <!-- GeneralRecipe -->
                        <xsd:enumeration value="GRECIPE INFORMATION"/>
                        <xsd:enumeration value="RESOURCE CONSTAINT LIBRARY"/>
                        <xsd:enumeration value="PROCESS ELEMENT LIBRARY"/>
                        <xsd:enumeration value="GRECIPE"/>
                        <xsd:enumeration value="RESOURCE CONSTRAINT"/>
                        <xsd:enumeration value="PROCESS ELEMENT"/>
          <!-- Confirm BOD -->
                        <xsd:enumeration value="CONFIRM BOD"/>
          <!-- Error Message -->
                        <xsd:enumeration value="ERROR MESSAGE"/>
          <!-- User Extension -->
                        <xsd:enumeration value="Other"/>
                </xsd:restriction>
          </xsd:simpleContent>
        </xsd:complexType>

        <xsd:complexType name = "TransactionNounType">
                <xsd:simpleContent>
                        <xsd:extension base="TransactionNoun1Type">
                                <xsd:attribute name = "OtherValue" type="xsd:string"/>
                        </xsd:extension>
                </xsd:simpleContent>
        </xsd:complexType>

        <xsd:complexType name = "TransactionVerb1Type">
          <xsd:simpleContent>
                <xsd:restriction base="CodeType">
                        <xsd:enumeration value="NOTIFY"/>
                        <xsd:enumeration value="GET"/>
                        <xsd:enumeration value="PROCESS"/>
                        <xsd:enumeration value="CHANGE"/>
                        <xsd:enumeration value="CANCEL"/>
                        <xsd:enumeration value="CONFIRM"/>
                        <xsd:enumeration value="SYNC ADD"/>
                        <xsd:enumeration value="SYNC CHANGE"/>
                        <xsd:enumeration value="SYNC DELETE"/>
                        <xsd:enumeration value="Other"/>
                </xsd:restriction>
          </xsd:simpleContent>
        </xsd:complexType>

        <xsd:complexType name = "TransactionVerbType">
                <xsd:simpleContent>
                        <xsd:extension base="TransactionVerb1Type">
                                <xsd:attribute name = "OtherValue" type="xsd:string"/>
                        </xsd:extension>
                </xsd:simpleContent>
        </xsd:complexType>

<!-- - - - - - - - - - - - - - - - - - - - - -->
<!-- TransactionProfile Transaction Types    -->
<!-- - - - - - - - - - - - - - - - - - - - - -->

  <xsd:complexType name = "GetTransactionProfileType">
    <xsd:sequence>
         <xsd:element name = "ApplicationArea"  type = "TransApplicationAreaType"/>
      <xsd:element name = "DataArea">
         <xsd:complexType>
            <xsd:sequence>
              <xsd:element name = "Get"         type = "TransGetType"/>
              <xsd:element name =  "TransactionProfile"
                                                type = "TransactionProfileType"
                                                minOccurs = "0"
                                                maxOccurs = "unbounded"/>
            </xsd:sequence>
         </xsd:complexType>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name = "releaseID"           type="xsd:normalizedString"     use="required"/>
    <xsd:attribute name = "versionID"           type="xsd:normalizedString"     use="optional"/>
  </xsd:complexType>

  <xsd:complexType name = "ShowTransactionProfileType">
    <xsd:sequence>
         <xsd:element name = "ApplicationArea"  type = "TransApplicationAreaType"/>
      <xsd:element name = "DataArea">
         <xsd:complexType>
            <xsd:sequence>
              <xsd:element name = "Show"        type = "TransShowType"/>
              <xsd:element name = "TransactionProfile"
                                                type = "TransactionProfileType"
                                                minOccurs = "0"
                                                maxOccurs = "unbounded"/>
            </xsd:sequence>
         </xsd:complexType>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name = "releaseID"           type="xsd:normalizedString"     use="required"/>
    <xsd:attribute name = "versionID"           type="xsd:normalizedString"     use="optional"/>
  </xsd:complexType>

</xsd:schema>
```
