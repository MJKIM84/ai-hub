(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-15
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 50. 안전 표준·인증·사고 조사 (M. 안전)
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

### runs/2026-09-30-15/target.json

```json
{
  "run_id": "2026-09-30-15",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 124,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 50,
    "area_name": "50. 안전 표준·인증·사고 조사",
    "category": "M. 안전",
    "category_letter": "M"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=50"
}
```

### runs/2026-09-30-15/research.json

```json
{
  "run_id": "2026-09-30-15",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 50,
    "area_name": "50. 안전 표준·인증·사고 조사",
    "category": "M. 안전"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 조화 표준·적합성 추정, 협동 적용, 로봇 분류(ISO 10218:2025), 윤리적 블랙박스, 잠금·표지(LOTO), 중상 보고(SIR) 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 제조 공장·물류창고 사고 사례, 실외 법정 인증, 가정 모의 사고 조사 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 표준 적합성 경로(제조사·통합자·사용자), 사고 기록 장치, 증언·기록 결합 조사 절차 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 10218-1/-2:2025, ISO/FDIS 13482, ANSI/A3 R15.08, 실외이동로봇 운행안전인증 고시, KS B 7317 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-170, oq-186, oq-230 반영 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? [분류원문]",
    "산업용·이동·서비스 로봇 안전 표준(ISO 10218, ISO 3691-4, ISO 13482, ANSI/A3 R15.08)은 최근 어떻게 개정되었고 제조사·통합자·사용자에게 무엇을 요구하는가? (섹션 4·7 겨냥, oq-170)",
    "한국에서 로봇에 적용되는 법정 인증·KS 표준(실외이동로봇 운행안전인증, 협동로봇 관련 기준, 이동로봇 승강기 탑승 KS)은 무엇이며 심사 항목은 무엇인가? (섹션 5·7 겨냥, oq-186, oq-230, 한국 자료 우선)",
    "로봇 사고·아차 사고를 기록하고 원인을 조사하는 방법(사고 기록 장치, 조사 절차)에 관한 연구는 무엇을 제안하는가? (섹션 6·8 겨냥)",
    "실제 로봇 사고 통계와 사례는 어떤 작업·상황에서 사고가 나는지, 조사 자료에 어떤 한계가 있는지 보여 주는가? (섹션 3·5 겨냥, 제조 공장·물류창고·가정·실외·기타)",
    "안전 표준·인증·사고 조사에서 ROP가 직접 맡을 것과 제조사·통합자·인증기관·조사 기관에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "ISO 10218-1:2025(산업용 로봇 설계·제조, 제조사 대상)와 ISO 10218-2:2025(로봇 적용·로봇 셀 설계·통합, 통합자 대상)는 2025년 2월 발행된 2011년판 이후 첫 개정으로, 별도 기술 사양이던 ISO/TS 15066 의 협동 적용 요구와 수동 적재·하역 및 말단 장치 관련 기술 보고서 내용을 본문에 합치고, 기능 안전 요구를 명시화하며, 새 로봇 분류와 사이버보안 요구를 더했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1225",
        "ref-1226"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "The Robot Report: 2025-02-18 발행, TS 15066 통합, 기능 안전 요구 명시화, 새 분류와 시험 방법, 사이버보안 요구 추가. IBF: TS 15066 통합(손 안내·속도·분리 감시·동력·힘 제한), 2개 클래스 분류, 사이버보안·재기동 인터록 변경.",
      "as_of": "2025-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "EN ISO 10218-1/-2:2025 의 참조가 2026-09-07 EU 관보에 (EU) 2026/2015 시행 결정으로 게재되어 기계류 지침 2006/42/EC 의 필수 안전보건 요구에 대한 적합성 추정을 주게 되었고, 개정판은 안전 관련 제어 기능에 일률적으로 요구하던 PL d·범주 3 대신 표의 기본 성능 수준 적용 또는 위험성평가 근거 선택을 허용하며, 교대 종료 같은 운전 정지용 정상 정지 기능을 새로 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1226"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"On 7 September 2026, the references were published in the Official Journal of the European Union by Commission Implementing Decision (EU) 2026/2015.\" 이전 판은 ISO 13849-1 의 PL d·범주 3 을 요구했다고 설명.",
      "as_of": "2026-09-18",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "서비스 로봇 안전 표준 ISO 13482 는 개정판 ISO/FDIS 13482 가 2026-09-15 기준 단계 50.20(FDIS 투표 개시)에 있어 ISO 13482:2014 를 대체할 예정이며, 개인·전문(상업) 용도 서비스 로봇의 물리적 접촉 위험과 기능 안전을 다루고 산업용·의료용 로봇은 적용 범위에서 제외한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1227"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "세르비아 표준원(ISS)의 ISO 프로젝트 페이지: 단계 50.20, 효력일 2026-09-15, ISO 13482:2014 대체, 산업용·의료용 로봇 제외.",
      "as_of": "2026-09-15",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "ANSI/A3 R15.08-2(2023)는 산업용 이동로봇 시스템을 특정 적용·현장에 배치할 때 위험성평가는 통합자가 하고, 제조사와 통합자는 사용자에게 사용 정보를 주며, 교육과 안전 작업 절차는 사용자 책임이고, 사용자가 시스템을 개조하면 제조사·통합자 역할을 떠맡는다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1084"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "R15.08-2 는 IMR 시스템·적용의 통합·구성·배치 요구를 다루며 역할별 책임을 나눈다(Part 1 은 2020년 제조사 요구). (재인용: 2026-09-30-14)",
      "as_of": "2023-10-26",
      "site_type": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f5",
      "claim": "연계 대상: 한국로봇산업진흥원이 맡는 실외이동로봇 운행안전인증은 지능형로봇법 제40조의2 에 근거한 인증으로, 최대 질량 500kg·최고 속도 15km/h 이하 로봇을 대상으로 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치의 8개 심사항목을 두고 인증 처리기간을 신청일로부터 30일 이내로 안내한다.",
      "tag": "사실",
      "source_ids": [
        "ref-980"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "진흥원 인증 안내 페이지의 심사항목 표 8개(규격 및 운행속도 ~ 관제장치), 법적 근거 지능형로봇법 제40조의2, 처리기간 30일 이내. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f6",
      "claim": "연계 대상: 실외이동로봇 운행안전인증의 절차와 기준은 산업통상자원부 고시 제2023-211호 '실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시'(2023-11-17)로 정해졌고, 이 고시는 지능형로봇법(법률 제19412호) 개정 시행에 따라 제정되었으며 별표에서 로봇 모델 구분, 최고속도, 최대폭, 최대질량, 운행안전성 기준을 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-1230"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "고시 제2023-211호, 2023-11-17 게시. 2023-05-16 일부개정·2023-11-17 시행 지능형로봇법에 따라 제정. 별표 2~3 에 모델 구분·최고속도·최대폭·최대질량·운행안전성.",
      "as_of": "2023-11-17",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f7",
      "claim": "연계 대상: 고시 행정예고 단계의 보도(ZDNet Korea 2023-07-28)는 운행안전 기준을 16가지로 전하며, 질량별 속도 제한(230kg 초과 5km/h, 100kg 초과 10km/h), 폭 80cm 이하(보도 폭 250cm 이상이면 120cm), 5도 경사로 안정 주행, 비상정지, 장애물 회피, 알림음 55~73dB, 등화장치 표면 온도 60도 이하, 방수 IPX4 이상을 예로 들어, 진흥원 페이지의 8개 심사항목(f5)과 항목 수가 다르다.",
      "tag": "사실",
      "source_ids": [
        "ref-992",
        "ref-991"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "\"알림음은 55~73dB 이내여야 한다\". 정책브리핑(2023-11-16)도 16개 시험항목을 전함(같은 정부 발표 계열이라 독립 확인으로 보지 않음). 16개 전체 목록은 기사에 없음.",
      "as_of": "2023-07-28",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f8",
      "claim": "국가기술표준원은 2021-11-11 행정안전부와 협력해 실내 배송 로봇처럼 층간 이동에 승강기를 타는 로봇을 위한 KS B 7317 '이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법'을 제정했고, 이 표준은 속도 제어, 위험 상황의 보호 정지, 높낮이 차·틈새 극복, 추락·넘어짐 방지를 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-945"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "산업통상자원부 국가기술표준원 보도자료(2021-11-11): 실내 배송 로봇 등 대상, 속도제어·보호정지·높낮이차·틈새극복·추락·넘어짐 방지.",
      "as_of": "2021-11-11",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f9",
      "claim": "Winfield 외(2020)는 산업용 로봇과 달리 사람 사이에서 움직이는 사회적 로봇의 사고는 항공·철도 사고 조사와 같은 엄격함으로 조사되어야 하며, 사고 조사 없는 사회적 로봇 개발은 항공 사고 조사 없는 항공만큼 무책임하다고 주장했다.",
      "tag": "의견",
      "source_ids": [
        "ref-1232"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"social robotics without accident investigation would be no less irresponsible than aviation without air accident investigation\" (arXiv 초록)",
      "as_of": "2020-05",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "Winfield·van Maris·Salvini·Jirotka(2022)는 사회적 로봇의 센서·구동기·제어 결정 데이터를 안전하게 기록해 사고·아차 사고 조사를 돕는 장치 또는 소프트웨어 모듈인 윤리적 블랙박스(EBB)의 공개 표준 초안을 항공기 비행기록장치를 본떠 제안했고, 이를 논의용 첫 초안으로 내놓았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1233"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: sensor, actuator and control decisions 기록, accident or near-miss 조사 지원, 로봇 윤리 공동체 논의용 first draft. 세부 데이터 형식·보존 기간은 본문 추출 실패로 미확인.",
      "as_of": "2022-05-13",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f11",
      "claim": "가정 사례(모의): Webb 외(2021)는 사고 조사를 목격자 증언, 윤리적 블랙박스 기록, 해당 환경·로봇 전문가 분석, 기술·조직 권고로 구성하고, 지원 주거 아파트에서 넘어진 거주자 곁의 보조 로봇이 오작동해 직원에게 알리지 못하고 인터넷에도 연결되지 않은 모의 사고를 역할극 증언 면담으로 조사해 방법을 시험했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1234"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Frontiers in Robotics and AI 2021-06-29. 실제 사고가 아닌 모의 시나리오(지원 주거 아파트, 보조 로봇의 알림 실패)로 가상 목격자 증언 역할극 면담을 시험.",
      "as_of": "2021-06-29",
      "site_type": "가정",
      "flow_item": "예외·성과"
    },
    {
      "id": "f12",
      "claim": "Sanders·Sener·Chen(Applied Ergonomics 121, 2024)은 미국 OSHA 중상 보고(SIR)에서 2015~2022년 로봇 관련 사고 77건을 찾아, 고정형 로봇 54건(부상 66건, 주로 손가락 절단과 머리·몸통 골절)과 이동로봇 23건(부상 27건, 주로 다리·발 골절)으로 나누었고, 보고서 서술이 더 구조화되고 상세해야 한다고 결론지었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1235"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"More structured and detailed narratives in the SIRs are needed.\" 최종 서술 텍스트에 연역·귀납 2단계 주제 분석 적용(초록 기준).",
      "as_of": "2024",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "제조 공장 사례: 서울신문(2017-04-07)이 보도한 안전보건공단 산업안전보건연구원 조사에 따르면 2011~2015년 국내 산업용 로봇 재해자는 207명(사망 15명)이고, 그중 134명(64.7%)이 수리·점검·준비·설치 작업 중에, 90.7%가 방책 안에서 다쳤으며, 평균 근로손실일수는 707.5일로 제조업 평균 351.7일의 약 두 배였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1236"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기사 수치: 재해자 207명·사망 15명, 수리·점검·준비·설치 134명(64.7%), 방책 내부 90.7%, 근로손실 707.5일 대 351.7일, 50인 미만 사업장 현장조사 안전기준 적합 36.6%. 보고서 원문 미확인.",
      "as_of": "2017-04-07",
      "site_type": "제조 공장",
      "flow_item": "예외·성과"
    },
    {
      "id": "f14",
      "claim": "물류창고 사례: 2023-11-07 경남 고성의 농산물유통센터에서 파프리카 상자를 선별해 팔레트로 옮기는(출하 단계) 산업용 로봇의 센서 오류를 점검하고 프로그램을 고친 뒤 작동을 확인하던 작업자가 로봇에 압착되어 숨졌고, 경찰은 로봇이 사람을 상자로 인식한 것으로 보고 안전관리 책임자의 과실 여부를 수사했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1237"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "경향신문 2023-11-08: 시운전을 앞두고 센서 점검·프로그램 수정 후 작동 확인 중 사고, \"로봇이 A씨를 박스로 인식했던 것으로 보인다\"(경찰).",
      "as_of": "2023-11-08",
      "site_type": "물류창고",
      "flow_item": "예외·성과"
    },
    {
      "id": "f15",
      "claim": "제조 공장 사례: 2026-09-21 경남 고성의 식품 제조 공장에서 멈춘 제품 적재용 로봇을 점검하던 노동자가 끼여 2026-09-25 숨졌으며, 보도에 따르면 전원 차단·기동스위치 잠금·표지(LOTO)와 재가동 전 안전 확인 절차가 없었고, 고용노동부 통영지청은 산업안전보건법·중대재해처벌법 위반을, 경찰은 임의 재가동·기계 오작동 여부를 조사 중이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1238"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "경남도민일보 2026-09-29: LOTO 미실시, 지게차 운전원이 로봇 점검에 투입, 출입 인원 확인·작업지휘 미흡, 재가동 전 확인 절차 부재. 조사 진행 중이며 확정된 원인 아님.",
      "as_of": "2026-09-29",
      "site_type": "제조 공장",
      "flow_item": "예외·성과"
    },
    {
      "id": "f16",
      "claim": "기타(건설 현장) 사례: Belzile 외(2025)는 ISO 10218, ISO/TS 15066, ANSI/RIA R15.08, ANSI/ITSDF B56.5, CSA Z434 를 검토하고 이동로봇 전용이면서 다양한 배치 상황에 적용할 수 있는 표준은 없으며 이동 플랫폼의 위험성평가 문헌도 제한적이라고 보고, 건설 현장 이동로봇 배치용 위험성평가 틀을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-563"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"the literature on risk assessment as well as the standard specific to mobile platforms is rather limited\" (arXiv 2502.20693). ISO 3691-4·ISO 13482 는 이 논문에서 다루지 않음.",
      "as_of": "2025-02-28",
      "site_type": "기타",
      "flow_item": "제약"
    },
    {
      "id": "f17",
      "claim": "확인한 자료를 종합하면 핵심 질문(어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가)에 대해, 따를 표준·인증은 로봇 유형(산업용 ISO 10218, 이동 R15.08, 서비스 ISO 13482)과 현장·국가 조건(한국 실외 보도 운행 법정 인증, 승강기 탑승 KS B 7317)에 따라 갈리고 주요 표준이 2025~2026년 개정 중이며, 사고 원인 규명은 비행기록장치식 기록과 증언을 결합하는 방법이 연구 단계로 제안되었지만 현행 보고 자료는 서술이 구조화되지 않아 원인 분석에 한계가 있는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1225",
        "ref-1226",
        "ref-1227",
        "ref-1084",
        "ref-980",
        "ref-945",
        "ref-1233",
        "ref-1234",
        "ref-1235"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1~f5·f8(표준·인증), f10·f11(기록·조사 방법), f12(보고 자료 한계)를 종합한 추론.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "확인한 사고 자료(f12~f15)는 로봇 관련 중대 사고가 정상 운전보다 점검·수리·프로그램 수정·재가동 같은 비정상 작업 중에, 방책 안에서, 재가동 확인 절차가 없을 때 주로 일어났음을 보여 주므로, 여러 로봇을 지휘하는 플랫폼에서는 정비·점검 상태와 재가동 명령의 권한·확인 이력을 남기는 것이 예방과 사후 조사 모두에 필요할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1236",
        "ref-1237",
        "ref-1238",
        "ref-1235"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "수리·점검·준비·설치 중 64.7%, 방책 내부 90.7%(f13), 점검 후 작동 확인 중 사고(f14), LOTO·재가동 확인 부재(f15)에서 도출한 추론.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f19",
      "claim": "확인한 자료를 종합하면 50. 안전 표준·인증·사고 조사에서 ROP가 직접 맡을 범위는 로봇·적용마다 인증 상태, 적용 표준과 판, 인증이 허용한 운행 조건(질량·속도·구역)을 등록 정보로 관리해 배정·경로 제약에 반영하는 일, 정지·재가동·정비 모드 전환 명령과 로봇 상태 보고를 사고 조사에 쓸 수 있게 보존하는 플릿 수준 실행 기록, 표준 판 개정을 추적하는 일로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-980",
        "ref-1226",
        "ref-1233",
        "ref-1235"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "인증 대상 조건(f5), 표준 판 개정과 조화 게재(f1·f2), 기록 장치 제안(f10), 구조화된 사고 서술 필요(f12)에서 도출한 추론.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "연계 대상: 분류 원문 19장 기준으로 로봇 본체의 표준 적합성과 제품 인증은 제조사와 인증기관이, 로봇 셀·이동로봇 적용의 위험성평가와 사용 정보는 통합자가, 교육·작업 절차·잠금·표지는 사용자 사업장이, 실외 운행 인증과 보험은 운영자와 진흥원이, 법정 사고 조사는 고용노동부·경찰이 맡으므로, ROP는 그 결과와 조사에 필요한 실행 기록을 주고받는 인터페이스를 맡는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1225",
        "ref-1084",
        "ref-980",
        "ref-991",
        "ref-1238"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ISO 10218 제조사/통합자 구분(f1), R15.08-2 역할 분담(f4), 실외 인증(f5·f7), 노동부·경찰 조사(f15)에서 도출한 추론.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f21",
      "claim": "이 영역은 위험성평가·정지 절차의 48. 안전·위험 관리(f4·f15), 협동 적용·분리 거리의 49. 사람 근접 안전(f1), 인증 속성을 등록하는 4. 이기종 로봇 등록(f5), 승강기 탑승 기준의 22. 설비·건물 시스템 연동(f8), 사고 조사용 기록의 37. 관제 화면·실행 기록·38. 모니터링·이상 탐지·원인 분석(f10~f12), 재가동 권한의 51. 인증·권한·격리(f15), 사이버보안 요구의 52. 통신 보호·위협 관리·감사(f1), 시험·인증 절차의 54. 시험·형식 검증·벤치마크, 현장 위험성평가의 55. 현장 조사·설치·시운전(f16), 표준 판 추적의 57. 자산·소프트웨어 수명주기 관리(f2·f3), 책임 분담의 58. 다사업자 책임·계약·데이터(f4), 법정 인증·보험·조사의 59. 법·규제·보험·라이선스(f5~f7·f15), 적용 현장인 61. 물류창고(f14)·62. 제조 공장(f13·f15)·65. 가정·공동주택(f11)·66. 실외(f5~f7)·67. 기타 현장(f16)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1084",
        "ref-1238",
        "ref-1225",
        "ref-980",
        "ref-945",
        "ref-1233",
        "ref-1234",
        "ref-1235",
        "ref-563",
        "ref-1226",
        "ref-1227",
        "ref-1230",
        "ref-992",
        "ref-1237",
        "ref-1236"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 finding 의 대상과 분류 원문 세부영역 정의를 대조한 연결 제안.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1225",
      "org": "The Robot Report",
      "title": "ISO 10218 industrial robot safety standard receives major overhaul",
      "published": "2025-02",
      "url": "https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ISO 10218-1/-2:2025 발행(2025-02-18)과 주요 변경(TS 15066 통합, 기능 안전 명시화, 새 분류, 사이버보안)을 전하는 전문지 기사. 미국 R15.06 채택 작업 진행 언급.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1226",
      "org": "IBF Solutions",
      "title": "New standards for industrial robots EN ISO 10218-1 and -2",
      "published": "2026-09-18",
      "url": "https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "기계 안전 컨설팅 업체의 해설. EN ISO 10218:2025 의 EU 관보 게재(2026-09-07, (EU) 2026/2015), PL d·범주 3 일률 요구 폐지, 2개 클래스, 정상 정지 기능 등을 설명.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1227",
      "org": "Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보",
      "title": "ISO/FDIS 13482 Robotics — Safety requirements for service robots",
      "published": null,
      "url": "https://iss.rs/en/project/show/iso:proj:83498",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ISO 13482 개정 프로젝트 정보(단계 50.20, 2026-09-15, ISO 13482:2014 대체, 산업용·의료용 제외). ISO 원 페이지는 403 으로 열리지 않아 국가 표준기관의 프로젝트 정보로 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "인증기관의 제도 안내 페이지. 법적 근거(지능형로봇법 제40조의2), 대상(500kg·15km/h 이하), 8개 심사항목, 처리기간 30일 이내를 안내.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-992",
      "org": "ZDNet Korea",
      "title": "실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사",
      "published": "2023-07-28",
      "url": "https://zdnet.co.kr/view/?no=20230728173101",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "실외이동로봇 운행안전인증 고시(안) 행정예고를 전한 기사. 16가지 기준과 질량별 속도·폭·경사로·알림음·등화장치·방수 기준 예시.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1230",
      "org": "산업통상자원부",
      "title": "실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시",
      "published": "2023-11-17",
      "url": "https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "고시 제2023-211호 게시 페이지. 지능형로봇법 개정 시행에 따른 제정, 별표에 모델 구분·최고속도·최대폭·최대질량·운행안전성 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-945",
      "org": "산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11-11",
      "url": "https://eiec.kdi.re.kr/policy/materialView.do?num=220004",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "KS B 7317(이동 로봇의 엘리베이터 탑승 안전 요구사항·평가 방법) 제정 보도자료. 행정안전부 협력, 실내 배송 로봇 대상, 속도제어·보호정지·단차 극복·추락 방지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1232",
      "org": "Winfield, A. F. T., Winkle, K., Webb, H., Lyngs, U., Jirotka, M., & Macrae, C. (arXiv)",
      "title": "Robot Accident Investigation: a case study in Responsible Robotics",
      "published": "2020-05",
      "url": "https://arxiv.org/abs/2005.07474",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "사회적 로봇 사고를 항공 사고 조사 수준으로 조사해야 한다는 논거와 조사 틀을 제시한 논문(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1233",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv)",
      "title": "An Ethical Black Box for Social Robots: a draft Open Standard",
      "published": "2022-05-13",
      "url": "https://arxiv.org/abs/2205.06564",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "사회적 로봇의 센서·구동기·제어 결정 기록 장치(EBB) 공개 표준 초안. 초록만 확인했고 PDF 본문 추출은 실패.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1234",
      "org": "Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI)",
      "title": "Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions",
      "published": "2021-06-29",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "증언·EBB 기록·전문가 분석을 결합한 로봇 사고 조사 방법을 모의 사고(지원 주거 아파트의 보조 로봇)와 역할극 면담으로 시험한 연구.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1235",
      "org": "Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121)",
      "title": "Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports",
      "published": "2024",
      "url": "https://eprints.whiterose.ac.uk/id/eprint/217393/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "OSHA 중상 보고 2015~2022 의 로봇 관련 사고 77건 분석(고정형 54, 이동 23). 초록만 확인(출판사 페이지 403, 기관 저장소 레코드로 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1236",
      "org": "서울신문",
      "title": "[단독] 산업용 로봇 재해 위험 제조업보다 두 배 ... (제목 일부만 확인)",
      "published": "2017-04-07",
      "url": "https://www.seoul.co.kr/news/society/2017/04/07/20170407011011",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "안전보건공단 산업안전보건연구원의 2011~2015 산업용 로봇 재해 조사 결과를 전한 기사. 보고서 원문은 확인하지 못함.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1237",
      "org": "경향신문",
      "title": "‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망",
      "published": "2023-11-08",
      "url": "https://www.khan.co.kr/article/202311081103001",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "2023-11-07 고성 농산물유통센터 선별·적재 로봇 점검 중 사망 사고 보도. 경찰의 초기 판단 포함.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1238",
      "org": "경남도민일보",
      "title": "오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다",
      "published": "2026-09-29",
      "url": "https://www.idomin.com/news/articleView.html?idxno=2015923",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "2026-09-21 고성 식품 공장 적재 로봇 끼임 사망 사고의 안전조치 미비(LOTO·재가동 확인 부재)와 노동부·경찰 조사 상황 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-563",
      "org": "Belzile, B., Wanang-Siyapdjie, T., Karimi, S., Braga, R. G., Iordanova, I., & St-Onge, D. (arXiv)",
      "title": "From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment",
      "published": "2025-02-28",
      "url": "https://arxiv.org/abs/2502.20693",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "이동로봇 관련 안전 표준을 검토하고 건설 현장 배치용 위험성평가 틀을 제안한 프리프린트(HTML 본문 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2502.20693",
      "source_unopened": false
    },
    {
      "id": "ref-1084",
      "org": "The Robot Report",
      "title": "New AMR safety standard available with release of ANSI/A3 R15.08-2",
      "published": "2023-10-26",
      "url": "https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ANSI/A3 R15.08-2 발간과 제조사·통합자·사용자 역할 분담을 전하는 전문지 기사(재사용 출처, 이번 실행에서 다시 열지 않음).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-991",
      "org": "산업통상자원부·경찰청 (대한민국 정책브리핑)",
      "title": "‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인)",
      "published": "2023-11-16",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922726",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "개정 지능형로봇법 시행(2023-11-17)과 운행안전인증·보험 의무를 알린 정부 발표(재사용 출처, 이번 실행에서 다시 열지 않음).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
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
      "rationale": "섹션 3: f13·f12(사고가 점검·재가동 중, 방책 안에서 나고 손실이 큼), f17(핵심 질문 답, 추정) / 섹션 4: ISO 10218:2025 제조사·통합자 구분과 로봇 분류 f1, 조화 표준·적합성 추정 f2, 윤리적 블랙박스 f10, 잠금·표지(LOTO) f15, 중상 보고 f12 / 섹션 5: 제조 공장 — f13(예외·성과: 재해 통계)·f15(예외·성과: 적재 로봇 점검 중 사고, 조사 중임 명시), 물류창고 — f14(출하 단계 선별·팔레트 적재 로봇 사고), 실외 — f5·f6·f7(제약: 운행안전인증, 항목 수 출처 충돌 병기), 가정 — f11(모의 사고 조사임 명시), 기타 — f16(건설 현장). 병원·상업 시설 사례는 찾지 못함을 명시 / 섹션 6: 역할별 적합성 경로 f1·f4, 기록 장치와 증언 결합 조사 f10·f11, 비정상 작업 관리 f18(추정) / 섹션 7: ISO 10218-1/-2:2025 f1·f2, ISO/FDIS 13482 f3, ANSI/A3 R15.08-2 f4, 실외이동로봇 운행안전인증·고시 제2023-211호 f5~f7, KS B 7317 f8, EBB 초안 f10 / 섹션 8: f9~f12·f16 / 섹션 9: f19(직접 범위), f20(연계 대상) / 섹션 10: f21 — 4, 22, 37, 38, 48, 49, 51, 52, 54, 55, 57, 58, 59, 61, 62, 65, 66, 67 / 섹션 11: 기존 oq-170·oq-186·oq-230(미해결 유지, f5~f7 로 부분 근거)과 open_questions_new 4건. 다음 실행 후보: 66. 실외 페이지에 f5~f7, 22. 설비·건물 시스템 연동 페이지에 f8 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "윤리적 블랙박스",
      "term_en": "Ethical Black Box (EBB)",
      "definition": "로봇의 센서·구동기·제어 결정 데이터를 안전하게 계속 기록해 사고나 아차 사고 뒤 원인 조사에 쓰도록 항공기 비행기록장치를 본떠 제안된 장치 또는 소프트웨어 모듈이다."
    },
    {
      "term_ko": "잠금·표지",
      "term_en": "Lockout/Tagout (LOTO)",
      "definition": "점검·수리 전에 설비의 동력을 차단하고 기동 장치를 잠근 뒤 다른 사람이 가동하지 못하도록 표지를 다는 작업 안전 절차다."
    },
    {
      "term_ko": "적합성 추정",
      "term_en": "Presumption of Conformity",
      "definition": "EU 관보에 참조가 게재된 조화 표준을 적용한 제품은 해당 법령(예: 기계류 지침)의 필수 안전보건 요구를 충족한 것으로 추정되는 효력이다."
    }
  ],
  "open_questions_new": [
    "국내 KS B ISO 10218-1·-2 는 ISO 10218:2025 판을 언제 부합화하며, 산업안전보건기준에 관한 규칙의 협동로봇 방책 면제 인정 기준과 협동로봇 설치 작업장 안전인증은 새 판(로봇 분류·기능 안전 요구 변경)을 기준으로 바뀌는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 62. 제조 공장 | 근거: f1 | 종류: 일반",
    "여러 제조사 로봇을 지휘하는 플랫폼 수준에서 사고·아차 사고 조사에 필요한 최소 기록 항목(명령·정지·재가동·정비 모드 전환·상태 보고)을 정한 표준이나 공개 규약이 있는가, 윤리적 블랙박스 초안을 플릿 기록에 적용한 사례가 있는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석 | 근거: f10 | 종류: 일반",
    "2016년 이후 국내 로봇 관련 산업재해 통계를 고정형 산업용 로봇과 이동로봇(AMR·AGV)으로 나누어 집계한 공식 자료가 있는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 48. 안전·위험 관리 | 근거: f13 | 종류: 일반",
    "ISO/FDIS 13482 개정판은 여러 대가 함께 운영되는 서비스 로봇의 플릿 관제·승강기 연동·소프트웨어 갱신에 관한 안전 요구를 포함하는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 64. 상업 시설, 63. 병원·의료 | 근거: f3 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 17,
    "cross_checked_count": 1,
    "unverified": [
      "oq-170 미해결: ISO 3691-4:2023 원문·ISO 페이지·iTeh 카탈로그가 열리지 않거나 본문이 없어 운용 구역 요구를 표준 원문으로 확인하지 못함(검색 요약의 제3자 블로그 설명은 넣지 않음)",
      "oq-186·oq-230 미해결: 진흥원 페이지는 8개 심사항목, 행정예고 보도와 정책브리핑은 16가지 항목으로 전하며, 8개가 16개를 묶은 상위 항목인지 개정인지 고시 별표 원문으로 확인하지 못함. 근거 고시는 제2023-211호로 확인(f6)",
      "f5 인증 처리기간: 진흥원 페이지는 30일 이내, 검색 요약 한 곳은 60일로 달라 페이지 값만 기재",
      "f10 EBB 초안의 데이터 항목·형식·보존 기간: arXiv PDF 본문 추출 실패로 초록 범위만 기재",
      "f12 OSHA SIR 분석: 출판사 페이지 403, 기관 저장소의 초록만 확인",
      "f13 산업안전보건연구원 보고서 원문 미확인(기사 재인용), 끼임·부딪힘 비율은 기사에 없어 넣지 않음",
      "f15 2026-09 고성 사고는 조사 진행 중이며 원인 확정 아님",
      "ISO 10218:2025 의 '협동 적용' 용어 전환과 ANSI/A3 R15.06-2025·R15.08-3-2026 발간은 검색 요약에만 있어 넣지 않음(A3·ANSI 블로그 403)",
      "산업안전보건기준에 관한 규칙 제223조 단서와 협동로봇 설치 작업장 안전인증 기관: 법제처 원문이 열리지 않았고 인증기관을 한국로봇사용자협회로 적은 자료와 한국로봇산업진흥원으로 적은 기사가 달라 넣지 않음",
      "KS B 7317 2025-05-09 개정 여부는 검색 요약에만 있어 넣지 않음",
      "EU 기계류 규정 2023/1230 전환과 ISO 10218:2025 의 관계는 조사하지 못함",
      "병원·상업 시설의 안전 인증·사고 조사 사례는 찾지 못함"
    ],
    "scope_violations": [
      "f5·f6·f7: 실외 보도 운행 법정 인증은 원문 19장 '업종별 조건'(실외 차량 등)의 연계 대상이므로 claim 을 '연계 대상: '으로 시작함",
      "f20: 로봇 본체 인증(제조사·인증기관), 적용 위험성평가(통합자), 법정 사고 조사(노동부·경찰)는 ROP 밖 주체의 일로 '연계 대상: '으로 구분함",
      "f13~f15: 산업용 로봇 셀의 방호장치·LOTO 는 원문 19장 '시설·설비 제어'·설비 안전 제어에 가까우므로 사고 조사 근거로만 쓰고 ROP 직접 범위(f19)는 기록·권한 쪽으로 한정함"
    ],
    "budget_used": {
      "queries": 16,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1225~ref-563, 예약 구간 안)로 신규 출처 상한에 도달해 ZDNet 2023-11-30(운행안전인증 심사 시작), ZDNet 2025-05-14(KS B 7317 평가 통과 사례), 한국로봇사용자협회·기사(협동로봇 설치 작업장 안전인증), CAST 핸드북(연결 끊김)을 출처로 넣지 못했다. 재사용 2건(ref-1084, ref-991): 참고문헌 전체 목록이 입력에 없어 값은 이전 브리프 2026-09-30-14 출처 표를 따랐고 이번에 다시 열지 않아 fetched: false 로 적었다. 원문 열람: 신규 15건 모두 WebFetch 로 열었으나 ref-1232·ref-1233·ref-1235 는 초록만 읽었다. ISO(10218·13482·3691-4), A3, ANSI 블로그, ScienceDirect 는 403 이었다. 교차 확인 1건(f1: The Robot Report·IBF 두 곳). 기사 근거 finding(f7·f13·f14·f15)은 low. 벤더 기능 주장 없음. 분류 원문 핵심 질문에는 f17 로 답했고 결론은 '따를 표준은 로봇 유형·현장·국가 조건에 따라 갈리고 주요 표준이 개정 중이며, 사고 원인 규명은 기록 장치와 증언을 결합하는 방법이 연구 단계이고 현행 보고 자료는 구조화가 부족하다'는 추정이다. 현장 유형 사례는 제조 공장(f13·f15)·물류창고(f14)·실외(f5~f7)·가정(f11, 모의)·기타(f16, 건설 현장)이며 병원·상업 시설은 찾지 못했다. 국내 자료는 진흥원·산업통상자원부 고시·국가기술표준원·정책브리핑(재사용)과 기사 4건이다. 기존 열린 질문 oq-170·oq-186·oq-230 은 원문 확인 실패로 해결 제안하지 않았다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding 없음(f14 의 인식 오류는 사고 사례로만 다룸). 용어집에 이미 있는 위험성평가·STPA·근본 원인 분석·운용 구역·실외이동로봇 운행안전인증·협동 적용·동력·힘 제한·속도·분리 감시는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-15/verification.json

```json
{
  "run_id": "2026-09-30-15",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. ref-1225(The Robot Report, 2025-02-18)와 ref-1226(IBF Solutions, 2026-09-18)을 모두 열었다. 두 출처 모두 TS 15066 통합, 새 분류, 사이버보안 요구 추가를 적고 있고, TR 20218-1/-2(수동 적재·하역, 말단 장치) 통합은 ref-1225, 2011년판 이후 첫 대개정이라는 설명도 ref-1225에 있다. 두 출처는 발행 주체가 다르고 서로 인용하지 않으므로 독립 출처로 본다. 다만 둘 다 ISO 발행 원문이 아니라 해설이다(ISO 페이지는 403으로 열리지 않음)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1226에 2026-09-07 EU 관보 게재와 (EU) 2026/2015 결정, 적합성 추정, PL d·범주 3 일률 요구를 기본 성능 수준 표(예: 비상정지 PL c)와 위험성평가로 바꾼 점, 교대 종료 같은 경우의 정상 정지 안전 기능이 모두 있다. 검색으로도 EUR-Lex나 EC 페이지에서 결정 번호를 따로 확인하지 못해 단일 출처(컨설팅사 해설)다. 결정 번호와 게재일이 IBF 해설에 기댄 것임을 본문에 밝히도록 지시했다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1227(세르비아 표준원의 ISO 프로젝트 정보)에 단계 50.20, 날짜 2026-09-15, ISO 13482:2014 대체, 개인·전문 용도, 산업용·의료용 제외가 있다. 발행 전 FDIS 단계라 내용이 바뀔 수 있으므로 '대체 예정'과 기준일을 적도록 지시했다. 단일 출처다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 브리프에서는 미열람(fetched: false)이었으나 검증 중에 ref-1084(The Robot Report, 2023-10-26)를 열었다. 통합자의 위험성평가, 제조사·통합자의 사용 정보 제공, 사용자의 교육·안전 작업 절차, 개조한 사용자가 제조사·통합자 역할을 맡는다는 내용이 모두 있다. 표준 원문이 아닌 전문지 기사라 단일 출처다. 2026-09-30-14의 f6과 같은 주장이므로 ref-1084 각주를 재사용한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-980(한국로봇산업진흥원 인증 안내)에 지능형로봇법 제40조의2, 500kg·15km/h 이하, 8개 심사항목의 이름, 신청일부터 30일 이내 처리가 있다. 페이지 발행일은 미확인이고 확인일은 2026-09-30이다. 16개 항목을 전하는 f7과 충돌하므로 둘 다 제시해야 한다(oq-230)."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1230(산업통상자원부)을 첫 시도에서 연결이 끊겨 재시도로 열었다. 고시 제2023-211호, 2023-11-17 게시, 법률 제19412호(2023-05-16 개정, 2023-11-17 시행)에 따른 제정, 별표의 모델 구분·최고속도·최대폭·최대질량·운행안전성 기준을 확인했다. 별표 본문(첨부)은 열지 않았다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-992(ZDNet Korea, 2023-07-28)에서 16가지 기준, 질량별 속도(230kg 초과 5km/h, 100kg 초과 10km/h), 폭 80cm(보도 250cm 이상이면 120cm), 5도 경사로, 알림음 55~73dB, 등화장치 표면 60도 이하, IPX4를 확인했다. 브리프에서 미열람이던 ref-991(정책브리핑, 2023-11-16)도 검증 중에 열어 16가지 시험항목을 확인했다. 다만 둘 다 같은 정부 발표 계열이다. 수치는 행정예고안 단계의 보도이고 확정 고시 별표와 같은지는 미확인이다. f5와 충돌하므로 둘 다 제시하고 oq-230·oq-186에 연결하게 했다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-945(KDI 경제정보센터에 실린 국가기술표준원 보도자료, 2021-11-11)에 행정안전부 협력, 실내 배송 로봇 대상, 속도 제어·보호 정지·높낮이 차와 틈새 극복·추락과 넘어짐 방지가 있다. 표준 명칭은 KSSN 검색 결과로 확인했다. 검색 요약에는 KSSN 발행일 2021-11-30과 2025-05-09 개정이 보이나 열어서 확인하지는 않았다. 보도자료 날짜와 제정일을 구분하고 판(기준일)을 밝히도록 지시했다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1232(arXiv 2005.07474, 2020-05-15 제출) 초록에 항공·철도 사고 조사만큼의 엄격함과 인용 구절이 그대로 있다. [의견] 태그가 적절하며 Winfield 외의 의견임을 밝혀야 한다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1233(arXiv 2205.06564) 초록에 센서·구동기·제어 결정을 안전하게 기록하는 장치 또는 소프트웨어 모듈, 비행기록장치에 해당하는 로봇 장치라는 설명, 사고·아차 사고 조사 지원, 논의용 첫 초안이라는 점이 있다. 데이터 형식과 보존 기간은 미확인이다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1234(Frontiers in Robotics and AI, 2021-06-29) 본문에서 증언, EBB 기록, 전문가 분석·권고의 조사 틀과 노인 지원 주거 공동체의 역할극 시나리오(넘어진 거주자, 보조 로봇의 낙상 알림 실패, 인터넷 연결 불가)를 확인했다. 실제 사고가 아니라 역할극 모의임을 반드시 명시해야 한다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1235(White Rose 저장소 레코드, Applied Ergonomics 121, 104324, 2024) 초록에서 2015~2022년 77건, 고정형 54건(부상 66건, 손가락 절단·머리와 몸통 골절), 이동로봇 23건(부상 27건, 다리·발 골절), 보고 서술 개선 필요를 확인했다. 초록 범위의 확인이다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1236(서울신문, 2017-04-07)에서 2011~2015년 207명(사망 15명), 수리·점검·준비·설치 중 134명(64.7%), 방책 안 90.7%, 근로손실 707.5일 대 351.7일을 확인했다. 산업안전보건연구원 보고서 원문은 확인하지 못했다(기사를 통한 재인용). 3절의 핵심 수치인데 단일 기사 출처이므로 '서울신문 보도 기준, 보고서 원문 미확인'을 병기하게 했다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1237(경향신문, 2023-11-08)에서 2023-11-07 고성 농산물유통센터, 파프리카 등 상자를 선별해 팔레트로 옮기는 로봇, 센서 오류 점검과 프로그램 수정 뒤 작동 확인 중 사고, 경찰의 '박스로 인식' 판단, 안전관리 책임자 과실 수사를 확인했다. '(출하 단계)'는 기사에 없는 해석이므로 빼게 했다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": false,
      "tag_decision": "강등",
      "cross_checked": false,
      "note": "일부만 뒷받침한다. ref-1238(경남도민일보, 2026-09-29 입력·09-30 수정)에서 2026-09-21 사고와 09-25 사망, 오뚜기에스에프 고성공장 적재 로봇, 노동부 통영지청이 지적한 LOTO 미실시, 산업안전보건법·중대재해처벌법, 경찰의 임의 재가동·오작동 수사를 확인했다. 그러나 '재가동 전 안전 확인 절차가 없었다'는 기사에서 사실로 확인되지 않는다. 기사는 이를 해야 할 조치(권고)와 경찰 수사 쟁점으로만 전한다. 해당 부분은 [사실]로 쓰지 않고 수사 쟁점으로 낮춘다. LOTO 미실시와 조사 현황은 보도 기준 [사실]로 둘 수 있다. 원인은 확정되지 않았다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-563(arXiv 2502.20693 HTML 본문)에서 검토한 표준 5종(ISO 10218, ISO/TS 15066, ANSI/RIA R15.08, ANSI/ITSDF B56.5, CSA Z434)을 확인했다. '이동로봇 전용이면서 다양한 배치에 적용되는 표준은 없다'는 본문 문장, 제한된 문헌에 관한 초록 문장, 건설 현장 위험성평가 제안도 있다. 프리프린트다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 종합으로 유지한다. 근거 finding(f1~f5, f8, f10~f12)이 모두 살아남았다. 핵심 질문에 대한 답이다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. f15를 강등했으므로 '재가동 확인 절차가 없을 때 주로 일어났다'는 표현을 고치도록 지시했다. 근거 사고 자료는 사례 4건과 통계이고, '주로'는 f13 통계(64.7%, 90.7%)에만 기댈 수 있다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 원문 19장 '업종별 조건 → 작업·경로·권한 제약으로 반영'과 맞는 직접 범위 서술이다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. '연계 대상: '으로 외부 주체의 역할을 구분했다. f15를 강등했으므로 법정 조사 주체(노동부·경찰)만 근거로 쓴다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 연결 제안으로 유지한다. 연결하는 영역마다 번호와 이름을 함께 썼다. 54. 시험·형식 검증·벤치마크는 근거 finding 없이 연결됐다."
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
      "f5와 f7(실외이동로봇 운행안전인증 심사항목 8개 대 16가지)은 기존 열린 질문 oq-186·oq-230과 같은 충돌이다. 2026-09-30-14의 f25(2. 사용 사례·요구·책임 범위 페이지, '16개 시험항목')와도 겹치고 충돌한다.",
      "f4는 2026-09-30-14의 f6(ANSI/A3 R15.08-2 역할 분담, ref-1084)과 같은 주장이므로 ref-1084 각주를 재사용한다.",
      "f1은 49. 사람 근접 안전 페이지의 협동 적용·동력·힘 제한 서술과 이어진다. 중복하지 말고 10절에서 연결한다."
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
    "f15: '재가동 전 안전 확인 절차가 없었다'를 [사실]로 쓰지 않는다. 5절 제조 공장 사례에서는 LOTO 미실시(노동부 통영지청 지적)와 노동부·경찰 조사 현황만 [사실][^ref-1238]로 쓴다. 재가동 경위는 '다른 노동자가 작업 중임을 확인하지 않고 재가동했는지, 기계 오작동인지를 경찰이 수사 중'이라는 조사 쟁점으로만 쓰고, '원인 미확정(2026-09-29 보도 기준)'을 명시한다. 이유: 기사는 재가동 확인을 권고와 수사 쟁점으로만 전한다.",
    "f18: '재가동 확인 절차가 없을 때 주로 일어났다'를 '재가동 경위가 조사 쟁점이 된 사례가 있다'로 고친다. '주로'는 f13 통계(수리·점검 등 64.7%, 방책 안 90.7%)에만 붙이고 [추정]을 유지한다. 이유: f15 강등.",
    "f14: 주장 속 '(출하 단계)'를 뺀다. 5절 물류창고 사례의 작업은 '상자를 선별해 팔레트로 옮기는 작업'으로만 쓴다. 이유: 흐름 단계는 기사에 없는 해석이다.",
    "f5·f7: 5절 실외 사례와 7절에서 진흥원 페이지의 8개 심사항목(f5)과 행정예고 보도·정책브리핑의 16가지 항목(f7)을 둘 다 제시하고 어느 쪽도 고르지 않는다. 11절에서는 기존 oq-186·oq-230을 '열림'으로 유지해 연결한다. f7의 수치(질량별 속도, 폭, 경사로, 알림음 55~73dB, 등화장치 60도, IPX4)는 '2023-07 행정예고안 보도 기준, 확정 고시 별표 원문 미확인'이라고 적고, 현행 기준처럼 쓰지 않는다.",
    "f5: 5절과 7절의 운행안전인증 서술을 '연계 대상'으로 시작한다. 9절에서는 인증 자체는 운영자·진흥원의 일이고 ROP는 인증 조건을 작업·경로 제약으로 반영하는 쪽임을 f19·f20으로 구분한다. 이유: 원문 19장 업종별 조건.",
    "f8: '2021-11-11 국가기술표준원 보도자료로 제정을 알렸다'로 쓰고 기준일을 보도자료 날짜로 둔다. 2025년 개정 여부는 '미확인'으로 남긴다. 이유: 검색 결과에 KSSN 발행일 2021-11-30과 2025-05-09 개정이 보이나 원문으로 확인하지 못했다.",
    "f13: 3절과 5절에서 수치를 쓸 때 '서울신문 2017-04-07 보도 기준, 산업안전보건연구원 보고서 원문 미확인'과 기간(2011~2015)을 병기한다. 이유: 핵심 수치이고 단일 기사 출처다.",
    "f2: EU 관보 게재일(2026-09-07)과 시행 결정 번호((EU) 2026/2015)는 IBF Solutions 해설(ref-1226) 기준임을 본문에 밝힌다. 이유: 단일 출처이고 EUR-Lex 원문으로 확인하지 못했다.",
    "f3: ISO 13482 개정은 'FDIS 투표 단계(50.20, 2026-09-15 기준)로 발행 전이며 ISO 13482:2014를 대체할 예정'이라고 쓴다. 현행 표준처럼 쓰지 않는다.",
    "f11: 5절 가정 사례는 '실제 사고가 아닌 역할극 모의 사고(노인 지원 주거 공동체 시나리오)'임을 사례 머리에 명시한다.",
    "f9: [의견]임을 유지하고 'Winfield 외(2020)의 주장'으로 누구의 의견인지 밝힌다.",
    "ref-1084·ref-991: 브리프에서 fetched: false 로 적힌 출처이므로 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣는다(브리프 표시와 일치시킨다).",
    "5절: 병원·상업 시설 사례를 찾지 못했음을 명시하고, 사례 없는 칸은 site_matrix_updates 에 넣지 않는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 20건, 미확인 1건, 교차 확인 1건(f1: The Robot Report·IBF Solutions). 강등: f15 사실 → 일부 강등(재가동 전 확인 절차 부재는 수사 쟁점으로만 쓰고 LOTO 미실시·조사 현황만 보도 기준 사실로 둔다). 원문 미열람 출처: ref-1084, ref-991(브리프 기준 미열람. 검증 중 열어 내용을 확인했다). 주의: 안전 표준 서술은 ISO·ANSI 원문(403으로 열리지 않음)이 아니라 전문지·컨설팅사·국가 표준기관의 해설과 프로젝트 정보에 기댄다. ISO 13482 개정판은 발행 전 FDIS 단계이다. 실외이동로봇 운행안전인증 심사항목 수는 인증기관 페이지(8개)와 행정예고 보도·정책브리핑(16가지)이 달라 둘 다 제시했고 oq-186·oq-230은 미해결이다. 국내 산업용 로봇 재해 통계(2011~2015)는 기사 재인용이고 보고서 원문은 미확인이다. 2026-09 고성 식품 공장 사고는 조사 중이며 원인이 확정되지 않았다. 병원·상업 시설 사례는 찾지 못했다. 정정 요청 없음. 검증 검색 2회(리서치 16회 포함 누계 18회/30).",
  "retry_reason": null
}
```

### runs/2026-09-30-15/pages.json

```json
{
  "run_id": "2026-09-30-15",
  "outline": [
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 750,
      "summary": "따를 표준·인증은 로봇 유형과 현장·국가 조건에 따라 갈리고 주요 표준이 개정 중이다. [추정][^ref-1225] 국내 산업용 로봇 재해는 수리·점검 중, 방책 안에서 주로 났다(서울신문 2017-04-07 보도 기준, 보고서 원문 미확인). [사실][^ref-1236]",
      "planned_findings": [
        "f17",
        "f13",
        "f12"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "협동 적용, ISO 10218:2025 로봇 분류, 적합성 추정, 위험성평가·사용 정보, 윤리적 블랙박스, 잠금·표지, 중상 보고를 정리한다. [사실][^ref-1226][^ref-1233]",
      "planned_findings": [
        "f1",
        "f2",
        "f4",
        "f10",
        "f15",
        "f12"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2200,
      "summary": "제조 공장·물류창고 사고, 실외 운행안전인증(연계 대상), 가정 모의 사고 조사, 기타(건설 현장) 위험성평가 사례를 여섯 항목으로 쓴다. 병원·상업 시설 사례는 찾지 못했다. [사실][^ref-1238]",
      "planned_findings": [
        "f15",
        "f14",
        "f5",
        "f6",
        "f7",
        "f11",
        "f16"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1000,
      "summary": "표준 적합성은 제조사·통합자·사용자가 역할을 나눠 맞추고, 사고 원인 규명은 기록 장치와 증언을 결합하는 방법이 연구 단계로 제안되어 있다. [추정][^ref-1084][^ref-1234]",
      "planned_findings": [
        "f1",
        "f4",
        "f10",
        "f11",
        "f9",
        "f18"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1100,
      "summary": "ISO 10218-1/-2:2025와 EU 조화 게재, ISO/FDIS 13482(발행 전), ANSI/A3 R15.08-2, 실외이동로봇 운행안전인증(연계 대상), KS B 7317, EBB 초안을 표로 정리한다. [사실][^ref-1225][^ref-1227]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f10"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 700,
      "summary": "Winfield 외의 사고 조사 주장과 EBB 초안, Webb 외의 역할극 조사 방법, OSHA 중상 보고 분석, Belzile 외의 이동로봇 표준 검토를 소개한다. [사실][^ref-1233][^ref-1235]",
      "planned_findings": [
        "f9",
        "f10",
        "f11",
        "f12",
        "f16"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 900,
      "summary": "ROP는 인증 상태·허용 운행 조건을 등록해 배정·경로 제약에 반영하고 사고 조사용 실행 기록을 보존하며, 제품 인증·위험성평가·법정 조사는 외부 주체와 연계한다. [추정][^ref-980][^ref-1084]",
      "planned_findings": [
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1100,
      "summary": "위험성평가·정지 절차, 협동 적용, 로봇 등록, 승강기 연동, 실행 기록·원인 분석, 권한·보안, 수명주기, 책임·법규, 현장 유형 영역과 이어진다. [추정][^ref-1225][^ref-1233]",
      "planned_findings": [
        "f21"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "11. 열린 질문",
      "budget_chars": 800,
      "summary": "oq-170·oq-186·oq-230을 열린 채로 두고, 국내 KS 부합화, 플릿 수준 사고 기록 항목, 국내 이동로봇 재해 통계, ISO/FDIS 13482의 플릿 요구에 관한 새 질문 4건을 올린다.",
      "planned_findings": [
        "f1",
        "f3",
        "f5",
        "f7",
        "f10",
        "f13"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "seed → draft: 3~11절 첫 작성(표준·인증 개정 현황, 제조 공장·물류창고·실외·가정·기타 사례, 사고 기록·조사 방법, 책임 경계, 연결 17건, 열린 질문 7건), 각주 17건"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area50-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 50. 안전 표준·인증·사고 조사 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,413자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area50-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 50. 안전 표준·인증·사고 조사 의 \"4. 핵심 개념과 용어\" 절(1,007자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area50-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 50. 안전 표준·인증·사고 조사 의 \"6. 대표 접근법과 기술\" 절(990자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area50-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 50. 안전 표준·인증·사고 조사 의 \"11. 열린 질문\" 절(978자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area50-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 50. 안전 표준·인증·사고 조사 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(974자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area50-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 50. 안전 표준·인증·사고 조사 의 \"8. 대표 연구와 자료\" 절(859자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area50-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 50. 안전 표준·인증·사고 조사 의 \"3. 왜 중요한가\" 절(602자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 50. 안전 표준·인증·사고 조사 | seed → draft: 3~11절 첫 작성(ISO 10218:2025·ISO/FDIS 13482·R15.08-2·실외이동로봇 운행안전인증·KS B 7317, 사고 기록·조사 방법, 5개 현장 유형 사례), 각주 17건, 새 열린 질문 4건 | run 2026-09-30-15",
  "index_updates": {
    "home_recent": "2026-09-30 — 50. 안전 표준·인증·사고 조사: 3~11절 첫 작성(표준 개정 현황, 실외이동로봇 운행안전인증, 윤리적 블랙박스와 사고 조사 방법, 제조 공장·물류창고·실외·가정·기타 사례)",
    "category_recent": "2026-09-30 — 50. 안전 표준·인증·사고 조사: seed → draft, ISO 10218:2025·ISO/FDIS 13482·R15.08-2·KS B 7317 정리와 사고 조사 방법·사례, 연결 17건, 열린 질문 7건",
    "area_recent": "2026-09-30 — 50. 안전 표준·인증·사고 조사: 3~11절 첫 작성, 각주 17건(실행 2026-09-30-15)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "ethical-black-box",
      "term_ko": "윤리적 블랙박스",
      "term_en": "Ethical Black Box (EBB)",
      "definition": "로봇의 센서·구동기·제어 결정 데이터를 안전하게 기록해 사고나 아차 사고 뒤 원인 조사에 쓰도록 항공기 비행기록장치를 본떠 제안된 장치 또는 소프트웨어 모듈이다.",
      "description": "Winfield 외(2022)가 사회적 로봇용 공개 표준 초안을 논의용 첫 초안으로 내놓았다. 데이터 형식과 보존 기간은 미확인이다.",
      "related_areas": [
        50,
        37,
        38
      ],
      "sources": [
        "ref-1233"
      ]
    },
    {
      "action": "new",
      "slug": "lockout-tagout",
      "term_ko": "잠금·표지",
      "term_en": "Lockout/Tagout (LOTO)",
      "definition": "점검·수리 전에 설비의 동력을 차단하고 기동 장치를 잠근 뒤 다른 사람이 가동하지 못하도록 표지를 다는 작업 안전 절차다.",
      "description": "2026-09 경남 고성 식품 공장 적재 로봇 사고에서 고용노동부 통영지청이 미실시를 지적했다.",
      "related_areas": [
        50,
        48
      ],
      "sources": [
        "ref-1238"
      ]
    },
    {
      "action": "new",
      "slug": "presumption-of-conformity",
      "term_ko": "적합성 추정",
      "term_en": "Presumption of Conformity",
      "definition": "EU 관보에 참조가 게재된 조화 표준을 적용한 제품은 해당 법령(예: 기계류 지침)의 필수 안전보건 요구를 충족한 것으로 추정되는 효력이다.",
      "description": "IBF Solutions 해설 기준으로 EN ISO 10218-1/-2:2025 는 2026-09-07 관보 게재로 기계류 지침 2006/42/EC 에 대한 적합성 추정을 얻었다.",
      "related_areas": [
        50,
        59
      ],
      "sources": [
        "ref-1226"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-1225",
      "org": "The Robot Report",
      "title": "ISO 10218 industrial robot safety standard receives major overhaul",
      "published": "2025-02",
      "url": "https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ISO 10218-1/-2:2025 발행(2025-02-18)과 주요 변경(TS 15066 통합, 기능 안전 명시화, 새 분류, 사이버보안)을 전하는 전문지 기사.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1226",
      "org": "IBF Solutions",
      "title": "New standards for industrial robots EN ISO 10218-1 and -2",
      "published": "2026-09-18",
      "url": "https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "기계 안전 컨설팅 업체의 해설. EN ISO 10218:2025 의 EU 관보 게재(2026-09-07, (EU) 2026/2015), PL d·범주 3 일률 요구 폐지, 정상 정지 기능 등을 설명.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1227",
      "org": "Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보",
      "title": "ISO/FDIS 13482 Robotics — Safety requirements for service robots",
      "published": null,
      "url": "https://iss.rs/en/project/show/iso:proj:83498",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ISO 13482 개정 프로젝트 정보(단계 50.20, 2026-09-15, ISO 13482:2014 대체 예정, 산업용·의료용 제외).",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "인증기관의 제도 안내 페이지. 법적 근거(지능형로봇법 제40조의2), 대상(500kg·15km/h 이하), 8개 심사항목, 처리기간 30일 이내를 안내.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-992",
      "org": "ZDNet Korea",
      "title": "실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사",
      "published": "2023-07-28",
      "url": "https://zdnet.co.kr/view/?no=20230728173101",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "실외이동로봇 운행안전인증 고시(안) 행정예고를 전한 기사. 16가지 기준과 질량별 속도·폭·경사로·알림음·등화장치·방수 기준 예시.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1230",
      "org": "산업통상자원부",
      "title": "실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시",
      "published": "2023-11-17",
      "url": "https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "고시 제2023-211호 게시 페이지. 지능형로봇법 개정 시행에 따른 제정, 별표에 모델 구분·최고속도·최대폭·최대질량·운행안전성 기준.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-945",
      "org": "산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11-11",
      "url": "https://eiec.kdi.re.kr/policy/materialView.do?num=220004",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "KS B 7317(이동 로봇의 엘리베이터 탑승 안전 요구사항·평가 방법) 제정 보도자료. 행정안전부 협력, 실내 배송 로봇 대상, 속도제어·보호정지·단차 극복·추락 방지.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1232",
      "org": "Winfield, A. F. T., Winkle, K., Webb, H., Lyngs, U., Jirotka, M., & Macrae, C. (arXiv)",
      "title": "Robot Accident Investigation: a case study in Responsible Robotics",
      "published": "2020-05",
      "url": "https://arxiv.org/abs/2005.07474",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "사회적 로봇 사고를 항공 사고 조사 수준으로 조사해야 한다는 논거와 조사 틀을 제시한 논문(초록 확인).",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1233",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv)",
      "title": "An Ethical Black Box for Social Robots: a draft Open Standard",
      "published": "2022-05-13",
      "url": "https://arxiv.org/abs/2205.06564",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "사회적 로봇의 센서·구동기·제어 결정 기록 장치(EBB) 공개 표준 초안. 초록만 확인.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1234",
      "org": "Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI)",
      "title": "Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions",
      "published": "2021-06-29",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "증언·EBB 기록·전문가 분석을 결합한 로봇 사고 조사 방법을 모의 사고(지원 주거 아파트의 보조 로봇)와 역할극 면담으로 시험한 연구.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1235",
      "org": "Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121)",
      "title": "Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports",
      "published": "2024",
      "url": "https://eprints.whiterose.ac.uk/id/eprint/217393/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "OSHA 중상 보고 2015~2022 의 로봇 관련 사고 77건 분석(고정형 54, 이동 23). 초록만 확인.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1236",
      "org": "서울신문",
      "title": "[단독] 산업용 로봇 재해 위험 제조업보다 두 배 ... (제목 일부만 확인)",
      "published": "2017-04-07",
      "url": "https://www.seoul.co.kr/news/society/2017/04/07/20170407011011",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "안전보건공단 산업안전보건연구원의 2011~2015 산업용 로봇 재해 조사 결과를 전한 기사. 보고서 원문은 확인하지 못함.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1237",
      "org": "경향신문",
      "title": "‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망",
      "published": "2023-11-08",
      "url": "https://www.khan.co.kr/article/202311081103001",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "2023-11-07 고성 농산물유통센터 선별·적재 로봇 점검 중 사망 사고 보도. 경찰의 초기 판단 포함.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1238",
      "org": "경남도민일보",
      "title": "오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다",
      "published": "2026-09-29",
      "url": "https://www.idomin.com/news/articleView.html?idxno=2015923",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "2026-09-21 고성 식품 공장 적재 로봇 끼임 사망 사고의 LOTO 미실시 지적과 노동부·경찰 조사 상황 보도. 원인 미확정.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-563",
      "org": "Belzile, B., Wanang-Siyapdjie, T., Karimi, S., Braga, R. G., Iordanova, I., & St-Onge, D. (arXiv)",
      "title": "From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment",
      "published": "2025-02-28",
      "url": "https://arxiv.org/abs/2502.20693",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "이동로봇 관련 안전 표준을 검토하고 건설 현장 배치용 위험성평가 틀을 제안한 프리프린트(HTML 본문 확인).",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1084",
      "org": "The Robot Report",
      "title": "New AMR safety standard available with release of ANSI/A3 R15.08-2",
      "published": "2023-10-26",
      "url": "https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ANSI/A3 R15.08-2 발간과 제조사·통합자·사용자 역할 분담을 전하는 전문지 기사(브리프 기준 이번 실행에서 원문 미열람, 검증 중 내용 확인).",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-991",
      "org": "산업통상자원부·경찰청 (대한민국 정책브리핑)",
      "title": "‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인)",
      "published": "2023-11-16",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922726",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "개정 지능형로봇법 시행(2023-11-17)과 운행안전인증·보험 의무, 16개 시험항목을 알린 정부 발표(브리프 기준 이번 실행에서 원문 미열람, 검증 중 내용 확인).",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ],
      "source_unopened": true
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "국내 KS B ISO 10218-1·-2 는 ISO 10218:2025 판을 언제 부합화하며, 산업안전보건기준에 관한 규칙의 협동로봇 방책 면제 인정 기준과 협동로봇 설치 작업장 안전인증은 새 판(로봇 분류·기능 안전 요구 변경)을 기준으로 바뀌는가?",
      "areas": [
        50,
        62
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "여러 제조사 로봇을 지휘하는 플랫폼 수준에서 사고·아차 사고 조사에 필요한 최소 기록 항목(명령·정지·재가동·정비 모드 전환·상태 보고)을 정한 표준이나 공개 규약이 있는가, 윤리적 블랙박스 초안을 플릿 기록에 적용한 사례가 있는가?",
      "areas": [
        50,
        37,
        38
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "2016년 이후 국내 로봇 관련 산업재해 통계를 고정형 산업용 로봇과 이동로봇(AMR·AGV)으로 나누어 집계한 공식 자료가 있는가?",
      "areas": [
        50,
        48
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "ISO/FDIS 13482 개정판은 여러 대가 함께 운영되는 서비스 로봇의 플릿 관제·승강기 연동·소프트웨어 갱신에 관한 안전 요구를 포함하는가?",
      "areas": [
        50,
        64,
        63
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "제조 공장",
      "item": "시작 조건",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "제조 공장",
      "item": "제약",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "제조 공장",
      "item": "예외·성과",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "실외",
      "item": "시작 조건",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "가정",
      "item": "시작 조건",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "가정",
      "item": "작업 대상",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "가정",
      "item": "수행 자원",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "가정",
      "item": "제약",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "가정",
      "item": "예외·성과",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "기타",
      "item": "시작 조건",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "기타",
      "item": "제약",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    }
  ],
  "standards_updates": [
    {
      "name": "윤리적 블랙박스(EBB) 공개 표준 초안 (An Ethical Black Box for Social Robots: a draft Open Standard)",
      "kind": "프레임워크",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv)",
      "url": "https://arxiv.org/abs/2205.06564",
      "related_areas": [
        50,
        37,
        38
      ],
      "summary": "사회적 로봇의 센서·구동기·제어 결정 데이터를 안전하게 기록해 사고·아차 사고 조사를 돕는 기록 장치의 논의용 첫 공개 표준 초안(2022). 데이터 형식·보존 기간은 미확인.",
      "ref_id": "ref-1233"
    }
  ],
  "additional_research_requests": [
    "11절 oq-170: ISO 3691-4:2023 원문(운용 구역·사람 감지 요구)을 표준 원문 또는 공식 발췌로 확인해 7절 표에 행을 더할 근거가 필요하다(이번 실행에서 ISO 페이지 403).",
    "5·7절, oq-186·oq-230: 산업통상자원부 고시 제2023-211호 별표 원문(첨부)을 열어 8개 심사항목과 16가지 기준의 관계, 확정 기준값(속도·폭·알림음 등)을 확인해야 한다.",
    "7절: KS B 7317 의 KSSN 발행일(2021-11-30)과 2025-05-09 개정 여부를 원문으로 확인해야 한다(현재 '미확인').",
    "6절: 윤리적 블랙박스 초안의 데이터 항목·형식·보존 기간을 PDF 본문으로 확인해 플릿 수준 기록 항목과 비교할 근거가 필요하다.",
    "5절: 병원·상업 시설의 로봇 안전 인증·사고 조사 사례를 찾아야 한다(이번 조사에서 찾지 못함).",
    "10절: 54. 시험·형식 검증·벤치마크와의 연결은 근거 finding 이 없어 넣지 않았다. 시험·인증 절차(예: 인증 시험 항목과 시험 방법)를 다룬 출처가 있으면 연결 근거로 조사해야 한다.",
    "7절: EU 기계류 규정 (EU) 2023/1230 전환과 EN ISO 10218:2025 조화 게재의 관계를 EUR-Lex 원문으로 확인해야 한다((EU) 2026/2015 결정 번호도 IBF 해설 단일 출처).",
    "11절 새 질문: 산업안전보건기준에 관한 규칙 제223조 단서(협동로봇 방책 면제)와 협동로봇 설치 작업장 안전인증 기관(한국로봇사용자협회 대 한국로봇산업진흥원 출처 충돌)을 법제처 원문으로 확인해야 한다."
  ],
  "fixes_applied": [
    "f15 재가동 확인 절차 부재를 사실로 쓰지 않음 — 5절 제조 공장 사례에서 LOTO 미실시(노동부 통영지청 지적)와 노동부·경찰 조사 현황만 [사실][^ref-1238]로 쓰고, 재가동 경위는 '다른 노동자가 작업 중임을 확인하지 않고 재가동했는지, 기계 오작동인지를 경찰이 수사 중'인 조사 쟁점으로, '원인 미확정, 2026-09-29 보도 기준'을 명시했다. 4절 잠금·표지 항목도 미실시 지적만 썼다.",
    "f18 문구 수정 — 6절 '비정상 작업과 재가동 관리'에서 '재가동 확인 절차가 없을 때 주로'를 '재가동 경위가 조사 쟁점이 된 사례도 있다'로 바꾸고, '주로'는 2011~2015 통계(서울신문 보도 기준)에만 붙여 [추정]을 유지했다.",
    "f14 '(출하 단계)' 삭제 — 5절 물류창고 사례의 작업을 '상자를 선별해 팔레트로 옮기는 작업'으로만 썼고 흐름 단계를 적지 않았다.",
    "f5·f7 병기 — 5절 실외 사례의 제약 칸과 7절 인증 행에 진흥원 8개 심사항목과 행정예고 보도·정책브리핑 16가지를 함께 두고 고르지 않았으며, 11절에 oq-186·oq-230을 '열림'으로 유지해 연결했다. f7 수치 앞에 '2023-07 행정예고안 보도 기준, 확정 고시 별표 원문 미확인'을 적고 현행 기준이 아님을 밝혔다.",
    "f5 연계 대상 표시 — 5절 실외 사례 제목·시작 조건·서술과 7절 인증 행을 '연계 대상'으로 시작했고, 9절 표의 업종별 조건 행과 표 아래 문단에서 인증은 운영자·진흥원의 일, ROP는 인증 조건을 작업·경로 제약으로 반영하는 쪽임을 f19·f20으로 구분했다.",
    "f8 기준일 — 7절 KS B 7317 행을 '국가기술표준원이 행정안전부와 협력해 2021-11-11 보도자료로 제정을 알렸다'로 쓰고 2025년 개정 여부를 '미확인'으로 남겼다.",
    "f13 병기 — 3절(재해 통계)과 6절(주로 표현의 근거)에서 수치에 '서울신문 2017-04-07 보도 기준, 산업안전보건연구원 보고서 원문 미확인'과 기간 2011~2015를 병기했다. 5절에는 f13 수치를 쓰지 않았다.",
    "f2 출처 명시 — 4절 적합성 추정 항목과 7절 EU 조화 게재 행에 게재일 2026-09-07과 (EU) 2026/2015가 'IBF Solutions 해설 기준'임을 밝혔다.",
    "f3 발행 전 명시 — 7절 ISO/FDIS 13482 행을 'FDIS 투표 단계(50.20, 2026-09-15 기준)로 발행 전이며 ISO 13482:2014 를 대체할 예정'으로 썼다.",
    "f11 모의 명시 — 5절 가정 사례 제목 머리에 '실제 사고가 아닌 역할극 모의 사고(노인 지원 주거 공동체 시나리오)'를 적고 표 각 칸과 서술에도 모의임을 밝혔다.",
    "f9 의견 주체 — 6절과 8절에서 [의견]을 유지하고 'Winfield 외(2020)의 주장'으로 누구의 의견인지 밝혔다.",
    "ref-1084·ref-991 — 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.",
    "5절 병원·상업 시설 — 절 첫 단락에 병원·상업 시설 사례를 찾지 못했음을 명시했고, 그 두 현장 유형과 '해당 없음' 칸은 site_matrix_updates 에 넣지 않았다.",
    "분량 초과 자동 분리: 50. 안전 표준·인증·사고 조사 본문 10,442자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,711자"
  ]
}
```

### runs/2026-09-30-15/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area50-s7.md (1,413자)
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area50-s4.md (1,007자)
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area50-s6.md (990자)
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area50-s11.md (978자)
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area50-s10.md (974자)
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area50-s8.md (859자)
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area50-s3.md (602자)
```

### runs/2026-09-30-15/pages/categories/safety/safety-standards-certification-and-incident-investigation.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사"
type: area
category: "M. 안전"
area_no: 50
related_areas: [4, 22, 37, 38, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [ISO 10218, 실외이동로봇 운행안전인증, 윤리적 블랙박스, 사고 조사, 잠금·표지]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1084, ref-991, ref-1225, ref-1226, ref-1227, ref-980, ref-992, ref-1230, ref-945, ref-1232, ref-1233, ref-1234, ref-1235, ref-1236, ref-1237, ref-1238, ref-563]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [M. 안전](index.md) › 50. 안전 표준·인증·사고 조사

# 50. 안전 표준·인증·사고 조사

!!! info "소속 대분류"
    [M. 안전](index.md) — 핵심 질문:
    여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

안전 표준 적합성·인증, 사고 기록과 사후 조사 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **안전 표준·인증**: 산업용 로봇·이동 로봇·서비스 로봇 안전 표준(ISO 10218, ISO 3691-4, ISO 13482 등)과 인증에 맞춘다
- **사고 기록·사후 조사**: 사고와 아차 사고를 기록하고 원인을 조사해 재발을 막는다

## 2. 핵심 질문

어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? [분류원문]

## 3. 왜 중요한가

따를 안전 표준과 인증은 로봇 유형(산업용 ISO 10218, 이동 R15.08, 서비스 ISO 13482)과 현장·국가 조건(한국 실외 보도 운행 법정 인증, 승강기 탑승 KS B 7317)에 따라 갈리고 주요 표준이 2025~2026년에 개정 중이어서, 여러 제조사 로봇을 함께 운영하는 ROP는 적용 기준을 한 번 정하고 끝낼 수 없는 것으로 보인다. [추정][^ref-1225][^ref-1227][^ref-980][^ref-945]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 왜 중요한가](../../topics/2026/2026-09-30-area50-s3.md)에 있다.

## 4. 핵심 개념과 용어

표준 개정과 사고 자료를 읽으려면 다음 용어가 필요하다. 표준 관련 용어의 설명은 ISO·ANSI 원문이 아니라 전문지·컨설팅사 해설에 기댄다. [사실][^ref-1225][^ref-1226]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area50-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인한 사례는 제조 공장·물류창고의 사고, 실외 로봇의 법정 인증, 가정의 모의 사고 조사, 건설 현장의 위험성평가다. 병원·상업 시설의 안전 인증·사고 조사 사례는 이번 조사에서 찾지 못했다.

**현장 유형:** 제조 공장

**사례:** 식품 제조 공장에서 멈춘 적재 로봇을 점검하던 노동자의 끼임 사망 사고(2026-09)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 2026-09-21 제품 적재용 로봇이 멈춰 노동자가 점검에 나섰다. [사실][^ref-1238] |
| 작업 대상 | 멈춘 제품 적재용 로봇과 그 로봇을 점검하던 노동자 [사실][^ref-1238] |
| 수행 자원 | 점검 노동자와 적재 로봇 [사실][^ref-1238] |
| 제약 | 고용노동부 통영지청은 전원 차단·기동스위치 잠금·표지(LOTO)가 실시되지 않았다고 지적했다. [사실][^ref-1238] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 노동자가 끼여 2026-09-25 숨졌다. 노동부 통영지청은 산업안전보건법·중대재해처벌법 위반을 조사하고 있다. [사실][^ref-1238] |

재가동 경위는 조사 쟁점이다. 경찰은 다른 노동자가 작업 중임을 확인하지 않고 재가동했는지, 기계 오작동인지를 수사 중이며, 원인은 확정되지 않았다(원인 미확정, 2026-09-29 보도 기준). [사실][^ref-1238] 이 사례에서 이 영역은 예외·성과 항목, 곧 사고 뒤 누가 무엇을 조사하는가에 관여한다.

**현장 유형:** 물류창고

**사례:** 농산물유통센터에서 상자를 선별해 팔레트로 옮기는 로봇의 점검 중 압착 사망 사고(2023-11)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 로봇의 센서 오류를 점검하고 프로그램을 고친 뒤 작동을 확인하는 작업이었다. [사실][^ref-1237] |
| 작업 대상 | 파프리카 상자를 선별해 팔레트로 옮기는 산업용 로봇 [사실][^ref-1237] |
| 수행 자원 | 산업용 로봇과 점검 작업자 [사실][^ref-1237] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 2023-11-07 작업자가 로봇에 압착되어 숨졌다. 경찰은 로봇이 사람을 상자로 인식한 것으로 보고 안전관리 책임자의 과실 여부를 수사했다(2023-11-08 보도 기준). [사실][^ref-1237] |

두 사고 모두 정상 운전이 아니라 점검과 작동 확인 같은 비정상 작업 중에 일어났다. [사실][^ref-1237][^ref-1238]

**현장 유형:** 실외

**사례:** 연계 대상: 보도를 운행하는 실외이동로봇의 운행안전인증

| 항목 | 내용 |
|---|---|
| 시작 조건 | 연계 대상: 인증 신청이 심사를 발생시키며, 한국로봇산업진흥원은 처리기간을 신청일로부터 30일 이내로 안내한다(확인일 2026-09-30). [사실][^ref-980] |
| 작업 대상 | 최대 질량 500kg·최고 속도 15km/h 이하 실외이동로봇 [사실][^ref-980] |
| 수행 자원 | 지능형로봇법 제40조의2 에 근거한 인증을 한국로봇산업진흥원이 맡는다. [사실][^ref-980] |
| 제약 | 진흥원 페이지는 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치의 8개 심사항목을 둔다. [사실][^ref-980] 행정예고 보도와 정책브리핑은 16가지 기준·시험항목을 전한다. [사실][^ref-992][^ref-991] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

연계 대상: 인증 절차와 기준은 산업통상자원부 고시 제2023-211호(2023-11-17)로 정해졌고, 이 고시는 지능형로봇법(법률 제19412호) 개정 시행에 따라 제정되었으며 별표에서 로봇 모델 구분, 최고속도, 최대폭, 최대질량, 운행안전성 기준을 다룬다. [사실][^ref-1230]

2023-07 행정예고안 보도 기준, 확정 고시 별표 원문 미확인인 기준 예시는 질량별 속도 제한(230kg 초과 5km/h, 100kg 초과 10km/h), 폭 80cm 이하(보도 폭 250cm 이상이면 120cm), 5도 경사로 안정 주행, 비상정지, 장애물 회피, 알림음 55~73dB, 등화장치 표면 온도 60도 이하, 방수 IPX4 이상이다. 현행 기준으로 확인된 값이 아니다. [사실][^ref-992] 심사항목 수가 8개와 16가지로 달라 어느 쪽도 고르지 않고 함께 두며, 11절의 oq-186·oq-230 으로 남긴다. ROP는 인증 자체가 아니라 인증이 허용한 운행 조건을 작업·경로 제약으로 받는 쪽에서 이 사례에 관여한다(9절). [추정][^ref-980]

**현장 유형:** 가정

**사례:** 실제 사고가 아닌 역할극 모의 사고(노인 지원 주거 공동체 시나리오) — 넘어진 거주자 곁 보조 로봇의 알림 실패 조사

| 항목 | 내용 |
|---|---|
| 시작 조건 | 지원 주거 아파트에서 거주자가 넘어졌다(모의). [사실][^ref-1234] |
| 작업 대상 | 넘어진 거주자와 그 사실을 직원에게 알리는 정보(모의) [사실][^ref-1234] |
| 수행 자원 | 보조 로봇과 직원, 그리고 사고를 조사하는 조사자(모의) [사실][^ref-1234] |
| 제약 | 로봇이 인터넷에 연결되지 않은 상태였다(모의 조건). [사실][^ref-1234] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 보조 로봇이 오작동해 직원에게 알리지 못했다(모의). 조사는 목격자 증언, 윤리적 블랙박스 기록, 환경·로봇 전문가 분석, 기술·조직 권고로 구성되었다. [사실][^ref-1234] |

Webb 외(2021)는 이 모의 사고를 역할극 증언 면담으로 조사해 조사 방법을 시험했다. 실제 사고 자료가 아니므로 방법의 시험 사례로만 읽는다. [사실][^ref-1234]

**현장 유형:** 기타

**사례:** 건설 현장에 이동로봇을 배치하기 전의 위험성평가

| 항목 | 내용 |
|---|---|
| 시작 조건 | 건설 현장에 이동로봇을 배치하기 전 위험성평가 틀이 필요한 상황이다. [사실][^ref-563] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 해당 없음 |
| 제약 | ISO 10218, ISO/TS 15066, ANSI/RIA R15.08, ANSI/ITSDF B56.5, CSA Z434 를 검토한 결과, 이동로봇 전용이면서 다양한 배치 상황에 적용할 수 있는 표준이 없고 이동 플랫폼의 위험성평가 문헌도 제한적이었다. [사실][^ref-563] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

Belzile 외(2025)는 이 공백을 메우려고 건설 현장 이동로봇 배치용 위험성평가 틀을 제안했다(프리프린트). [사실][^ref-563]

## 6. 대표 접근법과 기술

표준 적합성은 제조사·통합자·사용자가 역할을 나눠 맞추는 구조이고, 사고 원인 규명은 기록 장치와 증언을 결합하는 방법이 연구 단계로 제안되어 있다. [추정][^ref-1225][^ref-1084][^ref-1234]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area50-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

6절의 역할별 경로는 아래 표준·인증으로 구체화되며, 주요 표준은 2025~2026년에 개정 중이다. [사실][^ref-1225][^ref-1227] 표준 서술은 ISO·ANSI 원문이 아니라 전문지·컨설팅사·국가 표준기관의 해설과 프로젝트 정보에 기댄다.

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area50-s7.md)에 있다.

## 8. 대표 연구와 자료

사고 기록·조사 연구는 사회적 로봇을 중심으로 방법을 제안하는 단계이고, 산업 현장 자료는 보고 서술의 구조화 부족을 드러낸다. [추정][^ref-1233][^ref-1235]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 대표 연구와 자료](../../topics/2026/2026-09-30-area50-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP가 직접 맡을 범위는 인증 상태·적용 표준과 판·허용 운행 조건을 등록해 배정·경로 제약에 반영하고, 사고 조사에 쓸 플릿 수준 실행 기록을 보존하는 일로 보인다. [추정][^ref-980][^ref-1226][^ref-1233][^ref-1235]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇·적용마다 인증 상태와 적용 표준·판을 등록 정보로 관리하고, 정지·재가동·정비 모드 전환 명령과 로봇 상태 보고를 사고 조사에 쓸 수 있게 보존한다. [추정][^ref-1226][^ref-1233] | 연계 대상: 로봇 본체의 표준 적합성과 제품 인증은 제조사와 인증기관이, 로봇 셀·이동로봇 적용의 위험성평가와 사용 정보는 통합자가 맡는다. [추정][^ref-1225][^ref-1084] |
| 업종별 조건 | 인증이 허용한 운행 조건(질량·속도·구역)을 배정·경로 제약에 반영하고 표준 판 개정을 추적한다. [추정][^ref-980][^ref-1226] | 연계 대상: 실외 운행 인증과 보험은 운영자와 한국로봇산업진흥원의 일이다. [추정][^ref-980][^ref-991] |
| 시설·설비 제어 | 사고 조사에 필요한 실행 기록을 외부 주체와 주고받는 인터페이스를 둔다. [추정][^ref-1238] | 연계 대상: 교육·작업 절차·잠금·표지는 사용자 사업장이, 법정 사고 조사는 고용노동부·경찰이 맡는다. [추정][^ref-1084][^ref-1238] |

실외이동로봇 운행안전인증처럼 인증 자체는 운영자·진흥원의 일이고, ROP는 그 결과를 받아 작업·경로 제약으로 반영하는 쪽이다. [추정][^ref-980] 이 경계는 제품 전략에 따라 옮겨질 수 있으며 기준은 [범위 경계](../../about/scope-boundary.md)에 있다. 이종 제조사를 연결하는 ROP는 각 주체의 인증·평가 결과와 조사에 필요한 실행 기록을 주고받는 인터페이스를 맡는 것으로 보인다. [추정][^ref-1225][^ref-1084][^ref-1238]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 위험성평가·정지 절차, 인증 속성 등록, 사고 조사용 기록, 법정 인증·책임 분담을 매개로 여러 영역과 이어진다. 아래 연결은 이번 조사 결과를 세부영역 정의와 대조한 제안이다. [추정][^ref-1084][^ref-1233]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area50-s10.md)에 있다.

## 11. 열린 질문

표준 원문을 열지 못한 부분과 출처가 충돌한 부분은 질문으로 남긴다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 열린 질문](../../topics/2026/2026-09-30-area50-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30 (원문 미열람)
[^ref-991]: 산업통상자원부·경찰청 (대한민국 정책브리핑), ‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인), 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30 (원문 미열람)
[^ref-1225]: The Robot Report, ISO 10218 industrial robot safety standard receives major overhaul, 2025-02, https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/, 접근일 2026-09-30
[^ref-1226]: IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2, 2026-09-18, https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2, 접근일 2026-09-30
[^ref-1227]: Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보, ISO/FDIS 13482 Robotics — Safety requirements for service robots, 미확인, https://iss.rs/en/project/show/iso:proj:83498, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: ZDNet Korea, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1230]: 산업통상자원부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시, 2023-11-17, https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view, 접근일 2026-09-30
[^ref-945]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-09-30
[^ref-1233]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-09-30
[^ref-1234]: Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI), Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions, 2021-06-29, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full, 접근일 2026-09-30
[^ref-1235]: Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports, 2024, https://eprints.whiterose.ac.uk/id/eprint/217393/, 접근일 2026-09-30
[^ref-1237]: 경향신문, ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망, 2023-11-08, https://www.khan.co.kr/article/202311081103001, 접근일 2026-09-30
[^ref-1238]: 경남도민일보, 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다, 2026-09-29, https://www.idomin.com/news/articleView.html?idxno=2015923, 접근일 2026-09-30
[^ref-563]: Belzile, B., Wanang-Siyapdjie, T., Karimi, S., Braga, R. G., Iordanova, I., & St-Onge, D. (arXiv), From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, 2025-02-28, https://arxiv.org/abs/2502.20693, 접근일 2026-09-30
```

### docs/categories/safety/safety-standards-certification-and-incident-investigation.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사"
type: area
category: "M. 안전"
area_no: 50
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [M. 안전](index.md) › 50. 안전 표준·인증·사고 조사

# 50. 안전 표준·인증·사고 조사

!!! info "소속 대분류"
    [M. 안전](index.md) — 핵심 질문:
    여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

안전 표준 적합성·인증, 사고 기록과 사후 조사 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **안전 표준·인증**: 산업용 로봇·이동 로봇·서비스 로봇 안전 표준(ISO 10218, ISO 3691-4, ISO 13482 등)과 인증에 맞춘다
- **사고 기록·사후 조사**: 사고와 아차 사고를 기록하고 원인을 조사해 재발을 막는다

## 2. 핵심 질문

어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? [분류원문]

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

### runs/2026-09-30-15/pages/topics/2026/2026-09-30-area50-s7.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "M. 안전"
primary_area_no: 50
related_areas: [4, 22, 37, 38, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1084, ref-991, ref-1225, ref-1226, ref-1227, ref-980, ref-992, ref-1230, ref-945, ref-1233]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/safety-standards-certification-and-incident-investigation.md#7
---

[홈](../../index.md) › [주제](../index.md) › 50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스

# 50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 6절의 역할별 경로는 아래 표준·인증으로 구체화되며, 주요 표준은 2025~2026년에 개정 중이다. [사실][^ref-1225][^ref-1227] 표준 서술은 ISO·ANSI 원문이 아니라 전문지·컨설팅사·국가 표준기관의 해설과 프로젝트 정보에 기댄다.
- 이 페이지는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

6절의 역할별 경로는 아래 표준·인증으로 구체화되며, 주요 표준은 2025~2026년에 개정 중이다. [사실][^ref-1225][^ref-1227] 표준 서술은 ISO·ANSI 원문이 아니라 전문지·컨설팅사·국가 표준기관의 해설과 프로젝트 정보에 기댄다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| ISO 10218-1:2025 · ISO 10218-2:2025 | 표준 | 제조사(-1)와 통합자(-2) 요구. ISO/TS 15066 협동 적용 요구와 수동 적재·하역, 말단 장치 관련 기술 보고서 내용을 합치고 새 로봇 분류·사이버보안 요구를 더했다. [사실][^ref-1225][^ref-1226] | The Robot Report, IBF Solutions |
| EN ISO 10218-1/-2:2025 EU 조화 게재 | 표준 | IBF Solutions 해설 기준으로 2026-09-07 EU 관보에 시행 결정 (EU) 2026/2015 로 참조가 게재되어 기계류 지침 적합성 추정을 준다. 안전 관련 제어 기능에 일률 요구하던 성능 수준(Performance Level, PL) d·범주 3 대신 표의 기본 성능 수준 적용 또는 위험성평가 근거 선택을 허용하고, 교대 종료 같은 운전 정지용 정상 정지 기능을 새로 요구한다. [사실][^ref-1226] | IBF Solutions |
| ISO/FDIS 13482 | 표준 | FDIS 투표 단계(50.20, 2026-09-15 기준)로 발행 전이며 ISO 13482:2014 를 대체할 예정이다. 개인·전문(상업) 용도 서비스 로봇의 물리적 접촉 위험과 기능 안전을 다루고 산업용·의료용 로봇은 제외한다. [사실][^ref-1227] | 세르비아 표준원 ISO 프로젝트 정보 |
| ANSI/A3 R15.08-2(2023) | 표준 | 산업용 이동로봇 시스템 배치의 제조사·통합자·사용자 역할 분담. [사실][^ref-1084] | The Robot Report |
| 실외이동로봇 운행안전인증 · 산업통상자원부 고시 제2023-211호 | 평가 프로그램 | 연계 대상: 지능형로봇법 제40조의2 에 근거한 법정 인증이다. [사실][^ref-980] 절차·기준은 고시 제2023-211호(2023-11-17)가 정한다. [사실][^ref-1230] 심사항목은 진흥원 페이지 8개와 행정예고 보도·정책브리핑 16가지로 다르다(11절). [사실][^ref-980][^ref-992][^ref-991] | 한국로봇산업진흥원, 산업통상자원부, ZDNet Korea, 정책브리핑 |
| KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 표준 | 국가기술표준원이 행정안전부와 협력해 2021-11-11 보도자료로 제정을 알렸다. 속도 제어, 위험 상황의 보호 정지, 높낮이 차·틈새 극복, 추락·넘어짐 방지를 다룬다. 2025년 개정 여부는 미확인이다. [사실][^ref-945] | 국가기술표준원 보도자료 |
| 윤리적 블랙박스(EBB) 공개 표준 초안 | 프레임워크 | 사고·아차 사고 조사용 기록 장치의 논의용 첫 초안. [사실][^ref-1233] | Winfield 외(arXiv) |

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30 (원문 미열람)
[^ref-991]: 산업통상자원부·경찰청 (대한민국 정책브리핑), ‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인), 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30 (원문 미열람)
[^ref-1225]: The Robot Report, ISO 10218 industrial robot safety standard receives major overhaul, 2025-02, https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/, 접근일 2026-09-30
[^ref-1226]: IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2, 2026-09-18, https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2, 접근일 2026-09-30
[^ref-1227]: Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보, ISO/FDIS 13482 Robotics — Safety requirements for service robots, 미확인, https://iss.rs/en/project/show/iso:proj:83498, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: ZDNet Korea, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1230]: 산업통상자원부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시, 2023-11-17, https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view, 접근일 2026-09-30
[^ref-945]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-09-30
[^ref-1233]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-15 | 50. 안전 표준·인증·사고 조사 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-15/pages/topics/2026/2026-09-30-area50-s4.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어"
type: topic
category: "M. 안전"
primary_area_no: 50
related_areas: [4, 22, 37, 38, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1084, ref-1225, ref-1226, ref-1233, ref-1235, ref-1238]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/safety-standards-certification-and-incident-investigation.md#4
---

[홈](../../index.md) › [주제](../index.md) › 50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어

# 50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 표준 개정과 사고 자료를 읽으려면 다음 용어가 필요하다. 표준 관련 용어의 설명은 ISO·ANSI 원문이 아니라 전문지·컨설팅사 해설에 기댄다. [사실][^ref-1225][^ref-1226]
- 이 페이지는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

표준 개정과 사고 자료를 읽으려면 다음 용어가 필요하다. 표준 관련 용어의 설명은 ISO·ANSI 원문이 아니라 전문지·컨설팅사 해설에 기댄다. [사실][^ref-1225][^ref-1226]

- **협동 적용(Collaborative Application)** — ISO 10218:2025 는 별도 기술 사양이던 ISO/TS 15066 의 협동 적용 요구를 본문에 합쳤다. [사실][^ref-1225][^ref-1226] 용어 설명: [협동 적용](../../glossary/collaborative-application.md)
- **ISO 10218:2025 의 로봇 분류** — 개정판은 새 로봇 분류와 사이버보안 요구를 더하고 기능 안전 요구를 명시화했다. [사실][^ref-1225][^ref-1226]
- **적합성 추정(Presumption of Conformity)** — EU 관보에 참조가 게재된 조화 표준을 적용한 제품이 해당 법령의 필수 안전보건 요구를 충족한 것으로 추정되는 효력이다. IBF Solutions 해설 기준으로 EN ISO 10218-1/-2:2025 는 2026-09-07 관보 게재로 기계류 지침 2006/42/EC 에 대한 이 효력을 얻었다. [사실][^ref-1226]
- **위험성평가(Risk Assessment)와 사용 정보(Information for Use)** — ANSI/A3 R15.08-2(2023)에서 이동로봇 적용의 위험성평가는 통합자가 하고, 제조사와 통합자는 사용자에게 사용 정보를 준다. [사실][^ref-1084] 용어 설명: [위험성평가](../../glossary/risk-assessment.md), [사용 정보](../../glossary/information-for-use.md)
- **윤리적 블랙박스(Ethical Black Box, EBB)** — 로봇의 센서·구동기·제어 결정 데이터를 안전하게 기록해 사고·아차 사고 조사를 돕도록 항공기 비행기록장치를 본떠 제안된 장치 또는 소프트웨어 모듈이다. [사실][^ref-1233]
- **잠금·표지(Lockout/Tagout, LOTO)** — 점검 전에 전원을 차단하고 기동스위치를 잠근 뒤 표지를 다는 절차다. 2026-09 경남 고성 식품 공장 사고에서 고용노동부 통영지청이 이 조치의 미실시를 지적했다. [사실][^ref-1238]
- **중상 보고(Severe Injury Report, SIR)** — 미국 OSHA 의 중상 보고로, 2015~2022년 보고에서 로봇 관련 사고 77건을 찾아 분석한 연구가 있다. [사실][^ref-1235]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30 (원문 미열람)
[^ref-1225]: The Robot Report, ISO 10218 industrial robot safety standard receives major overhaul, 2025-02, https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/, 접근일 2026-09-30
[^ref-1226]: IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2, 2026-09-18, https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2, 접근일 2026-09-30
[^ref-1233]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-09-30
[^ref-1235]: Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports, 2024, https://eprints.whiterose.ac.uk/id/eprint/217393/, 접근일 2026-09-30
[^ref-1238]: 경남도민일보, 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다, 2026-09-29, https://www.idomin.com/news/articleView.html?idxno=2015923, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-15 | 50. 안전 표준·인증·사고 조사 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-15/pages/topics/2026/2026-09-30-area50-s6.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술"
type: topic
category: "M. 안전"
primary_area_no: 50
related_areas: [4, 22, 37, 38, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1084, ref-1225, ref-1226, ref-1232, ref-1233, ref-1234, ref-1235, ref-1236, ref-1237, ref-1238, ref-563]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/safety-standards-certification-and-incident-investigation.md#6
---

[홈](../../index.md) › [주제](../index.md) › 50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술

# 50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 표준 적합성은 제조사·통합자·사용자가 역할을 나눠 맞추는 구조이고, 사고 원인 규명은 기록 장치와 증언을 결합하는 방법이 연구 단계로 제안되어 있다. [추정][^ref-1225][^ref-1084][^ref-1234]
- 이 페이지는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

표준 적합성은 제조사·통합자·사용자가 역할을 나눠 맞추는 구조이고, 사고 원인 규명은 기록 장치와 증언을 결합하는 방법이 연구 단계로 제안되어 있다. [추정][^ref-1225][^ref-1084][^ref-1234]

### 역할별 표준 적합성 경로

ISO 10218-1:2025 는 산업용 로봇 설계·제조(제조사 대상), ISO 10218-2:2025 는 로봇 적용·로봇 셀 설계·통합(통합자 대상)을 다루며, 2025-02 에 발행된 2011년판 이후 첫 개정이다. [사실][^ref-1225][^ref-1226] ANSI/A3 R15.08-2(2023)는 이동로봇 시스템 배치에서 통합자의 위험성평가, 제조사·통합자의 사용 정보 제공, 사용자의 교육·안전 작업 절차를 나누고, 사용자가 시스템을 개조하면 제조사·통합자 역할을 떠맡는다고 정한다. [사실][^ref-1084] 한계는 역할 경계가 표준마다 따로 정해져 여러 표준이 겹치는 현장에서 누가 무엇을 맞추는지 다시 정리해야 한다는 점이다. [추정][^ref-563]

### 사고 기록 장치

Winfield·van Maris·Salvini·Jirotka(2022)는 사회적 로봇의 센서·구동기·제어 결정을 안전하게 기록하는 윤리적 블랙박스의 공개 표준 초안을 논의용 첫 초안으로 내놓았다. [사실][^ref-1233] 기록할 데이터 형식과 보존 기간은 이번 조사에서 확인하지 못했다(미확인).

### 기록과 증언을 결합한 사고 조사

Webb 외(2021)는 사고 조사를 목격자 증언, 윤리적 블랙박스 기록, 해당 환경·로봇 전문가 분석, 기술·조직 권고로 구성하고 역할극 모의 사고로 시험했다(5절 가정 사례). [사실][^ref-1234] 이 방향의 바탕에는 사회적 로봇 사고를 항공·철도 사고 조사와 같은 엄격함으로 조사해야 한다는 Winfield 외(2020)의 주장이 있다. [의견][^ref-1232]

### 비정상 작업과 재가동 관리

확인한 사고 자료는 로봇 관련 중대 사고가 정상 운전보다 점검·수리·프로그램 수정 같은 비정상 작업 중에, 방책 안에서 주로 일어났음을 보여 준다(이 '주로'는 2011~2015 통계, 서울신문 2017-04-07 보도 기준, 보고서 원문 미확인). 재가동 경위가 조사 쟁점이 된 사례도 있다. 따라서 여러 로봇을 지휘하는 플랫폼에서는 정비·점검 상태와 재가동 명령의 권한·확인 이력을 남기는 것이 예방과 사후 조사 모두에 필요할 것으로 보인다. [추정][^ref-1236][^ref-1237][^ref-1238][^ref-1235]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30 (원문 미열람)
[^ref-1225]: The Robot Report, ISO 10218 industrial robot safety standard receives major overhaul, 2025-02, https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/, 접근일 2026-09-30
[^ref-1226]: IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2, 2026-09-18, https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2, 접근일 2026-09-30
[^ref-1232]: Winfield, A. F. T., Winkle, K., Webb, H., Lyngs, U., Jirotka, M., & Macrae, C. (arXiv), Robot Accident Investigation: a case study in Responsible Robotics, 2020-05, https://arxiv.org/abs/2005.07474, 접근일 2026-09-30
[^ref-1233]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-09-30
[^ref-1234]: Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI), Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions, 2021-06-29, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full, 접근일 2026-09-30
[^ref-1235]: Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports, 2024, https://eprints.whiterose.ac.uk/id/eprint/217393/, 접근일 2026-09-30
[^ref-1236]: 서울신문, [단독] 산업용 로봇 재해 위험 제조업보다 두 배 ... (제목 일부만 확인), 2017-04-07, https://www.seoul.co.kr/news/society/2017/04/07/20170407011011, 접근일 2026-09-30
[^ref-1237]: 경향신문, ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망, 2023-11-08, https://www.khan.co.kr/article/202311081103001, 접근일 2026-09-30
[^ref-1238]: 경남도민일보, 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다, 2026-09-29, https://www.idomin.com/news/articleView.html?idxno=2015923, 접근일 2026-09-30
[^ref-563]: Belzile, B., Wanang-Siyapdjie, T., Karimi, S., Braga, R. G., Iordanova, I., & St-Onge, D. (arXiv), From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, 2025-02-28, https://arxiv.org/abs/2502.20693, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-15 | 50. 안전 표준·인증·사고 조사 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-15/pages/topics/2026/2026-09-30-area50-s11.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사 — 열린 질문"
type: topic
category: "M. 안전"
primary_area_no: 50
related_areas: [4, 22, 37, 38, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-980, ref-992, ref-1230]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/safety-standards-certification-and-incident-investigation.md#11
---

[홈](../../index.md) › [주제](../index.md) › 50. 안전 표준·인증·사고 조사 — 열린 질문

# 50. 안전 표준·인증·사고 조사 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 표준 원문을 열지 못한 부분과 출처가 충돌한 부분은 질문으로 남긴다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

표준 원문을 열지 못한 부분과 출처가 충돌한 부분은 질문으로 남긴다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-170** (상태: 열림) ISO 3691-4:2023 의 운용 구역 분류와 사람 감지 요구가 이기종 플릿 관제 계층에 어떤 정보(구역·속도 제한·모드)를 요구하는지 표준 원문으로 확인할 수 있는가? 이번 조사에서도 표준 원문을 열지 못했다.
- **oq-186** (상태: 열림) 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시는 무엇이며, 경사로·알림음·등화장치 같은 기존 항목은 어느 항목에 흡수됐는가? 근거 고시가 제2023-211호임은 확인했으나 별표 원문은 확인하지 못했다. [사실][^ref-1230]
- **oq-230** (상태: 열림) 출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? 이번 조사에서도 두 값이 그대로 확인되었다. [사실][^ref-980][^ref-992]
- (새 질문, 번호는 게시 때 부여) 국내 KS B ISO 10218-1·-2 는 ISO 10218:2025 판을 언제 부합화하며, 산업안전보건기준에 관한 규칙의 협동로봇 방책 면제 인정 기준과 협동로봇 설치 작업장 안전인증은 새 판(로봇 분류·기능 안전 요구 변경)을 기준으로 바뀌는가?
- (새 질문) 여러 제조사 로봇을 지휘하는 플랫폼 수준에서 사고·아차 사고 조사에 필요한 최소 기록 항목(명령·정지·재가동·정비 모드 전환·상태 보고)을 정한 표준이나 공개 규약이 있는가, 윤리적 블랙박스 초안을 플릿 기록에 적용한 사례가 있는가?
- (새 질문) 2016년 이후 국내 로봇 관련 산업재해 통계를 고정형 산업용 로봇과 이동로봇(AMR·AGV)으로 나누어 집계한 공식 자료가 있는가?
- (새 질문) ISO/FDIS 13482 개정판은 여러 대가 함께 운영되는 서비스 로봇의 플릿 관제·승강기 연동·소프트웨어 갱신에 관한 안전 요구를 포함하는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: ZDNet Korea, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1230]: 산업통상자원부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시, 2023-11-17, https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-15 | 50. 안전 표준·인증·사고 조사 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-15/pages/topics/2026/2026-09-30-area50-s10.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사 — 다른 연구영역과의 연결"
type: topic
category: "M. 안전"
primary_area_no: 50
related_areas: [4, 22, 37, 38, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1084, ref-1225, ref-1226, ref-1227, ref-980, ref-992, ref-1230, ref-945, ref-1233, ref-1234, ref-1235, ref-1236, ref-1237, ref-1238, ref-563]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/safety-standards-certification-and-incident-investigation.md#10
---

[홈](../../index.md) › [주제](../index.md) › 50. 안전 표준·인증·사고 조사 — 다른 연구영역과의 연결

# 50. 안전 표준·인증·사고 조사 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 위험성평가·정지 절차, 인증 속성 등록, 사고 조사용 기록, 법정 인증·책임 분담을 매개로 여러 영역과 이어진다. 아래 연결은 이번 조사 결과를 세부영역 정의와 대조한 제안이다. [추정][^ref-1084][^ref-1233]
- 이 페이지는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 위험성평가·정지 절차, 인증 속성 등록, 사고 조사용 기록, 법정 인증·책임 분담을 매개로 여러 영역과 이어진다. 아래 연결은 이번 조사 결과를 세부영역 정의와 대조한 제안이다. [추정][^ref-1084][^ref-1233]

- [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) — 인증 상태와 허용 운행 조건(질량·속도)을 등록 속성으로 담는다. [추정][^ref-980]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 이동로봇의 승강기 탑승 안전 기준(KS B 7317)이 승강기 연동과 이어진다. [추정][^ref-945]
- [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) — 사고 조사에 쓸 명령·상태 기록을 남긴다. [추정][^ref-1233]
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) — 사고·아차 사고의 원인 분석 방법과 보고 서술의 구조화가 이어진다. [추정][^ref-1234][^ref-1235]
- [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) — 위험성평가와 정지·재가동 절차를 다룬다. [추정][^ref-1084][^ref-1238]
- [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) — ISO 10218:2025 에 합쳐진 협동 적용 요구를 자세히 다룬다. [추정][^ref-1225]
- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — 재가동 명령의 권한 통제와 이어진다. [추정][^ref-1238]
- [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) — ISO 10218:2025 가 더한 사이버보안 요구와 이어진다. [추정][^ref-1225]
- [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) — 배치 현장의 위험성평가와 이어진다. [추정][^ref-563]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 표준 판 개정(ISO 10218:2025, ISO/FDIS 13482) 추적과 이어진다. [추정][^ref-1226][^ref-1227]
- [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) — 제조사·통합자·사용자의 책임 분담과 이어진다. [추정][^ref-1084]
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — 법정 인증·보험·사고 조사와 이어진다. [추정][^ref-980][^ref-1230][^ref-1238]
- [61. 물류창고](../../categories/site-type-applications/warehouse.md) — 5절 물류창고 사고 사례와 이어진다. [추정][^ref-1237]
- [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md) — 5절 제조 공장 사고 사례와 국내 재해 통계와 이어진다. [추정][^ref-1236][^ref-1238]
- [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) — 5절 가정 모의 사고 조사와 이어진다. [추정][^ref-1234]
- [66. 실외](../../categories/site-type-applications/outdoor.md) — 5절 실외이동로봇 운행안전인증과 이어진다. [추정][^ref-980][^ref-992][^ref-1230]
- [67. 기타 현장](../../categories/site-type-applications/other-sites.md) — 5절 건설 현장 위험성평가와 이어진다. [추정][^ref-563]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30 (원문 미열람)
[^ref-1225]: The Robot Report, ISO 10218 industrial robot safety standard receives major overhaul, 2025-02, https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/, 접근일 2026-09-30
[^ref-1226]: IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2, 2026-09-18, https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2, 접근일 2026-09-30
[^ref-1227]: Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보, ISO/FDIS 13482 Robotics — Safety requirements for service robots, 미확인, https://iss.rs/en/project/show/iso:proj:83498, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: ZDNet Korea, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1230]: 산업통상자원부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시, 2023-11-17, https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view, 접근일 2026-09-30
[^ref-945]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-09-30
[^ref-1233]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-09-30
[^ref-1234]: Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI), Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions, 2021-06-29, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full, 접근일 2026-09-30
[^ref-1235]: Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports, 2024, https://eprints.whiterose.ac.uk/id/eprint/217393/, 접근일 2026-09-30
[^ref-1236]: 서울신문, [단독] 산업용 로봇 재해 위험 제조업보다 두 배 ... (제목 일부만 확인), 2017-04-07, https://www.seoul.co.kr/news/society/2017/04/07/20170407011011, 접근일 2026-09-30
[^ref-1237]: 경향신문, ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망, 2023-11-08, https://www.khan.co.kr/article/202311081103001, 접근일 2026-09-30
[^ref-1238]: 경남도민일보, 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다, 2026-09-29, https://www.idomin.com/news/articleView.html?idxno=2015923, 접근일 2026-09-30
[^ref-563]: Belzile, B., Wanang-Siyapdjie, T., Karimi, S., Braga, R. G., Iordanova, I., & St-Onge, D. (arXiv), From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, 2025-02-28, https://arxiv.org/abs/2502.20693, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-15 | 50. 안전 표준·인증·사고 조사 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-15/pages/topics/2026/2026-09-30-area50-s8.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사 — 대표 연구와 자료"
type: topic
category: "M. 안전"
primary_area_no: 50
related_areas: [4, 22, 37, 38, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1232, ref-1233, ref-1234, ref-1235, ref-563]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/safety-standards-certification-and-incident-investigation.md#8
---

[홈](../../index.md) › [주제](../index.md) › 50. 안전 표준·인증·사고 조사 — 대표 연구와 자료

# 50. 안전 표준·인증·사고 조사 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사고 기록·조사 연구는 사회적 로봇을 중심으로 방법을 제안하는 단계이고, 산업 현장 자료는 보고 서술의 구조화 부족을 드러낸다. [추정][^ref-1233][^ref-1235]
- 이 페이지는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사고 기록·조사 연구는 사회적 로봇을 중심으로 방법을 제안하는 단계이고, 산업 현장 자료는 보고 서술의 구조화 부족을 드러낸다. [추정][^ref-1233][^ref-1235]

- Winfield 외, Robot Accident Investigation: a case study in Responsible Robotics(2020) — 사고 조사 없는 사회적 로봇 개발은 항공 사고 조사 없는 항공만큼 무책임하다는 것이 Winfield 외(2020)의 주장이다. [의견][^ref-1232]
- Winfield·van Maris·Salvini·Jirotka, An Ethical Black Box for Social Robots: a draft Open Standard(2022) — 비행기록장치를 본뜬 로봇 기록 장치의 공개 표준 초안. [사실][^ref-1233]
- Webb 외, 역할극 증언 면담을 이용한 위험한 사람–로봇 상호작용 조사(Frontiers in Robotics and AI, 2021) — 증언·기록·전문가 분석을 결합한 조사 방법을 모의 사고로 시험했다. [사실][^ref-1234]
- Sanders·Sener·Chen, Robot-related injuries in the workplace(Applied Ergonomics 121, 2024) — OSHA 중상 보고 2015~2022년의 로봇 관련 사고 77건을 고정형 로봇 54건(부상 66건, 주로 손가락 절단과 머리·몸통 골절)과 이동로봇 23건(부상 27건, 주로 다리·발 골절)으로 나누어 분석했다. [사실][^ref-1235]
- Belzile 외, From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment(2025, 프리프린트) — 이동로봇 관련 표준 5종을 검토하고 건설 현장 배치용 위험성평가 틀을 제안했다. [사실][^ref-563]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1232]: Winfield, A. F. T., Winkle, K., Webb, H., Lyngs, U., Jirotka, M., & Macrae, C. (arXiv), Robot Accident Investigation: a case study in Responsible Robotics, 2020-05, https://arxiv.org/abs/2005.07474, 접근일 2026-09-30
[^ref-1233]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-09-30
[^ref-1234]: Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI), Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions, 2021-06-29, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full, 접근일 2026-09-30
[^ref-1235]: Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports, 2024, https://eprints.whiterose.ac.uk/id/eprint/217393/, 접근일 2026-09-30
[^ref-563]: Belzile, B., Wanang-Siyapdjie, T., Karimi, S., Braga, R. G., Iordanova, I., & St-Onge, D. (arXiv), From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, 2025-02-28, https://arxiv.org/abs/2502.20693, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-15 | 50. 안전 표준·인증·사고 조사 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-15/pages/topics/2026/2026-09-30-area50-s3.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사 — 왜 중요한가"
type: topic
category: "M. 안전"
primary_area_no: 50
related_areas: [4, 22, 37, 38, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1225, ref-1227, ref-980, ref-945, ref-1233, ref-1234, ref-1235, ref-1236]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/safety-standards-certification-and-incident-investigation.md#3
---

[홈](../../index.md) › [주제](../index.md) › 50. 안전 표준·인증·사고 조사 — 왜 중요한가

# 50. 안전 표준·인증·사고 조사 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 따를 안전 표준과 인증은 로봇 유형(산업용 ISO 10218, 이동 R15.08, 서비스 ISO 13482)과 현장·국가 조건(한국 실외 보도 운행 법정 인증, 승강기 탑승 KS B 7317)에 따라 갈리고 주요 표준이 2025~2026년에 개정 중이어서, 여러 제조사 로봇을 함께 운영하는 ROP는 적용 기준을 한 번 정하고 끝낼 수 없는 것으로 보인다. [추정][^ref-1225][^ref-1227][^ref-980][^ref-945]
- 이 페이지는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

따를 안전 표준과 인증은 로봇 유형(산업용 ISO 10218, 이동 R15.08, 서비스 ISO 13482)과 현장·국가 조건(한국 실외 보도 운행 법정 인증, 승강기 탑승 KS B 7317)에 따라 갈리고 주요 표준이 2025~2026년에 개정 중이어서, 여러 제조사 로봇을 함께 운영하는 ROP는 적용 기준을 한 번 정하고 끝낼 수 없는 것으로 보인다. [추정][^ref-1225][^ref-1227][^ref-980][^ref-945]

사고의 무게도 크다. 서울신문 2017-04-07 보도 기준(안전보건공단 산업안전보건연구원 보고서 원문 미확인)으로 2011~2015년 국내 산업용 로봇 재해자는 207명(사망 15명)이었고, 그중 134명(64.7%)이 수리·점검·준비·설치 작업 중에, 90.7%가 방책 안에서 다쳤다. [사실][^ref-1236] 같은 보도에서 평균 근로손실일수는 707.5일로 제조업 평균 351.7일의 약 두 배였다. [사실][^ref-1236]

사고 뒤 원인을 밝히는 방법은 아직 자리 잡지 않았다. 비행기록장치식 기록과 증언을 결합하는 방법이 연구 단계로 제안되었지만, 현행 보고 자료는 서술이 구조화되지 않아 원인 분석에 한계가 있는 것으로 보인다. [추정][^ref-1233][^ref-1234][^ref-1235] 미국 산업안전보건청(OSHA)의 중상 보고를 분석한 연구(2024)도 보고서 서술이 더 구조화되고 상세해야 한다고 결론지었다. [사실][^ref-1235]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1225]: The Robot Report, ISO 10218 industrial robot safety standard receives major overhaul, 2025-02, https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/, 접근일 2026-09-30
[^ref-1227]: Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보, ISO/FDIS 13482 Robotics — Safety requirements for service robots, 미확인, https://iss.rs/en/project/show/iso:proj:83498, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-945]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-09-30
[^ref-1233]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-09-30
[^ref-1234]: Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI), Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions, 2021-06-29, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full, 접근일 2026-09-30
[^ref-1235]: Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports, 2024, https://eprints.whiterose.ac.uk/id/eprint/217393/, 접근일 2026-09-30
[^ref-1236]: 서울신문, [단독] 산업용 로봇 재해 위험 제조업보다 두 배 ... (제목 일부만 확인), 2017-04-07, https://www.seoul.co.kr/news/society/2017/04/07/20170407011011, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-15 | 50. 안전 표준·인증·사고 조사 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1113건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 309개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explainable-mapf: 설명 가능한 다중 에이전트 경로 찾기 (Explainable Multi-Agent Path Finding (Explainable MAPF))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
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
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
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
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
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

### docs/open-questions.md (요약: 대상 영역 [50] 에 걸린 3건 / 전체 245건)

```markdown
- oq-170 [열림] ISO 3691-4:2023 의 운용 구역 분류와 사람 감지 요구가 이기종 플릿 관제 계층에 어떤 정보(구역·속도 제한·모드)를 요구하는지 표준 원문으로 확인할 수 있는가(이번 조사는 인증 기관 설명만 확인했다)? (영역 62, 50)
- oq-186 [열림] 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시는 무엇이며, 경사로·알림음·등화장치 같은 기존 항목은 어느 항목에 흡수됐는가? (영역 66, 50, 59)
- oq-230 [열림] 출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? (영역 49, 50)
```
