(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-10-05
- date: 2026-10-10
- run_type: update (갱신)
- 대상: 28. 공용 자원·충전·에너지 최적화 (G. 계획·최적화)
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

## 입력

### runs/2026-10-10-05/target.json

```json
{
  "run_id": "2026-10-10-05",
  "date": "2026-10-10",
  "weekday": "Sat",
  "run_number": 165,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 28,
    "area_name": "28. 공용 자원·충전·에너지 최적화",
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
  "selection_rationale": "CLI 지정 run_type=update, area=28"
}
```

### runs/2026-10-10-05/research.json

```json
{
  "run_id": "2026-10-10-05",
  "date": "2026-10-10",
  "run_type": "update",
  "target": {
    "area_no": 28,
    "area_name": "28. 공용 자원·충전·에너지 최적화",
    "category": "G. 계획·최적화"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 — 호텔 연구 수치(ref-103)가 원문 미열람·저자 미확인 상태로 '거의 두 배'로 요약돼 있음",
    "섹션 5. 적용 사례 (현장 유형 명시) — 제약 행의 '임계 저충전 수준 이하에서는 충전소로 가는 주문만 보내야 한다'가 원문 권고(should)보다 강함. 물류창고 외 현장 유형 사례 없음",
    "섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 분리 페이지 53행의 is_parking_spot/is_charger 출처 충돌 미해소(oq-069), VDA 선언값과 Open-RMF 설정의 단위·의미 구분 없음(oq-068)",
    "섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — 승강기 메시지의 필드 범위와 배분 정책 부재 구분 없음(oq-067), Open-RMF 충전·뮤텍스 관련 2026년 수정 이력과 적용 버전 미기재",
    "섹션 8. 대표 연구와 자료(주제 페이지로 분리) — 배터리 열화·공용 충전기 비중첩 제약을 함께 푸는 최신 연구, 에너지 공급과 결합한 충전 연구 없음(oq-066)",
    "섹션 11. 열린 질문 — oq-066·oq-067·oq-068 부분 근거, oq-069 해소 근거 미반영",
    "정정 요청 없음(target.json corrections 비어 있음). 외부 조사 메모의 '수정' 항목 두 건(5절 제약 행, 6절 분리 페이지 충돌 문장)을 정정 근거로 다룸"
  ],
  "research_questions": [
    "로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]",
    "oq-069 출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot(지원 작업 문서)과 is_charger(교통 편집기 문서·데모 README) 가운데 어느 속성으로 하는가? (섹션 6·11 겨냥)",
    "oq-068 충전 하한을 제조사가 팩트시트로 선언한 값(criticalLowChargingLevel)과 ROP 운영 설정(recharge_threshold) 가운데 어느 것으로 삼고, 둘이 다르면 어떻게 조정하는가? (섹션 5·6·11 겨냥)",
    "oq-067 여러 제조사 플릿이 한 승강기를 함께 쓸 때 세션 순서·최대 점유 시간·목적층 묶음을 정하는 배분 규칙을 공개한 표준이나 구현이 있는가? (섹션 7·11 겨냥)",
    "oq-066 물류센터 로봇의 충전 시점을 시간대별 전기 요금이나 최대 수요 전력 기준으로 계획한 연구나 국내 사례가 있는가? (섹션 8·11 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 3.0.0 팩트시트의 batteryCharging.criticalLowChargingLevel 은 임계 충전 수준을 백분율(percent)로 선언하는 float64 필드다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3.0.0 명세 factsheet 표 2148행: \"criticalLowChargingLevel | float64 | Specifies the critical charging level in percent at or below which the fleet control should only send orders that command the mobile robot to a charging station.\" (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "같은 필드 설명은 그 충전 수준 이하에서 관제가 충전소로 가도록 지시하는 주문만 보내는 것이 좋다고 권고 표현(should)으로 기술한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3.0.0 명세 2148행 같은 행의 \"should only send orders\" 구절. 위키 5절 제약 행의 '보내야 한다'(근거 ref-228)는 원문의 권고 강도보다 강하다. 정정 대상 문장: \"팩트시트의 임계 저충전 수준 이하에서는 관제가 충전소로 가는 주문만 보내야 한다.\" (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f3",
      "claim": "따라서 criticalLowChargingLevel 을 shall 수준의 의무 문구로 옮기거나 모든 로봇에 공통으로 정해진 충전 시작 비율로 설명해서는 안 되며, 제조사가 로봇별로 선언하는 값으로 다뤄야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "근거: 2148행이 should 를 쓰고 값은 팩트시트(로봇별 선언)에 들어간다. 5절 제약 행의 '보내야 한다'를 '보내는 것이 좋다(권고)'로 고치는 정정 근거.",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "VDA 5050 3.0.0 팩트시트의 batteryCharging 객체는 criticalLowChargingLevel·maximumDesiredChargingLevel·minimumDesiredChargingLevel(모두 백분율)과 minimumChargingTime(초) 네 필드로 이루어진다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3.0.0 명세 2147~2151행: maximumDesiredChargingLevel \"maximum desired charging level in percent\", minimumDesiredChargingLevel \"minimum desired charging level in percent\", minimumChargingTime uint32 \"desired minimum charging time in seconds\". (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "Open-RMF fleet_adapter_template 의 config.yaml 은 recharge_threshold: 0.10 을 그 아래로는 로봇이 운행하지 않는 배터리 수준으로, recharge_soc: 1.0 을 충전 작업에서 채울 목표 배터리 수준으로 두며, 두 값은 0~1 비율로 적힌 템플릿 예시값이다.",
      "tag": "사실",
      "source_ids": [
        "ref-105"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "config.yaml 25~26행: \"recharge_threshold: 0.10 # Battery level below which robots in this fleet will not operate\", \"recharge_soc: 1.0 # Battery level to which robots in this fleet should be charged up to during recharging tasks\". 0.10 은 10% 에 해당하나 현장 권장값이 아니다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "VDA 5050 의 백분율 선언값과 Open-RMF 의 비율 설정을 대조할 때는 단위를 먼저 맞추고, 운행 하한·충전 시작 판단·충전 목표를 별도 정책 항목으로 기록하는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-031",
        "ref-105"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "근거: VDA 는 percent(2148~2150행), Open-RMF 템플릿은 0.10·1.0 비율(25~26행). VDA 의 임계 수준은 관제의 주문 제한 기준, Open-RMF 의 recharge_threshold 는 운행 하한으로 서로 의미가 다르다.",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "제조사가 팩트시트로 선언한 임계 충전 수준과 ROP 운영 설정(recharge_threshold) 가운데 어느 값을 자동으로 우선하는지에 관한 공통 조정 규칙은 확인한 두 원문에 없었다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-105"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDA 5050 3.0.0 명세 batteryCharging 행과 Open-RMF config.yaml 주석에 두 값의 동기화·우선순위 규정이 없음(확인한 범위 안의 부재). 다른 Open-RMF 구성요소에 그런 규칙이 있는지는 조사하지 않았다.",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "Open-RMF rmf_traffic 의 그래프 API(Graph.hpp)는 경유점에 주차 지점(is_parking_spot/set_parking_spot)과 충전 지점(is_charger/set_charger)을 서로 다른 속성으로 정의하며, 충전 지점은 배터리 충전 수준이 임계값 아래로 떨어진 로봇이 보내지는 곳으로 설명된다.",
      "tag": "사실",
      "source_ids": [
        "ref-536"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Graph.hpp 146~160행: \"Returns true if this Waypoint is a charger spot. Robots are routed to these spots when their batteries charge levels drop below the threshold value.\" 주차 지점은 비상 경보 때 로봇이 스스로 주차하는 곳. 참고: set_charger 위 주석이 \"Set this Waypoint to be a parking spot.\"으로 잘못 복사돼 있으나 함수 이름·인자(_is_charger)로 별도 속성임이 확인된다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "rmf_fleet_adapter 2.14.0 의 그래프 파서(parse_graph.cpp)는 경유점 옵션 is_parking_spot 을 set_parking_spot(true)로, is_charger 를 set_charger(true)로 각각 따로 변환한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1543"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2.14.0 태그 parse_graph.cpp 170~176행: options[\"is_parking_spot\"] → wp.set_parking_spot(true); 194~200행: options[\"is_charger\"] → wp.set_charger(true). 두 분기는 독립적이다.",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "따라서 이 구현에서 충전소 경유점 지정은 is_charger 로 확인되며, is_parking_spot 만 지정한 경유점을 충전소 지정과 같은 뜻으로 취급하면 안 된다. 지원 작업 문서의 is_parking_spot 서술과 생긴 출처 충돌(6절 분리 페이지)은 구현 기준으로 해소된다.",
      "tag": "의견",
      "source_ids": [
        "ref-536",
        "ref-1543"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "정정 대상: 6절 분리 페이지(2026-09-25-area16-s6.md 53행) \"한편 Open-RMF 지원 작업 문서는 충전소를 is_parking_spot 으로 설정한다고 적어 is_charger 로 적는 문서와 어긋난다.\" Graph.hpp 와 parse_graph.cpp 는 같은 프로젝트 자료라 독립 교차 확인으로 세지 않는다.",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "Open-RMF LiftRequest 메시지는 lift_name·request_time·session_id·request_type(세션 종료·AGV 모드·사람 모드)·destination_floor·door_state 필드로 이루어지고, LiftState 메시지는 세션 종료 요청을 보낼 때까지 승강기 제어권을 받은 session_id 를 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-312",
        "ref-286"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "LiftRequest.msg: REQUEST_END_SESSION=0, REQUEST_AGV_MODE=1, REQUEST_HUMAN_MODE=2; \"session_id should be unique at least between different requesters\". LiftState.msg: \"this field records the session_id that has been granted control of the lift until it sends a request with a request_type of REQUEST_END_SESSION\". (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "LiftRequest·LiftState 두 메시지에는 최대 점유 시간, 예약 시간창, 여러 요청의 목적층 묶음을 직접 지정하는 필드가 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-312",
        "ref-286"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "두 메시지 전체 필드 대조: LiftRequest(lift_name, request_time, session_id, request_type, destination_floor, door_state), LiftState(lift_time, lift_name, available_floors, current_floor, destination_floor, door_state, motion_state, available_modes, current_mode, session_id). 시간 한도·시간창·다중 목적층 필드 없음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f13",
      "claim": "따라서 승강기 세션 점유·종료 인터페이스가 공개되어 있다는 사실과 공정한 대기열·묶음 운행 같은 배분 정책이 정의되어 있다는 주장은 구별해야 하며, 메시지 정의만 본 결론이므로 다른 감독 구성요소에 타임아웃이나 대기열 구현이 없다는 뜻으로 넓히지 않는다.",
      "tag": "의견",
      "source_ids": [
        "ref-312",
        "ref-286"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "근거: f11·f12 의 메시지 정의. 승강기 감독(lift supervisor) 등 다른 구성요소의 소스는 이번에 조사하지 않았다.",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "Han 외(2025, Sensors)는 다층 호텔 배송 로봇의 경로 계획에서 승강기 노드를 암묵적 경유점으로 두고 문제를 다회 운행 차량 경로 문제(Multi-Trip Vehicle Routing Problem, MTVRP)로 정식화해 적응형 대규모 이웃 탐색으로 푼다.",
      "tag": "사실",
      "source_ids": [
        "ref-103"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록·§2: \"... nodes are modeled as implicit waypoints, and the routing problem is formulated as a Multi-Trip Vehicle Routing Problem (MTVRP). To solve this NP-hard problem, an Adaptive Large ...\" Sensors 25(6) 1783, doi:10.3390/s25061783, 2025-03-13.",
      "as_of": "2026-10-10",
      "site_type": "상업 시설",
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "이 논문은 고객 노드 60개 사례에서 승강기 운행 시간을 40초에서 100초로 늘리면 총 이동 시간이 약 225초에서 500초로 늘었다고 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-103"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.4 Discussion(p.16): \"in the scenario with 60 customer nodes, increasing elevator operation time from 40 s to 100 s nearly doubles the total travel time (from 225 s to 500 s).\" 호텔 사례의 수치 실험이며 물류센터 적용은 미확인.",
      "as_of": "2026-10-10",
      "site_type": "상업 시설",
      "flow_item": "제약"
    },
    {
      "id": "f16",
      "claim": "이 수치는 승강기 운행 시간에 대한 모델 민감도이며 실제 물류센터에서 측정한 승강기 대기열 손실값이 아니다.",
      "tag": "의견",
      "source_ids": [
        "ref-103"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "근거: §4 는 가정한 승강기 운행 시간(40·50·60·70·80·100 s)을 바꾸는 수치 실험이다. 기존 3절의 '거의 두 배' 표현 대신 원 수치(225→500 s)를 쓰는 정정 근거.",
      "as_of": "2026-10-10",
      "site_type": "상업 시설",
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "논문은 무작위·동적 승강기 운행 시간, 동적 수요 변동, 다중 로봇 협업·충돌 회피, 지능형 승강기 스케줄링 알고리즘을 후속 연구 과제로 남긴다.",
      "tag": "사실",
      "source_ids": [
        "ref-103"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§5: \"Future research will explore ... random or dynamic elevator operation times, dynamic demand fluctuations ... multi-robot collaboration mechanisms, collision avoidance mechanisms (e.g., velocity obstacles), intelligent elevator scheduling algorithms\". 여러 제조사 승강기 배분의 완성 사례로 쓰지 않는다.",
      "as_of": "2026-10-10",
      "site_type": "상업 시설",
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "Li 외(2026, arXiv 2603.22731 프리프린트)는 작업 배정·서비스 순서·선택적 충전 결정·충전 방식 선택·공용 충전기 접근을 하나의 혼합 정수 선형 계획(Mixed-Integer Linear Programming, MILP)으로 함께 표현한다.",
      "tag": "사실",
      "source_ids": [
        "ref-403"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"jointly optimizing task assignment, service sequencing, optional charging decisions, charging-mode selection, and charger access while balancing degradation across the fleet.\" v1, 2026-03-24.",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "이 모델의 목적함수는 총 배터리 열화, 충전기 대기, 납기 지연, 로봇 사이 열화 불균형을 함께 최소화한다.",
      "tag": "사실",
      "source_ids": [
        "ref-403"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§2.2 Objective function: \"The objective minimizes total degradation, charger waiting, tardiness, and degradation imbalance\"; 가중치 λ·µ·ρ 는 충전기 대기·납기 지연·불균형용.",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "같은 논문 §2.6 의 식 (33)–(34)는 같은 충전기에서 일어날 수 있는 서로 다른 충전 세션 쌍(같은 로봇의 세션 쌍 포함)마다 순서 변수를 두어 충전 구간이 겹치지 않게 하는 비중첩 순서 제약이다.",
      "tag": "사실",
      "source_ids": [
        "ref-403"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§2.6 Shared-charger capacity constraints: 충전기 m 의 세션 집합 Ωm 은 모든 로봇 r 의 세션을 포함하고, \"For each unordered pair of distinct sessions σ, σ′ ∈ Ωm, let uσ,σ′,m ∈ {0,1} enforce temporal ordering. Non-overlap is imposed by (33)–(34)\".",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "실험은 100×50 m 가상 창고, 동종 로봇, 표준·고속 두 충전 방식을 가정하며, §4.4 표 2 는 대표 사례(로봇 4·작업 40·충전기 2)의 '예시적 기대 평균(illustrative expected averages)'으로 총 열화가 규칙 기반 0.214 에서 0.098 로 준다고 보고하고, 기여 요약은 규칙 기반 대비 최대 54% 열화 감소를 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-403"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.1: \"100 × 50 m rectangular warehouse ... Robots are homogeneous with a two-mode charging set Lr = {standard, fast}\". §4.4: \"Table 2 reports illustrative expected averages for a representative instance with |R| = 4, |K| = 40, and |M| = 2\". §1 기여 (3): \"reduces total degradation by up to 54% over rule-based dispatch\".",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "§4.4 가 비교표를 예시적 기대 평균으로 설명하고 열화를 축약 대리 모형으로 표현하므로, 최대 54% 열화 감소를 현장 배터리 수명 개선의 검증값으로 인용하지 않는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-403"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "근거: 초록 \"reduced-form degradation proxies grounded in the empirical battery-aging literature\", §4.4 \"illustrative expected averages\". 실물 배터리 노화 실험·공개 재현 데이터는 확인 못 함.",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "Yang 외(2026, Processes)는 냉동 컨테이너 온도 제약 아래 항만 무인운반차(Automated Guided Vehicle, AGV)의 작업 스케줄링과 충전을, 태양광·풍력·에너지 저장 장치(Energy Storage System, ESS)를 갖춘 항만 마이크로그리드 운영과 결합해 운영비를 최소화하는 2단계 물류–에너지 협조 최적화 프레임워크를 제시한 것으로 소개된다.",
      "tag": "추정",
      "source_ids": [
        "ref-1544"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "원문 미열람. Crossref 초록 기준: 냉동 컨테이너 온도 제약, 항만 마이크로그리드(태양광·풍력·ESS), 운영비 최소화를 다루는 2단계 프레임워크. 초록에 '시간대별 전기 요금'·'충전소 용량' 표현은 직접 나오지 않는다. 출판사 본문 열기 실패.",
      "as_of": "2026-10-10",
      "site_type": "실외",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f24",
      "claim": "이 항만 연구는 물류 작업과 에너지 공급을 함께 계획하는 충전 연구의 후보 자료일 뿐이며, 원문을 열지 못했으므로 비용 절감 수치나 국내 물류센터 적용 근거로 채택하지 않는다.",
      "tag": "의견",
      "source_ids": [
        "ref-1544"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "원문 미열람. 항만(냉동 컨테이너·마이크로그리드)과 실내 물류센터의 적용 조건이 다르다. oq-066(시간대별 요금·최대 수요 전력 기준 충전 계획)에는 후보 자료 수준의 부분 근거만 된다.",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "rmf_fleet_adapter 변경 이력의 2.12.0(2026-02-23) 판에는 충전 대기(WaitForCharge) 단계 완료 발행(#502)과 다음 작업에 충전량이 모자라면 충전기로 복귀하는 변경(#423)이 기록되어 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1545"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2.14.0 태그 CHANGELOG.rst 57~77행, 2.12.0 (2026-02-23): \"Publish WaitForCharge phase completed (#502)\", \"Retreat to charger if there will not be enough charge for the next task (#423)\".",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "같은 변경 이력의 2.13.0(2026-06-15) 판에는 뮤텍스(Mutex) 잠금·해제 실행에서 생길 수 있는 교착을 고친 수정(#490)이 기록되어 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1545"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "CHANGELOG.rst 28~46행, 2.13.0 (2026-06-15): \"Fix potential deadlocks from execution of mutex lock and release (#490)\". 최신 판 2.14.0 은 2026-09-26.",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "따라서 Open-RMF 의 충전 작업 삽입·뮤텍스 그룹 기능을 인용할 때는 기능의 존재뿐 아니라 적용 버전과 이 수정들의 포함 여부를 함께 기록해야 하며, 이전 판이 모든 조건에서 교착 없이 동작했다는 근거로 쓰지 않는다.",
      "tag": "의견",
      "source_ids": [
        "ref-1545"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "근거: f25·f26 의 2026년 수정 이력. 위키 6절 분리 페이지의 충전 작업 삽입·뮤텍스 그룹 서술은 판을 적지 않았다.",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "VDA 5050 3.0.0 명세 원문. 이번에는 3.0.0 태그판의 팩트시트 batteryCharging 표(임계·최대·최소 희망 충전 수준 백분율, 최소 충전 시간)를 대조했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/3.0.0/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-105",
      "org": "Open Robotics (open-rmf)",
      "title": "fleet_adapter_template — fleet_adapter_template/config.yaml",
      "published": null,
      "url": "https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 플릿 어댑터 설정 템플릿. recharge_threshold(운행 하한 비율 0.10)와 recharge_soc(충전 목표 비율 1.0) 등 배터리·충전 설정 예시값을 담는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/fleet_adapter_template/main/fleet_adapter_template/config.yaml",
      "source_unopened": false
    },
    {
      "id": "ref-536",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 교통 그래프 API 헤더. 경유점의 주차 지점·충전 지점·대기 지점 속성과 뮤텍스 그룹 등을 정의한다(set_charger 위 주석은 주차 지점 문구가 잘못 복사돼 있음).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_traffic/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp",
      "source_unopened": false
    },
    {
      "id": "ref-1543",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp (2.14.0)",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 2.14.0 태그의 탐색 그래프 YAML 파서. 경유점 옵션 is_parking_spot·is_holding_point·is_passthrough_point·is_charger 를 각각 별도 속성으로 변환한다(발행일은 2.14.0 패키지판 날짜).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp",
      "source_unopened": false
    },
    {
      "id": "ref-312",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 승강기 요청 메시지. 승강기 이름·요청 시각·세션 id·요청 유형(세션 종료·AGV 모드·사람 모드)·목적층·문 상태 필드를 정의한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_internal_msgs/main/rmf_lift_msgs/msg/LiftRequest.msg",
      "source_unopened": false
    },
    {
      "id": "ref-286",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 승강기 상태 메시지. 층·문·운행·모드 상태와 세션 종료 요청 때까지 제어권을 가진 session_id 를 보고한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_internal_msgs/main/rmf_lift_msgs/msg/LiftState.msg",
      "source_unopened": false
    },
    {
      "id": "ref-103",
      "org": "Linghui Han, Junzhe Ding, Songtao Liu, Meng Meng (Sensors)",
      "title": "The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments",
      "published": "2025-03-13",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "Sensors 25(6) 1783, doi:10.3390/s25061783. 다층 호텔 배송 로봇 경로 계획을 승강기 노드를 암묵적 경유점으로 둔 MTVRP 로 정식화하고 승강기 운행 시간 민감도를 수치 실험한다. 이번 실행이 출판 PDF 첫 원문 열람이다(PMC·출판사 HTML 접근 실패).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pdfs.semanticscholar.org/428c/ef353aae52dbdc80767ccbe405597b13c4a4.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-403",
      "org": "Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin)",
      "title": "Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots",
      "published": "2026-03-24",
      "url": "https://arxiv.org/abs/2603.22731",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "arXiv 프리프린트 v1. 작업 배정·순서·충전 방식·공용 충전기 비중첩 제약을 MILP 로 함께 풀어 열화·충전기 대기·납기 지연·열화 불균형을 줄이는 계층형 해법을 제시한다(가상 창고 수치 실험).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2603.22731v1",
      "source_unopened": false
    },
    {
      "id": "ref-1544",
      "org": "Song Yang, Sichen Yue, Xiao Wang, Kaiyu Wang, Xin Tian, Xiao Wang (Processes, MDPI)",
      "title": "A Two-Stage Logistics–Energy Coordinated Optimization Framework for AGV Scheduling and Charging Under Reefer Container Temperature Constraints",
      "published": "2026-07-27",
      "url": "https://www.mdpi.com/2227-9717/14/15/2424",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "원문 미열람. Crossref 초록 기준으로 냉동 컨테이너 온도 제약 아래 항만 AGV 작업·충전을 태양광·풍력·ESS 를 갖춘 항만 마이크로그리드와 결합해 운영비를 최소화하는 2단계 프레임워크다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1545",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0)",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 패키지 변경 이력(2.14.0 태그). 2.12.0(2026-02-23)의 충전 대기 단계 완료 발행·충전기 복귀 변경과 2.13.0(2026-06-15)의 뮤텍스 잠금·해제 교착 수정을 기록한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
      "sections": [
        "3",
        "5",
        "6",
        "7",
        "8",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 3 — 호텔 연구 수치를 원문(§4.4 p.16) 기준 225→500 s 로 적고 저자·발행일 보강(f15), 모델 민감도임을 명시(f16) / 섹션 5 — 정정: 제약 행 '보내야 한다'를 권고(should)로 고치고 단위를 충전 수준(백분율)로 명시(f1·f2·f3); 상업 시설(호텔) 사례 추가(f14·f15·f16·f17) / 섹션 6(주제 페이지 요약) — 정정: 분리 페이지 53행 is_parking_spot/is_charger 충돌 문장을 구현 기준 해소로 교체(f8·f9·f10); VDA 백분율 선언과 Open-RMF 비율 설정의 단위·의미 구분(f4·f5·f6·f7) / 섹션 7(주제 페이지 요약) — 승강기 메시지 전체 필드와 배분 정책 필드 부재(f11·f12·f13; 세션 종료 전 제어권 유지는 기존 내용 확인), rmf_fleet_adapter 2026년 수정 이력과 버전 기록(f25·f26·f27) / 섹션 8(주제 페이지 요약) — Li 외 열화·공용 충전기 MILP(f18~f22), Yang 외 항만 물류–에너지 협조 연구는 원문 미열람 후보(f23·f24) / 섹션 11 — oq-069 해소 제안(f8·f9·f10), oq-068 부분 근거(f4~f7), oq-067 부분 근거(f11~f13), oq-066 후보 자료(f23·f24), 새 질문 4건."
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "공용 충전기 예약 시간이 끝났는데 로봇이 충전기 앞을 떠나지 못할 때 다음 예약의 시작을 어떻게 조정하는가? | 관련 영역: 28. 공용 자원·충전·에너지 최적화, 27. 다중 로봇 경로·교통 관리 — MAPF | 근거: f20 | 종류: 일반",
    "충전 상태(SOC) 추정 오차와 충전소까지의 이동·대기 에너지를 반영해 운영 하한에 더할 여유를 어떻게 검증하는가? | 관련 영역: 28. 공용 자원·충전·에너지 최적화, 5. 로봇 능력·작업 표현 | 근거: f5·f6 | 종류: 일반",
    "배터리 열화 최적화 모델의 예시 결과를 실제 셀·충전기·장기 운용 데이터로 검증한 공개 재현 자료가 있는가? | 관련 영역: 28. 공용 자원·충전·에너지 최적화, 57. 자산·소프트웨어 수명주기 관리 | 근거: f21·f22 | 종류: 일반",
    "승강기 운행 시간 민감도와 실제 승강기 대기열·최대 점유 시간의 관계를 같은 실험에서 측정한 자료가 있는가? | 관련 영역: 28. 공용 자원·충전·에너지 최적화, 22. 설비·건물 시스템 연동 | 근거: f15·f16 | 종류: 일반"
  ],
  "open_questions_resolved": [
    "oq-069"
  ],
  "self_check": {
    "source_count": 10,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-05/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.",
      "f23·f24: Yang 외(ref-1544) 원문 미열람. Crossref 초록만 확인했고 비용 절감 수치·요금제·충전소 용량 모델은 미확인",
      "f7: 임계 충전 수준과 recharge_threshold 의 우선순위 규칙 부재는 두 원문 범위 안의 확인이며, Open-RMF 다른 구성요소·VDA 5050 다른 절 전체를 뒤지지는 않음",
      "f13: 승강기 감독(lift supervisor) 등 메시지 밖 구성요소의 타임아웃·대기열 구현은 조사하지 않음",
      "f22: Li 외 결과를 실물 배터리 노화 실험·공개 재현 데이터로 확인하지 못함",
      "VDA 5050 3.0.0 발표일은 근거 미확인이라 적지 않음(published null)",
      "oq-066: 물류센터 로봇의 시간대별 전기 요금·최대 수요 전력 기준 충전 계획 연구와 국내 사례는 찾지 못함(항만 후보 자료만)",
      "섹션 5 의 물류창고 외 현장 유형 사례는 호텔(상업 시설)·항만(실외, 미열람) 외에는 찾지 못함"
    ],
    "scope_violations": [
      "f8·f9: 경유점 속성 정의는 15. 지도·공간·위치 모델과 겹치므로 이 영역에서는 충전소 지정 판별 근거로만 씀",
      "f11~f13: 승강기 메시지 인터페이스는 22. 설비·건물 시스템 연동 소관이며 이 영역에는 공용 자원 배분 정책의 유무 근거로만 씀",
      "f23·f24: 항만 마이크로그리드 운영은 ROP 직접 범위 밖(시설·에너지 설비 쪽 연계 대상)이며 충전 계획 연구 후보로만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 3
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(queries 0 은 집계 없음을 뜻함). 신규 출처 3건(ref-1543~ref-1545, 예약 구간 ref-1543~ref-1572 안), 재사용 7건(ref-031·ref-105·ref-536·ref-312·ref-286 github_raw, ref-103·ref-403 webfetch). ref-103 은 기존 위키 출처(원문 미열람·저자 미확인)와 같은 논문으로, 이번이 첫 원문 열람이며 저자·발행일·doi 를 보강했다(메모의 '재열람' 표현은 틀림). ref-403 은 영역 24 등에서 쓰인 기존 id 를 재사용했다. 검증 수정 반영: criticalLowChargingLevel 을 '충전 수준(백분율)'로 표기(f1), 호텔 논문 셋째 문장을 의견으로 강등(f16), Li 외 식 (33)–(34)를 같은 충전기의 세션 쌍 비중첩 제약으로 정정하고 목적에 충전기 대기·불균형 포함(f19·f20), 변경 이력 원문 문구 정정(f25·f26), Yang 외 서술을 Crossref 초록 내용으로 교체(f23), Graph.hpp 주석 복사 오류 기록(f8), LiftRequest 에 lift_name 포함(f11), VDA 5050 발표일 null. VDA 5050 3.0.0 release notes 출처는 넣지 않았다. 교차 확인 0건: Graph.hpp 와 parse_graph.cpp, 두 승강기 메시지는 같은 프로젝트 자료라 독립 출처가 아니다. 현장 유형: 상업 시설(호텔, f14~f17), 실외(항만, f23, 미열람). 열린 질문: oq-069 해소 제안(f8~f10), oq-066·oq-067·oq-068 은 부분 근거만. 정정 요청 없음, 우선 지정 질문 없음."
  }
}
```

### runs/2026-10-10-05/verification.json

```json
{
  "run_id": "2026-10-10-05",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: VDA5050 3.0.0 태그 원문(raw) factsheet 표에서 criticalLowChargingLevel float64, 'critical charging level in percent' 문구 확인. main 판 factsheet.schema(ref-228)도 percent·0~100 범위로 같으나 같은 발행 주체라 독립 교차 확인 아님. 발행일 미확인(원문에 날짜 없음)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 3.0.0 명세 표와 factsheet.schema(ref-228) 설명 모두 'fleet control should only send orders' 로 권고 표현이며 batteryCharging 안에 shall·must 없음. 기존 5절 제약 행이 ref-228 을 근거로 '보내야 한다'고 쓴 것은 ref-228 자체와도 어긋나므로 정정 근거로 인정. 같은 발행 주체 자료라 교차 확인으로 세지 않음."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: should 표현과 팩트시트(로봇 유형 단위 선언)에 값이 실린다는 점에서 도출. 페이지에서는 '이 위키는 본다'처럼 의견 주체를 밝힌다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 3.0.0 명세 표에 네 필드(최대·최소 희망 충전 수준 percent, minimumChargingTime uint32 seconds)가 있고 schema 도 같은 네 필드."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: config.yaml 원문(data/source_texts/ref-105) recharge_threshold: 0.10('will not operate'), recharge_soc: 1.0('charged up to during recharging tasks'). 템플릿 예시값이라는 한정 적절."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: VDA 는 percent 의 주문 제한 기준, Open-RMF 는 0~1 비율의 운행 하한으로 의미·단위가 다름이 두 원문에서 확인됨. 의견 주체 명시 필요."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 두 원문 범위 안의 부재 확인이며 다른 Open-RMF 구성요소·VDA 다른 절은 조사하지 않았다는 한정을 본문에 함께 적어야 함."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Graph.hpp 원문(data/source_texts/ref-536)에서 is_parking_spot(비상 경보 때 주차)과 is_charger('Robots are routed to these spots when their batteries charge levels drop below the threshold value')가 별도 속성, set_charger 위 주석이 'parking spot' 문구로 잘못 복사된 것도 확인. 발행일 미확인."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: rmf_ros2 2.14.0 태그 parse_graph.cpp 원문에서 is_parking_spot→set_parking_spot(true), is_charger→set_charger(true)가 독립 if 블록. 행 번호는 대조하지 않음. Graph.hpp 와 같은 프로젝트라 독립 교차 확인 아님."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지(구현 기준 판단). 검증 중 ros2multirobotbook task_types.md(ref-039) ChargingTask 절이 실제로 'is_parking_spot 을 true 로' 충전소를 지정한다고 적고 is_charger 는 나오지 않음을 확인 — 문서 쪽 서술은 여전히 존재하므로 페이지에서 문서 서술을 지우지 말고 '문서(ref-039)는 is_parking_spot, 현재 구현(ref-536·ref-1543)은 is_charger' 로 둘 다 제시하고 구현 기준 판단임을 밝혀야 함. 참고로 입력의 RobotUpdateHandle.hpp(ref-537) 주석도 is_charger() 속성 경유점을 충전기로 본다고 적지만 브리프 finding 이 아니므로 이번 페이지에 새로 인용하지 않는다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: LiftRequest.msg·LiftState.msg 원문(data/source_texts/ref-312·ref-286) 필드와 주석('unique at least between different requesters', 'granted control of the lift until ... REQUEST_END_SESSION') 일치. 같은 프로젝트 자료."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 두 메시지 전체 필드 대조 결과 최대 점유 시간·예약 시간창·다중 목적층 필드 없음(destination_floor 는 단일 문자열). 메시지 정의 범위의 사실로만 쓴다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: 메시지 정의만 본 결론이라는 한정이 적절함. 승강기 어댑터(ref-284)가 요청을 중계·차단한다는 기존 내용과 모순 없음. 의견 주체 명시 필요."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC 판(PMC11946681)과 출판 PDF 메타데이터에서 Han·Ding·Liu·Meng, Sensors 25(6) 1783, doi 10.3390/s25061783, 2025-03-13, 승강기 노드 암묵적 경유점·MTVRP·ALNS 확인. 이번 검증에서 PMC 페이지도 열림. 용어는 용어집의 '다중 운행 차량 경로 문제'로 맞춰야 함."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC 원문 Discussion 의 '60 customer nodes ... 40 s to 100 s nearly doubles the total travel time (from 225 s to 500 s)'. 원문 자체가 'nearly doubles' 라고 쓰므로 기존 3절 '거의 두 배'는 원문 표현과 어긋나지 않음 — 수치 병기로 고치되 '틀린 요약'으로 기록하지 않는다. 호텔 수치 실험이며 기존 3절 문장과 같은 주장(ref-103 재사용)."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: 가정한 승강기 운행 시간을 바꾼 수치 실험이라는 점은 원문과 맞음. 의견 주체 명시 필요."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC 원문 결론의 후속 연구(무작위·동적 승강기 운행 시간, 동적 수요, 다중 로봇 협업·충돌 회피, 지능형 승강기 스케줄링) 확인."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2603.22731 v1(2026-03-24) 초록에서 task assignment·service sequencing·optional charging decisions·charging mode selection·charger access 공동 최적화 확인. 저자 5명 모두 UT Austin. 프리프린트(동료심사 미확인)임을 본문에 밝힌다. MILP 한글 표기는 용어집 '혼합 정수 계획'으로."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv HTML v1 §2.2 'minimizes total degradation, charger waiting, tardiness, and degradation imbalance'."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §2.6 세션 집합 Ωm 이 모든 로봇의 세션으로 정의되고 'each unordered pair of distinct sessions' 마다 순서 변수로 비중첩(33)–(34)을 둠. 다만 '같은 로봇의 세션 쌍 포함'은 논문이 명시한 문장이 아니라 집합 정의에서 따라 나오는 것이므로 본문에서는 '세션 집합이 모든 로봇의 세션을 포함하도록 정의돼 있어' 처럼 정의에 근거해 적는다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §4.1 100×50 m 창고·동종 로봇·standard/fast 두 방식, §4.4 'illustrative expected averages'·|R|=4,|K|=40,|M|=2, 표 2 열화 0.214→0.098, §1 기여 'up to 54% over rule-based dispatch'. 단일 대표 사례의 예시값이며 핵심 수치이나 단일 출처."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: 초록의 'reduced-form degradation proxies' 와 §4.4 'illustrative expected averages' 로 뒷받침됨. 의견 주체 명시 필요."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(MDPI 403). Crossref 메타데이터(doi 10.3390/pr14152424, Processes 14(15) 2424, 2026-07-27, 저자 6명) 확인, 초록에서 냉동 컨테이너 온도 제약·태양광·풍력·ESS 항만 마이크로그리드·2단계(1단계 작업·야드 배정, 2단계 에너지 스케줄링)·운영비 최소화 확인. 시간대별 요금·충전소 용량은 초록에 없음. 추정 유지, 신뢰도 low 유지."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지(원문 미열람 근거). 후보 자료로만 쓰고 수치·국내 적용 근거로 채택하지 않는다는 한정이 적절. 항만 마이크로그리드 운영은 ROP 직접 범위 밖 연계 대상."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: rmf_fleet_adapter CHANGELOG.rst(2.14.0 태그) 2.12.0 (2026-02-23) 'Publish WaitForCharge phase completed (#502)', 'Retreat to charger if there will not be enough charge for the next task (#423)'."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 2.13.0 (2026-06-15) 'Fix potential deadlocks from execution of mutex lock and release (#490)', 최신 2.14.0 은 2026-09-26."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f25·f26 수정 이력에서 도출. 의견 주체 명시 필요. 변경 이력은 수정의 존재만 보여 주며 이전 판의 결함 범위를 정량화하지 않는다는 한정과 함께 쓴다."
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
      "ref-1545(rmf_ros2 2.14.0 rmf_fleet_adapter/CHANGELOG.rst)는 같은 날 실행 2026-10-10-03 의 ref-1487, 2026-10-10-04 의 ref-1513 과 URL 이 같다 — 새 참고문헌으로 중복 등록하지 않는다",
      "f15 는 기존 3절 둘째 단락의 호텔 연구 문장(ref-103, 225→500 s)과 같은 주장이다 — 새 문장을 더하지 말고 기존 문장을 고친다",
      "f8·f9·f10 은 6절 분리 페이지(2026-09-25-area16-s6) 53행의 is_parking_spot/is_charger 충돌 문장과 겹친다 — 교체 대상",
      "f1·f2·f6 은 기존 3절 첫 문장이 criticalLowChargingLevel 과 recharge_threshold 를 같은 '충전 임계값'으로 묶은 표현과 어긋난다(f6: 둘은 단위·의미가 다름)",
      "f2 는 기존 5절 제약 행 '보내야 한다'(ref-228)와 충돌하나 ref-228 원문도 should 이므로 정정으로 처리한다",
      "ref-403 은 24. 작업·워크플로 모델링 등에서 쓰인 기존 id 재사용(정상)"
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "f14: '다회 운행 차량 경로 문제' — 용어집 multi-trip-vehicle-routing-problem 의 한글 표기는 '다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))'",
      "f18: '혼합 정수 선형 계획' — 용어집 milp 의 한글 표기는 '혼합 정수 계획 (Mixed Integer Linear Programming (MILP))'"
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "5절 제약 행: '팩트시트의 임계 저충전 수준 이하에서는 관제가 충전소로 가는 주문만 보내야 한다. [사실][^ref-228]' 을 f1·f2 에 따라 '팩트시트의 임계 충전 수준(백분율, 로봇 유형별 선언값) 이하에서는 관제가 충전소로 가는 주문만 보내는 것이 좋다고 권고(should)한다' 로 고치고 각주는 [^ref-031][^ref-228] 로 둔다 — ref-031 3.0.0 명세 표와 ref-228 스키마 설명이 모두 should 이다(외부 메모 기반 정정이며 corr id 는 없음).",
    "3절 첫 문장: criticalLowChargingLevel 과 recharge_threshold 를 같은 '충전 임계값'으로 묶은 괄호 표현을 f1·f5·f6 에 맞게 'VDA 5050 의 임계 충전 수준(관제의 주문 제한 기준, 백분율)과 Open-RMF 의 recharge_threshold(운행 하한, 0~1 비율)' 처럼 둘의 의미·단위를 구분해 고친다 — f6 과 기존 문장이 어긋난다. 태그는 기존 [추정] 유지.",
    "3절 호텔 연구 문장: 새 문장을 더하지 말고 기존 문장을 f15·f16 기준으로 고친다(저자 Han 외 2025, 고객 노드 60개·승강기 운행 시간 40→100 s·총 이동 시간 약 225→500 s, 가정한 운행 시간을 바꾼 모델 수치 실험이며 실측 대기열 손실이 아님을 [의견]으로 덧붙임). '거의 두 배'는 원문(nearly doubles) 표현이므로 지워도 되지만 틀린 요약이라고 서술하지 않는다.",
    "[^ref-103] 각주를 'Han, L., Ding, J., Liu, S., & Meng, M.(Sensors 25(6) 1783, doi:10.3390/s25061783), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-10-10' 으로 고치고 ' (원문 미열람)' 표시를 뺀다 — 이번 실행과 검증에서 원문을 열었다. reference_updates 에도 저자·발행일을 반영한다.",
    "f14 의 MTVRP 한글 표기를 용어집대로 '다중 운행 차량 경로 문제(Multi-Trip Vehicle Routing Problem, MTVRP)'로, f18 의 MILP 한글 표기를 용어집대로 '혼합 정수 계획(Mixed Integer Linear Programming, MILP)'으로 쓴다 — 용어집과 충돌.",
    "5절 상업 시설 사례(f14~f17): 블록 머리에 '현장 유형: 상업 시설'과 '다층 호텔 배송을 모델링한 수치 실험(실제 배치 아님)'을 밝히고, 여섯 항목 가운데 f14~f17 로 채울 수 없는 칸(예: 완료·인계, 수행 자원의 설비 쪽 분담)은 '미확인'으로 두며 새 사실을 지어 넣지 않는다. 물류창고 사례 머리의 '다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다' 문장은 상업 시설 사례 추가에 맞게 고친다. site_matrix_updates 는 site_type '상업 시설' 한 칸만 낸다.",
    "f23·f24(Yang 외, ref-1544)는 5절 적용 사례로 쓰지 않고 8절 분리 페이지의 '원문 미열람 후보 자료'로만 [추정]·[의견]으로 둔다. 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-1544 에 source_unopened: true 를 둔다. 항만 마이크로그리드(태양광·풍력·ESS) 운영은 ROP 직접 범위가 아니라 연계 대상으로 짧게 적는다(원문 19장 시설·설비 제어·업종별 조건 경계).",
    "6절 분리 페이지 53행 충돌 문장 교체(f8·f9·f10): 문서 서술을 지우지 말고 'Open-RMF 지원 작업 문서(ref-039)는 충전소를 is_parking_spot 으로 설정한다고 적지만, 현재 구현의 그래프 API(ref-536)와 rmf_fleet_adapter 2.14.0 파서(ref-1543)는 주차 지점과 충전 지점을 별도 속성으로 두고 충전소를 is_charger 로 지정한다' 처럼 둘 다 제시한 뒤, 구현 기준으로 충전소 지정은 is_charger 로 보는 것이 이 위키의 판단임을 [의견]으로 적는다 — 검증에서 ref-039 ChargingTask 절이 실제로 is_parking_spot 을 쓰는 것을 확인했다. Graph.hpp 주석 복사 오류는 필요하면 한 문장으로만 언급한다.",
    "6·7절 분리 페이지: VDA 백분율 선언과 Open-RMF 비율 설정의 단위·의미 구분(f4·f5·f6)과 두 값의 우선순위 규칙이 확인한 두 원문에 없다는 점(f7, [추정], 조사 범위 한정 문구 포함)을 넣는다. f5 의 0.10·1.0 은 템플릿 예시값이지 권장값이 아님을 밝힌다.",
    "7절 분리 페이지: 승강기 메시지의 필드(f11)와 점유 시간·시간창·다중 목적층 필드 부재(f12)를 사실로, 배분 정책 부재로 넓히지 않는다는 한정(f13)을 [의견]으로 적는다. Open-RMF 충전 작업 삽입·뮤텍스 그룹 서술에는 rmf_fleet_adapter 2.12.0(2026-02-23)·2.13.0(2026-06-15)의 수정 이력(f25·f26)과 판 기록 권고(f27, [의견])를 붙인다.",
    "ref-1545 는 rmf_ros2 2.14.0 rmf_fleet_adapter/CHANGELOG.rst 로, 같은 날 실행 2026-10-10-03(ref-1487)·2026-10-10-04(ref-1513)와 URL 이 같다 — docs/references/index.md 에 이 URL 이 이미 등록돼 있으면 그 id 를 각주와 프런트매터에 쓰고 ref-1545 를 새로 등록하지 않으며, 등록돼 있지 않으면 reference_updates 의 URL 을 그대로 두어 퍼블리셔가 기존 id 로 합치게 한다.",
    "8절 분리 페이지(Li 외, ref-403): 프리프린트(arXiv v1, 2026-03-24, 동료심사 미확인)임을 밝히고, f20 의 '같은 로봇의 세션 쌍 포함'은 논문의 명시 문장이 아니라 세션 집합 Ωm 이 모든 로봇의 세션을 포함하도록 정의된 데서 따라 나온다고 적는다. 최대 54% 열화 감소(f21)는 대표 사례 하나의 예시적 기대 평균임을 같은 문장에 붙이고, 현장 배터리 수명 개선값으로 쓰지 않는다는 f22 를 [의견]으로 둔다.",
    "f3·f6·f10·f13·f16·f22·f24·f27 의 [의견] 문장은 '이 위키는 본다'처럼 의견 주체를 밝힌다 — 의견 표기 규칙.",
    "[^ref-031] 각주의 접근일을 2026-10-10 으로 갱신하고, 본문에서 batteryCharging 을 인용할 때 '3.0.0 판 기준(발행일 미확인)'을 밝힌다 — 이번 열람은 3.0.0 태그판이다.",
    "11절(분리 페이지)과 열린 질문 갱신: oq-069 는 해결로 바꾸되 해결 근거를 f8·f9 와 문서 서술(ref-039)이 다르다는 점으로 적는다. oq-066(f23·f24 후보 자료만)·oq-067(f11~f13)·oq-068(f4~f7)은 부분 근거만 적고 열림 상태를 유지한다. 새 질문 4건은 브리프 형식대로 등록한다.",
    "트랙 반영 제안 4건(IDTA 02047 충전 요소 2건·IDTA 디지털 배터리 여권 1건·rmf_traffic 문·승강기·VDA 해제 구역 1건)은 이번 브리프의 finding 이 다루지 않았으므로 7절·6절에 반영하지 않고 제안 상태로 둔다 — 근거 finding 없이 반영하면 드리프트다. oq-060(IDTA 02047 출처 충돌)도 그대로 둔다.",
    "원문의 직접 인용은 출처당 1회 이하로 하고 나머지는 재서술한다 — ref-031·ref-403·ref-103 은 브리프 발췌에 여러 구절이 있어 페이지에서 반복 인용하기 쉽다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 27건, 미확인 0건, 교차 확인 0건. 강등: 없음. 원문 미열람 출처: ref-1544(Yang 외, Crossref 초록만 확인). 주의: 이번 브리프는 외부 AI 조사 메모를 바꾼 것이라 이 실행 안의 검색 기록이 없고, 한국 자료는 없다. VDA 5050·Open-RMF 출처는 모두 같은 발행 주체나 같은 프로젝트의 자료라 독립 교차 확인으로 세지 않았다. VDA 5050 3.0.0 명세와 factsheet.schema(ref-228)는 모두 임계 충전 수준 이하 주문 제한을 권고(should)로 적으므로, 5절 제약 행의 '보내야 한다'는 권고 표현으로 정정한다. 호텔 연구(ref-103)는 이번 실행에서 원문을 처음 열었고, 원문 자체가 'nearly doubles'(225→500 s)라고 쓴다. Li 외(ref-403)의 최대 54% 열화 감소는 프리프린트 속 대표 사례 하나의 예시값이다. oq-069 해결 인정(f8·f9): 현재 구현은 충전소를 is_charger 로 지정하고, 지원 작업 문서(ref-039)는 아직 is_parking_spot 으로 적고 있어 두 서술을 함께 싣는다. oq-066·oq-067·oq-068 은 부분 근거만 있어 열린 질문으로 남긴다. 트랙 반영 제안 4건(IDTA 02047·배터리 여권·rmf_traffic 문·승강기 표현)은 이번 브리프가 조사하지 않아 반영하지 않았다. ref-1545 는 같은 날 실행 2026-10-10-03·04 에 등록된 변경 이력 출처(ref-1487·ref-1513)와 URL 이 같아 기존 id 로 합친다. 정정 요청(corr) 없음.",
  "retry_reason": null
}
```

### runs/2026-10-10-05/pages.json

```json
{
  "run_id": "2026-10-10-05",
  "outline": [
    {
      "path": "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "로봇마다 정한 충전 하한(VDA 5050 임계 충전 수준은 백분율 선언값, Open-RMF recharge_threshold 는 0~1 비율 운행 하한)에만 맞춰 충전하면 수요가 겹칠 수 있어 조율 계층이 충전·승강기 점유를 함께 맡아야 할 것으로 보인다. [추정][^ref-031][^ref-105]",
      "planned_findings": [
        "f1",
        "f5",
        "f6",
        "f15",
        "f16"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2600,
      "summary": "물류창고 가상 시나리오(제약 행을 VDA 5050 권고 표현으로 정정)와 다층 호텔 배송 수치 실험을 옮긴 상업 시설 사례를 둔다. [사실][^ref-031][^ref-103]",
      "planned_findings": [
        "f1",
        "f2",
        "f14",
        "f15",
        "f16",
        "f17"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 650,
      "summary": "현재 Open-RMF 구현은 충전소를 is_charger 로 지정하고(지원 작업 문서는 is_parking_spot), VDA 백분율 선언과 Open-RMF 비율 설정은 단위·의미가 다르다. [사실][^ref-536][^ref-1543]",
      "planned_findings": [
        "f1",
        "f5",
        "f8",
        "f9",
        "f10"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 650,
      "summary": "Open-RMF 승강기 메시지에는 점유 시간·시간창·다중 목적층 필드가 없고, rmf_fleet_adapter 는 2026년 충전·뮤텍스 관련 수정을 거쳤다. [사실][^ref-312][^ref-1545]",
      "planned_findings": [
        "f11",
        "f12",
        "f13",
        "f25",
        "f26",
        "f27"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 450,
      "summary": "Li 외(2026, 프리프린트)의 공용 충전기·열화 MILP 를 더하고, 54% 열화 감소는 대표 사례 하나의 예시값임을 밝힌다. [사실][^ref-403]",
      "planned_findings": [
        "f18",
        "f21",
        "f24"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
      "section": "11. 열린 질문",
      "budget_chars": 1100,
      "summary": "oq-069 해결(구현은 is_charger), oq-066·oq-067·oq-068 부분 근거, 새 질문 4건. [사실][^ref-536][^ref-1543]",
      "planned_findings": [
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f23",
        "f24"
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md",
      "section": "1~7절 (주제 페이지 본문)",
      "budget_chars": 3200,
      "summary": "충전 하한 값의 단위·의미 구분, 충전소 is_charger 지정, 승강기 메시지 범위, Open-RMF 판 기록, 공용 충전기·열화 MILP, 항만 물류–에너지 후보 자료를 정리한다. [사실][^ref-031][^ref-1543][^ref-403]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f18",
        "f19",
        "f20",
        "f21",
        "f22",
        "f23",
        "f24",
        "f25",
        "f26",
        "f27"
      ]
    },
    {
      "path": "docs/topics/2026/2026-09-25-area16-s6.md",
      "section": "3. 본문",
      "budget_chars": 550,
      "summary": "충전소 속성 충돌 문장을 정정하는 소제목을 덧붙여 문서(is_parking_spot)와 구현(is_charger)을 함께 제시한다. [사실][^ref-039][^ref-536][^ref-1543]",
      "planned_findings": [
        "f8",
        "f9",
        "f10"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "3절 충전 값 의미·단위 구분과 호텔 연구 수치(Han 외 2025) 보강, 5절 제약 행 권고 표현 정정·상업 시설(호텔 수치 실험) 사례 추가, 6·7·8·11절 갱신 요약과 새 주제 페이지 링크, 13절 각주 갱신(ref-031·ref-103 등)",
      "patches": [
        {
          "section": "3. 왜 중요한가",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-05/pages/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-05/pages/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-05/pages/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-05/pages/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-05/pages/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-05/pages/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-05/pages/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md 의 해당 절을 본다)",
          "frontmatter": {
            "sources": [
              "ref-031",
              "ref-039",
              "ref-051",
              "ref-060",
              "ref-079",
              "ref-098",
              "ref-103",
              "ref-104",
              "ref-105",
              "ref-109",
              "ref-146",
              "ref-216",
              "ref-219",
              "ref-228",
              "ref-284",
              "ref-286",
              "ref-312",
              "ref-321",
              "ref-377",
              "ref-403",
              "ref-530",
              "ref-531",
              "ref-532",
              "ref-533",
              "ref-534",
              "ref-535",
              "ref-536",
              "ref-537",
              "ref-538",
              "ref-1543",
              "ref-1544",
              "ref-1545"
            ],
            "last_run": "2026-10-10"
          }
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "신규 작성: 충전 하한 값 구분, 충전소 is_charger 지정(oq-069 해결), 승강기 메시지 범위, Open-RMF 판 기록, 공용 충전기·열화 MILP, 항만 물류–에너지 후보 자료"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area16-s6.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "3. 본문 끝에 충전소 속성 충돌 문장 정정 소제목 추가(문서 is_parking_spot·구현 is_charger 병기, 구현 기준 판단은 의견)",
      "patches": [
        {
          "section": "3. 본문",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-05/pages/topics/2026/2026-09-25-area16-s6.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-10-area28-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 28. 공용 자원·충전·에너지 최적화 의 \"11. 열린 질문\" 절(1,117자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area28-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 28. 공용 자원·충전·에너지 최적화 의 \"3. 왜 중요한가\" 절(770자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area28-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 28. 공용 자원·충전·에너지 최적화 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(637자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area28-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 28. 공용 자원·충전·에너지 최적화 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(555자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area28-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 28. 공용 자원·충전·에너지 최적화 의 \"6. 대표 접근법과 기술\" 절(535자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area28-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 28. 공용 자원·충전·에너지 최적화 의 \"8. 대표 연구와 자료\" 절(440자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-10 | 28. 공용 자원·충전·에너지 최적화 | 5절 제약 행을 VDA 5050 권고 표현으로 정정하고 상업 시설(호텔 수치 실험) 사례 추가, 3절 충전 값 구분·호텔 수치 보강, 충전소 is_charger 정리(oq-069 해결), 공용 충전기·승강기 메시지 확인 주제 페이지 신설 | run 2026-10-10-05",
  "index_updates": {
    "home_recent": "2026-10-10 — 28. 공용 자원·충전·에너지 최적화: 충전 하한 권고 표현 정정, 충전소 is_charger 정리(oq-069 해결), 상업 시설 사례와 공용 충전기·열화 연구 추가",
    "category_recent": "2026-10-10 — 28. 공용 자원·충전·에너지 최적화: 5절 제약 행 정정·상업 시설 사례 추가, 6·7·8·11절 갱신과 주제 페이지 '충전 하한과 충전소 지정, 승강기 세션 점유는 무엇이 확인됐는가' 신설",
    "area_recent": "2026-10-10 — 28. 공용 자원·충전·에너지 최적화: 3·5절 정정·보강, 6·7·8·11절에 갱신 요약과 새 주제 페이지 링크, 6절 분리 페이지에 충전소 속성 정정 추가"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "VDA 5050 3.0.0 명세 원문. 이번에는 3.0.0 태그판의 팩트시트 batteryCharging 표(임계·최대·최소 희망 충전 수준 백분율, 최소 충전 시간)를 대조했다.",
      "cited_by": [
        "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
        "docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md"
      ]
    },
    {
      "id": "ref-105",
      "org": "Open Robotics (open-rmf)",
      "title": "fleet_adapter_template — fleet_adapter_template/config.yaml",
      "published": null,
      "url": "https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 플릿 어댑터 설정 템플릿. recharge_threshold(운행 하한 비율 0.10)와 recharge_soc(충전 목표 비율 1.0) 등 배터리·충전 설정 예시값을 담는다.",
      "cited_by": [
        "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
        "docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md"
      ]
    },
    {
      "id": "ref-536",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 교통 그래프 API 헤더. 경유점의 주차 지점·충전 지점·대기 지점 속성과 뮤텍스 그룹 등을 정의한다(set_charger 위 주석은 주차 지점 문구가 잘못 복사돼 있음).",
      "cited_by": [
        "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
        "docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md",
        "docs/topics/2026/2026-09-25-area16-s6.md"
      ]
    },
    {
      "id": "ref-1543",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp (2.14.0)",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 2.14.0 태그의 탐색 그래프 YAML 파서. 경유점 옵션 is_parking_spot·is_holding_point·is_passthrough_point·is_charger 를 각각 별도 속성으로 변환한다(발행일은 2.14.0 패키지판 날짜).",
      "cited_by": [
        "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
        "docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md",
        "docs/topics/2026/2026-09-25-area16-s6.md"
      ]
    },
    {
      "id": "ref-312",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 승강기 요청 메시지. 승강기 이름·요청 시각·세션 id·요청 유형(세션 종료·AGV 모드·사람 모드)·목적층·문 상태 필드를 정의한다.",
      "cited_by": [
        "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
        "docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md"
      ]
    },
    {
      "id": "ref-286",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 승강기 상태 메시지. 층·문·운행·모드 상태와 세션 종료 요청 때까지 제어권을 가진 session_id 를 보고한다.",
      "cited_by": [
        "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
        "docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md"
      ]
    },
    {
      "id": "ref-103",
      "org": "Han, L., Ding, J., Liu, S., & Meng, M.(Sensors 25(6) 1783, doi:10.3390/s25061783)",
      "title": "The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments",
      "published": "2025-03-13",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "Sensors 25(6) 1783, doi:10.3390/s25061783. 다층 호텔 배송 로봇 경로 계획을 승강기 노드를 암묵적 경유점으로 둔 MTVRP 로 정식화하고 승강기 운행 시간 민감도를 수치 실험한다. 2026-10-10 실행에서 원문을 처음 열어 저자·발행일을 보강했다.",
      "cited_by": [
        "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-403",
      "org": "Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin)",
      "title": "Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots",
      "published": "2026-03-24",
      "url": "https://arxiv.org/abs/2603.22731",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "arXiv 프리프린트 v1. 작업 배정·순서·충전 방식·공용 충전기 비중첩 제약을 MILP 로 함께 풀어 열화·충전기 대기·납기 지연·열화 불균형을 줄이는 계층형 해법을 제시한다(가상 창고 수치 실험).",
      "cited_by": [
        "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
        "docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1544",
      "org": "Song Yang, Sichen Yue, Xiao Wang, Kaiyu Wang, Xin Tian, Xiao Wang (Processes, MDPI)",
      "title": "A Two-Stage Logistics–Energy Coordinated Optimization Framework for AGV Scheduling and Charging Under Reefer Container Temperature Constraints",
      "published": "2026-07-27",
      "url": "https://www.mdpi.com/2227-9717/14/15/2424",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "원문 미열람. Crossref 초록 기준으로 냉동 컨테이너 온도 제약 아래 항만 AGV 작업·충전을 태양광·풍력·ESS 를 갖춘 항만 마이크로그리드와 결합해 운영비를 최소화하는 2단계 프레임워크다.",
      "cited_by": [
        "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
        "docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1545",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0)",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 패키지 변경 이력(2.14.0 태그). 2.12.0(2026-02-23)의 충전 대기 단계 완료 발행·충전기 복귀 변경과 2.13.0(2026-06-15)의 뮤텍스 잠금·해제 교착 수정을 기록한다. 같은 날 실행 2026-10-10-03·04 의 출처와 URL 이 같아 퍼블리셔가 기존 id 로 합친다.",
      "cited_by": [
        "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md",
        "docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "update",
      "id": "oq-069",
      "question": "출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot(지원 작업 문서)과 is_charger(교통 편집기 문서·데모 README) 가운데 어느 속성으로 하는가?",
      "areas": [
        15,
        28
      ],
      "status": "해결",
      "link": "docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md"
    },
    {
      "action": "new",
      "question": "공용 충전기 예약 시간이 끝났는데 로봇이 충전기 앞을 떠나지 못할 때 다음 예약의 시작을 어떻게 조정하는가?",
      "areas": [
        28,
        27
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "충전 상태(SOC) 추정 오차와 충전소까지의 이동·대기 에너지를 반영해 운영 하한에 더할 여유를 어떻게 검증하는가?",
      "areas": [
        28,
        5
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "배터리 열화 최적화 모델의 예시 결과를 실제 셀·충전기·장기 운용 데이터로 검증한 공개 재현 자료가 있는가?",
      "areas": [
        28,
        57
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "승강기 운행 시간 민감도와 실제 승강기 대기열·최대 점유 시간의 관계를 같은 실험에서 측정한 자료가 있는가?",
      "areas": [
        28,
        22
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "상업 시설",
      "item": "시작 조건",
      "link": "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "28. 공용 자원·충전·에너지 최적화"
    },
    {
      "site_type": "상업 시설",
      "item": "작업 대상",
      "link": "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "28. 공용 자원·충전·에너지 최적화"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "28. 공용 자원·충전·에너지 최적화"
    },
    {
      "site_type": "상업 시설",
      "item": "제약",
      "link": "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "28. 공용 자원·충전·에너지 최적화"
    },
    {
      "site_type": "상업 시설",
      "item": "예외·성과",
      "link": "docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "28. 공용 자원·충전·에너지 최적화"
    }
  ],
  "additional_research_requests": [
    "6절 분리 페이지(docs/topics/2026/2026-09-25-area16-s6.md) 53행의 is_parking_spot/is_charger 충돌 문장 자체는 페이지 본문이 이번 입력에 없어 교체하지 못하고 3. 본문 끝에 정정 소제목만 덧붙였다 — 다음 갱신 실행에서 이 페이지를 입력으로 넣어 해당 문장을 정정 문장으로 바꿔야 한다",
    "7·8·11절 분리 페이지(2026-09-25-area16-s7·s8·s11)는 입력에 없고 하루 갱신 상한(2)도 찼으므로 고치지 않았다. 승강기 메시지 필드 범위·rmf_fleet_adapter 판 기록(7절), Li 외·Yang 외(8절), oq 상태(11절)는 새 주제 페이지와 세부영역 6·7·8·11절 요약에 실었다 — 다음 갱신에서 분리 페이지에도 반영할지 정해야 한다",
    "트랙 반영 제안 4건(IDTA 02047 충전 요소 2건, IDTA 디지털 배터리 여권 1건, rmf_traffic 문·승강기·VDA 해제 구역 1건)은 이번 브리프가 다루지 않아 반영하지 않았다 — 7·6절 반영을 위해 IDTA 02047 템플릿 원문(oq-060)과 배터리 여권 템플릿 본문, rmf_traffic 문·승강기 표현 원문 조사가 필요하다",
    "11절 oq-066: 물류센터 로봇의 시간대별 전기 요금·최대 수요 전력 기준 충전 계획 연구와 국내 사례(한국어 자료)가 필요하다. Yang 외(ref-1544)는 원문 미열람이라 수치를 쓸 수 없다",
    "11절 oq-067: Open-RMF 승강기 감독(lift supervisor) 등 메시지 밖 구성요소의 타임아웃·대기열 구현 조사가 필요하다",
    "5절: 물류창고·상업 시설 밖 현장 유형(병원·제조 공장 등)의 충전·승강기 공용 자원 사례와 상업 시설 사례의 완료·인계 항목 근거가 필요하다"
  ],
  "fixes_applied": [
    "5절 제약 행 정정 — '보내야 한다' 문장을 'VDA 5050 은 팩트시트의 임계 충전 수준(백분율, 로봇 유형별 선언값) 이하에서는 관제가 충전소로 가는 주문만 보내는 것이 좋다고 권고(should)한다(3.0.0 판 기준, 발행일 미확인)'로 바꾸고 각주를 [^ref-031][^ref-228]로 두었다(corr id 없음).",
    "3절 첫 문장 — 같은 '충전 임계값'으로 묶던 괄호를 'VDA 5050 의 임계 충전 수준(관제의 주문 제한 기준, 백분율)이나 Open-RMF 의 recharge_threshold(운행 하한, 0~1 비율)'로 의미·단위를 구분해 고쳤고 태그는 [추정] 그대로 두었다.",
    "3절 호텔 연구 문장 — 새 문장을 더하지 않고 기존 문장을 Han 외(2025), 고객 노드 60개·40→100초·약 225→500초로 고쳤으며 '거의 두 배'는 틀렸다는 서술 없이 뺐고, 모델 수치 실험이라는 [의견](이 위키는 본다)을 덧붙였다.",
    "[^ref-103] 각주 — 세부영역 13절에서 지시된 저자·Sensors 서지·doi·발행일 2025-03-13·접근일 2026-10-10 형식으로 바꾸고 '(원문 미열람)'을 뺐으며, reference_updates 의 ref-103 에도 저자·발행일을 반영했다.",
    "용어 표기 — MTVRP 는 5절 상업 시설 사례에서 '다중 운행 차량 경로 문제(Multi-Trip Vehicle Routing Problem, MTVRP)'(용어집 링크)로, MILP 는 주제 페이지 3절에서 '혼합 정수 계획(Mixed Integer Linear Programming, MILP)'으로 썼다.",
    "5절 상업 시설 사례 — '현장 유형: 상업 시설'과 '다층 호텔 배송을 모델링한 수치 실험(실제 배치 아님)'을 사례 머리에 밝히고, 완료·인계와 수행 자원의 설비 쪽 분담·복구 주체는 '미확인'으로 두었으며, 물류창고 머리 문장을 상업 시설 사례 추가에 맞게 고쳤다. site_matrix_updates 는 상업 시설(상업 시설|G 한 칸)에 해당하는 항목만 냈고 물류창고·실외는 내지 않았다(주제 페이지 4절의 가상 창고 수치 실험도 이 지시에 따라 매트릭스에 내지 않음).",
    "Yang 외(ref-1544) — 5절 적용 사례에 쓰지 않고 8절 성격의 원문 미열람 후보 자료로만 주제 페이지 3절과 세부영역 8절 요약에 [추정]·[의견]으로 두었으며, 각주 접근일 뒤에 '(원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다. 항만 마이크로그리드 운영은 주제 페이지 5절 연계 범위에 연계 대상으로 짧게 적었다.",
    "6절 분리 페이지 충돌 문장 — 해당 페이지 본문이 입력에 없어 53행을 직접 바꾸지 못했으므로, 그 페이지 '3. 본문' 끝에 '2026-10-10 정정' 소제목을 덧붙여 정정 대상 문장을 밝히고 '지원 작업 문서(ref-039)는 is_parking_spot, 현재 구현 그래프 API(ref-536)·rmf_fleet_adapter 2.14.0 파서(ref-1543)는 별도 속성·is_charger' 를 둘 다 제시한 뒤 구현 기준 판단을 [의견]으로 적었다. 같은 내용을 세부영역 6절과 주제 페이지 3절에도 실었고, 원 문장 교체는 additional_research_requests 에 올렸다. Graph.hpp 주석 복사 오류는 언급하지 않았다.",
    "6·7절 분리 페이지 내용(VDA 백분율 선언과 Open-RMF 비율 설정의 단위·의미 구분, f7 우선순위 규칙 부재와 조사 범위 한정, 0.10·1.0 이 템플릿 예시값임) — 분리 페이지가 입력에 없고 하루 갱신 상한이 차서, 새 주제 페이지 3절 '충전 하한' 소제목과 세부영역 6절 요약에 넣었다.",
    "7절 분리 페이지 내용(승강기 메시지 필드와 점유 시간·시간창·다중 목적층 필드 부재를 [사실], 배분 정책 부재로 넓히지 않는다는 [의견], rmf_fleet_adapter 2.12.0·2.13.0 수정 이력 [사실]과 판 기록 권고 [의견]) — 같은 이유로 주제 페이지 3절과 세부영역 7절 요약에 넣었다.",
    "ref-1545 — 입력의 참고문헌 색인에 같은 URL(ref-1487·ref-1513)이 아직 등록돼 있지 않아 각주·프런트매터에 ref-1545 를 쓰고 reference_updates 에 URL 을 그대로 두어 퍼블리셔가 기존 id 로 합치게 했다.",
    "Li 외(ref-403) — 주제 페이지 3절에 프리프린트(arXiv v1, 2026-03-24, 동료심사 미확인)를 밝히고 같은 로봇의 세션 쌍은 세션 집합이 모든 로봇의 세션을 포함하도록 정의된 데서 따라 나온다(논문이 따로 명시하지 않음)고 적었으며, 최대 54% 열화 감소는 대표 사례 하나의 예시적 기대 평균임을 같은 문장(주제 4절 예외·성과, 세부영역 8절)에 붙이고 f22 를 [의견]으로 두었다.",
    "[의견] 주체 명시 — f3·f6·f10·f13·f16·f22·f24·f27 의 의견 문장을 모두 '이 위키는 … 본다/쓰지 않는다' 형식으로 썼다.",
    "[^ref-031] — 세부영역·주제 페이지 각주 접근일을 2026-10-10 으로 갱신하고, batteryCharging·임계 충전 수준을 인용한 곳(세부영역 5·6절, 주제 3절)에 '3.0.0 판 기준(발행일 미확인)'을 밝혔다.",
    "11절·열린 질문 — oq-069 를 해결(link: 새 주제 페이지)로 open_question_updates 에 내고 해결 근거를 f8·f9 와 문서(ref-039) 서술 차이로 적었으며, oq-066·oq-067·oq-068 은 세부영역 11절에 부분 근거만 적고 열림을 유지했다. 새 질문 4건은 브리프 형식대로 new 로 등록했다.",
    "트랙 반영 제안 4건 — 근거 finding 이 없어 6·7절에 반영하지 않고 제안 상태로 두었으며 oq-060 도 건드리지 않았다(추가 조사 요청에 기록).",
    "직접 인용 — ref-031 은 세부영역 5절의 '(should)' 한 단어만 인용하고 주제 페이지에서는 재서술했으며, ref-403·ref-103 은 원문 구절을 인용하지 않고 모두 재서술했다.",
    "docs/topics/2026/2026-09-25-area16-s6.md: 각주 정의 1개를 참고문헌에서 만들어 붙임: ref-1543",
    "분량 초과 자동 분리: 28. 공용 자원·충전·에너지 최적화 본문 7,011자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 4,052자"
  ]
}
```

### runs/2026-10-10-05/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md (7개 절)
    - docs/topics/2026/2026-09-25-area16-s6.md (1개 절)
- 분량 초과 자동 분리:
    - docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md "11. 열린 질문" → docs/topics/2026/2026-10-10-area28-s11.md (1,117자)
    - docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md "3. 왜 중요한가" → docs/topics/2026/2026-10-10-area28-s3.md (770자)
    - docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-10-area28-s10.md (637자)
    - docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-10-area28-s7.md (555자)
    - docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-10-area28-s6.md (535자)
    - docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-10-area28-s8.md (440자)
```

### runs/2026-10-10-05/pages/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md

```markdown
---
title: "28. 공용 자원·충전·에너지 최적화"
type: area
category: "G. 계획·최적화"
area_no: 28
related_areas: [5, 18, 22, 25, 27, 34, 35, 47]
tags: [충전 상태, 충전 임계값, 뮤텍스 그룹, 승강기 세션, VDA 5050, Open-RMF]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-10-10
sources: [ref-031, ref-039, ref-051, ref-060, ref-079, ref-098, ref-103, ref-104, ref-105, ref-109, ref-146, ref-216, ref-219, ref-228, ref-284, ref-286, ref-312, ref-321, ref-377, ref-403, ref-530, ref-531, ref-532, ref-533, ref-534, ref-535, ref-536, ref-537, ref-538, ref-1543, ref-1544, ref-1545]
last_run: 2026-10-10
version: 3
---

[홈](../../index.md) › [G. 계획·최적화](index.md) › 28. 공용 자원·충전·에너지 최적화

# 28. 공용 자원·충전·에너지 최적화

!!! info "소속 대분류"
    [G. 계획·최적화](index.md) — 핵심 질문:
    누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

로봇마다 정해 둔 충전 하한 — VDA 5050 의 임계 충전 수준(criticalLowChargingLevel, 관제의 주문 제한 기준, 백분율)이나 Open-RMF 의 recharge_threshold(운행 하한, 0~1 비율) — 에만 맞춰 충전을 시작하면 충전 수요가 겹칠 수 있으므로, 충전소 대기를 반영한 충전 시점·충전기 선택, 공유 충전기의 우선 충전 정책, 충전기·승강기 점유의 예약·세션 관리를 조율 계층이 함께 맡아야 할 것으로 보인다. [추정][^ref-228][^ref-031][^ref-105][^ref-530][^ref-531][^ref-533][^ref-312]

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 왜 중요한가](../../topics/2026/2026-10-10-area28-s3.md)에 있다.

## 4. 핵심 개념과 용어

앞 절의 문제를 다루려면 배터리 상태와 공용 자원 점유를 표현하는 용어가 먼저 필요하다.

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area16-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 첫 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 2026-10-10 갱신에서 상업 시설 사례(다층 호텔 배송을 모델링한 수치 실험)를 더했고, 그 밖의 현장 유형 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹 → 출하

**시나리오:** 피킹 성수기에 충전 요청과 층간 출하 운반이 겹칠 때

다음은 설명을 위한 가상의 시나리오이다. 여러 제조사 로봇이 한 다층 물류센터에서 피킹 화물을 다른 층 출하 구역으로 옮기는 중에 충전 수요와 승강기 호출이 몰리는 상황을 가정한다.

| 항목 | 내용 |
|---|---|
| 시작 조건 | 로봇이 일련의 작업을 마칠 충전량이 부족하면 Open-RMF 작업 계획기가 충전 작업을 일정에 끼워 넣는다. [사실][^ref-104] 같은 시간대에 피킹을 마친 화물의 층간 운반 요청이 이어진다(가정). |
| 작업 대상 | 피킹을 마친 출하 대상 화물과 이를 실은 로봇이며, 충전기·승강기·대기 위치는 여러 로봇이 나눠 쓰는 공용 자원이다(가정). |
| 수행 자원 | 과충전 보호, 충전기와의 통신·정밀 도킹, 승강기 운행·설비 안전 제어는 로봇·충전 설비·승강기 쪽이 맡고, ROP 는 충전 시작·중지 요청, 상태 확인, 승강기 세션 요청과 모드 확인을 담당하는 것으로 보인다. [추정][^ref-031][^ref-216][^ref-284] |
| 제약 | VDA 5050 은 팩트시트의 임계 충전 수준(백분율, 로봇 유형별 선언값) 이하에서는 관제가 충전소로 가는 주문만 보내는 것이 좋다고 권고(should)한다(3.0.0 판 기준, 발행일 미확인). [사실][^ref-031][^ref-228] 승강기가 세션 단위로 한 요청자에게 점유되므로, 여러 제조사 로봇의 호출을 세션 순서·목적층 묶음으로 배분하지 않으면 층간 대기가 출하 마감을 위협할 수 있을 것으로 보인다. [추정][^ref-312][^ref-286][^ref-103] |
| 완료·인계 | 로봇 쪽 도킹 프레임워크(연계 대상)는 도킹 뒤 충전 시작 여부(isCharging)를 확인하는 함수를 둔다. [사실][^ref-216] 승강기 이용이 끝나면 세션 종료 요청을 보낼 때까지 제어권이 그 세션에 남는다. [사실][^ref-286] |
| 예외·성과 | VDA 5050 은 충전 주문이 운반 주문을 중단시킬 수 있다고 적는다. [사실][^ref-031] 여러 로봇이 비슷한 시각에 충전 하한에 닿아 충전기 대기열이 생기면 가용 로봇 수가 줄 수 있으므로, 주문이 적은 시간대의 기회 충전이나 충전 요청을 작업 배정과 함께 계획하는 방식이 처리량 손실을 줄이는 수단이 될 것으로 보인다. [추정][^ref-534][^ref-531][^ref-031] |

이 시나리오에서 이 영역이 관여하는 곳은 시작 조건(충전 작업을 언제 넣을지), 제약(충전 하한과 승강기 점유), 예외·성과(충전으로 빠지는 가용 로봇과 층간 대기)다. 화물의 인계 확인 자체는 다른 영역이 다룬다(가정).

실제 물류센터에서 충전 대기와 승강기 대기가 처리량을 얼마나 줄이는지는 이번 조사에서 확인되지 않았으며, [열린 질문](../../open-questions.md)의 oq-010 으로 남겨 둔다.

**현장 유형:** 상업 시설

**사례:** 다층 호텔에서 승강기를 거쳐 여러 층의 고객에게 배송(다층 호텔 배송을 모델링한 수치 실험이며 실제 배치 아님)

다음은 Han 외(2025)가 다층 호텔 배송을 모델링한 수치 실험을 여섯 항목으로 옮긴 것이며, 실제 현장 배치 사례가 아니다.

| 항목 | 내용 |
|---|---|
| 시작 조건 | 여러 층에 흩어진 고객 노드로 가는 배송 로봇의 경로 계획 문제가 주어지며, 논문은 이를 [다중 운행 차량 경로 문제](../../glossary/multi-trip-vehicle-routing-problem.md)(Multi-Trip Vehicle Routing Problem, MTVRP)로 정식화하고 적응형 대규모 이웃 탐색으로 푼다. [사실][^ref-103] |
| 작업 대상 | 층마다 흩어진 고객 노드와, 경로 안에서 암묵적 경유점으로 모델링한 승강기 노드다. [사실][^ref-103] |
| 수행 자원 | 배송 로봇이 승강기 노드를 거쳐 층을 옮기는 것으로 모델링된다. [사실][^ref-103] 승강기 설비 쪽의 호출·배분 분담은 미확인이다. |
| 제약 | 승강기 운행 시간이 모델의 입력이며, 고객 노드 60개 사례에서 승강기 운행 시간을 40초에서 100초로 늘리면 총 이동 시간이 약 225초에서 500초로 늘었다. [사실][^ref-103] |
| 완료·인계 | 미확인 |
| 예외·성과 | 논문은 무작위·동적 승강기 운행 시간, 동적 수요 변동, 다중 로봇 협업·충돌 회피, 지능형 승강기 스케줄링을 후속 연구 과제로 남긴다. [사실][^ref-103] 실패 시 누가 복구하는지는 미확인이다. |

이 사례에서 이 영역이 관여하는 곳은 제약(승강기라는 공용 자원의 운행 시간)과 예외·성과(그에 따른 총 이동 시간)다. 이 위키는 위 수치를 가정한 승강기 운행 시간을 바꾼 모델 민감도로 보며, 실제 승강기 대기열 손실값이나 여러 로봇이 승강기를 나눠 쓰는 배분 규칙의 근거로 쓰지 않는다. [의견][^ref-103]

## 6. 대표 접근법과 기술

Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다. [사실][^ref-104][^ref-536][^ref-312]

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술](../../topics/2026/2026-10-10-area28-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

VDA 5050 은 충전을 동작과 배터리 선언·상태 필드로 표현하고, Open-RMF 는 충전 설정·작업 계획기·교통 그래프·승강기 메시지로 공용 자원을 다룬다. [사실][^ref-031][^ref-105] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-10-area28-s7.md)에 있다.

## 8. 대표 연구와 자료

이 절은 충전 방식·정책의 처리량·비용 효과를 대기행렬로 분석한 창고 연구, 충전을 작업 배정·순서와 함께 푸는 최적화 연구, 승강기를 층간 병목으로 다룬 배송 로봇 연구로 나누어 정리한다.

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료](../../topics/2026/2026-10-10-area28-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP 가 직접 맡을 범위는 여러 제조사 로봇에 걸친 충전기·승강기·통로 구간·대기 위치의 예약과 배분, 충전 시점과 충전 목표 결정, 배터리 상태를 반영한 작업 배정 입력인 것으로 보인다. [추정][^ref-031][^ref-104][^ref-536][^ref-312]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 충전 시점·충전 목표 결정, 충전 시작·중지 요청, 배터리 상태 확인과 작업 배정 반영 | 과충전 보호, 충전기와의 통신·정밀 도킹, 배터리 관리 장치 |
| 시설·설비 제어 | 충전기·승강기·통로 구간·대기 위치의 예약과 배분, 승강기 세션 요청과 모드 확인 | 승강기 운행·설비 안전 제어 |

이 직접 범위는 VDA 5050 이 관제의 에너지 관리로 두고 Open-RMF 가 충전 작업 삽입·뮤텍스 그룹·승강기 세션으로 다루는 층위에 해당하는 것으로 보인다. [추정][^ref-031][^ref-104][^ref-536][^ref-312] 과충전 보호는 VDA 5050 이 이동로봇의 책임으로 명시한다. [사실][^ref-031] 정밀 도킹·충전 확인은 로봇 쪽 프레임워크가, 승강기 동작을 방해하는 요청의 차단은 승강기 어댑터가 맡으므로, ROP 는 요청과 상태 확인까지를 담당하는 연계 구조로 보인다. [추정][^ref-216][^ref-284] 경계의 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 충전과 공용 자원 점유를 매개로 배정·교통·설비 연동·설비 계획·능력 모델·상태 모델·시뮬레이션·학습 영역과 이어지는 것으로 보인다. [추정][^ref-534][^ref-536][^ref-312]

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 다른 연구영역과의 연결](../../topics/2026/2026-10-10-area28-s10.md)에 있다.

## 11. 열린 질문

충전·대기 시간을 성과 지표에서 어떻게 분류할지, 물류센터에서 충전·승강기 병목이 얼마나 되는지, 제조사가 다른 로봇이 충전기·승강기를 어떤 규칙으로 나눠 쓸지가 아직 확인되지 않았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 열린 질문](../../topics/2026/2026-10-10-area28-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) — 섹션 3~11 신규 작성(트랙 반영 제안 4건 반영, 1차 수정 지시 13건 이행), 2차 수정: 4·8절 연결 문장 태그 제거, 5절 조사 한계 문장 태그·각주 제거와 oq-010 연결, 6절 첫 문장을 출처 범위로 좁힘 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area16-s6.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장을 출처 범위(충전 작업 삽입·뮤텍스 그룹·승강기 세션)로 좁혔다 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료](../../topics/2026/2026-09-25-area16-s8.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: 첫 문장 태그 제거, 병원·호텔 연구 문구를 연관 관계로 고침, ref-535 제목 원문 복원 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area16-s7.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다(ref-536·ref-538 링크는 id 표기). 2차 수정: batteryCharging 행의 계획 입력 해석을 [추정]으로 분리 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 열린 질문](../../topics/2026/2026-09-25-area16-s11.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "11. 열린 질문" 절을 옮겼다 (실행 2026-09-25-40)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-103]: Han, L., Ding, J., Liu, S., & Meng, M.(Sensors 25(6) 1783, doi:10.3390/s25061783), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-10-10
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-10
[^ref-216]: ROS Navigation (ros-navigation/navigation2 GitHub), nav2_docking — README (Open Navigation's Nav2 Docking Framework), 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-10-10
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-10-10
[^ref-530]: Computers & Industrial Engineering 게재 논문(저자 미확인), Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach, 2024-08, https://www.sciencedirect.com/science/article/pii/S0360835224006314, 접근일 2026-09-25 (원문 미열람)
[^ref-531]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-533]: Chen, W., Gong, Y., Chen, Q., & Wang, H., Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse, 2024-01, https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770, 접근일 2026-09-25 (원문 미열람)
[^ref-534]: Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D., Scheduling heterogeneous multi-load AGVs with battery constraints, 2021-12, https://www.sciencedirect.com/science/article/pii/S0305054821002586, 접근일 2026-09-25 (원문 미열람)
[^ref-536]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-10-10
```

### docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md

```markdown
---
title: "28. 공용 자원·충전·에너지 최적화"
type: area
category: "G. 계획·최적화"
area_no: 28
related_areas: [5, 18, 22, 25, 27, 34, 35, 47]
tags: [충전 상태, 충전 임계값, 뮤텍스 그룹, 승강기 세션, VDA 5050, Open-RMF]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-031, ref-039, ref-051, ref-060, ref-079, ref-098, ref-103, ref-104, ref-105, ref-109, ref-146, ref-216, ref-219, ref-228, ref-284, ref-286, ref-312, ref-321, ref-377, ref-530, ref-531, ref-532, ref-533, ref-534, ref-535, ref-536, ref-537, ref-538]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [G. 계획·최적화](index.md) › 28. 공용 자원·충전·에너지 최적화

# 28. 공용 자원·충전·에너지 최적화

!!! info "소속 대분류"
    [G. 계획·최적화](index.md) — 핵심 질문:
    누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

로봇마다 같은 충전 임계값(VDA 5050 의 criticalLowChargingLevel, Open-RMF 의 recharge_threshold)으로만 충전을 시작하면 충전 수요가 겹칠 수 있으므로, 충전소 대기를 반영한 충전 시점·충전기 선택, 공유 충전기의 우선 충전 정책, 충전기·승강기 점유의 예약·세션 관리를 조율 계층이 함께 맡아야 할 것으로 보인다. [추정][^ref-228][^ref-105][^ref-530][^ref-531][^ref-533][^ref-312]

공용 자원의 대기는 곧 처리 시간 손실로 나타난다. 고밀도 병원 환경의 약품 배송 로봇 연구는 승강기 가동률이 높을수록 배송 실패가 많고 배송 시간이 길었다고 보고했다(병원 사례이며 물류센터 적용은 미확인). [사실][^ref-060] 다층 호텔 배송 경로 계획 연구는 고객 노드 60개 시나리오에서 승강기 운행 시간을 40초에서 100초로 늘리면 총 이동 시간이 약 225초에서 500초로 거의 두 배가 된다고 보고했다(호텔 사례이며 물류센터 적용은 미확인). [사실][^ref-103]

충전 방식과 정책도 처리량과 비용을 바꾼다. Zou 외(2018)는 로봇 이동형 풀필먼트 시스템에서 유도 충전이 회수 처리 시간에서 가장 좋았고, 배터리 비용이 낮으면 배터리 교환이 플러그인 충전보다 싸다고 보고했다. [사실][^ref-098] Chen 외(2024)는 자가 등반 로봇 창고에서 우선 충전 정책이 전용 충전 정책보다 비용 효율적이라고 보고했다. [사실][^ref-533]

## 4. 핵심 개념과 용어

앞 절의 문제를 다루려면 배터리 상태와 공용 자원 점유를 표현하는 용어가 먼저 필요하다.

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area16-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹 → 출하

**시나리오:** 피킹 성수기에 충전 요청과 층간 출하 운반이 겹칠 때

다음은 설명을 위한 가상의 시나리오이다. 여러 제조사 로봇이 한 다층 물류센터에서 피킹 화물을 다른 층 출하 구역으로 옮기는 중에 충전 수요와 승강기 호출이 몰리는 상황을 가정한다.

| 항목 | 내용 |
|---|---|
| 시작 조건 | 로봇이 일련의 작업을 마칠 충전량이 부족하면 Open-RMF 작업 계획기가 충전 작업을 일정에 끼워 넣는다. [사실][^ref-104] 같은 시간대에 피킹을 마친 화물의 층간 운반 요청이 이어진다(가정). |
| 작업 대상 | 피킹을 마친 출하 대상 화물과 이를 실은 로봇이며, 충전기·승강기·대기 위치는 여러 로봇이 나눠 쓰는 공용 자원이다(가정). |
| 수행 자원 | 과충전 보호, 충전기와의 통신·정밀 도킹, 승강기 운행·설비 안전 제어는 로봇·충전 설비·승강기 쪽이 맡고, ROP 는 충전 시작·중지 요청, 상태 확인, 승강기 세션 요청과 모드 확인을 담당하는 것으로 보인다. [추정][^ref-031][^ref-216][^ref-284] |
| 제약 | 팩트시트의 임계 저충전 수준 이하에서는 관제가 충전소로 가는 주문만 보내야 한다. [사실][^ref-228] 승강기가 세션 단위로 한 요청자에게 점유되므로, 여러 제조사 로봇의 호출을 세션 순서·목적층 묶음으로 배분하지 않으면 층간 대기가 출하 마감을 위협할 수 있을 것으로 보인다. [추정][^ref-312][^ref-286][^ref-103] |
| 완료·인계 | 로봇 쪽 도킹 프레임워크(연계 대상)는 도킹 뒤 충전 시작 여부(isCharging)를 확인하는 함수를 둔다. [사실][^ref-216] 승강기 이용이 끝나면 세션 종료 요청을 보낼 때까지 제어권이 그 세션에 남는다. [사실][^ref-286] |
| 예외·성과 | VDA 5050 은 충전 주문이 운반 주문을 중단시킬 수 있다고 적는다. [사실][^ref-031] 여러 로봇이 비슷한 시각에 충전 하한에 닿아 충전기 대기열이 생기면 가용 로봇 수가 줄 수 있으므로, 주문이 적은 시간대의 기회 충전이나 충전 요청을 작업 배정과 함께 계획하는 방식이 처리량 손실을 줄이는 수단이 될 것으로 보인다. [추정][^ref-534][^ref-531][^ref-031] |

이 시나리오에서 이 영역이 관여하는 곳은 시작 조건(충전 작업을 언제 넣을지), 제약(충전 하한과 승강기 점유), 예외·성과(충전으로 빠지는 가용 로봇과 층간 대기)다. 화물의 인계 확인 자체는 다른 영역이 다룬다(가정).

실제 물류센터에서 충전 대기와 승강기 대기가 처리량을 얼마나 줄이는지는 이번 조사에서 확인되지 않았으며, [열린 질문](../../open-questions.md)의 oq-010 으로 남겨 둔다.

## 6. 대표 접근법과 기술

Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다. [사실][^ref-104][^ref-536][^ref-312]

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area16-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

VDA 5050 은 충전을 동작과 배터리 선언·상태 필드로 표현하고, Open-RMF 는 충전 설정·작업 계획기·교통 그래프·승강기 메시지로 공용 자원을 다룬다. [사실][^ref-031][^ref-105] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area16-s7.md)에 있다.

## 8. 대표 연구와 자료

이 절은 충전 방식·정책의 처리량·비용 효과를 대기행렬로 분석한 창고 연구, 충전을 작업 배정·순서와 함께 푸는 최적화 연구, 승강기를 층간 병목으로 다룬 배송 로봇 연구로 나누어 정리한다.

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료](../../topics/2026/2026-09-25-area16-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP 가 직접 맡을 범위는 여러 제조사 로봇에 걸친 충전기·승강기·통로 구간·대기 위치의 예약과 배분, 충전 시점과 충전 목표 결정, 배터리 상태를 반영한 작업 배정 입력인 것으로 보인다. [추정][^ref-031][^ref-104][^ref-536][^ref-312]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 충전 시점·충전 목표 결정, 충전 시작·중지 요청, 배터리 상태 확인과 작업 배정 반영 | 과충전 보호, 충전기와의 통신·정밀 도킹, 배터리 관리 장치 |
| 시설·설비 제어 | 충전기·승강기·통로 구간·대기 위치의 예약과 배분, 승강기 세션 요청과 모드 확인 | 승강기 운행·설비 안전 제어 |

이 직접 범위는 VDA 5050 이 관제의 에너지 관리로 두고 Open-RMF 가 충전 작업 삽입·뮤텍스 그룹·승강기 세션으로 다루는 층위에 해당하는 것으로 보인다. [추정][^ref-031][^ref-104][^ref-536][^ref-312] 과충전 보호는 VDA 5050 이 이동로봇의 책임으로 명시한다. [사실][^ref-031] 정밀 도킹·충전 확인은 로봇 쪽 프레임워크가, 승강기 동작을 방해하는 요청의 차단은 승강기 어댑터가 맡으므로, ROP 는 요청과 상태 확인까지를 담당하는 연계 구조로 보인다. [추정][^ref-216][^ref-284] 경계의 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 충전과 공용 자원 점유를 매개로 배정·교통·설비 연동·설비 계획·능력 모델·상태 모델·시뮬레이션·학습 영역과 이어지는 것으로 보인다. [추정][^ref-534][^ref-536][^ref-312]

- [25. 작업 배정 — MRTA](task-allocation-mrta.md) — 운반 요청과 충전 요청을 함께 배정·순서화하는 연구가 두 영역을 잇는다. [추정][^ref-534]
- [27. 다중 로봇 경로·교통 관리 — MAPF](multi-robot-path-and-traffic-management-mapf.md) — 뮤텍스 그룹·대기 지점이 통로 구간 점유와 교통 조율을 공유한다. [추정][^ref-536]
- [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md) — 승강기 세션 요청·상태 확인이 설비 연동 인터페이스 위에서 이루어진다. [추정][^ref-312]
- [35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md) — 충전기 대수 결정과 창고 충전소 배치 최적화(Stark 외 2024)가 설비 계획으로 이어진다. [추정][^ref-533][^ref-109]
- [5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md) — 팩트시트의 충전 설정(batteryCharging)이 로봇 선언의 일부다. [추정][^ref-228]
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 현재 배터리 상태(충전 상태·충전 중 여부)를 표현한다. [추정][^ref-051]
- [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md) — 충전소 배치·충전 정책을 가정해 미래를 실험하는 시뮬레이션이 이어진다(현재 상태 표현과 구분). [추정][^ref-532]
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 강화학습 기반 충전소 선택·충전 시간 결정이 이 영역에 적용되는 연구 방법이다. [추정][^ref-531]

## 11. 열린 질문

충전·대기 시간을 성과 지표에서 어떻게 분류할지, 물류센터에서 충전·승강기 병목이 얼마나 되는지, 제조사가 다른 로봇이 충전기·승강기를 어떤 규칙으로 나눠 쓸지가 아직 확인되지 않았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 열린 질문](../../topics/2026/2026-09-25-area16-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) — 섹션 3~11 신규 작성(트랙 반영 제안 4건 반영, 1차 수정 지시 13건 이행), 2차 수정: 4·8절 연결 문장 태그 제거, 5절 조사 한계 문장 태그·각주 제거와 oq-010 연결, 6절 첫 문장을 출처 범위로 좁힘 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area16-s6.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장을 출처 범위(충전 작업 삽입·뮤텍스 그룹·승강기 세션)로 좁혔다 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료](../../topics/2026/2026-09-25-area16-s8.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: 첫 문장 태그 제거, 병원·호텔 연구 문구를 연관 관계로 고침, ref-535 제목 원문 복원 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area16-s7.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다(ref-536·ref-538 링크는 id 표기). 2차 수정: batteryCharging 행의 계획 입력 해석을 [추정]으로 분리 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 열린 질문](../../topics/2026/2026-09-25-area16-s11.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "11. 열린 질문" 절을 옮겼다 (실행 2026-09-25-40)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-060]: Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026, https://doi.org/10.1177/20552076261437181, 접근일 2026-09-25 (원문 미열람)
[^ref-098]: Zou, B., Gong, Y., de Koster, R., & Xu, X., Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system, 2018, https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901, 접근일 2026-09-25 (원문 미열람)
[^ref-103]: PMC 게재 논문(저자 미확인), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-25 (원문 미열람)
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-109]: Stark, H.-G. 외, A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse, 2024-06, https://arxiv.org/abs/2406.17003, 접근일 2026-09-25 (원문 미열람)
[^ref-216]: ROS Navigation (ros-navigation/navigation2 GitHub), nav2_docking — README (Open Navigation's Nav2 Docking Framework), 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25
[^ref-530]: Computers & Industrial Engineering 게재 논문(저자 미확인), Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach, 2024-08, https://www.sciencedirect.com/science/article/pii/S0360835224006314, 접근일 2026-09-25 (원문 미열람)
[^ref-531]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-532]: Ma, N., Zhou, C., & Stephen, A., Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals, 2020, https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X, 접근일 2026-09-25 (원문 미열람)
[^ref-533]: Chen, W., Gong, Y., Chen, Q., & Wang, H., Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse, 2024-01, https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770, 접근일 2026-09-25 (원문 미열람)
[^ref-534]: Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D., Scheduling heterogeneous multi-load AGVs with battery constraints, 2021-12, https://www.sciencedirect.com/science/article/pii/S0305054821002586, 접근일 2026-09-25 (원문 미열람)
[^ref-536]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-09-25
```

### runs/2026-10-10-05/pages/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md

```markdown
---
title: "충전 하한과 충전소 지정, 승강기 세션 점유는 무엇이 확인됐는가"
type: topic
category: "G. 계획·최적화"
primary_area_no: 28
related_areas: [5, 15, 22, 27, 57]
tags: [충전 하한, is_charger, 승강기 세션, 공용 충전기, 배터리 열화, Open-RMF]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-031, ref-039, ref-105, ref-286, ref-312, ref-403, ref-536, ref-1543, ref-1544, ref-1545]
last_run: 2026-10-10
version: 1
---

[홈](../../index.md) › [주제](../index.md) › 충전 하한과 충전소 지정, 승강기 세션 점유는 무엇이 확인됐는가

# 충전 하한과 충전소 지정, 승강기 세션 점유는 무엇이 확인됐는가

**주 연구영역:** [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) · **관련 영역:** [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) · **실행:** 2026-10-10-05

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- VDA 5050 팩트시트의 충전 수준은 백분율 선언값이고 Open-RMF 설정의 recharge_threshold 는 0~1 비율의 운행 하한이며, 현재 Open-RMF 구현은 충전소 경유점을 is_charger 로 지정한다. [사실][^ref-031][^ref-105][^ref-1543]
- 이 위키는 ROP 가 충전 하한·충전 목표·충전소 지정을 제조사 선언과 별도의 운영 정책 항목으로 기록하고, 기대는 Open-RMF 기능의 적용 판을 함께 남기는 편이 좋다고 본다. [의견][^ref-031][^ref-105][^ref-1545]
- 두 충전 값의 우선순위 규칙은 확인한 원문 범위에서 찾지 못했고, 여러 플릿의 승강기 배분 규칙과 공용 충전기 열화 최적화의 현장 검증도 아직 확인되지 않았다. [추정][^ref-031][^ref-105][^ref-403]

## 2. 배경

로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]

이 글은 [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md)의 위 핵심 질문 아래 남아 있던 열린 질문 oq-066·oq-067·oq-068·oq-069 와, 세부영역 페이지의 두 문장(충전 하한 아래 주문 제한을 의무로 적은 문장, 충전소 속성을 두고 문서가 어긋난다고 적은 문장)을 갱신 실행 2026-10-10-05 에서 다시 확인한 결과다. 조사는 외부 조사 메모를 공식 저장소·논문 원문과 대조한 것이며 한국 자료는 포함되지 않았다.

## 3. 본문

### 충전 하한: 제조사 선언값과 운영 설정

VDA 5050 3.0.0 판(발행일 미확인)의 팩트시트 batteryCharging 객체는 임계 충전 수준(criticalLowChargingLevel)·최대 희망 충전 수준·최소 희망 충전 수준을 백분율로, 최소 충전 시간을 초로 선언하는 네 필드로 이루어진다. [사실][^ref-031] 명세는 임계 충전 수준 이하에서 관제가 충전소로 가는 주문만 보내는 것을 의무가 아닌 권고 표현으로 적는다. [사실][^ref-031] 이 위키는 이 값을 의무 문구나 모든 로봇에 공통인 충전 시작 비율로 옮기지 않고, 제조사가 로봇별로 선언하는 값으로 다뤄야 한다고 본다. [의견][^ref-031]

Open-RMF fleet_adapter_template 의 설정 예시는 recharge_threshold 0.10 을 그 아래로는 로봇이 운행하지 않는 수준으로, recharge_soc 1.0 을 충전 작업에서 채울 목표 수준으로 두며, 두 값은 권장값이 아닌 템플릿 예시값이다. [사실][^ref-105] 이 위키는 두 체계를 대조할 때 단위를 먼저 맞추고, 관제의 주문 제한 기준인 VDA 의 임계 수준과 운행 하한인 Open-RMF 값을 구분해 운행 하한·충전 시작 판단·충전 목표를 별도 정책 항목으로 기록하는 편이 좋다고 본다. [의견][^ref-031][^ref-105] 두 값 가운데 무엇을 자동으로 우선하는지에 관한 공통 조정 규칙은 확인한 두 원문에 없었으며, Open-RMF 의 다른 구성요소와 VDA 5050 의 다른 절은 조사하지 않았다. [추정][^ref-031][^ref-105]

### 충전소 경유점 지정: 문서와 구현

Open-RMF 지원 작업 문서는 충전소를 is_parking_spot 으로 설정한다고 적지만, 현재 구현의 그래프 API 와 rmf_fleet_adapter 2.14.0 파서는 주차 지점과 충전 지점을 별도 속성으로 두고 충전소를 is_charger 로 지정한다. [사실][^ref-039][^ref-536][^ref-1543] 그래프 API 는 충전 지점을 배터리 충전 수준이 임계값 아래로 떨어진 로봇이 보내지는 곳으로, 주차 지점을 비상 경보 때 로봇이 스스로 주차하는 곳으로 설명한다. [사실][^ref-536] 두 구현 자료는 같은 프로젝트의 것이라 독립 교차 확인은 아니다. 이 위키는 구현 기준으로 충전소 지정을 is_charger 로 보며, is_parking_spot 만 지정한 경유점을 충전소와 같은 뜻으로 취급하지 않는 것이 맞다고 본다. [의견][^ref-536][^ref-1543]

### 승강기 세션 메시지의 범위

Open-RMF 의 승강기 요청 메시지는 승강기 이름·요청 시각·세션 id·요청 유형(세션 종료·AGV 모드·사람 모드)·목적층·문 상태 필드로 이루어지고, 상태 메시지는 세션 종료 요청 때까지 제어권을 받은 세션 id 를 보고한다. [사실][^ref-312][^ref-286] 두 메시지에는 최대 점유 시간, 예약 시간창, 여러 요청의 목적층 묶음을 지정하는 필드가 없다. [사실][^ref-312][^ref-286] 이 위키는 세션 점유·종료 인터페이스가 공개돼 있다는 사실과 공정한 대기열·묶음 운행 같은 배분 정책이 정의돼 있다는 주장을 구별해야 한다고 보며, 메시지 정의만 본 결론이므로 승강기 감독 등 다른 구성요소에 타임아웃이나 대기열 구현이 없다는 뜻으로 넓히지 않는다. [의견][^ref-312][^ref-286]

### Open-RMF 충전·뮤텍스 기능의 판 기록

rmf_fleet_adapter 변경 이력에는 2.12.0(2026-02-23)에 충전 대기 단계 완료 발행과 다음 작업에 충전량이 모자라면 충전기로 복귀하는 변경이, 2.13.0(2026-06-15)에 뮤텍스 잠금·해제 실행에서 생길 수 있는 교착 수정이 기록돼 있다(최신 판 2.14.0 은 2026-09-26). [사실][^ref-1545] 이 위키는 충전 작업 삽입·뮤텍스 그룹을 인용할 때 적용 판과 이 수정의 포함 여부를 함께 적고, 이전 판이 모든 조건에서 교착 없이 동작했다는 근거로 쓰지 않아야 한다고 본다. 변경 이력은 수정이 있었다는 것만 보여 줄 뿐 이전 판 결함의 범위를 정량화하지 않는다. [의견][^ref-1545]

### 공용 충전기와 배터리 열화를 함께 푸는 연구

Li 외(2026-03-24, arXiv v1 프리프린트, 동료심사 미확인)는 작업 배정·서비스 순서·선택적 충전 결정·충전 방식 선택·공용 충전기 접근을 하나의 혼합 정수 계획(Mixed Integer Linear Programming, MILP)으로 함께 표현하고, 총 배터리 열화·충전기 대기·납기 지연·로봇 사이 열화 불균형을 함께 줄이는 목적함수를 둔다. [사실][^ref-403] 공용 충전기 제약은 같은 충전기의 서로 다른 충전 세션 쌍마다 순서 변수를 두어 충전 구간이 겹치지 않게 하며, 세션 집합이 모든 로봇의 세션을 포함하도록 정의돼 있어 같은 로봇의 세션 쌍도 여기에 든다(논문이 따로 명시한 문장은 아니다). [사실][^ref-403] 결과 수치는 4절 사례에 적는다.

### 물류 작업과 에너지 공급을 함께 계획하는 후보 자료

Yang 외(2026-07-27, Processes)는 냉동 컨테이너 온도 제약 아래 항만 무인운반차(Automated Guided Vehicle, AGV)의 작업 스케줄링·충전을 태양광·풍력·에너지 저장 장치(Energy Storage System, ESS)를 갖춘 항만 마이크로그리드 운영과 결합해 운영비를 최소화하는 2단계 프레임워크를 제시한 것으로 초록에 소개된다(원문 미열람). [추정][^ref-1544] 이 위키는 이 자료를 물류 작업과 에너지 공급을 함께 계획하는 충전 연구의 후보로만 두며, 원문을 열지 못했으므로 비용 절감 수치나 국내 물류센터 적용 근거로 쓰지 않는다. [의견][^ref-1544]

## 4. 현장 시나리오

**현장 유형:** 물류창고

**사례:** 가상 창고에서 로봇 4대가 공용 충전기 2대를 나눠 쓰며 작업 40건을 처리(수치 실험이며 실제 배치 아님)

다음은 Li 외(2026, 프리프린트)의 대표 수치 실험을 여섯 항목으로 옮긴 것이며, 실제 현장 사례가 아니다.

| 항목 | 내용 |
|---|---|
| 시작 조건 | 작업 40건의 배정·서비스 순서와 선택적 충전 결정을 함께 정하는 계획 문제가 주어진다. [사실][^ref-403] |
| 작업 대상 | 100×50 m 가상 창고의 작업 40건과 공용 충전기 2대다. [사실][^ref-403] |
| 수행 자원 | 동종 로봇 4대가 표준·고속 두 충전 방식 가운데 하나를 골라 충전한다. [사실][^ref-403] |
| 제약 | 같은 충전기에서 충전 세션이 서로 겹치지 않아야 한다. [사실][^ref-403] |
| 완료·인계 | 미확인 |
| 예외·성과 | 기여 요약의 규칙 기반 대비 최대 54% 열화 감소는 대표 사례 하나(로봇 4·작업 40·충전기 2)의 예시적 기대 평균(총 열화 0.214→0.098)으로 보고된 값이다. [사실][^ref-403] 실패 시 누가 복구하는지는 미확인이다. |

이 사례에서 이 영역이 관여하는 곳은 제약(공용 충전기 비중첩)과 예외·성과(열화·충전기 대기)다. 이 위키는 열화를 축약 대리 모형으로 표현한 이 예시값을 현장 배터리 수명 개선의 검증값으로 인용하지 않는다. [의견][^ref-403]

## 5. ROP 관점의 시사점

**직접 범위:**

- 이 위키는 ROP 가 제조사 선언(임계 충전 수준)과 자체 운영 설정(운행 하한·충전 목표)을 단위를 맞춰 따로 기록하고, 충전소 지정은 구현 기준(is_charger)으로 확인하는 편이 좋다고 본다. [의견][^ref-031][^ref-105][^ref-1543]
- 승강기 세션 순서·점유 한도 같은 배분 규칙은 메시지 정의에 없으므로, 이 위키는 그 규칙을 어디서 정할지가 확인할 과제로 남는다고 본다. [의견][^ref-312][^ref-286]

**연계 범위:**

- 승강기 운행과 설비 안전 제어는 분류 원문 19장의 시설·설비 제어 경계에 속하는 연계 대상이며, 이 위키는 ROP 가 세션 요청과 상태 확인까지만 맡는다고 본다. [의견][^ref-312]
- 항만 마이크로그리드(태양광·풍력·ESS) 운영은 ROP 직접 범위가 아닌 에너지 설비 쪽 연계 대상이다. [의견][^ref-1544]

## 6. 연결되는 연구영역

- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 주 연구영역. 충전 하한·충전소·승강기 점유·공용 충전기 계획을 다룬다.
- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — 팩트시트의 batteryCharging 객체가 충전 수준을 로봇 선언으로 담는다. [사실][^ref-031]
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md) — 충전 지점·주차 지점이 교통 그래프 경유점 속성으로 정의된다. [사실][^ref-536]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 승강기 요청·상태 메시지가 설비 연동 인터페이스다. [사실][^ref-312][^ref-286]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 뮤텍스 잠금·해제 교착 수정이 통로 구간 점유 조율과 이어질 것으로 보인다. [추정][^ref-1545]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 배터리 열화 관리와 플릿 소프트웨어 판 기록이 수명주기 관리와 이어질 것으로 보인다. [추정][^ref-403][^ref-1545]

## 7. 열린 질문

- **oq-069** (상태: 해결 · 실행 2026-10-10-05) 출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot(지원 작업 문서)과 is_charger(교통 편집기 문서·데모 README) 가운데 어느 속성으로 하는가? — 답은 3절 "충전소 경유점 지정: 문서와 구현"에 있다.
- **oq-066**·**oq-067**·**oq-068** (상태: 열림) — 3절에 부분 근거만 있다.
- 새 질문 4건(공용 충전기 예약 초과 조정, SOC 추정 오차를 반영한 운영 하한 여유 검증, 열화 최적화 결과의 실물 재현 자료, 승강기 운행 시간 민감도와 실제 대기열의 관계)은 [열린 질문](../../open-questions.md)에 등록한다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-039]: Open Robotics, Currently supported Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_types.html, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-10
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-10-10
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-10-10
[^ref-403]: Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03-24, https://arxiv.org/abs/2603.22731, 접근일 2026-10-10
[^ref-536]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-10-10
[^ref-1543]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp (2.14.0), 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp, 접근일 2026-10-10
[^ref-1544]: Song Yang, Sichen Yue, Xiao Wang, Kaiyu Wang, Xin Tian, Xiao Wang (Processes, MDPI), A Two-Stage Logistics–Energy Coordinated Optimization Framework for AGV Scheduling and Charging Under Reefer Container Temperature Constraints, 2026-07-27, https://www.mdpi.com/2227-9717/14/15/2424, 접근일 2026-10-10 (원문 미열람)
[^ref-1545]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0), 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-10

## 9. 검증 노트

- 판정: 1차 조건부 승인 / 2차 대기
- 확인·미확인: 확인 27건 · 미확인 0건 · 교차 확인 0건
- 강등된 주장: 없음
- 검증자 주의: 판정: 조건부 승인. 확인 27건, 미확인 0건, 교차 확인 0건. 강등: 없음. 원문 미열람 출처: ref-1544(Yang 외, Crossref 초록만 확인). 주의: 이번 브리프는 외부 AI 조사 메모를 바꾼 것이라 이 실행 안의 검색 기록이 없고, 한국 자료는 없다. VDA 5050·Open-RMF 출처는 모두 같은 발행 주체나 같은 프로젝트의 자료라 독립 교차 확인으로 세지 않았다. VDA 5050 3.0.0 명세와 factsheet.schema(ref-228)는 모두 임계 충전 수준 이하 주문 제한을 권고(should)로 적으므로, 5절 제약 행의 '보내야 한다'는 권고 표현으로 정정한다. 호텔 연구(ref-103)는 이번 실행에서 원문을 처음 열었고, 원문 자체가 'nearly doubles'(225→500 s)라고 쓴다. Li 외(ref-403)의 최대 54% 열화 감소는 프리프린트 속 대표 사례 하나의 예시값이다. oq-069 해결 인정(f8·f9): 현재 구현은 충전소를 is_charger 로 지정하고, 지원 작업 문서(ref-039)는 아직 is_parking_spot 으로 적고 있어 두 서술을 함께 싣는다. oq-066·oq-067·oq-068 은 부분 근거만 있어 열린 질문으로 남긴다. 트랙 반영 제안 4건(IDTA 02047·배터리 여권·rmf_traffic 문·승강기 표현)은 이번 브리프가 조사하지 않아 반영하지 않았다. ref-1545 는 같은 날 실행 2026-10-10-03·04 에 등록된 변경 이력 출처(ref-1487·ref-1513)와 URL 이 같아 기존 id 로 합친다. 정정 요청(corr) 없음.
- 신뢰도: medium

## 10. 이력

| 날짜 | 실행 id | 변경 | 버전 |
|---|---|---|---|
| 2026-10-10 | 2026-10-10-05 | 신규 작성 | 1 |
```

### runs/2026-10-10-05/pages/topics/2026/2026-09-25-area16-s6.md

```markdown
---
title: "28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술"
type: topic
category: "G. 계획·최적화"
primary_area_no: 28
related_areas: [5, 18, 22, 25, 27, 34, 35, 47]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-10-10
sources: [ref-039, ref-079, ref-104, ref-105, ref-216, ref-219, ref-286, ref-312, ref-377, ref-530, ref-531, ref-532, ref-534, ref-536, ref-537, ref-538]
last_run: 2026-09-25
version: 2
split_from: docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#6
---

[홈](../../index.md) › [주제](../index.md) › 28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술

# 28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 1 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다. [사실][^ref-104][^ref-536][^ref-312]
- 이 페이지는 [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다. [사실][^ref-104][^ref-536][^ref-312]

### 임계값 기반 충전 작업 삽입

Open-RMF 에서 충전 작업은 플릿 어댑터가 스스로 만드는 작업이며, 로봇이 일련의 작업을 마칠 충전량이 부족하면 작업 계획기가 충전(ChargeBattery) 작업을 일정에 끼워 넣고, 현재는 로봇마다 전용 충전 위치가 있다고 가정한다. [사실][^ref-039][^ref-104] 작업 계획기는 충전소로 돌아갈 초기 충전량조차 없거나 요청을 감당할 배터리 용량이 없는 경우를 오류로 구분하고, 낮은 충전 상태를 이차항으로 강하게 벌점하는 배터리 우선 비용 설정을 둔다. [사실][^ref-377] 플릿 어댑터 설정은 배터리 전압·용량·충전 전류, 주변·도구 장치 소비 전력, 배터리 소모 반영 여부, 작업 종료 후 동작(park·charge·nothing), 로봇별 전용 충전기를 둔다(충전 전류 5.0 A 등 수치는 템플릿 예시값). [사실][^ref-105]

### 공용 자원의 상호 배제·세션·예약

Open-RMF 교통 그래프는 경유점·차선을 뮤텍스 그룹에 넣어 한 번에 한 로봇만 점유하게 할 수 있다(실제 동작 검증은 미확인). [사실][^ref-536] 승강기는 요청자별 세션 id 로 점유되고, AGV 모드에서는 승강기가 멈추면 문이 계속 열려 있다. [사실][^ref-312][^ref-286] 실험적 라이브러리 rmf_reservation 은 로봇이 충전기 같은 자원을 주어진 시간 범위 안에서 정해진 시간 동안 쓰겠다고 요청하면 해법기가 로봇을 자원에 배정하는 제약 자원 스케줄링을 제공한다고 소개되며, 배포판 포함 여부는 미확인이다. [사실][^ref-538] 플릿 어댑터의 주차 예약 시스템 사용은 기본값이 꺼짐이지만 켜기를 권장한다. [사실][^ref-537]

### 충전 시점·순서·충전기 선택 최적화

다중 AGV 충전 순서 최적화 연구(2024)는 도착 시 충전소가 사용 중일 확률과 대기 확률을 충전소마다 확률 변수로 두고 총 주행 시간 기댓값을 최소화하는 혼합 정수 선형 계획을 세웠으며, 허용 최대치까지 완전 충전하는 것이 최적이라고 보고했다. [사실][^ref-530] Dang 외(2021)는 운반 요청과 충전 요청을 함께 배정·순서화하고 임계 배터리 수준을 지키는 부분 충전 시간을 정하는 방법으로 현행 대비 비용을 약 20~50% 줄였다고 보고했다(저자 보고). [사실][^ref-534] 근접 정책 최적화(Proximal Policy Optimization, PPO) 기반 강화학습 프리프린트는 확률적 주문 도착 하에서 충전소 대기 예상 시간을 반영해 충전소 선택과 충전 시간을 학습하며, 고정 규칙 휴리스틱이 동적 환경에서 비효율적이라고 지적한다(프리프린트, 저자 보고). [사실][^ref-531] 이 학습 기반 결정은 [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)의 연구 방법을 이 영역에 적용한 사례다. [추정][^ref-531] Ma 외(2020)는 컨테이너 터미널 시뮬레이션에서 분산형 충전소 배치와 점진적 재충전 정책이 좋은 성능을 낸다고 보고했다(항만 사례이며 물류센터 적용은 미확인). [사실][^ref-532]

### 충전소 위치 정보의 출처

Open-RMF 에서 충전기 위치는 Traffic Editor 경유점의 is_charger 수동 주석으로 들어가 배터리가 임계값 아래로 떨어진 로봇이 그곳으로 보내지며, 로봇별 충전 경유점을 지정하지 않으면 그래프에서 가장 가까운 충전 경유점을 쓴다. [사실][^ref-079][^ref-536][^ref-537] 한편 Open-RMF 지원 작업 문서는 충전소를 is_parking_spot 으로 설정한다고 적어 is_charger 로 적는 문서와 어긋난다. [사실][^ref-039][^ref-079][^ref-104] 연계 대상인 Nav2 도킹 프레임워크는 도크 인스턴스(유형과 [x, y, θ] 위치)의 데이터베이스를 두고 충전 도크와 비충전 도크(컨베이어·팔레트 등)를 플러그인으로 구분하며 센서로 도크 자세를 보정한다. [사실][^ref-216] MiR 충전 스테이션 매뉴얼 게재본은 지도에 충전 스테이션 마커를 두고 로봇이 이를 감지해 도킹한다고 설명한다. [추정] 벤더 주장[^ref-219] 충전소 정보가 설비 위치(도크 자세)와 경로 그래프의 접근 지점(is_charger 경유점)으로 나뉘어 관리되므로, ROP 의 공용 자원 모델도 충전기 설비와 접근 경유점을 분리해 두어야 할 것으로 보인다. [추정][^ref-216][^ref-079][^ref-537]

### 2026-10-10 정정: 충전소 경유점 속성

이 절 앞부분에서 Open-RMF 지원 작업 문서가 충전소를 is_parking_spot 으로 설정한다고 적어 is_charger 로 적는 문서와 어긋난다고 쓴 문장은 다음과 같이 정리한다(실행 2026-10-10-05). Open-RMF 지원 작업 문서는 충전소를 is_parking_spot 으로 설정한다고 적지만, 현재 구현의 그래프 API 와 rmf_fleet_adapter 2.14.0 파서는 주차 지점과 충전 지점을 별도 속성으로 두고 충전소를 is_charger 로 지정한다. [사실][^ref-039][^ref-536][^ref-1543] 두 구현 자료는 같은 프로젝트의 것이라 독립 교차 확인은 아니다. 이 위키는 구현 기준으로 충전소 지정을 is_charger 로 보며, is_parking_spot 만 지정한 경유점을 충전소로 취급하지 않는 것이 맞다고 본다. [의견][^ref-536][^ref-1543] 충전 하한 값의 단위·의미 구분과 Open-RMF 기능의 판 기록은 주제 페이지 [충전 하한과 충전소 지정, 승강기 세션 점유는 무엇이 확인됐는가](2026-10-10-charging-threshold-charger-lift-evidence.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md)
- 관련 영역: [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-039]: Open Robotics, Currently supported Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_types.html, 접근일 2026-09-25
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-216]: ROS Navigation (ros-navigation/navigation2 GitHub), nav2_docking — README (Open Navigation's Nav2 Docking Framework), 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md, 접근일 2026-09-25
[^ref-219]: Mobile Industrial Robots(MiR) (ManualsLib 게재본), MiR Charge 24V Operating Manual — Setting charging station markers on the map (제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본), 미확인, https://www.manualslib.com/manual/1941068/Mir-Mir-Charge-24v.html?page=23, 접근일 2026-09-25 (원문 미열람)
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25
[^ref-377]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp, 접근일 2026-09-25
[^ref-530]: Computers & Industrial Engineering 게재 논문(저자 미확인), Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach, 2024-08, https://www.sciencedirect.com/science/article/pii/S0360835224006314, 접근일 2026-09-25 (원문 미열람)
[^ref-531]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-532]: Ma, N., Zhou, C., & Stephen, A., Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals, 2020, https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X, 접근일 2026-09-25 (원문 미열람)
[^ref-534]: Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D., Scheduling heterogeneous multi-load AGVs with battery constraints, 2021-12, https://www.sciencedirect.com/science/article/pii/S0305054821002586, 접근일 2026-09-25 (원문 미열람)
[^ref-536]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-09-25
[^ref-537]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 접근일 2026-09-25
[^ref-538]: Open Robotics (open-rmf), rmf_reservation — Experimental reservation library in rust (GitHub), 미확인, https://github.com/open-rmf/rmf_reservation, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-40 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-40 | 28. 공용 자원·충전·에너지 최적화 의 "대표 접근법과 기술" 절에서 분리 |

[^ref-1543]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp (2.14.0), 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp, 접근일 2026-10-10
```

### docs/topics/2026/2026-09-25-area16-s6.md

```markdown
---
title: "28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술"
type: topic
category: "G. 계획·최적화"
primary_area_no: 28
related_areas: [5, 18, 22, 25, 27, 34, 35, 47]
tags: [분리 페이지]
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-039, ref-079, ref-104, ref-105, ref-216, ref-219, ref-286, ref-312, ref-377, ref-530, ref-531, ref-532, ref-534, ref-536, ref-537, ref-538]
last_run: 2026-09-25
version: 1
split_from: docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#6
---

[홈](../../index.md) › [주제](../index.md) › 28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술

# 28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 1 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다. [사실][^ref-104][^ref-536][^ref-312]
- 이 페이지는 [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다. [사실][^ref-104][^ref-536][^ref-312]

### 임계값 기반 충전 작업 삽입

Open-RMF 에서 충전 작업은 플릿 어댑터가 스스로 만드는 작업이며, 로봇이 일련의 작업을 마칠 충전량이 부족하면 작업 계획기가 충전(ChargeBattery) 작업을 일정에 끼워 넣고, 현재는 로봇마다 전용 충전 위치가 있다고 가정한다. [사실][^ref-039][^ref-104] 작업 계획기는 충전소로 돌아갈 초기 충전량조차 없거나 요청을 감당할 배터리 용량이 없는 경우를 오류로 구분하고, 낮은 충전 상태를 이차항으로 강하게 벌점하는 배터리 우선 비용 설정을 둔다. [사실][^ref-377] 플릿 어댑터 설정은 배터리 전압·용량·충전 전류, 주변·도구 장치 소비 전력, 배터리 소모 반영 여부, 작업 종료 후 동작(park·charge·nothing), 로봇별 전용 충전기를 둔다(충전 전류 5.0 A 등 수치는 템플릿 예시값). [사실][^ref-105]

### 공용 자원의 상호 배제·세션·예약

Open-RMF 교통 그래프는 경유점·차선을 뮤텍스 그룹에 넣어 한 번에 한 로봇만 점유하게 할 수 있다(실제 동작 검증은 미확인). [사실][^ref-536] 승강기는 요청자별 세션 id 로 점유되고, AGV 모드에서는 승강기가 멈추면 문이 계속 열려 있다. [사실][^ref-312][^ref-286] 실험적 라이브러리 rmf_reservation 은 로봇이 충전기 같은 자원을 주어진 시간 범위 안에서 정해진 시간 동안 쓰겠다고 요청하면 해법기가 로봇을 자원에 배정하는 제약 자원 스케줄링을 제공한다고 소개되며, 배포판 포함 여부는 미확인이다. [사실][^ref-538] 플릿 어댑터의 주차 예약 시스템 사용은 기본값이 꺼짐이지만 켜기를 권장한다. [사실][^ref-537]

### 충전 시점·순서·충전기 선택 최적화

다중 AGV 충전 순서 최적화 연구(2024)는 도착 시 충전소가 사용 중일 확률과 대기 확률을 충전소마다 확률 변수로 두고 총 주행 시간 기댓값을 최소화하는 혼합 정수 선형 계획을 세웠으며, 허용 최대치까지 완전 충전하는 것이 최적이라고 보고했다. [사실][^ref-530] Dang 외(2021)는 운반 요청과 충전 요청을 함께 배정·순서화하고 임계 배터리 수준을 지키는 부분 충전 시간을 정하는 방법으로 현행 대비 비용을 약 20~50% 줄였다고 보고했다(저자 보고). [사실][^ref-534] 근접 정책 최적화(Proximal Policy Optimization, PPO) 기반 강화학습 프리프린트는 확률적 주문 도착 하에서 충전소 대기 예상 시간을 반영해 충전소 선택과 충전 시간을 학습하며, 고정 규칙 휴리스틱이 동적 환경에서 비효율적이라고 지적한다(프리프린트, 저자 보고). [사실][^ref-531] 이 학습 기반 결정은 [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)의 연구 방법을 이 영역에 적용한 사례다. [추정][^ref-531] Ma 외(2020)는 컨테이너 터미널 시뮬레이션에서 분산형 충전소 배치와 점진적 재충전 정책이 좋은 성능을 낸다고 보고했다(항만 사례이며 물류센터 적용은 미확인). [사실][^ref-532]

### 충전소 위치 정보의 출처

Open-RMF 에서 충전기 위치는 Traffic Editor 경유점의 is_charger 수동 주석으로 들어가 배터리가 임계값 아래로 떨어진 로봇이 그곳으로 보내지며, 로봇별 충전 경유점을 지정하지 않으면 그래프에서 가장 가까운 충전 경유점을 쓴다. [사실][^ref-079][^ref-536][^ref-537] 한편 Open-RMF 지원 작업 문서는 충전소를 is_parking_spot 으로 설정한다고 적어 is_charger 로 적는 문서와 어긋난다. [사실][^ref-039][^ref-079][^ref-104] 연계 대상인 Nav2 도킹 프레임워크는 도크 인스턴스(유형과 [x, y, θ] 위치)의 데이터베이스를 두고 충전 도크와 비충전 도크(컨베이어·팔레트 등)를 플러그인으로 구분하며 센서로 도크 자세를 보정한다. [사실][^ref-216] MiR 충전 스테이션 매뉴얼 게재본은 지도에 충전 스테이션 마커를 두고 로봇이 이를 감지해 도킹한다고 설명한다. [추정] 벤더 주장[^ref-219] 충전소 정보가 설비 위치(도크 자세)와 경로 그래프의 접근 지점(is_charger 경유점)으로 나뉘어 관리되므로, ROP 의 공용 자원 모델도 충전기 설비와 접근 경유점을 분리해 두어야 할 것으로 보인다. [추정][^ref-216][^ref-079][^ref-537]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md)
- 관련 영역: [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-039]: Open Robotics, Currently supported Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_types.html, 접근일 2026-09-25
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-216]: ROS Navigation (ros-navigation/navigation2 GitHub), nav2_docking — README (Open Navigation's Nav2 Docking Framework), 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md, 접근일 2026-09-25
[^ref-219]: Mobile Industrial Robots(MiR) (ManualsLib 게재본), MiR Charge 24V Operating Manual — Setting charging station markers on the map (제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본), 미확인, https://www.manualslib.com/manual/1941068/Mir-Mir-Charge-24v.html?page=23, 접근일 2026-09-25 (원문 미열람)
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25
[^ref-377]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp, 접근일 2026-09-25
[^ref-530]: Computers & Industrial Engineering 게재 논문(저자 미확인), Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach, 2024-08, https://www.sciencedirect.com/science/article/pii/S0360835224006314, 접근일 2026-09-25 (원문 미열람)
[^ref-531]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-532]: Ma, N., Zhou, C., & Stephen, A., Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals, 2020, https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X, 접근일 2026-09-25 (원문 미열람)
[^ref-534]: Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D., Scheduling heterogeneous multi-load AGVs with battery constraints, 2021-12, https://www.sciencedirect.com/science/article/pii/S0305054821002586, 접근일 2026-09-25 (원문 미열람)
[^ref-536]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-09-25
[^ref-537]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 접근일 2026-09-25
[^ref-538]: Open Robotics (open-rmf), rmf_reservation — Experimental reservation library in rust (GitHub), 미확인, https://github.com/open-rmf/rmf_reservation, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-40 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-40 | 28. 공용 자원·충전·에너지 최적화 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-10-05/pages/topics/2026/2026-10-10-area28-s11.md

```markdown
---
title: "28. 공용 자원·충전·에너지 최적화 — 열린 질문"
type: topic
category: "G. 계획·최적화"
primary_area_no: 28
related_areas: [5, 18, 22, 25, 27, 34, 35, 47]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-031, ref-039, ref-105, ref-1543, ref-1544, ref-286, ref-312, ref-536]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#11
---

[홈](../../index.md) › [주제](../index.md) › 28. 공용 자원·충전·에너지 최적화 — 열린 질문

# 28. 공용 자원·충전·에너지 최적화 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 충전·대기 시간을 성과 지표에서 어떻게 분류할지, 물류센터에서 충전·승강기 병목이 얼마나 되는지, 제조사가 다른 로봇이 충전기·승강기를 어떤 규칙으로 나눠 쓸지가 아직 확인되지 않았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

충전·대기 시간을 성과 지표에서 어떻게 분류할지, 물류센터에서 충전·승강기 병목이 얼마나 되는지, 제조사가 다른 로봇이 충전기·승강기를 어떤 규칙으로 나눠 쓸지가 아직 확인되지 않았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.


2026-10-10 갱신(실행 2026-10-10-05)에서 바뀐 열린 질문은 다음과 같다.

- **oq-069** (상태: 해결 · 실행 2026-10-10-05) 출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot(지원 작업 문서)과 is_charger(교통 편집기 문서·데모 README) 가운데 어느 속성으로 하는가? — 현재 구현의 그래프 API 와 rmf_fleet_adapter 2.14.0 파서는 충전소를 is_charger 로 지정하고, 지원 작업 문서는 여전히 is_parking_spot 으로 적는다. [사실][^ref-536][^ref-1543][^ref-039] 답은 [주제 페이지](2026-10-10-charging-threshold-charger-lift-evidence.md)에 있다.
- **oq-068** (상태: 열림) 부분 근거: 제조사 선언값은 백분율, Open-RMF 템플릿 값은 0~1 비율이며, 두 값의 우선순위 규칙은 확인한 두 원문 범위에서 찾지 못했다. [추정][^ref-031][^ref-105]
- **oq-067** (상태: 열림) 부분 근거: Open-RMF 승강기 메시지에는 최대 점유 시간·예약 시간창·다중 목적층 필드가 없으며, 다른 구성요소는 조사하지 않았다. [사실][^ref-312][^ref-286]
- **oq-066** (상태: 열림) 부분 근거: 항만 AGV 작업·충전과 마이크로그리드 운영을 결합한 연구 한 건(원문 미열람)만 후보로 찾았고, 물류센터 연구와 국내 사례는 찾지 못했다. [추정][^ref-1544]
- 새 질문(2026-10-10 등록, 번호는 열린 질문 목록에서 부여한다):
    - 공용 충전기 예약 시간이 끝났는데 로봇이 충전기 앞을 떠나지 못할 때 다음 예약의 시작을 어떻게 조정하는가?
    - 충전 상태(SOC) 추정 오차와 충전소까지의 이동·대기 에너지를 반영해 운영 하한에 더할 여유를 어떻게 검증하는가?
    - 배터리 열화 최적화 모델의 예시 결과를 실제 셀·충전기·장기 운용 데이터로 검증한 공개 재현 자료가 있는가?
    - 승강기 운행 시간 민감도와 실제 승강기 대기열·최대 점유 시간의 관계를 같은 실험에서 측정한 자료가 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-039]: Open Robotics, Currently supported Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_types.html, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-10
[^ref-1543]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp (2.14.0), 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp, 접근일 2026-10-10
[^ref-1544]: Song Yang, Sichen Yue, Xiao Wang, Kaiyu Wang, Xin Tian, Xiao Wang (Processes, MDPI), A Two-Stage Logistics–Energy Coordinated Optimization Framework for AGV Scheduling and Charging Under Reefer Container Temperature Constraints, 2026-07-27, https://www.mdpi.com/2227-9717/14/15/2424, 접근일 2026-10-10 (원문 미열람)
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-10-10
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-10-10
[^ref-536]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-05 | 28. 공용 자원·충전·에너지 최적화 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-10-05/pages/topics/2026/2026-10-10-area28-s3.md

```markdown
---
title: "28. 공용 자원·충전·에너지 최적화 — 왜 중요한가"
type: topic
category: "G. 계획·최적화"
primary_area_no: 28
related_areas: [5, 18, 22, 25, 27, 34, 35, 47]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-031, ref-060, ref-098, ref-103, ref-105, ref-228, ref-312, ref-530, ref-531, ref-533]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#3
---

[홈](../../index.md) › [주제](../index.md) › 28. 공용 자원·충전·에너지 최적화 — 왜 중요한가

# 28. 공용 자원·충전·에너지 최적화 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇마다 정해 둔 충전 하한 — VDA 5050 의 임계 충전 수준(criticalLowChargingLevel, 관제의 주문 제한 기준, 백분율)이나 Open-RMF 의 recharge_threshold(운행 하한, 0~1 비율) — 에만 맞춰 충전을 시작하면 충전 수요가 겹칠 수 있으므로, 충전소 대기를 반영한 충전 시점·충전기 선택, 공유 충전기의 우선 충전 정책, 충전기·승강기 점유의 예약·세션 관리를 조율 계층이 함께 맡아야 할 것으로 보인다. [추정][^ref-228][^ref-031][^ref-105][^ref-530][^ref-531][^ref-533][^ref-312]
- 이 페이지는 [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇마다 정해 둔 충전 하한 — VDA 5050 의 임계 충전 수준(criticalLowChargingLevel, 관제의 주문 제한 기준, 백분율)이나 Open-RMF 의 recharge_threshold(운행 하한, 0~1 비율) — 에만 맞춰 충전을 시작하면 충전 수요가 겹칠 수 있으므로, 충전소 대기를 반영한 충전 시점·충전기 선택, 공유 충전기의 우선 충전 정책, 충전기·승강기 점유의 예약·세션 관리를 조율 계층이 함께 맡아야 할 것으로 보인다. [추정][^ref-228][^ref-031][^ref-105][^ref-530][^ref-531][^ref-533][^ref-312]

공용 자원의 대기는 곧 처리 시간 손실로 나타난다. 고밀도 병원 환경의 약품 배송 로봇 연구는 승강기 가동률이 높을수록 배송 실패가 많고 배송 시간이 길었다고 보고했다(병원 사례이며 물류센터 적용은 미확인). [사실][^ref-060] Han 외(2025)의 다층 호텔 배송 경로 계획 연구는 고객 노드 60개 시나리오에서 승강기 운행 시간을 40초에서 100초로 늘리면 총 이동 시간이 약 225초에서 500초로 늘었다고 보고했다(호텔 사례이며 물류센터 적용은 미확인). [사실][^ref-103] 이 위키는 이 수치를 가정한 승강기 운행 시간을 바꾼 모델 수치 실험의 결과로 보며, 실제로 측정한 승강기 대기열 손실로 읽지 않는다. [의견][^ref-103]

충전 방식과 정책도 처리량과 비용을 바꾼다. Zou 외(2018)는 로봇 이동형 풀필먼트 시스템에서 유도 충전이 회수 처리 시간에서 가장 좋았고, 배터리 비용이 낮으면 배터리 교환이 플러그인 충전보다 싸다고 보고했다. [사실][^ref-098] Chen 외(2024)는 자가 등반 로봇 창고에서 우선 충전 정책이 전용 충전 정책보다 비용 효율적이라고 보고했다. [사실][^ref-533]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-060]: Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026, https://doi.org/10.1177/20552076261437181, 접근일 2026-09-25 (원문 미열람)
[^ref-098]: Zou, B., Gong, Y., de Koster, R., & Xu, X., Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system, 2018, https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901, 접근일 2026-09-25 (원문 미열람)
[^ref-103]: Han, L., Ding, J., Liu, S., & Meng, M.(Sensors 25(6) 1783, doi:10.3390/s25061783), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-10-10
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-10
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-10-10
[^ref-530]: Computers & Industrial Engineering 게재 논문(저자 미확인), Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach, 2024-08, https://www.sciencedirect.com/science/article/pii/S0360835224006314, 접근일 2026-09-25 (원문 미열람)
[^ref-531]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-533]: Chen, W., Gong, Y., Chen, Q., & Wang, H., Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse, 2024-01, https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-05 | 28. 공용 자원·충전·에너지 최적화 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-10-10-05/pages/topics/2026/2026-10-10-area28-s10.md

```markdown
---
title: "28. 공용 자원·충전·에너지 최적화 — 다른 연구영역과의 연결"
type: topic
category: "G. 계획·최적화"
primary_area_no: 28
related_areas: [5, 18, 22, 25, 27, 34, 35, 47]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-051, ref-109, ref-228, ref-312, ref-531, ref-532, ref-533, ref-534, ref-536]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#10
---

[홈](../../index.md) › [주제](../index.md) › 28. 공용 자원·충전·에너지 최적화 — 다른 연구영역과의 연결

# 28. 공용 자원·충전·에너지 최적화 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 충전과 공용 자원 점유를 매개로 배정·교통·설비 연동·설비 계획·능력 모델·상태 모델·시뮬레이션·학습 영역과 이어지는 것으로 보인다. [추정][^ref-534][^ref-536][^ref-312]
- 이 페이지는 [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 충전과 공용 자원 점유를 매개로 배정·교통·설비 연동·설비 계획·능력 모델·상태 모델·시뮬레이션·학습 영역과 이어지는 것으로 보인다. [추정][^ref-534][^ref-536][^ref-312]

- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 운반 요청과 충전 요청을 함께 배정·순서화하는 연구가 두 영역을 잇는다. [추정][^ref-534]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 뮤텍스 그룹·대기 지점이 통로 구간 점유와 교통 조율을 공유한다. [추정][^ref-536]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 승강기 세션 요청·상태 확인이 설비 연동 인터페이스 위에서 이루어진다. [추정][^ref-312]
- [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md) — 충전기 대수 결정과 창고 충전소 배치 최적화(Stark 외 2024)가 설비 계획으로 이어진다. [추정][^ref-533][^ref-109]
- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — 팩트시트의 충전 설정(batteryCharging)이 로봇 선언의 일부다. [추정][^ref-228]
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 현재 배터리 상태(충전 상태·충전 중 여부)를 표현한다. [추정][^ref-051]
- [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md) — 충전소 배치·충전 정책을 가정해 미래를 실험하는 시뮬레이션이 이어진다(현재 상태 표현과 구분). [추정][^ref-532]
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 강화학습 기반 충전소 선택·충전 시간 결정이 이 영역에 적용되는 연구 방법이다. [추정][^ref-531]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-109]: Stark, H.-G. 외, A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse, 2024-06, https://arxiv.org/abs/2406.17003, 접근일 2026-09-25 (원문 미열람)
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-10-10
[^ref-531]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-532]: Ma, N., Zhou, C., & Stephen, A., Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals, 2020, https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X, 접근일 2026-09-25 (원문 미열람)
[^ref-533]: Chen, W., Gong, Y., Chen, Q., & Wang, H., Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse, 2024-01, https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770, 접근일 2026-09-25 (원문 미열람)
[^ref-534]: Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D., Scheduling heterogeneous multi-load AGVs with battery constraints, 2021-12, https://www.sciencedirect.com/science/article/pii/S0305054821002586, 접근일 2026-09-25 (원문 미열람)
[^ref-536]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-05 | 28. 공용 자원·충전·에너지 최적화 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-10-10-05/pages/topics/2026/2026-10-10-area28-s7.md

```markdown
---
title: "28. 공용 자원·충전·에너지 최적화 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "G. 계획·최적화"
primary_area_no: 28
related_areas: [5, 18, 22, 25, 27, 34, 35, 47]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-031, ref-105, ref-1545, ref-286, ref-312]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#7
---

[홈](../../index.md) › [주제](../index.md) › 28. 공용 자원·충전·에너지 최적화 — 관련 표준·프레임워크·오픈소스

# 28. 공용 자원·충전·에너지 최적화 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- VDA 5050 은 충전을 동작과 배터리 선언·상태 필드로 표현하고, Open-RMF 는 충전 설정·작업 계획기·교통 그래프·승강기 메시지로 공용 자원을 다룬다. [사실][^ref-031][^ref-105] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

VDA 5050 은 충전을 동작과 배터리 선언·상태 필드로 표현하고, Open-RMF 는 충전 설정·작업 계획기·교통 그래프·승강기 메시지로 공용 자원을 다룬다. [사실][^ref-031][^ref-105] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.


Open-RMF 승강기 요청·상태 메시지는 세션 id 로 점유와 종료를 표현하지만, 최대 점유 시간·예약 시간창·여러 요청의 목적층 묶음을 지정하는 필드는 두지 않는다. [사실][^ref-312][^ref-286] 이 위키는 이를 메시지 정의 범위의 사실로만 보며, 배분 정책이나 다른 구성요소의 대기열 구현이 없다는 뜻으로 넓히지 않는다. [의견][^ref-312][^ref-286] rmf_fleet_adapter 변경 이력에는 2.12.0(2026-02-23)의 충전기 복귀 변경과 2.13.0(2026-06-15)의 뮤텍스 잠금·해제 교착 수정이 기록돼 있다. [사실][^ref-1545] 이 위키는 충전 작업 삽입·뮤텍스 그룹을 인용할 때 적용 판을 함께 적어야 한다고 본다. [의견][^ref-1545]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-10
[^ref-1545]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0), 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-10
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-10-10
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-05 | 28. 공용 자원·충전·에너지 최적화 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-10-05/pages/topics/2026/2026-10-10-area28-s6.md

```markdown
---
title: "28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술"
type: topic
category: "G. 계획·최적화"
primary_area_no: 28
related_areas: [5, 18, 22, 25, 27, 34, 35, 47]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-031, ref-039, ref-104, ref-105, ref-1543, ref-312, ref-536]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#6
---

[홈](../../index.md) › [주제](../index.md) › 28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술

# 28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다. [사실][^ref-104][^ref-536][^ref-312]
- 이 페이지는 [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다. [사실][^ref-104][^ref-536][^ref-312]


2026-10-10 갱신에서 충전소 경유점 지정과 충전 하한 값을 다시 확인했다. Open-RMF 지원 작업 문서는 충전소를 is_parking_spot 으로 설정한다고 적지만, 현재 구현의 그래프 API 와 rmf_fleet_adapter 2.14.0 파서는 주차 지점과 충전 지점을 별도 속성으로 두고 충전소를 is_charger 로 지정한다. [사실][^ref-039][^ref-536][^ref-1543] 이 위키는 구현 기준으로 충전소 지정을 is_charger 로 본다. [의견][^ref-536][^ref-1543] VDA 5050 3.0.0 판(발행일 미확인)의 임계 충전 수준은 백분율 선언값이고, Open-RMF 템플릿의 recharge_threshold 는 0~1 비율로 적힌 운행 하한 예시값이다. [사실][^ref-031][^ref-105]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-039]: Open Robotics, Currently supported Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_types.html, 접근일 2026-09-25
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-10
[^ref-1543]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp (2.14.0), 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp, 접근일 2026-10-10
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-10-10
[^ref-536]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-05 | 28. 공용 자원·충전·에너지 최적화 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-10-05/pages/topics/2026/2026-10-10-area28-s8.md

```markdown
---
title: "28. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료"
type: topic
category: "G. 계획·최적화"
primary_area_no: 28
related_areas: [5, 18, 22, 25, 27, 34, 35, 47]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-1544, ref-403]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#8
---

[홈](../../index.md) › [주제](../index.md) › 28. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료

# 28. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 절은 충전 방식·정책의 처리량·비용 효과를 대기행렬로 분석한 창고 연구, 충전을 작업 배정·순서와 함께 푸는 최적화 연구, 승강기를 층간 병목으로 다룬 배송 로봇 연구로 나누어 정리한다.
- 이 페이지는 [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 절은 충전 방식·정책의 처리량·비용 효과를 대기행렬로 분석한 창고 연구, 충전을 작업 배정·순서와 함께 푸는 최적화 연구, 승강기를 층간 병목으로 다룬 배송 로봇 연구로 나누어 정리한다.


2026-10-10 갱신에서 공용 충전기 비중첩 제약과 배터리 열화를 함께 푸는 연구로 Li 외(2026-03-24, arXiv 프리프린트, 동료심사 미확인)를 더했으며, 이 연구가 보고한 최대 54% 열화 감소는 가상 창고 대표 사례 하나의 예시적 기대 평균이다. [사실][^ref-403] 물류 작업과 에너지 공급을 함께 계획하는 항만 연구(Yang 외 2026)는 원문을 열지 못해, 이 위키는 후보 자료로만 둔다. [의견][^ref-1544] 자세한 내용은 주제 페이지 [충전 하한과 충전소 지정, 승강기 세션 점유는 무엇이 확인됐는가](2026-10-10-charging-threshold-charger-lift-evidence.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1544]: Song Yang, Sichen Yue, Xiao Wang, Kaiyu Wang, Xin Tian, Xiao Wang (Processes, MDPI), A Two-Stage Logistics–Energy Coordinated Optimization Framework for AGV Scheduling and Charging Under Reefer Container Temperature Constraints, 2026-07-27, https://www.mdpi.com/2227-9717/14/15/2424, 접근일 2026-10-10 (원문 미열람)
[^ref-403]: Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03-24, https://arxiv.org/abs/2603.22731, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-05 | 28. 공용 자원·충전·에너지 최적화 의 "대표 연구와 자료" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 28건 / 전체 1399건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-039 | Open Robotics | Currently supported Tasks - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/task_types.html | 2026-09-25 | 예 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 2026-09-25 | 예 |
| ref-060 | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026 | https://doi.org/10.1177/20552076261437181 | 2026-09-25 | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 2026-09-25 | 예 |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 2018 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 | 2026-09-25 | 아니오 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 2026-09-25 | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | https://github.com/open-rmf/rmf_demos | 2026-09-25 | 예 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 2026-09-25 | 예 |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 2024-06 | https://arxiv.org/abs/2406.17003 | 2026-09-25 | 아니오 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 2024 | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 | 2026-09-25 | 아니오 |
| ref-216 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_docking — README (Open Navigation's Nav2 Docking Framework) | 미확인 | https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md | 2026-09-25 | 예 |
| ref-219 | Mobile Industrial Robots(MiR) (ManualsLib 게재본) | MiR Charge 24V Operating Manual — Setting charging station markers on the map (제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본) | 미확인 | https://www.manualslib.com/manual/1941068/Mir-Mir-Charge-24v.html?page=23 | 2026-09-25 | 아니오 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 2026-09-25 | 예 |
| ref-284 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_lifts.html | 2026-09-25 | 예 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 2026-09-25 | 예 |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg | 2026-09-25 | 예 |
| ref-321 | Electronics(MDPI) 게재 논문(저자 미확인) | Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots | 2025 | https://doi.org/10.3390/electronics14050982 | 2026-09-25 | 아니오 |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 미확인 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp | 2026-09-25 | 예 |
| ref-530 | Computers & Industrial Engineering 게재 논문(저자 미확인) | Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach | 2024-08 | https://www.sciencedirect.com/science/article/pii/S0360835224006314 | 2026-09-25 | 아니오 |
| ref-531 | arXiv 2607.05683 저자(미확인) | Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers | 2026-07 | https://arxiv.org/abs/2607.05683 | 2026-09-25 | 아니오 |
| ref-532 | Ma, N., Zhou, C., & Stephen, A. | Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals | 2020 | https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X | 2026-09-25 | 아니오 |
| ref-533 | Chen, W., Gong, Y., Chen, Q., & Wang, H. | Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse | 2024-01 | https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770 | 2026-09-25 | 아니오 |
| ref-534 | Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D. | Scheduling heterogeneous multi-load AGVs with battery constraints | 2021-12 | https://www.sciencedirect.com/science/article/pii/S0305054821002586 | 2026-09-25 | 아니오 |
| ref-535 | 박재범, 조성준, 김준식, 유범재(전자공학회논문지 61(8)) | 배송 로봇의 다층, 다중 배송을 위한 효율적인 경로 계획 및 엘리베이터 층간 이동 시스템 | 2024 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003107904 | 2026-09-25 | 아니오 |
| ref-536 | Open Robotics (open-rmf) | rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 미확인 | https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 2026-09-25 | 예 |
| ref-537 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 미확인 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 2026-09-25 | 예 |
| ref-538 | Open Robotics (open-rmf) | rmf_reservation — Experimental reservation library in rust (GitHub) | 미확인 | https://github.com/open-rmf/rmf_reservation | 2026-09-25 | 아니오 |
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

### docs/open-questions.md (요약: 대상 영역 [28] 에 걸린 8건 / 전체 348건)

```markdown
- oq-016 [열림] 창고 이동로봇 플릿에 ISO 22400식 OEE(가용성·성능·품질)를 적용하는 합의된 정의가 있는가, 충전·대기·교통 정체 시간은 어느 손실로 분류해야 하는가? (영역 28, 39)
- oq-060 [열림] 출처 충돌: IDTA 02047 1.0 에 충전 관련 요소(ChargingTimeAsSpecified, ChargingDeviceRequirements, BatteryInformation)가 있는가? 명세 PDF 검색 요약은 있다고 전하지만, 공식 저장소 템플릿 JSON 의 잘린 열람 응답에서는 확인되지 않았다. (영역 5, 28)
- oq-065 [열림] 제조사가 다른 이동로봇이 같은 충전기를 함께 쓸 수 있게 하는 충전 커넥터·충전 통신의 공통 규격이나 공개 사례가 있는가? (영역 21, 28)
- oq-066 [열림] 물류센터 로봇의 충전 시점을 시간대별 전기 요금이나 최대 수요 전력 기준으로 계획한 연구나 국내 사례가 있는가? (영역 28, 39)
- oq-067 [열림] 여러 제조사 플릿이 한 승강기를 함께 쓸 때 세션 순서·최대 점유 시간·목적층 묶음을 정하는 배분 규칙을 공개한 표준이나 구현이 있는가? (영역 22, 28)
- oq-068 [열림] 충전 하한을 제조사가 팩트시트로 선언한 값(criticalLowChargingLevel)과 ROP 운영 설정(recharge_threshold) 가운데 어느 것으로 삼고, 둘이 다르면 어떻게 조정하는가? (영역 5, 28)
- oq-069 [열림] 출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot(지원 작업 문서)과 is_charger(교통 편집기 문서·데모 README) 가운데 어느 속성으로 하는가? (영역 15, 28)
- oq-152 [열림] Open-RMF 사용자 정의 동작이 교통 협상에서 빠지고 문·승강기 조작을 맡지 않을 때, ROP 는 그 동작의 배터리·설비 상태 같은 실행 시점 조건을 어디에서 검사하고 실패를 어떻게 복구하는가? (영역 6, 28, 29)
```
