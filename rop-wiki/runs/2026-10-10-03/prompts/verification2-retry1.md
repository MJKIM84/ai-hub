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
        "ref-1398"
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
        "ref-1398"
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
      "id": "ref-1398",
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
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 5건(ref-1483~ref-1398, 예약 구간 ref-1483~ref-1512 안), 재사용 3건(ref-125 task_request.json, ref-377 TaskPlanner.hpp, ref-379 OR-Tools scheduling.md). 메모의 n3(BinaryPriorityScheme.cpp)은 기존 ref-390(BinaryPriorityScheme.hpp)과 다른 파일이라 새 id 로 등록. 8개 출처 모두 원문 대조 확인(GitHub 파일은 github_raw, 논문 2건은 webfetch). 검증 수정 반영: (1) Tuck 외 증분 풀이 이득의 조건을 '해법기와 배치 크기'로 정정(f18), (2) '공통 필드의 부재가 확장 구현의 불가능을 뜻하지 않는다'를 추정으로 분리(f3), (3) Dai 외 '빠른 도착만으로 전체 종료 시간이 줄지 않는다'를 추정으로 분리(f21), 앞부분은 §III 사실(f20), (4) 이진 우선순위 배분 조건을 같은 계획기 안 로봇 사이 조건과 같은 로봇 안 순서 조건으로 정정하고 벌점식 _priority_penalty × (g + h) 명시(f6·f7), (5) TaskPlanner 의 A* 최적성 보장 명시(f24), (6) 메이크스팬을 Dai 외 정의(차고지 복귀 포함 모든 로봇의 최대 총 작업 시간)로 맞춤(f12), (7) task_request.json 최상위 필드 8개·필수 2개·additionalProperties 없음 명시(f1·f2), (8) Dai 외 게재지 미확인·published 2025·저자 5명(ref-1486), (9) 기존 id 연결. 열린 질문은 해결 제안 없이 oq-019(f28)·oq-049(f29) 부분 근거만 냈다. 메모의 출처 집계 문장('원문 열람 8/8')은 검증 결과와 일치. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-10-10-03/verification.json

```json
{
  "run_id": "2026-10-10-03",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: data/source_texts/ref-125.txt 의 task_request.json 원문에서 최상위 properties 8개, required [category, description], 마감·선행 작업 필드 없음을 확인했다. 발행일 미확인, 확인일 2026-10-10. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: description·priority 설명문(플릿이 지원하는 스키마를 따라야 함)과 최상위 additionalProperties 키가 없음을 ref-125 원문에서 확인했다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. f2 의 위임 구조에서 끌어낸 추론이며, 확장 필드를 실제로 집행하는 구현은 확인되지 않았다는 한계를 본문에 함께 적는다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 의견의 주체(외부 조사 메모를 변환한 리서치 판단)를 밝혀야 한다(required_fixes)."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: BinaryPriorityScheme.cpp(raw)를 열어 make_low_priority 가 nullptr, make_high_priority 가 BinaryPriority(1), make_cost_calculator 가 BinaryPriorityCostCalculator 를 돌려주는 것을 확인했다. 기존 ref-390(헤더)과 같은 프로젝트 자료라 독립 교차 확인은 아니다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: BinaryPriorityCostCalculator.cpp(raw)의 valid_assignment_priority 에서 STEP 1(로봇 사이: 최대 높은 작업 수가 1을 넘는데 0개인 로봇이 있으면 위반)과 STEP 2(같은 로봇 안: ChargeBattery 는 건너뛰고, 낮은 작업 뒤에 높은 작업이 오면 위반)를 확인했다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: compute_cost 는 check_priority 가 켜져 있고 배정이 위반이면 _priority_penalty * (g + h), 그 밖에는 g + h 를 돌려준다. 벌점 계수의 기본값은 이 파일에 없다(헤더 미대조)."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 근거 코드(cost.cpp 에 마감 검사가 없음)와 스키마(마감 필드가 없음)를 확인했다. 의견의 주체를 밝혀야 한다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: compute_g_assignment 는 finish_state 시각에서 booking 의 earliest_start_time 을 뺀 초 단위 값을 쓰고, compute_g 는 모든 로봇·모든 배정에 걸쳐 합산한다. 이 계산기에는 TaskAssignmentStrategy 가중치를 참조하는 코드가 없다. ref-377 은 비용 계산기를 지정하지 않으면(nullptr) 이 계산기를 쓴다고 적지만, 같은 헤더의 TaskAssignmentStrategy(완료 시각·배터리·바쁨 가중치)와 이 계산기의 관계는 확인하지 못했다. 그래서 서술은 이 계산기에 한정해야 한다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ChargeBattery::Description 분기의 'return 0.0; // Ignore charging tasks in cost'."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. f9·f10 의 정의에서 끌어낸 추론이며 실행 결과로 확인하지 않았다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. rmf_task 쪽 합산 정의는 코드로 확인했다. Dai 외가 메이크스팬 최소화를 목표로 한다는 점은 OpenAlex 의 초록 요약으로 확인했다. 다만 Dai 외 PDF 는 이번 검증에서 텍스트를 뽑지 못해(이진 PDF) '차고지(depot) 복귀를 포함한 총 작업 시간 최댓값'이라는 정의는 원문으로 대조하지 못했다. 이 괄호 정의는 빼거나 '미확인'으로 표시한다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-379 원문에서 'Cumulative constraint with min and max capacity profile' 절을 확인했다(어느 시점이든 진행 중인 작업 수요의 합이 용량 이하). 구간·선택 구간·시간 관계·NoOverlap 은 기존 7절과 같은 내용이다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 문서의 예제는 일반 스케줄링 예제이고 로봇·도크 사례가 아니라는 한계를 함께 적는다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2403.11737v1 HTML 을 열어 Definition 6(완료된 작업: drop 이 마감 전, pickup 은 도착 시각 이후)과 초록의 작업 마감·용량 있는 에이전트 설정을 확인했다. 2024-03-18 v1."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. CP-SAT 이 제약과 목적을 따로 두는 구조(ref-379)와 마감을 필수 조건으로 둔 Tuck 외 정의(ref-1485)를 확인했다. 의견의 주체를 밝혀야 한다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Definition 9 갱신 계획에서 과거 동작과 현재 동작은 바뀌지 않고, 계획은 시스템 위치에서만 갱신할 수 있다. §4.3 에서 과거 action point 를 고정한다. 같은 논문을 실행 2026-10-10-02 가 ref-1454 로 이미 등록했으므로 id 중복에 유의한다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §4.3 push·pop 증분 풀이를 확인했다. §6.2 의 200 작업·20 에이전트·배치 1·10 설정과, Z3-BV 는 작은 배치의 증분 풀이에서·Bitwuzla-BV 는 큰 배치의 비증분 풀이에서 우세하다는 결론을 확인했다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. Definition 9 에서 도출했다. 이동 시간이 불확실한 조건의 실행 성능 보장으로 넓히지 않는다는 한계를 유지한다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실에서 부분 강등. 출처 실재는 OpenAlex(DOI 10.1109/LRA.2025.3534682, IEEE RA-L 10(3):2654–2661, 2025-01-27, 저자 5명 일치)로 확인했다. marmotlab PDF 는 이번 검증에서 텍스트 추출에 실패했다(원문 미대조). 초록 요약으로 확인되는 부분은 '필요한 로봇이 모두 와야 작업을 시작하며, 대기(idle waiting)를 줄이는 것이 목표'라는 데까지다. 연합 능력 벡터 합 조건, 실행 기간 내내 함께 있어야 한다는 조건, '탐색·구조 모사 계산 실험'이라는 틀은 확인하지 못했다(SADCHER 논문의 인용 설명에도 없다). 확인된 부분은 [사실], 나머지는 [추정]으로 나눈다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 초록의 '모든 필요 로봇이 모여야 시작' 조건에서 끌어낸 추론이다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 실제 창고의 피킹–포장 인계와 같다고 주장하지 않는 한계를 유지하고, 의견의 주체를 밝힌다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실에서 추정으로 강등. 분산 강화학습 일정 정책과, 휴리스틱·MIP 기준선과 비슷하거나 낫고 두 자릿수 이상 빠르다는 저자 보고는 OpenAlex 의 초록 요약으로 확인했다. 그러나 '최대 150 에이전트·500 작업·5종 능력'이라는 규모 수치는 PDF 텍스트 추출 실패와 검색 2회로도 확인하지 못했다. 저자 보고이며 검증 단계에서 원문을 대조하지 못했다는 점을 병기한다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: data/source_texts/ref-377.txt 의 Options 주석(greedy 는 최적성 미보장·더 빠를 수 있음, A* 는 최적성 보장·더 오래 걸릴 수 있음). 기존 6절 분리 페이지와 같은 내용이므로 기존 각주를 재사용한다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 근거 메모의 'rmf_task 기본 계산기'는 비용 계산기를 지정하지 않았을 때 쓰는 BinaryPriorityCostCalculator(ref-377 주석)로 한정해야 한다. Dai 외의 목적(메이크스팬)은 초록 요약 수준에서 확인했다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: rmf_ros2 2.14.0 태그의 CHANGELOG.rst(raw)에서 '2.14.0 (2026-09-26)'과 #543 'Fix phase key for skip requests', #524 'Fix cumulative delay calculation in EasyTrafficLight'를 확인했다. 같은 URL 이 실행 2026-10-10-01(ref-1424)·2026-10-10-02(ref-1458)에서 이미 등록됐다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 근거(f26)를 확인했다. 의견의 주체를 밝힌다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. oq-019 부분 근거일 뿐이며 해결로 바꾸지 않는다(해결 제안 없음과 일치)."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. task_request.json 한 파일 범위의 판단이고 다른 작업 유형 스키마는 대조하지 않았다. oq-049 는 열린 상태로 둔다."
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
      "ref-1485(Tuck 외, https://arxiv.org/html/2403.11737v1)는 실행 2026-10-10-02 의 ref-1454 와 URL 이 같다 — 같은 출처를 새 id 로 중복 등록할 위험이 있다",
      "ref-1398(rmf_fleet_adapter 2.14.0 CHANGELOG.rst)은 실행 2026-10-10-01 의 ref-1424, 실행 2026-10-10-02 의 ref-1458 과 URL 이 같다",
      "f5 는 기존 7절 BinaryPriorityScheme 행(ref-390, 헤더)의 '낮음은 nullptr' 내용과 겹친다 — 행을 고쳐 쓰고 새 행을 만들지 않는다",
      "f24 는 기존 6절 주제 페이지(2026-09-25-area14-s6)의 탐욕·A* 문장과 같은 내용이다 — 기존 각주 ref-377 재사용",
      "f13 의 구간·선택 구간·시간 관계·겹침 금지는 기존 7절 OR-Tools 행과 같다 — 누적 용량 제약만 새로 더한다",
      "새 열린 질문 3번(작업 완료 시각 합·납기 지연 합·계획 변경량의 가중치 검증)은 oq-054(출하 마감과 배정 목적함수 결합), oq-051(순서 결정 목적함수 지표)과 일부 겹친다",
      "용어 후보 '이론 모듈로 만족 가능성(SMT)'은 실행 2026-10-10-02 브리프의 용어 후보와 같다"
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
    "f20: 문장을 둘로 나눈다. (가) '필요한 로봇이 모두 작업 위치에 와야 작업을 시작하고, 먼저 온 로봇의 대기를 줄이는 것이 목표다'는 [사실]로 둔다. (나) '연합 능력 벡터 합이 요구를 충족해야 시작한다, 실행 기간 내내 함께 있어야 한다, 탐색·구조를 모사한 계산 실험이다'는 [추정]으로 강등하고 '검증 단계 원문 미대조'를 병기한다 — 검증에서 PDF 텍스트를 뽑지 못했고 초록 요약으로는 (가)까지만 확인됐다.",
    "5절에 '현장 유형: 기타' 사례(f20~f22)를 둘 때 제목·설명을 '현장을 특정하지 않은 계산 실험이며 현장 적용 사례가 아니다'로 밝힌다. '탐색·구조'는 f20 (나)의 [추정] 범위로만 언급한다. site_matrix_updates 의 기타 칸 제목에도 '계산 실험'을 넣는다 — 현장 실증으로 읽히지 않게 하기 위해서다.",
    "f23: [사실] → [추정]으로 강등한다. '최대 150 에이전트·500 작업·5종 능력'은 '저자 보고, 검증 단계 원문 미대조'로 병기하고, 휴리스틱·MIP 대비 결과는 '저자 실험, 독립 재현 미확인'을 유지한다 — 검증에서는 규모 수치를 확인하지 못했다.",
    "f12: 메이크스팬 설명의 괄호 정의 '차고지 복귀를 포함한 모든 로봇의 총 작업 시간 중 최댓값'은 빼거나 '정의 세부 미확인'으로 표시한다. 'Dai 외는 메이크스팬 최소화를 목표로 한다'까지만 쓴다 — 검증에서 원문 정의를 대조하지 못했다.",
    "f9·f11·f12·f25: 비용 정의 문장의 주어를 'BinaryPriorityCostCalculator(계획기에 비용 계산기를 지정하지 않으면 쓰는 계산기, ref-377 주석)'로 한정한다. 'Open-RMF 계획기가 최소화하는 목적 전체' 또는 'Open-RMF 기본 비용'으로 일반화하지 않는다 — 같은 헤더(ref-377)에 완료 시각·배터리·바쁨 가중치를 갖는 TaskAssignmentStrategy 가 있으나, 그 가중치와 이 계산기의 관계는 확인되지 않았다. 이 관계의 확인은 additional_research_requests 로 넘긴다.",
    "f4·f8·f16·f22·f25·f27·f28: [의견] 문장마다 의견의 주체를 '이 위키의 판단(외부 조사 메모 기반)'처럼 밝힌다 — 공통 규칙 2절과 검증 항목 5에 따라 의견의 주체를 표시해야 한다.",
    "7절 BinaryPriorityScheme 행: '비용 반영 방식은 미확인'을 f5~f7 의 내용(높음은 BinaryPriority(1)·낮음은 nullptr, 로봇 사이 배분·로봇 안 순서 위반 시 비용에 벌점 계수를 곱함)으로 바꾼다. 각주는 ref-390 을 유지하고 ref-1484·ref-1483 을 더한다. 태그는 [사실]을 유지하고 f8 은 [의견]으로 덧붙인다 — 새 행을 만들지 않는다.",
    "7절 Open-RMF 작업 요청 스키마 행과 5절 시작 조건 칸: '마감·선후 필드 없음'을 '공통 최상위 스키마(8개 필드)에 마감·선후 필드 없음, description·priority 는 플릿 지원 스키마에 위임'(f1·f2)으로 범위를 한정한다. 접근일은 2026-10-10 으로 고친다.",
    "8절(주제 페이지 2026-09-25-area14-s8) 머리 문장 '성능 수치는 모두 저자 실험 결과이며 이 위키가 원문을 열지 못했다'를 고친다. 기존 항목에만 적용되도록 한정하고, Tuck 외는 원문을 열어 확인했다(ref-1485)는 점과 Dai 외는 검증 단계에서 원문을 대조하지 못했다는 점을 구분해 적는다.",
    "참고문헌: ref-1486 의 published 를 '2025' 대신 '2025-01-27'로 고친다. 게재지를 IEEE Robotics and Automation Letters, 10(3), 2654–2661, DOI 10.1109/LRA.2025.3534682 로 적고 '게재지 미확인' 문구를 지운다 — OpenAlex 서지 기록으로 확인했다.",
    "참고문헌 중복: ref-1485 는 실행 2026-10-10-02 의 ref-1454 와 URL 이 같고, ref-1398 은 ref-1424·ref-1458 과 URL 이 같다. 그 id 가 이미 게시돼 있으면 각주와 reference_updates 에 기존 id 를 쓰고 새 id 를 등록하지 않는다. 게시 전이면 reference_updates 에 같은 URL 을 다른 id 로 두 번 넣지 않는다 — 공통 규칙 10(같은 주장에는 기존 각주 재사용).",
    "새 열린 질문 3번('작업 완료 시각 합, 납기 지연 합, 계획 변경량을 함께 최적화할 때…'): 질문 끝에 '(관련 기존 질문: oq-054, oq-051)'을 붙인다 — 기존 질문과 일부 겹친다.",
    "용어집: '이론 모듈로 만족 가능성(SMT)'이 실행 2026-10-10-02 에서 이미 등록됐으면 신규 등록하지 않고 기존 항목을 쓴다. '메이크스팬' 정의는 ref-379(메이크스팬 목적 예제)와 f12 범위 안에서 쓰고, 차고지 복귀 같은 세부는 넣지 않는다.",
    "열린 질문 oq-019·oq-049: 부분 근거(f28·f29)만 덧붙이고 상태는 [열림]으로 둔다 — 해결 제안이 없고 답이 되는 finding 도 없다.",
    "트랙 반영 제안 4건(2026-09-25-51·66·77·98): 이번 브리프에 그 내용(HDDL, VDA 5050 waitForTrigger, LLM 스케줄 벤치마크, 재스케줄링 분류·안정성 지표)을 조사·검증한 finding 이 없으므로 이번 실행에서는 6·7절에 반영하지 않는다. 다음 26. 작업 순서·스케줄링 실행으로 넘긴다(본문에 넣으면 드리프트). 제안 요약의 '27. AI·학습·적응과 모델 운영'은 개정 분류의 '47. AI·학습·적응과 모델 운영'이다.",
    "직접 인용: 페이지에서 ref-1483(BinaryPriorityCostCalculator.cpp)의 코드나 주석을 직접 인용할 때는 한 번(예: 'Ignore charging tasks in cost')만 쓰고, 나머지 비용식·검사 조건은 재서술한다 — 출처당 직접 인용 1회 규칙(5.3)."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 27건, 미확인 2건, 교차 확인 0건(rmf_task 헤더·구현·스키마는 같은 프로젝트 자료라 독립 교차 확인으로 세지 않았다). 강등: f20 사실 → 일부 추정(연합 능력 조건·탐색·구조 모사 틀을 원문으로 대조하지 못함), f23 사실 → 추정(150 에이전트·500 작업·5종 능력 규모 수치 미확인). 원문 미열람 출처: ref-1486(Dai 외) — 검증 단계에서 PDF 텍스트를 뽑지 못했다. 실재와 서지(IEEE RA-L 10(3), 2025-01-27, DOI 10.1109/LRA.2025.3534682, 저자 5명)는 OpenAlex 로, 핵심 설정(필요한 로봇이 모두 모여야 시작, 메이크스팬 최소화, 휴리스틱·MIP 대비 두 자릿수 이상 빠름)은 초록 요약으로만 확인했다. ref-125·ref-377·ref-379 는 입력 원문 텍스트로, ref-1483·ref-1484·ref-1398 은 GitHub raw 로, ref-1485 는 arXiv HTML 로 원문을 대조했다. 브리프의 ref-1485·ref-1486 은 fetched: true 인데 fetch_url 이 null 이다(리서치 기록 누락). 주의: Open-RMF 비용 설명은 비용 계산기를 지정하지 않았을 때 쓰는 BinaryPriorityCostCalculator 에 한정된다. 같은 헤더의 TaskAssignmentStrategy(완료 시각·배터리·바쁨 가중치)와의 관계는 미확인이다. 이진 우선순위는 비용 벌점이며 마감 보장이 아니다. Tuck 외와 Dai 외는 계산 실험이고, 5절 '기타' 사례는 현장 실증이 아니다. 같은 URL 의 출처가 이전 실행(ref-1454, ref-1424·ref-1458)과 겹쳐 id 통일이 필요하다. 트랙 반영 제안 4건은 이번 브리프가 다루지 않아 반영하지 않고 다음 실행으로 넘긴다. 정정 요청 없음. 열린 질문 oq-019·oq-049 는 부분 근거만 추가하고 해결로 인정하지 않는다. 검증 검색 6회를 썼다.",
  "retry_reason": null
}
```

### runs/2026-10-10-03/pages.json

```json
{
  "run_id": "2026-10-10-03",
  "outline": [
    {
      "path": "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2600,
      "summary": "물류창고 사례의 시작 조건·제약 칸을 Open-RMF 공통 최상위 스키마 범위로 한정하고(f1·f2, f3 추정, f4 의견), 현장을 특정하지 않은 협업 작업 계산 실험을 현장 유형 ‘기타’로 더한다(f20 사실·추정 분리, f21 추정, f22 의견, f23 추정).",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f20",
        "f21",
        "f22",
        "f23"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 370,
      "summary": "Open-RMF rmf_task 의 이진 우선순위 비용 계산기는 마감을 검사하지 않고, 우선순위 검사가 켜져 있으면 우선순위 배분을 어긴 배정의 비용에 벌점 계수를 곱한다. [사실][^ref-1483] 세부는 새 주제 페이지로 연결한다.",
      "planned_findings": [
        "f6",
        "f7"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1520,
      "summary": "작업 요청 스키마 행을 공통 최상위 필드 기준으로 한정하고, BinaryPriorityScheme 행의 ‘비용 반영 방식 미확인’을 우선순위 검사가 켜져 있을 때의 벌점 방식으로 바꾸며, CP-SAT 누적 용량 제약과 rmf_fleet_adapter 2.14.0 변경 이력을 더한다. [사실][^ref-1483]",
      "planned_findings": [
        "f1",
        "f2",
        "f5",
        "f6",
        "f7",
        "f8",
        "f13",
        "f26",
        "f27"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1300,
      "summary": "머리 문장 안에 기존 2026-09-25 주제 페이지 링크를 두고 그 항목에만 ‘원문 미열람’을 한정하며, 원문을 연 Tuck 외(2024)와 원문을 대조하지 못한 Dai 외(2025)를 구분해 더한다. [사실][^ref-1485]",
      "planned_findings": [
        "f17",
        "f18",
        "f23",
        "f24",
        "f25"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
      "section": "11. 열린 질문",
      "budget_chars": 980,
      "summary": "머리 문장 안에 기존 열린 질문 정리 페이지 링크를 두고, oq-019·oq-049 에 부분 근거를 덧붙이며(상태 열림 유지) 새 질문 3건을 올린다. [추정][^ref-125]",
      "planned_findings": [
        "f28",
        "f29"
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md",
      "section": "1~7",
      "budget_chars": 2650,
      "summary": "이진 우선순위는 우선순위 검사가 켜져 있을 때 붙는 비용 벌점이며 마감 보장이 아니고(f5~f8), 비용 계산기는 작업별 (완료 − 가장 이른 시작) 합을 쓰며(f9~f12), 마감·용량은 제약으로(f13~f16), 긴급 삽입은 현재 동작 고정과 미실행 구간 재배열로(f17·f19) 나눠 다룬다.",
      "planned_findings": [
        "f5",
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
        "f19",
        "f1",
        "f4",
        "f28",
        "f29"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "5절 시작 조건·제약 칸을 공통 최상위 스키마 범위로 한정하고 ‘기타’(계산 실험) 사례 추가, 6절에 이진 우선순위 비용 요약(우선순위 검사 조건 명시)과 새 주제 페이지 링크, 7절 작업 요청 스키마·BinaryPriorityScheme·OR-Tools 행 갱신과 rmf_fleet_adapter 2.14.0 행 추가, 8절 머리 문장에 기존 주제 페이지 링크를 넣어 한정하고 Tuck 외·Dai 외 추가, 11절 머리 문장에 기존 열린 질문 페이지 링크를 넣고 oq-019·oq-049 부분 근거와 새 질문 3건, 13절 각주 갱신",
      "patches": [
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-03/pages/categories/planning-and-optimization/task-sequencing-and-scheduling.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-03/pages/categories/planning-and-optimization/task-sequencing-and-scheduling.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-03/pages/categories/planning-and-optimization/task-sequencing-and-scheduling.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-03/pages/categories/planning-and-optimization/task-sequencing-and-scheduling.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-03/pages/categories/planning-and-optimization/task-sequencing-and-scheduling.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-03/pages/categories/planning-and-optimization/task-sequencing-and-scheduling.md 의 해당 절을 본다)",
          "frontmatter": {
            "sources": [
              "ref-006",
              "ref-110",
              "ref-117",
              "ref-125",
              "ref-133",
              "ref-134",
              "ref-376",
              "ref-377",
              "ref-378",
              "ref-379",
              "ref-380",
              "ref-381",
              "ref-382",
              "ref-383",
              "ref-384",
              "ref-385",
              "ref-386",
              "ref-387",
              "ref-388",
              "ref-389",
              "ref-390",
              "ref-1483",
              "ref-1484",
              "ref-1485",
              "ref-1486",
              "ref-1398"
            ],
            "last_run": "2026-10-10",
            "confidence": "medium"
          }
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "신규 작성: Open-RMF 이진 우선순위 비용 벌점(우선순위 검사가 켜져 있을 때)과 비용 계산기 정의, 마감·누적 용량 제약 표현, 진행 중 동작을 고정하는 재계획(26. 작업 순서·스케줄링 6절 보강)"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area26-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 26. 작업 순서·스케줄링 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,369자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area26-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 26. 작업 순서·스케줄링 의 \"8. 대표 연구와 자료\" 절(1,194자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area26-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 26. 작업 순서·스케줄링 의 \"11. 열린 질문\" 절(931자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area26-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 26. 작업 순서·스케줄링 의 \"3. 왜 중요한가\" 절(722자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area26-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 26. 작업 순서·스케줄링 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(616자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-10 | 26. 작업 순서·스케줄링 | 5·6·7·8·11·13절 차등 갱신(이진 우선순위 비용 벌점 확인, 작업 요청 스키마 범위 한정, 계산 실험 사례 ‘기타’ 추가, rmf_fleet_adapter 2.14.0, Tuck 외·Dai 외 추가, 기존 주제 페이지 링크 유지), 주제 페이지 1건 신규 | run 2026-10-10-03",
  "index_updates": {
    "home_recent": "2026-10-10 — 26. 작업 순서·스케줄링: Open-RMF 이진 우선순위가 마감 보장이 아닌 비용 벌점(우선순위 검사가 켜져 있을 때)임을 확인하고, 마감·재계획 표현을 다룬 주제 페이지를 더했다",
    "category_recent": "2026-10-10 — 26. 작업 순서·스케줄링: 7절 BinaryPriorityScheme·작업 요청 스키마 행 갱신, 5절에 계산 실험 사례(현장 유형: 기타) 추가, 8절에 Tuck 외·Dai 외 추가",
    "area_recent": "2026-10-10 — 26. 작업 순서·스케줄링: 5·6·7·8·11절 갱신과 주제 페이지 ‘Open-RMF 이진 우선순위 비용과 마감·재계획 표현’ 신규(6절에서 연결)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "makespan",
      "term_ko": "메이크스팬",
      "term_en": "Makespan",
      "definition": "작업 집합 전체를 끝내는 데 걸린 시간으로, 일정 최적화에서는 가장 늦게 끝나는 작업(또는 로봇)의 종료 시각을 줄이는 목적으로 쓰인다.",
      "description": "다중 로봇 일정 연구(예: Dai 외 2025)가 최소화 목표로 쓴다. Open-RMF rmf_task 의 BinaryPriorityCostCalculator 가 더하는 작업별 (완료 시각 − 가장 이른 시작 시각)의 합과는 다른 지표다.",
      "related_areas": [
        26,
        25,
        39
      ],
      "sources": [
        "ref-379",
        "ref-1486"
      ]
    },
    {
      "action": "new",
      "slug": "satisfiability-modulo-theories",
      "term_ko": "이론 모듈로 만족 가능성",
      "term_en": "Satisfiability Modulo Theories (SMT)",
      "definition": "정수·비트벡터 산술 같은 배경 이론 위에서 논리식을 만족하는 값이 있는지 판정하는 문제와 그 해법기로, 일정·배정 제약을 논리식으로 풀 때 쓴다.",
      "description": "Tuck 외(2024)는 SMT 해법기의 증분 풀이로 동적 다중 로봇 작업 배정을 다뤘으며, 증분 풀이의 시간 이득은 해법기와 배치 크기에 따라 달랐다.",
      "related_areas": [
        26,
        25
      ],
      "sources": [
        "ref-1485"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-125",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_request.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 작업 요청 JSON 스키마. 최상위 필드 8개(가장 이른 시작 시각·요청 시각·우선순위·category·description·라벨·요청자·플릿 이름) 중 category·description 이 필수이며 마감·선후 필드는 없고, description·priority 는 플릿이 지원하는 스키마에 위임한다.",
      "cited_by": [
        "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
        "docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md"
      ],
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
      "summary": "Open-RMF 작업 계획기 헤더. 탐욕 방식(최적성 미보장, 더 빠를 수 있음)과 A* 방식(최적성 보장, 더 오래 걸릴 수 있음) 선택 옵션을 주석으로 설명한다.",
      "cited_by": [
        "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
        "docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md"
      ],
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
      "cited_by": [
        "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
        "docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md"
      ],
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
      "summary": "Open-RMF 이진 우선순위 비용 계산기 구현. 작업별 (완료 시각 − 가장 이른 시작 시각) 합을 비용으로 쓰고 충전 작업은 0 으로 두며, 우선순위 검사가 켜져 있을 때 우선순위 배분 위반이면 비용에 벌점 계수를 곱한다.",
      "cited_by": [
        "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
        "docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md"
      ],
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
      "cited_by": [
        "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
        "docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md"
      ],
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
      "cited_by": [
        "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
        "docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1486",
      "org": "Dai, W., Rai, U., Chiun, J., Cao, Y., & Sartoretti, G. (IEEE Robotics and Automation Letters)",
      "title": "Heterogeneous Multi-robot Task Allocation and Scheduling via Reinforcement Learning",
      "published": "2025-01-27",
      "url": "https://marmotlab.org/publications/73-RAL2025-HetMRTA.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "IEEE Robotics and Automation Letters 10(3), 2654–2661, DOI 10.1109/LRA.2025.3534682 (OpenAlex 서지 기록으로 확인). 필요한 로봇이 모두 모여야 시작하는 협업 작업에서 이종 로봇의 배정·일정을 강화학습으로 정하고 메이크스팬 최소화를 목표로 한다. 검증 단계에서 PDF 원문을 대조하지 못해 핵심 설정은 초록 요약 수준으로만 확인했다.",
      "cited_by": [
        "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md",
        "docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1398",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0)",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 태그 2.14.0 변경 이력. 2026-09-26 판에 단계 건너뛰기 요청 키 수정(#543)과 EasyTrafficLight 누적 지연 계산 수정(#524)이 들어 있다.",
      "cited_by": [
        "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "이진 우선순위에서 높은 작업이 계속 들어올 때 낮은 작업의 무한 대기를 막는 공개 정책이 있는가?",
      "areas": [
        26,
        25
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "제조사별 예상 완료 시간의 오차를 고려해 출하 마감 대비 여유 시간을 얼마나 두는가?",
      "areas": [
        26,
        20
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "작업 완료 시각 합, 납기 지연 합, 계획 변경량을 함께 최적화할 때 현장별 가중치를 어떻게 검증하는가? (관련 기존 질문: oq-054, oq-051)",
      "areas": [
        26,
        39
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "update",
      "id": "oq-019",
      "question": "상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가?",
      "areas": [
        23,
        26
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "update",
      "id": "oq-049",
      "question": "제조사가 다른 로봇 플릿 사이의 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 작업 요청 수준에서 표현·집행하는 표준 필드나 공개 구현이 있는가?",
      "areas": [
        20,
        25,
        26
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시",
      "title": "26. 작업 순서·스케줄링"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시",
      "title": "26. 작업 순서·스케줄링"
    },
    {
      "site_type": "기타",
      "item": "시작 조건",
      "link": "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시",
      "title": "26. 작업 순서·스케줄링 — 협업 작업 일정 계산 실험(현장 적용 사례 아님)"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시",
      "title": "26. 작업 순서·스케줄링 — 협업 작업 일정 계산 실험(현장 적용 사례 아님)"
    },
    {
      "site_type": "기타",
      "item": "제약",
      "link": "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시",
      "title": "26. 작업 순서·스케줄링 — 협업 작업 일정 계산 실험(현장 적용 사례 아님)"
    },
    {
      "site_type": "기타",
      "item": "예외·성과",
      "link": "docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시",
      "title": "26. 작업 순서·스케줄링 — 협업 작업 일정 계산 실험(현장 적용 사례 아님)"
    },
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md#4-현장-시나리오",
      "title": "Open-RMF 이진 우선순위 비용과 마감·재계획 표현"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md#4-현장-시나리오",
      "title": "Open-RMF 이진 우선순위 비용과 마감·재계획 표현"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md#4-현장-시나리오",
      "title": "Open-RMF 이진 우선순위 비용과 마감·재계획 표현"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md#4-현장-시나리오",
      "title": "Open-RMF 이진 우선순위 비용과 마감·재계획 표현"
    }
  ],
  "additional_research_requests": [
    "26. 작업 순서·스케줄링 6·7절과 주제 페이지 3절: rmf_task TaskPlanner.hpp 의 작업 배정 전략(TaskAssignmentStrategy: 완료 시각·배터리·바쁨 가중치)과 BinaryPriorityCostCalculator 의 관계를 확인해야 한다 — 이번에는 비용 설명을 이 계산기에 한정했고 계획기 목적 전체로 일반화하지 못했다(1차 검증 지시).",
    "26. 작업 순서·스케줄링 7절: BinaryPriorityCostCalculator 의 벌점 계수(priority_penalty) 기본값과 우선순위 검사(check_priority)가 기본으로 켜지는지를 헤더·계획기 코드에서 확인해야 한다 — 구현 파일에는 기본값이 없다.",
    "26. 작업 순서·스케줄링 5·8절: Dai 외(2025, ref-1486) 원문 대조가 필요하다 — 연합 능력 벡터 합 조건, 실행 기간 내내 함께 있어야 한다는 조건, 탐색·구조 모사 실험 틀, 최대 150 에이전트·500 작업·5종 능력 규모 수치를 원문으로 확인하지 못해 [추정]으로 두었다.",
    "26. 작업 순서·스케줄링 11절(oq-049): Open-RMF 의 다른 작업 유형 description 스키마(compose 등)에 마감·선행 작업 필드나 이를 집행하는 계획기 구현이 있는지 대조가 필요하다 — 이번에는 task_request.json 한 파일만 확인했다.",
    "26. 작업 순서·스케줄링 5절: 물류창고 외 현장 유형(제조 공장·병원·상업 시설 등)의 실제 작업 순서·스케줄링 적용 사례가 필요하다 — 이번에 더한 ‘기타’ 사례는 계산 실험이다.",
    "트랙 반영 제안 4건(실행 2026-09-25-51·66·77·98: HDDL 하위 작업 순서·VDA 5050 waitForTrigger, rmf_task 순서 계획과 LLM 직접 스케줄 생성 벤치마크, 재스케줄링 정책·방법 분류와 동결 구간, 재스케줄링 효율·안정성 지표)은 이번 브리프에 조사·검증한 finding 이 없어 6·7절에 반영하지 않았다 — 다음 26. 작업 순서·스케줄링 실행에서 조사·검증이 필요하며, AI 관련 내용은 47. AI·학습·적응과 모델 운영과 양쪽에 연결한다.",
    "리서치 기록 보완: ref-1485·ref-1486 은 fetched: true 인데 fetch_url 이 null 이다(1차 검증 지적).",
    "참고문헌 id 정리(퍼블리셔 담당): ref-1485 는 실행 2026-10-10-02 의 ref-1454 와, ref-1398 은 실행 2026-10-10-01 의 ref-1424·실행 2026-10-10-02 의 ref-1458 과 URL 이 같다. 이번 입력 docs_tree 에는 세 id 가 아직 게시되지 않아 이번 실행에서는 각 URL 을 한 번만 등록했으며, 먼저 게시된 id 로 합쳐 각주를 통일해야 한다.",
    "pipeline 담당 요청: 분량 초과 자동 분리가 원 절의 '자세한 내용은 주제 페이지 …' 같은 기존 링크 줄을 지운다(2차 검증 지적). 이번에는 링크를 머리 문장 안에 넣어 우회했으며, 분리 처리에서 기존 링크 줄을 보존하는지 확인이 필요하다."
  ],
  "fixes_applied": [
    "f20 분리 — 5절 ‘기타’ 사례 시작 조건 칸에 ‘필요한 로봇이 모두 작업 위치에 와야 시작하고 먼저 온 로봇의 대기를 줄이는 것이 목표’를 [사실]로, 연합 능력 벡터 합 조건을 [추정]+‘검증 단계에서 원문을 대조하지 못했다’로, 실행 기간 내내 동석 조건을 제약 칸에 [추정]+같은 병기로, 탐색·구조 모사 틀을 서술 단락에 [추정]+같은 병기로 나눠 썼다.",
    "‘기타’ 사례 표기 — 5절 사례 제목을 ‘현장을 특정하지 않은 협업 작업 일정 계산 실험(Dai 외, 2025) — 현장 적용 사례가 아니다’로 쓰고 서술에 ‘계산 실험이며 특정 현장의 적용 사례가 아니다’를 밝혔으며, 탐색·구조는 [추정] 범위로만 언급했고 site_matrix_updates 의 기타 칸 제목에 ‘협업 작업 일정 계산 실험(현장 적용 사례 아님)’을 넣었다.",
    "f23 강등 — 5절 수행 자원·예외·성과 칸과 8절 Dai 외 항목을 [추정]으로 쓰고, 150 에이전트·500 작업·5종 능력은 ‘저자 보고이며 검증 단계에서 원문을 대조하지 못했다’, 휴리스틱·MIP 대비 결과는 ‘저자 실험, 독립 재현 미확인’으로 병기했다.",
    "f12 괄호 정의 제거 — 주제 페이지 3절과 용어집 정의에서 ‘차고지 복귀를 포함한…’ 정의를 빼고 ‘Dai 외가 최소화하는 메이크스팬’까지만 썼다.",
    "f9·f11·f12·f25 주어 한정 — 주제 페이지 3절의 비용 정의 주어를 ‘BinaryPriorityCostCalculator(작업 계획기 헤더 주석상 비용 계산기를 지정하지 않으면 쓰는 계산기)’로, 8절 f25 문장도 같은 계산기로 한정했고 ‘이 계산기가 Open-RMF 계획기의 목적 전체를 대표하는지는 확인하지 못했다’를 적었으며 TaskAssignmentStrategy 관계 확인은 additional_research_requests 로 넘겼다.",
    "의견 주체 표시 — f4(5절 제약 칸·주제 1·5절), f8(7절 BinaryPriorityScheme 행·주제 3절), f16(주제 3절), f22(5절 ‘기타’ 서술), f25(8절), f27(7절 rmf_fleet_adapter 행), f28(11절·주제 7절)의 [의견] 문장마다 ‘이 위키의 판단(외부 조사 메모 기반)’을 넣었다.",
    "7절 BinaryPriorityScheme 행 — 새 행 없이 기존 행의 ‘비용 반영 방식은 미확인’을 높음 BinaryPriority(1)·낮음 nullptr, 로봇 사이 배분·로봇 안 순서 위반 시 비용에 벌점 계수를 곱한다는 [사실]로 바꾸고 f8 을 [의견]으로 덧붙였으며, 출처 칸에 ref-390 을 유지하고 ref-1484·ref-1483(f8 근거 ref-125 포함)을 더했다.",
    "작업 요청 스키마 범위 한정 — 7절 Open-RMF 작업 요청 스키마 행과 5절 물류창고 시작 조건 칸을 ‘공통 최상위 스키마(8개 필드, 필수 category·description)에 마감·선후 필드 없음, description·priority 는 플릿 지원 스키마에 위임’으로 고쳤고, 13절 ref-125 각주 접근일을 2026-10-10 으로 고쳤다.",
    "8절 머리 문장 — ‘성능 수치는 모두 저자 실험 결과이며 이 위키가 원문을 열지 못했다’를 2026-09-25 주제 페이지의 기존 항목에 한정하고, Tuck 외는 arXiv 원문을 열어 확인했고 Dai 외는 검증 단계에서 원문을 대조하지 못했다는 구분 문단을 더했다.",
    "ref-1486 서지 — reference_updates 의 published 를 2025-01-27 로 고치고, 각주·요약에 IEEE Robotics and Automation Letters 10(3), 2654–2661, DOI 10.1109/LRA.2025.3534682 를 적었으며 ‘게재지 미확인’ 문구를 지웠다(검증 단계 원문 미대조라 source_unopened: true, 각주에 ‘(원문 미열람)’ 표시).",
    "참고문헌 중복 — ref-1454·ref-1424·ref-1458 은 입력 docs_tree 에 게시되지 않아 이번에는 ref-1485·ref-1398 을 각 URL 당 한 번만 reference_updates 에 넣었고, 퍼블리셔가 같은 URL 을 먼저 게시된 id 로 합치도록 additional_research_requests 에 정리 요청을 적었다.",
    "새 열린 질문 3번 — 질문 끝에 ‘(관련 기존 질문: oq-054, oq-051)’을 붙여 open_question_updates 와 11절·주제 7절에 썼다.",
    "용어집 — 입력 용어집 색인에 ‘이론 모듈로 만족 가능성(SMT)’이 없어 신규로 냈고(같은 slug 면 퍼블리셔가 기존 항목으로 합침), ‘메이크스팬’ 정의는 ref-379·f12 범위 안에서 쓰고 차고지 복귀 같은 세부는 넣지 않았다.",
    "oq-019·oq-049 — 11절과 주제 7절에 부분 근거(f28 [의견], f29 [추정])만 덧붙이고 open_question_updates 에서 상태를 ‘열림’, link 는 null 로 두었다.",
    "트랙 반영 제안 4건 — HDDL·VDA 5050 waitForTrigger·LLM 스케줄 벤치마크·재스케줄링 분류·안정성 지표를 6·7절에 넣지 않고 다음 26. 작업 순서·스케줄링 실행으로 넘기도록 additional_research_requests 에 적었으며, ‘27. AI·학습·적응과 모델 운영’은 개정 분류의 ‘47. AI·학습·적응과 모델 운영’으로 표기했다.",
    "직접 인용 — ref-1483(BinaryPriorityCostCalculator.cpp)의 코드·주석은 직접 인용하지 않았고(0회), 비용식·검사 조건은 모두 재서술했다.",
    "2차: 8절 기존 주제 페이지 링크 복원 — ‘8. 대표 연구와 자료’ replace 패치의 머리 둘째 문장을 ‘[2026-09-25 에 정리한 기존 항목](../../topics/2026/2026-09-25-area14-s8.md)은 성능 수치가 모두 저자 실험 결과이며 이 위키가 원문을 열지 못했다.’로 바꿔 링크를 문장 안에 넣었고, 자동 분리에서 지워지는 별도 ‘자세한 내용은…’ 줄은 뺐다.",
    "2차: 11절 기존 열린 질문 페이지 링크 복원 — ‘11. 열린 질문’ 패치를 append 에서 replace 로 바꾸고 머리 둘째 문장을 ‘2026-09-25 까지의 질문은 [기존 열린 질문 정리](../../topics/2026/2026-09-25-area14-s11.md)에 있고, 전체 목록은 [열린 질문](../../open-questions.md)에 있다.’로 써서 링크를 문장 안에 넣었다(그 아래 2026-10-10 갱신 목록은 그대로).",
    "2차: f7 조건 보강 — (1) 세부영역 6절 append 패치, (2) 주제 페이지 1절 첫 항목, (3) 주제 페이지 4절 수행 자원 칸, (4) 7절 BinaryPriorityScheme 행에 ‘우선순위 검사가 켜져 있으면’ 조건을 넣어 벌점 계수를 곱하는 진술을 한정했다.",
    "분량 초과 자동 분리: 26. 작업 순서·스케줄링 본문 8,224자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 4,108자"
  ]
}
```

### runs/2026-10-10-03/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md (6개 절)
- 분량 초과 자동 분리:
    - docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-10-area26-s7.md (1,369자)
    - docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-10-area26-s8.md (1,194자)
    - docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md "11. 열린 질문" → docs/topics/2026/2026-10-10-area26-s11.md (931자)
    - docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md "3. 왜 중요한가" → docs/topics/2026/2026-10-10-area26-s3.md (722자)
    - docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-10-area26-s10.md (616자)
```

### runs/2026-10-10-03/pages/categories/planning-and-optimization/task-sequencing-and-scheduling.md

```markdown
---
title: "26. 작업 순서·스케줄링"
type: area
category: "G. 계획·최적화"
area_no: 26
related_areas: [20, 23, 24, 25, 27, 28, 31, 35, 39]
tags: [작업 순서, 스케줄링, 주문 배치, 선후 제약, 시간창, Open-RMF]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-10-10
sources: [ref-006, ref-110, ref-117, ref-125, ref-133, ref-134, ref-376, ref-377, ref-378, ref-379, ref-380, ref-381, ref-382, ref-383, ref-384, ref-385, ref-386, ref-387, ref-388, ref-389, ref-390, ref-1483, ref-1484, ref-1485, ref-1486, ref-1398]
last_run: 2026-10-10
version: 3
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

자세한 내용은 주제 페이지 [26. 작업 순서·스케줄링 — 왜 중요한가](../../topics/2026/2026-10-10-area26-s3.md)에 있다.

## 4. 핵심 개념과 용어

작업 순서를 다루려면 무엇을 묶고, 무엇이 먼저이며, 언제까지 해야 하는지를 표현하는 말이 필요하다.

자세한 내용은 주제 페이지 [26. 작업 순서·스케줄링 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area14-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 2026-10-10 에는 현장을 특정하지 않은 계산 실험을 현장 유형 ‘기타’로 따로 더했으며, 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹 → 포장 → 출하

**시나리오:** 랙 이동 로봇 작업대의 피킹 순서를 포장대 도착에 맞추고 출하 마감이 임박한 주문을 끼워 넣기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 시스템이 주문 줄이 적은 시간 임박 주문을 연속으로 내린다. [사실][^ref-382] 긴급 주문을 Open-RMF 요청으로 보낼 때 공통 최상위 스키마(8개 필드, 필수는 category·description)에서 시각 관련 필드는 가장 이른 시작 시각과 요청 시각뿐이고, 마감 시각이나 다른 작업과의 선후 필드는 없다(2026-10-10 확인). [사실][^ref-125] 작업 내용(description)과 우선순위(priority)는 플릿이 지원하는 스키마를 따르도록 위임되어 있다. [사실][^ref-125] |
| 작업 대상 | 로봇이 작업대로 옮기는 랙과 주문별 빈, 풋월의 주문 칸 [사실][^ref-381][^ref-385] |
| 수행 자원 | 랙 이동 로봇, 작업대 피커, 포장 작업자. 복수 포장대와 피킹-패킹 전환 정책(작업자가 피킹과 포장 사이를 옮겨 감)의 작업자 스케줄링을 다룬 국내 연구가 있다(2025, 결과 수치 미확인). [사실][^ref-388] |
| 제약 | 랙 도착 → 피킹 → 주문별 통합 → 포장의 선후가 있고, 배치·구역 피킹 뒤에는 주문별 통합이 필요하다. [사실][^ref-381][^ref-385] 공통 최상위 스키마에 마감 필드가 없으므로 긴급 작업을 끼워 넣고 대기 작업을 재정렬하는 규칙은 ROP 쪽에서 따로 정해야 할 것으로 보인다. [추정][^ref-125][^ref-390] 다만 이 부재가 유형별 description 확장이나 플릿별 우선순위 스키마로 그런 조건을 구현하는 것이 불가능하다는 뜻은 아닐 것으로 보이며, 확장 필드를 실제로 집행하는 계획기 구현은 확인하지 못했다. [추정][^ref-125] 이 위키의 판단(외부 조사 메모 기반)으로는 문법상 추가 필드를 넣을 수 있다는 것과 계획기가 그 필드를 집행한다는 것을 구분해, 확장 계약과 집행 주체를 따로 명시해야 한다. [의견][^ref-125] |
| 완료·인계 | 한 주문의 물품이 풋월 칸에 모두 모여야 포장으로 넘어간다. [사실][^ref-385] 피킹 로봇 완료 뒤 운반 로봇 출발처럼 제조사가 다른 플릿 사이 인계는 ROP 가 작업 흐름 수준에서 관리해야 할 것으로 보인다. [추정][^ref-376][^ref-125] |
| 예외·성과 | 빈 방출 순서가 맞지 않으면 포장 작업자가 유휴 대기한다. [사실][^ref-385] 편의점 물류센터 레이아웃 기준 국내 연구는 배치 피킹이 분배·포장 시간을 줄였지만 총 주문 처리 시간은 피킹 시간이 결정했다고 보고했다(2024). [사실][^ref-387] |

다음은 설명을 위한 가상의 시나리오이다. 이 영역이 관여하는 칸은 주로 제약과 완료·인계다. 작업대 앞의 랙 순서는 뒤쪽 풋월과 포장대가 기다리지 않도록 정해져야 하고, 긴급 주문이 들어오면 이미 대기 중인 작업을 어디까지 밀어낼지 정해야 한다.

출하 단계까지 넓히면 피킹과 분류를 배송 요구에 맞춰 동기화하는 문제가 된다. 피킹·분류가 어긋나면 긴급 품목이 빠져 추가 피킹이 생긴다는 문제 제기가 있다. [사실][^ref-386]

**현장 유형:** 기타

**사례:** 현장을 특정하지 않은 협업 작업 일정 계산 실험(Dai 외, 2025) — 현장 적용 사례가 아니다

| 항목 | 내용 |
|---|---|
| 시작 조건 | 필요한 로봇이 모두 작업 위치에 와야 작업을 시작하며, 먼저 온 로봇의 대기를 줄이는 것이 목표다. [사실][^ref-1486] 배정된 로봇 연합의 능력 벡터 합이 작업 요구를 충족해야 시작한다는 조건은 검증 단계에서 원문을 대조하지 못했다. [추정][^ref-1486] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 능력이 다른 이종 로봇이 다음 작업을 분산적으로 고르며, 그 협업 일정 정책을 강화학습(Reinforcement Learning, RL)으로 학습한다. [추정][^ref-1486] |
| 제약 | 모든 배정 로봇이 실행 기간 내내 작업 위치에 함께 있어야 한다는 조건은 검증 단계에서 원문을 대조하지 못했다. [추정][^ref-1486] 개별 로봇이 빨리 도착해도 다른 팀원이 늦으면 작업 시작이 늦어지므로, 개별 로봇의 빠른 도착만으로 전체 종료 시간이 줄지는 않을 것으로 보인다. [추정][^ref-1486] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 저자는 휴리스틱과 혼합 정수 계획(Mixed Integer Programming, MIP) 기준선보다 비슷하거나 나은 결과를 두 자릿수 이상 빠르게 얻었다고 보고한다(저자 실험, 독립 재현 미확인). [추정][^ref-1486] |

이 사례는 계산 실험이며 특정 현장의 적용 사례가 아니다. 실험이 탐색·구조 같은 협업 과제를 모사한 것이라는 설명은 검증 단계에서 원문을 대조하지 못했다. [추정][^ref-1486] 이 위키의 판단(외부 조사 메모 기반)으로는 이 사례를 이용하면 일정 설명에서 도착 동기화, 공동 작업 시간, 다음 작업으로의 이동을 구분해 적을 수 있으나, 물류창고의 피킹–포장 인계 구현과 같다고 보지는 않는다. [의견][^ref-1486]

## 6. 대표 접근법과 기술

앞의 시나리오에서 순서를 정하는 방법은 크게 여섯 갈래로 연구되어 있다.

자세한 내용은 주제 페이지 [26. 작업 순서·스케줄링 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area14-s6.md)에 있다.

### 2026-10-10 갱신: 우선순위 비용·제약 표현·재계획

Open-RMF rmf_task 의 이진 우선순위 비용 계산기는 마감을 검사하지 않고, 우선순위 검사가 켜져 있으면 우선순위 배분을 어긴 배정의 비용에 벌점 계수를 곱한다. [사실][^ref-1483] 이 계산기의 실비용 정의, 제약 프로그래밍의 누적 용량 제약과 마감을 필수 조건으로 둔 정식화, 진행 중 동작을 고정하는 온라인 재계획은 주제 페이지 [Open-RMF 이진 우선순위 비용과 마감·재계획 표현](../../topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md)에 정리했다.

## 7. 관련 표준·프레임워크·오픈소스

위 접근법을 현장 시스템에 옮길 때 참조하는 표현 형식과 도구는 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [26. 작업 순서·스케줄링 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-10-area26-s7.md)에 있다.

## 8. 대표 연구와 자료

6절의 접근법을 뒷받침하는 연구다. [2026-09-25 에 정리한 기존 항목](../../topics/2026/2026-09-25-area14-s8.md)은 성능 수치가 모두 저자 실험 결과이며 이 위키가 원문을 열지 못했다.

자세한 내용은 주제 페이지 [26. 작업 순서·스케줄링 — 대표 연구와 자료](../../topics/2026/2026-10-10-area26-s8.md)에 있다.

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

자세한 내용은 주제 페이지 [26. 작업 순서·스케줄링 — 다른 연구영역과의 연결](../../topics/2026/2026-10-10-area26-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 이번 조사로 근거가 늘었지만 답을 확인하지 못한 것이다. 2026-09-25 까지의 질문은 [기존 열린 질문 정리](../../topics/2026/2026-09-25-area14-s11.md)에 있고, 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [26. 작업 순서·스케줄링 — 열린 질문](../../topics/2026/2026-10-10-area26-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [26. 작업 순서·스케줄링](task-sequencing-and-scheduling.md) — 영역 심화: 섹션 3~11 신규 작성(4·6·8·11절은 주제 페이지로 분리), 2차 수정 지시 4건 반영(9절 경계 칸, 10절 태그, 5절 시작 조건·제약 칸) (실행 2026-09-25-34)
- 2026-09-25 · 생성 · [26. 작업 순서·스케줄링 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area14-s6.md) — 자동 분리: 14. 작업 순서·스케줄링 의 "6. 대표 접근법과 기술" 절(1,504자)을 옮겼다 (실행 2026-09-25-34)
- 2026-09-25 · 생성 · [26. 작업 순서·스케줄링 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area14-s4.md) — 자동 분리: 14. 작업 순서·스케줄링 의 "4. 핵심 개념과 용어" 절(985자)을 옮겼다 (실행 2026-09-25-34)
- 2026-09-25 · 생성 · [26. 작업 순서·스케줄링 — 대표 연구와 자료](../../topics/2026/2026-09-25-area14-s8.md) — 자동 분리: 14. 작업 순서·스케줄링 의 "8. 대표 연구와 자료" 절(904자)을 옮겼다 (실행 2026-09-25-34)
- 2026-09-25 · 생성 · [26. 작업 순서·스케줄링 — 열린 질문](../../topics/2026/2026-09-25-area14-s11.md) — 자동 분리: 14. 작업 순서·스케줄링 의 "11. 열린 질문" 절(865자)을 옮겼다 (실행 2026-09-25-34)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-117]: MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd, 접근일 2026-09-25
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-10-10
[^ref-376]: Open Robotics, Tasks in RMF (task) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task.html, 접근일 2026-09-25
[^ref-380]: de Koster, R., Le-Duc, T., & Roodbergen, K. J., Design and control of warehouse order picking: A literature review, 2007, https://pure.eur.nl/en/publications/design-and-control-of-warehouse-order-picking-a-literature-review/, 접근일 2026-09-25 (원문 미열람)
[^ref-381]: Boysen, N., Briskorn, D., & Emde, S., Parts-to-picker based order processing in a rack-moving mobile robots environment, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758, 접근일 2026-09-25 (원문 미열람)
[^ref-382]: Boysen, N., de Koster, R., & Weidinger, F., Warehousing in the e-commerce era: A survey, 2019, https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/, 접근일 2026-09-25 (원문 미열람)
[^ref-385]: Boysen, N., Stephan, K., & Weidinger, F., Manual order consolidation with put walls: the batched order bin sequencing problem, 2019, https://www.sciencedirect.com/science/article/pii/S2192437620300315, 접근일 2026-09-25 (원문 미열람)
[^ref-386]: Jiang, M., & Huang, G. Q., Intralogistics synchronization in robotic forward-reserve warehouses for e-commerce last-mile delivery, 2022, https://www.sciencedirect.com/science/article/abs/pii/S1366554522000175, 접근일 2026-09-25 (원문 미열람)
[^ref-387]: 신희철, 이강현, 방선호, 신광섭(한국빅데이터학회 학회지), 물류센터 생산성 향상을 위한 피킹스케줄링 문제에 관한 연구, 2024, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003163116, 접근일 2026-09-25 (원문 미열람)
[^ref-388]: Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지), 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링, 2025, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570, 접근일 2026-09-25 (원문 미열람)
[^ref-390]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/BinaryPriorityScheme.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/BinaryPriorityScheme.hpp, 접근일 2026-09-25
[^ref-1483]: Open Robotics (open-rmf), rmf_task — rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp, 접근일 2026-10-10
[^ref-1486]: Dai, W., Rai, U., Chiun, J., Cao, Y., & Sartoretti, G. (IEEE Robotics and Automation Letters 10(3), 2654–2661, DOI 10.1109/LRA.2025.3534682), Heterogeneous Multi-robot Task Allocation and Scheduling via Reinforcement Learning, 2025-01-27, https://marmotlab.org/publications/73-RAL2025-HetMRTA.pdf, 접근일 2026-10-10 (원문 미열람)
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

### runs/2026-10-10-03/pages/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md

```markdown
---
title: "Open-RMF 이진 우선순위 비용과 마감·재계획 표현"
type: topic
category: "G. 계획·최적화"
primary_area_no: 26
related_areas: [25, 28, 23, 20, 39]
tags: [이진 우선순위, 비용 벌점, 누적 용량 제약, 마감, 온라인 재계획]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-125, ref-377, ref-379, ref-1483, ref-1484, ref-1485, ref-1486]
last_run: 2026-10-10
version: 1
---

[홈](../../index.md) › [주제](../index.md) › Open-RMF 이진 우선순위 비용과 마감·재계획 표현

# Open-RMF 이진 우선순위 비용과 마감·재계획 표현

**주 연구영역:** [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) · **관련 영역:** [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) · **실행:** 2026-10-10-03

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Open-RMF rmf_task 의 이진 우선순위 비용 계산기는 마감을 검사하지 않고, 우선순위 검사가 켜져 있으면 우선순위 배분을 어긴 배정의 비용에 벌점 계수를 곱한다. [사실][^ref-1483]
- 이 위키의 판단(외부 조사 메모 기반)으로는 ROP 가 출하 마감이나 작업 간 선후를 지키려면 그 조건의 확장 계약과 집행 주체를 공통 요청 스키마 밖에서 따로 정해야 한다. [의견][^ref-125]
- 유형별 description 확장으로 마감·선후를 실제로 집행하는 구현과, 진행 중 작업을 재정렬하는 현장 설계는 확인하지 못했다. [추정][^ref-125]

## 2. 배경

이 글은 26. 작업 순서·스케줄링의 핵심 질문에서 출발했다.

일이 계속 새로 들어올 때 무엇을 먼저, 언제 할지 어떻게 정할 것인가? [분류원문]

세부영역 페이지 7절은 Open-RMF 이진 우선순위의 비용 반영 방식을 미확인으로 남겨 두었고, [열린 질문](../../open-questions.md) oq-019(출고 우선순위로 진행 중 작업 재정렬)와 oq-049(제조사가 다른 플릿 사이 작업 선후)가 답을 기다린다. 실행 2026-10-10-03 은 외부 조사 메모를 원문과 대조해 이 빈칸을 다시 확인했다.

## 3. 본문

### 이진 우선순위는 비용 벌점이다

rmf_task 의 이진 우선순위 체계는 낮은 우선순위를 nullptr, 높은 우선순위를 BinaryPriority(1) 로 만들고 BinaryPriorityCostCalculator 를 비용 계산기로 돌려준다. [사실][^ref-1484] 이 계산기는 두 경우를 위반으로 본다. 같은 계획 노드에서 한 로봇이 높은 작업을 2개 이상 받았는데 높은 작업이 없는 로봇이 있는 경우, 그리고 같은 로봇의 순서에서 충전 작업을 건너뛰고 보았을 때 낮은 작업 뒤에 높은 작업이 오는 경우다. [사실][^ref-1483] 우선순위 검사가 켜져 있고 배정이 위반이면 비용은 벌점 계수 × (g + h), 아니면 g + h 다. [사실][^ref-1483]

이 위키의 판단(외부 조사 메모 기반)으로는 이 처리가 납기를 직접 검사하는 코드가 아니므로 높은 우선순위를 마감 보장으로 해석하면 안 되고, 로봇 사이 배분 조건이 있어 단순한 선입선출 정렬로 설명해서도 안 된다. [의견][^ref-1483][^ref-125]

### 비용 계산기가 더하는 값

BinaryPriorityCostCalculator(작업 계획기 헤더 주석상 비용 계산기를 지정하지 않으면 쓰는 계산기[^ref-377])의 실비용 g 는 각 일반 작업의 (완료 시각 − 그 요청의 가장 이른 시작 시각)을 모든 로봇·모든 배정에 걸쳐 더한 값이다. [사실][^ref-1483] 충전 작업 배정 자체의 비용은 0 이다. [사실][^ref-1483] 다만 충전 때문에 같은 로봇의 뒤 작업 완료가 늦어지면 그 작업의 비용은 커질 수 있을 것으로 보인다. [추정][^ref-1483] 이 계산기가 Open-RMF 계획기의 목적 전체를 대표하는지는 확인하지 못했다. 이 위키의 판단(외부 조사 메모 기반)으로는 이 비용을 Dai 외가 최소화하는 메이크스팬(Makespan)이나 납기 지연 합과 같은 지표라고 부르면 안 된다. [의견][^ref-1483][^ref-1486]

### 마감과 용량을 제약으로 표현하기

OR-Tools CP-SAT 스케줄링 문서는 구간 변수, 선택 구간, 구간 사이 시간 관계, 겹침 금지에 더해 구간별 수요의 합이 용량 프로필을 넘지 않게 하는 누적 용량(Cumulative) 제약을 다룬다. [사실][^ref-379] 이 표현으로 ‘이전 작업 종료 뒤 시작’, ‘도크는 한 번에 한 작업’, ‘작업대 동시 사용량은 용량 이하’를 서로 다른 제약으로 쓸 수 있을 것으로 보이나, 문서의 예제는 로봇·도크 사례가 아닌 일반 스케줄링 예제다. [추정][^ref-379] Tuck 외(2024)의 동적 작업 배정 정식화는 내려놓기 동작이 마감 전에 일어나야 작업을 완료한 것으로 보아 마감을 필수 조건으로 둔다. [사실][^ref-1485] 이 위키의 판단(외부 조사 메모 기반)으로는 마감을 반드시 지킬 조건으로 둘지 어겼을 때 비용을 주는 조건으로 둘지를 목적함수와 제약식으로 나눠 설계해야 한다. [의견][^ref-379][^ref-1485]

### 진행 중 동작을 고정하는 재계획

Tuck 외는 새 작업이 들어올 때 각 로봇의 과거 동작과 현재 동작을 바꾸지 않은 채 계획을 갱신하도록 정의한다. [사실][^ref-1485] 이를 참고하면 긴급 작업 삽입 정책을 ‘현재 동작 고정’과 ‘아직 실행하지 않은 구간의 재배열’로 나눠 기술할 수 있을 것으로 보이나, 이동 시간이 불확실한 조건의 실행 성능 보장으로 넓히지는 않는다. [추정][^ref-1485]

## 4. 현장 시나리오

**현장 유형:** 물류창고

**사례:** 출하 마감이 임박한 주문을 이진 우선순위 요청으로 끼워 넣기(피킹 → 출하)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 시스템이 출하 마감이 임박한 주문을 내린다. Open-RMF 공통 요청 스키마로는 가장 이른 시작 시각과 우선순위를 줄 수 있지만 마감 시각 필드는 없다. [사실][^ref-125] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 한 플릿의 로봇들. 우선순위 검사가 켜져 있으면, 높은 작업이 한 로봇에 2개 이상 몰리고 높은 작업이 없는 로봇이 있을 때 배정 비용에 벌점이 붙는다. [사실][^ref-1483] |
| 제약 | 도크·작업대 동시 사용량은 누적 용량 제약으로 쓸 수 있을 것으로 보인다. [추정][^ref-379] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 긴급 주문이 들어오면 현재 동작은 고정하고 아직 실행하지 않은 구간만 재배열하는 정책으로 나눠 기술할 수 있을 것으로 보인다. [추정][^ref-1485] |

다음은 설명을 위한 가상의 사례이다. 이 영역이 관여하는 칸은 제약과 예외·성과다. 이 위키의 판단(외부 조사 메모 기반)으로는 마감이 실제로 지켜지는지는 우선순위 값이 아니라, 마감을 제약으로 표현하고 집행하는 주체가 있는지에 달려 있다. [의견][^ref-125][^ref-1483]

## 5. ROP 관점의 시사점

**직접 범위:**
- 상위 시스템에서 받은 출하 마감·작업 선후를 Open-RMF 공통 요청 스키마 밖의 확장 계약으로 정의하고 집행 주체를 명시하는 일이 ROP 쪽에 남는다는 것이 이 위키의 판단(외부 조사 메모 기반)이다. [의견][^ref-125]
- 긴급 작업 삽입 규칙은 ‘현재 동작 고정’과 ‘미실행 구간 재배열’로 나눠 정할 수 있을 것으로 보인다. [추정][^ref-1485]

**연계 범위:**
- 연계 대상: 출하 마감 시각 자체의 결정은 분류 원문 19장의 상위 업무 시스템 경계(WMS 등)에 속한다. [추정][^ref-125]

## 6. 연결되는 연구영역

- [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) — 이 글의 출발 영역이며, 7절 BinaryPriorityScheme 행과 11절 열린 질문을 보강한다.
- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 이진 우선순위 벌점이 로봇 사이 높은 작업 배분을 조건으로 삼는다.
- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 충전 작업의 비용과 뒤 작업 지연을 다룬다.
- [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) — 출하 마감을 상위 시스템에서 받는 쪽이다(oq-019).
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 플릿별 우선순위 스키마와 플릿 사이 선후(oq-049)를 다룬다.
- [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) — 완료 시각 합·납기 지연 합·메이크스팬 같은 지표를 구분한다.

## 7. 열린 질문

- **oq-019** (상태: 열림) 출고 우선순위로 진행 중 작업을 재정렬하는 공개 설계나 사례 — 3절의 이진 우선순위 표현·벌점은 부분 근거일 뿐이며 재정렬 현장 설계는 찾지 못했다는 것이 이 위키의 판단(외부 조사 메모 기반)이다. [의견][^ref-1483][^ref-1484]
- **oq-049** (상태: 열림) 제조사가 다른 플릿 사이 작업 선후의 표준 필드나 공개 구현 — 공통 요청 스키마에는 선행 작업 ID 가 없고 유형별 description 확장 경로만 있어, 이 경로만으로 선후 집행이 구현되었다고 볼 수 없다. [추정][^ref-125]
- 새 질문 3건(상태: 열림): 높은 작업이 계속 들어올 때 낮은 작업의 무한 대기를 막는 공개 정책, 제조사별 완료 시간 오차를 고려한 출하 마감 여유 시간, 작업 완료 시각 합·납기 지연 합·계획 변경량의 현장별 가중치 검증(관련 기존 질문: oq-054, oq-051). 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 8. 출처

[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-10-10
[^ref-377]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp, 접근일 2026-10-10
[^ref-379]: Google (google/or-tools GitHub), OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver), 미확인, https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md, 접근일 2026-10-10
[^ref-1483]: Open Robotics (open-rmf), rmf_task — rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp, 접근일 2026-10-10
[^ref-1484]: Open Robotics (open-rmf), rmf_task — rmf_task/src/rmf_task/BinaryPriorityScheme.cpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityScheme.cpp, 접근일 2026-10-10
[^ref-1485]: Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (UC Berkeley, Toyota Motor North America), SMT-Based Dynamic Multi-Robot Task Allocation, 2024-03-18, https://arxiv.org/html/2403.11737v1, 접근일 2026-10-10
[^ref-1486]: Dai, W., Rai, U., Chiun, J., Cao, Y., & Sartoretti, G. (IEEE Robotics and Automation Letters 10(3), 2654–2661, DOI 10.1109/LRA.2025.3534682), Heterogeneous Multi-robot Task Allocation and Scheduling via Reinforcement Learning, 2025-01-27, https://marmotlab.org/publications/73-RAL2025-HetMRTA.pdf, 접근일 2026-10-10 (원문 미열람)

## 9. 검증 노트

- 판정: 1차 조건부 승인 / 2차 대기
- 확인·미확인: 확인 27건 · 미확인 2건 · 교차 확인 0건
- 강등된 주장: f20 사실 → 일부 추정, f23 사실 → 추정
- 검증자 주의: 판정: 조건부 승인. 확인 27건, 미확인 2건, 교차 확인 0건(rmf_task 헤더·구현·스키마는 같은 프로젝트 자료라 독립 교차 확인으로 세지 않았다). 강등: f20 사실 → 일부 추정(연합 능력 조건·탐색·구조 모사 틀을 원문으로 대조하지 못함), f23 사실 → 추정(150 에이전트·500 작업·5종 능력 규모 수치 미확인). 원문 미열람 출처: ref-1486(Dai 외) — 검증 단계에서 PDF 텍스트를 뽑지 못했다. 실재와 서지(IEEE RA-L 10(3), 2025-01-27, DOI 10.1109/LRA.2025.3534682, 저자 5명)는 OpenAlex 로, 핵심 설정(필요한 로봇이 모두 모여야 시작, 메이크스팬 최소화, 휴리스틱·MIP 대비 두 자릿수 이상 빠름)은 초록 요약으로만 확인했다. ref-125·ref-377·ref-379 는 입력 원문 텍스트로, ref-1483·ref-1484·ref-1398 은 GitHub raw 로, ref-1485 는 arXiv HTML 로 원문을 대조했다. 브리프의 ref-1485·ref-1486 은 fetched: true 인데 fetch_url 이 null 이다(리서치 기록 누락). 주의: Open-RMF 비용 설명은 비용 계산기를 지정하지 않았을 때 쓰는 BinaryPriorityCostCalculator 에 한정된다. 같은 헤더의 TaskAssignmentStrategy(완료 시각·배터리·바쁨 가중치)와의 관계는 미확인이다. 이진 우선순위는 비용 벌점이며 마감 보장이 아니다. Tuck 외와 Dai 외는 계산 실험이고, 5절 '기타' 사례는 현장 실증이 아니다. 같은 URL 의 출처가 이전 실행(ref-1454, ref-1424·ref-1458)과 겹쳐 id 통일이 필요하다. 트랙 반영 제안 4건은 이번 브리프가 다루지 않아 반영하지 않고 다음 실행으로 넘긴다. 정정 요청 없음. 열린 질문 oq-019·oq-049 는 부분 근거만 추가하고 해결로 인정하지 않는다. 검증 검색 6회를 썼다.
- 신뢰도: medium

## 10. 이력

| 날짜 | 실행 id | 변경 | 버전 |
|---|---|---|---|
| 2026-10-10 | 2026-10-10-03 | 신규 작성 | 1 |
```

### runs/2026-10-10-03/pages/topics/2026/2026-10-10-area26-s7.md

```markdown
---
title: "26. 작업 순서·스케줄링 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "G. 계획·최적화"
primary_area_no: 26
related_areas: [20, 23, 24, 25, 27, 28, 31, 35, 39]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-110, ref-117, ref-125, ref-1483, ref-1484, ref-1398, ref-376, ref-377, ref-378, ref-379, ref-390]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#7
---

[홈](../../index.md) › [주제](../index.md) › 26. 작업 순서·스케줄링 — 관련 표준·프레임워크·오픈소스

# 26. 작업 순서·스케줄링 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 위 접근법을 현장 시스템에 옮길 때 참조하는 표현 형식과 도구는 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

위 접근법을 현장 시스템에 옮길 때 참조하는 표현 형식과 도구는 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| B2MML 공통 스키마 Dependency1Type | 표준 | 두 요소 사이 실행 의존(선후·병행 금지·시작 후 간격 등) 표현. 창고 물류 적용 사례는 미확인 [사실] | [^ref-117] |
| Open-RMF 작업 요청 스키마(task_request.json) | 오픈소스 | 공통 최상위 필드 8개(필수는 category·description) 가운데 시각 관련은 가장 이른 시작 시각·요청 시각뿐이고 마감·선후 필드는 없다. description·priority 는 플릿이 지원하는 스키마에 위임한다(2026-10-10 확인) [사실] | [^ref-125] |
| Open-RMF 작업 V2 | 오픈소스 | 작업을 단계의 연쇄·조합으로 구성 [사실] | [^ref-110] |
| Open-RMF 디스패처 | 오픈소스 | 입찰로 플릿 선정, 평가기 설정 가능 [사실] | [^ref-376][^ref-378] |
| Open-RMF rmf_task TaskPlanner | 오픈소스 | 플릿 안 일정 계획, 충전 작업 삽입, 탐욕·A* 선택 [사실] | [^ref-377] |
| Open-RMF BinaryPriorityScheme | 오픈소스 | 높음·낮음 두 단계 우선순위. 높음은 BinaryPriority(1), 낮음은 nullptr 로 만들고 비용 계산기로 BinaryPriorityCostCalculator 를 쓴다. 우선순위 검사가 켜져 있으면, 같은 계획 노드에서 높은 작업이 한 로봇에 2개 이상 몰렸는데 높은 작업이 없는 로봇이 있거나(로봇 사이 배분), 같은 로봇의 순서에서 충전 작업을 건너뛰고 보았을 때 낮은 작업 뒤에 높은 작업이 올 때(로봇 안 순서) 배정 비용에 벌점 계수를 곱한다 [사실]. 이 위키의 판단(외부 조사 메모 기반)으로는 비용 벌점이므로 높은 우선순위를 마감 보장으로 해석하면 안 되고 단순한 선입선출 정렬로 설명해서도 안 된다 [의견] | [^ref-390][^ref-1484][^ref-1483][^ref-125] |
| OR-Tools CP-SAT | 오픈소스 | 구간 변수·겹침 금지·선택 구간·선후 부등식, 그리고 구간별 수요의 합이 용량 프로필을 넘지 않게 하는 누적 용량(Cumulative) 제약으로 스케줄링 표현 [사실]. 문서의 예제는 로봇·도크 사례가 아닌 일반 스케줄링 예제다 | [^ref-379] |
| Open-RMF rmf_fleet_adapter 2.14.0 변경 이력 | 오픈소스 | 2.14.0(2026-09-26) 변경 이력에 단계 건너뛰기 요청의 단계 키 수정(#543)과 EasyTrafficLight 누적 지연 계산 수정(#524)이 있다 [사실]. 이 위키의 판단(외부 조사 메모 기반)으로는 일정의 예외 조정과 지연 기반 추정에 의존하는 구현은 사용하는 Open-RMF 패키지 버전을 함께 기록하는 편이 좋다 [의견] | [^ref-1398] |

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md)
- 관련 영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-110]: Open Robotics, Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-25
[^ref-117]: MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd, 접근일 2026-09-25
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-10-10
[^ref-1483]: Open Robotics (open-rmf), rmf_task — rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp, 접근일 2026-10-10
[^ref-1484]: Open Robotics (open-rmf), rmf_task — rmf_task/src/rmf_task/BinaryPriorityScheme.cpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityScheme.cpp, 접근일 2026-10-10
[^ref-1398]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0), 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-10
[^ref-376]: Open Robotics, Tasks in RMF (task) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task.html, 접근일 2026-09-25
[^ref-377]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp, 접근일 2026-10-10
[^ref-378]: Open Robotics (open-rmf), rmf_ros2 — rmf_task_ros2/include/rmf_task_ros2/Dispatcher.hpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/include/rmf_task_ros2/Dispatcher.hpp, 접근일 2026-09-25
[^ref-379]: Google (google/or-tools GitHub), OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver), 미확인, https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md, 접근일 2026-10-10
[^ref-390]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/BinaryPriorityScheme.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/BinaryPriorityScheme.hpp, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-03 | 26. 작업 순서·스케줄링 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-10-03/pages/topics/2026/2026-10-10-area26-s8.md

```markdown
---
title: "26. 작업 순서·스케줄링 — 대표 연구와 자료"
type: topic
category: "G. 계획·최적화"
primary_area_no: 26
related_areas: [20, 23, 24, 25, 27, 28, 31, 35, 39]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-1485, ref-1486, ref-377]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#8
---

[홈](../../index.md) › [주제](../index.md) › 26. 작업 순서·스케줄링 — 대표 연구와 자료

# 26. 작업 순서·스케줄링 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 6절의 접근법을 뒷받침하는 연구다. [2026-09-25 에 정리한 기존 항목](2026-09-25-area14-s8.md)은 성능 수치가 모두 저자 실험 결과이며 이 위키가 원문을 열지 못했다.
- 이 페이지는 [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

6절의 접근법을 뒷받침하는 연구다. [2026-09-25 에 정리한 기존 항목](2026-09-25-area14-s8.md)은 성능 수치가 모두 저자 실험 결과이며 이 위키가 원문을 열지 못했다.

2026-10-10 에 더한 두 연구는 원문 확인 수준이 다르다. Tuck 외는 이 위키가 arXiv 원문(v1)을 열어 정의와 실험 결론을 확인했고, Dai 외는 서지와 초록 요약만 확인했으며 검증 단계에서 원문을 대조하지 못했다.

- Tuck 외, SMT-Based Dynamic Multi-Robot Task Allocation(2024-03, arXiv 프리프린트) — 마감이 있는 작업이 온라인으로 들어오고 로봇이 여러 작업을 동시에 실을 수 있는 동적 다중 로봇 작업 배정(Multi-Robot Task Allocation, MRTA)을 다루며, 갱신 계획은 각 로봇의 과거 동작과 현재 동작을 바꾸지 않은 채 새 작업을 반영하도록 정의된다. [사실][^ref-1485] 이론 모듈로 만족 가능성(Satisfiability Modulo Theories, SMT) 해법기로 앞선 풀이 정보를 유지하는 증분 풀이를 쓰지만, 증분·비증분 풀이의 시간 성능은 해법기와 배치 크기에 따라 크게 달랐다(Z3-BV 와 Bitwuzla-BV 비교). [사실][^ref-1485]
- Dai 외, Heterogeneous Multi-robot Task Allocation and Scheduling via Reinforcement Learning(2025, IEEE Robotics and Automation Letters) — 강화학습으로 이종 로봇이 다음 작업을 분산적으로 고르는 협업 일정 정책을 학습한다. 저자는 최대 150 에이전트·500 작업·5종 능력 조건까지 다뤘다고 보고하지만 이 규모 수치는 저자 보고이며 검증 단계에서 원문을 대조하지 못했고, 휴리스틱·혼합 정수 계획 기준선 대비 결과는 저자 실험이며 독립 재현은 미확인이다. [추정][^ref-1486]

Open-RMF 작업 계획기는 탐욕 방식(최적성 미보장, 더 빠를 수 있음)과 A* 기반 방식(최적성 보장, 더 오래 걸릴 수 있음)을 고르게 한다. [사실][^ref-377] 이 위키의 판단(외부 조사 메모 기반)으로는 Dai 외의 강화학습 방식과, 계획기에 비용 계산기를 지정하지 않으면 쓰는 BinaryPriorityCostCalculator 를 쓴 Open-RMF 계획기는 목적·모델·평가 환경이 달라, 규모나 풀이 시간만으로 우열을 정하기보다 실행 가능한 일정 비율과 목적값을 같은 조건에서 비교하는 편이 좋다. [의견][^ref-1486][^ref-377]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md)
- 관련 영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1485]: Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (UC Berkeley, Toyota Motor North America), SMT-Based Dynamic Multi-Robot Task Allocation, 2024-03-18, https://arxiv.org/html/2403.11737v1, 접근일 2026-10-10
[^ref-1486]: Dai, W., Rai, U., Chiun, J., Cao, Y., & Sartoretti, G. (IEEE Robotics and Automation Letters 10(3), 2654–2661, DOI 10.1109/LRA.2025.3534682), Heterogeneous Multi-robot Task Allocation and Scheduling via Reinforcement Learning, 2025-01-27, https://marmotlab.org/publications/73-RAL2025-HetMRTA.pdf, 접근일 2026-10-10 (원문 미열람)
[^ref-377]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-03 | 26. 작업 순서·스케줄링 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-10-03/pages/topics/2026/2026-10-10-area26-s11.md

```markdown
---
title: "26. 작업 순서·스케줄링 — 열린 질문"
type: topic
category: "G. 계획·최적화"
primary_area_no: 26
related_areas: [20, 23, 24, 25, 27, 28, 31, 35, 39]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-125, ref-1483, ref-1484, ref-1485, ref-379]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#11
---

[홈](../../index.md) › [주제](../index.md) › 26. 작업 순서·스케줄링 — 열린 질문

# 26. 작업 순서·스케줄링 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아래 질문은 이번 조사로 근거가 늘었지만 답을 확인하지 못한 것이다. 2026-09-25 까지의 질문은 [기존 열린 질문 정리](2026-09-25-area14-s11.md)에 있고, 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아래 질문은 이번 조사로 근거가 늘었지만 답을 확인하지 못한 것이다. 2026-09-25 까지의 질문은 [기존 열린 질문 정리](2026-09-25-area14-s11.md)에 있고, 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

### 2026-10-10 갱신

- **oq-019** (상태: 열림) 상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가? — 부분 근거: 이진 우선순위의 표현과 비용 벌점 구현은 공개되어 있지만, 납기·운송 마감을 이진 값으로 바꾸고 진행 중 작업을 재정렬하는 현장 설계는 확인하지 못해 질문을 닫을 수 없다는 것이 이 위키의 판단(외부 조사 메모 기반)이다. [의견][^ref-125][^ref-1483][^ref-1484]
- **oq-049** (상태: 열림) 제조사가 다른 로봇 플릿 사이의 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 작업 요청 수준에서 표현·집행하는 표준 필드나 공개 구현이 있는가? — 부분 근거: 공통 작업 요청 스키마에는 선행 작업 ID 가 없고 유형별 description 확장 경로만 있어, 이 경로만으로 제조사 간 선후 집행이 구현되었다고 볼 수 없으며 범용 표준 필드나 완성된 공개 구현은 확인하지 못했다(다른 작업 유형 스키마는 대조하지 않음). [추정][^ref-125]
- (새 질문 · 상태: 열림) 이진 우선순위에서 높은 작업이 계속 들어올 때 낮은 작업의 무한 대기를 막는 공개 정책이 있는가? 근거는 이진 우선순위 비용 계산기의 배분·순서 조건이다.[^ref-1483]
- (새 질문 · 상태: 열림) 제조사별 예상 완료 시간의 오차를 고려해 출하 마감 대비 여유 시간을 얼마나 두는가? 근거는 마감을 필수 조건과 비용 조건 가운데 무엇으로 둘지의 설계 문제다.[^ref-379][^ref-1485]
- (새 질문 · 상태: 열림) 작업 완료 시각 합, 납기 지연 합, 계획 변경량을 함께 최적화할 때 현장별 가중치를 어떻게 검증하는가? (관련 기존 질문: oq-054, oq-051)

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md)
- 관련 영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-10-10
[^ref-1483]: Open Robotics (open-rmf), rmf_task — rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp, 접근일 2026-10-10
[^ref-1484]: Open Robotics (open-rmf), rmf_task — rmf_task/src/rmf_task/BinaryPriorityScheme.cpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityScheme.cpp, 접근일 2026-10-10
[^ref-1485]: Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (UC Berkeley, Toyota Motor North America), SMT-Based Dynamic Multi-Robot Task Allocation, 2024-03-18, https://arxiv.org/html/2403.11737v1, 접근일 2026-10-10
[^ref-379]: Google (google/or-tools GitHub), OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver), 미확인, https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-03 | 26. 작업 순서·스케줄링 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-10-03/pages/topics/2026/2026-10-10-area26-s3.md

```markdown
---
title: "26. 작업 순서·스케줄링 — 왜 중요한가"
type: topic
category: "G. 계획·최적화"
primary_area_no: 26
related_areas: [20, 23, 24, 25, 27, 28, 31, 35, 39]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-380, ref-381, ref-382, ref-385, ref-387]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#3
---

[홈](../../index.md) › [주제](../index.md) › 26. 작업 순서·스케줄링 — 왜 중요한가

# 26. 작업 순서·스케줄링 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 주문 피킹은 대부분 창고에서 가장 노동집약적이고 비용이 큰 활동으로 알려져 있으며, 2007년 문헌 검토는 그 비용을 창고 운영비의 최대 55%로 추정했다(그 문헌 검토가 제시한 단일 출처 추정치이며 독립 교차 확인은 없다). [사실][^ref-380] 같은 검토는 배치·구역화·경로·보관 배정을 피킹의 주요 설계·통제 결정 문제로 다룬다. [사실][^ref-380]
- 이 페이지는 [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

주문 피킹은 대부분 창고에서 가장 노동집약적이고 비용이 큰 활동으로 알려져 있으며, 2007년 문헌 검토는 그 비용을 창고 운영비의 최대 55%로 추정했다(그 문헌 검토가 제시한 단일 출처 추정치이며 독립 교차 확인은 없다). [사실][^ref-380] 같은 검토는 배치·구역화·경로·보관 배정을 피킹의 주요 설계·통제 결정 문제로 다룬다. [사실][^ref-380]

이커머스 창고는 주문 줄이 몇 개뿐인 시간 임박 주문을 대량으로 처리해야 하며, 로봇·자동 피킹 작업대 같은 자동화와 함께 동적 주문 처리·배치·구역화·분류 같은 운영 적응이 쓰인다고 2019년 조사 논문이 정리한다. [사실][^ref-382]

순서 결정만으로 필요한 자원이 달라질 수 있다는 보고도 있다. 랙 이동 로봇 창고에서 작업대의 주문 배치·순서와 랙 도착 순서를 함께 정한 2017년 연구는, 저자 계산 실험(원문 미열람, 독립 재현 미확인)에서 최적화된 주문 처리가 현장에서 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다고 보고했다. [사실][^ref-381]

분류 원문의 질문에 비추어 보면, 연구들은 피킹 작업대의 순서를 정할 때 뒤 공정(통합·포장)의 주문 완료 시간과 작업자 대기를 목적에 넣는 방식으로 대기를 줄이려 하므로, ROP 의 순서 결정도 포장대 도착 순서를 기준 제약으로 삼는 형태가 될 것으로 보인다. 다만 국내 연구는 총 주문 처리 시간을 피킹 시간이 결정했다고 보고하므로 포장 쪽 동기화만으로 전체 시간이 줄어든다고 볼 수는 없고, 로봇 운반을 포함한 국내 현장 검증도 없다. [추정][^ref-385][^ref-381][^ref-387]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md)
- 관련 영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-380]: de Koster, R., Le-Duc, T., & Roodbergen, K. J., Design and control of warehouse order picking: A literature review, 2007, https://pure.eur.nl/en/publications/design-and-control-of-warehouse-order-picking-a-literature-review/, 접근일 2026-09-25 (원문 미열람)
[^ref-381]: Boysen, N., Briskorn, D., & Emde, S., Parts-to-picker based order processing in a rack-moving mobile robots environment, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758, 접근일 2026-09-25 (원문 미열람)
[^ref-382]: Boysen, N., de Koster, R., & Weidinger, F., Warehousing in the e-commerce era: A survey, 2019, https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/, 접근일 2026-09-25 (원문 미열람)
[^ref-385]: Boysen, N., Stephan, K., & Weidinger, F., Manual order consolidation with put walls: the batched order bin sequencing problem, 2019, https://www.sciencedirect.com/science/article/pii/S2192437620300315, 접근일 2026-09-25 (원문 미열람)
[^ref-387]: 신희철, 이강현, 방선호, 신광섭(한국빅데이터학회 학회지), 물류센터 생산성 향상을 위한 피킹스케줄링 문제에 관한 연구, 2024, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003163116, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-03 | 26. 작업 순서·스케줄링 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-10-10-03/pages/topics/2026/2026-10-10-area26-s10.md

```markdown
---
title: "26. 작업 순서·스케줄링 — 다른 연구영역과의 연결"
type: topic
category: "G. 계획·최적화"
primary_area_no: 26
related_areas: [20, 23, 24, 25, 27, 28, 31, 35, 39]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-006, ref-117, ref-125, ref-376, ref-377, ref-381, ref-383, ref-385, ref-386, ref-388, ref-389]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#10
---

[홈](../../index.md) › [주제](../index.md) › 26. 작업 순서·스케줄링 — 다른 연구영역과의 연결

# 26. 작업 순서·스케줄링 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 작업 순서는 배정·경로·자원 계획과 얽혀 있어 다음 영역과 함께 읽어야 한다.
- 이 페이지는 [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

작업 순서는 배정·경로·자원 계획과 얽혀 있어 다음 영역과 함께 읽어야 한다.

- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 시간·순서 제약이 있는 배정 분류와 Open-RMF 입찰 기반 배정을 다룬다. [사실][^ref-383][^ref-376]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 선후 제약 MAPF 와 온라인 픽업·배송처럼 순서와 경로가 함께 풀린다. [사실][^ref-389][^ref-006]
- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 플릿 일정에 충전 작업을 끼워 넣는 결정이 순서에 영향을 준다. [사실][^ref-377]
- [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) — 출고 우선순위·시작 시각을 상위 시스템에서 받는 쪽에 가까울 것으로 보인다(oq-019). [추정][^ref-125][^ref-386]
- [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) — B2MML 의존 유형으로 공정 선후를 표현한다(oq-013). [사실][^ref-117]
- [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md) — 순서 최적화가 필요한 로봇 대수를 바꾼다는 저자 실험이 있다. [사실][^ref-381]
- [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) — 포장 작업자 대기·주문 완료 시간을 성과 지표로 쓰는 문제와 이어진다. [사실][^ref-385]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 제조사가 다른 플릿 사이 선후를 요청 수준에서 표현할 수단이 필요하다. [추정][^ref-125]
- [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — 피킹·포장 작업자 배치와 대기가 순서 결정과 맞물린다. [사실][^ref-388]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md)
- 관련 영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-25 (원문 미열람)
[^ref-117]: MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd, 접근일 2026-09-25
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-10-10
[^ref-376]: Open Robotics, Tasks in RMF (task) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task.html, 접근일 2026-09-25
[^ref-377]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp, 접근일 2026-10-10
[^ref-381]: Boysen, N., Briskorn, D., & Emde, S., Parts-to-picker based order processing in a rack-moving mobile robots environment, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758, 접근일 2026-09-25 (원문 미열람)
[^ref-383]: Nunes, E., Manner, M., Mitiche, H., & Gini, M., A taxonomy for task allocation problems with temporal and ordering constraints, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0921889016306157, 접근일 2026-09-25 (원문 미열람)
[^ref-385]: Boysen, N., Stephan, K., & Weidinger, F., Manual order consolidation with put walls: the batched order bin sequencing problem, 2019, https://www.sciencedirect.com/science/article/pii/S2192437620300315, 접근일 2026-09-25 (원문 미열람)
[^ref-386]: Jiang, M., & Huang, G. Q., Intralogistics synchronization in robotic forward-reserve warehouses for e-commerce last-mile delivery, 2022, https://www.sciencedirect.com/science/article/abs/pii/S1366554522000175, 접근일 2026-09-25 (원문 미열람)
[^ref-388]: Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지), 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링, 2025, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570, 접근일 2026-09-25 (원문 미열람)
[^ref-389]: Kedia, K., Jenamani, R. K., Hazra, A., & Chakrabarti, P. P., Optimal Multi-Agent Path Finding for Precedence Constrained Planning Tasks, 2022-02, https://arxiv.org/abs/2202.10449, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-03 | 26. 작업 순서·스케줄링 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 21건 / 전체 1401건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/open-questions.md (요약: 대상 영역 [26] 에 걸린 12건 / 전체 350건)

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

### runs/2026-10-10-03/verification2.json

```json
{
  "run_id": "2026-10-10-03",
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
    "ok": true,
    "overlaps": []
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
    "26. 작업 순서·스케줄링 8절(분리 페이지 docs/topics/2026/2026-10-10-area26-s8.md 3절): 기존 8절에 있던 2026-09-25 주제 페이지 링크 [26. 작업 순서·스케줄링 — 대표 연구와 자료](../../topics/2026/2026-09-25-area14-s8.md) 가 사라졌다. '8. 대표 연구와 자료' replace 패치의 머리 문장 안에 이 링크를 넣어 되살린다. 예: '[2026-09-25 에 정리한 기존 항목](../../topics/2026/2026-09-25-area14-s8.md)은 성능 수치가 모두 저자 실험 결과이며 이 위키가 원문을 열지 못했다.' 이유: 기존 연구 목록(ref-133·ref-134·ref-384 등)이 세부영역 페이지 8절에서 더는 연결되지 않는다. 형식 검증의 자동 분리가 '자세한 내용은 주제 페이지 …' 줄을 지운 것으로 보이므로(분리 페이지 3절에 빈 줄이 두 개 있다), 링크를 따로 떨어진 줄이 아니라 문장 안에 넣는다. 상대 경로 ../../topics/2026/… 는 세부영역 페이지와 분리 페이지 양쪽에서 같은 파일을 가리킨다.",
    "26. 작업 순서·스케줄링 11절(분리 페이지 docs/topics/2026/2026-10-10-area26-s11.md 3절): 기존 11절의 링크 [26. 작업 순서·스케줄링 — 열린 질문](../../topics/2026/2026-09-25-area14-s11.md) 이 사라졌다. '11. 열린 질문' 패치의 머리 문장 안에 이 링크를 넣어 되살린다. 예: '2026-09-25 까지의 질문은 [기존 열린 질문 정리](../../topics/2026/2026-09-25-area14-s11.md)에 있다.' 이유: 8절과 같다. 기존 질문(oq-013·oq-050·oq-051 등) 정리 페이지가 11절에서 더는 연결되지 않는다.",
    "f7 조건 누락: 아래 네 곳에 '우선순위 검사가 켜져 있을 때' 조건을 넣는다. (1) 세부영역 6절 append 패치의 '…우선순위 배분을 어긴 배정의 비용에 벌점 계수를 곱한다', (2) 주제 페이지 2026-10-10-binary-priority-cost-deadline-and-replanning.md 1절 첫 항목, (3) 같은 페이지 4절 표의 수행 자원 칸 '…배정 비용에 벌점이 붙는다', (4) 7절(분리 페이지 2026-10-10-area26-s7.md) BinaryPriorityScheme 행의 '…배정 비용에 벌점 계수를 곱한다'. 예: '우선순위 검사가 켜져 있으면 … 벌점 계수를 곱한다'. 이유: f7 은 compute_cost 의 check_priority 가 켜져 있을 때만 벌점을 곱한다고 확인했다. 주제 페이지 3절은 이 조건을 적었지만 요약·표에서는 조건 없이 일반화했다(검증 항목 2의 '조건부 진술의 일반화')."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 27건, 미확인 2건, 교차 확인 0건(rmf_task 헤더·구현·스키마는 같은 프로젝트 자료라 독립 교차 확인으로 세지 않았다). 강등: f20 사실 → 일부 추정(연합 능력 조건·탐색·구조 모사 틀을 원문으로 대조하지 못함), f23 사실 → 추정(150 에이전트·500 작업·5종 능력 규모 수치 미확인). 원문 미열람 출처: ref-1486(Dai 외). 검증 단계에서 PDF 텍스트를 뽑지 못했다. 실재와 서지(IEEE RA-L 10(3), 2025-01-27, DOI 10.1109/LRA.2025.3534682, 저자 5명)는 OpenAlex 로 확인했고, 핵심 설정(필요한 로봇이 모두 모여야 시작, 메이크스팬 최소화, 휴리스틱·MIP 대비 두 자릿수 이상 빠름)은 초록 요약으로만 확인했다. ref-125·ref-377·ref-379 는 입력 원문 텍스트로, ref-1483·ref-1484·ref-1398 은 GitHub raw 로, ref-1485 는 arXiv HTML 로 원문을 대조했다. 주의: Open-RMF 비용 설명은 비용 계산기를 지정하지 않았을 때 쓰는 BinaryPriorityCostCalculator 에 한정된다. 같은 헤더의 TaskAssignmentStrategy 와의 관계는 미확인이다. 이진 우선순위는 비용 벌점이며 마감 보장이 아니다. Tuck 외와 Dai 외는 계산 실험이고, 5절 '기타' 사례는 현장 실증이 아니다. 같은 URL 의 출처가 이전 실행(ref-1454, ref-1424·ref-1458)과 겹쳐 id 통일이 필요하다. 트랙 반영 제안 4건은 다음 실행으로 넘긴다. 정정 요청은 없다. 열린 질문 oq-019·oq-049 는 부분 근거만 추가하고 해결로 인정하지 않는다. / 2차 수정 후 재검증. 드리프트 없음. 1차 수정 지시 16건은 모두 이행을 확인했다(f20 사실·추정 분리, '기타' 계산 실험 표기, f23 강등, f12 괄호 정의 제거, 비용 주어 한정, [의견] 주체 표시, 7절 행 갱신, ref-1486 서지, 질문 중복 표시, 트랙 제안 미반영, 직접 인용 0회). [분류원문] 보존, 섹션 순서 준수. 지적 3건: (1) 8절·(2) 11절에서 기존 2026-09-25 분리 주제 페이지(2026-09-25-area14-s8, 2026-09-25-area14-s11)로 가는 링크가 사라졌다. 형식 검증의 자동 분리가 '자세한 내용은 주제 페이지 …' 줄을 지운 것으로 보이며, pipeline 담당이 분리 처리에서 기존 링크 줄을 보존하는지 확인해야 한다. (3) f7 의 '우선순위 검사가 켜져 있을 때' 조건이 요약·표 네 곳에서 빠졌다. 참고(수정 지시 아님): 6절의 '마감을 검사하지 않는다'는 1차에서 코드로 확인한 사실 범위 안에 있다. 페이지의 '혼합 정수 계획(Mixed Integer Programming, MIP)'은 용어집 milp(Mixed Integer Linear Programming)와 영문이 다르지만, 출처가 MIP 를 쓰므로 그대로 둔다. 2차는 도구를 쓰지 않았다.",
  "retry_reason": null
}
```
