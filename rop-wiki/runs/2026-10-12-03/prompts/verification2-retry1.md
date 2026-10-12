(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-12-03
- date: 2026-10-12
- run_type: update (갱신)
- 대상: 60. 노동·수용성·접근성 (P. 거버넌스·법규·사회)
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
- retry_count: 1
- max_retries: 2

## 입력

### runs/2026-10-12-03/target.json

```json
{
  "run_id": "2026-10-12-03",
  "date": "2026-10-12",
  "weekday": "Mon",
  "run_number": 175,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 60,
    "area_name": "60. 노동·수용성·접근성",
    "category": "P. 거버넌스·법규·사회",
    "category_letter": "P"
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
  "selection_rationale": "CLI 지정 run_type=update, area=60"
}
```

### runs/2026-10-12-03/research.json

```json
{
  "run_id": "2026-10-12-03",
  "date": "2026-10-12",
  "run_type": "update",
  "target": {
    "area_no": 60,
    "area_name": "60. 노동·수용성·접근성",
    "category": "P. 거버넌스·법규·사회"
  },
  "gaps": [
    "섹션 4. 핵심 개념과 용어(분리 2026-09-30-area60-s4) — '노사협의회 협의 사항'(39행)이 법률 제16320호(2019) 기준이고 작업·휴게 시간(제7호)과 고용조정 일반원칙(제6호)이 없음. 작업자 수용성 설문 자료의 표본 조건 설명 없음",
    "섹션 5. 적용 사례 — 물류창고 사례(74행 Malik 면담)의 참여자 구성 미확인, 부상 지표가 GMU 발표 단일 근거이고 회사 발표·노조 보고서의 분모·정의 차이가 없음. 병원 사례가 한림대성심병원 자체 설문뿐이라 국내 독립 연구 없음. 실외 사례에 물품 인수 접근 요구 없음",
    "섹션 6. 대표 접근법과 기술(분리 2026-09-30-area60-s6) — 수용성 측정이 고령자·돌봄 모델(알메러·Q방법론)뿐이고 산업 작업자 척도·표본 한계 없음, 노동자 참여 절차에 노사 공동 검토기구 사례 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area60-s7) — 디지털 접근성 표준(WCAG 2.2, WCAG2ICT, EN 301 549, 유럽 접근성법)과 자동 검사 도구가 없음. 근로자참여법 행이 '현행 조문 여부 미확인'",
    "섹션 8. 대표 연구와 자료(분리 2026-09-30-area60-s8) — Acemoglu·Restrepo 항목(40행)에 JPE 2020 게재판의 총량·지역 효과 구분이 없고, 독일 등 비교 연구 없음. 수용성 연구들의 표본 조건(국가·언어·모집·인원) 미기재",
    "섹션 9. 책임 경계 — 화면 접근성의 범위(웹 관제·비웹 HMI·로봇 단말 닫힌 기능·물리 접근)와 휴게·작업 순환 정책의 노사 검토 연계가 없음",
    "섹션 11. 열린 질문(분리 2026-09-30-area60-s11) — oq-146·oq-188·oq-266·oq-278·oq-284~oq-287 이 모두 열림 상태",
    "정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: 근로자참여법 제20조 판(2022-12-11 시행 법률 제18927호), 메모의 SOC '비교창고 456시설' 오기, Acemoglu 범위값은 오류 아님(유지)"
  ],
  "research_questions": [
    "로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? [분류원문]",
    "공개된 작업자·산업 수용성 설문과 척도는 어떤 국가·언어·모집 방법·표본으로 만들어졌고, 한국 현장 작업자에게 일반화할 수 있는가? (섹션 4·6·8 겨냥)",
    "창고 로봇 도입의 안전 효과를 말하는 회사 발표와 노조 보고서는 지표 정의·분모·기간·범위가 어떻게 다른가(oq-286)? (섹션 5·9 겨냥)",
    "근로자참여법 제20조의 현행 판은 작업 배정·휴게·직무 전환을 협의 사항으로 두는가, 노사 공동 검토기구 사례는 무엇이 있는가(oq-285·oq-266)? (섹션 4·6·7 겨냥)",
    "웹 관제 화면, 비웹 HMI, 로봇 단말의 닫힌 기능에 각각 어떤 접근성 기준(WCAG 2.2, WCAG2ICT, EN 301 549, 유럽 접근성법)이 어떤 범위로 적용되고 자동 검사는 무엇을 놓치는가(oq-284)? (섹션 7·9 겨냥)",
    "장애인 이용자의 보행 접근과 물품 인수 접근, 국내 간호사 요구 연구는 어떤 조건에서 나온 결과인가(oq-188·oq-287)? (섹션 5·8 겨냥)",
    "로봇의 고용 효과 연구의 게재판 수치와 국가 간 차이는 무엇인가? (섹션 8 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Liu 외(Data in Brief 61, 2025)의 공개 작업자 설문 데이터셋은 미국·캐나다·영국·호주의 블루칼라 노동자 설문 참여자 530명 가운데 데이터 공개에 동의한 337명의 응답(40문항)만 담고 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1547"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.5~4.6 Recruitment/Survey Method: \"A total of 530 participants took part in the survey, of which 337 provided consent to release their data publicly.\" 초록: 337 complete responses to a 40-question survey. 공개 표본(337)은 전체 참여(530)와 다른 분모",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "이 설문의 모집 기간은 2022-04-05~2022-07-04 이며, 데이터셋 논문 발행(2025-06)과 3년 가까이 떨어져 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1547"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.5 Recruitment: \"Participants in this study were recruited between April 5, 2022 and July 4, 2022.\" 발행: Data in Brief 61, 111750(온라인 2025-06-03). 발행일과 조사일을 구분해 적을 것",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "이 표본은 4개 선진국(미국·캐나다·영국·호주)의 6개 업종(제조·소매·운송·배송·우편, 창고, 건설, 계약직) 회사 연락처로 이메일 모집한 군집 표본(무작위 아님)이고, 영어로만 설문했으며, 남성 응답이 여성의 약 2배, 18~40세가 약 3분의 2, 창고 종사자는 123명(36.5%)이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1547"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.5: \"Our study uses a cluster sampling strategy\" / 회사 연락처에 이메일 모집. \"The survey was administered in English\", \"nearly twice as many responses from male workers\". Table: Warehousing 123 (36.50 %). 아시아·아프리카·남미 응답자 없음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "Liu 외 데이터는 4개 영어권 선진국의 회사 연락망 표본이고 한국어 문항 타당화나 한국 작업자 응답이 없으므로, 한국 산업 현장 작업자 수용성의 대리값으로 일반화할 근거가 없다. 40문항도 안전·동료·로봇 협업·데이터 프라이버시를 나눠 묻는 문항 묶음이지 단일 수용성 점수로 타당화된 척도가 아니다.",
      "tag": "추정",
      "source_ids": [
        "ref-1547"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1~f3 의 표본 조건(4개국·영어·군집 모집·남성 편중)에서 도출. 초록 문항 구성: demographics 7, physical safety 8, human coworkers 6, working with robots 16, data privacy 3",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "Malik 외(2026) 창고 작업자 연구에서 이번에 확인된 것은 초록의 'N = 12 semi-structured interviews' 뿐이다. 외부 메모가 적은 참여자 국가(영국 창고 근무 경험)·역할 구성(비관리 5명/관리·리더 7명)·로봇 사용 경험(7명)은 원문(Springer·KCL 저장소)이 접속 차단돼 확인하지 못했으므로, 5절 74행 문장은 그대로 두고 참여자 구성을 덧붙이지 않는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1226"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "독립 검증: 초록 \"N = 12 semi-structured interviews\" 만 확인. Springer 본문·KCL accepted manuscript 모두 Cloudflare 차단(원문 미열람). 메모 F04 의 '영국', F05, F06 은 확인 불가라 사실로 쓰지 않음. 12명이 모두 비관리 현장 작업자인지도 미확인",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f6",
      "claim": "포르투갈어판 산업 맥락 수용성 척도(FSQ-IC) 검증 연구(Pinto 외 6인, Human Behavior and Emerging Technologies 2025)는 연구진 네트워크 연락처로 배포한 온라인(LimeSurvey) 횡단 조사이며, 비확률 편의·눈덩이 표본 346명을 썼다.",
      "tag": "사실",
      "source_ids": [
        "ref-1548"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§3.1 Study Design and Sample: \"This study followed a cross-sectional design, involving a sample of 346 participants. The questionnaire was distributed through our network contacts … online LimeSurvey platform.\" §6 한계: convenience sampling. Article ID 8816379, 2025-01-17",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "같은 논문의 표 1·2 는 탐색적 요인분석(EFA) 표본을 140명, 확인적 요인분석(CFA) 표본을 210명으로 적고, 이 가운데 로봇을 다뤄 본 적 없는 응답자가 각각 102명, 147명이다. 원문은 40%/60% 분할이라고 적지만 140+210=350 으로 §3.1 의 346명과 맞지 않아 원문 자체가 불일치한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1548"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Table 1 Total 140 / 102, Table 2 Total 210 / 147. 본문 '40%/60%' 분할. 346 vs 350 차이는 원문 내 불일치이며 어느 쪽이 맞는지 확인 못 함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "FSQ-IC 검증 표본은 포르투갈어를 읽는 일반 성인 중심이고 로봇 무경험자가 다수(분석 표본의 약 70~73%)라서, 제목의 '산업 맥락'만으로 산업 현장 작업자에게서 검증된 척도로 볼 수 없고 한국 현장 작업자에게 그대로 옮길 근거도 없다.",
      "tag": "추정",
      "source_ids": [
        "ref-1548"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f6·f7 에서 도출(102/140, 147/210). 저자 §6 도 척도가 개발 중이며 안전 우려를 충분히 포괄하지 못할 수 있다고 적음. 한국어 인지면담·직군별 타당화 연구는 확인하지 못함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "Amazon 은 2026-03-12 자사 발표(2026-03-27 수정)에서 전 세계 운영의 기록대상 사고율(Global RIR)이 지난 6년간(2019 대비) 43%, 휴업 사고율(Global LTIR)이 70% 개선됐다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-1549"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: \"Global Recordable Incident Rate (RIR) has improved 43% and Global Lost Time Incident Rate (LTIR) has improved 70% over the past six years.\" 전년 대비 각 14%. 회사 자체 발표이며 로봇 도입 효과를 분리한 수치가 아님. datePublished 2026-03-12, dateModified 2026-03-27",
      "as_of": "2026-10-12",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f10",
      "claim": "Strategic Organizing Center(SOC)의 2025-05 보고서는 Amazon 과 다른 사업주가 2020~2024년 매년 OSHA 에 제출한 부상·질병 자료를 분석했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1550"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Overview(인쇄 p.2): \"SOC's analysis is based on data that Amazon and other employers provided to OSHA annually from 2020 to 2024.\" 2024년 Amazon 1,172개 창고·물류·배송 시설 보고",
      "as_of": "2026-10-12",
      "site_type": "물류창고",
      "flow_item": "예외·성과"
    },
    {
      "id": "f11",
      "claim": "SOC 보고서는 '중대 부상'을 경작업 전환(light duty) 또는 휴업(lost time)을 초래한 부상으로 분류한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1550"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Overview(인쇄 p.2): \"… categorized as either light duty or lost time injuries—that is, injuries where workers were hurt so badly that they were either unable to perform …\". GMU 발표(ref-1213)의 중대/비중대 구분과 같은 정의인지는 확인 못 함",
      "as_of": "2026-10-12",
      "site_type": "물류창고",
      "flow_item": "예외·성과"
    },
    {
      "id": "f12",
      "claim": "SOC 의 창고 비교는 Amazon 이 2024년 OSHA 보고에서 일반 창고·보관업(NAICS 493110)으로 분류한 Amazon 자체 시설 456곳의 부상률을 비(非)Amazon 창고 전체와 비교한 것이며, 2024년 중대 부상률은 100명당 5.9 대 3.0 이었다. 외부 메모의 '비교 창고 456시설'은 틀린 표현이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1550"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"SOC also analyzed injury rates at the subset of 456 facilities categorized by Amazon under the General Warehouse and Storage industry (NAICS 493110) … compared … with all non-Amazon warehouse facilities\"; \"5.9 per 100 workers compared to 3.0 per 100 workers\"",
      "as_of": "2026-10-12",
      "site_type": "물류창고",
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "SOC 는 보고서에서 스스로 SEIU(서비스노조)·CWA(미국통신노조)·UFW(농장노동자연합)와 협력하는 노동 조직이라고 밝히므로, 이 보고서는 노동조합 쪽 이해당사자 자료다.",
      "tag": "사실",
      "source_ids": [
        "ref-1550"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "About: \"We partner with workers and our affiliates—the Service Employees International Union (SEIU), Communication Workers of America (CWA), and the United Farmworkers of America (UFW)\"",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "Amazon 발표(전 세계·2025 기준·2019 대비 개선율)와 SOC 보고서(미국·2024·비Amazon 창고 대비 수준)는 범위·기간·지표·분모가 다르고 같은 OSHA 신고 자료에 일부 기초하며 양쪽 모두 이해당사자 자료이므로, 서로 독립된 교차 확인이나 단순 모순으로 셀 수 없다. 로봇 센터만의 부상 효과도 어느 쪽에서도 분리되지 않는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1549",
        "ref-1550"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f9~f13 에서 도출. 위키의 Burtch 외 40%/77%(ref-1213)는 이번에도 원논문 방법을 열지 못해 재검증하지 않음",
      "as_of": "2026-10-12",
      "site_type": "물류창고",
      "flow_item": "예외·성과"
    },
    {
      "id": "f15",
      "claim": "2026-10-12 국가법령정보센터에서 연 근로자참여 및 협력증진에 관한 법률 제20조 [시행 2022. 12. 11.] [법률 제18927호, 2022. 6. 10., 일부개정]의 제1항 제7호는 '작업과 휴게 시간의 운용'을 노사협의회가 협의하여야 할 사항으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1551"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제20조(협의 사항) ① \"협의회가 협의하여야 할 사항은 다음 각 호와 같다. <개정 2019. 4. 16.>\" … \"7. 작업과 휴게 시간의 운용\". 협의 사항이며 의결·동의 사항이 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "같은 판 제20조 제1항 제6호는 '경영상 또는 기술상의 사정으로 인한 인력의 배치전환ㆍ재훈련ㆍ해고 등 고용조정의 일반원칙'을 협의 사항으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1551"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제20조① \"6. 경영상 또는 기술상의 사정으로 인한 인력의 배치전환ㆍ재훈련ㆍ해고 등 고용조정의 일반원칙\"",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "2022년판(법률 제18927호) 제20조 제1항에도 위키가 인용한 제2호(근로자의 채용ㆍ배치 및 교육훈련), 제9호(신기계ㆍ기술의 도입 또는 작업 공정의 개선), 제14호(사업장 내 근로자 감시 설비의 설치)가 같은 문구로 있으며, 제1항의 마지막 개정 표시는 '<개정 2019. 4. 16.>'이다. 따라서 4·7절의 '법률 제16320호 기준, 현행 여부 미확인'은 2022-12-11 시행판 기준으로 갱신할 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1551"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ref-1551 원문: 2. 근로자의 채용ㆍ배치 및 교육훈련 / 9. 신기계ㆍ기술의 도입 또는 작업 공정의 개선 / 14. 사업장 내 근로자 감시 설비의 설치. 위키의 기존 근거 ref-1220(케이스노트 2019판)과 문구 비교만 했고 재열람하지 않음. 열람일 이후 개정 여부는 확인하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "근로자참여법 제20조는 협의 사항을 열거할 뿐이므로, ROP 의 작업 배정·휴게 반영 정책이나 개별 작업자 처리량·위치 로그가 제6·7·14호 협의 대상에 해당하는지는 조문만으로 정해지지 않으며 판례·행정해석은 이번에도 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1551"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "조문이 말하는 범위(협의 사항 열거)만 사실. 적용·해석(감시 설비 해당성, 도입 전 협의 시점)은 확인 못 함(oq-285 부분 답)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "ILO Working Paper 144(2025-07, Cornell University ILR School 소속 저자 5인)는 IBM 독일의 AI 기본협약이 AI 전문가와 사용자·근로자 대표로 구성된 AI 윤리위원회를 두고, 이 위원회가 AI 적용을 평가하고 협약 이행을 감독하며 AI 도구에 대한 직원 이의·불만을 논의하고 AI 권고를 검토·수정한다고 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1552"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IBM Germany 사례(인쇄 p.48): \"The agreement also establishes an AI Ethics Council made up of AI experts and employer and employee representatives, which evaluates AI applications and oversees implementation …\" 저자: Doellgast, Appalla, Ginzburg, Kim, Thian(모두 Cornell ILR)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "ILO Working Paper 144 는 ILO 공식 입장이 아니라 저자 견해를 담은 작업논문이며(면책 문구), 면담과 문헌에 기초한 질적 사례 연구다. 협약 원문을 싣지 않았고 IBM 면담 날짜가 각주 206(2021-11-08)과 부록 1(2024-07-26)에서 다르다. 사업장협의회 위원들이 협약이 안전보건과 AI 수용을 개선했다고 '느꼈다'는 서술도 측정된 효과가 아니다.",
      "tag": "추정",
      "source_ids": [
        "ref-1552"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "p.ii \"The opinions and views expressed in this publication are those of the author(s) and do not necessarily …\". p.48 \"Works councilors … felt that these agreements had improved workplace health and safety\". 2025-07-10 발행일은 확인 불가(PDF 표지 July/2025)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "WCAG 2.2(W3C 권고, 2024-12-12판) AA 성공기준 2.5.7(Dragging Movements)은 드래그가 필수이거나 기능이 사용자 에이전트가 정하고 저자가 수정하지 않은 경우가 아니면, 드래그로 하는 모든 기능을 드래그 없이 단일 포인터로 수행할 수 있어야 한다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1553"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "SC 2.5.7 Dragging Movements (Level AA): \"single pointer without dragging\" 예외 2개(Essential, 사용자 에이전트 결정). 웹 콘텐츠 적합성 기준이며 개별 ROP 의 법적 의무를 정하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "WCAG 2.2 AA 성공기준 2.5.8(Target Size (Minimum))은 간격(Spacing)·동등한 대체(Equivalent)·인라인(Inline)·사용자 에이전트(User Agent Control)·필수(Essential) 다섯 예외를 빼면 포인터 입력 대상의 크기를 최소 24×24 CSS 픽셀로 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1553"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "SC 2.5.8: \"The size of the target for pointer inputs is at least 24 by 24 CSS pixels, except when:\" Spacing / Equivalent / Inline / User Agent Control / Essential. CSS 픽셀은 로봇 본체 물리 버튼 치수가 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "WCAG2ICT(W3C Group Note, 2025-12-11)는 WCAG 2 를 비웹 문서·소프트웨어에 적용하는 방법에 대한 정보성 안내이며, 규범이 아니고 요구사항을 정하지 않는다고 스스로 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1556"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Abstract/Introduction: \"It provides informative guidance (guidance that is not normative and does not set requirements).\" 표지 'W3C Group Note'. 어떤 성공기준을 법적으로 적용할지 정하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "WCAG2ICT 는 제품의 하드웨어 측면은 다루지 않는다고 적용 범위에서 제외한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1556"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Excluded from Scope: \"This document does not comment on hardware aspects of products, because the basic constructs on which WCAG 2 is built do not apply to these.\" 로봇 본체·물리 접근은 이 문서 범위 밖",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "EN 301 549 의 최종판은 V4.1.1(2026-09, ETSI 배포본 04.01.01_60)이며, 2025-11 의 V4.1.0(04.01.00_20·_30)은 초안 단계 문서다. V4.1.1 머리말은 이 문서가 지침 (EU) 2019/882 를 위한 표준화 요청 C(2022) 6456 에 따라 준비됐고, EU 관보에 인용되면 적합성 추정을 준다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1555"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "표지 \"EN 301 549 V4.1.1 (2026-09)\". Foreword: \"Once the present document is cited in the Official Journal of the European Union under that Directive, compliance … confers … a presumption of conformity\". V4.1.1 의 관보 인용 여부는 확인 못 함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "EN 301 549 V4.1.1 제5.1.5절은 닫힌 기능(closed functionality)을 쓰는 데 청각 출력이 필요하면 그 청각 정보와 동등한 시각 정보를 제공하도록 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1555"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "5.1.5 Visual output for auditory information(p.34): \"Where ICT includes closed functionality, and auditory output is needed … the ICT shall provide visual information that is equivalent to the auditory information.\"",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "EN 301 549 V4.1.1 제5.1.7절은 닫힌 기능을 조작하는 데 음성이 필요하면 음성을 요구하지 않는 대체 입력 방식의 조작 모드를 적어도 하나 제공하도록 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1555"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "5.1.7 Access without speech(p.35): \"… the ICT shall provide at least one mode of operation using an alternative input mechanism that does not require speech.\" 닫힌 기능 조건이 없는 로봇에 일률 적용하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "유럽 접근성법(지침 (EU) 2019/882) 제2조 제1항 (b)는 2025-06-28 이후 출시되는 무인 단말기 가운데 (i) 결제 단말기는 한정 없이 열거하고, (ii) 현금자동인출기·발권기·체크인기·정보 제공 대화형 무인 단말기는 '이 지침이 다루는 서비스 제공 전용'인 것으로 한정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1554"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Art. 2(1): \"This Directive applies to the following products placed on the market after 28 June 2025\" (b)(i) \"payment terminals\"; (ii) \"the following self-service terminals dedicated to the provision of services covered by this Directive\"(차량·항공기 등 일체형 단말 제외)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "같은 지침 제15조 제1항은 EU 관보에 참조가 게재된 조화 표준(또는 그 일부)에 부합하는 제품·서비스가 그 표준이 다루는 범위에서 이 지침의 접근성 요구에 부합하는 것으로 추정된다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1554"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Art. 15(1): \"… harmonised standards … the references of which have been published in the Official Journal of the European Union, shall be presumed to be in conformity … in so far as those standards or parts thereof cover those requirements.\"",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f30",
      "claim": "로봇 본체 터치스크린, 기업용(B2B) 관제 화면, 작업자 HMI 가 지침 2019/882 제2조의 열거 제품·서비스에 드는지는 조문만으로 정해지지 않는다. 결제 기능이 있는 로봇 단말은 (i) 결제 단말기 해당 여부를, 정보 안내 화면은 (ii) 의 '서비스 제공 전용' 요건을 따로 검토해야 하는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1554"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f28 에서 도출. 해당성 판단 사례·가이드는 확인 못 함. 국내 무인정보단말기 해당성(oq-284)과는 별개 법역",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f31",
      "claim": "axe-core v4.14.0 태그(CHANGELOG 2026-10-05)의 target-size 규칙 정의에는 'wcag22aa'·'wcag258'·'EN-301-549v4'·'EN-9.2.5.8' 태그가 붙어 있고 \"enabled\": false 로 설정돼 있다.",
      "tag": "추정",
      "source_ids": [
        "ref-1557"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Deque 저장소 lib/rules/target-size.json(v4.14.0): \"enabled\": false, tags [\"cat.sensory-and-visual-cues\",\"wcag22aa\",\"wcag258\",\"EN-301-549v4\",\"EN-9.2.5.8\"]. Deque 저장소 단독 근거라 [추정]",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f32",
      "claim": "enabled:false 이므로 target-size 규칙은 axe-core 기본 실행에서 빠지는 것으로 보이며, EN 301 549 태그를 지정해 실행할 때 이 규칙이 켜지는지는 설정에 달려 있어 실행 시험으로 확인하지 않았다. README 는 자동 판단이 불확실한 항목을 incomplete 로 돌려 수동 검토가 필요하다고 안내한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1557"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: README \"incomplete\" … \"manual review is needed\". 규칙의 존재와 기본 실행은 다름. 실제 프로젝트에서 runOnly/rules 설정으로 실행해 보지 않음. README 의 57% 자동 검출 주장은 독립 재현이 없어 쓰지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f33",
      "claim": "Choo·Lee 의 Delphi 연구(Healthcare Informatics Research 32(1), 2026-01)는 서울의 한 상급종합병원 신경과 병동 6명과 뇌졸중 집중치료실 8명, 경력 7년 초과 간호사 14명을 전문가 패널로 3라운드 합의를 구했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1558"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"this study surveyed 14 nurses working in the neurology ward and stroke intensive care unit of a tertiary …\"; II.2 Delphi Panel(p.61): \"14 nurses with more than seven years of ex[perience]\"; 3 rounds. 단일 기관·편의 모집 한계(IV)",
      "as_of": "2026-10-12",
      "site_type": "병원",
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "이 Delphi 설문은 2022-11-07 부터 2023-04-12 까지 실시됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1558"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "II.4 Data Collection(p.61): \"The Delphi survey was conducted from November 7, 2022, to April 12, 2023.\" 발행(2026-01)과 조사 시점 구분",
      "as_of": "2026-10-12",
      "site_type": "병원",
      "flow_item": null
    },
    {
      "id": "f35",
      "claim": "Choo·Lee 연구는 급성 뇌졸중 환자 돌봄에 동반 로봇을 쓰는 미래 시나리오에 대한 단일 기관 간호사 14명의 전문가 합의이며, 로봇 도입 뒤 수용률이나 간호 업무 변화를 측정한 연구가 아니다. 따라서 한국 병원 간호사 일반이나 한림대성심병원 자체 설문(ref-1222)의 독립 재현으로 볼 수 없다.",
      "tag": "추정",
      "source_ids": [
        "ref-1558"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f33·f34 에서 도출. 저자 한계: convenience sampling, 단일 기관. 국내 병원·물류창고 종사자의 도입 후 독립 측정 연구(oq-287)는 여전히 찾지 못함",
      "as_of": "2026-10-12",
      "site_type": "병원",
      "flow_item": null
    },
    {
      "id": "f36",
      "claim": "Han 외(CHI 2024)의 이동장애인 15명·로봇 실무자 8명 면담과 짝 공동설계 워크숍은 모두 화상회의로 진행됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1214"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§3 Methods: \"All the activities were held over video conference. Interviews lasted 60–80 minutes and co-design workshops lasted 90 minutes.\" 15/8/4 숫자는 위키 기존 내용(5절 실외)",
      "as_of": "2026-10-12",
      "site_type": "실외",
      "flow_item": null
    },
    {
      "id": "f37",
      "claim": "Han 외 저자들은 자신들의 질적 결과와 제안한 상호작용을 실제 환경에서 평가할 필요가 남아 있다고 명시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1214"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§7.1: \"Nonetheless, there remains a pressing need to test these interactions and qualitative findings in real-world evaluations.\"",
      "as_of": "2026-10-12",
      "site_type": "실외",
      "flow_item": null
    },
    {
      "id": "f38",
      "claim": "Boadi-Agyemang 의 CMU 박사논문(CMU-RI-TR-26-106, 2026-06) 4장의 배송 로봇 공동설계는 2025년 미국 Pittsburgh 에서 2개월간 지역 모집한 장애 성인 14명(여성 9·남성 5, 31~75세, 시각·청각·이동 장애 중심)과 진행했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1559"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.3.1: \"We recruited 14 local participants (9 women, 5 men) who were between 31 and 75 years old\" 커뮤니티 센터·지역 장애 단체 등으로 모집. \"This work was conducted in Pittsburgh, a medium-sized U.S. city, over a two-month period in 2025.\"",
      "as_of": "2026-10-12",
      "site_type": "실외",
      "flow_item": null
    },
    {
      "id": "f39",
      "claim": "Boadi-Agyemang 연구 참여자들은 보행 중 로봇과의 통행 우선권과 별개로, 손을 뻗기 어려운 이동장애인이 물품을 인수할 때는 로봇과 가까이 상호작용하는 것이 중요하다고 보았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1559"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.4.3(인쇄 p.70): \"Close interactions were seen as critical for facilitating handovers with PwMDs for whom reaching can be difficult.\" 참여자 인용: 휠체어 이용자는 휴대폰 스캔·물건 꺼내기를 위해 로봇에 더 가까이 가야 함",
      "as_of": "2026-10-12",
      "site_type": "실외",
      "flow_item": "완료·인계"
    },
    {
      "id": "f40",
      "claim": "통행 중 충분한 간격(연석 경사로 비우기)과 물품 인수 때의 근접은 같은 이용자 집단 안에서도 상황별로 다른 요구다. 두 연구 모두 미국 소수 참여자의 요구·설계 연구이고 실제 배송의 접근 성공률을 측정하지 않았으며, 같은 CMU 계열이라 독립 교차 확인으로 세지 않는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1214",
        "ref-1559"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f36~f39 에서 도출. 국내 점자블록·연석 대기 위치 인증 항목(oq-188)은 확인 못 함",
      "as_of": "2026-10-12",
      "site_type": "실외",
      "flow_item": null
    },
    {
      "id": "f41",
      "claim": "위키 8절의 Acemoglu·Restrepo 범위값(노동자 1천 명당 로봇 1대 증가 시 고용인구비율 약 0.18~0.34%p, 임금 0.25~0.5% 감소)은 NBER 작업논문 w23285(2017-03) 초록과 일치하므로 틀린 값이 아니며 유지한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1223"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "NBER 초록: \"one more robot per thousand workers reduces the employment to population ratio by about 0.18-0.34 percentage points and wages by 0.25-0.5 percent.\" Issue Date March 2017. 수정이 아니라 JPE 게재판 수치 추가 대상",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f42",
      "claim": "Journal of Political Economy 128(6):2188–2244(2020-06) 게재판은 공간 파급을 반영한 미국 총량 효과로, 노동자 1천 명당 로봇 1대 증가가 고용인구비율을 약 0.2%p, 임금을 약 0.42% 낮춘다고 추정했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1560"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Introduction: \"… reduces the aggregate employment-to-population ratio by about 0.2 percentage points and wages by about 0.42%\". MIT 저자 보관 게재본으로 열람. 온라인 게재일(2020-04-22)은 확인 못 함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f43",
      "claim": "같은 JPE 게재판은 1990~2007년 미국 722개 통근권역 자료에서, 로봇 스톡 증가(1993~2007년 노동자 1천 명당 약 1대)가 로봇 노출이 없는 통근권역 대비 평균 고용인구비율을 0.39%p, 평균 임금을 0.77% 낮췄다고 추정했다(지역 효과).",
      "tag": "사실",
      "source_ids": [
        "ref-1560"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Introduction: \"reduced the average employment-to-population ratio in a commuting zone by 0.39 percentage points and average wages by 0.77% (relative to a commuting zone with no exposure to robots)\"; §III \"the 722 commuting zones\". 지역 효과와 총량 효과(f42)를 구분",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f44",
      "claim": "Dauth 외(Journal of the European Economic Association 19(6), 2021)는 1994~2014년 독일 행정자료로 같은 추정 전략을 재현했을 때 로봇 노출이 총고용을 줄이는 음(-)의 효과를 찾지 못했고, 제조업 일자리 감소를 서비스업(특히 기업 대상 지역 서비스)의 새 노동 수요가 상쇄했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1561"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§1(저자 2021-01-21판): \"We find no such negative effects of predicted robot exposure on total employment in Germany … new labor demand in the service sector … leads to an offsetting force.\" 출판 최종판과의 완전 동일성은 확인 못 함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f45",
      "claim": "미국(1990~2007, 통근권역)과 독일(1994~2014, 402개 지역·행정자료) 결과는 국가·시기·자료·노동 이동 조건이 달라 같은 주장의 재현이나 반박으로 볼 수 없고, 어느 쪽도 한국이나 개별 로봇 플릿 현장의 고용 효과를 측정한 것이 아니다.",
      "tag": "추정",
      "source_ids": [
        "ref-1560",
        "ref-1561"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f42~f44 에서 도출. 두 연구는 IFR 기초자료와 shift-share 계열 추정 전략을 일부 공유해 독립 교차 확인으로 세지 않음. 한국노동연구원 수치(ref-1215 보도)는 원표 미열람으로 [추정] 유지",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f46",
      "claim": "ROP 도입 전후 작업자 조사는 수용 의향, 실제 사용, 거부·우회, 도움 요청, 감시 우려를 별도 지표로 나누고, 응답 집단(관리자/비관리 작업자, 로봇 경험 유무)과 표본 조건(국가·언어·모집 방법·조사 시점·공개 동의 분모)을 결과와 함께 기록해야 한다. 해외 척도는 한국어 인지면담과 직군별 타당화를 거친 뒤 문항원으로만 쓴다.",
      "tag": "의견",
      "source_ids": [
        "ref-1547",
        "ref-1548",
        "ref-1558"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1~f8·f33~f35 에서 도출. 이 위키 구축자의 의견",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f47",
      "claim": "플릿 도입 효과를 평가할 때는 사고 분류 정의(경작업 전환·휴업 포함 여부), 노출 시간 분모, 직군, 로봇 공정 여부, 전환 작업을 함께 기록하고, 회사 발표와 노조 보고서 같은 이해당사자 자료의 출처를 표시해야 한다. 처리량 증가나 안전감 설문을 실제 부상 감소의 대리값으로 쓰지 않는다.",
      "tag": "의견",
      "source_ids": [
        "ref-1549",
        "ref-1550"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f9~f14 에서 도출",
      "as_of": "2026-10-12",
      "site_type": "물류창고",
      "flow_item": "예외·성과"
    },
    {
      "id": "f48",
      "claim": "ROP 스케줄러의 휴게 반영·작업 순환·직무 전환 정책 변경은 노사협의 기록(근로자참여법 제20조 제6·7호 협의 여부)과 연결해 이력으로 남기고, 작업자 데이터·자동 배정에 대한 이의 제기와 처리 결과를 변경 관리에 묶어야 한다. 법적 해당성 판단은 ROP 가 하지 않고 외부 결정을 제약으로 받는다.",
      "tag": "의견",
      "source_ids": [
        "ref-1551",
        "ref-1552"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f15~f20 에서 도출",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f49",
      "claim": "접근성 시험은 브라우저 관제 화면(WCAG 2.2: 드래그 대체 조작, 24×24 CSS px 대상), 비웹 작업자 프로그램(WCAG2ICT 는 안내일 뿐), 로봇 단말의 닫힌 기능(EN 301 549 5.1.5·5.1.7: 시각 경보 동등성, 음성 외 입력), 로봇 본체 물리 접근으로 범위를 나누고, 자동 검사 보고서에는 도구 버전·규칙 ID·활성화 설정을 남긴 뒤 키보드·스크린리더·실사용자 수동 검사를 더한다. 기술 시험 통과와 법적 적용 판단은 별도 기록으로 둔다.",
      "tag": "의견",
      "source_ids": [
        "ref-1553",
        "ref-1556",
        "ref-1555",
        "ref-1554",
        "ref-1557"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f21~f32 에서 도출. 다중 로봇 지도에서 드래그로 작업을 배정하는 기능에는 버튼·목록형 대체 조작이 필요",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f50",
      "claim": "플릿 경로·작업 모델은 보도 통행, 대기, 물품 인수 모드를 나누어, 통행·대기 중에는 연석 경사로를 비우고 간격을 두되 인수 때는 접근 가능한 위치·높이·입력 수단과 근접 허용을 작업 배정 조건으로 다뤄야 한다. 근접 허용은 이용자 요청과 현장 안전 평가를 전제로 시험한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1214",
        "ref-1559"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f36~f40 에서 도출",
      "as_of": "2026-10-12",
      "site_type": "실외",
      "flow_item": "완료·인계"
    },
    {
      "id": "f51",
      "claim": "국가 단위 로봇 노출 계수로 개별 플릿의 감원 인원을 계산하지 말고, 현장 도입 평가에서는 기존 작업자의 직무 전환, 신규 채용, 외주 전환을 구분해 수용성 조사와 함께 기록하는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1560",
        "ref-1561"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f41~f45 에서 도출",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1547",
      "org": "Liu, Y. (A.), Kaur, G., Banerjee, N. K., Banerjee, S. (Clarkson University·Wright State University) — Data in Brief 61",
      "title": "Dataset of worker perceptions of workforce robotics regarding safety, independence, job security, and privacy",
      "published": "2025-06-03",
      "url": "https://doi.org/10.1016/j.dib.2025.111750",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "미국·캐나다·영국·호주 6개 업종 블루칼라 노동자 대상 영어 온라인 설문(2022-04-05~07-04, 군집 모집) 530명 중 공개 동의 337명의 40문항 응답 데이터셋. PMC 전문으로 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12210288/",
      "source_unopened": false
    },
    {
      "id": "ref-1548",
      "org": "Pinto, A., Lemos, L., Carvalho, C., Santos, J., Menezes, P., Nomura, T. — Human Behavior and Emerging Technologies",
      "title": "Translation, Adaptation, and Validation in Portuguese of an Acceptance Scale for Human–Robot Interaction in an Industrial Context",
      "published": "2025-01-17",
      "url": "https://doi.org/10.1155/hbe2/8816379",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "FSQ-IC 포르투갈어판 검증 연구(Article ID 8816379). 네트워크 연락처 편의·눈덩이 온라인 표본 346명(EFA 140/CFA 210, 로봇 무경험 다수)이며 표본 수가 원문 안에서 불일치한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1549",
      "org": "Amazon (Sarah Rhoads, VP Global Workplace Health & Safety)",
      "title": "Amazon delivers another strong year of safety progress, making our workplaces even safer for our employees",
      "published": "2026-03-12",
      "url": "https://www.aboutamazon.com/news/workplace/amazon-workplace-safety-2025-injury-reduction",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "Amazon 자사 발표(2026-03-27 수정). 전 세계 운영의 기록대상 사고율 43%, 휴업 사고율 70% 개선(6년, 2019 대비)을 주장한다. 로봇 효과를 분리한 수치가 아니다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1550",
      "org": "Strategic Organizing Center (SOC; SEIU·CWA·UFW 연계 노동 조직)",
      "title": "Failure to Deliver: Amazon Falls Short on Safety",
      "published": "2025-05",
      "url": "https://thesoc.org/wp-content/uploads/2025/05/May-2025_Strategic-Organizing-Center_Report-x-Failure-To-Deliver.pdf",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "2020~2024년 OSHA 제출 자료로 Amazon 창고 부상률을 분석한 노동조합 측 이해당사자 보고서. 중대 부상=경작업 전환·휴업, Amazon NAICS 493110 시설 456곳과 비Amazon 창고 전체를 비교한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1551",
      "org": "법제처 국가법령정보센터 (대한민국, 법률 제18927호)",
      "title": "근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) [시행 2022. 12. 11.] [법률 제18927호, 2022. 6. 10., 일부개정]",
      "published": "2022-06-10",
      "url": "https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017145541",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "노사협의회 협의 사항 17개 호를 정한 조문. 2026-10-12 열람판은 2022-12-11 시행 법률 제18927호이며 제1항은 2019-04-16 개정 표시. 기존 ref-1220(케이스노트 2019판)의 후속 판.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1552",
      "org": "Doellgast, V., Appalla, S., Ginzburg, D., Kim, J., Thian, W. L. (Cornell University ILR School) — ILO Working Paper 144",
      "title": "Global case studies of social dialogue on AI and algorithmic management",
      "published": "2025-07",
      "url": "https://doi.org/10.54394/VOQE4924",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "ILO 작업논문 형식으로 낸 저자 견해(ILO 공식 입장 아님)의 질적 사례 연구. IBM 독일 AI 기본협약의 노사 AI 윤리위원회 사례를 포함한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.ilo.org/sites/default/files/2025-07/wp144_web.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-1553",
      "org": "W3C Accessibility Guidelines Working Group",
      "title": "Web Content Accessibility Guidelines (WCAG) 2.2 (W3C Recommendation 12 December 2024)",
      "published": "2024-12-12",
      "url": "https://www.w3.org/TR/2024/REC-WCAG22-20241212/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "웹 콘텐츠 접근성 W3C 권고. 이번에는 AA 성공기준 2.5.7(드래그 대체)과 2.5.8(최소 24×24 CSS px 대상과 예외 5개)만 사용.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1554",
      "org": "European Parliament and Council of the European Union (Official Journal L 151)",
      "title": "Directive (EU) 2019/882 of 17 April 2019 on the accessibility requirements for products and services",
      "published": "2019-06-07",
      "url": "https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "유럽 접근성법. 제2조(2025-06-28 이후 출시 제품의 적용 목록, 결제 단말기와 '서비스 제공 전용' 무인 단말기 구분)와 제15조(관보 게재 조화 표준의 적합성 추정)를 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng/pdf",
      "source_unopened": false
    },
    {
      "id": "ref-1555",
      "org": "ETSI / CEN / CENELEC",
      "title": "EN 301 549 V4.1.1 (2026-09) Accessibility requirements for ICT products and services",
      "published": "2026-09",
      "url": "https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "ICT 제품·서비스 접근성 유럽 표준 최종판(04.01.01_60). 5.1.5(청각 정보의 동등한 시각 정보)·5.1.7(음성 없는 조작 모드) 닫힌 기능 요구와 관보 인용 시 적합성 추정 머리말을 확인. 관보 인용 여부는 미확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1556",
      "org": "W3C Accessibility Guidelines Working Group (WCAG2ICT Task Force)",
      "title": "Guidance on Applying WCAG 2 to Non-Web Information and Communications Technologies (WCAG2ICT), W3C Group Note 11 December 2025",
      "published": "2025-12-11",
      "url": "https://www.w3.org/TR/2025/NOTE-wcag2ict-22-20251211/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "WCAG 2 를 비웹 문서·소프트웨어에 적용하는 정보성 안내(규범 아님). 제품 하드웨어 측면은 범위에서 제외한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1557",
      "org": "Deque Systems / axe-core contributors",
      "title": "axe-core v4.14.0 (lib/rules/target-size.json, README, CHANGELOG)",
      "published": "2026-10-05",
      "url": "https://github.com/dequelabs/axe-core/tree/v4.14.0",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "웹 접근성 자동 검사 엔진의 v4.14.0 태그 고정 원문. target-size 규칙의 태그(EN-301-549v4 등)와 enabled:false, README 의 incomplete 수동 검토 안내를 확인. 벤더(Deque) 저장소 단독.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/dequelabs/axe-core/v4.14.0/lib/rules/target-size.json",
      "source_unopened": false
    },
    {
      "id": "ref-1558",
      "org": "Choo, H.-J., Lee, S.-M. (Healthcare Informatics Research 32(1):59–68)",
      "title": "Nurses' Perceptions and Utilization Plans for Applying Companion Robots to Acute Stroke Patient Care: A Delphi Study",
      "published": "2026-01",
      "url": "https://doi.org/10.4258/hir.2026.32.1.59",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "서울 단일 상급종합병원 신경과·뇌졸중 집중치료실 간호사 14명의 3라운드 Delphi(2022-11-07~2023-04-12). 도입 후 효과 측정이 아니라 미래 시나리오 합의.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://synapse.koreamed.org/upload/synapsexml/1088hir/pdf/hir-2026-32-1-59.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-1559",
      "org": "Boadi-Agyemang, A. (Carnegie Mellon University Robotics Institute, CMU-RI-TR-26-106)",
      "title": "From Margin to Center: Designing Inclusive and Equitable Service Robots with Disabled Adults (PhD thesis)",
      "published": "2026-06",
      "url": "https://publications.ri.cmu.edu/storage/publications/2026/09/aboadiag-dissertation2026-manual-tagged-v2_20260902085808.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "CMU 박사논문. 4장은 2025년 Pittsburgh 장애 성인 14명과 한 배송 로봇 공동설계로, 물품 인수 시 근접 상호작용 요구를 보고한다. 저장소 게시 2026-09.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1560",
      "org": "Acemoglu, D., Restrepo, P. (Journal of Political Economy 128(6):2188–2244)",
      "title": "Robots and Jobs: Evidence from US Labor Markets (JPE 게재판)",
      "published": "2020-06",
      "url": "https://doi.org/10.1086/705716",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "NBER 작업논문(ref-1223)의 학술지 게재판. 1990~2007년 미국 722개 통근권역 지역 효과(-0.39%p, -0.77%)와 공간 파급을 반영한 총량 효과(-0.2%p, -0.42%)를 구분해 제시. MIT 저자 보관본으로 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://economics.mit.edu/sites/default/files/publications/Robots%20and%20Jobs%20-%20Evidence%20from%20US%20Labor%20Markets.p.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-1561",
      "org": "Dauth, W., Findeisen, S., Suedekum, J., Woessner, N. (Journal of the European Economic Association 19(6):3104–3153)",
      "title": "The Adjustment of Labor Markets to Robots",
      "published": "2021-12",
      "url": "https://doi.org/10.1093/jeea/jvab012",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "1994~2014년 독일 행정자료 연구. 총고용 감소 효과는 없고 제조업 감소를 서비스업 노동 수요가 상쇄했다고 보고. 저자 2021-01-21판 PDF 로 열람(온라인 2021-05-12, 권호 2021-12).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://sebastian-findeisen.com/downloads/labor_robots/AdjustmentLaborRobots_Final.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-1226",
      "org": "Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics)",
      "title": "Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety",
      "published": "2026-02-13",
      "url": "https://doi.org/10.1007/s12369-026-01359-1",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "창고 관련 참여자 12명 반구조화 면담 연구(IJSR 18, 26). 이번에는 Springer·KCL 원문이 접속 차단돼 초록의 N=12 만 확인했고 참여자 구성은 미확인.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1214",
      "org": "Han, H. Z. 외 (Carnegie Mellon University) — CHI '24",
      "title": "Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations",
      "published": "2024-04-07",
      "url": "https://arxiv.org/abs/2404.05050",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "이동장애인 15명·로봇 실무자 8명 면담과 공동설계 4회(모두 화상회의). arXiv v1 HTML 로 재열람. CHI 판 DOI 10.1145/3613904.3642875(2024-05-11).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2404.05050v1",
      "source_unopened": false
    },
    {
      "id": "ref-1223",
      "org": "Acemoglu, D., Restrepo, P. (NBER)",
      "title": "Robots and Jobs: Evidence from US Labor Markets",
      "published": "2017-03",
      "url": "https://www.nber.org/papers/w23285",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "NBER 작업논문 w23285 초록. 0.18~0.34%p·0.25~0.5% 범위값을 재열람으로 확인(위키 8절 값 유지 근거).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "sections": [
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 4(분리 2026-09-30-area60-s4) — '노사협의회 협의 사항'(39행)을 2022-12-11 시행 법률 제18927호 판(ref-1551)으로 근거 갱신하고(f17: 제2·9·14호 문구 동일, 제1항 개정 표시 2019-04-16), 제6호 고용조정 일반원칙(f16)·제7호 작업과 휴게 시간의 운용(f15)을 추가. '공개 작업자 설문 데이터' 항목으로 Liu 외 표본 조건(f1~f3)과 일반화 한계(f4) 추가 / 섹션 5 — 물류창고: 74행 Malik 면담 문장은 유지하고 참여자 국가·역할·로봇 경험은 덧붙이지 않음(f5 [추정], 메모 F04 '영국'·F05·F06 확인 불가). 예외·성과 칸 아래 본문에 SOC 보고서의 자료 기간(f10)·중대 부상 정의(f11)·Amazon NAICS 493110 자체 시설 456곳 대 비Amazon 창고 비교(f12, 메모 '비교창고 456시설' 정정)와 SOC 의 노조 연계 이해당사자 성격(f13), Amazon 자사 발표 43%·70%(f9 벤더 주장 [추정])를 넣고 둘을 교차 확인으로 세지 않음(f14). 병원: Choo·Lee Delphi(서울 단일 상급종합병원 간호사 14명, 2022-11~2023-04, f33·f34)를 사례 보충으로 넣되 도입 후 효과가 아니며 한림대 설문의 재현이 아님(f35). 실외: Han 외 활동이 모두 화상회의(f36)·실환경 평가 필요(f37), Boadi-Agyemang Pittsburgh 14명(f38)·물품 인수 근접 요구(f39)와 통행 간격과의 상황 차이(f40) / 섹션 6(분리 2026-09-30-area60-s6) — '수용성 측정 모델'에 FSQ-IC(f6~f8: 포르투갈 일반 성인 편의·눈덩이 표본, 무경험자 다수, 원문 표본 수 불일치)를 표본 조건과 함께 추가, 한국 일반화 금지. '노동자 참여 절차'의 '법률 제16320호, 2019-07-17 시행 기준'을 제18927호 판으로 갱신(f17)하고 ILO WP144 IBM 독일 AI 윤리위원회(f19, Cornell ILR 저자 견해이며 ILO 공식 아님 f20), 조문 적용 해석 미확인(f18); 의견 f46·f48 / 섹션 7(분리 2026-09-30-area60-s7) — 근로자참여법 행(43행) '법률 제16320호, 현행 조문 여부 미확인'을 2022-12-11 시행 법률 제18927호 열람판으로 갱신하고 제6·7호 추가(f15~f17). 새 행: WCAG 2.2 SC 2.5.7·2.5.8(f21·f22), WCAG2ICT 정보성 안내·하드웨어 제외(f23·f24), EN 301 549 V4.1.1 최종판·관보 인용 시 적합성 추정·5.1.5·5.1.7(f25~f27, 관보 인용 여부 미확인), 지침 (EU) 2019/882 제2조(1)(b) — (i) 결제 단말기는 '서비스 제공 전용' 한정이 없고 (ii) 단말기만 한정(f28), 제15조(1)(f29), 해당성 판단 유보(f30), axe-core v4.14.0 target-size 태그·enabled:false(f31)와 수동 검토(f32) — 벤더(Deque) 저장소 단독이라 [추정]·벤더 주장; 의견 f49. 무인정보단말기 소규모 시설 대체 이행(메모 F38)은 기존 내용 확인(2026-09-30-area60-s7.md 표 2행, ref-1217; chat-based-configuration-and-operation/index.md 124행)이라 새로 넣지 않음 / 섹션 8(분리 2026-09-30-area60-s8) — Acemoglu·Restrepo 항목(40행)의 0.18~0.34%p·0.25~0.5% 는 NBER 초록과 일치해 유지(f41)하고, JPE 2020 게재판 총량 효과 -0.2%p·-0.42%(f42)와 722개 통근권역 지역 효과 -0.39%p·-0.77%(f43)를 새 출처 ref-1560 으로 덧붙임. Dauth 외 독일 비교(f44)와 재현 아님(f45) 추가; 의견 f51. 새 수용성 연구 항목(Liu 외, FSQ-IC, Choo·Lee, Boadi-Agyemang)은 표본 조건을 문장에 넣고 어느 것도 한국 산업 현장 측정이 아님을 명시. 3절(분리 s3) 42행 '2017-03 작업논문' 문장은 유지(후속 정리 시 JPE 총량값 병기 검토) / 섹션 9 — 상위 업무 시스템 행: 휴게·작업 순환·직무 전환 정책을 노사협의 기록과 연결(f15·f16·f48). 업종별 조건 행: 화면 접근성을 웹 관제·비웹 HMI·로봇 단말 닫힌 기능·물리 접근으로 나누고 법적 적용 판단은 외부 연계(f21~f32·f49), 통행/대기/인수 모드 구분(f39·f50) / 섹션 11(분리 2026-09-30-area60-s11) — 해결 제안 없음. 부분 근거: oq-285(f15~f20), oq-286(f10~f14), oq-287(f33~f35), oq-284(f28~f30, 국내 장애인차별금지법 해당성은 미확인), oq-188(f36~f40, 국내 기준 미확인), oq-266(f19, 운영 소유권 비교 연구 아님). 답하지 못함: oq-146(EN 301 549 5.1.7 은 음성 대체 입력 요구일 뿐 한국어 인식률 자료 아님), oq-278(NCS 미확인). 다른 영역 페이지의 같은 근거(근로자참여법 제20조 ref-1220 '법률 제16320호' 표기: field-operations-and-monitoring/index.md 210·268행, 2026-09-30-area60-s10.md)는 후속 정리 필요(이번에 고치지 않음). 감시 관련 CNIL Amazon France 과징금(ref-1267, security-and-privacy/index.md)·oq-321 과 oq-285 연결은 참고만."
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "출처 충돌: FSQ-IC 포르투갈어판 검증 연구의 총 표본 346명과 두 분석 표본(EFA 140명 + CFA 210명 = 350명)이 맞지 않는 이유는 무엇이며, 어느 수가 실제 분석에 쓰였는가? | 관련 영역: 60. 노동·수용성·접근성 | 근거: f7 | 종류: 출처 충돌",
    "Burtch·Greenwood·Ravindran(ILR Review 2025) 원논문의 표본 시설·기간·추정식·강건성 검정은 무엇이며, 로봇 센터의 중대 부상 40% 감소·비중대 부상 77% 증가는 원논문에서 어떤 조건의 추정치인가? | 관련 영역: 60. 노동·수용성·접근성, 61. 물류창고, 49. 사람 근접 안전 | 근거: f14 | 종류: 일반",
    "알메러 모델·FSQ-IC 같은 수용성 척도를 한국어로 옮겨 국내 산업 현장 작업자(물류창고·제조·병원 직군)에게 타당화한 연구가 있는가? | 관련 영역: 60. 노동·수용성·접근성, 56. 운영 이관·확대·교육 | 근거: f8 | 종류: 일반",
    "EN 301 549 V4.1.1(2026-09)은 지침 (EU) 2019/882 의 조화 표준으로 EU 관보에 인용됐는가, 인용됐다면 언제부터 어떤 범위에서 적합성 추정을 주는가? | 관련 영역: 60. 노동·수용성·접근성, 59. 법·규제·보험·라이선스 | 근거: f25 | 종류: 일반",
    "한림대성심병원 의료서비스로봇 만족도 조사의 원 분모(간호사 109명 대 99명)·문항·조사 시점을 밝힌 병원 원보고서가 공개돼 있는가? | 관련 영역: 60. 노동·수용성·접근성, 63. 병원·의료 | 근거: f35 | 종류: 출처 충돌",
    "한국노동연구원 『기술 혁신과 노동시장 변화』(2024-12)의 로봇 노출도별 임금·고용 수치(고숙련 +2.5%·+0.55%p, 저숙련 -4.5~4.9%)의 원표와 식별 조건은 무엇인가? | 관련 영역: 60. 노동·수용성·접근성, 3. 경제성·조달·사업 모델 | 근거: f45 | 종류: 일반",
    "Han 외(CHI 2024) 공동설계 연구 참여자의 거주 국가와 지역은 본문 어디에 명시돼 있는가? | 관련 영역: 60. 노동·수용성·접근성, 66. 실외 | 근거: f36 | 종류: 일반",
    "접근성 요구가 서로 다른 이기종 로봇(배송·안내·병원 물류)의 작업 배정과 물품 인수 완료를 실제 이용자와 현장에서 검증하는 공개 시험 세트나 시나리오가 있는가? | 관련 영역: 60. 노동·수용성·접근성, 25. 작업 배정 — MRTA, 54. 시험·형식 검증·벤치마크 | 근거: f40 | 종류: 일반",
    "이용자의 장애 관련 접근 요구(인수 높이·근접 허용·입력 수단)를 플릿에 전달할 때 필요한 최소 정보 항목과 동의·보존·삭제 절차를 정한 운영 규약이나 검증 사례가 있는가? | 관련 영역: 60. 노동·수용성·접근성, 53. 개인정보·영상 데이터 | 근거: f39 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 18,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-03/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.",
      "f5: Malik 외(ref-1226) 원문은 Springer·KCL 저장소 모두 Cloudflare 차단으로 열지 못함. 초록의 N=12 반구조화 면담만 확인. 메모 F04 의 '영국 창고 경험', F05(비관리 5/관리·리더 7), F06(로봇 경험 7명)은 확인 불가라 사실로 쓰지 않음",
      "f7: FSQ-IC 원문의 346 vs 140+210=350 불일치 원인 미확인",
      "f15~f17: 근로자참여법 제20조는 2026-10-12 국가법령정보센터 조문 링크로 열람한 판(시행 2022-12-11, 법률 제18927호) 기준. 열람 이후 개정 여부와 ROP 로그·배정 정책의 협의 대상 해당성(판례·행정해석)은 확인 못 함",
      "f19·f20: ILO WP144 발행일 2025-07-10 은 확인 불가(PDF 표지 July/2025). IBM 면담 날짜가 각주 206(2021-11-08)과 부록 1(2024-07-26)에서 다름. IBM 협약 원문 미확보",
      "f25: EN 301 549 V4.1.1 의 EU 관보 인용 여부 미확인",
      "f31·f32: axe-core target-size 규칙을 실제로 실행해 enabled:false 와 태그 지정 실행의 동작을 시험하지 않음. README 의 57% 자동 검출 주장은 독립 재현 없음이라 쓰지 않음",
      "f42: JPE 게재판 온라인 게재일 2020-04-22 확인 불가(권호 2020-06 만 사용). f44: Dauth 외는 저자 2021-01-21판으로 읽었고 출판 최종판과의 완전 동일성 미확인",
      "f9: Amazon 발표의 지표 정의·노출 분모·로봇 센터 분리 수치 미확인(벤더 주장). 위키 Burtch 외 40%/77%(ref-1213)는 원논문 미열람 상태 그대로",
      "예산(신규 출처 15)에 맞추려고 메모 n4(Bartneck, Godspeed Questionnaire Series — 지각된 안전성 문항이 응답자 정서 상태를 묻고 Elena Knox 한국어 번역 제공, 메모 F10·F11)와 n14(W3C WAI, Selecting Web Accessibility Evaluation Tools — 'Human judgement is required', 메모 F28)는 검증에서 확인됐으나 출처에서 뺐다(후속 실행에서 추가 가능)",
      "oq-146(한국어 음성 인식률), oq-278(로봇 관제 NCS)은 이번 메모가 답하지 못함. oq-188 국내 점자블록·연석 대기 위치 기준, oq-284 로봇 단말의 장애인차별금지법상 무인정보단말기 해당성은 미확인"
    ],
    "scope_violations": [
      "f15~f20·f28~f30: 근로자참여법·유럽 접근성법의 법적 해당성 해석은 59. 법·규제·보험·라이선스 쪽 판단이므로 조문이 말하는 범위까지만 쓰고 개별 ROP 기능의 적용 여부는 판단하지 않음",
      "f21~f32: 웹·비웹 화면 접근성 기준은 37. 관제 화면·실행 기록, 13. 대화형 기능의 신뢰·기반과 겹치며, 이 영역에는 이용자·작업자 접근성 관점으로만 씀",
      "f9~f14: 창고 부상 지표는 49. 사람 근접 안전, 39. 운영 성과 측정·개선과 겹치며, 이 영역에는 노동 영향·이해당사자 자료 해석 관점으로만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 15
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 15건/15(ref-1547~ref-1561, 예약 구간 ref-1547~ref-1576 안), 재사용 3건(ref-1226·ref-1214·ref-1223). 출처 매핑(검증 결과 기준): 메모 n1→ref-1547, n2→ref-1226(미열람), n3→ref-1548, n4→예산 때문에 제외, n5→ref-1549(벤더 문서), n6→ref-1550, n7→ref-1551(2022판 새 출처; ref-1220 은 케이스노트 2019판이라 그대로 두고 비교에만 씀), n8→ref-1552, n9→ref-1553, n10→ref-1554, n11→ref-1555, n12→ref-1556, n13→ref-1557(github raw, v4.14.0 태그), n14→예산 때문에 제외, n15→ref-1558, n16→ref-1214(arXiv v1 HTML 재열람), n17→ref-1559, n18→ref-1560(JPE 게재판, NBER ref-1223 과 별도), n19→ref-1561, n20→ref-1217(메모 F38 중복이라 finding 없음, 출처에서 뺌). 추가 재사용: ref-1223(NBER 초록 재열람, 범위값 유지 근거). fetched: false 는 ref-1226. 교차 확인 0건(모든 사실 finding 이 단일 출처이거나 같은 계열: W3C 문서끼리, Han·Boadi 는 CMU 계열, Amazon·SOC 는 같은 OSHA 신고 자료 기초, Acemoglu·Dauth 는 IFR 자료·추정 전략 공유) — 단일 출처라 법령·표준 원문도 신뢰도 medium(validate 상한 규칙과 같음), 해석·벤더 finding 은 low. 중복 제거: 메모 F38(무인정보단말기 소규모 시설 대체 이행)은 2026-09-30-area60-s7.md 표·ref-1217·chat-based-configuration-and-operation/index.md 124행에 이미 있어 넣지 않음. 제20조 제2·9·14호, Han 15/8/4 숫자, 연석 경사로 사례도 기존 내용이라 재추가하지 않음. 검증 반영: F04 '영국'·F05·F06 확인 불가 → 사실 금지(f5 [추정]); A05 '비교창고 456시설' → Amazon NAICS 493110 자체 시설 456곳(f12), SOC 이해당사자 명시(f13); A06 근거 판을 2022-12-11 시행 법률 제18927호로(f15~f17); A07 ILO WP144 는 Cornell ILR 저자 견해이며 ILO 공식 아님(f19·f20); A11 (i) 결제 단말기에는 '서비스 제공 전용' 한정 없음 명시(f28); A12 axe-core 설정은 [추정]·벤더 주장(f31·f32); A15 는 Acemoglu 2017 범위값 유지(f41)와 JPE 2020 총량·지역 값 추가(f42·f43, 새 ref-1560); FSQ-IC 저자 6인으로 정정; 모든 수용성 연구는 표본 조건을 문장에 넣고 한국 일반화를 하지 않음(f4·f8·f35·f40·f45). 열린 질문: 해결 제안 없음(기존 질문 8개 모두 부분 답 또는 미답). 메모 new-1~4 는 기존 oq-284~oq-287 과 같은 질문이라 새로 만들지 않음(open-questions.md 306~309행 문구 대조). oq-146 은 페이지와 open-questions.md(168행)의 꼬리 문구만 다르고 같은 질문. 새 질문 9건(메모 U09~U17, 기존 질문과 겹침 없음 확인). 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·쪽·조와 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음."
  }
}
```

### runs/2026-10-12-03/verification.json

```json
{
  "run_id": "2026-10-12-03",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "DOI 10.1016/j.dib.2025.111750 이 Elsevier Data in Brief 레코드(PII S2352340925004779)로 해석됨. 검증자의 PMC 재열람은 reCAPTCHA 로, ScienceDirect 재열람은 리다이렉트로 실패해 530/337 은 리서치 열람 발췌 기준이다(검증자 원문 미대조). 단일 출처라 medium 상한."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "모집 기간 2022-04-05~07-04 는 리서치 열람 발췌 기준이고 검증자는 원문을 대조하지 못했다. 발행일(2025-06)과 조사일을 구분해 쓴 점 적절."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "표본 조건(4개국·영어·군집 모집·남성 편중·창고 123명 36.5%)은 리서치 열람 발췌 기준이며 검증자는 원문을 대조하지 못했다. 수치를 바꾸지 않고 그대로 쓸 것."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f1~f3 에서 이끌어 낸 [추정]. 일반화하지 않는다는 한계 서술로 적절."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1226 은 기존 참고문헌이며 이번에는 원문 미열람(fetched false)이다. 검증자 검색으로도 원문을 다시 찾지 못했다. 본문 문장을 바꾸지 않는다는 처분 진술이라 [추정]·low 가 적절하다. 기존 각주 접근일을 바꾸지 말 것."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리포지터리(recipp.ipp.pt)에서 저자 6인, 2025-01-17, Article 8816379 를 확인했다. 346명·편의/눈덩이 표본·LimeSurvey 는 리서치 발췌 기준이다(Wiley 403)."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리포지터리 요약으로 EFA 140, CFA 210 을 확인했다. 346 대 350 은 원문 안의 불일치이므로 한쪽을 고르지 말고 둘 다 제시한 뒤 열린 질문(출처 충돌)으로 둔다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f6·f7 에서 이끌어 낸 [추정]. 무경험자 비율(102/140, 147/210)은 리서치 발췌 기준이다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "aboutamazon 페이지를 열어 RIR 43%·LTIR 70%(6년)와 전년 대비 각 14% 를 확인했다. 현재 페이지 제목은 'Amazon invests $2.5 billion in workplace safety, reduces workplace injury rates'로 브리프 제목과 다르다(제목 정정 지시). 게시일은 페이지에 표시되지 않아 2026-03-12 는 리서치의 메타데이터 기준이다. 벤더 주장 [추정] 유지."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "SOC 자료 페이지(2025-05-16)와 PDF 가 있음을 확인했다. PDF 본문은 이진 데이터라 '2020~2024 OSHA 자료' 문구는 리서치 발췌 기준이다. 자료 페이지는 Amazon 이 OSHA 에 제출한 자료라고만 적는다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "중대 부상 정의(경작업 전환·휴업)는 리서치 발췌 기준이다. 검색 결과에 SOC 의 light duty 분석 맥락이 있어 일관된다. GMU 정의와 같은지는 미확인이므로 그렇게 적을 것."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검색 결과로 Amazon 이 NAICS 493110 으로 분류한 456개 시설과 비Amazon 창고를 비교한 사실, 2024 중대 부상률 5.9 대 3.0(100명당)을 확인했다. 메모의 '비교창고 456시설' 정정 판단은 맞다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검색 결과가 SOC 를 노동조합 연합으로 기술한다. SEIU·CWA·UFW 명시는 리서치 발췌 기준이다. 이해당사자 자료로 표시하는 것이 적절하다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 다만 Amazon 페이지는 전 세계 수치 외에 미국 OSHA 기준 일반 창고·보관업 수치도 싣고 있다. 따라서 'Amazon 발표=전 세계만'으로 쓰지 말고 '브리프가 인용한 Amazon 의 전 세계 수치(f9)'로 한정해야 한다(수정 지시). 미국 수치는 브리프에 없으므로 새로 넣지 않는다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "국가법령정보센터 조문을 열어 시행 2022-12-11, 법률 제18927호, 제1항 제7호 '작업과 휴게 시간의 운용', <개정 2019. 4. 16.> 을 확인했다. 확인 기준일은 2026-10-12."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "같은 조문에서 제6호 문구가 일치함을 확인했다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "제2·9·14호 문구가 같고 제1항 개정 표시가 2019-04-16 임을 확인했다. '현행 여부 미확인'을 '2026-10-12 열람판(2022-12-11 시행) 기준'으로 바꿀 근거가 된다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "조문이 협의 사항을 열거할 뿐이라는 것은 확인됨. 적용 해석 미확인을 밝힌 [추정]으로 적절하다(oq-285 부분 답)."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ILO 출판 페이지에서 WP144, 저자 5인, DOI 10.54394/VOQE4924, 발행 2025-07-10 을 확인했다. PDF 는 이진 응답이라 IBM 독일 AI 윤리위원회 서술(인쇄 p.48)은 리서치 발췌 기준이며 검증자는 원문을 대조하지 못했다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 다만 'ILO WP144 발행일 2025-07-10 확인 불가'는 틀렸다. ILO 출판 페이지가 2025-07-10 으로 표시하므로 그 날짜를 써도 된다(수정 지시). 면책 문구와 IBM 면담 날짜 불일치는 리서치 발췌 기준이다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "W3C 권고(2024-12-12)를 열어 SC 2.5.7(AA), 단일 포인터 대체, 예외 2개(필수·사용자 에이전트)를 확인했다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "SC 2.5.8(AA)의 24×24 CSS px 와 예외 5개(Spacing·Equivalent·Inline·User Agent Control·Essential)를 확인했다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "WCAG2ICT Group Note(2025-12-11)의 '정보성 안내, 규범 아님' 문구를 확인했다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "'제품의 하드웨어 측면은 다루지 않는다'는 적용 범위 제외 문구를 확인했다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ETSI 배포 디렉터리로 04.01.01_60(2026-09-02)이 최종판임을 확인했다. 다만 04.01.00_20 은 2025-11-12, 04.01.00_30 은 2026-06-24 배포라서 'V4.1.0(04.01.00_20·_30)을 2025-11' 하나로 묶은 표현은 부정확하다(수정 지시). 머리말의 적합성 추정 문구는 PDF 미대조이므로 리서치 발췌 기준이고, 관보 인용 여부는 미확인."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "5.1.5 조항 문구는 리서치 발췌 기준이다(PDF 본문 미대조). 닫힌 기능 조건부 요구라는 한정을 유지할 것."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "5.1.7 조항 문구는 리서치 발췌 기준이다. 닫힌 기능 조건이 없는 로봇에 일률 적용하지 않는다는 한정을 유지할 것."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "EUR-Lex 는 빈 응답이었다. 검색 결과(legislation.gov.uk 지침 본문 등)로 제2조(1)(b)의 구조, 곧 결제 단말기는 무한정이고 무인 단말기는 '서비스 제공 전용'으로 한정된다는 점과 2025-06-28 을 확인했다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "제15조(1) 문구는 리서치 발췌(EUR-Lex PDF) 기준이며 검증자는 원문을 대조하지 못했다. 관보 게재 조화 표준의 적합성 추정이라는 내용은 지침 구조와 일치한다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "해당성 판단을 유보한 [추정]. 59. 법·규제·보험·라이선스 쪽 판단이므로 연계 대상으로만 쓸 것."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "v4.14.0 태그의 raw target-size.json 을 열어 enabled:false 와 태그 5개(wcag22aa·wcag258·EN-301-549v4·EN-9.2.5.8 등)를 확인했다. 벤더 저장소 단독이라 [추정]·벤더 주장으로 둔다. 다만 파일 내용 자체는 문서 구조 사실이므로 강등 요구는 없다."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "README 의 incomplete 안내는 리서치 발췌 기준이다. 실행 시험을 하지 않았다는 한계를 적은 [추정]·벤더 주장으로 적절하다. 57% 주장을 쓰지 않는 처리도 맞다."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "e-hir.org 원문을 열어 간호사 14명(신경과 병동 6, 뇌졸중 집중치료실 8, 경력 7년 초과), 서울 단일 상급종합병원, 3라운드를 확인했다. 온라인 게재일은 2026-01-31."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "조사 기간 2022-11-07~2023-04-12 를 확인했다."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "저자 한계(단일 기관·편의 표집)를 확인했다. 도입 뒤 효과 측정이 아니라는 [추정]은 적절하다."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "arXiv v1 HTML 에서 'All the activities were held over video conference' 를 확인했다. 이동장애인 참여자의 국가는 본문에 명시되지 않음을 확인했다(새 열린 질문의 근거로 타당)."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "7.1 절의 실환경 평가 필요 문장을 확인했다."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "CMU RI 학위논문 심사 행사 페이지로 논문이 있음을 확인했다. PDF 는 이진 응답이라 14명·Pittsburgh·2025 두 달과 보고서 번호 CMU-RI-TR-26-106 은 리서치 발췌 기준이며 검증자는 대조하지 못했다. 같은 저자의 HRI 2026 배송 로봇 공동설계 논문이 있다는 것은 확인했다."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "인수 시 근접 상호작용 구절(인쇄 p.70)은 리서치 발췌 기준이며 검증자는 대조하지 못했다. 직접 인용은 이 출처에서 1회만 허용."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "같은 CMU 계열이라 독립 교차 확인으로 세지 않는다는 판단이 적절한 [추정]이다."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "NBER w23285(2017-03) 초록의 0.18~0.34%p·0.25~0.5% 를 확인했다. 기존 값은 유지한다."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "MIT DSpace 레코드와 검색 결과로 JPE 128(6):2188–2244 와 0.2%p·0.42% 를 확인했다(MIT PDF 직접 열람은 이진 응답)."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "722개 통근권역은 검색 결과로 확인했다. 지역 효과 0.39%p·0.77% 는 리서치 발췌(MIT 보관본) 기준이다. 총량 효과(f42)와 구분해 쓸 것."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검색 결과로 JEEA 19(6):3104–3153 과, 제조업 감소를 서비스업이 상쇄해 총고용 효과가 없다는 요지를 확인했다. 저자 2021-01 판 기준임을 표시할 것. 이 연구의 저숙련 임금 손실 같은 다른 결과는 브리프에 없으므로 덧붙이지 않는다."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "재현·반박으로 보지 않는다는 [추정]이 적절하다."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견]. 주체를 '이 위키 구축자의 의견'으로 밝힐 것."
    },
    {
      "finding_id": "f47",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견]. 주체를 '구축자 의견'으로 밝힐 것."
    },
    {
      "finding_id": "f48",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견]. 법적 해당성 판단은 ROP 밖(연계 대상)이라는 범위 경계를 지켰다. 주체를 밝힐 것."
    },
    {
      "finding_id": "f49",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견]. 기술 시험과 법적 적용 판단을 분리했다. 주체를 밝힐 것."
    },
    {
      "finding_id": "f50",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견]. 근접 허용은 현장 안전 평가 전제로 한정했다. 49. 사람 근접 안전과 연결한다."
    },
    {
      "finding_id": "f51",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견]. 주체를 밝힐 것."
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
      "f15~f17(ref-1551 법률 제18927호 판)은 기존 각주 ref-1220(케이스노트 법률 제16320호 판)과 같은 조문의 다른 판이다. 이 페이지 4·6·7·9절의 제20조 근거는 ref-1551 로 갱신하되, ref-1220 을 쓰는 다른 페이지(field-operations-and-monitoring/index.md, 2026-09-30-area60-s10.md)는 이번 범위 밖이다.",
      "f41 은 기존 8절 Acemoglu·Restrepo 항목(ref-1223)과 같은 주장의 재확인이며, f42·f43(ref-1560 JPE 게재판)은 같은 연구의 게재판 수치를 덧붙인 것이다.",
      "f36·f37 은 기존 5절 실외 사례(ref-1214, 15/8/4 숫자)를 보강한다. 기존 숫자를 다시 넣지 않는다.",
      "f9~f14 는 기존 5절 물류창고 예외·성과 칸(ref-1213 GMU 40%/77%)과 같은 주제의 다른 이해당사자 자료다. 서로 교차 확인이나 모순으로 세지 않는다."
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
    "ref-1549(f9): 참고문헌 제목을 2026-10-12 현재 페이지 제목 'Amazon invests $2.5 billion in workplace safety, reduces workplace injury rates' 로 고친다. 페이지에 게시일이 표시되지 않으므로 발행일 2026-03-12 는 페이지 메타데이터 기준임을 각주에 따로 단정하지 않는다. 이유: 검증자 열람에서 현재 제목이 브리프 제목과 달랐다.",
    "f9: 5절 물류창고 본문에 'Amazon 자사 발표에 따르면'으로 시작해 [추정]과 '벤더 주장'을 병기한다. 로봇 도입 효과를 분리한 수치가 아니라는 점도 함께 적는다. 이유: 회사 자체 발표이고 독립 확인이 없다.",
    "f14: 'Amazon 발표는 전 세계 범위'라고 단정하지 말고 '브리프가 인용한 Amazon 의 전 세계 수치(f9)'로 한정해 SOC(미국·2024·비Amazon 창고 대비)와 비교한다. Amazon 페이지의 미국 수치는 브리프에 없으므로 새로 넣지 않는다. 이유: Amazon 페이지는 미국 OSHA 기준 창고 수치도 함께 싣는다.",
    "f25: 7절 EN 301 549 행에서 'V4.1.0(04.01.00_20·_30)은 2025-11 초안'을 'V4.1.0 은 초안 단계 배포본(04.01.00_20 2025-11, 04.01.00_30 2026-06)'으로 고친다. V4.1.1(04.01.01_60)의 EU 관보 인용 여부는 '미확인'으로 남긴다. 이유: ETSI 배포 디렉터리에서 _30 은 2026-06-24 배포로 확인됐다.",
    "ref-1552(f19·f20): 발행일을 2025-07-10 으로 적을 수 있고, '발행일 확인 불가' 문구는 페이지에 옮기지 않는다. ILO 공식 입장이 아니라 저자(Cornell ILR) 견해라는 점은 반드시 병기한다. 이유: ILO 출판 페이지가 2025-07-10 으로 표시한다.",
    "f7: 6절 FSQ-IC 서술에서 총 표본 346명과 EFA 140 + CFA 210 = 350명을 둘 다 제시하고 원문 안의 불일치임을 밝힌다. 한쪽 수만 쓰지 않는다. 이유: 출처 내부 충돌이며 열린 질문(출처 충돌)으로 올라간다.",
    "5절 적용 사례: Choo·Lee Delphi(f33~f35)와 Han·Boadi-Agyemang(f36~f40)은 실제 도입 뒤 측정이 아니라 미래 시나리오 합의와 설계·요구 연구다. 표의 '예외·성과' 칸에 도입 성과처럼 쓰지 말고 '해당 없음' 또는 연구 조건 서술로 둔다. 현장 유형은 각각 '병원'·'실외'로 밝힌다. 이유: 사례 성격과 다르게 성과로 읽히는 것을 막기 위해서다.",
    "7절 접근성 표준 행(f21~f30): WCAG 2.2·WCAG2ICT·EN 301 549·지침 (EU) 2019/882 를 쓸 때 한국 ROP 나 개별 로봇 단말에 적용되는 법적 의무처럼 쓰지 않는다. 기술 기준과 EU 법역의 조문 범위로만 쓰고, 해당성 판단(f30)은 59. 법·규제·보험·라이선스 쪽 연계 대상으로 연결한다. 이유: 범위 경계(분류 원문 19장 업종별 조건)와 f30 의 유보 판단 때문이다.",
    "근로자참여법 제20조(4·6·7·9절): 근거를 ref-1551(2026-10-12 열람, 2022-12-11 시행 법률 제18927호)로 갱신하고 '현행 조문 여부 미확인' 문구를 지운다. 대신 '열람일 이후 개정 여부는 확인하지 않음'을 남긴다. 다른 줄이 아직 ref-1220 을 쓰면 그 각주 정의는 지우지 않는다. 이유: f15~f17 이 원문으로 확인됐다.",
    "ref-1226: 이번 실행에서는 원문을 열지 못했다(f5). 기존 각주 줄(접근일 2026-09-30)을 그대로 두고 reference_updates 로 접근일을 2026-10-12 로 바꾸지 않는다. 바꾸려면 ' (원문 미열람)'을 붙인다. 5절 74행의 Malik 문장에 참여자 국가·역할·로봇 경험을 덧붙이지 않는다.",
    "인용: 페이지에서 출처 원문 직접 인용은 출처당 1회 짧은 구절만 쓴다(특히 ref-1547·ref-1553·ref-1555·ref-1554 는 발췌가 여러 finding 에 걸쳐 있다). 나머지는 한국어로 재서술한다.",
    "f46~f51 [의견]: 문장마다 '이 위키 구축자의 의견'처럼 의견의 주체를 밝힌다.",
    "f44: Dauth 외 결과는 저자 2021-01-21 판 기준임을 밝히고, 미국(f42·f43)과 독일 결과를 재현·반박 관계로 쓰지 않는다(f45).",
    "open_questions_new 다섯 번째(한림대성심병원 원 분모 109 대 99): 근거 필드를 f35 가 아니라 ref-1222 로 고쳐 등록한다. 이유: 표본 수 충돌은 기존 각주 ref-1222 의 보도들 사이에서 나왔고 f35 는 그 충돌을 다루지 않는다.",
    "11절 열린 질문: 해결로 바꾸는 질문은 없다. oq-285(f15~f20), oq-286(f10~f14), oq-287(f33~f35), oq-284(f28~f30), oq-188(f36~f40), oq-266(f19)은 부분 근거로만 표시하고 상태를 '열림'으로 유지한다. oq-146·oq-278 은 근거가 없음을 그대로 둔다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 51건, 미확인 0건, 교차 확인 0건. 확인 51건 가운데 검증자가 원문·공식 페이지·검색 결과로 직접 대조한 것은 f7·f9·f12·f15~f17·f19(서지)·f21~f25·f28·f31·f33~f37·f41~f44 이다. f1~f3·f6(표본)·f10·f11·f13·f19(IBM 사례)·f20·f26·f27·f29·f38·f39 는 검증자 재열람이 막혀(PMC 캡차, PDF 이진 응답, Wiley 403) 리서치의 원문 열람 발췌를 기준으로 인정했다. 강등: 없음. 원문 미열람 출처: ref-1226(이번 실행). 정정 사항: Amazon 발표(ref-1549)의 현재 제목이 다르다. EN 301 549 V4.1.0 의 04.01.00_30 은 2026-06 배포본이다. ILO WP144 발행일 2025-07-10 은 ILO 출판 페이지로 확인된다. 주의: 수용성 연구(Liu 외·FSQ-IC·Choo·Lee·Han·Boadi-Agyemang)는 모두 해외 또는 단일 기관 표본이며 한국 산업 현장 작업자 측정이 아니다. FSQ-IC 원문의 표본 수(346 대 350)는 원문 안에서 서로 맞지 않는다. Amazon 발표와 SOC 보고서는 서로 다른 이해당사자 자료이고 로봇 효과를 분리하지 않는다. 접근성 표준·EU 지침의 개별 ROP 적용 여부는 판단하지 않았다. 리서치 출처 9건(ref-1548~ref-1551·ref-1553·ref-1555·ref-1556·ref-1559 등)은 fetched true 인데 fetch_url 이 비어 있다. 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-10-12-03/pages.json

```json
{
  "run_id": "2026-10-12-03",
  "outline": [
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1200,
      "summary": "근로자참여법 제20조 협의 사항을 2022-12-11 시행판(법률 제18927호)으로 갱신하고 제6·7호를 더한다. [사실][^ref-1551] 공개 작업자 설문 데이터(Liu 외)의 표본 조건과 한국 일반화 한계를 적는다. [추정][^ref-1547]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f15",
        "f16",
        "f17"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 4300,
      "summary": "물류창고 사례에 Amazon 자사 발표와 SOC 노조 보고서를 서로 다른 이해당사자 자료로 덧붙이고, 병원 사례에 Choo·Lee Delphi, 실외 사례에 화상회의 진행 조건과 Pittsburgh 물품 인수 공동설계 사례를 더한다. [추정][^ref-1549][^ref-1550]",
      "planned_findings": [
        "f5",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f33",
        "f34",
        "f35",
        "f36",
        "f37",
        "f38",
        "f39",
        "f40",
        "f47"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1800,
      "summary": "FSQ-IC 포르투갈어판 수용성 척도의 표본 조건과 표본 수 불일치를 적고, 노동자 참여 절차의 근거 판을 갱신하며 IBM 독일 노사 AI 윤리위원회 사례를 더한다. [사실][^ref-1548][^ref-1552]",
      "planned_findings": [
        "f6",
        "f7",
        "f8",
        "f18",
        "f19",
        "f20",
        "f46"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 2400,
      "summary": "근로자참여법 근거를 ref-1551로 바꾸고, WCAG 2.2·WCAG2ICT·EN 301 549 V4.1.1·지침 (EU) 2019/882·axe-core를 기술 기준과 EU 법역의 조문 범위로만 정리한다. [사실][^ref-1553][^ref-1555]",
      "planned_findings": [
        "f15",
        "f16",
        "f17",
        "f21",
        "f22",
        "f23",
        "f24",
        "f25",
        "f26",
        "f27",
        "f28",
        "f29",
        "f30",
        "f31",
        "f32"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1600,
      "summary": "Acemoglu·Restrepo 범위값을 유지하고 JPE 게재판의 지역 효과와 총량 효과를 구분해 더하며, 독일 Dauth 외 결과를 재현·반박이 아닌 별개 결과로 적는다. [사실][^ref-1560][^ref-1561]",
      "planned_findings": [
        "f41",
        "f42",
        "f43",
        "f44",
        "f45",
        "f51"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 2400,
      "summary": "상위 업무 시스템 행에 휴게·고용조정 협의 사항과 노사협의 기록 연결을, 업종별 조건 행에 화면 접근성 범위 구분과 통행·대기·인수 모드 구분을 더한다. [의견][^ref-1551][^ref-1553]",
      "planned_findings": [
        "f15",
        "f16",
        "f30",
        "f48",
        "f49",
        "f50"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "11. 열린 질문",
      "budget_chars": 1900,
      "summary": "기존 질문 8건의 부분 근거를 표시하되 모두 열림으로 두고, 새 질문 9건을 더한다.",
      "planned_findings": [
        "f7",
        "f8",
        "f14",
        "f25",
        "f35",
        "f36",
        "f39",
        "f40",
        "f45"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "차등 갱신: 4절(근로자참여법 제20조 2022판·공개 작업자 설문 표본 조건), 5절(물류창고 이해당사자 부상 자료·병원 Delphi·실외 물품 인수 사례), 6절(FSQ-IC·노사 AI 윤리위원회), 7절(근거 판 갱신·디지털 접근성 기준), 8절(JPE 게재판·독일 비교), 9절(책임 경계 보강), 11절(부분 근거·새 질문 9건), 13절 각주 15건 추가. 2차 수정: 4·6·7·8·11절에 2026-09-30 분리 주제 페이지 링크 복원, 8절 범위값 출처 링크, 5절 실외 끝 문장 정정",
      "patches": [
        {
          "section": "4. 핵심 개념과 용어",
          "action": "append",
          "frontmatter": {
            "sources": [
              "ref-1213",
              "ref-1214",
              "ref-1215",
              "ref-1216",
              "ref-1217",
              "ref-1218",
              "ref-1151",
              "ref-1219",
              "ref-1220",
              "ref-1221",
              "ref-1222",
              "ref-1223",
              "ref-1224",
              "ref-1225",
              "ref-1226",
              "ref-1547",
              "ref-1548",
              "ref-1549",
              "ref-1550",
              "ref-1551",
              "ref-1552",
              "ref-1553",
              "ref-1554",
              "ref-1555",
              "ref-1556",
              "ref-1557",
              "ref-1558",
              "ref-1559",
              "ref-1560",
              "ref-1561"
            ],
            "last_run": "2026-10-12"
          },
          "content": "(절 본문 생략 — runs/2026-10-12-03/pages/categories/governance-law-and-society/labor-acceptance-and-accessibility.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-03/pages/categories/governance-law-and-society/labor-acceptance-and-accessibility.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-03/pages/categories/governance-law-and-society/labor-acceptance-and-accessibility.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-03/pages/categories/governance-law-and-society/labor-acceptance-and-accessibility.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-03/pages/categories/governance-law-and-society/labor-acceptance-and-accessibility.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-03/pages/categories/governance-law-and-society/labor-acceptance-and-accessibility.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-03/pages/categories/governance-law-and-society/labor-acceptance-and-accessibility.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-03/pages/categories/governance-law-and-society/labor-acceptance-and-accessibility.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-12-area60-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(2,519자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area60-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"11. 열린 질문\" 절(2,273자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area60-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"6. 대표 접근법과 기술\" 절(1,757자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area60-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"8. 대표 연구와 자료\" 절(1,580자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area60-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"4. 핵심 개념과 용어\" 절(1,187자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-12 | 60. 노동·수용성·접근성 | 갱신: 근로자참여법 제20조 근거를 2022-12-11 시행판으로 바꾸고 수용성 연구 표본 조건, 물류창고 이해당사자 부상 자료, 병원·실외 사례, 디지털 접근성 기준, 고용 효과 게재판·독일 비교, 새 열린 질문 9건 추가 | run 2026-10-12-03",
  "index_updates": {
    "home_recent": "2026-10-12 — 60. 노동·수용성·접근성: 수용성 연구의 표본 조건, 창고 부상 자료(회사 발표·노조 보고서), 디지털 접근성 기준(WCAG 2.2·EN 301 549·유럽 접근성법), 근로자참여법 현행판 근거를 더했다",
    "category_recent": "2026-10-12 — 60. 노동·수용성·접근성: 4·5·6·7·8·9·11절 갱신(근로자참여법 제20조 2022-12-11 시행판, 수용성 표본 조건, 이해당사자 부상 자료, 접근성 기준, JPE 게재판·독일 비교), 각주 15건 추가",
    "area_recent": "2026-10-12 — 60. 노동·수용성·접근성: 갱신 — 근로자참여법 근거 판 갱신(제6·7호 추가), 공개 작업자 설문·FSQ-IC·간호사 Delphi·장애 이용자 공동설계의 표본 조건, Amazon 발표와 SOC 보고서 비교, 디지털 접근성 기준과 책임 경계, 새 열린 질문 9건"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-1547",
      "org": "Liu, Y. (A.), Kaur, G., Banerjee, N. K., Banerjee, S. (Clarkson University·Wright State University) — Data in Brief 61",
      "title": "Dataset of worker perceptions of workforce robotics regarding safety, independence, job security, and privacy",
      "published": "2025-06-03",
      "url": "https://doi.org/10.1016/j.dib.2025.111750",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "미국·캐나다·영국·호주 6개 업종 블루칼라 노동자 대상 영어 온라인 설문(2022-04-05~07-04, 군집 모집) 530명 중 공개 동의 337명의 40문항 응답 데이터셋.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1548",
      "org": "Pinto, A., Lemos, L., Carvalho, C., Santos, J., Menezes, P., Nomura, T. — Human Behavior and Emerging Technologies",
      "title": "Translation, Adaptation, and Validation in Portuguese of an Acceptance Scale for Human–Robot Interaction in an Industrial Context",
      "published": "2025-01-17",
      "url": "https://doi.org/10.1155/hbe2/8816379",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "FSQ-IC 포르투갈어판 검증 연구(저자 6인, Article ID 8816379). 네트워크 연락처 편의·눈덩이 온라인 표본 346명(EFA 140/CFA 210, 로봇 무경험 다수)이며 표본 수가 원문 안에서 불일치한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1549",
      "org": "Amazon (Sarah Rhoads, VP Global Workplace Health & Safety)",
      "title": "Amazon invests $2.5 billion in workplace safety, reduces workplace injury rates",
      "published": "2026-03-12",
      "url": "https://www.aboutamazon.com/news/workplace/amazon-workplace-safety-2025-injury-reduction",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "Amazon 자사 발표(2026-03-27 수정). 전 세계 운영의 기록대상 사고율 43%, 휴업 사고율 70% 개선(6년, 2019 대비)을 주장한다. 로봇 효과를 분리한 수치가 아니다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1550",
      "org": "Strategic Organizing Center (SOC; SEIU·CWA·UFW 연계 노동 조직)",
      "title": "Failure to Deliver: Amazon Falls Short on Safety",
      "published": "2025-05",
      "url": "https://thesoc.org/wp-content/uploads/2025/05/May-2025_Strategic-Organizing-Center_Report-x-Failure-To-Deliver.pdf",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "2020~2024년 OSHA 제출 자료로 Amazon 창고 부상률을 분석한 노동조합 측 이해당사자 보고서. 중대 부상=경작업 전환·휴업, Amazon NAICS 493110 자체 시설 456곳과 비Amazon 창고 전체를 비교한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1551",
      "org": "법제처 국가법령정보센터 (대한민국, 법률 제18927호)",
      "title": "근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) 시행 2022-12-11 법률 제18927호(2022-06-10 일부개정)",
      "published": "2022-06-10",
      "url": "https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017145541",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "노사협의회 협의 사항을 정한 조문. 2026-10-12 열람판은 2022-12-11 시행 법률 제18927호이며 제1항은 2019-04-16 개정 표시. 제6호 고용조정 일반원칙, 제7호 작업과 휴게 시간의 운용을 포함. 기존 ref-1220(케이스노트 2019판)의 후속 판.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1552",
      "org": "Doellgast, V., Appalla, S., Ginzburg, D., Kim, J., Thian, W. L. (Cornell University ILR School) — ILO Working Paper 144",
      "title": "Global case studies of social dialogue on AI and algorithmic management",
      "published": "2025-07-10",
      "url": "https://doi.org/10.54394/VOQE4924",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "ILO 작업논문 형식으로 낸 저자 견해(ILO 공식 입장 아님)의 질적 사례 연구. IBM 독일 AI 기본협약의 노사 AI 윤리위원회 사례를 포함한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1553",
      "org": "W3C Accessibility Guidelines Working Group",
      "title": "Web Content Accessibility Guidelines (WCAG) 2.2 (W3C Recommendation 12 December 2024)",
      "published": "2024-12-12",
      "url": "https://www.w3.org/TR/2024/REC-WCAG22-20241212/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "웹 콘텐츠 접근성 W3C 권고. AA 성공기준 2.5.7(드래그 대체)과 2.5.8(최소 24×24 CSS px 대상과 예외 5개)을 사용.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1554",
      "org": "European Parliament and Council of the European Union (Official Journal L 151)",
      "title": "Directive (EU) 2019/882 of 17 April 2019 on the accessibility requirements for products and services",
      "published": "2019-06-07",
      "url": "https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "유럽 접근성법. 제2조(2025-06-28 이후 출시 제품의 적용 목록, 결제 단말기와 '서비스 제공 전용' 무인 단말기 구분)와 제15조(관보 게재 조화 표준의 적합성 추정)를 확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1555",
      "org": "ETSI / CEN / CENELEC",
      "title": "EN 301 549 V4.1.1 (2026-09) Accessibility requirements for ICT products and services",
      "published": "2026-09",
      "url": "https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "ICT 제품·서비스 접근성 유럽 표준 최종판(04.01.01_60). V4.1.0 은 초안 단계 배포본(04.01.00_20 2025-11, 04.01.00_30 2026-06). 5.1.5·5.1.7 닫힌 기능 요구와 관보 인용 시 적합성 추정 머리말을 확인. 관보 인용 여부는 미확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1556",
      "org": "W3C Accessibility Guidelines Working Group (WCAG2ICT Task Force)",
      "title": "Guidance on Applying WCAG 2 to Non-Web Information and Communications Technologies (WCAG2ICT), W3C Group Note 11 December 2025",
      "published": "2025-12-11",
      "url": "https://www.w3.org/TR/2025/NOTE-wcag2ict-22-20251211/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "WCAG 2 를 비웹 문서·소프트웨어에 적용하는 정보성 안내(규범 아님). 제품 하드웨어 측면은 범위에서 제외한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1557",
      "org": "Deque Systems / axe-core contributors",
      "title": "axe-core v4.14.0 (lib/rules/target-size.json, README, CHANGELOG)",
      "published": "2026-10-05",
      "url": "https://github.com/dequelabs/axe-core/tree/v4.14.0",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "웹 접근성 자동 검사 엔진의 v4.14.0 태그 원문. target-size 규칙의 태그(EN-301-549v4 등)와 enabled:false, README 의 incomplete 수동 검토 안내를 확인. 벤더(Deque) 저장소 단독.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1558",
      "org": "Choo, H.-J., Lee, S.-M. (Healthcare Informatics Research 32(1):59–68)",
      "title": "Nurses' Perceptions and Utilization Plans for Applying Companion Robots to Acute Stroke Patient Care: A Delphi Study",
      "published": "2026-01",
      "url": "https://doi.org/10.4258/hir.2026.32.1.59",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "서울 단일 상급종합병원 신경과·뇌졸중 집중치료실 간호사 14명의 3라운드 Delphi(2022-11-07~2023-04-12). 도입 후 효과 측정이 아니라 미래 시나리오 합의.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1559",
      "org": "Boadi-Agyemang, A. (Carnegie Mellon University Robotics Institute, CMU-RI-TR-26-106)",
      "title": "From Margin to Center: Designing Inclusive and Equitable Service Robots with Disabled Adults (PhD thesis)",
      "published": "2026-06",
      "url": "https://publications.ri.cmu.edu/storage/publications/2026/09/aboadiag-dissertation2026-manual-tagged-v2_20260902085808.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "CMU 박사논문. 4장은 2025년 Pittsburgh 장애 성인 14명과 한 배송 로봇 공동설계로, 물품 인수 시 근접 상호작용 요구를 보고한다. 저장소 게시 2026-09.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1560",
      "org": "Acemoglu, D., Restrepo, P. (Journal of Political Economy 128(6):2188–2244)",
      "title": "Robots and Jobs: Evidence from US Labor Markets (JPE 게재판)",
      "published": "2020-06",
      "url": "https://doi.org/10.1086/705716",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "NBER 작업논문(ref-1223)의 학술지 게재판. 1990~2007년 미국 722개 통근권역 지역 효과(-0.39%p, -0.77%)와 공간 파급을 반영한 총량 효과(-0.2%p, -0.42%)를 구분해 제시.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    },
    {
      "id": "ref-1561",
      "org": "Dauth, W., Findeisen, S., Suedekum, J., Woessner, N. (Journal of the European Economic Association 19(6):3104–3153)",
      "title": "The Adjustment of Labor Markets to Robots",
      "published": "2021-12",
      "url": "https://doi.org/10.1093/jeea/jvab012",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "1994~2014년 독일 행정자료 연구. 총고용 감소 효과는 없고 제조업 감소를 서비스업 노동 수요가 상쇄했다고 보고. 저자 2021-01-21판 PDF 기준(온라인 2021-05-12, 권호 2021-12).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "출처 충돌: FSQ-IC 포르투갈어판 검증 연구의 총 표본 346명과 두 분석 표본(EFA 140명 + CFA 210명 = 350명)이 맞지 않는 이유는 무엇이며, 어느 수가 실제 분석에 쓰였는가?",
      "areas": [
        60
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "Burtch·Greenwood·Ravindran(ILR Review 2025) 원논문의 표본 시설·기간·추정식·강건성 검정은 무엇이며, 로봇 센터의 중대 부상 40% 감소·비중대 부상 77% 증가는 원논문에서 어떤 조건의 추정치인가?",
      "areas": [
        60,
        61,
        49
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "알메러 모델·FSQ-IC 같은 수용성 척도를 한국어로 옮겨 국내 산업 현장 작업자(물류창고·제조·병원 직군)에게 타당화한 연구가 있는가?",
      "areas": [
        60,
        56
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "EN 301 549 V4.1.1(2026-09)은 지침 (EU) 2019/882 의 조화 표준으로 EU 관보에 인용됐는가, 인용됐다면 언제부터 어떤 범위에서 적합성 추정을 주는가?",
      "areas": [
        60,
        59
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "출처 충돌: 한림대성심병원 의료서비스로봇 만족도 조사의 원 분모(간호사 109명 대 99명)·문항·조사 시점을 밝힌 병원 원보고서가 공개돼 있는가?",
      "areas": [
        60,
        63
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "한국노동연구원 『기술 혁신과 노동시장 변화』(2024-12)의 로봇 노출도별 임금·고용 수치의 원표와 식별 조건은 무엇인가?",
      "areas": [
        60,
        3
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "Han 외(CHI 2024) 공동설계 연구 참여자의 거주 국가와 지역은 본문 어디에 명시돼 있는가?",
      "areas": [
        60,
        66
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "접근성 요구가 서로 다른 이기종 로봇(배송·안내·병원 물류)의 작업 배정과 물품 인수 완료를 실제 이용자와 현장에서 검증하는 공개 시험 세트나 시나리오가 있는가?",
      "areas": [
        60,
        25,
        54
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "이용자의 장애 관련 접근 요구(인수 높이·근접 허용·입력 수단)를 플릿에 전달할 때 필요한 최소 정보 항목과 동의·보존·삭제 절차를 정한 운영 규약이나 검증 사례가 있는가?",
      "areas": [
        60,
        53
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "실외",
      "item": "완료·인계",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    }
  ],
  "standards_updates": [
    {
      "name": "WCAG 2.2 (Web Content Accessibility Guidelines 2.2, W3C 권고 2024-12-12)",
      "kind": "표준",
      "org": "W3C Accessibility Guidelines Working Group",
      "url": "https://www.w3.org/TR/2024/REC-WCAG22-20241212/",
      "related_areas": [
        60,
        37,
        13
      ],
      "summary": "웹 콘텐츠 접근성 W3C 권고. AA 성공기준 2.5.7은 드래그 기능의 단일 포인터 대체를, 2.5.8은 예외 다섯 가지를 빼고 포인터 대상 최소 24×24 CSS 픽셀을 정한다.",
      "ref_id": "ref-1553"
    },
    {
      "name": "WCAG2ICT (Guidance on Applying WCAG 2 to Non-Web ICT, W3C Group Note 2025-12-11)",
      "kind": "프레임워크",
      "org": "W3C Accessibility Guidelines Working Group (WCAG2ICT Task Force)",
      "url": "https://www.w3.org/TR/2025/NOTE-wcag2ict-22-20251211/",
      "related_areas": [
        60,
        37
      ],
      "summary": "WCAG 2를 비웹 문서·소프트웨어에 적용하는 정보성 안내로 규범이 아니며, 제품의 하드웨어 측면은 범위에서 제외한다.",
      "ref_id": "ref-1556"
    },
    {
      "name": "EN 301 549 V4.1.1 (2026-09) ICT 제품·서비스 접근성 요구사항",
      "kind": "표준",
      "org": "ETSI / CEN / CENELEC",
      "url": "https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf",
      "related_areas": [
        60,
        59,
        37
      ],
      "summary": "ICT 접근성 유럽 표준 최종판. 닫힌 기능의 청각 정보 시각 대체(5.1.5)와 음성 없는 조작 모드(5.1.7)를 요구하며, EU 관보 인용 시 적합성 추정을 준다고 적는다(관보 인용 여부 미확인).",
      "ref_id": "ref-1555"
    },
    {
      "name": "유럽 접근성법 (Directive (EU) 2019/882)",
      "kind": "프레임워크",
      "org": "European Parliament and Council of the European Union",
      "url": "https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng",
      "related_areas": [
        60,
        59
      ],
      "summary": "2025-06-28 이후 출시되는 결제 단말기와 서비스 제공 전용 무인 단말기 등에 접근성 요구를 적용하고, 관보 게재 조화 표준 부합 시 적합성을 추정한다.",
      "ref_id": "ref-1554"
    },
    {
      "name": "axe-core (v4.14.0, 웹 접근성 자동 검사 엔진)",
      "kind": "오픈소스",
      "org": "Deque Systems",
      "url": "https://github.com/dequelabs/axe-core/tree/v4.14.0",
      "related_areas": [
        60,
        37,
        54
      ],
      "summary": "웹 접근성 자동 검사 엔진. v4.14.0의 target-size 규칙은 WCAG 2.2·EN 301 549 태그를 달고 기본 비활성으로 설정돼 있으며, 불확실한 항목은 수동 검토로 돌린다(벤더 저장소 기준).",
      "ref_id": "ref-1557"
    }
  ],
  "additional_research_requests": [
    "근로자참여법 제20조 근거 판 후속 정리: 분리된 주제 페이지 docs/topics/2026/2026-09-30-area60-s4.md(노사협의회 협의 사항 항목), 2026-09-30-area60-s6.md(노동자 참여 절차의 '법률 제16320호, 2019-07-17 시행 기준'), 2026-09-30-area60-s7.md(근로자참여법 행의 '현행 조문 여부 미확인')는 이번 실행 입력에 본문이 없어 고치지 못했다. 다음 갱신 실행에 세 주제 페이지를 입력으로 넣어 근거를 ref-1551(2022-12-11 시행판)로 바꾸고 '현행 조문 여부 미확인' 문구를 지워야 한다(1차 required_fixes 9항의 주제 페이지 부분). 같은 근거를 쓰는 field-operations-and-monitoring/index.md 와 2026-09-30-area60-s10.md 도 후속 정리가 필요하다.",
    "pipeline 분리 처리 담당 요청: 절을 주제 페이지로 자동 분리할 때 원 절에 있던 '자세한 내용은 주제 페이지 …' 링크(이전 실행의 분리 페이지)를 지우지 말고 새 주제 페이지 본문에 보존해야 한다. 이번에는 4·6·7·8·11절 갱신 내용에 '2026-09-30 실행에서 분리된 이 절의 이전 내용은 …' 링크 문장을 직접 넣어 보완했다(2차 required_fixes 1항).",
    "주제 페이지 docs/topics/2026/2026-09-30-area60-s8.md 의 Acemoglu·Restrepo 항목에 JPE 2020 게재판의 지역 효과(-0.39%p, -0.77%)와 총량 효과(-0.2%p, -0.42%)를 병기하는 정리가 필요하다(이번에는 세부영역 페이지 8절에만 더했다).",
    "5절 물류창고 사례: Malik 외(ref-1226) 면담 참여자의 국가·역할 구성·로봇 사용 경험을 원문으로 확인해야 한다(이번 실행에서 원문 접속 차단).",
    "5절 물류창고 예외·성과: Burtch 외 원논문(ILR Review 2025)의 방법과 40%/77% 추정 조건을 원문으로 확인해야 한다(현재 GMU 발표 단일 근거).",
    "11절 한국노동연구원 질문: 『기술 혁신과 노동시장 변화』(2024-12, ref-1216)의 로봇 노출도별 수치를 원표로 확인해야 질문에 수치를 다시 실을 수 있다(이번에는 출처 없는 수치를 열린 질문에서 뺐다).",
    "11절 oq-284·oq-188: 로봇 단말의 장애인차별금지법상 무인정보단말기 해당성과 국내 점자블록·연석 대기 위치 기준 자료가 필요하다.",
    "11절 oq-146·oq-278: 한국어 음성 지시 인식률 현장 자료와 로봇 관제 인력 NCS 자료가 필요하다.",
    "4·6절 수용성 측정: 예산으로 제외된 Godspeed Questionnaire Series(한국어 번역 포함)와 W3C WAI 평가 도구 선택 안내를 후속 실행에서 출처로 추가할 수 있다."
  ],
  "fixes_applied": [
    "ref-1549 제목 정정 — 13절 각주와 reference_updates 의 제목을 'Amazon invests $2.5 billion in workplace safety, reduces workplace injury rates' 로 고쳤고, 발행일 2026-03-12 에 메타데이터 기준이라는 별도 단정을 각주에 붙이지 않았다.",
    "f9 벤더 주장 병기 — 5절 물류창고 본문을 'Amazon 자사 발표(…)에 따르면'으로 시작하고 '[추정] 벤더 주장'을 붙였으며, 로봇 도입 효과를 분리한 수치가 아니라는 점을 같은 문장에 적었다.",
    "f14 범위 한정 — 5절에서 '이 위키가 인용한 Amazon의 전 세계 수치(2019년 대비 개선율)'로 한정해 SOC(미국·2024년·비Amazon 창고 대비)와 비교했고, Amazon 페이지의 미국 수치는 넣지 않았다.",
    "f25 판 표기 정정 — 7절 EN 301 549 항목을 'V4.1.0은 초안 단계 배포본(04.01.00_20 2025-11, 04.01.00_30 2026-06)'으로 쓰고 V4.1.1의 EU 관보 인용 여부를 '미확인'으로 남겼다(reference_updates 요약도 같게 고침).",
    "ref-1552 발행일 — 각주와 reference_updates 의 발행일을 2025-07-10 으로 적고 '발행일 확인 불가' 문구는 옮기지 않았으며, 6절에서 ILO 공식 입장이 아니라 Cornell ILR 저자 견해라는 점을 병기했다.",
    "f7 표본 수 — 6절 FSQ-IC 서술에 총 표본 346명과 EFA 140명 + CFA 210명 = 350명을 둘 다 제시하고 원문 안의 불일치임을 밝혔으며, 11절과 open_question_updates 에 출처 충돌 질문으로 올렸다.",
    "5절 사례 성격 — Choo·Lee Delphi는 병원 현장 유형 아래 서술로만 두어 예외·성과 칸에 넣지 않았고, Boadi-Agyemang 공동설계는 '현장 유형: 실외' 사례 표에서 예외·성과를 '해당 없음'으로 두고 연구 조건(요구·설계 연구, 접근 성공률 미측정)을 서술로 적었으며, Han 외 사례에도 화상회의 진행과 실환경 평가 필요를 연구 조건으로만 더했다.",
    "7절 접근성 기준 범위 — WCAG 2.2·WCAG2ICT·EN 301 549·지침 (EU) 2019/882 항목 앞에 기술 기준과 EU 법역 조문 범위만 정리하며 한국 ROP·개별 로봇 단말의 법적 의무를 판단한 것이 아니라는 문장을 두고, 해당성 판단(f30)을 59. 법·규제·보험·라이선스 연계 대상으로 연결했다(9절 업종별 조건 행에도 같은 연계를 적음).",
    "근로자참여법 제20조 근거 갱신 — 세부영역 페이지의 4·6·7·9절에서 제20조 근거를 ref-1551(2026-10-12 열람, 2022-12-11 시행 법률 제18927호)로 바꾸고 '열람일 이후 개정 여부는 확인하지 않았다'를 남겼다. 10절이 아직 ref-1220 을 쓰므로 그 각주 정의는 지우지 않았다. '현행 조문 여부 미확인' 문구는 이 페이지가 아니라 분리된 주제 페이지(2026-09-30-area60-s4·s6·s7)에 있어 이번 입력에 없으므로 지우지 못했고, additional_research_requests 에 후속 정리를 요청했다.",
    "ref-1226 — 13절의 기존 각주 줄(접근일 2026-09-30)을 그대로 두고 reference_updates 에 넣지 않았으며, 5절 Malik 문장은 바꾸지 않고 참여자 구성이 미확인이라는 별도 문장만 [추정]으로 더했다.",
    "인용 — 페이지에서 출처 원문을 직접 인용하지 않고 모두 한국어로 재서술했다.",
    "f46~f51 의견 주체 — 6절(f46), 5절(f47), 9절(f48·f49·f50, 표 셀 포함), 8절(f51)의 [의견] 문장마다 '이 위키 구축자의 의견'을 밝혔다.",
    "f44 — 8절 Dauth 외 항목에 '저자 2021-01-21판 기준'을 밝히고 '같은 계열의 추정 전략을 적용했을 때'로 써서 재현으로 쓰지 않았으며, 미국·독일 결과를 재현·반박으로 볼 수 없다는 f45 문장을 붙였다.",
    "한림대성심병원 원 분모 질문 — 11절의 해당 새 질문에 근거 각주를 ref-1222 로 달았다(f35 를 근거로 쓰지 않음).",
    "11절 상태 — 해결로 바꾼 질문 없이 oq-285·oq-286·oq-287·oq-284·oq-188·oq-266 을 부분 근거로만 표시하고 상태를 열림으로 유지했으며, oq-146·oq-278 은 근거 없음을 그대로 적었다. open_question_updates 에 기존 질문의 상태 변경을 내지 않았다.",
    "2차: 이전 분리 주제 페이지 링크 복원 — 4·6·8·11절 append 내용 첫머리와 7절 replace 내용의 첫 문단 뒤(기존 '자세한 내용은' 줄 자리)에 '2026-09-30 실행에서 분리된 이 절의 이전 내용은 [60. 노동·수용성·접근성 — <절 이름> (2026-09-30)](../../topics/2026/2026-09-30-area60-sN.md)에 있다.' 문장을 두었고, '자세한 내용은 주제 페이지'로 시작하지 않게 썼다. 분리 코드의 링크 보존은 additional_research_requests 로 pipeline 담당에게 요청했다.",
    "2차: 8절 Acemoglu·Restrepo 항목의 '주제 페이지에 적은 범위값'을 '[60. 노동·수용성·접근성 — 대표 연구와 자료 (2026-09-30)](../../topics/2026/2026-09-30-area60-s8.md)에 적은 범위값'으로 바꿔 링크로 밝혔다.",
    "2차: 한국노동연구원 질문 — (a)안으로 맞췄다. 11절 질문과 open_question_updates 여섯 번째 질문 모두에서 수치(고숙련·저숙련 값)를 빼고 '로봇 노출도별 임금·고용 수치의 원표와 식별 조건은 무엇인가?'로 같은 문구를 썼다.",
    "2차: 5절 실외 사례 끝 문장을 '그래서 물품 인수 사례의 예외·성과 칸은 해당 없음으로 두었다.'로 고쳐 휠체어 통행 사례 표(예외·성과 칸에 기존 사건 유지)와 맞췄다.",
    "분량 초과 자동 분리: 60. 노동·수용성·접근성 본문 16,196자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 8,001자"
  ]
}
```

### runs/2026-10-12-03/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md (8개 절)
- 분량 초과 자동 분리:
    - docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-12-area60-s7.md (2,519자)
    - docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md "11. 열린 질문" → docs/topics/2026/2026-10-12-area60-s11.md (2,273자)
    - docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-12-area60-s6.md (1,757자)
    - docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-12-area60-s8.md (1,580자)
    - docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-10-12-area60-s4.md (1,187자)
```

### runs/2026-10-12-03/pages/categories/governance-law-and-society/labor-acceptance-and-accessibility.md

```markdown
---
title: "60. 노동·수용성·접근성"
type: area
category: "P. 거버넌스·법규·사회"
area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [기술 수용 모델, 노동자 참여, 근로자 감시 설비, 무인정보단말기 접근성, 연석 경사로]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-10-12
sources: [ref-1213, ref-1214, ref-1215, ref-1216, ref-1217, ref-1218, ref-1151, ref-1219, ref-1220, ref-1221, ref-1222, ref-1223, ref-1224, ref-1225, ref-1226, ref-1547, ref-1548, ref-1549, ref-1550, ref-1551, ref-1552, ref-1553, ref-1554, ref-1555, ref-1556, ref-1557, ref-1558, ref-1559, ref-1560, ref-1561]
last_run: 2026-10-12
version: 3
---

[홈](../../index.md) › [P. 거버넌스·법규·사회](index.md) › 60. 노동·수용성·접근성

# 60. 노동·수용성·접근성

!!! info "소속 대분류"
    [P. 거버넌스·법규·사회](index.md) — 핵심 질문:
    여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

노동 영향·사회적 수용성, 고령자·장애인·어린이 접근성 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **노동 영향·사회적 수용성**: 일자리와 일하는 방식의 변화, 로봇에 대한 사회적 수용성을 다룬다
- **접근성·포용**: 고령자·장애인·어린이도 로봇 서비스를 안전하게 쓰고 피할 수 있게 한다

## 2. 핵심 질문

로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? [분류원문]

## 3. 왜 중요한가

로봇 도입이 받아들여지는지에는 한 가지 답이 없으며, 일하는 사람 쪽에서는 작업 흐름 적합성, 작업 속도와 직무 설계, 데이터 감시, 고용과 숙련 효과가 수용 여부를 가르는 것으로 보인다. [추정][^ref-1151][^ref-1213][^ref-1226][^ref-1223][^ref-1215] 이용하는 사람 쪽에서는 사회적 상호작용 요인과 보행 약자의 공간·접근성이 같은 역할을 하는 것으로 보인다. [추정][^ref-1218][^ref-1221][^ref-1214][^ref-1217]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 왜 중요한가](../../topics/2026/2026-09-30-area60-s3.md)에 있다.

## 4. 핵심 개념과 용어

**알메러 모델(Almere Model)** — 통합 기술 수용 이론(Unified Theory of Acceptance and Use of Technology, UTAUT)에 사회적 상호작용 변수를 더해 고령자의 보조 소셜 에이전트 수용성을 설명하는 모델이다(Heerink 외, 2010). [사실][^ref-1218]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 핵심 개념과 용어](../../topics/2026/2026-10-12-area60-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 근거를 찾은 현장 유형은 물류창고·병원·실외다. 제조 공장·상업 시설·가정 현장의 노동·수용성·접근성 사례는 찾지 못했다. 돌봄 로봇 수용성 연구(4·6절)는 출처가 현장 유형을 하나로 밝히지 않아 사례로 세우지 않았다.

**현장 유형:** 물류창고

**사례:** 로봇을 도입한 물류창고의 피킹 작업(흐름 단계: 피킹)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 로봇 운영에 딸려 수집되는 작업자 데이터가 작업자의 데이터 감시 우려 대상이 된다. [사실][^ref-1226] |
| 수행 자원 | 창고 작업자는 로봇 운영에서 더 주체적인 협업을 요구했다. [사실][^ref-1226] |
| 제약 | 작업자 온라인 게시글에서는 로봇 센터의 피킹 목표량이 2~3배 높다는 진술이 나왔다(GMU 발표 기준). [사실][^ref-1213] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 로봇 센터는 기존 센터보다 중대 부상이 40% 적고 비중대 부상이 77% 많았다(논문 원문이 아니라 GMU 발표 기준). [사실][^ref-1213] |

이 사례는 서로 다른 두 연구를 묶었다. Burtch·Greenwood·Ravindran 연구진의 해석으로는 자동화가 위험 작업을 없애는 대신 남은 작업의 다양성을 줄이고 작업 속도를 높여 반복성 긴장 손상 같은 비중대 부상을 늘리므로, 위험이 사라지기보다 재분배되며 직무 설계로 대응해야 한다. [의견][^ref-1213] 창고 작업자 12명 반구조화 면담 연구는 수동 무시(override)·개인정보 통제·감시 활동 알림 같은 작업자 중심 요구를 제시했다(2026). [사실][^ref-1226] 이 면담 참여자의 국가·역할 구성과 로봇 사용 경험은 2026-10-12 재확인에서 원문을 열지 못해 확인하지 못했다. [추정][^ref-1226]

예외·성과 칸의 부상 수치는 GMU 발표 하나에 기대며, 같은 주제를 다룬 다른 이해당사자 자료는 지표와 분모가 다르다. Amazon 자사 발표(2026-03-12 게시, 2026-03-27 수정)에 따르면 전 세계 운영의 기록대상 사고율(Recordable Incident Rate, RIR)은 2019년 대비 6년간 43%, 휴업 사고율(Lost Time Incident Rate, LTIR)은 70% 개선됐으며, 이 수치는 로봇 도입 효과를 분리한 것이 아니다. [추정] 벤더 주장[^ref-1549]

노동조합 쪽 자료로는 Strategic Organizing Center(SOC)의 2025-05 보고서가 있다. SOC는 보고서에서 스스로 SEIU(서비스노조)·CWA(미국통신노조)·UFW(농장노동자연합)와 협력하는 노동 조직이라고 밝히므로, 이 보고서는 노동조합 쪽 이해당사자 자료다. [사실][^ref-1550] 보고서는 Amazon과 다른 사업주가 2020~2024년 매년 미국 산업안전보건청(Occupational Safety and Health Administration, OSHA)에 제출한 부상·질병 자료를 분석했고, 경작업 전환(light duty) 또는 휴업(lost time)을 초래한 부상을 중대 부상으로 분류한다. [사실][^ref-1550] 이 정의가 GMU 발표의 중대·비중대 구분과 같은지는 확인하지 못했다. SOC의 창고 비교는 Amazon이 2024년 OSHA 보고에서 일반 창고·보관업(북미산업분류체계 NAICS 493110)으로 분류한 Amazon 자체 시설 456곳의 부상률을 비Amazon 창고 전체와 비교한 것이며(456곳은 비교 대상 창고 수가 아니다), 2024년 중대 부상률은 100명당 5.9 대 3.0이었다. [사실][^ref-1550]

이 위키가 인용한 Amazon의 전 세계 수치(2019년 대비 개선율)와 SOC 보고서(미국·2024년·비Amazon 창고 대비 수준)는 범위·기간·지표·분모가 다르고, 같은 OSHA 신고 자료에 일부 기초하며, 양쪽 모두 이해당사자 자료다. 그래서 둘을 서로 독립된 교차 확인이나 단순 모순으로 셀 수 없고, 로봇 센터만의 부상 효과는 어느 쪽에서도 분리되지 않는다. [추정][^ref-1549][^ref-1550] 이 위키 구축자의 의견으로는, 플릿 도입 효과를 평가할 때 사고 분류 정의(경작업 전환·휴업 포함 여부), 노출 시간 분모, 직군, 로봇 공정 여부, 전환 작업을 함께 기록하고 회사 발표·노조 보고서 같은 이해당사자 자료의 출처를 표시해야 하며, 처리량 증가나 안전감 설문을 실제 부상 감소의 대리값으로 쓰지 않아야 한다. [의견][^ref-1549][^ref-1550]

**현장 유형:** 병원

**사례:** 병동에 물품을 배송하는 자율 배송 로봇 TUG 도입(미국, 2008 연구)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 자율 배송 로봇이 병동으로 배송하는 물품 [사실][^ref-1151] |
| 수행 자원 | 자율 배송 로봇 TUG와 병동 직원 [사실][^ref-1151] |
| 제약 | 내과 병동은 방해에 대한 허용도가 낮았고 붐비는 통로에서 로봇 운행이 멈췄다. [사실][^ref-1151] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 내과 병동에서는 로봇이 작업 흐름을 해치고 직원 저항을 불렀지만, 산후 병동은 로봇을 작업 흐름과 사회적 맥락에 통합했다. [사실][^ref-1151] |

같은 로봇이라도 병동의 작업 흐름, 방해 허용도, 인식된 비용과 이득의 불일치, 통로 환경에 따라 수용과 저항이 갈렸다. [사실][^ref-1151]

**현장 유형:** 병원

**사례:** 병동 의료서비스로봇 운영(한국 한림대성심병원, 2022-08~2024-12)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 간호사의 단순업무와 입원환자 대상 영상 안내 [추정][^ref-1222] |
| 수행 자원 | 의료서비스로봇 11종 77대와 간호사 [추정][^ref-1222] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 누적 51,092건을 사용했고, 간호사 109명 가운데 90% 이상이 단순업무 경감, 94%가 계속 사용 희망, 입원환자 147명 가운데 93.9%가 영상 안내가 도움이 됐고 99%가 로봇에 거부감이 없다고 답했다. [추정][^ref-1222] |

이 수치는 병원 자체 만족도 조사이며 의협신문 보도(2025-01-21) 기준이다. 조사 방법은 공개되지 않았고, 다른 보도는 표본을 병동 간호사 99명(91.9%)으로 적어 간호사 109명 표본과 다르다. [추정][^ref-1222]

병원 현장 유형의 국내 학술 근거로는 서울의 한 상급종합병원 신경과 병동 6명과 뇌졸중 집중치료실 8명, 경력 7년을 넘는 간호사 14명을 전문가 패널로 3라운드 합의를 구한 Delphi 연구(Healthcare Informatics Research 32(1), 2026-01)가 있다. [사실][^ref-1558] 이 Delphi 설문은 2022-11-07부터 2023-04-12까지 실시됐다. [사실][^ref-1558] 이 연구는 급성 뇌졸중 환자 돌봄에 동반 로봇을 쓰는 미래 시나리오에 대한 단일 기관 간호사 14명의 전문가 합의이며 로봇 도입 뒤 수용률이나 간호 업무 변화를 측정한 연구가 아니므로, 한국 병원 간호사 일반이나 위 한림대성심병원 자체 설문의 독립 재현으로 볼 수 없다. [추정][^ref-1558]

**현장 유형:** 실외

**사례:** 보도에서 운행하는 배송 로봇과 휠체어 이용자의 통행(미국)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 로봇과 보행 약자가 함께 쓰는 보도 공간 [사실][^ref-1214] |
| 수행 자원 | 보도 배송 로봇과 그 운영 업체 [사실][^ref-1214] |
| 제약 | 이동장애인은 로봇이 들어오면 보도 공간을 두고 경쟁해야 한다고 느꼈다. [사실][^ref-1214] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 배송 로봇이 연석 경사로에 멈춰 횡단한 휠체어 이용자의 통행을 막았고, 이용자가 이를 공개하자 업체가 로봇 운행을 잠시 중단했다. [사실][^ref-1214] |

이동장애인 15명과 로봇 실무자 8명 면담, 공동설계 워크숍 4회로 진행한 연구(CHI 2024)에서 로봇 실무자 참여자 한 명은 연석 경사로로 다가오는 사람을 감지하면 로봇이 자동으로 경로를 다시 계획하는 기능을 제안했다. [사실][^ref-1214] 국내에서 같은 문제를 다루는 대기 위치 기준은 확인되지 않았다([oq-188](../../open-questions.md)). 이 연구의 면담과 공동설계 워크숍은 모두 화상회의로 진행됐다. [사실][^ref-1214] 저자들은 자신들의 질적 결과와 제안한 상호작용을 실제 환경에서 평가할 필요가 남아 있다고 명시했다. [사실][^ref-1214]

**현장 유형:** 실외

**사례:** 배송 로봇의 물품 인수와 장애 이용자의 접근(미국 Pittsburgh 공동설계 연구, 2025)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 배송 로봇이 이용자에게 넘기는 물품 [사실][^ref-1559] |
| 수행 자원 | 배송 로봇과 물품을 받는 장애 이용자 [사실][^ref-1559] |
| 제약 | 해당 없음 |
| 완료·인계 | 손을 뻗기 어려운 이동장애인이 물품을 인수할 때는 로봇과 가까이 상호작용하는 것이 중요하다고 참여자들이 보았다. [사실][^ref-1559] |
| 예외·성과 | 해당 없음 |

이 사례는 CMU 박사논문(CMU-RI-TR-26-106, 2026-06) 4장의 배송 로봇 공동설계이며, 2025년 미국 Pittsburgh에서 2개월간 지역 모집한 장애 성인 14명(여성 9·남성 5, 31~75세, 시각·청각·이동 장애 중심)과 진행했다. [사실][^ref-1559] 참여자들은 이 근접 요구를 보행 중 로봇과의 통행 우선권과 별개의 문제로 보았다. [사실][^ref-1559]

통행 중 충분한 간격(연석 경사로 비우기)과 물품 인수 때의 근접은 같은 이용자 집단 안에서도 상황별로 다른 요구다. 두 실외 연구는 모두 미국 소수 참여자의 요구·설계 연구이고 실제 배송의 접근 성공률을 측정하지 않았으며, 같은 CMU 계열이라 독립 교차 확인으로 세지 않는다. [추정][^ref-1214][^ref-1559] 그래서 물품 인수 사례의 예외·성과 칸은 해당 없음으로 두었다.

## 6. 대표 접근법과 기술

알메러 모델은 요양시설과 가정에서 세 가지 소셜 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다(2010). [사실][^ref-1218] 국내에서는 Q방법론으로 노인 이용자·가족·돌봄 종사자의 돌봄로봇 인식을 네 유형으로 나눴고, '불가피한 대체재' 유형의 설명력이 가장 컸다(2023). [사실][^ref-1221] 두 연구는 요양시설·가정의 고령자와 돌봄 맥락에서 수행되었다. [사실][^ref-1218][^ref-1221]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 대표 접근법과 기술](../../topics/2026/2026-10-12-area60-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역과 관련된 규정으로 접근성 지침 ISO/IEC Guide 71:2014, 장애인차별금지법에 따른 무인정보단말기 접근성 의무, 노사협의회 협의 사항을 정한 근로자참여 및 협력증진에 관한 법률 제20조, 감시 장치 공동결정을 정한 독일 사업장조직법 제87조의 네 가지를 확인했다. [사실][^ref-1224][^ref-1217][^ref-1551][^ref-1219] 이 가운데 ISO/IEC Guide 71:2014는 원문을 열지 못하고 검색 결과로만 확인했다.

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-12-area60-s7.md)에 있다.

## 8. 대표 연구와 자료

EU-OSHA(유럽 산업안전보건청), Advanced robotics and automation: implications for occupational safety and health(2022-06-16) — 사람과 협업할 수 있는 로봇 시스템의 확산이 노동자의 안전·건강·웰빙과 고용 조건에 주는 영향을 다룬 보고서다. [사실][^ref-1225]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 대표 연구와 자료](../../topics/2026/2026-10-12-area60-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 로봇과 사람의 작업 분담과 작업 속도(목표량) 설정을 드러내고 조정할 수 있게 하고, 작업자 데이터 수집 범위 표시·감시 알림·수동 무시 같은 작업자 통제 수단을 제공하는 것으로 보인다. [추정][^ref-1213][^ref-1226] 휴게 반영·작업 순환·직무 전환 정책의 변경 이력을 노사협의 기록과 연결해 남기는 것은 이 위키 구축자의 의견이다. [의견][^ref-1551][^ref-1552] | 고용·임금·재교육 정책, 노사협의·공동결정 절차와 근로자 감시 설비의 적법성 판단(사업주·노동자 대표·법무)이 연계 대상으로 보인다. [추정][^ref-1551][^ref-1219][^ref-1215] 작업과 휴게 시간의 운용과 고용조정의 일반원칙도 노사협의회 협의 사항이다(2022-12-11 시행판 제20조 제1항 제6·7호). [사실][^ref-1551] |
| 업종별 조건 | 연석 경사로·통로에서 보행 약자에게 양보하고 멈추지 않는 대기 위치 규칙을 경로·작업 제약으로 반영하고, 운영자·이용자 화면의 접근성을 갖추는 것으로 보인다. [추정][^ref-1214][^ref-1217] 화면 접근성 시험 범위를 웹 관제 화면·비웹 작업자 프로그램·로봇 단말의 닫힌 기능·로봇 본체 물리 접근으로 나누고, 보도 통행·대기·물품 인수 모드를 구분하는 것은 이 위키 구축자의 의견이다. [의견][^ref-1553][^ref-1555][^ref-1559] | 장애인차별금지법 등 접근성 법적 적합성 판단(운영자·법무)이 연계 대상으로 보인다. [추정][^ref-1217] WCAG 2.2·EN 301 549·지침 (EU) 2019/882가 로봇 단말·관제 화면에 적용되는지에 대한 판단도 조문만으로 정해지지 않아 같은 연계 대상으로 보인다. [추정][^ref-1554] |
| 로봇 자체 지능·제어 | 제조사 설계를 전제로 대기·양보 조건을 작업·경로 제약으로 로봇에 전달하는 것으로 보인다. [추정][^ref-1214] | 로봇 본체의 물리적 접근성 설계(높이·음성 조작 등)는 제조사의 몫으로 보인다. [추정][^ref-1214] |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

이 영역에서 ROP는 법적 판단을 하지 않고, 외부에서 정한 결정을 작업·경로·권한 제약과 화면 설계로 받아 반영하며 그 근거 기록을 제공하는 쪽으로 보인다. [추정][^ref-1551][^ref-1219][^ref-1217][^ref-1214][^ref-1215] 경계 전체는 [범위 경계](../../about/scope-boundary.md)에 있다.

이 위키 구축자의 의견으로는, ROP 스케줄러의 휴게 반영·작업 순환·직무 전환 정책 변경은 노사협의 기록(근로자참여법 제20조 제6·7호 협의 여부)과 연결해 이력으로 남기고, 작업자 데이터·자동 배정에 대한 이의 제기와 처리 결과를 변경 관리에 묶어야 한다. 법적 해당성 판단은 ROP가 하지 않고 외부 결정을 제약으로 받는다. [의견][^ref-1551][^ref-1552]

이 위키 구축자의 의견으로는, 접근성 시험은 브라우저 관제 화면(WCAG 2.2의 드래그 대체 조작과 24×24 CSS 픽셀 대상), 비웹 작업자 프로그램(WCAG2ICT는 안내일 뿐이다), 로봇 단말의 닫힌 기능(EN 301 549 제5.1.5·5.1.7절의 시각 경보 동등성과 음성 외 입력), 로봇 본체 물리 접근으로 범위를 나누어야 한다. 자동 검사 보고서에는 도구 버전·규칙 ID·활성화 설정을 남긴 뒤 키보드·스크린리더·실사용자 수동 검사를 더하고, 기술 시험 통과와 법적 적용 판단은 별도 기록으로 둔다. 예를 들어 다중 로봇 지도에서 드래그로 작업을 배정하는 기능에는 버튼·목록형 대체 조작이 필요하다. [의견][^ref-1553][^ref-1556][^ref-1555][^ref-1554][^ref-1557]

이 위키 구축자의 의견으로는, 플릿 경로·작업 모델은 보도 통행, 대기, 물품 인수 모드를 나누어 통행·대기 중에는 연석 경사로를 비우고 간격을 두되, 인수 때는 접근 가능한 위치·높이·입력 수단과 근접 허용을 작업 배정 조건으로 다뤄야 한다. 근접 허용은 이용자 요청과 현장 안전 평가를 전제로 시험한다. [의견][^ref-1214][^ref-1559]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 작업 분담·속도로 25. 작업 배정 — MRTA와 31. 사람–로봇 협업, 부상으로 49. 사람 근접 안전, 작업자 데이터 감시로 53. 개인정보·영상 데이터, 보행 약자와 대기 위치로 19. 사람·보행자 모델과 16. 장소 의미·지도 관리, 목표량 지표로 39. 운영 성과 측정·개선, 도입 절차로 56. 운영 이관·확대·교육, 화면 접근성으로 37. 관제 화면·실행 기록과 13. 대화형 기능의 신뢰·기반, 법 의무로 59. 법·규제·보험·라이선스, 효과 추정으로 3. 경제성·조달·사업 모델, 적용 현장으로 61. 물류창고·63. 병원·의료·66. 실외와 이어지는 것으로 보인다. [추정][^ref-1213][^ref-1226][^ref-1214][^ref-1151][^ref-1217][^ref-1220][^ref-1219][^ref-1223][^ref-1215][^ref-1222]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area60-s10.md)에 있다.

## 11. 열린 질문

**oq-146** (상태: 열림) 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가? 이번 조사에서도 근거를 찾지 못했다.

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 열린 질문](../../topics/2026/2026-10-12-area60-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [60. 노동·수용성·접근성](labor-acceptance-and-accessibility.md) — 영역 심화: 3~11절 첫 작성(물류창고·병원·실외 적용 사례 4건, 수용성 모델·노동자 참여 절차·접근성 의무, 책임 경계, 연결 15개 영역, 열린 질문 8건), 각주 15건. 2차 수정: 6절 의견 주체 명시, 5절 물류창고 수행 자원 칸 드리프트 제거, 7절 도입 문장, 10절 요약 첫 문장 (실행 2026-09-30-24)
- 2026-09-30 · 생성 · [60. 노동·수용성·접근성 — 대표 연구와 자료](../../topics/2026/2026-09-30-area60-s8.md) — 자동 분리: 60. 노동·수용성·접근성 의 "8. 대표 연구와 자료" 절(1,290자)을 옮겼다 (실행 2026-09-30-24)
- 2026-09-30 · 생성 · [60. 노동·수용성·접근성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area60-s7.md) — 자동 분리: 60. 노동·수용성·접근성 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,060자)을 옮겼다 (실행 2026-09-30-24)
- 2026-09-30 · 생성 · [60. 노동·수용성·접근성 — 열린 질문](../../topics/2026/2026-09-30-area60-s11.md) — 자동 분리: 60. 노동·수용성·접근성 의 "11. 열린 질문" 절(1,002자)을 옮겼다 (실행 2026-09-30-24)
- 2026-09-30 · 생성 · [60. 노동·수용성·접근성 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area60-s4.md) — 자동 분리: 60. 노동·수용성·접근성 의 "4. 핵심 개념과 용어" 절(985자)을 옮겼다 (실행 2026-09-30-24)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1213]: George Mason University Costello College of Business, Warehouse automation hasn't made workers safer — it's just reshuffled risk, 2025-08-26, https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk, 접근일 2026-09-30
[^ref-1214]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-09-30
[^ref-1215]: 한국경제, 로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인), 2025-04-01, https://www.hankyung.com/article/2025040138391, 접근일 2026-09-30
[^ref-1217]: 대한민국 정책브리핑 (보건복지부), 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행, 2026-01-28, https://www.korea.kr/news/policyNewsView.do?newsId=148958690, 접근일 2026-09-30
[^ref-1218]: Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics), Assessing acceptance of assistive social agent technology by older adults: the Almere model, 2010, https://doi.org/10.1007/s12369-010-0068-5, 접근일 2026-09-30
[^ref-1151]: Mutlu, B., Forlizzi, J. (HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30
[^ref-1219]: Bundesministerium der Justiz (gesetze-im-internet.de), Betriebsverfassungsgesetz § 87 Mitbestimmungsrechte, 미확인, https://www.gesetze-im-internet.de/betrvg/__87.html, 접근일 2026-09-30
[^ref-1220]: 대한민국 국회 (법률 제16320호, 케이스노트 게재), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항), 2019-04-16, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0, 접근일 2026-09-30
[^ref-1221]: 김소라 (주관성 연구, 한국주관성연구학회), 돌봄로봇에 대한 돌봄서비스 종사자와 사용자의 인식 유형 연구, 2023, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002970146, 접근일 2026-09-30
[^ref-1222]: 의협신문, "로봇이 병원을 돌아다닌다"…의료서비스로봇 5만건 돌파, 2025-01-21, https://www.doctorsnews.co.kr/news/articleView.html?idxno=158208, 접근일 2026-09-30
[^ref-1223]: Acemoglu, D., Restrepo, P. (NBER), Robots and Jobs: Evidence from US Labor Markets, 2017-03, https://www.nber.org/papers/w23285, 접근일 2026-09-30
[^ref-1224]: ISO/IEC, ISO/IEC Guide 71:2014 Guide for addressing accessibility in standards, 2014-12, https://www.iso.org/standard/57385.html, 접근일 2026-09-30 (원문 미열람)
[^ref-1225]: European Agency for Safety and Health at Work (EU-OSHA), Advanced robotics and automation: implications for occupational safety and health, 2022-06-16, https://osha.europa.eu/en/publications/advanced-robotics-and-automation-implications-occupational-safety-and-health, 접근일 2026-09-30
[^ref-1226]: Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics), Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety, 2026, https://doi.org/10.1007/s12369-026-01359-1, 접근일 2026-09-30
[^ref-1549]: Amazon (Sarah Rhoads, VP Global Workplace Health & Safety), Amazon invests $2.5 billion in workplace safety, reduces workplace injury rates, 2026-03-12, https://www.aboutamazon.com/news/workplace/amazon-workplace-safety-2025-injury-reduction, 접근일 2026-10-12
[^ref-1550]: Strategic Organizing Center (SOC; SEIU·CWA·UFW 연계 노동 조직), Failure to Deliver: Amazon Falls Short on Safety, 2025-05, https://thesoc.org/wp-content/uploads/2025/05/May-2025_Strategic-Organizing-Center_Report-x-Failure-To-Deliver.pdf, 접근일 2026-10-12
[^ref-1551]: 법제처 국가법령정보센터 (대한민국, 법률 제18927호), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) 시행 2022-12-11 법률 제18927호(2022-06-10 일부개정), 2022-06-10, https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017145541, 접근일 2026-10-12
[^ref-1552]: Doellgast, V., Appalla, S., Ginzburg, D., Kim, J., Thian, W. L. (Cornell University ILR School) — ILO Working Paper 144, Global case studies of social dialogue on AI and algorithmic management, 2025-07-10, https://doi.org/10.54394/VOQE4924, 접근일 2026-10-12
[^ref-1553]: W3C Accessibility Guidelines Working Group, Web Content Accessibility Guidelines (WCAG) 2.2 (W3C Recommendation 12 December 2024), 2024-12-12, https://www.w3.org/TR/2024/REC-WCAG22-20241212/, 접근일 2026-10-12
[^ref-1554]: European Parliament and Council of the European Union (Official Journal L 151), Directive (EU) 2019/882 of 17 April 2019 on the accessibility requirements for products and services, 2019-06-07, https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng, 접근일 2026-10-12
[^ref-1555]: ETSI / CEN / CENELEC, EN 301 549 V4.1.1 (2026-09) Accessibility requirements for ICT products and services, 2026-09, https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf, 접근일 2026-10-12
[^ref-1556]: W3C Accessibility Guidelines Working Group (WCAG2ICT Task Force), Guidance on Applying WCAG 2 to Non-Web Information and Communications Technologies (WCAG2ICT), W3C Group Note 11 December 2025, 2025-12-11, https://www.w3.org/TR/2025/NOTE-wcag2ict-22-20251211/, 접근일 2026-10-12
[^ref-1557]: Deque Systems / axe-core contributors, axe-core v4.14.0 (lib/rules/target-size.json, README, CHANGELOG), 2026-10-05, https://github.com/dequelabs/axe-core/tree/v4.14.0, 접근일 2026-10-12
[^ref-1558]: Choo, H.-J., Lee, S.-M. (Healthcare Informatics Research 32(1):59–68), Nurses' Perceptions and Utilization Plans for Applying Companion Robots to Acute Stroke Patient Care: A Delphi Study, 2026-01, https://doi.org/10.4258/hir.2026.32.1.59, 접근일 2026-10-12
[^ref-1559]: Boadi-Agyemang, A. (Carnegie Mellon University Robotics Institute, CMU-RI-TR-26-106), From Margin to Center: Designing Inclusive and Equitable Service Robots with Disabled Adults (PhD thesis), 2026-06, https://publications.ri.cmu.edu/storage/publications/2026/09/aboadiag-dissertation2026-manual-tagged-v2_20260902085808.pdf, 접근일 2026-10-12
```

### docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md

```markdown
---
title: "60. 노동·수용성·접근성"
type: area
category: "P. 거버넌스·법규·사회"
area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [기술 수용 모델, 노동자 참여, 근로자 감시 설비, 무인정보단말기 접근성, 연석 경사로]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1213, ref-1214, ref-1215, ref-1216, ref-1217, ref-1218, ref-1151, ref-1219, ref-1220, ref-1221, ref-1222, ref-1223, ref-1224, ref-1225, ref-1226]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [P. 거버넌스·법규·사회](index.md) › 60. 노동·수용성·접근성

# 60. 노동·수용성·접근성

!!! info "소속 대분류"
    [P. 거버넌스·법규·사회](index.md) — 핵심 질문:
    여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

노동 영향·사회적 수용성, 고령자·장애인·어린이 접근성 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **노동 영향·사회적 수용성**: 일자리와 일하는 방식의 변화, 로봇에 대한 사회적 수용성을 다룬다
- **접근성·포용**: 고령자·장애인·어린이도 로봇 서비스를 안전하게 쓰고 피할 수 있게 한다

## 2. 핵심 질문

로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? [분류원문]

## 3. 왜 중요한가

로봇 도입이 받아들여지는지에는 한 가지 답이 없으며, 일하는 사람 쪽에서는 작업 흐름 적합성, 작업 속도와 직무 설계, 데이터 감시, 고용과 숙련 효과가 수용 여부를 가르는 것으로 보인다. [추정][^ref-1151][^ref-1213][^ref-1226][^ref-1223][^ref-1215] 이용하는 사람 쪽에서는 사회적 상호작용 요인과 보행 약자의 공간·접근성이 같은 역할을 하는 것으로 보인다. [추정][^ref-1218][^ref-1221][^ref-1214][^ref-1217]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 왜 중요한가](../../topics/2026/2026-09-30-area60-s3.md)에 있다.

## 4. 핵심 개념과 용어

**알메러 모델(Almere Model)** — 통합 기술 수용 이론(Unified Theory of Acceptance and Use of Technology, UTAUT)에 사회적 상호작용 변수를 더해 고령자의 보조 소셜 에이전트 수용성을 설명하는 모델이다(Heerink 외, 2010). [사실][^ref-1218]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area60-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 근거를 찾은 현장 유형은 물류창고·병원·실외다. 제조 공장·상업 시설·가정 현장의 노동·수용성·접근성 사례는 찾지 못했다. 돌봄 로봇 수용성 연구(4·6절)는 출처가 현장 유형을 하나로 밝히지 않아 사례로 세우지 않았다.

**현장 유형:** 물류창고

**사례:** 로봇을 도입한 물류창고의 피킹 작업(흐름 단계: 피킹)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 로봇 운영에 딸려 수집되는 작업자 데이터가 작업자의 데이터 감시 우려 대상이 된다. [사실][^ref-1226] |
| 수행 자원 | 창고 작업자는 로봇 운영에서 더 주체적인 협업을 요구했다. [사실][^ref-1226] |
| 제약 | 작업자 온라인 게시글에서는 로봇 센터의 피킹 목표량이 2~3배 높다는 진술이 나왔다(GMU 발표 기준). [사실][^ref-1213] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 로봇 센터는 기존 센터보다 중대 부상이 40% 적고 비중대 부상이 77% 많았다(논문 원문이 아니라 GMU 발표 기준). [사실][^ref-1213] |

이 사례는 서로 다른 두 연구를 묶었다. Burtch·Greenwood·Ravindran 연구진의 해석으로는 자동화가 위험 작업을 없애는 대신 남은 작업의 다양성을 줄이고 작업 속도를 높여 반복성 긴장 손상 같은 비중대 부상을 늘리므로, 위험이 사라지기보다 재분배되며 직무 설계로 대응해야 한다. [의견][^ref-1213] 창고 작업자 12명 반구조화 면담 연구는 수동 무시(override)·개인정보 통제·감시 활동 알림 같은 작업자 중심 요구를 제시했다(2026). [사실][^ref-1226]

**현장 유형:** 병원

**사례:** 병동에 물품을 배송하는 자율 배송 로봇 TUG 도입(미국, 2008 연구)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 자율 배송 로봇이 병동으로 배송하는 물품 [사실][^ref-1151] |
| 수행 자원 | 자율 배송 로봇 TUG와 병동 직원 [사실][^ref-1151] |
| 제약 | 내과 병동은 방해에 대한 허용도가 낮았고 붐비는 통로에서 로봇 운행이 멈췄다. [사실][^ref-1151] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 내과 병동에서는 로봇이 작업 흐름을 해치고 직원 저항을 불렀지만, 산후 병동은 로봇을 작업 흐름과 사회적 맥락에 통합했다. [사실][^ref-1151] |

같은 로봇이라도 병동의 작업 흐름, 방해 허용도, 인식된 비용과 이득의 불일치, 통로 환경에 따라 수용과 저항이 갈렸다. [사실][^ref-1151]

**현장 유형:** 병원

**사례:** 병동 의료서비스로봇 운영(한국 한림대성심병원, 2022-08~2024-12)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 간호사의 단순업무와 입원환자 대상 영상 안내 [추정][^ref-1222] |
| 수행 자원 | 의료서비스로봇 11종 77대와 간호사 [추정][^ref-1222] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 누적 51,092건을 사용했고, 간호사 109명 가운데 90% 이상이 단순업무 경감, 94%가 계속 사용 희망, 입원환자 147명 가운데 93.9%가 영상 안내가 도움이 됐고 99%가 로봇에 거부감이 없다고 답했다. [추정][^ref-1222] |

이 수치는 병원 자체 만족도 조사이며 의협신문 보도(2025-01-21) 기준이다. 조사 방법은 공개되지 않았고, 다른 보도는 표본을 병동 간호사 99명(91.9%)으로 적어 간호사 109명 표본과 다르다. [추정][^ref-1222]

**현장 유형:** 실외

**사례:** 보도에서 운행하는 배송 로봇과 휠체어 이용자의 통행(미국)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 로봇과 보행 약자가 함께 쓰는 보도 공간 [사실][^ref-1214] |
| 수행 자원 | 보도 배송 로봇과 그 운영 업체 [사실][^ref-1214] |
| 제약 | 이동장애인은 로봇이 들어오면 보도 공간을 두고 경쟁해야 한다고 느꼈다. [사실][^ref-1214] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 배송 로봇이 연석 경사로에 멈춰 횡단한 휠체어 이용자의 통행을 막았고, 이용자가 이를 공개하자 업체가 로봇 운행을 잠시 중단했다. [사실][^ref-1214] |

이동장애인 15명과 로봇 실무자 8명 면담, 공동설계 워크숍 4회로 진행한 연구(CHI 2024)에서 로봇 실무자 참여자 한 명은 연석 경사로로 다가오는 사람을 감지하면 로봇이 자동으로 경로를 다시 계획하는 기능을 제안했다. [사실][^ref-1214] 국내에서 같은 문제를 다루는 대기 위치 기준은 확인되지 않았다([oq-188](../../open-questions.md)).

## 6. 대표 접근법과 기술

알메러 모델은 요양시설과 가정에서 세 가지 소셜 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다(2010). [사실][^ref-1218] 국내에서는 Q방법론으로 노인 이용자·가족·돌봄 종사자의 돌봄로봇 인식을 네 유형으로 나눴고, '불가피한 대체재' 유형의 설명력이 가장 컸다(2023). [사실][^ref-1221] 두 연구는 요양시설·가정의 고령자와 돌봄 맥락에서 수행되었다. [사실][^ref-1218][^ref-1221]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area60-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역과 관련된 규정으로 접근성 지침 ISO/IEC Guide 71:2014, 장애인차별금지법에 따른 무인정보단말기 접근성 의무, 노사협의회 협의 사항을 정한 근로자참여 및 협력증진에 관한 법률 제20조, 감시 장치 공동결정을 정한 독일 사업장조직법 제87조의 네 가지를 확인했다. [사실][^ref-1224][^ref-1217][^ref-1220][^ref-1219] 이 가운데 ISO/IEC Guide 71:2014는 원문을 열지 못하고 검색 결과로만 확인했다.

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area60-s7.md)에 있다.

## 8. 대표 연구와 자료

EU-OSHA(유럽 산업안전보건청), Advanced robotics and automation: implications for occupational safety and health(2022-06-16) — 사람과 협업할 수 있는 로봇 시스템의 확산이 노동자의 안전·건강·웰빙과 고용 조건에 주는 영향을 다룬 보고서다. [사실][^ref-1225]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 대표 연구와 자료](../../topics/2026/2026-09-30-area60-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 로봇과 사람의 작업 분담과 작업 속도(목표량) 설정을 드러내고 조정할 수 있게 하고, 작업자 데이터 수집 범위 표시·감시 알림·수동 무시 같은 작업자 통제 수단을 제공하는 것으로 보인다. [추정][^ref-1213][^ref-1226] | 고용·임금·재교육 정책, 노사협의·공동결정 절차와 근로자 감시 설비의 적법성 판단(사업주·노동자 대표·법무)이 연계 대상으로 보인다. [추정][^ref-1220][^ref-1219][^ref-1215] |
| 업종별 조건 | 연석 경사로·통로에서 보행 약자에게 양보하고 멈추지 않는 대기 위치 규칙을 경로·작업 제약으로 반영하고, 운영자·이용자 화면의 접근성을 갖추는 것으로 보인다. [추정][^ref-1214][^ref-1217] | 장애인차별금지법 등 접근성 법적 적합성 판단(운영자·법무)이 연계 대상으로 보인다. [추정][^ref-1217] |
| 로봇 자체 지능·제어 | 제조사 설계를 전제로 대기·양보 조건을 작업·경로 제약으로 로봇에 전달하는 것으로 보인다. [추정][^ref-1214] | 로봇 본체의 물리적 접근성 설계(높이·음성 조작 등)는 제조사의 몫으로 보인다. [추정][^ref-1214] |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

이 영역에서 ROP는 법적 판단을 하지 않고, 외부에서 정한 결정을 작업·경로·권한 제약과 화면 설계로 받아 반영하며 그 근거 기록을 제공하는 쪽으로 보인다. [추정][^ref-1220][^ref-1219][^ref-1217][^ref-1214][^ref-1215] 경계 전체는 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 작업 분담·속도로 25. 작업 배정 — MRTA와 31. 사람–로봇 협업, 부상으로 49. 사람 근접 안전, 작업자 데이터 감시로 53. 개인정보·영상 데이터, 보행 약자와 대기 위치로 19. 사람·보행자 모델과 16. 장소 의미·지도 관리, 목표량 지표로 39. 운영 성과 측정·개선, 도입 절차로 56. 운영 이관·확대·교육, 화면 접근성으로 37. 관제 화면·실행 기록과 13. 대화형 기능의 신뢰·기반, 법 의무로 59. 법·규제·보험·라이선스, 효과 추정으로 3. 경제성·조달·사업 모델, 적용 현장으로 61. 물류창고·63. 병원·의료·66. 실외와 이어지는 것으로 보인다. [추정][^ref-1213][^ref-1226][^ref-1214][^ref-1151][^ref-1217][^ref-1220][^ref-1219][^ref-1223][^ref-1215][^ref-1222]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area60-s10.md)에 있다.

## 11. 열린 질문

**oq-146** (상태: 열림) 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가? 이번 조사에서도 근거를 찾지 못했다.

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 열린 질문](../../topics/2026/2026-09-30-area60-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [60. 노동·수용성·접근성](labor-acceptance-and-accessibility.md) — 영역 심화: 3~11절 첫 작성(물류창고·병원·실외 적용 사례 4건, 수용성 모델·노동자 참여 절차·접근성 의무, 책임 경계, 연결 15개 영역, 열린 질문 8건), 각주 15건. 2차 수정: 6절 의견 주체 명시, 5절 물류창고 수행 자원 칸 드리프트 제거, 7절 도입 문장, 10절 요약 첫 문장 (실행 2026-09-30-24)
- 2026-09-30 · 생성 · [60. 노동·수용성·접근성 — 대표 연구와 자료](../../topics/2026/2026-09-30-area60-s8.md) — 자동 분리: 60. 노동·수용성·접근성 의 "8. 대표 연구와 자료" 절(1,290자)을 옮겼다 (실행 2026-09-30-24)
- 2026-09-30 · 생성 · [60. 노동·수용성·접근성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area60-s7.md) — 자동 분리: 60. 노동·수용성·접근성 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,060자)을 옮겼다 (실행 2026-09-30-24)
- 2026-09-30 · 생성 · [60. 노동·수용성·접근성 — 열린 질문](../../topics/2026/2026-09-30-area60-s11.md) — 자동 분리: 60. 노동·수용성·접근성 의 "11. 열린 질문" 절(1,002자)을 옮겼다 (실행 2026-09-30-24)
- 2026-09-30 · 생성 · [60. 노동·수용성·접근성 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area60-s4.md) — 자동 분리: 60. 노동·수용성·접근성 의 "4. 핵심 개념과 용어" 절(985자)을 옮겼다 (실행 2026-09-30-24)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1213]: George Mason University Costello College of Business, Warehouse automation hasn't made workers safer — it's just reshuffled risk, 2025-08-26, https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk, 접근일 2026-09-30
[^ref-1214]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-09-30
[^ref-1215]: 한국경제, 로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인), 2025-04-01, https://www.hankyung.com/article/2025040138391, 접근일 2026-09-30
[^ref-1217]: 대한민국 정책브리핑 (보건복지부), 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행, 2026-01-28, https://www.korea.kr/news/policyNewsView.do?newsId=148958690, 접근일 2026-09-30
[^ref-1218]: Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics), Assessing acceptance of assistive social agent technology by older adults: the Almere model, 2010, https://doi.org/10.1007/s12369-010-0068-5, 접근일 2026-09-30
[^ref-1151]: Mutlu, B., Forlizzi, J. (HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30
[^ref-1219]: Bundesministerium der Justiz (gesetze-im-internet.de), Betriebsverfassungsgesetz § 87 Mitbestimmungsrechte, 미확인, https://www.gesetze-im-internet.de/betrvg/__87.html, 접근일 2026-09-30
[^ref-1220]: 대한민국 국회 (법률 제16320호, 케이스노트 게재), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항), 2019-04-16, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0, 접근일 2026-09-30
[^ref-1221]: 김소라 (주관성 연구, 한국주관성연구학회), 돌봄로봇에 대한 돌봄서비스 종사자와 사용자의 인식 유형 연구, 2023, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002970146, 접근일 2026-09-30
[^ref-1222]: 의협신문, "로봇이 병원을 돌아다닌다"…의료서비스로봇 5만건 돌파, 2025-01-21, https://www.doctorsnews.co.kr/news/articleView.html?idxno=158208, 접근일 2026-09-30
[^ref-1223]: Acemoglu, D., Restrepo, P. (NBER), Robots and Jobs: Evidence from US Labor Markets, 2017-03, https://www.nber.org/papers/w23285, 접근일 2026-09-30
[^ref-1224]: ISO/IEC, ISO/IEC Guide 71:2014 Guide for addressing accessibility in standards, 2014-12, https://www.iso.org/standard/57385.html, 접근일 2026-09-30 (원문 미열람)
[^ref-1225]: European Agency for Safety and Health at Work (EU-OSHA), Advanced robotics and automation: implications for occupational safety and health, 2022-06-16, https://osha.europa.eu/en/publications/advanced-robotics-and-automation-implications-occupational-safety-and-health, 접근일 2026-09-30
[^ref-1226]: Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics), Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety, 2026, https://doi.org/10.1007/s12369-026-01359-1, 접근일 2026-09-30
```

### runs/2026-10-12-03/pages/topics/2026/2026-10-12-area60-s7.md

```markdown
---
title: "60. 노동·수용성·접근성 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1217, ref-1219, ref-1224, ref-1551, ref-1553, ref-1554, ref-1555, ref-1556, ref-1557]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#7
---

[홈](../../index.md) › [주제](../index.md) › 60. 노동·수용성·접근성 — 관련 표준·프레임워크·오픈소스

# 60. 노동·수용성·접근성 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역과 관련된 규정으로 접근성 지침 ISO/IEC Guide 71:2014, 장애인차별금지법에 따른 무인정보단말기 접근성 의무, 노사협의회 협의 사항을 정한 근로자참여 및 협력증진에 관한 법률 제20조, 감시 장치 공동결정을 정한 독일 사업장조직법 제87조의 네 가지를 확인했다. [사실][^ref-1224][^ref-1217][^ref-1551][^ref-1219] 이 가운데 ISO/IEC Guide 71:2014는 원문을 열지 못하고 검색 결과로만 확인했다.
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역과 관련된 규정으로 접근성 지침 ISO/IEC Guide 71:2014, 장애인차별금지법에 따른 무인정보단말기 접근성 의무, 노사협의회 협의 사항을 정한 근로자참여 및 협력증진에 관한 법률 제20조, 감시 장치 공동결정을 정한 독일 사업장조직법 제87조의 네 가지를 확인했다. [사실][^ref-1224][^ref-1217][^ref-1551][^ref-1219] 이 가운데 ISO/IEC Guide 71:2014는 원문을 열지 못하고 검색 결과로만 확인했다.

2026-09-30 실행에서 분리된 이 절의 이전 내용은 [60. 노동·수용성·접근성 — 관련 표준·프레임워크·오픈소스 (2026-09-30)](2026-09-30-area60-s7.md)에 있다.

### 2026-10-12 갱신: 근로자참여법 근거 판과 디지털 접근성 기준

- **근로자참여 및 협력증진에 관한 법률 제20조(2022-12-11 시행, 법률 제18927호)** — 2026-10-12 국가법령정보센터 열람판의 제1항은 제2호(채용·배치 및 교육훈련), 제6호(고용조정의 일반원칙), 제7호(작업과 휴게 시간의 운용), 제9호(신기계·기술의 도입 또는 작업 공정의 개선), 제14호(근로자 감시 설비의 설치)를 노사협의회 협의 사항으로 둔다. [사실][^ref-1551] 열람일 이후 개정 여부는 확인하지 않았다.

아래 디지털 접근성 항목은 기술 기준과 EU 법역의 조문 범위를 정리한 것이며, 한국 ROP나 개별 로봇 단말에 적용되는 법적 의무를 판단한 것이 아니다. 적용 여부의 판단은 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)의 연계 대상이다.

- **WCAG 2.2(W3C 권고, 2024-12-12판)** — 웹 콘텐츠 접근성 지침(Web Content Accessibility Guidelines)이다. AA 성공기준 2.5.7(드래그 동작)은 드래그가 필수이거나 기능을 사용자 에이전트가 정하고 저자가 수정하지 않은 경우가 아니면, 드래그로 하는 모든 기능을 드래그 없이 단일 포인터로 수행할 수 있어야 한다고 정한다. [사실][^ref-1553] AA 성공기준 2.5.8(최소 대상 크기)은 간격·동등한 대체·인라인·사용자 에이전트 제어·필수의 다섯 예외를 빼면 포인터 입력 대상의 크기를 최소 24×24 CSS 픽셀로 정한다. [사실][^ref-1553] CSS 픽셀은 화면 단위이며 로봇 본체 물리 버튼의 치수가 아니다.
- **WCAG2ICT(W3C Group Note, 2025-12-11)** — WCAG 2를 비웹 문서·소프트웨어에 적용하는 방법에 대한 정보성 안내이며, 규범이 아니고 요구사항을 정하지 않는다고 스스로 밝힌다. [사실][^ref-1556] 제품의 하드웨어 측면은 다루지 않는다고 적용 범위에서 제외한다. [사실][^ref-1556]
- **EN 301 549 V4.1.1(2026-09)** — ETSI·CEN·CENELEC의 ICT 제품·서비스 접근성 유럽 표준이다. 최종판은 V4.1.1(배포본 04.01.01_60)이며, V4.1.0은 초안 단계 배포본(04.01.00_20 2025-11, 04.01.00_30 2026-06)이다. 머리말은 이 문서가 지침 (EU) 2019/882를 위한 표준화 요청 C(2022) 6456에 따라 준비됐고, EU 관보에 인용되면 적합성 추정을 준다고 적는다. [사실][^ref-1555] V4.1.1의 EU 관보 인용 여부는 미확인이다. 제5.1.5절은 닫힌 기능(closed functionality)을 쓰는 데 청각 출력이 필요하면 그 청각 정보와 동등한 시각 정보를 제공하도록 요구하고, 제5.1.7절은 닫힌 기능을 조작하는 데 음성이 필요하면 음성을 요구하지 않는 대체 입력 방식의 조작 모드를 적어도 하나 제공하도록 요구한다. [사실][^ref-1555] 두 조항은 닫힌 기능이 있을 때의 조건부 요구이므로 그런 조건이 없는 로봇에 일률 적용하지 않는다.
- **유럽 접근성법(지침 (EU) 2019/882)** — 제2조 제1항 (b)는 2025-06-28 이후 출시되는 무인 단말기 가운데 (i) 결제 단말기는 한정 없이 열거하고, (ii) 현금자동인출기·발권기·체크인기·정보 제공 대화형 무인 단말기는 이 지침이 다루는 서비스 제공 전용인 것으로 한정한다. [사실][^ref-1554] 제15조 제1항은 EU 관보에 참조가 게재된 조화 표준(또는 그 일부)에 부합하는 제품·서비스가 그 표준이 다루는 범위에서 이 지침의 접근성 요구에 부합하는 것으로 추정된다고 정한다. [사실][^ref-1554] 로봇 본체 터치스크린, 기업용(B2B) 관제 화면, 작업자용 사람–기계 인터페이스(Human-Machine Interface, HMI)가 제2조의 열거 제품·서비스에 드는지는 조문만으로 정해지지 않으며, 결제 기능이 있는 로봇 단말은 (i) 결제 단말기 해당 여부를, 정보 안내 화면은 (ii)의 서비스 제공 전용 요건을 따로 검토해야 하는 것으로 보인다. [추정][^ref-1554]
- **axe-core v4.14.0(Deque Systems, CHANGELOG 2026-10-05)** — 웹 접근성 자동 검사 오픈소스 엔진이다. v4.14.0 태그의 target-size 규칙 정의에는 wcag22aa·wcag258·EN-301-549v4·EN-9.2.5.8 태그가 붙어 있고 enabled 값이 false로 설정돼 있다. [추정] 벤더 주장[^ref-1557] 그래서 이 규칙은 기본 실행에서 빠지는 것으로 보이며, EN 301 549 태그를 지정해 실행할 때 켜지는지는 설정에 달려 있어 실행 시험으로 확인하지 않았다. README는 자동 판단이 불확실한 항목을 incomplete로 돌려 수동 검토가 필요하다고 안내한다. [추정] 벤더 주장[^ref-1557]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1217]: 대한민국 정책브리핑 (보건복지부), 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행, 2026-01-28, https://www.korea.kr/news/policyNewsView.do?newsId=148958690, 접근일 2026-09-30
[^ref-1219]: Bundesministerium der Justiz (gesetze-im-internet.de), Betriebsverfassungsgesetz § 87 Mitbestimmungsrechte, 미확인, https://www.gesetze-im-internet.de/betrvg/__87.html, 접근일 2026-09-30
[^ref-1224]: ISO/IEC, ISO/IEC Guide 71:2014 Guide for addressing accessibility in standards, 2014-12, https://www.iso.org/standard/57385.html, 접근일 2026-09-30 (원문 미열람)
[^ref-1551]: 법제처 국가법령정보센터 (대한민국, 법률 제18927호), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) 시행 2022-12-11 법률 제18927호(2022-06-10 일부개정), 2022-06-10, https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017145541, 접근일 2026-10-12
[^ref-1553]: W3C Accessibility Guidelines Working Group, Web Content Accessibility Guidelines (WCAG) 2.2 (W3C Recommendation 12 December 2024), 2024-12-12, https://www.w3.org/TR/2024/REC-WCAG22-20241212/, 접근일 2026-10-12
[^ref-1554]: European Parliament and Council of the European Union (Official Journal L 151), Directive (EU) 2019/882 of 17 April 2019 on the accessibility requirements for products and services, 2019-06-07, https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng, 접근일 2026-10-12
[^ref-1555]: ETSI / CEN / CENELEC, EN 301 549 V4.1.1 (2026-09) Accessibility requirements for ICT products and services, 2026-09, https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf, 접근일 2026-10-12
[^ref-1556]: W3C Accessibility Guidelines Working Group (WCAG2ICT Task Force), Guidance on Applying WCAG 2 to Non-Web Information and Communications Technologies (WCAG2ICT), W3C Group Note 11 December 2025, 2025-12-11, https://www.w3.org/TR/2025/NOTE-wcag2ict-22-20251211/, 접근일 2026-10-12
[^ref-1557]: Deque Systems / axe-core contributors, axe-core v4.14.0 (lib/rules/target-size.json, README, CHANGELOG), 2026-10-05, https://github.com/dequelabs/axe-core/tree/v4.14.0, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-03 | 60. 노동·수용성·접근성 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-12-03/pages/topics/2026/2026-10-12-area60-s11.md

```markdown
---
title: "60. 노동·수용성·접근성 — 열린 질문"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1213, ref-1214, ref-1222, ref-1548, ref-1549, ref-1550, ref-1551, ref-1552, ref-1554, ref-1555, ref-1558, ref-1559]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#11
---

[홈](../../index.md) › [주제](../index.md) › 60. 노동·수용성·접근성 — 열린 질문

# 60. 노동·수용성·접근성 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **oq-146** (상태: 열림) 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가? 이번 조사에서도 근거를 찾지 못했다.
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

**oq-146** (상태: 열림) 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가? 이번 조사에서도 근거를 찾지 못했다.


2026-09-30 실행에서 분리된 이 절의 이전 내용은 [60. 노동·수용성·접근성 — 열린 질문 (2026-09-30)](2026-09-30-area60-s11.md)에 있다.

### 2026-10-12 갱신: 기존 질문의 부분 근거

이번 갱신으로 해결된 질문은 없으며, 아래 질문은 모두 열림 상태로 둔다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-285** (상태: 열림) 부분 근거: 근로자참여법 제20조 2022-12-11 시행판이 제6·7·14호를 협의 사항으로 둔다는 것은 확인했지만, ROP 기록·배정 정책이 협의 대상에 해당하는지에 대한 판례·행정해석은 찾지 못했다. [추정][^ref-1551]
- **oq-286** (상태: 열림) 부분 근거: Amazon 자사 발표와 SOC 노조 보고서를 더했으나 둘은 지표·분모가 다른 이해당사자 자료이고 로봇 센터의 효과를 분리하지 않는다(5절). [추정][^ref-1549][^ref-1550]
- **oq-287** (상태: 열림) 부분 근거: 국내 간호사 Delphi 연구는 단일 기관의 미래 시나리오 합의이며 도입 뒤 측정이 아니다(5절). [추정][^ref-1558]
- **oq-284** (상태: 열림) 부분 근거: 지침 (EU) 2019/882 제2조의 조문 범위만 확인했고(7절), 국내 장애인차별금지법상 무인정보단말기 해당성은 미확인이다. [추정][^ref-1554]
- **oq-188** (상태: 열림) 부분 근거: 미국 연구 두 건이 통행 간격과 물품 인수 근접 요구를 보고했으나(5절), 국내 점자블록·연석 대기 위치 기준은 미확인이다. [추정][^ref-1214][^ref-1559]
- **oq-266** (상태: 열림) 부분 근거: IBM 독일 노사 AI 윤리위원회 사례(6절)는 노사 공동 검토기구의 예이지만 운영 책임 소유권을 비교한 연구가 아니다. [추정][^ref-1552]
- **oq-146**·**oq-278** (상태: 열림) 이번에도 근거를 찾지 못했다. EN 301 549 제5.1.7절은 음성을 요구하지 않는 대체 입력을 요구할 뿐 한국어 음성 인식률 자료가 아니다. [사실][^ref-1555]

### 2026-10-12 새 질문

- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-03) 출처 충돌: FSQ-IC 포르투갈어판 검증 연구의 총 표본 346명과 두 분석 표본(EFA 140명 + CFA 210명 = 350명)이 맞지 않는 이유는 무엇이며, 어느 수가 실제 분석에 쓰였는가?[^ref-1548]
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-03) Burtch·Greenwood·Ravindran(ILR Review 2025) 원논문의 표본 시설·기간·추정식·강건성 검정은 무엇이며, 로봇 센터의 중대 부상 40% 감소·비중대 부상 77% 증가는 원논문에서 어떤 조건의 추정치인가?[^ref-1213]
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-03) 알메러 모델·FSQ-IC 같은 수용성 척도를 한국어로 옮겨 국내 산업 현장 작업자(물류창고·제조·병원 직군)에게 타당화한 연구가 있는가?
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-03) EN 301 549 V4.1.1(2026-09)은 지침 (EU) 2019/882의 조화 표준으로 EU 관보에 인용됐는가, 인용됐다면 언제부터 어떤 범위에서 적합성 추정을 주는가?[^ref-1555]
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-03) 출처 충돌: 한림대성심병원 의료서비스로봇 만족도 조사의 원 분모(간호사 109명 대 99명)·문항·조사 시점을 밝힌 병원 원보고서가 공개돼 있는가?[^ref-1222]
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-03) 한국노동연구원 『기술 혁신과 노동시장 변화』(2024-12)의 로봇 노출도별 임금·고용 수치의 원표와 식별 조건은 무엇인가?
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-03) Han 외(CHI 2024) 공동설계 연구 참여자의 거주 국가와 지역은 본문 어디에 명시돼 있는가?[^ref-1214]
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-03) 접근성 요구가 서로 다른 이기종 로봇(배송·안내·병원 물류)의 작업 배정과 물품 인수 완료를 실제 이용자와 현장에서 검증하는 공개 시험 세트나 시나리오가 있는가?
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-03) 이용자의 장애 관련 접근 요구(인수 높이·근접 허용·입력 수단)를 플릿에 전달할 때 필요한 최소 정보 항목과 동의·보존·삭제 절차를 정한 운영 규약이나 검증 사례가 있는가?[^ref-1559]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1213]: George Mason University Costello College of Business, Warehouse automation hasn't made workers safer — it's just reshuffled risk, 2025-08-26, https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk, 접근일 2026-09-30
[^ref-1214]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-09-30
[^ref-1222]: 의협신문, "로봇이 병원을 돌아다닌다"…의료서비스로봇 5만건 돌파, 2025-01-21, https://www.doctorsnews.co.kr/news/articleView.html?idxno=158208, 접근일 2026-09-30
[^ref-1548]: Pinto, A., Lemos, L., Carvalho, C., Santos, J., Menezes, P., Nomura, T. — Human Behavior and Emerging Technologies, Translation, Adaptation, and Validation in Portuguese of an Acceptance Scale for Human–Robot Interaction in an Industrial Context, 2025-01-17, https://doi.org/10.1155/hbe2/8816379, 접근일 2026-10-12
[^ref-1549]: Amazon (Sarah Rhoads, VP Global Workplace Health & Safety), Amazon invests $2.5 billion in workplace safety, reduces workplace injury rates, 2026-03-12, https://www.aboutamazon.com/news/workplace/amazon-workplace-safety-2025-injury-reduction, 접근일 2026-10-12
[^ref-1550]: Strategic Organizing Center (SOC; SEIU·CWA·UFW 연계 노동 조직), Failure to Deliver: Amazon Falls Short on Safety, 2025-05, https://thesoc.org/wp-content/uploads/2025/05/May-2025_Strategic-Organizing-Center_Report-x-Failure-To-Deliver.pdf, 접근일 2026-10-12
[^ref-1551]: 법제처 국가법령정보센터 (대한민국, 법률 제18927호), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) 시행 2022-12-11 법률 제18927호(2022-06-10 일부개정), 2022-06-10, https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017145541, 접근일 2026-10-12
[^ref-1552]: Doellgast, V., Appalla, S., Ginzburg, D., Kim, J., Thian, W. L. (Cornell University ILR School) — ILO Working Paper 144, Global case studies of social dialogue on AI and algorithmic management, 2025-07-10, https://doi.org/10.54394/VOQE4924, 접근일 2026-10-12
[^ref-1554]: European Parliament and Council of the European Union (Official Journal L 151), Directive (EU) 2019/882 of 17 April 2019 on the accessibility requirements for products and services, 2019-06-07, https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng, 접근일 2026-10-12
[^ref-1555]: ETSI / CEN / CENELEC, EN 301 549 V4.1.1 (2026-09) Accessibility requirements for ICT products and services, 2026-09, https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf, 접근일 2026-10-12
[^ref-1558]: Choo, H.-J., Lee, S.-M. (Healthcare Informatics Research 32(1):59–68), Nurses' Perceptions and Utilization Plans for Applying Companion Robots to Acute Stroke Patient Care: A Delphi Study, 2026-01, https://doi.org/10.4258/hir.2026.32.1.59, 접근일 2026-10-12
[^ref-1559]: Boadi-Agyemang, A. (Carnegie Mellon University Robotics Institute, CMU-RI-TR-26-106), From Margin to Center: Designing Inclusive and Equitable Service Robots with Disabled Adults (PhD thesis), 2026-06, https://publications.ri.cmu.edu/storage/publications/2026/09/aboadiag-dissertation2026-manual-tagged-v2_20260902085808.pdf, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-03 | 60. 노동·수용성·접근성 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-12-03/pages/topics/2026/2026-10-12-area60-s6.md

```markdown
---
title: "60. 노동·수용성·접근성 — 대표 접근법과 기술"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1218, ref-1221, ref-1547, ref-1548, ref-1551, ref-1552, ref-1558]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#6
---

[홈](../../index.md) › [주제](../index.md) › 60. 노동·수용성·접근성 — 대표 접근법과 기술

# 60. 노동·수용성·접근성 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 알메러 모델은 요양시설과 가정에서 세 가지 소셜 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다(2010). [사실][^ref-1218] 국내에서는 Q방법론으로 노인 이용자·가족·돌봄 종사자의 돌봄로봇 인식을 네 유형으로 나눴고, '불가피한 대체재' 유형의 설명력이 가장 컸다(2023). [사실][^ref-1221] 두 연구는 요양시설·가정의 고령자와 돌봄 맥락에서 수행되었다. [사실][^ref-1218][^ref-1221]
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

알메러 모델은 요양시설과 가정에서 세 가지 소셜 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다(2010). [사실][^ref-1218] 국내에서는 Q방법론으로 노인 이용자·가족·돌봄 종사자의 돌봄로봇 인식을 네 유형으로 나눴고, '불가피한 대체재' 유형의 설명력이 가장 컸다(2023). [사실][^ref-1221] 두 연구는 요양시설·가정의 고령자와 돌봄 맥락에서 수행되었다. [사실][^ref-1218][^ref-1221]


2026-09-30 실행에서 분리된 이 절의 이전 내용은 [60. 노동·수용성·접근성 — 대표 접근법과 기술 (2026-09-30)](2026-09-30-area60-s6.md)에 있다.

### 산업 맥락 수용성 척도의 포르투갈어판(FSQ-IC)과 표본 조건

Pinto 외(저자 6인, Human Behavior and Emerging Technologies, 2025-01-17)의 FSQ-IC 포르투갈어판 검증 연구는 연구진 네트워크 연락처로 배포한 온라인(LimeSurvey) 횡단 조사이며, 비확률 편의·눈덩이 표본 346명을 썼다. [사실][^ref-1548] 같은 논문의 표는 탐색적 요인분석(Exploratory Factor Analysis, EFA) 표본을 140명, 확인적 요인분석(Confirmatory Factor Analysis, CFA) 표본을 210명으로 적고, 이 가운데 로봇을 다뤄 본 적 없는 응답자가 각각 102명, 147명이다. [사실][^ref-1548] 원문은 40%/60% 분할이라고 적지만 140명 + 210명 = 350명으로 총 표본 346명과 맞지 않아, 원문 안에서 표본 수가 서로 다르며 어느 쪽이 맞는지는 확인하지 못했다. [사실][^ref-1548]

검증 표본이 포르투갈어를 읽는 일반 성인 중심이고 로봇 무경험자가 분석 표본의 약 70~73%이므로, 제목의 산업 맥락만으로 산업 현장 작업자에게서 검증된 척도로 볼 수 없고 한국 현장 작업자에게 그대로 옮길 근거도 없다. [추정][^ref-1548] 이 위키 구축자의 의견으로는, ROP 도입 전후 작업자 조사는 수용 의향, 실제 사용, 거부·우회, 도움 요청, 감시 우려를 별도 지표로 나누고, 응답 집단(관리자·비관리 작업자, 로봇 경험 유무)과 표본 조건(국가·언어·모집 방법·조사 시점·공개 동의 분모)을 결과와 함께 기록해야 한다. 해외 척도는 한국어 인지면담과 직군별 타당화를 거친 뒤 문항원으로만 쓴다. [의견][^ref-1547][^ref-1548][^ref-1558]

### 노동자 참여 절차: 근거 판 갱신과 노사 공동 검토기구 사례

노동자 참여 절차의 국내 근거인 근로자참여법 제20조는 2026-10-12 열람한 2022-12-11 시행판(법률 제18927호)에서 고용조정의 일반원칙(제6호)과 작업과 휴게 시간의 운용(제7호)도 협의 사항으로 둔다(4절). [사실][^ref-1551] 다만 조문은 협의 사항을 열거할 뿐이므로, ROP의 작업 배정·휴게 반영 정책이나 개별 작업자 처리량·위치 로그가 제6·7·14호 협의 대상에 해당하는지는 조문만으로 정해지지 않으며 판례·행정해석은 찾지 못했다. [추정][^ref-1551]

노사 공동 검토기구의 사례로, Cornell University ILR School 소속 저자 5인의 국제노동기구(ILO) Working Paper 144(2025-07-10)는 IBM 독일의 AI 기본협약이 AI 전문가와 사용자·근로자 대표로 구성된 AI 윤리위원회를 두고, 이 위원회가 AI 적용을 평가하고 협약 이행을 감독하며 AI 도구에 대한 직원 이의·불만을 논의하고 AI 권고를 검토·수정한다고 보고한다. [사실][^ref-1552] 이 문서는 ILO 공식 입장이 아니라 저자 견해를 담은 작업논문이며 면담과 문헌에 기초한 질적 사례 연구다. 협약 원문을 싣지 않았고, IBM 면담 날짜가 본문 각주(2021-11-08)와 부록(2024-07-26)에서 다르며, 사업장협의회 위원들이 협약이 안전보건과 AI 수용을 개선했다고 느꼈다는 서술도 측정된 효과가 아니다. [추정][^ref-1552]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1218]: Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics), Assessing acceptance of assistive social agent technology by older adults: the Almere model, 2010, https://doi.org/10.1007/s12369-010-0068-5, 접근일 2026-09-30
[^ref-1221]: 김소라 (주관성 연구, 한국주관성연구학회), 돌봄로봇에 대한 돌봄서비스 종사자와 사용자의 인식 유형 연구, 2023, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002970146, 접근일 2026-09-30
[^ref-1547]: Liu, Y. (A.), Kaur, G., Banerjee, N. K., Banerjee, S. (Clarkson University·Wright State University) — Data in Brief 61, Dataset of worker perceptions of workforce robotics regarding safety, independence, job security, and privacy, 2025-06-03, https://doi.org/10.1016/j.dib.2025.111750, 접근일 2026-10-12
[^ref-1548]: Pinto, A., Lemos, L., Carvalho, C., Santos, J., Menezes, P., Nomura, T. — Human Behavior and Emerging Technologies, Translation, Adaptation, and Validation in Portuguese of an Acceptance Scale for Human–Robot Interaction in an Industrial Context, 2025-01-17, https://doi.org/10.1155/hbe2/8816379, 접근일 2026-10-12
[^ref-1551]: 법제처 국가법령정보센터 (대한민국, 법률 제18927호), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) 시행 2022-12-11 법률 제18927호(2022-06-10 일부개정), 2022-06-10, https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017145541, 접근일 2026-10-12
[^ref-1552]: Doellgast, V., Appalla, S., Ginzburg, D., Kim, J., Thian, W. L. (Cornell University ILR School) — ILO Working Paper 144, Global case studies of social dialogue on AI and algorithmic management, 2025-07-10, https://doi.org/10.54394/VOQE4924, 접근일 2026-10-12
[^ref-1558]: Choo, H.-J., Lee, S.-M. (Healthcare Informatics Research 32(1):59–68), Nurses' Perceptions and Utilization Plans for Applying Companion Robots to Acute Stroke Patient Care: A Delphi Study, 2026-01, https://doi.org/10.4258/hir.2026.32.1.59, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-03 | 60. 노동·수용성·접근성 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-12-03/pages/topics/2026/2026-10-12-area60-s8.md

```markdown
---
title: "60. 노동·수용성·접근성 — 대표 연구와 자료"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1223, ref-1225, ref-1547, ref-1548, ref-1558, ref-1559, ref-1560, ref-1561]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#8
---

[홈](../../index.md) › [주제](../index.md) › 60. 노동·수용성·접근성 — 대표 연구와 자료

# 60. 노동·수용성·접근성 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- EU-OSHA(유럽 산업안전보건청), Advanced robotics and automation: implications for occupational safety and health(2022-06-16) — 사람과 협업할 수 있는 로봇 시스템의 확산이 노동자의 안전·건강·웰빙과 고용 조건에 주는 영향을 다룬 보고서다. [사실][^ref-1225]
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

EU-OSHA(유럽 산업안전보건청), Advanced robotics and automation: implications for occupational safety and health(2022-06-16) — 사람과 협업할 수 있는 로봇 시스템의 확산이 노동자의 안전·건강·웰빙과 고용 조건에 주는 영향을 다룬 보고서다. [사실][^ref-1225]


2026-09-30 실행에서 분리된 이 절의 이전 내용은 [60. 노동·수용성·접근성 — 대표 연구와 자료 (2026-09-30)](2026-09-30-area60-s8.md)에 있다.

### 2026-10-12 갱신: 고용 효과 연구의 게재판과 국가 비교

- Acemoglu, D., Restrepo, P., Robots and Jobs: Evidence from US Labor Markets — [60. 노동·수용성·접근성 — 대표 연구와 자료 (2026-09-30)](2026-09-30-area60-s8.md)에 적은 범위값(노동자 1천 명당 로봇 1대 증가 시 고용인구비율 약 0.18~0.34%p, 임금 0.25~0.5% 감소)은 NBER 작업논문 w23285(2017-03) 초록과 일치하므로 그대로 둔다. [사실][^ref-1223] Journal of Political Economy 128(6) 게재판(2020-06)은 1990~2007년 미국 722개 통근권역 자료에서, 로봇 스톡 증가(1993~2007년 노동자 1천 명당 약 1대)가 로봇 노출이 없는 통근권역 대비 평균 고용인구비율을 0.39%p, 평균 임금을 0.77% 낮췄다고 추정했다(지역 효과). [사실][^ref-1560] 같은 게재판은 공간 파급을 반영한 미국 총량 효과로, 노동자 1천 명당 로봇 1대 증가가 고용인구비율을 약 0.2%p, 임금을 약 0.42% 낮춘다고 추정했다. [사실][^ref-1560]
- Dauth, W., Findeisen, S., Suedekum, J., Woessner, N., The Adjustment of Labor Markets to Robots(Journal of the European Economic Association 19(6), 2021) — 저자 2021-01-21판 기준으로, 1994~2014년 독일 행정자료에 같은 계열의 추정 전략을 적용했을 때 로봇 노출이 총고용을 줄이는 음(-)의 효과를 찾지 못했고, 제조업 일자리 감소를 서비스업(특히 기업 대상 지역 서비스)의 새 노동 수요가 상쇄했다고 보고했다. [사실][^ref-1561]
- 미국(1990~2007년, 통근권역)과 독일(1994~2014년, 402개 지역·행정자료) 결과는 국가·시기·자료·노동 이동 조건이 달라 같은 주장의 재현이나 반박으로 볼 수 없고, 어느 쪽도 한국이나 개별 로봇 플릿 현장의 고용 효과를 측정한 것이 아니다. [추정][^ref-1560][^ref-1561] 이 위키 구축자의 의견으로는, 국가 단위 로봇 노출 계수로 개별 플릿의 감원 인원을 계산하지 말고, 현장 도입 평가에서는 기존 작업자의 직무 전환, 신규 채용, 외주 전환을 구분해 수용성 조사와 함께 기록하는 것이 맞다. [의견][^ref-1560][^ref-1561]
- 이번 갱신에서 더한 수용성 연구 네 건(Liu 외 공개 작업자 설문 데이터, FSQ-IC 포르투갈어판, Choo·Lee Delphi, Boadi-Agyemang 공동설계)의 표본 조건은 4·5·6절에 적었다. 네 건은 해외 표본이거나 단일 기관 표본이며, 어느 것도 한국 산업 현장 작업자를 측정한 연구가 아니다. [추정][^ref-1547][^ref-1548][^ref-1558][^ref-1559]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1223]: Acemoglu, D., Restrepo, P. (NBER), Robots and Jobs: Evidence from US Labor Markets, 2017-03, https://www.nber.org/papers/w23285, 접근일 2026-09-30
[^ref-1225]: European Agency for Safety and Health at Work (EU-OSHA), Advanced robotics and automation: implications for occupational safety and health, 2022-06-16, https://osha.europa.eu/en/publications/advanced-robotics-and-automation-implications-occupational-safety-and-health, 접근일 2026-09-30
[^ref-1547]: Liu, Y. (A.), Kaur, G., Banerjee, N. K., Banerjee, S. (Clarkson University·Wright State University) — Data in Brief 61, Dataset of worker perceptions of workforce robotics regarding safety, independence, job security, and privacy, 2025-06-03, https://doi.org/10.1016/j.dib.2025.111750, 접근일 2026-10-12
[^ref-1548]: Pinto, A., Lemos, L., Carvalho, C., Santos, J., Menezes, P., Nomura, T. — Human Behavior and Emerging Technologies, Translation, Adaptation, and Validation in Portuguese of an Acceptance Scale for Human–Robot Interaction in an Industrial Context, 2025-01-17, https://doi.org/10.1155/hbe2/8816379, 접근일 2026-10-12
[^ref-1558]: Choo, H.-J., Lee, S.-M. (Healthcare Informatics Research 32(1):59–68), Nurses' Perceptions and Utilization Plans for Applying Companion Robots to Acute Stroke Patient Care: A Delphi Study, 2026-01, https://doi.org/10.4258/hir.2026.32.1.59, 접근일 2026-10-12
[^ref-1559]: Boadi-Agyemang, A. (Carnegie Mellon University Robotics Institute, CMU-RI-TR-26-106), From Margin to Center: Designing Inclusive and Equitable Service Robots with Disabled Adults (PhD thesis), 2026-06, https://publications.ri.cmu.edu/storage/publications/2026/09/aboadiag-dissertation2026-manual-tagged-v2_20260902085808.pdf, 접근일 2026-10-12
[^ref-1560]: Acemoglu, D., Restrepo, P. (Journal of Political Economy 128(6):2188–2244), Robots and Jobs: Evidence from US Labor Markets (JPE 게재판), 2020-06, https://doi.org/10.1086/705716, 접근일 2026-10-12
[^ref-1561]: Dauth, W., Findeisen, S., Suedekum, J., Woessner, N. (Journal of the European Economic Association 19(6):3104–3153), The Adjustment of Labor Markets to Robots, 2021-12, https://doi.org/10.1093/jeea/jvab012, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-03 | 60. 노동·수용성·접근성 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-12-03/pages/topics/2026/2026-10-12-area60-s4.md

```markdown
---
title: "60. 노동·수용성·접근성 — 핵심 개념과 용어"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1218, ref-1547, ref-1551]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#4
---

[홈](../../index.md) › [주제](../index.md) › 60. 노동·수용성·접근성 — 핵심 개념과 용어

# 60. 노동·수용성·접근성 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **알메러 모델(Almere Model)** — 통합 기술 수용 이론(Unified Theory of Acceptance and Use of Technology, UTAUT)에 사회적 상호작용 변수를 더해 고령자의 보조 소셜 에이전트 수용성을 설명하는 모델이다(Heerink 외, 2010). [사실][^ref-1218]
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

**알메러 모델(Almere Model)** — 통합 기술 수용 이론(Unified Theory of Acceptance and Use of Technology, UTAUT)에 사회적 상호작용 변수를 더해 고령자의 보조 소셜 에이전트 수용성을 설명하는 모델이다(Heerink 외, 2010). [사실][^ref-1218]


2026-09-30 실행에서 분리된 이 절의 이전 내용은 [60. 노동·수용성·접근성 — 핵심 개념과 용어 (2026-09-30)](2026-09-30-area60-s4.md)에 있다.

**근로자참여 및 협력증진에 관한 법률 제20조 협의 사항(2026-10-12 열람판)** — 2026-10-12 국가법령정보센터에서 연 판(2022-12-11 시행, 법률 제18927호)의 제1항에도 제2호 근로자의 채용·배치 및 교육훈련, 제9호 신기계·기술의 도입 또는 작업 공정의 개선, 제14호 사업장 내 근로자 감시 설비의 설치가 기존에 인용한 법률 제16320호 판과 같은 문구로 있고, 제1항의 마지막 개정 표시는 2019-04-16이다. [사실][^ref-1551] 같은 판 제1항은 제6호에 경영상 또는 기술상의 사정으로 인한 인력의 배치전환·재훈련·해고 등 고용조정의 일반원칙을, 제7호에 작업과 휴게 시간의 운용을 노사협의회 협의 사항으로 둔다. [사실][^ref-1551] 이 내용은 열람일 기준이며, 열람일 이후 개정 여부는 확인하지 않았다.

**공개 작업자 설문 데이터(Liu 외, 2025)** — Data in Brief 61(2025-06-03 온라인)에 공개된 작업자 설문 데이터셋은 미국·캐나다·영국·호주의 블루칼라 노동자 설문 참여자 530명 가운데 데이터 공개에 동의한 337명의 40문항 응답만 담는다. [사실][^ref-1547] 설문 모집 기간은 2022-04-05~2022-07-04로, 데이터셋 논문 발행과 3년 가까이 떨어져 있다. [사실][^ref-1547] 표본은 6개 업종(제조·소매·운송·배송·우편, 창고, 건설, 계약직) 회사 연락처로 이메일 모집한 군집 표본(무작위 아님)이고, 영어로만 설문했으며, 남성 응답이 여성의 약 2배, 18~40세가 약 3분의 2, 창고 종사자가 123명(36.5%)이다. [사실][^ref-1547] 한국어 문항 타당화나 한국 작업자 응답이 없으므로 이 데이터를 한국 산업 현장 작업자 수용성의 대리값으로 일반화할 근거가 없고, 40문항도 안전·동료·로봇 협업·데이터 프라이버시를 나눠 묻는 문항 묶음이지 단일 수용성 점수로 타당화된 척도가 아니다. [추정][^ref-1547]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1218]: Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics), Assessing acceptance of assistive social agent technology by older adults: the Almere model, 2010, https://doi.org/10.1007/s12369-010-0068-5, 접근일 2026-09-30
[^ref-1547]: Liu, Y. (A.), Kaur, G., Banerjee, N. K., Banerjee, S. (Clarkson University·Wright State University) — Data in Brief 61, Dataset of worker perceptions of workforce robotics regarding safety, independence, job security, and privacy, 2025-06-03, https://doi.org/10.1016/j.dib.2025.111750, 접근일 2026-10-12
[^ref-1551]: 법제처 국가법령정보센터 (대한민국, 법률 제18927호), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) 시행 2022-12-11 법률 제18927호(2022-06-10 일부개정), 2022-06-10, https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017145541, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-03 | 60. 노동·수용성·접근성 의 "핵심 개념과 용어" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 15건 / 전체 1496건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-1151 | Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008) | Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction | 2008-03 | https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf | 2026-09-30 | 예 |
| ref-1213 | George Mason University Costello College of Business | Warehouse automation hasn't made workers safer — it's just reshuffled risk | 2025-08-26 | https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk | 2026-09-30 | 예 |
| ref-1214 | Han, H. Z. 외 (Carnegie Mellon University) — CHI '24 | Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations | 2024-04-07 | https://arxiv.org/abs/2404.05050 | 2026-09-30 | 예 |
| ref-1215 | 한국경제 | 로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인) | 2025-04-01 | https://www.hankyung.com/article/2025040138391 | 2026-09-30 | 예 |
| ref-1216 | 한국노동연구원 (국회 정책정보 포털 NABIS 게재) | 기술 혁신과 노동시장 변화 | 2024-12 | https://www.nabis.go.kr/issuReportDetailView.do?menucd=130&gbnCode=P52&refCode=10&poIdx=16861 | 2026-09-30 | 예 |
| ref-1217 | 대한민국 정책브리핑 (보건복지부) | 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행 | 2026-01-28 | https://www.korea.kr/news/policyNewsView.do?newsId=148958690 | 2026-09-30 | 예 |
| ref-1218 | Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics) | Assessing acceptance of assistive social agent technology by older adults: the Almere model | 2010 | https://doi.org/10.1007/s12369-010-0068-5 | 2026-09-30 | 예 |
| ref-1219 | Bundesministerium der Justiz (gesetze-im-internet.de) | Betriebsverfassungsgesetz § 87 Mitbestimmungsrechte | 미확인 | https://www.gesetze-im-internet.de/betrvg/__87.html | 2026-09-30 | 예 |
| ref-1220 | 대한민국 국회 (법률 제16320호, 케이스노트 게재) | 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) | 2019-04-16 | https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0 | 2026-09-30 | 예 |
| ref-1221 | 김소라 (주관성 연구, 한국주관성연구학회) | 돌봄로봇에 대한 돌봄서비스 종사자와 사용자의 인식 유형 연구 | 2023 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002970146 | 2026-09-30 | 예 |
| ref-1222 | 의협신문 | "로봇이 병원을 돌아다닌다"…의료서비스로봇 5만건 돌파 | 2025-01-21 | https://www.doctorsnews.co.kr/news/articleView.html?idxno=158208 | 2026-09-30 | 예 |
| ref-1223 | Acemoglu, D., Restrepo, P. (NBER) | Robots and Jobs: Evidence from US Labor Markets | 2017-03 | https://www.nber.org/papers/w23285 | 2026-09-30 | 예 |
| ref-1224 | ISO/IEC | ISO/IEC Guide 71:2014 Guide for addressing accessibility in standards | 2014-12 | https://www.iso.org/standard/57385.html | 2026-09-30 | 아니오 |
| ref-1225 | European Agency for Safety and Health at Work (EU-OSHA) | Advanced robotics and automation: implications for occupational safety and health | 2022-06-16 | https://osha.europa.eu/en/publications/advanced-robotics-and-automation-implications-occupational-safety-and-health | 2026-09-30 | 예 |
| ref-1226 | Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics) | Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety | 2026 | https://doi.org/10.1007/s12369-026-01359-1 | 2026-09-30 | 예 |
```

### docs/glossary/index.md (요약: 용어 399개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- makespan: 메이크스팬 (Makespan)
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
- minimum-cost-flow: 최소 비용 흐름 (Minimum-Cost Flow)
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
- satisfiability-modulo-theories: 이론 모듈로 만족 가능성 (Satisfiability Modulo Theories (SMT))
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

### docs/open-questions.md (요약: 대상 영역 [60] 에 걸린 10건 / 전체 396건)

```markdown
- oq-146 [열림] 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가(이번 조사에서 확인된 현장 사례는 네덜란드 슈퍼마켓 연구뿐이다)? (영역 13, 60, 61)
- oq-188 [열림] 국내 보도에서 배송·순찰 로봇이 횡단 대기 중 연석 경사로·점자블록을 막지 않도록 하는 대기 위치 규칙이나 접근성 기준(인증 항목·지침)이 있는가? (영역 66, 60, 16)
- oq-266 [열림] 로봇 운영 책임을 전담 운영 조직(커맨드센터), 사용 부서, 시설·IT 부서 가운데 어디에 두는 것이 역할 모호성과 사용 저항을 줄이는지 비교한 연구가 있는가? (영역 40, 56, 60)
- oq-278 [열림] 로봇 관제 요원·운영 인력의 직무 역량과 교육 과정을 정한 국가직무능력표준(NCS)이나 공개 교육 표준이 있는가? (영역 56, 40, 60)
- oq-284 [열림] 서비스 로봇 본체에 달린 터치스크린·주문 화면이나 운영자·이용자용 채팅 화면이 장애인차별금지법상 무인정보단말기에 해당해 접근성 의무를 지는가? (영역 60, 59, 64)
- oq-285 [열림] 오케스트레이션 플랫폼이 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록하는 기능이 근로자참여법 제20조의 근로자 감시 설비나 독일 사업장조직법 제87조의 감시 장치에 해당해 도입 전 노사협의·공동결정 대상이 되는가? (영역 60, 53, 59)
- oq-286 [열림] 로봇 도입 뒤 늘어난 작업 속도(피킹 목표량)와 비중대 부상 증가를 오케스트레이션의 작업 배정·속도 정책(휴식·작업 순환 반영)으로 줄인 사례나 연구가 있는가? (영역 60, 31, 25)
- oq-287 [열림] 국내 병원·물류창고에서 로봇 도입 뒤 종사자 수용성과 직무 변화를 기관 자체 설문이 아닌 독립 연구로 조사한 자료가 있는가? (영역 60, 63, 61)
- oq-321 [열림] 작업자 스캐너 기록의 개인별 비활동·속도 지표를 과도한 감시로 본 CNIL 판단이 로봇 작업 기록에서 만든 작업자 지표에 적용된 감독기관 결정이나 국내 해석이 있는가? (관련: oq-285) (영역 53, 60, 39)
- oq-388 [열림] 아동·휠체어 사용자·보행 보조기 사용자·시각장애인이 가려진 모퉁이나 통로 점유 상황에서 로봇을 만날 때의 감지 누락·양보 결과를 독립적으로 측정한 데이터셋이나 시험 결과가 있는가? (영역 49, 60)
```

### runs/2026-10-12-03/verification2.json

```json
{
  "run_id": "2026-10-12-03",
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
      "이전 분리 주제 페이지 2026-09-30-area60-s4·s6·s7 에는 아직 '법률 제16320호 기준', '현행 조문 여부 미확인' 문구가 남아 있다. 이번에 새로 쓴 2022-12-11 시행판(ref-1551) 서술과 판이 다르다. 이번 실행 입력에 해당 본문이 없어 additional_research_requests 1항으로 미뤘으며, 다음 갱신 실행에서 정리할 대상이다.",
      "근로자참여법 제20조 ref-1220 표기를 쓰는 field-operations-and-monitoring/index.md 와 2026-09-30-area60-s10.md 도 후속 정리 대상이다(이번 범위 밖).",
      "9절은 f48·f49·f50 의견을 표 칸 안 짧은 문장과 표 아래 단락에서 두 번 싣는다. 드리프트는 아니며 표기 의견으로만 남긴다."
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
    "4·6·7·8·11절(머리말 패치 아님, 해당 절 append 내용): 자동 분리 뒤 세부영역 페이지와 새 주제 페이지(2026-10-12-area60-s4·s6·s7·s8·s11)가 이전 실행에서 분리된 주제 페이지(docs/topics/2026/2026-09-30-area60-s4.md·s6.md·s7.md·s8.md·s11.md)로 가는 링크를 잃었다. 새 주제 페이지 3절이 이전 페이지의 '자세한 내용은 주제 페이지 …' 줄 없이 옮겨졌고, 세부영역 페이지의 각 절은 새 페이지만 가리킨다. 각 절의 append 내용 첫머리에 '2026-09-30 실행에서 분리된 이 절의 이전 내용은 [60. 노동·수용성·접근성 — <절 이름> (2026-09-30)](../../topics/2026/2026-09-30-area60-sN.md)에 있다.' 형식의 링크 문장을 둔다. 분리 코드가 '자세한 내용은 주제 페이지'로 시작하는 줄을 지우므로 그 문구로 시작하지 않게 쓴다. 이유: 게시·검증된 이전 내용(노사협의회 협의 사항, Acemoglu 범위값, 열린 질문 8건 등)이 세부영역 페이지에서 닿지 않게 된다. 원 절 내용을 그대로 옮기지 못한 것이다(부록 R-3). 이 줄이 계속 지워지면 pipeline 의 분리 처리 담당에게 기존 '자세한 내용은' 링크를 새 주제 페이지 본문에 보존하도록 요청한다.",
    "8절(새 주제 페이지 2026-10-12-area60-s8 로 옮겨질 append 내용): 'Acemoglu … — 주제 페이지에 적은 범위값'의 '주제 페이지'를 [60. 노동·수용성·접근성 — 대표 연구와 자료 (2026-09-30)](../../topics/2026/2026-09-30-area60-s8.md) 링크로 밝힌다. 이유: 지금은 어느 페이지의 값을 유지한다는 것인지 독자가 찾을 수 없다.",
    "11절과 open_question_updates 여섯 번째(한국노동연구원 『기술 혁신과 노동시장 변화』) 질문의 문구를 맞춘다. 페이지는 수치를 뺐지만 open_question_updates 에는 '고숙련 +2.5%·+0.55%p, 저숙련 -4.5~4.9%'가 출처 없이 남아 있다. 둘 중 하나로 맞춘다. (a) 두 곳 모두 수치를 빼거나, (b) 두 곳 모두 수치를 남기고 페이지 질문에 기존 각주 [^ref-1215] 를 달아 '보도 기준'을 밝힌다. 이유: 열린 질문 목록에 출처 없는 수치가 실리지 않게 하고 페이지 11절과 open_question_updates 를 일치시키기 위해서다.",
    "5절 실외 사례 끝 문장 '그래서 두 실외 사례의 예외·성과 칸에는 도입 성과를 적지 않았다'를 고친다. 휠체어 통행 사례의 예외·성과 칸에는 기존 사건(연석 경사로 차단과 운행 일시 중단)이 그대로 있다. 이를 '그래서 물품 인수 사례의 예외·성과 칸은 해당 없음으로 두었다'처럼 실제 표와 맞는 문장으로 바꾼다. 이유: 같은 절의 표 내용과 어긋난다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 51건, 미확인 0건, 교차 확인 0건. 강등: 없음. 원문 미열람 출처: ref-1226(이번 실행). 1차 확인 51건 가운데 f1~f3·f6(표본)·f10·f11·f13·f19(IBM 사례)·f20·f26·f27·f29·f38·f39 는 검증자가 원문을 다시 열지 못해 리서치의 원문 열람 발췌를 기준으로 인정했다. 정정 사항: Amazon 발표(ref-1549)의 현재 제목, EN 301 549 V4.1.0 배포본 날짜(04.01.00_30 은 2026-06), ILO WP144 발행일 2025-07-10 을 반영했다. 주의: 수용성 연구(Liu 외·FSQ-IC·Choo·Lee·Han·Boadi-Agyemang)는 모두 해외 표본이거나 단일 기관 표본이며 한국 산업 현장 작업자를 측정한 연구가 아니다. FSQ-IC 원문의 표본 수(346 대 350)는 원문 안에서 서로 맞지 않는다. Amazon 발표와 SOC 보고서는 서로 다른 이해당사자 자료이고 로봇 효과를 분리하지 않는다. 접근성 표준과 EU 지침이 개별 ROP 에 적용되는지는 판단하지 않았고 59. 법·규제·보험·라이선스 의 연계 대상으로 두었다. 근로자참여법 제20조 근거는 세부영역 페이지와 새 주제 페이지에서 2022-12-11 시행판(ref-1551)으로 바꿨다. 다만 이전 분리 주제 페이지(2026-09-30-area60-s4·s6·s7)의 '법률 제16320호·현행 여부 미확인' 문구는 이번 입력 밖이라 다음 갱신으로 넘겼다. 정정 요청 없음. 2차: 드리프트 없음, 태그 처분 유지(태그를 올린 문장 없음), 의견 주체 명시, 벤더 주장 병기 유지, [분류원문] 보존, 섹션 순서 준수(형식 검증 통과). 1차 수정 지시 15건은 모두 이행됐다(9항은 입력 범위 안에서 이행). 지적 4건: (1) 자동 분리 뒤 이전 분리 주제 페이지(2026-09-30-area60-s4·s6·s7·s8·s11)로 가는 링크가 끊겼다. (2) 8절 '주제 페이지에 적은 범위값'이 어느 페이지인지 링크가 없다. (3) 한국노동연구원 열린 질문의 수치가 페이지와 open_question_updates 사이에서 다르다. (4) 5절 실외 사례 끝 문장이 표 내용과 어긋난다.",
  "retry_reason": null
}
```
