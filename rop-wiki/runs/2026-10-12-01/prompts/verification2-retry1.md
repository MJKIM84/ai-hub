(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-12-01
- date: 2026-10-12
- run_type: update (갱신)
- 대상: 58. 다사업자 책임·계약·데이터 (P. 거버넌스·법규·사회)
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

### runs/2026-10-12-01/target.json

```json
{
  "run_id": "2026-10-12-01",
  "date": "2026-10-12",
  "weekday": "Mon",
  "run_number": 173,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 58,
    "area_name": "58. 다사업자 책임·계약·데이터",
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
  "selection_rationale": "CLI 지정 run_type=update, area=58"
}
```

### runs/2026-10-12-01/research.json

```json
{
  "run_id": "2026-10-12-01",
  "date": "2026-10-12",
  "run_type": "update",
  "target": {
    "area_no": 58,
    "area_name": "58. 다사업자 책임·계약·데이터",
    "category": "P. 거버넌스·법규·사회"
  },
  "gaps": [
    "섹션 4. 핵심 개념과 용어(분리 2026-09-30-area58-s4) — '데이터 보유자' 항목(40행)이 '사용자 동의 없이 비개인 데이터를 이용할 수 없다'로 데이터법 제4조(13)의 '사용자와의 계약을 근거로만'과 다르고, 근거가 해설 페이지(ref-1191)뿐",
    "섹션 5. 적용 사례 — 병원 사례가 2025 공고 하나(ref-872, 각주에 '원문 미열람')에 기대며 '연 2회 평가·인증'(71행 표 '수행 자원', 76행 본문)을 원어 'bi-annual' 의 한 해석으로 단정, 2026 공고(연례·AutoveX 2026-09-01부터 2년) 미반영. 상업·물류 현장의 실제 공개 계약 문안(지원 응답·시설 장애·책임 상한) 사례 없음",
    "섹션 6. 대표 접근법과 기술(분리 2026-09-30-area58-s6) — 데이터 계약 소절(51·53행)에 '쉽게 이용 가능한 데이터' 범위·제3조(1) 설계 의무의 별도 적용일·MCT/SCC 의 제3자 면책 공백 없음. 변경 주체 책임 소절에 EU 제조물책임지침(소프트웨어 포함·실질적 변경자·업무용 재산 제외·증거 공개 비례성) 없음. 서비스 수준 소절(65행)이 ISO/IEC 19086-1(원문 미열람) 일반론뿐이라 응답·복구 시계, 시설 장애 예외, API 가용성 측정식 같은 실제 조항 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area58-s7) — 표에 EU 제조물책임지침과 RFC 9745(폐기 예고·종료 시각) 행이 없고, 데이터법 행(41행)이 일반 적용일만 적음",
    "섹션 8. 대표 연구와 자료 — 세 건뿐이며 데이터 접근 거절(영업비밀) 관할별 관행을 다룬 동료심사 연구 없음",
    "섹션 11. 열린 질문(분리 2026-09-30-area58-s11) — oq-241·oq-268·oq-279·oq-280·oq-259·oq-185 에 붙일 공개 원문 근거 없음",
    "정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: s4.md 40행 데이터 보유자 정의, 본 페이지 71·76행 '연 2회', ref-872·ref-706 의 '원문 미열람' 표시"
  ],
  "research_questions": [
    "제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까? [분류원문]",
    "EU 데이터법에서 데이터 보유자의 비개인 데이터 이용 근거와 사용자에게 제공할 데이터 범위, 설계 의무의 적용 시점은 원문상 무엇인가(oq-279·oq-320)? (섹션 4·6·7 겨냥)",
    "공개된 모델 계약 조항·표준 계약 조항과 EU 개정 제조물책임지침은 제3자 청구·소프트웨어 결함·실질적 변경·증거 공개를 다사업자 사이에서 어떻게 다루는가(oq-241·oq-289)? (섹션 6·7 겨냥)",
    "로봇 서비스·관제 플랫폼의 공개 약관은 지원 응답 시간·시설 장애 예외·책임 상한·과금 단위·가용성 측정을 어떻게 정하는가(oq-112·oq-268)? (섹션 5·6 겨냥)",
    "API 폐기 예고와 종료 시각의 관계를 정한 표준은 무엇을 정하고 무엇을 계약에 남기는가(oq-280)? (섹션 7 겨냥)",
    "통합자 사전 자격(RoMi-H 등재)의 주기·유효기간과, 영상 처리 위탁·데이터 접근 거절의 관리 기준은 공개 원문상 무엇인가(oq-149·oq-259)? (섹션 5·6·8 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "EU 데이터법(Regulation (EU) 2023/2854) 제4조(13)은 데이터 보유자가 쉽게 이용 가능한 데이터 가운데 비개인 데이터를 사용자와의 계약을 근거로만 이용할 수 있다고 정하고, 그 데이터로 사용자의 경제 상황·자산·생산 방식을 추론해 사용자의 시장 지위를 해치는 이용을 금지한다.",
      "tag": "사실",
      "source_ids": [
        "ref-636"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제4조(13): \"A data holder shall only use any readily available data that is non-personal data on the basis of a contract with the user. A data holder shall not use such data to derive insights about the economic situation, assets and production methods of, or the use by, the user …\". 정정 근거: docs/topics/2026/2026-09-30-area58-s4.md 40행 '데이터 보유자' 항목의 '사용자 동의 없이 비개인 데이터를 이용할 수 없다'[사실][^ref-1191] 는 조문의 '계약을 근거로만'과 다르다(동의가 아니라 계약). 근거도 해설 페이지(ref-1191) 대신 원문(ref-636)으로. 개인정보 처리의 법적 근거(GDPR 제6조)는 별개",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "데이터법 제4조(1)은 사용자가 연결 제품·관련 서비스에서 데이터에 직접 접근할 수 없을 때 데이터 보유자가 '쉽게 이용 가능한 데이터'와 그 해석·이용에 필요한 관련 메타데이터를 지체 없이 무료로 제공하도록 하며, 제2조(17)은 '쉽게 이용 가능한 데이터'를 데이터 보유자가 과도한 노력 없이 연결 제품·관련 서비스에서 적법하게 얻거나 얻을 수 있는 제품 데이터·관련 서비스 데이터로 정의한다.",
      "tag": "사실",
      "source_ids": [
        "ref-636"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제4조(1): \"Where data cannot be directly accessed by the user … data holders shall make readily available data, as well as the relevant metadata necessary to interpret and use those data, accessible to the user without undue delay … free of charge\". 제2조(17): \"'readily available data' means product data and related service data that a data holder lawfully obtains or can lawfully obtain … without disproportionate effort going beyond a simple operation\". 모든 데이터·추론 결과의 포괄적 소유권을 정한 조문으로 읽지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "데이터법 제50조는 이 규정을 2025-09-12부터 적용한다고 하면서, 제3조(1)의 설계 의무(연결 제품·관련 서비스를 데이터에 직접 접근 가능하게 설계·제조할 의무)는 2026-09-12 후에 시장에 출시되는 연결 제품과 관련 서비스에 적용한다고 따로 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-636"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제50조: \"It shall apply from 12 September 2025.\" / \"The obligation resulting from Article 3(1) shall apply to connected products and the services related to them placed on the market after 12 September 2026.\" 일반 적용일(2025-09-12, 기존 s6.md 51행·s7.md 41행에 있음)과 제3조(1) 적용 대상(2026-09-12 후 출시 제품)을 구분. 개별 로봇의 출시 시점 판정은 하지 않음. 관련 위키: docs/topics/2026/2026-09-25-area28-s3.md 41행 '주요 조항의 적용 개시일은 미확인'(후속 정리)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "집행위원회 권고 초안 부속서(C(2025) 7750 final ANNEX, 2025-11-19)의 클라우드 표준 계약 조항(SCC) 중 책임 조항 설명(Annex X)은 '이 SCC 는 면책(indemnification) 조항을 포함하지 않는다'고 적고, 한 당사자의 중대한 의무 위반으로 생긴 제3자 청구에 대해 면책·보호 조항이 필요한지와 그 범위를 당사자가 검토하도록 권한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1489",
        "ref-1192"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Annex X(SCC Liability), 인쇄 p.155(PDF p.156): \"Indemnification: These SCCs do not include provisions on indemnification. The Parties are encouraged to consider whether and, if so, to what extent a Party may need to indemnify … from any claims of third parties …\". 표지 \"Brussels, 19.11.2025 / C(2025) 7750 final / ANNEX\", 내부는 DRAFT. 공식 EC URL 로 열람(미러 대신). 클라우드용 비구속 초안이며 로봇 사고 책임 분담표가 아님. '자발적 사용'은 기존 내용(s6.md 53행·s7.md 42행)이라 제외",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "EU 개정 제조물책임지침(Directive (EU) 2024/2853) 제4조(1)은 '제품'에 소프트웨어를 포함하고, 제2조(2)는 상업 활동 밖에서 개발·공급된 자유·오픈소스 소프트웨어에는 지침을 적용하지 않는다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1490"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제4조(1): \"'product' means all movables … it includes electricity, digital manufacturing files, raw materials and software\". 제2조(2): \"This Directive does not apply to free and open-source software that is developed or supplied outside the course of a commercial activity.\" 기존 59영역(2026-09-30-area59-s3.md 39행·s7.md 44행)은 Gibson Dunn 해설(ref-1227) 근거라, 58영역에는 다사업자 책임 관점 핵심만 원문으로 둠. 개별 ROP 소프트웨어 적용 판정 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "같은 지침 제8조(2)는 제조자의 통제 밖에서 제품을 실질적으로 변경한 뒤 시장에 내놓거나 사용에 투입한 자연인·법인을 그 제품의 제조자로 본다.",
      "tag": "사실",
      "source_ids": [
        "ref-1490"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제8조(2): \"Any natural or legal person that substantially modifies a product outside the manufacturer's control and thereafter makes it available on the market or puts it into service shall be considered to be a manufacturer of that product for the purposes of paragraph 1.\" 기존 59영역 s4.md 43행(해설 근거)과 같은 내용을 원문으로 확인. 오케스트레이션 설정 변경이 실질적 변경인지(oq-289, oq-282)는 판단하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "지침 제2조(1)의 적용 대상은 2026-05-07 정오표(OJ L 2026/90364)로 '2026-12-09 후'에서 '2026-12-08 후(after 8 December 2026)' 시장에 출시되거나 사용에 투입된 제품으로 고쳐졌으며, 따라서 2026-12-09 당일부터 출시·투입되는 제품에 적용된다.",
      "tag": "사실",
      "source_ids": [
        "ref-1490"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "정오표(ELI http://data.europa.eu/eli/dir/2024/2853/corrigendum/2026-05-07/oj) \"On page 11, Article 2(1): for: '… after 9 December 2026.' read: '… after 8 December 2026.'\"; C1 반영 통합본 02024L2853-20241118 제2조(1) 같은 문구. 표기 주의: '2026-12-08부터'가 아니라 '2026-12-08 후' = 2026-12-09부터. 기존 59영역 '2026-12-09 이후'(s3.md 39행·s7.md 44행)는 정정 후 의미와 맞으나 근거가 해설(ref-1227)이라 원문 연결은 후속 정리",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "지침 제22조(1)은 회원국이 지침 이행 법령을 2026-12-09까지 시행하도록 정하고, 제21조는 구 제조물책임지침 85/374/EEC 를 2026-12-09 부로 폐지하되 그 전에 출시·사용 투입된 제품에는 계속 적용한다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1490"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제22조(1): \"Member States shall bring into force the laws, regulations and administrative provisions necessary to comply with this Directive by 9 December 2026.\" 통합본: \"Directive 85/374/EEC is repealed with effect from 9 December 2026. However, it shall continue to apply with regard to products placed on the market or put into service before that date.\" 공포(OJ 2024-11-18)·적용(제2조(1))·이행 기한(제22조(1))을 구분. 조사일(2026-10-12)은 이행 기한 전이며 회원국별 이행 법령은 확인하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "지침 제6조(1)(b)(iii)은 전적으로 업무 목적으로만 쓰는 재산의 손해를 이 지침의 보상 대상 손해에서 제외한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1490"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제6조(1)(b): 재산 손해 가운데 \"(iii) property used exclusively for professional purposes\" 제외. 전문 (22) 같은 취지. 계약상·국내법상 다른 구제를 배제한다는 뜻으로 해석하지 않음. 사업장 로봇·설비 손해는 이 지침보다 사업자 간 계약 조항이 다룰 몫이 크다는 추론은 의견 finding 으로 분리",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "지침 제9조(3)은 같은 조 제1·2항에 따른 증거 공개를 필요하고 비례적인 범위로 제한하도록 회원국에 요구하고, 제9조(4)는 그 판단에서 제3자를 포함한 모든 당사자의 정당한 이익, 특히 기밀·영업비밀 보호를 고려하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1490"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제9조(3): \"Member States shall ensure that the disclosure of evidence pursuant to paragraphs 1 and 2 … is limited to what is necessary and proportionate.\" (4): \"… national courts consider the legitimate interests of all parties concerned, including third parties, in particular in relation to the protection of confidential information and trade secrets …\". (5) 영업비밀 보호 조치. 법원 절차의 공개 범위이며 사업자에게 모든 로그를 상시 청구하는 권리가 아님. 증거 공개 자체는 기존 59영역 s6.md 45행에 있어 비례성·이해관계 고려만 보강",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "창이종합병원 CHART 의 2025년 RoMi-H 등재 공고는 프로그램을 'a bi-annual RoMi-H Empanelment Program'으로 적고, 같은 공고에서 등재 통합자 5개사(HOPE Technik, Medisys Innovation, Panasonic Asia Pacific, QuikBot Technologies, Techfox)의 등재가 2025-05-01부터 2년간 유효하다고 게시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-872"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "CGH 공고(2025-05-01, 'Updated as of 24 August 2026'): \"CHART organizes a bi-annual RoMi-H Empanelment Program, for which the objective is to assess / re-assess the System Integrator's ability to deploy RoMi-H\" / \"certified as Empanelled System Integrator (SI) … with effect from 1 May 2025 with a two-year validity\". 같은 공고: \"The integration via RoMi-H is to be undertaken by an empanelled System Integrator\". ref-872 는 기존 위키에 '원문 미열람'으로 표시돼 있었으나 이번에 원문 열람",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "2025년 공고의 'bi-annual'은 '연 2회'로도 '2년마다'로도 읽힐 수 있고 같은 공고가 등재 유효기간을 2년으로 적고 있어, 위키 5절의 '연 2회 평가·인증'(본문 76행, 표 '수행 자원' 행)은 원어 인용과 두 해석을 함께 적거나 [추정]으로 낮춰야 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-872",
        "ref-1495"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "독립 검증 수정(F13): 메모는 '연 2회'로 [사실] 처리했으나 원어 \"bi-annual\"은 두 뜻이 가능. 2026 공고는 \"an annual RoMi-H Empanelment Program\"이라 적어, 실제 주기는 공고마다 표현이 다르다. 다른 페이지의 같은 표현(docs/topics/2026/2026-09-30-area03-s7.md 44행, 2026-09-30-area56-s7.md 46행)은 후속 정리. 63영역 s4·s7 의 '2025-05-01부터 2년 유효'는 원문과 맞음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "SingHealth/CHART 의 2026년 RoMi-H 등재 공고(2026-05-06 게시, 2026-08-24 갱신)는 CHART 가 연례(annual) 등재 프로그램을 운영해 통합자의 RoMi-H 배치 역량을 평가·재평가한다고 적고, 등재 통합자는 CHART 웹사이트에 공개되어 공공 의료기관이 제안요청(RFP/RFI) 참여를 위해 연락할 수 있다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1495"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "SingHealth 공고 \"06 May 2026\", \"Updated as of 24 August 2026\": \"CHART organizes an annual RoMi-H Empanelment Program, for which the objective is to assess / re-assess …\" / \"Successfully empanelled SIs will be published on the CHART website and this will allow PHIs and potential collaborators to contact empanelled SIs for participation in Request For Proposal or Information (RFP/RFI).\" 2025 공고(ref-872)와 같은 기관 계열이라 독립 교차 확인 아님",
      "as_of": "2026-10-12",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f14",
      "claim": "2026년 공고의 등재 명단은 AutoveX Pte Ltd 1개사이며 등재는 2026-09-01부터 2년간 유효하다.",
      "tag": "사실",
      "source_ids": [
        "ref-1495"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"The following companies are certified as Empanelled System Integrator (SI) … with effect from 1 September 2026 with a two-year validity: AutoveX Pte Ltd\". 2025년 등재자(2025-05-01부터 2년)의 효력 변화는 공고에 없으며 자동 취소로 읽지 않음. 등재가 인수·장애 복구 책임까지 정한다는 근거는 없음",
      "as_of": "2026-10-12",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f15",
      "claim": "개인정보보호위원회는 「이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서」 발표 보도자료(2024-10-14 게시)에서 외부업체 위수탁으로 개인영상정보를 처리하는 경우 보호책임자 지정과 주기적인 점검ㆍ교육 등으로 안전하게 관리할 것을 당부했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1494"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보도자료 본문 ④: \"외부업체 위수탁을 통해 개인영상정보를 처리하는 경우에는 보호책임자 지정 및 주기적인 점검ㆍ교육 등을 통해 …\". 감독기관의 당부이며 새 법률 의무나 ROP 의 운영자·수탁자 지위 판정이 아님. 53영역 privacy-and-video-data.md 108행이 기사(ref-1136)로 같은 내용을 이미 서술 — 58영역에는 위탁 관리 점검을 계약 부속서와 잇는 짧은 연결로만 쓰고, 53영역 근거를 1차 보도자료로 바꾸는 것은 후속 정리",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "RFC 9745(2025-03, Standards Track) §5 는 자원을 폐기 예정(deprecated)으로 표시하는 행위가 자원의 동작을 바꾸지 않으며, 클라이언트는 폐기 표시 전과 같은 방식으로 자원을 계속 쓸 수 있다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-706"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§5 Resource Behavior: \"The act of deprecation does not change any behavior of the resource. … consumers can still use the resource in the same way as they did before the resource was declared deprecated.\" ref-706 은 기존 위키에서 '원문 미열람'(fetched false)이었으나 이번에 rfc-editor.org 원문 열람",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "RFC 9745 §4 는 Sunset 헤더(RFC 8594)로 자원이 응답하지 않게 될 시각을 함께 알릴 수 있게 하고, Sunset 시각이 Deprecation 시각보다 빨라서는 안 된다(MUST NOT)고 정하며, 두 시각 사이의 최소 간격은 정하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-706"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4 Sunset: \"The timestamp given in the Sunset HTTP header field MUST NOT be earlier than the one given in the Deprecation header field.\" 예시는 폐기 2023-06-30, 종료 2024-06-30. RFC 전문(§1~8)에 최소 유예 일수 규정 없음. 선후 관계 규정은 21영역 쪽 docs/topics/2026/2026-09-25-area28-s4.md 40행에 이미 있음(원문 미열람 근거) — 58영역에는 계약상 통지 기간과 구분하는 맥락으로만 씀",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "De Noyette·Stähler·Margoni(IIC 56(5):984–1014, 2025)는 데이터법의 영업비밀 체계를 분석하며, 회원국 관할 당국마다 영업비밀 관련 행정 관행이 달라져 더 파편화될 위험이 있다고 지적한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1488"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.1.4: 영업비밀 처리의 국가별 행정 관행에 대해 \"risk for further fragmentation\". 온라인 게재 2025-04-24, CC BY 4.0, DOI 10.1007/s40319-025-01601-9(Crossref 서지 확인). 동료심사 법학 논증이며 로봇 다사업자 계약의 실증·통계가 아님. 저자가 지적했다는 범위만 [사실]",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "Relay Robotics 공개 약관의 서비스 수준 부속서(Exhibit A)에 따르면 Tier 1(24시간 콜센터)은 서비스 개시일 이후 이메일 지원 요청을 받은 뒤 60분 안에 응답하도록 '상업적으로 합리적인 노력'을 기울이는 조건이며, 복구 완료 시각을 보장하는 문구는 아니다.",
      "tag": "추정",
      "source_ids": [
        "ref-1491"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Exhibit A Tier 1: \"After the In-Service Date … Relay Robotics will use commercially reasonable efforts to respond within 60 minutes of receiving the email request.\" 단일 업체의 공개 약관 문안이며 개별 체결본·이행 실적은 미확인",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f20",
      "claim": "Relay 약관의 같은 부속서 예외 조항에 따르면 고객의 네트워크나 시설(예: 승강기 고장)에서 생긴 문제는 고객이 고칠 때까지 지원 기한이 연장되고, Relay 는 고객 네트워크·시설 문제의 수리 책임을 지지 않는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1491"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Exhibit A Exclusions: \"For problems that result from an issue caused by or resulting from the Customer's network or premises (e.g., an elevator out of service), the time periods above will be extended until Customer has repaired the issue. Relay Robotics takes no responsibility for repairing or resolving Customer's issues …\". 단일 업체 사례. 시설 장애의 시작·종료를 누가 확인하는지는 약관에 없음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f21",
      "claim": "Relay 약관 §12 에 따르면 면책 의무, 고객의 라이선스 위반, 양측의 비밀유지 위반을 제외한 각 당사자의 책임은 청구 발생 전 18개월 동안 고객이 지급했거나 지급할 요금 총액을 넘지 않으며, 약관 준거법은 미국 캘리포니아주법이다.",
      "tag": "추정",
      "source_ids": [
        "ref-1491"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: §12: \"EXCEPT WITH RESPECT TO LIABILITIES ARISING OUT OF CUSTOMER'S BREACH OF THE LICENSES …, EITHER PARTY'S BREACH OF ITS CONFIDENTIALITY OBLIGATIONS HEREIN OR A PARTY'S INDEMNIFICATION OBLIGATIONS, NEITHER PARTY'S LIABILITY … WILL EXCEED THE TOTAL FEES PAID OR OWED … DURING THE 18 MONTHS BEFORE THE DATE THE CLAIM FIRST AROSE.\" §14.4 \"governed by the laws of the State of California\". 약관 표기일 'March 1st 2023'. 국내 집행 가능성은 판단하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f22",
      "claim": "Relay 약관 §5.2 에 따르면 당사자 사이에서 고객이 Relay 와 공유하기로 한 개인정보는 고객 소유이며, Relay 는 서비스 제공 목적에만 쓴다.",
      "tag": "추정",
      "source_ids": [
        "ref-1491"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: §5.2 \"As between the parties, Customer shall own all Personal Data that Customer elects to share with Relay. … Relay will use the Personal Data to provide the Services, and not for any other purpose except with Customer's prior written permission.\" 로봇이 만든 운영 데이터 전반의 법적 소유권을 정한 문구로 확대하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f23",
      "claim": "Formant 일반 약관(2026-04-16 갱신)에 따르면 고객이 지정한 통합자('Development Consultant')는 고객의 지시로만 일하며 고객이 그 통합자의 작위·부작위에 책임을 진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1496"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 정의 'Development Consultant': \"a third-party systems integrator that Customer has authorized to access, test, and customize the Products or Services. Any Development Consultant(s) … works expressly and exclusively at Customer's direction, and Customer is responsible for any acts or omissions of such Development Consultant(s).\" 정의 번호 대신 용어 이름으로 인용. 실제 체결·이행 결과는 미확인",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f24",
      "claim": "Formant 약관의 'Device' 정의에 따르면 하나의 장치에 가상 환경(PLC, Jetson, 가상 머신 등)이 둘 이상 있으면 가상 환경마다 별도 Device 로 센다.",
      "tag": "추정",
      "source_ids": [
        "ref-1496"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 정의 'Device': \"Where a Device contains more than one virtual environment (including PLCs, jetsons, virtual machines and virtual processors), each virtual environment will be counted as a separate …\". 주문서의 단가·최소 요금은 미공개라 과금 영향은 확인하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f25",
      "claim": "Formant 약관의 Formant AI 추가 조건에 따르면 고객은 AI 출력에 의존하거나 그 출력으로 명령을 실행하기 전에 출력을 검증하는 사람의 검토 절차를 사용 과정에 두어야 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1496"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Additional License Terms for Formant AI: \"Any decisions, actions, or omissions taken in reliance on or enabled by AI User Output, including where the Output is used to initiate or execute a command … Customer shall ensure that a human review process is incorporated into its use of the Products and Services to validate AI User Output prior to reliance or execution.\" 업체 약관상 조건이며 로봇 AI 일반의 법적 의무가 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f26",
      "claim": "AIRROBO(Best Epoch Technology)의 EU 데이터법 고지 §4(b)에 따르면 사용자는 앱에서 데이터를 내보내 한 번에 공유하거나, 승인된 QR 코드로 제3자와 지속 공유할 수 있으며 지속 공유를 받으려는 제3자는 Tuya 클라우드 플랫폼에 등록해야 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1487"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 고지 §4(b) p.3 \"You can export data via the App and manually share it with third parties in one go, or continuously share data with third parties through an authorized QR code. For continuous data sharing, the third party is required to access and register on https://platform.tuya.com/cloud …\". 대상은 고지에 열거된 로봇청소기(T20/T25/T30/E10)·수영장 청소 로봇(PC200/PS100). UBTech CDN 게시 PDF(작성 2025-12-23, 발행일 미확인). 실제 필드·지연·철회 동작은 시험하지 않음",
      "as_of": "2026-10-12",
      "site_type": "가정",
      "flow_item": "작업 대상",
      "vendor_claim": true
    },
    {
      "id": "f27",
      "claim": "AWS IoT RoboRunner 서비스 수준 협약(2022-11-28 갱신)에 따르면 'Error'는 500 또는 503 오류 코드를 돌려준 요청이고, 가용성은 5분 구간마다 오류 없이 처리된 요청 비율로 계산한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1492"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Definitions: \"An 'Error' is any Request that returns a 500 or 503 error code.\" / \"'Availability' is calculated for each 5-minute interval as the percentage of Requests processed by AWS IoT RoboRunner that do not fail with Errors.\" API 측정식이며 로봇 작업 성공·물리 가동을 재지 않음. 조사일 현재 RoboRunner 의 제공·지원 상태는 미확인(지원 종료 공지는 찾지 못함)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f28",
      "claim": "같은 SLA 는 요청이 하나도 없던 5분 구간을 가용성 100%로 간주한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1492"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Definitions: \"If you did not make any Requests in a given 5-minute interval, that interval is assumed to be 100% available.\" 단일 업체 사례",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f29",
      "claim": "1X Technologies 의 사전예약 약관(2025-10-28 갱신) §2.4 에 따르면 주문 초대를 받아 로봇을 받으려는 사람은 구매 시점에 제시되는 별도 판매약관(Terms of Sale)에 동의해야 하며, 취소·배송·보증 세부는 주문 초대나 판매약관에 둔다.",
      "tag": "추정",
      "source_ids": [
        "ref-1493"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: §2.4 Orders: \"you will be required to agree to the Terms of Sale (to be presented at the time of purchase …)\", \"Additional details regarding order cancellations, shipping, delivery and warranty will be set forth in the Order Invitation and/or the Terms of Sale.\" 사전예약 계약이며 원격 조작자의 영상 접근·사고 책임 조항은 이 문서에서 확인하지 못함(oq-185 미해결)",
      "as_of": "2026-10-12",
      "site_type": "가정",
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f30",
      "claim": "ROP 의 데이터 자산 대장은 데이터 항목마다 데이터법상 역할(사용자·데이터 보유자·제3자), 이용 근거(사용자와의 계약), 요청 가능 범위(쉽게 이용 가능한 데이터·메타데이터), 연결 제품의 출시일(2026-09-12 후 출시 여부)을 따로 기록하고, 개인정보 처리 근거는 별도로 심사하는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-636"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1~f3 에서 도출. 특정 ROP 의 보유자·수령자 지위(oq-279·oq-320)는 판단하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f31",
      "claim": "다사업자 계약은 클라우드 SCC 의 책임 조항을 그대로 옮기지 말고, 로봇 제조사·통합자·시설 관리주체·플랫폼 사이의 제3자 청구 면책을 따로 정해야 하며, 제조물책임지침이 업무 전용 재산 손해를 보상 대상에서 빼므로 사업장 설비·재고 손해는 계약 조항으로 다룰 필요가 커 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-1489",
        "ref-1490"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f4·f9 에서 도출. 개별 계약의 법적 효과는 59. 법·규제·보험·라이선스 쪽 판단",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f32",
      "claim": "ROP 는 사고 뒤 증거 공개가 법원 판단으로 필요·비례 범위에 한정된다는 점을 전제로, 로그 보관 기간·사고 후 동결·내보내기 형식·영업비밀 분리 절차를 계약 부속서에 미리 정해 두는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1490"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f10 에서 도출. oq-249(기계 규정 로그 의무의 플랫폼 적용)는 판단하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f33",
      "claim": "서비스 수준 부속서는 응답 시각·원인 분석·복구 완료 시각을 나누고, 시설 장애로 지원 기한이 멈추는 구간의 시작·종료와 확인 주체를 기록하며, API 오류율과 별도로 작업 성공률·지연·시설 대기 시간을 지표로 합의하는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1491",
        "ref-1492"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f19·f20·f27·f28 에서 도출. 두 업체 약관은 서로 다른 조건이라 교차 확인이 아님. oq-112·oq-268 부분 근거",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "플랫폼 약관과 고객–통합자 계약을 함께 대조해 통합자 행위의 책임 귀속, 과금 수량 단위(로봇 대수·가상 환경·설치 인스턴스)의 대응표와 계량 이의 절차, AI 출력으로 명령을 실행할 때의 검토자·승인 기록을 정하는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1496",
        "ref-1491"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f21~f25 에서 도출. 실제 주문서·단가는 미공개",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f35",
      "claim": "제조사의 데이터법 고지가 안내하는 내보내기·제3자 지속 공유 경로는 ROP 온보딩 때 제3자 등록·필드 목록·지연·승인 철회를 직접 시험해 확인하는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1487"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f26 에서 도출. 시험 결과는 없음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f36",
      "claim": "통합자 등재(사전 자격)는 연동 역량 평가일 뿐이므로, 등재 사실과 별도로 인수 기준·장애 복구 책임·등재 유효기간 만료 시 처리를 계약에 적는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-872",
        "ref-1495"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f11~f14 에서 도출. oq-149 는 국내 사례가 없어 열린 채 둠",
      "as_of": "2026-10-12",
      "site_type": "병원",
      "flow_item": "완료·인계"
    },
    {
      "id": "f37",
      "claim": "ROP 어댑터는 제조사 API 의 폐기 예고 시각·종료(Sunset) 시각·전환 문서 링크를 따로 저장하고, 두 시각 사이의 최소 통지 기간은 RFC 가 정하지 않으므로 계약에서 따로 확인하는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-706"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f16·f17 에서 도출. oq-280·oq-207 부분 근거",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f38",
      "claim": "영상 처리를 다른 사업자에게 맡길 때는 위탁 범위·보호책임자·교육·주기 점검 증빙을 계약 부속서로 관리하고, 데이터 접근 거절(영업비밀) 사유와 이의 경로는 관할별로 기록하되 법학 논문의 제안을 검증된 운영 성과로 표시하지 않는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1494",
        "ref-1488"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f15·f18 에서 도출. 개인정보 상세 설계는 53. 개인정보·영상 데이터 몫",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-636",
      "org": "European Union (EUR-Lex)",
      "title": "Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act)",
      "published": "2023-12-13",
      "url": "https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "EU 데이터법 원문(기존 출처). 이번에 제2조(17), 제4조(1)·(13), 제50조(일반 적용 2025-09-12, 제3조(1)은 2026-09-12 후 출시 제품)를 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1192",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts",
      "published": "2025-11-19",
      "url": "https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "MCT·SCC 권고 초안 발표 페이지(기존 출처). 2025-11-19 발표, 2026-03-03 갱신이며 여전히 초안(Draft) 표기다. 부속서 내려받기 링크가 이 페이지에 있다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-872",
      "org": "Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "RoMi-H Empanelment Programme 2025",
      "published": "2025-05-01",
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "2025년 RoMi-H 통합자 등재 공고(기존 출처, 이번에 원문 열람). 프로그램을 'bi-annual'로 적고 5개사 등재가 2025-05-01부터 2년 유효하다고 게시한다(2026-08-24 갱신).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-706",
      "org": "IETF (RFC Editor)",
      "title": "RFC 9745: The Deprecation HTTP Response Header Field",
      "published": "2025-03",
      "url": "https://www.rfc-editor.org/info/rfc9745/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "Deprecation HTTP 응답 헤더 규격(Standards Track, 기존 출처). 이번에 원문을 열어 §4(Sunset 시각은 Deprecation 시각보다 이르면 안 됨)와 §5(폐기 표시는 자원 동작을 바꾸지 않음)를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.rfc-editor.org/rfc/rfc9745.html",
      "source_unopened": false
    },
    {
      "id": "ref-1487",
      "org": "Best Epoch Technology Co., Ltd. (AIRROBO)",
      "title": "EU DATA ACT Notice",
      "published": null,
      "url": "https://owebsite-cdn.ubtrobot.com/resources/file/2025/12/25/755762357268549.pdf",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "로봇청소기·수영장 청소 로봇 제조사의 EU 데이터법 사전 고지 PDF. 제품 데이터 목록과 앱 내보내기·승인 QR 코드(Tuya 플랫폼 등록)를 통한 제3자 공유 경로를 안내한다. 발행일은 확인하지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1488",
      "org": "De Noyette, E., Stähler, L., Margoni, T. (IIC 56(5))",
      "title": "Data Secrets: The Data Act's New Trade Secrets Framework",
      "published": "2025-04-24",
      "url": "https://link.springer.com/article/10.1007/s40319-025-01601-9",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "데이터법의 영업비밀 체계를 분석한 동료심사 법학 논문(IIC 56(5):984–1014, CC BY 4.0). 회원국 행정 관행의 파편화 위험을 지적한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1489",
      "org": "European Commission",
      "title": "ANNEX to the Communication to the Commission — Approval of the draft Commission Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts (with Annexes), C(2025) 7750 final",
      "published": "2025-11-19",
      "url": "https://ec.europa.eu/newsroom/dae/redirection/document/121719",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "MCT·SCC 권고 초안 본문과 부속서(166쪽). 부속서 X(클라우드 SCC 책임)는 면책 조항을 두지 않고 제3자 청구 면책을 당사자가 검토하도록 권한다. 공식 EC 다운로드 URL 로 열람했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1490",
      "org": "European Union (EUR-Lex)",
      "title": "Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC",
      "published": "2024-11-18",
      "url": "https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "EU 개정 제조물책임지침 원문(2024-10-23 채택, 2024-11-18 관보). 2026-05-07 정오표(OJ L 2026/90364)로 제2조(1) 적용 대상이 '2026-12-08 후' 출시·투입 제품으로 고쳐졌다. 제2·4·6·8·9·22조를 C1 반영 통합본으로 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024L2853-20241118",
      "source_unopened": false
    },
    {
      "id": "ref-1491",
      "org": "Relay Robotics",
      "title": "Terms of Service (Exhibit A: Service Level Agreement)",
      "published": "2023-03-01",
      "url": "https://relayrobotics.com/tos",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "병원·호텔 배송 로봇 업체의 공개 서비스 약관. 지원 응답 시간, 시설 장애 시 지원 기한 연장, 18개월 요금 기준 책임 상한, 개인정보 귀속, 캘리포니아 준거법을 정한다. 단일 업체 문안이다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1492",
      "org": "Amazon Web Services",
      "title": "AWS IoT RoboRunner Service Level Agreement",
      "published": "2022-11-28",
      "url": "https://aws.amazon.com/roborunner/sla/",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "AWS IoT RoboRunner 의 공개 SLA. 500·503 응답을 오류로, 5분 구간 요청 성공률을 가용성으로 정의하고 요청 없는 구간은 100% 가용으로 본다. 조사일 현재 서비스 제공 상태는 확인하지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1493",
      "org": "1X Technologies, Inc.",
      "title": "Pre-Order Terms",
      "published": "2025-10-28",
      "url": "https://www.1x.tech/legal",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "가정용 휴머노이드 사전예약 약관. 구매 때 별도 판매약관 동의를 요구한다. 원격 조작자 운영 책임 조항은 이 문서에 없다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1494",
      "org": "개인정보보호위원회",
      "title": "자율주행 인공지능(AI) 발전을 위한 개인영상정보 보호ㆍ활용 기준 나왔다",
      "published": "2024-10-14",
      "url": "https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=10678",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "이동형 영상정보처리기기 개인영상정보 보호·활용 안내서 발표 보도자료. 외부업체 위수탁 처리 시 보호책임자 지정과 주기적 점검·교육을 당부한다. 안내서 본문(ref-1135)은 이번에 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1495",
      "org": "SingHealth / Changi General Hospital CHART",
      "title": "RoMi-H Empanelment Programme 2026",
      "published": "2026-05-06",
      "url": "https://www.singhealth.com.sg/news/robotics/romi-h-empanelment-programme-2026",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "2026년 RoMi-H 통합자 등재 공고(2026-08-24 갱신). 연례 프로그램이라 적고 AutoveX Pte Ltd 의 등재를 2026-09-01부터 2년 유효로 게시한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1496",
      "org": "Formant",
      "title": "General Terms",
      "published": "2026-04-16",
      "url": "https://www.formant.ai/terms_of_use",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "로봇 관제 플랫폼 업체의 일반 약관. 고객 지정 통합자 책임의 고객 귀속, 가상 환경별 Device 계수, Formant AI 출력의 사람 검토 요구를 정한다. 단일 업체 문안이다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "sections": [
        "4",
        "5",
        "6",
        "7",
        "8",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 4(분리 2026-09-30-area58-s4) — 40행 '데이터 보유자' 항목 정정: '사용자와 계약을 맺어야 하고 사용자 동의 없이 비개인 데이터를 이용할 수 없다'[사실][^ref-1191] → '쉽게 이용 가능한 비개인 데이터를 사용자와의 계약을 근거로만 이용할 수 있고, 사용자의 시장 지위를 해치는 추론에 쓸 수 없다'(f1, 근거 ref-636 원문). '쉽게 이용 가능한 데이터' 범위(f2)를 같은 항목이나 새 줄로 / 섹션 5 — 병원 사례: 71행 표 '수행 자원'과 76행 본문의 '연 2회'를 원어 'bi-annual'(2025 공고) 인용과 두 해석(연 2회/2년마다) 병기 또는 [추정]으로 정정(f11·f12), 2025 등재 5개사·2년 유효(f11), 2026 공고의 연례 표현·RFP/RFI 연락 경로(f13)와 AutoveX 2026-09-01부터 2년(f14)을 추가하고 '(2025-05 기준)'을 연차별로 나눔. ref-872 각주의 '(원문 미열람)' 해소. 의견 f36. 새 사례 블록(배송 로봇 서비스 계약; 약관이 현장 유형을 특정하지 않아 '병원·호텔 배송 로봇 업체의 공개 약관'으로만 표기): Relay 약관의 Tier 1 60분 응답 노력(f19), 시설 장애(승강기 고장) 시 지원 기한 연장(f20)을 '단일 업체 약관에 따르면' [추정]·벤더 주장으로, 완료·인계/예외·성과는 미확인. 가정 사례에 AIRROBO 고지의 QR 지속 공유 경로(f26)와 1X 사전예약 약관의 판매약관 위임(f29)을 [추정]·벤더 주장으로 짧게; 의견 f35 / 섹션 6(분리 2026-09-30-area58-s6) — 데이터 접근·공유 계약 소절: 일반 적용일(기존 51행) 뒤에 제3조(1) 설계 의무는 2026-09-12 후 출시 제품에만 적용(f3), 제4조(1)·(13) 범위와 계약 근거(f1·f2); MCT/SCC 문단(53행) 뒤에 부속서 X 의 면책 조항 부재와 제3자 청구 검토 권고(f4); 의견 f30·f31. 변경 주체 책임 소절: EU 개정 제조물책임지침의 다사업자 책임 관점 핵심만 — 소프트웨어 포함·비상업 FOSS 제외(f5), 실질적 변경자=제조자(f6), 적용 대상 '2026-12-08 후' 출시·투입 = 2026-12-09부터(f7, 정오표 2026-05-07; '2026-12-08부터'로 쓰지 말 것), 이행 기한 2026-12-09·구 지침 폐지(f8), 업무 전용 재산 손해 제외(f9), 증거 공개 필요·비례성과 영업비밀 고려(f10); 의견 f31·f32. 서비스 수준 약속과 감사 이력 소절: 공개 약관 비교 — Relay 책임 상한 18개월 요금·예외 3가지·캘리포니아 준거법(f21), 개인정보 고객 귀속(f22), Formant 통합자 책임 고객 귀속(f23)·가상 환경별 Device 계수(f24)·AI 출력 사람 검토(f25), AWS RoboRunner Error=500/503·5분 가용성·요청 없는 구간 100%(f27·f28) — 모두 [추정]·벤더 주장, 문장에 'OO사 약관에 따르면', 단일 업체 사례로 한정하고 업체 간 교차 확인으로 세지 않음; 의견 f33·f34. 영상 위탁 관리: 개인정보위 보도자료의 위수탁 시 보호책임자·주기 점검·교육 당부(f15)를 한두 문장으로만 넣고 53영역으로 연결; 의견 f38 / 섹션 7(분리 2026-09-30-area58-s7) — 데이터법 행(41행)에 '제3조(1)은 2026-09-12 후 출시 제품' 추가(f3). 행 추가: EU 개정 제조물책임지침(Directive (EU) 2024/2853, 소프트웨어 포함·실질적 변경자·적용 2026-12-09부터·이행 기한 2026-12-09, f5~f8), RFC 9745(폐기 표시는 동작 불변, Sunset≥Deprecation, 최소 간격 미규정, f16·f17); 의견 f37 / 섹션 8 — 연구 항목 추가: De Noyette·Stähler·Margoni(IIC 2025) 데이터법 영업비밀 체계와 관할별 행정 관행 파편화 위험(f18); 기존 MCT 항목(109행)은 기존 내용 확인(부속서 X 면책 공백은 6절로) / 섹션 11(분리 2026-09-30-area58-s11) — 해결 없음. 부분 근거: oq-241(f19~f25, 네 당사자 공통 분담표는 여전히 없음), oq-268(f24·f27·f28·f20; 메모의 'Formant 가상 환경 수량 공동 검증 주문서' 질문은 oq-268 의 하위 질문이라 새로 만들지 않음), oq-279·oq-320(f1·f2, 특정 ROP 지위 미판정), oq-280·oq-207(f16·f17, 로봇 계약상 최소 통지 일수 미확인), oq-259(f15), oq-185(f29, 원격 조작자 책임 미확인), oq-249(f10 은 법원 증거 공개 범위일 뿐 기계 규정 로그 의무의 플랫폼 적용은 미판정), oq-289(f5·f6 원문 조문만, 오케스트레이션 SW 해당 여부 미판정), oq-149(f13·f14, 국내 사례 없음), oq-110(f1~f3·f26). 답하지 못함: oq-145, oq-265, oq-281(가이드 본문 미열람), oq-282, oq-283, oq-290. 새 질문 3건 / 기존 내용 확인(새로 넣지 않음): MCT·SCC 사용이 자발적이라는 점(메모 F04) — s6.md 53행·s7.md 42행·본 페이지 109행·용어집 model-contractual-terms; 데이터법 일반 적용일 2025-09-12 — s6.md 51행·s7.md 41행; RFC 9745 Sunset≥Deprecation — 2026-09-25-area28-s4.md 40행(원문 미열람 근거였음); 증거 공개 제도 자체 — 2026-09-30-area59-s6.md 45행; 영상 위탁 점검 — privacy-and-video-data.md 108행(기사 ref-1136 근거) / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/glossary/data-holder.md 정의가 '연결 제품' 정의처럼 잘못 쓰임, docs/categories/security-and-privacy/index.md 169행의 비슷한 서술(ref-1274, ref-1191 과 같은 EC 해설 페이지), docs/topics/2026/2026-09-25-area28-s3.md 41행 '주요 조항의 적용 개시일은 미확인'(f3 로 해소 가능), docs/topics/2026/2026-09-30-area03-s7.md 44행·2026-09-30-area56-s7.md 46행 '연 2회'(f12), 59영역(2026-09-30-area59-s3·s4·s6·s7·s8, glossary/product-liability.md, standards/index.md 342행)의 제조물책임지침 서술 근거를 Gibson Dunn 해설(ref-1227)에서 원문(ref-1490)으로, 53영역 108행 근거를 1차 보도자료(ref-1494)로, ref-706 서지(발행 2025-03, 원문 열람). EU AI법 제25·26조 서술(s6.md 43·65행)은 개정 여부 점검 필요(미확인). 다음 실행 후보: 59. 법·규제·보험·라이선스(f5~f10), 63. 병원·의료(f11~f14), 3. 경제성·조달·사업 모델(f24·f27·f28)"
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "여러 사업자가 얽힌 장애·사고에서 서비스 수준 협약의 지원 기한을 멈추는 사유(시설 장애 등)와 재개 시점을 누가 확인·승인하며, 각 계약의 로그를 어떤 공통 식별자로 연결하는가? (관련: oq-112) | 관련 영역: 58. 다사업자 책임·계약·데이터, 32. 예외 복구·재계획·업무 연속성 | 근거: f20 | 종류: 일반",
    "제조사의 데이터법 고지가 안내하는 제3자 지속 공유 경로(승인 QR 코드·외부 플랫폼 등록 등)는 실제로 어떤 필드를 어떤 지연으로 제공하며, 사용자가 승인을 철회하면 언제 공유가 끊기는가? (관련: oq-110, oq-279) | 관련 영역: 58. 다사업자 책임·계약·데이터, 20. 로봇·제조사 관제 연동 | 근거: f26 | 종류: 일반",
    "RoMi-H 통합자 등재 프로그램의 실제 운영 주기는 무엇인가(2025 공고 'bi-annual', 2026 공고 'annual', 등재 유효 2년), 그리고 유효기간이 끝난 등재 통합자가 맡은 연동의 유지·장애 복구 책임은 어떻게 이어지는가? (관련: oq-149) | 관련 영역: 58. 다사업자 책임·계약·데이터, 63. 병원·의료 | 근거: f12 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 14,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-01/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.",
      "f4: C(2025) 7750 final 의 권고가 최종 채택(관보 게재)되었는지와 다국어본 공개 상태는 확인하지 못함(EC 페이지는 2026-03-03 갱신에도 Draft 표기). 합리적 보상 지침의 후속 발표 여부도 미확인",
      "f5~f10: 회원국별 제조물책임지침 이행 법령과 국내 제조물책임법의 소프트웨어 포함 개정 여부(oq-290)는 확인하지 못함. 오케스트레이션 소프트웨어가 제품·관련 서비스에 해당하는지(oq-289)는 판단하지 않음",
      "f11·f12: 2025 공고 'bi-annual'의 의도(연 2회/2년마다)는 공고 원문만으로 확정할 수 없음",
      "f15: 개인정보위 보도자료는 독립 검증 보고의 원문 대조 기준이며, 안내서 본문(ref-1135)과 개인정보 보호법 조문은 이번에 다시 열지 않음",
      "f18: 논문 §4.1.4 구절은 독립 검증 보고의 원문 대조 기준(로컬 저장본은 접근 차단 페이지), 서지는 Crossref 로 확인",
      "f19~f29: 벤더 약관은 공개 웹 문안이며 개별 체결본·주문서·단가·이행 실적은 미확인. AWS IoT RoboRunner 의 조사일 현재 신규 제공·지원 상태 미확인(지원 종료 공지는 찾지 못함). AIRROBO 고지의 발행일 미확인(PDF 작성 2025-12-23)",
      "검증 보고의 2차 자료 언급: 데이터법 개정안(Digital Omnibus, COM(2025) 837)이 협상 중으로 보이고 EU AI법이 개정되었다는 점은 원문으로 확인하지 않아 finding 으로 넣지 않음 — s6.md 의 AI법 제25·26조 서술 영향은 후속 점검",
      "oq-145(모델 대체·라우팅 희석 계약), oq-265(R15.08-3 사용자 의무), oq-281(산업데이터 계약 가이드 432쪽 본문), oq-282(기계 규정 실질적 변경과 플랫폼 설정 변경), oq-283(로봇-승강기 연동 표준 결과물)은 이번 메모가 답하지 못함"
    ],
    "scope_violations": [
      "f5~f10: EU 제조물책임지침의 법적 효력·적용 판단은 59. 법·규제·보험·라이선스 쪽 내용이므로 조문 확인까지만 하고 다사업자 책임 관점 핵심만 씀",
      "f15: 영상 위탁 관리는 53. 개인정보·영상 데이터와 겹치며, 이 영역에는 계약 부속서 관리 관점의 짧은 연결로만 씀",
      "f11~f14: RoMi-H 등재는 63. 병원·의료와 겹치며, 이 영역에는 통합자 사전 자격과 책임 주체 관점으로만 씀",
      "f16·f17: RFC 9745 는 41. 플랫폼 아키텍처·외부 API, 21. 상호운용 표준·적합성과 겹치며, 이 영역에는 제조사 API 폐기 통지의 계약 관점으로만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 10
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 10건/15(ref-1487~ref-1496, 예약 구간 ref-1487~ref-1516 안), 재사용 4건(ref-636·ref-1192·ref-872·ref-706). 출처 매핑(검증 결과 기준): 메모 n1→ref-636, n2→ref-1487(UBTech CDN), n3→ref-1488, n4→ref-1192, n5→ref-1489(미러 dirittobancario.it 대신 공식 EC URL), n6→ref-1490(EUR-Lex 원문; ref-1227 은 해설이라 쓰지 않음), n7→ref-1491(약관 표기 2023-03-01), n8→ref-1492, n9→ref-1493, n10→ref-1494(안내서 ref-1135·기사 ref-1136 과 별개 1차 보도자료), n11→ref-1495, n12→ref-872, n13→ref-706(원문 열람), n14→ref-1496. 교차 확인 0건(모든 사실 finding 이 단일 출처이거나 같은 기관 계열: EC 발표·부속서, CHART 2025·2026 공고) — 신뢰도 medium 이하. 벤더 약관 11건(Relay·Formant·AIRROBO·AWS·1X)은 모두 [추정]·vendor_claim, 서로 다른 업체의 다른 조건이라 교차 확인으로 세지 않음. 검증 반영: A01 정정 위치를 6절이 아니라 s4.md 40행(4절)으로, 근거 ref-1191→ref-636(f1); F03 제3조(1) 적용 대상(2026-09-12 후 출시)과 일반 적용일(2025-09-12) 구분(f3); F04 는 기존 내용이라 제외; F05 출처를 공식 EC URL 로(f4, 면책 조항 없음); 제조물책임지침은 다사업자 책임 관점 핵심만(f5~f10) 넣고 정오표 표기 '2026-12-08 후'=2026-12-09부터로 명시(f7), 제8조(2) 실질적 변경자 추가(f6); F13 'bi-annual' 원어 인용과 두 해석으로 정정(f11 사실·f12 추정); F14 는 53영역 중복이라 짧게(f15); RFC 9745 는 원문 열람으로 보강(f16·f17); 벤더 약관 X01~X11 은 '○○사 약관에 따르면'·단일 업체 사례로 한정(f19~f29), Formant 는 정의 번호 대신 용어 이름으로 인용. 열린 질문: 해결 없음. 부분 근거 oq-241·oq-268·oq-279·oq-320·oq-280·oq-207·oq-259·oq-185·oq-249·oq-289·oq-149·oq-110. 메모의 '답한 열린 질문' 가운데 '새 질문' 5건은 문구 대조로 기존 oq-279~oq-283 과 같아 새로 만들지 않음. 메모의 '새로 생긴 열린 질문' 3건 중 지원 기한 정지·제3자 공유 실동작 2건을 새로 올리고 Formant 수량 검증 건은 oq-268 에 묶음; RoMi-H 주기 질문 1건 추가. 메모의 '.research-work' 로컬 경로·행 번호(L…)는 쓰지 않고 원문 조·절·쪽과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음."
  }
}
```

### runs/2026-10-12-01/verification.json

```json
{
  "run_id": "2026-10-12-01",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: EUR-Lex 원문(2023-12-13 채택, OJ 2023-12-22)에서 제4조(13) 첫 문장 '계약을 근거로만'과 둘째 문장(경제 상황·자산·생산 방식 추론으로 시장 지위를 해치는 이용 금지)을 열람 확인. s4.md 40행 '사용자 동의 없이'는 조문과 다르므로 정정 근거로 유효. 단일 출처(1차 법령)"
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 제4조(1)(직접 접근 불가 시 쉽게 이용 가능한 데이터와 해석·이용에 필요한 메타데이터를 지체 없이 무료로 제공)과 제2조(17)('simple operation'을 넘는 과도한 노력 없이 적법하게 얻거나 얻을 수 있는 제품·관련 서비스 데이터) 원문 확인"
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 제50조 'It shall apply from 12 September 2025.' 및 제3조(1) 의무는 2026-09-12 후 출시 연결 제품·관련 서비스에 적용. 일반 적용일과 구분해 쓸 것"
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. ref-1489 URL 은 EC newsroom 공식 문서 주소에서 1.5MB PDF 로 응답했고 ref-1192 발표 페이지(2025-11-19 게시, 2026-03-03 갱신, Draft 표기)에 부속서·승인 문서 두 건이 링크돼 있어 실재는 인정. 그러나 검증 단계에서 PDF 텍스트를 추출하지 못했고 검색으로도 'do not include provisions on indemnification' 문구와 표지의 C(2025) 7750 번호를 확인하지 못함. ref-1192 발표 페이지는 부속서 X 내용을 담지 않아 교차 확인이 아님"
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 지침 2024/2853 통합본(02024L2853-20241118) 제4조(1)이 'it includes electricity, digital manufacturing files, raw materials and software', 제2조(2)가 상업 활동 밖 FOSS 제외. 오케스트레이션 SW 해당 여부 판정은 하지 않음(oq-289)"
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 제8조(2) 실질적 변경자를 제조자로 간주 원문 확인. 59영역 해설(ref-1227) 근거 서술과 같은 내용"
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 통합본 제2조(1)에 C1 정오표(32024L2853R(01), OJ L 90364, 2026-05-07) 표시와 'after 8 December 2026' 문구 확인. '2026-12-08 후 = 2026-12-09부터'로 쓰고 '2026-12-08부터'로 쓰지 않는다"
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 제22조(1) 이행 기한 2026-12-09, 제21조 구 지침 85/374/EEC 2026-12-09 부 폐지와 그 전 출시 제품 계속 적용 원문 확인. 회원국 이행 법령은 미확인"
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 제6조(1)(b) 재산 손해 제외 항목 'property used exclusively for professional purposes' 원문 확인"
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 제9조(3) 필요·비례 범위 제한, 제9조(4) 제3자 포함 모든 당사자의 정당한 이익 고려 원문 확인(영업비밀 언급 부분은 열람 요약 범위에서 확인). 법원 증거 공개 절차라는 한정 유지"
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: CGH 페이지(2025-05-01 게시, 'Updated as of 24 August 2026')에서 'bi-annual RoMi-H Empanelment Program', 5개사 2025-05-01부터 2년 유효, 'The integration via RoMi-H is to be undertaken by an empanelled System Integrator' 확인. ref-872 원문 열람으로 기존 '(원문 미열람)' 표시 해소 가능"
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 두 공고의 원어('bi-annual' 2025, 'annual' 2026)와 2년 유효기간을 열람 확인. 두 해석 병기 또는 [추정] 처리라는 판단은 [추정]으로 적정"
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: SingHealth 페이지(2026-05-06 게시, 2026-08-24 갱신) 'annual RoMi-H Empanelment Program', CHART 웹사이트 공개와 RFP/RFI 연락 문장 확인. ref-872 와 같은 기관 계열이라 독립 교차 확인 아님"
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 등재 명단 AutoveX Pte Ltd 1개사, 2026-09-01부터 2년 유효 확인. 2025 등재자 효력 변화는 공고에 없음"
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 개인정보보호위원회 보도자료(2024-10-14 게시, 제목 일치)에서 외부업체 위수탁 시 보호책임자 지정 및 주기적인 점검·교육 당부 문장 확인. 53영역과 중복이므로 짧은 연결로만"
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: RFC 9745(2025-03, Standards Track) §5 'The act of deprecation does not change any behavior of the resource' 및 이전과 같은 방식으로 계속 사용 가능 문장 확인"
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §4 Sunset 시각은 Deprecation 시각보다 이르면 안 됨(MUST NOT), 최소 간격 규정 없음(§3.1 'N days ahead'는 예시일 뿐) 확인"
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 서지(De Noyette·Ståhler·Margoni, IIC 56(5):984–1014, 온라인 2025-04-24, CC BY 4.0)는 Crossref 로 확인. 그러나 link.springer.com 은 인증 리디렉션으로 본문을 열 수 없었고, 브리프 self_check 도 §4.1.4 구절을 로컬 열람이 아니라 '독립 검증 보고' 기준으로 적었다(로컬 저장본은 접근 차단 페이지). 검색 요약은 '행정적 일관성에 관한 열린 질문'까지만 보여 '추가 파편화 위험' 구절은 확인하지 못함. 저자 성은 Crossref 기준 'Ståhler'(브리프 'Stähler')"
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Relay 약관(표기 'March 1st 2023') Exhibit A Tier 1 'commercially reasonable efforts to respond within 60 minutes of receiving the email request', 서비스 개시 후 적용. [추정]·벤더 주장 유지, 단일 업체 문안"
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 고객 네트워크·시설(승강기 고장 예) 문제 시 지원 기한이 고객 수리 때까지 연장되고 Relay 는 수리 책임을 지지 않는다는 예외 조항 확인. [추정]·벤더 주장 유지"
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §12 책임 상한 18개월 요금, 면책·라이선스 위반·비밀유지 위반 예외, §14.4 캘리포니아주법(산타클라라 카운티 관할) 확인. [추정]·벤더 주장 유지"
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §5.2 고객이 공유하기로 한 개인정보는 고객 소유, 서비스 제공 목적에만 사용 확인. 운영 데이터 전반 소유권으로 확대하지 않는다는 한정 유지"
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Formant 일반 약관(2026-04-16 갱신) 'Development Consultant' 정의에 고객 지시로만 일하며 고객이 그 작위·부작위에 책임진다는 문구 확인. [추정]·벤더 주장 유지"
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 'Device' 정의에서 한 장치에 가상 환경(PLC·Jetson·VM 등)이 둘 이상이면 각각 별도 Device 로 계수 확인. 단가 미공개"
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Formant AI 추가 조건에서 AI 출력 의존·실행 전 사람 검토 절차를 두도록 요구 확인. 업체 약관상 조건으로 한정"
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "부분 확인(벤더 주장 [추정] 유지): PDF URL 은 열렸고 파일 작성일(2025-12-23)이 브리프와 일치하나, 검증 단계에서 PDF 텍스트 추출에 실패해 §4(b) 문구와 발행 기관명 'Best Epoch Technology'는 직접 확인하지 못함. UBTech 데이터법 페이지에서 AIRROBO 가 UBTech 의 로봇청소기·수영장 청소 로봇 브랜드(T30+·E10+·PC200·PS100)임을, 다른 제조사(Proscenic) 고지에서 Tuya 승인 QR 코드 지속 공유와 앱 일회 내보내기 흐름을 정황 확인. 제품명 표기(T20/T25/T30/E10)는 UBTech 페이지 표기(T30+·E10+)와 다름"
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: AWS IoT RoboRunner SLA('Last Updated: November 28, 2022') Error=500·503, 5분 구간 가용성 정의 확인. 서비스 현재 제공 상태 미확인 병기 필요"
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 요청이 없던 5분 구간은 100% 가용으로 간주 문장 확인"
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 1X 사전예약 약관(2025-10-28 갱신) §2.4 구매 시 판매약관 동의, 취소·배송·보증 세부는 주문 초대·판매약관에 둔다 확인. 원격 조작자 책임 조항 없음(oq-185 미해결)"
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f1~f3(ref-636 원문 확인)에서 도출. 페이지에는 누구의 의견인지(구축자 의견) 밝혀야 함. 특정 ROP 지위 판정 아님"
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f4(이번 판정으로 [추정] 강등)·f9 에서 도출이므로 SCC 면책 공백 부분은 '부속서 설명에 따르면'이 아니라 추정 근거임을 드러내야 함. 계약 문안 결정은 계약 당사자·법무(59. 법·규제·보험·라이선스) 연계 대상으로 서술"
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f10 에서 도출. oq-249 판단 아님. 구축자 의견 표기 필요"
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f19·f20·f27·f28 에서 도출. 두 업체 약관은 교차 확인이 아님. 구축자 의견 표기 필요"
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f21~f25 에서 도출. 실제 주문서·단가 미공개. 구축자 의견 표기 필요"
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f26(부분 확인)에서 도출. 시험 결과 없음. 구축자 의견 표기 필요"
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f11~f14 에서 도출. flow_item '완료·인계'로 적혔으나 의견이므로 5절 표의 '완료·인계' 칸을 채우는 근거로 쓰지 않는다"
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f16·f17(RFC 9745 원문 확인)에서 도출. 구축자 의견 표기 필요"
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: f15·f18 에서 도출. f18 이 [추정]으로 강등됐으므로 논문 근거 부분은 '지적한 것으로 보인다' 수준으로 연결. 구축자 의견 표기 필요"
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": [
      "f5~f10: EU 개정 제조물책임지침의 적용·법적 효과 판단은 59. 법·규제·보험·라이선스 연계 대상이다. 조문 사실만 쓰고 ROP·오케스트레이션 소프트웨어에 대한 적용 판정처럼 쓰지 않도록 수정 지시로 처리(편집으로 해결 가능)",
      "f31·f32·f34: 계약 조항 설계 제안은 계약 당사자·법무 연계 대상에 대한 구축자 의견으로 써야 하며 ROP 가 계약을 체결·판정하는 것처럼 쓰지 않도록 수정 지시로 처리"
    ]
  },
  "duplication": {
    "ok": true,
    "overlaps": [
      "f1: docs/topics/2026/2026-09-30-area58-s4.md 40행 '데이터 보유자' 항목(ref-1191 근거)과 충돌 — 원문(ref-636) 기준 정정으로 처리",
      "f3: 데이터법 일반 적용일 2025-09-12 는 2026-09-30-area58-s6.md 51행·s7.md 41행에 이미 있음(기존 각주 재사용), 2026-09-25-area28-s3.md 41행 '적용 개시일 미확인'은 후속 정리",
      "f4: MCT·SCC 자발적 사용은 s6.md 53행·s7.md 42행·본 페이지 8절에 이미 있음(브리프가 제외함)",
      "f5~f10: 59영역(2026-09-30-area59-s3·s4·s6·s7)의 제조물책임지침 서술(ref-1227 해설 근거)과 같은 내용 — 58영역에는 다사업자 책임 관점 핵심만",
      "f11~f14: 63. 병원·의료 페이지와 2026-09-30-area03-s7.md 44행·2026-09-30-area56-s7.md 46행의 '연 2회' 표현과 겹침 — 다른 페이지는 후속 정리",
      "f15: 53. 개인정보·영상 데이터 privacy-and-video-data.md 108행(ref-1136 기사 근거)과 같은 내용",
      "f17: RFC 9745 선후 관계는 2026-09-25-area28-s4.md 40행에 이미 있음(원문 미열람 근거였음) — ref-706 재사용"
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
    "f4: [사실] → [추정]으로 강등한다 — 검증 단계에서 ref-1489 부속서 X 의 면책 조항 부재 문구를 확인하지 못했다(PDF 텍스트 추출 실패, 검색 미발견). 6절 MCT/SCC 문단에서는 '권고 초안 부속서의 클라우드 SCC 책임 조항 설명은 면책 조항을 두지 않고 제3자 청구 면책을 당사자가 검토하도록 권하는 것으로 보인다'처럼 추정 표현으로 쓰고, 권고가 여전히 초안(Draft)임을 함께 적는다.",
    "f18: [사실] → [추정]으로 강등하고 8절 항목을 '저자들은 회원국 관할 당국의 영업비밀 행정 관행 차이로 파편화 위험이 있다고 지적한 것으로 보인다' 수준으로 쓴다 — 논문 본문을 검증 단계·리서치 단계 모두 직접 열지 못했다. 저자 표기는 Crossref 기준 'Ståhler'로 쓴다.",
    "ref-1488: 브리프의 fetched: true 는 근거가 부족하다(self_check 가 로컬 저장본이 접근 차단 페이지였다고 적음). 페이지 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-1488 항목에 source_unopened: true 를 넣는다.",
    "f30~f38: 모든 [의견] 문장에 누구의 의견인지 '구축자 의견'으로 밝히고 근거 finding 의 사실 문장과 분리해 쓴다. f31·f32·f34 는 계약 당사자·법무와 59. 법·규제·보험·라이선스 쪽이 결정할 사항에 대한 제안으로 쓰고 ROP 가 계약을 정하는 것처럼 쓰지 않는다.",
    "f5~f10: 6절 변경 주체 책임 소절과 7절 행에는 조문 사실(소프트웨어 포함·비상업 FOSS 제외, 실질적 변경자=제조자, 적용 대상 '2026-12-08 후'=2026-12-09부터, 이행 기한·구 지침 폐지 2026-12-09, 업무 전용 재산 손해 제외, 증거 공개 필요·비례성)만 쓰고, 오케스트레이션 소프트웨어 해당 여부(oq-289)·설정 변경의 실질적 변경 여부는 판단하지 않는다고 밝히며 59. 법·규제·보험·라이선스로 연결한다. '2026-12-08부터'로 쓰지 않는다.",
    "5절 병원 사례: 표 '수행 자원' 칸과 본문의 '연 2회 평가·인증'을 지우고 2025 공고의 원어 'bi-annual'과 두 해석(연 2회/2년마다)을 [추정](f12)으로, 2025 등재 5개사·2025-05-01부터 2년(f11)과 2026 공고의 연례(annual) 표현·RFP/RFI 연락 경로(f13)·AutoveX 2026-09-01부터 2년(f14)을 연차별로 나눠 [사실]로 쓴다. '(2025-05 기준)'은 연차별 기준일로 바꾼다.",
    "5절 병원 사례: '완료·인계'·'예외·성과' 칸은 '미확인'을 유지하고, f36(의견)은 표 밖 본문에 구축자 의견으로만 쓴다. site_matrix_updates 에 의견을 근거로 한 칸을 넣지 않는다.",
    "ref-872: 각주의 ' (원문 미열람)' 표시를 지우고 접근일을 2026-10-12 로 고친다 — 이번 실행에서 원문을 열람해 확인했다.",
    "f19·f20(Relay 약관): 약관이 현장 유형을 특정하지 않으므로 현장 유형 없는 사례 블록을 5절에 만들지 않는다. 6절 서비스 수준 약속과 감사 이력 소절에 'Relay Robotics 공개 약관에 따르면' [추정]·벤더 주장으로 넣고, site_matrix_updates 에도 넣지 않는다.",
    "f19~f29: 벤더 약관 문장마다 [추정]에 '벤더 주장'을 병기하고 '○○사 약관(갱신일)에 따르면'으로 시작하며, 단일 업체 문안이고 업체 간 교차 확인이 아님을 밝힌다. f27·f28 에는 조사일 현재 AWS IoT RoboRunner 제공·지원 상태가 미확인임을 함께 적는다.",
    "f26: 고지가 열거한 개별 제품 모델명은 쓰지 않고 'AIRROBO 브랜드 로봇청소기·수영장 청소 로봇의 EU 데이터법 고지'로 쓴다 — 검증 단계에서 모델명 표기(T30/E10 대 T30+/E10+)를 확인하지 못했다. [추정]·벤더 주장, 실제 동작 미시험을 유지한다.",
    "4절(분리 2026-09-30-area58-s4) 40행 '데이터 보유자' 항목: '사용자 동의 없이'를 f1 대로 '쉽게 이용 가능한 비개인 데이터를 사용자와의 계약을 근거로만 이용할 수 있고 사용자의 시장 지위를 해치는 추론에 쓸 수 없다'로 고치고 근거 각주를 ref-1191 에서 ref-636 으로 바꾼다. 개인정보 처리 근거(GDPR)는 별개임을 밝힌다.",
    "6절·7절 데이터법: 일반 적용일(2025-09-12)과 제3조(1) 설계 의무 적용 대상(2026-09-12 후 출시 연결 제품·관련 서비스, f3)을 구분해 쓰고, 제4조(1) 제공 범위(쉽게 이용 가능한 데이터·메타데이터, f2)를 '모든 데이터의 소유권'처럼 넓히지 않는다.",
    "7절: RFC 9745 행(f16·f17)과 EU 개정 제조물책임지침 행을 추가할 때 ref-706 각주는 접근일 2026-10-12, 원문 열람으로 갱신하고 '최소 통지 간격은 정하지 않는다'를 함께 적는다.",
    "f15: 6절에 한두 문장으로만 넣고 53. 개인정보·영상 데이터로 연결한다. 감독기관의 당부이며 ROP 의 운영자·수탁자 지위 판정이 아님을 밝힌다(oq-259 미해결 유지).",
    "인용: 출처당 직접 인용은 1회 짧은 구절만 쓴다(예: ref-872 의 'bi-annual', ref-1495 의 'annual'). ref-636·ref-1490·ref-1491·ref-1496 등의 나머지 조문·약관 문구는 요약·재서술한다.",
    "용어: 데이터 보유자·모델 계약 조항·실질적 변경·제조물책임·API 폐기 정책·서비스 수준 협약·등재 프로그램은 기존 용어집 항목 표기를 쓰고 링크한다. 새 용어집 항목은 만들지 않는다.",
    "열린 질문: 해결 처리하는 기존 질문은 없다. open_questions_new 3건은 그대로 등록하고, 브리프가 든 부분 근거(oq-241·oq-268·oq-279·oq-320·oq-280·oq-207·oq-259·oq-185·oq-249·oq-289·oq-149·oq-110)는 '부분 근거'로만 적고 상태를 바꾸지 않는다.",
    "미사용 출처는 없다. ref-1192 는 f4 의 보조 근거(초안 상태·발표일)로만 쓰고 부속서 X 내용의 근거로 각주를 달지 않는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 36건, 미확인 2건, 교차 확인 0건. 강등: f4 사실 → 추정(부속서 X 면책 문구 미확인), f18 사실 → 추정(논문 본문 미열람). 원문 미열람 출처: ref-1488(브리프의 fetched 표시 근거 부족 — 페이지에 원문 미열람 표기 지시). 검증 단계 텍스트 추출 실패: ref-1489·ref-1487(PDF), ref-1487 은 UBTech 데이터법 페이지와 다른 제조사 고지로 정황만 확인. 주의: EU 데이터법(제2조(17)·제4조(1)·(13)·제50조), 개정 제조물책임지침(제2·4·6·8·9·21·22조, 2026-05-07 정오표), RFC 9745, RoMi-H 2025·2026 공고, 개인정보위 보도자료는 원문으로 확인했으나 모두 단일 출처다. 벤더 약관 11건(Relay·Formant·AIRROBO·AWS·1X)은 단일 업체의 공개 문안이며 벤더 주장이다. 2025 공고의 'bi-annual'은 연 2회와 2년마다로 모두 읽힐 수 있어 확정하지 않는다. 제조물책임지침의 오케스트레이션 소프트웨어 적용 여부는 판단하지 않았다. 정정 요청 없음. 검증 예산: 검색 5회, 열람은 출처당 2회 기준을 ref-636(EUR-Lex 장문 페이지 분할 열람 4회)에서 넘겼다.",
  "retry_reason": null
}
```

### runs/2026-10-12-01/pages.json

```json
{
  "run_id": "2026-10-12-01",
  "pages": [
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "차등 갱신: 4절 데이터 보유자 정의를 데이터법 원문(제4조(13)·제2조(17))으로 바로잡고 2026-09-30 분리 페이지 연결 복구, 5절 병원 사례의 '연 2회'를 원어와 두 해석으로 고치고 2025·2026 등재를 연차별로 나눔, 가정 청소 로봇 데이터 공유 사례 추가, 6절 데이터법 적용 시점·SCC 면책(추정)·제조물책임지침 조문·공개 약관 비교(벤더 주장)·영상 위탁 관리 보강과 2026-09-30 분리 페이지 연결, 7절 요약 문장에 제조물책임지침·RFC 9745 추가와 표 3행, 8절 논문 1건, 11절 실행별 질문 건수 정정·부분 근거·새 질문 3건, 13절 각주 갱신(ref-872 원문 열람, ref-1488 원문 미열람)",
      "patches": [
        {
          "section": "4. 핵심 개념과 용어",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-01/pages/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-01/pages/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-01/pages/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-01/pages/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-01/pages/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-01/pages/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "frontmatter": {
            "sources": [
              "ref-031",
              "ref-872",
              "ref-1191",
              "ref-1192",
              "ref-1193",
              "ref-1194",
              "ref-1204",
              "ref-555",
              "ref-1205",
              "ref-1206",
              "ref-1207",
              "ref-317",
              "ref-1208",
              "ref-1209",
              "ref-1210",
              "ref-1211",
              "ref-1212",
              "ref-636",
              "ref-706",
              "ref-1487",
              "ref-1488",
              "ref-1489",
              "ref-1490",
              "ref-1491",
              "ref-1492",
              "ref-1493",
              "ref-1494",
              "ref-1495",
              "ref-1496"
            ],
            "last_run": "2026-10-12"
          },
          "content": "(절 본문 생략 — runs/2026-10-12-01/pages/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-12-area58-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 58. 다사업자 책임·계약·데이터 의 \"6. 대표 접근법과 기술\" 절(4,483자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area58-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 58. 다사업자 책임·계약·데이터 의 \"11. 열린 질문\" 절(1,186자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area58-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 58. 다사업자 책임·계약·데이터 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,029자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area58-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 58. 다사업자 책임·계약·데이터 의 \"8. 대표 연구와 자료\" 절(774자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area58-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 58. 다사업자 책임·계약·데이터 의 \"4. 핵심 개념과 용어\" 절(699자)을 옮겼다"
    }
  ],
  "outline": [
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 700,
      "summary": "EU 데이터법 제4조(13)에 따르면 데이터 보유자는 쉽게 이용 가능한 비개인 데이터를 사용자와의 계약을 근거로만 이용할 수 있다. [사실][^ref-636] 2026-09-30 실행까지의 본문은 기존 분리 페이지에 있다.",
      "planned_findings": [
        "f1",
        "f2"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2600,
      "summary": "싱가포르 CHART는 RoMi-H 연동을 등재 통합자에게 맡기며 2025년 5개사, 2026년 AutoveX 1개사를 각 2년 유효로 등재했다. [사실][^ref-872][^ref-1495]",
      "planned_findings": [
        "f11",
        "f12",
        "f13",
        "f14",
        "f36",
        "f26",
        "f29",
        "f35"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 4300,
      "summary": "접근은 변경 주체 책임·데이터 계약·버전 폐기 규칙·서비스 수준과 감사 이력의 네 갈래로 보이며 [추정][^ref-555][^ref-1192][^ref-031][^ref-1205], 2026-09-30 실행까지의 본문은 기존 분리 페이지에 있다.",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f15",
        "f19",
        "f20",
        "f21",
        "f22",
        "f23",
        "f24",
        "f25",
        "f27",
        "f28",
        "f30",
        "f31",
        "f32",
        "f33",
        "f34",
        "f38"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 900,
      "summary": "규칙은 데이터 권리, 인터페이스 변경(RFC 9745 포함), 서비스 수준·보안·기록, 변경 주체 책임(EU 개정 제조물책임지침 포함)으로 나뉘며 2026-09-30 실행까지의 본문은 기존 분리 페이지에 있다.",
      "planned_findings": [
        "f3",
        "f5",
        "f6",
        "f7",
        "f8",
        "f16",
        "f17",
        "f37"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 250,
      "summary": "De Noyette·Ståhler·Margoni(2025)는 데이터법 영업비밀 체계의 관할별 행정 관행 파편화 위험을 지적한 것으로 보인다. [추정][^ref-1488]",
      "planned_findings": [
        "f18"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "11. 열린 질문",
      "budget_chars": 1200,
      "summary": "2026-09-30 실행에서 새 질문 5건, 2026-10-12 실행에서 해결 없이 새 질문 3건을 올렸고 2026-09-30 실행까지의 본문은 기존 분리 페이지에 있다.",
      "planned_findings": []
    }
  ],
  "changelog_entry": "2026-10-12 | 58. 다사업자 책임·계약·데이터 | 데이터 보유자 정의를 데이터법 원문으로 바로잡고 RoMi-H 등재 주기 표현('연 2회')을 원어·두 해석으로 정정, 데이터법 적용 시점·제조물책임지침 조문·공개 약관 비교(벤더 주장)·RFC 9745 보강, 2026-09-30 분리 페이지 연결 유지, 새 열린 질문 3건 | run 2026-10-12-01",
  "index_updates": {
    "home_recent": "2026-10-12 — 58. 다사업자 책임·계약·데이터: 데이터법 원문 기준으로 데이터 보유자 정의 정정, 병원 등재 통합자 사례 연차별 정리, 제조물책임지침 조문과 공개 서비스 약관 비교 보강",
    "category_recent": "2026-10-12 — 58. 다사업자 책임·계약·데이터: 4·5·6·7·8·11절 차등 갱신(데이터법 적용 시점, 제조물책임지침 조문, 공개 약관 비교, RFC 9745, 새 열린 질문 3건)",
    "area_recent": "2026-10-12 — 58. 다사업자 책임·계약·데이터: 갱신(4절 데이터 보유자 정정, 5절 병원 사례 'bi-annual' 정정·2026 공고 추가·가정 데이터 공유 사례, 6절 데이터법·제조물책임지침·공개 약관·영상 위탁, 7절 표 3행, 8절 논문, 11절 부분 근거·새 질문 3건, 2026-09-30 분리 페이지 연결 유지)"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-636",
      "org": "European Union (EUR-Lex)",
      "title": "Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act)",
      "published": "2023-12-13",
      "url": "https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "EU 데이터법 원문. 제2조(17), 제4조(1)·(13), 제50조(일반 적용 2025-09-12, 제3조(1)은 2026-09-12 후 출시 제품)를 원문으로 확인했다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1192",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts",
      "published": "2025-11-19",
      "url": "https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "MCT·SCC 권고 초안 발표 페이지. 2025-11-19 발표, 2026-03-03 갱신이며 여전히 초안(Draft) 표기다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-872",
      "org": "Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "RoMi-H Empanelment Programme 2025",
      "published": "2025-05-01",
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "2025년 RoMi-H 통합자 등재 공고(2026-08-24 갱신, 이번에 원문 열람). 프로그램을 'bi-annual'로 적고 5개사 등재가 2025-05-01부터 2년 유효하다고 게시한다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-706",
      "org": "IETF (RFC Editor)",
      "title": "RFC 9745: The Deprecation HTTP Response Header Field",
      "published": "2025-03",
      "url": "https://www.rfc-editor.org/info/rfc9745/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "Deprecation HTTP 응답 헤더 규격(Standards Track). 이번에 원문을 열어 §4(Sunset 시각은 Deprecation 시각보다 이를 수 없음, 최소 간격 미규정)와 §5(폐기 표시는 자원 동작을 바꾸지 않음)를 확인했다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1487",
      "org": "Best Epoch Technology Co., Ltd. (AIRROBO)",
      "title": "EU DATA ACT Notice",
      "published": null,
      "url": "https://owebsite-cdn.ubtrobot.com/resources/file/2025/12/25/755762357268549.pdf",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "AIRROBO 브랜드 로봇청소기·수영장 청소 로봇의 EU 데이터법 사전 고지 PDF. 앱 내보내기와 승인 QR 코드(Tuya 플랫폼 등록)를 통한 제3자 공유 경로를 안내한다. 발행일 미확인이며 검증 단계에서는 PDF 텍스트를 추출하지 못해 정황 확인에 그쳤다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1488",
      "org": "De Noyette, E., Ståhler, L., Margoni, T. (IIC 56(5))",
      "title": "Data Secrets: The Data Act's New Trade Secrets Framework",
      "published": "2025-04-24",
      "url": "https://link.springer.com/article/10.1007/s40319-025-01601-9",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "원문 미열람. 데이터법의 영업비밀 체계를 분석한 동료심사 법학 논문(IIC 56(5):984–1014, CC BY 4.0). 서지는 Crossref 로 확인했고, 회원국 행정 관행의 파편화 위험을 지적한 것으로 보인다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1489",
      "org": "European Commission",
      "title": "ANNEX to the Communication to the Commission — Approval of the draft Commission Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts (with Annexes), C(2025) 7750 final",
      "published": "2025-11-19",
      "url": "https://ec.europa.eu/newsroom/dae/redirection/document/121719",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "MCT·SCC 권고 초안 본문과 부속서. 부속서의 클라우드 SCC 책임 설명은 면책 조항을 두지 않고 제3자 청구 면책을 당사자가 검토하도록 권하는 것으로 보이나, 검증 단계에서 해당 문구를 직접 확인하지 못했다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1490",
      "org": "European Union (EUR-Lex)",
      "title": "Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC",
      "published": "2024-11-18",
      "url": "https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "EU 개정 제조물책임지침 원문. 2026-05-07 정오표로 제2조(1) 적용 대상이 '2026-12-08 후' 출시·투입 제품(2026-12-09부터)으로 고쳐졌다. 제2·4·6·8·9·21·22조를 통합본으로 확인했다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1491",
      "org": "Relay Robotics",
      "title": "Terms of Service (Exhibit A: Service Level Agreement)",
      "published": "2023-03-01",
      "url": "https://relayrobotics.com/tos",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "병원·호텔 배송 로봇 업체의 공개 서비스 약관. 지원 응답 시간, 시설 장애 시 지원 기한 연장, 18개월 요금 기준 책임 상한, 개인정보 귀속, 캘리포니아 준거법을 정한다. 단일 업체 문안이다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1492",
      "org": "Amazon Web Services",
      "title": "AWS IoT RoboRunner Service Level Agreement",
      "published": "2022-11-28",
      "url": "https://aws.amazon.com/roborunner/sla/",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "AWS IoT RoboRunner 의 공개 SLA. 500·503 응답을 오류로, 5분 구간 요청 성공률을 가용성으로 정의하고 요청 없는 구간은 100% 가용으로 본다. 조사일 현재 서비스 제공 상태는 미확인이다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1493",
      "org": "1X Technologies, Inc.",
      "title": "Pre-Order Terms",
      "published": "2025-10-28",
      "url": "https://www.1x.tech/legal",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "가정용 휴머노이드 사전예약 약관. 구매 때 별도 판매약관 동의를 요구한다. 원격 조작자 운영 책임 조항은 이 문서에 없다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1494",
      "org": "개인정보보호위원회",
      "title": "자율주행 인공지능(AI) 발전을 위한 개인영상정보 보호ㆍ활용 기준 나왔다",
      "published": "2024-10-14",
      "url": "https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=10678",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "이동형 영상정보처리기기 개인영상정보 보호·활용 안내서 발표 보도자료. 외부업체 위수탁 처리 시 보호책임자 지정과 주기적 점검·교육을 당부한다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1495",
      "org": "SingHealth / Changi General Hospital CHART",
      "title": "RoMi-H Empanelment Programme 2026",
      "published": "2026-05-06",
      "url": "https://www.singhealth.com.sg/news/robotics/romi-h-empanelment-programme-2026",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "2026년 RoMi-H 통합자 등재 공고(2026-08-24 갱신). 연례 프로그램이라 적고 AutoveX Pte Ltd 의 등재를 2026-09-01부터 2년 유효로 게시한다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1496",
      "org": "Formant",
      "title": "General Terms",
      "published": "2026-04-16",
      "url": "https://www.formant.ai/terms_of_use",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "로봇 관제 플랫폼 업체의 일반 약관. 고객 지정 통합자 책임의 고객 귀속, 가상 환경별 Device 계수, Formant AI 출력의 사람 검토 요구를 정한다. 단일 업체 문안이다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "여러 사업자가 얽힌 장애·사고에서 서비스 수준 협약의 지원 기한을 멈추는 사유(시설 장애 등)와 재개 시점을 누가 확인·승인하며, 각 계약의 로그를 어떤 공통 식별자로 연결하는가? (관련: oq-112)",
      "areas": [
        58,
        32
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "제조사의 데이터법 고지가 안내하는 제3자 지속 공유 경로(승인 QR 코드·외부 플랫폼 등록 등)는 실제로 어떤 필드를 어떤 지연으로 제공하며, 사용자가 승인을 철회하면 언제 공유가 끊기는가? (관련: oq-110, oq-279)",
      "areas": [
        58,
        20
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "RoMi-H 통합자 등재 프로그램의 실제 운영 주기는 무엇인가(2025 공고 'bi-annual', 2026 공고 'annual', 등재 유효 2년), 그리고 유효기간이 끝난 등재 통합자가 맡은 연동의 유지·장애 복구 책임은 어떻게 이어지는가? (관련: oq-149)",
      "areas": [
        58,
        63
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#5-적용-사례-현장-유형-명시",
      "title": "58. 다사업자 책임·계약·데이터"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#5-적용-사례-현장-유형-명시",
      "title": "58. 다사업자 책임·계약·데이터"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#5-적용-사례-현장-유형-명시",
      "title": "58. 다사업자 책임·계약·데이터"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#5-적용-사례-현장-유형-명시",
      "title": "58. 다사업자 책임·계약·데이터"
    },
    {
      "site_type": "가정",
      "item": "시작 조건",
      "link": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#5-적용-사례-현장-유형-명시",
      "title": "58. 다사업자 책임·계약·데이터"
    },
    {
      "site_type": "가정",
      "item": "작업 대상",
      "link": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#5-적용-사례-현장-유형-명시",
      "title": "58. 다사업자 책임·계약·데이터"
    },
    {
      "site_type": "가정",
      "item": "수행 자원",
      "link": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#5-적용-사례-현장-유형-명시",
      "title": "58. 다사업자 책임·계약·데이터"
    },
    {
      "site_type": "가정",
      "item": "제약",
      "link": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#5-적용-사례-현장-유형-명시",
      "title": "58. 다사업자 책임·계약·데이터"
    }
  ],
  "additional_research_requests": [
    "4절 정정(1차 수정 지시 12): 정정 대상 문장이 있는 주제 페이지 docs/topics/2026/2026-09-30-area58-s4.md 가 이번 입력에 없어 그 페이지의 40행을 직접 고치지 못했다. 다음 갱신 실행에서 그 주제 페이지를 입력에 넣어 '데이터 보유자' 항목의 '사용자 동의 없이'를 '사용자와의 계약을 근거로만'으로 고치고 각주를 ref-1191 에서 ref-636 으로 바꾸도록 요청한다(이번에는 세부영역 페이지 4절에 바로잡은 정의와 그 페이지 링크를 두었다).",
    "6·7·11절 분리 주제 페이지(2026-09-30-area58-s6·s7·s11)도 입력에 없어, 이번 보강은 세부영역 페이지 해당 절에 넣고 기존 분리 페이지로 가는 연결 문장을 두었다. s6.md 51행·s7.md 41행의 데이터법 서술에 제3조(1) 적용 대상(2026-09-12 후 출시 제품)을 함께 적는 정리는 그 페이지를 입력에 넣은 다음 실행에서 한다.",
    "5절 병원 사례의 '완료·인계'·'예외·성과' 칸: RoMi-H 연동 완료를 인정하는 기준과 장애 시 복구 주체에 관한 공개 원문이 필요하다(현재 미확인).",
    "5절: 물류창고·제조 공장·상업 시설·실외 현장의 다사업자 책임·계약 공개 사례(공개 계약 문안·지원 응답·시설 장애 예외)가 필요하다. Relay 약관처럼 현장 유형을 특정한 계약 문안이면 사례 블록으로 쓸 수 있다.",
    "후속 정리(이번 갱신 범위 밖 페이지): docs/glossary/data-holder.md 정의 점검, docs/categories/security-and-privacy/index.md 169행의 비슷한 서술, docs/topics/2026/2026-09-25-area28-s3.md 41행 '적용 개시일 미확인'(f3 로 해소 가능), docs/topics/2026/2026-09-30-area03-s7.md 44행·2026-09-30-area56-s7.md 46행의 '연 2회'(f12), 59영역 페이지·glossary/product-liability.md·standards/index.md 의 제조물책임지침 근거를 해설(ref-1227)에서 원문(ref-1490)으로, 53영역 privacy-and-video-data.md 108행 근거를 1차 보도자료(ref-1494)로 바꾸는 갱신을 요청한다. 하루 갱신 상한으로 이번에 다루지 않았다.",
    "6절 EU AI법 제25·26조 서술(분리 주제 페이지 2026-09-30-area58-s6.md 43·65행)이 최근 개정에 영향을 받았는지 원문 확인이 필요하다(브리프 self_check 기준 미확인)."
  ],
  "fixes_applied": [
    "f4 강등 — 6절 '데이터 접근·공유 계약' 보강에서 부속서 SCC 책임 설명을 '…권하는 것으로 보인다' [추정][^ref-1489]로 쓰고, 권고가 2026-03-03 갱신 때도 초안(Draft)임을 별도 문장 [사실][^ref-1192]로 함께 적었다.",
    "f18 강등 — 8절 항목을 '저자들은 … 파편화 위험이 있다고 지적한 것으로 보인다' [추정][^ref-1488]로 쓰고 저자 표기를 'Ståhler'로 했다.",
    "ref-1488 원문 미열람 — 13절 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-1488 에 source_unopened: true 와 '원문 미열람.'으로 시작하는 요약을 넣었다.",
    "f30~f38 구축자 의견 — 5·6·7절의 모든 [의견] 문장을 '구축자 의견으로는'으로 시작해 사실 문장과 분리했고, f31·f32·f34 는 계약 당사자·법무·59. 법·규제·보험·라이선스가 결정할 사항에 대한 제안이며 ROP가 정하는 일이 아니라고 적었다.",
    "f5~f10 — 6절 변경 주체 책임 소절과 7절 표 행에 조문 사실만 쓰고, oq-289·oq-282 를 판단하지 않는다고 밝히며 59. 법·규제·보험·라이선스로 연결했다. 적용 대상은 '2026-12-08 후', 즉 2026-12-09부터로만 썼다.",
    "5절 병원 사례 — 표 '수행 자원' 칸과 본문의 '연 2회 평가·인증'을 지우고, 'bi-annual' 원어와 두 해석을 [추정]으로, 2025 등재 5개사·2025-05-01부터 2년(f11)과 2026 공고의 연례 표현·RFP/RFI 연락 경로(f13)·AutoveX 2026-09-01부터 2년(f14)을 연차별 [사실]로 나눴다. '(2025-05 기준)'은 공고별 게시·갱신일로 바꿨다.",
    "5절 병원 사례 — '완료·인계'·'예외·성과' 칸은 '미확인'을 유지하고 f36 은 표 밖 본문에 구축자 의견으로만 썼으며, site_matrix_updates 에 완료·인계 칸을 넣지 않았다.",
    "ref-872 — 13절 각주의 ' (원문 미열람)'을 지우고 접근일을 2026-10-12 로 고쳤다.",
    "f19·f20 — Relay 약관은 5절 사례 블록으로 만들지 않고 6절 '서비스 수준 협약 — 공개 약관 비교' 소절에 'Relay Robotics 공개 약관(2023-03-01 표기)에 따르면' [추정] 벤더 주장으로 넣었으며 site_matrix_updates 에도 넣지 않았다.",
    "f19~f29 — 벤더 약관 문장마다 '○○ 약관(갱신일)에 따르면'으로 시작하고 [추정] 벤더 주장을 붙였으며, 단일 업체 문안이고 업체 간 교차 확인이 아님을 소절 머리에 밝혔다. f27·f28 에는 조사일 현재 RoboRunner 제공·지원 상태 미확인을 적었다.",
    "f26 — 개별 모델명을 쓰지 않고 'AIRROBO 브랜드 로봇청소기·수영장 청소 로봇의 EU 데이터법 고지'로 썼고, [추정] 벤더 주장과 실제 동작 미시험을 유지했다.",
    "4절 데이터 보유자 — 세부영역 페이지 4절에 f1 대로 '쉽게 이용 가능한 비개인 데이터를 사용자와의 계약을 근거로만 이용할 수 있고 사용자의 시장 지위를 해치는 추론에 쓸 수 없다'는 정의를 ref-636 각주로 덧붙이고, 주제 페이지의 '사용자 동의 없이' 표현이 조문과 다르다는 점과 GDPR 처리 근거가 별개임을 적었다. 부분 이행: 정정 대상 주제 페이지(2026-09-30-area58-s4.md)가 입력에 없어 그 40행 자체는 고치지 못했고 additional_research_requests 에 요청했다.",
    "데이터법 6·7절 — 일반 적용일(2025-09-12)과 제3조(1) 설계 의무 적용 대상(2026-09-12 후 출시 연결 제품·관련 서비스)을 구분해 6절 문단과 7절 표 행에 썼고, 제4조(1) 제공 범위를 쉽게 이용 가능한 데이터·메타데이터로 한정해 소유권처럼 넓히지 않았다.",
    "7절 — RFC 9745 행과 EU 개정 제조물책임지침 행을 추가하고, RFC 행에 '최소 통지 간격은 정하지 않는다'를 적었으며 ref-706 각주를 발행 2025-03·접근일 2026-10-12·원문 열람으로 갱신했다.",
    "f15 — 6절 '영상 처리 위탁 관리' 소절에 두 문장으로만 넣고 53. 개인정보·영상 데이터로 연결했으며, 감독기관 당부이고 운영자·수탁자 지위 판정이 아님(oq-259 열림)을 밝혔다.",
    "인용 — 직접 인용은 ref-872 'bi-annual', ref-1495 'annual', ref-1496 'Development Consultant' 각 1회로 한정하고 ref-636·ref-1490·ref-1491 등의 나머지 문구는 요약·재서술했다.",
    "용어 — 데이터 보유자·모델 계약 조항·실질적 변경·제조물책임·API 폐기 정책·서비스 수준 협약·등재 프로그램을 기존 용어집 표기로 쓰고 링크했으며, glossary_updates 는 비워 새 항목을 만들지 않았다.",
    "열린 질문 — 해결 처리한 질문이 없고, open_questions_new 3건을 그대로 open_question_updates 에 new 로 냈으며, 부분 근거 12건(oq-241·oq-268·oq-279·oq-320·oq-280·oq-207·oq-259·oq-185·oq-249·oq-289·oq-149·oq-110)은 11절에 '부분 근거'로만 적고 상태를 바꾸지 않았다.",
    "ref-1192 — 권고 초안의 발표일·초안 상태 문장에만 각주로 쓰고 부속서 X 내용 문장에는 ref-1489 만 달았다.",
    "2차: 2026-09-30 분리 페이지 연결 복구 — 4·6·7·11절 패치를 replace 로 보내고, 각 절 첫 문단을 '기존 요약 문장 + 2026-09-30 실행까지의 이 절 본문은 [2026-09-30 … 페이지](../../topics/2026/2026-09-30-area58-s4.md|s6.md|s7.md|s11.md)에 있다.' 두 문장으로 구성했다. '자세한 내용은 주제 페이지'로 시작하지 않게 했고, 자동 분리 뒤에도 세부영역 페이지에 남도록 첫 문단 안에 두었으며 링크 텍스트에는 마침표가 든 번호를 넣지 않았다. 각 절의 2026-10-12 보강 내용은 그대로 이어 두었다.",
    "2차: 4절 '위 주제 페이지' 링크화 — '위 주제 페이지의 데이터 보유자 항목'을 '[2026-09-30 핵심 개념과 용어 페이지](../../topics/2026/2026-09-30-area58-s4.md)의 데이터 보유자 항목'으로 바꾸고, 그 아래에 태그 없는 문장 '정정 대상 문장은 그 페이지에 아직 남아 있으며, 다음 갱신 실행에서 그 페이지를 직접 고친다.'를 더했다.",
    "2차: 11절 질문 건수 정정 — action 을 replace 로 바꾸고 첫 문장을 '2026-09-30 실행에서 기존 8건에 새 질문 5건을 더했고, 2026-10-12 실행에서는 해결된 질문 없이 새 질문 3건을 올렸다.'로 고쳐 쓴 뒤, 2026-09-30 열린 질문 페이지 연결 문장과 기존 append 내용(부분 근거 목록·새 질문 3건)을 그대로 이었다.",
    "2차: Formant Device 드리프트 삭제 — 6절 서비스 수준 협약 소절 Formant 둘째 항목의 '과금 단위인 장치(Device)'를 '약관이 정의한 장치(Device)'로 고치고, 뒤 문장을 '주문서의 단가·최소 요금은 공개되지 않아 이 계수 방식이 요금에 주는 영향은 확인하지 않았다.'로 써서 과금 영향을 단정하지 않았다.",
    "2차: 7절 요약 문장 보강 — action 을 replace 로 바꾸고 첫 문장의 '인터페이스 변경(VDA 5050·Kubernetes 폐기 정책)'에 RFC 9745 를, '변경 주체 책임(EU 기계류 규정·EU AI법)'에 EU 개정 제조물책임지침을 더했다. 이어서 연결 문장과 기존 append 내용(표 3행·구축자 의견)을 그대로 두었다.",
    "분량 초과 자동 분리: 58. 다사업자 책임·계약·데이터 본문 12,417자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 5,305자"
  ]
}
```

### runs/2026-10-12-01/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md (7개 절)
- 분량 초과 자동 분리:
    - docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-12-area58-s6.md (4,483자)
    - docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md "11. 열린 질문" → docs/topics/2026/2026-10-12-area58-s11.md (1,186자)
    - docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-12-area58-s7.md (1,029자)
    - docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-12-area58-s8.md (774자)
    - docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-10-12-area58-s4.md (699자)
```

### runs/2026-10-12-01/pages/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md

```markdown
---
title: "58. 다사업자 책임·계약·데이터"
type: area
category: "P. 거버넌스·법규·사회"
area_no: 58
related_areas: [2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65]
tags: [데이터 접근 계약, 실질적 변경, API 폐기 정책, 서비스 수준 협약, 감사 추적]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-10-12
sources: [ref-031, ref-872, ref-1191, ref-1192, ref-1193, ref-1194, ref-1204, ref-555, ref-1205, ref-1206, ref-1207, ref-317, ref-1208, ref-1209, ref-1210, ref-1211, ref-1212, ref-636, ref-706, ref-1487, ref-1488, ref-1489, ref-1490, ref-1491, ref-1492, ref-1493, ref-1494, ref-1495, ref-1496]
last_run: 2026-10-12
version: 3
---

[홈](../../index.md) › [P. 거버넌스·법규·사회](index.md) › 58. 다사업자 책임·계약·데이터

# 58. 다사업자 책임·계약·데이터

!!! info "소속 대분류"
    [P. 거버넌스·법규·사회](index.md) — 핵심 질문:
    여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

여러 사업자가 함께 운영하는 현장에서 연동 오류를 누가 고치고 변경을 누가 승인하는지를 한 번에 정한 공개 표준이나 책임 분담표는 이번 조사(2026-09-30 기준)에서 찾지 못했고, 실제 규칙은 변경한 주체에게 제조자·제공자 의무를 지우는 법 규정, 인터페이스 표준의 버전·폐기 규칙, 서비스 수준 협약·표준 계약 조항과 통합자 사전 자격 같은 계약·조달 장치가 겹쳐 정해지는 것으로 보인다. [추정][^ref-555][^ref-1209][^ref-031][^ref-1204][^ref-1205][^ref-1192][^ref-1206][^ref-872]

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 왜 중요한가](../../topics/2026/2026-09-30-area58-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 용어는 책임이 넘어가는 조건, 데이터 권리, 인터페이스 변경 예고, 서비스 약속과 기록의 네 묶음으로 나뉜다. 2026-09-30 실행까지의 이 절 본문은 [2026-09-30 핵심 개념과 용어 페이지](../../topics/2026/2026-09-30-area58-s4.md)에 있다.

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 핵심 개념과 용어](../../topics/2026/2026-10-12-area58-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 병원

**사례:** 싱가포르 공공 의료기관의 로봇·소프트웨어·IoT 연동을 등재 통합자에게 맡기기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 공공 의료기관이 로봇·소프트웨어·IoT를 연동하려 할 때 [사실][^ref-872] |
| 작업 대상 | 로봇·소프트웨어·IoT와 의료 로봇 미들웨어 RoMi-H 사이의 통합 [사실][^ref-872] |
| 수행 자원 | 창이종합병원 CHART의 등재 프로그램으로 평가·인증받은 시스템 통합자. 2025년 공고 기준 5개사가 2025-05-01부터 2년간 유효하게 등재되었다 [사실][^ref-872] 2026년 공고 기준 AutoveX Pte Ltd 1개사가 2026-09-01부터 2년간 유효하게 등재되었다 [사실][^ref-1495] |
| 제약 | 공공 의료기관의 RoMi-H 연동은 등재된 통합자가 맡아야 한다 [사실][^ref-872] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

창이종합병원 CHART는 의료 로봇 미들웨어 [RoMi-H](../../glossary/robotic-middleware-for-healthcare.md) 통합을 맡을 시스템 통합자를 [등재 프로그램](../../glossary/empanelment-programme.md)으로 평가·재평가하고, 공공 의료기관이 RoMi-H 연동에 등재된 통합자를 쓰게 해 연동을 맡을 주체를 사전 자격으로 정한다. [사실][^ref-872][^ref-1495] 2025년 공고(2025-05-01 게시, 2026-08-24 갱신본 확인)의 등재 통합자는 HOPE Technik, Medisys Innovation, Panasonic Asia Pacific, QuikBot Technologies, Techfox 5개사다. [사실][^ref-872] 2026년 공고(2026-05-06 게시, 2026-08-24 갱신)는 등재 통합자를 CHART 웹사이트에 공개해 공공 의료기관 등이 제안요청(RFP/RFI) 참여를 위해 연락할 수 있게 한다고 적는다. [사실][^ref-1495] 2025년 등재 통합자의 효력이 2026년 공고로 어떻게 되는지는 공고에서 확인되지 않는다.

프로그램 주기는 공고마다 표현이 다르다. 2025년 공고는 프로그램을 'bi-annual'로, 2026년 공고는 'annual'로 적는다. [사실][^ref-872][^ref-1495] 앞의 표현은 '연 2회'로도 '2년마다'로도 읽힐 수 있고 같은 공고가 등재 유효기간을 2년으로 적고 있어, 실제 평가 주기는 확정할 수 없다. [추정][^ref-872][^ref-1495]

구축자 의견으로는, 통합자 등재는 연동 역량을 평가한 사전 자격일 뿐이므로 등재 사실과 별도로 인수 기준·장애 복구 책임·등재 유효기간 만료 시 처리를 계약 당사자가 계약에 적어 두는 편이 좋다. [의견][^ref-872][^ref-1495] 연동 완료를 인정하는 기준과 장애 때 누가 복구하는지는 확인하지 못했다. 국내에서 비슷한 관문을 운용한 사례는 [oq-149](../../open-questions.md)에서 열려 있고, 등재 주기와 유효기간 만료 뒤 책임 승계는 이번 갱신에서 [열린 질문](../../open-questions.md)으로 새로 올렸다. 병원 현장 쪽 내용은 [63. 병원·의료](../site-type-applications/hospital-and-healthcare.md)에 있다.

**현장 유형:** 가정

**사례:** 한국 공동주택의 주차·순찰·운반 로봇 도입과 관리 책임

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 차량 주차, 단지 순찰, 물품 운반 [사실][^ref-1211] |
| 수행 자원 | 시흥 힐스테이트더웨이브시티 주차로봇 2세트(실증), 서울 송파구 아파트 자율주행 순찰로봇 2대, 강남 타워팰리스 사족보행로봇(기술검증), 부산 강서구 아파트 운반로봇 서비스 [사실][^ref-1211] |
| 제약 | 발의된 이동로봇 특별법안이 개인정보 처리·책임 분담·책임보험 가입 같은 안전관리 체계를 담는다고 전해졌다(법안 원문 미확인) [사실][^ref-1211] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

같은 사설(한국아파트신문, 2026-09-14)의 의견으로는 이런 로봇이 들어오면 관리주체의 관리 영역과 책임이 넓어질 수 있어, 도입 전에 책임 범위를 명확히 해야 한다. [의견][^ref-1211] 사례마다 제조사·관제 사업자·관리주체가 장애를 어떻게 나눠 맡는지는 확인하지 못했다. 가정 로봇의 원격 조작자 책임은 [oq-185](../../open-questions.md)에서 열려 있다.

**현장 유형:** 가정

**사례:** 가정용 청소 로봇의 데이터를 제3자와 공유하기(EU 데이터법 고지)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 고지에 따르면 사용자가 앱에서 데이터를 내보내거나 승인 QR 코드로 제3자 공유를 승인할 때 [추정] 벤더 주장[^ref-1487] |
| 작업 대상 | 고지에 따르면 로봇청소기·수영장 청소 로봇의 데이터 [추정] 벤더 주장[^ref-1487] |
| 수행 자원 | 고지에 따르면 사용자, 제조사 앱, Tuya 클라우드 플랫폼에 등록한 제3자 [추정] 벤더 주장[^ref-1487] |
| 제약 | 고지에 따르면 지속 공유를 받으려는 제3자는 Tuya 클라우드 플랫폼에 등록해야 한다 [추정] 벤더 주장[^ref-1487] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

AIRROBO 브랜드 로봇청소기·수영장 청소 로봇의 EU 데이터법 고지(발행일 미확인)에 따르면 사용자는 앱에서 데이터를 내보내 한 번에 제3자와 공유하거나, 승인된 QR 코드로 제3자와 지속 공유할 수 있고, 지속 공유를 받으려는 제3자는 Tuya 클라우드 플랫폼에 등록해야 한다. [추정] 벤더 주장[^ref-1487] 실제 제공 필드·지연·승인 철회 동작은 시험하지 않았다. 구축자 의견으로는, 제조사 고지가 안내하는 내보내기·제3자 지속 공유 경로를 ROP 온보딩 때 제3자 등록·필드 목록·지연·승인 철회까지 직접 시험해 확인하는 편이 좋다. [의견][^ref-1487]

1X Technologies 사전예약 약관(2025-10-28 갱신)에 따르면 가정용 휴머노이드의 주문 초대를 받아 로봇을 받으려는 사람은 구매 시점에 제시되는 별도 판매약관에 동의해야 하며, 취소·배송·보증 세부는 주문 초대나 판매약관에 둔다. [추정] 벤더 주장[^ref-1493] 이 문서에서는 원격 조작자의 영상 접근·사고 책임 조항을 확인하지 못해 [oq-185](../../open-questions.md)는 열려 있다.

물류창고·제조 공장·상업 시설·실외 현장의 다사업자 책임·계약 사례는 2026-10-12 갱신까지 찾지 못했다. 병원·호텔 배송 로봇 업체(Relay Robotics)의 공개 약관은 현장 유형을 특정하지 않아 사례 대신 6절에 두었다.

## 6. 대표 접근법과 기술

다사업자 책임·계약·데이터를 다루는 접근은 변경한 주체에게 책임을 지우는 규정과 사전 자격, 데이터 접근·공유 계약, 인터페이스 버전·폐기 규칙, 서비스 수준 약속과 감사 이력의 네 갈래로 모이는 것으로 보인다. [추정][^ref-555][^ref-1192][^ref-031][^ref-1205] 2026-09-30 실행까지의 이 절 본문은 [2026-09-30 대표 접근법과 기술 페이지](../../topics/2026/2026-09-30-area58-s6.md)에 있다.

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 대표 접근법과 기술](../../topics/2026/2026-10-12-area58-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역에 걸리는 규칙은 데이터 권리(EU 데이터법·국내 산업 디지털 전환 촉진법), 인터페이스 변경(VDA 5050·Kubernetes 폐기 정책·RFC 9745), 서비스 수준·보안·기록(ISO/IEC 19086-1·IEC 62443-2-4·21 CFR Part 11), 변경 주체 책임(EU 기계류 규정·EU AI법·EU 개정 제조물책임지침)으로 나뉜다.

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-12-area58-s7.md)에 있다.

## 8. 대표 연구와 자료

유럽연합 집행위원회, 데이터 접근·이용 모델 계약 조항과 클라우드 표준 계약 조항 권고 초안(2025) — 데이터법 이행용 계약 문안 네 벌과 클라우드 계약 조항 여섯 개를 담은 구속력 없는 초안이며, 의무적 기업 간 데이터 공유의 합리적 보상 지침은 추후 발표 예정으로 되어 있다. [사실][^ref-1192]

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 대표 연구와 자료](../../topics/2026/2026-10-12-area58-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사 어댑터별 인터페이스 버전과 폐기 일정 관리, 연동·설정 변경의 요청·승인·적용 기록 [추정][^ref-031][^ref-1204] | 로봇 펌웨어와 제조사 API의 수명주기(로봇 제조사) [추정][^ref-555][^ref-1209] |
| 시설·설비 제어 | 설비 어댑터의 인터페이스 버전 관리와 연동 변경 기록 [추정][^ref-031][^ref-1204] | 승강기·출입문 쪽 연동 인터페이스와 설비 안전(설비 제조사·관리주체) [추정][^ref-317][^ref-1211] |
| 원문 19장 다섯 경계 밖(계약·법무·데이터 권리·서비스 수준) | 누가 언제 어떤 명령·변경을 했는지 남기는 타임스탬프 감사 이력과 보관, 데이터 항목별 소유·접근·반출 조건 표시, 계약한 서비스 수준 지표의 측정·보고 [추정][^ref-1207][^ref-1210][^ref-1191][^ref-1192][^ref-1205] | 계약 체결, 법적 책임 판정·보험·규제 적합성 평가(계약 당사자·법무, [59. 법·규제·보험·라이선스](law-regulation-insurance-and-licensing.md)) [추정][^ref-555][^ref-1209][^ref-1208] |

이 영역에서 ROP가 직접 맡을 범위는 제조사·설비 어댑터별 인터페이스 버전과 폐기 일정 관리, 연동·설정 변경의 요청·승인·적용 기록, 타임스탬프 감사 이력과 보관, 데이터 항목별 소유·접근·반출 조건 표시, 계약한 서비스 수준 지표의 측정·보고로 보인다. [추정][^ref-031][^ref-1204][^ref-1207][^ref-1210][^ref-1191][^ref-1192][^ref-1205]

연계 대상: 계약 체결과 법적 책임 판정·보험·규제 적합성 평가는 계약 당사자와 법무에, 로봇 펌웨어와 제조사 API의 수명주기는 로봇 제조사에, 승강기·출입문 쪽 연동 인터페이스와 설비 안전은 설비 제조사·관리주체에 속하므로, ROP는 그들이 정한 조건을 운영 제약으로 받고 판단 근거가 되는 기록과 데이터를 제공하는 쪽을 맡는 것으로 보인다. [추정][^ref-555][^ref-1209][^ref-317][^ref-1211][^ref-1208] EU 기계류 규정과 EU AI법이 정하는 제조자·제공자·배포자 의무를 누가 지는지 판정하고 이행하는 일도 이 연계 대상에 들며, 이 페이지는 그 의무를 ROP가 직접 지는 것으로 서술하지 않는다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

범위 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 인터페이스 버전 규칙, 설비 연동, 감사 이력, 데이터 권리, 규제 책임, 조달, AI 가치사슬 책임, 적용 현장을 통해 열네 개 세부영역과 이어지는 것으로 보인다. [추정][^ref-031][^ref-1210][^ref-1191][^ref-1209]

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area58-s10.md)에 있다.

## 11. 열린 질문

2026-09-30 실행에서 기존 8건에 새 질문 5건을 더했고, 2026-10-12 실행에서는 해결된 질문 없이 새 질문 3건을 올렸다. 2026-09-30 실행까지의 이 절 본문은 [2026-09-30 열린 질문 페이지](../../topics/2026/2026-09-30-area58-s11.md)에 있다.

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 열린 질문](../../topics/2026/2026-10-12-area58-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [58. 다사업자 책임·계약·데이터](multi-party-responsibility-contracts-and-data.md) — 영역 심화: 3~11절 첫 작성(병원·가정 적용 사례, 데이터 계약·버전·폐기 규칙·SLA·감사 이력, 책임 경계, 연결 14건, 열린 질문 8건+새 질문 5건), 13절 각주, 1차 조건부 승인 수정 17건 반영, 2차 수정: 9절 표 셋째 행 경계 칸을 '원문 19장 다섯 경계 밖'으로 고침 (실행 2026-09-30-22)
- 2026-09-30 · 생성 · [58. 다사업자 책임·계약·데이터 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area58-s6.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "6. 대표 접근법과 기술" 절(2,613자)을 옮겼다 (실행 2026-09-30-22)
- 2026-09-30 · 생성 · [58. 다사업자 책임·계약·데이터 — 열린 질문](../../topics/2026/2026-09-30-area58-s11.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "11. 열린 질문" 절(1,824자)을 옮겼다 (실행 2026-09-30-22)
- 2026-09-30 · 생성 · [58. 다사업자 책임·계약·데이터 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area58-s7.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,269자)을 옮겼다 (실행 2026-09-30-22)
- 2026-09-30 · 생성 · [58. 다사업자 책임·계약·데이터 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area58-s10.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,155자)을 옮겼다 (실행 2026-09-30-22)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-10-12
[^ref-1191]: European Commission (Shaping Europe's digital future), Data Act explained, 2025-12-15, https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained, 접근일 2026-09-30
[^ref-1192]: European Commission (Shaping Europe's digital future), Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts, 2025-11-19, https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding, 접근일 2026-10-12
[^ref-1204]: The Kubernetes Authors, Kubernetes Deprecation Policy, 미확인, https://kubernetes.io/docs/reference/using-api/deprecation-policy/, 접근일 2026-09-30
[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)
[^ref-1205]: IEC / ISO (ISO/IEC JTC 1), ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts, 2016-09-21, https://webstore.iec.ch/en/publication/25920, 접근일 2026-09-30 (원문 미열람)
[^ref-1206]: IEC (BSI Knowledge 게재), IEC 62443-2-4:2023 Security for industrial automation and control systems - Security program requirements for IACS service providers, 2023-12-15, https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1, 접근일 2026-09-30 (원문 미열람)
[^ref-1207]: U.S. Food and Drug Administration 규정 (Cornell Law School LII 게재), 21 CFR § 11.10 - Controls for closed systems, 미확인, https://www.law.cornell.edu/cfr/text/21/11.10, 접근일 2026-09-30
[^ref-317]: 전기신문 (안상민), 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인, 2023-05-17, https://www.electimes.com/news/articleView.html?idxno=320147, 접근일 2026-09-30
[^ref-1208]: Shaik, A. S. (SSRN), Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong?, 2026-05-01, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6737139, 접근일 2026-09-30 (원문 미열람)
[^ref-1209]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 25: Responsibilities Along the AI Value Chain | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/25/, 접근일 2026-09-30
[^ref-1210]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 26: Obligations of Deployers of High-Risk AI Systems | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/26/, 접근일 2026-09-30
[^ref-1211]: 한국아파트신문 (사설), 공동주택에 밀려오는 로봇, 또 다른 관리책임은 없을까, 2026-09-14, https://www.hapt.co.kr/news/articleView.html?idxno=169488, 접근일 2026-09-30
[^ref-1487]: Best Epoch Technology Co., Ltd. (AIRROBO), EU DATA ACT Notice, 미확인, https://owebsite-cdn.ubtrobot.com/resources/file/2025/12/25/755762357268549.pdf, 접근일 2026-10-12
[^ref-1493]: 1X Technologies, Inc., Pre-Order Terms, 2025-10-28, https://www.1x.tech/legal, 접근일 2026-10-12
[^ref-1495]: SingHealth / Changi General Hospital CHART, RoMi-H Empanelment Programme 2026, 2026-05-06, https://www.singhealth.com.sg/news/robotics/romi-h-empanelment-programme-2026, 접근일 2026-10-12
```

### docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md

```markdown
---
title: "58. 다사업자 책임·계약·데이터"
type: area
category: "P. 거버넌스·법규·사회"
area_no: 58
related_areas: [2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65]
tags: [데이터 접근 계약, 실질적 변경, API 폐기 정책, 서비스 수준 협약, 감사 추적]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-031, ref-872, ref-1191, ref-1192, ref-1193, ref-1194, ref-1204, ref-555, ref-1205, ref-1206, ref-1207, ref-317, ref-1208, ref-1209, ref-1210, ref-1211, ref-1212]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [P. 거버넌스·법규·사회](index.md) › 58. 다사업자 책임·계약·데이터

# 58. 다사업자 책임·계약·데이터

!!! info "소속 대분류"
    [P. 거버넌스·법규·사회](index.md) — 핵심 질문:
    여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

여러 사업자가 함께 운영하는 현장에서 연동 오류를 누가 고치고 변경을 누가 승인하는지를 한 번에 정한 공개 표준이나 책임 분담표는 이번 조사(2026-09-30 기준)에서 찾지 못했고, 실제 규칙은 변경한 주체에게 제조자·제공자 의무를 지우는 법 규정, 인터페이스 표준의 버전·폐기 규칙, 서비스 수준 협약·표준 계약 조항과 통합자 사전 자격 같은 계약·조달 장치가 겹쳐 정해지는 것으로 보인다. [추정][^ref-555][^ref-1209][^ref-031][^ref-1204][^ref-1205][^ref-1192][^ref-1206][^ref-872]

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 왜 중요한가](../../topics/2026/2026-09-30-area58-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 용어는 책임이 넘어가는 조건, 데이터 권리, 인터페이스 변경 예고, 서비스 약속과 기록의 네 묶음으로 나뉜다.

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area58-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 병원

**사례:** 싱가포르 공공 의료기관의 로봇·소프트웨어·IoT 연동을 등재 통합자에게 맡기기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 공공 의료기관이 로봇·소프트웨어·IoT를 연동하려 할 때 [사실][^ref-872] |
| 작업 대상 | 로봇·소프트웨어·IoT와 의료 로봇 미들웨어 RoMi-H 사이의 통합 [사실][^ref-872] |
| 수행 자원 | 창이종합병원 CHART가 연 2회 평가·인증해 등재한 시스템 통합자 [사실][^ref-872] |
| 제약 | 공공 의료기관은 등재된 통합자를 써야 한다 [사실][^ref-872] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

창이종합병원 CHART는 의료 로봇 미들웨어 [RoMi-H](../../glossary/robotic-middleware-for-healthcare.md) 통합을 맡을 시스템 통합자를 연 2회 [등재 프로그램](../../glossary/empanelment-programme.md)으로 평가·인증하고, 공공 의료기관이 로봇·소프트웨어·IoT 연동에 등재된 통합자를 쓰게 해 다사업자 연동의 책임 주체를 사전 자격으로 정한다(2025-05 기준). [사실][^ref-872] 연동 완료를 인정하는 기준과 장애 때 누가 복구하는지는 확인하지 못했다. 국내에서 비슷한 관문을 운용한 사례는 [oq-149](../../open-questions.md)에서 열려 있다.

**현장 유형:** 가정

**사례:** 한국 공동주택의 주차·순찰·운반 로봇 도입과 관리 책임

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 차량 주차, 단지 순찰, 물품 운반 [사실][^ref-1211] |
| 수행 자원 | 시흥 힐스테이트더웨이브시티 주차로봇 2세트(실증), 서울 송파구 아파트 자율주행 순찰로봇 2대, 강남 타워팰리스 사족보행로봇(기술검증), 부산 강서구 아파트 운반로봇 서비스 [사실][^ref-1211] |
| 제약 | 발의된 이동로봇 특별법안이 개인정보 처리·책임 분담·책임보험 가입 같은 안전관리 체계를 담는다고 전해졌다(법안 원문 미확인) [사실][^ref-1211] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

같은 사설(한국아파트신문, 2026-09-14)의 의견으로는 이런 로봇이 들어오면 관리주체의 관리 영역과 책임이 넓어질 수 있어, 도입 전에 책임 범위를 명확히 해야 한다. [의견][^ref-1211] 사례마다 제조사·관제 사업자·관리주체가 장애를 어떻게 나눠 맡는지는 확인하지 못했다. 가정 로봇의 원격 조작자 책임은 [oq-185](../../open-questions.md)에서 열려 있다.

물류창고·제조 공장·상업 시설·실외 현장의 다사업자 책임·계약 사례는 이번 조사에서 찾지 못했다.

## 6. 대표 접근법과 기술

다사업자 책임·계약·데이터를 다루는 접근은 변경한 주체에게 책임을 지우는 규정과 사전 자격, 데이터 접근·공유 계약, 인터페이스 버전·폐기 규칙, 서비스 수준 약속과 감사 이력의 네 갈래로 모이는 것으로 보인다. [추정][^ref-555][^ref-1192][^ref-031][^ref-1205]

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area58-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역에 걸리는 규칙은 데이터 권리(EU 데이터법·국내 산업 디지털 전환 촉진법), 인터페이스 변경(VDA 5050·Kubernetes 폐기 정책), 서비스 수준·보안·기록(ISO/IEC 19086-1·IEC 62443-2-4·21 CFR Part 11), 변경 주체 책임(EU 기계류 규정·EU AI법)으로 나뉜다.

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area58-s7.md)에 있다.

## 8. 대표 연구와 자료

- 유럽연합 집행위원회, 데이터 접근·이용 모델 계약 조항과 클라우드 표준 계약 조항 권고 초안(2025) — 데이터법 이행용 계약 문안 네 벌과 클라우드 계약 조항 여섯 개를 담은 구속력 없는 초안이며, 의무적 기업 간 데이터 공유의 합리적 보상 지침은 추후 발표 예정으로 되어 있다. [사실][^ref-1192]
- 산업통상부, 산업데이터 계약 가이드라인(2023) — 국내 산업데이터 거래 당사자를 위한 유의사항·표준계약서·업종별 사례를 담은 432쪽 자료다. [사실][^ref-1194]
- Shaik, A. S., Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong?(SSRN, 2026, 동료심사 전 원고) — Shaik의 제안은 로봇 제조사(OEM)·시스템 통합자·AI 공급자·운영자 사이의 책임을 통제력(피해를 막을 수 있었는가)·예견 가능성·정보 비대칭의 세 원칙으로 배분하는 위험 비례 책임 프레임워크(RPLF)이며, 저자는 이를 상업 계약과 기존 보험으로 구현할 수 있다고 주장한다. [의견][^ref-1208]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사 어댑터별 인터페이스 버전과 폐기 일정 관리, 연동·설정 변경의 요청·승인·적용 기록 [추정][^ref-031][^ref-1204] | 로봇 펌웨어와 제조사 API의 수명주기(로봇 제조사) [추정][^ref-555][^ref-1209] |
| 시설·설비 제어 | 설비 어댑터의 인터페이스 버전 관리와 연동 변경 기록 [추정][^ref-031][^ref-1204] | 승강기·출입문 쪽 연동 인터페이스와 설비 안전(설비 제조사·관리주체) [추정][^ref-317][^ref-1211] |
| 원문 19장 다섯 경계 밖(계약·법무·데이터 권리·서비스 수준) | 누가 언제 어떤 명령·변경을 했는지 남기는 타임스탬프 감사 이력과 보관, 데이터 항목별 소유·접근·반출 조건 표시, 계약한 서비스 수준 지표의 측정·보고 [추정][^ref-1207][^ref-1210][^ref-1191][^ref-1192][^ref-1205] | 계약 체결, 법적 책임 판정·보험·규제 적합성 평가(계약 당사자·법무, [59. 법·규제·보험·라이선스](law-regulation-insurance-and-licensing.md)) [추정][^ref-555][^ref-1209][^ref-1208] |

이 영역에서 ROP가 직접 맡을 범위는 제조사·설비 어댑터별 인터페이스 버전과 폐기 일정 관리, 연동·설정 변경의 요청·승인·적용 기록, 타임스탬프 감사 이력과 보관, 데이터 항목별 소유·접근·반출 조건 표시, 계약한 서비스 수준 지표의 측정·보고로 보인다. [추정][^ref-031][^ref-1204][^ref-1207][^ref-1210][^ref-1191][^ref-1192][^ref-1205]

연계 대상: 계약 체결과 법적 책임 판정·보험·규제 적합성 평가는 계약 당사자와 법무에, 로봇 펌웨어와 제조사 API의 수명주기는 로봇 제조사에, 승강기·출입문 쪽 연동 인터페이스와 설비 안전은 설비 제조사·관리주체에 속하므로, ROP는 그들이 정한 조건을 운영 제약으로 받고 판단 근거가 되는 기록과 데이터를 제공하는 쪽을 맡는 것으로 보인다. [추정][^ref-555][^ref-1209][^ref-317][^ref-1211][^ref-1208] EU 기계류 규정과 EU AI법이 정하는 제조자·제공자·배포자 의무를 누가 지는지 판정하고 이행하는 일도 이 연계 대상에 들며, 이 페이지는 그 의무를 ROP가 직접 지는 것으로 서술하지 않는다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

범위 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 인터페이스 버전 규칙, 설비 연동, 감사 이력, 데이터 권리, 규제 책임, 조달, AI 가치사슬 책임, 적용 현장을 통해 열네 개 세부영역과 이어지는 것으로 보인다. [추정][^ref-031][^ref-1210][^ref-1191][^ref-1209]

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area58-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 기존 열린 질문 8건은 모두 열려 있고, 이번 실행에서 새 질문 5건을 올렸다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 열린 질문](../../topics/2026/2026-09-30-area58-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [58. 다사업자 책임·계약·데이터](multi-party-responsibility-contracts-and-data.md) — 영역 심화: 3~11절 첫 작성(병원·가정 적용 사례, 데이터 계약·버전·폐기 규칙·SLA·감사 이력, 책임 경계, 연결 14건, 열린 질문 8건+새 질문 5건), 13절 각주, 1차 조건부 승인 수정 17건 반영, 2차 수정: 9절 표 셋째 행 경계 칸을 '원문 19장 다섯 경계 밖'으로 고침 (실행 2026-09-30-22)
- 2026-09-30 · 생성 · [58. 다사업자 책임·계약·데이터 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area58-s6.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "6. 대표 접근법과 기술" 절(2,613자)을 옮겼다 (실행 2026-09-30-22)
- 2026-09-30 · 생성 · [58. 다사업자 책임·계약·데이터 — 열린 질문](../../topics/2026/2026-09-30-area58-s11.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "11. 열린 질문" 절(1,824자)을 옮겼다 (실행 2026-09-30-22)
- 2026-09-30 · 생성 · [58. 다사업자 책임·계약·데이터 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area58-s7.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,269자)을 옮겼다 (실행 2026-09-30-22)
- 2026-09-30 · 생성 · [58. 다사업자 책임·계약·데이터 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area58-s10.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,155자)을 옮겼다 (실행 2026-09-30-22)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30 (원문 미열람)
[^ref-1191]: European Commission (Shaping Europe's digital future), Data Act explained, 2025-12-15, https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained, 접근일 2026-09-30
[^ref-1192]: European Commission (Shaping Europe's digital future), Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts, 2025-11-19, https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding, 접근일 2026-09-30
[^ref-1194]: 산업통상부 (공공데이터포털), 산업통상부_산업데이터 계약 가이드라인_20230109, 2023-04-05, https://www.data.go.kr/data/15113186/fileData.do, 접근일 2026-09-30
[^ref-1204]: The Kubernetes Authors, Kubernetes Deprecation Policy, 미확인, https://kubernetes.io/docs/reference/using-api/deprecation-policy/, 접근일 2026-09-30
[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)
[^ref-1205]: IEC / ISO (ISO/IEC JTC 1), ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts, 2016-09-21, https://webstore.iec.ch/en/publication/25920, 접근일 2026-09-30 (원문 미열람)
[^ref-1206]: IEC (BSI Knowledge 게재), IEC 62443-2-4:2023 Security for industrial automation and control systems - Security program requirements for IACS service providers, 2023-12-15, https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1, 접근일 2026-09-30 (원문 미열람)
[^ref-1207]: U.S. Food and Drug Administration 규정 (Cornell Law School LII 게재), 21 CFR § 11.10 - Controls for closed systems, 미확인, https://www.law.cornell.edu/cfr/text/21/11.10, 접근일 2026-09-30
[^ref-317]: 전기신문 (안상민), 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인, 2023-05-17, https://www.electimes.com/news/articleView.html?idxno=320147, 접근일 2026-09-30
[^ref-1208]: Shaik, A. S. (SSRN), Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong?, 2026-05-01, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6737139, 접근일 2026-09-30 (원문 미열람)
[^ref-1209]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 25: Responsibilities Along the AI Value Chain | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/25/, 접근일 2026-09-30
[^ref-1210]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 26: Obligations of Deployers of High-Risk AI Systems | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/26/, 접근일 2026-09-30
[^ref-1211]: 한국아파트신문 (사설), 공동주택에 밀려오는 로봇, 또 다른 관리책임은 없을까, 2026-09-14, https://www.hapt.co.kr/news/articleView.html?idxno=169488, 접근일 2026-09-30
```

### runs/2026-10-12-01/pages/topics/2026/2026-10-12-area58-s6.md

```markdown
---
title: "58. 다사업자 책임·계약·데이터 — 대표 접근법과 기술"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 58
related_areas: [2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-031, ref-1192, ref-1205, ref-1488, ref-1489, ref-1490, ref-1491, ref-1492, ref-1494, ref-1496, ref-555, ref-636]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#6
---

[홈](../../index.md) › [주제](../index.md) › 58. 다사업자 책임·계약·데이터 — 대표 접근법과 기술

# 58. 다사업자 책임·계약·데이터 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 다사업자 책임·계약·데이터를 다루는 접근은 변경한 주체에게 책임을 지우는 규정과 사전 자격, 데이터 접근·공유 계약, 인터페이스 버전·폐기 규칙, 서비스 수준 약속과 감사 이력의 네 갈래로 모이는 것으로 보인다. [추정][^ref-555][^ref-1192][^ref-031][^ref-1205] 2026-09-30 실행까지의 이 절 본문은 [2026-09-30 대표 접근법과 기술 페이지](2026-09-30-area58-s6.md)에 있다.
- 이 페이지는 [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

다사업자 책임·계약·데이터를 다루는 접근은 변경한 주체에게 책임을 지우는 규정과 사전 자격, 데이터 접근·공유 계약, 인터페이스 버전·폐기 규칙, 서비스 수준 약속과 감사 이력의 네 갈래로 모이는 것으로 보인다. [추정][^ref-555][^ref-1192][^ref-031][^ref-1205] 2026-09-30 실행까지의 이 절 본문은 [2026-09-30 대표 접근법과 기술 페이지](2026-09-30-area58-s6.md)에 있다.

### 2026-10-12 보강: 데이터 접근·공유 계약

EU 데이터법은 2025-09-12부터 적용되지만, 연결 제품·관련 서비스를 사용자가 데이터에 직접 접근할 수 있게 설계·제조할 의무(제3조(1))는 2026-09-12 후에 시장에 출시되는 연결 제품과 관련 서비스에만 적용된다. [사실][^ref-636] 사용자가 직접 접근할 수 없으면 데이터 보유자는 쉽게 이용 가능한 데이터와 그 해석·이용에 필요한 관련 메타데이터를 지체 없이 무료로 제공해야 하며(제4조(1)), 제공 범위는 이 두 가지로 정해져 있다. [사실][^ref-636] 데이터 보유자가 그 비개인 데이터를 이용하려면 사용자와의 계약이 근거가 되어야 한다(제4조(13), 4절). [사실][^ref-636]

구축자 의견으로는, ROP의 데이터 자산 대장이 데이터 항목마다 데이터법상 역할(사용자·데이터 보유자·제3자), 이용 근거(사용자와의 계약), 요청 가능 범위(쉽게 이용 가능한 데이터·메타데이터), 연결 제품의 출시일(2026-09-12 후 출시 여부)을 따로 기록하고, 개인정보 처리 근거는 별도로 심사하는 편이 좋다. [의견][^ref-636] 특정 ROP가 데이터 보유자인지 제3자인지는 판단하지 않았다([oq-279](../../open-questions.md)·[oq-320](../../open-questions.md)).

집행위원회의 [모델 계약 조항](../../glossary/model-contractual-terms.md)·클라우드 표준 계약 조항(SCC) 권고는 2025-11-19 발표 뒤 2026-03-03 갱신 때도 초안(Draft)으로 표기되어 있다. [사실][^ref-1192] 그 부속서의 클라우드 SCC 책임 조항 설명은 면책(indemnification) 조항을 두지 않고, 한 당사자의 중대한 의무 위반으로 생긴 제3자 청구에 대한 면책을 둘지와 그 범위를 당사자가 검토하도록 권하는 것으로 보인다. [추정][^ref-1489] 이 부속서 문구는 검증 단계에서 직접 확인하지 못했다.

### 2026-10-12 보강: 변경 주체 책임 — EU 개정 제조물책임지침 조문

EU 개정 [제조물책임](../../glossary/product-liability.md)지침(Directive (EU) 2024/2853, 2024-11-18 관보)은 '제품'에 소프트웨어를 포함하고(제4조(1)), 상업 활동 밖에서 개발·공급된 자유·오픈소스 소프트웨어에는 적용하지 않는다(제2조(2)). [사실][^ref-1490] 제조자의 통제 밖에서 제품을 [실질적으로 변경](../../glossary/substantial-modification.md)한 뒤 시장에 내놓거나 사용에 투입한 자연인·법인은 그 제품의 제조자로 본다(제8조(2)). [사실][^ref-1490]

지침의 적용 대상은 2026-05-07 정오표로 '2026-12-08 후' 시장에 출시되거나 사용에 투입된 제품으로 고쳐졌으므로, 2026-12-09 당일부터 출시·투입되는 제품에 적용된다(제2조(1)). [사실][^ref-1490] 회원국 이행 기한도 2026-12-09이며(제22조(1)), 구 제조물책임지침 85/374/EEC 는 같은 날 폐지되지만 그 전에 출시·투입된 제품에는 계속 적용된다(제21조). [사실][^ref-1490] 회원국별 이행 법령은 확인하지 않았다.

손해 범위에서는 전적으로 업무 목적으로만 쓰는 재산의 손해를 보상 대상에서 뺀다(제6조(1)(b)(iii)). [사실][^ref-1490] 법원 절차의 증거 공개는 필요하고 비례적인 범위로 제한되며, 그 판단에서 제3자를 포함한 모든 당사자의 정당한 이익, 특히 기밀·영업비밀 보호를 고려한다(제9조(3)·(4)). [사실][^ref-1490]

이 페이지는 위 조문만 옮긴다. 여러 제조사 로봇에 명령을 내리는 오케스트레이션 소프트웨어가 이 지침의 제품에 해당하는지([oq-289](../../open-questions.md)), 플랫폼 설정 변경이 실질적 변경인지([oq-282](../../open-questions.md))는 판단하지 않았으며, 적용과 법적 효과 판단은 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)로 연결한다.

구축자 의견으로는, 클라우드 SCC 에 면책 조항이 없는 것으로 보인다는 점(위 추정)과 이 지침이 업무 전용 재산 손해를 보상 대상에서 빼는 점을 함께 보면, 로봇 제조사·통합자·시설 관리주체·플랫폼 사이의 제3자 청구 면책과 사업장 설비·재고 손해를 계약에서 따로 다룰 필요가 커 보인다. 그 조항을 정하는 일은 계약 당사자와 법무, 59. 법·규제·보험·라이선스 쪽이 결정할 사항이며 ROP가 정하는 일이 아니다. [의견][^ref-1489][^ref-1490] 같은 구축자 의견으로, 사고 뒤 증거 공개가 법원 판단으로 필요·비례 범위에 한정된다는 점을 전제로 로그 보관 기간·사고 후 동결·내보내기 형식·영업비밀 분리 절차를 계약 부속서에 미리 정해 두도록 계약 당사자에게 제안할 수 있고, ROP는 그 판단 근거가 되는 기록을 제공하는 쪽이다. [의견][^ref-1490]

### 2026-10-12 보강: 서비스 수준 협약 — 공개 약관 비교

아래는 업체 세 곳이 웹에 공개한 [서비스 수준 협약](../../glossary/service-level-agreement.md)·약관 문안이다. 모두 단일 업체 문안이라 개별 체결본·주문서·이행 실적은 확인하지 않았고, 업체 간 교차 확인으로 세지 않는다.

- Relay Robotics 공개 약관(2023-03-01 표기)에 따르면 서비스 개시 후 Tier 1(24시간 콜센터)은 이메일 지원 요청을 받은 뒤 60분 안에 응답하도록 상업적으로 합리적인 노력을 기울이는 조건이며, 복구 완료 시각을 보장하는 문구는 아니다. [추정] 벤더 주장[^ref-1491]
- Relay Robotics 공개 약관(2023-03-01 표기)에 따르면 고객의 네트워크나 시설(예: 승강기 고장)에서 생긴 문제는 고객이 고칠 때까지 지원 기한이 늘어나고, Relay는 그 수리 책임을 지지 않는다. [추정] 벤더 주장[^ref-1491] 시설 장애의 시작·종료를 누가 확인하는지는 약관에 없다.
- Relay Robotics 공개 약관(2023-03-01 표기)에 따르면 면책 의무, 고객의 라이선스 위반, 양측의 비밀유지 위반을 제외한 각 당사자의 책임은 청구 발생 전 18개월 동안 고객이 지급했거나 지급할 요금 총액을 넘지 않으며, 준거법은 미국 캘리포니아주법이다. [추정] 벤더 주장[^ref-1491] 국내 집행 가능성은 판단하지 않았다.
- Relay Robotics 공개 약관(2023-03-01 표기)에 따르면 당사자 사이에서 고객이 Relay와 공유하기로 한 개인정보는 고객 소유이고 Relay는 서비스 제공 목적에만 쓴다. [추정] 벤더 주장[^ref-1491] 로봇이 만든 운영 데이터 전반의 소유권을 정한 조항은 아니다.
- Formant 일반 약관(2026-04-16 갱신)에 따르면 고객이 지정한 통합자(약관 용어 'Development Consultant')는 고객의 지시로만 일하며, 고객이 그 통합자의 작위·부작위에 책임을 진다. [추정] 벤더 주장[^ref-1496]
- Formant 일반 약관(2026-04-16 갱신)에 따르면 약관이 정의한 장치(Device) 하나에 가상 환경(PLC·Jetson·가상 머신 등)이 둘 이상 있으면 가상 환경마다 별도 장치로 센다. [추정] 벤더 주장[^ref-1496] 주문서의 단가·최소 요금은 공개되지 않아 이 계수 방식이 요금에 주는 영향은 확인하지 않았다.
- Formant 일반 약관(2026-04-16 갱신)에 따르면 고객은 Formant AI 출력에 의존하거나 그 출력으로 명령을 실행하기 전에 출력을 검증하는 사람의 검토 절차를 사용 과정에 두어야 한다. [추정] 벤더 주장[^ref-1496] 업체 약관상 조건이며 로봇 AI 일반의 법적 의무는 아니다.
- AWS IoT RoboRunner 서비스 수준 협약(2022-11-28 갱신)에 따르면 500 또는 503 오류 코드를 돌려준 요청을 오류로 보고, 가용성은 5분 구간마다 오류 없이 처리된 요청 비율로 계산한다. [추정] 벤더 주장[^ref-1492] 이는 API 측정식이며 로봇 작업 성공이나 물리적 가동을 재지 않는다.
- AWS IoT RoboRunner 서비스 수준 협약(2022-11-28 갱신)에 따르면 요청이 하나도 없던 5분 구간은 가용성 100%로 간주한다. [추정] 벤더 주장[^ref-1492] 조사일(2026-10-12) 현재 이 서비스의 제공·지원 상태는 확인하지 못했다.

구축자 의견으로는, 서비스 수준 부속서가 응답 시각·원인 분석·복구 완료 시각을 나누고, 시설 장애로 지원 기한이 멈추는 구간의 시작·종료와 확인 주체를 기록하며, API 오류율과 별도로 작업 성공률·지연·시설 대기 시간을 지표로 합의하는 편이 좋다. [의견][^ref-1491][^ref-1492] 같은 구축자 의견으로, 플랫폼 약관과 고객–통합자 계약을 함께 대조해 통합자 행위의 책임 귀속, 과금 수량 단위(로봇 대수·가상 환경·설치 인스턴스)의 대응표와 계량 이의 절차, AI 출력으로 명령을 실행할 때의 검토자·승인 기록을 정하도록 계약 당사자와 법무(59. 법·규제·보험·라이선스)에 제안할 수 있으며, ROP는 합의된 지표를 측정·보고하고 승인 기록을 남기는 쪽이다. AI 출력 검토는 [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)·[47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)과 이어진다. [의견][^ref-1496][^ref-1491]

### 2026-10-12 보강: 영상 처리 위탁 관리

개인정보보호위원회는 이동형 영상정보처리기기 개인영상정보 보호·활용 안내서를 발표한 보도자료(2024-10-14)에서, 외부업체 위수탁으로 개인영상정보를 처리하면 보호책임자 지정과 주기적인 점검·교육으로 안전하게 관리하라고 당부했다. [사실][^ref-1494] 이는 감독기관의 당부이며 새 법률 의무나 ROP의 운영자·수탁자 지위 판정이 아니다([oq-259](../../open-questions.md) 열림). 상세 설계는 [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md)에서 다룬다.

구축자 의견으로는, 영상 처리를 다른 사업자에게 맡길 때 위탁 범위·보호책임자·교육·주기 점검 증빙을 계약 부속서로 관리하고, 데이터 접근 거절(영업비밀) 사유와 이의 경로를 관할별로 기록하는 편이 좋다. 관할별 영업비밀 행정 관행이 갈릴 수 있다는 점은 법학 논문이 지적한 것으로 보이는 수준이며(8절), 검증된 운영 성과로 표시하지 않는다. [의견][^ref-1494][^ref-1488]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)
- 관련 영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1192]: European Commission (Shaping Europe's digital future), Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts, 2025-11-19, https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding, 접근일 2026-10-12
[^ref-1205]: IEC / ISO (ISO/IEC JTC 1), ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts, 2016-09-21, https://webstore.iec.ch/en/publication/25920, 접근일 2026-09-30 (원문 미열람)
[^ref-1488]: De Noyette, E., Ståhler, L., Margoni, T. (IIC 56(5)), Data Secrets: The Data Act's New Trade Secrets Framework, 2025-04-24, https://link.springer.com/article/10.1007/s40319-025-01601-9, 접근일 2026-10-12 (원문 미열람)
[^ref-1489]: European Commission, ANNEX to the Communication to the Commission — Approval of the draft Commission Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts (with Annexes), C(2025) 7750 final, 2025-11-19, https://ec.europa.eu/newsroom/dae/redirection/document/121719, 접근일 2026-10-12
[^ref-1490]: European Union (EUR-Lex), Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC, 2024-11-18, https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng, 접근일 2026-10-12
[^ref-1491]: Relay Robotics, Terms of Service (Exhibit A: Service Level Agreement), 2023-03-01, https://relayrobotics.com/tos, 접근일 2026-10-12
[^ref-1492]: Amazon Web Services, AWS IoT RoboRunner Service Level Agreement, 2022-11-28, https://aws.amazon.com/roborunner/sla/, 접근일 2026-10-12
[^ref-1494]: 개인정보보호위원회, 자율주행 인공지능(AI) 발전을 위한 개인영상정보 보호ㆍ활용 기준 나왔다, 2024-10-14, https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=10678, 접근일 2026-10-12
[^ref-1496]: Formant, General Terms, 2026-04-16, https://www.formant.ai/terms_of_use, 접근일 2026-10-12
[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)
[^ref-636]: European Union (EUR-Lex), Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act), 2023-12-13, https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-01 | 58. 다사업자 책임·계약·데이터 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-12-01/pages/topics/2026/2026-10-12-area58-s11.md

```markdown
---
title: "58. 다사업자 책임·계약·데이터 — 열린 질문"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 58
related_areas: [2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: []
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#11
---

[홈](../../index.md) › [주제](../index.md) › 58. 다사업자 책임·계약·데이터 — 열린 질문

# 58. 다사업자 책임·계약·데이터 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 2026-09-30 실행에서 기존 8건에 새 질문 5건을 더했고, 2026-10-12 실행에서는 해결된 질문 없이 새 질문 3건을 올렸다. 2026-09-30 실행까지의 이 절 본문은 [2026-09-30 열린 질문 페이지](2026-09-30-area58-s11.md)에 있다.
- 이 페이지는 [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

2026-09-30 실행에서 기존 8건에 새 질문 5건을 더했고, 2026-10-12 실행에서는 해결된 질문 없이 새 질문 3건을 올렸다. 2026-09-30 실행까지의 이 절 본문은 [2026-09-30 열린 질문 페이지](2026-09-30-area58-s11.md)에 있다.

### 2026-10-12 갱신에서 더한 근거와 새 질문

이번 갱신으로 해결된 질문은 없다. 다음 질문에는 부분 근거만 더했고 상태는 모두 열림 그대로다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- oq-241: Relay·Formant 공개 약관의 책임 상한·통합자 책임 귀속 조항(6절)을 더했지만, 운영자·통합자·로봇 제조사·플랫폼 네 당사자 공통의 책임 분담표는 여전히 찾지 못했다.
- oq-268: Formant 의 가상 환경별 장치 계수, AWS IoT RoboRunner 의 가용성 측정식, Relay 의 시설 장애 예외(6절)를 더했다. 여러 사업자가 계량값을 합의하는 방식은 확인하지 못했다.
- oq-279·oq-320·oq-110: 데이터법 제2조(17)·제4조(1)·(13)과 제조사 고지의 제3자 공유 경로(4·5·6절)를 더했다. 특정 ROP의 지위는 판단하지 않았다.
- oq-280·oq-207: RFC 9745 의 폐기·종료 시각 규칙(7절)을 더했다. 로봇 계약상 최소 통지 일수는 확인하지 못했다.
- oq-259: 개인정보보호위원회의 위수탁 관리 당부(6절)를 더했다. 운영자·수탁자 지위는 판정하지 않았다.
- oq-185: 1X 사전예약 약관(5절)을 더했다. 원격 조작자의 영상 접근·사고 책임 조항은 확인하지 못했다.
- oq-249: 제조물책임지침 제9조의 증거 공개 범위(6절)를 더했다. 기계류 규정 로그 의무의 플랫폼 적용은 판단하지 않았다.
- oq-289: 제조물책임지침 제4조(1)·제8조(2) 조문(6절)을 더했다. 오케스트레이션 소프트웨어 해당 여부는 판단하지 않았다.
- oq-149: 2026년 RoMi-H 등재 공고(5절)를 더했다. 국내 사례는 찾지 못했다.

새로 올린 질문은 세 가지다. 여러 사업자가 얽힌 장애에서 서비스 수준 협약의 지원 기한을 멈추는 사유와 재개 시점을 누가 확인·승인하는가, 제조사 고지가 안내하는 제3자 지속 공유 경로가 실제로 어떤 필드를 어떤 지연으로 주고 승인 철회 뒤 언제 끊기는가, RoMi-H 등재 프로그램의 실제 운영 주기와 유효기간이 끝난 등재 통합자의 유지·복구 책임은 어떻게 이어지는가이다. 질문 번호는 열린 질문 목록에서 부여된다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)
- 관련 영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-01 | 58. 다사업자 책임·계약·데이터 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-12-01/pages/topics/2026/2026-10-12-area58-s7.md

```markdown
---
title: "58. 다사업자 책임·계약·데이터 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 58
related_areas: [2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1490, ref-636, ref-706]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#7
---

[홈](../../index.md) › [주제](../index.md) › 58. 다사업자 책임·계약·데이터 — 관련 표준·프레임워크·오픈소스

# 58. 다사업자 책임·계약·데이터 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에 걸리는 규칙은 데이터 권리(EU 데이터법·국내 산업 디지털 전환 촉진법), 인터페이스 변경(VDA 5050·Kubernetes 폐기 정책·RFC 9745), 서비스 수준·보안·기록(ISO/IEC 19086-1·IEC 62443-2-4·21 CFR Part 11), 변경 주체 책임(EU 기계류 규정·EU AI법·EU 개정 제조물책임지침)으로 나뉜다.
- 이 페이지는 [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에 걸리는 규칙은 데이터 권리(EU 데이터법·국내 산업 디지털 전환 촉진법), 인터페이스 변경(VDA 5050·Kubernetes 폐기 정책·RFC 9745), 서비스 수준·보안·기록(ISO/IEC 19086-1·IEC 62443-2-4·21 CFR Part 11), 변경 주체 책임(EU 기계류 규정·EU AI법·EU 개정 제조물책임지침)으로 나뉜다. 2026-09-30 실행까지의 이 절 본문은 [2026-09-30 관련 표준·프레임워크·오픈소스 페이지](2026-09-30-area58-s7.md)에 있다.

### 2026-10-12 보강

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| EU 데이터법 (Regulation (EU) 2023/2854) | 프레임워크 | 일반 적용일 2025-09-12와 별도로, 제3조(1) 설계 의무는 2026-09-12 후 출시되는 연결 제품·관련 서비스에 적용된다. 제4조(1)의 제공 범위는 쉽게 이용 가능한 데이터와 관련 메타데이터다 | [사실][^ref-636] |
| EU 개정 제조물책임지침 (Directive (EU) 2024/2853) | 프레임워크 | 소프트웨어를 제품에 포함하고 비상업 자유·오픈소스 소프트웨어는 제외한다. 실질적 변경자를 제조자로 본다. '2026-12-08 후', 즉 2026-12-09부터 출시·투입되는 제품에 적용되며 이행 기한과 구 지침 폐지일은 2026-12-09다. 오케스트레이션 소프트웨어 적용 여부는 판단하지 않았다([59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)) | [사실][^ref-1490] |
| IETF RFC 9745 Deprecation HTTP 응답 헤더 (2025-03) | 표준 | 폐기 예정 표시는 자원의 동작을 바꾸지 않고(§5), Sunset 시각은 Deprecation 시각보다 이를 수 없다(§4). 두 시각 사이의 최소 통지 간격은 정하지 않는다 | [사실][^ref-706] |

구축자 의견으로는, ROP 어댑터가 제조사 API의 폐기 예고 시각·종료(Sunset) 시각·전환 문서 링크를 따로 저장하고, 두 시각 사이의 최소 통지 기간은 RFC가 정하지 않으므로 계약에서 따로 확인하는 편이 좋다([API 폐기 정책](../../glossary/api-deprecation-policy.md), [oq-280](../../open-questions.md)). [의견][^ref-706]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)
- 관련 영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1490]: European Union (EUR-Lex), Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC, 2024-11-18, https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng, 접근일 2026-10-12
[^ref-636]: European Union (EUR-Lex), Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act), 2023-12-13, https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng, 접근일 2026-10-12
[^ref-706]: IETF (RFC Editor), RFC 9745: The Deprecation HTTP Response Header Field, 2025-03, https://www.rfc-editor.org/info/rfc9745/, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-01 | 58. 다사업자 책임·계약·데이터 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-12-01/pages/topics/2026/2026-10-12-area58-s8.md

```markdown
---
title: "58. 다사업자 책임·계약·데이터 — 대표 연구와 자료"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 58
related_areas: [2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1192, ref-1194, ref-1208, ref-1488]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#8
---

[홈](../../index.md) › [주제](../index.md) › 58. 다사업자 책임·계약·데이터 — 대표 연구와 자료

# 58. 다사업자 책임·계약·데이터 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 유럽연합 집행위원회, 데이터 접근·이용 모델 계약 조항과 클라우드 표준 계약 조항 권고 초안(2025) — 데이터법 이행용 계약 문안 네 벌과 클라우드 계약 조항 여섯 개를 담은 구속력 없는 초안이며, 의무적 기업 간 데이터 공유의 합리적 보상 지침은 추후 발표 예정으로 되어 있다. [사실][^ref-1192]
- 이 페이지는 [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- 유럽연합 집행위원회, 데이터 접근·이용 모델 계약 조항과 클라우드 표준 계약 조항 권고 초안(2025) — 데이터법 이행용 계약 문안 네 벌과 클라우드 계약 조항 여섯 개를 담은 구속력 없는 초안이며, 의무적 기업 간 데이터 공유의 합리적 보상 지침은 추후 발표 예정으로 되어 있다. [사실][^ref-1192]
- 산업통상부, 산업데이터 계약 가이드라인(2023) — 국내 산업데이터 거래 당사자를 위한 유의사항·표준계약서·업종별 사례를 담은 432쪽 자료다. [사실][^ref-1194]
- Shaik, A. S., Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong?(SSRN, 2026, 동료심사 전 원고) — Shaik의 제안은 로봇 제조사(OEM)·시스템 통합자·AI 공급자·운영자 사이의 책임을 통제력(피해를 막을 수 있었는가)·예견 가능성·정보 비대칭의 세 원칙으로 배분하는 위험 비례 책임 프레임워크(RPLF)이며, 저자는 이를 상업 계약과 기존 보험으로 구현할 수 있다고 주장한다. [의견][^ref-1208]

- De Noyette, E., Ståhler, L., Margoni, T., Data Secrets: The Data Act's New Trade Secrets Framework(IIC 56(5):984–1014, 2025) — 데이터법의 영업비밀 체계를 분석한 동료심사 법학 논문이며, 저자들은 회원국 관할 당국의 영업비밀 행정 관행 차이로 파편화 위험이 있다고 지적한 것으로 보인다. [추정][^ref-1488] 논문 본문은 열지 못했고 서지만 확인했다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)
- 관련 영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1192]: European Commission (Shaping Europe's digital future), Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts, 2025-11-19, https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding, 접근일 2026-10-12
[^ref-1194]: 산업통상부 (공공데이터포털), 산업통상부_산업데이터 계약 가이드라인_20230109, 2023-04-05, https://www.data.go.kr/data/15113186/fileData.do, 접근일 2026-09-30
[^ref-1208]: Shaik, A. S. (SSRN), Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong?, 2026-05-01, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6737139, 접근일 2026-09-30 (원문 미열람)
[^ref-1488]: De Noyette, E., Ståhler, L., Margoni, T. (IIC 56(5)), Data Secrets: The Data Act's New Trade Secrets Framework, 2025-04-24, https://link.springer.com/article/10.1007/s40319-025-01601-9, 접근일 2026-10-12 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-01 | 58. 다사업자 책임·계약·데이터 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-12-01/pages/topics/2026/2026-10-12-area58-s4.md

```markdown
---
title: "58. 다사업자 책임·계약·데이터 — 핵심 개념과 용어"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 58
related_areas: [2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-636]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#4
---

[홈](../../index.md) › [주제](../index.md) › 58. 다사업자 책임·계약·데이터 — 핵심 개념과 용어

# 58. 다사업자 책임·계약·데이터 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 용어는 책임이 넘어가는 조건, 데이터 권리, 인터페이스 변경 예고, 서비스 약속과 기록의 네 묶음으로 나뉜다. 2026-09-30 실행까지의 이 절 본문은 [2026-09-30 핵심 개념과 용어 페이지](2026-09-30-area58-s4.md)에 있다.
- 이 페이지는 [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 용어는 책임이 넘어가는 조건, 데이터 권리, 인터페이스 변경 예고, 서비스 약속과 기록의 네 묶음으로 나뉜다. 2026-09-30 실행까지의 이 절 본문은 [2026-09-30 핵심 개념과 용어 페이지](2026-09-30-area58-s4.md)에 있다.

### 2026-10-12 보강: 데이터 보유자와 쉽게 이용 가능한 데이터

- **[데이터 보유자](../../glossary/data-holder.md)(Data Holder, EU 데이터법)** — EU 데이터법 제4조(13)에 따르면 데이터 보유자는 쉽게 이용 가능한 데이터 가운데 비개인 데이터를 사용자와의 계약을 근거로만 이용할 수 있고, 그 데이터로 사용자의 경제 상황·자산·생산 방식을 추론해 사용자의 시장 지위를 해치는 데 쓸 수 없다. [사실][^ref-636]
- **쉽게 이용 가능한 데이터(Readily Available Data)** — 데이터법 제2조(17)은 데이터 보유자가 단순한 조작을 넘는 과도한 노력 없이 연결 제품·관련 서비스에서 적법하게 얻거나 얻을 수 있는 제품 데이터·관련 서비스 데이터로 정의한다. [사실][^ref-636]

[2026-09-30 핵심 개념과 용어 페이지](2026-09-30-area58-s4.md)의 '데이터 보유자' 항목에 있는 '사용자 동의 없이 비개인 데이터를 이용할 수 없다'는 표현은 조문이 정한 '사용자와의 계약을 근거로'와 다르므로, 이 영역은 위 정의를 기준으로 삼는다. 이 정의는 비개인 데이터에 관한 것이며, 개인정보를 처리하는 법적 근거(GDPR 제6조)는 따로 따진다. [사실][^ref-636]

정정 대상 문장은 그 페이지에 아직 남아 있으며, 다음 갱신 실행에서 그 페이지를 직접 고친다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)
- 관련 영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-636]: European Union (EUR-Lex), Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act), 2023-12-13, https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-01 | 58. 다사업자 책임·계약·데이터 의 "핵심 개념과 용어" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 17건 / 전체 1486건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-317 | 전기신문 | 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 | 미확인 | https://www.electimes.com/news/articleView.html?idxno=320147 | 2026-09-25 | 아니오 |
| ref-555 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 2023-06 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 2026-09-25 | 아니오 |
| ref-872 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART) | RoMi-H Empanelment Programme 2025 | 2025-05-01 | https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste | 2026-09-29 | 예 |
| ref-1191 | European Commission (Shaping Europe's digital future) | Data Act explained | 2025-12-15 | https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained | 2026-09-30 | 예 |
| ref-1192 | European Commission (Shaping Europe's digital future) | Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts | 2025-11-19 | https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding | 2026-09-30 | 예 |
| ref-1193 | 지디넷코리아 | 산업데이터 만든 자에게 사용·수익권 부여 | 2022-03-15 | https://zdnet.co.kr/view/?no=20220315103750 | 2026-09-30 | 예 |
| ref-1194 | 산업통상부 (공공데이터포털) | 산업통상부_산업데이터 계약 가이드라인_20230109 | 2023-04-05 | https://www.data.go.kr/data/15113186/fileData.do | 2026-09-30 | 예 |
| ref-1204 | The Kubernetes Authors | Kubernetes Deprecation Policy | 미확인 | https://kubernetes.io/docs/reference/using-api/deprecation-policy/ | 2026-09-30 | 예 |
| ref-1205 | IEC / ISO (ISO/IEC JTC 1) | ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts | 2016-09-21 | https://webstore.iec.ch/en/publication/25920 | 2026-09-30 | 아니오 |
| ref-1206 | IEC (BSI Knowledge 게재) | IEC 62443-2-4:2023 Security for industrial automation and control systems - Security program requirements for IACS service providers | 2023-12-15 | https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1 | 2026-09-30 | 아니오 |
| ref-1207 | U.S. Food and Drug Administration 규정 (Cornell Law School LII 게재) | 21 CFR § 11.10 - Controls for closed systems | 미확인 | https://www.law.cornell.edu/cfr/text/21/11.10 | 2026-09-30 | 예 |
| ref-1208 | Shaik, A. S. (SSRN) | Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong? | 2026-05-01 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6737139 | 2026-09-30 | 아니오 |
| ref-1209 | Future of Life Institute (EU AI법 조문 비공식 게재본) | Article 25: Responsibilities Along the AI Value Chain | EU Artificial Intelligence Act | 미확인 | https://artificialintelligenceact.eu/article/25/ | 2026-09-30 | 예 |
| ref-1210 | Future of Life Institute (EU AI법 조문 비공식 게재본) | Article 26: Obligations of Deployers of High-Risk AI Systems | EU Artificial Intelligence Act | 미확인 | https://artificialintelligenceact.eu/article/26/ | 2026-09-30 | 예 |
| ref-1211 | 한국아파트신문 (사설) | 공동주택에 밀려오는 로봇, 또 다른 관리책임은 없을까 | 2026-09-14 | https://www.hapt.co.kr/news/articleView.html?idxno=169488 | 2026-09-30 | 예 |
| ref-1212 | European Agency for Safety and Health at Work (EU-OSHA) | Regulation 2023/1230/EU - machinery | 미확인 | https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery | 2026-09-30 | 예 |
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

### docs/open-questions.md (요약: 대상 영역 [58] 에 걸린 18건 / 전체 393건)

```markdown
- oq-145 [열림] 언어 모델 게이트웨이의 모델 대체·라우팅 희석을 ROP 운영에서 탐지·기록하고 계약으로 막는 실무 절차나 사례가 있는가? (영역 13, 57, 58)
- oq-149 [열림] 싱가포르 공공 의료의 RoMi-H 등재 프로그램처럼 벤더·통합사를 사전 평가해 등록 자격을 주는 관문을 국내 병원·공공 현장에서 운용한 사례나 제도가 있는가? (영역 4, 63, 58)
- oq-185 [열림] 소유자가 원격 조작자를 예약해 가정 로봇을 안내하게 하는 방식(1X NEO 등)에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가? (영역 65, 53, 58)
- oq-241 [열림] 로봇 오케스트레이션 도입 계약에서 운영자·통합자·로봇 제조사·플랫폼 사업자 사이의 운영 책임을 나누는 책임 분담표나 표준 계약 조항을 공개한 사례가 있는가? (영역 2, 58)
- oq-249 [열림] EU 기계류 규정의 개입 증거 기록·안전 소프트웨어 추적 로그 요구가 개별 기계 밖에서 여러 로봇을 지시하는 오케스트레이션 플랫폼에도 미치는가, 미친다면 기록 책임은 누구에게 있는가? (영역 52, 59, 58)
- oq-259 [열림] 여러 제조사 로봇의 영상과 위치 정보를 모아 관제하는 플랫폼 사업자는 개인정보 보호법상 이동형 영상정보처리기기 운영자인가, 현장 운영 사업자의 수탁자인가, 그리고 촬영 표시·거부 의사 처리 의무는 누구에게 있는가? (영역 53, 58)
- oq-265 [열림] ANSI/A3 R15.08-3-2026 이 사용자에게 요구하는 운영 절차·교육·변경 관리 항목은 무엇이며, 여러 제조사 로봇을 함께 쓰는 현장에서 누가 이를 이행하는가? (영역 40, 50, 58)
- oq-268 [열림] 사용량 기반 서비스형 로봇 계약에서 과금·최소 요금·가동률 미달을 판정하는 계량 데이터를 누가 측정하고, 여러 사업자가 함께 쓰는 현장에서 그 값을 어떻게 합의하는가? (영역 3, 58, 39)
- oq-279 [열림] 여러 제조사 로봇의 운영 데이터를 모으는 오케스트레이션 플랫폼 사업자는 EU 데이터법상 데이터 보유자인가, 사용자가 지정한 제3자 데이터 수령자인가, 그리고 그에 따라 제조사에게 데이터 제공을 요구할 수 있는 범위는 어디까지인가? (영역 58, 59)
- oq-280 [열림] 로봇 제조사·관제 API 의 주 버전 변경이나 폐기를 오케스트레이션 플랫폼에 사전 통지하는 기간과 유예 기간을 계약이나 인터페이스 표준에 명시한 공개 사례가 있는가? (영역 58, 20, 57)
- oq-281 [열림] 국내 산업데이터 계약 가이드라인의 표준계약서와 업종별 사례가 로봇 운영 데이터(지도·작업 이력·센서 로그)처럼 여러 사업자가 함께 만드는 데이터를 어떻게 다루는가? (영역 58, 15)
- oq-282 [열림] 오케스트레이션 플랫폼에서 경로망·속도 제한·작업 규칙 같은 설정을 바꾸는 일이 EU 기계류 규정의 실질적 변경에 해당해 플랫폼 운영자나 통합자가 제조자 의무를 지는 경우가 있는가? (영역 58, 59, 48)
- oq-283 [열림] 로봇-승강기 연동 표준 과제의 결과물(표준 번호, 연동 장애 시 승강기 제조사·로봇 제조사·관제 사업자의 책임 분담)이 공개되었는가? (영역 58, 22)
- oq-289 [열림] EU 개정 제조물책임지침에서 여러 제조사 로봇에 명령을 내리는 오케스트레이션 소프트웨어는 결함 제품이나 관련 서비스로 다뤄지는가, 그 소프트웨어의 설정·기능 변경이 실질적 변경에 해당해 플랫폼 사업자가 제조자로 간주될 수 있는가? (영역 59, 58)
- oq-290 [열림] 국내 제조물책임법에 소프트웨어를 제조물로 포함하는 개정안이 발의되거나 통과되었는가, 그리고 로봇 관제·오케스트레이션 소프트웨어의 결함 사고에 관한 국내 판례가 있는가? (영역 59, 58)
- oq-313 [열림] 실외이동로봇의 운행안전인증 단위에 관제장치가 포함될 때, 관제를 맡는 오케스트레이션 플랫폼 사업자도 지능형로봇법의 운영자 보험 가입 의무 대상이 되는가? (영역 59, 58, 66)
- oq-320 [열림] EU 데이터법에서 여러 제조사 로봇의 데이터를 모아 관제하는 오케스트레이션 플랫폼 사업자는 사용자·제3자·데이터 보유자 가운데 어느 지위이며, 제조사에 로봇 데이터 제공을 요구할 수 있는가? (관련: oq-259) (영역 58, 53)
- oq-338 [열림] 로봇 플랫폼 사업자와 현장 운영자가 각각 EU AI Act 의 제공자·배포자가 될 때 실행 기록의 통제권과 6개월 이상 보관 책임을 계약으로 나눈 공개 사례나 지침이 있는가? (영역 43, 58, 59)
```

### runs/2026-10-12-01/verification2.json

```json
{
  "run_id": "2026-10-12-01",
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
    "ok": false,
    "overlaps": [
      "세부영역 페이지 4·6·7·11절이 새 분리 페이지(2026-10-12-area58-s4·s6·s7·s11)로만 연결되고, 2026-09-30 실행에서 분리·게시된 같은 절 페이지(2026-09-30-area58-s4·s6·s7·s11)로 가는 링크가 사라졌다. 제목이 같은 주제 페이지가 둘씩 생기고, 검증을 마친 기존 본문(용어 목록, 대표 접근법 2,613자, 표준 표, 열린 질문 목록)이 세부영역 페이지에서 닿지 않는다",
      "2026-10-12-area58-s4.md 의 '위 주제 페이지의 데이터 보유자 항목'은 링크 없이 가리키는 표현이다. 정정 대상인 2026-09-30-area58-s4.md 40행의 '사용자 동의 없이' [사실] 문장은 게시된 채 남는다(1차 수정 지시 12의 부분 이행. additional_research_requests 로 넘긴 것은 인정한다)",
      "2026-10-12-area58-s7.md 에 데이터법 행이 새로 생겼다. 2026-09-30-area58-s7.md 41행의 기존 데이터법 행과 나뉘어 있다(후속 정리 요청으로 인정한다)"
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
    "4·6·7·11절 패치(세부영역 페이지): 각 절 patch content 맨 앞에 2026-09-30 분리 페이지로 가는 연결 문장을 넣는다. 예: '2026-09-30 실행까지의 이 절 본문은 [58. 다사업자 책임·계약·데이터 — 핵심 개념과 용어(2026-09-30)](../../topics/2026/2026-09-30-area58-s4.md)에 있다.' 6절은 2026-09-30-area58-s6.md, 7절은 2026-09-30-area58-s7.md, 11절은 2026-09-30-area58-s11.md 로 연결한다. 자동 분리 코드가 지울 수 있으므로 '자세한 내용은 주제 페이지'로 시작하지 않는 문장으로 쓴다. 이유: 재분리 과정에서 기존 분리 페이지로 가는 링크가 사라져, 검증·게시된 기존 본문이 세부영역 페이지에서 닿지 않는다.",
    "4절 패치: '위 주제 페이지의 데이터 보유자 항목에 있는 …' 문장의 '위 주제 페이지'를 [2026-09-30 핵심 개념과 용어 페이지](../../topics/2026/2026-09-30-area58-s4.md) 링크로 바꾼다. 이유: 새 분리 페이지에서 가리키는 대상이 보이지 않는다. 정정 대상 문장은 그 페이지에 남아 있고 다음 갱신에서 고친다는 것도 한 문장(태그 없음)으로 밝힌다.",
    "11절: action 을 replace 로 바꾸고, 첫 문장 '이 영역에 걸린 기존 열린 질문 8건은 모두 열려 있고, 이번 실행에서 새 질문 5건을 올렸다.'를 실행별로 고쳐 쓴다. 예: '2026-09-30 실행에서 기존 8건에 새 질문 5건을 더했고, 2026-10-12 실행에서는 해결된 질문 없이 새 질문 3건을 올렸다.' 이어서 1번 지시의 연결 문장과 기존 append 내용을 그대로 둔다. 이유: 이 문장이 2026-10-12 분리 페이지 첫머리에 옮겨져, 이번 실행이 5건을 올린 것처럼 읽힌다.",
    "6절 서비스 수준 협약 소절의 Formant 둘째 항목: '과금 단위인 장치(Device) 하나에'에서 '과금 단위인'을 지우고 '약관이 정의한 장치(Device) 하나에'처럼 쓴다. 이유: f24 는 Device 계수 정의만 담고 과금 영향은 확인하지 않았다고 밝힌다. Device 를 과금 단위로 단정하면 브리프 밖 주장(드리프트)이 된다.",
    "7절 패치: 절 첫 문장(규칙 묶음 나열)의 '변경 주체 책임(EU 기계류 규정·EU AI법)'에 EU 개정 제조물책임지침을 더하고, '인터페이스 변경(VDA 5050·Kubernetes 폐기 정책)'에 RFC 9745 를 더한다. 이유: 이번에 추가한 표 행이 절 요약에서 빠져 세부영역 페이지 7절 요약과 내용이 어긋난다. action 은 replace 로 하고 기존 append 내용을 그대로 둔다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 36건, 미확인 2건, 교차 확인 0건. 강등: f4 사실 → 추정(권고 초안 부속서 X 의 면책 문구 미확인), f18 사실 → 추정(논문 본문 미열람). 원문 미열람 출처: ref-1488. 주의: EU 데이터법(제2조(17)·제4조(1)·(13)·제50조), 개정 제조물책임지침(제2·4·6·8·9·21·22조, 2026-05-07 정오표), RFC 9745, RoMi-H 2025·2026 공고, 개인정보보호위원회 보도자료는 원문으로 확인했으나 모두 단일 출처다. Relay·Formant·AIRROBO·AWS·1X 의 약관·고지는 각 업체가 공개한 문안이며 벤더 주장이다. 2025 공고의 'bi-annual'은 연 2회로도 2년마다로도 읽혀 확정하지 않는다. 제조물책임지침이 오케스트레이션 소프트웨어에 적용되는지는 판단하지 않았다. 정정 요청 없음. 2차: 1차 수정 지시 19건 가운데 18건을 이행했고, 4절 정정(2026-09-30-area58-s4.md 40행)은 입력 밖이라 부분 이행하고 후속 요청으로 넘겼다. 드리프트 1건(Formant Device 를 '과금 단위'로 단정)은 삭제를 지시했다. [분류원문] 보존, 섹션 순서 준수. 링크: 재분리 과정에서 2026-09-30 분리 페이지 4건(4·6·7·11절)으로 가는 연결이 끊겨 복구를 지시했다. 11절 첫 문장의 질문 건수가 실행 기준과 맞지 않아 고치게 했다. 참고: 자동 분리 코드가 이미 분리된 절을 다시 나눌 때 기존 분리 페이지 링크를 새 페이지로 옮기도록 pipeline 담당에게 요청한다. reference_updates 의 cited_by 에 분리 주제 페이지가 빠져 있는 점은 퍼블리셔 자동 영역에서 확인할 일이다.",
  "retry_reason": null
}
```
