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

### data/area_reflection_proposals.json (대상 영역 28. 공용 자원·충전·에너지 최적화 에 대한 트랙 반영 제안 4건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-09-25-45",
      "date": "2026-09-25",
      "track": "manual-capability-ontology",
      "stage": 1,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "IDTA 02047 의 충전 시간·충전 장치 요구·배터리 정보 요소가 충전기 배분·충전 시점 계획의 입력 후보가 될 수 있다는 [추정](명세 PDF 검색 요약 기준, 출처 충돌 열린 질문 참조, ref-198)을 반영 제안(실행 2026-09-25-45).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-47",
      "date": "2026-09-25",
      "track": "manual-capability-ontology",
      "stage": 1,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "IDTA 02047 의 EnergyAndCommunication/Battery 묶음과 충전 장치 요구(전압 범위·최대 전류)·배터리 정보(종류·용량·최대 충전 횟수) 요소가 충전기 배분·충전 시점 계획의 입력 후보라는 추정(명세 PDF 검색 요약 기준, ref-198)",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-53",
      "date": "2026-09-25",
      "track": "manual-capability-ontology",
      "stage": 1,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "IDTA Digital Battery Passport 계열 템플릿이 배터리 속성의 의미 식별자 원천 후보일 수 있으나 템플릿 본문과 충전 능력과의 관련성은 미확인이다 [추정][^ref-439]. 관련 트랙 질문 q4-16.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-58",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 3,
      "area_no": 28,
      "section": "6. 대표 접근법과 기술",
      "summary": "rmf_traffic 의 문·승강기 표현(차선 이벤트·경유점 승강기 안 여부)과 상호 배제 그룹(f2·f3), VDA 5050 해제 구역 접근 허가와 startCharging 의 위치(f9·f10), 공용 자원 개체가 걸친 경유점·차선·구역을 가리키는 예약 단위(추정, f15).",
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

### docs/categories/robot-ontology/robot-capability-and-task-representation.md (요약)

```markdown
# 5. 로봇 능력·작업 표현

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

능력·작업 요구·환경 조건을 공통 어휘로 표현하고 기존 표준과 맞춘다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇 능력 표현**: 이동·계단·적재·도어 조작·충전·파지·점검 같은 능력을 매개변수·입출력·전제조건·제약·실패 모드와 함께 공통 모델로 표현한다
- **작업 유형·작업 요구 표현**: 배송·운반·인계·순찰·점검·조작 같은 작업 유형과 각 작업이 요구하는 능력·조건을 능력 모델과 같은 어휘로 표현한다
- **환경 조건과 능력 대조**: 층·문·승강기·계단·충전기 같은 공간 조건을 온톨로지에 함께 담아 로봇별로 지나갈 수 있는 곳과 쓸 수 있는 시설을 판단한다
- **표현 표준 정렬**: 능력·작업 표현을 로봇 온톨로지 표준(IEEE 1872 계열), VDA 5050 팩트시트, 자산 관리 셸 같은 기존 규격과 대응시킨다
- **온톨로지 저장·질의 기반**: 온톨로지를 저장하고 질의하는 기술(그래프 데이터베이스, RDF·OWL, SPARQL, JSON 스키마)을 고르고 성능을 확인한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [4. 이기종 로봇 등록](heterogeneous-robot-registration.md), [6. 온톨로지 기반 시스템·로봇 연동](ontology-based-system-and-robot-integration.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 5번 영역 ‘로봇 능력·작업 온톨로지’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제조사별 기능·제약·장착 장비·실행 조건을 공통 모델로 표현하고, 작업 요구와 연결 [옛 분류원문]

> 옛 질문: 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

로봇이 할 수 있는 일과 작업이 요구하는 조건을 어떻게 같은 말로 표현할 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md (요약)

```markdown
# 18. 실시간 세계 상태·데이터 일관성

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

## 1. 한 줄 정의

로봇·설비·공간·물품의 현재 상태를 통합하고, 관측의 신선도·신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실시간 세계 상태 통합**: 로봇·설비·공간·물품·사람의 현재 상태를 한곳에 모으고 지연·누락·충돌·불확실성을 관리한다
- **관측 신선도·신뢰도**: 오래되거나 불확실한 관측(예를 들어 30초 전의 문 상태)을 지금의 판단에 써도 되는지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 8번 영역 ‘실시간 세계 상태·데이터 일관성’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 [옛 분류원문]

> 옛 질문: 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? [옛 분류원문]

> 옛 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [옛 분류원문]

## 2. 핵심 질문

조금 전에 받은 상태 정보를 지금의 판단에 믿고 써도 되는가? [분류원문]

> 원문 주석: 18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]
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

### docs/categories/design-and-simulation/simulation-and-predictive-digital-twin.md (요약)

```markdown
# 34. 시뮬레이션·예측용 디지털 트윈

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

물리·센서·다중 로봇 시뮬레이션과 그 자산, 운영 정책·수요 변화 예측 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시뮬레이션 엔진**: 로봇·설비·물품·사람을 물리·센서 수준에서 가상으로 재현한다(MuJoCo·Gazebo·Isaac Sim 등)
- **운영 정책·수요 변화 예측**: 배치·운영 정책·일의 양이 바뀔 때의 효과를 가상 환경에서 미리 본다
- **시뮬레이션 관측 모델**: 잡음·지연이 있는 관측을 만들어 시뮬레이션 시험이 현실의 불확실성을 반영하게 한다
- **시뮬레이션 자산 관리**: 로봇·물품·환경의 3D 모델과 물성 값을 출처·라이선스와 함께 관리해 시뮬레이션에 쓴다

이전 분류(2026-09-24)에서 이 페이지는 옛 22번 영역 ‘시뮬레이션·예측용 디지털 트윈’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 [옛 분류원문]

> 옛 질문: 성수기 주문량이 늘면 어디가 먼저 막힐까? [옛 분류원문]

> 옛 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [옛 분류원문]

## 2. 핵심 질문

현장을 바꾸기 전에 가상 환경에서 결과를 얼마나 믿을 만하게 미리 볼 수 있는가? [분류원문]

> 원문 주석: 18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]
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

### docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md (요약)

```markdown
# 47. AI·학습·적응과 모델 운영

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

AI 결과를 실행에 쓰는 기준과 불확실성, 모델 운영 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **AI 결과의 실행 사용 기준**: AI가 만든 계획·해석을 어떤 기준으로 실행에 쓸지 정하고 불확실성을 평가한다
- **모델 운영**: 모델 버전·학습 데이터·배포·성능 감시를 관리한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [44. 로봇 기반 모델·언어 모델 계획](robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](prediction-and-learning-based-optimization.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 27번 영역 ‘AI·학습·적응과 모델 운영’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 [옛 분류원문]

> 옛 질문: AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]
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

### runs/2026-10-10-04/research.md

```markdown
# 리서치 브리프 2026-10-10-04

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-04 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 27. 다중 로봇 경로·교통 관리 — MAPF |
| 대분류 | G. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 설명용 가정 시나리오뿐이며 확인된 다른 현장 유형(제조 공장 등) 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 첫 문장이 단일 로봇 계획인 SIPP를 CBS와 함께 '최적해를 보장하는 다중 로봇 탐색'으로 묶음. PIBT의 '완전·최적 아님' 명시와 마감을 목적으로 하는 정식화(MAPF-DL) 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — VDA 5050 은 main 판 기준(2026-09-25 확인)이며 3.0.0 태그의 예정 경로 공유(§6.8)·구역 요청 통신(§6.4.3) 미반영. Open-RMF 2026-09-25 이후 변경(신호등 수준 연동 수정) 미반영
- 섹션 8. 대표 연구와 자료(주제 페이지로 분리) — SILLM 이 '2024, 프리프린트'로 적혀 있고 계산 규모(10,000)와 실물 검증 규모, WPPL 비교 조건이 구분돼 있지 않음. 실행 조건을 평가한 LSMART 미수록. ref-189·ref-192·ref-195·ref-199 원문 미열람
- 섹션 11. 열린 질문 — oq-058·oq-059 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [분류원문]
2. SIPP·PIBT의 이론 보장(완전성·최적성·도달성)은 어떤 문제 설정과 그래프 조건에서 성립하며, 다중 로봇 현장 경로망에 그대로 옮길 수 있는가? (섹션 6 겨냥)
3. 좁은 통로와 이종 대형 AGV가 있는 산업 현장에 MAPF 기반 교통 관리를 적용한 공개 사례는 현장 유형·평가 방식·교착 처리를 어떻게 밝히는가? (섹션 5·6 겨냥)
4. VDA 5050 3.0.0 과 Open-RMF 의 최신 판은 교통 관리에 쓰이는 어떤 정보(예정 경로·구역 요청·신호등 수준 연동)를 바꾸거나 더했는가? (섹션 7 겨냥)
5. oq-058 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가? (섹션 8·11 겨냥)
6. oq-059 주문 납기·출하 마감 같은 업무 우선순위를 교통 협상·통로 양보의 우선권으로 옮기는 규칙을 정한 연구나 현장 기준이 있는가? (섹션 6·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Phillips·Likhachev(ICRA 2011)의 안전 구간 경로 계획(Safe Interval Path Planning, SIPP)은 동적 장애물마다 예측 궤적(predicted trajectories)이 주어졌다고 보고, 상태를 위치와 안전 구간의 쌍으로 묶어 로봇 한 대의 경로를 찾으며, 시간 차원을 더한 계획과 같은 최적성·완전성 보장을 준다고 밝힌다. | ref-195 | 아니오 | medium | 2026-10-10 | — | — |
| f2 | [추정] | SIPP의 완전성·최적성은 주어진 장애물 궤적에 대해 로봇 한 대의 시간 최소 경로를 찾는 범위의 결과이므로, 여러 로봇의 경로를 함께 정하는 다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF) 전체의 최적성 보장으로 옮길 수 없는 것으로 보인다. | ref-195, ref-192 | 아니오 | low | 2026-10-10 | — | — |
| f3 | [사실] | Bonetti 외(2026)의 관련 연구 절은 Yan·Li(2024)가 우선순위 기반 탐색(Priority Based Search, PBS)·SIPP·베지에 곡선 최적화를 결합한 3단 다중 로봇 계획기를 우선순위 탐색에 기대므로 전역 최적성을 보장하지 않는다고 평가해, SIPP가 상위 다중 로봇 조율 아래의 저수준 계획으로 쓰이는 예를 보여 준다. | ref-192 | 아니오 | medium | 2026-10-10 | — | — |
| f4 | [의견] | 기존 6절 첫 문장처럼 SIPP를 CBS와 함께 '최적해를 보장하는 다중 로봇 탐색'으로 묶기보다, SIPP는 다른 로봇의 예정 궤적 같은 동적 장애물을 피하는 단일 로봇 저수준 경로 탐색으로 분리해 소개하는 편이 정확하다고 이 위키는 본다. | ref-195, ref-192 | 아니오 | low | 2026-10-10 | — | — |
| f5 | [사실] | Okumura 외의 우선순위 상속과 되돌리기(Priority Inheritance with Backtracking, PIBT) 논문(arXiv v5 2022-06-27, Artificial Intelligence 2022 게재판, 초판 IJCAI-19)은 §2.1에서 PIBT가 MAPF에 대해 완전하지도 최적이지도 않다고 명시하고, 도달성은 모든 에이전트가 동시에 목표에 있음을 보장하지 않으므로 일반 MAPF에는 불완전하다고 설명한다. | ref-189 | 아니오 | medium | 2026-10-10 | — | — |
| f6 | [사실] | Bonetti 외 §9는 작업 갱신 같은 예측 못 한 사건과, 시간 지평이 부족해 복도 밖 구역의 시공간 충돌을 다 풀지 못할 때 교착이 생긴다고 보고, AGV 사이 선행 관계 그래프로 순환·비순환(중첩) 교착을 탐지한 뒤 관련 AGV의 경로를 갱신해 해소하는 별도 모듈을 둔다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 / 예외·성과 | — |
| f7 | [의견] | PIBT의 도달 보장은 그래프 조건과 지속형 설정을 전제로 하므로, 막다른 통로가 있는 실제 경로망에는 그 보장을 그대로 적용하지 말고 후퇴 공간과 별도 교착 탐지·해소 장치(f6)를 함께 확인해야 한다고 이 위키는 본다. | ref-189, ref-192 | 아니오 | low | 2026-10-10 | — | — |
| f8 | [사실] | Bonetti 외의 교통 관리 연구(The International Journal of Robotics Research 2026 게재, DOI 10.1177/02783649261470035; arXiv 2609.10400, 2026-09-09)는 생산라인 말단 설비 업체 Gruppo TecnoFerrari와 함께 개발했으며, 평가는 그 업체가 제공한 경로망·배치로 팔레타이징·보관·팔레트 포장 공장을 모사한 소·중·대 규모 세 배치에서 했다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 | — |
| f9 | [사실] | Bonetti 외의 배치 1에서 AGV는 팔레타이저에서 포장기로 팔레트를 나르고 포장기가 바쁘거나 쓸 수 없으면 임시 보관 구역으로 돌리며, 빈 팔레트를 디스펜서에서 받아 팔레타이저에 보충한다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 / 작업 대상 | — |
| f10 | [사실] | Bonetti 외의 배치 1은 같은 등급 AGV가 복도 4개를 포함한 8개 구역의 좁은 비정형 공간을, 배치 2는 두 등급의 이종 AGV가 고밀도 중형 공간을, 배치 3은 이종 AGV가 좁은 양방향 복도가 없는 넓은 공간을 다니며, 그림 10·11은 막다른 좁은 복도를 표시한다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 / 제약 | — |
| f11 | [사실] | Bonetti 외의 시스템은 NURBS 곡선 경로망 위 지속형 MAPF(L-MAPF) 조율기(수정 Bounded Horizon CBS를 순환 지평 충돌 해소에 넣고 복도 구간에 시간 지평을 늘림), 조율된 궤적을 실행 중 안전하게 할당하는 경로 할당기(§8), 교착 탐지·처리기(§9)를 결합하고 업체의 AGV 관제 소프트웨어(TecnoFerrari Supervisor)에 C#으로 통합됐다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 / 수행 자원 | — |
| f12 | [사실] | Bonetti 외 논문의 공장 실험 사진은 자동화 공장에서 찍은 그림 9 한 장이고 그림 10–12는 TecnoFerrari Supervisor 소프트웨어의 2D 재구성 화면이며, 성과 지표는 Supervisor 안에서 연속 작업 배정으로 시나리오당 약 10시간 실행하며 수집했다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 / 예외·성과 | — |
| f13 | [사실] | Bonetti 외는 업체가 배치한 규칙 기반 교통 관리, Pratissoli 외(2023)의 산업용 방법, PBS로 바꾼 L-MAPF 변형과 비교해 처리량이 최대 약 11% 높았다고 보고하며, 배치 2에서는 규칙 기반 대비 약 11%, PBS 변형 대비 약 10%, Pratissoli 외 대비 약 7%였다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 / 예외·성과 | — |
| f14 | [의견] | Bonetti 외의 배치별 수치는 업체가 제공한 실제 배치를 모사한 실행 결과로 제시되고 실제 운행은 사진 한 장으로만 보이며 업체 소속 공동저자가 있고 독립 재현은 확인하지 못했으므로, 처리량 최대 11%를 상용 공장 실측 개선율이나 다른 현장의 일반 개선율로 옮기지 않아야 한다고 이 위키는 본다. | ref-192 | 아니오 | low | 2026-10-10 | 제조 공장 / 예외·성과 | — |
| f15 | [사실] | Ma 외의 마감이 있는 다중 에이전트 경로 찾기(MAPF with Deadlines, MAPF-DL, IJCAI 2018, pp.417–423)는 공통 마감 시점에 자기 목표 정점을 점유한 에이전트를 성공으로 보고 충돌 없는 성공 에이전트 수를 최대화하는 문제로 정식화하며, 최적 풀이가 NP-hard임을 보이고 흐름 문제 환원 정수 계획법과 탐색 기반 해법을 낸다. | ref-1514 | 아니오 | medium | 2026-10-10 | — | — |
| f16 | [사실] | MAPF-DL의 목적함수는 도착 시각 합이나 전체 완료 시각(makespan)을 줄이는 일반 MAPF 목적과 달리 마감 안 성공 대수를 최대화하는, 교통 계획에 마감을 넣는 공개 정식화의 예다. | ref-1514 | 아니오 | medium | 2026-10-10 | — | — |
| f17 | [의견] | MAPF-DL은 모든 에이전트에 공통 마감 하나를 두므로, 작업별로 다른 출하 마감이나 업무 중요도를 이종 플릿의 통로 양보 규칙으로 바꾸는 산업 기준으로 볼 수는 없다고 이 위키는 본다. | ref-1514, ref-031 | 아니오 | low | 2026-10-10 | — | — |
| f18 | [사실] | VDA 5050 3.0.0 §6.8은 자유 주행 이동 로봇이 상태(state) 메시지로 관제에 예정 궤적을 알리게 하며, 주문 안의 긴 경로 plannedPath(NURBS, 최소한 현재 베이스를 포함하고 지날 nodeId 를 담을 수 있음)와 센서로 볼 수 있는 가까운 경유점별 예상 도착 시각(ETA)을 담은 폴리라인 intermediatePath를 매 상태 메시지마다 공유하게 한다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f19 | [사실] | VDA 5050 3.0.0 §6.4.3은 로봇이 협조 재계획(COORDINATED_REPLANNING) 구역에 들어가거나 구역 안에서 경로를 바꿀 때 zoneRequest 의 requestType 을 REPLANNING 으로 하고 예정 경로를 NURBS 궤적으로 실어 요청하게 하며, 응답을 제때 받지 못하면 구역에 들어가지 않게 한다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f20 | [의견] | VDA 5050 3.0.0은 §2 Scope에서 경로·우선순위·혼잡·교착 해소 같은 교통 관리 로직을 다루지 않으므로, 예정 경로 공유·구역 요청 메시지의 상호운용성과 그 정보를 쓰는 현장 교통 최적화의 성능은 따로 검토해야 한다고 이 위키는 본다. | ref-031 | 아니오 | low | 2026-10-10 | — | — |
| f21 | [사실] | Open-RMF rmf_fleet_adapter 2.14.0(2026-09-26)의 변경 이력은 EasyTrafficLight의 플릿 상태 발행 수정(#525)과 EasyTrafficLight 누적 지연 계산 수정(#524)을 기록한다. | ref-1513 | 아니오 | medium | 2026-10-10 | — | — |
| f22 | [의견] | Open-RMF의 신호등(일시정지·재개) 수준 연동을 비교·시험할 때는 제어 수준뿐 아니라 EasyTrafficLight 수정(f21)이 포함된 rmf_fleet_adapter 판도 기록해야 하며, 이 변경 이력은 수정의 존재를 보여 줄 뿐 제어 수준별 처리량 비교 실험은 아니라고 이 위키는 본다. | ref-1513 | 아니오 | low | 2026-10-10 | — | — |
| f23 | [사실] | Jiang 외의 SILLM 논문(Deploying Ten Thousand Robots, ICRA 2025 채택, arXiv 초판 2024-10-28, v2 2025-05-18)은 최대 10,000 에이전트의 6개 대형 지도 벤치마크와 별도로, 초록과 서론에서 실물 로봇 10대·가상 로봇 100대로 모사 창고(mock warehouse)에서 검증했다고 적는다. | ref-199 | 아니오 | medium | 2026-10-10 | — | — |
| f24 | [사실] | SILLM의 실물 검증(부록 VI-D)은 계획이 모든 에이전트 위치를 정확히 안다고 가정하므로 실물 로봇 위치를 외부 모션 캡처(Optitrack)로 얻고, 교란·제어 오차로 생기는 실행 오차는 행동 의존 그래프(Action Dependency Graph, ADG)로 없앴다. | ref-199 | 아니오 | medium | 2026-10-10 | — | — |
| f25 | [사실] | SILLM 논문은 2023 League of Robot Runners 우승 해법 WPPL과 비교할 때 다른 기준선에 맞추려고 회전 동작을 없애고, 원래의 단계당 계획 시간 1초 제한 대신 대규모 이웃 탐색 개선 반복 횟수를 40,000회로 제한했다. | ref-199 | 아니오 | medium | 2026-10-10 | — | — |
| f26 | [의견] | SILLM 제목의 10,000은 계산 벤치마크의 에이전트 수이지 실물 배치 대수가 아니고, WPPL 비교는 회전 제거·반복 수 제한으로 바꾼 조건의 결과이므로 원래 대회 조건의 재현으로 읽어서는 안 된다고 이 위키는 본다. | ref-199 | 아니오 | low | 2026-10-10 | — | — |
| f27 | [사실] | Yan 외의 LSMART(2026-02-17 프리프린트)는 운동 제약·통신 지연·실행 불확실성·계획과 실행의 동시 진행·계획 실패 복구를 고려해 AGV 플릿 관리 시스템(FMS) 안에서 임의의 MAPF 알고리즘을 평가하는 오픈소스 시뮬레이터이며, 계획기·인스턴스 생성기·계획 호출 정책·실패 정책을 설계 선택으로 비교한다. | ref-604 | 아니오 | medium | 2026-10-10 | — | — |
| f28 | [사실] | LSMART 실험은 지도와 에이전트 수 조건마다 600초 시뮬레이션을 10회 돌려 평균과 95% 신뢰구간을 제시한다. | ref-604 | 아니오 | medium | 2026-10-10 | — | — |
| f29 | [사실] | LSMART 실험에서 재계획을 더 자주 하는 것은 모든 지도·밀도에서 유리하지 않았으며(room-64-64-16과 낮은 밀도에서 이점이 일관되지 않음), 저자들은 ADG로 추정한 확정 지점이 실제 진행과 맞지 않는 실행–계획 불일치를 원인으로 든다. | ref-604 | 아니오 | medium | 2026-10-10 | — | — |
| f30 | [사실] | LSMART 실험에서 더 정확한 로봇 모델과 더 강한 최적성 보장은 계획기의 확장성을 떨어뜨려, 저자들은 이를 계획기의 해 품질과 확장성(solution quality and scalability) 사이의 절충으로 설명한다. | ref-604 | 아니오 | medium | 2026-10-10 | — | — |
| f31 | [사실] | LSMART는 4-연결 격자 기반 시뮬레이션이며 논문에 실물 로봇 실험은 없고, 저자들은 4-연결 격자를 넘는 그래프 지원을 향후 과제로 든다. | ref-604 | 아니오 | medium | 2026-10-10 | — | — |
| f32 | [추정] | LSMART가 격자 시뮬레이션만 다루므로(f31), 이종 제조사 로봇이 섞인 실물 창고에서의 개선율을 직접 제공하지는 않는 것으로 보인다. | ref-604 | 아니오 | low | 2026-10-10 | — | — |
| f33 | [의견] | oq-058에 대해 SILLM의 실물 10대 모사 창고 검증(f23·f24)과 LSMART의 실행 불확실성을 넣은 처리량 실험(f27~f29)이 부분 근거가 되지만, 벤치마크 개선율을 상용 물류센터 실측 개선율로 환산한 자료나 국내 사례는 확인하지 못해 정량 전이 질문은 열린 채로 둔다고 이 위키는 본다. | ref-199, ref-604 | 아니오 | low | 2026-10-10 | — | — |
| f34 | [사실] | oq-059에 대해 MAPF-DL은 공통 마감을 교통 계획의 목적함수에 넣는 정식화를 주지만 작업별 업무 우선순위를 통로 양보 우선권으로 바꾸는 규칙은 다루지 않고, VDA 5050 3.0.0도 우선순위·교착 해소 같은 교통 관리 로직을 범위에서 뺀다. | ref-1514, ref-031 | 아니오 | medium | 2026-10-10 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-195 | Phillips, M., & Likhachev, M. | SIPP: Safe interval path planning for dynamic environments | 2011 | 논문 | high | 2026-10-10 | https://www.researchgate.net/publication/224252713_SIPP_Safe_interval_path_planning_for_dynamic_environments | 아니오 |
| ref-189 | Okumura, K., Machida, M., Défago, X., & Tamura, Y. | Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding | 2019-01 | 논문 | high | 2026-10-10 | https://arxiv.org/abs/1901.11282 | 아니오 |
| ref-192 | Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L. | A traffic management system for large and heterogeneous vehicles in narrow industrial environments | 2026-09-09 | 논문 | high | 2026-10-10 | https://arxiv.org/abs/2609.10400 | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-10 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-1513 | Open-RMF (open-rmf/rmf_ros2 저장소) | Changelog for package rmf_fleet_adapter | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |
| ref-199 | Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 2024-10-28 | 논문 | high | 2026-10-10 | https://arxiv.org/abs/2410.21415 | 아니오 |
| ref-604 | Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J. | Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems | 2026-02-17 | 논문 | medium | 2026-10-10 | https://arxiv.org/abs/2602.15721 | 아니오 |
| ref-1514 | Ma, H., Wagner, G., Felner, A., Li, J., Kumar, T. K. S., & Koenig, S. | Multi-Agent Path Finding with Deadlines | 2018 | 논문 | high | 2026-10-10 | https://www.ijcai.org/proceedings/2018/0058.pdf | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md | 5, 6, 7, 8, 11 | 갱신(차등): 섹션 5 — 제조 공장 사례 추가: Bonetti 외(IJRR 2026) 팔레타이징·보관·팔레트 포장 공장을 모사한 세 배치(산업체 Gruppo TecnoFerrari 제공)(f8), 팔레트 운반 흐름(f9), 배치별 차량·복도 제약(f10), 시스템 구성(f11), 그림 9 실험 사진 한 장·그림 10–12 Supervisor 2D 재구성·10시간 실행(f12), 처리량 최대 약 11%는 저자 보고(f13), 현장 일반 개선율로 옮기지 않음(f14). 기존 ref-192 의 '프리프린트' 표기를 IJRR 게재로 고친다 / 섹션 6(주제 페이지 s6 요약) — 첫 문장 수정: SIPP 는 예측 궤적이 주어진 단일 로봇 경로 탐색(f1)이며 MAPF 전체 최적성으로 옮길 수 없음(f2), 다중 로봇 계획기 안 저수준 계층 예(f3), 서술 분리 권고(f4). PIBT '완전·최적 아님'(f5)과 현장 권고(f7), 교착 탐지·해소 모듈(f6). 그래프 조건 문장은 s6 기존 내용 확인(중복 추가 안 함). MAPF-DL 정식화(f15·f16)와 산업 기준이 아니라는 한정(f17) / 섹션 7(주제 페이지 s7 요약) — VDA 5050 3.0.0 §6.8 예정 경로 공유(f18), §6.4.3 협조 재계획 구역 REPLANNING 요청(f19), 메시지 상호운용성과 교통 최적화 성능 별도 검토(f20). 구역 4종 표·§2 범위 제외는 s7 기존 내용 확인(중복 추가 안 함), 발표일은 쓰지 않음. Open-RMF rmf_fleet_adapter 2.14.0 EasyTrafficLight 수정(f21)과 판 기록 권고(f22) / 섹션 8(주제 페이지 s8 요약) — SILLM 항목 수정: '2024, 프리프린트' → ICRA 2025 채택, 계산 벤치마크 10,000과 실물 10대·가상 100대(초록·서론 기준) 구분(f23), 모션 캡처·ADG(f24), WPPL 비교 조건 변경(f25), 해석 한정(f26). LSMART 추가(f27~f32): 시뮬레이터 구성, 600초×10회, 재계획 빈도 결과, 해 품질과 확장성 절충, 4-연결 격자·실물 실험 없음(사실)과 실물 창고 개선율 미제공(추정) / 섹션 11 — oq-058 부분 근거(f33), oq-059 부분 근거(f34), oq-032 는 f21·f22 가 관련 판 정보만 주며 답하지 않음. 새 질문 2건. 출처: ref-189·ref-192·ref-195·ref-199·ref-604·ref-031 원문 열람으로 갱신, 신규 ref-1513·ref-1514. 다음 실행 후보: 62. 제조 공장(f8~f14 사례 연결), 54. 시험·형식 검증·벤치마크(f27~f32), 20. 로봇·제조사 관제 연동(f18·f19·f21). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 막다른 통로·승강기 입구를 포함한 비격자 경로망에서 PIBT 같은 반복형 해법과 별도 교착 탐지·해소 장치 사이의 전환 기준은 무엇인가? | 관련 영역: 27. 다중 로봇 경로·교통 관리 — MAPF | 근거: f7 | 종류: 일반
- 실행 지연이 큰 환경에서 계획 호출 주기와 미리 확정하는 경로 길이를 함께 조절하는 공개 운영 기준이 있는가? | 관련 영역: 27. 다중 로봇 경로·교통 관리 — MAPF, 32. 예외 복구·재계획·업무 연속성 | 근거: f29 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 8 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 2건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-04/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - VDA 5050 3.0.0 발표일(메모의 2026-03-19)은 근거를 확인하지 못해 쓰지 않았고(published null), GitHub release notes 출처(메모 n4)는 원문 확인이 안 돼 제외했다. '주요 변경' 서술은 명세 본문 §6.8·§6.4.3 으로 근거를 옮겼다
    - ref-031 은 main 판 URL 의 기존 출처이며 이번 열람은 3.0.0 태그 판이다. main 판이 3.0.0 과 같은지는 다시 대조하지 않았다
    - f13·f14: Bonetti 외의 배치별 처리량 수치가 모사 실행인지 실제 공장 운행인지 원문이 수치 단위로 구분하지 않아 확인 못 함. 독립 현장 재현 미확인
    - f23: SILLM 의 실물 10대·가상 100대는 초록과 서론 끝 문장 기준이며 §V-C 본문은 대수 없이 프로젝트 웹페이지를 가리킨다(웹페이지 미열람)
    - 모든 사실 finding 은 단일 출처라 교차 확인 0건
    - oq-058·oq-059 는 부분 근거만 있어 해결 제안하지 않음. oq-032·oq-057 근거 없음
- 범위 경계 위반 의심:
    - f6·f11: 교착 탐지·해소와 경로 할당은 ROP 직접 범위(여러 플릿의 공유 공간 조율)에 해당하나, Bonetti 외 시스템은 단일 업체 관제 안의 기능이므로 9절 책임 경계와 섞지 않도록 사례 근거로만 쓴다
    - f24: 실물 로봇 위치 추정(모션 캡처)과 실행 오차 보정은 로봇 쪽 위치 인식·제어(외부 연계 대상)와 맞닿아 있어 실험 조건 설명으로만 쓴다
- 한계: 외부 조사 변환이라 검색 집계 없음(queries 0 은 이 실행 안의 WebSearch 호출이 없다는 뜻이며, 외부 AI의 검색 횟수는 알 수 없다). 원문 대조는 2026-10-10 검증 서브에이전트가 WebFetch·GitHub raw 로 연 사본(9건 중 release notes 제외 8건)으로 했다. 출처 8건: 기존 6건(ref-031·ref-189·ref-192·ref-195·ref-199·ref-604, 이번에 원문 열람으로 fetched true), 신규 2건(ref-1513 rmf_fleet_adapter 변경 이력, ref-1514 MAPF-DL; 예약 구간 ref-1513~ref-1542 안). 동료심사 게재가 확인된 논문(ref-189 AIJ 2022, ref-192 IJRR 2026, ref-195 ICRA 2011, ref-199 ICRA 2025, ref-1514 IJCAI 2018)은 원문 열람 기준에 따라 신뢰도 high 로 적었고 프리프린트 ref-604 는 medium. 검증 수정 반영: ref-192 를 프리프린트가 아닌 IJRR 게재로, 현장 유형을 '팔레타이징·보관·팔레트 포장 공장을 모사한 세 배치(산업체 제공)'로, 사진은 그림 9 한 장·그림 10–12 는 Supervisor 2D 재구성으로 정정. PIBT 는 v5=AIJ 게재판으로 적고 그래프 조건은 s6 기존 문장이 있어 다시 넣지 않음. SILLM ICRA 2025 채택 반영. VDA 5050 발표일 null·release notes 제외, 구역 4종·§2 범위 제외는 s7 기존 내용이라 사실 finding 으로 다시 내지 않음. LSMART 마지막 문장을 사실(f31: 4-연결 격자·실물 실험 없음)과 추정(f32: 실물 창고 개선율 미제공)으로 나누고 절충 표현은 원문 'solution quality and scalability'. SIPP 는 '예측 궤적'으로. 현장 유형 finding 은 제조 공장(f6·f8~f14)뿐이며 물류창고 사례는 모사 창고(SILLM)라 site_type null. 국내 자료 없음. 용어 후보 없음(MAPF·SIPP·PIBT·ADG 계열 용어는 기존 페이지에 있고 MAPF-DL 은 본문 정의로 충분). 입력 누락 없음. 정정 요청·우선 지정 질문 없음.
```

### runs/2026-10-10-03/research.md

```markdown
# 리서치 브리프 2026-10-10-03

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-03 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 26. 작업 순서·스케줄링 |
| 대분류 | G. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 시작 조건 칸의 'Open-RMF 요청에 마감·선후 필드는 없다'가 공통 최상위 스키마 범위인지 밝혀져 있지 않고, 유형별 description 확장 경로를 다루지 않음. 물류창고 외 현장 유형 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — Open-RMF 기본 비용이 무엇을 최소화하는지(완료 시각 합 vs 메이크스팬), 누적 용량 제약, 진행 중 동작을 고정하는 재계획 방식이 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 — BinaryPriorityScheme 행이 '비용 반영 방식은 미확인'으로 남아 있고, 2026-09-25 이후 rmf_fleet_adapter 변경(2.14.0) 미반영
- 섹션 8. 대표 연구와 자료(주제 페이지로 분리) — 성능 수치가 모두 원문 미열람이며 2024~2025년 동적·협업 일정 연구가 없음
- 섹션 11. 열린 질문(주제 페이지로 분리) — oq-019·oq-049 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 일이 계속 새로 들어올 때 무엇을 먼저, 언제 할지 어떻게 정할 것인가? [분류원문]
2. Open-RMF task_request 스키마의 마감·선후 필드 부재는 공통 최상위 스키마에 한정되는가, 유형별 확장 경로는 무엇인가? (섹션 5·7 겨냥)
3. Open-RMF 이진 우선순위는 비용 계산에 어떻게 반영되며, 기본 비용은 어떤 지표를 최소화하는가? (섹션 6·7 겨냥)
4. 마감·공용 자원 용량·선택 작업을 제약으로 표현하는 공개 도구와, 진행 중 동작을 보존하며 재계획하는 연구는 무엇인가? (섹션 6·8 겨냥)
5. oq-019 상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가? (섹션 11 겨냥)
6. oq-049 제조사가 다른 로봇 플릿 사이의 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 작업 요청 수준에서 표현·집행하는 표준 필드나 공개 구현이 있는가? (섹션 11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF task_request.json 의 공통 최상위 필드는 unix_millis_earliest_start_time·unix_millis_request_time·priority·category·description·labels·requester·fleet_name 의 8개이고 필수는 category·description 뿐이며, 마감 시각이나 다른 작업 ID 를 가리키는 선후 필드는 공통 최상위 스키마에 정의되어 있지 않다. | ref-125 | 아니오 | medium | 2026-10-10 | 시작 조건 | — |
| f2 | [사실] | 같은 스키마에서 description 은 그 작업 유형(category)에 대해 플릿이 지원하는 스키마를, priority 는 플릿이 지원하는 우선순위 스키마를 따라야 한다고 설명하며, 최상위에 additionalProperties 제한은 두지 않는다. | ref-125 | 아니오 | medium | 2026-10-10 | 시작 조건 | — |
| f3 | [추정] | 공통 최상위 스키마에 마감·선후 필드가 없다는 것이 유형별 description 확장이나 플릿별 우선순위 스키마로 그런 조건을 구현하는 것이 불가능하다는 뜻은 아닐 것으로 보인다. | ref-125 | 아니오 | low | 2026-10-10 | 제약 | — |
| f4 | [의견] | 출하 마감이나 다른 작업 완료를 시작 조건으로 쓰려면, 문법상 추가 필드를 넣을 수 있다는 것과 계획기가 그 필드를 집행한다는 것을 구분해 그 확장 계약과 집행 주체를 별도로 명시해야 한다. | ref-125 | 아니오 | low | 2026-10-10 | 제약 | — |
| f5 | [사실] | rmf_task 의 BinaryPriorityScheme.cpp 는 make_low_priority() 에서 nullptr 를, make_high_priority() 에서 BinaryPriority(1) 객체를 돌려주고, make_cost_calculator() 로 BinaryPriorityCostCalculator 를 만든다. | ref-1484 | 아니오 | medium | 2026-10-10 | — | — |
| f6 | [사실] | BinaryPriorityCostCalculator 의 valid_assignment_priority() 는 같은 계획 노드 안의 로봇(에이전트) 사이에서 한 로봇이 높은 우선순위 작업을 2개 이상 받았는데 높은 작업을 하나도 받지 않은 로봇이 있으면 위반으로 보고, 같은 로봇의 배정 순서 안에서는 충전 작업을 건너뛴 뒤 낮은 작업 다음에 높은 작업이 오면 위반으로 본다. | ref-1483 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f7 | [사실] | compute_cost(Node, time_now, check_priority) 는 우선순위 검사가 켜져 있고 배정이 위반이면 비용을 _priority_penalty × (g + h) 로, 그렇지 않으면 g + h 로 계산한다. | ref-1483 | 아니오 | medium | 2026-10-10 | — | — |
| f8 | [의견] | 이 우선순위 처리는 납기 제약을 직접 검사하는 코드가 아니라 배정 비용에 벌점을 곱하는 방식이므로, 높은 우선순위를 마감 보장으로 해석해서는 안 되며 로봇 사이 배분 조건이 있어 단순한 선입선출 정렬로 설명해서도 안 된다. | ref-1483, ref-125 | 아니오 | low | 2026-10-10 | 제약 | — |
| f9 | [사실] | BinaryPriorityCostCalculator 의 기본 실비용(g)은 각 일반 작업의 완료 시각(finish_state 시각)에서 그 요청의 가장 이른 시작 시각을 뺀 값을 모든 로봇·모든 배정에 걸쳐 합산한 값이다. | ref-1483 | 아니오 | medium | 2026-10-10 | — | — |
| f10 | [사실] | 같은 계산기는 충전 작업(ChargeBattery) 배정 자체의 비용을 0 으로 계산한다. | ref-1483 | 아니오 | medium | 2026-10-10 | — | — |
| f11 | [추정] | 충전 작업 자체의 비용은 0 이지만, 충전 때문에 같은 로봇의 뒤 작업 완료가 늦어지면 그 작업의 비용(완료 시각 − 가장 이른 시작 시각)은 커질 수 있을 것으로 보인다. | ref-1483 | 아니오 | low | 2026-10-10 | — | — |
| f12 | [의견] | 이 비용은 작업별 (완료 시각 − 가장 이른 시작 시각)의 합이므로, Dai 외가 정의한 메이크스팬(Makespan, 차고지 복귀를 포함한 모든 로봇의 총 작업 시간 중 최댓값)이나 납기 지연 합과 같은 지표라고 부르면 안 된다. | ref-1483, ref-1486 | 아니오 | low | 2026-10-10 | — | — |
| f13 | [사실] | OR-Tools CP-SAT 스케줄링 문서는 구간 변수, 실행 여부를 리터럴로 정하는 선택 구간, 구간 사이 시간 관계, 겹침 금지(NoOverlap)에 더해, 구간별 수요의 합이 용량 프로필을 넘지 않게 하는 누적 용량(Cumulative) 제약을 다룬다. | ref-379 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f14 | [추정] | 이 표현으로 '이전 작업 종료 뒤 시작'(시간 관계), '도크는 한 번에 한 작업'(겹침 금지), '작업대 동시 사용량은 용량 이하'(누적 용량)를 서로 다른 제약으로 작성할 수 있을 것으로 보인다. | ref-379 | 아니오 | low | 2026-10-10 | 제약 | — |
| f15 | [사실] | Tuck 외(2024)의 동적 다중 로봇 작업 배정 정식화는 Definition 6(완료된 작업)에서 내려놓기 동작이 마감 전에 일어나야 작업을 완료한 것으로 보아, 마감을 필수 완료 조건으로 둔다. | ref-1485 | 아니오 | medium | 2024-03-18 | 제약 | — |
| f16 | [의견] | 마감을 반드시 지킬 조건으로 둘지, 어겼을 때 비용을 주는 조건으로 둘지는 목적함수와 제약식을 나눠 설계해야 한다. | ref-379, ref-1485 | 아니오 | low | 2026-10-10 | 제약 | — |
| f17 | [사실] | Tuck 외(2024)는 마감이 있는 작업이 온라인으로 들어오고 로봇이 여러 작업을 동시에 실을 수 있는 동적 다중 로봇 작업 배정(Multi-Robot Task Allocation, MRTA)을 다루며, Definition 9 의 갱신 계획(Updated plan)은 각 로봇의 과거 동작과 현재 동작을 바꾸지 않은 채 새 작업을 반영하도록 정의한다. | ref-1485 | 아니오 | medium | 2024-03-18 | — | — |
| f18 | [사실] | 같은 연구는 이론 모듈로 만족 가능성(Satisfiability Modulo Theories, SMT) 해법기의 push·pop 기능으로 앞선 풀이 정보를 유지하는 증분 풀이를 쓰지만, 증분·비증분 풀이의 시간 성능은 해법기와 배치 크기에 따라 크게 달랐다(Z3-BV 와 Bitwuzla-BV 비교). | ref-1485 | 아니오 | medium | 2024-03-18 | — | — |
| f19 | [추정] | 이를 참고하면 긴급 작업 삽입 정책을 '현재 동작 고정'과 '아직 실행하지 않은 구간의 재배열'로 나눠 기술할 수 있을 것으로 보인다. | ref-1485 | 아니오 | low | 2024-03-18 | 예외·성과 | — |
| f20 | [사실] | Dai 외(2025)는 탐색·구조 같은 협업 과제를 모사한 계산 실험에서, 배정된 로봇 연합의 능력 벡터 합이 작업 요구를 충족해야 작업을 시작할 수 있고 모든 배정 로봇이 실행 기간 내내 작업 위치에 함께 있어야 하며 먼저 도착한 로봇은 나머지가 올 때까지 기다리는 작업을 모델링한다. | ref-1486 | 아니오 | medium | 2025 | 기타 / 시작 조건 | — |
| f21 | [추정] | 이런 협업 작업에서는 개별 로봇이 빨리 도착해도 다른 팀원이 늦으면 작업 시작이 늦어지므로, 개별 로봇의 빠른 도착만으로 전체 종료 시간이 줄지는 않을 것으로 보인다. | ref-1486 | 아니오 | low | 2025 | 기타 / 제약 | — |
| f22 | [의견] | 이 사례를 이용하면 일정 설명에서 도착 동기화, 공동 작업 시간, 다음 작업으로의 이동을 구분해 적을 수 있다. | ref-1486 | 아니오 | low | 2025 | 기타 | — |
| f23 | [사실] | Dai 외(2025)는 강화학습(Reinforcement Learning, RL)으로 이종 로봇이 다음 작업을 분산적으로 고르는 협업 일정 정책을 학습하고, 계산 실험에서 최대 150 에이전트·500 작업·5종 능력 조건까지 다뤘다고 보고한다. | ref-1486 | 아니오 | medium | 2025 | — | — |
| f24 | [사실] | Open-RMF TaskPlanner.hpp 의 Options 주석은 탐욕 방식은 최적성을 보장하지 않지만 더 빨리 풀 수 있고, A* 기반 방식은 최적성을 보장하지만 풀이에 더 오래 걸릴 수 있다고 설명한다. | ref-377 | 아니오 | medium | 2026-10-10 | — | — |
| f25 | [의견] | Dai 외의 강화학습 방식과 Open-RMF 계획기는 목적·모델·평가 환경이 달라, 규모나 풀이 시간만으로 우열을 정하기보다 실행 가능한 일정 비율과 목적값을 같은 조건에서 비교하는 편이 좋다. | ref-1486, ref-377 | 아니오 | low | 2026-10-10 | — | — |
| f26 | [사실] | rmf_fleet_adapter 2.14.0(2026-09-26) 변경 이력은 단계 건너뛰기 요청의 단계 키 수정(#543)과 EasyTrafficLight 의 누적 지연 계산 수정(#524)을 포함한다. | ref-1487 | 아니오 | medium | 2026-09-26 | 예외·성과 | — |
| f27 | [의견] | 일정의 예외 조정과 지연 기반 추정에 의존하는 구현은 사용하는 Open-RMF 패키지 버전을 함께 기록하는 편이 좋다. | ref-1487 | 아니오 | low | 2026-09-26 | — | — |
| f28 | [의견] | oq-019 부분 답변: 이진 우선순위의 표현과 비용 벌점 구현은 공개되어 있지만, 납기·운송 마감을 이진 값으로 바꾸고 진행 중 작업을 재정렬하는 현장 설계는 확인하지 못해 질문을 닫을 수 없다. | ref-125, ref-1483, ref-1484 | 아니오 | low | 2026-10-10 | — | — |
| f29 | [추정] | oq-049 부분 답변: 공통 task_request 스키마에는 선행 작업 ID 가 없고 유형별 description 확장 경로만 있어, 이 경로만으로 제조사 간 선후 집행이 구현되었다고 볼 수 없으며 범용 표준 필드나 완성된 공개 구현은 확인하지 못했다. | ref-125 | 아니오 | low | 2026-10-10 | 완료·인계 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp | 아니오 |
| ref-379 | Google (google/or-tools GitHub) | OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver) | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md | 아니오 |
| ref-1483 | Open Robotics (open-rmf) | rmf_task — rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp | 아니오 |
| ref-1484 | Open Robotics (open-rmf) | rmf_task — rmf_task/src/rmf_task/BinaryPriorityScheme.cpp | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityScheme.cpp | 아니오 |
| ref-1485 | Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (UC Berkeley, Toyota Motor North America) | SMT-Based Dynamic Multi-Robot Task Allocation | 2024-03-18 | 논문 | medium | 2026-10-10 | https://arxiv.org/html/2403.11737v1 | 아니오 |
| ref-1486 | Dai, W., Rai, U., Chiun, J., Cao, Y., & Sartoretti, G. | Heterogeneous Multi-robot Task Allocation and Scheduling via Reinforcement Learning | 2025 | 논문 | medium | 2026-10-10 | https://marmotlab.org/publications/73-RAL2025-HetMRTA.pdf | 아니오 |
| ref-1487 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md | 5, 6, 7, 8, 11 | 갱신(차등): 섹션 5 — 시작 조건 칸 문장을 공통 최상위 스키마 범위로 한정(f1)하고 description·priority 의 플릿 스키마 위임(f2), 확장 가능성(f3, 추정), 확장 계약·집행 주체 명시 필요(f4, 의견)를 제약 칸에 반영; 물류창고 표와 별도로 '현장 유형: 기타(탐색·구조 모사 계산 실험)' 협업 사례를 추가(f20 사실, f21 추정, f22 의견) / 섹션 6(주제 페이지 2026-09-25-area14-s6 요약) — 플릿 안 일정 계획에 기본 비용 정의(f9·f10, f11 추정)와 메이크스팬과의 구분(f12, 의견), 제약 프로그래밍에 누적 용량 제약(f13; 구간·선택 구간·선후·겹침 금지는 기존 내용 확인)과 창고 제약 대응(f14 추정)·마감의 필수/비용 설계 구분(f15·f16), 온라인 재계획에 Tuck 외 갱신 계획·증분 풀이(f17·f18, f19 추정) / 섹션 7 — BinaryPriorityScheme 행의 '비용 반영 방식은 미확인'을 f5~f7 로 교체하고 마감 보장 해석 금지(f8, 의견), Open-RMF 작업 요청 스키마 행 문구를 공통 최상위 필드 기준으로(f1·f2), rmf_fleet_adapter 2.14.0 변경 이력 행 추가(f26, f27 의견) / 섹션 8(주제 페이지 2026-09-25-area14-s8 요약) — Tuck 외(f17·f18), Dai 외(f23) 추가와 접근법 비교 방식(f24·f25; f24 의 탐욕·A* 설명은 기존 6절 분리 페이지 내용 확인) / 섹션 11(주제 페이지 2026-09-25-area14-s11) — oq-019 부분 근거(f28), oq-049 부분 근거(f29), 새 질문 3건. 두 열린 질문 모두 해결 제안 없음. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 메이크스팬 | Makespan | 작업 집합 전체를 끝내는 데 걸린 시간으로, 다중 로봇 일정에서는 보통 모든 로봇 가운데 가장 늦게 일을 마친 로봇의 종료 시각(또는 총 작업 시간)을 뜻한다. |
| 이론 모듈로 만족 가능성 | Satisfiability Modulo Theories (SMT) | 정수·비트벡터 산술 같은 배경 이론 위에서 논리식을 만족하는 값의 존재를 판정하는 문제와 그 해법기로, 일정·배정 제약을 논리식으로 풀 때 쓴다. |

## 열린 질문

새로 생긴 질문:

- 이진 우선순위에서 높은 작업이 계속 들어올 때 낮은 작업의 무한 대기를 막는 공개 정책이 있는가? | 관련 영역: 26. 작업 순서·스케줄링, 25. 작업 배정 — MRTA | 근거: f6 | 종류: 일반
- 제조사별 예상 완료 시간의 오차를 고려해 출하 마감 대비 여유 시간을 얼마나 두는가? | 관련 영역: 26. 작업 순서·스케줄링, 20. 로봇·제조사 관제 연동 | 근거: f16 | 종류: 일반
- 작업 완료 시각 합, 납기 지연 합, 계획 변경량을 함께 최적화할 때 현장별 가중치를 어떻게 검증하는가? | 관련 영역: 26. 작업 순서·스케줄링, 39. 운영 성과 측정·개선 | 근거: f12 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 8 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 5건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-03/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - ref-1486(Dai 외): 게재지 IEEE Robotics and Automation Letters 2025 는 PDF 파일명(73-RAL2025-HetMRTA) 기준이며 본문에서 확인하지 못함 — published 는 '2025'로만 둠, 동료심사 여부 미확인이라 신뢰도 medium
    - f3·f29: 유형별 description 확장으로 마감·선후 조건을 실제 집행하는 Open-RMF 구현은 확인하지 못함(다른 작업 유형 스키마 전체는 대조하지 않음)
    - f11: 충전 작업이 뒤 작업 비용을 늘리는 효과는 코드 정의에서 도출한 추론이며 실행 결과로 확인하지 않음
    - f21: '개별 로봇의 빠른 도착만으로 전체 종료 시간이 줄지 않는다'는 원문 직접 진술이 아니라 추론(검증에서 사실→추정 강등)
    - f23: Dai 외 성능 비교(MIP·휴리스틱 대비)는 저자 실험이며 독립 재현 미확인
    - oq-019·oq-049: 부분 근거만 확보, 재정렬 현장 설계와 제조사 간 선후 집행의 공개 구현은 미확인
    - 교차 확인 0건: rmf_task 헤더·구현·스키마는 같은 프로젝트 자료라 독립 교차 확인으로 세지 않음
- 범위 경계 위반 의심:
    - f20~f23: Dai 외는 탐색·구조를 모사한 계산 실험이라 물류창고 사례가 아님 — 5절에는 현장 유형 '기타'로 따로 두고 창고 피킹–포장 인계와 같다고 쓰지 않는다
    - f13·f14·f16: OR-Tools 는 일반 스케줄링 도구이며 로봇 관제용 스케줄러가 아님 — 제약 표현 근거로만 쓴다
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 5건(ref-1483~ref-1487, 예약 구간 ref-1483~ref-1512 안), 재사용 3건(ref-125 task_request.json, ref-377 TaskPlanner.hpp, ref-379 OR-Tools scheduling.md). 메모의 n3(BinaryPriorityScheme.cpp)은 기존 ref-390(BinaryPriorityScheme.hpp)과 다른 파일이라 새 id 로 등록. 8개 출처 모두 원문 대조 확인(GitHub 파일은 github_raw, 논문 2건은 webfetch). 검증 수정 반영: (1) Tuck 외 증분 풀이 이득의 조건을 '해법기와 배치 크기'로 정정(f18), (2) '공통 필드의 부재가 확장 구현의 불가능을 뜻하지 않는다'를 추정으로 분리(f3), (3) Dai 외 '빠른 도착만으로 전체 종료 시간이 줄지 않는다'를 추정으로 분리(f21), 앞부분은 §III 사실(f20), (4) 이진 우선순위 배분 조건을 같은 계획기 안 로봇 사이 조건과 같은 로봇 안 순서 조건으로 정정하고 벌점식 _priority_penalty × (g + h) 명시(f6·f7), (5) TaskPlanner 의 A* 최적성 보장 명시(f24), (6) 메이크스팬을 Dai 외 정의(차고지 복귀 포함 모든 로봇의 최대 총 작업 시간)로 맞춤(f12), (7) task_request.json 최상위 필드 8개·필수 2개·additionalProperties 없음 명시(f1·f2), (8) Dai 외 게재지 미확인·published 2025·저자 5명(ref-1486), (9) 기존 id 연결. 열린 질문은 해결 제안 없이 oq-019(f28)·oq-049(f29) 부분 근거만 냈다. 메모의 출처 집계 문장('원문 열람 8/8')은 검증 결과와 일치. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-09-25-69/research.md

```markdown
# 리서치 브리프 2026-09-25-69

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-69 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 28. 표준·상호운용성·다사업자 거버넌스 |
| 대분류 | G. 안전·보안·지능·거버넌스 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(적합성 시험·ECLASS·의미 식별자는 용어집에 있으나 의미적 버전 관리·서비스 수준 협약·감사 추적·산업데이터 없음)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음(트랙 반영 제안 12건 대기)
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(oq-004·005·020·025·026·027·041·044·055·065·085·089·091·096 이 이 영역에 걸려 있음)

## 조사 질문

1. 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [분류원문]
2. 로봇–관제 공통 규격(VDA 5050, MassRobotics AMR 상호운용 표준, Open-RMF)은 누가 관리하고, 각 규격은 관제와 로봇 사이 책임을 어떻게 나누는가? (섹션 3·7·9 겨냥)
3. 공통 규격과 ROP API 의 변경 정책(판 번호 규칙, 하위 호환, 폐기 예고)은 어떻게 정해지는가? (섹션 4·6 겨냥, oq-091 관련)
4. 적합성 시험·인증은 어떤 형태로 운영되는가(OPC UA 인증, VDA 5050 인증 발표, 국내 단체표준 상호운용성 시험 절차)? (섹션 6·7 겨냥, oq-055 관련)
5. 여러 사업자가 함께 만든 로봇 운행 데이터의 소유권·접근권은 국내외 법제에서 어떻게 다뤄지는가? (섹션 3·9 겨냥)
6. 다사업자 운영에서 서비스 수준과 감사 이력은 어떤 표준 요구로 뒷받침되는가? (섹션 4·6·7 겨냥)
7. 한국의 로봇 상호운용·건물 연동 관련 국가표준·단체표준은 무엇이 있는가? (섹션 7 겨냥, oq-041·oq-026 관련)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 은 VDA 와 VDMA 가 개발하고 카를스루에 공대(KIT) 물류연구소(IFL)가 위탁을 받아 개발을 주도하며 공식 GitHub 저장소를 관리하고, 명세는 사용이 선택적이고 구속력이 없다고 밝힌다. | ref-031, ref-704 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 3.0.0 은 주문 배정·경로 계산·교착 탐지와 해소·교통 제어를 관제 쪽, 위치 추정·경로와 동작 실행·상태의 지속 전송을 이동로봇 쪽 책임으로 나누고, 기능·운영·시스템 안전 요구와 교통 관리 로직은 다루지 않는다고 명시한다. | ref-031 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f3 | [사실] | VDA 5050 공식 저장소 README 는 VDA 웹사이트의 공식 PDF 가 GitHub 내용보다 우선하며, 어느 판에 대해서도 지원·유지보수·문제 해결을 받을 법적 권리가 없다고 적는다. | ref-704 | 아니오 | medium | 2026-09-25 | — | — |
| f4 | [사실] | VDA 5050 의 변경은 GitHub 이슈로 제안되고 월례 회의에서 논의되는 이슈에 진행 표시를, 수용된 변경에 반영 예정 판의 마일스톤을 붙이는 방식으로 관리되며, 3.0.1 은 오타·수정, 3.1.0 은 하위 호환 변경용이고 호환을 깨는 4.0.0 은 현재 계획되지 않았다. | ref-704 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | VDA 5050 3.0.0 은 의미적 버전 관리를 따라 필수 필드 추가 같은 파괴적 변경은 주 버전, 선택 매개변수 추가 같은 기능 추가는 부 버전, 오타 수정은 수 버전으로 올리고, 메시지 헤더의 version 필드에 [Major].[Minor].[Patch] 형식의 프로토콜 판을 싣는다. | ref-031, ref-051 | 아니오 | medium | 2026-09-25 | — | — |
| f6 | [사실] | 의미적 버전 관리(Semantic Versioning) 2.0.0 은 공개 API 선언을 요구하고, 호환되지 않는 API 변경은 MAJOR, 하위 호환 기능 추가는 MINOR, 하위 호환 버그 수정은 PATCH 를 올리며, 기능을 폐기할 때는 먼저 폐기 표시를 담은 부 버전을 낸 뒤 주 버전에서 제거하도록 권한다. | ref-706 | 아니오 | medium | 2026-09-25 | — | — |
| f7 | [사실] | IETF RFC 9745 는 자원이 폐기되었거나 폐기될 것임을 알리는 Deprecation HTTP 응답 헤더를 정하고, RFC 8594 의 Sunset 헤더와 함께 쓰일 때 Sunset 시각은 Deprecation 시각보다 이르면 안 된다. | ref-713 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f8 | [추정] | ROP 의 API 변경 정책은 상위 업무 시스템에 여는 API 에는 의미적 버전 관리와 폐기 예고·종료 시각 공지를 적용하고, 로봇 쪽에는 VDA 5050 헤더 version 처럼 로봇별 프로토콜 판을 기록해 판 차이를 관리하는 두 갈래로 설계할 수 있어 보인다. | ref-706, ref-713, ref-031, ref-051 | 아니오 | low | 2026-09-25 | — | — |
| f9 | [사실] | MassRobotics AMR 상호운용 표준의 JSON 스키마는 신원 보고(identityReport)와 상태 보고(statusReport) 두 보고 메시지만 정의하고 명령·작업 배정 메시지는 두지 않는다. | ref-253 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f10 | [사실] | MassRobotics AMR 상호운용 표준은 여러 제조사의 AMR 이 같은 현장에서 공존하도록 로봇의 위치·속도·방향·상태(health)·작업 가용성 정보를 공유하게 하는 것을 목적으로 한다. | ref-253 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f11 | [사실] | Open-RMF 는 플릿마다 플릿 어댑터가 제조사 고유 API 를 RMF 교통 일정·협상 인터페이스에 잇게 하고, 연동 수준을 전체 제어(Full Control)·신호등(Traffic Light)·읽기 전용(Read Only)·인터페이스 없음(No Interface)으로 나눠 제조사 관제를 표준화 없이 그 수준에 맞춰 통합한다. | ref-004 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f12 | [사실] | Open-RMF 는 2024-04-15 운영을 시작한 오픈소스 로보틱스 연합(OSRA) 체계에서 프로젝트 관리 위원회(PMC)가 일상 운영을 맡고, 기술 거버넌스 위원회(TGC)가 PMC 활동을 감독하며, 거버넌스 문서 개정은 해당 기구의 승인과 이사회 비준을 거친다. | ref-711, ref-710 | 아니오 | medium | 2024-03 | — | — |
| f13 | [사실] | OPC Foundation 은 규격 적합성을 확인하는 적합성 시험 도구(CTT)를 제공하고, 제조사가 자체 인증하거나 재단이 인정한 독립 시험소의 인증을 받게 하며, 통과 제품에 인증서와 인증 로고를 준다. | ref-712 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f14 | [추정] | 이번에 읽은 VDA 5050 3.0.0 명세와 저장소 README 에는 공식 적합성 시험·인증 절차가 정의되어 있지 않아 보이며, 확인한 VDA 5050 인증 근거는 제조사–관제 업체 간 인증 발표와 제3자 오픈소스 시험 도구뿐이다(부재 확정 아님). | ref-031, ref-704, ref-608, ref-407, ref-408 | 아니오 | low | 2026-09-25 | — | — |
| f15 | [추정] | OTTO by Rockwell Automation 은 자사 AMR 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 관제 업체와 인증을 마쳤다고 발표했으나 인증의 시험 항목과 주체는 공개 자료로 확인되지 않았다. | ref-608 | 아니오 | low | 2026-04 | — | 원문 미열람, 벤더 주장 |
| f16 | [사실] | 한국지능형로봇표준포럼(KOROS)은 단체표준 KOROS 1148-8:2025 '서비스 로봇을 위한 모듈 — 제2-8부: 소프트웨어 모듈용 정보모델 상호운용성 시험 절차'를 제·개정 현황에 올렸다. | ref-718 | 아니오 | medium | 2025 | — | 원문 미열람 |
| f17 | [사실] | EU 데이터법(Regulation (EU) 2023/2854, 2023-12-13 채택, 2024-01-11 발효)은 기업·이용자·공공 사이 데이터 접근·이용 규칙을 정하고, 제품 제조사와 데이터 보유자에게 데이터 공유·상호운용성 의무를, 데이터 처리 서비스 제공자에게 고객의 사업자 전환 허용 의무를 둔다. | ref-707 | 아니오 | medium | 2023-12-13 | — | 원문 미열람 |
| f18 | [사실] | 한국 산업디지털전환촉진법은 상당한 투자와 노력으로 산업데이터를 새로 생성한 자에게 사용·수익 권리를 주고, 2인 이상이 공동으로 생성하거나 제3자에게 제공한 경우 당사자 약정이 없으면 각자 사용·수익 권리를 가진다고 정한다. | ref-708, ref-709 | 아니오 | medium | 2022-01-04 | — | 원문 미열람 |
| f19 | [추정] | 로봇 상태·운행 기록처럼 제조사 로봇, ROP, 현장 운영사가 함께 만드는 데이터는 국내법상 공동 생성 데이터로 볼 여지가 있어, 약정이 없으면 각 사업자가 사용·수익 권리를 가지므로 연동 계약에서 데이터 범위·이용 목적·제3자 제공을 따로 정해야 할 것으로 보인다. | ref-708, ref-707 | 아니오 | low | 2026-09-25 | 완료·인계 | 원문 미열람 |
| f20 | [사실] | ISO 10218-2:2025 는 로봇 자체를 다루는 Part 1 과 구분해 산업용 로봇 적용과 로봇 셀의 안전 요구를 다루며, 통합자(integrator)가 합리적으로 예견할 수 있는 위험원과 위험 상황을 대상으로 한다. | ref-560 | 아니오 | medium | 2025-02 | — | 원문 미열람 |
| f21 | [추정] | 분류 원문 질문과 관련해, 확인한 규격을 종합하면 연동 오류 수정 책임은 규격 불일치는 해당 메시지를 구현한 쪽(로봇 제조사 또는 관제), 플릿 어댑터·매핑 오류는 ROP, 시스템 수준 위험과 변경 승인은 통합자 역할을 맡는 쪽으로 나누는 구조가 될 수 있어 보이나, 이를 정한 공식 기준은 확인되지 않았다. | ref-031, ref-004, ref-560, ref-704 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f22 | [사실] | IEC 62443-3-3:2013 은 제어 시스템이 감사 대상 이벤트를 기록하고(SR 2.8), 감사 기록에 타임스탬프를 쓰며(SR 2.11), 감사 정보를 보호하도록(SR 3.9) 요구하고, SR 2.8 의 강화 요구로 중앙에서 관리하는 시스템 전체 감사 추적을 둔다. | ref-715 | 아니오 | medium | 2013-08 | — | 원문 미열람 |
| f23 | [사실] | ISO/IEC 20000-1:2018 은 서비스 관리 시스템의 수립·실행·유지·지속 개선 요구사항을 정하는 표준으로, 서비스 수준 관리를 관계·합의 프로세스에 포함한다. | ref-716 | 아니오 | medium | 2018 | — | 원문 미열람 |
| f24 | [추정] | 이종 플릿 환경의 서비스 수준은 ROP 가 고객과 맺는 가용성·응답 목표가 제조사 관제·설비업체의 목표에 기대므로, 서비스 관리 표준의 서비스 수준 관리와 감사 추적 요구를 결합해 사업자별 목표와 장애 귀책을 기록으로 확인하는 구조가 필요해 보인다. | ref-716, ref-715 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f25 | [사실] | 산업통상자원부 국가기술표준원은 2021-11-11 행정안전부(승강기 안전기준 소관)와 협력해 로봇의 엘리베이터 탑승 시 안전 요구사항과 실내 배송 로봇 등에 관한 국가표준(KS)을 제정한다고 밝혔다. | ref-717 | 아니오 | medium | 2021-11-11 | 제약 | 원문 미열람 |
| f26 | [추정] | 출하 단계에서 한 제조사가 로봇 펌웨어를 올려 VDA 5050 프로토콜 판이 바뀌면, 관제가 헤더 version 으로 판 차이를 감지하고 지원하지 않는 선택 필드는 UNSUPPORTED_PARAMETER 오류로 드러나므로, 변경 승인 전 판 호환 시험과 수정 책임을 계약으로 정해 두어야 출하 마감 전 작업 실패를 막을 수 있을 것으로 보인다. | ref-031, ref-051 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f27 | [추정] | 입고 단계에서 새 제조사 로봇을 등록할 때 MassRobotics 신원 보고의 제조사명·모델·일련번호나 VDA 5050 헤더의 manufacturer·serialNumber 를 감사 기록의 주체 식별자로 쓰면, 이후 연동 오류와 변경 이력을 제조사별로 귀속할 수 있을 것으로 보인다. | ref-253, ref-051 | 아니오 | low | 2026-09-25 | 입고 / 수행 자원 | — |
| f28 | [추정] | 연계 대상: VDA 5050 이 범위 밖으로 둔 기능·시스템 안전과 로봇의 위치 추정·주행 실행은 제조사 쪽이며, 28. 표준·상호운용성·다사업자 거버넌스에서 ROP 몫은 인터페이스 판·적합성·책임 경계를 정하고 확인하는 쪽으로 보인다. | ref-031 | 아니오 | low | 2026-09-25 | — | — |
| f29 | [사실] | VDA 5050 공식 저장소 main 브랜치 명세는 3.0.0 판이며 문서 머리에 발행일이 적혀 있지 않아, 3.0.0 발행일 충돌(oq-005)은 명세 원문으로 해소되지 않는다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f30 | [추정] | 28. 표준·상호운용성·다사업자 거버넌스는 규격 판·책임 분리로 9. 로봇·제조사 관제 연동, 적합성 시험으로 23. 시험·형식 검증·벤치마크, 판 이행으로 24. 자산·소프트웨어 수명주기 관리, 감사 추적으로 26. 사이버보안·접근권한·개인정보, 통합자 위험성평가로 25. 안전·위험 관리, 승강기 연동 표준으로 10. 설비·건물 시스템 연동과 맞물리는 것으로 보인다. | ref-031, ref-004, ref-712, ref-715, ref-560, ref-717 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-407 | gpue (GitHub) | vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/gpue/vda5050-sim | 예 |
| ref-408 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/ekusiadadus/vda5050-lab | 예 |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 2026-04 | 벤더 문서 | low | 2026-09-25 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 예 |
| ref-704 | VDA / VDMA / KIT IFL (VDA5050 GitHub) | VDA5050/VDA5050 — README | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050 | 아니오 |
| ref-253 | MassRobotics | AMR_Interop_Standard — MassRobotics AMR Interoperability Standard (README, JSON schema) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard | 예 |
| ref-706 | Semantic Versioning (Tom Preston-Werner, semver.org) | Semantic Versioning 2.0.0 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://semver.org/spec/v2.0.0.html | 아니오 |
| ref-707 | European Union (EUR-Lex) | Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act) | 2023-12-13 | 정부·연구기관 | medium | 2026-09-25 | https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng | 예 |
| ref-708 | 국가법령정보센터(산업통상자원부) | 산업 디지털 전환 촉진법 (법률 제18692호) | 2022-01-04 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104) | 예 |
| ref-709 | 소프트웨어정책연구소(SPRi) | 산업 디지털 전환 촉진법의 의미와 시사점 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://spri.kr/posts/view/23480?code=industry_trend | 예 |
| ref-710 | Open Source Robotics Alliance (Open Robotics) | osra-policies-and-procedures — README | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/openrobotics/osra-policies-and-procedures | 아니오 |
| ref-711 | Open Source Robotics Alliance | Charter of the Open Source Robotics Alliance Project 'Open-RMF' | 2024-03 | 오픈소스 문서 | medium | 2026-09-25 | https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf | 예 |
| ref-712 | OPC Foundation | How to Certify - OPC Foundation | 미확인 | 표준 | medium | 2026-09-25 | https://opcfoundation.org/certification/how-to-certify/ | 예 |
| ref-713 | IETF (RFC Editor) | RFC 9745: The Deprecation HTTP Response Header Field | 미확인 | 표준 | medium | 2026-09-25 | https://www.rfc-editor.org/info/rfc9745/ | 예 |
| ref-560 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 2025-02 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/73934.html | 예 |
| ref-715 | IEC | IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample) | 2013-08 | 표준 | medium | 2026-09-25 | https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf | 예 |
| ref-716 | ISO/IEC | ISO/IEC 20000-1:2018 - Information technology — Service management — Part 1: Service management system requirements | 2018 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/70636.html | 예 |
| ref-717 | 대한민국 정책브리핑(산업통상자원부 국가기술표준원) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | 정부·연구기관 | medium | 2026-09-25 | https://korea.kr/news/pressReleaseView.do?newsId=156480155 | 예 |
| ref-718 | 한국지능형로봇표준포럼(KOROS) | KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 | 2025 | 표준 | medium | 2026-09-25 | http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절: f21(분류 원문 질문, 추정), f1·f3(표준 기구는 구속력·지원 의무 없음), f17·f18(데이터 권리 법제) / 4절: f6(의미적 버전 관리), f7(폐기 예고), f22(감사 추적), f23(서비스 수준 관리), f18(산업데이터) / 5절: f26(출하·예외·성과), f27(입고·수행 자원) / 6절: f4·f5·f6·f7·f8(변경 정책), f13·f14·f15(적합성 시험·인증, f15 벤더 주장 병기), f19·f24 / 7절: f1·f2·f4·f5·f29(VDA 5050, 트랙 반영 제안 2026-09-25-02 의 3.0.0 판 확인분), f9·f10(MassRobotics, 2026-09-25-02 f13 확인분), f11·f12(Open-RMF·OSRA), f13(OPC UA 인증), f16·f25(국내 단체표준·KS), f17·f18·f20·f22·f23 / 8절: f14 근거 도구 / 9절: f21·f24(직접), f28('연계 대상') / 10절: f30 / 11절: oq-005·055·091·096·041·026 유지와 open_questions_new 4건. 다음 실행 후보: 트랙 반영 제안 12건 중 IEEE 1872·AAS·ECLASS·IEC CDD·IDTA·ISO 22166·IFC·IndoorGML·ISO 19164·LIF·CAD 레이어·SHACL·IDS 관련(2026-09-25-11·16·19·28·35·36·41·44·47·53·54)은 출처 메타데이터가 입력에 없어 이번에 재확인하지 못했다. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 의미적 버전 관리 | Semantic Versioning (SemVer) | 공개 API 를 선언하고 호환되지 않는 변경·하위 호환 기능 추가·하위 호환 수정을 각각 MAJOR·MINOR·PATCH 번호로 올려 변경의 호환성을 판 번호로 알리는 규칙이다. |
| 서비스 수준 협약 | Service Level Agreement (SLA) | 서비스 제공자와 고객이 가용성·응답 시간 같은 측정 가능한 서비스 목표와 미달 시 처리 방식을 합의해 문서로 정한 것이다. |
| 감사 추적 | Audit Trail | 누가 언제 무엇을 했는지를 시간 순서로 남긴 변경·접근·명령 기록으로, 사후에 책임과 원인을 확인하는 데 쓴다. |
| 산업데이터 | Industrial Data | 한국 산업디지털전환촉진법에서 산업 활동 과정에서 생성·활용되는 데이터로, 상당한 투자로 이를 생성한 자에게 사용·수익 권리가 인정된다. |

## 열린 질문

새로 생긴 질문:

- ROP 사업자·로봇 제조사·현장 운영사가 함께 만든 로봇 운행·상태 데이터의 사용·수익 권리를 산업디지털전환촉진법의 공동 생성 규정에 따라 계약에서 어떻게 나누는가, 국내 로봇 관제 계약 사례가 있는가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f18 | 종류: 일반
- EU 데이터법의 데이터 공유 의무가 이종 로봇 플릿에서 제조사가 ROP 사업자(제3자)에게 로봇 사용 데이터를 제공해야 하는 근거가 되는가, 된다면 그 범위는 무엇인가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스, 9. 로봇·제조사 관제 연동 | 근거: f17 | 종류: 일반
- KOROS 1148-8:2025 의 상호운용성 시험 절차는 어떤 시험 항목을 두며, 물류 로봇 관제 연동의 적합성 시험 기준으로 쓸 수 있는가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스, 23. 시험·형식 검증·벤치마크 | 근거: f16 | 종류: 일반
- 이종 플릿 현장에서 ROP 가 고객과 맺는 가용성·응답 시간 목표를 제조사 관제·설비업체의 서비스 수준 목표와 어떻게 연쇄해 맞추며, 공개된 계약 구조나 사례가 있는가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스, 20. 예외 복구·재계획·업무 연속성 | 근거: f24 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 21 · 교차 확인: 0
- 예산 사용량: 검색 18회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처이거나 같은 기관 출처 쌍: f1 은 VDA 명세·README, f12 는 OSRA 헌장·정책 저장소, f5 는 VDA 명세·스키마)
    - f18 검색 요약 문구가 ref-708·ref-709 중 어느 출처에서 왔는지 구분 불가
    - f17 EU 데이터법의 적용 개시일(2025-09-12)은 법률사무소 검색 요약에만 있어 넣지 않음
    - f25 로봇 엘리베이터 탑승 KS 의 번호·세부 메시지 미확인(oq-041 미해결)
    - f16 KOROS 1148-8:2025 시험 항목과 ISO 22166 계열 관계 미확인
    - f15 OTTO VDA 5050 인증의 시험 항목·주체 미확인(벤더 주장)
    - ref-704·ref-253·ref-706·ref-709·ref-710·ref-712·ref-713 발행일 미확인
    - oq-005 VDA 5050 3.0.0 발행일은 명세 원문에 날짜가 없어 해소 못 함(f29)
    - oq-055 VDA 5050 공식 적합성 시험 부재는 읽은 명세·README 범위에서만 확인(f14), 해결 제안하지 않음
- 범위 경계 위반 의심:
    - f28: 기능·시스템 안전과 로봇 주행 실행은 분류 원문 9장 로봇 자체 지능·제어 경계라 '연계 대상:' 표시
    - f25: 승강기 안전기준·제어는 시설·설비 제어 경계라 표준 존재만 기술하고 10. 설비·건물 시스템 연동과의 연결로 제안
    - f20: ISO 10218-2 는 산업용 로봇 셀 표준이라 물류 이동로봇 적용은 미확인으로 명시
    - f17·f18·f19: 법 해석은 ROP 직접 범위가 아니며 계약 조건으로 반영할 과제로만 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: ref-031(VDA5050_EN.md), ref-051(state.schema), ref-004(rmf-core.md), ref-704(VDA5050 README), ref-253(MassRobotics README·JSON 스키마), ref-706(semver.md), ref-710(OSRA P&P README). 나머지 14건은 검색 요약 기준 원문 미열람(신뢰도 상한 medium). 원문을 연 출처가 있어도 공통 규칙 0절 6항에 따라 high 는 주지 않았다. 신규 출처 15건(ref-704~ref-718, 예약 구간 안)으로 신규 출처 상한에 도달해 실외이동로봇 운행안전인증(KIRIA)·국내 로봇 표준화 로드맵 논문은 넣지 못했다. 재사용 6건(ref-004·031·051·407·408·608)은 이전 브리프·역할 규칙 예시의 값을 썼다. 트랙 반영 제안 12건 가운데 VDA 5050 3.0.0 판(2026-09-25-02)과 MassRobotics(2026-09-25-02 f13)는 f29·f9·f10 으로 확인했고, 나머지(IEEE 1872·AAS·ECLASS·IEC CDD·IDTA·ISO 22166·IFC·IndoorGML·ISO 19164·VDMA LIF·CAD 레이어 표준·SHACL·IDS)는 해당 ref id 의 메타데이터가 입력에 없어 이번 실행에서 재확인하지 못하고 다음 실행 후보로 남겼다. 한국 자료: 산업디지털전환촉진법(ref-708), SPRi(ref-709), 국가기술표준원 보도자료(ref-717), KOROS 단체표준(ref-718). 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 27. AI·학습·적응과 모델 운영 관련 주장 없음. 정정 요청 없음. 해결된 열린 질문 없음.
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
…(발췌: 전체 207,642자 중 앞 8,514자)
```

### data/source_texts/ref-039.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Supported Tasks in RMF

## Clean Task:

![](images/cleaning_robots.png)

Cleaning robots are becoming increasingly popular in various facilities. While there are many ways of cleaning (vacuuming, mopping, disinfecting, etc) and hence many varieties of cleaning robots, the workflow remains identical across them all. Floor space in facilities is divided into a number of “zones” or sub-regions for cleaning. Each zone has a start and finish location for the robot. In-between these locations, the robot traverses along a special path while performing the cleaning operation.

RMF fully supports the integration of various cleaning robots. Further, RMF can intelligently assign cleaning jobs to available cleaning robots based on capability and available resources, while optimizing overall productivity. Most cleaning robots have a pre-configured cleaning routine for each zone that can be run from a given starting point. RMF’s goal is to guide the robot to this starting point, trigger the execution of the cleaning routine and then guide the robot to a holding waypoint once the cleaning is complete. A `Clean` Task has been designed in RMF to orchestrate this behavior.

The rest of this section provides an overview of the steps necessary to integrate cleaning robots with RMF. The `airport_terminal` example in `rmf_demos` is a useful reference. It showcases the integration of two brands of cleaning robots: `CleanerBotA` and `CleanerBotE` which operate on navigation graphs `Graph 0` and `Graph 4` respectively.

#### Step 1: Defining waypoints for cleaning in Traffic Editor
Two waypoints need to be added to the navigation graph of the robot. The first is the waypoint where the robot should initiate its cleaning routine. In the image below, this point is labelled as `zone_1_start`. Once the robot finishes its cleaning routine, RMF will guide the robot back to this waypoint. Connected to this waypoint, is waypoint `zone_1` that has the `dock_name` property set to its name. This is the waypoint where the robot ends up after its cleaning routine is completed. In the current implementation, it is important to have the names of these waypoints as `<zone_name>_start` and `<zone_name>` respectively. When a robot enters the lane from `zone_1_start` to `zone_1`, the fleet adapter will request the robot to initiate its docking (in this case cleaning) routine. Setting the `dock_name` parameter to `zone_1` will result in the fleet adapter triggering the `RobotCommandHandle::dock()` function. Thus, the user’s implementation of this function should in-turn make an API call to the robot to begin cleaning the specified zone. Once the cleaning process is completed, the `RobotCommandHandle` should trigger the `docking_finished_callback()`.

![](images/clean_traffic_editor.png)

> Note: In order to trigger the `DockPhase`, the direction of the lane is required to be from `<zone_name>_start` to `<zone_name>`.

#### Step 2: Publish DockSummary message
To estimate the resource drain from the cleaning process which is essential for optimal task allocation planning, the fleet adapters require the list of waypoints that the robot will traverse while cleaning.
This information can be summarized in a [DockSummary](https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/DockSummary.msg) message published to `/dock_summary` topic.
The [mock_docker](https://github.com/open-rmf/rmf_demos/blob/283af6d418f5c8d315cc4ca97c95885a12b15f94/rmf_demos/launch/airport_terminal.launch.xml#L97-L102) node is responsible for publishing this information.
It accepts a `yaml` configuration file containing the lists of waypoints for each zone for each fleet which is used to populate the `DockSummary` message.
For the `airport_terminal` demo the file is located [here](https://github.com/open-rmf/rmf_demos/blob/main/rmf_demos_tasks/rmf_demos_tasks/airport_docker_config.yaml)

#### Step 3: Configure fleet adapter to accept clean tasks
The fleet adapter needs to be configured to accept `Clean` type of task. Else, it will not submit a bid for this task to the dispatcher node during task bidding.
If the legacy `full_control` adapter is being used, the [perform_cleaning](https://github.com/open-rmf/rmf_demos/blob/283af6d418f5c8d315cc4ca97c95885a12b15f94/rmf_demos/launch/include/adapters/cleanerBotA_adapter.launch.xml#L52) parameter needs to be set to `true` in the adapter launch file.
For newer fleet adapters, the [FleetUpdateHandle::accept_task_requests()](https://github.com/open-rmf/rmf_ros2/blob/2fe08e328f543fe6a4e0853a60607b5b52015f2a/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/FleetUpdateHandle.hpp#L134) method should be called with an [AcceptTaskRequest](https://github.com/open-rmf/rmf_ros2/blob/2fe08e328f543fe6a4e0853a60607b5b52015f2a/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/FleetUpdateHandle.hpp#L123-L124) callback that returns `true` if a request with TaskProfile.Description.TaskType.TYPE_CLEAN is received.

#### Step 4: Send a Clean request
If the above steps are done correctly, a request to clean a zone can be submitted to RMF via the terminal or RMF_Demo_Panel.
To send a clean request from the terminal, source the workspace with RMF and then:
```
ros2 run rmf_demos_tasks dispatch_clean -cs zone_1 -st 0 --use_sim_time
```
This will submit a request to RMF to clean `zone_1`. The `--use_sim_time` argument is only required when testing in simulation. For more information on sending a clean request:
```
ros2 run rmf_demos_tasks dispatch_clean -h
```

## Delivery Task:
Another common application for mobile robots is performing deliveries within facilities.
A delivery typically involves the robot heading to a pickup location where it gets loaded with items and then navigating to a dropoff location where the items are unloaded.
At the pickup and dropoff sites, the mobile robot may have to interface with robotic arms, conveyors or other automation systems. We term systems that load items as `dispensers` and those that unload as `ingestors`.

To integrate these systems with RMF core systems, a set of [dispenser](https://github.com/open-rmf/rmf_internal_msgs/tree/main/rmf_dispenser_msgs/msg) and [ingestor](https://github.com/open-rmf/rmf_internal_msgs/tree/main/rmf_ingestor_msgs/msg) messages are defined.
Despite their names, these messages are sufficiently general enough to be used by any other system that perform similar actions.

A `Delivery` task is designed in RMF which guides the mobile robot to the pickup location where the dispenser is located. Once here, its `rmf_fleet_adapter` publishes a `DispenserRequest` message which the workcell receives and begins processing.
When the loading is successful, the dispenser publishes a `DispenserResult` message with `SUCCESS` status.
The `rmf_fleet_adapter` then guides the robot to the dropoff waypoint where the ingestor is located.
Here, a similar exchange of messages ensures. The `rmf_fleet_adapter` publishes an `IngestorRequest` message which instructs the ingestor to unload its payload. Upon completion, it publishes an `IngestorResult` message with a `SUCCESS` status.

To learn how to setup a simulation with dispensers and ingestors, see [Simulation](./simulation.md)

The fleet adapter needs to be configured to accept `Delivery` type of task. Else, it will not submit a bid for this task to the dispatcher node during task bidding.
If the legacy `full_control` adapter is being used, the [perform_deliveries](https://github.com/open-rmf/rmf_demos/blob/283af6d418f5c8d315cc4ca97c95885a12b15f94/rmf_demos/launch/include/adapters/deliveryRobot_adapter.launch.xml#L45) parameter needs to be set to `true` in the adapter launch file.
For newer fleet adapters, the [FleetUpdateHandle::accept_task_requests()](https://github.com/open-rmf/rmf_ros2/blob/2fe08e328f543fe6a4e0853a60607b5b52015f2a/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/FleetUpdateHandle.hpp#L134) method should be called with an [AcceptTaskRequest](https://github.com/open-rmf/rmf_ros2/blob/2fe08e328f543fe6a4e0853a60607b5b52015f2a/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/FleetUpdateHandle.hpp#L123-L124) callback that returns `true` if a request with TaskProfile.Description.TaskType.TYPE_DELIVERY is received.

To submit a `Delivery` request, the `dispatch_delivery` script in `rmf_demos_tasks` can be utilized.
```
ros2 run rmf_demos_tasks dispatch_delivery -h
usage: dispatch_delivery [-h] -p PICKUP -pd PICKUP_DISPENSER -d DROPOFF -di DROPOFF_INGESTOR
                         [-st START_TIME] [-pt PRIORITY] [--use_sim_time]

optional arguments:
  -h, --help            show this help message and exit
  -p PICKUP, --pickup PICKUP
                        Start waypoint
  -pd PICKUP_DISPENSER, --pickup_dispenser PICKUP_DISPENSER
                        Pickup dispenser name
  -d DROPOFF, --dropoff DROPOFF
                        Finish waypoint
  -di DROPOFF_INGESTOR, --dropoff_ingestor DROPOFF_INGESTOR
                        Dropoff ingestor name
  -st START_TIME, --start_time START_TIME
                        Start time from now in secs, default: 0
  -pt PRIORITY, --priority PRIORITY
                        Priority value for this request
  --use_sim_time        Use sim time, default: false
```
…(발췌: 전체 13,499자 중 앞 9,234자)
````

### data/source_texts/ref-051.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "state",
    "description": "State of the mobile robot.",
    "subtopic": "/state",
    "type": "object",
    "required": [
        "headerId",
        "timestamp",
        "version",
        "manufacturer",
        "serialNumber",
        "orderId",
        "orderUpdateId",
        "lastNodeId",
        "lastNodeSequenceId",
        "nodeStates",
        "edgeStates",
        "driving",
        "actionStates",
        "instantActionStates",
        "powerSupply",
        "operatingMode",
        "errors",
        "safetyState"
    ],
    "properties": {
        "headerId": {
            "type": "integer",
            "description": "headerId of the message. The headerId is defined per topic and incremented by 1 with each sent (but not necessarily received) message."
        },
        "timestamp": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp in ISO8601 format (YYYY-MM-DDTHH:mm:ss.fffZ).",
            "examples": [
                "1991-03-11T11:40:03.123Z"
            ]
        },
        "version": {
            "type": "string",
            "description": "Version of the protocol [Major].[Minor].[Patch]",
            "examples": [
                "1.3.2"
            ]
        },
        "manufacturer": {
            "type": "string",
            "description": "Manufacturer of the mobile robot"
        },
        "serialNumber": {
            "type": "string",
            "description": "Serial number of the mobile robot."
        },
        "maps":{
            "type": "array",
            "description": "Array of map-objects that are currently stored on the mobile robot.",
            "items": {
				"$ref": "#/definitions/map"
			}
        },
        "zoneSets":{
            "type": "array",
            "description": "Array of zoneSet objects that are currently stored on the mobile robot.",
            "items": {
				"$ref": "#/definitions/zoneSet"
			}
        },
        "orderId": {
            "type": "string",
            "description": "Unique order identification of the current order or the previous finished order. The orderId is kept until a new order is received. Empty string (\"\") if no previous orderId is available."
        },
        "orderUpdateId": {
            "type": "integer",
            "description": "Order Update Identification to identify that an order update has been accepted by the mobile robot. 0 if no previous orderUpdateId is available."
        },
        "lastNodeId": {
            "type": "string",
            "description": "Node ID of last reached node or, if mobile robot is currently on a node, current node (e.g., \"node7\"). Empty string (\"\") if no lastNodeId is available."
        },
        "lastNodeSequenceId": {
            "type": "integer",
            "description": "sequenceId of the last reached node or, if the mobile robot is currently on a node, sequenceId of current node. 0 if no lastNodeSequenceId is available."
        },
		"nodeStates": {
            "type": "array",
            "description": "Array of nodeState-Objects, that need to be traversed for fulfilling the order. Empty list if idle.",
            "items": {
                "$ref": "#/definitions/nodeState"
            }
        },
        "edgeStates": {
            "type": "array",
            "description": "Array of edgeState-Objects, that need to be traversed for fulfilling the order, empty list if idle.",
            "items": {
				"$ref": "#/definitions/edgeState"
			}
        },
        "plannedPath": {
            "$ref": "#/definitions/plannedPath"
        },
        "intermediatePath": {
            "$ref": "#/definitions/intermediatePath"
        },
        "mobileRobotPosition": {
            "$ref": "#/definitions/mobileRobotPosition"
        },
        "velocity": {
            "type": "object",
            "description": "The mobile robot's velocity in mobile robot coordinates",
            "properties": {
                "vx": {
                    "type": "number",
                    "description":"The mobile robot's velocity in its x direction",
                    "unit": "m/s"
                },
                "vy": {
                    "type": "number",
                    "description":"The mobile robot's velocity in its y direction",
                    "unit": "m/s"
                },
                "omega": {
                    "type": "number",
                    "description":"The mobile robot's turning speed around its z axis.",
                    "unit": "rad/s"
                }
            }
        },
        "loads": {
            "type": "array",
            "description": "Loads, that are currently handled by the mobile robot. Optional: If mobile robot cannot determine load state, leave the array out of the state. If the mobile robot can determine the load state, but the array is empty, the mobile robot is considered unloaded.",
            "items": {
                "$ref": "#/definitions/load"
            }
        },
        "driving": {
            "type": "boolean",
            "description": "True: indicates that the mobile robot is driving and/or rotating. Other movements of the mobile robot (e.g., lift movements) are not included here.\nFalse: indicates that the mobile robot is neither driving nor rotating."
        },
        "paused": {
            "type": "boolean",
            "description": "True: mobile robot is currently in a paused state, either because of the push of a physical button on the mobile robot or because of an instantAction. The mobile robot can resume the order.\nFalse: The mobile robot is currently not in a paused state."
        },
        "newBaseRequest": {
            "type": "boolean",
            "description": "True: mobile robot is almost at the end of the base and will reduce speed if no new base is transmitted. Trigger for fleet control to send new base\nFalse: no base update required."
        },
		"zoneRequests": {
            "description": "Array of zoneRequest objects that are currently active on the mobile robot. Empty array if no zone requests are active.",
            "type": "array",
            "items": {
				"$ref": "#/definitions/zoneRequest"
            }
        },
        "edgeRequests": {
            "description": "Array of edgeRequest objects that are currently active on the mobile robot. Empty array if no edge requests are active.",
            "type": "array",
            "items": {
				"$ref": "#/definitions/edgeRequest"
            }
        },
        "distanceSinceLastNode": {
            "type": "number",
            "description": "Used by line guided vehicles to indicate the distance it has been driving past the lastNodeId. Distance is in meters."
        },
        "actionStates": {
            "type": "array",
            "description": "Array of the current actions and the actions which are yet to be finished. This may include actions from previous nodes that are still in progress\nWhen an action is completed, an updated state message is published with actionStatus set to finished and if applicable with the corresponding resultDescriptor. The actionStates are kept until a new order is received.",
            "items": {
                "$ref": "#/definitions/actionState"
            }
        },
        "instantActionStates": {
            "type": "array",
            "description": "Array of all instant action states that the mobile robot received. Empty array if the mobile robot has not received any instant actions. Instant actions are kept in the state until restart or action clearInstantActions is executed.",
            "items": {
                "$ref": "#/definitions/actionState"
            }
        },
        "zoneActionStates": {
            "type": "array",
            "description": "Array of all zone actions that are in an end state or are currently running; sharing upcoming actions is optional. Zone action states are kept in the state message until restart or action clearZoneActions is executed.",
            "items": {
                "$ref": "#/definitions/actionState"
            }
        },
        "powerSupply": {
            "$ref": "#/definitions/powerSupply"
        },
        "operatingMode": {
            "type": "string",
            "description": "Current operating mode of the mobile robot.",
            "enum": [
                "STARTUP",
                "AUTOMATIC",
                "SEMIAUTOMATIC",
                "INTERVENED",
                "MANUAL",
                "SERVICE",
                "TEACH_IN"
            ]
        },
        "errors": {
            "type": "array",
            "description": "Array of error-objects. All active errors of the mobile robot should be in the list. An empty array indicates that the mobile robot has no active errors.",
            "items": {
				"$ref": "#/definitions/error"
            }
        },
        "information": {
            "type": "array",
            "description": "Array of info-objects. An empty array indicates, that the mobile robot has no information. This should only be used for visualization or debugging – it must not be used for logic in fleet control.",
…(발췌: 전체 34,440자 중 앞 9,285자)
```

### data/source_texts/ref-079.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Traffic Editor

This section describes the traffic-editor GUI and simulation tools.

## Introduction and Objectives

Traffic management of heterogeneous robot fleets is non-trivial. One of the
challenges with coordinated management arises from varying semantics in
information models used across fleets. Representations of waypoints, lanes,
charging/docking stations, restricted zones, infrastructure  systems such as
doors & lifts, among others, are subject to vendor's discretion. However,
standardized conventions that convey the capabilities and intentions of fleets
in a shared facility are quintessential for planning. Multi-agent participants
in other modes of transportation such as roadways collectively adhere to a set
of rules and conventions which minimize chaos. More importantly, they allow for
a new participant to readily integrate into the system by following the
prescribed rules. Existing agents can accommodate the new participant as its
behavior is apparent.

Traffic conventions for multi-robot systems do not exist.
The objective of the `traffic_editor` is to fill this gap by expressing the
intentions of various fleets in a standardized, vendor neutral manner through a
graphical interface. Collated traffic information from different fleets can then
be exported for planning and control. A secondary objective and benefit of the
`traffic_editor` is to facilitate generation of 3D simulation worlds which
accurately reflect physical environments.

## Overview

The `traffic_editor` [repository](https://github.com/open-rmf/rmf_traffic_editor) is home to the `traffic_editor` GUI and tools to auto-generate simulation worlds from GUI output.
The GUI is an easy-to-use interface which can create and annotate 2D floor plans with robot traffic along with building infrastructure information.
Often times, there are existing floor plans of the environment, such as architectural drawings, which simplify the task and provide a "reference" coordinate system for vendor-specific maps.
For such cases, `traffic-editor` can import these types of "backgroud images" to serve as a canvas upon which to draw the intended robot traffic maps, and to make it easy to trace the important wall segments required for simulation.

The `traffic_editor` GUI projects are stored as `yaml` files with `.building.yaml` file extensions.
Although the typical workflow uses the GUI and does not require hand-editing the `yaml` files directly, we have used a `yaml` file format to make it easy to parse using custom scripting if needed.
Each `.building.yaml` file includes several attributes for each level in the site as annotated by the user.
An empty `.building.yaml` file appears below.
The GUI tries to make it easy to add and update content to these file.

```yaml
levels:
  L1:
    doors:
      - []
    drawing:
      filename:
    fiducials:
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    floors:
      - parameters: {}
        vertices: []
    lanes:
      - []
    layers:
      {}
    measurements:
      - []
    models:
      -{}
    vertices:
      {}
    walls:
      {}
lifts:
  {}
name: building

```

## GUI Layout

The layout of the `traffic_editor` includes a `Toolbar`, a `Working Area` and a `Sidebar` as seen in the figure below:

![Traffic Editor GUI](images/traffic_editor/layout.png)

The toolbar contains a variety of tools to support actions such as setting the scale of the drawing, aligning levels for multi-level scenarios, adding virtual models to simulated environments, adding robot traffic lanes, simulated flooring, and so on.

As usual in a modern GUI, the top Toolbar contains a variety of tools to interact with items in the main Working Area.
This document will introduce and explain the tools as an example project is created.
However, the first three tools in the toolbar are commonly found in 2D drawing tools, and should behave as expected:

|                    Icon                           |  Name  | Shortkey |               Function               |
|:-------------------------------------------------:|:------:|:--------:|:------------------------------------:|
| ![Select icon](images/traffic_editor/icons/select.svg) | Select |   `Esc`  | Select an entity in the `Working Area` |
|  ![Move icon](images/traffic_editor/icons/move.svg)    |  Move  |    `m`   |  Move an entity in the `Working Area`  |
| ![Rotate icon](images/traffic_editor/icons/rotate.svg) | Rotate |    `r`   | Rotate an entity in the `Working Area` |

The `Working Area` is where the levels, along with their annotations, are rendered.
The user is able to zoom via the mouse scroll wheel, and pan the view by pressing the scroll wheel and moving the mouse cursor.

The `Sidebar` on the right side of the window contains multiple tabs with various functionalities:
* **levels:** to add a new level to the building. This can be done from scratch or by importing a floor plan image file.
* **layers:** to overlap other images such as lidar maps over the level
* **lifts:** to configure and add lifts to the building
* **traffic:** to select which "navigation graph" is currently being edited, and toggle which graph(s) are being rendered.

## Annotation Guide
This section walks through the process of annotating facilities while highlighting the capabilities of the `traffic_editor` GUI.

To create a new traffic editor `Building` file, launch the traffic editor from a terminal window (first sourcing the workspace if `traffic-editor` is built from source).
Then, click `Building -> New...` and choose a location and filename for your `.building.yaml` file.

### Adding a level
A new level in the building can be added by clicking the `Add` button in the `levels` tab of the `Sidebar`.
The operation will open a dialog box where the `name`, `elevation` (in meters) and path to a 2D `drawing` file (`.png`) can be specified.
In most use cases, the floor plan for the level is used as the drawing.
If unspecified, the user may explicitly enter dimensions of the level in the fields provided.

![Add a level dialog](images/traffic_editor/add_level.png)

In the figure above, a new level `L1` at `0m` elevation and a floor plan have been added as reflected in the `levels` tab.
A default scale `1px = 5cm` is applied.
The actual scale can be set by adding a measurement.
Any offsets applied to align levels will be reflected in the `X` and `Y` columns.
Saving the project will update the `tutorial.building.yaml` files as seen below:
```yaml
levels:
  L1:
    drawing:
      filename: office.png
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    layers:
      {}
lifts:
  {}
name: building
```
### Adding a vertex
|                    Icon                    | Shortkey |
|:------------------------------------------:| :-------:|
| ![Vertex icon](images/traffic_editor/icons/vertex.svg)| `v` |
…(발췌: 전체 28,978자 중 앞 6,859자)
````

### data/source_texts/ref-105.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# FLEET CONFIG =================================================================
# RMF Fleet parameters

rmf_fleet:
  name: "tinyRobot"
  limits:
    linear: [0.5, 0.75] # velocity, acceleration
    angular: [0.6, 2.0] # velocity, acceleration
  profile: # Robot profile is modelled as a circle
    footprint: 0.3 # radius in m
    vicinity: 0.5 # radius in m
  reversible: True # whether robots in this fleet can reverse
  battery_system:
    voltage: 12.0 # V
    capacity: 24.0 # Ahr
    charging_current: 5.0 # A
  mechanical_system:
    mass: 20.0 # kg
    moment_of_inertia: 10.0 #kgm^2
    friction_coefficient: 0.22
  ambient_system:
    power: 20.0 # W
  tool_system:
    power: 0.0 # W
  recharge_threshold: 0.10 # Battery level below which robots in this fleet will not operate
  recharge_soc: 1.0 # Battery level to which robots in this fleet should be charged up to during recharging tasks
  publish_fleet_state: 10.0 # Publish frequency for fleet state, ensure that it is same as robot_state_update_frequency
  account_for_battery_drain: True
  task_capabilities: # Specify the types of RMF Tasks that robots in this fleet are capable of performing
    loop: True
    delivery: True
  actions: ["some_action_here"]
  finishing_request: "park" # [park, charge, nothing]
  responsive_wait: True # Should responsive wait be on/off for the whole fleet by default? False if not specified.
  robots:
    tinyRobot1:
        charger: "tinyRobot1_charger"
        responsive_wait: False # Should responsive wait be on/off for this specific robot? Overrides the fleet-wide setting.
    tinyRobot2:
        charger: "tinyRobot2_charger"
        # No mention of responsive_wait means the fleet-wide setting will be used

  robot_state_update_frequency: 10.0 # Hz

fleet_manager:
  prefix: "http://127.0.0.1:8080"
  user: "some_user"
  password: "some_password"

# TRANSFORM CONFIG =============================================================
# For computing transforms between Robot and RMF coordinate systems

# Optional
reference_coordinates:
  L1:
    rmf: [[20.33, -3.156],
          [8.908, -2.57],
          [13.02, -3.601],
          [21.93, -4.124]]
    robot: [[59, 399],
          [57, 172],
          [68, 251],
          [75, 429]]
```

### data/source_texts/ref-216.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Open Navigation's Nav2 Docking Framework

This package contains an automatic robot docking framework & auxiliary tools. It uses plugin `dock` implementations for a particular platform to enable the framework to generalize to robots of many different kinematic models, charging methods, sensor modalities, non-charging dock request needs, and so on. It can also handle a database of many different docking locations and dock models to handle a heterogeneous environment. This task server is designed be called by an application BT or autonomy application to dock once completed with tasks or battery is low -- _not_ within the navigate-to-pose action itself (though `undock` may be called from inside navigate actions!).

This work is sponsored by [NVIDIA](https://www.nvidia.com/en-us/) and created by [Open Navigation LLC](https://opennav.org).

This is split into 4 packages

- `opennav_docking`: Contains the main docking framework
- `opennav_docking_core`: Contains the dock plugin header file to be implemented for each dock type
- `opennav_docking_bt`: Contains behavior tree nodes and example XML files using the docking task server
- `nova_carter_docking`: Contains an implementation using the Docking system with the Nvidia [Nova Carter](https://robotics.segway.com/nova-carter/) Robot platform and dock, available [here](https://github.com/NVIDIA-ISAAC-ROS/nova_carter/tree/main/nova_carter_docking)

![NvidiaxOpenNavigation](./docs/nv_on.png)

[![IMAGE ALT TEXT](./docs/demo.gif)](https://youtu.be/J3ygkehttlg)

Click on the image above to see an extended video of docking in action.

Want to learn more? Checkout the ROSCon 2024 talk on Docking by clicking on the image below!

[![IMAGE ALT TEXT](https://github.com/user-attachments/assets/468bb49c-87de-4c9e-83a8-ad6f14bbd6d3)](https://vimeo.com/1024971348)

## Architecture

The Docking Framework has 5 main components:
- `DockingServer`: The main action server and logic for performing the docking/undocking actions
- `Navigator`: A NavigateToPose action client to navigate the robot to the dock's staging pose if not with the prestaging tolerances
- `DockDatabase`: A database of dock instances in an environment and their associated interfaces for transacting with each type. An arbitrary number of types are supported.
- `Controller`: A spiral-based graceful controller to use for the vision-control loop for docking
- `ChargingDock` and `NonChargingDock`: Plugins that describe the dock and how to transact with it (check if charging, detection, etc). You can find these plugin headers in the `opennav_docking_core` package.

The `ChargingDock` and `NonChargingDock` plugins are the heart of the customizability of the framework to support any type of charging or non-charging dock for any kind of robot. This means you can both dock with charging stations, as well as non-charging infrastructure such as static locations (ex. conveyers) or dynamic locations (ex. pallets). The `DockDatabase` is how you describe where these docks exist in your environment to interact with and any of them may be used in your docking request. For dynamic locations like docking with movable objects, the action request can include an approximate docking location that uses vision-control loops to refine motion into it.

The docking procedure is as follows:
1. Take action request and obtain the dock's plugin and its pose
2. If the robot is not within the prestaging tolerance of the dock's staging pose, navigate to the staging pose
3. Call the dock's plugin `startDetectionProcess()` method to activate any external detection mechanisms.
4. Use the dock's plugin to initially detect the dock (`getRefinedPose`) and return the docking pose.
5. Enter a vision-control loop where the robot attempts to reach the docking pose while it's actively being refined by the vision system.
6. Exit the vision-control loop once contact has been detected or charging has started (if applicable).
7. Wait until charging starts (if applicable) and return success.
8. Call the dock's plugin `stopDetectionProcess()` method to deactivate any external detection mechanisms.

If anywhere this procedure is unsuccessful (before step 8), `N` retries may be made, driving back to the dock's staging pose, and then restarting the process from step 3. If still unsuccessful after retries, it will return a failure code to indicate what kind of failure occurred to the client.

Undocking works more simply:
1. If previously docked, use the known dock information to get the dock type. If not, use the undock action request's indicated dock type
2. Find the staging pose for this dock and back out to that pose
3. Check if successfully backed out to the pose and charging has stopped

## Interfaces

### Docking Action

The docking action can either operate on a dock in the `DockDatabase` or from a dock specified in the docking request. This second option is useful for testing or when dock's locales are not necessarily known in advance.
If `use_dock_id = true`, it uses the `dock_id` field to specify which dock in the database to use.
Else, you must populate the `dock_pose` and `dock_type` fields.

If you wish for the docking server to stage your robot at the the dock's staging pose for you, `navigate_to_staging_pose` must be true.
Else, you can send your robot to this pose and it will be skipped as long as the robot is within the prestaging tolerances.
You may set the maximum time for navigation using `max_staging_time`.

In return, you obtain the `num_retries`, for the number of attempted retries of the action; `success`, if the action worked and the robot is successfully charging; and `error_code` to return a semantically meaningful error code about what kind of error occurred, if any. See `DockRobot.action` for more details.

While the action is performing, you can obtain feedback about the current `state` of docking, how much time `docking_time` has elapsed, and the current number of retries attempted.

### Undocking Action

Undocking is similarly laid out. The action request contains the `dock_type` which is optional if the docking server previously docked the robot at its current dock. Else, it is required so that the undocking action can obtain the staging pose to back out to **if** there are multiple dock plugins specified (else, will use the default).
There is also a maximum undocking time as a timeout for failures to uncouple itself from the dock, `max_undocking_time`.

The result similarly contains `success` and semantic `error_code` with no feedback.

### Reload Database Service

This service exists to potentially reload the dock server's known dock database with a new file of docks after it is loaded. Simply provide the `filepath` to your new set of docks and it shall be done!

## Dock Specification

There are two unique elements to consider in specifying docks: dock _instances_ and dock _plugins_. Dock instances are instances of a particular dock in the map, as the database may contain many known docks (and you can specify which by name you'd like to dock at). Dock plugins are the model of dock that each is an instance of. The plugins contain the capabilities to generically detect and connect to a particular dock model. This separation allows us to efficiently enable many individual docking locations of potentially several different revisions with different attributes.

The **dock plugins** are specified in the parameter file as shown below. If you're familiar with plugins in other Nav2 servers, this should look like a familiar design pattern. Note that there is no specific information about the dock's pose or instances. These are generic attributes about the dock revision (such as staging pose, enable charging command, detection method, etc). You can add additional parameters in the dock's namespace as you choose (for example `timeout`). These can be of both charging and non-charging types.

```
dock_plugins: ["dockv1", "dockv3"]
dockv1:
  plugin: "my_custom_dock_ns::Dockv1"
dockv3:
  plugin: "my_custom_dock_ns::Dockv3"
  timeout: 10.0
```

There are two ways to populate the database of **dock instances** in your environment: through the parameter file or an external file. If you'd like to embed your dock information in your Docking Server config file (if you only have a couple of docks), you may use a similar method as defining the dock plugins, specifying the docks in the ``docks`` parameter. Note that we specify the plugin type and the dock's location `[x, y, theta]` in a particular frame.

```
docks: ['dock1', 'dock2']
dock1:
  type: "dockv3"
  frame: map
  pose: [0.3, 0.3, 0.0]
  id: "kitchen_dock"
dock2:
  type: "dockv1"
  frame: map
  pose: [0.0, 0.0, 0.4]
  id: "42"
```

If you'd prefer to specify the docks using an external file, you may use the `dock_database` parameter to specify the filepath to the yaml file. The file should be laid out like:

```
docks:
  dock1:
    type: "dockv3"
    frame: map
    pose: [0.3, 0.3, 0.0]
    id: "kitchen_dock"
  dock2:
    type: "dockv1"
    frame: map
    pose: [0.0, 0.0, 0.4]
    id: "42"
```

Note that you may leave the `type` to an empty string **if** there is only one type of dock being used. The `frame` will also default to `map` if not otherwise specified. The `type` and `pose` fields are required. Note also that these can be in any frame, not just map (i.e. `odom`, `base_link`, etc) in both the database and action requests. You may also specify the `id` field, for example to select the associated AprilTag. If the dock plugin does not use it, you can leave it unspecified.

## Dock Plugin API

The dock plugin has several key functions to implement. First, there are two
functions related to poses:

 * `getStagingPose`: This function should transform the dock pose into a
   pose for staging into the docking maneuver. Nav2 will be used to move the robot to the staging pose if not already within prestaging tolerances.
 * `getRefinedPose`: This function can be used refine the dock pose using sensors.
   Depending on how the robot can detect the dock, this might use laser scan data
   or camera data.

There are two functions used during dock approach:
…(발췌: 전체 24,257자 중 앞 10,148자)
````

### data/source_texts/ref-228.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Mobile Robot Factsheet",
    "description": "The factsheet provides basic information about a specific mobile robot type series. This information allows comparison of different mobile robot types and can be applied for the planning, dimensioning and simulation of a mobile robot system. The factsheet also includes information about mobile robot communication interfaces which are required for the integration of a mobile robot type series into a VD[M]A-5050-compliant fleet control.",
    "required": [
        "headerId",
        "timestamp",
        "version",
        "manufacturer",
        "serialNumber",
        "typeSpecification",
        "physicalParameters",
        "protocolLimits",
        "protocolFeatures",
        "mobileRobotGeometry",
        "loadSpecification"
    ],
    "subtopic": "/factsheet",
    "type": "object",
    "properties":{
        "headerId": {
            "type": "integer",
            "description": "Header ID of the message. The headerId is defined per topic and incremented by 1 with each sent (but not necessarily received) message.",
            "minimum": 0
        },
        "timestamp": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp in ISO8601 format (YYYY-MM-DDTHH:mm:ss.fffZ).",
            "examples": [
                "1991-03-11T11:40:03.123Z"
            ]
        },
        "version": {
            "title": "Version",
            "type": "string",
            "description": "Version of the protocol [Major].[Minor].[Patch]",
            "examples": [
                "1.3.2"
            ]
        },
        "manufacturer": {
            "type": "string",
            "description": "Manufacturer of the mobile robot"
        },
        "serialNumber": {
            "type": "string",
            "description": "Serial number of the mobile robot"
        },
        "typeSpecification": {
            "type": "object",
            "required": [
                "seriesName",
                "mobileRobotKinematics",
                "mobileRobotClass",
                "maximumLoadMass",
                "localizationTypes",
                "navigationTypes"
            ],
            "description": "These parameters generally specify the class and the capabilities of the mobile robot",
            "properties": {
                "seriesName": {
                    "type": "string",
                    "description": "Free text generalized series name as specified by manufacturer"
                },
                "seriesDescription": {
                    "type": "string",
                    "description": "Free text human readable description of the mobile robot type series"
                },
                "mobileRobotKinematics": {
                    "type": "string",
                    "description": "Simplified description of mobile robots kinematics-type. Extensible enum: DIFFERENTIAL, OMNIDIRECTIONAL, THREE_WHEEL"
                },
                "mobileRobotClass": {
                    "type": "string",
                    "description": "Simplified description of mobile robot class. Extensible enum: FORKLIFT, CONVEYOR, TUGGER, CARRIER"
                },
                "maximumLoadMass": {
                    "type": "number",
                    "description": "Maximum loadable mass",
                    "unit": "kg",
                    "minimum": 0
                },
                "localizationTypes": {
                    "type": "array",
                    "description": "Simplified description of localization type.",
                    "items": {
                        "type": "string",
                        "description": "Simplified description of localization type. Extensible enum: NATURAL, REFLECTOR, RFID, DMC, SPOT, GRID"
                    }
                },
                "navigationTypes": {
                    "type": "array",
                    "description": "List of path planning types supported by the mobile robot, sorted by priority",
                    "items": {
                        "type": "string",
						"description": "Planning type. Extensible enum: PHYSICAL_LINE_GUIDED, VIRTUAL_LINE_GUIDED, FREELY_NAVIGATING"
                    }
                },
                "supportedZones": {
                    "type": "array",
                    "description": "Array of zone types supported by the mobile robot.",
                    "items": {
                        "type": "string",
                        "enum": [
                            "BLOCKED",
                            "LINE_GUIDED",
                            "RELEASE",
                            "COORDINATED_REPLANNING",
                            "SPEED_LIMIT",
                            "ACTION",
                            "PRIORITY",
                            "PENALTY",
                            "DIRECTED",
                            "BIDIRECTED"
                        ]
                    }
                }
            }
        },
        "physicalParameters": {
            "type": "object",
            "required": [
                "minimumSpeed",
                "maximumSpeed",
                "maximumAcceleration",
                "maximumDeceleration",
                "minimumHeight",
                "maximumHeight",
                "width",
                "length"
            ],
            "description": "These parameters specify the basic physical properties of the mobile robot",
            "properties": {
                "minimumSpeed": {
                    "type": "number",
                    "description": "Minimal controlled continuous speed of the mobile robot",
                    "unit": "m/s",
					"minimum": 0.0
                },
                "maximumSpeed": {
                    "type": "number",
                    "description": "Maximum speed of the mobile robot",
                    "unit": "m/s",
					"minimum": 0.0
                },
                "minimumAngularSpeed": {
                    "type": "number",
                    "description": "Minimal controlled continuous rotation speed of the mobile robot",
                    "unit": "rad/s",
					"minimum": 0.0
                },
                "maximumAngularSpeed": {
                    "type": "number",
                    "description": "Maximum rotation speed of the mobile robot",
                    "unit": "rad/s",
					"minimum": 0.0
                },
                "maximumAcceleration": {
                    "type": "number",
                    "description": "Maximum acceleration with maximum load",
                    "unit": "m/s^2",
					"minimum": 0.0
                },
                "maximumDeceleration": {
                    "type": "number",
                    "description": "Maximum deceleration with maximum load",
                    "unit": "m/s^2"
                },
                "minimumHeight": {
                    "type": "number",
                    "description": "Minimum height of mobile robot",
                    "unit": "m"
                },
                "maximumHeight": {
                    "type": "number",
                    "description": "Maximum height of mobile robot",
                    "unit": "m"
                },
                "width": {
                    "type": "number",
                    "description": "Width of the mobile robot",
                    "unit": "m"
                },
                "length": {
                    "type": "number",
                    "description": "Length of the mobile robot",
                    "unit": "m"
                }
            }
        },
        "protocolLimits": {
            "type": "object",
            "required": [
                "maximumStringLengths",
                "maximumArrayLengths",
                "timing"
            ],
            "description": "This JSON-object describes the protocol limitations of the mobile robot. If a parameter is not defined or set to zero then there is no explicit limit for this parameter.",
            "properties": {
                "maximumStringLengths": {
                    "type": "object",
                    "description": "Maximum lengths of strings",
                    "properties": {
                        "maximumMessageLength": {
                            "type": "integer",
                            "description": "Maximum MQTT Message length",
							"minimum": 0
                        },
                        "maximumTopicSerialLength": {
                            "type": "integer",
                            "description": "Maximum length of serial-number part in MQTT-topics. Affected Parameters: order.serialNumber, instantActions.serialNumber, state.SerialNumber, visualization.serialNumber, connection.serialNumber",
							"minimum": 0
                        },
                        "maximumTopicElementLength": {
                            "type": "integer",
                            "description": "Maximum length of all other parts in MQTT-topics. Affected parameters: order.timestamp, order.version, order.manufacturer, instantActions.timestamp, instantActions.version, instantActions.manufacturer, state.timestamp, state.version, state.manufacturer, visualization.timestamp, visualization.version, visualization.manufacturer, connection.timestamp, connection.version, connection.manufacturer",
							"minimum": 0
                        },
                        "maximumIdLength": {
                            "type": "integer",
                            "description": "Maximum length of ID-Strings. Affected parameters: order.orderId, node.nodeId, nodePosition.mapId, action.actionId, edge.edgeId",
							"minimum": 0
                        },
                        "idNumericalOnly": {
                            "type": "boolean",
                            "description": "If true ID-strings need to contain numerical values only"
                        },
                        "maximumLoadIdLength": {
                            "type": "integer",
                            "description": "Maximum length of loadId Strings",
							"minimum": 0
                        }
                    }
                },
                "maximumArrayLengths": {
                    "type": "object",
…(발췌: 전체 45,983자 중 앞 10,474자)
```

### data/source_texts/ref-284.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# Lifts (i.e. Elevators)

## Map requirements

Before a lift can be properly integrated, be sure to draw up the lift locations with the correct lift names and levels on the navigation graph using `traffic_editor`. The instructions to do so can be found in [Traffic Editor](./traffic-editor.md) chapter.

## Integration

Elevator integration will allow RMF to work over multiple levels, resolving conflicts and managing shared resources on a larger scale. Similar to door integration, the basic requirement is that the lift controller accepts commands using a prescribed protocol, `OPC` is one such example.

The elevators will be integrated in a similar fashion as doors as well, relying on a lift node and a lift adapter. The following block diagram shows how each component works with each other:

<img src="images/lifts_block_diagram.png">

The lift node will act as a driver to work with the lift controller. An example of a lift node can be found in this [repository](https://github.com/sharp-rmf/kone_lift_controller). The node will publish its state and receive lift requests over ROS 2, using the messages and topics listed below.

| Message Types | ROS2 Topic | Description |
|---------------|------------|-------------|
| `rmf_lift_msgs/LiftState` | `/lift_states` | State of the lift published by the lift node
| `rmf_lift_msgs/LiftRequest` | `/lift_requests` | Direct requests subscribed by the lift node and published by the lift adapter
| `rmf_lift_msgs/LiftRequest` | `/adapter_lift_requests` | Requests to be sent to the lift adapter/supervisor to request safe operation of lifts |

A lift adapter subscribes to `lift_states` while keeping track of the internal and desired state of the lift in order to prevent it from performing any actions that might interrupt mobile robot or normal operations. The lift adapter performs this task by receiving lift requests from the fleet adapters and the RMF core systems and only relaying the instructions to the lift node if it is deemed appropriate. Any requests sent directly to the lift node, without going through the lift adapter, will also be negated by the lift adapter, to prevent unwanted disruption to mobile robot fleet operations.
```

### data/source_texts/ref-286.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# lift_time records when the information in this message was generated
builtin_interfaces/Time lift_time

string lift_name

string[] available_floors
string current_floor
string destination_floor

uint8 door_state
uint8 DOOR_CLOSED=0
uint8 DOOR_MOVING=1
uint8 DOOR_OPEN=2

uint8 motion_state
uint8 MOTION_STOPPED=0
uint8 MOTION_UP=1
uint8 MOTION_DOWN=2
uint8 MOTION_UNKNOWN=3

# We can only set human or agv mode, but we can read other modes: fire, etc.
uint8[] available_modes
uint8 current_mode
uint8 MODE_UNKNOWN=0
uint8 MODE_HUMAN=1
uint8 MODE_AGV=2
uint8 MODE_FIRE=3
uint8 MODE_OFFLINE=4
uint8 MODE_EMERGENCY=5
# we can add more "read-only" modes as we come across more of them.

# this field records the session_id that has been granted control of the lift
# until it sends a request with a request_type of REQUEST_END_SESSION
string session_id
```

### data/source_texts/ref-312.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
string lift_name
builtin_interfaces/Time request_time

# session_id should be unique at least between different requesters.
# For example, session_id could be the requester's node name.
string session_id

# AGV mode means that the doors are always open when the lift is stopped
# Human mode means that LiftDoorRequest messages must be used to open/close
# the doors explicitly, since they may "time out" and close automatically.
uint8 request_type
uint8 REQUEST_END_SESSION=0
uint8 REQUEST_AGV_MODE=1
uint8 REQUEST_HUMAN_MODE=2

# The destination_floor must be one of the values returned in a LiftState.
string destination_floor

# Explicit door requests are necessary in "human" mode to open/close doors.
# Door requests are not necessary in "AGV" mode, when the doors are always
# held open when the lift cabin is stopped.
uint8 door_state
uint8 DOOR_CLOSED=0
uint8 DOOR_OPEN=2
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

### data/source_texts/ref-536.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
/*
 * Copyright (C) 2019 Open Source Robotics Foundation
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

#ifndef RMF_TRAFFIC__AGV__GRAPH_HPP
#define RMF_TRAFFIC__AGV__GRAPH_HPP

#include <rmf_traffic/Time.hpp>

#include <Eigen/Geometry>

#include <rmf_utils/impl_ptr.hpp>
#include <rmf_utils/clone_ptr.hpp>

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <optional>
#include <iostream>

namespace rmf_traffic {
namespace agv {

//==============================================================================
class Graph
{
public:

  /// Properties related to lifts (elevators) that exist in the graph
  class LiftProperties
  {
  public:
    /// Get the name of the lift.
    const std::string& name() const;

    /// Get the (x, y) location of the lift in RMF canonical coordinates.
    Eigen::Vector2d location() const;

    /// Get the orientation (in radians) of the lift in RMF canonical
    /// coordinates.
    double orientation() const;

    /// Get the dimensions of the lift, aligned with the lift's local (x, y)
    /// coordinates.
    Eigen::Vector2d dimensions() const;

    /// Get whether the specified position, given in RMF canonical coordinates,
    /// is inside the lift. The envelope will expand the footprint of the lift
    /// that is used in the calculation.
    bool is_in_lift(Eigen::Vector2d position, double envelope = 0.0) const;

    /// Constructor
    LiftProperties(
      std::string name,
      Eigen::Vector2d location,
      double orientations,
      Eigen::Vector2d dimensions);

    class Implementation;
  private:
    rmf_utils::impl_ptr<Implementation> _pimpl;
  };
  using LiftPropertiesPtr = std::shared_ptr<LiftProperties>;

  class DoorProperties
  {
  public:
    /// Get the name of the door.
    const std::string& name() const;

    /// Get the start position of the door.
    Eigen::Vector2d start() const;

    /// Get the end position of the door.
    Eigen::Vector2d end() const;

    /// Get the name of the map that this door is on.
    const std::string& map() const;

    /// Check if the line formed by p0 -> p1 intersects this door.
    bool intersects(
      Eigen::Vector2d p0,
      Eigen::Vector2d p1,
      double envelope = 0.0) const;

    /// Constructor
    DoorProperties(
      std::string name,
      Eigen::Vector2d start,
      Eigen::Vector2d end,
      std::string map);

    class Implementation;
  private:
    rmf_utils::impl_ptr<Implementation> _pimpl;
  };
  using DoorPropertiesPtr = std::shared_ptr<DoorProperties>;

  /// Properties assigned to each waypoint (vertex) in the graph
  class Waypoint
  {
  public:
    /// Get the name of the map that this Waypoint exists on.
    const std::string& get_map_name() const;

    /// Set the name of the map that this Waypoint exists on.
    Waypoint& set_map_name(std::string map);

    /// Get the position of this Waypoint
    const Eigen::Vector2d& get_location() const;

    /// Set the position of this Waypoint
    Waypoint& set_location(Eigen::Vector2d location);

    /// Returns true if this Waypoint can be used as a holding point for the
    /// vehicle, otherwise returns false.
    bool is_holding_point() const;

    /// Set whether this waypoint can be used as a holding point for the
    /// vehicle.
    Waypoint& set_holding_point(bool _is_holding_point);

    /// Returns true if this Waypoint is a passthrough point, meaning a planner
    /// should not have a robot wait at this point, even just briefly to allow
    /// another robot to pass. Setting passthrough points reduces the branching
    /// factor of a planner, allowing it to run faster, at the cost of losing
    /// possible solutions to conflicts.
    bool is_passthrough_point() const;

    /// Set this Waypoint to be a passthrough point.
    Waypoint& set_passthrough_point(bool _is_passthrough);

    /// Returns true if this Waypoint is a parking spot. Parking spots are used
    /// when an emergency alarm goes off, and the robot is required to park
    /// itself.
    bool is_parking_spot() const;

    /// Set this Waypoint to be a parking spot.
    Waypoint& set_parking_spot(bool _is_parking_spot);

    /// Returns true if this Waypoint is a charger spot. Robots are routed to
    /// these spots when their batteries charge levels drop below the threshold
    /// value.
    bool is_charger() const;

    /// Set this Waypoint to be a parking spot.
    Waypoint& set_charger(bool _is_charger);

    /// If this waypoint is inside the lift then this will return a pointer to
    /// the properties of the lift. Otherwise this will be a nullptr.
    LiftPropertiesPtr in_lift() const;

    /// Set the properties of the lift that the waypoint is inside of, or
    /// provide a nullptr if it is not inside a lift.
    Waypoint& set_in_lift(LiftPropertiesPtr properties);

    /// The index of this waypoint within the Graph. This cannot be changed
    /// after the waypoint is created.
    std::size_t index() const;

    /// If this waypoint has a name, return a reference to it. If this waypoint
    /// does not have a name, return a nullptr.
    ///
    /// The name of a waypoint can only be set using add_key() or set_key().
    const std::string* name() const;

    /// If this waypoint has a name, the name will be returned. Otherwise it
    /// will return the waypoint index, formatted into a string based on
    /// the index_format argument.
    ///
    /// \param[in] name_format
    ///   If this waypoint has an assigned name, the first instance of "%s"
    ///   within name_format will be replaced with the name of the waypoint. If
    ///   there is no %s in the name_format string, then this function will
    ///   simply return the name_format string as-is when the waypoint has a
    ///   name.
    ///
    /// \param[in] index_format
    ///   If this waypoint does not have an assigned name, the first instance of
    ///   "%d" within the index_format string will be replaced with the
    ///   stringified decimal index value of the waypoint. If there is no "%d"
    ///   in the index_format string, then this function will simply return the
    ///   index_format string as-is when the waypoint does not have a name.
    std::string name_or_index(
      const std::string& name_format = "%s",
      const std::string& index_format = "#%d") const;

    /// Get the mutex group that this waypoint is associated with. An empty
    /// string implies that it is not associated with any mutex group.
    ///
    /// Only one robot at a time is allowed to occupy any waypoint or lane
    /// associated with a particular mutex group.
    const std::string& in_mutex_group() const;

    /// Set what mutex group this waypoint is associated with. Passing in an
    /// empty string will disasscoiate the waypoint from any mutex group.
    Waypoint& set_in_mutex_group(std::string group_name);

    /// Get a merge radius specific to this waypoint, if it has one. The radius
    /// indicates that any robot within this distance of the waypoint can merge
    /// onto this waypoint.
    std::optional<double> merge_radius() const;

    /// Set the merge radius specific to this waypoint.
    Waypoint& set_merge_radius(std::optional<double> value);

    class Implementation;
  private:
    Waypoint();
    rmf_utils::impl_ptr<Implementation> _pimpl;
  };

  /// A class that implicitly specifies a constraint on the robot's orientation.
  class OrientationConstraint
  {
  public:

    /// Make an orientation constraint that requires a specific value for the
    /// orientation.
    static rmf_utils::clone_ptr<OrientationConstraint>
    make(std::vector<double> acceptable_orientations);

    enum class Direction
    {
      Forward,
      Backward,
    };

    /// Make an orientation constraint that requires the vehicle to face forward
    /// or backward.
    static rmf_utils::clone_ptr<OrientationConstraint>
    make(Direction direction, const Eigen::Vector2d& forward_vector);

    /// Apply the constraint to the given homogeneous position.
    ///
    /// \param[in,out] position
    ///   The position which needs to be constrained. The function should modify
    ///   this position such that it satisfies the constraint, if possible.
    ///
    /// \param[in] course_vector
    ///   The direction that the robot is travelling in. Given for informational
    ///   purposes.
    ///
    /// \return True if the constraint is satisfied with the new value of
    /// position. False if the constraint could not be satisfied.
    virtual bool apply(
      Eigen::Vector3d& position,
      const Eigen::Vector2d& course_vector) const = 0;

    /// Clone this OrientationConstraint.
    virtual rmf_utils::clone_ptr<OrientationConstraint> clone() const = 0;

    // Default destructor.
    virtual ~OrientationConstraint() = default;
  };

  /// Add a lane to connect two waypoints
  class Lane
  {
  public:

    /// A door in the graph which needs to be opened before a robot can enter a
    /// certain lane or closed before the robot can exit the lane.
    class Door
    {
    public:

      /// Constructor
      ///
      /// \param[in] name
      ///   Unique name of the door.
      ///
      /// \param[in] duration
      ///   How long the door takes to open or close.
      Door(std::string name, Duration duration);

      /// Get the unique name (ID) of this Door
      const std::string& name() const;

      /// Set the unique name (ID) of this Door
      Door& name(std::string name);

      /// Get the duration incurred by waiting for this door to open or close.
      Duration duration() const;

      /// Set the duration incurred by waiting for this door to open or close.
      Door& duration(Duration duration);

      class Implementation;
    private:
      rmf_utils::impl_ptr<Implementation> _pimpl;
    };

    class DoorOpen : public Door { public: using Door::Door; };
    class DoorClose : public Door { public: using Door::Door; };

    /// A lift door in the graph which needs to be opened before a robot can
    /// enter a certain lane or closed before the robot can exit the lane.
    class LiftSession
    {
    public:

      /// Constructor
      ///
      /// \param[in] lift_name
      ///   Name of the lift that this door belongs to.
      ///
      /// \param[in] floor_name
      ///   Name of the floor that this door belongs to.
      ///
      /// \param[in] duration
      ///   How long the door takes to open or close.
      LiftSession(
        std::string lift_name,
        std::string floor_name,
        Duration duration);

      /// Get the name of the lift that the door belongs to
      const std::string& lift_name() const;

      /// Set the name of the lift that the door belongs to
      LiftSession& lift_name(std::string name);

      /// Get the name of the floor that this door is on
      const std::string& floor_name() const;

      /// Set the name of the floor that this door is on
      LiftSession& floor_name(std::string name);

      /// Get an estimate of how long it will take the door to open or close
      Duration duration() const;

      /// Set an estimate of how long it will take the door to open or close
      LiftSession& duration(Duration duration);

      class Implementation;
    private:
      rmf_utils::impl_ptr<Implementation> _pimpl;
    };

    class LiftSessionBegin : public LiftSession
    {
    public:
      using LiftSession::LiftSession;
    };

    class LiftMove : public LiftSession
    {
    public:
      using LiftSession::LiftSession;
    };

    class LiftDoorOpen : public LiftSession
    {
    public:
      using LiftSession::LiftSession;
    };

    class LiftSessionEnd : public LiftSession
    {
    public:
      using LiftSession::LiftSession;
    };

    class Dock
    {
    public:

      /// Constructor
      ///
      /// \param[in]
      ///   Name of the dock that will be approached
      ///
      /// \param[in]
      ///   How long the robot will take to dock
      Dock(
        std::string dock_name,
        Duration duration);

      /// Get the name of the dock
      const std::string& dock_name() const;

      /// Set the name of the dock
      Dock& dock_name(std::string name);

      /// Get an estimate for how long the docking will take
      Duration duration() const;

      /// Set an estimate for how long the docking will take
      Dock& duration(Duration d);

      class Implementation;
    private:
      rmf_utils::impl_ptr<Implementation> _pimpl;
    };

    class Wait
    {
    public:

      /// Constructor
      ///
      /// \param[in] duration
      ///   How long the wait will be.
      Wait(Duration value);

      /// Get how long the wait will be.
      Duration duration() const;

      /// Set how long the wait will be.
      Wait& duration(Duration value);

      class Implementation;
    private:
      rmf_utils::impl_ptr<Implementation> _pimpl;
    };

    /// A customizable Executor that can carry out actions based on which Event
    /// type is present.
    class Executor
    {
    public:

      using DoorOpen = Lane::DoorOpen;
      using DoorClose = Lane::DoorClose;
      using LiftSessionBegin = Lane::LiftSessionBegin;
      using LiftDoorOpen = Lane::LiftDoorOpen;
      using LiftSessionEnd = Lane::LiftSessionEnd;
      using LiftMove = Lane::LiftMove;
      using Dock = Lane::Dock;
      using Wait = Lane::Wait;

      virtual void execute(const DoorOpen& open) = 0;
      virtual void execute(const DoorClose& close) = 0;
      virtual void execute(const LiftSessionBegin& begin) = 0;
      virtual void execute(const LiftDoorOpen& open) = 0;
      virtual void execute(const LiftSessionEnd& end) = 0;
      virtual void execute(const LiftMove& move) = 0;
      virtual void execute(const Dock& dock) = 0;
      virtual void execute(const Wait& wait) = 0;

      virtual ~Executor() = default;
    };

    class Event;
    using EventPtr = rmf_utils::clone_ptr<Event>;

    /// An abstraction for the different kinds of Lane events
    class Event
    {
    public:

      /// An estimate of how long the event will take
      virtual Duration duration() const = 0;

      template<typename DerivedExecutor>
      DerivedExecutor& execute(DerivedExecutor& executor) const
      {
        return static_cast<DerivedExecutor&>(
          execute(static_cast<Executor&>(executor)));
      }

      /// Execute this event
      virtual Executor& execute(Executor& executor) const = 0;

      /// Clone this event
      virtual EventPtr clone() const = 0;

      virtual ~Event() = default;

      static EventPtr make(DoorOpen open);
      static EventPtr make(DoorClose close);
      static EventPtr make(LiftSessionBegin open);
      static EventPtr make(LiftSessionEnd close);
      static EventPtr make(LiftMove move);
      static EventPtr make(LiftDoorOpen open);
      static EventPtr make(Dock dock);
      static EventPtr make(Wait wait);
    };

    /// A Lane Node wraps up a Waypoint with constraints. The constraints
    /// stipulate the conditions for entering or exiting the lane to reach this
    /// waypoint.
    class Node
    {
    public:

      /// Constructor
      ///
      /// \param waypoint_index
      ///   The index of the waypoint for this Node
      ///
      /// \param event
      ///   An event that must happen before/after this Node is approached
      ///   (before if it's an entry Node or after if it's an exit Node).
      ///
      /// \param orientation
      ///   Any orientation constraints for moving to/from this Node (depending
      ///   on whether it's an entry Node or an exit Node).
      Node(
        std::size_t waypoint_index,
        rmf_utils::clone_ptr<Event> event = nullptr,
        rmf_utils::clone_ptr<OrientationConstraint> orientation = nullptr);

      /// Constructor. The event parameter will be nullptr.
      ///
      /// \param waypoint_index
      ///   The index of the waypoint for this Node
      ///
      /// \param orientation
      ///   Any orientation constraints for moving to/from this Node (depending
      ///   on whether it's an entry Node or an exit Node).
      Node(
        std::size_t waypoint_index,
        rmf_utils::clone_ptr<OrientationConstraint> orientation);

      /// Get the index of the waypoint that this Node is wrapped around.
      std::size_t waypoint_index() const;

      /// Get a reference to an event that must occur before or after this Node
      /// is visited.
      ///
      /// \note Before if this is an entry node or after if this is an exit node
      const Event* event() const;

      /// Set the event that must occur before or after this Node is visited
      Node& event(rmf_utils::clone_ptr<Event> new_event);

      /// Get the constraint on orientation that is tied to this Node.
      const OrientationConstraint* orientation_constraint() const;

      class Implementation;
    private:
      // We make the Lane a friend so it can copy and move the Nodes
      friend class Lane;

      // These constructors are private to make sure a user can't modify the
      // waypoint_index of a Node by copying or moving
      Node(const Node&) = default;
      Node(Node&&) = default;
      Node& operator=(const Node&) = default;
      Node& operator=(Node&&) = default;
      rmf_utils::impl_ptr<Implementation> _pimpl;
    };

    /// The Lane Properties class contains properties that apply across the full
    /// extent of the lane.
    class Properties
    {
    public:

      /// Construct a default set of properties
      /// * speed_limit: nullopt
      /// * mutex_group: ""
      Properties();

      /// Get the speed limit along this lane. If a std::nullopt is returned,
      /// then there is no specified speed limit for the lane.
      std::optional<double> speed_limit() const;

      /// Set the speed limit along this lane. Providing a std::nullopt
      /// indicates that there is no speed limit for the lane.
      Properties& speed_limit(std::optional<double> value);

      /// Get the mutex group that this lane is associated with. An empty string
      /// implies that it is not associated with any mutex group.
      ///
      /// Only one robot at a time is allowed to occupy any waypoint or lane
      /// associated with a particular mutex group.
      const std::string& in_mutex_group() const;

      /// Set what mutex group this lane is associated with. Passing in an
      /// empty string will disassociate the lane from any mutex group.
      Properties& set_in_mutex_group(std::string group_name);

      class Implementation;
    private:
      rmf_utils::impl_ptr<Implementation> _pimpl;
    };

    /// Get the entry node of this Lane. The lane represents an edge in the
    /// graph that goes away from this node.
    Node& entry();

    /// const-qualified entry()
    const Node& entry() const;

    /// Get the exit node of this Lane. The lane represents an edge in the graph
    /// that goes into this node.
    Node& exit();

    /// const-qualified exit()
    const Node& exit() const;

    /// Get the properties of this Lane
    Properties& properties();

    /// const-qualified properties()
    const Properties& properties() const;

    /// Get the index of this Lane within the Graph.
    std::size_t index() const;

    class Implementation;
  private:
    Lane();
    rmf_utils::impl_ptr<Implementation> _pimpl;
  };

  /// Default constructor
  Graph();

  /// Make a new waypoint for this graph. It will not be connected to any other
  /// waypoints until you use make_lane() to connect it.
  ///
  /// \note Waypoints cannot be erased from a Graph after they are created.
  Waypoint& add_waypoint(
    std::string map_name,
    Eigen::Vector2d location);

  /// Get a waypoint based on its index.
  Waypoint& get_waypoint(std::size_t index);

  /// const-qualified get_waypoint()
  const Waypoint& get_waypoint(std::size_t index) const;

  /// Find a waypoint given a key name. If the graph does not have a matching
  /// key name, then a nullptr will be returned.
  Waypoint* find_waypoint(const std::string& key);

  /// const-qualified find_waypoint()
  const Waypoint* find_waypoint(const std::string& key) const;

  /// Add a new waypoint key name to the graph. If a new key name is given, then
  /// this function will return true. If the given key name was already in use,
  /// then this will return false and nothing will be changed in the graph.
  bool add_key(const std::string& key, std::size_t wp_index);

  /// Remove the waypoint key with the given name, if it exists in this Graph.
  /// If the key was removed, this will return true. If the key did not exist,
  /// this will return false.
  bool remove_key(const std::string& key);

  /// Set a waypoint key. If this key is already in the Graph, it will be
  /// changed to the new association.
  ///
  /// This function will return false if wp_index is outside the range of the
  /// waypoints in this Graph.
  bool set_key(const std::string& key, std::size_t wp_index);

  /// Get the map of all keys in this Graph.
  const std::unordered_map<std::string, std::size_t>& keys() const;

  /// Get the number of waypoints in this Graph
  std::size_t num_waypoints() const;

  /// Make a lane for this graph. Lanes connect waypoints together, allowing the
  /// graph to know how the robot is allowed to traverse between waypoints.
  Lane& add_lane(
    const Lane::Node& entry,
    const Lane::Node& exit,
    Lane::Properties properties = Lane::Properties());

  /// Get the lane at the specified index
  Lane& get_lane(std::size_t index);

  /// const-qualified get_lane()
  const Lane& get_lane(std::size_t index) const;

  /// Get the number of Lanes in this Graph.
  std::size_t num_lanes() const;

  /// Get the indices of lanes that come out of the given Waypoint index
  const std::vector<std::size_t>& lanes_from(std::size_t wp_index) const;

  /// Get the indices of lanes that arrive into the given Waypoint index
  const std::vector<std::size_t>& lanes_into(std::size_t wp_index) const;

  /// Get a reference to the lane that goes from from_wp to to_wp if such a lane
  /// exists. If no such lane exists, this will return a nullptr. If multiple
  /// exist, this will return the one that was added most recently.
  Lane* lane_from(std::size_t from_wp, std::size_t to_wp);

  /// const-qualified lane_from()
  const Lane* lane_from(std::size_t from_wp, std::size_t to_wp) const;

  /// Add a known lift to the graph. If this lift has the same name as one
  /// previously added, we will continue to use the same pointer as the original
  /// and override the properties because lift names are expected to be unique.
  LiftPropertiesPtr set_known_lift(LiftProperties lift);

  /// Get all the known lifts.
  std::vector<LiftPropertiesPtr> all_known_lifts() const;

  /// Find a known lift based on its name.
  LiftPropertiesPtr find_known_lift(const std::string& name) const;

  /// Add a known door to the graph. If this door has the same name as one
  /// previously added, we will continue to use the same pointer as the original
  /// and override the properties because door names are expected to be unique.
  DoorPropertiesPtr set_known_door(DoorProperties door);

  /// Get all the known doors.
  std::vector<DoorPropertiesPtr> all_known_doors() const;

  /// Find a known door based on its name.
  DoorPropertiesPtr find_known_door(const std::string& name) const;
…(발췌: 전체 24,127자 중 앞 23,957자)
```

### data/source_texts/ref-537.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

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

#ifndef RMF_FLEET_ADAPTER__AGV__ROBOTUPDATEHANDLE_HPP
#define RMF_FLEET_ADAPTER__AGV__ROBOTUPDATEHANDLE_HPP

#include <rmf_traffic/Time.hpp>
#include <rmf_traffic/agv/Planner.hpp>
#include <rmf_utils/impl_ptr.hpp>
#include <rmf_utils/optional.hpp>

#include <rmf_traffic/schedule/Participant.hpp>

#include <rmf_task/RequestFactory.hpp>

#include <Eigen/Geometry>
#include <nlohmann/json.hpp>

#include <vector>
#include <memory>
#include <functional>

namespace rmf_fleet_adapter {
namespace agv {

//==============================================================================
/// You will be given an instance of this class every time you add a new robot
/// to your fleet. Use that instance to send updates to RoMi-H about your
/// robot's state.
class RobotUpdateHandle
{
public:

  [[deprecated("Use replan() instead")]]
  void interrupted();

  /// Tell the RMF schedule that the robot needs a new plan. A new plan will be
  /// generated, starting from the last position that was given by
  /// update_position(). It is best to call update_position() with the latest
  /// position of the robot before calling this function.
  void replan();

  /// Update the current position of the robot by specifying the waypoint that
  /// the robot is on and its orientation.
  void update_position(
    std::size_t waypoint,
    double orientation);

  /// Update the current position of the robot by specifying the x, y, yaw
  /// position of the robot and one or more lanes that the robot is occupying.
  ///
  /// \warning At least one lane must be specified. If no lane information is
  /// available, then use the update_position(std::string, Eigen::Vector3d)
  /// signature of this function.
  void update_position(
    const Eigen::Vector3d& position,
    const std::vector<std::size_t>& lanes);

  /// Update the current position of the robot by specifying the x, y, yaw
  /// position of the robot and the waypoint that it is moving towards.
  ///
  /// This should be used if the robot has diverged significantly from its
  /// course but it is merging back onto a waypoint.
  void update_position(
    const Eigen::Vector3d& position,
    std::size_t target_waypoint);

  /// Update the current position of the robot by specifying the x, y, yaw
  /// position of the robot and what map the robot is on.
  ///
  /// \warning This function should only be used if the robot has diverged from
  /// the navigation graph somehow.
  ///
  /// We will attempt to merge the robot back onto the navigation graph. The
  /// parameters for this function are passed along to
  /// rmf_traffic::agv::compute_plan_starts().
  void update_position(
    const std::string& map_name,
    const Eigen::Vector3d& position,
    const double max_merge_waypoint_distance = 0.1,
    const double max_merge_lane_distance = 1.0,
    const double min_lane_length = 1e-8);

  /// Update the current position of the robot by specifying a plan start set
  /// for it.
  void update_position(rmf_traffic::agv::Plan::StartSet position);

  /// Set whether this robot uses the parking reservation system. By default this
  /// is false in order to keep the system behavior backwards compatible, but it
  /// is recommended that you turn this on.
  ///
  /// If you are using the EasyFullControl API then you can set this in your
  /// fleet configuration.
  RobotUpdateHandle& use_parking_reservation_system(bool use);

  /// Set the waypoint where the charger for this robot is located.
  /// If not specified, the nearest waypoint in the graph with the is_charger()
  /// property will be assumed as the charger for this robot.
  RobotUpdateHandle& set_charger_waypoint(const std::size_t charger_wp);

  /// Set a finishing request for this robot.
  RobotUpdateHandle& set_finishing_request(rmf_task::ConstRequestFactoryPtr finishing_request);

  /// Set a finishing request for this robot to use the fleet-wide finishing
  /// request.
  RobotUpdateHandle& use_default_finishing_request();

  /// Update the current battery level of the robot by specifying its state of
  /// charge as a fraction of its total charge capacity, i.e. a value from 0.0
  /// to 1.0.
  void update_battery_soc(const double battery_soc);

  /// Use this function to override the robot status. The string provided must
  /// be a valid enum as specified in the robot_state.json schema.
  /// Pass std::nullopt to cancel the override and allow RMF to automatically
  /// update the status. The default value is std::nullopt.
  void override_status(std::optional<std::string> status);

  /// Specify how high the delay of the current itinerary can become before it
  /// gets interrupted and replanned. A nullopt value will allow for an
  /// arbitrarily long delay to build up without being interrupted.
  RobotUpdateHandle& maximum_delay(
    rmf_utils::optional<rmf_traffic::Duration> value);

  /// Get the value for the maximum delay.
  ///
  /// \note The setter for the maximum_delay field is run asynchronously, so
  /// it may take some time for the return value of this getter to match the
  /// value that was given to the setter.
  rmf_utils::optional<rmf_traffic::Duration> maximum_delay() const;

  /// Get the current task ID of the robot, or an empty string if the robot
  /// is not performing any task.
  const std::string current_task_id() const;

  /// Unique identifier for an activity that the robot is performing. Used by
  /// the EasyFullControl API.
  class ActivityIdentifier
  {
  public:

    /// Compare whether two activity handles are referring to the same activity.
    bool operator==(const ActivityIdentifier&) const;

    class Implementation;
  private:
    ActivityIdentifier();
    rmf_utils::unique_impl_ptr<Implementation> _pimpl;
  };
  using ActivityIdentifierPtr = std::shared_ptr<ActivityIdentifier>;
  using ConstActivityIdentifierPtr = std::shared_ptr<const ActivityIdentifier>;

  /// Hold onto this class to tell the robot to behave as a "stubborn
  /// negotiator", meaning it will always refuse to accommodate the schedule
  /// of any other agent. This could be used when teleoperating a robot, to
  /// tell other robots that the agent is unable to negotiate.
  ///
  /// When the object is destroyed, the stubbornness will automatically be
  /// released.
  class Stubbornness
  {
  public:
    /// Stop being stubborn
    void release();

    class Implementation;
  private:
    Stubbornness();
    rmf_utils::impl_ptr<Implementation> _pimpl;
  };

  /// The ActionExecution class should be used to manage the execution of and
  /// provide updates on ongoing actions.
  class ActionExecution
  {
  public:
    /// Update the amount of time remaining for this action.
    /// This does not need to be used for navigation requests.
    void update_remaining_time(rmf_traffic::Duration remaining_time_estimate);

    /// Set task status to underway and optionally log a message (info tier)
    void underway(std::optional<std::string> text);

    /// Set task status to error and optionally log a message (error tier)
    void error(std::optional<std::string> text);

    /// Set the task status to delayed and optionally log a message
    /// (warning tier)
    void delayed(std::optional<std::string> text);

    /// Set the task status to blocked and optionally log a message
    /// (warning tier)
    void blocked(std::optional<std::string> text);

    /// Use this to override the traffic schedule for the agent while it performs
    /// this command.
    ///
    /// If the given trajectory results in a traffic conflict then a negotiation
    /// will be triggered. Hold onto the `Stubbornness` returned by this function
    /// to ask other agents to plan around your trajectory, otherwise the
    /// negotiation may result in a replan for this agent and a new command will
    /// be issued.
    ///
    /// \note Using this will function always trigger a replan once the agent
    /// finishes the command.
    ///
    /// \warning Too many overridden/stubborn agents can cause a deadlock. It's
    ///   recommended to use this API sparingly and only over short distances or
    ///   small deviations.
    ///
    /// \param[in] map
    ///   Name of the map where the trajectory will take place
    ///
    /// \param[in] path
    ///   The path of the agent
    ///
    /// \param[in] hold
    ///   How long the agent will wait at the end of the path
    ///
    /// \return a Stubbornness handle that tells the fleet adapter to not let the
    /// overridden path be negotiated. The returned handle will stop having an
    /// effect after this command execution is finished.
    Stubbornness override_schedule(
      std::string map,
      std::vector<Eigen::Vector3d> path,
      rmf_traffic::Duration hold = rmf_traffic::Duration(0));

    /// Trigger this when the action is successfully finished.
    /// No other functions in this ActionExecution instance will
    /// be usable after this.
    void finished();

    /// Returns false if the Action has been killed or cancelled
    bool okay() const;

    /// Set whether automatic cancellation is turned on for this action.
    ///
    /// When automatic cancellation is on, the task system will believe that the
    /// action is successfully cancelled immediately upon receiving a cancel
    /// signal. By default, automatic cancellation is on (true).
    ///
    /// If your action needs to perform some kind of wind-down or cleanup after
    /// being cancelled, then you should set this to false. At that point you
    /// must ensure that your action implementation is watching okay() to know
    /// if it has been cancelled, and you must trigger finished() when your
    /// wind-down or cleanup is finished.
    void set_automatic_cancel(bool on);

    /// Activity identifier for this action. Used by the EasyFullControl API.
    ConstActivityIdentifierPtr identifier() const;

    class Implementation;
  private:
    ActionExecution();
    rmf_utils::impl_ptr<Implementation> _pimpl;
  };

  /// Signature for a callback to request the robot to perform an action
  ///
  /// \param[in] category
  ///   A category of the action to be performed
  ///
  /// \param[in] description
  ///   A description of the action to be performed
  ///
  /// \param[in] execution
  ///   An ActionExecution object that will be provided to the user for
  ///   updating the state of the action.
  using ActionExecutor = std::function<void(
        const std::string& category,
        const nlohmann::json& description,
        ActionExecution execution)>;

  /// Set the ActionExecutor for this robot
  void set_action_executor(ActionExecutor action_executor);

  /// Submit a direct task request to this manager
  /// \param[in] task_request
  ///   A JSON description of the task request. It should match the
  ///   task_request.json schema of rmf_api_msgs, in particular it must contain
  ///   `category` and `description` properties.
  ///
  /// \param[in] request_id
  ///   The unique ID for this task request.
  ///
  /// \param[in] receive_response
  ///   Provide a callback to receive the response. The response will be a
  ///   robot_task_response.json message from rmf_api_msgs (note: this message
  ///   is not validated before being returned).
  void submit_direct_request(
    nlohmann::json task_request,
    std::string request_id,
    std::function<void(nlohmann::json response)> receive_response);

  /// An object to maintain an interruption of the current task. When this
  /// object is destroyed, the task will resume.
  class Interruption
  {
  public:
    /// Call this function to resume the task while providing labels for
    /// resuming.
    void resume(std::vector<std::string> labels);

    class Implementation;
  private:
    Interruption();
    rmf_utils::unique_impl_ptr<Implementation> _pimpl;
  };

  /// Interrupt (pause) the current task, yielding control of the robot away
  /// from the fleet adapter's task manager.
  ///
  /// \param[in] labels
  ///   Labels that will be assigned to this interruption. It is recommended to
  ///   include information about why the interruption is happening.
  ///
  /// \return a handle for this interruption.
  Interruption interrupt(
    std::vector<std::string> labels,
    std::function<void()> robot_is_interrupted);

  /// Cancel a task, if it has been assigned to this robot
  ///
  /// \param[in] task_id
  ///   The ID of the task to be canceled
  ///
  /// \param[in] labels
  ///   Labels that will be assigned to this cancellation. It is recommended to
  ///   include information about why the cancellation is happening.
  ///
  /// \param[in] on_cancellation
  ///   Callback that will be triggered after the cancellation is issued.
  ///   task_was_found will be true if the task was successfully found and
  ///   issued the cancellation, false otherwise.
  void cancel_task(
    std::string task_id,
    std::vector<std::string> labels,
    std::function<void(bool task_was_found)> on_cancellation);

  /// Kill a task, if it has been assigned to this robot
  ///
  /// \param[in] task_id
  ///   The ID of the task to be canceled
  ///
  /// \param[in] labels
  ///   Labels that will be assigned to this cancellation. It is recommended to
  ///   include information about why the cancellation is happening.
  ///
  /// \param[in] on_kill
  ///   Callback that will be triggered after the cancellation is issued.
  ///   task_was_found will be true if the task was successfully found and
  ///   issued the kill, false otherwise.
  void kill_task(
    std::string task_id,
    std::vector<std::string> labels,
    std::function<void(bool task_was_found)> on_kill);

  enum class Tier
  {
    /// General status information, does not require special attention
    Info,

    /// Something unusual that might require attention
    Warning,

    /// A critical failure that requires immediate operator attention
    Error
  };

  /// An object to maintain an issue that is happening with the robot. When this
  /// object is destroyed without calling resolve(), the issue will be
  /// "dropped", which issues a warning to the log.
  class IssueTicket
  {
  public:

    /// Indicate that the issue has been resolved. The provided message will be
    /// logged for this robot and the issue will be removed from the robot
    /// state.
    void resolve(nlohmann::json msg);

    class Implementation;
  private:
    IssueTicket();
    rmf_utils::unique_impl_ptr<Implementation> _pimpl;
  };

  /// Create a new issue for the robot.
  ///
  /// \param[in] tier
  ///   The severity of the issue
  ///
  /// \param[in] category
  ///   A brief category to describe the issue
  ///
  /// \param[in] detail
  ///   Full details of the issue that might be relevant to an operator or
  ///   logging system.
  ///
  /// \return A ticket for this issue
  IssueTicket create_issue(
    Tier tier, std::string category, nlohmann::json detail);

  // TODO(MXG): Should we offer a "clear_all_issues" function?

  /// Add a log entry with Info severity
  void log_info(std::string text);

  /// Add a log entry with Warning severity
  void log_warning(std::string text);

  /// Add a log entry with Error severity
  void log_error(std::string text);

  /// Toggle the responsive wait behavior for this robot. When responsive wait
  /// is active, the robot will remain in the traffic schedule when it is idle
  /// and will negotiate its position with other traffic participants to
  /// potentially move out of their way.
  ///
  /// Disabling this behavior may be helpful to reduce CPU load or prevent
  /// parked robots from moving or being seen as conflicts when they are not
  /// actually at risk of creating traffic conflicts.
  ///
  /// By default this behavior is enabled.
  void enable_responsive_wait(bool value);

  /// If the robot is holding onto a session with a lift, release that session.
  void release_lift();

  /// A description of whether the robot should accept dispatched and/or direct
  /// tasks.
  class Commission
  {
  public:
    /// Construct a Commission description with all default values.
    /// - accept_dispatched_tasks: true
    /// - accept_direct_tasks: true
    /// - is_performing_idle_behavior: true
    Commission();

    /// Construct a Commission description that accepts no tasks at all.
    /// - accept_dispatch_tasks: false
    /// - accept_direct_tasks: false
    /// - is_performing_idle_behavior: false
    static Commission decommission();

    /// Set whether this commission should accept dispatched tasks.
    Commission& accept_dispatched_tasks(bool decision = true);

    /// Check whether this commission is accepting dispatched tasks.
    bool is_accepting_dispatched_tasks() const;

    /// Set whether this commission should accept direct tasks
    Commission& accept_direct_tasks(bool decision = true);

    /// Check whether this commission is accepting direct tasks.
    bool is_accepting_direct_tasks() const;

    /// Set whether this commission should perform idle behaviors (formerly
    /// referred to as "finishing tasks").
    Commission& perform_idle_behavior(bool decision = true);

    /// Check whether this commission is performing idle behaviors (formerly
    /// referred to as "finishing tasks").
    bool is_performing_idle_behavior() const;

    class Implementation;
  private:
    rmf_utils::impl_ptr<Implementation> _pimpl;
  };

  /// Set the current commission for the robot.
  void set_commission(Commission commission);

  /// Get the current commission for the robot. If the robot has been dropped
  /// from the fleet, this will return Commission::decommission().
  Commission commission() const;

  /// Tell the fleet adapter to reassign all the tasks that have been dispatched
  /// to this robot. To prevent the tasks from being reassigned back to this
  /// robot use .set_commission(Commission::decommission())
  ///
  /// In the current implementation, tasks will only be reassigned to robots
  /// in the same fleet that the task was originally assigned to. This behavior
  /// could change in the future.
  void reassign_dispatched_tasks();

  /// Information about where the lift will be asked to go for a robot.
  class LiftDestination
  {
  public:
    /// Name of the lift that is being used.
    const std::string& lift() const;

    /// Name of the level that the lift will be going to.
    const std::string& level() const;

    class Implementation;
  private:
    LiftDestination();
    rmf_utils::impl_ptr<Implementation> _pimpl;
  };

  /// If this robot has begun a lift session, this will contain information
  /// about where the robot will ask to go, and which lift it intends to use.
  std::optional<LiftDestination> lift_destination() const;

  class Implementation;

  /// This API is experimental and will not be supported in the future. Users
  /// are to avoid relying on these feature for any integration.
  class Unstable
  {
  public:
    /// True if this robot is allowed to accept new tasks. False if the robot
    /// will not accept any new tasks.
    [[deprecated("Use commission instead")]]
    bool is_commissioned() const;

    /// Stop this robot from accepting any new tasks. It will continue to
    /// perform tasks that are already in its queue. To reassign those tasks,
    /// you will need to use the task request API to cancel the tasks and
    /// re-request them.
    [[deprecated("Use set_commission instead")]]
    void decommission();

    /// Allow this robot to resume accepting new tasks.
    [[deprecated("Use set_commission instead")]]
    void recommission();

    /// Get the schedule participant of this robot
    rmf_traffic::schedule::Participant* get_participant();

    /// Change the radius of the footprint and vicinity of this participant.
    void change_participant_profile(
      double footprint_radius,
      double vicinity_radius);

    /// Override the schedule to say that the robot will be holding at a certain
    /// position. This should not be used while tasks with automatic schedule
    /// updating are running, or else the traffic schedule will have jumbled up
    /// information, which can be disruptive to the overall traffic management.
    void declare_holding(
      std::string on_map,
      Eigen::Vector3d at_position,
      rmf_traffic::Duration for_duration = std::chrono::seconds(30));

    /// Get the current Plan ID that this robot has sent to the traffic schedule
    rmf_traffic::PlanId current_plan_id() const;

    using Stubbornness = RobotUpdateHandle::Stubbornness;

    /// Tell this robot to be a stubborn negotiator.
    Stubbornness be_stubborn();

    enum class Decision
    {
      Undefined = 0,
      Clear = 1,
      Crowded = 2
    };

    /// A callback with this signature will be given to the watchdog when the
    /// robot is ready to enter a lift. If the watchdog passes in a true, then
    /// the robot will proceed to enter the lift. If the watchdog passes in a
    /// false, then the fleet adapter will release its session with the lift and
    /// resume later.
    using Decide = std::function<void(Decision)>;

    using Watchdog = std::function<void(const std::string&, Decide)>;

    /// Set a callback that can be used to check whether the robot is clear to
    /// enter the lift.
    void set_lift_entry_watchdog(
      Watchdog watchdog,
      rmf_traffic::Duration wait_duration = std::chrono::seconds(10));

    /// Turn on/off a debug dump of how position updates are being processed
    void debug_positions(bool on);

    /// Cancel a task but keep the task state displayed as completed, if it has
    /// been assigned to this robot
    ///
    /// \param[in] task_id
    ///   The ID of the task to be canceled
    ///
    /// \param[in] labels
    ///   Labels that will be assigned to this cancellation. It is recommended to
    ///   include information about why the cancellation is happening.
    ///
    /// \param[in] on_cancellation
    ///   Callback that will be triggered after the cancellation is issued.
    ///   task_was_found will be true if the task was successfully found and
    ///   issued the cancellation, false otherwise.
    void quiet_cancel_task(
      std::string task_id,
      std::vector<std::string> labels,
      std::function<void(bool task_was_found)> on_cancellation);

  private:
    friend Implementation;
    Implementation* _pimpl;
  };

  /// Get a mutable reference to the unstable API extension
  Unstable& unstable();
  /// Get a const reference to the unstable API extension
  const Unstable& unstable() const;

private:
  RobotUpdateHandle();
  rmf_utils::unique_impl_ptr<Implementation> _pimpl;
};

using RobotUpdateHandlePtr = std::shared_ptr<RobotUpdateHandle>;
using ConstRobotUpdateHandlePtr = std::shared_ptr<const RobotUpdateHandle>;

} // namespace agv
} // namespace rmf_fleet_adapter

#endif // RMF_FLEET_ADAPTER__AGV__ROBOTUPDATEHANDLE_HPP
```
