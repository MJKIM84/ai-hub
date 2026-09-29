(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-01
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 66. 실외 (Q. 현장 유형별 적용)
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

### runs/2026-09-30-01/target.json

```json
{
  "run_id": "2026-09-30-01",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 110,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 66,
    "area_name": "66. 실외",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=66"
}
```

### runs/2026-09-30-01/research.json

```json
{
  "run_id": "2026-09-30-01",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 66,
    "area_name": "66. 실외",
    "category": "Q. 현장 유형별 적용"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 공공 영역 이동로봇(PMR)·개인 배송 장치(PDD)·원격 조작형 소형차·실시간 이동 측위(RTK)·침범 후 시간(PET) 용어 없음(실외이동로봇 운행안전인증·원격 조작은 용어집에 이미 있음)",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 보도 배송(배민 딜리), 순찰(뉴빌리티 뉴비), 캠퍼스 배송(Starship·NAU), 접근성 사고(피츠버그), 눈 속 고립(탈린)과 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 위성 위치·센서 융합, 불확실성을 고려한 경로 계획, 날씨·사람 도움에 기대는 예외 처리 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 지능형로봇법 운행안전인증, 도로교통법 보행자 지위, 일본 원격 조작형 소형차, 미국 주 PDD 법, ISO 4448 시리즈, Nav2 GPS 항법 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음 — 보도 로봇–보행자 상충 관측 연구, 눈 속 로봇 연구, 강건 경로 계획 연구 없음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건, 정정 요청 없음",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? [분류원문]",
    "국내에서 실외 로봇이 보도를 다니려면 어떤 법적 요건(지능형로봇법 운행안전인증, 도로교통법상 보행자 지위, 보험)을 갖춰야 하며 그 기준은 어떻게 바뀌어 왔는가? (섹션 3·7 겨냥, 한국 자료 우선)",
    "일본·미국 등 다른 나라는 보도 주행 로봇의 크기·속도·신고를 어떻게 규정하고, 관할마다 다른 규정은 운영에 어떤 제약을 주는가? (섹션 7·9 겨냥)",
    "실외 배송·순찰·캠퍼스 운영의 실제 사례(국내외)는 어떤 작업을 어디서 어떻게 하고 있으며 여섯 항목으로 어떻게 정리되는가? (섹션 5 겨냥, 현장 유형 실외 명시)",
    "눈·비 같은 날씨와 보행자·장애물은 실외 로봇의 운행·경로·예외 처리에 어떤 영향을 주며 이를 다루는 방법은 무엇인가? (섹션 6·8 겨냥)",
    "실외 로봇의 위치 추정(위성 위치·RTK·센서 융합)은 어떤 한계가 있고, 공공 영역 이동로봇 표준(ISO 4448 등)은 무엇을 다루는가? (섹션 6·7 겨냥)",
    "실외에서 ROP 가 직접 맡을 것(요청 수신·배정·관할별 규정과 날씨를 경로·속도 제약으로 반영·예외 인계)과 로봇 자체 주행·위치 추정·배달 앱·법적 인증에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "한국로봇산업진흥원 안내에 따르면 실외이동로봇 운행안전인증은 지능형로봇법 제40조의2에 따른 의무인증으로, 최대 속도 15km/h·최대 질량 500kg 이하의 배송 등 자율주행(원격제어 포함) 로봇과 관제장치의 조합을 대상으로 하며, 현재 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치의 8개 항목을 심사하고 신청일로부터 30일 이내에 처리한다.",
      "tag": "사실",
      "source_ids": [
        "ref-980"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "인증 대상은 로봇과 관제장치의 조합, 15km/h·500kg 이하. 심사 8개 항목(규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치). \"인증 신청일로부터 30일 이내\" (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f2",
      "claim": "개정 지능형로봇법과 도로교통법은 2023-11-17 시행됐으며, 질량 500kg·시속 15km 이하 실외이동로봇은 16가지 시험항목의 운행안전인증을 받아야 보도를 다닐 수 있게 됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-991",
        "ref-992"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "정책브리핑(2023-11-16, 산업통상자원부·경찰청): 시행일 2023-11-17, 인증 대상 500kg·15km/h 이하, 16가지 시험항목. 지디넷코리아(2023-07-28)도 16개 항목과 2023-11-17 시행을 적는다.",
      "as_of": "2023-11-16",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f3",
      "claim": "정책브리핑에 따르면 개정 도로교통법은 운행안전인증을 받은 실외이동로봇에 보행자 지위를 주어 보도 통행을 허용하되 신호위반·무단횡단 금지 등 보행자 의무를 지키게 하고 위반 시 운용자에게 범칙금 3만 원을 부과하며, 보도에서 운영하려는 자에게 보험 또는 공제 가입 의무를 지우고 한국로봇산업협회를 손해보장사업 실시기관으로 지정했다.",
      "tag": "사실",
      "source_ids": [
        "ref-991"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"운행안전인증을 받은 실외이동로봇에 보행자의 지위를 부여해 보도 통행을 허용\". 위반 시 운용자 범칙금 3만 원, 보험·공제 가입 의무, 한국로봇산업협회 손해보장사업 실시기관.",
      "as_of": "2023-11-16",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f4",
      "claim": "지디넷코리아(2023-07-28)가 전한 운행안전 기준안은 질량에 따라 최고 속도를 230kg 초과 5km/h, 100kg 초과~230kg 10km/h, 100kg 이하 15km/h로 나누고, 로봇 폭은 기본 80cm·보도 폭 250cm 이상이면 최대 120cm로 하며, 보험 보장액을 사망·후유장애 1억 5천만 원, 부상 3천만 원, 재물 피해 사고당 10억 원으로 정했다.",
      "tag": "사실",
      "source_ids": [
        "ref-992"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "산업통상자원부·한국로봇산업진흥원 발표 기사. 질량별 속도 상한 3단계, 폭 80cm(보도 250cm 이상 시 120cm), 보험 1.5억/3천만/10억 원. 경사로 안정성·장애물 회피·비상정지·횡단보도 신호 준수·알림음·등화장치·방수등급 포함.",
      "as_of": "2023-07-28",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f5",
      "claim": "2023년 시행 당시 16개였던 운행안전인증 시험항목이 현재 한국로봇산업진흥원 안내에는 8개 심사항목으로 적혀 있어 심사항목이 통폐합된 것으로 보이나, 개정 시점·근거 고시와 세부 기준이 완화됐는지는 이번 조사에서 원문으로 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-991",
        "ref-980"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "2023-11 정책브리핑은 16가지 시험항목, 2026-09-30 확인한 KIRIA 인증 안내는 8개 심사항목. 검색 요약에는 2025-11 고시 개정·16→8 통폐합 언급이 있으나 원문 미확인.",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f6",
      "claim": "일본은 2023-04-01 시행한 개정 도로교통법에서 최고 속도 6km/h 이하, 길이 120cm·폭 70cm·높이 120cm 이하의 자동배송 로봇 등을 원격 조작형 소형차(遠隔操作型小型車)로 정의해 보도·노측대를 보행자에 준하는 규칙으로 다니게 하고, 차체 표지 부착과 통행 장소를 관할하는 도도부현 공안위원회에 대한 사전 신고를 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-985"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "내각부 교통안전백서(令和5년) 토픽: 6km/h 이하·120×70×120cm, \"歩道や路側帯を通行することが原則\", 표지 부착, 공안위원회 사전 신고, 令和5年4月1日 시행.",
      "as_of": "2023",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f7",
      "claim": "Supply Chain Dive(2023-04-26)에 따르면 2022년 말까지 미국 최소 23개 주가 배송 로봇(개인 배송 장치, PDD) 법을 제정했으나 주마다 기준이 달라 조지아는 최대 500파운드·보도 4mph, 뉴햄프셔는 최대 80파운드·10mph를 허용하며, 이 차이는 가벼운 로봇을 쓰는 Starship 과 무거운 장치를 원한 Amazon·FedEx 가 각 주 입법에 준 영향에서 비롯됐다고 분석했다.",
      "tag": "사실",
      "source_ids": [
        "ref-986"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "At least 23 states by end of 2022. Georgia 500 lb·4 mph, New Hampshire 80 lb·10 mph. 캔자스 주지사는 2022년 최소 배상책임 조항 불명확을 이유로 법안을 거부했다.",
      "as_of": "2023-04-26",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f8",
      "claim": "Ottonomy CEO 는 미국 주별 배송 로봇 규정의 차이가 커서 모든 주를 같은 기준으로 맞추는 일이 악몽이 될 것이라고 평가했다.",
      "tag": "의견",
      "source_ids": [
        "ref-986"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Ottonomy CEO Ritukar Vijay: \"It is going to be a nightmare to get all the states on the same page\"",
      "as_of": "2023-04-26",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f9",
      "claim": "DC Velocity 에 따르면 Starship Technologies 는 2026-06-08 미국 대학 캠퍼스 운영을 종료하고 캠퍼스 로봇 1,200대 이상을 유럽·미국의 식료품 배송으로 옮긴다고 발표했으며, 식료품 시장이 더 크고 로봇이 개방된 도심 환경에서 안정적으로 운행한다는 점과 2018년부터의 캠퍼스 운영 경험을 이유로 들었다.",
      "tag": "사실",
      "source_ids": [
        "ref-981"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2026-06-08 발표. 미국 캠퍼스 운영 종료, 1,200대 이상 식료품 배송으로 재배치. 식료품 소매 파트너는 추후 발표 예정.",
      "as_of": "2026-06",
      "site_type": "실외",
      "flow_item": "수행 자원"
    },
    {
      "id": "f10",
      "claim": "Starship 은 핀란드에서 자사 로봇이 식료품 배송의 약 20%를 처리하고 일반 배달원보다 건당 3~4달러 싸게 배송하며 식료품 사업이 2년간 10배 성장 궤도에 있다고 주장한다.",
      "tag": "추정",
      "source_ids": [
        "ref-981"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 기사가 회사 발표를 옮김. 핀란드 식료품 배송의 약 20%, 건당 3~4달러 절감, 2년 10배 성장 궤도.",
      "as_of": "2026-06",
      "site_type": "실외",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f11",
      "claim": "우아한형제들은 배달로봇 딜리 신규 모델이 바퀴를 키워 낮은 연석을 넘고 경사로 주행이 나아졌으며 적재량이 2L 생수 6병에서 18병으로, 배터리 용량이 약 30% 늘었고 LED 깃대로 이면도로 시인성을 높였으며, 시범 운영에서 평균 배달 시간 약 30분과 응답자 90%의 재이용 의사를 얻었다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-983"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 회사 발표를 기사가 옮김. 연석·경사로 성능 향상, 적재 6→18병, 배터리 약 30% 증가, LED 깃대, 평균 배달 약 30분, 재이용 의사 90%.",
      "as_of": "2025-06-23",
      "site_type": "실외",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f12",
      "claim": "지디넷코리아(2025-06-23)에 따르면 배민 배달로봇 딜리 신규 모델은 2025-06-17 한국로봇산업진흥원의 실외이동로봇 운행안전인증을 받았고, 딜리는 2025년 2월부터 서울 강남구 논현동·역삼동에서 배민B마트 배달을 시범 운영했으며 신규 모델은 2025년 8월부터 현장에 투입될 예정이었다.",
      "tag": "사실",
      "source_ids": [
        "ref-983"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2025-06-17 운행안전인증 획득, 2월부터 논현·역삼 B마트 시범, 8월 투입 예정. 운영 관제 방식은 기사에 없음.",
      "as_of": "2025-06-23",
      "site_type": "실외",
      "flow_item": "시작 조건"
    },
    {
      "id": "f13",
      "claim": "스포츠경향(2026-09-02)에 따르면 뉴빌리티의 자율주행 로봇 뉴비는 덕수궁에서 주·야간 순찰과 화재·쓰러짐 같은 이상 상황 감지를 지원하고 서울숲·충남대학교병원·도쿄 시부야 등에서 운영되며, 5방향 카메라 영상으로 지도를 만들고 위치를 파악하는 V-SLAM 방식을 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-984"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "덕수궁 주·야간 순찰, 화재·쓰러짐 감지, 보행자 회피. 5방향 카메라 RGB 영상과 V-SLAM. 관제 방식은 기사에 없음.",
      "as_of": "2026-09-02",
      "site_type": "실외",
      "flow_item": "작업 대상"
    },
    {
      "id": "f14",
      "claim": "뉴빌리티는 2026년 상반기까지 국내외 150여 개 현장에서 로봇을 운영해 누적 14만 6,721km 이상을 주행했고 2025년 한 해 4만 4,638회 서비스를 수행했으며 연간 약 1억 4,500만 건의 데이터를 만든다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-984"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 회사 수치를 기사가 옮김. 150여 현장, 누적 146,721km, 2025년 44,638회, 연 약 1.45억 건 데이터.",
      "as_of": "2026-09-02",
      "site_type": "실외",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f15",
      "claim": "Pitt News(2019-10-21)에 따르면 피츠버그 포브스 애비뉴에서 길을 건너려 대기하던 Starship 배송로봇이 연석 경사로를 막아 휠체어 이용자가 차도에 갇히는 일이 생기자 피츠버그 대학이 몇 시간 만에 시험 운행을 멈췄고, Starship 은 로봇이 원래 경사로 뒤에서 기다리도록 설계됐으며 해당 교차로의 지도 오류 때문이라며 소프트웨어를 고치고 다른 교차로를 점검했다고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-987"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "curb ramp 를 막은 로봇, 대학 시험 중단(\"We have paused testing\"), 회사는 교차로 지도 오류로 설명하고 소프트웨어 갱신.",
      "as_of": "2019-10-21",
      "site_type": "실외",
      "flow_item": "예외·성과"
    },
    {
      "id": "f16",
      "claim": "Gehrke·Phair·Russo·Smaglik(Transportation Research Interdisciplinary Perspectives 18, 2023-03)은 노던애리조나대학 캠퍼스 10개 지점의 1주일 영상으로 보도 자율 배송로봇과 보행자·자전거 이용자의 상호작용을 침범 후 시간(PET) 대리 안전 지표로 분석하고, 상충 수준·지점 특성을 예측 요인으로 모형화해 공유 통로의 시설 관리 전략을 제시하려 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-990"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"one week of field-recorded video from ten locations across the Northern Arizona University campus\", post-encroachment time 사용. 초록 기준이며 상충 비율 수치는 초록에 없음.",
      "as_of": "2023-03",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f17",
      "claim": "Dobrosovestnova·Schwaninger·Weiss(RO-MAN 2022)는 에스토니아 탈린에서 상업 운영 중인 배송로봇이 겨울에 눈에 갇혔을 때 지나가던 사람들이 자발적으로 도와 운행을 이어 가게 한 사례를 관찰·자기민속지·온라인 콘텐츠 분석으로 연구하고, 사람의 도움이 현실적 완화책이 될 수 있지만 회사가 무급 행인의 도움에 운영을 기대서는 안 된다고 지적했다.",
      "tag": "사실",
      "source_ids": [
        "ref-993"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "탈린 겨울, 눈에 갇힌 배송로봇을 행인이 도움. 로봇이 귀엽고 도움이 된다는 인식이 도움 행동에 작용했을 수 있다고 봄. 윤리 문제 제기. 초록 기준.",
      "as_of": "2022",
      "site_type": "실외",
      "flow_item": "예외·성과"
    },
    {
      "id": "f18",
      "claim": "Tong·Simoni(arXiv 2507.12067, 2025-07; 2026-03 개정)는 보행자·장애물·날씨·혼잡 때문에 보도 배송로봇의 이동 시간이 크게 불확실하다고 보고 강건 최적화와 시뮬레이션을 결합한 경로 계획을 스톡홀름 도심 자료로 시험해, 타원 불확실성 집합과 분포 강건 최단경로(DRSP) 방법이 평균·최악 지연에서 가장 나았고 그 이점은 폭이 넓고 느린 로봇, 궂은 날씨·혼잡 조건에서 가장 컸다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-982"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "스톡홀름 도심 보행 흐름 자료. 예산형·타원·SVC 불확실성 집합과 DRSP 비교. \"The ellipsoidal and DRSP approaches outperform the other methods in terms of average and worst-case delay.\" 프리프린트.",
      "as_of": "2025-07-16",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f19",
      "claim": "연계 대상: Nav2 공식 튜토리얼은 실외 항법에 GPS 를 쓰되 일반 GPS 정확도가 좋은 조건에서 1~2m, 최대 10m이고 위치가 자주 튀며, RTK 는 약 1cm까지 줄이지만 기준국이 필요하고 도심·숲에서는 정확도가 더 떨어진다고 적으며, 바퀴 주행거리계·IMU·GPS 를 두 개의 확장 칼만 필터로 융합하고 위경도 목표점을 UTM 좌표로 바꾸며 사전 지도 없이 로봇을 따라 움직이는 전역 비용 지도(rolling costmap)를 쓰는 구성을 안내한다.",
      "tag": "사실",
      "source_ids": [
        "ref-988"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "GPS 정확도 \"1-2 meters under excellent conditions and up to 10 meters\", RTK 1cm·기준국 필요, 절대 방위 IMU 필요, EKF 2개(odom·map), navsat_transform, rolling costmap 권장.",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": "수행 자원"
    },
    {
      "id": "f20",
      "claim": "ISO/TC 204(지능형 교통 시스템)가 개발하는 ISO 4448 시리즈는 보도 등 공공 영역에서 보행자 곁을 다니는 공공 영역 이동로봇(PMR)을 다루며, 개요(Part 1) 외에 경로 계획 충분성(Part 6), 운행 데이터 기록기(Part 9), 안전·신뢰성(Part 16) 부분이 위원회 초안 단계로 준비되고 있다고 표준 책임자가 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-989"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Urban Robotics Foundation(Bern Grush, 2024-02-04 게시·2025-04-20 갱신): Part 1 개요, Part 6 journey planning sufficiency, Part 9 journey data recorder, Part 16 safety and reliability. 2024~2026 단계적 발행 예상.",
      "as_of": "2025-04-20",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f21",
      "claim": "ISO/TR 4448-1:2024 는 2024-08 발행된 기술 보고서로, 연석에서 사람·화물을 싣고 내리는 로봇 도로 차량과 보호받지 않는 보행자 사이에서 배송·점검·유지보수·감시 같은 일을 하는 로봇 장치의 배치 체계를 개관한다.",
      "tag": "사실",
      "source_ids": [
        "ref-994"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 결과 요약 기준: ISO/TR 4448-1:2024, 2024-08 발행, 공공 영역에서 배송·점검·유지보수·감시를 하는 로봇과 연석 승하차 로봇 차량 대상. 원문 미열람.",
      "as_of": "2024-08",
      "site_type": "실외",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "확인한 자료를 종합하면 66. 실외의 로봇 작업은 (1) 보도 배송 — 음식·장보기 물품을 매장에서 주문자 문 앞까지(f9·f12), (2) 순찰 — 궁궐·공원·역 주변·병원 부지의 주·야간 이상 감지(f13), (3) 캠퍼스 배송 — 대학 캠퍼스 음식 배달(f9·f15·f16)의 세 형태로 나타나며, 대표 업체가 2026년 캠퍼스에서 식료품·도심 배송으로 방향을 바꾼 점(f9)은 캠퍼스 모델이 실외 운영의 시험장 역할을 했음을 시사한다.",
      "tag": "추정",
      "source_ids": [
        "ref-981",
        "ref-983",
        "ref-984",
        "ref-987",
        "ref-990"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "딜리(강남 B마트), 뉴비(덕수궁·서울숲·시부야), Starship(미국 캠퍼스→식료품), NAU 캠퍼스 연구를 종합한 추정.",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": "작업 대상"
    },
    {
      "id": "f23",
      "claim": "확인한 자료를 종합하면 실외 로봇 작업의 여섯 항목은 시작 조건이 배달 앱·장보기 주문과 순찰 일정(f12·f13), 작업 대상이 음식·식료품과 순찰 구역·이상 상황·보행자(f9·f13), 수행 자원이 배송·순찰 로봇과 관제장치·원격 제어자, 때로 도움을 주는 행인(f1·f17), 제약이 인증·보행자 의무·속도·폭·보험과 관할별 크기·속도·신고 기준, 연석 경사로·좁은 보도·눈·위치 오차(f1~f7·f15·f18·f19), 완료·인계가 주문자 문 앞 전달(f12), 예외·성과가 눈 속 고립·접근성 사고와 운행 중단·배달 시간·비용(f10·f11·f15·f17)으로 채워질 수 있으나, 완료·인계의 확인 방식은 이번 자료에서 명시적으로 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-983",
        "ref-984",
        "ref-981",
        "ref-980",
        "ref-993",
        "ref-991",
        "ref-992",
        "ref-985",
        "ref-986",
        "ref-987",
        "ref-982",
        "ref-988"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1~f19 를 여섯 항목으로 재배열한 추정. 완료·인계(수령 확인) 근거 부족.",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "확인한 자료를 종합하면 날씨는 실외 로봇 운영에서 인증 요건(방수 성능, f1), 이동 시간 불확실성과 경로 선택(f18), 눈 속 고립과 사람 개입(f17)의 세 층위로 나타나므로, 운영 계층은 날씨·혼잡을 배정·경로의 제약과 예외 복구 조건으로 다뤄야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-980",
        "ref-982",
        "ref-993"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "방수 성능 심사항목, 궂은 날씨에서 강건 경로의 이점, 눈 속 고립 시 행인 도움과 그 윤리 문제를 종합한 추정.",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f25",
      "claim": "확인한 자료를 종합하면 66. 실외에서 ROP 가 직접 맡을 범위는 배달·장보기 주문과 순찰 일정을 받아 인증받은 로봇에 배정하고(f1·f12·f13), 관할마다 다른 속도·크기·보행자 의무·신고 조건과 날씨·혼잡을 경로·속도·운행 가능 구역 제약으로 반영하며(f2·f6·f7·f18·f24), 연석 경사로 같은 접근성 민감 지점의 대기 규칙을 지도 제약으로 관리하고(f15), 눈 속 고립·위치 오차 같은 예외를 원격 제어자·현장 인력에게 넘기는 일(f17·f19)이며, 제조사가 다른 실외 로봇을 한 계층에서 묶은 공개 사례는 이번 조사에서 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-980",
        "ref-983",
        "ref-984",
        "ref-991",
        "ref-985",
        "ref-986",
        "ref-982",
        "ref-987",
        "ref-993",
        "ref-988"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "인증 대상에 관제장치가 포함된 점(f1), 관할별 규정 차이(f6·f7), 경사로 대기 위치 지도 오류 사례(f15)를 근거로 한 추정.",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "연계 대상: 분류 원문 19장 기준으로 배달 앱·식료품 주문 시스템은 상위 업무 시스템, 로봇의 위치 추정(GPS·RTK·V-SLAM)·장애물 회피·연석 주행은 로봇 자체 지능·제어, 운행안전인증·도로교통법·일본 신고제·미국 주 PDD 법·보험은 업종별 조건에 속하므로, 이종 제조사를 잇는 ROP 는 이들에 작업 요청·상태 확인·제약 반영만 걸고 주행 안전 성능과 법적 인증 취득은 로봇 제조사·운영사에 맡겨야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-983",
        "ref-988",
        "ref-984",
        "ref-980",
        "ref-991",
        "ref-985",
        "ref-986"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 19장 경계에 f1·f3·f6·f7·f13·f19 를 대응시킨 추정.",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "이 영역은 보도 통행 규정·인증을 다루는 59. 법·규제·보험·라이선스와 50. 안전 표준·인증·사고 조사(f1~f7·f20·f21), 보행자·자전거와의 상충을 다루는 19. 사람·보행자 모델과 49. 사람 근접 안전(f15·f16), 위경도 좌표와 운행 구역을 다루는 15. 지도·공간·위치 모델과 16. 장소 의미·지도 관리(f15·f19), 날씨·혼잡 아래 경로를 다루는 27. 다중 로봇 경로·교통 관리 — MAPF 와 26. 작업 순서·스케줄링(f18), 눈 속 고립·원격 개입을 다루는 32. 예외 복구·재계획·업무 연속성과 31. 사람–로봇 협업(f17), 순찰 이상 감지를 다루는 38. 모니터링·이상 탐지·원인 분석(f13), 접근성을 다루는 60. 노동·수용성·접근성(f15), 배달 앱 연동을 다루는 23. 업무 시스템 연동(f12), 이기종 관제를 다루는 20. 로봇·제조사 관제 연동(f1·f25), 사업 전환을 다루는 1. 기술·시장·업체 동향과 3. 경제성·조달·사업 모델(f9·f10)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-980",
        "ref-991",
        "ref-985",
        "ref-986",
        "ref-989",
        "ref-994",
        "ref-987",
        "ref-990",
        "ref-988",
        "ref-982",
        "ref-993",
        "ref-984",
        "ref-983",
        "ref-981"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 finding 의 주제를 세부영역에 대응시킨 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "지능형로봇법 제40조의2에 따른 실외이동로봇 운행안전인증 안내. 대상(15km/h·500kg 이하, 로봇+관제장치), 8개 심사항목, 30일 처리 기간, 절차를 적는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-981",
      "org": "DC Velocity",
      "title": "Starship steers its delivery robots off college campuses and toward grocery sector",
      "published": "2026-06",
      "url": "https://www.dcvelocity.com/transportation/trucking/last-mile/starship-steers-its-delivery-robots-off-college-campuses-and-toward-grocery-sector",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Starship 이 2026-06-08 미국 대학 캠퍼스 운영을 종료하고 로봇 1,200대 이상을 식료품 배송으로 옮긴다는 발표 기사. 회사가 밝힌 핀란드 점유율·비용 절감 수치를 옮긴다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-982",
      "org": "Tong, X., & Simoni, M. D. (arXiv)",
      "title": "Robust Route Planning for Sidewalk Delivery Robots",
      "published": "2025-07-16",
      "url": "https://arxiv.org/abs/2507.12067",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "보행자·장애물·날씨·혼잡에 따른 이동 시간 불확실성을 강건 최적화와 시뮬레이션으로 다룬 보도 배송로봇 경로 계획 프리프린트(스톡홀름 자료). 2026-03 개정.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-983",
      "org": "지디넷코리아",
      "title": "배민, 차세대 배달로봇 ‘딜리’ 8월 투입…운행안전인증 획득",
      "published": "2025-06-23",
      "url": "https://zdnet.co.kr/view/?no=20250623095742",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "배민 배달로봇 딜리 신규 모델의 운행안전인증 획득(2025-06-17), 성능 개선(회사 발표), 강남 B마트 시범 운영과 8월 투입 계획을 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-984",
      "org": "스포츠경향",
      "title": "뉴빌리티, 덕수궁 순찰부터 도쿄 시내 배달까지",
      "published": "2026-09-02",
      "url": "https://sports.khan.co.kr/article/202609020605003/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "뉴빌리티 뉴비의 덕수궁·서울숲·충남대병원·도쿄 시부야 운영, 순찰 기능, 카메라 기반 V-SLAM, 회사가 밝힌 누적 운영 수치를 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-985",
      "org": "内閣府 (일본 내각부)",
      "title": "令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について",
      "published": "2023",
      "url": "https://www8.cao.go.jp/koutu//taisaku/r05kou_haku/zenbun/genkyo/topics/topic_1.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "2023-04-01 시행 일본 개정 도로교통법의 원격 조작형 소형차(6km/h·120×70×120cm, 보도 통행, 사전 신고)와 레벨4 특정 자동운행 허가제를 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-986",
      "org": "Supply Chain Dive",
      "title": "Why delivery robots face a regulatory ‘nightmare’",
      "published": "2023-04-26",
      "url": "https://www.supplychaindive.com/news/delivery-robot-bills-laws-proliferate-state-legislatures/648303/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "미국 23개 이상 주의 배송 로봇(PDD) 법이 무게·속도 기준에서 서로 다르고 업체들의 입법 영향이 그 차이를 낳았다는 분석 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-987",
      "org": "The Pitt News",
      "title": "Pitt pauses testing of Starship robots due to safety concerns",
      "published": "2019-10-21",
      "url": "https://pittnews.com/article/151679/news/pitt-pauses-testing-of-starship-robots-due-to-safety-concerns/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "연석 경사로를 막은 Starship 로봇 때문에 휠체어 이용자가 차도에 갇힌 사건과 피츠버그 대학의 시험 중단, 회사의 지도 오류 설명을 보도한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-988",
      "org": "Open Navigation (Nav2)",
      "title": "Navigating Using GPS Localization — Nav2 documentation",
      "published": null,
      "url": "https://docs.nav2.org/tutorials/docs/navigation2_with_gps.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Nav2 의 실외 GPS 항법 튜토리얼. GPS·RTK 정확도 한계, IMU 절대 방위, 두 EKF 융합, navsat_transform, rolling 전역 비용 지도를 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://docs.nav2.org/jazzy/tutorials/general_tutorials/navigation2_with_gps/navigation2_with_gps/",
      "source_unopened": false
    },
    {
      "id": "ref-989",
      "org": "Urban Robotics Foundation (Bern Grush)",
      "title": "ISO-4448 Update Winter 2024",
      "published": "2024-02-04",
      "url": "https://www.urbanroboticsfoundation.org/post/iso-4448-update-winter-2024",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ISO/TC 204 ISO 4448 시리즈(공공 영역 이동로봇)의 부분 구성과 진행 상황을 표준 책임자가 정리한 글(2025-04-20 갱신).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-990",
      "org": "Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18)",
      "title": "Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists",
      "published": "2023-03",
      "url": "https://doi.org/10.1016/j.trip.2023.100789",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "노던애리조나대학 캠퍼스 10개 지점 1주일 영상으로 보도 배송로봇–보행자·자전거 상호작용을 침범 후 시간으로 분석한 동료심사 논문. 초록만 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://experts.nau.edu/en/publications/observed-sidewalk-autonomous-delivery-robot-interactions-with-ped/",
      "source_unopened": false
    },
    {
      "id": "ref-991",
      "org": "대한민국 정책브리핑 (산업통상자원부·경찰청)",
      "title": "‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용",
      "published": "2023-11-16",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922726",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "2023-11-17 시행 개정 지능형로봇법·도로교통법에 따른 실외이동로봇의 보행자 지위, 16가지 시험항목 인증, 범칙금, 보험·공제 가입 의무를 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-992",
      "org": "지디넷코리아",
      "title": "실외 배달로봇 '시속 15km 이하로'...16가지 안전기준",
      "published": "2023-07-28",
      "url": "https://zdnet.co.kr/view/?no=20230728173101",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "산업통상자원부·한국로봇산업진흥원의 실외이동로봇 운행안전 기준 16개 항목, 질량별 속도 상한, 폭 기준, 보험 보장액을 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-993",
      "org": "Dobrosovestnova, A., Schwaninger, I., & Weiss, A. (IEEE RO-MAN 2022)",
      "title": "With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow",
      "published": "2022",
      "url": "https://ieeexplore.ieee.org/abstract/document/9900588/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "탈린에서 눈에 갇힌 상업 배송로봇을 행인이 돕는 현상을 다룬 학회 논문(pp. 1023–1029). 연구 포털의 초록만 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://researchportal.lih.lu/en/publications/with-a-little-help-of-humans-an-exploratory-study-of-delivery-rob/",
      "source_unopened": false
    },
    {
      "id": "ref-994",
      "org": "ISO",
      "title": "ISO/TR 4448-1:2024 Intelligent transport systems — Public-area mobile robots (PMR) — Part 1: Overview of paradigm",
      "published": "2024-08",
      "url": "https://www.iso.org/standard/81068.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. ISO/TC 204 의 공공 영역 이동로봇 배치 체계 개요 기술 보고서. 발행일·범위는 검색 결과 요약으로만 확인했다(ISO 페이지 403).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/site-type-applications/outdoor.md",
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
      "rationale": "섹션 3: f2·f3(2023-11 보도 통행 허용), f9(대표 업체의 캠퍼스 철수와 도심 전환), f15(접근성 사고) / 섹션 4: f3(보행자 지위), f6(원격 조작형 소형차), f7(PDD), f16(침범 후 시간), f19(RTK), f20·f21(PMR) / 섹션 5(현장 유형 모두 실외): 보도 배송 — f12(딜리), f11(벤더 주장); 순찰 — f13, f14(벤더 주장); 캠퍼스 — f9, f10(벤더 주장), f15, f16; 날씨 — f17; 작업 형태 f22, 여섯 항목 f23(완료·인계 근거 부족 명시) / 섹션 6: 위치 추정·센서 융합 f19(연계 대상 표시), 강건 경로 계획 f18, 날씨 대응 f24, 사람 도움·원격 개입 f17 / 섹션 7: 운행안전인증 f1·f2·f4·f5, 도로교통법 f3, 일본 f6, 미국 f7·f8, ISO 4448 f20·f21(원문 미열람), Nav2 f19 / 섹션 8: f16, f17, f18 / 섹션 9: f25(직접 범위), f26(연계 대상) / 섹션 10: f27 — 1, 3, 15, 16, 19, 20, 23, 26, 27, 31, 32, 38, 49, 50, 59, 60 / 섹션 11: open_questions_new 5건. f10·f11·f14 는 벤더 주장 병기 필수. 다음 실행 후보: 59. 법·규제·보험·라이선스 페이지에 f2~f7 반영, 19. 사람·보행자 모델 페이지에 f15·f16 반영, 50. 안전 표준·인증·사고 조사 페이지에 f20·f21 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "공공 영역 이동로봇",
      "term_en": "Public-area Mobile Robot (PMR)",
      "definition": "보도·연석 같은 공공 공간에서 보호받지 않는 보행자 곁을 다니며 배송·점검·감시 등을 하는 로봇으로, ISO/TC 204 의 ISO 4448 시리즈가 쓰는 용어다."
    },
    {
      "term_ko": "개인 배송 장치",
      "term_en": "Personal Delivery Device (PDD)",
      "definition": "미국 여러 주 법에서 보도·횡단보도를 다니며 물건을 나르는 배송 로봇을 가리키는 법적 범주로, 무게·속도 상한이 주마다 다르다."
    },
    {
      "term_ko": "원격 조작형 소형차",
      "term_en": "Remote-controlled Small Vehicle (遠隔操作型小型車)",
      "definition": "일본 개정 도로교통법(2023-04 시행)이 정한 최고 6km/h·120×70×120cm 이하의 자동배송 로봇 등의 범주로, 보도를 보행자에 준하는 규칙으로 다니며 공안위원회에 사전 신고해야 한다."
    },
    {
      "term_ko": "침범 후 시간",
      "term_en": "Post-Encroachment Time (PET)",
      "definition": "한 이동체가 충돌 가능 지점을 떠난 뒤 다른 이동체가 그 지점에 도착하기까지의 시간 차로, 실제 충돌 없이 상충의 심각도를 재는 대리 안전 지표다."
    }
  ],
  "open_questions_new": [
    "실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시는 무엇이며, 경사로·알림음·등화장치 같은 기존 항목은 어느 항목에 흡수됐는가? | 관련 영역: 66. 실외, 50. 안전 표준·인증·사고 조사, 59. 법·규제·보험·라이선스 | 근거: f5 | 종류: 일반",
    "운행안전인증 대상이 로봇과 관제장치의 조합인데, 제조사가 다른 실외 로봇을 하나의 오케스트레이션 계층에서 지시할 때 그 계층이 인증상 관제장치에 해당하는지, 재인증이 필요한지에 관한 기준이나 해석이 있는가? | 관련 영역: 66. 실외, 20. 로봇·제조사 관제 연동, 59. 법·규제·보험·라이선스 | 근거: f1 | 종류: 일반",
    "국내 보도에서 배송·순찰 로봇이 횡단 대기 중 연석 경사로·점자블록을 막지 않도록 하는 대기 위치 규칙이나 접근성 기준(인증 항목·지침)이 있는가? | 관련 영역: 66. 실외, 60. 노동·수용성·접근성, 16. 장소 의미·지도 관리 | 근거: f15 | 종류: 일반",
    "국내 실외 로봇 운영사는 강설·결빙·폭우 때 운행 중단·재개 기준과 고립 로봇 회수 절차를 어떻게 정하고 있으며, 그 기준이 공개된 자료가 있는가? | 관련 영역: 66. 실외, 32. 예외 복구·재계획·업무 연속성 | 근거: f24 | 종류: 일반",
    "나라·주마다 다른 보도 로봇 규정(속도·크기·신고·보행자 의무)을 경로·속도 제약으로 기계가 읽을 수 있게 표현하는 공통 모델이 있으며, ISO 4448 의 경로 계획 충분성·운행 데이터 기록기 부분이 이를 다루는가? | 관련 영역: 66. 실외, 21. 상호운용 표준·적합성, 16. 장소 의미·지도 관리 | 근거: f20 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 1,
    "unverified": [
      "f5 운행안전인증 심사항목 16→8 개정 시점·근거 고시 원문 미확인(검색 요약에만 2025-11 개정 언급)",
      "f6 일본 규정은 내각부 백서 단독, 경찰청 원문 PDF 는 본문 추출 실패",
      "f7 미국 주 PDD 법 개수(23개 이상)는 2023-04 기사 기준이며 이후 변화 미확인",
      "f10·f11·f14 는 회사 발표 수치(벤더 주장)이며 독립 확인 없음",
      "f16 NAU 연구의 상충 비율 수치는 초록에 없어 넣지 않음(ScienceDirect 403)",
      "f17 탈린 연구는 초록 기준, 운영 업체명 미확인",
      "f18 은 동료심사 전 프리프린트",
      "f21 ISO/TR 4448-1 은 원문 미열람(ISO 페이지 403), 검색 요약 범위만 사용",
      "뉴빌리티·딜리의 관제·원격 제어 방식과 수령 확인(완료·인계) 방식 미확인",
      "국내 실외 로봇의 강설·폭우 운영 기준 자료 미확인"
    ],
    "scope_violations": [
      "f19: GPS·RTK·센서 융합은 분류 원문 19장의 로봇 자체 지능·제어(센서 인식·위치 추정)이므로 '연계 대상: '으로 표시하고 위치 오차가 운영 제약이 되는 근거로만 제안함",
      "f13: V-SLAM 위치 추정 언급은 로봇 자체 지능·제어이며 순찰 사례의 설명으로만 씀",
      "f26: 배달 앱, 로봇 주행·위치 추정, 인증·법령·보험은 상위 업무 시스템·로봇 자체 지능·제어·업종별 조건이므로 '연계 대상: '으로 표시함",
      "f2~f7: 법령·인증 내용은 59. 법·규제·보험·라이선스와 겹치므로 이 영역에서는 실외 운영의 제약 근거로만 제안함"
    ],
    "budget_used": {
      "queries": 16,
      "sources": 15
    },
    "limits": "재실행 1회차. 반려 사유 1(스키마 불일치: f11 이 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시 없음): 이전 반환값(runs/2026-09-30-01/research.json)이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로, 같은 대상·예산 안에서 조사를 다시 해 전체 브리프를 새로 만들었다. 이번 브리프의 회사 성능·실적 주장(f10 Starship, f11 배민 딜리, f14 뉴빌리티)은 모두 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈고, 벤더 문서 유형 출처만 근거로 한 [사실] finding 은 없다(관련 finding: f10, f11, f14). 이전 실행과 finding·출처 번호가 다를 수 있다. web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-980~ref-994, 예약 구간 안)로 출처 상한에 도달해 Knightscope 등 해외 순찰 사례, 공원·골프장 등 다른 실외 작업, 한국 강설 운영 기준은 조사하지 못했다. 원문 열람: 14건 webfetch(논문 2건은 초록 페이지), 1건 미열람(ref-994 ISO 403). 열지 못해 쓰지 않은 것: 경찰청 PDF(본문 추출 실패), MDPI 피츠버그 파일럿 논문·ACM 논문·ScienceDirect(403), 한국로봇학회지 RTK 논문(PDF 손상). 교차 확인 1건(f2: 정책브리핑·지디넷코리아). 신뢰도 high finding 1건(f2). 분류 원문 핵심 질문(보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가)에는 작업 형태 f22, 여섯 항목 f23, 날씨 f24, 직접 범위 f25, 연계 대상 f26 으로 답했으며, 결론은 '보도 운영은 관할마다 다른 인증·보행자 의무·속도·크기 조건 위에서 이루어지고, 날씨·보행자·접근성 민감 지점이 경로·대기·예외 처리의 제약이 되며, 제조사가 다른 실외 로봇을 한 계층에서 묶은 공개 사례는 확인되지 않았다'는 추정이다. 현장 유형은 f27(연결)을 빼고 모두 실외이며 캠퍼스·궁궐·공원·도심 보도 사례다. 이 영역의 성격상 다른 현장 유형 사례는 찾지 않았다. 국내 자료는 한국로봇산업진흥원·정책브리핑·지디넷코리아 2건·스포츠경향 다섯 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다(f18 의 시뮬레이션은 경로 계획 평가용으로 26·27 쪽에만 연결). 용어집에 이미 있는 실외이동로봇 운행안전인증·원격 조작·비용 지도는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음, 해결된 열린 질문 없음."
  }
}
```

### runs/2026-09-30-01/verification.json

```json
{
  "run_id": "2026-09-30-01",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-980(KIRIA 인증 안내)을 열어 제40조의2, 15km/h·500kg 이하, 로봇+관제장치 조합, 8개 심사항목, 30일 이내 처리를 확인했다. 페이지에 발행일·갱신일이 없어 기준일은 확인일 2026-09-30이다. 15km/h·500kg는 ref-991과도 일치하지만 8개 항목은 KIRIA 단독 출처다. 2023 시행 당시 16개 항목(f2)과 충돌하므로 둘 다 제시해야 한다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인: ref-991(정책브리핑 2023-11-16)과 ref-992(지디넷코리아 2023-07-28) 모두 2023-11-17 시행, 500kg·15km/h, 16개 항목을 적는다. 두 출처 모두 정부 발표에서 나왔으므로 독립성은 제한적이다. 인증 대상 기준은 ref-980으로도 확인했다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-991에서 보행자 지위 부여, 운용자 범칙금 3만 원, 보험·공제 가입 의무, 한국로봇산업협회의 손해보장사업 실시기관 지정을 확인했다. 단일 정부 출처다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-992에서 질량별 속도 3단계, 폭 80cm(보도 250cm 이상이면 120cm), 보험 1.5억/3천만/10억 원을 확인했다. 2023-07 시행 전 보도의 기준안이므로 최종 고시 반영 여부는 미확인이다. 페이지에 '2023-07 보도 기준안'임을 밝혀야 한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정]이 적정하다. ref-991(16개)과 ref-980(8개)의 차이는 두 출처에서 확인되지만, 개정 시점·근거 고시는 원문으로 확인되지 않았다. 검색 요약의 '2025-11 고시 개정'은 본문에 쓰지 않는다. 열린 질문 1과 짝을 이룬다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-985(내각부 교통안전백서 令和5년)에서 6km/h 이하, 120×70×120cm, 보도·노측대 통행 원칙, 표지 부착, 도도부현 공안위원회 사전 신고, 令和5年4月1日 시행을 확인했다. 단일 정부 출처다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-986(2023-04-26)에서 2022년 말까지 최소 23개 주, 조지아 500lb·4mph, 뉴햄프셔 80lb·10mph, Starship(2017~18)과 Amazon·FedEx(2019~20)의 입법 영향을 확인했다. 기사 단독이며 2023-04 기준이므로 이후 변화는 미확인이다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-986에서 Ottonomy CEO Ritukar Vijay의 'nightmare' 발언을 확인했다. [의견]의 주체(Ottonomy CEO)를 밝혀 둔다. ref-986의 직접 인용은 이것 하나다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-981(DC Velocity, 2026-06-08)에서 캠퍼스 운영 축소·종료(wind down), 1,200대 이상 식료품 배송 전환, 2018년 캠퍼스 운영 시작, 개방된 도심 환경 운영 역량을 이유로 든 점을 확인했다. 브리프의 발행일 '2026-06'은 2026-06-08로 좁힐 수 있다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정] 벤더 주장 표시가 적정하다. ref-981에 약 20%, 건당 3~4달러 절감이 있다. 다만 '10배 성장'은 원문이 앞으로 2년의 예상(projects)이므로 '성장 궤도에 있다'는 과장이다. 문구 수정을 지시한다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-983에서 바퀴 확대·연석, 경사로, 6→18병, 배터리 약 30%, LED 깃대, 평균 약 30분, 재이용 의사 90%를 확인했다. 회사 발표이므로 [추정] 벤더 주장 표시가 적정하다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-983에서 2025-06-17 인증 획득, 2월부터 논현·역삼 시범 운영, 8월 투입 예정을 확인했다. 배민B마트 배달 맥락도 같다. 문 앞 전달·수령 확인 방식은 기사에 없다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-984(2026-09-02)에서 덕수궁 주·야간 순찰, 화재·쓰러짐 감지, 서울숲·충남대병원·시부야 운영, 5방향 카메라 RGB와 V-SLAM을 확인했다. V-SLAM은 로봇 자체 지능·제어이므로 연계 대상으로만 짧게 쓴다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-984에서 150여 현장, 146,721km, 2025년 44,638회, 연 약 1.45억 건을 확인했다. 회사 수치이므로 [추정] 벤더 주장 표시가 적정하다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-987(2019-10-21)에서 포브스 애비뉴, 연석 경사로 봉쇄, 대학의 시험 중단, 교차로 지도 오류 설명, 다른 교차로 점검을 확인했다. 원문은 '트위터 게시 후 두 시간이 채 안 돼' 중단했다고 적으므로 '몇 시간 만에'는 고쳐야 한다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: NAU 연구 포털(fetch_url)에서 저자, TRIP 18(2023-03), DOI, 10개 지점 1주일 영상, PET 모형화, 시설 관리 전략 목표를 확인했다. 초록 기준이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: LIH 연구 포털(fetch_url)에서 RO-MAN 2022, 탈린 겨울, 관찰·자기민속지·온라인 콘텐츠 분석, 사람 도움이 합리적 완화책이라는 점, 무급 행인 도움에 기대는 사업 모델의 윤리 문제를 확인했다. 초록 기준이며 운영 업체명은 미확인이다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록 페이지(2025-07-16 제출, 2026-03-27 개정)에서 불확실성 원인, 예산형·타원·SVC 집합과 DRSP, 스톡홀름 자료, 타원·DRSP의 평균·최악 지연 우위, 넓고 느린 로봇·궂은 날씨·혼잡에서 이점이 가장 크다는 결과를 확인했다. 동료심사 전 프리프린트임을 밝혀야 한다. 인용 구절이 원문과 글자 단위로 같은지는 확인하지 못했으므로 페이지에서는 재서술한다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 브리프의 url(docs.nav2.org/tutorials/docs/navigation2_with_gps.html)은 HTTP 404이고, fetch_url(jazzy 경로)에서 원문을 확인했다. 일반 GPS 1~2m·최대 10m와 위치 튐, RTK 1cm·기준국 필요, ENU 절대 방위 IMU, EKF 2개(odom·map), navsat_transform의 UTM 변환, 사전 지도 없는 rolling 전역 비용 지도를 확인했다. '도심·숲에서 정확도가 더 떨어진다'는 원문에서 확인하지 못해 삭제를 지시한다. '연계 대상' 표시는 적정하다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-989(Bern Grush, 2024-02-04 게시, 2025-04-20 갱신)에서 PMR 범위와 Part 1·6·9·16 구성을 확인했다. 원문은 Part 6·9·16을 'Committee Draft submission pending'(위원회 초안 제출 대기)으로 적는다. '위원회 초안 단계로 준비되고 있다'는 한 단계 앞선 표현이므로 고쳐야 한다. 출처는 발행 기관(ISO)이 아니라 표준 책임자의 업계 글이며, 현재 진행 상태는 미확인이다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(ISO 페이지 403). 검색 결과 일치로 대신했다. ISO·SIS·ANSI 결과에서 제목, 2024-08 발행(1판), 연석 승하차 로봇 도로 차량과 보호받지 않는 보행자 사이의 배송·점검·유지보수·감시 로봇 범위를 확인했다. 드론은 범위 밖이다. 신뢰도 medium이 상한이다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 종합이다. '순찰 — 궁궐·공원·역 주변·병원 부지'의 '역 주변'은 어느 출처에도 없다. ref-984는 순찰을 덕수궁에 대해서만 적고 서울숲·충남대병원·시부야는 운영 장소로만 적으므로 수정을 지시한다. '캠퍼스가 시험장 역할'은 ref-981에 실린 Starship CEO 발언과 맞는다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 종합이다. 완료·인계 칸의 '주문자 문 앞 전달(f12)'은 f12·ref-983에 근거가 없다. finding 스스로도 확인 방식이 미확인이라고 적었으므로 이 칸은 '미확인'으로 두게 한다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정] 종합이다. 방수 성능(ref-980), 궂은 날씨의 강건 경로 이점(ref-982), 눈 속 고립(ref-993)이 각각 확인됐다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정] 종합이다. 원문 19장 경계와 맞고, 근거 finding들이 살아 있다. 이기종 실외 로봇 통합 사례는 미확인이라고 밝힌 점도 적정하다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정] 종합이다. 원문 19장의 상위 업무 시스템·로봇 자체 지능·제어·업종별 조건에 맞게 '연계 대상'으로 표시됐다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정] 연결 목록이다. 16개 세부영역이 모두 번호와 원문 명칭으로 표기됐다."
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
      "f2·f3(개정 지능형로봇법·도로교통법, 16개 시험항목)는 실행 2026-09-29-17 브리프 f10(ref-967 AI타임스)과 같은 사실이다. 65. 가정·공동주택 페이지의 '16개 시험항목' 서술은 이번 f1(현재 KIRIA 안내 8개 심사항목)과 기준일이 다른 채 충돌할 수 있다.",
      "f1(8개 심사항목, 확인일 2026-09-30)과 f2(16개 시험항목, 2023-11-16)는 서로 충돌한다. f5와 열린 질문 1로 처리하되, 본문에서는 둘 다 기준일과 함께 제시한다."
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "용어집 '실외이동로봇 운행안전인증'(outdoor-mobile-robot-operational-safety-certification)은 2026-09-29-17 후보 정의에서 '16개 시험항목'을 기준일 없이 적었다. 현재 KIRIA 안내는 8개 심사항목이다(f1·f2·f5)."
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "ref-988: 각주 정의와 reference_updates의 URL을 https://docs.nav2.org/jazzy/tutorials/general_tutorials/navigation2_with_gps/navigation2_with_gps/ 로 바꾼다. 브리프의 url(…/tutorials/docs/navigation2_with_gps.html)은 2026-09-30 확인 때 HTTP 404였다.",
    "f19: '도심·숲에서는 정확도가 더 떨어진다' 구절을 본문에서 뺀다. Nav2 원문에서 확인되지 않았다. 나머지(GPS 1~2m·최대 10m, RTK 약 1cm·기준국, EKF 2개, navsat_transform, rolling 전역 비용 지도)는 '연계 대상'으로 짧게 유지한다.",
    "f20: '위원회 초안 단계로 준비되고 있다'를 'Part 6·9·16은 위원회 초안(CD) 제출을 앞두고 있다고 표준 책임자가 밝혔다(2024-02-04 게시, 2025-04-20 갱신 기준, 이후 진행 상태 미확인)'로 고친다. 원문 표기는 'Committee Draft submission pending'이다.",
    "f15: '몇 시간 만에'를 '문제 제기가 트위터에 올라온 뒤 두 시간이 채 안 돼'로 고친다. ref-987 원문 표현에 맞춘다.",
    "f10: '식료품 사업이 2년간 10배 성장 궤도에 있다'를 '앞으로 2년간 식료품 사업이 10배 성장할 것으로 예상한다'로 고친다. [추정]과 '벤더 주장' 병기는 유지한다. 원문은 예상(projects)이다.",
    "f9·f10: ref-981의 발행일을 2026-06-08로 적는다. 기사와 발표 날짜가 같다.",
    "f22: '역 주변'을 삭제하고, 순찰 형태의 예는 덕수궁(f13)으로 한정한다. 서울숲·충남대학교병원·도쿄 시부야는 작업 형태를 붙이지 않은 운영 장소로만 쓴다. ref-984는 이들 장소의 작업을 순찰로 특정하지 않는다.",
    "f23: 5절 여섯 항목 정리에서 완료·인계 칸의 '주문자 문 앞 전달(f12)'을 빼고 '미확인(이번 자료에 수령 확인 방식 없음)'으로 둔다. site_matrix_updates에는 완료·인계 칸을 넣지 않는다. f12·ref-983에 문 앞 전달·수령 확인 근거가 없다.",
    "f1·f2·f5: 7절에서 운행안전인증 항목 수는 한쪽을 고르지 않고 '2023-11 시행 당시 16개 시험항목(f2, 기준일 2023-11-16)'과 '2026-09-30 확인한 KIRIA 안내 8개 심사항목(f1)'을 모두 기준일과 함께 제시한다. 차이의 원인은 [추정](f5)으로만 쓰고 열린 질문 1로 연결한다.",
    "f4: 질량별 속도·폭·보험 보장액을 '2023-07 지디넷코리아가 전한 시행 전 기준안'으로 밝히고, 최종 고시 반영 여부는 미확인이라고 적는다.",
    "f13: V-SLAM·5방향 카메라 위치 추정은 로봇 자체 지능·제어(원문 19장)이므로 '연계 대상'으로 한 문장 이내로 다룬다. ROP가 맡는 기능처럼 쓰지 않는다.",
    "f18: 8절과 6절에서 ref-982가 동료심사 전 arXiv 프리프린트(2025-07-16 제출, 2026-03-27 개정)임을 밝힌다. 결과 문장은 직접 인용하지 않고 재서술한다.",
    "f16·f17: 8절에서 ref-990·ref-993은 초록 기준으로 확인했음을 밝히고, 초록에 없는 수치(상충 비율 등)는 쓰지 않는다.",
    "ref-994(f21): 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 항목에 source_unopened: true를 넣는다. 본문은 검색 결과 요약 범위(2024-08 발행 기술 보고서, 공공 영역 배송·점검·유지보수·감시 로봇과 연석 승하차 로봇 차량 대상)를 넘지 않는다.",
    "용어집: docs/glossary/outdoor-mobile-robot-operational-safety-certification.md 정의가 심사항목 수를 기준일 없이 '16개'로만 적고 있으면, glossary_updates(action: update)로 '2023-11 시행 당시 16개 시험항목(f2), 2026-09-30 확인한 한국로봇산업진흥원 안내 8개 심사항목(f1)'과 두 기준일을 병기한다.",
    "f8: [의견]의 주체를 'Ottonomy CEO Ritukar Vijay(ref-986 기사 인용)'로 밝힌다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 27건, 미확인 0건, 교차 확인 1건(f2: 정책브리핑·지디넷코리아. 둘 다 정부 발표에서 나와 독립성은 제한적이다). 강등: 없음. 수정 지시는 f10·f15·f19·f20·f22·f23의 문구 수정과 ref-988 URL 교체(원 URL 404)다. 원문 미열람 출처: ref-994(ISO/TR 4448-1, ISO 페이지 403. 검색 결과 일치로 확인). 주의: 운행안전인증 항목 수는 2023 시행 당시 16개 시험항목(정책브리핑)과 현재 한국로봇산업진흥원 안내 8개 심사항목이 달라 두 값을 기준일과 함께 제시한다. 개정 시점은 열린 질문으로 남긴다. 사실 주장 대부분이 단일 출처이고, 기업 성과 수치(f10 Starship, f11 배민 딜리, f14 뉴빌리티)는 벤더 주장이다. f18은 프리프린트이고, f16·f17은 초록 기준이다. 2026-09-29-17 브리프가 쓴 '16개 시험항목' 서술(65. 가정·공동주택)과 용어집 정의의 기준일 병기가 필요하다. 5. 적용 사례의 완료·인계(수령 확인) 방식은 미확인이다. 제조사가 다른 실외 로봇을 한 계층에서 묶은 공개 사례는 확인되지 않았다. 검증 검색 1회(리서치 16회 포함 누계 17/30), 열람 14회. 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-09-30-01/pages.json

```json
{
  "run_id": "2026-09-30-01",
  "outline": [
    {
      "path": "docs/categories/site-type-applications/outdoor.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "한국에서는 2023-11-17 개정 지능형로봇법·도로교통법 시행으로 운행안전인증을 받은 실외이동로봇이 보행자 지위를 얻어 보도를 다닐 수 있게 됐고, 보도 운영은 인증·보행자 의무·보험 조건 위에서 이루어진다. [사실][^ref-991]",
      "planned_findings": [
        "f2",
        "f3",
        "f6",
        "f7",
        "f9",
        "f15",
        "f25"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/outdoor.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "실외이동로봇 운행안전인증, 보행자 지위, 원격 조작형 소형차, 개인 배송 장치(PDD), 공공 영역 이동로봇(PMR), RTK, 침범 후 시간(PET)을 정리한다. [사실][^ref-980]",
      "planned_findings": [
        "f1",
        "f3",
        "f6",
        "f7",
        "f16",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/outdoor.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2200,
      "summary": "확인한 자료에서 실외 로봇 작업은 보도 배송, 순찰, 캠퍼스 배송의 세 형태로 나타나며 세 사례를 여섯 항목으로 정리하되 완료·인계는 미확인으로 둔다. [추정][^ref-983]",
      "planned_findings": [
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f22",
        "f23"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/outdoor.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1500,
      "summary": "위치 추정은 연계 대상이고, 운영 계층은 불확실성을 고려한 경로 계획, 날씨의 제약·예외 처리, 사람 도움·원격 개입, 접근성 민감 지점 대기 규칙을 다룬다. [추정][^ref-982]",
      "planned_findings": [
        "f13",
        "f15",
        "f17",
        "f18",
        "f19",
        "f24",
        "f25"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/outdoor.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1700,
      "summary": "실외 로봇의 운영 기준은 한국 운행안전인증, 나라·주마다 다른 보도 통행 법규, 개발 중인 ISO 4448 시리즈로 이루어지며 인증 항목 수는 두 기준일의 값을 함께 제시한다. [추정][^ref-980]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f19",
        "f20",
        "f21"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/outdoor.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 900,
      "summary": "연구는 보도 로봇–보행자 상호작용 관측, 눈 속 고립과 사람 개입, 불확실성 아래 경로 계획에 모여 있다. [추정][^ref-990]",
      "planned_findings": [
        "f15",
        "f16",
        "f17",
        "f18",
        "f20"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/outdoor.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 900,
      "summary": "ROP는 요청 수신·배정, 관할 규정·날씨의 제약 반영, 예외 인계를 맡고 배달 앱·로봇 주행·법적 인증은 연계 대상으로 둔다. [추정][^ref-980]",
      "planned_findings": [
        "f1",
        "f25",
        "f26"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/outdoor.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 900,
      "summary": "법규·안전, 보행자, 지도·위치, 경로·스케줄링, 예외 복구, 관제·연동, 사업 동향의 16개 세부영역과 이어진다. [추정][^ref-980]",
      "planned_findings": [
        "f27"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/outdoor.md",
      "section": "11. 열린 질문",
      "budget_chars": 700,
      "summary": "인증 항목 개정, 관제장치 해당 여부, 접근성 대기 규칙, 강설·폭우 운영 기준, 관할 규정의 기계 판독 모델 다섯 질문을 연다.",
      "planned_findings": [
        "f1",
        "f5",
        "f15",
        "f20",
        "f24"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/site-type-applications/outdoor.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "섹션 3~11 신규 작성(seed → draft): 현장 유형 실외 사례 3건(보도 배송 딜리, 덕수궁 순찰 뉴비, 피츠버그 캠퍼스 배송 Starship)을 여섯 항목으로 정리, 위치 추정(연계 대상)·강건 경로 계획·날씨·사람 도움, 운행안전인증 항목 수 두 기준일 병기, 한국·일본·미국 보도 규정, ISO 4448, 책임 경계, 연결 영역 16개, 열린 질문 5건, 각주 15건"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area66-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 66. 실외 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,761자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area66-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 66. 실외 의 \"6. 대표 접근법과 기술\" 절(1,280자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area66-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 66. 실외 의 \"8. 대표 연구와 자료\" 절(1,110자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area66-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 66. 실외 의 \"4. 핵심 개념과 용어\" 절(909자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area66-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 66. 실외 의 \"11. 열린 질문\" 절(816자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area66-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 66. 실외 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(780자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area66-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 66. 실외 의 \"3. 왜 중요한가\" 절(683자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 66. 실외 | 섹션 3~11 신규 작성(seed → draft): 실외 사례 3건 여섯 항목 정리, 운행안전인증 항목 수 두 기준일 병기, 한국·일본·미국 보도 규정, ISO 4448, 책임 경계, 연결 영역 16개, 열린 질문 5건, 1차 수정 지시 16건 이행 | run 2026-09-30-01",
  "index_updates": {
    "home_recent": "2026-09-30 — 66. 실외: 보도 배송(딜리)·덕수궁 순찰(뉴비)·캠퍼스 배송(Starship) 사례와 한국 운행안전인증·일본·미국 보도 규정, 날씨·위치 오차를 다루는 운영 방법을 정리했다",
    "category_recent": "2026-09-30 — 66. 실외: 섹션 3~11 신규 작성(seed → draft), 실외 사례 3건 여섯 항목 정리, 운행안전인증 항목 수(2023 시행 16개·2026-09-30 확인 8개) 병기, 열린 질문 5건",
    "area_recent": "2026-09-30 — 66. 실외: 섹션 3~11 신규 작성, 각주 15건(ref-980~ref-994), 신뢰도 medium"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "public-area-mobile-robot",
      "term_ko": "공공 영역 이동로봇",
      "term_en": "Public-area Mobile Robot (PMR)",
      "definition": "보도·연석 같은 공공 공간에서 보호받지 않는 보행자 곁을 다니며 배송·점검·감시 등을 하는 로봇으로, ISO/TC 204 의 ISO 4448 시리즈가 쓰는 용어다.",
      "related_areas": [
        66,
        50
      ],
      "sources": [
        "ref-989",
        "ref-994"
      ]
    },
    {
      "action": "new",
      "slug": "personal-delivery-device",
      "term_ko": "개인 배송 장치",
      "term_en": "Personal Delivery Device (PDD)",
      "definition": "미국 여러 주 법에서 보도·횡단보도를 다니며 물건을 나르는 배송 로봇을 가리키는 법적 범주로, 무게·속도 상한이 주마다 다르다.",
      "description": "2023-04 기사 기준 2022년 말까지 최소 23개 주가 관련 법을 제정했으며, 조지아는 최대 500파운드·보도 4mph, 뉴햄프셔는 최대 80파운드·10mph를 허용한다.",
      "related_areas": [
        66,
        59
      ],
      "sources": [
        "ref-986"
      ]
    },
    {
      "action": "new",
      "slug": "remote-controlled-small-vehicle",
      "term_ko": "원격 조작형 소형차",
      "term_en": "Remote-controlled Small Vehicle (遠隔操作型小型車)",
      "definition": "일본 개정 도로교통법(2023-04 시행)이 정한 최고 6km/h·120×70×120cm 이하의 자동배송 로봇 등의 범주로, 보도를 보행자에 준하는 규칙으로 다니며 공안위원회에 사전 신고해야 한다.",
      "related_areas": [
        66,
        59
      ],
      "sources": [
        "ref-985"
      ]
    },
    {
      "action": "new",
      "slug": "post-encroachment-time",
      "term_ko": "침범 후 시간",
      "term_en": "Post-Encroachment Time (PET)",
      "definition": "한 이동체가 충돌 가능 지점을 떠난 뒤 다른 이동체가 그 지점에 도착하기까지의 시간 차로, 실제 충돌 없이 상충의 심각도를 재는 대리 안전 지표다.",
      "description": "보도 자율 배송로봇과 보행자·자전거 이용자의 상호작용 분석에 쓰였다.",
      "related_areas": [
        66,
        19,
        49
      ],
      "sources": [
        "ref-990"
      ]
    },
    {
      "action": "update",
      "slug": "outdoor-mobile-robot-operational-safety-certification",
      "term_ko": "실외이동로봇 운행안전인증",
      "term_en": "Outdoor Mobile Robot Operational Safety Certification",
      "definition": "지능형로봇법 제40조의2에 따라 최대 속도 15km/h·최대 질량 500kg 이하의 배송 등 자율주행(원격제어 포함) 로봇과 관제장치의 조합이 보도를 다니려면 받아야 하는 의무인증이다.",
      "description": "심사항목 수는 2023-11 시행 당시 16개 시험항목(기준일 2023-11-16, 정책브리핑·지디넷코리아)이었고, 2026-09-30 확인한 한국로봇산업진흥원 안내에는 8개 심사항목(규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치)으로 적혀 있다. 변경 시점과 근거 고시는 미확인이다.",
      "related_areas": [
        66,
        50,
        59,
        65
      ],
      "sources": [
        "ref-980",
        "ref-991",
        "ref-992"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "지능형로봇법 제40조의2에 따른 실외이동로봇 운행안전인증 안내. 대상(15km/h·500kg 이하, 로봇+관제장치), 8개 심사항목, 30일 처리 기간, 절차를 적는다.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-981",
      "org": "DC Velocity",
      "title": "Starship steers its delivery robots off college campuses and toward grocery sector",
      "published": "2026-06-08",
      "url": "https://www.dcvelocity.com/transportation/trucking/last-mile/starship-steers-its-delivery-robots-off-college-campuses-and-toward-grocery-sector",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Starship 이 2026-06-08 미국 대학 캠퍼스 운영을 종료하고 로봇 1,200대 이상을 식료품 배송으로 옮긴다는 발표 기사. 회사가 밝힌 핀란드 점유율·비용 절감 수치와 2년 성장 예상을 옮긴다.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-982",
      "org": "Tong, X., & Simoni, M. D. (arXiv)",
      "title": "Robust Route Planning for Sidewalk Delivery Robots",
      "published": "2025-07-16",
      "url": "https://arxiv.org/abs/2507.12067",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "보행자·장애물·날씨·혼잡에 따른 이동 시간 불확실성을 강건 최적화와 시뮬레이션으로 다룬 보도 배송로봇 경로 계획 프리프린트(스톡홀름 자료). 2026-03-27 개정, 동료심사 전.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-983",
      "org": "지디넷코리아",
      "title": "배민, 차세대 배달로봇 ‘딜리’ 8월 투입…운행안전인증 획득",
      "published": "2025-06-23",
      "url": "https://zdnet.co.kr/view/?no=20250623095742",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "배민 배달로봇 딜리 신규 모델의 운행안전인증 획득(2025-06-17), 성능 개선(회사 발표), 강남 B마트 시범 운영과 8월 투입 계획을 전한다.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-984",
      "org": "스포츠경향",
      "title": "뉴빌리티, 덕수궁 순찰부터 도쿄 시내 배달까지",
      "published": "2026-09-02",
      "url": "https://sports.khan.co.kr/article/202609020605003/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "뉴빌리티 뉴비의 덕수궁·서울숲·충남대병원·도쿄 시부야 운영, 덕수궁 순찰 기능, 카메라 기반 V-SLAM, 회사가 밝힌 누적 운영 수치를 전한다.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-985",
      "org": "内閣府 (일본 내각부)",
      "title": "令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について",
      "published": "2023",
      "url": "https://www8.cao.go.jp/koutu//taisaku/r05kou_haku/zenbun/genkyo/topics/topic_1.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "2023-04-01 시행 일본 개정 도로교통법의 원격 조작형 소형차(6km/h·120×70×120cm, 보도 통행, 사전 신고)와 레벨4 특정 자동운행 허가제를 설명한다.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-986",
      "org": "Supply Chain Dive",
      "title": "Why delivery robots face a regulatory ‘nightmare’",
      "published": "2023-04-26",
      "url": "https://www.supplychaindive.com/news/delivery-robot-bills-laws-proliferate-state-legislatures/648303/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "미국 23개 이상 주의 배송 로봇(PDD) 법이 무게·속도 기준에서 서로 다르고 업체들의 입법 영향이 그 차이를 낳았다는 분석 기사.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-987",
      "org": "The Pitt News",
      "title": "Pitt pauses testing of Starship robots due to safety concerns",
      "published": "2019-10-21",
      "url": "https://pittnews.com/article/151679/news/pitt-pauses-testing-of-starship-robots-due-to-safety-concerns/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "연석 경사로를 막은 Starship 로봇 때문에 휠체어 이용자가 차도에 갇힌 사건과 피츠버그 대학의 시험 중단, 회사의 지도 오류 설명을 보도한다.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-988",
      "org": "Open Navigation (Nav2)",
      "title": "Navigating Using GPS Localization — Nav2 documentation",
      "published": null,
      "url": "https://docs.nav2.org/jazzy/tutorials/general_tutorials/navigation2_with_gps/navigation2_with_gps/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Nav2 의 실외 GPS 항법 튜토리얼. GPS·RTK 정확도 한계, IMU 절대 방위, 두 EKF 융합, navsat_transform, rolling 전역 비용 지도를 설명한다.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-989",
      "org": "Urban Robotics Foundation (Bern Grush)",
      "title": "ISO-4448 Update Winter 2024",
      "published": "2024-02-04",
      "url": "https://www.urbanroboticsfoundation.org/post/iso-4448-update-winter-2024",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ISO/TC 204 ISO 4448 시리즈(공공 영역 이동로봇)의 부분 구성과 진행 상황을 표준 책임자가 정리한 글(2025-04-20 갱신). Part 6·9·16은 위원회 초안 제출 대기로 적는다.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-990",
      "org": "Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18)",
      "title": "Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists",
      "published": "2023-03",
      "url": "https://doi.org/10.1016/j.trip.2023.100789",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "노던애리조나대학 캠퍼스 10개 지점 1주일 영상으로 보도 배송로봇–보행자·자전거 상호작용을 침범 후 시간으로 분석한 동료심사 논문. 초록만 확인.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-991",
      "org": "대한민국 정책브리핑 (산업통상자원부·경찰청)",
      "title": "‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용",
      "published": "2023-11-16",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922726",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "2023-11-17 시행 개정 지능형로봇법·도로교통법에 따른 실외이동로봇의 보행자 지위, 16가지 시험항목 인증, 범칙금, 보험·공제 가입 의무를 설명한다.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-992",
      "org": "지디넷코리아",
      "title": "실외 배달로봇 '시속 15km 이하로'...16가지 안전기준",
      "published": "2023-07-28",
      "url": "https://zdnet.co.kr/view/?no=20230728173101",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "산업통상자원부·한국로봇산업진흥원의 실외이동로봇 운행안전 기준 16개 항목, 질량별 속도 상한, 폭 기준, 보험 보장액(시행 전 기준안)을 전한다.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-993",
      "org": "Dobrosovestnova, A., Schwaninger, I., & Weiss, A. (IEEE RO-MAN 2022)",
      "title": "With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow",
      "published": "2022",
      "url": "https://ieeexplore.ieee.org/abstract/document/9900588/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "탈린에서 눈에 갇힌 상업 배송로봇을 행인이 돕는 현상을 다룬 학회 논문(pp. 1023–1029). 연구 포털의 초록만 확인.",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-994",
      "org": "ISO",
      "title": "ISO/TR 4448-1:2024 Intelligent transport systems — Public-area mobile robots (PMR) — Part 1: Overview of paradigm",
      "published": "2024-08",
      "url": "https://www.iso.org/standard/81068.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. ISO/TC 204 의 공공 영역 이동로봇 배치 체계 개요 기술 보고서. 발행일·범위는 검색 결과 요약으로만 확인했다(ISO 페이지 403).",
      "cited_by": [
        "docs/categories/site-type-applications/outdoor.md"
      ],
      "source_unopened": true
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시는 무엇이며, 경사로·알림음·등화장치 같은 기존 항목은 어느 항목에 흡수됐는가?",
      "areas": [
        66,
        50,
        59
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "운행안전인증 대상이 로봇과 관제장치의 조합인데, 제조사가 다른 실외 로봇을 하나의 오케스트레이션 계층에서 지시할 때 그 계층이 인증상 관제장치에 해당하는지, 재인증이 필요한지에 관한 기준이나 해석이 있는가?",
      "areas": [
        66,
        20,
        59
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 보도에서 배송·순찰 로봇이 횡단 대기 중 연석 경사로·점자블록을 막지 않도록 하는 대기 위치 규칙이나 접근성 기준(인증 항목·지침)이 있는가?",
      "areas": [
        66,
        60,
        16
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 실외 로봇 운영사는 강설·결빙·폭우 때 운행 중단·재개 기준과 고립 로봇 회수 절차를 어떻게 정하고 있으며, 그 기준이 공개된 자료가 있는가?",
      "areas": [
        66,
        32
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "나라·주마다 다른 보도 로봇 규정(속도·크기·신고·보행자 의무)을 경로·속도 제약으로 기계가 읽을 수 있게 표현하는 공통 모델이 있으며, ISO 4448 의 경로 계획 충분성·운행 데이터 기록기 부분이 이를 다루는가?",
      "areas": [
        66,
        21,
        16
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "실외",
      "item": "시작 조건",
      "link": "docs/categories/site-type-applications/outdoor.md#5-적용-사례-현장-유형-명시",
      "title": "66. 실외"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/site-type-applications/outdoor.md#5-적용-사례-현장-유형-명시",
      "title": "66. 실외"
    },
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/site-type-applications/outdoor.md#5-적용-사례-현장-유형-명시",
      "title": "66. 실외"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/site-type-applications/outdoor.md#5-적용-사례-현장-유형-명시",
      "title": "66. 실외"
    },
    {
      "site_type": "실외",
      "item": "예외·성과",
      "link": "docs/categories/site-type-applications/outdoor.md#5-적용-사례-현장-유형-명시",
      "title": "66. 실외"
    }
  ],
  "standards_updates": [
    {
      "name": "실외이동로봇 운행안전인증 (지능형로봇법 제40조의2)",
      "kind": "평가 프로그램",
      "org": "한국로봇산업진흥원",
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "related_areas": [
        66,
        50,
        59
      ],
      "summary": "15km/h·500kg 이하 실외이동로봇과 관제장치 조합의 보도 운행 의무인증. 2026-09-30 확인한 안내는 8개 심사항목(2023-11 시행 당시 16개 시험항목)과 30일 이내 처리를 적는다.",
      "ref_id": "ref-980"
    },
    {
      "name": "ISO/TR 4448-1:2024 Public-area mobile robots (PMR) — Part 1: Overview of paradigm",
      "kind": "표준",
      "org": "ISO (ISO/TC 204)",
      "url": "https://www.iso.org/standard/81068.html",
      "related_areas": [
        66,
        50
      ],
      "summary": "원문 미열람. 2024-08 발행 기술 보고서로, 연석 승하차 로봇 도로 차량과 보호받지 않는 보행자 사이에서 배송·점검·유지보수·감시를 하는 로봇 장치의 배치 체계를 개관한다.",
      "ref_id": "ref-994"
    },
    {
      "name": "ISO 4448 시리즈 (Public-area mobile robots, Part 6·9·16 개발 중)",
      "kind": "표준",
      "org": "ISO/TC 204",
      "url": "https://www.urbanroboticsfoundation.org/post/iso-4448-update-winter-2024",
      "related_areas": [
        66,
        50,
        21
      ],
      "summary": "공공 영역 이동로봇 표준 시리즈. Part 6 경로 계획 충분성, Part 9 운행 데이터 기록기, Part 16 안전·신뢰성은 위원회 초안(CD) 제출을 앞두고 있다고 표준 책임자가 밝혔다(2025-04-20 갱신 기준, 이후 진행 상태 미확인).",
      "ref_id": "ref-989"
    },
    {
      "name": "Nav2 GPS 항법 구성 (navsat_transform·두 EKF 융합·rolling 전역 비용 지도)",
      "kind": "오픈소스",
      "org": "Open Navigation (Nav2)",
      "url": "https://docs.nav2.org/jazzy/tutorials/general_tutorials/navigation2_with_gps/navigation2_with_gps/",
      "related_areas": [
        66,
        15
      ],
      "summary": "실외 GPS 항법 튜토리얼. 일반 GPS 1~2m·최대 10m, RTK 약 1cm·기준국 필요를 적고 바퀴 주행거리계·IMU·GPS 융합 구성을 안내한다. ROP 에는 연계 대상이다.",
      "ref_id": "ref-988"
    }
  ],
  "additional_research_requests": [
    "5절 완료·인계: 딜리·뉴비·Starship 등 실외 배송·순찰 로봇의 수령 확인·순찰 완료 확인 방식(무엇이 확인돼야 일이 끝났다고 인정하는가) 자료가 브리프에 없어 '미확인'으로 두었다.",
    "5·9절: 딜리·뉴비의 관제·원격 제어 운영 방식과 사람 대응 분담, 실패 시 복구 주체 자료가 없어 미확인으로 두었다.",
    "5절 순찰 사례 제약: 덕수궁 등 순찰 구역의 운영 제약(시간·구역·관람객 동선) 자료가 없어 미확인으로 두었다.",
    "7절: 운행안전인증 심사항목 16개→8개 변경의 개정 시점·근거 고시 원문과 2023-07 기준안(질량별 속도·폭·보험 보장액)의 최종 고시 반영 여부 확인이 필요하다.",
    "7절: 미국 주 PDD 법 개수(2023-04 기준 23개 이상) 이후 변화와 일본 규정의 경찰청 원문 교차 확인이 필요하다.",
    "6절: 국내 실외 로봇 운영사의 강설·결빙·폭우 운행 중단·재개 기준과 고립 로봇 회수 절차 자료가 필요하다.",
    "9절: 제조사가 다른 실외 로봇을 한 오케스트레이션 계층에서 묶은 공개 사례를 찾아야 한다.",
    "5절: 출처 상한으로 조사하지 못한 해외 순찰(예: Knightscope)·공원·골프장 등 다른 실외 작업 사례가 필요하다.",
    "다음 65. 가정·공동주택 실행: 그 페이지의 '16개 시험항목' 서술에 기준일(2023-11-16)을 붙이고 2026-09-30 확인한 한국로봇산업진흥원 안내 8개 심사항목을 병기해야 한다(1차 검증 중복 지적)."
  ],
  "fixes_applied": [
    "ref-988 URL 교체 — 13절 각주 정의와 reference_updates·standards_updates 의 URL을 https://docs.nav2.org/jazzy/tutorials/general_tutorials/navigation2_with_gps/navigation2_with_gps/ 로 바꿨다.",
    "f19 구절 삭제 — 6절 위치 추정 소절에서 '도심·숲에서는 정확도가 더 떨어진다'를 빼고 GPS 1~2m·최대 10m, RTK 약 1cm·기준국, EKF 2개, navsat_transform(UTM 변환), rolling 전역 비용 지도만 '연계 대상'으로 짧게 썼다.",
    "f20 문구 수정 — 7절 표의 ISO 4448 시리즈 행과 standards_updates 를 'Part 6·9·16은 위원회 초안(CD) 제출을 앞두고 있다고 표준 책임자가 밝혔다(2024-02-04 게시, 2025-04-20 갱신 기준, 이후 진행 상태 미확인)'로 썼다.",
    "f15 문구 수정 — 5절 캠퍼스 사례 예외·성과 칸에 '문제 제기가 트위터에 올라온 뒤 두 시간이 채 안 돼' 대학이 시험 운행을 멈췄다고 썼다.",
    "f10 문구 수정 — 5절 캠퍼스 사례 서술에 '앞으로 2년간 식료품 사업이 10배 성장할 것으로 예상한다고 밝혔다(벤더 주장). [추정]'으로 쓰고 벤더 주장 병기를 유지했다.",
    "ref-981 발행일 — 13절 각주 정의와 reference_updates 의 발행일을 2026-06-08로 적었다.",
    "f22 수정 — 5절 도입 문장에서 '역 주변'을 빼고 순찰 형태는 덕수궁으로 한정했으며, 서울숲·충남대학교병원·도쿄 시부야는 작업 형태가 특정되지 않은 운영 장소로만 썼다.",
    "f23 수정 — 5절 세 사례의 완료·인계 칸과 여섯 항목 종합 문단에서 '주문자 문 앞 전달'을 빼고 '미확인(이번 자료에 수령 확인 방식 없음)'으로 두었으며 site_matrix_updates 에 완료·인계 칸을 넣지 않았다.",
    "f1·f2·f5 병기 — 7절 '인증 심사항목 수: 두 기준일의 값' 소절에 2023-11 시행 당시 16개 시험항목(기준일 2023-11-16)과 2026-09-30 확인한 KIRIA 안내 8개 심사항목을 모두 제시하고 차이의 원인은 [추정]으로만 쓴 뒤 11절 첫 번째 열린 질문으로 연결했다.",
    "f4 기준안 명시 — 7절 한국 항목에 '2023-07 지디넷코리아가 전한 시행 전 기준안'으로 밝히고 최종 고시 반영 여부는 미확인이라고 적었다.",
    "f13 연계 대상 — V-SLAM·5방향 카메라 위치 추정을 5절 순찰 사례 서술에서 '로봇 자체 지능·제어에 속하는 연계 대상'으로 한 문장만 썼다.",
    "f18 프리프린트 명시 — 6절과 8절에서 ref-982가 동료심사 전 arXiv 프리프린트(2025-07-16 제출, 2026-03-27 개정)임을 밝히고 결과는 직접 인용 없이 재서술했다.",
    "f16·f17 초록 기준 — 8절에서 ref-990·ref-993을 초록 기준으로 확인했음을 밝히고 상충 비율 등 초록에 없는 수치는 쓰지 않았다.",
    "ref-994 미열람 표시 — 13절 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, 7절 본문은 2024-08 발행 기술 보고서와 대상 범위만 썼다.",
    "용어집 기준일 병기 — glossary_updates 에 outdoor-mobile-robot-operational-safety-certification 을 action: update 로 내어 2023-11 시행 당시 16개 시험항목과 2026-09-30 확인한 한국로봇산업진흥원 안내 8개 심사항목을 두 기준일과 함께 적었다.",
    "f8 의견 주체 — 7절 미국 항목에서 [의견]의 주체를 'Ottonomy CEO Ritukar Vijay(ref-986 기사 인용)'로 밝혔다.",
    "분량 초과 자동 분리: 66. 실외 본문 10,505자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,034자"
  ]
}
```

### runs/2026-09-30-01/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/site-type-applications/outdoor.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area66-s7.md (1,761자)
    - docs/categories/site-type-applications/outdoor.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area66-s6.md (1,280자)
    - docs/categories/site-type-applications/outdoor.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area66-s8.md (1,110자)
    - docs/categories/site-type-applications/outdoor.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area66-s4.md (909자)
    - docs/categories/site-type-applications/outdoor.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area66-s11.md (816자)
    - docs/categories/site-type-applications/outdoor.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area66-s10.md (780자)
    - docs/categories/site-type-applications/outdoor.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area66-s3.md (683자)
```

### runs/2026-09-30-01/pages/categories/site-type-applications/outdoor.md

```markdown
---
title: "66. 실외"
type: area
category: "Q. 현장 유형별 적용"
area_no: 66
related_areas: [1, 3, 15, 16, 19, 20, 23, 26, 27, 31, 32, 38, 49, 50, 59, 60]
tags: [실외이동로봇 운행안전인증, 보도 배송, 순찰, 공공 영역 이동로봇, 날씨]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-980, ref-981, ref-982, ref-983, ref-984, ref-985, ref-986, ref-987, ref-988, ref-989, ref-990, ref-991, ref-992, ref-993, ref-994]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 66. 실외

# 66. 실외

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실외 적용**: 실외 배송·순찰·캠퍼스 운영과 보도 주행 규정·위성 위치·날씨 조건을 다룬다

## 2. 핵심 질문

보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? [분류원문]

## 3. 왜 중요한가

한국에서는 2023-11-17 개정 지능형로봇법·도로교통법 시행으로 운행안전인증을 받은 실외이동로봇이 보행자 지위를 얻어 보도를 다닐 수 있게 됐고, 이때부터 보도 운영은 인증·보행자 의무·보험이라는 법적 조건 위에서 이루어진다. [사실][^ref-991]

자세한 내용은 주제 페이지 [66. 실외 — 왜 중요한가](../../topics/2026/2026-09-30-area66-s3.md)에 있다.

## 4. 핵심 개념과 용어

실외 로봇을 이해하려면 보도 통행을 허용하는 법적 범주와 공공 영역 로봇 표준의 용어를 먼저 알아야 한다. [사실][^ref-980][^ref-989]

자세한 내용은 주제 페이지 [66. 실외 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area66-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

확인한 자료에서 실외 로봇 작업은 음식·장보기 물품을 매장에서 주문자에게 나르는 보도 배송, 덕수궁의 주·야간 순찰과 이상 감지, 대학 캠퍼스의 음식 배달이라는 세 형태로 나타난다. [추정][^ref-981][^ref-983][^ref-984][^ref-987][^ref-990]

**현장 유형:** 실외

**사례:** 서울 강남 보도에서 배민B마트 상품을 배달로봇 딜리로 배송

| 항목 | 내용 |
|---|---|
| 시작 조건 | 배민B마트 배달 주문이 작업을 발생시키는 것으로 보인다. [추정][^ref-983] |
| 작업 대상 | B마트 장보기 물품. 회사는 신규 모델 적재량이 2L 생수 6병에서 18병으로 늘었다고 밝혔다(벤더 주장). [추정][^ref-983] |
| 수행 자원 | 2025-06-17 운행안전인증을 받은 딜리 신규 모델. [사실][^ref-983] 인증은 로봇과 관제장치의 조합에 주어진다. [사실][^ref-980] 관제·원격 제어 운영 방식은 미확인 |
| 제약 | 보행자 지위에 따른 보행자 의무와 보도 운영자의 보험·공제 가입 의무. [사실][^ref-991] 낮은 연석·경사로·이면도로 시인성이 설계 개선 대상이었다고 회사가 밝혔다(벤더 주장). [추정][^ref-983] |
| 완료·인계 | 미확인(이번 자료에 수령 확인 방식 없음) |
| 예외·성과 | 시범 운영에서 평균 배달 시간 약 30분, 응답자 90%의 재이용 의사를 얻었다고 회사가 밝혔다(벤더 주장). [추정][^ref-983] 실패 시 복구 주체는 미확인 |

딜리는 2025년 2월부터 서울 강남구 논현동·역삼동에서 배민B마트 배달을 시범 운영했고, 신규 모델은 2025년 8월부터 현장에 투입될 예정이었다(2025-06-23 기사 기준). [사실][^ref-983] 회사는 신규 모델이 바퀴를 키워 낮은 연석을 넘고 경사로 주행이 나아졌으며, 배터리 용량이 약 30% 늘고 LED 깃대로 이면도로 시인성을 높였다고 밝혔다(벤더 주장). [추정][^ref-983]

**현장 유형:** 실외

**사례:** 덕수궁 경내 주·야간 순찰과 이상 상황 감지(뉴빌리티 뉴비)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 주·야간 순찰 운영. [사실][^ref-984] 순찰을 발생시키는 일정·호출 방식은 미확인 |
| 작업 대상 | 궁궐 경내 순찰 구역과 화재·쓰러짐 같은 이상 상황. [사실][^ref-984] |
| 수행 자원 | 자율주행 순찰 로봇 뉴비. [사실][^ref-984] 관제·사람 대응 분담은 미확인 |
| 제약 | 미확인(이번 자료에 순찰 구역의 운영 제약 없음) |
| 완료·인계 | 미확인(이번 자료에 순찰 완료 확인 방식 없음) |
| 예외·성과 | 회사 전체 기준으로 2026년 상반기까지 국내외 150여 개 현장, 누적 14만 6,721km 이상 주행, 2025년 한 해 4만 4,638회 서비스, 연간 약 1억 4,500만 건 데이터 생성(벤더 주장). [추정][^ref-984] |

뉴비는 덕수궁 외에 서울숲·충남대학교병원·도쿄 시부야 등에서도 운영되지만, 이들 장소의 작업 형태는 자료에서 특정되지 않았다(2026-09-02 기사 기준). [사실][^ref-984] 뉴비의 위치 추정은 5방향 카메라 영상으로 지도를 만들고 위치를 파악하는 V-SLAM(시각 기반 동시적 위치 추정·지도 작성) 방식이며, 이는 로봇 자체 지능·제어에 속하는 연계 대상이다. [사실][^ref-984]

**현장 유형:** 실외

**사례:** 피츠버그 대학 캠퍼스의 배송로봇 시험 운행과 연석 경사로 봉쇄(Starship)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 캠퍼스 음식 배달 주문. [추정][^ref-981][^ref-987] |
| 작업 대상 | 캠퍼스 배달 음식. [추정][^ref-981][^ref-987] |
| 수행 자원 | Starship 배송로봇과 시험 운행을 허가·중단한 대학. [사실][^ref-987] |
| 제약 | 길을 건너려 대기할 때 연석 경사로를 막지 않아야 한다. 회사는 로봇이 원래 경사로 뒤에서 기다리도록 설계됐다고 밝혔다. [사실][^ref-987] |
| 완료·인계 | 미확인(이번 자료에 수령 확인 방식 없음) |
| 예외·성과 | 휠체어 이용자가 차도에 갇혔고, 문제 제기가 트위터에 올라온 뒤 두 시간이 채 안 돼 대학이 시험 운행을 멈췄다. [사실][^ref-987] |

2019-10-21 보도에 따르면 이 일은 포브스 애비뉴에서 일어났고, Starship은 해당 교차로의 지도 오류 때문이라며 소프트웨어를 고치고 다른 교차로를 점검했다고 밝혔다. [사실][^ref-987] Starship은 2018년부터 캠퍼스를 운영해 왔으나 2026-06-08 미국 캠퍼스 운영을 종료하고 캠퍼스 로봇 1,200대 이상을 유럽·미국의 식료품 배송으로 옮긴다고 발표했으며, 식료품 시장이 더 크고 로봇이 개방된 도심 환경에서 안정적으로 운행한다는 점을 이유로 들었다. [사실][^ref-981] 이 전환은 캠퍼스가 실외 운영의 시험장 역할을 했음을 시사한다. [추정][^ref-981] 회사는 핀란드에서 자사 로봇이 식료품 배송의 약 20%를 처리하고 일반 배달원보다 건당 3~4달러 싸게 배송하며, 앞으로 2년간 식료품 사업이 10배 성장할 것으로 예상한다고 밝혔다(벤더 주장). [추정][^ref-981]

### 여섯 항목 종합

세 사례를 종합하면 시작 조건은 배달·장보기 주문과 순찰 일정, 작업 대상은 음식·식료품과 순찰 구역·이상 상황·보행자, 수행 자원은 배송·순찰 로봇과 관제장치·원격 제어자(때로 도움을 주는 행인), 제약은 인증·보행자 의무·속도·폭·보험과 관할별 크기·속도·신고 기준, 연석 경사로·좁은 보도·눈·위치 오차, 예외·성과는 눈 속 고립·접근성 사고와 운행 중단·배달 시간·비용으로 채워지며, 완료·인계의 확인 방식은 이번 자료에서 확인되지 않았다. [추정][^ref-983][^ref-984][^ref-980][^ref-993][^ref-991][^ref-985][^ref-986][^ref-987][^ref-982][^ref-988]

## 6. 대표 접근법과 기술

실외 로봇의 위치 추정과 주행은 로봇 제조사가 맡는 연계 대상이고, 운영 계층에 가까운 접근법은 불확실성을 고려한 경로 계획, 날씨의 제약·예외 처리, 사람 도움과 원격 개입, 접근성 민감 지점 관리다. [추정][^ref-988][^ref-982][^ref-993][^ref-987]

자세한 내용은 주제 페이지 [66. 실외 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area66-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

실외 로봇의 운영 기준은 한국의 운행안전인증, 나라·주마다 다른 보도 통행 법규, 개발 중인 ISO 4448 시리즈로 이루어진다. [추정][^ref-980][^ref-985][^ref-986][^ref-989]

자세한 내용은 주제 페이지 [66. 실외 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area66-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 연구는 보도 로봇과 보행자의 상호작용 관측, 눈 속 고립과 사람 개입, 불확실성 아래 경로 계획에 모여 있다. [추정][^ref-990][^ref-993][^ref-982]

자세한 내용은 주제 페이지 [66. 실외 — 대표 연구와 자료](../../topics/2026/2026-09-30-area66-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP는 실외에서 요청 수신·배정, 관할 규정과 날씨의 제약 반영, 예외 인계를 맡고, 배달 앱·로봇 주행·법적 인증은 연계 대상으로 두는 것이 원문 19장 경계에 맞는 것으로 보인다. [추정][^ref-980][^ref-983][^ref-988]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 배달·장보기 주문과 순찰 일정을 받아 인증받은 로봇에 배정하고 결과를 돌려준다. [추정][^ref-983][^ref-984] | 연계 대상: 배달 앱·식료품 주문 시스템. [추정][^ref-983] |
| 로봇 자체 지능·제어 | 위치 오차·눈 속 고립 같은 상태를 받아 원격 제어자·현장 인력에게 예외로 넘긴다. [추정][^ref-988][^ref-993] | 연계 대상: 위치 추정(GPS·RTK·V-SLAM)·장애물 회피·연석 주행. [추정][^ref-988][^ref-984] |
| 업종별 조건 | 관할마다 다른 속도·크기·보행자 의무·신고 조건과 날씨·혼잡을 경로·속도·운행 가능 구역 제약으로 반영하고, 연석 경사로 같은 접근성 민감 지점의 대기 규칙을 지도 제약으로 관리한다. [추정][^ref-991][^ref-985][^ref-986][^ref-982][^ref-987] | 연계 대상: 운행안전인증·도로교통법·일본 신고제·미국 주 PDD 법·보험, 주행 안전 성능과 인증 취득. [추정][^ref-980][^ref-991][^ref-985][^ref-986] |

이 표는 [범위 경계](../../about/scope-boundary.md)의 원문 19장 기준을 이 영역에 적용한 것이며, 경계는 제품 전략에 따라 이동할 수 있다. 한국 인증은 로봇과 관제장치의 조합을 대상으로 한다. [사실][^ref-980] 이종 제조사를 잇는 계층이 인증상 관제장치에 해당하는지는 11절 열린 질문으로 남기며, 제조사가 다른 실외 로봇을 한 계층에서 묶은 공개 사례는 이번 조사에서 확인되지 않았다. [추정][^ref-980][^ref-983][^ref-984]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 법규·안전, 보행자, 지도·위치, 경로·스케줄링, 예외 복구, 관제·연동, 사업 동향을 다루는 16개 세부영역과 이어진다. [추정][^ref-980][^ref-987][^ref-982][^ref-993][^ref-981]

자세한 내용은 주제 페이지 [66. 실외 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area66-s10.md)에 있다.

## 11. 열린 질문

이번 실행에서 다섯 질문이 새로 열렸다. id는 게시할 때 부여되며, 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [66. 실외 — 열린 질문](../../topics/2026/2026-09-30-area66-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-981]: DC Velocity, Starship steers its delivery robots off college campuses and toward grocery sector, 2026-06-08, https://www.dcvelocity.com/transportation/trucking/last-mile/starship-steers-its-delivery-robots-off-college-campuses-and-toward-grocery-sector, 접근일 2026-09-30
[^ref-982]: Tong, X., & Simoni, M. D. (arXiv), Robust Route Planning for Sidewalk Delivery Robots, 2025-07-16, https://arxiv.org/abs/2507.12067, 접근일 2026-09-30
[^ref-983]: 지디넷코리아, 배민, 차세대 배달로봇 ‘딜리’ 8월 투입…운행안전인증 획득, 2025-06-23, https://zdnet.co.kr/view/?no=20250623095742, 접근일 2026-09-30
[^ref-984]: 스포츠경향, 뉴빌리티, 덕수궁 순찰부터 도쿄 시내 배달까지, 2026-09-02, https://sports.khan.co.kr/article/202609020605003/, 접근일 2026-09-30
[^ref-985]: 内閣府 (일본 내각부), 令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について, 2023, https://www8.cao.go.jp/koutu//taisaku/r05kou_haku/zenbun/genkyo/topics/topic_1.html, 접근일 2026-09-30
[^ref-986]: Supply Chain Dive, Why delivery robots face a regulatory ‘nightmare’, 2023-04-26, https://www.supplychaindive.com/news/delivery-robot-bills-laws-proliferate-state-legislatures/648303/, 접근일 2026-09-30
[^ref-987]: The Pitt News, Pitt pauses testing of Starship robots due to safety concerns, 2019-10-21, https://pittnews.com/article/151679/news/pitt-pauses-testing-of-starship-robots-due-to-safety-concerns/, 접근일 2026-09-30
[^ref-988]: Open Navigation (Nav2), Navigating Using GPS Localization — Nav2 documentation, 미확인, https://docs.nav2.org/jazzy/tutorials/general_tutorials/navigation2_with_gps/navigation2_with_gps/, 접근일 2026-09-30
[^ref-989]: Urban Robotics Foundation (Bern Grush), ISO-4448 Update Winter 2024, 2024-02-04, https://www.urbanroboticsfoundation.org/post/iso-4448-update-winter-2024, 접근일 2026-09-30
[^ref-990]: Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18), Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists, 2023-03, https://doi.org/10.1016/j.trip.2023.100789, 접근일 2026-09-30
[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-993]: Dobrosovestnova, A., Schwaninger, I., & Weiss, A. (IEEE RO-MAN 2022), With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow, 2022, https://ieeexplore.ieee.org/abstract/document/9900588/, 접근일 2026-09-30
```

### docs/categories/site-type-applications/outdoor.md

```markdown
---
title: "66. 실외"
type: area
category: "Q. 현장 유형별 적용"
area_no: 66
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 66. 실외

# 66. 실외

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실외 적용**: 실외 배송·순찰·캠퍼스 운영과 보도 주행 규정·위성 위치·날씨 조건을 다룬다

## 2. 핵심 질문

보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? [분류원문]

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

### runs/2026-09-30-01/pages/topics/2026/2026-09-30-area66-s7.md

```markdown
---
title: "66. 실외 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 66
related_areas: [1, 3, 15, 16, 19, 20, 23, 26, 27, 31, 32, 38, 49, 50, 59, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-980, ref-985, ref-986, ref-988, ref-989, ref-991, ref-992, ref-994]
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/outdoor.md#7
---

[홈](../../index.md) › [주제](../index.md) › 66. 실외 — 관련 표준·프레임워크·오픈소스

# 66. 실외 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 실외 로봇의 운영 기준은 한국의 운행안전인증, 나라·주마다 다른 보도 통행 법규, 개발 중인 ISO 4448 시리즈로 이루어진다. [추정][^ref-980][^ref-985][^ref-986][^ref-989]
- 이 페이지는 [66. 실외](../../categories/site-type-applications/outdoor.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[66. 실외](../../categories/site-type-applications/outdoor.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

실외 로봇의 운영 기준은 한국의 운행안전인증, 나라·주마다 다른 보도 통행 법규, 개발 중인 ISO 4448 시리즈로 이루어진다. [추정][^ref-980][^ref-985][^ref-986][^ref-989]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| [실외이동로봇 운행안전인증](../../glossary/outdoor-mobile-robot-operational-safety-certification.md) | 평가 프로그램(법정 의무인증) | 보도를 다니는 로봇과 관제장치 조합의 인증이며, 신청일로부터 30일 이내에 처리한다(2026-09-30 확인). [사실][^ref-980] | [^ref-980] |
| ISO 4448 시리즈(공공 영역 이동로봇) | 표준(개발 중) | Part 1 개요 외에 Part 6 경로 계획 충분성, Part 9 운행 데이터 기록기, Part 16 안전·신뢰성이 있으며, Part 6·9·16은 위원회 초안(CD) 제출을 앞두고 있다고 표준 책임자가 밝혔다(2024-02-04 게시, 2025-04-20 갱신 기준, 이후 진행 상태 미확인). [사실][^ref-989] | [^ref-989] |
| ISO/TR 4448-1:2024 | 표준(기술 보고서) | 2024-08 발행. 연석에서 사람·화물을 싣고 내리는 로봇 도로 차량과 보호받지 않는 보행자 사이에서 배송·점검·유지보수·감시를 하는 로봇 장치의 배치 체계를 개관한다(원문 미열람). [사실][^ref-994] | [^ref-994] |
| Nav2 GPS 항법 구성 | 오픈소스 | 연계 대상: 로봇 자체 위치 추정·주행 구성(6절). [사실][^ref-988] | [^ref-988] |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

### 인증 심사항목 수: 두 기준일의 값

2023-11-17 시행 당시 운행안전인증은 16가지 시험항목을 두었다(기준일 2023-11-16). [사실][^ref-991][^ref-992] 2026-09-30 확인한 한국로봇산업진흥원 안내는 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치의 8개 심사항목을 적는다. [사실][^ref-980] 심사항목이 통폐합된 것으로 보이나, 개정 시점·근거 고시와 세부 기준이 완화됐는지는 원문으로 확인되지 않았다. [추정][^ref-991][^ref-980] 이 차이는 11절 첫 번째 열린 질문으로 남긴다.

### 관할별 보도 통행 규정

- **한국** — 개정 도로교통법은 운행안전인증을 받은 로봇에 보행자 지위를 주고 위반 시 운용자에게 범칙금 3만 원을 부과하며, 보도에서 운영하려는 자에게 보험 또는 공제 가입 의무를 지우고 한국로봇산업협회를 손해보장사업 실시기관으로 지정했다. [사실][^ref-991] 2023-07 지디넷코리아가 전한 시행 전 기준안은 질량에 따라 최고 속도를 230kg 초과 5km/h, 100kg 초과~230kg 10km/h, 100kg 이하 15km/h로 나누고, 로봇 폭을 기본 80cm·보도 폭 250cm 이상이면 최대 120cm로 하며, 보험 보장액을 사망·후유장애 1억 5천만 원, 부상 3천만 원, 재물 피해 사고당 10억 원으로 정했다. [사실][^ref-992] 이 기준안이 최종 고시에 그대로 반영됐는지는 미확인이다.
- **일본** — 2023-04-01 시행한 개정 도로교통법은 원격 조작형 소형차를 보도·노측대에서 보행자에 준하는 규칙으로 다니게 하고, 차체 표지 부착과 통행 장소를 관할하는 도도부현 공안위원회에 대한 사전 신고를 요구한다. [사실][^ref-985]
- **미국** — 주마다 기준이 달라 조지아는 최대 500파운드·보도 4mph, 뉴햄프셔는 최대 80파운드·10mph를 허용하며, 기사는 이 차이가 가벼운 로봇을 쓰는 Starship과 무거운 장치를 원한 Amazon·FedEx가 각 주 입법에 준 영향에서 비롯됐다고 분석했다(2023-04-26 기준). [사실][^ref-986] Ottonomy CEO Ritukar Vijay(ref-986 기사 인용)는 모든 주를 같은 기준으로 맞추는 일이 악몽이 될 것이라고 평가했다. [의견][^ref-986]

법령 자체는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)에서, 인증 제도는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)에서 다루며, 이 영역에서는 실외 운영의 제약 근거로만 쓴다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [66. 실외](../../categories/site-type-applications/outdoor.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/outdoor.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-985]: 内閣府 (일본 내각부), 令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について, 2023, https://www8.cao.go.jp/koutu//taisaku/r05kou_haku/zenbun/genkyo/topics/topic_1.html, 접근일 2026-09-30
[^ref-986]: Supply Chain Dive, Why delivery robots face a regulatory ‘nightmare’, 2023-04-26, https://www.supplychaindive.com/news/delivery-robot-bills-laws-proliferate-state-legislatures/648303/, 접근일 2026-09-30
[^ref-988]: Open Navigation (Nav2), Navigating Using GPS Localization — Nav2 documentation, 미확인, https://docs.nav2.org/jazzy/tutorials/general_tutorials/navigation2_with_gps/navigation2_with_gps/, 접근일 2026-09-30
[^ref-989]: Urban Robotics Foundation (Bern Grush), ISO-4448 Update Winter 2024, 2024-02-04, https://www.urbanroboticsfoundation.org/post/iso-4448-update-winter-2024, 접근일 2026-09-30
[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-994]: ISO, ISO/TR 4448-1:2024 Intelligent transport systems — Public-area mobile robots (PMR) — Part 1: Overview of paradigm, 2024-08, https://www.iso.org/standard/81068.html, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-01 | 66. 실외 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-01/pages/topics/2026/2026-09-30-area66-s6.md

```markdown
---
title: "66. 실외 — 대표 접근법과 기술"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 66
related_areas: [1, 3, 15, 16, 19, 20, 23, 26, 27, 31, 32, 38, 49, 50, 59, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-980, ref-982, ref-987, ref-988, ref-993]
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/outdoor.md#6
---

[홈](../../index.md) › [주제](../index.md) › 66. 실외 — 대표 접근법과 기술

# 66. 실외 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 실외 로봇의 위치 추정과 주행은 로봇 제조사가 맡는 연계 대상이고, 운영 계층에 가까운 접근법은 불확실성을 고려한 경로 계획, 날씨의 제약·예외 처리, 사람 도움과 원격 개입, 접근성 민감 지점 관리다. [추정][^ref-988][^ref-982][^ref-993][^ref-987]
- 이 페이지는 [66. 실외](../../categories/site-type-applications/outdoor.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[66. 실외](../../categories/site-type-applications/outdoor.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

실외 로봇의 위치 추정과 주행은 로봇 제조사가 맡는 연계 대상이고, 운영 계층에 가까운 접근법은 불확실성을 고려한 경로 계획, 날씨의 제약·예외 처리, 사람 도움과 원격 개입, 접근성 민감 지점 관리다. [추정][^ref-988][^ref-982][^ref-993][^ref-987]

### 위치 추정과 센서 융합 (연계 대상)

연계 대상: Nav2 공식 튜토리얼에 따르면 일반 GPS 정확도는 좋은 조건에서 1~2m, 최대 10m이고 위치가 자주 튀며, RTK는 약 1cm까지 줄이지만 기준국이 필요하다. [사실][^ref-988] 이 튜토리얼은 바퀴 주행거리계·관성 측정 장치(Inertial Measurement Unit, IMU)·GPS를 두 개의 확장 칼만 필터(Extended Kalman Filter, EKF)로 융합하고, 위경도 목표점을 UTM 좌표로 바꾸며, 사전 지도 없이 로봇을 따라 움직이는 전역 [비용 지도](../../glossary/costmap.md)(rolling costmap)를 쓰는 구성을 안내한다. [사실][^ref-988] 운영 계층은 이런 위치 오차를 제약과 예외 인계 조건으로 받아들이는 쪽을 맡는 것으로 보인다. [추정][^ref-988]

### 불확실성을 고려한 경로 계획

Tong·Simoni의 동료심사 전 arXiv 프리프린트(2025-07-16 제출, 2026-03-27 개정)는 보행자·장애물·날씨·혼잡 때문에 보도 배송로봇의 이동 시간이 크게 불확실하다고 보고, 강건 최적화와 시뮬레이션을 결합한 경로 계획을 스톡홀름 도심 자료로 시험했다. [사실][^ref-982] 여러 불확실성 표현 가운데 타원 불확실성 집합과 분포 강건 최단경로(Distributionally Robust Shortest Path, DRSP) 방법이 평균 지연과 최악 지연 모두에서 가장 좋은 결과를 냈고, 그 이점은 폭이 넓고 느린 로봇과 궂은 날씨·혼잡 조건에서 가장 컸다고 보고했다. [사실][^ref-982]

### 날씨를 제약과 예외 조건으로 다루기

날씨는 인증 요건(방수 성능), 이동 시간 불확실성과 경로 선택, 눈 속 고립과 사람 개입의 세 층위로 나타나므로, 운영 계층은 날씨·혼잡을 배정·경로의 제약과 예외 복구 조건으로 다뤄야 할 것으로 보인다. [추정][^ref-980][^ref-982][^ref-993] 국내 운영사의 강설·폭우 운행 중단·재개 기준은 이번 조사에서 확인되지 않아 11절 열린 질문으로 남긴다.

### 사람 도움과 원격 개입

에스토니아 탈린에서 눈에 갇힌 상업 배송로봇을 행인이 도와 운행을 이어 가게 한 현상을 다룬 연구는, 사람의 도움이 현실적 완화책이 될 수 있지만 회사가 무급 행인의 도움에 운영을 기대서는 안 된다고 지적했다. [사실][^ref-993] 따라서 눈 속 고립·위치 오차 같은 예외는 원격 제어자·현장 인력에게 넘기는 절차로 설계해야 할 것으로 보인다. [추정][^ref-993][^ref-988]

### 접근성 민감 지점의 대기 규칙

피츠버그 사례에서 회사는 로봇이 연석 경사로 뒤에서 기다리도록 설계됐으나 교차로 지도 오류로 경사로를 막았다고 설명했다. [사실][^ref-987] 연석 경사로 같은 접근성 민감 지점의 대기 위치를 지도 제약으로 관리하는 일은 운영 계층이 맡을 수 있는 일로 보인다. [추정][^ref-987]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [66. 실외](../../categories/site-type-applications/outdoor.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/outdoor.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-982]: Tong, X., & Simoni, M. D. (arXiv), Robust Route Planning for Sidewalk Delivery Robots, 2025-07-16, https://arxiv.org/abs/2507.12067, 접근일 2026-09-30
[^ref-987]: The Pitt News, Pitt pauses testing of Starship robots due to safety concerns, 2019-10-21, https://pittnews.com/article/151679/news/pitt-pauses-testing-of-starship-robots-due-to-safety-concerns/, 접근일 2026-09-30
[^ref-988]: Open Navigation (Nav2), Navigating Using GPS Localization — Nav2 documentation, 미확인, https://docs.nav2.org/jazzy/tutorials/general_tutorials/navigation2_with_gps/navigation2_with_gps/, 접근일 2026-09-30
[^ref-993]: Dobrosovestnova, A., Schwaninger, I., & Weiss, A. (IEEE RO-MAN 2022), With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow, 2022, https://ieeexplore.ieee.org/abstract/document/9900588/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-01 | 66. 실외 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-01/pages/topics/2026/2026-09-30-area66-s8.md

```markdown
---
title: "66. 실외 — 대표 연구와 자료"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 66
related_areas: [1, 3, 15, 16, 19, 20, 23, 26, 27, 31, 32, 38, 49, 50, 59, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-982, ref-987, ref-989, ref-990, ref-993]
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/outdoor.md#8
---

[홈](../../index.md) › [주제](../index.md) › 66. 실외 — 대표 연구와 자료

# 66. 실외 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 연구는 보도 로봇과 보행자의 상호작용 관측, 눈 속 고립과 사람 개입, 불확실성 아래 경로 계획에 모여 있다. [추정][^ref-990][^ref-993][^ref-982]
- 이 페이지는 [66. 실외](../../categories/site-type-applications/outdoor.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[66. 실외](../../categories/site-type-applications/outdoor.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 연구는 보도 로봇과 보행자의 상호작용 관측, 눈 속 고립과 사람 개입, 불확실성 아래 경로 계획에 모여 있다. [추정][^ref-990][^ref-993][^ref-982]

- Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J., Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists(2023) — 노던애리조나대학 캠퍼스 10개 지점의 1주일 영상으로 보도 자율 배송로봇과 보행자·자전거 이용자의 상호작용을 침범 후 시간(PET)으로 분석하고, 상충 수준·지점 특성을 예측 요인으로 모형화해 공유 통로의 시설 관리 전략을 제시하려 했다. 초록 기준으로 확인했으며 초록에 없는 상충 비율 같은 수치는 싣지 않는다. [사실][^ref-990]
- Dobrosovestnova, A., Schwaninger, I., & Weiss, A., With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow(2022) — 탈린에서 겨울에 눈에 갇힌 상업 배송로봇을 행인이 자발적으로 돕는 현상을 관찰·자기민속지·온라인 콘텐츠 분석으로 연구했다. 초록 기준으로 확인했고 운영 업체명은 미확인이다. [사실][^ref-993]
- Tong, X., & Simoni, M. D., Robust Route Planning for Sidewalk Delivery Robots(2025) — 이동 시간 불확실성을 강건 최적화와 시뮬레이션으로 다룬 경로 계획 연구이며, 동료심사 전 arXiv 프리프린트(2025-07-16 제출, 2026-03-27 개정)다. [사실][^ref-982]
- Urban Robotics Foundation(Bern Grush), ISO-4448 Update Winter 2024(2024-02-04 게시, 2025-04-20 갱신) — 표준 책임자가 ISO 4448 시리즈의 부분 구성과 진행 상황을 정리한 업계 글이다. [사실][^ref-989]
- The Pitt News, Pitt pauses testing of Starship robots due to safety concerns(2019) — 연석 경사로 봉쇄와 대학의 시험 중단, 회사의 지도 오류 설명을 보도했다. [사실][^ref-987]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [66. 실외](../../categories/site-type-applications/outdoor.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/outdoor.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-982]: Tong, X., & Simoni, M. D. (arXiv), Robust Route Planning for Sidewalk Delivery Robots, 2025-07-16, https://arxiv.org/abs/2507.12067, 접근일 2026-09-30
[^ref-987]: The Pitt News, Pitt pauses testing of Starship robots due to safety concerns, 2019-10-21, https://pittnews.com/article/151679/news/pitt-pauses-testing-of-starship-robots-due-to-safety-concerns/, 접근일 2026-09-30
[^ref-989]: Urban Robotics Foundation (Bern Grush), ISO-4448 Update Winter 2024, 2024-02-04, https://www.urbanroboticsfoundation.org/post/iso-4448-update-winter-2024, 접근일 2026-09-30
[^ref-990]: Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18), Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists, 2023-03, https://doi.org/10.1016/j.trip.2023.100789, 접근일 2026-09-30
[^ref-993]: Dobrosovestnova, A., Schwaninger, I., & Weiss, A. (IEEE RO-MAN 2022), With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow, 2022, https://ieeexplore.ieee.org/abstract/document/9900588/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-01 | 66. 실외 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-01/pages/topics/2026/2026-09-30-area66-s4.md

```markdown
---
title: "66. 실외 — 핵심 개념과 용어"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 66
related_areas: [1, 3, 15, 16, 19, 20, 23, 26, 27, 31, 32, 38, 49, 50, 59, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-980, ref-985, ref-986, ref-988, ref-989, ref-990, ref-991]
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/outdoor.md#4
---

[홈](../../index.md) › [주제](../index.md) › 66. 실외 — 핵심 개념과 용어

# 66. 실외 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 실외 로봇을 이해하려면 보도 통행을 허용하는 법적 범주와 공공 영역 로봇 표준의 용어를 먼저 알아야 한다. [사실][^ref-980][^ref-989]
- 이 페이지는 [66. 실외](../../categories/site-type-applications/outdoor.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[66. 실외](../../categories/site-type-applications/outdoor.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

실외 로봇을 이해하려면 보도 통행을 허용하는 법적 범주와 공공 영역 로봇 표준의 용어를 먼저 알아야 한다. [사실][^ref-980][^ref-989]

- **[실외이동로봇 운행안전인증](../../glossary/outdoor-mobile-robot-operational-safety-certification.md)(Outdoor Mobile Robot Operational Safety Certification)** — 지능형로봇법 제40조의2에 따른 의무인증으로, 최대 속도 15km/h·최대 질량 500kg 이하의 배송 등 자율주행([원격 조작](../../glossary/teleoperation.md) 포함) 로봇과 관제장치의 조합을 대상으로 한다(2026-09-30 확인). [사실][^ref-980]
- **보행자 지위** — 개정 도로교통법이 운행안전인증을 받은 실외이동로봇에 준 지위로, 보도 통행을 허용하는 대신 보행자 의무를 지게 한다. [사실][^ref-991]
- **원격 조작형 소형차(遠隔操作型小型車, Remote-controlled Small Vehicle)** — 일본 개정 도로교통법이 최고 속도 6km/h 이하, 길이 120cm·폭 70cm·높이 120cm 이하의 자동배송 로봇 등에 붙인 범주다. [사실][^ref-985]
- **개인 배송 장치(Personal Delivery Device, PDD)** — 미국 여러 주 법이 배송 로봇을 부르는 법적 범주이며, 무게·속도 기준이 주마다 다르다. [사실][^ref-986]
- **공공 영역 이동로봇(Public-area Mobile Robot, PMR)** — ISO/TC 204(지능형 교통 시스템)의 ISO 4448 시리즈가 다루는, 보도 등 공공 영역에서 보행자 곁을 다니는 로봇이다. [사실][^ref-989]
- **실시간 이동 측위(Real-Time Kinematic, RTK)** — 위성 위치 오차를 약 1cm까지 줄이지만 기준국이 필요한 방식으로, 로봇 자체 위치 추정에 속하는 연계 대상이다. [사실][^ref-988]
- **침범 후 시간(Post-Encroachment Time, PET)** — 보도 로봇과 보행자·자전거 이용자의 상호작용을 실제 충돌 없이 평가하는 대리 안전 지표로 쓰였다. [사실][^ref-990]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [66. 실외](../../categories/site-type-applications/outdoor.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/outdoor.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-985]: 内閣府 (일본 내각부), 令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について, 2023, https://www8.cao.go.jp/koutu//taisaku/r05kou_haku/zenbun/genkyo/topics/topic_1.html, 접근일 2026-09-30
[^ref-986]: Supply Chain Dive, Why delivery robots face a regulatory ‘nightmare’, 2023-04-26, https://www.supplychaindive.com/news/delivery-robot-bills-laws-proliferate-state-legislatures/648303/, 접근일 2026-09-30
[^ref-988]: Open Navigation (Nav2), Navigating Using GPS Localization — Nav2 documentation, 미확인, https://docs.nav2.org/jazzy/tutorials/general_tutorials/navigation2_with_gps/navigation2_with_gps/, 접근일 2026-09-30
[^ref-989]: Urban Robotics Foundation (Bern Grush), ISO-4448 Update Winter 2024, 2024-02-04, https://www.urbanroboticsfoundation.org/post/iso-4448-update-winter-2024, 접근일 2026-09-30
[^ref-990]: Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18), Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists, 2023-03, https://doi.org/10.1016/j.trip.2023.100789, 접근일 2026-09-30
[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-01 | 66. 실외 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-01/pages/topics/2026/2026-09-30-area66-s11.md

```markdown
---
title: "66. 실외 — 열린 질문"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 66
related_areas: [1, 3, 15, 16, 19, 20, 23, 26, 27, 31, 32, 38, 49, 50, 59, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: []
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/outdoor.md#11
---

[홈](../../index.md) › [주제](../index.md) › 66. 실외 — 열린 질문

# 66. 실외 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 실행에서 다섯 질문이 새로 열렸다. id는 게시할 때 부여되며, 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [66. 실외](../../categories/site-type-applications/outdoor.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[66. 실외](../../categories/site-type-applications/outdoor.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 실행에서 다섯 질문이 새로 열렸다. id는 게시할 때 부여되며, 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- (새 질문 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-01) 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시는 무엇이며, 경사로·알림음·등화장치 같은 기존 항목은 어느 항목에 흡수됐는가?
- (새 질문 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-01) 운행안전인증 대상이 로봇과 관제장치의 조합인데, 제조사가 다른 실외 로봇을 하나의 오케스트레이션 계층에서 지시할 때 그 계층이 인증상 관제장치에 해당하는지, 재인증이 필요한지에 관한 기준이나 해석이 있는가?
- (새 질문 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-01) 국내 보도에서 배송·순찰 로봇이 횡단 대기 중 연석 경사로·점자블록을 막지 않도록 하는 대기 위치 규칙이나 접근성 기준(인증 항목·지침)이 있는가?
- (새 질문 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-01) 국내 실외 로봇 운영사는 강설·결빙·폭우 때 운행 중단·재개 기준과 고립 로봇 회수 절차를 어떻게 정하고 있으며, 그 기준이 공개된 자료가 있는가?
- (새 질문 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-01) 나라·주마다 다른 보도 로봇 규정(속도·크기·신고·보행자 의무)을 경로·속도 제약으로 기계가 읽을 수 있게 표현하는 공통 모델이 있으며, ISO 4448의 경로 계획 충분성·운행 데이터 기록기 부분이 이를 다루는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [66. 실외](../../categories/site-type-applications/outdoor.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/outdoor.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-01 | 66. 실외 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-01/pages/topics/2026/2026-09-30-area66-s10.md

```markdown
---
title: "66. 실외 — 다른 연구영역과의 연결"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 66
related_areas: [1, 3, 15, 16, 19, 20, 23, 26, 27, 31, 32, 38, 49, 50, 59, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-980, ref-981, ref-982, ref-987, ref-993]
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/outdoor.md#10
---

[홈](../../index.md) › [주제](../index.md) › 66. 실외 — 다른 연구영역과의 연결

# 66. 실외 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 법규·안전, 보행자, 지도·위치, 경로·스케줄링, 예외 복구, 관제·연동, 사업 동향을 다루는 16개 세부영역과 이어진다. [추정][^ref-980][^ref-987][^ref-982][^ref-993][^ref-981]
- 이 페이지는 [66. 실외](../../categories/site-type-applications/outdoor.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[66. 실외](../../categories/site-type-applications/outdoor.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 법규·안전, 보행자, 지도·위치, 경로·스케줄링, 예외 복구, 관제·연동, 사업 동향을 다루는 16개 세부영역과 이어진다. [추정][^ref-980][^ref-987][^ref-982][^ref-993][^ref-981]

- [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md) — 캠퍼스에서 식료품 배송으로 옮긴 업체 전환.
- [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) — 건당 배송 비용과 사업 모델에 관한 회사 주장.
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md) — 위경도 좌표·UTM 변환과 운행 구역.
- [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 연석 경사로 같은 접근성 민감 지점과 교차로 지도 오류.
- [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) — 보도 로봇과 보행자·자전거 이용자의 상충 관측.
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 인증 대상인 관제장치와 이기종 관제.
- [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) — 배달 앱·주문 시스템 연동.
- [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) — 날씨·혼잡에 따른 이동 시간 불확실성.
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 불확실성을 고려한 강건 경로 계획.
- [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — 눈 속 고립 때 행인의 도움.
- [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 고립·위치 오차의 예외 인계와 원격 개입.
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) — 순찰 로봇의 이상 상황 감지.
- [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) — 보행자와 공유하는 보도의 안전.
- [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) — 운행안전인증과 ISO 4448 시리즈.
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — 도로교통법·관할별 규정·보험.
- [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) — 휠체어 이용자의 접근성.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [66. 실외](../../categories/site-type-applications/outdoor.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/outdoor.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-981]: DC Velocity, Starship steers its delivery robots off college campuses and toward grocery sector, 2026-06-08, https://www.dcvelocity.com/transportation/trucking/last-mile/starship-steers-its-delivery-robots-off-college-campuses-and-toward-grocery-sector, 접근일 2026-09-30
[^ref-982]: Tong, X., & Simoni, M. D. (arXiv), Robust Route Planning for Sidewalk Delivery Robots, 2025-07-16, https://arxiv.org/abs/2507.12067, 접근일 2026-09-30
[^ref-987]: The Pitt News, Pitt pauses testing of Starship robots due to safety concerns, 2019-10-21, https://pittnews.com/article/151679/news/pitt-pauses-testing-of-starship-robots-due-to-safety-concerns/, 접근일 2026-09-30
[^ref-993]: Dobrosovestnova, A., Schwaninger, I., & Weiss, A. (IEEE RO-MAN 2022), With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow, 2022, https://ieeexplore.ieee.org/abstract/document/9900588/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-01 | 66. 실외 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-01/pages/topics/2026/2026-09-30-area66-s3.md

```markdown
---
title: "66. 실외 — 왜 중요한가"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 66
related_areas: [1, 3, 15, 16, 19, 20, 23, 26, 27, 31, 32, 38, 49, 50, 59, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-981, ref-982, ref-985, ref-986, ref-987, ref-991, ref-992]
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/outdoor.md#3
---

[홈](../../index.md) › [주제](../index.md) › 66. 실외 — 왜 중요한가

# 66. 실외 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 한국에서는 2023-11-17 개정 지능형로봇법·도로교통법 시행으로 운행안전인증을 받은 실외이동로봇이 보행자 지위를 얻어 보도를 다닐 수 있게 됐고, 이때부터 보도 운영은 인증·보행자 의무·보험이라는 법적 조건 위에서 이루어진다. [사실][^ref-991]
- 이 페이지는 [66. 실외](../../categories/site-type-applications/outdoor.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[66. 실외](../../categories/site-type-applications/outdoor.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

한국에서는 2023-11-17 개정 지능형로봇법·도로교통법 시행으로 운행안전인증을 받은 실외이동로봇이 보행자 지위를 얻어 보도를 다닐 수 있게 됐고, 이때부터 보도 운영은 인증·보행자 의무·보험이라는 법적 조건 위에서 이루어진다. [사실][^ref-991]

인증 대상은 질량 500kg·시속 15km 이하 실외이동로봇이다. [사실][^ref-991][^ref-992] 인증받은 로봇도 신호위반·무단횡단 금지 같은 보행자 의무를 지키고, 위반하면 운용자가 범칙금 3만 원을 낸다(2023-11-16 발표 기준). [사실][^ref-991]

규정은 나라와 주마다 다르다. 일본은 2023-04-01부터 최고 6km/h 이하 소형 자동배송 로봇에 보도 통행을 허용하면서 사전 신고를 요구하고, 미국은 2022년 말까지 최소 23개 주가 무게·속도 기준이 서로 다른 배송 로봇 법을 만들었다(2023-04 기사 기준). [사실][^ref-985][^ref-986]

사업 흐름도 움직이고 있다. Starship Technologies는 2026-06-08 미국 대학 캠퍼스 운영을 끝내고 로봇을 식료품 배송으로 옮긴다고 발표했다. [사실][^ref-981] 공공 보도에서는 로봇의 판단 오류가 다른 사람에게 곧바로 영향을 준다. 2019년 피츠버그에서는 길을 건너려 대기하던 배송로봇이 연석 경사로를 막아 휠체어 이용자가 차도에 갇혔다. [사실][^ref-987]

그래서 여러 로봇을 묶어 운영하는 계층은 관할마다 다른 규정, 날씨·혼잡, 접근성 민감 지점을 배정·경로의 제약과 예외 조건으로 다뤄야 할 것으로 보인다. [추정][^ref-985][^ref-986][^ref-982][^ref-987]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/outdoor.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [66. 실외](../../categories/site-type-applications/outdoor.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/outdoor.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-981]: DC Velocity, Starship steers its delivery robots off college campuses and toward grocery sector, 2026-06-08, https://www.dcvelocity.com/transportation/trucking/last-mile/starship-steers-its-delivery-robots-off-college-campuses-and-toward-grocery-sector, 접근일 2026-09-30
[^ref-982]: Tong, X., & Simoni, M. D. (arXiv), Robust Route Planning for Sidewalk Delivery Robots, 2025-07-16, https://arxiv.org/abs/2507.12067, 접근일 2026-09-30
[^ref-985]: 内閣府 (일본 내각부), 令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について, 2023, https://www8.cao.go.jp/koutu//taisaku/r05kou_haku/zenbun/genkyo/topics/topic_1.html, 접근일 2026-09-30
[^ref-986]: Supply Chain Dive, Why delivery robots face a regulatory ‘nightmare’, 2023-04-26, https://www.supplychaindive.com/news/delivery-robot-bills-laws-proliferate-state-legislatures/648303/, 접근일 2026-09-30
[^ref-987]: The Pitt News, Pitt pauses testing of Starship robots due to safety concerns, 2019-10-21, https://pittnews.com/article/151679/news/pitt-pauses-testing-of-starship-robots-due-to-safety-concerns/, 접근일 2026-09-30
[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-01 | 66. 실외 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 979건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 260개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
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
- cell-based-production: 셀 생산 방식 (Cell-based Production)
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
- elevator-operating-rate: 승강기 가동률 (Elevator Operating Rate (EOR))
- empanelment-programme: 등재 프로그램 (Empanelment Programme)
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
- goods-to-person: 상품-대-사람 (Goods-to-Person (GTP))
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
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
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
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
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
- outdoor-mobile-robot-operational-safety-certification: 실외이동로봇 운행안전인증 (Outdoor Mobile Robot Operational Safety Certification)
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
- robot-friendly-building-certification: 로봇 친화형 건축물 인증 (Robot-Friendly Building Certification)
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
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- service-triad: 서비스 삼자 관계 (Service Triad (service robot, customer, frontline employee))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
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
- teleoperation: 원격 조작 (Teleoperation)
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
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [66] 에 걸린 0건 / 전체 185건)

```markdown
없음
```
