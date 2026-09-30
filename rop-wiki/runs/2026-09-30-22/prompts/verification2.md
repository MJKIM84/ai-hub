(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-22
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
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

## 입력

### runs/2026-09-30-22/target.json

```json
{
  "run_id": "2026-09-30-22",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 131,
  "run_type": "area_deep_dive",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=58"
}
```

### runs/2026-09-30-22/research.json

```json
{
  "run_id": "2026-09-30-22",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 58,
    "area_name": "58. 다사업자 책임·계약·데이터",
    "category": "P. 거버넌스·법규·사회"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 데이터 보유자, 실질적 변경, 모델 계약 조항, API 폐기 정책, 서비스 수준 협약 구성 요소 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·가정(공동주택)·건물 승강기 연동의 다사업자 책임 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 변경 승인·책임 분담, 데이터 접근·공유 계약, API 버전·폐기 정책, 서비스 수준·감사 이력 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — EU 데이터법·모델 계약 조항, 산업디지털전환법·산업데이터 계약 가이드라인, VDA 5050 버전 규칙, ISO/IEC 19086-1, IEC 62443-2-4, 21 CFR Part 11 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-145, oq-149, oq-185, oq-241, oq-249, oq-259 반영 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까? [분류원문]",
    "법·표준은 로봇·AI 시스템을 바꾼 주체의 책임을 어떻게 정하는가(기계류의 실질적 변경, AI 가치사슬 책임, 산업제어 서비스 제공자의 보안 요구)? (섹션 4·6·7 겨냥, oq-249 관련)",
    "여러 사업자가 함께 만드는 운영 데이터의 소유·접근·공유 권리를 정하는 법과 계약 도구(EU 데이터법과 모델 계약 조항, 국내 산업디지털전환법과 산업데이터 계약 가이드라인)는 무엇인가? (섹션 4·6·7 겨냥, 한국 자료 우선)",
    "제조사·플랫폼 API 가 바뀔 때 호환성과 공지를 정하는 규칙(VDA 5050 버전 규칙, 오픈소스의 API 폐기 정책)은 어떻게 되어 있는가? (섹션 6·7 겨냥)",
    "서비스 수준 약속과 감사 이력은 어떤 표준·규정이 요구하고 무엇을 기록해야 하는가(ISO/IEC 19086-1, 21 CFR Part 11, EU AI법 로그 보관)? (섹션 6·7 겨냥)",
    "병원·공동주택·건물 설비 연동 등 현장 유형별로 다사업자 책임·계약을 다룬 사례와 책임 분담표 공개 사례가 있는가? (섹션 5·11 겨냥, oq-241·oq-149·oq-185 관련)",
    "다사업자 책임·계약·데이터에서 ROP가 직접 맡을 것과 계약 당사자·법무·제조사·설비업체에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥, oq-145·oq-259 관련)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "EU 데이터법(Regulation (EU) 2023/2854)은 2025-09-12부터 일반 적용되며, 연결 제품(IoT 기기) 사용자가 제품 사용으로 함께 만든 데이터에 접근·이용·이전할 수 있게 하고, 제조사·서비스 제공자 같은 데이터 보유자는 사용자와 계약을 맺어야 하며 사용자 동의 없이 비개인 데이터를 활용할 수 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1345"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "EC 해설 페이지(2025-12-15 갱신): users of IoT objects can access, use and port data that they co-generate. 데이터 보유자는 사용자 동의 없이 비개인 데이터를 이용할 수 없고 계약으로 데이터 권리를 정한다. 적용 2025-09-12, 설계 의무 2026-09-12.",
      "as_of": "2025-12-15",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f2",
      "claim": "EU 데이터법은 사용자가 데이터를 직접 또는 데이터 보유자를 통해 자신이 고른 제3자에게 공유하게 하고, 기업 간 계약에서 일방적으로 부과된 조항 가운데 '항상 불공정'과 '불공정으로 추정'되는 조항을 정해 구속력을 없애며, 데이터 처리 서비스 간 전환 요금은 2027-01-12부터 완전히 없앤다.",
      "tag": "사실",
      "source_ids": [
        "ref-1345"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "EC 해설: 제3자 공유(DMA 게이트키퍼 제외), B2B 불공정 조항은 always unfair / presumed unfair 로 나뉘어 무효, 전환 시 데이터 반출 요금 2027-01-12 완전 폐지.",
      "as_of": "2025-12-15",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f3",
      "claim": "유럽연합 집행위원회가 2025-11-19에 낸 권고 초안은 EU 데이터법 이행을 돕는 구속력 없는 모델 계약 조항(MCT) 네 벌(데이터 보유자–사용자, 사용자–데이터 수령자, 데이터 보유자–데이터 수령자(보상 포함), 자발적 공유자–수령자)과 클라우드 표준 계약 조항 여섯 개(전환·이탈, 해지, 보안·업무 연속성, 비분산, 일방 변경 금지, 책임)를 제시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1346"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "EC 라이브러리 페이지(2025-11-19, Draft, non-binding): MCT 4벌과 SCC 6개(Switching & Exit, Termination, Security & Business Continuity, Non-Dispersion, Non-Amendment, Liability). 의무적 B2B 데이터 공유의 합리적 보상 지침은 추후 예고.",
      "as_of": "2025-11-19",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "한국의 산업 디지털 전환 촉진법(2022-07 시행)은 산업데이터 생성에 투자한 자에게 그 데이터의 사용·수익권을 인정하고 관계자 간 계약 체결을 권고하며, 정부가 산업데이터 계약 지침을 마련하도록 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1347"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "지디넷코리아(2022-03-15, 산업통상자원부 발표 보도): 산업데이터 생성자에게 사용·수익권 부여, 2022년 7월 시행, 지침 방향은 공정한 거래·분쟁 최소화·공유·이전·활용 촉진.",
      "as_of": "2022-03-15",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f5",
      "claim": "산업통상부의 산업데이터 계약 가이드라인(공공데이터포털 등록 2023-04-05, PDF 432쪽)은 총론·법적기초·산업데이터 가치 산정·계약의 유형·개인보상·국외이전으로 구성되며, 산업데이터 거래 당사자를 위해 유의사항·표준계약서·업종별 사례를 안내한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1348",
        "ref-1347"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공공데이터포털 설명: 총론, 법적기초, 산업데이터 가치 산정, 계약의 유형, 개인보상, 국외이전 순서, 유의사항·표준계약서·업종별 사례 안내. 공공누리 제3유형. 가이드라인 본문(PDF)은 열지 않았다.",
      "as_of": "2023-04-05",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "VDA 5050 3.0.0 명세는 [주].[부].[수정] 의미적 버전을 써서 주 버전은 필수 필드 추가 같은 호환을 깨는 변경, 부 버전은 선택 매개변수 추가 같은 새 기능, 수정 버전은 문서 오탈자 같은 작은 정정에 쓰고, MQTT 토픽 경로에 주 버전을 넣으며(interfaceName/majorVersion/manufacturer/serialNumber/topic), 변경 제안은 공식 GitHub 저장소로 받는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "VDA5050_EN.md(main, 3.0.0): 'Major version changes (x.0.0) typically involve breaking changes, such as the introduction of new non optional fields.' 토픽 예 vda5050/v3/KIT/0001/order. 판 간 호환 처리 절차는 명세에 따로 없다.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f7",
      "claim": "Kubernetes 의 API 폐기 정책은 API 요소를 API 그룹 버전을 올려야만 제거할 수 있게 하고, 버전 간 왕복 변환에서 정보가 보존되어야 하며, 정식(GA) API 는 주 버전 안에서 제거하지 않고 베타는 폐기 공지 뒤 9개월 또는 3개 부 릴리스 동안 유지하며, 폐기된 API 호출에는 경고 헤더·감사 주석·지표를 남긴다.",
      "tag": "사실",
      "source_ids": [
        "ref-1349"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Kubernetes Deprecation Policy: Rule #1 'API elements may only be removed by incrementing the version of the API group.' 베타 9 months or 3 minor releases, v1.19부터 Warning 헤더·k8s.io/deprecated 감사 주석·apiserver_requested_deprecated_apis 지표. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "ISO/IEC 19086-1:2016(2016-09-21, 1판)은 클라우드 서비스 수준 협약(SLA)의 공통 구성 요소(개요, 클라우드 서비스 계약과 SLA 의 관계, 개념, 용어)를 정하지만 모든 서비스에 쓰는 표준 SLA 구조나 서비스 수준 목표 세트는 정하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1351"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IEC 웹스토어 소개: overview of cloud SLAs, relationship between the cloud service agreement and the cloud SLA, concepts, terms. 표준 SLA 구조·SLO 세트는 제시하지 않음(검색 요약). 표준 본문은 유료로 미열람.",
      "as_of": "2016-09-21",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f9",
      "claim": "IEC 62443-2-4:2023(2023-12-15)은 산업 자동화·제어 시스템(IACS) 서비스 제공자가 자동화 솔루션의 통합·유지보수 중에 자산 소유자에게 제공할 보안 관련 프로세스 요구사항을 정하며, 자산 소유자·서비스 제공자·제품 공급자를 구분하고 업종별로 요구를 골라 쓰는 프로파일을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1352"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "BSI Knowledge 메타데이터(2023-12-15 발행)와 검색 요약: requirements for security-related processes that IACS service providers can offer to the asset owner during integration and maintenance. 본문 미열람.",
      "as_of": "2023-12-15",
      "site_type": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "EU 기계류 규정(Regulation (EU) 2023/1230, 2023-06-14 채택, 2027-01-20 적용)은 기계에 실질적 변경을 한 자연인·법인을 제조자로 보아 제조자 의무를 지게 하며, 실질적 변경은 새로운 위험을 만들거나 기존 위험을 키워 새로운 중요한 보호 조치가 필요한 변경이고 적합성에 영향을 주지 않는 수리·정비는 이에 해당하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-555",
        "ref-1359"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "EU-OSHA: 채택 2023-06-14, applies from 20 January 2027, 자율 이동 기계(로봇)·AI 안전 기능을 다룸. 실질적 변경 정의와 제18조 내용은 EUR-Lex 원문을 열지 못해 검색 요약 범위만 사용.",
      "as_of": "2023-06-14",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f11",
      "claim": "EU AI법 제25조는 유통자·수입자·배포자(deployer)·제3자가 고위험 AI 시스템에 자기 이름을 붙이거나 실질적 변경을 하거나 용도를 바꾸면 제공자로 보고, 최초 제공자에게 기술 문서·정보·기술적 접근을 주는 협력 의무를 지우며, 제공자와 부품·도구·서비스 공급자는 필요한 정보·기능·기술적 접근·지원을 서면 계약으로 정하게 한다(오픈소스 제외).",
      "tag": "사실",
      "source_ids": [
        "ref-1356"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Article 25 요약: 세 경우 제공자 지위 이전, 최초 제공자 협력 의무, 제4항 written agreement 로 necessary information, capabilities, technical access and other assistance 명시, AI Office 가 자발적 모델 계약 조건을 만들 수 있음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f12",
      "claim": "EU AI법 제26조는 고위험 AI 시스템 배포자가 자기 통제 아래 있는 자동 생성 로그를 최소 6개월 보관하고, 제공자 지침에 따라 운영을 감시하다가 위험이 의심되면 제공자 등에 알리고 사용을 멈추며 중대한 사고는 즉시 제공자에게 먼저 알리게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1357"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Article 26(6): 'keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control' 최소 6개월. 26(5): 감시·통지·사용 중단·중대 사고 보고. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "미국 21 CFR 11.10(e)는 폐쇄형 전자기록 시스템에 전자기록을 만들거나 고치거나 지우는 운영자 입력과 행위의 날짜·시각을 독립적으로 기록하는 보안이 적용된 컴퓨터 생성 타임스탬프 감사 추적을 쓰도록 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1353"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§11.10(e): secure, computer-generated, time-stamped audit trails to independently record the date and time of operator entries and actions that create, modify, or delete electronic records. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f14",
      "claim": "Shaik(SSRN, 2026-05)은 자율 산업 시스템의 책임을 로봇 제조사(OEM)·시스템 통합자·AI 공급자·운영자 사이에 통제력(피해를 막을 수 있었는가)·예견 가능성·정보 비대칭의 세 원칙으로 배분하는 위험 비례 책임 프레임워크(RPLF)를 제안하고, 이를 상업 계약과 기존 보험으로 구현할 수 있다고 주장한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1355"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "SSRN 초록(검색 요약): OEMs, system integrators, AI vendors, operators 사이 책임 배분, RPLF 의 control·foreseeability·information asymmetry, implementable through commercial contracts. 동료심사 전 원고, 원문 미열람.",
      "as_of": "2026-05-01",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f15",
      "claim": "병원 사례(싱가포르): 창이종합병원 CHART 는 의료 로봇 미들웨어 RoMi-H 통합을 맡을 시스템 통합자를 연 2회 등재 프로그램으로 평가·인증하고, 공공 의료기관은 로봇·소프트웨어·IoT 연동에 등재된 통합자를 쓰게 되어 있어 다사업자 연동의 책임 주체를 사전 자격으로 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-872"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "RoMi-H Empanelment Programme 2025: 통합자 연 2회 평가·등재, 공공 의료기관은 등재 통합자 사용. (재인용: 2026-09-30-19)",
      "as_of": "2025-05",
      "site_type": "병원",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f16",
      "claim": "한국승강기협회는 현대엘리베이터·오티스·TK엘리베이터·미쓰비시엘리베이터 등 승강기 제조사가 참여한 과학기술정보통신부 과제 '실내외 자율주행 로봇 상호연동 표준개발'로 배달 로봇과 승강기가 API 로 실시간 정보를 주고받는 연동 표준을 만들고 있으며, 2024-12-31까지 국내·국제 표준 개발, 전문가 협의체 구성, 테스트베드·개념증명을 목표로 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-317"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "전기신문(2023-05-17): 승강기 대기업·중소 제조사 참여, API 기반 실시간 통신, 연구 목표 2024-12-31까지 표준·협의체·테스트베드. 장애 시 책임 분담 내용은 기사에 없음.",
      "as_of": "2023-05-17",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f17",
      "claim": "가정 사례(한국 공동주택): 한국아파트신문 사설(2026-09-14)은 시흥 힐스테이트더웨이브시티의 주차로봇 2세트 실증, 서울 송파구 아파트의 자율주행 순찰로봇 2대, 강남 타워팰리스의 사족보행로봇 기술검증, 부산 강서구 아파트의 운반로봇 서비스를 들고, 발의된 이동로봇 특별법안이 개인정보 처리·책임 분담·책임보험 가입 같은 안전관리 체계를 담는다고 전했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1358"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "한국아파트신문 사설(2026-09-14): 공동주택 로봇 사례 4건과 한병도 의원 발의 이동로봇 특별법안(개인정보 처리, 책임 분담, 책임보험 가입). 법안 원문 미확인.",
      "as_of": "2026-09-14",
      "site_type": "가정",
      "flow_item": "수행 자원"
    },
    {
      "id": "f18",
      "claim": "같은 사설은 공동주택에 로봇·AI·통신망·관제시스템이 더해지면 관리사무소장 등 관리주체의 관리 영역과 책임이 오히려 넓어질 수 있으므로 도입 전에 책임 범위를 명확히 하고 법제도를 정비해야 한다고 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-1358"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "'기존 시설에 로봇과 AI, 통신망과 관제시스템까지 더해지면서 관리영역과 책임이 넓어질 수 있다' — 책임 범위 명확화와 법제도 정비 선행 주장.",
      "as_of": "2026-09-14",
      "site_type": "가정",
      "flow_item": "제약"
    },
    {
      "id": "f19",
      "claim": "확인한 자료를 종합하면 핵심 질문(제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까)에 대해 이를 한 번에 정한 공개 표준이나 책임 분담표는 찾지 못했고, 실제 규칙은 (a) 변경을 한 주체가 제조자·제공자 의무를 지는 법 규정(기계류 규정의 실질적 변경, AI법 가치사슬 책임), (b) 인터페이스 표준의 버전·폐기 규칙, (c) 서비스 수준 협약·표준 계약 조항과 통합자 사전 자격 같은 계약·조달 장치의 조합으로 정해지는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-555",
        "ref-1356",
        "ref-031",
        "ref-1349",
        "ref-1351",
        "ref-1346",
        "ref-1352",
        "ref-872"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f6·f7(버전·폐기 규칙), f8·f3(SLA·표준 계약 조항), f9·f15(서비스 제공자 요구·통합자 등재), f10·f11(변경 주체 책임)을 종합한 추정. oq-241 의 책임 분담표 공개 사례는 이번에도 찾지 못함.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 58. 다사업자 책임·계약·데이터에서 ROP가 직접 맡을 범위는 제조사·설비 어댑터별 인터페이스 버전과 폐기 일정 관리, 연동·설정 변경의 요청·승인·적용 기록, 누가 언제 어떤 명령·변경을 했는지 남기는 타임스탬프 감사 이력과 보관, 데이터 항목별 소유·접근·반출 조건 표시, 계약한 서비스 수준 지표의 측정·보고로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-1349",
        "ref-1353",
        "ref-1357",
        "ref-1345",
        "ref-1346",
        "ref-1351"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f6·f7(버전·폐기 관리), f13·f12(감사 추적·로그 보관), f1·f2·f3(데이터 접근·반출 조건), f8(SLA 구성 요소)에서 도출한 직접 범위 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f21",
      "claim": "연계 대상: 분류 원문 19장 기준으로 계약 체결과 법적 책임 판정·보험·규제 적합성 평가는 계약 당사자와 법무(59. 법·규제·보험·라이선스)에, 로봇 펌웨어와 제조사 API 의 수명주기는 로봇 제조사에, 승강기·출입문 쪽 연동 인터페이스와 설비 안전은 설비 제조사·관리주체에 속하므로, ROP는 그들이 정한 조건을 운영 제약으로 받고 판단 근거가 되는 기록과 데이터를 제공하는 쪽을 맡는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-555",
        "ref-1356",
        "ref-317",
        "ref-1358",
        "ref-1355"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f10·f11(규제상 책임 주체), f14(계약·보험으로 책임 배분), f16(승강기 제조사 주도 연동 표준), f17·f18(공동주택 관리주체 책임)을 원문 19장 경계에 대입한 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f22",
      "claim": "이 영역은 인터페이스 버전 규칙의 21. 상호운용 표준·적합성과 20. 로봇·제조사 관제 연동(f6·f7), 승강기 연동 책임의 22. 설비·건물 시스템 연동(f16), 감사 이력·로그의 37. 관제 화면·실행 기록과 52. 통신 보호·위협 관리·감사(f12·f13·f9), 데이터 권리와 개인정보의 53. 개인정보·영상 데이터(f1·f17, oq-259), API 폐기와 변경 관리의 57. 자산·소프트웨어 수명주기 관리(f7), 규제 책임의 59. 법·규제·보험·라이선스(f10·f11·f14), 통합자 자격·계약의 3. 경제성·조달·사업 모델(f15), 책임 범위 합의의 2. 사용 사례·요구·책임 범위(oq-241), AI 가치사슬 책임의 47. AI·학습·적응과 모델 운영과 13. 대화형 기능의 신뢰·기반(f11, oq-145), 적용 현장인 63. 병원·의료(f15)·65. 가정·공동주택(f17·f18)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-1349",
        "ref-317",
        "ref-1357",
        "ref-1353",
        "ref-1352",
        "ref-1345",
        "ref-1358",
        "ref-555",
        "ref-1356",
        "ref-1355",
        "ref-872"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 연결은 괄호 안 finding 에 근거한 추정이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 없다.",
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
      "summary": "VDA 5050 공식 명세(main, 3.0.0). 이번 실행에서 의미적 버전 규칙, 토픽의 주 버전 표기, GitHub 변경 제안 절차를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-872",
      "org": "Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "RoMi-H Empanelment Programme 2025",
      "published": "2025-05",
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "RoMi-H 통합 시스템 통합자를 연 2회 평가·등재하는 프로그램 안내. 이번 실행에서 다시 열지 않고 2026-09-30-19 브리프 내용을 재인용했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1345",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "Data Act explained",
      "published": "2025-12-15",
      "url": "https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "EU 데이터법의 연결 제품 데이터 접근권, 데이터 보유자 계약 의무, 제3자 공유, B2B 불공정 조항, 모델 계약 조항, 클라우드 전환, 적용 일정을 설명하는 집행위원회 해설(2025-12-15 갱신).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1346",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts",
      "published": "2025-11-19",
      "url": "https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "EU 데이터법용 구속력 없는 모델 계약 조항 4벌과 클라우드 표준 계약 조항 6개의 권고 초안 게시 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1347",
      "org": "지디넷코리아",
      "title": "산업데이터 만든 자에게 사용·수익권 부여",
      "published": "2022-03-15",
      "url": "https://zdnet.co.kr/view/?no=20220315103750",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "산업통상자원부 발표를 전한 기사. 산업디지털전환촉진법의 산업데이터 사용·수익권, 2022년 7월 시행, 산업데이터 계약 가이드라인 제정 방향을 다룬다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1348",
      "org": "산업통상부 (공공데이터포털)",
      "title": "산업통상부_산업데이터 계약 가이드라인_20230109",
      "published": "2023-04-05",
      "url": "https://www.data.go.kr/data/15113186/fileData.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "산업데이터 계약 가이드라인 파일데이터 소개(포털 등록일 2023-04-05, 수정 2025-12-09, PDF 432쪽). 목차와 안내 내용(유의사항·표준계약서·업종별 사례)을 확인했고 PDF 본문은 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1349",
      "org": "The Kubernetes Authors",
      "title": "Kubernetes Deprecation Policy",
      "published": null,
      "url": "https://kubernetes.io/docs/reference/using-api/deprecation-policy/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Kubernetes 프로젝트의 API 폐기 규칙(버전 증가로만 제거, 왕복 호환, 안정도별 유지 기간, 폐기 API 사용 경고·감사 주석·지표).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-555",
      "org": "European Parliament and Council of the European Union (EUR-Lex)",
      "title": "Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery",
      "published": "2023-06-14",
      "url": "https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. EU 기계류 규정 원문. EUR-Lex 페이지 본문을 읽지 못해 실질적 변경 정의·제18조는 검색 요약 범위만 사용했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1351",
      "org": "IEC / ISO (ISO/IEC JTC 1)",
      "title": "ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts",
      "published": "2016-09-21",
      "url": "https://webstore.iec.ch/en/publication/25920",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 유료 표준이라 IEC 웹스토어 소개 페이지만 열어 범위(클라우드 SLA 구성 요소·개념·용어)와 발행일을 확인했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1352",
      "org": "IEC (BSI Knowledge 게재)",
      "title": "IEC 62443-2-4:2023 Security for industrial automation and control systems - Security program requirements for IACS service providers",
      "published": "2023-12-15",
      "url": "https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 유료 표준. BSI 페이지에서 제목·발행일만 확인했고 범위(통합·유지보수 서비스 제공자의 보안 프로그램 요구)는 검색 요약 범위다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1353",
      "org": "U.S. Food and Drug Administration 규정 (Cornell Law School LII 게재)",
      "title": "21 CFR § 11.10 - Controls for closed systems",
      "published": null,
      "url": "https://www.law.cornell.edu/cfr/text/21/11.10",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "미국 연방규정 21 CFR Part 11 의 폐쇄형 시스템 통제 조항. (e)항 감사 추적 요구를 확인했다. eCFR 공식 페이지는 차단되어 LII 게재본을 열었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-317",
      "org": "전기신문 (안상민)",
      "title": "승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인",
      "published": "2023-05-17",
      "url": "https://www.electimes.com/news/articleView.html?idxno=320147",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한국승강기협회가 승강기 제조사들과 수행하는 로봇-승강기 API 연동 표준개발 과제와 목표를 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1355",
      "org": "Shaik, A. S. (SSRN)",
      "title": "Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong?",
      "published": "2026-05-01",
      "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6737139",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. SSRN 게재 원고(동료심사 전). 제조사·통합자·AI 공급자·운영자 사이 책임 배분 프레임워크(RPLF)를 제안한다. SSRN 403 으로 검색 요약과 초록 소개만 확인했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1356",
      "org": "Future of Life Institute (artificialintelligenceact.eu)",
      "title": "Article 25: Responsibilities Along the AI Value Chain | EU Artificial Intelligence Act",
      "published": null,
      "url": "https://artificialintelligenceact.eu/article/25/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "EU AI법 제25조 게재본. 제공자 지위 이전 조건, 최초 제공자 협력 의무, 공급자와의 서면 계약 요구를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1357",
      "org": "Future of Life Institute (artificialintelligenceact.eu)",
      "title": "Article 26: Obligations of Deployers of High-Risk AI Systems | EU Artificial Intelligence Act",
      "published": null,
      "url": "https://artificialintelligenceact.eu/article/26/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "EU AI법 제26조 게재본. 배포자의 로그 최소 6개월 보관, 운영 감시·통지·사용 중단·중대 사고 보고 의무를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1358",
      "org": "한국아파트신문 (사설)",
      "title": "공동주택에 밀려오는 로봇, 또 다른 관리책임은 (제목 일부만 확인)",
      "published": "2026-09-14",
      "url": "https://www.hapt.co.kr/news/articleView.html?idxno=169488",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "공동주택 로봇 도입 사례와 관리주체 책임 확대 우려, 이동로봇 특별법안의 책임 분담·책임보험 내용을 다룬 사설.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1359",
      "org": "European Agency for Safety and Health at Work (EU-OSHA)",
      "title": "Regulation 2023/1230/EU - machinery",
      "published": null,
      "url": "https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "EU 기계류 규정 소개. 채택일(2023-06-14), 적용일(2027-01-20), 자율 이동 기계·AI 안전 기능 포괄, 제조자 의무를 요약한다.",
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
      "rationale": "섹션 3: f19(핵심 질문 답, 추정), f18(공동주택 책임 확대 우려, 의견), f14(책임 공백 논의, 의견) / 섹션 4: 데이터 보유자·연결 제품 데이터 f1, 모델 계약 조항 f3, 산업데이터 사용·수익권 f4, 실질적 변경 f10·f11, 의미적 버전·API 폐기 정책 f6·f7, SLA 구성 요소 f8, 감사 추적 f13 / 섹션 5: 병원 — f15(수행 자원, 싱가포르), 가정 — f17(수행 자원, 한국 공동주택)·f18(제약), 현장 유형 미명시 건물 승강기 연동 — f16(22. 설비·건물 시스템 연동 연계로 서술). 물류창고·제조 공장·상업 시설·실외 사례는 찾지 못했음을 명시 / 섹션 6: 변경 승인·책임 분담 f10·f11·f9·f15, 데이터 접근·공유 계약 f1·f2·f3·f4·f5, API 버전·폐기 정책 f6·f7, 서비스 수준·감사 이력 f8·f12·f13 / 섹션 7: EU 데이터법·모델 계약 조항 f1~f3, 산업디지털전환법·산업데이터 계약 가이드라인 f4·f5, VDA 5050 버전 규칙 f6, Kubernetes 폐기 정책 f7, ISO/IEC 19086-1 f8(원문 미열람), IEC 62443-2-4 f9(원문 미열람), EU 기계류 규정 f10, EU AI법 제25·26조 f11·f12, 21 CFR Part 11 f13 / 섹션 8: f3·f5·f14 / 섹션 9: f20(직접 범위), f21(연계 대상) / 섹션 10: f22 — 2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65 / 섹션 11: 기존 oq-145·oq-149·oq-185·oq-241·oq-249·oq-259(모두 미해결 유지; oq-241·oq-249 는 f10·f11·f12·f19 로 부분 근거)와 open_questions_new 5건. 다음 실행 후보: 22. 설비·건물 시스템 연동 페이지에 f16, 65. 가정·공동주택 페이지에 f17·f18, 57. 자산·소프트웨어 수명주기 관리 페이지에 f7 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "데이터 보유자",
      "term_en": "Data Holder (EU Data Act)",
      "definition": "EU 데이터법에서 연결 제품이나 관련 서비스가 만든 데이터를 이용·제공할 권리나 의무를 가진 자로, 사용자 요청 시 데이터를 사용자나 제3자에게 제공해야 하고 사용자와의 계약 없이 비개인 데이터를 활용할 수 없다."
    },
    {
      "term_ko": "실질적 변경",
      "term_en": "Substantial Modification",
      "definition": "출시된 기계나 AI 시스템을 바꿔 새로운 위험을 만들거나 위험을 키우거나 적합성·용도에 영향을 주는 변경으로, 이를 한 자가 제조자·제공자의 의무를 지게 되는 기준이다."
    },
    {
      "term_ko": "모델 계약 조항",
      "term_en": "Model Contractual Terms (MCTs)",
      "definition": "EU 집행위원회가 데이터법 이행을 위해 데이터 보유자·사용자·데이터 수령자 사이의 데이터 접근·이용 계약에 쓰도록 권고하는 구속력 없는 표준 계약 문안이다."
    },
    {
      "term_ko": "API 폐기 정책",
      "term_en": "API Deprecation Policy",
      "definition": "API 요소를 언제 어떤 공지와 유예 기간을 거쳐 폐기·제거할지, 버전을 어떻게 올릴지를 미리 정해 이용자가 호환성을 예측하게 하는 규칙이다."
    }
  ],
  "open_questions_new": [
    "여러 제조사 로봇의 운영 데이터를 모으는 오케스트레이션 플랫폼 사업자는 EU 데이터법상 데이터 보유자인가, 사용자가 지정한 제3자 데이터 수령자인가, 그리고 그에 따라 제조사에게 데이터 제공을 요구할 수 있는 범위는 어디까지인가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 59. 법·규제·보험·라이선스 | 근거: f1 | 종류: 일반",
    "로봇 제조사·관제 API 의 주 버전 변경이나 폐기를 오케스트레이션 플랫폼에 사전 통지하는 기간과 유예 기간을 계약이나 인터페이스 표준에 명시한 공개 사례가 있는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 20. 로봇·제조사 관제 연동, 57. 자산·소프트웨어 수명주기 관리 | 근거: f7 | 종류: 일반",
    "국내 산업데이터 계약 가이드라인의 표준계약서와 업종별 사례가 로봇 운영 데이터(지도·작업 이력·센서 로그)처럼 여러 사업자가 함께 만드는 데이터를 어떻게 다루는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 15. 지도·공간·위치 모델 | 근거: f5 | 종류: 일반",
    "오케스트레이션 플랫폼에서 경로망·속도 제한·작업 규칙 같은 설정을 바꾸는 일이 EU 기계류 규정의 실질적 변경에 해당해 플랫폼 운영자나 통합자가 제조자 의무를 지는 경우가 있는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 59. 법·규제·보험·라이선스, 48. 안전·위험 관리 | 근거: f10 | 종류: 일반",
    "로봇-승강기 연동 표준 과제의 결과물(표준 번호, 연동 장애 시 승강기 제조사·로봇 제조사·관제 사업자의 책임 분담)이 공개되었는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 22. 설비·건물 시스템 연동 | 근거: f16 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 17,
    "cross_checked_count": 0,
    "unverified": [
      "f4 산업디지털전환법 제9조의 공동 생성 데이터·제3자 제공 시 권리(당사자 약정 우선) 조문은 검색 요약에만 있어 finding 으로 내지 않음 — 국가법령정보센터 조문 열람 실패",
      "f5 산업데이터 계약 가이드라인 PDF(432쪽) 본문 미열람 — 계약 유형 구분과 표준계약서 조항 미확인",
      "f8 ISO/IEC 19086-1 본문 미열람(유료), 표준 SLA 구조를 정하지 않는다는 부분은 검색 요약",
      "f9 IEC 62443-2-4 범위·역할 구분은 검색 요약 기준, 본문 미열람",
      "f10 EU 기계류 규정 실질적 변경 정의·제18조는 EUR-Lex 본문을 열지 못해 검색 요약 기준",
      "f14 Shaik 원고가 든 2024년 독일 자동차 공장 사고(6개 당사자 책임 부인) 사례는 저자 주장으로 독립 확인 실패 — finding 에서 제외",
      "f16 로봇-승강기 연동 표준 과제의 결과물(표준 번호·책임 분담) 미확인",
      "f17 이동로봇 특별법안 원문·발의일 미확인",
      "oq-241 로봇 오케스트레이션 도입 계약의 책임 분담표·표준 계약 조항 공개 사례를 이번에도 찾지 못함",
      "ISO/IEC 20000-1:2018 변경 관리 조항은 공개 원문을 읽지 못해 넣지 않음",
      "국내 공공 정보시스템 SLA 가이드는 공식 출처를 찾지 못해 넣지 않음",
      "물류창고·제조 공장·상업 시설·실외 현장의 다사업자 책임·계약 사례를 찾지 못함"
    ],
    "scope_violations": [
      "f10·f11·f12·f14: 규제상 책임·로그 의무와 책임 배분 이론은 59. 법·규제·보험·라이선스와 겹치므로 이 영역에서는 변경 승인·책임 분담 근거로만 쓰고 법적 판정은 f21 에서 연계 대상으로 둠",
      "f16: 승강기 쪽 연동 인터페이스와 설비 안전 제어는 원문 19장 '시설·설비 제어' 연계 영역이므로 ROP 직접 범위로 서술하지 않음(f21 연계 대상)",
      "f13: 21 CFR Part 11 은 FDA 규제 대상 전자기록에 적용되는 규정이라 감사 추적 요구의 참고 사례로만 쓰고 병원 현장 의무로 단정하지 않음(site_type null)"
    ],
    "budget_used": {
      "queries": 15,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-1345~ref-1359, 예약 구간 안)로 신규 출처 상한에 도달했다. 재사용 2건: ref-031(이전 브리프 2026-09-30-19 출처 표 값 사용, 이번에 GitHub 공식 저장소 원문을 다시 열어 버전 규칙 확인), ref-872(다시 열지 않고 재인용). 참고문헌 목록 요약에 행이 없어 같은 URL 이 이미 있으면 퍼블리셔 병합 필요. 원문 열람: 17건 중 12건(webfetch 11, github_raw 1)을 열었고 ref-872·ref-555(EUR-Lex 본문 비어 있음)·ref-1351·ref-1352(유료 표준, 소개 페이지만)·ref-1355(SSRN 403)는 fetched false 다. 교차 확인 0건. 벤더 주장 없음. 분류 원문 핵심 질문에는 f19 로 답했고 결론은 '연동 오류 수정·변경 승인 주체를 한 번에 정한 공개 표준·책임 분담표는 찾지 못했고, 변경 주체 책임 법규·인터페이스 버전 규칙·SLA와 표준 계약 조항·통합자 자격의 조합으로 정해지는 것으로 보인다'는 추정이다. 현장 유형 사례는 병원(f15 싱가포르, 재인용)·가정(f17·f18 한국 공동주택)이고 승강기 연동(f16)은 현장 유형을 밝히지 않아 null 로 두었다. 물류창고·제조 공장·상업 시설·실외는 찾지 못했다. 국내 자료는 지디넷코리아(ref-1347)·공공데이터포털(ref-1348)·전기신문(ref-317)·한국아파트신문(ref-1358)이다. 기존 열린 질문 oq-145·oq-149·oq-185·oq-241·oq-249·oq-259 는 해결하지 못했다(oq-249 는 f10·f12 가 개별 기계·AI 시스템 쪽 의무만 보여 플랫폼 적용 여부는 미해결, oq-241 은 f19 로 부분 근거). L. AI·학습 기술 관련은 f11(AI 가치사슬 책임)을 47. AI·학습·적응과 모델 운영과 연결 제안했다(f22). 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. 용어집에 이미 있는 감사 추적·서비스 수준 협약·의미적 버전 관리·산업데이터·서비스형 로봇·등재 프로그램·보안 수준(IEC 62443)은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-22/verification.json

```json
{
  "run_id": "2026-09-30-22",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1345 열람 확인(EC, Data Act explained, 최종 갱신 2025-12-15). 연결 제품 데이터 접근·이용·이전, 데이터 보유자–사용자 계약, 사용자 동의 없는 비개인 데이터 이용 금지, 2025-09-12 적용 모두 원문에 있다. 근거 발췌의 '설계 의무 2026-09-12'는 이 페이지에 없어 본문에 쓰지 않도록 지시했다. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1345 열람 확인. 제3자 공유(DMA 게이트키퍼 제외), 'always unfair'·'presumed unfair' 불공정 조항 목록, 2027-01-12 전환 요금 완전 폐지가 원문과 일치한다. 단일 출처."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1346 열람 확인(EC, 2025-11-19, 권고 초안). 모델 계약 조항 4벌과 클라우드 표준 계약 조항 6개(Switching & Exit, Termination, Security & Business continuity, Non-Dispersion, Non-Amendment, Liability)의 이름·구성이 일치하고, 합리적 보상 지침은 추후 발표 예정으로 되어 있다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1347 열람 확인(지디넷코리아, 2022-03-15). 산업데이터 생성 투자자의 사용·수익권, 7월 시행, 계약 체결 권고와 정부 지침 마련, 지침 방향이 기사에 있다. 법 조문을 직접 확인한 것이 아니라 산업통상자원부 발표를 전한 기사 1건에 기대므로 신뢰도는 low 그대로 둔다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1348 열람 확인(공공데이터포털, 등록 2023-04-05, 수정 2025-12-09, 432쪽). 목차 구성과 '유의사항, 표준계약서, 업종별 사례' 안내가 일치한다. ref-1347은 가이드라인 목차를 뒷받침하지 않으므로 f5 근거에서 빼게 했다. 가이드라인 본문 PDF는 열지 않았다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-031 원문(data/source_texts/ref-031.txt, VDA 5050 3.0.0)으로 확인했다. 1장의 의미적 버전 문장(주 버전은 'typically' 호환을 깨는 변경), 4.2절 토픽 구조 interfaceName/majorVersion/manufacturer/serialNumber/topic과 예 vda5050/v3/KIT/0001/order, GitHub 저장소를 통한 변경 제안이 모두 원문에 있다. 기준일은 확인일 2026-09-30이다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1349 열람 확인. Rule #1(API 그룹 버전을 올려야만 제거), Rule #2(왕복 변환 시 정보 무손실), GA는 주 버전 안에서 제거 불가, 베타는 폐기 뒤 9개월 또는 3개 부 릴리스(둘 중 긴 쪽) 뒤 제거, v1.19부터 Warning 헤더·k8s.io/deprecated 감사 주석·apiserver_requested_deprecated_apis 지표가 원문과 일치한다. 발행일이 없어 확인일 기준이다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증에서 IEC 웹스토어 소개 페이지를 열어 확인했다(2016-09-21, 1판). 초록에 '표준 SLA 구조나 표준 SLO 세트를 제시하지 않는다'는 문장이 있다. 표준 본문은 유료라 원문 미열람이다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "BSI 페이지를 열어 제목과 발행일(2023-12-15)을 확인했다. 통합·유지보수 중 IACS 서비스 제공자가 자산 소유자에게 제공하는 보안 프로세스 요구, 자산 소유자·서비스 제공자·제품 공급자 역할 구분, 4.1.4 프로파일은 IEC 웹스토어·IECEE 검색 요약 범위에서 확인된다. 표준 본문은 원문 미열람이다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1359(EU-OSHA)를 열어 채택일 2023-06-14, 적용일 2027-01-20, 자율 이동 기계·AI 안전 기능 포괄, 'substantial modification' 명확화 언급을 확인했다. 실질적 변경을 한 자를 제조자로 보는 제18조와 정의(새 위험 발생·기존 위험 증가로 새로운 중요한 보호 조치가 필요한 변경, 적합성에 영향이 없는 수리·정비 제외)는 EUR-Lex 본문이 비어 열리지 않아 EUR-Lex 검색 요약에서만 확인했다(ref-555 원문 미열람). 핵심 규칙은 ref-555 하나에 기대므로 교차 확인은 안 된 것으로 본다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1356 열람 확인(FLI의 EU AI법 조문 게재본으로, 공식 관보본이 아니다). 제공자 지위 이전의 세 경우, 최초 제공자 협력 의무, 서면 계약에 'necessary information, capabilities, technical access and other assistance' 명시, 오픈소스 예외, AI Office 자발적 모델 계약 조건이 원문과 일치한다. 셋째 경우는 '고위험이 아닌 AI 시스템(범용 AI 포함)의 용도를 바꿔 고위험이 되게 하는 것'이므로 그렇게 좁혀 쓰도록 지시했다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1357 열람 확인(FLI 게재본). 제26조 제5항의 운영 감시·위험 의심 시 통지·사용 중단, 중대 사고 시 '먼저 제공자에게' 즉시 통지, 제6항의 자기 통제 아래 있는 자동 생성 로그를 최소 6개월 보관(다른 법이 있으면 예외)이 원문과 일치한다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1353 열람 확인(Cornell LII 게재본). 21 CFR 11.10(e) 문구가 주장과 일치한다. FDA 규제 대상 전자기록에 적용되는 규정이므로 감사 추적 요구의 참고 사례로만 쓰게 했다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "SSRN은 검증에서도 403이다. 검색 결과(SSRN 목록, 2026-05-22 게재·2026-05-01 작성, 14쪽)와 private-law-theory.org 소개 글에서 OEM·통합자·AI 공급자·운영자 사이 책임 배분과 RPLF 세 원칙(통제·예견 가능성·정보 비대칭)을 확인했다. 소개 글은 같은 원고를 요약한 것이라 독립 출처가 아니다. 동료심사 전 원고의 저자 의견이므로 [의견]을 유지하고 저자를 밝히게 했다. 원문 미열람."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증에서 ref-1289를 열어 확인했다(2025-05-01, 갱신 2026-08-24). 'bi-annual' 통합자 평가·재평가 등재 프로그램이 있고, 공공 의료의 로봇·소프트웨어·IoT 통합은 RoMi-H를 거쳐 등재·인증된 통합자가 맡는다고 적혀 있다. 브리프의 원문 미열람 표시는 그대로 둔다. 2026-09-30-19·2026-09-30-21 브리프와 같은 출처이므로 ref-1289를 재사용한다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. ref-1354를 열어 보니 기관명이 '한국승강기협회'가 아니라 '대한승강기협회'다. 기사가 말하는 것은 협회·ETRI·뉴빌리티가 과기정통부 선정 과제 '실내외 자율주행 로봇 상호연동 표준개발'을 위해 연 승강기기업 간담회(2023-05-16)에 현대엘리베이터·오티스·TK엘리베이터·미쓰비시엘리베이터와 한국승강기공업협동조합 등이 참석했다는 것이다. '제조사가 참여한 과제로 표준을 만들고 있다'는 과장이다. API 실시간 연동과 2024-12-31 목표는 기사에 있다. 책임 분담 내용은 기사에 없다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1358 열람 확인(한국아파트신문 사설, 입력 2026-09-14). 사례 4건(시흥 현대위아 주차로봇 2세트, 송파 순찰로봇 2대, 타워팰리스 사족보행 경비로봇 기술검증, 부산 강서구 물품 운반 로봇)과 한병도 의원이 대표 발의한 이동로봇 특별법안(개인정보 처리·책임 분담·책임보험)이 사설에 있다. 제목 전체는 '공동주택에 밀려오는 로봇, 또 다른 관리책임은 없을까'다. 법안 원문은 미확인이다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1358에서 관리영역과 책임이 넓어질 수 있다는 문장을 확인했다. 한국아파트신문 사설의 의견임을 밝히게 했다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f6·f7·f8·f3·f9·f15·f10·f11을 종합한 추정이다. 근거 finding이 모두 확인됐다. 참고로 ref-031 원문 2장은 VDA 5050이 운영자·통합자·제조사·관제 제공자 사이의 운영 책임을 배분하지 않는다고 명시한다. 이 문장은 브리프 finding이 아니어서 이번 페이지에 쓸 수 없다. 다음 실행 후보로만 남긴다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "직접 범위에 대한 추정이다. 근거 f6·f7·f13·f12·f1~f3·f8이 확인됐다. 원문 19장 경계 안에 있다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "'연계 대상:'으로 표시한 추정이며 원문 19장 경계(시설·설비 제어, 로봇 자체 지능·제어)와 맞는다. f16이 추정으로 강등됐으므로 승강기 쪽 근거는 강등된 f16 범위로만 쓴다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "연결 제안이며 세부영역 번호와 명칭이 부록 A와 일치한다. L. AI·학습 기술 교차 규칙(47. AI·학습·적응과 모델 운영 연결)을 지켰다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 없다."
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
      "f15(ref-872 RoMi-H 등재 프로그램)는 2026-09-30-19·2026-09-30-21 브리프와 같은 출처다 — ref-872 id를 재사용한다",
      "f6(ref-031 VDA 5050)는 여러 이전 브리프의 출처다 — ref-031 id를 재사용한다",
      "f10·f11·f12는 59. 법·규제·보험·라이선스의 법·규제 대응 범위와 겹친다 — 이 페이지에서는 변경 승인·책임 분담·감사 이력의 근거로만 쓰고 59와 연결한다"
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
    "f16: [사실] → [추정]으로 강등한다. 기관명을 '대한승강기협회'로 바로잡는다. '승강기 제조사가 참여한 과제로 표준을 만들고 있다'는 쓰지 않는다. 대신 '대한승강기협회·ETRI·뉴빌리티가 과기정통부 선정 과제 「실내외 자율주행 로봇 상호연동 표준개발」을 위해 연 간담회(2023-05-16)에 현대엘리베이터·오티스·TK엘리베이터·미쓰비시엘리베이터 등이 참석했고, 과제는 API 기반 실시간 연동 표준과 2024-12-31까지의 표준·협의체·테스트베드를 목표로 했다'는 범위로 좁혀 쓴다 — 이유: ref-317 원문은 협회명이 다르고 제조사 참여를 간담회 참석으로만 적는다.",
    "f16은 현장 유형이 없으므로 5절 적용 사례로 세우지 않는다. 6절(변경 승인·책임 분담)이나 10절의 22. 설비·건물 시스템 연동 연결에서만 쓴다 — 이유: 5절 사례는 현장 유형 하나를 이름으로 밝혀야 한다. 5절에는 병원(f15)과 가정(f17·f18) 사례만 두고, 물류창고·제조 공장·상업 시설·실외 사례는 이번 조사에서 찾지 못했다고 적는다.",
    "ref-1358 각주의 제목을 '공동주택에 밀려오는 로봇, 또 다른 관리책임은 없을까'로 고치고 '(제목 일부만 확인)'을 뺀다 — 이유: 검증에서 원문 제목 전체를 확인했다.",
    "ref-872 각주의 발행일을 2025-05-01로 적는다 — 이유: 원문 페이지 날짜가 2025-05-01이고 2026-08-24에 갱신됐다. 브리프가 원문 미열람으로 표시했으므로 각주의 ' (원문 미열람)'과 reference_updates의 source_unopened: true는 유지한다.",
    "f1: 근거 발췌에 있는 '설계 의무 2026-09-12' 날짜를 본문에 쓰지 않는다 — 이유: ref-1345 페이지에 없는 날짜다.",
    "f5: 각주는 ref-1348만 단다. ref-1347은 f4에만 단다 — 이유: 지디넷코리아 기사는 가이드라인의 목차·쪽수를 뒷받침하지 않는다.",
    "f10: 실질적 변경의 정의와 '변경한 자를 제조자로 본다'는 규칙은 f10 주장 문장 범위를 넘지 않게 쓰고, 이 부분의 각주는 ref-1350으로 단다. 채택일·적용일은 ref-1359로 단다 — 이유: EUR-Lex 본문은 열리지 않아 검색 요약에서만 확인됐다.",
    "원문 미열람 표시: ref-872·ref-555·ref-1351·ref-1352·ref-1355의 각주 정의에서 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates의 같은 항목에 source_unopened: true를 넣는다 — 이유: 브리프에서 이 출처들은 fetched false이고, 유료 표준은 소개 페이지만 열었으며, SSRN은 403이다.",
    "f11: 제공자 지위가 넘어가는 셋째 경우를 '고위험이 아닌 AI 시스템(범용 AI 시스템 포함)의 용도를 바꿔 고위험 AI 시스템이 되게 하는 경우'로 좁혀 쓴다 — 이유: ref-1356 원문 조건이 그렇다. '용도를 바꾸면'은 일반화다.",
    "f14: 'Shaik(SSRN, 2026, 동료심사 전 원고)의 제안'으로 누구의 의견인지 밝혀 [의견]으로 쓴다. 원고가 드는 2024년 독일 자동차 공장 사고 사례는 쓰지 않는다 — 이유: 저자 주장이며 독립 확인되지 않았다.",
    "f18: '한국아파트신문 사설(2026-09-14)의 의견'임을 문장에 밝혀 [의견]으로 쓴다 — 이유: [의견]은 의견 주체를 밝혀야 한다.",
    "f13: 7절에서는 21 CFR Part 11을 'FDA 규제 대상 전자기록에 적용되는 규정으로, 감사 추적 요구의 참고 사례'로만 쓰고, 병원 현장의 의무로 서술하지 않는다 — 이유: 적용 범위가 FDA 규제 기록에 한정된다.",
    "f10·f11·f12: 법적 의무의 판정과 이행은 9절에서 f21의 연계 대상(계약 당사자·법무, 59. 법·규제·보험·라이선스)으로 두고, ROP가 이 법적 의무를 직접 진다는 식으로 쓰지 않는다 — 이유: 원문 19장 경계와 59와의 중복을 피하기 위해서다.",
    "11절: 이 영역에 걸린 기존 열린 질문에 oq-265(ANSI/A3 R15.08-3-2026의 사용자 운영 절차·교육·변경 관리를 여러 제조사 로봇 현장에서 누가 이행하는가)를 더해 모두 7건(oq-145·oq-149·oq-185·oq-241·oq-249·oq-259·oq-265)을 미해결로 싣는다 — 이유: 입력 열린 질문 목록에서 영역 58에 걸린 질문인데 브리프가 빠뜨렸다.",
    "용어집 후보 '데이터 보유자'의 정의에서 '사용자와의 계약 없이 비개인 데이터를 활용할 수 없다'를 '사용자의 동의 없이 비개인 데이터를 이용할 수 없고, 데이터 권리를 사용자와의 계약으로 정해야 한다'로 고친다 — 이유: ref-1345 원문 표현이 'without the user's agreement'와 'must have a contract'로 나뉘어 있다.",
    "f6: '의미적 버전'은 기존 용어집 항목 '의미적 버전 관리 (Semantic Versioning (SemVer))'에 링크하고 새 용어로 등록하지 않는다. 주 버전 변경은 명세 표현대로 '대개(typically) 호환을 깨는 변경'으로 쓴다 — 이유: 용어 일관성과 원문의 한정 표현을 지키기 위해서다.",
    "ref-1356·ref-1357 각주의 기관 표기에 'EU AI법 조문 비공식 게재본'임을 드러낸다(예: 'Future of Life Institute (EU AI법 조문 게재본)') — 이유: 공식 관보(EUR-Lex)가 아니다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 21건, 미확인 1건(f16), 교차 확인 0건. 강등: f16 사실 → 추정(기관명이 대한승강기협회로 다르고, 제조사 참여를 간담회 참석 이상으로 과장했다). 원문 미열람 출처: ref-872(검증 중 원문 일치 확인), ref-555(EUR-Lex 본문을 열지 못해 검색 요약으로 확인), ref-1351·ref-1352(유료 표준, 소개 페이지·검색 요약), ref-1355(SSRN 403, 검색 요약). 주의: 사실 주장이 모두 단일 출처다. 핵심 질문(누가 연동 오류를 고치고 변경을 승인하는가)의 답과 ROP 직접 범위는 추정(f19·f20·f21)이다. 이를 한 번에 정한 공개 표준이나 책임 분담표는 찾지 못했다(oq-241 미해결). EU AI법 조문은 비공식 게재본(artificialintelligenceact.eu)으로 확인했고, 21 CFR Part 11은 FDA 규제 기록에 한정되는 참고 사례다. 적용 사례는 병원(싱가포르)과 가정(한국 공동주택)뿐이며 물류창고·제조 공장·상업 시설·실외 사례는 없다. 브리프에서 webfetch로 연 출처 11건의 fetch_url이 비어 있었지만, 검증에서 다시 열어 내용 일치를 확인했다. 검색 3회를 썼다(리서치 15회와 합쳐 18회/30). 참고: VDA 5050 3.0.0 원문(ref-031) 2장은 운영자·통합자·제조사·관제 제공자 사이의 운영 책임을 배분하지 않는다고 명시한다. 이번 브리프 finding이 아니므로 다음 실행 후보로 둔다. 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-09-30-22/pages.json

```json
{
  "run_id": "2026-09-30-22",
  "outline": [
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 800,
      "summary": "연동 오류 수정·변경 승인 주체를 한 번에 정한 공개 표준·책임 분담표는 찾지 못했고, 규칙은 변경 주체 책임 법규·인터페이스 버전 규칙·계약·조달 장치의 조합으로 정해지는 것으로 보인다. [추정][^ref-555][^ref-872]",
      "planned_findings": [
        "f19",
        "f18",
        "f14",
        "f1"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1200,
      "summary": "실질적 변경, 데이터 보유자, 모델 계약 조항, 산업데이터 사용·수익권, 의미적 버전 관리, API 폐기 정책, 서비스 수준 협약, 감사 추적을 정의한다. [사실][^ref-555][^ref-1345]",
      "planned_findings": [
        "f10",
        "f11",
        "f1",
        "f3",
        "f4",
        "f6",
        "f7",
        "f8",
        "f13"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1400,
      "summary": "병원(싱가포르 RoMi-H 통합자 등재)과 가정(한국 공동주택 로봇 도입) 사례를 여섯 항목으로 정리한다. [사실][^ref-872][^ref-1358]",
      "planned_findings": [
        "f15",
        "f17",
        "f18"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2900,
      "summary": "변경 주체 책임과 사전 자격, 데이터 접근·공유 계약, 인터페이스 버전·폐기 규칙, 서비스 수준·감사 이력의 네 갈래 접근을 정리한다. [추정][^ref-555][^ref-1346]",
      "planned_findings": [
        "f10",
        "f11",
        "f9",
        "f15",
        "f16",
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f12",
        "f13"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1500,
      "summary": "EU 데이터법·모델 계약 조항, 산업디지털전환법·산업데이터 계약 가이드라인, VDA 5050 버전 규칙, Kubernetes 폐기 정책, ISO/IEC 19086-1, IEC 62443-2-4, EU 기계류 규정, EU AI법 제25·26조, 21 CFR Part 11을 표로 모은다. [사실][^ref-1345][^ref-031]",
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
        "f11",
        "f12",
        "f13"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 800,
      "summary": "EC 모델 계약 조항 권고 초안, 산업데이터 계약 가이드라인, Shaik(SSRN, 2026, 동료심사 전 원고)의 책임 배분 제안을 소개한다. [사실][^ref-1346] [의견][^ref-1355]",
      "planned_findings": [
        "f3",
        "f5",
        "f14"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1300,
      "summary": "ROP는 인터페이스 버전·폐기 일정, 변경 기록, 감사 이력, 데이터 조건 표시, SLA 지표 보고를 맡고 계약·법적 판정·제조사 API·설비 안전은 연계 대상으로 보인다. [추정][^ref-031][^ref-555]",
      "planned_findings": [
        "f20",
        "f21"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1700,
      "summary": "2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65번 세부영역과의 연결을 이름과 함께 적는다. [추정][^ref-031][^ref-1356]",
      "planned_findings": [
        "f22",
        "f16"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "section": "11. 열린 질문",
      "budget_chars": 1800,
      "summary": "기존 열린 질문 8건(oq-145·149·185·241·249·259·265·268)은 미해결로 두고 새 질문 5건을 올린다.",
      "planned_findings": [
        "f1",
        "f7",
        "f5",
        "f10",
        "f16"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 첫 작성(병원·가정 적용 사례, 데이터 계약·버전·폐기 규칙·SLA·감사 이력, 책임 경계, 연결 14건, 열린 질문 8건+새 질문 5건), 13절 각주 17건, 1차 조건부 승인 수정 17건 반영"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area58-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 58. 다사업자 책임·계약·데이터 의 \"6. 대표 접근법과 기술\" 절(2,613자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area58-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 58. 다사업자 책임·계약·데이터 의 \"11. 열린 질문\" 절(1,824자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area58-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 58. 다사업자 책임·계약·데이터 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,269자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area58-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 58. 다사업자 책임·계약·데이터 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,155자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area58-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 58. 다사업자 책임·계약·데이터 의 \"4. 핵심 개념과 용어\" 절(1,005자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area58-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 58. 다사업자 책임·계약·데이터 의 \"3. 왜 중요한가\" 절(649자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 58. 다사업자 책임·계약·데이터 | 영역 심화: 3~11절 첫 작성(병원·가정 적용 사례, 데이터 접근 계약·인터페이스 버전·폐기 규칙·서비스 수준·감사 이력, 책임 경계, 새 열린 질문 5건), 1차 조건부 승인 수정 17건 반영 | run 2026-09-30-22",
  "index_updates": {
    "home_recent": "2026-09-30 — 58. 다사업자 책임·계약·데이터: 3~11절 첫 작성(EU 데이터법·산업데이터 계약, VDA 5050 버전 규칙·API 폐기 정책, SLA·감사 이력, 병원·가정 사례, 새 열린 질문 5건)",
    "category_recent": "2026-09-30 — 58. 다사업자 책임·계약·데이터: 영역 심화로 3~11절 첫 작성, 연동 오류 수정·변경 승인 주체를 정한 공개 표준은 찾지 못함(추정), 새 열린 질문 5건",
    "area_recent": "2026-09-30 — 58. 다사업자 책임·계약·데이터: 3~11절 첫 작성(변경 주체 책임·데이터 접근 계약·인터페이스 버전·폐기 규칙·서비스 수준·감사 이력, 병원·가정 사례, 연결 14건, 새 열린 질문 5건)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "data-holder",
      "term_ko": "데이터 보유자",
      "term_en": "Data Holder (EU Data Act)",
      "definition": "EU 데이터법에서 연결 제품이나 관련 서비스가 만든 데이터를 이용·제공할 권리나 의무를 가진 자로, 사용자 요청 시 데이터를 사용자나 제3자에게 제공해야 하며, 사용자의 동의 없이 비개인 데이터를 이용할 수 없고, 데이터 권리를 사용자와의 계약으로 정해야 한다.",
      "related_areas": [
        58,
        53
      ],
      "sources": [
        "ref-1345"
      ]
    },
    {
      "action": "new",
      "slug": "substantial-modification",
      "term_ko": "실질적 변경",
      "term_en": "Substantial Modification",
      "definition": "출시된 기계나 AI 시스템을 바꿔 새로운 위험을 만들거나 위험을 키우거나 적합성·용도에 영향을 주는 변경으로, 이를 한 자가 제조자·제공자의 의무를 지게 되는 기준이다.",
      "related_areas": [
        58,
        59,
        48,
        47
      ],
      "sources": [
        "ref-555",
        "ref-1356"
      ]
    },
    {
      "action": "new",
      "slug": "model-contractual-terms",
      "term_ko": "모델 계약 조항",
      "term_en": "Model Contractual Terms (MCTs)",
      "definition": "EU 집행위원회가 데이터법 이행을 위해 데이터 보유자·사용자·데이터 수령자 사이의 데이터 접근·이용 계약에 쓰도록 권고하는 구속력 없는 표준 계약 문안이다.",
      "related_areas": [
        58
      ],
      "sources": [
        "ref-1346"
      ]
    },
    {
      "action": "new",
      "slug": "api-deprecation-policy",
      "term_ko": "API 폐기 정책",
      "term_en": "API Deprecation Policy",
      "definition": "API 요소를 언제 어떤 공지와 유예 기간을 거쳐 폐기·제거할지, 버전을 어떻게 올릴지를 미리 정해 이용자가 호환성을 예측하게 하는 규칙이다.",
      "related_areas": [
        58,
        57,
        20,
        41
      ],
      "sources": [
        "ref-1349"
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
      "summary": "VDA 5050 공식 명세(main, 3.0.0). 이번 실행에서 의미적 버전 규칙, 토픽의 주 버전 표기, GitHub 변경 제안 절차를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-872",
      "org": "Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "RoMi-H Empanelment Programme 2025",
      "published": "2025-05-01",
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. RoMi-H 통합 시스템 통합자를 연 2회 평가·등재하는 프로그램 안내(2025-05-01, 2026-08-24 갱신). 이번 브리프는 이전 브리프 내용을 재인용했고 검증에서 원문 일치를 확인했다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-1345",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "Data Act explained",
      "published": "2025-12-15",
      "url": "https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "EU 데이터법의 연결 제품 데이터 접근권, 데이터 보유자 계약 의무, 제3자 공유, B2B 불공정 조항, 모델 계약 조항, 클라우드 전환, 적용 일정을 설명하는 집행위원회 해설(2025-12-15 갱신).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-1346",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts",
      "published": "2025-11-19",
      "url": "https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "EU 데이터법용 구속력 없는 모델 계약 조항 4벌과 클라우드 표준 계약 조항 6개의 권고 초안 게시 페이지.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-1347",
      "org": "지디넷코리아",
      "title": "산업데이터 만든 자에게 사용·수익권 부여",
      "published": "2022-03-15",
      "url": "https://zdnet.co.kr/view/?no=20220315103750",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "산업통상자원부 발표를 전한 기사. 산업디지털전환촉진법의 산업데이터 사용·수익권, 2022년 7월 시행, 산업데이터 계약 가이드라인 제정 방향을 다룬다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-1348",
      "org": "산업통상부 (공공데이터포털)",
      "title": "산업통상부_산업데이터 계약 가이드라인_20230109",
      "published": "2023-04-05",
      "url": "https://www.data.go.kr/data/15113186/fileData.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "산업데이터 계약 가이드라인 파일데이터 소개(포털 등록일 2023-04-05, 수정 2025-12-09, PDF 432쪽). 목차와 안내 내용(유의사항·표준계약서·업종별 사례)을 확인했고 PDF 본문은 열지 않았다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-1349",
      "org": "The Kubernetes Authors",
      "title": "Kubernetes Deprecation Policy",
      "published": null,
      "url": "https://kubernetes.io/docs/reference/using-api/deprecation-policy/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Kubernetes 프로젝트의 API 폐기 규칙(버전 증가로만 제거, 왕복 호환, 안정도별 유지 기간, 폐기 API 사용 경고·감사 주석·지표).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-555",
      "org": "European Parliament and Council of the European Union (EUR-Lex)",
      "title": "Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery",
      "published": "2023-06-14",
      "url": "https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. EU 기계류 규정 원문. EUR-Lex 페이지 본문을 읽지 못해 실질적 변경 정의·제18조는 검색 요약 범위만 사용했다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-1351",
      "org": "IEC / ISO (ISO/IEC JTC 1)",
      "title": "ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts",
      "published": "2016-09-21",
      "url": "https://webstore.iec.ch/en/publication/25920",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 유료 표준이라 IEC 웹스토어 소개 페이지만 열어 범위(클라우드 SLA 구성 요소·개념·용어)와 발행일을 확인했다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-1352",
      "org": "IEC (BSI Knowledge 게재)",
      "title": "IEC 62443-2-4:2023 Security for industrial automation and control systems - Security program requirements for IACS service providers",
      "published": "2023-12-15",
      "url": "https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 유료 표준. BSI 페이지에서 제목·발행일만 확인했고 범위(통합·유지보수 서비스 제공자의 보안 프로그램 요구)는 검색 요약 범위다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-1353",
      "org": "U.S. Food and Drug Administration 규정 (Cornell Law School LII 게재)",
      "title": "21 CFR § 11.10 - Controls for closed systems",
      "published": null,
      "url": "https://www.law.cornell.edu/cfr/text/21/11.10",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "미국 연방규정 21 CFR Part 11 의 폐쇄형 시스템 통제 조항. (e)항 감사 추적 요구를 확인했다. FDA 규제 대상 전자기록에 적용되는 규정이다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-317",
      "org": "전기신문 (안상민)",
      "title": "승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인",
      "published": "2023-05-17",
      "url": "https://www.electimes.com/news/articleView.html?idxno=320147",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "대한승강기협회·ETRI·뉴빌리티가 과기정통부 과제 '실내외 자율주행 로봇 상호연동 표준개발'을 위해 연 승강기기업 간담회(2023-05-16)와 과제 목표(API 기반 실시간 연동 표준, 2024-12-31까지 표준·협의체·테스트베드)를 전한 기사. 기존 ref-317 과 URL 이 같다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-1355",
      "org": "Shaik, A. S. (SSRN)",
      "title": "Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong?",
      "published": "2026-05-01",
      "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6737139",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. SSRN 게재 원고(동료심사 전). 제조사·통합자·AI 공급자·운영자 사이 책임 배분 프레임워크(RPLF)를 제안한다. SSRN 403 으로 검색 요약과 초록 소개만 확인했다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-1356",
      "org": "Future of Life Institute (EU AI법 조문 비공식 게재본)",
      "title": "Article 25: Responsibilities Along the AI Value Chain | EU Artificial Intelligence Act",
      "published": null,
      "url": "https://artificialintelligenceact.eu/article/25/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "EU AI법 제25조 비공식 게재본(공식 관보 아님). 제공자 지위 이전 조건, 최초 제공자 협력 의무, 공급자와의 서면 계약 요구를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-1357",
      "org": "Future of Life Institute (EU AI법 조문 비공식 게재본)",
      "title": "Article 26: Obligations of Deployers of High-Risk AI Systems | EU Artificial Intelligence Act",
      "published": null,
      "url": "https://artificialintelligenceact.eu/article/26/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "EU AI법 제26조 비공식 게재본(공식 관보 아님). 배포자의 로그 최소 6개월 보관, 운영 감시·통지·사용 중단·중대 사고 보고 의무를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-1358",
      "org": "한국아파트신문 (사설)",
      "title": "공동주택에 밀려오는 로봇, 또 다른 관리책임은 없을까",
      "published": "2026-09-14",
      "url": "https://www.hapt.co.kr/news/articleView.html?idxno=169488",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "공동주택 로봇 도입 사례와 관리주체 책임 확대 우려, 이동로봇 특별법안의 책임 분담·책임보험 내용을 다룬 사설.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    },
    {
      "id": "ref-1359",
      "org": "European Agency for Safety and Health at Work (EU-OSHA)",
      "title": "Regulation 2023/1230/EU - machinery",
      "published": null,
      "url": "https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "EU 기계류 규정 소개. 채택일(2023-06-14), 적용일(2027-01-20), 자율 이동 기계·AI 안전 기능 포괄, 제조자 의무를 요약한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "여러 제조사 로봇의 운영 데이터를 모으는 오케스트레이션 플랫폼 사업자는 EU 데이터법상 데이터 보유자인가, 사용자가 지정한 제3자 데이터 수령자인가, 그리고 그에 따라 제조사에게 데이터 제공을 요구할 수 있는 범위는 어디까지인가?",
      "areas": [
        58,
        59
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 제조사·관제 API 의 주 버전 변경이나 폐기를 오케스트레이션 플랫폼에 사전 통지하는 기간과 유예 기간을 계약이나 인터페이스 표준에 명시한 공개 사례가 있는가?",
      "areas": [
        58,
        20,
        57
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 산업데이터 계약 가이드라인의 표준계약서와 업종별 사례가 로봇 운영 데이터(지도·작업 이력·센서 로그)처럼 여러 사업자가 함께 만드는 데이터를 어떻게 다루는가?",
      "areas": [
        58,
        15
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "오케스트레이션 플랫폼에서 경로망·속도 제한·작업 규칙 같은 설정을 바꾸는 일이 EU 기계류 규정의 실질적 변경에 해당해 플랫폼 운영자나 통합자가 제조자 의무를 지는 경우가 있는가?",
      "areas": [
        58,
        59,
        48
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇-승강기 연동 표준 과제의 결과물(표준 번호, 연동 장애 시 승강기 제조사·로봇 제조사·관제 사업자의 책임 분담)이 공개되었는가?",
      "areas": [
        58,
        22
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
  "standards_updates": [
    {
      "name": "EU 데이터법 (Regulation (EU) 2023/2854, Data Act)",
      "kind": "프레임워크",
      "org": "European Union (European Commission 해설)",
      "url": "https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained",
      "related_areas": [
        58,
        53,
        59
      ],
      "summary": "2025-09-12부터 적용. 연결 제품 사용자의 데이터 접근·이용·이전과 제3자 공유, 데이터 보유자의 사용자 계약 의무, 기업 간 불공정 조항 무효, 데이터 처리 서비스 전환 요금 폐지(2027-01-12)를 정한다.",
      "ref_id": "ref-1345"
    },
    {
      "name": "EU 데이터법 모델 계약 조항·클라우드 표준 계약 조항 권고 초안",
      "kind": "프레임워크",
      "org": "European Commission",
      "url": "https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding",
      "related_areas": [
        58
      ],
      "summary": "2025-11-19 권고 초안. 데이터 접근·이용 계약용 구속력 없는 모델 계약 조항 네 벌과 클라우드 표준 계약 조항 여섯 개(전환·이탈, 해지, 보안·업무 연속성, 비분산, 일방 변경 금지, 책임)를 제시한다.",
      "ref_id": "ref-1346"
    },
    {
      "name": "산업데이터 계약 가이드라인",
      "kind": "프레임워크",
      "org": "산업통상부",
      "url": "https://www.data.go.kr/data/15113186/fileData.do",
      "related_areas": [
        58
      ],
      "summary": "산업데이터 거래 당사자를 위한 유의사항·표준계약서·업종별 사례를 안내하는 432쪽 가이드라인(공공데이터포털 등록 2023-04-05). 본문 미열람.",
      "ref_id": "ref-1348"
    },
    {
      "name": "Kubernetes Deprecation Policy (API 폐기 정책)",
      "kind": "오픈소스",
      "org": "The Kubernetes Authors",
      "url": "https://kubernetes.io/docs/reference/using-api/deprecation-policy/",
      "related_areas": [
        58,
        57,
        41
      ],
      "summary": "API 요소는 API 그룹 버전을 올려야만 제거하고, 왕복 변환 정보 보존, 안정도별 유지 기간(베타 9개월 또는 3개 부 릴리스), 폐기 API 사용 시 경고 헤더·감사 주석·지표를 남기게 하는 규칙.",
      "ref_id": "ref-1349"
    },
    {
      "name": "ISO/IEC 19086-1:2016 클라우드 SLA 프레임워크 — Part 1: 개요와 개념",
      "kind": "표준",
      "org": "ISO/IEC (JTC 1)",
      "url": "https://webstore.iec.ch/en/publication/25920",
      "related_areas": [
        58,
        39
      ],
      "summary": "클라우드 서비스 수준 협약의 공통 구성 요소(개요, 서비스 계약과 SLA의 관계, 개념, 용어)를 정하며, 표준 SLA 구조나 서비스 수준 목표 세트는 정하지 않는다. 원문 미열람.",
      "ref_id": "ref-1351"
    },
    {
      "name": "IEC 62443-2-4:2023 IACS 서비스 제공자 보안 프로그램 요구사항",
      "kind": "표준",
      "org": "IEC",
      "url": "https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1",
      "related_areas": [
        58,
        52,
        55
      ],
      "summary": "산업 자동화·제어 시스템 서비스 제공자가 통합·유지보수 중 자산 소유자에게 제공할 보안 관련 프로세스 요구와 역할 구분을 정한다. 원문 미열람.",
      "ref_id": "ref-1352"
    },
    {
      "name": "EU AI법 제25조(AI 가치사슬 책임)·제26조(고위험 AI 배포자 의무)",
      "kind": "프레임워크",
      "org": "European Union (Future of Life Institute 비공식 게재본 경유)",
      "url": "https://artificialintelligenceact.eu/article/25/",
      "related_areas": [
        58,
        47,
        59
      ],
      "summary": "제25조는 고위험 AI 시스템에 실질적 변경 등을 한 자를 제공자로 보고 공급자와의 서면 계약을 요구하며, 제26조는 배포자에게 자동 생성 로그 최소 6개월 보관과 감시·통지 의무를 지운다.",
      "ref_id": "ref-1356"
    },
    {
      "name": "21 CFR Part 11 §11.10 폐쇄형 시스템 통제(감사 추적)",
      "kind": "프레임워크",
      "org": "U.S. Food and Drug Administration",
      "url": "https://www.law.cornell.edu/cfr/text/21/11.10",
      "related_areas": [
        58,
        37,
        52
      ],
      "summary": "FDA 규제 대상 전자기록에 적용되는 규정으로, (e)항이 보안이 적용된 컴퓨터 생성 타임스탬프 감사 추적을 요구한다. 감사 추적 요구의 참고 사례로 쓴다.",
      "ref_id": "ref-1353"
    }
  ],
  "additional_research_requests": [
    "6절·3절: VDA 5050 3.0.0 원문 2장이 운영자·통합자·제조사·관제 제공자 사이의 운영 책임을 배분하지 않는다고 명시한다는 점(1차 검증 노트 참고)을 finding 으로 확인해 달라 — 핵심 질문의 답을 표준 쪽 근거로 보강하기 위해서다.",
    "4·6·7절: 산업 디지털 전환 촉진법 제9조(공동 생성 데이터·제3자 제공 시 권리) 조문을 국가법령정보센터에서 직접 확인해 달라 — 현재 근거가 기사 1건(신뢰도 low)이다.",
    "6·7절: 산업데이터 계약 가이드라인 PDF 본문에서 계약 유형 구분과 표준계약서 조항, 로봇·설비 데이터에 해당하는 업종별 사례를 확인해 달라.",
    "6절: EU 기계류 규정 제18조와 실질적 변경 정의를 EUR-Lex 원문 또는 다른 공식 해설로 교차 확인해 달라 — 현재 검색 요약 범위에서만 확인됐다.",
    "5절: 물류창고·제조 공장·상업 시설·실외 현장의 다사업자 책임·계약(연동 오류 수정·변경 승인·데이터 권리) 사례가 필요하다 — 현재 병원·가정 사례뿐이다.",
    "5절: 병원(싱가포르 RoMi-H)·가정(한국 공동주택) 사례의 완료·인계와 예외·성과 칸(연동 완료 인정 기준, 장애 때 복구 주체)의 근거가 필요하다.",
    "5절: 이동로봇 특별법안의 원문·발의일과 책임 분담·책임보험 조항 내용을 확인해 달라.",
    "3·11절: 로봇 오케스트레이션 도입 계약의 책임 분담표·표준 계약 조항 공개 사례(oq-241)를 계속 찾아 달라.",
    "전반: 이 페이지의 사실 주장은 모두 단일 출처다. EU 데이터법·Kubernetes 폐기 정책·EU AI법 조항은 공식 관보(EUR-Lex) 등 독립 출처로 교차 확인이 필요하다."
  ],
  "fixes_applied": [
    "f16 강등·범위 축소 — 6절 '변경 주체 책임과 사전 자격'에서 [추정]으로 쓰고 기관명을 대한승강기협회로 고쳤으며, 제조사 참여를 대한승강기협회·ETRI·뉴빌리티가 연 간담회(2023-05-16) 참석으로, 과제를 API 기반 실시간 연동 표준과 2024-12-31까지의 표준·협의체·테스트베드 목표로 좁혀 썼다(10절 22. 설비·건물 시스템 연동 연결도 [추정]).",
    "f16 5절 제외 — 5절에는 병원(f15)·가정(f17·f18) 사례만 두고 물류창고·제조 공장·상업 시설·실외 사례를 이번 조사에서 찾지 못했다고 적었으며, f16은 6절과 10절의 22. 설비·건물 시스템 연동 연결에서만 썼다.",
    "ref-1358 제목 — 13절 각주와 reference_updates 의 제목을 '공동주택에 밀려오는 로봇, 또 다른 관리책임은 없을까'로 고치고 '(제목 일부만 확인)'을 뺐다.",
    "ref-872 발행일 — 13절 각주와 reference_updates 의 발행일을 2025-05-01로 적고, 각주의 ' (원문 미열람)'과 source_unopened: true 를 유지했다.",
    "f1 날짜 — '설계 의무 2026-09-12'를 본문 어디에도 쓰지 않고 2025-09-12 적용만 썼다(3·6·7절).",
    "f5 각주 — 산업데이터 계약 가이드라인 문장(6·7·8절)에는 ref-1348만 달고, ref-1347은 산업 디지털 전환 촉진법(f4) 문장에만 달았다.",
    "f10 각주 — 실질적 변경 정의와 '변경한 자를 제조자로 본다'는 규칙은 f10 주장 범위 안에서 쓰고 ref-1350을, 채택일(2023-06-14)·적용일(2027-01-20)은 ref-1359를 달았다(4·6·7절).",
    "원문 미열람 표시 — ref-872·ref-555·ref-1351·ref-1352·ref-1355 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 같은 항목에 source_unopened: true 를 넣었다.",
    "f11 범위 — 6절에서 제공자 지위가 넘어가는 셋째 경우를 '고위험이 아닌 AI 시스템(범용 AI 시스템 포함)의 용도를 바꿔 고위험 AI 시스템이 되게 한 경우'로 좁혀 썼다.",
    "f14 의견 주체 — 3절과 8절에서 'Shaik(SSRN, 2026, 동료심사 전 원고)의 제안'으로 누구의 의견인지 밝혀 [의견]으로 썼고, 2024년 독일 자동차 공장 사고 사례는 쓰지 않았다.",
    "f18 의견 주체 — 3절과 5절에서 '한국아파트신문 사설(2026-09-14)의 의견'임을 문장에 밝혀 [의견]으로 썼다.",
    "f13 적용 범위 — 7절 표에서 21 CFR Part 11을 'FDA 규제 대상 전자기록에 적용되는 규정으로, 감사 추적 요구의 참고 사례'로만 썼고, 6절에서도 '감사 이력의 참고 사례'로 두어 병원 현장 의무로 서술하지 않았다.",
    "f10·f11·f12 경계 — 9절 표와 연계 대상 단락에서 법적 의무의 판정·이행을 계약 당사자·법무와 59. 법·규제·보험·라이선스의 연계 대상으로 두고, 이 페이지가 그 의무를 ROP가 직접 지는 것으로 서술하지 않는다고 밝혔다.",
    "11절 열린 질문 — oq-265를 더해 oq-145·oq-149·oq-185·oq-241·oq-249·oq-259·oq-265 7건을 모두 열림(미해결)으로 실었다. 입력 열린 질문 목록에서 영역 58에 걸린 oq-268도 같은 이유로 함께 실어 기존 질문은 8건이다.",
    "용어집 '데이터 보유자' — 정의의 해당 부분을 '사용자의 동의 없이 비개인 데이터를 이용할 수 없고, 데이터 권리를 사용자와의 계약으로 정해야 한다'로 고쳐 glossary_updates 에 냈고, 4절 본문도 같은 구분으로 썼다.",
    "f6 용어 — '의미적 버전'을 기존 용어집 항목 [의미적 버전 관리](../../glossary/semantic-versioning.md)에 링크하고 새 용어로 등록하지 않았으며, 주 버전 변경을 '대개(typically) 호환을 깨는 변경'으로 썼다(4·6절).",
    "ref-1356·ref-1357 기관 표기 — 13절 각주와 reference_updates 의 기관을 'Future of Life Institute (EU AI법 조문 비공식 게재본)'으로 고쳤고, 7절 표 아래에 비공식 게재본으로 확인했음을 적었다.",
    "분량 초과 자동 분리: 58. 다사업자 책임·계약·데이터 본문 11,154자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,719자"
  ]
}
```

### runs/2026-09-30-22/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area58-s6.md (2,613자)
    - docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area58-s11.md (1,824자)
    - docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area58-s7.md (1,269자)
    - docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area58-s10.md (1,155자)
    - docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area58-s4.md (1,005자)
    - docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area58-s3.md (649자)
```

### runs/2026-09-30-22/pages/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md

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
updated: 2026-09-30
sources: [ref-031, ref-872, ref-1345, ref-1346, ref-1347, ref-1348, ref-1349, ref-555, ref-1351, ref-1352, ref-1353, ref-317, ref-1355, ref-1356, ref-1357, ref-1358, ref-1359]
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
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
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

여러 사업자가 함께 운영하는 현장에서 연동 오류를 누가 고치고 변경을 누가 승인하는지를 한 번에 정한 공개 표준이나 책임 분담표는 이번 조사(2026-09-30 기준)에서 찾지 못했고, 실제 규칙은 변경한 주체에게 제조자·제공자 의무를 지우는 법 규정, 인터페이스 표준의 버전·폐기 규칙, 서비스 수준 협약·표준 계약 조항과 통합자 사전 자격 같은 계약·조달 장치가 겹쳐 정해지는 것으로 보인다. [추정][^ref-555][^ref-1356][^ref-031][^ref-1349][^ref-1351][^ref-1346][^ref-1352][^ref-872]

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
| 작업 대상 | 차량 주차, 단지 순찰, 물품 운반 [사실][^ref-1358] |
| 수행 자원 | 시흥 힐스테이트더웨이브시티 주차로봇 2세트(실증), 서울 송파구 아파트 자율주행 순찰로봇 2대, 강남 타워팰리스 사족보행로봇(기술검증), 부산 강서구 아파트 운반로봇 서비스 [사실][^ref-1358] |
| 제약 | 발의된 이동로봇 특별법안이 개인정보 처리·책임 분담·책임보험 가입 같은 안전관리 체계를 담는다고 전해졌다(법안 원문 미확인) [사실][^ref-1358] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

같은 사설(한국아파트신문, 2026-09-14)의 의견으로는 이런 로봇이 들어오면 관리주체의 관리 영역과 책임이 넓어질 수 있어, 도입 전에 책임 범위를 명확히 해야 한다. [의견][^ref-1358] 사례마다 제조사·관제 사업자·관리주체가 장애를 어떻게 나눠 맡는지는 확인하지 못했다. 가정 로봇의 원격 조작자 책임은 [oq-185](../../open-questions.md)에서 열려 있다.

물류창고·제조 공장·상업 시설·실외 현장의 다사업자 책임·계약 사례는 이번 조사에서 찾지 못했다.

## 6. 대표 접근법과 기술

다사업자 책임·계약·데이터를 다루는 접근은 변경한 주체에게 책임을 지우는 규정과 사전 자격, 데이터 접근·공유 계약, 인터페이스 버전·폐기 규칙, 서비스 수준 약속과 감사 이력의 네 갈래로 모이는 것으로 보인다. [추정][^ref-555][^ref-1346][^ref-031][^ref-1351]

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area58-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역에 걸리는 규칙은 데이터 권리(EU 데이터법·국내 산업 디지털 전환 촉진법), 인터페이스 변경(VDA 5050·Kubernetes 폐기 정책), 서비스 수준·보안·기록(ISO/IEC 19086-1·IEC 62443-2-4·21 CFR Part 11), 변경 주체 책임(EU 기계류 규정·EU AI법)으로 나뉜다.

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area58-s7.md)에 있다.

## 8. 대표 연구와 자료

- 유럽연합 집행위원회, 데이터 접근·이용 모델 계약 조항과 클라우드 표준 계약 조항 권고 초안(2025) — 데이터법 이행용 계약 문안 네 벌과 클라우드 계약 조항 여섯 개를 담은 구속력 없는 초안이며, 의무적 기업 간 데이터 공유의 합리적 보상 지침은 추후 발표 예정으로 되어 있다. [사실][^ref-1346]
- 산업통상부, 산업데이터 계약 가이드라인(2023) — 국내 산업데이터 거래 당사자를 위한 유의사항·표준계약서·업종별 사례를 담은 432쪽 자료다. [사실][^ref-1348]
- Shaik, A. S., Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong?(SSRN, 2026, 동료심사 전 원고) — Shaik의 제안은 로봇 제조사(OEM)·시스템 통합자·AI 공급자·운영자 사이의 책임을 통제력(피해를 막을 수 있었는가)·예견 가능성·정보 비대칭의 세 원칙으로 배분하는 위험 비례 책임 프레임워크(RPLF)이며, 저자는 이를 상업 계약과 기존 보험으로 구현할 수 있다고 주장한다. [의견][^ref-1355]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사 어댑터별 인터페이스 버전과 폐기 일정 관리, 연동·설정 변경의 요청·승인·적용 기록 [추정][^ref-031][^ref-1349] | 로봇 펌웨어와 제조사 API의 수명주기(로봇 제조사) [추정][^ref-555][^ref-1356] |
| 시설·설비 제어 | 설비 어댑터의 인터페이스 버전 관리와 연동 변경 기록 [추정][^ref-031][^ref-1349] | 승강기·출입문 쪽 연동 인터페이스와 설비 안전(설비 제조사·관리주체) [추정][^ref-317][^ref-1358] |
| 업종별 조건 | 누가 언제 어떤 명령·변경을 했는지 남기는 타임스탬프 감사 이력과 보관, 데이터 항목별 소유·접근·반출 조건 표시, 계약한 서비스 수준 지표의 측정·보고 [추정][^ref-1353][^ref-1357][^ref-1345][^ref-1346][^ref-1351] | 계약 체결, 법적 책임 판정·보험·규제 적합성 평가(계약 당사자·법무, [59. 법·규제·보험·라이선스](law-regulation-insurance-and-licensing.md)) [추정][^ref-555][^ref-1356][^ref-1355] |

이 영역에서 ROP가 직접 맡을 범위는 제조사·설비 어댑터별 인터페이스 버전과 폐기 일정 관리, 연동·설정 변경의 요청·승인·적용 기록, 타임스탬프 감사 이력과 보관, 데이터 항목별 소유·접근·반출 조건 표시, 계약한 서비스 수준 지표의 측정·보고로 보인다. [추정][^ref-031][^ref-1349][^ref-1353][^ref-1357][^ref-1345][^ref-1346][^ref-1351]

연계 대상: 계약 체결과 법적 책임 판정·보험·규제 적합성 평가는 계약 당사자와 법무에, 로봇 펌웨어와 제조사 API의 수명주기는 로봇 제조사에, 승강기·출입문 쪽 연동 인터페이스와 설비 안전은 설비 제조사·관리주체에 속하므로, ROP는 그들이 정한 조건을 운영 제약으로 받고 판단 근거가 되는 기록과 데이터를 제공하는 쪽을 맡는 것으로 보인다. [추정][^ref-555][^ref-1356][^ref-317][^ref-1358][^ref-1355] EU 기계류 규정과 EU AI법이 정하는 제조자·제공자·배포자 의무를 누가 지는지 판정하고 이행하는 일도 이 연계 대상에 들며, 이 페이지는 그 의무를 ROP가 직접 지는 것으로 서술하지 않는다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

범위 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 인터페이스 버전 규칙, 설비 연동, 감사 이력, 데이터 권리, 규제 책임, 조달, AI 가치사슬 책임, 적용 현장을 통해 열네 개 세부영역과 이어지는 것으로 보인다. [추정][^ref-031][^ref-1357][^ref-1345][^ref-1356]

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area58-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 기존 열린 질문 8건은 모두 열려 있고, 이번 실행에서 새 질문 5건을 올렸다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 열린 질문](../../topics/2026/2026-09-30-area58-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30 (원문 미열람)
[^ref-1345]: European Commission (Shaping Europe's digital future), Data Act explained, 2025-12-15, https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained, 접근일 2026-09-30
[^ref-1346]: European Commission (Shaping Europe's digital future), Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts, 2025-11-19, https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding, 접근일 2026-09-30
[^ref-1348]: 산업통상부 (공공데이터포털), 산업통상부_산업데이터 계약 가이드라인_20230109, 2023-04-05, https://www.data.go.kr/data/15113186/fileData.do, 접근일 2026-09-30
[^ref-1349]: The Kubernetes Authors, Kubernetes Deprecation Policy, 미확인, https://kubernetes.io/docs/reference/using-api/deprecation-policy/, 접근일 2026-09-30
[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)
[^ref-1351]: IEC / ISO (ISO/IEC JTC 1), ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts, 2016-09-21, https://webstore.iec.ch/en/publication/25920, 접근일 2026-09-30 (원문 미열람)
[^ref-1352]: IEC (BSI Knowledge 게재), IEC 62443-2-4:2023 Security for industrial automation and control systems - Security program requirements for IACS service providers, 2023-12-15, https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1, 접근일 2026-09-30 (원문 미열람)
[^ref-1353]: U.S. Food and Drug Administration 규정 (Cornell Law School LII 게재), 21 CFR § 11.10 - Controls for closed systems, 미확인, https://www.law.cornell.edu/cfr/text/21/11.10, 접근일 2026-09-30
[^ref-317]: 전기신문 (안상민), 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인, 2023-05-17, https://www.electimes.com/news/articleView.html?idxno=320147, 접근일 2026-09-30
[^ref-1355]: Shaik, A. S. (SSRN), Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong?, 2026-05-01, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6737139, 접근일 2026-09-30 (원문 미열람)
[^ref-1356]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 25: Responsibilities Along the AI Value Chain | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/25/, 접근일 2026-09-30
[^ref-1357]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 26: Obligations of Deployers of High-Risk AI Systems | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/26/, 접근일 2026-09-30
[^ref-1358]: 한국아파트신문 (사설), 공동주택에 밀려오는 로봇, 또 다른 관리책임은 없을까, 2026-09-14, https://www.hapt.co.kr/news/articleView.html?idxno=169488, 접근일 2026-09-30
```

### docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md

```markdown
---
title: "58. 다사업자 책임·계약·데이터"
type: area
category: "P. 거버넌스·법규·사회"
area_no: 58
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [P. 거버넌스·법규·사회](index.md) › 58. 다사업자 책임·계약·데이터

# 58. 다사업자 책임·계약·데이터

!!! info "소속 대분류"
    [P. 거버넌스·법규·사회](index.md) — 핵심 질문:
    여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
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

### runs/2026-09-30-22/pages/topics/2026/2026-09-30-area58-s6.md

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
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-872, ref-1345, ref-1346, ref-1347, ref-1348, ref-1349, ref-555, ref-1351, ref-1352, ref-1353, ref-317, ref-1356, ref-1357, ref-1359]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#6
---

[홈](../../index.md) › [주제](../index.md) › 58. 다사업자 책임·계약·데이터 — 대표 접근법과 기술

# 58. 다사업자 책임·계약·데이터 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 다사업자 책임·계약·데이터를 다루는 접근은 변경한 주체에게 책임을 지우는 규정과 사전 자격, 데이터 접근·공유 계약, 인터페이스 버전·폐기 규칙, 서비스 수준 약속과 감사 이력의 네 갈래로 모이는 것으로 보인다. [추정][^ref-555][^ref-1346][^ref-031][^ref-1351]
- 이 페이지는 [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

다사업자 책임·계약·데이터를 다루는 접근은 변경한 주체에게 책임을 지우는 규정과 사전 자격, 데이터 접근·공유 계약, 인터페이스 버전·폐기 규칙, 서비스 수준 약속과 감사 이력의 네 갈래로 모이는 것으로 보인다. [추정][^ref-555][^ref-1346][^ref-031][^ref-1351]

### 변경 주체 책임과 사전 자격

EU 기계류 규정(Regulation (EU) 2023/1230)은 2023-06-14에 채택되어 2027-01-20부터 적용된다. [사실][^ref-1359] 이 규정은 기계에 실질적 변경을 한 자연인·법인을 제조자로 보아 제조자 의무를 지게 하고, 적합성에 영향을 주지 않는 수리·정비는 실질적 변경으로 보지 않는다. [사실][^ref-555]

EU AI법 제25조는 유통자·수입자·배포자(deployer)·제3자가 고위험 AI 시스템에 자기 이름을 붙이거나 실질적 변경을 한 경우, 그리고 고위험이 아닌 AI 시스템(범용 AI 시스템 포함)의 용도를 바꿔 고위험 AI 시스템이 되게 한 경우 그를 제공자로 본다. [사실][^ref-1356] 같은 조는 최초 제공자에게 기술 문서·정보·기술적 접근을 주는 협력 의무를 지우고, 제공자와 부품·도구·서비스 공급자가 필요한 정보·기능·기술적 접근·지원을 서면 계약으로 정하게 한다(오픈소스 제외). [사실][^ref-1356]

IEC 62443-2-4:2023은 산업 자동화·제어 시스템(Industrial Automation and Control Systems, IACS) 서비스 제공자가 통합·유지보수 중에 자산 소유자에게 제공할 보안 관련 프로세스 요구를 정하고, 자산 소유자·서비스 제공자·제품 공급자를 구분하며 업종별로 요구를 골라 쓰는 프로파일을 둔다. [사실][^ref-1352] 조달 쪽에서는 5절의 병원 사례처럼 통합자를 미리 평가·등재해 연동 책임 주체를 정하는 방법이 있다. [사실][^ref-872]

설비 연동에서는 대한승강기협회·ETRI·뉴빌리티가 과기정통부 선정 과제 「실내외 자율주행 로봇 상호연동 표준개발」을 위해 연 간담회(2023-05-16)에 현대엘리베이터·오티스·TK엘리베이터·미쓰비시엘리베이터 등이 참석했고, 과제는 API 기반 실시간 연동 표준과 2024-12-31까지의 표준·협의체·테스트베드를 목표로 했으며, 연동 장애 때의 책임 분담은 기사에서 다루지 않는다. [추정][^ref-317]

### 데이터 접근·공유 계약

EU 데이터법(Regulation (EU) 2023/2854)은 2025-09-12부터 일반 적용되며, 연결 제품 사용자가 제품 사용으로 함께 만든 데이터에 접근·이용·이전할 수 있게 한다. [사실][^ref-1345] 사용자는 데이터를 직접 또는 데이터 보유자를 통해 자신이 고른 제3자에게 공유하게 할 수 있고, 기업 간 계약에서 일방적으로 부과된 조항 가운데 '항상 불공정'·'불공정으로 추정'되는 조항은 구속력이 없으며, 데이터 처리 서비스 간 전환 요금은 2027-01-12부터 완전히 없어진다. [사실][^ref-1345]

유럽연합 집행위원회의 권고 초안(2025-11-19)은 구속력 없는 모델 계약 조항 네 벌(데이터 보유자–사용자, 사용자–데이터 수령자, 데이터 보유자–데이터 수령자(보상 포함), 자발적 공유자–수령자)과 클라우드 표준 계약 조항 여섯 개(전환·이탈, 해지, 보안·업무 연속성, 비분산, 일방 변경 금지, 책임)를 제시한다. [사실][^ref-1346]

국내에서는 산업 디지털 전환 촉진법(2022-07 시행)이 산업데이터 생성에 투자한 자에게 그 데이터의 사용·수익권을 인정하고 관계자 간 계약 체결을 권고하며, 정부가 산업데이터 계약 지침을 마련하도록 했다(산업통상자원부 발표를 전한 기사 기준). [사실][^ref-1347] 산업통상부의 산업데이터 계약 가이드라인(공공데이터포털 등록 2023-04-05, PDF 432쪽)은 총론·법적기초·산업데이터 가치 산정·계약의 유형·개인보상·국외이전으로 구성되고 유의사항·표준계약서·업종별 사례를 안내한다. [사실][^ref-1348] 가이드라인 본문은 아직 열람하지 못했다.

### 인터페이스 버전·폐기 규칙

VDA 5050 3.0.0은 주.부.수정 형식의 의미적 버전을 써서 주 버전은 대개(typically) 필수 필드 추가 같은 호환을 깨는 변경, 부 버전은 선택 매개변수 추가 같은 새 기능, 수정 버전은 문서 오탈자 같은 작은 정정에 쓰고, MQTT 토픽 경로(interfaceName/majorVersion/manufacturer/serialNumber/topic)에 주 버전을 넣으며, 변경 제안은 공식 GitHub 저장소로 받는다(2026-09-30 확인). [사실][^ref-031]

Kubernetes API 폐기 정책은 API 요소를 API 그룹 버전을 올려야만 제거할 수 있게 하고, 버전 간 왕복 변환에서 정보가 보존되어야 하며, 정식(GA) API는 주 버전 안에서 제거하지 않고 베타는 폐기 공지 뒤 9개월 또는 3개 부 릴리스 동안 유지한다. [사실][^ref-1349] 폐기된 API를 호출하면 경고 헤더·감사 주석·지표가 남는다(2026-09-30 확인). [사실][^ref-1349]

### 서비스 수준 약속과 감사 이력

ISO/IEC 19086-1:2016(2016-09-21, 1판)은 클라우드 SLA의 공통 구성 요소를 정하지만 모든 서비스에 쓰는 표준 SLA 구조나 서비스 수준 목표 세트는 정하지 않는다. [사실][^ref-1351] EU AI법 제26조는 고위험 AI 시스템 배포자가 자기 통제 아래 있는 자동 생성 로그를 최소 6개월 보관하고, 제공자 지침에 따라 운영을 감시하다가 위험이 의심되면 제공자 등에 알리고 사용을 멈추며, 중대한 사고는 즉시 제공자에게 먼저 알리게 한다. [사실][^ref-1357]

감사 이력의 참고 사례로, 미국 21 CFR 11.10(e)는 FDA 규제 대상 폐쇄형 전자기록 시스템에 전자기록을 만들거나 고치거나 지우는 운영자 입력과 행위의 날짜·시각을 독립적으로 기록하는, 보안이 적용된 컴퓨터 생성 타임스탬프 감사 추적을 쓰도록 요구한다. [사실][^ref-1353]

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
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30 (원문 미열람)
[^ref-1345]: European Commission (Shaping Europe's digital future), Data Act explained, 2025-12-15, https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained, 접근일 2026-09-30
[^ref-1346]: European Commission (Shaping Europe's digital future), Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts, 2025-11-19, https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding, 접근일 2026-09-30
[^ref-1347]: 지디넷코리아, 산업데이터 만든 자에게 사용·수익권 부여, 2022-03-15, https://zdnet.co.kr/view/?no=20220315103750, 접근일 2026-09-30
[^ref-1348]: 산업통상부 (공공데이터포털), 산업통상부_산업데이터 계약 가이드라인_20230109, 2023-04-05, https://www.data.go.kr/data/15113186/fileData.do, 접근일 2026-09-30
[^ref-1349]: The Kubernetes Authors, Kubernetes Deprecation Policy, 미확인, https://kubernetes.io/docs/reference/using-api/deprecation-policy/, 접근일 2026-09-30
[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)
[^ref-1351]: IEC / ISO (ISO/IEC JTC 1), ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts, 2016-09-21, https://webstore.iec.ch/en/publication/25920, 접근일 2026-09-30 (원문 미열람)
[^ref-1352]: IEC (BSI Knowledge 게재), IEC 62443-2-4:2023 Security for industrial automation and control systems - Security program requirements for IACS service providers, 2023-12-15, https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1, 접근일 2026-09-30 (원문 미열람)
[^ref-1353]: U.S. Food and Drug Administration 규정 (Cornell Law School LII 게재), 21 CFR § 11.10 - Controls for closed systems, 미확인, https://www.law.cornell.edu/cfr/text/21/11.10, 접근일 2026-09-30
[^ref-317]: 전기신문 (안상민), 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인, 2023-05-17, https://www.electimes.com/news/articleView.html?idxno=320147, 접근일 2026-09-30
[^ref-1356]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 25: Responsibilities Along the AI Value Chain | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/25/, 접근일 2026-09-30
[^ref-1357]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 26: Obligations of Deployers of High-Risk AI Systems | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/26/, 접근일 2026-09-30
[^ref-1359]: European Agency for Safety and Health at Work (EU-OSHA), Regulation 2023/1230/EU - machinery, 미확인, https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-22 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-22 | 58. 다사업자 책임·계약·데이터 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-22/pages/topics/2026/2026-09-30-area58-s11.md

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
created: 2026-09-30
updated: 2026-09-30
sources: [ref-555, ref-1357]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#11
---

[홈](../../index.md) › [주제](../index.md) › 58. 다사업자 책임·계약·데이터 — 열린 질문

# 58. 다사업자 책임·계약·데이터 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에 걸린 기존 열린 질문 8건은 모두 열려 있고, 이번 실행에서 새 질문 5건을 올렸다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에 걸린 기존 열린 질문 8건은 모두 열려 있고, 이번 실행에서 새 질문 5건을 올렸다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-145** (상태: 열림) 언어 모델 게이트웨이의 모델 대체·라우팅 희석을 ROP 운영에서 탐지·기록하고 계약으로 막는 실무 절차나 사례가 있는가?
- **oq-149** (상태: 열림) 싱가포르 공공 의료의 RoMi-H 등재 프로그램처럼 벤더·통합사를 사전 평가해 등록 자격을 주는 관문을 국내 병원·공공 현장에서 운용한 사례나 제도가 있는가?
- **oq-185** (상태: 열림) 소유자가 원격 조작자를 예약해 가정 로봇을 안내하게 하는 방식(1X NEO 등)에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가?
- **oq-241** (상태: 열림) 로봇 오케스트레이션 도입 계약에서 운영자·통합자·로봇 제조사·플랫폼 사업자 사이의 운영 책임을 나누는 책임 분담표나 표준 계약 조항을 공개한 사례가 있는가? 이번 조사에서도 공개 사례를 찾지 못했고, 3절의 추정이 부분 근거다.
- **oq-249** (상태: 열림) EU 기계류 규정의 개입 증거 기록·안전 소프트웨어 추적 로그 요구가 개별 기계 밖에서 여러 로봇을 지시하는 오케스트레이션 플랫폼에도 미치는가, 미친다면 기록 책임은 누구에게 있는가? 이번에 확인한 EU 기계류 규정과 EU AI법 조항은 개별 기계·AI 시스템 쪽 의무만 보여, 플랫폼에 미치는지는 아직 풀리지 않았다. [추정][^ref-555][^ref-1357]
- **oq-259** (상태: 열림) 여러 제조사 로봇의 영상과 위치 정보를 모아 관제하는 플랫폼 사업자는 개인정보 보호법상 이동형 영상정보처리기기 운영자인가, 현장 운영 사업자의 수탁자인가, 그리고 촬영 표시·거부 의사 처리 의무는 누구에게 있는가?
- **oq-265** (상태: 열림) ANSI/A3 R15.08-3-2026 이 사용자에게 요구하는 운영 절차·교육·변경 관리 항목은 무엇이며, 여러 제조사 로봇을 함께 쓰는 현장에서 누가 이를 이행하는가?
- **oq-268** (상태: 열림) 사용량 기반 서비스형 로봇 계약에서 과금·최소 요금·가동률 미달을 판정하는 계량 데이터를 누가 측정하고, 여러 사업자가 함께 쓰는 현장에서 그 값을 어떻게 합의하는가?
- (새 질문 · 제기 2026-09-30 · 실행 2026-09-30-22) 여러 제조사 로봇의 운영 데이터를 모으는 오케스트레이션 플랫폼 사업자는 EU 데이터법상 데이터 보유자인가, 사용자가 지정한 제3자 데이터 수령자인가, 그리고 그에 따라 제조사에게 데이터 제공을 요구할 수 있는 범위는 어디까지인가?
- (새 질문 · 제기 2026-09-30 · 실행 2026-09-30-22) 로봇 제조사·관제 API 의 주 버전 변경이나 폐기를 오케스트레이션 플랫폼에 사전 통지하는 기간과 유예 기간을 계약이나 인터페이스 표준에 명시한 공개 사례가 있는가?
- (새 질문 · 제기 2026-09-30 · 실행 2026-09-30-22) 국내 산업데이터 계약 가이드라인의 표준계약서와 업종별 사례가 로봇 운영 데이터(지도·작업 이력·센서 로그)처럼 여러 사업자가 함께 만드는 데이터를 어떻게 다루는가?
- (새 질문 · 제기 2026-09-30 · 실행 2026-09-30-22) 오케스트레이션 플랫폼에서 경로망·속도 제한·작업 규칙 같은 설정을 바꾸는 일이 EU 기계류 규정의 실질적 변경에 해당해 플랫폼 운영자나 통합자가 제조자 의무를 지는 경우가 있는가?
- (새 질문 · 제기 2026-09-30 · 실행 2026-09-30-22) 로봇-승강기 연동 표준 과제의 결과물(표준 번호, 연동 장애 시 승강기 제조사·로봇 제조사·관제 사업자의 책임 분담)이 공개되었는가?

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

[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)
[^ref-1357]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 26: Obligations of Deployers of High-Risk AI Systems | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/26/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-22 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-22 | 58. 다사업자 책임·계약·데이터 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-22/pages/topics/2026/2026-09-30-area58-s7.md

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
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1345, ref-1346, ref-1347, ref-1348, ref-1349, ref-555, ref-1351, ref-1352, ref-1353, ref-1356, ref-1357, ref-1359]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#7
---

[홈](../../index.md) › [주제](../index.md) › 58. 다사업자 책임·계약·데이터 — 관련 표준·프레임워크·오픈소스

# 58. 다사업자 책임·계약·데이터 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에 걸리는 규칙은 데이터 권리(EU 데이터법·국내 산업 디지털 전환 촉진법), 인터페이스 변경(VDA 5050·Kubernetes 폐기 정책), 서비스 수준·보안·기록(ISO/IEC 19086-1·IEC 62443-2-4·21 CFR Part 11), 변경 주체 책임(EU 기계류 규정·EU AI법)으로 나뉜다.
- 이 페이지는 [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에 걸리는 규칙은 데이터 권리(EU 데이터법·국내 산업 디지털 전환 촉진법), 인터페이스 변경(VDA 5050·Kubernetes 폐기 정책), 서비스 수준·보안·기록(ISO/IEC 19086-1·IEC 62443-2-4·21 CFR Part 11), 변경 주체 책임(EU 기계류 규정·EU AI법)으로 나뉜다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| EU 데이터법(Regulation (EU) 2023/2854) | 프레임워크 | 연결 제품 데이터의 사용자 접근·제3자 공유, 데이터 보유자 계약, 기업 간 불공정 조항 무효(2025-09-12 적용) | [사실][^ref-1345] |
| 데이터법 모델 계약 조항·클라우드 표준 계약 조항(권고 초안, 2025-11-19) | 프레임워크 | 데이터 접근·이용 계약 문안 네 벌과 클라우드 계약 조항 여섯 개, 구속력 없음 | [사실][^ref-1346] |
| 산업 디지털 전환 촉진법(2022-07 시행) | 프레임워크 | 산업데이터 사용·수익권, 계약 체결 권고, 정부 계약 지침 | [사실][^ref-1347] |
| 산업데이터 계약 가이드라인(산업통상부) | 프레임워크 | 산업데이터 거래 유의사항·표준계약서·업종별 사례(본문 미열람) | [사실][^ref-1348] |
| VDA 5050 3.0.0 버전 규칙 | 표준 | 의미적 버전, 토픽 경로의 주 버전, GitHub 변경 제안 | [사실][^ref-031] |
| Kubernetes API 폐기 정책 | 오픈소스 | 버전 증가로만 제거, 안정도별 유지 기간, 폐기 API 사용 경고·감사 주석·지표 | [사실][^ref-1349] |
| ISO/IEC 19086-1:2016 | 표준 | 클라우드 SLA 공통 구성 요소·개념·용어, 표준 SLA 구조는 정하지 않음(원문 미열람) | [사실][^ref-1351] |
| IEC 62443-2-4:2023 | 표준 | IACS 서비스 제공자의 통합·유지보수 보안 프로세스 요구(원문 미열람) | [사실][^ref-1352] |
| EU 기계류 규정(Regulation (EU) 2023/1230) | 프레임워크 | 실질적 변경을 한 자를 제조자로 봄(2027-01-20 적용) | [사실][^ref-555][^ref-1359] |
| EU AI법 제25조·제26조 | 프레임워크 | AI 가치사슬 책임 이전과 서면 계약, 배포자 로그 최소 6개월 보관 | [사실][^ref-1356][^ref-1357] |
| 21 CFR Part 11(§11.10) | 프레임워크 | FDA 규제 대상 전자기록에 적용되는 규정으로, 감사 추적 요구의 참고 사례 | [사실][^ref-1353] |

EU AI법 조문은 비공식 게재본으로 확인했고, EU 기계류 규정의 실질적 변경 규정은 EUR-Lex 본문을 열지 못해 검색 요약 범위에서 확인했다. 표준·프레임워크 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

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
[^ref-1345]: European Commission (Shaping Europe's digital future), Data Act explained, 2025-12-15, https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained, 접근일 2026-09-30
[^ref-1346]: European Commission (Shaping Europe's digital future), Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts, 2025-11-19, https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding, 접근일 2026-09-30
[^ref-1347]: 지디넷코리아, 산업데이터 만든 자에게 사용·수익권 부여, 2022-03-15, https://zdnet.co.kr/view/?no=20220315103750, 접근일 2026-09-30
[^ref-1348]: 산업통상부 (공공데이터포털), 산업통상부_산업데이터 계약 가이드라인_20230109, 2023-04-05, https://www.data.go.kr/data/15113186/fileData.do, 접근일 2026-09-30
[^ref-1349]: The Kubernetes Authors, Kubernetes Deprecation Policy, 미확인, https://kubernetes.io/docs/reference/using-api/deprecation-policy/, 접근일 2026-09-30
[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)
[^ref-1351]: IEC / ISO (ISO/IEC JTC 1), ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts, 2016-09-21, https://webstore.iec.ch/en/publication/25920, 접근일 2026-09-30 (원문 미열람)
[^ref-1352]: IEC (BSI Knowledge 게재), IEC 62443-2-4:2023 Security for industrial automation and control systems - Security program requirements for IACS service providers, 2023-12-15, https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1, 접근일 2026-09-30 (원문 미열람)
[^ref-1353]: U.S. Food and Drug Administration 규정 (Cornell Law School LII 게재), 21 CFR § 11.10 - Controls for closed systems, 미확인, https://www.law.cornell.edu/cfr/text/21/11.10, 접근일 2026-09-30
[^ref-1356]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 25: Responsibilities Along the AI Value Chain | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/25/, 접근일 2026-09-30
[^ref-1357]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 26: Obligations of Deployers of High-Risk AI Systems | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/26/, 접근일 2026-09-30
[^ref-1359]: European Agency for Safety and Health at Work (EU-OSHA), Regulation 2023/1230/EU - machinery, 미확인, https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-22 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-22 | 58. 다사업자 책임·계약·데이터 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-22/pages/topics/2026/2026-09-30-area58-s10.md

```markdown
---
title: "58. 다사업자 책임·계약·데이터 — 다른 연구영역과의 연결"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 58
related_areas: [2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-872, ref-1345, ref-1346, ref-1349, ref-555, ref-1352, ref-1353, ref-317, ref-1355, ref-1356, ref-1357, ref-1358]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#10
---

[홈](../../index.md) › [주제](../index.md) › 58. 다사업자 책임·계약·데이터 — 다른 연구영역과의 연결

# 58. 다사업자 책임·계약·데이터 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 인터페이스 버전 규칙, 설비 연동, 감사 이력, 데이터 권리, 규제 책임, 조달, AI 가치사슬 책임, 적용 현장을 통해 열네 개 세부영역과 이어지는 것으로 보인다. [추정][^ref-031][^ref-1357][^ref-1345][^ref-1356]
- 이 페이지는 [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 인터페이스 버전 규칙, 설비 연동, 감사 이력, 데이터 권리, 규제 책임, 조달, AI 가치사슬 책임, 적용 현장을 통해 열네 개 세부영역과 이어지는 것으로 보인다. [추정][^ref-031][^ref-1357][^ref-1345][^ref-1356]

- [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) — 도입 전에 운영자·통합자·제조사·플랫폼 사업자의 책임 범위를 합의하는 일로 이어지며, 책임 분담표 공개 사례는 아직 찾지 못했다([oq-241](../../open-questions.md)). [추정][^ref-1346][^ref-872]
- [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) — 통합자 사전 등재 같은 조달·계약 장치가 연동 책임 주체를 정한다. [추정][^ref-872]
- [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) — AI 공급자와 필요한 정보·기술적 접근을 서면 계약으로 정하는 AI 가치사슬 책임이 대화형 기능의 신뢰 기반과 겹친다([oq-145](../../open-questions.md)). [추정][^ref-1356]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 제조사 인터페이스의 주 버전 변경과 폐기 일정이 연동 유지 책임으로 이어진다. [추정][^ref-031][^ref-1349]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — VDA 5050의 의미적 버전 규칙과 토픽 경로의 주 버전 표기가 인터페이스 변경 규칙의 기준이 된다. [추정][^ref-031]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 로봇–승강기 API 연동 표준 과제가 있었으나 연동 장애 때 책임 분담은 확인되지 않았다. [추정][^ref-317]
- [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) — 누가 언제 어떤 명령·변경을 했는지 남기는 감사 이력과 로그 보관이 실행 기록과 겹친다. [추정][^ref-1353][^ref-1357]
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — AI 시스템을 실질적으로 바꾸거나 용도를 바꾼 자가 제공자 의무를 지는 규정이 모델 교체·운영과 이어진다. [추정][^ref-1356]
- [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) — 서비스 제공자 보안 요구(IEC 62443-2-4)와 감사 추적 요구가 보안 감사와 이어진다. [추정][^ref-1352][^ref-1353]
- [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) — 데이터 권리 계약과 공동주택 로봇 법안의 개인정보 처리 조항이 이어진다([oq-259](../../open-questions.md)). [추정][^ref-1345][^ref-1358]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — API 폐기 정책과 변경 관리가 소프트웨어 수명주기와 이어진다. [추정][^ref-1349]
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — 변경 주체 책임 규정과 책임 배분 제안의 법적 판정·보험은 이 영역이 다룬다. [추정][^ref-555][^ref-1356][^ref-1355]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 싱가포르 공공 의료의 통합자 등재가 병원 현장의 다사업자 책임 사례다. [추정][^ref-872]
- [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) — 공동주택 관리주체의 책임 범위 논의가 가정 현장의 다사업자 책임 사례다. [추정][^ref-1358]

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
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30 (원문 미열람)
[^ref-1345]: European Commission (Shaping Europe's digital future), Data Act explained, 2025-12-15, https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained, 접근일 2026-09-30
[^ref-1346]: European Commission (Shaping Europe's digital future), Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts, 2025-11-19, https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding, 접근일 2026-09-30
[^ref-1349]: The Kubernetes Authors, Kubernetes Deprecation Policy, 미확인, https://kubernetes.io/docs/reference/using-api/deprecation-policy/, 접근일 2026-09-30
[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)
[^ref-1352]: IEC (BSI Knowledge 게재), IEC 62443-2-4:2023 Security for industrial automation and control systems - Security program requirements for IACS service providers, 2023-12-15, https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1, 접근일 2026-09-30 (원문 미열람)
[^ref-1353]: U.S. Food and Drug Administration 규정 (Cornell Law School LII 게재), 21 CFR § 11.10 - Controls for closed systems, 미확인, https://www.law.cornell.edu/cfr/text/21/11.10, 접근일 2026-09-30
[^ref-317]: 전기신문 (안상민), 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인, 2023-05-17, https://www.electimes.com/news/articleView.html?idxno=320147, 접근일 2026-09-30
[^ref-1355]: Shaik, A. S. (SSRN), Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong?, 2026-05-01, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6737139, 접근일 2026-09-30 (원문 미열람)
[^ref-1356]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 25: Responsibilities Along the AI Value Chain | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/25/, 접근일 2026-09-30
[^ref-1357]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 26: Obligations of Deployers of High-Risk AI Systems | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/26/, 접근일 2026-09-30
[^ref-1358]: 한국아파트신문 (사설), 공동주택에 밀려오는 로봇, 또 다른 관리책임은 없을까, 2026-09-14, https://www.hapt.co.kr/news/articleView.html?idxno=169488, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-22 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-22 | 58. 다사업자 책임·계약·데이터 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-22/pages/topics/2026/2026-09-30-area58-s4.md

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
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1345, ref-1346, ref-1347, ref-1349, ref-555, ref-1351, ref-1353, ref-1356]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#4
---

[홈](../../index.md) › [주제](../index.md) › 58. 다사업자 책임·계약·데이터 — 핵심 개념과 용어

# 58. 다사업자 책임·계약·데이터 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 용어는 책임이 넘어가는 조건, 데이터 권리, 인터페이스 변경 예고, 서비스 약속과 기록의 네 묶음으로 나뉜다.
- 이 페이지는 [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 용어는 책임이 넘어가는 조건, 데이터 권리, 인터페이스 변경 예고, 서비스 약속과 기록의 네 묶음으로 나뉜다.

- **실질적 변경(Substantial Modification)** — EU 기계류 규정에서 새로운 위험을 만들거나 기존 위험을 키워 새로운 중요한 보호 조치가 필요한 변경을 말하며, 이런 변경을 한 자는 제조자로 본다. [사실][^ref-555] EU AI법도 고위험 AI 시스템에 실질적 변경을 한 자를 제공자로 본다. [사실][^ref-1356]
- **데이터 보유자(Data Holder)** — EU 데이터법에서 연결 제품(IoT 기기) 데이터를 가진 제조사·서비스 제공자 같은 자로, 사용자와 계약을 맺어야 하고 사용자 동의 없이 비개인 데이터를 이용할 수 없다. [사실][^ref-1345]
- **모델 계약 조항(Model Contractual Terms, MCT)** — 유럽연합 집행위원회가 데이터법 이행을 돕도록 권고 초안(2025-11-19)으로 낸 구속력 없는 계약 문안이다. [사실][^ref-1346]
- **산업데이터 사용·수익권** — 한국 산업 디지털 전환 촉진법(2022-07 시행)이 산업데이터 생성에 투자한 자에게 인정하는 권리다([산업데이터](../../glossary/industrial-data.md)). [사실][^ref-1347]
- **[의미적 버전 관리](../../glossary/semantic-versioning.md)(Semantic Versioning)** — VDA 5050 3.0.0은 주.부.수정 번호로 변경의 성격을 알리며, 주 버전은 대개(typically) 호환을 깨는 변경에 쓴다. [사실][^ref-031]
- **API 폐기 정책(API Deprecation Policy)** — API 요소를 언제, 어떤 공지와 유예 기간을 거쳐 없앨지 미리 정한 규칙으로, Kubernetes 폐기 정책이 한 예다. [사실][^ref-1349]
- **[서비스 수준 협약](../../glossary/service-level-agreement.md)(Service Level Agreement, SLA)** — ISO/IEC 19086-1:2016은 클라우드 SLA의 공통 구성 요소(개요, 클라우드 서비스 계약과 SLA의 관계, 개념, 용어)를 정한다. [사실][^ref-1351]
- **[감사 추적](../../glossary/audit-trail.md)(Audit Trail)** — 전자기록을 만들거나 고치거나 지운 운영자 입력과 행위의 날짜·시각을 독립적으로 남기는 기록이다. [사실][^ref-1353]

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
[^ref-1345]: European Commission (Shaping Europe's digital future), Data Act explained, 2025-12-15, https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained, 접근일 2026-09-30
[^ref-1346]: European Commission (Shaping Europe's digital future), Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts, 2025-11-19, https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding, 접근일 2026-09-30
[^ref-1347]: 지디넷코리아, 산업데이터 만든 자에게 사용·수익권 부여, 2022-03-15, https://zdnet.co.kr/view/?no=20220315103750, 접근일 2026-09-30
[^ref-1349]: The Kubernetes Authors, Kubernetes Deprecation Policy, 미확인, https://kubernetes.io/docs/reference/using-api/deprecation-policy/, 접근일 2026-09-30
[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)
[^ref-1351]: IEC / ISO (ISO/IEC JTC 1), ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts, 2016-09-21, https://webstore.iec.ch/en/publication/25920, 접근일 2026-09-30 (원문 미열람)
[^ref-1353]: U.S. Food and Drug Administration 규정 (Cornell Law School LII 게재), 21 CFR § 11.10 - Controls for closed systems, 미확인, https://www.law.cornell.edu/cfr/text/21/11.10, 접근일 2026-09-30
[^ref-1356]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 25: Responsibilities Along the AI Value Chain | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/25/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-22 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-22 | 58. 다사업자 책임·계약·데이터 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-22/pages/topics/2026/2026-09-30-area58-s3.md

```markdown
---
title: "58. 다사업자 책임·계약·데이터 — 왜 중요한가"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 58
related_areas: [2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-872, ref-1345, ref-1346, ref-1349, ref-555, ref-1351, ref-1352, ref-1355, ref-1356, ref-1358]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#3
---

[홈](../../index.md) › [주제](../index.md) › 58. 다사업자 책임·계약·데이터 — 왜 중요한가

# 58. 다사업자 책임·계약·데이터 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 여러 사업자가 함께 운영하는 현장에서 연동 오류를 누가 고치고 변경을 누가 승인하는지를 한 번에 정한 공개 표준이나 책임 분담표는 이번 조사(2026-09-30 기준)에서 찾지 못했고, 실제 규칙은 변경한 주체에게 제조자·제공자 의무를 지우는 법 규정, 인터페이스 표준의 버전·폐기 규칙, 서비스 수준 협약·표준 계약 조항과 통합자 사전 자격 같은 계약·조달 장치가 겹쳐 정해지는 것으로 보인다. [추정][^ref-555][^ref-1356][^ref-031][^ref-1349][^ref-1351][^ref-1346][^ref-1352][^ref-872]
- 이 페이지는 [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

여러 사업자가 함께 운영하는 현장에서 연동 오류를 누가 고치고 변경을 누가 승인하는지를 한 번에 정한 공개 표준이나 책임 분담표는 이번 조사(2026-09-30 기준)에서 찾지 못했고, 실제 규칙은 변경한 주체에게 제조자·제공자 의무를 지우는 법 규정, 인터페이스 표준의 버전·폐기 규칙, 서비스 수준 협약·표준 계약 조항과 통합자 사전 자격 같은 계약·조달 장치가 겹쳐 정해지는 것으로 보인다. [추정][^ref-555][^ref-1356][^ref-031][^ref-1349][^ref-1351][^ref-1346][^ref-1352][^ref-872]

책임 범위가 흐릿한 채 로봇을 들이는 데 대한 우려도 있다. 한국아파트신문 사설(2026-09-14)은 공동주택에 로봇·AI·통신망·관제시스템이 더해지면 관리사무소장 등 관리주체의 관리 영역과 책임이 오히려 넓어질 수 있으므로, 도입 전에 책임 범위를 명확히 하고 법제도를 정비해야 한다는 의견을 냈다. [의견][^ref-1358] Shaik(SSRN, 2026, 동료심사 전 원고)의 제안은 자율 산업 시스템의 책임을 로봇 제조사·시스템 통합자·AI 공급자·운영자 사이에 나누는 틀을 세우고, 이를 상업 계약과 기존 보험으로 구현할 수 있다는 것이다(8절). [의견][^ref-1355]

데이터 권리 쪽에서는 EU 데이터법이 2025-09-12부터 적용되어, 연결 제품 사용자가 제품 사용으로 함께 만든 데이터에 접근·이용·이전할 수 있게 하고 제조사·서비스 제공자 같은 데이터 보유자가 사용자와 계약을 맺게 한다. [사실][^ref-1345]

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
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30 (원문 미열람)
[^ref-1345]: European Commission (Shaping Europe's digital future), Data Act explained, 2025-12-15, https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained, 접근일 2026-09-30
[^ref-1346]: European Commission (Shaping Europe's digital future), Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts, 2025-11-19, https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding, 접근일 2026-09-30
[^ref-1349]: The Kubernetes Authors, Kubernetes Deprecation Policy, 미확인, https://kubernetes.io/docs/reference/using-api/deprecation-policy/, 접근일 2026-09-30
[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)
[^ref-1351]: IEC / ISO (ISO/IEC JTC 1), ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts, 2016-09-21, https://webstore.iec.ch/en/publication/25920, 접근일 2026-09-30 (원문 미열람)
[^ref-1352]: IEC (BSI Knowledge 게재), IEC 62443-2-4:2023 Security for industrial automation and control systems - Security program requirements for IACS service providers, 2023-12-15, https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1, 접근일 2026-09-30 (원문 미열람)
[^ref-1355]: Shaik, A. S. (SSRN), Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong?, 2026-05-01, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6737139, 접근일 2026-09-30 (원문 미열람)
[^ref-1356]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 25: Responsibilities Along the AI Value Chain | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/25/, 접근일 2026-09-30
[^ref-1358]: 한국아파트신문 (사설), 공동주택에 밀려오는 로봇, 또 다른 관리책임은 없을까, 2026-09-14, https://www.hapt.co.kr/news/articleView.html?idxno=169488, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-22 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-22 | 58. 다사업자 책임·계약·데이터 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1199건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 335개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- life-cycle-costing: 수명주기 비용 분석 (Life Cycle Costing (LCC, IEC 60300-3-3))
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
- role-ambiguity: 역할 모호성 (Role Ambiguity)
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
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- social-force-model: 사회적 힘 모델 (Social Force Model)
- social-robot-navigation: 사회적 내비게이션 (Social Robot Navigation (Human-aware Navigation))
- soft-landings: 소프트 랜딩 (Soft Landings (BSRIA BG 54))
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
- total-cost-of-ownership: 총소유비용 (Total Cost of Ownership (TCO))
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

### docs/open-questions.md (요약: 대상 영역 [58] 에 걸린 8건 / 전체 278건)

```markdown
- oq-145 [열림] 언어 모델 게이트웨이의 모델 대체·라우팅 희석을 ROP 운영에서 탐지·기록하고 계약으로 막는 실무 절차나 사례가 있는가? (영역 13, 57, 58)
- oq-149 [열림] 싱가포르 공공 의료의 RoMi-H 등재 프로그램처럼 벤더·통합사를 사전 평가해 등록 자격을 주는 관문을 국내 병원·공공 현장에서 운용한 사례나 제도가 있는가? (영역 4, 63, 58)
- oq-185 [열림] 소유자가 원격 조작자를 예약해 가정 로봇을 안내하게 하는 방식(1X NEO 등)에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가? (영역 65, 53, 58)
- oq-241 [열림] 로봇 오케스트레이션 도입 계약에서 운영자·통합자·로봇 제조사·플랫폼 사업자 사이의 운영 책임을 나누는 책임 분담표나 표준 계약 조항을 공개한 사례가 있는가? (영역 2, 58)
- oq-249 [열림] EU 기계류 규정의 개입 증거 기록·안전 소프트웨어 추적 로그 요구가 개별 기계 밖에서 여러 로봇을 지시하는 오케스트레이션 플랫폼에도 미치는가, 미친다면 기록 책임은 누구에게 있는가? (영역 52, 59, 58)
- oq-259 [열림] 여러 제조사 로봇의 영상과 위치 정보를 모아 관제하는 플랫폼 사업자는 개인정보 보호법상 이동형 영상정보처리기기 운영자인가, 현장 운영 사업자의 수탁자인가, 그리고 촬영 표시·거부 의사 처리 의무는 누구에게 있는가? (영역 53, 58)
- oq-265 [열림] ANSI/A3 R15.08-3-2026 이 사용자에게 요구하는 운영 절차·교육·변경 관리 항목은 무엇이며, 여러 제조사 로봇을 함께 쓰는 현장에서 누가 이를 이행하는가? (영역 40, 50, 58)
- oq-268 [열림] 사용량 기반 서비스형 로봇 계약에서 과금·최소 요금·가동률 미달을 판정하는 계량 데이터를 누가 측정하고, 여러 사업자가 함께 쓰는 현장에서 그 값을 어떻게 합의하는가? (영역 3, 58, 39)
```
