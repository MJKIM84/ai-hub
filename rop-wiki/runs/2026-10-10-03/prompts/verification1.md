(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-10-03
- date: 2026-10-10
- run_type: update (갱신)
- 대상: 26. 작업 순서·스케줄링 (G. 계획·최적화)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 세부영역 반영 제안: 4건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

## 입력

### runs/2026-10-10-03/target.json

```json
{
  "run_id": "2026-10-10-03",
  "date": "2026-10-10",
  "weekday": "Sat",
  "run_number": 163,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 26,
    "area_name": "26. 작업 순서·스케줄링",
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
  "selection_rationale": "CLI 지정 run_type=update, area=26"
}
```

### runs/2026-10-10-03/research.json

```json
{
  "run_id": "2026-10-10-03",
  "date": "2026-10-10",
  "run_type": "update",
  "target": {
    "area_no": 26,
    "area_name": "26. 작업 순서·스케줄링",
    "category": "G. 계획·최적화"
  },
  "gaps": [
    "섹션 5. 적용 사례 (현장 유형 명시) — 시작 조건 칸의 'Open-RMF 요청에 마감·선후 필드는 없다'가 공통 최상위 스키마 범위인지 밝혀져 있지 않고, 유형별 description 확장 경로를 다루지 않음. 물류창고 외 현장 유형 사례 없음",
    "섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — Open-RMF 기본 비용이 무엇을 최소화하는지(완료 시각 합 vs 메이크스팬), 누적 용량 제약, 진행 중 동작을 고정하는 재계획 방식이 비어 있음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 — BinaryPriorityScheme 행이 '비용 반영 방식은 미확인'으로 남아 있고, 2026-09-25 이후 rmf_fleet_adapter 변경(2.14.0) 미반영",
    "섹션 8. 대표 연구와 자료(주제 페이지로 분리) — 성능 수치가 모두 원문 미열람이며 2024~2025년 동적·협업 일정 연구가 없음",
    "섹션 11. 열린 질문(주제 페이지로 분리) — oq-019·oq-049 부분 근거 미반영",
    "정정 요청 없음"
  ],
  "research_questions": [
    "일이 계속 새로 들어올 때 무엇을 먼저, 언제 할지 어떻게 정할 것인가? [분류원문]",
    "Open-RMF task_request 스키마의 마감·선후 필드 부재는 공통 최상위 스키마에 한정되는가, 유형별 확장 경로는 무엇인가? (섹션 5·7 겨냥)",
    "Open-RMF 이진 우선순위는 비용 계산에 어떻게 반영되며, 기본 비용은 어떤 지표를 최소화하는가? (섹션 6·7 겨냥)",
    "마감·공용 자원 용량·선택 작업을 제약으로 표현하는 공개 도구와, 진행 중 동작을 보존하며 재계획하는 연구는 무엇인가? (섹션 6·8 겨냥)",
    "oq-019 상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가? (섹션 11 겨냥)",
    "oq-049 제조사가 다른 로봇 플릿 사이의 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 작업 요청 수준에서 표현·집행하는 표준 필드나 공개 구현이 있는가? (섹션 11 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Open-RMF task_request.json 의 공통 최상위 필드는 unix_millis_earliest_start_time·unix_millis_request_time·priority·category·description·labels·requester·fleet_name 의 8개이고 필수는 category·description 뿐이며, 마감 시각이나 다른 작업 ID 를 가리키는 선후 필드는 공통 최상위 스키마에 정의되어 있지 않다.",
      "tag": "사실",
      "source_ids": [
        "ref-125"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "task_request.json properties 8개와 \"required\": [\"category\", \"description\"]. 시각 관련은 earliest_start_time(\"The earliest time that this task may start\")·request_time 뿐이고 deadline·선행 작업 필드 없음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f2",
      "claim": "같은 스키마에서 description 은 그 작업 유형(category)에 대해 플릿이 지원하는 스키마를, priority 는 플릿이 지원하는 우선순위 스키마를 따라야 한다고 설명하며, 최상위에 additionalProperties 제한은 두지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-125"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "description: \"This must match a schema supported by a fleet for the category of this task request.\" priority: \"must match a priority schema supported by a fleet\". 최상위 additionalProperties 키 없음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f3",
      "claim": "공통 최상위 스키마에 마감·선후 필드가 없다는 것이 유형별 description 확장이나 플릿별 우선순위 스키마로 그런 조건을 구현하는 것이 불가능하다는 뜻은 아닐 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-125"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2 의 유형별 description·플릿별 priority 스키마 위임에서 도출한 추론. 검증에서 '사실'을 '추정'으로 강등했다. 확장 필드를 실제로 집행하는 계획기 구현은 확인하지 못했다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f4",
      "claim": "출하 마감이나 다른 작업 완료를 시작 조건으로 쓰려면, 문법상 추가 필드를 넣을 수 있다는 것과 계획기가 그 필드를 집행한다는 것을 구분해 그 확장 계약과 집행 주체를 별도로 명시해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-125"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "외부 조사 메모의 의견. 근거: 스키마는 description 구조를 플릿에 위임할 뿐 집행 주체를 정하지 않는다(ref-125) (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f5",
      "claim": "rmf_task 의 BinaryPriorityScheme.cpp 는 make_low_priority() 에서 nullptr 를, make_high_priority() 에서 BinaryPriority(1) 객체를 돌려주고, make_cost_calculator() 로 BinaryPriorityCostCalculator 를 만든다.",
      "tag": "사실",
      "source_ids": [
        "ref-1484"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "make_low_priority(){ return nullptr; } / make_high_priority(){ return std::make_shared<BinaryPriority>(1); } / make_cost_calculator(){ return std::make_shared<BinaryPriorityCostCalculator>(); } (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "BinaryPriorityCostCalculator 의 valid_assignment_priority() 는 같은 계획 노드 안의 로봇(에이전트) 사이에서 한 로봇이 높은 우선순위 작업을 2개 이상 받았는데 높은 작업을 하나도 받지 않은 로봇이 있으면 위반으로 보고, 같은 로봇의 배정 순서 안에서는 충전 작업을 건너뛴 뒤 낮은 작업 다음에 높은 작업이 오면 위반으로 본다.",
      "tag": "사실",
      "source_ids": [
        "ref-1483"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "STEP 1 \"Checking for validity across agents\": max_priority_count > 1 이고 priority_count 0 인 에이전트가 있으면 false. STEP 2 \"within assignments of an agent\": ChargeBattery 는 continue, prev_priority == nullptr && curr_priority != nullptr 이면 false (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f7",
      "claim": "compute_cost(Node, time_now, check_priority) 는 우선순위 검사가 켜져 있고 배정이 위반이면 비용을 _priority_penalty × (g + h) 로, 그렇지 않으면 g + h 로 계산한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1483"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "if (check_priority) { if (!valid_assignment_priority(n)) return _priority_penalty * (g + h); } return g + h; 벌점 계수는 생성자 인자 priority_penalty (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "이 우선순위 처리는 납기 제약을 직접 검사하는 코드가 아니라 배정 비용에 벌점을 곱하는 방식이므로, 높은 우선순위를 마감 보장으로 해석해서는 안 되며 로봇 사이 배분 조건이 있어 단순한 선입선출 정렬로 설명해서도 안 된다.",
      "tag": "의견",
      "source_ids": [
        "ref-1483",
        "ref-125"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "외부 조사 메모의 의견. 근거: cost.cpp 에 deadline 관련 검사 없음, 공통 요청 스키마에도 마감 필드 없음(ref-125). 같은 프로젝트 자료라 독립 교차 확인 아님 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f9",
      "claim": "BinaryPriorityCostCalculator 의 기본 실비용(g)은 각 일반 작업의 완료 시각(finish_state 시각)에서 그 요청의 가장 이른 시작 시각을 뺀 값을 모든 로봇·모든 배정에 걸쳐 합산한 값이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1483"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "compute_g_assignment: finish_state().time() - booking()->earliest_start_time() 를 초 단위로; compute_g: for agent / for assignment 로 cost += 합산 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "같은 계산기는 충전 작업(ChargeBattery) 배정 자체의 비용을 0 으로 계산한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1483"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "compute_g_assignment 의 ChargeBattery::Description 분기: \"return 0.0; // Ignore charging tasks in cost\" (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "충전 작업 자체의 비용은 0 이지만, 충전 때문에 같은 로봇의 뒤 작업 완료가 늦어지면 그 작업의 비용(완료 시각 − 가장 이른 시작 시각)은 커질 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1483"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f9·f10 의 비용 정의에서 도출한 추론. 코드에 이 효과를 직접 설명한 주석은 없다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "이 비용은 작업별 (완료 시각 − 가장 이른 시작 시각)의 합이므로, Dai 외가 정의한 메이크스팬(Makespan, 차고지 복귀를 포함한 모든 로봇의 총 작업 시간 중 최댓값)이나 납기 지연 합과 같은 지표라고 부르면 안 된다.",
      "tag": "의견",
      "source_ids": [
        "ref-1483",
        "ref-1486"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Dai 외 §III: \"minimize the makespan, which is the maximum total working time among all agents\", 각 로봇은 작업 후 차고지(depot)로 복귀. rmf_task 비용은 compute_g 합산. 사용자 지정 계산기를 쓴 경우로 일반화하지 않는다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "OR-Tools CP-SAT 스케줄링 문서는 구간 변수, 실행 여부를 리터럴로 정하는 선택 구간, 구간 사이 시간 관계, 겹침 금지(NoOverlap)에 더해, 구간별 수요의 합이 용량 프로필을 넘지 않게 하는 누적 용량(Cumulative) 제약을 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-379"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "scheduling.md 절: Interval variables / Optional intervals / Time relations between intervals / NoOverlap constraint / \"Cumulative constraint with min and max capacity profile\". 구간·선택 구간·선후·겹침 금지는 기존 6절에 있음(기존 내용 확인), 누적 용량이 새 내용 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f14",
      "claim": "이 표현으로 '이전 작업 종료 뒤 시작'(시간 관계), '도크는 한 번에 한 작업'(겹침 금지), '작업대 동시 사용량은 용량 이하'(누적 용량)를 서로 다른 제약으로 작성할 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-379"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f13 의 제약 종류를 창고 시나리오에 대응시킨 추론. 문서의 예제는 일반 스케줄링 예제이며 로봇·도크 사례가 아니다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f15",
      "claim": "Tuck 외(2024)의 동적 다중 로봇 작업 배정 정식화는 Definition 6(완료된 작업)에서 내려놓기 동작이 마감 전에 일어나야 작업을 완료한 것으로 보아, 마감을 필수 완료 조건으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1485"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§3 Definition 6 Completed task: \"the drop action must be before the deadline\", 픽업 이동 전 시각은 시작 시각 이상. 초록: 작업은 \"a strict deadline\" 을 가진다(arXiv v1, 2024-03-18)",
      "as_of": "2024-03-18",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f16",
      "claim": "마감을 반드시 지킬 조건으로 둘지, 어겼을 때 비용을 주는 조건으로 둘지는 목적함수와 제약식을 나눠 설계해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-379",
        "ref-1485"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "외부 조사 메모의 의견. 근거: CP-SAT 은 제약과 목적을 따로 둘 수 있고(ref-379), Tuck 외는 마감을 필수 조건으로 둔 예(ref-1485). OR-Tools 가 바로 쓸 수 있는 로봇 스케줄러라는 뜻은 아니다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f17",
      "claim": "Tuck 외(2024)는 마감이 있는 작업이 온라인으로 들어오고 로봇이 여러 작업을 동시에 실을 수 있는 동적 다중 로봇 작업 배정(Multi-Robot Task Allocation, MRTA)을 다루며, Definition 9 의 갱신 계획(Updated plan)은 각 로봇의 과거 동작과 현재 동작을 바꾸지 않은 채 새 작업을 반영하도록 정의한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1485"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§3 Definition 9 Updated plan: 이전 계획과 같은 접두부를 유지하며 \"past actions and the current action are unchanged\". §4.3 SavePastState() 로 과거 action point 를 상수로 고정",
      "as_of": "2024-03-18",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "같은 연구는 이론 모듈로 만족 가능성(Satisfiability Modulo Theories, SMT) 해법기의 push·pop 기능으로 앞선 풀이 정보를 유지하는 증분 풀이를 쓰지만, 증분·비증분 풀이의 시간 성능은 해법기와 배치 크기에 따라 크게 달랐다(Z3-BV 와 Bitwuzla-BV 비교).",
      "tag": "사실",
      "source_ids": [
        "ref-1485"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.3: push·pop 으로 \"retain information about previous solves\". §6.2 RQ2(200 작업·20 에이전트, 배치 1·10): \"depend greatly on the solver and batch size\" — Z3-BV 는 작은 배치의 증분 풀이에서, Bitwuzla-BV 는 큰 배치의 비증분 풀이에서 우세. 검증에서 '인코딩'을 '배치 크기'로 정정",
      "as_of": "2024-03-18",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "이를 참고하면 긴급 작업 삽입 정책을 '현재 동작 고정'과 '아직 실행하지 않은 구간의 재배열'로 나눠 기술할 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1485"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f17 의 갱신 계획 정의에서 도출. 논문은 새 작업마다 진행 중 물리 동작을 중단하지 않으며, 불확실한 이동 시간을 포함한 실행 성능 보장으로 넓히지 않는다",
      "as_of": "2024-03-18",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f20",
      "claim": "Dai 외(2025)는 탐색·구조 같은 협업 과제를 모사한 계산 실험에서, 배정된 로봇 연합의 능력 벡터 합이 작업 요구를 충족해야 작업을 시작할 수 있고 모든 배정 로봇이 실행 기간 내내 작업 위치에 함께 있어야 하며 먼저 도착한 로봇은 나머지가 올 때까지 기다리는 작업을 모델링한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1486"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§III: 시작 조건 c_L ⪰ q_mj, \"all assigned agents must be present at the task location for the entire execution duration ... they must wait until all collaborating agents are present.\" 정규화된 2D 영역의 계산 실험이며 실제 현장 검증 아님. 협업 조립은 동기 예시로만 등장",
      "as_of": "2025",
      "site_type": "기타",
      "flow_item": "시작 조건"
    },
    {
      "id": "f21",
      "claim": "이런 협업 작업에서는 개별 로봇이 빨리 도착해도 다른 팀원이 늦으면 작업 시작이 늦어지므로, 개별 로봇의 빠른 도착만으로 전체 종료 시간이 줄지는 않을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1486"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f20 의 시작·대기 조건에서 도출한 추론. 검증에서 '사실'을 '추정'으로 강등했다(원문은 도착 동기화로 대기 시간을 줄여야 한다고만 서술)",
      "as_of": "2025",
      "site_type": "기타",
      "flow_item": "제약"
    },
    {
      "id": "f22",
      "claim": "이 사례를 이용하면 일정 설명에서 도착 동기화, 공동 작업 시간, 다음 작업으로의 이동을 구분해 적을 수 있다.",
      "tag": "의견",
      "source_ids": [
        "ref-1486"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "외부 조사 메모의 의견. 실제 창고의 피킹–포장 인계 구현과 같다고 주장하지 않는다",
      "as_of": "2025",
      "site_type": "기타",
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "Dai 외(2025)는 강화학습(Reinforcement Learning, RL)으로 이종 로봇이 다음 작업을 분산적으로 고르는 협업 일정 정책을 학습하고, 계산 실험에서 최대 150 에이전트·500 작업·5종 능력 조건까지 다뤘다고 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1486"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"scale up to 150 agents and 500 tasks, with up to 5 skills\". 표 IV 대규모 실험(km=500, kn=150). 저자는 MIP 정확 해법기·휴리스틱과 비슷하거나 낫고 두 자릿수 이상 빠르다고 보고(저자 실험, 독립 재현 미확인)",
      "as_of": "2025",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "Open-RMF TaskPlanner.hpp 의 Options 주석은 탐욕 방식은 최적성을 보장하지 않지만 더 빨리 풀 수 있고, A* 기반 방식은 최적성을 보장하지만 풀이에 더 오래 걸릴 수 있다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-377"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Options(greedy, interrupter, finishing_request) 주석: \"Optimality is not guaranteed but the solution time may be faster. If false, an A* based approach ... which guarantees optimality but may take longer to solve.\" 기존 6절 분리 페이지에 같은 내용 있음(기존 내용 확인) (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "Dai 외의 강화학습 방식과 Open-RMF 계획기는 목적·모델·평가 환경이 달라, 규모나 풀이 시간만으로 우열을 정하기보다 실행 가능한 일정 비율과 목적값을 같은 조건에서 비교하는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1486",
        "ref-377"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "외부 조사 메모의 의견. Dai 외는 메이크스팬 최소화, rmf_task 기본 계산기는 (완료 − 가장 이른 시작) 합. 두 접근을 직접 비교한 실험은 확인하지 못했다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "rmf_fleet_adapter 2.14.0(2026-09-26) 변경 이력은 단계 건너뛰기 요청의 단계 키 수정(#543)과 EasyTrafficLight 의 누적 지연 계산 수정(#524)을 포함한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1487"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "CHANGELOG.rst 2.14.0 (2026-09-26): \"Fix phase key for skip requests (#543)\", \"Fix cumulative delay calculation in EasyTrafficLight (#524)\". 새 납기 최적화나 진행 중 작업 선점 기능을 뜻하지는 않는다",
      "as_of": "2026-09-26",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f27",
      "claim": "일정의 예외 조정과 지연 기반 추정에 의존하는 구현은 사용하는 Open-RMF 패키지 버전을 함께 기록하는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1487"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "외부 조사 메모의 의견. 근거: 2.14.0 에서 건너뛰기 요청 키와 누적 지연 계산이 수정됨(f26)",
      "as_of": "2026-09-26",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "oq-019 부분 답변: 이진 우선순위의 표현과 비용 벌점 구현은 공개되어 있지만, 납기·운송 마감을 이진 값으로 바꾸고 진행 중 작업을 재정렬하는 현장 설계는 확인하지 못해 질문을 닫을 수 없다.",
      "tag": "의견",
      "source_ids": [
        "ref-125",
        "ref-1483",
        "ref-1484"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "근거: f5~f7(이진 우선순위 표현·벌점), f1(마감 필드 없음). 재정렬 현장 설계·사례는 이번 자료에서 찾지 못함 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "oq-049 부분 답변: 공통 task_request 스키마에는 선행 작업 ID 가 없고 유형별 description 확장 경로만 있어, 이 경로만으로 제조사 간 선후 집행이 구현되었다고 볼 수 없으며 범용 표준 필드나 완성된 공개 구현은 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-125"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "근거: f1·f2. 확인한 자료 범위(task_request.json) 안의 판단이며 다른 Open-RMF 작업 유형 스키마 전체는 이번에 대조하지 않았다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "완료·인계"
    }
  ],
  "sources": [
    {
      "id": "ref-125",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_request.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 작업 요청 JSON 스키마. 최상위 필드 8개(가장 이른 시작 시각·요청 시각·우선순위·category·description·라벨·요청자·플릿 이름) 중 category·description 이 필수이며 마감·선후 필드는 없다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_request.json",
      "source_unopened": false
    },
    {
      "id": "ref-377",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 작업 계획기 헤더. 탐욕 방식(최적성 미보장, 더 빠를 수 있음)과 A* 방식(최적성 보장, 더 오래 걸릴 수 있음) 선택 옵션, 배정별 가장 이른 시작 시각을 주석으로 정한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_task/main/rmf_task/include/rmf_task/TaskPlanner.hpp",
      "source_unopened": false
    },
    {
      "id": "ref-379",
      "org": "Google (google/or-tools GitHub)",
      "title": "OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver)",
      "published": null,
      "url": "https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "CP-SAT 스케줄링 문서 원본. 구간 변수, 선택 구간, 구간 사이 시간 관계, 겹침 금지, 최소·최대 용량 프로필의 누적 제약을 다룬다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/google/or-tools/stable/ortools/sat/docs/scheduling.md",
      "source_unopened": false
    },
    {
      "id": "ref-1483",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_task — rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 이진 우선순위 비용 계산기 구현. 작업별 (완료 시각 − 가장 이른 시작 시각) 합을 비용으로 쓰고 충전 작업은 0 으로 두며, 우선순위 배분 위반이면 비용에 벌점 계수를 곱한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_task/main/rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp",
      "source_unopened": false
    },
    {
      "id": "ref-1484",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_task — rmf_task/src/rmf_task/BinaryPriorityScheme.cpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityScheme.cpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 이진 우선순위 체계 구현. 낮은 우선순위는 nullptr, 높은 우선순위는 BinaryPriority(1) 로 만들고 BinaryPriorityCostCalculator 를 비용 계산기로 돌려준다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_task/main/rmf_task/src/rmf_task/BinaryPriorityScheme.cpp",
      "source_unopened": false
    },
    {
      "id": "ref-1485",
      "org": "Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (UC Berkeley, Toyota Motor North America)",
      "title": "SMT-Based Dynamic Multi-Robot Task Allocation",
      "published": "2024-03-18",
      "url": "https://arxiv.org/html/2403.11737v1",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "마감이 있는 작업이 온라인으로 들어오는 용량 있는 로봇의 동적 작업 배정을 SMT 증분 풀이로 다룬 arXiv 프리프린트(v1). 과거·현재 동작을 보존하는 갱신 계획을 정의하고, 증분 풀이 이득이 해법기·배치 크기에 따라 다름을 실험으로 보였다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1486",
      "org": "Dai, W., Rai, U., Chiun, J., Cao, Y., & Sartoretti, G.",
      "title": "Heterogeneous Multi-robot Task Allocation and Scheduling via Reinforcement Learning",
      "published": "2025",
      "url": "https://marmotlab.org/publications/73-RAL2025-HetMRTA.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "모든 배정 로봇이 모여야 시작하는 협업 작업에서 이종 로봇의 배정·일정을 강화학습으로 정하고 메이크스팬을 최소화하는 연구(저자 5명). 게재지(IEEE RA-L 2025)는 파일명 기준이며 PDF 본문에서는 확인하지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1487",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0)",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 태그 2.14.0 변경 이력. 2026-09-26 판에 단계 건너뛰기 요청 키 수정(#543)과 EasyTrafficLight 누적 지연 계산 수정(#524)이 들어 있다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
      "sections": [
        "5",
        "6",
        "7",
        "8",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 5 — 시작 조건 칸 문장을 공통 최상위 스키마 범위로 한정(f1)하고 description·priority 의 플릿 스키마 위임(f2), 확장 가능성(f3, 추정), 확장 계약·집행 주체 명시 필요(f4, 의견)를 제약 칸에 반영; 물류창고 표와 별도로 '현장 유형: 기타(탐색·구조 모사 계산 실험)' 협업 사례를 추가(f20 사실, f21 추정, f22 의견) / 섹션 6(주제 페이지 2026-09-25-area14-s6 요약) — 플릿 안 일정 계획에 기본 비용 정의(f9·f10, f11 추정)와 메이크스팬과의 구분(f12, 의견), 제약 프로그래밍에 누적 용량 제약(f13; 구간·선택 구간·선후·겹침 금지는 기존 내용 확인)과 창고 제약 대응(f14 추정)·마감의 필수/비용 설계 구분(f15·f16), 온라인 재계획에 Tuck 외 갱신 계획·증분 풀이(f17·f18, f19 추정) / 섹션 7 — BinaryPriorityScheme 행의 '비용 반영 방식은 미확인'을 f5~f7 로 교체하고 마감 보장 해석 금지(f8, 의견), Open-RMF 작업 요청 스키마 행 문구를 공통 최상위 필드 기준으로(f1·f2), rmf_fleet_adapter 2.14.0 변경 이력 행 추가(f26, f27 의견) / 섹션 8(주제 페이지 2026-09-25-area14-s8 요약) — Tuck 외(f17·f18), Dai 외(f23) 추가와 접근법 비교 방식(f24·f25; f24 의 탐욕·A* 설명은 기존 6절 분리 페이지 내용 확인) / 섹션 11(주제 페이지 2026-09-25-area14-s11) — oq-019 부분 근거(f28), oq-049 부분 근거(f29), 새 질문 3건. 두 열린 질문 모두 해결 제안 없음."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "메이크스팬",
      "term_en": "Makespan",
      "definition": "작업 집합 전체를 끝내는 데 걸린 시간으로, 다중 로봇 일정에서는 보통 모든 로봇 가운데 가장 늦게 일을 마친 로봇의 종료 시각(또는 총 작업 시간)을 뜻한다."
    },
    {
      "term_ko": "이론 모듈로 만족 가능성",
      "term_en": "Satisfiability Modulo Theories (SMT)",
      "definition": "정수·비트벡터 산술 같은 배경 이론 위에서 논리식을 만족하는 값의 존재를 판정하는 문제와 그 해법기로, 일정·배정 제약을 논리식으로 풀 때 쓴다."
    }
  ],
  "open_questions_new": [
    "이진 우선순위에서 높은 작업이 계속 들어올 때 낮은 작업의 무한 대기를 막는 공개 정책이 있는가? | 관련 영역: 26. 작업 순서·스케줄링, 25. 작업 배정 — MRTA | 근거: f6 | 종류: 일반",
    "제조사별 예상 완료 시간의 오차를 고려해 출하 마감 대비 여유 시간을 얼마나 두는가? | 관련 영역: 26. 작업 순서·스케줄링, 20. 로봇·제조사 관제 연동 | 근거: f16 | 종류: 일반",
    "작업 완료 시각 합, 납기 지연 합, 계획 변경량을 함께 최적화할 때 현장별 가중치를 어떻게 검증하는가? | 관련 영역: 26. 작업 순서·스케줄링, 39. 운영 성과 측정·개선 | 근거: f12 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 8,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-03/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.",
      "ref-1486(Dai 외): 게재지 IEEE Robotics and Automation Letters 2025 는 PDF 파일명(73-RAL2025-HetMRTA) 기준이며 본문에서 확인하지 못함 — published 는 '2025'로만 둠, 동료심사 여부 미확인이라 신뢰도 medium",
      "f3·f29: 유형별 description 확장으로 마감·선후 조건을 실제 집행하는 Open-RMF 구현은 확인하지 못함(다른 작업 유형 스키마 전체는 대조하지 않음)",
      "f11: 충전 작업이 뒤 작업 비용을 늘리는 효과는 코드 정의에서 도출한 추론이며 실행 결과로 확인하지 않음",
      "f21: '개별 로봇의 빠른 도착만으로 전체 종료 시간이 줄지 않는다'는 원문 직접 진술이 아니라 추론(검증에서 사실→추정 강등)",
      "f23: Dai 외 성능 비교(MIP·휴리스틱 대비)는 저자 실험이며 독립 재현 미확인",
      "oq-019·oq-049: 부분 근거만 확보, 재정렬 현장 설계와 제조사 간 선후 집행의 공개 구현은 미확인",
      "교차 확인 0건: rmf_task 헤더·구현·스키마는 같은 프로젝트 자료라 독립 교차 확인으로 세지 않음"
    ],
    "scope_violations": [
      "f20~f23: Dai 외는 탐색·구조를 모사한 계산 실험이라 물류창고 사례가 아님 — 5절에는 현장 유형 '기타'로 따로 두고 창고 피킹–포장 인계와 같다고 쓰지 않는다",
      "f13·f14·f16: OR-Tools 는 일반 스케줄링 도구이며 로봇 관제용 스케줄러가 아님 — 제약 표현 근거로만 쓴다"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 5
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 5건(ref-1483~ref-1487, 예약 구간 ref-1483~ref-1512 안), 재사용 3건(ref-125 task_request.json, ref-377 TaskPlanner.hpp, ref-379 OR-Tools scheduling.md). 메모의 n3(BinaryPriorityScheme.cpp)은 기존 ref-390(BinaryPriorityScheme.hpp)과 다른 파일이라 새 id 로 등록. 8개 출처 모두 원문 대조 확인(GitHub 파일은 github_raw, 논문 2건은 webfetch). 검증 수정 반영: (1) Tuck 외 증분 풀이 이득의 조건을 '해법기와 배치 크기'로 정정(f18), (2) '공통 필드의 부재가 확장 구현의 불가능을 뜻하지 않는다'를 추정으로 분리(f3), (3) Dai 외 '빠른 도착만으로 전체 종료 시간이 줄지 않는다'를 추정으로 분리(f21), 앞부분은 §III 사실(f20), (4) 이진 우선순위 배분 조건을 같은 계획기 안 로봇 사이 조건과 같은 로봇 안 순서 조건으로 정정하고 벌점식 _priority_penalty × (g + h) 명시(f6·f7), (5) TaskPlanner 의 A* 최적성 보장 명시(f24), (6) 메이크스팬을 Dai 외 정의(차고지 복귀 포함 모든 로봇의 최대 총 작업 시간)로 맞춤(f12), (7) task_request.json 최상위 필드 8개·필수 2개·additionalProperties 없음 명시(f1·f2), (8) Dai 외 게재지 미확인·published 2025·저자 5명(ref-1486), (9) 기존 id 연결. 열린 질문은 해결 제안 없이 oq-019(f28)·oq-049(f29) 부분 근거만 냈다. 메모의 출처 집계 문장('원문 열람 8/8')은 검증 결과와 일치. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md

```markdown
---
title: "26. 작업 순서·스케줄링"
type: area
category: "G. 계획·최적화"
area_no: 26
related_areas: [20, 23, 24, 25, 27, 28, 31, 35, 39]
tags: [작업 순서, 스케줄링, 주문 배치, 선후 제약, 시간창, Open-RMF]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-006, ref-110, ref-117, ref-125, ref-133, ref-134, ref-376, ref-377, ref-378, ref-379, ref-380, ref-381, ref-382, ref-383, ref-384, ref-385, ref-386, ref-387, ref-388, ref-389, ref-390]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [G. 계획·최적화](index.md) › 26. 작업 순서·스케줄링

# 26. 작업 순서·스케줄링

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

## 3. 왜 중요한가

주문 피킹은 대부분 창고에서 가장 노동집약적이고 비용이 큰 활동으로 알려져 있으며, 2007년 문헌 검토는 그 비용을 창고 운영비의 최대 55%로 추정했다(그 문헌 검토가 제시한 단일 출처 추정치이며 독립 교차 확인은 없다). [사실][^ref-380] 같은 검토는 배치·구역화·경로·보관 배정을 피킹의 주요 설계·통제 결정 문제로 다룬다. [사실][^ref-380]

이커머스 창고는 주문 줄이 몇 개뿐인 시간 임박 주문을 대량으로 처리해야 하며, 로봇·자동 피킹 작업대 같은 자동화와 함께 동적 주문 처리·배치·구역화·분류 같은 운영 적응이 쓰인다고 2019년 조사 논문이 정리한다. [사실][^ref-382]

순서 결정만으로 필요한 자원이 달라질 수 있다는 보고도 있다. 랙 이동 로봇 창고에서 작업대의 주문 배치·순서와 랙 도착 순서를 함께 정한 2017년 연구는, 저자 계산 실험(원문 미열람, 독립 재현 미확인)에서 최적화된 주문 처리가 현장에서 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다고 보고했다. [사실][^ref-381]

분류 원문의 질문에 비추어 보면, 연구들은 피킹 작업대의 순서를 정할 때 뒤 공정(통합·포장)의 주문 완료 시간과 작업자 대기를 목적에 넣는 방식으로 대기를 줄이려 하므로, ROP 의 순서 결정도 포장대 도착 순서를 기준 제약으로 삼는 형태가 될 것으로 보인다. 다만 국내 연구는 총 주문 처리 시간을 피킹 시간이 결정했다고 보고하므로 포장 쪽 동기화만으로 전체 시간이 줄어든다고 볼 수는 없고, 로봇 운반을 포함한 국내 현장 검증도 없다. [추정][^ref-385][^ref-381][^ref-387]

## 4. 핵심 개념과 용어

작업 순서를 다루려면 무엇을 묶고, 무엇이 먼저이며, 언제까지 해야 하는지를 표현하는 말이 필요하다.

자세한 내용은 주제 페이지 [26. 작업 순서·스케줄링 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area14-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹 → 포장 → 출하

**시나리오:** 랙 이동 로봇 작업대의 피킹 순서를 포장대 도착에 맞추고 출하 마감이 임박한 주문을 끼워 넣기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 시스템이 주문 줄이 적은 시간 임박 주문을 연속으로 내린다. [사실][^ref-382] 긴급 주문을 Open-RMF 요청으로 보낼 때 시각·순서 관련 필드로는 가장 이른 시작 시각과 우선순위를 두고, 마감 시각이나 다른 작업과의 선후 필드는 없다. [사실][^ref-125] |
| 작업 대상 | 로봇이 작업대로 옮기는 랙과 주문별 빈, 풋월의 주문 칸 [사실][^ref-381][^ref-385] |
| 수행 자원 | 랙 이동 로봇, 작업대 피커, 포장 작업자. 복수 포장대와 피킹-패킹 전환 정책(작업자가 피킹과 포장 사이를 옮겨 감)의 작업자 스케줄링을 다룬 국내 연구가 있다(2025, 결과 수치 미확인). [사실][^ref-388] |
| 제약 | 랙 도착 → 피킹 → 주문별 통합 → 포장의 선후가 있고, 배치·구역 피킹 뒤에는 주문별 통합이 필요하다. [사실][^ref-381][^ref-385] 마감 필드가 없으므로 긴급 작업을 끼워 넣고 대기 작업을 재정렬하는 규칙은 ROP 쪽에서 따로 정해야 할 것으로 보인다. [추정][^ref-125][^ref-390] |
| 완료·인계 | 한 주문의 물품이 풋월 칸에 모두 모여야 포장으로 넘어간다. [사실][^ref-385] 피킹 로봇 완료 뒤 운반 로봇 출발처럼 제조사가 다른 플릿 사이 인계는 ROP 가 작업 흐름 수준에서 관리해야 할 것으로 보인다. [추정][^ref-376][^ref-125] |
| 예외·성과 | 빈 방출 순서가 맞지 않으면 포장 작업자가 유휴 대기한다. [사실][^ref-385] 편의점 물류센터 레이아웃 기준 국내 연구는 배치 피킹이 분배·포장 시간을 줄였지만 총 주문 처리 시간은 피킹 시간이 결정했다고 보고했다(2024). [사실][^ref-387] |

다음은 설명을 위한 가상의 시나리오이다. 이 영역이 관여하는 칸은 주로 제약과 완료·인계다. 작업대 앞의 랙 순서는 뒤쪽 풋월과 포장대가 기다리지 않도록 정해져야 하고, 긴급 주문이 들어오면 이미 대기 중인 작업을 어디까지 밀어낼지 정해야 한다.

출하 단계까지 넓히면 피킹과 분류를 배송 요구에 맞춰 동기화하는 문제가 된다. 피킹·분류가 어긋나면 긴급 품목이 빠져 추가 피킹이 생긴다는 문제 제기가 있다. [사실][^ref-386]

## 6. 대표 접근법과 기술

앞의 시나리오에서 순서를 정하는 방법은 크게 여섯 갈래로 연구되어 있다.

자세한 내용은 주제 페이지 [26. 작업 순서·스케줄링 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area14-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

위 접근법을 현장 시스템에 옮길 때 참조하는 표현 형식과 도구는 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| B2MML 공통 스키마 Dependency1Type | 표준 | 두 요소 사이 실행 의존(선후·병행 금지·시작 후 간격 등) 표현. 창고 물류 적용 사례는 미확인 [사실] | [^ref-117] |
| Open-RMF 작업 요청 스키마(task_request.json) | 오픈소스 | 가장 이른 시작 시각·우선순위 필드, 마감·선후 필드 없음 [사실] | [^ref-125] |
| Open-RMF 작업 V2 | 오픈소스 | 작업을 단계의 연쇄·조합으로 구성 [사실] | [^ref-110] |
| Open-RMF 디스패처 | 오픈소스 | 입찰로 플릿 선정, 평가기 설정 가능 [사실] | [^ref-376][^ref-378] |
| Open-RMF rmf_task TaskPlanner | 오픈소스 | 플릿 안 일정 계획, 충전 작업 삽입, 탐욕·A* 선택 [사실] | [^ref-377] |
| Open-RMF BinaryPriorityScheme | 오픈소스 | 높음·낮음 두 단계 우선순위, 낮음은 현재 nullptr 반환. 비용 반영 방식은 미확인 [사실] | [^ref-390] |
| OR-Tools CP-SAT | 오픈소스 | 구간 변수·겹침 금지·선택 구간·선후 부등식으로 스케줄링 표현 [사실] | [^ref-379] |

## 8. 대표 연구와 자료

6절의 접근법을 뒷받침하는 연구다. 성능 수치는 모두 저자 실험 결과이며 이 위키가 원문을 열지 못했다.

자세한 내용은 주제 페이지 [26. 작업 순서·스케줄링 — 대표 연구와 자료](../../topics/2026/2026-09-25-area14-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

작업 순서에서 ROP 의 몫은 마감과 운송 계획을 정하는 일이 아니라, 받은 제약을 현장 작업의 순서로 바꾸고 플릿 사이를 맞추는 일에 가까울 것으로 보인다. [추정][^ref-125][^ref-386]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 가장 이른 시작 시각·우선순위·배송 요구를 작업 제약으로 받아 현장 작업 순서에 반영 [추정][^ref-125][^ref-386] | 연계 대상: 출하 마감 시각의 결정(WMS 등) [추정][^ref-125] |
| 거점 간 운송 | 운송 마감에 맞춘 긴급 작업 삽입·대기 작업 재정렬 규칙 [추정][^ref-125][^ref-390] | 연계 대상: 배송 배차·운송 계획(TMS 등) [추정][^ref-386] |
| 로봇 자체 지능·제어 | 제조사가 다른 플릿 사이의 선후·동기화(예: 피킹 로봇 완료 뒤 운반 로봇 출발) [추정][^ref-376][^ref-125][^ref-117] | 연계 대상: 로봇의 주행·로컬 회피(분류 원문 19장 기준) |

Open-RMF 의 배정은 플릿 단위 입찰과 플릿 안 일정 계획으로 이루어지고 요청 스키마에 작업 간 선후 필드가 없으므로, 플릿 사이 선후는 ROP 가 작업 흐름 수준에서 관리해야 할 것으로 보인다(공개 구현은 찾지 못했다). [추정][^ref-376][^ref-125][^ref-117] 이 경계는 제품 전략에 따라 이동할 수 있으며 자세한 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

작업 순서는 배정·경로·자원 계획과 얽혀 있어 다음 영역과 함께 읽어야 한다.

- [25. 작업 배정 — MRTA](task-allocation-mrta.md) — 시간·순서 제약이 있는 배정 분류와 Open-RMF 입찰 기반 배정을 다룬다. [사실][^ref-383][^ref-376]
- [27. 다중 로봇 경로·교통 관리 — MAPF](multi-robot-path-and-traffic-management-mapf.md) — 선후 제약 MAPF 와 온라인 픽업·배송처럼 순서와 경로가 함께 풀린다. [사실][^ref-389][^ref-006]
- [28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) — 플릿 일정에 충전 작업을 끼워 넣는 결정이 순서에 영향을 준다. [사실][^ref-377]
- [23. 업무 시스템 연동](../integration/business-system-integration.md) — 출고 우선순위·시작 시각을 상위 시스템에서 받는 쪽에 가까울 것으로 보인다(oq-019). [추정][^ref-125][^ref-386]
- [24. 작업·워크플로 모델링](task-and-workflow-modeling.md) — B2MML 의존 유형으로 공정 선후를 표현한다(oq-013). [사실][^ref-117]
- [35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md) — 순서 최적화가 필요한 로봇 대수를 바꾼다는 저자 실험이 있다. [사실][^ref-381]
- [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) — 포장 작업자 대기·주문 완료 시간을 성과 지표로 쓰는 문제와 이어진다. [사실][^ref-385]
- [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md) — 제조사가 다른 플릿 사이 선후를 요청 수준에서 표현할 수단이 필요하다. [추정][^ref-125]
- [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md) — 피킹·포장 작업자 배치와 대기가 순서 결정과 맞물린다. [사실][^ref-388]

## 11. 열린 질문

아래 질문은 이번 조사로 근거가 늘었지만 답을 확인하지 못한 것이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [26. 작업 순서·스케줄링 — 열린 질문](../../topics/2026/2026-09-25-area14-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [26. 작업 순서·스케줄링](task-sequencing-and-scheduling.md) — 영역 심화: 섹션 3~11 신규 작성(4·6·8·11절은 주제 페이지로 분리), 2차 수정 지시 4건 반영(9절 경계 칸, 10절 태그, 5절 시작 조건·제약 칸) (실행 2026-09-25-34)
- 2026-09-25 · 생성 · [26. 작업 순서·스케줄링 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area14-s6.md) — 자동 분리: 14. 작업 순서·스케줄링 의 "6. 대표 접근법과 기술" 절(1,504자)을 옮겼다 (실행 2026-09-25-34)
- 2026-09-25 · 생성 · [26. 작업 순서·스케줄링 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area14-s4.md) — 자동 분리: 14. 작업 순서·스케줄링 의 "4. 핵심 개념과 용어" 절(985자)을 옮겼다 (실행 2026-09-25-34)
- 2026-09-25 · 생성 · [26. 작업 순서·스케줄링 — 대표 연구와 자료](../../topics/2026/2026-09-25-area14-s8.md) — 자동 분리: 14. 작업 순서·스케줄링 의 "8. 대표 연구와 자료" 절(904자)을 옮겼다 (실행 2026-09-25-34)
- 2026-09-25 · 생성 · [26. 작업 순서·스케줄링 — 열린 질문](../../topics/2026/2026-09-25-area14-s11.md) — 자동 분리: 14. 작업 순서·스케줄링 의 "11. 열린 질문" 절(865자)을 옮겼다 (실행 2026-09-25-34)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-25 (원문 미열람)
[^ref-110]: Open Robotics, Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-25
[^ref-117]: MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd, 접근일 2026-09-25
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25
[^ref-376]: Open Robotics, Tasks in RMF (task) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task.html, 접근일 2026-09-25
[^ref-377]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp, 접근일 2026-09-25
[^ref-378]: Open Robotics (open-rmf), rmf_ros2 — rmf_task_ros2/include/rmf_task_ros2/Dispatcher.hpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/include/rmf_task_ros2/Dispatcher.hpp, 접근일 2026-09-25
[^ref-379]: Google (google/or-tools GitHub), OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver), 미확인, https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md, 접근일 2026-09-25
[^ref-380]: de Koster, R., Le-Duc, T., & Roodbergen, K. J., Design and control of warehouse order picking: A literature review, 2007, https://pure.eur.nl/en/publications/design-and-control-of-warehouse-order-picking-a-literature-review/, 접근일 2026-09-25 (원문 미열람)
[^ref-381]: Boysen, N., Briskorn, D., & Emde, S., Parts-to-picker based order processing in a rack-moving mobile robots environment, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758, 접근일 2026-09-25 (원문 미열람)
[^ref-382]: Boysen, N., de Koster, R., & Weidinger, F., Warehousing in the e-commerce era: A survey, 2019, https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/, 접근일 2026-09-25 (원문 미열람)
[^ref-383]: Nunes, E., Manner, M., Mitiche, H., & Gini, M., A taxonomy for task allocation problems with temporal and ordering constraints, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0921889016306157, 접근일 2026-09-25 (원문 미열람)
[^ref-385]: Boysen, N., Stephan, K., & Weidinger, F., Manual order consolidation with put walls: the batched order bin sequencing problem, 2019, https://www.sciencedirect.com/science/article/pii/S2192437620300315, 접근일 2026-09-25 (원문 미열람)
[^ref-386]: Jiang, M., & Huang, G. Q., Intralogistics synchronization in robotic forward-reserve warehouses for e-commerce last-mile delivery, 2022, https://www.sciencedirect.com/science/article/abs/pii/S1366554522000175, 접근일 2026-09-25 (원문 미열람)
[^ref-387]: 신희철, 이강현, 방선호, 신광섭(한국빅데이터학회 학회지), 물류센터 생산성 향상을 위한 피킹스케줄링 문제에 관한 연구, 2024, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003163116, 접근일 2026-09-25 (원문 미열람)
[^ref-388]: Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지), 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링, 2025, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570, 접근일 2026-09-25 (원문 미열람)
[^ref-389]: Kedia, K., Jenamani, R. K., Hazra, A., & Chakrabarti, P. P., Optimal Multi-Agent Path Finding for Precedence Constrained Planning Tasks, 2022-02, https://arxiv.org/abs/2202.10449, 접근일 2026-09-25 (원문 미열람)
[^ref-390]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/BinaryPriorityScheme.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/BinaryPriorityScheme.hpp, 접근일 2026-09-25
```

### data/area_reflection_proposals.json (대상 영역 26. 작업 순서·스케줄링 에 대한 트랙 반영 제안 4건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-09-25-51",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 2,
      "area_no": 26,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "Open-RMF 복합 작업의 순서 있는 단계(f1), HDDL 의 하위 작업 부분·전체 순서(f14, 원문 미열람), VDA 5050 waitForTrigger–trigger 동작(f5). 확인한 로봇 관제·보고 형식과 ISA-95 작업 제어 노드셋에서는 제조사가 다른 플릿 작업 사이 선행 의존 필드를 찾지 못했고, 워크플로·계획 형식은 순서를 표현하나 수행 플릿에 묶는 필드는 확인되지 않았다(f18 범위 축소판, 추정, oq-049·oq-013 연결).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-66",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 3,
      "area_no": 26,
      "section": "6. 대표 접근법과 기술",
      "summary": "rmf_task 작업 계획기의 순서 계획(요청 시작 시각 준수, 탐욕·A* 선택)과 README 기준 충전 작업 자동 삽입(f1·f2), LLM 직접 스케줄 생성의 실행 가능성 한계 벤치마크(ConstraintBench 65.0%·30.5% 조건 병기 f8, SCHEDBench 표현 민감성 f10, DynaSchedBench f12, R-ConstraintBench [추정] f9), LLM 을 결정 루프 밖에 두고 규칙을 합성하는 RACE-Sched(f13)와 분담 가설(f22·f24 [추정]). 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽에 연결한다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-77",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 3,
      "area_no": 26,
      "section": "6. 대표 접근법과 기술",
      "summary": "재스케줄링 정책(주기적·사건 기반, 혼합은 검색 요약 기준)과 방법(수선·재생성, 검색 요약 기준)의 분류 틀(ref-682), 기준생산계획 동결 구간의 비용 영향(저자 보고, ref-683, 로봇 적용 미확인), 작업 계획기 재실행으로 일정 갱신과 LLM 을 결정 루프 밖에 두는 분담(추정, oq-104). 27. AI·학습·적응과 모델 운영과 양쪽 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-98",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 5,
      "area_no": 26,
      "section": "6. 대표 접근법과 기술",
      "summary": "재스케줄링 일정 품질을 효율(makespan·납기 지연)과 안정성(작업 시작 시각 편차)으로 재는 지표(2004)와 강건성·안정성 대리 척도(2008, 정의 원문 문구 미확인). 두 연구는 제조 작업장·단일 기계 조건이며 물류 적용은 미확인이다.",
      "status": "제안"
    }
  ]
}
```

### docs/categories/planning-and-optimization/task-and-workflow-modeling.md (요약)

```markdown
# 24. 작업·워크플로 모델링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

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

### docs/categories/execution-collaboration-and-recovery/human-robot-collaboration.md (요약)

```markdown
# 31. 사람–로봇 협업

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

사람과의 작업 분담, 수동 개입·원격 조작, 주변 사람과의 소통 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람–로봇 작업 분담**: 사람과 로봇이 서로 기다리지 않도록 일을 나누고 작업자의 부담(인체공학)을 고려한다
- **수동 개입·원격 조작**: 운영자가 승인·수동 전환·원격 조작으로 로봇 작업에 개입한다
- **주변 사람과의 소통**: 로봇이 빛·소리·화면으로 의도를 알리고 주변 사람을 안내한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 18번 영역 ‘사람–로봇 협업·운영 인터페이스’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 [옛 분류원문]

> 옛 질문: 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? [옛 분류원문]

## 2. 핵심 질문

사람과 로봇이 같은 공간에서 서로 기다리거나 방해하지 않게 하려면? [분류원문]
```

### docs/categories/design-and-simulation/capacity-sizing-and-layout-design.md (요약)

```markdown
# 35. 처리능력·규모·배치 설계

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

필요한 로봇 수·배치·병목·여러 현장의 자원 배치를 설계하고, 로봇이 다니기 쉬운 공간을 만든다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **처리능력·규모 산정**: 처리할 일의 양에 맞는 로봇 수·종류, 충전기·작업대 배치, 운영 시간대를 정한다
- **병목 분석**: 로봇·설비·사람·승강기 가운데 어디가 병목인지 찾는다
- **다현장 자원 배치**: 여러 현장 사이에서 로봇과 자원을 어디에 얼마나 둘지 정한다
- **로봇 친화 공간 설계·개조**: 문 폭·문턱·경사·승강기 연동·충전 공간처럼 로봇이 다니고 일하기 쉬운 공간을 설계하거나 기존 공간을 고친다

이전 분류(2026-09-24)에서 이 페이지는 옛 3번 영역 ‘처리능력·거점·설비 계획’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 물동량에 필요한 로봇 수와 종류, 작업대·충전기 배치, 교대 운영, 여러 거점의 자원 배치를 결정 [옛 분류원문]

> 옛 질문: 로봇을 늘려야 할까, 포장대나 엘리베이터가 병목일까? [옛 분류원문]

## 2. 핵심 질문

로봇을 늘려야 할까, 공간이나 설비가 병목일까? [분류원문]
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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 21건 / 전체 1399건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 2017 | https://arxiv.org/abs/1705.10868 | 2026-09-24 | 아니오 |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/task_new.html | 2026-09-25 | 예 |
| ref-117 | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 2023 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd | 2026-09-25 | 예 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 2026-09-25 | 예 |
| ref-133 | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 2025 | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 | 2026-09-25 | 아니오 |
| ref-134 | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 2010 | https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291 | 2026-09-25 | 아니오 |
| ref-376 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/task.html | 2026-09-25 | 예 |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 미확인 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp | 2026-09-25 | 예 |
| ref-378 | Open Robotics (open-rmf) | rmf_ros2 — rmf_task_ros2/include/rmf_task_ros2/Dispatcher.hpp | 미확인 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/include/rmf_task_ros2/Dispatcher.hpp | 2026-09-25 | 예 |
| ref-379 | Google (google/or-tools GitHub) | OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver) | 미확인 | https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md | 2026-09-25 | 예 |
| ref-380 | de Koster, R., Le-Duc, T., & Roodbergen, K. J. | Design and control of warehouse order picking: A literature review | 2007 | https://pure.eur.nl/en/publications/design-and-control-of-warehouse-order-picking-a-literature-review/ | 2026-09-25 | 아니오 |
| ref-381 | Boysen, N., Briskorn, D., & Emde, S. | Parts-to-picker based order processing in a rack-moving mobile robots environment | 2017 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758 | 2026-09-25 | 아니오 |
| ref-382 | Boysen, N., de Koster, R., & Weidinger, F. | Warehousing in the e-commerce era: A survey | 2019 | https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/ | 2026-09-25 | 아니오 |
| ref-383 | Nunes, E., Manner, M., Mitiche, H., & Gini, M. | A taxonomy for task allocation problems with temporal and ordering constraints | 2017 | https://www.sciencedirect.com/science/article/abs/pii/S0921889016306157 | 2026-09-25 | 아니오 |
| ref-384 | Yang, X., Hua, G., Zhang, L., Cheng, T. C. E., & Choi, T. M. | Joint order assignment and picking station scheduling in KIVA warehouses with multiple stations | 2021-08 | https://arxiv.org/abs/2108.09056 | 2026-09-25 | 아니오 |
| ref-385 | Boysen, N., Stephan, K., & Weidinger, F. | Manual order consolidation with put walls: the batched order bin sequencing problem | 2019 | https://www.sciencedirect.com/science/article/pii/S2192437620300315 | 2026-09-25 | 아니오 |
| ref-386 | Jiang, M., & Huang, G. Q. | Intralogistics synchronization in robotic forward-reserve warehouses for e-commerce last-mile delivery | 2022 | https://www.sciencedirect.com/science/article/abs/pii/S1366554522000175 | 2026-09-25 | 아니오 |
| ref-387 | 신희철, 이강현, 방선호, 신광섭(한국빅데이터학회 학회지) | 물류센터 생산성 향상을 위한 피킹스케줄링 문제에 관한 연구 | 2024 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003163116 | 2026-09-25 | 아니오 |
| ref-388 | Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지) | 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링 | 2025 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570 | 2026-09-25 | 아니오 |
| ref-389 | Kedia, K., Jenamani, R. K., Hazra, A., & Chakrabarti, P. P. | Optimal Multi-Agent Path Finding for Precedence Constrained Planning Tasks | 2022-02 | https://arxiv.org/abs/2202.10449 | 2026-09-25 | 아니오 |
| ref-390 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/BinaryPriorityScheme.hpp | 미확인 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/BinaryPriorityScheme.hpp | 2026-09-25 | 예 |
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

### docs/open-questions.md (요약: 대상 영역 [26] 에 걸린 12건 / 전체 348건)

```markdown
- oq-013 [열림] ISA-95 세그먼트 의존 유형(B2MML DependencyType)을 입고·적치·피킹·출하 같은 창고 물류 작업의 선후관계 표현에 적용한 사례나 확장이 있는가? (영역 24, 26)
- oq-019 [열림] 상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가? (영역 23, 26)
- oq-049 [열림] 제조사가 다른 로봇 플릿 사이의 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 작업 요청 수준에서 표현·집행하는 표준 필드나 공개 구현이 있는가? (영역 20, 25, 26)
- oq-050 [열림] 로봇 작업대의 주문·랙 순서 최적화 연구가 보고한 로봇 대수·랙 방문 절감 효과를 이종 로봇과 사람 포장대가 섞인 국내 물류센터에서 검증한 자료가 있는가? (영역 26, 35)
- oq-051 [열림] 피킹–포장 동기화의 성과를 포장 작업자 대기시간이나 주문 완료 시간 분산 같은 지표로 재는 합의된 정의가 있는가, ROP 가 순서 결정의 목적함수로 쓸 수 있는가? (영역 26, 39)
- oq-054 [열림] 출하 마감·납기 같은 상위 업무 제약을 배정 목적함수(완료 시각 최소화, 비용 최소화)와 어떻게 결합하는지 정한 공개 설계나 창고 사례가 있는가? (관련 기존 질문: oq-019) (영역 23, 25, 26)
- oq-059 [열림] 주문 납기·출하 마감 같은 업무 우선순위를 교통 협상·통로 양보의 우선권으로 옮기는 규칙을 정한 연구나 현장 기준이 있는가? (영역 26, 27)
- oq-104 [열림] 창고 이동로봇 플릿의 재배정·재스케줄링 주기에서 LLM 추론 지연이 허용되는 한계를 측정했거나, LLM 을 결정 루프 밖에 둔 운영 사례가 있는가? (영역 26, 47)
- oq-137 [열림] 완료 기한·반복 주기·실패 처리 조건처럼 관제 작업 요청 스키마에 자리가 없는 시나리오 항목을 어느 층(시나리오 모델·워크플로 모델·스케줄러)이 보관하고 실행 시점에 어떻게 작업 요청으로 변환하는가? (영역 9, 24, 26, 20)
- oq-178 [열림] 영업 중인 매장·쇼핑몰에서 청소·재고 스캔 로봇을 손님이 많은 시간과 어떻게 나눠 운영하는지(운영 시간대 규칙과 그 효과)를 수치로 보인 연구나 공개 자료가 있는가? (영역 64, 26)
- oq-273 [열림] 병원·상업 시설·물류창고에서 시간대별 사람 혼잡을 로봇 작업 시간 추정과 배정·스케줄링에 반영해 처리 시간이나 지연 변화를 측정한 현장 연구가 있는가? (영역 19, 26, 63)
- oq-328 [열림] 병원 승강기 가동률·탑승 인원 같은 혼잡 임계값(예: 고려대 구로병원의 약 60%)을 다른 병원·건물로 옮겨 로봇 배정 시점에 쓸 때 재보정하는 방법이나 다기관 연구가 있는가? (영역 19, 26, 22)
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

### runs/2026-10-10-02/research.md

```markdown
# 리서치 브리프 2026-10-10-02

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-02 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 25. 작업 배정 — MRTA |
| 대분류 | G. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 가상 시나리오뿐이고, 제약 행의 '출하 마감을 배정 목적함수에 넣는 방법은 미확인'(oq-054)이 남아 있음. 운영 중 도착하는 작업과 용량·마감을 함께 다룬 다른 현장 유형 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 문헌 검토(ref-152)의 계열 구분·실험 플릿 규모가 '미확인'으로 남아 있고, LTAA(ref-168) 비교 결과가 출처 충돌(oq-030)로 11절에 미뤄져 있음. rmf_task TaskPlanner 최적 배정의 적용 범위(한 플릿)가 명시되지 않음
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — Open-RMF 입찰(BidProposal)이 담는 필드가 구체적으로 적혀 있지 않고, 2026-09-26 rmf_fleet_adapter 2.14.0 의 플릿 이름 필터 수정이 반영되지 않음(바뀐 출처)
- 섹션 8. 대표 연구와 자료(주제 페이지로 분리) — 2024~2026 연구(마감 제약 SMT 배정, 혼잡 환경 재분배 배정 MRTA-RM, 최소 비용 흐름 기반 대규모 배정) 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 두 수준 배정에서 제조사 관제가 내야 할 비용·상태 정보(oq-053)가 미확인으로 남아 있음
- 섹션 11. 열린 질문(주제 페이지로 분리) — oq-030·oq-053·oq-054 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. oq-030 LTAA(arXiv 2512.02810) 원문은 LLM 배정과 동적 계획법·강화학습의 성공률을 어떤 조건에서 비교했고, 초록의 '전통 기법을 모두 앞섰다'는 표현은 본문 수치와 맞는가? (섹션 6·11 겨냥)
3. oq-053 ROP 가 플릿 단위로 배정하고 제조사 관제가 플릿 안에서 로봇을 고르는 두 수준 배정에서 제조사 관제는 어떤 비용·상태 정보를 내며, 한 플릿 안의 최적 배정은 어디까지 보장되는가? (섹션 6·7·9·11 겨냥)
4. oq-054 출하 마감·납기 같은 상위 업무 제약을 배정과 결합하는 공개 설계가 있는가? (섹션 5·6·11 겨냥)
5. 이동로봇 플릿 작업 배정 문헌 검토(2025-01)는 방법을 어떤 계열로 나누고 실험 플릿 규모를 어떻게 보고하는가? (섹션 6 겨냥)
6. 배정 비용에 환경 구조·혼잡을 반영해 대규모로 배정하는 최근(2024~2026) 연구와 공개 구현은 무엇이며, 그 결과는 어떤 조건의 실험인가? (섹션 6·8 겨냥)
7. 바뀐 출처: Open-RMF rmf_fleet_adapter 의 입찰 동작은 최근 판에서 어떻게 바뀌었는가? (섹션 7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Meseguer Valenzuela·Blanes Noguera 의 2025 년 문헌 검토는 이동로봇 플릿의 다중 로봇 작업 배정(Multi-Robot Task Allocation, MRTA) 방법을 휴리스틱, 메타휴리스틱, 정확·수리 휴리스틱(matheuristic), 시장 기반, 인공지능 기반의 다섯 계열로 정리한다. | ref-152 | 아니오 | medium | 2025-01 | — | — |
| f2 | [사실] | 같은 문헌 검토의 표 I~V 는 계열별로 각 연구의 방법, 중앙·분산 구조, 구현 환경(프레임워크), 플릿 규모, 주요 결과를 함께 제시한다. | ref-152 | 아니오 | medium | 2025-01 | — | — |
| f3 | [의견] | 문헌 검토의 본문 설명과 표의 플릿 규모 값이 서로 달라, 검토된 연구의 최대 플릿 규모나 계열 간 우열을 하나의 수치로 요약하지 않는 편이 좋다. | ref-152 | 아니오 | low | 2025-01 | — | — |
| f4 | [사실] | LTAA 원문(Kaitha·Yu, 2025-12 프리프린트)의 그림 15 비교는 TEACh 데이터셋의 건설 작업에서 전체 성공률을 LTAA 75.97%, Q-learning 73%, DQN 77% 로 보고하며, 초록은 LTAA 값을 76% 로 반올림해 적는다. | ref-168 | 아니오 | medium | 2025-12-02 | — | — |
| f5 | [사실] | 같은 원문 p.61 은 결정적 비교군의 성공률을 brute force 0.77, greedy 0.81, 동적 계획법(Dynamic Programming, DP) 0.95 로 적고, 이 결정적 알고리즘들은 불확실성 모델이 없어 비교 그림에서 제외했으며 확률적 조건의 직접 비교 기준은 강화학습이라고 설명한다. | ref-168 | 아니오 | medium | 2025-12-02 | — | — |
| f6 | [사실] | LTAA 원문 초록은 로봇 전문화가 뚜렷한 Heavy Excels 설정에서 LTAA 가 77% 완료율과 더 나은 작업 부하 균형으로 전통 기법을 모두 앞섰다고 쓰고, 결론(p.62)은 이 설정의 성공률을 77.1% 로 적는다. | ref-168 | 아니오 | medium | 2025-12-02 | — | — |
| f7 | [의견] | f4~f6 을 함께 보면 원문에는 LTAA 전체 75.97%, Heavy Excels 77.1%, DP 95% 가 모두 있으나 DP 는 불확실성 모델 차이로 비교에서 빠졌으므로, 'LTAA 가 전통 배정법 전체보다 우수하다'는 결론은 지지되지 않으며 같은 조건의 LLM 대 DP 우열은 확정할 수 없고, Heavy Excels 결과와 전체 비교 결과는 분리해 적어야 한다(oq-030 부분 해소). | ref-168 | 아니오 | low | 2025-12-02 | — | — |
| f8 | [사실] | Open-RMF 의 입찰 제안 메시지 BidProposal.msg 는 입찰 공고(BidNotice)에 답해 플릿 어댑터가 내는 것으로, 플릿 이름(fleet_name), 작업을 수행할 것으로 예상되는 로봇 이름(expected_robot_name), 새 작업 수용 전·후의 전체 배정 비용(prev_cost·new_cost), 새 작업의 예상 완료 시각(finish_time) 다섯 필드를 담는다. | ref-1453 | 아니오 | medium | 2026-10-10 | — | — |
| f9 | [추정] | BidProposal 의 필드(f8)는 두 수준 배정에서 제조사 관제(플릿)가 공개하는 비용·상태 정보의 구체적인 예이지만, 이 메시지는 각 플릿이 자기 안에서 계산한 비용만 전하므로 이것만으로 모든 플릿을 합친 최적 배정이 보장되지는 않으며, 이종 플릿의 최적성 손실을 수치로 제한하는 근거는 확인하지 못했다(oq-053 부분 근거). | ref-1453, ref-404 | 아니오 | low | 2026-10-10 | — | — |
| f10 | [사실] | Open-RMF rmf_task README 는 작업 계획기(TaskPlanner)의 최적 배정을 물리·운동 특성을 공유하는 한 플릿에 속한 로봇과 주어진 작업 집합에 대해, 요청된 시작 시각을 고려해 작업이 가장 짧은 시간에 끝나도록 순서를 정하는 문제로 설명한다. | ref-404 | 아니오 | medium | 2026-10-10 | — | — |
| f11 | [의견] | TaskPlanner 의 '최적 배정'(f10)은 한 플릿의 주어진 작업 집합에 한정되므로, 앞으로 들어올 작업, 다른 제조사 관제의 내부 결정, 실제 혼잡까지 포함한 운영 전체의 전역 최적성으로 넓혀 해석해서는 안 된다. | ref-404, ref-1457 | 아니오 | low | 2026-10-10 | — | — |
| f12 | [사실] | Tuck 외(2024, NFM 2024 게재 예정 프리프린트)는 이론 모듈로 만족 가능성(Satisfiability Modulo Theories, SMT) 풀이를 써서, 온라인으로 도착하는 픽업·배송 작업의 배정, 로봇의 동시 적재 용량, 엄격한 마감 준수를 함께 제약식으로 표현하고 점진(incremental) 풀이로 새 작업을 배정한다. | ref-1454 | 아니오 | medium | 2024-03-18 | — | — |
| f13 | [사실] | Tuck 외 방법의 목표는 주어진 모델에서 제약을 모두 만족하는 계획을 찾는 것이고 최소 이동 비용의 전역 최적해를 찾는 것과는 구별되며, 저자들은 알고리즘이 건전·완전하다고 증명하지만 이는 논문의 모델·인코딩 조건 안의 결과이고 국소 경로 계획·충돌 회피는 하위 계획기에 맡긴다. | ref-1454 | 아니오 | medium | 2024-03-18 | — | — |
| f14 | [의견] | 납기·마감 준수가 필수인 작업은 높은 우선순위 점수만 주는 방식과 별도로, 마감을 필수 제약으로 두는 정식화(f12)를 검토할 필요가 있으나, 출하 마감을 배정에 연동한 창고 현장 사례는 확인하지 못했다(oq-054 부분 근거). | ref-1454 | 아니오 | low | 2024-03-18 | 제약 | — |
| f15 | [사실] | Tuck 외는 병원과 유사한 공간을 그래프(노드=구역, 가중치=최악 이동 시간)로 추상화한 다중 로봇 배송 벤치마크 200개(작업 10~30개, 로봇 5~20대, 최대 용량 2 또는 3, 마감 균등 분포)에서 용량 제한 로봇의 동적 작업 배정을 평가했다. | ref-1454 | 아니오 | medium | 2024-03-18 | 병원 / 수행 자원 | — |
| f16 | [사실] | Tuck 외의 병원 모사 배송 문제에서 각 요청은 출발·도착 위치와 발생·마감 시각을 가지며, 새 요청이 들어오면 이미 실행한 동작과 현재 동작은 유지한 채 계획을 갱신한다. | ref-1454 | 아니오 | medium | 2024-03-18 | 병원 / 시작 조건 | — |
| f17 | [의견] | Tuck 외 연구는 병원 배송의 계산 실험 사례이며 병원 현장 실증으로 분류해서는 안 된다. | ref-1454 | 아니오 | low | 2024-03-18 | 병원 / 예외·성과 | — |
| f18 | [사실] | Lee·Sim·Nam 의 MRTA-RM 은 장애물이 밀집하고 통로가 좁은 환경에서 일반화 보로노이 다이어그램(GVD)으로 로드맵을 만들고 이를 여러 구역으로 나눈 뒤 구역 사이에 로봇을 재분배하고 작업을 배정해, 충돌·교착을 줄이면서 전체 완료 시간(makespan)을 줄이려 한다. | ref-1455 | 아니오 | medium | 2025-06-08 | — | — |
| f19 | [사실] | MRTA-RM 저자들은 수백 대 규모 로봇의 동적 시뮬레이션 결과(무작위 시나리오 성공률 96% 초과, 분리 시나리오 58~100%)를 보고하고 Python 구현을 공개했으며, 결론에서 성공률 100% 달성(경로 추종 제어기)과 이종 로봇 팀 확장을 후속 과제로 남겼다. | ref-1455, ref-1456 | 아니오 | medium | 2025-06-08 | — | — |
| f20 | [의견] | MRTA-RM 은 혼잡을 줄이는 배정의 재현 후보로 볼 수 있지만, 임의 환경에서 교착이 없다는 보장으로 소개해서는 안 된다. | ref-1455 | 아니오 | low | 2025-06-08 | — | — |
| f21 | [사실] | Zhang 외의 AAMAS 2026 연구는 온라인 다중 에이전트 픽업·배송의 작업 배정을 환경 그래프 위의 최소 비용 흐름(Minimum-Cost Flow) 문제로 풀어, 선형 배정 방식이 요구하는 로봇·작업 사이 모든 쌍의 거리 행렬 계산을 피한다. | ref-1457 | 아니오 | medium | 2026-05 | — | — |
| f22 | [사실] | Zhang 외는 격자 지도 벤치마크(창고형 Sortation Large 포함)에서 1초 계획 예산으로 최대 20,000 에이전트와 30,000 작업까지 다뤘다고 보고하며, 이는 실제 로봇 배치가 아니라 계산 실험이다. | ref-1457 | 아니오 | medium | 2026-05 | — | — |
| f23 | [사실] | Zhang 외의 흐름 정식화는 기본 간선 비용으로 단위 비용을 쓰고, 선택할 수 있는 대체 비용 모델로 경로 계획기의 혼잡 추정치나 실행 중 평균 대기 시간을 배정 비용에 반영할 수 있으며, 계획기와의 결합은 6절에서 다룬다. | ref-1457 | 아니오 | medium | 2026-05 | — | — |
| f24 | [추정] | MRTA-RM(f18)과 Zhang 외(f21~f23)를 함께 보면 배정 비용에 환경 구조와 혼잡을 반영하는 연구 흐름은 확인되지만, 두 방법은 환경·규모·지표가 달라 성능 수치를 같은 조건의 순위로 비교할 수 없는 것으로 보인다. | ref-1455, ref-1457 | 아니오 | low | 2026-10-10 | — | — |
| f25 | [사실] | Open-RMF rmf_fleet_adapter 2.14.0(2026-09-26)의 변경 이력은 작업 요청에 지정된 플릿 이름이 문자열 또는 배열에 포함되기만 하면 입찰하도록 한 수정(#534)을 기록한다. | ref-1458 | 아니오 | medium | 2026-09-26 | — | — |
| f26 | [의견] | 요청에 후보 플릿을 제한하는 배정 사례를 적을 때는 #534 수정이 포함된 rmf_fleet_adapter 패키지 버전(2.14.0 이상)을 함께 적는 편이 좋으며, 이 변경이 모든 배포판에 자동 반영되었다는 뜻은 아니다. | ref-1458 | 아니오 | low | 2026-09-26 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-152 | Meseguer Valenzuela, A., & Blanes Noguera, F. | Task Allocation in Mobile Robot Fleets: A review | 2025-01 | 논문 | medium | 2026-10-10 | https://arxiv.org/abs/2501.08726 | 아니오 |
| ref-168 | Kaitha, S. p. r., & Yu, H. (Virginia Tech; arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 2025-12-02 | 논문 | medium | 2026-10-10 | https://arxiv.org/abs/2512.02810 | 아니오 |
| ref-404 | Open Robotics (open-rmf) | rmf_task — README | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_task | 아니오 |
| ref-1453 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_internal_msgs — rmf_task_msgs/msg/BidProposal.msg | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/BidProposal.msg | 아니오 |
| ref-1454 | Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (arXiv 2403.11737, NFM 2024 게재 예정) | SMT-Based Dynamic Multi-Robot Task Allocation | 2024-03-18 | 논문 | medium | 2026-10-10 | https://arxiv.org/html/2403.11737v1 | 아니오 |
| ref-1455 | Lee, S., Sim, J., & Nam, C. (arXiv 2506.07293) | Very Large-scale Multi-Robot Task Allocation in Challenging Environments via Robot Redistribution | 2025-06-08 | 논문 | medium | 2026-10-10 | https://arxiv.org/html/2506.07293 | 아니오 |
| ref-1456 | Lee, S. 외 (SeBin-Lee-SG GitHub) | MRTA-RM_public — README | 미확인 | 오픈소스 문서 | medium | 2026-10-10 | https://github.com/SeBin-Lee-SG/MRTA-RM_public | 아니오 |
| ref-1457 | Zhang, Y., Chen, Z., Harabor, D., Le Bodic, P., & Stuckey, P. J. (AAMAS 2026, IFAAMAS) | Flow-Based Task Assignment for Large-Scale Online Multi-Agent Pickup and Delivery | 2026-05 | 논문 | high | 2026-10-10 | https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQIK8423.pdf | 아니오 |
| ref-1458 | Open Robotics (open-rmf/rmf_ros2) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/task-allocation-mrta.md | 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 5 — 병원 모사 환경의 동적 배정 계산 실험 사례 추가(f15 수행 자원·f16 시작 조건·f17 현장 실증 아님 표시), 물류창고 표 제약 행의 '출하 마감 결합 미확인'에 마감 필수 제약 정식화 근거 보충(f12·f14) / 섹션 6(주제 페이지 2026-09-25-area13-s6 반영) — 문헌 검토 문장의 '미확인'을 계열 구분·표 구성으로 교체(f1·f2)하고 최대 규모를 한 수치로 요약하지 않음(f3), LTAA 문장을 원문 수치로 교체(f4·f5·f6·f7: 전체 75.97%·Heavy Excels 77.1%·결정적 비교군 brute force 0.77·greedy 0.81·DP 0.95 의 비교 제외), TaskPlanner 최적 배정의 범위 한정(f10·f11), SMT 기반 마감·용량 배정(f12·f13) / 섹션 7(주제 페이지 s7 반영) — BidProposal 다섯 필드(f8), 메시지만으로 전 플릿 최적이 보장되지 않음(f9), rmf_fleet_adapter 2.14.0 #534(f25·f26) / 섹션 8(주제 페이지 s8 반영) — Tuck 외 2024(f12·f13), MRTA-RM(f18·f19·f20), Zhang 외 AAMAS 2026(f21·f22·f23), 두 연구 비교 한계(f24) / 섹션 9 — 두 수준 배정에서 제조사 관제가 내는 정보의 예와 한계(f8·f9·f10·f11) / 섹션 11(주제 페이지 s11 반영) — oq-030 부분 해소(f4~f7, 출처 충돌의 원인: 초록과 본문 p.61 의 서로 다른 비교 조건), oq-053 부분 근거(f8·f9·f11), oq-054 부분 근거(f12·f14), 새 질문 4건. 참고문헌 ref-168 저자 표기 정정(Yu, S. → Yu, H.; Hongrui Yu)과 ref-152·ref-168 원문 열람 반영. 기존 내용 확인: Open-RMF 입찰이 비용을 담는다는 문장(s7, ref-376)과 TaskPlanner 의 배정·충전 삽입 문장(s6, ref-404)은 이미 있으므로 중복하지 않고 세부(필드·범위)만 더한다. 다음 실행 후보: 20. 로봇·제조사 관제 연동(f8·f9·f25), 27. 다중 로봇 경로·교통 관리 — MAPF(f18·f21~f24), 47. AI·학습·적응과 모델 운영(f4~f7). |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 최소 비용 흐름 | Minimum-Cost Flow | 간선마다 용량과 단위 비용이 있는 네트워크에서 정해진 양의 흐름을 출발점에서 도착점으로 보낼 때 총비용이 가장 작은 흐름을 찾는 최적화 문제로, 대규모 작업 배정을 그래프 위에서 푸는 데 쓰인다. |
| 이론 모듈로 만족 가능성 | Satisfiability Modulo Theories (SMT) | 산술·비트벡터·미해석 함수 같은 이론을 포함한 논리식이 참이 되도록 하는 값이 있는지 판정하는 문제와 그 풀이 기법으로, 마감·용량 같은 제약을 모두 만족하는 배정 계획을 찾는 데 쓰인다. |

## 열린 질문

새로 생긴 질문:

- 서로 다른 제조사 관제가 낸 입찰 비용이 같은 시간·금액 단위와 같은 계산 범위를 뜻하도록 정규화하는 공개 규칙이 있는가? | 관련 영역: 25. 작업 배정 — MRTA, 20. 로봇·제조사 관제 연동 | 근거: f8 | 종류: 일반
- 플릿이 입찰에서 밝힌 예상 수행 로봇과 실제 수행 로봇이 달라질 때 비용·완료 시각을 언제 다시 평가해야 하는가? | 관련 영역: 25. 작업 배정 — MRTA, 20. 로봇·제조사 관제 연동 | 근거: f8 | 종류: 일반
- LTAA 의 결정적 비교군(brute force·greedy·DP)과 확률적 비교군(LTAA·Q-learning·DQN)을 같은 성공 확률 모델과 작업 집합으로 재평가한 공개 재현 자료가 있는가? | 관련 영역: 25. 작업 배정 — MRTA, 47. AI·학습·적응과 모델 운영 | 근거: f5 | 종류: 일반
- 최소 비용 흐름 기반 배정에 이종 로봇의 능력·적재량·충전 제약을 더해도 대규모 계산 성능이 유지되는가? | 관련 영역: 25. 작업 배정 — MRTA, 28. 공용 자원·충전·에너지 최적화 | 근거: f21 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 9 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 6건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-02/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - f1~f3: 문헌 검토의 총 검토 편수는 선정·제외 절차가 원문에 없어 확인하지 못함
    - f4~f7: LTAA 결정적·확률적 비교군을 같은 조건으로 비교한 결과는 원문에 없음(oq-030 은 부분 해소에 그침). 초록의 '전통 기법 모두 우위' 표현과 p.61 의 DP 제외 설명의 불일치는 저자 설명이 없음
    - f8·f9: BidProposal 과 rmf_task README 는 같은 Open-RMF 프로젝트 자료라 독립 교차 확인이 아님. 이종 플릿 두 수준 배정의 최적성 손실을 수치로 제한하는 근거는 찾지 못함(oq-053 미해결)
    - f12: NFM 2024 게재 예정 표기는 arXiv comment 기준이며 게재본(쪽·DOI)은 확인하지 않음
    - f14: 출하 마감을 배정에 연동한 창고 현장 사례는 확인하지 못함(oq-054 미해결)
    - f19: MRTA-RM 논문과 공개 구현은 같은 팀 산출물이라 독립 재현 근거가 아님. RAS 게재본은 README 표기로만 확인
    - f25·f26: #534 수정이 ROS 배포판별 바이너리에 언제 반영되었는지는 확인하지 않음
    - 모든 사실 finding 은 단일 출처라 교차 확인 0건
- 범위 경계 위반 의심:
    - f13: 국소 경로 계획·충돌 회피는 로봇 자체 지능·제어(연계 대상) 몫이며, 원문도 하위 계획기에 맡긴다고 밝혀 배정 범위만 다룸
    - f18~f24: 경로 충돌·교착·혼잡 비용은 27. 다중 로봇 경로·교통 관리 — MAPF 와 겹치므로 배정 비용에 반영하는 부분만 이 영역에 쓰고 경로 계획 자체는 27 에 연결
    - f4~f7: LLM 기반 배정은 교차 규칙상 47. AI·학습·적응과 모델 운영의 연구 방법이 이 영역에 적용된 것으로 양쪽에 연결
    - f15~f17: 병원 모사 환경의 계산 실험이므로 site_type 병원은 '모사 환경'으로 명시하고 현장 실증으로 쓰지 않음
- 한계: 외부 조사 변환이라 검색 횟수 집계 없음(queries 0 은 미집계 표시). 신규 출처 6건(ref-1453~ref-1458, 예약 구간 ref-1453~ref-1482 안), 재사용 3건(ref-152 리뷰 논문·ref-168 LTAA·ref-404 rmf_task README, 모두 이번에 원문 열람). 원문 열람 9/9. 갱신(update) 실행이고 정정 요청이 없어 약한 절(5·6·7·8·9·11절)과 바뀐 출처(rmf_fleet_adapter 2.14.0)만 다뤘다. 검증 수정 반영: Zhang 외 절 번호(§2 문제 정의, §5 흐름 정식화·§5.3.2 거리 행렬 회피, §6 계획기 결합, §7·§7.2·표 1 실험)와 혼잡 비용을 '선택할 수 있는 대체 비용 모델'로 범위 한정(f21~f23), LTAA p.61 의 brute force 0.77·greedy 0.81·DP 0.95 병기와 초록 76% 반올림·arXiv 2025-12-02·저자 Hongrui Yu 정정(f4~f6, ref-168), 리뷰 본문 25대·표 I 45 AMR·표 IV 48 AMR 을 의견 근거에 병기(f3), Tuck 외 NFM 2024 게재 예정(f12, ref-1454), BidProposal 필드 5개와 같은 프로젝트 자료라 독립 확인 아님(f8·f9), #534 확인(f25). 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-030 근거 f4~f7, oq-053 근거 f8·f9·f11, oq-054 근거 f12·f14. 교차 확인 0건이라 사실 finding 신뢰도는 medium 이하. 현장 유형 사례 finding 은 병원 모사 환경(f15~f17)뿐이고 물류창고 실측 비교(2절 질문)는 이번에도 찾지 못함. 국내 자료 없음. L. AI·학습 기술 관련 f4~f7 은 47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안한다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 입력 누락 없음. 우선 지정 질문 없음.
```

### runs/2026-10-10-01/research.md

```markdown
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

(이전 브리프 요약: 이 소절은 생략했다)
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

(이전 브리프 요약: 이 소절은 생략했다)
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
```

### runs/2026-09-25-64/research.md

```markdown
# 리서치 브리프 2026-09-25-64

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-64 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 26. 사이버보안·접근권한·개인정보 |
| 대분류 | G. 안전·보안·지능·거버넌스 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(인증·접근 제어·인클레이브·보안 구역과 도관·이동형 영상정보처리기기)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음(SROS 2 권한, MQTT 접근 제어, 대시보드 역할 인증, 인증서 교체)
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(대상 영역에 걸린 열린 질문 oq-043, oq-056, oq-082 반영 필요)

## 조사 질문

1. 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]
2. ROS 2(SROS 2), Open-RMF, VDA 5050, MQTT 브로커는 장비 인증·통신 보호·명령 권한을 어떤 구조로 제공하거나 구현자에게 맡기는가? (섹션 4·6·7 겨냥)
3. 산업 보안 표준·규제(IEC 62443, NIST SP 800-82, ISO 10218-1:2025, EU 기계 규정, EU 사이버 복원력법)는 로봇·관제 시스템에 무엇을 요구하는가? (섹션 3·7 겨냥)
4. 물류 로봇·관제 소프트웨어에서 공개된 실제 취약점 사례는 무엇이며 어떤 영향을 보고했는가? (섹션 3·8 겨냥)
5. 로봇 카메라 영상과 작업자 데이터 보호에 적용되는 한국 법규·가이드(개인정보 보호법 이동형 영상정보처리기기, 근로자 감시 설비, KISA 로봇 보안 자료)는 무엇인가? (섹션 5·9 겨냥, 한국 자료 우선)
6. 대상 영역 열린 질문 oq-043(출입통제 연동 권한), oq-056(SROS 2 인클레이브 단위), oq-082(관제 보고값 위조 검증)에 답할 근거가 있는가? (섹션 10·11 겨냥)
7. 고객별 격리와 원격 접속 중개 가운데 ROP가 직접 맡을 부분과 제조사·IT 조직에 맡길 부분은 어떻게 나뉘는가? (섹션 9 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ROS 2 보안은 DDS-Security 의 다섯 플러그인 가운데 인증·접근 제어·암호 세 가지만 쓰며, 참여자마다 도메인 보호 방식을 정한 서명된 거버넌스 파일과 참여자 권한을 담은 서명된 권한 파일을 둔다. | ref-009 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | SROS 2 접근 제어 정책은 XML 로 인클레이브·프로파일·권한 규칙을 계층적으로 적고, 토픽(발행·구독)·서비스(요청·응답)·액션(호출·실행)마다 허용·거부를 명시하며, 거부가 같은 대상의 허용보다 우선하고 XSLT 로 DDS 권한 파일로 변환된다. | ref-610 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f3 | [사실] | SROS 2 인클레이브는 인증서·키·거버넌스·권한 파일을 묶은 하나의 보안 신원이며, 한 컨텍스트를 공유하는 노드들은 한 인클레이브의 권한으로 합쳐지고, 인클레이브를 적용하는 범위는 운영체제 프로세스·사용자·장치·군집 단위로 고를 수 있다. | ref-611 | 아니오 | medium | 2026-09-25 | — | — |
| f4 | [사실] | Open-RMF 보안 구성은 ROS 2 부분을 SROS 2(키스토어·인클레이브·서명된 권한)로 보호하고, 웹 대시보드는 TLS 와 Keycloak 기반 OpenID Connect 사용자 인증으로 보호하며, API 서버가 역할마다 보안이 적용된 ROS 2 노드를 하나씩 두고 사용자의 ID 토큰에 따라 접근을 준다. | ref-405 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f5 | [사실] | ROS 2 로봇 시스템 위협 모델(초안)은 보안이 꺼져 있으면 어떤 노드든 어떤 토픽에나 발행할 수 있어 구성요소 신원 위조·명령 가로채기가 가능하고, 기본 자격증명의 SSH 같은 원격 접속이 권한 상승 경로가 되며, 카메라 영상·로그가 보호해야 할 민감 자산이고 빌드 팜·서드파티 구성요소를 통한 공급망 위협이 있다고 정리한다. | ref-010 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f6 | [사실] | VDA 5050 3.0.0 명세는 보안 통신·데이터 보호의 메커니즘을 규정하지 않고 MQTT 프로토콜 보안을 브로커 설정에 맡기며, 운영자·시스템 통합자·차량 제조사·플릿 제어 제공자 사이의 안전·보안 책임도 배분하지 않는다고 적는다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f7 | [사실] | VDA 5050 3.0.0 의 즉시 동작 updateCertificate 는 서비스(MQTT)와 로봇별 개인 키·공개 인증서(선택적으로 루트 인증서)의 내려받기 링크를 받아 인증서를 설치·활성화하며, 명령 발신자를 검증할 수 없으므로 내려받기도 TLS 로 보호하고 활성화 전 인증서 체인을 확인하도록 권고한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f8 | [사실] | VDA 5050 3.0.0 에서 RELEASE 유형 구역은 플릿 제어가 진입을 허가한 뒤에만 로봇이 들어갈 수 있고, 로봇은 requestType ACCESS 인 zoneRequest 로 허가를 요청해 responses 토픽으로 승인을 받는다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f9 | [사실] | Eclipse Mosquitto MQTT 브로커는 ACL 파일로 토픽마다 read·write·readwrite·deny 접근을 정하고 pattern 규칙에서 클라이언트 id(%c)·사용자 이름(%u)을 치환할 수 있으며, require_certificate 와 use_identity_as_username 을 함께 켜면 클라이언트 인증서의 일반 이름(CN)을 접근 제어용 사용자 이름으로 쓴다. | ref-613 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f10 | [추정] | VDA 5050 이 보안을 브로커 설정에 맡기므로, 로봇별 인증서(updateCertificate)의 CN 을 사용자 이름으로 쓰고 제조사·일련번호가 들어간 토픽 경로에 pattern ACL 을 걸면 로봇마다 자기 토픽만 읽고 쓰게 제한하는 구성이 가능해 보이나, 이를 규정한 공개 표준 구성은 확인하지 못했다. | ref-031, ref-613 | 아니오 | low | 2026-09-25 | 제약 | — |
| f11 | [사실] | IEC 62443-3-3 은 IEC 62443-1-1 의 7개 기본 요구(식별·인증 제어, 사용 제어, 시스템 무결성, 데이터 기밀성, 데이터 흐름 제한, 사건 적시 대응, 자원 가용성)에 딸린 제어 시스템 기술 요구와 제어 시스템 능력 보안 수준을 정의한다. | ref-617 | 아니오 | medium | 2013-08 | — | 원문 미열람 |
| f12 | [사실] | IEC 62443 의 보안 구역(zone)은 기능·논리·물리적 관계에 따라 묶여 공통 보안 요구를 공유하는 시스템·구성요소 집합이고, 도관(conduit)은 두 개 이상의 구역을 잇는 통신 채널의 묶음으로 구역 경계에서 통신을 제한·여과하는 역할을 한다. | ref-618 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f13 | [추정] | MiR 는 자사 AMR 이 암호화 통신·접근 제어·보안 부팅을 쓰고 MiR Fleet Enterprise 가 IEC 62443-4-2(SL-C 3)에 맞춰 설계됐다고 밝힌다. | ref-619 | 아니오 | low | 2026-09-25 | — | 원문 미열람, 벤더 주장 |
| f14 | [사실] | 미국 CISA 의 ICS 권고 ICSA-21-280-02 는 Alias Robotics 가 보고한 MiR 차량·MiR Fleet 소프트웨어의 복수 취약점(부적절한 접근 제어, 중요 기능 인증 누락, 민감 데이터 암호화 누락 등)을 공지했고, 악용되면 권한 상승·데이터 유출·로봇 제어·서비스 거부가 가능하다고 했다. | ref-616 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f15 | [사실] | 2025년 개정 ISO 10218-1 은 산업용 로봇 안전에 적용되는 범위에서 사이버보안 요구를 포함한다. | ref-471 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f16 | [사실] | EU 기계 규정 (EU) 2023/1230 은 부속서 III 1.1.9 에서 기계의 안전 기능이 우발적·악의적 손상(corruption)으로부터 보호되도록 설계할 것을 요구하며, 이 규정은 2027-01-20 부터 적용된다. | ref-555 | 아니오 | medium | 2023-06 | — | 원문 미열람 |
| f17 | [사실] | EU 사이버 복원력법(Cyber Resilience Act)은 다른 기기·네트워크와 데이터 연결이 있는 하드웨어·소프트웨어 '디지털 요소가 있는 제품'에 적용되며, 제14조 보고 의무는 2026-09-11 부터, 필수 사이버보안 요구·취약점 처리 등 나머지 주요 의무는 2027-12-11 부터 적용된다. | ref-624 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f18 | [사실] | NIST SP 800-82 Rev. 3(2023-09)은 제목을 운영 기술(OT) 보안 지침으로 바꾸고 범위를 건물 자동화·물리적 출입통제·산업용 IoT 로 넓혔으며, NIST SP 800-53 Rev. 5 통제 목록에 대한 OT 오버레이를 제공한다. | ref-615 | 아니오 | medium | 2023-09 | — | 원문 미열람 |
| f19 | [사실] | 개인정보 보호법 제25조의2는 업무 목적으로 이동형 영상정보처리기기를 운영하는 자가 공개된 장소에서 사람 또는 관련 사물의 영상을 촬영하는 것을 원칙적으로 제한하되, 촬영 사실을 명확히 표시해 정보주체가 거부하지 않은 경우 등을 허용하고, 촬영 시 불빛·소리·안내판 등으로 촬영 사실을 알리도록 한다. | ref-620 | 아니오 | medium | 2026-09-25 | 제약 | 원문 미열람 |
| f20 | [사실] | 개인정보보호위원회의 '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서'는 자율주행차·배달로봇 등이 촬영 영상을 AI 개발에 쓰려면 기기 외부에 촬영 사실을 표시하고, 공개된 장소의 불특정 다수 영상은 원칙적으로 가명처리 후 활용하며, 원본 활용은 규제샌드박스 실증특례로 안전조치를 지킬 때만 가능하다고 안내한다. | ref-621 | 아니오 | medium | 2026-09-25 | 제약 | 원문 미열람 |
| f21 | [사실] | 근로자참여 및 협력증진에 관한 법률은 '사업장 내 근로자 감시 설비의 설치'를 노사협의회의 협의 사항으로 정한다. | ref-622 | 아니오 | medium | 2026-09-25 | 제약 | 원문 미열람 |
| f22 | [사실] | 한국인터넷진흥원(KISA)은 지식플랫폼에 '로봇 보안취약점 점검 체크리스트 해설서'를 게시해 로봇 보안 취약점 점검 항목을 안내한다. | ref-623 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f23 | [추정] | 분류 원문 질문 '외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가?'에 대해, 확인한 자료로는 사용자 역할(OIDC ID 토큰의 역할), ROS 2 인클레이브별 토픽·서비스·액션 허용·거부, MQTT 클라이언트별 토픽 ACL 의 세 층에서 권한을 표현할 수 있으나, 로봇·명령 단위 유지보수 권한 매트릭스를 규정한 공개 표준은 찾지 못했고 VDA 5050 은 이를 구현자에게 맡긴다. | ref-405, ref-610, ref-613, ref-031 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f24 | [추정] | 출하 마감 시간대에 제조사 원격 유지보수 엔지니어가 로봇 한 대의 진단 접속을 요청하면, 기본 자격증명·인증 없는 원격 접속이 권한 상승·로봇 제어로 이어질 수 있으므로 ROP 는 대상 로봇·진단 명령만 허용하고 이동 명령은 막으며 세션을 감사 기록으로 남기는 제약이 필요해 보인다. | ref-010, ref-616, ref-405 | 아니오 | low | 2026-09-25 | 출하 / 제약 | — |
| f25 | [추정] | 입고 도크에서 카메라를 단 AMR 이 작업자를 촬영하는 경우, 물류센터 내부가 개인정보 보호법 제25조의2의 '공개된 장소'인지는 불분명하고 근로자 감시 설비로서 노사협의회 협의 대상이 될 수 있어, 영상 수집·보관·학습 활용 조건이 입고 작업의 제약으로 작용할 것으로 보인다. | ref-620, ref-622, ref-010 | 아니오 | low | 2026-09-25 | 입고 / 제약 | — |
| f26 | [추정] | ROP 가 직접 맡을 보안 몫은 누가 어느 로봇·설비에 어떤 명령을 내릴 수 있는지의 권한 정책, 외부 유지보수 접속의 중개·감사 기록, 고객별 작업·데이터 격리, 영상 데이터 접근 정책, 로봇 인증서 교체(updateCertificate) 같은 보안 명령의 조율로 보인다. | ref-031, ref-405, ref-010 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f27 | [추정] | 연계 대상: 로봇 내부 보안(보안 부팅, 펌웨어 서명, 자격증명 보관, 안전 PLC 설정 보호)과 로봇 안전 기능의 사이버보안 설계는 제조사 몫이고, 네트워크 분할 장비·사용자 신원 제공자는 현장 IT·OT 조직 몫이며, ROP 는 그 결과와 인터페이스를 받아 쓰는 쪽으로 보인다. | ref-010, ref-616, ref-471 | 아니오 | low | 2026-09-25 | — | — |
| f28 | [추정] | 26. 사이버보안·접근권한·개인정보는 로봇 안전 기능의 사이버보안(25. 안전·위험 관리), 규격이 비워 둔 보안 책임 배분(28. 표준·상호운용성·다사업자 거버넌스), 운영자 역할 인증(18. 사람–로봇 협업·운영 인터페이스), 영상의 AI 학습 활용(27. AI·학습·적응과 모델 운영)과 맞물리는 것으로 보인다. | ref-471, ref-031, ref-405, ref-621 | 아니오 | low | 2026-09-25 | — | — |
| f29 | [추정] | 확인한 VDA 5050·SROS 2·Open-RMF 문서는 고객(화주)별 작업·데이터 격리를 규정하지 않아, 공유 창고에서 고객별 격리는 인클레이브 범위나 대시보드 역할 같은 일반 수단을 ROP 가 조합해 설계해야 할 것으로 보인다. | ref-031, ref-611, ref-405 | 아니오 | low | 2026-09-25 | 제약 | — |
| f30 | [추정] | oq-082 와 관련해, DDS 인증은 메시지를 보낸 참여자의 신원을 확인해 구성요소 위조를 막지만 위치·배터리 같은 보고값 내용의 참·거짓은 검증하지 않으므로, 오염된 보고값 검증은 인증과 별도의 타당성 검사가 필요해 보인다. | ref-009, ref-010 | 아니오 | low | 2026-09-25 | 예외·성과 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-009 | Open Robotics (ROS 2 Design) | ROS 2 DDS-Security integration | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://design.ros2.org/articles/ros2_dds_security.html | 아니오 |
| ref-010 | Open Robotics (ROS 2 Design) | ROS 2 Robotic Systems Threat Model | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://design.ros2.org/articles/ros2_threat_model.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-555 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 2023-06 | 정부·연구기관 | medium | 2026-09-25 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 예 |
| ref-610 | Open Robotics (ROS 2 Design) | ROS 2 Access Control Policies | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://design.ros2.org/articles/ros2_access_control_policies.html | 아니오 |
| ref-611 | Open Robotics (ROS 2 Design) | ROS 2 Security Enclaves | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://design.ros2.org/articles/ros2_security_enclaves.html | 아니오 |
| ref-405 | Open Robotics (osrf/ros2multirobotbook) | Programming Multiple Robots with ROS 2 — Security | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/security.html | 아니오 |
| ref-613 | Eclipse Foundation (Eclipse Mosquitto) | mosquitto.conf man page | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://mosquitto.org/man/mosquitto-conf-5.html | 아니오 |
| ref-471 | Association for Advancing Automation (A3) | Updated ISO 10218 \| Answers to Frequently Asked Questions (FAQs) | 미확인 | 업계 보고서 | medium | 2026-09-25 | https://www.automate.org/robotics/blogs/updated-iso-10218-faq | 예 |
| ref-615 | NIST | NIST SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security | 2023-09 | 정부·연구기관 | medium | 2026-09-25 | https://csrc.nist.gov/pubs/sp/800/82/r3/final | 예 |
| ref-616 | CISA | Mobile Industrial Robots Vehicles and MiR Fleet Software (ICSA-21-280-02) | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.cisa.gov/news-events/ics-advisories/icsa-21-280-02 | 예 |
| ref-617 | CSA / IEC (ANSI Webstore) | CAN/CSA IEC 62443-3-3-2017 - Industrial communication networks - Network and system security - Part 3-3: System security requirements and security levels (Adopted IEC 62443-3-3:2013, first edition, 2013-08) | 2013-08 | 표준 | medium | 2026-09-25 | https://webstore.ansi.org/standards/csa/csaiec624432017-2442576 | 예 |
| ref-618 | MDPI (Journal of Cybersecurity and Privacy) | Security Aspects of Zones and Conduits in IEC 62443 | 미확인 | 논문 | medium | 2026-09-25 | https://www.mdpi.com/2624-800X/6/2/52 | 예 |
| ref-619 | Mobile Industrial Robots (MiR) | AMRs and Cybersecurity \| Secure Robotics at MiR | 미확인 | 벤더 문서 | low | 2026-09-25 | https://mobile-industrial-robots.com/blog/amrs-and-cybersecurity | 예 |
| ref-620 | 법제처 국가법령정보센터 | 개인정보 보호법 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/lsEfInfoP.do?lsiSeq=195062 | 예 |
| ref-621 | 김·장 법률사무소 | '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트 | 미확인 | 업계 보고서 | medium | 2026-09-25 | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477 | 예 |
| ref-622 | 법제처 국가법령정보센터 | 근로자참여 및 협력증진에 관한 법률 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636 | 예 |
| ref-623 | 한국인터넷진흥원(KISA) | 로봇 보안취약점 점검 체크리스트 해설서 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://kisa.or.kr/2060205/form?lang_type=KO&page=&postSeq=36 | 예 |
| ref-624 | European Commission (Shaping Europe's digital future) | The Cyber Resilience Act - Summary of the legislative text | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://digital-strategy.ec.europa.eu/en/policies/cra-summary | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절 왜 중요한가: f14(실제 AMR 취약점과 영향), f15·f16·f17(로봇 안전·기계·제품 규제가 사이버보안을 요구), f5(위협 모델) / 4절 핵심 개념: f1(인증·접근 제어·권한 파일), f3(인클레이브), f11(62443 기본 요구·보안 수준), f12(구역·도관), f19(이동형 영상정보처리기기) / 5절 현장 시나리오: f24(출하·제약, 원격 유지보수), f25(입고·제약, 카메라 영상과 작업자) / 6절 대표 접근법: f2(SROS 2 권한), f4(Open-RMF 역할 인증), f7(인증서 교체), f8(RELEASE 구역 허가), f9·f10(MQTT ACL), f13(벤더 주장 병기) / 7절 표준·오픈소스: f6(VDA 5050 보안 범위 제외), f11·f12, f15~f18, f19~f22(한국 법규·KISA) / 8절 대표 연구와 자료: f5, f14, f18, f22 / 9절 경계: f26(ROP 직접), f27('연계 대상'), f23(분류 원문 질문 — 추정) / 10절 연결: f28(25. 안전·위험 관리, 28. 표준·상호운용성·다사업자 거버넌스, 18. 사람–로봇 협업·운영 인터페이스, 27. AI·학습·적응과 모델 운영), f30(13. 작업 배정 — MRTA, oq-082), 기존 oq-043·oq-056(10. 설비·건물 시스템 연동) / 11절: 기존 oq-043·oq-056·oq-082 와 open_questions_new 4건, f29(고객별 격리). |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 보안 구역과 도관 | Zones and Conduits (IEC 62443) | 공통 보안 요구를 공유하는 시스템 묶음(구역)과 구역 사이 통신 채널 묶음(도관)으로 산업 제어 시스템을 나눠 보호하는 IEC 62443 의 구조다. |
| 보안 수준 | Security Level (SL, IEC 62443) | IEC 62443 에서 우발적 위반(SL 1)부터 자원을 갖춘 숙련 공격자(SL 4)까지 막아야 할 위협 수준에 따라 요구의 엄격함을 나눈 등급이다. |
| 권한 파일 | Permissions File (DDS-Security) | DDS 참여자가 어떤 토픽을 발행·구독할 수 있는지 등 권한을 적고 권한 인증기관이 서명한 XML 문서다. |
| 이동형 영상정보처리기기 | Mobile Video Information Processing Device | 사람이 몸에 착용하거나 이동 가능한 물체에 부착해 영상을 촬영하는 장치로, 개인정보 보호법 제25조의2가 업무 목적 운영을 제한한다. |

## 열린 질문

새로 생긴 질문:

- 물류센터 내부처럼 공개되지 않은 작업장에서 카메라를 단 로봇이 작업자를 촬영할 때 개인정보 보호법 제25조의2와 근로자 감시 설비 협의 가운데 무엇이 적용되는지 공식 해석이 있는가? | 관련 영역: 26. 사이버보안·접근권한·개인정보, 18. 사람–로봇 협업·운영 인터페이스 | 근거: f25 | 종류: 일반
- 외부 유지보수 계정의 권한을 로봇·명령 단위로 나눈 매트릭스(예: 진단은 허용, 이동은 불허)를 공개한 로봇 관제·ROP 구성이나 표준이 있는가? | 관련 영역: 26. 사이버보안·접근권한·개인정보, 9. 로봇·제조사 관제 연동 | 근거: f23 | 종류: 일반
- 여러 화주가 로봇 플릿을 공유하는 창고에서 고객별 작업·데이터 격리를 오케스트레이션 수준에서 규정한 표준이나 공개 설계가 있는가? | 관련 영역: 26. 사이버보안·접근권한·개인정보, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f29 | 종류: 일반
- ISO 10218-1:2025 의 사이버보안 요구는 어느 조항에서 무엇(접근 제한·원격 접속·로그 등)을 요구하며 로봇 관제 연동에 어떤 조건을 주는가? | 관련 영역: 26. 사이버보안·접근권한·개인정보, 25. 안전·위험 관리 | 근거: f15 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 0
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처 또는 이 위키의 종합)
    - f11 IEC 62443-3-3 은 판매 목록 소개만 확인, 표준 원문 미열람
    - f14 CISA 권고 발행일·영향 제품 판 미확인(검색 요약 기준)
    - f15 ISO 10218-1:2025 사이버보안 조항 내용 미확인
    - f19 제25조의2 시행일 미확인
    - f20 안내서 발행일 미확인(법률사무소 해설 경유)
    - f21 근로자참여법 조항 번호는 판에 따라 다를 수 있음
    - f22 KISA 해설서의 항목 수·범주는 검색 요약끼리 달라 넣지 않음
    - oq-043·oq-056·oq-082 는 부분 근거만 확보(f3·f30)해 해결 제안하지 않음
    - CISA 원격 접속 지침(2023·2025)은 문서 귀속을 확인하지 못해 넣지 않음
- 범위 경계 위반 의심:
    - f27: 로봇 내부 보안·안전 PLC·네트워크 장비는 분류 원문 9장 '로봇 자체 지능·제어'·'시설·설비 제어' 쪽이라 '연계 대상:'으로 표시
    - f13: 제조사 관제 제품의 보안 인증 주장은 벤더 주장으로만 제안
- 한계: 재실행 1회차. 반려 사유 1(스키마 불일치: finding f27 이 sources 에 없는 ref-012 를 참조): 직전 반환값(research.json)이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로 같은 대상·예산 안에서 브리프 전체를 다시 작성했고, 모든 findings[].source_ids 가 sources[].id 에 있는지 확인했다. ref-012 는 쓰지 않았으며 f27 은 ref-010·ref-616·ref-471 를 근거로 한다(관련 finding: f27). web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 재사용 ref-009·ref-010·ref-031, 신규 ref-610·ref-611·ref-405·ref-613. 나머지는 검색 요약 기준(원문 미열람, 신뢰도 상한 medium). 재사용 ref-009·ref-010 은 참고문헌 목록 요약이 입력에 없어 제목·기관을 원문 기준으로 적었다(같은 URL 이면 퍼블리셔가 기존 항목으로 합친다). 재사용 ref-031·ref-555 는 2026-09-25-61 브리프 값. 검색 16회/30, 신규 출처 15건/15(ref-610~ref-624, 예약 구간 안) — 신규 출처 예산에 도달해 The Robot Report(ISO 10218 교차 확인용), 비잔틴 로봇 연구 논문, KISA 로봇 보안모델 보도, 멀티테넌트 로보틱스 벤더 자료는 출처로 넣지 않았다. 교차 확인 0건. 한국 자료: 개인정보 보호법 제25조의2(ref-620), 개인정보위 안내서 해설(ref-621), 근로자참여법(ref-622), KISA 해설서(ref-623). 교차 규칙: 영상의 AI 학습 활용(f20)은 27. AI·학습·적응과 모델 운영과 연결 제안(f28). 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음.
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
…(발췌: 전체 102,673자 중 앞 15,754자)
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

### data/source_texts/ref-376.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# Tasks in RMF

RMF simplifies task allocation and management across multi-fleet systems.
When a user submits a new task request, RMF will intelligently assign it to the robot in the fleet that can best perform the task. When

RMF supports three types of task requests out of the box:
* Clean: For robots capable of cleaning floor spaces in facilities
* Delivery: For robots capable of delivering items between locations in facilities
* Loop: For robots capable to navigating back and forth between locations in facilities
> Note: A single robot may be capable of performing one of more of the above tasks and fleet adapters can be configured to reflect the capability of its robots.
For more information on the supported task types, [click here](./task_types.md)

In RMF version 21.04 and above, tasks are awarded to robot fleets based on the outcome of a bidding process that is orchestrated by a Dispatcher node, `rmf_dispatcher_node`.
When the Dispatcher receives a new task request from a dashboard or terminal, it sends out a `rmf_task_msgs/BidNotice` message to all the fleet adapters. If a fleet adapter is able to process that request, it submits a `rmf_task_msgs/BidProposal` message back to the Dispatcher with a cost to accommodate the task. An instance of `rmf_task::agv::TaskPlanner` is used by the fleet adapters to determine how best to accommodate the new request. For more information on the task planner, [click here](./task_planner.md)

The Dispatcher then compares all the `BidProposals` received and submits a `rmf_task_msgs/DispatchRequest` message with the fleet name of the robot that the bid is awarded to. There are a couple different ways the Dispatcher evaluates the proposals such as fastest to finish, lowest cost, etc which can be configured.

Battery recharging is tightly integrated with the new task planner. `ChargeBattery` tasks are optimally injected into a robot's schedule when the robot has insufficient charge to fulfill a series of tasks. Currently we assume each robot in the map has a dedicated charging location as annotated with the `is_charger` option in the traffic editor map.

![RMF Bidding Diagram](images/rmf_core/rmf_bidding.png)
```

### data/source_texts/ref-377.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
/*
 * Copyright (C) 2020 Open Source Robotics Foundation
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

#ifndef RMF_TASK__AGV__TASKPLANNER_HPP
#define RMF_TASK__AGV__TASKPLANNER_HPP

#include <rmf_task/Request.hpp>
#include <rmf_task/RequestFactory.hpp>
#include <rmf_task/CostCalculator.hpp>
#include <rmf_task/Constraints.hpp>
#include <rmf_task/Parameters.hpp>
#include <rmf_task/State.hpp>

#include <rmf_utils/impl_ptr.hpp>

#include <vector>
#include <memory>
#include <functional>
#include <variant>

namespace rmf_task {

//==============================================================================
class TaskPlanner
{
public:

  /// The TaskAssignmentStrategy class contains the various profiles and
  /// their associated weights for cost calculation.
  class TaskAssignmentStrategy
  {
  public:

    /// Predefined profiles that initialize the strategy with
    /// pre-defined weights and options.
    enum class Profile : uint32_t
    {
      /// Standard RMF assignment strategy with fastest-first approach
      DefaultFastest = 0,

      /// Prioritize battery level, strongly penalize low SOC with a quadratic term.
      /// Still account for task efficiency (fastest-first), but ignore busyness.
      BatteryAware,

      /// To be overwritten from fleet_config.yaml
      Unset
    };

    /// Options for computing the busyness penalty.
    enum class BusyMode : uint8_t
    {
      /// Mode where busyness penalty is 0 if idle, else 1
      Binary = 0,

      /// Mode where busyness penalty is based on task count
      Count
    };

    /// Constructor
    TaskAssignmentStrategy();

    /// Make a strategy initialized from a predefined profile
    static TaskAssignmentStrategy make(Profile profile);

    /// Set the finish-time polynomial weights
    TaskAssignmentStrategy& finish_time_weights(std::vector<double> values);

    /// Get the finish-time polynomial weights
    const std::vector<double>& finish_time_weights() const;

    /// Set the battery penalty polynomial weights
    TaskAssignmentStrategy& battery_penalty_weights(std::vector<double> values);

    /// Get the battery penalty polynomial weights
    const std::vector<double>& battery_penalty_weights() const;

    /// Set the busy penalty polynomial weights
    TaskAssignmentStrategy& busy_penalty_weights(std::vector<double> values);

    /// Get the busy penalty polynomial weights
    const std::vector<double>& busy_penalty_weights() const;

    /// Set the busyness penalty mode
    TaskAssignmentStrategy& busy_mode(BusyMode mode);

    /// Get the busyness penalty mode
    BusyMode busy_mode() const;

    class Implementation;

  private:
    rmf_utils::impl_ptr<Implementation> _pimpl;
  };

  /// The Configuration class contains planning parameters that are immutable
  /// for each TaskPlanner instance and should not change in between plans.
  class Configuration
  {
  public:
    /// Constructor
    ///
    /// \param[in] parameters
    ///   The parameters that describe the agents
    ///
    /// \param[in] constraints
    ///   The constraints that apply to the agents
    ///
    /// \param[in] cost_calculator
    ///   An object that tells the planner how to calculate cost
    Configuration(
      Parameters parameters,
      Constraints constraints,
      ConstCostCalculatorPtr cost_calculator);

    /// Get the parameters that describe the agents
    const Parameters& parameters() const;

    /// Set the parameters that describe the agents
    Configuration& parameters(Parameters parameters);

    /// Get the constraints that are applicable to the agents
    const Constraints& constraints() const;

    /// Set the constraints that are applicable to the agents
    Configuration& constraints(Constraints constraints);

    /// Get the CostCalculator
    const ConstCostCalculatorPtr& cost_calculator() const;

    /// Set the CostCalculator. If a nullptr is passed, the
    /// BinaryPriorityCostCalculator is used by the planner.
    Configuration& cost_calculator(ConstCostCalculatorPtr cost_calculator);

    class Implementation;

  private:
    rmf_utils::impl_ptr<Implementation> _pimpl;
  };

  /// The Options class contains planning parameters that can change between
  /// each planning attempt.
  class Options
  {
  public:

    /// Constructor
    ///
    /// \param[in] greedy
    ///   If true, a greedy approach will be used to solve for the task
    ///   assignments. Optimality is not guaranteed but the solution time may be
    ///   faster. If false, an A* based approach will be used within the planner
    ///   which guarantees optimality but may take longer to solve.
    ///
    /// \param[in] interrupter
    ///   A function that can determine whether the planning should be interrupted.
    ///
    /// \param[in] finishing_request
    ///   A request factory that generates a tailored task for each agent/AGV
    ///   to perform at the end of their assignments
    Options(
      bool greedy,
      std::function<bool()> interrupter = nullptr,
      ConstRequestFactoryPtr finishing_request = nullptr);

    /// Set whether a greedy approach should be used
    Options& greedy(bool value);

    /// Get whether a greedy approach will be used
    bool greedy() const;

    /// Set an interrupter callback that will indicate to the planner if it
    /// should stop trying to plan
    Options& interrupter(std::function<bool()> interrupter);

    /// Get the interrupter that will be used in this Options
    const std::function<bool()>& interrupter() const;

    /// Set the request factory that will generate a finishing task
    Options& finishing_request(ConstRequestFactoryPtr finishing_request);

    /// Get the request factory that will generate a finishing task
    ConstRequestFactoryPtr finishing_request() const;

    /// Set the task assignment strategy (profile & custom weights)
    /// used by the planner
    Options& task_assignment_strategy(TaskAssignmentStrategy strategy);

    /// Get the task assignment strategy (profile & custom weights)
    /// used by the planner
    const TaskAssignmentStrategy& task_assignment_strategy() const;

    class Implementation;
  private:
    rmf_utils::impl_ptr<Implementation> _pimpl;
  };

  class Assignment
  {
  public:

    /// Constructor
    ///
    /// \param[in] request
    ///   The task request for this assignment
    ///
    /// \param[in] state
    ///   The state of the agent at the end of the assigned task
    ///
    /// \param[in] earliest_start_time
    ///   The earliest time the agent will begin exececuting this task
    Assignment(
      rmf_task::ConstRequestPtr request,
      State finish_state,
      rmf_traffic::Time deployment_time);

    // Get the request of this task
    const rmf_task::ConstRequestPtr& request() const;

    // Get a const reference to the predicted state at the end of the assignment
    const State& finish_state() const;

    // Get the time when the robot begins executing
    // this assignment
    const rmf_traffic::Time deployment_time() const;

    class Implementation;

  private:
    rmf_utils::impl_ptr<Implementation> _pimpl;
  };

  enum class TaskPlannerError
  {
    /// None of the agents in the initial states have sufficient initial charge
    /// to even head back to their charging stations. Manual intervention is
    /// needed to recharge one or more agents.
    low_battery,

    /// None of the agents in the initial states have sufficient battery
    /// capacity to accommodate one or more requests. This may be remedied by
    /// increasing the battery capacity or by lowering the threshold_soc in the
    /// state configs of the agents or by modifying the original request.
    limited_capacity
  };

  /// Container for assignments for each agent
  using Assignments = std::vector<std::vector<Assignment>>;
  using Result = std::variant<Assignments, TaskPlannerError>;

  /// Constructor
  ///
  /// \param[in] configuration
  ///   The configuration for the planner
  ///
  /// \param[in] default_options
  ///   Default options for the task planner to use when solving for assignments.
  ///   These options can be overriden each time a plan is requested.
  TaskPlanner(
    Configuration configuration,
    Options default_options);

  /// Constructor
  ///
  /// \param[in] planner_id
  ///   Identifier of this task planner, to be used for booking automated
  ///   requests.
  ///
  /// \param[in] configuration
  ///   The configuration for the planner.
  ///
  /// \param[in] default_options
  ///   Default options for the task planner to use when solving for assignments.
  ///   These options can be overriden each time a plan is requested.
  TaskPlanner(
    const std::string& planner_id,
    Configuration configuration,
    Options default_options);

  /// Get a const reference to configuration of this task planner
  const Configuration& configuration() const;

  /// Get a const reference to the default planning options.
  const Options& default_options() const;

  /// Get a mutable reference to the default planning options.
  Options& default_options();

  /// Generate assignments for requests among available agents. The default
  /// Options of this TaskPlanner instance will be used.
  ///
  /// \param[in] time_now
  ///   The current time when this plan is requested
  ///
  /// \param[in] agents
  ///   The initial states of the agents/AGVs that can undertake the requests
  ///
  /// \param[in] requests
  ///   The set of requests that need to be assigned among the agents/AGVs
  Result plan(
    rmf_traffic::Time time_now,
    std::vector<State> agents,
    std::vector<ConstRequestPtr> requests);

  /// Generate assignments for requests among available agents. Override the
  /// default parameters
  ///
  /// \param[in] time_now
  ///   The current time when this plan is requested
  ///
  /// \param[in] agents
  ///   The initial states of the agents/AGVs that can undertake the requests
  ///
  /// \param[in] requests
  ///   The set of requests that need to be assigned among the agents/AGVs
  ///
  /// \param[in] options
  ///   The options to use for this plan. This overrides the default Options of
  ///   the TaskPlanner instance
  Result plan(
    rmf_traffic::Time time_now,
    std::vector<State> agents,
    std::vector<ConstRequestPtr> requests,
    Options options);

  /// Compute the cost of a set of assignments
  double compute_cost(const Assignments& assignments) const;

  class Implementation;

private:
  rmf_utils::impl_ptr<Implementation> _pimpl;

};

} // namespace rmf_task

#endif // RMF_TASK__AGV__TASKPLANNER_HPP
```

### data/source_texts/ref-378.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
/*
 * Copyright (C) 2020 Open Source Robotics Foundation
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

#ifndef RMF_TASK_ROS2__DISPATCHER_HPP
#define RMF_TASK_ROS2__DISPATCHER_HPP

#include <rclcpp/node.hpp>
#include <rclcpp/rclcpp.hpp>
#include <rmf_utils/impl_ptr.hpp>
#include <rmf_utils/optional.hpp>

#include <rmf_task_ros2/bidding/Auctioneer.hpp>
#include <rmf_task_ros2/DispatchState.hpp>

// Deprecated message definition
#include <rmf_task_msgs/msg/task_description.hpp>

namespace rmf_task_ros2 {

//==============================================================================
/// This dispatcher class holds an instance which handles the dispatching of
/// tasks to all downstream RMF fleet adapters.
class Dispatcher : public std::enable_shared_from_this<Dispatcher>
{
public:
  using DispatchStates = std::unordered_map<TaskID, DispatchStatePtr>;

  /// Initialize an rclcpp context and make an dispatcher instance. This will
  /// instantiate an rclcpp::Node, a task dispatcher node. Dispatcher node will
  /// allow you to dispatch submitted task to the best fleet/robot within RMF.
  ///
  /// \param[in] dispatcher_node_name
  ///   The ROS 2 node to manage the Dispatching of Task
  ///
  /// \sa init_and_make_node()
  static std::shared_ptr<Dispatcher> init_and_make_node(
    const std::string dispatcher_node_name);

  /// Similarly this will init the dispatcher, but you will also need to init
  /// rclcpp via rclcpp::init(~).
  ///
  /// \param[in] dispatcher_node_name
  ///   The ROS 2 node to manage the Dispatching of Task
  ///
  /// \sa make_node()
  static std::shared_ptr<Dispatcher> make_node(
    const std::string dispatcher_node_name);

  /// Create a dispatcher by providing the ros2 node
  ///
  /// \param[in] node
  ///   ROS 2 node instance
  ///
  /// \sa make()
  static std::shared_ptr<Dispatcher> make(
    const std::shared_ptr<rclcpp::Node>& node);

  /// Submit task to dispatcher node. Calling this function will immediately
  /// trigger the bidding process, then the task "action". Once submmitted,
  /// Task State will be in 'Pending' State, till the task is awarded to a fleet
  /// then the state will turn to 'Queued'
  ///
  /// \param [in] task_description
  ///   Submit a task to dispatch
  ///
  /// \return task_id
  ///   self-generated task_id, nullopt is submit task failed
  [[deprecated]]
  std::optional<TaskID> submit_task(
    const rmf_task_msgs::msg::TaskDescription& task_description);

  /// Cancel an active task which was previously submitted to Dispatcher. This
  /// will terminate the task with a State of: `Canceled`. If a task is
  /// `Queued` or `Executing`, this function will send a cancel req to
  /// the respective fleet adapter. It is the responsibility of the fleet adapter
  /// to make sure it cancels the task internally.
  ///
  /// \param [in] task_id
  ///   Task to cancel
  ///
  /// \return true if success
  bool cancel_task(const TaskID& task_id);

  /// Check the state of a submited task. It can be either active or terminated
  ///
  /// \param [in] task_id
  ///   task_id obtained from `submit_task()`
  ///
  /// \return State of the task, nullopt if task is not available
  std::optional<DispatchState> get_dispatch_state(
    const TaskID& task_id) const;

  /// Get a mutable ref of active tasks map list handled by dispatcher
  const DispatchStates& active_dispatches() const;

  /// Get a mutable ref of terminated tasks map list
  const DispatchStates& finished_dispatches() const;

  using DispatchStateCallback =
    std::function<void(const DispatchState& status)>;

  /// Trigger this callback when a task status is changed. This will return the
  /// Changed task status.
  ///
  /// \param [in] callback function
  void on_change(DispatchStateCallback on_change_fn);

  /// Change the default evaluator to a custom evaluator, which is used by
  /// bidding auctioneer. Default evaluator is: `QuickestFinishEvaluator`
  ///
  /// \param [in] evaluator
  ///   evaluator used to select the best bid from fleets
  void evaluator(bidding::Auctioneer::ConstEvaluatorPtr evaluator);

  /// Get the rclcpp::Node that this dispatcher will be using for communication.
  std::shared_ptr<rclcpp::Node> node();

  /// spin dispatcher node
  void spin();

  class Implementation;

private:
  Dispatcher();
  rmf_utils::unique_impl_ptr<Implementation> _pimpl;
};

} // namespace rmf_task_ros2

#endif // RMF_TASK_ROS2__DISPATCHER_HPP
```

### data/source_texts/ref-379.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
[home](README.md) | [boolean logic](boolean_logic.md) | [integer arithmetic](integer_arithmetic.md) | [channeling constraints](channeling.md) | [scheduling](scheduling.md) | [Using the CP-SAT solver](solver.md) | [Model manipulation](model.md) | [Troubleshooting](troubleshooting.md) | [Python API](https://or-tools.github.io/docs/pdoc/ortools/sat/python/cp_model.html)
----------------- | --------------------------------- | ------------------------------------------- | --------------------------------------- | --------------------------- | ------------------------------------ | ------------------------------ | ------------------------------------- | -----------------------------------------------------------------------------------
# Scheduling recipes for the CP-SAT solver.

https://developers.google.com/optimization/

## Introduction

Scheduling in Operations Research involves problems of tasks, resources and
times. In general, scheduling problems have the following features: fixed or
variable durations, alternate ways of performing the same task, mutual
exclusivity between tasks, and temporal relations between tasks.

## Interval variables

Intervals are constraints containing three constant of affine expressions
(start, size, and end). Creating an interval constraint will enforce that `start
+ size == end`.

The more general API uses three expressions to define the interval. If the size
is fixed, a simpler API uses the start expression and the fixed size.

Creating these intervals is illustrated in the following code snippets.

### Python code

```python
# Snippet from ortools/sat/samples/interval_sample_sat.py
"""Code sample to demonstrates how to build an interval."""

from ortools.sat.python import cp_model

def interval_sample_sat():
  """Showcases how to build interval variables."""
  model = cp_model.CpModel()
  horizon = 100

  # An interval can be created from three affine expressions.
  start_var = model.new_int_var(0, horizon, 'start')
  duration = 10  # Python cp/sat code accept integer variables or constants.
  end_var = model.new_int_var(0, horizon, 'end')
  interval_var = model.new_interval_var(
      start_var, duration, end_var + 2, 'interval'
  )

  print(f'interval = {repr(interval_var)}')

  # If the size is fixed, a simpler version uses the start expression and the
  # size.
  fixed_size_interval_var = model.new_fixed_size_interval_var(
      start_var, 10, 'fixed_size_interval_var'
  )
  print(f'fixed_size_interval_var = {repr(fixed_size_interval_var)}')

  # A fixed interval can be created using the same API.
  fixed_interval = model.new_fixed_size_interval_var(5, 10, 'fixed_interval')
  print(f'fixed_interval = {repr(fixed_interval)}')

interval_sample_sat()
```

### C++ code

```cpp
// Snippet from ortools/sat/samples/interval_sample_sat.cc
#include <stdlib.h>

#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "absl/base/log_severity.h"
#include "absl/log/globals.h"
#include "ortools/sat/cp_model.h"
#include "ortools/util/sorted_interval_list.h"

namespace operations_research {
namespace sat {

void IntervalSampleSat() {
  CpModelBuilder cp_model;
  const int kHorizon = 100;
  const Domain horizon(0, kHorizon);

  // An interval can be created from three affine expressions.
  const IntVar x = cp_model.NewIntVar(horizon).WithName("x");
  const IntVar y = cp_model.NewIntVar({2, 4}).WithName("y");
  const IntVar z = cp_model.NewIntVar(horizon).WithName("z");

  const IntervalVar interval_var =
      cp_model.NewIntervalVar(x, y, z + 2).WithName("interval");
  LOG(INFO) << "start = " << interval_var.StartExpr()
            << ", size = " << interval_var.SizeExpr()
            << ", end = " << interval_var.EndExpr()
            << ", interval_var = " << interval_var;

  // If the size is fixed, a simpler version uses the start expression and the
  // size.
  const IntervalVar fixed_size_interval_var =
      cp_model.NewFixedSizeIntervalVar(x, 10).WithName(
          "fixed_size_interval_var");
  LOG(INFO) << "start = " << fixed_size_interval_var.StartExpr()
            << ", size = " << fixed_size_interval_var.SizeExpr()
            << ", end = " << fixed_size_interval_var.EndExpr()
            << ", fixed_size_interval_var = " << fixed_size_interval_var;

  // A fixed interval can be created using the same API.
  const IntervalVar fixed_interval =
      cp_model.NewFixedSizeIntervalVar(5, 10).WithName("fixed_interval");
  LOG(INFO) << "start = " << fixed_interval.StartExpr()
            << ", size = " << fixed_interval.SizeExpr()
            << ", end = " << fixed_interval.EndExpr()
            << ", fixed_interval = " << fixed_interval;
}

}  // namespace sat
}  // namespace operations_research

int main(int argc, char* argv[]) {
  InitGoogle(argv[0], &argc, &argv, true);
  absl::SetStderrThreshold(absl::LogSeverityAtLeast::kInfo);
  operations_research::sat::IntervalSampleSat();
  return EXIT_SUCCESS;
}
```

### Java code

```java
// Snippet from ortools/sat/samples/IntervalSampleSat.java
package com.google.ortools.sat.samples;

import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.IntVar;
import com.google.ortools.sat.IntervalVar;
import com.google.ortools.sat.LinearExpr;

/** Code sample to demonstrates how to build an interval. */
public class IntervalSampleSat {
  public static void main(String[] args) throws Exception {
    Loader.loadNativeLibraries();
    CpModel model = new CpModel();
    int horizon = 100;

    // An interval can be created from three affine expressions.
    IntVar startVar = model.newIntVar(0, horizon, "start");
    IntVar endVar = model.newIntVar(0, horizon, "end");
    IntervalVar intervalVar =
        model.newIntervalVar(
            startVar,
            LinearExpr.constant(10),
            LinearExpr.newBuilder().add(endVar).add(2),
            "interval");
    System.out.println(intervalVar);

    // If the size is fixed, a simpler version uses the start expression and the size.
    IntervalVar fixedSizeIntervalVar =
        model.newFixedSizeIntervalVar(startVar, 10, "fixed_size_interval_var");
    System.out.println(fixedSizeIntervalVar);

    // A fixed interval can be created using another method.
    IntervalVar fixedInterval = model.newFixedInterval(5, 10, "fixed_interval");
    System.out.println(fixedInterval);
  }
}
```

### C\# code

```csharp
// Snippet from ortools/sat/samples/IntervalSampleSat.cs
using System;
using Google.OrTools.Sat;

public class IntervalSampleSat
{
    static void Main()
    {
        CpModel model = new CpModel();
        int horizon = 100;

        // C# code supports constant of affine expressions.
        IntVar start_var = model.NewIntVar(0, horizon, "start");
        IntVar end_var = model.NewIntVar(0, horizon, "end");
        IntervalVar interval = model.NewIntervalVar(start_var, 10, end_var + 2, "interval");
        Console.WriteLine(interval);

        // If the size is fixed, a simpler version uses the start expression, the size and the
        // literal.
        IntervalVar fixedSizeIntervalVar = model.NewFixedSizeIntervalVar(start_var, 10, "fixed_size_interval_var");
        Console.WriteLine(fixedSizeIntervalVar);

        // A fixed interval can be created using the same API.
        IntervalVar fixedInterval = model.NewFixedSizeIntervalVar(5, 10, "fixed_interval");
        Console.WriteLine(fixedInterval);
    }
}
```

### Go code

```go
// Snippet from ortools/sat/samples/interval_sample_sat.go
// The interval_sample_sat_go command is a simple example of the Interval variable.
package main

import (
	"fmt"

	log "github.com/golang/glog"
	"github.com/google/or-tools/ortools/sat/go/cpmodel"
)

const horizon = 100

func intervalSampleSat() error {
	model := cpmodel.NewCpModelBuilder()
	domain := cpmodel.NewDomain(0, horizon)

	x := model.NewIntVarFromDomain(domain).WithName("x")
	y := model.NewIntVar(2, 4).WithName("y")
	z := model.NewIntVarFromDomain(domain).WithName("z")

	// An interval can be created from three affine expressions.
	intervalVar := model.NewIntervalVar(x, y, cpmodel.NewConstant(2).Add(z)).WithName("interval")

	// If the size is fixed, a simpler version uses the start expression and the size.
	fixedSizeIntervalVar := model.NewFixedSizeIntervalVar(x, 10).WithName("fixedSizeInterval")

	// A fixed interval can be created using the same API.
	fixedIntervalVar := model.NewFixedSizeIntervalVar(cpmodel.NewConstant(5), 10).WithName("fixedInterval")

	m, err := model.Model()
	if err != nil {
		return fmt.Errorf("failed to instantiate the CP model: %w", err)
	}
	fmt.Printf("%v\n", m.GetConstraints()[intervalVar.Index()])
	fmt.Printf("%v\n", m.GetConstraints()[fixedSizeIntervalVar.Index()])
	fmt.Printf("%v\n", m.GetConstraints()[fixedIntervalVar.Index()])

	return nil
}

func main() {
	if err := intervalSampleSat(); err != nil {
		log.Exitf("intervalSampleSat returned with error: %v", err)
	}
}

```

## Optional intervals

An interval can be marked as optional. The presence of this interval is
controlled by a literal. The **no overlap** and **cumulative** constraints
understand these presence literals, and correctly ignore inactive intervals.

### Python code

```python
# Snippet from ortools/sat/samples/optional_interval_sample_sat.py
"""Code sample to demonstrates how to build an optional interval."""

from ortools.sat.python import cp_model

def optional_interval_sample_sat():
  """Showcases how to build optional interval variables."""
  model = cp_model.CpModel()
  horizon = 100

  # An interval can be created from three affine expressions.
  start_var = model.new_int_var(0, horizon, 'start')
  duration = 10  # Python cp/sat code accept integer variables or constants.
  end_var = model.new_int_var(0, horizon, 'end')
  presence_var = model.new_bool_var('presence')
  interval_var = model.new_optional_interval_var(
      start_var, duration, end_var + 2, presence_var, 'interval'
  )

  print(f'interval = {repr(interval_var)}')

  # If the size is fixed, a simpler version uses the start expression and the
  # size.
  fixed_size_interval_var = model.new_optional_fixed_size_interval_var(
      start_var, 10, presence_var, 'fixed_size_interval_var'
  )
  print(f'fixed_size_interval_var = {repr(fixed_size_interval_var)}')

  # A fixed interval can be created using the same API.
  fixed_interval = model.new_optional_fixed_size_interval_var(
      5, 10, presence_var, 'fixed_interval'
  )
  print(f'fixed_interval = {repr(fixed_interval)}')

optional_interval_sample_sat()
```

### C++ code

```cpp
// Snippet from ortools/sat/samples/optional_interval_sample_sat.cc
#include <stdlib.h>

#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "absl/base/log_severity.h"
#include "absl/log/globals.h"
#include "ortools/sat/cp_model.h"
#include "ortools/util/sorted_interval_list.h"

namespace operations_research {
namespace sat {

void OptionalIntervalSampleSat() {
  CpModelBuilder cp_model;
  const int kHorizon = 100;
  const Domain horizon(0, kHorizon);

  // An optional interval can be created from three affine expressions and a
  // BoolVar.
  const IntVar x = cp_model.NewIntVar(horizon).WithName("x");
  const IntVar y = cp_model.NewIntVar({2, 4}).WithName("y");
  const IntVar z = cp_model.NewIntVar(horizon).WithName("z");
  const BoolVar presence_var = cp_model.NewBoolVar().WithName("presence");

  const IntervalVar interval_var =
      cp_model.NewOptionalIntervalVar(x, y, z + 2, presence_var)
          .WithName("interval");
  LOG(INFO) << "start = " << interval_var.StartExpr()
            << ", size = " << interval_var.SizeExpr()
            << ", end = " << interval_var.EndExpr()
            << ", presence = " << interval_var.PresenceBoolVar()
            << ", interval_var = " << interval_var;

  // If the size is fixed, a simpler version uses the start expression and the
  // size.
  const IntervalVar fixed_size_interval_var =
      cp_model.NewOptionalFixedSizeIntervalVar(x, 10, presence_var)
          .WithName("fixed_size_interval_var");
  LOG(INFO) << "start = " << fixed_size_interval_var.StartExpr()
            << ", size = " << fixed_size_interval_var.SizeExpr()
            << ", end = " << fixed_size_interval_var.EndExpr()
            << ", presence = " << fixed_size_interval_var.PresenceBoolVar()
            << ", interval_var = " << fixed_size_interval_var;
}

}  // namespace sat
}  // namespace operations_research

int main(int argc, char* argv[]) {
  InitGoogle(argv[0], &argc, &argv, true);
  absl::SetStderrThreshold(absl::LogSeverityAtLeast::kInfo);
  operations_research::sat::OptionalIntervalSampleSat();
  return EXIT_SUCCESS;
}
```

### Java code

```java
// Snippet from ortools/sat/samples/OptionalIntervalSampleSat.java
package com.google.ortools.sat.samples;

import com.google.ortools.Loader;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.IntVar;
import com.google.ortools.sat.IntervalVar;
import com.google.ortools.sat.LinearExpr;
import com.google.ortools.sat.Literal;

/** Code sample to demonstrates how to build an optional interval. */
public class OptionalIntervalSampleSat {
  public static void main(String[] args) throws Exception {
    Loader.loadNativeLibraries();
    CpModel model = new CpModel();
    int horizon = 100;

    // An interval can be created from three affine expressions, and a literal.
    IntVar startVar = model.newIntVar(0, horizon, "start");
    IntVar endVar = model.newIntVar(0, horizon, "end");
    Literal presence = model.newBoolVar("presence");
    IntervalVar intervalVar =
        model.newOptionalIntervalVar(
            startVar,
            LinearExpr.constant(10),
            LinearExpr.newBuilder().add(endVar).add(2),
            presence,
            "interval");
    System.out.println(intervalVar);

    // If the size is fixed, a simpler version uses the start expression, the size and the literal.
    IntervalVar fixedSizeIntervalVar =
        model.newOptionalFixedSizeIntervalVar(startVar, 10, presence, "fixed_size_interval_var");
    System.out.println(fixedSizeIntervalVar);

    // A fixed interval can be created using another method.
    IntervalVar fixedInterval = model.newOptionalFixedInterval(5, 10, presence, "fixed_interval");
    System.out.println(fixedInterval);
  }
}
```

### C\# code

```csharp
// Snippet from ortools/sat/samples/OptionalIntervalSampleSat.cs
using System;
using Google.OrTools.Sat;

public class OptionalIntervalSampleSat
{
    static void Main()
    {
        CpModel model = new CpModel();
        int horizon = 100;

        // C# code supports constant of affine expressions.
        IntVar start_var = model.NewIntVar(0, horizon, "start");
        IntVar end_var = model.NewIntVar(0, horizon, "end");
        BoolVar presence_var = model.NewBoolVar("presence");
        IntervalVar interval = model.NewOptionalIntervalVar(start_var, 10, end_var + 2, presence_var, "interval");
        Console.WriteLine(interval);

        // If the size is fixed, a simpler version uses the start expression, the size and the
        // literal.
        IntervalVar fixedSizeIntervalVar =
            model.NewOptionalFixedSizeIntervalVar(start_var, 10, presence_var, "fixed_size_interval_var");
        Console.WriteLine(fixedSizeIntervalVar);

        // A fixed interval can be created using the same API.
        IntervalVar fixedInterval = model.NewOptionalFixedSizeIntervalVar(5, 10, presence_var, "fixed_interval");
        Console.WriteLine(fixedInterval);
    }
}
```

### Go code

```go
// Snippet from ortools/sat/samples/optional_interval_sample_sat.go
// The optional_interval_sample_sat command is an example of an Interval variable that is
// marked as optional.
package main

import (
	"fmt"

	log "github.com/golang/glog"
	"github.com/google/or-tools/ortools/sat/go/cpmodel"
)

const horizon = 100

func optionalIntervalSampleSat() error {
	model := cpmodel.NewCpModelBuilder()
	domain := cpmodel.NewDomain(0, horizon)

	x := model.NewIntVarFromDomain(domain).WithName("x")
	y := model.NewIntVar(2, 4).WithName("y")
	z := model.NewIntVarFromDomain(domain).WithName("z")
	presenceVar := model.NewBoolVar().WithName("presence")

	// An optional interval can be created from three affine expressions and a BoolVar.
	intervalVar := model.NewOptionalIntervalVar(x, y, cpmodel.NewConstant(2).Add(z), presenceVar).WithName("interval")

	// If the size is fixed, a simpler version uses the start expression and the size.
	fixedSizeIntervalVar := model.NewOptionalFixedSizeIntervalVar(x, 10, presenceVar).WithName("fixedSizeInterval")

	m, err := model.Model()
	if err != nil {
		return fmt.Errorf("failed to instantiate the CP model: %w", err)
	}
	fmt.Printf("%v\n", m.GetConstraints()[intervalVar.Index()])
	fmt.Printf("%v\n", m.GetConstraints()[fixedSizeIntervalVar.Index()])

	return nil
}

func main() {
	if err := optionalIntervalSampleSat(); err != nil {
		log.Exitf("optionalIntervalSampleSat returned with error: %v", err)
	}
}

```

## Time relations between intervals

Temporal relations between intervals can be expressions using linear
inequalities involving the start and end expressions of the intervals.

As seen above, the factory methods on the model used to build intervals accept
1-var affine expression (a * var + b, a, b integer constants) as arguments to
the start, size, and end parameters.

Once the interval is build, these same expressions can be queries using
`StartExpr(), SizeExpr() and EndExpr()` in C++ and C#, `start_expr(),
size_expr(), and end_expr()` in python, and `getStartExpr(), getSizeExpr(), and
getEndExpr()` in Java.

If one or both intervals are optional, then these inequalities must be reified
by the presence literals of the optional intervals used.

### Python code

```python
# Snippet from ortools/sat/samples/interval_relations_sample_sat.py
"""Builds temporal relations between intervals."""

from ortools.sat.python import cp_model

def interval_relations_sample_sat():
  """Showcases how to build temporal relations between intervals."""
  model = cp_model.CpModel()
  horizon = 100

  # An interval can be created from three 1-var affine expressions.
  start_var = model.new_int_var(0, horizon, 'start')
  duration = 10  # Python CP-SAT code accept integer variables or constants.
  end_var = model.new_int_var(0, horizon, 'end')
  interval_var = model.new_interval_var(
      start_var, duration, end_var, 'interval'
  )

  # If the size is fixed, a simpler version uses the start expression and the
  # size.
  fixed_size_start_var = model.new_int_var(0, horizon, 'fixed_start')
  fixed_size_duration = 10
  fixed_size_interval_var = model.new_fixed_size_interval_var(
      fixed_size_start_var,
      fixed_size_duration,
      'fixed_size_interval_var',
  )

  # An optional interval can be created from three 1-var affine expressions and
  # a literal.
  opt_start_var = model.new_int_var(0, horizon, 'opt_start')
  opt_duration = model.new_int_var(2, 6, 'opt_size')
  opt_end_var = model.new_int_var(0, horizon, 'opt_end')
  opt_presence_var = model.new_bool_var('opt_presence')
  opt_interval_var = model.new_optional_interval_var(
      opt_start_var, opt_duration, opt_end_var, opt_presence_var, 'opt_interval'
  )

  # If the size is fixed, a simpler version uses the start expression, the
  # size, and the presence literal.
  opt_fixed_size_start_var = model.new_int_var(0, horizon, 'opt_fixed_start')
  opt_fixed_size_duration = 10
  opt_fixed_size_presence_var = model.new_bool_var('opt_fixed_presence')
  opt_fixed_size_interval_var = model.new_optional_fixed_size_interval_var(
      opt_fixed_size_start_var,
      opt_fixed_size_duration,
      opt_fixed_size_presence_var,
      'opt_fixed_size_interval_var',
  )

  # Simple precedence between two non optional intervals.
  model.add(interval_var.start_expr() >= fixed_size_interval_var.end_expr())

  # Synchronize start between two intervals (one optional, one not)
  model.add(
      interval_var.start_expr() == opt_interval_var.start_expr()
  ).only_enforce_if(opt_presence_var)

  # Exact delay between two optional intervals.
  exact_delay: int = 5
  model.add(
      opt_interval_var.start_expr()
      == opt_fixed_size_interval_var.end_expr() + exact_delay
  ).only_enforce_if(opt_presence_var, opt_fixed_size_presence_var)

interval_relations_sample_sat()
```

## NoOverlap constraint

A no_overlap constraint simply states that all intervals are disjoint. It is
built with a list of interval variables. Fixed intervals are useful for
excluding part of the timeline.

In the following examples, you want to schedule 3 tasks on 3 weeks excluding
weekends, making the final day as early as possible.

### Python code

```python
# Snippet from ortools/sat/samples/no_overlap_sample_sat.py
"""Code sample to demonstrate how to build a NoOverlap constraint."""

from ortools.sat.python import cp_model

def no_overlap_sample_sat():
  """No overlap sample with fixed activities."""
  model = cp_model.CpModel()
  horizon = 21  # 3 weeks.

  # Task 0, duration 2.
  start_0 = model.new_int_var(0, horizon, 'start_0')
  duration_0 = 2  # Python cp/sat code accepts integer variables or constants.
  end_0 = model.new_int_var(0, horizon, 'end_0')
  task_0 = model.new_interval_var(start_0, duration_0, end_0, 'task_0')
  # Task 1, duration 4.
  start_1 = model.new_int_var(0, horizon, 'start_1')
  duration_1 = 4  # Python cp/sat code accepts integer variables or constants.
  end_1 = model.new_int_var(0, horizon, 'end_1')
  task_1 = model.new_interval_var(start_1, duration_1, end_1, 'task_1')

  # Task 2, duration 3.
  start_2 = model.new_int_var(0, horizon, 'start_2')
  duration_2 = 3  # Python cp/sat code accepts integer variables or constants.
  end_2 = model.new_int_var(0, horizon, 'end_2')
  task_2 = model.new_interval_var(start_2, duration_2, end_2, 'task_2')

  # Weekends.
  weekend_0 = model.new_interval_var(5, 2, 7, 'weekend_0')
  weekend_1 = model.new_interval_var(12, 2, 14, 'weekend_1')
  weekend_2 = model.new_interval_var(19, 2, 21, 'weekend_2')

  # No Overlap constraint.
  model.add_no_overlap(
      [task_0, task_1, task_2, weekend_0, weekend_1, weekend_2]
  )

  # Makespan objective.
  obj = model.new_int_var(0, horizon, 'makespan')
  model.add_max_equality(obj, [end_0, end_1, end_2])
  model.minimize(obj)

  # Solve model.
  solver = cp_model.CpSolver()
  status = solver.solve(model)

  if status == cp_model.OPTIMAL:
    # Print out makespan and the start times for all tasks.
    print(f'Optimal Schedule Length: {solver.objective_value}')
    print(f'Task 0 starts at {solver.value(start_0)}')
    print(f'Task 1 starts at {solver.value(start_1)}')
    print(f'Task 2 starts at {solver.value(start_2)}')
  else:
    print(f'Solver exited with nonoptimal status: {status}')

no_overlap_sample_sat()
```

### C++ code

```cpp
// Snippet from ortools/sat/samples/no_overlap_sample_sat.cc
#include <stdlib.h>

#include <cstdint>

#include "ortools/base/init_google.h"
#include "ortools/base/logging.h"
#include "absl/base/log_severity.h"
#include "absl/log/globals.h"
#include "absl/types/span.h"
#include "ortools/sat/cp_model.h"
#include "ortools/sat/cp_model.pb.h"
#include "ortools/sat/cp_model_solver.h"
#include "ortools/sat/model.h"
#include "ortools/util/sorted_interval_list.h"

namespace operations_research {
namespace sat {

void NoOverlapSampleSat() {
  CpModelBuilder cp_model;
  const int64_t kHorizon = 21;  // 3 weeks.

  const Domain horizon(0, kHorizon);
  // Task 0, duration 2.
  const IntVar start_0 = cp_model.NewIntVar(horizon);
  const int64_t duration_0 = 2;
  const IntVar end_0 = cp_model.NewIntVar(horizon);
  const IntervalVar task_0 =
      cp_model.NewIntervalVar(start_0, duration_0, end_0);

  // Task 1, duration 4.
  const IntVar start_1 = cp_model.NewIntVar(horizon);
  const int64_t duration_1 = 4;
  const IntVar end_1 = cp_model.NewIntVar(horizon);
  const IntervalVar task_1 =
      cp_model.NewIntervalVar(start_1, duration_1, end_1);

  // Task 2, duration 3.
  const IntVar start_2 = cp_model.NewIntVar(horizon);
  const int64_t duration_2 = 3;
  const IntVar end_2 = cp_model.NewIntVar(horizon);
  const IntervalVar task_2 =
      cp_model.NewIntervalVar(start_2, duration_2, end_2);

  // Week ends.
  const IntervalVar weekend_0 = cp_model.NewIntervalVar(5, 2, 7);
  const IntervalVar weekend_1 = cp_model.NewIntervalVar(12, 2, 14);
  const IntervalVar weekend_2 = cp_model.NewIntervalVar(19, 2, 21);

  // No Overlap constraint.
  cp_model.AddNoOverlap(
      {task_0, task_1, task_2, weekend_0, weekend_1, weekend_2});

  // Makespan.
  IntVar makespan = cp_model.NewIntVar(horizon);
  cp_model.AddLessOrEqual(end_0, makespan);
  cp_model.AddLessOrEqual(end_1, makespan);
  cp_model.AddLessOrEqual(end_2, makespan);

  cp_model.Minimize(makespan);

  // Solving part.
  Model model;
  const CpSolverResponse response = SolveCpModel(cp_model.Build(), &model);
  LOG(INFO) << CpSolverResponseStats(response);

  if (response.status() == CpSolverStatus::OPTIMAL) {
    LOG(INFO) << "Optimal Schedule Length: " << response.objective_value();
    LOG(INFO) << "Task 0 starts at " << SolutionIntegerValue(response, start_0);
    LOG(INFO) << "Task 1 starts at " << SolutionIntegerValue(response, start_1);
    LOG(INFO) << "Task 2 starts at " << SolutionIntegerValue(response, start_2);
  }
}

}  // namespace sat
}  // namespace operations_research

int main(int argc, char* argv[]) {
  InitGoogle(argv[0], &argc, &argv, true);
  absl::SetStderrThreshold(absl::LogSeverityAtLeast::kInfo);
  operations_research::sat::NoOverlapSampleSat();
  return EXIT_SUCCESS;
}
```

### Java code

```java
// Snippet from ortools/sat/samples/NoOverlapSampleSat.java
package com.google.ortools.sat.samples;

import com.google.ortools.Loader;
import com.google.ortools.sat.CpSolverStatus;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpSolver;
import com.google.ortools.sat.IntVar;
import com.google.ortools.sat.IntervalVar;
import com.google.ortools.sat.LinearExpr;

/**
 * We want to schedule 3 tasks on 3 weeks excluding weekends, making the final day as early as
 * possible.
 */
public class NoOverlapSampleSat {
  public static void main(String[] args) throws Exception {
    Loader.loadNativeLibraries();
    CpModel model = new CpModel();
    // Three weeks.
    int horizon = 21;

    // Task 0, duration 2.
    IntVar start0 = model.newIntVar(0, horizon, "start0");
    int duration0 = 2;
    IntervalVar task0 = model.newFixedSizeIntervalVar(start0, duration0, "task0");

    //  Task 1, duration 4.
    IntVar start1 = model.newIntVar(0, horizon, "start1");
    int duration1 = 4;
    IntervalVar task1 = model.newFixedSizeIntervalVar(start1, duration1, "task1");

    // Task 2, duration 3.
    IntVar start2 = model.newIntVar(0, horizon, "start2");
    int duration2 = 3;
    IntervalVar task2 = model.newFixedSizeIntervalVar(start2, duration2, "task2");

    // Weekends.
    IntervalVar weekend0 = model.newFixedInterval(5, 2, "weekend0");
    IntervalVar weekend1 = model.newFixedInterval(12, 2, "weekend1");
    IntervalVar weekend2 = model.newFixedInterval(19, 2, "weekend2");

    // No Overlap constraint. This constraint enforces that no two intervals can overlap.
    // In this example, as we use 3 fixed intervals that span over weekends, this constraint makes
    // sure that all tasks are executed on weekdays.
    model.addNoOverlap(new IntervalVar[] {task0, task1, task2, weekend0, weekend1, weekend2});

    // Makespan objective.
    IntVar obj = model.newIntVar(0, horizon, "makespan");
    model.addMaxEquality(
        obj,
        new LinearExpr[] {
          LinearExpr.newBuilder().add(start0).add(duration0).build(),
          LinearExpr.newBuilder().add(start1).add(duration1).build(),
          LinearExpr.newBuilder().add(start2).add(duration2).build()
        });
    model.minimize(obj);

    // Creates a solver and solves the model.
    CpSolver solver = new CpSolver();
    CpSolverStatus status = solver.solve(model);

    if (status == CpSolverStatus.OPTIMAL) {
      System.out.println("Optimal Schedule Length: " + solver.objectiveValue());
      System.out.println("Task 0 starts at " + solver.value(start0));
      System.out.println("Task 1 starts at " + solver.value(start1));
      System.out.println("Task 2 starts at " + solver.value(start2));
    }
  }
}
```

### C\# code

```csharp
// Snippet from ortools/sat/samples/NoOverlapSampleSat.cs
using System;
using Google.OrTools.Sat;

public class NoOverlapSampleSat
{
    static void Main()
    {
        CpModel model = new CpModel();
        // Three weeks.
        int horizon = 21;

        // Task 0, duration 2.
        IntVar start_0 = model.NewIntVar(0, horizon, "start_0");
        int duration_0 = 2;
        IntVar end_0 = model.NewIntVar(0, horizon, "end_0");
        IntervalVar task_0 = model.NewIntervalVar(start_0, duration_0, end_0, "task_0");

        //  Task 1, duration 4.
        IntVar start_1 = model.NewIntVar(0, horizon, "start_1");
        int duration_1 = 4;
        IntVar end_1 = model.NewIntVar(0, horizon, "end_1");
        IntervalVar task_1 = model.NewIntervalVar(start_1, duration_1, end_1, "task_1");

        // Task 2, duration 3.
        IntVar start_2 = model.NewIntVar(0, horizon, "start_2");
        int duration_2 = 3;
        IntVar end_2 = model.NewIntVar(0, horizon, "end_2");
        IntervalVar task_2 = model.NewIntervalVar(start_2, duration_2, end_2, "task_2");

        // Weekends.
        IntervalVar weekend_0 = model.NewIntervalVar(5, 2, 7, "weekend_0");
        IntervalVar weekend_1 = model.NewIntervalVar(12, 2, 14, "weekend_1");
        IntervalVar weekend_2 = model.NewIntervalVar(19, 2, 21, "weekend_2");

        // No Overlap constraint.
        model.AddNoOverlap(new IntervalVar[] { task_0, task_1, task_2, weekend_0, weekend_1, weekend_2 });

        // Makespan objective.
        IntVar obj = model.NewIntVar(0, horizon, "makespan");
        model.AddMaxEquality(obj, new IntVar[] { end_0, end_1, end_2 });
        model.Minimize(obj);

        // Creates a solver and solves the model.
        CpSolver solver = new CpSolver();
        CpSolverStatus status = solver.Solve(model);

        if (status == CpSolverStatus.Optimal)
        {
            Console.WriteLine("Optimal Schedule Length: " + solver.ObjectiveValue);
            Console.WriteLine("Task 0 starts at " + solver.Value(start_0));
            Console.WriteLine("Task 1 starts at " + solver.Value(start_1));
            Console.WriteLine("Task 2 starts at " + solver.Value(start_2));
        }
    }
}
```

### Go code

```go
// Snippet from ortools/sat/samples/no_overlap_sample_sat.go
// The no_overlap_sample_sat command is an example of the NoOverlap constraints.
package main

import (
	"fmt"

	log "github.com/golang/glog"
	"github.com/google/or-tools/ortools/sat/go/cpmodel"

	cmpb "github.com/google/or-tools/ortools/sat/proto/cpmodel"
)

const horizon = 21 // 3 weeks

func noOverlapSampleSat() error {
	model := cpmodel.NewCpModelBuilder()
	domain := cpmodel.NewDomain(0, horizon)

	// Task 0, duration 2.
	start0 := model.NewIntVarFromDomain(domain)
	duration0 := cpmodel.NewConstant(2)
	end0 := model.NewIntVarFromDomain(domain)
	task0 := model.NewIntervalVar(start0, duration0, end0)

	// Task 1, duration 4.
	start1 := model.NewIntVarFromDomain(domain)
	duration1 := cpmodel.NewConstant(4)
	end1 := model.NewIntVarFromDomain(domain)
	task1 := model.NewIntervalVar(start1, duration1, end1)

	// Task 2, duration 3
	start2 := model.NewIntVarFromDomain(domain)
	duration2 := cpmodel.NewConstant(2)
	end2 := model.NewIntVarFromDomain(domain)
	task2 := model.NewIntervalVar(start2, duration2, end2)

	// Weekends.
	weekend0 := model.NewFixedSizeIntervalVar(cpmodel.NewConstant(5), 2)
	weekend1 := model.NewFixedSizeIntervalVar(cpmodel.NewConstant(12), 2)
	weekend2 := model.NewFixedSizeIntervalVar(cpmodel.NewConstant(19), 2)

	// No Overlap constraint.
	model.AddNoOverlap(task0, task1, task2, weekend0, weekend1, weekend2)

	// Makespan.
	makespan := model.NewIntVarFromDomain(domain)
	model.AddLessOrEqual(end0, makespan)
	model.AddLessOrEqual(end1, makespan)
	model.AddLessOrEqual(end2, makespan)

	model.Minimize(makespan)

	// Solve.
	m, err := model.Model()
	if err != nil {
		return fmt.Errorf("failed to instantiate the CP model: %w", err)
	}
	response, err := cpmodel.SolveCpModel(m)
	if err != nil {
		return fmt.Errorf("failed to solve the model: %w", err)
	}

	if response.GetStatus() == cmpb.CpSolverStatus_OPTIMAL {
		fmt.Println(response.GetStatus())
		fmt.Println("Optimal Schedule Length: ", response.GetObjectiveValue())
		fmt.Println("Task 0 starts at ", cpmodel.SolutionIntegerValue(response, start0))
		fmt.Println("Task 1 starts at ", cpmodel.SolutionIntegerValue(response, start1))
		fmt.Println("Task 2 starts at ", cpmodel.SolutionIntegerValue(response, start2))
	}

	return nil
}

func main() {
	if err := noOverlapSampleSat(); err != nil {
		log.Exitf("noOverlapSampleSat returned with error: %v", err)
	}
}

```

## Cumulative constraint with min and max capacity profile.

A cumulative constraint takes a list of intervals, and a list of demands, and a
capacity. It enforces that at any time point, the sum of demands of tasks active
at that time point is less than a given capacity.

Modeling a non constant max profile can be done using fixed (interval, demand)
to occupy the capacity between the actual profile and it max capacity.

Modeling a non zero min profile can be done using fixed (interval, demand) on
the complementary cumulative constraint.

### Python code

```python
# Snippet from ortools/sat/samples/cumulative_variable_profile_sample_sat.py
"""Solves a scheduling problem with a min and max profile for the work load."""

import io

from absl import app
import pandas as pd

from ortools.sat.python import cp_model

def create_data_model() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
  """Creates the dataframes that describes the model."""

  max_load_str: str = """
  start_hour  max_load
     0            0
     2            0
     4            3
     6            6
     8            8
    10           12
    12            8
    14           12
    16           10
    18            6
    20            4
    22            0
  """

  min_load_str: str = """
  start_hour  min_load
     0            0
     2            0
     4            0
     6            0
     8            3
    10            3
    12            1
    14            3
    16            3
    18            1
    20            1
    22            0
  """

  tasks_str: str = """
  name  duration load  priority
   t1      60      3      2
   t2     180      2      1
   t3     240      5      3
   t4      90      4      2
   t5     120      3      1
   t6     300      3      3
   t7     120      1      2
   t8     100      5      2
   t9     110      2      1
   t10    300      5      3
   t11     90      4      2
   t12    120      3      1
   t13    250      3      3
   t14    120      1      2
   t15     40      5      3
   t16     70      4      2
   t17     90      8      1
   t18     40      3      3
   t19    120      5      2
   t20     60      3      2
   t21    180      2      1
   t22    240      5      3
   t23     90      4      2
   t24    120      3      1
   t25    300      3      3
   t26    120      1      2
   t27    100      5      2
   t28    110      2      1
   t29    300      5      3
   t30     90      4      2
  """

  max_load_df = pd.read_table(io.StringIO(max_load_str), sep=r'\s+')
  min_load_df = pd.read_table(io.StringIO(min_load_str), sep=r'\s+')
  tasks_df = pd.read_table(io.StringIO(tasks_str), index_col=0, sep=r'\s+')
  return max_load_df, min_load_df, tasks_df

def check_solution(
    tasks: list[tuple[int, int, int]],
    min_load_df: pd.DataFrame,
    max_load_df: pd.DataFrame,
    period_length: int,
    horizon: int,
) -> bool:
  """Checks the solution validity against the min and max load constraints."""
  minutes_per_hour = 60
  actual_load_profile = [0 for _ in range(horizon)]
  min_load_profile = [0 for _ in range(horizon)]
  max_load_profile = [0 for _ in range(horizon)]

  # The complexity of the checker is linear in the number of time points, and
  # should be improved.
  for task in tasks:
    for t in range(task[1]):
      actual_load_profile[task[0] + t] += task[2]
  for row in max_load_df.itertuples():
    for t in range(period_length):
      max_load_profile[row.start_hour * minutes_per_hour + t] = row.max_load
  for row in min_load_df.itertuples():
    for t in range(period_length):
      min_load_profile[row.start_hour * minutes_per_hour + t] = row.min_load

  for time in range(horizon):
    if actual_load_profile[time] > max_load_profile[time]:
      print(
          f'actual load {actual_load_profile[time]} at time {time} is greater'
          f' than max load {max_load_profile[time]}'
      )
      return False
    if actual_load_profile[time] < min_load_profile[time]:
      print(
          f'actual load {actual_load_profile[time]} at time {time} is'
          f' less than min load {min_load_profile[time]}'
      )
      return False
  return True

def main(_) -> None:
  """Create the model and solves it."""
  max_load_df, min_load_df, tasks_df = create_data_model()

  # Create the model.
  model = cp_model.CpModel()

  # Get the max capacity from the capacity dataframe.
  max_load = max_load_df.max_load.max()
  print(f'Max capacity = {max_load}')
  print(f'#tasks = {len(tasks_df)}')

  minutes_per_hour: int = 60
  horizon: int = 24 * 60

  # Variables
  starts = model.new_int_var_series(
      name='starts',
      lower_bounds=0,
      upper_bounds=horizon - tasks_df.duration,
      index=tasks_df.index,
  )
  performed = model.new_bool_var_series(name='performed', index=tasks_df.index)

  intervals = model.new_optional_fixed_size_interval_var_series(
      name='intervals',
      index=tasks_df.index,
      starts=starts,
      sizes=tasks_df.duration,
      are_present=performed,
  )
…(발췌: 전체 101,719자 중 앞 38,101자)
````

### data/source_texts/ref-390.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

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

#ifndef RMF_TASK__BINARYPRIORITYSCHEME_HPP
#define RMF_TASK__BINARYPRIORITYSCHEME_HPP

#include <rmf_task/Priority.hpp>
#include <rmf_task/CostCalculator.hpp>

#include <memory>

namespace rmf_task {

//==============================================================================
/// A class that serves as a binary prioritization scheme by genrating either
/// high or low Priority objects for requests.
class BinaryPriorityScheme
{
public:

  /// Use these to assign the task priority
  /// In the current implementation this returns a nullptr.
  static std::shared_ptr<Priority> make_low_priority();
  /// Get a shared pointer to a high priority object of the binary prioritization scheme
  static std::shared_ptr<Priority> make_high_priority();

  /// Use this to give the appropriate cost calculator to the task planner
  static std::shared_ptr<CostCalculator> make_cost_calculator();
};

} // namespace rmf_task

#endif // RMF_TASK__BINARYPRIORITYSCHEME_HPP
```
