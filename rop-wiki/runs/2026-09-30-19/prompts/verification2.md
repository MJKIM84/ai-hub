(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-19
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 3. 경제성·조달·사업 모델 (A. 기획·사업)
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

### runs/2026-09-30-19/target.json

```json
{
  "run_id": "2026-09-30-19",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 128,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 3,
    "area_name": "3. 경제성·조달·사업 모델",
    "category": "A. 기획·사업",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=3"
}
```

### runs/2026-09-30-19/research.json

```json
{
  "run_id": "2026-09-30-19",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 3,
    "area_name": "3. 경제성·조달·사업 모델",
    "category": "A. 기획·사업"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 총소유비용(TCO)·수명주기 비용·투자 회수 기간·사용량 기반 과금·서비스형 로봇 계약 구조 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고·제조 공장·병원·상업 시설의 도입 효과·과금·조달 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 투자 판단 기준, 수명주기 비용 분석, 다기준 선정, 과금 모델, 공공 실증·조달 방식 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — IEC 60300-3-3, VDA 5050 목적, Open-RMF 라이선스, 국내 지원·조달 제도 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-129, oq-160, oq-162 반영 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "도입 비용을 넘는 효과가 나오며, 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가? [분류원문]",
    "로봇 도입의 투자 판단에 쓰는 기준(투자수익률·회수 기간·총소유비용)과 비용 항목·분석 방법(수명주기 비용 표준 등)은 무엇인가? (섹션 4·6·7 겨냥)",
    "서비스형 로봇(RaaS)·구독·작업당 과금 같은 사업 모델은 어떻게 구성되고, 과금 근거가 되는 사용량은 무엇으로 재는가? (섹션 4·6·9 겨냥)",
    "로봇·플랫폼 선정과 조달은 어떤 방법(다기준 의사결정, 시범 실증, 공공 조달)과 조건(개방 인터페이스, 인증 통합자)으로 이루어지는가? (섹션 5·6·7 겨냥, 한국 제도 우선)",
    "물류창고·제조 공장·병원·상업 시설 등 현장 유형별로 도입 효과와 비용을 정량 보고한 사례는 무엇이며 근거 수준은 어떤가? (섹션 3·5·8 겨냥)",
    "국내 로봇산업 통계는 관제·오케스트레이션 소프트웨어와 서비스형 로봇 매출을 따로 집계하는가, 시장 규모 자료의 산정 방법은 공개되어 있는가? (oq-162, oq-160, 섹션 8·11 겨냥)",
    "경제성·조달·사업 모델에서 ROP가 직접 맡을 것과 재무·구매·업무 시스템에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (oq-129 포함, 섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Modern Materials Handling 의 2026 사내 물류 로봇 설문(응답 166명, 2026-03~04)에서 로봇 투자 결정 요인은 투자수익률(ROI) 63%, 회수 기간 52%, 총소유비용(TCO) 47%, 공정 성과 41% 순이었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1299"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Peerless Research Group·MHI 등과 한 설문. 응답자 166명(제조 29%, 운송·창고 21%, 도매 14%, 소매 12%). 결정 요인 ROI 63%, payback time 52%, TCO 47%, process performance 41%.",
      "as_of": "2026-06-01",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f2",
      "claim": "같은 설문에서 로봇 도입 방식은 하드웨어 구매와 소프트웨어 구독을 섞은 하이브리드 53%, 전액 자본 지출 구매 37%, 서비스형 로봇(RaaS) 11%였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1299"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "도입 방식: hybrid(하드웨어 구매 + 소프트웨어 구독) 53%, full CapEx 37%, RaaS 11%. 표본 166명, 방법론 세부는 기사 수준으로만 공개.",
      "as_of": "2026-06-01",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f3",
      "claim": "같은 설문에서 로봇 투자가 사업 목표를 달성했다는 응답은 74%였고, 11%는 투자수익률·신뢰성·통합 비용 관련 목표에 못 미쳤다고 답했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1299"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "74% met business goals; 94% 가 가동 속도 기대 충족·초과; 11% 가 ROI, reliability, integration costs 목표 미달.",
      "as_of": "2026-06-01",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f4",
      "claim": "NIST GCR 24-054 보고서는 로봇 도입의 가장 큰 과제로 투자수익률을 찾고 달성하는 일을 들고, 서비스형 로봇으로 초기 투자와 위험을 줄이는 방식이 매력적이라고 서술한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1285"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "검색 요약 기준: 'top challenge to pursuing robotics was identifying and achieving ROI', RaaS 로 장비 지출과 위험을 줄이는 것이 매력적이라는 서술. 이전 MMH 설문의 ROI 70%·회수 기간 64%·TCO 60% 인용. PDF 본문 추출 실패.",
      "as_of": "2024",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f5",
      "claim": "IEC 60300-3-3:2017(신뢰성 관리 — 적용 지침 — 수명주기 비용, 3판)은 수명주기 비용(LCC) 개념과 적용을 안내하며 특히 품목의 신뢰성(dependability)과 관련된 비용을 강조하는 국제 표준이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1296"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IEC 웹스토어 개요: 3.0판 2017-01-27 발행. 'particularly highlights the costs associated with the dependability of an item.' 경영자·엔지니어·재무·계약자 대상. 표준 본문은 유료라 미열람.",
      "as_of": "2017-01-27",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f6",
      "claim": "Buerkle 외(Robotics and Computer-Integrated Manufacturing 81, 2023)는 산업용 로봇 서비스(IRaaS)를 유연성·사용성·안전·사업 모델(시간 기반·사용량 기반) 네 요소로 제안하고, 중소기업의 로봇 도입 장벽으로 큰 초기 투자, 총소유비용의 불확실성, 전문성 부족을 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-1286"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약 기준: IRaaS 네 요소 Flexibility·Usability·Safety·Business Models(Time-based, Usage-based). 장벽: large initial investment, TCO 불확실성, lack of expertise. 원문 403.",
      "as_of": "2023-06",
      "site_type": "제조 공장",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f7",
      "claim": "Lee·Aswani(2025, arXiv)는 서비스형 로봇 제공자가 작업마다 가격을 제시하고 고객이 수락·거절하며 로봇이 작업 후 확률적으로 열화하는 상황에서, 가격 결정과 로봇 교체 결정을 함께 최적화하는 마르코프 결정 과정 모델을 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1287"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 'jobs arrive sequentially, and for each, the provider must decide on a price, which the customer can accept or reject.' 데이터 기반 수요 추정 + MDP 로 가격·교체 정책 산출.",
      "as_of": "2025-09-30",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f8",
      "claim": "물류창고 사례(벤더 주장): AutoStore 의 피킹량 기반 서비스형 로봇 모델은 알루미늄 저장 그리드를 고객이 먼저 사고, 로봇·포트(작업대)·소프트웨어는 피킹량에 따라 월 요금을 내는 구독으로 쓰게 하며, 보통 3~5년 최소 계약과 가동 로봇·포트 수에 따른 월 최소 요금을 둔다.",
      "tag": "추정",
      "source_ids": [
        "ref-1292"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 그리드는 전체 시스템 비용의 약 20~40%로 선구매, 로봇·포트·소프트웨어는 피킹량 기반 월 과금, 최소 계약 3~5년. 'This volume-based pricing approach makes robotics more accessible' (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "물류창고",
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f9",
      "claim": "상업 시설 사례(한국): 지디넷코리아(2023-03)는 식당 서빙로봇 렌털 요금이 월 30만원대로 월 최저임금 수준 인건비 200만원대와 비교되며, 브이디컴퍼니(월 29만9천원 상품)·비로보틱스(3년 사용 후 소유권 결정하는 유예형)·알지티 등이 렌털 상품을 내놓았다고 보도했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1293"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기사: '월 요금을 30만원대 수준으로 낮췄다'. 구매·렌털 선택형, 유예형은 3년 사용 후 소유권 결정, 12개월 무상 수리. 인건비 절감 효과 수치는 업체·기사 주장 수준.",
      "as_of": "2023-03",
      "site_type": "상업 시설",
      "flow_item": "수행 자원"
    },
    {
      "id": "f10",
      "claim": "병원 사례: Li 외(Scientific Reports 16, 2026-04)는 중국 3차 병원의 약품·검체 배송에 자율이동로봇 10대를 6개월 병행 대조로 평가해, 배송 시간이 수작업 대비 32~36% 줄고 인력 19명보다 7.3배 많은 배송을 했으며 10년 수명주기 동안 692.8만 위안 절감을 추정했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1290"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 기준: 단일 기관 병행 대조, 10대 AMR, 배송 시간 32~36% 단축(p<0.001), 7.3배 배송 횟수, 10년 절감 6.928 million RMB, 민감도 분석으로 경제성 확인. 비용 항목·할인율은 본문 미확인.",
      "as_of": "2026-04",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f11",
      "claim": "병원 사례(싱가포르): 창이종합병원의 CHART 는 RoMi-H(의료 로봇 미들웨어) 통합을 맡을 시스템 통합자를 연 2회 등재 프로그램으로 평가·인증하며, 공공 의료기관은 로봇·소프트웨어·IoT 연동에 등재된 통합자를 쓰게 되어 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-872"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "CHART 운영, 연 2회, 기술 역량·배포 지식 평가, 2025-05-01 시행. 'Integration to RoMi-H facilitates interoperability of diverse systems and devices.'",
      "as_of": "2025-05",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f12",
      "claim": "한국로봇산업진흥원의 서비스로봇 실증사업(2020년부터)은 물류·웨어러블·의료·협동로봇·언택트 서비스 분야에 로봇 도입 비용의 50% 이내를 국비로 지원하고 민간 부담 50% 이상(수요기관 25% 이상)을 요구하며, 서류·발표·현장 평가로 과제를 뽑고 중간 점검과 최종 평가를 거친다.",
      "tag": "사실",
      "source_ids": [
        "ref-947"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "사업 안내 페이지: '로봇 도입 비용 50% 이내 국비 지원', 민간부담금 총사업비 50% 이상(현금), 수요기관 25% 이상. 절차: 공모→서류→발표→현장→최종평가→협약→중간점검→최종평가.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f13",
      "claim": "연계 대상: 조달청의 2026년 혁신제품 시범구매 기본계획은 예산을 전년 529억원에서 839억원으로 늘리고 로봇·드론·스마트팩토리 같은 AI 융복합 제품을 중점으로 하며, 조달청이 혁신제품을 사서 공공기관에 제공한 뒤 시범 사용 후 관리·활용 여부를 점검하는 방식이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1295"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "전자신문 2025-12-18: 예산 529억→839억원, AI 융복합제품(로봇·드론·스마트팩토리) 중점, 시범사용 이후 관리·활용 점검과 성과 중심 관리체계.",
      "as_of": "2025-12-18",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f14",
      "claim": "로봇신문이 요약한 2024년 국내 로봇산업 실태조사(2024년 말 기준)에서 로봇산업 매출은 6조1695억원이며 제조업용 로봇 3조1075억원, 로봇부품 및 소프트웨어 1조9810억원, 전문서비스용 로봇 6423억원, 개인서비스용 로봇 4386억원으로 나뉜다.",
      "tag": "사실",
      "source_ids": [
        "ref-903"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "산업통상부·한국로봇산업진흥원·한국AI·로봇산업협회 조사(2025-07~09 실시). 로봇부품 및 소프트웨어 세부 상위 항목은 구동용 부품 5414억원, 제어용 부품 4841억원, 기타 부품 2910억원.",
      "as_of": "2026-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "같은 실태조사 요약에는 관제·오케스트레이션 소프트웨어나 서비스형 로봇(임대·구독) 매출을 따로 집계한 항목이 나타나지 않아, 국내 공식 통계만으로 관제 소프트웨어 시장 규모를 추적하기는 어려울 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-903"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기사 요약의 분류는 제조업용·전문서비스용·개인서비스용·로봇부품 및 소프트웨어뿐이고 소프트웨어 세부 품목은 확인되지 않음. 보고서 원문 품목 분류표는 미확인.",
      "as_of": "2026-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "VDA 5050 3.0.0 명세는 이동로봇을 플릿 관제에 연결하는 복잡도를 줄이고 여러 제조사의 이기종 이동로봇 플릿이 같은 공간에서 조율되어 운영되게 하는 것을 목표로 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "목표: 'to reduce complexity when connecting mobile robots to a fleet control system', 서로 다른 제조사 이기종 플릿의 공동 운영, 항법 방식과 무관한 범용 인터페이스.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f17",
      "claim": "Open-RMF 의 플릿 어댑터 패키지(rmf_fleet_adapter 2.14.0)는 Apache License 2.0 으로 배포된다.",
      "tag": "사실",
      "source_ids": [
        "ref-1297"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "package.xml 의 license 태그: 'Apache License 2.0', version 2.14.0 (main 브랜치, 확인일 기준).",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "제조 공장 사례(한국, 벤더 주장 인용): 한국무역협회 보고서(2021-11)는 협동로봇 가격이 전통 산업용 로봇의 25~30% 수준이고 투자 회수 기간이 약 195일이라고 제시하나, 회수 기간 수치는 장비 제조사 자료에 기댄 것이다.",
      "tag": "추정",
      "source_ids": [
        "ref-1298"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 회수 기간 약 195일(출처: 장비 제조사). '비용도 전통 산업용 로봇의 25~30% 수준으로 저렴'. 측정 방법·기준선 미공개.",
      "as_of": "2021-11-22",
      "site_type": "제조 공장",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f19",
      "claim": "제조 공장 사례: Sivalingam·Subramaniam(Heliyon, 2024-02)은 디젤 연료 필터 조립 공정에 쓸 협동로봇 12종을 비용을 포함한 가중 기준으로 비교해 고르는 AHP–TOPSIS 혼합 다기준 의사결정 방법을 적용했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1291"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 'The choice of a suitable collaborative robot (cobot) for a real-time industrial process is one of the obstacles to effective robot implementation in terms of energy and cost.' 12종 비교.",
      "as_of": "2024-02",
      "site_type": "제조 공장",
      "flow_item": "수행 자원"
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 핵심 질문(도입 비용을 넘는 효과가 나오며 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가)에 대해, 현장은 투자수익률·회수 기간·총소유비용을 주 판단 기준으로 쓰고 구매·하이브리드·서비스형 로봇으로 조달 방식이 나뉘며 병원·식당·창고의 효과 수치가 보고되지만 대부분 단일 사례·벤더 수치여서 같은 기준선의 독립 비교는 부족하고, 이기종 통합 비용과 잠금을 줄이려 개방 인터페이스·인증 통합자를 조달 조건으로 두는 사례가 있는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1299",
        "ref-1285",
        "ref-1296",
        "ref-1292",
        "ref-1290",
        "ref-1293",
        "ref-1298",
        "ref-872",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1~f3(결정 요인·조달 방식·통합 비용 미달), f8·f9·f10·f18(현장 사례 수치, 벤더·단일 사례 중심), f11·f16(개방 인터페이스·통합자 인증) 종합.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 3. 경제성·조달·사업 모델에서 ROP가 직접 맡을 범위는 사용량 기반 과금과 투자 효과 판단의 근거가 되는 계량 데이터(작업 완료 수·피킹 수·가동 시간 등)와 도입 전후 성과 기준선의 기록·제공, 로봇 선정 때 필요한 능력·인터페이스 적합성 정보 제공, 개방 인터페이스 준수로 로봇 교체·추가 비용을 낮추는 구조로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1292",
        "ref-1299",
        "ref-1286",
        "ref-031",
        "ref-1291"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "피킹량 기반 월 과금(f8), 사용량 기반 사업 모델(f6), 통합 비용 미달(f3), 이기종 연결 복잡도 감소 목표(f16), 선정 기준(f19) 종합.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f22",
      "claim": "연계 대상: 분류 원문 19장 기준으로 자본 예산·회계 처리·구매 계약·요금 청구·정부 지원 신청은 재무·구매·전사 자원 계획 쪽이, 로봇 하드웨어 가격과 정비는 제조사·통합자가 맡으므로, ROP는 그들에게 사용량·성과 데이터를 넘기고 계약 조건(최소 요금·계약 기간)을 운영 제약으로 받는 쪽을 맡는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1292",
        "ref-947",
        "ref-1295",
        "ref-1296"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "최소 계약 3~5년·월 최소 요금(f8), 국비 지원·민간 부담 구조(f12), 공공 시범구매(f13), 수명주기 비용 분석 대상자(f5) 종합.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f23",
      "claim": "이 영역은 시장 통계의 1. 기술·시장·업체 동향(f14·f15), 수용 기준의 2. 사용 사례·요구·책임 범위(f20), 대수 산정 비용의 35. 처리능력·규모·배치 설계(oq-129), 성과 기준선의 39. 운영 성과 측정·개선(f3·f21), 개방 인터페이스의 21. 상호운용 표준·적합성과 20. 로봇·제조사 관제 연동(f16·f11·f3), 선정 기준의 5. 로봇 능력·작업 표현(f19), 계약 조건의 58. 다사업자 책임·계약·데이터(f8), 라이선스의 59. 법·규제·보험·라이선스(f17), 교체·수명주기 비용의 57. 자산·소프트웨어 수명주기 관리(f5·f7), 과금 데이터 전달의 23. 업무 시스템 연동(f22), 인력 대체 논의의 60. 노동·수용성·접근성(f9), 적용 현장인 61. 물류창고(f8)·62. 제조 공장(f6·f18·f19)·63. 병원·의료(f10·f11)·64. 상업 시설(f9)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-903",
        "ref-1299",
        "ref-031",
        "ref-872",
        "ref-1291",
        "ref-1292",
        "ref-1297",
        "ref-1296",
        "ref-1287",
        "ref-1293",
        "ref-1290",
        "ref-1298",
        "ref-1286"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 연결의 근거 finding 을 괄호로 표시. 35. 처리능력·규모·배치 설계 연결은 기존 열린 질문 oq-129 에 기댐.",
      "as_of": "2026-09-30",
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
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 공식 명세(현재 main 은 3.0.0). 이번 실행에서 이기종 플릿 연결 복잡도 감소라는 명세 목표를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-1285",
      "org": "NIST (National Institute of Standards and Technology)",
      "title": "NIST Grant/Contractor Report NIST GCR 24-054",
      "published": "2024",
      "url": "https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958147",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. PDF 는 받았으나 본문 텍스트를 추출하지 못해 검색 요약 범위만 썼다. 로봇 도입의 ROI 과제와 서비스형 로봇의 초기 투자 완화를 다룬 NIST 위탁 보고서다.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1286",
      "org": "Buerkle, A., Eaton, W., Al-Yacoub, A., Zimmer, M., Kinnell, P., Henshaw, M., Coombes, M., Chen, W.-H., & Lohse, N. (Robotics and Computer-Integrated Manufacturing 81)",
      "title": "Towards industrial robots as a service (IRaaS): Flexibility, usability, safety and business models",
      "published": "2023-06",
      "url": "https://www.sciencedirect.com/science/article/pii/S0736584522001661",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 출판사·저장소 모두 403 이며 서지는 Semantic Scholar API 로 확인했다. 이동형 산업용 로봇을 빌려 쓰는 IRaaS 패러다임과 시간·사용량 기반 사업 모델을 제안한다.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1287",
      "org": "Lee, J. S., & Aswani, A. (arXiv)",
      "title": "Profit Maximization for a Robotics-as-a-Service Model",
      "published": "2025-09-30",
      "url": "https://arxiv.org/abs/2509.26595",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "서비스형 로봇 제공자의 작업별 가격 결정과 열화 로봇 교체 결정을 마르코프 결정 과정으로 함께 최적화하는 프리프린트(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2509.26595",
      "source_unopened": false
    },
    {
      "id": "ref-947",
      "org": "한국로봇산업진흥원",
      "title": "서비스로봇 실증사업",
      "published": null,
      "url": "https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "로봇 도입 비용 50% 이내 국비 지원, 민간 부담 구조, 선정·평가 절차를 안내하는 한국로봇산업진흥원 사업 소개 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do",
      "source_unopened": false
    },
    {
      "id": "ref-872",
      "org": "Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "RoMi-H Empanelment Programme 2025",
      "published": "2025-05",
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "RoMi-H 통합을 맡을 시스템 통합자를 연 2회 평가·등재하는 CHART 프로그램 안내(2025-05-01 시행).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "source_unopened": false
    },
    {
      "id": "ref-1290",
      "org": "Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16)",
      "title": "Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios",
      "published": "2026-04",
      "url": "https://www.nature.com/articles/s41598-026-49800-9",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "중국 3차 병원의 약품·검체 배송 AMR 10대를 6개월 병행 대조로 평가하고 10년 경제성을 추정한 연구(Europe PMC 초록 확인, 본문 미확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:PMC13276296&resultType=core&format=json",
      "source_unopened": false
    },
    {
      "id": "ref-1291",
      "org": "Sivalingam, C. S., & Subramaniam, S. K. (Heliyon)",
      "title": "Cobot selection using hybrid AHP-TOPSIS based multi-criteria decision making technique for fuel filter assembly process",
      "published": "2024-02",
      "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10882119/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "연료 필터 조립 공정용 협동로봇 12종을 AHP–TOPSIS 로 선정한 사례 연구(Europe PMC 초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:PMC10882119&resultType=core&format=json",
      "source_unopened": false
    },
    {
      "id": "ref-1292",
      "org": "AutoStore",
      "title": "Buying vs. RaaS: What's the Best Strategy for Investing in Warehouse Robotics?",
      "published": null,
      "url": "https://www.autostoresystem.com/insights/buying-vs-raas-whats-the-best-strategy-for-investing-in-warehouse-robotics",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "구매와 피킹량 기반 서비스형 로봇(pay-per-pick) 모델을 비교하고 선구매 그리드·구독 대상·최소 계약 조건을 설명하는 벤더 글.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.autostoresystem.com/insights/buying-vs-raas-whats-the-best-strategy-for-investing-in-warehouse-robotics",
      "source_unopened": false
    },
    {
      "id": "ref-1293",
      "org": "지디넷코리아 (신영빈)",
      "title": "'30만원 vs 200만원' 인건비 부담…서빙로봇 판 커진다",
      "published": "2023-03",
      "url": "https://zdnet.co.kr/view/?no=20230307165036",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "국내 식당 서빙로봇 렌털 요금(월 30만원대)과 업체별 렌털·유예형 상품을 인건비와 비교한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://zdnet.co.kr/view/?no=20230307165036",
      "source_unopened": false
    },
    {
      "id": "ref-903",
      "org": "로봇신문",
      "title": "[Cover Story] '2024년 국내 로봇산업 실태 조사 결과 보고서' 요약",
      "published": "2026-01",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=44544",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "2024년 말 기준 국내 로봇산업 실태조사의 매출·분류 결과를 요약한 기사. 보고서 원문은 미확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.irobotnews.com/news/articleView.html?idxno=44544",
      "source_unopened": false
    },
    {
      "id": "ref-1295",
      "org": "전자신문",
      "title": "조달청, 2026년 혁신제품 시범구매 기본계획 발표",
      "published": "2025-12-18",
      "url": "https://www.etnews.com/20251218000194",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "조달청 2026년 혁신제품 시범구매 예산 확대(839억원)와 로봇 등 AI 융복합 제품 중점, 시범사용 후 점검 방식을 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.etnews.com/20251218000194",
      "source_unopened": false
    },
    {
      "id": "ref-1296",
      "org": "IEC (International Electrotechnical Commission)",
      "title": "IEC 60300-3-3:2017 Dependability management - Part 3-3: Application guide - Life cycle costing",
      "published": "2017-01-27",
      "url": "https://webstore.iec.ch/en/publication/31206",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 유료 표준이라 IEC 웹스토어의 공식 개요 페이지만 열었다. 수명주기 비용 개념과 적용, 신뢰성 관련 비용을 다루는 적용 지침 3판.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": "https://webstore.iec.ch/en/publication/31206"
    },
    {
      "id": "ref-1297",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "rmf_ros2/rmf_fleet_adapter/package.xml",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/package.xml",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 플릿 어댑터 패키지 정의 파일. 버전 2.14.0, 라이선스 Apache License 2.0.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/main/rmf_fleet_adapter/package.xml",
      "source_unopened": false
    },
    {
      "id": "ref-1298",
      "org": "한국무역협회 (KDI 경제정보센터 게재)",
      "title": "협동로봇: 중소기업 스마트 제조의 시작점",
      "published": "2021-11-22",
      "url": "https://eiec.kdi.re.kr/policy/domesticView.do?ac=0000159915&datecount=&issus=S&pg=&pp=20",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "중소 제조기업의 협동로봇 도입을 다룬 한국무역협회 보고서 소개. 가격 비율과 제조사 자료 기반 회수 기간을 제시한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://eiec.kdi.re.kr/policy/domesticView.do?ac=0000159915&datecount=&issus=S&pg=&pp=20",
      "source_unopened": false
    },
    {
      "id": "ref-1299",
      "org": "Modern Materials Handling (Bridget McCrea; Peerless Research Group·MHI 조사)",
      "title": "2026 Intralogistics Robotics Survey: Robotics moves into the mainstream",
      "published": "2026-06-01",
      "url": "https://www.mmh.com/article/2026_intralogistics_robotics_survey_robotics_moves_into_the_mainstream",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "사내 물류 로봇 도입 설문(응답 166명)의 투자 결정 요인, 도입 방식(구매·하이브리드·RaaS), 목표 달성 여부를 보고한 기사형 설문 보고.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.mmh.com/article/2026_intralogistics_robotics_survey_robotics_moves_into_the_mainstream",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/planning-and-business/economics-procurement-and-business-models.md",
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
      "rationale": "섹션 3: f20(핵심 질문 답, 추정), f1·f3(ROI·회수 기간·TCO 가 판단 기준이고 11% 는 통합 비용 등 목표 미달), f4(ROI 가 최대 과제) / 섹션 4: TCO·ROI·회수 기간 f1, 수명주기 비용 f5, 서비스형 로봇·사용량 기반 과금 f6·f8(벤더 주장 병기), 동적 가격·교체 f7 / 섹션 5: 물류창고 — f8(수행 자원, 벤더 주장), 제조 공장 — f6(제약)·f18(예외·성과, 벤더 주장)·f19(수행 자원), 병원 — f10(예외·성과)·f11(수행 자원, 싱가포르), 상업 시설 — f9(수행 자원, 한국 식당). 가정·실외·기타 사례는 찾지 못했음을 명시 / 섹션 6: 투자 판단 기준 f1·f2, 수명주기 비용 분석 f5, 다기준 선정 f19, 과금 모델 f2·f6·f7·f8·f9, 공공 실증·조달 f12·f13, 개방 인터페이스·인증 통합자 조건 f11·f16 / 섹션 7: IEC 60300-3-3 f5(원문 미열람), VDA 5050 목적 f16, Open-RMF 라이선스 f17, 서비스로봇 실증사업 f12, 조달청 혁신제품 시범구매 f13(연계 대상) / 섹션 8: f1~f3·f6·f7·f10·f19 / 섹션 9: f21(직접 범위), f22(연계 대상) / 섹션 10: f23 — 1, 2, 5, 20, 21, 23, 35, 39, 57, 58, 59, 60, 61, 62, 63, 64 / 섹션 11: 기존 oq-129(미해결), oq-160(미해결), oq-162(f14·f15 로 부분 근거, 미해결 유지)와 open_questions_new 5건. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f10·f11, 64. 상업 시설 페이지에 f9, 62. 제조 공장 페이지에 f18·f19 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "총소유비용",
      "term_en": "Total Cost of Ownership (TCO)",
      "definition": "장비를 사는 비용뿐 아니라 설치·통합·교육·운영·정비·폐기까지 보유 기간 전체에 드는 비용을 합한 투자 판단 지표이다."
    },
    {
      "term_ko": "수명주기 비용 분석",
      "term_en": "Life Cycle Costing (LCC, IEC 60300-3-3)",
      "definition": "품목의 획득부터 운영·정비·개선·폐기까지 수명주기 전체 비용을 산정해 대안을 비교하는 방법으로, IEC 60300-3-3 이 신뢰성 관련 비용을 중심으로 적용 지침을 준다."
    },
    {
      "term_ko": "투자 회수 기간",
      "term_en": "Payback Period",
      "definition": "도입으로 얻는 순절감·순수익의 누적액이 초기 투자액과 같아지기까지 걸리는 기간이다."
    },
    {
      "term_ko": "피킹량 기반 과금",
      "term_en": "Pay-per-pick",
      "definition": "자동화 창고 설비나 로봇의 사용료를 실제 처리한 피킹 수(물동량)에 따라 매기는 사용량 기반 과금 방식이다."
    }
  ],
  "open_questions_new": [
    "ROP 같은 다중 제조사 오케스트레이션 플랫폼의 과금 단위(로봇당·작업당·현장당·구독)를 비교하거나 공개한 자료가 있는가? | 관련 영역: 3. 경제성·조달·사업 모델, 41. 플랫폼 아키텍처·외부 API | 근거: f2 | 종류: 일반",
    "사용량 기반 서비스형 로봇 계약에서 과금·최소 요금·가동률 미달을 판정하는 계량 데이터를 누가 측정하고, 여러 사업자가 함께 쓰는 현장에서 그 값을 어떻게 합의하는가? | 관련 영역: 3. 경제성·조달·사업 모델, 58. 다사업자 책임·계약·데이터, 39. 운영 성과 측정·개선 | 근거: f8 | 종류: 일반",
    "병원 배송 로봇 경제성 평가의 비용 항목·할인율·인건비 산정 방식을 비교 가능한 기준으로 정리한 연구가 있으며, 국내 병원 인건비 조건에서도 같은 결론이 나오는가? | 관련 영역: 3. 경제성·조달·사업 모델, 63. 병원·의료 | 근거: f10 | 종류: 일반",
    "국내 공공·민간 로봇 조달에서 VDA 5050 같은 개방 인터페이스 적합성이나 통합자 인증을 입찰 요구조건으로 명시한 사례가 있는가? | 관련 영역: 3. 경제성·조달·사업 모델, 21. 상호운용 표준·적합성 | 근거: f16 | 종류: 일반",
    "이기종 로봇 통합 비용이 로봇 도입 총소유비용에서 차지하는 비중과, 공통 인터페이스·오케스트레이션 플랫폼이 그 비용을 얼마나 줄이는지 측정한 독립 연구가 있는가? | 관련 영역: 3. 경제성·조달·사업 모델, 20. 로봇·제조사 관제 연동 | 근거: f3 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 16,
    "cross_checked_count": 0,
    "unverified": [
      "f4 NIST GCR 24-054 는 PDF 본문 추출 실패로 검색 요약 범위만 사용, 제목·저자 세부 미확인",
      "f6 Buerkle 외 2023 원문·초록 모두 열지 못함(403, API 초록 없음), 검색 요약 범위만 사용",
      "f10 Li 외 2026 은 초록만 확인해 비용 항목·할인율·회수 기간 미확인",
      "f14·f15 실태조사 보고서 원문 품목 분류표 미확인(기사 요약 기준)",
      "f1~f3 설문 방법론(표본 추출·가중) 미공개",
      "f8 AutoStore 그리드 비용 비중 20~40% 는 벤더 주장이며 독립 확인 실패",
      "f18 협동로봇 회수 기간 195일은 제조사 자료 인용, 측정 기준 미확인",
      "IRaaS 기술·시스템 요구(Mabkhot 외, Procedia CIRP 130, 2024)는 서지만 확인하고 초록을 얻지 못해 넣지 않음",
      "Forrester TEI(Locus Robotics 위탁) PDF 추출 실패로 넣지 않음",
      "플릿 관리 소프트웨어 로봇당 월 요금(검색 요약의 $50~500)은 제3자 블로그뿐이고 InOrbit 공식 페이지에 가격이 없어 넣지 않음",
      "하나금융경영연구소 RaaS 보고서(국회도서관 국가전략정보포털)는 요약 내용의 사례 신뢰성이 낮아 넣지 않음",
      "싱가포르 보건부가 RoMi-H 를 공공 의료기관 통합 플랫폼으로 인정했다는 내용은 검색 요약과 CGH 소개 페이지 표현이 달라 finding 으로 내지 않음",
      "가정·실외·기타 현장의 경제성·과금 사례를 찾지 못함",
      "oq-160 시장 규모 산정 방법론 공개 독립 출처를 찾지 못함",
      "oq-129 채팅 기반 대수 결정과 비용 목적 설정 주체에 관한 자료를 찾지 못함"
    ],
    "scope_violations": [
      "f12·f13: 정부 지원 신청·공공 조달은 원문 19장 '상위 업무 시스템'의 재무·구매 쪽 연계 대상에 가까워 f13 은 '연계 대상: '으로 표시하고 f22 에서 ROP 직접 범위와 구분함",
      "f8·f9: 로봇 하드웨어 가격·렌털 조건은 제조사·서비스 사업자의 사업 조건으로 참고 사례로만 쓰고, ROP 직접 범위는 f21 에서 계량 데이터 제공으로 한정함",
      "f10: 병원 AMR 의 경로 계획 알고리즘(Dijkstra·A*·DWA)은 원문 19장 '로봇 자체 지능·제어' 쪽이라 claim 에서 빼고 경제성 결과만 씀"
    ],
    "budget_used": {
      "queries": 19,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 19회/30, 신규 출처 15건/15(ref-1285~ref-1299, 예약 구간 안)로 신규 출처 상한에 도달해 CGH RoMi-H 소개 페이지, Mabkhot 외(2024), 하나금융경영연구소 보고서를 출처로 넣지 않았다. 재사용 1건(ref-031): 참고문헌 목록 요약에 행이 없어 값은 이전 브리프 2026-09-30-18 출처 표를 따랐고, 이번에 GitHub 공식 저장소 원문을 다시 열어 명세 목표 문장을 확인했다. 원문 열람: 16건 중 14건을 열었다(webfetch 12, github_raw 2). ref-1285(PDF 추출 실패)·ref-1286(403)은 fetched false·원문 미열람이며, ref-1296 은 유료 표준이라 공식 개요 페이지만 열어 원문 미열람으로 표시했다. ref-1290·ref-1291 은 PMC 가 캡차로 막혀 Europe PMC API 로 초록만 읽었다. 교차 확인 0건(주요 수치마다 독립 출처 2곳을 찾지 못함; NIST 보고서가 인용한 이전 MMH 설문 수치는 2026 설문과 연도가 달라 교차 확인으로 보지 않음). 벤더 주장 2건(f8·f18)은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문에는 f20 으로 답했고 결론은 '판단 기준(ROI·회수 기간·TCO)과 조달 방식(구매·하이브리드·RaaS)은 확인되나 현장 효과 수치는 단일 사례·벤더 중심이어서 같은 기준선의 독립 비교가 부족하다'는 추정이다. 현장 유형 사례는 물류창고(f8, 벤더)·제조 공장(f6·f18·f19)·병원(f10 중국, f11 싱가포르)·상업 시설(f9, 한국 식당)이며 가정·실외·기타는 찾지 못했다. 국내 자료는 한국로봇산업진흥원(ref-947)·로봇신문(ref-903)·전자신문(ref-1295)·지디넷코리아(ref-1293)·한국무역협회(ref-1298)다. 기존 열린 질문 oq-162 는 f14·f15 로 부분 근거(요약 기사상 관제 소프트웨어 별도 집계 항목 없음)만 있어 해결 제안하지 않았고, oq-129·oq-160 은 새 근거가 없다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding 은 없다(f7 의 데이터 기반 가격 결정은 운영 연구 모델로 보고 L 영역 연결을 제안하지 않음). 용어집에 이미 있는 서비스형 로봇·서비스 수준 협약·핀옵스·기술 성숙도·차량 소요대수 산정·등재 프로그램·의료 로봇 미들웨어 RoMi-H 는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-19/verification.json

```json
{
  "run_id": "2026-09-30-19",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: MMH 기사(Bridget McCrea, 2026-06-01, 응답 166명, 2026-03~04 조사) 원문에서 ROI 63%·회수 기간 52%·TCO 47%·공정 성과 41% 일치. 단일 출처이며, NIST 보고서가 인용한 이전 MMH 설문(70%·64%·60%)은 연도가 달라 교차 확인으로 보지 않는다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 하이브리드 53%·전액 CapEx 37%·RaaS 11% 일치. 원문은 이 비율을 '현재 로봇을 쓰는 응답자' 기준으로 제시하므로 본문에 그 기준을 밝혀야 한다(수정 지시)."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "수치는 원문과 같다. 다만 원문은 사업 목표 달성 74%·미달 21%·모름 5%를 따로 제시하고, 11%는 ROI·신뢰성·통합 비용 목표를 놓쳤다는 별도 성과 항목이다. 지금 문장은 74%와 11%를 짝지어 나머지 비율처럼 읽힐 수 있으니 고쳐야 한다(수정 지시)."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "PDF 열람은 했으나 본문 추출이 되지 않아 원문 미열람이다. 검색 결과 요약에서 'top challenge … identifying and achieving ROI'와 RaaS가 큰 자본 지출 없이 시도할 수 있어 SME·위험 회피 기업에 매력적이라는 서술을 확인했다. NIST 발행 정보 페이지 기준 정식 제목은 'Research Opportunities for Advancing Measurement Science for Manufacturing Robotics', 저자 Elena Messina·Kamel S. Saidi, 발행일 2024-06-07이며 브리프의 제목(PDF 페이지 제목)과 다르다(수정 지시). medium 이상 부여 불가."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: IEC 웹스토어 공식 개요에서 3.0판·2017-01-27 발행, 'particularly highlights the costs associated with the dependability of an item' 문장 일치. 유료 표준이라 본문은 미열람이다. 발행 9년이 지났으므로 월간 재검증 대상이다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ScienceDirect·Loughborough 저장소 모두 403으로 원문 미열람이다. 검색 결과(Semantic Scholar·dblp·Loughborough 소개)에서 RCIM 81(102484, 2023), IRaaS 네 요소, 시간·사용량 기반 모델, SME 장벽(큰 초기 투자·TCO 불확실성·전문성 부족)을 확인했다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2509.26595 초록(2025-09-30 제출)에서 작업별 가격 제시·수락/거절, 확률적 열화, 가격·교체 결정의 MDP 공동 최적화, 생존 분석 기반 데이터 추정을 확인했다. 프리프린트다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: AutoStore 글 원문에서 그리드 선구매(시스템 비용의 20~40%), 로봇·포트·소프트웨어의 피킹량 기반 구독, 최소 계약 3~5년, 가동 로봇·포트 수 기준 월 최소 요금을 확인했다. 발행일은 미확인이다. 벤더 주장 표시(vendor_claim·추정·'벤더 주장:' 첫머리)가 올바르다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 지디넷코리아 신영빈 기자 기사. 발행일은 2023-03-08(브리프 2023-03)이다. 브이디컴퍼니 월 29만9천원, 비로보틱스 유예형(3년 후 소유권 결정), 알지티 월 30만원대, 최저임금 월 200만원 초과 비교가 일치한다. 렌털 요금은 업체 상품 조건을 옮긴 보도라 인건비 절감 효과로 일반화하지 않는다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Europe PMC 초록(Scientific Reports 16, 2026-04)에서 AMR 10대, 6개월 단일 기관 병행 대조, 배송 시간 32~36% 단축(p<0.001), 인력 19명 대비 7.3배 배송, 10년 692.8만 위안 절감, 민감도 분석이 일치한다. 비용 항목·할인율은 본문 미확인이며 중국 사례임을 밝힌다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: CGH 페이지 원문에서 CHART의 연 2회(bi-annual) 등재 프로그램, 기술 역량·배포 지식 평가, 2025-05-01부터 2년 유효, 공공 의료 분야 로봇·소프트웨어·IoT 통합은 등재된 시스템 통합자가 맡는다는 문장, 상호운용 문장을 확인했다. 같은 페이지에 보건부가 RoMi-H를 통합 플랫폼으로 인정한다는 문장도 있으나 브리프가 finding으로 내지 않았으므로 본문에 넣지 않는다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "한국로봇산업진흥원 페이지 원문에서 2020년부터 지원, 도입 비용 50% 이내 국비, 민간 부담 총사업비 50% 이상(현금)·수요기관 25% 이상, 서류→발표→현장→최종평가·중간점검 절차를 확인했다. 지원 분야는 '물류, 웨어러블, 의료, 돌봄' 4대 분야와 협동로봇·언택트서비스인데 브리프에는 '돌봄'이 빠져 있다(수정 지시)."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 전자신문 2025-12-18 기사에서 예산 839억원(전년 대비 310억원 증가, 곧 529억원), AI 융복합제품(로봇·드론·스마트팩토리) 중점, 시범사용 뒤 관리·활용 점검을 확인했다. '조달청이 직접 구매해 공공기관에 제공'은 기사에서 공통 행정 AI 제품 설명으로 나오므로 제도 일반의 서술은 기사 요약 범위로 한정한다. '연계 대상' 표시를 유지한다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 로봇신문 기사(2026-01-25)에서 조사 주체, 2024-12-31 기준, 조사 기간 2025-07-04~09-12, 총매출 6조1695억원과 네 부문 금액이 일치한다. 보고서 원문은 미확인이며 기사 요약에 기댄 단일 출처다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 기사 요약의 로봇부품 및 소프트웨어 세부 품목은 구동용·제어용·기타 부품뿐이고 소프트웨어 세부 항목이 없다. 보고서 원문의 품목 분류표는 확인하지 못했으므로 추정 태그가 맞다. oq-162 해결 근거로는 부족하다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문(data/source_texts/ref-031, 3.0.0) 2장 Scope의 목표 문장 'to reduce complexity when connecting mobile robots to a fleet control system'과 이기종 플릿 공동 운영 목표가 일치한다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: GitHub raw package.xml에서 rmf_fleet_adapter 2.14.0, 'Apache License 2.0'을 확인했다(main 브랜치, 확인일 2026-09-30)."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "부분 뒷받침. KDI 경제정보센터 게재 페이지와 한국무역협회 원게시 페이지 모두에서 '전통 산업용 로봇의 25~30% 수준(대당 2~6천만 원)'은 확인했으나, 투자 회수 기간 약 195일은 두 페이지와 검색 결과 어디에서도 찾지 못했다. 195일 수치는 본문에서 빼고 가격 비율만 [추정]·벤더 주장 병기 없이 보고서 인용으로 둔다. 발행일은 KDI 게재 2021-11-22, 무역협회 원게시 2021-11-17로 다르다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Europe PMC 초록(Heliyon 10(4), 2024-02-15)에서 협동로봇 12종, 비용을 포함한 기준, AHP 가중치·TOPSIS 순위, 디젤 연료 필터 조립 공정 적용을 확인했다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정. 근거 finding이 확인된 범위에서 결론이 성립한다. 단 f18의 195일 수치는 근거로 쓰지 않는다(수정 지시). 핵심 질문에 대한 답으로 3절에 추정으로 둔다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정. 피킹량 과금(f8), 사용량 기반 모델(f6), 통합 비용 미달(f3), 연결 복잡도 감소 목표(f16), 선정 기준(f19)에서 추론한 ROP 직접 범위로 원문 19장 경계와 충돌하지 않는다. 추정 태그를 유지한다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정. 재무·구매·전사 자원 계획과 제조사·통합자를 연계 대상으로 구분해 원문 19장 '상위 업무 시스템' 경계에 맞다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "연결 목록 추정. 모두 번호와 이름을 함께 썼고 부록 A 명칭과 일치한다. 35. 처리능력·규모·배치 설계 연결은 oq-129에만 기대므로 열린 질문 연계로 서술한다."
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
      "f14·f15(국내 로봇산업 실태조사 매출·분류)는 1. 기술·시장·업체 동향 페이지와 기존 열린 질문 oq-162(영역 1, 3)에 걸친다. 입력의 1. 기술·시장·업체 동향 요약에는 본문이 없어 같은 주장 여부는 확인하지 못했다. 같은 URL이 참고문헌에 있으면 퍼블리셔가 기존 id로 합친다.",
      "f16(VDA 5050 목적)은 ref-031을 재사용하며 다른 영역 페이지들의 VDA 5050 범위 서술과 겹칠 수 있다. 새 각주를 만들지 않고 ref-031을 재사용한 것이 맞다."
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
    "f3: 본문에 '사업 목표 달성 74%, 미달 21%, 모름 5%'를 함께 쓰고, 11%는 'ROI·신뢰성·통합 비용 목표를 놓쳤다는 별도 성과 항목'이라고 구분한다. 현재 문장은 11%가 74%의 나머지처럼 읽히기 때문이다(ref-1299 원문).",
    "f2: 도입 방식 비율(하이브리드 53%, 전액 CapEx 37%, RaaS 11%)이 '현재 로봇을 쓰는 응답자' 기준임을 본문에 밝힌다. 원문이 이 모집단 기준으로 제시한다.",
    "f18: '투자 회수 기간 약 195일'을 본문·표·5절 사례에서 삭제하고, '협동로봇 가격이 전통 산업용 로봇의 25~30% 수준'이라는 보고서 인용만 [추정]으로 남긴다. 195일은 KDI·한국무역협회 페이지와 검색 결과 어디에서도 확인되지 않았다.",
    "f20: 3절 종합 서술에서 f18의 195일 수치를 근거나 예시로 쓰지 않는다. f18 처분에 따른 조치다.",
    "ref-1285: 각주·reference_updates의 제목을 'Research Opportunities for Advancing Measurement Science for Manufacturing Robotics (NIST GCR 24-054)'로, 기관 표기에 저자 Messina, E. & Saidi, K. S.를, 발행일을 2024-06-07로 고친다. NIST 발행 정보 페이지와 다르기 때문이다.",
    "f12: 서비스로봇 실증사업의 지원 분야에 '돌봄'을 더해 '물류·웨어러블·의료·돌봄 4대 분야와 협동로봇·언택트서비스'로 쓴다. 한국로봇산업진흥원 원문이 이렇게 적는다.",
    "ref-1293 발행일을 2023-03-08로, ref-903 발행일을 2026-01-25로, ref-1291 발행일을 2024-02-15로 각주에 적는다. 이번 원문 확인 결과다.",
    "ref-1298: 각주 발행일을 2021-11-22(KDI 경제정보센터 게재일)로 두고, 한국무역협회 원게시일은 2021-11-17로 확인됐다고 13절 각주 또는 8절 서술에 짧게 남긴다. 두 날짜가 다르기 때문이다.",
    "ref-1285·ref-1286·ref-1296: 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates의 세 항목에 source_unopened: true를 넣는다. 각각 PDF 추출 실패, 403, 유료 표준이라 개요만 열람했다.",
    "f12·f13: 7절·9절에서 국비 실증 지원과 조달청 혁신제품 시범구매는 도입 조건·재원을 정하는 외부 제도(재무·구매 쪽 연계 대상)로 짧게 다루고, ROP 기능처럼 서술하지 않는다. 원문 19장 '상위 업무 시스템' 경계를 따른다.",
    "f8·f18: 본문에서 [추정]에 '벤더 주장'을 병기한 표시를 유지한다. f8은 AutoStore 자사 글이고, f18의 가격 비율도 업계 보고서의 제조사 자료 기반 인용이다.",
    "5절: 현장 유형을 물류창고(f8)·제조 공장(f6·f18·f19)·병원(f10 중국, f11 싱가포르)·상업 시설(f9 한국)로 나누고 사례마다 국가를 밝힌다. 가정·실외·기타 현장의 사례는 이번 조사에서 찾지 못했다고 명시하며, site_matrix_updates는 이 네 현장 유형 칸만 낸다.",
    "용어집 '수명주기 비용 분석' 후보: 정의를 f5가 확인한 범위(품목의 수명주기 비용을 산정하는 방법, IEC 60300-3-3은 특히 신뢰성 관련 비용을 강조)로 한정하고, '획득부터 … 폐기까지' 같은 세부 단계 나열은 근거 finding이 없으므로 빼거나 일반 정의로만 쓴다.",
    "11절: 기존 oq-129·oq-160·oq-162는 모두 미해결로 유지한다. oq-162에는 f14·f15가 부분 근거(요약 기사상 소프트웨어 별도 항목 없음, 보고서 원문 미확인)임을 적는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 22건, 미확인 1건, 교차 확인 0건. 강등: f18(투자 회수 기간 195일은 출처에서 확인되지 않아 삭제하고 가격 비율 25~30%만 [추정]으로 유지). 원문 미열람 출처: ref-1285(NIST GCR 24-054, PDF 본문 추출 실패, 검색 결과로 ROI·RaaS 서술 확인), ref-1286(Buerkle 외 2023, 403, 검색 결과 일치), ref-1296(IEC 60300-3-3, 유료 표준이라 공식 개요만 열람). 주의: 핵심 수치는 모두 단일 출처다. 설문 수치(f1~f3)는 표본 166명의 업계 설문이고 방법론은 기사 수준으로만 공개됐다. 현장 효과·요금 수치(f8 AutoStore 벤더 글, f9 국내 기사, f10 중국 단일 병원 초록)는 같은 기준선으로 비교할 수 없다. 가정·실외·기타 현장의 경제성 사례는 찾지 못했다. ref-1285의 정식 제목·저자·발행일(2024-06-07), f3의 목표 달성 비율 해석, f12 지원 분야의 '돌봄' 누락을 고치도록 지시했다. 기존 열린 질문 oq-129·oq-160·oq-162는 해결로 인정하지 않는다(oq-162는 f14·f15의 부분 근거만 있음). 정정 요청 없음. 검증 검색 6회(리서치 19회와 합해 25회/30).",
  "retry_reason": null
}
```

### runs/2026-09-30-19/pages.json

```json
{
  "run_id": "2026-09-30-19",
  "outline": [
    {
      "path": "docs/categories/planning-and-business/economics-procurement-and-business-models.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "로봇 도입 판단은 투자수익률·회수 기간·총소유비용이 주 기준이다. [사실][^ref-1299] 효과 수치는 단일 사례·벤더 중심이라 같은 기준선의 독립 비교가 부족한 것으로 보인다. [추정][^ref-1290]",
      "planned_findings": [
        "f1",
        "f3",
        "f4",
        "f20"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/economics-procurement-and-business-models.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "투자수익률·회수 기간·총소유비용·수명주기 비용 분석·서비스형 로봇·하이브리드 도입·피킹량 기반 과금·작업별 가격 결정을 정리한다. [사실][^ref-1299]",
      "planned_findings": [
        "f1",
        "f2",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/economics-procurement-and-business-models.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2200,
      "summary": "물류창고(벤더 계약 설명)·제조 공장(한국 보고서, 선정 사례)·병원(중국, 싱가포르)·상업 시설(한국) 사례를 여섯 항목으로 정리하고 가정·실외·기타 사례는 찾지 못했음을 밝힌다. [사실][^ref-1290]",
      "planned_findings": [
        "f6",
        "f8",
        "f9",
        "f10",
        "f11",
        "f18",
        "f19"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/economics-procurement-and-business-models.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1500,
      "summary": "로봇 도입 방식은 구매·하이브리드·서비스형 로봇으로 나뉘며 현재 사용자 기준 37%·53%·11%다. [사실][^ref-1299] 수명주기 비용 분석, 다기준 선정, 과금 모델, 외부 지원·조달 제도, 개방 인터페이스 조건을 다룬다.",
      "planned_findings": [
        "f1",
        "f2",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f11",
        "f12",
        "f13",
        "f16",
        "f19"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/economics-procurement-and-business-models.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 800,
      "summary": "수명주기 비용 지침 IEC 60300-3-3과 VDA 5050·Open-RMF 라이선스·RoMi-H 등재 프로그램, 그리고 연계 대상인 국내 실증·조달 제도를 표로 정리한다. [사실][^ref-1296]",
      "planned_findings": [
        "f5",
        "f11",
        "f12",
        "f13",
        "f16",
        "f17"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/economics-procurement-and-business-models.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1000,
      "summary": "업계 설문, NIST 보고서, IRaaS·RaaS 가격 연구, 병원 AMR 경제성 연구, 협동로봇 선정 연구, 국내 보고서·통계를 소개한다. [사실][^ref-1299]",
      "planned_findings": [
        "f1",
        "f4",
        "f6",
        "f7",
        "f10",
        "f14",
        "f18",
        "f19"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/economics-procurement-and-business-models.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 700,
      "summary": "ROP는 사용량·성과 계량 데이터와 기준선, 선정용 능력·인터페이스 정보를 맡고, 예산·회계·구매·청구·지원 신청은 재무·구매 쪽, 하드웨어 가격·정비는 제조사·통합자 쪽 연계 대상으로 보인다. [추정][^ref-1292]",
      "planned_findings": [
        "f21",
        "f22"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/economics-procurement-and-business-models.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1300,
      "summary": "성과 측정·연동·계약·라이선스·현장 유형 영역과 16개 연결을 정리한다. [추정][^ref-1299]",
      "planned_findings": [
        "f23"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/economics-procurement-and-business-models.md",
      "section": "11. 열린 질문",
      "budget_chars": 1000,
      "summary": "기존 oq-129·oq-160·oq-162·oq-257을 열림으로 유지하고(oq-162는 부분 근거) 새 질문 5건을 올린다. [추정][^ref-903]",
      "planned_findings": [
        "f14",
        "f15"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/planning-and-business/economics-procurement-and-business-models.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "섹션 3~11 신규 작성(현장 유형 사례 5건: 물류창고·제조 공장·병원 2·상업 시설, 표준·제도 6건, 자료 8건, 경계 2행, 연결 16개, 열린 질문 9건), 프런트매터 채움, 13절 각주 16건"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area03-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 3. 경제성·조달·사업 모델 의 \"6. 대표 접근법과 기술\" 절(1,380자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area03-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 3. 경제성·조달·사업 모델 의 \"8. 대표 연구와 자료\" 절(1,281자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area03-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 3. 경제성·조달·사업 모델 의 \"11. 열린 질문\" 절(1,265자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area03-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 3. 경제성·조달·사업 모델 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,106자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area03-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 3. 경제성·조달·사업 모델 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(857자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area03-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 3. 경제성·조달·사업 모델 의 \"4. 핵심 개념과 용어\" 절(817자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area03-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 3. 경제성·조달·사업 모델 의 \"3. 왜 중요한가\" 절(795자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 3. 경제성·조달·사업 모델 | 섹션 3~11 신규 작성(투자 판단 기준·도입 방식 설문, 현장 유형 사례 5건: 물류창고·제조 공장·병원 2·상업 시설, 표준·제도 6건, 자료 8건, 경계 2행, 연결 16개, 열린 질문 9건), 1차 수정 지시 14건 이행 | run 2026-09-30-19",
  "index_updates": {
    "home_recent": "2026-09-30 — 3. 경제성·조달·사업 모델: 섹션 3~11 신규 작성(투자 판단 기준과 구매·하이브리드·서비스형 로봇 도입 방식, 물류창고·제조 공장·병원·상업 시설 사례 5건, 국내 실증·조달 제도는 연계 대상으로 정리)",
    "category_recent": "2026-09-30 — 3. 경제성·조달·사업 모델: 섹션 3~11 신규 작성(현장 유형 사례 5건, 표준·제도 6건, 자료 8건, 연결 16개, 열린 질문 9건)",
    "area_recent": "2026-09-30 — 3. 경제성·조달·사업 모델: 영역 심화로 섹션 3~11 신규 작성, 새 열린 질문 5건"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "total-cost-of-ownership",
      "term_ko": "총소유비용",
      "term_en": "Total Cost of Ownership (TCO)",
      "definition": "장비를 사는 비용만이 아니라 보유·운영 기간 전체에 드는 비용을 합해 보는 투자 판단 지표이다.",
      "description": "2026년 사내 물류 로봇 설문에서 로봇 투자 결정 요인 3위(47%)였고, 중소기업에는 총소유비용의 불확실성이 도입 장벽으로 꼽힌다.",
      "related_areas": [
        3,
        39,
        57
      ],
      "sources": [
        "ref-1299",
        "ref-1286"
      ]
    },
    {
      "action": "new",
      "slug": "life-cycle-costing",
      "term_ko": "수명주기 비용 분석",
      "term_en": "Life Cycle Costing (LCC, IEC 60300-3-3)",
      "definition": "품목의 수명주기 비용을 산정하는 방법으로, IEC 60300-3-3 이 그 개념과 적용을 안내하며 특히 신뢰성 관련 비용을 강조한다.",
      "description": "IEC 60300-3-3:2017 은 3판이며 유료 표준이라 공식 개요만 확인했다.",
      "related_areas": [
        3,
        57
      ],
      "sources": [
        "ref-1296"
      ]
    },
    {
      "action": "new",
      "slug": "payback-period",
      "term_ko": "투자 회수 기간",
      "term_en": "Payback Period",
      "definition": "도입으로 얻는 순절감·순수익의 누적액이 초기 투자액과 같아지기까지 걸리는 기간이다.",
      "description": "2026년 사내 물류 로봇 설문에서 투자수익률 다음으로 많이 꼽힌 로봇 투자 결정 요인(52%)이다.",
      "related_areas": [
        3,
        39
      ],
      "sources": [
        "ref-1299"
      ]
    },
    {
      "action": "new",
      "slug": "pay-per-pick",
      "term_ko": "피킹량 기반 과금",
      "term_en": "Pay-per-pick",
      "definition": "자동화 창고 설비나 로봇의 사용료를 실제 처리한 피킹 수(물동량)에 따라 매기는 사용량 기반 과금 방식이다.",
      "description": "벤더 설명에 따르면 저장 그리드는 선구매하고 로봇·포트·소프트웨어를 피킹량 기반 월 구독으로 쓰며 최소 계약 기간과 월 최소 요금을 둔다(벤더 주장).",
      "related_areas": [
        3,
        58,
        61
      ],
      "sources": [
        "ref-1292"
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
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 공식 명세(현재 main 은 3.0.0). 이기종 플릿 연결 복잡도 감소라는 명세 목표를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-1285",
      "org": "Messina, E. & Saidi, K. S. (NIST, National Institute of Standards and Technology)",
      "title": "Research Opportunities for Advancing Measurement Science for Manufacturing Robotics (NIST GCR 24-054)",
      "published": "2024-06-07",
      "url": "https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958147",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. PDF 본문 텍스트를 추출하지 못해 검색 요약 범위만 썼다. 로봇 도입의 최대 과제로 투자수익률을 들고 서비스형 로봇의 초기 투자·위험 완화를 서술한 NIST 위탁 보고서다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-1286",
      "org": "Buerkle, A., Eaton, W., Al-Yacoub, A., Zimmer, M., Kinnell, P., Henshaw, M., Coombes, M., Chen, W.-H., & Lohse, N. (Robotics and Computer-Integrated Manufacturing 81)",
      "title": "Towards industrial robots as a service (IRaaS): Flexibility, usability, safety and business models",
      "published": "2023-06",
      "url": "https://www.sciencedirect.com/science/article/pii/S0736584522001661",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 출판사·저장소 모두 403 이며 서지는 검색 결과로 확인했다. 산업용 로봇을 빌려 쓰는 IRaaS 패러다임과 시간·사용량 기반 사업 모델을 제안하고 중소기업 도입 장벽을 든다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-1287",
      "org": "Lee, J. S., & Aswani, A. (arXiv)",
      "title": "Profit Maximization for a Robotics-as-a-Service Model",
      "published": "2025-09-30",
      "url": "https://arxiv.org/abs/2509.26595",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "서비스형 로봇 제공자의 작업별 가격 결정과 열화 로봇 교체 결정을 마르코프 결정 과정으로 함께 최적화하는 프리프린트(초록 확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-947",
      "org": "한국로봇산업진흥원",
      "title": "서비스로봇 실증사업",
      "published": null,
      "url": "https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "물류·웨어러블·의료·돌봄 4대 분야와 협동로봇·언택트서비스에 로봇 도입 비용 50% 이내 국비 지원, 민간 부담 구조, 선정·평가 절차를 안내하는 사업 소개 페이지.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-872",
      "org": "Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "RoMi-H Empanelment Programme 2025",
      "published": "2025-05",
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "RoMi-H 통합을 맡을 시스템 통합자를 연 2회 평가·등재하는 CHART 프로그램 안내(2025-05-01 시행).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-1290",
      "org": "Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16)",
      "title": "Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios",
      "published": "2026-04",
      "url": "https://www.nature.com/articles/s41598-026-49800-9",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "중국 3차 병원의 약품·검체 배송 AMR 10대를 6개월 병행 대조로 평가하고 10년 경제성을 추정한 연구(초록 확인, 본문 미확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-1291",
      "org": "Sivalingam, C. S., & Subramaniam, S. K. (Heliyon)",
      "title": "Cobot selection using hybrid AHP-TOPSIS based multi-criteria decision making technique for fuel filter assembly process",
      "published": "2024-02-15",
      "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10882119/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "연료 필터 조립 공정용 협동로봇 12종을 AHP–TOPSIS 로 선정한 사례 연구(초록 확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-1292",
      "org": "AutoStore",
      "title": "Buying vs. RaaS: What's the Best Strategy for Investing in Warehouse Robotics?",
      "published": null,
      "url": "https://www.autostoresystem.com/insights/buying-vs-raas-whats-the-best-strategy-for-investing-in-warehouse-robotics",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "구매와 피킹량 기반 서비스형 로봇 모델을 비교하고 선구매 그리드·구독 대상·최소 계약 조건을 설명하는 벤더 글(벤더 주장).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-1293",
      "org": "지디넷코리아 (신영빈)",
      "title": "'30만원 vs 200만원' 인건비 부담…서빙로봇 판 커진다",
      "published": "2023-03-08",
      "url": "https://zdnet.co.kr/view/?no=20230307165036",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "국내 식당 서빙로봇 렌털 요금(월 30만원대)과 업체별 렌털·유예형 상품을 인건비와 비교한 기사.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-903",
      "org": "로봇신문",
      "title": "[Cover Story] '2024년 국내 로봇산업 실태 조사 결과 보고서' 요약",
      "published": "2026-01-25",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=44544",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "2024년 말 기준 국내 로봇산업 실태조사의 매출·분류 결과를 요약한 기사. 보고서 원문은 미확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-1295",
      "org": "전자신문",
      "title": "조달청, 2026년 혁신제품 시범구매 기본계획 발표",
      "published": "2025-12-18",
      "url": "https://www.etnews.com/20251218000194",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "조달청 2026년 혁신제품 시범구매 예산 확대(839억원)와 로봇 등 AI 융복합 제품 중점, 시범사용 후 점검 방식을 전한 기사.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-1296",
      "org": "IEC (International Electrotechnical Commission)",
      "title": "IEC 60300-3-3:2017 Dependability management - Part 3-3: Application guide - Life cycle costing",
      "published": "2017-01-27",
      "url": "https://webstore.iec.ch/en/publication/31206",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 유료 표준이라 IEC 웹스토어의 공식 개요 페이지만 열었다. 수명주기 비용 개념과 적용, 신뢰성 관련 비용을 다루는 적용 지침 3판.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-1297",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "rmf_ros2/rmf_fleet_adapter/package.xml",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/package.xml",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 플릿 어댑터 패키지 정의 파일. 버전 2.14.0, 라이선스 Apache License 2.0.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-1298",
      "org": "한국무역협회 (KDI 경제정보센터 게재)",
      "title": "협동로봇: 중소기업 스마트 제조의 시작점",
      "published": "2021-11-22",
      "url": "https://eiec.kdi.re.kr/policy/domesticView.do?ac=0000159915&datecount=&issus=S&pg=&pp=20",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "중소 제조기업의 협동로봇 도입을 다룬 한국무역협회 보고서 소개. 제조사 자료 기반의 가격 비율(전통 산업용 로봇의 25~30%)을 인용한다. KDI 게재일 2021-11-22, 한국무역협회 원게시일 2021-11-17.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    },
    {
      "id": "ref-1299",
      "org": "Modern Materials Handling (Bridget McCrea; Peerless Research Group·MHI 조사)",
      "title": "2026 Intralogistics Robotics Survey: Robotics moves into the mainstream",
      "published": "2026-06-01",
      "url": "https://www.mmh.com/article/2026_intralogistics_robotics_survey_robotics_moves_into_the_mainstream",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "사내 물류 로봇 도입 설문(응답 166명)의 투자 결정 요인, 도입 방식(구매·하이브리드·RaaS), 목표 달성 여부를 보고한 기사형 설문 보고.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-business/economics-procurement-and-business-models.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "ROP 같은 다중 제조사 오케스트레이션 플랫폼의 과금 단위(로봇당·작업당·현장당·구독)를 비교하거나 공개한 자료가 있는가?",
      "areas": [
        3,
        41
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "사용량 기반 서비스형 로봇 계약에서 과금·최소 요금·가동률 미달을 판정하는 계량 데이터를 누가 측정하고, 여러 사업자가 함께 쓰는 현장에서 그 값을 어떻게 합의하는가?",
      "areas": [
        3,
        58,
        39
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "병원 배송 로봇 경제성 평가의 비용 항목·할인율·인건비 산정 방식을 비교 가능한 기준으로 정리한 연구가 있으며, 국내 병원 인건비 조건에서도 같은 결론이 나오는가?",
      "areas": [
        3,
        63
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 공공·민간 로봇 조달에서 VDA 5050 같은 개방 인터페이스 적합성이나 통합자 인증을 입찰 요구조건으로 명시한 사례가 있는가?",
      "areas": [
        3,
        21
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "이기종 로봇 통합 비용이 로봇 도입 총소유비용에서 차지하는 비중과, 공통 인터페이스·오케스트레이션 플랫폼이 그 비용을 얼마나 줄이는지 측정한 독립 연구가 있는가?",
      "areas": [
        3,
        20
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시",
      "title": "3. 경제성·조달·사업 모델"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시",
      "title": "3. 경제성·조달·사업 모델"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시",
      "title": "3. 경제성·조달·사업 모델"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시",
      "title": "3. 경제성·조달·사업 모델"
    },
    {
      "site_type": "제조 공장",
      "item": "제약",
      "link": "docs/categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시",
      "title": "3. 경제성·조달·사업 모델"
    },
    {
      "site_type": "제조 공장",
      "item": "예외·성과",
      "link": "docs/categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시",
      "title": "3. 경제성·조달·사업 모델"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시",
      "title": "3. 경제성·조달·사업 모델"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시",
      "title": "3. 경제성·조달·사업 모델"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시",
      "title": "3. 경제성·조달·사업 모델"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시",
      "title": "3. 경제성·조달·사업 모델"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시",
      "title": "3. 경제성·조달·사업 모델"
    },
    {
      "site_type": "상업 시설",
      "item": "예외·성과",
      "link": "docs/categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시",
      "title": "3. 경제성·조달·사업 모델"
    }
  ],
  "standards_updates": [
    {
      "name": "IEC 60300-3-3:2017 신뢰성 관리 — 적용 지침 — 수명주기 비용",
      "kind": "표준",
      "org": "IEC(International Electrotechnical Commission)",
      "url": "https://webstore.iec.ch/en/publication/31206",
      "related_areas": [
        3,
        57
      ],
      "summary": "수명주기 비용 분석의 개념과 적용을 안내하고 품목의 신뢰성 관련 비용을 강조하는 적용 지침 3판(2017-01-27). 유료 표준이라 공식 개요만 확인했다.",
      "ref_id": "ref-1296"
    }
  ],
  "additional_research_requests": [
    "5절: 가정·실외·기타 현장 유형에서 로봇 도입 비용·과금·조달 방식을 보고한 사례가 필요하다. 이번 조사에서 찾지 못해 네 현장 유형만 썼다.",
    "3·6절: 투자 결정 요인·도입 방식 비율(MMH 2026 설문)을 교차 확인할 독립 설문이나 통계가 필요하다. 현재 핵심 수치가 모두 단일 출처다.",
    "5절 병원 사례: Li 외(2026) 본문의 비용 항목·할인율·회수 기간을 확인해야 경제성 결과를 다른 현장과 비교할 수 있다.",
    "6·7절: IEC 60300-3-3 본문 또는 공개 해설로 수명주기 비용 항목 구성과 로봇 도입 적용 사례를 확인할 필요가 있다.",
    "5절 물류창고 사례: AutoStore 그리드 비용 비중(20~40%)과 피킹량 기반 과금 조건을 독립 출처로 확인해야 벤더 주장 표시를 뗄 수 있다.",
    "5절 제조 공장 사례: 협동로봇 투자 회수 기간을 측정 기준과 함께 보고한 독립 자료가 필요하다(1차 검증에서 195일 수치를 삭제함).",
    "11절 oq-162: 2024년 국내 로봇산업 실태조사 보고서 원문의 품목 분류표로 관제 소프트웨어 별도 집계 여부를 확인해야 한다.",
    "6절: 싱가포르 보건부가 RoMi-H 를 공공 의료기관 통합 플랫폼으로 인정했는지 공식 출처로 확인하면 개방 플랫폼 조달 조건 서술을 보강할 수 있다."
  ],
  "fixes_applied": [
    "f3 목표 달성 비율 — 3절 둘째 단락에 사업 목표 달성 74%·미달 21%·모름 5%를 함께 쓰고, 11%는 투자수익률·신뢰성·통합 비용 목표를 놓친 별도 성과 항목으로 따로 적었다.",
    "f2 모집단 기준 — 6절 첫 문장에 도입 방식 비율(하이브리드 53%·전액 구매 37%·서비스형 로봇 11%)이 '현재 로봇을 쓰는 응답자' 기준임을 밝혔다.",
    "f18 195일 삭제 — 투자 회수 기간 195일을 본문·표·5절 사례 어디에도 쓰지 않고, 가격 비율 25~30% 인용만 5절 제조 공장 표의 예외·성과 칸과 8절에 [추정]으로 남겼다.",
    "f20 종합 서술 — 3절 셋째 단락의 종합 추정에서 195일 수치를 근거나 예시로 쓰지 않았다.",
    "ref-1285 서지 — 13절 각주, 8절 목록, reference_updates 의 제목을 'Research Opportunities for Advancing Measurement Science for Manufacturing Robotics (NIST GCR 24-054)'로, 기관에 Messina, E. & Saidi, K. S. 를, 발행일을 2024-06-07로 고쳤다.",
    "f12 지원 분야 — 6절 공공 실증·조달 소제목에 '물류·웨어러블·의료·돌봄 4대 분야와 협동로봇·언택트서비스'로 썼다.",
    "발행일 — 13절 각주와 reference_updates 에서 ref-1293 을 2023-03-08, ref-903 를 2026-01-25, ref-1291 을 2024-02-15 로 적었다(5절 서술에도 반영).",
    "ref-1298 날짜 — 13절 각주 발행일을 2021-11-22(KDI 게재일)로 두고, 8절 서술에 한국무역협회 원게시일 2021-11-17을 확인했다고 남겼다.",
    "원문 미열람 표시 — 13절의 ref-1285·ref-1286·ref-1296 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 세 항목에 source_unopened: true 를 넣었다.",
    "f12·f13 경계 — 6절 소제목을 '공공 실증·조달(외부 제도, 연계 대상)'로 두고, 7절 표 유형 칸과 표 아래 문장, 9절 표 외부 칸에서 두 제도를 재무·구매 쪽 연계 대상으로만 다뤘다.",
    "벤더 주장 병기 — f8 을 쓴 4절 피킹량 기반 과금, 5절 물류창고 표·서술, 6절 과금 목록과 f18 을 쓴 5절 제조 공장 예외·성과 칸·8절에 '[추정] 벤더 주장'을 유지했다.",
    "5절 현장 유형 — 물류창고(f8)·제조 공장(f6·f18·f19)·병원(f10 중국, f11 싱가포르)·상업 시설(f9 한국)로 나누고 사례마다 국가(미특정·미확인 포함)를 밝혔으며, 가정·실외·기타 사례를 찾지 못했다고 절 첫머리에 적고 site_matrix_updates 는 네 현장 유형 칸만 냈다.",
    "용어집 수명주기 비용 분석 — 정의를 '품목의 수명주기 비용을 산정하는 방법으로, IEC 60300-3-3 이 개념과 적용을 안내하며 특히 신뢰성 관련 비용을 강조한다'로 한정하고 획득~폐기 단계 나열을 뺐다.",
    "11절 기존 질문 — oq-129·oq-160·oq-162 를 모두 '열림'으로 유지하고, oq-162 에는 f14·f15 가 요약 기사 기준의 부분 근거이며 보고서 원문은 미확인임을 적었다(open_question_updates 에 해결 변경을 내지 않음).",
    "분량 초과 자동 분리: 3. 경제성·조달·사업 모델 본문 10,415자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,016자"
  ]
}
```

### runs/2026-09-30-19/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/planning-and-business/economics-procurement-and-business-models.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area03-s6.md (1,380자)
    - docs/categories/planning-and-business/economics-procurement-and-business-models.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area03-s8.md (1,281자)
    - docs/categories/planning-and-business/economics-procurement-and-business-models.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area03-s11.md (1,265자)
    - docs/categories/planning-and-business/economics-procurement-and-business-models.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area03-s10.md (1,106자)
    - docs/categories/planning-and-business/economics-procurement-and-business-models.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area03-s7.md (857자)
    - docs/categories/planning-and-business/economics-procurement-and-business-models.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area03-s4.md (817자)
    - docs/categories/planning-and-business/economics-procurement-and-business-models.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area03-s3.md (795자)
```

### runs/2026-09-30-19/pages/categories/planning-and-business/economics-procurement-and-business-models.md

```markdown
---
title: "3. 경제성·조달·사업 모델"
type: area
category: "A. 기획·사업"
area_no: 3
related_areas: [1, 2, 5, 20, 21, 23, 35, 39, 57, 58, 59, 60, 61, 62, 63, 64]
tags: [총소유비용, 투자 회수 기간, 서비스형 로봇, 사용량 기반 과금, 로봇 조달]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-031, ref-1285, ref-1286, ref-1287, ref-947, ref-872, ref-1290, ref-1291, ref-1292, ref-1293, ref-903, ref-1295, ref-1296, ref-1297, ref-1298, ref-1299]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [A. 기획·사업](index.md) › 3. 경제성·조달·사업 모델

# 3. 경제성·조달·사업 모델

!!! info "소속 대분류"
    [A. 기획·사업](index.md) — 핵심 질문:
    어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

투자 효과를 따지고, 로봇·플랫폼을 골라 계약하고, 과금 방식을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **경제성·투자 효과 분석**: 도입 비용·운영비·총소유비용과 기대 효과를 비교해 투자 여부를 판단한다
- **로봇·솔루션 선정·조달**: 요구에 맞춰 로봇과 플랫폼을 평가하고 시범 운영과 계약을 진행한다
- **사업 모델·과금**: 서비스형 로봇(RaaS)·구독·작업당 과금 같은 사업 모델과 사용량 계량을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 4번 영역 ‘성과·경제성·프로세스 개선’에서 왔다. 그 본문은 [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

도입 비용을 넘는 효과가 나오며, 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가? [분류원문]

## 3. 왜 중요한가

로봇 도입을 결정하는 현장은 투자수익률(Return on Investment, ROI)·투자 회수 기간·총소유비용(Total Cost of Ownership, TCO)을 주된 판단 기준으로 쓴다. [사실][^ref-1299]

자세한 내용은 주제 페이지 [3. 경제성·조달·사업 모델 — 왜 중요한가](../../topics/2026/2026-09-30-area03-s3.md)에 있다.

## 4. 핵심 개념과 용어

**투자수익률(ROI)·투자 회수 기간(Payback Period)** — 투자 대비 이익과 초기 투자를 회수하기까지 걸리는 기간으로, 2026년 설문에서 로봇 투자 결정 요인 1·2위였다. [사실][^ref-1299]

자세한 내용은 주제 페이지 [3. 경제성·조달·사업 모델 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area03-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인한 사례는 물류창고·제조 공장·병원·상업 시설 네 현장 유형이며, 가정·실외·기타 현장의 경제성·과금 사례는 찾지 못했다. 사례마다 국가를 밝힌다.

**현장 유형:** 물류창고

**사례:** 피킹량 기반 서비스형 로봇 계약으로 자동화 저장·피킹 설비 도입(피킹 단계. 국가: 특정 현장 없음, 벤더의 일반 계약 설명)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 알루미늄 저장 그리드는 고객이 먼저 사고, 로봇·포트(작업대)·소프트웨어는 피킹량에 따라 월 요금을 내는 구독으로 쓴다. [추정] 벤더 주장[^ref-1292] |
| 제약 | 보통 3~5년 최소 계약과 가동 로봇·포트 수에 따른 월 최소 요금을 둔다. [추정] 벤더 주장[^ref-1292] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

AutoStore 는 선구매하는 그리드가 전체 시스템 비용의 약 20~40%라고 설명하며, 이 비중은 독립 출처로 확인되지 않았다. [추정] 벤더 주장[^ref-1292] 이 계약에서는 요금과 최소 요금이 피킹량과 가동 로봇·포트 수라는 계량값에 걸리므로, 그 값을 누가 재고 어떻게 합의하는지가 운영 문제로 넘어올 것으로 보인다. [추정][^ref-1292]

**현장 유형:** 제조 공장

**사례:** 중소 제조기업의 협동로봇 선정·도입(국가: 가격 비율 인용은 한국 보고서, 선정 사례와 IRaaS 제안의 국가는 미확인)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 디젤 연료 필터 조립 공정 [사실][^ref-1291] |
| 수행 자원 | 협동로봇 후보 12종을 비용을 포함한 가중 기준으로 비교해 고른다. [사실][^ref-1291] |
| 제약 | 중소기업에는 큰 초기 투자, 총소유비용의 불확실성, 전문성 부족이 도입 장벽이다. [사실][^ref-1286] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 한국무역협회 보고서(2021)는 협동로봇 가격이 전통 산업용 로봇의 25~30% 수준이라고 제조사 자료를 인용한다. [추정] 벤더 주장[^ref-1298] |

선정 사례(Heliyon, 2024-02-15)는 에너지와 비용 측면에서 알맞은 협동로봇을 고르는 일을 효과적인 로봇 도입의 장애물 가운데 하나로 본다. [사실][^ref-1291] Buerkle 외(2023)는 중소기업의 도입 장벽을 들며 산업용 로봇을 서비스로 빌려 쓰는 IRaaS 를 제안했다. [사실][^ref-1286]

**현장 유형:** 병원

**사례:** 3차 병원의 약품·검체 배송에 자율이동로봇 도입(국가: 중국)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 약품·검체 [사실][^ref-1290] |
| 수행 자원 | 자율이동로봇(Autonomous Mobile Robot, AMR) 10대. 비교 대상은 인력 19명의 수작업 배송이다. [사실][^ref-1290] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 배송 시간이 수작업 대비 32~36% 줄고 인력 19명보다 7.3배 많은 배송을 했으며, 10년 수명주기 절감액을 692.8만 위안으로 추정했다. [사실][^ref-1290] |

Li 외(Scientific Reports 16, 2026-04)는 단일 기관에서 6개월 병행 대조로 평가하고 민감도 분석으로 경제성을 확인했다고 보고했다. [사실][^ref-1290] 초록만 확인해 비용 항목·할인율은 미확인이며, 한 병원의 결과여서 인건비 조건이 다른 곳에 그대로 옮기기는 어려울 것으로 보인다. [추정][^ref-1290]

**현장 유형:** 병원

**사례:** 공공 의료기관의 로봇 미들웨어 통합자 조달(국가: 싱가포르)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 로봇·소프트웨어·사물인터넷(Internet of Things, IoT) 기기를 [의료 로봇 미들웨어 RoMi-H](../../glossary/robotic-middleware-for-healthcare.md)에 연동하는 일 [사실][^ref-872] |
| 수행 자원 | 창이종합병원 CHART 가 기술 역량·배포 지식을 연 2회 평가해 등재한 시스템 통합자 [사실][^ref-872] |
| 제약 | 공공 의료기관은 로봇·소프트웨어·IoT 연동에 등재된 통합자를 쓰게 되어 있다(2025-05-01 시행). [사실][^ref-872] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

이 [등재 프로그램](../../glossary/empanelment-programme.md)은 통합자 자격을 조달 조건으로 두고, RoMi-H 통합으로 다양한 시스템·기기의 상호운용을 꾀한다. [사실][^ref-872]

**현장 유형:** 상업 시설

**사례:** 식당 서빙로봇의 렌털 도입(국가: 한국)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 식당이 서빙로봇을 구매하거나 월 30만원대 렌털로 들인다. 브이디컴퍼니는 월 29만9천원 상품을, 비로보틱스는 3년 사용 뒤 소유권을 정하는 유예형을 내놓았고 알지티 등도 렌털 상품을 냈다. [사실][^ref-1293] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 기사는 월 렌털 요금을 최저임금 수준의 월 인건비 200만원대와 비교했다. [사실][^ref-1293] |

이 비교는 업체의 상품 조건을 옮긴 보도(2023-03-08)이며, 실제 인건비 절감 효과를 측정한 것은 아니다. [추정][^ref-1293]

## 6. 대표 접근법과 기술

로봇 도입 방식은 전액 자본 지출(CapEx) 구매, 하드웨어 구매와 소프트웨어 구독을 섞은 하이브리드, 서비스형 로봇으로 나뉘며, 현재 로봇을 쓰는 응답자 기준 비율은 각각 37%, 53%, 11%였다. [사실][^ref-1299] 이 설문의 표본은 166명(제조 29%, 운송·창고 21%, 도매 14%, 소매 12%)이고 방법론은 기사 수준으로만 공개되어 있다. [사실][^ref-1299]

자세한 내용은 주제 페이지 [3. 경제성·조달·사업 모델 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area03-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역에 직접 쓰이는 표준은 수명주기 비용 분석 지침 IEC 60300-3-3 이고, 개방 인터페이스 표준·오픈소스 라이선스·통합자 등재 제도·국내 지원·조달 제도가 도입 비용과 조건에 관여하는 것으로 보인다. [추정][^ref-1296][^ref-031]

자세한 내용은 주제 페이지 [3. 경제성·조달·사업 모델 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area03-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 투자 판단 기준을 보인 업계 설문, 서비스형 로봇 사업 모델 연구, 현장 효과를 정량 보고한 병원 연구, 국내 보고서·통계다.

자세한 내용은 주제 페이지 [3. 경제성·조달·사업 모델 — 대표 연구와 자료](../../topics/2026/2026-09-30-area03-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 작업 완료 수·피킹 수·가동 시간 같은 사용량·성과 계량 데이터와 도입 전후 성과 기준선을 기록해 넘기고, 최소 요금·계약 기간 같은 계약 조건을 운영 제약으로 받는다. [추정][^ref-1292][^ref-1299] | 자본 예산·회계 처리·구매 계약·요금 청구·정부 지원 신청(서비스로봇 실증사업·혁신제품 시범구매 포함)은 재무·구매·전사 자원 계획 쪽 연계 대상이다. [추정][^ref-947][^ref-1295] |
| 로봇 자체 지능·제어 | 로봇 선정에 필요한 능력·인터페이스 적합성 정보를 제공하고, 개방 인터페이스를 지켜 로봇 교체·추가 비용을 낮추는 구조를 맡는다. [추정][^ref-031][^ref-1291] | 로봇 하드웨어 가격과 정비는 제조사·통합자가 맡는다. [추정][^ref-1292] |

과금이 사용량에 걸리는 계약에서는 ROP가 기록하는 작업 완료·가동 기록이 요금과 투자 효과 판단의 원천이 될 것으로 보인다. [추정][^ref-1292][^ref-1286] 반면 요금을 청구하고 예산을 집행하는 일은 ROP가 아니라 재무·구매 시스템이 맡는 연계 대상이다. [추정][^ref-1296] 경계를 나누는 기준은 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 비용·효과 판단의 근거를 대는 J. 현장 운영·관제, 통합 비용을 좌우하는 F. 연동, 계약·라이선스를 다루는 P. 거버넌스·법규·사회, 그리고 사례가 모이는 Q. 현장 유형별 적용과 주로 이어지는 것으로 보인다. [추정][^ref-1299][^ref-031][^ref-1292]

자세한 내용은 주제 페이지 [3. 경제성·조달·사업 모델 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area03-s10.md)에 있다.

## 11. 열린 질문

전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [3. 경제성·조달·사업 모델 — 열린 질문](../../topics/2026/2026-09-30-area03-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-1286]: Buerkle, A., Eaton, W., Al-Yacoub, A., Zimmer, M., Kinnell, P., Henshaw, M., Coombes, M., Chen, W.-H., & Lohse, N. (Robotics and Computer-Integrated Manufacturing 81), Towards industrial robots as a service (IRaaS): Flexibility, usability, safety and business models, 2023-06, https://www.sciencedirect.com/science/article/pii/S0736584522001661, 접근일 2026-09-30 (원문 미열람)
[^ref-947]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-30
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30
[^ref-1290]: Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04, https://www.nature.com/articles/s41598-026-49800-9, 접근일 2026-09-30
[^ref-1291]: Sivalingam, C. S., & Subramaniam, S. K. (Heliyon), Cobot selection using hybrid AHP-TOPSIS based multi-criteria decision making technique for fuel filter assembly process, 2024-02-15, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10882119/, 접근일 2026-09-30
[^ref-1292]: AutoStore, Buying vs. RaaS: What's the Best Strategy for Investing in Warehouse Robotics?, 미확인, https://www.autostoresystem.com/insights/buying-vs-raas-whats-the-best-strategy-for-investing-in-warehouse-robotics, 접근일 2026-09-30
[^ref-1293]: 지디넷코리아 (신영빈), '30만원 vs 200만원' 인건비 부담…서빙로봇 판 커진다, 2023-03-08, https://zdnet.co.kr/view/?no=20230307165036, 접근일 2026-09-30
[^ref-1295]: 전자신문, 조달청, 2026년 혁신제품 시범구매 기본계획 발표, 2025-12-18, https://www.etnews.com/20251218000194, 접근일 2026-09-30
[^ref-1296]: IEC (International Electrotechnical Commission), IEC 60300-3-3:2017 Dependability management - Part 3-3: Application guide - Life cycle costing, 2017-01-27, https://webstore.iec.ch/en/publication/31206, 접근일 2026-09-30 (원문 미열람)
[^ref-1298]: 한국무역협회 (KDI 경제정보센터 게재), 협동로봇: 중소기업 스마트 제조의 시작점, 2021-11-22, https://eiec.kdi.re.kr/policy/domesticView.do?ac=0000159915&datecount=&issus=S&pg=&pp=20, 접근일 2026-09-30
[^ref-1299]: Modern Materials Handling (Bridget McCrea; Peerless Research Group·MHI 조사), 2026 Intralogistics Robotics Survey: Robotics moves into the mainstream, 2026-06-01, https://www.mmh.com/article/2026_intralogistics_robotics_survey_robotics_moves_into_the_mainstream, 접근일 2026-09-30
```

### docs/categories/planning-and-business/economics-procurement-and-business-models.md

```markdown
---
title: "3. 경제성·조달·사업 모델"
type: area
category: "A. 기획·사업"
area_no: 3
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [A. 기획·사업](index.md) › 3. 경제성·조달·사업 모델

# 3. 경제성·조달·사업 모델

!!! info "소속 대분류"
    [A. 기획·사업](index.md) — 핵심 질문:
    어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

투자 효과를 따지고, 로봇·플랫폼을 골라 계약하고, 과금 방식을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **경제성·투자 효과 분석**: 도입 비용·운영비·총소유비용과 기대 효과를 비교해 투자 여부를 판단한다
- **로봇·솔루션 선정·조달**: 요구에 맞춰 로봇과 플랫폼을 평가하고 시범 운영과 계약을 진행한다
- **사업 모델·과금**: 서비스형 로봇(RaaS)·구독·작업당 과금 같은 사업 모델과 사용량 계량을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 4번 영역 ‘성과·경제성·프로세스 개선’에서 왔다. 그 본문은 [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

도입 비용을 넘는 효과가 나오며, 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가? [분류원문]

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

### runs/2026-09-30-19/pages/topics/2026/2026-09-30-area03-s6.md

```markdown
---
title: "3. 경제성·조달·사업 모델 — 대표 접근법과 기술"
type: topic
category: "A. 기획·사업"
primary_area_no: 3
related_areas: [1, 2, 5, 20, 21, 23, 35, 39, 57, 58, 59, 60, 61, 62, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1286, ref-1287, ref-947, ref-872, ref-1291, ref-1292, ref-1293, ref-1295, ref-1296, ref-1299]
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/economics-procurement-and-business-models.md#6
---

[홈](../../index.md) › [주제](../index.md) › 3. 경제성·조달·사업 모델 — 대표 접근법과 기술

# 3. 경제성·조달·사업 모델 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇 도입 방식은 전액 자본 지출(CapEx) 구매, 하드웨어 구매와 소프트웨어 구독을 섞은 하이브리드, 서비스형 로봇으로 나뉘며, 현재 로봇을 쓰는 응답자 기준 비율은 각각 37%, 53%, 11%였다. [사실][^ref-1299] 이 설문의 표본은 166명(제조 29%, 운송·창고 21%, 도매 14%, 소매 12%)이고 방법론은 기사 수준으로만 공개되어 있다. [사실][^ref-1299]
- 이 페이지는 [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇 도입 방식은 전액 자본 지출(CapEx) 구매, 하드웨어 구매와 소프트웨어 구독을 섞은 하이브리드, 서비스형 로봇으로 나뉘며, 현재 로봇을 쓰는 응답자 기준 비율은 각각 37%, 53%, 11%였다. [사실][^ref-1299] 이 설문의 표본은 166명(제조 29%, 운송·창고 21%, 도매 14%, 소매 12%)이고 방법론은 기사 수준으로만 공개되어 있다. [사실][^ref-1299]

### 수명주기 비용 분석

IEC 60300-3-3:2017 은 수명주기 비용의 개념과 적용을 경영자·엔지니어·재무 담당·계약자에게 안내하는 적용 지침이다. [사실][^ref-1296] 유료 표준이라 본문은 확인하지 못했고, 로봇 도입에 적용한 사례도 이번 조사에서 찾지 못했다.

### 다기준 선정

Sivalingam·Subramaniam(2024)은 계층 분석법(Analytic Hierarchy Process, AHP)으로 비용을 포함한 기준의 가중치를 정하고 TOPSIS(Technique for Order of Preference by Similarity to Ideal Solution)로 협동로봇 12종의 순위를 매겼다. [사실][^ref-1291]

### 과금·사업 모델

- IRaaS 제안은 사업 모델을 시간 기반과 사용량 기반으로 나눈다. [사실][^ref-1286]
- 물류창고 설비의 피킹량 기반 월 구독은 선구매 그리드와 3~5년 최소 계약을 함께 둔다. [추정] 벤더 주장[^ref-1292]
- 한국 식당 서빙로봇 시장에는 구매·렌털 선택형과 3년 사용 뒤 소유권을 정하는 유예형이 있다. [사실][^ref-1293]
- Lee·Aswani(2025)는 작업마다 가격을 제시하고 고객이 수락·거절하며 로봇이 확률적으로 열화하는 상황에서, 데이터 기반 수요 추정과 마르코프 결정 과정으로 가격과 교체 정책을 함께 구했다. [사실][^ref-1287] 이 연구는 동료 심사 전 프리프린트다. [사실][^ref-1287]

### 공공 실증·조달(외부 제도, 연계 대상)

국비 실증 지원과 공공 시범구매는 도입 재원과 조건을 정하는 외부 제도로, ROP 기능이 아니라 재무·구매 쪽 연계 대상이다. [추정][^ref-947][^ref-1295] 한국로봇산업진흥원의 서비스로봇 실증사업(2020년부터)은 물류·웨어러블·의료·돌봄 4대 분야와 협동로봇·언택트서비스에 로봇 도입 비용의 50% 이내를 국비로 지원하고, 민간 부담 총사업비 50% 이상(현금, 수요기관 25% 이상)을 요구하며, 서류·발표·현장 평가로 과제를 뽑아 중간 점검과 최종 평가를 거친다(확인일 2026-09-30). [사실][^ref-947] 조달청의 2026년 혁신제품 시범구매 기본계획은 예산을 전년 529억원에서 839억원으로 늘리고 로봇·드론·스마트팩토리 같은 AI 융복합 제품을 중점으로 하며, 시범 사용 뒤 관리·활용 여부를 점검한다. [사실][^ref-1295]

### 개방 인터페이스와 인증 통합자를 조달 조건으로

VDA 5050 3.0.0 명세는 이동로봇을 플릿 관제에 연결하는 복잡도를 줄이고 여러 제조사의 이기종 이동로봇 플릿이 같은 공간에서 조율되어 운영되게 하는 것을 목표로 든다. [사실][^ref-031] 싱가포르 공공 의료기관은 로봇 연동에 등재된 통합자를 쓰게 되어 있다. [사실][^ref-872] 이런 조건은 이기종 통합 비용을 줄이는 조달 수단으로 쓰일 수 있을 것으로 보이나, 그 효과를 측정한 자료는 찾지 못했다. [추정][^ref-872][^ref-031]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-1286]: Buerkle, A., Eaton, W., Al-Yacoub, A., Zimmer, M., Kinnell, P., Henshaw, M., Coombes, M., Chen, W.-H., & Lohse, N. (Robotics and Computer-Integrated Manufacturing 81), Towards industrial robots as a service (IRaaS): Flexibility, usability, safety and business models, 2023-06, https://www.sciencedirect.com/science/article/pii/S0736584522001661, 접근일 2026-09-30 (원문 미열람)
[^ref-1287]: Lee, J. S., & Aswani, A. (arXiv), Profit Maximization for a Robotics-as-a-Service Model, 2025-09-30, https://arxiv.org/abs/2509.26595, 접근일 2026-09-30
[^ref-947]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-30
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30
[^ref-1291]: Sivalingam, C. S., & Subramaniam, S. K. (Heliyon), Cobot selection using hybrid AHP-TOPSIS based multi-criteria decision making technique for fuel filter assembly process, 2024-02-15, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10882119/, 접근일 2026-09-30
[^ref-1292]: AutoStore, Buying vs. RaaS: What's the Best Strategy for Investing in Warehouse Robotics?, 미확인, https://www.autostoresystem.com/insights/buying-vs-raas-whats-the-best-strategy-for-investing-in-warehouse-robotics, 접근일 2026-09-30
[^ref-1293]: 지디넷코리아 (신영빈), '30만원 vs 200만원' 인건비 부담…서빙로봇 판 커진다, 2023-03-08, https://zdnet.co.kr/view/?no=20230307165036, 접근일 2026-09-30
[^ref-1295]: 전자신문, 조달청, 2026년 혁신제품 시범구매 기본계획 발표, 2025-12-18, https://www.etnews.com/20251218000194, 접근일 2026-09-30
[^ref-1296]: IEC (International Electrotechnical Commission), IEC 60300-3-3:2017 Dependability management - Part 3-3: Application guide - Life cycle costing, 2017-01-27, https://webstore.iec.ch/en/publication/31206, 접근일 2026-09-30 (원문 미열람)
[^ref-1299]: Modern Materials Handling (Bridget McCrea; Peerless Research Group·MHI 조사), 2026 Intralogistics Robotics Survey: Robotics moves into the mainstream, 2026-06-01, https://www.mmh.com/article/2026_intralogistics_robotics_survey_robotics_moves_into_the_mainstream, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-19 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-19 | 3. 경제성·조달·사업 모델 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-19/pages/topics/2026/2026-09-30-area03-s8.md

```markdown
---
title: "3. 경제성·조달·사업 모델 — 대표 연구와 자료"
type: topic
category: "A. 기획·사업"
primary_area_no: 3
related_areas: [1, 2, 5, 20, 21, 23, 35, 39, 57, 58, 59, 60, 61, 62, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1285, ref-1286, ref-1287, ref-1290, ref-1291, ref-903, ref-1298, ref-1299]
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/economics-procurement-and-business-models.md#8
---

[홈](../../index.md) › [주제](../index.md) › 3. 경제성·조달·사업 모델 — 대표 연구와 자료

# 3. 경제성·조달·사업 모델 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대표 자료는 투자 판단 기준을 보인 업계 설문, 서비스형 로봇 사업 모델 연구, 현장 효과를 정량 보고한 병원 연구, 국내 보고서·통계다.
- 이 페이지는 [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대표 자료는 투자 판단 기준을 보인 업계 설문, 서비스형 로봇 사업 모델 연구, 현장 효과를 정량 보고한 병원 연구, 국내 보고서·통계다.

- Modern Materials Handling(Peerless Research Group·MHI 조사), 2026 Intralogistics Robotics Survey(2026) — 로봇 투자 결정 요인, 도입 방식, 목표 달성 여부를 보고한 설문으로, 표본 166명에 방법론은 기사 수준으로만 공개됐다. [사실][^ref-1299]
- Messina, E.·Saidi, K. S.(NIST), Research Opportunities for Advancing Measurement Science for Manufacturing Robotics(NIST GCR 24-054, 2024) — 투자수익률을 로봇 도입의 최대 과제로 들고, 서비스형 로봇이 초기 투자와 위험을 줄이는 방식으로 매력적이라고 서술한다. 본문은 추출하지 못해 원문 미열람이다. [사실][^ref-1285]
- Buerkle 외, Towards industrial robots as a service (IRaaS)(2023) — 유연성·사용성·안전·사업 모델 네 요소와 시간·사용량 기반 모델을 제안한다. [사실][^ref-1286]
- Lee·Aswani, Profit Maximization for a Robotics-as-a-Service Model(2025, 프리프린트) — 서비스형 로봇 제공자의 작업별 가격과 로봇 교체 결정을 함께 최적화한다. [사실][^ref-1287]
- Li 외, 병원 약품·검체 배송 물류 로봇의 적용 관리와 효과 분석(Scientific Reports, 2026) — 병원 자율이동로봇의 병행 대조 평가와 10년 경제성 추정을 보고한다. [사실][^ref-1290]
- Sivalingam·Subramaniam, AHP–TOPSIS 기반 협동로봇 선정(Heliyon, 2024) — 비용을 포함한 다기준 의사결정으로 조립 공정용 협동로봇을 고른다. [사실][^ref-1291]
- 한국무역협회, 협동로봇: 중소기업 스마트 제조의 시작점(2021) — 협동로봇 가격이 전통 산업용 로봇의 25~30% 수준이라는 제조사 자료 기반 수치를 인용한다. [추정] 벤더 주장[^ref-1298] KDI 경제정보센터 게재일은 2021-11-22, 한국무역협회 원게시일은 2021-11-17로 확인됐다. [사실][^ref-1298]
- 로봇신문, 2024년 국내 로봇산업 실태조사 요약(2026-01-25) — 산업통상부·한국로봇산업진흥원·한국AI·로봇산업협회 조사(2024년 말 기준)에서 로봇산업 매출은 6조1695억원이며 제조업용 로봇 3조1075억원, 로봇부품 및 소프트웨어 1조9810억원, 전문서비스용 로봇 6423억원, 개인서비스용 로봇 4386억원이다. [사실][^ref-903]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1285]: Messina, E. & Saidi, K. S. (NIST, National Institute of Standards and Technology), Research Opportunities for Advancing Measurement Science for Manufacturing Robotics (NIST GCR 24-054), 2024-06-07, https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958147, 접근일 2026-09-30 (원문 미열람)
[^ref-1286]: Buerkle, A., Eaton, W., Al-Yacoub, A., Zimmer, M., Kinnell, P., Henshaw, M., Coombes, M., Chen, W.-H., & Lohse, N. (Robotics and Computer-Integrated Manufacturing 81), Towards industrial robots as a service (IRaaS): Flexibility, usability, safety and business models, 2023-06, https://www.sciencedirect.com/science/article/pii/S0736584522001661, 접근일 2026-09-30 (원문 미열람)
[^ref-1287]: Lee, J. S., & Aswani, A. (arXiv), Profit Maximization for a Robotics-as-a-Service Model, 2025-09-30, https://arxiv.org/abs/2509.26595, 접근일 2026-09-30
[^ref-1290]: Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04, https://www.nature.com/articles/s41598-026-49800-9, 접근일 2026-09-30
[^ref-1291]: Sivalingam, C. S., & Subramaniam, S. K. (Heliyon), Cobot selection using hybrid AHP-TOPSIS based multi-criteria decision making technique for fuel filter assembly process, 2024-02-15, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10882119/, 접근일 2026-09-30
[^ref-903]: 로봇신문, [Cover Story] '2024년 국내 로봇산업 실태 조사 결과 보고서' 요약, 2026-01-25, https://www.irobotnews.com/news/articleView.html?idxno=44544, 접근일 2026-09-30
[^ref-1298]: 한국무역협회 (KDI 경제정보센터 게재), 협동로봇: 중소기업 스마트 제조의 시작점, 2021-11-22, https://eiec.kdi.re.kr/policy/domesticView.do?ac=0000159915&datecount=&issus=S&pg=&pp=20, 접근일 2026-09-30
[^ref-1299]: Modern Materials Handling (Bridget McCrea; Peerless Research Group·MHI 조사), 2026 Intralogistics Robotics Survey: Robotics moves into the mainstream, 2026-06-01, https://www.mmh.com/article/2026_intralogistics_robotics_survey_robotics_moves_into_the_mainstream, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-19 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-19 | 3. 경제성·조달·사업 모델 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-19/pages/topics/2026/2026-09-30-area03-s11.md

```markdown
---
title: "3. 경제성·조달·사업 모델 — 열린 질문"
type: topic
category: "A. 기획·사업"
primary_area_no: 3
related_areas: [1, 2, 5, 20, 21, 23, 35, 39, 57, 58, 59, 60, 61, 62, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-903]
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/economics-procurement-and-business-models.md#11
---

[홈](../../index.md) › [주제](../index.md) › 3. 경제성·조달·사업 모델 — 열린 질문

# 3. 경제성·조달·사업 모델 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-129** (상태: 열림) 채팅으로 정한 로봇 대수를 시뮬레이션 기반 대수 산정과 어떻게 연결하고, 처리량 최대화와 비용 최소화 가운데 어느 목적을 누가 정하는가? 이번 조사에서 새 근거를 찾지 못했다.
- **oq-160** (상태: 열림) 다중 플릿 오케스트레이션 소프트웨어 시장의 규모·성장률에 대해 산정 방법론이 공개된 독립 출처가 있는가? 이번 조사에서도 찾지 못했다.
- **oq-162** (상태: 열림) 국내 로봇산업 실태조사에 오케스트레이션·관제 소프트웨어 매출을 따로 집계하는 항목이 있는가, 없다면 국내 관제 소프트웨어 시장 규모를 어떤 자료로 추적할 것인가? 2024년 실태조사를 요약한 기사에는 로봇부품 및 소프트웨어의 세부 품목이 구동용·제어용·기타 부품뿐이고 소프트웨어 세부 항목이 보이지 않아 부분 근거만 있으며, 보고서 원문의 품목 분류표는 미확인이다. [추정][^ref-903]
- **oq-257** (상태: 열림) 물류창고·공장 가상 시운전의 효과(프로젝트 기간·현장 시운전 기간 단축)를 벤더 사례가 아닌 독립 연구가 같은 기준선으로 측정한 결과가 있는가?
- **새 질문** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-19) ROP 같은 다중 제조사 오케스트레이션 플랫폼의 과금 단위(로봇당·작업당·현장당·구독)를 비교하거나 공개한 자료가 있는가?
- **새 질문** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-19) 사용량 기반 서비스형 로봇 계약에서 과금·최소 요금·가동률 미달을 판정하는 계량 데이터를 누가 측정하고, 여러 사업자가 함께 쓰는 현장에서 그 값을 어떻게 합의하는가?
- **새 질문** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-19) 병원 배송 로봇 경제성 평가의 비용 항목·할인율·인건비 산정 방식을 비교 가능한 기준으로 정리한 연구가 있으며, 국내 병원 인건비 조건에서도 같은 결론이 나오는가?
- **새 질문** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-19) 국내 공공·민간 로봇 조달에서 VDA 5050 같은 개방 인터페이스 적합성이나 통합자 인증을 입찰 요구조건으로 명시한 사례가 있는가?
- **새 질문** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-19) 이기종 로봇 통합 비용이 로봇 도입 총소유비용에서 차지하는 비중과, 공통 인터페이스·오케스트레이션 플랫폼이 그 비용을 얼마나 줄이는지 측정한 독립 연구가 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-903]: 로봇신문, [Cover Story] '2024년 국내 로봇산업 실태 조사 결과 보고서' 요약, 2026-01-25, https://www.irobotnews.com/news/articleView.html?idxno=44544, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-19 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-19 | 3. 경제성·조달·사업 모델 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-19/pages/topics/2026/2026-09-30-area03-s10.md

```markdown
---
title: "3. 경제성·조달·사업 모델 — 다른 연구영역과의 연결"
type: topic
category: "A. 기획·사업"
primary_area_no: 3
related_areas: [1, 2, 5, 20, 21, 23, 35, 39, 57, 58, 59, 60, 61, 62, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1286, ref-1287, ref-872, ref-1290, ref-1291, ref-1292, ref-1293, ref-903, ref-1296, ref-1297, ref-1298, ref-1299]
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/economics-procurement-and-business-models.md#10
---

[홈](../../index.md) › [주제](../index.md) › 3. 경제성·조달·사업 모델 — 다른 연구영역과의 연결

# 3. 경제성·조달·사업 모델 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 비용·효과 판단의 근거를 대는 J. 현장 운영·관제, 통합 비용을 좌우하는 F. 연동, 계약·라이선스를 다루는 P. 거버넌스·법규·사회, 그리고 사례가 모이는 Q. 현장 유형별 적용과 주로 이어지는 것으로 보인다. [추정][^ref-1299][^ref-031][^ref-1292]
- 이 페이지는 [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 비용·효과 판단의 근거를 대는 J. 현장 운영·관제, 통합 비용을 좌우하는 F. 연동, 계약·라이선스를 다루는 P. 거버넌스·법규·사회, 그리고 사례가 모이는 Q. 현장 유형별 적용과 주로 이어지는 것으로 보인다. [추정][^ref-1299][^ref-031][^ref-1292]

- [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md) — 국내 로봇산업 매출 통계가 관제·오케스트레이션 소프트웨어를 따로 집계하는지가 두 영역에 걸친다. [추정][^ref-903]
- [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) — 도입 효과를 판단하는 수용 기준이 사용 사례와 요구에서 정해진다. [추정][^ref-1299]
- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — 로봇 선정의 비교 기준이 로봇 능력 표현과 이어진다. [추정][^ref-1291]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 통합 비용이 투자 목표 미달 사유로 꼽히며 제조사 관제 연동 방식이 그 비용과 이어진다. [추정][^ref-1299][^ref-031]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — 개방 인터페이스 준수와 통합자 인증이 조달 조건이 될 수 있다. [추정][^ref-031][^ref-872]
- [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) — 과금·성과 데이터를 재무·구매 시스템에 넘기는 연동이 필요하다. [추정][^ref-1292]
- [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md) — 로봇 대수 산정에서 처리량과 비용 가운데 어느 목적을 누가 정하는지가 [열린 질문](../../open-questions.md) oq-129 로 남아 있다.
- [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) — 도입 전후 성과 기준선과 투자 목표 달성 판단이 성과 측정에 기댄다. [추정][^ref-1299]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 수명주기 비용과 열화 로봇의 교체 결정이 자산 수명주기 관리와 이어진다. [추정][^ref-1296][^ref-1287]
- [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) — 최소 계약 기간·최소 요금 같은 계약 조건과 계량값 합의가 다사업자 계약 문제로 넘어간다. [추정][^ref-1292]
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — 오픈소스 관제 구성요소의 라이선스가 조달 조건에 들어간다. [추정][^ref-1297]
- [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) — 서빙로봇 렌털 요금을 인건비와 비교하는 인력 대체 논의가 이어진다. [추정][^ref-1293]
- [61. 물류창고](../../categories/site-type-applications/warehouse.md) — 피킹량 기반 과금 계약 사례가 놓이는 현장이다. [추정][^ref-1292]
- [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md) — 협동로봇 선정·가격과 IRaaS 제안이 놓이는 현장이다. [추정][^ref-1291][^ref-1298][^ref-1286]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 병원 배송 로봇 경제성 평가와 통합자 등재 제도가 놓이는 현장이다. [추정][^ref-1290][^ref-872]
- [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) — 식당 서빙로봇 렌털 사례가 놓이는 현장이다. [추정][^ref-1293]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-1286]: Buerkle, A., Eaton, W., Al-Yacoub, A., Zimmer, M., Kinnell, P., Henshaw, M., Coombes, M., Chen, W.-H., & Lohse, N. (Robotics and Computer-Integrated Manufacturing 81), Towards industrial robots as a service (IRaaS): Flexibility, usability, safety and business models, 2023-06, https://www.sciencedirect.com/science/article/pii/S0736584522001661, 접근일 2026-09-30 (원문 미열람)
[^ref-1287]: Lee, J. S., & Aswani, A. (arXiv), Profit Maximization for a Robotics-as-a-Service Model, 2025-09-30, https://arxiv.org/abs/2509.26595, 접근일 2026-09-30
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30
[^ref-1290]: Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04, https://www.nature.com/articles/s41598-026-49800-9, 접근일 2026-09-30
[^ref-1291]: Sivalingam, C. S., & Subramaniam, S. K. (Heliyon), Cobot selection using hybrid AHP-TOPSIS based multi-criteria decision making technique for fuel filter assembly process, 2024-02-15, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10882119/, 접근일 2026-09-30
[^ref-1292]: AutoStore, Buying vs. RaaS: What's the Best Strategy for Investing in Warehouse Robotics?, 미확인, https://www.autostoresystem.com/insights/buying-vs-raas-whats-the-best-strategy-for-investing-in-warehouse-robotics, 접근일 2026-09-30
[^ref-1293]: 지디넷코리아 (신영빈), '30만원 vs 200만원' 인건비 부담…서빙로봇 판 커진다, 2023-03-08, https://zdnet.co.kr/view/?no=20230307165036, 접근일 2026-09-30
[^ref-903]: 로봇신문, [Cover Story] '2024년 국내 로봇산업 실태 조사 결과 보고서' 요약, 2026-01-25, https://www.irobotnews.com/news/articleView.html?idxno=44544, 접근일 2026-09-30
[^ref-1296]: IEC (International Electrotechnical Commission), IEC 60300-3-3:2017 Dependability management - Part 3-3: Application guide - Life cycle costing, 2017-01-27, https://webstore.iec.ch/en/publication/31206, 접근일 2026-09-30 (원문 미열람)
[^ref-1297]: Open-RMF (open-rmf/rmf_ros2 저장소), rmf_ros2/rmf_fleet_adapter/package.xml, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/package.xml, 접근일 2026-09-30
[^ref-1298]: 한국무역협회 (KDI 경제정보센터 게재), 협동로봇: 중소기업 스마트 제조의 시작점, 2021-11-22, https://eiec.kdi.re.kr/policy/domesticView.do?ac=0000159915&datecount=&issus=S&pg=&pp=20, 접근일 2026-09-30
[^ref-1299]: Modern Materials Handling (Bridget McCrea; Peerless Research Group·MHI 조사), 2026 Intralogistics Robotics Survey: Robotics moves into the mainstream, 2026-06-01, https://www.mmh.com/article/2026_intralogistics_robotics_survey_robotics_moves_into_the_mainstream, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-19 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-19 | 3. 경제성·조달·사업 모델 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-19/pages/topics/2026/2026-09-30-area03-s7.md

```markdown
---
title: "3. 경제성·조달·사업 모델 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "A. 기획·사업"
primary_area_no: 3
related_areas: [1, 2, 5, 20, 21, 23, 35, 39, 57, 58, 59, 60, 61, 62, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-947, ref-872, ref-1295, ref-1296, ref-1297]
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/economics-procurement-and-business-models.md#7
---

[홈](../../index.md) › [주제](../index.md) › 3. 경제성·조달·사업 모델 — 관련 표준·프레임워크·오픈소스

# 3. 경제성·조달·사업 모델 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에 직접 쓰이는 표준은 수명주기 비용 분석 지침 IEC 60300-3-3 이고, 개방 인터페이스 표준·오픈소스 라이선스·통합자 등재 제도·국내 지원·조달 제도가 도입 비용과 조건에 관여하는 것으로 보인다. [추정][^ref-1296][^ref-031]
- 이 페이지는 [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에 직접 쓰이는 표준은 수명주기 비용 분석 지침 IEC 60300-3-3 이고, 개방 인터페이스 표준·오픈소스 라이선스·통합자 등재 제도·국내 지원·조달 제도가 도입 비용과 조건에 관여하는 것으로 보인다. [추정][^ref-1296][^ref-031]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| IEC 60300-3-3:2017 신뢰성 관리 — 적용 지침 — 수명주기 비용 | 표준 | 수명주기 비용 분석의 개념과 적용을 안내하는 3판(2017-01-27 발행)으로, 신뢰성 관련 비용을 강조한다. [사실][^ref-1296] | IEC 웹스토어 개요(원문 미열람) |
| [VDA 5050](../../glossary/vda-5050.md) 3.0.0 | 표준 | 이동로봇을 플릿 관제에 연결하는 복잡도를 줄이고 이기종 플릿의 공동 운영을 목표로 든다. [사실][^ref-031] | 공식 명세 저장소 |
| [Open-RMF](../../glossary/open-rmf.md) 플릿 어댑터(rmf_fleet_adapter 2.14.0) | 오픈소스 | Apache License 2.0 으로 배포된다(확인일 2026-09-30). [사실][^ref-1297] | 공식 저장소 package.xml |
| RoMi-H 등재 프로그램 | 평가 프로그램 | 싱가포르 공공 의료기관의 로봇 통합자 자격을 연 2회 평가·등재한다. [사실][^ref-872] | CHART 안내 |
| 서비스로봇 실증사업 | 평가 프로그램(외부 제도, 연계 대상) | 로봇 도입 비용의 50% 이내를 국비로 지원하는 도입 재원 제도다. [사실][^ref-947] | 한국로봇산업진흥원 |
| 혁신제품 시범구매(2026년 기본계획) | 공공 조달 제도(연계 대상) | 로봇 등 AI 융복합 제품을 중점으로 한 공공 시범구매다. [사실][^ref-1295] | 전자신문 보도 |

뒤의 두 제도는 도입 조건과 재원을 정하는 외부 제도로 다루며 ROP 기능으로 보지 않는다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-947]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-30
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30
[^ref-1295]: 전자신문, 조달청, 2026년 혁신제품 시범구매 기본계획 발표, 2025-12-18, https://www.etnews.com/20251218000194, 접근일 2026-09-30
[^ref-1296]: IEC (International Electrotechnical Commission), IEC 60300-3-3:2017 Dependability management - Part 3-3: Application guide - Life cycle costing, 2017-01-27, https://webstore.iec.ch/en/publication/31206, 접근일 2026-09-30 (원문 미열람)
[^ref-1297]: Open-RMF (open-rmf/rmf_ros2 저장소), rmf_ros2/rmf_fleet_adapter/package.xml, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/package.xml, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-19 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-19 | 3. 경제성·조달·사업 모델 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-19/pages/topics/2026/2026-09-30-area03-s4.md

```markdown
---
title: "3. 경제성·조달·사업 모델 — 핵심 개념과 용어"
type: topic
category: "A. 기획·사업"
primary_area_no: 3
related_areas: [1, 2, 5, 20, 21, 23, 35, 39, 57, 58, 59, 60, 61, 62, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1285, ref-1286, ref-1287, ref-1292, ref-1296, ref-1299]
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/economics-procurement-and-business-models.md#4
---

[홈](../../index.md) › [주제](../index.md) › 3. 경제성·조달·사업 모델 — 핵심 개념과 용어

# 3. 경제성·조달·사업 모델 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **투자수익률(ROI)·투자 회수 기간(Payback Period)** — 투자 대비 이익과 초기 투자를 회수하기까지 걸리는 기간으로, 2026년 설문에서 로봇 투자 결정 요인 1·2위였다. [사실][^ref-1299]
- 이 페이지는 [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **투자수익률(ROI)·투자 회수 기간(Payback Period)** — 투자 대비 이익과 초기 투자를 회수하기까지 걸리는 기간으로, 2026년 설문에서 로봇 투자 결정 요인 1·2위였다. [사실][^ref-1299]
- **총소유비용(TCO)** — 구입 비용만이 아니라 보유·운영 기간 전체의 비용을 보는 기준으로, 같은 설문의 결정 요인 3위(47%)였다. [사실][^ref-1299] 중소기업에는 총소유비용의 불확실성 자체가 로봇 도입 장벽으로 꼽힌다. [사실][^ref-1286]
- **수명주기 비용 분석(Life Cycle Costing, LCC)** — 품목의 수명주기 비용을 산정하는 방법이다. IEC 60300-3-3:2017(3판)은 그 개념과 적용을 안내하며 특히 품목의 신뢰성(dependability) 관련 비용을 강조한다. [사실][^ref-1296]
- **[서비스형 로봇](../../glossary/robot-as-a-service.md)(Robot-as-a-Service, RaaS)** — 로봇을 사지 않고 서비스로 쓰는 방식으로, 초기 투자와 위험을 줄이는 방법으로 거론된다. [사실][^ref-1285] 산업용 로봇 서비스(Industrial Robots as a Service, IRaaS) 제안은 사업 모델을 시간 기반과 사용량 기반으로 나눈다. [사실][^ref-1286]
- **하이브리드 도입** — 하드웨어는 사고 소프트웨어는 구독하는 방식이다. [사실][^ref-1299]
- **피킹량 기반 과금(Pay-per-pick)** — 자동화 창고의 로봇·작업대·소프트웨어 사용료를 처리한 피킹 수에 따라 매기는 방식이다. [추정] 벤더 주장[^ref-1292]
- **작업별 가격·교체 결정** — 서비스형 로봇 제공자가 작업마다 가격을 제시하고 열화한 로봇의 교체 시점을 함께 정하는 문제로, 마르코프 결정 과정(Markov Decision Process, MDP)으로 모델링한 연구가 있다. [사실][^ref-1287]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1285]: Messina, E. & Saidi, K. S. (NIST, National Institute of Standards and Technology), Research Opportunities for Advancing Measurement Science for Manufacturing Robotics (NIST GCR 24-054), 2024-06-07, https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958147, 접근일 2026-09-30 (원문 미열람)
[^ref-1286]: Buerkle, A., Eaton, W., Al-Yacoub, A., Zimmer, M., Kinnell, P., Henshaw, M., Coombes, M., Chen, W.-H., & Lohse, N. (Robotics and Computer-Integrated Manufacturing 81), Towards industrial robots as a service (IRaaS): Flexibility, usability, safety and business models, 2023-06, https://www.sciencedirect.com/science/article/pii/S0736584522001661, 접근일 2026-09-30 (원문 미열람)
[^ref-1287]: Lee, J. S., & Aswani, A. (arXiv), Profit Maximization for a Robotics-as-a-Service Model, 2025-09-30, https://arxiv.org/abs/2509.26595, 접근일 2026-09-30
[^ref-1292]: AutoStore, Buying vs. RaaS: What's the Best Strategy for Investing in Warehouse Robotics?, 미확인, https://www.autostoresystem.com/insights/buying-vs-raas-whats-the-best-strategy-for-investing-in-warehouse-robotics, 접근일 2026-09-30
[^ref-1296]: IEC (International Electrotechnical Commission), IEC 60300-3-3:2017 Dependability management - Part 3-3: Application guide - Life cycle costing, 2017-01-27, https://webstore.iec.ch/en/publication/31206, 접근일 2026-09-30 (원문 미열람)
[^ref-1299]: Modern Materials Handling (Bridget McCrea; Peerless Research Group·MHI 조사), 2026 Intralogistics Robotics Survey: Robotics moves into the mainstream, 2026-06-01, https://www.mmh.com/article/2026_intralogistics_robotics_survey_robotics_moves_into_the_mainstream, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-19 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-19 | 3. 경제성·조달·사업 모델 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-19/pages/topics/2026/2026-09-30-area03-s3.md

```markdown
---
title: "3. 경제성·조달·사업 모델 — 왜 중요한가"
type: topic
category: "A. 기획·사업"
primary_area_no: 3
related_areas: [1, 2, 5, 20, 21, 23, 35, 39, 57, 58, 59, 60, 61, 62, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1285, ref-872, ref-1290, ref-1292, ref-1293, ref-1299]
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/economics-procurement-and-business-models.md#3
---

[홈](../../index.md) › [주제](../index.md) › 3. 경제성·조달·사업 모델 — 왜 중요한가

# 3. 경제성·조달·사업 모델 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇 도입을 결정하는 현장은 투자수익률(Return on Investment, ROI)·투자 회수 기간·총소유비용(Total Cost of Ownership, TCO)을 주된 판단 기준으로 쓴다. [사실][^ref-1299]
- 이 페이지는 [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇 도입을 결정하는 현장은 투자수익률(Return on Investment, ROI)·투자 회수 기간·총소유비용(Total Cost of Ownership, TCO)을 주된 판단 기준으로 쓴다. [사실][^ref-1299] Modern Materials Handling 이 Peerless Research Group·MHI 와 함께 한 2026년 사내 물류 로봇 설문(응답 166명, 2026년 3~4월 조사)에서 투자 결정 요인은 투자수익률 63%, 회수 기간 52%, 총소유비용 47%, 공정 성과 41% 순이었다. [사실][^ref-1299] 미국 국립표준기술연구소(National Institute of Standards and Technology, NIST)의 위탁 보고서(2024-06-07)도 로봇 도입의 가장 큰 과제로 투자수익률을 찾고 달성하는 일을 들었다. [사실][^ref-1285]

같은 설문에서 로봇 투자가 사업 목표를 달성했다는 응답은 74%, 달성하지 못했다는 응답은 21%, 모른다는 응답은 5%였다. [사실][^ref-1299] 이와 별개의 성과 항목에서 응답자 11%는 투자수익률·신뢰성·통합 비용 목표를 놓쳤다고 답했다. [사실][^ref-1299] 통합 비용이 목표 미달 사유로 함께 꼽힌다는 점은 여러 제조사의 로봇을 잇는 ROP의 비용 구조와 맞닿는 것으로 보인다. [추정][^ref-1299]

확인한 자료를 종합하면 판단 기준과 조달 방식(구매·하이브리드·서비스형 로봇)은 드러나지만, 병원·식당·창고에서 보고된 효과 수치는 대부분 단일 사례나 벤더 수치여서 같은 기준선으로 비교한 독립 자료는 부족한 것으로 보인다. [추정][^ref-1299][^ref-1290][^ref-1293][^ref-1292] 이기종 통합 비용과 특정 업체 종속을 줄이려고 개방 인터페이스나 인증된 통합자를 조달 조건으로 두는 사례도 있는 것으로 보인다. [추정][^ref-872][^ref-031]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/economics-procurement-and-business-models.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-1285]: Messina, E. & Saidi, K. S. (NIST, National Institute of Standards and Technology), Research Opportunities for Advancing Measurement Science for Manufacturing Robotics (NIST GCR 24-054), 2024-06-07, https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958147, 접근일 2026-09-30 (원문 미열람)
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30
[^ref-1290]: Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04, https://www.nature.com/articles/s41598-026-49800-9, 접근일 2026-09-30
[^ref-1292]: AutoStore, Buying vs. RaaS: What's the Best Strategy for Investing in Warehouse Robotics?, 미확인, https://www.autostoresystem.com/insights/buying-vs-raas-whats-the-best-strategy-for-investing-in-warehouse-robotics, 접근일 2026-09-30
[^ref-1293]: 지디넷코리아 (신영빈), '30만원 vs 200만원' 인건비 부담…서빙로봇 판 커진다, 2023-03-08, https://zdnet.co.kr/view/?no=20230307165036, 접근일 2026-09-30
[^ref-1299]: Modern Materials Handling (Bridget McCrea; Peerless Research Group·MHI 조사), 2026 Intralogistics Robotics Survey: Robotics moves into the mainstream, 2026-06-01, https://www.mmh.com/article/2026_intralogistics_robotics_survey_robotics_moves_into_the_mainstream, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-19 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-19 | 3. 경제성·조달·사업 모델 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1157건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 323개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alternative-name: 대체 이름 (Alternative Name (IMDF alt_name))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
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
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-domain-definition-language: 행동 영역 정의 언어 (Behavior Domain Definition Language (BDDL))
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- brainless-robot: 브레인리스 로봇 (Brainless Robot)
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
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
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
- hungarian-method: 헝가리안 방법 (Hungarian Method)
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
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
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
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- models-and-simulations-credibility-assessment: 모델·시뮬레이션 신뢰도 평가 (Models and Simulations Credibility Assessment (NASA-STD-7009))
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- observability: 관측성 (Observability)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry: 오픈텔레메트리 (OpenTelemetry (OTel))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- outdoor-mobile-robot-operational-safety-certification: 실외이동로봇 운행안전인증 (Outdoor Mobile Robot Operational Safety Certification)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- presumption-of-conformity: 적합성 추정 (Presumption of Conformity)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
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
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
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
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
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
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- stride-threat-classification: STRIDE 위협 분류 (STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
- tamper-evident-log: 변조 탐지 로그 (Tamper-evident Log)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [3] 에 걸린 4건 / 전체 262건)

```markdown
- oq-129 [열림] 채팅으로 정한 로봇 대수를 시뮬레이션 기반 대수 산정과 어떻게 연결하고, 처리량 최대화와 비용 최소화 가운데 어느 목적을 누가 정하는가? (영역 10, 35, 3)
- oq-160 [열림] 다중 플릿 오케스트레이션 소프트웨어 시장의 규모·성장률에 대해 산정 방법론이 공개된 독립 출처가 있는가(확인한 시장조사 전망은 방법론이 공개되지 않았다)? (영역 1, 3)
- oq-162 [열림] 국내 로봇산업 실태조사에 오케스트레이션·관제 소프트웨어 매출을 따로 집계하는 항목이 있는가, 없다면 국내 관제 소프트웨어 시장 규모를 어떤 자료로 추적할 것인가? (영역 1, 3)
- oq-257 [열림] 물류창고·공장 가상 시운전의 효과(프로젝트 기간·현장 시운전 기간 단축)를 벤더 사례가 아닌 독립 연구가 같은 기준선으로 측정한 결과가 있는가? (영역 36, 3)
```
