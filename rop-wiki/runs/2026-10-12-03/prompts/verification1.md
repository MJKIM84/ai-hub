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
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
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

### docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md (요약)

```markdown
# 58. 다사업자 책임·계약·데이터

소속 대분류: P. 거버넌스·법규·사회 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

책임과 변경 승인, 데이터 소유권, API 변경 정책, 서비스 수준·감사 이력 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **다사업자 책임·변경 승인**: 연동 오류를 누가 고치고 변경을 누가 승인할지 정한다
- **데이터 소유권**: 운영 데이터를 누가 갖고 어디까지 쓸 수 있는지 정한다
- **API 변경 정책**: 제조사와 플랫폼의 API가 바뀔 때 호환성과 공지 방식을 정한다
- **서비스 수준·감사 이력**: 서비스 수준 약속과 감사 이력을 정하고 지킨다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 28번 영역 ‘표준·상호운용성·다사업자 거버넌스’에서 왔다. 그 본문은 [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까? [분류원문]
```

### docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md (요약)

```markdown
# 59. 법·규제·보험·라이선스

소속 대분류: P. 거버넌스·법규·사회 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

법·규제 대응, 보험·사고 책임, 오픈소스·라이선스 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **법·규제 대응**: 기계류 규정·AI 규제·로봇 관련 법·개인정보 법·실외 로봇 운행 규정을 파악하고 대응한다
- **보험·사고 책임**: 사고 책임의 배분과 보험을 정한다
- **오픈소스·라이선스 관리**: 오픈소스·SDK·3D 자산의 라이선스를 지킨다

## 2. 핵심 질문

이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가? [분류원문]
```

### docs/categories/planning-and-business/economics-procurement-and-business-models.md (요약)

```markdown
# 3. 경제성·조달·사업 모델

소속 대분류: A. 기획·사업 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

투자 효과를 따지고, 로봇·플랫폼을 골라 계약하고, 과금 방식을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **경제성·투자 효과 분석**: 도입 비용·운영비·총소유비용과 기대 효과를 비교해 투자 여부를 판단한다
- **로봇·솔루션 선정·조달**: 요구에 맞춰 로봇과 플랫폼을 평가하고 시범 운영과 계약을 진행한다
- **사업 모델·과금**: 서비스형 로봇(RaaS)·구독·작업당 과금 같은 사업 모델과 사용량 계량을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 4번 영역 ‘성과·경제성·프로세스 개선’에서 왔다. 그 본문은 [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

도입 비용을 넘는 효과가 나오며, 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md (요약)

```markdown
# 13. 대화형 기능의 신뢰·기반

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **오해석 방지·근거 표시**: 해석의 근거(장소·물품·문서 식별자)를 보여 주고, 없는 물품이나 검토되지 않은 문·측정값을 모델이 지어내지 못하게 막는다
- **대화 권한·기록 보호**: 사용자별로 대화로 지시할 수 있는 로봇·구역·작업의 범위를 제한하고 대화 기록을 보존·보호한다
- **언어 모델 연결·교체**: 언어 모델 공급자를 고르고 바꾸며 자격 증명을 보호하고, 모델 장애 때 임의로 다른 모델로 넘기지 않는다
- **대화형 기능 평가**: 해석·분해 정확도, 배정 적합성, 질문 횟수, 구성 완료 시간 같은 지표와 시나리오 시험으로 대화 기능을 평가한다
- **대화와 화면 편집 연동**: 지도에서 고른 장소·로봇 같은 화면 선택이 대화에 그대로 반영되고, 대화로 바꾼 내용이 편집 화면에 바로 보이게 한다
- **음성·다국어·현장 단말 대화**: 현장 사람이 음성·모바일·태블릿과 여러 언어로 지시하고 질문한다

## 2. 핵심 질문

언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? [분류원문]
```

### docs/categories/space-and-map-model/place-semantics-and-map-management.md (요약)

```markdown
# 16. 장소 의미·지도 관리

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

장소에 이름·용도를 붙이고, 지도를 편집하고, 바뀔 때 버전을 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **장소 의미·이름**: 구역·방·목적지에 이름·별칭·용도를 붙여 업무와 대화에서 같은 장소를 같은 이름으로 가리키게 한다
- **지도 버전·변경 관리**: 배치 변경과 임시 통제 구역을 지도에 반영하고 지도 버전을 관리한다
- **지도·환경 편집기**: 사람이 직접 공간과 시설을 그리고 고치는 편집 화면을 제공한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

같은 장소를 모두가 같은 이름으로 부르고, 공간이 바뀌면 지도를 어떻게 따라 바꿀 것인가? [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]
```

### docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md (요약)

```markdown
# 19. 사람·보행자 모델

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

## 1. 한 줄 정의

현장 사람의 위치·흐름·혼잡을 모델링해 계획과 안전에 쓴다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람·보행자 모델**: 현장 사람의 위치·목적지·멈춤·교차를 모델링해 로봇 계획과 안전에 반영한다
- **사람 흐름·혼잡 추정**: 시간대·구역별 사람의 흐름과 혼잡을 추정해 경로와 작업 시간에 반영한다

## 2. 핵심 질문

현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]
```

### docs/categories/planning-and-optimization/task-allocation-mrta.md (요약)

```markdown
# 25. 작업 배정 — MRTA

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

## 1. 한 줄 정의

작업을 로봇 또는 로봇 팀에 배정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 배정**: 능력·위치·적재량·배터리·기한을 고려해 로봇 또는 로봇 팀에 작업을 배정한다
- **이종 로봇 팀 구성**: 한 작업에 필요한 로봇 조합(운반·팔·순찰 등)을 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 13번 영역 ‘작업 배정 — MRTA’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 [옛 분류원문]

> 옛 질문: 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/execution-collaboration-and-recovery/human-robot-collaboration.md (요약)

```markdown
# 31. 사람–로봇 협업

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

사람과의 작업 분담, 수동 개입·원격 조작, 주변 사람과의 소통 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람–로봇 작업 분담**: 사람과 로봇이 서로 기다리지 않도록 일을 나누고 작업자의 부담(인체공학)을 고려한다
- **수동 개입·원격 조작**: 운영자가 승인·수동 전환·원격 조작으로 로봇 작업에 개입한다
- **주변 사람과의 소통**: 로봇이 빛·소리·화면으로 의도를 알리고 주변 사람을 안내한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 18번 영역 ‘사람–로봇 협업·운영 인터페이스’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 [옛 분류원문]

> 옛 질문: 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? [옛 분류원문]

## 2. 핵심 질문

사람과 로봇이 같은 공간에서 서로 기다리거나 방해하지 않게 하려면? [분류원문]
```

### docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md (요약)

```markdown
# 37. 관제 화면·실행 기록

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

## 1. 한 줄 정의

지도 위 상태 표시, 설명 가능한 표시, 실행 기록 재생 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **관제 화면**: 지도 위에 로봇·작업·설비·사람·물품 상태를 보여 주고 층을 골라 본다
- **설명 가능한 상태 표시**: 로봇이 지금 무엇을 왜 하고 있는지 운영자가 알아볼 수 있게 표시한다
- **실행 기록·재생**: 실행 기록을 저장하고 시간축으로 재생하며 사건을 찾아본다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 18번 영역 ‘사람–로봇 협업·운영 인터페이스’에서 왔다. 그 본문은 [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? [분류원문]
```

### docs/categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md (요약)

```markdown
# 39. 운영 성과 측정·개선

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-26 · 버전: 3

## 1. 한 줄 정의

지표 정의·측정, 로봇 성과와 업무 성과 구분, 운영 개선 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 성과 측정**: 처리량·완료 시간·가동률·대기 시간·에너지 같은 지표를 정의하고 측정한다
- **로봇 성과와 업무 성과 구분**: 로봇 가동률이 올라간 것이 실제 업무 성과(처리량·서비스 시간·비용)로 이어졌는지 나눠 본다
- **운영 개선**: 측정 결과로 운영 정책·배치·절차를 고치고 효과를 다시 잰다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 4번 영역 ‘성과·경제성·프로세스 개선’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 [옛 분류원문]

> 옛 질문: 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? [옛 분류원문]

## 2. 핵심 질문

로봇 가동률이 오른 것이 실제 업무 성과로 이어졌는가? [분류원문]
```

### docs/categories/safety/human-proximity-safety.md (요약)

```markdown
# 49. 사람 근접 안전

소속 대분류: M. 안전 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-11 · 버전: 3

## 1. 한 줄 정의

사람과의 분리 거리·감속·양보, 구역별 속도·진입 제한 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람 근접 안전**: 사람과의 분리 거리를 지키고 감속·양보·재개를 판단한다
- **구역별 속도·진입 제한**: 구역·시간대별 속도 제한과 진입 금지를 설정해 계획과 실행에 반영한다

## 2. 핵심 질문

사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]
```

### docs/categories/security-and-privacy/privacy-and-video-data.md (요약)

```markdown
# 53. 개인정보·영상 데이터

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

영상·작업자·거주자 데이터 보호, 최소 수집·익명화 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **개인정보·영상 데이터 보호**: 카메라 영상과 작업자·환자·거주자 데이터를 보호한다
- **사람 데이터 최소 수집·익명화**: 보행자 위치·영상에서 신원을 떼어 내고 필요한 만큼만 모은다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md (요약)

```markdown
# 56. 운영 이관·확대·교육

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

운영 이관·지원, 단계적 확대, 교육·변화 관리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 이관·지원 체계**: 구축 팀에서 운영 팀으로 넘기고 지원·장애 대응 체계를 정한다
- **단계적 확대**: 시범 운영에서 넓혀 가며 새 현장과 새 로봇을 추가한다
- **사용자 교육·변화 관리**: 운영자·작업자를 교육하고 일하는 방식의 변화를 관리한다

## 2. 핵심 질문

시범 운영을 넓히면서 운영을 누구에게 어떻게 넘기고 사람을 어떻게 준비시킬 것인가? [분류원문]
```

### docs/categories/site-type-applications/warehouse.md (요약)

```markdown
# 61. 물류창고

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

입고~반품 흐름의 로봇 작업. 기존 흐름 매트릭스와 영역 페이지의 물류 시나리오를 사례로 모은다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **물류창고 작업 흐름 적용**: 입고·적치·보충·피킹·포장·출하·반품 흐름에 로봇 작업을 대입해 시작 조건·작업 대상·수행 자원·제약·완료·예외를 정리한다

## 2. 핵심 질문

물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? [분류원문]
```

### docs/categories/site-type-applications/hospital-and-healthcare.md (요약)

```markdown
# 63. 병원·의료

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

검체·약품·식사·린넨 이송, 감염 관리, 환자 정보 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **병원 적용**: 검체·약품·식사·린넨 이송과 감염 관리 구역, 환자 정보 보호를 다룬다

## 2. 핵심 질문

감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가? [분류원문]
```

### docs/categories/site-type-applications/outdoor.md (요약)

```markdown
# 66. 실외

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실외 적용**: 실외 배송·순찰·캠퍼스 운영과 보도 주행 규정·위성 위치·날씨 조건을 다룬다

## 2. 핵심 질문

보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 15건 / 전체 1486건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/open-questions.md (요약: 대상 영역 [60] 에 걸린 10건 / 전체 393건)

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

### config/priority.yaml

```yaml
# config/priority.yaml — 사용자가 지정하는 우선 영역·주제·질문 (빌드 사양서 7.1, 7.4, 8.2)
#
# 비어 있으면 순환 규칙(config/rotation.yaml)만 따른다. 항목이 없는 키는 빈 목록([])으로 둔다.
# 네 키(areas, topics, questions, track_questions)는 빈 목록이라도 모두 있어야 하고, 항목의 필드 이름은 아래 예시와 같아야 한다.
# 항목의 뜻과 반영 시점은 config/README.md 와 docs/about/how-to-contribute.md 에 있다.
#
# 읽는 주체:
#   - pipeline/select_target.*  : areas·topics·questions 로 그날의 대상을 정한다(순환보다 우선, 7.1). questions 는 area_no 영역을 대상으로 올리고, 2주기에는 그 영역의 점수에도 더한다
#   - 리서치·검증 에이전트       : 이 파일 전문이 프롬프트의 "## 입력"에 들어간다. 대상 영역의 questions 는 조사 질문에 포함된다
#   - pipeline/select_target.*  : 트랙 실행의 대상 선정에서 track_questions 를 트랙 백로그(data/tracks/<slug>/backlog.json)에 제기 근거 "사용자"로 먼저 등록하고 그 실행의 질문으로 고른다
#   - 퍼블리셔                   : 대상 선정 뒤에 더해진 track_questions 를 같은 방식으로 등록한다(보완)
#
# area_no 는 1~67 의 세부영역 번호다(2026-09-28 개정 분류, _source/ROP_연구분야_분류.md). 사람이 읽기 쉽도록 주석에 영역 이름을 함께 적는다(예: 17. 작업 대상·자산 식별과 인계 추적).
# 지정한 항목이 처리되면 목록에서 지워도 된다. 지우지 않으면 rotation.yaml 의 priority.skip_if_targeted_within_days 가 지난 뒤 다시 우선된다.
# 우선 지정은 조사 대상을 정할 뿐 검증 규칙과 하루 예산(daily_budget)을 바꾸지 않는다.

# 세부영역을 먼저 다루게 한다. weight 는 대상 선정 점수에 더하는 가중치, reason 은 로그(target.json·일일 로그)에 남는 지정 사유다.
areas: []
# 작성 예시:
# areas:
#   - area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적
#     weight: 10            # 대상 선정 점수에 더하는 가중치
#     reason: "병원·상업 시설의 인계 확인 사례가 부족하다"

# 특정 주제로 주제 조사(run_type topic)를 실행하게 한다. area_no 는 주 연구영역이다.
topics: []
# 작성 예시:
# topics:
#   - title: "작업 대상 인계 확인에 EPCIS 이벤트를 쓰는 방법"
#     area_no: 17           # 주 연구영역: 17. 작업 대상·자산 식별과 인계 추적
#     weight: 8

# 답을 찾게 할 질문이다. area_no 영역을 areas 와 같이 순환보다 먼저 대상으로 올리고(가중치는 rotation.yaml 의 priority.question_weight), 그 영역이 대상이 되면 리서치 에이전트의 조사 질문에 포함된다.
questions: []
# 작성 예시:
# questions:
#   - question: "로봇 도착과 실제 작업 대상 인계를 어떤 이벤트로 구분해 기록하는가?"
#     area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적

# 트랙 백로그에 넣을 질문이다(8.2). 다음 트랙 실행의 대상 선정이 제기 근거 "사용자"로 백로그에 등록해 우선순위를 올린다(8.2).
# 처리 순서: 리서치 에이전트는 트랙 실행마다 현재 단계의 열린 질문 가운데 사용자 지정 → 앞 단계로 되돌아온 질문 → 오래된 순으로 1~3개를 고르므로(6.1),
# 현재 단계에 넣은 사용자 질문이 가장 앞에 온다. 사용자 질문이 여럿이면 priority(high → normal → low), 같으면 파일에 적힌 순이다 [가정].
# stage 가 현재 단계보다 앞이면 되돌아온 질문과 같이 다음 트랙 실행에서 우선 처리하고(8.2), 뒤이면 그 단계가 현재 단계가 될 때 다룬다 [가정].
track_questions: []
# 작성 예시:
# track_questions:
#   - track: manual-capability-ontology   # config/tracks/<slug>.yaml 의 slug
#     stage: 1              # 질문을 넣을 단계 번호(1 ~ 그 트랙의 단계 수: 매뉴얼 기반 로봇 기능 온톨로지 7, 채팅 기반 구성·운영 10, 건축 도면 자동 인식 5). 예: 단계 1. 기존 능력 표현 모델과 표준 조사
#     question: "산업 상호운용 규격의 팩트시트는 적재 제약을 어떤 필드로 기술하는가?"
#     priority: high        # high / normal / low. 사용자 지정 질문이 여럿일 때 고르는 순서에만 쓴다 [가정]
```

### runs/2026-10-12-01/research.md

```markdown
# 리서치 브리프 2026-10-12-01

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-12-01 |
| 날짜 | 2026-10-12 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 58. 다사업자 책임·계약·데이터 |
| 대분류 | P. 거버넌스·법규·사회 |

## 갭(비어 있거나 약한 섹션)

- 섹션 4. 핵심 개념과 용어(분리 2026-09-30-area58-s4) — '데이터 보유자' 항목(40행)이 '사용자 동의 없이 비개인 데이터를 이용할 수 없다'로 데이터법 제4조(13)의 '사용자와의 계약을 근거로만'과 다르고, 근거가 해설 페이지(ref-1191)뿐
- 섹션 5. 적용 사례 — 병원 사례가 2025 공고 하나(ref-872, 각주에 '원문 미열람')에 기대며 '연 2회 평가·인증'(71행 표 '수행 자원', 76행 본문)을 원어 'bi-annual' 의 한 해석으로 단정, 2026 공고(연례·AutoveX 2026-09-01부터 2년) 미반영. 상업·물류 현장의 실제 공개 계약 문안(지원 응답·시설 장애·책임 상한) 사례 없음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area58-s6) — 데이터 계약 소절(51·53행)에 '쉽게 이용 가능한 데이터' 범위·제3조(1) 설계 의무의 별도 적용일·MCT/SCC 의 제3자 면책 공백 없음. 변경 주체 책임 소절에 EU 제조물책임지침(소프트웨어 포함·실질적 변경자·업무용 재산 제외·증거 공개 비례성) 없음. 서비스 수준 소절(65행)이 ISO/IEC 19086-1(원문 미열람) 일반론뿐이라 응답·복구 시계, 시설 장애 예외, API 가용성 측정식 같은 실제 조항 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area58-s7) — 표에 EU 제조물책임지침과 RFC 9745(폐기 예고·종료 시각) 행이 없고, 데이터법 행(41행)이 일반 적용일만 적음
- 섹션 8. 대표 연구와 자료 — 세 건뿐이며 데이터 접근 거절(영업비밀) 관할별 관행을 다룬 동료심사 연구 없음
- 섹션 11. 열린 질문(분리 2026-09-30-area58-s11) — oq-241·oq-268·oq-279·oq-280·oq-259·oq-185 에 붙일 공개 원문 근거 없음
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: s4.md 40행 데이터 보유자 정의, 본 페이지 71·76행 '연 2회', ref-872·ref-706 의 '원문 미열람' 표시

## 조사 질문

1. 제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까? [분류원문]
2. EU 데이터법에서 데이터 보유자의 비개인 데이터 이용 근거와 사용자에게 제공할 데이터 범위, 설계 의무의 적용 시점은 원문상 무엇인가(oq-279·oq-320)? (섹션 4·6·7 겨냥)
3. 공개된 모델 계약 조항·표준 계약 조항과 EU 개정 제조물책임지침은 제3자 청구·소프트웨어 결함·실질적 변경·증거 공개를 다사업자 사이에서 어떻게 다루는가(oq-241·oq-289)? (섹션 6·7 겨냥)
4. 로봇 서비스·관제 플랫폼의 공개 약관은 지원 응답 시간·시설 장애 예외·책임 상한·과금 단위·가용성 측정을 어떻게 정하는가(oq-112·oq-268)? (섹션 5·6 겨냥)
5. API 폐기 예고와 종료 시각의 관계를 정한 표준은 무엇을 정하고 무엇을 계약에 남기는가(oq-280)? (섹션 7 겨냥)
6. 통합자 사전 자격(RoMi-H 등재)의 주기·유효기간과, 영상 처리 위탁·데이터 접근 거절의 관리 기준은 공개 원문상 무엇인가(oq-149·oq-259)? (섹션 5·6·8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | EU 데이터법(Regulation (EU) 2023/2854) 제4조(13)은 데이터 보유자가 쉽게 이용 가능한 데이터 가운데 비개인 데이터를 사용자와의 계약을 근거로만 이용할 수 있다고 정하고, 그 데이터로 사용자의 경제 상황·자산·생산 방식을 추론해 사용자의 시장 지위를 해치는 이용을 금지한다. | ref-636 | 아니오 | medium | 2026-10-12 | — | — |
| f2 | [사실] | 데이터법 제4조(1)은 사용자가 연결 제품·관련 서비스에서 데이터에 직접 접근할 수 없을 때 데이터 보유자가 '쉽게 이용 가능한 데이터'와 그 해석·이용에 필요한 관련 메타데이터를 지체 없이 무료로 제공하도록 하며, 제2조(17)은 '쉽게 이용 가능한 데이터'를 데이터 보유자가 과도한 노력 없이 연결 제품·관련 서비스에서 적법하게 얻거나 얻을 수 있는 제품 데이터·관련 서비스 데이터로 정의한다. | ref-636 | 아니오 | medium | 2026-10-12 | — | — |
| f3 | [사실] | 데이터법 제50조는 이 규정을 2025-09-12부터 적용한다고 하면서, 제3조(1)의 설계 의무(연결 제품·관련 서비스를 데이터에 직접 접근 가능하게 설계·제조할 의무)는 2026-09-12 후에 시장에 출시되는 연결 제품과 관련 서비스에 적용한다고 따로 정한다. | ref-636 | 아니오 | medium | 2026-10-12 | — | — |
| f4 | [사실] | 집행위원회 권고 초안 부속서(C(2025) 7750 final ANNEX, 2025-11-19)의 클라우드 표준 계약 조항(SCC) 중 책임 조항 설명(Annex X)은 '이 SCC 는 면책(indemnification) 조항을 포함하지 않는다'고 적고, 한 당사자의 중대한 의무 위반으로 생긴 제3자 청구에 대해 면책·보호 조항이 필요한지와 그 범위를 당사자가 검토하도록 권한다. | ref-1489, ref-1192 | 아니오 | medium | 2026-10-12 | — | — |
| f5 | [사실] | EU 개정 제조물책임지침(Directive (EU) 2024/2853) 제4조(1)은 '제품'에 소프트웨어를 포함하고, 제2조(2)는 상업 활동 밖에서 개발·공급된 자유·오픈소스 소프트웨어에는 지침을 적용하지 않는다고 정한다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f6 | [사실] | 같은 지침 제8조(2)는 제조자의 통제 밖에서 제품을 실질적으로 변경한 뒤 시장에 내놓거나 사용에 투입한 자연인·법인을 그 제품의 제조자로 본다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f7 | [사실] | 지침 제2조(1)의 적용 대상은 2026-05-07 정오표(OJ L 2026/90364)로 '2026-12-09 후'에서 '2026-12-08 후(after 8 December 2026)' 시장에 출시되거나 사용에 투입된 제품으로 고쳐졌으며, 따라서 2026-12-09 당일부터 출시·투입되는 제품에 적용된다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f8 | [사실] | 지침 제22조(1)은 회원국이 지침 이행 법령을 2026-12-09까지 시행하도록 정하고, 제21조는 구 제조물책임지침 85/374/EEC 를 2026-12-09 부로 폐지하되 그 전에 출시·사용 투입된 제품에는 계속 적용한다고 정한다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f9 | [사실] | 지침 제6조(1)(b)(iii)은 전적으로 업무 목적으로만 쓰는 재산의 손해를 이 지침의 보상 대상 손해에서 제외한다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f10 | [사실] | 지침 제9조(3)은 같은 조 제1·2항에 따른 증거 공개를 필요하고 비례적인 범위로 제한하도록 회원국에 요구하고, 제9조(4)는 그 판단에서 제3자를 포함한 모든 당사자의 정당한 이익, 특히 기밀·영업비밀 보호를 고려하게 한다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f11 | [사실] | 창이종합병원 CHART 의 2025년 RoMi-H 등재 공고는 프로그램을 'a bi-annual RoMi-H Empanelment Program'으로 적고, 같은 공고에서 등재 통합자 5개사(HOPE Technik, Medisys Innovation, Panasonic Asia Pacific, QuikBot Technologies, Techfox)의 등재가 2025-05-01부터 2년간 유효하다고 게시한다. | ref-872 | 아니오 | medium | 2026-10-12 | — | — |
| f12 | [추정] | 2025년 공고의 'bi-annual'은 '연 2회'로도 '2년마다'로도 읽힐 수 있고 같은 공고가 등재 유효기간을 2년으로 적고 있어, 위키 5절의 '연 2회 평가·인증'(본문 76행, 표 '수행 자원' 행)은 원어 인용과 두 해석을 함께 적거나 [추정]으로 낮춰야 한다. | ref-872, ref-1495 | 아니오 | low | 2026-10-12 | — | — |
| f13 | [사실] | SingHealth/CHART 의 2026년 RoMi-H 등재 공고(2026-05-06 게시, 2026-08-24 갱신)는 CHART 가 연례(annual) 등재 프로그램을 운영해 통합자의 RoMi-H 배치 역량을 평가·재평가한다고 적고, 등재 통합자는 CHART 웹사이트에 공개되어 공공 의료기관이 제안요청(RFP/RFI) 참여를 위해 연락할 수 있다고 적는다. | ref-1495 | 아니오 | medium | 2026-10-12 | 병원 / 수행 자원 | — |
| f14 | [사실] | 2026년 공고의 등재 명단은 AutoveX Pte Ltd 1개사이며 등재는 2026-09-01부터 2년간 유효하다. | ref-1495 | 아니오 | medium | 2026-10-12 | 병원 / 수행 자원 | — |
| f15 | [사실] | 개인정보보호위원회는 「이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서」 발표 보도자료(2024-10-14 게시)에서 외부업체 위수탁으로 개인영상정보를 처리하는 경우 보호책임자 지정과 주기적인 점검ㆍ교육 등으로 안전하게 관리할 것을 당부했다. | ref-1494 | 아니오 | medium | 2026-10-12 | — | — |
| f16 | [사실] | RFC 9745(2025-03, Standards Track) §5 는 자원을 폐기 예정(deprecated)으로 표시하는 행위가 자원의 동작을 바꾸지 않으며, 클라이언트는 폐기 표시 전과 같은 방식으로 자원을 계속 쓸 수 있다고 정한다. | ref-706 | 아니오 | medium | 2026-10-12 | — | — |
| f17 | [사실] | RFC 9745 §4 는 Sunset 헤더(RFC 8594)로 자원이 응답하지 않게 될 시각을 함께 알릴 수 있게 하고, Sunset 시각이 Deprecation 시각보다 빨라서는 안 된다(MUST NOT)고 정하며, 두 시각 사이의 최소 간격은 정하지 않는다. | ref-706 | 아니오 | medium | 2026-10-12 | — | — |
| f18 | [사실] | De Noyette·Stähler·Margoni(IIC 56(5):984–1014, 2025)는 데이터법의 영업비밀 체계를 분석하며, 회원국 관할 당국마다 영업비밀 관련 행정 관행이 달라져 더 파편화될 위험이 있다고 지적한다. | ref-1488 | 아니오 | medium | 2026-10-12 | — | — |
| f19 | [추정] | Relay Robotics 공개 약관의 서비스 수준 부속서(Exhibit A)에 따르면 Tier 1(24시간 콜센터)은 서비스 개시일 이후 이메일 지원 요청을 받은 뒤 60분 안에 응답하도록 '상업적으로 합리적인 노력'을 기울이는 조건이며, 복구 완료 시각을 보장하는 문구는 아니다. | ref-1491 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f20 | [추정] | Relay 약관의 같은 부속서 예외 조항에 따르면 고객의 네트워크나 시설(예: 승강기 고장)에서 생긴 문제는 고객이 고칠 때까지 지원 기한이 연장되고, Relay 는 고객 네트워크·시설 문제의 수리 책임을 지지 않는다. | ref-1491 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f21 | [추정] | Relay 약관 §12 에 따르면 면책 의무, 고객의 라이선스 위반, 양측의 비밀유지 위반을 제외한 각 당사자의 책임은 청구 발생 전 18개월 동안 고객이 지급했거나 지급할 요금 총액을 넘지 않으며, 약관 준거법은 미국 캘리포니아주법이다. | ref-1491 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f22 | [추정] | Relay 약관 §5.2 에 따르면 당사자 사이에서 고객이 Relay 와 공유하기로 한 개인정보는 고객 소유이며, Relay 는 서비스 제공 목적에만 쓴다. | ref-1491 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f23 | [추정] | Formant 일반 약관(2026-04-16 갱신)에 따르면 고객이 지정한 통합자('Development Consultant')는 고객의 지시로만 일하며 고객이 그 통합자의 작위·부작위에 책임을 진다. | ref-1496 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f24 | [추정] | Formant 약관의 'Device' 정의에 따르면 하나의 장치에 가상 환경(PLC, Jetson, 가상 머신 등)이 둘 이상 있으면 가상 환경마다 별도 Device 로 센다. | ref-1496 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f25 | [추정] | Formant 약관의 Formant AI 추가 조건에 따르면 고객은 AI 출력에 의존하거나 그 출력으로 명령을 실행하기 전에 출력을 검증하는 사람의 검토 절차를 사용 과정에 두어야 한다. | ref-1496 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f26 | [추정] | AIRROBO(Best Epoch Technology)의 EU 데이터법 고지 §4(b)에 따르면 사용자는 앱에서 데이터를 내보내 한 번에 공유하거나, 승인된 QR 코드로 제3자와 지속 공유할 수 있으며 지속 공유를 받으려는 제3자는 Tuya 클라우드 플랫폼에 등록해야 한다. | ref-1487 | 아니오 | low | 2026-10-12 | 가정 / 작업 대상 | 벤더 주장 |
| f27 | [추정] | AWS IoT RoboRunner 서비스 수준 협약(2022-11-28 갱신)에 따르면 'Error'는 500 또는 503 오류 코드를 돌려준 요청이고, 가용성은 5분 구간마다 오류 없이 처리된 요청 비율로 계산한다. | ref-1492 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f28 | [추정] | 같은 SLA 는 요청이 하나도 없던 5분 구간을 가용성 100%로 간주한다. | ref-1492 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f29 | [추정] | 1X Technologies 의 사전예약 약관(2025-10-28 갱신) §2.4 에 따르면 주문 초대를 받아 로봇을 받으려는 사람은 구매 시점에 제시되는 별도 판매약관(Terms of Sale)에 동의해야 하며, 취소·배송·보증 세부는 주문 초대나 판매약관에 둔다. | ref-1493 | 아니오 | low | 2026-10-12 | 가정 | 벤더 주장 |
| f30 | [의견] | ROP 의 데이터 자산 대장은 데이터 항목마다 데이터법상 역할(사용자·데이터 보유자·제3자), 이용 근거(사용자와의 계약), 요청 가능 범위(쉽게 이용 가능한 데이터·메타데이터), 연결 제품의 출시일(2026-09-12 후 출시 여부)을 따로 기록하고, 개인정보 처리 근거는 별도로 심사하는 편이 좋다. | ref-636 | 아니오 | low | 2026-10-12 | — | — |
| f31 | [의견] | 다사업자 계약은 클라우드 SCC 의 책임 조항을 그대로 옮기지 말고, 로봇 제조사·통합자·시설 관리주체·플랫폼 사이의 제3자 청구 면책을 따로 정해야 하며, 제조물책임지침이 업무 전용 재산 손해를 보상 대상에서 빼므로 사업장 설비·재고 손해는 계약 조항으로 다룰 필요가 커 보인다. | ref-1489, ref-1490 | 아니오 | low | 2026-10-12 | — | — |
| f32 | [의견] | ROP 는 사고 뒤 증거 공개가 법원 판단으로 필요·비례 범위에 한정된다는 점을 전제로, 로그 보관 기간·사고 후 동결·내보내기 형식·영업비밀 분리 절차를 계약 부속서에 미리 정해 두는 편이 좋다. | ref-1490 | 아니오 | low | 2026-10-12 | — | — |
| f33 | [의견] | 서비스 수준 부속서는 응답 시각·원인 분석·복구 완료 시각을 나누고, 시설 장애로 지원 기한이 멈추는 구간의 시작·종료와 확인 주체를 기록하며, API 오류율과 별도로 작업 성공률·지연·시설 대기 시간을 지표로 합의하는 편이 좋다. | ref-1491, ref-1492 | 아니오 | low | 2026-10-12 | — | — |
| f34 | [의견] | 플랫폼 약관과 고객–통합자 계약을 함께 대조해 통합자 행위의 책임 귀속, 과금 수량 단위(로봇 대수·가상 환경·설치 인스턴스)의 대응표와 계량 이의 절차, AI 출력으로 명령을 실행할 때의 검토자·승인 기록을 정하는 편이 좋다. | ref-1496, ref-1491 | 아니오 | low | 2026-10-12 | — | — |
| f35 | [의견] | 제조사의 데이터법 고지가 안내하는 내보내기·제3자 지속 공유 경로는 ROP 온보딩 때 제3자 등록·필드 목록·지연·승인 철회를 직접 시험해 확인하는 편이 좋다. | ref-1487 | 아니오 | low | 2026-10-12 | — | — |
| f36 | [의견] | 통합자 등재(사전 자격)는 연동 역량 평가일 뿐이므로, 등재 사실과 별도로 인수 기준·장애 복구 책임·등재 유효기간 만료 시 처리를 계약에 적는 편이 좋다. | ref-872, ref-1495 | 아니오 | low | 2026-10-12 | 병원 / 완료·인계 | — |
| f37 | [의견] | ROP 어댑터는 제조사 API 의 폐기 예고 시각·종료(Sunset) 시각·전환 문서 링크를 따로 저장하고, 두 시각 사이의 최소 통지 기간은 RFC 가 정하지 않으므로 계약에서 따로 확인하는 편이 좋다. | ref-706 | 아니오 | low | 2026-10-12 | — | — |
| f38 | [의견] | 영상 처리를 다른 사업자에게 맡길 때는 위탁 범위·보호책임자·교육·주기 점검 증빙을 계약 부속서로 관리하고, 데이터 접근 거절(영업비밀) 사유와 이의 경로는 관할별로 기록하되 법학 논문의 제안을 검증된 운영 성과로 표시하지 않는 편이 좋다. | ref-1494, ref-1488 | 아니오 | low | 2026-10-12 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-636 | European Union (EUR-Lex) | Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act) | 2023-12-13 | 정부·연구기관 | high | 2026-10-12 | https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng | 아니오 |
| ref-1192 | European Commission (Shaping Europe's digital future) | Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts | 2025-11-19 | 정부·연구기관 | high | 2026-10-12 | https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding | 아니오 |
| ref-872 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART) | RoMi-H Empanelment Programme 2025 | 2025-05-01 | 정부·연구기관 | medium | 2026-10-12 | https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste | 아니오 |
| ref-706 | IETF (RFC Editor) | RFC 9745: The Deprecation HTTP Response Header Field | 2025-03 | 표준 | high | 2026-10-12 | https://www.rfc-editor.org/info/rfc9745/ | 아니오 |
| ref-1487 | Best Epoch Technology Co., Ltd. (AIRROBO) | EU DATA ACT Notice | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://owebsite-cdn.ubtrobot.com/resources/file/2025/12/25/755762357268549.pdf | 아니오 |
| ref-1488 | De Noyette, E., Stähler, L., Margoni, T. (IIC 56(5)) | Data Secrets: The Data Act's New Trade Secrets Framework | 2025-04-24 | 논문 | medium | 2026-10-12 | https://link.springer.com/article/10.1007/s40319-025-01601-9 | 아니오 |
| ref-1489 | European Commission | ANNEX to the Communication to the Commission — Approval of the draft Commission Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts (with Annexes), C(2025) 7750 final | 2025-11-19 | 정부·연구기관 | high | 2026-10-12 | https://ec.europa.eu/newsroom/dae/redirection/document/121719 | 아니오 |
| ref-1490 | European Union (EUR-Lex) | Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC | 2024-11-18 | 정부·연구기관 | high | 2026-10-12 | https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng | 아니오 |
| ref-1491 | Relay Robotics | Terms of Service (Exhibit A: Service Level Agreement) | 2023-03-01 | 벤더 문서 | medium | 2026-10-12 | https://relayrobotics.com/tos | 아니오 |
| ref-1492 | Amazon Web Services | AWS IoT RoboRunner Service Level Agreement | 2022-11-28 | 벤더 문서 | medium | 2026-10-12 | https://aws.amazon.com/roborunner/sla/ | 아니오 |
| ref-1493 | 1X Technologies, Inc. | Pre-Order Terms | 2025-10-28 | 벤더 문서 | medium | 2026-10-12 | https://www.1x.tech/legal | 아니오 |
| ref-1494 | 개인정보보호위원회 | 자율주행 인공지능(AI) 발전을 위한 개인영상정보 보호ㆍ활용 기준 나왔다 | 2024-10-14 | 정부·연구기관 | high | 2026-10-12 | https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=10678 | 아니오 |
| ref-1495 | SingHealth / Changi General Hospital CHART | RoMi-H Empanelment Programme 2026 | 2026-05-06 | 정부·연구기관 | medium | 2026-10-12 | https://www.singhealth.com.sg/news/robotics/romi-h-empanelment-programme-2026 | 아니오 |
| ref-1496 | Formant | General Terms | 2026-04-16 | 벤더 문서 | medium | 2026-10-12 | https://www.formant.ai/terms_of_use | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md | 4, 5, 6, 7, 8, 11 | 갱신(차등): 섹션 4(분리 2026-09-30-area58-s4) — 40행 '데이터 보유자' 항목 정정: '사용자와 계약을 맺어야 하고 사용자 동의 없이 비개인 데이터를 이용할 수 없다'[사실][^ref-1191] → '쉽게 이용 가능한 비개인 데이터를 사용자와의 계약을 근거로만 이용할 수 있고, 사용자의 시장 지위를 해치는 추론에 쓸 수 없다'(f1, 근거 ref-636 원문). '쉽게 이용 가능한 데이터' 범위(f2)를 같은 항목이나 새 줄로 / 섹션 5 — 병원 사례: 71행 표 '수행 자원'과 76행 본문의 '연 2회'를 원어 'bi-annual'(2025 공고) 인용과 두 해석(연 2회/2년마다) 병기 또는 [추정]으로 정정(f11·f12), 2025 등재 5개사·2년 유효(f11), 2026 공고의 연례 표현·RFP/RFI 연락 경로(f13)와 AutoveX 2026-09-01부터 2년(f14)을 추가하고 '(2025-05 기준)'을 연차별로 나눔. ref-872 각주의 '(원문 미열람)' 해소. 의견 f36. 새 사례 블록(배송 로봇 서비스 계약; 약관이 현장 유형을 특정하지 않아 '병원·호텔 배송 로봇 업체의 공개 약관'으로만 표기): Relay 약관의 Tier 1 60분 응답 노력(f19), 시설 장애(승강기 고장) 시 지원 기한 연장(f20)을 '단일 업체 약관에 따르면' [추정]·벤더 주장으로, 완료·인계/예외·성과는 미확인. 가정 사례에 AIRROBO 고지의 QR 지속 공유 경로(f26)와 1X 사전예약 약관의 판매약관 위임(f29)을 [추정]·벤더 주장으로 짧게; 의견 f35 / 섹션 6(분리 2026-09-30-area58-s6) — 데이터 접근·공유 계약 소절: 일반 적용일(기존 51행) 뒤에 제3조(1) 설계 의무는 2026-09-12 후 출시 제품에만 적용(f3), 제4조(1)·(13) 범위와 계약 근거(f1·f2); MCT/SCC 문단(53행) 뒤에 부속서 X 의 면책 조항 부재와 제3자 청구 검토 권고(f4); 의견 f30·f31. 변경 주체 책임 소절: EU 개정 제조물책임지침의 다사업자 책임 관점 핵심만 — 소프트웨어 포함·비상업 FOSS 제외(f5), 실질적 변경자=제조자(f6), 적용 대상 '2026-12-08 후' 출시·투입 = 2026-12-09부터(f7, 정오표 2026-05-07; '2026-12-08부터'로 쓰지 말 것), 이행 기한 2026-12-09·구 지침 폐지(f8), 업무 전용 재산 손해 제외(f9), 증거 공개 필요·비례성과 영업비밀 고려(f10); 의견 f31·f32. 서비스 수준 약속과 감사 이력 소절: 공개 약관 비교 — Relay 책임 상한 18개월 요금·예외 3가지·캘리포니아 준거법(f21), 개인정보 고객 귀속(f22), Formant 통합자 책임 고객 귀속(f23)·가상 환경별 Device 계수(f24)·AI 출력 사람 검토(f25), AWS RoboRunner Error=500/503·5분 가용성·요청 없는 구간 100%(f27·f28) — 모두 [추정]·벤더 주장, 문장에 'OO사 약관에 따르면', 단일 업체 사례로 한정하고 업체 간 교차 확인으로 세지 않음; 의견 f33·f34. 영상 위탁 관리: 개인정보위 보도자료의 위수탁 시 보호책임자·주기 점검·교육 당부(f15)를 한두 문장으로만 넣고 53영역으로 연결; 의견 f38 / 섹션 7(분리 2026-09-30-area58-s7) — 데이터법 행(41행)에 '제3조(1)은 2026-09-12 후 출시 제품' 추가(f3). 행 추가: EU 개정 제조물책임지침(Directive (EU) 2024/2853, 소프트웨어 포함·실질적 변경자·적용 2026-12-09부터·이행 기한 2026-12-09, f5~f8), RFC 9745(폐기 표시는 동작 불변, Sunset≥Deprecation, 최소 간격 미규정, f16·f17); 의견 f37 / 섹션 8 — 연구 항목 추가: De Noyette·Stähler·Margoni(IIC 2025) 데이터법 영업비밀 체계와 관할별 행정 관행 파편화 위험(f18); 기존 MCT 항목(109행)은 기존 내용 확인(부속서 X 면책 공백은 6절로) / 섹션 11(분리 2026-09-30-area58-s11) — 해결 없음. 부분 근거: oq-241(f19~f25, 네 당사자 공통 분담표는 여전히 없음), oq-268(f24·f27·f28·f20; 메모의 'Formant 가상 환경 수량 공동 검증 주문서' 질문은 oq-268 의 하위 질문이라 새로 만들지 않음), oq-279·oq-320(f1·f2, 특정 ROP 지위 미판정), oq-280·oq-207(f16·f17, 로봇 계약상 최소 통지 일수 미확인), oq-259(f15), oq-185(f29, 원격 조작자 책임 미확인), oq-249(f10 은 법원 증거 공개 범위일 뿐 기계 규정 로그 의무의 플랫폼 적용은 미판정), oq-289(f5·f6 원문 조문만, 오케스트레이션 SW 해당 여부 미판정), oq-149(f13·f14, 국내 사례 없음), oq-110(f1~f3·f26). 답하지 못함: oq-145, oq-265, oq-281(가이드 본문 미열람), oq-282, oq-283, oq-290. 새 질문 3건 / 기존 내용 확인(새로 넣지 않음): MCT·SCC 사용이 자발적이라는 점(메모 F04) — s6.md 53행·s7.md 42행·본 페이지 109행·용어집 model-contractual-terms; 데이터법 일반 적용일 2025-09-12 — s6.md 51행·s7.md 41행; RFC 9745 Sunset≥Deprecation — 2026-09-25-area28-s4.md 40행(원문 미열람 근거였음); 증거 공개 제도 자체 — 2026-09-30-area59-s6.md 45행; 영상 위탁 점검 — privacy-and-video-data.md 108행(기사 ref-1136 근거) / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/glossary/data-holder.md 정의가 '연결 제품' 정의처럼 잘못 쓰임, docs/categories/security-and-privacy/index.md 169행의 비슷한 서술(ref-1274, ref-1191 과 같은 EC 해설 페이지), docs/topics/2026/2026-09-25-area28-s3.md 41행 '주요 조항의 적용 개시일은 미확인'(f3 로 해소 가능), docs/topics/2026/2026-09-30-area03-s7.md 44행·2026-09-30-area56-s7.md 46행 '연 2회'(f12), 59영역(2026-09-30-area59-s3·s4·s6·s7·s8, glossary/product-liability.md, standards/index.md 342행)의 제조물책임지침 서술 근거를 Gibson Dunn 해설(ref-1227)에서 원문(ref-1490)으로, 53영역 108행 근거를 1차 보도자료(ref-1494)로, ref-706 서지(발행 2025-03, 원문 열람). EU AI법 제25·26조 서술(s6.md 43·65행)은 개정 여부 점검 필요(미확인). 다음 실행 후보: 59. 법·규제·보험·라이선스(f5~f10), 63. 병원·의료(f11~f14), 3. 경제성·조달·사업 모델(f24·f27·f28) |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 여러 사업자가 얽힌 장애·사고에서 서비스 수준 협약의 지원 기한을 멈추는 사유(시설 장애 등)와 재개 시점을 누가 확인·승인하며, 각 계약의 로그를 어떤 공통 식별자로 연결하는가? (관련: oq-112) | 관련 영역: 58. 다사업자 책임·계약·데이터, 32. 예외 복구·재계획·업무 연속성 | 근거: f20 | 종류: 일반
- 제조사의 데이터법 고지가 안내하는 제3자 지속 공유 경로(승인 QR 코드·외부 플랫폼 등록 등)는 실제로 어떤 필드를 어떤 지연으로 제공하며, 사용자가 승인을 철회하면 언제 공유가 끊기는가? (관련: oq-110, oq-279) | 관련 영역: 58. 다사업자 책임·계약·데이터, 20. 로봇·제조사 관제 연동 | 근거: f26 | 종류: 일반
- RoMi-H 통합자 등재 프로그램의 실제 운영 주기는 무엇인가(2025 공고 'bi-annual', 2026 공고 'annual', 등재 유효 2년), 그리고 유효기간이 끝난 등재 통합자가 맡은 연동의 유지·장애 복구 책임은 어떻게 이어지는가? (관련: oq-149) | 관련 영역: 58. 다사업자 책임·계약·데이터, 63. 병원·의료 | 근거: f12 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 14 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 10건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-01/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f4: C(2025) 7750 final 의 권고가 최종 채택(관보 게재)되었는지와 다국어본 공개 상태는 확인하지 못함(EC 페이지는 2026-03-03 갱신에도 Draft 표기). 합리적 보상 지침의 후속 발표 여부도 미확인
    - f5~f10: 회원국별 제조물책임지침 이행 법령과 국내 제조물책임법의 소프트웨어 포함 개정 여부(oq-290)는 확인하지 못함. 오케스트레이션 소프트웨어가 제품·관련 서비스에 해당하는지(oq-289)는 판단하지 않음
    - f11·f12: 2025 공고 'bi-annual'의 의도(연 2회/2년마다)는 공고 원문만으로 확정할 수 없음
    - f15: 개인정보위 보도자료는 독립 검증 보고의 원문 대조 기준이며, 안내서 본문(ref-1135)과 개인정보 보호법 조문은 이번에 다시 열지 않음
    - f18: 논문 §4.1.4 구절은 독립 검증 보고의 원문 대조 기준(로컬 저장본은 접근 차단 페이지), 서지는 Crossref 로 확인
    - f19~f29: 벤더 약관은 공개 웹 문안이며 개별 체결본·주문서·단가·이행 실적은 미확인. AWS IoT RoboRunner 의 조사일 현재 신규 제공·지원 상태 미확인(지원 종료 공지는 찾지 못함). AIRROBO 고지의 발행일 미확인(PDF 작성 2025-12-23)
    - 검증 보고의 2차 자료 언급: 데이터법 개정안(Digital Omnibus, COM(2025) 837)이 협상 중으로 보이고 EU AI법이 개정되었다는 점은 원문으로 확인하지 않아 finding 으로 넣지 않음 — s6.md 의 AI법 제25·26조 서술 영향은 후속 점검
    - oq-145(모델 대체·라우팅 희석 계약), oq-265(R15.08-3 사용자 의무), oq-281(산업데이터 계약 가이드 432쪽 본문), oq-282(기계 규정 실질적 변경과 플랫폼 설정 변경), oq-283(로봇-승강기 연동 표준 결과물)은 이번 메모가 답하지 못함
- 범위 경계 위반 의심:
    - f5~f10: EU 제조물책임지침의 법적 효력·적용 판단은 59. 법·규제·보험·라이선스 쪽 내용이므로 조문 확인까지만 하고 다사업자 책임 관점 핵심만 씀
    - f15: 영상 위탁 관리는 53. 개인정보·영상 데이터와 겹치며, 이 영역에는 계약 부속서 관리 관점의 짧은 연결로만 씀
    - f11~f14: RoMi-H 등재는 63. 병원·의료와 겹치며, 이 영역에는 통합자 사전 자격과 책임 주체 관점으로만 씀
    - f16·f17: RFC 9745 는 41. 플랫폼 아키텍처·외부 API, 21. 상호운용 표준·적합성과 겹치며, 이 영역에는 제조사 API 폐기 통지의 계약 관점으로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 10건/15(ref-1487~ref-1496, 예약 구간 ref-1487~ref-1516 안), 재사용 4건(ref-636·ref-1192·ref-872·ref-706). 출처 매핑(검증 결과 기준): 메모 n1→ref-636, n2→ref-1487(UBTech CDN), n3→ref-1488, n4→ref-1192, n5→ref-1489(미러 dirittobancario.it 대신 공식 EC URL), n6→ref-1490(EUR-Lex 원문; ref-1227 은 해설이라 쓰지 않음), n7→ref-1491(약관 표기 2023-03-01), n8→ref-1492, n9→ref-1493, n10→ref-1494(안내서 ref-1135·기사 ref-1136 과 별개 1차 보도자료), n11→ref-1495, n12→ref-872, n13→ref-706(원문 열람), n14→ref-1496. 교차 확인 0건(모든 사실 finding 이 단일 출처이거나 같은 기관 계열: EC 발표·부속서, CHART 2025·2026 공고) — 신뢰도 medium 이하. 벤더 약관 11건(Relay·Formant·AIRROBO·AWS·1X)은 모두 [추정]·vendor_claim, 서로 다른 업체의 다른 조건이라 교차 확인으로 세지 않음. 검증 반영: A01 정정 위치를 6절이 아니라 s4.md 40행(4절)으로, 근거 ref-1191→ref-636(f1); F03 제3조(1) 적용 대상(2026-09-12 후 출시)과 일반 적용일(2025-09-12) 구분(f3); F04 는 기존 내용이라 제외; F05 출처를 공식 EC URL 로(f4, 면책 조항 없음); 제조물책임지침은 다사업자 책임 관점 핵심만(f5~f10) 넣고 정오표 표기 '2026-12-08 후'=2026-12-09부터로 명시(f7), 제8조(2) 실질적 변경자 추가(f6); F13 'bi-annual' 원어 인용과 두 해석으로 정정(f11 사실·f12 추정); F14 는 53영역 중복이라 짧게(f15); RFC 9745 는 원문 열람으로 보강(f16·f17); 벤더 약관 X01~X11 은 '○○사 약관에 따르면'·단일 업체 사례로 한정(f19~f29), Formant 는 정의 번호 대신 용어 이름으로 인용. 열린 질문: 해결 없음. 부분 근거 oq-241·oq-268·oq-279·oq-320·oq-280·oq-207·oq-259·oq-185·oq-249·oq-289·oq-149·oq-110. 메모의 '답한 열린 질문' 가운데 '새 질문' 5건은 문구 대조로 기존 oq-279~oq-283 과 같아 새로 만들지 않음. 메모의 '새로 생긴 열린 질문' 3건 중 지원 기한 정지·제3자 공유 실동작 2건을 새로 올리고 Formant 수량 검증 건은 oq-268 에 묶음; RoMi-H 주기 질문 1건 추가. 메모의 '.research-work' 로컬 경로·행 번호(L…)는 쓰지 않고 원문 조·절·쪽과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
```

### runs/2026-10-11-06/research.md

```markdown
# 리서치 브리프 2026-10-11-06

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-11-06 |
| 날짜 | 2026-10-11 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 50. 안전 표준·인증·사고 조사 |
| 대분류 | M. 안전 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 — 실외 사례 표·본문(98·100·104·106행)이 고시 제2023-211호를 현행 근거로 두고 심사항목 8개·16가지를 '어느 쪽도 고르지 않고' 병기하며, 행정예고 기준값을 '확정 고시 별표 원문 미확인'으로 둠. 제조 공장·물류창고 사고 사례는 수사·조사 중 기사 두 건뿐이고 공식 재해사례 자료가 없음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area50-s6) — '사고 기록 장치' 소절의 '기록할 데이터 형식과 보존 기간 … 미확인'(45행), 조직·제어 책임까지 보는 사고 분석 방법(CAST) 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area50-s7) — EN ISO 10218 EU 조화 게재 행(42행)이 IBF 해설 단독 근거로 [사실], 실외이동로봇 행(45행)의 '고시 제2023-211호가 정한다'가 낡음, R15.08-3·ISO 3691-4 차기판·KS 부합판·UL 3100·국내 자율안전확인·EU 기계 규정 기록 요구·rosbag2/MCAP 기록 계약 없음
- 섹션 8. 대표 연구와 자료(분리 2026-09-30-area50-s8) — Sanders 외의 관측 기간·관할 범위 미기재, 미국 보상 청구 자료(Suresh 외 2026) 없음, Webb 외 역할극의 수행 조건·한계 미기재
- 섹션 4. 핵심 개념과 용어(분리 2026-09-30-area50-s4) — '적합성 추정' 항목(41행)이 해설 기준이고 2027-01-20 목록 폐지 미반영, '중상 보고' 항목(45행)의 기간이 연 단위
- 섹션 9. 책임 경계 — 실외 인증이 요구하는 관제장치 기능(실시간 상태·원격 정지)과 인증 정보의 관제장치 모델 단위 미반영
- 섹션 11. 열린 질문(분리 2026-09-30-area50-s11) — oq-186·oq-230 이 별표 원문 미확인 상태, oq-384(ISO 3691-4 차기판 단계 충돌) 미해소
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: 고시 근거(제2025-021호), 16/8 항목 경위, EU 게재 서술 강등, ref-789 제목, 'KS B ISO 10218-2 2017 확인'

## 조사 질문

1. 어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? [분류원문]
2. oq-186·oq-230 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시와 항목 대응은 무엇인가? (섹션 5·7·11 겨냥)
3. EN ISO 10218-1/-2:2025 의 EU 조화 게재는 어떤 법령에 대한 것이며 언제까지 효력이 있는가, ISO 3691-4 차기판·국내 KS 부합판의 현재 상태는 무엇인가(oq-384, oq-251)? (섹션 4·7 겨냥)
4. oq-252 사고 조사에 필요한 기록 항목·형식·보존을 정한 공개 규약(EBB 초안, EU 기계 규정, rosbag2·MCAP)은 무엇을 정하고 무엇을 비워 두는가? (섹션 6·7 겨냥)
5. 로봇 사고 통계(OSHA SIR, Ohio 보상 청구, 국내 공식 재해사례)는 어떤 관할·기간·집계 단위·한계를 가지는가? (섹션 5·8 겨냥)
6. 사고 원인을 개인 과실이 아니라 제어 구조·조직 정책까지 조사하는 방법(CAST·역할극 증언)은 무엇을 요구하고 어떤 한계가 있는가? (섹션 6·8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | 위원회 시행결정 (EU) 2026/2015(2026-09-04 채택, 2026-09-07 관보 L 시리즈 게재)의 부속서는 시행결정 (EU) 2023/1586 부속서 I 에 EN ISO 10218-1:2025(223a)와 EN ISO 10218-2:2025(224a)의 참조를 추가한다. | ref-1496 | 아니오 | medium | 2026-10-11 | — | — |
| f2 | [사실] | 이 결정이 참조를 추가한 목록(2023/1586 부속서 I)은 기계류 지침 2006/42/EC 에 대한 적합성 추정을 주는 조화 표준 목록이며, 같은 결정 제2조는 2023/1586 을 2027-01-20 부로 폐지한다. 전문 (14)는 그 이유를 지침 2006/42/EC 가 규정 (EU) 2023/1230 으로 같은 날 폐지되기 때문이라고 적는다. | ref-1496 | 아니오 | medium | 2026-10-11 | — | — |
| f3 | [추정] | 기존 위키(2026-09-30-area50-s7.md 42행)의 'PL d·범주 3 일률 요구 대신 표의 기본 성능 수준 또는 위험성평가 근거 선택 허용, 운전 정지용 정상 정지 기능 신설' 서술은 컨설팅사 IBF Solutions 해설만 근거로 [사실]로 실려 있다. 관보 원문으로 확인되는 것은 참조 게재 사실·날짜·법적 기반뿐이므로 이 서술은 [추정]·벤더 해설로 낮추는 것이 맞다. | ref-1116, ref-1496 | 아니오 | low | 2026-10-11 | — | 벤더 주장 |
| f4 | [추정] | ANSI/A3 R15.08-3-2026(Part 3: Use of IMR Applications)은 A3 판매 페이지 기준 2026-04-23 발행으로 표시되며, 이 사실은 위키에 이미 있다. 이 영역 7절 표에는 R15.08-2 만 있어 Part 3 행을 더할 근거로만 쓴다. | ref-1255 | 아니오 | low | 2026-10-11 | — | 원문 미열람 |
| f5 | [사실] | ISO 3691-4 차기판 프로젝트는 ISO 위원회 페이지에서 'ISO/DIS 3691-4, Edition 3, Under development'이며 단계 40.60(투표 종료, 2026-09-10)으로 표시되고 ISO 3691-4:2023 을 대체할 예정이다. 발행된 개정판이 아니다. | ref-789 | 아니오 | medium | 2026-10-11 | — | — |
| f6 | [사실] | 국가표준 목록에서 KS B ISO 10218-1(산업용 로봇의 안전 요구사항 제1부: 로봇)의 대응 국제표준은 ISO 10218-1:2011(IDT, 일치)이고 최종개정확인일은 2021-11-26 이다(제정 2008-01-17). | ref-1497 | 아니오 | medium | 2026-10-11 | — | — |
| f7 | [사실] | 같은 목록에서 KS B ISO 10218-2(제2부: 로봇 시스템 및 통합)의 대응 국제표준은 ISO 10218-2:2011(IDT)이고 최종개정확인일은 2022-10-12(고시 제2022-0433호)다. 위키의 'KS B ISO 10218-2 2017 확인' 표현은 낡았다. | ref-211 | 아니오 | medium | 2026-10-11 | — | — |
| f8 | [사실] | EU 기계 규정 (EU) 2023/1230 부속서 III 1.2.1(f)는 제어 시스템을, 개입과 관련해 생성된 데이터와 출시·사용 개시 뒤 업로드한 안전 소프트웨어 판의 추적 기록이 업로드 뒤 5년간 활성화되도록 설계·제작해야 한다고 정한다. 목적은 관할 국가기관의 이유 있는 요청에 따른 적합성 입증에 한정된다. | ref-555 | 아니오 | medium | 2026-10-11 | — | — |
| f9 | [사실] | 같은 절 둘째 목록 (b)는 행동·논리가 전부 또는 일부 자체 진화하며 여러 자율성 수준으로 작동하도록 설계된 기계의 제어 시스템에 대해, 안전 기능을 보장하는 소프트웨어 기반 안전 시스템의 안전 관련 의사결정 데이터를 기록하고 수집 뒤 1년간 보존하도록 정한다. | ref-555 | 아니오 | medium | 2026-10-11 | — | — |
| f10 | [사실] | UL 3100(Automated Mobile Platforms, AMPs) 공식 목록은 제1판의 최초 발행일을 2021-05-26, 최근 개정일과 ANSI 승인일을 2026-06-10 으로 표시한다. | ref-1498 | 아니오 | medium | 2026-10-11 | — | — |
| f11 | [사실] | UL 3100 의 공개 적용 범위 1.4 는 산업용 로봇 자체의 요구사항은 포함하지 않으며(UL 1740·CSA Z434 가 다룸), 그 표준에 맞는 로봇 매니퓰레이터는 통합 시스템의 탑재물로 쓸 수 있다고 적는다. | ref-1498 | 아니오 | medium | 2026-10-11 | — | — |
| f12 | [추정] | UL Solutions 는 2026-03-11 보도자료에서 Simbe 의 매장용 자율이동로봇 Tally 가 UL 3300(SCIEE 로봇 표준) 인증을 받았으며, 로봇과 충전 도크가 화재·감전 위험과 안전한 자율 이동 시험을 거쳤다고 발표했다. | ref-1499 | 아니오 | low | 2026-10-11 | — | 벤더 주장 |
| f13 | [사실] | 정부의 2025-11-27 보도참고자료(신산업 규제합리화 1호 로드맵, AI 분야)는 실외이동로봇 운행안전인증의 심사 평가항목을 16개에서 8개로 통폐합하고 심사기간을 60일에서 30일로 줄였다고('25.11 시행) 적는다. | ref-1504 | 아니오 | medium | 2026-10-11 | — | — |
| f14 | [사실] | 산업통상부 고시 제2025-021호(실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 일부개정)는 2025-11-24 발령되었고 부칙에서 '발령한 날부터 시행'하므로 2025-11-24 부터 시행이다. 현행 절차·기준의 근거는 제2023-211호가 아니라 이 개정 고시다. | ref-1505 | 아니오 | medium | 2026-10-11 | — | — |
| f15 | [추정] | 고시 제2023-211호는 2023-11-17 발령(제정)되었다. 시행일은 원 고시 첨부 부칙이 '2023년 11월 17일부터 시행', 제2025-021호 첨부 본문에 실린 구 부칙(<제2023-211호, 2023.11.17.>)이 '2023년 11월 21일부터 시행'으로 서로 달라 확정하지 않는다. | ref-1118, ref-1505 | 아니오 | low | 2026-10-11 | — | — |
| f16 | [사실] | 고시 제2025-021호 제9조①은 운행안전인증기관이 인증신청서를 접수한 날부터 30일 이내에 심사 결과를 통보하도록 정한다. 제2023-211호 제9조①에는 이 기한이 없고 심사 종료 뒤 통보만 정했다. | ref-1505, ref-1118 | 아니오 | medium | 2026-10-11 | — | — |
| f17 | [사실] | 고시 제2023-211호 별표 3(운행안전인증 기준)은 질량 및 폭 제한, 운행 속도, 겉모양, 동적 안정성, 비상정지, 운행구역 준수, 속도 제어, 장애물 감지, 알림음, 등화장치, 방수 성능, 물리적 보안, 횡단보도 통행, 관제장치, 통신장애 대응, 원격조작의 16개 항목을 둔다. | ref-1118 | 아니오 | medium | 2026-10-11 | — | — |
| f18 | [사실] | 현행 고시 제2025-021호 별표 3 은 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치의 8개 항목을 두며, 한국로봇산업진흥원 안내의 8개 심사항목과 이름이 같다. | ref-1505, ref-980 | 아니오 | medium | 2026-10-11 | — | — |
| f19 | [사실] | 두 별표를 조문으로 대조하면 구 질량·폭 제한과 운행 속도는 '규격 및 운행속도'로, 동적 안정성(5° 경사·30 mm 턱)과 속도 제어(±10 %)는 '동적 특성'으로, 운행구역 준수와 장애물 감지는 '주변 인식'으로, 관제장치와 원격조작(원격 정지·영상 확인 원격 수동조작)은 '관제장치'로 합쳐졌다. 알림음(55~73 dB(A)), 등화장치(표면 60℃ 이하), 물리적 보안(통신포트·저장장치 단자 보호)은 새 별표에 없고, 통신장애 대응(운행계획서 시나리오)은 횡단보도 통행 중 통신 단절 시 정차 조항으로만 남았다. 빠진 항목이 다른 규정으로 옮겨졌는지는 확인하지 못했다. | ref-1118, ref-1505 | 아니오 | medium | 2026-10-11 | — | — |
| f20 | [사실] | 본 페이지 5절이 '2023-07 행정예고안 보도 기준, 확정 고시 별표 원문 미확인'으로 둔 기준 예시(질량별 속도 230 kg 초과 5 km/h·100 kg 초과 10 km/h, 폭 800 mm·보도 2,500 mm 이상이면 1,200 mm, 5° 경사, 알림음 55~73 dB, 등화장치 60℃, IPX4)는 확정 고시 제2023-211호 별표 3 에 그대로 있다. 현행 제2025-021호에는 질량·폭·속도·5° 경사·IPX4 는 남고 알림음·등화장치 기준은 없다. | ref-1118, ref-1505 | 아니오 | medium | 2026-10-11 | — | — |
| f21 | [사실] | 현행 별표 3 의 관제장치 항목은 관제장치가 운용 중인 모든 로봇을 식별하고, 모든 로봇의 위치·속력, 주행가능 거리 또는 배터리 잔량, 로봇–관제장치 통신 신호 감도, 상태(주행·대기·비상정지·오류)를 실시간으로 확인할 수 있어야 하며, 통행 불가 시 관제장치 알림과 관리자 조치, 원격 정지 수단, 영상장치로 주변을 확인하는 원격 수동조작을 요구한다. | ref-1505 | 아니오 | medium | 2026-10-11 | 실외 / 수행 자원 | — |
| f22 | [사실] | 고시 제2025-021호 제10조②는 인증기관이 인증번호, 회사명, 실외이동로봇 제품명·모델명과 함께 관제장치 제품명·모델명, 소재지 등의 정보를 보관하도록 정해, 인증 정보가 로봇 모델과 관제장치 모델의 조합으로 관리됨을 보여 준다. | ref-1505 | 아니오 | medium | 2026-10-11 | 실외 / 수행 자원 | — |
| f23 | [사실] | 안전보건공단 산업안전보건인증원의 자율안전확인 대상 안내는 산업용 로봇을 직교좌표로봇을 포함해 3축 이상의 매니퓰레이터(액추에이터·교시 펜던트·제어기·통신 인터페이스 포함)를 갖추고 전용 제어기로 프로그램·자동제어가 가능한 고정식 로봇으로 정의한다. | ref-1500 | 아니오 | medium | 2026-10-11 | — | — |
| f24 | [사실] | Sanders 외(2024)가 분석한 OSHA 중상 보고(SIR)의 기간은 2015-01-01 부터 2022-04-30 까지다. | ref-1122 | 아니오 | medium | 2026-10-11 | — | — |
| f25 | [사실] | 같은 연구는 SIR 이 연방 OSHA 관할 사업장의 보고만 담고 자체 주 계획(State Plan)을 운영하는 22개 주의 사업장은 포함하지 않는다고 밝힌다. | ref-1122 | 아니오 | medium | 2026-10-11 | — | — |
| f26 | [사실] | 같은 연구에서 분석한 사고 서술의 단어 수 중앙값은 36 단어였다. | ref-1122 | 아니오 | medium | 2026-10-11 | — | — |
| f27 | [사실] | Suresh 외(American Journal of Industrial Medicine 69(5), 2026)는 Ohio 산재보상국(OHBWC) 자료에서 2001~2020년 로봇 관련 산재보상 청구 1,076건을 키워드 검색으로 찾았다. | ref-1501 | 아니오 | medium | 2026-10-11 | — | — |
| f28 | [사실] | 초록 기준으로 이 청구의 85% 가 의료비만 청구(의료 처치만 또는 휴업 7일 이하)였고, 청구의 75.7% 가 공유 작업공간에서 협동 적용 로봇 팔을 다루는 작업과 관련됐다. | ref-1501 | 아니오 | medium | 2026-10-11 | — | — |
| f29 | [사실] | 안전보건공단 공개 재해사례(광주 광산구 사업장)는 로봇 용접기의 용접 팁 교체 작업자가 작동 중인 로봇 팔과 지그 사이에 흉부가 끼어 숨진 사고의 원인을 두 가지로 든다: 일시중지(muting) 기능 사용으로 감응식 방호장치가 작동하지 않은 것, 로봇 운전을 정지하지 않고 안전 조치가 없는 재료 투입구로 셀에 들어간 것. | ref-1502 | 아니오 | medium | 2026-10-11 | 제조 공장 / 예외·성과 | — |
| f30 | [사실] | 같은 사례의 재발방지대책은 출입 시 감응식 방호장치가 작동하도록 하고 muting 사용 시 다른 수단으로 안전이 유지되도록 관리하며, 수리·점검 같은 비정형 작업은 로봇 운전을 정지한 뒤 출입문으로 들어가 하라고 제시한다. | ref-1502 | 아니오 | medium | 2026-10-11 | 제조 공장 / 제약 | — |
| f31 | [사실] | Leveson 의 MIT OCW 강의 자료(16.863J System Safety, 2016년 봄 학기) 'CAST 분석'은 SO2 탱크 넘침 사례에서 안전 핵심 장비가 오랫동안 작동하지 않은 이유, 그런 상태로 공장을 운전하는 정책과 위험성평가 여부, 점검·정비 정책을 조사 질문으로 던진다. | ref-1506 | 아니오 | medium | 2026-10-11 | — | — |
| f32 | [사실] | 같은 강의는 운전원 수준 분석 항목으로 맥락·시스템 요인과 정신 모형의 결함을 두고, 사후 판단 편향(hindsight bias)을 경계한다. | ref-1506 | 아니오 | medium | 2026-10-11 | — | — |
| f33 | [사실] | Webb 외(2021)는 2020년 11월 같은 연구자 한 명이 Zoom 으로 가상 목격자 증언(VWT) 역할극 면담 22회를 진행했으며, 실제 사고가 아닌 삽화 시나리오를 보여 주는 방식이었다. | ref-1121 | 아니오 | medium | 2026-10-11 | — | — |
| f34 | [사실] | 연구진은 정지 이미지를 써서 시나리오의 동적인 부분을 효과적으로 전달하지 못했다고 한계를 밝혔다(예: 로봇이 거주자 다리와 부딪혔을 가능성을 시사하는 움직임). | ref-1121 | 아니오 | medium | 2026-10-11 | — | — |
| f35 | [사실] | 윤리적 블랙박스 초안(ICRES 2022 게재본 부록, RFC Draft 0.1)은 날짜 필드 ebbD 의 길이를 표에서는 10자, MD 기록 주석 2 에서는 12 ASCII 문자로 다르게 적고, 시각 필드도 표와 주석이 다르다. | ref-1503 | 아니오 | medium | 2026-10-11 | — | — |
| f36 | [사실] | 같은 초안의 체크섬 표기는 표 2 의 4 문자, 표 3 의 8자리 16진수, 주석 4 의 '64비트 비암호학적 해시(추후 결정)'로 서로 맞지 않는다. | ref-1503 | 아니오 | medium | 2026-10-11 | — | — |
| f37 | [사실] | 초안은 로봇 결정 코드의 숫자값 정의를 표준 범위 밖으로 두고 로봇 제조사나 운영자에게 맡긴다. | ref-1503 | 아니오 | medium | 2026-10-11 | — | — |
| f38 | [사실] | 초안의 로봇 데이터(RD) 기록은 저장 한도에 이르면 가장 오래된 RD 기록부터 덮어쓰는 순환 구조이며, 고정 보존 기간을 정하지 않는다. | ref-1503 | 아니오 | medium | 2026-10-11 | — | — |
| f39 | [사실] | rosbag2 0.35.0 README 의 --repeat-transient-local 옵션은 지정 토픽의 최근 N개(기본 1개) 메시지를 보관했다가 분할로 새 파일이 시작되거나 스냅샷을 쓸 때 앞에 다시 넣는다. | ref-831 | 아니오 | medium | 2026-10-11 | — | — |
| f40 | [사실] | 같은 판의 스냅샷 모드는 메시지를 바로 디스크에 쓰지 않고 --max-cache-size(바이트)와 선택적 --max-cache-duration(초)로 제한한 메모리 순환 버퍼에 두었다가 요청 시(~/snapshot 서비스) 디스크에 저장한다. | ref-831 | 아니오 | medium | 2026-10-11 | — | — |
| f41 | [사실] | rosbag2 의 유실 메시지 통계는 증분 방식이라 유실이 0인 토픽은 이벤트에 들어가지 않고, 내부 카운터는 이벤트를 발행할 때마다 0으로 재설정된다. | ref-831 | 아니오 | medium | 2026-10-11 | — | — |
| f42 | [사실] | MCAP 명세는 Message 레코드의 publish_time 을 '발행 시각, 알 수 없으면 log_time 으로 설정해야 한다(must)'고 정한다. 따라서 publish_time 이 log_time 과 같으면 실제 발행 시각인지 대체값인지 포맷만으로 구분되지 않는다. | ref-1096 | 아니오 | medium | 2026-10-11 | — | — |
| f43 | [사실] | MCAP 명세는 Chunk 의 uncompressed_crc 와 여러 레코드의 crc 값이 0 이면 'CRC 검증을 수행하지 않아야 한다(should not)'는 뜻으로 정한다. CRC 는 오류 검출용이며 서명이나 증거 인계를 보장하지 않는다. | ref-1096 | 아니오 | medium | 2026-10-11 | — | — |
| f44 | [의견] | 표준 레지스트리는 발행판(ISO 3691-4:2023)과 개발 중 프로젝트(ISO/DIS 3691-4 제3판), 국내 부합판(KS B ISO 10218-1·-2, ISO 10218:2011 IDT)과 국제 최신판(ISO 10218:2025), EU 조화 게재(지침 2006/42/EC 기반, 2027-01-20 폐지 예정 목록)를 별도 속성으로 두고, 배포 설정에는 현장 승인된 판을 고정해야 한다. | ref-789, ref-1497, ref-211, ref-1496 | 아니오 | low | 2026-10-11 | — | — |
| f45 | [의견] | 실외이동로봇 인증 정보는 고시 번호·시행일(제2025-021호, 2025-11-24)과 별표 판(16항목/8항목)을 함께 기록하고, 구 별표로 받은 인증과 현행 별표 기준을 구분해야 한다. 현행 관제장치 항목의 실시간 상태(위치·속력·배터리·통신 감도·상태)와 원격 정지는 ROP 가 이종 로봇 상태 모델로 받아야 할 최소 항목으로 쓸 수 있다. | ref-1505, ref-1118 | 아니오 | low | 2026-10-11 | 실외 / 수행 자원 | — |
| f46 | [의견] | EU 부속서 III 1.2.1 의 5년·1년 기록 의무는 안전 소프트웨어 개입·판 이력과 자체 진화 제어의 안전 결정 데이터에 한정되므로, ROP 는 인증 증거용 이력과 일반 작업 로그를 나눠 보존 정책을 정하고 플릿 전체 데이터를 일률적으로 5년 또는 1년 보관해야 한다고 해석하지 않는 것이 맞다. | ref-555 | 아니오 | low | 2026-10-11 | — | — |
| f47 | [의견] | 사고 자료 레코드에는 출처별 관할(연방 OSHA 관할만 등), 관측 기간, 집계 단위(보고 건수·부상 수·보상 청구), 중증도 정의, 노출 분모 유무를 필드로 두어 OSHA SIR 과 Ohio 보상 청구 같은 서로 다른 모집단을 합산·비교하지 않게 해야 한다. | ref-1122, ref-1501 | 아니오 | low | 2026-10-11 | — | — |
| f48 | [의견] | EBB 초안을 공통 기록 스키마로 쓰기 전에 날짜·시각·체크섬 표기 충돌을 해소하고, ROP 쪽에서 제조사 원본 결정 코드·공통 사건 유형·코드표 판·시각 기준·사고 시 보존 잠금을 따로 정의해야 한다. 기록기 쪽에서는 사고 트리거 스냅샷, 정적 토픽 재삽입 depth, 유실 이벤트 수신 여부, MCAP publish_time 대체 여부와 원본 해시·추출 이력을 증거 메타데이터로 함께 남겨야 한다. | ref-1503, ref-1120, ref-831, ref-1096 | 아니오 | low | 2026-10-11 | — | — |
| f49 | [의견] | CAST 의 조사 질문을 플릿 사고에 옮기면, 사건 시간선 뒤에 제조사·통합자·현장 운영자·관제자 각각의 제어 책임, 당시 관측 가능했던 정보, 방호장치 우회(muting)와 정비·승인 정책을 따로 조사하고, '교육 부족' 같은 결론을 증거 없이 먼저 정하지 않는 절차가 필요하다. | ref-1506, ref-1502 | 아니오 | low | 2026-10-11 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1496 | European Commission (Official Journal of the European Union) | Commission Implementing Decision (EU) 2026/2015 of 4 September 2026 amending and repealing Implementing Decision (EU) 2023/1586 as regards harmonised standards for machinery drafted in support of Directive 2006/42/EC | 2026-09-07 | 정부·연구기관 | high | 2026-10-11 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026D2015 | 아니오 |
| ref-1497 | 국가기술표준원 (국가표준인증 통합정보시스템) | KS B ISO 10218-1 로봇 및 로봇장치 ─ 산업용 로봇의 안전에 관한 요구사항 ─ 제1부: 로봇 | 2021-11-26 | 표준 | medium | 2026-10-11 | https://standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSBISO10218-1&menuId=919&reformNo=05&tmprKsNo=KSBISO10218-1&topMenuId=502&upperMenuId=503 | 아니오 |
| ref-1498 | UL Standards & Engagement | UL 3100 Automated Mobile Platforms (AMPs) | 2026-06-10 | 표준 | medium | 2026-10-11 | https://www.shopulstandards.com/ProductDetail.aspx?UniqueKey=39063 | 아니오 |
| ref-1499 | UL Solutions | UL Solutions Grants Its First Global Certification for a Public-Facing Robot to Simbe's Tally Autonomous Mobile Robot | 2026-03-11 | 벤더 문서 | medium | 2026-10-11 | https://www.ul.com/news/ul-solutions-grants-its-first-global-certification-public-facing-robot-simbes-tally-autonomous | 아니오 |
| ref-1500 | 안전보건공단 산업안전보건인증원 | 자율안전확인 대상품 (자율안전확인신고 대상 및 적용범위) | 미확인 | 정부·연구기관 | high | 2026-10-11 | https://miis.kosha.or.kr/oshci/busi/viewMiisJayulMerchandiseInfo.do | 아니오 |
| ref-1501 | Suresh, V., Konda, S., Haney, J. M. 외 (American Journal of Industrial Medicine 69(5)) | Robot-Related Workers' Compensation Claims in Ohio, 2001–2020 | 2026-05 | 논문 | medium | 2026-10-11 | https://stacks.cdc.gov/view/cdc/258698 | 아니오 |
| ref-1502 | 안전보건공단 | 산업용 로봇 팔과 지그 사이에 끼임 (재해사례) | 미확인 | 정부·연구기관 | high | 2026-10-11 | https://oshri.kosha.or.kr/kosha/data/machine.do?articleNo=411924&attachNo=233368&mode=download | 아니오 |
| ref-1503 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (ICRES 2022 Proceedings, CLAWAR) | An Ethical Black Box for Social Robots: a draft Open Standard (ICRES 2022 게재본) | 2022-07 | 논문 | medium | 2026-10-11 | https://doi.org/10.13180/icres.2022.18-19.07.019 | 아니오 |
| ref-1504 | 관계부처 합동 (금융위원회 누리집 게재 보도참고자료) | 규제의 벽은 허물고 AI의 길은 넓힌다 — 신산업 규제합리화 1호 로드맵(AI 분야) 발표 | 2025-11-27 | 정부·연구기관 | high | 2026-10-11 | https://www.fsc.go.kr/no010101/85753 | 아니오 |
| ref-1505 | 산업통상부 | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 (고시 제2025-021호, 일부개정) | 2025-11-24 | 정부·연구기관 | high | 2026-10-11 | https://www.motir.go.kr/kor/article/ATCL0c554f816/64952/view | 아니오 |
| ref-1506 | Leveson, N. (MIT OpenCourseWare, 16.863J System Safety) | System Safety: CAST Analysis (강의 자료) | 2016 | 정부·연구기관 | medium | 2026-10-11 | https://ocw.mit.edu/courses/16-863j-system-safety-spring-2016/7dc4344ef259e4bde4acc1bb2d578a95_MIT16_863JS16_LecNotes3-2.pdf | 아니오 |
| ref-1255 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications | 2026-04-23 | 표준 | medium | 2026-10-11 | https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download | 예 |
| ref-789 | ISO | ISO/DIS 3691-4 (제3판) - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 미확인 | 표준 | medium | 2026-10-11 | https://www.iso.org/standard/88615.html | 아니오 |
| ref-211 | 국가표준인증통합정보시스템(KSSN) | KS B ISO 10218-2 로봇 및 로봇 장치 - 산업용 로봇의 안전에 관한 요구사항 - 제2부: 로봇 시스템 및 통합 | 2022-10-12 | 표준 | medium | 2026-10-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010083660 | 아니오 |
| ref-555 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 2023-06 | 정부·연구기관 | high | 2026-10-11 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 아니오 |
| ref-1122 | Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121) | Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports | 2024 | 논문 | medium | 2026-10-11 | https://eprints.whiterose.ac.uk/id/eprint/217393/ | 아니오 |
| ref-1120 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) | An Ethical Black Box for Social Robots: a draft Open Standard | 2022-05-13 | 논문 | medium | 2026-10-11 | https://arxiv.org/abs/2205.06564 | 예 |
| ref-1121 | Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI) | Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions | 2021-06-29 | 논문 | high | 2026-10-11 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full | 아니오 |
| ref-831 | ROS 2 (ros2/rosbag2 GitHub) | rosbag2 — README (Recording and playback of ROS 2 communications) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/ros2/rosbag2 | 아니오 |
| ref-1096 | MCAP 프로젝트 (Foxglove) | MCAP Format Specification | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://mcap.dev/spec | 아니오 |
| ref-1118 | 산업통상자원부 | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 | 2023-11-17 | 정부·연구기관 | high | 2026-10-11 | https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view | 아니오 |
| ref-1116 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 2026-09-18 | 업계 보고서 | medium | 2026-10-11 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 | 예 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | high | 2026-10-11 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/safety/safety-standards-certification-and-incident-investigation.md | 4, 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 4(분리 2026-09-30-area50-s4) — '적합성 추정' 항목(41행)을 IBF 해설 대신 관보 원문으로 보강(f1)하고 지침 2006/42/EC 기반 목록이 2027-01-20 폐지됨을 덧붙임(f2). '중상 보고' 항목(45행)의 기간을 2015-01-01~2022-04-30 로(f24), 연방 관할 한정(f25) / 섹션 5 — 실외 사례: 104행 '고시 제2023-211호(2023-11-17)로 정해졌고'를 현행 제2025-021호(2025-11-24 발령·시행, f14)로 정정하고 제2023-211호 시행일은 두 원문이 달라 확정하지 않음(f15 [추정], 독립 검증 보고의 2023-11-21 과도 다름); 100행 제약 칸과 106행 W19 문장('8개와 16가지로 달라 어느 쪽도 고르지 않고')을 '구 고시 별표 3 16개(f17) → 현행 별표 3 8개(f18), 2025-11 통폐합(f13)'으로 정정하고 항목 대응·빠진 항목(알림음·등화장치·물리적 보안, 다른 규정 이동 여부 미확인)을 f19 로; 106행 '확정 고시 별표 원문 미확인' 기준값은 2023-211 별표 3 에 있음과 현행 잔존 여부(f20); 98행 30일 처리기간에 제9조① 근거(f16)·60→30일 경위(f13). 제조 공장: 공식 재해사례(용접 팁 교체 끼임, muting 우회·운전 정지 미실시, f29·f30)를 사례로 추가하되 고성·오뚜기 기사 사건과 연결하지 않음; 의견 f45·f49 / 섹션 6(분리 2026-09-30-area50-s6) — '사고 기록 장치' 소절 45행 '형식과 보존 기간 … 미확인'을 EBB 초안 게재본 내용으로 보강: 날짜·시각 필드 충돌(f35), 체크섬 충돌(f36), 결정 코드 제조사 위임(f37), RD 순환 덮어쓰기·보존 기간 없음(f38). 조직·제어 분석 방법 CAST 소절 추가(f31·f32, 2016 은 강의 학기이며 사고 연도 아님); 의견 f48·f49 / 섹션 7(분리 2026-09-30-area50-s7) — 42행 EN ISO 10218 EU 조화 게재 행: 게재 사실·날짜·법적 기반은 관보 원문(f1·f2)으로, PL d·범주 3 대체·정상 정지 서술은 IBF 단독 근거라 [사실]→[추정]·벤더 해설로 강등(f3). 45행 실외이동로봇 행 '절차·기준은 고시 제2023-211호(2023-11-17)가 정한다'→ 제2023-211호를 제2025-021호가 2025-11-24 개정·시행(f14), 심사항목 구판 16·현행 8(f17·f18). R15.08-3 행 추가(f4 [추정], 발행 사실은 기존 내용 확인 — safety/index.md 53행, 재추가 아님). ISO/DIS 3691-4 제3판 40.60(2026-09-10) 행(f5) — ref-789 제목을 'ISO/DIS 3691-4 (제3판)'으로 갱신. KS 부합판 ISO 10218-1/-2:2011 IDT(f6·f7). EU 기계 규정 부속서 III 1.2.1(f) 5년 추적 기록(f8: 영역 52 의 IES 해설 기반 문장 2026-09-30-area52-s3.md 43행을 1차 원문으로 보강)과 자체 진화 제어 1년 보존(f9). UL 3100 판·범위(f10·f11), UL 3300 Tally 인증은 벤더 주장(f12 [추정]). 자율안전확인 대상 정의(f23). rosbag2 0.35.0 repeat-transient-local·스냅샷·유실 통계(f39~f41, 기능 일반은 ref-831 기존 내용), MCAP publish_time 대체 규칙·CRC 0(f42·f43, log_time/publish_time 구분 자체는 design-and-simulation/index.md 100행 기존 내용); 의견 f44·f46 기존 내용 확인(새로 넣지 않음): EU 기계 규정 일반 적용일 2027-01-20(2026-09-25-area26-s7.md 55행, 2026-09-30-area52-s3.md 43행), 제54조 (b) 제50조(1) 2026-10-20(safety-and-risk-management.md 142행, 2026-10-11 게시), R15.08-3 발행일(safety/index.md 53행) / 섹션 8(분리 2026-09-30-area50-s8) — Sanders 외 항목(42행)에 기간(f24)·연방 관할 한정(f25)·서술 단어 수 중앙값 36(f26). Suresh 외 2026 AJIM 69(5):345–357 추가(f27·f28: 85% 는 초록 수치, n=917·발생률 미산출 서술은 미확인이라 쓰지 않음). Webb 외 항목(41행)에 2020-11 Zoom 22회(f33)와 정지 이미지 한계(f34); 의견 f47 / 섹션 9 — 업종별 조건 행: 실외 인증의 관제장치 요구(실시간 상태·원격 정지, f21)와 인증 정보의 관제장치 모델 단위(f22)를 인증 상태 등록 근거로; 의견 f45 / 섹션 11(분리 2026-09-30-area50-s11) — 해결 제안: oq-230(구판 16·현행 8 이 모두 항목 단위이며 세부 목록 확인, f17·f18·f19), oq-384(ISO/DIS 3691-4 제3판 40.60, f5). 부분 답: oq-186(시점·근거 고시 f13·f14, 경사로→동적 특성, 알림음·등화장치는 새 별표에 없음 f19; 다른 규정 이동 여부가 남아 열린 채 둠), oq-251·oq-123(KS 는 여전히 2011 IDT, f6·f7), oq-252(f8·f9·f35~f43), oq-333(관제장치 항목에 기록 보관 요구 문구 없음, f21), oq-187(관련 근거 f22). 답하지 못함: oq-170, oq-253, oq-254, oq-265. 메모의 '새 질문' 4건은 문구 대조로 기존 oq-251~oq-254 와 같아 새로 만들지 않음. 메모의 '새로 생긴 열린 질문' 중 '별표 구·신 대응표'는 f19 로 대부분 답해져 만들지 않고 남은 부분은 oq-186 에 둠; EBB·스냅샷 검증·MCAP 증거 표시 3건과 제2023-211호 시행일 출처 충돌, 2023/1230 조화 게재 시점 질문을 새로 올림 / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/topics/2026/2026-09-26-area25-s7.md 45행 'KS B ISO 10218-2 … 2017 확인' → 2022-10-12 확인(f7)과 ref-814 제목, docs/categories/safety/index.md 177행(IBF 단독 근거 [사실]·'산업통상자원부 고시(2023-11-17)로 정해졌다')을 f1·f2·f14 로 정리, 2026-09-30-area52-s3.md 43행에 f8 1차 근거 연결. 다음 실행 후보: 66. 실외(f17~f22), 59. 법·규제·보험·라이선스(f2·f8·f9·f14), 37. 관제 화면·실행 기록(f21·f39~f43) |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 윤리적 블랙박스 초안의 날짜·시각·체크섬 표기 충돌을 해소한 후속 판이 있는가, 서로 다른 제조사의 로봇 결정 코드를 공통 사건 유형으로 옮기는 공개 매핑이 있는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 37. 관제 화면·실행 기록 | 근거: f35 | 종류: 일반
- rosbag2 스냅샷·repeat-transient-local·유실 통계를 쓴 사고 전후 기록을 현장 설정(스냅샷 트리거 지연, 전원 상실, 정적 토픽 depth, 유실 이벤트 누락)에서 시험해 보존 길이와 누락을 검증한 사례가 있는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 43. 데이터·관측성·배포 | 근거: f40 | 종류: 일반
- MCAP 의 publish_time 이 log_time 으로 대체된 경우와 원본 추출·해시·서명 이력을 사고 증거 묶음에 어떻게 표시하고 검증할 것인가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 38. 모니터링·이상 탐지·원인 분석 | 근거: f42 | 종류: 일반
- 출처 충돌: 실외이동로봇 운행안전인증 고시 제2023-211호의 시행일은 원 고시 첨부 부칙(2023-11-17)과 제2025-021호 첨부 본문에 실린 구 부칙(2023-11-21) 가운데 어느 쪽인가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 66. 실외 | 근거: f15 | 종류: 출처 충돌
- EN ISO 10218-1/-2:2025 참조는 기계 규정 (EU) 2023/1230 의 조화 표준으로 언제 게재되며, 지침 2006/42/EC 기반 목록(시행결정 2023/1586)이 2027-01-20 폐지된 뒤 적합성 추정은 어떻게 이어지는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 59. 법·규제·보험·라이선스 | 근거: f2 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- oq-230
- oq-384

## 자체 점검

- 출처 수: 23 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 11건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-06/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f4: A3 R15.08-3 판매 페이지 재열람 실패(Cloudflare) — 발행일은 기존 ref-1255(2026-10-09 열람) 기준이라 [추정]
    - f15: 고시 제2023-211호 시행일 — 원 고시 첨부 HWP 부칙 '2023년 11월 17일부터 시행'과 제2025-021호 첨부 본문의 구 부칙 '2023년 11월 21일부터 시행'이 충돌. 독립 검증 보고(2023-11-21)와도 달라 확정하지 않음
    - f19: 2023-211 별표 3 의 알림음·등화장치·물리적 보안과 통신장애 대응(운행계획서 시나리오)이 세부운영지침 등 다른 규정으로 옮겨졌는지 미확인
    - f13: 메모가 든 kmcc.go.kr 로드맵 파일(인쇄 p.50)은 열지 못해 같은 날 정부 보도참고(fsc.go.kr, ref-1504)로 출처를 바꾸고 쪽 번호를 삭제
    - f27·f28: Suresh 외는 CDC Stacks 초록·Crossref 서지만 확인(본문 PDF 열람 실패). 메모의 'n = 917(85.2%)'·'발생률 미산출(§4.1)'은 미확인이라 쓰지 않음
    - 메모 F19(OSHA SIR 대시보드는 업무상 사망 제외)는 osha.gov 403 으로 확인하지 못해 넣지 않음(연방 관할 한정은 Sanders 원고로 f25)
    - f10·f11: UL 3100 은 공식 목록의 판·범위만 확인, 2026 개정 조항 전체·시험 수치 미확인. f12: Tally UL 3300 인증서·시험보고서 미확인(벤더 주장)
    - f3: ISO 10218:2025 원문 미열람이라 IBF 해설의 PL d·범주 3·정상 정지 서술이 틀렸다고 판단한 것이 아니라 근거 수준만 낮춤
    - f39~f43: rosbag2 0.35.0 태그 대상 커밋 날짜와 MCAP 고정 커밋(f7069e6) 날짜는 확인하지 못해 published null. 현장 무유실 성능은 시험하지 않음
    - f6·f7: KS 목록에서 ISO 10218:2025 부합 KS 를 찾지 못했으나 후속 고시 전수 부재를 증명한 것은 아님(oq-251 부분 답)
    - oq-170(ISO 3691-4:2023 원문 플릿 정보 요구), oq-253(국내 고정형·이동형 분리 재해 통계), oq-254(ISO/FDIS 13482 플릿 요구), oq-265(R15.08-3 사용자 의무)는 이번 메모가 답하지 못함
    - 메모가 2026-10-11 기준 위키 진단에 쓴 고정 커밋과 배포 페이지의 동일성, 오뚜기·고성 사고의 공식 최종 원인, 국내 실외운행인증 최신 누계는 확인하지 못함
- 범위 경계 위반 의심:
    - f8·f9·f2: EU 기계 규정·조화 표준의 법적 효력 해석은 59. 법·규제·보험·라이선스 쪽 내용이므로 조문 확인까지만 하고 개별 제품의 적용 여부는 판단하지 않음
    - f39~f43: rosbag2·MCAP 기록 기능은 37. 관제 화면·실행 기록, 43. 데이터·관측성·배포와 겹치며, 이 영역에는 사고 조사 증거 보존 관점으로만 씀
    - f17~f22: 실외이동로봇 인증 기준은 66. 실외와 겹치며, 이 영역에는 인증 근거·항목 변화와 ROP 가 받는 관제장치 요구로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 11건/15(ref-1496~ref-1506, 예약 구간 ref-1496~ref-1525 안), 재사용 12건(ref-1255·ref-789·ref-211·ref-555·ref-1122·ref-1120·ref-1121·ref-831·ref-1096·ref-1118·ref-1116·ref-980). 출처 매핑(검증 결과 기준): 메모 n1→ref-1496, n2→ref-1255(미열람), n3→ref-1497, n4→ref-211(standard.go.kr 상세로 열람; ref-814 는 '2017 확인' 제목이라 쓰지 않음), n5→ref-789(제목 ISO/DIS 3691-4 (제3판)으로 갱신), n6→ref-555(2026-07-27 통합본), n7→ref-1498, n8→ref-1499(벤더 문서), n9→ref-1500, n10→ref-1122(White Rose 원고), n11→ref-1501(초록만), n12(OSHA SIR 페이지)는 403 이라 출처에서 뺌, n13→ref-1502, n14→ref-1503(ICRES 게재본, DOI 10.13180/icres.2022.18-19.07.019; arXiv 판 ref-1120 은 미재열람), n15→ref-1121, n16→ref-831(0.35.0 태그 raw), n17→ref-1096(고정 커밋 raw), n18→ref-1504(kmcc.go.kr 대신 fsc.go.kr 보도참고 85753), n19→ref-1505(첨부 본문·별표 3 열람), n20→ref-1506. 추가 재사용: ref-1118(2023-211 첨부 HWP 별표 3·부칙), ref-1116(강등 대상 해설, 미재열람), ref-980(진흥원 8개 항목 재열람). fetched: false 는 ref-1255·ref-1120·ref-1116. 교차 확인 0건(모든 사실 finding 이 단일 출처이거나 같은 기관 계열: 고시·진흥원·로드맵은 정부 계열, EBB·Webb 은 RoboTIPS 계열) — 신뢰도 medium 이하. 중복 제거: 메모 F07(일반 적용일)·F08(제50조(1) 2026-10-20, 2026-10-11 게시된 safety-and-risk-management.md 142행)·F03(R15.08-3 발행일)은 기존 위키에 있어 rationale 에 위치만 적고 F03 만 7절 행 근거로 [추정] f4 에 남김. 메모 F19·F22 는 확인 불가로 넣지 않음. 검증 반영: F13 출처 교체·쪽 번호 삭제, F15 시행일 2025-11-24·고시 번호 제2025-021호, 별표 3 원문(구 16·신 8)으로 W19·W82 정정, F02 에 2023/1586 2027-01-20 폐지 보완, W78 강등(f3), F04 로 oq-384 해소·ref-789 제목 갱신, F17 행 번호 137–138, F23 원인 2개·장소, F25 '2016'=강의 학기, F37 should 강도, F21 은 초록 85% 만, X01 벤더 주장 [추정]. 검증 보고와 다르게 둔 것: 제2023-211호 시행일(검증 보고 2023-11-21)은 원 고시 첨부 부칙(2023-11-17)과 충돌해 f15 [추정]과 출처 충돌 질문으로 남김. 열린 질문: 해결 제안 oq-230·oq-384, 부분 답 oq-186·oq-251·oq-123·oq-252·oq-333·oq-187. 메모의 새 질문 4건은 기존 oq-251~oq-254 와 같아 새로 만들지 않음. 새 질문 5건. 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·쪽·조와 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
```

### runs/2026-09-30-24/research.md

```markdown
# 리서치 브리프 2026-09-30-24

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-24 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 60. 노동·수용성·접근성 |
| 대분류 | P. 거버넌스·법규·사회 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 기술 수용 모델(UTAUT·Almere 모델), 노사협의·공동결정, 근로자 감시 설비, 무인정보단말기 접근성, 연석 경사로 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고(부상·감시 우려), 병원(작업 흐름 적합성·종사자·환자 만족도), 실외(휠체어 이용자와 보도 로봇) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 수용성 측정 모델, 참여 설계(co-design), 직무 설계, 노동자 참여 절차 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO/IEC Guide 71, 장애인차별금지법 무인정보단말기 의무, 근로자참여법 제20조, 독일 사업장조직법 제87조 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — 로봇의 고용·임금 효과(미국·한국), 창고 로봇과 부상, 병원 로봇 민족지 연구 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-146, oq-188, oq-266 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? [분류원문]
2. 로봇 도입은 고용·임금과 일하는 방식(작업 속도·부상·직무 내용)을 어떻게 바꾸는가(미국·한국 실증 연구, 물류창고 부상 자료)? (섹션 3·5·8 겨냥)
3. 일하는 사람과 이용하는 사람의 로봇 수용성은 어떤 모델로 측정하고, 어떤 요인(작업 흐름 적합성, 감시·데이터, 사회적 상호작용)이 좌우하는가(병원·돌봄·물류창고 사례)? (섹션 4·5·6 겨냥)
4. 고령자·장애인·어린이가 로봇 서비스를 안전하게 쓰고 피할 수 있게 하는 표준·법 의무(ISO/IEC Guide 71, 장애인차별금지법 무인정보단말기 접근성)는 무엇인가? (섹션 7 겨냥, 한국 자료 우선)
5. 보도 로봇이 휠체어 이용자 등 보행 약자의 통행을 막지 않게 하는 설계·운영 기준이나 사례가 있는가? (섹션 5·6 겨냥, oq-188 관련)
6. 로봇 도입과 작업자 데이터 수집에 노동자 참여·협의를 요구하는 법 절차(한국 근로자참여법, 독일 사업장조직법)는 무엇인가? (섹션 6·7 겨냥, oq-266 관련)
7. 노동·수용성·접근성에서 ROP가 직접 맡을 것과 사용자·노사·제조사·법무에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | EU-OSHA(유럽 산업안전보건청)는 2022-06-16 보고서 'Advanced robotics and automation: implications for occupational safety and health'에서 사람과 협업할 수 있는 로봇 시스템의 확산이 노동자의 안전·건강·웰빙과 고용 조건에 주는 영향을 다뤘다. | ref-1277 | 아니오 | medium | 2022-06-16 | — | — |
| f2 | [추정] | EU-OSHA 게시 페이지 요약은 첨단 로봇의 심리사회적 위험으로 고용 불안, 작업 강도 증가, 의사결정 자율성 감소, 탈숙련, 로봇에 대한 신뢰 문제를 들고, 도입 결정에 노동자 참여·인간 중심 설계·교육을 권고하는 것으로 보인다. | ref-1277 | 아니오 | low | 2022-06-16 | 예외·성과 | — |
| f3 | [사실] | 물류창고 사례(미국 아마존 풀필먼트 센터): Burtch·Greenwood·Ravindran(ILR Review, 2025)은 로봇 풀필먼트 센터에서 기존 센터보다 중대 부상이 40% 줄고 비중대 부상이 77% 늘었다고 보고했고, 작업자 온라인 게시글에서는 로봇 센터의 피킹 목표량이 2~3배 높다는 진술이 나왔다. | ref-1264 | 아니오 | medium | 2025-08-26 | 물류창고 / 예외·성과 | — |
| f4 | [의견] | 같은 연구진은 창고 자동화가 위험 작업을 없애는 대신 남은 작업의 다양성을 줄이고 작업 속도를 높여 반복성 긴장 손상 같은 비중대 부상을 늘리므로, 위험이 사라지기보다 재분배되며 직무 설계로 대응해야 한다고 해석한다. | ref-1264 | 아니오 | medium | 2025-08-26 | 물류창고 / 제약 | — |
| f5 | [사실] | 물류창고 사례: Malik·Brandão·Coopamootoo(International Journal of Social Robotics, 2026)는 창고 작업자 12명 반구조화 면담에서 로봇 운영에 딸린 데이터 감시에 대한 우려와 더 주체적인 협업에 대한 요구를 확인하고, 수동 무시(override)·개인정보 통제·감시 활동 알림 같은 작업자 중심 요구를 제시했다. | ref-1278 | 아니오 | medium | 2026 | 물류창고 / 제약 | — |
| f6 | [사실] | Acemoglu·Restrepo(NBER 작업논문 w23285, 2017-03; Journal of Political Economy 2020 게재)는 1990~2007년 미국 통근권역 자료로 노동자 1천 명당 로봇 1대가 늘면 고용률이 약 0.18~0.34%p, 임금이 0.25~0.5% 낮아진다고 추정했다. | ref-1275 | 아니오 | medium | 2017-03 | — | — |
| f7 | [사실] | 한국노동연구원 보고서 '기술 혁신과 노동시장 변화'(2024-12)를 전한 보도에 따르면, 노동자 1천 명당 로봇 6.6대 증가(로봇 노출도 한 단계)마다 고숙련 제조업 노동자의 임금은 2.5%, 고용률은 0.55%p 올랐으나 저숙련 제조업 노동자 임금은 4.5~4.9% 줄었고 45~54세 고용률은 0.37%p 낮아졌다. | ref-1266, ref-1267 | 아니오 | low | 2025-04-01 | — | — |
| f8 | [사실] | 병원 사례(미국): Mutlu·Forlizzi(HRI 2008)의 자율 배송 로봇 TUG 민족지 연구에서 내과 병동은 방해에 대한 낮은 허용도, 인식된 비용과 이득의 불일치, 붐비는 통로의 운행 중단 때문에 로봇이 작업 흐름을 해치고 직원 저항을 불렀지만 산후 병동은 로봇을 작업 흐름과 사회적 맥락에 통합했다. | ref-1151 | 아니오 | medium | 2008 | 병원 / 예외·성과 | — |
| f9 | [사실] | 병원 사례(한국): 한림대성심병원은 2022-08~2024-12 의료서비스로봇 11종 77대를 도입해 51,092건을 사용했고, 2023년 하반기 간호사 109명 조사에서 90% 이상이 단순업무 경감, 94%가 계속 사용을 희망했으며, 입원환자 147명 중 93.9%가 영상 안내가 도움이 됐고 99%가 로봇에 거부감이 없다고 답했다고 보도됐다. | ref-1274 | 아니오 | low | 2025-01-21 | 병원 / 예외·성과 | — |
| f10 | [사실] | Heerink 외(International Journal of Social Robotics 2(4), 2010)의 Almere 모델은 통합 기술 수용 이론(UTAUT)에 사회적 상호작용 변수를 더해 고령자의 보조 소셜 에이전트 수용성을 설명하며, 요양시설과 가정에서 세 가지 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다. | ref-1269 | 아니오 | medium | 2010 | — | — |
| f11 | [사실] | 김소라(주관성 연구 63, 2023)는 Q방법론으로 노인 이용자·가족·돌봄서비스 종사자의 돌봄로봇 인식을 '불가피한 대체재', '상호보완적 동반자', '열등한 보조재', '불완전한 경쟁자'의 네 유형으로 나눴다. | ref-1273 | 아니오 | medium | 2023 | — | — |
| f12 | [사실] | 실외 사례(미국): Han 외(CHI 2024)는 이동장애인 15명과 로봇 실무자 8명 면담, 4회의 공동설계 워크숍으로 보도 로봇이 들어오면 이동장애인이 보도 공간을 두고 경쟁한다고 느끼고, 실무자는 기업이 문제가 생긴 뒤에야 접근성을 다룬다고 인정했으며, 두 집단 모두 처음부터 접근성을 통합해야 한다고 보았음을 보고했다. | ref-1265 | 아니오 | medium | 2024-04-07 | 실외 / 제약 | — |
| f13 | [사실] | 같은 연구가 출발점으로 삼은 사례에서 배송 로봇이 연석 경사로에 멈춰 휠체어 이용자의 횡단 후 통행을 막았고 이용자가 이를 공개하자 업체가 로봇 운행을 잠시 중단했으며, 참여자들은 연석 경사로로 다가오는 사람을 감지하면 로봇이 자동으로 경로를 다시 계획하고 스스로 비켜 주차하는 기능을 제안했다. | ref-1265 | 아니오 | medium | 2024-04-07 | 실외 / 예외·성과 | — |
| f14 | [사실] | ISO/IEC Guide 71:2014(2판, 2014-12)는 사람이 쓰는 제품·서비스·건축 환경을 다루는 표준에 접근성 요구를 넣도록 표준 개발자에게 지침을 주며 장애인·어린이·고령자의 접근성 요구를 주로 다룬다. | ref-1276 | 아니오 | medium | 2014-12 | 제약 | 원문 미열람 |
| f15 | [사실] | 한국에서는 2026-01-28부터 무인정보단말기를 설치·운영하는 모든 사업자가 디지털 접근성 지침의 검증 기준을 충족하는 장애인 접근 가능 기기를 제공해야 하며, 바닥면적 50㎡ 미만 시설·소상공인·테이블 주문형 기기는 보조기기·보조 인력·호출벨 등으로 대신할 수 있고, 위반은 장애인 차별에 해당한다. | ref-1268 | 아니오 | medium | 2026-01-28 | 제약 | — |
| f16 | [사실] | 한국 근로자참여 및 협력증진에 관한 법률 제20조 제1항은 노사협의회가 협의할 사항으로 근로자의 채용·배치 및 교육훈련(제2호), 신기계·기술의 도입 또는 작업 공정의 개선(제9호), 사업장 내 근로자 감시 설비의 설치(제14호)를 둔다. | ref-1272 | 아니오 | medium | 2019-07-17 | 시작 조건 | — |
| f17 | [사실] | 독일 사업장조직법(BetrVG) 제87조 제1항 제6호는 법률·단체협약 규정이 없는 한 노동자의 행동이나 성과를 감시하도록 정해진 기술 장치의 도입과 적용에 사업장협의회의 공동결정권을 두고, 합의가 안 되면 중재위원회(Einigungsstelle)가 결정한다. | ref-1271 | 아니오 | medium | 2026-09-30 | 시작 조건 | — |
| f18 | [추정] | f5·f16·f17을 종합하면 로봇 작업과 연결해 개별 작업자의 처리량·위치·행동 데이터를 남기는 오케스트레이션 기능은 한국에서는 노사협의회 협의 사항(신기계 도입, 근로자 감시 설비), 독일에서는 공동결정 대상 감시 장치로 다뤄질 수 있어 도입 전에 노동자 참여 절차가 필요할 가능성이 있으나, 해당 여부는 법적 판단으로 확인하지 못했다. | ref-1278, ref-1272, ref-1271 | 아니오 | low | 2026-09-30 | 제약 | — |
| f19 | [추정] | 확인한 자료를 종합하면 핵심 질문(로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가)의 답은 한 가지가 아니며, 일하는 사람 쪽은 작업 흐름 적합성(f8)·작업 속도와 직무 설계(f3·f4)·데이터 감시(f5)·고용과 숙련 효과(f6·f7)가, 이용하는 사람 쪽은 사회적 상호작용 요인(f10·f11)과 보행 약자의 공간·접근성(f12·f13·f15)이 수용 여부를 가르는 것으로 보이고, 기관 자체 설문은 높은 만족도를 보고한다(f9). | ref-1151, ref-1264, ref-1278, ref-1275, ref-1266, ref-1269, ref-1273, ref-1265, ref-1268, ref-1274 | 아니오 | low | 2026-09-30 | — | — |
| f20 | [추정] | 확인한 자료를 종합하면 60. 노동·수용성·접근성에서 ROP가 직접 맡을 범위는 로봇과 사람의 작업 분담·작업 속도(목표량) 설정을 드러내고 조정할 수 있게 하는 것, 작업자 데이터 수집 범위 표시·감시 알림·수동 무시 같은 작업자 통제 수단을 제공하는 것, 연석 경사로·통로에서 보행 약자에게 양보하고 멈추지 않는 대기 위치 규칙을 경로·작업 제약으로 반영하는 것, 운영자·이용자 화면의 접근성을 갖추는 것으로 보인다. | ref-1264, ref-1278, ref-1265, ref-1268 | 아니오 | low | 2026-09-30 | 제약 | — |
| f21 | [추정] | 연계 대상: 분류 원문 19장 기준으로 고용·임금·재교육 정책, 노사협의·공동결정 절차와 근로자 감시 설비의 적법성 판단(사업주·노동자 대표·법무), 장애인차별금지법 등 접근성 법적 적합성 판단(운영자·법무), 로봇 본체의 물리적 접근성 설계(높이·음성 조작 등 제조사)는 외부가 맡고, ROP는 그 결정을 작업·경로·권한 제약과 화면 설계로 받아 반영하고 근거 기록을 제공하는 쪽인 것으로 보인다. | ref-1272, ref-1271, ref-1268, ref-1265, ref-1266 | 아니오 | low | 2026-09-30 | 수행 자원 | — |
| f22 | [추정] | 이 영역은 작업 분담·속도의 31. 사람–로봇 협업과 25. 작업 배정 — MRTA(f3·f4), 부상의 49. 사람 근접 안전(f3), 작업자 데이터 감시의 53. 개인정보·영상 데이터(f5·f18), 보행 약자와 대기 위치의 19. 사람·보행자 모델과 16. 장소 의미·지도 관리(f12·f13), 목표량 지표의 39. 운영 성과 측정·개선(f3), 교육·도입 절차의 56. 운영 이관·확대·교육(f2·f8), 화면 접근성의 37. 관제 화면·실행 기록과 13. 대화형 기능의 신뢰·기반(f15), 법 의무의 59. 법·규제·보험·라이선스(f15·f16·f17), 효과 추정의 3. 경제성·조달·사업 모델(f6·f7), 적용 현장인 61. 물류창고·63. 병원·의료·66. 실외(f3·f5·f8·f9·f12)와 이어진다. | ref-1264, ref-1278, ref-1265, ref-1277, ref-1151, ref-1268, ref-1272, ref-1271, ref-1275, ref-1266, ref-1274 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1264 | George Mason University Costello College of Business | Warehouse automation hasn't made workers safer — it's just reshuffled risk | 2025-08-26 | 정부·연구기관 | medium | 2026-09-30 | https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk | 아니오 |
| ref-1265 | Han, H. Z. 외 (Carnegie Mellon University) — CHI '24 | Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations | 2024-04-07 | 논문 | high | 2026-09-30 | https://arxiv.org/abs/2404.05050 | 아니오 |
| ref-1266 | 한국경제 | 로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인) | 2025-04-01 | 기사 | low | 2026-09-30 | https://www.hankyung.com/article/2025040138391 | 아니오 |
| ref-1267 | 한국노동연구원 (국회 정책정보 포털 NABIS 게재) | 기술 혁신과 노동시장 변화 | 2024-12 | 정부·연구기관 | medium | 2026-09-30 | https://www.nabis.go.kr/issuReportDetailView.do?menucd=130&gbnCode=P52&refCode=10&poIdx=16861 | 아니오 |
| ref-1268 | 대한민국 정책브리핑 (보건복지부) | 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행 | 2026-01-28 | 정부·연구기관 | high | 2026-09-30 | https://www.korea.kr/news/policyNewsView.do?newsId=148958690 | 아니오 |
| ref-1269 | Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics) | Assessing acceptance of assistive social agent technology by older adults: the Almere model | 2010 | 논문 | medium | 2026-09-30 | https://doi.org/10.1007/s12369-010-0068-5 | 아니오 |
| ref-1151 | Mutlu, B., Forlizzi, J. (HRI 2008) | Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction | 2008 | 논문 | medium | 2026-09-30 | https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf | 아니오 |
| ref-1271 | Bundesministerium der Justiz (gesetze-im-internet.de) | Betriebsverfassungsgesetz § 87 Mitbestimmungsrechte | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.gesetze-im-internet.de/betrvg/__87.html | 아니오 |
| ref-1272 | 대한민국 국회 (법률 제16320호, 케이스노트 게재) | 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) | 2019-04-16 | 정부·연구기관 | medium | 2026-09-30 | https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0 | 아니오 |
| ref-1273 | 김소라 (주관성 연구, 한국주관성연구학회) | 돌봄로봇에 대한 돌봄서비스 종사자와 사용자의 인식 유형 연구 | 2023 | 논문 | medium | 2026-09-30 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002970146 | 아니오 |
| ref-1274 | 의협신문 | "로봇이 병원을 돌아다닌다"…의료서비스로봇 5만건 돌파 | 2025-01-21 | 기사 | low | 2026-09-30 | https://www.doctorsnews.co.kr/news/articleView.html?idxno=158208 | 아니오 |
| ref-1275 | Acemoglu, D., Restrepo, P. (NBER) | Robots and Jobs: Evidence from US Labor Markets | 2017-03 | 논문 | medium | 2026-09-30 | https://www.nber.org/papers/w23285 | 아니오 |
| ref-1276 | ISO/IEC | ISO/IEC Guide 71:2014 Guide for addressing accessibility in standards | 2014-12 | 표준 | medium | 2026-09-30 | https://www.iso.org/standard/57385.html | 예 |
| ref-1277 | European Agency for Safety and Health at Work (EU-OSHA) | Advanced robotics and automation: implications for occupational safety and health | 2022-06-16 | 정부·연구기관 | medium | 2026-09-30 | https://osha.europa.eu/en/publications/advanced-robotics-and-automation-implications-occupational-safety-and-health | 아니오 |
| ref-1278 | Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics) | Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety | 2026 | 논문 | medium | 2026-09-30 | https://doi.org/10.1007/s12369-026-01359-1 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f19(핵심 질문 답, 추정), f3·f4(위험 재분배), f6·f7(고용·임금 효과), f12(보행 약자 공간 경쟁) / 섹션 4: 기술 수용 모델 UTAUT·Almere 모델 f10, 돌봄로봇 인식 유형 f11, 노사협의 협의 사항·근로자 감시 설비 f16, 공동결정 f17, 무인정보단말기 접근성 f15, 연석 경사로 f13, 접근성 대상 집단 f14 / 섹션 5: 물류창고 — f3(예외·성과), f4·f5(제약), 병원 — f8(예외·성과, 미국), f9(예외·성과, 한국), 실외 — f12(제약)·f13(예외·성과). 제조 공장·상업 시설·가정 사례는 찾지 못했음을 명시(f7 은 현장 사례가 아니라 산업 통계) / 섹션 6: 수용성 측정 모델 f10·f11, 참여 설계 f12·f13, 직무 설계 f4, 노동자 참여 절차 f2·f16·f17·f18 / 섹션 7: ISO/IEC Guide 71 f14(원문 미열람), 장애인차별금지법 무인정보단말기 의무 f15, 근로자참여법 제20조 f16, 독일 사업장조직법 제87조 f17 / 섹션 8: f1·f3·f6·f7·f8·f10·f12 / 섹션 9: f20(직접 범위), f21(연계 대상) / 섹션 10: f22 — 3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66 / 섹션 11: 기존 oq-146·oq-188·oq-266(모두 미해결 유지; oq-188 은 f13 이 해외 사례만 제공, oq-266 은 f8 이 병동 단위 차이만 제공)과 open_questions_new 4건. 다음 실행 후보: 61. 물류창고 페이지에 f3·f5, 66. 실외 페이지에 f12·f13, 63. 병원·의료 페이지에 f8·f9 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 통합 기술 수용 이론 | Unified Theory of Acceptance and Use of Technology (UTAUT) | 성과 기대·노력 기대·사회적 영향·촉진 조건으로 기술 사용 의도와 실제 사용을 설명하는 기술 수용 모델로, 로봇 수용성 연구의 출발점으로 널리 쓰인다. |
| 알메러 모델 | Almere Model | UTAUT 에 사회적 존재감·신뢰 같은 사회적 상호작용 변수를 더해 고령자의 보조 소셜 로봇·에이전트 수용성을 측정하도록 만든 모델이다(Heerink 외, 2010). |
| 무인정보단말기 접근성 | Kiosk Accessibility (Unmanned Information Terminal Accessibility) | 키오스크 같은 무인정보단말기를 시각·이동 등 장애가 있는 사람도 동등하게 쓸 수 있게 하는 요건으로, 한국은 장애인차별금지법에 따라 2026-01-28부터 모든 설치 사업자에게 의무화했다. |
| 연석 경사로 | Curb Cut (Curb Ramp) | 보도와 차도 사이 턱을 경사로로 낮춘 부분으로, 휠체어·유모차 이용자가 횡단할 때 반드시 지나야 하므로 로봇이 이곳에 멈추면 통행을 막는다. |

## 열린 질문

새로 생긴 질문:

- 서비스 로봇 본체에 달린 터치스크린·주문 화면이나 운영자·이용자용 채팅 화면이 장애인차별금지법상 무인정보단말기에 해당해 접근성 의무를 지는가? | 관련 영역: 60. 노동·수용성·접근성, 59. 법·규제·보험·라이선스, 64. 상업 시설 | 근거: f15 | 종류: 일반
- 오케스트레이션 플랫폼이 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록하는 기능이 근로자참여법 제20조의 근로자 감시 설비나 독일 사업장조직법 제87조의 감시 장치에 해당해 도입 전 노사협의·공동결정 대상이 되는가? | 관련 영역: 60. 노동·수용성·접근성, 53. 개인정보·영상 데이터, 59. 법·규제·보험·라이선스 | 근거: f18 | 종류: 일반
- 로봇 도입 뒤 늘어난 작업 속도(피킹 목표량)와 비중대 부상 증가를 오케스트레이션의 작업 배정·속도 정책(휴식·작업 순환 반영)으로 줄인 사례나 연구가 있는가? | 관련 영역: 60. 노동·수용성·접근성, 31. 사람–로봇 협업, 25. 작업 배정 — MRTA | 근거: f3 | 종류: 일반
- 국내 병원·물류창고에서 로봇 도입 뒤 종사자 수용성과 직무 변화를 기관 자체 설문이 아닌 독립 연구로 조사한 자료가 있는가? | 관련 영역: 60. 노동·수용성·접근성, 63. 병원·의료, 61. 물류창고 | 근거: f9 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 20회 · 신규 출처 15건
- 미확인 항목:
    - f2 EU-OSHA 보고서 PDF 본문이 읽히지 않아 심리사회적 위험 목록과 권고를 원문에서 확인하지 못함(게시 페이지 요약 기준, 추정·low)
    - f3 ILR Review 논문 원문(SAGE·SSRN 403) 미열람 — 대학 뉴스 기준이며 데이터 출처(OSHA 사업장 부상 보고 2016~2020)는 검색 요약에만 있어 claim 에서 뺌
    - f6 JPE 게재본 수치(고용률 0.2%p·임금 0.42%)는 검색 요약에만 있어 NBER 작업논문 범위값으로 적음
    - f7 한국노동연구원 보고서 수치는 보도 기준이며 보고서 원문 미열람. 저자 한글 이름 미확인
    - f9 간호사 조사 표본이 보도마다 다름(109명 90% 이상 / 병동 99명 91.9%) — 두 보도가 같은 병원 발표에서 나와 독립 교차 확인 불가
    - f14 ISO/IEC Guide 71 원문·ISO 페이지 403 으로 미열람
    - f16 국가법령정보센터 본문이 열리지 않아 법령 게재 사이트로 확인
    - 시각장애인과 공원 청소 로봇 현장 연구(ACM 2026, 10.1145/3776734.3794493)는 ACM 403 과 출처 상한으로 넣지 않음
    - oq-146(국내 음성 지시 인식률)·oq-188(국내 대기 위치·점자블록 기준)·oq-266(운영 책임 조직 비교) 근거를 찾지 못함
    - 제조 공장·상업 시설·가정 현장의 노동·수용성·접근성 사례 미확인
- 범위 경계 위반 의심:
    - f6·f7: 로봇의 고용·임금 효과는 노동시장 정책 영역이므로 배경 근거로만 쓰고 ROP 직접 범위로 서술하지 않음(f21 연계 대상)
    - f16·f17·f18: 노사협의·공동결정 절차와 감시 설비 적법성 판단은 사업주·노동자 대표·법무의 몫이며 59. 법·규제·보험·라이선스와 겹치므로 규칙 목록으로만 제안
    - f15: 접근성 법 의무 적합성 판단은 운영자·법무 몫이며 로봇에 적용되는지는 열린 질문으로 보냄
    - f13: 로봇 본체의 물리적 접근성 설계(높이 조절·음성 조작)는 제조사 영역이므로 ROP 몫은 경로·대기 위치 제약으로 한정(f20·f21)
- 한계: web_fetch_available: true · fetch_mode full. 검색 20회/30, 신규 출처 15건/15(ref-1264~ref-1278, 예약 구간 안)로 신규 출처 상한에 도달해 시각장애인·공공 로봇 현장 연구, 제조 공장 사례 추가 조사를 하지 못했다. 재사용 출처 없음(참고문헌 목록 요약에 이 영역 인용 0건). 원문 열람: 15건 중 14건을 webfetch 로 열었고 ISO/IEC Guide 71(ref-1276)만 403 으로 미열람이다. 다만 ref-1269·ref-1273·ref-1278 은 초록만, ref-1151 은 PDF 일부만, ref-1277 은 게시 페이지만 읽었다. 교차 확인 0건(한림대성심병원 수치는 같은 병원 발표에서 나온 두 보도라 독립 아님). 벤더 주장 없음. 분류 원문 핵심 질문에는 f19 로 답했고 결론은 '한 가지 답은 없고, 일하는 사람 쪽은 작업 흐름 적합성·작업 속도·데이터 감시·고용 효과가, 이용하는 사람 쪽은 사회적 상호작용과 보행 약자 접근성이 수용을 가르며 기관 자체 설문은 높은 만족을 보고한다'는 추정이다. 현장 유형 사례는 물류창고(f3·f4·f5, 미국·영국계 연구), 병원(f8 미국, f9 한국), 실외(f12·f13 미국)이고 돌봄(f10·f11)은 출처가 현장 유형을 하나로 밝히지 않아 null 로 두었다. 제조 공장·상업 시설·가정 사례는 찾지 못했다. 국내 자료는 한국경제·국회 정책정보(한국노동연구원 보고서)·정책브리핑·근로자참여법·KCI 논문·의협신문이다. 기존 열린 질문 oq-146·oq-188·oq-266 은 해결하지 못했다(oq-188 은 f13 이 해외 연석 경사로 사례만, oq-266 은 f8 이 병동 단위 수용 차이만 제공). L. AI·학습 기술 관련 finding 은 없고, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. 용어집에 이미 있는 역할 모호성·자동화 편향·공공 영역 이동로봇·서비스 삼자 관계·이동형 영상정보처리기기는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```
