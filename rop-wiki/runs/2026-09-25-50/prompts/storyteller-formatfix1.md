(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-50
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 20. 예외 복구·재계획·업무 연속성 (E. 협업·현장 운영)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: false · fetch_mode: mirror_only (일반 웹 페이지 열람은 네트워크 정책으로 막혀 있다. raw.githubusercontent.com 은 열린다: 공식 문서가 GitHub 에 있는 출처는 입력의 config/source_mirrors.yaml 경로를 WebFetch 로 열어 원문을 읽고 sources[].fetched=true, fetched_via=github_raw, fetch_url 을 적는다. 입력에 원문 텍스트(data/source_texts)가 있는 출처는 fetched_via=inbox. 그 밖의 출처는 fetched=false 이며 코드가 신뢰도 상한(medium)을 강제한다 — 공통 규칙 0절 6항)
- 언어: ko

## 입력

### runs/2026-09-25-50/target.json

```json
{
  "run_id": "2026-09-25-50",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 50,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 20,
    "area_name": "20. 예외 복구·재계획·업무 연속성",
    "category": "E. 협업·현장 운영",
    "category_letter": "E"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=20"
}
```

### runs/2026-09-25-50/research.json

```json
{
  "run_id": "2026-09-25-50",
  "date": "2026-09-25",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 20,
    "area_name": "20. 예외 복구·재계획·업무 연속성",
    "category": "E. 협업·현장 운영"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음",
    "섹션 5. 현장 시나리오 비어 있음 — 운반 중 고장 난 로봇의 화물·남은 주문 처리 시나리오 필요",
    "섹션 6. 대표 접근법과 기술 비어 있음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 기존 oq-003, oq-021, oq-038, oq-048 이 이 영역과 관련"
  ],
  "research_questions": [
    "운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? [분류원문]",
    "로봇–관제 인터페이스 표준(VDA 5050)과 오픈소스 관제(Open-RMF)는 고장·통신 단절·작업 취소·일시정지·재계획을 어떤 메시지·기능으로 다루는가? (섹션 6·7 겨냥)",
    "지연·고장이 생겼을 때 다중 로봇 경로와 작업 배정을 실시간으로 재계획하는 연구는 무엇이 있는가? (섹션 6·8 겨냥)",
    "업무 연속성 관리 표준과 국내 제도는 무엇이며 로봇 현장의 제한 운영·수동 전환 계획과 어떻게 연결되는가? (섹션 3·7 겨냥, 한국 자료 우선)",
    "이미 수행한 물리 작업을 취소·되돌릴 때 이벤트 기록과 재고를 어떻게 바로잡는가? (oq-021, oq-003 관련, 섹션 4·6 겨냥)",
    "통신 단절이나 관제 어댑터 재시작 동안 작업을 어디까지 계속하고 재연결 뒤 어떻게 맞추는가? (oq-038, oq-048 관련, 섹션 6·11 겨냥)",
    "예외 복구에서 ROP 직접 범위와 연계 대상(로봇 자체 복구·안전 제어, 상위 WMS)의 경계는 어디인가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 3.0.0 명세에서 이동로봇은 즉시 동작 cancelOrder 를 받으면 가능한 한 빨리 정지하고, 예정된 동작은 FAILED 로 보고하며, 정지 뒤 cancelOrder 상태를 FINISHED 로 보고하고 유휴 상태가 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"After receiving the instantAction cancelOrder, the mobile robot shall attempt to stop as soon as possible.\" 명세는 취소 시 적재물 처리는 따로 정하지 않는다(VDA5050_EN.md main, 3.0.0).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f2",
      "claim": "VDA 5050 3.0.0 은 MQTT 라스트 윌 메시지로 관제가 로봇의 연결 끊김을 감지하게 하고(connectionState ONLINE·OFFLINE·CONNECTION_BROKEN), 브로커와 연결이 끊긴 로봇은 주문 정보를 유지한 채 마지막으로 해제된(released) 노드까지 주문을 수행한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "연결 시 last will 토픽·메시지를 설정해 끊김 시 브로커가 게시하고, 끊긴 로봇은 주문을 last released node 까지 수행한다고 적는다(VDA5050_EN.md main, 3.0.0).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f3",
      "claim": "VDA 5050 최신판 state 스키마는 오류 수준(errorLevel)을 WARNING·URGENT·CRITICAL·FATAL 로, 동작 상태(actionStatus)에 RETRIABLE 을 두며, 명세는 RETRIABLE 상태의 로봇이 관제나 운영자의 개입을 기다린다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-051",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "state.schema 의 errorLevel 열거값 4개와 actionStatus 의 RETRIABLE. 명세: 실패한 집기 등 RETRIABLE 상태에서 로봇은 fleet control 또는 operator 의 개입을 기다린다.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f4",
      "claim": "VDA 5050 state 스키마의 loads 배열은 로봇에 실린 적재물의 식별번호(loadId), 종류, 적재 위치(loadPosition), 치수, 무게를 보고하게 하므로 고장 로봇에 어떤 화물이 실려 있는지 관제가 알 수 있는 근거가 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "loads: loadId \"Unique identification number of the load\", loadType, loadPosition, loadDimensions, weight(kg).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f5",
      "claim": "VDA 5050 의 startPause 즉시 동작은 자동 주행을 멈추고 일시정지 가능한 동작(pauseAllowed=true)만 멈추며, stopPause 로 주문 실행을 재개한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "startPause: 자동 주행 중지, pauseAllowed 동작만 일시정지하고 다른 동작은 계속, stopPause 뒤 재개. state 의 paused 값으로 확인.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f6",
      "claim": "VDA 5050 은 교착(deadlock) 탐지·해소와 통신 오류 탐지·해소를 관제(fleet control)의 역할로 두고, 구역 충돌 같은 상황에서 사용자 개입이 필요한지, 현재 주문을 취소하고 새 주문을 보낼지를 관제가 결정한다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "관제 역할 목록에 blockages(deadlocks)와 communication errors 의 탐지·해소가 있고, 관제가 user interaction 필요 여부 또는 cancel 후 new order 를 결정한다.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f7",
      "claim": "Open-RMF 플릿 어댑터의 RobotUpdateHandle 은 작업 중단(interrupt)과 재개(resume), 작업 취소(cancel_task)·강제 종료(kill_task), 마지막 보고 위치에서의 재계획 요청(replan), 작업 수락 중지(set_commission), 이슈 생성(create_issue) 기능을 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-537"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "replan(): \"Tell the RMF schedule that the robot needs a new plan.\" 새 계획은 update_position() 으로 준 마지막 위치에서 시작한다(rmf_ros2 main 헤더 주석).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f8",
      "claim": "Open-RMF 의 교통 스케줄은 지연·취소·경로 변경을 반영해 계속 바뀌는 데이터베이스이고, 충돌이 예상되면 관련 플릿 관리자 사이의 협상이 시작되며, 긴급 참여자는 의도적으로 충돌을 게시해 협상을 강제할 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "스케줄은 \"a living database\"로 지연·취소·경로 변경을 반영하고, 충돌 시 conflict notice 후 협상과 제3자 판정으로 선택한다(rmf-core.md).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "Open-RMF 연동 수준 가운데 전체 제어(Full Control)는 경로를 언제든 중단하고 새 경로로 바꿀 수 있고, 신호등 제어(Traffic Light)는 일시정지·재개만 허용하며, 읽기 전용(Read Only) 플릿은 RMF 에 제어권 없이 상태만 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-251",
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Full Control: path can be interrupted at any time and replaced; Traffic Light: pause/resume 만; Read Only: RMF 에 제어권 없음, 한 공간에 하나만(rmf-core.md, integration_fleets.md).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f10",
      "claim": "Open-RMF rmf_ros2 이슈 224 는 플릿 어댑터가 재시작되면 배정된 작업이 유실되는 문제를 제기하고, 작업 로그·백업을 SQLite 로 저장하는 PR 161 과 rmf-web 영속 데이터베이스를 조회하는 대안을 제안하지만, 배포판 반영 여부는 이번에 확인되지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-374"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "재시작 뒤 assigned tasks 가 lost 되며, 작업은 어댑터 내부 큐에만 저장된다고 적는다. 반영 여부 미확인(oq-048 관련, 발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "Hönig 외(IEEE RA-L, 2019)는 MAPF 계획을 후처리해 로봇 간 순서와 운동 제약을 행동 의존 그래프(ADG)로 인코딩함으로써 예기치 않은 감속·장애물·지연에도 계획을 충돌 없이 실행하고 재계획과 실행을 겹치게 하는 창고용 실행 틀을 제시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-188"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ADG 로 순서·운동 제약을 인코딩해 unforeseen delays 에도 실행하며, overlap of re-planning and execution 을 가능하게 한다(검색 요약 기준).",
      "as_of": "2019-04",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f12",
      "claim": "Feng 외(ICAPS 2024)는 실행 중 로봇이 지연될 때 경로는 유지하고 통과 순서만 다시 정하는 전환 가능 간선 탐색(Switchable-Edge Search, SES)을 제안하며, 최선 변형이 중소 규모 문제에서 1초 미만, 대규모 문제에서 기준선보다 최대 4배 빠르다고 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-572"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "delayed agents 에 대해 passing order 를 재스케줄하는 A* 계열 SES, 최적성 증명, 소·중 규모 1초 미만·대규모 최대 4배 빠름(ICAPS 34(1) 201–209, 검색 요약 기준).",
      "as_of": "2024",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "Kalempa 외(Sensors, 2021)의 MRPF 는 작업 간 의존성, 우선순위 기반 선점(preemption) 스케줄링, 고장 복구를 함께 다루는 다중 로봇 작업 배정 방법이며, 소규모 창고 물류 실험 환경(ARENA)에서 평가되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-573"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "priority policies on preemptive task scheduling, dependencies between tasks, tolerates faults; small-scale warehouse logistics(ARENA)에서 평가(검색 요약 기준).",
      "as_of": "2021-09-30",
      "flow_step": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f14",
      "claim": "창고 로봇 경로 계획용 다중 에이전트 롤아웃·재배열(multiagent rollout with reshuffling) 방법은 온라인 재계획으로 환경 변화에 적응하며, 일부 로봇이 고장 나는 예제로 이를 보여 준다.",
      "tag": "사실",
      "source_ids": [
        "ref-574"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "generic rollout 의 online replanning 능력을 물려받아 some robots malfunction 예제로 시연(arXiv 2211.08201 v2, IFAC, 검색 요약 기준).",
      "as_of": "2023",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f15",
      "claim": "ISO 22301:2019(Security and resilience — Business continuity management systems — Requirements)는 교란 사건으로부터 보호하고 발생 가능성을 줄이며 복구를 보장하기 위한 업무연속성 관리 시스템(BCMS)의 수립·운영·점검·개선 요구사항을 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-575"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "BCMS 를 plan, establish, implement, operate, monitor, review, maintain, continually improve 하여 disruptive incidents 에 대비·복구(검색 요약 기준, 유료 원문 미열람).",
      "as_of": "2019",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f16",
      "claim": "국내에서는 「재해경감을 위한 기업의 자율활동 지원에 관한 법률」에 따라 행정안전부가 기업재난관리표준을 고시하고, 재해경감활동관리체계를 갖춘 기업을 문서평가·현장평가를 거쳐 재해경감 우수기업으로 인증한다.",
      "tag": "사실",
      "source_ids": [
        "ref-576"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기업재난관리표준(행정안전부 고시)에 따라 재해경감활동계획을 수립·이행하고 인증대행기관의 1차 문서평가, 2차 현장평가 후 인증 신청(검색 요약 기준, 발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "고용노동부는 2022년 오미크론 확산기에 '중소규모 사업장 기능연속성계획(BCP) 수립 가이드'를 안내했으며, 가이드는 사업 우선순위 파악부터 위험성 분석, 피해 최소화 조치, 분야별 대응, 계획 수립·시행, 공유, 점검까지 7단계로 구성된다.",
      "tag": "사실",
      "source_ids": [
        "ref-577"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "① 사업의 우선순위 파악 ② 위험성 분석 ③ 피해 최소화 조치 ④ 분야별 대응 ⑤ 수립·시행 ⑥ 공유 ⑦ 점검(검색 요약 기준).",
      "as_of": "2022-03",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "Microsoft 아키텍처 센터의 보상 트랜잭션 패턴은 실패한 여러 단계 작업에서 완료된 단계의 효과를 되돌리되 원래 상태를 그대로 복원하는 것이 아니라 업무 규칙에 맞춰 보정하며, 보상 자체가 실패할 수 있으므로 단계를 멱등 명령으로 정의하고 진행 상황을 기록해 실패 지점부터 재개하고, 영향이 큰 결정에는 사람을 참여시키라고 권한다.",
      "tag": "사실",
      "source_ids": [
        "ref-578"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"define each step as an idempotent command\"; 진행 기록 후 실패 지점부터 재개, 자동화가 어려운 고영향 결정은 사람 포함(compensating-transaction.md, 2026-04-16).",
      "as_of": "2026-04-16",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f19",
      "claim": "Element Logic 은 AutoStore 의 XHandler 소프트웨어 모듈이 고장 난 로봇을 넘겨받아 시스템을 멈추지 않고 오류를 처리하며, 자동 처리가 불가능하거나 로봇 충돌 위험이 있을 때만 시스템이 정지한다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-579"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: XHandler 가 failed robot 을 넘겨받아 시스템 정지 없이 복구 시도, 자동 처리 불가·충돌 위험 시에만 정지(FAQ 검색 요약 기준, 발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": "피킹",
      "flow_item": "예외·성과",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f20",
      "claim": "Swisslog 은 AutoStore 그리드에서 로봇이 멈추면 자사 SynQ 소프트웨어가 멈춘 로봇 아래 보관함의 재고를 다른 보관함으로 재할당해, 멈춘 로봇을 정기 휴식이나 저수요 시간에 꺼낼 때까지 주문 처리를 계속한다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-580"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: SynQ 가 stalled robot 아래 재고를 다른 bin 으로 re-allocate 하고 로봇 제거 전까지 주문 처리 지속(블로그 검색 요약 기준).",
      "as_of": "2025-07",
      "flow_step": "피킹",
      "flow_item": "예외·성과",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f21",
      "claim": "GS1 EPCIS 저장소는 기존 이벤트를 수정·삭제하지 않는 일지(journal) 방식이며, 잘못 기록된 이벤트는 같은 eventID 에 오류 선언(errorDeclaration: 선언 시각, 사유, 정정 이벤트 id 목록)을 붙인 이벤트로 정정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-581"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "no mechanism for modification or deletion; 정정 시 원 eventID 와 같은 near-duplicate 이벤트가 ErrorDeclaration 과 correctiveEventIDs 를 가리킨다(EPCIS 1.2, 검색 요약 기준).",
      "as_of": "2016-09-29",
      "flow_step": null,
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "f1~f4·f13·f18·f21 을 종합하면 운반 중 고장 로봇의 화물과 남은 주문 처리는 고장·연결 끊김 감지(오류·연결 상태), 주문 일시정지·취소, 실린 화물 식별(loads), 남은 작업의 재배정, 화물의 물리적 회수, 재고·이벤트 기록의 보상·정정으로 이어지는 결정 흐름으로 볼 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-051",
        "ref-573",
        "ref-578",
        "ref-581"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "개별 출처는 각 단계의 메커니즘만 다루며, 이 흐름을 한 절차로 정한 출처는 이번 조사에서 찾지 못했다(종합 추정).",
      "as_of": "2026-09-25",
      "flow_step": "피킹",
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f23",
      "claim": "연계 대상: 장애물 회피·재위치 추정·비상정지 회로 같은 로봇 자체 복구·안전 제어는 제조사 몫이고, VDA 5050·Open-RMF 가 관제에 주는 기능(주문 취소·일시정지·재계획 요청·작업 수락 중지·이슈 보고)을 보면 이종 로봇을 연결하는 ROP 는 주문 취소·재배정·수동 전환 결정과 기록 정정을 맡는 경계가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-537"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDA 5050 은 로봇이 오류를 보고하고 관제가 취소·새 주문·사용자 개입을 결정하는 구조이고, RobotUpdateHandle 은 interrupt·replan·set_commission 을 관제 쪽에 준다(경계 추정).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f24",
      "claim": "VDA 5050 에서 연결이 끊긴 로봇이 마지막 해제 노드까지만 주행한다는 규칙(f2)을 보면, 관제가 한 번에 해제하는 주문 범위(base)의 길이가 통신 단절 동안 현장 작업이 얼마나 계속되는지를 정하는 설계 변수가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "끊긴 로봇은 order 를 last released node 까지 수행하고, newBaseRequest 가 없으면 속도를 줄인다(state.schema 설명과 명세의 종합, oq-038 관련 추정).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
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
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 최신판(3.0.0) 명세 원문. cancelOrder·startPause·연결 끊김·오류 처리와 관제 역할을 규정한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 상태 메시지 JSON 스키마. errorLevel, actionStatus, loads, paused, newBaseRequest 필드를 정의한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/json_schemas/state.schema",
      "source_unopened": false
    },
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/rmf-core.md",
      "source_unopened": false
    },
    {
      "id": "ref-251",
      "org": "Open Robotics",
      "title": "Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration)",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 플릿 어댑터 연동 수준(Full Control, Easy Full Control, Traffic Light)과 경로 중단·교체 방식을 설명하는 장.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/integration_fleets.md",
      "source_unopened": false
    },
    {
      "id": "ref-537",
      "org": "Open Robotics (open-rmf/rmf_ros2)",
      "title": "rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "플릿 어댑터의 로봇 갱신 핸들 API 헤더. interrupt·resume·cancel_task·kill_task·replan·set_commission·create_issue·responsive wait 등의 문서 주석을 담는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp",
      "source_unopened": false
    },
    {
      "id": "ref-188",
      "org": "Hönig, W., Kiesel, S., Tinka, A., Durham, J. W., & Ayanian, N.",
      "title": "Persistent and Robust Execution of MAPF Schedules in Warehouses",
      "published": "2019-04",
      "url": "https://ieeexplore.ieee.org/abstract/document/8620328/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 행동 의존 그래프로 창고 MAPF 계획을 지연·감속에 강건하게 실행하고 재계획과 실행을 겹치게 하는 틀(IEEE RA-L).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-572",
      "org": "Feng, Y., Paul, A., Chen, Z., & Li, J.",
      "title": "A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution",
      "published": "2024",
      "url": "https://arxiv.org/abs/2403.18145",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 실행 중 지연된 로봇의 통과 순서를 전환 가능 간선 탐색(SES)으로 실시간 재스케줄하는 알고리즘(ICAPS 2024).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-573",
      "org": "Kalempa, V. C., Piardi, L., Limeira, M., & de Oliveira, A. S.",
      "title": "Multi-Robot Preemptive Task Scheduling with Fault Recovery: A Novel Approach to Automatic Logistics of Smart Factories",
      "published": "2021-09-30",
      "url": "https://www.mdpi.com/1424-8220/21/19/6536",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 우선순위 선점 스케줄링·작업 의존성·고장 복구를 결합한 다중 로봇 작업 배정 방법 MRPF(Sensors 21(19)).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-574",
      "org": "KTH 연구진 (arXiv:2211.08201)",
      "title": "Multiagent Rollout with Reshuffling for Warehouse Robots Path Planning",
      "published": "2023",
      "url": "https://arxiv.org/abs/2211.08201",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 창고 로봇 경로 계획용 다중 에이전트 롤아웃 방법으로, 온라인 재계획으로 로봇 고장에 적응하는 예제를 보인다(IFAC 게재, 프리프린트).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-575",
      "org": "ISO",
      "title": "ISO 22301:2019 - Security and resilience — Business continuity management systems — Requirements",
      "published": "2019",
      "url": "https://www.iso.org/standard/75106.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 업무연속성 관리 시스템(BCMS)의 요구사항 국제표준. 유료 원문은 열지 못하고 발행 기관 소개 페이지 검색 결과로 확인.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-576",
      "org": "행정안전부",
      "title": "재해경감 우수기업 인증제도",
      "published": null,
      "url": "https://www.mois.go.kr/frt/sub/a06/b10/disasterMitigationCompanies/screen.do",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 재해경감을 위한 기업의 자율활동 지원에 관한 법률에 따른 기업재난관리표준과 재해경감 우수기업 인증 절차 안내.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-577",
      "org": "고용노동부",
      "title": "중소규모 사업장 기능연속성계획(BCP) 수립 가이드 안내",
      "published": "2022-03",
      "url": "https://www.moel.go.kr/news/notice/noticeView.do?bbs_seq=20220301591",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 오미크론 확산기 사회 필수 기능 유지를 위한 중소규모 사업장 BCP 수립 7단계 가이드 안내.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-578",
      "org": "Microsoft (MicrosoftDocs/architecture-center)",
      "title": "Compensating Transaction pattern",
      "published": "2026-04-16",
      "url": "https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "여러 단계 작업이 실패할 때 완료된 단계를 되돌리는 보상 트랜잭션 패턴 설명. 멱등 단계, 진행 기록, 사람 개입을 권한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/main/docs/patterns/compensating-transaction.md",
      "source_unopened": false
    },
    {
      "id": "ref-579",
      "org": "Element Logic",
      "title": "FAQ - Element Logic (AutoStore)",
      "published": null,
      "url": "https://www.elementlogic.net/solutions-and-services/autostore/faq/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AutoStore 통합 업체의 FAQ. 로봇 고장 시 XHandler 모듈의 처리와 시스템 지속 운영을 설명한다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-580",
      "org": "Swisslog",
      "title": "The benefits of using AutoStore for high-throughput retail fulfillment",
      "published": "2025-07",
      "url": "https://www.swisslog.com/en-us/case-studies-and-resources/blog/2025/07/benefits-of-autostore-htp",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Swisslog 블로그. 멈춘 로봇 아래 재고를 SynQ 가 재할당해 주문 처리를 계속한다고 설명한다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-581",
      "org": "GS1",
      "title": "EPC Information Services (EPCIS) Standard 1.2",
      "published": "2016-09-29",
      "url": "https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. EPCIS 1.2 표준. 저장소를 일지 방식으로 두고 오류 선언(errorDeclaration)으로 이벤트를 정정하는 방법을 정한다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-374",
      "org": "Open Robotics (open-rmf/rmf_ros2)",
      "title": "Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/issues/224",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 플릿 어댑터 재시작 시 작업 유실 문제와 SQLite 백업(PR 161)·rmf-web 영속 DB 조회 제안을 다룬 이슈.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md",
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
      "rationale": "3절 왜 중요한가: f19·f20(벤더 주장 병기, 고장 로봇 하나가 전체를 멈추지 않게 하는 설계), f15·f17(업무 연속성) / 4절 용어: f1(cancelOrder), f2(연결 상태), f3(오류 수준·RETRIABLE), f18(보상 트랜잭션), f21(오류 선언), f11(ADG, 기존 용어 재사용) / 5절 시나리오: 피킹 단계 운반 중 고장 f22(시작 조건·작업 대상 f4·수행 자원 f13·완료·인계 f21·예외·성과 f1·f19·f20), 통신 단절 f2·f24 / 6절 접근법: 관제 인터페이스의 중단·취소·재계획 f1~f10, 실행 중 재계획 f11·f12·f14, 고장 허용 재배정 f13, 보상·정정 f18·f21 / 7절 표준·오픈소스: VDA 5050(f1~f6), Open-RMF(f7~f10), ISO 22301(f15), 국내 제도(f16·f17), EPCIS(f21) / 8절 연구: f11~f14 / 9절 범위: f23(로봇 자체 복구·안전 제어는 연계 대상) / 10절 연결: 12. 명령·작업 실행의 신뢰성(f1·f2·f10), 13. 작업 배정 — MRTA(f13), 15. 다중 로봇 경로·교통 관리 — MAPF(f8·f11·f12·f14), 19. 모니터링·이상 탐지·원인 분석(f3·f7 이슈 보고), 18. 사람–로봇 협업·운영 인터페이스(f5·f18 사람 개입), 7. 화물·재고·자산 식별과 추적(f4·f21, oq-003), 1. 주문·업무 시스템 연계(f18, oq-021), 11. 분산 시스템·통신·컴퓨팅 구조(f2·f24, oq-038), 22. 시뮬레이션·예측용 디지털 트윈(제한 운영 처리량 추정 질문) / 11절 열린 질문: oq-003·oq-021·oq-038·oq-048(f10 은 부분 근거일 뿐 해결 아님)과 새 질문 3건"
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "보상 트랜잭션",
      "term_en": "Compensating Transaction",
      "definition": "여러 단계로 이루어진 작업이 도중에 실패했을 때 이미 완료된 단계의 효과를 업무 규칙에 맞게 되돌리는 작업이다."
    },
    {
      "term_ko": "업무연속성 관리 시스템",
      "term_en": "Business Continuity Management System (BCMS)",
      "definition": "교란 사건에 대비하고 핵심 업무를 지속·복구하기 위한 조직의 관리 체계로, ISO 22301 이 요구사항을 정한다."
    },
    {
      "term_ko": "주문 취소 즉시 동작",
      "term_en": "cancelOrder (VDA 5050 instant action)",
      "definition": "VDA 5050 에서 관제가 보내면 로봇이 가능한 한 빨리 정지하고 남은 동작을 실패로 보고한 뒤 유휴 상태가 되게 하는 즉시 동작이다."
    }
  ],
  "open_questions_new": [
    "운반 중 고장 난 로봇에 실린 화물을 사람이나 다른 로봇이 회수할 때 어떤 확인(스캔·무게·위치)으로 재고 위치를 바로잡는지 정한 운영 기준이나 국내 사례가 있는가? | 관련 영역: 20. 예외 복구·재계획·업무 연속성, 7. 화물·재고·자산 식별과 추적 | 근거: f22 | 종류: 일반",
    "국내 물류센터가 로봇·관제 장애 때 수동 운영이나 제한 운영으로 전환하는 기준(허용 중단 시간, 전환·복귀 절차)을 BCP 에 정한 사례가 있는가? | 관련 영역: 20. 예외 복구·재계획·업무 연속성, 18. 사람–로봇 협업·운영 인터페이스 | 근거: f16 | 종류: 일반",
    "로봇 일부가 멈춘 제한 운영 상태의 처리량 저하를 미리 추정해 전환 결정에 쓰는 방법이나 사례가 있는가? | 관련 영역: 20. 예외 복구·재계획·업무 연속성, 22. 시뮬레이션·예측용 디지털 트윈 | 근거: f20 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 17,
    "cross_checked_count": 0,
    "unverified": [
      "f3: 명세 본문 요약은 오류 수준을 WARNING·CRITICAL 위주로 설명하고 state 스키마는 네 값을 두어, 본문 문구와 스키마를 글자 단위로 대조하지 못함",
      "f10: PR 161(SQLite 작업 백업)이 현재 배포판에 반영됐는지 미확인 — oq-048 해결 제안하지 않음",
      "f11~f17·f21: 원문 미열람, 검색 요약 기준",
      "ISO 22301 의 업무 영향 분석·목표 복구 시간(RTO) 요구는 제3자 해설에서만 확인되어 finding 으로 내지 않음",
      "KS A ISO 22301 부합화 연도는 출처를 특정하지 못해 finding 으로 내지 않음",
      "ref-574 저자 이름 미확인(KTH 연구진으로 표기)",
      "f19·f20 벤더 주장, 독립 확인 없음",
      "모든 finding 교차 확인 없음"
    ],
    "scope_violations": [
      "f23: 장애물 회피·재위치 추정·비상정지 회로는 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시하고 ROP 는 취소·재배정·기록 정정만 맡는다고 구분",
      "f16·f17: 기업 BCP 체계 전반은 전사 관리 영역이라 ROP 직접 범위가 아니며 현장 로봇 운영 계획의 참조 틀로만 제안"
    ],
    "budget_used": {
      "queries": 20,
      "sources": 14
    },
    "limits": "재실행(스키마 불일치) 1회차. 반려 사유 1·2(f19·f20 이 벤더 문서만 근거로 한 [사실]이고 vendor_claim 표시 없음): 직전 research.json 이 이번 입력에 포함되지 않아 형식만 고칠 원본이 없었으므로, 같은 대상에 대해 예산 안에서 브리프 전체를 다시 작성했다. 벤더 문서만 근거로 한 f19(Element Logic·AutoStore XHandler)·f20(Swisslog SynQ 재고 재할당)은 vendor_claim: true, 태그 추정, 신뢰도 low, evidence_excerpt 첫머리 '벤더 주장: '으로 냈다(관련 finding: f19, f20). 직전 브리프와 finding 번호·내용이 다를 수 있다. web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: 재사용 ref-031·ref-051(VDA 5050)·ref-004(rmf-core), 신규 ref-251(integration_fleets)·ref-537(RobotUpdateHandle.hpp)·ref-578(보상 트랜잭션 패턴). 그 밖의 신규 출처는 원문 미열람(신뢰도 상한 medium). web_fetch_available: false 에 따라 재사용 출처의 신뢰도도 medium 으로 적었다. 검색 20회/30, 신규 출처 14건/15(ref-251~ref-374, 예약 구간 안). 한국 자료: 행정안전부 재해경감 인증(f16), 고용노동부 BCP 가이드(f17). 국내 물류센터의 로봇 장애 수동 전환 사례는 한국어 검색 3회에서 찾지 못함(열린 질문으로 올림). 입력의 참고문헌 목록은 요약본(0건 표시)이라 기존 id 는 이전 브리프에 나온 ref-031·ref-051 과 공통 규칙의 ref-004 만 재사용했다 — 같은 URL 이 이미 있으면 퍼블리셔가 합쳐야 한다. 기존 열린 질문 oq-003·oq-021·oq-038·oq-048 은 관련 근거(f21·f18·f2·f24·f10)만 내고 해결 제안하지 않음. 27. AI·학습·적응과 모델 운영 관련 주장 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 열린 질문 1건으로만 연결했고 섞지 않았다. 정정 요청 없음."
  }
}
```

### runs/2026-09-25-50/verification.json

```json
{
  "run_id": "2026-09-25-50",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문(data/source_texts/ref-031.txt) 6.1.3 절 — 가능한 한 빨리 정지, 예정 동작 FAILED, 정지 뒤 cancelOrder FINISHED, 유휴. 단일 출처(같은 발행 주체). evidence_excerpt 의 '취소 시 적재물 처리는 따로 정하지 않는다'는 원문에 언급이 없다는 해석이므로 본문에 쓰면 [추정]으로 둔다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 4.1 절 last will·'fulfills the order up to the last released node'(입력 원문). 단 github_raw 로 다시 연 6.5 절에는 connectionState 값이 HIBERNATING 까지 넷이다 — 세 값만 적은 것은 불완전하므로 수정 지시. 원문은 connection 토픽을 로봇 상태 점검용으로 쓰지 말라고 적는다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: state.schema(github_raw 열람) errorLevel = WARNING·URGENT·CRITICAL·FATAL, actionStatus 에 RETRIABLE. 명세 6.2.3.2 에서 RETRIABLE 상태의 로봇은 관제 또는 운영자 개입을 기다리고 retry·skipRetry 즉시 동작으로 처리된다. ref-051·ref-031 은 발행 주체가 같아 교차 확인이 아니다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: state.schema loads 의 loadId(바코드·RFID 예시), loadType, loadPosition, loadDimensions, weight(kg). '관제가 알 수 있는 근거가 된다'는 로봇이 loads 를 보고하는 경우에 한한다(선택 필드)."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 표 4 의 startPause·stopPause 설명과 state.schema paused 설명이 일치."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "부분 확인: 5.3 절 관제 기능 목록에 교착 탐지·해소와 통신 오류 탐지·해소가 있음(입력 원문). 그러나 '사용자 개입이 필요한지, 취소 뒤 새 주문을 보낼지 관제가 결정'하는 문장은 6.1.5 절 통로(corridor) 이탈 오류(OUTSIDE_OF_CORRIDOR) 맥락이고, 6.4.5 절 구역 오류 처리는 관제가 진행 방법을 정한다고만 적는다 — '구역 충돌' 표현 수정 지시. 2장 범위에서 교착 해소 전략·알고리즘 자체는 명세 밖이다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: RobotUpdateHandle.hpp(github_raw 열람)에 interrupt, Interruption::resume, cancel_task, kill_task, replan(update_position 으로 준 마지막 위치에서 새 계획), set_commission(Commission: 배정·직접 작업 수락 여부), create_issue 가 있음. 헤더 문서 주석 기준이며 동작 검증은 아님."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-004 — 'living database' 로 지연·취소·경로 변경 반영, 충돌 통지 뒤 플릿 관리자 협상과 제3자 판정, 긴급 참여자의 의도적 충돌 게시. 게시된 D. 계획·최적화 연결 주장(실행 2026-09-25-49 f15)과 같은 출처이므로 ref-004 각주 재사용."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: integration_fleets.md(github_raw) — Full Control 은 경로를 언제든 중단·교체, Traffic Light 는 pause/resume 만 허용. Read Only 는 ref-251 에 없고 ref-004 에만 있다(제어권 없음, 공유 공간당 하나). ref-004·ref-251 는 같은 발행 주체라 교차 확인 아님. 각주를 주장 부분별로 맞게 단다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람, 검색 결과 일치: 이슈 224 의 재시작 뒤 작업 유실, SQLite 작업 백업 PR 161, rmf-web 영속 DB 조회 제안이 검색 요약에 나타남. 발행일 미확인. 반영 여부 미확인이므로 oq-048 은 해결 아님."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 같은 논문·같은 URL 이 기존 ref-188(실행 2026-09-25-49 f23, 게시된 D. 계획·최적화 연결)로 이미 있다 — ref-188 을 새로 등록하지 말고 ref-188 재사용. 용어는 기존 용어집 action-dependency-graph(행동 의존 그래프) 재사용."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람, 검색 결과 일치(arXiv 2403.18145, ICAPS 34 pp.201–209, 저자 Feng·Paul·Chen·Li): SES 가 지연된 로봇의 통과 순서를 재스케줄, 최선 변형이 중소 규모 1초 미만·대규모 기준선 대비 최대 4배 빠름. 수치는 저자 보고값이며 단일 출처."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람, 검색 결과 일치(MDPI Sensors 21(19) 6536, 저자 Kalempa·Piardi·Limeira·Oliveira): 우선순위 선점 스케줄링·작업 의존성·고장 허용, ARENA 소규모 창고 물류 실험."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람, 검색 결과로 실재 확인(arXiv 2211.08201 v2 2023-06-03, IFAC 2023 게재). 저자는 Emanuelsson, Penacho Riveiros, Li, Johansson, Mårtensson(KTH) — 출처 기관 칸 수정 지시. 고장 예제 부분은 리서치 브리프의 검색 요약 기준이며 이번 검증 검색에서 다시 확인하지 못함."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(유료), 검색 결과로 ISO 소개 페이지·제목 일치 확인. ISO 22301:2019 는 2012 판을 대체한 2판이고, 개정 1:2024(기후 행동 변경, iso.org/standard/88412)이 있다 — 기준 판 명시 지시."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람, 검색 결과 일치: 행정안전부 페이지가 「재해경감을 위한 기업의 자율활동 지원에 관한 법률」, 기업재난관리표준(행정안전부 고시), 인증대행기관의 1차 문서평가·2차 현장평가를 설명. 발행일 미확인."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람, 검색 결과 일치(고용노동부 공지 bbs_seq=20220301591, 2022-03): 오미크론 확산기 중소규모 사업장 BCP 가이드와 7단계. 감염병 대응 목적의 권고 가이드임을 본문에 밝힌다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: compensating-transaction.md(github_raw, ms.date 2026-04-16) — 원래 상태를 반드시 복원하지 않음, 보상 실패 가능, 단계를 멱등 명령으로, 진행 기록 후 실패 지점부터 재개, 영향이 크거나 자동화가 어려운 결정은 사람 포함. 소프트웨어 설계 패턴이므로 물리 작업 되돌림에 적용하는 부분은 [추정]으로 서술."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람, 검색 결과 일치: XHandler 가 고장 로봇을 넘겨받아 시스템 정지 없이 복구 시도, 자동 처리 불가·충돌 위험 때만 정지. [추정]·벤더 주장·vendor_claim 표시 적정. 통합업체 FAQ 로 AutoStore 와 독립 출처가 아니다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람, 검색 결과 일치: SynQ 가 멈춘 로봇 아래 재고를 다른 보관함으로 재할당하고 정기 휴식·저수요 시간에 로봇을 꺼낼 때까지 주문 처리 지속. [추정]·벤더 주장 표시 적정. 검색에 나온 URL 은 https://www.swisslog.com/en-us/blog/2025/07/benefits-of-autostore-htp 로 브리프 URL 경로와 다르다 — 수정 지시."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람, 검색 결과 일치: 저장소를 일지 방식으로 두어 수정·삭제 수단이 없고, 같은 eventID 의 거의 같은 이벤트가 ErrorDeclaration(선언 시각, 선택 사유, 선택 correctiveEventIDs)을 가리킨다. EPCIS 1.2(2016-09-29) 기준이며 현행 판은 아님 — 기준 판 명시. 기존 용어집 epcis-error-declaration 재사용."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정으로 [추정]·low 적정. 근거 출처 가운데 ref-573·ref-581 은 원문 미열람인데 finding 은 source_unopened: false 로 적혀 있다(브리프 표시 불일치, 페이지 서술에는 영향 없음). 이 흐름을 한 절차로 정한 출처는 없다고 밝힌다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "경계 추정으로 [추정] 적정. '연계 대상:' 표시가 있고 분류 원문 9장 '로봇 자체 지능·제어' 경계와 맞다. VDA 5050 2장이 운영 책임 배분을 범위 밖으로 둔다는 점과도 맞는다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 적정. 근거 확인: 4.1 절 last released node 규칙, 6.1.2 절 결정 지점에서 정지, state.schema newBaseRequest '새 기반이 오지 않으면 속도를 줄인다'. oq-038 해결은 아님."
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
      "ref-188(Hönig 외, Persistent and Robust Execution of MAPF Schedules in Warehouses, https://ieeexplore.ieee.org/abstract/document/8620328/)은 기존 ref-188 과 같은 논문·같은 URL — 실행 2026-09-25-49 f23(D. 계획·최적화 대분류 연결)에서 이미 인용",
      "f8·f9 는 실행 2026-09-25-49 f15(Open-RMF 제어 수준·교통 협상, ref-004)와 겹친다 — ref-004 각주 재사용",
      "f3 는 실행 2026-09-25-48 f1(VDA 5050 errorLevel 네 값, ref-051)과 겹친다 — ref-051 각주 재사용, 19. 모니터링·이상 탐지·원인 분석과 연결",
      "f2 는 실행 2026-09-25-48 f4(connection 토픽 last will, ref-506 connection.schema)와 겹친다"
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "f11 의 행동 의존 그래프(ADG)는 용어집 action-dependency-graph 로 이미 있다 — 새 등록하지 않고 재사용",
      "f21 의 오류 선언(errorDeclaration)은 용어집 epcis-error-declaration 로 이미 있다 — 재사용",
      "용어 후보 '업무연속성 관리 시스템'은 세부영역 원문 명칭 '20. 예외 복구·재계획·업무 연속성'의 띄어쓰기('업무 연속성')와 다르다 — '업무 연속성 관리 시스템'으로 통일"
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "ref-188: 새 참고문헌으로 등록하지 않고 기존 ref-188(같은 논문·같은 URL)로 바꾼다. f11 을 쓰는 본문 각주와 reference_updates 모두 ref-188 을 쓴다 — 중복 출처 방지.",
    "f11·f21: 행동 의존 그래프와 오류 선언은 기존 용어집 항목(action-dependency-graph, epcis-error-declaration)에 연결하고 glossary_updates 에 새로 넣지 않는다 — 용어집에 이미 있다.",
    "용어 후보 '업무연속성 관리 시스템'을 '업무 연속성 관리 시스템'으로 고쳐 등록한다 — 세부영역 명칭의 띄어쓰기와 맞춘다.",
    "f2: connectionState 값을 ONLINE·OFFLINE·CONNECTION_BROKEN·HIBERNATING 네 값으로 적거나 '등'을 붙인다 — ref-031 6.5 절(github_raw 열람)에 HIBERNATING 이 있다.",
    "f6: '구역 충돌 같은 상황에서' 부분을 '통로(corridor) 이탈 오류 같은 상황에서'로 고친다 — 사용자 개입·취소 뒤 새 주문 결정 문장은 ref-031 6.1.5 절 문맥이다. 교착 해소 전략·알고리즘 자체는 명세 범위 밖(ref-031 2장)이라는 점도 함께 적는다.",
    "f1: evidence_excerpt 의 '취소 시 적재물 처리는 따로 정하지 않는다'를 본문에 쓰면 [추정]으로 두고 '6.1.3 절에 적재물 언급이 없음'으로 표현한다 — 명세 원문에 없는 해석이다.",
    "f9: Read Only 설명의 각주는 ref-004 만 단다 — ref-251(integration_fleets)는 Full Control·Traffic Light 만 다룬다.",
    "f12: 1초 미만·최대 4배 수치를 '저자 보고값(ICAPS 2024, 단일 출처)'으로 명시한다 — 독립 교차 확인이 없다.",
    "f15: 'ISO 22301:2019 기준(개정 1:2024 별도)'으로 판을 명시한다 — ISO 가 2024년 개정 1(기후 행동 변경)을 냈다.",
    "f21: 'EPCIS 1.2(2016-09-29) 기준'을 본문에 명시하고 현행 판에서의 유지 여부는 단정하지 않는다 — 현행 판 원문을 확인하지 않았다.",
    "f15·f16·f17: 기업 BCP·BCMS 체계는 ROP 직접 범위가 아니라 현장 제한 운영·수동 전환 계획의 참조 틀(연계 대상)로 짧게 서술하고, f17 은 감염병 대응 권고 가이드임을 밝힌다.",
    "f19·f20: 본문에서 [추정] 뒤에 '벤더 주장'을 병기하고, AutoStore 자체 제어기(XHandler)·통합업체 소프트웨어(SynQ)의 기능으로 서술하며 ROP 기능처럼 쓰지 않는다 — 두 출처는 서로 독립이 아니다.",
    "f18: 보상 트랜잭션 패턴을 물리 작업·재고 되돌림에 적용하는 문장은 [추정]으로 쓴다 — 출처는 소프트웨어 설계 패턴이다.",
    "ref-574: 기관 칸을 'Emanuelsson, W., Penacho Riveiros, A., Li, Y., Johansson, K. H., & Mårtensson, J. (KTH)'로 고친다 — 검색 결과로 저자를 확인했다.",
    "ref-580: URL 을 검색 결과로 확인한 https://www.swisslog.com/en-us/blog/2025/07/benefits-of-autostore-htp 로 고친다 — 브리프 URL 경로가 확인되지 않았다.",
    "원문을 열지 못한 출처(ref-188, ref-572, ref-573, ref-574, ref-575, ref-576, ref-577, ref-579, ref-580, ref-581, ref-374)는 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣는다. 발행일이 없는 ref-576·ref-579·ref-374 는 각주 발행일 자리에 '미확인'을 쓴다.",
    "11절 열린 질문: oq-003·oq-021·oq-038·oq-048 은 해결로 바꾸지 않는다 — f10·f18·f21·f24 는 부분 근거일 뿐 답이 아니다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. raw.githubusercontent.com 으로 연 출처(ref-031, ref-051, ref-004, ref-251, ref-537, ref-578)는 원문과 대조했고, 나머지는 검색 결과 일치로 확인했다. 확인 24건, 미확인 0건, 교차 확인 0건(VDA 5050 명세와 스키마, Open-RMF 문서들은 각각 발행 주체가 같아 독립 교차 확인이 아니다). 강등: 없음(f19·f20 은 이미 [추정]·벤더 주장). 원문 미열람 출처: ref-188(브리프의 ref-188, 기존 id 로 통합), ref-572, ref-573, ref-574, ref-575, ref-576, ref-577, ref-579, ref-580, ref-581, ref-374. 수정 사항: f2 connectionState 에 HIBERNATING 누락, f6 사용자 개입 결정은 통로 이탈 오류 문맥, ISO 22301 개정 1:2024 와 EPCIS 1.2 기준 판 명시, ref-574 저자·ref-580 URL 정정. 브리프 표시 불일치: f22 는 원문 미열람 출처(ref-573·ref-581)에 기대는데 source_unopened: false 로 적혀 있다. 해결 인정한 열린 질문 없음(oq-003·oq-021·oq-038·oq-048 은 부분 근거만 있음). 정정 요청 없음. 검증 검색 10회(리서치 20회와 합쳐 30/30, 상한 도달). 주의: 핵심 주장은 표준·오픈소스 문서 각각 한 곳에 기댄다. 연구 수치(f12)는 저자 보고값이다. 운반 중 고장 처리 흐름(f22)과 ROP 경계(f23)는 이를 한 절차로 정한 출처가 없는 종합 추정이다.",
  "retry_reason": null
}
```

### docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md

```markdown
---
title: "20. 예외 복구·재계획·업무 연속성"
type: area
category: "E. 협업·현장 운영"
area_no: 20
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [E. 협업·현장 운영](index.md) › 20. 예외 복구·재계획·업무 연속성

# 20. 예외 복구·재계획·업무 연속성

!!! info "소속 대분류"
    [E. 협업·현장 운영](index.md) — 핵심 질문:
    계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 [분류원문]

## 2. SCM 관점의 질문

운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? [분류원문]

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

### docs/categories/e-collaboration-and-field-operations/index.md

```markdown
---
title: "E. 협업·현장 운영"
type: category
status: seed
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](../../index.md) › E. 협업·현장 운영

# E. 협업·현장 운영

## 핵심 질문

계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? [분류원문]

## 개요

**계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가**를 연구한다. 정상적인 시연과 실제 운영의 차이가 많이 드러나는 영역이다. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·SCM 관점의 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **17. 로봇 간 협업·물리적 인계** | 이동로봇–로봇팔 협업, 공동 운반, 작업 동기화, 인계 확인, 필요한 정보·인식 결과 공유 | AMR이 물건을 가져온 뒤 로봇팔이 안전하게 인수했음을 어떻게 확인할까? | [17. 로봇 간 협업·물리적 인계](17-robot-to-robot-collaboration-and-physical-handover.md) | published |
| **18. 사람–로봇 협업·운영 인터페이스** | 작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 | 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? | [18. 사람–로봇 협업·운영 인터페이스](18-human-robot-collaboration-and-operator-interface.md) | published |
| **19. 모니터링·이상 탐지·원인 분석** | 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 | 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? | [19. 모니터링·이상 탐지·원인 분석](19-monitoring-anomaly-detection-and-root-cause-analysis.md) | seed |
| **20. 예외 복구·재계획·업무 연속성** | 고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 | 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? | [20. 예외 복구·재계획·업무 연속성](20-exception-recovery-replanning-and-business-continuity.md) | seed |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

17번의 협업은 이동로봇끼리 길을 양보하는 문제보다 넓다. **이동·조작·검사·사람 작업을 하나의 공정으로 묶는 문제**까지 포함한다. NIST도 이종 로봇과 사람의 협업 성능을 별도 연구·평가 대상으로 다룬다. [7] [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-25 · 갱신 · [18. 사람–로봇 협업·운영 인터페이스](18-human-robot-collaboration-and-operator-interface.md) — 영역 심화: 3~11절 신규 작성(협동 피킹 조율, VDA 5050 운용 모드·안전 상태, 관제 대시보드, 안전 표준·국내 가이드, 설명·감독, 트랙 자연어 업무 지시 챗봇 반영 제안 6건 검토 반영), 페이지 상태 자동 영역 추가. 2차: 9절 시설·설비 제어 행을 [추정]으로 낮추고 Open-RMF 데모 내용을 따로 적음 (실행 2026-09-25-46)
- 2026-09-25 · 생성 · [18. 사람–로봇 협업·운영 인터페이스 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area18-s6.md) — 자동 분리: 18. 사람–로봇 협업·운영 인터페이스 의 "6. 대표 접근법과 기술" 절을 옮겼다. 27. AI·학습·적응과 모델 운영 링크를 주제 페이지 기준 경로로 고침. 2차: 운용 모드 소절 마지막 문장을 [사실]과 [추정]으로 나눔 (실행 2026-09-25-46)
- 2026-09-25 · 생성 · [18. 사람–로봇 협업·운영 인터페이스 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area18-s7.md) — 자동 분리: 18. 사람–로봇 협업·운영 인터페이스 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,079자)을 옮겼다 (실행 2026-09-25-46)
- 2026-09-25 · 생성 · [18. 사람–로봇 협업·운영 인터페이스 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area18-s4.md) — 자동 분리: 18. 사람–로봇 협업·운영 인터페이스 의 "4. 핵심 개념과 용어" 절(897자)을 옮겼다 (실행 2026-09-25-46)
- 2026-09-25 · 생성 · [18. 사람–로봇 협업·운영 인터페이스 — 대표 연구와 자료](../../topics/2026/2026-09-25-area18-s8.md) — 자동 분리: 18. 사람–로봇 협업·운영 인터페이스 의 "8. 대표 연구와 자료" 절(750자)을 옮겼다 (실행 2026-09-25-46)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [7]은 참고문헌 [ref-007](../../references/ref-007.md)에 해당한다.[^ref-007]

[^ref-007]: NIST, Performance of Collaborative Robot Systems, 미확인, https://www.nist.gov/programs-projects/performance-collaborative-robot-systems, 접근일 2026-09-24
```

### templates/area.md

```markdown
---
title: "{{area_no}}. {{area_name}}"        # 원문 명칭 그대로. 예: "7. 화물·재고·자산 식별과 추적"
type: area
category: "{{category}}"                    # 소속 대분류 원문 명칭. 예: "B. 공통 정보·환경 모델"
area_no: {{area_no}}                        # 1~28 정수
related_areas: [{{related_areas}}]          # 10절에서 연결한 세부영역 번호. 예: [8, 12, 17]. 없으면 []
tags: [{{tags}}]                            # 핵심 용어 3~6개. 예: [EPCIS, 인계 확인, 자산 추적]. 시드면 []
status: {{status}}                          # seed | draft | verified | published | needs_update | deprecated
confidence: {{confidence}}                  # high | medium | low. 내용 검증 에이전트가 부여. 시드면 이 줄을 뺀다
created: {{created}}                        # YYYY-MM-DD. 페이지를 처음 만든 날
updated: {{updated}}                        # YYYY-MM-DD. 마지막으로 내용을 바꾼 날
sources: [{{sources}}]                      # 이 페이지 각주에 쓴 참고문헌 id. 예: [ref-003, ref-021]. 없으면 []
last_run: {{last_run}}                      # 이 페이지를 마지막으로 다룬 실행 날짜 YYYY-MM-DD. 시드면 이 줄을 뺀다
version: {{version}}                        # 정수. 시드 1, 갱신마다 +1
---
<!--
[템플릿] 세부 연구영역 페이지 (type: area)
경로: docs/categories/<대분류 slug>/<두 자리 번호-slug>.md  (아래 경로 규약 표)
쓰임: 구축 시 시드 생성 → 영역 심화 실행(1주기)에서 3~11절 작성 → 갱신·월간 재검증 실행에서 부분 갱신.
시드 규칙(4.4): 1절·2절의 원문 정의·질문, 소속 대분류, 원문 주석(2절의 "> 원문 주석:" 인용 블록. 예: 7. 화물·재고·자산 식별과 추적의 EPCIS 언급, 6. 지도·공간·위치 모델의 지도 버전 관리 포함 주석, 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈의 구분, 27. AI·학습·적응과 모델 운영의 교차 적용 주석)만 넣고, 3~11절은 제목만 두고 "아직 작성되지 않음"으로 표시한다. status 는 seed.
분량: 3~11절의 본문 글자 수(공백 포함, 표 구분 기호·각주 정의·프런트매터 제외)를 4,000자 이내로 한다. 넘치면 주제 페이지(docs/topics/)로 분리하고 이 페이지에서는 링크한다.
갱신 규칙: 갱신 실행에서는 기존 본문 중 유지할 부분과 바꿀 부분을 정하고, 브리프에 없는 새 사실을 더하지 않는다. 조건부 승인의 수정 목록은 모두 반영한다. 변경 요약은 pages.json 의 diff_summary 와 changelog_entry 로 내고(12절 최근 업데이트는 퍼블리셔가 채운다) version 을 올린다.
절 제목: 아래 13개 H2 문자열은 사양서 5.4 문구 그대로(괄호 설명 포함)이며 pipeline/checks/protect_source.py 의 AREA_SECTIONS 와 글자 단위로 같다. 괄호까지 포함해 그대로 쓴다. 다르면 "섹션 제목·순서 불일치"로 반려된다.

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 SCM·로봇·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "7. 화물·재고·자산 식별과 추적", "B. 공통 정보·환경 모델". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_SCM_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다. 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 12장의 1~10번에 대응한다(ref-001 ASCM SCOR, ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 9장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 재고정책 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: 27. AI·학습·적응과 모델 운영의 AI는 매뉴얼 해석은 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전, 도면 해석은 6. 지도·공간·위치 모델, 학습 기반 배차는 13. 작업 배정 — MRTA, 장애 분석은 19. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 27. AI·학습·적응과 모델 운영 페이지와 적용 대상 영역 페이지 양쪽에 연결한다. 8. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.

[경로 규약] 대분류 폴더와 세부영역 파일. 같은 대분류 안의 세부영역은 파일명만으로, 다른 대분류의 세부영역은 ../<대분류 slug>/<파일>로 링크한다. 홈은 ../../index.md, 열린 질문은 ../../open-questions.md, 흐름 매트릭스는 ../../flow-matrix.md, 용어집은 ../../glossary/<slug>.md, 참고문헌은 ../../references/ref-NNN.md, 표준 목록은 ../../standards/index.md, 주제 페이지는 ../../topics/YYYY/YYYY-MM-DD-slug.md, 트랙 개요는 ../../tracks/manual-capability-ontology/index.md 이다.
| 대분류 | 핵심 질문 | 폴더 (docs/categories/ 아래, index.md 가 대분류 페이지) |
|-|-|-|
| A. 업무·공급망 설계 | 무슨 일을 왜, 얼마나 해야 하는가? | a-business-supply-chain-design/ |
| B. 공통 정보·환경 모델 | 로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? | b-common-information-and-environment-model/ |
| C. 연결·실행 기반 | 계획한 작업을 실제 장비가 확실하게 수행하게 하려면? | c-connectivity-and-execution-foundation/ |
| D. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? | d-planning-and-optimization/ |
| E. 협업·현장 운영 | 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? | e-collaboration-and-field-operations/ |
| F. 도입·검증·유지관리 | 새 현장에 설치하고, 변경하면서, 오래 운영하려면? | f-deployment-verification-and-maintenance/ |
| G. 안전·보안·지능·거버넌스 | 전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? | g-safety-security-intelligence-and-governance/ |

| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 주문·업무 시스템 연계 | A. 업무·공급망 설계 | a-business-supply-chain-design/01-order-and-business-system-integration.md |
| 2 | 2. 공정·워크플로 모델링 | A. 업무·공급망 설계 | a-business-supply-chain-design/02-process-and-workflow-modeling.md |
| 3 | 3. 처리능력·거점·설비 계획 | A. 업무·공급망 설계 | a-business-supply-chain-design/03-capacity-site-and-facility-planning.md |
| 4 | 4. 성과·경제성·프로세스 개선 | A. 업무·공급망 설계 | a-business-supply-chain-design/04-performance-economics-and-process-improvement.md |
| 5 | 5. 로봇 능력·작업 온톨로지 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md |
| 6 | 6. 지도·공간·위치 모델 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/06-map-space-and-location-model.md |
| 7 | 7. 화물·재고·자산 식별과 추적 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md |
| 8 | 8. 실시간 세계 상태·데이터 일관성 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md |
| 9 | 9. 로봇·제조사 관제 연동 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md |
| 10 | 10. 설비·건물 시스템 연동 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md |
| 11 | 11. 분산 시스템·통신·컴퓨팅 구조 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md |
| 12 | 12. 명령·작업 실행의 신뢰성 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md |
| 13 | 13. 작업 배정 — MRTA | D. 계획·최적화 | d-planning-and-optimization/13-task-allocation-mrta.md |
| 14 | 14. 작업 순서·스케줄링 | D. 계획·최적화 | d-planning-and-optimization/14-task-sequencing-and-scheduling.md |
| 15 | 15. 다중 로봇 경로·교통 관리 — MAPF | D. 계획·최적화 | d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md |
| 16 | 16. 공용 자원·충전·에너지 최적화 | D. 계획·최적화 | d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md |
| 17 | 17. 로봇 간 협업·물리적 인계 | E. 협업·현장 운영 | e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md |
| 18 | 18. 사람–로봇 협업·운영 인터페이스 | E. 협업·현장 운영 | e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md |
| 19 | 19. 모니터링·이상 탐지·원인 분석 | E. 협업·현장 운영 | e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md |
| 20 | 20. 예외 복구·재계획·업무 연속성 | E. 협업·현장 운영 | e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md |
| 21 | 21. 온보딩·설정·현장 시운전 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md |
| 22 | 22. 시뮬레이션·예측용 디지털 트윈 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md |
| 23 | 23. 시험·형식 검증·벤치마크 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md |
| 24 | 24. 자산·소프트웨어 수명주기 관리 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md |
| 25 | 25. 안전·위험 관리 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md |
| 26 | 26. 사이버보안·접근권한·개인정보 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md |
| 27 | 27. AI·학습·적응과 모델 운영 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md |
| 28 | 28. 표준·상호운용성·다사업자 거버넌스 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md |
-->
[홈](../../index.md) › [{{category}}](index.md) › {{area_no}}. {{area_name}}

# {{area_no}}. {{area_name}}

!!! info "소속 대분류"
    [{{category}}](index.md) — 핵심 질문:
    {{category_core_question}} [분류원문]
<!-- 4.8: 세부영역 페이지 상단에 소속 대분류와 핵심 질문을 노출한다. 시드 28페이지(예: docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)·agents/storyteller.md 4.2·agents/verifier.md 11절 항목 3·부록 C 와 같은 세 줄 admonition 블록이다.
1줄: !!! info "소속 대분류"
2줄: 공백 4칸 + 대분류 링크 + " — 핵심 질문:" (콜론에서 줄이 끝난다. 콜론 뒤에 공백을 두지 않는다)
3줄: 공백 4칸 + 분류 원문 1장 표의 핵심 질문 문장 그대로(위 경로 규약의 대분류 표 참고) + " [분류원문]"
예(B. 공통 정보·환경 모델):
!!! info "소속 대분류"
    [B. 공통 정보·환경 모델](index.md) — 핵심 질문:
    로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? [분류원문]
3줄은 태그를 뗀 문자열이 분류 원문 표 셀 하나와 글자 단위로 같아야 퍼블리셔 원문 보호 검사(protect_source.py 의 check_area·check_tagged_lines)를 통과한다. 링크와 핵심 질문을 한 줄에 합치면 태그 줄이 원문 셀과 달라져 반려된다. 갱신 실행에서는 입력으로 받은 시드의 이 세 줄을 들여쓰기·줄바꿈 위치까지 한 글자도 바꾸지 않고 그대로 둔다. 2차 검증(verifier.md 항목 3·부록 C)은 이 블록을 입력 시드와 줄바꿈까지 글자 단위로 대조하며, 한 줄로 합치거나 "**소속 대분류:** …" 단락으로 바꾸면 [분류원문] 훼손으로 불통과된다. -->

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->
<!-- "관련 연구 트랙" 안내. 퍼블리셔가 config/tracks/*.yaml 의 primary_area·related_areas·idea_areas 에서 만든다(연결된 트랙이 없으면 빈 영역). 시드 28페이지 모두 admonition 블록 바로 아래에 이 마커가 있다. 마커를 지우거나 옮기지 않는다. -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->
<!-- 페이지 상태 줄은 손으로 쓰지 않는다. 상태의 단일 원천은 프런트매터(status·confidence·version·updated·last_run)이며, 퍼블리셔가 이 마커 안에 "> 페이지 상태: … · 신뢰도: … · 페이지 버전: … · 마지막 갱신: … · 마지막 실행: …" 한 줄을 만든다. 마커 밖에 "페이지 상태:" 나 "> 상태: draft …" 같은 줄을 쓰면 check_frontmatter 가 반려한다. 시드 세부영역에는 이 마커가 없으며, 영역 심화 실행에서 area-tracks 마커 아래(1절 제목 위)에 빈 마커 두 줄을 넣는다. 새 시드를 이 템플릿으로 만들 때는 이 마커를 지운다. -->

## 1. 한 줄 정의

{{definition}} [분류원문]
<!--
분류 원문 표의 "무엇을 연구하는가" 칸 문장을 한 글자도 바꾸지 않고 옮기고 끝에 " [분류원문]" 을 붙인다. 예: "제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 [분류원문]".
이 절의 첫 내용 줄은 정의 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 태그 뒤에 각주나 다른 글자를 붙이지 않고, 이 절에는 다른 문장을 두지 않는다. 원문 주석은 이 절이 아니라 2절의 인용 블록에 둔다.
이 절의 문장은 에이전트가 수정하지 않는다. 퍼블리셔(pipeline/checks/protect_source.py check_area)가 _source/ 원문과 글자 단위로 대조한다.
-->

## 2. SCM 관점의 질문

{{scm_question}} [분류원문]

> 원문 주석: {{source_note_paragraph}} [분류원문]

{{source_note_footnote_sentence}}
<!--
첫 내용 줄은 분류 원문 표의 "SCM 관점의 질문" 칸 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 예: "로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? [분류원문]". 수정 금지.
원문 주석: 분류 원문에서 이 세부영역을 "N번"으로 명시해 언급하는 표 아래 문단이 있는 영역(5. 로봇 능력·작업 온톨로지, 6. 지도·공간·위치 모델, 7. 화물·재고·자산 식별과 추적, 8. 실시간 세계 상태·데이터 일관성, 13. 작업 배정 — MRTA, 17. 로봇 간 협업·물리적 인계, 19. 모니터링·이상 탐지·원인 분석, 21. 온보딩·설정·현장 시운전, 22. 시뮬레이션·예측용 디지털 트윈, 27. AI·학습·적응과 모델 운영. 예: 7. 화물·재고·자산 식별과 추적의 EPCIS 언급, 6. 지도·공간·위치 모델의 지도 버전 관리 포함 주석, 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈의 구분, 27. AI·학습·적응과 모델 운영의 교차 적용 주석)은 문단마다 이 절 안에 "> 원문 주석: <문단 그대로> [분류원문]" 인용 블록 하나를 둔다. 굵게 표기와 원문의 [n] 번호를 그대로 두고, 인용 블록은 " [분류원문]" 으로 끝나야 하며 그 뒤에 각주를 붙이지 않는다. 한 문단이 여러 영역을 언급하면 각 영역 페이지에 같은 인용 블록을 둔다(27. AI·학습·적응과 모델 운영의 교차 규칙 문단은 5. 로봇 능력·작업 온톨로지, 6. 지도·공간·위치 모델, 13. 작업 배정 — MRTA, 19. 모니터링·이상 탐지·원인 분석, 21. 온보딩·설정·현장 시운전, 27. AI·학습·적응과 모델 운영 페이지에 둔다). 문단이 둘인 영역(6. 지도·공간·위치 모델)은 인용 블록도 둘이다. 원문 주석이 없는 영역은 인용 블록 줄과 각주 문장 줄을 지운다.
각주: 원문의 [n] 에 대응하는 참고문헌 각주는 인용 블록 밖의 별도 문장에 둔다. 예: "원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]". 각주 정의는 13절에 둔다. [n] 이 없는 주석이면 각주 문장 줄을 지운다.
퍼블리셔(pipeline/checks/protect_source.py check_area)가 이 절의 첫 줄과 "> 원문 주석:" 인용 블록 목록을 _source/ 원문과 글자 단위로 대조한다. 인용 블록이 1절에 있거나, "원문 주석: "으로 시작하지 않거나, 태그 뒤에 각주가 붙으면 "원문 주석 인용 불일치"로 반려된다.
-->

## 3. 왜 중요한가

{{why_it_matters}}
<!--
2~4개의 짧은 단락. 이 영역이 없으면 공급망 운영에서 무엇이 막히는지, 로봇 개별 성능과 공급망 전체 성과가 어떻게 갈리는지를 쓴다. 2절의 SCM 관점 질문에서 출발한다.
주장마다 태그와 각주를 붙인다. 근거가 브리프에 없으면 [의견]으로 쓰거나 쓰지 않는다. 사례·수치는 출처가 있을 때만 쓴다.
-->

## 4. 핵심 개념과 용어

{{key_concepts}}
<!--
형식: "- **용어(영문)** — 한 줄 설명. [태그][^ref]" 목록. 3~8개.
약어는 첫 등장 시 풀어 쓴다. 예: "WES(Warehouse Execution System, 창고 실행 시스템)". 용어집에 있는 용어는 ../../glossary/<slug>.md 로 링크한다. 새 용어는 pages.json 의 glossary_updates 로도 낸다.
-->

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** {{flow_steps}}
<!-- 분류 원문 11장의 흐름 "입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품" 중 이 시나리오가 놓이는 단계를 이름으로 명시한다. 예: "피킹 → 포장". 여러 단계에 걸치면 모두 적는다. -->

**시나리오:** {{scenario_title}}
<!-- 한 현장의 구체적 작업 하나를 제목으로 쓴다. 예: "피킹한 박스를 포장대로 운반". -->

| 항목 | 내용 |
|---|---|
| 시작 조건 | {{trigger}} |
| 작업 대상 | {{object}} |
| 수행 자원 | {{resources}} |
| 제약 | {{constraints}} |
| 완료·인계 | {{completion_handover}} |
| 예외·성과 | {{exception_performance}} |

{{scenario_narrative}}
<!--
여섯 항목은 분류 원문 11장의 정의를 따른다. 시작 조건: 어떤 주문·재고·설비 이벤트가 작업을 발생시키는가 / 작업 대상: 어떤 화물·운반구를 다루는가 / 수행 자원: 로봇·사람·설비 중 누가 어떤 부분을 맡는가 / 제약: 납기·공간·적재량·설비·권한 제약은 무엇인가 / 완료·인계: 무엇이 확인돼야 업무 완료와 재고 변경을 인정하는가 / 예외·성과: 실패하면 누가 복구하며, 처리량·시간·비용에 어떤 영향을 주는가.
표 아래에 1~3단락으로 시나리오를 서술한다. 이 영역이 여섯 항목 중 어디에 관여하는지가 드러나야 한다. 지어낸 현장 수치는 쓰지 않는다(설명용 가상 시나리오임을 첫 문장에 밝힌다. 예: "다음은 설명을 위한 가상의 시나리오이다.").
다룬 칸(단계 × 항목)은 pages.json 의 flow_matrix_updates 로 함께 낸다. 흐름 매트릭스 페이지: ../../flow-matrix.md
-->

## 6. 대표 접근법과 기술

{{approaches}}
<!--
소제목(###)별로 접근법을 2~5개 정리한다. 각 접근법: 무엇을 해결하는가, 어떻게 동작하는가, 한계는 무엇인가. 주장마다 태그·각주.
벤더 제품의 기능·성능은 [추정]에 "벤더 주장"을 병기한다. 표·그림은 복제하지 않고 필요하면 mermaid 로 직접 그린다.
-->

## 7. 관련 표준·프레임워크·오픈소스

{{standards}}
<!--
표 형식: | 이름 | 유형(표준 / 오픈소스 / 평가 프로그램 / 프레임워크) | 이 영역과의 관계 | 출처 |. 각 행의 출처 칸에 각주.
표준·규격은 발행 기관의 공식 자료를 근거로 하고, 원문을 못 열었으면 "원문 미열람"을 표기한다. 대체·개정된 표준은 현재 버전을 확인해 기준일을 쓴다. 표준 목록 페이지(../../standards/index.md)와 용어집 링크를 함께 둔다.
-->

## 8. 대표 연구와 자료

{{key_research}}
<!--
목록 형식: "- 저자 또는 기관, 제목(연도) — 한두 문장 요약과 이 영역에서의 의미. [태그][^ref]". 3~8건. 학술 논문·표준·정부·연구기관 보고서를 우선하고 기사·벤더 문서는 보조로 둔다.
-->

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| {{boundary_row}} | {{owned}} | {{external}} |

{{boundary_note}}
<!--
분류 원문 9장의 다섯 경계(상위 업무 시스템 / 로봇 자체 지능·제어 / 시설·설비 제어 / 거점 간 운송 / 업종별 조건) 중 이 영역에 해당하는 행만 골라 채운다(최소 1행). 이 표는 위키의 열 이름과 영역에 맞게 고쳐 쓴 셀을 섞은 합성 표이므로 행 끝에 [분류원문] 을 붙이지 않는다(원문의 줄도 셀도 아닌 문장에 태그가 붙으면 태그 줄 원문 대조에 실패한다). 원문 9장 표를 열 이름·셀까지 그대로 옮길 때만 표 아래 빈 줄 다음에 [분류원문] 한 줄을 두고, 영역에 맞게 고쳐 쓴 행·문장에는 태그를 붙이지 않고 주장에 [사실]/[추정]/[의견]과 각주를 붙인다. 원문 셀 문구를 인용할 때는 문장 안에 따옴표로 인용하고 범위 경계 페이지(../../about/scope-boundary.md)로 링크한다.
표 아래 1~2단락: 경계가 제품 전략에 따라 이동할 수 있다는 점과, 이 영역에서 이종 제조사를 연결하는 ROP가 어디까지를 인터페이스와 실행 보장으로 맡는지를 쓴다. 외부 연계 영역을 ROP 직접 범위처럼 서술하지 않는다. 범위 경계 페이지: ../../about/scope-boundary.md
-->

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

{{connections}}
<!--
목록 형식: "- [8. 실시간 세계 상태·데이터 일관성](08-real-time-world-state-and-data-consistency.md) — 연결 이유 한 문장". 다른 대분류의 영역은 ../<대분류 slug>/<파일>.md 로 링크한다(경로 규약 표 참고).
반드시 번호와 이름을 함께 쓴다. 여기에 적은 번호를 프런트매터 related_areas 에 넣는다.
교차 규칙: AI를 다루면 27. AI·학습·적응과 모델 운영을 연결한다. 8. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. 트랙과 관련된 영역이면 트랙 개요(../../tracks/manual-capability-ontology/index.md)도 연결한다.
-->

## 11. 열린 질문

{{open_questions}}
<!--
목록 형식: "- **oq-012** (상태: 열림 | 조사 중 | 해결 | 보류 · 제기 2026-09-25 · 실행 2026-09-25-01) 질문 문장". 해결된 질문은 답이 실린 페이지 링크를 덧붙인다.
새 질문·해결된 질문은 pages.json 의 open_question_updates 로도 낸다. 전체 목록: ../../open-questions.md
트랙 전용 질문(q1-01 형식)은 여기에 두지 않고 트랙 백로그(../../tracks/manual-capability-ontology/question-backlog.md)로 링크만 둔다.
출처가 충돌한 주장, 확인하지 못한 수치, "분류 확장 제안"은 여기에 질문으로 올린다.
-->

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:area-recent:end -->
<!-- 퍼블리셔가 이 영역을 다룬 실행과 주제 페이지를 최신순으로 넣는다(날짜 | 실행 id | 변경 요약 | 페이지 링크). 스토리텔러는 마커 사이를 건드리지 않는다. -->

## 13. 참고 자료 (각주)

{{footnotes}}
<!--
각주 정의만 둔다. 형식: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"(공통 규칙 9). 본문에서 쓴 각주는 모두 여기에 정의하고, 정의만 있고 본문에 없는 각주는 지운다. 프런트매터 sources 와 일치시킨다.
시드 페이지는 2절 원문 주석의 [n] 에 대응하는 각주 정의만 둔다(없으면 "아직 작성되지 않음"). 각주 정의는 이 절에만 두고 [분류원문] 이 붙은 줄에는 붙이지 않는다.
-->
```

### templates/category.md

```markdown
---
title: "{{category}}"                       # 원문 명칭 그대로. 예: "B. 공통 정보·환경 모델"
type: category
category: "{{category}}"                    # title 과 같은 값
tags: [{{tags}}]                            # 선택. 없으면 []
status: {{status}}                          # seed | published. 시드 대분류 페이지는 seed 이며, "다른 대분류와의 연결"이 채워져 게시되면 published 로 바꾼다 [가정]
created: {{created}}                        # YYYY-MM-DD
updated: {{updated}}                        # YYYY-MM-DD
sources: [{{sources}}]                      # 원문 주석의 [n] 에 대응하는 참고문헌 id. 예: [ref-003]
version: {{version}}                        # 정수
---
<!--
[템플릿] 대분류 페이지 (type: category)
경로: docs/categories/<대분류 slug>/index.md
쓰임: 구축 시 원문 부분(핵심 질문·개요·세부 연구영역·이 대분류의 핵심 포인트)을 채워 만든다. "다른 대분류와의 연결"은 에이전트(스토리텔러)가 관련 영역을 다루는 실행에서 채우고, "세부 연구영역" 표(페이지·현재 상태 열 포함)와 "최근 업데이트"는 퍼블리셔가 자동 갱신한다.
여섯 섹션(4.3): 핵심 질문 / 개요 / 세부 연구영역 / 이 대분류의 핵심 포인트 / 다른 대분류와의 연결 / 최근 업데이트. 제목·순서 고정. H2 문자열은 사양서 4.3 문구 그대로이며 번호를 붙이지 않는다(pipeline/checks/protect_source.py 의 CATEGORY_SECTIONS 와 글자 단위로 같다. "1. 핵심 질문"처럼 번호를 붙이면 "섹션 제목·순서 불일치"로 반려된다). 각주 정의를 둘 자리로 번호 없는 "참고 자료" 절을 여섯 섹션 뒤에 하나 더 두었다. 이 절은 사양서 4.3 의 여섯 섹션에 없는 구축자 추가 절이다 [가정].

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 SCM·로봇·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "7. 화물·재고·자산 식별과 추적", "B. 공통 정보·환경 모델". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_SCM_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다. 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 12장의 1~10번에 대응한다(ref-001 ASCM SCOR, ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 9장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 재고정책 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: 27. AI·학습·적응과 모델 운영의 AI는 매뉴얼 해석은 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전, 도면 해석은 6. 지도·공간·위치 모델, 학습 기반 배차는 13. 작업 배정 — MRTA, 장애 분석은 19. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 27. AI·학습·적응과 모델 운영 페이지와 적용 대상 영역 페이지 양쪽에 연결한다. 8. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.

[경로 규약] 이 페이지에서 홈은 ../../index.md, 같은 대분류의 세부영역은 <파일>.md, 다른 대분류는 ../<대분류 slug>/index.md 이다.
| 대분류 | 핵심 질문 | 폴더 (docs/categories/ 아래, index.md 가 대분류 페이지) |
|-|-|-|
| A. 업무·공급망 설계 | 무슨 일을 왜, 얼마나 해야 하는가? | a-business-supply-chain-design/ |
| B. 공통 정보·환경 모델 | 로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? | b-common-information-and-environment-model/ |
| C. 연결·실행 기반 | 계획한 작업을 실제 장비가 확실하게 수행하게 하려면? | c-connectivity-and-execution-foundation/ |
| D. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? | d-planning-and-optimization/ |
| E. 협업·현장 운영 | 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? | e-collaboration-and-field-operations/ |
| F. 도입·검증·유지관리 | 새 현장에 설치하고, 변경하면서, 오래 운영하려면? | f-deployment-verification-and-maintenance/ |
| G. 안전·보안·지능·거버넌스 | 전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? | g-safety-security-intelligence-and-governance/ |

| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 주문·업무 시스템 연계 | A. 업무·공급망 설계 | a-business-supply-chain-design/01-order-and-business-system-integration.md |
| 2 | 2. 공정·워크플로 모델링 | A. 업무·공급망 설계 | a-business-supply-chain-design/02-process-and-workflow-modeling.md |
| 3 | 3. 처리능력·거점·설비 계획 | A. 업무·공급망 설계 | a-business-supply-chain-design/03-capacity-site-and-facility-planning.md |
| 4 | 4. 성과·경제성·프로세스 개선 | A. 업무·공급망 설계 | a-business-supply-chain-design/04-performance-economics-and-process-improvement.md |
| 5 | 5. 로봇 능력·작업 온톨로지 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md |
| 6 | 6. 지도·공간·위치 모델 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/06-map-space-and-location-model.md |
| 7 | 7. 화물·재고·자산 식별과 추적 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md |
| 8 | 8. 실시간 세계 상태·데이터 일관성 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md |
| 9 | 9. 로봇·제조사 관제 연동 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md |
| 10 | 10. 설비·건물 시스템 연동 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md |
| 11 | 11. 분산 시스템·통신·컴퓨팅 구조 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md |
| 12 | 12. 명령·작업 실행의 신뢰성 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md |
| 13 | 13. 작업 배정 — MRTA | D. 계획·최적화 | d-planning-and-optimization/13-task-allocation-mrta.md |
| 14 | 14. 작업 순서·스케줄링 | D. 계획·최적화 | d-planning-and-optimization/14-task-sequencing-and-scheduling.md |
| 15 | 15. 다중 로봇 경로·교통 관리 — MAPF | D. 계획·최적화 | d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md |
| 16 | 16. 공용 자원·충전·에너지 최적화 | D. 계획·최적화 | d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md |
| 17 | 17. 로봇 간 협업·물리적 인계 | E. 협업·현장 운영 | e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md |
| 18 | 18. 사람–로봇 협업·운영 인터페이스 | E. 협업·현장 운영 | e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md |
| 19 | 19. 모니터링·이상 탐지·원인 분석 | E. 협업·현장 운영 | e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md |
| 20 | 20. 예외 복구·재계획·업무 연속성 | E. 협업·현장 운영 | e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md |
| 21 | 21. 온보딩·설정·현장 시운전 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md |
| 22 | 22. 시뮬레이션·예측용 디지털 트윈 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md |
| 23 | 23. 시험·형식 검증·벤치마크 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md |
| 24 | 24. 자산·소프트웨어 수명주기 관리 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md |
| 25 | 25. 안전·위험 관리 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md |
| 26 | 26. 사이버보안·접근권한·개인정보 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md |
| 27 | 27. AI·학습·적응과 모델 운영 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md |
| 28 | 28. 표준·상호운용성·다사업자 거버넌스 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md |
-->
[홈](../../index.md) › {{category}}

# {{category}}

## 핵심 질문

{{core_question}} [분류원문]
<!-- 분류 원문 1장 표의 "핵심 질문" 칸 문장 그대로. 예: "로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? [분류원문]". 수정 금지. -->

## 개요

{{overview_paragraph}} [분류원문]
<!-- 분류 원문에서 이 대분류 장의 첫 문단(표 위의 문단)을 굵게 표기까지 그대로 옮긴다. 예: "**로봇, 물건, 공간, 상태를 어떻게 같은 의미로 이해할 것인가**를 연구한다. 매뉴얼 온톨로지와 건축 도면 기반 지도가 주로 이 영역에 들어간다. [분류원문]". G. 안전·보안·지능·거버넌스처럼 첫 문단에 굵은 표기가 없는 장도 그대로 옮긴다. -->

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·SCM 관점의 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{scm_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{scm_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{scm_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{scm_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |

[분류원문]
<!-- auto:category-area-table:end -->
<!--
원문 표 4행을 그대로 옮기고(앞 3열은 원문 셀과 글자 단위로 같게, 첫 열의 굵은 표기 유지, 첫 열에 링크를 씌우지 않음), "페이지" 열에 세부영역 페이지 링크, "현재 상태" 열에 해당 페이지 프런트매터 status(seed | draft | verified | published | needs_update | deprecated)를 둔다(4.3 의 "링크와 현재 상태 열만 추가"). 표 바로 아래 빈 줄 다음에 [분류원문] 한 줄을 둔다. 퍼블리셔(pipeline/checks/protect_source.py check_category)가 각 행의 앞 3칸과 [분류원문] 줄을 원문과 대조한다.
표 전체는 auto:category-area-table 마커 안에 있고 퍼블리셔(pipeline/lib/render.py render_category_area_table)가 원문 파서와 세부영역 페이지의 status 로 다시 쓴다. 스토리텔러는 마커 사이를 건드리지 않는다. 마커 위의 안내 문장은 마커 밖이므로 그대로 둔다. 이 key 는 사양서에 없는 구축자 추가 key 이며, 시드 대분류 페이지·agents/shared-rules.md 6절의 auto key 목록·퍼블리셔(pipeline/lib/autoregion.py AUTO_KEYS)가 같은 값을 쓴다 [가정 — 사용자 결정 항목: 표 전체를 자동 영역으로 둘지, 표는 마커 밖에 두고 현재 상태 열만 갱신할지].
-->

## 이 대분류의 핵심 포인트

{{key_point_paragraphs}}
<!--
분류 원문에서 이 대분류 장의 표 아래 설명 문단들을 순서대로 모두 옮긴다. 문단마다 끝에 " [분류원문]" 을 붙이고, 그 줄에는 태그 뒤에 아무것도(각주 포함) 붙이지 않는다. 원문의 [n] 번호 표기는 문장 안에 그대로 둔다. 예: "... 참고 표준이다. [3] [분류원문]". 대응 각주 [^ref-00n] 은 이 절이 아니라 "참고 자료" 절의 별도 문장에 둔다. 굵게·기울임 표기를 유지한다. 에이전트는 이 절의 원문 문장을 고치지 않고, 원문 문단 뒤에 자기 문장을 덧붙이지도 않는다.
퍼블리셔(pipeline/checks/protect_source.py check_category)는 이 절에서 " [분류원문]" 으로 끝나는 줄만 모아 원문 문단 목록과 글자 단위로 대조한다. 태그 뒤에 각주를 붙이면 그 줄이 빠져 "핵심 포인트 문단 불일치"로 반려된다.
-->

## 다른 대분류와의 연결

{{category_connections}}
<!--
에이전트가 채운다. 목록 형식: "- [C. 연결·실행 기반](../c-connectivity-and-execution-foundation/index.md) — 이 대분류의 어떤 영역이 저 대분류의 어떤 영역과 왜 이어지는지 한두 문장(세부영역은 번호와 이름 함께)". 주장에는 태그·각주. 구축 시에는 "아직 작성되지 않음"으로 둔다.
G. 안전·보안·지능·거버넌스는 나머지 여섯 대분류 전체에 적용된다는 원문 취지를 반영한다. 27. AI·학습·적응과 모델 운영의 교차 규칙(매뉴얼 해석은 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전, 도면 해석은 6. 지도·공간·위치 모델, 학습 기반 배차는 13. 작업 배정 — MRTA, 장애 분석은 19. 모니터링·이상 탐지·원인 분석)을 여기서도 지킨다.
-->

## 최근 업데이트

<!-- auto:category-recent:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:category-recent:end -->
<!-- 퍼블리셔가 이 대분류에 속한 세부영역·주제 페이지의 최근 변경을 최신순으로 넣는다(날짜 | 실행 id | 페이지 | 변경 요약). 마커 사이는 스토리텔러가 건드리지 않는다. -->

## 참고 자료

{{source_footnote_sentences}}

{{footnotes}}
<!-- "이 대분류의 핵심 포인트" 원문 문단의 [n] 에 대응하는 각주를 별도 문장으로 두고(예: "원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]"), 그 아래에 각주 정의를 둔다. 형식: "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD". "다른 대분류와의 연결"에서 쓴 각주도 여기에 둔다. 각주가 없으면 "없음". 이 절은 사양서 4.3 의 여섯 섹션 밖의 보조 절로, 5.3 의 각주 정의 자리를 위해 구축자가 추가했으며 번호를 붙이지 않는다 [가정]. -->
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 468건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 118개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- battery-swapping: 배터리 교환 (Battery Swapping)
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
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformance-test: 적합성 시험 (Conformance Test)
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
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
- fan-out: 팬아웃 (Fan-out (human-robot team))
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
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
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
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
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
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
```

### docs/open-questions.md (요약: 대상 영역 [20] 에 걸린 4건 / 전체 72건)

```markdown
- oq-003 [열림] 로봇·게이트의 바코드·RFID 판독 실패나 오판독이 생기면 인계 확정을 보류·재스캔·사람 확인 중 어떤 기준으로 처리해야 하는가? (영역 7, 20)
- oq-021 [열림] 로봇이 이미 화물을 싣거나 옮긴 뒤 상위 시스템이 주문을 취소·변경하면 되돌림 작업과 재고 반영을 누가 어떤 규칙으로 정하는가(국내 물류센터 사례 포함)? (영역 1, 20)
- oq-038 [열림] 외부망이 끊겨 클라우드 WMS 와 단절된 동안 현장 ROP 가 이미 받은 주문·작업을 어디까지 계속 실행하고, 재연결 뒤 재고·완료 기록을 어떻게 맞추는지 정한 국내 물류센터 운영 기준이나 사례가 있는가? (영역 11, 1, 20)
- oq-048 [열림] Open-RMF 플릿 어댑터 재시작 시 작업 유실을 막는 작업 백업·복원 기능(SQLite 저장 제안)이 현재 배포판에 반영되었는가, 반영되었다면 복원 뒤 로봇의 실제 위치·적재 상태와 어떻게 대조하는가? (영역 12, 20)
```

### docs/standards/index.md

```markdown
---
title: "표준·프레임워크 목록"
type: standard
subtype: index
status: published
created: 2026-09-24
updated: 2026-09-24
version: 3
---

[홈](../index.md) › 표준·프레임워크 목록

# 표준·프레임워크 목록

이 위키가 참조하는 표준·오픈소스·평가 프로그램·프레임워크를 관련 세부영역과 함께 정리한다. 시드 8건은 분류 원문 12장의 참고 자료 가운데 표준·오픈소스·평가 프로그램·프레임워크에 해당하는 항목이며(12장 참고 자료 목록의 다섯째·여섯째 항목인 Li 등 2020, Ma 등 2017 논문은 제외), 각 항목의 출처는 [참고문헌](../references/index.md)의 ref-001 ~ ref-010 에 대응한다. 시드 표는 아래 "시드 목록"에 손으로 두고, 리서치 에이전트가 제안하고 내용 검증 에이전트가 실재와 최신성을 확인한 새 항목은 퍼블리셔가 "추가 항목"의 자동 갱신 영역에 표로 넣는다. [가정]

종류는 네 가지로 나눈다. **표준**은 표준 기관이 제정·관리하는 규격, **오픈소스**는 공개 저장소로 배포되는 소프트웨어와 그 공식 문서, **평가 프로그램**은 연구기관이 운영하는 성능 평가·경진대회, **프레임워크**는 규범적 규격은 아니지만 구조·어휘·설계 관점을 제공하는 참조 모델·설계 문서다. SCOR(Supply Chain Operations Reference)의 종류는 참고문헌 ref-001 의 유형(표준)과 같게 표준으로 두었고, ROS 2(Robot Operating System 2) DDS-Security와 ROS 2 위협 모델은 규격 본문이 아니라 ROS 2 설계 문서이므로 둘 다 프레임워크로 두었다. 이 둘은 구축자의 분류이며 검증 에이전트가 바꿀 수 있다. [가정]

관련 세부영역은 번호와 이름을 함께 쓴다. "원문 12장 요약" 열은 분류 원문 12장의 요약 구절을 그대로 옮긴 것이다. 세부 내용과 근거는 이름 열의 링크(용어집 항목)와 출처 열의 참고문헌 페이지에서 본다.

## 시드 목록

| 이름 | 종류 | 발행 기관 | 관련 세부영역 | 원문 12장 요약 | 출처 |
|---|---|---|---|---|---|
| [SCOR (SCOR Digital Standard)](../glossary/scor.md) | 표준 | ASCM(Association for Supply Chain Management) | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) · [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) · [4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 공급망 프로세스 범위 참고. [분류원문] | [ref-001](../references/ref-001.md)[^ref-001] |
| [ISA-95 (ANSI/ISA-95)](../glossary/isa-95.md) | 표준 | ISA(International Society of Automation) | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) · [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) · [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 기업 업무와 제조 운영·제어의 통합 경계 참고. [분류원문] | [ref-002](../references/ref-002.md)[^ref-002] |
| [GS1 EPCIS](../glossary/epcis.md) | 표준 | GS1 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) · [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) · [17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) | 제품·자산의 상태·위치·이동·인계 이벤트 모델 참고. [분류원문] | [ref-003](../references/ref-003.md)[^ref-003] |
| [Open-RMF](../glossary/open-rmf.md) | 오픈소스 | Open Robotics | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) · [10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) · [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) · [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) | 작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고. [분류원문] | [ref-004](../references/ref-004.md)[^ref-004] |
| [ROS 2 DDS-Security (ROS 2 DDS-Security Integration)](../glossary/dds-security.md) | 프레임워크 | ROS 2 Design | [26. 사이버보안·접근권한·개인정보](../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md) · [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) · [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 인증·암호화·접근통제 구조 참고. [분류원문] | [ref-009](../references/ref-009.md)[^ref-009] |
| ROS 2 위협 모델 (ROS 2 Robotic Systems Threat Model) | 프레임워크 | ROS 2 Design | [26. 사이버보안·접근권한·개인정보](../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md) · [25. 안전·위험 관리](../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) · [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 로봇 시스템의 보안 위협과 대응 설계 참고. [분류원문] | [ref-010](../references/ref-010.md)[^ref-010] |
| NIST 협업 로봇 성능 (Performance of Collaborative Robot Systems) | 평가 프로그램 | NIST(National Institute of Standards and Technology) | [17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) · [18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) · [23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | 사람–로봇 및 이종 로봇 협업 성능 평가 참고. [분류원문] | [ref-007](../references/ref-007.md)[^ref-007] |
| [ARIAC](../glossary/ariac.md) | 평가 프로그램 | NIST | [23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) · [22. 시뮬레이션·예측용 디지털 트윈](../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) · [20. 예외 복구·재계획·업무 연속성](../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | 변화하는 제조 환경에서의 로봇 작업 수행·적응성 평가 참고. [분류원문] | [ref-008](../references/ref-008.md)[^ref-008] |

## 추가 항목

리서치·검증을 거쳐 새로 등록되는 항목은 퍼블리셔가 아래 자동 갱신 영역에 표로 넣는다. 그 표의 열 구성(이름 | 기관 | 종류 | 관련 영역 | 참고문헌 | URL)은 퍼블리셔 렌더러를 따르며, 위의 시드 표는 이 영역 밖에 있어 자동 갱신이 지우지 않는다. [가정]

<!-- auto:standards-table:start -->
| 이름 | 기관 | 종류 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| GS1 EPCIS 2.0 (ISO/IEC 19987:2024) | ISO/IEC · GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-011](../references/ref-011.md) | <https://www.iso.org/standard/85557.html> |
| GS1 CBV (Core Business Vocabulary) | GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-014](../references/ref-014.md) | <https://ref.gs1.org/standards/cbv/> |
| SSCC (Serial Shipping Container Code) | GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-016](../references/ref-016.md) | <https://www.gs1.org/standards/id-keys/sscc> |
| GS1 Logistic Label Guideline | GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-018](../references/ref-018.md) | <https://www.gs1.org/docs/tl/GS1_Logistic_Label_Guideline.pdf> |
| GRAI (Global Returnable Asset Identifier) | GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-019](../references/ref-019.md) | <https://www.gs1.org/standards/id-keys/grai> |
| GIAI (Global Individual Asset Identifier) | GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-020](../references/ref-020.md) | <https://support.gs1.org/support/solutions/articles/43000734294-which-gs1-identification-key-should-be-used-for-individual-assets-used-to-transport-goods-> |
| EPC Tag Data Standard (1.11판) | GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-021](../references/ref-021.md) | <https://www.gs1.org/sites/default/files/docs/epc/GS1_EPC_TDS_i1_11.pdf> |
| VDA 5050 (2.0.0) | VDA(Verband der Automobilindustrie) | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-022](../references/ref-022.md) | <https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf> |
| OpenEPCIS | OpenEPCIS | 오픈소스 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-013](../references/ref-013.md) | <https://openepcis.io/docs/epcis/> |
| IEEE 1872-2015 Standard Ontologies for Robotics and Automation (CORA) | IEEE | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-025](../references/ref-025.md) | <https://ieeexplore.ieee.org/document/7084073/> |
| IEEE 1872.2-2021 Standard for Autonomous Robotics (AuR) Ontology | IEEE | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-026](../references/ref-026.md) | <https://standards.ieee.org/standard/1872_2-2021.html> |
| W3C/OGC Semantic Sensor Network Ontology (SSN/SOSA) | W3C / OGC | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-030](../references/ref-030.md) | <https://www.w3.org/TR/vocab-ssn/> |
| VDA 5050 (3.0.0) | VDA(Verband der Automobilindustrie) | 표준 | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-032](../references/ref-032.md) | <https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN> |
| MassRobotics AMR Interoperability Standard (1.0) | MassRobotics | 표준 | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-033](../references/ref-033.md) | <https://www.massrobotics.org/autonomous-mobile-robot-standards-published-by-massrobotics/> |
| OPC UA for Robotics Part 1: Vertical Integration (OPC 40010-1) | OPC Foundation / VDMA | 표준 | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-034](../references/ref-034.md) | <https://reference.opcfoundation.org/specs/OPC-40010-1> |
| Information Model for Capabilities, Skills & Services (CSS) | Plattform Industrie 4.0 | 프레임워크 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-035](../references/ref-035.md) | <https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html> |
| Oliot EPCIS (GS1 EPCIS/CBV 2.0 오픈소스 구현) | Auto-ID Labs Korea(세종대학교) | 오픈소스 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-050](../references/ref-050.md) | <https://github.com/JaewookByun/epcis> |
| RAWSim-O | Merschformann, M. (RAWSim-O GitHub) | 오픈소스 | [3. 처리능력·거점·설비 계획](../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[22. 시뮬레이션·예측용 디지털 트윈](../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) | [ref-101](../references/ref-101.md) | <https://github.com/merschformann/RAWSim-O> |
| 스마트물류센터 인증제 | 한국교통연구원(인증스마트물류센터) | 평가 프로그램 | [3. 처리능력·거점·설비 계획](../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | [ref-106](../references/ref-106.md) | <https://cslc.koti.re.kr/> |
| BPMN 2.0 (ISO/IEC 19510:2013) | OMG(Object Management Group) · ISO/IEC | 표준 | [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | [ref-112](../references/ref-112.md) | <https://www.omg.org/spec/BPMN/2.0/About-BPMN> |
| IEC 62264-3:2016 (ISA-95 Part 3) 제조 운영 관리 활동 모델 | IEC / ISO | 표준 | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) | [ref-119](../references/ref-119.md) | <https://www.iso.org/standard/67480.html> |
| B2MML (Business To Manufacturing Markup Language, 판 0701) | MESA International | 표준 | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) | [ref-117](../references/ref-117.md) | <https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd> |
| OCEL 2.0 (Object-Centric Event Log) | arXiv:2403.01975 저자(미확인) | 표준 | [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[19. 모니터링·이상 탐지·원인 분석](../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) | [ref-122](../references/ref-122.md) | <https://arxiv.org/abs/2403.01975> |
| ISO 22400-2:2014 제조 운영 관리 KPI 정의 | ISO | 표준 | [4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | [ref-139](../references/ref-139.md) | <https://www.iso.org/standard/54497.html> |
| WERC DC Measures | WERC(Warehousing Education and Research Council) | 평가 프로그램 | [4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | [ref-141](../references/ref-141.md) | <https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf> |
| PM4Py | Process Intelligence Solutions | 오픈소스 | [4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[19. 모니터링·이상 탐지·원인 분석](../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) | [ref-147](../references/ref-147.md) | <https://github.com/process-intelligence-solutions/pm4py> |
| OPC UA for ISA-95 Part 4: Job Control (OPC 10031-4, 노드셋 2.0.0) | OPC Foundation / ISA | 표준 | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-130](../references/ref-130.md) | <https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL> |
| osmAG-from-cad (CAD-to-osmAG 파이프라인) | Zhang, J. (jiajiezhang7 GitHub) | 오픈소스 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | [ref-084](../references/ref-084.md) | <https://github.com/jiajiezhang7/osmAG-from-cad> |
| Ogm2Pgbm | Vega-Torres, M. A. (MigVega GitHub) | 오픈소스 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | [ref-082](../references/ref-082.md) | <https://github.com/MigVega/Ogm2Pgbm> |
| ifc2indoorgml | Diakité, A. A. 외 | 오픈소스 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-225](../references/ref-225.md) | <https://isprs-archives.copernicus.org/articles/XLIII-B4-2022/295/2022/> |
| IDTA 02020 Capability Description 1.0 | IDTA(Industrial Digital Twin Association) | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-229](../references/ref-229.md) | <https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description> |
| IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 | IDTA(Industrial Digital Twin Association) | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-234](../references/ref-234.md) | <https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles> |
| CaSkMan | CaSkade-Automation (GitHub) | 오픈소스 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-231](../references/ref-231.md) | <https://github.com/CaSkade-Automation/CaSkMan> |
| SOMA (Socio-physical Model of Activities) | EASE CRC | 오픈소스 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-233](../references/ref-233.md) | <https://github.com/ease-crc/soma> |
| IEEE 1872.2 AuR 온톨로지 OWL 구현(IndustrialStandard-ODP-IEEE1872-2) | Helmut Schmidt University, Institute of Automation Technology | 오픈소스 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-232](../references/ref-232.md) | <https://github.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2> |
| ISO 22166-201:2024 서비스 로봇 모듈 공통 정보 모델 | ISO | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-240](../references/ref-240.md) | <https://www.iso.org/standard/82334.html> |
| KS B 7321-2 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 국가표준인증통합정보시스템(KSSN) | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-138](../references/ref-138.md) | <https://www.kssn.net/search/stddetail.do?itemNo=K001010147546> |
| VDMA LIF (Layout Interchange Format) | VDMA | 표준 | [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-046](../references/ref-046.md) | <https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format> |
| IFC 4.3 (Industry Foundation Classes, 개발 저장소 ifc4.3-main) | buildingSMART | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-213](../references/ref-213.md) | <https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md> |
| Nav2 Docking Framework (nav2_docking) | ROS Navigation (Open Navigation) | 오픈소스 | [16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)<br>[6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | [ref-216](../references/ref-216.md) | <https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md> |
| IDTA 02020 Capability Description (AAS 서브모델 1.0) | IDTA(Industrial Digital Twin Association) | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-243](../references/ref-243.md) | <https://github.com/admin-shell-io/submodel-templates/blob/main/published/Capability%20Description/1/0/IDTA%2002020_Template_Capability_Description.json> |
| IDTA 02047 Technical Data for Automated Guided Vehicles (1.0) | IDTA(Industrial Digital Twin Association) | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-245](../references/ref-245.md) | <https://github.com/admin-shell-io/submodel-templates/blob/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles/1/0/IDTA%2002047-1-0%20Template_TechnicalDataForAGV.json> |
| AAS Part 3a: Data Specification – IEC 61360 (IDTA-01003-a 3.0.2) | IDTA(Industrial Digital Twin Association) | 표준 | [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-247](../references/ref-247.md) | <https://industrialdigitaltwin.org/wp-content/uploads/2024/07/IDTA-01003-a-3-0-2_SpecificationAssetAdministrationShell_Part3a_DataSpecification_IEC613601.pdf> |
| ISO 22166-202:2025 서비스 로봇 소프트웨어 모듈 정보 모델 | ISO | 표준 | [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-248](../references/ref-248.md) | <https://www.iso.org/standard/84589.html> |
| KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 국가표준인증통합정보시스템(KSSN) | 표준 | [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-138](../references/ref-138.md) | <https://www.kssn.net/search/stddetail.do?itemNo=K001010147546> |
| SkiROS2 | RVMI lab, Aalborg University | 오픈소스 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-250](../references/ref-250.md) | <https://github.com/RVMI/skiros2> |
| LIF (Layout Interchange Format) 1.0.0 | VDMA | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-046](../references/ref-046.md) | <https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format> |
| ISO 21423 Industrial mobile robots — Communications and interoperability | ISO | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-159](../references/ref-159.md) | <https://www.iso.org/standard/86749.html> |
| IFC 4.3 (IfcSpace) | buildingSMART International | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-156](../references/ref-156.md) | <https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md> |
| OGC IndoorGML 2.0 | OGC | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-157](../references/ref-157.md) | <https://github.com/opengeospatial/IndoorGML-SWG> |
| ISO 19164:2024 Indoor feature model | ISO | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-158](../references/ref-158.md) | <https://www.iso.org/standard/83153.html> |
| GS1 GLN (Global Location Number) | GS1 | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-162](../references/ref-162.md) | <https://www.gs1.org/standards/id-keys/gln/physical-location> |
| REP 105 Coordinate Frames for Mobile Platforms | ROS (ros-infrastructure/rep) | 프레임워크 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-155](../references/ref-155.md) | <https://www.ros.org/reps/rep-0105.html> |
| ROSA (ROS Agent) | NASA Jet Propulsion Laboratory | 오픈소스 | [27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)<br>[18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | [ref-171](../references/ref-171.md) | <https://github.com/nasa-jpl/rosa> |
| RAI | Robotec.ai | 오픈소스 | [27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)<br>[18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | [ref-175](../references/ref-175.md) | <https://github.com/RobotecAI/rai> |
| free_fleet (Open-RMF 플릿 어댑터) | Open Robotics (open-rmf) | 오픈소스 | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-256](../references/ref-256.md) | <https://github.com/open-rmf/free_fleet> |
| ros_amr_interop (VDA5050 커넥터·MassRobotics 송신 노드) | InOrbit | 오픈소스 | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-255](../references/ref-255.md) | <https://github.com/inorbit-ai/ros_amr_interop> |
| Open-RMF fleet_adapter_template | Open Robotics (open-rmf) | 오픈소스 | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-105](../references/ref-105.md) | <https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml> |
| SLAM Toolbox | Macenski, S. (SteveMacenski GitHub) | 오픈소스 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[21. 온보딩·설정·현장 시운전](../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) | [ref-270](../references/ref-270.md) | <https://github.com/SteveMacenski/slam_toolbox> |
| ROS 2 QoS 정책 (Deadline·Lifespan·Liveliness, Jazzy 문서) | Open Robotics (ROS 2 Documentation) | 오픈소스 | [8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) | [ref-282](../references/ref-282.md) | <https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html> |
| Eclipse Sparkplug (Chapter 5 Operational Behavior) | Eclipse Foundation | 표준 | [8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[19. 모니터링·이상 탐지·원인 분석](../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) | [ref-287](../references/ref-287.md) | <https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc> |
| OPC UA Part 4: Services (7.11 DataValue) | OPC Foundation | 표준 | [8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) | [ref-288](../references/ref-288.md) | <https://reference.opcfoundation.org/specs/OPC-10000-4/7.11> |
| ISO 23247 제조 디지털 트윈 프레임워크 | ISO (NIST 해설 경유) | 표준 | [8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[22. 시뮬레이션·예측용 디지털 트윈](../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) | [ref-290](../references/ref-290.md) | <https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417> |
| ROS 2 설계 문서 — ROS on DDS · QoS 정책 | ROS 2 Design | 프레임워크 | [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-298](../references/ref-298.md) | <https://design.ros2.org/articles/qos.html> |
| rmw_zenoh (Zenoh 기반 ROS 2 미들웨어) | ROS 2 (ros2/rmw_zenoh) | 오픈소스 | [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-299](../references/ref-299.md) | <https://github.com/ros2/rmw_zenoh> |
| KubeEdge | KubeEdge (CNCF) | 오픈소스 | [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[20. 예외 복구·재계획·업무 연속성](../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | [ref-300](../references/ref-300.md) | <https://github.com/kubeedge/kubeedge> |
| Open-RMF rmf-web (대시보드·API 서버) | Open Robotics (open-rmf) | 오픈소스 | [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-302](../references/ref-302.md) | <https://github.com/open-rmf/rmf-web> |
| MQTT Version 5.0 | OASIS | 표준 | [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-306](../references/ref-306.md) | <https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html> |
| NIST SP 500-325 Fog Computing Conceptual Model | NIST | 프레임워크 | [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) | [ref-303](../references/ref-303.md) | <https://csrc.nist.gov/pubs/sp/500/325/final> |
| KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 산업통상자원부 국가기술표준원 | 표준 | [10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)<br>[25. 안전·위험 관리](../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | [ref-314](../references/ref-314.md) | <https://www.kssn.net/search/stddetail.do?itemNo=K001010135682> |
| Open-RMF 승강기·문 메시지(rmf_internal_msgs의 rmf_lift_msgs·rmf_door_msgs) | Open Robotics (open-rmf) | 오픈소스 | [10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)<br>[12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) | [ref-286](../references/ref-286.md) | <https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg> |
| KnowRob (하이브리드 지식 베이스) | KnowRob (knowrob GitHub) | 오픈소스 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-326](../references/ref-326.md) | <https://github.com/knowrob/knowrob> |
| IEEE1872-owl (CORA 공개 OWL 번역, 제3자) | srfiorini (IEEE1872-owl GitHub) | 오픈소스 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-330](../references/ref-330.md) | <https://github.com/srfiorini/IEEE1872-owl/blob/master/cora-bare.owl> |
| CityGML 3.0 Part 1: Conceptual Model (OGC 20-010) | OGC | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-339](../references/ref-339.md) | <https://docs.ogc.org/is/20-010/20-010.html> |
| IMDF (Indoor Mapping Data Format) 1.0.0 | OGC / Apple | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-338](../references/ref-338.md) | <https://docs.ogc.org/cs/20-094/> |
| BOT (Building Topology Ontology) 0.3.2 | W3C Linked Building Data Community Group | 프레임워크 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-336](../references/ref-336.md) | <https://github.com/w3c-lbd-cg/bot/blob/master/bot.ttl> |
| ifcOWL | buildingSMART | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-342](../references/ref-342.md) | <https://github.com/buildingsmart-community/ifcOWL> |
| Brick Schema | Brick Consortium | 오픈소스 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | [ref-341](../references/ref-341.md) | <https://docs.brickschema.org/brick/relationships.html> |
| ISO 16739-1:2024 (IFC 4.3) | ISO | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-335](../references/ref-335.md) | <https://www.iso.org/standard/84123.html> |
| Rasa 폼(Forms, Rasa 3.x) | Rasa Technologies | 오픈소스 | [18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)<br>[27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) | [ref-356](../references/ref-356.md) | <https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx> |
| ROS 2 액션 설계(Actions) | ROS 2 Design | 프레임워크 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-363](../references/ref-363.md) | <https://design.ros2.org/articles/actions.html> |
| ROS 2 관리형 노드 수명주기(Managed nodes) | ROS 2 Design | 프레임워크 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[24. 자산·소프트웨어 수명주기 관리](../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) | [ref-364](../references/ref-364.md) | <https://design.ros2.org/articles/node_lifecycle.html> |
| Open-RMF rmf_task | Open Robotics (open-rmf) | 오픈소스 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[20. 예외 복구·재계획·업무 연속성](../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | [ref-366](../references/ref-366.md) | <https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp> |
| IETF Idempotency-Key HTTP 헤더 초안(draft-ietf-httpapi-idempotency-key-header) | IETF HTTPAPI Working Group | 표준 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | [ref-367](../references/ref-367.md) | <https://github.com/ietf-wg-httpapi/idempotency/blob/main/draft-ietf-httpapi-idempotency-key-header.md> |
| OPC UA Part 10: Programs (v1.04) | OPC Foundation | 표준 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | [ref-368](../references/ref-368.md) | <https://reference.opcfoundation.org/Core/Part10/v104/docs/4.2.4> |
| ISA-TR88.00.02 Machine and Unit States (PackML) | ISA | 표준 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | [ref-369](../references/ref-369.md) | <https://www.isa.org/products/isa-tr88-00-02-2022-machine-and-unit-states-an-imp> |
| BehaviorTree.CPP | BehaviorTree (GitHub) | 오픈소스 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | [ref-371](../references/ref-371.md) | <https://github.com/BehaviorTree/BehaviorTree.CPP/blob/master/include/behaviortree_cpp/decorators/retry_node.h> |
| OR-Tools CP-SAT (스케줄링 레시피) | Google | 오픈소스 | [14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) | [ref-379](../references/ref-379.md) | <https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md> |
| Open-RMF rmf_task (TaskPlanner·BinaryPriorityScheme) | Open Robotics (open-rmf) | 오픈소스 | [14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) | [ref-377](../references/ref-377.md) | <https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp> |
| rmf_task (Open-RMF 작업 계획기 TaskPlanner) | Open Robotics (open-rmf) | 오픈소스 | [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) | [ref-404](../references/ref-404.md) | <https://github.com/open-rmf/rmf_task> |
| ISO 13567-1:2017 CAD 레이어 구성·명명 — Part 1: 개요와 원칙 | ISO | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-427](../references/ref-427.md) | <https://www.iso.org/standard/70181.html> |
| 미국 국가 CAD 표준(NCS) AIA CAD 레이어 이름 형식(V5, V6 판 있음) | National Institute of Building Sciences | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-428](../references/ref-428.md) | <https://www.nationalcadstandard.org/ncs5/pdfs/ncs5_clg_lnf.pdf> |
| KS F 1542 CAD 도면 작성을 위한 레이어 원칙과 기준 | 국가표준인증통합정보시스템(KSSN) | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-429](../references/ref-429.md) | <https://www.kssn.net/search/stddetail.do?itemNo=K001010129900> |
| 건설CALS/EC 전자도면 작성표준(V1.1, KCCS-0001-2006) | 한국건설기술연구원(건설CALS 체계) | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-430](../references/ref-430.md) | <https://www.calspia.go.kr/portal/intro/introStandard02.do> |
| ezdxf (DXF 읽기·쓰기 라이브러리) | Moitzi, M. (mozman/ezdxf GitHub) | 오픈소스 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | [ref-424](../references/ref-424.md) | <https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/blocks.rst> |
| ECLASS (제품·서비스 분류·속성 사전, Release 15.0·16.0) | ECLASS e.V. | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-185](../references/ref-185.md) | <https://eclass.eu/en/eclass-standard/releases> |
| IEC 공통 데이터 사전(IEC CDD) | IEC | 표준 | [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-183](../references/ref-183.md) | <https://tc3.iec.ch/tc-activity/common-data-dictionary-cdd/> |
| rmf_traffic (Open-RMF 교통 스케줄링·협상 패키지) | Open Robotics (open-rmf) | 오픈소스 | [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-197](../references/ref-197.md) | <https://github.com/open-rmf/rmf_traffic> |
| Open-RMF Traffic Editor | Open Robotics | 오픈소스 | [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[21. 온보딩·설정·현장 시운전](../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) | [ref-079](../references/ref-079.md) | <https://osrf.github.io/ros2multirobotbook/traffic-editor.html> |
| MAPF-LRR2023 (League of Robot Runners 2023 팀 해법 WPPL) | DiligentPanda (Team Pikachu, GitHub) | 오픈소스 | [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | [ref-191](../references/ref-191.md) | <https://github.com/DiligentPanda/MAPF-LRR2023> |
| SEMI E84 Enhanced Carrier Handoff Parallel I/O Interface | SEMI | 표준 | [17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | [ref-202](../references/ref-202.md) | <https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface> |
| ASTM F3499-21 A-UGV 도킹 성능 시험 방법 | ASTM International | 표준 | [17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | [ref-204](../references/ref-204.md) | <https://www.astm.org/f3499-21.html> |
| ANSI/A3 R15.08-2-2023 Industrial Mobile Robots — Safety Requirements — Part 2 | ANSI / A3 | 표준 | [25. 안전·위험 관리](../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md)<br>[17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) | [ref-210](../references/ref-210.md) | <https://webstore.ansi.org/standards/ria/ansia3r15082023> |
| KS B ISO 10218-2 산업용 로봇의 안전 — 제2부: 로봇 시스템 및 통합 | 국가표준인증통합정보시스템(KSSN) | 표준 | [25. 안전·위험 관리](../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md)<br>[17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) | [ref-211](../references/ref-211.md) | <https://www.kssn.net/search/stddetail.do?itemNo=K001010083660> |
| Open-RMF 디스펜서·인제스터 메시지(rmf_internal_msgs의 rmf_dispenser_msgs) | Open Robotics (open-rmf) | 오픈소스 | [17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | [ref-499](../references/ref-499.md) | <https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserResult.msg> |
| Open-RMF rmf_traffic (교통 그래프·뮤텍스 그룹) | Open Robotics (open-rmf) | 오픈소스 | [16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)<br>[15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) | [ref-536](../references/ref-536.md) | <https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp> |
| Open-RMF rmf_reservation (실험적 예약 라이브러리) | Open Robotics (open-rmf) | 오픈소스 | [16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) | [ref-538](../references/ref-538.md) | <https://github.com/open-rmf/rmf_reservation> |
| ISO 3691-4:2023 무인 산업용 트럭과 그 시스템의 안전 요구·검증 | ISO | 표준 | [18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)<br>[25. 안전·위험 관리](../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | [ref-470](../references/ref-470.md) | <https://www.iso.org/standard/83545.html> |
| ISO 10218-1·10218-2:2025 산업용 로봇 안전(협동 적용 통합) | ISO (A3 해설 경유) | 표준 | [18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)<br>[25. 안전·위험 관리](../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | [ref-471](../references/ref-471.md) | <https://www.automate.org/robotics/blogs/updated-iso-10218-faq> |
| ANSI/A3 R15.08-2 산업용 이동로봇 시스템·적용 안전 표준 | A3(Association for Advancing Automation) | 표준 | [18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)<br>[25. 안전·위험 관리](../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | [ref-472](../references/ref-472.md) | <https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available> |
| 고정식·이동식 산업용 로봇의 협동작업 안전 가이드 | 고용노동부·한국산업안전보건공단 | 프레임워크 | [18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)<br>[25. 안전·위험 관리](../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | [ref-473](../references/ref-473.md) | <https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065> |
| 이동식 협동로봇 안전기준 KS(표준 번호 미확인) | 중소벤처기업부 발표(대구 이동식 협동로봇 규제자유특구) | 표준 | [18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)<br>[25. 안전·위험 관리](../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | [ref-475](../references/ref-475.md) | <https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517> |
| Open-RMF rmf_demos | Open Robotics (open-rmf) | 오픈소스 | [18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)<br>[20. 예외 복구·재계획·업무 연속성](../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | [ref-104](../references/ref-104.md) | <https://github.com/open-rmf/rmf_demos> |
| IEC 61360-7:2024 교차 도메인 개념 데이터 사전(General items) | IEC | 표준 | [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-437](../references/ref-437.md) | <https://webstore.iec.ch/en/publication/72956> |
| IDTA 02003 Generic Frame for Technical Data for Industrial Equipment in Manufacturing (1.2) | IDTA(Industrial Digital Twin Association) | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-438](../references/ref-438.md) | <https://industrialdigitaltwin.org/wp-content/uploads/2022/10/IDTA-02003-1-2_Submodel_TechnicalData.pdf> |
| Nav2 map_server (ROS 2 지도 서버, 점유 격자 지도 YAML 형식) | ROS Navigation (ros-navigation/navigation2) | 오픈소스 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-440](../references/ref-440.md) | <https://github.com/ros-navigation/navigation2/blob/main/nav2_map_server/README.md> |
<!-- auto:standards-table:end -->

## 읽는 법

- 표의 항목 이름에 링크가 있으면 용어집 항목으로 이어진다. ROS 2 위협 모델과 NIST 협업 로봇 성능은 아직 용어집 항목이 없다.
- ROS 2 DDS-Security 행은 ROS 2 설계 문서 "ROS 2 DDS-Security Integration"을 가리킨다. 그 바탕이 되는 객체 관리 그룹(OMG, Object Management Group)의 DDS(Data Distribution Service) 보안 규격 DDS-Security(표준)는 용어집 항목 [DDS 보안 규격 (DDS-Security)](../glossary/dds-security.md)에서 다루며, 규격 자체는 검증을 거쳐 별도 행으로 등록될 수 있다.
- 관련 세부영역은 구축자가 분류 원문의 인용 위치와 각 항목의 성격을 바탕으로 배정한 것이며, 세부영역 페이지의 "7. 관련 표준·프레임워크·오픈소스" 절이 채워지면 그에 맞춰 조정한다. [가정]
- 표준의 현행 판본·발행일은 대부분 미확인이다. 이번 구축에서는 출처 원문을 열지 못했으므로 아래 각주에 "(원문 미열람)"을 표시했다. 판본이 바뀌거나 대체된 표준은 월간 재검증에서 `needs_update` 또는 `deprecated` 로 처리한다.
- 여기 실린 항목의 기능·성능에 관한 주장은 이 위키에서 확인하지 않았다. 각 항목의 근거 문장과 태그는 용어집 항목과 세부영역 페이지에서 본다.

## 출처

[^ref-001]: ASCM, SCOR Digital Standard, 미확인, https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/, 접근일 2026-09-24 (원문 미열람)
[^ref-002]: ISA, Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems, 2025, https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of, 접근일 2026-09-24 (원문 미열람)
[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24 (원문 미열람)
[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-24 (원문 미열람)
[^ref-007]: NIST, Performance of Collaborative Robot Systems, 미확인, https://www.nist.gov/programs-projects/performance-collaborative-robot-systems, 접근일 2026-09-24 (원문 미열람)
[^ref-008]: NIST, ARIAC Documentation, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/, 접근일 2026-09-24 (원문 미열람)
[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-24 (원문 미열람)
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-24 (원문 미열람)

- 참고문헌 페이지: [ref-001](../references/ref-001.md), [ref-002](../references/ref-002.md), [ref-003](../references/ref-003.md), [ref-004](../references/ref-004.md), [ref-007](../references/ref-007.md), [ref-008](../references/ref-008.md), [ref-009](../references/ref-009.md), [ref-010](../references/ref-010.md)
- [용어집](../glossary/index.md)
```

### runs/2026-09-25-50/docs_tree.txt

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
glossary/battery-swapping.md
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
glossary/collaborative-perception.md
glossary/conflict-based-search.md
glossary/conformance-test.md
glossary/consensus-based-bundle-algorithm.md
glossary/cooperative-object-transport.md
glossary/cora.md
glossary/crdt.md
glossary/cross-schedule-dependency.md
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
glossary/mobile-manipulator.md
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
glossary/state-of-charge.md
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
references/ref-198.md
references/ref-199.md
references/ref-200.md
references/ref-201.md
references/ref-202.md
references/ref-203.md
references/ref-204.md
references/ref-205.md
references/ref-206.md
references/ref-207.md
references/ref-208.md
references/ref-209.md
references/ref-210.md
references/ref-211.md
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
references/ref-497.md
references/ref-498.md
references/ref-499.md
references/ref-530.md
references/ref-531.md
references/ref-532.md
references/ref-533.md
references/ref-534.md
references/ref-535.md
references/ref-536.md
references/ref-537.md
references/ref-538.md
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
topics/2026/2026-09-25-area16-s11.md
topics/2026/2026-09-25-area16-s4.md
topics/2026/2026-09-25-area16-s6.md
topics/2026/2026-09-25-area16-s7.md
topics/2026/2026-09-25-area16-s8.md
topics/2026/2026-09-25-area17-s10.md
topics/2026/2026-09-25-area17-s11.md
topics/2026/2026-09-25-area17-s4.md
topics/2026/2026-09-25-area17-s6.md
topics/2026/2026-09-25-area17-s7.md
topics/2026/2026-09-25-area17-s8.md
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

### runs/2026-09-25-50/pages.json

```json
{
  "run_id": "2026-09-25-50",
  "outline": [
    {
      "path": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 650,
      "summary": "VDA 5050 은 교착·통신 오류의 탐지·해소를 관제의 역할로 두므로 고장 한 건의 처리는 현장 전체를 보는 층에서 정할 문제가 된다. [추정][^ref-031]",
      "planned_findings": [
        "f6",
        "f8",
        "f19",
        "f20",
        "f15"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 800,
      "summary": "이 영역은 로봇 인터페이스의 중단·취소 동작(cancelOrder, startPause, RETRIABLE, connectionState)과 기록 쪽의 보상·정정(보상 트랜잭션, 오류 선언) 용어로 읽는다. [사실][^ref-031]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f5",
        "f18",
        "f21",
        "f11",
        "f15"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md",
      "section": "5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)",
      "budget_chars": 800,
      "summary": "피킹한 토트를 포장대로 옮기던 로봇이 멈추면 감지·취소·화물 식별·재배정·회수·기록 정정으로 이어지는 결정 흐름이 필요하다. [추정][^ref-031]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f13",
        "f19",
        "f20",
        "f21",
        "f22",
        "f24"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1100,
      "summary": "관제 인터페이스의 중단·취소·재계획 기능, 통신 단절 동안의 계속 운행 규칙, 실행 중 재계획 연구, 고장 허용 재배정, 보상·정정 패턴이 대표 접근법이다. [사실][^ref-031]",
      "planned_findings": [
        "f1",
        "f2",
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
        "f18",
        "f21",
        "f24"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 500,
      "summary": "VDA 5050·Open-RMF 가 예외 동작을 정의하고, ISO 22301 과 국내 BCP 제도는 현장 제한 운영 계획의 참조 틀(연계 대상)이다. [사실][^ref-031]",
      "planned_findings": [
        "f1",
        "f7",
        "f15",
        "f16",
        "f17",
        "f18",
        "f21"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 450,
      "summary": "지연에 강건한 MAPF 실행(행동 의존 그래프), 통과 순서 재스케줄(SES), 고장 복구 포함 작업 배정(MRPF), 롤아웃 기반 온라인 재계획이 대표 연구다. [사실][^ref-188]",
      "planned_findings": [
        "f11",
        "f12",
        "f13",
        "f14"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)",
      "budget_chars": 450,
      "summary": "로봇 자체 복구·안전 제어는 연계 대상이고, 이종 로봇을 잇는 ROP 는 주문 취소·재배정·수동 전환 결정과 기록 정정을 맡는 경계가 될 것으로 보인다. [추정][^ref-031]",
      "planned_findings": [
        "f23",
        "f15"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 550,
      "summary": "예외 복구는 명령 신뢰성·작업 배정·경로 관리·모니터링·사람 개입·재고 정정 영역과 맞물린다. [추정][^ref-031]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f7",
        "f10",
        "f11",
        "f12",
        "f13",
        "f18",
        "f21"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md",
      "section": "11. 열린 질문",
      "budget_chars": 550,
      "summary": "화물 회수 뒤 재고 확인 기준, 국내 수동·제한 운영 전환 기준, 제한 운영 처리량 추정이 새로 열렸고 기존 oq-003·oq-021·oq-038·oq-048 은 부분 근거만 있다. [의견]",
      "planned_findings": [
        "f10",
        "f18",
        "f21",
        "f24"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성(VDA 5050·Open-RMF 예외 동작, 통신 단절, 실행 중 재계획 연구, 보상·정정, BCP 참조 틀, 피킹→포장 운반 중 고장 시나리오), 페이지 상태 자동 영역 추가"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area20-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 20. 예외 복구·재계획·업무 연속성 의 \"6. 대표 접근법과 기술\" 절(1,542자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area20-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 20. 예외 복구·재계획·업무 연속성 의 \"4. 핵심 개념과 용어\" 절(1,199자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area20-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 20. 예외 복구·재계획·업무 연속성 의 \"11. 열린 질문\" 절(1,125자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area20-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 20. 예외 복구·재계획·업무 연속성 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(837자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area20-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 20. 예외 복구·재계획·업무 연속성 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(736자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-25 | 20. 예외 복구·재계획·업무 연속성 | 영역 심화: 3~11절 신규 작성(VDA 5050·Open-RMF 예외 동작, 통신 단절, 실행 중 재계획 연구, 보상·정정, BCP 참조 틀, 피킹→포장 운반 중 고장 시나리오) | run 2026-09-25-50",
  "index_updates": {
    "home_recent": "2026-09-25 — 20. 예외 복구·재계획·업무 연속성: 영역 심화로 3~11절 작성(운반 중 고장 로봇의 화물·남은 주문 처리 흐름, VDA 5050·Open-RMF 중단·취소·재계획, 업무 연속성 참조 틀)",
    "category_recent": "2026-09-25 — 20. 예외 복구·재계획·업무 연속성: 영역 심화 3~11절 신규 작성, 열린 질문 3건 추가",
    "area_recent": "2026-09-25 — 20. 예외 복구·재계획·업무 연속성: 3~11절 신규 작성(실행 2026-09-25-50)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "compensating-transaction",
      "term_ko": "보상 트랜잭션",
      "term_en": "Compensating Transaction",
      "definition": "여러 단계로 이루어진 작업이 도중에 실패했을 때 이미 완료된 단계의 효과를 업무 규칙에 맞게 되돌리는 작업이다.",
      "description": "원래 상태를 그대로 복원하는 것이 아니라 보정하며, 보상 자체가 실패할 수 있으므로 단계를 멱등 명령으로 정의하고 진행 상황을 기록해 실패 지점부터 재개하라고 권한다. 소프트웨어 설계 패턴이며 물리 작업·재고 되돌림 적용은 추정 단계다.",
      "related_areas": [
        20,
        1,
        12
      ],
      "sources": [
        "ref-578"
      ]
    },
    {
      "action": "new",
      "slug": "business-continuity-management-system",
      "term_ko": "업무 연속성 관리 시스템",
      "term_en": "Business Continuity Management System (BCMS)",
      "definition": "교란 사건에 대비하고 핵심 업무를 지속·복구하기 위한 조직의 관리 체계로, ISO 22301 이 요구사항을 정한다.",
      "description": "ISO 22301:2019 기준(개정 1:2024 별도). ROP 에서는 직접 범위가 아니라 현장 제한 운영·수동 전환 계획의 참조 틀이다.",
      "related_areas": [
        20
      ],
      "sources": [
        "ref-575"
      ]
    },
    {
      "action": "new",
      "slug": "vda-5050-cancel-order",
      "term_ko": "주문 취소 즉시 동작",
      "term_en": "cancelOrder (VDA 5050 instant action)",
      "definition": "VDA 5050 에서 관제가 보내면 로봇이 가능한 한 빨리 정지하고 남은 동작을 실패로 보고한 뒤 유휴 상태가 되게 하는 즉시 동작이다.",
      "description": "VDA 5050 3.0.0 기준. 예정 동작은 FAILED, 정지 뒤 cancelOrder 는 FINISHED 로 보고한다.",
      "related_areas": [
        20,
        9,
        12
      ],
      "sources": [
        "ref-031"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고. 교통 스케줄 협상과 읽기 전용 플릿 설명.",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 최신판(3.0.0) 명세 원문. cancelOrder·startPause·연결 끊김·오류 처리와 관제 역할을 규정한다.",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
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
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 상태 메시지 JSON 스키마. errorLevel, actionStatus, loads, paused, newBaseRequest 필드를 정의한다.",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-188",
      "org": "Hönig, W., Kiesel, S., Tinka, A., Durham, J. W., & Ayanian, N.",
      "title": "Persistent and Robust Execution of MAPF Schedules in Warehouses",
      "published": "2019-04",
      "url": "https://ieeexplore.ieee.org/abstract/document/8620328/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 행동 의존 그래프로 창고 MAPF 계획을 지연·감속에 강건하게 실행하고 재계획과 실행을 겹치게 하는 틀(IEEE RA-L).",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-251",
      "org": "Open Robotics",
      "title": "Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration)",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 플릿 어댑터 연동 수준(Full Control, Easy Full Control, Traffic Light)과 경로 중단·교체 방식을 설명하는 장.",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-537",
      "org": "Open Robotics (open-rmf/rmf_ros2)",
      "title": "rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "플릿 어댑터의 로봇 갱신 핸들 API 헤더. interrupt·resume·cancel_task·kill_task·replan·set_commission·create_issue 등의 문서 주석을 담는다.",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-572",
      "org": "Feng, Y., Paul, A., Chen, Z., & Li, J.",
      "title": "A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution",
      "published": "2024",
      "url": "https://arxiv.org/abs/2403.18145",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 실행 중 지연된 로봇의 통과 순서를 전환 가능 간선 탐색(SES)으로 실시간 재스케줄하는 알고리즘(ICAPS 2024).",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-573",
      "org": "Kalempa, V. C., Piardi, L., Limeira, M., & de Oliveira, A. S.",
      "title": "Multi-Robot Preemptive Task Scheduling with Fault Recovery: A Novel Approach to Automatic Logistics of Smart Factories",
      "published": "2021-09-30",
      "url": "https://www.mdpi.com/1424-8220/21/19/6536",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 우선순위 선점 스케줄링·작업 의존성·고장 복구를 결합한 다중 로봇 작업 배정 방법 MRPF(Sensors 21(19)).",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-574",
      "org": "Emanuelsson, W., Penacho Riveiros, A., Li, Y., Johansson, K. H., & Mårtensson, J. (KTH)",
      "title": "Multiagent Rollout with Reshuffling for Warehouse Robots Path Planning",
      "published": "2023",
      "url": "https://arxiv.org/abs/2211.08201",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 창고 로봇 경로 계획용 다중 에이전트 롤아웃 방법으로, 온라인 재계획으로 로봇 고장에 적응하는 예제를 보인다(IFAC 게재, 프리프린트).",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-575",
      "org": "ISO",
      "title": "ISO 22301:2019 - Security and resilience — Business continuity management systems — Requirements",
      "published": "2019",
      "url": "https://www.iso.org/standard/75106.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 업무 연속성 관리 시스템(BCMS)의 요구사항 국제표준(2019 기준, 개정 1:2024 별도). 발행 기관 소개 페이지 검색 결과로 확인.",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-576",
      "org": "행정안전부",
      "title": "재해경감 우수기업 인증제도",
      "published": null,
      "url": "https://www.mois.go.kr/frt/sub/a06/b10/disasterMitigationCompanies/screen.do",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 재해경감을 위한 기업의 자율활동 지원에 관한 법률에 따른 기업재난관리표준과 재해경감 우수기업 인증 절차 안내.",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-577",
      "org": "고용노동부",
      "title": "중소규모 사업장 기능연속성계획(BCP) 수립 가이드 안내",
      "published": "2022-03",
      "url": "https://www.moel.go.kr/news/notice/noticeView.do?bbs_seq=20220301591",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 오미크론 확산기 사회 필수 기능 유지를 위한 중소규모 사업장 BCP 수립 7단계 가이드 안내(감염병 대응 권고 가이드).",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-578",
      "org": "Microsoft (MicrosoftDocs/architecture-center)",
      "title": "Compensating Transaction pattern",
      "published": "2026-04-16",
      "url": "https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "여러 단계 작업이 실패할 때 완료된 단계를 되돌리는 보상 트랜잭션 패턴 설명. 멱등 단계, 진행 기록, 사람 개입을 권한다.",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-579",
      "org": "Element Logic",
      "title": "FAQ - Element Logic (AutoStore)",
      "published": null,
      "url": "https://www.elementlogic.net/solutions-and-services/autostore/faq/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AutoStore 통합 업체의 FAQ. 로봇 고장 시 XHandler 모듈의 처리와 시스템 지속 운영을 설명한다(벤더 주장).",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-580",
      "org": "Swisslog",
      "title": "The benefits of using AutoStore for high-throughput retail fulfillment",
      "published": "2025-07",
      "url": "https://www.swisslog.com/en-us/blog/2025/07/benefits-of-autostore-htp",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Swisslog 블로그. 멈춘 로봇 아래 재고를 SynQ 가 재할당해 주문 처리를 계속한다고 설명한다(벤더 주장).",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-581",
      "org": "GS1",
      "title": "EPC Information Services (EPCIS) Standard 1.2",
      "published": "2016-09-29",
      "url": "https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. EPCIS 1.2 표준. 저장소를 일지 방식으로 두고 오류 선언(errorDeclaration)으로 이벤트를 정정하는 방법을 정한다.",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-374",
      "org": "Open Robotics (open-rmf/rmf_ros2)",
      "title": "Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/issues/224",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 플릿 어댑터 재시작 시 작업 유실 문제와 SQLite 백업(PR 161)·rmf-web 영속 DB 조회 제안을 다룬 이슈.",
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md"
      ],
      "source_unopened": true
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "운반 중 고장 난 로봇에 실린 화물을 사람이나 다른 로봇이 회수할 때 어떤 확인(스캔·무게·위치)으로 재고 위치를 바로잡는지 정한 운영 기준이나 국내 사례가 있는가?",
      "areas": [
        20,
        7
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 물류센터가 로봇·관제 장애 때 수동 운영이나 제한 운영으로 전환하는 기준(허용 중단 시간, 전환·복귀 절차)을 BCP 에 정한 사례가 있는가?",
      "areas": [
        20,
        18
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 일부가 멈춘 제한 운영 상태의 처리량 저하를 미리 추정해 전환 결정에 쓰는 방법이나 사례가 있는가?",
      "areas": [
        20,
        22
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [
    {
      "step": "피킹",
      "item": "시작 조건",
      "link": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "20. 예외 복구·재계획·업무 연속성"
    },
    {
      "step": "피킹",
      "item": "작업 대상",
      "link": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "20. 예외 복구·재계획·업무 연속성"
    },
    {
      "step": "피킹",
      "item": "수행 자원",
      "link": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "20. 예외 복구·재계획·업무 연속성"
    },
    {
      "step": "피킹",
      "item": "제약",
      "link": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "20. 예외 복구·재계획·업무 연속성"
    },
    {
      "step": "피킹",
      "item": "완료·인계",
      "link": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "20. 예외 복구·재계획·업무 연속성"
    },
    {
      "step": "피킹",
      "item": "예외·성과",
      "link": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "20. 예외 복구·재계획·업무 연속성"
    },
    {
      "step": "포장",
      "item": "시작 조건",
      "link": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "20. 예외 복구·재계획·업무 연속성"
    },
    {
      "step": "포장",
      "item": "작업 대상",
      "link": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "20. 예외 복구·재계획·업무 연속성"
    },
    {
      "step": "포장",
      "item": "수행 자원",
      "link": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "20. 예외 복구·재계획·업무 연속성"
    },
    {
      "step": "포장",
      "item": "제약",
      "link": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "20. 예외 복구·재계획·업무 연속성"
    },
    {
      "step": "포장",
      "item": "완료·인계",
      "link": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "20. 예외 복구·재계획·업무 연속성"
    },
    {
      "step": "포장",
      "item": "예외·성과",
      "link": "docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "20. 예외 복구·재계획·업무 연속성"
    }
  ],
  "standards_updates": [
    {
      "name": "ISO 22301:2019 업무 연속성 관리 시스템 요구사항(개정 1:2024 별도)",
      "kind": "표준",
      "org": "ISO",
      "url": "https://www.iso.org/standard/75106.html",
      "related_areas": [
        20
      ],
      "summary": "교란 사건 대비·복구를 위한 BCMS 의 수립·운영·점검·개선 요구사항. ROP 에는 현장 제한 운영·수동 전환 계획의 참조 틀(연계 대상)이다. 원문 미열람.",
      "ref_id": "ref-575"
    },
    {
      "name": "기업재난관리표준·재해경감 우수기업 인증제",
      "kind": "평가 프로그램",
      "org": "행정안전부",
      "url": "https://www.mois.go.kr/frt/sub/a06/b10/disasterMitigationCompanies/screen.do",
      "related_areas": [
        20
      ],
      "summary": "「재해경감을 위한 기업의 자율활동 지원에 관한 법률」에 따른 기업재난관리표준 고시와 문서평가·현장평가를 거치는 재해경감 우수기업 인증. 원문 미열람.",
      "ref_id": "ref-576"
    },
    {
      "name": "중소규모 사업장 기능연속성계획(BCP) 수립 가이드(2022)",
      "kind": "프레임워크",
      "org": "고용노동부",
      "url": "https://www.moel.go.kr/news/notice/noticeView.do?bbs_seq=20220301591",
      "related_areas": [
        20
      ],
      "summary": "오미크론 확산기에 안내한 감염병 대응 권고 가이드로 7단계 BCP 수립 절차를 담는다. 원문 미열람.",
      "ref_id": "ref-577"
    },
    {
      "name": "보상 트랜잭션 패턴(Compensating Transaction pattern)",
      "kind": "프레임워크",
      "org": "Microsoft (Azure Architecture Center)",
      "url": "https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction",
      "related_areas": [
        20,
        1,
        12
      ],
      "summary": "실패한 다단계 작업의 완료 단계를 업무 규칙에 맞춰 보정하는 설계 패턴. 멱등 단계·진행 기록·사람 참여를 권한다.",
      "ref_id": "ref-578"
    },
    {
      "name": "Open-RMF rmf_ros2 플릿 어댑터(RobotUpdateHandle)",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp",
      "related_areas": [
        20,
        9,
        12
      ],
      "summary": "작업 중단·재개·취소·강제 종료·재계획 요청·작업 수락 중지·이슈 생성 API(헤더 문서 주석 기준).",
      "ref_id": "ref-537"
    }
  ],
  "additional_research_requests": [
    "5절 예외·성과: 로봇 일부 고장·제한 운영 시 처리량·시간·비용 영향 수치(독립 출처 2개 이상)가 없어 '미확인'으로 두었다.",
    "5절 완료·인계·11절: 고장 로봇 화물 회수 시 재고 위치 확인(스캔·무게·위치) 운영 기준과 국내 사례가 필요하다.",
    "7절: ISO 22301 의 업무 영향 분석·목표 복구 시간(RTO) 요구와 KS A ISO 22301 부합화 연도를 1차 출처로 확인할 필요가 있다.",
    "4·6절: EPCIS 현행 판(2.0, ISO/IEC 19987:2024)에서 오류 선언 방식이 유지되는지 확인이 필요하다(현재 EPCIS 1.2 기준으로만 서술).",
    "6절: VDA 5050 에서 cancelOrder 뒤 적재물 처리 규정 유무를 다른 절(3.0.0 전체)과 교차 확인할 필요가 있다.",
    "6·7절: 표준 목록이 20. 예외 복구·재계획·업무 연속성과 연결한 ARIAC(ref-008)·KubeEdge(ref-300)·rmf_task(ref-366)·rmf_demos(ref-104)의 예외 복구 관련 내용이 이번 브리프에 없어 본문에 넣지 못했다.",
    "3절: 국내 물류센터의 로봇·관제 장애 수동 전환 사례(한국어 자료)가 필요하다."
  ],
  "fixes_applied": [
    "ref-188 → ref-188 — f11 을 쓴 4·6·8·10절 각주와 13절 정의, reference_updates 모두 ref-188 로 바꾸고 ref-188 은 등록하지 않았다.",
    "f11·f21 기존 용어 재사용 — 4절에서 행동 의존 그래프·오류 선언을 용어집 action-dependency-graph·epcis-error-declaration 에 링크했고 glossary_updates 에 넣지 않았다.",
    "'업무 연속성 관리 시스템' 띄어쓰기 — 4절 용어와 glossary_updates 의 term_ko 를 '업무 연속성 관리 시스템'으로 적었다.",
    "f2 connectionState 네 값 — 4절에 ONLINE·OFFLINE·CONNECTION_BROKEN·HIBERNATING 네 값을 적었다.",
    "f6 통로 이탈 문맥 — 6절에서 '통로(corridor) 이탈 오류 같은 상황에서'로 쓰고 교착 해소 전략·알고리즘 자체는 명세 범위 밖이라는 문장을 더했다.",
    "f1 적재물 처리 — 4절에 '명세 6.1.3 절에는 취소 시 실린 적재물을 어떻게 처리하는지에 대한 언급이 없다'를 [추정]으로 적었다.",
    "f9 Read Only 각주 — 6절의 읽기 전용 문장에는 ref-004 만, 전체 제어·신호등 제어 문장에는 ref-251 를 달았다.",
    "f12 수치 — 6절에 '저자 보고값(ICAPS 2024, 단일 출처)', 8절에 '속도 수치는 저자 보고값'을 명시했다.",
    "f15 판 명시 — 7절 표에 'ISO 22301:2019 기준(개정 1:2024 별도)'으로 적었다.",
    "f21 기준 판 — 4·5·6절에 'EPCIS 1.2(2016-09-29) 기준'을 명시하고 6절에 현행 판 유지 여부는 확인하지 않았다고 적었다.",
    "f15·f16·f17 범위 — 3절·7절·9절에서 기업 BCP·BCMS 체계를 ROP 직접 범위가 아닌 참조 틀(연계 대상)로 짧게 서술하고 f17 을 감염병 대응 권고 가이드로 밝혔다.",
    "f19·f20 벤더 주장 — 3·5절에서 [추정] 뒤에 '벤더 주장'을 병기하고 AutoStore 제어 소프트웨어의 XHandler 모듈·Swisslog 자사 소프트웨어 SynQ 의 기능으로 서술했으며 ROP 기능으로 쓰지 않았다.",
    "f18 물리 적용 — 6절에서 보상 트랜잭션을 화물 되돌림·재고 반영에 적용하는 문장을 [추정]으로 썼다.",
    "ref-574 기관 — 각주와 reference_updates 의 기관을 'Emanuelsson, W., Penacho Riveiros, A., Li, Y., Johansson, K. H., & Mårtensson, J. (KTH)'로 고쳤다.",
    "ref-580 URL — 각주와 reference_updates 의 URL 을 https://www.swisslog.com/en-us/blog/2025/07/benefits-of-autostore-htp 로 고쳤다.",
    "원문 미열람 표시 — ref-188·572·573·574·575·576·577·579·580·581·582 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-576·579·582 의 발행일 자리에 '미확인'을 썼다.",
    "열린 질문 상태 — 11절에서 oq-003·oq-021·oq-038·oq-048 을 모두 '열림'으로 두고 부분 근거로만 적었으며 open_question_updates 에 해결로 내지 않았다.",
    "분량 초과 자동 분리: 20. 예외 복구·재계획·업무 연속성 본문 8,408자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,648자"
  ]
}
```

### runs/2026-09-25-50/pages/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md

````markdown
---
title: "20. 예외 복구·재계획·업무 연속성"
type: area
category: "E. 협업·현장 운영"
area_no: 20
related_areas: [1, 7, 9, 11, 12, 13, 15, 18, 19, 22]
tags: [예외 복구, VDA 5050, Open-RMF, 재계획, 업무 연속성, 보상 트랜잭션]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-004, ref-031, ref-051, ref-188, ref-251, ref-537, ref-572, ref-573, ref-574, ref-575, ref-576, ref-577, ref-578, ref-579, ref-580, ref-581, ref-374]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [E. 협업·현장 운영](index.md) › 20. 예외 복구·재계획·업무 연속성

# 20. 예외 복구·재계획·업무 연속성

!!! info "소속 대분류"
    [E. 협업·현장 운영](index.md) — 핵심 질문:
    계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 [분류원문]

## 2. SCM 관점의 질문

운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? [분류원문]

## 3. 왜 중요한가

로봇 인터페이스 표준 VDA 5050 은 교착(deadlock)과 통신 오류의 탐지·해소를 개별 로봇이 아니라 관제(fleet control)의 역할로 두므로, 고장 한 건의 처리는 현장 전체를 보는 층에서 정해야 하는 문제가 된다. [추정][^ref-031]

한 로봇의 지연·취소는 주변 로봇의 계획에도 번진다. Open-RMF 의 교통 스케줄은 지연·취소·경로 변경을 반영해 계속 바뀌는 데이터베이스이고, 충돌이 예상되면 관련 플릿 관리자 사이의 협상이 시작된다. [사실][^ref-004]

고장 로봇 하나가 전체를 멈추지 않게 하는 설계는 제품 차원에서도 다뤄진다. Element Logic 은 AutoStore 제어 소프트웨어의 XHandler 모듈이 고장 난 로봇을 넘겨받아 시스템을 멈추지 않고 오류를 처리하며, 자동 처리가 불가능하거나 충돌 위험이 있을 때만 시스템이 정지한다고 설명한다. [추정] 벤더 주장[^ref-579] Swisslog 은 로봇이 멈추면 자사 소프트웨어 SynQ 가 멈춘 로봇 아래 보관함의 재고를 다른 보관함으로 재할당해, 로봇을 정기 휴식이나 저수요 시간에 꺼낼 때까지 주문 처리를 계속한다고 설명한다(2025년 7월 기준). [추정] 벤더 주장[^ref-580]

기업 차원에서는 업무 연속성 관리가 같은 질문을 더 넓게 다룬다. 다만 기업 업무 연속성 계획(Business Continuity Plan, BCP) 체계는 ROP 직접 범위가 아니라 현장의 제한 운영·수동 전환 계획을 세울 때 참조하는 연계 대상이다(7절). [추정][^ref-575]

## 4. 핵심 개념과 용어

이 영역의 용어는 로봇 인터페이스의 중단·취소 동작과, 이미 일어난 일을 기록에서 보상·정정하는 개념으로 나뉜다. [사실][^ref-031]

자세한 내용은 주제 페이지 [20. 예외 복구·재계획·업무 연속성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area20-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 피킹 → 포장

**시나리오:** 피킹한 주문 토트를 포장대로 운반하던 로봇이 도중에 멈춤

| 항목 | 내용 |
|---|---|
| 시작 조건 | 운반 중인 로봇이 오류 수준(WARNING·URGENT·CRITICAL·FATAL)을 보고하거나 연결 상태가 CONNECTION_BROKEN 으로 바뀐다. [사실][^ref-051][^ref-031] |
| 작업 대상 | 로봇에 실린 토트. 로봇이 loads 를 보고한다면 적재물 식별번호(loadId)·종류·적재 위치·치수·무게로 어떤 화물이 실렸는지 관제가 알 수 있다(선택 필드). [사실][^ref-051] |
| 수행 자원 | 멈춘 로봇, 남은 작업을 넘겨받을 대체 로봇, 화물을 회수할 작업자, 결정을 내리는 관제. 작업 의존성·우선순위 선점·고장 복구를 함께 다루는 배정 방법이 연구돼 있다. [사실][^ref-573] |
| 제약 | 연결이 끊긴 로봇은 마지막으로 해제된 노드까지만 주문을 수행하므로, 관제가 한 번에 해제하는 범위(base)의 길이가 단절 동안 작업이 얼마나 계속되는지를 정하는 설계 변수가 될 것으로 보인다. [추정][^ref-031] |
| 완료·인계 | 회수한 화물의 위치를 다시 확인한 뒤 재고·이벤트 기록을 정정해야 완료로 인정할 수 있다. EPCIS 1.2 기준으로는 오류 선언 이벤트로 기존 기록을 정정한다. [사실][^ref-581] 회수 때 어떤 확인(스캔·무게·위치)을 요구할지는 미확인이다(11절). |
| 예외·성과 | 관제가 cancelOrder 를 보내면 로봇은 정지하고 남은 동작을 FAILED 로 보고한다. [사실][^ref-031] 멈춘 로봇의 영향을 줄이는 재고 재할당·자동 복구는 AutoStore 계열 제품의 기능으로 설명된다. [추정] 벤더 주장[^ref-579][^ref-580] 처리량·시간·비용 영향 수치는 미확인이다. |

다음은 설명을 위한 가상의 시나리오이다. 피킹을 마친 토트를 싣고 포장대로 가던 로봇이 통로에서 멈추면, 관제는 먼저 오류·연결 상태로 무엇이 일어났는지 확인하고 주문을 일시정지하거나 취소한다. 이어 로봇이 보고한 적재물 정보로 어떤 주문의 화물이 묶였는지 파악하고, 남은 작업을 다른 로봇에 넘기며, 사람이 화물을 회수한 뒤 재고 기록을 바로잡는다.

이렇게 감지 → 일시정지·취소 → 실린 화물 식별 → 남은 작업 재배정 → 물리적 회수 → 재고·이벤트 기록의 보상·정정으로 이어지는 결정 흐름으로 볼 수 있을 것으로 보인다. 다만 이 흐름을 한 절차로 정한 출처는 이번 조사에서 찾지 못했다. [추정][^ref-031][^ref-051][^ref-573][^ref-578][^ref-581]

```mermaid
flowchart LR
  detect[고장·연결 끊김 감지] --> hold[주문 일시정지·취소]
  hold --> identify[실린 화물 식별]
  identify --> reassign[남은 작업 재배정]
  reassign --> recover[화물 물리적 회수]
  recover --> correct[재고·이벤트 기록 보상·정정]
```

## 6. 대표 접근법과 기술

대표 접근법은 관제 인터페이스의 중단·취소·재계획 기능, 통신 단절 동안의 계속 운행 규칙, 실행 중 재계획 연구, 고장 허용 재배정, 기록의 보상·정정으로 나뉜다. [사실][^ref-031][^ref-537]

자세한 내용은 주제 페이지 [20. 예외 복구·재계획·업무 연속성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area20-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

예외 동작 자체는 VDA 5050·Open-RMF 가 정의하고, 업무 연속성 표준과 국내 제도는 현장 제한 운영·수동 전환 계획의 참조 틀(연계 대상)로 쓴다. [추정][^ref-031][^ref-575]

자세한 내용은 주제 페이지 [20. 예외 복구·재계획·업무 연속성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area20-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 연구는 지연에 강건한 계획 실행, 통과 순서 재스케줄, 고장 복구를 포함한 작업 배정, 온라인 재계획 네 갈래다. [사실][^ref-188][^ref-572]

- Hönig 외, Persistent and Robust Execution of MAPF Schedules in Warehouses(IEEE RA-L, 2019) — 행동 의존 그래프로 창고 다중 로봇 계획을 감속·장애물·지연에도 충돌 없이 실행하는 틀이다. [사실][^ref-188]
- Feng 외, A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution(ICAPS 2024) — 지연된 로봇의 통과 순서를 SES 로 재스케줄한다. 속도 수치는 저자 보고값이다. [사실][^ref-572]
- Kalempa 외, Multi-Robot Preemptive Task Scheduling with Fault Recovery(Sensors, 2021) — 선점 스케줄링과 고장 복구를 결합한 MRPF. [사실][^ref-573]
- Emanuelsson 외, Multiagent Rollout with Reshuffling for Warehouse Robots Path Planning(IFAC 게재, 2023) — 온라인 재계획으로 로봇 고장에 적응하는 예제를 보인다. [사실][^ref-574]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

로봇 자체 복구·안전 제어는 제조사 몫인 연계 대상이고, 이종 로봇을 잇는 ROP 는 주문 취소·재배정·수동 전환 결정과 기록 정정을 맡는 경계가 될 것으로 보인다. [추정][^ref-031][^ref-537]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 오류·연결 상태 수신, 주문 일시정지·취소, 재계획 요청·작업 수락 중지, 사용자 개입·수동 전환 결정 [추정][^ref-031][^ref-537] | 연계 대상: 장애물 회피·재위치 추정·비상정지 회로 같은 로봇 자체 복구·안전 제어 [추정][^ref-031] |
| 상위 업무 시스템 | 취소·회수 결과를 보상 원칙에 따라 기록하고 재고·이벤트 정정을 반영 [추정][^ref-578][^ref-581] | 연계 대상: 전사 BCP·BCMS 와 재해경감 체계(현장 제한 운영 계획의 참조 틀) [추정][^ref-575][^ref-576] |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

예외 복구는 명령 실행 보장, 재배정·재계획, 모니터링, 사람 개입, 재고 정정을 맡는 영역과 맞물린다. [추정][^ref-031]

자세한 내용은 주제 페이지 [20. 예외 복구·재계획·업무 연속성 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area20-s10.md)에 있다.

## 11. 열린 질문

화물 회수 뒤 재고 확인 기준, 국내 수동·제한 운영 전환 기준, 제한 운영 처리량 추정이 새로 열렸고, 기존 네 질문은 부분 근거만 있어 열림 상태를 유지한다. [의견]

자세한 내용은 주제 페이지 [20. 예외 복구·재계획·업무 연속성 — 열린 질문](../../topics/2026/2026-09-25-area20-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-188]: Hönig, W., Kiesel, S., Tinka, A., Durham, J. W., & Ayanian, N., Persistent and Robust Execution of MAPF Schedules in Warehouses, 2019-04, https://ieeexplore.ieee.org/abstract/document/8620328/, 접근일 2026-09-25 (원문 미열람)
[^ref-537]: Open Robotics (open-rmf/rmf_ros2), rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 접근일 2026-09-25
[^ref-572]: Feng, Y., Paul, A., Chen, Z., & Li, J., A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution, 2024, https://arxiv.org/abs/2403.18145, 접근일 2026-09-25 (원문 미열람)
[^ref-573]: Kalempa, V. C., Piardi, L., Limeira, M., & de Oliveira, A. S., Multi-Robot Preemptive Task Scheduling with Fault Recovery: A Novel Approach to Automatic Logistics of Smart Factories, 2021-09-30, https://www.mdpi.com/1424-8220/21/19/6536, 접근일 2026-09-25 (원문 미열람)
[^ref-574]: Emanuelsson, W., Penacho Riveiros, A., Li, Y., Johansson, K. H., & Mårtensson, J. (KTH), Multiagent Rollout with Reshuffling for Warehouse Robots Path Planning, 2023, https://arxiv.org/abs/2211.08201, 접근일 2026-09-25 (원문 미열람)
[^ref-575]: ISO, ISO 22301:2019 - Security and resilience — Business continuity management systems — Requirements, 2019, https://www.iso.org/standard/75106.html, 접근일 2026-09-25 (원문 미열람)
[^ref-576]: 행정안전부, 재해경감 우수기업 인증제도, 미확인, https://www.mois.go.kr/frt/sub/a06/b10/disasterMitigationCompanies/screen.do, 접근일 2026-09-25 (원문 미열람)
[^ref-578]: Microsoft (MicrosoftDocs/architecture-center), Compensating Transaction pattern, 2026-04-16, https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction, 접근일 2026-09-25
[^ref-579]: Element Logic, FAQ - Element Logic (AutoStore), 미확인, https://www.elementlogic.net/solutions-and-services/autostore/faq/, 접근일 2026-09-25 (원문 미열람)
[^ref-580]: Swisslog, The benefits of using AutoStore for high-throughput retail fulfillment, 2025-07, https://www.swisslog.com/en-us/blog/2025/07/benefits-of-autostore-htp, 접근일 2026-09-25 (원문 미열람)
[^ref-581]: GS1, EPC Information Services (EPCIS) Standard 1.2, 2016-09-29, https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf, 접근일 2026-09-25 (원문 미열람)
````

### runs/2026-09-25-50/pages/topics/2026/2026-09-25-area20-s6.md

```markdown
---
title: "20. 예외 복구·재계획·업무 연속성 — 대표 접근법과 기술"
type: topic
category: "E. 협업·현장 운영"
primary_area_no: 20
related_areas: [1, 7, 9, 11, 12, 13, 15, 18, 19, 22]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-004, ref-031, ref-188, ref-251, ref-537, ref-572, ref-573, ref-574, ref-578, ref-581, ref-374]
last_run: 2026-09-25
version: 1
split_from: docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#6
---

[홈](../../index.md) › [주제](../index.md) › 20. 예외 복구·재계획·업무 연속성 — 대표 접근법과 기술

# 20. 예외 복구·재계획·업무 연속성 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대표 접근법은 관제 인터페이스의 중단·취소·재계획 기능, 통신 단절 동안의 계속 운행 규칙, 실행 중 재계획 연구, 고장 허용 재배정, 기록의 보상·정정으로 나뉜다. [사실][^ref-031][^ref-537]
- 이 페이지는 [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대표 접근법은 관제 인터페이스의 중단·취소·재계획 기능, 통신 단절 동안의 계속 운행 규칙, 실행 중 재계획 연구, 고장 허용 재배정, 기록의 보상·정정으로 나뉜다. [사실][^ref-031][^ref-537]

### 관제 인터페이스의 중단·취소·재계획

VDA 5050 은 교착 탐지·해소와 통신 오류 탐지·해소를 관제의 역할로 두고, 통로(corridor) 이탈 오류 같은 상황에서 사용자 개입이 필요한지, 현재 주문을 취소하고 새 주문을 보낼지를 관제가 결정한다고 설명한다. [사실][^ref-031] 교착 해소 전략·알고리즘 자체는 명세 범위 밖이다. [사실][^ref-031]

Open-RMF 플릿 어댑터의 RobotUpdateHandle 은 작업 중단(interrupt)과 재개(resume), 작업 취소(cancel_task)·강제 종료(kill_task), 마지막 보고 위치에서의 재계획 요청(replan), 작업 수락 중지(set_commission), 이슈 생성(create_issue) 기능을 헤더 문서 주석으로 정의한다(동작 검증은 아님). [사실][^ref-537] 연동 수준에 따라 쓸 수 있는 복구 수단이 다르다. 전체 제어(Full Control)는 경로를 언제든 중단하고 새 경로로 바꿀 수 있고, 신호등 제어(Traffic Light)는 일시정지·재개만 허용한다. [사실][^ref-251] 읽기 전용(Read Only) 플릿은 RMF 에 제어권 없이 상태만 보고한다. [사실][^ref-004] 교통 스케줄에서는 긴급 참여자가 의도적으로 충돌을 게시해 협상을 강제할 수 있다. [사실][^ref-004]

### 통신 단절과 관제 재시작 동안의 계속 운행

VDA 5050 3.0.0 에서 브로커와 연결이 끊긴 로봇은 주문 정보를 유지한 채 마지막으로 해제된 노드까지 주문을 수행한다. [사실][^ref-031] 관제 쪽 재시작도 예외다. Open-RMF rmf_ros2 이슈 224 는 플릿 어댑터가 재시작되면 배정된 작업이 유실되는 문제를 제기하고 SQLite 작업 백업(PR 161)과 rmf-web 영속 데이터베이스 조회를 제안하지만, 배포판 반영 여부는 미확인이다. [사실][^ref-374]

### 실행 중 재계획

계획을 처음부터 다시 풀지 않고 지연을 흡수하는 연구가 있다. 행동 의존 그래프로 순서 제약을 인코딩하면 예기치 않은 지연에도 충돌 없이 실행하고 재계획과 실행을 겹칠 수 있다. [사실][^ref-188] 전환 가능 간선 탐색(Switchable-Edge Search, SES)은 경로는 유지하고 통과 순서만 다시 정하며, 최선 변형이 중소 규모에서 1초 미만, 대규모에서 기준선보다 최대 4배 빠르다는 것은 저자 보고값(ICAPS 2024, 단일 출처)이다. [사실][^ref-572] 다중 에이전트 롤아웃·재배열 방법은 일부 로봇이 고장 나는 예제로 온라인 재계획을 보인다. [사실][^ref-574]

### 고장 허용 재배정

MRPF 는 작업 간 의존성, 우선순위 기반 선점 스케줄링, 고장 복구를 함께 다루는 다중 로봇 작업 배정 방법이며 소규모 창고 물류 실험 환경에서 평가되었다. [사실][^ref-573]

### 보상과 기록 정정

보상 트랜잭션 패턴은 보상 자체가 실패할 수 있으므로 단계를 멱등 명령으로 정의하고 진행 상황을 기록해 실패 지점부터 재개하며, 영향이 큰 결정에는 사람을 참여시키라고 권한다. [사실][^ref-578] 이 패턴은 소프트웨어 설계 패턴이므로, 이미 옮긴 화물의 되돌림과 재고 반영에 그대로 적용할 수 있는지는 추정 단계다. [추정][^ref-578] EPCIS 1.2(2016-09-29) 기준 저장소는 기존 이벤트를 수정·삭제하지 않는 일지 방식이어서 정정은 오류 선언으로 한다. 현행 판에서의 유지 여부는 이번에 확인하지 않았다. [사실][^ref-581]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [11. 분산 시스템·통신·컴퓨팅 구조](../../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-188]: Hönig, W., Kiesel, S., Tinka, A., Durham, J. W., & Ayanian, N., Persistent and Robust Execution of MAPF Schedules in Warehouses, 2019-04, https://ieeexplore.ieee.org/abstract/document/8620328/, 접근일 2026-09-25 (원문 미열람)
[^ref-251]: Open Robotics, Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration), 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-09-25
[^ref-537]: Open Robotics (open-rmf/rmf_ros2), rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 접근일 2026-09-25
[^ref-572]: Feng, Y., Paul, A., Chen, Z., & Li, J., A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution, 2024, https://arxiv.org/abs/2403.18145, 접근일 2026-09-25 (원문 미열람)
[^ref-573]: Kalempa, V. C., Piardi, L., Limeira, M., & de Oliveira, A. S., Multi-Robot Preemptive Task Scheduling with Fault Recovery: A Novel Approach to Automatic Logistics of Smart Factories, 2021-09-30, https://www.mdpi.com/1424-8220/21/19/6536, 접근일 2026-09-25 (원문 미열람)
[^ref-574]: Emanuelsson, W., Penacho Riveiros, A., Li, Y., Johansson, K. H., & Mårtensson, J. (KTH), Multiagent Rollout with Reshuffling for Warehouse Robots Path Planning, 2023, https://arxiv.org/abs/2211.08201, 접근일 2026-09-25 (원문 미열람)
[^ref-578]: Microsoft (MicrosoftDocs/architecture-center), Compensating Transaction pattern, 2026-04-16, https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction, 접근일 2026-09-25
[^ref-581]: GS1, EPC Information Services (EPCIS) Standard 1.2, 2016-09-29, https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-374]: Open Robotics (open-rmf/rmf_ros2), Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2, 미확인, https://github.com/open-rmf/rmf_ros2/issues/224, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-50 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-50 | 20. 예외 복구·재계획·업무 연속성 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-25-50/pages/topics/2026/2026-09-25-area20-s4.md

```markdown
---
title: "20. 예외 복구·재계획·업무 연속성 — 핵심 개념과 용어"
type: topic
category: "E. 협업·현장 운영"
primary_area_no: 20
related_areas: [1, 7, 9, 11, 12, 13, 15, 18, 19, 22]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-051, ref-188, ref-575, ref-578, ref-581]
last_run: 2026-09-25
version: 1
split_from: docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#4
---

[홈](../../index.md) › [주제](../index.md) › 20. 예외 복구·재계획·업무 연속성 — 핵심 개념과 용어

# 20. 예외 복구·재계획·업무 연속성 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 용어는 로봇 인터페이스의 중단·취소 동작과, 이미 일어난 일을 기록에서 보상·정정하는 개념으로 나뉜다. [사실][^ref-031]
- 이 페이지는 [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 용어는 로봇 인터페이스의 중단·취소 동작과, 이미 일어난 일을 기록에서 보상·정정하는 개념으로 나뉜다. [사실][^ref-031]

- **주문 취소 즉시 동작(cancelOrder)** — [VDA 5050](../../glossary/vda-5050.md) 3.0.0 에서 이 즉시 동작을 받은 로봇은 가능한 한 빨리 정지하고, 예정된 동작을 FAILED 로 보고하며, 정지 뒤 cancelOrder 상태를 FINISHED 로 보고하고 유휴 상태가 된다. [사실][^ref-031] 명세 6.1.3 절에는 취소 시 실린 적재물을 어떻게 처리하는지에 대한 언급이 없다. [추정][^ref-031]
- **연결 상태(connectionState)** — [MQTT(Message Queuing Telemetry Transport)](../../glossary/mqtt.md) 라스트 윌(last will) 메시지로 관제가 로봇의 연결 끊김을 감지하게 하는 값이며, ONLINE·OFFLINE·CONNECTION_BROKEN·HIBERNATING 네 값이 있다. [사실][^ref-031]
- **오류 수준(errorLevel)과 RETRIABLE** — 상태 스키마는 오류 수준을 WARNING·URGENT·CRITICAL·FATAL 로, 동작 상태에 RETRIABLE 을 두며, 명세는 RETRIABLE 상태의 로봇이 관제나 운영자의 개입을 기다린다고 설명한다. [사실][^ref-051][^ref-031]
- **일시정지(startPause·stopPause)** — startPause 는 자동 주행과 일시정지 가능한 동작(pauseAllowed=true)만 멈추고, stopPause 로 주문 실행을 재개한다. [사실][^ref-031]
- **보상 트랜잭션(Compensating Transaction)** — 여러 단계 작업이 실패했을 때 완료된 단계의 효과를 원래 상태 그대로가 아니라 업무 규칙에 맞춰 보정해 되돌리는 설계 패턴이다. [사실][^ref-578]
- **[오류 선언(errorDeclaration)](../../glossary/epcis-error-declaration.md)** — EPCIS 1.2(2016-09-29) 기준으로, 잘못 기록된 이벤트를 수정·삭제하지 않고 같은 eventID 에 오류 선언을 붙인 이벤트로 정정하는 방식이다. [사실][^ref-581]
- **[행동 의존 그래프(Action Dependency Graph, ADG)](../../glossary/action-dependency-graph.md)** — 다중 로봇 계획의 로봇 간 순서와 운동 제약을 그래프로 인코딩해 지연이 생겨도 충돌 없이 실행하게 하는 표현이다. [사실][^ref-188]
- **업무 연속성 관리 시스템(Business Continuity Management System, BCMS)** — 교란 사건에 대비하고 복구를 보장하기 위한 관리 체계로, ISO 22301 이 요구사항을 정한다. [사실][^ref-575]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [11. 분산 시스템·통신·컴퓨팅 구조](../../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-188]: Hönig, W., Kiesel, S., Tinka, A., Durham, J. W., & Ayanian, N., Persistent and Robust Execution of MAPF Schedules in Warehouses, 2019-04, https://ieeexplore.ieee.org/abstract/document/8620328/, 접근일 2026-09-25 (원문 미열람)
[^ref-575]: ISO, ISO 22301:2019 - Security and resilience — Business continuity management systems — Requirements, 2019, https://www.iso.org/standard/75106.html, 접근일 2026-09-25 (원문 미열람)
[^ref-578]: Microsoft (MicrosoftDocs/architecture-center), Compensating Transaction pattern, 2026-04-16, https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction, 접근일 2026-09-25
[^ref-581]: GS1, EPC Information Services (EPCIS) Standard 1.2, 2016-09-29, https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-50 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-50 | 20. 예외 복구·재계획·업무 연속성 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-25-50/pages/topics/2026/2026-09-25-area20-s11.md

```markdown
---
title: "20. 예외 복구·재계획·업무 연속성 — 열린 질문"
type: topic
category: "E. 협업·현장 운영"
primary_area_no: 20
related_areas: [1, 7, 9, 11, 12, 13, 15, 18, 19, 22]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-578, ref-581, ref-374]
last_run: 2026-09-25
version: 1
split_from: docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#11
---

[홈](../../index.md) › [주제](../index.md) › 20. 예외 복구·재계획·업무 연속성 — 열린 질문

# 20. 예외 복구·재계획·업무 연속성 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 화물 회수 뒤 재고 확인 기준, 국내 수동·제한 운영 전환 기준, 제한 운영 처리량 추정이 새로 열렸고, 기존 네 질문은 부분 근거만 있어 열림 상태를 유지한다. [의견]
- 이 페이지는 [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

화물 회수 뒤 재고 확인 기준, 국내 수동·제한 운영 전환 기준, 제한 운영 처리량 추정이 새로 열렸고, 기존 네 질문은 부분 근거만 있어 열림 상태를 유지한다. [의견]

- **oq-003** (상태: 열림) 로봇·게이트의 바코드·RFID 판독 실패나 오판독이 생기면 인계 확정을 보류·재스캔·사람 확인 중 어떤 기준으로 처리해야 하는가? — EPCIS 1.2 오류 선언은 정정 수단일 뿐 판단 기준의 답은 아니다. [의견][^ref-581]
- **oq-021** (상태: 열림) 로봇이 이미 화물을 싣거나 옮긴 뒤 상위 시스템이 주문을 취소·변경하면 되돌림 작업과 재고 반영을 누가 어떤 규칙으로 정하는가(국내 물류센터 사례 포함)? — 보상 트랜잭션 패턴은 설계 원칙만 준다. [의견][^ref-578]
- **oq-038** (상태: 열림) 외부망이 끊겨 클라우드 WMS 와 단절된 동안 현장 ROP 가 이미 받은 주문·작업을 어디까지 계속 실행하고, 재연결 뒤 재고·완료 기록을 어떻게 맞추는지 정한 국내 물류센터 운영 기준이나 사례가 있는가? — VDA 5050 의 마지막 해제 노드 규칙은 로봇–관제 구간의 부분 근거다. [추정][^ref-031]
- **oq-048** (상태: 열림) Open-RMF 플릿 어댑터 재시작 시 작업 유실을 막는 작업 백업·복원 기능(SQLite 저장 제안)이 현재 배포판에 반영되었는가, 반영되었다면 복원 뒤 로봇의 실제 위치·적재 상태와 어떻게 대조하는가? — 이슈 224 의 제안만 확인했고 반영 여부는 미확인이다. [사실][^ref-374]
- (신규, 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-50) 운반 중 고장 난 로봇에 실린 화물을 사람이나 다른 로봇이 회수할 때 어떤 확인(스캔·무게·위치)으로 재고 위치를 바로잡는지 정한 운영 기준이나 국내 사례가 있는가?
- (신규, 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-50) 국내 물류센터가 로봇·관제 장애 때 수동 운영이나 제한 운영으로 전환하는 기준(허용 중단 시간, 전환·복귀 절차)을 BCP 에 정한 사례가 있는가?
- (신규, 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-50) 로봇 일부가 멈춘 제한 운영 상태의 처리량 저하를 미리 추정해 전환 결정에 쓰는 방법이나 사례가 있는가?

전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [11. 분산 시스템·통신·컴퓨팅 구조](../../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-578]: Microsoft (MicrosoftDocs/architecture-center), Compensating Transaction pattern, 2026-04-16, https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction, 접근일 2026-09-25
[^ref-581]: GS1, EPC Information Services (EPCIS) Standard 1.2, 2016-09-29, https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-374]: Open Robotics (open-rmf/rmf_ros2), Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2, 미확인, https://github.com/open-rmf/rmf_ros2/issues/224, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-50 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-50 | 20. 예외 복구·재계획·업무 연속성 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-25-50/pages/topics/2026/2026-09-25-area20-s7.md

```markdown
---
title: "20. 예외 복구·재계획·업무 연속성 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "E. 협업·현장 운영"
primary_area_no: 20
related_areas: [1, 7, 9, 11, 12, 13, 15, 18, 19, 22]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-004, ref-031, ref-051, ref-537, ref-575, ref-576, ref-577, ref-578, ref-581]
last_run: 2026-09-25
version: 1
split_from: docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#7
---

[홈](../../index.md) › [주제](../index.md) › 20. 예외 복구·재계획·업무 연속성 — 관련 표준·프레임워크·오픈소스

# 20. 예외 복구·재계획·업무 연속성 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 예외 동작 자체는 VDA 5050·Open-RMF 가 정의하고, 업무 연속성 표준과 국내 제도는 현장 제한 운영·수동 전환 계획의 참조 틀(연계 대상)로 쓴다. [추정][^ref-031][^ref-575]
- 이 페이지는 [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

예외 동작 자체는 VDA 5050·Open-RMF 가 정의하고, 업무 연속성 표준과 국내 제도는 현장 제한 운영·수동 전환 계획의 참조 틀(연계 대상)로 쓴다. [추정][^ref-031][^ref-575]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| [VDA 5050](../../glossary/vda-5050.md) (3.0.0) | 표준 | cancelOrder·startPause·연결 상태·오류 수준·loads 로 고장·단절·취소를 표현한다. [사실] | [^ref-031][^ref-051] |
| [Open-RMF](../../glossary/open-rmf.md) ([플릿 어댑터](../../glossary/fleet-adapter.md) rmf_ros2) | 오픈소스 | 중단·재개·취소·재계획 요청·작업 수락 중지·이슈 생성, 교통 스케줄 협상을 제공한다. [사실] | [^ref-537][^ref-004] |
| ISO 22301:2019 기준(개정 1:2024 별도) | 표준 | 교란 사건으로부터 보호하고 복구를 보장하기 위한 BCMS 의 수립·운영·점검·개선 요구사항을 정한다. 현장에는 참조 틀이다. [사실] | [^ref-575] |
| 기업재난관리표준·재해경감 우수기업 인증 | 평가 프로그램 | 「재해경감을 위한 기업의 자율활동 지원에 관한 법률」에 따라 행정안전부가 표준을 고시하고, 재해경감활동관리체계를 갖춘 기업을 문서평가·현장평가를 거쳐 인증한다. [사실] | [^ref-576] |
| 중소규모 사업장 기능연속성계획(BCP) 수립 가이드 | 프레임워크 | 고용노동부가 2022년 오미크론 확산기에 안내한 감염병 대응 권고 가이드로, 사업 우선순위 파악부터 위험성 분석·피해 최소화·분야별 대응·수립·시행·공유·점검까지 7단계다. [사실] | [^ref-577] |
| 보상 트랜잭션 패턴 | 프레임워크 | 실패한 다단계 작업의 보정·재개 설계 원칙. [사실] | [^ref-578] |
| GS1 EPCIS 1.2 | 표준 | 오류 선언으로 이벤트 기록을 정정한다. [사실] | [^ref-581] |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [11. 분산 시스템·통신·컴퓨팅 구조](../../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-537]: Open Robotics (open-rmf/rmf_ros2), rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 접근일 2026-09-25
[^ref-575]: ISO, ISO 22301:2019 - Security and resilience — Business continuity management systems — Requirements, 2019, https://www.iso.org/standard/75106.html, 접근일 2026-09-25 (원문 미열람)
[^ref-576]: 행정안전부, 재해경감 우수기업 인증제도, 미확인, https://www.mois.go.kr/frt/sub/a06/b10/disasterMitigationCompanies/screen.do, 접근일 2026-09-25 (원문 미열람)
[^ref-577]: 고용노동부, 중소규모 사업장 기능연속성계획(BCP) 수립 가이드 안내, 2022-03, https://www.moel.go.kr/news/notice/noticeView.do?bbs_seq=20220301591, 접근일 2026-09-25 (원문 미열람)
[^ref-578]: Microsoft (MicrosoftDocs/architecture-center), Compensating Transaction pattern, 2026-04-16, https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction, 접근일 2026-09-25
[^ref-581]: GS1, EPC Information Services (EPCIS) Standard 1.2, 2016-09-29, https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-50 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-50 | 20. 예외 복구·재계획·업무 연속성 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-25-50/pages/topics/2026/2026-09-25-area20-s10.md

```markdown
---
title: "20. 예외 복구·재계획·업무 연속성 — 다른 연구영역과의 연결"
type: topic
category: "E. 협업·현장 운영"
primary_area_no: 20
related_areas: [1, 7, 9, 11, 12, 13, 15, 18, 19, 22]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-004, ref-031, ref-051, ref-188, ref-251, ref-537, ref-572, ref-573, ref-578, ref-581, ref-374]
last_run: 2026-09-25
version: 1
split_from: docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#10
---

[홈](../../index.md) › [주제](../index.md) › 20. 예외 복구·재계획·업무 연속성 — 다른 연구영역과의 연결

# 20. 예외 복구·재계획·업무 연속성 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 예외 복구는 명령 실행 보장, 재배정·재계획, 모니터링, 사람 개입, 재고 정정을 맡는 영역과 맞물린다. [추정][^ref-031]
- 이 페이지는 [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

예외 복구는 명령 실행 보장, 재배정·재계획, 모니터링, 사람 개입, 재고 정정을 맡는 영역과 맞물린다. [추정][^ref-031]

- [1. 주문·업무 시스템 연계](../a-business-supply-chain-design/01-order-and-business-system-integration.md) — 이미 옮긴 화물의 주문이 취소될 때의 보상·되돌림 규칙(oq-021)이 상위 시스템과의 약속 문제다. [추정][^ref-578]
- [7. 화물·재고·자산 식별과 추적](../b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) — 로봇의 loads 보고와 EPCIS 오류 선언이 고장 화물 식별·재고 정정의 근거다(oq-003). [사실][^ref-051][^ref-581]
- [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — 연동 수준(전체 제어·신호등·읽기 전용)이 쓸 수 있는 복구 수단을 정한다. [사실][^ref-251][^ref-004]
- [11. 분산 시스템·통신·컴퓨팅 구조](../c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) — 라스트 윌 기반 단절 감지와 단절 동안의 계속 운행 범위(oq-038). [추정][^ref-031]
- [12. 명령·작업 실행의 신뢰성](../c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) — 취소 상태 보고와 어댑터 재시작 시 작업 유실(oq-048). [사실][^ref-031][^ref-374]
- [13. 작업 배정 — MRTA](../d-planning-and-optimization/13-task-allocation-mrta.md) — 고장 복구를 포함한 재배정. [사실][^ref-573]
- [15. 다중 로봇 경로·교통 관리 — MAPF](../d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) — 교통 스케줄 협상, 지연에 강건한 실행과 통과 순서 재스케줄. [사실][^ref-004][^ref-188][^ref-572]
- [18. 사람–로봇 협업·운영 인터페이스](18-human-robot-collaboration-and-operator-interface.md) — RETRIABLE 상태의 운영자 개입과 영향이 큰 결정의 사람 참여. [사실][^ref-031][^ref-578]
- [19. 모니터링·이상 탐지·원인 분석](19-monitoring-anomaly-detection-and-root-cause-analysis.md) — 오류 수준 보고와 이슈 생성이 복구 결정의 입력이다. [사실][^ref-051][^ref-537]
- [22. 시뮬레이션·예측용 디지털 트윈](../f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) — 로봇 일부가 멈춘 제한 운영의 처리량을 가정해 실험하는 일은 이 영역의 몫으로 넘긴다(11절 새 질문). [의견]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [11. 분산 시스템·통신·컴퓨팅 구조](../../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-188]: Hönig, W., Kiesel, S., Tinka, A., Durham, J. W., & Ayanian, N., Persistent and Robust Execution of MAPF Schedules in Warehouses, 2019-04, https://ieeexplore.ieee.org/abstract/document/8620328/, 접근일 2026-09-25 (원문 미열람)
[^ref-251]: Open Robotics, Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration), 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-09-25
[^ref-537]: Open Robotics (open-rmf/rmf_ros2), rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp, 접근일 2026-09-25
[^ref-572]: Feng, Y., Paul, A., Chen, Z., & Li, J., A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution, 2024, https://arxiv.org/abs/2403.18145, 접근일 2026-09-25 (원문 미열람)
[^ref-573]: Kalempa, V. C., Piardi, L., Limeira, M., & de Oliveira, A. S., Multi-Robot Preemptive Task Scheduling with Fault Recovery: A Novel Approach to Automatic Logistics of Smart Factories, 2021-09-30, https://www.mdpi.com/1424-8220/21/19/6536, 접근일 2026-09-25 (원문 미열람)
[^ref-578]: Microsoft (MicrosoftDocs/architecture-center), Compensating Transaction pattern, 2026-04-16, https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction, 접근일 2026-09-25
[^ref-581]: GS1, EPC Information Services (EPCIS) Standard 1.2, 2016-09-29, https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-374]: Open Robotics (open-rmf/rmf_ros2), Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2, 미확인, https://github.com/open-rmf/rmf_ros2/issues/224, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-50 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-50 | 20. 예외 복구·재계획·업무 연속성 의 "다른 연구영역과의 연결" 절에서 분리 |
```


## 형식 검증 오류 (재작성)

직전 원고(runs/<run_id>/pages.json, pages/)가 코드 형식 검증(pipeline/validate_run.py)을 통과하지 못했다. 내용(주장·태그·각주·판정)은 바꾸지 말고 아래 형식 오류만 고친 전체 pages.json 을 다시 반환한다. 차등 갱신 실행이면 patches 로, 아니면 content 로 보낸다.

- 퍼블리셔 사전 검사: [publish] 원복: 4단계 링크·각주 검사 실패 — docs/data/config/tracks/mkdocs.yml/inbox/corrections.md 를 스냅숏으로 되돌렸다
- 퍼블리셔 사전 검사: [publish] 실패: 4단계 내부 링크·각주 검사 실패:
- 퍼블리셔 사전 검사: - topics/2026/2026-09-25-area20-s10.md: 깨진 링크 ../a-business-supply-chain-design/01-order-and-business-system-integration.md
- 퍼블리셔 사전 검사: - topics/2026/2026-09-25-area20-s10.md: 깨진 링크 ../b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md
- 퍼블리셔 사전 검사: - topics/2026/2026-09-25-area20-s10.md: 깨진 링크 ../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md
- 퍼블리셔 사전 검사: - topics/2026/2026-09-25-area20-s10.md: 깨진 링크 ../c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md
- 퍼블리셔 사전 검사: - topics/2026/2026-09-25-area20-s10.md: 깨진 링크 ../c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md
- 퍼블리셔 사전 검사: - topics/2026/2026-09-25-area20-s10.md: 깨진 링크 ../d-planning-and-optimization/13-task-allocation-mrta.md
- 퍼블리셔 사전 검사: - topics/2026/2026-09-25-area20-s10.md: 깨진 링크 ../d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md
- 퍼블리셔 사전 검사: - topics/2026/2026-09-25-area20-s10.md: 깨진 링크 18-human-robot-collaboration-and-operator-interface.md
- 퍼블리셔 사전 검사: - topics/2026/2026-09-25-area20-s10.md: 깨진 링크 19-monitoring-anomaly-detection-and-root-cause-analysis.md
- 퍼블리셔 사전 검사: - topics/2026/2026-09-25-area20-s10.md: 깨진 링크 ../f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md
