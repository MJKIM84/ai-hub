(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-14
- date: 2026-10-09
- run_type: category_link (대분류 연결)
- 대상: 대분류 Q. 현장 유형별 적용 페이지의 '다른 대분류와의 연결' 절(대분류 연결 실행). 게시된 세부영역 페이지를 근거로 다른 대분류와의 연결을 조사·서술한다. 스토리텔러는 그 절만 patches 로 바꾼다
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

### runs/2026-10-09-14/target.json

```json
{
  "run_id": "2026-10-09-14",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 147,
  "run_type": "category_link",
  "forced": true,
  "target": {
    "area_no": null,
    "area_name": null,
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
  "selection_rationale": "CLI 지정 run_type=category_link"
}
```

### runs/2026-10-09-14/research.json

```json
{
  "run_id": "2026-10-09-14",
  "date": "2026-10-09",
  "run_type": "category_link",
  "target": {
    "area_no": null,
    "area_name": null,
    "category": "Q. 현장 유형별 적용"
  },
  "gaps": [
    "Q. 현장 유형별 적용 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다",
    "61. 물류창고 ~ 67. 기타 현장 일곱 세부영역의 게시 사례가 A~P 대분류의 어느 세부영역과 무엇을 주고받는지 대분류 단위로 정리되어 있지 않다",
    "현장 유형마다 승강기·문 연동 방식, 수령 확인 방식, 제조사가 다른 로봇을 한 계층에서 묶은 공개 사례 유무가 대분류 연결 관점에서 비교되어 있지 않다",
    "C. 채팅 기반 구성·운영, K. 플랫폼 아키텍처·인프라, L. AI·학습 기술과 Q. 현장 유형별 적용을 잇는 현장 사례 근거가 약하다"
  ],
  "research_questions": [
    "현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]",
    "61. 물류창고·62. 제조 공장의 게시 사례는 F. 연동(업무 시스템·관제 연동)과 G. 계획·최적화(배정·경로)에 어떤 입력과 제약을 넘기는가?",
    "63. 병원·의료·64. 상업 시설·65. 가정·공동주택의 승강기·문 연동과 수령 확인 사례는 F. 연동의 22. 설비·건물 시스템 연동, E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적, N. 보안·개인정보와 어떻게 이어지는가?",
    "66. 실외의 인증·보도 규정·접근성 사례는 P. 거버넌스·법규·사회와 M. 안전, D. 공간·지도 모델에 어떤 요구를 넘기는가?",
    "67. 기타 현장(점검·건설·농업·오피스·데이터센터)의 사례는 J. 현장 운영·관제, D. 공간·지도 모델, K. 플랫폼 아키텍처·인프라와 어떻게 이어지는가?",
    "현장 유형 전반에서 제조사가 다른 로봇을 하나의 오케스트레이션 계층으로 묶은 공개 사례가 있는가(oq-163, oq-174, oq-176, oq-183)? A. 기획·사업의 2. 사용 사례·요구·책임 범위와 어떻게 이어지는가?"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Q. 현장 유형별 적용의 61. 물류창고 ↔ F. 연동의 23. 업무 시스템 연동: 국내 스마트물류센터 인증 심사기준은 하차·입고를 입고예정정보 확인·하역작업·상품검수·제품정보 인식·등록으로, 상차·출고를 발주처별 분류·차량입차·상차순서관리·출고정보전달로 나누어, 물류창고 로봇 작업의 시작 조건과 완료 정보가 업무 시스템 단계에 묶여 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-919"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "인증 심사기준이 하차·입고와 상차·출고 프로세스를 세부 단계로 구분함(61. 물류창고 5절 표). (발행일 미확인, 확인일 기준) (재인용: 2026-09-29-11)",
      "as_of": "2026-10-09",
      "site_type": "물류창고",
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f2",
      "claim": "Q. 현장 유형별 적용의 61. 물류창고 ↔ F. 연동의 20. 로봇·제조사 관제 연동·A. 기획·사업의 1. 기술·시장·업체 동향: 쿠팡 대구 풀필먼트센터가 AGV·소팅봇·무인지게차를 층별로 나눠 투입했고 다중 플릿 오케스트레이션 소프트웨어가 창고 제어 시스템에 비견된다는 시장 정의가 있어, ROP 가 WMS 와 WCS 사이에서 제조사가 다른 로봇에 작업을 배정하는 자리가 이 연결의 중심이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-257",
        "ref-917",
        "ref-918",
        "ref-919"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "61. 물류창고 9절의 종합 추정(AGV·AMR·소팅봇·무인지게차·하역 로봇 배정, 다중 플릿 오케스트레이션 시장 정의). (재인용: 2026-09-29-11)",
      "as_of": "2026-10-09",
      "site_type": "물류창고",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f3",
      "claim": "Q. 현장 유형별 적용의 61. 물류창고 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF·M. 안전의 49. 사람 근접 안전: 쿠팡 대구 풀필먼트센터의 AGV 는 바닥 QR 코드 경로를 따르고 무인지게차는 사람 출입을 막은 구역에서만 주행하며 경계 침범 시 안전 센서로 정지한다.",
      "tag": "사실",
      "source_ids": [
        "ref-917",
        "ref-918"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "두 보도는 같은 현장 공개 행사의 회사 제공 정보에 기반해 독립성이 제한적(61. 물류창고 5절). (재인용: 2026-09-29-11)",
      "as_of": "2023-02-07",
      "site_type": "물류창고",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f4",
      "claim": "Q. 현장 유형별 적용의 61. 물류창고 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Li 외(2020)는 대규모 물류창고의 지속형 다중 에이전트 경로 찾기를, Ma 외(2017)는 온라인 픽업·배송 작업의 지속형 경로 찾기를 다루어, 작업이 계속 들어오는 물류창고 운영이 경로 계획 연구의 대표 적용 대상이다.",
      "tag": "사실",
      "source_ids": [
        "ref-005",
        "ref-006"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Lifelong Multi-Agent Path Finding in Large-Scale Warehouses(2020), Lifelong MAPF for Online Pickup and Delivery Tasks(2017). (재인용: 2026-09-29-11)",
      "as_of": "2020",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f5",
      "claim": "Q. 현장 유형별 적용의 61. 물류창고 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적: 쿠팡 대구 풀필먼트센터의 소팅봇은 포장 라벨 바코드를 읽어 목적지별로 분류·이송하므로, 물류창고 출하 단계의 완료 확인이 작업 대상 식별에 기댄다.",
      "tag": "사실",
      "source_ids": [
        "ref-917"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "소팅봇의 바코드 판독과 목적지별 분류·이송(61. 물류창고 5절 완료·인계 칸). (재인용: 2026-09-29-11)",
      "as_of": "2023-02-07",
      "site_type": "물류창고",
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f6",
      "claim": "연계 대상: Q. 현장 유형별 적용의 61. 물류창고 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: DHL 의 트레일러 하역 로봇은 떨어진 상자의 자동 복구 개선이 향후 목표로 보도되었을 뿐이며, 로봇 자체 복구와 ROP 재계획의 분담은 공개 자료에서 확인되지 않아 두 영역의 경계 과제로 남는 것으로 보인다(oq-166).",
      "tag": "추정",
      "source_ids": [
        "ref-921"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "떨어진 상자의 자동 복구 개선이 향후 목표(61. 물류창고 5절 예외·성과 칸, 벤더 설명). (재인용: 2026-09-29-11)",
      "as_of": "2023-02-01",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f7",
      "claim": "Q. 현장 유형별 적용의 61. 물류창고 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링: Schrotenboer 외(2019)는 반품 재적치를 고객 주문 피킹 경로에 통합하는 최적화를 다루었으나 피커 기반 창고 연구이며 로봇 피킹 적용은 아니다(oq-165).",
      "tag": "사실",
      "source_ids": [
        "ref-912"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "반품 단계: 반품 재적치를 피커 경로에 통합하는 연구가 있으나 피커 기반 창고의 최적화(61. 물류창고 5절). (재인용: 2026-09-29-11)",
      "as_of": "2019-09-01",
      "site_type": "물류창고",
      "flow_item": "작업 대상",
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "Q. 현장 유형별 적용의 62. 제조 공장 ↔ G. 계획·최적화의 24. 작업·워크플로 모델링: Schmid·Limère(2019)는 조립라인 부품을 라인 적재·상자 공급·순서 공급·키팅 같은 공급 정책에 배정하는 조립라인 공급 문제를 분류해, 제조 공장 라인 공급 작업을 나누는 기준을 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-922"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "조립라인 공급 문제(ALFP)와 라인 공급 정책 정의(62. 제조 공장 4절). (재인용: 2026-09-29-12)",
      "as_of": "2019-02-23",
      "site_type": "제조 공장",
      "flow_item": "작업 대상",
      "source_unopened": true
    },
    {
      "id": "f9",
      "claim": "Q. 현장 유형별 적용의 62. 제조 공장 ↔ F. 연동의 21. 상호운용 표준·적합성·20. 로봇·제조사 관제 연동: SYNAOS 는 폭스바겐 하노버 공장에서 MLR 언더라이드 로봇 약 100대와 자율 견인차 40대 등 135대 이상을 제조사 독립 플랫폼이 VDA 5050 으로 관제한다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-924"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 135대 이상을 VDA 5050 으로 관제, 하루 9,000개 랙 운반(62. 제조 공장 5절, 회사 설명). (재인용: 2026-09-29-12)",
      "as_of": "2025-10-16",
      "site_type": "제조 공장",
      "flow_item": "수행 자원",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f10",
      "claim": "Q. 현장 유형별 적용의 62. 제조 공장 ↔ F. 연동의 23. 업무 시스템 연동: Wally 외(2019)는 ISA-95 모델과 PDDL 로 유연 생산 시스템의 운영 계획을 자동 생성하는 방법을 제안해, 생산 관리 쪽 요청을 실행 계획으로 옮기는 연결의 연구 근거가 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-925"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Flexible Production Systems: Automated Generation of Operations Plans Based on ISA-95 and PDDL(62. 제조 공장 5·9절 근거). (재인용: 2026-09-29-12)",
      "as_of": "2019-11-13",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "Q. 현장 유형별 적용의 62. 제조 공장 ↔ F. 연동의 23. 업무 시스템 연동: Siemens 는 자재 관리 시스템이 생산 계획과 칸반에 따라 운송 주문을 자동 생성해 AGV 플릿에 보낸다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-926"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 자재 관리 시스템이 생산 계획·칸반에 따라 운송 주문 자동 생성(62. 제조 공장 5절 시작 조건 칸). (발행일 미확인, 확인일 기준) (재인용: 2026-09-29-12)",
      "as_of": "2026-10-09",
      "site_type": "제조 공장",
      "flow_item": "시작 조건",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f12",
      "claim": "Q. 현장 유형별 적용의 62. 제조 공장 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계·34. 시뮬레이션·예측용 디지털 트윈: 국내 자동차 공장 연구는 시뮬레이션으로 AGV 대수·단일 차선 양방향 도로의 타당성을 따졌고(2014), 차체 버퍼 창고가 따로 운영될 때의 결품·막힘을 통합창고 모형으로 비교했다(2012).",
      "tag": "사실",
      "source_ids": [
        "ref-935",
        "ref-936"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "두 연구는 가정한 미래를 실험하는 시뮬레이션 사례(62. 제조 공장 5절 두 번째 사례). (재인용: 2026-09-29-12)",
      "as_of": "2014-04",
      "site_type": "제조 공장",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "Q. 현장 유형별 적용의 62. 제조 공장 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업·M. 안전의 49. 사람 근접 안전: 유럽 전문가 31명 조사(2024-12-02)는 좁은 조립 공간에서 협동로봇끼리, 그리고 외골격과의 충돌을 예측·회피하는 것을 핵심 안전·기술 과제로 꼽았다.",
      "tag": "사실",
      "source_ids": [
        "ref-928"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "협동로봇이 무거운 부품 지지·공구 전달을 맡고 충돌 예측·회피가 과제(62. 제조 공장 5절 세 번째 사례). (재인용: 2026-09-29-12)",
      "as_of": "2024-12-02",
      "site_type": "제조 공장",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f14",
      "claim": "Q. 현장 유형별 적용의 62. 제조 공장 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: 인증 기관 Applus+ 는 ISO 3691-4:2023 이 무인 산업 차량의 사람 감지·제동·속도 제어·운용 구역 분류를 요구한다고 안내하며, 표준 원문은 확인되지 않았다(oq-170).",
      "tag": "추정",
      "source_ids": [
        "ref-938"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 인증 기관 안내 기준의 ISO 3691-4:2023 요구 항목, 표준 원문 미열람(62. 제조 공장 5절 제약 칸). (발행일 미확인, 확인일 기준) (재인용: 2026-09-29-12)",
      "as_of": "2026-10-09",
      "site_type": "제조 공장",
      "flow_item": "제약",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f15",
      "claim": "Q. 현장 유형별 적용의 62. 제조 공장 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션·L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획: 국내 제조 현장에서 확인된 자료는 한국전자기술연구원(KETI)의 언어 모델·모방학습 조립공정 자동화 기술 공개(2025-03)와 자연어 지시가 언급되지 않은 정부 'AI 공장장' 사업(2026-09 보도)뿐이다(oq-142).",
      "tag": "사실",
      "source_ids": [
        "ref-931",
        "ref-932"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "'AI 공장장' 사업은 2026 개별 물류 작업→2029 '다크팩토리 OS'로 확대 계획, 기사에 자연어 지시 언급 없음(62. 제조 공장 5·11절). (재인용: 2026-09-29-12)",
      "as_of": "2026-09-07",
      "site_type": "제조 공장",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f16",
      "claim": "Q. 현장 유형별 적용의 63. 병원·의료 ↔ F. 연동의 22. 설비·건물 시스템 연동·G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화: 고려대학교 구로병원 연구는 승강기 제어반에 단 전용 통신 모듈로 로봇의 승강기 호출·탑승을 자동화했고, 승강기 가동률 59% 미만 구간의 성공률이 95.52% 이며 실패가 가동률 90% 초과 구간에 몰렸다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "단일 기관·2025-06-18~29 비긴급 배송 122건 조건, TK50M 제어반 전용 통신 모듈(63. 병원·의료 5절). 전체 성공률 분모는 oq-215 로 미확인. (재인용: 2026-09-29-13)",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "Q. 현장 유형별 적용의 63. 병원·의료 ↔ F. 연동의 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성: 싱가포르 창이종합병원 CHART 의 RoMi-H 는 ROS 2·DDS 기반 오픈소스 미들웨어로 여러 제조사 로봇·센서·병원 정보 시스템을 잇고, 2025-05-01 부터 2년 유효한 등재 프로그램으로 시스템 통합사 5곳이 배치를 맡으며, 로봇들이 승강기를 공유하고 출입 금지 구역으로 충돌을 피한다.",
      "tag": "사실",
      "source_ids": [
        "ref-937",
        "ref-872",
        "ref-942"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "RoMi-H 네 도메인(기계·제어·중앙·통합), 등재 통합사 5곳, 승강기 공유·출입 금지 구역(63. 병원·의료 4·5절). (재인용: 2026-09-29-13)",
      "as_of": "2025-05-01",
      "site_type": "병원",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "Q. 현장 유형별 적용의 63. 병원·의료 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적·N. 보안·개인정보의 51. 인증·권한·격리: 중국 산시성 인민병원 연구에서 AMR 10대의 약품·검체 이송은 픽업·배송 지점의 RFID 신원 확인으로 완료·인계를 확인했고, 약국·병동·시스템 관리자·장비 관리자의 역할을 정한 협력 책임 체계를 두었다.",
      "tag": "사실",
      "source_ids": [
        "ref-929"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "단일 연구(2025-06-01~11-30) 조건, 배송 시간 32~36% 단축, RFID 신원 확인(63. 병원·의료 5절 해외 사례). (재인용: 2026-09-29-13)",
      "as_of": "2026-04-24",
      "site_type": "병원",
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "Q. 현장 유형별 적용의 63. 병원·의료 ↔ F. 연동의 20. 로봇·제조사 관제 연동·J. 현장 운영·관제의 37. 관제 화면·실행 기록·O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 한림대성심병원은 2024-04 기준 7종 73대 서비스 로봇을 커맨드센터의 통합관제 시스템으로 관리하고 LG전자와 빅웨이브로보틱스가 배송로봇을 공급하며, 시스템 정착에 약 3년이 걸렸으나 통합관제의 인터페이스·표준은 공개되지 않았다(oq-174).",
      "tag": "사실",
      "source_ids": [
        "ref-944",
        "ref-941"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "7종 73대 통합관제, 2023년 27,300건 배송, 정착 약 3년(63. 병원·의료 5절 국내 사례). (재인용: 2026-09-29-13)",
      "as_of": "2024-07-15",
      "site_type": "병원",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f20",
      "claim": "Q. 현장 유형별 적용의 63. 병원·의료·64. 상업 시설 ↔ F. 연동의 22. 설비·건물 시스템 연동·M. 안전의 50. 안전 표준·인증·사고 조사: 국가기술표준원은 2021-11-11 로봇의 엘리베이터 탑승 안전 요구사항 KS 제정을 발표했으며, 병원 이송과 호텔 배송 사례가 모두 이 요구 아래 승강기를 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-945"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다(63·64 페이지 5절 제약 칸). 조항은 oq-173 로 미확인. (재인용: 2026-09-29-16)",
      "as_of": "2021-11-11",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "Q. 현장 유형별 적용의 63. 병원·의료 ↔ M. 안전의 48. 안전·위험 관리·N. 보안·개인정보의 53. 개인정보·영상 데이터: 병원에서 감염 관리 구역·야간 시간대·권한은 ROP 의 경로·배정 제약이 되고, 감염 관리 기준 설정과 이동형 영상정보처리기기 운영 제한 같은 법 판단은 병원 감염관리 조직·법령 쪽 연계 대상으로 남는 것으로 보인다(oq-171, oq-172).",
      "tag": "추정",
      "source_ids": [
        "ref-950",
        "ref-929",
        "ref-978"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "63. 병원·의료 9절 업종별 조건 행의 추정(감염 관리 구역·권한을 제약으로, 기준 설정은 연계 대상). (재인용: 2026-09-29-13)",
      "as_of": "2026-10-09",
      "site_type": "병원",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "Q. 현장 유형별 적용의 63. 병원·의료 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: 국내 병원 로봇 도입의 장애 요인으로 속도·안전성 부족, 대당 억 단위 비용, 경사 구간·문 호환·건물마다 다른 회사의 승강기가 보도되었고, 확인된 국내 지원 제도는 과제 단위의 서비스로봇 실증사업이다.",
      "tag": "사실",
      "source_ids": [
        "ref-948",
        "ref-947"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기사가 전한 국내 병원 일반의 장애 요인(63. 병원·의료 5절 울산대병원 사례 제약 칸, 11절 oq-149). (재인용: 2026-09-29-13)",
      "as_of": "2025-04-10",
      "site_type": "병원",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "Q. 현장 유형별 적용의 63. 병원·의료 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: 분당서울대병원은 KT 5G 특화망 위의 AMR 6대가 다중 연동된 승강기·자동문을 거쳐 약 300m 연결 터널로 진료재료·약품·린넨 카트를 야간에 옮기게 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-939"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "5G 특화망 위 AMR 6대, 승강기·자동문 다중 연동, 야간 배송으로 환자 동선 분리(63. 병원·의료 5절). (재인용: 2026-09-29-13)",
      "as_of": "2023-07-06",
      "site_type": "병원",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f24",
      "claim": "Q. 현장 유형별 적용의 64. 상업 시설 ↔ G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화·26. 작업 순서·스케줄링: 다층 호텔 배치 자료(3개 층 67실) 실험에서 승강기 운행 시간이 40초에서 100초로 늘면 총 이동 시간이 거의 두 배가 되었고, 로봇이 5대를 넘으면 추가 로봇의 한계 이익이 크게 줄었다.",
      "tag": "사실",
      "source_ids": [
        "ref-103"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "고객 노드 60개에서 225초→500초, 아침 식사·체크아웃 시간대 고려 제안(64. 상업 시설 5절 호텔 사례). (발행일 미확인, 확인일 기준) (재인용: 2026-09-29-16)",
      "as_of": "2026-10-09",
      "site_type": "상업 시설",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "Q. 현장 유형별 적용의 64. 상업 시설 ↔ F. 연동의 22. 설비·건물 시스템 연동: 오티스는 자사 클라우드 API(Otis Integrated Dispatch)로 로봇이 승강기를 스스로 호출·탑승·층 선택하며, 오사카 호텔에서 2022-12 부터 24시간 객실 배송을 한다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-957"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: OID 클라우드 API, 야간 최대 60건 요청 처리(64. 상업 시설 5절). (발행일 미확인, 확인일 기준) (재인용: 2026-09-29-16)",
      "as_of": "2026-10-09",
      "site_type": "상업 시설",
      "flow_item": "수행 자원",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f26",
      "claim": "Q. 현장 유형별 적용의 64. 상업 시설 ↔ F. 연동의 22. 설비·건물 시스템 연동: 화성 동탄 상업시설 레이크 꼬모에서는 라이노스의 청소로봇 휠리 J40 이 클라우드 승강기 관리 솔루션 rEMS 로 전 층을 오간다고 보도되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-963"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "층간 이동을 승강기 관리 솔루션이 맡음(64. 상업 시설 5절 매장·쇼핑몰 사례). (재인용: 2026-09-29-16)",
      "as_of": "2025-04-02",
      "site_type": "상업 시설",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f27",
      "claim": "Q. 현장 유형별 적용의 64. 상업 시설 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업·32. 예외 복구·재계획·업무 연속성: 일본 헨나 호텔에서는 객실 음성 비서·짐 운반·프런트 로봇이 기본 질문과 여권 복사 같은 업무를 해내지 못해 직원이 계속 넘겨받아야 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-961",
        "ref-962"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "로봇이 해내지 못한 일을 직원이 계속 넘겨받음(64. 상업 시설 5절 예외·성과). (재인용: 2026-09-29-16)",
      "as_of": "2019-01",
      "site_type": "상업 시설",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f28",
      "claim": "Q. 현장 유형별 적용의 64. 상업 시설 ↔ F. 연동의 23. 업무 시스템 연동: Sam's Club 은 약 600개 매장의 자율 바닥 청소기에 재고 스캔 타워를 달아, 로봇이 모은 가격 정확도·재고 수준·진열 위치 정보를 매장 관리자에게 전달하게 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-952"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "청소와 재고 스캔을 한 로봇으로, 수집 정보는 매장 관리자에게 전달(64. 상업 시설 5절). (재인용: 2026-09-29-16)",
      "as_of": "2022-02-01",
      "site_type": "상업 시설",
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f29",
      "claim": "Q. 현장 유형별 적용의 64. 상업 시설 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업: 쇼핑몰 안내 로봇 연구(2010)는 소음 속 음성 인식과 예상치 못한 지식 요구 때문에 일부 기능을 원격 조작자가 맡는 반자율 방식을 택했다.",
      "tag": "사실",
      "source_ids": [
        "ref-953"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "25일 현장 시험 2,642회 상호작용(초록 요약 기준, 64. 상업 시설 5절). (재인용: 2026-09-29-16)",
      "as_of": "2010-10",
      "site_type": "상업 시설",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f30",
      "claim": "Q. 현장 유형별 적용의 64. 상업 시설 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반·P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: 네덜란드 슈퍼마켓 로봇 연구는 영어·네덜란드어와 성별 집단으로 음성 인식 기술을 비교해 Whisper 가 가장 낮은 단어 오류율을 보였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-868"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "참가자 40명, 질의 분류기 정확도 약 87%(C. 채팅 기반 구성·운영 연결 절 상업 시설 사례). (재인용: 2026-10-09-01)",
      "as_of": "2025-04-29",
      "site_type": "상업 시설",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f31",
      "claim": "Q. 현장 유형별 적용의 65. 가정·공동주택 ↔ F. 연동의 22. 설비·건물 시스템 연동·E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적: 서울 래미안 리더스원에서는 공동현관 자동문 개폐와 엘리베이터 호출을 연동해 배송로봇이 세대 현관까지 가고, 주문자만 음식을 꺼낼 수 있는 방식으로 넘기며 인증 수단은 공개되지 않았다(oq-184).",
      "tag": "사실",
      "source_ids": [
        "ref-966",
        "ref-965",
        "ref-979"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "2024-12 시범 운영, 2025 실증, 2026 요기요 연계 확대(65. 가정·공동주택 5절). (재인용: 2026-09-29-17)",
      "as_of": "2026-09-20",
      "site_type": "가정",
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f32",
      "claim": "Q. 현장 유형별 적용의 65. 가정·공동주택 ↔ N. 보안·개인정보의 53. 개인정보·영상 데이터: 개인정보 보호법 제25조의2 는 이동형 영상정보처리기기의 운영을 제한하며, 개발용 Roomba 가 집 안에서 찍은 이미지가 라벨링 외주를 거쳐 외부에 게시된 사례가 보도되었다(세대 안 적용 여부는 oq-181).",
      "tag": "사실",
      "source_ids": [
        "ref-978",
        "ref-968"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "민간 법령 DB 게재 조문 기준, 국가법령정보센터 원문 미열람; iRobot 개발용 기기 사례(65. 가정·공동주택 5·7절). (재인용: 2026-09-29-17)",
      "as_of": "2023-03-14",
      "site_type": "가정",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f33",
      "claim": "Q. 현장 유형별 적용의 65. 가정·공동주택 ↔ F. 연동의 21. 상호운용 표준·적합성: Matter 1.2 는 로봇청소기를 기기 유형으로 더해 원격 시작과 진행 알림, 브러시·오류·충전 상태 보고를 가전 연동 표준으로 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-977"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Matter 1.2 Arrives with Nine New Device Types(65. 가정·공동주택 5절 세대 안 사례). (재인용: 2026-09-29-17)",
      "as_of": "2023-10-23",
      "site_type": "가정",
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f34",
      "claim": "Q. 현장 유형별 적용의 65. 가정·공동주택 ↔ F. 연동의 23. 업무 시스템 연동·J. 현장 운영·관제의 37. 관제 화면·실행 기록: LH토지주택연구원 자료를 인용한 보도는 택배 차량이 단지 집하처에서 송장번호를 인식시키면 물품 정보가 관제실로 가고, 단지 로봇 택배를 단지 중앙집하·동 단위·구역 단위 분산집하의 세 시나리오로 나눈다고 전한다.",
      "tag": "사실",
      "source_ids": [
        "ref-976"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "관제실이 거주자와 통신하며 로봇을 통제해 배송(65. 가정·공동주택 5절 택배 사례). (재인용: 2026-09-29-17)",
      "as_of": "2024-07-18",
      "site_type": "가정",
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f35",
      "claim": "Q. 현장 유형별 적용의 66. 실외 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스·M. 안전의 50. 안전 표준·인증·사고 조사: 2023-11-17 개정 지능형로봇법·도로교통법 시행으로 운행안전인증을 받은 실외이동로봇이 보행자 지위를 얻고 운영자의 보험 가입 의무가 생겼으며, 인증은 로봇과 관제장치의 조합에 주어진다.",
      "tag": "사실",
      "source_ids": [
        "ref-991",
        "ref-980"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보행자 의무와 보험·공제 가입 의무, 로봇+관제장치 조합 인증(66. 실외 3·5절). (재인용: 2026-09-30-01)",
      "as_of": "2023-11-16",
      "site_type": "실외",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f36",
      "claim": "Q. 현장 유형별 적용의 66. 실외 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 운행안전인증이 로봇과 관제장치의 조합을 대상으로 하므로, 제조사가 다른 실외 로봇을 하나의 오케스트레이션 계층에서 지시할 때 그 계층이 인증상 관제장치에 해당하는지가 연동 설계의 쟁점이 될 것으로 보인다(oq-187).",
      "tag": "추정",
      "source_ids": [
        "ref-980"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "이종 제조사를 잇는 계층의 관제장치 해당 여부는 열린 질문(66. 실외 9절). (발행일 미확인, 확인일 기준) (재인용: 2026-09-30-01)",
      "as_of": "2026-10-09",
      "site_type": "실외",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f37",
      "claim": "Q. 현장 유형별 적용의 66. 실외 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리·P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: 피츠버그 대학 캠퍼스에서 Starship 배송로봇이 연석 경사로를 막아 휠체어 이용자가 차도에 갇힌 뒤 대학이 시험 운행을 멈췄고, 회사는 해당 교차로의 지도 오류를 원인으로 들었다.",
      "tag": "사실",
      "source_ids": [
        "ref-987"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "문제 제기 뒤 두 시간이 채 안 돼 시험 운행 중단, 지도 오류 수정(66. 실외 5절, 2019-10-21 보도). (재인용: 2026-09-30-01)",
      "as_of": "2019-10-21",
      "site_type": "실외",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f38",
      "claim": "Q. 현장 유형별 적용의 66. 실외 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델·G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Gehrke 외(2023)는 대학 캠퍼스 녹화 영상으로 보도 자율 배송로봇과 보행자·자전거 이용자의 상호작용 빈도·심각도를 침범 후 시간(PET)으로 쟀다.",
      "tag": "사실",
      "source_ids": [
        "ref-990"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists(66. 실외 8절). (재인용: 2026-09-30-01)",
      "as_of": "2023-03",
      "site_type": "실외",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f39",
      "claim": "Q. 현장 유형별 적용의 66. 실외 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성·31. 사람–로봇 협업: Dobrosovestnova 외(RO-MAN 2022)는 눈 속에 갇힌 배송로봇을 행인이 도운 사례를 탐색적으로 연구했다.",
      "tag": "사실",
      "source_ids": [
        "ref-993"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow(66. 실외 5·8절). (재인용: 2026-09-30-01)",
      "as_of": "2022",
      "site_type": "실외",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f40",
      "claim": "연계 대상: Q. 현장 유형별 적용의 66. 실외 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델: Nav2 문서는 GPS 위치추정으로 실외에서 주행하는 방법을 튜토리얼로 제공하며, 위성 위치 기반 위치추정은 로봇 자체 지능·제어 쪽 기능이다.",
      "tag": "사실",
      "source_ids": [
        "ref-988"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Navigating Using GPS Localization — Nav2 documentation(66. 실외 9절 로봇 자체 지능·제어 행). (발행일 미확인, 확인일 기준) (재인용: 2026-09-30-01)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f41",
      "claim": "Q. 현장 유형별 적용의 66. 실외 ↔ F. 연동의 21. 상호운용 표준·적합성·P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 일본(2022년 공포 개정 도로교통법)과 미국 주별 개인 배송 장치(PDD) 법처럼 관할마다 보도 로봇의 크기·속도·신고 기준이 달라, ROP 가 관할 조건을 경로·속도 제약으로 바꿔 담는 공통 표현이 필요할 것으로 보인다(oq-190).",
      "tag": "추정",
      "source_ids": [
        "ref-985",
        "ref-986"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "66. 실외 9절 업종별 조건 행의 추정(관할별 속도·크기·보행자 의무·신고 조건을 제약으로 반영). (재인용: 2026-09-30-01)",
      "as_of": "2026-10-09",
      "site_type": "실외",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f42",
      "claim": "Q. 현장 유형별 적용의 67. 기타 현장 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석·F. 연동의 23. 업무 시스템 연동: Equinor 의 이산화탄소 포집·저장 시설에서는 4족 로봇이 계기 판독·밸브 위치 확인·누출 탐지를 하고, 현장 운영자가 연구개발 부서 도움 없이 점검 임무를 직접 만든다.",
      "tag": "사실",
      "source_ids": [
        "ref-995"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "2024-11 배치, 운영자가 직접 임무 생성, 완료 확인 주체는 미확인(67. 기타 현장 5절). (재인용: 2026-09-30-02)",
      "as_of": "2025-11-21",
      "site_type": "기타",
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f43",
      "claim": "Q. 현장 유형별 적용의 67. 기타 현장 ↔ D. 공간·지도 모델의 14. 도면·BIM에서 지도 만들기: GS건설은 4족 로봇 스팟이 모은 건설 현장 데이터를 기존 3차원 BIM 데이터와 통합해 전기·설비 공사 간섭 확인과 안전관리계획 수립에 썼다고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1000"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "2020-07 큐픽스와 함께 국내 건설 현장 첫 도입(67. 기타 현장 5절). (재인용: 2026-09-30-02)",
      "as_of": "2020-07-13",
      "site_type": "기타",
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f44",
      "claim": "Q. 현장 유형별 적용의 67. 기타 현장 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조·F. 연동의 22. 설비·건물 시스템 연동: 네이버 제2사옥 1784 의 배달 로봇 루키는 클라우드 기반 멀티 로봇 시스템 ARC 가 5G 특화망으로 제어하고 로봇 전용 엘리베이터 로보포트로 층을 오간다.",
      "tag": "사실",
      "source_ids": [
        "ref-997"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "초기 40대에서 100여 대로 증가, 브레인리스 로봇(67. 기타 현장 5절). 배달 시간 단축 수치는 벤더 주장이라 제외. (재인용: 2026-09-30-02)",
      "as_of": "2023-01-11",
      "site_type": "기타",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f45",
      "claim": "Q. 현장 유형별 적용의 67. 기타 현장 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 농촌진흥청 통합 관리 프로그램은 자체 개발한 방제·운반·모니터링 로봇 3종을 하나의 화면으로 관리하며, 다른 제조사 로봇의 연결 여부는 보도에 없다(oq-192).",
      "tag": "사실",
      "source_ids": [
        "ref-1007"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "작업 순서 설정, 위치·속도·이동 거리 표시, SIL 2 제어기(67. 기타 현장 5절). (재인용: 2026-09-30-02)",
      "as_of": "2025-04-23",
      "site_type": "기타",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f46",
      "claim": "Q. 현장 유형별 적용의 67. 기타 현장 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적: 네이버 데이터센터 각 세종에서는 서버 관리 로봇과 운반 로봇이 협력해 서버 자산 흐름을 실시간으로 추적·관리한다고 보도되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1002"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "'세로'·'가로' 로봇이 ARC·ARM 시스템으로 공간·서비스 인프라와 연동(67. 기타 현장 5절, 2023-11 기준). (재인용: 2026-09-30-02)",
      "as_of": "2023-11-08",
      "site_type": "기타",
      "flow_item": "작업 대상",
      "source_unopened": true
    },
    {
      "id": "f47",
      "claim": "Q. 현장 유형별 적용의 67. 기타 현장 ↔ M. 안전의 48. 안전·위험 관리: ISO 18497-3:2024 는 부분 자동·반자율·자율 농업기계의 자율 운용 구역을 다루어, 농업 현장 로봇의 운용 구역이 ROP 의 운행 제약 입력이 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-1009"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Part 3: Autonomous operating zones, 원문 미열람(67. 기타 현장 9절 업종별 조건 행). (재인용: 2026-09-30-02)",
      "as_of": "2024",
      "site_type": "기타",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f48",
      "claim": "Q. 현장 유형별 적용의 67. 기타 현장 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 싱가포르 창이 공항에서 Open-RMF 가 청소 로봇 운영에 쓰인다는 기사가 있으나, 제조사가 다른 로봇을 한 계층에서 묶은 기타 현장의 공개 사례로 확인할 수준은 아닌 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1004"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기사와 벤더 주장만 있음(67. 기타 현장 9절). (재인용: 2026-09-30-02)",
      "as_of": "2025-10-29",
      "site_type": "기타",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f49",
      "claim": "Q. 현장 유형별 적용의 63. 병원·의료 ↔ D. 공간·지도 모델의 14. 도면·BIM에서 지도 만들기·O. 검증·도입·수명주기의 55. 현장 조사·설치·시운전: 에스토니아 타르투 대학병원 현장 시험은 Open-RMF 교통 편집기로 평면도를 주석하고 로봇 격자 지도를 정합해 중환자실에서 검사실로 혈액 검체를 운반했으며, 작은 구역으로 나눠 매핑한 뒤 합치는 편이 더 정확했다.",
      "tag": "사실",
      "source_ids": [
        "ref-869"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test(D. 공간·지도 모델 연결 절). (재인용: 2026-10-09-02)",
      "as_of": "2022-08-23",
      "site_type": "병원",
      "flow_item": "작업 대상",
      "source_unopened": true
    },
    {
      "id": "f50",
      "claim": "Q. 현장 유형별 적용의 61. 물류창고 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: EU ILIAD 프로젝트는 학습한 사람 흐름에 맞춰 물류창고 자율 지게차의 경로를 계획했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1180"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "스웨덴 외레브로 창고의 자율 지게차 플릿, 움직임 지도 활용(E. 사물·사람·실시간 상태 연결 절). (재인용: 2026-10-09-03)",
      "as_of": "2021-06",
      "site_type": "물류창고",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f51",
      "claim": "Q. 현장 유형별 적용 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: 게시된 61. 물류창고 ~ 67. 기타 현장 페이지가 확인한 국내 사례는 한 운영사가 설비별로 로봇을 들이거나 건설사·물류사 한 곳과 로봇 업체 한 곳이 짝을 이루거나 한 기관이 만든 로봇을 자체 계층으로 묶은 형태이며, 제조사가 다른 로봇을 하나의 오케스트레이션 계층으로 묶은 국내 공개 사례는 지금까지 확인되지 않은 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-917",
        "ref-944",
        "ref-966",
        "ref-997",
        "ref-1007"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "61·63·65·67 페이지 9절의 종합(oq-163, oq-174, oq-183). 조사 범위의 한계이며 부재를 뜻하지 않음. (재인용: 2026-09-30-02)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    }
  ],
  "sources": [
    {
      "id": "ref-005",
      "org": "Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S.",
      "title": "Lifelong Multi-Agent Path Finding in Large-Scale Warehouses",
      "published": "2020",
      "url": "https://arxiv.org/abs/2005.07371",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 대규모 물류창고의 지속형 다중 에이전트 경로 찾기 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-006",
      "org": "Ma, H., Li, J., Kumar, T. K. S., & Koenig, S.",
      "title": "Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks",
      "published": "2017",
      "url": "https://arxiv.org/abs/1705.10868",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 온라인 픽업·배송 작업의 지속형 경로 찾기(MAPD) 연구.",
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
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 다층 호텔 배송 로봇 경로 계획에서 승강기 대기·운행 시간을 모델링.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-257",
      "org": "Interact Analysis",
      "title": "AMR Multi-Fleet Orchestration Software Explained",
      "published": null,
      "url": "https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 다중 플릿 오케스트레이션 소프트웨어의 시장 정의.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-868",
      "org": "Nandkumar, C., & Peternel, L. (Delft University of Technology), Frontiers in Robotics and AI",
      "title": "Enhancing supermarket robot interaction: an equitable multi-level LLM conversational interface for handling diverse customer intents",
      "published": "2025-04-29",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12069059/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 슈퍼마켓 로봇 대화 인터페이스의 음성 인식·질의 분류 비교.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-869",
      "org": "Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 타르투 대학병원 이기종 로봇 플릿 현장 시험(Open-RMF 지도 주석, 혈액 검체 운반).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-872",
      "org": "Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "RoMi-H Empanelment Programme 2025",
      "published": "2025-05-01",
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. RoMi-H 시스템 통합사 등재 프로그램(2년 유효).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-912",
      "org": "Schrotenboer, A. H., Wruck, S., Vis, I. F. A., & Roodbergen, K. J.",
      "title": "Integration of returns and decomposition of customer orders in e-commerce warehouses",
      "published": "2019-09-01",
      "url": "https://arxiv.org/abs/1909.01794",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 반품 재적치를 피커 경로에 통합하는 창고 최적화 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-917",
      "org": "로봇신문 (장길수)",
      "title": "쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이...",
      "published": "2023-02-07",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=30736",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 쿠팡 대구 FC 의 AGV·소팅봇·무인지게차 현장 공개 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-918",
      "org": "물류신문 (석한글)",
      "title": "‘물류 투자만 6조’, 쿠팡 물류 인프라의 정점 ‘대구 FC’ 가보니",
      "published": "2023-02-07",
      "url": "https://www.klnews.co.kr/news/articleView.html?idxno=306994",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 같은 현장 공개 행사의 층별 로봇 투입 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-919",
      "org": "스마트물류시설인증센터 (한국교통연구원)",
      "title": "인증스마트물류센터 : 인증심사 > 심사기준 > 일반",
      "published": null,
      "url": "https://cslc.koti.re.kr/new_sub2/new_sub2_2_1",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 스마트물류센터 인증 심사기준(입고·출고 프로세스, 정보시스템 항목).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-921",
      "org": "Robotics 24/7 (Eugene Demaitre)",
      "title": "DHL Makes First Commercial Deployment of Boston Dynamics Stretch Robot to Unload Trailers and Containers",
      "published": "2023-02-01",
      "url": "https://www.robotics247.com/article/dhl_makes_first_commercial_deployment_boston_dynamics_stretch_robot_unload_trailers_containers",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. DHL 의 트레일러 하역 로봇 상업 배치 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-922",
      "org": "Schmid, N. A., & Limère, V. (International Journal of Production Research 57(24))",
      "title": "A classification of tactical assembly line feeding problems",
      "published": "2019-02-23",
      "url": "https://www.tandfonline.com/doi/full/10.1080/00207543.2019.1581957",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 조립라인 공급 문제의 분류 틀.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-924",
      "org": "SYNAOS (IoT Use Case)",
      "title": "VDA 5050: unified AGV fleet control in real time at VW",
      "published": "2025-10-16",
      "url": "https://www.iotusecase.com/en/solution-examples/vda-5050-agv-fleet-control",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 폭스바겐 하노버 VDA 5050 플릿 관제 사례(회사 설명).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-925",
      "org": "Wally, B., Vyskočil, J., Novák, P., Huemer, C., Šindelář, R., Kadera, P., Mazak, A., & Wimmer, M.",
      "title": "Flexible Production Systems: Automated Generation of Operations Plans Based on ISA-95 and PDDL",
      "published": "2019-11-13",
      "url": "https://arxiv.org/abs/1911.05481",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ISA-95 와 PDDL 로 생산 운영 계획을 자동 생성.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-926",
      "org": "Siemens",
      "title": "AGV fleet management integration with intralogistics",
      "published": null,
      "url": "https://resources.sw.siemens.com/en-US/white-paper-integrating-agv-automated-guided-vehicle-system-with-intralogistics/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 자재 관리 시스템과 AGV 플릿 연동 백서.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-928",
      "org": "Pietrantoni, L., Favilla, M., Fraboni, F., Mazzoni, E., Morandini, S., Benvenuti, M., & De Angelis, M. (Frontiers in Robotics and AI)",
      "title": "Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors",
      "published": "2024-12-02",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1342130/full",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 협동로봇 통합에 관한 유럽 전문가 조사.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-929",
      "org": "Li, M. 외 (Scientific Reports)",
      "title": "Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios",
      "published": "2026-04-24",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 중국 병원 약품·검체 이송 로봇 운영 관리·효과 분석.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-931",
      "org": "뉴시스",
      "title": "\"로봇 몇 대, 어디로 움직일까\"…중소 제조현장에 'AI 공장장' 뜬다",
      "published": "2026-09-07",
      "url": "https://www.newsis.com/view/NISX20260907_0003779780",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 중소 제조 현장 'AI 공장장' 정부 사업 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-932",
      "org": "테크데일리",
      "title": "KETI, LLM 모델 및 모방학습, 조립공정 자동화 기술 공개",
      "published": "2025-03-12",
      "url": "https://www.techdaily.co.kr/news/articleView.html?idxno=25352",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. KETI 의 언어 모델·모방학습 조립 자동화 시연 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-935",
      "org": "강명훈, 곽춘종 (부산대학교; Asia-Pacific Journal of Business & Commerce)",
      "title": "시뮬레이션을 이용한 자동차 부품 공급 시스템 도입 방안 분석: R자동차 사례",
      "published": "2014-04",
      "url": "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE02448280",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 자동차 부품 공급 AGV 도입 시뮬레이션 분석.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-936",
      "org": "옥창훈, 김득수, 공정수, 서윤호 (고려대학교, 현대자동차; 한국시뮬레이션학회 논문지 21(2))",
      "title": "자동차 생산을 위한 통합창고 연구",
      "published": "2012",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001671601",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 차체 버퍼 창고 통합 모형의 결품·막힘 비교.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-937",
      "org": "Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "ROMI-H | Changi General Hospital",
      "published": null,
      "url": "https://www.cgh.com.sg/chart/projects/romi-h",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 의료 로봇 미들웨어 RoMi-H 소개.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-938",
      "org": "Applus+ Laboratories",
      "title": "ISO 3691-4:2023: Compliance Testing for Automated Guided Vehicles (AGVs)",
      "published": null,
      "url": "https://www.appluslaboratories.com/global/en/what-we-do/service-sheet/iso-3691-4-2023-compliance-testing-for-automated-guided-vehicles-agvs",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 인증 기관의 ISO 3691-4:2023 적합성 시험 안내.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-939",
      "org": "이데일리",
      "title": "분당서울대병원, 무거운 이송카트 로봇자율배송, 무안경 3D 의료실습에 도입",
      "published": "2023-07-06",
      "url": "https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01403846635671896",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 분당서울대병원 5G AMR 카트 이송 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-941",
      "org": "데일리팜",
      "title": "원내 약 배송로봇 도입 확대...정부 지원에 변화 바람",
      "published": "2024-07-15",
      "url": "https://m.dailypharm.com/user/news/15128",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 국내 병원 약 배송로봇 도입 현황 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-942",
      "org": "Open Robotics",
      "title": "ROMI-H: Bringing Robot Traffic Control to Healthcare",
      "published": "2021-02-10",
      "url": "https://www.openrobotics.org/blog/2021/2/10/romi-h-bringing-robot-traffic-control-to-healthcare",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. RoMi-H 의 승강기 공유·교통 관리 소개.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-943",
      "org": "Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03-31",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 승강기 가동률과 약품 배송 로봇 성공률 분석.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-944",
      "org": "로봇신문",
      "title": "국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원'",
      "published": "2024-04-15",
      "url": "http://www.irobotnews.com/news/articleView.html?idxno=34601",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 한림대성심병원 7종 73대 로봇 통합관제 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-945",
      "org": "산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11-11",
      "url": "https://eiec.kdi.re.kr/policy/materialView.do?num=220004",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 로봇 엘리베이터 탑승 KS 제정 발표.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-947",
      "org": "한국로봇산업진흥원",
      "title": "서비스로봇 실증사업",
      "published": null,
      "url": "https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 과제 단위 서비스로봇 실증사업 안내.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-948",
      "org": "비즈한국",
      "title": "병원에 늘어나는 '로봇', 의사·간호사도 편해졌을까",
      "published": "2025-04-10",
      "url": "https://bizhankook.com/articles/29394.html",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 국내 병원 로봇 도입 효과와 장애 요인 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-950",
      "org": "한국보건산업진흥원 스마트병원 확산지원센터",
      "title": "선도모델 및 모듈 소개",
      "published": null,
      "url": "https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 스마트병원 선도모델 소개.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-952",
      "org": "Retail Dive (Sam Silverstein)",
      "title": "Sam's Club rolls out inventory-checking robots chainwide",
      "published": "2022-02-01",
      "url": "https://www.retaildive.com/news/sams-club-rolls-out-inventory-checking-robots-chainwide/618040/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Sam's Club 청소·재고 스캔 로봇 전 매장 배치 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-953",
      "org": "Kanda, T., Shiomi, M., Miyashita, Z., Ishiguro, H., & Hagita, N. (IEEE Transactions on Robotics 26(5))",
      "title": "A Communication Robot in a Shopping Mall",
      "published": "2010-10",
      "url": "https://ieeexplore.ieee.org/abstract/document/5557825",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 쇼핑몰 안내 로봇의 반자율 현장 시험.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-957",
      "org": "Otis Elevator Company",
      "title": "Elevators and service robots",
      "published": null,
      "url": "https://www.otis.com/en/us/innovation/elevators-and-service-robots",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 오티스 승강기·서비스 로봇 연동 소개(회사 설명).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-961",
      "org": "Responsible AI Collaborative (AI Incident Database)",
      "title": "Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks",
      "published": null,
      "url": "https://incidentdatabase.ai/cite/346/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 헨나 호텔 로봇 실패 사건 기록.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-962",
      "org": "Hotel Technology News",
      "title": "Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce",
      "published": "2019-01",
      "url": "https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 헨나 호텔 로봇 절반 퇴출 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-963",
      "org": "서울경제 (백주연)",
      "title": "엘리베이터 타고 쇼핑몰 왔다갔다…바닥 물걸레질까지 하는 '로봇 청소부' 등장",
      "published": "2025-04-02",
      "url": "https://www.sedaily.com/article/14048085",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 레이크 꼬모 청소로봇의 승강기 연동 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-965",
      "org": "삼성물산 뉴스룸",
      "title": "삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영",
      "published": "2026-01-15",
      "url": "https://news.samsungcnt.com/ko/%EC%A0%84%EC%B2%B4%EA%B8%B0%EC%82%AC/%EA%B1%B4%EC%84%A4%EB%B6%80%EB%AC%B8/2026-01-%EC%82%BC%EC%84%B1%EB%AC%BC%EC%82%B0-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%84%B8%EB%8C%80-%ED%98%84%EA%B4%80%EA%B9%8C%EC%A7%80-%EC%9D%8C%EC%8B%9D%EB%B0%B0%EB%8B%AC%EB%A1%9C%EB%B4%87-%ED%99%95%EC%9E%A5/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 래미안 리더스원 세대 현관 배달로봇 확장 운영 발표.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-966",
      "org": "지디넷코리아 (신영빈)",
      "title": "로봇이 문앞까지 택배 가져다 주는 미래 곧 온다",
      "published": "2025-01-19",
      "url": "https://zdnet.co.kr/view/?no=20250119062609",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 공동주택 배송로봇 실증 사례 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-968",
      "org": "MIT Technology Review (Eileen Guo)",
      "title": "A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?",
      "published": "2022-12-19",
      "url": "https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 개발용 로봇청소기 영상 유출 탐사 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-976",
      "org": "정보통신신문 (김연균)",
      "title": "로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’",
      "published": "2024-07-18",
      "url": "https://www.koit.co.kr/news/articleView.html?idxno=123976",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. LH토지주택연구원 자료를 인용한 단지 로봇 택배 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-977",
      "org": "Connectivity Standards Alliance (CSA)",
      "title": "Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board",
      "published": "2023-10-23",
      "url": "https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Matter 1.2 의 로봇청소기 기기 유형 추가 발표.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-978",
      "org": "CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관)",
      "title": "개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)",
      "published": "2023-03-14",
      "url": "https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4_%EB%B3%B4%ED%98%B8%EB%B2%95/%EC%A0%9C25%EC%A1%B0%EC%9D%982",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 이동형 영상정보처리기기 운영 제한 조문(민간 법령 DB 게재).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-979",
      "org": "미디어펜 (조태민)",
      "title": "로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도",
      "published": "2026-09-20",
      "url": "https://www.mediapen.com/news/view/1124680",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 건설사의 공동현관·승강기 연동 로봇 친화 설계 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 로봇과 관제장치 조합 대상의 운행안전인증 안내.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-985",
      "org": "内閣府 (일본 내각부)",
      "title": "令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について",
      "published": "2023",
      "url": "https://www8.cao.go.jp/koutu//taisaku/r05kou_haku/zenbun/genkyo/topics/topic_1.html",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 일본 개정 도로교통법(원격 조작형 소형차 등) 해설.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-986",
      "org": "Supply Chain Dive",
      "title": "Why delivery robots face a regulatory ‘nightmare’",
      "published": "2023-04-26",
      "url": "https://www.supplychaindive.com/news/delivery-robot-bills-laws-proliferate-state-legislatures/648303/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 미국 주별 배송로봇 법규 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-987",
      "org": "The Pitt News",
      "title": "Pitt pauses testing of Starship robots due to safety concerns",
      "published": "2019-10-21",
      "url": "https://pittnews.com/article/151679/news/pitt-pauses-testing-of-starship-robots-due-to-safety-concerns/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 피츠버그 대학 Starship 시험 운행 중단 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-988",
      "org": "Open Navigation (Nav2)",
      "title": "Navigating Using GPS Localization — Nav2 documentation",
      "published": null,
      "url": "https://docs.nav2.org/jazzy/tutorials/general_tutorials/navigation2_with_gps/navigation2_with_gps/",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Nav2 의 GPS 위치추정 주행 튜토리얼.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-990",
      "org": "Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18)",
      "title": "Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists",
      "published": "2023-03",
      "url": "https://doi.org/10.1016/j.trip.2023.100789",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 보도 배송로봇과 보행자·자전거 상호작용 관측 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-991",
      "org": "대한민국 정책브리핑 (산업통상자원부·경찰청)",
      "title": "‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용",
      "published": "2023-11-16",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922726",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 개정 지능형로봇법·도로교통법 시행에 따른 실외이동로봇 보도 통행.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-993",
      "org": "Dobrosovestnova, A., Schwaninger, I., & Weiss, A. (IEEE RO-MAN 2022)",
      "title": "With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow",
      "published": "2022",
      "url": "https://ieeexplore.ieee.org/abstract/document/9900588/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 눈 속 고립 배송로봇과 행인 도움에 관한 탐색 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-995",
      "org": "Offshore Technology (Eve Thomas)",
      "title": "Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones",
      "published": "2025-11-21",
      "url": "https://www.offshore-technology.com/features/equinor-autonomous-robotics/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Equinor 시설의 4족 점검 로봇 운영 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-997",
      "org": "이코노미스트 (송재민)",
      "title": "로봇이 로봇들을 움직이는, 네이버 1784",
      "published": "2023-01-11",
      "url": "https://economist.co.kr/article/view/ecn202301110006",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 네이버 1784 클라우드 제어 배달 로봇 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1000",
      "org": "인더스트리뉴스 (정형우)",
      "title": "GS건설, 4족보행 로봇 '스팟(SPOT)' 국내 최초 건설현장 도입하기로",
      "published": "2020-07-13",
      "url": "https://www.industrynews.co.kr/news/articleView.html?idxno=38911",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. GS건설 스팟 도입과 BIM 데이터 통합 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1002",
      "org": "아주경제 (윤선훈)",
      "title": "아시아 최대 규모 데이터센터…네이버 '각 세종' 본격 가동",
      "published": "2023-11-08",
      "url": "https://www.ajunews.com/view/20231107091520837",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 데이터센터 서버 관리·운반 로봇 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1004",
      "org": "The Robot Report",
      "title": "Singapore's National Robotics Programme reveals initiatives to advance robot adoption",
      "published": "2025-10-29",
      "url": "https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 싱가포르 국가 로보틱스 프로그램 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1007",
      "org": "뉴스토마토 (이규하)",
      "title": "방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동",
      "published": "2025-04-23",
      "url": "https://www.newstomato.com/ReadNews.aspx?no=1259970",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 농촌진흥청 농업 로봇 통합 관리 프로그램 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1009",
      "org": "ISO",
      "title": "ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones",
      "published": "2024",
      "url": "https://www.iso.org/standard/82687.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 자율 농업기계의 자율 운용 구역 안전 표준.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1180",
      "org": "ILIAD 프로젝트 컨소시엄 (EU Horizon 2020)",
      "title": "Concluding ILIAD",
      "published": "2021-06",
      "url": "https://iliad-project.eu/concluding-iliad/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 창고 자율 지게차 플릿과 사람 흐름 기반 계획을 다룬 EU 프로젝트 정리.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/site-type-applications/index.md",
      "sections": [
        "5. 다른 대분류와의 연결"
      ],
      "rationale": "대분류 연결(category_link): '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 묶음 제안 — A. 기획·사업: f2·f22·f51 / C. 채팅 기반 구성·운영: f15·f30 / D. 공간·지도 모델: f37·f40·f43·f49 / E. 사물·사람·실시간 상태: f5·f18·f31·f38·f46·f50 / F. 연동: f1·f9·f10·f11·f16·f17·f19·f20·f25·f26·f28·f33·f34·f36·f41·f45·f48 / G. 계획·최적화: f3·f4·f7·f8·f24 / H. 실행·협업·예외 복구: f6·f13·f27·f29·f39 / I. 설계·시뮬레이션: f12 / J. 현장 운영·관제: f19·f34·f42 / K. 플랫폼 아키텍처·인프라: f23·f44 / L. AI·학습 기술: f15 / M. 안전: f3·f14·f21·f35·f47 / N. 보안·개인정보: f18·f21·f32 / O. 검증·도입·수명주기: f19·f49 / P. 거버넌스·법규·사회: f35·f37·f41. 벤더 주장(f9·f11·f14·f25)은 '벤더 주장' 병기, 연계 대상(f6·f40)은 짧게. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 섞지 않는다(f12 는 가정한 미래 실험 쪽). 모든 현장에 공통인 기능은 A~P 에 두고 이 절은 현장 사례가 넘기는 요구만 적는다."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "사람-대-상품",
      "term_en": "Person-to-Goods (PTG)",
      "definition": "작업자가 선반·보관 위치까지 걸어가 물품을 집는 피킹 방식으로, 설비·로봇이 선반을 작업자에게 가져오는 상품-대-사람 방식과 대비된다."
    },
    {
      "term_ko": "도어 투 도어 로봇 배송",
      "term_en": "Door-to-Door Robot Delivery",
      "definition": "공동주택 단지 입구에서 공동현관·승강기 연동을 거쳐 세대 현관 앞까지 로봇이 물품을 나르는 배송 방식이다."
    }
  ],
  "open_questions_new": [
    "병원·호텔·쇼핑몰·공동주택에서 로봇의 승강기 연동이 승강기 제조사 API, 승강기 관리 솔루션, 로봇팔 버튼 조작, 제어반 전용 통신 모듈로 갈리는데, 이 방식들을 한 현장에서 같은 승강기 인터페이스로 묶어 제조사가 다른 로봇이 함께 쓰게 한 사례나 방식별 비교 자료가 있는가? | 관련 영역: 22. 설비·건물 시스템 연동, 63. 병원·의료, 64. 상업 시설, 65. 가정·공동주택 | 근거: f16 | 종류: 일반",
    "병원·오피스처럼 5G 특화망으로 로봇을 연결하거나 클라우드에서 제어하는 현장에서 통신이 끊길 때 로봇의 현장 동작과 진행 중 작업의 재배정 기준을 공개한 사례가 있는가? | 관련 영역: 42. 분산 시스템·통신·컴퓨팅 구조, 63. 병원·의료, 67. 기타 현장 | 근거: f44 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 62,
    "cross_checked_count": 0,
    "unverified": [
      "직전 반환값(1회차 브리프)이 입력에 포함되지 않아 그 브리프의 신규 출처(예약 구간 ref-1539~)와 finding 을 확인할 수 없었다",
      "f3·f5 쿠팡 사례 두 보도는 같은 현장 공개 행사 기반이라 독립 교차 확인 아님",
      "f16 구로병원 전체 성공률 분모(oq-215) 미확인",
      "f19 한림대성심병원 통합관제의 인터페이스·표준(oq-174) 미확인",
      "f21 병원 감염 관리 구역 규칙(oq-172)과 영상 촬영 법 적용(oq-171) 미확인",
      "f31 공동주택 배송로봇 수령 인증 수단(oq-184) 미확인",
      "f36 이종 제조사 계층의 운행안전인증상 관제장치 해당 여부(oq-187) 미확인",
      "f9·f11·f14·f25 벤더 주장은 독립 확인 없음"
    ],
    "scope_violations": [
      "f6: 떨어진 상자 복구는 로봇 자체 지능·제어 경계라 claim 을 '연계 대상: '으로 시작하고 ROP 쪽은 재계획 분담만 다룸",
      "f40: GPS 위치추정은 로봇 자체 지능·제어 경계라 '연계 대상: '으로 표시",
      "f16·f20·f25·f26: 승강기 운행·호출 제어 자체는 시설·설비 제어 경계의 연계 대상이며 ROP 몫은 예약·상태 확인·제약 반영으로 한정해야 함",
      "f21·f32·f35·f41: 법 적용·인증 판단은 운영자·법무·인증 기관 쪽 연계 대상"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 0
    },
    "limits": "재실행 1회차. 반려 사유 1(스키마 불일치: f17 이 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시 없음): 지시에 따라 새 조사 없이 형식만 고쳤다. 다만 직전 반환값이 입력에 포함되지 않아 그대로 수정할 수 없었으므로, 입력으로 받은 게시 페이지(61. 물류창고 ~ 67. 기타 현장, A~G 대분류 연결 절)의 검증된 주장과 각주(기존 참고문헌 재사용)만으로 브리프를 다시 구성했다. 새 f17 은 RoMi-H 연결로 근거가 정부·연구기관·오픈소스 출처뿐이다. 벤더 문서만 근거로 한 finding(f9·f11·f14·f25)은 모두 tag 추정·vendor_claim true·evidence_excerpt 첫머리 '벤더 주장: '으로 냈고, [사실] finding 가운데 벤더 문서만 근거로 한 것은 없다(f31 은 기사 2건과 함께 인용). 검색 0회, WebFetch 0회, 신규 출처 0건으로 예약 구간 ref-1539~ref-1568 은 쓰지 않았다. 이번 실행에서 원문을 열지 않았으므로 모든 출처를 fetched false·source_unopened true 로 표시했고 신뢰도는 medium 이하다. 교차 확인 0건. 현장 유형: 물류창고(f1~f7·f50), 제조 공장(f8~f15), 병원(f16~f23·f49), 상업 시설(f24~f30), 가정(f31~f34), 실외(f35~f41), 기타(f42~f48)를 고르게 다뤘다. 34. 시뮬레이션·예측용 디지털 트윈(f12, 가정한 미래 실험)과 18. 실시간 세계 상태·데이터 일관성을 섞지 않았다. L. AI·학습 기술 연결 근거는 f15 하나뿐이다. 해결 제안한 열린 질문 없음. 입력 누락 없음. 우선 지정 질문·정정 요청 없음."
  }
}
```

### runs/2026-10-09-14/verification.json

```json
{
  "run_id": "2026-10-09-14",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-919 원문 열람(검증): 하차·입고(입고예정정보 확인·하역 작업·상품 검수·제품정보 인식 및 등록)와 상차·출고(발주처별 분류·차량 입차정보 인식·상차순서 관리·출고정보 전달) 항목 확인. 뒤의 '로봇 작업의 시작 조건과 완료 정보가 업무 시스템 단계에 묶여 있다'는 원문에 없는 해석이므로 [추정] 별도 문장으로 분리(수정 지시)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. ref-917·918 열람(층별 투입 확인), ref-257 열람: 현재 제목은 'AMR Multi-Fleet Orchestration Software: The Emerging Segment Growing 138% Annually'(Rueben Scriven, 2023-01)이며 다중 플릿 오케스트레이션이 WCS 부문의 전개를 닮았다고 서술 — 브리프의 제목·발행일(null)과 다르므로 각주는 61. 물류창고 페이지의 2023-01 표기로 맞춘다. ref-919 는 이 추정을 직접 뒷받침하지 않음."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-917: AGV 바닥 QR 코드 추종, 무인지게차 구역에 사람 이동 차단 확인. ref-918: 작업자가 안전구역을 침범하면 무인지게차가 즉시 멈춤. 그러나 두 기사 모두 '안전 센서'를 언급하지 않고 '그 구역에서만 주행'도 명시하지 않음. '안전 센서로'를 빼고 '사람 출입을 막은 구역에서 운영되며 작업자가 구역을 침범하면 멈춘다(ref-918)'로 고치는 조건으로 [사실] 유지. 같은 행사 기반이라 교차 확인 아님. 정지 기능은 로봇 자체 안전 기능(연계 대상)."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-005 열람: AAAI 2021 게재, v1 2020-05-15·v2 2021-03-12, 대규모 창고 시뮬레이션. ref-006 열람: AAMAS 2017, 초록에 자동화 창고·시뮬레이션 창고 언급. 두 논문 서술은 [사실] 유지, '대표 적용 대상이다'는 순위 표현이라 [추정]으로 분리(수정 지시)."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-917: 소팅봇이 운송장 바코드를 인식해 배송지별 분류·이송 확인. '출하 단계 완료 확인이 작업 대상 식별에 기댄다'는 해석이므로 [추정]으로 분리."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-921 열람: 떨어진 상자 자동 복구 개선이 향후 목표로 보도됨 확인. 추정 유지, '연계 대상' 표시 적절. 회사 계획 진술이므로 61. 물류창고 페이지처럼 '벤더 주장' 병기."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-912 열람: 반품 재적치를 정규 피킹 경로에 통합(피커 기반) 확인. 확인."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-922 원문 미열람(검증), 검색 결과(IJPR 57(24), 2019, 공급 정책 라인 적재·상자 공급·순서 공급·키팅) 일치. 뒤의 '라인 공급 작업을 나누는 기준을 제공한다'는 62. 제조 공장 페이지 8절이 [추정]으로 둔 추론이므로 [추정]으로 분리."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-924 열람: MLR 언더라이드 로봇 약 100대, 괴팅·린데 자율 견인차 40대, '135개 이상 장치' 안정 관제(CPO 발언), 하루 9,000랙(사진 설명은 최대 9,000). 벤더 주장·추정 표시 적절."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-925 열람: 생산 시스템 모델을 범용 계획기 입력 파일로 변환해 계획을 계산하고 모델에 다시 통합(ISA-95·PDDL 은 제목에만 명시). 논문 서술은 [사실], '생산 관리 쪽 요청을 실행 계획으로 옮기는 연결의 연구 근거가 된다'는 [추정]으로 분리."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-926 원문 미열람(검증), 62. 제조 공장 페이지 검증 기록 기준. 벤더 주장·추정 표시 적절."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-935·936 원문 미열람(검증), 게시 페이지 검증 기록 기준. 두 출처는 서로 다른 내용이라 교차 확인 아님. 기준일을 2014-04(ref-935)·2012(ref-936)로 각각 밝힐 것. 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험) 쪽 서술 적절."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-928 열람: 9개국 전문가 31명(64명 중 선별), 외골격과 협동로봇의 충돌 예측·방지, 차량 지붕 지지·공구 전달 확인. 논문은 '좁은 공간'을 핵심 과제로 명시하지 않으므로 '좁은 조립 공간에서' 수식은 빼거나 '차량 조립 현장에서'로 바꾼다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-938 열람: 사람 감지·제동·속도 제어·안정성을 보호 조치로 열거하고 구역 정의·분류 개선을 언급하나 '요구한다'고 단정하지 않음. '다룬다고 안내한다'로 표현을 낮추고 벤더 주장·표준 원문 미열람 유지."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. ref-932(2025-03-12, LLM·모방학습 조립 자동화, 자연어 명령 제어)·ref-931(2026-09-07, 자연어 지시 언급 없음) 열람 확인. 그러나 '확인된 자료는 … 뿐이다'는 조사 범위에 따른 부재 진술이며 62. 제조 공장 11절도 [추정]으로 둠. '조사 범위의 한계이며 부재를 뜻하지 않는다'를 함께 적는다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-943 열람: 전용 통신 모듈(TK50M), 122건(2025-06-18~29), EOR 59.01% 미만 95.52%, 전체 87.03% 확인. 단 원문은 실패의 EOR 이 상위 구간에 몰렸고 중앙값이 약 90%라고 적을 뿐 '90% 초과 구간'은 아님 — '실패 건의 승강기 가동률 중앙값이 약 90%로 상위 구간에 몰렸다'로 고치는 조건으로 [사실] 유지. 같은 논문이 ref-060·ref-1487 로도 등록돼 있음(중복)."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-937 열람: 네 도메인(기계·제어·중앙·통합), 이기종 로봇·센서·정보 시스템 연결 확인, '오픈소스'·'ROS 2'·'DDS' 문구는 없음. ref-942 열람: 'ROS 2 기반 오픈소스', 서로 다른 벤더 로봇의 승강기 공유, 다른 로봇에 대한 출입 금지 구역 확인, DDS 언급 없음. ref-872 열람: 2025-05-01부터 2년 유효, 통합사 5곳 확인. 'DDS'를 빼고 'ROS 2 기반 오픈소스'는 ref-942 에 귀속하는 조건으로 [사실] 유지."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "PMC 본문은 브라우저 확인 페이지로 열람 실패, Europe PMC 서지(Sci Rep 2026-04-24, Li M 외) 일치. 세부 수치는 63. 병원·의료 페이지 검증 기록 기준(원문 미열람(검증)). 같은 논문이 ref-1161 로도 등록돼 있음(중복). '협력 책임 체계'는 조직 역할 분담이라 51. 인증·권한·격리보다 RFID 신원 확인 쪽으로만 연결하는 편이 맞다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-944 열람: 7종 73대(2024-04), 커맨드센터 통합관제, '국내 최다종 로봇 연동 통합관제 플랫폼' 확인. LG전자·빅웨이브로보틱스 언급 없음, '정착 약 3년' 언급 없음. ref-941 열람: LG전자는 한림대성심병원에 배송로봇 공급, 빅웨이브로보틱스는 XaaS 과제로 시험할 예정(2024-07 기준)이며 정착 3년 언급 없음. '빅웨이브로보틱스가 공급' → '시험 예정'으로, '정착 약 3년'은 삭제(브리프 출처가 뒷받침하지 않음), '공개되지 않았다' → '확인되지 않았다(oq-174)'로 고치는 조건으로 [사실] 유지."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-945 열람: 2021-11-11 국가기술표준원의 로봇 엘리베이터 탑승 지원 KS 제정 발표(속도제어·보호정지·높낮이차·틈새) 확인, KS 번호·의무 여부는 본문에 없음. 앞 절은 [사실] 유지. 뒤 절 '병원 이송과 호텔 배송 사례가 모두 이 요구 아래 승강기를 쓴다'는 어느 출처도 뒷받침하지 않으므로 삭제. 같은 발표가 ref-315·ref-709 로도 등록돼 있고 F. 연동 페이지는 번호를 KS B 7317(ref-314)로 적음."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. ref-950·ref-978 원문 미열람(검증), ref-929 서지 확인. 법 판단·감염 관리 기준 설정을 연계 대상으로 둔 범위 처리 적절."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-948 열람: 속도·안전성, 대당 수억 원 비용, 경사·수동 문·건물마다 다른 제조사 승강기 확인. ref-947 원문 미열람(검증). 앞 절 [사실] 유지. 뒤 절 '확인된 국내 지원 제도는 … 실증사업이다'는 조사 범위 진술이므로 [추정]으로 분리하고, 63. 병원·의료 11절처럼 스마트병원 선도모델 사업(ref-950)도 함께 든 표현과 어긋나지 않게 '확인된 제도에는 … 이 있다'로 쓴다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-939 열람: KT 5G 특화망, AMR 6대, 승강기·자동문 다중 연동, 약 300m 워킹갤러리, 진료재료·약품·린넨 카트, 야간 배송 모두 확인."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "PMC 본문은 확인 페이지로 열람 실패, 검색으로 서지 확인: Han, L., Ding, J., Liu, S., & Meng, M., Sensors 25(6) 1783, 2025-03-13. 수치는 64. 상업 시설 페이지 검증 기록 기준(원문 미열람(검증)). 브리프의 기관 '저자 미확인'·발행일 null·as_of 2026-10-09 는 틀리므로 2025-03-13 으로 고친다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-957 열람: 로봇이 Otis Integrated Dispatch(클라우드 API)로 승강기 호출·탑승·층 선택, 호텔 케이한 유니버설 타워, 바쁜 밤 최대 60건 확인. 2022-12 는 구독 계약 체결 시점이며 24시간 배송 시작 시점은 원문에 없음 — '2022-12 부터'를 '2022-12 로봇 구독 계약 뒤'로 고치거나 삭제. 벤더 주장·추정 유지."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-963 열람: 2025-04-02 기사, 라이노스 휠리 J40, 클라우드 승강기 연동 솔루션 rEMS 로 전 층 자동 이동 확인. 승강기 연동 솔루션 자체는 설비 쪽 연계 대상."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-961·962 원문 미열람(검증), 64. 상업 시설 페이지 검증 기록 기준. AI Incident Database 는 보도를 모은 기록이라 두 출처가 독립 교차 확인은 아님."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-952 열람: 약 600개 매장, Tennant 바닥 청소기에 붙인 선반 스캔 부속(shelf-scanning accessory), 가격 정확도·재고 수준·진열 위치 데이터가 매장 관리자용 보고에 쓰임 확인. '재고 스캔 타워' 표현은 '선반 스캔 부속'으로 바꾼다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-953 원문 미열람(검증), 검색된 초록 일치: 음성 인식 어려움과 사람만 줄 수 있는 지식 때문에 일부 원격 조작, 25일 시험 2,642회 상호작용. 확인."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-868 열람: 영어·네덜란드어×성별 네 집단, Whisper 최저 WER, 참가자 40명 확인."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-965 열람: 공동현관 자동문·엘리베이터 호출 연동, '주문자만 배달음식 픽업이 가능' 설명, 인증 수단 언급 없음. ref-966: 엘리베이터 자동 호출 실내 배송은 있으나 공동현관 연동 없음. ref-979: 삼성물산 공동현관·승강기 연동 언급. '주문자만 꺼낼 수 있다'는 ref-965(회사 발표)에만 기대므로 '삼성물산은 … 설명한다'로 귀속하거나 '벤더 주장'을 병기하고, '인증 수단은 공개되지 않았다'는 '확인되지 않았다(oq-184)'로 고친다."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-968 열람: iRobot 개발용 로봇 이미지가 Scale AI 라벨링 외주를 거쳐 15장 게시 확인. ref-978(CaseNote) 페이지는 이번에 열지 않았으나 조문 내용은 다른 검색 결과로 일치 확인(원문 미열람(검증))."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-977 열람: Matter 1.2(2023-10-23) 로봇청소기 기기 유형, 기본 제어·진행 업데이트, 브러시·오류·충전 상태 보고 확인."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-976 열람: 송장번호 인식→관제실 물품정보 전송, 단지 단위 중앙집하·동 단위·지역(Zone) 단위 분산집하 세 방식 확인."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-991 열람 실패(연결 재설정 2회), 검색 결과(같은 날 산업부·경찰청 발표 보도)로 17일 시행·보행자 지위·보험(공제) 의무 일치. ref-980 열람: 인증 대상이 '실외이동로봇과 그 운행에 필요한 관제장치 조합의 일체' 확인. 두 출처는 서로 다른 부분을 뒷받침."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. ref-980 열람으로 조합 인증 확인, 관제장치 해당 여부는 oq-187 로 남김."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-987 열람은 403, 검색 결과 일치: 연석 경사로를 막아 휠체어 이용자가 차도에 갇힘, 두 시간이 채 안 돼 시험 중단, 해당 교차로 지도 소프트웨어 수정. 확인."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-990 열람은 리디렉트로 실패, 검색 결과(TRIP 18, 2023-03, NAU 캠퍼스 10곳 1주 영상, PET) 일치. 같은 논문이 ref-1481 로도 등록돼 있음(중복)."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-993 열람은 418, 검색 결과(RO-MAN 2022, 탈린의 상용 배송로봇을 행인이 도운 사례의 탐색 연구) 일치. 확인."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-988 열람: GPS 위치추정으로 실외에서 Nav2 를 쓰는 튜토리얼 확인. 뒤 절 '로봇 자체 지능·제어 쪽 기능'은 분류 원문 19장 경계에 따른 구분이며 '연계 대상' 표시 적절."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. ref-986 열람: 주마다 크기·무게·속도가 다름(조지아 500lb·약 4mph, 뉴햄프셔 10mph·80lb), 신고 규정은 다루지 않음. ref-985 는 검색으로 일본 개정법(원격 조작형 소형차, 공안위원회 신고) 확인. '신고' 차이는 일본 출처에만 기댐을 밝힐 것."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-995 열람: 계기·밸브 위치 판독, CO₂ 감지·누출 분석, 운영자가 스스로 임무를 만들기 시작함 확인. 기사는 Northern Lights 를 '장차 무인화될 시설'로만 적고 CCS 시설이라고 쓰지 않으므로 'Northern Lights 시설'로 고친다. 23. 업무 시스템 연동 연결은 근거가 없어 oq-194 를 가리키는 데 그친다."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1000 열람: 스팟 수집 데이터를 3차원 BIM 데이터와 통합해 전기·설비 공사 간섭 확인과 안전관리계획 수립에 활용 확인."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-997 열람: ARC(네이버 클라우드 기반)가 루키를 제어, 초저지연 5G·5G 특화망, 40대→100여 대 확인. 로보포트는 '전용 엘리베이터를 타고 충전소로 이동'하는 장면만 있어 '층을 오간다'는 '로봇 전용 엘리베이터 로보포트를 탄다'로 낮춘다."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1007 열람: 방제(2022)·운반(2023)·모니터링(2024) 로봇을 PC·휴대전화 하나로 관리, 다른 제조사 로봇 연결 언급 없음 확인."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1002 열람: 세로·가로 로봇으로 자산 흐름을 실시간 추적해 하나의 시스템으로 통합 관리 확인(협력 방식 세부는 없음)."
    },
    {
      "finding_id": "f47",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1009 열람(ISO 발행 기관 자료): 2024-07-31 발행, 자율 운용 구역 경계를 벗어나지 않게 하는 기계 쪽 설계 원칙을 다루며 '자율 운용 구역 자체는 범위 밖'이라고 명시. '자율 운용 구역을 다루어'를 '자율 운용 구역 경계 이탈을 막는 기계 쪽 안전 요구를 다룬다(구역 자체는 범위 밖)'로 고치고, '운용 구역이 ROP 의 운행 제약 입력이 된다'는 [추정]으로 분리하는 조건으로 [사실] 유지."
    },
    {
      "finding_id": "f48",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. ref-1004 열람: RMF 가 CGH 와 창이 공항에서 쓰인다고 적고 사진 설명에 Avidbots 청소 로봇이 있으나, 청소 로봇이 RMF 로 운영된다고는 명시하지 않음. 'RMF 가 창이 공항에서 쓰인다는 기사가 있으나 청소 로봇과의 연결은 명시되지 않았다'로 고친다."
    },
    {
      "finding_id": "f49",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-869 열람: 교통 편집기 주석(벽·차선·충전기·문), 격자 지도 정합, 중환자실→검사실 혈액 검체, 작은 구역 매핑 후 수동 병합이 더 정확하다는 경험적 권고 확인."
    },
    {
      "finding_id": "f50",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1180 열람: 외레브로(Orkla Foods) 창고 두 곳, 트럭이 사람 움직임 패턴을 고려해 경로 계획, 움직임 지도 확인. 게시일은 2021-07-14 로 보이며 참고문헌의 2021-06 과 다름 — 기준일 표기를 확인할 것."
    },
    {
      "finding_id": "f51",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지하되 내용 수정 필요. ref-944 는 '국내 최다종 로봇 연동 통합관제 플랫폼'을 적고, 63. 병원·의료 페이지 9절은 한림대성심병원 통합관제를 제조사가 다른 로봇 공존의 '가장 가까운 공개 사례(인터페이스·표준 미확인)'로 둔다. f51 의 세 유형(설비별 도입·건설사-로봇 업체 짝·자체 계층)에 한림대 사례가 들어가지 않아 근거 출처(ref-944)와 기존 게시 페이지에 어긋난다. 한림대 사례를 '여러 제조사 로봇의 통합관제가 보도됐으나 인터페이스·표준은 미확인'으로 따로 적고, 결론을 '인터페이스까지 공개된 국내 사례는 확인되지 않았다'로 좁힌다."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": false,
    "issues": [
      "f3: 무인지게차의 침범 감지·정지는 로봇 자체 안전 기능이므로 49. 사람 근접 안전 연결에서 '연계 대상'으로 두고, ROP 몫은 구역 분리 규칙의 반영·확인으로 한정한다",
      "f16·f20·f25·f26: 승강기 호출·운행·제어반 통신 모듈·rEMS·OID 는 분류 원문 19장 시설·설비 제어 경계의 연계 대상이다. ROP 몫은 승강기 예약·상태 확인·혼잡 제약 반영으로만 서술한다",
      "f21·f32·f35·f41: 감염 관리 기준 설정, 개인정보 보호법·지능형로봇법 적용 판단, 운행안전인증 취득은 운영자·법무·인증 기관 쪽 연계 대상이며 ROP 는 해당 조건을 경로·권한·속도 제약으로 반영하는 쪽만 맡는다",
      "f44: 브레인리스 로봇을 클라우드 ARC 가 직접 제어하는 구조는 네이버 자체 로봇·플랫폼의 사례이며, ROP 직접 범위 사례처럼 쓰지 않는다",
      "f47: 농업기계의 자율 운용 구역 이탈 방지는 기계 쪽 안전 기능(연계 대상)이고 구역 정의 자체는 표준 범위 밖이다"
    ]
  },
  "duplication": {
    "ok": false,
    "overlaps": [
      "f51 ↔ 63. 병원·의료 9절과 f19: 한림대성심병원 통합관제를 제조사가 다른 로봇 공존의 가장 가까운 국내 공개 사례로 둔 게시 서술과 충돌 — 둘 다 반영하고 결론을 좁힌다",
      "f20 ↔ F. 연동 대분류 연결 절: 같은 KS 를 KS B 7317(ref-314)로 이미 [사실] 기재. f20 의 '번호·조항은 oq-173 미확인'과 충돌하지 않게 번호는 F. 연동 쪽 서술을 링크로 넘긴다",
      "같은 문헌의 중복 참고문헌 id: ref-943·ref-060·ref-1487(구로병원 Digital Health 논문), ref-929·ref-1161(Scientific Reports 병원 물류 로봇 논문), ref-990·ref-1481(Gehrke 외 보도 로봇 논문), ref-945·ref-315·ref-709(국가기술표준원 KS 발표). 이 페이지에서는 브리프의 id(ref-943·ref-929·ref-990·ref-945)만 쓰고, 통합은 퍼블리셔·참고문헌 담당 과제로 남긴다",
      "f17·f19·f49·f50·f30·f15 등 다수 연결이 C. 채팅 기반 구성·운영, D. 공간·지도 모델, E. 사물·사람·실시간 상태 대분류 페이지의 'Q. 현장 유형별 적용' 항목에 이미 같은 각주로 실려 있다 — 같은 각주를 재사용하고 '같은 연결은 … 페이지에도 있다'로 표시한다",
      "f16·f17·f19·f25·f3 의 교정 사항(가동률 90% '초과', RoMi-H 'DDS', 빅웨이브로보틱스 '공급', 오티스 '2022-12 부터', 쿠팡 '안전 센서')은 각각 63. 병원·의료, 64. 상업 시설, 61. 물류창고 게시 페이지에도 같은 표현으로 남아 있어 게시 페이지와 이 절이 어긋나게 된다"
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
    "page_proposals 의 섹션 이름: '5. 다른 대분류와의 연결'이 아니라 대분류 페이지 정본 제목인 '다른 대분류와의 연결'(번호 없음) 절 하나만 patches(action replace)로 바꾼다 — 대분류 H2 에는 번호가 없고, 다른 절·auto 마커는 건드리지 않는다.",
    "f1·f4·f5·f8·f10·f47: 출처가 직접 말한 부분만 [사실]로 두고, 연결 해석 부분(f1 '업무 시스템 단계에 묶여 있다', f4 '대표 적용 대상이다', f5 '완료 확인이 식별에 기댄다', f8 '나누는 기준을 제공한다', f10 '연결의 연구 근거가 된다', f47 '운행 제약 입력이 된다')은 별도 문장으로 나눠 [추정]을 붙인다 — 해석은 출처에 없고 62. 제조 공장 8절도 같은 추론을 [추정]으로 두었다.",
    "f15: [사실] → [추정]으로 강등하고 '조사 범위의 한계이며 부재를 뜻하지 않는다(oq-142)'를 함께 적는다 — '확인된 자료는 … 뿐이다'는 부재 진술이다.",
    "f3: '경계 침범 시 안전 센서로 정지'를 '작업자가 구역을 침범하면 무인지게차가 멈춘다'(ref-918)로 고치고 '안전 센서'는 빼며, 정지 기능은 로봇 자체 안전 기능(연계 대상)으로 표시한다 — 두 기사에 안전 센서 언급이 없다.",
    "f16: '실패가 가동률 90% 초과 구간에 몰렸다'를 '실패 건의 승강기 가동률 중앙값이 약 90%로 상위 구간에 몰렸다'로 고친다 — 원문(ref-943)은 90%를 중앙값으로 적는다. 승강기 제어 자체는 연계 대상으로 적는다.",
    "f17: 'ROS 2·DDS 기반 오픈소스'에서 'DDS'를 빼고 'ROS 2 기반 오픈소스'는 ref-942 에, 네 도메인·이기종 연결은 ref-937 에, 2년 유효·통합사 5곳은 ref-872 에 각주를 나눠 단다 — ref-937·942 어디에도 DDS 가 없다.",
    "f19: 'LG전자와 빅웨이브로보틱스가 배송로봇을 공급하며'를 'LG전자가 배송로봇을 공급하고 빅웨이브로보틱스는 이 병원에서 로봇을 시험할 예정(2024-07 기준)'으로 고치고, '시스템 정착에 약 3년'은 삭제하며, '공개되지 않았다'는 '확인되지 않았다(oq-174)'로 바꾼다 — ref-944·941 은 정착 3년을 말하지 않고 빅웨이브로보틱스는 시험 예정으로만 적는다.",
    "f20: 둘째 절 '병원 이송과 호텔 배송 사례가 모두 이 요구 아래 승강기를 쓴다'를 삭제한다 — 어떤 출처도 사례 로봇의 KS 준수를 뒷받침하지 않는다. KS 번호는 F. 연동 대분류 페이지 연결 절(KS B 7317)로 링크만 건다.",
    "f22: 앞 절(장애 요인 보도)은 [사실], 뒤 절 '확인된 국내 지원 제도'는 [추정]으로 분리하고 63. 병원·의료 11절과 맞게 '확인된 제도에는 과제 단위 서비스로봇 실증사업 등이 있다'로 쓴다.",
    "f24: ref-103 각주·출처를 'Han, L., Ding, J., Liu, S., & Meng, M. (Sensors 25(6)), …, 2025-03-13'으로 적고 기준일을 2025-03-13 으로 한다 — 64. 상업 시설 페이지 각주와 같고 검색으로 확인됐다. reference_updates 로 ref-103 의 기관·발행일 정정을 요청한다.",
    "f25: '오사카 호텔에서 2022-12 부터 24시간 객실 배송'을 '오사카 호텔(2022-12 로봇 구독 계약)에서 24시간 객실 배송을 한다고 설명한다'로 고치고 [추정] 벤더 주장을 유지한다 — 2022-12 는 계약 시점이다.",
    "f28: '재고 스캔 타워'를 '선반 스캔 부속'으로 바꾼다 — ref-952 표현과 맞춘다.",
    "f31: '주문자만 음식을 꺼낼 수 있는 방식으로 넘기며'를 '삼성물산은 주문자만 음식을 꺼낼 수 있다고 설명한다'로 귀속하거나 '벤더 주장'을 병기하고, '인증 수단은 공개되지 않았다'를 '인증 수단은 확인되지 않았다(oq-184)'로 바꾼다 — 근거가 회사 발표(ref-965) 하나다.",
    "f42: '이산화탄소 포집·저장 시설'을 'Northern Lights 시설(장차 무인화 예정)'로 고친다 — ref-995 는 CCS 시설이라고 쓰지 않는다. 23. 업무 시스템 연동 연결은 oq-194 를 가리키는 데 그친다.",
    "f44: '로보포트로 층을 오간다'를 '로봇 전용 엘리베이터 로보포트를 탄다'로 낮춘다 — ref-997 은 충전소로 가는 장면만 적는다.",
    "f13: '좁은 조립 공간에서'를 '차량 조립 현장에서'로 바꾼다 — ref-928 은 좁은 공간을 핵심 과제로 명시하지 않는다.",
    "f14: 'ISO 3691-4:2023 이 … 요구한다고 안내하며'를 '… 를 다룬다고 안내하며'로 낮추고 [추정] 벤더 주장·표준 원문 미확인(oq-170)을 유지한다 — ref-938 은 요구 내용을 설명하지 않는다.",
    "f48: 'Open-RMF 가 청소 로봇 운영에 쓰인다는 기사'를 'RMF 가 창이 공항에서 쓰인다는 기사가 있으나 청소 로봇과의 연결은 명시되지 않았다'로 고친다.",
    "f51: 결론을 다시 쓴다 — 한림대성심병원은 여러 종류·제조사 로봇의 통합관제가 보도된 국내 사례(ref-944, 63. 병원·의료 9절)로 따로 적고, '제조사가 다른 로봇을 하나의 계층으로 묶으면서 그 인터페이스·표준까지 공개한 국내 사례는 확인되지 않았다(조사 범위의 한계)'로 좁힌다. [추정] 유지.",
    "f2·f9·f11·f14·f25 와 f6(회사 계획 진술)은 본문에 [추정]과 '벤더 주장'을 함께 쓰고 태그 앞 본문에 병기한다.",
    "범위 경계: f3·f16·f20·f25·f26·f40·f44·f47 의 로봇 자체 안전·위치추정, 승강기·설비 제어, 업종별 법·인증 판단은 '연계 대상'으로 짧게 적고 ROP 몫(요청·예약·상태 확인·제약 반영)만 직접 범위로 서술한다.",
    "근거 finding 이 없는 B. 로봇 온톨로지(4~7번 세부영역)와, 근거가 한 건뿐인 I. 설계·시뮬레이션(f12)·L. AI·학습 기술(f15)·K. 플랫폼 아키텍처·인프라(f23·f44)는 '아직 다루지 않은 연결' 또는 근거 한계와 함께 적는다. 브리프 rationale 의 묶음에 f30 을 P. 거버넌스·법규·사회(60. 노동·수용성·접근성)에, f13 을 M. 안전(49. 사람 근접 안전)에 더한다.",
    "이미 C. 채팅 기반 구성·운영·D. 공간·지도 모델·E. 사물·사람·실시간 상태 대분류 페이지에 실린 같은 연결(f15·f17·f19·f30·f31·f49·f50 등)은 새 각주를 만들지 말고 같은 각주 id 를 재사용하며 '같은 연결은 … 페이지에도 있다'를 붙인다.",
    "각주 정의는 '참고 자료' 절에 브리프 sources 와 같은 기관·제목·발행일·URL 로 두되 접근일은 2026-10-09 로 하고 이번 리서치가 원문을 열지 않았으므로 모두 접근일 뒤에 ' (원문 미열람)'을 붙인다. ref-257 은 61. 물류창고 각주처럼 'Interact Analysis (Rueben Scriven) … 2023-01'로 적는다(현재 페이지 제목은 'AMR Multi-Fleet Orchestration Software: The Emerging Segment Growing 138% Annually'로 바뀌어 있어 reference_updates 로 제목 갱신을 요청한다).",
    "모든 [사실] 문장에 기준일(발행일)을 남긴다. 특히 as_of 가 '2026-10-09'로 된 f1·f11·f14·f25·f40 은 '발행일 미확인, 확인일 2026-10-09'로, f50 은 ILIAD 게시일(2021-07-14 로 보임, 참고문헌 2021-06)과의 차이를 보이지 않게 단정하지 말고 참고문헌 표기를 따른다.",
    "open_questions_new 첫 질문의 근거를 'f16'에서 승강기 방식 세 가지를 모두 담는 쪽으로 보강할 수 없으면 그대로 두되, 질문 본문 끝에 관련 기존 질문 oq-176·oq-182·oq-191 을 밝혀 중복이 아님을 드러낸다. 둘째 질문은 oq-038(외부망 단절)과 대상 현장이 달라 등록한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 42건, 미확인 9건(f3·f15·f16·f17·f19·f20·f25·f47·f51), 교차 확인 0건. 강등: f15 사실 → 추정, 그리고 f1·f4·f5·f8·f10·f22·f47 의 연결 해석 부분을 [추정]으로 분리, f20 둘째 절 삭제. 원문 미열람 출처: 브리프는 이번 실행에서 원문을 열지 않아 62건 전부를 원문 미열람으로 표시했다(재실행 1회차, 검색 0회). 검증에서 47건을 직접 열거나 서지를 확인했고, ref-922·926·935·936·947·950·953·961·962·978·985·987·990·991·993 은 검색 결과 일치로만, ref-103·ref-929 는 서지만 확인했다(본문 미열람). 주의: 모든 연결이 게시된 61. 물류창고~67. 기타 현장 페이지와 다른 대분류 연결 절의 재인용이고 사실 주장도 단일 출처라 교차 확인이 없다. 검증 중 게시 페이지와 원문이 어긋나는 표현 다섯 곳을 찾았다 — 63. 병원·의료의 '실패가 가동률 90% 초과 구간에 집중'(원문은 중앙값 약 90%), 'RoMi-H ROS 2·DDS 기반'(원문에 DDS 없음), '빅웨이브로보틱스가 배송로봇 공급'(원문은 시험 예정), 64. 상업 시설의 '2022-12부터 24시간 배송'(원문은 계약 시점), 61. 물류창고의 '안전 센서로 정지'(원문에 센서 언급 없음). 이 절에서는 고쳐 쓰고, 해당 세부영역 페이지는 정정 요청이나 다음 갱신 실행으로 다시 확인해야 한다. 같은 문헌이 여러 참고문헌 id 로 등록된 경우(ref-943·060·1487, ref-929·1161, ref-990·1481, ref-945·315·709)도 통합이 필요하다. B. 로봇 온톨로지와의 연결은 근거가 없다. 정정 요청 없음. 해결 제안된 열린 질문 없음.",
  "retry_reason": null
}
```

### runs/2026-10-09-14/pages.json

```json
{
  "run_id": "2026-10-09-14",
  "outline": [
    {
      "path": "docs/categories/site-type-applications/index.md",
      "section": "다른 대분류와의 연결",
      "budget_chars": 9500,
      "summary": "61. 물류창고 ~ 67. 기타 현장의 게시 사례는 F. 연동(승강기·업무 시스템·제조사 관제)과 G. 계획·최적화에 가장 많은 요구를 넘기며, 제조사가 다른 로봇을 하나의 계층으로 묶으면서 인터페이스·표준까지 공개한 국내 사례는 확인되지 않았다. [추정][^ref-944] B. 로봇 온톨로지와의 연결은 근거가 없고 I·K·L 은 근거가 한두 건뿐이다.",
      "planned_findings": [
        "A: f2, f22, f51",
        "B: 근거 없음",
        "C: f15, f30",
        "D: f49, f43, f37, f40",
        "E: f5, f18, f31(수령), f46, f50, f38",
        "F: f9, f17, f19, f36, f45, f48, f33, f41, f16, f20, f25, f26, f31(연동), f44, f1, f10, f11, f28, f34, f42(oq-194)",
        "G: f8, f7, f24, f3(QR), f4, f16(28)",
        "H: f13, f27, f29, f39, f6",
        "I: f12",
        "J: f19, f34, f42",
        "K: f23, f44",
        "L: f15",
        "M: f21, f47, f3(정지), f13, f14, f20, f35",
        "N: f21, f32",
        "O: f49",
        "P: f35, f41, f30, f37"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/site-type-applications/index.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "'다른 대분류와의 연결' 절 신규 작성: 현장 사례가 A·C~P 대분류의 세부영역에 넘기는 요구를 대분류별로 정리(B. 로봇 온톨로지는 근거 없음), 각주 정의 62건을 절 끝에 둠",
      "patches": [
        {
          "section": "다른 대분류와의 연결",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-14/pages/categories/site-type-applications/index.md 의 해당 절을 본다)"
        }
      ]
    }
  ],
  "changelog_entry": "2026-10-09 | Q. 현장 유형별 적용 | 다른 대분류와의 연결 절 신규 작성(현장 사례가 A·C~P 대분류 세부영역에 넘기는 요구 정리, B. 로봇 온톨로지는 근거 없음) | run 2026-10-09-14",
  "index_updates": {
    "home_recent": "2026-10-09 — Q. 현장 유형별 적용: '다른 대분류와의 연결' 절 신규 작성. 61. 물류창고 ~ 67. 기타 현장 사례가 F. 연동·G. 계획·최적화 등에 넘기는 요구를 대분류별로 정리",
    "category_recent": "2026-10-09 — Q. 현장 유형별 적용: '다른 대분류와의 연결' 절 신규 작성(A·C~P 대분류 연결, 승강기·설비 제어와 법·인증 판단은 연계 대상으로 구분, B. 로봇 온톨로지 연결은 근거 없음)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "door-to-door-robot-delivery",
      "term_ko": "도어 투 도어 로봇 배송",
      "term_en": "Door-to-Door Robot Delivery",
      "definition": "공동주택 단지 입구에서 공동현관·승강기 연동을 거쳐 세대 현관 앞까지 로봇이 물품을 나르는 배송 방식이다.",
      "related_areas": [
        65,
        22
      ],
      "sources": [
        "ref-965",
        "ref-979"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-103",
      "org": "Han, L., Ding, J., Liu, S., & Meng, M. (Sensors 25(6))",
      "title": "The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments",
      "published": "2025-03-13",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 다층 호텔 배송 로봇 경로 계획에서 승강기 대기·운행 시간을 모델링한 논문. 1차 검증에서 저자·학술지(Sensors 25(6) 1783)·발행일(2025-03-13)을 검색으로 확인해 기관·발행일을 정정한다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/site-type-applications/index.md"
      ]
    },
    {
      "id": "ref-257",
      "org": "Interact Analysis (Rueben Scriven)",
      "title": "AMR Multi-Fleet Orchestration Software: The Emerging Segment Growing 138% Annually",
      "published": "2023-01",
      "url": "https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 다중 플릿 오케스트레이션 소프트웨어의 시장 정의. 1차 검증에서 현재 페이지 제목이 바뀌어 있음(구 제목 'AMR Multi-Fleet Orchestration Software Explained')과 저자·발행 시점(2023-01)을 확인해 제목 갱신을 요청한다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/site-type-applications/index.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "병원·호텔·쇼핑몰·공동주택에서 로봇의 승강기 연동이 승강기 제조사 API, 승강기 관리 솔루션, 로봇팔 버튼 조작, 제어반 전용 통신 모듈로 갈리는데, 이 방식들을 한 현장에서 같은 승강기 인터페이스로 묶어 제조사가 다른 로봇이 함께 쓰게 한 사례나 방식별 비교 자료가 있는가(관련 기존 질문 oq-176 은 오케스트레이션 계층, oq-182 는 공동주택 연동 절차, oq-191 은 싱가포르 표준을 묻고, 이 질문은 승강기 연동 방식 간 비교를 묻는다)?",
      "areas": [
        22,
        63,
        64,
        65
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "병원·오피스처럼 5G 특화망으로 로봇을 연결하거나 클라우드에서 제어하는 현장에서 통신이 끊길 때 로봇의 현장 동작과 진행 중 작업의 재배정 기준을 공개한 사례가 있는가?",
      "areas": [
        42,
        63,
        67
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [],
  "standards_updates": [],
  "additional_research_requests": [
    "B. 로봇 온톨로지 연결: 현장 사례(병원·공동주택·제조 공장 등)에서 4. 이기종 로봇 등록·5. 로봇 능력·작업 표현을 다룬 근거가 브리프에 없어 '아직 다루지 않은 연결'로 두었다. 현장 도입 시 이기종 로봇 등록·능력 기술 방식을 보고한 자료가 필요하다.",
    "I. 설계·시뮬레이션: 33. 시나리오 모델·편집과 36. 가상 시운전·실제 상황 재현의 현장 사례(oq-134) 근거가 없어 연결이 한 건(제조 공장 시뮬레이션)뿐이다.",
    "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API·43. 데이터·관측성·배포, L. AI·학습 기술의 45~47번 영역에 대한 현장 사례 근거가 없다.",
    "O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 한림대성심병원 '정착 약 3년' 서술이 출처로 뒷받침되지 않아 삭제되면서 연결 근거가 없어졌다. 현장 운영 이관·확대 기간을 보고한 자료가 필요하다.",
    "N. 보안·개인정보의 51. 인증·권한·격리: 수령인 인증(oq-293, oq-184)을 다룬 현장 근거가 없어 연결을 넣지 않았다.",
    "정정 확인 필요(조사 요청이 아니라 게시 페이지 재검증): 1차 검증이 게시 페이지와 원문이 어긋난다고 본 다섯 곳 — 63. 병원·의료의 '실패가 가동률 90% 초과 구간에 집중'(원문은 중앙값 약 90%), 'RoMi-H ROS 2·DDS 기반'(원문에 DDS 없음), '빅웨이브로보틱스가 배송로봇 공급'(원문은 시험 예정), 64. 상업 시설의 '2022-12부터 24시간 배송'(원문은 계약 시점), 61. 물류창고의 '안전 센서로 정지'(원문에 센서 언급 없음). 정정 요청 또는 다음 갱신 실행으로 다시 확인해야 한다.",
    "f17·f19·f31 연결이 C·D·E 대분류 페이지 가운데 어디에 이미 실렸는지 입력에 없어 '같은 연결은 … 페이지에도 있다' 표시를 하지 못했다. 해당 대분류 페이지의 연결 절 확인이 필요하다.",
    "중복 참고문헌 id 통합(참고문헌 담당): ref-943·ref-060·ref-1487, ref-929·ref-1161, ref-990·ref-1481, ref-945·ref-315·ref-709. 이 페이지에서는 브리프 id 만 썼다.",
    "ref-1180(ILIAD) 게시일이 2021-07-14 로 보인다는 검증 지적이 있어 참고문헌 표기(2021-06) 확인이 필요하다."
  ],
  "fixes_applied": [
    "섹션 이름 — 대분류 정본 제목 '다른 대분류와의 연결'(번호 없음) 한 절만 patches(action replace)로 바꾸고 다른 절·auto 마커는 건드리지 않았다.",
    "f1·f4·f5·f8·f10·f47 — 출처가 직접 말한 부분은 [사실] 문장으로 두고, 연결 해석(업무 시스템 단계에 묶임, 대표 적용 대상, 완료 확인이 식별에 기댐, 라인 공급 작업을 나누는 기준, 연결의 연구 근거, 운행 제약 입력)은 별도 문장으로 나눠 [추정]을 붙였다.",
    "f15 — C. 채팅 기반 구성·운영 항목에서 [추정]으로 강등해 쓰고 '조사 범위의 한계이고 부재를 뜻하지 않는다(oq-142)'를 함께 적었다.",
    "f3 — '안전 센서'를 빼고 '작업자가 구역을 침범하면 무인지게차가 멈춘다'(ref-917·ref-918)로 고쳐 M. 안전 항목에 두었고, 정지 기능을 로봇 자체 안전 기능(연계 대상)으로 표시했다. QR 코드 경로 부분은 G. 계획·최적화 항목에 따로 두었다.",
    "f16 — '실패 건의 승강기 가동률 중앙값이 약 90%로 상위 구간에 몰렸다'로 고치고, 승강기 제어·제어반 통신 모듈은 연계 대상이라는 문장을 덧붙였다.",
    "f17 — 'DDS'를 빼고 네 도메인·이기종 연결은 ref-937, 'ROS 2 기반 오픈소스'·승강기 공유·출입 금지 구역은 ref-942, 2년 유효·통합사 5곳은 ref-872 로 문장별 각주를 나눴다.",
    "f19 — 'LG전자가 배송로봇을 공급하고 빅웨이브로보틱스는 이 병원에서 로봇을 시험할 예정(2024-07 기준)'으로 고치고 '정착 약 3년'을 삭제했으며 '인터페이스·표준은 확인되지 않았다(oq-174)'로 썼다. 이 삭제로 O. 검증·도입·수명주기의 56. 운영 이관·확대·교육 연결은 근거가 없어 '아직 다루지 않은 연결'로 두었다.",
    "f20 — 둘째 절('병원 이송과 호텔 배송 사례가 모두 이 요구 아래 승강기를 쓴다')을 삭제하고 KS 번호는 F. 연동 대분류 페이지 연결 절(../integration/index.md#다른-대분류와의-연결)로 링크만 걸었다.",
    "f22 — 장애 요인 보도는 [사실], 지원 제도는 '확인된 국내 지원 제도에는 과제 단위의 서비스로봇 실증사업 등이 있다' [추정]으로 분리했다.",
    "f24 — ref-103 각주를 'Han, L., Ding, J., Liu, S., & Meng, M. (Sensors 25(6)), …, 2025-03-13'으로 적고 본문 기준일을 2025-03-13 으로 했으며 reference_updates 로 ref-103 의 기관·발행일 정정을 요청했다.",
    "f25 — '오사카 호텔(2022-12 로봇 구독 계약)에서 24시간 객실 배송을 한다고 설명한다'로 고치고 [추정]·벤더 주장을 유지했다.",
    "f28 — '재고 스캔 타워'를 '선반 스캔 부속'으로 바꿨다.",
    "f31 — 공동현관·승강기 연동은 [사실](ref-965·ref-979)로 F. 연동의 22. 설비·건물 시스템 연동 항목에 두고, 수령 방식은 '삼성물산은 주문자만 음식을 꺼낼 수 있다고 설명하며'로 귀속하면서 벤더 주장·[추정]을 함께 병기해 E. 사물·사람·실시간 상태 항목에 두었으며, '인증 수단은 확인되지 않았다(oq-184)'로 바꿨다.",
    "f42 — 'Northern Lights 시설(장차 무인화 예정)'로 고쳐 J. 현장 운영·관제 항목에 두고, 23. 업무 시스템 연동 쪽은 oq-194 를 가리키는 문장에 그쳤다.",
    "f44 — '로보포트로 층을 오간다'를 '로봇 전용 엘리베이터 로보포트를 탄다'로 낮췄다.",
    "f13 — '좁은 조립 공간에서'를 '차량 조립 현장에서'로 바꿨다.",
    "f14 — '… 를 다룬다고 안내하며'로 낮추고 [추정]·벤더 주장·표준 원문 미확인(oq-170)을 유지했다.",
    "f48 — 'RMF 가 창이 공항에서 쓰인다는 기사가 있으나 청소 로봇과의 연결은 명시되지 않아 …'로 고쳤다.",
    "f51 — A. 기획·사업 항목에서 세 유형 서술 뒤에 한림대성심병원을 여러 종류·제조사 로봇의 통합관제가 보도된 국내 사례(ref-944, 63. 병원·의료)로 따로 적고, 결론을 '인터페이스·표준까지 공개한 국내 사례는 확인되지 않았고 조사 범위의 한계이며 부재를 뜻하지 않는다'로 좁혔다. [추정] 유지.",
    "벤더 주장 병기 — f2·f9·f11·f14·f25 와 f6(회사 계획 진술) 문장에 [추정]을 쓰고 태그 앞 본문에 '벤더 주장'을 병기했다. f2 는 1차 검증이 직접 뒷받침하지 않는다고 본 ref-919 를 각주에서 뺐다.",
    "범위 경계 — f3·f16·f20·f25·f26·f40·f44·f47 의 로봇 자체 안전·위치추정, 승강기·설비 제어(호출·제어반 모듈·rEMS·OID), 농업기계 구역 이탈 방지, 네이버 자체 플랫폼 구조를 연계 대상 또는 ROP 직접 범위 아님으로 짧게 적고, f21·f32·f35·f41 의 감염 관리 기준·법 적용·인증 취득도 연계 대상으로 두어 ROP 몫은 요청·예약·상태 확인·경로·권한·속도 제약 반영으로만 서술했다. 절 첫 단락에도 이 경계를 밝혔다.",
    "근거 한계 — B. 로봇 온톨로지는 '아직 다루지 않은 연결'로, I. 설계·시뮬레이션(한 건)·L. AI·학습 기술(한 건)·K. 플랫폼 아키텍처·인프라(두 건)는 근거 건수와 빈 세부영역을 함께 적었다. f30 을 P. 거버넌스·법규·사회의 60. 노동·수용성·접근성에, f13 을 M. 안전의 49. 사람 근접 안전에 더했다.",
    "기존 연결 재사용 — f15·f30(C. 채팅 기반 구성·운영), f49(D. 공간·지도 모델), f50(E. 사물·사람·실시간 상태)은 같은 각주 id 를 재사용하고 '같은 연결은 … 페이지에도 있다'를 붙였다. f17·f19·f31 은 어느 대분류 페이지에 실렸는지 입력에 없어 표시하지 못했고 additional_research_requests 에 적었다.",
    "각주 정의 — 이 대분류 페이지에는 '참고 자료' 절이 없고 storyteller 부록 R-4 가 연결 절 끝에 각주 정의를 두도록 정하므로 '다른 대분류와의 연결' 절 끝에 62건을 두었다(새 절을 만들면 섹션 순서 검사에 걸린다). 형식은 지시대로 브리프 sources 의 기관·제목·발행일·URL, 접근일 2026-10-09, 뒤에 ' (원문 미열람)'이다. ref-257 은 'Interact Analysis (Rueben Scriven), …, 2023-01'로 적고 reference_updates 로 제목 갱신을 요청했다.",
    "기준일 — 모든 [사실] 문장에 발행·보도일을 남기고, f1·f11·f14·f25·f40 과 ref-937·ref-980 근거 문장은 '발행일 미확인, 확인일 2026-10-09'로 적었다. f50 은 본문에 날짜를 단정하지 않고 참고문헌 표기(2021-06)를 각주로 따랐다.",
    "열린 질문 — 첫 질문은 근거를 보강할 수 없어 그대로 두되 질문 끝에 oq-176·oq-182·oq-191 과의 차이를 밝혀 중복이 아님을 드러냈고, 둘째 질문(oq-038 과 대상 현장이 다름)은 그대로 등록했다."
  ]
}
```

### runs/2026-10-09-14/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/site-type-applications/index.md (1개 절)
```

### runs/2026-10-09-14/pages/categories/site-type-applications/index.md

```markdown
---
title: "Q. 현장 유형별 적용"
type: category
status: draft
created: 2026-09-28
updated: 2026-10-09
version: 2
---

[홈](../../index.md) › Q. 현장 유형별 적용

# Q. 현장 유형별 적용

## 핵심 질문

현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

## 개요

현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타)마다 다른 요구와 도입 사례를 모으는 곳. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **61. 물류창고** | 입고~반품 흐름의 로봇 작업. 기존 흐름 매트릭스와 영역 페이지의 물류 시나리오를 사례로 모은다 | 물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? | [61. 물류창고](warehouse.md) | published |
| **62. 제조 공장** | 라인 공급, 공정 간 운반, 여러 로봇이 함께 하는 공정 작업 | 여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가? | [62. 제조 공장](manufacturing-plant.md) | published |
| **63. 병원·의료** | 검체·약품·식사·린넨 이송, 감염 관리, 환자 정보 | 감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가? | [63. 병원·의료](hospital-and-healthcare.md) | published |
| **64. 상업 시설** | 호텔 객실 배송, 식당 서빙, 매장·쇼핑몰 안내·청소 | 손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가? | [64. 상업 시설](commercial-facilities.md) | published |
| **65. 가정·공동주택** | 집안일 보조, 공동주택 배송, 사생활 | 가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가? | [65. 가정·공동주택](home-and-apartment.md) | published |
| **66. 실외** | 실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 | 보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? | [66. 실외](outdoor.md) | published |
| **67. 기타 현장** | 점검·순찰(플랜트·데이터센터·빌딩), 건설, 농업, 공공시설, 오피스, 연구실 | 점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? | [67. 기타 현장](other-sites.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

물류창고는 여러 현장 유형 가운데 하나다. 현장마다 다른 요구는 여기에 모으고, **모든 현장에 공통인 기능은 A~P에 둔다**. [분류원문]

## 다른 대분류와의 연결

이 절은 [61. 물류창고](warehouse.md) ~ [67. 기타 현장](other-sites.md)에 게시된 현장 사례가 A~P 대분류의 어느 세부영역에 어떤 요구·입력·제약을 넘기는지 대분류별로 정리한다. 모든 현장에 공통인 기능 자체는 각 대분류 페이지에서 다루고, 이 절에는 현장 사례가 넘기는 요구와 근거만 적는다. 연결 대부분은 게시된 세부영역 페이지의 검증된 주장을 다시 인용한 것이며 단일 출처라 교차 확인되지 않았다. 승강기·설비 제어, 로봇 자체의 안전 기능·위치추정, 업종별 법·인증 판단은 분류 원문 19장의 경계에 따라 연계 대상으로 짧게 적고, ROP 몫은 요청·예약·상태 확인·제약 반영으로 한정한다.

- [A. 기획·사업](../planning-and-business/index.md) — 현장 사례는 1. 기술·시장·업체 동향, 2. 사용 사례·요구·책임 범위, 3. 경제성·조달·사업 모델에 시장 정의, 도입 형태, 도입 장애 요인을 넘긴다.
    - [61. 물류창고](warehouse.md) ↔ 1. 기술·시장·업체 동향: 쿠팡 대구 풀필먼트센터가 무인 운반차(Automated Guided Vehicle, AGV)·소팅봇·무인지게차를 층별로 나눠 투입했고(2023-02 보도) 시장 조사 기관이 다중 플릿 오케스트레이션 소프트웨어를 창고 제어 시스템(Warehouse Control System, WCS)의 전개에 비견한 것(2023-01)으로 보아, ROP 가 창고 관리 시스템(Warehouse Management System, WMS)과 WCS 사이에서 제조사가 다른 로봇에 작업을 배정하는 자리가 F. 연동의 20. 로봇·제조사 관제 연동과 함께 이 연결의 중심이 될 것으로 보이며, 근거는 회사 공개 행사 보도와 업계 보고서에 기댄 벤더 주장 수준이다. [추정][^ref-917][^ref-918][^ref-257]
    - [63. 병원·의료](hospital-and-healthcare.md) ↔ 3. 경제성·조달·사업 모델: 국내 병원 로봇 도입의 장애 요인으로 속도·안전성 부족, 대당 억 단위 비용, 경사 구간·문 호환·건물마다 다른 회사의 승강기가 보도되었다(2025-04-10 보도). [사실][^ref-948] 확인된 국내 지원 제도에는 과제 단위의 서비스로봇 실증사업 등이 있다(발행일 미확인, 확인일 2026-10-09). [추정][^ref-947]
    - Q. 현장 유형별 적용 전반 ↔ 2. 사용 사례·요구·책임 범위: 게시된 61. 물류창고 ~ 67. 기타 현장 페이지가 확인한 국내 사례는 대부분 한 운영사가 설비별로 로봇을 들이거나, 건설사·물류사 한 곳과 로봇 업체 한 곳이 짝을 이루거나, 한 기관이 만든 로봇을 자체 계층으로 묶은 형태다. [추정][^ref-917][^ref-966][^ref-997][^ref-1007] 이와 별도로 한림대성심병원은 여러 종류·제조사 로봇의 통합관제가 보도된 국내 사례이며, [63. 병원·의료](hospital-and-healthcare.md)는 이를 제조사가 다른 로봇 공존에 가장 가까운 공개 사례로 둔다(아래 F. 연동 항목). [추정][^ref-944] 그러나 제조사가 다른 로봇을 하나의 계층으로 묶으면서 그 인터페이스·표준까지 공개한 국내 사례는 확인되지 않았고, 이는 조사 범위의 한계이며 부재를 뜻하지 않는다(oq-163, oq-174, oq-183). [추정][^ref-944]
- [B. 로봇 온톨로지](../robot-ontology/index.md) — 아직 다루지 않은 연결이다. 이번 조사에서는 현장 사례가 4. 이기종 로봇 등록 ~ 7. 온톨로지 검증·변경 관리에 무엇을 넘기는지 보여 주는 근거를 찾지 못했다.
- [C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md) — 현장 사례 근거가 두 건뿐이다.
    - [62. 제조 공장](manufacturing-plant.md) ↔ 12. 채팅으로 업무 지시·오케스트레이션·[L. AI·학습 기술](../ai-and-learning/index.md)의 44. 로봇 기반 모델·언어 모델 계획: 국내 제조 현장에서 확인된 자료는 한국전자기술연구원(KETI)의 언어 모델·모방학습 조립공정 자동화 기술 공개(2025-03)와 자연어 지시가 언급되지 않은 정부 'AI 공장장' 사업(2026-09 보도)뿐이며, 이는 조사 범위의 한계이고 부재를 뜻하지 않는다(oq-142). [추정][^ref-932][^ref-931] 업무 지시 대화가 부르는 엔진은 G. 계획·최적화의 25. 작업 배정 — MRTA 와 26. 작업 순서·스케줄링이므로 이 연결은 아래 G. 계획·최적화 항목과 함께 읽는다. 같은 연결은 C. 채팅 기반 구성·운영 페이지에도 있다.
    - [64. 상업 시설](commercial-facilities.md) ↔ 13. 대화형 기능의 신뢰·기반·[P. 거버넌스·법규·사회](../governance-law-and-society/index.md)의 60. 노동·수용성·접근성: 네덜란드 슈퍼마켓 로봇 연구는 영어·네덜란드어와 성별 집단으로 음성 인식 기술을 비교해 Whisper 가 가장 낮은 단어 오류율을 보였다고 보고했다(2025-04-29 발행). [사실][^ref-868] 같은 연결은 C. 채팅 기반 구성·운영 페이지에도 있다.
- [D. 공간·지도 모델](../space-and-map-model/index.md) — 병원·건설·실외 사례가 도면 기반 지도, 장소 의미, 위치 모델에 요구를 넘긴다.
    - [63. 병원·의료](hospital-and-healthcare.md) ↔ 14. 도면·BIM에서 지도 만들기·[O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)의 55. 현장 조사·설치·시운전: 에스토니아 타르투 대학병원 현장 시험은 Open-RMF 교통 편집기로 평면도를 주석하고 로봇 격자 지도를 정합해 중환자실에서 검사실로 혈액 검체를 운반했으며, 작은 구역으로 나눠 매핑한 뒤 합치는 편이 더 정확했다(2022-08-23 발행). [사실][^ref-869] 같은 연결은 D. 공간·지도 모델 페이지에도 있다.
    - [67. 기타 현장](other-sites.md) ↔ 14. 도면·BIM에서 지도 만들기: GS건설은 4족 로봇 스팟이 모은 건설 현장 데이터를 기존 3차원 건물 정보 모델링(Building Information Modeling, BIM) 데이터와 통합해 전기·설비 공사 간섭 확인과 안전관리계획 수립에 썼다고 밝혔다(2020-07-13 보도). [사실][^ref-1000]
    - [66. 실외](outdoor.md) ↔ 16. 장소 의미·지도 관리·P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: 피츠버그 대학 캠퍼스에서 Starship 배송로봇이 연석 경사로를 막아 휠체어 이용자가 차도에 갇힌 뒤 대학이 시험 운행을 멈췄고, 회사는 해당 교차로의 지도 오류를 원인으로 들었다(2019-10-21 보도). [사실][^ref-987]
    - 연계 대상: [66. 실외](outdoor.md) ↔ 15. 지도·공간·위치 모델: Nav2 문서는 GPS 위치추정으로 실외에서 주행하는 방법을 튜토리얼로 제공하며(발행일 미확인, 확인일 2026-10-09), 위성 위치 기반 위치추정은 로봇 자체 지능·제어 쪽 기능이다. [사실][^ref-988]
- [E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md) — 현장 사례는 17. 작업 대상·자산 식별과 인계 추적에 완료·인계 확인 방식을, 19. 사람·보행자 모델에 사람 흐름과 상호작용 자료를 넘긴다.
    - [61. 물류창고](warehouse.md) ↔ 17. 작업 대상·자산 식별과 인계 추적: 쿠팡 대구 풀필먼트센터의 소팅봇은 포장 라벨의 운송장 바코드를 읽어 목적지별로 분류·이송한다(2023-02-07 보도). [사실][^ref-917] 이로 미루어 물류창고 출하 단계의 완료 확인은 작업 대상 식별에 기대는 것으로 보인다. [추정][^ref-917]
    - [63. 병원·의료](hospital-and-healthcare.md) ↔ 17. 작업 대상·자산 식별과 인계 추적: 중국 산시성 인민병원 연구에서 자율 이동 로봇(Autonomous Mobile Robot, AMR) 10대의 약품·검체 이송은 픽업·배송 지점의 무선 주파수 식별(Radio-Frequency Identification, RFID) 신원 확인으로 완료·인계를 확인했고, 약국·병동·시스템 관리자·장비 관리자의 역할을 정한 협력 책임 체계를 두었다(2026-04-24 발행). [사실][^ref-929]
    - [65. 가정·공동주택](home-and-apartment.md) ↔ 17. 작업 대상·자산 식별과 인계 추적: 래미안 리더스원 배송로봇의 수령 방식에 대해 삼성물산은 주문자만 음식을 꺼낼 수 있다고 설명하며(2026-01-15 발표, 벤더 주장), 인증 수단은 확인되지 않았다(oq-184). [추정][^ref-965]
    - [67. 기타 현장](other-sites.md) ↔ 17. 작업 대상·자산 식별과 인계 추적: 네이버 데이터센터 각 세종에서는 서버 관리 로봇과 운반 로봇이 협력해 서버 자산 흐름을 실시간으로 추적·관리한다고 보도되었다(2023-11-08 보도). [사실][^ref-1002]
    - [61. 물류창고](warehouse.md) ↔ 19. 사람·보행자 모델: EU ILIAD 프로젝트는 학습한 사람 흐름에 맞춰 물류창고 자율 지게차의 경로를 계획했다. [사실][^ref-1180] 같은 연결은 E. 사물·사람·실시간 상태 페이지에도 있다.
    - [66. 실외](outdoor.md) ↔ 19. 사람·보행자 모델·G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Gehrke 외(2023-03)는 대학 캠퍼스 녹화 영상으로 보도 자율 배송로봇과 보행자·자전거 이용자의 상호작용 빈도·심각도를 침범 후 시간(Post-Encroachment Time, PET)으로 쟀다. [사실][^ref-990]
- [F. 연동](../integration/index.md) — 이 절에서 현장 사례 근거가 가장 많이 모인 대분류다. 승강기 호출·운행 제어, 승강기 클라우드 API, 승강기 관리 솔루션은 시설·설비 제어 쪽 연계 대상이고, ROP 몫은 승강기 예약·상태 확인·혼잡 조건 반영이다.
    - 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성
        - [62. 제조 공장](manufacturing-plant.md): SYNAOS 는 폭스바겐 하노버 공장에서 MLR 언더라이드 로봇 약 100대와 자율 견인차 40대 등 135대 이상을 제조사 독립 플랫폼이 VDA 5050 으로 관제한다고 설명한다(2025-10-16, 벤더 주장). [추정][^ref-924]
        - [63. 병원·의료](hospital-and-healthcare.md): 싱가포르 창이종합병원 CHART 의 RoMi-H 는 기계·제어·중앙·통합 네 도메인으로 여러 제조사 로봇·센서·병원 정보 시스템을 잇는 미들웨어이다(발행일 미확인, 확인일 2026-10-09). [사실][^ref-937] Open Robotics 는 RoMi-H 를 ROS 2 기반 오픈소스로 소개하며, 서로 다른 벤더의 로봇이 승강기를 공유하고 출입 금지 구역으로 충돌을 피한다고 적었다(2021-02-10). [사실][^ref-942] 창이종합병원은 2025-05-01 부터 2년 유효한 등재 프로그램으로 시스템 통합사 5곳이 배치를 맡게 했다. [사실][^ref-872]
        - [63. 병원·의료](hospital-and-healthcare.md): 한림대성심병원은 2024-04 기준 7종 73대 서비스 로봇을 커맨드센터의 통합관제 시스템으로 관리하며, 통합관제의 인터페이스·표준은 확인되지 않았다(oq-174). [사실][^ref-944] LG전자가 이 병원에 배송로봇을 공급하고 빅웨이브로보틱스는 이 병원에서 로봇을 시험할 예정이었다(2024-07 기준). [사실][^ref-941]
        - [66. 실외](outdoor.md): 운행안전인증이 로봇과 관제장치의 조합을 대상으로 하므로(아래 P. 거버넌스·법규·사회 항목), 제조사가 다른 실외 로봇을 하나의 오케스트레이션 계층에서 지시할 때 그 계층이 인증상 관제장치에 해당하는지가 연동 설계의 쟁점이 될 것으로 보인다(oq-187). [추정][^ref-980]
        - [67. 기타 현장](other-sites.md): 농촌진흥청 통합 관리 프로그램은 자체 개발한 방제·운반·모니터링 로봇 3종을 하나의 화면으로 관리하며, 다른 제조사 로봇의 연결 여부는 보도에 없다(2025-04-23 보도, oq-192). [사실][^ref-1007] 싱가포르 창이 공항에서 로보틱스 미들웨어 프레임워크(Robotics Middleware Framework, RMF)가 쓰인다는 기사(2025-10-29)가 있으나 청소 로봇과의 연결은 명시되지 않아, 제조사가 다른 로봇을 한 계층에서 묶은 기타 현장의 공개 사례로 확인할 수준은 아닌 것으로 보인다. [추정][^ref-1004]
        - [65. 가정·공동주택](home-and-apartment.md): Matter 1.2 는 로봇청소기를 기기 유형으로 더해 원격 시작과 진행 알림, 브러시·오류·충전 상태 보고를 가전 연동 표준으로 다룬다(2023-10-23 발표). [사실][^ref-977]
        - [66. 실외](outdoor.md): 일본(2022년 공포 개정 도로교통법)과 미국 주별 개인 배송 장치(Personal Delivery Device, PDD) 법처럼 관할마다 보도 로봇의 크기·속도 기준이 다르고 신고 기준의 차이는 일본 출처에만 기대고 있어, ROP 가 관할 조건을 경로·속도 제약으로 바꿔 담는 공통 표현이 필요할 것으로 보인다(oq-190). [추정][^ref-985][^ref-986]
    - 22. 설비·건물 시스템 연동
        - [63. 병원·의료](hospital-and-healthcare.md): 고려대학교 구로병원 연구는 승강기 제어반에 단 전용 통신 모듈로 로봇의 승강기 호출·탑승을 자동화했고, 승강기 가동률 59% 미만 구간의 성공률이 95.52% 였으며 실패 건의 승강기 가동률 중앙값이 약 90%로 상위 구간에 몰렸다고 보고했다(2026-03-31 발행). [사실][^ref-943] 승강기 제어와 제어반 통신 모듈은 연계 대상이며, ROP 몫은 승강기 예약·상태 확인과 가동률 같은 혼잡 조건을 배정 제약으로 반영하는 데 있는 것으로 보인다. [추정][^ref-943]
        - [63. 병원·의료](hospital-and-healthcare.md)·[64. 상업 시설](commercial-facilities.md): 국가기술표준원은 2021-11-11 로봇의 엘리베이터 탑승 안전 요구사항 KS 제정을 발표했다. [사실][^ref-945] 표준 번호는 [F. 연동 페이지의 연결 절](../integration/index.md#다른-대분류와의-연결) 서술을 따른다.
        - [64. 상업 시설](commercial-facilities.md): 오티스는 자사 클라우드 API(Otis Integrated Dispatch)로 로봇이 승강기를 스스로 호출·탑승·층 선택하며, 오사카 호텔(2022-12 로봇 구독 계약)에서 24시간 객실 배송을 한다고 설명한다(벤더 주장, 발행일 미확인, 확인일 2026-10-09). [추정][^ref-957] 화성 동탄 상업시설 레이크 꼬모에서는 라이노스의 청소로봇 휠리 J40 이 클라우드 승강기 관리 솔루션 rEMS 로 전 층을 오간다고 보도되었다(2025-04-02 보도). [사실][^ref-963] 두 사례의 승강기 API·관리 솔루션은 설비 쪽 연계 대상이며, ROP 는 승강기 예약·상태 확인만 맡는 것으로 보인다. [추정][^ref-957][^ref-963]
        - [65. 가정·공동주택](home-and-apartment.md): 서울 래미안 리더스원에서는 공동현관 자동문 개폐와 엘리베이터 호출을 연동해 배송로봇이 세대 현관까지 간다(2026-09-20 보도 기준). [사실][^ref-965][^ref-979]
        - [67. 기타 현장](other-sites.md): 네이버 제2사옥 1784 의 배달 로봇 루키는 로봇 전용 엘리베이터 로보포트를 탄다(2023-01-11 보도). [사실][^ref-997]
    - 23. 업무 시스템 연동
        - [61. 물류창고](warehouse.md): 국내 스마트물류센터 인증 심사기준은 하차·입고를 입고예정정보 확인·하역작업·상품검수·제품정보 인식·등록으로, 상차·출고를 발주처별 분류·차량입차·상차순서관리·출고정보전달로 나눈다(발행일 미확인, 확인일 2026-10-09). [사실][^ref-919] 이로 미루어 물류창고 로봇 작업의 시작 조건과 완료 정보가 업무 시스템 단계에 묶여 있는 것으로 보인다. [추정][^ref-919]
        - [62. 제조 공장](manufacturing-plant.md): Wally 외(2019-11-13)는 ISA-95 모델과 계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)로 유연 생산 시스템의 운영 계획을 자동 생성하는 방법을 제안했다. [사실][^ref-925] 이 방법은 생산 관리 쪽 요청을 실행 계획으로 옮기는 연결의 연구 근거가 될 것으로 보인다. [추정][^ref-925] Siemens 는 자재 관리 시스템이 생산 계획과 칸반에 따라 운송 주문을 자동 생성해 AGV 플릿에 보낸다고 설명한다(벤더 주장, 발행일 미확인, 확인일 2026-10-09). [추정][^ref-926]
        - [64. 상업 시설](commercial-facilities.md): Sam's Club 은 약 600개 매장의 자율 바닥 청소기에 선반 스캔 부속을 달아, 로봇이 모은 가격 정확도·재고 수준·진열 위치 정보를 매장 관리자에게 전달하게 했다(2022-02-01 보도). [사실][^ref-952]
        - [65. 가정·공동주택](home-and-apartment.md): LH토지주택연구원 자료를 인용한 보도는 택배 차량이 단지 집하처에서 송장번호를 인식시키면 물품 정보가 관제실로 가고, 단지 로봇 택배를 단지 중앙집하·동 단위·구역 단위 분산집하의 세 시나리오로 나눈다고 전한다(2024-07-18 보도). [사실][^ref-976]
        - [67. 기타 현장](other-sites.md): 점검 로봇이 얻은 결과를 설비 보전 시스템으로 돌려주는 연결은 [열린 질문](../../open-questions.md) oq-194 로 남아 있다(점검 사례는 아래 J. 현장 운영·관제 항목).
- [G. 계획·최적화](../planning-and-optimization/index.md) — 현장 사례는 작업 모델, 배정·순서, 경로, 공용 자원(승강기) 혼잡을 계획 입력으로 넘긴다.
    - [62. 제조 공장](manufacturing-plant.md) ↔ 24. 작업·워크플로 모델링: Schmid·Limère(2019-02-23)는 조립라인 부품을 라인 적재·상자 공급·순서 공급·키팅 같은 공급 정책에 배정하는 조립라인 공급 문제를 분류했다. [사실][^ref-922] 이 분류는 제조 공장 라인 공급 작업을 나누는 기준이 될 것으로 보인다. [추정][^ref-922]
    - [61. 물류창고](warehouse.md) ↔ 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링: Schrotenboer 외(2019-09-01)는 반품 재적치를 고객 주문 피킹 경로에 통합하는 최적화를 다루었으나, 피커 기반 창고 연구이며 로봇 피킹 적용은 아니다(oq-165). [사실][^ref-912]
    - [64. 상업 시설](commercial-facilities.md) ↔ 26. 작업 순서·스케줄링·28. 공용 자원·충전·에너지 최적화: 다층 호텔 배치 자료(3개 층 67실) 실험에서 승강기 운행 시간이 40초에서 100초로 늘면 총 이동 시간이 거의 두 배가 되었고, 로봇이 5대를 넘으면 추가 로봇의 한계 이익이 크게 줄었다(2025-03-13 발행). [사실][^ref-103]
    - [63. 병원·의료](hospital-and-healthcare.md) ↔ 28. 공용 자원·충전·에너지 최적화: 구로병원 연구의 승강기 가동률 결과(위 F. 연동 항목)로 보아, 병원 승강기는 28. 공용 자원·충전·에너지 최적화가 다룰 공용 자원 혼잡 입력이 될 것으로 보인다. [추정][^ref-943]
    - [61. 물류창고](warehouse.md) ↔ 27. 다중 로봇 경로·교통 관리 — MAPF: 쿠팡 대구 풀필먼트센터의 AGV 는 바닥 QR 코드를 따라 움직인다(2023-02-07 보도). [사실][^ref-917] Li 외(2020)는 대규모 물류창고의 지속형 다중 에이전트 경로 찾기를, Ma 외(2017)는 온라인 픽업·배송 작업의 지속형 경로 찾기를 다루었다. [사실][^ref-005][^ref-006] 작업이 계속 들어오는 물류창고 운영은 경로 계획 연구의 대표 적용 대상인 것으로 보인다. [추정][^ref-005][^ref-006]
    - [66. 실외](outdoor.md) ↔ 27. 다중 로봇 경로·교통 관리 — MAPF: 보도 로봇과 보행자·자전거 이용자의 상호작용 연구는 위 E. 사물·사람·실시간 상태 항목에 있다.
- [H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md) — 현장 사례는 로봇이 끝내지 못한 일을 사람이 넘겨받는 방식과 예외 복구 분담을 31. 사람–로봇 협업과 32. 예외 복구·재계획·업무 연속성에 넘긴다.
    - [62. 제조 공장](manufacturing-plant.md) ↔ 31. 사람–로봇 협업: 유럽 전문가 31명 조사(2024-12-02)는 차량 조립 현장에서 협동로봇끼리, 그리고 외골격과의 충돌을 예측·회피하는 것을 핵심 안전·기술 과제로 꼽았다. [사실][^ref-928]
    - [64. 상업 시설](commercial-facilities.md) ↔ 31. 사람–로봇 협업·32. 예외 복구·재계획·업무 연속성: 일본 헨나 호텔에서는 객실 음성 비서·짐 운반·프런트 로봇이 기본 질문과 여권 복사 같은 업무를 해내지 못해 직원이 계속 넘겨받아야 했다(2019-01 보도). [사실][^ref-961][^ref-962] 쇼핑몰 안내 로봇 연구(2010-10)는 소음 속 음성 인식과 예상치 못한 지식 요구 때문에 일부 기능을 원격 조작자가 맡는 반자율 방식을 택했다. [사실][^ref-953]
    - [66. 실외](outdoor.md) ↔ 32. 예외 복구·재계획·업무 연속성·31. 사람–로봇 협업: Dobrosovestnova 외(RO-MAN 2022)는 눈 속에 갇힌 배송로봇을 행인이 도운 사례를 탐색적으로 연구했다. [사실][^ref-993]
    - 연계 대상: [61. 물류창고](warehouse.md) ↔ 32. 예외 복구·재계획·업무 연속성: DHL 의 트레일러 하역 로봇은 떨어진 상자의 자동 복구 개선이 향후 목표라고 보도되었을 뿐이며(2023-02-01, 회사 계획 진술에 기댄 벤더 주장), 상자 복구 동작은 로봇 자체 지능·제어 쪽 연계 대상이다. [추정][^ref-921] 로봇 자체 복구와 ROP 재계획의 분담은 공개 자료에서 확인되지 않아 두 영역의 경계 과제로 남는 것으로 보인다(oq-166). [추정][^ref-921]
- [I. 설계·시뮬레이션](../design-and-simulation/index.md) — 현장 사례 근거가 한 건뿐이다.
    - [62. 제조 공장](manufacturing-plant.md) ↔ 35. 처리능력·규모·배치 설계·34. 시뮬레이션·예측용 디지털 트윈: 국내 자동차 공장 연구는 시뮬레이션으로 AGV 대수·단일 차선 양방향 도로의 타당성을 따졌고(2014-04), 차체 버퍼 창고가 따로 운영될 때의 결품·막힘을 통합창고 모형으로 비교했다(2012). [사실][^ref-935][^ref-936] 두 연구는 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 쪽 사례이며, 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성과는 다르다. [추정][^ref-935][^ref-936]
    - 33. 시나리오 모델·편집과 36. 가상 시운전·실제 상황 재현에 대한 현장 사례는 아직 다루지 않은 연결이다(oq-134).
- [J. 현장 운영·관제](../field-operations-and-monitoring/index.md) — 현장 사례는 37. 관제 화면·실행 기록과 38. 모니터링·이상 탐지·원인 분석에 통합관제·관제실·점검 임무 운영 방식을 넘긴다.
    - [63. 병원·의료](hospital-and-healthcare.md) ↔ 37. 관제 화면·실행 기록: 한림대성심병원의 커맨드센터 통합관제는 위 F. 연동 항목에 있다.
    - [65. 가정·공동주택](home-and-apartment.md) ↔ 37. 관제 화면·실행 기록: 단지 로봇 택배의 관제실 구조는 위 F. 연동의 23. 업무 시스템 연동 항목에 있다.
    - [67. 기타 현장](other-sites.md) ↔ 38. 모니터링·이상 탐지·원인 분석: Equinor 의 Northern Lights 시설(장차 무인화 예정)에서는 4족 로봇이 계기 판독·밸브 위치 확인·누출 탐지를 하고, 현장 운영자가 연구개발 부서 도움 없이 점검 임무를 직접 만든다(2025-11-21 보도). [사실][^ref-995]
- [K. 플랫폼 아키텍처·인프라](../platform-architecture-and-infrastructure/index.md) — 현장 사례 근거가 두 건뿐이며 둘 다 42. 분산 시스템·통신·컴퓨팅 구조에 걸린다.
    - [63. 병원·의료](hospital-and-healthcare.md) ↔ 42. 분산 시스템·통신·컴퓨팅 구조: 분당서울대병원은 KT 5G 특화망 위의 AMR 6대가 다중 연동된 승강기·자동문을 거쳐 약 300m 연결 터널로 진료재료·약품·린넨 카트를 야간에 옮기게 했다(2023-07-06 보도). [사실][^ref-939]
    - [67. 기타 현장](other-sites.md) ↔ 42. 분산 시스템·통신·컴퓨팅 구조: 네이버 제2사옥 1784 의 배달 로봇 루키는 네이버 클라우드 기반 멀티 로봇 시스템 ARC 가 5G 특화망으로 제어한다(2023-01-11 보도). [사실][^ref-997] 이 구조는 네이버 자체 로봇·플랫폼의 사례이므로 ROP 직접 범위의 사례로 보지 않는다. [추정][^ref-997]
- [L. AI·학습 기술](../ai-and-learning/index.md) — 현장 사례 근거가 한 건뿐이다. 62. 제조 공장과 44. 로봇 기반 모델·언어 모델 계획의 연결은 위 C. 채팅 기반 구성·운영 항목에 있고, 45. 문서·도면·장면 이해, 46. 예측·학습 기반 최적화, 47. AI·학습·적응과 모델 운영에 대한 현장 사례는 아직 다루지 않은 연결이다.
- [M. 안전](../safety/index.md) — 여러 현장 유형에 걸쳐 적용되는 대분류다. 로봇·기계 쪽 안전 기능은 연계 대상이고, ROP 몫은 구역·시간·권한 규칙을 경로·배정 제약으로 반영하고 확인하는 것이다.
    - [63. 병원·의료](hospital-and-healthcare.md) ↔ 48. 안전·위험 관리: 병원에서 감염 관리 구역·야간 시간대·권한은 ROP 의 경로·배정 제약이 되고, 감염 관리 기준 설정과 이동형 영상정보처리기기 운영 제한 같은 법 판단은 병원 감염관리 조직·법령 쪽 연계 대상으로 남는 것으로 보인다(oq-171, oq-172). [추정][^ref-950][^ref-929][^ref-978]
    - [67. 기타 현장](other-sites.md) ↔ 48. 안전·위험 관리: ISO 18497-3:2024 는 부분 자동·반자율·자율 농업기계가 자율 운용 구역 경계를 벗어나지 않게 하는 기계 쪽 안전 요구를 다루며, 구역 자체의 정의는 이 표준의 범위 밖이다(2024 발행). [사실][^ref-1009] 경계 이탈 방지는 기계 쪽 연계 대상이고, 농업 현장 로봇의 운용 구역은 ROP 의 운행 제약 입력이 될 것으로 보인다. [추정][^ref-1009]
    - [61. 물류창고](warehouse.md) ↔ 49. 사람 근접 안전: 쿠팡 대구 풀필먼트센터는 무인지게차 구역에서 사람 이동을 막아 두며, 작업자가 구역을 침범하면 무인지게차가 멈춘다(2023-02-07 보도, 같은 공개 행사 기반). [사실][^ref-917][^ref-918] 정지 기능은 로봇 자체 안전 기능으로 연계 대상이며, ROP 몫은 구역 분리 규칙을 경로·배정에 반영하고 지켜지는지 확인하는 데 그치는 것으로 보인다. [추정][^ref-918]
    - [62. 제조 공장](manufacturing-plant.md) ↔ 49. 사람 근접 안전: 차량 조립 현장의 협동로봇·외골격 충돌 예측·회피 과제는 위 H. 실행·협업·예외 복구 항목에 있다.
    - [62. 제조 공장](manufacturing-plant.md) ↔ 50. 안전 표준·인증·사고 조사: 인증 기관 Applus+ 는 ISO 3691-4:2023 이 무인 산업 차량의 사람 감지·제동·속도 제어·운용 구역 분류를 다룬다고 안내하며, 표준 원문은 확인되지 않았다(벤더 주장, 발행일 미확인, 확인일 2026-10-09, oq-170). [추정][^ref-938]
    - [63. 병원·의료](hospital-and-healthcare.md)·[64. 상업 시설](commercial-facilities.md) ↔ 50. 안전 표준·인증·사고 조사: 로봇 엘리베이터 탑승 KS 는 위 F. 연동의 22. 설비·건물 시스템 연동 항목에 있다.
    - [66. 실외](outdoor.md) ↔ 50. 안전 표준·인증·사고 조사: 실외이동로봇 운행안전인증은 아래 P. 거버넌스·법규·사회 항목에 있다.
- [N. 보안·개인정보](../security-and-privacy/index.md) — 여러 현장 유형에 걸쳐 적용되며, 현장 사례는 주로 53. 개인정보·영상 데이터에 걸린다. 법 적용 판단은 운영자·법무 쪽 연계 대상이다.
    - [63. 병원·의료](hospital-and-healthcare.md) ↔ 53. 개인정보·영상 데이터: 병원 이송 로봇의 영상 촬영 법 적용은 위 M. 안전 항목의 감염 관리·법 판단 연결과 함께 oq-171 로 남아 있다.
    - [65. 가정·공동주택](home-and-apartment.md) ↔ 53. 개인정보·영상 데이터: 개인정보 보호법 제25조의2 는 이동형 영상정보처리기기의 운영을 제한하며(2023-03-14 게재 조문 기준), 개발용 Roomba 가 집 안에서 찍은 이미지가 라벨링 외주를 거쳐 외부에 게시된 사례가 보도되었다(2022-12-19 보도, 세대 안 적용 여부는 oq-181). [사실][^ref-978][^ref-968]
- [O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md) — 현장 사례 근거는 55. 현장 조사·설치·시운전 한 건이다. 타르투 대학병원의 평면도 주석·지도 정합 경험은 위 D. 공간·지도 모델 항목에 있고, 56. 운영 이관·확대·교육과 57. 자산·소프트웨어 수명주기 관리에 대한 현장 사례는 아직 다루지 않은 연결이다.
- [P. 거버넌스·법규·사회](../governance-law-and-society/index.md) — 여러 현장 유형에 걸쳐 적용되며, 실외 현장이 59. 법·규제·보험·라이선스에, 상업 시설·실외 현장이 60. 노동·수용성·접근성에 요구를 넘긴다.
    - [66. 실외](outdoor.md) ↔ 59. 법·규제·보험·라이선스·M. 안전의 50. 안전 표준·인증·사고 조사: 2023-11-17 시행된 개정 지능형로봇법·도로교통법으로 운행안전인증을 받은 실외이동로봇이 보행자 지위를 얻고 운영자의 보험 가입 의무가 생겼으며(2023-11-16 발표), 인증은 로봇과 관제장치의 조합에 주어진다(발행일 미확인, 확인일 2026-10-09). [사실][^ref-991][^ref-980] 인증 취득과 법 적용 판단은 운영자·인증 기관 쪽 연계 대상이고, ROP 는 해당 조건을 경로·속도·권한 제약으로 반영하는 쪽만 맡는 것으로 보인다. [추정][^ref-980]
    - [66. 실외](outdoor.md) ↔ 59. 법·규제·보험·라이선스: 관할별 보도 로봇 규정을 제약으로 담는 공통 표현 문제는 위 F. 연동의 21. 상호운용 표준·적합성 항목에 있다.
    - [64. 상업 시설](commercial-facilities.md)·[66. 실외](outdoor.md) ↔ 60. 노동·수용성·접근성: 슈퍼마켓 로봇의 언어·성별 집단별 음성 인식 비교는 위 C. 채팅 기반 구성·운영 항목에, 배송로봇이 연석 경사로를 막은 사례는 위 D. 공간·지도 모델 항목에 있다.

[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2020, https://arxiv.org/abs/2005.07371, 접근일 2026-10-09 (원문 미열람)
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-10-09 (원문 미열람)
[^ref-103]: Han, L., Ding, J., Liu, S., & Meng, M. (Sensors 25(6)), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-10-09 (원문 미열람)
[^ref-257]: Interact Analysis (Rueben Scriven), AMR Multi-Fleet Orchestration Software Explained, 2023-01, https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/, 접근일 2026-10-09 (원문 미열람)
[^ref-868]: Nandkumar, C., & Peternel, L. (Delft University of Technology), Frontiers in Robotics and AI, Enhancing supermarket robot interaction: an equitable multi-level LLM conversational interface for handling diverse customer intents, 2025-04-29, https://pmc.ncbi.nlm.nih.gov/articles/PMC12069059/, 접근일 2026-10-09 (원문 미열람)
[^ref-869]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-10-09 (원문 미열람)
[^ref-872]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-10-09 (원문 미열람)
[^ref-912]: Schrotenboer, A. H., Wruck, S., Vis, I. F. A., & Roodbergen, K. J., Integration of returns and decomposition of customer orders in e-commerce warehouses, 2019-09-01, https://arxiv.org/abs/1909.01794, 접근일 2026-10-09 (원문 미열람)
[^ref-917]: 로봇신문 (장길수), 쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이..., 2023-02-07, https://www.irobotnews.com/news/articleView.html?idxno=30736, 접근일 2026-10-09 (원문 미열람)
[^ref-918]: 물류신문 (석한글), ‘물류 투자만 6조’, 쿠팡 물류 인프라의 정점 ‘대구 FC’ 가보니, 2023-02-07, https://www.klnews.co.kr/news/articleView.html?idxno=306994, 접근일 2026-10-09 (원문 미열람)
[^ref-919]: 스마트물류시설인증센터 (한국교통연구원), 인증스마트물류센터 : 인증심사 > 심사기준 > 일반, 미확인, https://cslc.koti.re.kr/new_sub2/new_sub2_2_1, 접근일 2026-10-09 (원문 미열람)
[^ref-921]: Robotics 24/7 (Eugene Demaitre), DHL Makes First Commercial Deployment of Boston Dynamics Stretch Robot to Unload Trailers and Containers, 2023-02-01, https://www.robotics247.com/article/dhl_makes_first_commercial_deployment_boston_dynamics_stretch_robot_unload_trailers_containers, 접근일 2026-10-09 (원문 미열람)
[^ref-922]: Schmid, N. A., & Limère, V. (International Journal of Production Research 57(24)), A classification of tactical assembly line feeding problems, 2019-02-23, https://www.tandfonline.com/doi/full/10.1080/00207543.2019.1581957, 접근일 2026-10-09 (원문 미열람)
[^ref-924]: SYNAOS (IoT Use Case), VDA 5050: unified AGV fleet control in real time at VW, 2025-10-16, https://www.iotusecase.com/en/solution-examples/vda-5050-agv-fleet-control, 접근일 2026-10-09 (원문 미열람)
[^ref-925]: Wally, B., Vyskočil, J., Novák, P., Huemer, C., Šindelář, R., Kadera, P., Mazak, A., & Wimmer, M., Flexible Production Systems: Automated Generation of Operations Plans Based on ISA-95 and PDDL, 2019-11-13, https://arxiv.org/abs/1911.05481, 접근일 2026-10-09 (원문 미열람)
[^ref-926]: Siemens, AGV fleet management integration with intralogistics, 미확인, https://resources.sw.siemens.com/en-US/white-paper-integrating-agv-automated-guided-vehicle-system-with-intralogistics/, 접근일 2026-10-09 (원문 미열람)
[^ref-928]: Pietrantoni, L., Favilla, M., Fraboni, F., Mazzoni, E., Morandini, S., Benvenuti, M., & De Angelis, M. (Frontiers in Robotics and AI), Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors, 2024-12-02, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1342130/full, 접근일 2026-10-09 (원문 미열람)
[^ref-929]: Li, M. 외 (Scientific Reports), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04-24, https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/, 접근일 2026-10-09 (원문 미열람)
[^ref-931]: 뉴시스, "로봇 몇 대, 어디로 움직일까"…중소 제조현장에 'AI 공장장' 뜬다, 2026-09-07, https://www.newsis.com/view/NISX20260907_0003779780, 접근일 2026-10-09 (원문 미열람)
[^ref-932]: 테크데일리, KETI, LLM 모델 및 모방학습, 조립공정 자동화 기술 공개, 2025-03-12, https://www.techdaily.co.kr/news/articleView.html?idxno=25352, 접근일 2026-10-09 (원문 미열람)
[^ref-935]: 강명훈, 곽춘종 (부산대학교; Asia-Pacific Journal of Business & Commerce), 시뮬레이션을 이용한 자동차 부품 공급 시스템 도입 방안 분석: R자동차 사례, 2014-04, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE02448280, 접근일 2026-10-09 (원문 미열람)
[^ref-936]: 옥창훈, 김득수, 공정수, 서윤호 (고려대학교, 현대자동차; 한국시뮬레이션학회 논문지 21(2)), 자동차 생산을 위한 통합창고 연구, 2012, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001671601, 접근일 2026-10-09 (원문 미열람)
[^ref-937]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), ROMI-H | Changi General Hospital, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-10-09 (원문 미열람)
[^ref-938]: Applus+ Laboratories, ISO 3691-4:2023: Compliance Testing for Automated Guided Vehicles (AGVs), 미확인, https://www.appluslaboratories.com/global/en/what-we-do/service-sheet/iso-3691-4-2023-compliance-testing-for-automated-guided-vehicles-agvs, 접근일 2026-10-09 (원문 미열람)
[^ref-939]: 이데일리, 분당서울대병원, 무거운 이송카트 로봇자율배송, 무안경 3D 의료실습에 도입, 2023-07-06, https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01403846635671896, 접근일 2026-10-09 (원문 미열람)
[^ref-941]: 데일리팜, 원내 약 배송로봇 도입 확대...정부 지원에 변화 바람, 2024-07-15, https://m.dailypharm.com/user/news/15128, 접근일 2026-10-09 (원문 미열람)
[^ref-942]: Open Robotics, ROMI-H: Bringing Robot Traffic Control to Healthcare, 2021-02-10, https://www.openrobotics.org/blog/2021/2/10/romi-h-bringing-robot-traffic-control-to-healthcare, 접근일 2026-10-09 (원문 미열람)
[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-09 (원문 미열람)
[^ref-944]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원', 2024-04-15, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-10-09 (원문 미열람)
[^ref-945]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-10-09 (원문 미열람)
[^ref-947]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-10-09 (원문 미열람)
[^ref-948]: 비즈한국, 병원에 늘어나는 '로봇', 의사·간호사도 편해졌을까, 2025-04-10, https://bizhankook.com/articles/29394.html, 접근일 2026-10-09 (원문 미열람)
[^ref-950]: 한국보건산업진흥원 스마트병원 확산지원센터, 선도모델 및 모듈 소개, 미확인, https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040, 접근일 2026-10-09 (원문 미열람)
[^ref-952]: Retail Dive (Sam Silverstein), Sam's Club rolls out inventory-checking robots chainwide, 2022-02-01, https://www.retaildive.com/news/sams-club-rolls-out-inventory-checking-robots-chainwide/618040/, 접근일 2026-10-09 (원문 미열람)
[^ref-953]: Kanda, T., Shiomi, M., Miyashita, Z., Ishiguro, H., & Hagita, N. (IEEE Transactions on Robotics 26(5)), A Communication Robot in a Shopping Mall, 2010-10, https://ieeexplore.ieee.org/abstract/document/5557825, 접근일 2026-10-09 (원문 미열람)
[^ref-957]: Otis Elevator Company, Elevators and service robots, 미확인, https://www.otis.com/en/us/innovation/elevators-and-service-robots, 접근일 2026-10-09 (원문 미열람)
[^ref-961]: Responsible AI Collaborative (AI Incident Database), Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks, 미확인, https://incidentdatabase.ai/cite/346/, 접근일 2026-10-09 (원문 미열람)
[^ref-962]: Hotel Technology News, Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce, 2019-01, https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/, 접근일 2026-10-09 (원문 미열람)
[^ref-963]: 서울경제 (백주연), 엘리베이터 타고 쇼핑몰 왔다갔다…바닥 물걸레질까지 하는 '로봇 청소부' 등장, 2025-04-02, https://www.sedaily.com/article/14048085, 접근일 2026-10-09 (원문 미열람)
[^ref-965]: 삼성물산 뉴스룸, 삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영, 2026-01-15, https://news.samsungcnt.com/ko/%EC%A0%84%EC%B2%B4%EA%B8%B0%EC%82%AC/%EA%B1%B4%EC%84%A4%EB%B6%80%EB%AC%B8/2026-01-%EC%82%BC%EC%84%B1%EB%AC%BC%EC%82%B0-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%84%B8%EB%8C%80-%ED%98%84%EA%B4%80%EA%B9%8C%EC%A7%80-%EC%9D%8C%EC%8B%9D%EB%B0%B0%EB%8B%AC%EB%A1%9C%EB%B4%87-%ED%99%95%EC%9E%A5/, 접근일 2026-10-09 (원문 미열람)
[^ref-966]: 지디넷코리아 (신영빈), 로봇이 문앞까지 택배 가져다 주는 미래 곧 온다, 2025-01-19, https://zdnet.co.kr/view/?no=20250119062609, 접근일 2026-10-09 (원문 미열람)
[^ref-968]: MIT Technology Review (Eileen Guo), A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?, 2022-12-19, https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/, 접근일 2026-10-09 (원문 미열람)
[^ref-976]: 정보통신신문 (김연균), 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’, 2024-07-18, https://www.koit.co.kr/news/articleView.html?idxno=123976, 접근일 2026-10-09 (원문 미열람)
[^ref-977]: Connectivity Standards Alliance (CSA), Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board, 2023-10-23, https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/, 접근일 2026-10-09 (원문 미열람)
[^ref-978]: CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관), 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한), 2023-03-14, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4_%EB%B3%B4%ED%98%B8%EB%B2%95/%EC%A0%9C25%EC%A1%B0%EC%9D%982, 접근일 2026-10-09 (원문 미열람)
[^ref-979]: 미디어펜 (조태민), 로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도, 2026-09-20, https://www.mediapen.com/news/view/1124680, 접근일 2026-10-09 (원문 미열람)
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-10-09 (원문 미열람)
[^ref-985]: 内閣府 (일본 내각부), 令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について, 2023, https://www8.cao.go.jp/koutu//taisaku/r05kou_haku/zenbun/genkyo/topics/topic_1.html, 접근일 2026-10-09 (원문 미열람)
[^ref-986]: Supply Chain Dive, Why delivery robots face a regulatory ‘nightmare’, 2023-04-26, https://www.supplychaindive.com/news/delivery-robot-bills-laws-proliferate-state-legislatures/648303/, 접근일 2026-10-09 (원문 미열람)
[^ref-987]: The Pitt News, Pitt pauses testing of Starship robots due to safety concerns, 2019-10-21, https://pittnews.com/article/151679/news/pitt-pauses-testing-of-starship-robots-due-to-safety-concerns/, 접근일 2026-10-09 (원문 미열람)
[^ref-988]: Open Navigation (Nav2), Navigating Using GPS Localization — Nav2 documentation, 미확인, https://docs.nav2.org/jazzy/tutorials/general_tutorials/navigation2_with_gps/navigation2_with_gps/, 접근일 2026-10-09 (원문 미열람)
[^ref-990]: Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18), Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists, 2023-03, https://doi.org/10.1016/j.trip.2023.100789, 접근일 2026-10-09 (원문 미열람)
[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-10-09 (원문 미열람)
[^ref-993]: Dobrosovestnova, A., Schwaninger, I., & Weiss, A. (IEEE RO-MAN 2022), With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow, 2022, https://ieeexplore.ieee.org/abstract/document/9900588/, 접근일 2026-10-09 (원문 미열람)
[^ref-995]: Offshore Technology (Eve Thomas), Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones, 2025-11-21, https://www.offshore-technology.com/features/equinor-autonomous-robotics/, 접근일 2026-10-09 (원문 미열람)
[^ref-997]: 이코노미스트 (송재민), 로봇이 로봇들을 움직이는, 네이버 1784, 2023-01-11, https://economist.co.kr/article/view/ecn202301110006, 접근일 2026-10-09 (원문 미열람)
[^ref-1000]: 인더스트리뉴스 (정형우), GS건설, 4족보행 로봇 '스팟(SPOT)' 국내 최초 건설현장 도입하기로, 2020-07-13, https://www.industrynews.co.kr/news/articleView.html?idxno=38911, 접근일 2026-10-09 (원문 미열람)
[^ref-1002]: 아주경제 (윤선훈), 아시아 최대 규모 데이터센터…네이버 '각 세종' 본격 가동, 2023-11-08, https://www.ajunews.com/view/20231107091520837, 접근일 2026-10-09 (원문 미열람)
[^ref-1004]: The Robot Report, Singapore's National Robotics Programme reveals initiatives to advance robot adoption, 2025-10-29, https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/, 접근일 2026-10-09 (원문 미열람)
[^ref-1007]: 뉴스토마토 (이규하), 방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동, 2025-04-23, https://www.newstomato.com/ReadNews.aspx?no=1259970, 접근일 2026-10-09 (원문 미열람)
[^ref-1009]: ISO, ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones, 2024, https://www.iso.org/standard/82687.html, 접근일 2026-10-09 (원문 미열람)
[^ref-1180]: ILIAD 프로젝트 컨소시엄 (EU Horizon 2020), Concluding ILIAD, 2021-06, https://iliad-project.eu/concluding-iliad/, 접근일 2026-10-09 (원문 미열람)

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 110건이다(논문 30건 · 기사·보고서 48건 · 업체 발표 10건 · 표준·오픈소스·기관 자료 22건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-972](../../references/ref-972.md) — Hwang, I. T., Kim, G. T., & Kwag, B. C. (한국생활환경학회지 30), Comparing Perceptions of Service Robot Adoption in Multi-Family Housing Between Residents and Industry Stakeholders: Focusing on Acceptance Attitudes, Concerns, and Technological Needs (발행 2026-06)
- [ref-929](../../references/ref-929.md) — Li, M. 외 (Scientific Reports), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios (발행 2026-04-24)
- [ref-964](../../references/ref-964.md) — Karlsen, A. S. T., Andersen, B., Nevstad, K., Heirsaunet, S. E., Indergård, E., & Aarseth, W. (Frontiers in Robotics and AI), Digital transformation in restaurants: key aspects of service robot deployment from project initiation to evaluation (발행 2026-04-22)
- [ref-943](../../references/ref-943.md) — Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026-03-31)
- [ref-982](../../references/ref-982.md) — Tong, X., & Simoni, M. D. (arXiv), Robust Route Planning for Sidewalk Delivery Robots (발행 2025-07-16)
- [ref-928](../../references/ref-928.md) — Pietrantoni, L., Favilla, M., Fraboni, F., Mazzoni, E., Morandini, S., Benvenuti, M., & De Angelis, M. (Frontiers in Robotics and AI), Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors (발행 2024-12-02)
- [ref-946](../../references/ref-946.md) — Babalola, G. T., Gaston, J.-M., Trombetta, J., & Tulk Jesso, S. (Frontiers in Robotics and AI), A systematic review of collaborative robots for nurses: where are we now, and where is the evidence? (발행 2024-06-05)
- [ref-971](../../references/ref-971.md) — Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation (발행 2024-03-14)
- [ref-933](../../references/ref-933.md) — Keshvarparast, A., Battini, D., Battaia, O., & Pirayesh, A. (Journal of Intelligent Manufacturing 35), Collaborative robots in manufacturing and assembly systems: literature review and future research agenda (발행 2023-05-30)
- [ref-990](../../references/ref-990.md) — Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18), Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists (발행 2023-03)
- 그 밖에 20건

**기사·보고서**

- [ref-975](../../references/ref-975.md) — 한국경제 (김익환), 배송·주차·청소까지…로봇 아파트 뜬다 (발행 2026-09-27)
- [ref-979](../../references/ref-979.md) — 미디어펜 (조태민), 로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도 (발행 2026-09-20)
- [ref-931](../../references/ref-931.md) — 뉴시스, "로봇 몇 대, 어디로 움직일까"…중소 제조현장에 'AI 공장장' 뜬다 (발행 2026-09-07)
- [ref-984](../../references/ref-984.md) — 스포츠경향, 뉴빌리티, 덕수궁 순찰부터 도쿄 시내 배달까지 (발행 2026-09-02)
- [ref-981](../../references/ref-981.md) — DC Velocity, Starship steers its delivery robots off college campuses and toward grocery sector (발행 2026-06-08)
- [ref-995](../../references/ref-995.md) — Offshore Technology (Eve Thomas), Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones (발행 2025-11-21)
- [ref-969](../../references/ref-969.md) — 바이라인네트워크, '로봇청소기' 다수 제품 보안 취약…대응방안은? (발행 2025-10-31)
- [ref-973](../../references/ref-973.md) — The Robot Report (Mike Oitzman), NEO humanoid designed for household use, available for preorder (발행 2025-10-30)
- [ref-1004](../../references/ref-1004.md) — The Robot Report, Singapore's National Robotics Programme reveals initiatives to advance robot adoption (발행 2025-10-29)
- [ref-970](../../references/ref-970.md) — 매일신문, 사생활 훔치는 로봇청소기…중국산 제품서 `무단 촬영` 가능성 확인 (발행 2025-10-06)
- 그 밖에 38건

**업체 발표**

- [ref-965](../../references/ref-965.md) — 삼성물산 뉴스룸, 삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영 (발행 2026-01-15)
- [ref-974](../../references/ref-974.md) — LG Electronics USA, LG ELECTRONICS PRESENTS LG CLOiD HOME ROBOT TO DEMONSTRATE "ZERO LABOR HOME" AT CES 2026 (발행 2026-01-06)
- [ref-924](../../references/ref-924.md) — SYNAOS (IoT Use Case), VDA 5050: unified AGV fleet control in real time at VW (발행 2025-10-16)
- [ref-916](../../references/ref-916.md) — Amazon, Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot (발행 2025-07)
- [ref-930](../../references/ref-930.md) — 현대자동차그룹, ‘혁신의 장場’ HMGICS, 인간 중심 모빌리티 솔루션의 새 시대 열다 (발행 2023-11-21)
- [ref-920](../../references/ref-920.md) — CJ대한통운, CJ대한통운 안성 MP허브, 국토부 ‘스마트물류센터 1등급’ 인증 (발행 2023-10-26)
- [ref-1003](../../references/ref-1003.md) — Korial (구 Energy Robotics) — Andre Retterath, Earlybird Venture Capital 기고, Game-changer: The rationale behind the investment in Energy Robotics (발행 2021-01-15)
- [ref-957](../../references/ref-957.md) — Otis Elevator Company, Elevators and service robots (발행 미확인)
- [ref-938](../../references/ref-938.md) — Applus+ Laboratories, ISO 3691-4:2023: Compliance Testing for Automated Guided Vehicles (AGVs) (발행 미확인)
- [ref-926](../../references/ref-926.md) — Siemens, AGV fleet management integration with intralogistics (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-872](../../references/ref-872.md) — Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025 (발행 2025-05-01)
- [ref-994](../../references/ref-994.md) — ISO, ISO/TR 4448-1:2024 Intelligent transport systems — Public-area mobile robots (PMR) — Part 1: Overview of paradigm (발행 2024-08)
- [ref-959](../../references/ref-959.md) — 한국노동연구원 (박수민 외), 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향 (발행 2024)
- [ref-1009](../../references/ref-1009.md) — ISO, ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones (발행 2024)
- [ref-991](../../references/ref-991.md) — 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 (발행 2023-11-16)
- [ref-977](../../references/ref-977.md) — Connectivity Standards Alliance (CSA), Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board (발행 2023-10-23)
- [ref-978](../../references/ref-978.md) — CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관), 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) (발행 2023-03-14)
- [ref-985](../../references/ref-985.md) — 内閣府 (일본 내각부), 令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について (발행 2023)
- [ref-945](../../references/ref-945.md) — 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 (발행 2021-11-11)
- [ref-942](../../references/ref-942.md) — Open Robotics, ROMI-H: Bringing Robot Traffic Control to Healthcare (발행 2021-02-10)
- 그 밖에 12건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [67. 기타 현장](other-sites.md) — 섹션 3~11 신규 작성(seed → draft): 현장 유형 기타 사례 4건(Equinor CCS 시설 점검, 건설 현장 점검, 농업 로봇 통합 관리·운반, 네이버 1784 사내 배달)을 여섯 항목으로 정리, 접근법 6가지, 표준 5건, 책임 경계, 연결 영역 17개, 열린 질문 5건. 2차 수정: 출처 5건 제목 정정, 9절 태그 추가, BIM·라이다·RMF 첫 등장 풀어 쓰기. 2차 재검증 수정: 9절 RMF 풀이를 Robotics Middleware Framework 로 정정 (실행 2026-09-30-02)
- 2026-09-30 · 생성 · [67. 기타 현장 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area67-s6.md) — 자동 분리: 67. 기타 현장 의 "6. 대표 접근법과 기술" 절(1,209자)을 옮겼다. 2차 수정: 출처 제목 정정(ref-995·1000·1002·1006·1007) (실행 2026-09-30-02)
- 2026-09-30 · 생성 · [67. 기타 현장 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area67-s7.md) — 자동 분리: 67. 기타 현장 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,102자)을 옮겼다. ref-004 각주 줄은 참고문헌 페이지가 입력에 없어 이전 값을 유지했다(퍼블리셔 대조 요청) (실행 2026-09-30-02)
- 2026-09-30 · 생성 · [67. 기타 현장 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area67-s10.md) — 자동 분리: 67. 기타 현장 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,022자)을 옮겼다. 2차 수정: 20. 로봇·제조사 관제 연동 항목의 창이 공항 서술을 기사 수준으로 고치고 출처 제목 정정 (실행 2026-09-30-02)
- 2026-09-30 · 생성 · [67. 기타 현장 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area67-s4.md) — 자동 분리: 67. 기타 현장 의 "4. 핵심 개념과 용어" 절(903자)을 옮겼다. 2차 수정: ref-1000 제목 정정. ref-004 각주 줄은 참고문헌 페이지가 입력에 없어 이전 값을 유지했다(퍼블리셔 대조 요청) (실행 2026-09-30-02)
<!-- auto:category-recent:end -->
```

### docs/categories/site-type-applications/index.md

```markdown
---
title: "Q. 현장 유형별 적용"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › Q. 현장 유형별 적용

# Q. 현장 유형별 적용

## 핵심 질문

현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

## 개요

현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타)마다 다른 요구와 도입 사례를 모으는 곳. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **61. 물류창고** | 입고~반품 흐름의 로봇 작업. 기존 흐름 매트릭스와 영역 페이지의 물류 시나리오를 사례로 모은다 | 물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? | [61. 물류창고](warehouse.md) | published |
| **62. 제조 공장** | 라인 공급, 공정 간 운반, 여러 로봇이 함께 하는 공정 작업 | 여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가? | [62. 제조 공장](manufacturing-plant.md) | published |
| **63. 병원·의료** | 검체·약품·식사·린넨 이송, 감염 관리, 환자 정보 | 감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가? | [63. 병원·의료](hospital-and-healthcare.md) | published |
| **64. 상업 시설** | 호텔 객실 배송, 식당 서빙, 매장·쇼핑몰 안내·청소 | 손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가? | [64. 상업 시설](commercial-facilities.md) | published |
| **65. 가정·공동주택** | 집안일 보조, 공동주택 배송, 사생활 | 가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가? | [65. 가정·공동주택](home-and-apartment.md) | published |
| **66. 실외** | 실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 | 보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? | [66. 실외](outdoor.md) | published |
| **67. 기타 현장** | 점검·순찰(플랜트·데이터센터·빌딩), 건설, 농업, 공공시설, 오피스, 연구실 | 점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? | [67. 기타 현장](other-sites.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

물류창고는 여러 현장 유형 가운데 하나다. 현장마다 다른 요구는 여기에 모으고, **모든 현장에 공통인 기능은 A~P에 둔다**. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 110건이다(논문 30건 · 기사·보고서 48건 · 업체 발표 10건 · 표준·오픈소스·기관 자료 22건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-972](../../references/ref-972.md) — Hwang, I. T., Kim, G. T., & Kwag, B. C. (한국생활환경학회지 30), Comparing Perceptions of Service Robot Adoption in Multi-Family Housing Between Residents and Industry Stakeholders: Focusing on Acceptance Attitudes, Concerns, and Technological Needs (발행 2026-06)
- [ref-929](../../references/ref-929.md) — Li, M. 외 (Scientific Reports), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios (발행 2026-04-24)
- [ref-964](../../references/ref-964.md) — Karlsen, A. S. T., Andersen, B., Nevstad, K., Heirsaunet, S. E., Indergård, E., & Aarseth, W. (Frontiers in Robotics and AI), Digital transformation in restaurants: key aspects of service robot deployment from project initiation to evaluation (발행 2026-04-22)
- [ref-943](../../references/ref-943.md) — Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026-03-31)
- [ref-982](../../references/ref-982.md) — Tong, X., & Simoni, M. D. (arXiv), Robust Route Planning for Sidewalk Delivery Robots (발행 2025-07-16)
- [ref-928](../../references/ref-928.md) — Pietrantoni, L., Favilla, M., Fraboni, F., Mazzoni, E., Morandini, S., Benvenuti, M., & De Angelis, M. (Frontiers in Robotics and AI), Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors (발행 2024-12-02)
- [ref-946](../../references/ref-946.md) — Babalola, G. T., Gaston, J.-M., Trombetta, J., & Tulk Jesso, S. (Frontiers in Robotics and AI), A systematic review of collaborative robots for nurses: where are we now, and where is the evidence? (발행 2024-06-05)
- [ref-971](../../references/ref-971.md) — Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation (발행 2024-03-14)
- [ref-933](../../references/ref-933.md) — Keshvarparast, A., Battini, D., Battaia, O., & Pirayesh, A. (Journal of Intelligent Manufacturing 35), Collaborative robots in manufacturing and assembly systems: literature review and future research agenda (발행 2023-05-30)
- [ref-990](../../references/ref-990.md) — Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18), Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists (발행 2023-03)
- 그 밖에 20건

**기사·보고서**

- [ref-975](../../references/ref-975.md) — 한국경제 (김익환), 배송·주차·청소까지…로봇 아파트 뜬다 (발행 2026-09-27)
- [ref-979](../../references/ref-979.md) — 미디어펜 (조태민), 로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도 (발행 2026-09-20)
- [ref-931](../../references/ref-931.md) — 뉴시스, "로봇 몇 대, 어디로 움직일까"…중소 제조현장에 'AI 공장장' 뜬다 (발행 2026-09-07)
- [ref-984](../../references/ref-984.md) — 스포츠경향, 뉴빌리티, 덕수궁 순찰부터 도쿄 시내 배달까지 (발행 2026-09-02)
- [ref-981](../../references/ref-981.md) — DC Velocity, Starship steers its delivery robots off college campuses and toward grocery sector (발행 2026-06-08)
- [ref-995](../../references/ref-995.md) — Offshore Technology (Eve Thomas), Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones (발행 2025-11-21)
- [ref-969](../../references/ref-969.md) — 바이라인네트워크, '로봇청소기' 다수 제품 보안 취약…대응방안은? (발행 2025-10-31)
- [ref-973](../../references/ref-973.md) — The Robot Report (Mike Oitzman), NEO humanoid designed for household use, available for preorder (발행 2025-10-30)
- [ref-1004](../../references/ref-1004.md) — The Robot Report, Singapore's National Robotics Programme reveals initiatives to advance robot adoption (발행 2025-10-29)
- [ref-970](../../references/ref-970.md) — 매일신문, 사생활 훔치는 로봇청소기…중국산 제품서 `무단 촬영` 가능성 확인 (발행 2025-10-06)
- 그 밖에 38건

**업체 발표**

- [ref-965](../../references/ref-965.md) — 삼성물산 뉴스룸, 삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영 (발행 2026-01-15)
- [ref-974](../../references/ref-974.md) — LG Electronics USA, LG ELECTRONICS PRESENTS LG CLOiD HOME ROBOT TO DEMONSTRATE "ZERO LABOR HOME" AT CES 2026 (발행 2026-01-06)
- [ref-924](../../references/ref-924.md) — SYNAOS (IoT Use Case), VDA 5050: unified AGV fleet control in real time at VW (발행 2025-10-16)
- [ref-916](../../references/ref-916.md) — Amazon, Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot (발행 2025-07)
- [ref-930](../../references/ref-930.md) — 현대자동차그룹, ‘혁신의 장場’ HMGICS, 인간 중심 모빌리티 솔루션의 새 시대 열다 (발행 2023-11-21)
- [ref-920](../../references/ref-920.md) — CJ대한통운, CJ대한통운 안성 MP허브, 국토부 ‘스마트물류센터 1등급’ 인증 (발행 2023-10-26)
- [ref-1003](../../references/ref-1003.md) — Korial (구 Energy Robotics) — Andre Retterath, Earlybird Venture Capital 기고, Game-changer: The rationale behind the investment in Energy Robotics (발행 2021-01-15)
- [ref-957](../../references/ref-957.md) — Otis Elevator Company, Elevators and service robots (발행 미확인)
- [ref-938](../../references/ref-938.md) — Applus+ Laboratories, ISO 3691-4:2023: Compliance Testing for Automated Guided Vehicles (AGVs) (발행 미확인)
- [ref-926](../../references/ref-926.md) — Siemens, AGV fleet management integration with intralogistics (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-872](../../references/ref-872.md) — Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025 (발행 2025-05-01)
- [ref-994](../../references/ref-994.md) — ISO, ISO/TR 4448-1:2024 Intelligent transport systems — Public-area mobile robots (PMR) — Part 1: Overview of paradigm (발행 2024-08)
- [ref-959](../../references/ref-959.md) — 한국노동연구원 (박수민 외), 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향 (발행 2024)
- [ref-1009](../../references/ref-1009.md) — ISO, ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones (발행 2024)
- [ref-991](../../references/ref-991.md) — 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 (발행 2023-11-16)
- [ref-977](../../references/ref-977.md) — Connectivity Standards Alliance (CSA), Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board (발행 2023-10-23)
- [ref-978](../../references/ref-978.md) — CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관), 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) (발행 2023-03-14)
- [ref-985](../../references/ref-985.md) — 内閣府 (일본 내각부), 令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について (발행 2023)
- [ref-945](../../references/ref-945.md) — 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 (발행 2021-11-11)
- [ref-942](../../references/ref-942.md) — Open Robotics, ROMI-H: Bringing Robot Traffic Control to Healthcare (발행 2021-02-10)
- 그 밖에 12건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [67. 기타 현장](other-sites.md) — 섹션 3~11 신규 작성(seed → draft): 현장 유형 기타 사례 4건(Equinor CCS 시설 점검, 건설 현장 점검, 농업 로봇 통합 관리·운반, 네이버 1784 사내 배달)을 여섯 항목으로 정리, 접근법 6가지, 표준 5건, 책임 경계, 연결 영역 17개, 열린 질문 5건. 2차 수정: 출처 5건 제목 정정, 9절 태그 추가, BIM·라이다·RMF 첫 등장 풀어 쓰기. 2차 재검증 수정: 9절 RMF 풀이를 Robotics Middleware Framework 로 정정 (실행 2026-09-30-02)
- 2026-09-30 · 생성 · [67. 기타 현장 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area67-s6.md) — 자동 분리: 67. 기타 현장 의 "6. 대표 접근법과 기술" 절(1,209자)을 옮겼다. 2차 수정: 출처 제목 정정(ref-995·1000·1002·1006·1007) (실행 2026-09-30-02)
- 2026-09-30 · 생성 · [67. 기타 현장 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area67-s7.md) — 자동 분리: 67. 기타 현장 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,102자)을 옮겼다. ref-004 각주 줄은 참고문헌 페이지가 입력에 없어 이전 값을 유지했다(퍼블리셔 대조 요청) (실행 2026-09-30-02)
- 2026-09-30 · 생성 · [67. 기타 현장 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area67-s10.md) — 자동 분리: 67. 기타 현장 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,022자)을 옮겼다. 2차 수정: 20. 로봇·제조사 관제 연동 항목의 창이 공항 서술을 기사 수준으로 고치고 출처 제목 정정 (실행 2026-09-30-02)
- 2026-09-30 · 생성 · [67. 기타 현장 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area67-s4.md) — 자동 분리: 67. 기타 현장 의 "4. 핵심 개념과 용어" 절(903자)을 옮겼다. 2차 수정: ref-1000 제목 정정. ref-004 각주 줄은 참고문헌 페이지가 입력에 없어 이전 값을 유지했다(퍼블리셔 대조 요청) (실행 2026-09-30-02)
<!-- auto:category-recent:end -->
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 110건 / 전체 1282건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-003 | GS1 | EPCIS and CBV Linked Data Model | 미확인 | https://ref.gs1.org/epcis/ | 2026-09-24 | 아니오 |
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 2026-09-25 | 예 |
| ref-005 | Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding in Large-Scale Warehouses | 2020 | https://arxiv.org/abs/2005.07371 | 2026-09-24 | 아니오 |
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 2017 | https://arxiv.org/abs/1705.10868 | 2026-09-24 | 아니오 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | https://github.com/merschformann/RAWSim-O | 2026-09-25 | 예 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 2026-09-25 | 아니오 |
| ref-124 | 국가물류통합정보센터(국토교통부) | 스마트물류센터 인증제 안내 | 미확인 | https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW | 2026-09-25 | 아니오 |
| ref-257 | Interact Analysis | AMR Multi-Fleet Orchestration Software Explained | 미확인 | https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/ | 2026-09-25 | 아니오 |
| ref-382 | Boysen, N., de Koster, R., & Weidinger, F. | Warehousing in the e-commerce era: A survey | 2019 | https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/ | 2026-09-25 | 아니오 |
| ref-872 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART) | RoMi-H Empanelment Programme 2025 | 2025-05-01 | https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste | 2026-09-29 | 예 |
| ref-910 | Azadeh, K., de Koster, R., & Roy, D. (Transportation Science 53(4)) | Robotized and Automated Warehouse Systems: Review and Recent Developments | 2019-06-28 | https://pubsonline.informs.org/doi/10.1287/trsc.2018.0873 | 2026-09-29 | 예 |
| ref-911 | Fragapane, G., de Koster, R., Sgarbossa, F., & Strandhagen, J. O. (European Journal of Operational Research 294(2)) | Planning and control of autonomous mobile robots for intralogistics: Literature review and research agenda | 2021 | https://doi.org/10.1016/j.ejor.2021.01.019 | 2026-09-29 | 예 |
| ref-912 | Schrotenboer, A. H., Wruck, S., Vis, I. F. A., & Roodbergen, K. J. | Integration of returns and decomposition of customer orders in e-commerce warehouses | 2019-09-01 | https://arxiv.org/abs/1909.01794 | 2026-09-29 | 예 |
| ref-913 | 곽경민, 박범, 고은지, 윤철주, 김경훈 (CJ대한통운, 로봇학회 논문지 17(4)) | 급속 확산되는 물류현장의 로봇적용 사례 | 2022 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002899267 | 2026-09-29 | 예 |
| ref-914 | 김태현, 송상화 (인천대학교, 한국디지털산업학회지 26(1)) | 온라인 주문 풀필먼트를 위한 물류센터 피킹 설비 최적화에 대한 연구 | 2021 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002687327 | 2026-09-29 | 예 |
| ref-915 | 로봇신문 (장길수) | CJ대한통운이 뽑은 물류자동화 혁신 기술 '톱3' | 2022-05-06 | https://www.irobotnews.com/news/articleView.html?idxno=28424 | 2026-09-29 | 예 |
| ref-916 | Amazon | Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot | 2025-07 | https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model | 2026-09-29 | 예 |
| ref-917 | 로봇신문 (장길수) | 쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이... | 2023-02-07 | https://www.irobotnews.com/news/articleView.html?idxno=30736 | 2026-09-29 | 예 |
| ref-918 | 물류신문 (석한글) | ‘물류 투자만 6조’, 쿠팡 물류 인프라의 정점 ‘대구 FC’ 가보니 | 2023-02-07 | https://www.klnews.co.kr/news/articleView.html?idxno=306994 | 2026-09-29 | 예 |
| ref-919 | 스마트물류시설인증센터 (한국교통연구원) | 인증스마트물류센터 : 인증심사 > 심사기준 > 일반 | 미확인 | https://cslc.koti.re.kr/new_sub2/new_sub2_2_1 | 2026-09-29 | 예 |
| ref-920 | CJ대한통운 | CJ대한통운 안성 MP허브, 국토부 ‘스마트물류센터 1등급’ 인증 | 2023-10-26 | https://cjlogistics.com/ko/newsroom/news/NR_00001109 | 2026-09-29 | 예 |
| ref-921 | Robotics 24/7 (Eugene Demaitre) | DHL Makes First Commercial Deployment of Boston Dynamics Stretch Robot to Unload Trailers and Containers | 2023-02-01 | https://www.robotics247.com/article/dhl_makes_first_commercial_deployment_boston_dynamics_stretch_robot_unload_trailers_containers | 2026-09-29 | 예 |
| ref-922 | Schmid, N. A., & Limère, V. (International Journal of Production Research 57(24)) | A classification of tactical assembly line feeding problems | 2019-02-23 | https://www.tandfonline.com/doi/full/10.1080/00207543.2019.1581957 | 2026-09-29 | 예 |
| ref-923 | Verband der Automobilindustrie (VDA) | VDA 5050: Managing Transport in Manufacturing Plants | 미확인 | https://www.vda.de/en/news/articles/vda-5050 | 2026-09-29 | 예 |
| ref-924 | SYNAOS (IoT Use Case) | VDA 5050: unified AGV fleet control in real time at VW | 2025-10-16 | https://www.iotusecase.com/en/solution-examples/vda-5050-agv-fleet-control | 2026-09-29 | 예 |
| ref-925 | Wally, B., Vyskočil, J., Novák, P., Huemer, C., Šindelář, R., Kadera, P., Mazak, A., & Wimmer, M. | Flexible Production Systems: Automated Generation of Operations Plans Based on ISA-95 and PDDL | 2019-11-13 | https://arxiv.org/abs/1911.05481 | 2026-09-29 | 예 |
| ref-926 | Siemens | AGV fleet management integration with intralogistics | 미확인 | https://resources.sw.siemens.com/en-US/white-paper-integrating-agv-automated-guided-vehicle-system-with-intralogistics/ | 2026-09-29 | 예 |
| ref-927 | 물류신문 (이경성) | LG전자, 스마트팩토리 솔루션 확대에 AMR 등 물류로봇 적극 활용한다 | 2024-07-18 | https://www.klnews.co.kr/news/articleView.html?idxno=313143 | 2026-09-29 | 예 |
| ref-928 | Pietrantoni, L., Favilla, M., Fraboni, F., Mazzoni, E., Morandini, S., Benvenuti, M., & De Angelis, M. (Frontiers in Robotics and AI) | Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors | 2024-12-02 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1342130/full | 2026-09-29 | 예 |
| ref-929 | Li, M. 외 (Scientific Reports) | Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios | 2026-04-24 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/ | 2026-09-29 | 예 |
| ref-930 | 현대자동차그룹 | ‘혁신의 장場’ HMGICS, 인간 중심 모빌리티 솔루션의 새 시대 열다 | 2023-11-21 | https://www.hyundaimotorgroup.com/ko/news/hmgics-human-centric-mobility-solutions-new-era | 2026-09-29 | 예 |
| ref-931 | 뉴시스 | "로봇 몇 대, 어디로 움직일까"…중소 제조현장에 'AI 공장장' 뜬다 | 2026-09-07 | https://www.newsis.com/view/NISX20260907_0003779780 | 2026-09-29 | 예 |
| ref-932 | 테크데일리 | KETI, LLM 모델 및 모방학습, 조립공정 자동화 기술 공개 | 2025-03-12 | https://www.techdaily.co.kr/news/articleView.html?idxno=25352 | 2026-09-29 | 예 |
| ref-933 | Keshvarparast, A., Battini, D., Battaia, O., & Pirayesh, A. (Journal of Intelligent Manufacturing 35) | Collaborative robots in manufacturing and assembly systems: literature review and future research agenda | 2023-05-30 | https://link.springer.com/article/10.1007/s10845-023-02137-w | 2026-09-29 | 예 |
| ref-934 | Marvel, J. A., Bostelman, R., & Falco, J. (NIST; ACM Computing Surveys 51) | Multi-Robot Assembly Strategies and Metrics | 2018-01-01 | https://dl.acm.org/doi/10.1145/3150225 | 2026-09-29 | 예 |
| ref-935 | 강명훈, 곽춘종 (부산대학교; Asia-Pacific Journal of Business & Commerce) | 시뮬레이션을 이용한 자동차 부품 공급 시스템 도입 방안 분석: R자동차 사례 | 2014-04 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE02448280 | 2026-09-29 | 예 |
| ref-936 | 옥창훈, 김득수, 공정수, 서윤호 (고려대학교, 현대자동차; 한국시뮬레이션학회 논문지 21(2)) | 자동차 생산을 위한 통합창고 연구 | 2012 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001671601 | 2026-09-29 | 예 |
| ref-937 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART) | ROMI-H | Changi General Hospital | 미확인 | https://www.cgh.com.sg/chart/projects/romi-h | 2026-09-29 | 예 |
| ref-938 | Applus+ Laboratories | ISO 3691-4:2023: Compliance Testing for Automated Guided Vehicles (AGVs) | 미확인 | https://www.appluslaboratories.com/global/en/what-we-do/service-sheet/iso-3691-4-2023-compliance-testing-for-automated-guided-vehicles-agvs | 2026-09-29 | 예 |
| ref-939 | 이데일리 | 분당서울대병원, 무거운 이송카트 로봇자율배송, 무안경 3D 의료실습에 도입 | 2023-07-06 | https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01403846635671896 | 2026-09-29 | 예 |
| ref-940 | 뉴스투데이 | [한림대성심병원 로봇 사용기 (下)] 배송로봇, 엘리베이터 타고 횡단보도 건너 검체 운반 | 2025-02-11 | https://www.news2day.co.kr/article/20250211500007 | 2026-09-29 | 예 |
| ref-941 | 데일리팜 | 원내 약 배송로봇 도입 확대...정부 지원에 변화 바람 | 2024-07-15 | https://m.dailypharm.com/user/news/15128 | 2026-09-29 | 예 |
| ref-942 | Open Robotics | ROMI-H: Bringing Robot Traffic Control to Healthcare | 2021-02-10 | https://www.openrobotics.org/blog/2021/2/10/romi-h-bringing-robot-traffic-control-to-healthcare | 2026-09-29 | 예 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 2026-09-29 | 예 |
| ref-944 | 로봇신문 | 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' | 2024-04-15 | http://www.irobotnews.com/news/articleView.html?idxno=34601 | 2026-09-29 | 예 |
| ref-945 | 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | https://eiec.kdi.re.kr/policy/materialView.do?num=220004 | 2026-09-29 | 예 |
| ref-946 | Babalola, G. T., Gaston, J.-M., Trombetta, J., & Tulk Jesso, S. (Frontiers in Robotics and AI) | A systematic review of collaborative robots for nurses: where are we now, and where is the evidence? | 2024-06-05 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1398140/full | 2026-09-29 | 예 |
| ref-947 | 한국로봇산업진흥원 | 서비스로봇 실증사업 | 미확인 | https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do | 2026-09-29 | 예 |
| ref-948 | 비즈한국 | 병원에 늘어나는 '로봇', 의사·간호사도 편해졌을까 | 2025-04-10 | https://bizhankook.com/articles/29394.html | 2026-09-29 | 예 |
| ref-949 | 최현철, 서슬기, 권재용, 박상찬, 장혜정 (경희대학교, Korea SUNY; 품질경영학회지 51(3)) | 감염환자 이송 로봇에 대한 의료종사자의 인식: SERVQUAL과 AHP를 활용하여 | 2023 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002997683 | 2026-09-29 | 예 |
| ref-950 | 한국보건산업진흥원 스마트병원 확산지원센터 | 선도모델 및 모듈 소개 | 미확인 | https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040 | 2026-09-29 | 예 |
| ref-951 | 지디넷코리아 (윤상은) | 엘베 타고 수건 배달·안내·방역도 '척척'...호텔로 간 로봇 | 2022-05-03 | https://zdnet.co.kr/view/?no=20220503124850 | 2026-09-29 | 예 |
| ref-952 | Retail Dive (Sam Silverstein) | Sam's Club rolls out inventory-checking robots chainwide | 2022-02-01 | https://www.retaildive.com/news/sams-club-rolls-out-inventory-checking-robots-chainwide/618040/ | 2026-09-29 | 예 |
| ref-953 | Kanda, T., Shiomi, M., Miyashita, Z., Ishiguro, H., & Hagita, N. (IEEE Transactions on Robotics 26(5)) | A Communication Robot in a Shopping Mall | 2010-10 | https://ieeexplore.ieee.org/abstract/document/5557825 | 2026-09-29 | 아니오 |
| ref-954 | Ivanov, S., Seyitoğlu, F., & Markova, M. (Information Technology & Tourism) | Hotel managers' perceptions towards the use of robots: a mixed-methods approach | 2020-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7486590/ | 2026-09-29 | 예 |
| ref-955 | 지디넷코리아 (신영빈) | 식당 음식 나르던 서빙로봇, 공장·창고로 진격 | 2024-07-30 | https://zdnet.co.kr/view/?no=20240730115912 | 2026-09-29 | 예 |
| ref-956 | 지디넷코리아 (김성현) | 네이버 제2사옥, 로봇 친화형 건축물 인증 획득 | 2022-04-11 | https://zdnet.co.kr/view/?no=20220411142336 | 2026-09-29 | 예 |
| ref-957 | Otis Elevator Company | Elevators and service robots | 미확인 | https://www.otis.com/en/us/innovation/elevators-and-service-robots | 2026-09-29 | 예 |
| ref-958 | 이투데이 (구예지) | 브이디컴퍼니, 신규 서빙로봇 3종 출시…“식당 전체 자동화 이룰 것” | 2023-03-30 | https://www.etoday.co.kr/news/view/2235962 | 2026-09-29 | 예 |
| ref-959 | 한국노동연구원 (박수민 외) | 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향 | 2024 | https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf | 2026-09-29 | 아니오 |
| ref-960 | Odekerken-Schröder, G., Mennens, K., Steins, M., & Mahr, D. (Journal of Service Management 33(2)) | The service triad: an empirical study of service robots, customers and frontline employees | 2022 | https://www.emerald.com/josm/article/33/2/246/227998/The-service-triad-an-empirical-study-of-service | 2026-09-29 | 예 |
| ref-961 | Responsible AI Collaborative (AI Incident Database) | Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks | 미확인 | https://incidentdatabase.ai/cite/346/ | 2026-09-29 | 예 |
| ref-962 | Hotel Technology News | Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce | 2019-01 | https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/ | 2026-09-29 | 예 |
| ref-963 | 서울경제 (백주연) | 엘리베이터 타고 쇼핑몰 왔다갔다…바닥 물걸레질까지 하는 '로봇 청소부' 등장 | 2025-04-02 | https://www.sedaily.com/article/14048085 | 2026-09-29 | 예 |
| ref-964 | Karlsen, A. S. T., Andersen, B., Nevstad, K., Heirsaunet, S. E., Indergård, E., & Aarseth, W. (Frontiers in Robotics and AI) | Digital transformation in restaurants: key aspects of service robot deployment from project initiation to evaluation | 2026-04-22 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1793138/full | 2026-09-29 | 예 |
| ref-965 | 삼성물산 뉴스룸 | 삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영 | 2026-01-15 | https://news.samsungcnt.com/ko/%EC%A0%84%EC%B2%B4%EA%B8%B0%EC%82%AC/%EA%B1%B4%EC%84%A4%EB%B6%80%EB%AC%B8/2026-01-%EC%82%BC%EC%84%B1%EB%AC%BC%EC%82%B0-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%84%B8%EB%8C%80-%ED%98%84%EA%B4%80%EA%B9%8C%EC%A7%80-%EC%9D%8C%EC%8B%9D%EB%B0%B0%EB%8B%AC%EB%A1%9C%EB%B4%87-%ED%99%95%EC%9E%A5/ | 2026-09-29 | 예 |
| ref-966 | 지디넷코리아 (신영빈) | 로봇이 문앞까지 택배 가져다 주는 미래 곧 온다 | 2025-01-19 | https://zdnet.co.kr/view/?no=20250119062609 | 2026-09-29 | 예 |
| ref-967 | AI타임스 | 실외이동로봇 시대 개막...개정 지능형로봇법 17일 시행 | 2023-11-16 | https://www.aitimes.com/news/articleView.html?idxno=155217 | 2026-09-29 | 예 |
| ref-968 | MIT Technology Review (Eileen Guo) | A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook? | 2022-12-19 | https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/ | 2026-09-29 | 예 |
| ref-969 | 바이라인네트워크 | '로봇청소기' 다수 제품 보안 취약…대응방안은? | 2025-10-31 | https://byline.network/2025/10/31-283/ | 2026-09-29 | 예 |
| ref-970 | 매일신문 | 사생활 훔치는 로봇청소기…중국산 제품서 `무단 촬영` 가능성 확인 | 2025-10-06 | https://www.imaeil.com/page/view/2025100618362463025 | 2026-09-29 | 예 |
| ref-971 | Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판) | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 2024-03-14 | https://arxiv.org/abs/2403.09227 | 2026-09-29 | 예 |
| ref-972 | Hwang, I. T., Kim, G. T., & Kwag, B. C. (한국생활환경학회지 30) | Comparing Perceptions of Service Robot Adoption in Multi-Family Housing Between Residents and Industry Stakeholders: Focusing on Acceptance Attitudes, Concerns, and Technological Needs | 2026-06 | https://journal.ksles.org/articles/xml/g9G5/ | 2026-09-29 | 예 |
| ref-973 | The Robot Report (Mike Oitzman) | NEO humanoid designed for household use, available for preorder | 2025-10-30 | https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/ | 2026-09-29 | 예 |
| ref-974 | LG Electronics USA | LG ELECTRONICS PRESENTS LG CLOiD HOME ROBOT TO DEMONSTRATE "ZERO LABOR HOME" AT CES 2026 | 2026-01-06 | https://www.lg.com/us/press-release/lg-cloid-home-robot | 2026-09-29 | 예 |
| ref-975 | 한국경제 (김익환) | 배송·주차·청소까지…로봇 아파트 뜬다 | 2026-09-27 | https://www.hankyung.com/article/2026092776141 | 2026-09-29 | 예 |
| ref-976 | 정보통신신문 (김연균) | 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’ | 2024-07-18 | https://www.koit.co.kr/news/articleView.html?idxno=123976 | 2026-09-29 | 예 |
| ref-977 | Connectivity Standards Alliance (CSA) | Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board | 2023-10-23 | https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/ | 2026-09-29 | 예 |
| ref-978 | CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관) | 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) | 2023-03-14 | https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4_%EB%B3%B4%ED%98%B8%EB%B2%95/%EC%A0%9C25%EC%A1%B0%EC%9D%982 | 2026-09-29 | 예 |
| ref-979 | 미디어펜 (조태민) | 로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도 | 2026-09-20 | https://www.mediapen.com/news/view/1124680 | 2026-09-29 | 예 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 2026-09-30 | 예 |
| ref-981 | DC Velocity | Starship steers its delivery robots off college campuses and toward grocery sector | 2026-06-08 | https://www.dcvelocity.com/transportation/trucking/last-mile/starship-steers-its-delivery-robots-off-college-campuses-and-toward-grocery-sector | 2026-09-30 | 예 |
| ref-982 | Tong, X., & Simoni, M. D. (arXiv) | Robust Route Planning for Sidewalk Delivery Robots | 2025-07-16 | https://arxiv.org/abs/2507.12067 | 2026-09-30 | 예 |
| ref-983 | 지디넷코리아 | 배민, 차세대 배달로봇 ‘딜리’ 8월 투입…운행안전인증 획득 | 2025-06-23 | https://zdnet.co.kr/view/?no=20250623095742 | 2026-09-30 | 예 |
| ref-984 | 스포츠경향 | 뉴빌리티, 덕수궁 순찰부터 도쿄 시내 배달까지 | 2026-09-02 | https://sports.khan.co.kr/article/202609020605003/ | 2026-09-30 | 예 |
| ref-985 | 内閣府 (일본 내각부) | 令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について | 2023 | https://www8.cao.go.jp/koutu//taisaku/r05kou_haku/zenbun/genkyo/topics/topic_1.html | 2026-09-30 | 예 |
| ref-986 | Supply Chain Dive | Why delivery robots face a regulatory ‘nightmare’ | 2023-04-26 | https://www.supplychaindive.com/news/delivery-robot-bills-laws-proliferate-state-legislatures/648303/ | 2026-09-30 | 예 |
| ref-987 | The Pitt News | Pitt pauses testing of Starship robots due to safety concerns | 2019-10-21 | https://pittnews.com/article/151679/news/pitt-pauses-testing-of-starship-robots-due-to-safety-concerns/ | 2026-09-30 | 예 |
| ref-988 | Open Navigation (Nav2) | Navigating Using GPS Localization — Nav2 documentation | 미확인 | https://docs.nav2.org/jazzy/tutorials/general_tutorials/navigation2_with_gps/navigation2_with_gps/ | 2026-09-30 | 예 |
| ref-989 | Urban Robotics Foundation (Bern Grush) | ISO-4448 Update Winter 2024 | 2024-02-04 | https://www.urbanroboticsfoundation.org/post/iso-4448-update-winter-2024 | 2026-09-30 | 예 |
| ref-990 | Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18) | Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists | 2023-03 | https://doi.org/10.1016/j.trip.2023.100789 | 2026-09-30 | 예 |
| ref-991 | 대한민국 정책브리핑 (산업통상자원부·경찰청) | ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 | 2023-11-16 | https://www.korea.kr/news/policyNewsView.do?newsId=148922726 | 2026-09-30 | 예 |
| ref-992 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 | 2023-07-28 | https://zdnet.co.kr/view/?no=20230728173101 | 2026-09-30 | 예 |
| ref-993 | Dobrosovestnova, A., Schwaninger, I., & Weiss, A. (IEEE RO-MAN 2022) | With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow | 2022 | https://ieeexplore.ieee.org/abstract/document/9900588/ | 2026-09-30 | 예 |
| ref-994 | ISO | ISO/TR 4448-1:2024 Intelligent transport systems — Public-area mobile robots (PMR) — Part 1: Overview of paradigm | 2024-08 | https://www.iso.org/standard/81068.html | 2026-09-30 | 아니오 |
| ref-995 | Offshore Technology (Eve Thomas) | Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones | 2025-11-21 | https://www.offshore-technology.com/features/equinor-autonomous-robotics/ | 2026-09-30 | 예 |
| ref-996 | Burger, B., Maffettone, P. M., Gusev, V. V. 외 (Nature 583) | A mobile robotic chemist | 2020-07 | https://www.nature.com/articles/s41586-020-2442-2 | 2026-09-30 | 아니오 |
| ref-997 | 이코노미스트 (송재민) | 로봇이 로봇들을 움직이는, 네이버 1784 | 2023-01-11 | https://economist.co.kr/article/view/ecn202301110006 | 2026-09-30 | 예 |
| ref-998 | 로봇신문 (정원영) | 인천국제공항, 안내 로봇 '에어스타' 본격 운영 | 2018-07-11 | https://www.irobotnews.com/news/articleView.html?idxno=14422 | 2026-09-30 | 예 |
| ref-999 | 서울신문 | 로봇 '스팟' 건설현장 누빈다…현대건설 품질·안전 관리 | 2022-11-15 | https://www.seoul.co.kr/news/economy/2022/11/15/20221115500118 | 2026-09-30 | 예 |
| ref-1000 | 인더스트리뉴스 (정형우) | GS건설, 4족보행 로봇 '스팟(SPOT)' 국내 최초 건설현장 도입하기로 | 2020-07-13 | https://www.industrynews.co.kr/news/articleView.html?idxno=38911 | 2026-09-30 | 예 |
| ref-1001 | SiLA Consortium | SiLA Standards | 미확인 | https://sila-standard.com/standards/ | 2026-09-30 | 예 |
| ref-1002 | 아주경제 (윤선훈) | 아시아 최대 규모 데이터센터…네이버 '각 세종' 본격 가동 | 2023-11-08 | https://www.ajunews.com/view/20231107091520837 | 2026-09-30 | 예 |
| ref-1003 | Korial (구 Energy Robotics) — Andre Retterath, Earlybird Venture Capital 기고 | Game-changer: The rationale behind the investment in Energy Robotics | 2021-01-15 | https://www.energy-robotics.com/post/revolutionizing-industrial-inspection-the-rationale-behind-the-investment-in-energy-robotics | 2026-09-30 | 예 |
| ref-1004 | The Robot Report | Singapore's National Robotics Programme reveals initiatives to advance robot adoption | 2025-10-29 | https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/ | 2026-09-30 | 예 |
| ref-1005 | 헬로디디 (이유진) | 스스로 수확하고 운반···'로봇농부' 나왔다 | 2023-03-09 | https://www.hellodd.com/news/articleView.html?idxno=99827 | 2026-09-30 | 예 |
| ref-1006 | 농민신문 (조영창) | 농민 뒤 졸졸 '운반로봇'…무거운 수확물 옮기고 자동 하역 | 2024-03-25 | https://www.nongmin.com/article/20240322500556 | 2026-09-30 | 예 |
| ref-1007 | 뉴스토마토 (이규하) | 방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동 | 2025-04-23 | https://www.newstomato.com/ReadNews.aspx?no=1259970 | 2026-09-30 | 예 |
| ref-1008 | 넷매니아즈 (손장우) | 한전의 5G 특화망 기반 응용: IoT 예방진단, 로봇기반 순시점검 및 안전관리 | 2023-09-30 | https://www.netmanias.com/ko/post/blog/15878/5g-5g-private-5g-5g/applications-based-on-kepco-s-private-5g-network-iot-preventive-diagnosis-robot-based-inspection-and-safety-management | 2026-09-30 | 예 |
| ref-1009 | ISO | ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones | 2024 | https://www.iso.org/standard/82687.html | 2026-09-30 | 아니오 |
```

### docs/glossary/index.md (요약: 용어 364개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- actively-exploited-vulnerability: 적극 악용 취약점 (Actively Exploited Vulnerability (EU Cyber Resilience Act))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alarm-management: 경보 관리 (Alarm Management (ANSI/ISA 18.2))
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
- curb-cut: 연석 경사로 (Curb Cut (Curb Ramp))
- cyber-resilience-act: 사이버복원력법 (Cyber Resilience Act (CRA))
- data-holder: 데이터 보유자 (Data Holder (EU Data Act))
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
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- life-cycle-costing: 수명주기 비용 분석 (Life Cycle Costing (LCC, IEC 60300-3-3))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
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
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
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
- pay-per-pick: 피킹량 기반 과금 (Pay-per-pick)
- payback-period: 투자 회수 기간 (Payback Period)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- post-occupancy-evaluation: 사용 후 평가 (Post-Occupancy Evaluation (POE))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
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
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
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
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- total-cost-of-ownership: 총소유비용 (Total Cost of Ownership (TCO))
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- utaut: 통합 기술 수용 이론 (Unified Theory of Acceptance and Use of Technology (UTAUT))
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
- wireless-safety-rated-emergency-stop: 무선 안전 비상정지 (Wireless Safety-rated Emergency Stop)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [61, 62, 63, 64, 65, 66, 67] 에 걸린 61건 / 전체 321건)

```markdown
- oq-134 [열림] 국내 물류창고·병원에서 로봇 운영 기록으로 혼잡·고장·승강기 대기 같은 실제 상황을 시뮬레이션에 재현한 사례가 있는가(이번 조사에서 확인된 국내 자료는 설계 검증·모니터링용 디지털 트윈과 시나리오 기반 검증뿐이다)? (영역 11, 61, 63)
- oq-138 [열림] 국내 물류창고·병원·제조 공장에서 대화로 로봇 작업 시나리오를 구성한 사례가 있는가(이번 조사에서 확인된 국내 자료는 자연어 로봇 제어 동향 논문뿐이다)? (영역 9, 61, 63)
- oq-142 [열림] 국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 ETRI 동향 논문뿐이다)? (영역 12, 61, 63, 62)
- oq-146 [열림] 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가(이번 조사에서 확인된 현장 사례는 네덜란드 슈퍼마켓 연구뿐이다)? (영역 13, 60, 61)
- oq-149 [열림] 싱가포르 공공 의료의 RoMi-H 등재 프로그램처럼 벤더·통합사를 사전 평가해 등록 자격을 주는 관문을 국내 병원·공공 현장에서 운용한 사례나 제도가 있는가? (영역 4, 63, 58)
- oq-163 [열림] 국내 물류센터에서 서로 다른 제조사의 AGV·소팅봇·무인지게차·하역 로봇을 하나의 오케스트레이션 계층으로 관제한 공개 사례가 있는가(쿠팡 대구·CJ대한통운 사례는 설비별 도입만 확인됐다)? (영역 61, 20)
- oq-164 [열림] 스마트물류센터 인증 심사기준의 정보시스템 항목(WMS 150점, WCS/MCS 50점)에서 이기종 로봇 오케스트레이션 계층은 어느 항목으로 평가되며 인증 심사가 로봇 플릿 관제 기능을 따로 보는가? (영역 61, 23)
- oq-165 [열림] 반품 재적치를 피킹 경로에 통합하는 최적화 연구를 로봇 이동형 풀필먼트 시스템이나 AMR 협업 피킹에 적용한 연구·사례가 있는가? (영역 61, 25)
- oq-166 [열림] 트레일러 하역 로봇의 떨어진 상자 복구 같은 예외 처리가 로봇 자체 복구와 오케스트레이션 계층의 재계획 사이에서 어떻게 분담되는지 공개된 인터페이스나 사례가 있는가? (영역 61, 32)
- oq-167 [열림] 국내 제조 공장에서 서로 다른 제조사의 AGV·AMR·모바일 매니퓰레이터를 VDA 5050 같은 표준 인터페이스로 하나의 관제 계층 아래 운영한 공개 사례가 있는가(확인된 국내 사례는 자체 로봇 도입과 정부 시범사업뿐이다)? (영역 62, 21)
- oq-168 [열림] 생산 관리 시스템(MES)이 로봇 플릿에 내는 운송·공정 작업 요청과 완료 보고에 ISA-95 의 작업 요청·작업 응답 모델을 실제로 쓴 공개 사례나 표준 매핑이 있는가? (영역 62, 23)
- oq-169 [열림] 셀 생산 방식에서 여러 셀이 동시에 같은 부품을 요청할 때 운반 로봇 배정과 셀 안 로봇팔·작업자의 조립 순서를 어떤 계층이 조율하며 라인 정지·결품 시 재계획 책임은 어디에 있는가? (영역 62, 32)
- oq-170 [열림] ISO 3691-4:2023 의 운용 구역 분류와 사람 감지 요구가 이기종 플릿 관제 계층에 어떤 정보(구역·속도 제한·모드)를 요구하는지 표준 원문으로 확인할 수 있는가(이번 조사는 인증 기관 설명만 확인했다)? (영역 62, 50)
- oq-171 [열림] 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)의 촬영 사실 표시·촬영 거부 규정이 병원 이송 로봇의 카메라·센서 촬영에 어떻게 적용되며, 환자·방문객 영상을 관제 계층이 어디까지 저장·전송할 수 있는지 법령 원문과 해석 사례로 확인할 수 있는가(이번 조사는 법령 원문을 열지 못했다)? (영역 63, 53)
- oq-172 [열림] 격리 병동·감염 관리 구역을 지나는 이송 로봇의 출입 허용 규칙과 로봇 표면 소독 절차를 병원 감염관리 조직이 어떻게 정하고 로봇 플릿 관제가 이를 경로·배정 제약으로 어떻게 받는지 공개된 지침이나 연구가 있는가? (영역 63, 48)
- oq-173 [열림] 국가기술표준원이 2021년 제정을 발표한 로봇의 승강기 탑승 안전 요구사항 KS 와 실내 배송 로봇 KS 의 표준 번호·조항은 무엇이며, 그 요구(속도 제어·보호 정지·높낮이차·틈새)가 승강기 연동 계층에 어떤 정보를 요구하는가? (영역 63, 22, 59)
- oq-174 [열림] 한림대성심병원처럼 제조사가 다른 여러 로봇을 통합관제하는 국내 병원은 어떤 인터페이스·표준(Open-RMF, VDA 5050, 제조사 API)으로 로봇과 승강기를 연결하며 그 구조가 공개돼 있는가? (영역 63, 20)
- oq-175 [열림] 국내 병원에서 식사(환자식) 이송을 로봇이 맡은 운영 사례가 있으며, 식사 이송은 약품·검체 이송과 시작 조건·시간 제약·인계 방식이 어떻게 다른가? (영역 63)
- oq-176 [열림] 호텔·쇼핑몰에서 제조사가 다른 배송·청소·안내 로봇을 하나의 오케스트레이션 계층(Open-RMF 등)으로 묶어 승강기를 함께 쓰게 한 국내외 공개 사례가 있는가? (영역 64, 20, 22)
- oq-177 [열림] 호텔 객실 배송 로봇이 객실 관리 시스템(PMS)이나 객실 전화에서 요청을 받고 배송 완료를 되돌려 주는 표준 인터페이스나 공개된 연동 구조가 있는가? (영역 64, 23)
- oq-178 [열림] 영업 중인 매장·쇼핑몰에서 청소·재고 스캔 로봇을 손님이 많은 시간과 어떻게 나눠 운영하는지(운영 시간대 규칙과 그 효과)를 수치로 보인 연구나 공개 자료가 있는가? (영역 64, 26)
- oq-179 [열림] 로봇 친화형 건축물 인증이 오피스를 넘어 호텔·쇼핑몰 같은 상업 시설로 확대됐는가? (영역 64, 22)
- oq-180 [열림] 식당 서빙로봇과 호텔 배송 로봇은 손님이 음식·물품을 받았는지(완료·인계)를 어떤 방식(무게 감지·버튼·직원 확인·객실 문 앞 알림)으로 확인하며 그 결과가 주문 시스템에 기록되는가? (영역 64, 17)
- oq-181 [열림] 세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 영상 수집에는 개인정보 보호법 제25조의2(이동형 영상정보처리기기)가 적용되는가, 아니면 동의 기반 처리 조항만 적용되는가, 그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가? (영역 65, 53)
- oq-182 [열림] 이동로봇 특별법안이 간소화·표준화하겠다는 공동현관·엘리베이터 통신 연동 절차는 어떤 기존 표준(KS 로봇 승강기 탑승 요구사항, 홈네트워크 월패드 규격)을 참조하며, 한 단지에서 제조사가 다른 배송로봇이 같은 인터페이스를 쓰게 하는가? (영역 65, 22, 21)
- oq-183 [열림] 한 아파트 단지에서 제조사가 다른 배송·청소·순찰·주차 로봇을 하나의 관제 계층으로 묶어 공동현관·승강기를 함께 쓰게 한 국내외 공개 사례가 있는가? (영역 65, 20)
- oq-184 [열림] 공동주택 배송로봇의 수령 확인(주문자만 꺼낼 수 있는 방식)은 어떤 인증 수단(비밀번호·앱·QR)으로 이루어지며, 그 결과가 배달 앱·택배사 시스템에 완료 이벤트로 어떻게 돌아가는가? (영역 65, 17, 23)
- oq-185 [열림] 소유자가 원격 조작자를 예약해 가정 로봇을 안내하게 하는 방식(1X NEO 등)에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가? (영역 65, 53, 58)
- oq-186 [열림] 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시는 무엇이며, 경사로·알림음·등화장치 같은 기존 항목은 어느 항목에 흡수됐는가? (영역 66, 50, 59)
- oq-187 [열림] 운행안전인증 대상이 로봇과 관제장치의 조합인데, 제조사가 다른 실외 로봇을 하나의 오케스트레이션 계층에서 지시할 때 그 계층이 인증상 관제장치에 해당하는지, 재인증이 필요한지에 관한 기준이나 해석이 있는가? (영역 66, 20, 59)
- oq-188 [열림] 국내 보도에서 배송·순찰 로봇이 횡단 대기 중 연석 경사로·점자블록을 막지 않도록 하는 대기 위치 규칙이나 접근성 기준(인증 항목·지침)이 있는가? (영역 66, 60, 16)
- oq-189 [열림] 국내 실외 로봇 운영사는 강설·결빙·폭우 때 운행 중단·재개 기준과 고립 로봇 회수 절차를 어떻게 정하고 있으며, 그 기준이 공개된 자료가 있는가? (영역 66, 32)
- oq-190 [열림] 나라·주마다 다른 보도 로봇 규정(속도·크기·신고·보행자 의무)을 경로·속도 제약으로 기계가 읽을 수 있게 표현하는 공통 모델이 있으며, ISO 4448 의 경로 계획 충분성·운행 데이터 기록기 부분이 이를 다루는가? (영역 66, 21, 16)
- oq-191 [열림] 싱가포르 SS 713(로봇·승강기·자동문 데이터 교환)과 TR 130(로봇·중앙 관제 상호운용)은 무엇을 규정하며, ISO 제안은 어디까지 진행됐고 국내 로봇 승강기 탑승 KS 와는 어떻게 다른가? (영역 67, 22, 21)
- oq-192 [열림] 농촌진흥청 통합 관리 프로그램은 다른 제조사의 농업 로봇도 연결할 수 있는 공개 인터페이스를 갖는가, 아니면 자체 개발 로봇 3종 전용인가? (영역 67, 20)
- oq-193 [열림] 건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추며, 드론과 지상 로봇을 한 계층에서 함께 운영한 국내 공개 사례가 있는가? (영역 67, 14, 16)
- oq-194 [열림] 플랜트·변전소 점검 로봇이 얻은 계기값·열화상·이상 판정은 설비 보전 시스템의 작업 지시·점검 기록으로 어떤 형식과 승인 절차를 거쳐 돌아가는가? (영역 67, 23, 38)
- oq-195 [열림] SiLA 로봇·이동 로봇 작업반은 실험실 이동 로봇의 능력과 작업 인계를 어떻게 표현하려 하며, 결과물이 공개됐는가? (영역 67, 21, 5)
- oq-203 [열림] 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가? (영역 16, 40, 63)
- oq-205 [열림] 국토지리정보원 실내공간정보(지하철·철도역사 등)를 로봇 운영 지도나 장소 목록의 출발점으로 쓴 국내 사례가 있는가? (영역 16, 67)
- oq-215 [열림] 구로병원 실증의 전체 성공률 87.03% 가 122건 중 실패 14건과 맞지 않는데(약 88.5%) 성공률의 분모는 무엇인가? (영역 43, 63)
- oq-218 [열림] 국내 로봇 AI 파운데이션 모델 과제의 물류센터 실증 목표(자동화율 80%, 성공률 90%)에 대한 공개된 측정 결과가 있는가? (영역 44, 61)
- oq-219 [열림] 출처 충돌: BMW 그룹 보도자료(2026-06-25) 안에서 Figure 02의 스파턴버그 배치 기간이 10개월과 11개월로 엇갈리는데, 실제 배치 기간은 얼마인가? (영역 44, 62)
- oq-224 [열림] 국내 물류창고·병원·공장에서 로봇 배정·경로에 강화학습·모방학습 같은 학습 기반 방법을 적용한 공개 사례나 연구가 있는가? (영역 46, 61)
- oq-236 [열림] 국내 아파트·병원·물류센터·호텔을 본뜬 다중 로봇 시나리오 예제 라이브러리를 공개한 기관이나 프로젝트가 있는가? (영역 33, 65)
- oq-242 [열림] 병원 검체 이송 같은 업무에서 로봇·컨베이어·사람 운반을 같은 조건으로 비교해 로봇에게 맡길 업무를 정한 정량 연구가 있는가? (영역 2, 63)
- oq-245 [열림] 가정·공동주택과 기타 현장(공공시설·연구실 등)에서 여러 로봇에게 맡길 일과 요구를 사용자와 함께 도출한 연구나 실증 사례가 있는가? (영역 2, 65, 67)
- oq-251 [열림] 국내 KS B ISO 10218-1·-2 는 ISO 10218:2025 판을 언제 부합화하며, 산업안전보건기준에 관한 규칙의 협동로봇 방책 면제 인정 기준과 협동로봇 설치 작업장 안전인증은 새 판(로봇 분류·기능 안전 요구 변경)을 기준으로 바뀌는가? (영역 50, 62)
- oq-254 [열림] ISO/FDIS 13482 개정판은 여러 대가 함께 운영되는 서비스 로봇의 플릿 관제·승강기 연동·소프트웨어 갱신에 관한 안전 요구를 포함하는가? (영역 50, 64, 63)
- oq-258 [열림] 한 병원의 실제 기록으로 찾은 승강기 가동률 임계값 같은 운영 기준이 다른 병원 구조·승강기 제어 정책을 재현한 시뮬레이션에서도 유지되는지 검증한 연구가 있는가? (영역 36, 63, 22)
- oq-264 [열림] 병원·호텔에서 안내 데스크·프런트 담당자가 로봇 요청을 대신 입력하는 방식과 현장 사용자가 직접 요청하는 방식의 처리 시간·오류·업무 부담을 비교한 연구가 있는가? (영역 40, 63, 64)
- oq-269 [열림] 병원 배송 로봇 경제성 평가의 비용 항목·할인율·인건비 산정 방식을 비교 가능한 기준으로 정리한 연구가 있으며, 국내 병원 인건비 조건에서도 같은 결론이 나오는가? (영역 3, 63)
- oq-273 [열림] 병원·상업 시설·물류창고에서 시간대별 사람 혼잡을 로봇 작업 시간 추정과 배정·스케줄링에 반영해 처리 시간이나 지연 변화를 측정한 현장 연구가 있는가? (영역 19, 26, 63)
- oq-274 [열림] 기지국 기반 인파관리지원시스템 같은 공공 인파 밀집 데이터를 실외 배송로봇의 경로·운행 제한에 연동한 국내 사례나 데이터 제공 조건이 있는가? (영역 19, 66)
- oq-284 [열림] 서비스 로봇 본체에 달린 터치스크린·주문 화면이나 운영자·이용자용 채팅 화면이 장애인차별금지법상 무인정보단말기에 해당해 접근성 의무를 지는가? (영역 60, 59, 64)
- oq-287 [열림] 국내 병원·물류창고에서 로봇 도입 뒤 종사자 수용성과 직무 변화를 기관 자체 설문이 아닌 독립 연구로 조사한 자료가 있는가? (영역 60, 63, 61)
- oq-288 [열림] 한국 실외이동로봇 책임보험·공제의 최저 가입금액(사망·부상·재물 한도)을 정한 산업통상자원부령 조항과 금액은 무엇인가? (영역 59, 66)
- oq-293 [열림] 병원 운반 로봇의 생체 인식·PIN 수령 확인처럼 수령인 인증 결과를 작업 완료·인계 이벤트로 ROP 와 병원 정보 시스템에 남기는 공개 인터페이스나 표준 필드가 있는가? (영역 17, 51, 63)
- oq-296 [열림] 전자의무기록 주문이 로봇 작업 요청을 자동으로 만드는 병원 연동에서 주문 취소·변경을 진행 중인 로봇 작업에 반영하고 결과를 기록에 되돌린 공개 사례가 있는가? (영역 40, 23, 63)
- oq-299 [열림] 비전 언어 모델의 평면도 해석이 큰 개방 구역에서 성능이 떨어진다는 보고가 물류창고·제조 공장처럼 넓은 개방 구역이 많은 비주거 시설 도면에서 어떤 오류로 나타나는가? (영역 14, 45, 61)
- oq-313 [열림] 실외이동로봇의 운행안전인증 단위에 관제장치가 포함될 때, 관제를 맡는 오케스트레이션 플랫폼 사업자도 지능형로봇법의 운영자 보험 가입 의무 대상이 되는가? (영역 59, 58, 66)
```
