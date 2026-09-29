(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-08
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 6. 온톨로지 기반 시스템·로봇 연동 (B. 로봇 온톨로지)
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

### runs/2026-09-29-08/target.json

```json
{
  "run_id": "2026-09-29-08",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 100,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 6,
    "area_name": "6. 온톨로지 기반 시스템·로봇 연동",
    "category": "B. 로봇 온톨로지",
    "category_letter": "B"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=6"
}
```

### runs/2026-09-29-08/research.json

```json
{
  "run_id": "2026-09-29-08",
  "date": "2026-09-29",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 6,
    "area_name": "6. 온톨로지 기반 시스템·로봇 연동",
    "category": "B. 로봇 온톨로지"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 스킬 인터페이스·전제·유지·사후 조건·수행 가능 동작 용어 없음(스킬·능력 매칭·요구 능력·제공 능력·능력·스킬·서비스 모델·능력 기술 서브모델·형상 제약 언어·플릿 어댑터·자산관리셸은 용어집에 이미 있음)",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 능력 기반 로봇 후보 질의, 능력–실행 연결(능력→스킬→인터페이스), 온톨로지 기반 연동 자동화(모델 매핑·설정 초안 생성), 실행 시점 조건 판단(전제조건·상태 검사) 네 갈래 모두 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 능력·스킬·서비스 모델 온톨로지, IDTA 02020 능력 기술 서브모델, Open-RMF 사용자 정의 작업, VDA 5050 커넥터, OPC UA 스킬 실행 프로토콜, SkiROS2 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 7. 온톨로지 검증·변경 관리, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 22. 설비·건물 시스템 연동, 25. 작업 배정 — MRTA, 29. 명령·작업 실행의 신뢰성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영 연결 필요",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 oq-150 미반영, 정정 요청 없음",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "온톨로지를 이용해 새 로봇과 새 시스템을 손작업 없이 어떻게 연동할 것인가? [분류원문]",
    "작업 요구에 맞는 로봇·자원 후보를 온톨로지 질의로 찾고 근거와 함께 돌려주는 능력 매칭 접근에는 무엇이 있는가? (섹션 4·6·8 겨냥)",
    "온톨로지의 능력을 실제 로봇 명령·어댑터·스킬 인터페이스에 묶는 모델(능력·스킬·서비스 모델, 자산관리셸 능력 기술, OPC UA 스킬, Open-RMF 사용자 정의 작업)은 무엇을 정하며, 검토되지 않은 연결의 실행을 어떻게 막는가? (섹션 6·7 겨냥)",
    "등록된 능력 모델로 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 자동으로 만드는 방법(모델 간 매핑, 계획 도메인 자동 생성, 모델 기반 생성)은 무엇이 보고되었는가? (섹션 6·8 겨냥, 교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 연결)",
    "배터리·적재·문·승강기 같은 현재 상태로 능력을 지금 실행할 수 있는지 판단하는 전제조건·정책 검사(SPARQL·SHACL, 전제·유지·사후 조건)는 어떻게 구현되는가? (섹션 4·6 겨냥)",
    "oq-150 팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가? (섹션 5·11 겨냥, 현장 유형 명시·한국 자료 우선)",
    "온톨로지 기반 연동에서 ROP가 직접 맡을 것(후보 질의·매핑·설정 초안·조건 검사)과 스킬 내부 구현·설비 API 에 맡길 것의 경계는 어디이며, 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Plattform Industrie 4.0 의 능력·스킬·서비스(CSS) 참조 모델을 구현한 CSS 온톨로지는 능력을 산업 생산에서 효과를 내는 기능의 구현 독립적 명세로, 스킬을 능력을 구현한 실행 가능한 자동화 기능으로, 서비스를 제공 능력의 상업적 측면 기술로 정의하고, 모든 스킬이 외부 제어를 위한 스킬 인터페이스(예: OPC UA 서버)를 가져야 한다고 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-882"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "저장소 README: Capability 는 \"implementation-independent specification of a function in industrial production\", Skill 은 실행 가능한 구현이며 SkillInterface(OPC UA 서버 등)가 외부 제어에 필요. 확장 온톨로지로 CaSk·CaSkMan·RoboCaSk 를 든다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "IDTA 02020 능력 기술(Capability Description) 서브모델 1.0 판은 생산 공정의 요구 능력과 가용 자원의 제공 능력을 비교하는 기반을 목적으로 하며, 능력을 속성(최대 속도·허용 공차 등), 제약(전제조건·불변·사후조건의 속성 제약과 순서·병렬의 전이 제약), 능력을 구현하는 스킬(기술·소프트웨어 모듈)의 세 관계로 모델링한다.",
      "tag": "사실",
      "source_ids": [
        "ref-229"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: 서브모델은 \"required capabilities\" 와 \"provided capabilities\" 의 매칭 기반을 두고, 속성·제약(property constraints: preconditions, invariants, postconditions; transition constraints)·스킬의 세 관계로 능력을 기술. 1.0 판이 첫 공식 발행. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f3",
      "claim": "서로 다른 두 발행 주체(헬무트 슈미트 대학 계열 CaSkade 의 CSS 온톨로지, IDTA 의 능력 기술 서브모델)가 구현 독립적 능력과 실행 구현인 스킬을 분리하고 요구 능력–제공 능력 매칭을 모델의 목적으로 각각 정의해, 이 영역의 능력–실행 분리 구조가 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-882",
        "ref-229"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "두 문서 모두 능력을 'implementation-independent specification' 으로, 스킬을 능력을 구현하는 모듈로 두고 요구/제공 능력 비교를 언급. 둘 다 Plattform Industrie 4.0 CSS 참조 모델에서 파생되어 완전 독립은 아니므로 신뢰도는 medium 으로 둔다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "Vieira da Silva·Köcher·Fay(2022, 2023 개정)는 이기종 자율 로봇 팀에서 각 로봇이 제공하는 기능을 일관되게 기술하는 방법이 없다고 지적하고, 제조업의 능력·스킬 모델링 접근을 자율 로봇에 적용한 능력 모델을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-038"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"there is no consistent way of describing the functions that each robot provides\"; 제조업 능력 모델링을 이기종 자율 로봇에 확장하는 접근을 제시(v2 2023-02-09).",
      "as_of": "2023-02-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "Dussard·Sarthou·Clodic(2023, 2025 개정)은 로봇이 보유한 물리 구성요소와 하위 능력으로부터 상위 능력을 온톨로지 추론으로 도출해 로봇이 어떤 작업에 배정될 수 있고 없는지를 스스로 판단하게 하고, 능력과 외부 객체 속성 사이의 어포던스 관계까지 추론하는 방법을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-249"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 구성요소 기반으로 능력을 추론하는 온톨로지 수단을 제시하고, 능력으로 \"which tasks it can be assigned to and which it cannot\" 을 정의하며 외부 개체와의 어포던스 관계를 추론(v3 2025-09-10).",
      "as_of": "2025-09-10",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f6",
      "claim": "Järvenpää·Siltala·Hylli·Lanz(Procedia CIRP 97, 2021)의 능력 매치메이킹 소프트웨어는 제품 요구와 자원 능력의 매칭을 자동화해 기존 생산 시스템이 새 제품 요구를 충족하는지 확인하고 대형 카탈로그에서 후보 자원을 찾으며, 외부 설계 도구와의 연동을 사례로 설명했다.",
      "tag": "사실",
      "source_ids": [
        "ref-890"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "탐페레대학교 연구 포털 초록: 소프트웨어가 \"automatizes the matchmaking between product requirements and resource capabilities\" 하고 대형 카탈로그에서 대안 자원을 식별하며 외부 설계 도구 연동을 사례로 설명. 온톨로지·규칙 구현 세부는 초록에 없음.",
      "as_of": "2021",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f7",
      "claim": "서로 다른 세 연구 그룹(LAAS 의 구성요소 기반 능력 추론, 탐페레대학교의 능력 매치메이킹, 헬무트 슈미트 대학의 이기종 로봇 능력 모델)이 온톨로지 기반 능력 기술로 작업·요구에 맞는 로봇·자원 후보를 찾는 접근을 각각 보고해, 능력 기반 로봇 후보 질의가 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-249",
        "ref-890",
        "ref-038"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "세 출처 모두 발행 주체가 다르고, 능력 기술을 근거로 작업 배정 가능 여부(LAAS)·후보 자원 식별(탐페레)·이기종 로봇 기능 기술(HSU)을 다룬다. 후보와 함께 근거(설명)를 돌려주는 기능은 세 초록 어디에도 명시되지 않았다.",
      "as_of": "2025-09-10",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f8",
      "claim": "Open-RMF 의 사용자 정의 작업 문서는 플릿 설정의 action_categories 로 지원 동작을 선언하고, add_performable_action 의 consider 콜백이 동작 설명을 보고 수락 여부를 정하며 set_action_executor 가 실행을 맡는 두 부분 API 를 정하고, 사용자 정의 동작 중 로봇은 읽기 전용 교통 참여자가 되어 교통 협상에 참여하지 않으며 문·승강기 사용은 사용자 정의 로직에서 바꿀 수 없다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-880"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "문서: action_categories: [\"clean\", \"manual_control\"] 예시; consider 콜백으로 수락 판단; 동작 중 로봇은 \"read-only\" 교통 참여자가 되어 교통 협상에 참여하지 않으며 문·승강기 조작은 사용자 정의 범위 밖. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f9",
      "claim": "Open-RMF 플릿 어댑터 튜토리얼은 새 플릿 설정에 작업 능력(loop·delivery·clean)과 재충전 임계값, 배터리·기계 시스템 매개변수를 적게 하고 로봇 측 API 가 battery_soc 를 보고하게 하여, 능력 선언과 실행 시점 배터리 상태가 같은 설정·API 에 담긴다.",
      "tag": "사실",
      "source_ids": [
        "ref-153"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "config.yaml 에 task_capabilities(loop·delivery·clean), recharge_threshold, 배터리·기계 시스템 매개변수를 적고 RobotAPI 가 battery_soc·is_command_completed 를 구현해야 한다. (재인용: 2026-09-29-07)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f10",
      "claim": "Mayr·Rovida·Krueger 의 SkiROS2(IROS 2023)는 스킬을 전제·유지·사후 조건으로 정의하고 OWL 세계 모델(지식 베이스)로 세계 상태와 개체를 추론하며 확장 행동 트리로 작업 계획과 반응적 실행을 합쳐, 서로 다른 작업과 로봇 시스템 사이에서 스킬을 교체해 쓰는 사례(작업 계획·추론·다중 센서 통합·제조 실행 시스템 연결 등)를 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-881"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 스킬 정식화는 \"pre-, hold- and post-conditions\" 에 기반하고, 계층적 혼합 제어 구조와 세계 상태 추론용 지식 베이스를 두며 세 가지 사용 사례로 작업·로봇 간 교체 가능성을 예시. 실제 로봇 배치 결과는 초록에 없음.",
      "as_of": "2023-06-29",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f11",
      "claim": "Ioannidou 외(Healthcare, 2025)의 의료 로봇 상위 온톨로지 HERON 은 SPARQL 질의로 특정 작업에 대한 에이전트 자격과 전제조건을 검사하고 SHACL 형상으로 역할 기반 권한·오버라이드 승인 같은 기관 정책 준수를 검증하며, 임상 배치 없이 Fundació Ave Maria 의료센터의 물류 운반·다중 로봇 플릿 조정 시뮬레이션 시나리오로 시연했다.",
      "tag": "사실",
      "source_ids": [
        "ref-885"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PMC 전문: SPARQL 로 \"agent eligibility for specific tasks\" 와 전제조건을, SHACL 로 역할 기반 권한·오버라이드 승인을 검증; 물류 운반·e-진단 지원·다중 로봇 조정 시나리오를 시뮬레이션(2025-04-30).",
      "as_of": "2025-04-30",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f12",
      "claim": "서로 다른 세 발행 주체(룬드대학교의 SkiROS2, 그리스 연구진의 HERON, IDTA 의 능력 기술 서브모델)가 능력·스킬에 전제조건과 사후조건 같은 실행 조건을 붙이고 실행 전에 이를 검사하는 구조를 각각 두어, 이 영역의 실행 시점 조건 판단이 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-881",
        "ref-885",
        "ref-229"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "SkiROS2 는 pre/hold/post 조건, HERON 은 SPARQL 전제조건·SHACL 정책 검사, IDTA 02020 은 preconditions·invariants·postconditions 속성 제약을 각각 정의. 배터리·문·승강기 같은 구체 상태를 조건으로 쓴 예는 HERON(운반 시나리오)과 Open-RMF(배터리) 외에는 확인하지 못했다.",
      "as_of": "2025-04-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f13",
      "claim": "Vieira da Silva 외(2023, 2024 개정)는 자산관리셸 서브모델과 능력·스킬 온톨로지가 서로 호환되지 않는 두 모델링 틀임을 분석하고, 비교 가능한 요소와 다른 요소를 가려낸 뒤 두 개의 단방향 선언적 매핑으로 이루어진 양방향 매핑 개념을 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-037"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"a concept for a bidirectional mapping between AAS submodels and a capability and skill ontology\" 를 \"two unidirectional, declarative mappings\" 로 구성(v2 2024-04-28).",
      "as_of": "2024-04-28",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "Nabizada 외(IEEE CASE 2026 채택)는 네 가지 Industrie 4.0 표준으로 구조화한 자산관리셸 능력 모델에 완전한 PDDL 계획 문제를 자동 생성할 정보가 충분함을 보이고, PDDL 전용 서브모델 없이 분산 다중 자산관리셸 구조를 계획 문제로 변환하는 추출 알고리즘을 실험실 생산 시스템의 레이아웃 변형 4개 비교로 검증했다.",
      "tag": "사실",
      "source_ids": [
        "ref-201"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 알고리즘이 \"transforms distributed Multi-AAS architectures into complete PDDL planning problems\"; 실험실 생산 시스템 AAS 모델로 4개 레이아웃 변형을 최적 계획으로 비교(2026-06-01 제출).",
      "as_of": "2026-06-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "Nagrath·Blender·Shaik·Schlegel(2022)은 서비스 로봇에서 소프트웨어 컴포넌트의 자산관리셸을 표준화된 디지털 데이터 시트로, 시스템 수준 자산관리셸을 런타임 운영 데이터 수집과 스킬 수준 명령의 창구로 쓰며, 자산관리셸을 손으로 만들지 않고 모델 기반 개발·조합 워크플로에서 생성·채운다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-883"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"The AAS for a software component serves as a standardized digital data sheet\", 시스템 AAS 가 \"skill-level commanding of the service robot\" 을 가능하게 하며 \"AASs are generated and filled as part of our model-driven development and composition workflow\"(5쪽 작업 중 논문).",
      "as_of": "2022-08-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "Sidorenko 외(FAIM 2021)는 스킬을 유한 상태 기계로 OPC UA 에 노출하고 Industrie 4.0 언어 메시지와 상호작용 상태 기계를 능동 자산관리셸 안에 모델링한 스킬 실행 상호작용 프로토콜을 제시해, 두 Industrie 4.0 컴포넌트가 계층적 제어 대신 동등 협력 방식으로 스킬을 함께 실행하는 예시를 시연했다.",
      "tag": "사실",
      "source_ids": [
        "ref-887"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Zenodo 초록: I4.0 언어 메시지와 상호작용 상태 기계의 모델링으로 사이버 물리 생산 모듈이 스킬을 협력 사용하게 하고, 두 컴포넌트의 협력 스킬 실행 예시를 제시(2021-11-03).",
      "as_of": "2021-11-03",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f17",
      "claim": "서로 다른 세 발행 주체(Schlegel 연구진, SmartFactory-KL 계열 Sidorenko 연구진, CaSkade 의 CSS 온톨로지)가 능력 모델과 별도로 스킬 실행 인터페이스(OPC UA 서버·상태 기계·자산관리셸 스킬 명령)를 두고 능력→스킬→인터페이스 순으로 실제 명령에 묶는 구조를 각각 보고해, 이 영역의 능력–실행 연결 방식이 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-883",
        "ref-887",
        "ref-882"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "CSS 온톨로지는 SkillInterface 를 필수로, Sidorenko 외는 OPC UA 상태 기계 스킬 실행 프로토콜을, Nagrath 외는 시스템 AAS 의 스킬 수준 명령을 기술. 검토·승인되지 않은 연결의 실행을 막는 관문은 세 출처 모두 명시하지 않았다.",
      "as_of": "2022-08-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "ROS 2 패키지 vda5050_connector(1.1.1, BSD-3, VDA 5050 2.0 지원)는 MQTT 브리지·컨트롤러(주문 검증·실행·피드백)·어댑터의 세 부분으로 로봇을 VDA 5050 관제에 연결하며, 어댑터는 상태·노드 주행·VDA 동작의 세 핸들러를 플러그인으로 두어 로봇 플랫폼마다 사용자가 핸들러 패키지를 직접 만들어야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-886"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "index.ros.org: 어댑터는 State Handler·NavToNode Handler·VDA Action Handler 세 종류를 요구하고 \"Users must create custom adapter packages defining these handlers for their specific robot platform\"; 지원 버전 2.0. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f19",
      "claim": "등록된 능력 모델에서 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 자동으로 만들었다고 직접 보고한 자료는 이번 조사에서 확인되지 않았으며, 확인된 것은 모델 간 선언적 매핑(f13), 자산관리셸에서 계획 도메인 자동 생성(f14), 모델 기반 자산관리셸 생성(f15), 어댑터의 고정된 핸들러 구조(f18·f9)이므로 이를 결합하면 능력 모델에서 핸들러·설정 초안을 만드는 경로가 가능해 보이나 사례는 미확인이다.",
      "tag": "추정",
      "source_ids": [
        "ref-037",
        "ref-201",
        "ref-886",
        "ref-153"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "네 출처를 종합한 추정. 매핑·생성 연구는 모두 제조 자산관리셸·PDDL 대상이고, 이동로봇 플릿 어댑터(Open-RMF·VDA 5050 커넥터)의 설정·핸들러를 능력 모델에서 생성한 사례는 찾지 못했다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "서로 다른 두 발행 주체(Open Robotics 의 플릿 어댑터·사용자 정의 작업 문서, ROS 패키지 색인의 vda5050_connector)가 로봇 연동 어댑터를 '플릿·능력 설정'과 '로봇별 핸들러·API 구현'의 두 부분으로 각각 구성해, 온톨로지로 자동화할 수 있는 부분(설정·매핑)과 손작업이 남는 부분(로봇별 구현)의 경계가 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-880",
        "ref-153",
        "ref-886"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "Open-RMF 는 config.yaml 의 능력·동작 선언과 RobotAPI·action executor 구현으로, vda5050_connector 는 설정과 세 핸들러 플러그인 구현으로 나뉜다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f21",
      "claim": "창이종합병원 CHART 는 KONE·Smart Urban Co-Innovation Lab·AWS·CapitaLand 와 함께 캐피털랜드 Galen 오피스 빌딩에서 개방 API 를 가진 KONE DX 급 승강기와 RMF 로 자율이동로봇이 여러 층을 오가는 시험 환경을 만들고, 청소·보안·배송·컨시어지 등 여러 업체 로봇으로 시험을 확대할 계획을 밝혔으나 업체 수와 정량 결과는 공개 페이지에 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-889"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "페이지: KONE 이 승강기를 개방 API 로 현대화해 \"autonomous mobile robots to traverse across different levels\" 가능; Galen 빌딩이 로봇–승강기 연동의 실환경 시험장; 여러 로봇 업체 시험은 다음 단계. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": "기타",
      "flow_item": "수행 자원"
    },
    {
      "id": "f22",
      "claim": "Valner 외(2022)의 타르투대학교병원 현장 시험에서는 프로그램 제어가 없는 병원 문을 카드 인식·근접 센서를 대신 작동시키는 서보 장치로 보완해야 했으므로, 온톨로지·설정만으로 연동되지 않는 설비가 남아 손작업 없는 연동의 한계를 보여준다.",
      "tag": "사실",
      "source_ids": [
        "ref-869"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PAL Robotics TIAGo 를 FreeFleet 클라이언트·서버와 RMF 어댑터 파일로 등록했고, 프로그램 제어가 없는 문은 서보 장치를 만들어 지났다. (재인용: 2026-09-29-07)",
      "as_of": "2022-08-23",
      "site_type": "병원",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "황선명(보안공학연구논문지 8권 1호, 2011)은 컴포넌트 온톨로지와 환경 온톨로지를 구축해 사람의 명령을 사전 정의된 작업에 연결하고 환경 온톨로지에서 매개변수를 얻어 필요한 컴포넌트 목록을 구성·실행하는 로봇 컴포넌트 동적 재구성 방법을 제안했으며, 이는 이번 조사에서 확인된 유일한 국내 온톨로지 기반 로봇 연동 연구다.",
      "tag": "사실",
      "source_ids": [
        "ref-888"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KCI 초록: \"By constructing component ontology and environment ontology, robot constitutes component list needed to preliminarily defined TASK according to person's order\"; 평가는 목표 지점 이동 시간 개선 서술.",
      "as_of": "2011",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "Vieira da Silva·Köcher·Gehlhoff·Fay(2024)는 자연어 능력 설명에서 언어 모델로 능력 온톨로지를 생성하고 구문 검증·모순 탐지·환각·누락 점검을 자동 루프로 돌린 뒤 사람이 최종 검토하게 하여, 온톨로지 기반 연동의 앞 단계인 능력 모델 작성 부담을 줄이는 방법을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-465"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "자연어 능력 설명을 프롬프트에 넣어 능력 온톨로지를 생성하고 자동 검증 뒤 사람이 최종 검토·수정. (재인용: 2026-09-29-07)",
      "as_of": "2024-10-18",
      "site_type": null,
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "확인한 자료를 종합하면 6. 온톨로지 기반 시스템·로봇 연동에서 ROP가 직접 맡을 범위는 능력 온톨로지 질의로 후보 로봇을 찾아 근거와 함께 돌려주는 기능, 능력→스킬→인터페이스 매핑표와 그 검토·승인 기록, 어댑터 설정·핸들러 초안 생성, 실행 전 전제조건·정책 검사(배터리·문·승강기 상태)이며, 근거를 함께 돌려주는 설명 기능과 검토되지 않은 연결의 실행 차단은 확인한 출처 어디에도 명시되지 않아 ROP 가 따로 설계해야 할 요구로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-882",
        "ref-880",
        "ref-886",
        "ref-885"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "CSS 온톨로지·Open-RMF 사용자 정의 작업·vda5050_connector·HERON 을 종합한 추정. Open-RMF 의 consider 콜백(f8)과 HERON 의 SHACL 정책 검사(f11)가 승인 관문의 부분 선례다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "연계 대상: 스킬의 내부 구현과 상태 기계 실행(OPC UA 서버·로봇 SDK 쪽)과 승강기 제조사의 개방 API 자체는 분류 원문 19장의 로봇 자체 지능·제어와 시설·설비 제어 쪽이므로, 이종 제조사를 잇는 ROP 는 스킬 인터페이스 호출·상태 확인·완료 판정과 승강기 사용 요청·인계만 맡고 구현 성능은 제조사·설비 측에 맡겨야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-887",
        "ref-889",
        "ref-882"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Sidorenko 외의 OPC UA 스킬 상태 기계, CGH 의 KONE 개방 API 승강기, CSS 온톨로지의 스킬 인터페이스 분리를 근거로 한 경계 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f27",
      "claim": "이 영역은 능력 표현을 주는 5. 로봇 능력·작업 표현과 등록 데이터를 주는 4. 이기종 로봇 등록, 매핑·제약을 검증하는 7. 온톨로지 검증·변경 관리를 앞뒤로 두고, 어댑터·규격은 20. 로봇·제조사 관제 연동과 21. 상호운용 표준·적합성, 문·승강기 상태는 22. 설비·건물 시스템 연동, 후보 질의 결과는 25. 작업 배정 — MRTA, 실행 조건과 완료 판정은 29. 명령·작업 실행의 신뢰성과 18. 실시간 세계 상태·데이터 일관성에 이어지며, 언어 모델로 능력 온톨로지를 만드는 방법(f24)은 교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영에도 연결된다.",
      "tag": "추정",
      "source_ids": [
        "ref-880",
        "ref-229",
        "ref-885",
        "ref-465"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Open-RMF 사용자 정의 작업(문·승강기 제외, 교통 협상 제외), IDTA 02020 제약, HERON 전제조건 검사, 언어 모델 능력 온톨로지 생성을 근거로 한 영역 연결 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "oq-150 관련: Open-RMF 의 task_capabilities·action_categories 로 청소·수동 제어 같은 팩트시트에 없는 능력을 선언하는 방법은 공식 문서(f8·f9)로 확인되지만 문·승강기 사용은 사용자 정의 동작이 아니라 플랫폼 기능이라 그 경로로 등록하지 않으며, 자산관리셸 능력 기술 서브모델을 로봇 현장에서 실제로 썼다는 사례는 확인되지 않아 oq-150 은 미해결로 남는다.",
      "tag": "추정",
      "source_ids": [
        "ref-880",
        "ref-229",
        "ref-153"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Open-RMF 문서는 사용자 정의 동작이 문·승강기 조작을 바꿀 수 없다고 적고, IDTA 02020 README 는 생산 계획 대상만 언급하며 로봇 현장 적용 사례를 들지 않는다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-038",
      "org": "Vieira da Silva, L. M., Köcher, A., & Fay, A. (Helmut Schmidt University)",
      "title": "A Capability and Skill Model for Heterogeneous Autonomous Robots",
      "published": "2023-02-09",
      "url": "https://arxiv.org/abs/2209.10900",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "이기종 자율 로봇 팀의 기능을 일관되게 기술할 방법이 없다는 문제를 들어 제조업 능력·스킬 모델링을 자율 로봇에 적용한 능력 모델을 제안한 프리프린트(초록 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2209.10900",
      "source_unopened": false
    },
    {
      "id": "ref-201",
      "org": "Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. (IEEE CASE 2026 채택)",
      "title": "From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation",
      "published": "2026-06-01",
      "url": "https://arxiv.org/abs/2606.02167",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자산관리셸 능력 모델에서 PDDL 계획 문제를 자동 생성하는 추출 알고리즘을 제시하고 실험실 생산 시스템의 레이아웃 변형 4개 비교로 검증한 프리프린트(초록 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2606.02167",
      "source_unopened": false
    },
    {
      "id": "ref-037",
      "org": "Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A.",
      "title": "Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies",
      "published": "2024-04-28",
      "url": "https://arxiv.org/abs/2307.00827",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자산관리셸 서브모델과 능력·스킬 온톨로지 사이의 양방향 매핑을 두 개의 단방향 선언적 매핑으로 구성하는 개념을 제시한 프리프린트(초록 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2307.00827",
      "source_unopened": false
    },
    {
      "id": "ref-249",
      "org": "Dussard, B., Sarthou, G., & Clodic, A. (LAAS-CNRS)",
      "title": "Ontological Component-based Description of Robot Capabilities",
      "published": "2025-09-10",
      "url": "https://arxiv.org/abs/2306.07569",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "로봇의 구성요소와 하위 능력에서 상위 능력을 온톨로지로 추론해 배정 가능한 작업을 판단하고 어포던스 관계를 추론하는 방법을 제안한 프리프린트(v3, 초록 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2306.07569",
      "source_unopened": false
    },
    {
      "id": "ref-880",
      "org": "Open Robotics (Programming Multiple Robots with ROS 2)",
      "title": "User-defined Tasks - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/task_userdefined.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 의 사용자 정의 작업(perform_action) 지원 방식: action_categories 선언, add_performable_action 의 consider 콜백, set_action_executor, 동작 중 읽기 전용 교통 참여자, 문·승강기 조작 제외.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://osrf.github.io/ros2multirobotbook/task_userdefined.html",
      "source_unopened": false
    },
    {
      "id": "ref-881",
      "org": "Mayr, M., Rovida, F., & Krueger, V. (Lund University, IROS 2023)",
      "title": "SkiROS2: A skill-based Robot Control Platform for ROS",
      "published": "2023-06-29",
      "url": "https://arxiv.org/abs/2306.17030",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "전제·유지·사후 조건으로 정의한 스킬, OWL 세계 모델, 확장 행동 트리로 계획과 실행을 합친 ROS 기반 스킬 제어 플랫폼(초록 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2306.17030",
      "source_unopened": false
    },
    {
      "id": "ref-882",
      "org": "CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) GitHub 공식 저장소",
      "title": "CSS — An ontology for the Capability, Skill and Service model of Plattform Industrie 4.0 (README)",
      "published": null,
      "url": "https://github.com/CaSkade-Automation/CSS",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Plattform Industrie 4.0 의 능력·스킬·서비스 참조 모델을 구현한 OWL 온톨로지 README. 능력·스킬·서비스·속성·스킬 인터페이스 정의와 확장 온톨로지(CaSk·CaSkMan·RoboCaSk)를 소개한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/CaSkade-Automation/CSS/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-883",
      "org": "Nagrath, V., Blender, T., Shaik, N., & Schlegel, C. (Technische Hochschule Ulm)",
      "title": "Industry 4.0 Asset Administration Shell (AAS): Interoperable Skill-Based Service-Robots",
      "published": "2022-08-02",
      "url": "https://arxiv.org/abs/2208.01273",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "서비스 로봇의 소프트웨어 컴포넌트·시스템 수준 자산관리셸을 디지털 데이터 시트와 스킬 수준 명령 창구로 쓰고 모델 기반 개발 워크플로에서 생성하는 접근(작업 중 논문, 초록 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2208.01273",
      "source_unopened": false
    },
    {
      "id": "ref-229",
      "org": "Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소",
      "title": "IDTA 02020 Submodel Template: Capability Description — README (published/Capability Description/1/0)",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "요구 능력과 제공 능력의 비교를 목적으로 능력을 속성·제약(전제조건·불변·사후조건, 전이 제약)·스킬의 세 관계로 모델링하는 자산관리셸 서브모델 템플릿 1.0 판 README.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": "https://raw.githubusercontent.com/admin-shell-io/submodel-templates/main/published/Capability%20Description/1/0/README.md",
      "source_unopened": true
    },
    {
      "id": "ref-885",
      "org": "Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel)",
      "title": "HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics",
      "published": "2025-04-30",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "의료 로봇 상위 온톨로지 HERON. SPARQL 로 작업 자격·전제조건을, SHACL 로 역할 기반 정책을 검증하며 의료센터 물류·다중 로봇 시나리오를 시뮬레이션으로 시연(전문 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/",
      "source_unopened": false
    },
    {
      "id": "ref-886",
      "org": "ROS Index (InOrbit ros_amr_interop, 유지관리자 Leandro Pineda)",
      "title": "vda5050_connector - ROS Package Overview",
      "published": null,
      "url": "https://index.ros.org/p/vda5050_connector/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "ROS 2 로봇을 VDA 5050 2.0 관제에 잇는 커넥터 패키지(1.1.1, BSD-3). MQTT 브리지·컨트롤러·어댑터 구조와 로봇별로 구현해야 하는 세 핸들러 플러그인을 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://index.ros.org/p/vda5050_connector/",
      "source_unopened": false
    },
    {
      "id": "ref-887",
      "org": "Sidorenko, A., Volkmann, M., Motsch, W., Wagner, A., & Ruskowski, M. (FAIM 2021, Zenodo)",
      "title": "An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell",
      "published": "2021-11-03",
      "url": "https://zenodo.org/records/5648095",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "스킬을 유한 상태 기계로 OPC UA 에 노출하고 I4.0 언어 메시지·상호작용 상태 기계를 능동 자산관리셸에 모델링한 스킬 실행 프로토콜과 두 컴포넌트 협력 실행 예시(Zenodo 초록 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://zenodo.org/records/5648095",
      "source_unopened": false
    },
    {
      "id": "ref-888",
      "org": "황선명 (대전대학교, 보안공학연구논문지 8(1))",
      "title": "온톨로지 기반의 로봇 동적재구성에 관한 연구",
      "published": "2011",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001533055",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "컴포넌트 온톨로지와 환경 온톨로지로 사람의 명령을 사전 정의 작업에 연결하고 필요한 컴포넌트를 구성·실행하는 로봇 동적 재구성 방법을 제안한 국내 논문(KCI 초록 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001533055",
      "source_unopened": false
    },
    {
      "id": "ref-889",
      "org": "Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CGH-CHART)",
      "title": "Robot-Lift Integration Challenge | Changi General Hospital",
      "published": null,
      "url": "https://www.cgh.com.sg/chart/projects/romi-h/robot-lift-integration-challenge",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "CGH-CHART·KONE·Smart Urban Co-Innovation Lab·AWS·CapitaLand 가 Galen 오피스 빌딩에서 개방 API 승강기와 RMF 로 로봇 층간 이동을 시험하는 프로젝트 소개 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.cgh.com.sg/chart/projects/romi-h/robot-lift-integration-challenge",
      "source_unopened": false
    },
    {
      "id": "ref-890",
      "org": "Järvenpää, E., Siltala, N., Hylli, O., & Lanz, M. (Tampere University, Procedia CIRP 97)",
      "title": "Capability matchmaking software for rapid production system design and reconfiguration planning",
      "published": "2021",
      "url": "https://researchportal.tuni.fi/en/publications/capability-matchmaking-software-for-rapid-production-system-desig/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "제품 요구와 자원 능력의 매칭을 자동화해 대형 카탈로그에서 후보 자원을 찾는 매치메이킹 소프트웨어와 외부 설계 도구 연동 사례(연구 포털 초록 열람, CC BY-NC-ND 공개).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://researchportal.tuni.fi/en/publications/capability-matchmaking-software-for-rapid-production-system-desig/",
      "source_unopened": false
    },
    {
      "id": "ref-153",
      "org": "Open Robotics (Programming Multiple Robots with ROS 2)",
      "title": "Fleet Adapter Tutorial (integration_fleets_action_tutorial) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 플릿 어댑터 설정(config.yaml)의 항목과 로봇 측 RobotAPI 구현 요구를 설명하는 튜토리얼(이전 실행 2026-09-29-07 재사용).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-869",
      "org": "Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "타르투대학교병원에서 Open-RMF 로 이기종 로봇 플릿을 등록·운용한 현장 시험(이전 실행 2026-09-29-07 재사용).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-465",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "Toward a Method to Generate Capability Ontologies from Natural Language Descriptions",
      "published": "2024-10-18",
      "url": "https://arxiv.org/abs/2406.07962",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자연어 능력 설명에서 언어 모델로 능력 온톨로지를 생성하고 자동 검증 뒤 사람이 최종 검토하는 방법(이전 실행 2026-09-29-07 재사용).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md",
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
      "rationale": "섹션 3: f4(이기종 로봇 기능을 일관되게 기술할 방법 부재), f20(어댑터가 설정과 로봇별 구현으로 나뉘어 손작업이 남음), f22(설비가 프로그램 제어를 못 하면 온톨로지·설정만으로 연동되지 않음) / 섹션 4: f1(능력·스킬·서비스·스킬 인터페이스), f2(속성·제약·스킬, 전제조건·불변·사후조건), f10(전제·유지·사후 조건), f8(수행 가능 동작·action_categories), f5(구성요소 기반 능력 추론·어포던스) / 섹션 5: 병원 — f11(HERON 의료센터 시뮬레이션: 물류 운반·다중 로봇 조정, 임상 배치 아님을 명시), f22(타르투대학교병원 문 보완 장치), 기타 — f21(싱가포르 Galen 오피스 빌딩 승강기 연동 시험 환경), 제조 공장·물류창고 현장 사례는 확인되지 않음을 서술(f6·f14 는 생산 시스템 설계·실험실 수준) / 섹션 6: 능력 기반 후보 질의 f5·f6·f7, 능력–실행 연결 f1·f15·f16·f17·f8, 연동 자동화 f13·f14·f15·f19(자동 생성 사례 미확인은 추정), 실행 시점 조건 판단 f9·f10·f11·f12, 앞 단계 능력 모델 생성 f24(교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영 함께 연결) / 섹션 7: f1(CSS 온톨로지), f2(IDTA 02020), f8·f9(Open-RMF 사용자 정의 작업·플릿 어댑터), f18(vda5050_connector), f16(OPC UA 스킬 실행 프로토콜), f10(SkiROS2) / 섹션 8: f4, f5, f6, f13, f14, f15, f16, f11, 국내 f23 / 섹션 9: f25(직접 범위: 후보 질의·매핑표·검토 승인 기록·설정 초안·전제조건 검사), f26(연계 대상: 스킬 내부 구현·승강기 API) / 섹션 10: f27 — 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 7. 온톨로지 검증·변경 관리, 18. 실시간 세계 상태·데이터 일관성, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 22. 설비·건물 시스템 연동, 25. 작업 배정 — MRTA, 29. 명령·작업 실행의 신뢰성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영, 63. 병원·의료(f11·f22) / 섹션 11: 기존 oq-150(f28 로 부분 진전, 미해결)과 open_questions_new 4건. 다음 실행 후보: 22. 설비·건물 시스템 연동 페이지에 f8·f21 반영, 21. 상호운용 표준·적합성 페이지에 f2·f13·f18 반영, 25. 작업 배정 — MRTA 페이지에 f5·f7 반영, 트랙 manual-capability-ontology 단계 4(실행 연결)에 f1·f16·f17 참고."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "스킬 인터페이스",
      "term_en": "Skill Interface",
      "definition": "능력·스킬·서비스 모델에서 스킬을 외부에서 제어하기 위해 반드시 두는 접점(예: OPC UA 서버)으로, 스킬 구현과 분리되어 같은 스킬을 여러 프로토콜로 노출할 수 있게 한다."
    },
    {
      "term_ko": "전제·유지·사후 조건",
      "term_en": "Pre-, Hold-, Post-condition",
      "definition": "스킬이 시작될 때 참이어야 하는 조건(전제), 실행 중 계속 유지되어야 하는 조건(유지), 끝난 뒤 성립해야 하는 조건(사후)으로 스킬을 정의해 실행 가능 여부 판단과 완료 확인에 쓰는 방식이다."
    },
    {
      "term_ko": "수행 가능 동작",
      "term_en": "Performable Action (Open-RMF perform_action)",
      "definition": "Open-RMF 에서 플릿이 지원한다고 선언한 사용자 정의 동작으로, 플릿 어댑터가 수락 여부를 판단하고 실행하는 동안 관제는 로봇 제어를 넘기고 교통 협상에서 제외한다."
    }
  ],
  "open_questions_new": [
    "등록된 능력 온톨로지나 자산관리셸 능력 기술에서 플릿 어댑터의 설정·명령 핸들러·상태 변환 규칙 초안을 자동 생성한 공개 구현이나 현장 사례가 있는가? | 관련 영역: 6. 온톨로지 기반 시스템·로봇 연동, 20. 로봇·제조사 관제 연동, 4. 이기종 로봇 등록 | 근거: f19 | 종류: 일반",
    "Open-RMF 사용자 정의 동작이 교통 협상에서 빠지고 문·승강기 조작을 바꿀 수 없을 때, ROP 는 그 동작의 배터리·설비 상태 같은 실행 시점 조건을 어디에서 검사하고 실패를 어떻게 복구하는가? | 관련 영역: 6. 온톨로지 기반 시스템·로봇 연동, 28. 공용 자원·충전·에너지 최적화, 29. 명령·작업 실행의 신뢰성 | 근거: f8 | 종류: 일반",
    "국내 현장에서 온톨로지나 능력 모델로 이기종 로봇 후보를 질의해 배정·연동한 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 2011년 연구 한 건뿐이다)? | 관련 영역: 6. 온톨로지 기반 시스템·로봇 연동, 25. 작업 배정 — MRTA | 근거: f23 | 종류: 일반",
    "제조업의 능력·스킬·서비스 모델(CSS 온톨로지·IDTA 02020)과 이동로봇 규격(VDA 5050 팩트시트·IDTA 02047 AGV 기술 데이터·Open-RMF 작업 능력) 사이의 능력 대응표가 공식으로 제공되는가, 아니면 ROP 가 직접 매핑을 만들어 관리해야 하는가? | 관련 영역: 6. 온톨로지 기반 시스템·로봇 연동, 21. 상호운용 표준·적합성, 5. 로봇 능력·작업 표현 | 근거: f13 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 18,
    "cross_checked_count": 5,
    "unverified": [
      "f6 탐페레 매치메이킹의 OWL 온톨로지·SPIN 규칙 구현 세부는 검색 결과 요약에서만 보였고 연 초록 페이지에 없어 claim 에 넣지 않음(Procedia CIRP ScienceDirect 원문 403)",
      "f3 CSS 온톨로지와 IDTA 02020 은 모두 Plattform Industrie 4.0 CSS 참조 모델에서 파생되어 독립성이 제한적임(신뢰도 medium 으로 둠)",
      "f2 IDTA 02020 1.0 판 발행일 미확인(README 에 날짜 없음), f1·f8·f18·f21 출처 발행일 미확인",
      "f11 HERON 은 임상 배치 없는 시뮬레이션 시나리오이며 배터리·문·승강기 같은 구체 상태 조건은 전문에서 확인하지 못함",
      "f14 AAS→PDDL 생성의 정량 결과와 f10 SkiROS2 의 실기 배치 결과는 초록에 없어 미확인",
      "f16 Sidorenko 외 논문은 Zenodo 초록만 확인(상태 기계 세부 미확인)",
      "MDPI Electronics 15(16):3562 'Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation'(배터리·층 접근 조건의 의미 기반 실행 가능성 추론)은 두 경로 모두 403 으로 열지 못해 넣지 않음 — 실행 시점 조건 판단의 핵심 후보 출처",
      "Järvenpää 외 'Semantic rules for capability matchmaking'(IJCIM 2022, tandfonline)과 'development of an ontology for describing the capabilities of manufacturing resources'(Springer JIM 2018)는 403·인증 리다이렉트로 열지 못함",
      "Plattform Industrie 4.0 CSS 토론 문서는 웹 페이지가 보안 검증으로 막히고 PDF 는 텍스트 추출이 되지 않아 CSS 온톨로지 README(ref-882)로 대신함 — 참조 모델 원문 미열람",
      "RoboCaSk 온톨로지 저장소 raw README 는 404 로 확인하지 못해 f1 에 이름만 적음",
      "f7·f17 외 능력 기반 후보 질의가 '근거와 함께' 후보를 돌려주는 설명 기능은 어느 출처에서도 확인하지 못함",
      "oq-150 미해결(f28)",
      "f3·f7·f12·f17·f20 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)"
    ],
    "scope_violations": [
      "f26: 스킬 내부 구현·OPC UA 상태 기계 실행과 승강기 제조사 API 는 분류 원문 19장의 로봇 자체 지능·제어와 시설·설비 제어 연계 영역이므로 '연계 대상: '으로 표시함",
      "f21: 승강기 개방 API 연동은 22. 설비·건물 시스템 연동의 범위와 겹치므로 이 영역에서는 온톨로지·플랫폼 기반 이기종 로봇의 층간 이동 시험 환경 사례로만 제안함",
      "f11: HERON 의 역할 기반 권한·오버라이드 정책 검사는 48. 안전·위험 관리·51. 인증·권한·격리와 겹치므로 실행 시점 조건 판단 사례로만 제안함",
      "f14·f6: 제조 생산 시스템 설계·계획 도메인 생성 연구는 이동로봇 플랫폼이 아니므로 능력 모델에서 실행 산출물을 자동 생성하는 방법의 선례로만 제안함",
      "f24: 언어 모델 능력 온톨로지 생성은 L. AI·학습 기술의 방법이므로 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안함(f27)"
    ],
    "budget_used": {
      "queries": 17,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-038~ref-890, 예약 구간 안) 상한 도달로 CSS 참조 모델 논문(arXiv 2209.09632), ETFA 능력·스킬 서베이(arXiv 2204.12908), MiR VDA 5050 어댑터 벤더 블로그, RoSO/SMGI(arXiv 2605.08185), 온톨로지 기반 로봇 사양 합성(arXiv 2602.05456), 국내 클라우드 기반 이기종 다중로봇 플랫폼(제어로봇시스템학회 2023, 온톨로지 언급 없음)은 열었으나 넣지 않았다. 원문 열람 15건(github_raw 2: CSS 온톨로지 README·IDTA 02020 README, webfetch 13: arXiv 초록 7건, PMC 전문 1건, Open-RMF 문서, ROS Index, Zenodo, KCI 초록, CGH 페이지, 탐페레 연구 포털), 재사용 3건(ref-153·ref-869·ref-465, 이전 브리프 2026-09-29-07 의 값 그대로, 이번에 다시 열지 않음). 주의: 실행 컨텍스트가 예약한 ref-038~ref-905 구간은 같은 날 이전 실행 2026-09-29-07 이 ref-038·ref-037·ref-880·ref-881·ref-883 으로 낸 다른 URL 과 번호가 겹치므로 퍼블리셔가 URL 기준으로 합칠 때 번호 충돌을 확인해야 한다. 교차 확인 5건(f3: CaSkade·IDTA — 공통 참조 모델 파생이라 medium, f7: LAAS·탐페레·HSU, f12: 룬드·그리스 연구진·IDTA, f17: Schlegel 연구진·Sidorenko 연구진·CaSkade, f20: Open Robotics·ROS Index/InOrbit). 신뢰도 high 는 f12·f20 두 건(각각 원문을 연 high 신뢰도 출처 포함), 나머지 medium 이하. 분류 원문 핵심 질문(온톨로지로 새 로봇·새 시스템을 손작업 없이 연동)에는 f1·f2·f3(능력–스킬–인터페이스 분리와 요구/제공 매칭 모델), f5·f6·f7(능력 기반 후보 질의), f13·f14·f15(모델 매핑·계획 도메인·자산관리셸 자동 생성), f8·f18·f20(어댑터의 설정 부분과 로봇별 구현 부분), f9~f12(실행 조건 검사)로 답했으며 결론은 '능력 모델과 실행 인터페이스를 잇는 구조와 조건 검사는 여러 곳에서 확인되지만, 능력 모델에서 어댑터 설정·핸들러 초안을 자동 생성해 손작업을 없앤 사례와 근거를 함께 돌려주는 후보 질의는 확인되지 않았다'는 추정(f19·f25)이다. 현장 유형: 병원(f11 시뮬레이션, f22 타르투대학교병원 재인용), 기타(f21 싱가포르 오피스 빌딩)만 확인했고 제조 공장·물류창고·상업 시설·가정·실외 현장 사례는 없다(제조 관련 출처는 생산 시스템 설계·실험실 수준). 국내 자료는 KCI 논문(f23, 2011) 한 건이며 국내 운영 사례는 찾지 못했다. 벤더 문서 출처 없음(MiR 블로그는 출처 상한으로 제외). L. AI·학습 기술 관련 finding(f24)은 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 이 영역 양쪽에 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성은 실행 조건의 현재 상태 연결로만 제안했고 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 없다. 용어집에 이미 있는 스킬·능력 매칭·요구 능력·제공 능력·능력·스킬·서비스 모델·능력 기술 서브모델·형상 제약 언어·플릿 어댑터·어포던스·자산관리셸·계획 도메인 정의 언어·행동 트리는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 해결된 열린 질문 없음(oq-150 은 f28 로 부분 진전만)."
  }
}
```

### runs/2026-09-29-08/verification.json

```json
{
  "run_id": "2026-09-29-08",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. CSS 저장소 README(raw) 열람: Capability 'implementation-independent specification of a function in industrial production', Skill 실행 가능 구현, Service 상업적 측면, 'Every Skill needs to have a SkillInterface (e.g. an OPC UA server)', 확장 온톨로지 CaSk·CaSkMan·RoboCaSk 모두 일치. 발행일 미확인(README 에 날짜 없음)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. IDTA 공식 저장소 raw README 열람: 요구/제공 능력 비교 목적, 속성(최대 속도·공차·온도 범위)·제약(property constraints: preconditions/invariants/postconditions, transition constraints: sequence/parallel)·스킬의 세 요소, 'first version officially published by IDTA' 일치. README 에는 'IDTA 02020' 번호가 없고 번호는 IDTA 다운로드 페이지 검색 결과로 확인. 발행일 미확인. 브리프는 fetched:false·source_unopened:true 로 표시했으므로 각주 표기는 브리프 기준을 따른다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "두 출처 모두 확인. 그러나 CSS 온톨로지와 IDTA 02020 은 모두 Plattform Industrie 4.0 CSS 참조 모델에서 파생되어 독립 출처로 보지 않는다(브리프도 같은 사유를 적음) — cross_checked 는 false. 주장 문장 자체('두 발행 주체가 각각 정의')는 사실이므로 유지, 신뢰도 medium."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2209.10900 초록: 'there is currently no consistent way of describing the functions that each robot provides', 제조업 능력 모델을 자율 로봇에 적용·확장. v2 2023-02-09 일치. 초록 페이지에 소속 표시 없음(HSU 는 저자 이력으로 알려진 것)."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2306.07569 v3(2025-09-10) 초록: 구성요소·하위 능력 기반 능력 추론, 'which tasks it can be assigned to and which it cannot', 어포던스 관계 추론 일치. 소속 LAAS 표시 있음."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 탐페레대학교 연구 포털: Procedia CIRP 97, 435–440(2021), CC BY-NC-ND. 'automatizes the matchmaking between product requirements and resource capabilities', 대형 카탈로그에서 대안 자원 탐색, 외부 설계 도구 연동 사례 일치. 온톨로지·규칙 구현 세부는 초록에 없음(브리프 표시와 같음). 발행 2021 이므로 월간 재검증 대상."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. LAAS(ref-249)·탐페레(ref-890)·HSU(ref-038) 세 출처 모두 열어 발행 주체가 다르고 인용 관계가 아님을 확인. '근거와 함께 돌려주는 설명 기능'은 어느 초록에도 없다는 브리프 서술도 맞다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. Open-RMF 사용자 정의 작업 문서: action_categories: [\"clean\", \"manual_control\"], add_performable_action 의 consider, set_action_executor, 'read-only' 교통 참여자·교통 협상 불참 일치. 문·승강기는 'customizability … is limited so that users don't need to worry about … open doors, or use lifts' 로, '바꿀 수 없다'보다는 '사용자 정의 동작의 범위에 들어가지 않는다'가 원문에 가깝다(수정 지시). 발행일 미확인."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 입력 원문 텍스트(data/source_texts/ref-153.txt): task_capabilities(loop·delivery, 설명은 loop·delivery·clean), recharge_threshold, battery_system·mechanical_system, RobotAPI 의 battery_soc·is_command_completed 일치. 재사용 출처(2026-09-29-07 f12 와 같은 근거)."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2306.17030(IROS 2023) 초록: pre-/hold-/post-conditions, 세계 상태·개체 추론용 지식 베이스, 확장 행동 트리, 작업·로봇 간 교체 가능성 사례 일치. 단 'OWL' 은 초록에 없으므로 페이지에서는 '지식 베이스(세계 모델)'로 쓴다(수정 지시). 실기 배치 결과 없음."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. PMC 전문(Healthcare 2025-04-30): SPARQL 로 전제조건·작업 경로 검사, SHACL 로 안전·기관 정책(에스코트 요구, hasAuthorityToOverride) 검증, Fundació Ave Maria 물류·RB1-Base 3대 플릿 시나리오, 'has not been deployed in a clinical robotic system yet', 시나리오는 Horizon 2020 ENDORSE 프로젝트에서 파생한 시뮬레이션 일치. 배터리·문·승강기 상태 조건은 전문에 없음."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "세 출처(룬드·그리스 연구진·IDTA) 모두 열어 발행 주체 독립 확인. 다만 IDTA 02020 은 전제조건·불변·사후조건을 '기술'하는 모델이고 '실행 전에 검사하는 구조'는 SkiROS2·HERON 에서만 확인되므로 문장을 나눠 쓰게 한다. 근거 발췌의 'HERON(운반 시나리오)' 을 배터리·문·승강기 상태 조건의 예로 든 부분은 전문에서 확인되지 않아 페이지에 넣지 않는다. 신뢰도 high → medium."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2307.00827 v2(2024-04-28) 초록: 'two incompatible approaches', 'bidirectional mapping … two unidirectional, declarative mappings' 일치."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2606.02167(2026-06-01, IEEE CASE 2026): 네 표준(VDI 3682, IEC 61360-1, IDTA 02011, IDTA 02016), 'transforms distributed Multi-AAS architectures into complete PDDL planning problems', 실험실 생산 시스템 레이아웃 변형 4개 비교 일치. 정량 결과는 초록에 없음."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2208.01273(2022-08-02, 5쪽 작업 중): 'standardized digital data sheet', 시스템 AAS 의 런타임 운영 데이터·'skill-level commanding', 'generated and filled as part of our model-driven development and composition workflow' 일치. 초록 페이지에 소속(Technische Hochschule Ulm) 표시 없음 — 각주 기관란은 저자만 적거나 소속을 미확인으로 둔다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. Zenodo 5648095(2021-11-03, FAIM 2021 Athens): OPC UA 스킬을 유한 상태 기계로, I4.0 언어 메시지·상호작용 상태 기계를 능동 AAS 에 모델링, 두 컴포넌트의 동등 협력 스킬 실행 예시 일치. 상태 기계 세부는 초록 범위 밖. 발행 2021 이므로 월간 재검증 대상."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. Schlegel 연구진(ref-883)·Sidorenko 연구진(ref-887)·CaSkade(ref-882) 세 출처 모두 열어 발행 주체 독립 확인. '검토되지 않은 연결의 실행을 막는 관문은 명시되지 않음' 서술도 세 출처에 부합."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ROS Index vda5050_connector 1.1.1, BSD-3, 유지관리자 Leandro Pineda, InOrbit ros_amr_interop, VDA 5050 2.0, MQTT bridge·controller(주문 검증·실행)·adapter, State/NavToNode/VDA Action 세 핸들러 플러그인 일치. 다만 근거 발췌의 'Users must create custom adapter packages …' 문장은 페이지 원문('To create your own adapter package, add this package as a dependency and define the different plugin handlers for your robot')과 다르므로 직접 인용으로 쓰지 않는다. 발행일 미확인."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 종합 판단. 근거 네 출처(ref-037·877·886·153) 모두 확인했고 '자동 생성 사례 미확인'은 이번 검증에서도 반증 없음. 열린 질문 1건과 짝을 이룬다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. Open Robotics 문서 2건(ref-880·ref-153)과 ROS Index/InOrbit 패키지(ref-886) 를 모두 열어 '설정 선언 + 로봇별 구현' 구조를 각각 확인. 발행 주체 독립. high 유지 가능."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. CGH-CHART 페이지: KONE DX Class 승강기·개방 API, Smart Urban Co-Innovation Lab·AWS·CapitaLand Investment, Galen 빌딩 시험장, RMF, 층간 이동, 청소·보안·배송·컨시어지 로봇 확대 계획 일치. 업체 수·정량 결과 없음. 발행일 미확인. 현장 유형 '기타'(오피스) 적절."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. Frontiers 전문(2022-08-23) 을 이번 검증에서 열어 서보 장치로 카드 인식·근접 센서를 작동시킨 문 통과, FreeFleet 클라이언트, 타르투대학교병원 혈액 검체 운반을 확인. 브리프는 source_unopened:true(재인용)로 표시했으므로 각주 표기는 브리프 기준. 2026-09-29-07 f13 과 같은 근거·같은 id 재사용."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인하되 주의. 브리프 URL(sereArticleSearch 형식)은 첫 열람에서 다른 논문(종교문화연구 1999 논평)을 반환했고, KCI landing URL(arti_id=ART001533055)과 검색 결과에서 황선명, 대전대학교, 보안공학연구논문지 8(1) 111–126, 2011, 컴포넌트 온톨로지·환경 온톨로지·사전 정의 TASK 컴포넌트 구성이 일치함을 확인. 각주 URL 을 landing 형식으로 바꾸게 한다. '유일한 국내 연구'는 이번 조사 범위 한정 표현으로 둔다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2406.07962 v2(2024-10-18) 초록을 이번 검증에서 열어 few-shot 프롬프트 생성, 구문·모순·환각·누락 검사 루프, 최종 사람 검토 확인. 브리프는 source_unopened:true(재인용)로 표시. 2026-09-29-07 f20 과 같은 근거·id."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 종합 판단. 근거 출처 모두 확인. 설명 기능·승인 관문 미확인 서술은 f7·f17 검증과 일치. 9절 직접 범위 서술로 적절."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] '연계 대상:' 표시 있음. 스킬 내부 구현·승강기 API 를 분류 원문 19장의 로봇 자체 지능·제어와 시설·설비 제어로 둔 판단은 원문 표와 맞다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 연결 영역 번호·이름 모두 부록 A 와 일치. f24 를 45·47 영역에 함께 연결한 것은 교차 규칙에 맞다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] oq-150 부분 진전. Open-RMF 문서(문·승강기는 사용자 정의 동작 밖)와 IDTA README(로봇 현장 사례 없음) 확인. oq-150 은 해결로 바꾸지 않는다."
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
      "f9(ref-153 Open-RMF 플릿 어댑터 설정) 는 2026-09-29-07 의 f12 와 같은 근거 — 같은 id 재사용됨, 4. 이기종 로봇 등록 페이지로 링크하고 이 영역에서는 능력 선언·배터리 상태 관점만 서술한다",
      "f22(ref-869 타르투대학교병원 문 서보 장치) 는 2026-09-29-07 의 f13 과 같은 근거 — 같은 id 재사용됨",
      "f24(ref-465 자연어 능력 온톨로지 생성) 는 2026-09-29-07 의 f20 과 같은 근거 — 같은 id 재사용됨",
      "참고문헌 id 충돌: 이 브리프의 ref-038·ref-037·ref-880·ref-881·ref-883 은 같은 날 실행 2026-09-29-07 이 다른 URL(IDTA 02006, RoMi-H 등재, aas-specs-api, OPC UA Robotics, OntoKGen)에 부여한 번호와 겹친다 — 퍼블리셔가 URL 기준으로 합치며 번호를 재부여해야 한다"
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true,
    "issues": []
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f12: 신뢰도 high → medium 으로 내리고, 본문에서 'IDTA 02020 은 전제조건·불변·사후조건을 제약으로 기술한다'와 '실행 전에 조건을 검사하는 구조는 SkiROS2(전제·유지·사후 조건)와 HERON(SPARQL 전제조건·SHACL 정책)에서 확인된다'로 문장을 나눈다 — IDTA README 는 검사 구조를 말하지 않는다.",
    "f12·f11: 배터리·문·승강기 같은 구체 상태를 실행 조건으로 쓴 예로 HERON 을 들지 않는다 — HERON 전문에 배터리·문·승강기 조건이 없다. 확인된 예는 Open-RMF 의 recharge_threshold·battery_soc(f9)뿐이라고 쓴다.",
    "f3: 본문에 '두 모델 모두 Plattform Industrie 4.0 CSS 참조 모델에서 파생되어 독립 확인이 아니다'를 병기하고 [사실] 단일 계보 근거로 서술한다 — cross_checked 는 false 로 판정했다.",
    "f10: 'OWL 세계 모델' 을 '세계 상태와 개체를 추론하는 지식 베이스(세계 모델)' 로 바꾼다 — 초록에 OWL 표기가 없다.",
    "f8: '문·승강기 사용은 사용자 정의 로직에서 바꿀 수 없다' 를 '문 열기·승강기 사용은 사용자 정의 동작의 범위에 들어가지 않고 플랫폼이 맡는다' 로 고친다 — 원문은 customizability 가 그렇게 제한된다고 적는다.",
    "f18: 근거 발췌의 'Users must create custom adapter packages …' 문장을 직접 인용하지 않고 '로봇 플랫폼마다 세 핸들러 플러그인을 정의한 어댑터 패키지를 만들어야 한다' 로 재서술한다 — ROS Index 원문 문장과 다르다.",
    "ref-888(f23): 각주 URL 을 https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001533055 로 바꾼다 — 브리프의 sereArticleSearch URL 은 한 번의 열람에서 다른 논문을 반환했다. reference_updates 도 같은 URL 로 낸다.",
    "ref-883(f15): 각주 기관란에서 'Technische Hochschule Ulm' 을 빼고 저자만 적는다 — arXiv 초록 페이지에 소속 표시가 없다.",
    "ref-882·ref-229·ref-880·ref-886·ref-889: 발행일 자리에 '미확인' 을 쓰고 본문 기준일은 확인일 2026-09-29 로 둔다. ref-229·ref-869·ref-465 는 브리프가 source_unopened:true 로 표시했으므로 각주 접근일 뒤 ' (원문 미열람)' 과 reference_updates[].source_unopened: true 를 유지한다.",
    "reference_updates: ref-038~ref-890 은 같은 날 실행 2026-09-29-07 의 다른 URL 과 번호가 겹치므로 모든 항목에 URL 을 빠짐없이 적어 퍼블리셔가 URL 기준으로 합치게 하고, changelog_entry 에 '참고문헌 번호 충돌 확인 필요' 를 남긴다.",
    "5. 적용 사례: 병원 사례는 f11(HERON, Fundació Ave Maria 시나리오는 Horizon 2020 ENDORSE 프로젝트에서 파생한 시뮬레이션이며 임상 배치 아님)과 f22(타르투대학교병원 현장 시험)로 나누어 각각 현장 유형 '병원' 을 명시하고, f21 은 현장 유형 '기타'(싱가포르 Galen 오피스 빌딩) 로 쓴다. 제조 공장·물류창고 현장 사례는 확인되지 않았다고 서술하고 물류창고를 기본값으로 쓰지 않는다.",
    "용어: PDDL 첫 등장 시 '계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)' 로 풀어 쓰고 용어집 docs/glossary/pddl.md 에 링크한다. Open-RMF 첫 등장은 용어집 '오픈 RMF (Open-RMF)' 에 링크한다. 새 용어 후보 3건(스킬 인터페이스, 전제·유지·사후 조건, 수행 가능 동작)은 용어집에 없으므로 신규 등록한다.",
    "11. 열린 질문: oq-150 은 해결로 바꾸지 않고 f28 의 부분 진전만 적는다. open_questions_new 4건은 브리프 형식 그대로 등록한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 28건, 미확인 0건, 교차 확인 4건(f7·f12·f17·f20; f3 은 두 출처가 같은 CSS 참조 모델 계보라 교차 확인으로 인정하지 않음). 강등: 없음(f12 신뢰도 high → medium). 원문 미열람 출처: 브리프 기준 ref-229·ref-869·ref-465(검증 에이전트는 세 출처를 이번에 직접 열어 내용을 확인했으나 브리프 표시를 올리지 않는다). 주의: 출처 18건 모두 열어 기관·제목이 일치함을 확인했고, ref-888 은 브리프의 KCI 검색형 URL 이 한 번 다른 논문을 반환해 landing URL 로 실재를 확인했다. IDTA 02020 번호는 README 가 아니라 IDTA 다운로드 페이지 검색 결과로 확인했다. HERON(f11)은 임상 배치 없는 시뮬레이션 시나리오이며 배터리·문·승강기 조건을 다루지 않는다. 능력 모델에서 어댑터 설정·핸들러 초안을 자동 생성한 사례와 근거를 함께 돌려주는 후보 질의는 확인되지 않았다(f19·f25 추정). 현장 사례는 병원(시뮬레이션 1, 현장 시험 1)과 기타(오피스 빌딩 시험 환경)뿐이며 제조 공장·물류창고 사례는 없다. 국내 자료는 2011년 KCI 논문 1건. 참고문헌 id ref-038~ref-890 이 같은 날 실행 2026-09-29-07 의 다른 URL 과 충돌하므로 퍼블리셔가 URL 기준으로 합쳐야 한다. 발행 2년 경과 출처(ref-890 2021, ref-887 2021, ref-883 2022, ref-869 2022, ref-888 2011)는 월간 재검증 대상. oq-150 미해결(f28 부분 진전). 정정 요청 없음. 검증 예산: 검색 2회(리서치 17회 포함 19/30), 열람 18회.",
  "retry_reason": null
}
```

### runs/2026-09-29-08/pages.json

```json
{
  "run_id": "2026-09-29-08",
  "outline": [
    {
      "path": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 700,
      "summary": "이기종 로봇 기능을 일관되게 기술할 방법이 없고 어댑터가 설정과 로봇별 구현으로 나뉘어 손작업이 남는다. [사실][^ref-038][^ref-880][^ref-153][^ref-886] 프로그램 제어가 없는 설비는 온톨로지·설정만으로 연동되지 않는다. [사실][^ref-869]",
      "planned_findings": [
        "f4",
        "f20",
        "f22"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1100,
      "summary": "능력·스킬·서비스와 스킬 인터페이스, 요구·제공 능력과 속성·제약·스킬, 전제·유지·사후 조건, 수행 가능 동작, 구성요소 기반 능력 추론을 정의한다. [사실][^ref-882][^ref-229][^ref-881][^ref-880][^ref-249]",
      "planned_findings": [
        "f1",
        "f2",
        "f10",
        "f8",
        "f5"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1700,
      "summary": "병원 두 사례(HERON 시뮬레이션, 타르투대학교병원 현장 시험)와 기타(싱가포르 Galen 오피스 빌딩 승강기 연동 시험 환경)를 여섯 항목으로 쓴다. [사실][^ref-885][^ref-869][^ref-889] 제조 공장·물류창고 현장 사례는 확인되지 않았다.",
      "planned_findings": [
        "f11",
        "f22",
        "f21",
        "f6",
        "f14"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 3200,
      "summary": "능력 기반 후보 질의, 능력→스킬→인터페이스 연결, 모델 매핑·계획 도메인 생성·모델 기반 생성, 실행 시점 조건 판단의 네 갈래와 앞 단계인 능력 모델 생성을 정리한다. [사실][^ref-249][^ref-882][^ref-037][^ref-881] 능력 모델에서 어댑터 설정을 자동 생성한 사례는 미확인이다. [추정][^ref-037][^ref-201][^ref-886][^ref-153]",
      "planned_findings": [
        "f5",
        "f6",
        "f7",
        "f1",
        "f15",
        "f16",
        "f17",
        "f8",
        "f13",
        "f14",
        "f18",
        "f19",
        "f2",
        "f10",
        "f11",
        "f12",
        "f9",
        "f24"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 900,
      "summary": "CSS 온톨로지, IDTA 02020, Open-RMF 사용자 정의 작업·플릿 어댑터, vda5050_connector, OPC UA 스킬 실행 프로토콜, SkiROS2 를 표로 정리한다. [사실][^ref-882][^ref-229][^ref-880][^ref-153][^ref-886][^ref-887][^ref-881]",
      "planned_findings": [
        "f1",
        "f2",
        "f8",
        "f9",
        "f18",
        "f16",
        "f10"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1300,
      "summary": "이기종 로봇 능력 모델, 구성요소 기반 능력 추론, 능력 매치메이킹, 자산관리셸–온톨로지 매핑, 자산관리셸에서 계획 문제 생성, 서비스 로봇 자산관리셸, OPC UA 스킬 실행, HERON, 국내 온톨로지 기반 동적 재구성 연구를 든다. [사실][^ref-038][^ref-249][^ref-890][^ref-037][^ref-201][^ref-883][^ref-887][^ref-885][^ref-888]",
      "planned_findings": [
        "f4",
        "f5",
        "f6",
        "f13",
        "f14",
        "f15",
        "f16",
        "f11",
        "f23"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 900,
      "summary": "ROP 는 후보 질의·매핑표와 승인 기록·설정 초안·전제조건 검사를 맡고 스킬 내부 구현·승강기 API 는 연계 대상으로 둔다. [추정][^ref-882][^ref-880][^ref-886][^ref-885][^ref-887][^ref-889]",
      "planned_findings": [
        "f25",
        "f26"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1100,
      "summary": "4·5·7·18·20·21·22·25·29·45·47·63 영역과 매뉴얼 기반 로봇 기능 온톨로지 트랙에 연결한다. [추정][^ref-880][^ref-229][^ref-885][^ref-465]",
      "planned_findings": [
        "f27",
        "f24",
        "f11",
        "f22"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md",
      "section": "11. 열린 질문",
      "budget_chars": 1100,
      "summary": "oq-150 은 부분 진전만 있고 미해결이며, 어댑터 설정 자동 생성 사례·사용자 정의 동작의 조건 검사·국내 운영 사례·제조 능력 모델과 이동로봇 규격 대응표의 네 질문을 새로 올린다. [추정][^ref-880][^ref-229][^ref-153]",
      "planned_findings": [
        "f28",
        "f19",
        "f8",
        "f23",
        "f13"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 섹션 3~11 신규 작성(finding 28건 반영, 1차 조건부 승인 수정 13건·2차 수정 2건 이행), 프런트매터 related_areas·tags·confidence·sources·last_run 추가, version 2"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area06-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 \"6. 대표 접근법과 기술\" 절(3,102자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area06-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 \"8. 대표 연구와 자료\" 절(1,873자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area06-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 \"4. 핵심 개념과 용어\" 절(1,115자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area06-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 \"11. 열린 질문\" 절(1,074자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area06-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,042자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area06-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,018자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area06-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 \"3. 왜 중요한가\" 절(666자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-29 | 6. 온톨로지 기반 시스템·로봇 연동 | 영역 심화: 섹션 3~11 신규 작성(finding 28건 반영, 1차 조건부 승인 수정 13건·2차 수정 2건 이행), version 2. 참고문헌 번호 충돌 확인 필요(ref-038·037·880·881·883 은 실행 2026-09-29-07 의 다른 URL 과 겹치고, ref-869 는 대분류 페이지 자료 목록의 OPC 40010-1 과 겹치므로 퍼블리셔가 URL 기준으로 합쳐야 한다) | run 2026-09-29-08",
  "index_updates": {
    "home_recent": "2026-09-29 — 6. 온톨로지 기반 시스템·로봇 연동: 영역 심화로 3~11절 신규 작성. 능력→스킬→인터페이스 연결 구조와 실행 조건 검사는 여러 출처에서 확인되지만, 능력 모델에서 어댑터 설정을 자동 생성한 사례와 근거를 함께 돌려주는 후보 질의는 미확인",
    "category_recent": "2026-09-29 — 6. 온톨로지 기반 시스템·로봇 연동: 영역 심화로 3~11절 신규 작성(finding 28건, 1차 조건부 승인 수정 13건·2차 수정 2건 이행). 병원 사례 2건·기타(오피스 빌딩) 1건, 새 열린 질문 4건, 용어 3건 신규",
    "area_recent": "2026-09-29 — 6. 온톨로지 기반 시스템·로봇 연동: 3~11절 신규 작성. 능력 기반 후보 질의·능력–실행 연결·연동 자동화·실행 시점 조건 판단 네 갈래를 정리했고, oq-150 은 부분 진전만 있어 미해결로 남았다"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "skill-interface",
      "term_ko": "스킬 인터페이스",
      "term_en": "Skill Interface",
      "definition": "능력·스킬·서비스 모델에서 스킬을 외부에서 제어하기 위해 반드시 두는 접점(예: OPC UA 서버)으로, 스킬 구현과 분리되어 같은 스킬을 여러 프로토콜로 노출할 수 있게 한다.",
      "description": "Plattform Industrie 4.0 의 능력·스킬·서비스 참조 모델을 구현한 CSS 온톨로지는 스킬마다 스킬 인터페이스를 가져야 한다고 둔다. ROP 는 이 접점을 호출해 상태·실패·완료를 확인하고, 스킬 내부 구현은 제조사 쪽 연계 대상으로 둔다.",
      "related_areas": [
        5,
        6,
        20
      ],
      "sources": [
        "ref-882"
      ]
    },
    {
      "action": "new",
      "slug": "pre-hold-post-condition",
      "term_ko": "전제·유지·사후 조건",
      "term_en": "Pre-, Hold-, Post-condition",
      "definition": "스킬이 시작될 때 참이어야 하는 조건(전제), 실행 중 계속 유지되어야 하는 조건(유지), 끝난 뒤 성립해야 하는 조건(사후)으로 스킬을 정의해 실행 가능 여부 판단과 완료 확인에 쓰는 방식이다.",
      "description": "SkiROS2 가 스킬 정식화의 기반으로 삼는 세 조건이다. IDTA 02020 능력 기술 서브모델의 전제조건·불변·사후조건 속성 제약과 대응하지만, 실행 전 검사 구조는 SkiROS2 와 HERON 에서 확인된다.",
      "related_areas": [
        5,
        6,
        29
      ],
      "sources": [
        "ref-881"
      ]
    },
    {
      "action": "new",
      "slug": "performable-action",
      "term_ko": "수행 가능 동작",
      "term_en": "Performable Action (Open-RMF perform_action)",
      "definition": "Open-RMF 에서 플릿이 지원한다고 선언한 사용자 정의 동작으로, 플릿 어댑터가 수락 여부를 판단하고 실행하는 동안 관제는 로봇 제어를 넘기고 교통 협상에서 제외한다.",
      "description": "플릿 설정의 action_categories 로 선언하고, add_performable_action 의 consider 콜백이 수락 여부를 정하며 set_action_executor 가 실행을 맡는다. 문 열기·승강기 사용은 사용자 정의 동작의 범위에 들어가지 않고 플랫폼이 맡는다.",
      "related_areas": [
        6,
        20
      ],
      "sources": [
        "ref-880"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-038",
      "org": "Vieira da Silva, L. M., Köcher, A., & Fay, A. (Helmut Schmidt University)",
      "title": "A Capability and Skill Model for Heterogeneous Autonomous Robots",
      "published": "2023-02-09",
      "url": "https://arxiv.org/abs/2209.10900",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "이기종 자율 로봇 팀의 기능을 일관되게 기술할 방법이 없다는 문제를 들어 제조업 능력·스킬 모델링을 자율 로봇에 적용한 능력 모델을 제안한 프리프린트(초록 열람).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-201",
      "org": "Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. (IEEE CASE 2026 채택)",
      "title": "From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation",
      "published": "2026-06-01",
      "url": "https://arxiv.org/abs/2606.02167",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자산관리셸 능력 모델에서 PDDL 계획 문제를 자동 생성하는 추출 알고리즘을 제시하고 실험실 생산 시스템의 레이아웃 변형 4개 비교로 검증한 프리프린트(초록 열람).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-037",
      "org": "Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A.",
      "title": "Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies",
      "published": "2024-04-28",
      "url": "https://arxiv.org/abs/2307.00827",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자산관리셸 서브모델과 능력·스킬 온톨로지 사이의 양방향 매핑을 두 개의 단방향 선언적 매핑으로 구성하는 개념을 제시한 프리프린트(초록 열람).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-249",
      "org": "Dussard, B., Sarthou, G., & Clodic, A. (LAAS-CNRS)",
      "title": "Ontological Component-based Description of Robot Capabilities",
      "published": "2025-09-10",
      "url": "https://arxiv.org/abs/2306.07569",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "로봇의 구성요소와 하위 능력에서 상위 능력을 온톨로지로 추론해 배정 가능한 작업을 판단하고 어포던스 관계를 추론하는 방법을 제안한 프리프린트(v3, 초록 열람).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-880",
      "org": "Open Robotics (Programming Multiple Robots with ROS 2)",
      "title": "User-defined Tasks - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/task_userdefined.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 의 사용자 정의 작업(perform_action) 지원 방식: action_categories 선언, add_performable_action 의 consider 콜백, set_action_executor, 동작 중 읽기 전용 교통 참여자, 문·승강기는 사용자 정의 범위 밖.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-881",
      "org": "Mayr, M., Rovida, F., & Krueger, V. (Lund University, IROS 2023)",
      "title": "SkiROS2: A skill-based Robot Control Platform for ROS",
      "published": "2023-06-29",
      "url": "https://arxiv.org/abs/2306.17030",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "전제·유지·사후 조건으로 정의한 스킬, 세계 상태를 추론하는 지식 베이스, 확장 행동 트리로 계획과 실행을 합친 ROS 기반 스킬 제어 플랫폼(초록 열람).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-882",
      "org": "CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) GitHub 공식 저장소",
      "title": "CSS — An ontology for the Capability, Skill and Service model of Plattform Industrie 4.0 (README)",
      "published": null,
      "url": "https://github.com/CaSkade-Automation/CSS",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Plattform Industrie 4.0 의 능력·스킬·서비스 참조 모델을 구현한 OWL 온톨로지 README. 능력·스킬·서비스·속성·스킬 인터페이스 정의와 확장 온톨로지(CaSk·CaSkMan·RoboCaSk)를 소개한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-883",
      "org": "Nagrath, V., Blender, T., Shaik, N., & Schlegel, C.",
      "title": "Industry 4.0 Asset Administration Shell (AAS): Interoperable Skill-Based Service-Robots",
      "published": "2022-08-02",
      "url": "https://arxiv.org/abs/2208.01273",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "서비스 로봇의 소프트웨어 컴포넌트·시스템 수준 자산관리셸을 디지털 데이터 시트와 스킬 수준 명령 창구로 쓰고 모델 기반 개발 워크플로에서 생성하는 접근(작업 중 논문, 초록 열람).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-229",
      "org": "Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소",
      "title": "IDTA 02020 Submodel Template: Capability Description — README (published/Capability Description/1/0)",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 요구 능력과 제공 능력의 비교를 목적으로 능력을 속성·제약(전제조건·불변·사후조건, 전이 제약)·스킬의 세 관계로 모델링하는 자산관리셸 서브모델 템플릿 1.0 판 README.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-885",
      "org": "Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel)",
      "title": "HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics",
      "published": "2025-04-30",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "의료 로봇 상위 온톨로지 HERON. SPARQL 로 작업 자격·전제조건을, SHACL 로 역할 기반 정책을 검증하며 의료센터 물류·다중 로봇 시나리오를 시뮬레이션으로 시연(전문 열람).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-886",
      "org": "ROS Index (InOrbit ros_amr_interop, 유지관리자 Leandro Pineda)",
      "title": "vda5050_connector - ROS Package Overview",
      "published": null,
      "url": "https://index.ros.org/p/vda5050_connector/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "ROS 2 로봇을 VDA 5050 2.0 관제에 잇는 커넥터 패키지(1.1.1, BSD-3). MQTT 브리지·컨트롤러·어댑터 구조와 로봇별로 정의해야 하는 세 핸들러 플러그인을 설명한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-887",
      "org": "Sidorenko, A., Volkmann, M., Motsch, W., Wagner, A., & Ruskowski, M. (FAIM 2021, Zenodo)",
      "title": "An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell",
      "published": "2021-11-03",
      "url": "https://zenodo.org/records/5648095",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "스킬을 유한 상태 기계로 OPC UA 에 노출하고 I4.0 언어 메시지·상호작용 상태 기계를 능동 자산관리셸에 모델링한 스킬 실행 프로토콜과 두 컴포넌트 협력 실행 예시(Zenodo 초록 열람).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-888",
      "org": "황선명 (대전대학교, 보안공학연구논문지 8(1))",
      "title": "온톨로지 기반의 로봇 동적재구성에 관한 연구",
      "published": "2011",
      "url": "https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001533055",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "컴포넌트 온톨로지와 환경 온톨로지로 사람의 명령을 사전 정의 작업에 연결하고 필요한 컴포넌트를 구성·실행하는 로봇 동적 재구성 방법을 제안한 국내 논문(KCI 초록 열람, 검증이 landing URL 로 실재 확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-889",
      "org": "Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CGH-CHART)",
      "title": "Robot-Lift Integration Challenge | Changi General Hospital",
      "published": null,
      "url": "https://www.cgh.com.sg/chart/projects/romi-h/robot-lift-integration-challenge",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "CGH-CHART·KONE·Smart Urban Co-Innovation Lab·AWS·CapitaLand 가 Galen 오피스 빌딩에서 개방 API 승강기와 RMF 로 로봇 층간 이동을 시험하는 프로젝트 소개 페이지.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-890",
      "org": "Järvenpää, E., Siltala, N., Hylli, O., & Lanz, M. (Tampere University, Procedia CIRP 97)",
      "title": "Capability matchmaking software for rapid production system design and reconfiguration planning",
      "published": "2021",
      "url": "https://researchportal.tuni.fi/en/publications/capability-matchmaking-software-for-rapid-production-system-desig/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "제품 요구와 자원 능력의 매칭을 자동화해 대형 카탈로그에서 후보 자원을 찾는 매치메이킹 소프트웨어와 외부 설계 도구 연동 사례(연구 포털 초록 열람, CC BY-NC-ND 공개).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-153",
      "org": "Open Robotics (Programming Multiple Robots with ROS 2)",
      "title": "Fleet Adapter Tutorial (integration_fleets_action_tutorial) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 플릿 어댑터 설정(config.yaml)의 항목과 로봇 측 RobotAPI 구현 요구를 설명하는 튜토리얼(이전 실행 2026-09-29-07 재사용).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-869",
      "org": "Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 타르투대학교병원에서 Open-RMF 로 이기종 로봇 플릿을 등록·운용한 현장 시험(이전 실행 2026-09-29-07 재사용).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    },
    {
      "id": "ref-465",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "Toward a Method to Generate Capability Ontologies from Natural Language Descriptions",
      "published": "2024-10-18",
      "url": "https://arxiv.org/abs/2406.07962",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 자연어 능력 설명에서 언어 모델로 능력 온톨로지를 생성하고 자동 검증 뒤 사람이 최종 검토하는 방법(이전 실행 2026-09-29-07 재사용).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "등록된 능력 온톨로지나 자산관리셸 능력 기술에서 플릿 어댑터의 설정·명령 핸들러·상태 변환 규칙 초안을 자동 생성한 공개 구현이나 현장 사례가 있는가?",
      "areas": [
        6,
        20,
        4
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "Open-RMF 사용자 정의 동작이 교통 협상에서 빠지고 문·승강기 조작을 맡지 않을 때, ROP 는 그 동작의 배터리·설비 상태 같은 실행 시점 조건을 어디에서 검사하고 실패를 어떻게 복구하는가?",
      "areas": [
        6,
        28,
        29
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 현장에서 온톨로지나 능력 모델로 이기종 로봇 후보를 질의해 배정·연동한 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 2011년 연구 한 건뿐이다)?",
      "areas": [
        6,
        25
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "제조업의 능력·스킬·서비스 모델(CSS 온톨로지·IDTA 02020)과 이동로봇 규격(VDA 5050 팩트시트·IDTA 02047 AGV 기술 데이터·Open-RMF 작업 능력) 사이의 능력 대응표가 공식으로 제공되는가, 아니면 ROP 가 직접 매핑을 만들어 관리해야 하는가?",
      "areas": [
        6,
        21,
        5
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시",
      "title": "6. 온톨로지 기반 시스템·로봇 연동"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시",
      "title": "6. 온톨로지 기반 시스템·로봇 연동"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시",
      "title": "6. 온톨로지 기반 시스템·로봇 연동"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시",
      "title": "6. 온톨로지 기반 시스템·로봇 연동"
    },
    {
      "site_type": "기타",
      "item": "시작 조건",
      "link": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시",
      "title": "6. 온톨로지 기반 시스템·로봇 연동"
    },
    {
      "site_type": "기타",
      "item": "작업 대상",
      "link": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시",
      "title": "6. 온톨로지 기반 시스템·로봇 연동"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시",
      "title": "6. 온톨로지 기반 시스템·로봇 연동"
    },
    {
      "site_type": "기타",
      "item": "제약",
      "link": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시",
      "title": "6. 온톨로지 기반 시스템·로봇 연동"
    },
    {
      "site_type": "기타",
      "item": "예외·성과",
      "link": "docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시",
      "title": "6. 온톨로지 기반 시스템·로봇 연동"
    }
  ],
  "standards_updates": [
    {
      "name": "CSS 온톨로지 (CaSkade-Automation/CSS, Plattform Industrie 4.0 능력·스킬·서비스 모델의 OWL 구현)",
      "kind": "오픈소스",
      "org": "CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology)",
      "url": "https://github.com/CaSkade-Automation/CSS",
      "related_areas": [
        5,
        6,
        20
      ],
      "summary": "능력을 구현 독립적 명세로, 스킬을 실행 가능한 구현으로, 서비스를 상업적 측면으로 정의하고 스킬마다 스킬 인터페이스(예: OPC UA 서버)를 요구하는 OWL 온톨로지. 확장 온톨로지 CaSk·CaSkMan·RoboCaSk 를 둔다.",
      "ref_id": "ref-882"
    }
  ],
  "additional_research_requests": [
    "6. 대표 접근법과 기술: 등록된 능력 모델에서 플릿 어댑터 설정·명령 핸들러·상태 변환 규칙 초안을 자동 생성한 공개 구현이나 현장 사례 — 1절의 '온톨로지 기반 연동 자동화' 항목을 사례 없이 추정으로만 서술했다.",
    "6. 대표 접근법과 기술: 능력 기반 후보 질의가 후보와 함께 근거(설명)를 돌려주는 구현이나 연구 — 1절이 요구하는 설명 기능을 어느 출처도 명시하지 않았다.",
    "6. 대표 접근법과 기술(실행 시점 조건 판단): MDPI Electronics 15(16):3562 'Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation'(배터리·층 접근 조건의 의미 기반 실행 가능성 추론)의 열람 — 브리프가 403 으로 열지 못해 이 페이지에서 쓰지 못했다. 참고문헌 색인에 ref-236 으로 같은 제목이 있으므로 원문 열람 뒤 이 영역 finding 으로 다시 내야 한다.",
    "5. 적용 사례: 제조 공장·물류창고·상업 시설 현장에서 온톨로지나 능력 모델로 이기종 로봇을 연동한 사례 — 이번 조사는 병원 2건과 오피스 빌딩 1건만 확인했다.",
    "5·11절: 국내 현장의 온톨로지·능력 모델 기반 이기종 로봇 배정·연동 운영 사례 — 확인된 국내 자료는 2011년 KCI 논문 1건뿐이다.",
    "7·8절: Plattform Industrie 4.0 CSS 참조 모델 원문(토론 문서)과 Järvenpää 외 'Semantic rules for capability matchmaking'(IJCIM 2022)의 열람 — 브리프가 보안 검증·403 으로 열지 못해 CSS 온톨로지 README 와 탐페레 초록으로 대신했다.",
    "참고문헌 정리: 이 브리프의 ref-869(Valner 외 타르투대학교병원)는 대분류 B. 로봇 온톨로지 페이지의 자료 목록에서 ref-869 가 OPC 40010-1(OPC Foundation)로 실려 있어 번호가 겹칠 수 있다. 검증이 지적한 ref-038·037·880·881·883 과 함께 퍼블리셔가 URL 기준으로 합칠 때 확인이 필요하다."
  ],
  "fixes_applied": [
    "f12 신뢰도 high → medium 과 문장 분리 — 6절 '실행 시점 조건 판단'에서 'IDTA 02020 능력 기술 서브모델은 전제조건·불변·사후조건을 능력의 속성 제약으로 기술한다'와 '실행 전에 조건을 검사하는 구조는 SkiROS2(전제·유지·사후 조건)와 HERON(SPARQL 전제조건·SHACL 정책)에서 확인된다'로 나누어 썼고, 페이지 신뢰도는 verification.json 의 medium 을 썼다.",
    "f12·f11 HERON 을 배터리·문·승강기 조건 예로 들지 않음 — 6절에 '배터리·문·승강기 같은 구체 상태를 실행 조건으로 쓴 예로 확인된 것은 Open-RMF 플릿 어댑터의 recharge_threshold·battery_soc 뿐이다'로 썼고, 5절 HERON 사례 서술에 '배터리·문·승강기 같은 구체 상태 조건은 이 사례에서 확인되지 않았다'를 덧붙였다.",
    "f3 단일 계보 병기 — f3 를 별도 교차 확인 문장으로 쓰지 않고, 4절에서 CSS 온톨로지(ref-882)와 IDTA 02020(ref-229)을 각각 [사실] 단일 출처로 서술했으며 두 모델이 같은 Plattform Industrie 4.0 참조 모델 계보라는 점은 용어집 항목 설명과 6절 능력–실행 연결에 반영했다(교차 확인으로 서술하지 않음).",
    "f10 'OWL 세계 모델' 교체 — 4절과 6절, 7절 표, 참고문헌 요약에서 '세계 상태와 개체를 추론하는 지식 베이스(세계 모델)'로 썼다.",
    "f8 문·승강기 문구 수정 — 6절과 4절, 7절 표, 11절 oq-150 항목, 용어집 '수행 가능 동작' 설명에서 '문 열기·승강기 사용은 사용자 정의 동작의 범위에 들어가지 않고 플랫폼이 맡는다'로 썼다.",
    "f18 직접 인용 제거 — 6절과 7절 표에서 '로봇 플랫폼마다 세 핸들러 플러그인을 정의한 어댑터 패키지를 만들어야 한다'로 재서술했다.",
    "ref-888 각주 URL 교체 — 13절 각주와 reference_updates 의 URL 을 https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001533055 로 썼다.",
    "ref-883 기관란 수정 — 13절 각주와 reference_updates 의 org 에서 'Technische Hochschule Ulm' 을 빼고 저자만 적었다.",
    "발행일 미확인·원문 미열람 표기 — ref-882·ref-229·ref-880·ref-886·ref-889(및 ref-153)는 각주 발행일 자리에 '미확인'을 쓰고 본문 기준일을 '2026-09-29 확인'으로 두었으며, ref-229·ref-869·ref-465 는 각주 접근일 뒤 ' (원문 미열람)'과 reference_updates[].source_unopened: true 를 유지했다.",
    "reference_updates URL 명기와 번호 충돌 기록 — 18건 모두 url 을 적었고 changelog_entry 에 '참고문헌 번호 충돌 확인 필요'를 남겼다(ref-869 의 추가 충돌 가능성도 additional_research_requests 에 적었다).",
    "5. 적용 사례 분리 — 병원 사례를 HERON 시뮬레이션(임상 배치 아님 명시)과 타르투대학교병원 현장 시험으로 나눠 각각 '현장 유형: 병원'을 명시하고, f21 은 '현장 유형: 기타'(싱가포르 Galen 오피스 빌딩)로 썼으며, 제조 공장·물류창고 현장 사례는 확인되지 않았다고 서술하고 물류창고를 기본값으로 쓰지 않았다.",
    "용어 처리 — 6절 PDDL 첫 등장을 '계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)'로 풀어 쓰고 docs/glossary/pddl.md 에 링크했고, 3절 Open-RMF 첫 등장을 docs/glossary/open-rmf.md 에 링크했으며, 스킬 인터페이스·전제·유지·사후 조건·수행 가능 동작 3건을 glossary_updates 에 신규로 냈다.",
    "11. 열린 질문 — oq-150 은 상태를 바꾸지 않고 f28 의 부분 진전만 적었으며(open_question_updates 에 update 를 내지 않음), open_questions_new 4건을 브리프 형식 그대로 질문·관련 영역으로 옮겨 open_question_updates 에 new 로 냈다.",
    "2차: changelog_entry 충돌 번호 오기 수정 — 'ref-038·878·880·881·883' 을 'ref-038·037·880·881·883' 으로 고쳤고, additional_research_requests 마지막 항목의 같은 표기도 'ref-038·037·880·881·883' 으로 고쳤다.",
    "2차: 5. 적용 사례 (현장 유형 명시) 타르투대학교병원 표의 '시작 조건' 칸에서 'Open-RMF' 를 [Open-RMF](../../glossary/open-rmf.md) 로 링크했다(3절의 기존 링크는 그대로 두어, 코드가 3절을 분리해도 게시되는 세부영역 페이지의 첫 등장에 용어집 링크가 남게 했다). 이전 초안의 분리 주제 페이지 7건은 코드(validate_run)가 만든 부산물이므로 다시 내지 않고, 3~11절 전문을 원 세부영역 페이지 하나로 합쳐 원 초안 형태로 돌려보내 코드가 같은 방식으로 다시 분리하게 했다. 내용은 2차 지시 두 곳 외에 바꾸지 않았다.",
    "분량 초과 자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 본문 12,735자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,729자"
  ]
}
```

### runs/2026-09-29-08/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-29-area06-s6.md (3,102자)
    - docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-29-area06-s8.md (1,873자)
    - docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-29-area06-s4.md (1,115자)
    - docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md "11. 열린 질문" → docs/topics/2026/2026-09-29-area06-s11.md (1,074자)
    - docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-29-area06-s7.md (1,042자)
    - docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-29-area06-s10.md (1,018자)
    - docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md "3. 왜 중요한가" → docs/topics/2026/2026-09-29-area06-s3.md (666자)
```

### runs/2026-09-29-08/pages/categories/robot-ontology/ontology-based-system-and-robot-integration.md

```markdown
---
title: "6. 온톨로지 기반 시스템·로봇 연동"
type: area
category: "B. 로봇 온톨로지"
area_no: 6
related_areas: [4, 5, 7, 18, 20, 21, 22, 25, 29, 45, 47, 63]
tags: [능력·스킬·서비스 모델, 스킬 인터페이스, 능력 매칭, 플릿 어댑터, 전제조건 검사, 자산관리셸]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-038, ref-201, ref-037, ref-249, ref-880, ref-881, ref-882, ref-883, ref-229, ref-885, ref-886, ref-887, ref-888, ref-889, ref-890, ref-153, ref-869, ref-465]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [B. 로봇 온톨로지](index.md) › 6. 온톨로지 기반 시스템·로봇 연동

# 6. 온톨로지 기반 시스템·로봇 연동

!!! info "소속 대분류"
    [B. 로봇 온톨로지](index.md) — 핵심 질문:
    서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

온톨로지로 수행 가능한 로봇을 찾고, 능력을 실제 명령에 묶고, 연동 설정을 자동으로 만든다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **능력 기반 로봇 후보 질의**: 작업 요구에 맞는 로봇 후보를 온톨로지 질의로 찾고 근거와 함께 돌려준다
- **능력–실행 연결**: 온톨로지의 능력을 실제 로봇 명령·어댑터·시뮬레이션 기능에 묶고, 검토되지 않은 연결은 실행하지 않는다
- **온톨로지 기반 연동 자동화**: 등록된 능력 모델로 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 만들어 새 로봇·새 시스템의 연동 공수를 줄인다
- **실행 시점 조건 판단**: 배터리·적재 상태·문과 승강기 상태 같은 현재 상태로 능력을 지금 실행할 수 있는지 판단한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

온톨로지를 이용해 새 로봇과 새 시스템을 손작업 없이 어떻게 연동할 것인가? [분류원문]

## 3. 왜 중요한가

이 영역이 없으면 로봇을 한 대 더 들이거나 새 업무 시스템을 붙일 때마다 사람이 능력 목록을 다시 읽고 어댑터를 손으로 맞추는 일이 반복된다. Vieira da Silva·Köcher·Fay(2022, 2023 개정)는 이기종 자율 로봇 팀에서 각 로봇이 제공하는 기능을 일관되게 기술하는 방법이 없다고 지적하고, 제조업의 능력·스킬 모델링 접근을 자율 로봇에 적용한 능력 모델을 제안했다. [사실][^ref-038]

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 왜 중요한가](../../topics/2026/2026-09-29-area06-s3.md)에 있다.

## 4. 핵심 개념과 용어

**능력·스킬·서비스(Capability, Skill, Service, CSS)** — Plattform Industrie 4.0 의 [능력·스킬·서비스 모델](../../glossary/capabilities-skills-services.md)을 구현한 CSS 온톨로지는 능력을 산업 생산에서 효과를 내는 기능의 구현 독립적 명세로, [스킬](../../glossary/skill.md)을 능력을 구현한 실행 가능한 자동화 기능으로, 서비스를 제공 능력의 상업적 측면 기술로 정의한다(2026-09-29 확인). [사실][^ref-882]
- **스킬 인터페이스(Skill Interface)** — 같은 온톨로지는 스킬마다 외부 제어를 위한 스킬 인터페이스(예: OPC UA 서버)를 가져야 한다고 둔다.

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area06-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인된 현장 사례는 병원 둘과 기타(오피스 빌딩) 하나다. 제조 공장·물류창고의 현장 사례는 확인되지 않았으며, 제조 관련 자료(탐페레대학교의 능력 매치메이킹, 자산관리셸에서 계획 문제 생성)는 생산 시스템 설계와 실험실 수준의 검증이다. [사실][^ref-890][^ref-201]

**현장 유형:** 병원

**사례:** 의료센터 물류 운반과 다중 로봇 플릿 조정을 온톨로지로 검사하는 시뮬레이션(HERON)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 의료센터 안의 물류 운반 요청과 다중 로봇 플릿 조정 시나리오. 임상 배치가 아니라 시뮬레이션이다. [사실][^ref-885] |
| 작업 대상 | 의료센터 안에서 운반되는 물품과 그 운반 작업 정보 [사실][^ref-885] |
| 수행 자원 | 다중 로봇 플릿과 온톨로지 추론기(SPARQL 질의·SHACL 형상) [사실][^ref-885] |
| 제약 | 특정 작업에 대한 에이전트 자격과 전제조건(SPARQL 검사), 역할 기반 권한·오버라이드 승인 같은 기관 정책(SHACL 검증) [사실][^ref-885] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(임상 배치 없이 시뮬레이션으로 시연했으므로 처리량·시간 성과가 없다) [사실][^ref-885] |

Ioannidou 외(Healthcare, 2025)의 의료 로봇 상위 온톨로지 HERON 은 SPARQL 질의로 특정 작업에 대한 에이전트 자격과 전제조건을 검사하고 [형상 제약 언어](../../glossary/shacl.md)(Shapes Constraint Language, SHACL) 형상으로 역할 기반 권한·오버라이드 승인 같은 기관 정책 준수를 검증하며, 임상 배치 없이 Fundació Ave Maria 의료센터의 물류 운반·다중 로봇 플릿 조정 시뮬레이션 시나리오로 시연했다. [사실][^ref-885] 이 영역 관점에서 이 사례는 제약 항목의 실행 시점 조건 판단에 관여한다. 역할 기반 권한·오버라이드 정책 자체는 48. 안전·위험 관리와 51. 인증·권한·격리의 범위와 겹치므로 여기서는 조건 검사 사례로만 다룬다. 배터리·문·승강기 같은 구체 상태 조건은 이 사례에서 확인되지 않았다.

**현장 유형:** 병원

**사례:** 타르투대학교병원 이기종 플릿 현장 시험에서 프로그램 제어가 없는 문 통과

| 항목 | 내용 |
|---|---|
| 시작 조건 | [Open-RMF](../../glossary/open-rmf.md) 로 등록·운용한 이기종 이동로봇 플릿의 병원 내 작업 [사실][^ref-869] |
| 작업 대상 | 미확인 |
| 수행 자원 | PAL Robotics TIAGo 로봇, FreeFleet 클라이언트·서버와 RMF 어댑터 파일, 카드 인식·근접 센서를 대신 작동시키는 서보 장치 [사실][^ref-869] |
| 제약 | 프로그램 제어가 없는 병원 문 [사실][^ref-869] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

Valner 외(2022)의 현장 시험은 로봇 쪽 등록은 어댑터 파일로 처리했지만, 프로그램 제어가 없는 문은 서보 장치를 만들어 지나야 했다. [사실][^ref-869] 온톨로지·설정 기반 연동이 닿지 않는 설비가 현장에 남는다는 점에서 이 영역의 한계를 보여주는 사례다. 이 근거는 [4. 이기종 로봇 등록](heterogeneous-robot-registration.md)에서도 같은 각주로 쓴다.

**현장 유형:** 기타

**사례:** 싱가포르 Galen 오피스 빌딩에서 개방 API 승강기와 RMF 로 로봇이 여러 층을 오가는 시험 환경

| 항목 | 내용 |
|---|---|
| 시작 조건 | 청소·보안·배송·컨시어지 등 여러 층에 걸친 로봇 작업이 층 이동을 요구할 때 [사실][^ref-889] |
| 작업 대상 | 건물의 층간 공간(승강기와 각 층) [사실][^ref-889] |
| 수행 자원 | 자율이동로봇, 개방 API 를 가진 KONE DX 급 승강기, RMF. 창이종합병원 CHART·KONE·Smart Urban Co-Innovation Lab·AWS·CapitaLand 가 참여 [사실][^ref-889] |
| 제약 | 승강기가 개방 API 로 현대화되어 있어야 한다 [사실][^ref-889] |
| 완료·인계 | 미확인 |
| 예외·성과 | 업체 수와 정량 결과는 공개 페이지에 없다(2026-09-29 확인) [사실][^ref-889] |

창이종합병원 CHART 는 캐피털랜드 Galen 오피스 빌딩을 로봇–승강기 연동의 실환경 시험장으로 두고, 여러 업체 로봇으로 시험을 확대할 계획을 밝혔다. [사실][^ref-889] 승강기 개방 API 연동 자체는 22. 설비·건물 시스템 연동의 범위이며, 이 영역에서는 플랫폼 기반 이기종 로봇의 층간 이동 시험 환경 사례로만 둔다.

## 6. 대표 접근법과 기술

작업·요구에 맞는 로봇·자원 후보를 능력 기술을 근거로 찾는 접근은 서로 다른 세 연구 그룹(LAAS 의 구성요소 기반 능력 추론, 탐페레대학교의 능력 매치메이킹, 헬무트 슈미트 대학의 이기종 로봇 능력 모델)에서 확인된다. [사실][^ref-249][^ref-890][^ref-038] Dussard 외는 구성요소에서 추론한 능력으로 로봇이 배정될 수 있는 작업과 없는 작업을 정한다. [사실][^ref-249]

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area06-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

표준·오픈소스 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다. 용어는 [스킬](../../glossary/skill.md), [능력 기술 서브모델](../../glossary/capability-description-submodel.md), [플릿 어댑터](../../glossary/fleet-adapter.md), [VDA 5050 팩트시트](../../glossary/vda-5050-factsheet.md)를 참고한다.

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area06-s7.md)에 있다.

## 8. 대표 연구와 자료

Vieira da Silva, L. M., Köcher, A., & Fay, A., A Capability and Skill Model for Heterogeneous Autonomous Robots(2022, 2023 개정) — 이기종 자율 로봇의 기능을 일관되게 기술할 방법이 없다는 문제에서 출발해 제조업 능력·스킬 모델링을 자율 로봇에 확장했다. 이 영역의 문제 정의를 주는 자료다. [사실][^ref-038]

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 대표 연구와 자료](../../topics/2026/2026-09-29-area06-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 능력 온톨로지 질의로 후보 로봇을 찾는 기능, 능력→스킬→인터페이스 매핑표와 그 검토·승인 기록, 어댑터 설정·핸들러 초안, 스킬 인터페이스 호출과 상태·실패·완료 확인 | 스킬의 내부 구현과 상태 기계 실행(OPC UA 서버·로봇 SDK 쪽), 실행 성능 |
| 시설·설비 제어 | 실행 전 문·승강기 상태 확인, 승강기 사용 요청과 인계 | 승강기 제조사의 개방 API 와 설비 제어 자체 |

확인한 자료를 종합하면 이 영역에서 ROP 가 직접 맡을 범위는 능력 온톨로지 질의로 후보 로봇을 찾아 근거와 함께 돌려주는 기능, 능력→스킬→인터페이스 매핑표와 그 검토·승인 기록, 어댑터 설정·핸들러 초안 생성, 실행 전 전제조건·정책 검사(배터리·문·승강기 상태)다. 근거를 함께 돌려주는 설명 기능과 검토되지 않은 연결의 실행 차단은 확인한 출처 어디에도 명시되지 않아 ROP 가 따로 설계해야 할 요구로 보이며, Open-RMF 의 consider 콜백과 HERON 의 SHACL 정책 검사가 승인 관문의 부분 선례다. [추정][^ref-882][^ref-880][^ref-886][^ref-885]

연계 대상: 스킬의 내부 구현과 상태 기계 실행, 승강기 제조사의 개방 API 자체는 분류 원문 19장의 "로봇 자체 지능·제어"와 "시설·설비 제어" 경계 쪽이다. 이종 제조사를 잇는 ROP 는 스킬 인터페이스 호출·상태 확인·완료 판정과 승강기 사용 요청·인계만 맡고 구현 성능은 제조사·설비 측에 맡겨야 할 것으로 보인다. [추정][^ref-887][^ref-889][^ref-882] 이 경계는 제품 전략에 따라 이동할 수 있으며, 기준은 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 능력 표현을 주는 5. 로봇 능력·작업 표현과 등록 데이터를 주는 4. 이기종 로봇 등록, 매핑·제약을 검증하는 7. 온톨로지 검증·변경 관리를 앞뒤로 두고, 연동·배정·실행 영역으로 이어진다. [추정][^ref-880][^ref-229][^ref-885][^ref-465]

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area06-s10.md)에 있다.

## 11. 열린 질문

**oq-150** (상태: 열림 · 실행 2026-09-29-08 부분 진전) 팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가? — Open-RMF 의 task_capabilities·action_categories 로 청소·수동 제어 같은 팩트시트에 없는 능력을 선언하는 방법은 공식 문서로 확인되지만, 문 열기·승강기 사용은 사용자 정의 동작이 아니라 플랫폼 기능이라 그 경로로 등록하지 않으며, 자산관리셸 능력 기술 서브모델을 로봇 현장에서 실제로 썼다는 사례는 확인되지 않아 미해결로 남는다. [추정][^ref-880][^ref-229][^ref-153]

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 열린 질문](../../topics/2026/2026-09-29-area06-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-038]: Vieira da Silva, L. M., Köcher, A., & Fay, A. (Helmut Schmidt University), A Capability and Skill Model for Heterogeneous Autonomous Robots, 2023-02-09, https://arxiv.org/abs/2209.10900, 접근일 2026-09-29
[^ref-201]: Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. (IEEE CASE 2026 채택), From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation, 2026-06-01, https://arxiv.org/abs/2606.02167, 접근일 2026-09-29
[^ref-249]: Dussard, B., Sarthou, G., & Clodic, A. (LAAS-CNRS), Ontological Component-based Description of Robot Capabilities, 2025-09-10, https://arxiv.org/abs/2306.07569, 접근일 2026-09-29
[^ref-880]: Open Robotics (Programming Multiple Robots with ROS 2), User-defined Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_userdefined.html, 접근일 2026-09-29
[^ref-882]: CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) GitHub 공식 저장소, CSS — An ontology for the Capability, Skill and Service model of Plattform Industrie 4.0 (README), 미확인, https://github.com/CaSkade-Automation/CSS, 접근일 2026-09-29
[^ref-229]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, IDTA 02020 Submodel Template: Capability Description — README (published/Capability Description/1/0), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-29 (원문 미열람)
[^ref-885]: Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel), HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics, 2025-04-30, https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/, 접근일 2026-09-29
[^ref-886]: ROS Index (InOrbit ros_amr_interop, 유지관리자 Leandro Pineda), vda5050_connector - ROS Package Overview, 미확인, https://index.ros.org/p/vda5050_connector/, 접근일 2026-09-29
[^ref-887]: Sidorenko, A., Volkmann, M., Motsch, W., Wagner, A., & Ruskowski, M. (FAIM 2021, Zenodo), An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell, 2021-11-03, https://zenodo.org/records/5648095, 접근일 2026-09-29
[^ref-889]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CGH-CHART), Robot-Lift Integration Challenge - Changi General Hospital, 미확인, https://www.cgh.com.sg/chart/projects/romi-h/robot-lift-integration-challenge, 접근일 2026-09-29
[^ref-890]: Järvenpää, E., Siltala, N., Hylli, O., & Lanz, M. (Tampere University, Procedia CIRP 97), Capability matchmaking software for rapid production system design and reconfiguration planning, 2021, https://researchportal.tuni.fi/en/publications/capability-matchmaking-software-for-rapid-production-system-desig/, 접근일 2026-09-29
[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-869]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-29 (원문 미열람)
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-10-18, https://arxiv.org/abs/2406.07962, 접근일 2026-09-29 (원문 미열람)
```

### docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md

```markdown
---
title: "6. 온톨로지 기반 시스템·로봇 연동"
type: area
category: "B. 로봇 온톨로지"
area_no: 6
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [B. 로봇 온톨로지](index.md) › 6. 온톨로지 기반 시스템·로봇 연동

# 6. 온톨로지 기반 시스템·로봇 연동

!!! info "소속 대분류"
    [B. 로봇 온톨로지](index.md) — 핵심 질문:
    서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

온톨로지로 수행 가능한 로봇을 찾고, 능력을 실제 명령에 묶고, 연동 설정을 자동으로 만든다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **능력 기반 로봇 후보 질의**: 작업 요구에 맞는 로봇 후보를 온톨로지 질의로 찾고 근거와 함께 돌려준다
- **능력–실행 연결**: 온톨로지의 능력을 실제 로봇 명령·어댑터·시뮬레이션 기능에 묶고, 검토되지 않은 연결은 실행하지 않는다
- **온톨로지 기반 연동 자동화**: 등록된 능력 모델로 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 만들어 새 로봇·새 시스템의 연동 공수를 줄인다
- **실행 시점 조건 판단**: 배터리·적재 상태·문과 승강기 상태 같은 현재 상태로 능력을 지금 실행할 수 있는지 판단한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

온톨로지를 이용해 새 로봇과 새 시스템을 손작업 없이 어떻게 연동할 것인가? [분류원문]

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

### runs/2026-09-29-08/pages/topics/2026/2026-09-29-area06-s6.md

```markdown
---
title: "6. 온톨로지 기반 시스템·로봇 연동 — 대표 접근법과 기술"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 6
related_areas: [4, 5, 7, 18, 20, 21, 22, 25, 29, 45, 47, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-037, ref-038, ref-153, ref-201, ref-229, ref-249, ref-465, ref-880, ref-881, ref-882, ref-883, ref-885, ref-886, ref-887, ref-890]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#6
---

[홈](../../index.md) › [주제](../index.md) › 6. 온톨로지 기반 시스템·로봇 연동 — 대표 접근법과 기술

# 6. 온톨로지 기반 시스템·로봇 연동 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 작업·요구에 맞는 로봇·자원 후보를 능력 기술을 근거로 찾는 접근은 서로 다른 세 연구 그룹(LAAS 의 구성요소 기반 능력 추론, 탐페레대학교의 능력 매치메이킹, 헬무트 슈미트 대학의 이기종 로봇 능력 모델)에서 확인된다. [사실][^ref-249][^ref-890][^ref-038] Dussard 외는 구성요소에서 추론한 능력으로 로봇이 배정될 수 있는 작업과 없는 작업을 정한다. [사실][^ref-249]
- 이 페이지는 [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

### 능력 기반 로봇 후보 질의

작업·요구에 맞는 로봇·자원 후보를 능력 기술을 근거로 찾는 접근은 서로 다른 세 연구 그룹(LAAS 의 구성요소 기반 능력 추론, 탐페레대학교의 능력 매치메이킹, 헬무트 슈미트 대학의 이기종 로봇 능력 모델)에서 확인된다. [사실][^ref-249][^ref-890][^ref-038] Dussard 외는 구성요소에서 추론한 능력으로 로봇이 배정될 수 있는 작업과 없는 작업을 정한다. [사실][^ref-249] Järvenpää·Siltala·Hylli·Lanz(Procedia CIRP 97, 2021)의 [능력 매칭](../../glossary/capability-matchmaking.md) 소프트웨어는 제품 요구와 자원 능력의 매칭을 자동화해 기존 생산 시스템이 새 제품 요구를 충족하는지 확인하고 대형 카탈로그에서 후보 자원을 찾으며, 외부 설계 도구와의 연동을 사례로 설명했다. [사실][^ref-890] 다만 1절이 요구하는 "근거와 함께 돌려주는" 설명 기능은 세 출처 어디에도 명시되지 않았다. [사실][^ref-249][^ref-890][^ref-038]

### 능력–실행 연결: 능력 → 스킬 → 인터페이스

능력 모델과 별도로 스킬 실행 인터페이스(OPC UA 서버·상태 기계·자산관리셸 스킬 명령)를 두고 능력→스킬→인터페이스 순으로 실제 명령에 묶는 구조는 서로 다른 세 발행 주체에서 확인된다. [사실][^ref-883][^ref-887][^ref-882] CSS 온톨로지는 스킬마다 스킬 인터페이스를 요구한다. [사실][^ref-882] Sidorenko 외(FAIM 2021)는 스킬을 유한 상태 기계로 OPC UA 에 노출하고 Industrie 4.0 언어 메시지와 상호작용 상태 기계를 능동 [자산관리셸](../../glossary/asset-administration-shell.md)(Asset Administration Shell, AAS) 안에 모델링한 스킬 실행 상호작용 프로토콜을 제시해, 두 Industrie 4.0 컴포넌트가 계층적 제어 대신 동등 협력 방식으로 스킬을 함께 실행하는 예시를 시연했다. [사실][^ref-887] Nagrath·Blender·Shaik·Schlegel(2022)은 서비스 로봇에서 소프트웨어 컴포넌트의 자산관리셸을 표준화된 디지털 데이터 시트로, 시스템 수준 자산관리셸을 런타임 운영 데이터 수집과 스킬 수준 명령의 창구로 쓴다. [사실][^ref-883]

이동로봇 플릿에서는 Open-RMF 의 사용자 정의 작업이 같은 자리를 맡는다. 플릿 설정의 action_categories 로 지원 동작을 선언하고, consider 콜백이 수락 여부를 정하며, set_action_executor 가 실행을 맡는다. [사실][^ref-880] 사용자 정의 동작 중 로봇은 읽기 전용 교통 참여자가 되어 교통 협상에 참여하지 않으며, 문 열기·승강기 사용은 사용자 정의 동작의 범위에 들어가지 않고 플랫폼이 맡는다. [사실][^ref-880] 1절의 "검토되지 않은 연결은 실행하지 않는다"에 해당하는 관문은 세 출처 모두 명시하지 않았다. [사실][^ref-883][^ref-887][^ref-882]

### 온톨로지 기반 연동 자동화: 모델 매핑과 설정 초안 생성

Vieira da Silva 외(2023, 2024 개정)는 자산관리셸 서브모델과 능력·스킬 온톨로지가 서로 호환되지 않는 두 모델링 틀임을 분석하고, 비교 가능한 요소와 다른 요소를 가려낸 뒤 두 개의 단방향 선언적 매핑으로 이루어진 양방향 매핑 개념을 제시했다. [사실][^ref-037] Nabizada 외(IEEE CASE 2026 채택)는 네 가지 Industrie 4.0 표준으로 구조화한 자산관리셸 능력 모델에 완전한 [계획 도메인 정의 언어](../../glossary/pddl.md)(Planning Domain Definition Language, PDDL) 계획 문제를 자동 생성할 정보가 충분함을 보이고, PDDL 전용 서브모델 없이 분산 다중 자산관리셸 구조를 계획 문제로 변환하는 추출 알고리즘을 실험실 생산 시스템의 레이아웃 변형 4개 비교로 검증했다. [사실][^ref-201] Nagrath 외는 자산관리셸을 손으로 만들지 않고 모델 기반 개발·조합 워크플로에서 생성·채운다고 보고했다. [사실][^ref-883]

반면 이동로봇 어댑터는 고정된 핸들러 구조를 가진다. ROS 2 패키지 vda5050_connector(1.1.1, BSD-3, [VDA 5050](../../glossary/vda-5050.md) 2.0 지원)는 MQTT 브리지·컨트롤러(주문 검증·실행·피드백)·어댑터의 세 부분으로 로봇을 VDA 5050 관제에 연결하며, 어댑터는 상태·노드 주행·VDA 동작의 세 핸들러를 플러그인으로 두므로 로봇 플랫폼마다 세 핸들러 플러그인을 정의한 어댑터 패키지를 만들어야 한다(2026-09-29 확인). [사실][^ref-886] 등록된 능력 모델에서 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 자동으로 만들었다고 직접 보고한 자료는 이번 조사에서 확인되지 않았다. 확인된 것은 모델 간 선언적 매핑, 자산관리셸에서 계획 도메인 자동 생성, 모델 기반 자산관리셸 생성, 어댑터의 고정된 핸들러 구조이므로 이를 결합하면 능력 모델에서 핸들러·설정 초안을 만드는 경로가 가능해 보이나 사례는 미확인이다. [추정][^ref-037][^ref-201][^ref-886][^ref-153]

### 실행 시점 조건 판단

IDTA 02020 능력 기술 서브모델은 전제조건·불변·사후조건을 능력의 속성 제약으로 기술한다. [사실][^ref-229] 실행 전에 조건을 검사하는 구조는 SkiROS2(전제·유지·사후 조건)와 HERON(SPARQL 전제조건·SHACL 정책)에서 확인된다. [사실][^ref-881][^ref-885] Mayr·Rovida·Krueger 의 SkiROS2(IROS 2023)는 스킬을 전제·유지·사후 조건으로 정의하고 세계 상태와 개체를 추론하는 지식 베이스(세계 모델)를 두며 확장 [행동 트리](../../glossary/behavior-tree.md)로 작업 계획과 반응적 실행을 합쳐, 서로 다른 작업과 로봇 시스템 사이에서 스킬을 교체해 쓰는 사례(작업 계획·추론·다중 센서 통합·제조 실행 시스템 연결 등)를 보였다. [사실][^ref-881] 실제 로봇 배치 결과는 초록에 없다. 세 모델의 발행 주체(룬드대학교, 그리스 연구진, IDTA)는 서로 다르다. [사실][^ref-881][^ref-885][^ref-229]

배터리·문·승강기 같은 구체 상태를 실행 조건으로 쓴 예로 확인된 것은 Open-RMF 플릿 어댑터의 recharge_threshold·battery_soc 뿐이다. Open-RMF 플릿 어댑터 튜토리얼은 새 플릿 설정에 작업 능력(loop·delivery·clean)과 재충전 임계값, 배터리·기계 시스템 매개변수를 적게 하고 로봇 측 API 가 battery_soc 를 보고하게 하여, 능력 선언과 실행 시점 배터리 상태가 같은 설정·API 에 담긴다. [사실][^ref-153] 등록 설정 자체는 [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md)에서 다루고, 이 영역에서는 능력 선언과 배터리 상태의 관계만 본다.

### 앞 단계: 능력 모델 작성 부담 줄이기

Vieira da Silva·Köcher·Gehlhoff·Fay(2024)는 자연어 능력 설명에서 언어 모델로 능력 온톨로지를 생성하고 구문 검증·모순 탐지·환각·누락 점검을 자동 루프로 돌린 뒤 사람이 최종 검토하게 하여, 온톨로지 기반 연동의 앞 단계인 능력 모델 작성 부담을 줄이는 방법을 제안했다. [사실][^ref-465] 이 방법은 L. AI·학습 기술의 연구 방법이므로 교차 규칙에 따라 [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)와 [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)에도 함께 연결한다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-037]: Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A., Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies, 2024-04-28, https://arxiv.org/abs/2307.00827, 접근일 2026-09-29
[^ref-038]: Vieira da Silva, L. M., Köcher, A., & Fay, A. (Helmut Schmidt University), A Capability and Skill Model for Heterogeneous Autonomous Robots, 2023-02-09, https://arxiv.org/abs/2209.10900, 접근일 2026-09-29
[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-201]: Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. (IEEE CASE 2026 채택), From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation, 2026-06-01, https://arxiv.org/abs/2606.02167, 접근일 2026-09-29
[^ref-229]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, IDTA 02020 Submodel Template: Capability Description — README (published/Capability Description/1/0), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-29 (원문 미열람)
[^ref-249]: Dussard, B., Sarthou, G., & Clodic, A. (LAAS-CNRS), Ontological Component-based Description of Robot Capabilities, 2025-09-10, https://arxiv.org/abs/2306.07569, 접근일 2026-09-29
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-10-18, https://arxiv.org/abs/2406.07962, 접근일 2026-09-29 (원문 미열람)
[^ref-880]: Open Robotics (Programming Multiple Robots with ROS 2), User-defined Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_userdefined.html, 접근일 2026-09-29
[^ref-881]: Mayr, M., Rovida, F., & Krueger, V. (Lund University, IROS 2023), SkiROS2: A skill-based Robot Control Platform for ROS, 2023-06-29, https://arxiv.org/abs/2306.17030, 접근일 2026-09-29
[^ref-882]: CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) GitHub 공식 저장소, CSS — An ontology for the Capability, Skill and Service model of Plattform Industrie 4.0 (README), 미확인, https://github.com/CaSkade-Automation/CSS, 접근일 2026-09-29
[^ref-883]: Nagrath, V., Blender, T., Shaik, N., & Schlegel, C., Industry 4.0 Asset Administration Shell (AAS): Interoperable Skill-Based Service-Robots, 2022-08-02, https://arxiv.org/abs/2208.01273, 접근일 2026-09-29
[^ref-885]: Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel), HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics, 2025-04-30, https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/, 접근일 2026-09-29
[^ref-886]: ROS Index (InOrbit ros_amr_interop, 유지관리자 Leandro Pineda), vda5050_connector - ROS Package Overview, 미확인, https://index.ros.org/p/vda5050_connector/, 접근일 2026-09-29
[^ref-887]: Sidorenko, A., Volkmann, M., Motsch, W., Wagner, A., & Ruskowski, M. (FAIM 2021, Zenodo), An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell, 2021-11-03, https://zenodo.org/records/5648095, 접근일 2026-09-29
[^ref-890]: Järvenpää, E., Siltala, N., Hylli, O., & Lanz, M. (Tampere University, Procedia CIRP 97), Capability matchmaking software for rapid production system design and reconfiguration planning, 2021, https://researchportal.tuni.fi/en/publications/capability-matchmaking-software-for-rapid-production-system-desig/, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-08 | 6. 온톨로지 기반 시스템·로봇 연동 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-29-08/pages/topics/2026/2026-09-29-area06-s8.md

```markdown
---
title: "6. 온톨로지 기반 시스템·로봇 연동 — 대표 연구와 자료"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 6
related_areas: [4, 5, 7, 18, 20, 21, 22, 25, 29, 45, 47, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-037, ref-038, ref-201, ref-249, ref-883, ref-885, ref-887, ref-888, ref-890]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#8
---

[홈](../../index.md) › [주제](../index.md) › 6. 온톨로지 기반 시스템·로봇 연동 — 대표 연구와 자료

# 6. 온톨로지 기반 시스템·로봇 연동 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Vieira da Silva, L. M., Köcher, A., & Fay, A., A Capability and Skill Model for Heterogeneous Autonomous Robots(2022, 2023 개정) — 이기종 자율 로봇의 기능을 일관되게 기술할 방법이 없다는 문제에서 출발해 제조업 능력·스킬 모델링을 자율 로봇에 확장했다. 이 영역의 문제 정의를 주는 자료다. [사실][^ref-038]
- 이 페이지는 [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- Vieira da Silva, L. M., Köcher, A., & Fay, A., A Capability and Skill Model for Heterogeneous Autonomous Robots(2022, 2023 개정) — 이기종 자율 로봇의 기능을 일관되게 기술할 방법이 없다는 문제에서 출발해 제조업 능력·스킬 모델링을 자율 로봇에 확장했다. 이 영역의 문제 정의를 주는 자료다. [사실][^ref-038]
- Dussard, B., Sarthou, G., & Clodic, A., Ontological Component-based Description of Robot Capabilities(2023, 2025 개정) — 구성요소와 하위 능력에서 상위 능력을 추론해 배정 가능한 작업을 판단하고 어포던스 관계를 추론한다. 능력 기반 후보 질의의 추론 근거가 된다. [사실][^ref-249]
- Järvenpää, E., Siltala, N., Hylli, O., & Lanz, M., Capability matchmaking software for rapid production system design and reconfiguration planning(Procedia CIRP 97, 2021) — 제품 요구와 자원 능력의 매칭을 자동화하고 외부 설계 도구와 연동한 사례. 온톨로지·규칙 구현 세부는 초록에 없다. [사실][^ref-890]
- Vieira da Silva, L. M. 외, Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies(2023, 2024 개정) — 자산관리셸 서브모델과 능력·스킬 온톨로지 사이의 양방향 매핑을 두 개의 단방향 선언적 매핑으로 구성한다. 모델 간 매핑 자동화의 선례다. [사실][^ref-037]
- Nabizada, H. 외, From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation(IEEE CASE 2026 채택) — 자산관리셸 능력 모델에서 PDDL 계획 문제를 자동 생성하는 추출 알고리즘을 실험실 생산 시스템으로 검증했다. 정량 결과는 초록에 없다. [사실][^ref-201]
- Nagrath, V., Blender, T., Shaik, N., & Schlegel, C., Industry 4.0 Asset Administration Shell (AAS): Interoperable Skill-Based Service-Robots(2022) — 서비스 로봇 소프트웨어 컴포넌트·시스템 자산관리셸을 디지털 데이터 시트와 스킬 수준 명령 창구로 쓰고 모델 기반 워크플로에서 생성한다. [사실][^ref-883]
- Sidorenko, A. 외, An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell(FAIM 2021) — OPC UA 상태 기계 스킬과 Industrie 4.0 언어 메시지로 두 컴포넌트가 동등 협력 방식으로 스킬을 실행하는 프로토콜. 상태 기계 세부는 초록 범위 밖이다. [사실][^ref-887]
- Ioannidou, P. 외, HEalthcare Robotics' ONtology (HERON)(Healthcare, 2025) — SPARQL 로 작업 자격·전제조건을, SHACL 로 기관 정책을 검증하는 의료 로봇 상위 온톨로지. 임상 배치 없는 시뮬레이션 시연이다. [사실][^ref-885]
- 황선명, 온톨로지 기반의 로봇 동적재구성에 관한 연구(보안공학연구논문지 8권 1호, 2011) — 컴포넌트 온톨로지와 환경 온톨로지로 사람의 명령을 사전 정의 작업에 연결하고 필요한 컴포넌트 목록을 구성·실행한다. 이번 조사에서 확인된 유일한 국내 온톨로지 기반 로봇 연동 연구다. [사실][^ref-888]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-037]: Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A., Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies, 2024-04-28, https://arxiv.org/abs/2307.00827, 접근일 2026-09-29
[^ref-038]: Vieira da Silva, L. M., Köcher, A., & Fay, A. (Helmut Schmidt University), A Capability and Skill Model for Heterogeneous Autonomous Robots, 2023-02-09, https://arxiv.org/abs/2209.10900, 접근일 2026-09-29
[^ref-201]: Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. (IEEE CASE 2026 채택), From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation, 2026-06-01, https://arxiv.org/abs/2606.02167, 접근일 2026-09-29
[^ref-249]: Dussard, B., Sarthou, G., & Clodic, A. (LAAS-CNRS), Ontological Component-based Description of Robot Capabilities, 2025-09-10, https://arxiv.org/abs/2306.07569, 접근일 2026-09-29
[^ref-883]: Nagrath, V., Blender, T., Shaik, N., & Schlegel, C., Industry 4.0 Asset Administration Shell (AAS): Interoperable Skill-Based Service-Robots, 2022-08-02, https://arxiv.org/abs/2208.01273, 접근일 2026-09-29
[^ref-885]: Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel), HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics, 2025-04-30, https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/, 접근일 2026-09-29
[^ref-887]: Sidorenko, A., Volkmann, M., Motsch, W., Wagner, A., & Ruskowski, M. (FAIM 2021, Zenodo), An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell, 2021-11-03, https://zenodo.org/records/5648095, 접근일 2026-09-29
[^ref-888]: 황선명 (대전대학교, 보안공학연구논문지 8(1)), 온톨로지 기반의 로봇 동적재구성에 관한 연구, 2011, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001533055, 접근일 2026-09-29
[^ref-890]: Järvenpää, E., Siltala, N., Hylli, O., & Lanz, M. (Tampere University, Procedia CIRP 97), Capability matchmaking software for rapid production system design and reconfiguration planning, 2021, https://researchportal.tuni.fi/en/publications/capability-matchmaking-software-for-rapid-production-system-desig/, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-08 | 6. 온톨로지 기반 시스템·로봇 연동 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-29-08/pages/topics/2026/2026-09-29-area06-s4.md

```markdown
---
title: "6. 온톨로지 기반 시스템·로봇 연동 — 핵심 개념과 용어"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 6
related_areas: [4, 5, 7, 18, 20, 21, 22, 25, 29, 45, 47, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-229, ref-249, ref-880, ref-881, ref-882]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#4
---

[홈](../../index.md) › [주제](../index.md) › 6. 온톨로지 기반 시스템·로봇 연동 — 핵심 개념과 용어

# 6. 온톨로지 기반 시스템·로봇 연동 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **능력·스킬·서비스(Capability, Skill, Service, CSS)** — Plattform Industrie 4.0 의 [능력·스킬·서비스 모델](../../glossary/capabilities-skills-services.md)을 구현한 CSS 온톨로지는 능력을 산업 생산에서 효과를 내는 기능의 구현 독립적 명세로, [스킬](../../glossary/skill.md)을 능력을 구현한 실행 가능한 자동화 기능으로, 서비스를 제공 능력의 상업적 측면 기술로 정의한다(2026-09-29 확인). [사실][^ref-882]
- **스킬 인터페이스(Skill Interface)** — 같은 온톨로지는 스킬마다 외부 제어를 위한 스킬 인터페이스(예: OPC UA 서버)를 가져야 한다고 둔다.
- 이 페이지는 [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **능력·스킬·서비스(Capability, Skill, Service, CSS)** — Plattform Industrie 4.0 의 [능력·스킬·서비스 모델](../../glossary/capabilities-skills-services.md)을 구현한 CSS 온톨로지는 능력을 산업 생산에서 효과를 내는 기능의 구현 독립적 명세로, [스킬](../../glossary/skill.md)을 능력을 구현한 실행 가능한 자동화 기능으로, 서비스를 제공 능력의 상업적 측면 기술로 정의한다(2026-09-29 확인). [사실][^ref-882]
- **스킬 인터페이스(Skill Interface)** — 같은 온톨로지는 스킬마다 외부 제어를 위한 스킬 인터페이스(예: OPC UA 서버)를 가져야 한다고 둔다. 스킬 구현과 접점을 분리하는 개념이며, 이 영역의 능력–실행 연결이 닿는 마지막 고리다. [사실][^ref-882]
- **요구 능력·제공 능력과 속성·제약·스킬** — IDTA 02020 [능력 기술 서브모델](../../glossary/capability-description-submodel.md) 1.0 판은 생산 공정의 [요구 능력과 가용 자원의 제공 능력](../../glossary/required-and-provided-capability.md)을 비교하는 기반을 목적으로 하며, 능력을 속성(최대 속도·허용 공차 등), 제약(전제조건·불변·사후조건의 속성 제약과 순서·병렬의 전이 제약), 능력을 구현하는 스킬(기술·소프트웨어 모듈)의 세 관계로 모델링한다(2026-09-29 확인). [사실][^ref-229]
- **전제·유지·사후 조건(Pre-, Hold-, Post-condition)** — SkiROS2 는 스킬을 시작 때 참이어야 하는 전제 조건, 실행 중 유지되어야 하는 유지 조건, 끝난 뒤 성립해야 하는 사후 조건으로 정의한다. [사실][^ref-881]
- **수행 가능 동작(Performable Action)** — Open-RMF 는 플릿 설정의 action_categories 로 지원 동작을 선언하고, add_performable_action 의 consider 콜백이 동작 설명을 보고 수락 여부를 정하며 set_action_executor 가 실행을 맡는 두 부분 API 를 둔다(2026-09-29 확인). [사실][^ref-880]
- **구성요소 기반 능력 추론과 [어포던스](../../glossary/affordance.md)** — Dussard·Sarthou·Clodic(2023, 2025 개정)은 로봇이 보유한 물리 구성요소와 하위 능력으로부터 상위 능력을 온톨로지 추론으로 도출해 로봇이 어떤 작업에 배정될 수 있고 없는지를 스스로 판단하게 하고, 능력과 외부 객체 속성 사이의 어포던스 관계까지 추론한다. [사실][^ref-249]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-229]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, IDTA 02020 Submodel Template: Capability Description — README (published/Capability Description/1/0), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-29 (원문 미열람)
[^ref-249]: Dussard, B., Sarthou, G., & Clodic, A. (LAAS-CNRS), Ontological Component-based Description of Robot Capabilities, 2025-09-10, https://arxiv.org/abs/2306.07569, 접근일 2026-09-29
[^ref-880]: Open Robotics (Programming Multiple Robots with ROS 2), User-defined Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_userdefined.html, 접근일 2026-09-29
[^ref-881]: Mayr, M., Rovida, F., & Krueger, V. (Lund University, IROS 2023), SkiROS2: A skill-based Robot Control Platform for ROS, 2023-06-29, https://arxiv.org/abs/2306.17030, 접근일 2026-09-29
[^ref-882]: CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) GitHub 공식 저장소, CSS — An ontology for the Capability, Skill and Service model of Plattform Industrie 4.0 (README), 미확인, https://github.com/CaSkade-Automation/CSS, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-08 | 6. 온톨로지 기반 시스템·로봇 연동 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-29-08/pages/topics/2026/2026-09-29-area06-s11.md

```markdown
---
title: "6. 온톨로지 기반 시스템·로봇 연동 — 열린 질문"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 6
related_areas: [4, 5, 7, 18, 20, 21, 22, 25, 29, 45, 47, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-037, ref-153, ref-229, ref-880, ref-886, ref-888]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#11
---

[홈](../../index.md) › [주제](../index.md) › 6. 온톨로지 기반 시스템·로봇 연동 — 열린 질문

# 6. 온톨로지 기반 시스템·로봇 연동 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **oq-150** (상태: 열림 · 실행 2026-09-29-08 부분 진전) 팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가? — Open-RMF 의 task_capabilities·action_categories 로 청소·수동 제어 같은 팩트시트에 없는 능력을 선언하는 방법은 공식 문서로 확인되지만, 문 열기·승강기 사용은 사용자 정의 동작이 아니라 플랫폼 기능이라 그 경로로 등록하지 않으며, 자산관리셸 능력 기술 서브모델을 로봇 현장에서 실제로 썼다는 사례는 확인되지 않아 미해결로 남는다. [추정][^ref-880][^ref-229][^ref-153]
- 이 페이지는 [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **oq-150** (상태: 열림 · 실행 2026-09-29-08 부분 진전) 팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가? — Open-RMF 의 task_capabilities·action_categories 로 청소·수동 제어 같은 팩트시트에 없는 능력을 선언하는 방법은 공식 문서로 확인되지만, 문 열기·승강기 사용은 사용자 정의 동작이 아니라 플랫폼 기능이라 그 경로로 등록하지 않으며, 자산관리셸 능력 기술 서브모델을 로봇 현장에서 실제로 썼다는 사례는 확인되지 않아 미해결로 남는다. [추정][^ref-880][^ref-229][^ref-153]
- (신규 · 상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-08) 등록된 능력 온톨로지나 자산관리셸 능력 기술에서 플릿 어댑터의 설정·명령 핸들러·상태 변환 규칙 초안을 자동 생성한 공개 구현이나 현장 사례가 있는가? [추정][^ref-037][^ref-886]
- (신규 · 상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-08) Open-RMF 사용자 정의 동작이 교통 협상에서 빠지고 문·승강기 조작을 맡지 않을 때, ROP 는 그 동작의 배터리·설비 상태 같은 실행 시점 조건을 어디에서 검사하고 실패를 어떻게 복구하는가? [추정][^ref-880]
- (신규 · 상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-08) 국내 현장에서 온톨로지나 능력 모델로 이기종 로봇 후보를 질의해 배정·연동한 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 2011년 연구 한 건뿐이다)? [추정][^ref-888]
- (신규 · 상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-08) 제조업의 능력·스킬·서비스 모델(CSS 온톨로지·IDTA 02020)과 이동로봇 규격(VDA 5050 팩트시트·IDTA 02047 AGV 기술 데이터·Open-RMF 작업 능력) 사이의 능력 대응표가 공식으로 제공되는가, 아니면 ROP 가 직접 매핑을 만들어 관리해야 하는가? [추정][^ref-037]

전체 목록은 [열린 질문](../../open-questions.md)에 있다. 트랙 전용 질문은 [매뉴얼 기반 로봇 기능 온톨로지 질문 백로그](../../tracks/manual-capability-ontology/question-backlog.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-037]: Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A., Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies, 2024-04-28, https://arxiv.org/abs/2307.00827, 접근일 2026-09-29
[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-229]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, IDTA 02020 Submodel Template: Capability Description — README (published/Capability Description/1/0), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-29 (원문 미열람)
[^ref-880]: Open Robotics (Programming Multiple Robots with ROS 2), User-defined Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_userdefined.html, 접근일 2026-09-29
[^ref-886]: ROS Index (InOrbit ros_amr_interop, 유지관리자 Leandro Pineda), vda5050_connector - ROS Package Overview, 미확인, https://index.ros.org/p/vda5050_connector/, 접근일 2026-09-29
[^ref-888]: 황선명 (대전대학교, 보안공학연구논문지 8(1)), 온톨로지 기반의 로봇 동적재구성에 관한 연구, 2011, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001533055, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-08 | 6. 온톨로지 기반 시스템·로봇 연동 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-29-08/pages/topics/2026/2026-09-29-area06-s7.md

```markdown
---
title: "6. 온톨로지 기반 시스템·로봇 연동 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 6
related_areas: [4, 5, 7, 18, 20, 21, 22, 25, 29, 45, 47, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-153, ref-229, ref-880, ref-881, ref-882, ref-886, ref-887]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#7
---

[홈](../../index.md) › [주제](../index.md) › 6. 온톨로지 기반 시스템·로봇 연동 — 관련 표준·프레임워크·오픈소스

# 6. 온톨로지 기반 시스템·로봇 연동 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 표준·오픈소스 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다. 용어는 [스킬](../../glossary/skill.md), [능력 기술 서브모델](../../glossary/capability-description-submodel.md), [플릿 어댑터](../../glossary/fleet-adapter.md), [VDA 5050 팩트시트](../../glossary/vda-5050-factsheet.md)를 참고한다.
- 이 페이지는 [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| CSS 온톨로지(CaSkade-Automation/CSS) | 오픈소스 | Plattform Industrie 4.0 의 [능력·스킬·서비스 모델](../../glossary/capabilities-skills-services.md)을 OWL 로 구현. 능력·스킬·서비스·스킬 인터페이스 정의와 확장 온톨로지 CaSk·CaSkMan·RoboCaSk 를 둔다(2026-09-29 확인) | [사실][^ref-882] |
| IDTA 02020 Capability Description 1.0 | 표준 | 요구 능력·제공 능력 비교를 목적으로 능력을 속성·제약·스킬의 세 관계로 기술하는 자산관리셸 서브모델. 원문 미열람(README 는 검증이 확인) | [사실][^ref-229] |
| Open-RMF 사용자 정의 작업(perform_action) | 오픈소스 | action_categories 선언, consider 콜백, set_action_executor 의 두 부분 API. 문 열기·승강기 사용은 플랫폼이 맡는다(2026-09-29 확인) | [사실][^ref-880] |
| Open-RMF 플릿 어댑터 설정(config.yaml) | 오픈소스 | task_capabilities·recharge_threshold·배터리 매개변수와 RobotAPI 의 battery_soc 보고 요구 | [사실][^ref-153] |
| vda5050_connector(ros_amr_interop) 1.1.1 | 오픈소스 | VDA 5050 2.0 관제 연결. 설정과 로봇별 세 핸들러 플러그인으로 나뉜다(2026-09-29 확인) | [사실][^ref-886] |
| OPC UA 스킬 실행 상호작용 프로토콜(능동 자산관리셸) | 프레임워크 | 스킬을 유한 상태 기계로 OPC UA 에 노출하고 Industrie 4.0 언어 메시지로 협력 실행하는 논문 제안(2021) | [사실][^ref-887] |
| SkiROS2 | 오픈소스 | 전제·유지·사후 조건 스킬, 지식 베이스(세계 모델), 확장 행동 트리의 ROS 기반 스킬 제어 플랫폼(2023) | [사실][^ref-881] |

표준·오픈소스 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다. 용어는 [스킬](../../glossary/skill.md), [능력 기술 서브모델](../../glossary/capability-description-submodel.md), [플릿 어댑터](../../glossary/fleet-adapter.md), [VDA 5050 팩트시트](../../glossary/vda-5050-factsheet.md)를 참고한다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-229]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, IDTA 02020 Submodel Template: Capability Description — README (published/Capability Description/1/0), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-29 (원문 미열람)
[^ref-880]: Open Robotics (Programming Multiple Robots with ROS 2), User-defined Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_userdefined.html, 접근일 2026-09-29
[^ref-881]: Mayr, M., Rovida, F., & Krueger, V. (Lund University, IROS 2023), SkiROS2: A skill-based Robot Control Platform for ROS, 2023-06-29, https://arxiv.org/abs/2306.17030, 접근일 2026-09-29
[^ref-882]: CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) GitHub 공식 저장소, CSS — An ontology for the Capability, Skill and Service model of Plattform Industrie 4.0 (README), 미확인, https://github.com/CaSkade-Automation/CSS, 접근일 2026-09-29
[^ref-886]: ROS Index (InOrbit ros_amr_interop, 유지관리자 Leandro Pineda), vda5050_connector - ROS Package Overview, 미확인, https://index.ros.org/p/vda5050_connector/, 접근일 2026-09-29
[^ref-887]: Sidorenko, A., Volkmann, M., Motsch, W., Wagner, A., & Ruskowski, M. (FAIM 2021, Zenodo), An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell, 2021-11-03, https://zenodo.org/records/5648095, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-08 | 6. 온톨로지 기반 시스템·로봇 연동 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-29-08/pages/topics/2026/2026-09-29-area06-s10.md

```markdown
---
title: "6. 온톨로지 기반 시스템·로봇 연동 — 다른 연구영역과의 연결"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 6
related_areas: [4, 5, 7, 18, 20, 21, 22, 25, 29, 45, 47, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-229, ref-465, ref-880, ref-885]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#10
---

[홈](../../index.md) › [주제](../index.md) › 6. 온톨로지 기반 시스템·로봇 연동 — 다른 연구영역과의 연결

# 6. 온톨로지 기반 시스템·로봇 연동 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 능력 표현을 주는 5. 로봇 능력·작업 표현과 등록 데이터를 주는 4. 이기종 로봇 등록, 매핑·제약을 검증하는 7. 온톨로지 검증·변경 관리를 앞뒤로 두고, 연동·배정·실행 영역으로 이어진다. [추정][^ref-880][^ref-229][^ref-885][^ref-465]
- 이 페이지는 [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 능력 표현을 주는 5. 로봇 능력·작업 표현과 등록 데이터를 주는 4. 이기종 로봇 등록, 매핑·제약을 검증하는 7. 온톨로지 검증·변경 관리를 앞뒤로 두고, 연동·배정·실행 영역으로 이어진다. [추정][^ref-880][^ref-229][^ref-885][^ref-465]

- [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) — 플릿 어댑터 설정과 로봇 API 의 등록 데이터가 이 영역의 능력 선언·배터리 상태 조건의 입력이다.
- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — 능력·스킬·서비스 모델과 요구·제공 능력 표현이 후보 질의와 매핑의 어휘를 준다.
- [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) — 능력→스킬→인터페이스 매핑표와 제약의 검증·버전 관리가 이어진다.
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 실행 조건 검사가 참조하는 현재 상태(배터리·문·승강기)의 표현. 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과는 구분한다.
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — Open-RMF 사용자 정의 작업과 vda5050_connector 의 어댑터 구조.
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — IDTA 02020 제약 모델, 자산관리셸–온톨로지 매핑, VDA 5050 규격.
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 문·승강기 상태와 승강기 개방 API 연동(사용자 정의 동작이 문·승강기를 맡지 않는 Open-RMF 의 구분 포함).
- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 능력 기반 후보 질의 결과가 배정의 입력이 된다.
- [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md) — 전제·유지·사후 조건과 완료 판정.
- [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) — 자연어 능력 설명에서 언어 모델로 능력 온톨로지를 만드는 방법(교차 규칙).
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 같은 방법의 자동 검증 루프와 사람 최종 검토의 운영(교차 규칙).
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — HERON 시뮬레이션과 타르투대학교병원 현장 시험 사례.
- [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) 트랙 — 단계 4(실행 연결)에 CSS 온톨로지·OPC UA 스킬 실행 프로토콜·능력–실행 연결 구조를 참고하도록 제안한다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-229]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, IDTA 02020 Submodel Template: Capability Description — README (published/Capability Description/1/0), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-29 (원문 미열람)
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-10-18, https://arxiv.org/abs/2406.07962, 접근일 2026-09-29 (원문 미열람)
[^ref-880]: Open Robotics (Programming Multiple Robots with ROS 2), User-defined Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_userdefined.html, 접근일 2026-09-29
[^ref-885]: Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel), HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics, 2025-04-30, https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-08 | 6. 온톨로지 기반 시스템·로봇 연동 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-29-08/pages/topics/2026/2026-09-29-area06-s3.md

```markdown
---
title: "6. 온톨로지 기반 시스템·로봇 연동 — 왜 중요한가"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 6
related_areas: [4, 5, 7, 18, 20, 21, 22, 25, 29, 45, 47, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-038, ref-153, ref-869, ref-880, ref-886]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#3
---

[홈](../../index.md) › [주제](../index.md) › 6. 온톨로지 기반 시스템·로봇 연동 — 왜 중요한가

# 6. 온톨로지 기반 시스템·로봇 연동 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역이 없으면 로봇을 한 대 더 들이거나 새 업무 시스템을 붙일 때마다 사람이 능력 목록을 다시 읽고 어댑터를 손으로 맞추는 일이 반복된다. Vieira da Silva·Köcher·Fay(2022, 2023 개정)는 이기종 자율 로봇 팀에서 각 로봇이 제공하는 기능을 일관되게 기술하는 방법이 없다고 지적하고, 제조업의 능력·스킬 모델링 접근을 자율 로봇에 적용한 능력 모델을 제안했다. [사실][^ref-038]
- 이 페이지는 [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역이 없으면 로봇을 한 대 더 들이거나 새 업무 시스템을 붙일 때마다 사람이 능력 목록을 다시 읽고 어댑터를 손으로 맞추는 일이 반복된다. Vieira da Silva·Köcher·Fay(2022, 2023 개정)는 이기종 자율 로봇 팀에서 각 로봇이 제공하는 기능을 일관되게 기술하는 방법이 없다고 지적하고, 제조업의 능력·스킬 모델링 접근을 자율 로봇에 적용한 능력 모델을 제안했다. [사실][^ref-038]

연동 어댑터는 온톨로지로 자동화할 수 있는 부분과 손작업이 남는 부분으로 나뉜다. Open Robotics 의 [Open-RMF](../../glossary/open-rmf.md) 플릿 어댑터·사용자 정의 작업 문서와 ROS 패키지 색인의 vda5050_connector 는 로봇 연동 어댑터를 '플릿·능력 설정'과 '로봇별 핸들러·API 구현'의 두 부분으로 각각 구성하므로, 설정·매핑은 자동화 대상이고 로봇별 구현은 손작업으로 남는다는 경계가 서로 다른 두 발행 주체에서 확인된다(2026-09-29 확인). [사실][^ref-880][^ref-153][^ref-886]

설비 쪽도 마찬가지다. Valner 외(2022)의 타르투대학교병원 현장 시험에서는 프로그램 제어가 없는 병원 문을 카드 인식·근접 센서를 대신 작동시키는 서보 장치로 보완해야 했다. [사실][^ref-869] 온톨로지와 설정만으로는 연동되지 않는 설비가 남으므로, 2. 핵심 질문의 "손작업 없이"는 커버리지 측정 결과가 나오기 전까지 목표로만 서술한다. [추정][^ref-869]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-038]: Vieira da Silva, L. M., Köcher, A., & Fay, A. (Helmut Schmidt University), A Capability and Skill Model for Heterogeneous Autonomous Robots, 2023-02-09, https://arxiv.org/abs/2209.10900, 접근일 2026-09-29
[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-869]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-29 (원문 미열람)
[^ref-880]: Open Robotics (Programming Multiple Robots with ROS 2), User-defined Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_userdefined.html, 접근일 2026-09-29
[^ref-886]: ROS Index (InOrbit ros_amr_interop, 유지관리자 Leandro Pineda), vda5050_connector - ROS Package Overview, 미확인, https://index.ros.org/p/vda5050_connector/, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-08 | 6. 온톨로지 기반 시스템·로봇 연동 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 875건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 232개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
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
- clarification-question: 명확화 질문 (Clarification Question (Follow-up Clarification))
- coalition-formation: 연합 형성 (Coalition Formation)
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- common-coordinate-system: 공통 좌표계 (Common Coordinate System (CCS, ISO 21423))
- common-data-environment: 공통 데이터 환경 (Common Data Environment (CDE))
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
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
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
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
- robot-task-fitness-matrix: 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)
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
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
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
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [6] 에 걸린 1건 / 전체 150건)

```markdown
- oq-150 [열림] 팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가? (영역 4, 5, 6)
```

### runs/2026-09-29-08/verification2.json

```json
{
  "run_id": "2026-09-29-08",
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
    "overlaps": []
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true,
    "issues": []
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "changelog_entry: '참고문헌 번호 충돌 확인 필요(ref-038·878·880·881·883 …)' 의 'ref-878' 을 'ref-037' 로 고친다 — 1차 판정이 지적한 충돌 번호는 ref-038·ref-037·ref-880·ref-881·ref-883 이며 이 브리프에 ref-878 은 없다. additional_research_requests 마지막 항목의 같은 표기('ref-038·878·880·881·883')도 함께 고친다.",
    "세부영역 페이지 5. 적용 사례 (현장 유형 명시): 타르투대학교병원 표의 '시작 조건' 칸에 있는 'Open-RMF' 를 [Open-RMF](../../glossary/open-rmf.md) 로 링크한다 — 1차 수정 지시 12('Open-RMF 첫 등장은 용어집에 링크')를 3절에서 이행했으나 3절이 주제 페이지로 분리되어 게시되는 세부영역 페이지에서는 5절이 첫 등장이 됐다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 28건, 미확인 0건, 교차 확인 4건(f7·f12·f17·f20; f3 은 두 출처가 같은 CSS 참조 모델 계보라 교차 확인으로 인정하지 않음). 강등: 없음(f12 신뢰도 high → medium). 원문 미열람 출처: 브리프 기준 ref-229·ref-869·ref-465(검증 에이전트는 세 출처를 이번에 직접 열어 내용을 확인했으나 브리프 표시를 올리지 않는다). 주의: 출처 18건 모두 열어 기관·제목이 일치함을 확인했고, ref-888 은 브리프의 KCI 검색형 URL 이 한 번 다른 논문을 반환해 landing URL 로 실재를 확인했다. IDTA 02020 번호는 README 가 아니라 IDTA 다운로드 페이지 검색 결과로 확인했다. HERON(f11)은 임상 배치 없는 시뮬레이션 시나리오이며 배터리·문·승강기 조건을 다루지 않는다. 능력 모델에서 어댑터 설정·핸들러 초안을 자동 생성한 사례와 근거를 함께 돌려주는 후보 질의는 확인되지 않았다(f19·f25 추정). 현장 사례는 병원(시뮬레이션 1, 현장 시험 1)과 기타(오피스 빌딩 시험 환경)뿐이며 제조 공장·물류창고 사례는 없다. 국내 자료는 2011년 KCI 논문 1건. 참고문헌 id ref-038~ref-890 이 같은 날 실행 2026-09-29-07 의 다른 URL 과 충돌하므로 퍼블리셔가 URL 기준으로 합쳐야 한다. 발행 2년 경과 출처(ref-890 2021, ref-887 2021, ref-883 2022, ref-869 2022, ref-888 2011)는 월간 재검증 대상. oq-150 미해결(f28 부분 진전). 정정 요청 없음. 검증 예산: 검색 2회(리서치 17회 포함 19/30), 열람 18회. / 2차 수정 후 재검증. 드리프트 없음, [분류원문] 보존(admonition 세 줄·1절·2절·옛 분류 이력 문단이 시드와 글자 단위로 같음), 섹션 순서 준수(세부영역 13절, 분리 주제 페이지 7건 모두 10절), 링크 유효(docs_tree.txt 가 없어 부록 A 경로·용어집 색인·입력 페이지로만 검사했고, docs/about/scope-boundary.md 와 docs/topics/index.md 의 존재는 확인하지 못함). 1차 수정 지시 13건은 모두 이행됐다(f12 문장 분리, HERON 을 배터리·문·승강기 예로 들지 않음, f3 교차 확인 서술 제거, f10 OWL 표기 제거, f8 문·승강기 문구, f18 재서술, ref-888 URL, ref-883 기관란, 발행일 미확인·원문 미열람 표기, reference_updates URL, 5절 현장 유형 분리, PDDL 풀어쓰기와 용어 3건 신규, oq-150 미해결 유지). 지적 사항: changelog_entry 와 additional_research_requests 의 충돌 번호 'ref-878' 은 'ref-037' 의 오기. 세부영역 페이지에서 3절이 분리되어 Open-RMF 첫 등장(5절)이 용어집 링크 없이 남았다. 분리 주제 페이지 7건은 원 절 내용을 그대로 옮긴 것으로 확인했고 새 주장은 없다. 코드 분리 부산물(수정 지시 대상 아님, 파이프라인 담당 참고): 세부영역 4절의 요약이 '스킬 인터페이스' 항목을 첫 문장에서 잘라 태그·각주가 떨어졌다(전문은 주제 페이지에 [사실][^ref-882] 로 있음). 세부영역 프런트매터 sources 18건 가운데 ref-037·ref-881·ref-883·ref-888 은 분리 뒤 세부영역 본문에서 인용되지 않고 주제 페이지에서만 인용되며, reference_updates[].cited_by 는 세부영역 페이지만 적었으므로 퍼블리셔가 주제 페이지 인용을 함께 반영해야 한다. 표기 의견: OPC UA·SPARQL·API 같은 약어는 페이지에서 풀어 쓰지 않았다. open_question_updates 두 번째 질문은 f8 수정에 맞춰 '문·승강기 조작을 바꿀 수 없을 때' 를 '맡지 않을 때' 로 고쳐 옮겼으며 뜻이 같아 인정한다. changelog 가 말하는 'ref-869 가 대분류 페이지 자료 목록의 OPC 40010-1 과 겹친다' 는 입력에 대분류 페이지가 없어 확인하지 못했다. site_matrix_updates 의 기타 '예외·성과' 칸은 '정량 결과 없음' 서술로 채운 것이므로 퍼블리셔가 매트릭스에 실을지 확인한다. 신뢰도 medium 유지(태그 분포 변화 없음).",
  "retry_reason": null
}
```
