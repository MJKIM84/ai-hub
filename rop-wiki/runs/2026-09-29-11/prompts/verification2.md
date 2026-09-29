(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-11
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 61. 물류창고 (Q. 현장 유형별 적용)
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

### runs/2026-09-29-11/target.json

```json
{
  "run_id": "2026-09-29-11",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 103,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 61,
    "area_name": "61. 물류창고",
    "category": "Q. 현장 유형별 적용",
    "category_letter": "Q"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=61"
}
```

### runs/2026-09-29-11/research.json

```json
{
  "run_id": "2026-09-29-11",
  "date": "2026-09-29",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 61,
    "area_name": "61. 물류창고",
    "category": "Q. 현장 유형별 적용"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 상품-대-사람(GTP)·셔틀 기반 저장·회수 시스템·AMR 협업 피킹·스마트물류센터 인증 용어 없음(로봇 이동형 풀필먼트 시스템·주문 배치·풋월·웨이브리스 출고 지시·창고 실행·창고 제어·창고 관리 시스템은 용어집에 이미 있음)",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 입고(하역)·적치·보충·피킹·포장·출하·반품 단계별 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 로봇 이동형 풀필먼트·셔틀·AMR 협업 피킹·트레일러 하역·소팅 로봇, 다중 에이전트 픽업·배송(MAPD)·지속형 MAPF 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 국토교통부 스마트물류센터 인증 심사기준, GS1 EPCIS, Open-RMF, RAWSim-O 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음 — 로봇화 창고 서베이, 전자상거래 창고 서베이, AMR 계획·제어 서베이, 국내 논문 없음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 17. 작업 대상·자산 식별과 인계 추적, 22. 설비·건물 시스템 연동, 23. 업무 시스템 연동, 25. 작업 배정 — MRTA, 27. 다중 로봇 경로·교통 관리 — MAPF, 32. 예외 복구·재계획·업무 연속성, 35. 처리능력·규모·배치 설계, 49. 사람 근접 안전 연결 필요",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 oq-134·oq-138·oq-142·oq-146 미반영, 정정 요청 없음",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? [분류원문]",
    "입고(하역·검수)·적치·보관·보충·피킹·포장·출하·반품 각 단계에 어떤 로봇 시스템(트레일러 하역 로봇, 로봇 이동형 풀필먼트 시스템, 셔틀, AMR 협업 피킹, 소팅 로봇, 무인지게차)이 들어가며, 학술 서베이는 이를 어떻게 분류하는가? (섹션 4·6·8 겨냥)",
    "단계별 로봇 작업의 시작 조건·작업 대상·수행 자원·제약·완료·인계·예외·성과는 실제 도입 사례(국내 쿠팡·CJ대한통운, 해외 DHL·Amazon)에서 어떻게 나타나는가? (섹션 5 겨냥, 현장 유형 물류창고 명시, 한국 자료 우선)",
    "물류창고 로봇 운영의 계획·제어 문제(온라인 픽업·배송 작업 배정, 대규모 경로 계획, 보충 최적화, 반품 재적치 통합)는 어떤 연구가 다루며 오픈소스 시뮬레이터가 있는가? (섹션 6·7·8 겨냥)",
    "국내 규제·인증(국토교통부 스마트물류센터 인증 심사기준)은 물류처리 과정별 자동화와 정보시스템(WMS·WCS)을 어떻게 평가하며, 이것이 ROP 의 위치를 어떻게 규정하는가? (섹션 7·9 겨냥)",
    "물류창고에서 ROP 가 직접 맡을 것(흐름 단계별 작업 요청의 수신·배정·인계 확인·결과 반환)과 WMS·소터·컨베이어 PLC·로봇 파지 인식에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)",
    "oq-134·oq-138·oq-142·oq-146: 국내 물류창고에서 운영 기록의 시뮬레이션 재현, 대화로 시나리오 구성·업무 지시, 소음 조건 음성 지시 인식률을 보고한 자료가 있는가? (섹션 11 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Azadeh·de Koster·Roy(Transportation Science 53(4), 2019)의 서베이는 배송센터에 로봇 취급 시스템이 늘어나는 이유로 작은 공간·수요 변동 대응 유연성·24시간 가동을 들고, 셔틀 기반 저장·회수 시스템, 셔틀 기반 압축 저장 시스템, 로봇 이동형 풀필먼트 시스템(RMFS)을 새 범주로 검토하며 문헌을 시스템 분석·설계 최적화·운영 계획·제어의 세 갈래로 나누고, 통합 로봇 창고에서는 레이아웃·저장 슬로팅·주문 배치·피커 경로·피커–주문 배정 같은 설계·계획·제어 논리를 다시 세워야 한다고 결론짓는다.",
      "tag": "사실",
      "source_ids": [
        "ref-910"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록(Semantic Scholar 경유): \"Integrated robotic warehouse systems will form the next category of warehouses.\" 문헌 분류는 system analysis, design optimization, operations planning and control 의 세 그룹. 실제 사용에 비해 학술 연구가 적은 로봇 시스템이 많다고 지적.",
      "as_of": "2019-06-28",
      "site_type": "물류창고",
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "Boysen·Weidinger·de Koster(European Journal of Operational Research 277(2), 2019)의 전자상거래 창고 서베이는 소량·소수 라인의 시간 민감 피킹 주문이 대량으로 발생하는 조건에서 전통적 피커-대-상품 창고가 부족해 자동 피킹 워크스테이션·로봇·AGV 지원 피킹 같은 자동화 시스템과 혼합 선반 저장·동적 주문 처리·배치·존 분할·분류 시스템 같은 조직적 적응이 채택된다고 정리해, 물류창고 로봇 작업의 시작 조건이 전자상거래 주문 특성임을 보인다.",
      "tag": "사실",
      "source_ids": [
        "ref-382"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 자동화 시스템으로 \"automated picking workstations, robots, and AGV-assisted order picking systems\", 조직적 적응으로 mixed-shelves storage, dynamic order processing, batching, zoning, sorting 을 든다(온라인 게재 2018-08-23, 권호 277(2) 396–411).",
      "as_of": "2019",
      "site_type": "물류창고",
      "flow_item": "시작 조건"
    },
    {
      "id": "f3",
      "claim": "Fragapane·de Koster·Sgarbossa·Strandhagen(European Journal of Operational Research 294(2), 2021)의 문헌 검토는 자율이동로봇(AMR)이 중앙 장치가 스케줄링·라우팅·배차를 모두 맡는 AGV 시스템과 달리 다른 자원과 독립적으로 통신·협상해 의사결정을 분산할 수 있다고 보고, 제조·창고·크로스독·터미널·병원을 적용 분야로 들며 관리자를 위한 AMR 계획·제어 프레임워크와 연구 의제를 제시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-911"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "RePub 초록: \"AMRs can communicate and negotiate independently with other resources\" 로 의사결정을 분산하며, 적용 분야로 manufacturing, warehousing, cross-docks, terminals, hospitals 를 열거. 계획·제어 결정으로 scheduling, routing, dispatching.",
      "as_of": "2021",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f4",
      "claim": "Ma·Li·Kumar·Koenig(AAMAS 2017)의 다중 에이전트 픽업·배송(MAPD) 문제는 자동화 창고에서 에이전트가 온라인으로 도착하는 배송 작업 스트림을 픽업 위치와 배송 위치로 충돌 없이 이동하며 계속 처리하는 지속형 경로 계획 문제이며, 토큰 전달(TP)과 작업 교환 토큰 전달(TPTS) 알고리즘으로 수백 대의 에이전트·작업을 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-006"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록: 에이전트가 \"attend to a stream of delivery tasks in an online setting\" 하는 자동화 창고를 가정하고 TP·TPTS 두 알고리즘을 제시(시뮬레이션 기반).",
      "as_of": "2017-05-30",
      "site_type": "물류창고",
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "Li·Tinka·Kiesel·Durham·Kumar·Koenig(AAAI 2021)의 롤링 호라이즌 충돌 해결(RHCR)은 지속형 다중 에이전트 경로 찾기를 시간창 단위의 순차 문제로 나눠 시뮬레이션 창고에서 최대 1,000대(지도 빈 칸의 38.9%)의 에이전트에 대해 높은 품질의 해를 내어, 대규모 물류창고 로봇 교통 관리의 규모 기준을 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-005"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록: \"can produce high-quality solutions for up to 1,000 agents (= 38.9% of the empty cells on the map)\" — 시뮬레이션 창고 지도 기준.",
      "as_of": "2021-03-12",
      "site_type": "물류창고",
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "RAWSim-O 는 로봇 이동형 풀필먼트 시스템(RMFS)의 의사결정 문제를 연구하기 위한 이산 사건 시뮬레이션 프레임워크로 GNU GPL v3 이상으로 공개돼 있으며, 2D·3D 시각화, 다층 창고 시뮬레이션, 경로 계획 시각화, 로봇 이동 히트맵 기능을 갖추고 새 의사결정 방법을 컨트롤러로 확장할 수 있게 하며, 대표 논문은 Logistics Research 11(1)(2018)이다.",
      "tag": "사실",
      "source_ids": [
        "ref-101"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "GitHub 공식 저장소 README(raw): discrete event-based simulation framework for RMFS, GPL v3 or later, 2D/3D visualization, multi-level warehouse, path planning visualization, heat mapping; 인용 논문 Merschformann·Xie·Li, Logistics Research 11(1), 2018. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": "물류창고",
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "Schrotenboer·Wruck·Vis·Roodbergen(arXiv, 2019)은 전자상거래 창고에서 반품 상품의 재적치를 일반 주문 피커의 경로에 통합하면 비용이 10~15% 절감되고, 고객 주문을 여러 배치로 분해하는 것까지 허용하면 절감이 44%에 이른다고 보고해, 반품 단계가 피킹 단계와 함께 최적화될 수 있음을 보였다(피커 기반 창고의 최적화 연구이며 로봇 피킹 적용은 아니다).",
      "tag": "사실",
      "source_ids": [
        "ref-913"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록: \"integrating the restocking of returned products into regular order picker routes results in cost-savings of 10 to 15%\", 주문 분해까지 허용하면 44%.",
      "as_of": "2019-09-01",
      "site_type": "물류창고",
      "flow_item": "예외·성과"
    },
    {
      "id": "f8",
      "claim": "곽경민·박범·고은지·윤철주·김경훈(CJ대한통운, 로봇학회 논문지 17(4), 2022)은 물류 현장의 로봇 적용을 계약물류·소포·풀필먼트의 차이에 따라 논의하며 적용 유형으로 로봇 낱개 피킹(piece picking), 로봇 박스 취급(디팔레타이징), AGV·AMR 이송, 자동창고(ASRS), 로봇 웨어러블 장치를 들어, 국내 물류창고의 흐름 단계별 로봇 작업 유형을 정리한 국내 문헌이다.",
      "tag": "사실",
      "source_ids": [
        "ref-915"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KCI 초록: 물류산업이 여러 공정에서 인력에 의존하나 로봇 기술 발전과 저가 솔루션으로 적용이 빠르게 늘고 있으며 \"계약물류, 소포, 풀필먼트의 차이점을 다루고\" 로봇 특성과 이슈를 논의(저자 전원 CJ대한통운 소속).",
      "as_of": "2022",
      "site_type": "물류창고",
      "flow_item": "수행 자원"
    },
    {
      "id": "f9",
      "claim": "김태현·송상화(인천대학교, 한국디지털산업학회지 26(1), 2021)는 온라인 주문 풀필먼트 센터의 오더피킹 설비에서 재고 보충을 최적화하는 혼합정수계획 모형을 개발해 실제 운영 프로세스·데이터와 시뮬레이션으로 효과를 검증했으며, 이는 물류창고 보충 단계를 다룬 국내 연구다.",
      "tag": "사실",
      "source_ids": [
        "ref-916"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KCI 초록: \"오더피킹 시스템에서의 재고 보충 최적화\" 를 주제로 \"혼합정수계획 모형을 개발·구현하고 실제 운영 프로세스와 데이터를 활용\" 해 시뮬레이션으로 검증(pp. 67–78).",
      "as_of": "2021",
      "site_type": "물류창고",
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "로봇신문(2022-05-06)이 전한 CJ대한통운의 설명에 따르면 자사 물류 자동화 기술 3종 가운데 QPS 는 피킹·이송·분류 컨베이어를 분리해 시간당 최대 2,000건을 처리하며 기존 DPS 대비 생산성 48% 증가, 지능형 스캐너(ITS)는 시간당 약 7,000건 인식으로 검수 시간 35% 이상 단축, AMR 은 12시간 배터리·50kg 적재·최대 7.2km/h 로 AMR 기반 오더피킹에서 작업자 1명이 시간당 120 오더라인을 처리한다.",
      "tag": "추정",
      "source_ids": [
        "ref-917"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 기사 속 회사 설명. \"작업자 1명이 시간당 120 오더라인을 처리할 수 있다\"; QPS 시간당 최대 2,000건·48% 증가, ITS 시간당 약 7,000건·검수 35% 단축, AMR 12시간·50kg·7.2km/h. 사이트 미명시.",
      "as_of": "2022-05-06",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f11",
      "claim": "로봇신문(2023-02-07)에 따르면 쿠팡 대구 풀필먼트센터는 바닥 QR 코드를 따라 최대 1,000kg 의 선반을 작업자에게 2분 안에 가져오는 AGV 1,000대 이상, 포장 라벨 바코드를 읽어 목적지별로 분류·이송하는 소팅봇 수백 대, 버튼 한 번으로 대용량 제품을 옮기며 사람 출입을 막은 구역에서만 움직이는 무인지게차 수십 대를 갖추고 사람-대-상품(PTG)에서 상품-대-사람(GTP) 방식으로 전환했으며 투자액은 3,200억 원 이상이다.",
      "tag": "사실",
      "source_ids": [
        "ref-919"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기사(현장 공개 취재): AGV 1,000대 이상, 선반 최대 1,000kg, 2분 이내 전달, 소팅봇 수백 대(바코드 스캔·목적지 분류), 무인지게차 수십 대(구역 출입 제한), PTG→GTP, 3,200억 원 이상 투자, 전국 확산의 테스트베드.",
      "as_of": "2023-02-07",
      "site_type": "물류창고",
      "flow_item": "수행 자원"
    },
    {
      "id": "f12",
      "claim": "서로 다른 두 전문지(로봇신문, 물류신문)가 2023-02-07 쿠팡 대구 풀필먼트센터 현장 공개를 각각 보도하며 7층의 AGV 1,000대 이상(최대 1,000kg 선반 운반), 1층의 소팅봇 수백 대(8kg 이하 상품 분류), 5층의 무인지게차(작업자 구역과 분리, 경계 침범 시 안전 센서로 정지)를 같은 내용으로 전해, 국내 물류창고에서 적치·피킹(AGV 선반 운반), 출하 분류(소팅봇), 대용량 운반(무인지게차)에 서로 다른 로봇이 층별로 나뉘어 투입된 사례가 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-919",
        "ref-920"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "물류신문: 연면적 33만㎡·12개 층, 7층 AGV 1,000대 이상·최대 1,000kg 선반, 1층 소팅봇(8kg 이하), 5층 무인지게차 구역 분리와 안전 센서 정지. 로봇신문 보도와 항목·수치 일치. 두 보도 모두 같은 현장 공개 행사에 기반해 회사 제공 정보를 공유한다.",
      "as_of": "2023-02-07",
      "site_type": "물류창고",
      "flow_item": "제약"
    },
    {
      "id": "f13",
      "claim": "쿠팡은 대구 풀필먼트센터의 AGV 가 연중 24시간 가동되고 필요 시 자동 충전하며 이를 통해 전체 업무 단계를 65% 줄였다고 설명했다.",
      "tag": "추정",
      "source_ids": [
        "ref-919",
        "ref-920"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 두 기사 모두 회사 설명으로 \"전체 업무 단계를 65% 줄일 수 있었다\" 를 전하며 산정 방법은 밝히지 않는다.",
      "as_of": "2023-02-07",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f14",
      "claim": "Robotics 24/7(2023-02-01)에 따르면 DHL Supply Chain 은 Boston Dynamics 의 Stretch 로봇을 트레일러·컨테이너 하역에 상업 배치한 첫 회사로, 로봇이 트레일러 뒤쪽에서 상자를 집어 유연 컨베이어에 올리며 DHL 은 1년 전 Boston Dynamics 로봇에 1,500만 달러를 투자했고 이후 여러 창고로 확대하고 하역 외 작업으로 넓힐 계획이라고 보도됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-924"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기사(DHL 발표 기반): first commercial deployment of Stretch for trailer and container unloading, cartons onto a flexible conveyor, $15 million investment one year prior, 향후 여러 창고로 확대. DHL 원 보도자료 페이지는 세 차례 시도 모두 연결 끊김.",
      "as_of": "2023-02-01",
      "site_type": "물류창고",
      "flow_item": "수행 자원"
    },
    {
      "id": "f15",
      "claim": "DHL 과 Boston Dynamics 는 Stretch 의 하역 속도가 시험한 모든 환경에서 수작업을 넘어섰다고 밝히고, 향후 개선 목표로 사람 개입 감소와 떨어진 상자의 자동 복구 개선을 들었다.",
      "tag": "추정",
      "source_ids": [
        "ref-924"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 기사가 전한 회사 설명. unload speeds \"exceeded the manual approach\" 라는 주장과 함께 reducing human interventions, improving automated recovery for fallen boxes 를 목표로 제시(수치 근거 미공개).",
      "as_of": "2023-02-01",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f16",
      "claim": "Amazon 은 2025년 7월 발표에서 100만 번째 로봇을 일본의 풀필먼트센터에 배치해 300개 이상 시설에 로봇 100만 대를 운용하며, 최대 1,250파운드의 재고를 옮기는 Hercules, 정밀 컨베이어로 개별 패키지를 다루는 Pegasus, 직원 주변을 안전하게 주행하며 주문 카트를 옮기는 자율 로봇 Proteus 를 예로 들고, 플릿 이동을 조율하는 생성형 AI 기반 모델 DeepFleet 을 도입했다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-918"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Amazon 자사 뉴스 페이지. \"This milestone robot was recently delivered to a fulfillment center in Japan\"; over 300 facilities; Hercules 1,250 lb, Pegasus, Proteus; DeepFleet 을 지능형 교통 관리 시스템으로 설명. 페이지에 발행일 표기 없음(검색 결과 기준 2025-07).",
      "as_of": "2025-07",
      "site_type": "물류창고",
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f17",
      "claim": "Amazon 은 DeepFleet 이 풀필먼트 네트워크 전체에서 로봇 플릿의 이동 시간을 10% 개선한다고 주장한다.",
      "tag": "추정",
      "source_ids": [
        "ref-918"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 10% improvement in robotic fleet travel time — 자사 발표이며 측정 조건 미공개.",
      "as_of": "2025-07",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f18",
      "claim": "스마트물류시설인증센터(한국교통연구원 운영)의 스마트물류센터 인증 심사기준(일반)은 기능영역 600점을 하차·입고(입고예정정보 확인, 하역작업, 상품검수, 제품정보 인식·등록), 운반·적치(작업정보 제공, 적치장소 이동, 경로관리, 장소식별), 보관·재고관리(재고조사, 보충정보 생성, 위치조정, 모니터링, 품질관리), 피킹·분류(작업정보 생성, 확인방법, 실시간 경로관리, 분류작업), 검품·검수·포장, 상차·출고(발주처별 분류, 차량입차, 상차순서관리, 출고정보전달)의 6개 프로세스 각 100점으로 나누고, 기반영역 400점을 구조적 성능 100점·성과관리 100점·정보시스템 200점(WMS 150점, WCS/MCS 50점)으로 두며 우수물류신기술 적용 가산점은 최대 50점이다.",
      "tag": "사실",
      "source_ids": [
        "ref-921"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "심사기준(일반) 페이지: 기능영역 6개 프로세스 각 100점(계 600점), 기반영역 구조적 성능 100·성과관리 100·정보시스템 200(WMS 150, WCS/MCS 50), 기본 1,000점 + 가산점 최대 50점. 등급 구분 기준은 페이지에 없음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": "물류창고",
      "flow_item": "완료·인계"
    },
    {
      "id": "f19",
      "claim": "국토교통부의 스마트물류센터 인증제는 물류시설의 개발 및 운영에 관한 법률 제21조의4에 근거해 첨단·자동화 설비를 갖춘 물류창고를 1~5등급으로 인증하고, 인증을 받으면 건축·설비 구입 비용을 저리로 융자받고 정부가 최대 2%p 의 이자 비용을 지원하며 용적률·높이 제한 완화 혜택을 받는다(2020-10-08 법 개정, 2021-01-01 시행).",
      "tag": "사실",
      "source_ids": [
        "ref-124",
        "ref-921"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "국토교통부 안내: 물류시설법 제21조의4, 첨단·자동화 시스템 도입 물류시설 인증과 행정·재정 지원, 본인증·예비인증. 인증센터 페이지: 시행령 제12조의5, 2021-01-01 시행, 1~5등급, \"정부가 최대 2%p의 이자비용을 지원\", 시설자금 최대 1,500억 원. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": "물류창고",
      "flow_item": "제약"
    },
    {
      "id": "f20",
      "claim": "CJ대한통운은 2023-10-26 보도자료에서 안성 MP허브터미널(연면적 12,000㎡)이 국토교통부 스마트물류센터 1등급 인증을 받았고 크로스벨트 소터, 컨베이어 센서로 화물을 분산하는 로드 밸런싱, 120개 이상 도크의 차량 배정을 맡는 AI 기반 도크 관리 시스템(DMS)과 오류 자동 복구 기술로 하루 200만 건의 소형 상품을 처리하며 이것이 자사의 9번째 1등급 인증이라고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-923"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 회사 보도자료. 크로스벨트 소터, 로드 밸런싱, DMS(120개 이상 도크), 하루 200만 건, 9번째 1등급 인증, 오류 자동 복구('failover'). 인증 사실 자체는 인증센터 목록으로 대조하지 못함.",
      "as_of": "2023-10-26",
      "site_type": "물류창고",
      "flow_item": "완료·인계",
      "vendor_claim": true
    },
    {
      "id": "f21",
      "claim": "GS1 EPCIS 는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준으로, 물류창고 입고·출하 단계의 완료·인계 기록(무엇이 어디서 누구에게 넘어갔는가)을 로봇 작업 결과와 함께 남기는 데 쓸 수 있는 후보 형식이다.",
      "tag": "사실",
      "source_ids": [
        "ref-003"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "분류 원문 22장 참고 자료 3번(GS1 EPCIS)의 위키 기본 서술을 재사용. 이번 실행에서 원문을 다시 열지 않음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "Interact Analysis(2023-01)는 다중 플릿 오케스트레이션 소프트웨어를 서로 다른 제조사의 AMR 플릿 여럿을 하나의 창고 시스템 안에서 관리하는 소프트웨어로 정의하고, 로봇을 직접 통합하는 저수준 제어와 제조사 플릿 매니저를 관리하는 고수준 제어로 접근을 나누며 상호운용은 표준 또는 미들웨어로 푼다고 정리해, 물류창고를 이 소프트웨어 범주의 기본 현장으로 놓는다.",
      "tag": "사실",
      "source_ids": [
        "ref-257"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "다중 플릿 오케스트레이션 소프트웨어를 고정 자동화의 창고 제어 시스템에 비견하고 저수준·고수준 제어 접근과 표준·미들웨어 기반 상호운용을 구분. (재인용: 2026-09-29-10)",
      "as_of": "2023-01",
      "site_type": "물류창고",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "Open-RMF 는 플릿 어댑터로 서로 다른 제조사의 로봇 플릿을 붙이고 작업·교통 조율과 문·승강기 같은 설비 연동을 제공하는 오픈소스 미들웨어로, 물류창고의 AGV·AMR·소팅 로봇처럼 제조사가 다른 플릿을 하나의 오케스트레이션 계층으로 묶는 참고 구조가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "RMF Core 개요의 작업·교통 조율, Fleet Adapter, 설비 연동 구조를 물류창고 다중 플릿에 대입한 추정. 이번 실행에서 원문을 다시 열지 않음. (재인용: 2026-09-29-10)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원",
      "source_unopened": false
    },
    {
      "id": "f24",
      "claim": "확인한 자료를 종합하면 물류창고의 로봇 작업은 흐름 단계마다 다른 형태로 들어간다: 입고 단계는 트레일러 하역 로봇(f14)과 고속 검수 스캐너(f10), 적치·보관·피킹 단계는 선반(pod)을 작업자에게 가져오는 로봇 이동형 풀필먼트 시스템과 셔틀·압축 저장 시스템(f1·f11·f12), 사람과 함께 걷는 AMR 협업 피킹과 로봇 낱개 피킹(f2·f8·f10), 보충 단계는 보충 정보 생성과 보충 최적화(f9·f18), 출하 단계는 소팅봇·크로스벨트 소터·도크 배정(f12·f20), 반품 단계는 재적치를 피킹 경로에 통합하는 최적화(f7)로 나타나며, 무인지게차는 대용량 운반을 사람 출입이 막힌 구역에서 맡는다(f12).",
      "tag": "추정",
      "source_ids": [
        "ref-910",
        "ref-382",
        "ref-913",
        "ref-915",
        "ref-916",
        "ref-917",
        "ref-919",
        "ref-920",
        "ref-921",
        "ref-923",
        "ref-924"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2·f7~f12·f14·f18·f20 을 입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품 흐름에 대입한 종합. 포장 단계의 로봇 사례는 이번 실행에서 확인하지 못함(직전 실행 2026-09-29-10 의 CJ대한통운 양팔 로봇 포장 사례는 그 브리프 참조).",
      "as_of": "2026-09-29",
      "site_type": "물류창고",
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "확인한 자료를 종합하면 물류창고 로봇 작업의 여섯 항목은 시작 조건이 전자상거래 주문(f2)과 입고예정정보(f18), 작업 대상이 선반(pod)·토트·박스·팔레트·반품 상품(f7·f11·f14), 수행 자원이 AGV·AMR·소팅봇·무인지게차·하역 로봇과 상품-대-사람 스테이션의 작업자(f11·f12·f14), 제약이 적재 한계(선반 1,000kg, 소팅봇 8kg 이하, AMR 50kg)·배터리·사람 출입이 막힌 무인지게차 구역(f10·f12·f13), 완료·인계가 바코드 인식·검수·출고정보 전달과 인계 이벤트 기록(f18·f21), 예외·성과가 떨어진 상자 복구와 처리량·오더라인 지표(f10·f15·f17)로 채워질 수 있으나, 각 사례의 수치는 회사 설명이라 성과 항목은 벤더 주장으로 남는다.",
      "tag": "추정",
      "source_ids": [
        "ref-382",
        "ref-913",
        "ref-917",
        "ref-919",
        "ref-920",
        "ref-921",
        "ref-924",
        "ref-003",
        "ref-918"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 21장의 여섯 항목에 f2·f7·f10~f18·f21 을 대입한 종합. 수치는 f10·f13·f15·f17 의 벤더 주장에 기댐.",
      "as_of": "2026-09-29",
      "site_type": "물류창고",
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "확인한 자료를 종합하면 61. 물류창고에서 ROP 가 직접 맡을 범위는 인증 심사기준의 정보시스템 계층(WMS 와 WCS/MCS, f18) 사이에서 흐름 단계별 작업 요청(입고예정·주문·보충·출고 정보)을 받아 제조사가 다른 AGV·AMR·소팅봇·무인지게차·하역 로봇에 배정하고(f4·f22·f23) 경로·교통을 조율하며(f5) 바코드 인식·인계 이벤트로 완료를 확인해 결과를 WMS 로 돌려주는 일이며, 다중 플릿 오케스트레이션 소프트웨어가 창고 제어 시스템에 비견된다는 시장 정의(f22)와 맞는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-921",
        "ref-257",
        "ref-004",
        "ref-006",
        "ref-005",
        "ref-003"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f18 의 WMS/WCS·MCS 구분, f22 의 다중 플릿 오케스트레이션 정의, f4·f5 의 온라인 작업 배정·경로 계획, f21 의 인계 이벤트를 분류 원문 19장의 직접 범위에 대입한 종합.",
      "as_of": "2026-09-29",
      "site_type": "물류창고",
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "연계 대상: 물류창고에서 주문·재고·보충 규칙을 정하는 WMS 는 분류 원문 19장의 상위 업무 시스템, 크로스벨트 소터·컨베이어·로드 밸런싱과 도크 배정은 시설·설비 제어, 하역 로봇의 상자 인식·파지와 로봇 낱개 피킹의 비전·파지는 로봇 자체 지능·제어에 속하므로, 이종 제조사를 잇는 ROP 는 이들에 작업 요청·예약·인계·상태 확인만 걸고 재고 판단·설비 제어·파지 성능은 WMS·설비 업체·로봇 제조사에 맡겨야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-921",
        "ref-923",
        "ref-924",
        "ref-915"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f18(WMS·WCS/MCS 계층), f20(소터·로드 밸런싱·DMS), f14·f15(하역 로봇의 상자 인식·복구), f8(로봇 낱개 피킹)을 분류 원문 19장의 외부 연계 영역에 대입한 종합.",
      "as_of": "2026-09-29",
      "site_type": "물류창고",
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "이 영역은 작업 대상의 식별·인계 기록을 다루는 17. 작업 대상·자산 식별과 인계 추적(f21), 소터·컨베이어·도크 연동을 다루는 22. 설비·건물 시스템 연동(f20), WMS·WCS 연동을 다루는 23. 업무 시스템 연동(f18), 온라인 픽업·배송 작업 배정과 대규모 경로 계획을 다루는 25. 작업 배정 — MRTA·27. 다중 로봇 경로·교통 관리 — MAPF(f4·f5), 로봇 밀도·처리능력 설계를 다루는 35. 처리능력·규모·배치 설계(f1·f6), 무인지게차 구역 분리와 사람 협업 피킹을 다루는 49. 사람 근접 안전·31. 사람–로봇 협업(f12·f2), 떨어진 상자 복구 같은 예외를 다루는 32. 예외 복구·재계획·업무 연속성(f15), 시장 동향을 다루는 1. 기술·시장·업체 동향(f16·f22)에 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-003",
        "ref-923",
        "ref-921",
        "ref-006",
        "ref-005",
        "ref-910",
        "ref-101",
        "ref-919",
        "ref-382",
        "ref-924",
        "ref-918",
        "ref-257"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2·f4~f6·f12·f15·f16·f18·f20~f22 의 내용을 관련 세부영역에 대응시킨 종합.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-910",
      "org": "Azadeh, K., de Koster, R., & Roy, D. (Transportation Science 53(4))",
      "title": "Robotized and Automated Warehouse Systems: Review and Recent Developments",
      "published": "2019-06-28",
      "url": "https://pubsonline.informs.org/doi/10.1287/trsc.2018.0873",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "셔틀 기반 저장·회수, 셔틀 기반 압축 저장, 로봇 이동형 풀필먼트 시스템을 검토한 로봇화 창고 서베이. 출판사 페이지는 403 이라 Semantic Scholar API 로 서지·초록만 읽었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1287/trsc.2018.0873?fields=title,authors,year,abstract,venue,publicationDate",
      "source_unopened": false
    },
    {
      "id": "ref-911",
      "org": "Fragapane, G., de Koster, R., Sgarbossa, F., & Strandhagen, J. O. (European Journal of Operational Research 294(2))",
      "title": "Planning and control of autonomous mobile robots for intralogistics: Literature review and research agenda",
      "published": "2021",
      "url": "https://doi.org/10.1016/j.ejor.2021.01.019",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "AMR 의 분산 의사결정과 계획·제어(스케줄링·라우팅·배차) 프레임워크, 창고·제조·크로스독·터미널·병원 적용 분야를 정리한 문헌 검토. 에라스무스 대학교 RePub 저장소 페이지에서 초록을 읽었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://repub.eur.nl/pub/134773/",
      "source_unopened": false
    },
    {
      "id": "ref-382",
      "org": "Boysen, N., Weidinger, F., & de Koster, R. (European Journal of Operational Research 277(2))",
      "title": "Warehousing in the e-commerce era: A survey",
      "published": "2019",
      "url": "https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "전자상거래 주문 특성에 맞춘 자동화 시스템(자동 피킹 워크스테이션·로봇·AGV 지원 피킹)과 조직적 적응(혼합 선반 저장·동적 주문 처리·배치·존·분류)을 정리한 서베이(온라인 2018-08-23, 권호 277(2) 396–411).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-913",
      "org": "Schrotenboer, A. H., Wruck, S., Vis, I. F. A., & Roodbergen, K. J.",
      "title": "Integration of returns and decomposition of customer orders in e-commerce warehouses",
      "published": "2019-09-01",
      "url": "https://arxiv.org/abs/1909.01794",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "반품 재적치를 피커 경로에 통합하면 10~15%, 주문 분해까지 허용하면 44% 비용 절감을 보고한 프리프린트.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-101",
      "org": "Merschformann, M. (RAWSim-O GitHub 공식 저장소)",
      "title": "RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README)",
      "published": null,
      "url": "https://github.com/merschformann/RAWSim-O",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "로봇 이동형 풀필먼트 시스템용 이산 사건 시뮬레이션 프레임워크의 공식 README. GPL v3 이상, 2D·3D 시각화·다층 창고·히트맵 기능, 대표 논문 Logistics Research 11(1) 2018.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/merschformann/RAWSim-O/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-915",
      "org": "곽경민, 박범, 고은지, 윤철주, 김경훈 (CJ대한통운, 로봇학회 논문지 17(4))",
      "title": "급속 확산되는 물류현장의 로봇적용 사례",
      "published": "2022",
      "url": "https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002899267",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "계약물류·소포·풀필먼트의 차이에 따른 물류 로봇 적용(로봇 낱개 피킹, 박스 취급, AGV·AMR, ASRS, 웨어러블)을 정리한 국내 논문(pp. 387–396). 저자 전원 CJ대한통운 소속.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-916",
      "org": "김태현, 송상화 (인천대학교, 한국디지털산업학회지 26(1))",
      "title": "온라인 주문 풀필먼트를 위한 물류센터 피킹 설비 최적화에 대한 연구",
      "published": "2021",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002687327",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "오더피킹 설비의 재고 보충을 혼합정수계획 모형으로 최적화하고 실제 운영 데이터와 시뮬레이션으로 검증한 국내 논문(pp. 67–78).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-917",
      "org": "로봇신문 (장길수)",
      "title": "CJ대한통운이 뽑은 물류자동화 혁신 기술 '톱3'",
      "published": "2022-05-06",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=28424",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-29",
      "summary": "CJ대한통운이 밝힌 QPS·지능형 스캐너·AMR 의 기능과 처리량 수치를 전한 기사. 수치는 회사 설명이다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-918",
      "org": "Amazon",
      "title": "Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot",
      "published": "2025-07",
      "url": "https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "로봇 100만 대 배치와 플릿 조율용 생성형 AI 기반 모델 DeepFleet(이동 시간 10% 개선 주장)을 알린 Amazon 자사 발표. 페이지에 발행일 표기가 없어 검색 결과의 2025-07 로 적었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-919",
      "org": "로봇신문 (장길수)",
      "title": "쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이...",
      "published": "2023-02-07",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=30736",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "쿠팡 대구 풀필먼트센터 현장 공개 취재. AGV 1,000대 이상·소팅봇 수백 대·무인지게차 수십 대의 역할, 3,200억 원 투자, PTG→GTP 전환.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-920",
      "org": "물류신문 (석한글)",
      "title": "‘물류 투자만 6조’, 쿠팡 물류 인프라의 정점 ‘대구 FC’ 가보니",
      "published": "2023-02-07",
      "url": "https://www.klnews.co.kr/news/articleView.html?idxno=306994",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "같은 현장 공개를 취재한 물류 전문지 기사. 층별 로봇 배치(7층 AGV, 1층 소팅봇, 5층 무인지게차)와 구역 분리·안전 센서, 33만㎡ 규모.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-921",
      "org": "스마트물류시설인증센터 (한국교통연구원)",
      "title": "인증스마트물류센터 : 인증심사 > 심사기준 > 일반",
      "published": null,
      "url": "https://cslc.koti.re.kr/new_sub2/new_sub2_2_1",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "스마트물류센터 인증 심사기준(일반): 기능영역 6개 프로세스 각 100점, 기반영역 구조·성과·정보시스템(WMS 150·WCS/MCS 50), 가산점 최대 50점.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-124",
      "org": "국토교통부 (국가물류통합정보센터)",
      "title": "스마트물류센터 인증제 안내",
      "published": null,
      "url": "https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "물류시설법 제21조의4에 따른 스마트물류센터 인증제의 목적·대상(본인증·예비인증) 안내. 세부 기준은 첨부 파일에 있어 페이지에서는 읽지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-923",
      "org": "CJ대한통운",
      "title": "CJ대한통운 안성 MP허브, 국토부 ‘스마트물류센터 1등급’ 인증",
      "published": "2023-10-26",
      "url": "https://cjlogistics.com/ko/newsroom/news/NR_00001109",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "안성 MP허브터미널의 스마트물류센터 1등급 인증과 크로스벨트 소터·로드 밸런싱·도크 관리 시스템·하루 200만 건 처리를 알린 회사 보도자료.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-924",
      "org": "Robotics 24/7 (Eugene Demaitre)",
      "title": "DHL Makes First Commercial Deployment of Boston Dynamics Stretch Robot to Unload Trailers and Containers",
      "published": "2023-02-01",
      "url": "https://www.robotics247.com/article/dhl_makes_first_commercial_deployment_boston_dynamics_stretch_robot_unload_trailers_containers",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "DHL Supply Chain 의 Stretch 트레일러·컨테이너 하역 로봇 첫 상업 배치, 1,500만 달러 투자, 향후 확대 계획을 전한 전문지 기사. DHL 원 보도자료는 연결 끊김으로 열지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-003",
      "org": "GS1",
      "title": "EPCIS and CBV Linked Data Model",
      "published": null,
      "url": "https://ref.gs1.org/epcis/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 GS1 표준(분류 원문 22장 3번, 재사용). 이번 실행에서 다시 열지 않았다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고(분류 원문 22장 4번, 재사용). 이번 실행에서 다시 열지 않았다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-005",
      "org": "Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. (AAAI 2021)",
      "title": "Lifelong Multi-Agent Path Finding in Large-Scale Warehouses",
      "published": "2021-03-12",
      "url": "https://arxiv.org/abs/2005.07371",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "롤링 호라이즌 충돌 해결(RHCR)로 시뮬레이션 창고에서 최대 1,000대 에이전트의 지속형 경로 찾기를 푼 논문(분류 원문 22장 5번, 재사용). arXiv 초록을 열어 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-006",
      "org": "Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. (AAMAS 2017)",
      "title": "Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks",
      "published": "2017-05-30",
      "url": "https://arxiv.org/abs/1705.10868",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자동화 창고의 온라인 픽업·배송 작업 스트림을 다루는 MAPD 문제와 TP·TPTS 알고리즘(분류 원문 22장 6번, 재사용). arXiv 초록을 열어 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-257",
      "org": "Interact Analysis (Rueben Scriven)",
      "title": "AMR Multi-Fleet Orchestration Software Explained",
      "published": "2023-01",
      "url": "https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 다중 플릿 오케스트레이션 소프트웨어의 정의와 저수준·고수준 제어 접근, 표준·미들웨어 기반 상호운용(2026-09-29-10 재사용). 이번 실행에서 다시 열지 않았다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/site-type-applications/warehouse.md",
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
      "rationale": "섹션 3: f1(로봇 취급 시스템이 늘고 설계·계획·제어 논리를 다시 세워야 함), f2(전자상거래 주문 특성이 시작 조건), f22(다중 플릿 오케스트레이션의 기본 현장이 창고) / 섹션 4: f2·f11(상품-대-사람·AMR 협업 피킹), f1(셔틀 기반 저장·회수·RMFS), f4(MAPD), f19(스마트물류센터 인증) / 섹션 5(현장 유형 모두 물류창고): 입고 — f14·f15(DHL 트레일러 하역, 성과는 벤더 주장), 적치·피킹·출하 — f11·f12·f13(쿠팡 대구: 층별 AGV·소팅봇·무인지게차, 65% 는 벤더 주장), 피킹·검수 — f10(CJ대한통운 QPS·ITS·AMR, 벤더 주장), 출하·도크 — f20(CJ대한통운 안성, 벤더 주장), 반품 — f7(반품 재적치 통합 연구, 로봇 적용 아님을 명시), 전체 — f16·f17(Amazon, 벤더 주장), 여섯 항목 정리는 f25 / 섹션 6: 흐름 단계별 로봇 작업 지도 f24, 계획·제어 f3·f4·f5·f9, 반품 f7, 국내 유형 분류 f8 / 섹션 7: f18·f19(국토교통부 스마트물류센터 인증 심사기준·법적 근거), f21(GS1 EPCIS, ref-003 재사용), f23(Open-RMF, ref-004 재사용), f6(RAWSim-O) / 섹션 8: f1·f2·f3(서베이 3편), f4·f5(MAPD·지속형 MAPF), f7(반품), f6(시뮬레이터), 국내 f8·f9 / 섹션 9: f26(직접 범위: WMS 와 WCS/MCS 사이에서 단계별 작업 요청 수신·이기종 플릿 배정·경로 조율·인계 확인·결과 반환), f27(연계 대상: WMS 재고·주문 판단, 소터·컨베이어·도크 설비 제어, 하역·피킹 로봇의 인식·파지) / 섹션 10: f28 — 1. 기술·시장·업체 동향, 17. 작업 대상·자산 식별과 인계 추적, 22. 설비·건물 시스템 연동, 23. 업무 시스템 연동, 25. 작업 배정 — MRTA, 27. 다중 로봇 경로·교통 관리 — MAPF, 31. 사람–로봇 협업, 32. 예외 복구·재계획·업무 연속성, 35. 처리능력·규모·배치 설계, 49. 사람 근접 안전 / 섹션 11: 기존 oq-134·oq-138·oq-142·oq-146(이번 조사에서도 국내 물류창고 자료 미확인, 미해결)과 open_questions_new 4건. f10·f13·f15·f16·f17·f20 은 벤더 주장 병기 필수. 다음 실행 후보: 23. 업무 시스템 연동 페이지에 f18(WMS·WCS/MCS 배점) 반영, 25. 작업 배정 — MRTA·27. 다중 로봇 경로·교통 관리 — MAPF 페이지에 f4·f5 반영, 35. 처리능력·규모·배치 설계 페이지에 f6 반영, 49. 사람 근접 안전 페이지에 f12(무인지게차 구역 분리) 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "상품-대-사람",
      "term_en": "Goods-to-Person (GTP)",
      "definition": "로봇이나 설비가 선반·토트를 작업자 스테이션으로 가져와 작업자는 제자리에서 피킹하는 방식으로, 작업자가 선반까지 걸어가는 사람-대-상품(Person-to-Goods, PTG) 방식과 대비되며 로봇 이동형 풀필먼트 시스템이 대표 구현이다."
    },
    {
      "term_ko": "셔틀 기반 저장·회수 시스템",
      "term_en": "Shuttle-Based Storage and Retrieval System (SBS/RS)",
      "definition": "층마다 움직이는 셔틀 차량과 리프트로 토트·상자를 랙에 넣고 꺼내는 자동 창고 시스템으로, 로봇화 창고 서베이가 로봇 이동형 풀필먼트 시스템·셔틀 기반 압축 저장 시스템과 함께 새 범주로 검토한다."
    },
    {
      "term_ko": "AMR 협업 피킹",
      "term_en": "AMR-assisted Order Picking",
      "definition": "자율이동로봇이 피킹 경로를 따라 작업자와 함께 움직이며 상품을 싣고 나르고 작업자는 집는 일만 맡는 방식으로, 기존 피커-대-상품 창고에 큰 개조 없이 도입할 수 있어 전자상거래 창고 서베이가 자동화 선택지의 하나로 든다."
    },
    {
      "term_ko": "스마트물류센터 인증",
      "term_en": "Smart Logistics Center Certification",
      "definition": "물류시설의 개발 및 운영에 관한 법률 제21조의4에 따라 국토교통부가 첨단·자동화 설비를 갖춘 물류창고를 1~5등급으로 인증하는 제도로, 하차·입고부터 상차·출고까지 6개 프로세스의 기능영역과 구조·성과·정보시스템의 기반영역을 심사한다."
    }
  ],
  "open_questions_new": [
    "국내 물류센터에서 서로 다른 제조사의 AGV·소팅봇·무인지게차·하역 로봇을 하나의 오케스트레이션 계층으로 관제한 공개 사례가 있는가(쿠팡 대구·CJ대한통운 사례는 설비별 도입만 확인됐다)? | 관련 영역: 61. 물류창고, 20. 로봇·제조사 관제 연동 | 근거: f12 | 종류: 일반",
    "스마트물류센터 인증 심사기준의 정보시스템 항목(WMS 150점, WCS/MCS 50점)에서 이기종 로봇 오케스트레이션 계층은 어느 항목으로 평가되며 인증 심사가 로봇 플릿 관제 기능을 따로 보는가? | 관련 영역: 61. 물류창고, 23. 업무 시스템 연동 | 근거: f18 | 종류: 일반",
    "반품 재적치를 피킹 경로에 통합하는 최적화 연구를 로봇 이동형 풀필먼트 시스템이나 AMR 협업 피킹에 적용한 연구·사례가 있는가? | 관련 영역: 61. 물류창고, 25. 작업 배정 — MRTA | 근거: f7 | 종류: 일반",
    "트레일러 하역 로봇의 떨어진 상자 복구 같은 예외 처리가 로봇 자체 복구와 오케스트레이션 계층의 재계획 사이에서 어떻게 분담되는지 공개된 인터페이스나 사례가 있는가? | 관련 영역: 61. 물류창고, 32. 예외 복구·재계획·업무 연속성 | 근거: f15 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 20,
    "cross_checked_count": 2,
    "unverified": [
      "f12 외 사례 finding 교차 확인 실패(CJ대한통운·DHL·Amazon 사례는 발행 주체 한 곳)",
      "f12 의 두 기사는 같은 현장 공개 행사에 기반해 회사 제공 정보를 공유하므로 독립성이 제한적임",
      "f1 Azadeh 외 서베이는 출판사 페이지 403 으로 Semantic Scholar API 의 초록만 확인",
      "f3 Fragapane 외 서베이는 RePub 저장소의 초록만 확인(권호·쪽수는 검색 결과 기준 294(2) 405–426)",
      "f14·f15 DHL 원 보도자료(dhl.com 2023-02, group.dhl.com 2025-05·2025-07)는 세 차례 모두 연결 끊김으로 열지 못해 전문지 기사로 대신함",
      "f16·f17 Amazon 페이지의 발행일은 페이지에 없어 검색 결과(2025-07)로 적음",
      "f18 인증 심사기준의 등급 구분 점수 기준은 페이지에 없어 미확인",
      "f20 CJ대한통운 안성 1등급 인증 사실을 인증센터 목록으로 대조하지 못함",
      "쿠팡 뉴스룸 보도자료(news.coupang.com)는 403 으로 열지 못함",
      "국토교통부 인증제 안내의 세부 기준 첨부 파일 미열람",
      "특허청·한국로봇산업협회 '물류로봇 특집편' PDF 와 로봇학회 논문지 PDF(jkros.org)는 텍스트 추출 실패로 출처 제외",
      "포장 단계의 로봇 사례는 이번 실행에서 확인하지 못함(직전 실행 2026-09-29-10 의 CJ대한통운 양팔 로봇 사례는 이번 출처 상한으로 재인용하지 않음)",
      "oq-134 미해결: 국내 물류창고 운영 기록의 시뮬레이션 재현 사례 미확인",
      "oq-138 미해결: 국내 물류창고의 대화형 시나리오 구성 사례 미확인",
      "oq-142 미해결: 국내 물류창고의 대화형 업무 지시·승인 사례 미확인",
      "oq-146 미해결: 물류창고 소음 조건 음성 지시 인식률 자료 미확인(예산 안에서 별도 검색은 하지 못함)",
      "ref-005·ref-006·ref-003·ref-004·ref-257 재사용 항목은 참고문헌 목록 입력이 0건이라 등록된 기관·제목·URL 과 글자 단위로 대조하지 못함(ref-005·ref-006 은 arXiv URL 로 적음)"
    ],
    "scope_violations": [
      "f27: WMS 의 재고·주문 판단, 소터·컨베이어·도크 설비 제어, 하역·피킹 로봇의 인식·파지는 분류 원문 19장의 상위 업무 시스템·시설·설비 제어·로봇 자체 지능·제어 쪽이므로 '연계 대상: '으로 표시함",
      "f7·f9: 피커 경로·보충 최적화는 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링·28. 공용 자원·충전·에너지 최적화 의 방법 영역과 겹치므로 이 영역에서는 반품·보충 단계의 연구 근거로만 제안함",
      "f4·f5: MAPD·지속형 MAPF 는 27. 다중 로봇 경로·교통 관리 — MAPF 의 핵심이므로 이 영역에서는 물류창고 규모 기준과 연결 근거로만 제안함",
      "f16·f17: Amazon DeepFleet 은 L. AI·학습 기술의 방법(46. 예측·학습 기반 최적화)과 겹치므로 벤더 주장으로만 제안함",
      "f18·f19: 스마트물류센터 인증은 59. 법·규제·보험·라이선스·23. 업무 시스템 연동과 겹치므로 이 영역에서는 흐름 단계 정의와 정보시스템 계층의 근거로만 제안함"
    ],
    "budget_used": {
      "queries": 15,
      "sources": 15
    },
    "limits": "재실행 1회차. 반려 사유 1(f11: 벤더 문서만 근거로 한 사실 태그에 vendor_claim 없음): 직전 반환값(runs/2026-09-29-11/research.json)이 입력에 포함되지 않아 형식만 고칠 수 없었으므로 예산 안에서 브리프를 다시 작성했고, 벤더 문서(Amazon ref-918, CJ대한통운 보도자료 ref-923)만 근거로 한 finding 과 기사에 실린 기업 성능 수치는 모두 vendor_claim true·태그 추정·신뢰도 low·evidence_excerpt 첫머리 '벤더 주장: '으로 표시했다(관련 finding: f10, f13, f15, f16, f17, f20). 이번 브리프의 finding 번호는 직전 반환값과 대응하지 않는다. web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-910~ref-924, 예약 구간 ref-910~ref-939 안) 상한 도달로 RAWSim-O 논문 arXiv 초록(1710.04726, 열었으나 README 로 대체), 국토교통부 인증제 상세 첨부, 콜드체인뉴스·물류신문의 인증제 해설, Locus Robotics·Optoro 의 반품 자동화 글(벤더 문서), DHL Group 2025 보도자료 2건(연결 끊김), 쿠팡 뉴스룸 보도자료(403), ISO 3691-4 계열 물류 로봇 안전 규격은 넣지 못했다. 원문 열람 17건(github_raw 1: RAWSim-O README, webfetch 16: Semantic Scholar API 초록 1, RePub·Pure 초록 2, arXiv 초록 3(ref-913·ref-005·ref-006), KCI 초록 2, 인증센터·국토교통부 페이지 2, 기사 4, 벤더 페이지 2), 재사용 미열람 3건(ref-003·ref-004·ref-257 은 이번에 다시 열지 않아 fetched false·source_unopened true; ref-005·ref-006 은 재사용이지만 arXiv 초록을 열어 fetched true). 주의: 같은 날 이전 실행 2026-09-29-10 이 ref-910~ref-913 을 다른 URL(The Robot Report, 아시아경제, 서울신문)에 부여했다고 그 브리프에 적혀 있으므로 퍼블리셔가 URL 기준으로 합칠 때 번호 충돌을 확인해야 하고, 참고문헌 목록 입력이 이 페이지 인용분 0건만 요약되어 학술 서베이·Amazon·인증센터 페이지가 전체 909건과 URL 이 겹칠 수 있다. 교차 확인 2건(f12: 로봇신문/물류신문 — 같은 현장 공개에 기반해 독립성 제한, f19: 국토교통부/한국교통연구원 인증센터). 신뢰도 high 는 f19 한 건(정부·연구기관 원문 2건 열람). 분류 원문 핵심 질문(물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가)에는 단계별 로봇 작업 지도 f24 와 여섯 항목 정리 f25 로 답했으며 결론은 '입고 하역·검수, 적치·피킹의 상품-대-사람 운반, 보충 최적화, 출하 분류·도크 배정, 반품 재적치 통합까지 단계마다 다른 로봇·설비가 들어가고 국내 인증 심사기준이 같은 6단계 구분을 쓰며, 이들을 한 계층에서 묶은 공개 사례는 확인되지 않았고 성과 수치는 회사 설명 수준'이라는 추정이다. 현장 유형: 모두 물류창고(국내 쿠팡 대구·CJ대한통운, 해외 DHL·Amazon, 학술 서베이)이며 이 영역의 성격상 다른 현장 유형 사례는 찾지 않았다(f3 의 병원·제조 등 적용 분야 언급만 있음). 국내 자료는 로봇학회 논문지(f8)·한국디지털산업학회지(f9)·인증 심사기준과 안내(f18·f19)·쿠팡(f11~f13)·CJ대한통운(f10·f20) 여덟 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음(RAWSim-O 는 설계 연구용 시뮬레이터로 35. 처리능력·규모·배치 설계에 연결). 용어집에 이미 있는 로봇 이동형 풀필먼트 시스템·주문 배치·풋월·웨이브리스 출고 지시·창고 실행·창고 제어·창고 관리 시스템·다중 에이전트 픽업·배송·지속형 다중 에이전트 경로 찾기·플릿 관리 시스템은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 4건(oq-134·oq-138·oq-142·oq-146)은 조사 질문에 넣었으나 별도 검색 예산을 배분하지 못해 미해결로 남긴다. 해결된 열린 질문 없음."
  }
}
```

### runs/2026-09-29-11/verification.json

```json
{
  "run_id": "2026-09-29-11",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. Semantic Scholar API 로 서지·초록 일치(Transportation Science, 2019-06-28). 단, 결론의 '레이아웃·저장 슬로팅·주문 배치·피커 경로·피커–주문 배정' 열거는 초록에 없고 'all vital warehouse design, planning, and control logic' 만 있음 — 열거 삭제 지시. 출판사 페이지 미열람(403), 초록만 확인."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. Pure(EUR) 페이지에서 초록 원문 일치(EJOR 277(2) 396–411, 온라인 2018-08-23). 초록 확인, 본문 미열람."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. RePub 페이지 초록에 분산 의사결정·협상, 적용 분야(제조·창고·크로스독·터미널·병원) 일치. 권호 294(2)는 페이지에서 확인되지 않아 브리프 기록대로 둠. 발행 2021."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 1705.10868 초록에 MAPD 온라인 작업 스트림, TP·TPTS, 수백 대 규모 일치(AAMAS 2017). 발행 2017-05-30, 2년 경과 자료."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2005.07371(v2 2021-03-12, AAAI 2021) 초록에 '1,000 agents (= 38.9% of the empty cells)' 일치. '규모 기준을 제공한다'는 해석이므로 시뮬레이션 창고 기준임을 명시하게 함."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. GitHub raw README 에 GPL v3+, 2D·3D 시각화, 다층 창고, 경로 계획 시각화, 히트맵, 컨트롤러 확장, 인용 논문 Logistics Research 11(1) 2018 일치. 발행일 미확인(확인일 기준)."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 1909.01794 초록에 10~15%, 주문 분해 시 최대 44% 일치. 브리프대로 피커 기반 창고 연구임을 본문에 명시."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. KCI 랜딩 페이지에서 저자·소속(CJ대한통운)·권호(17(4), 2022, 387–396)·초록의 계약물류·소포·풀필먼트, AGV·AMR·ASRS·박스/낱개 취급·웨어러블 일치. 초록만 확인."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. KCI 페이지에서 인천대학교, 한국디지털산업학회지 26(1) 2021 67–78, 재고 보충 최적화·혼합정수계획·실제 데이터·시뮬레이션 일치. 초록만 확인."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 로봇신문 2022-05-06 기사에 QPS 2,000건·48%, ITS 시간당 약 7,000개·35% 이상, AMR 12시간·50kg·7.2km/h·120 오더라인 일치. 수치 출처는 CJ대한통운 설명 — 추정·벤더 주장 병기 유지."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 로봇신문 2023-02-07 기사에 AGV 1,000대 이상, 선반 최대 1,000kg, 소팅봇 수백 대, 무인지게차 수십 대, PTG→GTP, 3,200억 원 이상 일치. 물류신문(ref-920)도 같은 항목 보도(검증에서 확인). 단 기사는 '평균 2분'이므로 '2분 안에'를 고치고, 수치가 현장 공개에서 회사가 제공한 것임을 병기. 두 보도의 독립성은 제한적."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 물류신문 원문: '7층에는 총 1,000여 대의 AGV', '1층에 수백 대가 넘는 소팅 봇', 5층 무인지게차 구역 분리와 안전구역 침범 시 정지, 연면적 33만㎡·지하 2층 지상 10층. 로봇신문과 항목 일치. 물류신문의 AGV 표현은 '1,000여 대'로 정확히 옮기게 함. 두 출처 모두 같은 현장 공개 행사 기반이라 독립성 제한 — medium 유지."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 물류신문 원문 '1년 365일, 24시간 작동하며 … 자동으로 충전', '전체 업무 단계를 65% 줄일 수 있었다', 로봇신문도 65% 보도. 두 매체 모두 회사 설명을 전한 것이라 독립 교차 아님 — 추정·벤더 주장 유지."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. Robotics 24/7 2023-02-01(Eugene Demaitre) 기사에 첫 상업 배치, 트레일러 뒤쪽에서 상자를 유연 컨베이어로, 1년 전 1,500만 달러 투자, 여러 창고 확대 계획 일치. DHL 원 보도자료 미열람은 브리프대로."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 같은 기사에 'exceeded the manual approach'(DHL 설명), 사람 개입 감소·떨어진 상자 자동 복구 개선 목표 일치. 수치 미공개 — 추정·벤더 주장 유지."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. Amazon 자사 페이지에 일본 풀필먼트센터의 100만 번째 로봇, 300개 이상 시설, Hercules 1,250파운드, Pegasus, Proteus, DeepFleet 일치. 페이지에 발행일 없음(브리프의 2025-07 은 검색 결과 기준) — 추정·벤더 주장 유지."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 같은 페이지에 'improving the travel time of our robotic fleet by 10%' 일치. 측정 조건 미공개 — 추정·벤더 주장 유지."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 인증센터 심사기준(일반) 페이지에서 기능영역 6개 프로세스 각 100점(세부 항목 포함), 기반영역 구조 100·성과 100·정보시스템 200(WMS 150, WCS/MCS 50), 가산점 최대 50점 일치. 가산점은 2025-04-17 국토교통부 고시 기준이라고 페이지에 적혀 있음. 발행일 미확인(확인일 기준)."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "부분 확인. 국토교통부(nlic) 안내 페이지는 법 제21조의4·본인증·예비인증만 담고, 인용한 ref-921 URL(심사기준 페이지)에는 등급·이자·시행일이 없음. 1~5등급, 최대 2%p 이자 지원(등급·기업 규모별 0.25~2.00%p), 시설자금 한도 500억~1,500억 원, 용적률·높이 완화, 시행령 2020-10-08 개정·2021-01-01 시행은 같은 인증센터 사이트의 인증혜택(new_sub1_4)·법적근거(new_sub1_2) 페이지에서 검증자가 확인. 따라서 사실 유지하되 교차 확인은 법적 근거 부분만이고 수치는 단일 기관 — 신뢰도 high → medium. '2020-10-08 법 개정'은 시행령 개정으로 고쳐야 함."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. CJ대한통운 보도자료 2023-10-26 에 연면적 12,000㎡, 1등급(9번째), 크로스벨트 소터, 로드 밸런싱, DMS, 페일오버, 하루 200만 개 일치. 도크는 '간선차량 120여 대 동시 접안' 표현이므로 '120개 이상 도크' 수정. 인증 사실은 인증센터 목록으로 대조하지 못함 — 추정·벤더 주장 유지."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 검증에서 ref.gs1.org/epcis 를 열어 '상태·위치·이동·관리 이전(chain of custody)' 이벤트 공유 표준임을 확인. 브리프는 미열람(fetched false)으로 표시했으므로 각주 표기는 브리프 기준. 후보 형식이라는 서술은 적용 가능성 제안이며 사실 부분은 표준 정의에 한함."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(페이지 두 차례 빈 응답). 검색 결과에서 기관·제목·URL 일치, 스니펫에 저수준·고수준 제어 두 접근과 창고 제어 소프트웨어 발전을 따라왔다는 서술 확인. 2026-09-29-10 f8 과 같은 주장으로 ref-257 재사용 적절. 발행 2023-01."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 입력의 data/source_texts/ref-004.txt(RMF Core Overview)에 Fleet Adapter, 교통 일정·협상, 문·승강기·디스펜서 연동 서술 있음 — 연 원문으로 인정. 물류창고 대입은 추정이며 유지."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정. 인용한 finding 들이 모두 확인됨. 포장 단계 사례 없음은 본문에 명시하고 직전 실행 사례를 출처 없이 넣지 말 것."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정. 여섯 항목 대입이 근거 finding 과 일치. 성과 항목은 벤더 주장에 기댐을 5절에 명시."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정. 직접 범위 서술이 분류 원문 19장 기준과 맞음."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정. '연계 대상: ' 표시 있음. 9절에서 외부 영역은 짧게 연계 대상으로만 다룰 것."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정. 연결 영역 번호·이름이 부록 A 와 일치."
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
      "ref-910~ref-913 id 가 같은 날 실행 2026-09-29-10 에서 다른 URL(The Robot Report, 아시아경제, 서울신문 등)에 부여된 id 와 충돌한다 — 내용 중복은 아니며 퍼블리셔가 URL 기준으로 새 id 를 부여해야 한다",
      "f22(다중 플릿 오케스트레이션 정의)는 2026-09-29-10 f8 과 같은 주장이며 ref-257 을 재사용했으므로 중복 각주 아님"
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
    "f1: 결론 문장에서 '레이아웃·저장 슬로팅·주문 배치·피커 경로·피커–주문 배정' 열거를 빼고 '창고 설계·계획·제어 논리 전반을 다시 세워야 한다'로 쓴다 — 초록에 그 목록이 없다.",
    "f5: 1,000대(빈 칸의 38.9%) 수치 옆에 '시뮬레이션 창고 기준'을 명시한다 — 실제 현장 측정이 아니다.",
    "f11: '2분 안에'를 '평균 2분'으로 고치고, AGV 대수·선반 1,000kg·2분·3,200억 원이 현장 공개에서 회사가 제공한 수치임을 문장에 병기한다 — 기사 원문 표현과 수치 출처가 그렇다.",
    "f12: 물류신문의 AGV 대수는 '1,000여 대', 소팅봇은 '수백 대가 넘는'으로 정확히 옮기고, 두 보도가 같은 현장 공개 행사의 회사 제공 정보에 기반해 독립성이 제한된다는 점을 5절 사례 문장이나 각주 옆에 남긴다 — 교차 확인은 인정하되 신뢰도는 medium 이다.",
    "f19: [사실] 유지하되 신뢰도를 high 에서 medium 으로 내리고, '2020-10-08 법 개정'을 '시행령 2020-10-08 개정, 2021-01-01 시행'으로 고친다 — 인증센터 법적근거 페이지 기준. 1~5등급·최대 2%p 이자 지원·시설자금 한도·용적률·높이 완화는 ref-921 URL(심사기준 페이지)에 없고 같은 인증센터 사이트의 인증혜택·법적근거 페이지에 있으므로 본문에 '스마트물류시설인증센터 인증혜택·법적근거 안내 기준'이라고 밝히고, 두 페이지(https://cslc.koti.re.kr/new_sub1/new_sub1_4, https://cslc.koti.re.kr/new_sub1/new_sub1_2)의 참고문헌 등록은 additional_research_requests 로 넘긴다 — 스토리텔러는 새 출처를 추가할 수 없다.",
    "f20: '120개 이상 도크'를 '간선차량 120여 대 동시 접안'으로 고치고 [추정]에 '벤더 주장'을 병기한다 — 보도자료 원문 표현이 그렇고 인증 사실은 인증센터 목록으로 대조되지 않았다.",
    "f10·f13·f15·f16·f17·f20: 본문에서 [추정]에 '벤더 주장'을 병기한다 — 회사 설명 수치이며 독립 확인이 없다.",
    "ref-003·ref-257: 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 두 항목에 source_unopened: true 를 넣는다 — 브리프가 fetched false 로 표시했다. ref-004 는 입력에 원문 텍스트(data/source_texts/ref-004.txt)가 있으므로 미열람 표기를 붙이지 않고 source_unopened: false 로 둔다 — 브리프 summary 의 '원문 미열람.' 머리말은 fetched 값과 어긋난 오기다.",
    "reference_updates: ref-910~ref-913 항목에 URL 을 정확히 적고 changelog_entry 에 '같은 날 실행 2026-09-29-10 의 ref-910~ref-913 과 id 충돌, URL 기준 병합 필요'를 남긴다 — 퍼블리셔가 새 id 를 부여할 근거가 되도록 한다.",
    "5절: 모든 사례의 현장 유형을 '물류창고'로 명시하고 여섯 항목(시작 조건·작업 대상·수행 자원·제약·완료·인계·예외·성과)에 f25 대로 놓되, 포장 단계는 '이번 실행에서 로봇 사례 미확인'으로 적고 직전 실행의 CJ대한통운 양팔 로봇 사례를 출처 없이 넣지 않는다 — f24 근거 발췌가 그렇게 밝혔다.",
    "f7: 반품 재적치 통합 연구가 피커 기반 창고의 최적화이며 로봇 피킹 적용이 아님을 5·6절 문장에 명시한다 — 출처 범위를 넘지 않기 위해서다.",
    "f16·f17: 각주 발행일은 브리프대로 2025-07 로 두되 본문 또는 각주 옆에 '페이지에 발행일 표기 없음(검색 결과 기준)'을 남긴다 — 기준일의 근거를 밝힌다.",
    "11절: oq-134·oq-138·oq-142·oq-146 은 상태를 바꾸지 않고 '이번 조사에서도 국내 물류창고 자료 미확인'으로 적고, open_questions_new 4건은 브리프 문구대로 관련 영역 번호·이름을 유지해 등록한다 — 근거 finding(f12·f18·f7·f15)이 모두 확인됐다.",
    "9절: f27 의 WMS 재고·주문 판단, 소터·컨베이어·도크 설비 제어, 하역·피킹 로봇의 인식·파지는 '연계 대상'으로 짧게만 다루고 ROP 직접 범위처럼 쓰지 않는다 — 분류 원문 19장 기준."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 28건, 미확인 0건, 교차 확인 2건(f11·f12 쿠팡 대구: 로봇신문/물류신문, 같은 현장 공개 기반이라 독립성 제한; f19 는 법적 근거 부분만 국토교통부/인증센터 2건). 강등: 없음(f19 신뢰도 high → medium: 등급·이자 수치가 인용 URL 이 아닌 같은 인증센터 사이트의 인증혜택·법적근거 페이지에 있고 단일 기관 근거). 원문 미열람 출처: ref-257(페이지 빈 응답, 검색 결과 일치), ref-003(브리프 미열람 표시, 검증에서 열어 표준 정의 확인). ref-004 는 입력 원문 텍스트로 열람 확인. 주의: 학술 서베이 4편(ref-910·911·912·913)과 국내 논문 2편은 초록만 확인했고 본문은 열지 않았다. 쿠팡·CJ대한통운·DHL·Amazon 사례의 성과 수치(65%, 48%, 35%, 10%, 하역 속도 우위 등)는 모두 회사 설명이며 벤더 주장으로 남는다. 국토교통부 인증제 세부 기준 첨부와 DHL 원 보도자료는 열지 못했다. ref-910~ref-913 은 같은 날 실행 2026-09-29-10 이 다른 URL 에 쓴 id 와 충돌하므로 퍼블리셔가 URL 기준으로 병합해야 한다. 정정 요청 없음. 열린 질문 해결 인정 없음(oq-134·oq-138·oq-142·oq-146 미해결 유지). 검증 예산: 검색 3회(브리프 15회와 합쳐 18/30), 열람 24회.",
  "retry_reason": null
}
```

### runs/2026-09-29-11/pages.json

```json
{
  "run_id": "2026-09-29-11",
  "outline": [
    {
      "path": "docs/categories/site-type-applications/warehouse.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "planned_findings": [
        "f1",
        "f2",
        "f22"
      ],
      "summary": "물류창고는 로봇 취급 시스템이 빠르게 늘고 있는 현장이며, 로봇이 들어오면 창고 설계·계획·제어 논리 전반을 다시 세워야 한다. [사실][^ref-910] 이 현장은 서로 다른 제조사의 플릿을 한 시스템 안에서 관리하는 다중 플릿 오케스트레이션 소프트웨어의 기본 현장으로 놓인다. [사실][^ref-257]"
    },
    {
      "path": "docs/categories/site-type-applications/warehouse.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1100,
      "planned_findings": [
        "f1",
        "f2",
        "f4",
        "f10",
        "f11",
        "f18",
        "f19"
      ],
      "summary": "상품-대-사람, 로봇 이동형 풀필먼트 시스템, 셔틀 기반 저장·회수 시스템, AMR 협업 피킹, 다중 에이전트 픽업·배송, WMS·WCS, 스마트물류센터 인증을 정의한다. 쿠팡 대구 풀필먼트센터는 사람-대-상품에서 상품-대-사람으로 전환했다. [사실][^ref-919]"
    },
    {
      "path": "docs/categories/site-type-applications/warehouse.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2300,
      "planned_findings": [
        "f7",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f20",
        "f25"
      ],
      "summary": "현장 유형 물류창고의 사례 셋(쿠팡 대구의 상품-대-사람 피킹·출하 분류, DHL 의 트레일러 하역, CJ대한통운 안성의 출하 분류·도크 배정)을 여섯 항목으로 쓴다. 국내 대형 센터는 적치·피킹·출하 분류·대용량 운반에 서로 다른 로봇을 층별로 나눠 투입한다. [사실][^ref-919][^ref-920]"
    },
    {
      "path": "docs/categories/site-type-applications/warehouse.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1500,
      "planned_findings": [
        "f3",
        "f4",
        "f5",
        "f7",
        "f8",
        "f9",
        "f17",
        "f24"
      ],
      "summary": "로봇 작업은 흐름 단계마다 다른 형태로 들어간다: 입고 하역 로봇, 적치·피킹의 상품-대-사람 운반, 보충 최적화, 출하 분류·도크 배정, 반품 재적치 통합. [추정][^ref-910][^ref-919][^ref-924] 온라인 작업 배정(MAPD)과 시뮬레이션 창고 기준 최대 1,000대의 지속형 경로 계획이 계획·제어의 규모 기준이다. [사실][^ref-006][^ref-005]"
    },
    {
      "path": "docs/categories/site-type-applications/warehouse.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1000,
      "planned_findings": [
        "f6",
        "f18",
        "f19",
        "f21",
        "f23"
      ],
      "summary": "국내 스마트물류센터 인증 심사기준은 기능영역을 하차·입고부터 상차·출고까지 6개 프로세스로 나누고 정보시스템을 WMS 150점·WCS/MCS 50점으로 둔다. [사실][^ref-921] GS1 EPCIS, Open-RMF, RAWSim-O 를 표로 정리한다."
    },
    {
      "path": "docs/categories/site-type-applications/warehouse.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 900,
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9"
      ],
      "summary": "로봇화 창고 서베이(Azadeh 외 2019), 전자상거래 창고 서베이(Boysen 외 2019), AMR 계획·제어 서베이(Fragapane 외 2021), MAPD·RHCR, 반품 통합, RAWSim-O, 국내 논문 2편을 정리한다. [사실][^ref-910][^ref-382][^ref-911]"
    },
    {
      "path": "docs/categories/site-type-applications/warehouse.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 900,
      "planned_findings": [
        "f26",
        "f27"
      ],
      "summary": "ROP 는 WMS 와 WCS/MCS 사이에서 흐름 단계별 작업 요청을 받아 이기종 플릿에 배정하고 경로를 조율하며 인계를 확인해 결과를 돌려주는 일을 맡는 것으로 보인다. [추정][^ref-921][^ref-257] WMS 재고 판단, 소터·도크 설비 제어, 하역·피킹 로봇의 인식·파지는 연계 대상이다. [추정][^ref-923][^ref-924]"
    },
    {
      "path": "docs/categories/site-type-applications/warehouse.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 900,
      "planned_findings": [
        "f28",
        "f22",
        "f23"
      ],
      "summary": "1·17·20·22·23·25·27·31·32·35·46·49번 영역과의 연결을 번호와 이름으로 적는다. 소터·도크 연동은 22. 설비·건물 시스템 연동, WMS·WCS 연동은 23. 업무 시스템 연동에 이어진다. [추정][^ref-923][^ref-921]"
    },
    {
      "path": "docs/categories/site-type-applications/warehouse.md",
      "section": "11. 열린 질문",
      "budget_chars": 800,
      "planned_findings": [
        "f7",
        "f12",
        "f15",
        "f18"
      ],
      "summary": "기존 oq-134·oq-138·oq-142·oq-146 은 상태를 바꾸지 않고 이번 조사에서도 국내 물류창고 자료 미확인으로 남기며, 이기종 로봇 통합 관제 사례·인증 심사의 오케스트레이션 평가·반품 통합의 로봇 적용·하역 예외 분담에 관한 새 질문 4건을 올린다."
    }
  ],
  "pages": [
    {
      "path": "docs/categories/site-type-applications/warehouse.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "섹션 3~11 신규 작성(seed → draft), 프런트매터 related_areas·tags·confidence·sources·last_run 채움, 13절 각주 20건 추가"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area61-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 61. 물류창고 의 \"8. 대표 연구와 자료\" 절(1,603자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area61-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 61. 물류창고 의 \"6. 대표 접근법과 기술\" 절(1,262자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area61-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 61. 물류창고 의 \"4. 핵심 개념과 용어\" 절(1,156자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area61-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 61. 물류창고 의 \"11. 열린 질문\" 절(1,068자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area61-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 61. 물류창고 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,062자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area61-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 61. 물류창고 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(868자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area61-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 61. 물류창고 의 \"3. 왜 중요한가\" 절(855자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-29 | 61. 물류창고 | 3~11절 신규 작성(seed → draft): 흐름 단계별 로봇 작업, 쿠팡 대구·DHL·CJ대한통운 사례, 스마트물류센터 인증 심사기준, ROP 직접 범위; 같은 날 실행 2026-09-29-10 의 ref-910~ref-913 과 id 충돌, URL 기준 병합 필요 | run 2026-09-29-11",
  "index_updates": {
    "home_recent": "2026-09-29 — 61. 물류창고: 3~11절 신규 작성(입고~반품 흐름 단계별 로봇 작업, 국내 쿠팡 대구·CJ대한통운과 해외 DHL·Amazon 사례, 스마트물류센터 인증 심사기준, ROP 직접 범위와 연계 대상)",
    "category_recent": "2026-09-29 — 61. 물류창고: 3~11절 신규 작성(흐름 단계별 로봇 작업 지도, 물류창고 사례 3건과 여섯 항목, 인증 심사기준의 6개 프로세스와 WMS·WCS/MCS 계층, 새 열린 질문 4건)",
    "area_recent": "2026-09-29 — 61. 물류창고: 3~11절 신규 작성. 학술 서베이 3편, MAPD·지속형 MAPF, RAWSim-O, 국내 논문 2편, 인증 심사기준, 쿠팡 대구·DHL·CJ대한통운 사례를 정리하고 새 열린 질문 4건을 올렸다"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "goods-to-person",
      "term_ko": "상품-대-사람",
      "term_en": "Goods-to-Person (GTP)",
      "definition": "로봇이나 설비가 선반·토트를 작업자 스테이션으로 가져와 작업자는 제자리에서 피킹하는 방식으로, 작업자가 선반까지 걸어가는 사람-대-상품(Person-to-Goods, PTG) 방식과 대비되며 로봇 이동형 풀필먼트 시스템이 대표 구현이다.",
      "description": "쿠팡 대구 풀필먼트센터는 2023-02-07 현장 공개에서 사람-대-상품에서 상품-대-사람 방식으로 전환했다고 알렸다. 전자상거래 창고 서베이는 자동 피킹 워크스테이션·로봇·AGV 지원 피킹을 자동화 선택지로 든다.",
      "related_areas": [
        61,
        31,
        25
      ],
      "sources": [
        "ref-919",
        "ref-382"
      ]
    },
    {
      "action": "new",
      "slug": "shuttle-based-storage-and-retrieval-system",
      "term_ko": "셔틀 기반 저장·회수 시스템",
      "term_en": "Shuttle-Based Storage and Retrieval System (SBS/RS)",
      "definition": "층마다 움직이는 셔틀 차량과 리프트로 토트·상자를 랙에 넣고 꺼내는 자동 창고 시스템으로, 로봇화 창고 서베이가 로봇 이동형 풀필먼트 시스템·셔틀 기반 압축 저장 시스템과 함께 새 범주로 검토한다.",
      "related_areas": [
        61,
        35
      ],
      "sources": [
        "ref-910"
      ]
    },
    {
      "action": "new",
      "slug": "amr-assisted-order-picking",
      "term_ko": "AMR 협업 피킹",
      "term_en": "AMR-assisted Order Picking",
      "definition": "자율이동로봇이 피킹 경로를 따라 작업자와 함께 움직이며 상품을 싣고 나르고 작업자는 집는 일만 맡는 방식으로, 기존 피커-대-상품 창고에 큰 개조 없이 도입할 수 있어 전자상거래 창고 서베이가 자동화 선택지의 하나로 든다.",
      "description": "CJ대한통운은 AMR 기반 오더피킹에서 작업자 1명이 시간당 120 오더라인을 처리한다고 설명하나 이는 벤더 주장이다.",
      "related_areas": [
        61,
        31
      ],
      "sources": [
        "ref-382",
        "ref-917"
      ]
    },
    {
      "action": "new",
      "slug": "smart-logistics-center-certification",
      "term_ko": "스마트물류센터 인증",
      "term_en": "Smart Logistics Center Certification",
      "definition": "물류시설의 개발 및 운영에 관한 법률 제21조의4에 따라 국토교통부가 첨단·자동화 설비를 갖춘 물류창고를 1~5등급으로 인증하는 제도로, 하차·입고부터 상차·출고까지 6개 프로세스의 기능영역과 구조·성과·정보시스템의 기반영역을 심사한다.",
      "description": "심사기준(일반)은 기능영역 600점(6개 프로세스 각 100점)과 기반영역 400점(구조적 성능 100점, 성과관리 100점, 정보시스템 200점: WMS 150점·WCS/MCS 50점), 우수물류신기술 가산점 최대 50점으로 구성된다. 운영은 한국교통연구원 스마트물류시설인증센터가 맡는다.",
      "related_areas": [
        61,
        23,
        59
      ],
      "sources": [
        "ref-124",
        "ref-921"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-910",
      "org": "Azadeh, K., de Koster, R., & Roy, D. (Transportation Science 53(4))",
      "title": "Robotized and Automated Warehouse Systems: Review and Recent Developments",
      "published": "2019-06-28",
      "url": "https://pubsonline.informs.org/doi/10.1287/trsc.2018.0873",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "셔틀 기반 저장·회수, 셔틀 기반 압축 저장, 로봇 이동형 풀필먼트 시스템을 검토한 로봇화 창고 서베이. 출판사 페이지는 403 이라 Semantic Scholar API 로 서지·초록만 읽었다. 같은 날 실행 2026-09-29-10 의 ref-910 과 id 충돌(URL 기준 병합 필요).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-911",
      "org": "Fragapane, G., de Koster, R., Sgarbossa, F., & Strandhagen, J. O. (European Journal of Operational Research 294(2))",
      "title": "Planning and control of autonomous mobile robots for intralogistics: Literature review and research agenda",
      "published": "2021",
      "url": "https://doi.org/10.1016/j.ejor.2021.01.019",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "AMR 의 분산 의사결정과 계획·제어(스케줄링·라우팅·배차) 프레임워크, 창고·제조·크로스독·터미널·병원 적용 분야를 정리한 문헌 검토. 에라스무스 대학교 RePub 저장소 페이지에서 초록을 읽었다. 같은 날 실행 2026-09-29-10 의 ref-911 과 id 충돌(URL 기준 병합 필요).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-382",
      "org": "Boysen, N., Weidinger, F., & de Koster, R. (European Journal of Operational Research 277(2))",
      "title": "Warehousing in the e-commerce era: A survey",
      "published": "2019",
      "url": "https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "전자상거래 주문 특성에 맞춘 자동화 시스템(자동 피킹 워크스테이션·로봇·AGV 지원 피킹)과 조직적 적응(혼합 선반 저장·동적 주문 처리·배치·존·분류)을 정리한 서베이(온라인 2018-08-23, 권호 277(2) 396–411). 같은 날 실행 2026-09-29-10 의 ref-382 와 id 충돌(URL 기준 병합 필요).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-913",
      "org": "Schrotenboer, A. H., Wruck, S., Vis, I. F. A., & Roodbergen, K. J.",
      "title": "Integration of returns and decomposition of customer orders in e-commerce warehouses",
      "published": "2019-09-01",
      "url": "https://arxiv.org/abs/1909.01794",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "반품 재적치를 피커 경로에 통합하면 10~15%, 주문 분해까지 허용하면 44% 비용 절감을 보고한 프리프린트(피커 기반 창고). 같은 날 실행 2026-09-29-10 의 ref-913 과 id 충돌(URL 기준 병합 필요).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-101",
      "org": "Merschformann, M. (RAWSim-O GitHub 공식 저장소)",
      "title": "RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README)",
      "published": null,
      "url": "https://github.com/merschformann/RAWSim-O",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "로봇 이동형 풀필먼트 시스템용 이산 사건 시뮬레이션 프레임워크의 공식 README. GPL v3 이상, 2D·3D 시각화·다층 창고·히트맵 기능, 대표 논문 Logistics Research 11(1) 2018.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-915",
      "org": "곽경민, 박범, 고은지, 윤철주, 김경훈 (CJ대한통운, 로봇학회 논문지 17(4))",
      "title": "급속 확산되는 물류현장의 로봇적용 사례",
      "published": "2022",
      "url": "https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002899267",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "계약물류·소포·풀필먼트의 차이에 따른 물류 로봇 적용(로봇 낱개 피킹, 박스 취급, AGV·AMR, ASRS, 웨어러블)을 정리한 국내 논문(pp. 387–396). 저자 전원 CJ대한통운 소속.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-916",
      "org": "김태현, 송상화 (인천대학교, 한국디지털산업학회지 26(1))",
      "title": "온라인 주문 풀필먼트를 위한 물류센터 피킹 설비 최적화에 대한 연구",
      "published": "2021",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002687327",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "오더피킹 설비의 재고 보충을 혼합정수계획 모형으로 최적화하고 실제 운영 데이터와 시뮬레이션으로 검증한 국내 논문(pp. 67–78).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-917",
      "org": "로봇신문 (장길수)",
      "title": "CJ대한통운이 뽑은 물류자동화 혁신 기술 '톱3'",
      "published": "2022-05-06",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=28424",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-29",
      "summary": "CJ대한통운이 밝힌 QPS·지능형 스캐너·AMR 의 기능과 처리량 수치를 전한 기사. 수치는 회사 설명이다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-918",
      "org": "Amazon",
      "title": "Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot",
      "published": "2025-07",
      "url": "https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "로봇 100만 대 배치와 플릿 조율용 생성형 AI 기반 모델 DeepFleet(이동 시간 10% 개선 주장)을 알린 Amazon 자사 발표. 페이지에 발행일 표기가 없어 검색 결과의 2025-07 로 적었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-919",
      "org": "로봇신문 (장길수)",
      "title": "쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이...",
      "published": "2023-02-07",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=30736",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "쿠팡 대구 풀필먼트센터 현장 공개 취재. AGV 1,000대 이상·소팅봇 수백 대·무인지게차 수십 대의 역할, 3,200억 원 투자, PTG→GTP 전환. 수치는 현장 공개에서 회사가 제공한 것이다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-920",
      "org": "물류신문 (석한글)",
      "title": "‘물류 투자만 6조’, 쿠팡 물류 인프라의 정점 ‘대구 FC’ 가보니",
      "published": "2023-02-07",
      "url": "https://www.klnews.co.kr/news/articleView.html?idxno=306994",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "같은 현장 공개를 취재한 물류 전문지 기사. 층별 로봇 배치(7층 AGV 1,000여 대, 1층 수백 대가 넘는 소팅봇, 5층 무인지게차)와 구역 분리·안전 센서, 33만㎡ 규모. 로봇신문과 같은 행사 기반이라 독립성은 제한적이다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-921",
      "org": "스마트물류시설인증센터 (한국교통연구원)",
      "title": "인증스마트물류센터 : 인증심사 > 심사기준 > 일반",
      "published": null,
      "url": "https://cslc.koti.re.kr/new_sub2/new_sub2_2_1",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "스마트물류센터 인증 심사기준(일반): 기능영역 6개 프로세스 각 100점, 기반영역 구조·성과·정보시스템(WMS 150·WCS/MCS 50), 가산점 최대 50점.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-124",
      "org": "국토교통부 (국가물류통합정보센터)",
      "title": "스마트물류센터 인증제 안내",
      "published": null,
      "url": "https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "물류시설법 제21조의4에 따른 스마트물류센터 인증제의 목적·대상(본인증·예비인증) 안내. 세부 기준은 첨부 파일에 있어 페이지에서는 읽지 못했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-923",
      "org": "CJ대한통운",
      "title": "CJ대한통운 안성 MP허브, 국토부 ‘스마트물류센터 1등급’ 인증",
      "published": "2023-10-26",
      "url": "https://cjlogistics.com/ko/newsroom/news/NR_00001109",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "안성 MP허브터미널의 스마트물류센터 1등급 인증과 크로스벨트 소터·로드 밸런싱·도크 관리 시스템·하루 200만 건 처리를 알린 회사 보도자료. 인증 사실은 인증센터 목록으로 대조하지 못했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-924",
      "org": "Robotics 24/7 (Eugene Demaitre)",
      "title": "DHL Makes First Commercial Deployment of Boston Dynamics Stretch Robot to Unload Trailers and Containers",
      "published": "2023-02-01",
      "url": "https://www.robotics247.com/article/dhl_makes_first_commercial_deployment_boston_dynamics_stretch_robot_unload_trailers_containers",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "DHL Supply Chain 의 Stretch 트레일러·컨테이너 하역 로봇 첫 상업 배치, 1,500만 달러 투자, 향후 확대 계획을 전한 전문지 기사. DHL 원 보도자료는 연결 끊김으로 열지 못했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-003",
      "org": "GS1",
      "title": "EPCIS and CBV Linked Data Model",
      "published": null,
      "url": "https://ref.gs1.org/epcis/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 GS1 표준(분류 원문 22장 3번, 재사용). 이번 실행에서 다시 열지 않았다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고(분류 원문 22장 4번, 재사용). 입력의 원문 텍스트(data/source_texts/ref-004.txt)로 열람 확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-005",
      "org": "Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. (AAAI 2021)",
      "title": "Lifelong Multi-Agent Path Finding in Large-Scale Warehouses",
      "published": "2021-03-12",
      "url": "https://arxiv.org/abs/2005.07371",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "롤링 호라이즌 충돌 해결(RHCR)로 시뮬레이션 창고에서 최대 1,000대 에이전트의 지속형 경로 찾기를 푼 논문(분류 원문 22장 5번, 재사용). arXiv 초록을 열어 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-006",
      "org": "Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. (AAMAS 2017)",
      "title": "Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks",
      "published": "2017-05-30",
      "url": "https://arxiv.org/abs/1705.10868",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자동화 창고의 온라인 픽업·배송 작업 스트림을 다루는 MAPD 문제와 TP·TPTS 알고리즘(분류 원문 22장 6번, 재사용). arXiv 초록을 열어 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    },
    {
      "id": "ref-257",
      "org": "Interact Analysis (Rueben Scriven)",
      "title": "AMR Multi-Fleet Orchestration Software Explained",
      "published": "2023-01",
      "url": "https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 다중 플릿 오케스트레이션 소프트웨어의 정의와 저수준·고수준 제어 접근, 표준·미들웨어 기반 상호운용(2026-09-29-10 재사용). 이번 실행에서 다시 열지 않았다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/site-type-applications/warehouse.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "국내 물류센터에서 서로 다른 제조사의 AGV·소팅봇·무인지게차·하역 로봇을 하나의 오케스트레이션 계층으로 관제한 공개 사례가 있는가(쿠팡 대구·CJ대한통운 사례는 설비별 도입만 확인됐다)?",
      "areas": [
        61,
        20
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "스마트물류센터 인증 심사기준의 정보시스템 항목(WMS 150점, WCS/MCS 50점)에서 이기종 로봇 오케스트레이션 계층은 어느 항목으로 평가되며 인증 심사가 로봇 플릿 관제 기능을 따로 보는가?",
      "areas": [
        61,
        23
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "반품 재적치를 피킹 경로에 통합하는 최적화 연구를 로봇 이동형 풀필먼트 시스템이나 AMR 협업 피킹에 적용한 연구·사례가 있는가?",
      "areas": [
        61,
        25
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "트레일러 하역 로봇의 떨어진 상자 복구 같은 예외 처리가 로봇 자체 복구와 오케스트레이션 계층의 재계획 사이에서 어떻게 분담되는지 공개된 인터페이스나 사례가 있는가?",
      "areas": [
        61,
        32
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/site-type-applications/warehouse.md#5-적용-사례-현장-유형-명시",
      "title": "61. 물류창고"
    },
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/site-type-applications/warehouse.md#5-적용-사례-현장-유형-명시",
      "title": "61. 물류창고"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/site-type-applications/warehouse.md#5-적용-사례-현장-유형-명시",
      "title": "61. 물류창고"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/site-type-applications/warehouse.md#5-적용-사례-현장-유형-명시",
      "title": "61. 물류창고"
    },
    {
      "site_type": "물류창고",
      "item": "완료·인계",
      "link": "docs/categories/site-type-applications/warehouse.md#5-적용-사례-현장-유형-명시",
      "title": "61. 물류창고"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/site-type-applications/warehouse.md#5-적용-사례-현장-유형-명시",
      "title": "61. 물류창고"
    }
  ],
  "additional_research_requests": [
    "7절 스마트물류센터 인증제 행: 1~5등급·최대 2%p 이자 지원·시설자금 한도·용적률·높이 완화·시행령 개정일의 직접 근거인 스마트물류시설인증센터 인증혜택 페이지(https://cslc.koti.re.kr/new_sub1/new_sub1_4)와 법적근거 페이지(https://cslc.koti.re.kr/new_sub1/new_sub1_2)를 참고문헌으로 등록해야 한다 — 1차 검증이 확인했으나 브리프 출처에 없어 본문은 ref-921·ref-124 로만 각주를 달았다.",
    "5절 포장 단계: 물류창고 포장 단계의 로봇 도입 사례(출처 있는 것)가 필요하다 — 이번 브리프에 없어 '이번 실행에서 로봇 사례 미확인'으로 두었다(직전 실행 2026-09-29-10 의 CJ대한통운 양팔 로봇 사례를 재인용하려면 그 출처를 이 영역 브리프에 넣어야 한다).",
    "5절 DHL 사례: DHL 원 보도자료(dhl.com 2023-02, group.dhl.com 2025-05·2025-07)를 열어 전문지 기사(ref-924)와 대조하고, 하역 사례의 제약·완료 확인 방식(현재 '미확인')을 채울 사실이 필요하다.",
    "5·7절 인증: CJ대한통운 안성 MP허브터미널의 1등급 인증 사실을 스마트물류시설인증센터의 인증 목록으로 대조하고, 등급 구분 점수 기준(심사기준 페이지에 없음)을 확인해야 한다.",
    "11절: oq-134·oq-138·oq-142·oq-146(국내 물류창고의 운영 기록 시뮬레이션 재현, 대화형 시나리오 구성·업무 지시, 소음 조건 음성 지시 인식률)은 이번 실행에서 별도 검색 예산이 배분되지 않아 미해결로 남았다 — 다음 실행에서 국내 자료를 겨냥한 검색이 필요하다.",
    "13절 각주: 재사용 참고문헌 ref-003·ref-004·ref-005·ref-006·ref-257 의 각주 줄은 참고문헌 목록 입력이 0건이라 docs/references/ref-NNN.md 의 '각주 형식' 줄과 대조하지 못하고 브리프 sources 값으로 적었다 — 퍼블리셔가 등록된 기관·제목·URL 과 맞춰야 한다.",
    "6절 계획·제어: 국내 물류창고의 이기종 플릿 통합 관제나 로봇 밀도·처리능력 설계 수치를 보고한 독립 출처(학술·기관)가 있으면 성과 항목의 벤더 주장(65%, 48%, 35%, 10%)을 대체하거나 대조할 수 있다."
  ],
  "fixes_applied": [
    "f1 열거 삭제 — 3절 첫 단락에서 '레이아웃·저장 슬로팅·주문 배치·피커 경로·피커–주문 배정' 열거를 빼고 '창고 설계·계획·제어 논리 전반을 다시 세워야 한다'로 썼다.",
    "f5 시뮬레이션 창고 기준 명시 — 6절 '온라인 작업 배정과 대규모 경로 계획', 8절 Li 외 항목, 10절 27. 다중 로봇 경로·교통 관리 — MAPF 연결에서 1,000대(지도 빈 칸의 38.9%) 수치 옆에 '시뮬레이션 창고 기준'을 붙였다.",
    "f11 표현·출처 병기 — 5절 쿠팡 대구 사례의 표(완료·인계·예외·성과)와 서술에서 '2분 안에'를 '평균 2분'으로 고치고, AGV 대수·선반 1,000kg·평균 2분·3,200억 원 이상이 현장 공개에서 회사가 제공한 수치임을 문장에 병기했다.",
    "f12 정확한 옮김·독립성 표시 — 5절에서 물류신문의 AGV 는 '1,000여 대', 소팅봇은 '수백 대가 넘는'으로 옮기고, 두 보도가 같은 현장 공개 행사의 회사 제공 정보에 기반해 독립성이 제한된다는 문장을 사례 서술에 [의견] 으로 남겼다(교차 확인은 [사실][^ref-919][^ref-920] 로 유지, 페이지 신뢰도 medium).",
    "f19 신뢰도·문구·출처 범위 — [사실] 로 유지하되 페이지 confidence 는 verification.json 의 medium 을 썼고, 4·7절에서 '시행령은 2020-10-08 개정돼 2021-01-01 시행'으로 고쳤으며, 7절 인증제 행에 '스마트물류시설인증센터 인증혜택·법적근거 안내 기준'을 밝히고 두 페이지의 참고문헌 등록은 additional_research_requests 첫 항목으로 넘겼다.",
    "f20 표현·벤더 주장 병기 — 5절 CJ대한통운 안성 사례의 표와 서술에서 '120개 이상 도크'를 '간선차량 120여 대 동시 접안'으로 고치고, 모든 문장을 [추정] 벤더 주장[^ref-923] 으로 썼으며 인증 사실이 인증센터 목록으로 대조되지 않았음을 적었다.",
    "f10·f13·f15·f16·f17·f20 벤더 주장 병기 — 4절 AMR 협업 피킹(f10), 5절 쿠팡 65%(f13)·DHL 하역 속도와 복구 목표(f15)·Amazon 로봇 100만 대(f16)·CJ대한통운 QPS·ITS·AMR(f10)·안성(f20), 6절 DeepFleet 10%(f17), 10절 1·46번 연결(f16·f17)에서 [추정] 뒤에 '벤더 주장'을 병기했다.",
    "ref-003·ref-257 미열람 표기, ref-004 열람 표기 — 13절 각주 정의에서 ref-003·ref-257 의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 두 항목에 source_unopened: true 를 넣었으며, ref-004 는 미열람 표기를 붙이지 않고 source_unopened: false 로 두고 summary 의 '원문 미열람.' 머리말을 제거했다.",
    "ref-910~ref-913 URL·id 충돌 기록 — reference_updates 의 네 항목에 브리프 URL 을 그대로 적고 summary 에 충돌 사실을 덧붙였으며, changelog_entry 에 '같은 날 실행 2026-09-29-10 의 ref-910~ref-913 과 id 충돌, URL 기준 병합 필요'를 남겼다.",
    "5절 현장 유형·여섯 항목·포장 단계 — 사례 셋(쿠팡 대구, DHL 하역, CJ대한통운 안성) 모두 '현장 유형: 물류창고'를 명시하고 여섯 항목 표를 f25 대로 채웠으며, 포장 단계는 '이번 실행에서 로봇 사례를 확인하지 못했다'로 적고 직전 실행의 CJ대한통운 양팔 로봇 사례는 넣지 않았다.",
    "f7 피커 기반 명시 — 5절 반품 단계 문장과 6절 '보충과 반품의 최적화', 8절 Schrotenboer 항목에서 이 연구가 피커 기반 창고의 최적화이며 로봇 피킹 적용이 아님을 명시했다.",
    "f16·f17 기준일 근거 — 13절 각주 발행일은 브리프대로 2025-07 로 두고, 5절 Amazon 문장에 '페이지에 발행일 표기 없음, 검색 결과 기준'을 남겼다.",
    "11절 기존·신규 질문 — oq-134·oq-138·oq-142·oq-146 은 상태 '열림'을 바꾸지 않고 '이번 조사에서도 국내 물류창고 자료 미확인'으로 적었으며(open_question_updates 에 update 없음), open_questions_new 4건은 브리프 문구대로 관련 영역 번호·이름을 유지해 페이지 11절과 open_question_updates(new, areas 61·20 / 61·23 / 61·25 / 61·32)에 등록했다.",
    "9절 연계 대상 — f27 의 WMS 재고·주문 판단, 소터·컨베이어·도크 설비 제어, 하역·피킹 로봇의 인식·파지를 표 오른쪽 열에 '연계 대상:' 접두어로 짧게만 적고, 아래 단락에서 분류 원문 19장의 외부 영역임을 밝혀 ROP 직접 범위처럼 쓰지 않았다.",
    "분량 초과 자동 분리: 61. 물류창고 본문 12,217자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 5,137자"
  ]
}
```

### runs/2026-09-29-11/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/site-type-applications/warehouse.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-29-area61-s8.md (1,603자)
    - docs/categories/site-type-applications/warehouse.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-29-area61-s6.md (1,262자)
    - docs/categories/site-type-applications/warehouse.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-29-area61-s4.md (1,156자)
    - docs/categories/site-type-applications/warehouse.md "11. 열린 질문" → docs/topics/2026/2026-09-29-area61-s11.md (1,068자)
    - docs/categories/site-type-applications/warehouse.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-29-area61-s7.md (1,062자)
    - docs/categories/site-type-applications/warehouse.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-29-area61-s10.md (868자)
    - docs/categories/site-type-applications/warehouse.md "3. 왜 중요한가" → docs/topics/2026/2026-09-29-area61-s3.md (855자)
```

### runs/2026-09-29-11/pages/categories/site-type-applications/warehouse.md

```markdown
---
title: "61. 물류창고"
type: area
category: "Q. 현장 유형별 적용"
area_no: 61
related_areas: [1, 17, 20, 22, 23, 25, 27, 31, 32, 35, 46, 49]
tags: [상품-대-사람, 로봇 이동형 풀필먼트 시스템, 소팅 로봇, 무인지게차, 스마트물류센터 인증]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-003, ref-004, ref-005, ref-006, ref-257, ref-910, ref-911, ref-382, ref-913, ref-101, ref-915, ref-916, ref-917, ref-918, ref-919, ref-920, ref-921, ref-124, ref-923, ref-924]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 61. 물류창고

# 61. 물류창고

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

입고~반품 흐름의 로봇 작업. 기존 흐름 매트릭스와 영역 페이지의 물류 시나리오를 사례로 모은다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **물류창고 작업 흐름 적용**: 입고·적치·보충·피킹·포장·출하·반품 흐름에 로봇 작업을 대입해 시작 조건·작업 대상·수행 자원·제약·완료·예외를 정리한다

## 2. 핵심 질문

물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? [분류원문]

## 3. 왜 중요한가

물류창고는 로봇 취급 시스템이 빠르게 늘고 있는 현장이며, 로봇이 들어오면 창고 설계·계획·제어 논리 전반을 다시 세워야 한다. [사실][^ref-910]

자세한 내용은 주제 페이지 [61. 물류창고 — 왜 중요한가](../../topics/2026/2026-09-29-area61-s3.md)에 있다.

## 4. 핵심 개념과 용어

**상품-대-사람(Goods-to-Person, GTP)** — 로봇이나 설비가 선반·토트를 작업자 스테이션으로 가져와 작업자는 제자리에서 피킹하는 방식으로, 작업자가 선반까지 걸어가는 사람-대-상품(Person-to-Goods, PTG) 방식과 대비된다. 쿠팡 대구 풀필먼트센터는 PTG 에서 GTP 로 전환했다. [사실][^ref-919]

자세한 내용은 주제 페이지 [61. 물류창고 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area61-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

아래 사례는 모두 현장 유형이 물류창고이며, 예외·성과 항목의 수치는 회사 설명에 기댄 것이라 벤더 주장으로 남는다. [추정][^ref-917][^ref-919][^ref-924][^ref-918]

**현장 유형:** 물류창고

**사례:** 쿠팡 대구 풀필먼트센터의 상품-대-사람 피킹과 출하 분류(적치 → 피킹 → 출하 단계)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 소량·소수 라인의 시간 민감 전자상거래 주문이 대량으로 발생한다. [사실][^ref-382] |
| 작업 대상 | 최대 1,000kg 선반(pod)에 적치된 상품과 8kg 이하의 포장된 소형 상품. [사실][^ref-919][^ref-920] |
| 수행 자원 | 7층의 AGV 1,000여 대(선반 운반), 1층의 수백 대가 넘는 소팅봇(포장 라벨 바코드 판독·목적지 분류), 5층의 무인지게차 수십 대(대용량 운반), 상품-대-사람 스테이션의 작업자. [사실][^ref-919][^ref-920] |
| 제약 | 선반 최대 1,000kg, 소팅봇 8kg 이하, AGV 는 바닥 QR 코드 경로, 무인지게차는 사람 출입을 막은 구역에서만 주행하고 경계 침범 시 안전 센서로 정지. [사실][^ref-919][^ref-920] |
| 완료·인계 | 선반이 작업자에게 평균 2분에 도착(현장 공개에서 회사가 제공한 수치), 소팅봇의 바코드 판독과 목적지별 분류·이송. [사실][^ref-919] |
| 예외·성과 | AGV 의 연중 24시간 가동과 자동 충전, 전체 업무 단계 65% 감소(산정 방법 미공개). [추정] 벤더 주장[^ref-919][^ref-920] 투자액 3,200억 원 이상(회사 제공 수치). [사실][^ref-919] |

2023-02-07 현장 공개를 취재한 로봇신문에 따르면 이 센터는 바닥 QR 코드를 따라 최대 1,000kg 의 선반을 작업자에게 평균 2분에 가져오는 AGV 1,000대 이상, 포장 라벨 바코드를 읽어 목적지별로 분류·이송하는 소팅봇 수백 대, 버튼 한 번으로 대용량 제품을 옮기며 사람 출입을 막은 구역에서만 움직이는 무인지게차 수십 대를 갖추고 PTG 에서 GTP 로 전환했으며, AGV 대수·선반 1,000kg·평균 2분·3,200억 원 이상의 투자액은 현장 공개에서 회사가 제공한 수치다. [사실][^ref-919] 같은 날 물류신문은 7층의 AGV 1,000여 대(최대 1,000kg 선반 운반), 1층의 수백 대가 넘는 소팅봇(8kg 이하 상품 분류), 5층의 무인지게차(작업자 구역과 분리, 경계 침범 시 안전 센서로 정지)를 같은 내용으로 전해, 국내 물류창고에서 적치·피킹, 출하 분류, 대용량 운반에 서로 다른 로봇이 층별로 나뉘어 투입된 사례가 확인된다. [사실][^ref-919][^ref-920] 두 보도는 같은 현장 공개 행사의 회사 제공 정보에 기반하므로 교차 확인의 독립성은 제한적이다. [의견][^ref-919][^ref-920] 쿠팡은 AGV 가 연중 24시간 가동되고 필요 시 자동 충전하며 이를 통해 전체 업무 단계를 65% 줄였다고 설명했으나 산정 방법은 밝히지 않았다. [추정] 벤더 주장[^ref-919][^ref-920]

**현장 유형:** 물류창고

**사례:** DHL Supply Chain 의 트레일러·컨테이너 하역(입고 단계)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 트레일러·컨테이너 도착 뒤의 하역작업. 국내 인증 심사기준은 하차·입고 프로세스를 입고예정정보 확인, 하역작업, 상품검수, 제품정보 인식·등록으로 나눈다. [사실][^ref-921] |
| 작업 대상 | 트레일러 뒤쪽에 실린 상자(carton). [사실][^ref-924] |
| 수행 자원 | Boston Dynamics 의 Stretch 로봇이 상자를 집어 유연 컨베이어에 올린다. [사실][^ref-924] 사람의 개입은 줄이는 것이 목표다. [추정] 벤더 주장[^ref-924] |
| 제약 | 출처에 명시된 제약 없음(미확인). |
| 완료·인계 | 상자가 유연 컨베이어로 넘어간다. [사실][^ref-924] 검수·제품정보 등록 방식은 출처에 없음(미확인). |
| 예외·성과 | 떨어진 상자의 자동 복구 개선이 향후 목표이며, 하역 속도가 시험한 모든 환경에서 수작업을 넘어섰다는 설명은 수치 근거가 없다. [추정] 벤더 주장[^ref-924] DHL 은 1년 전 Boston Dynamics 로봇에 1,500만 달러를 투자했다. [사실][^ref-924] |

Robotics 24/7(2023-02-01)에 따르면 DHL Supply Chain 은 Stretch 를 트레일러·컨테이너 하역에 상업 배치한 첫 회사이며, 이후 여러 창고로 확대하고 하역 외 작업으로 넓힐 계획이라고 보도됐다. [사실][^ref-924] DHL 원 보도자료는 브리프가 열지 못했고 전문지 기사로 대신했다. [의견][^ref-924]

**현장 유형:** 물류창고

**사례:** CJ대한통운 안성 MP허브터미널의 출하 분류·도크 배정(출하 단계)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 하루 200만 건 규모의 소형 상품 분류 요청. [추정] 벤더 주장[^ref-923] |
| 작업 대상 | 소형 상품(소포). [추정] 벤더 주장[^ref-923] |
| 수행 자원 | 크로스벨트 소터, 컨베이어 센서로 화물을 분산하는 로드 밸런싱, 간선차량 배정을 맡는 AI 기반 도크 관리 시스템(DMS). [추정] 벤더 주장[^ref-923] |
| 제약 | 간선차량 120여 대 동시 접안, 연면적 12,000㎡. [추정] 벤더 주장[^ref-923] |
| 완료·인계 | 국내 인증 심사기준의 상차·출고 프로세스 항목인 발주처별 분류, 차량입차, 상차순서관리, 출고정보전달. [사실][^ref-921] |
| 예외·성과 | 오류 자동 복구 기술, 하루 200만 건 처리, 스마트물류센터 1등급 인증(자사 9번째, 인증센터 목록으로 대조되지 않음). [추정] 벤더 주장[^ref-923] |

CJ대한통운은 2023-10-26 보도자료에서 이 터미널이 국토교통부 스마트물류센터 1등급 인증을 받았고 크로스벨트 소터, 로드 밸런싱, 간선차량 120여 대 동시 접안 도크의 차량 배정을 맡는 DMS, 오류 자동 복구 기술로 하루 200만 건의 소형 상품을 처리한다고 밝혔으나, 인증 사실은 인증센터 목록으로 대조되지 않았다. [추정] 벤더 주장[^ref-923] 같은 회사가 2022-05-06 로봇신문을 통해 밝힌 QPS(피킹·이송·분류 컨베이어 분리, 시간당 최대 2,000건, 기존 DPS 대비 생산성 48% 증가)와 지능형 스캐너 ITS(시간당 약 7,000건 인식, 검수 시간 35% 이상 단축), AMR(12시간 배터리·50kg 적재·최대 7.2km/h)도 사이트가 명시되지 않은 회사 설명이다. [추정] 벤더 주장[^ref-917]

나머지 단계는 다음과 같다. 보충 단계는 국내 연구가 오더피킹 설비의 재고 보충을 혼합정수계획 모형으로 최적화했다(6절). [사실][^ref-916] 포장 단계는 이번 실행에서 로봇 사례를 확인하지 못했다. 반품 단계는 반품 재적치를 피커 경로에 통합하는 연구가 있으나 피커 기반 창고의 최적화이며 로봇 피킹 적용은 아니다. [사실][^ref-913] Amazon 은 2025년 7월 발표(페이지에 발행일 표기 없음, 검색 결과 기준)에서 100만 번째 로봇을 일본의 풀필먼트센터에 배치해 300개 이상 시설에 로봇 100만 대를 운용하며, 최대 1,250파운드의 재고를 옮기는 Hercules, 정밀 컨베이어로 개별 패키지를 다루는 Pegasus, 직원 주변을 주행하며 주문 카트를 옮기는 Proteus 와 플릿 이동을 조율하는 생성형 AI 기반 모델 DeepFleet 을 들었다. [추정] 벤더 주장[^ref-918] 여섯 항목을 종합하면 시작 조건은 전자상거래 주문과 입고예정정보, 작업 대상은 선반·토트·박스·팔레트·반품 상품, 수행 자원은 AGV·AMR·소팅봇·무인지게차·하역 로봇과 스테이션 작업자, 제약은 적재 한계·배터리·사람 출입 제한 구역, 완료·인계는 바코드 인식·검수·출고정보 전달과 인계 이벤트 기록, 예외·성과는 떨어진 상자 복구와 처리량·오더라인 지표로 채워지되, 성과 수치는 회사 설명이라 벤더 주장으로 남는다. [추정][^ref-382][^ref-913][^ref-917][^ref-919][^ref-920][^ref-921][^ref-924][^ref-003][^ref-918] 다룬 칸은 [현장 유형 매트릭스](../../site-matrix.md)에 반영한다.

## 6. 대표 접근법과 기술

확인한 자료를 종합하면 물류창고의 로봇 작업은 흐름 단계마다 다른 형태로 들어간다. [추정][^ref-910][^ref-382][^ref-913][^ref-915][^ref-916][^ref-917][^ref-919][^ref-920][^ref-921][^ref-923][^ref-924]

자세한 내용은 주제 페이지 [61. 물류창고 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area61-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [61. 물류창고 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area61-s7.md)에 있다.

## 8. 대표 연구와 자료

아래 학술 서베이와 국내 논문은 이번 실행에서 초록만 확인했고 본문은 열지 않았다.

자세한 내용은 주제 페이지 [61. 물류창고 — 대표 연구와 자료](../../topics/2026/2026-09-29-area61-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 입고예정·주문·보충·출고 정보를 흐름 단계별 작업 요청으로 받아 배정하고, 인계 확인 결과를 WMS 로 돌려준다 | 연계 대상: WMS 의 주문·재고·보충 규칙 판단 |
| 로봇 자체 지능·제어 | 하역 로봇·피킹 로봇·AGV 가 할 수 있는 작업과 실행 조건, 상태·실패·완료 확인 | 연계 대상: 하역 로봇의 상자 인식·파지, 로봇 낱개 피킹의 비전·파지, 떨어진 상자의 로봇 자체 복구 |
| 시설·설비 제어 | 소터·컨베이어·도크에 대한 작업 요청·예약·인계·상태 확인 | 연계 대상: 크로스벨트 소터·컨베이어·로드 밸런싱·도크 배정의 설비 제어 |

확인한 자료를 종합하면 물류창고에서 ROP 가 직접 맡을 범위는 인증 심사기준이 구분하는 정보시스템 계층(WMS 와 WCS/MCS) 사이에서 흐름 단계별 작업 요청을 받아 제조사가 다른 AGV·AMR·소팅봇·무인지게차·하역 로봇에 배정하고, 경로·교통을 조율하며, 바코드 인식·인계 이벤트로 완료를 확인해 결과를 WMS 로 돌려주는 일이며, 다중 플릿 오케스트레이션 소프트웨어가 창고 제어 시스템에 비견된다는 시장 정의와 맞는 것으로 보인다. [추정][^ref-921][^ref-257][^ref-004][^ref-006][^ref-005][^ref-003] 표 오른쪽 열의 항목은 분류 원문 19장의 상위 업무 시스템·로봇 자체 지능·제어·시설·설비 제어에 속하므로 연계 대상으로만 다루며, 이종 제조사를 잇는 ROP 는 이들에 작업 요청·예약·인계·상태 확인만 걸고 재고 판단·설비 제어·파지 성능은 WMS·설비 업체·로봇 제조사에 맡기는 것으로 본다. [추정][^ref-921][^ref-923][^ref-924][^ref-915] 이 경계는 제품 전략에 따라 이동할 수 있으며, 기준은 [범위 경계](../../about/scope-boundary.md) 페이지를 따른다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[1. 기술·시장·업체 동향](../planning-and-business/technology-market-and-vendor-trends.md) — Amazon 의 로봇 100만 대 배치와 다중 플릿 오케스트레이션 소프트웨어의 시장 정의는 이 현장의 시장 동향 근거다. [추정][^ref-918][^ref-257]

자세한 내용은 주제 페이지 [61. 물류창고 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area61-s10.md)에 있다.

## 11. 열린 질문

기존 열린 질문(상태 변경 없음. 전체 목록: [열린 질문](../../open-questions.md)):

자세한 내용은 주제 페이지 [61. 물류창고 — 열린 질문](../../topics/2026/2026-09-29-area61-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-29 (원문 미열람)
[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-29
[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. (AAAI 2021), Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2021-03-12, https://arxiv.org/abs/2005.07371, 접근일 2026-09-29
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. (AAMAS 2017), Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017-05-30, https://arxiv.org/abs/1705.10868, 접근일 2026-09-29
[^ref-257]: Interact Analysis (Rueben Scriven), AMR Multi-Fleet Orchestration Software Explained, 2023-01, https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/, 접근일 2026-09-29 (원문 미열람)
[^ref-910]: Azadeh, K., de Koster, R., & Roy, D. (Transportation Science 53(4)), Robotized and Automated Warehouse Systems: Review and Recent Developments, 2019-06-28, https://pubsonline.informs.org/doi/10.1287/trsc.2018.0873, 접근일 2026-09-29
[^ref-382]: Boysen, N., Weidinger, F., & de Koster, R. (European Journal of Operational Research 277(2)), Warehousing in the e-commerce era: A survey, 2019, https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/, 접근일 2026-09-29
[^ref-913]: Schrotenboer, A. H., Wruck, S., Vis, I. F. A., & Roodbergen, K. J., Integration of returns and decomposition of customer orders in e-commerce warehouses, 2019-09-01, https://arxiv.org/abs/1909.01794, 접근일 2026-09-29
[^ref-915]: 곽경민, 박범, 고은지, 윤철주, 김경훈 (CJ대한통운, 로봇학회 논문지 17(4)), 급속 확산되는 물류현장의 로봇적용 사례, 2022, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002899267, 접근일 2026-09-29
[^ref-916]: 김태현, 송상화 (인천대학교, 한국디지털산업학회지 26(1)), 온라인 주문 풀필먼트를 위한 물류센터 피킹 설비 최적화에 대한 연구, 2021, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002687327, 접근일 2026-09-29
[^ref-917]: 로봇신문 (장길수), CJ대한통운이 뽑은 물류자동화 혁신 기술 '톱3', 2022-05-06, https://www.irobotnews.com/news/articleView.html?idxno=28424, 접근일 2026-09-29
[^ref-918]: Amazon, Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot, 2025-07, https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model, 접근일 2026-09-29
[^ref-919]: 로봇신문 (장길수), 쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이..., 2023-02-07, https://www.irobotnews.com/news/articleView.html?idxno=30736, 접근일 2026-09-29
[^ref-920]: 물류신문 (석한글), ‘물류 투자만 6조’, 쿠팡 물류 인프라의 정점 ‘대구 FC’ 가보니, 2023-02-07, https://www.klnews.co.kr/news/articleView.html?idxno=306994, 접근일 2026-09-29
[^ref-921]: 스마트물류시설인증센터 (한국교통연구원), 인증스마트물류센터 : 인증심사 > 심사기준 > 일반, 미확인, https://cslc.koti.re.kr/new_sub2/new_sub2_2_1, 접근일 2026-09-29
[^ref-923]: CJ대한통운, CJ대한통운 안성 MP허브, 국토부 ‘스마트물류센터 1등급’ 인증, 2023-10-26, https://cjlogistics.com/ko/newsroom/news/NR_00001109, 접근일 2026-09-29
[^ref-924]: Robotics 24/7 (Eugene Demaitre), DHL Makes First Commercial Deployment of Boston Dynamics Stretch Robot to Unload Trailers and Containers, 2023-02-01, https://www.robotics247.com/article/dhl_makes_first_commercial_deployment_boston_dynamics_stretch_robot_unload_trailers_containers, 접근일 2026-09-29
```

### docs/categories/site-type-applications/warehouse.md

```markdown
---
title: "61. 물류창고"
type: area
category: "Q. 현장 유형별 적용"
area_no: 61
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 61. 물류창고

# 61. 물류창고

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

입고~반품 흐름의 로봇 작업. 기존 흐름 매트릭스와 영역 페이지의 물류 시나리오를 사례로 모은다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **물류창고 작업 흐름 적용**: 입고·적치·보충·피킹·포장·출하·반품 흐름에 로봇 작업을 대입해 시작 조건·작업 대상·수행 자원·제약·완료·예외를 정리한다

## 2. 핵심 질문

물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? [분류원문]

## 3. 왜 중요한가

아직 작성되지 않음

## 4. 핵심 개념과 용어

아직 작성되지 않음

## 5. 적용 사례 (현장 유형 명시)

아직 작성되지 않음

## 6. 대표 접근법과 기술

아직 작성되지 않음

## 7. 관련 표준·프레임워크·오픈소스

아직 작성되지 않음

## 8. 대표 연구와 자료

아직 작성되지 않음

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

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

### runs/2026-09-29-11/pages/topics/2026/2026-09-29-area61-s8.md

```markdown
---
title: "61. 물류창고 — 대표 연구와 자료"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 61
related_areas: [1, 17, 20, 22, 23, 25, 27, 31, 32, 35, 46, 49]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-005, ref-006, ref-910, ref-911, ref-382, ref-913, ref-101, ref-915, ref-916]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/warehouse.md#8
---

[홈](../../index.md) › [주제](../index.md) › 61. 물류창고 — 대표 연구와 자료

# 61. 물류창고 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아래 학술 서베이와 국내 논문은 이번 실행에서 초록만 확인했고 본문은 열지 않았다.
- 이 페이지는 [61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아래 학술 서베이와 국내 논문은 이번 실행에서 초록만 확인했고 본문은 열지 않았다.

- Azadeh, K., de Koster, R., & Roy, D., Robotized and Automated Warehouse Systems: Review and Recent Developments(Transportation Science 53(4), 2019) — 로봇화 창고 문헌을 시스템 분석·설계 최적화·운영 계획·제어의 세 갈래로 나누고 통합 로봇 창고가 다음 범주의 창고가 될 것이라고 본다. 이 영역의 기술 분류 기준이다. [사실][^ref-910]
- Boysen, N., Weidinger, F., & de Koster, R., Warehousing in the e-commerce era: A survey(European Journal of Operational Research 277(2), 2019) — 전자상거래 주문 특성에 맞춘 자동화 시스템과 조직적 적응을 정리한다. 시작 조건의 근거다. [사실][^ref-382]
- Fragapane, G., de Koster, R., Sgarbossa, F., & Strandhagen, J. O., Planning and control of autonomous mobile robots for intralogistics(European Journal of Operational Research 294(2), 2021) — AMR 의 분산 의사결정과 계획·제어 프레임워크, 창고·제조·크로스독·터미널·병원 적용 분야. [사실][^ref-911]
- Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks(AAMAS 2017) — MAPD 문제와 TP·TPTS 알고리즘. 온라인 작업 배정의 기본 문제 정의다. [사실][^ref-006]
- Li, J. 외, Lifelong Multi-Agent Path Finding in Large-Scale Warehouses(AAAI 2021) — RHCR 로 시뮬레이션 창고 기준 최대 1,000대의 지속형 경로 찾기를 푼다. 대규모 교통 관리의 규모 기준이다. [사실][^ref-005]
- Schrotenboer, A. H., Wruck, S., Vis, I. F. A., & Roodbergen, K. J., Integration of returns and decomposition of customer orders in e-commerce warehouses(arXiv, 2019) — 반품 재적치를 피커 경로에 통합하는 최적화(피커 기반 창고). [사실][^ref-913]
- Merschformann, M. 외, RAWSim-O(Logistics Research 11(1), 2018; GitHub README) — 로봇 이동형 풀필먼트 시스템용 이산 사건 시뮬레이터. [사실][^ref-101]
- 곽경민·박범·고은지·윤철주·김경훈(CJ대한통운), 급속 확산되는 물류현장의 로봇적용 사례(로봇학회 논문지 17(4), 2022) — 계약물류·소포·풀필먼트의 차이에 따른 국내 로봇 적용 유형. [사실][^ref-915]
- 김태현·송상화(인천대학교), 온라인 주문 풀필먼트를 위한 물류센터 피킹 설비 최적화에 대한 연구(한국디지털산업학회지 26(1), 2021) — 오더피킹 설비의 재고 보충 최적화. [사실][^ref-916]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [61. 물류창고](../../categories/site-type-applications/warehouse.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/warehouse.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. (AAAI 2021), Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2021-03-12, https://arxiv.org/abs/2005.07371, 접근일 2026-09-29
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. (AAMAS 2017), Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017-05-30, https://arxiv.org/abs/1705.10868, 접근일 2026-09-29
[^ref-910]: Azadeh, K., de Koster, R., & Roy, D. (Transportation Science 53(4)), Robotized and Automated Warehouse Systems: Review and Recent Developments, 2019-06-28, https://pubsonline.informs.org/doi/10.1287/trsc.2018.0873, 접근일 2026-09-29
[^ref-911]: Fragapane, G., de Koster, R., Sgarbossa, F., & Strandhagen, J. O. (European Journal of Operational Research 294(2)), Planning and control of autonomous mobile robots for intralogistics: Literature review and research agenda, 2021, https://doi.org/10.1016/j.ejor.2021.01.019, 접근일 2026-09-29
[^ref-382]: Boysen, N., Weidinger, F., & de Koster, R. (European Journal of Operational Research 277(2)), Warehousing in the e-commerce era: A survey, 2019, https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/, 접근일 2026-09-29
[^ref-913]: Schrotenboer, A. H., Wruck, S., Vis, I. F. A., & Roodbergen, K. J., Integration of returns and decomposition of customer orders in e-commerce warehouses, 2019-09-01, https://arxiv.org/abs/1909.01794, 접근일 2026-09-29
[^ref-101]: Merschformann, M. (RAWSim-O GitHub 공식 저장소), RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-09-29
[^ref-915]: 곽경민, 박범, 고은지, 윤철주, 김경훈 (CJ대한통운, 로봇학회 논문지 17(4)), 급속 확산되는 물류현장의 로봇적용 사례, 2022, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002899267, 접근일 2026-09-29
[^ref-916]: 김태현, 송상화 (인천대학교, 한국디지털산업학회지 26(1)), 온라인 주문 풀필먼트를 위한 물류센터 피킹 설비 최적화에 대한 연구, 2021, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002687327, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-11 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-11 | 61. 물류창고 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-29-11/pages/topics/2026/2026-09-29-area61-s6.md

````markdown
---
title: "61. 물류창고 — 대표 접근법과 기술"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 61
related_areas: [1, 17, 20, 22, 23, 25, 27, 31, 32, 35, 46, 49]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-005, ref-006, ref-910, ref-911, ref-382, ref-913, ref-915, ref-916, ref-917, ref-918, ref-919, ref-920, ref-921, ref-923, ref-924]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/warehouse.md#6
---

[홈](../../index.md) › [주제](../index.md) › 61. 물류창고 — 대표 접근법과 기술

# 61. 물류창고 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 확인한 자료를 종합하면 물류창고의 로봇 작업은 흐름 단계마다 다른 형태로 들어간다. [추정][^ref-910][^ref-382][^ref-913][^ref-915][^ref-916][^ref-917][^ref-919][^ref-920][^ref-921][^ref-923][^ref-924]
- 이 페이지는 [61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

확인한 자료를 종합하면 물류창고의 로봇 작업은 흐름 단계마다 다른 형태로 들어간다. [추정][^ref-910][^ref-382][^ref-913][^ref-915][^ref-916][^ref-917][^ref-919][^ref-920][^ref-921][^ref-923][^ref-924]

```mermaid
flowchart LR
    Inbound["입고: 트레일러 하역 로봇·고속 검수 스캐너"] --> Putaway["적치·보관: 로봇 이동형 풀필먼트 시스템·셔틀"]
    Putaway --> Replenish["보충: 보충 정보 생성·보충 최적화"]
    Replenish --> Pick["피킹: 상품-대-사람 스테이션·AMR 협업 피킹·로봇 낱개 피킹"]
    Pick --> Pack["포장: 이번 실행 사례 미확인"]
    Pack --> Ship["출하: 소팅봇·크로스벨트 소터·도크 배정"]
    Ship --> Return["반품: 재적치를 피킹 경로에 통합"]
    Forklift["무인지게차: 사람 출입 제한 구역의 대용량 운반"] -.-> Putaway
```

### 흐름 단계별 로봇 작업 지도

입고 단계는 트레일러 하역 로봇과 고속 검수 스캐너, 적치·보관·피킹 단계는 선반을 작업자에게 가져오는 로봇 이동형 풀필먼트 시스템과 셔틀·압축 저장 시스템, 그리고 사람과 함께 걷는 AMR 협업 피킹과 로봇 낱개 피킹, 보충 단계는 보충 정보 생성과 보충 최적화, 출하 단계는 소팅봇·크로스벨트 소터·도크 배정, 반품 단계는 재적치를 피킹 경로에 통합하는 최적화로 나타나며, 무인지게차는 사람 출입이 막힌 구역에서 대용량 운반을 맡는다. [추정][^ref-910][^ref-382][^ref-913][^ref-915][^ref-916][^ref-917][^ref-919][^ref-920][^ref-921][^ref-923][^ref-924] 곽경민 외(CJ대한통운, 2022)는 국내 물류 현장의 로봇 적용을 계약물류·소포·풀필먼트의 차이에 따라 논의하며 적용 유형으로 로봇 낱개 피킹, 로봇 박스 취급(디팔레타이징), AGV·AMR 이송, 자동창고(ASRS), 로봇 웨어러블 장치를 든다. [사실][^ref-915]

### 분산 의사결정을 하는 AMR 의 계획·제어

Fragapane 외(2021)는 AMR 이 중앙 장치가 스케줄링·라우팅·배차를 모두 맡는 AGV 시스템과 달리 다른 자원과 독립적으로 통신·협상해 의사결정을 분산할 수 있다고 보고, 제조·창고·크로스독·터미널·병원을 적용 분야로 들며 관리자를 위한 AMR 계획·제어 프레임워크와 연구 의제를 제시한다. [사실][^ref-911]

### 온라인 작업 배정과 대규모 경로 계획

Ma 외(AAMAS 2017)의 MAPD 문제는 온라인으로 도착하는 배송 작업 스트림을 픽업·배송 위치로 충돌 없이 처리하는 지속형 경로 계획 문제이며, 토큰 전달(TP)과 작업 교환 토큰 전달(TPTS) 알고리즘으로 수백 대의 에이전트·작업을 다룬다. [사실][^ref-006] Li 외(AAAI 2021)의 롤링 호라이즌 충돌 해결(RHCR)은 [지속형 다중 에이전트 경로 찾기](../../glossary/lifelong-mapf.md)를 시간창 단위의 순차 문제로 나눠, 시뮬레이션 창고 기준으로 최대 1,000대(지도 빈 칸의 38.9%)의 에이전트에 대해 높은 품질의 해를 낸다. [사실][^ref-005] Amazon 은 생성형 AI 기반 모델 DeepFleet 이 풀필먼트 네트워크 전체에서 로봇 플릿의 이동 시간을 10% 개선한다고 주장하나 측정 조건은 공개되지 않았다. [추정] 벤더 주장[^ref-918]

### 보충과 반품의 최적화

김태현·송상화(2021)는 온라인 주문 풀필먼트 센터의 오더피킹 설비에서 재고 보충을 최적화하는 혼합정수계획 모형을 개발해 실제 운영 프로세스·데이터와 시뮬레이션으로 효과를 검증했다. [사실][^ref-916] Schrotenboer 외(2019)는 전자상거래 창고에서 반품 상품의 재적치를 일반 주문 피커의 경로에 통합하면 비용이 10~15% 절감되고, 고객 주문을 여러 배치로 분해하는 것까지 허용하면 절감이 44%에 이른다고 보고했으며, 이는 피커 기반 창고의 최적화 연구로 로봇 피킹에 적용한 것은 아니다. [사실][^ref-913]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [61. 물류창고](../../categories/site-type-applications/warehouse.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/warehouse.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. (AAAI 2021), Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2021-03-12, https://arxiv.org/abs/2005.07371, 접근일 2026-09-29
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. (AAMAS 2017), Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017-05-30, https://arxiv.org/abs/1705.10868, 접근일 2026-09-29
[^ref-910]: Azadeh, K., de Koster, R., & Roy, D. (Transportation Science 53(4)), Robotized and Automated Warehouse Systems: Review and Recent Developments, 2019-06-28, https://pubsonline.informs.org/doi/10.1287/trsc.2018.0873, 접근일 2026-09-29
[^ref-911]: Fragapane, G., de Koster, R., Sgarbossa, F., & Strandhagen, J. O. (European Journal of Operational Research 294(2)), Planning and control of autonomous mobile robots for intralogistics: Literature review and research agenda, 2021, https://doi.org/10.1016/j.ejor.2021.01.019, 접근일 2026-09-29
[^ref-382]: Boysen, N., Weidinger, F., & de Koster, R. (European Journal of Operational Research 277(2)), Warehousing in the e-commerce era: A survey, 2019, https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/, 접근일 2026-09-29
[^ref-913]: Schrotenboer, A. H., Wruck, S., Vis, I. F. A., & Roodbergen, K. J., Integration of returns and decomposition of customer orders in e-commerce warehouses, 2019-09-01, https://arxiv.org/abs/1909.01794, 접근일 2026-09-29
[^ref-915]: 곽경민, 박범, 고은지, 윤철주, 김경훈 (CJ대한통운, 로봇학회 논문지 17(4)), 급속 확산되는 물류현장의 로봇적용 사례, 2022, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002899267, 접근일 2026-09-29
[^ref-916]: 김태현, 송상화 (인천대학교, 한국디지털산업학회지 26(1)), 온라인 주문 풀필먼트를 위한 물류센터 피킹 설비 최적화에 대한 연구, 2021, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002687327, 접근일 2026-09-29
[^ref-917]: 로봇신문 (장길수), CJ대한통운이 뽑은 물류자동화 혁신 기술 '톱3', 2022-05-06, https://www.irobotnews.com/news/articleView.html?idxno=28424, 접근일 2026-09-29
[^ref-918]: Amazon, Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot, 2025-07, https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model, 접근일 2026-09-29
[^ref-919]: 로봇신문 (장길수), 쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이..., 2023-02-07, https://www.irobotnews.com/news/articleView.html?idxno=30736, 접근일 2026-09-29
[^ref-920]: 물류신문 (석한글), ‘물류 투자만 6조’, 쿠팡 물류 인프라의 정점 ‘대구 FC’ 가보니, 2023-02-07, https://www.klnews.co.kr/news/articleView.html?idxno=306994, 접근일 2026-09-29
[^ref-921]: 스마트물류시설인증센터 (한국교통연구원), 인증스마트물류센터 : 인증심사 > 심사기준 > 일반, 미확인, https://cslc.koti.re.kr/new_sub2/new_sub2_2_1, 접근일 2026-09-29
[^ref-923]: CJ대한통운, CJ대한통운 안성 MP허브, 국토부 ‘스마트물류센터 1등급’ 인증, 2023-10-26, https://cjlogistics.com/ko/newsroom/news/NR_00001109, 접근일 2026-09-29
[^ref-924]: Robotics 24/7 (Eugene Demaitre), DHL Makes First Commercial Deployment of Boston Dynamics Stretch Robot to Unload Trailers and Containers, 2023-02-01, https://www.robotics247.com/article/dhl_makes_first_commercial_deployment_boston_dynamics_stretch_robot_unload_trailers_containers, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-11 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-11 | 61. 물류창고 의 "대표 접근법과 기술" 절에서 분리 |
````

### runs/2026-09-29-11/pages/topics/2026/2026-09-29-area61-s4.md

```markdown
---
title: "61. 물류창고 — 핵심 개념과 용어"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 61
related_areas: [1, 17, 20, 22, 23, 25, 27, 31, 32, 35, 46, 49]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-006, ref-910, ref-382, ref-917, ref-919, ref-921, ref-124]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/warehouse.md#4
---

[홈](../../index.md) › [주제](../index.md) › 61. 물류창고 — 핵심 개념과 용어

# 61. 물류창고 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **상품-대-사람(Goods-to-Person, GTP)** — 로봇이나 설비가 선반·토트를 작업자 스테이션으로 가져와 작업자는 제자리에서 피킹하는 방식으로, 작업자가 선반까지 걸어가는 사람-대-상품(Person-to-Goods, PTG) 방식과 대비된다. 쿠팡 대구 풀필먼트센터는 PTG 에서 GTP 로 전환했다. [사실][^ref-919]
- 이 페이지는 [61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **상품-대-사람(Goods-to-Person, GTP)** — 로봇이나 설비가 선반·토트를 작업자 스테이션으로 가져와 작업자는 제자리에서 피킹하는 방식으로, 작업자가 선반까지 걸어가는 사람-대-상품(Person-to-Goods, PTG) 방식과 대비된다. 쿠팡 대구 풀필먼트센터는 PTG 에서 GTP 로 전환했다. [사실][^ref-919]
- **[로봇 이동형 풀필먼트 시스템(RMFS)](../../glossary/robotic-mobile-fulfillment-system.md)** — 이동 로봇이 선반(pod)을 작업자에게 가져오는 GTP 의 대표 구현으로, 로봇화 창고 서베이가 셔틀 기반 시스템과 함께 새 범주로 검토한다. [사실][^ref-910]
- **셔틀 기반 저장·회수 시스템(Shuttle-Based Storage and Retrieval System, SBS/RS)** — 층마다 움직이는 셔틀 차량과 리프트로 토트·상자를 랙에 넣고 꺼내는 자동 창고 시스템으로, 같은 서베이가 셔틀 기반 압축 저장 시스템과 함께 검토한다. [사실][^ref-910]
- **AMR 협업 피킹(AMR-assisted Order Picking)** — 자율이동로봇(Autonomous Mobile Robot, AMR)이 피킹 경로를 따라 작업자와 함께 움직이며 상품을 싣고 나르고 작업자는 집는 일만 맡는 방식으로, 전자상거래 창고 서베이가 AGV 지원 피킹을 자동화 선택지의 하나로 든다. [사실][^ref-382] CJ대한통운은 AMR 기반 오더피킹에서 작업자 1명이 시간당 120 오더라인을 처리한다고 설명한다. [추정] 벤더 주장[^ref-917]
- **[다중 에이전트 픽업·배송(Multi-Agent Pickup and Delivery, MAPD)](../../glossary/multi-agent-pickup-and-delivery.md)** — 자동화 창고에서 온라인으로 도착하는 배송 작업 스트림을 픽업 위치와 배송 위치로 충돌 없이 계속 처리하는 지속형 경로 계획 문제다. [사실][^ref-006]
- **[창고 관리 시스템(WMS)·창고 제어 시스템(WCS)](../../glossary/wes-wcs-wms-mes-tms.md)** — 국내 스마트물류센터 인증 심사기준은 정보시스템 200점을 WMS(Warehouse Management System) 150점과 WCS/MCS 50점으로 나눈다. [사실][^ref-921]
- **스마트물류센터 인증(Smart Logistics Center Certification)** — 물류시설의 개발 및 운영에 관한 법률 제21조의4에 근거해 국토교통부가 첨단·자동화 설비를 갖춘 물류창고를 1~5등급으로 인증하는 제도로, 하차·입고부터 상차·출고까지 6개 프로세스의 기능영역과 구조·성과·정보시스템의 기반영역을 심사한다. [사실][^ref-124][^ref-921]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [61. 물류창고](../../categories/site-type-applications/warehouse.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/warehouse.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. (AAMAS 2017), Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017-05-30, https://arxiv.org/abs/1705.10868, 접근일 2026-09-29
[^ref-910]: Azadeh, K., de Koster, R., & Roy, D. (Transportation Science 53(4)), Robotized and Automated Warehouse Systems: Review and Recent Developments, 2019-06-28, https://pubsonline.informs.org/doi/10.1287/trsc.2018.0873, 접근일 2026-09-29
[^ref-382]: Boysen, N., Weidinger, F., & de Koster, R. (European Journal of Operational Research 277(2)), Warehousing in the e-commerce era: A survey, 2019, https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/, 접근일 2026-09-29
[^ref-917]: 로봇신문 (장길수), CJ대한통운이 뽑은 물류자동화 혁신 기술 '톱3', 2022-05-06, https://www.irobotnews.com/news/articleView.html?idxno=28424, 접근일 2026-09-29
[^ref-919]: 로봇신문 (장길수), 쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이..., 2023-02-07, https://www.irobotnews.com/news/articleView.html?idxno=30736, 접근일 2026-09-29
[^ref-921]: 스마트물류시설인증센터 (한국교통연구원), 인증스마트물류센터 : 인증심사 > 심사기준 > 일반, 미확인, https://cslc.koti.re.kr/new_sub2/new_sub2_2_1, 접근일 2026-09-29
[^ref-124]: 국토교통부 (국가물류통합정보센터), 스마트물류센터 인증제 안내, 미확인, https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-11 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-11 | 61. 물류창고 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-29-11/pages/topics/2026/2026-09-29-area61-s11.md

```markdown
---
title: "61. 물류창고 — 열린 질문"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 61
related_areas: [1, 17, 20, 22, 23, 25, 27, 31, 32, 35, 46, 49]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: []
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/warehouse.md#11
---

[홈](../../index.md) › [주제](../index.md) › 61. 물류창고 — 열린 질문

# 61. 물류창고 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 기존 열린 질문(상태 변경 없음. 전체 목록: [열린 질문](../../open-questions.md)):
- 이 페이지는 [61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

기존 열린 질문(상태 변경 없음. 전체 목록: [열린 질문](../../open-questions.md)):

- **oq-134** (상태: 열림) 국내 물류창고·병원에서 로봇 운영 기록으로 혼잡·고장·승강기 대기 같은 실제 상황을 시뮬레이션에 재현한 사례가 있는가? — 이번 조사에서도 국내 물류창고 자료 미확인.
- **oq-138** (상태: 열림) 국내 물류창고·병원·제조 공장에서 대화로 로봇 작업 시나리오를 구성한 사례가 있는가? — 이번 조사에서도 국내 물류창고 자료 미확인.
- **oq-142** (상태: 열림) 국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가? — 이번 조사에서도 국내 물류창고 자료 미확인.
- **oq-146** (상태: 열림) 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가? — 이번 조사에서도 국내 물류창고 자료 미확인.

이번 실행에서 새로 올리는 질문(id 는 퍼블리셔가 부여):

- (신규 · 관련 영역: 61. 물류창고, 20. 로봇·제조사 관제 연동) 국내 물류센터에서 서로 다른 제조사의 AGV·소팅봇·무인지게차·하역 로봇을 하나의 오케스트레이션 계층으로 관제한 공개 사례가 있는가(쿠팡 대구·CJ대한통운 사례는 설비별 도입만 확인됐다)?
- (신규 · 관련 영역: 61. 물류창고, 23. 업무 시스템 연동) 스마트물류센터 인증 심사기준의 정보시스템 항목(WMS 150점, WCS/MCS 50점)에서 이기종 로봇 오케스트레이션 계층은 어느 항목으로 평가되며 인증 심사가 로봇 플릿 관제 기능을 따로 보는가?
- (신규 · 관련 영역: 61. 물류창고, 25. 작업 배정 — MRTA) 반품 재적치를 피킹 경로에 통합하는 최적화 연구를 로봇 이동형 풀필먼트 시스템이나 AMR 협업 피킹에 적용한 연구·사례가 있는가?
- (신규 · 관련 영역: 61. 물류창고, 32. 예외 복구·재계획·업무 연속성) 트레일러 하역 로봇의 떨어진 상자 복구 같은 예외 처리가 로봇 자체 복구와 오케스트레이션 계층의 재계획 사이에서 어떻게 분담되는지 공개된 인터페이스나 사례가 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [61. 물류창고](../../categories/site-type-applications/warehouse.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/warehouse.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-11 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-11 | 61. 물류창고 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-29-11/pages/topics/2026/2026-09-29-area61-s7.md

```markdown
---
title: "61. 물류창고 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 61
related_areas: [1, 17, 20, 22, 23, 25, 27, 31, 32, 35, 46, 49]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-003, ref-004, ref-101, ref-921, ref-124]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/warehouse.md#7
---

[홈](../../index.md) › [주제](../index.md) › 61. 물류창고 — 관련 표준·프레임워크·오픈소스

# 61. 물류창고 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| 스마트물류센터 인증 심사기준(일반) | 평가 프로그램 | 기능영역 600점을 하차·입고, 운반·적치, 보관·재고관리, 피킹·분류, 검품·검수·포장, 상차·출고의 6개 프로세스 각 100점으로 나누고, 기반영역 400점을 구조적 성능 100점·성과관리 100점·정보시스템 200점(WMS 150점, WCS/MCS 50점)으로 두며, 우수물류신기술 적용 가산점은 최대 50점이다. 이 6개 프로세스가 물류창고 흐름 단계의 국내 기준 구분이다. | [사실][^ref-921] |
| 스마트물류센터 인증제(법적 근거·혜택) | 평가 프로그램 | 물류시설의 개발 및 운영에 관한 법률 제21조의4에 근거해 첨단·자동화 설비를 갖춘 물류창고를 1~5등급으로 인증한다. 스마트물류시설인증센터 인증혜택·법적근거 안내 기준으로 인증을 받으면 건축·설비 구입 비용을 저리로 융자받고 정부가 최대 2%p 의 이자 비용을 지원하며 용적률·높이 제한이 완화되고, 시행령은 2020-10-08 개정돼 2021-01-01 시행됐다. | [사실][^ref-124][^ref-921] |
| [GS1 EPCIS](../../glossary/epcis.md) | 표준 | 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다(원문 미열람). 입고·출하 단계의 완료·인계 기록을 로봇 작업 결과와 함께 남기는 후보 형식으로 본다. | [사실][^ref-003] 후보 형식 부분은 [추정][^ref-003] |
| [Open-RMF](../../glossary/open-rmf.md) | 오픈소스 | 플릿 어댑터로 제조사가 다른 로봇 플릿을 붙이고 작업·교통 조율과 문·승강기 같은 설비 연동을 제공하는 미들웨어로, AGV·AMR·소팅 로봇처럼 제조사가 다른 플릿을 하나의 오케스트레이션 계층으로 묶는 참고 구조가 될 것으로 보인다. | [추정][^ref-004] |
| RAWSim-O | 오픈소스 | 로봇 이동형 풀필먼트 시스템의 의사결정 문제를 연구하는 이산 사건 시뮬레이션 프레임워크(GNU GPL v3 이상)로, 2D·3D 시각화, 다층 창고 시뮬레이션, 경로 계획 시각화, 로봇 이동 히트맵을 갖추고 새 의사결정 방법을 컨트롤러로 확장할 수 있다. 대표 논문은 Logistics Research 11(1)(2018)이다. | [사실][^ref-101] |

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [61. 물류창고](../../categories/site-type-applications/warehouse.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/warehouse.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-29 (원문 미열람)
[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-29
[^ref-101]: Merschformann, M. (RAWSim-O GitHub 공식 저장소), RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-09-29
[^ref-921]: 스마트물류시설인증센터 (한국교통연구원), 인증스마트물류센터 : 인증심사 > 심사기준 > 일반, 미확인, https://cslc.koti.re.kr/new_sub2/new_sub2_2_1, 접근일 2026-09-29
[^ref-124]: 국토교통부 (국가물류통합정보센터), 스마트물류센터 인증제 안내, 미확인, https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-11 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-11 | 61. 물류창고 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-29-11/pages/topics/2026/2026-09-29-area61-s10.md

```markdown
---
title: "61. 물류창고 — 다른 연구영역과의 연결"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 61
related_areas: [1, 17, 20, 22, 23, 25, 27, 31, 32, 35, 46, 49]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-003, ref-004, ref-005, ref-006, ref-257, ref-910, ref-382, ref-101, ref-918, ref-919, ref-920, ref-921, ref-923, ref-924]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/warehouse.md#10
---

[홈](../../index.md) › [주제](../index.md) › 61. 물류창고 — 다른 연구영역과의 연결

# 61. 물류창고 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md) — Amazon 의 로봇 100만 대 배치와 다중 플릿 오케스트레이션 소프트웨어의 시장 정의는 이 현장의 시장 동향 근거다. [추정][^ref-918][^ref-257]
- 이 페이지는 [61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md) — Amazon 의 로봇 100만 대 배치와 다중 플릿 오케스트레이션 소프트웨어의 시장 정의는 이 현장의 시장 동향 근거다. [추정][^ref-918][^ref-257]
- [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) — 입고·출하 단계의 바코드 인식·검수와 인계 이벤트 기록(GS1 EPCIS)이 여기에 속한다. [추정][^ref-003][^ref-921]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 제조사 플릿 매니저를 관리하는 고수준 제어와 플릿 어댑터가 이 현장의 이기종 플릿 연동 방식이다. [추정][^ref-257][^ref-004]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 크로스벨트 소터·컨베이어·도크 관리 시스템과의 연동이 출하 단계의 설비 연동이다. [추정][^ref-923]
- [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) — WMS·WCS/MCS 연동과 인증 심사기준의 정보시스템 배점이 여기에 이어진다. [추정][^ref-921]
- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 온라인 픽업·배송 작업 배정이 이 영역의 배정 문제다. [추정][^ref-006]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 시뮬레이션 창고 기준 최대 1,000대의 지속형 경로 계획이 대규모 교통 관리의 규모 기준이다. [추정][^ref-005]
- [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — AMR 협업 피킹과 상품-대-사람 스테이션의 작업자 협업이 여기에 속한다. [추정][^ref-382]
- [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 하역 로봇의 떨어진 상자 복구 같은 예외가 여기에 이어진다. [추정][^ref-924]
- [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md) — 로봇 창고의 설계 최적화와 RAWSim-O 같은 설계 연구용 시뮬레이터가 여기에 속한다. [추정][^ref-910][^ref-101]
- [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) — DeepFleet 같은 학습 기반 플릿 조율은 이 영역의 방법이며 벤더 주장으로만 확인된다. [추정] 벤더 주장[^ref-918]
- [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) — 무인지게차의 구역 분리와 경계 침범 시 정지가 사람 근접 안전의 사례다. [추정][^ref-919][^ref-920]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [61. 물류창고](../../categories/site-type-applications/warehouse.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/warehouse.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-29 (원문 미열람)
[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-29
[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. (AAAI 2021), Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2021-03-12, https://arxiv.org/abs/2005.07371, 접근일 2026-09-29
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. (AAMAS 2017), Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017-05-30, https://arxiv.org/abs/1705.10868, 접근일 2026-09-29
[^ref-257]: Interact Analysis (Rueben Scriven), AMR Multi-Fleet Orchestration Software Explained, 2023-01, https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/, 접근일 2026-09-29 (원문 미열람)
[^ref-910]: Azadeh, K., de Koster, R., & Roy, D. (Transportation Science 53(4)), Robotized and Automated Warehouse Systems: Review and Recent Developments, 2019-06-28, https://pubsonline.informs.org/doi/10.1287/trsc.2018.0873, 접근일 2026-09-29
[^ref-382]: Boysen, N., Weidinger, F., & de Koster, R. (European Journal of Operational Research 277(2)), Warehousing in the e-commerce era: A survey, 2019, https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/, 접근일 2026-09-29
[^ref-101]: Merschformann, M. (RAWSim-O GitHub 공식 저장소), RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-09-29
[^ref-918]: Amazon, Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot, 2025-07, https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model, 접근일 2026-09-29
[^ref-919]: 로봇신문 (장길수), 쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이..., 2023-02-07, https://www.irobotnews.com/news/articleView.html?idxno=30736, 접근일 2026-09-29
[^ref-920]: 물류신문 (석한글), ‘물류 투자만 6조’, 쿠팡 물류 인프라의 정점 ‘대구 FC’ 가보니, 2023-02-07, https://www.klnews.co.kr/news/articleView.html?idxno=306994, 접근일 2026-09-29
[^ref-921]: 스마트물류시설인증센터 (한국교통연구원), 인증스마트물류센터 : 인증심사 > 심사기준 > 일반, 미확인, https://cslc.koti.re.kr/new_sub2/new_sub2_2_1, 접근일 2026-09-29
[^ref-923]: CJ대한통운, CJ대한통운 안성 MP허브, 국토부 ‘스마트물류센터 1등급’ 인증, 2023-10-26, https://cjlogistics.com/ko/newsroom/news/NR_00001109, 접근일 2026-09-29
[^ref-924]: Robotics 24/7 (Eugene Demaitre), DHL Makes First Commercial Deployment of Boston Dynamics Stretch Robot to Unload Trailers and Containers, 2023-02-01, https://www.robotics247.com/article/dhl_makes_first_commercial_deployment_boston_dynamics_stretch_robot_unload_trailers_containers, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-11 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-11 | 61. 물류창고 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-29-11/pages/topics/2026/2026-09-29-area61-s3.md

```markdown
---
title: "61. 물류창고 — 왜 중요한가"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 61
related_areas: [1, 17, 20, 22, 23, 25, 27, 31, 32, 35, 46, 49]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-257, ref-910, ref-382, ref-919, ref-920]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/warehouse.md#3
---

[홈](../../index.md) › [주제](../index.md) › 61. 물류창고 — 왜 중요한가

# 61. 물류창고 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 물류창고는 로봇 취급 시스템이 빠르게 늘고 있는 현장이며, 로봇이 들어오면 창고 설계·계획·제어 논리 전반을 다시 세워야 한다. [사실][^ref-910]
- 이 페이지는 [61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[61. 물류창고](../../categories/site-type-applications/warehouse.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

물류창고는 로봇 취급 시스템이 빠르게 늘고 있는 현장이며, 로봇이 들어오면 창고 설계·계획·제어 논리 전반을 다시 세워야 한다. [사실][^ref-910] Azadeh·de Koster·Roy(2019)의 서베이는 배송센터에 로봇 취급 시스템이 늘어나는 이유로 작은 공간, 수요 변동 대응 유연성, 24시간 가동을 들고, 셔틀 기반 저장·회수 시스템, 셔틀 기반 압축 저장 시스템, 로봇 이동형 풀필먼트 시스템(Robotic Mobile Fulfillment System, RMFS)을 새 범주로 검토하며, 실제 사용에 비해 학술 연구가 적은 로봇 시스템이 많다고 지적한다. [사실][^ref-910]

이 현장에서 로봇 작업을 부르는 것은 전자상거래 주문의 특성이다. Boysen·Weidinger·de Koster(2019)는 소량·소수 라인의 시간 민감 피킹 주문이 대량으로 발생하는 조건에서 전통적 피커-대-상품 창고가 부족해, 자동 피킹 워크스테이션·로봇·AGV 지원 피킹 같은 자동화 시스템과 혼합 선반 저장·동적 주문 처리·배치·존 분할·분류 같은 조직적 적응이 채택된다고 정리한다. [사실][^ref-382]

ROP 에게 물류창고가 중요한 이유는 이 현장이 서로 다른 제조사의 AMR 플릿 여럿을 하나의 창고 시스템 안에서 관리하는 다중 플릿 오케스트레이션 소프트웨어의 기본 현장으로 놓이기 때문이다. [사실][^ref-257] Interact Analysis(2023-01)는 이 소프트웨어를 고정 자동화의 창고 제어 시스템에 비견하고, 로봇을 직접 통합하는 저수준 제어와 제조사 플릿 매니저를 관리하는 고수준 제어로 접근을 나누며, 상호운용은 표준 또는 미들웨어로 푼다고 정리한다. [사실][^ref-257] 5절의 사례가 보여 주듯 국내 대형 센터도 층별로 서로 다른 로봇을 두고 있어, 이들을 한 계층에서 묶는 문제가 이 영역의 핵심이다. [추정][^ref-919][^ref-920]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/warehouse.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [61. 물류창고](../../categories/site-type-applications/warehouse.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/warehouse.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-257]: Interact Analysis (Rueben Scriven), AMR Multi-Fleet Orchestration Software Explained, 2023-01, https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/, 접근일 2026-09-29 (원문 미열람)
[^ref-910]: Azadeh, K., de Koster, R., & Roy, D. (Transportation Science 53(4)), Robotized and Automated Warehouse Systems: Review and Recent Developments, 2019-06-28, https://pubsonline.informs.org/doi/10.1287/trsc.2018.0873, 접근일 2026-09-29
[^ref-382]: Boysen, N., Weidinger, F., & de Koster, R. (European Journal of Operational Research 277(2)), Warehousing in the e-commerce era: A survey, 2019, https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/, 접근일 2026-09-29
[^ref-919]: 로봇신문 (장길수), 쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이..., 2023-02-07, https://www.irobotnews.com/news/articleView.html?idxno=30736, 접근일 2026-09-29
[^ref-920]: 물류신문 (석한글), ‘물류 투자만 6조’, 쿠팡 물류 인프라의 정점 ‘대구 FC’ 가보니, 2023-02-07, https://www.klnews.co.kr/news/articleView.html?idxno=306994, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-11 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-11 | 61. 물류창고 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 909건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 243개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- attribute-based-access-control: 속성 기반 접근 통제 (Attribute-Based Access Control (ABAC))
- audit-trail: 감사 추적 (Audit Trail)
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
- business-continuity-management-system: 업무 연속성 관리 시스템 (Business Continuity Management System (BCMS))
- business-location: 업무 위치 (Business Location (EPCIS bizLocation))
- cap-theorem: CAP 정리 (CAP Theorem)
- capabilities-skills-services: 능력·스킬·서비스 모델 (Capabilities, Skills and Services (CSS) Model)
- capability-based-task-allocation: 능력 기반 작업 배정 (Capability-based Task Allocation)
- capability-description-submodel: 능력 기술 서브모델 (Capability Description Submodel (IDTA 02020))
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- clarification-question: 명확화 질문 (Clarification Question (Follow-up Clarification))
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
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- constrained-decoding: 제약 디코딩 (Constrained Decoding)
- contrastive-explanation: 대조적 설명 (Contrastive Explanation)
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD))
- costmap: 비용 지도 (Costmap)
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- digital-nameplate: 디지털 명판 (Digital Nameplate (IDTA 02006))
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- eclass: ECLASS (ECLASS)
- edit-cost: 편집 비용 (Edit Cost)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
- failure-explanation: 실패 설명 (Failure Explanation)
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- filter-mask: 필터 마스크 (Filter Mask (Nav2 costmap filter))
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- frozen-horizon: 동결 구간 (Frozen Horizon (Frozen Zone))
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- goal-condition: 목표 조건 (Goal Condition)
- grade-certainty-of-evidence: 근거 확실성 등급 (GRADE (Grading of Recommendations, Assessment, Development and Evaluation))
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- graph-edit-distance: 그래프 편집 거리 (Graph Edit Distance (GED))
- hallucination: 환각 (Hallucination)
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- industrial-data: 산업데이터 (Industrial Data)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
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
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mission-specification-pattern: 미션 명세 패턴 (Mission Specification Pattern)
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robot-as-a-service: 서비스형 로봇 (Robot-as-a-Service (RaaS))
- robot-density: 로봇 밀도 (Robot Density)
- robot-task-fitness-matrix: 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scan-vs-bim: 스캔 대 BIM 비교 (Scan-vs-BIM)
- scenario-reconstruction: 시나리오 재구성 (Scenario Reconstruction)
- schedule-stability: 일정 안정성 (Schedule Stability)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [61] 에 걸린 4건 / 전체 162건)

```markdown
- oq-134 [열림] 국내 물류창고·병원에서 로봇 운영 기록으로 혼잡·고장·승강기 대기 같은 실제 상황을 시뮬레이션에 재현한 사례가 있는가(이번 조사에서 확인된 국내 자료는 설계 검증·모니터링용 디지털 트윈과 시나리오 기반 검증뿐이다)? (영역 11, 61, 63)
- oq-138 [열림] 국내 물류창고·병원·제조 공장에서 대화로 로봇 작업 시나리오를 구성한 사례가 있는가(이번 조사에서 확인된 국내 자료는 자연어 로봇 제어 동향 논문뿐이다)? (영역 9, 61, 63)
- oq-142 [열림] 국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 ETRI 동향 논문뿐이다)? (영역 12, 61, 63, 62)
- oq-146 [열림] 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가(이번 조사에서 확인된 현장 사례는 네덜란드 슈퍼마켓 연구뿐이다)? (영역 13, 60, 61)
```
