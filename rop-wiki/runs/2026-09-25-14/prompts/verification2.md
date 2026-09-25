(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-14
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 4. 성과·경제성·프로세스 개선 (A. 업무·공급망 설계)
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

### runs/2026-09-25-14/target.json

```json
{
  "run_id": "2026-09-25-14",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 14,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 4,
    "area_name": "4. 성과·경제성·프로세스 개선",
    "category": "A. 업무·공급망 설계",
    "category_letter": "A"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=4"
}
```

### runs/2026-09-25-14/research.json

```json
{
  "run_id": "2026-09-25-14",
  "date": "2026-09-25",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 4,
    "area_name": "4. 성과·경제성·프로세스 개선",
    "category": "A. 업무·공급망 설계"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음",
    "섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음",
    "섹션 6. 대표 접근법과 기술 비어 있음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 용어집 SCOR 항목만 이 영역에 연결됨",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-008, oq-011 있음, 정정 요청 없음"
  ],
  "research_questions": [
    "로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? [분류원문]",
    "납기 준수율·처리량·리드타임·가동률 같은 성과 지표를 정의하는 표준·벤치마크(ISO 22400, SCOR, WERC DC Measures)는 무엇이며 각각 어떤 지표를 어떻게 정의하는가? (섹션 4·7 겨냥)",
    "처리량·재공품·리드타임의 관계와 병목을 찾는 방법(리틀의 법칙, 활성 구간 기반 병목 탐지, 프로세스 마이닝)은 무엇인가? (섹션 4·6 겨냥)",
    "로봇 창고 연구는 로봇 수·작업대·충전·에너지·운영 규칙이 처리량과 비용에 주는 영향을 어떻게 평가했는가? (섹션 5·6·8 겨냥)",
    "ROP가 쌓는 실행 기록(로봇 상태, 작업 상태)으로 어떤 성과 지표를 계산할 수 있고, 무엇은 상위 업무 시스템 데이터가 있어야 하는가? (섹션 9·10 겨냥)",
    "oq-011 스마트물류센터 인증의 세부 평가 기준에 성과관리·설비 지표가 어떻게 들어가는가, 국내 물류 로봇 도입의 투자 효과 자료는 무엇이 있는가? (한국 자료 우선, 섹션 3·8·11 겨냥)",
    "oq-008 여러 거점 간 로봇 재배치·성수기 임대 보충의 경제성을 다룬 학술·공공 자료가 있는가? (섹션 11 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "ISO 22400-2:2014는 제조 운영 관리용 핵심성과지표(KPI)를 공식·구성 요소·시간 특성·단위와 함께 정의하며, 처리율(throughput rate), 가동 효율, 종합설비효율(OEE), 가용성, 품질률, 재고 회전율, 평균 고장 간격·수리 시간 등 30여 개 지표를 담는다.",
      "tag": "사실",
      "source_ids": [
        "ref-139"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: specifies a selected number of KPIs ... by means of their formula and corresponding elements, their time behaviour, their unit/dimension. Part 2 는 34개 KPI 정의로 요약됨(개수는 제3자 요약). 원문 미열람.",
      "as_of": "2014",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f2",
      "claim": "ISO 22400-2에서 종합설비효율(OEE)은 가용성·효과성(성능)·품질률의 곱으로 정의되고 계획 가동 시간(PBT) 같은 시간 상태 모델을 기준으로 계산되며, 2부의 개정안(ISO/DIS 22400-2)이 진행 중이다.",
      "tag": "사실",
      "source_ids": [
        "ref-139"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: OEE = Availability x Effectiveness x Quality Ratio; Planned busy time(PBT). ISO 사이트에 ISO/DIS 22400-2(표준 번호 87563) 페이지가 별도로 있음. 원문 미열람.",
      "as_of": "2014",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f3",
      "claim": "Computers & Industrial Engineering(2020) 게재 논문은 ISO 22400의 OEE 정의가 판마다 서로 어긋나고 나카지마의 TPM 원래 정식화와도 달라 불완전하다고 평가하고, 둘을 맞추는 암묵적 가정을 제시했다.",
      "tag": "의견",
      "source_ids": [
        "ref-142"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: ISO 22400 standard OEE ... versions seem inconsistent ... differs from established scientific literature; the standard appears to be incomplete. CIE 145, 106518. 원문 미열람.",
      "as_of": "2020",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f4",
      "claim": "ASCM SCOR의 완전 고객 주문 이행률(RL.1.1 Perfect Customer Order Fulfillment)은 완전 주문 수를 전체 주문 수로 나눈 비율이며, 주문의 모든 품목 줄이 완전해야 완전 주문으로 보고, 하위 지표로 완납 주문 비율(RL.2.1), 최초 약속일 대비 납기 성과(RL.2.2), 주문 문서 정확도(RL.2.3), 무손상 상태(RL.2.4)를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-140"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: (Total perfect orders / Total number of orders) x 100%, an order is perfect if the individual line items making up that order are all perfect; RL.2.1~RL.2.4. scor.ascm.org 원문 미열람. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f5",
      "claim": "SCOR의 대표 성과 지표는 신뢰성(완전 주문 이행), 대응성(주문 이행 사이클 타임), 비용(공급망 관리 총비용) 같은 성과 속성별로 나뉘어, 로봇 운영 지표보다 상위의 주문·공급망 단위 성과를 잰다.",
      "tag": "사실",
      "source_ids": [
        "ref-001",
        "ref-140"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: headline metrics include Perfect Order Fulfillment (reliability), Order Fulfillment Cycle Time (responsiveness), Total Supply Chain Management Cost (cost). 두 출처 모두 ASCM이라 독립 교차 아님. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f6",
      "claim": "WERC DC Measures 연례 조사는 물류센터 운영자가 꼽는 주요 지표로 정시 출하율, 평균 창고 용량 사용률, 주문 피킹 정확도, 입고–적치 소요 시간(dock-to-stock cycle time)을 다루며, 2026년 보고서는 주문 피킹 정확도를 품질 지표로 명시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-141"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: most important DC metrics, including on-time shipments, average warehouse capacity used, order picking accuracy and dock-to-stock cycle time. 벤치마크 수치는 2차 요약 경유라 넣지 않음. 원문 미열람.",
      "as_of": "2025",
      "flow_step": "입고",
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f7",
      "claim": "리틀의 법칙(Little's Law)은 재공품(WIP) = 처리량(TH) × 사이클 타임(CT)의 관계이며, Hopp·Spearman의 팩토리 피직스는 병목 속도에서 최대 처리량을 내는 임계 재공품(critical WIP)을 넘으면 처리량은 늘지 않고 대기 때문에 사이클 타임만 길어진다고 본다.",
      "tag": "사실",
      "source_ids": [
        "ref-143"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: WIP = TH × CT; Critical WIP (W0) ... Any WIP above this critical level would not result in additional throughput, but rather increases cycle time. 원문 미열람. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "리틀의 법칙과 RMFS 대기행렬 연구를 함께 보면, 작업대·포장대 같은 병목의 처리 속도를 넘어 로봇 작업을 더 투입하면 로봇 가동률은 올라가도 출하 처리량은 늘지 않고 주문 사이클 타임만 길어질 수 있어, 로봇 가동률 상승이 곧 출하량 증가를 뜻하지 않을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-143",
        "ref-096",
        "ref-097"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f7(임계 재공품 이상에서 처리량 정체)과 f9(작업대 위치·가동률이 처리량을 좌우), RMFS 스테이션 비율 연구(재인용: 2026-09-25-10)를 분류 원문 SCM 질문에 대응시킨 추론.",
      "as_of": "2026-09-25",
      "flow_step": "피킹",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f9",
      "claim": "Lamballais·Roy·de Koster(2017)의 RMFS 대기행렬 모델은 최대 주문 처리량·평균 주문 사이클 타임·로봇 가동률을 함께 추정하며, 처리량은 보관 구역 둘레의 작업대 위치에 영향을 받았다.",
      "tag": "사실",
      "source_ids": [
        "ref-096"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: queueing network models ... estimate maximum order throughput, average order cycle time, and robot utilization; affected by the location of the workstations. EJOR 256. (재인용: 2026-09-25-10)",
      "as_of": "2017",
      "flow_step": "피킹",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "Ghelichi·Kilaru(2021)는 협업형 AMR 피킹 방식 두 가지(라스트 마일 배송형 LMD, 통로 만남형 MIA)의 해석적 모델을 세워, 처리율·피킹 구역 크기·클러스터 크기가 성과를 가장 크게 좌우하고, 피킹 주기가 높을 때 LMD가 필요한 로봇 수를 줄이며 MIA는 로봇이 더 필요하지만 작업자 참여를 높인다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-145"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: Throughput rate, picking area and cluster size are the most decisive factors; LMD outperform MIA at higher pick cycles, reducing the required number of robots; MIA requires more robots but improve picker engagement. Applied Mathematical Modelling. 원문 미열람.",
      "as_of": "2021",
      "flow_step": "피킹",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "Azadeh·de Koster·Roy(2019)의 리뷰는 로봇형 처리 시스템(셔틀 기반 저장·반출, 컴팩트 저장, RMFS 등)이 공간을 적게 쓰고 수요 변동에 유연하며 24시간 운영할 수 있다고 정리하고, 연구를 시스템 분석·설계 최적화·운영 계획·통제로 나누면서 많은 신규 시스템이 학술적으로 거의 연구되지 않았다고 지적했다.",
      "tag": "사실",
      "source_ids": [
        "ref-144"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: require little space, provide flexibility in managing varying demand requirements, and are able to work 24/7; system analysis, design optimization, and operations planning and control. Transportation Science 53(4) 917-945. 원문 미열람.",
      "as_of": "2019",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f12",
      "claim": "Omega(2024) 게재 RMFS 에너지 연구는 일반·긴급 주문의 동적 우선순위 정책을 평가해 처리량과 에너지 소비 사이에 절충이 있음을 보이고, 제안한 우선순위 규칙이 선착순(FCFS) 대비 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-146"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: trade-off between order throughput and energy consumption; proposed priority rule reduces energy consumption by 3.41% and increases throughput by 26.07% compared to FCFS. 모델·시뮬레이션 조건의 값이며 현장 실측 아님. 원문 미열람.",
      "as_of": "2024",
      "flow_step": "피킹",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "충전 설비 결정은 비용과 처리 시간의 절충으로 연구되어, RMFS에서는 배터리 비용이 낮으면 배터리 교환이 플러그인 충전보다 저렴했고, AMR 물류센터 시뮬레이션에서는 충전기가 부족하면 큰 지연이, 과잉이면 불필요한 비용이 생겼다.",
      "tag": "사실",
      "source_ids": [
        "ref-098",
        "ref-102"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: battery swapping is cheaper than plug-in charging when battery costs are low(EJOR 267(2)); insufficient chargers led to significant system delays, whereas excessive capacity added unnecessary costs(FAIM 2025). 두 출처는 서로 다른 부분을 뒷받침. (재인용: 2026-09-25-10)",
      "as_of": "2025",
      "flow_step": "적치",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f14",
      "claim": "처리량 병목 탐지 문헌에서 활성 구간 방법(Roser 외 2001)은 중단 없이 가장 오래 가동 중인 자원을 순간 병목으로 보고, 병목을 순간·평균·이동(shifting) 병목으로 구분하며, 버퍼 재고와 결합해 병목 이동을 예측하는 데까지 확장되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-115"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: the process with the longest active period is the bottleneck ... three types of throughput bottleneck: momentary, average, and shifting. Production & Manufacturing Research 체계적 리뷰(2023). 원문 미열람.",
      "as_of": "2023",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f15",
      "claim": "활성 구간 방법은 자원별 가동·유휴 시각 기록만으로 계산되므로, ROP가 수집하는 로봇 상태(작업 중·유휴·충전·오류) 기록과 작업대·승강기 이벤트를 쓰면 로봇·작업대·설비 가운데 이동하는 병목을 찾는 데 적용할 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-115",
        "ref-148"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f14(활성 구간 정의)와 f16(robot_state 상태 값·시각)을 대응시킨 추론. 제조 라인 중심 방법이며 이동 로봇·작업대 혼합 창고에 적용한 사례는 확인하지 못함.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f16",
      "claim": "Open-RMF API의 로봇 상태 스키마(robot_state)는 로봇 상태를 uninitialized, offline, shutdown, idle, charging, working, error 일곱 값으로 두고, 배터리 충전 상태(0.0~1.0), 현재 작업 id, 운영자가 조치할 문제(issues), 위치, 시각(unix_millis_time)을 함께 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-148"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 status enum: uninitialized, offline, shutdown, idle, charging, working, error; battery \"State of charge of the battery. Values range from 0.0 (depleted) to 1.0\". (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f17",
      "claim": "Open-RMF API의 작업 상태 스키마(task_state)는 작업 시작·종료 시각(unix_millis_start_time, unix_millis_finish_time), 최초 예상 소요 시간과 현재 예상 소요 시간(original_estimate_millis, estimate_millis), 12개 상태 값, 배정 로봇, 단계, 중단·취소·강제 종료 정보를 담는다.",
      "tag": "사실",
      "source_ids": [
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 필드: unix_millis_start_time, unix_millis_finish_time, original_estimate_millis·estimate_millis \"An estimate, in milliseconds, of how long the subject will take to complete\", interruptions, cancellation, killed. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f18",
      "claim": "로봇·작업 상태 기록으로 로봇 가동률(작업 중 시간 비율), 충전·오류 시간 비율, 작업 사이클 타임과 예상 대비 편차, 취소·실패 비율 같은 운영 지표는 ROP 안에서 계산할 수 있으나, 완전 주문 이행률·주문 이행 사이클 타임 같은 주문 단위 지표는 WMS·ERP의 주문 데이터와 연결해야 계산될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-111",
        "ref-148",
        "ref-140"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f16·f17(로봇·작업 상태 필드에 주문·품목 줄 정보 없음)과 f4(완전 주문은 주문의 모든 품목 줄 기준)를 대응시킨 추론.",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f19",
      "claim": "PM4Py는 Fraunhofer FIT에서 분사한 Process Intelligence Solutions가 관리하는 오픈소스 파이썬 프로세스 마이닝 라이브러리로, 프로세스 발견 등 알고리즘을 제공하고 객체 중심 이벤트 로그(OCEL)를 선택 기능으로 두며, 공개판은 AGPL-3.0이고 상용 라이선스를 별도로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-147"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README 원문: \"PM4Py is a python library that supports state-of-the-art process mining algorithms in Python.\" OCEL 2.0 전면 지원은 검색 요약에만 있어 주장에 넣지 않음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "창고 업무 개선을 위한 프로세스 마이닝 사례 연구는 SAP 창고 관리 모듈 테이블에서 이벤트 로그를 뽑아 ProM의 Heuristic Miner로 분석했고, 병목 분석에서 자재가 고층 랙에 오래 머물고 고층 랙 사이를 옮겨 다니는 흐름을 찾았다.",
      "tag": "사실",
      "source_ids": [
        "ref-149"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: extracting activities from SAP Warehouse Management module tables ... Heuristic Miner Algorithm in PROM; material spent a long time in high racks and transferred between high racks. 원문 미열람.",
      "as_of": "2015",
      "flow_step": "적치",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "오토스토어가 발표한 경제성 연구는 국내 도입 기업 5곳이 3년간 시스템 도입 비용 87.4억 원 대비 약 156.7억 원의 경제적 효과, 순현재가치 약 69.2억 원, 투자 회수 18개월, ROI 79%를 거뒀다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-150"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 검색 요약 기준. 보관 면적 75% 절감, 피킹 오류 99% 감소 등 효과를 근거로 제시. 연구 수행 주체·방법론 미확인, 독립 출처 없음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과",
      "vendor_claim": true,
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "oq-011 관련: 스마트물류센터 인증은 기반영역에서 성과관리 체계를 평가하며, 세부 항목 판단 기준을 데이터 관리 기반 구축(5등급), 실시간 모니터링(4등급), 관리와 통제(3등급), 최적화(2등급), 자율운영(1등급)의 단계로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-106"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 세부항목 평가의 판단기준은 5등급 데이터 관리 기반 구축, 4등급 실시간 모니터링, 3등급 관리와 통제, 2등급 최적화, 1등급 자율운영. 로봇 대수·가동률 같은 개별 지표의 포함 여부는 여전히 미확인. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "박정수·안영효(2010)는 화주기업과 물류기업이 공동으로 핵심성과지표(KPI)를 관리하는 방법을 다루며, 경영환경 변화에 대응하려면 KPI를 분석해 빠르게 피드백하는 체계가 필요하다고 보았다.",
      "tag": "의견",
      "source_ids": [
        "ref-151"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KCI 검색 요약: 화주기업과 물류기업의 공동 핵심성과지표 관리방법, KPI를 분석하여 빠르게 피드백할 수 있는 메커니즘의 필요성. 유통경영학회지 게재. 원문 미열람.",
      "as_of": "2010",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f24",
      "claim": "연계 대상: 투자 수익률·순현재가치·회수 기간 같은 재무적 투자 평가와 원가 배분은 재무 등 상위 업무 영역의 몫이고, ROP는 그 입력이 되는 처리량·가동률·충전·예외 같은 실행 데이터를 제공하고 운영 규칙 변경의 효과를 측정하는 쪽을 맡는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-150",
        "ref-139",
        "ref-148"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f21(재무 지표 구성), f1(운영 관리 수준 KPI), f16(로봇 상태 데이터)과 분류 원문 9장 '상위 업무 시스템'(재무는 외부 연계) 경계를 대응시킨 추론.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f25",
      "claim": "분류 원문의 질문(로봇 가동률 상승이 출하량·비용 개선으로 이어졌는가)에 답하려면 같은 기간의 로봇 운영 지표(가동률·충전·오류 시간)와 주문 단위 지표(완전 주문 이행률, 주문 이행 사이클 타임)와 비용을 함께 비교해야 하며, 처리량이 작업대 같은 공유 자원에 묶이는 연구 결과로 볼 때 가동률만으로는 판단할 수 없을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-096",
        "ref-140",
        "ref-148",
        "ref-143"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f4·f5(주문·비용 지표), f7·f8(재공품–처리량–사이클 타임), f9(작업대가 처리량 좌우), f16(가동률 원천 데이터)에서 도출한 추론. 이를 실증한 공개 사례는 찾지 못함.",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "예외·성과",
      "source_unopened": false
    }
  ],
  "sources": [
    {
      "id": "ref-001",
      "org": "ASCM",
      "title": "SCOR Digital Standard",
      "published": null,
      "url": "https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ASCM이 관리하는 공급망 운영 참조 모델(SCOR DS)의 공식 소개 페이지. 프로세스와 성과 지표 체계를 담는다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-096",
      "org": "Lamballais, T., Roy, D., & de Koster, M. B. M.",
      "title": "Estimating performance in a Robotic Mobile Fulfillment System",
      "published": "2017",
      "url": "https://repub.eur.nl/pub/107376/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RMFS의 대기행렬 네트워크 모델로 최대 처리량·사이클 타임·로봇 가동률을 추정하고 작업대 위치 영향을 분석한 EJOR 256 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-097",
      "org": "Lamballais, T., Roy, D., & de Koster, M. B. M.",
      "title": "Inventory allocation in robotic mobile fulfillment systems",
      "published": "2020",
      "url": "https://www.tandfonline.com/doi/abs/10.1080/24725854.2018.1560517",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 품목당 선반 수, 피킹·보충 스테이션 비율, 보충 수준이 RMFS 처리량에 주는 영향을 분석한 IISE Transactions 논문.",
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
      "summary": "원문 미열람. RMFS 로봇의 플러그인 충전·배터리 교환·유도 충전을 비용·처리 시간 측면에서 비교한 EJOR 267(2) 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-102",
      "org": "Springer(FAIM 2025 발표 논문, 저자 미확인)",
      "title": "Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics",
      "published": "2025",
      "url": "https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 물류센터 팔레트 이동 데이터로 AMR 대수와 충전기 수를 시뮬레이션으로 정하는 의사결정 지원 틀을 제시한 학술대회 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-106",
      "org": "한국교통연구원(인증스마트물류센터)",
      "title": "인증스마트물류센터",
      "published": null,
      "url": "https://cslc.koti.re.kr/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 국토교통부 스마트물류센터 인증제의 근거·평가 영역(기능영역·기반영역)·심사기준·등급을 안내하는 인증 운영 사이트.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-139",
      "org": "ISO",
      "title": "ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions",
      "published": "2014",
      "url": "https://www.iso.org/standard/54497.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 제조 운영 관리용 KPI의 공식·구성 요소·시간 특성·단위를 정의한 국제표준(처리율, OEE, 가용성, 품질률 등).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-140",
      "org": "ASCM",
      "title": "SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment",
      "published": null,
      "url": "https://scor.ascm.org/performance/reliability/RL.1.1",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. SCOR 신뢰성 성과 지표 완전 고객 주문 이행률의 정의·계산식·하위 지표 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-141",
      "org": "WERC(Warehousing Education and Research Council)",
      "title": "WERC DC Measures Survey - 2025",
      "published": "2025",
      "url": "https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 물류센터 운영 지표(정시 출하, 용량 사용률, 피킹 정확도, 입고–적치 소요 시간 등)를 조사해 벤치마크를 내는 협회 연례 보고서.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-142",
      "org": "Computers & Industrial Engineering 게재 논문(저자 미확인)",
      "title": "Overall Equipment Effectiveness: consistency of ISO standard with literature",
      "published": "2020",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0360835220302527",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ISO 22400의 OEE 정의가 판마다, 그리고 기존 문헌·실무와 어긋나는 점을 분석하고 정합을 위한 가정을 제시한 논문(CIE 145).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-143",
      "org": "Project Production Institute",
      "title": "Little’s Law – A Practical Approach to Understanding Production System Performance",
      "published": null,
      "url": "https://projectproduction.org/journal/littles-law-a-practical-approach-to-understanding-production-system-performance/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 리틀의 법칙과 팩토리 피직스의 임계 재공품 개념으로 처리량·재공품·사이클 타임 관계를 설명한 협회 저널 글.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-115",
      "org": "Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본)",
      "title": "Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes",
      "published": "2023",
      "url": "https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 제조 처리량 병목 탐지 방법(활성 구간 방법 등)과 운영 방식을 체계적으로 정리한 리뷰.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-144",
      "org": "Azadeh, K., de Koster, R., & Roy, D.",
      "title": "Robotized and Automated Warehouse Systems: Review and Recent Developments",
      "published": "2019",
      "url": "https://pubsonline.informs.org/doi/abs/10.1287/trsc.2018.0873",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 셔틀·컴팩트 저장·RMFS 등 로봇형·자동화 창고 시스템 연구를 분석·설계·운영으로 나눠 정리한 Transportation Science 리뷰.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-145",
      "org": "Ghelichi, Z., & Kilaru, S.",
      "title": "Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers",
      "published": "2021",
      "url": "https://www.sciencedirect.com/science/article/pii/S0307904X20305801",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 협업형 AMR 피킹 방식(LMD, MIA)의 성과를 해석적 모델로 비교한 Applied Mathematical Modelling 논문.",
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
      "summary": "원문 미열람. RMFS에서 일반·긴급 주문의 동적 우선순위 정책이 처리 시간과 에너지 소비에 주는 영향을 평가한 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-147",
      "org": "Process Intelligence Solutions (PM4Py GitHub)",
      "title": "pm4py — Official public repository for PM4Py (Process Mining for Python) (README)",
      "published": null,
      "url": "https://github.com/process-intelligence-solutions/pm4py",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "오픈소스 파이썬 프로세스 마이닝 라이브러리 PM4Py 공식 저장소 README. 관리 주체, 라이선스(AGPL-3.0·상용), 설치와 선택 기능(OCEL 등)을 안내한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/process-intelligence-solutions/pm4py/release/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-111",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF API 작업 상태 JSON 스키마. 작업 시작·종료 시각, 최초·현재 예상 소요 시간, 상태 12종, 배정 로봇, 단계, 중단·취소 정보를 정의한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_state.json",
      "source_unopened": false
    },
    {
      "id": "ref-148",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF API 로봇 상태 JSON 스키마. 상태 7종(유휴·충전·작업 중·오류 등), 배터리 충전 상태, 현재 작업 id, 문제 목록, 위치, 시각을 정의한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/robot_state.json",
      "source_unopened": false
    },
    {
      "id": "ref-149",
      "org": "Springer(학술대회 발표 논문, 저자 미확인)",
      "title": "Material Movement Analysis for Warehouse Business Process Improvement with Process Mining: A Case Study",
      "published": "2015",
      "url": "https://link.springer.com/chapter/10.1007/978-3-319-19509-4_9",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. SAP 창고 관리 모듈 데이터로 이벤트 로그를 만들어 프로세스 마이닝으로 창고 자재 이동의 병목을 분석한 사례 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-150",
      "org": "CIO Korea",
      "title": "오토스토어, 물류 자동화 시스템의 경제적 효과 연구 보고서 발표",
      "published": null,
      "url": "https://www.cio.com/article/3517636/%EC%98%A4%ED%86%A0%EC%8A%A4%ED%86%A0%EC%96%B4-%EB%AC%BC%EB%A5%98-%EC%9E%90%EB%8F%99%ED%99%94-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%EA%B2%BD%EC%A0%9C%EC%A0%81-%ED%9A%A8%EA%B3%BC-%EC%97%B0%EA%B5%AC.html",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 오토스토어가 국내 도입 기업 5곳의 3년간 도입 비용 대비 경제적 효과(NPV, 회수 기간, ROI)를 분석했다고 발표한 내용을 전한 기사(벤더 발표).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-151",
      "org": "박정수, 안영효(유통경영학회지)",
      "title": "화주기업과 물류기업의 공동 핵심성과지표 관리방법에 대한 연구",
      "published": "2010",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001434387",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 화주기업과 물류기업이 공동으로 KPI를 관리하고 빠르게 피드백하는 방법을 다룬 국내 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md",
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
      "rationale": "섹션 3: f8·f25(로봇 가동률이 출하량을 보장하지 않음, 운영·주문·비용 지표를 함께 봐야 함), f22(국내 인증이 성과관리 체계를 평가) / 섹션 4: f1·f2(ISO 22400 KPI·OEE), f4·f5(SCOR 완전 주문 이행·사이클 타임·비용), f6(입고–적치 소요 시간·피킹 정확도), f7(리틀의 법칙·임계 재공품), f14(순간·이동 병목) / 섹션 5: 입고 완료·인계 f6, 적치 예외·성과 f20, 적치 제약 f13, 피킹 수행 자원 f9·f10, 피킹 예외·성과 f8·f12, 출하 완료·인계 f4, 출하 예외·성과 f18·f25 / 섹션 6: f7·f8(흐름 법칙), f9·f10(해석적 모델), f12·f13(에너지·충전 비용 절충), f14·f15(병목 탐지), f19·f20(프로세스 마이닝) / 섹션 7: f1·f2·f3(ISO 22400과 OEE 정합성 비판 병기), f4·f5(SCOR), f6(WERC DC Measures), f16·f17(Open-RMF 로봇·작업 상태 스키마), f19(PM4Py), f22(스마트물류센터 인증) / 섹션 8: f3, f9~f14, f20, f23(국내 KPI 연구), f21(벤더 주장 병기 필수) / 섹션 9: f18(ROP 안에서 계산 가능한 운영 지표 대 주문 데이터가 필요한 지표), f24(연계 대상: 재무 투자 평가) / 섹션 10: 1. 주문·업무 시스템 연계(f18 주문 단위 지표), 2. 공정·워크플로 모델링(f19·f20 프로세스 마이닝), 3. 처리능력·거점·설비 계획(f9·f10), 16. 공용 자원·충전·에너지 최적화(f12·f13), 19. 모니터링·이상 탐지·원인 분석(f14·f15), 8. 실시간 세계 상태·데이터 일관성(f16 현재 상태 기록), 22. 시뮬레이션·예측용 디지털 트윈(f12·f13 가정한 정책 실험) / 섹션 11: open_questions_new 4건, 기존 oq-008(미해결)·oq-011(f22로 부분 보강, 개별 지표 미확인). 다음 실행 후보: ASTM F45 이동로봇 성능 시험 방법(23. 시험·형식 검증·벤치마크)과 인간–로봇 협업 피킹 현장 실험(18. 사람–로봇 협업·운영 인터페이스)은 출처 예산으로 넣지 못함"
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "종합설비효율",
      "term_en": "Overall Equipment Effectiveness (OEE)",
      "definition": "설비의 가용성·성능(효과성)·품질률을 곱해 계획된 시간 대비 실제로 좋은 산출을 낸 비율을 나타내는 지표로, ISO 22400-2가 제조 운영 관리 KPI의 하나로 정의한다."
    },
    {
      "term_ko": "완전 주문 이행률",
      "term_en": "Perfect Order Fulfillment",
      "definition": "납기·수량·문서·상태가 모두 요구대로 충족된 주문의 비율로, SCOR의 신뢰성 대표 지표(RL.1.1)이다."
    },
    {
      "term_ko": "리틀의 법칙",
      "term_en": "Little's Law",
      "definition": "안정된 흐름에서 재공품(WIP)이 처리량과 사이클 타임의 곱과 같다는 관계로, 처리량·재고·리드타임을 함께 해석하는 기준이 된다."
    },
    {
      "term_ko": "프로세스 마이닝",
      "term_en": "Process Mining",
      "definition": "시스템에 남은 이벤트 로그로 실제 업무 흐름을 발견하고 설계와 비교하며 대기·병목을 분석하는 기법이다."
    }
  ],
  "open_questions_new": [
    "로봇 상태 기록(작업 중·유휴·충전·오류)과 WMS·ERP의 주문 이행 지표(완전 주문 이행률, 주문 이행 사이클 타임)를 같은 기간·같은 주문 단위로 연결해 로봇 도입이 출하량·비용 개선으로 이어졌는지 검증한 공개 사례가 있는가? | 관련 영역: 4. 성과·경제성·프로세스 개선, 1. 주문·업무 시스템 연계 | 근거: f25 | 종류: 일반",
    "창고 이동로봇 플릿에 ISO 22400식 OEE(가용성·성능·품질)를 적용하는 합의된 정의가 있는가, 충전·대기·교통 정체 시간은 어느 손실로 분류해야 하는가? | 관련 영역: 4. 성과·경제성·프로세스 개선, 16. 공용 자원·충전·에너지 최적화 | 근거: f2 | 종류: 일반",
    "벤더 발표가 아닌 공공·학술 자료로 국내 물류 로봇 도입의 투자 효과(생산성·비용·회수 기간)를 측정한 결과가 있는가? | 관련 영역: 4. 성과·경제성·프로세스 개선, 3. 처리능력·거점·설비 계획 | 근거: f21 | 종류: 일반",
    "이동로봇·작업대·승강기가 섞인 창고 흐름에 활성 구간 기반 이동 병목 탐지나 객체 중심 프로세스 마이닝을 적용한 연구가 있는가? | 관련 영역: 4. 성과·경제성·프로세스 개선, 19. 모니터링·이상 탐지·원인 분석 | 근거: f15 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 21,
    "cross_checked_count": 0,
    "unverified": [
      "모든 finding 교차 확인 실패: 표준·연구마다 발행 주체 한 곳의 자료만 확인(f5 의 ref-001·ref-140 은 모두 ASCM)",
      "f1 ISO 22400-2 KPI 개수(34개)는 제3자 요약 기준",
      "f6 WERC 벤치마크 수치(최우수 피킹 정확도·입고–적치 시간 등)는 2차 요약 경유라 finding 으로 내지 않음",
      "f7 ref-143 발행일 미확인",
      "f12 Omega 논문 저자·실험 조건 미확인",
      "f21 오토스토어 연구의 수행 주체·방법론 미확인(벤더 주장)",
      "f22 스마트물류센터 인증 세부 항목에 로봇 대수·가동률 지표가 있는지 여전히 미확인 — oq-011 미해결",
      "oq-008 로봇 재배치·성수기 임대(RaaS)는 벤더·블로그 자료만 나와 finding 으로 내지 않음 — 미해결",
      "ref-142·ref-115·ref-146·ref-149 저자 미확인, ref-150 발행일 미확인",
      "인간–로봇 협업 피킹 현장 실험(Pasparakis·de Vries·de Koster, Logistics Research)과 ASTM F45 이동로봇 성능 시험 방법은 출처 상한으로 넣지 못함"
    ],
    "scope_violations": [
      "f24: 재무적 투자 평가(ROI·NPV·원가)는 분류 원문 9장 '상위 업무 시스템'의 재무 연계 영역이므로 '연계 대상: '으로 표시함",
      "f21: 벤더의 경제 효과 주장은 vendor_claim 으로 표시하고 ROP 직접 범위로 서술하지 않음"
    ],
    "budget_used": {
      "queries": 28,
      "sources": 15
    },
    "limits": "web_fetch_available: false · fetch_mode mirror_only. GitHub 공식 저장소 원문 3건(ref-147 PM4Py README, ref-111 task_state.json, ref-148 robot_state.json)만 raw.githubusercontent.com 으로 열었고, ISO·ASCM·WERC·논문·기사 12건은 검색 요약만 봐서 원문 미열람(신뢰도 상한 medium). 교차 확인 0건. 검색 28회/30, 신규 출처 15건/15(ref-139~ref-151, next_ref_id 기준)로 출처 상한에 도달했다. 재사용 6건(ref-001, ref-096, ref-097, ref-098, ref-102, ref-106). 이전 브리프에서 Open-RMF task_state.json 에 ref-054·ref-098 을 붙인 이력이 있으나 참고문헌 목록의 해당 id 는 다른 출처라 새 id(ref-111)를 붙였다 — 퍼블리셔가 중복을 확인해야 한다. 한국 자료: 스마트물류센터 인증 심사 기준(ref-106), 국내 KPI 논문(ref-151), 벤더 경제성 발표 기사(ref-150). 국내 공공 기관의 물류 로봇 투자 효과 실측 자료는 찾지 못했다. oq-011 은 f22 로 부분 보강했으나 해결 아님, oq-008 은 학술·공공 자료를 찾지 못했다. 에너지 지표는 RMFS 모델 연구(f12)와 충전 비용 절충(f13)뿐이고 현장 실측 자료는 없다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성(현재 로봇 상태 기록, f16)과 22. 시뮬레이션·예측용 디지털 트윈(정책·투자 대안의 가정 실험, f12·f13)은 구분해 연결을 제안했다."
  }
}
```

### runs/2026-09-25-14/verification.json

```json
{
  "run_id": "2026-09-25-14",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과로 ISO 페이지(iso.org/standard/54497, ISO 22400-2:2014)의 기관·제목·URL이 일치함을 확인했다. KPI 정의 구조는 확인. '30여 개'(34개)라는 개수는 제3자 블로그 요약에만 있어 미확인이다. 기준일은 2014판."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. OEE = Availability × Effectiveness × Quality Ratio 식은 검색 요약(제3자 해설 여러 건)에 나타난다. 그러나 'ISO/DIS 22400-2 개정안 진행 중'이라는 부분은 이번 검증 검색에서 확인하지 못했다. 이 부분은 '미확인'으로 표시하거나 삭제해야 한다(required_fixes). f3의 비판(판마다 정의가 어긋남)과 함께 제시해야 한다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. ScienceDirect S0360835220302527 검색 결과에서 제목·URL과 'provides two definitions of the OEE indicator' 취지를 확인했다. [의견]의 주체(논문 저자, 저자 미확인)를 밝혀야 한다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. scor.ascm.org/performance/reliability/RL.1.1이 검색 결과로 확인됐고, RL.2.1~RL.2.4 구성과 '품목 줄이 모두 완전해야 완전 주문'이라는 설명이 검색 요약과 맞는다. 요약은 ASCM 페이지와 제3자 해설(supplychainplanning.ie)에서 나왔다. 발행일 미확인, 확인일 기준."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. ref-001·ref-140(브리프 id)은 모두 ASCM 자료라 독립 교차가 아니다. 성과 속성별 대표 지표의 분류는 검색 요약 범위에서 확인했다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 근거 출처는 'WERC DC Measures Survey - 2025'(2025)인데, 주장에는 출처에 없는 '2026년 보고서는 주문 피킹 정확도를 품질 지표로 명시했다'가 들어 있다. 이 절은 삭제하고, 나머지 지표 목록은 원문 미열람·검색 요약 기준의 [추정]으로 둔다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 협회 저널 글의 검색 요약이 WIP = TH × CT와 임계 재공품 설명을 담고 있다. 리틀의 법칙은 널리 확립된 관계이지만, 교차 출처는 이번 브리프에 등록돼 있지 않다. ref-143(브리프 id) 발행일 미확인."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 적정. f7·f9와 RMFS 스테이션 비율 연구(재인용)에서 끌어낸 추론이며, 추론임을 밝히고 있다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 게시된 3. 처리능력·거점·설비 계획 페이지의 기존 각주 ref-096과 같은 출처·같은 주장이므로 재사용이 맞다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 요약 범위에서 Applied Mathematical Modelling 게재 논문의 결론과 일치한다. 해석적 모델의 결과임을 밝혀야 한다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. Transportation Science 53(4) 리뷰의 검색 요약과 일치한다. '공간을 적게 쓰고 24시간 운영'은 리뷰 저자의 정리로 서술해야 한다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 3.41%·26.07%는 단일 논문이 모델·시뮬레이션 조건에서 보고한 값이다. 본문에서 '저자 보고값, 모델·시뮬레이션 조건, 현장 실측 아님'을 병기하는 조건으로 유지한다. 저자 미확인."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 두 출처(ref-098, ref-102)는 각자 다른 부분을 뒷받침하므로 교차 확인이 아니다. 3. 처리능력·거점·설비 계획 페이지의 기존 각주를 재사용한다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. Production & Manufacturing Research 2023 체계적 리뷰의 검색 요약과 일치한다. Roser 외(2001)는 리뷰를 통한 재인용이다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 적정. 제조 라인 방법을 창고에 적용하는 추론이며, 적용 사례가 없음을 밝히고 있다. robot_state 스키마(원문 열람)의 상태 값으로 근거를 확인했다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증에서 raw.githubusercontent.com으로 원문을 다시 열어 확인했다. 상태 7값, battery 0.0~1.0 설명, task_id·issues·location·unix_millis_time 필드가 모두 일치한다. fetched=true가 정당하다. 발행일 미확인, 확인일 기준."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문을 다시 열어 확인했다. 시작·종료 시각, original_estimate_millis·estimate_millis, 12개 상태 값, assigned_to, phases, interruptions·cancellation·killed가 모두 일치한다. 이 출처(task_state.json, 같은 URL)는 참고문헌에 이미 ref-111로 등록돼 있으므로 브리프의 새 id ref-111 대신 기존 ref-111을 재사용해야 한다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 적정. 로봇·작업 상태 스키마에 주문·품목 줄 필드가 없다는 점은 원문 열람으로 확인했다(robot_state·task_state 최상위 필드)."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "README 원문을 다시 열어 확인했다. 관리 주체 Process Intelligence Solutions(Fraunhofer FIT 분사), AGPL-3.0과 상용 라이선스, OCEL 선택 기능이 모두 일치한다. 인용 구절은 README 첫 문장이다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. Springer 학술대회 사례 연구(2015)의 검색 요약과 일치한다. 단일 사례임을 밝혀야 한다. 저자 미확인."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low·vendor_claim true, '벤더 주장' 표시가 모두 적정하다. 원문 미열람(기사). 수치는 벤더 발표를 전한 기사 요약 범위이며, 연구 수행 주체·방법론은 미확인이다. 본문에서 벤더 주장 병기를 유지하고, 재무 지표는 연계 대상 맥락에서만 다뤄야 한다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 인증 운영 사이트의 검색 요약 범위다. '기반영역에서 성과관리 체계를 평가'는 기존 참고문헌 ref-151(국가물류통합정보센터 인증제 안내, 2. 공정·워크플로 모델링 페이지 근거)와도 맞는다. 그러나 두 출처 모두 같은 제도 운영 측 자료라 독립 교차로 보지 않는다. oq-011은 부분 보강일 뿐 해결이 아니다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. KCI 서지·초록 요약과 일치한다. [의견]의 주체(박정수·안영효 2010)를 밝혀야 한다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low, '연계 대상:' 표시가 적정하다. 분류 원문 9장 '상위 업무 시스템'(재무는 외부 연계) 경계와 맞다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 적정. 분류 원문 SCM 질문에 답하는 추론이며, 실증 사례가 없음을 밝히고 있다."
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
      "참고문헌 id 충돌: 브리프의 신규 출처 ref-139~ref-124는 docs/references/index.md에 이미 다른 출처로 등록된 id다(ref-139 Open-RMF task_new, ref-140 task_state.json, ref-141 OMG BPMN, ref-142 Camunda, ref-143 Corradini 외 FaMe, ref-144 Filippone 외, ref-145·ref-146 B2MML, ref-147 IEC 62264-3, ref-148 workflow net, ref-149 OCEL 2.0, ref-150 SCOR F1.3, ref-151 국가물류통합정보센터 인증제 안내). 그대로 게시하면 게시된 2. 공정·워크플로 모델링 등의 각주가 덮어써진다",
      "브리프 ref-111(rmf_api_msgs task_state.json)은 기존 ref-111과 같은 URL·같은 문서다. 새 id를 만들지 말고 ref-111을 재사용해야 한다",
      "f22(스마트물류센터 인증 기반영역의 성과관리 평가)는 기존 ref-151(국가물류통합정보센터 인증제 안내)와 게시된 2. 공정·워크플로 모델링 페이지의 주장과 겹친다. 기존 각주를 함께 쓸 수 있다",
      "f9·f13은 게시된 3. 처리능력·거점·설비 계획 페이지의 주장과 같다. 기존 각주 ref-096·ref-098·ref-102 재사용이 맞다(브리프가 이미 재사용함)",
      "glossary_candidates '프로세스 마이닝'은 기존 용어 '객체 중심 이벤트 로그(OCEL)'와 뜻이 다르므로 신규 등록해도 된다. 다만 정의에서 OCEL 용어 페이지로 연결해야 한다"
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
    "참고문헌 id 재부여: 브리프 신규 출처 ref-139~ref-124는 docs/references/index.md의 기존 출처와 id가 겹친다. 페이지 각주·프런트매터 sources·reference_updates에서 다음과 같이 바꾼다. ref-139→ref-125(ISO 22400-2), ref-140→ref-126(SCOR RL.1.1), ref-141→ref-127(WERC DC Measures 2025), ref-142→ref-128(CIE OEE 논문), ref-143→ref-129(PPI Little's Law), ref-115→ref-130(병목 탐지 리뷰), ref-144→ref-131(Azadeh 외), ref-145→ref-132(Ghelichi·Kilaru), ref-146→ref-133(Omega RMFS 에너지), ref-147→ref-134(PM4Py README), ref-148→ref-135(robot_state.json), ref-149→ref-136(창고 프로세스 마이닝 사례), ref-150→ref-137(CIO Korea 오토스토어 기사), ref-151→ref-138(박정수·안영효). 기존 ref-139~ref-151 페이지는 덮어쓰지 않는다 — 실행 컨텍스트의 next_ref_id(ref-139)가 이미 쓰인 범위를 가리켰기 때문이다.",
    "f17·f18의 브리프 ref-111(task_state.json)은 새로 등록하지 않는다. 기존 ref-140 각주 줄을 그대로 재사용한다 — 같은 URL·같은 문서다.",
    "f6: [사실] → [추정]으로 강등한다. '2026년 보고서는 주문 피킹 정확도를 품질 지표로 명시했다' 절은 삭제한다 — 근거 출처는 2025년판 조사이고 2026년 보고서는 출처에 없다.",
    "f1: '30여 개 지표'라는 개수 표현을 빼거나 '(개수는 제3자 요약 기준, 미확인)'을 붙인다. 기준일을 '2014판'으로 명시한다 — 개수는 ISO 원문으로 확인되지 않았다.",
    "f2: 'ISO/DIS 22400-2 개정안이 진행 중'이라는 부분을 삭제하거나 '미확인'으로 표시한다. OEE 정의 문장 바로 뒤에 f3(판마다 정의가 어긋난다는 논문 저자들의 평가)을 [의견]으로 함께 제시한다 — 개정 진행 여부는 검증에서 확인되지 않았고, 두 주장은 함께 읽어야 한다.",
    "f3·f23: [의견]의 주체를 문장 안에 밝힌다('Computers & Industrial Engineering 2020 게재 논문 저자들은', '박정수·안영효(2010)는').",
    "f12: 3.41%·26.07% 수치 뒤에 '저자 보고값이며 모델·시뮬레이션 조건의 결과이고 현장 실측이 아님'을 병기한다 — 단일 출처 수치다.",
    "f21: [추정]과 '벤더 주장' 병기를 유지한다. ROI·NPV·회수 기간은 9절에서 연계 대상(재무) 맥락으로만 두고 ROP 직접 성과처럼 쓰지 않는다 — 벤더 발표를 전한 기사이고 독립 확인이 없다.",
    "원문 미열람 표기: f16·f17·f19의 근거(PM4Py README, robot_state.json, 기존 ref-140)를 뺀 모든 신규·재사용 출처의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates의 해당 항목에 source_unopened: true를 넣는다 — 이번 실행은 fetch_mode mirror_only다.",
    "oq-011은 해결로 바꾸지 않는다 — f22는 성과관리 체계 평가와 등급 판단 기준만 확인했고, 로봇 대수·가동률 같은 개별 지표는 여전히 미확인이다. 11절에는 f22로 부분 보강했다고만 적는다. oq-008도 미해결로 둔다.",
    "10절 연결: f16의 로봇 상태 기록은 8. 실시간 세계 상태·데이터 일관성(현재 상태 표현)에, f12·f13의 정책·충전 대안 비교는 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)에 나눠 연결하고 두 역할을 섞지 않는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(fetch_mode mirror_only)에서 검증했다. 확인 24건, 미확인 1건(f6), 교차 확인 0건. 강등: f6 사실 → 추정(2026년 보고서 절은 출처에 없어 삭제). 원문 미열람 출처(브리프 id 기준): ref-001, ref-096, ref-097, ref-098, ref-102, ref-106, ref-139~ref-146, ref-149, ref-150, ref-151. 검증에서 원문을 다시 연 출처: ref-147(PM4Py README), ref-111(task_state.json, 기존 ref-111과 같은 문서), ref-148(robot_state.json). ISO 22400-2와 SCOR RL.1.1은 검색 결과로 실재와 핵심 정의를 확인했다(검증 검색 2회, 리서치 28회와 합쳐 회당 상한 30회 도달). 주의: 브리프 신규 출처 id ref-139~ref-124가 기존 참고문헌 id와 겹쳐 ref-125~ref-138로 다시 부여하도록 지시했다. 실행 컨텍스트의 next_ref_id가 이미 쓰인 범위를 가리키므로 pipeline/agent_runner.py와 퍼블리셔 담당의 확인이 필요하다. 핵심 주장은 대부분 단일 발행 주체 자료의 검색 요약에 기대고, 3·9절의 결론(가동률만으로 출하량·비용 개선을 판단할 수 없음, ROP 계산 지표와 주문 단위 지표의 경계)은 [추정]이다. 로봇 가동률과 주문·비용 지표를 연결해 실증한 공개 사례는 확인되지 않았다. 오토스토어 경제성 수치는 벤더 주장이다. 정정 요청 없음. 열린 질문 oq-008·oq-011은 미해결로 유지한다.",
  "retry_reason": null
}
```

### runs/2026-09-25-14/pages.json

```json
{
  "run_id": "2026-09-25-14",
  "outline": [
    {
      "path": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 650,
      "summary": "로봇 가동률만으로는 출하량·비용 개선을 판단할 수 없을 것으로 보이며, 운영 지표·주문 단위 지표·비용을 같은 기간으로 함께 비교해야 한다. [추정][^ref-096][^ref-126][^ref-135][^ref-129]",
      "planned_findings": [
        "f25",
        "f8",
        "f22"
      ]
    },
    {
      "path": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1300,
      "summary": "ISO 22400-2(2014판)는 OEE 등 제조 운영 KPI를, SCOR는 완전 주문 이행률 같은 주문 단위 성과를 정의하며, 리틀의 법칙은 재공품·처리량·사이클 타임의 관계를 준다. [사실][^ref-125][^ref-126][^ref-129]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f14"
      ]
    },
    {
      "path": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md",
      "section": "5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)",
      "budget_chars": 1100,
      "summary": "피킹 로봇을 늘린 뒤 효과를 점검하는 가상 시나리오로, 작업대·포장대 병목과 충전 제약 때문에 가동률 상승이 출하 증가로 이어지지 않을 수 있음을 보인다. [추정][^ref-129][^ref-096][^ref-097]",
      "planned_findings": [
        "f9",
        "f10",
        "f13",
        "f17",
        "f4",
        "f8",
        "f12",
        "f18",
        "f25"
      ]
    },
    {
      "path": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1300,
      "summary": "성과를 병목과 연결해 해석하는 기본 도구는 리틀의 법칙이며, 해석적 대기행렬 모델·에너지·충전 절충 평가·활성 구간 병목 탐지·프로세스 마이닝이 쓰인다. [사실][^ref-129]",
      "planned_findings": [
        "f7",
        "f9",
        "f10",
        "f12",
        "f13",
        "f14",
        "f15",
        "f20"
      ]
    },
    {
      "path": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 900,
      "summary": "ISO 22400-2, SCOR, WERC DC Measures, Open-RMF 로봇·작업 상태 스키마, PM4Py, 스마트물류센터 인증제가 이 영역의 지표 정의와 데이터 원천이다. [사실][^ref-125][^ref-126][^ref-135]",
      "planned_findings": [
        "f1",
        "f4",
        "f5",
        "f6",
        "f16",
        "f17",
        "f19",
        "f22"
      ]
    },
    {
      "path": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1100,
      "summary": "로봇형 창고 리뷰, RMFS 대기행렬·에너지 연구, 병목 탐지 리뷰, OEE 정합성 비판, 창고 프로세스 마이닝 사례, 국내 공동 KPI 연구가 대표 자료다. [사실][^ref-131][^ref-096][^ref-130]",
      "planned_findings": [
        "f11",
        "f9",
        "f10",
        "f12",
        "f13",
        "f14",
        "f3",
        "f20",
        "f23"
      ]
    },
    {
      "path": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)",
      "budget_chars": 900,
      "summary": "ROP는 로봇·작업 상태 기록으로 운영 지표를 계산하고, 주문 단위 지표와 재무적 투자 평가는 WMS·ERP·재무와 연계하는 것으로 보인다. [추정][^ref-140][^ref-135][^ref-126]",
      "planned_findings": [
        "f18",
        "f16",
        "f24",
        "f21"
      ]
    },
    {
      "path": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 800,
      "summary": "1. 주문·업무 시스템 연계, 2. 공정·워크플로 모델링, 3. 처리능력·거점·설비 계획, 8. 실시간 세계 상태·데이터 일관성, 16. 공용 자원·충전·에너지 최적화, 19. 모니터링·이상 탐지·원인 분석, 22. 시뮬레이션·예측용 디지털 트윈과 연결된다.",
      "planned_findings": [
        "f18",
        "f20",
        "f9",
        "f10",
        "f16",
        "f13",
        "f15",
        "f12"
      ]
    },
    {
      "path": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md",
      "section": "11. 열린 질문",
      "budget_chars": 700,
      "summary": "가동률–주문 지표 연결 실증, 이동로봇 OEE 정의, 국내 투자 효과 공공 자료, 창고 병목 탐지 적용의 새 질문 4건과 미해결 oq-008·oq-011을 둔다.",
      "planned_findings": [
        "f25",
        "f2",
        "f21",
        "f15",
        "f22"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성(성과 지표 표준, 흐름 법칙·병목 탐지·프로세스 마이닝, 가상 시나리오, ROP 경계, 연결 7개 영역, 열린 질문 4건+기존 2건), 참고문헌 id 재부여(ref-125~ref-138) 반영"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area04-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 4. 성과·경제성·프로세스 개선 의 \"8. 대표 연구와 자료\" 절(1,579자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area04-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 4. 성과·경제성·프로세스 개선 의 \"4. 핵심 개념과 용어\" 절(1,517자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area04-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 4. 성과·경제성·프로세스 개선 의 \"6. 대표 접근법과 기술\" 절(1,238자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area04-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 4. 성과·경제성·프로세스 개선 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,187자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area04-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 4. 성과·경제성·프로세스 개선 의 \"11. 열린 질문\" 절(970자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-25 | 4. 성과·경제성·프로세스 개선 | 3~11절 신규 작성(ISO 22400·SCOR·WERC 지표, 리틀의 법칙·병목 탐지·프로세스 마이닝, ROP 계산 지표와 주문·재무 지표의 경계, 열린 질문 4건), 참고문헌 id ref-125~ref-138 재부여 | run 2026-09-25-14",
  "index_updates": {
    "home_recent": "2026-09-25 — 4. 성과·경제성·프로세스 개선: 3~11절 신규 작성(성과 지표 표준, 병목 분석, 로봇 가동률과 주문·비용 지표의 경계, 열린 질문 4건)",
    "category_recent": "2026-09-25 — 4. 성과·경제성·프로세스 개선: 3~11절 신규 작성(ISO 22400·SCOR·WERC 지표, 리틀의 법칙·병목 탐지·프로세스 마이닝, ROP 경계, 열린 질문 4건)",
    "area_recent": "2026-09-25 — 4. 성과·경제성·프로세스 개선: 영역 심화로 3~11절 신규 작성, 신뢰도 medium (실행 2026-09-25-14)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "overall-equipment-effectiveness",
      "term_ko": "종합설비효율",
      "term_en": "Overall Equipment Effectiveness (OEE)",
      "definition": "설비의 가용성·효과성(성능)·품질률을 곱해 구하는 지표로, ISO 22400-2(2014판)가 제조 운영 관리 KPI의 하나로 정의한다.",
      "description": "ISO 22400-2는 계획 가동 시간(PBT) 같은 시간 상태 모델을 기준으로 계산한다. Computers & Industrial Engineering(2020) 게재 논문 저자들은 표준의 OEE 정의가 판마다 어긋난다고 평가했다.",
      "related_areas": [
        4,
        16
      ],
      "sources": [
        "ref-125",
        "ref-128"
      ]
    },
    {
      "action": "new",
      "slug": "perfect-order-fulfillment",
      "term_ko": "완전 주문 이행률",
      "term_en": "Perfect Order Fulfillment",
      "definition": "완전 주문 수를 전체 주문 수로 나눈 비율로, 주문의 모든 품목 줄이 완전해야 완전 주문으로 보는 SCOR의 신뢰성 대표 지표(RL.1.1)이다.",
      "description": "하위 지표로 완납 주문 비율(RL.2.1), 최초 약속일 대비 납기 성과(RL.2.2), 주문 문서 정확도(RL.2.3), 무손상 상태(RL.2.4)를 둔다.",
      "related_areas": [
        4,
        1
      ],
      "sources": [
        "ref-126"
      ]
    },
    {
      "action": "new",
      "slug": "littles-law",
      "term_ko": "리틀의 법칙",
      "term_en": "Little's Law",
      "definition": "재공품(WIP)이 처리량(TH)과 사이클 타임(CT)의 곱과 같다는 관계로, 처리량·재공품·리드타임을 함께 해석하는 기준이 된다.",
      "description": "팩토리 피직스의 임계 재공품 개념과 함께 쓰이며, 임계 재공품을 넘으면 처리량은 늘지 않고 사이클 타임만 길어진다고 본다.",
      "related_areas": [
        4,
        3
      ],
      "sources": [
        "ref-129"
      ]
    },
    {
      "action": "new",
      "slug": "process-mining",
      "term_ko": "프로세스 마이닝",
      "term_en": "Process Mining",
      "definition": "시스템에 남은 이벤트 로그로 실제 업무 흐름을 발견하고 대기·병목을 분석하는 기법이다.",
      "description": "창고 사례로 SAP 창고 관리 데이터에서 이벤트 로그를 뽑아 자재 이동 병목을 찾은 연구가 있고, 오픈소스 도구로 PM4Py가 있다. 여러 객체를 함께 기록하는 로그 형식은 용어집의 객체 중심 이벤트 로그(OCEL, ocel.md)를 참고한다.",
      "related_areas": [
        4,
        2,
        19
      ],
      "sources": [
        "ref-136",
        "ref-134"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-001",
      "org": "ASCM",
      "title": "SCOR Digital Standard",
      "published": null,
      "url": "https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-24",
      "summary": "원문 미열람. ASCM이 관리하는 공급망 운영 참조 모델(SCOR DS)의 공식 소개 페이지. 프로세스와 성과 지표 체계를 담는다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-096",
      "org": "Lamballais, T., Roy, D., & de Koster, M. B. M.",
      "title": "Estimating performance in a Robotic Mobile Fulfillment System",
      "published": "2017",
      "url": "https://repub.eur.nl/pub/107376/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RMFS의 대기행렬 네트워크 모델로 최대 처리량·사이클 타임·로봇 가동률을 추정하고 작업대 위치 영향을 분석한 EJOR 256 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-097",
      "org": "Lamballais, T., Roy, D., & de Koster, M. B. M.",
      "title": "Inventory allocation in robotic mobile fulfillment systems",
      "published": "2020",
      "url": "https://www.tandfonline.com/doi/abs/10.1080/24725854.2018.1560517",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 품목당 선반 수, 피킹·보충 스테이션 비율, 보충 수준이 RMFS 처리량에 주는 영향을 분석한 IISE Transactions 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
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
      "summary": "원문 미열람. RMFS 로봇의 플러그인 충전·배터리 교환·유도 충전을 비용·처리 시간 측면에서 비교한 EJOR 267(2) 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-102",
      "org": "Springer(FAIM 2025 발표 논문, 저자 미확인)",
      "title": "Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics",
      "published": "2025",
      "url": "https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 물류센터 팔레트 이동 데이터로 AMR 대수와 충전기 수를 시뮬레이션으로 정하는 의사결정 지원 틀을 제시한 학술대회 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-106",
      "org": "한국교통연구원(인증스마트물류센터)",
      "title": "인증스마트물류센터",
      "published": null,
      "url": "https://cslc.koti.re.kr/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 국토교통부 스마트물류센터 인증제의 근거·평가 영역(기능영역·기반영역)·심사기준·등급을 안내하는 인증 운영 사이트.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-140",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF API 작업 상태 JSON 스키마. 작업 시작·종료 시각, 최초·현재 예상 소요 시간, 상태 12종, 배정 로봇, 단계, 중단·취소 정보를 정의한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-125",
      "org": "ISO",
      "title": "ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions",
      "published": "2014",
      "url": "https://www.iso.org/standard/54497.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 제조 운영 관리용 KPI의 공식·구성 요소·시간 특성·단위를 정의한 국제표준(처리율, OEE, 가용성, 품질률 등).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-126",
      "org": "ASCM",
      "title": "SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment",
      "published": null,
      "url": "https://scor.ascm.org/performance/reliability/RL.1.1",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. SCOR 신뢰성 성과 지표 완전 고객 주문 이행률의 정의·계산식·하위 지표 페이지.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-127",
      "org": "WERC(Warehousing Education and Research Council)",
      "title": "WERC DC Measures Survey - 2025",
      "published": "2025",
      "url": "https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 물류센터 운영 지표(정시 출하, 용량 사용률, 피킹 정확도, 입고–적치 소요 시간 등)를 조사해 벤치마크를 내는 협회 연례 보고서.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-128",
      "org": "Computers & Industrial Engineering 게재 논문(저자 미확인)",
      "title": "Overall Equipment Effectiveness: consistency of ISO standard with literature",
      "published": "2020",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0360835220302527",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ISO 22400의 OEE 정의가 판마다, 그리고 기존 문헌·실무와 어긋나는 점을 분석하고 정합을 위한 가정을 제시한 논문(CIE 145).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-129",
      "org": "Project Production Institute",
      "title": "Little’s Law – A Practical Approach to Understanding Production System Performance",
      "published": null,
      "url": "https://projectproduction.org/journal/littles-law-a-practical-approach-to-understanding-production-system-performance/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 리틀의 법칙과 팩토리 피직스의 임계 재공품 개념으로 처리량·재공품·사이클 타임 관계를 설명한 협회 저널 글.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-130",
      "org": "Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본)",
      "title": "Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes",
      "published": "2023",
      "url": "https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 제조 처리량 병목 탐지 방법(활성 구간 방법 등)과 운영 방식을 체계적으로 정리한 리뷰.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-131",
      "org": "Azadeh, K., de Koster, R., & Roy, D.",
      "title": "Robotized and Automated Warehouse Systems: Review and Recent Developments",
      "published": "2019",
      "url": "https://pubsonline.informs.org/doi/abs/10.1287/trsc.2018.0873",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 셔틀·컴팩트 저장·RMFS 등 로봇형·자동화 창고 시스템 연구를 분석·설계·운영으로 나눠 정리한 Transportation Science 리뷰.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-132",
      "org": "Ghelichi, Z., & Kilaru, S.",
      "title": "Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers",
      "published": "2021",
      "url": "https://www.sciencedirect.com/science/article/pii/S0307904X20305801",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 협업형 AMR 피킹 방식(LMD, MIA)의 성과를 해석적 모델로 비교한 Applied Mathematical Modelling 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-133",
      "org": "Omega 게재 논문(저자 미확인)",
      "title": "The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority",
      "published": "2024",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RMFS에서 일반·긴급 주문의 동적 우선순위 정책이 처리 시간과 에너지 소비에 주는 영향을 평가한 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-134",
      "org": "Process Intelligence Solutions (PM4Py GitHub)",
      "title": "pm4py — Official public repository for PM4Py (Process Mining for Python) (README)",
      "published": null,
      "url": "https://github.com/process-intelligence-solutions/pm4py",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "오픈소스 파이썬 프로세스 마이닝 라이브러리 PM4Py 공식 저장소 README. 관리 주체, 라이선스(AGPL-3.0·상용), 설치와 선택 기능(OCEL 등)을 안내한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-135",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF API 로봇 상태 JSON 스키마. 상태 7종(유휴·충전·작업 중·오류 등), 배터리 충전 상태, 현재 작업 id, 문제 목록, 위치, 시각을 정의한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-136",
      "org": "Springer(학술대회 발표 논문, 저자 미확인)",
      "title": "Material Movement Analysis for Warehouse Business Process Improvement with Process Mining: A Case Study",
      "published": "2015",
      "url": "https://link.springer.com/chapter/10.1007/978-3-319-19509-4_9",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. SAP 창고 관리 모듈 데이터로 이벤트 로그를 만들어 프로세스 마이닝으로 창고 자재 이동의 병목을 분석한 사례 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-137",
      "org": "CIO Korea",
      "title": "오토스토어, 물류 자동화 시스템의 경제적 효과 연구 보고서 발표",
      "published": null,
      "url": "https://www.cio.com/article/3517636/%EC%98%A4%ED%86%A0%EC%8A%A4%ED%86%A0%EC%96%B4-%EB%AC%BC%EB%A5%98-%EC%9E%90%EB%8F%99%ED%99%94-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%EA%B2%BD%EC%A0%9C%EC%A0%81-%ED%9A%A8%EA%B3%BC-%EC%97%B0%EA%B5%AC.html",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 오토스토어가 국내 도입 기업 5곳의 3년간 도입 비용 대비 경제적 효과(NPV, 회수 기간, ROI)를 분석했다고 발표한 내용을 전한 기사(벤더 발표).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    },
    {
      "id": "ref-138",
      "org": "박정수, 안영효(유통경영학회지)",
      "title": "화주기업과 물류기업의 공동 핵심성과지표 관리방법에 대한 연구",
      "published": "2010",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001434387",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 화주기업과 물류기업이 공동으로 KPI를 관리하고 빠르게 피드백하는 방법을 다룬 국내 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "로봇 상태 기록(작업 중·유휴·충전·오류)과 WMS·ERP의 주문 이행 지표(완전 주문 이행률, 주문 이행 사이클 타임)를 같은 기간·같은 주문 단위로 연결해 로봇 도입이 출하량·비용 개선으로 이어졌는지 검증한 공개 사례가 있는가?",
      "areas": [
        4,
        1
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "창고 이동로봇 플릿에 ISO 22400식 OEE(가용성·성능·품질)를 적용하는 합의된 정의가 있는가, 충전·대기·교통 정체 시간은 어느 손실로 분류해야 하는가?",
      "areas": [
        4,
        16
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "벤더 발표가 아닌 공공·학술 자료로 국내 물류 로봇 도입의 투자 효과(생산성·비용·회수 기간)를 측정한 결과가 있는가?",
      "areas": [
        4,
        3
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "이동로봇·작업대·승강기가 섞인 창고 흐름에 활성 구간 기반 이동 병목 탐지나 객체 중심 프로세스 마이닝을 적용한 연구가 있는가?",
      "areas": [
        4,
        19
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [
    {
      "step": "피킹",
      "item": "시작 조건",
      "link": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "4. 성과·경제성·프로세스 개선"
    },
    {
      "step": "피킹",
      "item": "작업 대상",
      "link": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "4. 성과·경제성·프로세스 개선"
    },
    {
      "step": "피킹",
      "item": "수행 자원",
      "link": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "4. 성과·경제성·프로세스 개선"
    },
    {
      "step": "피킹",
      "item": "제약",
      "link": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "4. 성과·경제성·프로세스 개선"
    },
    {
      "step": "피킹",
      "item": "예외·성과",
      "link": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "4. 성과·경제성·프로세스 개선"
    },
    {
      "step": "포장",
      "item": "제약",
      "link": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "4. 성과·경제성·프로세스 개선"
    },
    {
      "step": "출하",
      "item": "완료·인계",
      "link": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "4. 성과·경제성·프로세스 개선"
    },
    {
      "step": "출하",
      "item": "예외·성과",
      "link": "docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "4. 성과·경제성·프로세스 개선"
    }
  ],
  "standards_updates": [
    {
      "name": "ISO 22400-2:2014 제조 운영 관리 KPI 정의",
      "kind": "표준",
      "org": "ISO",
      "url": "https://www.iso.org/standard/54497.html",
      "related_areas": [
        4
      ],
      "summary": "제조 운영 관리용 KPI(처리율, OEE, 가용성, 품질률 등)를 공식·구성 요소·시간 특성·단위와 함께 정의한 국제표준(2014판, 원문 미열람).",
      "ref_id": "ref-125"
    },
    {
      "name": "WERC DC Measures",
      "kind": "평가 프로그램",
      "org": "WERC(Warehousing Education and Research Council)",
      "url": "https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf",
      "related_areas": [
        4
      ],
      "summary": "물류센터 운영 지표(정시 출하, 용량 사용률, 피킹 정확도, 입고–적치 소요 시간 등)를 조사하는 협회 연례 벤치마크(2025년판, 원문 미열람).",
      "ref_id": "ref-127"
    },
    {
      "name": "PM4Py",
      "kind": "오픈소스",
      "org": "Process Intelligence Solutions",
      "url": "https://github.com/process-intelligence-solutions/pm4py",
      "related_areas": [
        4,
        2,
        19
      ],
      "summary": "프로세스 발견 등 알고리즘을 제공하고 OCEL을 선택 기능으로 두는 파이썬 프로세스 마이닝 라이브러리. 공개판 AGPL-3.0, 상용 라이선스 별도.",
      "ref_id": "ref-134"
    }
  ],
  "additional_research_requests": [
    "4·7절: ISO 22400-2:2014의 KPI 개수와 ISO/DIS 22400-2 개정 진행 여부를 ISO 원문 또는 독립 출처로 확인해야 한다 — 이번에는 제3자 요약뿐이라 개수는 미확인, 개정 부분은 삭제했다.",
    "4·7절: WERC DC Measures 2025의 지표 정의와 벤치마크 수치를 원문으로 확인해야 한다 — f6이 [추정]으로 강등되었다.",
    "3·11절: 로봇 가동률과 주문 단위 지표(완전 주문 이행률, 주문 이행 사이클 타임)·비용을 같은 기간으로 연결해 실증한 공개 사례가 필요하다 — 2절 질문에 대한 3절 결론이 [추정]뿐이다.",
    "9·11절: 국내 물류 로봇 도입 투자 효과를 측정한 공공·학술 자료가 필요하다 — 현재는 벤더 발표 기사(ref-137)뿐이다.",
    "11절: oq-008(거점 간 로봇 재배치·성수기 임대)과 oq-011(스마트물류센터 인증 세부 지표에 로봇 대수·가동률 포함 여부)의 학술·공공 근거가 여전히 없다.",
    "다음 실행 후보: ASTM F45 이동로봇 성능 시험 방법(23. 시험·형식 검증·벤치마크)과 인간–로봇 협업 피킹 현장 실험(18. 사람–로봇 협업·운영 인터페이스)은 출처 상한으로 브리프에 들어오지 않았다.",
    "pipeline 담당: 실행 컨텍스트의 next_ref_id(ref-139)가 이미 쓰인 범위를 가리켜 1차 검증이 ref-125~ref-138로 재부여를 지시했다. agent_runner.py 의 next_ref_id 계산과 퍼블리셔의 id 중복 검사를 확인해야 한다."
  ],
  "fixes_applied": [
    "참고문헌 id 재부여 — 페이지 각주·프런트매터 sources·reference_updates에서 ref-139→ref-125, ref-140(SCOR)→ref-126, ref-141→ref-127, ref-142→ref-128, ref-143→ref-129, ref-115→ref-130, ref-144→ref-131, ref-145→ref-132, ref-146→ref-133, ref-147→ref-134, ref-148→ref-135, ref-149→ref-136, ref-150→ref-137, ref-151→ref-138로 바꾸고 기존 ref-139~ref-151 항목은 내지 않았다.",
    "task_state.json 재사용 — f17·f18을 쓴 5·7·9·10절 문장에 새 id 대신 기존 ref-140 각주를 달고, 13절에 기존 ref-140 각주 줄을 그대로 두었으며 reference_updates 에는 cited_by 갱신으로만 넣었다.",
    "f6 강등 — 4절 용어 목록과 7절 표의 WERC 문장을 [추정]으로 쓰고 '2026년 보고서는 주문 피킹 정확도를 품질 지표로 명시' 절을 삭제했다.",
    "f1 — 4·7절에서 '30여 개' 표현을 빼고 '(지표 개수는 미확인)'을 적었으며 'ISO 22400-2:2014판', '2014판'으로 기준일을 명시했다.",
    "f2 — 'ISO/DIS 22400-2 개정안 진행 중' 부분을 삭제하고, 4절 OEE 정의 문장 바로 뒤에 f3을 논문 저자들의 [의견]으로 붙였다.",
    "f3·f23 — 4·8절에서 'Computers & Industrial Engineering(2020) 게재 논문 저자들은', '박정수·안영효(2010)는'으로 [의견]의 주체를 문장 안에 밝혔다.",
    "f12 — 5절 표 예외·성과 칸의 3.41%·26.07% 수치 뒤에 '(저자 보고값이며 모델·시뮬레이션 조건의 결과이고 현장 실측이 아님)'을 병기했고, 6·8절에는 수치 없이 절충 결과만 적었다.",
    "f21 — 오토스토어 경제성 수치를 9절 연계 대상(재무) 맥락에만 두고 '[추정] 벤더 주장' 병기와 '연구 수행 주체와 방법론은 미확인이며 ROP의 직접 성과가 아니다'를 적었다.",
    "원문 미열람 표기 — ref-140·ref-134·ref-135를 뺀 모든 각주 정의(ref-001·096·097·098·102·106·125~133·136~138)의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true를 넣었다.",
    "oq-011·oq-008 — 11절에서 oq-011은 열림 상태로 두고 f22로 성과관리 체계 평가와 등급 기준만 부분 보강했으며 개별 지표는 미확인이라고 적었고, oq-008도 미해결로 두었다. open_question_updates 에 해결 변경을 내지 않았다.",
    "10절 연결 — f16 로봇 상태 기록은 8. 실시간 세계 상태·데이터 일관성(현재 상태 표현)에, f12·f13의 정책·충전 대안 비교는 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)에 나눠 연결하고 두 역할을 구분하는 문장을 넣었다.",
    "분량 초과 자동 분리: 4. 성과·경제성·프로세스 개선 본문 9,623자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,845자"
  ]
}
```

### runs/2026-09-25-14/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-25-area04-s8.md (1,579자)
    - docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-25-area04-s4.md (1,517자)
    - docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-25-area04-s6.md (1,238자)
    - docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-25-area04-s7.md (1,187자)
    - docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md "11. 열린 질문" → docs/topics/2026/2026-09-25-area04-s11.md (970자)
```

### runs/2026-09-25-14/pages/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md

```markdown
---
title: "4. 성과·경제성·프로세스 개선"
type: area
category: "A. 업무·공급망 설계"
area_no: 4
related_areas: [1, 2, 3, 8, 16, 19, 22]
tags: [KPI, OEE, 완전 주문 이행률, 리틀의 법칙, 병목 분석, 프로세스 마이닝]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-001, ref-096, ref-097, ref-098, ref-102, ref-106, ref-140, ref-125, ref-126, ref-127, ref-128, ref-129, ref-130, ref-131, ref-132, ref-133, ref-134, ref-135, ref-136, ref-137, ref-138]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [A. 업무·공급망 설계](index.md) › 4. 성과·경제성·프로세스 개선

# 4. 성과·경제성·프로세스 개선

!!! info "소속 대분류"
    [A. 업무·공급망 설계](index.md) — 핵심 질문:
    무슨 일을 왜, 얼마나 해야 하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 [분류원문]

## 2. SCM 관점의 질문

로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? [분류원문]

## 3. 왜 중요한가

로봇 가동률이 올랐다는 것만으로는 출하량과 비용이 개선됐다고 판단할 수 없을 것으로 보이며, 같은 기간의 로봇 운영 지표(가동률·충전·오류 시간), 주문 단위 지표(완전 주문 이행률, 주문 이행 사이클 타임), 비용을 함께 비교해야 한다. [추정][^ref-096][^ref-126][^ref-135][^ref-129]

작업대·포장대 같은 병목의 처리 속도를 넘어 로봇 작업을 더 투입하면 로봇 가동률은 올라가도 출하 처리량은 늘지 않고 주문 사이클 타임만 길어질 수 있다. [추정][^ref-129][^ref-096][^ref-097] 이 판단은 리틀의 법칙과 로봇 이동형 풀필먼트 시스템(Robotic Mobile Fulfillment System, RMFS) 대기행렬 연구를 함께 읽어 끌어낸 추론이다. 로봇 가동률과 주문·비용 지표를 연결해 실증한 공개 사례는 미확인이다(11절).

국내 제도도 성과관리를 평가한다. 스마트물류센터 인증은 기반영역에서 성과관리 체계를 평가하며, 세부 항목 판단 기준을 데이터 관리 기반 구축(5등급), 실시간 모니터링(4등급), 관리와 통제(3등급), 최적화(2등급), 자율운영(1등급)의 단계로 둔다(2026-09-25 확인). [사실][^ref-106]

## 4. 핵심 개념과 용어

성과를 재는 지표는 설비·운영 수준(ISO 22400-2)과 주문·공급망 수준(SCOR)으로 나뉘고, 둘 사이를 잇는 흐름 법칙으로 리틀의 법칙이 쓰인다. 아래 용어가 이 페이지의 기준이다.

자세한 내용은 주제 페이지 [4. 성과·경제성·프로세스 개선 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area04-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

다음은 설명을 위한 가상의 시나리오이다. 현장 수치는 넣지 않았다.

**물류 흐름 단계:** 피킹 → 포장 → 출하

**시나리오:** 출고 물량이 늘어 피킹 로봇 투입을 늘린 뒤 효과를 점검

| 항목 | 내용 |
|---|---|
| 시작 조건 | 출고 주문이 늘어 운영자가 부품-작업자 방식 창고의 피킹 로봇 투입을 늘린다. |
| 작업 대상 | 상품을 담은 이동식 선반([로봇 이동형 풀필먼트 시스템](../../glossary/robotic-mobile-fulfillment-system.md))과 피킹된 주문 상자 |
| 수행 자원 | 로봇이 선반을 작업대로 옮기고 작업자가 피킹한다. RMFS 대기행렬 모델에서 처리량은 보관 구역 둘레의 작업대 위치에 영향을 받았고(2017) [사실][^ref-096], 협업형 AMR 피킹의 해석적 모델에서는 처리율·피킹 구역 크기·클러스터 크기가 성과를 가장 크게 좌우했다(2021). [사실][^ref-132] |
| 제약 | 작업대·포장대의 처리 속도와 충전기 수. AMR 물류센터 시뮬레이션에서 충전기가 부족하면 큰 지연이, 과잉이면 불필요한 비용이 생겼다(2025). [사실][^ref-102] |
| 완료·인계 | 로봇 작업은 작업 상태 기록의 시작·종료 시각과 상태 값으로 완료가 남는다. [사실][^ref-140] 출하 성과는 SCOR 기준에서 주문의 모든 품목 줄이 완전해야 완전 주문으로 센다. [사실][^ref-126] |
| 예외·성과 | 병목의 처리 속도를 넘어 로봇 작업을 더 넣으면 가동률은 올라도 출하 처리량은 늘지 않고 주문 사이클 타임만 길어질 수 있다. [추정][^ref-129][^ref-096][^ref-097] 운영 규칙도 성과를 바꾼다. Omega(2024) 게재 연구는 동적 우선순위 규칙이 선착순(FCFS) 대비 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했다(저자 보고값이며 모델·시뮬레이션 조건의 결과이고 현장 실측이 아님). [사실][^ref-133] |

운영자는 로봇 가동률이 올랐다는 보고를 먼저 받는다. 로봇·작업 상태 기록으로 가동률, 충전·오류 시간 비율, 작업 사이클 타임과 예상 대비 편차, 취소·실패 비율은 ROP 안에서 계산할 수 있으나, 완전 주문 이행률·주문 이행 사이클 타임은 WMS·ERP의 주문 데이터와 연결해야 계산될 것으로 보인다. [추정][^ref-140][^ref-135][^ref-126]

그래서 이 시나리오의 판단은 출하 단계에서 내려진다. 처리량이 작업대 같은 공유 자원에 묶이는 연구 결과로 볼 때, 로봇 증차의 효과는 가동률이 아니라 같은 기간의 주문 단위 지표와 비용을 함께 비교해야 판단할 수 있을 것으로 보인다. [추정][^ref-096][^ref-126][^ref-135][^ref-129]

## 6. 대표 접근법과 기술

성과를 병목과 연결해 해석하는 기본 도구는 리틀의 법칙이며, 임계 재공품을 넘는 투입은 처리량 대신 사이클 타임만 늘린다고 본다. [사실][^ref-129] 그 위에 해석적 모델, 에너지·충전 절충 평가, 병목 탐지, 프로세스 마이닝이 쓰인다.

자세한 내용은 주제 페이지 [4. 성과·경제성·프로세스 개선 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area04-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 지표 정의는 ISO 22400-2와 SCOR에서, 계산의 원천 데이터는 로봇·작업 상태 스키마에서 온다. [사실][^ref-125][^ref-126][^ref-135]

자세한 내용은 주제 페이지 [4. 성과·경제성·프로세스 개선 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area04-s7.md)에 있다.

## 8. 대표 연구와 자료

로봇형 창고의 성과 연구는 대기행렬·해석적 모델과 시뮬레이션이 중심이고, 현장 실측 자료는 이번 조사에서 확인하지 못했다. 대표 자료는 다음과 같다.

자세한 내용은 주제 페이지 [4. 성과·경제성·프로세스 개선 — 대표 연구와 자료](../../topics/2026/2026-09-25-area04-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

ROP는 로봇·작업 상태 기록으로 운영 지표를 계산하는 쪽을 맡고, 주문 단위 지표와 재무적 투자 평가는 상위 업무 시스템과 연계하는 것으로 보인다. [추정][^ref-140][^ref-135][^ref-126]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 로봇·작업 상태 기록으로 로봇 가동률(작업 중 시간 비율), 충전·오류 시간 비율, 작업 사이클 타임과 예상 대비 편차, 취소·실패 비율 같은 운영 지표 계산 [추정][^ref-140][^ref-135] | 연계 대상: 완전 주문 이행률·주문 이행 사이클 타임 같은 주문 단위 지표(WMS·ERP 주문 데이터), 투자 수익률·순현재가치·회수 기간 같은 재무 평가와 원가 배분 [추정][^ref-126][^ref-137][^ref-125] |
| 로봇 자체 지능·제어 | 제조사 관제가 보고하는 로봇 상태 값, 배터리 충전 상태, 현재 작업 id, 문제 목록, 위치, 시각의 수집 [사실][^ref-135] | 연계 대상: 원문 9장이 로봇 자체 기능으로 든 '센서 인식, SLAM, 로컬 회피, 파지, 모터·관절 제어' |

재무적 투자 평가와 원가 배분은 재무 등 상위 업무 영역의 몫이고, ROP는 그 입력이 되는 처리량·가동률·충전·예외 같은 실행 데이터를 제공하고 운영 규칙 변경의 효과를 측정하는 쪽을 맡는 것으로 보인다. [추정][^ref-137][^ref-125][^ref-135]

연계 대상인 재무 평가의 예로, 오토스토어가 발표한 경제성 연구는 국내 도입 기업 5곳이 3년간 시스템 도입 비용 87.4억 원 대비 약 156.7억 원의 경제적 효과, 순현재가치 약 69.2억 원, 투자 회수 18개월, ROI 79%를 거뒀다고 밝혔다. [추정] 벤더 주장[^ref-137] 연구 수행 주체와 방법론은 미확인이며, 이 수치는 ROP의 직접 성과가 아니다. 경계가 제품 전략에 따라 달라질 수 있다는 원문 9장의 취지는 [범위 경계](../../about/scope-boundary.md)에 정리돼 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 다른 영역이 만든 기록과 모델을 성과 판단에 쓰므로 데이터 원천과 실험 도구 양쪽에 연결된다.

- [1. 주문·업무 시스템 연계](01-order-and-business-system-integration.md) — 완전 주문 이행률 같은 주문 단위 지표는 WMS·ERP 주문 데이터와 로봇 작업 기록을 연결해야 계산될 것으로 보인다. [추정][^ref-126][^ref-140][^ref-135]
- [2. 공정·워크플로 모델링](02-process-and-workflow-modeling.md) — 이벤트 로그로 실제 창고 흐름과 병목을 찾는 프로세스 마이닝이 공정 모델과 실제의 차이를 드러낸다. [사실][^ref-136]
- [3. 처리능력·거점·설비 계획](03-capacity-site-and-facility-planning.md) — 작업대 위치와 피킹 방식이 처리량과 필요한 로봇 수를 좌우한다는 해석적 모델 결과를 공유한다. [사실][^ref-096][^ref-132]
- [8. 실시간 세계 상태·데이터 일관성](../b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md) — 성과 계산의 원천은 로봇의 현재 상태를 표현하는 상태 기록(상태 값·배터리·작업 id·시각)이다. [사실][^ref-135]
- [16. 공용 자원·충전·에너지 최적화](../d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) — 충전 방식과 충전기 수 결정이 비용과 처리 시간의 절충으로 연구되어 있다. [사실][^ref-098][^ref-102]
- [19. 모니터링·이상 탐지·원인 분석](../e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) — 활성 구간 기반 이동 병목 탐지를 로봇 상태 기록에 적용할 수 있을 것으로 보인다. [추정][^ref-130][^ref-135]
- [22. 시뮬레이션·예측용 디지털 트윈](../f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) — 우선순위 정책과 충전 대안을 운영 전에 비교하는 일은 가정한 미래를 실험하는 쪽이다. [사실][^ref-133][^ref-102] 현재 상태를 표현하는 8. 실시간 세계 상태·데이터 일관성과는 역할을 나눠 연결한다.

## 11. 열린 질문

로봇 운영 지표와 주문·비용 지표를 연결한 실증 자료가 없다는 점이 이 영역의 가장 큰 공백이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [4. 성과·경제성·프로세스 개선 — 열린 질문](../../topics/2026/2026-09-25-area04-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-096]: Lamballais, T., Roy, D., & de Koster, M. B. M., Estimating performance in a Robotic Mobile Fulfillment System, 2017, https://repub.eur.nl/pub/107376/, 접근일 2026-09-25 (원문 미열람)
[^ref-097]: Lamballais, T., Roy, D., & de Koster, M. B. M., Inventory allocation in robotic mobile fulfillment systems, 2020, https://www.tandfonline.com/doi/abs/10.1080/24725854.2018.1560517, 접근일 2026-09-25 (원문 미열람)
[^ref-098]: Zou, B., Gong, Y., de Koster, R., & Xu, X., Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system, 2018, https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901, 접근일 2026-09-25 (원문 미열람)
[^ref-102]: Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics, 2025, https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69, 접근일 2026-09-25 (원문 미열람)
[^ref-106]: 한국교통연구원(인증스마트물류센터), 인증스마트물류센터, 미확인, https://cslc.koti.re.kr/, 접근일 2026-09-25 (원문 미열람)
[^ref-140]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25
[^ref-125]: ISO, ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions, 2014, https://www.iso.org/standard/54497.html, 접근일 2026-09-25 (원문 미열람)
[^ref-126]: ASCM, SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment, 미확인, https://scor.ascm.org/performance/reliability/RL.1.1, 접근일 2026-09-25 (원문 미열람)
[^ref-129]: Project Production Institute, Little’s Law – A Practical Approach to Understanding Production System Performance, 미확인, https://projectproduction.org/journal/littles-law-a-practical-approach-to-understanding-production-system-performance/, 접근일 2026-09-25 (원문 미열람)
[^ref-130]: Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본), Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes, 2023, https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031, 접근일 2026-09-25 (원문 미열람)
[^ref-132]: Ghelichi, Z., & Kilaru, S., Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers, 2021, https://www.sciencedirect.com/science/article/pii/S0307904X20305801, 접근일 2026-09-25 (원문 미열람)
[^ref-133]: Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336, 접근일 2026-09-25 (원문 미열람)
[^ref-135]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25
[^ref-136]: Springer(학술대회 발표 논문, 저자 미확인), Material Movement Analysis for Warehouse Business Process Improvement with Process Mining: A Case Study, 2015, https://link.springer.com/chapter/10.1007/978-3-319-19509-4_9, 접근일 2026-09-25 (원문 미열람)
[^ref-137]: CIO Korea, 오토스토어, 물류 자동화 시스템의 경제적 효과 연구 보고서 발표, 미확인, https://www.cio.com/article/3517636/%EC%98%A4%ED%86%A0%EC%8A%A4%ED%86%A0%EC%96%B4-%EB%AC%BC%EB%A5%98-%EC%9E%90%EB%8F%99%ED%99%94-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%EA%B2%BD%EC%A0%9C%EC%A0%81-%ED%9A%A8%EA%B3%BC-%EC%97%B0%EA%B5%AC.html, 접근일 2026-09-25 (원문 미열람)
```

### docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md

```markdown
---
title: "4. 성과·경제성·프로세스 개선"
type: area
category: "A. 업무·공급망 설계"
area_no: 4
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [A. 업무·공급망 설계](index.md) › 4. 성과·경제성·프로세스 개선

# 4. 성과·경제성·프로세스 개선

!!! info "소속 대분류"
    [A. 업무·공급망 설계](index.md) — 핵심 질문:
    무슨 일을 왜, 얼마나 해야 하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 [분류원문]

## 2. SCM 관점의 질문

로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? [분류원문]

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

### runs/2026-09-25-14/pages/topics/2026/2026-09-25-area04-s8.md

```markdown
---
title: "4. 성과·경제성·프로세스 개선 — 대표 연구와 자료"
type: topic
category: "A. 업무·공급망 설계"
primary_area_no: 4
related_areas: [1, 2, 3, 8, 16, 19, 22]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-096, ref-098, ref-128, ref-130, ref-131, ref-132, ref-133, ref-136, ref-138]
last_run: 2026-09-25
version: 1
split_from: docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#8
---

[홈](../../index.md) › [주제](../index.md) › 4. 성과·경제성·프로세스 개선 — 대표 연구와 자료

# 4. 성과·경제성·프로세스 개선 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇형 창고의 성과 연구는 대기행렬·해석적 모델과 시뮬레이션이 중심이고, 현장 실측 자료는 이번 조사에서 확인하지 못했다. 대표 자료는 다음과 같다.
- 이 페이지는 [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇형 창고의 성과 연구는 대기행렬·해석적 모델과 시뮬레이션이 중심이고, 현장 실측 자료는 이번 조사에서 확인하지 못했다. 대표 자료는 다음과 같다.

- Azadeh, K., de Koster, R., & Roy, D., Robotized and Automated Warehouse Systems: Review and Recent Developments(2019) — 리뷰 저자들은 로봇형 처리 시스템(셔틀 기반 저장·반출, 컴팩트 저장, RMFS 등)이 공간을 적게 쓰고 수요 변동에 유연하며 24시간 운영할 수 있다고 정리하고, 연구를 시스템 분석·설계 최적화·운영 계획·통제로 나누면서 많은 신규 시스템이 학술적으로 거의 연구되지 않았다고 지적했다. [사실][^ref-131]
- Lamballais, T., Roy, D., & de Koster, M. B. M., Estimating performance in a Robotic Mobile Fulfillment System(2017) — 최대 주문 처리량·평균 주문 사이클 타임·로봇 가동률을 한 대기행렬 모델로 함께 추정했다. [사실][^ref-096]
- Ghelichi, Z., & Kilaru, S., Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers(2021) — 해석적 모델에서 처리율·피킹 구역 크기·클러스터 크기가 협업형 AMR 피킹 성과를 가장 크게 좌우했다. [사실][^ref-132]
- Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems(2024) — 동적 우선순위 정책을 평가해 처리량과 에너지 소비 사이의 절충을 보였다. [사실][^ref-133]
- Zou, B. 외, Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system(2018) — RMFS에서 배터리 비용이 낮으면 배터리 교환이 플러그인 충전보다 저렴했다. [사실][^ref-098]
- Production & Manufacturing Research 게재 체계적 리뷰(2023, 저자 미확인) — 처리량 병목 탐지 방법을 정리하고 병목을 순간·평균·이동 병목으로 구분했다. [사실][^ref-130]
- Computers & Industrial Engineering 게재 논문(2020, 저자 미확인), Overall Equipment Effectiveness: consistency of ISO standard with literature — 논문 저자들은 ISO 22400의 OEE 정의가 판마다, 그리고 기존 정식화와 어긋나 표준이 불완전하다고 평가했다. [의견][^ref-128]
- 창고 프로세스 마이닝 사례 연구(2015, 저자 미확인) — 단일 사례에서 SAP 창고 관리 데이터로 이벤트 로그를 만들어 자재 이동의 병목을 찾았다. [사실][^ref-136]
- 박정수·안영효, 화주기업과 물류기업의 공동 핵심성과지표 관리방법에 대한 연구(2010) — 박정수·안영효(2010)는 화주기업과 물류기업이 공동으로 KPI를 관리하는 방법을 다루며, 경영환경 변화에 대응하려면 KPI를 분석해 빠르게 피드백하는 체계가 필요하다고 보았다. [의견][^ref-138]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [2. 공정·워크플로 모델링](../../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md), [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-096]: Lamballais, T., Roy, D., & de Koster, M. B. M., Estimating performance in a Robotic Mobile Fulfillment System, 2017, https://repub.eur.nl/pub/107376/, 접근일 2026-09-25 (원문 미열람)
[^ref-098]: Zou, B., Gong, Y., de Koster, R., & Xu, X., Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system, 2018, https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901, 접근일 2026-09-25 (원문 미열람)
[^ref-128]: Computers & Industrial Engineering 게재 논문(저자 미확인), Overall Equipment Effectiveness: consistency of ISO standard with literature, 2020, https://www.sciencedirect.com/science/article/abs/pii/S0360835220302527, 접근일 2026-09-25 (원문 미열람)
[^ref-130]: Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본), Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes, 2023, https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031, 접근일 2026-09-25 (원문 미열람)
[^ref-131]: Azadeh, K., de Koster, R., & Roy, D., Robotized and Automated Warehouse Systems: Review and Recent Developments, 2019, https://pubsonline.informs.org/doi/abs/10.1287/trsc.2018.0873, 접근일 2026-09-25 (원문 미열람)
[^ref-132]: Ghelichi, Z., & Kilaru, S., Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers, 2021, https://www.sciencedirect.com/science/article/pii/S0307904X20305801, 접근일 2026-09-25 (원문 미열람)
[^ref-133]: Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336, 접근일 2026-09-25 (원문 미열람)
[^ref-136]: Springer(학술대회 발표 논문, 저자 미확인), Material Movement Analysis for Warehouse Business Process Improvement with Process Mining: A Case Study, 2015, https://link.springer.com/chapter/10.1007/978-3-319-19509-4_9, 접근일 2026-09-25 (원문 미열람)
[^ref-138]: 박정수, 안영효(유통경영학회지), 화주기업과 물류기업의 공동 핵심성과지표 관리방법에 대한 연구, 2010, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001434387, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-14 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-14 | 4. 성과·경제성·프로세스 개선 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-25-14/pages/topics/2026/2026-09-25-area04-s4.md

```markdown
---
title: "4. 성과·경제성·프로세스 개선 — 핵심 개념과 용어"
type: topic
category: "A. 업무·공급망 설계"
primary_area_no: 4
related_areas: [1, 2, 3, 8, 16, 19, 22]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-001, ref-125, ref-126, ref-127, ref-128, ref-129, ref-130]
last_run: 2026-09-25
version: 1
split_from: docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#4
---

[홈](../../index.md) › [주제](../index.md) › 4. 성과·경제성·프로세스 개선 — 핵심 개념과 용어

# 4. 성과·경제성·프로세스 개선 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 성과를 재는 지표는 설비·운영 수준(ISO 22400-2)과 주문·공급망 수준(SCOR)으로 나뉘고, 둘 사이를 잇는 흐름 법칙으로 리틀의 법칙이 쓰인다. 아래 용어가 이 페이지의 기준이다.
- 이 페이지는 [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

성과를 재는 지표는 설비·운영 수준(ISO 22400-2)과 주문·공급망 수준(SCOR)으로 나뉘고, 둘 사이를 잇는 흐름 법칙으로 리틀의 법칙이 쓰인다. 아래 용어가 이 페이지의 기준이다.

- **핵심성과지표(Key Performance Indicator, KPI)와 ISO 22400-2** — ISO 22400-2:2014판은 제조 운영 관리용 KPI를 공식·구성 요소·시간 특성·단위와 함께 정의하며, 처리율(throughput rate), 가동 효율, 종합설비효율, 가용성, 품질률, 재고 회전율, 평균 고장 간격·수리 시간 같은 지표를 담는다(지표 개수는 미확인). [사실][^ref-125]
- **종합설비효율(Overall Equipment Effectiveness, OEE)** — ISO 22400-2(2014판)에서 OEE는 가용성·효과성(성능)·품질률의 곱으로 정의되고 계획 가동 시간(Planned Busy Time, PBT) 같은 시간 상태 모델을 기준으로 계산된다. [사실][^ref-125] Computers & Industrial Engineering(2020) 게재 논문 저자들은 ISO 22400의 OEE 정의가 판마다 서로 어긋나고 나카지마의 TPM(Total Productive Maintenance) 원래 정식화와도 달라 표준이 불완전하다고 평가하고, 둘을 맞추는 암묵적 가정을 제시했다. [의견][^ref-128]
- **완전 고객 주문 이행률(Perfect Customer Order Fulfillment)** — SCOR의 신뢰성 지표(RL.1.1)로, 완전 주문 수를 전체 주문 수로 나눈 비율이다. 주문의 모든 품목 줄이 완전해야 완전 주문으로 보고, 하위 지표로 완납 주문 비율(RL.2.1), 최초 약속일 대비 납기 성과(RL.2.2), 주문 문서 정확도(RL.2.3), 무손상 상태(RL.2.4)를 둔다(2026-09-25 확인). [사실][^ref-126]
- **SCOR 성과 속성** — [SCOR](../../glossary/scor.md)의 대표 지표는 신뢰성(완전 주문 이행), 대응성(주문 이행 사이클 타임), 비용(공급망 관리 총비용) 같은 성과 속성별로 나뉘어, 로봇 운영 지표보다 상위의 주문·공급망 단위 성과를 잰다(2026-09-25 확인). [사실][^ref-001][^ref-126]
- **물류센터 운영 지표** — WERC DC Measures 연례 조사(2025년판)는 물류센터 운영자가 꼽는 주요 지표로 정시 출하율, 평균 창고 용량 사용률, 주문 피킹 정확도, 입고–적치 소요 시간(dock-to-stock cycle time)을 다루는 것으로 보인다. [추정][^ref-127]
- **리틀의 법칙(Little's Law)과 임계 재공품** — 재공품(Work In Process, WIP) = 처리량(Throughput, TH) × 사이클 타임(Cycle Time, CT)의 관계이며, Hopp·Spearman의 팩토리 피직스는 병목 속도에서 최대 처리량을 내는 임계 재공품(critical WIP)을 넘으면 처리량은 늘지 않고 대기 때문에 사이클 타임만 길어진다고 본다. [사실][^ref-129]
- **순간·평균·이동 병목** — 처리량 병목 탐지 문헌은 병목을 순간(momentary)·평균(average)·이동(shifting) 병목으로 구분한다. [사실][^ref-130]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [2. 공정·워크플로 모델링](../../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md), [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-001]: ASCM, SCOR Digital Standard, 미확인, https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/, 접근일 2026-09-24 (원문 미열람)
[^ref-125]: ISO, ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions, 2014, https://www.iso.org/standard/54497.html, 접근일 2026-09-25 (원문 미열람)
[^ref-126]: ASCM, SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment, 미확인, https://scor.ascm.org/performance/reliability/RL.1.1, 접근일 2026-09-25 (원문 미열람)
[^ref-127]: WERC(Warehousing Education and Research Council), WERC DC Measures Survey - 2025, 2025, https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-128]: Computers & Industrial Engineering 게재 논문(저자 미확인), Overall Equipment Effectiveness: consistency of ISO standard with literature, 2020, https://www.sciencedirect.com/science/article/abs/pii/S0360835220302527, 접근일 2026-09-25 (원문 미열람)
[^ref-129]: Project Production Institute, Little’s Law – A Practical Approach to Understanding Production System Performance, 미확인, https://projectproduction.org/journal/littles-law-a-practical-approach-to-understanding-production-system-performance/, 접근일 2026-09-25 (원문 미열람)
[^ref-130]: Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본), Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes, 2023, https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-14 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-14 | 4. 성과·경제성·프로세스 개선 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-25-14/pages/topics/2026/2026-09-25-area04-s6.md

```markdown
---
title: "4. 성과·경제성·프로세스 개선 — 대표 접근법과 기술"
type: topic
category: "A. 업무·공급망 설계"
primary_area_no: 4
related_areas: [1, 2, 3, 8, 16, 19, 22]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-096, ref-098, ref-102, ref-129, ref-130, ref-132, ref-133, ref-135, ref-136]
last_run: 2026-09-25
version: 1
split_from: docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#6
---

[홈](../../index.md) › [주제](../index.md) › 4. 성과·경제성·프로세스 개선 — 대표 접근법과 기술

# 4. 성과·경제성·프로세스 개선 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 성과를 병목과 연결해 해석하는 기본 도구는 리틀의 법칙이며, 임계 재공품을 넘는 투입은 처리량 대신 사이클 타임만 늘린다고 본다. [사실][^ref-129] 그 위에 해석적 모델, 에너지·충전 절충 평가, 병목 탐지, 프로세스 마이닝이 쓰인다.
- 이 페이지는 [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

성과를 병목과 연결해 해석하는 기본 도구는 리틀의 법칙이며, 임계 재공품을 넘는 투입은 처리량 대신 사이클 타임만 늘린다고 본다. [사실][^ref-129] 그 위에 해석적 모델, 에너지·충전 절충 평가, 병목 탐지, 프로세스 마이닝이 쓰인다.

### 해석적 대기행렬 모델

Lamballais·Roy·de Koster(2017)의 RMFS 대기행렬 모델은 최대 주문 처리량·평균 주문 사이클 타임·로봇 가동률을 함께 추정하며, 처리량은 보관 구역 둘레의 작업대 위치에 영향을 받았다. [사실][^ref-096]

Ghelichi·Kilaru(2021)는 협업형 자율이동로봇(Autonomous Mobile Robot, AMR) 피킹 방식 두 가지(라스트 마일 배송형 LMD, 통로 만남형 MIA)의 해석적 모델을 세워, 피킹 주기가 높을 때 LMD가 필요한 로봇 수를 줄이며 MIA는 로봇이 더 필요하지만 작업자 참여를 높인다고 보고했다. [사실][^ref-132] 두 결과 모두 해석적 모델에서 나온 것이다.

### 에너지·충전의 비용 절충

Omega(2024) 게재 RMFS 에너지 연구는 일반·긴급 주문의 동적 우선순위 정책을 평가해 처리량과 에너지 소비 사이에 절충이 있음을 보였다(수치는 5절, 모델·시뮬레이션 조건). [사실][^ref-133] 충전 설비 결정도 비용과 처리 시간의 절충으로 연구되어, RMFS에서는 배터리 비용이 낮으면 배터리 교환이 플러그인 충전보다 저렴했고 [사실][^ref-098], AMR 물류센터 시뮬레이션에서는 충전기가 부족하면 큰 지연이, 과잉이면 불필요한 비용이 생겼다. [사실][^ref-102]

### 처리량 병목 탐지

활성 구간 방법(Roser 외 2001, 2023년 체계적 리뷰를 통한 재인용)은 중단 없이 가장 오래 가동 중인 자원을 순간 병목으로 보고, 버퍼 재고와 결합해 병목 이동을 예측하는 데까지 확장되었다. [사실][^ref-130] 이 방법은 자원별 가동·유휴 시각 기록만으로 계산되므로, ROP가 수집하는 로봇 상태(작업 중·유휴·충전·오류) 기록과 작업대·승강기 이벤트를 쓰면 로봇·작업대·설비 가운데 이동하는 병목을 찾는 데 적용할 수 있을 것으로 보인다. [추정][^ref-130][^ref-135] 제조 라인 중심의 방법이며, 이동로봇·작업대가 섞인 창고에 적용한 사례는 미확인이다.

### 프로세스 마이닝

프로세스 마이닝(Process Mining)은 시스템에 남은 이벤트 로그로 실제 업무 흐름과 병목을 분석한다. 창고 업무 개선 사례 연구(2015, 단일 사례)는 SAP 창고 관리 모듈 테이블에서 이벤트 로그를 뽑아 ProM의 Heuristic Miner로 분석했고, 병목 분석에서 자재가 고층 랙에 오래 머물고 고층 랙 사이를 옮겨 다니는 흐름을 찾았다. [사실][^ref-136] 여러 객체를 함께 다루는 로그 형식은 용어집의 [객체 중심 이벤트 로그(OCEL)](../../glossary/ocel.md)를, 도구는 7절을 참고한다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [2. 공정·워크플로 모델링](../../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md), [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-096]: Lamballais, T., Roy, D., & de Koster, M. B. M., Estimating performance in a Robotic Mobile Fulfillment System, 2017, https://repub.eur.nl/pub/107376/, 접근일 2026-09-25 (원문 미열람)
[^ref-098]: Zou, B., Gong, Y., de Koster, R., & Xu, X., Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system, 2018, https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901, 접근일 2026-09-25 (원문 미열람)
[^ref-102]: Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics, 2025, https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69, 접근일 2026-09-25 (원문 미열람)
[^ref-129]: Project Production Institute, Little’s Law – A Practical Approach to Understanding Production System Performance, 미확인, https://projectproduction.org/journal/littles-law-a-practical-approach-to-understanding-production-system-performance/, 접근일 2026-09-25 (원문 미열람)
[^ref-130]: Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본), Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes, 2023, https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031, 접근일 2026-09-25 (원문 미열람)
[^ref-132]: Ghelichi, Z., & Kilaru, S., Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers, 2021, https://www.sciencedirect.com/science/article/pii/S0307904X20305801, 접근일 2026-09-25 (원문 미열람)
[^ref-133]: Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336, 접근일 2026-09-25 (원문 미열람)
[^ref-135]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25
[^ref-136]: Springer(학술대회 발표 논문, 저자 미확인), Material Movement Analysis for Warehouse Business Process Improvement with Process Mining: A Case Study, 2015, https://link.springer.com/chapter/10.1007/978-3-319-19509-4_9, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-14 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-14 | 4. 성과·경제성·프로세스 개선 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-25-14/pages/topics/2026/2026-09-25-area04-s7.md

```markdown
---
title: "4. 성과·경제성·프로세스 개선 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "A. 업무·공급망 설계"
primary_area_no: 4
related_areas: [1, 2, 3, 8, 16, 19, 22]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-001, ref-106, ref-140, ref-125, ref-126, ref-127, ref-134, ref-135]
last_run: 2026-09-25
version: 1
split_from: docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#7
---

[홈](../../index.md) › [주제](../index.md) › 4. 성과·경제성·프로세스 개선 — 관련 표준·프레임워크·오픈소스

# 4. 성과·경제성·프로세스 개선 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 지표 정의는 ISO 22400-2와 SCOR에서, 계산의 원천 데이터는 로봇·작업 상태 스키마에서 온다. [사실][^ref-125][^ref-126][^ref-135]
- 이 페이지는 [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 지표 정의는 ISO 22400-2와 SCOR에서, 계산의 원천 데이터는 로봇·작업 상태 스키마에서 온다. [사실][^ref-125][^ref-126][^ref-135]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| ISO 22400-2:2014 | 표준 | 제조 운영 관리 KPI(처리율, OEE, 가용성, 품질률, 재고 회전율 등)를 공식·구성 요소·시간 특성·단위와 함께 정의한다(2014판). [사실][^ref-125] | 원문 미열람 |
| SCOR (RL.1.1 완전 고객 주문 이행률) | 표준 | 신뢰성·대응성·비용 같은 성과 속성별로 주문·공급망 단위 성과를 잰다(2026-09-25 확인). [사실][^ref-001][^ref-126] | 원문 미열람 |
| WERC DC Measures | 평가 프로그램 | 정시 출하율, 창고 용량 사용률, 주문 피킹 정확도, 입고–적치 소요 시간 같은 물류센터 운영 지표를 조사하는 것으로 보인다(2025년판). [추정][^ref-127] | 원문 미열람 |
| [Open-RMF](../../glossary/open-rmf.md) API 로봇 상태 스키마(robot_state) | 오픈소스 | 로봇 상태를 uninitialized, offline, shutdown, idle, charging, working, error 일곱 값으로 두고 배터리 충전 상태(0.0~1.0), 현재 작업 id, 운영자가 조치할 문제(issues), 위치, 시각(unix_millis_time)을 함께 보고한다(2026-09-25 확인). [사실][^ref-135] | 원문 열람 |
| Open-RMF API 작업 상태 스키마(task_state) | 오픈소스 | 작업 시작·종료 시각, 최초 예상 소요 시간과 현재 예상 소요 시간, 12개 상태 값, 배정 로봇, 단계, 중단·취소·강제 종료 정보를 담는다(2026-09-25 확인). [사실][^ref-140] | 원문 열람 |
| PM4Py | 오픈소스 | Fraunhofer FIT에서 분사한 Process Intelligence Solutions가 관리하는 파이썬 프로세스 마이닝 라이브러리로, 프로세스 발견 등 알고리즘을 제공하고 OCEL을 선택 기능으로 두며, 공개판은 AGPL-3.0이고 상용 라이선스를 별도로 둔다(2026-09-25 확인). [사실][^ref-134] | 원문 열람 |
| 스마트물류센터 인증제 | 평가 프로그램 | 기반영역에서 성과관리 체계를 평가하고 세부 항목을 5등급(데이터 관리 기반 구축)부터 1등급(자율운영)까지의 단계로 판단한다(2026-09-25 확인). [사실][^ref-106] | 원문 미열람 |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [2. 공정·워크플로 모델링](../../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md), [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-001]: ASCM, SCOR Digital Standard, 미확인, https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/, 접근일 2026-09-24 (원문 미열람)
[^ref-106]: 한국교통연구원(인증스마트물류센터), 인증스마트물류센터, 미확인, https://cslc.koti.re.kr/, 접근일 2026-09-25 (원문 미열람)
[^ref-140]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25
[^ref-125]: ISO, ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions, 2014, https://www.iso.org/standard/54497.html, 접근일 2026-09-25 (원문 미열람)
[^ref-126]: ASCM, SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment, 미확인, https://scor.ascm.org/performance/reliability/RL.1.1, 접근일 2026-09-25 (원문 미열람)
[^ref-127]: WERC(Warehousing Education and Research Council), WERC DC Measures Survey - 2025, 2025, https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-134]: Process Intelligence Solutions (PM4Py GitHub), pm4py — Official public repository for PM4Py (Process Mining for Python) (README), 미확인, https://github.com/process-intelligence-solutions/pm4py, 접근일 2026-09-25
[^ref-135]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-14 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-14 | 4. 성과·경제성·프로세스 개선 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-25-14/pages/topics/2026/2026-09-25-area04-s11.md

```markdown
---
title: "4. 성과·경제성·프로세스 개선 — 열린 질문"
type: topic
category: "A. 업무·공급망 설계"
primary_area_no: 4
related_areas: [1, 2, 3, 8, 16, 19, 22]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-106]
last_run: 2026-09-25
version: 1
split_from: docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#11
---

[홈](../../index.md) › [주제](../index.md) › 4. 성과·경제성·프로세스 개선 — 열린 질문

# 4. 성과·경제성·프로세스 개선 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇 운영 지표와 주문·비용 지표를 연결한 실증 자료가 없다는 점이 이 영역의 가장 큰 공백이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇 운영 지표와 주문·비용 지표를 연결한 실증 자료가 없다는 점이 이 영역의 가장 큰 공백이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- (신규 · 열림 · 제기 2026-09-25 · 실행 2026-09-25-14) 로봇 상태 기록(작업 중·유휴·충전·오류)과 WMS·ERP의 주문 이행 지표(완전 주문 이행률, 주문 이행 사이클 타임)를 같은 기간·같은 주문 단위로 연결해 로봇 도입이 출하량·비용 개선으로 이어졌는지 검증한 공개 사례가 있는가?
- (신규 · 열림 · 제기 2026-09-25 · 실행 2026-09-25-14) 창고 이동로봇 플릿에 ISO 22400식 OEE(가용성·성능·품질)를 적용하는 합의된 정의가 있는가, 충전·대기·교통 정체 시간은 어느 손실로 분류해야 하는가?
- (신규 · 열림 · 제기 2026-09-25 · 실행 2026-09-25-14) 벤더 발표가 아닌 공공·학술 자료로 국내 물류 로봇 도입의 투자 효과(생산성·비용·회수 기간)를 측정한 결과가 있는가?
- (신규 · 열림 · 제기 2026-09-25 · 실행 2026-09-25-14) 이동로봇·작업대·승강기가 섞인 창고 흐름에 활성 구간 기반 이동 병목 탐지나 객체 중심 프로세스 마이닝을 적용한 연구가 있는가?
- **oq-008** (열림 · 제기 2026-09-25 · 실행 2026-09-25-10) 여러 거점 사이에서 로봇을 재배치·공유하거나 성수기에 임대로 보충하는 결정을 다룬 학술·공공 자료나 국내 사례가 있는가? 이번 실행에서도 학술·공공 자료는 확인하지 못했다.
- **oq-011** (열림 · 제기 2026-09-25 · 실행 2026-09-25-10) 스마트물류센터 인증의 세부 평가 지표에 로봇 대수·가동률·처리능력 같은 설비 계획 지표가 포함되는가? 이번 실행에서 부분 보강했다: 기반영역의 성과관리 체계 평가와 등급 판단 기준은 확인했다. [사실][^ref-106] 로봇 대수·가동률 같은 개별 지표의 포함 여부는 여전히 미확인이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [2. 공정·워크플로 모델링](../../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md), [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-106]: 한국교통연구원(인증스마트물류센터), 인증스마트물류센터, 미확인, https://cslc.koti.re.kr/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-14 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-14 | 4. 성과·경제성·프로세스 개선 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-25-14/docs_tree.txt

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
glossary/aggregation-event.md
glossary/ariac.md
glossary/association-event.md
glossary/behavior-tree.md
glossary/business-location.md
glossary/capabilities-skills-services.md
glossary/cbv.md
glossary/cora.md
glossary/dds-security.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/epcis.md
glossary/fleet-adapter.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/giai.md
glossary/grai.md
glossary/index.md
glossary/isa-95.md
glossary/lifelong-mapf.md
glossary/linear-temporal-logic.md
glossary/mapf.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/open-rmf.md
glossary/panoptic-symbol-spotting.md
glossary/pddl.md
glossary/raster-to-vector-conversion.md
glossary/read-point.md
glossary/robotic-mobile-fulfillment-system.md
glossary/scor.md
glossary/semi-open-queueing-network.md
glossary/sscc.md
glossary/task-decomposition.md
glossary/vda-5050.md
glossary/wes-wcs-wms-mes-tms.md
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
standards/index.md
topics/2026/2026-09-25-area03-s11.md
topics/2026/2026-09-25-area03-s6.md
topics/2026/2026-09-25-area03-s7.md
topics/2026/2026-09-25-area03-s8.md
topics/2026/2026-09-25-area07-s6.md
topics/2026/2026-09-25-area07-s7.md
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

### docs/glossary/index.md

```markdown
---
title: "용어집"
type: glossary
subtype: index
status: published
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](../index.md) › 용어집

# 용어집

이 위키에서 쓰는 용어의 한글·영문 표기와 한 줄 정의를 모은다. 용어마다 개별 페이지에 설명, 관련 연구영역, 출처를 둔다. 시드 용어는 SCOR, ISA-95, EPCIS, Open-RMF, Fleet Adapter, WES/WCS/WMS/MES/TMS, MRTA, MAPF, Lifelong MAPF, Multi-Agent Pickup and Delivery, ARIAC, DDS-Security, 디지털 트윈이다. 새 용어는 스토리텔러 에이전트가 제안하고 퍼블리셔가 반영한다.

아래 표는 용어 페이지의 프런트매터(term_ko, term_en, definition, related_areas)에서 자동으로 만든다.

## 용어 목록

<!-- auto:glossary-index:start -->
| 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 |
|---|---|---|---|
| [B2MML](b2mml.md) | Business To Manufacturing Markup Language (B2MML) | MESA International이 ISA-95(IEC 62264)의 데이터 모델을 XML 스키마로 구현한 교환 형식이다. | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) |
| [DDS 보안 규격](dds-security.md) | DDS Security (DDS-Security) | DDS(Data Distribution Service)의 보안 규격으로, ROS 2가 인증·암호화·접근통제 구조의 기반으로 통합했다. | [26. 사이버보안·접근권한·개인정보](../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)<br>[11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) |
| [VDA 5050](vda-5050.md) | VDA 5050 | 독일자동차산업협회(VDA)와 VDMA가 정한 이동로봇(AGV·AMR)과 상위 관제(fleet control) 사이의 통신 인터페이스 권고안이며 현행판은 3.0.0이다. | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) |
| [객체 중심 이벤트 로그](ocel.md) | Object-Centric Event Log (OCEL) | 이벤트와 여러 객체 사이 관계, 관계의 한정자, 시간에 따라 바뀌는 객체 속성을 기록하는 이벤트 로그 교환 표준이며, 2.0판은 SQLite·XML·JSON 형식을 둔다. | [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[19. 모니터링·이상 탐지·원인 분석](../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) |
| [계획 도메인 정의 언어](pddl.md) | Planning Domain Definition Language (PDDL) | 자동 계획 문제에서 행동을 파라미터·전제조건·효과로 기술하고 도메인과 문제 인스턴스를 분리해 표현하는 언어이다. | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) |
| [공급망 운영 참조 모델](scor.md) | Supply Chain Operations Reference (SCOR) | ASCM이 관리하는 공급망 프로세스 참조 모델로, 공급망을 계획·주문·조달·생산/가공·이행·반품 프로세스와 이를 아우르는 오케스트레이션 프로세스로 기술한다. | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) |
| [글로벌 개별 자산 식별자](giai.md) | Global Individual Asset Identifier (GIAI) | 컨테이너·트럭·트레일러 같은 개별 자산을 식별하는 GS1 식별 키이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) |
| [글로벌 반환형 자산 식별자](grai.md) | Global Returnable Asset Identifier (GRAI) | 팔레트·상자·트레이·케그처럼 여러 번 재사용되는 운반구를 식별하는 GS1 식별 키이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) |
| [기업–제어 시스템 통합 표준](isa-95.md) | ISA-95 Enterprise-Control System Integration | 국제자동화협회(ISA)가 제정한, 기업 업무 시스템과 제조 운영·제어 시스템의 통합을 다루는 표준 시리즈이다. | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) |
| [능력·스킬·서비스 모델](capabilities-skills-services.md) | Capabilities, Skills and Services (CSS) Model | Plattform Industrie 4.0 작업반이 제안한 정보 모델로, 구현과 무관한 기능 명세(능력)와 그 실행 가능한 구현(스킬), 제공 형태(서비스)를 구분한다. 이 위키의 온톨로지 초안에서는 CSS의 능력(capability)을 기능(Capability)으로 부른다. | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) |
| [다중 로봇 작업 배정](mrta.md) | Multi-Robot Task Allocation (MRTA) | 여러 로봇과 여러 작업이 있을 때 어떤 로봇(또는 로봇 팀)이 어떤 작업을 맡을지 정하는 문제이다. | [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) |
| [다중 에이전트 경로 찾기](mapf.md) | Multi-Agent Path Finding (MAPF) | 여러 에이전트(로봇)가 각자의 출발지에서 목적지까지 서로 충돌하지 않고 동시에 따라갈 수 있는 경로들을 계획하는 문제이다. | [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) |
| [다중 에이전트 픽업·배송](multi-agent-pickup-and-delivery.md) | Multi-Agent Pickup and Delivery (MAPD) | 픽업 위치와 배송 위치가 있는 작업이 온라인으로 계속 들어올 때, 에이전트에 작업을 배정하고 충돌 없는 경로를 함께 계획하는 문제이다. | [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) |
| [디지털 트윈](digital-twin.md) | Digital Twin | 물리적 대상(장비·자재·공정·설비·제품 등)을 데이터로 연결된 가상 모델로 표현한 것이다. | [22. 시뮬레이션·예측용 디지털 트윈](../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)<br>[8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) |
| [래스터–벡터 변환](raster-to-vector-conversion.md) | Raster-to-Vector Conversion | 픽셀 이미지로 된 평면도를 벽 선분·교차점·방 다각형 같은 기하 요소의 벡터 표현으로 바꾸는 처리이다. | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) |
| [로봇 이동형 풀필먼트 시스템](robotic-mobile-fulfillment-system.md) | Robotic Mobile Fulfillment System (RMFS) | 로봇이 상품을 담은 이동식 선반(pod)을 작업대까지 옮기고 작업자가 그 앞에서 피킹·보충하는 부품-작업자(parts-to-picker) 방식의 자동화 창고 시스템이다. | [3. 처리능력·거점·설비 계획](../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) |
| [로봇·자동화 핵심 온톨로지](cora.md) | Core Ontology for Robotics and Automation (CORA) | IEEE 1872-2015가 정한 로봇·자동화 분야의 가장 일반적인 개념·관계·공리를 담은 핵심 온톨로지이다. | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) |
| [물류 단위 일련 코드](sscc.md) | Serial Shipping Container Code (SSCC) | 케이스·팔레트·소포 등 보관·운송을 위해 묶인 물류 단위를 고유하게 식별하는 18자리 GS1 식별 키이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) |
| [반개방형 대기행렬 네트워크](semi-open-queueing-network.md) | Semi-Open Queueing Network (SOQN) | 외부에서 주문이 들어오되 로봇 같은 한정된 자원 수가 고정된 채 순환하는 시스템의 처리량·대기 시간을 해석적으로 추정하는 대기행렬 모델이다. | [3. 처리능력·거점·설비 계획](../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) |
| [비즈니스 프로세스 모델 및 표기법](bpmn.md) | Business Process Model and Notation (BPMN) | OMG가 정한 업무 프로세스 표기법으로, ISO/IEC 19510:2013은 OMG BPMN 2.0.1을 PAS 절차로 국제표준화한 것이다. | [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) |
| [산업 자동화용 민첩 로봇 경진대회](ariac.md) | Agile Robotics for Industrial Automation Competition (ARIAC) | NIST가 운영하는 로봇 경진대회로, 변화하는 제조 환경에서 로봇의 계획·인식·행동과 적응성을 평가한다. | [23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)<br>[22. 시뮬레이션·예측용 디지털 트윈](../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)<br>[20. 예외 복구·재계획·업무 연속성](../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) |
| [선형 시간 논리](linear-temporal-logic.md) | Linear Temporal Logic (LTL) | 작업의 순서·시간 제약을 명확한 의미로 기술하는 형식 논리이다. | [27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)<br>[23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) |
| [업무 위치](business-location.md) | Business Location (EPCIS bizLocation) | EPCIS 이벤트 뒤 다른 이벤트가 반박할 때까지 객체가 있다고 보는 업무상 위치를 나타내는 선택 필드이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) |
| [연결 이벤트](association-event.md) | AssociationEvent | 물리 객체를 상위 객체나 특정 물리 위치와 연결하거나 연결을 해제한 사실을 기록하는 EPCIS 2.0 이벤트 유형이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) |
| [오픈 RMF](open-rmf.md) | Open-RMF (Open Robotics Middleware Framework) | ROS 2 기반의 다중 로봇 조율 프레임워크로, 제조사별 플릿 어댑터와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결하고 작업·교통을 조율한다. | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)<br>[15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) |
| [워크플로 넷](workflow-net.md) | Workflow Net (WF-net) | 워크플로를 모델링·분석하는 표준적 방법 가운데 하나로 쓰이는 페트리 넷의 한 부류이다. | [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) |
| [이산 사건 시뮬레이션](discrete-event-simulation.md) | Discrete Event Simulation (DES) | 주문 도착·작업 완료 같은 사건이 일어나는 시점마다 시스템 상태를 갱신해 처리량·대기·가동률을 실험하는 시뮬레이션 방식이다. | [3. 처리능력·거점·설비 계획](../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[22. 시뮬레이션·예측용 디지털 트윈](../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) |
| [작업 분해](task-decomposition.md) | Task Decomposition | 상위 지시나 목표를 로봇이 실행할 수 있는 하위 작업·동작의 순서나 구조로 나누는 일이다. | [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) |
| [전자 제품 코드 정보 서비스](epcis.md) | Electronic Product Code Information Services (EPCIS) | GS1이 정한, 제품·자산의 상태·위치·이동·인계에 관한 이벤트를 기록하고 공유하기 위한 표준이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) |
| [지속형 다중 에이전트 경로 찾기](lifelong-mapf.md) | Lifelong Multi-Agent Path Finding (Lifelong MAPF) | 에이전트가 목적지에 도착하면 곧바로 새 목적지를 받아 계속 이동하는 조건에서 충돌 없는 경로를 계속 계획하는 MAPF의 변형이다. | [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) |
| [집계 이벤트](aggregation-event.md) | AggregationEvent | 상자를 팔레트에 싣거나 내리는 것처럼 상위 객체와 하위 객체의 물리적 결합·분리를 기록하는 EPCIS 이벤트 유형이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) |
| [차량 소요대수 산정](fleet-sizing.md) | Fleet Sizing | 예상 물동량과 서비스 수준(대기 시간·처리량) 목표를 만족하는 데 필요한 로봇·운반 차량의 최소 대수를 정하는 계획 문제이다. | [3. 처리능력·거점·설비 계획](../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) |
| [창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템](wes-wcs-wms-mes-tms.md) | Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System | 창고·생산·운송의 주문·재고·설비·공정을 관리하거나 실행하는 업무·실행 시스템 계열의 약어이며, ROP는 이들에서 작업 요청을 받아 로봇 작업으로 바꾸고 결과를 되돌려 주는 관계에 있다. | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) |
| [파놉틱 심볼 스포팅](panoptic-symbol-spotting.md) | Panoptic Symbol Spotting | CAD 도면의 선 요소마다 문·창문 같은 셀 수 있는 기호의 개별 인스턴스와 벽 같은 셀 수 없는 영역의 의미를 함께 판별하는 과제이다. | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) |
| [판독 지점](read-point.md) | Read Point (EPCIS readPoint) | EPCIS 이벤트가 일어난 지점을 나타내는 선택 필드이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) |
| [평면도 인식](floor-plan-recognition.md) | Floor Plan Recognition | 평면도 이미지나 CAD 도면에서 벽·문·창문·계단 같은 건축 요소와 방 영역·유형을 자동으로 찾아내 구조화하는 작업이다. | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) |
| [플릿 어댑터](fleet-adapter.md) | Fleet Adapter | Open-RMF에서 제조사별 로봇 플릿(같은 관제 아래 묶인 로봇 무리)을 연결하기 위해 두는 제조사별 연결 구성요소이다. | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[21. 온보딩·설정·현장 시운전](../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) |
| [핵심 업무 어휘](cbv.md) | Core Business Vocabulary (CBV) | EPCIS 이벤트의 업무 단계·상태·인계 유형 등에 채울 표준 어휘 값을 정한 GS1 표준(ISO/IEC 19988)이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) |
| [행동 트리](behavior-tree.md) | Behavior Tree | 로봇 동작과 조건 확인을 트리 노드로 조합해 실행 구조를 표현하는 형식이다. | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) |
<!-- auto:glossary-index:end -->
```

### docs/references/index.md

```markdown
---
title: "참고문헌"
type: reference
subtype: index
status: published
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](../index.md) › 참고문헌

# 참고문헌

이 위키가 인용한 출처의 목록이다. 출처마다 id, 기관, 제목, 발행일, URL, 유형, 신뢰도, 접근일, 요약, 인용된 페이지를 개별 페이지에 둔다. 시드 10건(ref-001 ~ ref-010)은 분류 원문 12장의 참고 자료 1~10번에 그대로 대응한다. 새 출처는 리서치 에이전트가 제안하고 내용 검증 에이전트가 실재를 확인한 뒤 퍼블리셔가 추가한다.

신뢰도는 출처 유형을 기준으로 한다. 표준·정부·연구기관·논문·오픈소스 공식 문서는 high, 기사·보도자료·벤더 문서는 medium 이며, 내용 검증 에이전트가 원문을 열어 확인하면 조정할 수 있다. 다만 URL 을 열어 확인하지 못한 출처(원문 미열람)에는 유형과 무관하게 high 를 주지 않고 medium 상한을 적용한다. 시드 10건은 구축 환경의 네트워크 정책으로 URL 을 열지 못했으므로 모두 원문 미열람 상태이며, 각 페이지의 "원문 열람" 행에 그 사실을 적어 둔다. 외부 접속이 가능한 환경에서 `ROP_CHECK_URLS=1 bash pipeline/checks/run_all.sh` 를 실행한 뒤 `python3 pipeline/scaffold.py --apply-url-check` 를 실행하면 열림이 확인된 출처의 신뢰도가 유형 기준값으로 올라간다.

## 목록

<!-- auto:references-index:start -->
| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL |
|---|---|---|---|---|---|---|---|
| [ref-001](ref-001.md) | ASCM | SCOR Digital Standard | 미확인 | 표준 | medium | 2026-09-24 | <https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/> |
| [ref-002](ref-002.md) | ISA | Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems | 2025 | 기사 | medium | 2026-09-24 | <https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of> |
| [ref-003](ref-003.md) | GS1 | EPCIS and CBV Linked Data Model | 미확인 | 표준 | medium | 2026-09-24 | <https://ref.gs1.org/epcis/> |
| [ref-004](ref-004.md) | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://osrf.github.io/ros2multirobotbook/rmf-core.html> |
| [ref-005](ref-005.md) | Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding in Large-Scale Warehouses | 2020 | 논문 | medium | 2026-09-24 | <https://arxiv.org/abs/2005.07371> |
| [ref-006](ref-006.md) | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 2017 | 논문 | medium | 2026-09-24 | <https://arxiv.org/abs/1705.10868> |
| [ref-007](ref-007.md) | NIST | Performance of Collaborative Robot Systems | 미확인 | 정부·연구기관 | medium | 2026-09-24 | <https://www.nist.gov/programs-projects/performance-collaborative-robot-systems> |
| [ref-008](ref-008.md) | NIST | ARIAC Documentation | 미확인 | 정부·연구기관 | high | 2026-09-25 | <https://pages.nist.gov/ARIAC_docs/en/latest/> |
| [ref-009](ref-009.md) | ROS 2 Design | ROS 2 DDS-Security Integration | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://design.ros2.org/articles/ros2_dds_security.html> |
| [ref-010](ref-010.md) | ROS 2 Design | ROS 2 Robotic Systems Threat Model | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://design.ros2.org/articles/ros2_threat_model.html> |
| [ref-011](ref-011.md) | ISO/IEC | ISO/IEC 19987:2024 - Information technology — EPC Information Services (EPCIS) | 2024-03 | 표준 | medium | 2026-09-25 | <https://www.iso.org/standard/85557.html> |
| [ref-012](ref-012.md) | ISO/IEC | ISO/IEC 19988:2024 - Information technology — GS1 Core Business Vocabulary (CBV) | 2024 | 표준 | medium | 2026-09-25 | <https://www.iso.org/standard/85558.html> |
| [ref-013](ref-013.md) | OpenEPCIS | EPCIS 2.0 and EPCIS 1.2 \| OpenEPCIS Docs | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://openepcis.io/docs/epcis/> |
| [ref-014](ref-014.md) | GS1 | Core Business Vocabulary (CBV) Standard | 미확인 | 표준 | medium | 2026-09-25 | <https://ref.gs1.org/standards/cbv/> |
| [ref-015](ref-015.md) | GS1 | EPCIS and CBV Implementation Guideline | 미확인 | 표준 | medium | 2026-09-25 | <https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf> |
| [ref-016](ref-016.md) | GS1 | Serial Shipping Container Code (SSCC) | 미확인 | 표준 | medium | 2026-09-25 | <https://www.gs1.org/standards/id-keys/sscc> |
| [ref-017](ref-017.md) | GS1 Korea(대한상공회의소 유통물류진흥원) | SSCC (Serial Shipping Container Code) GS1 Information Vol. 21 | 2019-09 | 표준 | medium | 2026-09-25 | <http://www.gs1kr.org/front/service/File/SSCC%20%EB%B0%9C%EA%B0%84%20%EC%9E%90%EB%A3%8C.pdf> |
| [ref-018](ref-018.md) | GS1 | GS1 Logistic Label Guideline | 미확인 | 표준 | medium | 2026-09-25 | <https://www.gs1.org/docs/tl/GS1_Logistic_Label_Guideline.pdf> |
| [ref-019](ref-019.md) | GS1 | Global Returnable Asset Identifier (GRAI) | 미확인 | 표준 | medium | 2026-09-25 | <https://www.gs1.org/standards/id-keys/grai> |
| [ref-020](ref-020.md) | GS1 | Which GS1 identification key should be used for individual assets used to transport goods? (GS1 GO Customer Service Portal) | 미확인 | 표준 | medium | 2026-09-25 | <https://support.gs1.org/support/solutions/articles/43000734294-which-gs1-identification-key-should-be-used-for-individual-assets-used-to-transport-goods-> |
| [ref-021](ref-021.md) | GS1 | EPC Tag Data Standard | 미확인 | 표준 | medium | 2026-09-25 | <https://www.gs1.org/sites/default/files/docs/epc/GS1_EPC_TDS_i1_11.pdf> |
| [ref-022](ref-022.md) | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 2022-01 | 표준 | medium | 2026-09-25 | <https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf> |
| [ref-023](ref-023.md) | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://osrf.github.io/ros2multirobotbook/integration_workcells.html> |
| [ref-024](ref-024.md) | Singh, J. 외 | RFID tag readability issues with palletized loads of consumer goods | 2009 | 논문 | medium | 2026-09-25 | <https://onlinelibrary.wiley.com/doi/abs/10.1002/pts.864> |
| [ref-025](ref-025.md) | IEEE | 1872-2015 - IEEE Standard Ontologies for Robotics and Automation | 2015 | 표준 | medium | 2026-09-25 | <https://ieeexplore.ieee.org/document/7084073/> |
| [ref-026](ref-026.md) | IEEE | IEEE 1872.2-2021 - IEEE Standard for Autonomous Robotics (AuR) Ontology | 2022 | 표준 | medium | 2026-09-25 | <https://standards.ieee.org/standard/1872_2-2021.html> |
| [ref-027](ref-027.md) | Beetz, M., Beßler, D., Haidu, A., Pomarlan, M., Bozcuoglu, A. K., & Bartels, G. | KnowRob 2.0 — A 2nd Generation Knowledge Processing Framework for Cognition-Enabled Robotic Agents | 2018 | 논문 | medium | 2026-09-25 | <https://ai.uni-bremen.de/papers/beetz18knowrob.pdf> |
| [ref-028](ref-028.md) | Beßler, D. 외 | Foundations of the Socio-physical Model of Activities (SOMA) for Autonomous Robotic Agents | 2021 | 논문 | medium | 2026-09-25 | <https://arxiv.org/pdf/2011.11972> |
| [ref-029](ref-029.md) | McDermott, D. 외 | PDDL - The Planning Domain Definition Language | 1998 | 논문 | medium | 2026-09-25 | <https://www.researchgate.net/publication/2278933_PDDL_-_The_Planning_Domain_Definition_Language> |
| [ref-030](ref-030.md) | W3C / OGC | Semantic Sensor Network Ontology | 2017-10-19 | 표준 | medium | 2026-09-25 | <https://www.w3.org/TR/vocab-ssn/> |
| [ref-031](ref-031.md) | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | <https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md> |
| [ref-032](ref-032.md) | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04 | 표준 | medium | 2026-09-25 | <https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN> |
| [ref-033](ref-033.md) | MassRobotics | Autonomous Mobile Robot Standards Published by MassRobotics | 2021-05 | 표준 | medium | 2026-09-25 | <https://www.massrobotics.org/autonomous-mobile-robot-standards-published-by-massrobotics/> |
| [ref-034](ref-034.md) | OPC Foundation / VDMA | OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration | 미확인 | 표준 | medium | 2026-09-25 | <https://reference.opcfoundation.org/specs/OPC-40010-1> |
| [ref-035](ref-035.md) | Plattform Industrie 4.0 | Information Model for Capabilities, Skills & Services | 2022-11 | 정부·연구기관 | medium | 2026-09-25 | <https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html> |
| [ref-036](ref-036.md) | Köcher, A. 외 | A Reference Model for Common Understanding of Capabilities and Skills in Manufacturing | 2022 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2209.09632> |
| [ref-037](ref-037.md) | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 2023-07 | 논문 | low | 2026-09-25 | <https://arxiv.org/abs/2307.00827> |
| [ref-038](ref-038.md) | Vieira da Silva, L. M., Köcher, A., & Fay, A. | A Capability and Skill Model for Heterogeneous Autonomous Robots | 2022-09 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2209.10900> |
| [ref-039](ref-039.md) | Open Robotics | Currently supported Tasks - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://osrf.github.io/ros2multirobotbook/task_types.html> |
| [ref-040](ref-040.md) | Open Robotics | PerformAction Tutorial - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html> |
| [ref-041](ref-041.md) | Naqvi, M. R. 외(Scientific Reports) | Ontology-driven integration of advertised and operational capabilities in robots | 2025-10-02 | 논문 | medium | 2026-09-25 | <https://www.nature.com/articles/s41598-025-16649-3> |
| [ref-042](ref-042.md) | Aguado, E., Gomez, V., Hernando, M., Rossi, C., & Sanz, R. | A survey of ontology-enabled processes for dependable robot autonomy | 2024-07 | 논문 | medium | 2026-09-25 | <https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1377897/full> |
| [ref-043](ref-043.md) | 신민종, 한영석, 정재윤 | 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계 | 2024 | 논문 | medium | 2026-09-25 | <https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560> |
| [ref-044](ref-044.md) | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | 표준 | high | 2026-09-25 | <https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl> |
| [ref-045](ref-045.md) | GS1 | gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) | 2021-09-30 | 표준 | high | 2026-09-25 | <https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl> |
| [ref-047](ref-047.md) | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequest.msg> |
| [ref-048](ref-048.md) | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequestItem.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequestItem.msg> |
| [ref-049](ref-049.md) | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg> |
| [ref-050](ref-050.md) | Auto-ID Labs Korea(세종대학교), Byun, J. | Oliot EPCIS for GS1 EPCIS/CBV 2.0.0 (GitHub JaewookByun/epcis README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/JaewookByun/epcis> |
| [ref-051](ref-051.md) | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-09-25 | <https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema> |
| [ref-052](ref-052.md) | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — README.md | 미확인 | 표준 | high | 2026-09-25 | <https://github.com/VDA5050/VDA5050/blob/main/README.md> |
| [ref-053](ref-053.md) | NVIDIA Research (NVlabs) | progprompt-vh — ProgPrompt: Generating Situated Robot Task Plans using Large Language Models (GitHub README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/NVlabs/progprompt-vh> |
| [ref-054](ref-054.md) | Singh, I. 외 | ProgPrompt: Generating Situated Robot Task Plans using Large Language Models | 2022-09 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2209.11302> |
| [ref-055](ref-055.md) | Brown University H2R Lab | Lang2LTL — Code for paper Lang2LTL: Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments (GitHub README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/h2r/Lang2LTL> |
| [ref-056](ref-056.md) | Liu, J. X. 외 | Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments | 2023-02 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2302.11649> |
| [ref-057](ref-057.md) | Tellex, S. 외 | Understanding Natural Language Commands for Robotic Navigation and Mobile Manipulation | 2011-08 | 논문 | medium | 2026-09-25 | <https://ojs.aaai.org/index.php/AAAI/article/view/7979> |
| [ref-058](ref-058.md) | Cohen, V., Liu, J. X., Mooney, R., Tellex, S., & Watkins, D. | A Survey of Robotic Language Grounding: Tradeoffs between Symbols and Embeddings | 2024-08 | 논문 | medium | 2026-09-25 | <https://www.ijcai.org/proceedings/2024/885> |
| [ref-059](ref-059.md) | Wang, Y. 외(DART-LLM 저자) | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 2024-11 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2411.09022> |
| [ref-060](ref-060.md) | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026 | 논문 | medium | 2026-09-25 | <https://doi.org/10.1177/20552076261437181> |
| [ref-061](ref-061.md) | Izzo, R. A., Bardaro, G., & Matteucci, M. (Politecnico di Milano AIRLab) | BTGenBot: Behavior Tree Generation for Robotic Tasks with Lightweight LLMs | 2024-03 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2403.12761> |
| [ref-062](ref-062.md) | CubiCasa (Kalervo, A. 외) | CubiCasa5k — README (CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/CubiCasa/CubiCasa5k> |
| [ref-063](ref-063.md) | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 2019-04 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/1904.01920> |
| [ref-064](ref-064.md) | Zeng, Z., Li, X., Yu, Y. K., & Fu, C.-W. | DeepFloorplan — README (Deep Floor Plan Recognition using a Multi-task Network with Room-boundary-Guided Attention) | 2019 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/zlzeng/DeepFloorplan> |
| [ref-065](ref-065.md) | Liu, C., Wu, J., Kohli, P., & Furukawa, Y. | FloorplanTransformation — README (Raster-to-Vector: Revisiting Floorplan Transformation) | 2017 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/art-programmer/FloorplanTransformation> |
| [ref-066](ref-066.md) | FloorPlanCAD 프로젝트(Fan, Z. 외) | FloorPlanCAD Dataset — project page (floorplancad.github.io index.md) | 2021 | 오픈소스 문서 | medium | 2026-09-25 | <https://floorplancad.github.io/> |
| [ref-067](ref-067.md) | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 2021-05 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2105.07147> |
| [ref-068](ref-068.md) | Voxel51 (Hugging Face) | Voxel51/FloorPlanCAD · Datasets at Hugging Face | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://huggingface.co/datasets/Voxel51/FloorPlanCAD> |
| [ref-069](ref-069.md) | Pizarro, P. N., Hitschfeld, N., & Sipiran, I. (MLSTRUCT) | MLStructFP — README (Large-scale multi-unit floor plan dataset for architectural plan analysis and recognition) | 2023 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/MLSTRUCT/MLStructFP> |
| [ref-070](ref-070.md) | Hu, S. 외 | Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer) | 2024 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/SizheHu/Raster-to-Graph> |
| [ref-071](ref-071.md) | Agour, M. 외 (ResPlan) | ResPlan — README (ResPlan: A Large-Scale Vector-Graph Dataset of 17,000 Residential Floor Plans) | 2025-08 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/m-agour/ResPlan> |
| [ref-072](ref-072.md) | van Engelenburg, C. 외 (MSD) | msd — README (MSD: A Benchmark Dataset for Floor Plan Generation of Building Complexes) | 2024 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/caspervanengelenburg/msd> |
| [ref-073](ref-073.md) | Luo, R. 외 | ArchCAD-400K: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting | 2025-03 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2503.22346> |
| [ref-074](ref-074.md) | 한국지능정보사회진흥원(AI Hub) | 건축 도면 데이터 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | <https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71465> |
| [ref-075](ref-075.md) | de las Heras, L.-P., Terrades, O. R., Robles, S., & Sánchez, G. | CVC-FP and SGT: a new database for structural floor plan analysis and its groundtruthing tool | 2015 | 논문 | medium | 2026-09-25 | <https://www.researchgate.net/publication/270597635_CVC-FP_and_SGT_a_new_database_for_structural_floor_plan_analysis_and_its_groundtruthing_tool> |
| [ref-076](ref-076.md) | DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S. | Vision Language Models Can Parse Floor Plan Maps | 2024-09 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2409.12842> |
| [ref-077](ref-077.md) | DoorDet 저자(arXiv 2508.07714) | DoorDet: Semi-Automated Multi-Class Door Detection Dataset via Object Detection and Large Language Models | 2025-08 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2508.07714> |
| [ref-078](ref-078.md) | Kratochvila, L., de Jong, G., Arkesteijn, M., Zemcik, T., Bilik, S., Horak, K., & Rellermeyer, J. S. | Multi-Unit Floor Plan Recognition and Reconstruction Using Improved Semantic Segmentation of Raster-Wise Floor Plans | 2024-08 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2408.01526> |
| [ref-087](ref-087.md) | Google Research | SayCan (google-research/saycan README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/google-research/google-research/blob/master/saycan/README.md> |
| [ref-088](ref-088.md) | Ahn, M. 외(Google) | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022-04 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2204.01691> |
| [ref-089](ref-089.md) | SMARTlab-Purdue (Purdue University) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/SMARTlab-Purdue/SMART-LLM> |
| [ref-090](ref-090.md) | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2309.10062> |
| [ref-091](ref-091.md) | Cranial-XIX (LLM+P 저자) | llm-pddl — LLM+P: Empowering Large Language Models with Optimal Planning Proficiency (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/Cranial-XIX/llm-pddl> |
| [ref-092](ref-092.md) | Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P. | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2304.11477> |
| [ref-093](ref-093.md) | Huang, W., Abbeel, P., Pathak, D., & Mordatch, I. | Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents | 2022-07 | 논문 | medium | 2026-09-25 | <https://proceedings.mlr.press/v162/huang22a.html> |
| [ref-094](ref-094.md) | Huang, W. (language-planner 공식 저장소) | language-planner — Official Code for "Language Models as Zero-Shot Planners" (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/huangwl18/language-planner> |
| [ref-095](ref-095.md) | Google Research | Code as Policies: Language Model Programs for Embodied Control (google-research/code_as_policies README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/google-research/google-research/blob/master/code_as_policies/README.md> |
| [ref-096](ref-096.md) | Lamballais, T., Roy, D., & de Koster, M. B. M. | Estimating performance in a Robotic Mobile Fulfillment System | 2017 | 논문 | medium | 2026-09-25 | <https://repub.eur.nl/pub/107376/> |
| [ref-097](ref-097.md) | Lamballais, T., Roy, D., & de Koster, M. B. M. | Inventory allocation in robotic mobile fulfillment systems | 2020 | 논문 | medium | 2026-09-25 | <https://www.tandfonline.com/doi/abs/10.1080/24725854.2018.1560517> |
| [ref-098](ref-098.md) | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 2018 | 논문 | medium | 2026-09-25 | <https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901> |
| [ref-099](ref-099.md) | Le-Anh, T., & de Koster, M. B. M. | A review of design and control of automated guided vehicle systems | 2006 | 논문 | medium | 2026-09-25 | <https://www.sciencedirect.com/science/article/abs/pii/S0377221705001840> |
| [ref-100](ref-100.md) | Vis, I. F. A. | Survey of research in the design and control of automated guided vehicle systems | 2006 | 논문 | medium | 2026-09-25 | <https://www.sciencedirect.com/science/article/abs/pii/S0377221704006459> |
| [ref-101](ref-101.md) | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/merschformann/RAWSim-O> |
| [ref-102](ref-102.md) | Springer(FAIM 2025 발표 논문, 저자 미확인) | Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics | 2025 | 논문 | medium | 2026-09-25 | <https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69> |
| [ref-103](ref-103.md) | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | 논문 | medium | 2026-09-25 | <https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/> |
| [ref-104](ref-104.md) | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/open-rmf/rmf_demos> |
| [ref-105](ref-105.md) | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml> |
| [ref-106](ref-106.md) | 한국교통연구원(인증스마트물류센터) | 인증스마트물류센터 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | <https://cslc.koti.re.kr/> |
| [ref-107](ref-107.md) | 법제처 국가법령정보센터 | 물류시설의 개발 및 운영에 관한 법률 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | <https://www.law.go.kr/LSW/lsInfoP.do?lsId=000091> |
| [ref-108](ref-108.md) | 이문수, 채준재(로지스틱스연구) | AGV 기반 제조물류시스템의 성능평가를 위한 해석적 모형에 관한 연구 - 반도체 Tandem 레이아웃 시스템을 중심으로 - | 2010 | 논문 | medium | 2026-09-25 | <https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001485142> |
| [ref-109](ref-109.md) | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 2024-06 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2406.17003> |
| [ref-110](ref-110.md) | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://osrf.github.io/ros2multirobotbook/task_new.html> |
| [ref-111](ref-111.md) | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json> |
| [ref-112](ref-112.md) | OMG(Object Management Group) | About the Business Process Model And Notation Specification Version 2.0 | 미확인 | 표준 | medium | 2026-09-25 | <https://www.omg.org/spec/BPMN/2.0/About-BPMN> |
| [ref-113](ref-113.md) | Camunda | Messages \| Camunda 8 Docs (camunda-docs: docs/components/concepts/messages.md) | 미확인 | 벤더 문서 | medium | 2026-09-25 | <https://docs.camunda.io/docs/components/concepts/messages/> |
| [ref-114](ref-114.md) | Corradini, F., Pettinari, S., Re, B., Rossi, L., & Tiezzi, F. | A BPMN-driven framework for Multi-Robot System development | 2023 | 논문 | medium | 2026-09-25 | <https://www.sciencedirect.com/science/article/abs/pii/S0921889022002111> |
| [ref-116](ref-116.md) | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2603.15427> |
| [ref-117](ref-117.md) | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 2023 | 표준 | high | 2026-09-25 | <https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd> |
| [ref-118](ref-118.md) | MESA International | B2MML-BatchML — Schema/B2MML-OperationsDefinition.xsd | 미확인 | 표준 | high | 2026-09-25 | <https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-OperationsDefinition.xsd> |
| [ref-119](ref-119.md) | IEC / ISO | IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management | 2016 | 표준 | medium | 2026-09-25 | <https://www.iso.org/standard/67480.html> |
| [ref-121](ref-121.md) | Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022) | The complexity of soundness in workflow nets | 2022 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2201.05588> |
| [ref-122](ref-122.md) | arXiv:2403.01975 저자(미확인) | OCEL (Object-Centric Event Log) 2.0 Specification | 2024-03 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2403.01975> |
| [ref-123](ref-123.md) | ASCM | SCOR Model — Fulfill F1.3 Pick Product | 미확인 | 표준 | medium | 2026-09-25 | <https://scor.ascm.org/processes/fulfill/F1.3> |
| [ref-124](ref-124.md) | 국가물류통합정보센터(국토교통부) | 스마트물류센터 인증제 안내 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | <https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW> |
<!-- auto:references-index:end -->
```

### docs/open-questions.md

```markdown
---
title: "열린 질문"
type: questions
status: published
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](index.md) › 열린 질문

# 열린 질문

아직 해결되지 않은 질문의 목록이다. 질문마다 관련 영역, 제기일, 제기한 실행, 상태(열림 / 조사 중 / 해결 / 보류), 해결 시 링크를 둔다. 세 에이전트 모두 질문을 제기할 수 있고, 해결 판정은 내용 검증 에이전트가 한다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시한 뒤 여기에 올린다. 새 세부영역이 필요해 보이면 분류를 바꾸지 않고 "분류 확장 제안"으로 여기에 기록한다.

중점 연구 트랙 전용 질문은 트랙의 질문 백로그에 두고, 여기에는 링크만 둔다. 이 표는 `data/open_questions.json` 에서 자동으로 만든다.

## 목록

<!-- auto:open-questions:start -->
| id | 질문 | 관련 영역 | 제기일 | 제기한 실행 | 상태 | 해결 시 링크 |
|---|---|---|---|---|---|---|
| oq-001 | 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[17. 로봇 간 협업·물리적 인계](categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-01 | 열림 | — |
| oq-002 | 국내 물류센터에서 SSCC 라벨이나 EPCIS 이벤트를 로봇 작업 결과(적재·하역 완료)와 연결해 운영하는 사례가 있는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | 2026-09-25 | 2026-09-25-01 | 열림 | — |
| oq-003 | 로봇·게이트의 바코드·RFID 판독 실패나 오판독이 생기면 인계 확정을 보류·재스캔·사람 확인 중 어떤 기준으로 처리해야 하는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | 2026-09-25 | 2026-09-25-01 | 열림 | — |
| oq-004 | IEEE 1872 계열 로봇 온톨로지 표준이나 AAS 능력 서브모델을 KS로 부합화했거나 국내 로봇 관제 사업에 적용한 사례가 있는가? | [28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[5. 로봇 능력·작업 온톨로지](categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | 2026-09-25 | 2026-09-25-02 | 열림 | — |
| oq-005 | 출처 충돌: VDA 5050 3.0.0의 정확한 발행일은 언제인가? 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 2026-04-21 계열이다. | [9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-02 | 열림 | — |
| oq-006 | CBV의 loading·unloading이 운송 수단 적재로 정의되어 있을 때 시설 안 로봇의 적재·운반·하역은 어떤 업무 단계(bizStep) 값이나 사용자 정의 어휘로 기록해야 하는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[17. 로봇 간 협업·물리적 인계](categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) | 2026-09-25 | 2026-09-25-03 | 열림 | — |
| oq-007 | VDA 5050 3.0.0에서 관제가 loadId를 정할 때 SSCC 같은 GS1 키를 그대로 쓰도록 권고하거나 제약하는 규정이 있는가, 로봇이 판독한 식별자와 다르면 어떻게 보고하는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-03 | 열림 | — |
| oq-008 | 여러 거점 사이에서 로봇을 재배치·공유하거나 성수기에 임대로 보충하는 결정을 다룬 학술·공공 자료나 국내 사례가 있는가? | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 2026-09-25-10 | 열림 | — |
| oq-009 | 교대조별 작업자 수와 로봇·작업대 수를 함께 정하는 처리능력 계획 모델이나 사례가 있는가? | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[18. 사람–로봇 협업·운영 인터페이스](categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | 2026-09-25 | 2026-09-25-10 | 열림 | — |
| oq-010 | 국내 다층 물류센터에서 화물용 승강기나 층간 반송 설비가 로봇 처리량의 병목이 된다는 정량 자료가 있는가, 병원·호텔 사례의 승강기 혼잡 결과를 물류센터에 옮길 수 있는가? | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | 2026-09-25 | 2026-09-25-10 | 열림 | — |
| oq-011 | 스마트물류센터 인증의 세부 평가 지표에 로봇 대수·가동률·처리능력 같은 설비 계획 지표가 포함되는가? | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 2026-09-25-10 | 열림 | — |
| oq-012 | 국내 물류센터는 로봇의 운반 완료와 WMS의 입고·인수 확정을 별도 단계로 두는가, 그렇다면 두 단계를 잇는 식별 키와 확정 대기 시간 기준은 무엇인가? | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | 2026-09-25 | 2026-09-25-09 | 열림 | — |
| oq-013 | ISA-95 세그먼트 의존 유형(B2MML DependencyType)을 입고·적치·피킹·출하 같은 창고 물류 작업의 선후관계 표현에 적용한 사례나 확장이 있는가? | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[14. 작업 순서·스케줄링](categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) | 2026-09-25 | 2026-09-25-09 | 열림 | — |
| oq-014 | 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가? | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[12. 명령·작업 실행의 신뢰성](categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | 2026-09-25 | 2026-09-25-09 | 열림 | — |

상태별 건수: 열림 14건

**트랙 전용 질문(트랙 백로그)**

- 매뉴얼 기반 로봇 기능 온톨로지: [질문 백로그](tracks/manual-capability-ontology/question-backlog.md) (열린 질문 39건)
- 자연어 업무 지시 챗봇: [질문 백로그](tracks/nl-task-chatbot/question-backlog.md) (열린 질문 21건)
- 건축 도면 자동 인식: [질문 백로그](tracks/floorplan-recognition/question-backlog.md) (열린 질문 20건)
<!-- auto:open-questions:end -->
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
