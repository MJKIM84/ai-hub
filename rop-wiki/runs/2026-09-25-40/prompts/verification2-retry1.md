(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-40
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 16. 공용 자원·충전·에너지 최적화 (D. 계획·최적화)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: false · fetch_mode: mirror_only (일반 웹 페이지 열람은 네트워크 정책으로 막혀 있다. raw.githubusercontent.com 은 열린다: 공식 문서가 GitHub 에 있는 출처는 입력의 config/source_mirrors.yaml 경로를 WebFetch 로 열어 원문을 읽고 sources[].fetched=true, fetched_via=github_raw, fetch_url 을 적는다. 입력에 원문 텍스트(data/source_texts)가 있는 출처는 fetched_via=inbox. 그 밖의 출처는 fetched=false 이며 코드가 신뢰도 상한(medium)을 강제한다 — 공통 규칙 0절 6항)
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

### runs/2026-09-25-40/target.json

```json
{
  "run_id": "2026-09-25-40",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 40,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 16,
    "area_name": "16. 공용 자원·충전·에너지 최적화",
    "category": "D. 계획·최적화",
    "category_letter": "D"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=16"
}
```

### runs/2026-09-25-40/research.json

```json
{
  "run_id": "2026-09-25-40",
  "date": "2026-09-25",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 16,
    "area_name": "16. 공용 자원·충전·에너지 최적화",
    "category": "D. 계획·최적화"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음",
    "섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 트랙 floorplan-recognition 단계 1 반영 제안(충전소 위치 정보 출처: ref-079·ref-216·ref-219) 검토 대상",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 트랙 반영 제안 2건(VDA 5050 startCharging·stopCharging과 구역 유형, Nav2 도킹 / VDA 5050 팩트시트 batteryCharging) 검토 대상",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 비어 있음 — 트랙 반영 제안(Stark 외 2024 충전소 배치 → 3. 처리능력·거점·설비 계획) 검토 대상",
    "섹션 11. 열린 질문 비어 있음(기존 oq-016 이 이 영역에 걸림)"
  ],
  "research_questions": [
    "로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]",
    "VDA 5050·Open-RMF 같은 표준·오픈소스는 충전 명령, 배터리 상태, 충전 임계값, 충전기 위치를 어떤 필드와 동작으로 표현하는가? (섹션 4·7 겨냥, 트랙 반영 제안 2건 검증)",
    "충전기·승강기·통로 구간 같은 공용 자원을 한 번에 한 로봇에 배분하거나 예약하는 오픈소스 장치(뮤텍스 그룹, 승강기 세션, 예약 시스템)는 무엇인가? (섹션 6·7 겨냥)",
    "충전 시점·충전기 선택·충전 방식(플러그인·교환·유도)과 충전기 대수를 정하는 대표 연구는 무엇이고 어떤 결과를 보고하는가? (섹션 6·8 겨냥, 트랙 반영 제안 ref-109 검토)",
    "다층 시설에서 승강기가 로봇 배송의 병목이 되는 근거와 승강기 선택·층간 이동을 다룬 연구(국내 포함)는 무엇인가? (섹션 3·5·8 겨냥)",
    "충전 대기·배터리 제약을 작업 배정과 함께 푸는 연구와 학습 기반 충전 결정은 13. 작업 배정 — MRTA·27. AI·학습·적응과 모델 운영과 어떻게 연결되는가? (섹션 6·10 겨냥)",
    "ROP가 직접 맡을 충전·공용 자원 계획과 로봇 자체 제어(과충전 보호·정밀 도킹)·설비 안전 제어 사이 경계는 어디인가? — oq-016(충전·대기 시간의 OEE 손실 분류)과 연결 (섹션 9·11 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 3.0.0(main)은 충전을 즉시 동작 또는 노드 동작인 startCharging·stopCharging 으로 표현하며, 충전은 정지한 충전 지점이나 주행 중 충전 차선에서 할 수 있고 과충전 보호는 이동로봇의 책임이다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "VDA5050_EN.md 원본(github_raw) 동작 표: startCharging 'Charging can be done on a charging spot (mobile robot stopped) or on a charging lane (while driving). Protection against overcharging is the responsibility of the mobile robot.' (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f2",
      "claim": "VDA 5050 3.0.0 은 관제(fleet control)의 기능으로 에너지 관리를 들며, 충전 주문이 운반 주문을 중단시킬 수 있다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "VDA5050_EN.md 원본 5.3 관제 기능: 에너지 관리 — 충전 주문이 운반 주문을 중단할 수 있음. 충전 순서·시점 결정 알고리즘은 규정하지 않음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f3",
      "claim": "VDA 5050 최신 팩트시트 스키마의 batteryCharging 은 criticalLowChargingLevel(이 수준 이하에서는 관제가 충전소로 가는 주문만 보내야 함), minimumDesiredChargingLevel, maximumDesiredChargingLevel, minimumChargingTime 네 항목을 로봇 선언으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-228"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "factsheet.schema 원본(github_raw): criticalLowChargingLevel 'at or below which the fleet control should only send orders that command the mobile robot to a charging station'; minimumChargingTime 'desired minimum charging time in seconds'. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f4",
      "claim": "VDA 5050 최신 상태 스키마의 powerSupply 는 충전 상태(stateOfCharge, %), 충전 중 여부(charging), 배터리 전압·전류, 건강 상태(batteryHealth), 현재 충전량으로 갈 수 있는 거리(range, m)를 담으며, 좋음·나쁨만 아는 로봇은 80%·20%로 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "state.schema 원본(github_raw): stateOfCharge 'If mobile robot only provides values for good or bad battery levels, these will be indicated as 20% (bad) and 80% (good).' range 'Estimated reach with current State of Charge in meter.' (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "VDA 5050 3.0.0 명세는 충전소를 별도 구역 유형으로 두지 않고 충전을 주문의 노드 동작과 즉시 동작으로 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "VDA5050_EN.md 원본: 구역 유형(BLOCKED·RELEASE·COORDINATED_REPLANNING·SPEED_LIMIT 등)에 충전 구역 없음, 충전은 startCharging 동작으로 표현(트랙 실행 2026-09-25-19 반영 제안을 이번에 원문으로 재확인). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "Open-RMF 플릿 어댑터 템플릿 설정은 로봇이 운행하지 않는 배터리 하한(recharge_threshold), 충전 목표(recharge_soc), 배터리 전압·용량·충전 전류, 주변·도구 장치 소비 전력, 배터리 소모 반영 여부, 작업 종료 후 동작(park·charge·nothing), 로봇별 전용 충전기를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-105"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "config.yaml 원본(github_raw): 'recharge_threshold: 0.10 # Battery level below which robots in this fleet will not operate', 'recharge_soc: 1.0', 'charging_current: 5.0 # A', 'account_for_battery_drain: True', 로봇마다 charger 지정. 예시값. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f7",
      "claim": "Open-RMF 에서 충전 작업은 플릿 어댑터가 스스로 만드는 작업이며, 로봇이 일련의 작업을 마칠 충전량이 부족하면 작업 계획기가 충전(ChargeBattery) 작업을 일정에 끼워 넣고, 현재는 로봇마다 전용 충전 위치가 있다고 가정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-039",
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "task_types.md 원본: 'This is a self-generated task, self generated by RMF fleet adapter.' rmf_demos README 원본: 'ChargeBattery tasks are optimally injected into a robot's schedule when the robot has insufficient charge'; 'we assume each robot in the map has a dedicated charging location'. 같은 발행 주체. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f8",
      "claim": "Open-RMF 작업 계획기(rmf_task TaskPlanner)는 충전소로 돌아갈 초기 충전량조차 없거나 요청을 감당할 배터리 용량이 없는 경우를 오류로 구분하고, 낮은 충전 상태를 이차항으로 강하게 벌점하는 배터리 우선 비용 설정을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-377"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "TaskPlanner.hpp 원본(github_raw): 'sufficient initial charge to even head back to their charging stations'; 해결책으로 배터리 용량 증대 또는 threshold_soc 낮추기 제시; BatteryAware 설정 'strongly penalize low SOC with a quadratic term'. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f9",
      "claim": "Open-RMF 에서 충전기 위치는 Traffic Editor 경유점의 is_charger 수동 주석으로 들어가 배터리가 임계값 아래로 떨어진 로봇이 그곳으로 보내지며, 로봇별 충전 경유점을 지정하지 않으면 그래프에서 가장 가까운 충전 경유점을 쓰고, 주차 예약 시스템 사용은 기본값 꺼짐이지만 켜기를 권장한다.",
      "tag": "사실",
      "source_ids": [
        "ref-079",
        "ref-864",
        "ref-865"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "traffic-editor.md 원본: is_charger 이면 'rmf_fleet_adapter will treat this as a charging station'. Graph.hpp: 'Robots are routed to these spots when their batteries charge levels drop below the threshold value.' RobotUpdateHandle.hpp: 지정 없으면 가장 가까운 is_charger 경유점. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "Open-RMF 교통 그래프는 경유점·차선을 뮤텍스 그룹(mutex group)에 넣을 수 있고, 같은 뮤텍스 그룹에 속한 경유점이나 차선은 한 번에 한 로봇만 점유할 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-864"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Graph.hpp 원본(github_raw) in_mutex_group(): 'Only one robot at a time is allowed to occupy any waypoint or lane associated with a particular mutex group.' 저장소 이슈에 동시 진입 버그 보고가 있어 동작 신뢰성은 미확인. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f11",
      "claim": "Open-RMF 승강기 요청은 요청자별 고유 세션 id 로 승강기를 점유하며, 승강기 상태는 세션 종료 요청(REQUEST_END_SESSION)을 보낼 때까지 제어권을 받은 세션 id 를 기록하고, AGV 모드에서는 승강기가 멈추면 문이 계속 열려 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-312",
        "ref-286"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "LiftRequest.msg 원본: 'session_id should be unique at least between different requesters'; 'AGV mode means that the doors are always open when the lift is stopped'. LiftState.msg 원본: session_id 'has been granted control of the lift until it sends a request with a request_type of REQUEST_END_SESSION'. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f12",
      "claim": "Open-RMF 의 실험적 예약 라이브러리 rmf_reservation 은 로봇이 충전기 같은 자원을 주어진 시간 범위 안에서 정해진 시간 동안 쓰겠다고 요청하면 해법기가 로봇을 자원에 배정하는 제약 자원 스케줄링을 제공한다고 소개된다.",
      "tag": "사실",
      "source_ids": [
        "ref-866"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'Experimental reservation library in rust'; 'A robot may request the use of a resource like a charger for a fixed duration of time within a given time range'. README 원본은 main·master 경로 모두 404로 열지 못함.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "연계 대상: Nav2 도킹 프레임워크는 환경 안 도크 인스턴스(유형과 [x, y, θ] 위치)의 데이터베이스를 두고 충전 도크와 비충전 도크(컨베이어·팔레트 등)를 플러그인으로 구분하며, 센서로 도크 자세를 보정하고 도킹 뒤 충전 시작 여부(isCharging)를 확인한다.",
      "tag": "사실",
      "source_ids": [
        "ref-216"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "nav2_docking README 원본(github_raw): 'dock with charging stations, as well as non-charging infrastructure such as static locations (ex. conveyers) or dynamic locations (ex. pallets)'; getRefinedPose 로 센서 보정; isCharging·hasStoppedCharging. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f14",
      "claim": "MiR 충전 스테이션 매뉴얼 게재본은 지도에 충전 스테이션 마커를 두고 로봇이 이를 감지해 도킹한다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-219"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본의 충전 마커 설정 절. 이번 실행에서 원문 미열람. (재인용: 2026-09-25-19)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f15",
      "claim": "Zou·Gong·de Koster·Xu(2018)는 로봇 이동형 풀필먼트 시스템(RMFS)에서 플러그인 충전·배터리 교환·유도 충전 전략을 반개방형 대기행렬 네트워크와 시뮬레이션으로 비교해, 유도 충전이 회수 처리 시간에서 가장 좋고 배터리 비용이 낮으면 배터리 교환이 플러그인 충전보다 싸다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-098"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'Inductive charging performs the best in terms of retrieval throughput time'; 배터리 비용이 낮을 때 교환이 플러그인보다 저렴. EJOR 267(2), 733–753. 원문 미열람.",
      "as_of": "2018",
      "flow_step": "피킹",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f16",
      "claim": "Chen·Gong·Chen·Wang(2024)은 자가 등반 로봇(SCR) 창고의 배터리 관리를 반개방형 대기행렬 네트워크로 모델링해, 배터리 열화를 반영하면 느린 충전이 빠른 충전보다 나은 조건이 있고, 우선 충전 정책이 전용 충전 정책보다 비용 효율적이며, 충전기 대수 결정 도구를 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-861"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'slow charging outperforms fast charging' 조건 도출, 'The priority charging policy is more cost-effective than the dedicated charging policy', 충전기 대수 결정 도구. EJOR 312(1), 164–181. 원문 미열람.",
      "as_of": "2024-01",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "다중 AGV 충전 순서 최적화 연구(Computers & Industrial Engineering, 2024)는 도착 시 충전소가 사용 중일 확률과 충전 전 대기 확률을 충전소마다 확률 변수로 두고 총 주행 시간 기댓값을 최소화하는 혼합 정수 선형 계획을 세웠으며, 허용 최대치까지 완전 충전하는 것이 최적임을 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-858"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'two random variables for each charging station—one modeling the probability of finding the station busy upon arrival, and another modeling the probability of having to wait'; 'fully recharging to the maximum allowed is optimal'. 저자 미확인. 원문 미열람.",
      "as_of": "2024-08",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "Dang·Singh·Adan·Martagan·van de Sande(2021)는 다중 적재·다능력 AGV 에 운반 요청과 충전 요청을 함께 배정·순서화하고 임계 배터리 수준을 지키는 부분 충전 시간을 정하는 혼합 정수 선형 계획과 적응형 대규모 이웃 탐색을 제시해, 현행 방식 대비 비용을 약 20~50% 줄였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-862"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'assigning transport and charging requests to AGVs, sequencing these requests, and determining the arrival times and charging duration'; 'about 20%–50% cost reduction with respect to current practice'(저자 보고). 원문 미열람.",
      "as_of": "2021-12",
      "flow_step": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "근접 정책 최적화(PPO) 기반 심층 강화학습 연구(arXiv 2607.05683)는 고정 충전소가 있는 다중 블록 창고에서 주문이 확률적으로 도착할 때 충전소 선택과 충전 시간을 충전소 대기 예상 시간을 반영해 학습하며, 고정 규칙 휴리스틱은 동적 환경과 다중 로봇 조율에서 비효율적이라고 지적한다.",
      "tag": "사실",
      "source_ids": [
        "ref-859"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'charging station selection and optimal charging duration, explicitly accounting for anticipated queuing times at the stations'; 'fixed-rule heuristics often prove suboptimal'. 프리프린트, 성능 비교는 저자 보고. 원문 미열람.",
      "as_of": "2026-07",
      "flow_step": "피킹",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f20",
      "claim": "Ma·Zhou·Stephen(2020)은 자동화 컨테이너 터미널의 배터리 AGV 시스템을 시뮬레이션해 분산형 충전소 배치와 점진적 재충전 정책이 좋은 성능을 낸다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-860"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'a decentralized charging station layout and a progressive recharging policy lead to excellent performance'. Simulation Modelling Practice and Theory 106. 항만 사례라 물류센터 적용은 미확인. 원문 미열람.",
      "as_of": "2020",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "Stark 외(2024)는 창고 안 충전소의 최적 배치를 PageRank 와 비슷한 방법으로 다룬 연구를 발표했다.",
      "tag": "사실",
      "source_ids": [
        "ref-109"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "참고문헌 목록 제목 기준: 'A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse'(arXiv 2406.17003). 이번 실행에서 원문 미열람. (재인용: 2026-09-25-19)",
      "as_of": "2024-06",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "Omega 게재 논문(2024)은 로봇 이동형 풀필먼트 시스템의 성능 평가에 로봇 에너지 소비를 넣고 동적 우선순위를 쓰는 운영 정책을 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-146"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "참고문헌 목록 제목 기준: 'The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority'. 결과 수치 미확인.",
      "as_of": "2024",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "고밀도 병원 환경의 약품 배송 로봇 연구는 승강기 가동률이 높을수록 배송 실패가 많고 배송 시간이 길었다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-060"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Digital Health 2026 논문. 병원 사례이며 물류센터 적용은 미확인(oq-010). 결과 수치는 원문 미열람으로 쓰지 않음. (재인용: 2026-09-25-38)",
      "as_of": "2026",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f24",
      "claim": "다층 호텔 배송 경로 계획 연구는 승강기를 층간 이동의 대기·운행 시간으로 모델링했고, 고객 노드 60개 시나리오에서 승강기 운행 시간을 40초에서 100초로 늘리면 총 이동 시간이 약 225초에서 500초로 거의 두 배가 된다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-103"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'increasing elevator operation time from 40 s to 100 s nearly doubles the total travel time (from 225 s to 500 s)'. Sensors 게재(doi 10.3390/s25061783). 호텔 사례. 원문 미열람.",
      "as_of": "2025",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "Electronics(2025) 게재 논문은 실내 배송 로봇의 그래프 기반 다층 경로 계획에서 승강기 선택을 최적화하는 방법을 제시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-321"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "검색 결과 제목 기준: 'Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots'. 결과 수치 미확인. 원문 미열람.",
      "as_of": "2025",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f26",
      "claim": "박재범·조성준·김준식·유범재(2024)는 서버를 통해 엘리베이터를 신속하게 제어하는 모듈과 작업 구조로 층간 이동을 처리하고, 노드 그래프 기반으로 한 번의 주행에서 여러 목적지를 고려하는 다층 경로 계획 알고리즘을 제안해 실증 시험과 주행 시간 비교로 검증했다.",
      "tag": "사실",
      "source_ids": [
        "ref-863"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약(국문): 서버를 통한 엘리베이터 제어 모듈과 task 구조, 노드 그래프 기반 다층 경로 계획, 다수 실증 테스트. 배송 로봇 대상(물류센터 아님). 원문 미열람.",
      "as_of": "2024",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f27",
      "claim": "분류 원문 질문(로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까)에 대해, 로봇마다 같은 충전 임계값(criticalLowChargingLevel, recharge_threshold)으로만 충전을 시작하면 충전 수요가 겹칠 수 있으므로, 충전소 대기를 반영한 충전 시점·충전기 선택, 공유 충전기의 우선 충전 정책, 충전기·승강기 점유의 예약·세션 관리를 조율 계층이 함께 맡아야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-228",
        "ref-105",
        "ref-858",
        "ref-859",
        "ref-861",
        "ref-312"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f3·f6(임계값 기반 충전 시작), f17·f19(대기 반영 충전 결정), f16(우선 충전 정책), f11·f12(세션·예약)를 SCM 질문에 대응시킨 이 위키의 추론. 물류센터 실측 자료는 확인 못함.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f28",
      "claim": "피킹 성수기에는 여러 로봇이 비슷한 시각에 충전 하한에 닿아 충전기 대기열이 생기고 가용 로봇 수가 줄 수 있으므로, 주문이 적은 시간대에 기회 충전을 넣거나 충전 요청을 작업 배정과 함께 계획하는 방식이 처리량 손실을 줄이는 수단이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-862",
        "ref-859",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f18(운반·충전 요청 동시 배정과 부분 충전), f19(확률적 주문 도착 하의 충전 결정), f2(충전 주문이 운반 주문을 중단 가능)를 현장 시나리오로 조합한 추론. 실제 현장 사례는 확인 못함.",
      "as_of": "2026-09-25",
      "flow_step": "피킹",
      "flow_item": "예외·성과"
    },
    {
      "id": "f29",
      "claim": "다층 시설의 출하 단계에서는 승강기가 세션 단위로 한 요청자에게 점유되므로, 여러 제조사 로봇의 승강기 호출을 조율 계층이 세션 순서·목적층 묶음으로 배분하지 않으면 층간 대기가 출하 마감을 위협할 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-312",
        "ref-286",
        "ref-103"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f11(세션 점유), f24(승강기 운행 시간에 따른 총 이동 시간 증가)를 출하 단계에 적용한 추론. 물류센터 정량 자료는 oq-010 미해결.",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "제약"
    },
    {
      "id": "f30",
      "claim": "ROP 가 직접 맡을 범위는 여러 제조사 로봇에 걸친 충전기·승강기·통로 구간·대기 위치의 예약과 배분, 충전 시점과 충전 목표 결정, 배터리 상태를 반영한 작업 배정 입력이며, 이는 VDA 5050 이 관제의 에너지 관리로 두고 Open-RMF 가 충전 작업 삽입·뮤텍스 그룹·승강기 세션으로 다루는 층위에 해당하는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-104",
        "ref-864",
        "ref-312"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2·f7·f10·f11 을 분류 원문 9장 경계에 대응시킨 추론.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f31",
      "claim": "연계 대상: 과충전 보호, 충전기와의 통신·정밀 도킹, 배터리 관리 장치, 승강기 운행·설비 안전 제어는 로봇·충전 설비·승강기 쪽이 맡고, ROP 는 충전 시작·중지 요청, 상태 확인, 승강기 세션 요청과 모드 확인을 담당하는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-216",
        "ref-284"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1('Protection against overcharging is the responsibility of the mobile robot'), f13(도크 자세 보정·충전 확인은 로봇 쪽 프레임워크), Lifts 문서의 승강기 어댑터가 승강기 동작을 방해하는 요청을 막는 역할에서 도출.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f32",
      "claim": "충전소 정보는 시설 안 설비 위치(도크 인스턴스 자세)와 로봇이 경로 그래프에서 접근하는 지점(is_charger 경유점)으로 나뉘어 관리되므로, ROP 의 공용 자원 모델도 충전기 설비와 접근 경유점을 분리해 두어야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-216",
        "ref-079",
        "ref-865"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f9(경유점 주석·가장 가까운 충전 경유점)와 f13(도크 위치 데이터베이스·센서 보정)을 결합한 추론(트랙 실행 2026-09-25-19 f19 의 추정을 이번 원문으로 뒷받침).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f33",
      "claim": "이 영역은 충전 요청을 작업 배정과 함께 푸는 연구로 13. 작업 배정 — MRTA 와, 뮤텍스 그룹·대기 지점으로 15. 다중 로봇 경로·교통 관리 — MAPF 와, 승강기 세션으로 10. 설비·건물 시스템 연동과, 충전기 대수·배치로 3. 처리능력·거점·설비 계획과, 팩트시트 충전 설정으로 5. 로봇 능력·작업 온톨로지와, 현재 배터리 상태로 8. 실시간 세계 상태·데이터 일관성과, 충전 정책 시뮬레이션으로 22. 시뮬레이션·예측용 디지털 트윈과, 학습 기반 충전 결정으로 27. AI·학습·적응과 모델 운영과 이어지는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-862",
        "ref-864",
        "ref-312",
        "ref-861",
        "ref-109",
        "ref-228",
        "ref-051",
        "ref-860",
        "ref-859"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f18·f10·f11·f16·f21·f3·f4·f20·f19 를 영역 연결로 정리한 추론. 8번(현재 배터리 상태)과 22번(충전 정책을 가정해 실험하는 시뮬레이션)은 구분.",
      "as_of": "2026-09-25",
      "flow_step": null,
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
      "accessed": "2026-09-25",
      "summary": "VDA 5050 최신판(main, 3.0.0) 명세 원문. 이번 실행은 startCharging·stopCharging 동작, 관제의 에너지 관리 기능, 구역 유형을 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-228",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/factsheet.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 팩트시트 JSON 스키마. 이번 실행은 batteryCharging 네 항목을 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/json_schemas/factsheet.schema",
      "source_unopened": false
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 상태 메시지 JSON 스키마. 이번 실행은 powerSupply 항목을 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/json_schemas/state.schema",
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
      "accessed": "2026-09-25",
      "summary": "플릿 어댑터 설정 템플릿. 이번 실행은 충전 임계값·충전 목표·배터리·전력 소비·작업 종료 동작·로봇별 충전기 항목을 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/fleet_adapter_template/main/fleet_adapter_template/config.yaml",
      "source_unopened": false
    },
    {
      "id": "ref-079",
      "org": "Open Robotics",
      "title": "Traffic Editor - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 교통 편집기 문서. 이번 실행은 is_charger·dock_name·대기 지점 속성과 승강기를 공유 자원으로 보는 서술을 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/traffic-editor.md",
      "source_unopened": false
    },
    {
      "id": "ref-039",
      "org": "Open Robotics",
      "title": "Currently supported Tasks - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/task_types.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 지원 작업 유형 문서. 이번 실행은 충전 작업이 플릿 어댑터가 스스로 만드는 작업이라는 서술을 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/task_types.md",
      "source_unopened": false
    },
    {
      "id": "ref-104",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_demos — Demonstrations of Open-RMF (README)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_demos",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 데모 README. 이번 실행은 충전 작업의 일정 삽입과 로봇별 전용 충전 위치 가정을 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_demos/main/README.md",
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
      "accessed": "2026-09-25",
      "summary": "Open-RMF 작업 계획기 헤더. 이번 실행은 충전량 부족 오류 구분과 배터리 우선 비용 설정을 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_task/main/rmf_task/include/rmf_task/TaskPlanner.hpp",
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
      "accessed": "2026-09-25",
      "summary": "승강기 요청 메시지. 이번 실행은 세션 id, 요청 유형, AGV 모드의 문 동작을 원문으로 확인했다.",
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
      "accessed": "2026-09-25",
      "summary": "승강기 상태 메시지. 이번 실행은 제어권을 받은 세션 id 기록과 운영 모드를 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_internal_msgs/main/rmf_lift_msgs/msg/LiftState.msg",
      "source_unopened": false
    },
    {
      "id": "ref-284",
      "org": "Open Robotics",
      "title": "Lifts (integration_lifts) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_lifts.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 승강기 연동 문서. 이번 실행은 승강기 어댑터의 역할을 원문으로 확인했다(여러 플릿 사이 배분 규칙은 문서에 없음).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/integration_lifts.md",
      "source_unopened": false
    },
    {
      "id": "ref-216",
      "org": "ROS Navigation (ros-navigation/navigation2 GitHub)",
      "title": "nav2_docking — README (Open Navigation's Nav2 Docking Framework)",
      "published": null,
      "url": "https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "Nav2 도킹 프레임워크 README. 이번 실행은 도크 데이터베이스, 충전·비충전 도크 플러그인, 센서 보정, 충전 확인 함수를 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros-navigation/navigation2/main/nav2_docking/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-219",
      "org": "Mobile Industrial Robots(MiR) (ManualsLib 게재본)",
      "title": "MiR Charge 24V Operating Manual — Setting charging station markers on the map (제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본)",
      "published": null,
      "url": "https://www.manualslib.com/manual/1941068/Mir-Mir-Charge-24v.html?page=23",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이번 실행에서 다시 열지 않았다. 지도에 충전 스테이션 마커를 설정하는 매뉴얼 절.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-098",
      "org": "Zou, B., Gong, Y., de Koster, R., & Xu, X.",
      "title": "Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system",
      "published": "2018",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RMFS 에서 플러그인·교환·유도 충전 전략을 반개방형 대기행렬 네트워크와 시뮬레이션으로 비교한 EJOR 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-109",
      "org": "Stark, H.-G. 외",
      "title": "A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse",
      "published": "2024-06",
      "url": "https://arxiv.org/abs/2406.17003",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 창고 충전소 배치를 PageRank 와 비슷한 방법으로 최적화한 프리프린트.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-146",
      "org": "Omega 게재 논문(저자 미확인)",
      "title": "The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority",
      "published": "2024",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RMFS 성능 평가에 에너지 소비를 넣고 동적 우선순위 운영 정책을 다룬 논문(제목 기준).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-060",
      "org": "Lee, Y. 외(Digital Health)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026",
      "url": "https://doi.org/10.1177/20552076261437181",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 병원 약품 배송 로봇의 승강기 이용과 배송 실패·시간의 관계를 다룬 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-103",
      "org": "PMC 게재 논문(저자 미확인)",
      "title": "The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments",
      "published": null,
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 다층 호텔 배송 로봇 경로 계획에서 승강기 대기·운행 시간을 모델링한 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-321",
      "org": "Electronics(MDPI) 게재 논문(저자 미확인)",
      "title": "Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots",
      "published": "2025",
      "url": "https://doi.org/10.3390/electronics14050982",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 실내 배송 로봇의 다층 경로 계획에서 승강기 선택을 최적화한 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-858",
      "org": "Computers & Industrial Engineering 게재 논문(저자 미확인)",
      "title": "Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach",
      "published": "2024-08",
      "url": "https://www.sciencedirect.com/science/article/pii/S0360835224006314",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 충전소 사용 중·대기 확률을 확률 변수로 둔 다중 AGV 충전 순서 최적화(혼합 정수 선형 계획) 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-859",
      "org": "arXiv 2607.05683 저자(미확인)",
      "title": "Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers",
      "published": "2026-07",
      "url": "https://arxiv.org/abs/2607.05683",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 다중 블록 창고에서 PPO 기반 강화학습으로 충전소 선택과 충전 시간을 학습하는 프리프린트.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-860",
      "org": "Ma, N., Zhou, C., & Stephen, A.",
      "title": "Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals",
      "published": "2020",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자동화 컨테이너 터미널의 충전소 배치와 배터리 AGV 충전 정책을 시뮬레이션으로 평가한 논문(Simulation Modelling Practice and Theory 106).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-861",
      "org": "Chen, W., Gong, Y., Chen, Q., & Wang, H.",
      "title": "Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse",
      "published": "2024-01",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자가 등반 로봇 창고에서 충전 기술·충전 정책·충전기 대수를 반개방형 대기행렬 네트워크로 분석한 EJOR 312(1) 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-862",
      "org": "Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D.",
      "title": "Scheduling heterogeneous multi-load AGVs with battery constraints",
      "published": "2021-12",
      "url": "https://www.sciencedirect.com/science/article/pii/S0305054821002586",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 운반·충전 요청을 함께 배정·순서화하고 부분 충전 시간을 정하는 MILP·적응형 대규모 이웃 탐색 논문(Computers & Operations Research).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-863",
      "org": "박재범, 조성준, 김준식, 유범재",
      "title": "배송 로봇의 다층, 다중 배송을 위한 효율적인 경로 계획 및 엘리베이터 층간 이동 시스템",
      "published": "2024",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003107904",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서버 기반 엘리베이터 제어 모듈과 노드 그래프 기반 다층·다중 목적지 경로 계획을 제안하고 실증 시험한 국내 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-864",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 교통 그래프 헤더. 경유점·차선의 뮤텍스 그룹(한 번에 한 로봇만 점유), 충전 경유점·주차 지점·대기 지점, 문·승강기 문 차선 조건을 정의한다. 이번 실행에서 원본을 열었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_traffic/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp",
      "source_unopened": false
    },
    {
      "id": "ref-865",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "플릿 어댑터 로봇 갱신 인터페이스 헤더. 로봇별 충전 경유점 지정, 주차 예약 시스템 사용 설정, 배터리 충전 상태 갱신, 승강기 세션 정보를 다룬다. 이번 실행에서 원본을 열었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp",
      "source_unopened": false
    },
    {
      "id": "ref-866",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_reservation — Experimental reservation library in rust (GitHub)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_reservation",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 충전기 같은 자원을 시간 범위 안에서 정해진 시간 동안 로봇에 배정하는 실험적 제약 자원 스케줄링 라이브러리(검색 요약 기준). README raw 경로는 404.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md",
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
      "rationale": "3절: f27(SCM 질문 — 같은 임계값에 따른 충전 수요 겹침), f23·f24(승강기 병목 근거), f15·f16(충전 정책이 처리량·비용에 미치는 영향) / 4절: f3·f4(충전 상태·임계 저충전 수준), f6(recharge_threshold·recharge_soc), f10(뮤텍스 그룹), f11(승강기 세션), f15(플러그인·교환·유도 충전) / 5절: f28(피킹, 예외·성과), f29(출하, 제약), f7(시작 조건) / 6절: f7·f8·f9·f10·f11·f12, f17·f18·f19·f20, f32 — 트랙 floorplan-recognition 반영 제안(충전소 위치 정보 출처) 검토 결과: f9(ref-079 is_charger, 원문 확인)·f13(Nav2 도크 데이터베이스, 연계 대상)·f14(MiR, 벤더 주장 유지)·f32(시설 위치와 접근 지점 분리 [추정]) 반영 / 7절: f1·f2·f3·f4·f5(VDA 5050 — 트랙 반영 제안 2건을 원문으로 재확인, 필드 이름은 스키마 기준 minimumDesiredChargingLevel·maximumDesiredChargingLevel), f6~f12(Open-RMF), f13(Nav2 도킹) / 8절: f15~f26(국내 f26) / 9절: f30(직접 범위), f31(연계 대상) / 10절: f33 — 트랙 반영 제안(Stark 외 2024 → 3. 처리능력·거점·설비 계획) 반영(f21), f19 는 27. AI·학습·적응과 모델 운영과 양쪽 연결 / 11절: 기존 oq-016 과 새 열린 질문"
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "충전 상태",
      "term_en": "State of Charge (SOC)",
      "definition": "배터리에 남은 충전량을 전체 용량 대비 비율(%)로 나타낸 값으로, VDA 5050 상태 메시지의 stateOfCharge 와 Open-RMF 배터리 갱신이 이 값을 쓴다."
    },
    {
      "term_ko": "뮤텍스 그룹",
      "term_en": "Mutex Group (Open-RMF)",
      "definition": "Open-RMF 교통 그래프에서 같은 그룹에 묶인 경유점·차선을 한 번에 한 로봇만 점유하도록 하는 상호 배제 단위이다."
    },
    {
      "term_ko": "승강기 세션",
      "term_en": "Lift Session (Open-RMF)",
      "definition": "Open-RMF 에서 한 요청자가 세션 id 로 승강기 제어권을 받아 세션 종료 요청을 보낼 때까지 점유하는 단위이다."
    },
    {
      "term_ko": "배터리 교환",
      "term_en": "Battery Swapping",
      "definition": "방전된 로봇 배터리를 충전기에 꽂아 기다리는 대신 충전된 배터리로 바꿔 끼워 로봇을 곧바로 다시 운행하게 하는 충전 방식이다."
    }
  ],
  "open_questions_new": [
    "제조사가 다른 이동로봇이 같은 충전기를 함께 쓸 수 있게 하는 충전 커넥터·충전 통신의 공통 규격이나 공개 사례가 있는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f1 | 종류: 일반",
    "물류센터 로봇의 충전 시점을 시간대별 전기 요금이나 최대 수요 전력 기준으로 계획한 연구나 국내 사례가 있는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 4. 성과·경제성·프로세스 개선 | 근거: f17 | 종류: 일반",
    "여러 제조사 플릿이 한 승강기를 함께 쓸 때 세션 순서·최대 점유 시간·목적층 묶음을 정하는 배분 규칙을 공개한 표준이나 구현이 있는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 10. 설비·건물 시스템 연동 | 근거: f11 | 종류: 일반",
    "충전 하한을 제조사가 팩트시트로 선언한 값(criticalLowChargingLevel)과 ROP 운영 설정(recharge_threshold) 가운데 어느 것으로 삼고, 둘이 다르면 어떻게 조정하는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 5. 로봇 능력·작업 온톨로지 | 근거: f3 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 28,
    "cross_checked_count": 0,
    "unverified": [
      "모든 finding 교차 확인 없음: 표준·오픈소스 내용은 단일 발행 주체, 연구 결과는 각 논문 단일 출처",
      "f12 rmf_reservation README 원문 열지 못함(main·master 404), 배포판 사용 여부 미확인",
      "f10 뮤텍스 그룹 동시 진입 버그 보고(open-rmf 이슈)가 있어 실제 동작 신뢰성 미확인",
      "f15~f26 근거 논문 원문 미열람(검색 요약·제목 범위)",
      "f17 ref-858 저자 미확인",
      "f18·f19 성능 수치는 저자 보고",
      "f22·f25 는 제목 수준만 확인",
      "f14 MiR 충전 마커는 벤더 주장이며 이번에 다시 열지 않음",
      "국내 물류센터 충전·승강기 병목 정량 자료 미확인(oq-010 관련)",
      "시간대별 전기 요금 기반 로봇 충전 계획의 학술 출처 미확보"
    ],
    "scope_violations": [
      "f13·f31: 정밀 도킹·과충전 보호·승강기 안전 제어는 분류 원문 9장 '로봇 자체 지능·제어'·'시설·설비 제어' 연계 대상이라 claim 을 '연계 대상: '으로 표시하고 ROP 역할을 요청·상태 확인으로 한정함",
      "f20·f23·f24·f26: 컨테이너 터미널·병원·호텔·배송 로봇 사례라 물류센터 직접 적용 근거로는 제한적임"
    ],
    "budget_used": {
      "queries": 19,
      "sources": 9
    },
    "limits": "web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 재사용 ref-031·ref-228·ref-051·ref-105·ref-079·ref-039·ref-104·ref-377·ref-312·ref-286·ref-284·ref-216, 신규 ref-864·ref-865. rmf_reservation README 는 404, task_new.md 에는 충전 내용 없음. 그 밖의 신규 7건(ref-858~ref-863, ref-866)과 재사용 ref-219·ref-098·ref-109·ref-146·ref-060·ref-103·ref-321 은 원문 미열람(신뢰도 상한 medium). finding 신뢰도 모두 medium 이하, 교차 확인 0건. 검색 19회/30, 신규 출처 9건/15(ref-858~ref-866, 예약 구간 안), 재사용 19건. 세부영역 반영 제안 4건(트랙 floorplan-recognition 2026-09-25-19 3건, manual-capability-ontology 2026-09-25-23 1건)을 모두 검토해 f1·f3·f5·f9·f13·f14·f21·f32 로 6·7·10절 반영을 제안했다(batteryCharging 필드 이름은 스키마 원문 기준으로 정정). 한국 자료: 박재범 외 2024(ref-863). 한국 물류센터 충전 연구는 검색 2회에서 찾지 못함. 교차 규칙: 학습 기반 충전 결정(f19)은 27. AI·학습·적응과 모델 운영과 이 영역 양쪽 연결을 제안했다. 8. 실시간 세계 상태·데이터 일관성(현재 배터리 상태)과 22. 시뮬레이션·예측용 디지털 트윈(충전 정책 실험)은 섞지 않았다. 정정 요청 없음. oq-016(충전·대기 시간의 OEE 손실 분류)은 관련 근거를 찾지 못해 해결 제안하지 않았다."
  }
}
```

### runs/2026-09-25-40/verification.json

```json
{
  "run_id": "2026-09-25-40",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 data/source_texts/ref-031.txt 동작 표 startCharging 행이 충전 지점·충전 차선과 과충전 보호의 로봇 책임을 적는다. 단일 공식 명세, 발행일 미확인(oq-005)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 5.3 'Energy management: Charging orders can interrupt transfer orders'. evidence_excerpt 의 '충전 순서·시점 알고리즘은 규정하지 않음'은 명세 문구가 아니라 2절(교통 관리 로직 범위 제외)에서 끌어낸 해석이므로 본문에 명세 문구처럼 쓰지 않는다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: factsheet.schema(main) raw 원본을 다시 열었다. batteryCharging 네 필드와 criticalLowChargingLevel 설명이 일치한다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: state.schema raw 원본. powerSupply 필드, 20%·80% 표기, range(m) 설명이 일치한다. stateOfCharge·charging 만 필수이고 나머지는 선택 필드다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: VDA5050_EN.md raw 6.4.1 구역 유형은 BLOCKED·LINE_GUIDED·RELEASE·COORDINATED_REPLANNING·SPEED_LIMIT·ACTION·PRIORITY·PENALTY·DIRECTED·BIDIRECTED 이고 충전 구역은 없다. 충전은 동작으로 표현된다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: config.yaml raw. recharge_threshold 0.10, recharge_soc 1.0, 전압·용량·충전 전류, ambient·tool 소비 전력, account_for_battery_drain, finishing_request, 로봇별 charger. 수치는 템플릿 예시값이다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-039(입력 원문) 'self-generated task', ref-104 README raw 의 ChargeBattery 일정 삽입과 전용 충전 위치 가정(is_charger 주석). 두 출처는 같은 발행 주체라 독립 교차가 아니다. 주의: ref-039 는 충전소를 is_parking_spot 으로 설정한다고 적어 ref-104·ref-079 의 is_charger 와 어긋난다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: TaskPlanner.hpp raw. 충전소 복귀 충전량 부족 오류, 배터리 용량 부족 오류, BatteryAware 'strongly penalize low SOC with a quadratic term'."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: traffic-editor.md raw 의 is_charger, Graph.hpp 'Robots are routed to these spots...', RobotUpdateHandle.hpp 의 가장 가까운 is_charger 경유점 기본값과 주차 예약 시스템(기본 false, 켜기 권장). 모두 같은 발행 주체다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Graph.hpp raw 뮤텍스 그룹 문구가 일치한다. evidence_excerpt 가 말하는 '동시 진입 버그 보고'는 브리프에 출처가 없어 본문에 쓸 수 없다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: LiftRequest.msg·LiftState.msg raw. 세션 id 고유성, REQUEST_END_SESSION 까지의 제어권, AGV 모드의 정지 시 문 개방이 일치한다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(README raw 404를 검증에서도 재현). 검색 결과가 저장소 제목 'Experimental reservation library in rust'와 충전기 예약 설명을 확인한다. 실험적 라이브러리이며 배포판 포함 여부는 미확인이다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: nav2_docking README raw. 도크 인스턴스(플러그인 유형과 [x, y, theta]), 비충전 도크(컨베이어·팔레트), getRefinedPose, isCharging·hasStoppedCharging. '연계 대상' 표시가 적절하다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검증에서도 다시 열지 않았다. 기존 등록 출처 ref-219 의 재인용(2026-09-25-19)이며 제조사 공식 사이트가 아닌 게재본이다. [추정]·벤더 주장·low 가 적절하다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과(Erasmus 저장소·ScienceDirect)가 EJOR 267(2) 733–753, SOQN, 유도 충전 최선, 배터리 비용이 낮을 때 교환이 더 저렴함을 확인한다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과(ScienceDirect·RePEc EJOR 312(1) 164–181)가 느린 충전이 나은 조건, 우선 충전 정책의 비용 효율, 충전기 대수 결정 도구를 확인한다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검증 검색이 C&IE 2024-08 게재, ILP, 허용 최대치까지 완전 충전이 최적임을 확인했다. 충전소별 확률 변수 두 개와 목적함수(총 주행 시간 기댓값)는 리서치 스니펫에만 있다. 저자 미확인."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과(TU/e 저장소, C&OR 136, 105517)가 저자, 하이브리드 ALNS, 산업 사례, 현행 대비 20~50% 비용 절감(저자 보고)을 확인한다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과가 arXiv 2607.05683(2026-07-06, Shaji·Sobhanan·Defryn), PPO, 다중 블록 창고, 고정 충전소, 대기 예상 시간을 반영한 충전소 선택·충전 시간을 확인한다. 프리프린트다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검증 검색은 저자·제목만 확인했다. '분산형 충전소 배치·점진적 재충전 정책이 좋은 성능' 문구는 리서치 스니펫에 기댄다. 항만 사례다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. arXiv 2406.17003(2024-06-24, Stark 외 3인) 검색 요약이 PageRank 에서 착안한 창고 충전소 배치를 확인한다. 대상은 전기 산업용 트럭·지게차 플릿이다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 제목 수준 주장이며 기존 등록 출처 ref-146 이다. 검증에서 다시 검색하지 않았다(예산). 결과 수치는 미확인이다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 기존 등록 출처 ref-060 의 재인용(2026-09-25-38)이다. 병원 사례이며 물류센터 적용은 미확인(oq-010)이다. 수치는 쓰지 않는다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검증 검색(PMC·PubMed)이 고객 노드 60개, 40초→100초, 225초→500초 수치와 2025년 3월 게재를 확인한다. 브리프 sources 의 published 는 null 이다. 호텔 사례다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과에 doi 10.3390/electronics14050982 제목이 나타난다. 제목 수준 주장이며 결과는 미확인이다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과(KCI)가 전자공학회논문지 61(8) 2024, 엘리베이터 제어 모듈·task 구조, 노드 그래프 다층 경로 계획, 실증 시험·주행 시간 비교를 확인한다. 배송 로봇 대상이다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f3·f6·f11·f12·f16·f17·f19 를 종합한 이 위키의 추론이다. [추정] 태그가 적절하다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f2·f18·f19 를 조합한 현장 시나리오 추론이며 [추정]이 적절하다. 실제 현장 사례는 없다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f11·f24 를 조합한 추론이다. 여러 플릿 사이 승강기 배분 규칙은 Lifts 문서(ref-284)에도 없음을 검증에서 확인했다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f2·f7·f10·f11 을 분류 원문 9장 경계(시설·설비 제어의 '작업 요청·예약·인계·상태 확인')에 대응시킨 추론이며 범위 안이다."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-031 과충전 보호 문구, ref-216, ref-284 승강기 어댑터가 방해 요청을 막는다는 문구가 뒷받침한다. '연계 대상:' 표시가 적절하다."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f9·f13 을 결합한 추론이며 [추정]이 적절하다."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 영역 연결 추론이다. 8. 실시간 세계 상태·데이터 일관성(현재 배터리 상태)과 22. 시뮬레이션·예측용 디지털 트윈(충전 정책 실험)을 구분했고, 27. AI·학습·적응과 모델 운영의 양쪽 연결 규칙도 지켰다."
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
    "ok": true,
    "overlaps": [
      "f23·f24 는 ref-060·ref-103 을 이미 인용한 3. 처리능력·거점·설비 계획·C. 연결·실행 기반 페이지와 겹친다. 기존 각주 id 를 그대로 재사용하고 oq-010 에 연결한다.",
      "f6·f29·f31 은 C. 연결·실행 기반 대분류 연결(2026-09-25-38 f14·f15)과 같은 출처(ref-105·ref-312)를 쓴다. 같은 각주를 재사용한다.",
      "ref-039 는 충전소를 is_parking_spot 으로 설정한다고 적고, ref-104·ref-079 는 is_charger 로 적는다. Open-RMF 문서 사이의 충돌이다."
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
    "원문을 열지 못한 출처 ref-219·ref-098·ref-109·ref-146·ref-060·ref-103·ref-321·ref-858·ref-859·ref-860·ref-861·ref-862·ref-863·ref-866 과, 이번 실행에서 원문을 다시 연 기록이 없는 ref-039 는 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 해당 항목에 source_unopened: true 를 넣는다 — web_fetch_available: false 환경이며 github_raw 로 연 출처만 원문 열람으로 인정된다. (ref-039 는 입력 원문이 있으므로 fetched 로 볼 수 있어 표시에서 빼도 된다.)",
    "f7: ref-039 의 '충전소는 is_parking_spot 으로 설정' 안내를 본문에 쓰지 않는다. 쓰려면 ref-104·ref-079 의 is_charger 와 둘 다 [사실]로 제시하고, 11절 열린 질문에 '출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot(ref-039)과 is_charger(ref-079·ref-104) 가운데 어느 속성으로 하는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 6. 지도·공간·위치 모델 | 근거: f7 | 종류: 출처 충돌'로 올린다 — 같은 발행 주체의 문서끼리 내용이 어긋난다.",
    "f10: 뮤텍스 그룹의 '동시 진입 버그 보고·동작 신뢰성 미확인'은 출처가 없으므로 사실로 쓰지 않는다. 필요하면 '실제 동작 검증은 미확인'이라고만 적는다 — 브리프에 근거 출처가 없다.",
    "f2: 'VDA 5050 은 충전 순서·시점 결정 알고리즘을 규정하지 않는다'를 명세 문구처럼 쓰지 않고 '명세에서 확인되지 않는다'로 적는다 — 원문은 에너지 관리를 관제 기능으로 들 뿐 이를 명시적으로 제외한다고 쓰지 않는다.",
    "f6: recharge_threshold 0.10·recharge_soc 1.0·충전 전류 5.0 A 같은 수치를 쓰면 '템플릿 예시값'임을 밝힌다 — 운영 권장값이 아니다.",
    "f12: '실험적 라이브러리'와 '배포판 포함 여부 미확인'을 함께 적고, ref-866 각주에 원문 미열람을 표시한다 — README raw 경로가 404 였다.",
    "f15~f26 의 연구 결과 문장에는 '저자 보고' 또는 '논문이 보고했다' 형식을 유지하고, f19 에는 프리프린트임을, f20·f23·f24·f26 에는 항만·병원·호텔·배송 로봇 사례로 물류센터 적용이 미확인임을 병기한다 — 단일 출처이고 원문을 열지 못했다.",
    "ref-103 각주의 발행일을 '미확인'에서 '2025-03'으로 고친다 — 검증 검색(PMC·PubMed)이 2025년 3월 Sensors 게재를 확인했다.",
    "ref-863 각주에 게재지 '전자공학회논문지 61(8)'을 넣는다 — 검증 검색(KCI)이 확인했다.",
    "새 열린 질문 2번(시간대별 전기 요금·최대 수요 전력 기반 충전 계획)의 근거를 f17 에서 f2 로 바꾼다 — f17 은 전력 요금을 다루지 않고, f2(관제의 에너지 관리 기능)가 질문의 출발점이다.",
    "f14: [추정]과 '벤더 주장' 병기를 유지하고, 제조사 공식 사이트가 아닌 게재본임을 각주 제목에 남긴다.",
    "f19(학습 기반 충전 결정)는 10절에서 27. AI·학습·적응과 모델 운영과 이 영역 양쪽에 연결하고, 13. 작업 배정 — MRTA 연결에는 f18 을 쓴다 — 분류 원문 8장 교차 규칙에 따른다.",
    "트랙 반영 제안 4건은 6·7·10절에 반영하되, 반영한 문장의 각주는 브리프 출처 id(ref-031·ref-228·ref-079·ref-216·ref-219·ref-109)만 쓴다. 트랙 실행 2026-09-25-19 f19 의 [추정]은 이번 f32 로 대체한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. VDA 5050·Open-RMF·Nav2 출처는 GitHub 공식 저장소 원문을 검증에서 다시 열어 확인했고, 논문 출처는 검색 결과 요약으로만 대조했다. 확인 33건, 미확인 0건, 교차 확인 0건. 강등: 없음. 원문 미열람 출처: ref-219, ref-098, ref-109, ref-146, ref-060, ref-103, ref-321, ref-858, ref-859, ref-860, ref-861, ref-862, ref-863, ref-866. 주의: 표준·오픈소스 내용은 모두 같은 발행 주체의 단일 자료이고, 연구 결과는 논문마다 단일 출처인 저자 보고다. 충전·승강기 병목의 근거인 병원·호텔·항만·배송 로봇 사례가 물류센터에도 적용되는지는 확인되지 않았다(oq-010). 충전소 지정 속성을 두고 Open-RMF 문서끼리 서로 다르게 적는다(ref-039 is_parking_spot, ref-079·ref-104 is_charger). 검증 검색 11회를 더해 이번 실행 검색 상한 30회를 모두 썼다. 그래서 ref-146·ref-219 는 다시 검색하지 않고 기존 등록 출처로 실재를 인정했다. 트랙 반영 제안 4건은 원문으로 다시 확인해 반영을 승인했다. oq-016 은 해결하지 않았다. 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-09-25-40/pages.json

```json
{
  "run_id": "2026-09-25-40",
  "outline": [
    {
      "path": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 650,
      "summary": "로봇마다 같은 충전 임계값으로만 충전을 시작하면 충전 수요가 겹칠 수 있어 충전 시점·충전기 선택·공용 자원 점유를 조율 계층이 함께 맡아야 할 것으로 보인다. [추정][^ref-228][^ref-105]",
      "planned_findings": [
        "f27",
        "f23",
        "f24",
        "f15",
        "f16"
      ]
    },
    {
      "path": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "충전 상태, 임계 저충전 수준, 충전 임계값·목표, 충전 방식, 뮤텍스 그룹, 승강기 세션이 이 영역의 기본 용어다(첫 문장은 태그 없는 연결 문장).",
      "planned_findings": [
        "f3",
        "f4",
        "f6",
        "f10",
        "f11",
        "f15"
      ]
    },
    {
      "path": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md",
      "section": "5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)",
      "budget_chars": 1100,
      "summary": "피킹 성수기에 충전 요청과 층간 출하 운반이 겹치는 가상 시나리오로 충전 작업 삽입·승강기 세션 점유·처리량 손실을 보인다. [추정][^ref-862]",
      "planned_findings": [
        "f7",
        "f3",
        "f11",
        "f13",
        "f2",
        "f28",
        "f29",
        "f31"
      ]
    },
    {
      "path": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1500,
      "summary": "Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다. [사실][^ref-104][^ref-864][^ref-312]",
      "planned_findings": [
        "f7",
        "f8",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f17",
        "f18",
        "f19",
        "f20",
        "f32"
      ]
    },
    {
      "path": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1000,
      "summary": "VDA 5050 은 충전을 startCharging·stopCharging 동작으로 표현하고 팩트시트 batteryCharging·상태 powerSupply 로 배터리 선언과 상태를 담는다. [사실][^ref-031][^ref-228]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f8",
        "f10",
        "f11",
        "f12",
        "f13"
      ]
    },
    {
      "path": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1200,
      "summary": "충전 방식 비교, 배터리 관리 정책, 운반·충전 동시 배정, 승강기 병목 연구로 나누어 정리한다(첫 문장은 태그 없는 연결 문장).",
      "planned_findings": [
        "f15",
        "f16",
        "f17",
        "f18",
        "f19",
        "f20",
        "f21",
        "f22",
        "f23",
        "f24",
        "f25",
        "f26"
      ]
    },
    {
      "path": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)",
      "budget_chars": 650,
      "summary": "ROP 는 여러 제조사 로봇에 걸친 공용 자원 예약·배분과 충전 시점 결정을 맡고, 과충전 보호·정밀 도킹·승강기 운행 제어는 연계 대상으로 보인다. [추정][^ref-031][^ref-216]",
      "planned_findings": [
        "f30",
        "f31",
        "f1"
      ]
    },
    {
      "path": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 800,
      "summary": "13. 작업 배정 — MRTA, 15. 다중 로봇 경로·교통 관리 — MAPF, 10. 설비·건물 시스템 연동, 3. 처리능력·거점·설비 계획 등 여덟 영역과 이어지는 것으로 보인다. [추정][^ref-862]",
      "planned_findings": [
        "f33",
        "f18",
        "f19",
        "f21"
      ]
    },
    {
      "path": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md",
      "section": "11. 열린 질문",
      "budget_chars": 800,
      "summary": "충전·대기 시간의 OEE 손실 분류(oq-016), 물류센터 승강기 병목 자료(oq-010), 충전기 공통 규격·전기 요금 기반 충전·승강기 배분 규칙·충전 하한 기준·충전소 지정 속성 충돌이 남아 있다.",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f7",
        "f11"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "섹션 3~11 신규 작성(트랙 반영 제안 4건 반영, 1차 수정 지시 13건 이행), 2차 수정: 4·8절 연결 문장 태그 제거, 5절 조사 한계 문장 태그·각주 제거와 oq-010 연결, 6절 첫 문장을 출처 범위로 좁힘"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area16-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 16. 공용 자원·충전·에너지 최적화 의 \"6. 대표 접근법과 기술\" 절을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장을 출처 범위(충전 작업 삽입·뮤텍스 그룹·승강기 세션)로 좁혔다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area16-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 16. 공용 자원·충전·에너지 최적화 의 \"8. 대표 연구와 자료\" 절을 옮겼다. 2차 수정: 첫 문장 태그 제거, 병원·호텔 연구 문구를 연관 관계로 고침, ref-863 제목 원문 복원"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area16-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 16. 공용 자원·충전·에너지 최적화 의 \"7. 관련 표준·프레임워크·오픈소스\" 절을 옮겼다(ref-864·ref-866 링크는 id 표기). 2차 수정: batteryCharging 행의 계획 입력 해석을 [추정]으로 분리"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area16-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 16. 공용 자원·충전·에너지 최적화 의 \"11. 열린 질문\" 절을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area16-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 16. 공용 자원·충전·에너지 최적화 의 \"4. 핵심 개념과 용어\" 절을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 연결 문장의 태그·각주 제거"
    }
  ],
  "changelog_entry": "2026-09-25 | 16. 공용 자원·충전·에너지 최적화 | 영역 심화: 3~11절 신규 작성, 트랙 반영 제안 4건 반영, 1차 수정 지시 13건·2차 수정 지시 6건 이행 | run 2026-09-25-40",
  "index_updates": {
    "home_recent": "2026-09-25 — 16. 공용 자원·충전·에너지 최적화: 영역 심화로 3~11절 신규 작성(충전 임계값·충전 작업 삽입·뮤텍스 그룹·승강기 세션, 충전 정책 연구, 트랙 반영 제안 4건 반영)",
    "category_recent": "2026-09-25 — 16. 공용 자원·충전·에너지 최적화: 영역 심화로 3~11절 신규 작성, 새 열린 질문 5건",
    "area_recent": "2026-09-25 — 16. 공용 자원·충전·에너지 최적화: 3~11절 신규 작성(VDA 5050 충전 동작·batteryCharging, Open-RMF 충전 작업 삽입·뮤텍스 그룹·승강기 세션, 충전 정책 연구), 트랙 반영 제안 4건 반영"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "state-of-charge",
      "term_ko": "충전 상태",
      "term_en": "State of Charge (SOC)",
      "definition": "배터리에 남은 충전량을 전체 용량 대비 비율(%)로 나타낸 값으로, VDA 5050 상태 메시지의 stateOfCharge 와 Open-RMF 배터리 갱신이 이 값을 쓴다.",
      "description": "VDA 5050 상태 메시지의 powerSupply 는 충전 상태 외에 충전 중 여부·전압·전류·건강 상태·주행 가능 거리를 담으며, 좋음·나쁨만 아는 로봇은 80%·20%로 보고한다.",
      "related_areas": [
        16,
        8,
        9
      ],
      "sources": [
        "ref-051",
        "ref-865"
      ]
    },
    {
      "action": "new",
      "slug": "mutex-group",
      "term_ko": "뮤텍스 그룹",
      "term_en": "Mutex Group (Open-RMF)",
      "definition": "Open-RMF 교통 그래프에서 같은 그룹에 묶인 경유점·차선을 한 번에 한 로봇만 점유하도록 하는 상호 배제 단위이다.",
      "related_areas": [
        16,
        15
      ],
      "sources": [
        "ref-864"
      ]
    },
    {
      "action": "new",
      "slug": "lift-session",
      "term_ko": "승강기 세션",
      "term_en": "Lift Session (Open-RMF)",
      "definition": "Open-RMF 에서 한 요청자가 세션 id 로 승강기 제어권을 받아 세션 종료 요청을 보낼 때까지 점유하는 단위이다.",
      "related_areas": [
        16,
        10
      ],
      "sources": [
        "ref-312",
        "ref-286"
      ]
    },
    {
      "action": "new",
      "slug": "battery-swapping",
      "term_ko": "배터리 교환",
      "term_en": "Battery Swapping",
      "definition": "방전된 로봇 배터리를 충전기에 꽂아 기다리는 대신 충전된 배터리로 바꿔 끼워 로봇을 곧바로 다시 운행하게 하는 충전 방식이다.",
      "related_areas": [
        16,
        3
      ],
      "sources": [
        "ref-098"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 최신판(main, 3.0.0) 명세 원문. 이번 실행은 startCharging·stopCharging 동작, 관제의 에너지 관리 기능, 구역 유형을 원문으로 확인했다.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-039",
      "org": "Open Robotics",
      "title": "Currently supported Tasks - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/task_types.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 지원 작업 유형 문서. 충전 작업이 플릿 어댑터가 스스로 만드는 작업이라는 서술과, 충전소를 is_parking_spot 으로 설정한다는 안내(다른 문서의 is_charger 와 충돌)를 담는다.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 상태 메시지 JSON 스키마. 이번 실행은 powerSupply 항목을 원문으로 확인했다.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-060",
      "org": "Lee, Y. 외(Digital Health)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026",
      "url": "https://doi.org/10.1177/20552076261437181",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 병원 약품 배송 로봇의 승강기 이용과 배송 실패·시간의 관계를 다룬 논문.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-079",
      "org": "Open Robotics",
      "title": "Traffic Editor - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 교통 편집기 문서. 이번 실행은 is_charger·dock_name·대기 지점 속성과 승강기를 공유 자원으로 보는 서술을 원문으로 확인했다.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-098",
      "org": "Zou, B., Gong, Y., de Koster, R., & Xu, X.",
      "title": "Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system",
      "published": "2018",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RMFS 에서 플러그인·교환·유도 충전 전략을 반개방형 대기행렬 네트워크와 시뮬레이션으로 비교한 EJOR 논문.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-103",
      "org": "PMC 게재 논문(저자 미확인)",
      "title": "The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments",
      "published": "2025-03",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 다층 호텔 배송 로봇 경로 계획에서 승강기 대기·운행 시간을 모델링한 Sensors 게재 논문(2025년 3월, 검증 검색 확인).",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-104",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_demos — Demonstrations of Open-RMF (README)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_demos",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 데모 README. 이번 실행은 충전 작업의 일정 삽입과 로봇별 전용 충전 위치 가정을 원문으로 확인했다.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
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
      "accessed": "2026-09-25",
      "summary": "플릿 어댑터 설정 템플릿. 이번 실행은 충전 임계값·충전 목표·배터리·전력 소비·작업 종료 동작·로봇별 충전기 항목을 원문으로 확인했다(수치는 예시값).",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-109",
      "org": "Stark, H.-G. 외",
      "title": "A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse",
      "published": "2024-06",
      "url": "https://arxiv.org/abs/2406.17003",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 창고 충전소 배치를 PageRank 와 비슷한 방법으로 최적화한 프리프린트.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-146",
      "org": "Omega 게재 논문(저자 미확인)",
      "title": "The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority",
      "published": "2024",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RMFS 성능 평가에 에너지 소비를 넣고 동적 우선순위 운영 정책을 다룬 논문(제목 기준).",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-216",
      "org": "ROS Navigation (ros-navigation/navigation2 GitHub)",
      "title": "nav2_docking — README (Open Navigation's Nav2 Docking Framework)",
      "published": null,
      "url": "https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "Nav2 도킹 프레임워크 README. 이번 실행은 도크 데이터베이스, 충전·비충전 도크 플러그인, 센서 보정, 충전 확인 함수를 원문으로 확인했다.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-219",
      "org": "Mobile Industrial Robots(MiR) (ManualsLib 게재본)",
      "title": "MiR Charge 24V Operating Manual — Setting charging station markers on the map (제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본)",
      "published": null,
      "url": "https://www.manualslib.com/manual/1941068/Mir-Mir-Charge-24v.html?page=23",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이번 실행에서 다시 열지 않았다. 지도에 충전 스테이션 마커를 설정하는 매뉴얼 절.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-228",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/factsheet.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 팩트시트 JSON 스키마. 이번 실행은 batteryCharging 네 항목을 원문으로 확인했다.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-284",
      "org": "Open Robotics",
      "title": "Lifts (integration_lifts) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_lifts.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 승강기 연동 문서. 이번 실행은 승강기 어댑터의 역할을 원문으로 확인했다(여러 플릿 사이 배분 규칙은 문서에 없음).",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
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
      "accessed": "2026-09-25",
      "summary": "승강기 상태 메시지. 이번 실행은 제어권을 받은 세션 id 기록과 운영 모드를 원문으로 확인했다.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
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
      "accessed": "2026-09-25",
      "summary": "승강기 요청 메시지. 이번 실행은 세션 id, 요청 유형, AGV 모드의 문 동작을 원문으로 확인했다.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-321",
      "org": "Electronics(MDPI) 게재 논문(저자 미확인)",
      "title": "Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots",
      "published": "2025",
      "url": "https://doi.org/10.3390/electronics14050982",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 실내 배송 로봇의 다층 경로 계획에서 승강기 선택을 최적화한 논문.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-377",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 작업 계획기 헤더. 이번 실행은 충전량 부족 오류 구분과 배터리 우선 비용 설정을 원문으로 확인했다.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-858",
      "org": "Computers & Industrial Engineering 게재 논문(저자 미확인)",
      "title": "Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach",
      "published": "2024-08",
      "url": "https://www.sciencedirect.com/science/article/pii/S0360835224006314",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 충전소 사용 중·대기 확률을 확률 변수로 둔 다중 AGV 충전 순서 최적화(혼합 정수 선형 계획) 논문.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-859",
      "org": "arXiv 2607.05683 저자(미확인)",
      "title": "Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers",
      "published": "2026-07",
      "url": "https://arxiv.org/abs/2607.05683",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 다중 블록 창고에서 PPO 기반 강화학습으로 충전소 선택과 충전 시간을 학습하는 프리프린트.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-860",
      "org": "Ma, N., Zhou, C., & Stephen, A.",
      "title": "Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals",
      "published": "2020",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자동화 컨테이너 터미널의 충전소 배치와 배터리 AGV 충전 정책을 시뮬레이션으로 평가한 논문(Simulation Modelling Practice and Theory 106).",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-861",
      "org": "Chen, W., Gong, Y., Chen, Q., & Wang, H.",
      "title": "Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse",
      "published": "2024-01",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자가 등반 로봇 창고에서 충전 기술·충전 정책·충전기 대수를 반개방형 대기행렬 네트워크로 분석한 EJOR 312(1) 논문.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-862",
      "org": "Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D.",
      "title": "Scheduling heterogeneous multi-load AGVs with battery constraints",
      "published": "2021-12",
      "url": "https://www.sciencedirect.com/science/article/pii/S0305054821002586",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 운반·충전 요청을 함께 배정·순서화하고 부분 충전 시간을 정하는 MILP·적응형 대규모 이웃 탐색 논문(Computers & Operations Research).",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-863",
      "org": "박재범, 조성준, 김준식, 유범재(전자공학회논문지 61(8))",
      "title": "배송 로봇의 다층, 다중 배송을 위한 효율적인 경로 계획 및 엘리베이터 층간 이동 시스템",
      "published": "2024",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003107904",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서버 기반 엘리베이터 제어 모듈과 노드 그래프 기반 다층·다중 목적지 경로 계획을 제안하고 실증 시험한 국내 논문(전자공학회논문지 61(8), 검증 검색 확인).",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-864",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 교통 그래프 헤더. 경유점·차선의 뮤텍스 그룹(한 번에 한 로봇만 점유), 충전 경유점·주차 지점·대기 지점, 문·승강기 문 차선 조건을 정의한다. 이번 실행에서 원본을 열었다.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-865",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "플릿 어댑터 로봇 갱신 인터페이스 헤더. 로봇별 충전 경유점 지정, 주차 예약 시스템 사용 설정, 배터리 충전 상태 갱신, 승강기 세션 정보를 다룬다. 이번 실행에서 원본을 열었다.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-866",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_reservation — Experimental reservation library in rust (GitHub)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_reservation",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 충전기 같은 자원을 시간 범위 안에서 정해진 시간 동안 로봇에 배정하는 실험적 제약 자원 스케줄링 라이브러리(검색 요약 기준). README raw 경로는 404, 배포판 포함 여부 미확인.",
      "cited_by": [
        "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md"
      ],
      "source_unopened": true
    }
  ],
  "standards_updates": [
    {
      "name": "Open-RMF rmf_traffic (교통 그래프·뮤텍스 그룹)",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp",
      "related_areas": [
        16,
        15
      ],
      "summary": "Open-RMF 교통 그래프 헤더로, 같은 뮤텍스 그룹의 경유점·차선을 한 번에 한 로봇만 점유하게 하고 충전 경유점·주차·대기 지점을 정의한다.",
      "ref_id": "ref-864"
    },
    {
      "name": "Open-RMF rmf_reservation (실험적 예약 라이브러리)",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_reservation",
      "related_areas": [
        16
      ],
      "summary": "충전기 같은 자원을 시간 범위 안에서 로봇에 배정하는 실험적 제약 자원 스케줄링 라이브러리로 소개된다(원문 미열람, 배포판 포함 여부 미확인).",
      "ref_id": "ref-866"
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "제조사가 다른 이동로봇이 같은 충전기를 함께 쓸 수 있게 하는 충전 커넥터·충전 통신의 공통 규격이나 공개 사례가 있는가?",
      "areas": [
        16,
        28
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "물류센터 로봇의 충전 시점을 시간대별 전기 요금이나 최대 수요 전력 기준으로 계획한 연구나 국내 사례가 있는가?",
      "areas": [
        16,
        4
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "여러 제조사 플릿이 한 승강기를 함께 쓸 때 세션 순서·최대 점유 시간·목적층 묶음을 정하는 배분 규칙을 공개한 표준이나 구현이 있는가?",
      "areas": [
        16,
        10
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "충전 하한을 제조사가 팩트시트로 선언한 값(criticalLowChargingLevel)과 ROP 운영 설정(recharge_threshold) 가운데 어느 것으로 삼고, 둘이 다르면 어떻게 조정하는가?",
      "areas": [
        16,
        5
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot(지원 작업 문서)과 is_charger(교통 편집기 문서·데모 README) 가운데 어느 속성으로 하는가?",
      "areas": [
        16,
        6
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [
    {
      "step": "피킹",
      "item": "시작 조건",
      "link": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "16. 공용 자원·충전·에너지 최적화"
    },
    {
      "step": "피킹",
      "item": "작업 대상",
      "link": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "16. 공용 자원·충전·에너지 최적화"
    },
    {
      "step": "피킹",
      "item": "수행 자원",
      "link": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "16. 공용 자원·충전·에너지 최적화"
    },
    {
      "step": "피킹",
      "item": "제약",
      "link": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "16. 공용 자원·충전·에너지 최적화"
    },
    {
      "step": "피킹",
      "item": "완료·인계",
      "link": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "16. 공용 자원·충전·에너지 최적화"
    },
    {
      "step": "피킹",
      "item": "예외·성과",
      "link": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "16. 공용 자원·충전·에너지 최적화"
    },
    {
      "step": "출하",
      "item": "시작 조건",
      "link": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "16. 공용 자원·충전·에너지 최적화"
    },
    {
      "step": "출하",
      "item": "작업 대상",
      "link": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "16. 공용 자원·충전·에너지 최적화"
    },
    {
      "step": "출하",
      "item": "수행 자원",
      "link": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "16. 공용 자원·충전·에너지 최적화"
    },
    {
      "step": "출하",
      "item": "제약",
      "link": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "16. 공용 자원·충전·에너지 최적화"
    },
    {
      "step": "출하",
      "item": "완료·인계",
      "link": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "16. 공용 자원·충전·에너지 최적화"
    },
    {
      "step": "출하",
      "item": "예외·성과",
      "link": "docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "16. 공용 자원·충전·에너지 최적화"
    }
  ],
  "additional_research_requests": [
    "11절 oq-016: 이동로봇 플릿의 충전·대기·교통 정체 시간을 OEE 손실로 분류한 정의나 사례가 필요하다 — 이번 브리프에 근거가 없어 해결하지 못했다.",
    "3·5절: 국내 물류센터의 충전 대기·승강기 대기가 처리량에 주는 영향을 정량화한 자료가 필요하다 — 현재 근거는 병원·호텔·항만·배송 로봇 사례뿐이다(oq-010).",
    "6·7절: rmf_reservation README 원문과 배포판 포함 여부 확인이 필요하다 — 원문 미열람(404)이라 실험적 라이브러리로만 적었다.",
    "6절: 뮤텍스 그룹의 실제 동작 신뢰성(동시 진입 문제 보고)의 출처 확인이 필요하다 — 브리프에 출처가 없어 '실제 동작 검증은 미확인'으로만 적었다.",
    "8절: ref-858 저자, ref-146·ref-321 의 결과 수치, 논문 원문 대조가 필요하다 — 모두 검색 요약·제목 수준이다.",
    "11절: 시간대별 전기 요금·최대 수요 전력 기반 로봇 충전 계획의 학술·국내 출처가 필요하다.",
    "4·6절: 배터리 교환 방식을 쓰는 국내 물류 로봇 사례가 있으면 현장 시나리오 보강에 필요하다.",
    "5절: 흐름 매트릭스의 피킹·출하 두 단계가 한 시나리오 표를 공유한다 — 단계별로 나눈 시나리오를 쓰려면 출하 단계 충전·승강기 대기의 근거가 더 필요하다."
  ],
  "fixes_applied": [
    "원문 미열람 표시 — ref-219·ref-098·ref-109·ref-146·ref-060·ref-103·ref-321·ref-858·ref-859·ref-860·ref-861·ref-862·ref-863·ref-866 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다. ref-039 는 브리프가 github_raw 로 열었다고 기록했고 지시가 제외를 허용하므로 표시하지 않았다.",
    "f7 is_parking_spot 충돌 — 6절 '충전소 위치 정보의 출처'에 ref-039(is_parking_spot)와 ref-079·ref-104(is_charger)를 모두 [사실]로 제시하고, 11절과 open_question_updates 에 '출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot 과 is_charger 가운데 어느 속성으로 하는가?'(관련 영역 16·6)를 올렸다.",
    "f10 — 동시 진입 버그 보고는 쓰지 않고 6절 뮤텍스 그룹 문장에 '실제 동작 검증은 미확인'만 적었다.",
    "f2 — 7절 VDA 5050 관제 기능 행에 '충전 순서·시점 결정 방법은 명세에서 확인되지 않는다'로 적고 명세 문구처럼 쓰지 않았다.",
    "f6 — 4절과 6절·7절에서 0.10·1.0·5.0 A 등 수치를 템플릿 예시값이며 운영 권장값이 아니라고 밝혔다.",
    "f12 — 6·7절에 '실험적 라이브러리'와 '배포판 포함 여부는 미확인'을 함께 적고 ref-866 각주에 원문 미열람을 표시했다.",
    "f15~f26 — 연구 결과 문장을 '보고했다'·'저자 보고' 형식으로 쓰고, f19 에 프리프린트, f20(항만)·f23(병원)·f24(호텔)·f26(배송 로봇)에 물류센터 적용 미확인을 병기했다(3·6·8절).",
    "ref-103 — 각주 발행일을 2025-03 으로 쓰고 reference_updates 의 published 도 2025-03 으로 고쳤다.",
    "ref-863 — 각주 기관 표기에 '전자공학회논문지 61(8)'을 넣고 reference_updates 의 org·summary 에도 반영했다.",
    "새 열린 질문 2번(전기 요금·최대 수요 전력) — 근거를 f2 로 바꿔 11절에서 ref-031(관제의 에너지 관리) 각주를 달았다.",
    "f14 — 6절에서 [추정] 벤더 주장 병기를 유지하고 ref-219 각주 제목에 제조사 공식 사이트가 아닌 게재본임을 남겼다.",
    "f19·f18 — 10절에서 f19 를 27. AI·학습·적응과 모델 운영 연결에, f18 을 13. 작업 배정 — MRTA 연결에 쓰고, 6절에도 27. AI·학습·적응과 모델 운영 링크를 두었다.",
    "트랙 반영 제안 4건 — 6절(충전소 위치 정보 출처: ref-079·ref-216·ref-219), 7절(VDA 5050 startCharging·stopCharging·구역 유형 ref-031, batteryCharging ref-228, Nav2 도킹 ref-216), 10절(Stark 외 2024 ref-109 → 3. 처리능력·거점·설비 계획)에 반영했고, 트랙 실행 2026-09-25-19 f19 의 [추정] 대신 이번 f32 를 썼다.",
    "분량 초과 자동 분리: 16. 공용 자원·충전·에너지 최적화 본문 9,913자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,779자",
    "2차: ref-863 제목 복원 — 주제 페이지 2026-09-25-area16-s8 의 출처 절 ref-863 각주 제목을 원 제목 '배송 로봇의 다층, 다중 배송을 위한 효율적인 경로 계획 및 엘리베이터 층간 이동 시스템'(쉼표)으로 되돌렸다.",
    "2차: 6절 첫 문장 — 세부영역 페이지 6절과 주제 페이지 s6 의 세 줄 요약·본문 첫 문장을 'Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다.'로 좁혀 '대표 접근'과 '예약'을 뺐다(예약은 본문 소절에서 ref-866·실험적 표시와 함께만 둔다).",
    "2차: 5절 마지막 문장 — [사실] 태그와 ref-060·ref-103 각주를 빼고 조사 한계 문장으로 바꿔 열린 질문 페이지의 oq-010 에 연결했다.",
    "2차: 4·8절 첫 문장 — 세부영역 페이지와 주제 페이지 s4·s8 의 세 줄 요약·본문 첫 문장에서 [사실] 태그와 각주를 뺐고, 8절 첫 문장은 '이 절은 … 나누어 정리한다'는 태그 없는 연결 문장으로 바꿨다.",
    "2차: 8절 병원·호텔 항목 — 주제 페이지 s8 에서 병원 연구를 '승강기 가동률이 높을수록 배송 실패가 많고 배송 시간이 길었다'로, 호텔 연구를 '승강기 운행 시간을 늘리면 총 이동 시간이 늘었다'로 나눠 고쳐 인과 표현을 없앴다.",
    "2차: 7절 batteryCharging 행 — 주제 페이지 s7 표에서 네 항목 선언은 [사실]로 두고 '충전 시점 계획의 입력이 될 수 있을 것으로 보인다'를 [추정] 문장으로 떼어 적었다."
  ]
}
```

### runs/2026-09-25-40/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-25-40/pages/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md

```markdown
---
title: "16. 공용 자원·충전·에너지 최적화"
type: area
category: "D. 계획·최적화"
area_no: 16
related_areas: [3, 5, 8, 10, 13, 15, 22, 27]
tags: [충전 상태, 충전 임계값, 뮤텍스 그룹, 승강기 세션, VDA 5050, Open-RMF]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-031, ref-039, ref-051, ref-060, ref-079, ref-098, ref-103, ref-104, ref-105, ref-109, ref-146, ref-216, ref-219, ref-228, ref-284, ref-286, ref-312, ref-321, ref-377, ref-858, ref-859, ref-860, ref-861, ref-862, ref-863, ref-864, ref-865, ref-866]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [D. 계획·최적화](index.md) › 16. 공용 자원·충전·에너지 최적화

# 16. 공용 자원·충전·에너지 최적화

!!! info "소속 대분류"
    [D. 계획·최적화](index.md) — 핵심 질문:
    누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 [분류원문]

## 2. SCM 관점의 질문

로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]

## 3. 왜 중요한가

로봇마다 같은 충전 임계값(VDA 5050 의 criticalLowChargingLevel, Open-RMF 의 recharge_threshold)으로만 충전을 시작하면 충전 수요가 겹칠 수 있으므로, 충전소 대기를 반영한 충전 시점·충전기 선택, 공유 충전기의 우선 충전 정책, 충전기·승강기 점유의 예약·세션 관리를 조율 계층이 함께 맡아야 할 것으로 보인다. [추정][^ref-228][^ref-105][^ref-858][^ref-859][^ref-861][^ref-312]

공용 자원의 대기는 곧 처리 시간 손실로 나타난다. 고밀도 병원 환경의 약품 배송 로봇 연구는 승강기 가동률이 높을수록 배송 실패가 많고 배송 시간이 길었다고 보고했다(병원 사례이며 물류센터 적용은 미확인). [사실][^ref-060] 다층 호텔 배송 경로 계획 연구는 고객 노드 60개 시나리오에서 승강기 운행 시간을 40초에서 100초로 늘리면 총 이동 시간이 약 225초에서 500초로 거의 두 배가 된다고 보고했다(호텔 사례이며 물류센터 적용은 미확인). [사실][^ref-103]

충전 방식과 정책도 처리량과 비용을 바꾼다. Zou 외(2018)는 로봇 이동형 풀필먼트 시스템에서 유도 충전이 회수 처리 시간에서 가장 좋았고, 배터리 비용이 낮으면 배터리 교환이 플러그인 충전보다 싸다고 보고했다. [사실][^ref-098] Chen 외(2024)는 자가 등반 로봇 창고에서 우선 충전 정책이 전용 충전 정책보다 비용 효율적이라고 보고했다. [사실][^ref-861]

## 4. 핵심 개념과 용어

앞 절의 문제를 다루려면 배터리 상태와 공용 자원 점유를 표현하는 용어가 먼저 필요하다.

자세한 내용은 주제 페이지 [16. 공용 자원·충전·에너지 최적화 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area16-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

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
| 예외·성과 | VDA 5050 은 충전 주문이 운반 주문을 중단시킬 수 있다고 적는다. [사실][^ref-031] 여러 로봇이 비슷한 시각에 충전 하한에 닿아 충전기 대기열이 생기면 가용 로봇 수가 줄 수 있으므로, 주문이 적은 시간대의 기회 충전이나 충전 요청을 작업 배정과 함께 계획하는 방식이 처리량 손실을 줄이는 수단이 될 것으로 보인다. [추정][^ref-862][^ref-859][^ref-031] |

이 시나리오에서 이 영역이 관여하는 곳은 시작 조건(충전 작업을 언제 넣을지), 제약(충전 하한과 승강기 점유), 예외·성과(충전으로 빠지는 가용 로봇과 층간 대기)다. 화물의 인계 확인 자체는 다른 영역이 다룬다(가정).

실제 물류센터에서 충전 대기와 승강기 대기가 처리량을 얼마나 줄이는지는 이번 조사에서 확인되지 않았으며, [열린 질문](../../open-questions.md)의 oq-010 으로 남겨 둔다.

## 6. 대표 접근법과 기술

Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다. [사실][^ref-104][^ref-864][^ref-312]

자세한 내용은 주제 페이지 [16. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area16-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

VDA 5050 은 충전을 동작과 배터리 선언·상태 필드로 표현하고, Open-RMF 는 충전 설정·작업 계획기·교통 그래프·승강기 메시지로 공용 자원을 다룬다. [사실][^ref-031][^ref-105] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [16. 공용 자원·충전·에너지 최적화 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area16-s7.md)에 있다.

## 8. 대표 연구와 자료

이 절은 충전 방식·정책의 처리량·비용 효과를 대기행렬로 분석한 창고 연구, 충전을 작업 배정·순서와 함께 푸는 최적화 연구, 승강기를 층간 병목으로 다룬 배송 로봇 연구로 나누어 정리한다.

자세한 내용은 주제 페이지 [16. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료](../../topics/2026/2026-09-25-area16-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

ROP 가 직접 맡을 범위는 여러 제조사 로봇에 걸친 충전기·승강기·통로 구간·대기 위치의 예약과 배분, 충전 시점과 충전 목표 결정, 배터리 상태를 반영한 작업 배정 입력인 것으로 보인다. [추정][^ref-031][^ref-104][^ref-864][^ref-312]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 충전 시점·충전 목표 결정, 충전 시작·중지 요청, 배터리 상태 확인과 작업 배정 반영 | 과충전 보호, 충전기와의 통신·정밀 도킹, 배터리 관리 장치 |
| 시설·설비 제어 | 충전기·승강기·통로 구간·대기 위치의 예약과 배분, 승강기 세션 요청과 모드 확인 | 승강기 운행·설비 안전 제어 |

이 직접 범위는 VDA 5050 이 관제의 에너지 관리로 두고 Open-RMF 가 충전 작업 삽입·뮤텍스 그룹·승강기 세션으로 다루는 층위에 해당하는 것으로 보인다. [추정][^ref-031][^ref-104][^ref-864][^ref-312] 과충전 보호는 VDA 5050 이 이동로봇의 책임으로 명시한다. [사실][^ref-031] 정밀 도킹·충전 확인은 로봇 쪽 프레임워크가, 승강기 동작을 방해하는 요청의 차단은 승강기 어댑터가 맡으므로, ROP 는 요청과 상태 확인까지를 담당하는 연계 구조로 보인다. [추정][^ref-216][^ref-284] 경계의 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 충전과 공용 자원 점유를 매개로 배정·교통·설비 연동·설비 계획·능력 모델·상태 모델·시뮬레이션·학습 영역과 이어지는 것으로 보인다. [추정][^ref-862][^ref-864][^ref-312]

- [13. 작업 배정 — MRTA](13-task-allocation-mrta.md) — 운반 요청과 충전 요청을 함께 배정·순서화하는 연구가 두 영역을 잇는다. [추정][^ref-862]
- [15. 다중 로봇 경로·교통 관리 — MAPF](15-multi-robot-path-and-traffic-management-mapf.md) — 뮤텍스 그룹·대기 지점이 통로 구간 점유와 교통 조율을 공유한다. [추정][^ref-864]
- [10. 설비·건물 시스템 연동](../c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) — 승강기 세션 요청·상태 확인이 설비 연동 인터페이스 위에서 이루어진다. [추정][^ref-312]
- [3. 처리능력·거점·설비 계획](../a-business-supply-chain-design/03-capacity-site-and-facility-planning.md) — 충전기 대수 결정과 창고 충전소 배치 최적화(Stark 외 2024)가 설비 계획으로 이어진다. [추정][^ref-861][^ref-109]
- [5. 로봇 능력·작업 온톨로지](../b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) — 팩트시트의 충전 설정(batteryCharging)이 로봇 선언의 일부다. [추정][^ref-228]
- [8. 실시간 세계 상태·데이터 일관성](../b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md) — 현재 배터리 상태(충전 상태·충전 중 여부)를 표현한다. [추정][^ref-051]
- [22. 시뮬레이션·예측용 디지털 트윈](../f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) — 충전소 배치·충전 정책을 가정해 미래를 실험하는 시뮬레이션이 이어진다(현재 상태 표현과 구분). [추정][^ref-860]
- [27. AI·학습·적응과 모델 운영](../g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) — 강화학습 기반 충전소 선택·충전 시간 결정이 이 영역에 적용되는 연구 방법이다. [추정][^ref-859]

## 11. 열린 질문

충전·대기 시간을 성과 지표에서 어떻게 분류할지, 물류센터에서 충전·승강기 병목이 얼마나 되는지, 제조사가 다른 로봇이 충전기·승강기를 어떤 규칙으로 나눠 쓸지가 아직 확인되지 않았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [16. 공용 자원·충전·에너지 최적화 — 열린 질문](../../topics/2026/2026-09-25-area16-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
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
[^ref-858]: Computers & Industrial Engineering 게재 논문(저자 미확인), Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach, 2024-08, https://www.sciencedirect.com/science/article/pii/S0360835224006314, 접근일 2026-09-25 (원문 미열람)
[^ref-859]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-860]: Ma, N., Zhou, C., & Stephen, A., Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals, 2020, https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X, 접근일 2026-09-25 (원문 미열람)
[^ref-861]: Chen, W., Gong, Y., Chen, Q., & Wang, H., Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse, 2024-01, https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770, 접근일 2026-09-25 (원문 미열람)
[^ref-862]: Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D., Scheduling heterogeneous multi-load AGVs with battery constraints, 2021-12, https://www.sciencedirect.com/science/article/pii/S0305054821002586, 접근일 2026-09-25 (원문 미열람)
[^ref-864]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-09-25
```

### docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md

```markdown
---
title: "16. 공용 자원·충전·에너지 최적화"
type: area
category: "D. 계획·최적화"
area_no: 16
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [D. 계획·최적화](index.md) › 16. 공용 자원·충전·에너지 최적화

# 16. 공용 자원·충전·에너지 최적화

!!! info "소속 대분류"
    [D. 계획·최적화](index.md) — 핵심 질문:
    누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 [분류원문]

## 2. SCM 관점의 질문

로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]

## 3. 왜 중요한가

아직 작성되지 않음

## 4. 핵심 개념과 용어

아직 작성되지 않음

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

아직 작성되지 않음

## 6. 대표 접근법과 기술

아직 작성되지 않음

## 7. 관련 표준·프레임워크·오픈소스

아직 작성되지 않음

## 8. 대표 연구와 자료

아직 작성되지 않음

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

아직 작성되지 않음

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

아직 작성되지 않음

## 11. 열린 질문

아직 작성되지 않음

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

(아직 각주가 없다. 본문이 작성되면 출처 각주를 여기에 둔다.)
```

### runs/2026-09-25-40/pages/topics/2026/2026-09-25-area16-s6.md

```markdown
---
title: "16. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술"
type: topic
category: "D. 계획·최적화"
primary_area_no: 16
related_areas: [3, 5, 8, 10, 13, 15, 22, 27]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-039, ref-079, ref-104, ref-105, ref-216, ref-219, ref-286, ref-312, ref-377, ref-858, ref-859, ref-860, ref-862, ref-864, ref-865, ref-866]
last_run: 2026-09-25
version: 1
split_from: docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#6
---

[홈](../../index.md) › [주제](../index.md) › 16. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술

# 16. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다. [사실][^ref-104][^ref-864][^ref-312]
- 이 페이지는 [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다. [사실][^ref-104][^ref-864][^ref-312]

### 임계값 기반 충전 작업 삽입

Open-RMF 에서 충전 작업은 플릿 어댑터가 스스로 만드는 작업이며, 로봇이 일련의 작업을 마칠 충전량이 부족하면 작업 계획기가 충전(ChargeBattery) 작업을 일정에 끼워 넣고, 현재는 로봇마다 전용 충전 위치가 있다고 가정한다. [사실][^ref-039][^ref-104] 작업 계획기는 충전소로 돌아갈 초기 충전량조차 없거나 요청을 감당할 배터리 용량이 없는 경우를 오류로 구분하고, 낮은 충전 상태를 이차항으로 강하게 벌점하는 배터리 우선 비용 설정을 둔다. [사실][^ref-377] 플릿 어댑터 설정은 배터리 전압·용량·충전 전류, 주변·도구 장치 소비 전력, 배터리 소모 반영 여부, 작업 종료 후 동작(park·charge·nothing), 로봇별 전용 충전기를 둔다(충전 전류 5.0 A 등 수치는 템플릿 예시값). [사실][^ref-105]

### 공용 자원의 상호 배제·세션·예약

Open-RMF 교통 그래프는 경유점·차선을 뮤텍스 그룹에 넣어 한 번에 한 로봇만 점유하게 할 수 있다(실제 동작 검증은 미확인). [사실][^ref-864] 승강기는 요청자별 세션 id 로 점유되고, AGV 모드에서는 승강기가 멈추면 문이 계속 열려 있다. [사실][^ref-312][^ref-286] 실험적 라이브러리 rmf_reservation 은 로봇이 충전기 같은 자원을 주어진 시간 범위 안에서 정해진 시간 동안 쓰겠다고 요청하면 해법기가 로봇을 자원에 배정하는 제약 자원 스케줄링을 제공한다고 소개되며, 배포판 포함 여부는 미확인이다. [사실][^ref-866] 플릿 어댑터의 주차 예약 시스템 사용은 기본값이 꺼짐이지만 켜기를 권장한다. [사실][^ref-865]

### 충전 시점·순서·충전기 선택 최적화

다중 AGV 충전 순서 최적화 연구(2024)는 도착 시 충전소가 사용 중일 확률과 대기 확률을 충전소마다 확률 변수로 두고 총 주행 시간 기댓값을 최소화하는 혼합 정수 선형 계획을 세웠으며, 허용 최대치까지 완전 충전하는 것이 최적이라고 보고했다. [사실][^ref-858] Dang 외(2021)는 운반 요청과 충전 요청을 함께 배정·순서화하고 임계 배터리 수준을 지키는 부분 충전 시간을 정하는 방법으로 현행 대비 비용을 약 20~50% 줄였다고 보고했다(저자 보고). [사실][^ref-862] 근접 정책 최적화(Proximal Policy Optimization, PPO) 기반 강화학습 프리프린트는 확률적 주문 도착 하에서 충전소 대기 예상 시간을 반영해 충전소 선택과 충전 시간을 학습하며, 고정 규칙 휴리스틱이 동적 환경에서 비효율적이라고 지적한다(프리프린트, 저자 보고). [사실][^ref-859] 이 학습 기반 결정은 [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)의 연구 방법을 이 영역에 적용한 사례다. [추정][^ref-859] Ma 외(2020)는 컨테이너 터미널 시뮬레이션에서 분산형 충전소 배치와 점진적 재충전 정책이 좋은 성능을 낸다고 보고했다(항만 사례이며 물류센터 적용은 미확인). [사실][^ref-860]

### 충전소 위치 정보의 출처

Open-RMF 에서 충전기 위치는 Traffic Editor 경유점의 is_charger 수동 주석으로 들어가 배터리가 임계값 아래로 떨어진 로봇이 그곳으로 보내지며, 로봇별 충전 경유점을 지정하지 않으면 그래프에서 가장 가까운 충전 경유점을 쓴다. [사실][^ref-079][^ref-864][^ref-865] 한편 Open-RMF 지원 작업 문서는 충전소를 is_parking_spot 으로 설정한다고 적어 is_charger 로 적는 문서와 어긋난다. [사실][^ref-039][^ref-079][^ref-104] 연계 대상인 Nav2 도킹 프레임워크는 도크 인스턴스(유형과 [x, y, θ] 위치)의 데이터베이스를 두고 충전 도크와 비충전 도크(컨베이어·팔레트 등)를 플러그인으로 구분하며 센서로 도크 자세를 보정한다. [사실][^ref-216] MiR 충전 스테이션 매뉴얼 게재본은 지도에 충전 스테이션 마커를 두고 로봇이 이를 감지해 도킹한다고 설명한다. [추정] 벤더 주장[^ref-219] 충전소 정보가 설비 위치(도크 자세)와 경로 그래프의 접근 지점(is_charger 경유점)으로 나뉘어 관리되므로, ROP 의 공용 자원 모델도 충전기 설비와 접근 경유점을 분리해 두어야 할 것으로 보인다. [추정][^ref-216][^ref-079][^ref-865]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)
- 관련 영역: [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

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
[^ref-858]: Computers & Industrial Engineering 게재 논문(저자 미확인), Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach, 2024-08, https://www.sciencedirect.com/science/article/pii/S0360835224006314, 접근일 2026-09-25 (원문 미열람)
[^ref-859]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-860]: Ma, N., Zhou, C., & Stephen, A., Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals, 2020, https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X, 접근일 2026-09-25 (원문 미열람)
[^ref-862]: Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D., Scheduling heterogeneous multi-load AGVs with battery constraints, 2021-12, https://www.sciencedirect.com/science/article/pii/S0305054821002586, 접근일 2026-09-25 (원문 미열람)
[^ref-864]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-09-25
[^ref-865]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 접근일 2026-09-25
[^ref-866]: Open Robotics (open-rmf), rmf_reservation — Experimental reservation library in rust (GitHub), 미확인, https://github.com/open-rmf/rmf_reservation, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-40 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-40 | 16. 공용 자원·충전·에너지 최적화 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-25-40/pages/topics/2026/2026-09-25-area16-s8.md

```markdown
---
title: "16. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료"
type: topic
category: "D. 계획·최적화"
primary_area_no: 16
related_areas: [3, 5, 8, 10, 13, 15, 22, 27]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-060, ref-098, ref-103, ref-109, ref-146, ref-321, ref-858, ref-859, ref-860, ref-861, ref-862, ref-863]
last_run: 2026-09-25
version: 1
split_from: docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#8
---

[홈](../../index.md) › [주제](../index.md) › 16. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료

# 16. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 절은 충전 방식·정책의 처리량·비용 효과를 대기행렬로 분석한 창고 연구, 충전을 작업 배정·순서와 함께 푸는 최적화 연구, 승강기를 층간 병목으로 다룬 배송 로봇 연구로 나누어 정리한다.
- 이 페이지는 [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 절은 충전 방식·정책의 처리량·비용 효과를 대기행렬로 분석한 창고 연구, 충전을 작업 배정·순서와 함께 푸는 최적화 연구, 승강기를 층간 병목으로 다룬 배송 로봇 연구로 나누어 정리한다.

- Zou·Gong·de Koster·Xu, Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system(2018) — 플러그인 충전·배터리 교환·유도 충전을 비교해 유도 충전이 회수 처리 시간에서 가장 좋고 배터리 비용이 낮으면 교환이 플러그인보다 싸다고 보고했다. [사실][^ref-098]
- Chen·Gong·Chen·Wang, Does battery management matter?(2024) — 배터리 열화를 반영하면 느린 충전이 빠른 충전보다 나은 조건이 있고, 우선 충전 정책이 전용 충전 정책보다 비용 효율적이라고 보고했으며 충전기 대수 결정 도구를 제시했다. [사실][^ref-861]
- Omega 게재 논문(2024) — 로봇 이동형 풀필먼트 시스템 성능 평가에 에너지 소비를 넣고 동적 우선순위 운영 정책을 다룬다(제목 기준, 결과 수치 미확인). [사실][^ref-146]
- Dang·Singh·Adan·Martagan·van de Sande, Scheduling heterogeneous multi-load AGVs with battery constraints(2021) — 운반·충전 요청 동시 배정·순서화와 부분 충전 시간 결정으로 현행 대비 약 20~50% 비용 절감을 저자가 보고했다. [사실][^ref-862]
- Optimal recharge sequencing in multi-AGV systems(2024, 저자 미확인) — 충전소 사용 중·대기 확률을 반영한 혼합 정수 선형 계획으로 허용 최대치까지 완전 충전이 최적이라고 보고했다. [사실][^ref-858]
- Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers(2026, 프리프린트) — 대기 예상 시간을 반영한 충전소 선택·충전 시간 학습을 제시한다(저자 보고). [사실][^ref-859]
- Ma·Zhou·Stephen(2020) — 컨테이너 터미널에서 분산형 충전소 배치와 점진적 재충전 정책이 좋은 성능을 낸다고 보고했다(항만 사례, 물류센터 적용 미확인). [사실][^ref-860]
- Stark 외, A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse(2024) — 창고 안 충전소 배치를 PageRank 와 비슷한 방법으로 다룬다. [사실][^ref-109]
- Lee 외(2026, 병원) — 고밀도 병원 환경의 약품 배송 로봇 연구로, 승강기 가동률이 높을수록 배송 실패가 많고 배송 시간이 길었다고 보고했다(물류센터 적용 미확인). [사실][^ref-060]
- 다층 호텔 배송 경로 계획 연구(2025, 호텔) — 승강기 운행 시간을 늘리면 총 이동 시간이 늘었다고 보고했다(물류센터 적용 미확인). [사실][^ref-103]
- Electronics(2025) 게재 논문 — 실내 배송 로봇의 다층 경로 계획에서 승강기 선택을 최적화하는 방법을 제시한다(제목 기준). [사실][^ref-321]
- 박재범·조성준·김준식·유범재(2024, 국내) — 서버를 통한 엘리베이터 제어 모듈과 노드 그래프 기반 다층·다중 목적지 경로 계획을 제안하고 실증 시험과 주행 시간 비교로 검증했다고 보고했다(배송 로봇 사례, 물류센터 적용 미확인). [사실][^ref-863]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)
- 관련 영역: [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-060]: Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026, https://doi.org/10.1177/20552076261437181, 접근일 2026-09-25 (원문 미열람)
[^ref-098]: Zou, B., Gong, Y., de Koster, R., & Xu, X., Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system, 2018, https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901, 접근일 2026-09-25 (원문 미열람)
[^ref-103]: PMC 게재 논문(저자 미확인), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-25 (원문 미열람)
[^ref-109]: Stark, H.-G. 외, A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse, 2024-06, https://arxiv.org/abs/2406.17003, 접근일 2026-09-25 (원문 미열람)
[^ref-146]: Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336, 접근일 2026-09-25 (원문 미열람)
[^ref-321]: Electronics(MDPI) 게재 논문(저자 미확인), Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots, 2025, https://doi.org/10.3390/electronics14050982, 접근일 2026-09-25 (원문 미열람)
[^ref-858]: Computers & Industrial Engineering 게재 논문(저자 미확인), Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach, 2024-08, https://www.sciencedirect.com/science/article/pii/S0360835224006314, 접근일 2026-09-25 (원문 미열람)
[^ref-859]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-860]: Ma, N., Zhou, C., & Stephen, A., Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals, 2020, https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X, 접근일 2026-09-25 (원문 미열람)
[^ref-861]: Chen, W., Gong, Y., Chen, Q., & Wang, H., Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse, 2024-01, https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770, 접근일 2026-09-25 (원문 미열람)
[^ref-862]: Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D., Scheduling heterogeneous multi-load AGVs with battery constraints, 2021-12, https://www.sciencedirect.com/science/article/pii/S0305054821002586, 접근일 2026-09-25 (원문 미열람)
[^ref-863]: 박재범, 조성준, 김준식, 유범재(전자공학회논문지 61(8)), 배송 로봇의 다층, 다중 배송을 위한 효율적인 경로 계획 및 엘리베이터 층간 이동 시스템, 2024, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003107904, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-40 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-40 | 16. 공용 자원·충전·에너지 최적화 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-25-40/pages/topics/2026/2026-09-25-area16-s7.md

```markdown
---
title: "16. 공용 자원·충전·에너지 최적화 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "D. 계획·최적화"
primary_area_no: 16
related_areas: [3, 5, 8, 10, 13, 15, 22, 27]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-051, ref-105, ref-216, ref-228, ref-286, ref-312, ref-377, ref-864, ref-866]
last_run: 2026-09-25
version: 1
split_from: docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#7
---

[홈](../../index.md) › [주제](../index.md) › 16. 공용 자원·충전·에너지 최적화 — 관련 표준·프레임워크·오픈소스

# 16. 공용 자원·충전·에너지 최적화 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- VDA 5050 은 충전을 동작과 배터리 선언·상태 필드로 표현하고, Open-RMF 는 충전 설정·작업 계획기·교통 그래프·승강기 메시지로 공용 자원을 다룬다. [사실][^ref-031][^ref-105] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

VDA 5050 은 충전을 동작과 배터리 선언·상태 필드로 표현하고, Open-RMF 는 충전 설정·작업 계획기·교통 그래프·승강기 메시지로 공용 자원을 다룬다. [사실][^ref-031][^ref-105] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| VDA 5050 3.0.0 명세 | 표준 | 충전을 즉시 동작 또는 노드 동작인 startCharging·stopCharging 으로 표현하며, 충전은 정지한 충전 지점이나 주행 중 충전 차선에서 할 수 있고 과충전 보호는 이동로봇의 책임이다. [사실][^ref-031] | [ref-031](../../references/ref-031.md) |
| VDA 5050 3.0.0 관제 기능·구역 유형 | 표준 | 관제 기능으로 에너지 관리를 들며 충전 주문이 운반 주문을 중단시킬 수 있다고 적는다. [사실][^ref-031] 충전소를 별도 구역 유형으로 두지 않고 충전을 주문의 노드 동작과 즉시 동작으로 다룬다. [사실][^ref-031] 충전 순서·시점 결정 방법은 명세에서 확인되지 않는다. [사실][^ref-031] | [ref-031](../../references/ref-031.md) |
| VDA 5050 팩트시트 batteryCharging | 표준 | 임계 저충전 수준, 희망 최소·최대 충전 수준, 최소 충전 시간 네 항목을 로봇 선언으로 둔다. [사실][^ref-228] 이 선언은 충전 시점 계획의 입력이 될 수 있을 것으로 보인다. [추정][^ref-228] | [ref-228](../../references/ref-228.md) |
| VDA 5050 상태 powerSupply | 표준 | 충전 상태·충전 중 여부·전압·전류·건강 상태·주행 가능 거리를 담는다. [사실][^ref-051] | [ref-051](../../references/ref-051.md) |
| Open-RMF fleet_adapter_template | 오픈소스 | 충전 임계값·충전 목표·배터리·전력 소비·작업 종료 동작·로봇별 충전기 설정을 둔다(수치는 예시값). [사실][^ref-105] | [ref-105](../../references/ref-105.md) |
| Open-RMF rmf_task TaskPlanner | 오픈소스 | 충전량 부족 오류 구분과 배터리 우선 비용 설정을 둔다. [사실][^ref-377] | [ref-377](../../references/ref-377.md) |
| Open-RMF rmf_traffic 교통 그래프 | 오픈소스 | 뮤텍스 그룹, 충전 경유점이 정의된다. [사실][^ref-864] | ref-864 |
| Open-RMF rmf_lift_msgs | 오픈소스 | 승강기 요청·상태의 세션 id 와 운영 모드를 정의한다. [사실][^ref-312][^ref-286] | [ref-312](../../references/ref-312.md) |
| Open-RMF rmf_reservation(실험적) | 오픈소스 | 충전기 같은 자원의 시간 범위 예약·배정을 제공한다고 소개되며 배포판 포함 여부는 미확인이다. [사실][^ref-866] | ref-866 |
| Nav2 Docking Framework(연계 대상) | 오픈소스 | 도크 데이터베이스, 충전·비충전 도크 플러그인, 센서 보정, 충전 확인 함수를 둔다. [사실][^ref-216] | [ref-216](../../references/ref-216.md) |

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)
- 관련 영역: [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-216]: ROS Navigation (ros-navigation/navigation2 GitHub), nav2_docking — README (Open Navigation's Nav2 Docking Framework), 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25
[^ref-377]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp, 접근일 2026-09-25
[^ref-864]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-09-25
[^ref-866]: Open Robotics (open-rmf), rmf_reservation — Experimental reservation library in rust (GitHub), 미확인, https://github.com/open-rmf/rmf_reservation, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-40 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-40 | 16. 공용 자원·충전·에너지 최적화 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-25-40/pages/topics/2026/2026-09-25-area16-s11.md

```markdown
---
title: "16. 공용 자원·충전·에너지 최적화 — 열린 질문"
type: topic
category: "D. 계획·최적화"
primary_area_no: 16
related_areas: [3, 5, 8, 10, 13, 15, 22, 27]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-039, ref-079, ref-104, ref-105, ref-228, ref-312]
last_run: 2026-09-25
version: 1
split_from: docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#11
---

[홈](../../index.md) › [주제](../index.md) › 16. 공용 자원·충전·에너지 최적화 — 열린 질문

# 16. 공용 자원·충전·에너지 최적화 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 충전·대기 시간을 성과 지표에서 어떻게 분류할지, 물류센터에서 충전·승강기 병목이 얼마나 되는지, 제조사가 다른 로봇이 충전기·승강기를 어떤 규칙으로 나눠 쓸지가 아직 확인되지 않았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

충전·대기 시간을 성과 지표에서 어떻게 분류할지, 물류센터에서 충전·승강기 병목이 얼마나 되는지, 제조사가 다른 로봇이 충전기·승강기를 어떤 규칙으로 나눠 쓸지가 아직 확인되지 않았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-016** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-14) 창고 이동로봇 플릿에 ISO 22400식 OEE(가용성·성능·품질)를 적용하는 합의된 정의가 있는가, 충전·대기·교통 정체 시간은 어느 손실로 분류해야 하는가? 이번 실행에서도 관련 근거를 찾지 못했다.
- **oq-010** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-10) 국내 다층 물류센터에서 화물용 승강기나 층간 반송 설비가 로봇 처리량의 병목이 된다는 정량 자료가 있는가, 병원·호텔 사례의 승강기 혼잡 결과를 물류센터에 옮길 수 있는가?
- (새 질문 · 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-40) 제조사가 다른 이동로봇이 같은 충전기를 함께 쓸 수 있게 하는 충전 커넥터·충전 통신의 공통 규격이나 공개 사례가 있는가? 관련 근거는 VDA 5050 이 과충전 보호를 로봇 책임으로 둔다는 점이다.[^ref-031]
- (새 질문 · 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-40) 물류센터 로봇의 충전 시점을 시간대별 전기 요금이나 최대 수요 전력 기준으로 계획한 연구나 국내 사례가 있는가? 출발점은 VDA 5050 이 관제 기능으로 드는 에너지 관리다.[^ref-031]
- (새 질문 · 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-40) 여러 제조사 플릿이 한 승강기를 함께 쓸 때 세션 순서·최대 점유 시간·목적층 묶음을 정하는 배분 규칙을 공개한 표준이나 구현이 있는가?[^ref-312]
- (새 질문 · 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-40) 충전 하한을 제조사가 팩트시트로 선언한 값(criticalLowChargingLevel)과 ROP 운영 설정(recharge_threshold) 가운데 어느 것으로 삼고, 둘이 다르면 어떻게 조정하는가?[^ref-228][^ref-105]
- (새 질문 · 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-40) 출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot 과 is_charger 가운데 어느 속성으로 하는가?[^ref-039][^ref-079][^ref-104]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)
- 관련 영역: [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-039]: Open Robotics, Currently supported Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_types.html, 접근일 2026-09-25
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-40 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-40 | 16. 공용 자원·충전·에너지 최적화 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-25-40/pages/topics/2026/2026-09-25-area16-s4.md

```markdown
---
title: "16. 공용 자원·충전·에너지 최적화 — 핵심 개념과 용어"
type: topic
category: "D. 계획·최적화"
primary_area_no: 16
related_areas: [3, 5, 8, 10, 13, 15, 22, 27]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-051, ref-098, ref-105, ref-228, ref-286, ref-312, ref-864]
last_run: 2026-09-25
version: 1
split_from: docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#4
---

[홈](../../index.md) › [주제](../index.md) › 16. 공용 자원·충전·에너지 최적화 — 핵심 개념과 용어

# 16. 공용 자원·충전·에너지 최적화 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 앞 절의 문제를 다루려면 배터리 상태와 공용 자원 점유를 표현하는 용어가 먼저 필요하다.
- 이 페이지는 [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

앞 절의 문제를 다루려면 배터리 상태와 공용 자원 점유를 표현하는 용어가 먼저 필요하다.

- **충전 상태(State of Charge, SOC)** — 배터리에 남은 충전량의 비율이다. VDA 5050 상태 메시지의 powerSupply 는 충전 상태(%), 충전 중 여부, 배터리 전압·전류, 건강 상태, 현재 충전량으로 갈 수 있는 거리(m)를 담고, 좋음·나쁨만 아는 로봇은 80%·20%로 보고한다. [사실][^ref-051]
- **임계 저충전 수준(criticalLowChargingLevel)** — VDA 5050 팩트시트 batteryCharging 의 로봇 선언 항목으로, 이 수준 이하에서는 관제가 충전소로 가는 주문만 보내야 한다. 같은 블록에 희망 최소 충전 수준(minimumDesiredChargingLevel), 희망 최대 충전 수준(maximumDesiredChargingLevel), 최소 충전 시간(minimumChargingTime)이 있다. [사실][^ref-228]
- **충전 임계값과 충전 목표(recharge_threshold·recharge_soc)** — Open-RMF 플릿 어댑터 설정에서 로봇이 운행하지 않는 배터리 하한과 충전 목표다. 템플릿의 0.10·1.0 은 예시값이며 운영 권장값이 아니다. [사실][^ref-105]
- **충전 방식(플러그인 충전·배터리 교환·유도 충전)** — [로봇 이동형 풀필먼트 시스템](../../glossary/robotic-mobile-fulfillment-system.md) 연구가 비교한 세 전략이며, 이 연구는 [반개방형 대기행렬 네트워크](../../glossary/semi-open-queueing-network.md)와 시뮬레이션을 썼다. [사실][^ref-098]
- **뮤텍스 그룹(mutex group)** — Open-RMF 교통 그래프에서 같은 그룹에 속한 경유점이나 차선을 한 번에 한 로봇만 점유하게 하는 단위다. [사실][^ref-864]
- **승강기 세션(lift session)** — Open-RMF 승강기 요청은 요청자별 고유 세션 id 로 승강기를 점유하고, 승강기 상태는 세션 종료 요청(REQUEST_END_SESSION)이 올 때까지 제어권을 받은 세션 id 를 기록한다. [사실][^ref-312][^ref-286] 승강기 요청을 감독하는 구성요소는 [승강기 어댑터](../../glossary/lift-adapter.md)다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)
- 관련 영역: [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-098]: Zou, B., Gong, Y., de Koster, R., & Xu, X., Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system, 2018, https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901, 접근일 2026-09-25 (원문 미열람)
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25
[^ref-864]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-40 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-40 | 16. 공용 자원·충전·에너지 최적화 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-25-40/docs_tree.txt

```text
about/agents.md
about/how-to-contribute.md
about/idea-mapping.md
about/reading-guide.md
about/research-method.md
about/scope-boundary.md
about/what-is-rop.md
categories/a-business-supply-chain-design/01-order-and-business-system-integration.md
categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md
categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md
categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md
categories/a-business-supply-chain-design/index.md
categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md
categories/b-common-information-and-environment-model/06-map-space-and-location-model.md
categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md
categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md
categories/b-common-information-and-environment-model/index.md
categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md
categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md
categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md
categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md
categories/c-connectivity-and-execution-foundation/index.md
categories/d-planning-and-optimization/13-task-allocation-mrta.md
categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md
categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md
categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md
categories/d-planning-and-optimization/index.md
categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md
categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md
categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md
categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md
categories/e-collaboration-and-field-operations/index.md
categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md
categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md
categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md
categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md
categories/f-deployment-verification-and-maintenance/index.md
categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md
categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md
categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md
categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md
categories/g-safety-security-intelligence-and-governance/index.md
changelog.md
corrections.md
flow-matrix.md
glossary/action-dependency-graph.md
glossary/age-of-information.md
glossary/aggregation-event.md
glossary/ariac.md
glossary/asset-administration-shell.md
glossary/association-event.md
glossary/b2mml.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/building-information-modeling.md
glossary/building-topology-ontology.md
glossary/business-location.md
glossary/cap-theorem.md
glossary/capabilities-skills-services.md
glossary/capability-based-task-allocation.md
glossary/capability-matchmaking.md
glossary/cbv.md
glossary/conflict-based-search.md
glossary/conformance-test.md
glossary/consensus-based-bundle-algorithm.md
glossary/cora.md
glossary/crdt.md
glossary/dds-security.md
glossary/deadlock.md
glossary/digital-shadow.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/drawing-exchange-format.md
glossary/eclass.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/fleet-adapter.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/giai.md
glossary/grai.md
glossary/hallucination.md
glossary/hungarian-method.md
glossary/idempotency-key.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/index.md
glossary/indoor-mapping-data-format.md
glossary/indoorgml.md
glossary/intent-recognition.md
glossary/irdi.md
glossary/isa-95.md
glossary/layout-interchange-format.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/location-check-digit.md
glossary/managed-node.md
glossary/map-alignment.md
glossary/mapf.md
glossary/market-based-task-allocation.md
glossary/milp.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/nearest-vehicle-first-rule.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/open-rmf.md
glossary/order-batching.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-symbol-spotting.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/precedence-constraint.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/read-point.md
glossary/release-zone.md
glossary/required-and-provided-capability.md
glossary/roadmap.md
glossary/robotic-mobile-fulfillment-system.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scor.md
glossary/semantic-id.md
glossary/semi-open-queueing-network.md
glossary/shacl.md
glossary/skill.md
glossary/slot-filling.md
glossary/space-graph.md
glossary/sscc.md
glossary/structured-output.md
glossary/task-decomposition.md
glossary/time-window.md
glossary/topological-map.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/wes-wcs-wms-mes-tms.md
glossary/workflow-net.md
ideas/floorplan-recognition.md
ideas/index.md
ideas/nl-task-chatbot.md
ideas/robot-capability-ontology.md
index.md
logs/daily/2026-09-25.md
logs/index.md
metrics.md
open-questions.md
references/index.md
references/ref-001.md
references/ref-002.md
references/ref-003.md
references/ref-004.md
references/ref-005.md
references/ref-006.md
references/ref-007.md
references/ref-008.md
references/ref-009.md
references/ref-010.md
references/ref-011.md
references/ref-012.md
references/ref-013.md
references/ref-014.md
references/ref-015.md
references/ref-016.md
references/ref-017.md
references/ref-018.md
references/ref-019.md
references/ref-020.md
references/ref-021.md
references/ref-022.md
references/ref-023.md
references/ref-024.md
references/ref-025.md
references/ref-026.md
references/ref-027.md
references/ref-028.md
references/ref-029.md
references/ref-030.md
references/ref-031.md
references/ref-032.md
references/ref-033.md
references/ref-034.md
references/ref-035.md
references/ref-036.md
references/ref-037.md
references/ref-038.md
references/ref-039.md
references/ref-040.md
references/ref-041.md
references/ref-042.md
references/ref-043.md
references/ref-044.md
references/ref-045.md
references/ref-046.md
references/ref-047.md
references/ref-048.md
references/ref-049.md
references/ref-050.md
references/ref-051.md
references/ref-052.md
references/ref-053.md
references/ref-054.md
references/ref-055.md
references/ref-056.md
references/ref-057.md
references/ref-058.md
references/ref-059.md
references/ref-060.md
references/ref-061.md
references/ref-062.md
references/ref-063.md
references/ref-064.md
references/ref-065.md
references/ref-066.md
references/ref-067.md
references/ref-068.md
references/ref-069.md
references/ref-070.md
references/ref-071.md
references/ref-072.md
references/ref-073.md
references/ref-074.md
references/ref-075.md
references/ref-076.md
references/ref-077.md
references/ref-078.md
references/ref-079.md
references/ref-080.md
references/ref-081.md
references/ref-082.md
references/ref-083.md
references/ref-084.md
references/ref-085.md
references/ref-086.md
references/ref-087.md
references/ref-088.md
references/ref-089.md
references/ref-090.md
references/ref-091.md
references/ref-092.md
references/ref-093.md
references/ref-094.md
references/ref-095.md
references/ref-096.md
references/ref-097.md
references/ref-098.md
references/ref-099.md
references/ref-100.md
references/ref-101.md
references/ref-102.md
references/ref-103.md
references/ref-104.md
references/ref-105.md
references/ref-106.md
references/ref-107.md
references/ref-108.md
references/ref-109.md
references/ref-110.md
references/ref-111.md
references/ref-112.md
references/ref-113.md
references/ref-114.md
references/ref-115.md
references/ref-116.md
references/ref-117.md
references/ref-118.md
references/ref-119.md
references/ref-120.md
references/ref-121.md
references/ref-122.md
references/ref-123.md
references/ref-124.md
references/ref-125.md
references/ref-126.md
references/ref-127.md
references/ref-128.md
references/ref-129.md
references/ref-130.md
references/ref-131.md
references/ref-132.md
references/ref-133.md
references/ref-134.md
references/ref-135.md
references/ref-136.md
references/ref-137.md
references/ref-138.md
references/ref-139.md
references/ref-140.md
references/ref-141.md
references/ref-142.md
references/ref-143.md
references/ref-144.md
references/ref-145.md
references/ref-146.md
references/ref-147.md
references/ref-148.md
references/ref-149.md
references/ref-150.md
references/ref-151.md
references/ref-152.md
references/ref-153.md
references/ref-154.md
references/ref-155.md
references/ref-156.md
references/ref-157.md
references/ref-158.md
references/ref-159.md
references/ref-160.md
references/ref-161.md
references/ref-162.md
references/ref-163.md
references/ref-164.md
references/ref-165.md
references/ref-166.md
references/ref-167.md
references/ref-168.md
references/ref-169.md
references/ref-170.md
references/ref-171.md
references/ref-172.md
references/ref-173.md
references/ref-174.md
references/ref-175.md
references/ref-176.md
references/ref-177.md
references/ref-178.md
references/ref-179.md
references/ref-180.md
references/ref-181.md
references/ref-182.md
references/ref-183.md
references/ref-184.md
references/ref-185.md
references/ref-186.md
references/ref-187.md
references/ref-188.md
references/ref-189.md
references/ref-190.md
references/ref-191.md
references/ref-192.md
references/ref-193.md
references/ref-194.md
references/ref-195.md
references/ref-196.md
references/ref-197.md
references/ref-199.md
references/ref-212.md
references/ref-213.md
references/ref-214.md
references/ref-215.md
references/ref-216.md
references/ref-217.md
references/ref-218.md
references/ref-219.md
references/ref-220.md
references/ref-221.md
references/ref-222.md
references/ref-223.md
references/ref-224.md
references/ref-225.md
references/ref-226.md
references/ref-227.md
references/ref-228.md
references/ref-229.md
references/ref-230.md
references/ref-231.md
references/ref-232.md
references/ref-233.md
references/ref-234.md
references/ref-235.md
references/ref-236.md
references/ref-237.md
references/ref-238.md
references/ref-239.md
references/ref-240.md
references/ref-241.md
references/ref-242.md
references/ref-243.md
references/ref-244.md
references/ref-245.md
references/ref-246.md
references/ref-247.md
references/ref-248.md
references/ref-249.md
references/ref-250.md
references/ref-251.md
references/ref-252.md
references/ref-253.md
references/ref-254.md
references/ref-255.md
references/ref-256.md
references/ref-257.md
references/ref-258.md
references/ref-259.md
references/ref-260.md
references/ref-261.md
references/ref-262.md
references/ref-263.md
references/ref-264.md
references/ref-265.md
references/ref-266.md
references/ref-267.md
references/ref-268.md
references/ref-269.md
references/ref-270.md
references/ref-271.md
references/ref-272.md
references/ref-273.md
references/ref-274.md
references/ref-275.md
references/ref-276.md
references/ref-277.md
references/ref-278.md
references/ref-279.md
references/ref-280.md
references/ref-281.md
references/ref-282.md
references/ref-283.md
references/ref-284.md
references/ref-285.md
references/ref-286.md
references/ref-287.md
references/ref-288.md
references/ref-289.md
references/ref-290.md
references/ref-291.md
references/ref-292.md
references/ref-293.md
references/ref-294.md
references/ref-295.md
references/ref-296.md
references/ref-297.md
references/ref-298.md
references/ref-299.md
references/ref-300.md
references/ref-301.md
references/ref-302.md
references/ref-303.md
references/ref-304.md
references/ref-305.md
references/ref-306.md
references/ref-307.md
references/ref-308.md
references/ref-309.md
references/ref-310.md
references/ref-311.md
references/ref-312.md
references/ref-313.md
references/ref-314.md
references/ref-315.md
references/ref-316.md
references/ref-317.md
references/ref-318.md
references/ref-319.md
references/ref-320.md
references/ref-321.md
references/ref-322.md
references/ref-323.md
references/ref-324.md
references/ref-325.md
references/ref-326.md
references/ref-327.md
references/ref-328.md
references/ref-329.md
references/ref-330.md
references/ref-331.md
references/ref-332.md
references/ref-333.md
references/ref-334.md
references/ref-335.md
references/ref-336.md
references/ref-337.md
references/ref-338.md
references/ref-339.md
references/ref-340.md
references/ref-341.md
references/ref-342.md
references/ref-343.md
references/ref-344.md
references/ref-345.md
references/ref-346.md
references/ref-347.md
references/ref-348.md
references/ref-349.md
references/ref-350.md
references/ref-351.md
references/ref-352.md
references/ref-353.md
references/ref-354.md
references/ref-355.md
references/ref-356.md
references/ref-357.md
references/ref-358.md
references/ref-359.md
references/ref-360.md
references/ref-361.md
references/ref-362.md
references/ref-363.md
references/ref-364.md
references/ref-365.md
references/ref-366.md
references/ref-367.md
references/ref-368.md
references/ref-369.md
references/ref-370.md
references/ref-371.md
references/ref-372.md
references/ref-373.md
references/ref-374.md
references/ref-375.md
references/ref-376.md
references/ref-377.md
references/ref-378.md
references/ref-379.md
references/ref-380.md
references/ref-381.md
references/ref-382.md
references/ref-383.md
references/ref-384.md
references/ref-385.md
references/ref-386.md
references/ref-387.md
references/ref-388.md
references/ref-389.md
references/ref-390.md
references/ref-391.md
references/ref-392.md
references/ref-393.md
references/ref-394.md
references/ref-395.md
references/ref-396.md
references/ref-397.md
references/ref-398.md
references/ref-399.md
references/ref-400.md
references/ref-401.md
references/ref-402.md
references/ref-403.md
references/ref-404.md
references/ref-405.md
references/ref-406.md
references/ref-407.md
references/ref-408.md
references/ref-409.md
references/ref-410.md
references/ref-411.md
references/ref-412.md
references/ref-413.md
references/ref-414.md
references/ref-415.md
references/ref-416.md
references/ref-417.md
references/ref-418.md
references/ref-419.md
references/ref-420.md
references/ref-421.md
references/ref-422.md
references/ref-423.md
references/ref-424.md
references/ref-425.md
references/ref-426.md
references/ref-427.md
references/ref-428.md
references/ref-429.md
references/ref-430.md
references/ref-431.md
references/ref-432.md
references/ref-433.md
references/ref-434.md
references/ref-435.md
references/ref-436.md
standards/index.md
topics/2026/2026-09-25-area01-s11.md
topics/2026/2026-09-25-area01-s3.md
topics/2026/2026-09-25-area01-s4.md
topics/2026/2026-09-25-area01-s6.md
topics/2026/2026-09-25-area01-s7.md
topics/2026/2026-09-25-area01-s8.md
topics/2026/2026-09-25-area02-s10.md
topics/2026/2026-09-25-area02-s11.md
topics/2026/2026-09-25-area02-s4.md
topics/2026/2026-09-25-area02-s6.md
topics/2026/2026-09-25-area02-s7.md
topics/2026/2026-09-25-area02-s8.md
topics/2026/2026-09-25-area03-s11.md
topics/2026/2026-09-25-area03-s6.md
topics/2026/2026-09-25-area03-s7.md
topics/2026/2026-09-25-area03-s8.md
topics/2026/2026-09-25-area04-s11.md
topics/2026/2026-09-25-area04-s4.md
topics/2026/2026-09-25-area04-s6.md
topics/2026/2026-09-25-area04-s7.md
topics/2026/2026-09-25-area04-s8.md
topics/2026/2026-09-25-area05-s4.md
topics/2026/2026-09-25-area05-s6.md
topics/2026/2026-09-25-area05-s7.md
topics/2026/2026-09-25-area05-s8.md
topics/2026/2026-09-25-area06-s10.md
topics/2026/2026-09-25-area06-s3.md
topics/2026/2026-09-25-area06-s4.md
topics/2026/2026-09-25-area06-s6.md
topics/2026/2026-09-25-area06-s7.md
topics/2026/2026-09-25-area06-s8.md
topics/2026/2026-09-25-area07-s6.md
topics/2026/2026-09-25-area07-s7.md
topics/2026/2026-09-25-area08-s10.md
topics/2026/2026-09-25-area08-s11.md
topics/2026/2026-09-25-area08-s3.md
topics/2026/2026-09-25-area08-s4.md
topics/2026/2026-09-25-area08-s6.md
topics/2026/2026-09-25-area08-s7.md
topics/2026/2026-09-25-area08-s8.md
topics/2026/2026-09-25-area09-s10.md
topics/2026/2026-09-25-area09-s11.md
topics/2026/2026-09-25-area09-s4.md
topics/2026/2026-09-25-area09-s6.md
topics/2026/2026-09-25-area09-s7.md
topics/2026/2026-09-25-area09-s8.md
topics/2026/2026-09-25-area10-s10.md
topics/2026/2026-09-25-area10-s11.md
topics/2026/2026-09-25-area10-s4.md
topics/2026/2026-09-25-area10-s7.md
topics/2026/2026-09-25-area10-s8.md
topics/2026/2026-09-25-area11-s10.md
topics/2026/2026-09-25-area11-s4.md
topics/2026/2026-09-25-area11-s6.md
topics/2026/2026-09-25-area11-s7.md
topics/2026/2026-09-25-area11-s8.md
topics/2026/2026-09-25-area12-s11.md
topics/2026/2026-09-25-area12-s4.md
topics/2026/2026-09-25-area12-s6.md
topics/2026/2026-09-25-area12-s7.md
topics/2026/2026-09-25-area12-s8.md
topics/2026/2026-09-25-area13-s11.md
topics/2026/2026-09-25-area13-s4.md
topics/2026/2026-09-25-area13-s6.md
topics/2026/2026-09-25-area13-s7.md
topics/2026/2026-09-25-area13-s8.md
topics/2026/2026-09-25-area14-s11.md
topics/2026/2026-09-25-area14-s4.md
topics/2026/2026-09-25-area14-s6.md
topics/2026/2026-09-25-area14-s8.md
topics/2026/2026-09-25-area15-s3.md
topics/2026/2026-09-25-area15-s4.md
topics/2026/2026-09-25-area15-s6.md
topics/2026/2026-09-25-area15-s7.md
topics/2026/2026-09-25-area15-s8.md
topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md
topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md
topics/index.md
tracks/floorplan-recognition/experiments.md
tracks/floorplan-recognition/index.md
tracks/floorplan-recognition/log.md
tracks/floorplan-recognition/question-backlog.md
tracks/floorplan-recognition/space-graph-schema-draft.md
tracks/floorplan-recognition/stage-1-prior-work-and-products.md
tracks/floorplan-recognition/stage-2-data-and-standards.md
tracks/floorplan-recognition/stage-3-implementation-hypothesis.md
tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md
tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md
tracks/manual-capability-ontology/document-type-matrix.md
tracks/manual-capability-ontology/evaluation-and-verification.md
tracks/manual-capability-ontology/experiments.md
tracks/manual-capability-ontology/index.md
tracks/manual-capability-ontology/log.md
tracks/manual-capability-ontology/model-standard-comparison.md
tracks/manual-capability-ontology/ontology-draft.md
tracks/manual-capability-ontology/question-backlog.md
tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md
tracks/manual-capability-ontology/stage-2-document-types.md
tracks/manual-capability-ontology/stage-3-extraction-methods.md
tracks/manual-capability-ontology/stage-4-execution-grounding.md
tracks/manual-capability-ontology/stage-5-completeness-verification.md
tracks/manual-capability-ontology/stage-6-lifecycle-governance.md
tracks/manual-capability-ontology/stage-7-rop-scenarios-and-hypotheses.md
tracks/nl-task-chatbot/experiments.md
tracks/nl-task-chatbot/index.md
tracks/nl-task-chatbot/log.md
tracks/nl-task-chatbot/question-backlog.md
tracks/nl-task-chatbot/stage-1-prior-work-and-products.md
tracks/nl-task-chatbot/stage-2-data-and-standards.md
tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md
tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md
tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md
tracks/nl-task-chatbot/task-model-draft.md
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 426건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 107개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
- business-location: 업무 위치 (Business Location (EPCIS bizLocation))
- cap-theorem: CAP 정리 (CAP Theorem)
- capabilities-skills-services: 능력·스킬·서비스 모델 (Capabilities, Skills and Services (CSS) Model)
- capability-based-task-allocation: 능력 기반 작업 배정 (Capability-based Task Allocation)
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformance-test: 적합성 시험 (Conformance Test)
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- eclass: ECLASS (ECLASS)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- hallucination: 환각 (Hallucination)
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoorgml: IndoorGML (IndoorGML)
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- order-batching: 주문 배치 (Order Batching)
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- roadmap: 경로망 (Roadmap)
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- structured-output: 구조화 출력 (Structured Output)
- task-decomposition: 작업 분해 (Task Decomposition)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
```

### docs/open-questions.md (요약: 대상 영역 [16] 에 걸린 2건 / 전체 60건)

```markdown
- oq-016 [열림] 창고 이동로봇 플릿에 ISO 22400식 OEE(가용성·성능·품질)를 적용하는 합의된 정의가 있는가, 충전·대기·교통 정체 시간은 어느 손실로 분류해야 하는가? (영역 4, 16)
- oq-060 [열림] 출처 충돌: IDTA 02047 1.0 에 충전 관련 요소(ChargingTimeAsSpecified, ChargingDeviceRequirements, BatteryInformation)가 있는가? 명세 PDF 검색 요약은 있다고 전하지만, 공식 저장소 템플릿 JSON 의 잘린 열람 응답에서는 확인되지 않았다. (영역 5, 16)
```

### _source/ROP_SCM_연구분야_분류.md

```markdown
# SCM 관점의 로봇 오케스트레이션 플랫폼 연구분야

> 문서화: 2026-09-24  
> 범위: 7개 대분류·28개 세부 연구영역, ROP의 책임 경계, 기존 아이디어의 위치, SCM 기반 분석 방법  
> 이 문서는 앞선 대화의 분류 내용을 Markdown으로 정리한 자료다. 공식 단일 분류가 아니라 공급망 프레임워크·로봇 연구·실제 플랫폼 구조를 종합한 연구 범위 점검용 분류이며, 모든 항목을 직접 개발한다는 의미는 아니다.

## 1. 전체 관점

SCM 관점에서 ROP는 **주문·물류·생산 계획을 로봇과 현장 설비의 실제 행동으로 연결하고, 결과를 다시 업무 시스템에 반영하는 실행 플랫폼**으로 볼 수 있다.

연구 범위는 다음과 같이 구분한다.

| 대분류 | 핵심 질문 | 세부영역 |
|---|---|---|
| A. 업무·공급망 설계 | 무슨 일을 왜, 얼마나 해야 하는가? | 1–4 |
| B. 공통 정보·환경 모델 | 로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? | 5–8 |
| C. 연결·실행 기반 | 계획한 작업을 실제 장비가 확실하게 수행하게 하려면? | 9–12 |
| D. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? | 13–16 |
| E. 협업·현장 운영 | 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? | 17–20 |
| F. 도입·검증·유지관리 | 새 현장에 설치하고, 변경하면서, 오래 운영하려면? | 21–24 |
| G. 안전·보안·지능·거버넌스 | 전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? | 25–28 |

ASCM의 SCOR는 계획·주문·조달·생산/가공·이행·반품과 이를 아우르는 Orchestrate를 다룬다. **ROP는 이 중 물리적인 작업이 발생하는 부분을 연결하는 역할**로 접근할 수 있다. SCOR의 공급망 오케스트레이션과 로봇 오케스트레이션은 범위가 다르다. [1]

## 2. A — 업무·공급망 설계

**무슨 일을 왜, 얼마나 해야 하는가**를 연구한다. 로봇을 움직이기 전에 공급망의 요구를 실행 가능한 업무로 정의하는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **1. 주문·업무 시스템 연계** | ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 | 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? |
| **2. 공정·워크플로 모델링** | 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 | ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? |
| **3. 처리능력·거점·설비 계획** | 물동량에 필요한 로봇 수와 종류, 작업대·충전기 배치, 교대 운영, 여러 거점의 자원 배치를 결정 | 로봇을 늘려야 할까, 포장대나 엘리베이터가 병목일까? |
| **4. 성과·경제성·프로세스 개선** | 납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 | 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? |

핵심은 **로봇 개별 성능과 공급망 전체 성과를 구분하는 것**이다. 로봇이 물건을 더 빨리 가져와도 다음 공정이 막히면 대기 재고만 늘어날 수 있다.

기업 업무와 현장 운영·제어의 경계를 정리할 때는 ISA-95의 기업–제어 시스템 통합 관점이 참고가 된다. 실제 제품별로 WES·WCS·FMS·ROP의 책임은 겹칠 수 있다. [2]

## 3. B — 공통 정보·환경 모델

**로봇, 물건, 공간, 상태를 어떻게 같은 의미로 이해할 것인가**를 연구한다. 매뉴얼 온톨로지와 건축 도면 기반 지도가 주로 이 영역에 들어간다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **5. 로봇 능력·작업 온톨로지** | 제조사별 기능·제약·장착 장비·실행 조건을 공통 모델로 표현하고, 작업 요구와 연결 | 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? |
| **6. 지도·공간·위치 모델** | BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 | 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? |
| **7. 화물·재고·자산 식별과 추적** | 제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 | 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? |
| **8. 실시간 세계 상태·데이터 일관성** | 로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 | 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? |

**7번은 SCM 관점에서 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 화물의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3]

6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다.

## 4. C — 연결·실행 기반

**계획한 작업을 실제 장비가 확실하게 수행하게 하는 방법**을 연구한다. 공통 모델을 실제 명령·통신·실행으로 연결하는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **9. 로봇·제조사 관제 연동** | 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 | 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? |
| **10. 설비·건물 시스템 연동** | 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 | 컨베이어 준비와 로봇 도착을 어떻게 맞출까? |
| **11. 분산 시스템·통신·컴퓨팅 구조** | 클라우드·현장 서버·로봇의 역할 분담, 네트워크 지연, 서비스 가용성, 데이터 전송 품질, 다거점 운영 | 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? |
| **12. 명령·작업 실행의 신뢰성** | 접수·실행·완료·취소 상태, 제어권, 중복 요청 방지, 시간 초과, 재시작 후 상태 복원 | 응답이 끊긴 운반 요청을 다시 보내면 같은 화물을 두 번 처리하지 않을까? |

Open-RMF도 제조사별 Fleet Adapter와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결한다. **로봇 연결과 시설 연결을 함께 보는 것**이 필요하다. [4]

## 5. D — 계획·최적화

**누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가**를 연구한다. 논문에서 작업 배정이나 경로 계획으로 많이 등장하는 영역이다. 네 항목은 분리해서 연구할 수 있지만 실제 운영에서는 서로 영향을 준다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **13. 작업 배정 — MRTA** | 능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 | 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? |
| **14. 작업 순서·스케줄링** | 주문 묶음, 작업 선후관계, 시간 제약, 공정 간 동기화, 긴급 작업 삽입 | 피킹·운반·포장이 서로 기다리지 않게 어떤 순서로 실행할까? |
| **15. 다중 로봇 경로·교통 관리 — MAPF** | 여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 | 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? |
| **16. 공용 자원·충전·에너지 최적화** | 충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 | 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? |

SCM에서는 **작업이 계속 새로 들어오는 조건**이 중요하다. 정해진 목적지까지 한 번 이동하는 문제와 지속적으로 주문이 들어오는 운영은 다르다. 이를 다루는 연구가 *Lifelong MAPF*, *Multi-Agent Pickup and Delivery*이다. [5][6]

## 6. E — 협업·현장 운영

**계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가**를 연구한다. 정상적인 시연과 실제 운영의 차이가 많이 드러나는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **17. 로봇 간 협업·물리적 인계** | 이동로봇–로봇팔 협업, 공동 운반, 작업 동기화, 인계 확인, 필요한 정보·인식 결과 공유 | AMR이 물건을 가져온 뒤 로봇팔이 안전하게 인수했음을 어떻게 확인할까? |
| **18. 사람–로봇 협업·운영 인터페이스** | 작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 | 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? |
| **19. 모니터링·이상 탐지·원인 분석** | 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 | 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? |
| **20. 예외 복구·재계획·업무 연속성** | 고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 | 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? |

17번의 협업은 이동로봇끼리 길을 양보하는 문제보다 넓다. **이동·조작·검사·사람 작업을 하나의 공정으로 묶는 문제**까지 포함한다. NIST도 이종 로봇과 사람의 협업 성능을 별도 연구·평가 대상으로 다룬다. [7]

## 7. F — 도입·검증·유지관리

**새 현장에 설치하고, 변경하면서, 오래 운영하는 방법**을 연구한다. 플랫폼 사업에서는 알고리즘 성능 못지않게 중요한 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **21. 온보딩·설정·현장 시운전** | 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 | 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? |
| **22. 시뮬레이션·예측용 디지털 트윈** | 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 | 성수기 주문량이 늘면 어디가 먼저 막힐까? |
| **23. 시험·형식 검증·벤치마크** | 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 | 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? |
| **24. 자산·소프트웨어 수명주기 관리** | 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 | 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? |

8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다.

NIST의 ARIAC처럼 변화하는 제조 환경에서 로봇의 계획·인식·행동과 적응성을 평가하는 시험 환경도 참고할 수 있다. [8]

## 8. G — 안전·보안·지능·거버넌스

위 여섯 영역 전체에 적용되는 연구다. 마지막에 추가하는 부가기능으로 보면 누락되기 쉽다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **25. 안전·위험 관리** | 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 | 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? |
| **26. 사이버보안·접근권한·개인정보** | 장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 | 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? |
| **27. AI·학습·적응과 모델 운영** | 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 | AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? |
| **28. 표준·상호운용성·다사업자 거버넌스** | 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 | 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? |

ROS 2도 인증·암호화·접근권한과 보안 위협 모델을 별도로 다룬다. 기능 연동과 보안 연동은 함께 설계해야 하는 영역이다. [9][10]

27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다.

## 9. ROP가 직접 소유할 범위와 외부 연계 경계

전체를 연구하되 **ROP가 직접 소유할 범위는 별도로 정해야 한다.** 그렇지 않으면 SCM 시스템부터 로봇의 모터 제어까지 모두 만드는 프로젝트가 된다.

| 경계 | ROP에서 다룰 내용 | 주로 연계할 외부 영역 |
|---|---|---|
| **상위 업무 시스템** | 주문·납기·재고 제약을 받아 실행하고 결과 반영 | 수요예측, 구매, 재무, 전사 재고정책 |
| **로봇 자체 지능·제어** | 가능한 기능과 실행 조건, 상태·실패·완료 확인 | 센서 인식, SLAM, 로컬 회피, 파지, 모터·관절 제어 |
| **시설·설비 제어** | 작업 요청·예약·인계·상태 확인 | 승강기·컨베이어·PLC·설비 안전 제어 |
| **거점 간 운송** | 입출고 시간과 인계, 현장 작업 동기화 | 배차·운송계획·운임·국제물류 |
| **업종별 조건** | 해당 조건을 작업·경로·권한 제약으로 반영 | 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항 |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.**

## 10. 논의한 아이디어의 연구영역 매핑

| 아이디어 | 중심 연구영역 | 함께 필요한 영역 |
|---|---|---|
| 매뉴얼 기반 로봇 온톨로지 | **5. 능력·작업 온톨로지** | 9. 어댑터, 21. 온보딩, 23. 검증, 24. 버전 관리 |
| 건축 도면 기반 이동 지도 | **6. 지도·공간 모델** | 15. 교통 관리, 21. 시운전, 22. 시뮬레이션 |
| 로봇과 건물 조건을 함께 판단 | **5+6+8. 능력·공간·현재 상태** | 13. 배정, 16. 자원, 25. 안전 |
| SCM 전체와 연결한 ROP | **1+2+4. 업무 연계·공정·성과** | C~G의 필요한 기능을 조합 |

## 11. SCM 관점의 연구 시작 방법

**기술 목록에 실제 물류 흐름을 교차해서 본다.**

첫 분석 대상으로 한 현장의 **입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품**을 잡고, 각 단계마다 다음 여섯 항목을 채운다.

1. **시작 조건:** 어떤 주문·재고·설비 이벤트가 작업을 발생시키는가?
2. **작업 대상:** 어떤 화물·운반구를 다루는가?
3. **수행 자원:** 로봇·사람·설비 중 누가 어떤 부분을 맡는가?
4. **제약:** 납기·공간·적재량·설비·권한 제약은 무엇인가?
5. **완료·인계:** 무엇이 확인돼야 업무 완료와 재고 변경을 인정하는가?
6. **예외·성과:** 실패하면 누가 복구하며, 처리량·시간·비용에 어떤 영향을 주는가?

예를 들어 **‘피킹한 박스를 포장대로 운반’**이라는 작업 하나에서도 로봇 배정, 경로, 포장대 수용능력, 화물 식별, 인계 확인, 고장 복구가 연결된다. 이 흐름을 먼저 정하면, 온톨로지와 지도 자동화가 **전체 공급망의 어느 비용과 병목을 줄이는 기술인지** 구체적으로 판단할 수 있다.

## 12. 참고 자료

아래는 앞선 답변에서 확인·인용한 공식 자료와 연구 논문이다. 분류표 전체를 단일 출처에서 가져온 것은 아니며, 세부 분류와 연구 질문은 이를 바탕으로 구성한 분석이다.

1. ASCM. [SCOR Digital Standard](https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/). 공급망 프로세스 범위 참고.
2. ISA. [Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems](https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of), 2025. 기업 업무와 제조 운영·제어의 통합 경계 참고.
3. GS1. [EPCIS and CBV Linked Data Model](https://ref.gs1.org/epcis/). 제품·자산의 상태·위치·이동·인계 이벤트 모델 참고.
4. Open Robotics. [RMF Core Overview — Programming Multiple Robots with ROS 2](https://osrf.github.io/ros2multirobotbook/rmf-core.html). 작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.
5. Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. [Lifelong Multi-Agent Path Finding in Large-Scale Warehouses](https://arxiv.org/abs/2005.07371), 2020. 지속적으로 목표가 들어오는 다중 로봇 경로 계획 연구.
6. Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. [Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks](https://arxiv.org/abs/1705.10868), 2017. 온라인 픽업·배송 작업의 배정과 충돌 없는 이동 연구.
7. NIST. [Performance of Collaborative Robot Systems](https://www.nist.gov/programs-projects/performance-collaborative-robot-systems). 사람–로봇 및 이종 로봇 협업 성능 평가 참고.
8. NIST. [ARIAC Documentation](https://pages.nist.gov/ARIAC_docs/en/latest/). 변화하는 제조 환경에서의 로봇 작업 수행·적응성 평가 참고.
9. ROS 2 Design. [ROS 2 DDS-Security Integration](https://design.ros2.org/articles/ros2_dds_security.html). 인증·암호화·접근통제 구조 참고.
10. ROS 2 Design. [ROS 2 Robotic Systems Threat Model](https://design.ros2.org/articles/ros2_threat_model.html). 로봇 시스템의 보안 위협과 대응 설계 참고.
```

### runs/2026-09-25-40/verification2.json

```json
{
  "run_id": "2026-09-25-40",
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
    "overlaps": [
      "ref-060·ref-103·ref-105·ref-312 는 기존 각주 id 를 그대로 재사용했다(1차 지시 이행).",
      "Open-RMF 문서의 충전소 지정 속성 충돌(ref-039 is_parking_spot, ref-079·ref-104 is_charger)은 6절에서 둘 다 제시했고 11절에 출처 충돌 질문으로 올렸다."
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
    "8절(자동 분리 주제 페이지 2026-09-25-area16-s8 의 출처 절 포함): ref-863 각주 정의의 제목을 브리프·reference_updates 와 같은 원 제목 '배송 로봇의 다층, 다중 배송을 위한 효율적인 경로 계획 및 엘리베이터 층간 이동 시스템'으로 되돌린다. 이유: 제목의 쉼표(,)가 가운뎃점(·)으로 바뀌어 출처 제목이 원문과 달라졌다.",
    "6절 첫 문장(분리 주제 페이지 s6 의 세 줄 요약·본문 첫 문장 포함): '공용 자원 문제에 대한 오픈소스의 대표 접근은 …'을 'Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다'처럼 출처가 말한 범위로 좁힌다. 예약을 넣으려면 ref-866 각주와 '실험적' 표시를 함께 단다. 이유: '대표 접근'은 순위 표현인데 교차 확인이 없다. 또 '예약'은 인용한 ref-104·ref-864·ref-312 가 뒷받침하지 않는다.",
    "5절 마지막 문장 '실제 물류센터에서 충전 대기와 승강기 대기가 처리량을 얼마나 줄이는지는 이번 조사에서 확인되지 않았다. [사실][^ref-060][^ref-103]'에서 태그와 두 각주를 뺀다. 이 문장은 조사 한계로만 적고 열린 질문 oq-010 에 연결한다. 이유: ref-060·ref-103 은 병원·호텔 연구이며 이 문장을 뒷받침하지 않는다. 이 문장은 브리프 self_check 의 한계 항목이다.",
    "4절 첫 문장 '앞 절의 문제를 다루려면 … 용어가 먼저 필요하다. [사실][^ref-051][^ref-864]'(분리 주제 페이지 s4 의 세 줄 요약·본문 첫 문장 포함)에서 태그와 각주를 뺀다. 이 문장은 연결 문장으로 둔다. 8절 첫 문장 '대표 연구는 … 나뉜다. [사실][^ref-098][^ref-862][^ref-103]'(s8 포함)은 이 위키의 정리이므로 [의견]으로 바꾸거나 태그를 뺀 연결 문장으로 둔다. 이유: 출처가 이 문장들을 진술하지 않는데 [사실]과 각주가 붙어 있다.",
    "8절 병원·호텔 항목의 '승강기 가동률과 운행 시간이 배송 실패·총 이동 시간을 늘린다고 보고했다'를 f23·f24 문구대로 고친다. 병원 연구는 '승강기 가동률이 높을수록 배송 실패가 많고 배송 시간이 길었다'로, 호텔 연구는 '승강기 운행 시간을 늘리면 총 이동 시간이 늘었다'로 쓴다. 이유: f23 은 연관 관계를 보고했는데 본문이 인과 관계로 일반화했다.",
    "7절 표의 'VDA 5050 팩트시트 batteryCharging' 행에서 '충전 시점 계획의 입력이 될 수 있다'를 [사실] 문장에서 떼어 [추정]으로 따로 적거나 삭제한다. 이유: f3 은 네 필드와 criticalLowChargingLevel 의 의미만 확인했다. 계획 입력이라는 해석은 이 위키의 추론이다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인 / 2차 수정 후 재검증. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. VDA 5050·Open-RMF·Nav2 출처는 GitHub 공식 저장소 원문으로 확인했고, 논문 출처는 검색 결과 요약으로만 대조했다. 확인 33건, 미확인 0건, 교차 확인 0건. 강등: 없음. 원문 미열람 출처: ref-219, ref-098, ref-109, ref-146, ref-060, ref-103, ref-321, ref-858, ref-859, ref-860, ref-861, ref-862, ref-863, ref-866. 주의: 표준·오픈소스 내용은 발행 주체마다 단일 자료다. 연구 결과는 논문마다 단일 출처의 저자 보고다. 충전·승강기 병목 근거는 병원·호텔·항만·배송 로봇 사례이며, 물류센터에도 적용되는지는 확인되지 않았다(oq-010). 충전소 지정 속성을 두고 Open-RMF 문서끼리 서로 다르게 적는다(ref-039 is_parking_spot, ref-079·ref-104 is_charger). 트랙 반영 제안 4건은 반영을 승인했다. oq-016 은 해결하지 않았다. 정정 요청 없음. / 2차 수정 후 재검증. 1차 수정 지시 13건은 모두 이행됐다. 드리프트·태그 문제는 6건이다: ref-863 제목 변형, 6절 '대표 접근' 일반화와 근거 없는 '예약' 포함, 5절 조사 한계 문장의 [사실]·각주 오귀속, 4·8절 정리 문장의 [사실] 태그, 8절 승강기 연구의 인과 일반화, 7절 batteryCharging 행의 추론을 [사실]로 쓴 것. [분류원문] 보존, 섹션 순서 준수, 링크 유효(형식 검증 코드 통과). 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈의 구분, 27. AI·학습·적응과 모델 운영과의 양쪽 연결, 범위 경계는 지켜졌다. 흐름 매트릭스 12칸은 피킹→출하 단일 시나리오 표 하나에 기대고 있어 두 단계가 같은 표를 공유한다.",
  "retry_reason": null
}
```
