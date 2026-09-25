(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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
- verification_stage: second
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

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
      "diff_summary": "자동 분리: 20. 예외 복구·재계획·업무 연속성 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(736자)을 옮겼다. 본문 링크를 주제 페이지 기준 경로(../../categories/…)로 고침"
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
        "docs/topics/2026/2026-09-25-area20-s6.md",
        "docs/topics/2026/2026-09-25-area20-s10.md"
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
        "docs/topics/2026/2026-09-25-area20-s7.md"
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
        "docs/topics/2026/2026-09-25-area20-s6.md",
        "docs/topics/2026/2026-09-25-area20-s10.md",
        "docs/topics/2026/2026-09-25-area20-s11.md"
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
    "ref-188 중복 방지 — 브리프의 ref-188 을 기존 ref-188(같은 논문·같은 URL)로 통합해 f11 을 쓴 4·6·8·10절 각주와 13절 정의, reference_updates 모두 기존 ref-188 로 두고 새로 등록하지 않았다.",
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
    "원문 미열람 표시 — ref-188·572·573·574·575·576·577·579·580·581·374 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-576·579·374 의 발행일 자리에 '미확인'을 썼다.",
    "열린 질문 상태 — 11절에서 oq-003·oq-021·oq-038·oq-048 을 모두 '열림'으로 두고 부분 근거로만 적었으며 open_question_updates 에 해결로 내지 않았다.",
    "분량 초과 자동 분리: 20. 예외 복구·재계획·업무 연속성 본문 8,408자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,648자",
    "형식 검증 재작성: docs/topics/2026/2026-09-25-area20-s10.md 3절의 세부영역 링크 10개를 주제 페이지 위치 기준 경로(../../categories/<대분류 slug>/<파일>.md)로 고쳤고, 세부영역 페이지 프런트매터 sources 를 13절 각주 정의(14건)와 일치시켰다. 주장·태그·각주 내용은 바꾸지 않았다."
  ]
}
```

### runs/2026-09-25-50/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
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
sources: [ref-004, ref-031, ref-051, ref-188, ref-537, ref-572, ref-573, ref-574, ref-575, ref-576, ref-578, ref-579, ref-580, ref-581]
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

- [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) — 이미 옮긴 화물의 주문이 취소될 때의 보상·되돌림 규칙(oq-021)이 상위 시스템과의 약속 문제다. [추정][^ref-578]
- [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) — 로봇의 loads 보고와 EPCIS 오류 선언이 고장 화물 식별·재고 정정의 근거다(oq-003). [사실][^ref-051][^ref-581]
- [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — 연동 수준(전체 제어·신호등·읽기 전용)이 쓸 수 있는 복구 수단을 정한다. [사실][^ref-251][^ref-004]
- [11. 분산 시스템·통신·컴퓨팅 구조](../../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) — 라스트 윌 기반 단절 감지와 단절 동안의 계속 운행 범위(oq-038). [추정][^ref-031]
- [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) — 취소 상태 보고와 어댑터 재시작 시 작업 유실(oq-048). [사실][^ref-031][^ref-374]
- [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md) — 고장 복구를 포함한 재배정. [사실][^ref-573]
- [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) — 교통 스케줄 협상, 지연에 강건한 실행과 통과 순서 재스케줄. [사실][^ref-004][^ref-188][^ref-572]
- [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) — RETRIABLE 상태의 운영자 개입과 영향이 큰 결정의 사람 참여. [사실][^ref-031][^ref-578]
- [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) — 오류 수준 보고와 이슈 생성이 복구 결정의 입력이다. [사실][^ref-051][^ref-537]
- [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) — 로봇 일부가 멈춘 제한 운영의 처리량을 가정해 실험하는 일은 이 영역의 몫으로 넘긴다(11절 새 질문). [의견]

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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 481건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 122개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- distributed-tracing: 분산 추적 (Distributed Tracing)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- eclass: ECLASS (ECLASS)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
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
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
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

### docs/open-questions.md (요약: 대상 영역 [20] 에 걸린 5건 / 전체 75건)

```markdown
- oq-003 [열림] 로봇·게이트의 바코드·RFID 판독 실패나 오판독이 생기면 인계 확정을 보류·재스캔·사람 확인 중 어떤 기준으로 처리해야 하는가? (영역 7, 20)
- oq-021 [열림] 로봇이 이미 화물을 싣거나 옮긴 뒤 상위 시스템이 주문을 취소·변경하면 되돌림 작업과 재고 반영을 누가 어떤 규칙으로 정하는가(국내 물류센터 사례 포함)? (영역 1, 20)
- oq-038 [열림] 외부망이 끊겨 클라우드 WMS 와 단절된 동안 현장 ROP 가 이미 받은 주문·작업을 어디까지 계속 실행하고, 재연결 뒤 재고·완료 기록을 어떻게 맞추는지 정한 국내 물류센터 운영 기준이나 사례가 있는가? (영역 11, 1, 20)
- oq-048 [열림] Open-RMF 플릿 어댑터 재시작 시 작업 유실을 막는 작업 백업·복원 기능(SQLite 저장 제안)이 현재 배포판에 반영되었는가, 반영되었다면 복원 뒤 로봇의 실제 위치·적재 상태와 어떻게 대조하는가? (영역 12, 20)
- oq-075 [열림] 국내 물류센터에서 로봇 정지·지연의 원인별 발생 비율이나 이상 대응 시간을 실측해 공개한 자료가 있는가? (영역 19, 20)
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
