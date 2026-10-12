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
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
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

### docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md (요약)

```markdown
# 60. 노동·수용성·접근성

소속 대분류: P. 거버넌스·법규·사회 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

노동 영향·사회적 수용성, 고령자·장애인·어린이 접근성 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **노동 영향·사회적 수용성**: 일자리와 일하는 방식의 변화, 로봇에 대한 사회적 수용성을 다룬다
- **접근성·포용**: 고령자·장애인·어린이도 로봇 서비스를 안전하게 쓰고 피할 수 있게 한다

## 2. 핵심 질문

로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? [분류원문]
```

### docs/categories/planning-and-business/use-cases-requirements-and-scope.md (요약)

```markdown
# 2. 사용 사례·요구·책임 범위

소속 대분류: A. 기획·사업 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

로봇에게 맡길 일과 현장 유형별 요구, 플랫폼이 직접 맡을 범위와 외부에 맡길 범위를 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **책임 범위 정의**: 플랫폼이 직접 맡을 범위와 외부(업무 시스템·로봇 자체 지능·설비 제어·현장 간 운송·업종별 조건)에 맡길 범위를 정한다
- **사용 사례 발굴·요구 정의**: 로봇에게 맡길 일과 성공 기준·수용 기준을 정한다
- **현장 유형별 요구 정리**: 물류창고·제조 공장·병원·상업 시설·가정·실외 같은 현장 유형마다 공통 요구와 고유 요구를 정리한다

## 2. 핵심 질문

로봇에게 어떤 일을 맡기고, 플랫폼은 그중 어디까지 직접 책임질 것인가? [분류원문]
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

### docs/categories/integration/robot-and-vendor-fleet-manager-integration.md (요약)

```markdown
# 20. 로봇·제조사 관제 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

## 1. 한 줄 정의

제조사 API·SDK·관제 시스템과 연결하는 어댑터, 공통 명령·관측 계약, 로봇과 주고받는 통신 방식 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇·제조사 관제 연동 어댑터**: 제조사 API·SDK·관제 시스템을 연결해 명령·상태·오류를 변환하는 어댑터를 만든다
- **제어 위임 수준 결정**: 로봇을 하나씩 직접 제어할지, 제조사 관제에 임무 단위로 맡길지 정한다
- **공통 명령·관측 계약**: 단위와 시각 기준을 명시한 제조사 중립 명령·관측 형식을 정한다
- **로봇 통신 방식·메시징**: 명령·상태·지도·영상 데이터를 어떤 통신 방식(MQTT·DDS·gRPC·WebRTC 등)과 주기로 주고받을지 정하고 끊김·지연에 대비한다

이전 분류(2026-09-24)에서 이 페이지는 옛 9번 영역 ‘로봇·제조사 관제 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 [옛 분류원문]

> 옛 질문: 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? [옛 분류원문]

## 2. 핵심 질문

로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? [분류원문]
```

### docs/categories/integration/interoperability-standards-and-conformance.md (요약)

```markdown
# 21. 상호운용 표준·적합성

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-11 · 버전: 3

## 1. 한 줄 정의

로봇 상호운용 표준을 채택·변환하고 적합성을 시험한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상호운용 표준 채택**: VDA 5050·MassRobotics 상호운용 표준·Open-RMF·ROS 2·OPC UA 같은 표준을 채택하고 서로 변환한다
- **적합성 시험**: 표준과 연동 규격을 지키는지 시험한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 28번 영역 ‘표준·상호운용성·다사업자 거버넌스’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [옛 분류원문]

> 옛 질문: 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [옛 분류원문]

## 2. 핵심 질문

어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]
```

### docs/categories/integration/facility-and-building-system-integration.md (요약)

```markdown
# 22. 설비·건물 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-11 · 버전: 3

## 1. 한 줄 정의

문·승강기·출입통제·컨베이어·PLC·고정 센서와 작업을 연계한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **설비·건물 연동**: 문·승강기·출입통제·컨베이어·자동창고·PLC·빌딩 관리 시스템과 작업을 연계한다
- **승강기·문 예약과 연동**: 승강기와 문을 예약하고 로봇의 진입과 설비 상태를 맞물려 확인한다
- **로봇–설비 작업 동기화**: 컨베이어·작업대 준비와 로봇 도착처럼 설비와 로봇의 시점을 맞춘다
- **IoT·고정 센서 연동**: 고정 카메라·출입 센서·환경 센서처럼 로봇 밖의 센서 데이터를 연결한다

이전 분류(2026-09-24)에서 이 페이지는 옛 10번 영역 ‘설비·건물 시스템 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 [옛 분류원문]

> 옛 질문: 컨베이어 준비와 로봇 도착을 어떻게 맞출까? [옛 분류원문]

## 2. 핵심 질문

문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? [분류원문]
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

### docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md (요약)

```markdown
# 47. AI·학습·적응과 모델 운영

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

AI 결과를 실행에 쓰는 기준과 불확실성, 모델 운영 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **AI 결과의 실행 사용 기준**: AI가 만든 계획·해석을 어떤 기준으로 실행에 쓸지 정하고 불확실성을 평가한다
- **모델 운영**: 모델 버전·학습 데이터·배포·성능 감시를 관리한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [44. 로봇 기반 모델·언어 모델 계획](robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](prediction-and-learning-based-optimization.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 27번 영역 ‘AI·학습·적응과 모델 운영’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 [옛 분류원문]

> 옛 질문: AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]
```

### docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md (요약)

```markdown
# 52. 통신 보호·위협 관리·감사

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

통신 보호, 위협 모델·취약점, 문서·대화 입력 보안, 감사 기록 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **통신 보호**: 로봇·플랫폼·설비 사이 통신을 암호화하고 무결성을 지킨다(ROS 2 보안 등)
- **보안 위협 모델·취약점 관리**: 위협 모델을 세우고 취약점을 찾아 고친다(ROS 2 위협 모델, IEC 62443 등)
- **문서·대화 입력 보안**: 문서나 대화에 숨은 지시를 명령으로 실행하지 않게 막는다(프롬프트 주입 방지)
- **명령·승인 감사 기록**: 누가 언제 무엇을 지시·승인·변경했는지 지울 수 없게 기록한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

통신·문서·대화를 통한 공격이 로봇 동작으로 이어지지 않게 하려면? [분류원문]
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

### docs/categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md (요약)

```markdown
# 57. 자산·소프트웨어 수명주기 관리

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

정비·고장 예측, 버전 관리, 장비 교체, 폐기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **정비·고장 예측**: 고장을 예측하고 예방 정비를 계획하며 배터리 열화를 관리한다
- **소프트웨어·펌웨어·어댑터 버전 관리**: 펌웨어·어댑터·지도·모델 버전의 호환을 관리하고, 바뀔 때 다시 검증할 범위를 정하며 배포·복구한다
- **장비 교체**: 로봇을 바꿀 때 설정·지도·능력 정의를 새 장비로 옮긴다
- **폐기·데이터 삭제**: 로봇과 시스템을 폐기할 때 데이터를 지우고 자산을 처리한다

이전 분류(2026-09-24)에서 이 페이지는 옛 24번 영역 ‘자산·소프트웨어 수명주기 관리’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 [옛 분류원문]

> 옛 질문: 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [옛 분류원문]

## 2. 핵심 질문

제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]
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

### docs/categories/site-type-applications/home-and-apartment.md (요약)

```markdown
# 65. 가정·공동주택

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

집안일 보조, 공동주택 배송, 사생활 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **가정·공동주택 적용**: 집안일 보조(정리·청소·세탁)와 공동주택 배송(승강기·공동현관), 거주자의 사생활을 다룬다

## 2. 핵심 질문

가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가? [분류원문]
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

### runs/2026-10-11-05/research.md

```markdown
# 리서치 브리프 2026-10-11-05

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-11-05 |
| 날짜 | 2026-10-11 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 49. 사람 근접 안전 |
| 대분류 | M. 안전 |

## 갭(비어 있거나 약한 섹션)

- 섹션 4. 핵심 개념과 용어(분리 2026-09-30-area49-s4) — NIST SSM 논문 연도를 '2016' 으로 적어 학술지 게재 연도(2017)와 다름
- 섹션 5. 적용 사례 — 병원 사례를 '시뮬레이션 평가' 로 잘못 분류(89행), 창고 연구(74행)는 '정량 결과 미확인', 아마존 글 '발행일 미확인'(72행), 실외 사례 제약 칸(100행)이 2023 기사의 '당시 개정안' 수치에만 기대고 현행 고시 원문 근거가 없음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area49-s6) — 구역 지원 신고·적재 외곽 기준 진입, Nav2·RMF 의 0 값 의미 차이, 감지 응답시간 보정 요인이 없고, Farrell(55행)·Jafari(61행) 문장이 실험 조건을 '미확인' 으로 둠
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area49-s7) — 실외 인증 행이 인증기관 페이지·기사 근거뿐이고 시행규칙·고시 원조문이 없음. ISO 13482:2014·ISO 10218-1:2025 범위·국내 실내 KS(KS B 8252) 행 없음
- 섹션 8. 대표 연구와 자료(분리 2026-09-30-area49-s8) — Farrell·HATA·Jafari 서지가 프리프린트 기준이고 Rondoni 제목·환경 표현 부정확, HATA 평가가 시뮬레이션이라는 점과 실패율 정의 없음
- 섹션 9. 책임 경계 — 사람 위치를 플릿에 전달하는 공개 구현과 그 한계(좌표계·변환 실패), 실외 인증의 운행계획서·보행자 밀집 알림 요구 미반영
- 섹션 11. 열린 질문 — oq-229·oq-230·oq-231·oq-232 부분 근거 미반영
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정 5건(f1·f14·f20·f24·f49)

## 조사 질문

1. 사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]
2. oq-229 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가? (섹션 6·9·11 겨냥)
3. oq-230 출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? (섹션 5·7·11 겨냥)
4. oq-231 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가? (섹션 7·11 겨냥)
5. oq-232 착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가? (섹션 9·11 겨냥)
6. 바뀐 출처: 병원·창고·편안함 연구의 실험 조건과 출판 서지, 현행 실외 인증 고시 별표의 실제 기준은 무엇인가? (섹션 5·8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Marvel·Norcross(NIST)의 SSM 논문 학술지판은 Robotics and Computer-Integrated Manufacturing 44권(2017) 144–155쪽에 실렸고, 2015-03-04 접수·2016-08-01 승인됐다. 위키 4절·8절과 분리 페이지의 '2016년 논문' 표기는 승인 연도 기준이라 게재 연도(2017)와 다르다. | ref-1075 | 아니오 | medium | 2026-10-11 | — | — |
| f2 | [추정] | SICK 의 기술 블로그는 안전 레이저 스캐너에서 감시 케이스(보호 필드 집합) 사이를 전환하면 시스템 응답시간이 늘어나고, 다중 샘플링 값을 올리면 물체가 연속으로 더 여러 번 감지돼야 출력이 꺼지므로 응답시간 보정분이 더해진다고 설명한다. | ref-1466 | 아니오 | low | 2026-10-11 | 제약 | 벤더 주장 |
| f3 | [사실] | VDA 5050 3.0.0 은 로봇마다 처리할 수 있는 구역 유형이 다르므로, 모든 이동 로봇이 이해할 수 있는 구역 이름을 factsheet 의 typeSpecifications.supportedZones 배열로 플릿 관제에 보고하도록 요구한다(shall). | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f4 | [사실] | 같은 명세의 외곽 기준 구역(contour-based zones)에서는 적재물을 포함한 로봇 외곽이 구역 진입·이탈을 정하며, 외곽의 어느 부분이라도 구역에 들어가면 진입이고 외곽이 모두 빠져나가야 이탈이다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f5 | [의견] | ROP 가 구역 속도 제한을 등록할 때는 로봇별 supportedZones 신고를 먼저 확인하고, 적재물로 커진 외곽이 진입 경계에 닿기 전에 감속을 마치도록 감속 시작 지점을 경계 앞에 두며, 실제 감속을 통합 시험으로 확인하는 절차가 필요하다. | ref-031 | 아니오 | low | 2026-10-11 | 제약 | — |
| f6 | [사실] | Nav2(Jazzy) Collision Monitor 문서는 source_timeout(기본 2.0초) 안에 새 센서 데이터가 오지 않으면 로봇을 정지시키며, source_timeout 을 0.0 으로 두면 이 차단 동작이 꺼진다고 설명한다. | ref-1467 | 아니오 | medium | 2026-10-11 | — | — |
| f7 | [사실] | Nav2(Jazzy) Speed Filter 에서 speed_limit 메시지 값 0 은 정지가 아니라 '속도 제한 없음'을 뜻하며, 이는 백분율·절댓값 설정과 관계없다. | ref-1468 | 아니오 | medium | 2026-10-11 | — | — |
| f8 | [사실] | Open-RMF rmf_fleet_adapter 2.14.0 의 차선 속도 제한(limit_lane_speeds) 처리는 요청 속도가 0 이하이거나 차선 번호가 그래프 범위를 벗어나면 경고만 남기고 그 요청을 무시하며, 경고문은 차선을 닫으려면 close_lanes API 를 쓰라고 안내한다. | ref-1464 | 아니오 | medium | 2026-10-11 | — | — |
| f9 | [사실] | 같은 코드에서 유효한 속도 제한은 계획 그래프의 차선 속성(speed_limit)에 기록된 뒤 새 Planner 를 만들어 작업 파라미터에 넘기고 차선 상태를 발행하는 데서 끝나며, 차량이 실제로 감속을 마쳤는지 확인하는 경로는 이 함수에 없다. | ref-1464 | 아니오 | medium | 2026-10-11 | — | — |
| f10 | [추정] | Nav2 의 speed_limit 0(제한 없음)·source_timeout 0.0(차단 해제)과 Open-RMF 의 0 이하 속도 제한(무시) 모두 '정지'를 뜻하지 않으므로, 이종 플릿 어댑터가 '0' 을 정지 명령으로 그대로 옮기면 의도와 반대로 제한이 풀리거나 무시될 수 있는 것으로 보인다. | ref-1467, ref-1468, ref-1464 | 아니오 | low | 2026-10-11 | 제약 | — |
| f11 | [의견] | ROP 어댑터 계약은 '제한 없음', '양수 속도 제한', '통로 폐쇄', '보호 정지'를 서로 다른 명령으로 표현하고, 구역 전송·활성화·계획 반영·차량 감속 관측을 별개 상태로 기록해 계획 상태 갱신만으로 감속 완료를 보고하지 않도록 해야 한다. | ref-1464, ref-1468, ref-031 | 아니오 | low | 2026-10-11 | 제약 | — |
| f12 | [사실] | Farrell 외의 창고 연구는 Freight·Jackal·Megarover 실물 로봇으로 실험했고, 로봇과 보행자 위치는 OptiTrack 모션 캡처로 측정했다. 정적·동적 장애물 회피 단위 실험은 설정마다 10회 수행했다. | ref-1082 | 아니오 | medium | 2026-10-11 | 물류창고 / 수행 자원 | — |
| f13 | [사실] | 같은 연구의 Open-RMF 플릿 실험(Table IV)은 로봇 4대·최고 1.0 m/s 또는 2대·1.5 m/s 설정에서 보행자 0·1·2명 조건을 비교했고, 표의 값은 Open-RMF 상위 계획기가 로봇을 일부러 세워 둔 시간을 뺀 것이다. | ref-1082 | 아니오 | medium | 2026-10-11 | 물류창고 / 예외·성과 | — |
| f14 | [추정] | 정정 제안: 49영역 본문 74행('정량 결과는 미확인')·2026-09-30-area49-s6.md 55행('정량 결과 미확인')·2026-09-30-area49-s8.md 42행('2025-03, 프리프린트 … 정량 결과 미확인')은 실물 실험 조건(f12)과 Table IV 조건·분모(f13)를 적고, 서지를 2025 IEEE CASE(pp.548–555, 2025-08-17) 게재로 고치는 것이 맞아 보인다. 현장 배치 사례가 아니라 연구 평가라는 기존 구분은 유지한다. | ref-1082 | 아니오 | medium | 2026-10-11 | 물류창고 / 예외·성과 | — |
| f15 | [사실] | HATA(Kazemi Eskeri 외) 논문의 5·10·15대 플릿 평가는 실제 기록된 사람 궤적을 재생하는 시뮬레이션 환경에서 수행됐다. | ref-1083 | 아니오 | medium | 2026-10-11 | — | — |
| f16 | [사실] | 같은 논문의 실패율은 교착 또는 10분 제한시간 초과로 완료하지 못한 과제의 비율로, 사고율이나 사람과의 충돌률이 아니다. | ref-1083 | 아니오 | medium | 2026-10-11 | — | — |
| f17 | [사실] | Tartu 병원 현장 시험 논문은 TIAGo·Clearpath Jackal 이종 로봇을 RMF 로 관리하는 능력을 '시험 환경'에서 검증했고, 병원 안에서 여러 배송 로봇을 운용하는 것은 아직 하지 않은 향후 과제로 적었다. | ref-869 | 아니오 | medium | 2026-10-11 | 병원 / 수행 자원 | — |
| f18 | [사실] | Rondoni 외(Scientific Reports, 2024-08-07)의 병원 주행 벤치마크는 컴퓨터 시뮬레이션이 아니라, 병상·복도·대기 공간·가구 등 실제 병원의 물리적 배치를 재현한 모의 병원 공간에서 HOSBOT·TIAGo 실물 로봇으로 수행됐고 Vicon 카메라 8대로 위치를 측정했다. | ref-1081 | 아니오 | medium | 2026-10-11 | 병원 / 작업 대상 | — |
| f19 | [사실] | 같은 연구의 이동 장애물은 사람이 아니라 정해진 경로를 고정 선속도·각속도로 원격조종해 움직인 두 번째 시험용 이동 로봇 베이스였다. | ref-1081 | 아니오 | medium | 2026-10-11 | 병원 / 제약 | — |
| f20 | [추정] | 정정 제안: 49영역 본문 89행 '이 사례는 실제 병원이 아닌 모의 병원 환경에서 수행한 시뮬레이션 평가다' 는 '실제 병원 구조를 재현한 모의 병원 공간에서 실물 로봇으로 수행한 실험 평가(이동 장애물은 원격조종 로봇)' 로 고치는 것이 맞아 보인다. 2026-09-30-area49-s8.md 41행의 논문 제목도 원문대로 단수 'hospital environment' 로 맞춘다. | ref-1081 | 아니오 | medium | 2026-10-11 | 병원 / 작업 대상 | — |
| f21 | [사실] | Jafari·Nguyen·Liu 의 보행자 편안함 실험 참가자는 23~41세 자원자 32명(남 22·여 10)이었고, 폭 3.2 m 복도에서 원격조종 로봇이 1.4·2.8 m/s 로 움직였으며, 160회 시행 중 데이터 수집이 완전히 실패한 2회를 뺐다(측면 거리 관련 분석은 13회를 더 뺐다). | ref-1085 | 아니오 | medium | 2026-10-11 | 작업 대상 | — |
| f22 | [사실] | 같은 연구의 복합 예측기는 분석에 쓴 데이터와 같은 데이터로 평가돼, 독립 시험 집합에서의 성능은 아니다. | ref-1085 | 아니오 | medium | 2026-10-11 | — | — |
| f23 | [사실] | 논문의 오즈비 3.67 은 복합 예측기가 '편안함'으로 예측했을 때 실제로 편안했을 오즈가 그렇지 않게 예측했을 때보다 3.67배라는 뜻으로, 사고 감소 확률이나 안전 거리 기준이 아니다. | ref-1085 | 아니오 | medium | 2026-10-11 | — | — |
| f24 | [추정] | 정정 제안: 2026-09-30-area49-s6.md 61행의 '(실험 장소·참가자 수 미확인)' 은 참가자 32명·3.2 m 복도·원격조종 로봇·1.4/2.8 m/s 조건(f21)과 같은 데이터 평가 한계(f22)로 바꾸고, 2026-09-30-area49-s8.md 40행의 '(2026-04, 프리프린트)' 는 'ICRA 2026 채택(arXiv 저자판)' 으로 고치는 것이 맞아 보인다. | ref-1085 | 아니오 | medium | 2026-10-11 | — | — |
| f25 | [사실] | 지능형 로봇 개발 및 보급 촉진법 시행규칙 제7조의4제1항은 운행안전인증 기준으로 로봇의 최대 질량(적재물 포함) 500 kg 이하(1호)와 최대 속도 시속 15 km 이하(2호)를 정하고, 제2항은 그 밖의 세부사항을 산업통상부장관 고시로 위임한다. | ref-1470 | 아니오 | medium | 2026-10-11 | 실외 / 제약 | — |
| f26 | [사실] | 같은 시행규칙 제7조의5제1항은 운행안전인증 신청서에 횡단보도 통행방식, 통신장애 대응 시나리오, 사고발생 대응 시나리오, 혼잡상황 대응 시나리오 등을 담은 운행계획서를 첨부해 제출하도록 한다(4호). | ref-1470 | 아니오 | medium | 2026-10-11 | 실외 / 시작 조건 | — |
| f27 | [사실] | 현행 「실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시」는 산업통상부고시 제2025-21호(2025-11-24 일부개정)이며 부칙에 따라 발령한 날부터 시행하고, 제4조는 운행안전인증 기준을 별표 3 으로 정한다. | ref-1469 | 아니오 | medium | 2026-10-11 | 실외 | — |
| f28 | [사실] | 고시 제2025-21호 별표 3(실외이동로봇 운행안전인증 기준)의 상위 항목은 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치의 8개이며, 한국로봇산업진흥원 인증 안내 페이지의 '총 8개 심사항목' 이름과 같다. | ref-1469, ref-980 | 아니오 | medium | 2026-10-11 | 실외 | — |
| f29 | [사실] | 별표 3 의 1.규격 및 운행속도는 로봇과 적재물 질량 합계 500 kg 초과를 금지하고, 최대 운행 속도를 질량 230 kg 초과 500 kg 이하 5 km/h, 100 kg 초과 230 kg 이하 10 km/h, 100 kg 이하 15 km/h 로 정한다. | ref-1469 | 아니오 | medium | 2026-10-11 | 실외 / 제약 | — |
| f30 | [사실] | 별표 3 1.라는 도로교통법상 어린이 보호구역·노인 보호구역·장애인 보호구역에서 로봇이 최대 운행 속도 5 km/h 를 지키는지 확인하도록 한다. | ref-1469 | 아니오 | medium | 2026-10-11 | 실외 / 제약 | — |
| f31 | [사실] | 별표 3 4.주변 인식은 로봇이 지정된 운행구역을 지키고 제한된 금지구역에 들어가지 않을 것(가), 사람이나 장애물을 감지해 안전하게 감속·정지 또는 회피할 것(다)을 요구하며, 다목의 평가 방법은 KS B 7320 의 5.6절(장애물 감지와 회피)을 따른다. | ref-1469 | 아니오 | medium | 2026-10-11 | 실외 / 제약 | — |
| f32 | [사실] | 별표 3 7.횡단보도 통행은 대기 장소에 도착했을 때 보행 신호가 이미 켜져 있으면 정지 상태로 기다렸다가 다음 보행 신호에 횡단하도록 하고(가.3), 횡단 중 통신이 끊기면 횡단을 마친 뒤 안전한 곳에 정차하도록 한다(나). | ref-1469 | 아니오 | medium | 2026-10-11 | 실외 / 제약 | — |
| f33 | [사실] | 별표 3 8.관제장치 다목은 주행 경로가 보행자 밀집 등으로 통행할 수 없으면 로봇이 관제장치에 알리고 관리자가 조치할 수 있어야 한다고 정한다. | ref-1469 | 아니오 | medium | 2026-10-11 | 실외 / 예외·성과 | — |
| f34 | [추정] | 49영역 본문 5절 실외 사례 제약 칸(100행)이 2023-07-28 기사의 '당시 개정안'으로 전한 질량별 속도 구간(230·100 kg 경계, 5·10·15 km/h)과 횡단보도 대기 규칙은 현행 고시 제2025-21호 별표 3 의 값과 같으므로, 현행 고시 원문을 근거로 바꿔 쓰고 보호구역 5 km/h 를 덧붙일 수 있어 보인다. | ref-1469, ref-992 | 아니오 | medium | 2026-10-11 | 실외 / 제약 | — |
| f35 | [의견] | ROP 가 실외 로봇의 관제 역할을 맡으면, 운행계획서의 통신장애·혼잡 대응 시나리오와 별표 3 8.다의 보행자 밀집 알림·관리자 조치, 보호구역 5 km/h 를 구역별 속도 제한 정책과 알림 흐름으로 연결해 두는 것이 필요하다. | ref-1469, ref-1470 | 아니오 | low | 2026-10-11 | 실외 / 예외·성과 | — |
| f36 | [사실] | ISS(세르비아 표준원)가 제공하는 ISO 프로젝트 정보에서 ISO 13482:2014 는 2014-02-03 발행, 현재 단계 90.92(개정 예정)의 발행 표준(Published)으로 표시된다. | ref-1471 | 아니오 | medium | 2026-10-11 | — | — |
| f37 | [사실] | ISS 가 제공하는 ISO 10218-1:2025(2025-02-05 발행) 적용 범위는 로봇·매니퓰레이터가 무인 산업용 트럭이나 이동 플랫폼에 고정되거나 그 일부일 때의 이동성(mobility) 관련 위험을 이 문서가 다루지 않는다고 적는다. | ref-1472 | 아니오 | medium | 2026-10-11 | — | — |
| f38 | [사실] | 국가표준 KS B 8252 '실내 이동로봇의 보호정지 시험방법'은 안전한 실내 공간에서 이동 로봇이 자율 주행할 때 정적 장애물에 대한 보호정지를 평가하는 시험방법 표준으로 ISO 13482 를 기반으로 하며, 2020-02-26 제정(고시 2020-0026)·2025-09-05 확인(고시 2025-0241, 5년 도래 확인)됐다. | ref-1473 | 아니오 | medium | 2026-10-11 | — | — |
| f39 | [추정] | 확인한 국내 실내 이동로봇 KS(KS B 8252)는 정적 장애물에 대한 보호정지 시험방법이어서, 움직이는 사람과의 속도·거리 기준값이나 병원·상업 시설·공동주택 실내 운행을 강제하는 기준은 이번에도 확인되지 않았다(oq-231 부분 근거). | ref-1473, ref-1471 | 아니오 | low | 2026-10-11 | — | — |
| f40 | [사실] | 공개 ROS 2 패키지 human_detection_fusion 은 YOLO 검출과 UWB 위치를 합쳐 사람 식별자별 위치를 '/humans/persons/<id>/position' 토픽에 ROS4HRI 의 hri_msgs/PointOfInterest3DStamped 형식으로 발행한다. | ref-1474 | 아니오 | medium | 2026-10-11 | 수행 자원 | — |
| f41 | [사실] | 같은 코드의 transformUWBPosition 함수는 UWB 좌표를 계획 좌표계로 바꾸다 TF 변환 예외가 나면 경고 로그를 남기고 입력 좌표를 그대로 돌려준다. | ref-1474 | 아니오 | medium | 2026-10-11 | — | — |
| f42 | [추정] | 호출부는 반환된 좌표에 header.frame_id 를 TARGET_FRAME(계획 좌표계)으로 붙여 발행하므로, 변환이 실패하면 UWB 좌표계 값이 계획 좌표계 값으로 표시돼 나갈 수 있어 보인다. 실제 운용에서 오류가 났는지, 상위 계층이 이를 보정하는지는 확인하지 못했다. | ref-1474 | 아니오 | low | 2026-10-11 | 제약 | — |
| f43 | [사실] | 이 저장소의 'KIRO' 는 EU ARISE 1차 공개 모집의 실험 이름으로, 한국로봇융합연구원(KIRO)과는 다른 것이며, 저작권자는 그리스 연구기관 ATHENA RC 이고 라이선스는 AGPL-3.0 이다. | ref-1474 | 아니오 | medium | 2026-10-11 | — | — |
| f44 | [의견] | 사람 위치를 받아 플릿 감속·정지에 쓰는 ROP 연계에는 측정 시각, 좌표계, 변환 성공 여부, 만료 시각을 메시지에 명시하게 하고, 위치 수신과 차량의 실제 감속 확인을 별도 단계로 시험해야 한다. | ref-1474, ref-1080 | 아니오 | low | 2026-10-11 | 제약 | — |
| f45 | [추정] | 확인한 자료 범위에서 사람 위치를 여러 제조사 플릿에 동시에 전달해 감속·정지시키는 공통 안전 인터페이스는 없고, 기업 단독 사례(아마존 조끼, 벤더 주장)와 사람 위치 발행 형식만 정한 공개 구현(ROS4HRI 기반 human_detection_fusion)이 따로 있는 것으로 보인다(oq-232 부분 근거). | ref-1080, ref-1474 | 아니오 | low | 2026-10-11 | — | — |
| f46 | [사실] | NavWareSet 프로젝트는 통제된 실내 수집 실험에 참가자 총 17명이 참여했고 5명씩 2개 그룹과 5개 쌍으로 나뉘었다고 설명한다. | ref-1475 | 아니오 | medium | 2026-10-11 | 작업 대상 | — |
| f47 | [사실] | NavWareSet 의 시나리오에는 시야가 가려진 모퉁이에서 로봇과 사람이 마주치는 'BLIND CORNER' 가 포함된다. | ref-1475 | 아니오 | medium | 2026-10-11 | — | — |
| f48 | [의견] | 사람 근접 감속·정지 정책의 재생 시험에는 가려진 모퉁이·통로 점유·혼잡 장면을 넣고, 아동·보행 보조기·휠체어 사용자처럼 감지 특성이 다른 보행자를 따로 평가해야 하며, 기존 데이터셋만으로 취약 보행자 범위가 충족됐다고 보면 안 된다. | ref-1475, ref-1085 | 아니오 | low | 2026-10-11 | — | — |
| f49 | [추정] | 아마존의 로보틱스 테크 조끼 설명 글은 페이지 메타데이터 기준 2019-04-06 에 발행됐다. 49영역 본문 72행과 2026-09-30-area49-s6.md 55행의 '발행일 미확인' 을 이 날짜로 고칠 수 있다. | ref-1080 | 아니오 | low | 2026-10-11 | 물류창고 | 벤더 주장 |
| f50 | [추정] | 확인한 명세·코드는 구역 제한의 지원 신고(supportedZones)·적재 외곽 기준 진입 판정·계획 계층 속도 반영까지만 다루고, 플릿 구역 제한을 위험성 평가의 위험 감소 조치로 인정하는 조건이나 로봇 보호 필드 설정과의 정합을 누가 검증하는지는 다루지 않는다(oq-229 부분 근거). | ref-031, ref-1464, ref-1467 | 아니오 | low | 2026-10-11 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1466 | SICK (Martin Kidman) | The perfect size of the protective field on an industrial autonomous vehicle | 2021-02-09 | 벤더 문서 | medium | 2026-10-11 | https://www.sick.com/ag/en/the-perfect-size-of-the-protective-field-on-an-industrial-autonomous-vehicle/w/blog-size-protective-field-industrial-autonomous-vehicle | 아니오 |
| ref-1467 | Open Navigation (Nav2 documentation, Jazzy) | Collision Monitor Node — Nav2 Docs (Jazzy) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/collision_monitor/configuring_collision_monitor_node/ | 아니오 |
| ref-1468 | Open Navigation (Nav2 documentation, Jazzy) | Speed Filter Parameters — Nav2 Docs (Jazzy) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/costmap_2d/costmap_filters/speed_filter/ | 아니오 |
| ref-1469 | 산업통상부 (국가법령정보센터 행정규칙) | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 및 별표 3 실외이동로봇 운행안전인증 기준 | 2025-11-24 | 정부·연구기관 | high | 2026-10-11 | https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000269426 | 아니오 |
| ref-1470 | 법제처 국가법령정보센터 | 지능형 로봇 개발 및 보급 촉진법 시행규칙(산업통상부령 제1호, 2025-10-01 시행) 제7조의4·제7조의5 | 2025-10-01 | 정부·연구기관 | high | 2026-10-11 | https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lspttninfSeq=183075 | 아니오 |
| ref-1471 | Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보 | ISO 13482:2014 Robots and robotic devices — Safety requirements for personal care robots | 2014-02-03 | 표준 | medium | 2026-10-11 | https://iss.rs/en/project/show/iso:proj:53820 | 아니오 |
| ref-1472 | Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보 | ISO 10218-1:2025 Robotics — Safety requirements — Part 1: Industrial robots | 2025-02-05 | 표준 | medium | 2026-10-11 | https://iss.rs/en/project/show/iso:proj:73933 | 아니오 |
| ref-1473 | 국가기술표준원 (e-나라표준인증) | KS B 8252 실내 이동로봇의 보호정지 시험방법 | 2020-02-26 | 표준 | high | 2026-10-11 | https://www.standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSB8252&menuId=919&reformNo=&tmprKsNo=KSB8252&topMenuId=502&upperMenuId=503 | 아니오 |
| ref-1474 | ATHENA RC (유지관리 Andreas Vatistas, Nikolaos Lappas) — EU ARISE 'KIRO' 실험 | human_detection_fusion — src/yolo_uwb_fusion_node.cpp 및 README (커밋 934ca8387a205aaac894da22451970a203777e18) | 2026-06-29 | 오픈소스 문서 | medium | 2026-10-11 | https://github.com/nikolaslps/human_detection_fusion/blob/934ca8387a205aaac894da22451970a203777e18/src/yolo_uwb_fusion_node.cpp | 아니오 |
| ref-1475 | Brayan, J., Deng, S., Alves Neto, A., Okunevich, I., Krajnik, T., Bremond, F., & Yan, Z. (NavWare 프로젝트) | NavWareSet: A Dataset of Socially Compliant and Non-Compliant Robot Navigation (프로젝트 사이트) | 2026-05-24 | 논문 | medium | 2026-10-11 | https://anr-navware.github.io/navwareset/ | 아니오 |
| ref-1075 | Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing) | Implementing Speed and Separation Monitoring in Collaborative Robot Workcells | 2017 | 논문 | high | 2026-10-11 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/ | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-1464 | Open-RMF (open-rmf/rmf_ros2 저장소) | rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp(handle_target_emergency)·Node.cpp(비상 신호 구독) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp | 아니오 |
| ref-1082 | Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv; 2025 IEEE CASE) | Safe Human Robot Navigation in Warehouse Scenario | 2025-03-27 | 논문 | medium | 2026-10-11 | https://arxiv.org/abs/2503.21141 | 아니오 |
| ref-1083 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 2025-08-27 | 논문 | medium | 2026-10-11 | https://arxiv.org/abs/2508.19731 | 아니오 |
| ref-869 | Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | high | 2026-10-11 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full | 아니오 |
| ref-1081 | Rondoni 외 (Scientific Reports) | Navigation benchmarking for autonomous mobile robots in hospital environment | 2024-08-07 | 논문 | high | 2026-10-11 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/ | 아니오 |
| ref-1085 | Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv; IEEE ICRA 2026 채택) | Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters | 2026-04-15 | 논문 | medium | 2026-10-11 | https://arxiv.org/abs/2604.13677 | 아니오 |
| ref-1080 | Amazon | Ever wonder how people and robots team up on your Amazon order? | 2019-04-06 | 벤더 문서 | low | 2026-10-11 | https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order | 아니오 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | medium | 2026-10-11 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 아니오 |
| ref-992 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 | 2023-07-28 | 기사 | low | 2026-10-11 | https://zdnet.co.kr/view/?no=20230728173101 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/safety/human-proximity-safety.md | 4, 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 4(분리 2026-09-30-area49-s4) — NIST 논문 서지 정정: 학술지판 RCIM 44(2017), 2016-08-01 승인(f1). 본문 53행·s4 28·37행·s8 37행의 '2016' 표기를 '2017(2016 승인)'으로. ZR·ZS 위치 불확실성(메모 H02)은 기존 내용 확인(2026-09-30-area49-s4.md 38행) / 섹션 5 — 물류창고: 아마존 글 발행일 2019-04-06(f49, 벤더 주장 [추정]; 본문 72행·s6 55행 '발행일 미확인' 정정), Farrell 연구 문단(본문 74행)의 '정량 결과는 미확인' 정정 — 실물 로봇·OptiTrack·설정별 10회(f12), Table IV 4대·1.0 m/s/2대·1.5 m/s·보행자 0~2명·정지 구간 제외(f13), CASE 2025 서지(f14). 병원: 89행 '시뮬레이션 평가' 정정 — 실제 병원 배치를 재현한 모의 병원의 실물 실험·Vicon 8대(f18), 이동 장애물은 원격조종 로봇(f19), 정정 제안 f20. 같은 오류가 docs/categories/safety/index.md 125행·187행에도 있으나 이번 실행 범위 밖이라 후속 정리 필요. Tartu: 이종 다로봇은 시험 환경·병원 내 복수 배송 로봇은 향후 과제(f17), 혈액 운반 시연(메모 H19)은 기존 내용 확인(ref-869). 실외: 제약 칸(100행)의 질량별 속도·횡단 대기를 2023 기사 '당시 개정안'에서 현행 고시 제2025-21호 별표 3 근거로 바꾸고(f27·f29·f32·f34), 보호구역 5 km/h(f30), 감속·정지·회피(f31), 보행자 밀집 알림(f33)을 더함; 시행규칙 원조문(f25, 수치는 기존·근거만 새), 운행계획서 시나리오(f26), 의견 f35 / 섹션 6(분리 2026-09-30-area49-s6) — 보호 분리 거리: SICK 케이스 전환·다중 샘플링 응답시간(f2, 벤더 주장 [추정]); NIST 0.113 s(메모 H01)는 기존 내용 확인(s6 41행). 플릿 구역: supportedZones 보고 의무(f3), 적재 외곽 기준 진입(f4), 의견 f5; maximumSpeed m/s·진입 시 이미 제한 속도 도달(메모 H06·H07)은 기존 내용 확인(docs/categories/safety/index.md 77행), zoneSetId 변경·DISABLED 후 enableZoneSet(메모 H08·H09)은 기존 내용 확인(2026-09-30-area16-s6.md 49행, 2026-09-30-area16-s4.md 40행). 로봇 측: source_timeout 0.0 차단 해제(f6), speed_limit 0 = 제한 없음(f7), RMF 0 이하 무시·close_lanes(f8)·계획 반영까지만(f9), 0 값 의미 차이 [추정](f10), 의견 f11; Nav2 하드 실시간 인증 미제공(메모 H10)은 기존 내용 확인(s6 47행, ref-1077). s6 55행 Farrell 문장 정정(f12·f13), s6 57행 HATA 는 시뮬레이션·실패율 정의(f15·f16) 보강. s6 61행 Jafari '(실험 장소·참가자 수 미확인)' 정정 — 32명·3.2 m 복도·1.4/2.8 m/s·원격조종(f21), 같은 데이터 평가(f22), 오즈비 의미(f23), 정정 제안 f24. 데이터셋: NavWareSet 17명(f46)·BLIND CORNER(f47), 의견 f48 / 섹션 7(분리 2026-09-30-area49-s7) — 실외이동로봇 운행안전인증 행(44행): 시행규칙 제7조의4·제7조의5 원조문(f25·f26), 현행 고시 제2025-21호(f27)·별표 3 상위 8개 항목과 인증기관 8개 항목 일치(f28), 질량별 속도(f29). 새 행: ISO 13482:2014 발행·90.92(f36; ISO/FDIS 13482 50.20·2026-09-15(메모 H30)은 기존 내용 확인 — ref-1117), ISO 10218-1:2025 범위의 이동성 위험 제외(f37, 판 번호는 쓰지 않음), KS B 8252 정적 장애물 보호정지 시험방법(f38)과 한계(f39). Nav2 Collision Monitor 행에 source_timeout(f6), Speed Filter 0 값(f7) 추가 / 섹션 8(분리 2026-09-30-area49-s8) — Farrell 항목(42행) 서지를 CASE 2025(pp.548–555, 2025-08-17)로·'정량 결과 미확인' 삭제(f14), Rondoni 항목(41행) 제목 단수 'environment'·'모의 병원 환경' → 실물 모의 병원 실험(f20), Jafari 항목(40행) ICRA 2026 채택·32명(f24), HATA 항목(43행) IROS 2025 pp.12697–12703·시뮬레이션 평가·실패율 정의(f15·f16), NIST 항목 연도(f1), NavWareSet 새 항목(f46·f47) / 섹션 9 — 로봇 자체 지능·제어 행: 0 값 계약 차이와 어댑터 명령 구분(f10·f11), 사람 위치 연계 공개 구현 human_detection_fusion 의 ROS4HRI 발행(f40)·변환 실패 시 원좌표 반환(f41)·좌표계 표기 문제 [추정](f42)·'KIRO' 는 EU ARISE 실험 이름(f43, 한국로봇융합연구원 아님), 의견 f44; 업종별 조건 행: 운행계획서·보행자 밀집 알림(f26·f33·f35). 아마존 조끼(메모 H34)는 기존 내용 확인(본문 65~72행), 발행일만 f49 / 섹션 11 — 해결 제안 없음, 부분 근거만: oq-229(f50, 바탕 f3·f4·f8·f9), oq-230(f28 — 현행 별표 3 상위 8개 항목과 인증기관 8개 항목은 일치하나 기사 16가지와의 대응은 미확인; 오늘 50번 영역에서도 다루므로 부분 답변으로 둠), oq-231(f38·f39), oq-232(f40·f45). 관련 기존 질문: oq-186(16→8 개정 시점, 이번 미확인), oq-333(관제장치 항목 — 별표 3 8.가~라 f33 근거가 부분 관련). 메모의 새 질문 대조: U01→oq-229 하위, U08→f29·f32 로 답해 질문으로 올리지 않음, U09→oq-230·oq-186, U10→oq-064, U11→oq-254, U12→oq-231 하위, U13→oq-232, U14→oq-272 와 같아 새로 만들지 않음. U04(Farrell 독립 재현)·U06(Jafari 표 VI·VII 정밀도·재현율 산술)·U07(Tartu 장기 운영)은 이번 검증 범위 밖이라 올리지 않음. 새 질문 4건(U02·U03·U05·U15) / 다음 실행 후보: 50. 안전 표준·인증·사고 조사(f25~f29·f36~f38), 66. 실외(f29~f35), 63. 병원·의료(f17~f20), 20. 로봇·제조사 관제 연동(f8~f11), 19. 사람·보행자 모델(f40~f47). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 로봇별 반응 시간·제동 거리·적재 하중·센서 오차가 펌웨어 변경이나 운용 조건 변화로 바뀌었을 때, 로봇 측 보호 필드와 ROP 의 구역 속도 제한·감속 시작 지점을 함께 다시 검증하는 절차나 공개 사례가 있는가? | 관련 영역: 49. 사람 근접 안전, 57. 자산·소프트웨어 수명주기 관리 | 근거: f2 | 종류: 일반
- Nav2 의 speed_limit 0(제한 없음)·source_timeout 0.0(차단 해제)과 Open-RMF 의 0 이하 속도 제한(무시) 같은 서로 다른 '0' 의미를 이종 플릿 어댑터가 올바르게 변환하는지 실행 시험으로 확인한 공개 자료나 적합성 시험 항목이 있는가? | 관련 영역: 49. 사람 근접 안전, 20. 로봇·제조사 관제 연동 | 근거: f10 | 종류: 일반
- HATA 의 임무 완료 시간 최대 26%·19% 단축을 다시 계산할 수 있도록 실험별 분모, 교착·타임아웃 실패 시행의 처리 방식, 고정된 실행 코드가 공개돼 있는가? | 관련 영역: 49. 사람 근접 안전, 25. 작업 배정 — MRTA | 근거: f16 | 종류: 일반
- 아동·휠체어 사용자·보행 보조기 사용자·시각장애인이 가려진 모퉁이나 통로 점유 상황에서 로봇을 만날 때의 감지 누락·양보 결과를 독립적으로 측정한 데이터셋이나 시험 결과가 있는가? | 관련 영역: 49. 사람 근접 안전, 60. 노동·수용성·접근성 | 근거: f47 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 21 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 10건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-05/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f2: SICK 블로그는 원문 대조로 문장을 확인했으나 저장소 규칙(6.2 항목 13)에 따라 벤더 문서만 근거라 vendor_claim: true·[추정]으로 둔다. 특정 센서·하중 조건의 응답시간 실측값은 없음
    - f49: 아마존 글 발행일(2019-04-06)은 페이지 메타데이터 기준이며 벤더 문서만 근거라 [추정]. 조끼 신호의 거리·지연·안전 등급은 여전히 미확인
    - f14: Farrell 의 CASE 2025 쪽수(pp.548–555)·날짜(2025-08-17)는 UC eScholarship 기준이며 IEEE Xplore 원문은 열지 않음. Table IV 개별 수치는 옮기지 않음
    - f15: HATA 출판판 쪽수(pp.12697–12703)는 검증 결과 기준이며 IEEE Xplore 원문은 열지 않음
    - f24: Jafari 의 ICRA 2026 발표 쪽수·DOI 미확인(arXiv 저자판 표지의 채택 표기만 확인). 메모가 부록에서 제기한 Table VI·VII 정밀도·재현율 산술 불일치(U06)는 이번 검증 범위 밖이라 확인 못 함
    - f28·f34(oq-230·oq-186): 현행 별표 3 상위 8개 항목과 인증기관 8개 항목의 일치는 확인했으나, 2023-07-28 기사의 '16가지' 가 어느 판·계층(세부 항목)에 대응하는지와 16→8 개정 시점은 이번에 확인하지 못함. ref-992 는 다시 열지 않음
    - f36·f37: ISO 목록은 iso.org 403 이라 ISS(세르비아 표준원) 미러로 확인. ISO 10218-1:2025 의 판 번호는 쓰지 않음. 표준 본문 미열람
    - f38·f39: KS B 8252 본문 미열람(목록·적용범위만). kssn.net 은 502 로 열리지 않아 e-나라표준인증 상세로 확인. 국내 병원·상업·공동주택 실내의 사람 근접 속도·거리 강제 기준은 여전히 미확인(oq-231)
    - f42: human_detection_fusion 의 변환 실패 시 좌표계 표기 문제는 코드 경로 해석이며 실제 운용 오류·상위 보정 여부는 미확인. README 의 'Standard ROS4HRI output' 은 프로젝트 자기 서술
    - f46: NavWareSet 연결 논문(IJRR 2026)의 권호는 임시(0(0))라 확정 서지로 쓰지 않음
    - 메모의 VDA 5050 '2026-03' 날짜는 명세 안에 근거가 없어 쓰지 않음(ref-031 published null 유지)
    - oq-229(위험 감소 조치 인정 조건·검증 주체)·oq-232(이종 플릿 공통 감속·정지 인터페이스)는 부분 근거만 있고 답을 찾지 못함
- 범위 경계 위반 의심:
    - f2·f6·f7: 안전 레이저 스캐너 응답시간과 Nav2 Collision Monitor·Speed Filter 는 로봇 측 안전·로컬 회피 기능(연계 대상)이며, ROP 몫은 그 의미를 어댑터 계약에 반영하는 데로 한정
    - f25~f35: 실외이동로봇 운행안전인증 법령·고시는 59. 법·규제·보험·라이선스, 50. 안전 표준·인증·사고 조사, 66. 실외와 겹치므로 이 영역에는 사람 근접 감속·정지·속도 기준 근거로만 씀
    - f36~f39: 표준 목록 정보는 50. 안전 표준·인증·사고 조사 쪽 내용이며, 이 영역에는 사람 근접 요구의 적용 범위 확인용으로만 씀
    - f40~f43: 사람 검출·추적 모듈은 19. 사람·보행자 모델 쪽 기술이며, 이 영역에는 사람 위치를 감속·정지로 연결하는 인터페이스 근거로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 10건/15(ref-1466~ref-1475, 예약 구간 ref-1466~ref-1495 안), 재사용 11건(ref-1075·ref-031·ref-1464·ref-1082·ref-1083·ref-869·ref-1081·ref-1085·ref-1080·ref-980·ref-992). 출처 매핑(검증 결과 기준): 메모 n1→ref-1075(NIST 공개 PDF 로 열람), n2→ref-1466(벤더), n3→ref-031(3.0.0 태그), n4→ref-1467(Collision Monitor 문서 페이지; H10 은 기존 ref-1077 내용이라 이번 출처에서 뺌), n5→ref-1468, n6→ref-1464(오늘 48번 영역에서 등록), n7→ref-1082, n8→ref-1083, n9→ref-869, n10→ref-1081, n11→ref-1085, n12→ref-1469(산업통상부 게시글 대신 국가법령정보센터 고시 본문·별표 3), n13→ref-1470, n14→ref-1117(H30 기존 내용 확인만, finding 없어 sources 에서 뺌), n15→ref-1471, n16→ref-1473(standard.go.kr), n17→ref-1080, n18→ref-1474, n19→ref-1475, n20→ref-1472. 추가 재사용: ref-980(8개 항목 대조), ref-992(2023 기사 수치 비교, 이번 미열람). 교차 확인 0건 — 모든 [사실] finding 이 단일 출처이거나 같은 제도·프로젝트 계열(고시·시행규칙·인증기관은 같은 운행안전인증 체계, 코드·README 는 같은 저장소). 중복 제거: 메모 H01(NIST 0.113 s)·H02(ZR·ZS)·H06·H07(maximumSpeed m/s·진입 시 도달)·H08·H09(zoneSetId·enableZoneSet)·H10(Nav2 인증 미제공)·H19(Tartu 혈액 운반)·H30(ISO/FDIS 13482 50.20)·H34(아마존 조끼 동작)는 기존 위키에 있어 새 finding 으로 넣지 않고 위치만 rationale 에 적었다. 검증 반영: H03·H34 벤더 주장 [추정] 유지, H21·H22 로 본문 89행 정정(f20), Farrell 정량 미확인 문장 정정(f14), Jafari 참가자 정정(f24), 아마존 발행일(f49), NIST 연도(f1), 고시 표기 '제2025-21호' 통일, 메모가 '별표 미열람'으로 남긴 질량별 속도·횡단 조건은 별표 3 원문으로 확인(f29~f33), H36 의 좌표계 문제는 [추정] 시사점(f42), n18 'KIRO' 는 EU ARISE 실험명(f43), ISO 목록은 ISS 근거로 판 번호 없이(f36·f37). 현장 유형: 물류창고(f12~f14·f49), 병원(f17~f20), 실외(f25~f35). 국내 자료: 시행규칙(ref-1470)·고시(ref-1469)·KS(ref-1473)·인증기관(ref-980). 열린 질문 해결 제안 없음 — 부분 근거만: oq-229(f50), oq-230(f28, 오늘 50번 영역에서도 다룸), oq-231(f38·f39), oq-232(f40·f45). 메모의 새 질문 중 U01·U08~U14 는 기존 oq 와 같거나 이번 finding 으로 답해 새로 만들지 않았고, U02·U03·U05·U15 는 docs/open-questions.md 에 같은 질문이 없어 새로 올린다(U04·U06·U07 은 검증 범위 밖이라 보류). 메모의 '.research-work' 로컬 보존본 경로·행 번호는 저장소에 없어 쓰지 않고 원문 절·조항과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
```

### runs/2026-09-30-22/research.md

```markdown
# 리서치 브리프 2026-09-30-22

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-22 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 58. 다사업자 책임·계약·데이터 |
| 대분류 | P. 거버넌스·법규·사회 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 데이터 보유자, 실질적 변경, 모델 계약 조항, API 폐기 정책, 서비스 수준 협약 구성 요소 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·가정(공동주택)·건물 승강기 연동의 다사업자 책임 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 변경 승인·책임 분담, 데이터 접근·공유 계약, API 버전·폐기 정책, 서비스 수준·감사 이력 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — EU 데이터법·모델 계약 조항, 산업디지털전환법·산업데이터 계약 가이드라인, VDA 5050 버전 규칙, ISO/IEC 19086-1, IEC 62443-2-4, 21 CFR Part 11 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-145, oq-149, oq-185, oq-241, oq-249, oq-259 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까? [분류원문]
2. 법·표준은 로봇·AI 시스템을 바꾼 주체의 책임을 어떻게 정하는가(기계류의 실질적 변경, AI 가치사슬 책임, 산업제어 서비스 제공자의 보안 요구)? (섹션 4·6·7 겨냥, oq-249 관련)
3. 여러 사업자가 함께 만드는 운영 데이터의 소유·접근·공유 권리를 정하는 법과 계약 도구(EU 데이터법과 모델 계약 조항, 국내 산업디지털전환법과 산업데이터 계약 가이드라인)는 무엇인가? (섹션 4·6·7 겨냥, 한국 자료 우선)
4. 제조사·플랫폼 API 가 바뀔 때 호환성과 공지를 정하는 규칙(VDA 5050 버전 규칙, 오픈소스의 API 폐기 정책)은 어떻게 되어 있는가? (섹션 6·7 겨냥)
5. 서비스 수준 약속과 감사 이력은 어떤 표준·규정이 요구하고 무엇을 기록해야 하는가(ISO/IEC 19086-1, 21 CFR Part 11, EU AI법 로그 보관)? (섹션 6·7 겨냥)
6. 병원·공동주택·건물 설비 연동 등 현장 유형별로 다사업자 책임·계약을 다룬 사례와 책임 분담표 공개 사례가 있는가? (섹션 5·11 겨냥, oq-241·oq-149·oq-185 관련)
7. 다사업자 책임·계약·데이터에서 ROP가 직접 맡을 것과 계약 당사자·법무·제조사·설비업체에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥, oq-145·oq-259 관련)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | EU 데이터법(Regulation (EU) 2023/2854)은 2025-09-12부터 일반 적용되며, 연결 제품(IoT 기기) 사용자가 제품 사용으로 함께 만든 데이터에 접근·이용·이전할 수 있게 하고, 제조사·서비스 제공자 같은 데이터 보유자는 사용자와 계약을 맺어야 하며 사용자 동의 없이 비개인 데이터를 활용할 수 없다. | ref-1345 | 아니오 | medium | 2025-12-15 | 작업 대상 | — |
| f2 | [사실] | EU 데이터법은 사용자가 데이터를 직접 또는 데이터 보유자를 통해 자신이 고른 제3자에게 공유하게 하고, 기업 간 계약에서 일방적으로 부과된 조항 가운데 '항상 불공정'과 '불공정으로 추정'되는 조항을 정해 구속력을 없애며, 데이터 처리 서비스 간 전환 요금은 2027-01-12부터 완전히 없앤다. | ref-1345 | 아니오 | medium | 2025-12-15 | 제약 | — |
| f3 | [사실] | 유럽연합 집행위원회가 2025-11-19에 낸 권고 초안은 EU 데이터법 이행을 돕는 구속력 없는 모델 계약 조항(MCT) 네 벌(데이터 보유자–사용자, 사용자–데이터 수령자, 데이터 보유자–데이터 수령자(보상 포함), 자발적 공유자–수령자)과 클라우드 표준 계약 조항 여섯 개(전환·이탈, 해지, 보안·업무 연속성, 비분산, 일방 변경 금지, 책임)를 제시한다. | ref-1346 | 아니오 | medium | 2025-11-19 | — | — |
| f4 | [사실] | 한국의 산업 디지털 전환 촉진법(2022-07 시행)은 산업데이터 생성에 투자한 자에게 그 데이터의 사용·수익권을 인정하고 관계자 간 계약 체결을 권고하며, 정부가 산업데이터 계약 지침을 마련하도록 했다. | ref-1347 | 아니오 | low | 2022-03-15 | 작업 대상 | — |
| f5 | [사실] | 산업통상부의 산업데이터 계약 가이드라인(공공데이터포털 등록 2023-04-05, PDF 432쪽)은 총론·법적기초·산업데이터 가치 산정·계약의 유형·개인보상·국외이전으로 구성되며, 산업데이터 거래 당사자를 위해 유의사항·표준계약서·업종별 사례를 안내한다. | ref-1348, ref-1347 | 아니오 | medium | 2023-04-05 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 명세는 [주].[부].[수정] 의미적 버전을 써서 주 버전은 필수 필드 추가 같은 호환을 깨는 변경, 부 버전은 선택 매개변수 추가 같은 새 기능, 수정 버전은 문서 오탈자 같은 작은 정정에 쓰고, MQTT 토픽 경로에 주 버전을 넣으며(interfaceName/majorVersion/manufacturer/serialNumber/topic), 변경 제안은 공식 GitHub 저장소로 받는다. | ref-031 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f7 | [사실] | Kubernetes 의 API 폐기 정책은 API 요소를 API 그룹 버전을 올려야만 제거할 수 있게 하고, 버전 간 왕복 변환에서 정보가 보존되어야 하며, 정식(GA) API 는 주 버전 안에서 제거하지 않고 베타는 폐기 공지 뒤 9개월 또는 3개 부 릴리스 동안 유지하며, 폐기된 API 호출에는 경고 헤더·감사 주석·지표를 남긴다. | ref-1349 | 아니오 | medium | 2026-09-30 | — | — |
| f8 | [사실] | ISO/IEC 19086-1:2016(2016-09-21, 1판)은 클라우드 서비스 수준 협약(SLA)의 공통 구성 요소(개요, 클라우드 서비스 계약과 SLA 의 관계, 개념, 용어)를 정하지만 모든 서비스에 쓰는 표준 SLA 구조나 서비스 수준 목표 세트는 정하지 않는다. | ref-1351 | 아니오 | medium | 2016-09-21 | 예외·성과 | 원문 미열람 |
| f9 | [사실] | IEC 62443-2-4:2023(2023-12-15)은 산업 자동화·제어 시스템(IACS) 서비스 제공자가 자동화 솔루션의 통합·유지보수 중에 자산 소유자에게 제공할 보안 관련 프로세스 요구사항을 정하며, 자산 소유자·서비스 제공자·제품 공급자를 구분하고 업종별로 요구를 골라 쓰는 프로파일을 둔다. | ref-1352 | 아니오 | medium | 2023-12-15 | 수행 자원 | 원문 미열람 |
| f10 | [사실] | EU 기계류 규정(Regulation (EU) 2023/1230, 2023-06-14 채택, 2027-01-20 적용)은 기계에 실질적 변경을 한 자연인·법인을 제조자로 보아 제조자 의무를 지게 하며, 실질적 변경은 새로운 위험을 만들거나 기존 위험을 키워 새로운 중요한 보호 조치가 필요한 변경이고 적합성에 영향을 주지 않는 수리·정비는 이에 해당하지 않는다. | ref-555, ref-1359 | 아니오 | medium | 2023-06-14 | 제약 | — |
| f11 | [사실] | EU AI법 제25조는 유통자·수입자·배포자(deployer)·제3자가 고위험 AI 시스템에 자기 이름을 붙이거나 실질적 변경을 하거나 용도를 바꾸면 제공자로 보고, 최초 제공자에게 기술 문서·정보·기술적 접근을 주는 협력 의무를 지우며, 제공자와 부품·도구·서비스 공급자는 필요한 정보·기능·기술적 접근·지원을 서면 계약으로 정하게 한다(오픈소스 제외). | ref-1356 | 아니오 | medium | 2026-09-30 | 수행 자원 | — |
| f12 | [사실] | EU AI법 제26조는 고위험 AI 시스템 배포자가 자기 통제 아래 있는 자동 생성 로그를 최소 6개월 보관하고, 제공자 지침에 따라 운영을 감시하다가 위험이 의심되면 제공자 등에 알리고 사용을 멈추며 중대한 사고는 즉시 제공자에게 먼저 알리게 한다. | ref-1357 | 아니오 | medium | 2026-09-30 | 예외·성과 | — |
| f13 | [사실] | 미국 21 CFR 11.10(e)는 폐쇄형 전자기록 시스템에 전자기록을 만들거나 고치거나 지우는 운영자 입력과 행위의 날짜·시각을 독립적으로 기록하는 보안이 적용된 컴퓨터 생성 타임스탬프 감사 추적을 쓰도록 요구한다. | ref-1353 | 아니오 | medium | 2026-09-30 | 완료·인계 | — |
| f14 | [의견] | Shaik(SSRN, 2026-05)은 자율 산업 시스템의 책임을 로봇 제조사(OEM)·시스템 통합자·AI 공급자·운영자 사이에 통제력(피해를 막을 수 있었는가)·예견 가능성·정보 비대칭의 세 원칙으로 배분하는 위험 비례 책임 프레임워크(RPLF)를 제안하고, 이를 상업 계약과 기존 보험으로 구현할 수 있다고 주장한다. | ref-1355 | 아니오 | low | 2026-05-01 | 예외·성과 | 원문 미열람 |
| f15 | [사실] | 병원 사례(싱가포르): 창이종합병원 CHART 는 의료 로봇 미들웨어 RoMi-H 통합을 맡을 시스템 통합자를 연 2회 등재 프로그램으로 평가·인증하고, 공공 의료기관은 로봇·소프트웨어·IoT 연동에 등재된 통합자를 쓰게 되어 있어 다사업자 연동의 책임 주체를 사전 자격으로 정한다. | ref-872 | 아니오 | medium | 2025-05 | 병원 / 수행 자원 | 원문 미열람 |
| f16 | [사실] | 한국승강기협회는 현대엘리베이터·오티스·TK엘리베이터·미쓰비시엘리베이터 등 승강기 제조사가 참여한 과학기술정보통신부 과제 '실내외 자율주행 로봇 상호연동 표준개발'로 배달 로봇과 승강기가 API 로 실시간 정보를 주고받는 연동 표준을 만들고 있으며, 2024-12-31까지 국내·국제 표준 개발, 전문가 협의체 구성, 테스트베드·개념증명을 목표로 했다. | ref-317 | 아니오 | low | 2023-05-17 | 수행 자원 | — |
| f17 | [사실] | 가정 사례(한국 공동주택): 한국아파트신문 사설(2026-09-14)은 시흥 힐스테이트더웨이브시티의 주차로봇 2세트 실증, 서울 송파구 아파트의 자율주행 순찰로봇 2대, 강남 타워팰리스의 사족보행로봇 기술검증, 부산 강서구 아파트의 운반로봇 서비스를 들고, 발의된 이동로봇 특별법안이 개인정보 처리·책임 분담·책임보험 가입 같은 안전관리 체계를 담는다고 전했다. | ref-1358 | 아니오 | low | 2026-09-14 | 가정 / 수행 자원 | — |
| f18 | [의견] | 같은 사설은 공동주택에 로봇·AI·통신망·관제시스템이 더해지면 관리사무소장 등 관리주체의 관리 영역과 책임이 오히려 넓어질 수 있으므로 도입 전에 책임 범위를 명확히 하고 법제도를 정비해야 한다고 본다. | ref-1358 | 아니오 | low | 2026-09-14 | 가정 / 제약 | — |
| f19 | [추정] | 확인한 자료를 종합하면 핵심 질문(제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까)에 대해 이를 한 번에 정한 공개 표준이나 책임 분담표는 찾지 못했고, 실제 규칙은 (a) 변경을 한 주체가 제조자·제공자 의무를 지는 법 규정(기계류 규정의 실질적 변경, AI법 가치사슬 책임), (b) 인터페이스 표준의 버전·폐기 규칙, (c) 서비스 수준 협약·표준 계약 조항과 통합자 사전 자격 같은 계약·조달 장치의 조합으로 정해지는 것으로 보인다. | ref-555, ref-1356, ref-031, ref-1349, ref-1351, ref-1346, ref-1352, ref-872 | 아니오 | low | 2026-09-30 | — | — |
| f20 | [추정] | 확인한 자료를 종합하면 58. 다사업자 책임·계약·데이터에서 ROP가 직접 맡을 범위는 제조사·설비 어댑터별 인터페이스 버전과 폐기 일정 관리, 연동·설정 변경의 요청·승인·적용 기록, 누가 언제 어떤 명령·변경을 했는지 남기는 타임스탬프 감사 이력과 보관, 데이터 항목별 소유·접근·반출 조건 표시, 계약한 서비스 수준 지표의 측정·보고로 보인다. | ref-031, ref-1349, ref-1353, ref-1357, ref-1345, ref-1346, ref-1351 | 아니오 | low | 2026-09-30 | 완료·인계 | — |
| f21 | [추정] | 연계 대상: 분류 원문 19장 기준으로 계약 체결과 법적 책임 판정·보험·규제 적합성 평가는 계약 당사자와 법무(59. 법·규제·보험·라이선스)에, 로봇 펌웨어와 제조사 API 의 수명주기는 로봇 제조사에, 승강기·출입문 쪽 연동 인터페이스와 설비 안전은 설비 제조사·관리주체에 속하므로, ROP는 그들이 정한 조건을 운영 제약으로 받고 판단 근거가 되는 기록과 데이터를 제공하는 쪽을 맡는 것으로 보인다. | ref-555, ref-1356, ref-317, ref-1358, ref-1355 | 아니오 | low | 2026-09-30 | 수행 자원 | — |
| f22 | [추정] | 이 영역은 인터페이스 버전 규칙의 21. 상호운용 표준·적합성과 20. 로봇·제조사 관제 연동(f6·f7), 승강기 연동 책임의 22. 설비·건물 시스템 연동(f16), 감사 이력·로그의 37. 관제 화면·실행 기록과 52. 통신 보호·위협 관리·감사(f12·f13·f9), 데이터 권리와 개인정보의 53. 개인정보·영상 데이터(f1·f17, oq-259), API 폐기와 변경 관리의 57. 자산·소프트웨어 수명주기 관리(f7), 규제 책임의 59. 법·규제·보험·라이선스(f10·f11·f14), 통합자 자격·계약의 3. 경제성·조달·사업 모델(f15), 책임 범위 합의의 2. 사용 사례·요구·책임 범위(oq-241), AI 가치사슬 책임의 47. AI·학습·적응과 모델 운영과 13. 대화형 기능의 신뢰·기반(f11, oq-145), 적용 현장인 63. 병원·의료(f15)·65. 가정·공동주택(f17·f18)과 이어진다. | ref-031, ref-1349, ref-317, ref-1357, ref-1353, ref-1352, ref-1345, ref-1358, ref-555, ref-1356, ref-1355, ref-872 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-872 | Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART) | RoMi-H Empanelment Programme 2025 | 2025-05 | 정부·연구기관 | medium | 2026-09-30 | https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste | 예 |
| ref-1345 | European Commission (Shaping Europe's digital future) | Data Act explained | 2025-12-15 | 정부·연구기관 | high | 2026-09-30 | https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained | 아니오 |
| ref-1346 | European Commission (Shaping Europe's digital future) | Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts | 2025-11-19 | 정부·연구기관 | high | 2026-09-30 | https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding | 아니오 |
| ref-1347 | 지디넷코리아 | 산업데이터 만든 자에게 사용·수익권 부여 | 2022-03-15 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20220315103750 | 아니오 |
| ref-1348 | 산업통상부 (공공데이터포털) | 산업통상부_산업데이터 계약 가이드라인_20230109 | 2023-04-05 | 정부·연구기관 | high | 2026-09-30 | https://www.data.go.kr/data/15113186/fileData.do | 아니오 |
| ref-1349 | The Kubernetes Authors | Kubernetes Deprecation Policy | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://kubernetes.io/docs/reference/using-api/deprecation-policy/ | 아니오 |
| ref-555 | European Parliament and Council of the European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery | 2023-06-14 | 정부·연구기관 | medium | 2026-09-30 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 예 |
| ref-1351 | IEC / ISO (ISO/IEC JTC 1) | ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts | 2016-09-21 | 표준 | medium | 2026-09-30 | https://webstore.iec.ch/en/publication/25920 | 예 |
| ref-1352 | IEC (BSI Knowledge 게재) | IEC 62443-2-4:2023 Security for industrial automation and control systems - Security program requirements for IACS service providers | 2023-12-15 | 표준 | medium | 2026-09-30 | https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1 | 예 |
| ref-1353 | U.S. Food and Drug Administration 규정 (Cornell Law School LII 게재) | 21 CFR § 11.10 - Controls for closed systems | 미확인 | 정부·연구기관 | medium | 2026-09-30 | https://www.law.cornell.edu/cfr/text/21/11.10 | 아니오 |
| ref-317 | 전기신문 (안상민) | 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 | 2023-05-17 | 기사 | low | 2026-09-30 | https://www.electimes.com/news/articleView.html?idxno=320147 | 아니오 |
| ref-1355 | Shaik, A. S. (SSRN) | Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong? | 2026-05-01 | 논문 | medium | 2026-09-30 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6737139 | 예 |
| ref-1356 | Future of Life Institute (artificialintelligenceact.eu) | Article 25: Responsibilities Along the AI Value Chain \| EU Artificial Intelligence Act | 미확인 | 정부·연구기관 | medium | 2026-09-30 | https://artificialintelligenceact.eu/article/25/ | 아니오 |
| ref-1357 | Future of Life Institute (artificialintelligenceact.eu) | Article 26: Obligations of Deployers of High-Risk AI Systems \| EU Artificial Intelligence Act | 미확인 | 정부·연구기관 | medium | 2026-09-30 | https://artificialintelligenceact.eu/article/26/ | 아니오 |
| ref-1358 | 한국아파트신문 (사설) | 공동주택에 밀려오는 로봇, 또 다른 관리책임은 (제목 일부만 확인) | 2026-09-14 | 기사 | low | 2026-09-30 | https://www.hapt.co.kr/news/articleView.html?idxno=169488 | 아니오 |
| ref-1359 | European Agency for Safety and Health at Work (EU-OSHA) | Regulation 2023/1230/EU - machinery | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f19(핵심 질문 답, 추정), f18(공동주택 책임 확대 우려, 의견), f14(책임 공백 논의, 의견) / 섹션 4: 데이터 보유자·연결 제품 데이터 f1, 모델 계약 조항 f3, 산업데이터 사용·수익권 f4, 실질적 변경 f10·f11, 의미적 버전·API 폐기 정책 f6·f7, SLA 구성 요소 f8, 감사 추적 f13 / 섹션 5: 병원 — f15(수행 자원, 싱가포르), 가정 — f17(수행 자원, 한국 공동주택)·f18(제약), 현장 유형 미명시 건물 승강기 연동 — f16(22. 설비·건물 시스템 연동 연계로 서술). 물류창고·제조 공장·상업 시설·실외 사례는 찾지 못했음을 명시 / 섹션 6: 변경 승인·책임 분담 f10·f11·f9·f15, 데이터 접근·공유 계약 f1·f2·f3·f4·f5, API 버전·폐기 정책 f6·f7, 서비스 수준·감사 이력 f8·f12·f13 / 섹션 7: EU 데이터법·모델 계약 조항 f1~f3, 산업디지털전환법·산업데이터 계약 가이드라인 f4·f5, VDA 5050 버전 규칙 f6, Kubernetes 폐기 정책 f7, ISO/IEC 19086-1 f8(원문 미열람), IEC 62443-2-4 f9(원문 미열람), EU 기계류 규정 f10, EU AI법 제25·26조 f11·f12, 21 CFR Part 11 f13 / 섹션 8: f3·f5·f14 / 섹션 9: f20(직접 범위), f21(연계 대상) / 섹션 10: f22 — 2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65 / 섹션 11: 기존 oq-145·oq-149·oq-185·oq-241·oq-249·oq-259(모두 미해결 유지; oq-241·oq-249 는 f10·f11·f12·f19 로 부분 근거)와 open_questions_new 5건. 다음 실행 후보: 22. 설비·건물 시스템 연동 페이지에 f16, 65. 가정·공동주택 페이지에 f17·f18, 57. 자산·소프트웨어 수명주기 관리 페이지에 f7 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 데이터 보유자 | Data Holder (EU Data Act) | EU 데이터법에서 연결 제품이나 관련 서비스가 만든 데이터를 이용·제공할 권리나 의무를 가진 자로, 사용자 요청 시 데이터를 사용자나 제3자에게 제공해야 하고 사용자와의 계약 없이 비개인 데이터를 활용할 수 없다. |
| 실질적 변경 | Substantial Modification | 출시된 기계나 AI 시스템을 바꿔 새로운 위험을 만들거나 위험을 키우거나 적합성·용도에 영향을 주는 변경으로, 이를 한 자가 제조자·제공자의 의무를 지게 되는 기준이다. |
| 모델 계약 조항 | Model Contractual Terms (MCTs) | EU 집행위원회가 데이터법 이행을 위해 데이터 보유자·사용자·데이터 수령자 사이의 데이터 접근·이용 계약에 쓰도록 권고하는 구속력 없는 표준 계약 문안이다. |
| API 폐기 정책 | API Deprecation Policy | API 요소를 언제 어떤 공지와 유예 기간을 거쳐 폐기·제거할지, 버전을 어떻게 올릴지를 미리 정해 이용자가 호환성을 예측하게 하는 규칙이다. |

## 열린 질문

새로 생긴 질문:

- 여러 제조사 로봇의 운영 데이터를 모으는 오케스트레이션 플랫폼 사업자는 EU 데이터법상 데이터 보유자인가, 사용자가 지정한 제3자 데이터 수령자인가, 그리고 그에 따라 제조사에게 데이터 제공을 요구할 수 있는 범위는 어디까지인가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 59. 법·규제·보험·라이선스 | 근거: f1 | 종류: 일반
- 로봇 제조사·관제 API 의 주 버전 변경이나 폐기를 오케스트레이션 플랫폼에 사전 통지하는 기간과 유예 기간을 계약이나 인터페이스 표준에 명시한 공개 사례가 있는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 20. 로봇·제조사 관제 연동, 57. 자산·소프트웨어 수명주기 관리 | 근거: f7 | 종류: 일반
- 국내 산업데이터 계약 가이드라인의 표준계약서와 업종별 사례가 로봇 운영 데이터(지도·작업 이력·센서 로그)처럼 여러 사업자가 함께 만드는 데이터를 어떻게 다루는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 15. 지도·공간·위치 모델 | 근거: f5 | 종류: 일반
- 오케스트레이션 플랫폼에서 경로망·속도 제한·작업 규칙 같은 설정을 바꾸는 일이 EU 기계류 규정의 실질적 변경에 해당해 플랫폼 운영자나 통합자가 제조자 의무를 지는 경우가 있는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 59. 법·규제·보험·라이선스, 48. 안전·위험 관리 | 근거: f10 | 종류: 일반
- 로봇-승강기 연동 표준 과제의 결과물(표준 번호, 연동 장애 시 승강기 제조사·로봇 제조사·관제 사업자의 책임 분담)이 공개되었는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 22. 설비·건물 시스템 연동 | 근거: f16 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 0
- 예산 사용량: 검색 15회 · 신규 출처 15건
- 미확인 항목:
    - f4 산업디지털전환법 제9조의 공동 생성 데이터·제3자 제공 시 권리(당사자 약정 우선) 조문은 검색 요약에만 있어 finding 으로 내지 않음 — 국가법령정보센터 조문 열람 실패
    - f5 산업데이터 계약 가이드라인 PDF(432쪽) 본문 미열람 — 계약 유형 구분과 표준계약서 조항 미확인
    - f8 ISO/IEC 19086-1 본문 미열람(유료), 표준 SLA 구조를 정하지 않는다는 부분은 검색 요약
    - f9 IEC 62443-2-4 범위·역할 구분은 검색 요약 기준, 본문 미열람
    - f10 EU 기계류 규정 실질적 변경 정의·제18조는 EUR-Lex 본문을 열지 못해 검색 요약 기준
    - f14 Shaik 원고가 든 2024년 독일 자동차 공장 사고(6개 당사자 책임 부인) 사례는 저자 주장으로 독립 확인 실패 — finding 에서 제외
    - f16 로봇-승강기 연동 표준 과제의 결과물(표준 번호·책임 분담) 미확인
    - f17 이동로봇 특별법안 원문·발의일 미확인
    - oq-241 로봇 오케스트레이션 도입 계약의 책임 분담표·표준 계약 조항 공개 사례를 이번에도 찾지 못함
    - ISO/IEC 20000-1:2018 변경 관리 조항은 공개 원문을 읽지 못해 넣지 않음
    - 국내 공공 정보시스템 SLA 가이드는 공식 출처를 찾지 못해 넣지 않음
    - 물류창고·제조 공장·상업 시설·실외 현장의 다사업자 책임·계약 사례를 찾지 못함
- 범위 경계 위반 의심:
    - f10·f11·f12·f14: 규제상 책임·로그 의무와 책임 배분 이론은 59. 법·규제·보험·라이선스와 겹치므로 이 영역에서는 변경 승인·책임 분담 근거로만 쓰고 법적 판정은 f21 에서 연계 대상으로 둠
    - f16: 승강기 쪽 연동 인터페이스와 설비 안전 제어는 원문 19장 '시설·설비 제어' 연계 영역이므로 ROP 직접 범위로 서술하지 않음(f21 연계 대상)
    - f13: 21 CFR Part 11 은 FDA 규제 대상 전자기록에 적용되는 규정이라 감사 추적 요구의 참고 사례로만 쓰고 병원 현장 의무로 단정하지 않음(site_type null)
- 한계: web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-1345~ref-1359, 예약 구간 안)로 신규 출처 상한에 도달했다. 재사용 2건: ref-031(이전 브리프 2026-09-30-19 출처 표 값 사용, 이번에 GitHub 공식 저장소 원문을 다시 열어 버전 규칙 확인), ref-872(다시 열지 않고 재인용). 참고문헌 목록 요약에 행이 없어 같은 URL 이 이미 있으면 퍼블리셔 병합 필요. 원문 열람: 17건 중 12건(webfetch 11, github_raw 1)을 열었고 ref-872·ref-555(EUR-Lex 본문 비어 있음)·ref-1351·ref-1352(유료 표준, 소개 페이지만)·ref-1355(SSRN 403)는 fetched false 다. 교차 확인 0건. 벤더 주장 없음. 분류 원문 핵심 질문에는 f19 로 답했고 결론은 '연동 오류 수정·변경 승인 주체를 한 번에 정한 공개 표준·책임 분담표는 찾지 못했고, 변경 주체 책임 법규·인터페이스 버전 규칙·SLA와 표준 계약 조항·통합자 자격의 조합으로 정해지는 것으로 보인다'는 추정이다. 현장 유형 사례는 병원(f15 싱가포르, 재인용)·가정(f17·f18 한국 공동주택)이고 승강기 연동(f16)은 현장 유형을 밝히지 않아 null 로 두었다. 물류창고·제조 공장·상업 시설·실외는 찾지 못했다. 국내 자료는 지디넷코리아(ref-1347)·공공데이터포털(ref-1348)·전기신문(ref-317)·한국아파트신문(ref-1358)이다. 기존 열린 질문 oq-145·oq-149·oq-185·oq-241·oq-249·oq-259 는 해결하지 못했다(oq-249 는 f10·f12 가 개별 기계·AI 시스템 쪽 의무만 보여 플랫폼 적용 여부는 미해결, oq-241 은 f19 로 부분 근거). L. AI·학습 기술 관련은 f11(AI 가치사슬 책임)을 47. AI·학습·적응과 모델 운영과 연결 제안했다(f22). 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. 용어집에 이미 있는 감사 추적·서비스 수준 협약·의미적 버전 관리·산업데이터·서비스형 로봇·등재 프로그램·보안 수준(IEC 62443)은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### data/source_texts/ref-031.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
![logo](./assets/logo.png)

# Interface for the Communication between Mobile Robots and a Fleet Control

## VDA 5050

## Version 3.0.0

![Fleet control system and mobile robots](./assets/csagv.png)

# Disclaimer
The following explanations are intended to provide guidance for implementing an interface that enables communication between mobile robots and a fleet management system. They are intended to be freely accessible to all users and are non-binding. Any party choosing to apply these guidelines is responsible for ensuring their correct and appropriate use in each specific case.
Users must consider the applicable state of the art at the time the guidelines are applied. The use of these proposals does not relieve any party of responsibility for its own actions. These statements do not claim to be exhaustive, nor do they constitute an authoritative interpretation of existing laws. They do not replace the need to review and comply with relevant policies, legislation, or regulations.
In addition, the specific characteristics of the respective products and their various potential applications must be considered. All users act at their own risk. Any liability on the part of the VDA and VDMA or any individuals involved in the development or application of these proposals is excluded.
If you identify any inaccuracies in the application of these proposals or potential risks of misinterpretation, please notify the VDA immediately so that any necessary corrections can be made.

**Publisher**
Verband der Automobilindustrie e. V. (VDA)
Behrenstraße 35, 10117 Berlin,
Germany
www.vda.de

**Copyright**
Association of the Automotive Industry (VDA)
Reproduction and any other form of reproduction is only permitted with specification of the source.

Version 3.0.0

## Table of contents
[0 Foreword](#0-foreword)<br>
[1 Introduction](#1-introduction)<br>
[2 Scope](#2-scope)<br>
[3 Definitions](#3-definitions)<br>
  [3.1 Mobile Robot](#31-mobile-robot)<br>
  [3.2 Moving](#32-moving)<br>
  [3.3 Driving](#33-driving)<br>
  [3.4 Automatic driving](#34-automatic-driving)<br>
  [3.5 Manual driving](#35-manual-driving)<br>
  [3.6 Line-guided mobile robot](#36-line-guided-mobile-robot)<br>
  [3.7 Freely navigating mobile robot](#37-freely-navigating-mobile-robot)<br>
[4 Transport protocol](#4-transport-protocol)<br>
  [4.1 Connection handling, security and QoS](#41-connection-handling-security-and-qos)<br>
  [4.2 Topic levels](#42-topic-levels)<br>
  [4.3 Topics for communication](#43-topics-for-communication)<br>
[5 Process and content of communication](#5-process-and-content-of-communication)<br>
  [5.1 General](#51-general)<br>
  [5.2 Implementation Phase](#52-implementation-phase)<br>
  [5.3 Functions of the fleet control](#53-functions-of-the-fleet-control)<br>
  [5.4 Functions of the mobile robots](#54-functions-of-the-mobile-robots)<br>
[6 Protocol specification](#6-protocol-specification)<br>
  [6.1 Order](#61-order)<br>
    [6.1.1 Concept and logic](#611-concept-and-logic)<br>
    [6.1.2 Orders and order updates](#612-orders-and-order-update)<br>
    [6.1.3 Order cancellation](#613-order-cancellation)<br>
    [6.1.4 Order rejection](#614-order-rejection)<br>
    [6.1.5 Corridors](#615-corridors)<br>
  [6.2 Actions](#62-actions)<br>
    [6.2.1 Instant actions](#621-instant-actions)<br>
    [6.2.2 Action blocking types and sequence](#622-action-blocking-types-and-sequence)<br>
    [6.2.3 Predefined actions](#623-predefined-actions)<br>
  [6.3 Maps](#63-maps)<br>
    [6.3.1 Map distribution](#631-map-distribution)<br>
    [6.3.2 Maps in mobile robot state](#632-maps-in-the-mobile-robot-state)<br>
    [6.3.3 Map download](#633-map-download)<br>
    [6.3.4 Enable downloaded maps](#634-enable-downloaded-maps)<br>
    [6.3.5 Delete maps on the mobile robot](#635-delete-maps-on-the-mobile-robot)<br>
  [6.4 Zones](#64-zones)<br>
    [6.4.1 Zone types](#641-zone-types)<br>
    [6.4.2 Zone set transfer](#642-zone-set-transfer)<br>
    [6.4.3 Communication for interactive zones](#643-communication-for-interactive-zones)<br>
    [6.4.4 Interaction between zones](#644-interactions-between-zones)<br>
    [6.4.5 Error handling within zones](#645-error-handling-within-zones)<br>
  [6.5 Connection](#65-connection)<br>
  [6.6 State](#66-state)<br>
    [6.6.1 Concept and logic](#661-concept-and-logic)<br>
    [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges)<br>
    [6.6.3 Base request](#663-base-request)<br>
    [6.6.4 Information](#664-information)<br>
    [6.6.5 Errors](#665-errors)<br>
    [6.6.6 Operating Mode](#666-operating-mode)<br>
    [6.6.7 Clearing the order on the mobile robot](#667-clearing-the-order-on-the-mobile-robot)<br>
    [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)<br>
    [6.6.9 Action states](#669-action-states)<br>
    [6.6.10 Request use of Corridors](#6610-request-use-of-corridors)<br>
  [6.7 Visualization](#67-visualization)<br>
  [6.8 Sharing of planned paths for freely navigating mobile robots](#68-sharing-of-planned-paths-for-freely-navigating-mobile-robots)<br>
  [6.9 Request/response mechanism](#69-requestresponse-mechanism)<br>
  [6.10 Factsheet](#610-factsheet)<br>
[7 Message specification](#7-message-specification)<br>
  [7.1 Symbols of the tables and meaning of formatting](#71-symbols-of-the-tables-and-meaning-of-formatting)<br>
    [7.1.1 Optional fields](#711-optional-fields)<br>
    [7.1.2 Permitted characters and field lengths](#712-permitted-characters-and-field-lengths)<br>
    [7.1.3 Notation of fields, topics and enumerations](#713-notation-of-fields-topics-and-enumerations)<br>
    [7.1.4 JSON data types](#714-json-data-types)<br>
  [7.2 Protocol header](#72-protocol-header)<br>
  [7.3 Implementation of the order message](#73-implementation-of-the-order-message)<br>
    [7.3.1 Format of action parameters](#731-format-of-action-parameters)<br>
  [7.4 Implementation of the instantAction message](#74-implementation-of-the-instantaction-message)<br>
  [7.5 Implementation of the response message](#75-implementation-of-the-response-message)<br>
  [7.6 Implementation of the zoneSet message](#76-implementation-of-the-zoneset-message)<br>
  [7.7 Implementation of the connection message](#77-implementation-of-the-connection-message)<br>
  [7.8 Implementation of the state message](#78-implementation-of-the-state-message)<br>
  [7.9 Implementation of the visualization message](#79-implementation-of-the-visualization-message)<br>
  [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message)<br>

# 0 Foreword

The specification for this interface has been jointly developed by the Verband der Automobilindustrie e. V. (VDA) and the VDMA e. V. (Mechanical Engineering Industry Association).
The VDA represents the German automotive sector, including OEMs and Tier‑1/Tier‑n suppliers, and contributes its expertise in vehicle architectures, system integration, and safety‑critical communication.
The VDMA represents companies across the European mechanical and plant engineering industry and brings extensive knowledge in automation technology, machinery interoperability, and production system standardization.
Both organizations collaborate to ensure that the interface specification reflects current engineering requirements, supports robust and scalable system integration, and enables consistent data exchange across heterogeneous environments. Their joint development process emphasizes harmonized communication models, compatibility with established industrial standards, and long‑term maintainability of cross‑domain interfaces. This cooperation ensures that the resulting specification can be reliably implemented in automotive, machinery, and mixed‑industry applications, supporting high interoperability, operational safety, and future-proof system architectures.
The Institute for Material Handling and Logistics (IFL) at Karlsruhe Institute of Technology (KIT) is part of the department of mechanical engineering and focuses on combining research, teaching, and industrial application. Its interdisciplinary team works on future logistics challenges, including material flow analysis, automation, robotics, digitalization, AI, sustainability, and system design.
The Institute has been commissioned by the VDA and the VDMA to oversee the development of the VDA 5050. It contributes to this process by taking the lead in development, supporting issue review, and managing the official GitHub repository.

# 1 Introduction
This recommendation describes the communication interface for exchanging information between central fleet control and mobile robots.
The objective of this recommendation is to support the integration and efficient operation of mobile robot fleets under the supervision of a centralized fleet control system. This is achieved through the implementation of a standardized, vendor neutral communication interface that ensures interoperability between the fleet control system and individual mobile robots.
Various national technical guidelines and legal frameworks may offer general orientation in this context. They could provide indicative information on aspects such as planning, operation, safety, or coordination of automated systems. In addition, national standards and regulatory provisions may help ensure that technical processes and terminology are considered within a consistent overall framework.
The recommendation uses a semantic versioning schema. Major version changes (x.0.0) typically involve breaking changes, such as the introduction of new non optional fields. Minor version changes (3.x.0) generally introduce new features, for example the addition of an optional parameter for visualization. Patch version changes (3.0.x) usually address smaller corrections, such as fixing typographical errors in the documentation.
Stakeholders are invited to submit proposals for modifications or enhancements to the interface. Such proposals shall be submitted via the GitHub repository at: <https://github.com/vda5050/vda5050>.

# 2 Scope

This document describes a standardized and vendor-neutral communication interface between a fleet control system and mobile robots. Its purpose is to provide a common reference that supports interoperability in environments where multiple mobile robots operate under the coordination of a fleet control system. The use of this specification is optional and non-binding, and its application is at the discretion of the respective stakeholders.

The objectives of this specification are:

- to reduce complexity when connecting mobile robots to a fleet control system.
- to enable the coordinated operation of heterogeneous mobile robot fleets from different manufacturers within a shared physical environment.
- to provide a generic and domain independent set of interface definitions applicable to mobile robots with varying navigation principles, physical dimensions, load handling or manipulation capabilities, and autonomy levels.

This specification does not address the following topics:

- Safety Requirements: This document does not define functional, operational, or system safety requirements and shall not be regarded or applied as a safety standard.
- Traffic Management Logic: Strategies, algorithms, or decision making processes for traffic coordination (e.g., routing, prioritization, congestion handling, or deadlock resolution) are not included.
- Other Communication Interfaces: Interfaces unrelated to the communication between a fleet control system and mobile robots are excluded, such as interfaces to peripheral equipment, infrastructure components, or external IT systems.
- Project Coordination and Implementation Procedures: Project management activities, integration methodologies, commissioning workflows, validation and acceptance procedures, and similar organizational processes are not covered.
- Operational Responsibilities: This document does not allocate responsibilities among operators, system integrators, vehicle manufacturers, or fleet control providers with respect to planning, operation, maintenance, or safety.
- Cybersecurity Measures: Mechanisms, technologies, or processes for secure communication or data protection are not specified.

# 3 Definitions
The following terms and definitions apply for the purposes of this document. Terms that are not officially defined by standardization organizations may be interpreted differently in other contexts.

## 3.1 Mobile Robot
A driverless system for material transport primarily in operational settings, controlled by automation independently of their level of autonomy [Source ISO 3691-4]

## 3.2 Moving
State in which a mobile robot or any of its components undergoes a change in spatial position or orientation, including movement of wheels, load handling devices, or the robot body.

## 3.3 Driving
Operating state in which the mobile robot has a non zero translational and/or rotational velocity.

## 3.4 Automatic driving
Driving state in which the mobile robot operates without human intervention.

## 3.5 Manual driving
Driving state in which the mobile robot operates under direct human control.

## 3.6 Line-guided mobile robot
Mobile robots that follow predefined trajectories. Predefined trajectories are sent by fleet control as part of the order or defined on the robot, either explicitly or implicitly as the direct connection between nodes.

## 3.7 Freely navigating mobile robot
Mobile robots that plan their own trajectories. If fleet control sends a trajectory within the order, the robot shall follow this trajectory.

# 4 Transport protocol

Communication is expected to be done via wireless networks, considering the effects of connection failures and potential loss of messages.

The message protocol is Message Queuing Telemetry Transport (MQTT), which is to be used in combination with a JSON format.
MQTT 3.1.1 is the minimum required version for compatibility.
MQTT allows the distribution of messages to subchannels, which are called "topics".
Participants in the MQTT network subscribe to these topics and receive information that concerns them.

The JSON format allows for future extensions of the protocol with additional parameters as well as validation against schemas.

### 4.1 Connection handling, security and QoS

The MQTT protocol provides the option of setting a last will message for a client.
If the client disconnects unexpectedly for any reason, the last will is distributed by the broker to other subscribed clients.
The use of this feature is described in Section [6.5 Connection](#65-connection).

If the mobile robot disconnects from the broker, it keeps all the order information and fulfills the order up to the last released node.

To reduce the communication overhead, the MQTT QoS level 0 (Best Effort) shall be used for the topics `order`, `instantActions`, `state`, `factsheet`, `zoneSet`, `responses` and `visualization`. QoS level 1 (At Least Once) shall be used for the topic `connection`.

Protocol security needs to be taken into account by broker configuration, but is not addressed within this guideline.

### 4.2 Topic levels

The MQTT topic structure is not strictly defined due to the mandatory topic structure of cloud providers.
For a cloud-based MQTT broker the topic structure might have to be adapted individually, but it should roughly follow the proposed structure.
The topic names defined in the following sections are mandatory.

For a local broker the MQTT topic levels are suggested as followed:

**interfaceName/majorVersion/manufacturer/serialNumber/topic**

Example:
```
vda5050/v3/KIT/0001/order
```

MQTT Topic Level | Data type | Description
---|---|---
interfaceName | string | Name of the used interface
majorVersion | string | Major version number of the VDA 5050 recommendation, preceded by "v"
manufacturer | string | Manufacturer of the mobile robot.
serialNumber | string | Unique mobile robot serial number consisting of the following characters: <br>A-Z <br>a-z <br>0-9 <br>_ <br>. <br>: <br>-
topic | string | Topic (e.g., order or state) see Section [4.4 Topics for Communication](#43-topics-for-communication)

>Table 1 Explanation of suggested MQTT topic levels

Since the `/` character is used to define topic hierarchies, it shall not be used in any of the aforementioned fields.
Wildcard characters `+` and `#` as well as the character `$` that is reserved for broker internal topics should not be used either.

### 4.3 Topics for communication

The protocol uses the following topics for information exchange between fleet control and mobile robots.

Topic name | Published by | Subscribed by | Used for | Implementation | Schema
---|---|---|---|---|---
order | fleet control | mobile robot | Communication of orders | mandatory | order.schema
instantActions | fleet control | mobile robot | Communication of the actions that are to be executed immediately | mandatory | instantActions.schema
state | mobile robot | fleet control | Communication of the mobile robot state | mandatory | state.schema
visualization | mobile robot | visualization systems | High frequency communication of position and planned path | optional | visualization.schema
connection | broker / mobile robot | fleet control | Indicates when mobile robot connection is lost. Not to be used by fleet control for checking the mobile robot health, added for an MQTT protocol level check of connection | mandatory | connection.schema
factsheet | mobile robot | fleet control | Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control | mandatory | factsheet.schema
zoneSet | fleet control | mobile robot | Transfer of zone sets from fleet control to the mobile robot | optional | zoneSet.schema
responses | fleet control | mobile robot | Fleet control's responses to requests from within the mobile robot's state | optional | responses.schema

>Table 2 Topics for communication between fleet control and mobile robot

# 5 Process and content of communication

## 5.1 General

There are at least the following participants for the operation of driverless transport system:

- The operator of the DTS provides basic information
- The fleet control organizes and manages the operation
- The mobile robot carries out the orders

Figure 1 describes the communication content during the operational phase.
During implementation or modification, the mobile robot and the fleet control are manually configured.

![Figure 1 Structure of the information flow](./assets/information_flow_VDA5050.png)
>Figure 1 - Structure of the information flow

## 5.2 Implementation Phase

During the implementation phase, the DTS consisting of fleet control and mobile robots is set up.
The necessary framework conditions are defined by the operator and the required information is either entered manually by them or stored in the fleet control by importing from other systems.
Essentially, this concerns the following content:

- Definition of routes:
Using the Layout Interchange Format (LIF), routes can be imported to the fleet control. The LIF is a file format of track layouts for exchange between the integrator of the driverless transport mobile robots and a (third-party) fleet control system (LIF – Layout Interchange Format, VDMA 2024-03).
Alternatively, routes can also be implemented manually in the fleet control by the operator.
Routes can be one-way streets, restricted for certain mobile robot groups (based on the size ratios), etc.
- Route network configuration:
Within the routes, stations for loading and unloading, battery charging stations, peripheral environments (gates, elevators, barriers), waiting positions, buffer stations, etc. are defined.
- Mobile robot configuration: The physical properties of a mobile robot (size, available load carrier mounts, etc.) are stored by the operator.
The mobile robot shall communicate this information via the topic `factsheet` in a specific way that is defined in Section [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message) of this document.

The configuration of routes and the route network described above are not part of this document.
They form the basis for enabling order control and driving course assignment by the fleet control based on this information and the transport requirements to be completed.
The resulting orders to be executed by the robotic fleet are transferred to the individual mobile robots via MQTT.
The mobile robot then continuously reports its status to the fleet control in parallel with the execution of the order, also using MQTT.

## 5.3 Functions of the fleet control

The fleet control system performs, at minimum, the following functions:

- Assignment of orders to the mobile robots
- Route calculation and guidance of line-guided mobile robots (taking into account the limitations of the individual physical properties of each mobile robot, e.g., size, maneuverability, etc.)
- Detection and resolution of blockages ("deadlocks")
- Energy management: Charging orders can interrupt transfer orders
- Traffic control: Buffer routes and waiting positions
- (Temporary) changes in the environment, such as freeing certain areas or changing the maximum speed
- Communication with peripheral systems such as doors, gates, elevators, etc.
- Detection and resolution of communication errors

## 5.4 Functions of the mobile robots

Each mobile robot shall perform the following functions:

- Localization
- Execution of associated routes (line-guided or freely navigating)
- Execution of actions
- Continuous transmission of its status

# 6 Protocol specification

The following section describes the details of the communication protocol.
The protocol specifies the communication between the fleet control and the mobile robot.

## 6.1 Order

The topic `order` is the MQTT topic via which the mobile robot receives an order, containing instructions for the robot to move or execute actions.

### 6.1.1 Concept and logic

The core of a transport order is a node-edge-graph segment defining the route to be travelled.
The mobile robot is expected to traverse the nodes and edges to fulfill the order.
The full graph of all connected nodes and edges is held by fleet control. It may contain restrictions, e.g., which mobile robot is allowed to traverse which edge.
These restrictions will not be communicated to the mobile robot.
The fleet control only includes edges in an order which the concerning mobile robot is allowed to traverse.

![Figure 2 Graph representation in fleet control and graph transmitted in orders](./assets/graph_representation_transmission.png)
>Figure 2 - Graph representation in fleet control and graph transmitted in orders

The nodes and edges are passed as two lists in the order message.
The order of the nodes and edges within those lists also governs the sequence in which the nodes and edges shall be traversed. The 'sequenceId' is shared between nodes and edges and defines the sequence of traversal. The first node has a `sequenceId` of 0, the first edge has a `sequenceId` of 1, the second node has a `sequenceId` of 2, etc. An edge with `sequenceId` n connects the nodes with `sequenceId` n-1 and n+1. The `sequenceId` shall be continuous within an order.

For a valid order, there shall be at least one node and the number of edges shall be equal to the number of nodes minus one.

The first node of an order (`sequenceId` = 0) shall be trivially reachable for the mobile robot and always be released.
This means either that the mobile robot is already standing on the node, or that the mobile robot is in the node's deviation range. As such, the first node shall not be reported in the `nodeStates`.

Nodes and edges both have a boolean attribute `released`.
If a node or edge is released, the mobile robot is expected to traverse it.
If a node or edge is not released, the mobile robot shall not traverse it.

An edge can be released only if both the start and the end node of the edge are released.

After an unreleased edge, no released nodes or edges can follow in the sequence.

The set of released nodes and edges are called the "base".
The set of unreleased nodes and edges are called the "horizon".

It is valid to send an order without a horizon.

An order message does not necessarily describe the full transport order.
For traffic control and to accommodate resource constrained mobile robots, the full transport order (which might consist of many nodes and edges) can be split up into many sub-orders, which are connected via their `orderId` and `orderUpdateId`.
The process of updating an order is described in the next section.

### 6.1.2 Orders and order update

To support traffic management, fleet control can split the path communicated via order into two parts:

- *"Base"*: This is the defined route that the mobile robot is allowed to travel. All nodes and edges of the base route have already been released by the fleet control for the mobile robot. The last node of the base is called decision point.
- *"Horizon"*: This is the route currently planned by fleet control for the mobile robot to travel after the decision point. The horizon route has not yet been released by the fleet control.

The mobile robot shall stop at the decision point if no further nodes and edges are added to the base. In order to ensure a fluent movement, the fleet control should extend the base before the mobile robot reaches the decision point, if the traffic situation allows for it.

Since MQTT is an asynchronous protocol and transmission via wireless networks is not reliable, the base cannot be changed. The fleet control shall therefore assume that the base has already been executed by the mobile robot. A later section describes a procedure to cancel an order, but this is also considered unreliable due to the communication limitations mentioned above.

The fleet control can change the horizon by sending an updated route to the mobile robot which includes the changed list of nodes and edges. The procedure for changing the horizon route is shown in Figure 3.

![Figure 3 Procedure for changing the driving route "Horizon"](./assets/driving_route_horizon.png)
>Figure 3 - Procedure for expanding the driving route "Horizon"

In Figure 3, an initial order is first sent by the fleet control at time t = 0.
Figure 4 shows the pseudocode of a possible order.
For the sake of readability, a complete JSON example has been omitted here.

```
{
	orderId: "1234",
	orderUpdateId:0,
	nodes: [
	 	 f {released: true},
	 	 d {released: true},
	 	 g {released: true},
	 	 b {released: false},
	 	 h {released: false}
	],
	edges: [
		e1 {released: true},
		e3 {released: true},
		e8 {released: false},
		e9 {released: false}
	]
}
```
>Figure 4 Pseudocode of an order.

At a later point in time, the order is extended by sending an order update (see pseudocode in Figure 5).
Note that the `orderUpdateId` is incremented and that the first node of the order update corresponds to the last base node of the previous order message, the stitching node. The other nodes and edges from the previous base are not resent.

This ensures that the mobile robot can also perform the order update, i.e., that the first node of the order update is reachable by executing the edges already known to the mobile robot.

```
{
	orderId: "1234",
	orderUpdateId: 1,
	nodes: [
		g {released: true},
		b {released: true},
		h {released: true},
		i {released: false}
	],
	edges: [
		e8 {released: true},
		e9 {released: true},
		e10 {released: false}
	]
}
```
>Figure 5 Pseudocode of an order update. Note the change of the `orderUpdateId`.

This also aids in the event that an order update is lost (e.g., due to an unreliable wireless network).
The mobile robot can always check that the last known base node has the same `nodeId` (and `sequenceId`) as the first node of a new order update.

Also note that node g is the only base node that is sent again.
Since the base cannot be changed, a retransmission of nodes f and d is not valid.

![Figure 6 Regular update process - order extension](./assets/update_order_extension.png)
>Figure 6 - Regular update process - order extension.

Figure 6 describes how an order should be extended.
It shows the information that is currently available on the mobile robot.
The `orderId` stays the same and the `orderUpdateId` is incremented.

It is important that the contents of the decision point (node g in Figure 6) are not changed. This means actions, deviation range, etc., shall be resent (see Figure 7, `orderUpdateId` 1).
In order to release actions for the mobile robot to execute on a node it is already positioned on through an order update, the fleet control shall re-send this node once with all meta-data (including potentially already 'FINISHED'/'RUNNING' actions) from the previous order update, which will not be executed again by the mobile robot, and then add a node with the now newly released actions to be executed with this order update. This node can have the same `nodeId` as the decision node or a different `nodeId` but the same position as the decision node. The `sequenceId` of the new node is always the `sequenceId` of the decision node plus 2.

![Figure 7 Order update with additional stitching node.](./assets/update_order_stitching_node.png)
>Figure 7 - Order update with additional stitching node (e.g., to execute new actions on decision point)

The horizon may be modified or deleted entirely with any order update, or the base may be extended in a way different from the previous horizon.

Once a `sequenceId` is assigned and the node is released, it does not change with order updates (see Figure 6).

Figure 8 describes the process of accepting an order or order update.

![Figure 8 The process of accepting an order or orderUpdate](./assets/process_order_update.png)
>Figure 8 - The process of accepting an order or order update.

1) **Is received order valid?**:
All formatting and JSON data types are correct?

2) **Is received order new or an update of the current order?**:
Is `orderId` of the received order different to `orderId` of order the mobile robot currently holds?

3) **Is mobile robot idle and not waiting for an update?**:
Is the mobile robot in an idle state according to [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot) and not waiting for an update? Since nodes and edges and the corresponding action states of the order horizon are also included inside the state, the mobile robot might still have a horizon and therefore is waiting for an update and executing an order.

4) **Is OrderUpdateId 0?**: Is the `orderUpdateId` of the new order 0?

5) **Is start of new order close enough to current position?**:	Is the mobile robot already standing on the node, or is it in the node's deviation range ([6.1.1 Concept and logic](#611-concept-and-logic))?

6) **Is received order update deprecated?**: Is `orderUpdateId` less than or equal to one currently on the mobile robot?

7) **Is order update following cancelOrder?**: No further order updates to the cancelled order shall be sent by the fleet control or accepted by the mobile robot.

8) **Is received order update currently on mobile robot?**: Is `orderUpdateId` equal to the one currently on the mobile robot?

9) **Is the received update a valid continuation of the currently still running order?**:	Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is still moving or executing actions related to the base released in previous order updates or still has a horizon and is therefore waiting for a continuation of the order. In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

10) **Is the received update a valid continuation of the previously completed order?**: Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is not executing any actions anymore neither is it waiting for a continuation of the order (meaning that it has completed its base with all related actions and does not have a horizon). In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

11) **Populate/append** new states to the `actionStates`/`nodeStates`/`edgeStates`.

#### 6.1.2.1 Finishing an order

After the mobile robot has traversed the last node of an order and has finished all order related movement and actions, it is idle and shall be ready to receive a new order (see [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)).

### 6.1.3 Order cancellation

Fleet control can cancel an active order using the instantAction `cancelOrder`.

Fleet control can optionally pass an `orderId` to reference which order shall be canceled.
After receiving the instantAction `cancelOrder`, the mobile robot shall attempt to stop as soon as possible.
For line-guided mobile robots, this could be the next feasible node. A freely navigating mobile robot shall stop as soon as possible, not merely at the next node.

If there are actions in the `actionStates` scheduled, these actions shall be cancelled and report 'FAILED' in their `actionState`.
If there are actions in the `actionStates` running, those actions should be cancelled and also be reported as 'FAILED'.
If the action cannot be cancelled, the `actionState` of that action should reflect that by reporting 'RUNNING' while it is running, and after that the respective state ('FINISHED', if successful and 'FAILED', if not).
While there are running actions in the `actionStates`, the cancelOrder action shall report 'RUNNING' until all actions are cancelled/finished. Actions that cannot be cancelled (cancelAllowed = false) shall be finished.
After all movement of the mobile robot and all of the actions in the `actionStates` are stopped, the `cancelOrder` action status shall report 'FINISHED'.
The mobile robot shall then be idle and ready to receive new orders.

The `orderId` and `orderUpdateId` are kept.

Figure 9 shows the expected behavior for different mobile robot capabilities.

![Figure 9 Expected behavior after a cancelOrder](./assets/process_cancel_order.png)
>Figure 9 - Expected behavior after a `cancelOrder`.

#### 6.1.3.1 Receiving a new order after cancellation

After the cancellation of an order, the mobile robot is idle and shall be ready to receive a new order. No further order updates to the cancelled order shall be sent by the fleet control. If the mobile robot receives an order update it shall report an error of type 'ORDER_UPDATE_FOLLOWING_CANCEL' and level 'WARNING'.

In the case of a mobile robot that can only localize itself on a node, the new order shall begin on the node the mobile robot is now standing on (see also Figure 4).

In case of a mobile robot that can stop in between nodes, fleet control can decide how to start the next order.
The mobile robot shall accept both methods.

There are two options:

- The first node of the new order is a temporary node that is positioned at the mobile robot's current position. The mobile robot shall then recognize that this node is trivially reachable and accept the order.
- The first node of the new order is the last traversed node of the previous order. The allowed deviation of this node is set large enough to ensure that the mobile robot is within this range. Thus, the mobile robot shall immediately treat this node as traversed and accept the order.

#### 6.1.3.2 Receiving a cancelOrder action when mobile robot is idle

If the mobile robot receives a `cancelOrder` instant action but the mobile robot is currently idle, or the `orderId` specified in the action does not match the `orderId` of the mobile robot’s currently active order, the `cancelOrder` action shall be reported as 'FAILED'.

The mobile robot shall report an error of type 'NO_ORDER_TO_CANCEL' with the level set to 'WARNING'. The `actionId` of the `instantAction` shall be passed as an `errorReference`.

### 6.1.4 Order rejection

There are several scenarios, when an order shall be rejected.
These scenarios are shown in Figure 8 and described below.

#### 6.1.4.1 Mobile robot receives a malformed order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'VALIDATION_FAILURE' and level 'WARNING‘
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.2 Mobile robot receives an order with optional fields it cannot use

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'UNSUPPORTED_PARAMETER' with level 'CRITICAL' and the erroneous fields as errorReferences
3. The error shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.3 Mobile robot receives an order with actions it cannot perform

Example:

- lifting height higher than maximum lifting height
- lifting actions although no stroke is installed, etc.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'INVALID_ORDER_ACTION' with level 'WARNING' and the erroneous fields as errorReferences
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.4 Mobile robot receives an order with the same orderId, but a lower orderUpdateId than the current orderUpdateId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. The mobile robot shall report an error of type 'OUTDATED_ORDER_UPDATE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.5 Mobile robot receives an order with the same orderId and same orderUpdateId as the current orderUpdateId

Example:

- Fleet control resends the order because it did not yet receive any state message with the respective `orderUpdateId`.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. Reporting depends on the content of the message:
	- If the content of the new order is the same as the content of the previous one, the mobile robot shall ignore the new order.
	- If the content of the new order differs, the mobile robot shall report an error of type 'SAME_ORDER_UPDATE_ID' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.6 Mobile robot receives an order with orderId different to the orderId of an active order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot keeps the previous order in its buffer.
3. The mobile robot shall report an error of type 'OTHER_ORDER_ACTIVE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.7 Mobile robot receives an order with the start node being out of range

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'START_NODE_OUT_OF_RANGE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.8 Mobile robot receives an order with at least one node not being reachable

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'NO_ROUTE_TO_TARGET' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.9 Mobile robot receives an order while in an operating mode that does not allow new orders

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'MOBILE_ROBOT_NOT_AVAILABLE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot is in an order mode that allows for new orders.

#### 6.1.4.10 Mobile robot receives an order containing nodes with unknown mapId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'UNKNOWN_MAP_ID' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

### 6.1.5 Corridors

The optional `corridor` edge attribute allows the mobile robot to deviate from the edge trajectory for obstacle avoidance and defines the boundaries within which the mobile robot is allowed to operate.
To use the `corridor` attribute, a predefined trajectory is required that the mobile robot would follow if no `corridor` attribute was defined. This can be either the trajectory defined on the mobile robot known to the fleet control or the trajectory sent in an order. The behavior of a mobile robot using the `corridor` attribute is still the behavior of a line-guided mobile robot, except that it is allowed to temporarily deviate from a trajectory to avoid obstacles.
Note that a corridor communicated within an order is released for the mobile robot by default. If the `releaseRequired` flag is set to true, the mobile robot shall request approval from fleet control before using the corridor as described in chapter [6.6.10 Request use of Corridors](#6610-request-use-of-corridors).

*Remark:
An edge inside an order defines a logical connection between two nodes and not necessarily the (real) trajectory that a mobile robot follows when driving from the start node to the end node.
Depending on the mobile robot type, the trajectory that a mobile robot takes between the start and end nodes is either defined by fleet control via the trajectory edge attribute or assigned to the mobile robot as a predefined trajectory.
Depending on the internal state of the mobile robot, the selected trajectory may vary.*

![Figure 10 Edges with corridor attribute.](./assets/edges_with_corridors.png)
>Figure 10 - Edges with a `corridor` attribute that defines the left and right boundaries within which a mobile robot is allowed to deviate from its predefined trajectory to avoid obstacles. On the left, the kinematic center defines the allowed deviation, while on the right, the contour of the mobile robot, possibly extended by the load, defines the allowed deviation. This is defined by the `corridorReferencePoint` parameter.
The area in which the mobile robot is allowed to navigate independently (and deviate from the original edge trajectory) is defined by a left and a right boundary.
The optional `corridorReferencePoint` field specifies whether the mobile robot control point or the mobile robot contour should be inside the defined boundary.
The boundaries of the edges shall be defined in such a way that the mobile robot is inside the boundaries of the new and now current edge as soon as it passes a node.
Instead of setting the corridor boundaries to zero, fleet control shall not use the `corridor` attribute if the mobile robot shall not deviate from the trajectory.

The mobile robot's motion control software shall constantly check that the mobile robot is within the defined boundaries.
If not, the mobile robot shall stop because it is out of the allowed navigation space and report an error of type 'OUTSIDE_OF_CORRIDOR' with level 'CRITICAL'.
The fleet control can decide if user interaction is required or if the mobile robot can continue by canceling the current order and sending a new order to the mobile robot with corridor information that allows the mobile robot to move again.

*Remark: Allowing the mobile robot to deviate from the trajectory increases the possible footprint of the mobile robot during driving. This circumstance shall be considered during initial operation, and when the fleet control makes a traffic control decision based on the mobile robot's footprint.*
See also Section [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges) for further information.

## 6.2 Actions

If the mobile robot supports actions other than driving, these actions are instructed via the `actions` array that is attached to a node or an edge, sent via the separate topic `instantActions` (see section [6.2.1 Instant actions](#621-instant-actions)) or configured via action zones (see section [6.4.1 Zone types](#641-zone-types)).
Actions that are to be executed on an edge shall only run while the mobile robot is on the edge (see Section [6.6.2 Traversal of nodes and entering/leaving edges, triggering of actions](#662-traversal-of-nodes-and-enteringleaving-edges-triggering-of-actions)).

Actions that are triggered on nodes can run as long as they need to run and should be self-terminating (e.g., an audio signal that lasts for five seconds or a pick action, that is finished after picking up a load) or formulated pairwise (e.g., "activateWarningLights" and "deactivateWarningLights").

### 6.2.1 Instant Actions

In certain cases, it is necessary to send actions to the mobile robot that need to be performed immediately.
This is possible by publishing an `instantAction` message to the topic `instantActions`.
These actions shall not conflict with the content of the mobile robot's current order (e.g., `instantAction` to lower fork, while order says to raise fork).

Some examples for which instant actions could be relevant are:

- pause the mobile robot without changing anything in the current order
- resume order after pause
- activate signal (optical, audio, etc.)

When a mobile robot receives an `instantAction`, an appropriate `actionStatus` shall be added to the `instantActionStates` array of the mobile robot's state.
The `actionStatus` shall be updated according to the progress of the action.
See also Figure 11 for the different transitions of an `actionStatus`.
The `blockingType` of an instant action is always 'NONE'.

When the mobile robot receives an `instantAction` it cannot execute, it shall report an 'INVALID_INSTANT_ACTION' error with level 'WARNING' and the `actionId` of the `instantAction` as `errorReference`.

### 6.2.2 Action blocking types and sequence

The order of multiple actions in a list defines the sequence in which the mobile robot shall execute them.

The parallel execution of actions is governed by their respective `blockingType`.
Actions can have four distinct blocking types, described in Table 3.

-| Parallel execution allowed | Parallel execution not allowed
---|---|---
Automatic driving allowed | NONE | SINGLE
Automatic driving not allowed | SOFT | HARD

>Table 3 Definition of action blocking types dependent on driving and parallel execution

Figure 11 describes how the mobile robot shall handle the blocking type of actions. Whenever the mobile robot arrives at a point where new actions are to be executed (i.e., when it reaches a node, edge, or action zone), the actions are enqueued in the same sequence as the actions array. This queue is continually processed as shown in Figure 11. If the blocking type of any action in the queue is 'SOFT' or 'HARD', the mobile robot shall stop automatic driving. Actions are collected for parallel execution if the action's blocking type is 'NONE' or 'SOFT'. If an action with blocking type 'SINGLE' or 'HARD' is to be executed, all collected parallel actions shall be 'FINISHED' or 'FAILED' before starting the action. If there are no more actions with blocking type 'SOFT' or 'HARD' in the queue, the mobile robot can resume automatic driving. 'FINISHED' or 'FAILED' actions shall be removed from the queue.

![Figure 11 Handling multiple actions](./assets/handling_multiple_actions.png)
>Figure 11 - Handling multiple actions

### 6.2.3 Predefined Actions

This section presents predefined actions that shall be used by the mobile robot, if the mobile robot's capabilities map to the action description.
If there is a sensible way to use the defined parameters, they shall be used.
Additional parameters can be defined, if they are needed to execute an action successfully.
The actions `cancelOrder`, `startPause` and `stopPause` shall be supported by every mobile robot.

If there is no way to map some action to one of the actions of the following section, the mobile robot manufacturer can define additional actions that shall be used by fleet control.

#### 6.2.3.1 Definition, parameters, effects and scope

action type | counter action | description | idempotent | parameters | linked state | instant | node | edge | zone
---|---|---|---|---|---|---|---|---|---
startPause | stopPause | Activates the pause mode. <br>A linked state is required, because many mobile robots can be paused by using a hardware switch. <br>No more automatic driving - reaching next node is not necessary. Actions that can be paused (`pauseAllowed`=`true`), shall be paused, other actions continue. Order execution is resumed after stopPause. | yes | - | paused | yes | no | no | no
stopPause | startPause | Deactivates the pause mode. <br>Movement and all other actions will be resumed (if any). <br>A linked state is required because many mobile robots can be paused by using a hardware switch. <br>stopPause can also restart mobile robots that were stopped with a hardware button that triggered startPause (if configured). | yes | - | paused | yes | no | no | no
startHibernation | stopHibernation | Initiates hibernate mode, in which the mobile robot shall remain connected to the MQTT broker but no longer needs to send state messages. The mobile robot shall report this action as 'FINISHED' before discontinuing publishing state messages and publish a connection state of 'HIBERNATING'. If the mobile robot has an active order, it shall clear it. Reaching the next node is not required.<br>While in 'HIBERNATING' connection state, mobile robot shall not be moving. The mobile robot shall only receive and respond to the instant action 'stopHibernation' and shall not respond to any other commands, such as orders or additional instant actions. <br>If the mobile robot's battery becomes critically low while in this mode, the mobile robot may stop 'HIBERNATING' autonomously to report an error. In case a wake‑up time is set, the mobile robot is able to autonomously exit the 'HIBERNATING' connection state at the specified time and will publish the corresponding connection state transition before resuming normal operation. | yes | wakeUpTime (string, optional) | - | yes | no | no
stopHibernation | startHibernation | Ends hibernate mode. To initiate wake‑up while the mobile robot is in the 'HIBERNATING' state, a control device (onboard or external) shall subscribe to the `instantAction` topic and remain connected to the MQTT broker. Because the mobile robots standard control device may be partially shut down during hibernation, the wake‑up may be triggered by a distinct MQTT client (separate from the mobile robots usual communication client).<br>Upon success, the mobile robot shall publish the connection state ONLINE.| yes | - | - | yes | no | no
shutdown | - | Initiates a coordinated shutdown of the mobile robot, where it disconnects from the MQTT broker. The execution of the shutdown action requires the mobile robot to be in an idle state. There is no way using the VDA 5050 protocol to automatically restart due to the connection being terminated.<br>If a mobile robot is in hibernate mode but should be shut down, it shall first exit hibernation (via stopHibernation) before executing shutdown.| yes | - | - | yes | no | no | no
startCharging | stopCharging | Activates the charging process. <br>Charging can be done on a charging spot (mobile robot stopped) or on a charging lane (while driving). <br>Protection against overcharging is the responsibility of the mobile robot. | yes | - | powerSupply.charging | yes | yes | no | no
stopCharging | startCharging | Discontinues the charging process. <br>The charging process can also be interrupted by the mobile robot or the charging station, e.g., if the battery is full. | yes | - | powerSupply.charging | yes | yes | no | no
initializePosition | - | Resets (overrides) the pose of the mobile robot with the given parameters. | yes | x (float64)<br>y (float64)<br>theta (float64)<br>mapId (string)<br>lastNodeId (string) | mobileRobotPosition.x<br>mobileRobotPosition.y<br>mobileRobotPosition.theta<br>mobileRobotPosition.mapId<br>lastNodeId<br> maps | yes | yes<br>(Elevator) | no | no
enableMap | - | Enable a previously downloaded map explicitly to be used in orders without initializing a new position. | yes | mapId (string)<br>mapVersion (string) | maps | yes | yes | no | no
downloadMap | - | Trigger the download of a new map. Active during the download. Errors reported in mobile robot state. Finished after verifying the successful download, preparing the map for use and setting the map in the state. | yes | mapId (string)<br>mapVersion (string)<br>mapDownloadLink (string)<br>mapHash (string, optional) | maps | yes | no | no | no
deleteMap | - | Trigger the removal of a map from the mobile robot's memory. | yes | mapId (string)<br>mapVersion (string) | maps | yes | no | no | no
downloadZoneSet | - | Trigger the download of a zone set. Active during the download. Errors reported in mobile robot state. Finished after verifying the successful download, preparing the zone set for use and setting the zone set in the state. | yes | zoneSetId (string)<br>zoneSetDownloadLink (string)<br>zoneSetHash (string, optional) | zoneSets | yes | no | no | no
enableZoneSet | - | Enable a previously downloaded zone set explicitly to be used in orders. | yes | zoneSetId (string)<br> | zoneSets | yes | yes | no | no
deleteZoneSet | - | Trigger the removal of a zone set from the mobile robot's memory. | yes | zoneSetId (string) | zoneSets | yes | no | no | no
clearInstantActions | - | Removes all finished or failed instant actions from the mobile robot state. | yes | - | instantActionStates | yes | yes | no | no
clearZoneActions | - | Removes all finished or failed zone actions from the mobile robot's state. | yes | - | zoneActionStates | yes | yes | no | no
stateRequest | - | Requests the mobile robot to send a new state message. | yes | - | - | yes | no | no | no
logReport | - | Requests the mobile robot to generate and store a log report. | yes | reason<br>(string) | - | yes | no | no | no
pick | drop<br><br>(if automated) | Request the mobile robot to pick a load. <br>Mobile robots with multiple load handling devices can process multiple pick operations in parallel. <br>In this case, the parameter lhd needs to be present (e.g., LHD1). <br>The parameter stationType informs how the pick operation is handled in detail (e.g., floor location, rack location, passive conveyor, active conveyor, etc.). <br>The load type informs about the load unit and can be used to switch field for example (e.g., EPAL, INDU, etc). <br>For preparing the load handling device (e.g., pre-lift operations based on the height parameter), the action could be announced in the horizon in advance. <br>But, pre-Lift operations, etc., are not reported as 'RUNNING' in the mobile robot state, because the associated node is not released yet.<br>If on an edge, the mobile robot can use its sensing device to detect the position for picking the node. | no |lhd (string, optional)<br>stationType (string, optional)<br>stationName (string, optional)<br>loadType (string, optional) <br>loadId (string, optional)<br>height (float64, optional)<br>defines bottom of the load related to the floor<br>depth (float64, optional) for forklifts<br>side (string, optional) e.g., conveyor | .load | no | yes | yes | no
drop | pick<br><br>(if automated) | Request the mobile robot to drop a load. <br>See action pick for more details. | no | lhd (string, optional)<br>stationType (string, optional)<br>stationName (string, optional)<br>loadType (string, optional)<br>loadId (string, optional)<br>height (float64, optional)<br>depth (float64, optional) <br>… | .load | no | yes | yes | no
detectObject | - | Mobile robot detects object (e.g., load, charging spot, free parking position). | yes | objectType (string, optional) | - | no | yes | yes | yes
finePositioning | - | On a node, mobile robot will position exactly on a target.<br>The mobile robot is allowed to deviate from its node position.<br>On an edge, the mobile robot will e.g., align on stationary equipment while traversing an edge. | yes | stationType (string, optional)<br>stationName (string, optional) | - | no | yes | yes | yes
waitForTrigger | - | Mobile robot shall wait for a trigger of the type defined specified in the triggerType parameter, which is an array of strings. Two predefined values shall be used when semantically appropriate: 'FLEET_CONTROL' if the trigger originates from the fleet control, and 'LOCAL' if the trigger comes from an input on the mobile robot (e.g., button press, manual loading). If none of the predefined values meet the specific requirements, custom values can be defined. <br>Fleet control is responsible for handling the timeout and shall cancel the order if necessary. | yes | triggerType [string] (array) | - | no | yes | no | yes
trigger | - | Fleet control system notifies the mobile robot that a waitForTrigger action has been released. Typically, this occurs when the fleet control system receives information from a third-party system indicating that the process the mobile robot was waiting for has completed. | yes | - | - | yes | no | no | no
retry | - | Mobile robot retries action defined via actionId that is currently in state RETRIABLE. | yes | actionId (string) | - | yes | no | no | no
skipRetry | - | Mobile robot shall skip the action defined via actionId that is currently in state RETRIABLE, setting action to FAILED. | yes | actionId (string) | - | yes | no | no | no
cancelOrder | - | Mobile robot stops as soon as possible. This could be immediately or on the next node. See Chapter 6.1.3 Order cancellation. | yes | orderId (string, optional) | - | yes | no | no | no
factsheetRequest | - | Requests the mobile robot to send a factsheet | yes | - | - | yes | no | no | no
updateCertificate | - | Request the mobile robot to download and activate a new certificate set, the service parameter is an extensible enum with the predefined parameter 'MQTT' to be used for mqtt connection. | yes | service (string)<br>keyDownloadLink (string)<br>certificateDownloadLink (string)<br>certificateAuthorityDownloadLink (string, optional) | - | yes | no | no | no

>Table 4 - Predefined actions and their scope (instant, node, edge, zone)

#### 6.2.3.2 Action states

action type | 'INITIALIZING' | 'RUNNING' | 'PAUSED' | 'FINISHED' | 'FAILED' | 'RETRIABLE'
---|---|---|---|---|---|---
startPause | - | Activation of the mode is in preparation.<br>If the mobile robot supports an instant transition, this state can be omitted. | - | Mobile robot is not moving. <br>All pauseable actions are paused. <br> The pause mode has been activated. <br>The mobile robot reports paused: "true". | The pause mode cannot be activated for some reason (e.g., overridden by hardware switch).
stopPause | - | Deactivation of the mode is in preparation. <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The pause mode has been deactivated. <br>All paused actions are resumed. <br>The mobile robot reports paused: "false". | The pause mode cannot be deactivated for some reason (e.g., overridden by hardware switch). | -
startHibernation | - | Activation of the hibernate mode is in preparation. If the mobile robot supports an instant transition, this state can be omitted.| - | Mobile robot is not moving. The active order has been cleared, if any. No state messages are sent by the mobile robot. <br>Hibernate mode has been activated. The mobile robot reports connection state "HIBERNATING".| The HIBERNATING connection state could not be published (e.g., overridden by a hardware switch).| -
stopHibernation | - | Deactivation of the hibernate mode is in preparation. If the mobile robot supports an instant transition, this state can be omitted.| - | Hibernate mode has been deactivated.<br>The mobile robot reports connectionState "ONLINE".| The hibernate mode could not be deactivated (e.g., overridden by a hardware switch).| -
shutdown | - | Activation of the OFFLINE connection state is in preparation. If the mobile robot supports an instant transition, this state can be omitted.| - | Mobile robot is not moving. The connection between mobile robot and broker is terminated in a coordinated way.<br>The mobile robot reports connection state "OFFLINE".| The shutdown cannot be executed for some reason (e.g., mobile robot is not in idle state, overridden by a hardware switch).| -
startCharging | - | Activation of the charging process is in progress (communication with charger is running). <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The charging process has been started. <br>The mobile robot reports powerSupply.charging: "true". | The charging process could not be started for some reason (e.g., not aligned to charger). Charging problems should correspond with an error. | The charging process could not be initiated. The mobile robot is waiting for intervention from fleet control or an operator.
stopCharging | - | Deactivation of the charging process is in progress (communication with charger is running). <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The charging process has been stopped. <br>The mobile robot reports powerSupply.charging: "false" | The charging process could not be stopped for some reason (e.g., not aligned to charger).<br> Charging problems should correspond with an error. | -
initializePosition | - | Initializing of the new pose in progress (confidence checks, etc.). <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The pose has been reset. <br>The mobile robot reports <br>mobileRobotPosition.x = x, <br>mobileRobotPosition.y = y, <br>mobileRobotPosition.theta = theta <br>mobileRobotPosition.mapId = mapId <br>mobileRobotPosition.lastNodeId = lastNodeId | The pose is not valid or cannot be reset. <br>General localization problems should correspond with an error. | -
downloadMap | Initialize the connection to the map server. | Mobile robot is downloading the map. | - | The download has finished. Mobile robot updates its state by setting the mapId/mapVersion and the corresponding mapStatus to 'DISABLED'. | The download failed, updated in mobile robot state (e.g., connection lost, Map server unreachable, mapId/mapVersion not existing on map server). | Download failed or was interrupted. The mobile robot is waiting for intervention from fleet control.
enableMap | - | The mobile robot enables the map with the requested mapId and mapVersion and disables any other map with the same mapId. | - | The map has been enabled. The mobile robot updates the corresponding mapStatus of the requested map to 'ENABLED' and the other versions with same mapId to 'DISABLED'. | The requested combination of mapId/mapVersion does not exist.| -
deleteMap | - | Mobile robot deletes map with requested mapId and mapVersion from its internal memory. | - | The map has been deleted. The mobile robot removes mapId/mapVersion from its state. | The map could not be deleted, e.g., because map is currently in use or requested combination of mapId/mapVersion has already been deleted before. | -
downloadZoneSet | Initialize the connection to the zone set server. | Mobile robot is downloading the zone set. | - | The download has finished. The mobile robot updates its state by setting a corresponding zoneSet object in its state with zoneSetStatus 'DISABLED'. | The download failed, updated in mobile robot state (e.g., connection lost, server unreachable, zone set not existing, zone set with same zoneSetId already on mobile robot). | Download failed or was interrupted. The mobile robot is waiting for intervention from fleet control.
enableZoneSet | - | Mobile robot enables the zone set with the requested zoneSetId and disables any other zone set for the same mapId. | - | The zone set has been enabled. The mobile robot updates the corresponding zoneSetStatus of the requested zoneSet to 'ENABLED' and the other zone sets for the same mapId to 'DISABLED'. | The requested zone set does not exist.| -
deleteZoneSet | - | Mobile robot deletes the zone set with requested zoneSetId from its internal memory. | - | The zone set has been deleted. The mobile robot removes zoneSet object from its state. | The zone set could not be deleted, deleted, e.g., because zone set is currently in use or the requested zone set has already been deleted before. | -
clearInstantActions | - | | - | The instant actions array has been cleaned from all FINISHED or FAILED instantActions. | - | -
clearZoneActions | - | | - | The zone actions array has been cleaned from all FINISHED or FAILED instantActions. | - | -
stateRequest | - | - | - | The state has been communicated | - | -
logReport | - | The report is being generated. <br>If the mobile robot supports an instant generation, this state can be omitted. | - | The report has been stored. <br>The name of the log is reported as part of the action state. | The report can not be stored (e.g., no space).| -
pick | Initializing of the pick process, e.g., outstanding lift operations. | The pick process is running (mobile robot is moving into station, load handling device is busy, communication with station is running, etc.). | The pick process is being paused, e.g., if a safety field is violated. <br>After removing the violation, the pick process continues. | Pick has been done. <br>Load has entered the mobile robot and mobile robot reports new load state. | Pick failed, e.g., station is unexpected empty. <br> Failed pick operations should correspond with an error. | Pick failed, but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
drop | Initializing of the drop process, e.g., outstanding lift operations. | The drop process is running (mobile robot is moving into station, load handling device is busy, communication with station is running, etc.). | The drop process is being paused, e.g., if a safety field is violated. <br>After removing the violation the drop process continues. | Drop has been done. <br>Load has left the mobile robot and mobile robot reports new load state. | Drop failed, e.g., station is unexpected occupied. <br>Failed drop operations should correspond with an error. | Drop failed, but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
detectObject | - | Object detection is running. | - | Object has been detected. | Could not detect the object. | Object detection failed, but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
finePositioning | - | Mobile robot positions itself exactly on a target. | The fine positioning process is being paused, e.g., if a safety field is violated. <br> The fine positioning continues after e.g. the violation had been resolved. | Goal position in reference to the station has been reached. | Goal position in reference to the station could not be reached. | Fine positioning failed but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
waitForTrigger | - | Mobile robot is waiting for the trigger | - | Trigger has been triggered. | waitForTrigger fails, if order has been canceled. | -
cancelOrder | - | Mobile robot is stopping or driving, until it reaches the next node. | - | Mobile robot is not moving. Mobile robot has canceled executing the order and is in idle state. | <br>Mobile robot has no active order<br>The previous order has already been canceled.<br>Passed orderId does not match the currently active orderId. | -
factsheetRequest | - | - | - | The factsheet has been communicated | - | -
updateCertificate | - | Mobile robot is downloading and installing certificates | - | Certificates have been downloaded, installed and are active. | Download or installation failed. | -

>Table 5 - Expected behavior in action states of predefined actions

#### 6.2.3.3 Update mobile robot certificate

For security reasons, mobile robot communication (at least for fleet management) should be secured. Typically, communication to the MQTT broker is secured via TLS, which requires one or more root certificates and a mobile robot-specific key pair. The parameter `service` specifies the service (e.g., 'MQTT') for which the certificates are to be used. The parameter `certificateAuthorityDownloadLink` specifies the URL for the root certificate(s). The parameters `certificateDownloadLink` and `keyDownloadLink` specify the URLs for the mobile robot-specific public and private keys.

The download shall be secured via TLS as well, since the sender of the instantAction cannot be verified. It is also advisable to validate the certificate chain before it is activated.

## 6.3 Maps

To ensure consistent navigation among different types of mobile robots, the position is always specified in reference to the project-specific coordinate system (see Figure 12). The project-specific coordinate system is referring to the coordinate system that is defined for the interaction between fleet control and the mobile robot.
For the differentiation between different levels of a site or location, a unique `mapId` is used.
The map coordinate system is to be specified as a right-handed coordinate system with the z-axis pointing skywards.
A positive rotation therefore is to be understood as a counterclockwise rotation.
The mobile robot coordinate system is also specified as a right-handed coordinate system (ISO 9787 4.1) with the x-axis pointing in the forward direction of the mobile robot and the z-axis pointing upward (ISO 9787 5.5). The mobile robot reference point is defined as (0,0,0) in the mobile robot reference frame, unless specified otherwise.

![Figure 12 Coordinate system with sample mobile robot and orientation](./assets/coordinate_system_vehicle_orientation.png)
>Figure 12 - Coordinate system with sample mobile robot and orientation

The X, Y, and Z coordinates shall be given in meters.
The orientation shall be in radians and shall be within -Pi and +Pi.

### 6.3.1 Map distribution

To enable an automatic map distribution and intelligent management of restarting the mobile robots if necessary, fleet control can manage the maps on the mobile robot.

The map files to be distributed are stored on a dedicated map server that is accessible by the mobile robots. To ensure efficient transmission, each transmission should consist of a single file. If multiple maps or files are required, they should be bundled or packed into a single file. The process of transferring a map from the map server to a mobile robot is a pull operation, initiated by the fleet control triggering a download command using an `instantAction`.

Each map is uniquely identified by a combination of a map identifier (field `mapId`) and a map version (field `mapVersion`). The map identifier describes a specific area of the mobile robot's physical workspace, and the map version indicates updates to previous versions. Before accepting a new order, the mobile robot shall check that there is a map on the mobile robot for each map identifier in the requested order. If a corresponding `mapId` is missing in the list of available maps, the mobile robot shall report an error of type 'UNKNOWN_MAP_ID' and level 'WARNING'. It is the responsibility of the fleet control to ensure that the correct maps are enabled to operate the mobile robot.

In order to minimize downtime and make it easier for the fleet control to synchronize the process of enabling of new maps, maps shall be pre-loaded or buffered on the mobile robots. The status of the maps on the mobile robot is reflected in the mobile robot's state. Transferring a map to a mobile robot and enabling the map are different processes. To enable a pre-loaded map on a mobile robot, the fleet control shall send an instant action. As a result, any other map with the same map identifier but a different map version shall be disabled by the mobile robot.

Deletion of maps can also be done by the fleet control via an instant action.

The map distribution process is shown in Figure 13.

![Figure 13 Map distribution process](./assets/map_distribution_process.png)
>Figure 13 - Communication required between fleet control, mobile robot and map server to download, enable, and delete a map.

### 6.3.2 Maps in the mobile robot state

The `mapId` field in the `mobileRobotPosition` of the state represents the currently active map.

Information about the maps available on a mobile robot is presented in the `maps` array, which is a component of the state message. Each entry in this array is a JSON object consisting of the mandatory fields `mapId`, `mapVersion`, and `mapStatus`, which can be either 'ENABLED' or 'DISABLED'. An 'ENABLED' map can be used by the mobile robot if necessary. A 'DISABLED' map shall not be used. The status of the download process is indicated by the current action not being completed. Errors are also reported in the state.
Note that multiple maps with different `mapId` can be enabled at the same time. There shall only be one version of maps with the same `mapId` enabled at a time. If the `maps` array is empty, no maps are currently available on the mobile robot.

### 6.3.3 Map download

The map download shall be triggered by the `downloadMap` instant action from the fleet control. It shall contain the mandatory parameters `mapId` and `mapDownloadLink` under which the map is stored on the map server and which can be accessed by the mobile robot.

The mobile robot sets the `actionStatus` to 'RUNNING' as soon as it starts downloading the map file. If the download is successful, the `actionStatus` is updated to 'FINISHED'. If the download is unsuccessful, the status is set to 'FAILED'. Once the download has been successfully completed, the map shall be added to the array of `maps` in the state. Maps shall not be reported in the state until they are ready to be enabled.

The process of downloading a map shall not modify, delete, enable, or disable any existing maps on the mobile robot.
The mobile robot shall reject the download of a map with a `mapId` and `mapVersion` that is already on the mobile robot. An error of type 'DUPLICATE_MAP' and level 'WARNING' shall be reported, and the status of the instant action shall be set to 'FAILED'. The fleet control shall first delete the map on the mobile robot and then restart the download.

### 6.3.4 Enable downloaded maps

There are two ways to enable a map on a mobile robot:

1. **Fleet control enables map**: Use the `enableMap` instant action to set a map to 'ENABLED' on the mobile robot. Other Versions of the same `mapId` with different `mapVersion` are set to 'DISABLED'.
2. **Manually enable a map on the mobile robot**: In some cases, it might be necessary to enable the maps on the mobile robot directly. The result shall be reported in the mobile robot state.

Fleet control shall ensure that the correct maps are activated on the mobile robot when sending the corresponding `mapId` as part of a `nodePosition` in an order.
If the mobile robot is to be set to a specific position on a new map, the `initializePosition` instant action shall be used.

### 6.3.5 Delete maps on the mobile robot

The fleet control can request the deletion of a specific map from a mobile robot. This shall be done by using the instant action `deleteMap`. When a mobile robot runs out of memory, it should report this to the fleet control, which can then initiate the deletion of maps. The mobile robot itself shall not delete maps.
After successfully deleting a map, the mobile robot shall remove the corresponding entry from its `maps` array in the state message.

## 6.4 Zones

Zones are used to define rules for specific areas of the mobile robot workspace. In this way, zones allow mobile robots to navigate freely between nodes while giving the fleet control the ability to manage traffic. Zones can be used to locally deny mobile robots access to areas or to link access to conditions (zone types: 'BLOCKED' and 'RELEASE'). It is also possible to enforce specific behavior while within the zone (zone types: 'LINE_GUIDED', 'SPEED_LIMIT', 'COORDINATED_REPLANNING', and 'ACTION') or influence the driving behavior by incentivizing or penalizing certain areas (zone types: 'PRIORITY' and 'PENALTY') or giving a predefined driving direction (zone types: 'DIRECTED', 'BIDIRECTED'). The zone types are defined in the following sections.

Potential conflicts in orders due to overlapping of zones or combination of zone and edge properties and how to resolve them are addressed in section [6.4.4 Interaction between zones](#644-interactions-between-zones). For released nodes that are part of the order but are restricted due to zones (e.g., node located within a 'BLOCKED' or 'RELEASE' zone), the robot is expected to act according to the zones (e.g., not enter or wait for 'GRANTED' state of the request).
Some mobile robots cannot process zones at all, while other mobile robots might only be able to work with a certain subset of zone types, such as 'BLOCKED'. All mobile robots shall therefore report to fleet control which zones they are able to understand by adding the according zone names to the `supportedZones` array under `typeSpecifications` in their factsheet.
Also (virtually) line-guided mobile robots can choose to support zone-based navigation if they can implement the logic of the corresponding zone types defined in the following.
A zone set shall only be changed and distributed by fleet control to keep consistency in the system.

### 6.4.1 Zone types

Two categories of zones are distinguished: contour-based zones and kinematic center-based zones. This distinction is based on the different conditions for when the mobile robot is considered to be entering and exiting zones.

#### 6.4.1.1 Contour-based zones

For contour-based zones, the contour of the mobile robot (including its load) determines zone entry and exit. Any part of the contour entering the zone is a zone entry. As soon as no part of the mobile robot's contour remains within the zone, it is a zone exit.

![Figure 14 Depiction of a mobile robot entering a zone based on its contour (left) and a loaded mobile robot with corresponding extended bounding box exiting a zone (right)](./assets/contour_entry.png)
>Figure 14 - Depiction of a mobile robot entering a zone based on its contour (left) and a loaded mobile robot with corresponding extended bounding box exiting a zone (right)

The following contour-based zones are defined:

| **Zone Type**| **Zone Parameters** | **Data type** | **Description** |
| --- | --- | --- | --- |
| BLOCKED | none | | Mobile robots shall not enter this zone. If a mobile robot has entered the zone or finds itself within one, it shall stop and throw an 'BLOCKED_ZONE_VIOLATION' error with level set to 'CRITICAL'.|
| LINE_GUIDED | none | | No free navigation is allowed in this zone, mobile robots shall follow the predefined trajectories on edges. Mobile robots may only enter this zone if the route is explicitly specified by the fleet control in the form of a node-edge graph. Any movement of the mobile robot that requires it to enter this zone shall follow a predefined trajectory. When entering the zone, the mobile robot shall be on the trajectory of the edge that crosses the zone. The edges that enter and are inside the line-guided zone require a trajectory sent from the fleet control or a predefined trajectory on the mobile robot. A corridor can be sent to allow the mobile robot to deviate from the trajectory. |
| RELEASE | | - | Mobile robots are only allowed entering this zone once they have been granted access through fleet control. |
| | releaseLossBehavior | string | Enum {'STOP', 'CONTINUE', 'EVACUATE'}<br>When the access to this zone is revoked or expired, the mobile robot can either 'STOP', 'CONTINUE', or 'EVACUATE' the zone. This action is only executed, when the mobile robot is already in the zone and the release expires or is revoked. If not defined, the mobile robot is expected to STOP and report an error.<br>'STOP': Mobile robot stops and sends a 'RELEASE_LOST' error with level 'CRITICAL'.<br>'EVACUATE': Execute the evacuation behavior of the mobile robot to leave the zone, keeping the `zoneRequest` object granting release in its state until the zone is left.<br>'CONTINUE': If the release is revoked or expires after the mobile robot has already entered the zone, the mobile robot continues its path, keeping the `zoneRequest` object granting the zone release in its state. If the order ends inside the zone, the mobile robot waits for a new order.|
| COORDINATED_REPLANNING | none | | No autonomous replanning is allowed within this zone. Mobile robots are only allowed adjusting their path if granted permission by fleet control. |
| SPEED_LIMIT | | | Mobile robots shall not drive faster than the defined maximum speed within this zone. |
| | maximumSpeed | float64 | Maximum permitted speed for mobile robot within the zone in m/s. The speed limit shall already be reached upon entering the zone.|
| ACTION | | | The mobile robot shall perform predefined actions when entering, traversing, or exiting the zone. The factsheet defines which actions can be executed when. |
| | entryActions[action] | array | Actions to be triggered when entering the zone. Empty array, if no actions required. |
| | duringActions[action] | array | Actions to be executed while crossing the zone. Empty array, if no actions required. |
| | exitActions[action] | array | Actions to be triggered when leaving the zone. Empty array, if no actions required. |

>Table 6 - Contour-based zone types and their parameters

#### 6.4.1.2 Kinematic center-based zones

In kinematic center-based zones, the mobile robot's kinematic center determines its entry and exit of the zones. When the mobile robot's kinematic center is inside a zone, the mobile robot shall follow the defined behavior.
'PRIORITY' and 'PENALTY' zones are zones which only influence the path planning of mobile robots.
'DIRECTED' zones define a preferred direction of travel within the zone. 'BIDIRECTED' zones define a travel direction and its opposite direction to be used. Other directions shall be avoided. The `directedLimitation` and `bidirectedLimitation` enums specify the limits within which the mobile robot may deviate from its direction of travel. The direction of travel is the velocity vector in the project-specific coordinate system.

![Figure 15 Depiction of a mobile robot entering a zone based on its kinematic center (left) and a loaded mobile robot exiting a zone based on its kinematic center (right)](./assets/kinematic_center_entry.png)
>Figure 15 - Depiction of a mobile robot entering a zone based on its kinematic center (left) and a loaded mobile robot exiting a zone based on its kinematic center (right)

| **Zone Type**| **Zone Parameters** | **Data type** | **Description** |
| --- | --- | --- | --- |
| PRIORITY | | | The workspace encompassed by this zone is associated with an incentive for the mobile robot to plan its route through this zone compared to an otherwise equivalent area without such a zone on the map.|
| | priorityFactor | float64 | [0.0...1.0]<br>Relative factor that determines the preference of the zone over a workspace without a zone. 0.0 means no preference, as if there was no zone, 1.0 is maximum preference.|
| PENALTY | | | The workspace encompassed by this zone is associated with a disincentive for the mobile robot to plan its route through this zone compared to an otherwise equivalent area without such a zone on the map.|
| | penaltyFactor | float64 | [0.0...1.0]<br> Relative factor that determines the penalty of the zone compared to a workspace without that zone. 0.0 means no penalty, as if there was no zone, 1.0 is the maximum penalty, causing the mobile robot to take this path only if it cannot find any other feasible route. |
| DIRECTED | | | Mobile robots shall traverse this zone in a specific direction of travel. |
| | direction | float64 | Preferred direction of travel within the zone in radians. The direction of travel is the angular orientation of the mobile robot's velocity vector in the project-specific coordinate system. |
| | directedLimitation | string | Enum {'SOFT','RESTRICTED','STRICT'}<br>SOFT: Mobile robots may deviate from the defined direction of travel, but should avoid it, RESTRICTED: The mobile robot may deviate from the defined direction of travel, e.g., to avoid an obstacle, but shall never traverse opposite to the defined direction of travel, STRICT: The mobile robot shall maintain the defined direction of travel as precisely as its technical capabilities allow. |
| BIDIRECTED | | | While in this zone, mobile robots shall only move in the defined direction of travel and its direct opposite (+ Pi), mobile robots should not cross this zone in any other direction. |
 | direction | float64 | Preferred direction of travel within the zone in radians. The direction of travel is the angular orientation of the mobile robot's velocity vector in the project-specific coordinate system.|
| | bidirectedLimitation | string | Enum {'SOFT', 'RESTRICTED'}<\br>SOFT: Mobile robots may deviate from the defined directions of travel, but should avoid it, RESTRICTED: The mobile robot shall not traverse in any other direction than the directions of travel, except for obstacle avoidance. |

>Table 7 - Kinematic center-based zone types and their parameters

### 6.4.2 Zone set transfer

Zone sets shall only be changed and distributed by fleet control to keep consistency in the system. The preferred way to distribute zone sets is via the `zoneSet` topic. If the mobile robot supports zones, the update via the `zoneSet` topic shall be supported. Larger zone sets can also be shared through the `downloadZoneSet` instant action, following the map distribution concept in figure 13.

A `zoneSet` is an array of `zone` objects with a globally unique identifier, `zoneSetId`. It is associated with a single map referenced through the `mapId`. The `mapVersion` shall not be referenced, as the same zone set might be intended to be used for several versions of one map. In general, several zone sets can be defined in addition to a single map and it is upon fleet control to ensure that the right zone set is enabled for each map on the mobile robot. As with maps, the `zoneSetStatus` indicates which zone set is currently used by the mobile robot. Only a single zone set can be active at once for each `mapId` on the mobile robot. Zones shall not extend beyond the spatial boundaries of a map.
The content of a zone set with a unique `zoneSetId` shall not change. If changes are required within a zone set, it shall be referenced with a new `zoneSetId`.

The `zoneSetStatus` of a newly added zone set shall always be set to 'DISABLED' and shall be enabled through the `enableZoneSet` instant action before use.

If the mobile robot receives a new zone set via the `zoneSet` topic or `downloadZoneSet` instant action with the same `zoneSetId` as an existing one, it shall not take over the zone set in its internal memory and report an error of type 'DUPLICATE_ZONE_SET' and level 'WARNING' for a reasonable amount of time for the fleet control to notice that the zone update failed.

## 6.4.3 Communication for interactive zones

For communicating requests for the interactive zones 'RELEASE' and 'COORDINATED_REPLANNING', the field `zoneRequests` in the state message is used. The separate topic `responses` is used by fleet control to respond to these requests.

Before entering an interactive zone, the mobile robot shall state a request.
A request before entry of an interactive zone is necessary, even if the order contains released nodes within the zone.
The mobile robot decides at which point before entering the zone to make its requests.
If the response is not received in time, the mobile robot shall not enter the zone.

Requests shall only be made for zones of enabled zone sets. Zone requests can also be made for zone sets belonging to maps that the mobile robot is not currently on.

The `requestId` allows fleet control to distinguish between different requests and allows the mobile robot to issue several alternative requests for the same zone at the same time.
Each request attempt shall use a unique identifier per mobile robot. Ids can be reused after a mobile robot restart.

For requests to enter a 'RELEASE' zone, a `zoneRequest` object of `requestType` 'ACCESS' shall be added to the state message.
For permission to enter a 'COORINATED_REPLANNING' zone with a planned path or for replanning its path within the zone, the `requestType` shall be set to 'REPLANNING'.
For a 'REPLANNING' request, the planned path shall be added as NURBS to the `trajectory` field of the `zoneRequest`. Multiple requests with different trajectories for the same zone can be made. Each path shall be requested with its own `zoneRequest` object.
If a mobile robot requires access to a workspace covered by two or more 'RELEASE' zones, it shall request access and receive approval for all necessary zones before entering the area.
If a mobile robot navigates through a workspace on the map that is covered by two or more 'COORDINATED REPLANNING' zones, it shall request its path within this area individually for each zone and receive approval from the fleet control before entering or changing paths.

The parameter `requestStatus` shall be initially set to 'REQUESTED' by the mobile robot when stating its request.

Fleet control responds to zone requests via the `responses` topic.
The response message contains an array of `response` objects. Each `response` shall only respond to a single request referenced by the `requestId`.
Each response has a `responseType` that is either 'GRANTED', 'QUEUED', 'REVOKED', or 'REJECTED'.
If the `responseType` is 'GRANTED', the mobile robot is allowed to enter the zone or use the requested trajectory.
Fleet control can set the `responseType` to 'QUEUED' to acknowledge the mobile robot's request without giving permission, informing the mobile robot that its request is being processed.
If the `responseType` is 'REJECTED', the mobile robot shall not enter the zone or use the requested trajectory.
The `responseType` 'REVOKED' indicates that the permission is no longer valid. The fleet control shall assume a 'REVOKED' request as still being 'GRANTED', until the `requestStatus` of the mobile robot is set to 'REVOKED'.
The `response` object can include a `leaseExpiry` which specifies until when a 'GRANTED' request is valid. To extend the `leaseExpiry` fleet control can resend a response message with an updated `leaseExpiry` time.

The mobile robot shall acknowledge the fleet controls response by setting the `requestStatus` accordingly and keep the request for as long as it considers the information relevant. See also Section [6.9 Request/response mechanism](#69-requestresponse-mechanism).

The interaction between the mobile robot and the fleet control for 'RELEASE' zones shall be according to Figure 16.

While the mobile robot remains in the 'RELEASE' zone, it keeps the `zoneRequest` object in its state and continues to report `requestStatus` as 'GRANTED' to inform fleet control that it is still inside the zone. After mobile robot has exited the zone, it shall remove the corresponding `zoneRequest` entry from its state message.
When receiving a response with `responseType` 'REVOKED', the mobile robot shall remove the request from its state. When the `leaseExpiry` has passed, the requestStatus shall be set to 'EXPIRED' and the zone shall not be entered. If the mobile robot is already inside the 'RELEASE' zone when the `leaseExpiry` has passed or the request is 'REVOKED', it shall report a warning and react according to the `releaseLossBehavior` defined in the zone definition.

![Figure 16 Zone request behavior for a RELEASE zone.](./assets/request_release_zone_access.png)
>Figure 16 - Zone request behavior for a RELEASE zone.

The interaction between the mobile robot and the fleet control for 'COORDINATED_REPLANNING' zones shall be according to Figure 17.

The mobile robot shall choose one of the trajectories of all 'GRANTED' requests to the zone and set the corresponding `requestStatus`to 'GRANTED' while removing all other requests from its state.
When receiving a response with `responseType` 'REVOKED', the mobile robot shall remove the request from its state and not enter the 'COORDINATED_REPLANNING' zone. When the `leaseExpiry` has passed, the `requestStatus` shall be set to 'EXPIRED' and the zone shall not be entered. If the mobile robot is already inside the 'RELEASE' zone when the `leaseExpiry` has passed or the request is 'REVOKED', it shall stop driving and report a warning. To continue, the mobile robot shall state a new request.

![Figure 17 Zone request behavior for a COORDINATED_REPLANNING zone.](./assets/request_coordinated_replanning_zone_replanning.png)
>Figure 17 - Zone request behavior for a COORDINATED_REPLANNING zone.

### 6.4.4 Interactions between zones

In the following matrix possible interactions between zones are described. The matrix is symmetric, as the interaction between two zones is the same, regardless of the order in which they are considered. For each combination, there is either a zone behavior that is overrulling the other (e.g., a 'BLOCKED' zone overrules a 'LINE_GUIDED' zone) or there is no conflict (e.g., a 'LINE_GUIDED' zone and a 'COORDINATED_REPLANNING' zone). 'DIRECTED' and 'BIDIRECTED' zones shall not overlap, since this might lead to an undefined behavior. The column No Zone defines the behavior for contour-based zones, where mobile robots can be inside a defined zone type and an area without a zone at the same time. For kinematic center-based zones the mobile robot can only be completely within or outside the zone, so there is no possible interaction.

| |**BLOCKED**|**RELEASE**|**LINE_GUIDED**|**COORDINATED_REPLANNING**|**SPEED_LIMIT**|**ACTION**|**PRIORITY**|**PENALTY**|**DIRECTED**|**BIDIRECTED**|**No Zone**|**EDGE-PROPERTIES**
---|---|---|---|---|---|---|---|---|---|---|---|---
**BLOCKED**|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|
**RELEASE**||No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict
**LINE_GUIDED**|||No conflict|LINE_GUIDED|No Conflict| (1) |LINE_GUIDED|LINE_GUIDED|LINE_GUIDED|No conflict|LINE_GUIDED|No conflict
**COORDINATED_REPLANNING**||||(2)|No conflict|(1)|No conflict|No conflict|No conflict|No conflict|COORDINATED_REPLANNING|(3)
**SPEED_LIMIT** |||||(4)|No conflict|No conflict|No conflict|No conflict|No conflict|SPEED_LIMIT|(4)
**ACTION** ||||||(5)|No conflict|No conflict|No conflict|No conflict|ACTION|(5)
**PRIORITY** |||||||(6)|(6)|No conflict|No conflict|(7)|No conflict
**PENALTY** ||||||||(6)|No conflict|No conflict|(7)|No conflict
**DIRECTED** |||||||||(8)|(8)|(7)|(9)
**BIDIRECTED** ||||||||||(8)|(7)|(9)

>Table 8 - Interaction matrix for zones

1) If actions would conflict with other zones' behavior, report a 'ZONE_ACTION_CONFLICT' error with level 'CRITICAL' (order error) and stop the mobile robot.
2) Planned trajectory required to be granted for all 'COORDINATED_REPLANNING' zones.
3) If a trajectory is predefined for the edge, it shall be sent in the zone request.
4) The lowest of the competing `maximumSpeed` values applies.
5) Execute all actions.
6) The most restrictive one is always selected here; for PRIORITY zones, the lowest `priorityFactor` is used; for overlapping PRIORITY and PENALTY zones, the highest `penaltyFactor` is used; for overlapping PENALTY zones, the highest `penaltyFactor` is used.
7) For kinematic center-based zones the mobile robot can only be completely within or outside the zone, so this overlap is not possible.
8) Zones shall not overlap, since the behavior is not defined.
9) A `trajectory` as part of the edge properties shall override the directed and bidirected zones.

### 6.4.5 Error handling within zones

If at any point of the order execution, a mobile robot realizes, that it can not reach a node in its order, it shall report a 'NODE_UNREACHABLE' error with level 'CRITICAL' to the fleet control. The fleet control shall then decide how to proceed. The mobile robot shall not try to reach the node again, but wait for further instructions from the fleet control.

## 6.5 Connection

During the connection of a mobile robot client to the broker, a last will topic and message shall be set, which is published by the broker upon disconnection of the mobile robot client from the broker.
Thus, the fleet control can detect a disconnection event by subscribing the connection topics of all mobile robots.
The disconnection is detected via a heartbeat that is exchanged between the broker and the client.
Thus, the fleet control can detect a disconnection event by subscribing to the `connection` topic of each mobile robot.

As a result, the timestamp and headerId fields will always be outdated.

Mobile robot wants to disconnect gracefully:

1. Mobile robot sends "vda5050/v3/manufacturer/serialNumber/connection" with `connectionState` set to `OFFLINE`.
2. Disconnect the MQTT connection with a disconnect command.

Mobile robot comes online:

1. Set the last will to "vda5050/v3/manufacturer/serialNumber/connection" with the field `connectionState` set to 'CONNECTION_BROKEN', when the MQTT connection is created.
2. Send the topic "vda5050/v3/manufacturer/serialNumber/connection" with `connectionState` set to 'ONLINE'.

All messages on this topic shall be sent with a `retained` flag.

When connection between the mobile robot and the broker stops unexpectedly, the broker will send the last will to the topic: "vda5050/v3/manufacturer/serialNumber/connection" with the field `connectionState` set to 'CONNECTION_BROKEN'.

## 6.6 State

The mobile robot state shall be published on a single topic.
Compared to separate messages (e.g., for current order progress, battery state and errors), using a single topic reduces the workload of both the broker and the fleet control system when handling messages, while also keeping the mobile robot state information synchronized.

The mobile robot state message shall be published when relevant events occur or at least every 30 seconds.

The following events shall trigger a transmission of the state message:

- Receiving an order
- Receiving an order update
- Changes in the `load` object
- Change in the `errors` array
- Change in the `operatingMode` field
- Change in the `driving` field
- Change in the `paused` field
- Change in the `safetyState` object
- Change in the `newBaseRequest` field
- Change in the `lastNodeId` or `lastNodeSequenceId` field
- Change in the `edgeRequests` or `zoneRequests` arrays
- Change in the `powerSupply.charging` field
- Change in the `nodeStates` or `edgeStates` arrays
- Change in the `actionStates`, `instantActionStates` or `zoneActionStates` arrays
- Change in the `zoneSets` array
- Change in the `maps` array

*Remark: For above mentioned arrays, changes in the individual items of the array as well as adding or removing entries shall trigger a state message transmission.*

There should be an effort to curb the amount of communication.
If two events correlate with each other (e.g., the receiving of a new order usually forces an update of the `nodeStates` and `edgeStates`; as does the driving over a node), it is sensible to trigger one state update instead of multiple. The minimum time between two consecutive state messages is defined by the factsheet ([7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message) `protocolLimits.timing.minimumStateInterval`) .

### 6.6.1 Concept and logic

The order progress is tracked by the `nodeStates` and `edgeStates`.
Additionally, if the mobile robot is capable of determining its current position, it shall publish it via the `mobileRobotPosition` field.

The `nodeStates` and `edgeStates` include all upcoming nodes and edges for the mobile robot to traverse.

![Figure 18 Order information provided by the state topic. Only the ID of the last node and the remaining nodes and edges are transmitted](./assets/order_information_state_topic.png)
>Figure 18 - Order information provided by the state topic. Only the ID of the last node and the remaining nodes and edges are transmitted

### 6.6.2 Traversal of nodes and edges

The mobile robot decides on its own when a node should count as traversed.
A requirement for the traversal is that the mobile robot's control point shall be within the node's `allowedDeviationXY` and its orientation within `allowedDeviationTheta`.
The `allowedDeviationXY` defines at what point a line-guided mobile robot can deviate from its predefined trajectory, to cut the corner along a smoother path rather than reaching the node's exact position. When leaving the `allowedDeviationXY` the mobile robot shall be back on its predefined trajectory of the subsequent edge.
If the edge attribute `corridor` of the subsequent edge is set, these boundaries should be met additionally.

In case the mobile robot is located too far away from the first node of an order, the fleet control can add an extended `allowedDeviationXY` to this node to include the mobile robot's current position.

The mobile robot shall report the traversal of a node by removing its `nodeState` from the `nodeStates` array and setting the `lastNodeId` and `lastNodeSequenceId` to the traversed node's values.

As soon as the mobile robot reports the node as traversed, the mobile robot shall trigger the actions associated with the node, if any.
The traversal of a node also necessarily implies leaving the edge that is leading up to the node.
The edge shall then also be removed from the `edgeStates` and the actions that were active on the edge shall be finished.

The traversal of the node also marks the moment when the mobile robot enters the following edge, if there is one.
The edge's actions shall be triggered, if any.
An exception to this rule is if the mobile robot shall stop on the node (because of a soft or hard blocking action) – then the mobile robot only enters the following edge once it begins driving again.

When an active order exists, the fields `lastNodeId` and `lastNodeSequenceId` shall be updated only when the mobile robot traverses a released node that is part of this order. For example if a physically line‑guided mobile robot detects a physical marker/tag that is not part of the active order’s `nodes`, this detection shall not lead to a change of `lastNodeId` or `lastNodeSequenceId`.

![Figure 19 Depiction of nodeStates, edgeStates, and actionStates during order handling](./assets/states_during_order_handling.png)
>Figure 19 - Depiction of `nodeStates`, `edgeStates`, and `actionStates` during order handling

#### 6.6.2.1 Definition of allowedDeviationXY as an ellipse

The allowedDeviationXY is defined as an ellipse around the node position to allow more flexible approaches to the node.

![Figure 20 allowedDeviationXY ellipse](./assets/ellipse.png)
>Figure 20 - allowedDeviation ellipse

### 6.6.3 Base request

If the mobile robot detects that its base is running short, it can set the `newBaseRequest` flag to "true" to attempt to prevent unnecessary braking.

### 6.6.4 Information

The mobile robot can submit arbitrary additional information to the fleet control via the `information` array.
It is up to the mobile robot to decide how long it reports information via an information message.

The fleet control shall not use the information for logic; they shall only be used for visualization and debugging purposes.

### 6.6.5 Errors

The mobile robot reports any issues via the `errors` array.

#### 6.6.5.1 Error levels

The issues can have four levels: 'WARNING', 'URGENT', 'CRITICAL', and 'FATAL'.

- A 'WARNING' level issue does not require immediate attention. The mobile robot can continue its current order and is able to take new orders. The error might be self-resolving, e.g., a dirty LiDar-scanner.
- An 'URGENT' level issue, e.g., a low battery level, requires immediate attention. The mobile robot can continue its current order and is able to take new orders.
- A 'CRITICAL' level issue requires immediate attention, e.g., trying to pick an object, that is not there. The mobile robot shall not continue driving since it can not continue its current order but is able to take new orders.
- A 'FATAL' level issue requires user intervention, e.g., losing localization. The mobile robot shall not continue driving since it can neither continue its currently active order nor take any new orders.

The mobile robot can add references that help with finding the cause of the error via the `errorReferences` array.
The fields `errorDescription` and `errorHint` may provide human-readable text explaining the error or suggesting a possible resolution.

Regardless of the level of the issue, the mobile robot shall never clear its order due to it.

#### 6.6.5.2 Error references

If an error occurs due to an erroneous order or execution failure, the mobile robot can return meaningful error references in the field `errorReferences` to support finding the cause of the error.
This can include the following information:

- `headerId`
- Topic (`order` or `instantAction`)
- `orderId` and `orderUpdateId` if error was caused by an order update
- `actionId` if error was caused by an action
- List of parameters if error was caused by erroneous action parameters

#### 6.6.5.3 Error translations

For both `errorDescription` and `errorHint`, the mobile robot can provide translations by using the `errorDescriptionTranslations` and `errorHintTranslations` arrays.
Each translation consists of an ISO 639-1 language code and the corresponding translated text.

#### 6.6.5.4 Predefined error types

The mobile robot shall use predefined error types to report specific issues. The following table lists the predefined error types and their description.

Error Type | Error level | Description | Reference | Report duration
---|---|---|---|---
'UNSUPPORTED_PARAMETER' | 'CRITICAL' | Receival of message with an unsupported optional parameter. | Name of parameter | Until new order is accepted.
'NO_ORDER_TO_CANCEL' | 'WARNING'  | The mobile robot received a `cancelOrder` action, but it does not have an active order to cancel. | `actionId` of `cancelOrder` | Until new order is accepted.
'VALIDATION_FAILURE'|'WARNING'| Receival of malformed order. | If possible, `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'INVALID_ORDER_ACTION' | 'WARNING' | Receival of an order containing unsupported actions. | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'INVALID_INSTANT_ACTION' | 'WARNING' | Receival of an unsupported instant action. | `actionId` of `instantAction` | Until new instant action is accepted.
'OUTDATED_ORDER_UPDATE'| 'WARNING' | Receival of an order with correct `orderId` but outdated `orderUpdateId`. | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'SAME_ORDER_UPDATE_ID' | 'WARNING' | Receival of a duplicate order message (same `orderId` and `orderUpdateId`) | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'ORDER_UPDATE_FOLLOWING_CANCEL' | 'WARNING' | Receival of an order update for an order that has already been cancelled. | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'OUTSIDE_OF_CORRIDOR' | 'CRITICAL' | Leaving the corridor defined for an edge. | `edgeId` | Until the mobile robot is no longer violating the corridor boundaries.
'INSUFFICIENT_MEMORY' | 'URGENT' | Mobile robot does not have enough memory to process received order. | If possible, `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'DUPLICATE_MAP' | 'WARNING' | Receival of a map with `mapId` and `mapVersion` already existing. | `mapId` and `mapVersion` of duplicate | Until a new map related instantAction was accepted.
'BLOCKED_ZONE_VIOLATION' | 'CRITICAL' | Entering a 'BLOCKED' zone. | `zoneId` | Until the mobile robot is no longer violating the blocked zone.
'DUPLICATE_ZONE_SET' | 'WARNING' | Receival of a zone set with `zoneSetId` already existing. | `zoneSetId` or `actionId` of `instantAction` | Reasonable amount of time for the fleet control to notice that the zone update failed.
'RELEASE_LOST' | 'CRITICAL' | Losing the release for a 'RELEASE' zone. | `zoneId` | Until the mobile robot is no longer within the 'RELEASE' zone or is granted a the release again.
'ZONE_ACTION_CONFLICT' | 'CRITICAL' | Conflict between zone behavior and zone actions. | `zoneId` of 'ACTION' zone | Until the mobile robot is no longer violating the zone behavior.
'NODE_UNREACHABLE'|'CRITICAL'| The mobile robot cannot reach a node in its order. | `nodeId` | Until new order is accepted.
'LOCALIZATION_ERROR'|'FATAL'| The mobile robot is not localized. | | Until localization is regained.
'NO_ROUTE_TO_TARGET' | 'WARNING' | Receival of an order with at least one unreachable node. | `orderId` | Until new order is accepted.
'OTHER_ORDER_ACTIVE' | 'WARNING' | Receival of a new order while another order is still active. | `orderId` | Until new order is accepted.
'START_NODE_OUT_OF_RANGE' | 'WARNING' | Receival of an order with unreachable first node. | `orderId` | Until new order is accepted.
'MOBILE_ROBOT_NOT_AVAILABLE' | 'WARNING' | Receival of an order while not in 'AUTOMATIC', 'SEMIAUTOMATIC' or 'INTERVENED' operating mode. | `orderId` | Until operating mode allows for new orders
'UNKNOWN_MAP_ID' | 'WARNING' | Receival of an order containing nodes referencing an unknown `mapId`. | `orderId` | Until new order is accepted.

> Table 9 - Predefined error types

### 6.6.6 Operating Mode

For regular order execution, fleet control shall be in full control of the mobile robot. There are however situations where this is not possible, e.g., when manual interaction on the mobile robot is required. The mobile robot shall report this using the field `operatingMode`.

The following lists describe the values of the field `operatingMode`, their meaning, and implications on the interaction between mobile robot and fleet control:

Operating Mode | Description
---|---
AUTOMATIC | Fleet control is in full control of the mobile robot. <br>Mobile robot moves and executes actions based on orders from the fleet control.
SEMIAUTOMATIC | Fleet control is in control of the mobile robot.<br> Mobile robot moves and executes actions based on orders from the fleet control. <br>The driving speed is controlled by the HMI.<br>The steering is under automatic control.
INTERVENED | Fleet control is not in control of the mobile robot. The mobile robot is reporting its state correctly.<br>HMI can be used to control the steering, velocity and handling devices of the mobile robot.<br>Fleet control is allowed to send orders or order updates to the mobile robot to be executed after changing back into operating mode 'AUTOMATIC' or 'SEMI-AUTOMATIC'. Fleet control shall not send any instant action except `cancelOrder`.<br>The mobile robot shall not clear the order but shall remove all zone requests from the state, also if the mobile robot is already inside a 'RELEASE' zone. (*Remark: If necessary, the fleet control can continue to track the position of the mobile robot and decide whether clearance for other mobile robots is possible.*) The mobile robot shall not request any permissions to enter a 'RELEASE' zone or for replanning inside a 'COORDINATED_REPLANNING' zone.<br>If entering operating mode 'INTERVENED' has any impact on running actions the mobile robot shall reflect this in the state message accordingly.<br>If the mobile robot leaves this operating mode and does not directly switch into 'AUTOMATIC' or 'SEMI-AUTOMATIC' mode it shall act according to new operating mode. If the mobile robot leaves this operating mode and switches directly into 'AUTOMATIC' or 'SEMI-AUTOMATIC' mode the mobile robot shall continue executing any current order. If the mobile robot detects during operating mode 'INTERVENED' that a continuation of the current order is not possible the mobile robot shall switch into operating mode 'MANUAL' and act accordingly.
MANUAL | Fleet control is not in control of the mobile robot. <br>Fleet control shall not send orders or actions to the mobile robot. <br>HMI can be used to control the steering, velocity and handling devices of the mobile robot.<br>The position of the mobile robot is sent to the fleet control.<br>When the mobile robot enters this mode, it immediately clears any current order.<br>If, while being in this mode, the mobile robot detects that it is being moved to a position where the current value of `lastNodeId` cannot be used as a start node of a new order, it shall set `lastNodeId` to an empty string ("").
STARTUP | Fleet control is not in control of the mobile robot. The mobile robot is starting up and not ready to receive orders. State message parameters may be incomplete or invalid until startup is finished.
SERVICE | Fleet control is not in control of the mobile robot. <br>Fleet control shall not send orders or actions to the mobile robot. <br>When the mobile robot enters this mode, it immediately clears any current order.<br>The mobile robot shall set `lastNodeId` to an empty string ("").<br>Authorized personnel can reconfigure the mobile robot.
TEACH_IN | Fleet control is not in control of the mobile robot. <br>Fleet control shall not send orders or actions to the mobile robot. <br>When the mobile robot enters this mode, it immediately clears any current order.<br>The mobile robot shall set `lastNodeId` to an empty string ("").<br>The mobile robot is being taught, e.g., mapping is done by an operator.

>Table 10 - Operating modes of the mobile robot

Operating Mode | Fleet Control in control | Valid state message content | Clear order when entering | Set `lastNodeId` to empty | Clear zone requests when entering | Sending instant actions allowed | Sending orders allowed
--- | --- | --- | --- | --- | --- | --- | ---
AUTOMATIC | YES | YES | NO | NO | NO | YES | YES
SEMIAUTOMATIC | YES | YES | NO | NO | NO | YES | YES
INTERVENED | NO | YES | NO | NO | YES | Only `cancelOrder` allowed | YES
MANUAL | NO | YES | YES | YES, if continuation of order is not possible | YES | NO | NO
STARTUP | NO | NO | YES | YES | YES | NO | NO
SERVICE | NO | YES | YES | YES | YES | NO | NO
TEACH_IN | NO | YES | YES | YES | YES | NO | NO

>Table 11 - Overview of operating modes and their implications

### 6.6.7 Clearing the order on the mobile robot

In response to one of the following events, the mobile robot shall stop executing the current order:

- The mobile robot is changing the operating mode to 'MANUAL', 'STARTUP', 'SERVICE' or 'TEACH_IN' (see also [6.6.6 Operating Mode](#666-operating-mode)).
- The mobile robot receives a `cancelOrder` instant action from fleet control.
- The mobile robot receives a `startHibernation` instant action.

In these cases the mobile robot shall clear its current order which means that:

- Any scheduled actions in the `actionStates` shall be cancelled and be reported as 'FAILED' in `actionStates`.
- Any running action in the `actionStates` that
	- can be cancelled (cancelAllowed = true) shall be cancelled and be reported as 'FAILED' in `actionStates`.
	- cannot be cancelled (cancelAllowed = false) shall be reflected by reporting 'RUNNING' while being executed, and afterwards as the respective state ('FINISHED' if successful, 'FAILED' otherwise).
- The value of `orderId`, `orderUpdateId`, `lastNodeId` and `lastNodeSequenceId` remain unchanged.
- The arrays `nodeStates` and `edgeStates` are set to empty lists.
- Any requests shall be removed from the state.

As long as the actions of an order are not in state 'FINISHED' or 'FAILED' the mobile robot shall not report operating mode 'MANUAL', 'SERVICE' or 'TEACH_IN'. `nodesStates` and `edgeStates` shall not be emptied before the operating mode 'MANUAL', 'SERVICE' or 'TEACH_IN' is reported.

An order cancellation can only be triggered by fleet control.

### 6.6.8 Idle state of the mobile robot

A mobile robot is idle if its `nodeStates` and `edgeStates` are empty and all actions in the `actionStates` are either 'FINISHED' or 'FAILED'. A new order shall only be accepted if the mobile robot is idle. An order update can be accepted when the mobile robot is idle or during order execution. When idle, a mobile robot can execute instantActions.

### 6.6.9 Action states

When a mobile robot receives an `action` as part of the order (attached to a `node` or `edge` of an order), it shall report this `action` with an `actionState` in its `actionStates` array.
When a mobile robot receives an `instantAction`, it shall report this `action` with an `actionState` in its `instantActionStates` array.
When a mobile robot executes a `zoneAction`, it shall report this `action` with an `actionState` in its `zoneActionStates` array. Optionally, a mobile robot can report any planned `zoneAction` here.

The current stage of an action shall be reflected in the field `actionStatus` of the corresponding `actionState` (see Table 2).

actionStatus | Description
---|---
'WAITING' | Action was received by the mobile robot but the corresponding node was not yet traversed or the corresponding edge was not yet entered.
'INITIALIZING' | Action was triggered, preparatory measures are initiated.
'RUNNING' | The action is running.
'PAUSED' | The action is paused because of a pause instantAction or external trigger (pause button on the mobile robot)
'RETRIABLE' | Actions that failed, but can be retried, specified by the retriable parameter in the action of an order. Transition from this state is triggered by a retry or skipRetry instantAction or an external trigger.
'FINISHED' | The action is finished. <br>A result is reported via the `actionResult`.
'FAILED' | Action could not be finished for whatever reason.

>Table 12 - Feasible values for the `actionStatus` field

All possible action state transitions are visualized in Figure 21 and examples are given in the following matrix:
…(발췌: 전체 207,642자 중 앞 119,109자)
````
