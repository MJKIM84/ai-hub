(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-23
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 59. 법·규제·보험·라이선스 (P. 거버넌스·법규·사회)
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

### runs/2026-09-30-23/target.json

```json
{
  "run_id": "2026-09-30-23",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 132,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 59,
    "area_name": "59. 법·규제·보험·라이선스",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=59"
}
```

### runs/2026-09-30-23/research.json

```json
{
  "run_id": "2026-09-30-23",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 59,
    "area_name": "59. 법·규제·보험·라이선스",
    "category": "P. 거버넌스·법규·사회"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 운행안전인증, 운용자, 책임보험·공제, 제조물(소프트웨어 포함 여부), 사이버복원력법 보고 의무, SBOM·SPDX, 패키지 라이선스 선언 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 실외(한국 보도 통행 로봇, 미국 주법 개인 배송 장치)·산업 사업장(산업용 로봇 안전검사) 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 인증·보험 조건의 운영 제약 반영, 사고·취약점 보고 체계, 라이선스 선언·SBOM 관리 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 지능형로봇법·도로교통법, 산업안전보건법 안전검사, EU 기계류 규정, EU 제조물책임지침, 한국 제조물책임법, 인공지능 기본법, EU 사이버복원력법, 개인정보보호법 제25조의2, ROS 2 REP 2004, SPDX(ISO/IEC 5962) 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-143, oq-173, oq-186, oq-187, oq-231, oq-239, oq-249, oq-250, oq-262 반영 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가? [분류원문]",
    "실외에서 로봇을 운행할 때 한국(지능형로봇법·도로교통법의 운행안전인증·운용자 의무·보험)과 해외(미국 주법의 개인 배송 장치)는 무엇을 요구하며, 운행안전인증의 심사항목과 인증 대상은 어떻게 정해져 있는가? (섹션 5·7 겨냥, oq-186·oq-187 관련, 한국 자료 우선)",
    "로봇 사고의 책임을 정하는 제조물 책임 법제는 소프트웨어·AI를 어떻게 다루는가(EU 개정 제조물책임지침, 한국 제조물책임법)? (섹션 4·6·7 겨냥)",
    "AI 규제와 사이버보안 규제(한국 인공지능 기본법, EU 사이버복원력법)는 로봇 운영 사업자에게 어떤 의무와 시행 일정을 두는가? (섹션 7 겨냥, oq-143 관련)",
    "산업 사업장에서 로봇을 쓸 때 적용되는 기계·안전 규제(산업안전보건법 안전검사, EU 기계류 규정)는 무엇인가? (섹션 5·7 겨냥)",
    "오픈소스·SDK·3D 자산의 라이선스를 지키기 위한 선언·목록화 수단(ROS 2 패키지 라이선스 규칙, SPDX·SBOM, 시뮬레이션 모델 데이터베이스의 라이선스 표기)은 무엇인가? (섹션 6·7 겨냥)",
    "법·규제·보험·라이선스에서 ROP가 직접 맡을 것과 제조사·운영자·보험사·법무에 맡길 것의 경계는 어디이며 어느 영역(개인정보 법 포함, oq-262 관련)과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "한국에서는 개정 지능형로봇법과 도로교통법이 2023-11-17부터 시행되어, 운행안전인증을 받은 질량 500kg 이하·최고속도 15km/h 이하의 실외이동로봇이 보행자 지위로 보도를 통행할 수 있게 되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-991",
        "ref-980"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "정책브리핑(산업통상자원부·경찰청, 2023-11-16): 2023-11-17 시행, 대상 질량 500kg 이하·15km/h 이하, 16가지 시험항목. 한국로봇산업진흥원 인증 안내도 최대 속도 15km/h 이하·최대 질량 500kg 이하를 대상 요건으로 둔다.",
      "as_of": "2023-11-16",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f2",
      "claim": "개정 도로교통법은 실외이동로봇을 조작·관리하는 운용자에게 정확한 조작과 안전한 운용 의무를 두고, 로봇도 신호위반·무단횡단 금지 같은 보행자 교통규칙을 지키게 하며, 안전운용의무 위반에는 범칙금(3만원)을 부과할 수 있게 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-991"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "운용자에게 로봇에 대한 정확한 조작 및 안전한 운용 의무를 부과하고, 신호위반·무단횡단 금지 등 도로교통법을 준수해야 하며 위반 시 범칙금 3만 원 등이 부과된다(2023-11-16 정책브리핑).",
      "as_of": "2023-11-16",
      "site_type": "실외",
      "flow_item": "수행 자원"
    },
    {
      "id": "f3",
      "claim": "한국에서 운행안전인증을 받은 실외이동로봇을 보도에서 운영하는 자는 인적·물적 손해 배상을 위한 보험 또는 공제에 가입해야 하며, 정부는 한국로봇산업협회를 손해보장사업 실시기관으로 지정했다.",
      "tag": "사실",
      "source_ids": [
        "ref-991",
        "ref-1240"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "정책브리핑: 보도 운영자에게 \"보험 또는 공제 가입 의무를 부과\", 한국로봇산업협회를 손해보장사업 실시기관으로 지정. 지디넷코리아(2024-02-08)도 실외 이동로봇 운영 주체의 의무 가입 보험으로 보도.",
      "as_of": "2023-11-16",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f4",
      "claim": "실외 사례(한국): 한국로봇산업협회는 2024-02 실외이동로봇 손해배상책임 단체보험을 내놓아 로봇 1대당 약 500만원 수준이던 보험료를 30만원대로 낮췄다고 밝혔고, 첫 가입 기업은 뉴빌리티·로보티즈였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1240"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기사 보도: 협회가 민관 협력으로 단체보험을 출시, 기존 대당 약 500만원에서 약 30만원대로 94% 인하, 첫 가입 기업 뉴빌리티·로보티즈(2024-02-08). 보장 한도는 기사에 없음.",
      "as_of": "2024-02-08",
      "site_type": "실외",
      "flow_item": "예외·성과"
    },
    {
      "id": "f5",
      "claim": "한국로봇산업진흥원 안내에 따르면 실외이동로봇 운행안전인증은 지능형로봇법 제40조의2에 근거하며, 인증 대상은 실외이동로봇과 그 운행에 필요한 관제장치 조합의 일체이고, 현재 심사항목은 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치의 8개다.",
      "tag": "사실",
      "source_ids": [
        "ref-980"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "인증 대상은 \"실외이동로봇과 그 운행에 필요한 관제장치 조합의 일체\". 심사항목 8개, 절차는 서류심사→제품심사→인증표시, 처리기간 신청일부터 30일 이내. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": "수행 자원"
    },
    {
      "id": "f6",
      "claim": "2023-07 한국로봇산업진흥원이 행정예고한 실외이동로봇 운행 안전기준은 16가지 항목으로, 질량별 속도 제한, 폭 80cm(보도 폭 250cm 이상이면 120cm), 5도 경사로 안정성, 비상정지, 장애물 회피, 횡단보도 신호 준수, 알림음 55~73dB, 등화장치 온도 60도 이하, 방수 IPX4 이상 등을 담았다.",
      "tag": "사실",
      "source_ids": [
        "ref-992"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기사 보도(2023-07-28): 16가지 안전기준, 의견 제출 마감 2023-08-28(국민참여입법센터). 항목 전체 목록은 기사에 없음.",
      "as_of": "2023-07-28",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f7",
      "claim": "f5와 f6을 비교하면 실외이동로봇 운행안전인증의 심사 체계가 제정 당시 16가지 안전기준에서 현재 8개 심사항목으로 재편된 것으로 보이나, 개정 시점·근거 고시와 알림음·등화장치·경사로 같은 기존 기준이 어느 항목에 흡수됐는지는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-980",
        "ref-992"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "인증기관 안내 페이지는 8개 항목을 나열하고(2026-09-30 확인), 2023-07 기사는 16가지 기준을 전한다. 개정 고시 원문은 열지 못함(oq-186 관련).",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f8",
      "claim": "실외 사례(미국): 버지니아주법 §46.2-908.1:1은 개인 배송 장치(PDD)가 보도·횡단보도에서 시속 10마일 이하로 운행하고 운영자를 식별하는 표시를 달게 하며, 운영자에게 장치 운행으로 생긴 손해에 대해 최소 10만 달러의 일반배상책임 보험을 유지하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1248"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "운영자는 \"general liability coverage of at least $100,000\"의 보험을 유지해야 하고, 보도·횡단보도 속도 10mph 이하, 운영자 식별 표시 필요. 지방정부는 추가 안전 요건을 둘 수 있음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f9",
      "claim": "EU 개정 제조물책임지침(Directive (EU) 2024/2853)은 2026-12-09 이후 시장에 출시되거나 사용이 개시된 제품에 적용되며, 독립형 소프트웨어·디지털 제조 파일·통합 디지털 요소를 제품에 포함하고, 출시 뒤 제품을 실질적으로 변경한 자를 제조자로 볼 수 있게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1235"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"will apply to products placed on the Union market or put into service after December 9, 2026\"; 제품 범위에 stand-alone software, digital manufacturing files, integrated digital elements 포함; 실질적 변경자는 제조자로 간주될 수 있음(Gibson Dunn, 2026-03-23).",
      "as_of": "2026-03-23",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f10",
      "claim": "같은 지침에서는 결함 있는 소프트웨어나 필요한 보안 업데이트 미제공도 책임 원인이 될 수 있고, 청구인이 그럴듯한 청구를 하면 피고에게 증거 공개를 명할 수 있으며, 공개 의무 불이행 등의 경우 결함이 추정된다.",
      "tag": "사실",
      "source_ids": [
        "ref-1235"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "책임은 결함 소프트웨어, 안전하지 않은 디지털 기능, 필요한 보안 업데이트 미제공에서 생길 수 있고, 피고의 증거 공개 의무와 반증 가능한 결함 추정이 처음 도입됐다(Gibson Dunn 요약).",
      "as_of": "2026-03-23",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f11",
      "claim": "한국 제조물책임법은 제조물을 제조되거나 가공된 동산으로 정의해 소프트웨어를 명시적으로 포함하지 않으므로, 사람의 개입 없이 동작한 자율 시스템 사고에서 소프트웨어 개발자가 제조물 책임을 지는지가 쟁점으로 남아 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1243"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "현행법은 제조물을 제조·가공된 동산으로 정의해 자율주행차 사고 같은 소프트웨어 기인 사고를 명확히 포섭하지 못하며, 무과실책임 적용 여부가 쟁점이라고 설명(김·장 법률사무소, 2024-07).",
      "as_of": "2024-07",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f12",
      "claim": "EU 기계류 규정(Regulation (EU) 2023/1230)은 2027-01-20부터 적용되며, 출시된 기계에 실질적 변경을 한 자를 제조자로 보아 제조자 의무를 지게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1212",
        "ref-555"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2023-06-14 채택, 2027-01-20 적용. 실질적 변경은 새 위험을 만들거나 기존 위험을 키워 새로운 중요한 보호 조치가 필요한 변경. (재인용: 2026-09-30-22)",
      "as_of": "2023-06-14",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "한국 인공지능 기본법은 2026-01-22 시행되었고, 정부는 최종 의사결정 권한을 사람이 가지는 경우 고영향 인공지능 분류에서 제외된다고 설명하며, 과태료 등 규제를 최소 1년 이상 유예하고 지원데스크를 운영한다고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1245"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "정책브리핑: 2026-01-22 시행, 생성형 AI 결과물·딥페이크 표시 의무, 사람이 최종 결정 권한을 유지하면 고영향 분류에서 제외, \"최소 1년 이상 규제를 유예\", 인공지능기본법 지원데스크 운영. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f14",
      "claim": "EU 사이버복원력법(CRA)에 따라 2026-09-11부터 디지털 요소 제품의 제조자는 실제 악용되는 취약점과 중대한 보안 사고를 ENISA 단일 보고 플랫폼을 통해 24시간 안에 조기 경보, 72시간 안에 통지, 이후 최종 보고(취약점은 수정 조치 후 14일, 중대 사고는 1개월)해야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1236"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보고 의무는 2026-09-11 시작, 조기 경보 24시간·통지 72시간·최종 보고 14일 또는 1개월, 단일 보고 플랫폼(SRP) 운영. 페이지는 오픈소스 스튜어드의 보고 의무 준수 시점을 2027-12-11로 적는다.",
      "as_of": "2026-09-11",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f15",
      "claim": "한국 개인정보보호법 제25조의2는 착용형·휴대형·부착·거치형 이동형 영상정보처리기기로 공개된 장소에서 사람을 촬영할 때 불빛·소리·안내판·안내방송 등으로 촬영 사실을 표시하게 하고, 표시했는데 거부 의사가 없는 경우 등에 한해 촬영을 허용한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1244"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "촬영 사실은 \"불빛, 소리, 안내판, 안내서면, 안내방송 또는 이에 준하는 수단\"으로 표시. 근거는 법 제25조의2·시행령 제27조. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f16",
      "claim": "고용노동부는 2017-10-29부터 산업용 로봇과 컨베이어를 산업안전보건법상 안전검사 대상에 추가해, 이미 쓰던 설비는 2018-12-31까지 최초 안전검사를 받게 했고, 그 근거로 최근 5년간 산업용 로봇 재해자 221명을 들었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1247"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보도자료(2017-10-26): 설비 자동화·무인화로 재해 증가가 예상되어 신규 선정, 기존 설비는 2018-12-31까지 최초 검사, 최근 5년 산업용 로봇 사고 221명·컨베이어 1,008명. 정기 검사 주기는 보도자료 본문에서 확인하지 못함.",
      "as_of": "2017-10-26",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f17",
      "claim": "ROS 2 개발자 가이드는 각 패키지에 LICENSE 파일(대개 Apache 2.0, 기존 허용형 라이선스가 있으면 예외)을 두고 모든 소스 파일에 라이선스·저작권 문구를 넣어 자동 린터(ament_copyright)로 검사하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1246"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Each source file must have a license and copyright statement, checked with an automated linter.\" 예외 예시로 rviz 의 3조항 BSD. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f18",
      "claim": "ROS 2 패키지 품질 등급을 정한 REP 2004(2019-12-17 작성, Active)는 품질 수준 1~4 패키지에 선언된 라이선스와 프로젝트 안의 저작권 명시·모든 저자 표기를 요구하고, 수준 5에는 권장만 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1237"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "수준 1~4 요구: \"Must have a declared license or set of licenses\", 저작권 명시와 저자 표기. 패키지는 품질 선언 문서로 충족 근거를 적는다.",
      "as_of": "2019-12-17",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f19",
      "claim": "SPDX는 소프트웨어 자재명세서(SBOM)의 출처·라이선스·보안 정보를 교환하는 개방 표준으로 ISO/IEC 5962:2021로 인정되었고, SPDX 라이선스 목록은 라이선스 식별자·예외·라이선스 표현식 문법을 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1238"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"recognized as the international open standard for security, license compliance, and other software supply chain artifacts as ISO/IEC 5962:2021\"; Linux Foundation 호스팅 프로젝트. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f20",
      "claim": "Gazebo(클래식) 모델 데이터베이스 규칙은 database.config 의 license 요소로 데이터베이스 안 모델의 라이선스를 지정하고 CC BY 3.0 Unported를 권장하며, 각 모델의 model.config 에 작성자 이름·이메일을 필수로 적게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1239"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "database.config 의 license: 데이터베이스 안 모델의 라이선스, Creative Commons Attribution 3.0 Unported 권장. model.config 에는 저작자 이름과 이메일. 개별 model.config 의 라이선스 필드는 요구하지 않음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 핵심 질문(이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가)의 답은 현장마다 다르며, 실외는 운행 규정·운행안전인증·운용자 의무·의무 보험(한국 f1~f5, 미국 버지니아 f8), 산업 사업장은 기계 안전 규제(한국 안전검사 f16, EU 기계류 규정 f12), 공통으로 AI·사이버보안·개인정보 규제(f13·f14·f15), 사고 책임 법제(f9~f11), 오픈소스·3D 자산 라이선스(f17~f20)가 겹치는 구조로 보이고, 병원·상업 시설·가정 실내 로봇에 특화된 운행 규정은 이번 조사에서 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-991",
        "ref-980",
        "ref-1248",
        "ref-1247",
        "ref-1212",
        "ref-1245",
        "ref-1236",
        "ref-1244",
        "ref-1235",
        "ref-1243",
        "ref-1246",
        "ref-1238",
        "ref-1239"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 finding 종합. 실내 서비스 로봇 사람 근접 기준(oq-231)과 승강기 탑승 KS(oq-173)는 이번 실행에서 다루지 못함.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "확인한 자료를 종합하면 59. 법·규제·보험·라이선스에서 ROP가 직접 맡을 범위는 로봇별 인증·보험 상태와 인증 조건(관제장치 조합, 속도·질량·운행 구역)을 등록 정보와 작업·경로 제약으로 반영하고, 사고·취약점 보고와 책임 판단에 필요한 실행 기록을 남기며, 촬영 표시 같은 규제 상태를 운영 조건으로 확인하고, 플랫폼 배포물의 라이선스·SBOM 목록을 관리하는 일로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-980",
        "ref-991",
        "ref-1236",
        "ref-1244",
        "ref-1238",
        "ref-1246"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f5 인증 대상이 로봇+관제장치 조합, f14 보고 기한 24·72시간, f15 촬영 표시, f17·f19 라이선스 선언·SBOM 에서 도출.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f23",
      "claim": "연계 대상: 분류 원문 19장의 업종별 조건 경계에 따라 인증 취득과 법적 적합성 판단(제조사·운영자), 보험 계약과 보상(운영자·보험사·협회), 제조물 책임 판정(당사자·법원), 개인정보 처리 적법성 판단(개인정보처리자), 사업장 안전검사(사업주)는 외부가 맡고, ROP는 그 결과를 작업·경로·권한 제약으로 받아 반영하고 근거 기록을 제공하는 쪽인 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-980",
        "ref-1240",
        "ref-1243",
        "ref-1235",
        "ref-1244",
        "ref-1247"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "원문 19장 '업종별 조건: 해당 조건을 작업·경로·권한 제약으로 반영'과 각 finding 의 의무 주체(운용자·운영자·제조자·사업주)에서 도출.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f24",
      "claim": "이 영역은 인증·안전검사의 50. 안전 표준·인증·사고 조사(f5·f16), 실외 운행 규정의 66. 실외(f1~f8), 촬영 표시의 53. 개인정보·영상 데이터(f15), 실질적 변경·책임 배분의 58. 다사업자 책임·계약·데이터(f9·f12), AI 규제의 13. 대화형 기능의 신뢰·기반과 47. AI·학습·적응과 모델 운영(f13), 취약점 보고의 52. 통신 보호·위협 관리·감사(f14), 라이선스·SBOM·보안 업데이트의 57. 자산·소프트웨어 수명주기 관리(f10·f17~f19), 인증 정보 등록의 4. 이기종 로봇 등록(f5), 운행 구역 규정의 16. 장소 의미·지도 관리(f6), 3D 자산 라이선스의 36. 가상 시운전·실제 상황 재현(f20), 보험료 부담의 3. 경제성·조달·사업 모델(f4)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-980",
        "ref-1247",
        "ref-991",
        "ref-1244",
        "ref-1235",
        "ref-1212",
        "ref-1245",
        "ref-1236",
        "ref-1246",
        "ref-1237",
        "ref-1238",
        "ref-992",
        "ref-1239",
        "ref-1240"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 finding 의 대상과 의무를 해당 세부영역에 대응시킨 종합.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-991",
      "org": "대한민국 정책브리핑 (산업통상자원부·경찰청)",
      "title": "‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 (제목 일부만 확인)",
      "published": "2023-11-16",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922726",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "개정 지능형로봇법·도로교통법 2023-11-17 시행으로 운행안전인증 실외이동로봇의 보도 통행 허용, 운용자 의무·범칙금, 보험·공제 가입 의무와 한국로봇산업협회 손해보장사업을 알린 정부 보도자료.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1235",
      "org": "Gibson Dunn",
      "title": "EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains",
      "published": "2026-03-23",
      "url": "https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "EU 개정 제조물책임지침(2024/2853)의 적용 시점(2026-12-09 이후 출시 제품), 소프트웨어 포함 제품 범위, 실질적 변경자 책임, 보안 업데이트 책임, 증거 공개·결함 추정을 정리한 법률사무소 해설. EUR-Lex 원문은 본문이 비어 열지 못해 대신 사용.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1236",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "Cyber Resilience Act - Reporting obligations",
      "published": "2026-09-11",
      "url": "https://digital-strategy.ec.europa.eu/en/policies/cra-reporting",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "EU 사이버복원력법의 취약점·중대 사고 보고 의무(2026-09-11 시작, 24시간·72시간·최종 보고)와 ENISA 단일 보고 플랫폼, 오픈소스 스튜어드 적용 시점을 안내하는 집행위원회 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1237",
      "org": "ROS (ros-infrastructure/rep)",
      "title": "REP 2004 -- Package Quality Categories",
      "published": "2019-12-17",
      "url": "https://ros.org/reps/rep-2004.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "ROS 2 패키지 품질 등급 1~5와 등급별 요구(라이선스 선언, 저작권·저자 표기 포함)를 정한 ROS 개선 제안 문서. ros.org 는 봇 차단 페이지가 떠 공식 저장소 원본을 열었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros-infrastructure/rep/master/rep-2004.rst",
      "source_unopened": false
    },
    {
      "id": "ref-1238",
      "org": "SPDX Project (Linux Foundation)",
      "title": "SPDX Overview",
      "published": null,
      "url": "https://spdx.dev/about/overview/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "SBOM 정보(출처·라이선스·보안)를 교환하는 개방 표준 SPDX 와 ISO/IEC 5962:2021 인정, SPDX 라이선스 목록을 소개하는 공식 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1239",
      "org": "Open Robotics (Gazebo Classic)",
      "title": "Gazebo : Tutorial : Model structure and requirements",
      "published": null,
      "url": "https://classic.gazebosim.org/tutorials?tut=model_structure",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Gazebo 모델 데이터베이스의 파일 구조와 database.config·model.config 요소(라이선스, 작성자 정보)를 설명하는 공식 튜토리얼.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1240",
      "org": "지디넷코리아",
      "title": "\"실외 이동로봇 필수보험 94% 저렴하게\"",
      "published": "2024-02-08",
      "url": "https://zdnet.co.kr/view/?no=20240208201432",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한국로봇산업협회가 실외이동로봇 손해배상책임 단체보험을 출시해 보험료를 대당 약 500만원에서 30만원대로 낮췄고 첫 가입 기업이 뉴빌리티·로보티즈라고 전한 기사.",
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
      "summary": "운행안전인증의 법적 근거(지능형로봇법 제40조의2), 인증 대상(실외이동로봇과 관제장치 조합), 8개 심사항목, 절차·처리기간을 안내하는 인증기관 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-992",
      "org": "지디넷코리아",
      "title": "실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 (제목 일부만 확인)",
      "published": "2023-07-28",
      "url": "https://zdnet.co.kr/view/?no=20230728173101",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한국로봇산업진흥원이 행정예고한 실외이동로봇 운행 안전기준 16가지 항목의 주요 수치(속도·폭·경사·알림음·방수 등)를 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1243",
      "org": "김·장 법률사무소",
      "title": "인공지능, 소프트웨어 결함으로 인한 제조물책임의 … (제목 일부만 확인)",
      "published": "2024-07",
      "url": "https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "한국 제조물책임법의 제조물 정의가 소프트웨어·AI 기인 사고를 포섭하는지, 해외 입법과 EU 제조물책임지침 동향을 다룬 법률사무소 뉴스레터(웹 요약만 열람, PDF 본문 미열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1244",
      "org": "법제처 찾기쉬운 생활법령정보",
      "title": "개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인)",
      "published": null,
      "url": "https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "개인정보보호법 제25조의2·시행령 제27조의 이동형 영상정보처리기기 정의, 공개된 장소 촬영 허용 요건, 촬영 사실 표시 방법을 설명하는 법제처 생활법령 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1245",
      "org": "대한민국 정책브리핑 (과학기술정보통신부)",
      "title": "'인공지능기본법' 22일 시행…생성형 AI 결과물 … (제목 일부만 확인)",
      "published": null,
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148958380",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "인공지능 기본법 2026-01-22 시행, 생성형 AI·딥페이크 표시, 고영향 AI 판단(사람의 최종 결정 권한 시 제외), 최소 1년 규제 유예, 지원데스크를 알린 정부 보도. 고영향 AI 정의에 연산량 기준을 섞은 요약이 나와 그 부분은 쓰지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1246",
      "org": "Open Robotics (ROS 2 Documentation)",
      "title": "ROS 2 developer guide",
      "published": null,
      "url": "https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "ROS 2 핵심 패키지 개발 규칙. 패키지 LICENSE 파일(대개 Apache 2.0), 소스 파일별 라이선스·저작권 문구, 자동 린터 검사를 정한다. 공식 문서 저장소 원본을 열었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/ros2_documentation/rolling/source/The-ROS2-Project/Contributing/Developer-Guide.rst",
      "source_unopened": false
    },
    {
      "id": "ref-1247",
      "org": "고용노동부",
      "title": "산업용 로봇과 컨베이어도 안전검사 필수",
      "published": "2017-10-26",
      "url": "https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "2017-10-29부터 산업용 로봇·컨베이어를 안전검사 대상에 추가하고 기존 설비의 최초 검사 기한(2018-12-31)과 재해 통계를 밝힌 정부 보도자료.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1248",
      "org": "Commonwealth of Virginia (Code of Virginia)",
      "title": "§ 46.2-908.1:1. Personal delivery devices",
      "published": null,
      "url": "https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "버지니아주 개인 배송 장치(PDD)의 운행 장소, 속도(보도 10mph 이하), 운영자 식별 표시, 최소 10만 달러 일반배상책임 보험을 정한 주법 조문.",
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
      "summary": "EU 기계류 규정 원문. 실질적 변경을 한 자의 제조자 의무와 2027-01-20 적용을 정한다. 이번 실행에서 다시 열지 않았다(재사용).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1212",
      "org": "European Agency for Safety and Health at Work (EU-OSHA)",
      "title": "Regulation 2023/1230/EU - machinery",
      "published": null,
      "url": "https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "EU 기계류 규정의 채택·적용 시점과 주요 내용을 소개하는 EU-OSHA 페이지. 이번 실행에서 다시 열지 않았다(재사용).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
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
      "rationale": "섹션 3: f21(핵심 질문 답, 추정), f9·f11(소프트웨어 사고 책임의 법적 공백·변화), f14(보고 기한) / 섹션 4: 운행안전인증·관제장치 조합 f1·f5, 운용자 f2, 책임보험·공제 f3, 제조물(소프트웨어 포함 여부) f9·f11, 실질적 변경 f9·f12, 사이버복원력법 보고 f14, 이동형 영상정보처리기기 f15, 라이선스 선언·SBOM f17~f19 / 섹션 5: 실외 — f1·f5(제약·수행 자원, 한국)·f2(수행 자원)·f3(제약)·f4(예외·성과)·f6·f7(제약), f8(제약, 미국 버지니아). 산업 사업장 안전검사 f16 은 출처가 현장 유형을 밝히지 않아 현장 유형 미명시로 서술. 물류창고·제조 공장·병원·상업 시설·가정 사례는 찾지 못했음을 명시 / 섹션 6: 인증·보험 조건의 운영 제약 반영 f5·f3·f8, 사고·취약점 보고 체계 f14·f10, 라이선스 선언·자동 검사·SBOM f17~f20 / 섹션 7: 지능형로봇법·도로교통법 f1~f7, 버지니아 PDD 주법 f8, EU 제조물책임지침 f9·f10, 한국 제조물책임법 f11, EU 기계류 규정 f12, 인공지능 기본법 f13, EU 사이버복원력법 f14, 개인정보보호법 제25조의2 f15, 산업안전보건법 안전검사 f16, ROS 2 개발자 가이드·REP 2004 f17·f18, SPDX(ISO/IEC 5962) f19, Gazebo 모델 라이선스 f20 / 섹션 8: f9·f11·f14 / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 3, 4, 13, 16, 36, 47, 50, 52, 53, 57, 58, 66 / 섹션 11: 기존 oq-143·oq-173·oq-186·oq-187·oq-231·oq-239·oq-249·oq-250·oq-262(모두 미해결 유지; oq-186 은 f5·f6·f7 로 현재 8개 항목만 확인, oq-143 은 f13 으로 부분 근거)와 open_questions_new 5건. 다음 실행 후보: 66. 실외 페이지에 f1~f8, 57. 자산·소프트웨어 수명주기 관리 페이지에 f17~f19 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "제조물책임",
      "term_en": "Product Liability",
      "definition": "제조물의 결함으로 생명·신체·재산에 손해가 생겼을 때 제조업자 등이 과실과 관계없이 배상 책임을 지는 제도로, 한국은 제조물책임법, EU는 개정 제조물책임지침(2024/2853)이 정하며 EU 지침은 소프트웨어를 제품에 포함한다."
    },
    {
      "term_ko": "사이버복원력법",
      "term_en": "Cyber Resilience Act (CRA)",
      "definition": "디지털 요소를 가진 제품의 사이버보안 요구사항과 제조자의 취약점·중대 사고 보고 의무(2026-09-11부터)를 정한 EU 규정이다."
    },
    {
      "term_ko": "소프트웨어 자재명세서",
      "term_en": "Software Bill of Materials (SBOM)",
      "definition": "소프트웨어를 이루는 구성 요소와 그 출처·버전·라이선스·보안 정보를 기계가 읽을 수 있게 나열한 목록으로, SPDX(ISO/IEC 5962:2021) 같은 형식으로 교환한다."
    },
    {
      "term_ko": "오픈소스 소프트웨어 스튜어드",
      "term_en": "Open-source Software Steward",
      "definition": "EU 사이버복원력법에서 상업 활동에 쓰이는 자유·오픈소스 소프트웨어의 개발을 체계적·지속적으로 지원하는 법인으로, 제조자보다 가벼운 사이버보안·보고 의무를 진다."
    }
  ],
  "open_questions_new": [
    "한국 실외이동로봇 책임보험·공제의 최저 가입금액(사망·부상·재물 한도)을 정한 산업통상자원부령 조항과 금액은 무엇인가? | 관련 영역: 59. 법·규제·보험·라이선스, 66. 실외 | 근거: f3 | 종류: 일반",
    "EU 개정 제조물책임지침에서 여러 제조사 로봇에 명령을 내리는 오케스트레이션 소프트웨어는 결함 제품이나 관련 서비스로 다뤄지는가, 그 소프트웨어의 설정·기능 변경이 실질적 변경에 해당해 플랫폼 사업자가 제조자로 간주될 수 있는가? | 관련 영역: 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터 | 근거: f9 | 종류: 일반",
    "국내 제조물책임법에 소프트웨어를 제조물로 포함하는 개정안이 발의되거나 통과되었는가, 그리고 로봇 관제·오케스트레이션 소프트웨어의 결함 사고에 관한 국내 판례가 있는가? | 관련 영역: 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터 | 근거: f11 | 종류: 일반",
    "로봇 오케스트레이션 플랫폼이 EU 사이버복원력법의 디지털 요소 제품 제조자에 해당하는가, 해당하면 로봇 제조사와 플랫폼 사업자 사이에 취약점 보고 의무를 어떻게 나누는가? | 관련 영역: 59. 법·규제·보험·라이선스, 52. 통신 보호·위협 관리·감사, 57. 자산·소프트웨어 수명주기 관리 | 근거: f14 | 종류: 일반",
    "시뮬레이션·가상 시운전에 쓰는 3D 자산(로봇 모델·건물 모델)의 라이선스와 저작자 표기를 자산 단위로 추적하는 표준 방법이 있으며, SPDX 로 3D 자산의 라이선스를 기술한 사례가 있는가? | 관련 영역: 59. 법·규제·보험·라이선스, 36. 가상 시운전·실제 상황 재현, 57. 자산·소프트웨어 수명주기 관리 | 근거: f20 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 17,
    "cross_checked_count": 2,
    "unverified": [
      "f3 실외이동로봇 책임보험 가입금액(사망 1억5천만원·부상 3천만원·재물 10억원)은 검색 요약에만 있고 시행규칙 원문을 열지 못해 finding 에서 뺌",
      "f4 단체보험 보장 한도 미확인",
      "f7 운행안전인증 심사항목이 16가지에서 8개로 바뀐 개정 시점·근거 고시 미확인(oq-186). 검색 요약에 '다시 16개로 재정의'라는 서술이 있었으나 인증기관 페이지(2026-09-30 확인)는 8개를 나열해 확인되지 않은 요약은 쓰지 않음",
      "f9·f10 EU 제조물책임지침은 EUR-Lex 원문·PDF 본문이 비어 열지 못해 법률사무소 해설 기준. 오픈소스 예외 조항 미확인",
      "f11 김·장 뉴스레터 PDF 본문 미열람, 웹 요약 기준",
      "f13 고영향 인공지능의 법정 영역 목록과 사업자 책무 조문은 시행령·가이드라인 원문을 열지 못해 미확인(신·김 뉴스레터 403)",
      "f14 오픈소스 스튜어드 보고 의무 시점(2027-12-11)은 집행위원회 페이지 한 곳 기준이며, 제조자 보고 의무 시점과 같다고 적은 다른 요약과 교차 확인하지 못함",
      "f15 개인정보보호법 제25조의2 시행일은 출처 요약이 2023-09-15(검색 요약)와 2024-12-03(생활법령 페이지 요약)으로 달라 finding 에 넣지 않음",
      "f16 산업용 로봇 정기 안전검사 주기(최초 3년 이내, 이후 2년)는 검색 요약에만 있고 안전보건공단 페이지가 비어 확인하지 못함",
      "Open-RMF 저장소 라이선스는 GitHub 페이지 403·raw 경로 404 로 확인하지 못해 넣지 않음",
      "일본 원격조작형 소형차 신고제(2023-04 시행)는 1차 출처를 열지 않아 넣지 않음",
      "병원·상업 시설·가정 실내 로봇의 운행 규정, 승강기 탑승 KS(oq-173), 실내 사람 근접 기준(oq-231)은 이번에 조사하지 못함"
    ],
    "scope_violations": [
      "f16: 산업용 로봇 안전검사는 사업주의 설비 안전 의무이고 원문 19장 '시설·설비 제어'·'업종별 조건' 쪽이므로 규제 사례로만 쓰고 ROP 직접 범위로 서술하지 않음(f23 연계 대상)",
      "f9·f10·f11: 제조물 책임의 법적 판정은 당사자·법원 몫이므로 ROP 가 제공할 기록의 근거로만 쓰고 f23 에서 연계 대상으로 둠",
      "f15: 영상 촬영 적법성 판단은 53. 개인정보·영상 데이터와 겹치므로 이 영역에서는 규제 목록으로만 다룸",
      "f8: 미국 주법은 한국 현장에 바로 적용되지 않으므로 해외 비교 사례로만 제안"
    ],
    "budget_used": {
      "queries": 17,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-991~ref-1248, 예약 구간 안)로 신규 출처 상한에 도달했다. 재사용 2건: ref-555·ref-1212(EU 기계류 규정, 이전 브리프 2026-09-30-22 출처 표 값 사용, 이번에 다시 열지 않아 fetched false). 참고문헌 목록 요약에 행이 없어 같은 URL 이 이미 있으면 퍼블리셔 병합 필요. 원문 열람: 신규 15건 모두 열었다(webfetch 13, github_raw 2). ros.org(봇 차단)는 ros-infrastructure/rep, docs.ros.org 는 ros2/ros2_documentation 공식 저장소 원본을 열었다. EUR-Lex(본문 비어 있음)·신·김 뉴스레터(403)·안전보건공단 포털(본문 비어 있음)·Open-RMF GitHub(403)는 열지 못해 출처로 쓰지 않았다. 교차 확인 2건(f1: 정책브리핑·한국로봇산업진흥원, f3: 정책브리핑·지디넷코리아). 벤더 주장 없음. 분류 원문 핵심 질문에는 f21 로 답했고 결론은 '현장마다 다르며 실외는 운행 규정·인증·운용자 의무·의무 보험, 산업 사업장은 기계 안전 규제, 공통으로 AI·사이버보안·개인정보 규제, 제조물 책임, 오픈소스·3D 자산 라이선스가 겹친다'는 추정이다. 현장 유형 사례는 실외(f1~f7 한국, f8 미국)뿐이고 f16(산업용 로봇 안전검사)은 출처가 현장 유형을 밝히지 않아 null 로 두었다. 물류창고·제조 공장·병원·상업 시설·가정 사례는 찾지 못했다. 국내 자료는 정책브리핑(ref-991·ref-1245)·한국로봇산업진흥원(ref-980)·고용노동부(ref-1247)·법제처 생활법령(ref-1244)·김·장(ref-1243)·지디넷코리아(ref-1240·ref-992)다. 기존 열린 질문 9건은 해결하지 못했다(oq-186 은 현재 8개 심사항목만 확인, 개정 시점·흡수 관계 미확인; oq-187 은 인증 대상이 로봇과 관제장치 조합이라는 전제만 재확인; oq-143 은 f13 이 사람의 최종 결정 권한 시 고영향 제외라는 정부 설명만 제공해 부분 근거). L. AI·학습 기술 관련은 f13(인공지능 기본법)을 13. 대화형 기능의 신뢰·기반과 47. AI·학습·적응과 모델 운영에 연결 제안했다(f24). 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. 용어집에 이미 있는 고영향 인공지능·실외이동로봇 운행안전인증·개인 배송 장치·이동형 영상정보처리기기·원격 조작형 소형차·위험성평가는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-23/verification.json

```json
{
  "run_id": "2026-09-30-23",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. ref-991(산업통상자원부·경찰청 공동 발표, 2023-11-16)를 직접 열어 2023-11-17 시행, 질량 500kg 이하·15km/h 이하, 운행안전인증 로봇에 보행자 지위를 부여한다는 문장을 확인했다. ref-980(한국로봇산업진흥원)에서도 최대 속도 15km/h 이하·최대 질량 500kg 이하 요건을 확인해 두 출처로 교차 확인했다. 시행일은 ref-991 단독이지만 정부 1차 자료다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-991 에 운용자의 정확한 조작·안전한 운용 의무, 로봇도 보행자와 같이 신호위반·무단횡단 금지 등 도로교통법을 지켜야 한다는 문장, 위반 시 범칙금 3만 원이 있다. 정부 1차 자료 단일 출처."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. ref-991 에 보도 운영자의 보험·공제 가입 의무 부과와 한국로봇산업협회의 손해보장사업 실시기관 지정이 있고, ref-1240(지디넷코리아, 2024-02-08)이 '운영 주체는 의무적으로 공제(보험)에 가입해야 한다'고 보도해 교차 확인했다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. ref-1240 에서 약 500만원대 → 30만원대(94% 할인), 1호 가입 기업 뉴빌리티·로보티즈를 확인했다. 다만 보험료 수치는 상품을 낸 한국로봇산업협회의 발표를 옮긴 기사 한 건뿐이고 독립 확인이 없다. 기사는 이 상품을 '공제상품'이라고도 부른다. 보장 한도는 미확인이다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-980 인증기관 페이지(2026-09-30 확인)에서 근거(지능형로봇법 제40조의2), 8개 심사항목(규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치), 서류심사→제품심사→인증표시 절차, 신청일부터 30일 이내 처리를 확인했다. 인증 대상의 페이지 표현은 '배송 등을 위하여 자율주행(원격제어 포함)으로 운행할 수 있는 지능형 로봇 및 그 운행에 필요한 관제장치 조합'이고, 브리프 발췌의 '…조합의 일체'라는 문구는 확인하지 못해 직접 인용하지 않는다. 발행일은 미확인이다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-992 를 열어 질량별 속도(230kg 초과 5km/h, 100kg 초과 10km/h, 그 이하 15km/h), 폭 80cm(보도 폭 250cm 이상이면 120cm), 5도 경사, 비상정지, 장애물 회피, 횡단보도 신호 대기, 알림음 55~73dB, 등화장치 표면온도 60도 이하, IPX4 이상, 의견 제출 마감 2023-08-28 을 확인했다. 기사는 행정예고 주체를 한국로봇산업진흥원이 아니라 산업통상자원부로 적으므로 주체를 고쳐야 한다. 제목 전체는 '실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사'다. 행정예고안(2023-07) 기준 내용이라는 기준일을 밝힌다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 인증기관 페이지(8개 항목, 2026-09-30 확인)와 2023-07 기사(16가지)의 차이가 확인된다. ref-991(2023-11-16)도 시행 시점에 '16가지 시험항목'으로 검증한다고 밝혀 추정의 전제가 강해진다. 개정 시점·고시와 흡수 관계는 미확인이므로 oq-186 은 열린 채로 둔다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1248 버지니아주법 원문에서 보도·횡단보도 10mph 이하, 잘 보이는 운영자 식별 수단, 'general liability coverage of at least $100,000' 보험 유지를 확인했다. 지방정부는 도로 운행에 추가 안전 요건을 둘 수 있으나, 제한 속도 25mph 이하 도로에서의 사용을 금지할 수는 없다. 해외 비교 사례다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. ref-1235(Gibson Dunn, 2026-03-23)에서 2026-12-09 이후 출시·사용 개시 제품에 적용, 독립형 소프트웨어·디지털 제조 파일·통합 디지털 요소 포함, 실질적 변경자의 제조자 간주를 확인했다. 검증에서 연 CMS 해설(2024-12-04, 브리프 출처 아님)도 같은 내용이어서 교차 확인은 했지만, EUR-Lex 원문은 열리지 않아 법률사무소 해설 기준이다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1235 에 보안 업데이트 미제공에 따른 책임, 증거 공개 불이행 시 반증 가능한 결함 추정이 있다. 증거 공개·결함 추정은 CMS 해설로도 확인했지만, 보안 업데이트 책임은 ref-1235 단독이다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1243 웹 요약에서 제조물 정의('제조되거나 가공된 동산')와, 자율주행차 소프트웨어 결함 사고에서 인간 개입이 없거나 최소화된 경우 개발자의 제조물책임이 핵심 쟁점이라는 서술을 확인했다. 정확한 제목은 '인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점', 발행일은 2024-07-05 다. '쟁점으로 남아 있다'는 2024-07 기준이다. PDF 본문은 미열람이다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1212(EU-OSHA)를 검증에서 열어 채택 2023-06-14·적용 2027-01-20 을 확인했다. 다만 이 페이지는 실질적 변경자의 제조자 간주를 직접 말하지 않는다. 제18조 내용은 EUR-Lex(ref-555) 검색 결과 요약과 일치하지만 PDF 본문이 비어 원문 미열람이다. 이전 실행 2026-09-30-22 의 f10 과 같은 주장이므로 같은 참고문헌 id 를 재사용한다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1245(과학기술정보통신부, 2026-01-21)에서 2026-01-22 시행, 최종 의사결정에 사람이 개입하면 고영향AI 대상에서 제외, '최소 1년 이상 규제를 유예'(사실조사·과태료 계도기간), 인공지능기본법 지원데스크 운영을 확인했다. 브리프의 발행일 null 과 as_of 2026-09-30 은 2026-01-21 로 고쳐야 한다. 정확한 제목은 ''인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무'다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1236(집행위원회, 최종 갱신 2026-09-11)에서 제조자 보고 의무 2026-09-11 시작, 24시간 조기 경보·72시간 통지·최종 보고(취약점은 수정 조치 후 14일, 중대 사고는 72시간 통지 후 1개월), ENISA 가 세운 단일 보고 플랫폼, 오픈소스 스튜어드 2027-12-11 을 확인했다. 집행기관 1차 자료 단일 출처."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1244(법제처 생활법령)에서 착용형·휴대형·부착·거치형 정의, 촬영 사실을 표시했는데 거부 의사가 없는 경우 등의 허용 요건, '불빛, 소리, 안내판, 안내서면, 안내방송 또는 그 밖에 이에 준하는 수단' 표시를 확인했다. 페이지가 드는 근거는 법 제25조의2·시행령 제22조·제27조의2 이며, 브리프 발췌의 '시행령 제27조'와 다르다. 시행일은 넣지 않는다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1247(2017-10-26)에서 2017-10-29 시행, 기존 설비 2018-12-31 까지 최초 안전검사, 최근 5년 산업용 로봇 221명·컨베이어 1,008명 재해를 확인했다. 정기검사 주기는 본문에 없어 미확인이다. 출처가 현장 유형을 밝히지 않는다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1246 원본(github_raw)에서 'Each package must have a LICENSE file, typically the Apache 2.0 license, unless the package has an existing permissive license (e.g. rviz uses three-clause BSD)'와 소스 파일별 라이선스·저작권 문구의 자동 린터 검사를 확인했다. 요약에서 확인된 도구 이름은 ament_lint_common 이고 'ament_copyright'는 확인하지 못했으므로 도구 이름을 빼게 한다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1237 원본(Created 17-Dec-2019, Active)에서 수준 1~4 의 'Must have a declared license or set of licenses'·저작권 명시와 저자 표기, 수준 5 의 강한 권장을 확인했다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1238 에서 ISO/IEC 5962:2021 인정 문장, SBOM 정보(출처·라이선스·보안) 교환 개방 표준, 라이선스 목록의 식별자·예외·표현식 문법을 확인했다. 발행일은 미확인이다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1239 에서 database.config 의 CC BY 3.0 Unported 권장, model.config 의 작성자 이름·이메일 필수, 개별 model.config 에 라이선스 필드가 없음을 확인했다. Gazebo 클래식 기준임을 밝힌다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 인용한 finding 들의 종합이며 과장이 없다. 병원·상업 시설·가정 실내 규정을 확인하지 못했다는 한계를 함께 적었다. 원문 핵심 질문에 답하는 finding 이다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. f5(인증 대상이 로봇과 관제장치의 조합)·f14·f15·f17·f19 에서 도출한 직접 범위 제안이며 범위 경계 위반이 없다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 분류 원문 19장 '업종별 조건' 경계에 맞게 인증·보험·책임 판정·개인정보 적법성·안전검사를 연계 대상으로 두었다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 연결 영역이 모두 부록 A 번호·이름과 맞고, 교차 규칙에 따라 AI 규제(f13)를 13. 대화형 기능의 신뢰·기반과 47. AI·학습·적응과 모델 운영 양쪽에 연결했다."
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
      "f12(EU 기계류 규정의 실질적 변경·적용일)는 이전 실행 2026-09-30-22 의 f10(58. 다사업자 책임·계약·데이터)과 같은 주장이다 — 같은 참고문헌 id(ref-555·ref-1212)를 재사용하고, 58. 다사업자 책임·계약·데이터 페이지와 연결만 한다",
      "open_questions_new 2번(EU 제조물책임지침에서 오케스트레이션 소프트웨어의 실질적 변경)은 2026-09-30-22 브리프의 새 질문(오케스트레이션 설정 변경이 EU 기계류 규정의 실질적 변경인가)과 가깝지만, 대상 법이 달라 중복으로 보지 않는다",
      "f12·f14 는 oq-249(EU 기계류 규정 기록 요구의 플랫폼 적용)와 관련된다 — 해결 근거는 아니다"
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
    "ref-991: 각주 제목을 '‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용'으로 쓰고 '(제목 일부만 확인)'을 뺀다 — 검증에서 원문을 열어 전체 제목과 산업통상자원부·경찰청 공동 발표(2023-11-16)를 확인했다.",
    "ref-992·f6: 각주 제목을 '실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사'로 고치고, 본문에서 행정예고 주체를 '한국로봇산업진흥원'이 아니라 '산업통상자원부'로 쓴다. 기준일은 '2023-07 행정예고안 기준'으로 밝힌다 — 기사 원문이 산업통상자원부를 행정예고 주체로 적는다.",
    "ref-1245·f13: 각주 발행일을 2026-01-21 로, 제목을 ''인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무'로 쓰고, f13 문장의 기준일도 2026-01-21 로 쓴다 — 원문의 발행일이 2026-01-21 이다.",
    "ref-1243·f11: 각주 제목을 '인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점', 발행일을 2024-07-05 로 쓰고, '쟁점으로 남아 있다'는 서술에 '2024-07 기준'을 붙인다 — 원문 페이지에서 확인한 값이다.",
    "f4: [사실]을 [추정]으로 강등하고, '한국로봇산업협회 발표를 전한 기사(ref-1240) 기준'임과 보장 한도 미확인을 함께 적는다 — 보험료 수치(약 500만원대 → 30만원대, 94%)는 상품 출시 주체의 발표를 옮긴 기사 한 건뿐이다.",
    "f5: 인증 대상은 '…조합의 일체'를 직접 인용하지 말고 '배송 등을 위해 자율주행(원격제어 포함)으로 운행하는 지능형 로봇과 그 운행에 필요한 관제장치의 조합'으로 재서술한다 — 인증기관 페이지에서 '일체'라는 문구를 확인하지 못했다.",
    "f15: 근거 조항을 '개인정보 보호법 제25조의2와 같은 법 시행령(생활법령 페이지가 드는 제22조·제27조의2)'으로 쓰고 '시행령 제27조'라고 쓰지 않는다. 시행일은 쓰지 않는다 — 출처 페이지의 조항 표기가 브리프 발췌와 다르고, 시행일은 출처끼리 충돌한다.",
    "f17: 'ament_copyright'라는 도구 이름을 빼고 '자동 린터로 검사한다'고만 쓴다 — 확인한 원문 요약은 ament_lint_common 을 들고 있고 ament_copyright 는 확인되지 않았다.",
    "f12: 제18조(실질적 변경자의 제조자 간주) 문장에는 ref-555 각주를 붙이고, ref-555·ref-1212 두 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이며 reference_updates 의 두 항목에 source_unopened: true 를 넣는다. 58. 다사업자 책임·계약·데이터 페이지와 같은 참고문헌 id 를 재사용한다 — 리서치에서 두 출처를 다시 열지 않았고(fetched false), EU-OSHA 페이지는 적용일만 뒷받침한다.",
    "f9·f10: 본문에 'EUR-Lex 원문이 아니라 법률사무소 해설(Gibson Dunn, 2026-03-23) 기준'임을 밝힌다 — 지침 원문 본문을 열지 못했다.",
    "f16: 5절 '적용 사례 (현장 유형 명시)'에 현장 유형 미명시 사례로 넣지 말고, 7절(관련 표준·프레임워크·오픈소스)의 산업안전보건법 안전검사 항목으로만 쓴다 — 출처가 현장 유형을 밝히지 않아 여섯 항목 사례를 세울 수 없다.",
    "5절: 현장 유형은 '실외'로만 쓴다(한국 f1~f7, 미국 버지니아 f8). f8 은 해외 비교 사례로 한국 현장에 바로 적용되지 않음을 밝히고, 물류창고·제조 공장·병원·상업 시설·가정 사례는 이번 조사에서 찾지 못했다고 적는다. site_matrix_updates 는 실외 칸만 낸다 — 브리프 근거가 실외뿐이다.",
    "glossary_candidates '오픈소스 소프트웨어 스튜어드': 용어집에 등록하지 않는다 — 정의의 '법인'·'제조자보다 가벼운 의무' 부분을 뒷받침하는 finding 이 없다(f14 는 보고 의무 시점만 담는다).",
    "glossary_candidates '제조물책임': 정의에서 '과실과 관계없이'를 빼고 f9·f11 이 뒷받침하는 범위(제조물 결함으로 생긴 손해의 배상 책임, 한국 제조물책임법은 제조·가공된 동산을 제조물로 정의, EU 개정 지침은 소프트웨어를 제품에 포함)로 쓴다 — 무과실 책임을 뒷받침하는 finding 이 없다.",
    "11절: 기존 oq-143·oq-173·oq-186·oq-187·oq-231·oq-239·oq-249·oq-250·oq-262 는 모두 열림으로 둔다. oq-186 에는 2023-11-16 정책브리핑(ref-991)도 '16가지 시험항목'을 밝혔다는 점을 f7 과 함께 적을 수 있다 — 해결을 인정할 finding 이 없다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 24건, 미확인 0건, 교차 확인 3건(f1·f3·f9). 강등: f4 사실 → 추정(보험료 인하 수치가 협회 발표를 옮긴 기사 한 건뿐). 원문 미열람 출처: ref-555, ref-1212(이전 실행에서 재사용했고 이번 리서치에서 다시 열지 않음. 검증에서 ref-1212 는 열어 적용일만 확인했고, ref-555 은 EUR-Lex 본문이 비어 검색 결과 일치로만 확인). 주의: 사실 주장은 대부분 정부·기관 1차 자료 단일 출처다. EU 제조물책임지침(f9·f10)은 지침 원문이 아니라 법률사무소 해설 기준이다. 실외이동로봇 운행안전인증 심사항목이 16가지에서 8개로 바뀐 시점과 근거(oq-186)는 확인하지 못했다. 한국 제조물책임법의 소프트웨어 포섭 쟁점(f11)은 2024-07 기준이다. 현장 유형 사례는 실외뿐이며 병원·상업 시설·가정 실내 로봇 규정은 확인하지 못했다. 검증에서 f6 의 행정예고 주체(산업통상자원부)와 ref-991·ref-992·ref-1243·ref-1245 의 제목·발행일을 정정하도록 지시했다. 미사용 출처 없음. 정정 요청 없음. 해결 인정한 열린 질문 없음. 검증 검색 2회를 썼다(리서치와 합쳐 19/30).",
  "retry_reason": null
}
```

### runs/2026-09-30-23/pages.json

```json
{
  "run_id": "2026-09-30-23",
  "outline": [
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "지켜야 할 법·규제·보험·라이선스는 현장마다 다르고, 실외 운행 규정·산업 기계 안전·AI·사이버보안·개인정보·사고 책임·라이선스가 겹치는 구조로 보인다. [추정][^ref-991][^ref-1235]",
      "planned_findings": [
        "f21",
        "f9",
        "f11",
        "f14"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1100,
      "summary": "운행안전인증·운용자·책임보험·제조물책임·실질적 변경·고영향 인공지능·사이버복원력법 보고 의무·SBOM 을 정리한다. [사실][^ref-980][^ref-1235]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f5",
        "f9",
        "f11",
        "f12",
        "f13",
        "f14",
        "f19"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1600,
      "summary": "실외 사례 두 건(한국 보도 운행, 미국 버지니아 개인 배송 장치 해외 비교)을 여섯 항목으로 쓴다. [사실][^ref-991][^ref-1248]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1300,
      "summary": "인증·보험 조건을 운영 제약으로 반영, 사고·취약점 보고와 증거 기록, 라이선스 선언·자동 검사·SBOM 의 세 갈래로 보인다. [추정][^ref-980][^ref-1236][^ref-1246]",
      "planned_findings": [
        "f5",
        "f3",
        "f10",
        "f14",
        "f17",
        "f18",
        "f19",
        "f20",
        "f22"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 2000,
      "summary": "한국 실외 로봇 법령·운행안전인증, 버지니아 PDD 주법, EU 제조물책임지침·기계류 규정·사이버복원력법, 한국 제조물책임법·인공지능 기본법·개인정보 보호법·산업안전보건법 안전검사, ROS 2 라이선스 규칙·REP 2004·SPDX·Gazebo 규칙을 표로 둔다. [사실][^ref-991][^ref-1238]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f5",
        "f8",
        "f9",
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17",
        "f18",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 900,
      "summary": "정부·집행기관 1차 자료와 법률사무소 해설이 중심이다. [사실][^ref-1235][^ref-1243]",
      "planned_findings": [
        "f9",
        "f11",
        "f14",
        "f1",
        "f5"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 900,
      "summary": "ROP는 인증·보험 상태와 규제 조건을 작업·경로·권한 제약으로 반영하고 기록·라이선스 목록을 관리하며, 인증 취득·보험·책임 판정·적법성 판단·안전검사는 연계 대상으로 보인다. [추정][^ref-980][^ref-1247]",
      "planned_findings": [
        "f22",
        "f23"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1200,
      "summary": "안전 인증, 개인정보·보안, 수명주기, 책임 배분, 실외 현장 등 12개 영역과 이어지는 것으로 보인다. [추정][^ref-980][^ref-1244]",
      "planned_findings": [
        "f24"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "11. 열린 질문",
      "budget_chars": 1900,
      "summary": "기존 열린 질문 10건은 모두 열림으로 두고 새 질문 5건을 올린다. [사실][^ref-980]",
      "planned_findings": [
        "f7",
        "f13",
        "f3",
        "f9",
        "f11",
        "f14",
        "f20"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 첫 작성(seed → draft), 13절 각주 16건, 프런트매터 related_areas·tags·sources·confidence·last_run 채움(2차 수정: 열린 질문 10건, 구축자 의견 표시, 7절 각주 보강, SBOM 풀어쓰기, 8절 문장 정리)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area59-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"7. 관련 표준·프레임워크·오픈소스\" 절을 옮겼다(2차 수정: 요약 문장 각주 보강, ROS 2 행 표현, ENISA·SBOM 풀어쓰기)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area59-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"11. 열린 질문\" 절을 옮겼다(2차 수정: 기존 열린 질문 10건, oq-275 추가)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area59-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"4. 핵심 개념과 용어\" 절을 옮겼다(2차 수정: 구축자 의견 표시, ENISA 풀어쓰기)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area59-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"6. 대표 접근법과 기술\" 절을 옮겼다(2차 수정: SBOM 풀어쓰기)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area59-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절을 옮겼다(2차 수정: SBOM 풀어쓰기)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area59-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"3. 왜 중요한가\" 절을 옮겼다(2차 수정: 구축자 의견 표시)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area59-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"8. 대표 연구와 자료\" 절을 옮겼다(2차 수정: 첫 문장 정리)"
    }
  ],
  "changelog_entry": "2026-09-30 | 59. 법·규제·보험·라이선스 | 영역 심화 3~11절 첫 작성(한국·미국 실외 로봇 운행 규정·보험, EU·한국 제조물 책임, AI·사이버보안·개인정보·산업안전 규제, ROS 2·SPDX·Gazebo 라이선스 규칙), 새 열린 질문 5건 | run 2026-09-30-23",
  "index_updates": {
    "home_recent": "2026-09-30 — 59. 법·규제·보험·라이선스: 영역 심화 첫 작성(실외이동로봇 운행안전인증·보험 의무, EU 제조물책임지침·사이버복원력법, ROS 2 라이선스 선언·SPDX)",
    "category_recent": "2026-09-30 — 59. 법·규제·보험·라이선스: 3~11절 첫 작성(실외 운행 규정·보험, 제조물 책임, AI·보안·개인정보 규제, 오픈소스 라이선스), 새 열린 질문 5건",
    "area_recent": "2026-09-30 — 59. 법·규제·보험·라이선스: 영역 심화로 3~11절 첫 작성, 실외 적용 사례 2건(한국, 미국 버지니아 해외 비교), 참고 자료 17건"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "product-liability",
      "term_ko": "제조물책임",
      "term_en": "Product Liability",
      "definition": "제조물 결함으로 생긴 손해의 배상 책임을 정하는 제도로, 한국 제조물책임법은 제조되거나 가공된 동산을 제조물로 정의하고, EU 개정 제조물책임지침(Directive (EU) 2024/2853)은 독립형 소프트웨어를 제품에 포함한다.",
      "description": "한국 제조물책임법은 소프트웨어를 명시적으로 포함하지 않아 자율 시스템 사고에서 소프트웨어 개발자의 책임이 쟁점으로 남아 있다(2024-07 기준). EU 지침 내용은 법률사무소 해설(Gibson Dunn, 2026-03-23) 기준이다.",
      "related_areas": [
        59,
        58,
        57
      ],
      "sources": [
        "ref-1235",
        "ref-1243"
      ]
    },
    {
      "action": "new",
      "slug": "cyber-resilience-act",
      "term_ko": "사이버복원력법",
      "term_en": "Cyber Resilience Act (CRA)",
      "definition": "디지털 요소를 가진 제품의 제조자에게 실제 악용되는 취약점과 중대한 보안 사고의 보고 의무(2026-09-11부터)를 두는 EU 규정이다.",
      "description": "보고는 유럽연합 사이버보안청(European Union Agency for Cybersecurity, ENISA) 단일 보고 플랫폼으로 24시간 안 조기 경보, 72시간 안 통지, 최종 보고(취약점은 수정 조치 후 14일, 중대 사고는 1개월) 순이다.",
      "related_areas": [
        59,
        52,
        57
      ],
      "sources": [
        "ref-1236"
      ]
    },
    {
      "action": "new",
      "slug": "software-bill-of-materials",
      "term_ko": "소프트웨어 자재명세서",
      "term_en": "Software Bill of Materials (SBOM)",
      "definition": "소프트웨어를 이루는 구성 요소의 출처·라이선스·보안 정보를 담은 목록으로, SPDX(ISO/IEC 5962:2021) 같은 개방 표준으로 교환한다.",
      "related_areas": [
        59,
        57
      ],
      "sources": [
        "ref-1238"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-991",
      "org": "대한민국 정책브리핑 (산업통상자원부·경찰청)",
      "title": "‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용",
      "published": "2023-11-16",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922726",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "개정 지능형로봇법·도로교통법 2023-11-17 시행으로 운행안전인증 실외이동로봇의 보도 통행 허용, 운용자 의무·범칙금, 보험·공제 가입 의무와 한국로봇산업협회 손해보장사업을 알린 산업통상자원부·경찰청 공동 보도자료.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s3.md",
        "docs/topics/2026/2026-09-30-area59-s4.md",
        "docs/topics/2026/2026-09-30-area59-s6.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s8.md",
        "docs/topics/2026/2026-09-30-area59-s10.md",
        "docs/topics/2026/2026-09-30-area59-s11.md"
      ]
    },
    {
      "id": "ref-1235",
      "org": "Gibson Dunn",
      "title": "EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains",
      "published": "2026-03-23",
      "url": "https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "EU 개정 제조물책임지침(2024/2853)의 적용 시점(2026-12-09 이후 출시 제품), 소프트웨어 포함 제품 범위, 실질적 변경자 책임, 보안 업데이트 책임, 증거 공개·결함 추정을 정리한 법률사무소 해설. EUR-Lex 원문을 열지 못해 대신 사용.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s3.md",
        "docs/topics/2026/2026-09-30-area59-s4.md",
        "docs/topics/2026/2026-09-30-area59-s6.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s8.md",
        "docs/topics/2026/2026-09-30-area59-s10.md"
      ]
    },
    {
      "id": "ref-1236",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "Cyber Resilience Act - Reporting obligations",
      "published": "2026-09-11",
      "url": "https://digital-strategy.ec.europa.eu/en/policies/cra-reporting",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "EU 사이버복원력법의 취약점·중대 사고 보고 의무(2026-09-11 시작, 24시간·72시간·최종 보고)와 ENISA 단일 보고 플랫폼, 오픈소스 스튜어드 적용 시점을 안내하는 집행위원회 페이지.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s3.md",
        "docs/topics/2026/2026-09-30-area59-s4.md",
        "docs/topics/2026/2026-09-30-area59-s6.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s8.md",
        "docs/topics/2026/2026-09-30-area59-s10.md"
      ]
    },
    {
      "id": "ref-1237",
      "org": "ROS (ros-infrastructure/rep)",
      "title": "REP 2004 -- Package Quality Categories",
      "published": "2019-12-17",
      "url": "https://ros.org/reps/rep-2004.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "ROS 2 패키지 품질 등급 1~5와 등급별 요구(라이선스 선언, 저작권·저자 표기 포함)를 정한 ROS 개선 제안 문서. 공식 저장소 원본을 열었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s10.md"
      ]
    },
    {
      "id": "ref-1238",
      "org": "SPDX Project (Linux Foundation)",
      "title": "SPDX Overview",
      "published": null,
      "url": "https://spdx.dev/about/overview/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "SBOM 정보(출처·라이선스·보안)를 교환하는 개방 표준 SPDX 와 ISO/IEC 5962:2021 인정, SPDX 라이선스 목록을 소개하는 공식 페이지.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s4.md",
        "docs/topics/2026/2026-09-30-area59-s6.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s10.md"
      ]
    },
    {
      "id": "ref-1239",
      "org": "Open Robotics (Gazebo Classic)",
      "title": "Gazebo : Tutorial : Model structure and requirements",
      "published": null,
      "url": "https://classic.gazebosim.org/tutorials?tut=model_structure",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Gazebo 모델 데이터베이스의 파일 구조와 database.config·model.config 요소(라이선스, 작성자 정보)를 설명하는 공식 튜토리얼.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s6.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s10.md"
      ]
    },
    {
      "id": "ref-1240",
      "org": "지디넷코리아",
      "title": "\"실외 이동로봇 필수보험 94% 저렴하게\"",
      "published": "2024-02-08",
      "url": "https://zdnet.co.kr/view/?no=20240208201432",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한국로봇산업협회 발표를 전한 기사로, 협회가 실외이동로봇 손해배상책임 단체보험을 출시해 보험료를 대당 약 500만원에서 30만원대로 낮췄고 첫 가입 기업이 뉴빌리티·로보티즈라고 전했다. 보장 한도는 기사에 없다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s4.md",
        "docs/topics/2026/2026-09-30-area59-s10.md"
      ]
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
      "summary": "운행안전인증의 법적 근거(지능형로봇법 제40조의2), 인증 대상(실외이동로봇과 관제장치의 조합), 8개 심사항목, 절차·처리기간을 안내하는 인증기관 페이지.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s3.md",
        "docs/topics/2026/2026-09-30-area59-s4.md",
        "docs/topics/2026/2026-09-30-area59-s6.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s8.md",
        "docs/topics/2026/2026-09-30-area59-s10.md",
        "docs/topics/2026/2026-09-30-area59-s11.md"
      ]
    },
    {
      "id": "ref-992",
      "org": "지디넷코리아",
      "title": "실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사",
      "published": "2023-07-28",
      "url": "https://zdnet.co.kr/view/?no=20230728173101",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "산업통상자원부가 행정예고한 실외이동로봇 운행 안전기준 16가지 항목의 주요 수치(속도·폭·경사·알림음·방수 등)를 전한 기사(2023-07 행정예고안 기준).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s10.md",
        "docs/topics/2026/2026-09-30-area59-s11.md"
      ]
    },
    {
      "id": "ref-1243",
      "org": "김·장 법률사무소",
      "title": "인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점",
      "published": "2024-07-05",
      "url": "https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "한국 제조물책임법의 제조물 정의가 소프트웨어·AI 기인 사고를 포섭하는지, 해외 입법과 EU 제조물책임지침 동향을 다룬 법률사무소 뉴스레터(웹 요약만 열람, PDF 본문 미열람).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s3.md",
        "docs/topics/2026/2026-09-30-area59-s4.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s8.md"
      ]
    },
    {
      "id": "ref-1244",
      "org": "법제처 찾기쉬운 생활법령정보",
      "title": "개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인)",
      "published": null,
      "url": "https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "개인정보 보호법 제25조의2와 같은 법 시행령(페이지가 드는 제22조·제27조의2)의 이동형 영상정보처리기기 정의, 공개된 장소 촬영 허용 요건, 촬영 사실 표시 방법을 설명하는 법제처 생활법령 페이지.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s3.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s10.md"
      ]
    },
    {
      "id": "ref-1245",
      "org": "대한민국 정책브리핑 (과학기술정보통신부)",
      "title": "'인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무",
      "published": "2026-01-21",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148958380",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "인공지능 기본법 2026-01-22 시행, 생성형 AI·딥페이크 표시, 고영향 AI 판단(사람의 최종 결정 권한 시 제외), 최소 1년 규제 유예, 지원데스크를 알린 정부 보도(2026-01-21).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s3.md",
        "docs/topics/2026/2026-09-30-area59-s4.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s10.md",
        "docs/topics/2026/2026-09-30-area59-s11.md"
      ]
    },
    {
      "id": "ref-1246",
      "org": "Open Robotics (ROS 2 Documentation)",
      "title": "ROS 2 developer guide",
      "published": null,
      "url": "https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "ROS 2 핵심 패키지 개발 규칙. 패키지마다 LICENSE 파일(대개 Apache 2.0)을 두고, 소스 파일마다 라이선스·저작권 문구를 넣어 자동 린터로 검사하게 한다. 공식 문서 저장소 원본을 열었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s3.md",
        "docs/topics/2026/2026-09-30-area59-s4.md",
        "docs/topics/2026/2026-09-30-area59-s6.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s10.md"
      ]
    },
    {
      "id": "ref-1247",
      "org": "고용노동부",
      "title": "산업용 로봇과 컨베이어도 안전검사 필수",
      "published": "2017-10-26",
      "url": "https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "2017-10-29부터 산업용 로봇·컨베이어를 안전검사 대상에 추가하고 기존 설비의 최초 검사 기한(2018-12-31)과 재해 통계를 밝힌 정부 보도자료. 정기검사 주기는 본문에 없다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s3.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s10.md"
      ]
    },
    {
      "id": "ref-1248",
      "org": "Commonwealth of Virginia (Code of Virginia)",
      "title": "§ 46.2-908.1:1. Personal delivery devices",
      "published": null,
      "url": "https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "버지니아주 개인 배송 장치(PDD)의 운행 장소, 속도(보도 10mph 이하), 운영자 식별 표시, 최소 10만 달러 일반배상책임 보험을 정한 주법 조문.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s3.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s10.md"
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
      "summary": "원문 미열람. EU 기계류 규정 원문. 실질적 변경을 한 자의 제조자 의무(제18조)와 2027-01-20 적용을 정한다. 이번 실행에서 다시 열지 않았다(58. 다사업자 책임·계약·데이터와 같은 id 재사용).",
      "source_unopened": true,
      "cited_by": [
        "docs/topics/2026/2026-09-30-area59-s4.md",
        "docs/topics/2026/2026-09-30-area59-s7.md",
        "docs/topics/2026/2026-09-30-area59-s10.md"
      ]
    },
    {
      "id": "ref-1212",
      "org": "European Agency for Safety and Health at Work (EU-OSHA)",
      "title": "Regulation 2023/1230/EU - machinery",
      "published": null,
      "url": "https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. EU 기계류 규정의 채택(2023-06-14)·적용(2027-01-20) 시점과 주요 내용을 소개하는 EU-OSHA 페이지. 리서치에서 다시 열지 않았다(58. 다사업자 책임·계약·데이터와 같은 id 재사용).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
        "docs/topics/2026/2026-09-30-area59-s7.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "한국 실외이동로봇 책임보험·공제의 최저 가입금액(사망·부상·재물 한도)을 정한 산업통상자원부령 조항과 금액은 무엇인가?",
      "areas": [
        59,
        66
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "EU 개정 제조물책임지침에서 여러 제조사 로봇에 명령을 내리는 오케스트레이션 소프트웨어는 결함 제품이나 관련 서비스로 다뤄지는가, 그 소프트웨어의 설정·기능 변경이 실질적 변경에 해당해 플랫폼 사업자가 제조자로 간주될 수 있는가?",
      "areas": [
        59,
        58
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 제조물책임법에 소프트웨어를 제조물로 포함하는 개정안이 발의되거나 통과되었는가, 그리고 로봇 관제·오케스트레이션 소프트웨어의 결함 사고에 관한 국내 판례가 있는가?",
      "areas": [
        59,
        58
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 오케스트레이션 플랫폼이 EU 사이버복원력법의 디지털 요소 제품 제조자에 해당하는가, 해당하면 로봇 제조사와 플랫폼 사업자 사이에 취약점 보고 의무를 어떻게 나누는가?",
      "areas": [
        59,
        52,
        57
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "시뮬레이션·가상 시운전에 쓰는 3D 자산(로봇 모델·건물 모델)의 라이선스와 저작자 표기를 자산 단위로 추적하는 표준 방법이 있으며, SPDX 로 3D 자산의 라이선스를 기술한 사례가 있는가?",
      "areas": [
        59,
        36,
        57
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#5-적용-사례-현장-유형-명시",
      "title": "59. 법·규제·보험·라이선스"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#5-적용-사례-현장-유형-명시",
      "title": "59. 법·규제·보험·라이선스"
    },
    {
      "site_type": "실외",
      "item": "예외·성과",
      "link": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#5-적용-사례-현장-유형-명시",
      "title": "59. 법·규제·보험·라이선스"
    }
  ],
  "standards_updates": [
    {
      "name": "지능형로봇법·도로교통법 개정(실외이동로봇 보도 통행·운용자 의무·보험 의무, 2023-11-17 시행)",
      "kind": "프레임워크",
      "org": "산업통상자원부·경찰청",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922726",
      "related_areas": [
        59,
        66
      ],
      "summary": "운행안전인증을 받은 질량 500kg 이하·15km/h 이하 실외이동로봇의 보도 통행을 허용하고, 운용자 의무·범칙금, 보도 운영자의 보험·공제 가입 의무를 둔 개정 법령.",
      "ref_id": "ref-991"
    },
    {
      "name": "버지니아주법 §46.2-908.1:1 개인 배송 장치(Personal Delivery Devices)",
      "kind": "프레임워크",
      "org": "Commonwealth of Virginia",
      "url": "https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/",
      "related_areas": [
        59,
        66
      ],
      "summary": "개인 배송 장치의 보도·횡단보도 속도(10mph 이하), 운영자 식별 표시, 최소 10만 달러 일반배상책임 보험을 정한 미국 주법 조문(해외 비교).",
      "ref_id": "ref-1248"
    },
    {
      "name": "EU 개정 제조물책임지침 (Directive (EU) 2024/2853)",
      "kind": "프레임워크",
      "org": "European Union (Gibson Dunn 해설 경유)",
      "url": "https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/",
      "related_areas": [
        59,
        58,
        57
      ],
      "summary": "2026-12-09 이후 출시·사용 개시 제품에 적용되며 독립형 소프트웨어를 제품에 포함하고 실질적 변경자를 제조자로 볼 수 있게 한다(법률사무소 해설 기준).",
      "ref_id": "ref-1235"
    },
    {
      "name": "한국 제조물책임법",
      "kind": "프레임워크",
      "org": "대한민국 (김·장 법률사무소 해설 경유)",
      "url": "https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930",
      "related_areas": [
        59,
        58
      ],
      "summary": "제조물을 제조되거나 가공된 동산으로 정의해 소프트웨어 기인 자율 시스템 사고의 개발자 책임이 쟁점으로 남아 있다(2024-07 기준).",
      "ref_id": "ref-1243"
    },
    {
      "name": "인공지능 기본법 (2026-01-22 시행)",
      "kind": "프레임워크",
      "org": "과학기술정보통신부",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148958380",
      "related_areas": [
        59,
        13,
        47
      ],
      "summary": "사람이 최종 의사결정 권한을 가지면 고영향 인공지능 분류에서 제외된다는 정부 설명과 최소 1년 이상 규제 유예, 지원데스크 운영을 알린 한국 AI 법(2026-01-21 발표 기준).",
      "ref_id": "ref-1245"
    },
    {
      "name": "EU 사이버복원력법(CRA) 보고 의무",
      "kind": "프레임워크",
      "org": "European Commission",
      "url": "https://digital-strategy.ec.europa.eu/en/policies/cra-reporting",
      "related_areas": [
        59,
        52,
        57
      ],
      "summary": "2026-09-11부터 디지털 요소 제품 제조자가 실제 악용되는 취약점과 중대 보안 사고를 유럽연합 사이버보안청(ENISA) 단일 보고 플랫폼으로 24시간·72시간·최종 보고하게 한다.",
      "ref_id": "ref-1236"
    },
    {
      "name": "산업안전보건법 안전검사 (산업용 로봇·컨베이어)",
      "kind": "프레임워크",
      "org": "고용노동부",
      "url": "https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135",
      "related_areas": [
        59,
        50
      ],
      "summary": "2017-10-29부터 산업용 로봇과 컨베이어를 안전검사 대상에 추가하고 기존 설비는 2018-12-31까지 최초 안전검사를 받게 했다. 정기 검사 주기는 미확인.",
      "ref_id": "ref-1247"
    },
    {
      "name": "ROS 2 개발자 가이드 (패키지 라이선스·저작권 규칙)",
      "kind": "오픈소스",
      "org": "Open Robotics (ROS 2 Documentation)",
      "url": "https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html",
      "related_areas": [
        59,
        57
      ],
      "summary": "LICENSE 파일(대개 Apache 2.0)을 패키지마다 두고, 소스 파일마다 라이선스·저작권 문구를 넣어 자동 린터로 검사한다.",
      "ref_id": "ref-1246"
    },
    {
      "name": "REP 2004 Package Quality Categories",
      "kind": "프레임워크",
      "org": "ROS (ros-infrastructure/rep)",
      "url": "https://ros.org/reps/rep-2004.html",
      "related_areas": [
        59,
        57
      ],
      "summary": "ROS 2 패키지 품질 수준 1~4에 선언된 라이선스와 저작권 명시·저자 표기를 요구하고 수준 5에는 권장한다.",
      "ref_id": "ref-1237"
    },
    {
      "name": "SPDX (ISO/IEC 5962:2021)",
      "kind": "표준",
      "org": "SPDX Project (Linux Foundation)",
      "url": "https://spdx.dev/about/overview/",
      "related_areas": [
        59,
        57
      ],
      "summary": "소프트웨어 자재명세서(SBOM)의 출처·라이선스·보안 정보를 교환하는 개방 표준이며, 라이선스 목록은 식별자·예외·표현식 문법을 제공한다.",
      "ref_id": "ref-1238"
    },
    {
      "name": "Gazebo(클래식) 모델 구조·요구사항 (모델 데이터베이스 라이선스 표기)",
      "kind": "오픈소스",
      "org": "Open Robotics (Gazebo Classic)",
      "url": "https://classic.gazebosim.org/tutorials?tut=model_structure",
      "related_areas": [
        59,
        36
      ],
      "summary": "database.config 의 license 요소로 모델 데이터베이스의 라이선스를 지정하고 CC BY 3.0 Unported를 권장하며, model.config 에 작성자 이름·이메일을 필수로 적게 한다.",
      "ref_id": "ref-1239"
    }
  ],
  "additional_research_requests": [
    "5절 한국 실외 사례의 '시작 조건'·'작업 대상'·'완료·인계' 칸: 실제 보도 배달·순찰 로봇 운영 사례(요청 발생, 수령 확인)를 다룬 출처가 브리프에 없어 '해당 없음'으로 두었다. 실외 도입 사례 조사가 필요하다.",
    "5절: 물류창고·제조 공장·병원·상업 시설·가정 현장의 법·규제·보험 적용 사례(예: 산업용 로봇 안전검사를 받은 제조 공장 사례, 병원 실내 배송 로봇 규정)를 찾지 못했다. 현장 유형을 밝힌 출처가 필요하다(oq-231 관련).",
    "7절 산업안전보건법 안전검사: 산업용 로봇 정기 안전검사 주기를 안전보건공단·법령 원문으로 확인해야 한다(검색 요약만 있음).",
    "5·11절: 실외이동로봇 책임보험·공제 최저 가입금액을 정한 시행규칙 원문과 단체보험 보장 한도를 확인해야 한다.",
    "5·11절 oq-186: 운행안전인증 심사항목이 16가지에서 8개로 바뀐 개정 고시와 시점 원문 확인이 필요하다.",
    "3·6·7절: EU 개정 제조물책임지침(2024/2853)은 법률사무소 해설 기준이다. EUR-Lex 원문(오픈소스 예외 조항 포함)을 열어 확인해야 한다.",
    "7절: 개인정보 보호법 제25조의2 시행일은 출처끼리 달라(2023-09-15·2024-12-03) 쓰지 않았다. 법령 원문으로 확인이 필요하다.",
    "11절 oq-275: 서비스 로봇 운영 인력의 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육 적용에 관한 근거가 이번 브리프에 없어 열린 질문 목록에만 올렸다.",
    "다음 실행 후보: 66. 실외 페이지에 실외이동로봇 규정(f1~f8), 57. 자산·소프트웨어 수명주기 관리 페이지에 라이선스 선언·SBOM(f17~f19) 반영을 검토한다."
  ],
  "fixes_applied": [
    "ref-991 제목 정정 — 13절 각주와 reference_updates 의 제목을 '‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용'으로 쓰고 '(제목 일부만 확인)'을 뺐다.",
    "ref-992·f6 정정 — 각주·reference_updates 제목을 '실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사'로 고치고, 5절 본문에서 행정예고 주체를 산업통상자원부로 쓰고 '(2023-07 행정예고안 기준)'을 밝혔다(reference 요약도 산업통상자원부로 고침).",
    "ref-1245·f13 정정 — 각주·reference_updates 의 발행일을 2026-01-21, 제목을 ''인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무'로 쓰고, 4·7·10·11절의 f13 문장에 '2026-01-21 발표 기준'을 붙였다.",
    "ref-1243·f11 정정 — 각주·reference_updates 제목을 '인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점', 발행일을 2024-07-05 로 쓰고, 3·7·8절의 쟁점 서술에 '2024-07 기준'을 붙였다.",
    "f4 강등 — 5절 예외·성과 칸에서 [추정]으로 쓰고 '한국로봇산업협회 발표를 전한 기사(ref-1240) 기준'과 '보장 한도는 미확인'을 함께 적었다.",
    "f5 재서술 — 4·5·7절에서 인증 대상을 '배송 등을 위해 자율주행(원격제어 포함)으로 운행하는 지능형 로봇과 그 운행에 필요한 관제장치의 조합'으로 쓰고 '일체'를 인용하지 않았다.",
    "f15 조항 표기 — 7절 이름 칸을 '개인정보 보호법 제25조의2와 같은 법 시행령(생활법령 페이지가 드는 제22조·제27조의2)'으로 쓰고 '시행령 제27조'와 시행일을 쓰지 않았다.",
    "f17 도구 이름 삭제 — 6·7절에서 'ament_copyright'를 빼고 '자동 린터로 검사한다'고만 썼다.",
    "f12 각주 — 7절에서 제18조(실질적 변경자의 제조자 간주) 문장에 ref-555, 적용일 문장에 ref-1212 각주를 붙이고 두 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙였으며, reference_updates 두 항목에 source_unopened: true 를 넣고 58. 다사업자 책임·계약·데이터와 같은 id 를 재사용한다고 밝혔다.",
    "f9·f10 기준 명시 — 3·4·6·7·8절의 EU 제조물책임지침 서술마다 'EUR-Lex 원문이 아니라 법률사무소 해설(Gibson Dunn, 2026-03-23) 기준'임을 적었다.",
    "f16 위치 — 5절 적용 사례에 넣지 않고 7절 '산업안전보건법 안전검사 (산업용 로봇·컨베이어)' 행으로만 썼다(9절 연계 대상 표기는 f23 근거).",
    "5절 현장 유형 — 두 사례 모두 '실외'로 쓰고, 버지니아 사례(f8)는 해외 비교 사례로 한국 현장에 바로 적용되지 않음을 밝혔으며, 물류창고·제조 공장·병원·상업 시설·가정 사례는 찾지 못했다고 적고, site_matrix_updates 는 실외 칸(수행 자원·제약·예외·성과)만 냈다.",
    "'오픈소스 소프트웨어 스튜어드' — glossary_updates 에 넣지 않았다.",
    "'제조물책임' 용어 정의 — '과실과 관계없이'를 빼고 f9·f11 이 뒷받침하는 범위(제조물 결함으로 생긴 손해의 배상 책임, 한국은 제조·가공된 동산, EU 개정 지침은 소프트웨어 포함)로 썼다.",
    "11절 — 기존 oq-143·oq-173·oq-186·oq-187·oq-231·oq-239·oq-249·oq-250·oq-262 를 모두 '열림'으로 두고 open_question_updates 로 상태를 바꾸지 않았으며, oq-186 에 2023-11-16 정책브리핑(ref-991)도 16가지 시험항목을 밝혔다는 점을 f6·f5 와 함께 적었다.",
    "2차: 11절 열린 질문 수 — 원 페이지 11절 요약 문장과 주제 페이지 2026-09-30-area59-s11 의 1·3절에서 '9건'을 '10건'으로 고치고, 3절 목록에 oq-275(상태: 열림)를 docs/open-questions.md 의 질문 문장 그대로 더했다(상태는 바꾸지 않아 open_question_updates 에는 넣지 않았다).",
    "2차: [의견] 출처 표시 — 원 페이지 4절 첫 문장, 주제 페이지 2026-09-30-area59-s4 의 1·3절 같은 문장, 주제 페이지 2026-09-30-area59-s3 3절의 '두 법제가 이렇게 다르기 때문에 … 아직 열린 문제다' 문장의 [의견] 앞에 '(구축자 의견)'을 붙였다.",
    "2차: 7절 첫 문장 각주 — 원 페이지 7절과 주제 페이지 2026-09-30-area59-s7 의 1·3절 문장에 ref-980·ref-1248·ref-1212·ref-1243·ref-1245·ref-1244·ref-1247·ref-1237·ref-1238·ref-1239 각주를 더하고 나열을 '한국의 제조물책임·AI·개인정보·산업안전 법령'으로 맞췄으며, 원 페이지 13절에 ref-1237·ref-1239·ref-1212(접근일 뒤 ' (원문 미열람)') 각주 정의를 reference_updates 와 같은 줄 형식으로 더했다. 원 페이지 프런트매터 sources 를 각주 정의와 맞추면서 원 페이지에서 인용하지 않는 ref-555 는 뺐고, reference_updates 의 cited_by 도 실제 인용 페이지 기준으로 고쳤다.",
    "2차: ROS 2 라이선스 규칙 표현 — 주제 페이지 2026-09-30-area59-s7 표의 'ROS 2 개발자 가이드 (라이선스 규칙)' 행과 standards_updates 같은 항목 summary 를 'LICENSE 파일(대개 Apache 2.0)을 패키지마다 두고, 소스 파일마다 라이선스·저작권 문구를 넣어 자동 린터로 검사한다'로 고쳤다(reference_updates 의 ref-1246 요약도 같은 뜻으로 맞췄다).",
    "2차: 약어 풀어쓰기 — 원 페이지 9절의 첫 'SBOM'을 '소프트웨어 자재명세서(Software Bill of Materials, SBOM)'로, 주제 페이지 s4·s7 의 첫 'ENISA'를 '유럽연합 사이버보안청(European Union Agency for Cybersecurity, ENISA)'으로 썼다. 주제 페이지 s6 에는 ENISA 가 나오지 않아 고칠 곳이 없었다. 같은 규칙에 따라 s6·s7·s10 본문에서 처음 나오는 SBOM 과 s8 의 ENISA 도 풀어 썼다.",
    "2차: 8절 문장 정리 — 원 페이지 8절과 주제 페이지 2026-09-30-area59-s8 의 1·3절 첫 문장을 '… 법률사무소 해설이 중심이다.'로 고쳐 그 문장만으로 끝나게 했다."
  ]
}
```

### runs/2026-09-30-23/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-30-23/pages/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md

```markdown
---
title: "59. 법·규제·보험·라이선스"
type: area
category: "P. 거버넌스·법규·사회"
area_no: 59
related_areas: [3, 4, 13, 16, 36, 47, 50, 52, 53, 57, 58, 66]
tags: [실외이동로봇 운행안전인증, 책임보험, 제조물책임, 사이버복원력법, SBOM, 오픈소스 라이선스]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-991, ref-1235, ref-1236, ref-1237, ref-1238, ref-1239, ref-1240, ref-980, ref-992, ref-1243, ref-1244, ref-1245, ref-1246, ref-1247, ref-1248, ref-1212]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [P. 거버넌스·법규·사회](index.md) › 59. 법·규제·보험·라이선스

# 59. 법·규제·보험·라이선스

!!! info "소속 대분류"
    [P. 거버넌스·법규·사회](index.md) — 핵심 질문:
    여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

법·규제 대응, 보험·사고 책임, 오픈소스·라이선스 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **법·규제 대응**: 기계류 규정·AI 규제·로봇 관련 법·개인정보 법·실외 로봇 운행 규정을 파악하고 대응한다
- **보험·사고 책임**: 사고 책임의 배분과 보험을 정한다
- **오픈소스·라이선스 관리**: 오픈소스·SDK·3D 자산의 라이선스를 지킨다

## 2. 핵심 질문

이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가? [분류원문]

## 3. 왜 중요한가

로봇을 운영할 때 지켜야 할 법·규제·보험·라이선스는 현장마다 달라 보이며, 이번 조사 범위에서는 실외의 운행 규정·운행안전인증·운용자 의무·의무 보험, 산업 사업장의 기계 안전 규제, 모든 현장에 걸치는 AI·사이버보안·개인정보 규제와 사고 책임 법제, 오픈소스·3D 자산 라이선스가 겹치는 구조로 보인다. [추정][^ref-991][^ref-980][^ref-1248][^ref-1247][^ref-1245][^ref-1236][^ref-1244][^ref-1235][^ref-1246]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 왜 중요한가](../../topics/2026/2026-09-30-area59-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 용어는 운행 조건을 정하는 인증·보험, 사고 뒤 책임을 정하는 제조물책임·실질적 변경, 운영 중 의무를 정하는 AI·보안 규제, 배포물의 권리를 정하는 라이선스 선언으로 나눠 볼 수 있다. (구축자 의견) [의견][^ref-980][^ref-1235][^ref-1236][^ref-1246]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area59-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 실외

**사례:** 한국 보도에서 실외이동로봇 운행

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 운행안전인증 대상은 배송 등을 위해 자율주행(원격제어 포함)으로 운행하는 지능형 로봇과 그 운행에 필요한 관제장치의 조합이다. [사실][^ref-980] 운용자는 로봇을 정확히 조작하고 안전하게 운용할 의무를 진다. [사실][^ref-991] |
| 제약 | 2023-11-17부터 운행안전인증을 받은 질량 500kg 이하·최고속도 15km/h 이하 실외이동로봇이 보행자 지위로 보도를 통행할 수 있다. [사실][^ref-991][^ref-980] 로봇도 신호위반·무단횡단 금지 같은 보행자 교통규칙을 지켜야 한다. [사실][^ref-991] 보도에서 운영하는 자는 인적·물적 손해 배상을 위한 보험 또는 공제에 가입해야 한다. [사실][^ref-991][^ref-1240] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 안전운용의무 위반에는 범칙금(3만원)을 부과할 수 있다. [사실][^ref-991] 한국로봇산업협회 발표를 전한 기사(ref-1240) 기준으로, 협회는 2024-02 실외이동로봇 손해배상책임 단체보험을 내놓아 로봇 1대당 약 500만원 수준이던 보험료를 30만원대로 낮췄다고 밝혔고 첫 가입 기업은 뉴빌리티·로보티즈였다. 보장 한도는 미확인이다. [추정][^ref-1240] |

정부는 한국로봇산업협회를 손해보장사업 실시기관으로 지정했다(2023-11-16 발표). [사실][^ref-991] 운행안전인증은 서류심사→제품심사→인증표시 순으로 진행되고 신청일부터 30일 이내에 처리되며, 현재 심사항목은 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치의 8개다(2026-09-30 확인). [사실][^ref-980]

제정 당시의 기준은 달랐다. 2023-07 산업통상자원부가 행정예고한 실외이동로봇 운행 안전기준은 16가지 항목으로, 질량별 속도 제한, 폭 80cm(보도 폭 250cm 이상이면 120cm), 5도 경사로 안정성, 비상정지, 장애물 회피, 횡단보도 신호 준수, 알림음 55~73dB, 등화장치 온도 60도 이하, 방수 IPX4 이상 등을 담았다(2023-07 행정예고안 기준). [사실][^ref-992] 두 자료를 비교하면 심사 체계가 16가지 안전기준에서 현재 8개 심사항목으로 재편된 것으로 보이나, 개정 시점·근거 고시와 알림음·등화장치·경사로 같은 기존 기준이 어느 항목에 흡수됐는지는 확인하지 못했다. [추정][^ref-980][^ref-992]

**현장 유형:** 실외

**사례:** 미국 버지니아주에서 개인 배송 장치를 보도로 운행 (해외 비교)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 장치에 운영자를 식별하는 표시를 단다. [사실][^ref-1248] |
| 제약 | [개인 배송 장치](../../glossary/personal-delivery-device.md)(Personal Delivery Device, PDD)는 보도·횡단보도에서 시속 10마일 이하로 운행한다. [사실][^ref-1248] 운영자는 장치 운행으로 생긴 손해에 대해 최소 10만 달러의 일반배상책임 보험을 유지해야 한다. [사실][^ref-1248] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

이 사례는 버지니아주법 §46.2-908.1:1 기준이며(2026-09-30 확인), 지방정부는 추가 안전 요건을 둘 수 있다. [사실][^ref-1248] 미국 주법이므로 한국 현장에 바로 적용되지 않으며, 한국 사례와 운행 속도·보험 요구를 비교하는 해외 비교 사례로만 둔다.

이번 조사에서 근거를 찾은 현장 유형은 실외뿐이다. 물류창고·제조 공장·병원·상업 시설·가정의 사례는 이번 조사에서 찾지 못했다.

## 6. 대표 접근법과 기술

확인한 자료로 보면 이 영역의 대응 수단은 인증·보험 조건을 운영 제약으로 반영하는 것, 사고·취약점 보고와 증거 기록을 갖추는 것, 라이선스를 선언하고 자동으로 검사하는 것의 세 갈래로 보인다. [추정][^ref-980][^ref-1236][^ref-1246]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area59-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이번 조사로 확인한 규범은 한국 실외 로봇 법령과 운행안전인증, 해외 실외 배송 로봇 주법, EU의 제조물 책임·기계·사이버보안 규범, 한국의 제조물책임·AI·개인정보·산업안전 법령, ROS 2·SPDX·Gazebo의 라이선스 규칙이다. [사실][^ref-991][^ref-980][^ref-1248][^ref-1235][^ref-1212][^ref-1236][^ref-1243][^ref-1245][^ref-1244][^ref-1247][^ref-1246][^ref-1237][^ref-1238][^ref-1239]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area59-s7.md)에 있다.

## 8. 대표 연구와 자료

이번 조사에서 모은 자료는 학술 논문보다 정부·집행기관의 1차 자료와 법률사무소 해설이 중심이다.

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 대표 연구와 자료](../../topics/2026/2026-09-30-area59-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 업종별 조건 | 로봇별 인증·보험 상태와 인증 조건(관제장치 조합, 속도·질량·운행 구역)을 등록 정보와 작업·경로 제약으로 반영하고, 촬영 표시 같은 규제 상태를 운영 조건으로 확인한다. [추정][^ref-980][^ref-991][^ref-1244] | 인증 취득과 법적 적합성 판단(제조사·운영자), 보험 계약과 보상(운영자·보험사·협회), 제조물 책임 판정(당사자·법원), 개인정보 처리 적법성 판단(개인정보처리자)은 연계 대상으로 보인다. [추정][^ref-980][^ref-1240][^ref-1243][^ref-1235][^ref-1244] |
| 시설·설비 제어 | 사업장 안전검사 결과를 받아 작업·경로·권한 제약으로 반영한다. [추정][^ref-1247] | 산업용 로봇 안전검사는 사업주가 맡는 연계 대상으로 보인다. [추정][^ref-1247] |

분류 원문 19장의 [범위 경계](../../about/scope-boundary.md)는 업종별 조건에서 ROP가 "해당 조건을 작업·경로·권한 제약으로 반영"한다고 정한다. 이 영역에서 ROP는 법적 판단을 내리지 않고 그 결과를 받아 반영하며 근거 기록을 제공하는 쪽인 것으로 보인다. [추정][^ref-980][^ref-1247] 그 밖에 사고·취약점 보고와 책임 판단에 필요한 실행 기록을 남기는 일과 플랫폼 배포물의 라이선스·소프트웨어 자재명세서(Software Bill of Materials, SBOM) 목록을 관리하는 일은 ROP 직접 범위로 보인다. [추정][^ref-1236][^ref-1238][^ref-1246] 오케스트레이션 계층이 운행안전인증상 관제장치에 해당하면 경계가 달라질 수 있으나, 이에 대한 기준은 확인되지 않았다(oq-187).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 안전 인증, 개인정보·보안, 수명주기, 다사업자 책임, 실외 현장 영역과 두루 이어지는 것으로 보인다. [추정][^ref-980][^ref-1244][^ref-1236][^ref-1235]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area59-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 기존 열린 질문 10건은 이번 실행에서 해결되지 않아 모두 열림으로 두고, 새 질문 5건을 올린다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 열린 질문](../../topics/2026/2026-09-30-area59-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-1235]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1236]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-1238]: SPDX Project (Linux Foundation), SPDX Overview, 미확인, https://spdx.dev/about/overview/, 접근일 2026-09-30
[^ref-1240]: 지디넷코리아, "실외 이동로봇 필수보험 94% 저렴하게", 2024-02-08, https://zdnet.co.kr/view/?no=20240208201432, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1243]: 김·장 법률사무소, 인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점, 2024-07-05, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930, 접근일 2026-09-30
[^ref-1244]: 법제처 찾기쉬운 생활법령정보, 개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인), 미확인, https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3, 접근일 2026-09-30
[^ref-1245]: 대한민국 정책브리핑 (과학기술정보통신부), '인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무, 2026-01-21, https://www.korea.kr/news/policyNewsView.do?newsId=148958380, 접근일 2026-09-30
[^ref-1246]: Open Robotics (ROS 2 Documentation), ROS 2 developer guide, 미확인, https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html, 접근일 2026-09-30
[^ref-1247]: 고용노동부, 산업용 로봇과 컨베이어도 안전검사 필수, 2017-10-26, https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135, 접근일 2026-09-30
[^ref-1248]: Commonwealth of Virginia (Code of Virginia), § 46.2-908.1:1. Personal delivery devices, 미확인, https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/, 접근일 2026-09-30
[^ref-1237]: ROS (ros-infrastructure/rep), REP 2004 -- Package Quality Categories, 2019-12-17, https://ros.org/reps/rep-2004.html, 접근일 2026-09-30
[^ref-1239]: Open Robotics (Gazebo Classic), Gazebo : Tutorial : Model structure and requirements, 미확인, https://classic.gazebosim.org/tutorials?tut=model_structure, 접근일 2026-09-30
[^ref-1212]: European Agency for Safety and Health at Work (EU-OSHA), Regulation 2023/1230/EU - machinery, 미확인, https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery, 접근일 2026-09-30 (원문 미열람)
```

### docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md

```markdown
---
title: "59. 법·규제·보험·라이선스"
type: area
category: "P. 거버넌스·법규·사회"
area_no: 59
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [P. 거버넌스·법규·사회](index.md) › 59. 법·규제·보험·라이선스

# 59. 법·규제·보험·라이선스

!!! info "소속 대분류"
    [P. 거버넌스·법규·사회](index.md) — 핵심 질문:
    여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

법·규제 대응, 보험·사고 책임, 오픈소스·라이선스 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **법·규제 대응**: 기계류 규정·AI 규제·로봇 관련 법·개인정보 법·실외 로봇 운행 규정을 파악하고 대응한다
- **보험·사고 책임**: 사고 책임의 배분과 보험을 정한다
- **오픈소스·라이선스 관리**: 오픈소스·SDK·3D 자산의 라이선스를 지킨다

## 2. 핵심 질문

이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가? [분류원문]

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

### runs/2026-09-30-23/pages/topics/2026/2026-09-30-area59-s7.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 47, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-991, ref-1235, ref-1236, ref-1237, ref-1238, ref-1239, ref-980, ref-1243, ref-1244, ref-1245, ref-1246, ref-1247, ref-1248, ref-555, ref-1212]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#7
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 관련 표준·프레임워크·오픈소스

# 59. 법·규제·보험·라이선스 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 조사로 확인한 규범은 한국 실외 로봇 법령과 운행안전인증, 해외 실외 배송 로봇 주법, EU의 제조물 책임·기계·사이버보안 규범, 한국의 제조물책임·AI·개인정보·산업안전 법령, ROS 2·SPDX·Gazebo의 라이선스 규칙이다. [사실][^ref-991][^ref-980][^ref-1248][^ref-1235][^ref-1212][^ref-1236][^ref-1243][^ref-1245][^ref-1244][^ref-1247][^ref-1246][^ref-1237][^ref-1238][^ref-1239]
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 조사로 확인한 규범은 한국 실외 로봇 법령과 운행안전인증, 해외 실외 배송 로봇 주법, EU의 제조물 책임·기계·사이버보안 규범, 한국의 제조물책임·AI·개인정보·산업안전 법령, ROS 2·SPDX·Gazebo의 라이선스 규칙이다. [사실][^ref-991][^ref-980][^ref-1248][^ref-1235][^ref-1212][^ref-1236][^ref-1243][^ref-1245][^ref-1244][^ref-1247][^ref-1246][^ref-1237][^ref-1238][^ref-1239]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| 지능형로봇법·도로교통법 개정(실외이동로봇) | 프레임워크(법령) | 2023-11-17 시행으로 운행안전인증 실외이동로봇의 보도 통행, 운용자 의무와 범칙금, 보도 운영자의 보험·공제 가입 의무를 두었다. [사실][^ref-991] | 정책브리핑(2023-11-16) |
| [실외이동로봇 운행안전인증](../../glossary/outdoor-mobile-robot-operational-safety-certification.md) | 평가 프로그램 | 지능형로봇법 제40조의2에 근거하며 인증 대상(로봇과 관제장치의 조합)·8개 심사항목·30일 이내 처리를 정한다(2026-09-30 확인). [사실][^ref-980] | 한국로봇산업진흥원 |
| 버지니아주법 §46.2-908.1:1 (개인 배송 장치) | 프레임워크(법령) | 보도·횡단보도 10mph 이하, 운영자 식별 표시, 최소 10만 달러 일반배상책임 보험을 정한 해외 비교 사례다(2026-09-30 확인). [사실][^ref-1248] | Code of Virginia |
| EU 개정 제조물책임지침 (Directive (EU) 2024/2853) | 프레임워크(법령) | 2026-12-09 이후 출시·사용 개시 제품에 적용되고 독립형 소프트웨어를 제품에 포함하며 실질적 변경자를 제조자로 볼 수 있게 한다(EUR-Lex 원문이 아니라 법률사무소 해설(Gibson Dunn, 2026-03-23) 기준). [사실][^ref-1235] | Gibson Dunn |
| 한국 제조물책임법 | 프레임워크(법령) | 제조물을 제조되거나 가공된 동산으로 정의해, 소프트웨어 기인 자율 시스템 사고에서 개발자의 책임이 쟁점으로 남아 있다(2024-07 기준). [사실][^ref-1243] | 김·장 법률사무소(2024-07-05) |
| EU 기계류 규정 (Regulation (EU) 2023/1230) | 프레임워크(법령) | 2023-06-14 채택, 2027-01-20부터 적용된다. [사실][^ref-1212] 출시된 기계에 실질적 변경을 한 자를 제조자로 보아 제조자 의무를 지게 한다(제18조). [사실][^ref-555] [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)와 같은 출처를 쓴다. | EUR-Lex·EU-OSHA (원문 미열람) |
| 인공지능 기본법 | 프레임워크(법령) | 2026-01-22 시행. 정부는 최종 의사결정 권한을 사람이 가지면 고영향 인공지능 분류에서 제외된다고 설명하고, 과태료 등 규제를 최소 1년 이상 유예하며 지원데스크를 운영한다고 밝혔다(2026-01-21 발표 기준). [사실][^ref-1245] | 과학기술정보통신부 |
| EU 사이버복원력법 보고 의무 | 프레임워크(법령) | 2026-09-11부터 제조자는 실제 악용되는 취약점과 중대한 보안 사고를 유럽연합 사이버보안청(European Union Agency for Cybersecurity, ENISA) 단일 보고 플랫폼으로 24시간 조기 경보·72시간 통지·최종 보고해야 한다. [사실][^ref-1236] | European Commission |
| 개인정보 보호법 제25조의2와 같은 법 시행령(생활법령 페이지가 드는 제22조·제27조의2) | 프레임워크(법령) | 착용형·휴대형·부착·거치형 [이동형 영상정보처리기기](../../glossary/mobile-video-information-processing-device.md)로 공개된 장소에서 사람을 촬영할 때 불빛·소리·안내판·안내방송 등으로 촬영 사실을 표시하게 하고, 표시했는데 거부 의사가 없는 경우 등에 한해 촬영을 허용한다. [사실][^ref-1244] | 법제처 생활법령 |
| 산업안전보건법 안전검사 (산업용 로봇·컨베이어) | 프레임워크(법령) | 고용노동부는 2017-10-29부터 산업용 로봇과 컨베이어를 산업안전보건법상 안전검사 대상에 추가해, 이미 쓰던 설비는 2018-12-31까지 최초 안전검사를 받게 했고, 그 근거로 최근 5년간 산업용 로봇 재해자 221명을 들었다. [사실][^ref-1247] 정기 검사 주기는 미확인이다. | 고용노동부(2017-10-26) |
| ROS 2 개발자 가이드 (라이선스 규칙) | 오픈소스 | LICENSE 파일(대개 Apache 2.0)을 패키지마다 두고, 소스 파일마다 라이선스·저작권 문구를 넣어 자동 린터로 검사한다. [사실][^ref-1246] | ROS 2 Documentation |
| REP 2004 Package Quality Categories | 프레임워크 | 2019-12-17 작성(Active). 품질 수준 1~4 패키지에 선언된 라이선스와 프로젝트 안의 저작권 명시·모든 저자 표기를 요구하고, 수준 5에는 권장만 한다. [사실][^ref-1237] | ROS REP |
| SPDX (ISO/IEC 5962:2021) | 표준 | 소프트웨어 자재명세서(Software Bill of Materials, SBOM)의 출처·라이선스·보안 정보를 교환하는 개방 표준이며, SPDX 라이선스 목록은 라이선스 식별자·예외·라이선스 표현식 문법을 제공한다. [사실][^ref-1238] | SPDX Project |
| Gazebo(클래식) 모델 데이터베이스 규칙 | 오픈소스 | database.config 의 license 요소로 데이터베이스 안 모델의 라이선스를 지정하고 CC BY 3.0 Unported를 권장하며, 각 모델의 model.config 에 작성자 이름·이메일을 필수로 적게 한다. [사실][^ref-1239] | Open Robotics |

전체 표준·프레임워크 목록은 [표준 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-1235]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1236]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-1237]: ROS (ros-infrastructure/rep), REP 2004 -- Package Quality Categories, 2019-12-17, https://ros.org/reps/rep-2004.html, 접근일 2026-09-30
[^ref-1238]: SPDX Project (Linux Foundation), SPDX Overview, 미확인, https://spdx.dev/about/overview/, 접근일 2026-09-30
[^ref-1239]: Open Robotics (Gazebo Classic), Gazebo : Tutorial : Model structure and requirements, 미확인, https://classic.gazebosim.org/tutorials?tut=model_structure, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-1243]: 김·장 법률사무소, 인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점, 2024-07-05, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930, 접근일 2026-09-30
[^ref-1244]: 법제처 찾기쉬운 생활법령정보, 개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인), 미확인, https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3, 접근일 2026-09-30
[^ref-1245]: 대한민국 정책브리핑 (과학기술정보통신부), '인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무, 2026-01-21, https://www.korea.kr/news/policyNewsView.do?newsId=148958380, 접근일 2026-09-30
[^ref-1246]: Open Robotics (ROS 2 Documentation), ROS 2 developer guide, 미확인, https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html, 접근일 2026-09-30
[^ref-1247]: 고용노동부, 산업용 로봇과 컨베이어도 안전검사 필수, 2017-10-26, https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135, 접근일 2026-09-30
[^ref-1248]: Commonwealth of Virginia (Code of Virginia), § 46.2-908.1:1. Personal delivery devices, 미확인, https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/, 접근일 2026-09-30
[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)
[^ref-1212]: European Agency for Safety and Health at Work (EU-OSHA), Regulation 2023/1230/EU - machinery, 미확인, https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-23 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-23 | 59. 법·규제·보험·라이선스 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-23/pages/topics/2026/2026-09-30-area59-s11.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 열린 질문"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 47, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-991, ref-980, ref-992, ref-1245]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#11
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 열린 질문

# 59. 법·규제·보험·라이선스 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에 걸린 기존 열린 질문 10건은 이번 실행에서 해결되지 않아 모두 열림으로 두고, 새 질문 5건을 올린다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에 걸린 기존 열린 질문 10건은 이번 실행에서 해결되지 않아 모두 열림으로 두고, 새 질문 5건을 올린다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-143** (상태: 열림) ROP 의 로봇 대화 기능이 국내 인공지능 기본법의 고영향 인공지능이나 EU AI Act 의 고위험 AI 시스템에 해당하는지, 해당한다면 대화 기록 자동 로그의 항목과 보존 기간을 어떻게 정해야 하는가? 정부는 사람이 최종 의사결정 권한을 가지면 고영향 분류에서 제외된다고 설명했으나(2026-01-21 발표 기준), 이것은 부분 근거에 그친다. [사실][^ref-1245]
- **oq-173** (상태: 열림) 국가기술표준원이 2021년 제정을 발표한 로봇의 승강기 탑승 안전 요구사항 KS 와 실내 배송 로봇 KS 의 표준 번호·조항은 무엇이며, 그 요구(속도 제어·보호 정지·높낮이차·틈새)가 승강기 연동 계층에 어떤 정보를 요구하는가?
- **oq-186** (상태: 열림) 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시는 무엇이며, 경사로·알림음·등화장치 같은 기존 항목은 어느 항목에 흡수됐는가? 2023-07 행정예고안은 16가지 기준을 담았고 [사실][^ref-992], 2023-11-16 정책브리핑도 16가지 시험항목을 밝혔으나 [사실][^ref-991], 인증기관 안내는 현재 8개 항목을 나열한다(2026-09-30 확인). [사실][^ref-980] 개정 시점과 흡수 관계는 확인하지 못했다.
- **oq-187** (상태: 열림) 운행안전인증 대상이 로봇과 관제장치의 조합인데, 제조사가 다른 실외 로봇을 하나의 오케스트레이션 계층에서 지시할 때 그 계층이 인증상 관제장치에 해당하는지, 재인증이 필요한지에 관한 기준이나 해석이 있는가?
- **oq-231** (상태: 열림) 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가?
- **oq-239** (상태: 열림) 병원의 특수 물품(마약류·검체 등) 로봇 배송 이력처럼 보관 의무가 걸릴 수 있는 실행 기록의 보관 기간과 무결성 요건을 국내 법령·지침이 정하고 있는가?
- **oq-249** (상태: 열림) EU 기계류 규정의 개입 증거 기록·안전 소프트웨어 추적 로그 요구가 개별 기계 밖에서 여러 로봇을 지시하는 오케스트레이션 플랫폼에도 미치는가, 미친다면 기록 책임은 누구에게 있는가?
- **oq-250** (상태: 열림) KISA 로봇 보안모델(고도화)과 사이버보안 요구사항 해설서는 로봇 통신 암호화·감사 기록·원격 업데이트에 어떤 요구 항목을 두며 다중 로봇 관제 플랫폼을 대상에 포함하는가?
- **oq-262** (상태: 열림) 유럽데이터보호이사회(European Data Protection Board, EDPB) 영상 장치 지침 3/2019 를 이동 로봇 카메라에 적용한 유럽 감독기관의 결정이나 해석 사례가 있으며, 보존 기간 권고는 무엇인가?
- **oq-275** (상태: 열림) 서비스 로봇(서빙·배송·조리 로봇)을 운영하는 인력에게 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육이 실제로 어떻게 적용되며, 고용노동부 지침이나 사례가 있는가?
- (새 질문, 상태: 열림) 한국 실외이동로봇 책임보험·공제의 최저 가입금액(사망·부상·재물 한도)을 정한 산업통상자원부령 조항과 금액은 무엇인가?
- (새 질문, 상태: 열림) EU 개정 제조물책임지침에서 여러 제조사 로봇에 명령을 내리는 오케스트레이션 소프트웨어는 결함 제품이나 관련 서비스로 다뤄지는가, 그 소프트웨어의 설정·기능 변경이 실질적 변경에 해당해 플랫폼 사업자가 제조자로 간주될 수 있는가?
- (새 질문, 상태: 열림) 국내 제조물책임법에 소프트웨어를 제조물로 포함하는 개정안이 발의되거나 통과되었는가, 그리고 로봇 관제·오케스트레이션 소프트웨어의 결함 사고에 관한 국내 판례가 있는가?
- (새 질문, 상태: 열림) 로봇 오케스트레이션 플랫폼이 EU 사이버복원력법의 디지털 요소 제품 제조자에 해당하는가, 해당하면 로봇 제조사와 플랫폼 사업자 사이에 취약점 보고 의무를 어떻게 나누는가?
- (새 질문, 상태: 열림) 시뮬레이션·가상 시운전에 쓰는 3D 자산(로봇 모델·건물 모델)의 라이선스와 저작자 표기를 자산 단위로 추적하는 표준 방법이 있으며, SPDX 로 3D 자산의 라이선스를 기술한 사례가 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1245]: 대한민국 정책브리핑 (과학기술정보통신부), '인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무, 2026-01-21, https://www.korea.kr/news/policyNewsView.do?newsId=148958380, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-23 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-23 | 59. 법·규제·보험·라이선스 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-23/pages/topics/2026/2026-09-30-area59-s4.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 핵심 개념과 용어"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 47, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-991, ref-1235, ref-1236, ref-1238, ref-1240, ref-980, ref-1243, ref-1245, ref-1246, ref-555]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#4
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 핵심 개념과 용어

# 59. 법·규제·보험·라이선스 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 용어는 운행 조건을 정하는 인증·보험, 사고 뒤 책임을 정하는 제조물책임·실질적 변경, 운영 중 의무를 정하는 AI·보안 규제, 배포물의 권리를 정하는 라이선스 선언으로 나눠 볼 수 있다. (구축자 의견) [의견][^ref-980][^ref-1235][^ref-1236][^ref-1246]
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 용어는 운행 조건을 정하는 인증·보험, 사고 뒤 책임을 정하는 제조물책임·실질적 변경, 운영 중 의무를 정하는 AI·보안 규제, 배포물의 권리를 정하는 라이선스 선언으로 나눠 볼 수 있다. (구축자 의견) [의견][^ref-980][^ref-1235][^ref-1236][^ref-1246]

- **[실외이동로봇 운행안전인증](../../glossary/outdoor-mobile-robot-operational-safety-certification.md)(Outdoor Mobile Robot Operational Safety Certification)** — 지능형로봇법 제40조의2에 근거한 인증으로, 대상은 배송 등을 위해 자율주행(원격제어 포함)으로 운행하는 지능형 로봇과 그 운행에 필요한 관제장치의 조합이다. [사실][^ref-980]
- **운용자** — 개정 도로교통법에서 실외이동로봇을 조작·관리하며 정확한 조작과 안전한 운용 의무를 지는 사람이다. [사실][^ref-991]
- **책임보험·공제** — 운행안전인증을 받은 실외이동로봇을 보도에서 운영하는 자가 인적·물적 손해 배상을 위해 가입해야 하는 보험 또는 공제다. [사실][^ref-991][^ref-1240]
- **제조물책임(Product Liability)** — 제조물 결함으로 생긴 손해의 배상 책임을 정하는 제도로, 한국 제조물책임법은 제조물을 제조되거나 가공된 동산으로 정의한다. [사실][^ref-1243] EU 개정 지침은 독립형 소프트웨어를 제품에 포함한다(EUR-Lex 원문이 아니라 법률사무소 해설(Gibson Dunn, 2026-03-23) 기준). [사실][^ref-1235]
- **실질적 변경(Substantial Modification)** — 출시 뒤 제품이나 기계를 실질적으로 바꾼 자를 제조자로 볼 수 있게 하는 개념으로, EU 개정 제조물책임지침(법률사무소 해설 기준)과 EU 기계류 규정에 모두 있다. [사실][^ref-1235][^ref-555]
- **[고영향 인공지능](../../glossary/high-impact-ai.md)(High-impact AI)** — 한국 인공지능 기본법의 규제 분류로, 정부는 최종 의사결정 권한을 사람이 가지면 이 분류에서 제외된다고 설명했다(2026-01-21 발표 기준). [사실][^ref-1245]
- **사이버복원력법 보고 의무(Cyber Resilience Act, CRA)** — 디지털 요소 제품의 제조자가 실제 악용되는 취약점과 중대한 보안 사고를 유럽연합 사이버보안청(European Union Agency for Cybersecurity, ENISA) 단일 보고 플랫폼으로 알리는 의무로, 2026-09-11 시작됐다. [사실][^ref-1236]
- **소프트웨어 자재명세서(Software Bill of Materials, SBOM)와 SPDX** — SPDX는 SBOM의 출처·라이선스·보안 정보를 교환하는 개방 표준이며 ISO/IEC 5962:2021로 인정되었다. [사실][^ref-1238]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-1235]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1236]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-1238]: SPDX Project (Linux Foundation), SPDX Overview, 미확인, https://spdx.dev/about/overview/, 접근일 2026-09-30
[^ref-1240]: 지디넷코리아, "실외 이동로봇 필수보험 94% 저렴하게", 2024-02-08, https://zdnet.co.kr/view/?no=20240208201432, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-1243]: 김·장 법률사무소, 인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점, 2024-07-05, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930, 접근일 2026-09-30
[^ref-1245]: 대한민국 정책브리핑 (과학기술정보통신부), '인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무, 2026-01-21, https://www.korea.kr/news/policyNewsView.do?newsId=148958380, 접근일 2026-09-30
[^ref-1246]: Open Robotics (ROS 2 Documentation), ROS 2 developer guide, 미확인, https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html, 접근일 2026-09-30
[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-23 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-23 | 59. 법·규제·보험·라이선스 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-23/pages/topics/2026/2026-09-30-area59-s6.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 대표 접근법과 기술"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 47, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-991, ref-1235, ref-1236, ref-1238, ref-1239, ref-980, ref-1246]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#6
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 대표 접근법과 기술

# 59. 법·규제·보험·라이선스 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 확인한 자료로 보면 이 영역의 대응 수단은 인증·보험 조건을 운영 제약으로 반영하는 것, 사고·취약점 보고와 증거 기록을 갖추는 것, 라이선스를 선언하고 자동으로 검사하는 것의 세 갈래로 보인다. [추정][^ref-980][^ref-1236][^ref-1246]
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

확인한 자료로 보면 이 영역의 대응 수단은 인증·보험 조건을 운영 제약으로 반영하는 것, 사고·취약점 보고와 증거 기록을 갖추는 것, 라이선스를 선언하고 자동으로 검사하는 것의 세 갈래로 보인다. [추정][^ref-980][^ref-1236][^ref-1246]

### 인증·보험 조건을 운영 제약으로 반영

운행안전인증의 대상이 로봇 단독이 아니라 로봇과 그 운행에 필요한 관제장치의 조합이다. [사실][^ref-980] 그래서 로봇별 인증 여부·인증 조건(관제장치 조합, 속도·질량, 운행 구역)과 보험·공제 가입 상태를 등록 정보와 작업·경로 제약으로 관리하는 방식이 가능해 보인다. [추정][^ref-980][^ref-991] 여러 제조사 로봇을 지시하는 오케스트레이션 계층이 인증상 관제장치에 해당하는지는 확인되지 않았다(oq-187).

### 사고·취약점 보고와 증거 기록

EU 개정 제조물책임지침에서는 결함 있는 소프트웨어나 필요한 보안 업데이트 미제공도 책임 원인이 될 수 있고, 청구인이 그럴듯한 청구를 하면 피고에게 증거 공개를 명할 수 있으며, 공개 의무 불이행 등의 경우 결함이 추정된다. [사실][^ref-1235] 이 서술은 EUR-Lex 원문이 아니라 법률사무소 해설(Gibson Dunn, 2026-03-23) 기준이다. EU 사이버복원력법의 보고는 24시간 안 조기 경보, 72시간 안 통지, 최종 보고(취약점은 수정 조치 후 14일, 중대 사고는 1개월)의 세 단계다. [사실][^ref-1236] 이 기한 안에 보고하고 결함 추정에 대응하려면 실행·변경·업데이트 기록을 남겨 두는 설계가 필요해 보인다. [추정][^ref-1236][^ref-1235]

### 라이선스 선언·자동 검사·SBOM

ROS 2 개발자 가이드는 각 패키지에 LICENSE 파일(대개 Apache 2.0, 기존 허용형 라이선스가 있으면 예외)을 두고 모든 소스 파일에 라이선스·저작권 문구를 넣어 자동 린터로 검사하게 한다. [사실][^ref-1246] 3D 자산은 Gazebo(클래식) 규칙이 모델 데이터베이스 단위로 라이선스를 지정하고, 개별 모델 설정 파일(model.config)에는 라이선스 필드를 요구하지 않는다. [사실][^ref-1239] 따라서 시뮬레이션 자산은 모델 단위 라이선스 추적에 공백이 생길 수 있어 보인다. [추정][^ref-1239] 이렇게 모은 라이선스 정보는 SPDX 같은 소프트웨어 자재명세서(Software Bill of Materials, SBOM) 교환 표준으로 목록화할 수 있다. [추정][^ref-1238]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-1235]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1236]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-1238]: SPDX Project (Linux Foundation), SPDX Overview, 미확인, https://spdx.dev/about/overview/, 접근일 2026-09-30
[^ref-1239]: Open Robotics (Gazebo Classic), Gazebo : Tutorial : Model structure and requirements, 미확인, https://classic.gazebosim.org/tutorials?tut=model_structure, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-1246]: Open Robotics (ROS 2 Documentation), ROS 2 developer guide, 미확인, https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-23 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-23 | 59. 법·규제·보험·라이선스 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-23/pages/topics/2026/2026-09-30-area59-s10.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 다른 연구영역과의 연결"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 47, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-991, ref-1235, ref-1236, ref-1237, ref-1238, ref-1239, ref-1240, ref-980, ref-992, ref-1244, ref-1245, ref-1246, ref-1247, ref-1248, ref-555]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#10
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 다른 연구영역과의 연결

# 59. 법·규제·보험·라이선스 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 안전 인증, 개인정보·보안, 수명주기, 다사업자 책임, 실외 현장 영역과 두루 이어지는 것으로 보인다. [추정][^ref-980][^ref-1244][^ref-1236][^ref-1235]
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 안전 인증, 개인정보·보안, 수명주기, 다사업자 책임, 실외 현장 영역과 두루 이어지는 것으로 보인다. [추정][^ref-980][^ref-1244][^ref-1236][^ref-1235]

- [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) — 실외이동로봇 의무 보험의 보험료가 도입 비용에 들어간다. [추정][^ref-1240]
- [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) — 로봇과 관제장치의 조합으로 주어지는 인증 정보를 등록 정보로 담아야 한다. [추정][^ref-980]
- [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) — 사람이 최종 결정 권한을 가지면 고영향 인공지능에서 제외된다는 정부 설명(2026-01-21 발표 기준)이 대화형 지시의 승인 설계와 맞물린다. [추정][^ref-1245]
- [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 보도 폭·경사로·횡단보도 같은 운행 기준이 장소 의미 정보로 들어간다. [추정][^ref-992]
- [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) — 시뮬레이션에 쓰는 3D 자산의 라이선스 표기를 지켜야 한다. [추정][^ref-1239]
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 인공지능 기본법 대응이 AI 모델 운영 체계에 걸린다. [추정][^ref-1245]
- [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) — 운행안전인증과 산업용 로봇 안전검사가 안전 인증 체계에 속한다. [추정][^ref-980][^ref-1247]
- [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) — 사이버복원력법의 취약점·사고 보고가 위협 관리·감사와 이어진다. [추정][^ref-1236]
- [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) — 이동형 영상정보처리기기의 촬영 표시 의무가 로봇 카메라 운영에 걸린다. [추정][^ref-1244]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 라이선스 선언·소프트웨어 자재명세서(Software Bill of Materials, SBOM)와 보안 업데이트 책임이 소프트웨어 수명주기에 걸린다. [추정][^ref-1246][^ref-1237][^ref-1238][^ref-1235]
- [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) — 실질적 변경자를 제조자로 보는 규정이 사업자 사이 책임 배분과 이어진다. [추정][^ref-1235][^ref-555]
- [66. 실외](../../categories/site-type-applications/outdoor.md) — 한국 보도 통행 규정과 미국 주법의 개인 배송 장치 규정이 실외 현장의 요구다. [추정][^ref-991][^ref-1248]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-1235]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1236]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-1237]: ROS (ros-infrastructure/rep), REP 2004 -- Package Quality Categories, 2019-12-17, https://ros.org/reps/rep-2004.html, 접근일 2026-09-30
[^ref-1238]: SPDX Project (Linux Foundation), SPDX Overview, 미확인, https://spdx.dev/about/overview/, 접근일 2026-09-30
[^ref-1239]: Open Robotics (Gazebo Classic), Gazebo : Tutorial : Model structure and requirements, 미확인, https://classic.gazebosim.org/tutorials?tut=model_structure, 접근일 2026-09-30
[^ref-1240]: 지디넷코리아, "실외 이동로봇 필수보험 94% 저렴하게", 2024-02-08, https://zdnet.co.kr/view/?no=20240208201432, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1244]: 법제처 찾기쉬운 생활법령정보, 개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인), 미확인, https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3, 접근일 2026-09-30
[^ref-1245]: 대한민국 정책브리핑 (과학기술정보통신부), '인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무, 2026-01-21, https://www.korea.kr/news/policyNewsView.do?newsId=148958380, 접근일 2026-09-30
[^ref-1246]: Open Robotics (ROS 2 Documentation), ROS 2 developer guide, 미확인, https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html, 접근일 2026-09-30
[^ref-1247]: 고용노동부, 산업용 로봇과 컨베이어도 안전검사 필수, 2017-10-26, https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135, 접근일 2026-09-30
[^ref-1248]: Commonwealth of Virginia (Code of Virginia), § 46.2-908.1:1. Personal delivery devices, 미확인, https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/, 접근일 2026-09-30
[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-23 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-23 | 59. 법·규제·보험·라이선스 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-23/pages/topics/2026/2026-09-30-area59-s3.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 왜 중요한가"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 47, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-991, ref-1235, ref-1236, ref-980, ref-1243, ref-1244, ref-1245, ref-1246, ref-1247, ref-1248]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#3
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 왜 중요한가

# 59. 법·규제·보험·라이선스 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇을 운영할 때 지켜야 할 법·규제·보험·라이선스는 현장마다 달라 보이며, 이번 조사 범위에서는 실외의 운행 규정·운행안전인증·운용자 의무·의무 보험, 산업 사업장의 기계 안전 규제, 모든 현장에 걸치는 AI·사이버보안·개인정보 규제와 사고 책임 법제, 오픈소스·3D 자산 라이선스가 겹치는 구조로 보인다. [추정][^ref-991][^ref-980][^ref-1248][^ref-1247][^ref-1245][^ref-1236][^ref-1244][^ref-1235][^ref-1246]
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇을 운영할 때 지켜야 할 법·규제·보험·라이선스는 현장마다 달라 보이며, 이번 조사 범위에서는 실외의 운행 규정·운행안전인증·운용자 의무·의무 보험, 산업 사업장의 기계 안전 규제, 모든 현장에 걸치는 AI·사이버보안·개인정보 규제와 사고 책임 법제, 오픈소스·3D 자산 라이선스가 겹치는 구조로 보인다. [추정][^ref-991][^ref-980][^ref-1248][^ref-1247][^ref-1245][^ref-1236][^ref-1244][^ref-1235][^ref-1246] 병원·상업 시설·가정 실내 로봇에 특화된 운행 규정은 이번 조사에서 확인하지 못했다.

EU 개정 제조물책임지침(Directive (EU) 2024/2853)은 2026-12-09 이후 시장에 출시되거나 사용이 개시된 제품에 적용되며, 독립형 소프트웨어·디지털 제조 파일·통합 디지털 요소를 제품에 포함한다. [사실][^ref-1235] 이 서술은 EUR-Lex 원문이 아니라 법률사무소 해설(Gibson Dunn, 2026-03-23) 기준이다. 반면 한국 제조물책임법은 제조물을 제조되거나 가공된 동산으로 정의해 소프트웨어를 명시적으로 포함하지 않으므로, 사람의 개입 없이 동작한 자율 시스템 사고에서 소프트웨어 개발자가 제조물 책임을 지는지가 쟁점으로 남아 있다(2024-07 기준). [사실][^ref-1243] 두 법제가 이렇게 다르기 때문에, 여러 제조사 로봇에 명령을 내리는 오케스트레이션 소프트웨어가 사고 책임에서 어떤 지위를 갖는지는 아직 열린 문제다. (구축자 의견) [의견][^ref-1235][^ref-1243]

규제는 사고 뒤의 기록과 보고도 요구한다. EU 사이버복원력법은 2026-09-11부터 디지털 요소 제품의 제조자에게 실제 악용되는 취약점과 중대한 보안 사고의 조기 경보를 24시간 안에 내게 한다. [사실][^ref-1236] 이런 보고 기한과 사고 책임 판단에 대비하려면 실행 기록을 미리 남겨 두는 일이 운영 준비의 일부가 될 것으로 보인다. [추정][^ref-1236][^ref-1235]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-1235]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1236]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-1243]: 김·장 법률사무소, 인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점, 2024-07-05, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930, 접근일 2026-09-30
[^ref-1244]: 법제처 찾기쉬운 생활법령정보, 개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인), 미확인, https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3, 접근일 2026-09-30
[^ref-1245]: 대한민국 정책브리핑 (과학기술정보통신부), '인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무, 2026-01-21, https://www.korea.kr/news/policyNewsView.do?newsId=148958380, 접근일 2026-09-30
[^ref-1246]: Open Robotics (ROS 2 Documentation), ROS 2 developer guide, 미확인, https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html, 접근일 2026-09-30
[^ref-1247]: 고용노동부, 산업용 로봇과 컨베이어도 안전검사 필수, 2017-10-26, https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135, 접근일 2026-09-30
[^ref-1248]: Commonwealth of Virginia (Code of Virginia), § 46.2-908.1:1. Personal delivery devices, 미확인, https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-23 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-23 | 59. 법·규제·보험·라이선스 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-30-23/pages/topics/2026/2026-09-30-area59-s8.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 대표 연구와 자료"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 47, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-991, ref-1235, ref-1236, ref-980, ref-1243]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#8
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 대표 연구와 자료

# 59. 법·규제·보험·라이선스 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 조사에서 모은 자료는 학술 논문보다 정부·집행기관의 1차 자료와 법률사무소 해설이 중심이다.
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 조사에서 모은 자료는 학술 논문보다 정부·집행기관의 1차 자료와 법률사무소 해설이 중심이다.

- Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains(2026) — 개정 제조물책임지침의 적용 시점, 소프트웨어 포함 범위, 실질적 변경자 책임, 보안 업데이트 책임, 증거 공개·결함 추정을 정리한 해설이며, 이 페이지의 EU 제조물 책임 서술은 EUR-Lex 원문이 아니라 이 법률사무소 해설(Gibson Dunn, 2026-03-23) 기준이다. [사실][^ref-1235]
- 김·장 법률사무소, 인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점(2024) — 한국 제조물책임법의 제조물 정의가 소프트웨어 기인 자율 시스템 사고를 포섭하는지를 다룬다(2024-07 기준, 웹 요약 기준). [사실][^ref-1243]
- European Commission, Cyber Resilience Act - Reporting obligations(2026) — 제조자의 취약점·중대 사고 보고 기한과 유럽연합 사이버보안청(European Union Agency for Cybersecurity, ENISA) 단일 보고 플랫폼을 안내하는 집행기관 1차 자료다. [사실][^ref-1236]
- 산업통상자원부·경찰청(정책브리핑), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용(2023) — 개정 지능형로봇법·도로교통법의 시행과 운용자·보험 의무를 알린 정부 발표다. [사실][^ref-991]
- 한국로봇산업진흥원, 실외이동로봇 운행안전인증 안내 — 인증 근거·대상·심사항목·절차의 현재 기준을 확인할 수 있는 인증기관 자료다(2026-09-30 확인). [사실][^ref-980]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-1235]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1236]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-1243]: 김·장 법률사무소, 인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점, 2024-07-05, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-23 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-23 | 59. 법·규제·보험·라이선스 의 "대표 연구와 자료" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1212건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 339개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- model-contractual-terms: 모델 계약 조항 (Model Contractual Terms (MCTs))
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
- substantial-modification: 실질적 변경 (Substantial Modification)
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

### docs/open-questions.md (요약: 대상 영역 [59] 에 걸린 12건 / 전체 283건)

```markdown
- oq-143 [열림] ROP 의 로봇 대화 기능이 국내 인공지능 기본법의 고영향 인공지능이나 EU AI Act 의 고위험 AI 시스템에 해당하는지, 해당한다면 대화 기록 자동 로그의 항목과 보존 기간을 어떻게 정해야 하는가? (영역 13, 59, 53)
- oq-173 [열림] 국가기술표준원이 2021년 제정을 발표한 로봇의 승강기 탑승 안전 요구사항 KS 와 실내 배송 로봇 KS 의 표준 번호·조항은 무엇이며, 그 요구(속도 제어·보호 정지·높낮이차·틈새)가 승강기 연동 계층에 어떤 정보를 요구하는가? (영역 63, 22, 59)
- oq-186 [열림] 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시는 무엇이며, 경사로·알림음·등화장치 같은 기존 항목은 어느 항목에 흡수됐는가? (영역 66, 50, 59)
- oq-187 [열림] 운행안전인증 대상이 로봇과 관제장치의 조합인데, 제조사가 다른 실외 로봇을 하나의 오케스트레이션 계층에서 지시할 때 그 계층이 인증상 관제장치에 해당하는지, 재인증이 필요한지에 관한 기준이나 해석이 있는가? (영역 66, 20, 59)
- oq-231 [열림] 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가? (영역 49, 59)
- oq-239 [열림] 병원의 특수 물품(마약류·검체 등) 로봇 배송 이력처럼 보관 의무가 걸릴 수 있는 실행 기록의 보관 기간과 무결성 요건을 국내 법령·지침이 정하고 있는가? (영역 37, 59)
- oq-249 [열림] EU 기계류 규정의 개입 증거 기록·안전 소프트웨어 추적 로그 요구가 개별 기계 밖에서 여러 로봇을 지시하는 오케스트레이션 플랫폼에도 미치는가, 미친다면 기록 책임은 누구에게 있는가? (영역 52, 59, 58)
- oq-250 [열림] KISA 로봇 보안모델(고도화)과 사이버보안 요구사항 해설서는 로봇 통신 암호화·감사 기록·원격 업데이트에 어떤 요구 항목을 두며 다중 로봇 관제 플랫폼을 대상에 포함하는가? (영역 52, 59)
- oq-262 [열림] 유럽데이터보호이사회(European Data Protection Board, EDPB) 영상 장치 지침 3/2019 를 이동 로봇 카메라에 적용한 유럽 감독기관의 결정이나 해석 사례가 있으며, 보존 기간 권고는 무엇인가? (영역 53, 59)
- oq-275 [열림] 서비스 로봇(서빙·배송·조리 로봇)을 운영하는 인력에게 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육이 실제로 어떻게 적용되며, 고용노동부 지침이나 사례가 있는가? (영역 56, 59, 50)
- oq-279 [열림] 여러 제조사 로봇의 운영 데이터를 모으는 오케스트레이션 플랫폼 사업자는 EU 데이터법상 데이터 보유자인가, 사용자가 지정한 제3자 데이터 수령자인가, 그리고 그에 따라 제조사에게 데이터 제공을 요구할 수 있는 범위는 어디까지인가? (영역 58, 59)
- oq-282 [열림] 오케스트레이션 플랫폼에서 경로망·속도 제한·작업 규칙 같은 설정을 바꾸는 일이 EU 기계류 규정의 실질적 변경에 해당해 플랫폼 운영자나 통합자가 제조자 의무를 지는 경우가 있는가? (영역 58, 59, 48)
```

### runs/2026-09-30-23/verification2.json

```json
{
  "run_id": "2026-09-30-23",
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
      "f12(EU 기계류 규정의 실질적 변경·적용일)는 58. 다사업자 책임·계약·데이터와 같은 참고문헌 id(ref-555·ref-1212)를 재사용했고, 주제 페이지 2026-09-30-area59-s7 표에서 58. 다사업자 책임·계약·데이터로 연결만 했다 — 1차 지시대로다"
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
    "11절(원 페이지 11절 요약 문장, 주제 페이지 docs/topics/2026/2026-09-30-area59-s11.md 의 1절·3절): '기존 열린 질문 9건'을 '10건'으로 고치고, 3절 목록에 oq-275(상태: 열림)를 docs/open-questions.md 의 질문 문장 그대로 더한다 — 입력 열린 질문 목록에는 영역 59 로 걸린 질문이 oq-275 까지 10건 있어 '9건'은 사실과 다르다(1차 지시에 없던 새 지적이다).",
    "[의견] 문장 두 곳에 누구의 의견인지 밝힌다: 원 페이지 4절 첫 문장과 주제 페이지 2026-09-30-area59-s4 의 1·3절 같은 문장('이 영역의 용어는 … 나눠 볼 수 있다'), 주제 페이지 2026-09-30-area59-s3 3절의 '두 법제가 이렇게 다르기 때문에 … 아직 열린 문제다'. 각 문장의 [의견] 앞에 '(구축자 의견)'을 붙인다 — 브리프에는 의견 finding 이 없으므로 스토리텔러가 정리한 판단임을 드러내야 한다(verifier.md 3절 항목 5).",
    "7절 첫 문장('이번 조사로 확인한 규범은 …')은 원 페이지 7절과 주제 페이지 2026-09-30-area59-s7 의 1·3절 모두에서 [사실] 뒤 각주가 ref-991·ref-1235·ref-1236·ref-1246 뿐이다. 문장이 나열한 나머지 규범에도 각주를 붙인다: 해외 주법 [^ref-1248], EU 기계 규범 [^ref-1212], 한국 AI·개인정보·산업안전 법령 [^ref-1245][^ref-1244][^ref-1247], 한국 제조물책임 [^ref-1243], ROS 2·SPDX·Gazebo 라이선스 규칙 [^ref-1237][^ref-1238][^ref-1239]. 그리고 원 페이지 13절에 새로 인용한 ref-1237·ref-1239·ref-1212 각주 정의를 reference_updates 와 같은 줄 형식으로 더한다(ref-1212 는 접근일 뒤 ' (원문 미열람)') — 지금은 [사실] 문장의 절반을 뒷받침하는 각주가 없다.",
    "주제 페이지 2026-09-30-area59-s7 표의 'ROS 2 개발자 가이드 (라이선스 규칙)' 행과 standards_updates 의 같은 항목 summary 를 'LICENSE 파일(대개 Apache 2.0)을 패키지마다 두고, 소스 파일마다 라이선스·저작권 문구를 넣어 자동 린터로 검사한다'처럼 고친다 — 지금 문장은 LICENSE 파일도 린터 검사 대상인 것처럼 읽히지만, f17 의 원문은 소스 파일 문구만 자동 린터 검사 대상으로 둔다.",
    "약어 풀어쓰기: 원 페이지 9절에서 처음 나오는 'SBOM'을 '소프트웨어 자재명세서(Software Bill of Materials, SBOM)'로, 주제 페이지 s4·s6·s7 에서 각각 처음 나오는 'ENISA'를 '유럽연합 사이버보안청(European Union Agency for Cybersecurity, ENISA)'으로 쓴다 — 약어는 페이지마다 첫 등장 시 풀어 써야 한다(공통 규칙 6절).",
    "8절 첫 문장 '… 법률사무소 해설이 중심이며, 대표 자료는 다음과 같다.'를 '… 법률사무소 해설이 중심이다.'처럼 그 문장만으로 끝나게 고친다(원 페이지 8절과 주제 페이지 2026-09-30-area59-s8 의 1·3절) — 자동 분리 뒤 원 페이지에는 이 문장만 남아서 '다음과 같다' 뒤에 목록이 없다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 24건, 미확인 0건, 교차 확인 3건(f1·f3·f9). 강등: f4 사실 → 추정(보험료 인하 수치가 협회 발표를 옮긴 기사 한 건뿐). 원문 미열람 출처: ref-555, ref-1212(이전 실행에서 재사용했고 이번 리서치에서 다시 열지 않음. 검증에서 ref-1212 는 열어 적용일만 확인했고, ref-555 는 EUR-Lex 본문이 비어 검색 결과 일치로만 확인). 주의: 사실 주장은 대부분 정부·기관 1차 자료 단일 출처다. EU 제조물책임지침(f9·f10)은 지침 원문이 아니라 법률사무소 해설 기준이다. 실외이동로봇 운행안전인증 심사항목이 16가지에서 8개로 바뀐 시점과 근거(oq-186)는 확인하지 못했다. 한국 제조물책임법의 소프트웨어 포섭 쟁점(f11)은 2024-07 기준이다. 현장 유형 사례는 실외뿐이며 병원·상업 시설·가정 실내 로봇 규정은 확인하지 못했다. 1차 수정 지시 15건은 모두 이행됐다(f4 강등, f5 재서술, f6 행정예고 주체, f12 각주·원문 미열람 표기, f15 조항 표기, f17 도구 이름 삭제, f16 위치, 5절 현장 유형 실외, 용어집 두 건, 제목·발행일 정정, 11절 열림 유지). / 2차 수정 후 재검증. 드리프트 없음(태그가 붙은 문장이 모두 브리프 finding 이나 분류원문에 대응한다), [분류원문] 보존(소속 대분류 블록·1절·2절이 시드와 같다), 섹션 순서 준수, 링크 유효(형식 검증 통과 기준). 새 지적 6건: 영역 59 의 기존 열린 질문 수 오기(9건 → 10건, oq-275 누락), 출처를 밝히지 않은 [의견] 두 곳, 7절 요약 [사실] 문장의 각주 부족, ROS 2 라이선스 규칙 행의 표현, 약어 풀어쓰기(SBOM·ENISA), 8절 분리 뒤 남은 문장. 참고(파이프라인 담당): 자동 분리 뒤 원 페이지 프런트매터 sources 와 reference_updates 의 cited_by 가 분리 전 기준으로 남아 있다(ref-1237·ref-1239·ref-555·ref-1212 는 주제 페이지에서만 인용). 분리 코드가 이 값을 다시 계산해야 한다. 정정 요청 없음. 해결을 인정한 열린 질문 없음. 2차 검증에서는 검색 도구를 쓰지 않았다.",
  "retry_reason": null
}
```
